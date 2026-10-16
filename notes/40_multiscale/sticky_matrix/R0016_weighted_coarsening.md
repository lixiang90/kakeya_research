# R0016: coarse time and grain cells with their original weights

2026-10-17, root. This fills a finite averaging interface needed between the source L-tuples and a scalar theorem at resolution rho. It does not manufacture an original dense graph, slab-Frostman direction prior, or full Kakeya configuration. Those must be supplied separately and are audited in R0016_original_tuple_audit.md.

## 1. Finite weighted quotient lemma

Let pi_A:A_f -> A_c and pi_B:B_f -> B_c be surjections with fibers at most M_A and M_B. Let P be any finite parameter probability space. Given 0<=g(a,b,b',p)<=1, define

    g_c(u,v,v',p) = sum_{pi_A(a)=u,pi_B(b)=v,pi_B(b')=v'}
                        g(a,b,b',p)/(M_A M_B^2).

Then 0<=g_c<=1 and its total mass is the original mass divided by M_A M_B^2. If #A_f >= theta M_A #A_c, #B_f >= theta M_B #B_c and the original normalized mass is at least theta, the coarse normalized mass is at least theta^4. This is an identity and inequality, so it also holds for an arbitrary parameter measure and previously restricted graphs; it never replaces path weights by an unrelated uniform prior.

When individual fibers must have lower bounds, use a heavy-fiber deletion first. Suppose M_A #A_c <= K #A_f, M_B #B_c <= K #B_f, and the graph density is d. Delete A-fibers smaller than d M_A/(10K), and B-fibers smaller than d M_B/(10K). Their respective original masses are at most d/10 of the original A or B mass. Since g<=1, deleting all three corresponding vertex coordinates removes at most 3d/10 of the normalized graph mass. Every surviving fiber is now within a factor 10K/d of its maximum. Renormalization only improves the density up to that controlled power. All these factors may be delta^-O(eta); they are not silently O(1).

This proof applies to marked original vertices. It does not require every tube to retain many marks and does not assert that a restricted object again satisfies every item of Definition 17.2.

## 2. The time scale and dyadic Lipschitz hypothesis

Here rho is a source-allowed scale and J is a dyadic rho-cell. Write r=rho, tau=C delta^-eta rho^2, and normalize J by b=(z-z*)/rho, with z* in J. Normalize the slope by

    F(b)=(f(z)-f(z*))/(tau/rho).

Choose a source-allowed dyadic scale s at least rho^2 with s<=C' delta^-eta rho^2. If rho is not exactly on its scale grid, fixed endpoint/enlargement constants must be retained. A time interval of length rho meets O(rho/s+1) such cells. Source dyadic Lipschitz bounds give oscillation at most C s for f within each cell. Thus the oscillation of F within a cell is O(rho), while its normalized time diameter is

    s/rho <= C' delta^-eta rho.

For eta<mu/10, this tends to zero and tau<rho. A fine time set of cardinality at least delta^Ceta rho/delta, with delta separation, has at most C s/delta preimages per such cell. There are at most C rho/s cells, so heavy-fiber deletion has only delta^-O(eta) cost. Use the normalized center of each surviving s-cell as its coarse time label, and assign to it the F-value of one original time from that cell. The centers have spacing s/rho>=rho and total number at least delta^O(eta) rho^-1. Thus the same coarse B in both time coordinates is rho-separated and has the exponent-one Frostman upper bound with constant delta^-O(eta). The assigned F-values are actual original values, so linewise image identities are preserved. Coarse time labels themselves need not be original times; their affine fits are lifted to the original attached vertices in Section 4.

The centers need not form a complete time grid. All original fine vertices in a cell stay attached to its center and chosen F-value in the quotient weights of Section 1. Choosing independent colors for the two time coordinates would not automatically yield the same B required by the scalar theorem; this construction avoids that issue.

There is an important normalization cancellation. Dyadic Lipschitz on the full allowed J gives ||F||<=C delta^eta. Replacing fine b,b' by their cell representatives changes S(b,b')=(b'-b)(F(b')-F(b)) by O(rho): the time error O(delta^-eta rho) multiplies an F-difference O(delta^eta), and the F error O(rho) multiplies a bounded time difference. Thus the original working resolution r=rho is preserved. On the exact multiplicative source grid rho^2 is itself allowed; the slightly larger s accommodates fixed dyadic rounding without changing this argument. If rho were not source-allowed and only a larger allowed parent were known, the full-J normalization bound must be rechecked rather than assumed. This proof explicitly uses the allowed-scale version of the target.

## 3. Grain cells and tube Katz-Tao

For a fixed endpoint slice, let the original Y be (delta,s_Y,delta^-Ceta)-AD with s_Y=2-kappa. Inside a tau-ball carrying a delta^O(eta) fraction of the usual AD mass, its fine cardinality is delta^O(eta)(tau/delta)^s_Y. At normalized resolution r the maximum fine mass of a cell is at most delta^-O(eta)(tau r/delta)^s_Y, and there are at most delta^-O(eta)r^-s_Y occupied cells in a fixed enlargement. These give the K bounds of Section 1, so passing to heavy coarse Y cells preserves a delta^O(eta) dense weighted graph. An arbitrarily clipped subset with no mass lower bound is not being assigned AD lower regularity.

Source tube Katz-Tao passes to the coarse endpoint support directly: a normalized width-w, length-t tube corresponds to an original tube of width tau w and length tau t. For r<=w<=t<=O(1), the original range delta<=tau w<=tau t<=1 is valid, since tau r is much larger than delta for rho>=delta^(1/4) and small eta. Thus

    N_w(Y_normalized intersect tube) <= delta^-O(eta)(t/w)^(1-gamma).

Finite enlargements and cube/ball conversions affect only fixed dimensional constants. This is a support statement; its probability normalization must still be tracked separately if used with a weighted graph.

## 4. Lifting a matrix-affine fit back to original times

Suppose a coarse fit subset Q has at least r^b #B_c representatives, with b>0 small, and

    ||F(v)-vR-U|| <= r^a, v in Q,

where 0<a<1-b and F is bounded by a fixed constant. The representative counting upper bound gives span(Q)>=delta^O(eta)r^b, once #Q>=2. Evaluating the fit at its two extreme times then bounds

    ||R|| <= delta^-O(eta)r^-b.

The original time and F oscillation estimates show that every attached fine time of Q satisfies the same affine fit with error

    r^a + delta^-O(eta)r^(1-b).

For eta sufficiently small relative to 1-b-a and mu, this is at most 2r^a. The heavy-fiber lower bound shows that the lifted fine subset has at least delta^O(eta)r^b of the original fine time mass. Thus a coarse fit at an exponent strictly larger than the original forbidden-accuracy exponent is ruled out by (SM), with explicit margins. The all-real R,U quantifier is essential here; bounded-matrix notation would not cover this recovered R.

In the source normalization, (SM) forbids error rho^(1+epsilon0)/(tau/rho)=C^-1 delta^eta rho^epsilon0, which is at least rho^(2epsilon0) for eta small compared to mu epsilon0. A coarse fit at exponent 3epsilon0, with fixed factors absorbed by a gap, lifts within that forbidden tolerance. Its mass must also exceed the original rho^epsilon bound; choose the fit-mass exponent strictly below epsilon after every eta-loss. No assumption of uniform fine time occupancy is needed because the heavy-fiber step supplied the precise lower bound used here.

## 5. Scope and remaining interfaces

The preceding arguments justify weighted coarsening at resolution rho and lifting affine fits, including the small-amplitude normalization needed to preserve the output error. They do not prove the L-tuple lower bound or a suitable direction-pair prior. In particular, inclusion Phi_p subset N_rho Phi_q alone does not imply that unused Phi_q cells are slab Frostman. A claim for actual source configurations must verify that extra interface, or replace it by a pair prior with a proved slab bound. The abstract linewise branch is kept separate until these original source inputs have been checked.
