# MNL-001: exclusion of linewise matrix-translation mass

2026-10-17, R0016. Conditional finite-graph result, internally cross-reviewed, not externally peer reviewed. It uses the beta=1, C={1} case of Wang-Zakharov Theorem 13.5 as an explicit input; that entire theorem has not been independently re-proved here. No novelty or major-intermediate-result claim is made. It does not solve the full Mat(2,2) branch or give a new Kakeya dimension bound.

## Statement

Fix gamma_T,gamma_Phi>0 and b0>0. There are a0(gamma_T)>0 and, for 0<a<a0, a sufficiently small h>0 such that the following configuration is impossible for sufficiently small r (allowed to depend on h).

All data lie in fixed bounded boxes. B is an r-separated exponent-one Frostman set with constant r^-h. A_minus,A_plus are r-separated planar sets with #A_plus<=r^-h #A_minus; A_minus is tube Katz-Tao of exponent 1-gamma_T and constant r^-h. A finite probability space of original difference labels has bounded vectors psi whose law assigns at most r^-h t^gamma_Phi to every width-t slab for t>=r. Multiplicities of equal differences are retained.

Let F:B->Mat(2,2) be bounded. Every real affine matrix function bR+U fits F within r^a on at most r^b0 #B times. Suppose a weight 0<=g<=1, integrated against the same label prior, has mass at least r^h #A_minus #B^2, and every positive edge satisfies

    dist(a+(b-b')(F(b)-F(b'))psi,A_plus) <= C r.

If for every used label the whole curve F(B)psi lies within C r of an affine line (the line may depend on the label), these assumptions contradict Theorem 13.5.

Proof with all fiber/parameter losses: notes/40_multiscale/sticky_matrix/R0016_vector_attack.md, Sections 2-6. Its key steps are a cardinal-ratio deletion on the original input fibers, scalar expansion along the retained fiber, and two independent differences whose scalar affine fits overlap on the same original times. Slab Frostman pays for the determinant loss; right multiplication recovers an all-real matrix fit, contradicting the stated nonaffinity.

## Mass interpretation and exact slope families

The same statement applies after restricting the original graph to the labels whose curves are linewise. If that restriction carried r^h of normalized mass it would contradict the result. Thus its mass is less than that threshold. When the original graph has density r^h1 with h1 sufficiently smaller than this h, deleting linewise labels removes o(1) of its mass. This is a proved conditional mass exclusion under the displayed hypotheses, not an assumed inverse conclusion.

In particular the branch includes F(b)=F0+v r(b), with r(b) a row vector, and F(b)=F0+h(b)M for any fixed matrix M, even invertible or scalar. No irreducibility or minimum singular value is assumed. The exact classification when all directions are linewise is in R0016_matrix_span_boundary.md; it is not a quantitative near-rank classification.

## Scope of the original-source interface

The finite theorem needs the dense bounded graph, original-prior domination or an auxiliary direction set with an independently proved slab bound, and a legitimate fine-to-coarse time map. These are not implied by writing down the algebraic translation identity. R0016_original_tuple_audit.md and R0016_weighted_coarsening.md audit these interfaces, including good-cube choice, the omitted L-tuple Cauchy-Schwarz step, unused coarse direction cells, and the all-real fit transfer. They must be checked before applying this result to an original configuration.

The source-scale application uses a=3 epsilon0 (with a strict error margin), b0 a fixed fraction of the source epsilon, and eta small after the scalar theorem's thresholds. It explicitly requires epsilon0 sufficiently small depending on the tube exponent; it does not prove the unrestricted epsilon0 wording of the earlier literal candidate. Kappa is fixed and is never reduced. Source-allowed rho and the small amplitude of normalized F preserve O(rho) output error.

Planar curves F(B)psi that are not contained in an O(r) neighborhood of a line remain open. This describes affine geometry, not a claim that such a curve has dimension two. No claim is made that these yield irreducibility, a sum-product action on Y, or the missing joint expansion. Other sticky mixed cases, the general-to-sticky step, and Hausdorff covering remain outside this result.
