"""R0003 exact certificates: full coefficient density and observed-list map.

This does not certify cap-class membership, horizon, or a critical path.
"""
from pathlib import Path
import json
import sympy as sp


def main():
    y1, y2, y3, theta, c, z2, z3, zw = sp.symbols("y1 y2 y3 theta c z2 z3 zW")
    beta, rho, t = sp.symbols("beta rho t")
    kappa = beta*rho
    invariant = y2-2*theta*y1
    v1 = theta
    v2 = theta**2+z2
    v3 = theta**3-rho*invariant+z3
    w0 = -beta*y1*y2+c
    w1 = beta*(y3-theta*y2-theta**2*y1)-kappa*y1**2+zw
    inputs = (y1, y2, y3, theta, c, z2, z3, zw)
    outputs = sp.Matrix([y1, y2, y3, v1, v2, v3, w0, w1])
    jacobian = sp.expand(outputs.jacobian(inputs).det())
    assert jacobian == 1
    x, y, z = y1+t*v1, y2+t*v2, y3+t*v3
    signal = sp.Poly(sp.expand(w0+t*w1-beta*(t*z-x*y)), t)
    expected = [c, -kappa*y1**2+beta*y1*z2+zw,
                kappa*invariant+beta*(theta*z2-z3)]
    assert [signal.nth(i) for i in range(3)] == [sp.expand(v) for v in expected]
    assert signal.degree() <= 2
    assert sp.expand(v2-v1**2) == z2
    spatial_jacobian = sp.Matrix([x, y, z]).jacobian([y1,y2,y3]).det()
    assert spatial_jacobian == 1
    # Projection of observed coefficients recovers (initial position,theta,c)
    # exactly when noises vanish, giving the uniform inverse Lipschitz map.
    exact_signal = [sp.expand(v.subs({z2:0,z3:0,zw:0})) for v in expected]
    assert exact_signal == [c, -kappa*y1**2, kappa*y2-2*kappa*theta*y1]
    out = {
        "scope": "finite-grid prior and list identities; no full critical-path or Kakeya claim",
        "sympy_version": sp.__version__,
        "parameters": {"beta":"S/h^2", "rho":"a/(S h)", "kappa":"beta*rho=a/h^3"},
        "required_uniform_list_regime": "0<kappa<=1 and 0<rho<=1 on fixed bounded parameter boxes",
        "full_coefficient_map_jacobian": int(jacobian),
        "spatial_flow_jacobian": int(spatial_jacobian),
        "full_coefficient_order": [str(v) for v in outputs],
        "input_order": [str(v) for v in inputs],
        "native_signal_coefficients": [str(sp.expand(v)) for v in expected],
        "visible_polynomial_defect": "V2-V1^2=z2",
        "exact_model_inverse_projection": ["Y0", "V1=theta", "X0=c"],
        "noise_condition": "(1+beta)*eta much smaller than every prepared mesh and required witness tolerance",
        "not_verified": ["complete original Kakeya provenance", "membership of the full cap class", "positive horizon", "critical path extremality"]
    }
    path=Path(__file__).with_name("tempered_prior_probe.json")
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    print("Exact checks passed: full 8-coordinate Jacobian=1; native X coefficient formula; flow Jacobian=1; inverse projection.")
    print(path)


if __name__=="__main__":
    main()
