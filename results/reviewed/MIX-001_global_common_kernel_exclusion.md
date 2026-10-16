# MIX-001: global common-kernel slice deficit is excluded

Status: conditional application of named existing three-dimensional results; internally cross-reviewed in R0019, not externally peer-reviewed. No novelty, new Kakeya dimension bound or major-intermediate-result claim.

Fix zeta in (0,1) and bounded tube/slope charts in R5. For eta sufficiently small in zeta and the fixed chart constants, and delta sufficiently small, the following data cannot coexist:

1. An original family of unit delta-tubes with normalized convex Wolff bound C_CW<=Cdelta^{-eta}.
2. Original marks on a **common** delta-separated bounded time set Z, with average at least cdelta^{-1+eta} distinct marks per tube.
3. In one fixed coordinate frame all those marks satisfy

       x4=y+beta(t)x3+O(delta), y in Y_t,
       N_delta(Y_t)<=Cdelta^{-1+kappa-eta}, kappa>=zeta,

   where beta is bounded on Z. The other two spatial coordinates are free in a fixed bounded box. Beta may depend on delta; it need not be continuous or polynomial.

The actual d5/k4/ell2 global profile tilde f=(0,0,beta) is a special case, for arbitrary compatible f and xi. This is a proper global branch; local approximate profiles with fixed-power restriction/blur costs are outside the conclusion.

Proof and exact original-weight costs: notes/40_multiscale/sticky_mixed/R0019_global_residual_projection.md, Section6. Keep original good tubes, project whole tubes to (x3,x4,t), assign bounded-grid representatives and retain their original weights. Delete representatives lighter than delta^5 and select a dyadic weight bin of mass at least c/log(1/delta). The uniform bin law inherits normalized convex Frostman with only delta^{-O(eta)} cost, because preimages of convex sets are actual full-tube convex prisms. Each representative retains one good original witness tube's marks, giving dense shading. The multiplicity input below then gives projected union volume at least delta^{epsilon+O(eta)}. Its slice covering upper is Cdelta^{kappa-eta}, even for arbitrary beta on the discrete common Z. Choose epsilon and eta sufficiently small in zeta for a contradiction.

Named dependency: Guth-Wang-Zahl arXiv2601.14411v2, Theorem1.1 and Lemma3.7 at KKT parameter0, giving multiplicity<=delta^{-epsilon}Delta_max for dense shadings. Their complete proof/author-reported formalization have not been rerun independently. The companion GGW2211.09508v2 Theorem2.1 argument in Sections1-4 of the proof independently excludes three fixed profiles but is not needed for Section6.

Finalized reviews: research/reviews/R0019_projection_review.md; research/reviews/R0019_source_and_countermodel_review.md; root integration research/reviews/R0019_root_integration_review.md. Common-Z, time-net rounding, whole-tube containment and the tiny-weight tail correction are included in the final proof.

No implication is asserted from the actual local quadratic reduction to hypothesis3 at delta resolution in a single global frame. That reduction currently gives only a and the parallel component of b slowly varying, plus one remaining scalar beta. Its unresolved multiscale projection/CW/shading interface is precisely the next task within N5-MIXED42-Q01. General five-dimensional and Hausdorff steps remain open.
