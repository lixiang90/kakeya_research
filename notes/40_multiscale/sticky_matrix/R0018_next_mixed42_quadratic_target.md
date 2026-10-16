# R0018 handoff: a different actual five-dimensional mixed branch

The long-term Goal is unchanged. N5-STICKY-MATRIX-01 is still open, while its Y-only and local W/BSG/inverse iterations are frozen. This is a separate source branch, not a renamed version of the same inverse problem. Next main task: N5-MIXED42-Q01, the quadratic alternative for an actual d=5, k=4, ell=2 configuration. This is not the full mixed branch or general Kakeya.

## Complete data and candidate

Use the entire Wang-Zakharov Definitions17.2-17.4, with original tube joint-parameter AD, convex Wolff C_CW(T)<=delta^{-eta}, original dense horizontal grains, time set Z, xi coherence, the consistent two slope functions and original shading/weights. Here Phi is scalar, k-grain Y is scalar with dimension1-kappa, but horizontal k-grains have dimension3. Write

    f=(u,v), u:Z->R2, v:Z->R,
    tilde f=(a,b), a:Z->R, b:Z->Mat(1,2),
    v(z)=a(z)+b(z)u(z).

The conditional affine alternative obtained from the named scalar-input source Lemma21.1 is to be separately verified/preserved: on a dense original Z' and each allowed rho-window J,

    f(z)-f(z')=(z-z')R_J+O(rho^{1+epsilon0}),
    R_J=(r_J,s_J), r_J in R2.

Do not assume a nonzero lower bound for |r_J| merely from a lower bound for |R_J|. Lemma19.2/19.5 and scalar Lemma21.1 are named source inputs until their required applications have been checked. Required source parameter order: fix zeta>0, mu>0, gamma>0 and epsilon0>0 from the scalar alternative, choose a sufficiently small epsilon<epsilon0/2 depending on these and zeta, then sufficiently small eta and tilde-eta (the latter is the exponent of the retained time density), finally delta sufficiently small depending on the fixed parameters. Use an original allowed rho in [delta^{1/4},delta^mu]. Every restriction of time or original graph must retain its explicitly charged original mass; do not declare a selected piece AD for free.

Define the actual axis-adjusted scalar

    h_{z0}(z)=v(z)-b(z0)u(z).

Quadratic candidate: if an original Ztilde has density at least delta^{tilde-eta} in Z' and for every z0 in Ztilde and J=z0^rho there are real A0,A1,A2 such that for every z in Ztilde intersect J,

    |h_{z0}(z)-A0-A1(z-z0)-A2(z-z0)^2|
      <= C rho^epsilon (rho^2+rho|A1|+rho^2|A2|),

then prove kappa<=zeta under the full actual configuration and correct quantifiers, or give a strict obstruction to a necessary step preserving all the inputs claimed for that step. This would extend the *quadratic alternative* of source Lemma22.4, which is stated only for d4/k3/ell2. It is a research candidate, not a known theorem or a new result ID.

## Exact new obstruction to confront

Source Section22.1, identities (174)-(183), is stated for general k,ell,d. In this branch the coefficient in (176)/(179) is the scalar

    E(z,z')=v(z)-v(z')-b(z')(u(z)-u(z')).

After the affine approximation to u, it involves b(z')r_J. The source scalar k3/ell2 proof bounds r1 times the oscillation of tilde f2 and then recovers all of tilde f2 by dividing by a non-small scalar r1. In k4/ell2, a bound for (b(z')-b(z''))r_J controls only a contraction of a two-entry row. The component of b orthogonal to r_J remains free; if r_J=0 even this contraction controls nothing. For example r=(1,0) and rows (0,t) have exactly zero contraction and nonzero oscillation. This elementary example is only an obstruction to that algebraic inference, not a full-source counterexample.

The next attack must use the remaining actual horizontal dimension, tube paths, xi coherence or convex Wolff mass to control this residual component, or derive a legitimate lower-grain reduction with its original mass. Replacing scalar products by a dot product and concluding the full row is small is prohibited. A fixed generic projection to R4 need not preserve the Y dimension deficit or the required tube/source multiplicities; no free projection is allowed.

## Closure, novelty boundary and stop

This task has scalar Phi and scalar Y but distinct 3D horizontal grains and two independent slope functions. It is not the Mat2 action on vector Phi from N5-STICKY-MATRIX-01, a CP/PM shading equivalence, or a formal j3 horizon theorem. Check any claimed reduction both ways with its legal source restriction closure before declaring a new mechanism. The LIFT005 smooth affine codimension-one classification and HOR003 visible-cost failure remain frozen; they do not resolve or refute this full mixed configuration. Do not reopen them through a change of names.

One main actual attack is allowed next round, with complementary mass/source audit and residual-component counterattack. Its desired output is a real mixed quadratic exclusion or a strict step obstruction with original hypotheses. If it yields only the already exposed contraction-versus-row observation or scalar-to-dot algebra, freeze this local extension and perform a new macro choice. No further bookkeeping-only continuation is justified. Even a successful quadratic case leaves the nonquadratic case, other five-dimensional branches, general-to-sticky and Hausdorff steps open.
