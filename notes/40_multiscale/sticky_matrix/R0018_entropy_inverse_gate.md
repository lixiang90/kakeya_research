# R0018: the common-subspace entropy input and its unpaid gate

2026-10-17. Main N5-STICKY-MATRIX-01 remains open. This note records a checked external input and a strict counterexample to one proposed use of it; it does not prove or refute the actual matrix/source statement. Normalized dyadic entropy is H_n(mu)=H(mu,D_n)/n, with base-two logs.

## 1. Exact primary input

Michael Hochman, arXiv:1503.09043v2 (2017-06-05), Theorem 2.8, PDF/printed p.19: for fixed ambient dimension, R, epsilon>0 and m, there are d_ent=d_ent(epsilon,R,m)>0 and n0 so that probabilities mu,nu supported in [-R,R]^d satisfying

    H_n(mu*nu) < H_n(mu)+d_ent, n>n0

admit subspaces V_0,...,V_n such that, with probability >1-epsilon over a uniform i and independently sampled component locations x~mu,y~nu, mu^{x,i} is (V_i,epsilon,m)-saturated and nu^{y,i} is (V_i,epsilon)-concentrated. V_i is common to the locations at that level; it can vary with i. These are rescaled dyadic components, not a claim that most of the original support lies near one affine plane.

Definitions 2.1/2.3 on p.16 mean concentration near some translate of V, and H_m(theta)>=H_m(pi_{Vperp}theta)+dim V-epsilon. Saturation alone is not concentration of theta on V. Neither dim V_i=2 nor a global graph plane follows just from naming the theorem. The support parameter R occurs explicitly in v2; the version history says it was omitted earlier. The particular normalized W frame in R0018_W_mass_extraction Sections4-5 already has bounded support and coefficients, so fixed R is paid there. In any different normalization producing support of size delta^{-O(eta)}, a bounded-support localization and its mass cost would be required; it is not an additional unresolved gate in that exact bounded W frame.

The final argument in Section 4.6, pp.56-58, was inspected: Theorem 4.12 provides saturation for an iterated convolution nu^{*k} and concentration for nu on the same V_i; the entropy increase in a failed saturation alternative contradicts Corollary 4.16. Theorem 4.12 and all its inputs have not been independently re-proved here. Definition 2.6's independent sampling convention was checked. Theorem 2.14, pp.22-23, concerns a C1 map on fixed compact balls and product measures, with parameters depending on that map (including its linear approximation); it does not automatically apply to scale-dependent dyadic-Lipschitz source f and restricted path weights.

Local original PDF: literature/primary/R0018_hochman_1503_09043_v2.pdf. Page19 rendered and visually checked. This is a more directly aligned statement than merely matching dimensions in Shmerkin Theorem1.2; it is still conditional on a small **independent convolution** entropy increase.

## 2. A strict graph counterexample to automatic independent convolution

The following elementary example specifically refutes the inference

    a positive-density bounded graph a+v in a two-dimensional
    horizontal graph, with >1-dimensional horizontal increment law
    => small entropy increase for the original independent mu*nu.

It even has a globally Lipschitz horizontal graph and a 2-Frostman horizontal increment law. It does not satisfy the actual common time/matrix nonaffinity hypothesis and is not a Kakeya counterexample. It does not refute a correctly paid BSG extraction.

Write R4=R2_x x R2_xi. Set P0={(x,0)} and P1={(x,x)}; P0 and P1 are complementary two-planes. Take rectangles D0=[-3,-2]x[0,1] and D1=[2,3]x[0,1], and a fixed small square U=[-a,a]^2, say a=1/100. For r=2^{-n}, choose the normalized uniform r-grid measures mu_j on {(x,jx):x in Dj} and nu_j on {(u,ju):u in U}, j=0,1. Endpoint domain and increment domains have disjoint labels up to O(1) grid ambiguities at u=0; deleting these zero-scale ambiguities changes no entropy estimates. Let mu=(mu0+mu1)/2, nu=(nu0+nu1)/2.

The support of mu is a Lipschitz graph: xi=0 on D0, xi=x on D1; their positive separation bounds the cross-domain Lipschitz ratio, and a Lipschitz extension may be chosen in the intervening gap. The same holds for the output support

    Aplus = union_j {(x,jx): x in (Dj+U) intersect rZ2}.

Both input and output have O(r^{-2}) cells, comparable counts and uniform 2-Frostman upper bounds. The horizontal projection of nu is exactly the uniform grid law on U, hence has ball bound C w^2 for r<=w<=1. It also has the slab/line cap Cw.

On the independent pair mu x nu define g(a,v)=1 when their plane labels agree and 0 otherwise. Its density is 1/2+o(1), it stays bounded by 1, and every retained sum belongs to Aplus. The retained endpoint and increment laws have constant domination by their original laws. Thus the honest restricted sum has entropy at most 2n+O(1).

But the **independent** convolution has entropy 3n+O(1). Indeed, the two same-plane components have entropy 2n+O(1). Each cross-plane component has entropy 4n+O(1): (x,u)->(x+u,u), respectively (x+u,x), is an invertible linear map of four grid coordinates with uniformly bounded multiplicity. For a mixture of four laws the entropy differs from the average component entropy by a number in [0,log2(4)]. Averaging gives (2+2+4+4)n/4+O(1)=3n+O(1). Therefore H_n(mu*nu)-H_n(mu)=1+O(1/n), despite dense original g and a small two-dimensional output. Independence cannot be obtained by erasing g.

This example supplies a strict boundary for this gate, rather than another unproved inverse conjecture. BSG could select the 0/0 or 1/1 branch here at constant cost and produce a common plane. In the actual problem one must additionally show that extracted time/direction fibers still violate the original all-real matrix-affine nonconcentration. The example proves no impossibility for that task.

## 3. What the actual W facts do and do not pay

R0018_W_mass_extraction.md reconstructs a bounded graph in a common terminal grain neighborhood. It retains real W witnesses; it does not turn the two endpoints into independent samples. R0018_W_inverse_attack.md gives a same-g horizontal increment ball bound with exponent 1+gamma and explicit r^{-C_gamma h} constant after deleting only small original mass. In particular its global increment entropy is >1 at fine scale when h is sufficiently small. These inputs do not supply the independent convolution hypothesis of Theorem2.8. The counterexample in Section2 shows this gap persists even with a stronger horizontal exponent2.

Even after a justified independent extraction, one still has to pay the selected time/direction law, the passage from averaged component planes to actual graph planes, and an affine fit to f at the original power precision and on enough of the **same** B. Support is already bounded in the exact W frame; any further enlargement/localization must be charged only if actually used. Local entropy >1 does not say that each conditional component has dimension >1. Saturation by itself is not a global flatness statement. These are missing estimates, not assumptions added to the target.

## 4. Closing decision

No actual joint expansion, dense-time matrix-affine branch, kappa improvement or complete matrix counterexample has been obtained. The new mass bookkeeping and >1 increment nonconcentration are useful and elementary; they are not certified major intermediate results. The two-plane model strictly rejects the unweighted-convolution shortcut. Following the opening macro, freeze local W/BSG/common-plane iteration without a new estimate paying its independent extraction and original-time return. Do not restart it under an entropy, alignment, or inverse label. The full matrix target stays open; a separate actual mixed sticky branch is selected in the closing macro.
