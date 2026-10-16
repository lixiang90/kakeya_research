# R0008 prior/profile 独立审查

日期：2026-10-17。审查者：`lifting_obstructions`。对象：`notes/50_counterexamples/R0008_smoothed_quadric_prior.md`。结论：**稿件当前的 full8 tempered prior、典型 profile 与 joint-angular upper 均通过内部独立审查**；不据此登记 horizon 或 Kakeya 结论。

## 1. 审查范围与唯一措辞修订

逐项核验了固定 `ρ_noise=1` 的六系数盒平滑、相同 grid-index 概率、有限 Cantor hidden initial law、完整八系数 pieces、原始 incidence mass 1/4、两侧典型 profile、ρ_velocity 高于/低于 δ 的 joint-angular cap，以及负 f(0) 与源定义的关系。

原 §1 的“所有 visible、hidden 随机变量相互独立”可能被误解为六个最终可见 coefficients 内部独立。作者已修订并核对现稿：独立的是整个 `(B,V)` block、C、W 三组；ξ、ζ 与 index λ 独立；B、V 内部仍经共同 λ 耦合。修订后没有此歧义。

本审查不要求在 quadric 邻域的每个点填满 noise support，也不将 λ 变成 world 或被观察 index。

## 2. 完整八系数 prior：通过

grid 的三个参数恰好分别出现在无噪声系数 `b₁=s,u₁=p,u₃=q`。固定完整 coefficient point 时，满足半宽 δ 噪声条件的每个参数坐标至多有 3 个格点，因此重叠数至多 27（端点约定只改固定因子）。没有 δ⁻¹ 阶重叠损失。

每个 λ 的 full-six box density 为 `Nδ⁻¹(2δ)⁻⁶≈δ⁻³`。再乘 Cantor terminal interval density `ℓ^{d−1}` 与 independent W density `η⁻¹`，得到稿件 (1.8) 的完整八维 ceiling

\[
 C\delta^{-3}\ell^{d-1}\eta^{-1}.
\]

δ、ℓ、η 的倒数均为 N₀ 的固定幂，故此 ceiling 合法。无 index 实现中，把六坐标的全部 box facets 作共同 refinement 至多给 O(Nδ⁶) 个 visible rectangles；再乘 2^m 个 Cantor pieces，仍是固定多项式数。每个 piece 由固定数量的线性不等式定义。

若改用源 Definition 2.2 许可的 indexed copies，也只是同一个 coefficient law 的内部实现；λ 仍不进入 observation。若把 λ 改成 world，conditional densities 和 angular cap 会发生变化，不能沿用本稿结论；现稿没有这样做。

`P_*=w` 的 native bounds、B=1、bounded Y,V,w 和 selected event `t∈[1/2,3/4]` 均逐项符合稿件声明的 j=3 形式模型。原源稿 version 2 实际 j=2，这一点在首段已经明确。

## 3. Exact-base upper、support 与典型 lower：通过

固定 t∈[1/2,3/4]，给定 s 格点后，`x=s+tp,z=s⁻¹+tq` 的 near-Y 条件分别将 p、q 限在 O(δ) 区间，因此贡献给一个 O(δ) 空间盒的 indices 至多 Cδ⁻¹。单 index 的 ξ+tζ density 至多 Cδ⁻³；乘原始 index 权 Nδ⁻¹≈δ³ 后得

\[
 g_t(Y)\le C\delta^{-1}.
\]

所有 noisy positions 满足 `|tY₂+Y₁Y₃−1|≤Cδ`。因 t≥1/2，对固定有界 Y₁,Y₃，Y₂ 允许长度为 O(δ)，所以实际 support 的体积至多 Cδ。这个 upper 不要求任何 pointwise lower，也没有假设离散像无孔。

独立 hidden block 的每个 a-bin 质量≤Ca^d，occupied bins 数≤Ca⁻ᵈ。后者由 Cantor support covering 独立证明，不能仅凭 Frostman upper 推出；现稿的论证没有混用二者。

因此原始 observation density G_r 满足

\[
 G_r\le C n_r,\qquad
 |\operatorname{supp}G_r|_{dt\,dY\times\#B}\le C/n_r,
 \quad n_r=\delta^{-1}a_r^d.
\]

在 sampled observation law 下直接积分可得

\[
 \mu\{G_r<n_r/K\}\le C/K.
\]

这是正确的**典型 lower**：density 自己小的区域只承载相应的小质量。它完全不推出 quadric 邻域内 everywhere lower 或 arbitrary occupied-bin lower；稿件明确保持这个边界。

取 K=N₀^τ 后，异常质量是固定幂小，正好符合源“typical”的量词。常数对 a∈[a_L,1] 一致，有限预备表的 subpower 次 union bound 合法。η≪ℓ≪a_L 充分保证此区间内的 Cantor covering；r=0 的至多固定个 unit bins 也包括在内。

## 4. Joint angular cap 的两个尺度：通过

这里用 ρ 表示速度 bin 宽度，与固定 noise 半宽常数 1 区分。

当 ρ≥δ 时，velocity bin 第一坐标将 p 限在长 O(ρ) 的区间；near-Y₁ 将 s 限在长 O(ρ) 的区间，因此有 O(ρ/δ) 个 s 格点。每个 s 的 near-Y₁、near-Y₃ 再给 O(1) 个 p、q。每个 index 的 joint `(Y,[V]ρ)` density 不超过其 Y-density Cδ⁻³，于是

\[
 g_{t,\rho}(Y,J)
 \le C\delta^{-3}\,\delta^3(\rho/\delta)
 =C\delta^{-1}\rho.
\]

当 ρ<δ 时，velocity bin 把 p、q 各限在长 O(δ) 区间，near-Y₁ 再把 s 限在长 O(δ) 区间，故仅 O(1) 个 indices。单 index 的 `(Y,V)` density ceiling 为 Cδ⁻⁶：`(ξ,ζ)→(ξ+tζ,ζ)` 的 Jacobian 确为 1。积分 velocity box 体积 ρ³，并乘同一 index 权 δ³，得

\[
 g_{t,\rho}(Y,J)\le C\delta^{-3}\rho^3
 \le C\delta^{-1}\rho.
\]

最后一式恰用 ρ≤δ，没有丢掉 δ 以下的角尺度。hidden 与 visible blocks 独立，所以乘 hidden-bin upper 后，原 selected measure 的 joint density everywhere 满足

\[
 G_{r,\rho}\le C\delta^{-1}a_r^d\rho.
\]

取 ρ=N₀⁻ᵘ、r=L，得到源 (2.6) 形式的 S=1 upper，固定 u-range 任意。该式是 joint-density upper；conditional version 仍须结合纯 observation 的典型 lower。现稿已经这样区分。

## 5. 负 f(0) 的源定义核对：形式允许，来源限制仍保留

独立核对源文 Definition 2.1、2.2、2.6 和 Lemma 2.5。源 Definition 2.1 将 typical density 写成 `N₀^{-f}`，没有要求 f 非负；Definition 2.2 反而明确允许完整 coefficient density 有任意固定 N₀ 幂 ceiling。exact-base density 可以在固定幂小 support 上达到固定幂大。

稿件给

\[
 f(r)=dr-M,\qquad d=1/2.
\]

此 profile 非递减、1-Lipschitz，且

\[
 f(L)-f(r)=d(L-r),
\]

满足 Definition 2.6 的 endpoint 差值约束。该定义也没有附加 f(0)=0 或 n(0)≈log1 的条件。因此 **f(0)=−M 不违反源 generic 数值定义**。

后文在 prepared true parent 正规化后出现的 `n′(0)≈log1` 属于额外来源/路径结构；不能把它倒灌进 Definition 2.1 或 2.6。反过来，本模型也没有验证这种来源结构，不能以“形式 cap class 输入”宣称已经得到 Kakeya maximizing sequence。

严格地说，原 source version 2 只有 j=2；本稿证明的是将 visible dimension 改为 3 后，完整先验满足相应 finiteness/native、homogeneous profile 和 cap 数值条件。现稿首段与末段均保留此限定，表述通过。

## 6. 审查结论与未审部分

以上 prior/profile/angular 论证无需修改数学主式；独立措辞问题已经由作者修正。所有估计使用同一个未重新归一化的概率 prior 与其 1/4 质量 selected incidence measure。

本 review 不认证 short-block 任意二次测试上界、true-floor 使用、非空 terminal systems、horizon lower、horizon upper 或 Kakeya 来源。这些需要本轮独立接口结果，不能从本文 profile 单独推出。
