# R0016 working specification: actual five-dimensional matrix nonlinearity

2026-10-17. Start from R0015 commit 15483e64fd9d825a834dbb319fe7217f936ad188; receipt, HEAD and clean worktree checked. Previous Goal turn: progress, because it corrected a quantifier error, froze an equivalent local route, and identified a different source configuration; no new Kakeya bound was obtained. Goal remains active.

## Relation to the final objective

The main task is N5-STICKY-MATRIX-01, precisely as in notes/40_multiscale/sticky_matrix/R0015_next_matrix_target.md: the complete Wang-Zakharov Definitions 17.2-17.4 configuration with d=5, k=ell=3 and Mat(2,2) slope, including every tube/AD/coherence/slab/tube-Katz-Tao assumption. Prove the matrix analogue of nonlinear Lemma 20.3, or locate a strict obstruction in its actual proof mechanism. This would address one genuine five-dimensional sticky branch; it would not finish the other mixed branches, general Kakeya, or Hausdorff reduction.

## Quantifiers and checks

Keep fixed zeta,kappa,gamma,epsilon0,mu and the small epsilon, then eta and eta-dependent delta0 order of the R0015 specification. Keep the all-real-matrix nonaffinity (SM), original dense graph weights and original scale interval. No free irreducibility, additive closure, product structure, slice regularity or per-tube density is allowed.

Before treating any derived condition as a new target, check legal restrictions and both implications. CP/PM remain locally frozen. The actual source uses multiscale coherence absent from CP, so this is not its equivalent restatement. Restricting one matrix row, a source time subset or a fiber does not automatically preserve the full configuration; explicitly account for this whenever used.

## One main task, two complementary reviews

Root: attempt a joint two-dimensional nonlinear expansion from the actual dense translation graph; test reducible and anisotropic cases and the applicability of existing sum-product inputs.

Audit A: reconstruct source L-tuple/dense-graph multiplicities and matrix linear Lemma 20.2 interfaces, distinguishing source statements from independently filled details. Assigned file notes/40_multiscale/sticky_matrix/R0016_original_tuple_audit.md.

Audit B: adversarially examine vector expansion, reducible coefficient families and whether (SM) is enough for the contemplated action theorem. Assigned file notes/40_multiscale/sticky_matrix/R0016_vector_attack.md.

## Acceptance and stop conditions

A proof must cover the full original matrix configuration and all legal reducible cases with original mass and parameter losses. A counterexample must satisfy all of that data and positive fixed kappa; a matrix function or abstract graph alone is only a mechanism test. A strictly narrowed missing branch must be accompanied by an actual proved implication, not renamed assumptions.

Do not continue condition-number, scalar projection, or generic BSG iteration without a new joint mass estimate. If source or action checks yield no such new information this main round, execute macro review and choose a substantive different mechanism; do not revert to CP/PM or formal j=3 models. Record failures and verification scope, independently review any proposed result, then synchronize the complete round to the authorized repository.
