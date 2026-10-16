# R0021 独审：mixed32 实际 cubic、原质量与条件排除

2026-10-17，`lifting_obstructions`。审查对象：

- root `notes/40_multiscale/sticky_mixed/R0021_conditional_quadratic_exclusion.md`；
- A `notes/40_multiscale/sticky_mixed/R0021_mixed32_source_audit.md`；
- 配套 finite PCT 的 source 接口。

核读本库 WZ2609.22035v1 Definitions17.2–17.4、§22.1(174)–(183)、§22.4 的相关原文，并与本轮修正版 PCT 证明对照。**审定：所列固定尺度准备下的条件 quadratic 排除链通过。** 不将该准备从原 all-scale Lemma21.1 自动推出，也未独立重证 Lemmas19.2/19.4 等高级 source 输入。没有审定整个 mixed32、五维或一般 Kakeya 已解决。

## 1. 条件不是隐去的 source 结论

root 明确保留：完整 d5/k3/ℓ2 配置、原 AD4/CW、ξ/Φ coherence、原 marks、two-slope consistency，以及以下额外的已准备输入：固定尺度全局 dense retained times、**完整 f** 的 affine fit 与 whole velocity 下界、两 slope 本尺度 Lipschitz、有限 stable graph refinement 的合法性和一般维度19.4。

这些条件比仅知道“原 Lemma21.1 的全尺度非集中结论形式上失败”更强。单一窗口有 affine fit 不等于全局 dense windows、good-q 和后续细化都可用；两个被审稿均明确未跨过这条边界。本条件定理因此有实质内容，但不能登记成无条件取得 actual alternative。

## 2. 原 V/J/L 质量与 horizontal2 幂

写 α=2−κ、m=#Z(q)、e=#E(q)。合法 good-q 给

    e≈K^(±1)m(ρ/δ)^(α+2)，
    #T(q)≤Kρ⁻κ(ρ/δ)⁴，deg(p)≈K^(±1)δ⁻κ。

逐 fine Φ-bin 取一实际 witness 后，原 incidence I≈eδ⁻κ，原 d_T 的平方和满足

    Σ_T d_T²≥I²/#T(q)≥K⁻¹eδ⁻κm。

这是真实 one-arm 加权质量。V 通过 (p,z′) 的 CS 得 lower K⁻¹eδ⁻²κm；不要求每管有 m 个 marks。J 的权重为中间 grain 上 incoming/outgoing one-arm 权重之积；因为 incidence 对两端对称，确可写成

    J=Σ_grain(Σ_{p∈grain}B_p)²。

中间 grain 总数≤Km(ρ/δ)^α，结合 e 的 lower，得到

    J≥K⁻¹eδ⁻²κm²(ρ/δ)²。

若 ρ max|E(z,z′)|≤cτ，固定 p,z,z′ 和 translated horizontal τ-bin 后，由原(176)可知两个 translated 中间点 physically O(τ)-close。原 ξ/Φ coherence 给 terminal directions 的共同 τ-carrier；signature 数至多

    K e m²(ρ/τ)²τ⁻κ。

再 CS 给 L≥K⁻¹eF_Lm²，其中

    F_L=δ⁻⁴κτ^κ(ρ/δ)²(τ/δ)²。

上式是实际 horizontal2，而不是从旧 scalar-Y 的符号直接抄来。非允许 τ 的邻近 allowed scale只付 δ⁻O(η)，并须计入 K；A 已列明。

## 3. Code 重数、同一 frame 与角差

A 的 code fibre 各项乘积为

    (ρ/δ)² · δ⁻κ · (ρ/δ)² · (ρ/δ)^{2κ}
            · (τ/δ)² · (τ/δ)^κ
      = F_Lρ^{2κ}(ρ/δ)²，

再付 K。这来自两次 actual horizontal 选择、fine original witnesses 和 terminal τ-angle cap；不能按 y 的二维坐标分别选择世界。

对 z″平均、使用 #tildeY_z″(q)≤K(ρ/δ)^α 与 #Φ_q≈K^(±1)ρ⁻κ 后，graph density 的剩余比值恰为

    e/[m(ρ/δ)^(α+2)]≥K⁻¹。

因此 bounded g 位于同一个 vector-Y × Z² × scalar-Φ² frame 上。coarse Φ_q 为标量 κ-AD，可以在 |ψ|≥K⁻C≫ρ 的尺度直接使用 interval cap；原 time packing 同样控制 |z−z′|<K⁻Cρ 的 reference mass。由于 g≤1，删除这些小 reference sets 保留 K⁻C 原质量，之后 averaging 才固定实际 y,z′,φ pair。

原(180)的两终端顺序和 graph 正负号必须一致。交换两条 ordered paths，或选择另一终端作输入 y，重数和质量不变。root 现已明确 ψ=φ₂−φ₁，使其所写 `(z′−z)E(φ₁−φ₂)` 对应正号 cubic；该修复通过。

## 4. 全窗口振幅，而非离散样本直径

h=v−b(z₀)u 的原振荡≤Kρ。原 retained samples 有 K⁻Cρ 的 span，并可选择三个相互分离 K⁻Cρ 的 times。逐坐标 quadratic 插值因而给

    ρ|A₁|+ρ²|A₂|≤K^C(ρ+Δ)。

把 Δ=ρ^ε(ρ²+ρ|A₁|+ρ²|A₂|) 代入、以 K^Cρ^ε≪1 吸收，得 Δ≤K^Cρ^{1+ε} 和系数总量≤K^Cρ。加上 |c(z′)r|≤K^Cρ 后，完整 cubic window 上 R≤K^Cρ²≤1。该步骤确实控制整个 polynomial，而不是把稠密样本之间的 diameter 当 R。

只归一化 domain，d₀=δ/ρ。于是

    d₀R≤K^Cδρ≤δ≤e，
    e=K^C(τρ+δ+ρΔ)。

K^Cρ≤1 由 ρ≤δ^μ、全部 loss 足够小获得。若 e≥1 或一个固定平凡阈值，直接 R≤1≤C e 即够；其余 e<1 可用 finite PCT。由于 P(z′)=0，oscillation 同时控制绝对 sup。

## 5. Physical tube-KT 与常数修正

源 Def17.3 的 tube-KT 基底是 physical δ；Def17.4(4) 的对象维数 d−k，正是这里 R² 中的 tildeY。选同一 terminal 层的 q-subset、平移减 y 只继承 upper，不需要新的 AD lower。原文局部“rescaled δ/ρ-AD”的叙述不迫使把空间也除ρ。

因为 e≥δ，PCT 的全部 e′≥e 查询都在原 tube-KT 范围内。源 dyadic covering 与 finite PCT 的球 covering 只差固定维常数；相邻尺度和固定倍 tube 宽度也只付固定常数，但这些常数必须位于 2/γ 幂内。

原幂外常数的一致形式已由本轮有限反例否定。修正版实际给

    R≤K_γ(τρ+δ+ρΔ)，K_γ=δ⁻C_γϑ。

γ 先固定，fixed C^{2/γ} 由最后 δ 小吸收；所有 1/γ 费用在 C_γ 中保留。finite PCT 的非闭 Y witness 已改≤2e，preimage 区间仍是 O(e)，不改变任何幂。

## 6. 向量 cubic 系数与 τ 稳定化

归一 z-coordinate 后，最高次系数为 ρ³A₂ψ；二次项恢复 ρ²(A₁−c(z′)r)ψ。z′在 unit window 内、|ψ|≥K⁻C，有限系数范数常数统一，得

    |A₂|≤K_γ(τ/ρ²+δ/ρ³+Δ/ρ²)，
    |A₁−c(z′)r|≤K_γ(τ/ρ+δ/ρ²+Δ/ρ)。

同一 good z′ 对其余全部 retained z 可代回 E，得到 ρ|E(z,z′)|≤K_γ(ρτ+δ+ρΔ)。因此下一候选集可取这些 good z′，并非分别挑选坐标。

稳定化必须以原全局 retained times 为母集；每 window 的 good-q 和 good z′ 只丢 K_γ 固定幂。root 的条件4明确要求该有限细化合法，A 给出其原质量计数，不从一个单独 window 冒充全局密度。令 θ_{j+1}≫C_γθ_j，并先固定 M≥20/ε；初始 θ₀可选小到所有有限 j 都满足 μ、γ 预算。

若所有 τ_j>ρ^{3+ε/2}，从 τ_j≤Kρ² 的有限乘积比较选相邻稳定 j，得

    τ≤K_γρ⁻ε/10(δ+ρΔ)。

系数式与 Δ 定义又给 Δ≤K_γρ^ε(ρ²+τ+δ/ρ)，故

    τ≤K_γ²[δρ⁻ε/10+ρ^{3+9ε/10}]

（τ 项先吸收）。allowed ρ≥δ^{1/4} 给 δ≤ρ⁴；小 ε、K_γ≤ρ⁻o(ε) 后确得 τ≤ρ^{3+ε/2}。没有漏掉 γ 固定后选所有 losses 足够小的顺序。

## 7. 非零 scalar r、整列 b 与19.4

在原 surviving times 选一对 gap≥K⁻Cρ。whole-f affine fit 和 τ-collapse 给

    |s|≤K|r|+K_γ[τ/ρ²+ρ^ε₀]。

误差相对 named whole velocity 下界 K⁻¹ 足够小，推出 |r|≥K⁻C。这里确实使用了 s∈R² 的向量估计；没有把非零 (r,s) 偷换成非零第一坐标。

E+swap 的精确恒等式为 `(b(z)−b(z′))(u(z)−u(z′))`。对分离 pair 代入 affine u，先用原 osc b≤Kρ 控制乘上 affine error 的项，得到

    |(b(z)−b(z′))r|≤K_γ[τ/ρ²+ρ^{1+ε₀}]。

近 pair 可经一个共同远 anchor 连接，packing 和 surviving span 保证它存在。r 为标量且已有下界，因而控制**整列** b，osc b≤K_γρ^{1+ε/2}。这与 mixed42 遗留正交 row 的情况不同。

root 与 A 终稿均在原坐标直接用 `a(z)−a(z′)=E(z,z′)+[b(z′)−b(z)]u(z)`，给 osc a≤K_γρ^{1+ε/2}，足以控制整个原 tildef。A 已删去非必要的新 axis-aligned chart 和 a≤Kρ² 强化；终步没有额外坐标变化的费用或该强化的依赖。

σ=ρ^{1+ε/4} 在 [ρ²,ρ] 内，且 ρ≥δ^{1/4}≥δ^{1/3}。某原 window 的 good times 数≥K_γ⁻Cρ/δ、原 times 数≤Cρ/δ，所以19.4所需相对原 density 为 δ^{C_γϑ}。直接对原配置及该 cluster 调用，给

    C_CW(T)≥δ^{C_γϑ/γ}ρ⁻κε/4
               ≥δ^{C_γϑ/γ−μζε/4}。

所有 losses 在 γ、μ、ζ、ε 固定之后取小，使该指数严格小于−η，与原 CW upper 冲突。整个终步没有使用原PDF99未支付的 ρ^{2+ε/2} 行变差。

## 8. 最终范围

本轮新增且已自包含核验的是 finite polynomial tube-KT 机制；被审应用则是完整实际 mixed32 数据上、明确固定尺度准备和 named 高级输入下的条件 quadratic 排除。原 graph/mass、physical 尺度、标量 r 和19.4链条未发现剩余费用或方向错误。

但 fixed-scale 全局 affine/nondegenerate 准备及其 stable closure 仍有单列 source 责任；原 all-scale 声明不能直接充当它们的已证来源。非二次 alternative、其他五维分支、general-to-sticky/Hausdorff 和一般维度均未完成。本审查不认证新颖性、重大性或最终 Goal 完成。
