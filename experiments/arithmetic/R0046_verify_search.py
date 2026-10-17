"""Independent bitmask recount of the bounded R0046 Gray-code search.

Iterates ordinary integer masks; counts occupied projection classes by
bit intersections, without the search's incremental counters or row histogram.
"""

import hashlib
import json
from pathlib import Path


def classes(points, a, b):
    result = {}
    for i, (x, y) in enumerate(points):
        value = a*x+b*y
        result[value] = result.get(value, 0) | (1 << i)
    return list(result.values())


def main():
    directory = Path(__file__).parent
    raw = (directory / "outputs/R0046_search.json").read_bytes()
    output = json.loads(raw)
    assert output["script_sha256"] == hashlib.sha256(
        (directory / "R0046_rational_projection_search.py").read_bytes()).hexdigest()
    assert output["strict_failure_found"] is False
    reports = []
    for record in output["grids"]:
        points = record["grid_points"]
        rows = classes(points, 1, 0)
        images = [classes(points, a, b) for a, b in ((1, 1), (-1, 1), (0, 1), (1, 3))]
        old = 0
        outside = 0
        best = None
        for mask in range(1, 1 << len(points)):
            n = mask.bit_count()
            m = max((mask & row).bit_count() for row in rows)
            s = [sum(bool(mask & group) for group in image) for image in images]
            left = n**21
            right = m**7 * (s[0]*s[1]*s[2])**10 * s[3]**5
            assert left <= right, (record["selected_forms"], mask)
            if n <= m*m:
                old += 1
            else:
                outside += 1
                if best is None or left*best[1] > best[0]*right:
                    best = (left, right)
        assert record["nonempty_subsets_examined"] == (1 << len(points))-1
        assert (old, outside) == (record["N_le_M_squared"], record["N_gt_M_squared"])
        reported = record["best_outside_old_region"]
        assert best[0]*reported["right_M7_P10_S4_5"] == best[1]*reported["left_N21"]
        reports.append({"selected_forms": record["selected_forms"],
                        "all_subsets_recounted": old+outside,
                        "N_gt_M_squared": outside, "best_ratio_agrees_exactly": True})
    assert len(reports) == 10
    total = sum(g["all_subsets_recounted"] for g in reports)
    assert total == output["total_subsets_examined"] == 655350
    report = {"round": "R0046", "input_sha256": hashlib.sha256(raw).hexdigest(),
              "independent_method": "ordinary masks / bit intersections / exact integers",
              "all_subsets_recounted": total,
              "N_gt_M_squared": sum(g["N_gt_M_squared"] for g in reports),
              "all_finite_comparisons_passed": True,
              "universal_inequality_proved": False, "grids": reports}
    (directory / "outputs/R0046_search_verification.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in report.items() if k != "grids"}))


if __name__ == "__main__":
    main()
