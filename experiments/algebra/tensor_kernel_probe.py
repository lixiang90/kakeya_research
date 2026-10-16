"""Exact finite-dimensional diagnostics for OAI four-dimensional Lemma 6.6.

Uses rational/integer arithmetic only. This is an algebraic check, not a Kakeya
proof. Output includes a nonsingular minor certifying the twisted-cubic quartic
rank; the accompanying note explains why coefficient tests are universal.
"""
from pathlib import Path
from itertools import combinations
from math import factorial, prod
import json
import sympy as sp


def indices(d, r):
    if d == 1:
        return [(r,)]
    return [(a,) + tail for a in range(r, -1, -1)
            for tail in indices(d - 1, r - a)]


def derivative_value(alpha, beta, point):
    if any(a < b for a, b in zip(alpha, beta)):
        return 0
    return prod(factorial(a) // factorial(a - b) * x ** (a - b)
                for a, b, x in zip(alpha, beta, point))


def test_matrix(d, r, copies, points):
    # T(p repeated `copies`, free slots) corresponds, up to nonzero
    # fixed factors, to partial derivatives of order r-copies of F at p.
    cols = indices(d, r)
    rows = [(p, beta) for p in points for beta in indices(d, r - copies)]
    return sp.Matrix([[derivative_value(a, b, p) for a in cols] for p, b in rows])


def coefficient_matrix(d, r, copies):
    # p(t)=(1,t,...,t^(d-1)). Store coefficients of every derivative
    # restricted to the entire curve; each row is (derivative, t-degree).
    cols = indices(d, r)
    betas = indices(d, r - copies)
    degrees = range((d - 1) * copies + 1)
    labels = [(list(b), k) for b in betas for k in degrees]
    matrix = []
    for beta in betas:
        for k in degrees:
            row = []
            for alpha in cols:
                if any(a < b for a, b in zip(alpha, beta)):
                    row.append(0)
                    continue
                degree = sum(j * (a - b) for j, (a, b) in enumerate(zip(alpha, beta)))
                row.append(prod(factorial(a) // factorial(a - b)
                                for a, b in zip(alpha, beta)) if degree == k else 0)
            matrix.append(row)
    return sp.Matrix(matrix), cols, labels


def main():
    out = {"arithmetic": "exact integers/rationals", "sympy": sp.__version__,
           "scope": "finite-dimensional algebra only; no Kakeya dimension claim"}
    for d, count, label in [(3, 7, "conic"), (4, 10, "twisted_cubic")]:
        points = [tuple(t ** j for j in range(d)) for t in range(count)]
        dets = [abs(int(sp.Matrix(c).det())) for c in combinations(points, d)]
        data = {"parameters": list(range(count)), "min_abs_independence_det": min(dets)}
        q = test_matrix(d, 2, 2, points)
        data["quadratic_kernel_dimension"] = q.cols - q.to_DM().rank()
        for r in (3, 4, 5):
            m = test_matrix(d, r, 3, points)
            rank = m.to_DM().rank()
            data[f"rank_{r}_three_copy"] = {"rows": m.rows, "columns": m.cols,
                                              "rank": rank, "kernel_dimension": m.cols - rank}
        m2 = test_matrix(d, 3, 2, points)
        data["cubic_two_copy_kernel_dimension"] = m2.cols - m2.to_DM().rank()
        out[label] = data
    assert [out["conic"][f"rank_{r}_three_copy"]["kernel_dimension"]
            for r in (3, 4, 5)] == [3, 1, 0]
    assert out["twisted_cubic"]["quadratic_kernel_dimension"] == 3
    assert [out["twisted_cubic"][f"rank_{r}_three_copy"]["kernel_dimension"]
            for r in (3, 4, 5)] == [10, 6, 0]

    matrix, columns, labels = coefficient_matrix(4, 4, 3)
    pivot_cols = list(matrix.to_DM().rref()[1])
    pivot_rows = list(matrix[:, pivot_cols].T.to_DM().rref()[1])
    minor = matrix.extract(pivot_rows, pivot_cols)
    determinant = int(minor.det())
    assert len(pivot_cols) == 29 and determinant != 0
    x = sp.symbols("x0:4")
    qs = [x[0]*x[2]-x[1]**2, x[0]*x[3]-x[1]*x[2], x[1]*x[3]-x[2]**2]
    products = [sp.Poly(sp.expand(qs[i]*qs[j]), *x)
                for i in range(3) for j in range(i, 3)]
    basis = sp.Matrix([[f.coeff_monomial(prod(xx ** a for xx, a in zip(x, alpha)))
                        for f in products] for alpha in columns])
    assert basis.to_DM().rank() == 6 and matrix * basis == sp.zeros(40, 6)
    out["quartic_coefficient_certificate"] = {
        "matrix_shape": [matrix.rows, matrix.cols], "rank": 29,
        "row_order": labels, "column_order": [list(a) for a in columns],
        "minor_rows_zero_based": pivot_rows, "minor_columns_zero_based": pivot_cols,
        "minor_determinant": determinant,
        "six_quadric_products_independent_and_in_kernel": True}
    y = sp.symbols("y0:5")
    t = sp.symbols("t")
    determinant_cubic = sp.det(sp.Matrix([[y[0], y[1], y[2]],
                                         [y[1], y[2], y[3]],
                                         [y[2], y[3], y[4]]]))
    vanishing_quadric = y[0]*y[2] - y[1]**2
    quintic = sp.expand(determinant_cubic * vanishing_quadric)
    moment = {v: t**i for i, v in enumerate(y)}
    gradient = [sp.expand(sp.diff(determinant_cubic, v).subs(moment)) for v in y]
    hessian = [[sp.expand(sp.diff(quintic, v, w).subs(moment)) for w in y] for v in y]
    assert all(v == 0 for v in gradient)
    assert all(v == 0 for row in hessian for v in row)
    witness = dict(zip(y, (0, 1, 0, 0, 1)))
    assert determinant_cubic.subs(witness) == -1 and quintic.subs(witness) == 1
    out["ambient_n_at_least_6_obstruction"] = {
        "cubic": str(determinant_cubic), "quadric": str(vanishing_quadric),
        "moment_curve_gradient_identically_zero": True,
        "quintic_hessian_identically_zero": True,
        "nonzero_witness": [0, 1, 0, 0, 1],
        "cubic_witness_value": -1, "quintic_witness_value": 1,
        "scope": "counterexample to naive tensor-lemma extensions, not to Kakeya"}
    path = Path(__file__).with_name("tensor_kernel_probe.json")
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "quartic_coefficient_certificate"}, indent=2))
    print("quartic rank certificate determinant:", determinant)
    print("saved:", path)


if __name__ == "__main__":
    main()
