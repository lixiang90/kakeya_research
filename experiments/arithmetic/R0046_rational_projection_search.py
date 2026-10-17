"""Bounded, exact subset search for R0046; never a universal proof.

Usage: python experiments/arithmetic/R0046_rational_projection_search.py
The ten grids are adjugate images of {0,1,2,3}^2 under pairs of the
five relevant forms. All comparisons use Python integers. A strict
failure would need the separate tensor argument in the research note.
"""

import hashlib
import itertools
import json
from pathlib import Path


FORMS = ((1, 0), (1, 1), (-1, 1), (0, 1), (1, 3))
NAMES = ("x", "x+y", "-x+y", "y", "x+3y")
GRID_SIDE = 4


def certificate(points):
    """Independent direct count, also used to check every reported witness."""
    points = sorted(set(map(tuple, points)))
    fibres = {}
    for x, y in points:
        fibres.setdefault(x, set()).add(y)
    m = max(map(len, fibres.values()))
    sizes = [len({a*x+b*y for x, y in points}) for a, b in FORMS[1:]]
    n = len(points)
    left = n**21
    right = m**7 * (sizes[0]*sizes[1]*sizes[2])**10 * sizes[3]**5
    return {"points": points, "N": n, "M": m, "projection_sizes": sizes,
            "left_N21": left, "right_M7_P10_S4_5": right,
            "strict_failure": left > right}


def search_grid(i, j):
    a, b = FORMS[i]
    c, d = FORMS[j]
    det = a*d-b*c
    assert det != 0
    # Selected forms have values det*u, det*v, so no rational rounding occurs.
    points = [(d*u-b*v, -c*u+a*v)
              for u in range(GRID_SIDE) for v in range(GRID_SIDE)]
    assert len(set(points)) == GRID_SIDE**2
    values = [[p*x+q*y for p, q in FORMS] for x, y in points]
    counts = [{} for _ in FORMS]
    sizes = [0]*len(FORMS)
    row_histogram = [0]*(len(points)+1)
    m = 0
    n = 0
    previous_gray = 0
    covered_by_old_bound = 0
    tested_outside_old_region = 0
    best = None
    failure = None
    for step in range(1, 1 << len(points)):
        gray = step ^ (step >> 1)
        bit = (gray ^ previous_gray).bit_length()-1
        delta = 1 if gray & (1 << bit) else -1
        row = values[bit][0]
        old_row = counts[0].get(row, 0)
        if old_row:
            row_histogram[old_row] -= 1
        new_row = old_row+delta
        if new_row:
            row_histogram[new_row] += 1
        for k, value in enumerate(values[bit]):
            old = counts[k].get(value, 0)
            new = old+delta
            if new:
                counts[k][value] = new
            else:
                del counts[k][value]
            sizes[k] += int(new > 0)-int(old > 0)
        n += delta
        m = max(m, new_row)
        while m and row_histogram[m] == 0:
            m -= 1
        left = n**21
        right = m**7 * (sizes[1]*sizes[2]*sizes[3])**10 * sizes[4]**5
        if n <= m*m:
            covered_by_old_bound += 1
        else:
            tested_outside_old_region += 1
            if best is None or left*best[1] > best[0]*right:
                best = (left, right, gray)
        if left > right:
            failure = certificate([p for k, p in enumerate(points) if gray & (1 << k)])
            assert failure["strict_failure"]
            break
        previous_gray = gray
    best_certificate = None
    if best:
        best_certificate = certificate([p for k, p in enumerate(points)
                                        if best[2] & (1 << k)])
        assert best_certificate["left_N21"] == best[0]
        assert best_certificate["right_M7_P10_S4_5"] == best[1]
    return {"selected_forms": [NAMES[i], NAMES[j]], "determinant": det,
            "grid_points": points, "nonempty_subsets_examined": step,
            "N_le_M_squared": covered_by_old_bound,
            "N_gt_M_squared": tested_outside_old_region,
            "best_outside_old_region": best_certificate, "strict_failure": failure}


def main():
    grids = []
    for i, j in itertools.combinations(range(len(FORMS)), 2):
        result = search_grid(i, j)
        grids.append(result)
        if result["strict_failure"]:
            break
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = {"round": "R0046", "arithmetic": "exact Python integers",
              "script_sha256": source_hash, "grid_side": GRID_SIDE,
              "scope": "All nonempty subsets of each explicitly listed 16-point integer grid; grids may overlap",
              "candidate": "N^21 <= M^7 (S1*S2*S3)^10 S4^5",
              "universal_inequality_proved": False, "Kakeya_counterexample": False,
              "total_subsets_examined": sum(g["nonempty_subsets_examined"] for g in grids),
              "strict_failure_found": any(g["strict_failure"] is not None for g in grids),
              "grids": grids}
    target = Path(__file__).parent / "outputs/R0046_search.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in output.items() if k != "grids"}))


if __name__ == "__main__":
    main()
