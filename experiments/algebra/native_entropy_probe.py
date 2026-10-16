"""R0005 exact native inverse and finite-bin transfer identities.

The script checks the algebra covered here; it does not certify a critical
Kakeya model or prove a Hausdorff bound.
"""
import json
from pathlib import Path
import sympy as sp

t, S = sp.symbols('t S', positive=True)
y1,y2,y3,v1,v2,c,e1,e2 = sp.symbols('y1 y2 y3 v1 v2 c e1 e2',real=True)
inputs=sp.Matrix([y1,y2,y3,v1,v2,c,e1,e2])
v3=-e2/S
slope_w=S*y3+e1
coefficients=sp.Matrix([y1,y2,y3,v1,v2,v3,c,slope_w])
jac=sp.factor(coefficients.jacobian(inputs).det())
assert sp.simplify(abs(jac)-1/S)==0
Y3=y3+t*v3
w=c+t*slope_w
X=sp.expand(w-S*t*Y3)
assert sp.simplify(X-(c+e1*t+e2*t*t))==0
assert sp.simplify(slope_w-(S*Y3+e1+t*e2))==0

# A more general bilinear quadratic shear, used in the mass bound.
W,w0,V3,beta=sp.symbols('W w0 V3 beta',real=True)
Y1=y1+t*v1
Y2=y2+t*v2
Y3b=y3+t*V3
Xb=sp.Poly(sp.expand(w0+t*W-beta*(t*Y3b-Y1*Y2)),t)
native_coeffs=[sp.factor(Xb.nth(k)) for k in range(3)]
expected=[w0+beta*y1*y2,
          W-beta*(y3-y1*v2-y2*v1),
          beta*(v1*v2-V3)]
assert all(sp.simplify(a-b)==0 for a,b in zip(native_coeffs,expected))

# Integer bit counts for the two-scale counterexample with no mixed cap.
finite=[]
for m in range(1,7):
    fine_mass=sp.Rational(1,2)**(10*m)
    coarse_mass=sp.Rational(1,2)**(5*m)
    p=sp.Rational(1,2)**(4*m)
    r=sp.Rational(1,2)**(2*m)
    assert fine_mass==p**sp.Rational(5,2)
    assert coarse_mass==r**sp.Rational(5,2)
    E_fine_bits=2*m
    E_coarse_bits=m
    transfer_bits=m
    conditional_rate_bits=2*m
    assert conditional_rate_bits==E_fine_bits-E_coarse_bits+transfer_bits
    assert p**2/(p**2*r**sp.Rational(1,2))==2**m
    finite.append({'m':m,'E_fine_bits':E_fine_bits,'E_coarse_bits':E_coarse_bits,
                   'transfer_bits':transfer_bits,'mixed_cap_violation_factor':2**m})

result={
 'scope':'exact polynomial identities and finite-bin counts; no critical or Kakeya claim',
 'sympy_version':sp.__version__,
 'simple_full_coefficient_jacobian':str(jac),
 'simple_native_signal':str(X),
 'exact_point_inverse':'W=S*Y3+e1+t*e2',
 'bin_inverse_loss':'conditional y03 p-cell remains uniform; W_p max atom <=1/S',
 'required_old_affine_mesh':'p/S, unless exact current base is conditioned upon',
 'bilinear_native_coefficients':[str(x) for x in native_coeffs],
 'finite_bin_counterexamples':finite,
 'not_certified':['positive critical horizon','full raw slope subpower density','general Kakeya bound'],
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result,ensure_ascii=False))
