# R0016: applying the linewise exclusion to the actual five-dimensional source

2026-10-17, root. This is a conditional subcase of N5-STICKY-MATRIX-01, using Wang-Zakharov Theorem 13.5 as a named external mathematical input. It does not use Lemma 19.2 or the full four-dimensional Kakeya proof. The original Definitions 17.2-17.4 data are retained throughout; no restricted data are declared to be a new complete configuration.

## Statement and fixed parameters

Fix kappa in the source range (0,2], gamma in (0,1), mu in (0,1/4). Choose epsilon0>0 sufficiently small depending on gamma and with 3epsilon0<1/10. Choose the source epsilon>0 small, then eta>0 sufficiently small depending on all previous parameters, and delta sufficiently small depending on eta and them. The smallness of epsilon0 is an explicit refinement of the literal R0015 candidate, needed for the existing scalar theorem. Kappa is not changed.

Let a complete d=5,k=ell=3 configuration satisfy (SM) at a source-allowed rho in [delta^(1/4),delta^mu]. Suppose there is a dyadic rho-time cell J with

    #(Z intersect J) >= delta^Ceta rho/delta,

where C is fixed independently of eta,delta, on which either

    f(z)=F0+h(z)M,                              (PENCIL)
    f(z)=F0+v r(z), r(z) a row vector.           (IMAGE)

All matrices/vectors/functions are the actual source values. No bounded inverse of M, rank lower bound or smoothness of h,r is assumed. Then this configuration cannot exist. More generally the argument needs only that, for every used coarse direction difference, the corresponding f(Z intersect J) image is linewise; the two displayed families give that condition automatically.

This is a real subcase exclusion, not a proof of (SM) for general matrix slopes. A claim for arbitrary epsilon0 or all remaining genuinely two-dimensional images is not made.

## 1. Original tuples, direction set, and endpoint grain mass

First choose original tube witnesses for each fine Phi_p bin, with bounded collision multiplicity; any extra point-tube incidences need not be retained. This preserves the supplied direction witnesses and coherence. Only upper AD bounds of the original ambient tube family are used for these selected incidences; no new complete AD-regular tube family is asserted. Apply R0016_original_tuple_audit.md, Sections 2-6, with A=Z and the specified J. With K=delta^-C'eta (changing fixed C' when needed), it gives an actual good cube q, original time set B_f=Z_q with

    m=#B_f >= K^-1 rho/delta,

and an auxiliary rho-separated direction set H with uniform slab exponent gamma and constant K, constructed from the actual incidence mixture. Heavy direction bins retain the original L-tuple mass by its proved marginal upper. This does not rely on unused cells of the original Phi_q being slab Frostman.

For a selected original endpoint time z*, there is a subset Y0 of actual grain labels, all inside an O(rho) ball, such that

    #Y0 >= K^-1(rho/delta)^(2-kappa),
    G subset Y0 x B_f x B_f x H x H,
    #G >= K^-1 #Y0 m^2 #H^2.

Every edge gives an original endpoint y2 in the full source Y_(z*) with

    y2-y1=(z-z')(f(z)-f(z'))(phi1-phi2)+O(tau rho+delta),

where tau=C delta^-eta rho^2. The direction values phi_i are H-bin centers. If exact linewise families are imposed, applying any such difference to the original f-values is still exactly linewise. Replacing original fine directions by the bin centers has already been paid for by the displayed O(tau rho) error.

## 2. A good tau-window without resetting AD lower bounds

Put alpha=2-kappa. The original Y_(z*) is AD; Y0 inherits its upper bounds, not its lower bounds. Since Y0 lies in an O(rho) ball, at most K(rho/tau)^alpha tau-cubes meet it, by the original AD lower/upper packing applied to the full Y. Delete cubes Q with

    #(Y0 intersect Q) < K^-B(tau/delta)^alpha.

Their total input mass is at most K^(1-B)(rho/delta)^alpha, hence at most K^(C-B)#Y0. As G is an indicator, choosing B larger than its density loss removes less than half of its original graph mass. Average the remaining graph by its original input point counts. This selects a cube Q with

    #A_f^- >= K^-C(tau/delta)^alpha,
    G_Q density >= K^-C,

where A_f^-=Y0 intersect Q is the actual input. Since f is Lipschitz on J, the translation length is O(rho^2), at most O(tau), so every output lies in A_f^+=Y_(z*) intersect C Q after a fixed enlargement. Original AD upper gives #A_f^+<=K(tau/delta)^alpha and therefore #A_f^+<=K^C #A_f^-.

For alpha=0 the same packing/count inequalities have exponent zero and fixed K losses; no division by alpha is used. Any original grain-label multiplicity within one delta-cell is at most K and is included in these fixed powers, as proved in the tuple audit. Select separated coarse supports only after aggregating those weights.

## 3. Weighted quotient at resolution r=rho

Normalize y by tau, time by rho, and F by tau/rho. Use the heavy-fiber quotient and time-cell-center construction of R0016_weighted_coarsening.md. The input and output coarse supports A_minus,A_plus have the required cardinal ratio K^C. A_minus inherits tube Katz-Tao exponent 1-gamma with constant K^C directly from the full original Y; the original widths queried are at least tau rho, much larger than delta. The two time coordinates use one common rho-separated set B of source-cell centers, with exponent-one Frostman constant K^C.

The normalized F values are chosen actual fine f-values divided by tau/rho and have norm O(delta^eta). This amplitude cancels the possible delta^-eta time displacement, leaving O(rho) output error. The bounded quotient weight g has density at least K^-C on A_minus x B x B x H x H. The pair prior is the uniform ordered difference law of H; it has the slab line-cap required by MNL-001. No product structure of Y or independent original times is introduced.

The quotient's representative F-values are still in the same matrix pencil or common-image family. Coarse time centers may be new domain labels, but the linewise condition is a condition on the image F(B), so it is preserved exactly. There is no assumption that the original source f is defined at those centers.

## 4. All-real matrix nonaffinity passes to this B

Take a=3epsilon0 and b0=epsilon/2. If an all-real matrix fit on B with error rho^a met more than rho^b0 #B points, the exponent-one count and #B>=K^-C rho^-1 would give its time span at least K^-C rho^b0. Bounded F then gives ||R||<=K^C rho^-b0. The source-cell time displacement and F oscillation imply that all attached fine points fit the same affine matrix with error

    rho^(3epsilon0)+K^C rho^(1-b0).

Choose epsilon small enough that 1-b0>3epsilon0, and then eta small. This error is at most 2rho^(3epsilon0), smaller than the original normalized forbidden tolerance C^-1 delta^eta rho^epsilon0. Heavy time-fiber lower bounds make the lifted fine mass at least

    K^-C rho^b0 (rho/delta),

which exceeds rho^epsilon(rho/delta) when eta is sufficiently small. This contradicts the original (SM), whose coefficients range over all real matrices. Thus (SM_r) holds on the actual coarse B. No per-bin occupancy or bounded coefficient restriction was assumed for free.

## 5. Apply the finite theorem; stop at the genuine remainder

Choose eta last so every K^C is at most rho^-h for the h in MNL-001 with parameters a,b0,gamma. The complete bounded graph now satisfies that theorem. All its labels are linewise for either displayed source family, which yields a contradiction.

The tuple counts, auxiliary H, good endpoint/window choice, and weighted coarsening above are explicit interfaces. The only advanced expansion input is the existing scalar Theorem 13.5. The scalar theorem itself has not been fully independently re-proved, so the application remains explicitly conditional on that named theorem. This is not a conditional restatement of the whole matrix target: the displayed proper slope subfamilies have actually been excluded under that established input, while general F(B)psi curves in R^2 remain unhandled.

For general slopes, positive original graph mass with planar F(B)psi curves outside an O(rho) neighborhood of every line remains possible. Such a curve need not have dimension two. The linewise theorem supplies no irreducibility or iterated action closure for it. This is the remaining main task, not permission to assume those properties. The other sticky mixed branches, general-to-sticky reduction, and Hausdorff covering are still open.
