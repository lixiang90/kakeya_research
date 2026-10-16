# R0016: linewise matrix spans and the boundary of a generic inverse theorem

2026-10-17, root. This is an elementary algebraic boundary and source-interface analysis, not a Kakeya result. The nonlinear estimate for linewise increments is developed separately in R0016_vector_attack.md. No implication for general Mat(2,2) coefficients is asserted here.

## 1. Exact classification of globally linewise increments

Let L be a real linear subspace of Mat(2,2). Suppose

    dim{A psi : A in L} <= 1 for every psi in R^2.             (LW)

Then either dim L <= 1, or there is one line V in R^2 such that im A is contained in V for every A in L. Conversely each of these two alternatives implies (LW).

Proof. If L contains an invertible A, then for each B in L the matrix A^(-1)B maps every vector into its own span. Applying it to e1,e2,e1+e2 shows it is scalar; hence B is a scalar multiple of A and dim L=1. Otherwise every nonzero A in L has rank one. Fix A=u a^T. If B=v b^T has image different from span(u), then

    det(A psi,B psi)=det(u,v)(a^T psi)(b^T psi)

is a nonzero polynomial (both linear forms are nonzero). It cannot vanish for every psi, contrary to (LW). Thus every B has the same image line. The converse is immediate. This proof does not use or assume a matrix algebra or irreducibility.

For an arbitrary F:Btime -> Mat(2,2), set L=span{F(b)-F(b0): b in Btime}. The two cases are respectively

    F(b)=F0+h(b)M,
    F(b)=F0+v r(b),  r(b) a row vector.

In the first case the output line of the increment F(b)psi-F(b')psi can depend on psi; in the second it is one fixed line. These are different admissible mechanisms; neither has to give irreducible matrix actions.

## 2. Positive slab-Frostman mass suffices for the exact classification

Let Phi be a finite r-separated subset of a bounded planar box satisfying, for any width-r slab S,

    # (Phi intersect S) <= C r^gamma #Phi,

and let P subset Phi x Phi have #P > 2 C' C r^gamma #Phi^2, with C' an absolute enlargement constant. Suppose for every pair in P the full set {F(b)(phi1-phi2): b in Btime} is contained in some affine line depending on the pair.

Then the classification above still follows. For any A,B in L, the homogeneous quadratic q(psi)=det(A psi,B psi) vanishes on these differences. A nonzero homogeneous quadratic on R^2 has its real zero set contained in at most two lines through the origin, possibly only the origin. For each fixed phi1, differences on either line place phi2 in a width-r slab. Hence at most 2 C' C r^gamma #Phi^2 such pairs exist. Thus every q is the zero polynomial, which implies (LW), and Section 1 applies.

This is an exact statement: it does not give a scale-independent quantitative classification from small determinants. In particular, a very small nonzero polynomial still has the same exact zero lines, but its approximate zero set can occupy almost everything. Replacing equalities by O(r^a) needs coefficient normalization and a separate quantitative argument. No such argument is claimed here.

The slab condition on the source Phi_q would give C=delta^-O(eta), r=rho, so a graph with subpower pair density can exceed the displayed exceptional mass if eta is sufficiently small relative to mu*gamma. A dense graph does not by itself imply that its projected increments are linewise. This lemma classifies the branch only after that exact condition is verified.

## 3. A newly archived general inverse theorem does not close the main branch

Primary source: Pablo Shmerkin, arXiv:2308.09846v3 (19 pages, 2024-09-23 version; official version history checked 2026-10-17). Read Theorem 1.2, Theorem 1.5 and Section 4.3 including Proposition 4.3; inspect original PDF page 2. This is selected-statement/interface reading, not an independent proof verification.

The convolution inverse theorem allows saturation on intermediate subspaces, whose directions may vary with scale and location. It does not supply the alignment between those subspaces that a direct matrix-action proof would need. The line-porosity application requires a porosity constant fixed before the small scale tends to zero. Source tube Katz-Tao with constant delta^-eta does not immediately supply such a constant.

An elementary parameter test makes this precise. Fix gamma in (0,1), eta>0 and a in (0,eta/2). Let

    P_delta={(j delta,0): 0 <= j < floor(delta^-a)}.

Its cardinality is at most delta^-eta, so it obeys the source-style (delta,0,delta^-eta) AD bounds up to fixed norm constants. For a width-r, length-t tube, its r-cover is at most C min(delta^-a,t/r+1), which is at most C delta^(-a gamma)(t/r)^(1-gamma), and hence at most C delta^-eta (t/r)^(1-gamma). Nevertheless it contains an arbitrarily long consecutive grid segment relative to resolution delta. On its supporting line, balls with radius a small fixed multiple of delta^(1-a) have no hole of a fixed relative radius once delta is small. Thus these two Y-type hypotheses alone do not imply uniform line porosity between delta and 1.

This is a test of two Y hypotheses (dimension zero, the kappa=2 boundary), not a complete positive-loss tube configuration or a counterexample to the matrix lemma. It rules out a direct invocation of the fixed-porosity corollary from those estimates. It does not rule out using the full convolution inverse theorem together with the original time/coherence data. The original graph coefficients act on Phi differences, while Y carries translations; that interface still has to be proved.

## 4. Research decision

The linewise branch can be attacked by actual scalar translation estimates on fibers, without imposing irreducibility. The unhandled branch consists of genuinely two-dimensional projected increments; it cannot be dismissed by the algebraic classification or by applying the generic inverse theorem title. A proved linewise exclusion is a strict subcase of the main target, not a new equivalent formulation of the whole target. No source-free CP/PM route is reopened.
