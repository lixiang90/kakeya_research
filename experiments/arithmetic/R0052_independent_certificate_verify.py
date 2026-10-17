"""Independent exact aggregation and rational log enclosures for R0052.

No optimizer, external numerical package, source notebook execution, or root
aggregation code is used. Input: {"joint_integer_weights": [[a,b,count], ...]}.
The output certifies the finite law and exact factorial type-cardinality
comparison. Type-image surjectivity and graph/tensor realization remain a
separate mathematical responsibility.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


TERMS = 48
SCALE = 10**48


def atanh_log_bounds(z: Fraction) -> tuple[Fraction, Fraction]:
    """Enclose log((1+z)/(1-z)), for 0 <= z <= 1/3.

    The omitted positive terms are bounded by replacing every denominator
    2*j+1, j>=TERMS, with 2*TERMS+1 and summing the geometric series.
    """
    if not 0 <= z <= Fraction(1, 3):
        raise ValueError("range-reduction invariant failed")
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(TERMS):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    tail = 2 * power / ((2 * TERMS + 1) * (1 - z2))
    return lower, lower + tail


LN2_LOWER, LN2_UPPER = atanh_log_bounds(Fraction(1, 3))


def integer_floor(x: Fraction) -> int:
    return x.numerator // x.denominator


def integer_ceil(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


@lru_cache(maxsize=None)
def integer_log_bounds(n: int) -> tuple[int, int]:
    """Outward integer endpoints, in units of SCALE^-1, for natural log n."""
    if type(n) is not int or n <= 0:
        raise ValueError("log argument must be a positive integer")
    k = n.bit_length() - 1
    p2 = 1 << k
    z = Fraction(n - p2, n + p2)
    lo, hi = atanh_log_bounds(z)
    lo += k * LN2_LOWER
    hi += k * LN2_UPPER
    return integer_floor(lo * SCALE), integer_ceil(hi * SCALE)


def read_integer_law(path: Path) -> tuple[dict, list[tuple[int, int, int]]]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    raw_rows = obj["joint_integer_weights"]
    rows = []
    seen = set()
    for row in raw_rows:
        if not isinstance(row, list) or len(row) != 3:
            raise ValueError("each row must have exactly [a,b,count]")
        a, b, count = row
        if any(type(v) is not int for v in row) or count <= 0:
            raise ValueError("integer coordinates and strictly positive counts required")
        if (a, b) in seen:
            raise ValueError("duplicate support pair is forbidden")
        seen.add((a, b))
        rows.append((a, b, count))
    if not rows:
        raise ValueError("empty probability law")
    return obj, sorted(rows)


def aggregate(rows: list[tuple[int, int, int]], coefficients: tuple[int, int]):
    """Sort actual integer images, then group equal adjacent images."""
    c, d = coefficients
    images = sorted((c * a + d * b, weight) for a, b, weight in rows)
    return [
        (value, sum(weight for _, weight in group))
        for value, group in itertools.groupby(images, key=lambda pair: pair[0])
    ]


def entropy_bounds(marginal, total: int) -> tuple[Fraction, Fraction]:
    if sum(count for _, count in marginal) != total:
        raise ValueError("marginal mass mismatch")
    if len(marginal) == 1:
        return Fraction(0), Fraction(0)
    qlo, qhi = integer_log_bounds(total)
    sum_lo = sum(count * integer_log_bounds(count)[0] for _, count in marginal)
    sum_hi = sum(count * integer_log_bounds(count)[1] for _, count in marginal)
    denominator = total * SCALE
    return (
        Fraction(total * qlo - sum_hi, denominator),
        Fraction(total * qhi - sum_lo, denominator),
    )


def linear_bounds(bounds, coefficients) -> tuple[Fraction, Fraction]:
    lo, hi = Fraction(0), Fraction(0)
    for name, coefficient in coefficients.items():
        left, right = bounds[name]
        lo += coefficient * (left if coefficient >= 0 else right)
        hi += coefficient * (right if coefficient >= 0 else left)
    return lo, hi


def scaled_interval(bounds, decimal_places=30):
    scale = 10**decimal_places
    lo, hi = bounds
    return {
        "lower_numerator": str(integer_floor(lo * scale)),
        "upper_numerator": str(integer_ceil(hi * scale)),
        "common_denominator": str(scale),
        "strictly_positive": lo > 0,
    }


def factor_integer(n: int) -> dict[int, int]:
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def exact_weighted_ratio(marginals, total: int) -> dict:
    """Derive exp(total*weighted_gap) from the input counts, not a supplied formula."""
    exponents = {}

    def add_power(integer, power):
        for prime, multiplicity in factor_integer(integer).items():
            exponents[prime] = exponents.get(prime, 0) + power * multiplicity

    coefficients = {"D": 21, "A": -10, "B": -10, "A_plus_B": -10, "A_plus_2B": -5}
    add_power(total, sum(coefficients.values()) * total)
    for name, coefficient in coefficients.items():
        for _, count in marginals[name]:
            add_power(count, -coefficient * count)
    exponents = {prime: exponent for prime, exponent in sorted(exponents.items()) if exponent}
    numerator = math.prod(prime**exponent for prime, exponent in exponents.items() if exponent > 0)
    denominator = math.prod(prime**(-exponent) for prime, exponent in exponents.items() if exponent < 0)
    return {
        "prime_exponents": {str(p): e for p, e in exponents.items()},
        "numerator": str(numerator),
        "denominator": str(denominator),
        "numerator_strictly_larger": numerator > denominator,
    }


def integer_digest(n: int) -> dict:
    return {"bit_length": n.bit_length(), "sha256_unsigned_big_endian": hashlib.sha256(
        n.to_bytes((n.bit_length() + 7) // 8, "big")).hexdigest()}


def exact_type_test(rows, marginals, total: int, multiplier: int) -> dict:
    if type(multiplier) is not int or multiplier <= 0:
        raise ValueError("positive integer type_multiplier required")
    n = multiplier * total

    def multinomial(counts):
        numerator = math.factorial(n)
        denominator = math.prod(math.factorial(multiplier * count) for count in counts)
        quotient, remainder = divmod(numerator, denominator)
        if remainder:
            raise ValueError("nonintegral multinomial")
        return quotient

    n_target = multinomial([count for _, count in marginals["D"]])
    n_joint = multinomial([count for _, _, count in rows])
    controls = {name: multinomial([count for _, count in marginals[name]])
                for name in ("A", "B", "A_plus_B", "A_plus_2B")}
    left = n_target**21
    right = (controls["A"] * controls["B"] * controls["A_plus_B"])**10 * controls["A_plus_2B"]**5
    support_d_injective = len(marginals["D"]) == len(rows)
    if support_d_injective and n_joint != n_target:
        raise ValueError("injective D support but type counts disagree")
    return {
        "type_multiplier": multiplier,
        "word_length": n,
        "target_type_count": str(n_target),
        "joint_type_count": str(n_joint),
        "controlled_marginal_type_cardinality_upper_bounds": {k: str(v) for k, v in controls.items()},
        "difference_is_injective_on_single_coordinate_support": support_d_injective,
        "joint_type_equals_target_type_count": n_joint == n_target,
        "left_N_power_21": integer_digest(left),
        "right_controlled_product": integer_digest(right),
        "exact_finite_C1_defect_positive": left > right,
        "ratio_lower_bound_exceeds_two_to_39": left > (right << 39),
        "warning": "Controlled type counts are safe projection upper bounds. "
                   "No unproved equality of actual projection sets with these bounds is used.",
    }


def verify(path: Path) -> dict:
    obj, rows = read_integer_law(path)
    total = sum(row[2] for row in rows)
    for key in ("total_weight", "Q"):
        if key in obj and obj[key] != total:
            raise ValueError("declared total weight mismatch")
    forms = {"D": (1, -1), "A": (1, 0), "B": (0, 1),
             "A_plus_B": (1, 1), "A_plus_2B": (1, 2)}
    marginals = {name: aggregate(rows, coefficients) for name, coefficients in forms.items()}
    bounds = {name: entropy_bounds(marginal, total) for name, marginal in marginals.items()}
    sd_gaps = {
        name: linear_bounds(bounds, {"D": 3, name: -5})
        for name in forms if name != "D"
    }
    weighted_gap = linear_bounds(bounds, {
        "D": 21, "A": -10, "B": -10, "A_plus_B": -10, "A_plus_2B": -5})
    integer_ratio = exact_weighted_ratio(marginals, total)
    type_test = exact_type_test(rows, marginals, total, obj["type_multiplier"])
    if (weighted_gap[0] > 0) != integer_ratio["numerator_strictly_larger"]:
        raise ValueError("rational-log and exact-integer entropy sign tests disagree")

    # Independently check the four forms after the exact invertible change
    # x=b-a, y=a+b, including their multiplicities under the probability law.
    transformed = [(b - a, a + b, weight) for a, b, weight in rows]
    transformed_forms = {
        "A": (-1, 1), "B": (1, 1), "A_plus_B": (0, 1), "A_plus_2B": (1, 3)}
    multipliers = {"A": 2, "B": 2, "A_plus_B": 1, "A_plus_2B": 2}
    for name, coefficients in transformed_forms.items():
        actual = aggregate(transformed, coefficients)
        expected = [(multipliers[name] * value, count) for value, count in marginals[name]]
        if actual != expected:
            raise ValueError("transformed projection identity failed: " + name)

    return {
        "round": "R0052",
        "verifier": "independent_sorted_groupby_and_exact_rational_atanh_bounds",
        "input_path": path.as_posix(),
        "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "support_size": len(rows),
        "total_integer_weight": str(total),
        "source_notebook_executed": False,
        "root_aggregation_imported": False,
        "log_method": {
            "base": "natural",
            "atanh_terms": TERMS,
            "per_log_outward_scale": str(SCALE),
            "range_reduction": "n=2^k*(1+z)/(1-z), 0<=z<1/3; ln2 uses z=1/3",
            "tail_bound": "2*z^(2*TERMS+1)/((2*TERMS+1)*(1-z^2))",
        },
        "marginals": {
            name: {"integer_values_and_counts": [[v, str(c)] for v, c in marginal],
                   "natural_entropy_interval": scaled_interval(bounds[name])}
            for name, marginal in marginals.items()
        },
        "three_HD_minus_five_Hcontrolled": {
            name: scaled_interval(interval) for name, interval in sd_gaps.items()},
        "all_four_SD_gaps_strictly_positive": all(lo > 0 for lo, _ in sd_gaps.values()),
        "weighted_gap_21HD_minus_10HA_HB_HAplusB_minus_5HAplus2B": scaled_interval(weighted_gap),
        "weighted_gap_strictly_positive": weighted_gap[0] > 0,
        "exact_integer_weighted_entropy_ratio": integer_ratio,
        "exact_finite_type_test": type_test,
        "four_transformed_projection_laws_exactly_checked": True,
        "scope": "This finite integer law, rigorous entropy bounds and exact factorial type counts. "
                 "Type surjectivity, M=1 selector, integer graph and all-C tensor proof are separate.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path(
        "experiments/arithmetic/outputs/R0052_independent_verification.json"))
    args = parser.parse_args()
    result = verify(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8", newline="\n")
    print(json.dumps({key: result[key] for key in (
        "support_size", "total_integer_weight", "input_sha256",
        "weighted_gap_strictly_positive", "all_four_SD_gaps_strictly_positive")},
        ensure_ascii=False))
    if not result["weighted_gap_strictly_positive"]:
        raise SystemExit("No strict weighted entropy certificate was verified.")
    if not result["exact_finite_type_test"]["exact_finite_C1_defect_positive"]:
        raise SystemExit("The supplied type multiplier does not certify a finite C=1 defect.")


if __name__ == "__main__":
    main()
