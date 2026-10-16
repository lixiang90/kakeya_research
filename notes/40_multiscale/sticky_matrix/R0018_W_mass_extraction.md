# R0018：原 W 路径的联合图提取与边缘费用

2026-10-17。已读本轮 working spec、开轮 macro、STATE 及 WZ arXiv:2609.22035v1 §19.1、§21.1。本稿只证明实际 W 计数到有界联合图的质量接口；**没有证明 joint growth，不将这些准备步骤算成完整主目标结果。** κ、γ 固定，完整 source/SM 保留。没有免费调用标量 Theorem21.2 的向量版本。

## 1. 精确输入、原权与尺度

采用 R0016_original_tuple_audit.md 的原 witness 选择和合法 good-q：每个 p 的每个 fine Φ_p-bin 取原管见证，原 ambient T 的联合参数 AD upper 不变；不把删选管族重新声明为 AD。对 source-allowed ρ∈[δ^(1/4),δ^µ]，选实际 q 与时间集合 Z_q，记

    α=2−κ, D=4−κ=2+α, e=#E_q, m=#Z_q,
    K=δ^(−Cη), σ=ρ²,
    F_W=δ^(−4κ)ρ^κ.

K 的固定次幂可改变 C，所有此类成本必须在 η 最后选择时支付；不是 O(1)。原 good-q 保

    m≥K⁻¹ρ/δ,
    K⁻¹m(ρ/δ)^D≤e≤Km(ρ/δ)^D,
    #T_q≤Kρ^(−κ)(ρ/δ)⁴,
    K⁻¹δ^(−κ)≤#T_p≤Kδ^(−κ).               (1)

原 W-tuple 与 source 4050–4052 行完全相同：同一起点 p、三层时间 z,z',z''，两条两边原管路径，最后两管方向 ρ-close。每个实际 tuple 权为 1。未先将路径像、方向差或 endpoint 支持改成均匀 prior。

主推导取 exact multiplicative allowed grid，使 σ=ρ² 也 source-allowed。固定倍邻域用 O(1) 个 σ-cubes 覆盖。若尺度约定需邻近 allowed scale，相关 σ-cover、图误差和 multiplicity 另付 δ^(−O(η))；不能在后续定理中把 O(Kσ) 偷写为 O(σ)。

## 2. 原 W 总数、endpoint upper 与初始方向上界

令 d_T 是原见证管在 E_q 的 marked degree，I=Σ_Td_T。原 incidence Cauchy–Schwarz 给 R=Σ_Td_T²≥K⁻¹emδ^(−κ)。令 B_p=Σ_(T∈T_p)d_T，则 Σ_pB_p=R。故两边路径总数至少 R²/e≥K⁻¹eδ^(−2κ)m²。按 (p,z',z'',terminal coarse ρ-direction bin) 编码，签名数≤Kem²ρ^(−κ)，再次平方得到

    K⁻¹eF_Wm²≤#W≤KeF_Wm².                 (2)

upper 直接逐项选管：从 p 选两个初始管，选 z'，再选第一终端管及 ρ-close 的第二终端管，最后选 z''。每个管/slice 交截有 O(1) 原点。

**固定原第一终端点 u。** 其 z'' 已固定；先选 T₁'（≤Kδ⁻κ）、z'（m）、T₁（≤Kδ⁻κ）、z（m）、T₂（≤Kδ⁻κ）、ρ-close T₂'（≤K(ρ/δ)^κ），其余原点确定到 O(1)。因此

    #W_(p₁''=u)≤KF_Wm².                    (3)

所以完整 W 的实际 endpoint law 被原 E_q 的均匀计数概率支配 K 固定次幂；不是反向 domination，也不是每个 endpoint 都 rich。

固定一个原 (p,T₁) 时，其 W 扩展数≤Kδ^κF_Wm²。因此 R0016 的原 incidence 混合 μ 与 heavy bins 可在 W 上同样使用，得到共同 coarse ρ-direction 集 H：

    K⁻¹ρ⁻κ≤#H≤Kρ⁻κ,
    #(H∩slab_t)/#H≤K t^γ  (ρ≤t≤1),

并在两个初始方向均落 H 时仍保 (2) 的 lower，K 再付固定次幂。只删真实 W-tuples，不赋给原 unused Φ_q cells slab 性质。

## 3. 在原质量上选一个 σ-thick grain bucket

按第一终端时间 z'' 与第一终端 grain 标签 y₁'' 的半开 σ-cell Q 分桶。令 E_(z'',Q) 是桶内全部原点，e_(z'',Q) 为其数量，W_(z'',Q) 为其全部保留的原 W 权。

原 Y_z 的 α-AD packing 给每个 z'' 至多 K(ρ/σ)^α 个占用的 y-buckets。每桶最多

    M_Q=K(ρ/δ)²(σ/δ)^α                     (4)

个原点；这里 x 只用 packing upper。删除 e_(z'',Q)<K^(−B)(ρ/δ)²(σ/δ)^α 的轻桶，所删原点数≤K^(C−B)e。由 (3)，所删 W 权≤K^(C−B)eF_Wm²。选 B 足够大后仍保 (2) 的固定 K 幂 lower。

按剩余桶的**原 e_(z'',Q)** 加权平均，可取原 z*、Q，使

    e_Q≥K⁻¹(ρ/δ)²(σ/δ)^α,
    W_Q≥K⁻¹e_QF_Wm².                       (5)

也有对应 upper，K 幂已统一。后续不把这个桶重新声明为完整配置，也不把它变成一个精确 y-grain。

需要明确两种成本：在选中桶自己的自然 frame 内，(5) 是 K-loss density；但该单桶占整个 W 的比例只能保证

    W_Q/#W≥K⁻¹/[m(ρ/σ)^α].                 (6)

σ=ρ² 时自然 bucket 成本为 mρ^(−α)。它通常是固定幂，而非 K；不能把“局部 frame 仍 dense”改说成“单桶保留全局 K⁻¹ 比例原 W”。

## 4. 厚 grain 的联合 (x,ξ) 支持与原 endpoint law

定义 A_f⁻ 为桶 E_Q 上实际 joint points (x,ξ_p)，A_f⁺ 为同一终端时间 z*、x 仍在 q 内且 y 落在 Q 的固定倍扩大 C Q 上的实际 joint points。source (152) 确保每个所选 W 的第二终端落 A_f⁺；两端只在 σ-thick 邻域，不要求同一精确 grain。

在 σ尺度，固定一个 x-σcell 与 y∈Q，物理 p=(x,y+f(z*)x,z*) 只遇 O(1) 个 σ-cubes。实际 ξ coherence 控制每个物理 cube 内的 ξ oscillation 为 O(σ)。所以输入、输出 joint σ-cells 每个 x-cell 只有 O(1) 个（rounding 情形为 K 个），因而

    #A_c⁻,#A_c⁺≤K(ρ/σ)².

每个 joint input cell 的原 p fibre upper 为

    M_a=K(σ/δ)^D.                           (7)

用 (5) 得 #A_c⁻≥K⁻¹(ρ/σ)²，因此两者 cardinal ratio 为 K，并非免费 AD lower。σ=ρ² 后 #A_c⁻≈K^(±1)ρ⁻²。

选原 q 的水平原点 x₀ 与共同 ξ_q，将 joint coordinates 同除以 ρ，working resolution r=σ/ρ=ρ。input 支持在固定 R4 盒中。其均匀 coarse counting 概率有 2-Frostman upper：normalized radius w≥r 的 ball 只容 C(w/r)² 个 x-cells，每 x-cell 的 joint multiplicity≤K，结合全局 cardinal lower 即得≤Kw²。

更直接的**原 W endpoint 概率**也有同一 upper。由 (3)、(5)，条件于选中桶后的路径 endpoint law 满足

    μ_(W,Q)(U)≤K #U/e_Q                    (8)

对所有桶内原点 U 成立。一个 normalized joint ball 半径 w 的 preimage 至多 K(wρ/δ)²(σ/δ)^α 个原点，除以 (5) 得 μ_(W,Q)(ball_w)≤Kw²。这里控制的是原按 W 重数的 law，不是先用 uniform support 替换它。

## 5. Joint graph 的精确恢复上界

把每个桶中原 W 编码为

    (a,z,z',b₁,b₂)∈A_c⁻×Z_q²×H²,            (9)

其中 a 为第一终端的实际 joint σ-cell，b_i 为初始管的 coarse ρ-bin。给定 code，恢复表为：

| 原对象 | 数量 upper |
| --- | --- |
| p₁'' 的 x、y、ξ，已限制 a 与 Q | K(σ/δ)^D |
| T₁'∈T_(p₁'')，及其 z' 原点 p₁ | Kδ⁻κ，随后 O(1) |
| T₁ 在 coarse b₁；其 z 原点 p | K(ρ/δ)^κ，随后 O(1) |
| T₂ 在 coarse b₂；其 z' 原点 p₂ | K(ρ/δ)^κ，随后 O(1) |
| ρ-close 的 T₂'；其 z* 原点 p₂'' | K(ρ/δ)^κ，随后 O(1) |

故每个 code 的最大原路径 fibre 为

    M_code=K(σ/δ)^D F_Wρ^(2κ).              (10)

置 g(code)=原 fibre 数/M_code，精确保总权 W_Q/M_code 且 0≤g≤1。由

    (ρ/δ)²(σ/δ)^α
       =(ρ/σ)²(σ/δ)^D,

以及 (5)、#H≈K^(±1)ρ⁻κ、#A_c⁻≈K^(±1)(ρ/σ)²，得到

    Σg≥K⁻¹#A_c⁻ m²#H².                    (11)

这是实际 original W quotient 的有界 dense graph，没有假定输出独立或丢掉大重数后重新赋均匀权。

原 (151) 与 coarse direction error 给每个正权 code 的实际 joint 输出 a'∈A_c⁺：

    a'−a=M_(z,z')(b₂−b₁)+O(r),
    M_(z,z')=((z'−z)I₂ ; f(z)−f(z'))/ρ.     (12)

这里 ; 表示竖直堆叠，M 是 4×2 矩阵。f 在 allowed J 上 Lipschitz，||M||=O(1)。fine φ 换成 coarse b 的 raw error O(ρ²)=O(σ)，除以 ρ 后为 O(r)。若用了非 exact source grid 而只有 Kσ 误差，(12) 必须相应写 O(Kr) 或另证分辨率修补。

Z_q 目前是原 fine times，其 normalized spacing 是 δ/ρ，不是 r。若后续定理要求 r-separated B，须再对同一个 σ-time partition 聚合/删除 heavy fibres，并支付其原 mass 与 SM 回传；本稿不把 fine 时间 cardinal 当成已分离 coarse cardinal。

## 6. 两种方向 prior 必须区分

**有界 product frame。** 由 (10)、(11)，所选 W 的 coded joint 概率被

    Uniform(A_c⁻)×Uniform(Z_q)²×Uniform(H)²

支配 K。它只是一个有证明的 dominating reference measure；原相关性全部仍在 g，不声称实际端点或两方向独立。于是 clipped W 的 direction-pair marginal≤K Uniform(H)²，difference law 的 slab upper 也可付 K 后使用。endpoint 与 time-pair marginal 同理。这一步实际依赖恢复表，不能仅从 #W 多推出。

**raw 同 p 方向 pair law。** 若 ν_q 另定义为 Σ_p 的原 T_p×T_p 混合（归一化因子 Σ_pdeg(p)²），固定 (p,T₁,T₂) 的扩展 upper 为 Kδ^(2κ)F_Wm²，所以整体 W pair law≤Kν_q。但选定 Q,z* 后，现有估计只保证

    (pair law | Q,z*) ≤ K m(ρ/σ)^α ν_q.     (13)

这是由 (6) 的条件化费用；尚未证明同一个 raw ν_q 在任意所选桶中只付 K。Uniform(H)² 与 raw ν_q 可以有不同 pair correlations，不能把它们写成相同 prior。使用前者是经 (10)–(11) 支配证明的 quotient frame，不是未验证地把 rare 原 pair 变成独立常见 pair。

## 7. 精确 grain 不能由当前计数免费选出

厚桶 Q 可能容纳 K^(±1)(σ/δ)^α 个实际 y-grains。当前 upper/lower 与原 endpoint domination 允许其质量在这些 grains 间均匀分布。单个精确 grain 能得到的仅是自然比例 (δ/σ)^α；κ<2 固定时，σ=ρ²≥δ^(1/2)，这是至多 δ^(α/2) 的固定幂，不能在任意小 η 下称为 K loss。

这严格指出一个计数推断的界限：原 AD＋现有 W marginal bounds 不直接提供一个精确 common grain 的 K⁻¹ 原质量。它不是满足完整 source/SM 的反例；额外原几何也许迫使更集中，目前未证明。σ-thick 的 coarse joint graph 已足够满足 (7)–(12) 的覆盖和质量接口，不应无需要求 exact grain 再暗中丢质量。

## 8. 本轮实际结论与未闭合处

已证明从完整实际配置提取 σ-thick joint 图的 bounded weights、原 endpoint domination、共同 H frame 的方向 domination，并列出单桶全局比例、raw ν_q 条件化及 exact grain 的真实费用。全过程不重置 AD lower，不赋独立 endpoints，不增添 C²/irreducibility，也不使用 scalar21.2 的向量推广。

**尚无 joint expansion/flatness 或 κ 的新上界。** 二维 cover、2-Frostman upper、(12) 的 joint time-matrix identity 及有界 g 不能被当作已经取得平面集中、small convolution 或共同 subspace。此稿是必要接口准备，不是主轮最终增长成果。开轮 macro 的停止条件仍有效；若 root/B 没有额外真增长或严格反模型，应停止该局部机制，而非继续优化这些归一化费用。
