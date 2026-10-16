"""Exact symbolic certificates for the R0002 local ruled-cubic obstruction.

No finite numerical sample is promoted to a Kakeya claim. SymPy simplifies
identities in all base points, line times, and direction parameters.
"""
from pathlib import Path
import json
import sympy as sp


def main():
    x = sp.symbols("x0:4")
    theta, tau, eps, scale = sp.symbols("theta tau eps S")
    q = x[0]*x[3] - x[1]*x[2]
    k = x[0]*x[2] - x[1]**2
    r = x[0]*k
    f = scale*(q + eps*r)  # a = S*eps
    invariant = x[2] - 2*theta*x[1] + theta**2*x[0]
    p = sp.Matrix([1, theta, theta**2, theta**3 - eps*invariant])
    along = dict(zip(x, [x[i] + tau*p[i] for i in range(4)]))
    # simultaneous=True is essential: all x are evaluated at the same base point.
    substitute = lambda poly: sp.expand(poly.subs(along, simultaneous=True))
    directional = lambda poly: sp.expand(sum(p[i]*sp.diff(poly, x[i]) for i in range(4)))
    assert directional(invariant) == 0
    assert sp.expand(k.subs(dict(zip(x, p)), simultaneous=True)) == 0
    assert sp.expand(q.subs(dict(zip(x, p)), simultaneous=True) + eps*invariant) == 0
    affine_remainder = sp.expand(substitute(f) - f - tau*directional(f))
    assert affine_remainder == 0
    assert sp.Poly(substitute(r), tau).degree() <= 2

    # The point-dependent direction transformation has determinant one.
    transform = sp.eye(4)
    transform[3, 0] = -eps*x[2]
    transform[3, 1] = 2*eps*x[1]
    transform[3, 2] = -eps*x[0]
    moment = sp.Matrix([1, theta, theta**2, theta**3])
    assert (transform*moment-p).applyfunc(sp.expand) == sp.zeros(4, 1)
    assert transform.det() == 1
    q_matrix = sp.hessian(q, x)/2
    assert q_matrix.det() == sp.Rational(1, 16)

    # Initial x0=0, x=(y1,y2,y3); spatial flow has exactly unit Jacobian.
    y = sp.symbols("y1:4")
    initial_invariant = y[1] - 2*theta*y[0]
    flow = sp.Matrix([y[0]+tau*theta, y[1]+tau*theta**2,
                      y[2]+tau*(theta**3-eps*initial_invariant)])
    assert flow.jacobian(y).det() == 1

    # For every quadratic test P=A_2+(b+l.x)w+c*w^2, isolate its
    # coefficients from P(x,f(x)). A_2 has no effect on degrees >=3.
    a, b, c = sp.symbols("a b c")
    ell = sp.symbols("l0:4")
    graph = scale*q + a*r
    restriction = sp.Poly(sp.expand((b+sum(ell[i]*x[i] for i in range(4)))*graph
                                     + c*graph**2), *x)
    monomials = [x[0]**2*x[2], x[0]**2*x[3], x[0]*x[1]*x[3],
                 x[0]*x[2]*x[3], x[0]*x[3]**2, x[1]**2*x[2]**2]
    expected = [a*b, scale*ell[0], scale*ell[1], scale*ell[2], scale*ell[3], c*scale**2]
    actual = [restriction.coeff_monomial(m) for m in monomials]
    assert actual == expected
    out = {
        "scope": "local algebraic obstruction and finite-grid cap interface only; not a Kakeya counterexample",
        "arithmetic": "symbolic polynomial identities over Q",
        "sympy_version": sp.__version__,
        "q": str(q), "k": str(k), "r": str(r),
        "q_matrix_determinant": str(q_matrix.det()),
        "direction": [str(v) for v in p],
        "invariant": str(invariant),
        "invariant_directional_derivative_zero": True,
        "graph_is_affine_along_each_selected_full_line": True,
        "native_test_is_quadratic_along_each_selected_full_line": True,
        "direction_transform_determinant": 1,
        "spatial_flow_jacobian": 1,
        "quadratic_test_coefficient_certificate": [
            {"monomial": str(m), "coefficient": str(v)} for m, v in zip(monomials, actual)],
        "logical_limits": [
            "Finite-grid joint-cap compatibility requires an epsilon depending on the entire finite grid and deletion of direction-parameter boundary neighborhoods.",
            "No uniform claim over all arbitrarily fine grids is made.",
            "Original-resolution guards, all coefficient lower bounds, and critical-path extremality have not been verified for this model."]
    }
    path = Path(__file__).with_name("ruled_cubic_probe.json")
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    print("All 9 symbolic identity groups passed; nonsingular q, full affine rulings, determinant and coefficient certificates verified.")
    print(path)


if __name__ == "__main__":
    main()
