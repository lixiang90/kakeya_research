"""Exact integer certificate for the fixed R0046 arithmetic candidate.

The finite type classes are specified by their counts, not enumerated.
The proof of graph/encoding/tensor transfer is in the accompanying notes.
No floating-point value is used for any mathematical decision.
"""
from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


INPUT = Path("experiments/arithmetic/inputs/R0052_rational_counterlaw.json")
OUTPUT = Path("experiments/arithmetic/outputs/R0052_exact_countercertificate.json")


def multinomial(counts: list[int]) -> int:
    numerator = math.factorial(sum(counts))
    denominator = math.prod(math.factorial(c) for c in counts)
    answer, remainder = divmod(numerator, denominator)
    if remainder:
        raise ArithmeticError("multinomial was not integral")
    return answer


def main() -> None:
    obj = json.loads(INPUT.read_text(encoding="utf-8"))
    rows = obj["joint_integer_weights"]
    if not rows or any(len(row) != 3 or any(type(v) is not int for v in row)
                       or row[2] <= 0 for row in rows):
        raise ValueError("expected nonempty positive integer joint law")
    if len({(a, b) for a, b, _ in rows}) != len(rows):
        raise ValueError("duplicate joint pair")
    q = sum(w for _, _, w in rows)
    if obj["Q"] != q:
        raise ValueError("wrong declared normalization")
    coefficients = {"D": (1, -1), "A": (1, 0), "B": (0, 1),
                    "A_plus_B": (1, 1), "A_plus_2B": (1, 2)}
    marginals = {}
    for name, (c, d) in coefficients.items():
        counts = Counter()
        for a, b, w in rows:
            counts[c * a + d * b] += w
        marginals[name] = dict(sorted(counts.items()))
    if len(marginals["D"]) != len(rows):
        raise ValueError("this explicit graph certificate requires unique D on support")
    products = {name: math.prod(c**c for c in marginal.values())
                for name, marginal in marginals.items()}
    lhs = (products["A"] * products["B"] * products["A_plus_B"])**10 \
        * products["A_plus_2B"]**5
    rhs = q**(14 * q) * products["D"]**21
    entropy_ratio = Fraction(lhs, rhs)
    simple_ratio = Fraction(5**100, 2**140 * 3**54)
    if entropy_ratio != simple_ratio or lhs <= rhs:
        raise ArithmeticError("strict weighted entropy certificate failed")
    # The stronger, unnecessary four-slope SD target fails for this law.
    strong_sd = {
        name: products[name]**5 > q**(2*q) * products["D"]**3
        for name in coefficients if name != "D"}
    k = obj["type_multiplier"]
    if type(k) is not int or k <= 0:
        raise ValueError("positive integer type multiplier required")
    type_counts = {name: [k*c for c in marginal.values()]
                   for name, marginal in marginals.items()}
    sizes = {name: multinomial(cs) for name, cs in type_counts.items()}
    finite_lhs = sizes["D"]**21
    finite_rhs = (sizes["A"] * sizes["B"] * sizes["A_plus_B"])**10 \
        * sizes["A_plus_2B"]**5
    if finite_lhs <= finite_rhs:
        raise ArithmeticError("finite type cardinality certificate failed")
    transformed = [(b-a, a+b, w) for a, b, w in rows]
    # All simultaneous scalar word values lie in [-L,L]. Base 2L+2
    # is injective there, including on the original x and y word sets.
    all_scalars = [v for x, y, _ in transformed
                   for v in (x, y, x+y, -x+y, x+3*y)]
    bound = max(abs(v) for v in all_scalars)
    output = {
        "round": "R0052", "input": INPUT.as_posix(),
        "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "Q": q, "support_size": len(rows), "D_injective_on_support": True,
        "marginals": {name: [[v, c] for v, c in marginal.items()]
                      for name, marginal in marginals.items()},
        "entropy_product_ratio": {"numerator": str(entropy_ratio.numerator),
                                  "denominator": str(entropy_ratio.denominator),
                                  "formula": "5^100/(2^140*3^54)",
                                  "strictly_above_one": True},
        "three_HD_gt_five_Hcontrolled": strong_sd,
        "all_four_strong_SD_tests_pass": all(strong_sd.values()),
        "type_multiplier": k, "type_length": k*q,
        "type_counts": type_counts,
        "type_cardinalities_or_projection_upper_bounds": {
            name: str(size) for name, size in sizes.items()},
        "graph_maximum_x_fibre": 1,
        "finite_N21_gt_product_K_strict": True,
        "finite_left_bit_length": finite_lhs.bit_length(),
        "finite_right_bit_length": finite_rhs.bit_length(),
        "finite_integer_difference_sha256": hashlib.sha256(
            str(finite_lhs-finite_rhs).encode("ascii")).hexdigest(),
        "simultaneous_scalar_coordinate_bound": bound,
        "integer_encoding_base": 2*bound+2,
        "word_sets_enumerated": False, "float_used_for_decisions": False,
        "external_notebook_executed": False,
        "scope": "Exact rational law and one finite multinomial comparison. "
                 "The accompanying mathematical type, integer encoding and tensor proof "
                 "excludes every uniform C in R0046, even for G=Z. "
                 "No Euclidean Kakeya counterexample or new dimension bound is asserted.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n",
                      encoding="utf-8", newline="\n")
    print(json.dumps({key: output[key] for key in (
        "Q", "support_size", "type_length", "finite_N21_gt_product_K_strict",
        "finite_left_bit_length", "finite_right_bit_length",
        "integer_encoding_base", "all_four_strong_SD_tests_pass")}))


if __name__ == "__main__":
    main()
