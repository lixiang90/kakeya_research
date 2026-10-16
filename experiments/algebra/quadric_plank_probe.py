"""Exact identities and a finite-grid lower-bound check; not an all-plank test."""
from pathlib import Path
import json
import sympy as sp

t, s, p, q, h = sp.symbols("t s p q h", real=True)
x, y, z = s+p*t, -s*q-p/s-p*q*t, 1/s+q*t
assert sp.cancel(t*y+x*z-1) == 0
bad = {s: 1+h, q: -p}
xx, yy, zz = [sp.cancel(v.subs(bad, simultaneous=True)) for v in (x, y, z)]
assert sp.cancel(xx+zz-2-h**2/(1+h)) == 0
assert sp.cancel(yy-p*((1+h)-1/(1+h))-p**2*t) == 0
checks = []
for m in (8, 16, 32):
    delta = sp.Rational(1, m*m)
    count = 0
    for i in range(m):
        for j in range(m):
            vals = {h:i*delta, p:j*delta}
            for time in (0, 1):
                a, b, c = [v.subs(vals).subs(t, time) for v in (xx, yy, zz)]
                assert abs(a+c-2) <= delta
                assert abs(b) <= 4*delta
                assert abs(a-c) <= sp.Rational(4, m)
            count += 1
    assert count == m*m
    checks.append(dict(m=m, delta=str(delta), contained_lines=count,
                       density_lower_exponent="delta^-1/2 up to fixed constants"))
out = dict(quadric_identity=True, bad_plank_identities=True, finite_grids=checks,
           scope="Endpoint checks imply whole-time strip containment for affine lines. No all-plank upper bound, Kakeya dimension theorem, or novelty is verified by this code.")
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out))
