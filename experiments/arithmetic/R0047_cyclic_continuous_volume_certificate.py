"""Exact finite collision certificates for real whole-clock cyclic tube unions.

Outputs lower bounds for Lebesgue volume of the Euclidean 1/N-neighborhood
of K_N, hence also for the requested C0/N-neighborhood. It never estimates
continuous volume from time samples: each time cell uses an integer collision
upper envelope, then the analytic smoothing/Cauchy argument in the note.
All maps and integer counts are saved. No assertion of uniform CYCL follows.
"""

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


def patterns(n):
    k = n.bit_length()-1
    j = np.arange(n, dtype=np.int64)
    zero = np.zeros(n, dtype=np.int64)
    reverse = np.array([int(f"{a:0{k}b}"[::-1], 2) for a in range(n)], dtype=np.int64)
    weighted = np.array([-sum(((a >> p) & 1)*(p+1)*(1 << p)
                              for p in range(k))//k for a in range(n)], dtype=np.int64)
    rng = np.random.Generator(np.random.PCG64(47000+n))
    return {
        "constant": [zero]*4,
        "affine_positive": [j]*4,
        "affine_negative": [-j]*4,
        "three_quarter_resonance_rounded": [-(3*j//4)]*4,
        "negative_orientation_product": [-j, j, j, j],
        "bit_reversal": [reverse]*4,
        "gray_code": [j ^ (j >> 1)]*4,
        "modular_permutations": [(s*j) % n for s in (3, 5, 7, 9)],
        "random_permutations": [rng.permutation(n).astype(np.int64) for _ in range(4)],
        "weighted_binary_digits": [weighted]*4,
    }


def difference_prefix(b):
    n = len(b)
    j = np.arange(n, dtype=np.int64)
    da = j[:, None]-j[None, :]
    db = b[:, None]-b[None, :]
    h = np.zeros((2*n-1, 4*n+1), dtype=np.int64)
    np.add.at(h, (da.ravel()+n-1, db.ravel()+2*n), 1)
    assert int(h.sum()) == n*n
    return np.concatenate([np.zeros((2*n-1, 1), dtype=np.int64),
                           np.cumsum(h, axis=1)], axis=1)


def transfer(prefix, numerator, denominator, n):
    m = np.zeros((2*n-1, 2*n-1), dtype=np.int64)
    for row, d in enumerate(range(1-n, n)):
        # For t in [j/Q,(j+1)/Q], |t*d+db| <= 1 implies
        # |j*d+Q*db| <= Q+|d|. This is an upper envelope, not quadrature.
        radius = denominator+abs(d)
        lo = max(-2*n, -((radius+numerator*d)//denominator))
        hi = min(2*n, (radius-numerator*d)//denominator)
        if lo <= hi:
            m[row, :] = prefix[:, hi+2*n+1]-prefix[:, lo+2*n]
    return m


def direct_pair_counts(maps, q):
    """Independent direct direction-pair count; only used for n=4."""
    n = len(maps[0])
    a = np.array(list(itertools.product(range(n), repeat=4)), dtype=np.int64)
    d = a[:, None, :]-a[None, :, :]
    b = np.column_stack([maps[i][a[:, (i+1) % 4]] for i in range(4)])
    db = b[:, None, :]-b[None, :, :]
    return [int(np.all(np.abs(j*d+q*db) <= q+np.abs(d), axis=2).sum())
            for j in range(q//2, q)]


def run(n, name, maps):
    assert n in (4, 8, 16, 32, 64) and n & (n-1) == 0
    assert all(len(b) == n and np.max(np.abs(b)) <= n for b in maps)
    # Each trace counts a subset of n^8 original ordered direction pairs.
    # Every nonnegative intermediate entry is at most n^8 as well.
    assert n**8 < np.iinfo(np.int64).max
    prefixes = [difference_prefix(b) for b in maps]
    q = n
    counts = []
    for j in range(q//2, q):
        matrices = [transfer(p, j, q, n) for p in prefixes]
        count = int(np.trace(matrices[0] @ matrices[1] @ matrices[2] @ matrices[3]))
        assert n**4 <= count <= n**8
        counts.append(count)
    direct_verified = None
    if n == 4:
        assert direct_pair_counts(maps, q) == counts
        direct_verified = True
    total = sum(counts)  # Python int, not an overflowing NumPy reduction.
    lower = Fraction(q*n**4, 4*total)
    return {"name": name, "N": n, "Q": q, "maps_integer_indices": [b.tolist() for b in maps],
            "clock": ["1/2", "1"], "time_cells": q//2,
            "collision_upper_counts": counts, "sum_collision_upper_counts": total,
            "volume_lower_exact_numerator": lower.numerator,
            "volume_lower_exact_denominator": lower.denominator,
            "volume_lower_display": float(lower),
            "continuous_time_cell_envelope": True,
            "small_N_direct_pair_recount": direct_verified}


def main():
    records = [run(n, name, maps) for n in (4, 8, 16, 32, 64)
               for name, maps in patterns(n).items()]
    report = {"round": "R0047", "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "arithmetic": "exact int64 within proved n^8 bound; Python integers/Fraction for totals",
              "numpy_version": np.__version__,
              "scope": "50 explicit finite cyclic families; real continuous-time neighborhood LOWER certificates only",
              "target_radius": "1/N (Euclidean), so also applies to C0/N for fixed C0>=10",
              "certificate": "volume >= Q*N^4/(4*sum(time-cell collision upper traces))",
              "universal_CYCL_proved": False, "asymptotic_power_upper_constructed": False,
              "Kakeya_counterexample": False, "records": records}
    target = Path(__file__).parent / "outputs/R0047_continuous_volume_certificates.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps({"round": "R0047", "families": len(records),
                      "small_N_direct_pair_recounts": sum(r["small_N_direct_pair_recount"] is True for r in records),
                      "min_certified_lower": min(r["volume_lower_display"] for r in records),
                      "universal_CYCL_proved": False, "power_upper_constructed": False}))


if __name__ == "__main__":
    main()
