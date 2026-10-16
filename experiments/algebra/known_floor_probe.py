"""Exact identities for R0004's d=1 boundary model; no critical-path claim."""
import json
from pathlib import Path
import sympy as sp

th, z, v3, slope_w, e1, e2, y03, w0 = sp.symbols(
    'theta z v3 W e1 e2 y03 w0', real=True
)
t, t0, tau, th0, s, z0, r = sp.symbols('t t0 tau theta0 s z0 r', real=True)
v2 = th**2 + z
inputs = sp.Matrix([th, z, v3, slope_w, e1, e2, y03, w0])
coeffs = sp.Matrix([v2 + e1, th + e2, y03, th, v2, v3, w0, slope_w])
coefficient_jacobian = sp.factor(coeffs.jacobian(inputs).det())
assert abs(coefficient_jacobian) == 1

y1 = v2 + t * th + e1
y2 = th + t * v2 + e2
base_jacobian = sp.factor(sp.Matrix([y1, y2]).jacobian([th, z]).det())
assert sp.simplify(base_jacobian - (t**2 - 1)) == 0

# Ignoring the small intercept noise, the exact point recovers both slopes.
theta_hat = sp.cancel((y2 - t * y1) / (1 - t**2))
v2_hat = sp.cancel((y1 - t * y2) / (1 - t**2))
assert sp.simplify(theta_hat - th - (e2 - t*e1)/(1-t**2)) == 0
assert sp.simplify(v2_hat - v2 - (e1 - t*e2)/(1-t**2)) == 0

sub = {th: th0+s, z: z0+r, t: t0+tau}
center = sp.Matrix([th0**2+z0+(t0+tau)*th0,
                    th0+(t0+tau)*(th0**2+z0)])
offset = sp.simplify(sp.Matrix([y1, y2]).subs(sub) - center)
tangent = sp.Matrix([2*th0+t0, 1+2*th0*t0])
normal = sp.Matrix([-(1+2*th0*t0), 2*th0+t0])
chart_determinant = sp.factor(sp.Matrix.hstack(tangent, sp.Matrix([1,t0])).det())
assert sp.simplify(chart_determinant - (t0**2-1)) == 0
remainder = sp.simplify(offset - tangent*s)
expected = sp.Matrix([tau*s+s*s+r+e1,
                      2*th0*tau*s+(t0+tau)*(s*s+r)+e2])
assert sp.simplify(remainder - expected) == sp.zeros(2, 1)
normal_error = sp.expand((normal.T * offset)[0])
normal_expected = ((4*th0**2-1)*tau*s
                   + (t0**2-1+(2*th0+t0)*tau)*(s*s+r)
                   - (1+2*th0*t0)*e1 + (2*th0+t0)*e2)
assert sp.simplify(normal_error - normal_expected) == 0

# R0004's cancellation, under the stated true-saturation comparison.
J, q, n, kvis, eta = sp.symbols('J q n Kvis eta', positive=True)
assert sp.cancel((kvis*eta*J/q**3)/(n*J)) == kvis*eta/(n*q**3)

result = {
    'scope': 'exact algebra for pointwise-known true packets at d=1; no horizon or Kakeya claim',
    'sympy_version': sp.__version__,
    'full_coefficient_jacobian': str(coefficient_jacobian),
    'fixed_time_visible_base_jacobian': str(base_jacobian),
    'point_inverse_denominator': '1-t^2 >= 3/4 on 0<=t<=1/2',
    'chart_tangent': [str(x) for x in tangent],
    'chart_remainder': [str(x) for x in expected],
    'normal_error': str(sp.expand(normal_expected)),
    'required_widths': 'q^2 <= eta <= q; intercept noise much smaller than eta',
    'chart_2d_determinant_factor': str(chart_determinant),
    'packet_scaling': 'J comparable to q^2*eta, nu_packet comparable to q^3*eta=a*J when a=q',
    'true_floor_direction_ratio': str(kvis*eta/(n*q**3)),
    'not_verified': ['d<1', 'positive horizon', 'critical extremality', 'Kakeya counterexample'],
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps(result, ensure_ascii=False))
