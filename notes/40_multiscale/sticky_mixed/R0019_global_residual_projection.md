# R0019: actual global residual shears excluded by a paid projection input

2026-10-17. Sections1-4 prove global fixed-profile proper families using Gan-Guo-Wang Theorem2.1. Section6 strengthens this to arbitrary bounded global residual shears using the already archived three-dimensional Guth-Wang-Zahl theorem. These are applications of existing theorems, not novelty/major-result claims. They do not solve a local normal form extracted at a fixed-power mass cost, which is the actual remaining mixed42 difficulty.

## 1. Precise geometric statement

Fix kappa>0 and a bounded coordinate chart with last coordinate t and bounded tube slopes. Let T be a finite family of unit delta-tubes in a fixed box in R5. Assume the normalized original convex Wolff bound

    # {T in T: T subset U} / #T <= C delta^{-eta}|U|

for every convex U (constant dilates are allowed by changing C). All original marks use one common delta-separated time set Z in a fixed bounded clock interval, and have average at least c delta^{-1+eta} distinct marked levels per tube. This common Z is part of the statement, as in the actual source; allowing different unconstrained dense clocks for different tubes would not justify the union upper below. At every used t in Z the marks belong, up to Cdelta error, to

    E_t = {(x1,x2,x3, y+beta(t)x3,t): y in Y_t},
    #Y_t <= C delta^{-1+kappa-eta},

with all spatial variables bounded. No uniform distribution of distinct projected tubes or coefficient values is assumed. No independence of the marks and parameters is assumed. Each Y_t has a delta-cover of the displayed size; no lower regularity is needed. Take one of the following fixed profiles on its stated clock interval:

    (i) beta(t)=t,       -1<=t<=1;
    (ii) beta(t)=t^2,    -1<=t<=1;
    (iii) beta(t)=t/(1+t), 0<=t<=1.

Then these hypotheses are inconsistent for eta sufficiently small in kappa and delta sufficiently small. All fixed chart constants may affect delta0 and eta thresholds. In particular, any complete global d5/k4/ell2 configuration with tilde f(t)=(0,0,beta(t)) in this same bounded chart and these profiles is excluded when kappa stays bounded below. Its arbitrary xi, f and actual original tube witnesses are allowed. This is stronger than testing only the explicit product-transport line model.

## 2. Keep actual marked tubes and their weights

Let N=#T and m(T) be the number of its marked delta-time levels. We have m(T)<=Cdelta^{-1} and sum_T m(T)>=c delta^{-1+eta}N. Delete tubes with m(T)<c' delta^{-1+eta}, with c' sufficiently small relative to c. The remaining original family S has #S>=c''delta^eta N and every tube in S keeps at least c'delta^{-1+eta} of its original marked levels. The probability nu=Uniform(S) satisfies

    nu{T subset U} <= C delta^{-2eta}|U|.                 (2.1)

This is the original restriction cost, not a reset of AD or a uniform law on distinct projected images. For source configurations Remark17.1 supplies the dense shading with a fixed multiple of eta in its exponent; replace eta everywhere by that fixed multiple. The proof only requires the displayed density/CW bounds. Such source bookkeeping changes constants A in delta^{-Aeta}, not a fixed power independent of eta.

Parameterize the actual axes by x_j(t)=a_j+t v_j. Tube-to-axis error is O(delta), and all a_j,v_j are bounded. Push nu to

    p=(a3,a4,v3,v4) in R4,

keeping original multiplicities. A parameter ball of radius w>=delta describes projected axes contained in a Cw-tube in (x3,x4,t). Its preimage, intersected with the fixed bounded x1,x2 box and a bounded clock interval containing the whole unit tubes, is convex and has volume O(w^2). Therefore the pushforward omega has

    omega(B(p,w)) <= C delta^{-2eta} w^2,
    delta<=w<=1.                                      (2.2)

This uses a real convex set containing the entire original tubes, rather than only their marked segments. No local-q restriction has been made.

## 3. The conic coefficient law is Frostman with the original weights

For beta=t define the linear coefficient map

    C(p)=(a4, v4-a3, -v3) in R3.

Every original marked level obeys

    q_t(C)=C0+tC1+t^2 C2 in N_(Cdelta)Y_t.              (3.1)

For a coefficient ball of radius w, its inverse in the bounded p box is covered by O(w^{-1}) parameter balls of radius Cw, by covering the one free coordinate a3. Equation(2.2) gives for the original coefficient probability mu=C_*omega

    mu(B(c,w)) <= C delta^{-2eta} w.                   (3.2)

The map for beta=t^2 is instead

    C(p)=(a4,v4,-a3,-v3) in R4,
    q_t(C)=C0+tC1+t^2C2+t^3C3.

It is invertible, so (2.2) yields the stronger coefficient exponent2 and hence also exponent1 on bounded scales. For beta=t/(1+t), multiply the marked relation by 1+t (uniformly bounded above and below on [0,1]) and use

    C(p)=(a4, a4+v4-a3, v4-v3) in R3,
    (1+t)[a4+t v4-beta(t)(a3+t v3)]
          =C0+tC1+t^2C2.

This map has rank3 with a bounded one-dimensional fiber. The same covering argument gives (3.2); the target sets are now (1+t)Y_t, whose Cdelta-cover numbers have the same upper bound. A fixed affine reparameterization to a subinterval of [-1,1] preserves all bounded constants.

Mollify mu at radius c delta and apply a fixed homothety so its support is in the unit ball. At w<delta, a ball bound C delta^{-2eta}delta^{-2}w^3 in R3 (respectively C delta^{-2eta}delta^{-2}w^4 for the exponent2 R4 case) follows from the corresponding above-delta bound. Consequently c_alpha(mu_moll)<=C delta^{-Aeta} for every fixed 0<alpha<1, where A is an absolute fixed constant after restriction; no Frostman constant is silently reset. Every point of a mollified coefficient ball satisfies the marked relation at that coefficient's original levels with only a fixed enlargement of its target interval, because ||q_t|| is uniformly bounded. Thus each point of the mollified support has at least c delta^{-1+eta} incident time-slabs. Shared coefficient values may have different original marks; their union has at least this many levels, which is all the pointwise incidence theorem requires.

## 4. Use the actual finite projection theorem

Named primary input: Gan-Guo-Wang, arXiv2211.09508v2, Theorem2.1, PDFp3. For a fixed nondegenerate moment curve in Rn, m=1, a probability of alpha-Frostman constant c_alpha, 0<alpha<1, and a family W of delta by1 by...by1 boxes normal to the curve's tangent lines at a delta-net of times, if each support point lies in at least delta^{epsilon-1} boxes, then

    #W >= c_{epsilon,n,alpha} c_alpha^{-1}
                    delta^{-1-alpha+L_n sqrt(epsilon)},           (4.1)

where the printed statement permits L_n=10^{10n}. This external theorem has not been independently re-proved here. The raw powers and pointwise hypothesis have been checked; an a.e. Hausdorff projection assertion would not suffice instead.

For the conic use the derivative of Gamma(t)=(t,t^2/2,t^3/3), namely (1,t,t^2). For the cubic phase use Gamma(t)=(t,t^2/2,t^3/3,t^4/4), whose derivative is (1,t,t^2,t^3). Their first n derivatives have a triangular derivative matrix with nonzero constant determinant, so the required nondegeneracy is uniform. A fixed diagonal transformation converts these curves to the factorial normalization in the source.

Round original delta-separated times to a fixed constant multiple of the delta regular net, so each net point receives O(1) original levels and at least a fixed fraction of distinct marks survives. The phase q_t changes by O(delta), so enlarge target intervals by a fixed factor and use the union of the O(1) sets assigned to that net point. Refine to a full regular net at a comparable resolution, with empty targets at unused levels. This avoids relying on the literal unusual net condition in source(2.4). At each used net time take only those standard disjoint time-normal boxes meeting the enlarged target intervals and fixed coefficient support box. Fixed bounded support meets only O(1) boxes in the long directions per target interval. Hence

    #W <= C delta^{-1} max_t #Y_t
         <= C delta^{-2+kappa-eta}.                    (4.2)

Choose alpha=1-kappa/4 if 0<kappa<=1 (larger kappa makes the target count smaller and can be reduced to kappa=1). Choose epsilon>0 so L_n sqrt(epsilon)<kappa/8 and then eta so small that eta<epsilon/2 and all Aeta losses are <kappa/8. After absorbing fixed constants by sufficiently small delta, pointwise original participation dominates delta^{epsilon-1}. From (4.1) and (3.2),

    #W >= c delta^{-2+kappa/4+L_n sqrt(epsilon)+Aeta}
         >= c delta^{-2+kappa/2}.

This contradicts (4.2) for eta small and delta sufficiently small. The probability law used throughout is a pushforward of the same retained original tubes. There is no unproved independent convolution or scalar-to-vector multiplier theorem in this argument.

## 5. Why this does not close the mixed quadratic candidate

The actual general residual beta is only dyadic-Lipschitz, can depend on delta, and need not have any of the three fixed profiles. Source quadratic control concerns h_{z0}=v-b(z0)u, not the remaining beta itself. No source argument here puts beta into these profiles with a bounded change of coordinates and a subpower cost.

Nor does a single rho-window/q inherit the global probability in (2.1) at subpower cost. Conditioning on a family of mass p only gives the original CW bound divided by p. The known natural local mass can be rho^{4-kappa}; this is a fixed-power cost, not delta^{-O(eta)}. A projection of a locally selected normal form therefore cannot be silently substituted for the whole-source argument above. These two gates remain open.

This is an actual global proper-branch exclusion with a verified finite theorem interface; it is not the desired full mixed42 result or a new dimension bound. It is compatible with the counterattack's exact straight-line residual examples, because their convex Wolff constant is too large. Section6 gives a stronger global exclusion; it does not remove the local/source gates above.

## 6. Stronger global result for arbitrary bounded beta

The three-dimensional theorem gives a stronger conclusion than the preceding fixed-profile projection argument. Retain the geometric and original-weight hypotheses of Section1 and its common time set Z. Now beta may be an arbitrary bounded function on Z and may depend on delta. No differentiability, common Cantor transport, polynomial profile or time regularity of beta is needed. Under these hypotheses the same inconsistency holds for sufficiently small eta in kappa.

Named primary input: Guth-Wang-Zahl, arXiv2601.14411v2, Theorem1.1 (PDFp2) and Lemma3.7 (PDFp7) with the parameter in KKT(beta_KKT) set to beta_KKT=0. Theorem1.1 is exactly KKT(0): for every epsilon>0, sufficiently dense shading under small Delta_max has union volume at least delta^epsilon times the sum of tube volumes. Lemma3.7 supplies, for arbitrary Delta_max, the multiplicity bound

    multiplicity(P,Y) <= delta^{-epsilon} Delta_max(P)          (6.1)

when the shading density is at least delta^{eta_GWZ(epsilon)}. Its use here is conditional on those named source results. The proof of the full three-dimensional theorem and its author-reported Lean formalization have not been independently rerun. The parameter beta_KKT is unrelated to the residual function beta(t).

### 6.1 Project original mass, then select comparable weights

Use the same original good family S and probability nu from Section2. Project every whole tube to (x3,x4,t). Its vertical time extent is comparable to1 in the bounded slope chart. Cover it, with a fixed margin, by a standard comparable-delta tube from a fixed parameter net; bounded length-chart subdivisions and finitely many colors cost only constants. Assign each original tube to one such projected tube P_j and let

    w_j = # {assigned original T} / #S.

Keep these actual weights. All P_j lie in a fixed box; whenever P_j is contained in a convex set U, every original tube assigned to it is contained in the convex prism (bounded x1,x2 box) times U. Its volume is O(|U|). Thus

    sum_{j:P_j subset U} w_j <= C delta^{-2eta}|U|.            (6.2)

The argument controls the **whole** assigned original tubes, not just projected marked pieces. Margins ensure projected mark balls also lie inside P_j.

The fixed projected parameter net in bounded R4 has O(delta^{-4}) representatives. Discard representatives of weight <delta^5; their total original mass is O(delta). The remaining weights lie in [delta^5,1] and have O(log(1/delta)) dyadic bins. One bin J has original mass p=sum_{j in J}w_j>=c/log(1/delta). This also works for arbitrary finite positive original weights, without a bound on #T. Within the bin w_j is within a factor2 of p/#J. Consequently the uniform probability on the actual distinct projected tubes in this bin has normalized convex Frostman bound

    # {j in J:P_j subset U}/#J
          <= C delta^{-2eta}p^{-1}|U|
          <= delta^{-Aeta}|U|,                             (6.3)

for small delta, with fixed A (choose slack once). This is a paid replacement of a weighted image by comparable-weight tubes. It is not a uniformization of arbitrary rare images. Bounded net multiplicities/essential-distinctness colors, if used, lose only another fixed factor of mass. Fixed homotheties put the bounded chart inside the unit ball, changing only constants and a comparable delta.

For each P_j in J choose one of its assigned original good tubes and retain **that tube's original marked levels**, with projected delta-ball shadings inside P_j. There are at least c delta^{-1+eta} such levels, with bounded overlap at delta scale. Hence every projected tube has shading volume at least c delta^{2+eta}, and lambda(P,Y)>=c delta^eta. No independent samples or newly invented mark times are introduced. The resulting union is a subset of a fixed enlargement of the projection of the original marked points.

### 6.2 Apply the three-dimensional multiplicity estimate

Write Np=#J and use radius comparable to delta. From (6.3),

    Delta_max(P) = sup_U #P[U] Vol(P_j)/|U|
                     <= C delta^{-Aeta} Np delta^2.          (6.4)

Choose epsilon=kappa/4 (or any sufficiently small fixed fraction of kappa) in (6.1). Then choose eta sufficiently small that the actual shading density meets eta_GWZ(epsilon) and (A+1)eta<kappa/4. Equation(6.1) and the sum of original projected shading volumes give

    |union Y(P_j)|
       >= c delta^{epsilon+(A+1)eta}
       >= c delta^{kappa/2}.                               (6.5)

The number Np cancels; no assumption Np approximately delta^{-2} has been inserted. This is why the normalized Frostman form (6.3) suffices despite Theorem1.1 itself being phrased with Delta_max. The small-bin cost is explicitly included in Aeta.

For the opposing upper, at each original delta-separated time level the projected marks have x3 in a bounded interval and x4=y+beta(t)x3+O(delta), where beta is bounded and #Y_t<=C delta^{-1+kappa-eta}. This slice has at most C delta^{-2+kappa-eta} delta-cells. Thickening each marked point by O(delta) touches O(1) adjacent time cells. There are O(delta^{-1}) original time levels; even if beta jumps between them, no extra continuous-time image is required. Therefore

    |union Y(P_j)| <= C delta^{kappa-eta}.                   (6.6)

Equations(6.5)-(6.6) contradict each other for eta small and delta sufficiently small. This excludes arbitrary global residual beta in the stated fixed-frame geometric family. It subsumes the three profiles above, which remain as a separately paid finite-projection calibration. Neither argument is claimed new in the literature: this is a direct source application with weights and marks spelled out.

### 6.3 Exact boundary for the actual mixed problem

The proof applies when a common fixed two-dimensional spatial kernel removes the other horizontal coordinates from **all** projected slices at the working resolution while keeping the original whole-source CW probability and long original marks. The actual local reduction in R0019_source_and_mass_audit gives only osc a<=K rho^2 and osc(proj_r b)<=K rho^{1+c epsilon}, with an unconstrained dyadic-Lipschitz beta. These errors are far larger than delta; their projected blur is not automatically a delta-level global shear. A local q/time restriction, anisotropic change of scale or parent-tube selection must independently pay the law, shading, error resolution and convex-prism costs. Simply importing (6.2) after such a restriction divides by its original mass, possibly a fixed rho power.

Thus no complete mixed quadratic theorem has been proved. The meaningful next gate is actual multiscale globalization of this paid three-dimensional input, or a strict obstruction preserving the local source hypotheses; repeating the three fixed profiles, the exact product-transport models or unweighted projection is not further progress.
