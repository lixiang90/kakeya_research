# R0016：原关联、good cube、L-tuples 与方向辅助集

2026-10-17。本稿只处理 Wang–Zakharov arXiv:2609.22035v1 的完整 d=5、k=ℓ=3 配置。主要补足是原计数的 Cauchy–Schwarz、合法 good-q 选择、dense graph 的重数上界，以及不必假设原 Φ_q 自身 slab Frostman 的修补。没有证明二维 nonlinear expansion，没有独立验证该文全篇或完整 Lemma19.2。

## 1. 源位置、计数约定与参数

原件 literature/primary/wang_zakharov_2026_sticky.pdf；行号指 literature/extracted/wang_zakharov_2026_sticky.txt 按换行符计数，不把分页符另计一行。已读 Definitions3.6/3.9、17.2–17.4、§19.1–19.2 和 §20；渲染核对印刷 pp77、85、87（上一轮另核 pp65、86、88）。关键位置：

- pp65–66，3362–3434 行：完整配置与原管/Φ_p/ξ_p 相容。
- pp76–77，4033–4084 行：局部 (146)、W-path 的 Cauchy–Schwarz。
- pp78–80，4124–4240 行：Lemma19.2 的 slow-variation 分支。
- pp83–86，4381–4520 行：V、one-arm J、L-tuples，(156)–(161)。原文 4487–4489 行略去 L 计数的部分细节。
- pp86–89，4522–4677 行：矩阵 affine Lemma20.2、scalar nonlinear Lemma20.3 与 graph G。

置 h=2、α=2−κ、D=h+α=4−κ。K 表示 δ^(−Cη)，固定次幂仍可吸收入 K 的另一个固定次幂；C 可依固定维数与先前参数，不能把 K 当绝对常数。全过程保持固定 κ、γ。原计数每个实际点—管关联权为 1；下面的 d_T、B_g、μ 都是这些原关联的重数，不是新选的均匀 prior。

取 source 允许的 dyadic ρ∈[δ^(1/4),δ^µ]。对于任意给定的原时间子集 A⊂Z，先按一个长度 ρ 的时间区间 J 选择 A∩J，再选空间 ρ-cube q；不先任取 q 并假设其中各 grain 都 dense。记 E_q 为原 E 在 q 内且时间属于 A∩J 的点，Z_q 为其实际占用时间，e=#E_q，m=#Z_q。保留每个 p 原有的全部 T_p，T_q=∪_(p∈E_q)T_p。

先明确原见证的选择约定：对每个 p 和每个占用的 fine Φ_p-δ-bin，只选一根 Definition17.2(4) 已提供的实际管作见证，保留这些原关联，仍记为 T_p。一个管最多见证 O(1) 个相邻 fine bins；如果配置记法允许额外关联，这里先不使用它们。这是点态关联选择，原 T 管族及其 AD upper 保持原样；没有声称被选中的管族自己重新 AD 正则，也没有额外赋予逐管 dense marks。

原 δ-tube 与每一 z-slice 的交截直径 O(δ)，而 E 为 δ-separated，所以一个给定 T,z 仅有 O(1) 个原关联点。所选 T_p 的方向图与 Φ_p 的 fine bins 对应，固定 p 及一个 fine φ-bin 至多 O(1) 根实际 dyadic 管。因此

    K⁻¹δ^(−κ) ≤ deg(p)=#T_p ≤ Kδ^(−κ).       (1)

若 source 的 Y 标签未取 δ-separated representatives，仍可保留原标签：同一 δ-ball 内有至多 K 个不同 grain 标签。原因是每个完整 grain 原有至少 K⁻¹δ⁻² 个 x 点，而这些 grain 在同一个 y-δ-ball 内的全部原 E 点总数至多 Cδ⁻²。以下 grain 数量的上界吸收这一 K，不合并 grains、不增加原路径。

## 2. 从原加权关联选择 good q

令 n=#(A∩J)>0。source 全局 Y_z 的 α-AD 与各 X_(y,z) 的 global dense 条件给

    #E_(A∩J) ≥ K⁻¹ n δ^(−D),
    I_J=Σ_(p∈E_(A∩J))deg(p) ≥ K⁻¹ n δ⁻⁴.  (2)

Definition17.2(3) 对这个 J 内全部 Y_z 的合并集给 ρ-cover upper ≤Kρ^(−α)；选 A 的子集只减少该 cover。x 方向有 O(ρ⁻²) 个 ρ-cells。f 的 dyadic Lipschitz 给 ||f(z)−f(z₀)||≤Cρ，所以每个 x-cell 与 y-cell 的原像在物理空间只占 O(1) 个 ρ-cubes。故

    N_ρ(E_(A∩J)) ≤ Kρ^(−D).                 (3)

在覆盖这些原点的半开 ρ-cubes 中，直接按原加权关联 I_q=Σ_(p∈E_q)deg(p) 平均，选 q 使

    I_q ≥ K⁻¹ n δ⁻⁴ρ^D,
    e ≥ K⁻¹ n(ρ/δ)^D.                       (4)

这里第二式用 (1)，K 已吸收固定次损失。另一方面，每个实际 z-slice 在 q 内至多 K(ρ/δ)^D 个点：x 可选 O((ρ/δ)²) 个，而 y 落在 O(ρ) ball 内，使用原 Y_z 的 AD upper。因此

    e≤Km(ρ/δ)^D,
    m≥K⁻¹n,
    e≥K⁻¹m(ρ/δ)^D.                          (5)

后续只需 (5)，无需每个局部 grain 各自有 (ρ/δ)² 个点。若 #A≥δ^a#Z，可先在时间区间间平均取 n≥cδ^(a+η)ρ/δ，因而 m≥δ^(a+O(η))ρ/δ；没有逐管 dense 假设。

若 ρ 不在 f/AD 的指定离散尺度上，只能借相邻较大 admissible 尺度的 upper bounds，额外比例至多 δ⁻η，仍付 K 固定次幂；不能未经说明改变原 SM 的 ρ。本稿主证明直接取 source 允许的 ρ。

**边界：**原 §19 对任意 q 直接写 (146)，且后文把每个 X_(y,z)(q) 当 locally dense。仅 X 全局 dense 不形式推出逐 q、逐 grain 下界。本稿不认证这个逐 q 版本；(2)–(5) 给实际使用足够的 good-q 存在性。没有把限制后的 E_q/T_q 声称为新的完整 Definition17 配置。

## 3. 局部管 upper 与 V/J 的总质量

q 内原 coherence 给至多 Kρ^(−κ) 个 coarse ρ-direction bins：ξ_p 在共同 ξ_q 的 O(ρ) 内，φ 属于 Φ_q 的 ρ-neighborhood，f 在 J 内变动 O(ρ)。每个这样的方向 bin 经过 q 的实际管落入 O(1) 个 coarse ρ-tube parameter cells；原 T 的联合参数 4-AD upper 给

    #T_q ≤ Kρ^(−κ)(ρ/δ)⁴.                  (6)

令 a_(p,T) 是原关联的 0/1 指示函数，d_T=Σ_(p∈E_q)a_(p,T)，I=Σ_Td_T=Σ_pdeg(p)。精确重数

    R=Σ_Td_T²
      =Σ_(p'∈E_q)Σ_(T∈T_p')d_T
      ≥ I²/#T_q
      ≥ K⁻¹ e m δ^(−κ).                   (7)

最后一步用 (1)、(5)、(6)。不需要每根管有 m 个 marked times；这些 degrees 完全可以不均匀。

V：令 v_(p,z') 为从 p 经过某个原 T 到 z'-slice 中原点的关联数，Σ_(p,z')v_(p,z')=R。一次 Cauchy–Schwarz 得

    #V=Σ_(p,z')v_(p,z')²
       ≥R²/(em)≥K⁻¹ eδ^(−2κ)m.            (8)

O(1) 的同 tube/slice 交点多重性只影响 K。反向 upper 由 p、两根原管及 z' 逐项选择，得到 #V≤Keδ^(−2κ)m。这补齐 source (156) 的平均下界，不把平均 d_T 偷换成逐管下界。

J：对每个实际水平 grain g=(z',y)，令

    B_g=Σ_(p'∈g∩E_q)Σ_(T∈T_p')d_T.

一个 one-arm path 的两半臂分别是 (p,T,p') 与 (tilde-p',T',p'')，中间两点在同一个原 grain；故**精确**有

    #J=Σ_gB_g²,   Σ_gB_g=R.

局部实际 grain 数 ≤Km(ρ/δ)^α。由 (7) 和 (5) 再次 Cauchy–Schwarz，

    K⁻¹ eδ^(−2κ)m²(ρ/δ)²
       ≤#J≤Keδ^(−2κ)m²(ρ/δ)².             (9)

upper 由 p,T,z',tilde-p',T',z'' 逐项计数，局部 grain 点数只用 ≤C(ρ/δ)²。这正是 d5/k3 的 (159)，且不需要逐 grain locally dense。

## 4. L-tuples：填补省略的 signature Cauchy–Schwarz

给定 δ≤τ≤ρ，保 source 小 variation 条件

    ||(f(z)−f(z'))φ||≤cτ/ρ                  (10)

对所有相关 z,z'、原 p 与 φ∈Φ_p 成立。将每条原 one-arm path 编码为

    (p,z',z'', bin_(c₁τ)(tilde-x'),
                       bin_(c₂τ)(θ(T'))).  (11)

c₁,c₂ 为只依维数的小常数。两条路径同码即有同一个 p、相同 z',z''、中间 x 相距 O(τ)、终端方向相距≤τ，因此构成合法原 L-tuple，重复编码数至多 O(1)。

固定 (p,z',z'') 与中间 x-bin，所有可能 p' 的 y 差由原 V 恒等式 (157) 及 (10) 控制为 O(τ)。移到同 grain 的 tilde-p' 不变 y，故这些 tilde-p' 全落在同一个 Cτ-ball。Definition17.2(4) 在 τ 尺度控制这一个 ball 上的方向 union，给 ≤Kτ^(−κ) 个 c₂τ-direction bins。若 τ 不 admissible，借相邻更大尺度并把相应四维方向盒细分到 τ，比例≤δ⁻η，仍只付 K；不改变 τ。

于是路径签名总数至多

    K e m²(ρ/τ)²τ^(−κ).

对每个签名的**实际原路径数**平方求和，用 (9) 得

    #L ≥ (#J)²/[K e m²(ρ/τ)²τ^(−κ)]
       ≥ K⁻¹ eδ^(−4κ)τ^κ(ρ/δ)²(τ/δ)²m².   (12)

这是所需 lower，没有假定两个近点的方向集有大交；原文那句“平均有交”由 (11) 的平方计数取代。

同一量的 upper 也成立：固定 p,z',z''，选 T₁,T₂（≤Kδ^(−2κ)）、tilde-p₁'（≤C(ρ/δ)²）、tilde-p₂'（≤C(τ/δ)²）、T₁'（≤Kδ^(−κ)）及 τ-close 的 T₂'（≤K(τ/δ)^κ），所有剩余交点在给定 slice 上至多 O(1) 个。因此置

    F_L=δ^(−4κ)τ^κ(ρ/δ)²(τ/δ)²,

有 K⁻¹eF_Lm²≤#L≤KeF_Lm²。对路径任意非负权，signature 的平方和形式仍成立；本稿使用权 1 的原路径。任意删选只有在证明保住相应原 mass 后才能继续使用 lower。

## 5. 原 Φ_q 的 slab 缺口与合法辅助 H

Def17.2(4) 给 Φ_p⊂N_ρΦ_q 及 κ-AD，但没有直接说 Φ_q 的全部 unused cells 都 slab Frostman。原 4569–4576、4650–4651 行直接使用 uniform Φ_q slab；仅凭包含关系不能认定它。以下无需把 Φ_q 重设成完整配置的一部分。

取所有原 marked incidences 的方向混合概率

    μ(b)=I⁻¹ Σ_(p∈E_q)#{T∈T_p:φ(T)在ρ-bin b}.

原每个 Φ_p 的 κ-AD、γ-slab Frostman 与 (1) 给

    #supp μ≤Kρ^(−κ),  μ(b)≤Kρ^κ,
    μ(S_r)≤Kr^γ  (ρ≤r≤1),                 (13)

S_r 为任意平面 slab 的 r-neighborhood；bin center 误差仅扩大其常数。

选一个足够大的固定 B，删 μ(b)<K^(−B)ρ^κ 的 bins，余集 H。被删原概率≤K^(1−B)。故 #H 在 K 固定次幂内可比 ρ^(−κ)，且

    #(H∩S_r)/#H≤K^(B+C)r^γ.                (14)

这不仅是抽象存在 H，还能保原 L-mass：固定一个原 (p,T₁)，其 L 扩展数至多 Kδ^κF_Lm²，逐项选择与 §4 upper 相同但不再选 T₁。因此对任意 coarse bin 集 U，

    #L_(φ₁∈U) ≤ K eF_Lm² μ(U),             (15)

φ₂ 亦然。选择 B 大于 (12)、(15) 的固定 K 损失，删去任一初始方向不在 H 的 L-tuples 后仍保留至少 K⁻¹eF_Lm² 个原 L-tuples。H 是供 dense graph 使用的共同辅助集；没有声称原 Φ_q 自身满足 (14)，也没有重置任意 Φ_p。

## 6. Dense graph 的完整原重数 upper

固定终端时间 z''，把保留的 L-tuple 映到

    (y₁'', z,z', b₁,b₂)∈Y_(z'')(q)×Z_q²×H², (16)

其中 b_i 是原 T_i 的 coarse ρ-bin。给定这个 code，依次恢复原对象，upper 如下：

| 恢复对象 | 上界 |
| --- | --- |
| x₁''，因而 p₁'' | N_(y₁'',z'')≤C(ρ/δ)² |
| T₁'∈T_(p₁'')；其在 z' 的 tilde-p₁' | Kδ^(−κ)，然后 O(1) |
| p₁' 在同一个原 grain | C(ρ/δ)² |
| T₁ 在给定 coarse b₁ 内；原 p 在 z | K(ρ/δ)^κ，然后 O(1) |
| T₂ 在给定 coarse b₂ 内；p₂' 在 z' | K(ρ/δ)^κ，然后 O(1) |
| tilde-p₂' 的 x 在 tilde-p₁' 的 O(τ) 内 | C(τ/δ)² |
| τ-close 的 T₂'；p₂'' 在 z'' | K(τ/δ)^κ，然后 O(1) |

所以每个 code 的原 fibre upper 为

    K N_(y₁'',z'') F_L ρ^(2κ),             (17)

粗略 upper 为 K(ρ/δ)²F_Lρ^(2κ)。固定单个实际 p₁'' 再对所有 z,z',b₁,b₂ 求和，得

    #L_(first terminal p₁'') ≤ KF_Lm².     (18)

与 (12) 配合，(18) 允许在**原质量**上做有限 heavy-fibre 修剪：删终端 slice 点数小于 K^(−B)(ρ/δ)^D 的 slices，以及局部点数 N_(y,z'')<K^(−B)(ρ/δ)² 的 grains。由 (5) 和局部 grain 数 upper，这两类原终端点总数至多 K^(C−B)e，故 B 足够大时所删 L-mass 小于 (12) 的一半。

按原 e_(z'') 加权平均，可取某个未删 z*，使保留的 L_(z*)≥K⁻¹e_(z*)F_Lm² 且 e_(z*)≥K⁻¹(ρ/δ)^D。令 Y₀ 为这些 L-tuples 的第一终端实际 grain 标签。由 (18)、局部 N_y upper、heavy-grain lower，得到

    #Y₀≥K⁻¹(ρ/δ)^α,
    #G≥K⁻¹ #Y₀ m²#H²,                    (19)

其中 G 是 (16) 的无权 image set；(17) 给出其最大重数控制。K 的固定次幂已统一吸收。没有抹去路径重数后免费假设 image 均匀。

原 (161) 保证每个 G-edge 都有原 y₂''∈Y_(z*)(q)，满足

    y₂''−y₁''=(z−z')(f(z)−f(z'))(b₁−b₂)
                          +O(τρ+ρ³+δ).     (20)

右端用 coarse b_i 替代 fine φ_i 的额外误差为 O(ρ² sup||f(z)−f(z')||)=O(ρ³)。在实际 nonlinear 调用 τ=Cδ⁻ηρ²≥cρ² 时，(20) 简化为 O(τρ+δ)；不能对 Lemma20.1 的任意小 τ 免费省掉 ρ³。此标准选择满足 τ≤ρ（取 η<µ 且 δ 小）、τ≥δ，且 (10) 成立。输入 Y₀ 的平移落在完整 Y_(z*)，**不保证落回 Y₀**；不能由 (19) 宣称 Y₀+Y₀ 或 Y₀+aY₀ small doubling。

Y₀ 继承的是原 Y 的 upper、(19) 的数量 lower 及辅助 graph。任意局部 Y₀ 不自动重新满足全套 AD lower，更不自动成为新的完整 source 配置。进一步 τ-window/ρ-resolution coarse graph 由 root 单独核验；本稿不把 fine time spacing δ/ρ 当成 ρ-separated。

## 7. Lemma20.2 与 Lemma19.2 的接口边界

大 slope R 分支可在上述修补后保持原证明：先对原 V-tuples 用与 (15) 相同的边际 upper 保住 H，再选一个 p₁ 使 V_(p₁)≥K⁻¹δ^(−2κ)m。code (z,b₁,b₂) 的 fibre upper ≤K(ρ/δ)^(2κ)，故得到 ≥K⁻¹m#H² 个 code。由 H 的 slab γ，去掉 ||R(b₁−b₂)||过小的 pair 只需 K 固定次幂损失，可选一个固定 v=R(b₁−b₂)≠0，保住 ≥K⁻¹m 个实际时间。

其后二次时间轨迹 y₁+(z'−z)²v 在原 Y 中，除去 |z−z'| 太小的时间用 m≥δ^(a+O(η))ρ/δ 支付实际质量；原 Y_z 的 tube Katz–Tao 可直接在物理宽度 Δ 查询，无需把受限 Y 重新声明 AD 正则。取 ε₀'≤min(ε₀,1/2) 后，Δ≈ρ^(2+ε₀')||R||≥cδ，因为 ||R||≥ρ、ρ≥δ^(1/4)。原 tube KT 查询合法。

这核清了 general-matrix 非零 affine 部分的几何和尺度接口，但**没有独立完成 Lemma19.2**。当 ||R||≤ρ，原 fit 只给 selected times 上 ||f(z)−f(z')||≤Cρ²。要用 Lemma19.2 必须在原配置保这些时间/关联并支付其密度；不能把时间子集默认为新的完整配置。其陈述本来适用任意矩阵尺寸，ρ≥δ^(1/4) 也满足其 ρ≥δ^(1/3) 的范围，σ=Cρ² 在小 δ 时合法。

Lemma19.2 从 W-tuples 转为多个 graph-neighborhood 的填充、再用 convex Wolff 的部分（4174–4240 行）仍为 source 依赖；本稿没有逐步补完该段全部 graph 选择和增长。上文能以相同 incidence-CS 补其 W lower：两边原路径总数至少 K⁻¹eδ^(−2κ)m²，再按 (p,z',z'',terminal ρ-direction bin) 平方，得 K⁻¹eδ^(−4κ)ρ^κm²。但不能把这一个计数补足说成完整 Lemma19.2 已验证。

## 8. 本轮结论与停止范围

已独立补出：原 marked incidence 的 good-q 存在性；(156)/(159) 的平均下界；L20.1 在 good q 上的 signature CS 与 upper；未使用原 Φ_q uniform-slab 断言的 heavy-incidence 辅助 H；dense graph 的逐项 fibre 上界及保原质量的 terminal-heavy 修剪。它们全都保原点、原管和实际路径，没有新增 product/irreducibility/per-tube density 假设。

尚未补完：Lemma19.2 全部凸集 neighborhood 扩张、任意 q/任意时间子集无需重选 good q 的 source 字面版本、二维 nonlinear expansion 与一般五维其余分支。root 负责后续 coarse graph；本稿不抢先把它或 vector 引理当已通过接口。上述内容是源机制修补和有限计数，不是新 Kakeya 界，也不认证文献全证明或新颖性。
