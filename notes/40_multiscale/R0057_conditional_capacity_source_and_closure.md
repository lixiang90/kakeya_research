# R0057：条件容量的原先验、时间闭包与全分区费用下界

2026-10-17，A 独立推导。已实际恢复 GOAL/STATE/ROADMAP/registry、R57 working spec/macro 及 R56 next；重读 elliptic 原文 PDF9–12（抽取按 `split('\n')` 的 411–630 行）、R15 的 CP/PM 全称删选证明。本稿只检验本轮指定的条件容量—slab 上界聚合，不证明 H5，不反驳 Th2.2，也不登记新数学 ID。未经外部同行评审。

## 1. 本轮命题、原律与停止范围

固定有界二维方形 Q、固定非退化时间区间 I，A、B 独立均匀于 Q，T 独立均匀于 I。原概率为 μ=μ_AB×dt/|I|。令

    U=(A,B),  V=(B,A),  X_t=V+tU,
    (U1,V1)=(A,B),  (U2,V2)=(B,A).

允许任意有限或可数可测 base partition Γ_j，Γ_j 仅依赖 (B,A)，包含于

    {B∈b_j+E_j, A∈a_j+E_j},

其中 E_j 为同一个居中椭圆在两个坐标中的独立平移，长短半轴 δ≤w_j≤L_j≤C；方向、形状、尺度随 j 变化。Γ_j 可以远小于这个乘积盒，也不要求其内部为乘积律。记 p0_j=μ_AB(Γ_j)。允许任意 ν≤μ，可依赖时间，其总质量为 m，分项质量 p_j=ν(Γ_j×I)。

每项使用在固定原 block 坐标（允许共同固定 scalar clock 变换）中的实际 normalized 第一块先验容量常数 K_j。若每包另作 anisotropic 空间坐标变换，physical 终端 cells 和 tests 的回传费用必须另证，本文不将其无费纳入。只允许经如下完整几何 slab 上界聚合：

    S_j={(t,x2):t∈A_j, x2∈a_j+t b_j+C1 E_j},
    C(t,x2)=Σ_j p_j K_j 1_(S_j)(t,x2),                 (1)

其中 A_j 是实际保留时间支持，C1 为固定足够大常数，允许 O(δ) 增厚。证明：对全部上述 partition 和全部 ν，

    ess sup C ≥ c δ^κ m².                             (2)

这是下述完整证明的结论；不是只对某个先选分解的 free-K 失败。即使把所有逐项调用、共同子律和条件时间问题先乐观地授予，(2) 仍成立。因此本轮止于这个上界聚合机制，不续 κ、s 或 packet 数的微调。不排除用实际联合支持而非完整 slabs、改变坐标划分、利用跨包相关性或更强 singleblock 定理的其他策略。

## 2. Th2.2 的精确可调用内容

一手来源为已入库 *Elliptic capacity propagation and Fourier restriction to the sphere*，官方 Sept24,2026 稿。本文只核 PDF9–12 的 Def2.1、Th2.2、§2.2、Lemma2.3，不认证全103页证明。下列是文献声称的具名输入。

固定 0<s≤1、0<κ<1/10，M=2^n，base label 确定二维 U、V。条件于原 label，每个 dyadic depth j 都要求

    max_I Pr(T∈I|label) ≤ M^ε 2^(−sj),
    #{I:Pr(T∈I|label)>0} ≤ M^ε 2^(sj).                (3)

同一椭圆形状、方向而两个独立中心的输入为

    Pr(U∈u+E,V∈v+E) ≤ K Wκ(E),
    Wκ(E)=L^(1+κ)w^(1−κ),  M^(−D)≤w≤L≤1.           (4)

D≥1 固定有限。输出在某个 dominated M^(−o(1)) 子律上同时控制

    Pr(T1=v,U∈u+E,X_v∈x+M^(−1)E)
      ≤ M^(−q+o(1)) K Wκ(E),                        (5)

终端范围是 M^(−(D−1))≤w≤L≤1，v=T1 是 bin 左端点，X_v=V+vU。q*≥1+2s−10κ，所以任何严格 q<1+2s−10κ 可用。**源陈述不是 q*≤1+2s−10κ**；本文只分析该陈述保证的这些指数。固定 q 的一个足够小 ε 阈值对所有有限 D 适用；足够大 M 的阈值仍可依赖所固定的 D。不能令 D 沿同一个内层 M 序列无界后仍直接调用。

bounded 坐标变化、矩形代椭圆和常数倍扩大可由固定覆盖付常数，原文 PDF9–10 已明确。输出是 retained law，不是原 μ 的上界；同一个最终 ν 必须同时用于所需两块。对可数多个 j 的同步保留也不是由“每次可保 subpower”一句自动取得。本费用反攻允许更有利的假设，即所有逐项合法调用都已完成；仍证明 (2)。

## 3. 为什么实际容量 K_j 至少是 1/Wκ(E_j)

交换律上，Γ_j 既把第二块 (B,A) 放在两个 E_j 平移中，也把第一块 (A,B) 放在相同两个平移中，只交换中心。因此，无论 normalized 第一块先验是 ν 在 Γ_j 上的边缘，还是较早一次真实 source 调用的条件先验，只要它仍支持 Γ_j，均有一个同形双椭圆测试承载概率 1。由 (4)，

    K_j ≥ c/[L_j^(1+κ) w_j^(1−κ)].                  (6)

这里未假设 Γ_j=product、均匀性、A/B 在条件后独立或任何 AD lower。若原 source 权重为 r_j≥p_j，则 normalized 较早先验仍满足 (6)，原费用 r_jK_j≥p_jK_j。

对 L_j≤1，δ=M^−1≥M^−D，故 E_j 是合法初始测试。若 L_j 在固定常数 C 内而大于1，可用固定数个半轴 ≤1 的同方向椭圆分别覆盖两坐标；至少一个乘积测试概率为固定正数，其容量不大于常数倍 Wκ(E_j)，仍得 (6)。若两半轴都大于1，用固定数单位测试即可。对 O(δ) 物理误差，可将 E_j 扩固定倍，因 w_j≥δ 不改变 (6) 的指数。若 K_j=∞ 且 p_j>0，费用已无有利上界，不是漏洞。

## 4. 任意时间相关删选的原质量不等式

写 dν=g(P,t)dμ，0≤g≤1。令

    h_j(t)=∫_(Γ_j) g(P,t)dμ_AB(P),
    A_j={t∈I:h_j(t)>0}  （忽略 dt 零集）。

Fubini 给可测版本；0≤h_j≤p0_j。记 a_j=|A_j|，于是

    p_j=(1/|I|)∫_(A_j)h_j(t)dt ≤ p0_j a_j/|I|.      (7)

若 A_j 采用保留质量为正的 δ-time bins 的并集，同一公式仍成立；只是把支持扩大到这些 bins。末端 bin 裁切到 I 或扩大固定倍，常数不变。这里不存在假设 ν 时间独立的步骤，也没有把 p_j 当成 p0_j。

由于 Γ_j 为 base partition，Σp0_j≤1，Σp_j=m。p0_j=0 时 p_j=0；对其余项，Cauchy–Schwarz 给

    Σ_j p_j a_j ≥ |I|Σ_j p_j²/p0_j ≥ |I|m².          (8)

可数 partition 由非负部分和、单调收敛取得。即使每项只支持很短时间，(8) 仍把它的原分母 p0_j 和保留质量一起记账；忽略这一步才会虚得免费短 clock。

## 5. 完整 slab 积分与全分区结论

因为 S_j 使用整个椭圆而非 Γ_j 的真实投影，其 Lebesgue 测度满足

    |S_j|=c_C1 a_j L_j w_j.

结合 (6)，并用 w_j/L_j≥δ/C，Tonelli 给

    ∫ C(t,x2)dt dx2
      ≥ c Σ_j p_j a_j (w_j/L_j)^κ
      ≥ c δ^κ Σ_j p_j a_j
      ≥ c δ^κ m².                                   (9)

所有 Γ_j 非空时，a_j、b_j 距固定有界 Q 至多固定 C；t∈I，E_j 半轴 ≤C。因此全部 slabs 都位于一个固定体积区域。以此区域体积除 (9)，得 (2)。没有为每个 j 另换一个积分域，因而不漏包数。O(δ) 扩大只令左侧更大。

(9) 是对完整上界表达式的 lower bound；它不是对真实 (T,X2) 密度的 lower bound。如果换成可远小于 E_j 的真实细支持，|S_j|≈a_jL_jw_j 这一步不再成立，本文不能据此否定那种新聚合。若 j 不是 base partition 而是随 t 重选的标签，也须另证明原 p0_j 的计数；当前定理不暗含此更大类。

## 6. 单块指数如何与这个费用相撞

在单位终端椭圆测试中，第一块坐标有界，所以只需固定数个 U1 单位测试覆盖。实际调用的上界右侧形如 Σ_j r_jδ^(q_j−o(1))K_j1_(S_j)，其中 r_j≥p_j 是调用前的真实未归一化质量；不能把 r_j 换成较小 p_j 后仍称真实 atom 的 upper bound。以下仅以下调后的数值表达式作实际 RHS 的 lower bound。当前具名陈述保证的指数满足

    q_j<1+2s_j−10κ≤3−10κ.

即便统一取其最乐观端点 q_max=3−10κ，这个乐观数值表达式仍至少在某处达到

    δ^(q_max+o(1)) C(t,x2)
      ≥ c δ^(3−9κ+o(1))m².                           (10)

若仅保 m≥δ^η，(10) ≥cδ^(3−9κ+2η+o(1))。当 η 可任意小，这个证书远大于 H5 所需 δ^(4+σ) 量级；若先把 ν 归一化，则此数值表达式再除 m，其下界为 cδ^(3−9κ+o(1))m，同样不足。更小的 q_j 只使这一 upper-envelope certificate 更大。

关键逻辑是“该上界不能证明目标 cap”，不是“真实 cap 必大”。交换族的真实物理 union 为常数量级，不是小 Kakeya 集；此证明不反 H5、Th2.2、独立的全 R5 定理，亦不声称 source 的最优 q 无法更强。对 κ→0 或极细多包的微调，(9) 已一致记下所有可能收益，故不以它们另开局部轮次。

## 7. 原 time profile、retention 和平均密度

单有 ν≤μ，不会给 normalized 条件时间律 (3)。在原 uniform T 的 s=1 情形，确有一个有费用的修复：令 h(P)=|I|^−1∫g(P,t)dt。删 h(P)<m/2 的整 base fibers，损失至多 m/2 总质量。每个留下 fiber 的条件时间密度 ≤2/m 倍原 uniform 密度，所以任意 δ 以上 dyadic bin 的概率 ≤C m^−1 2^−j，支持数 ≤C2^j。若 m=M^−o(1)，这只改 subpower；若 m≥δ^η，则是 O(η) 误差，须在 source 时间容许误差以内。重标固定 I 为 [0,1) 只付固定常数。

这不表示每个极小 Γ_j 的归一条件律都自动享同一时间常数；逐包需对自己的原质量/保留分母做同样截断。s<1 的双 profile 更不能由 global time 支持大小或一个 upper bound 代替。原 Lemma2.3 是相对于原 reference law 的固定有限轮删选、有限 prefix 与 whole-fiber 例外清理，不能拿它为随意 T/X_T 条件化免费背书。本费用证明特意不需 (3)，所以即使给所有这些额外有利条件，也不能消除 (9)。

ν 的 global mass m 是平均 incidence 密度。整 label 分区并保完整原 Y_i 时，若原来每管有 λ_i≥λ0，则每个子族中余管仍有这个逐管下界；进一步缩 Y_i 或按 T 删选后不自动保持。不能从 m≥δ^η 直接读出所有余管的同一下界，需另付 heavy-fiber 修剪。

## 8. 左端点、薄椭圆、端帽与真实有限几何

source 输出用 X_v，不是 X_T。bounded U 下二者距 O(δ)；对于本轮 w_j≥δ 的第二块 slabs，O(δ) 可由固定 E_j 扩大吸收。单位终端第一块 M^−1E 可以用固定邻格处理；若终端 w≪1，误差 O(δ) 不能免费吸入 δw，须按尺度支付 U-test 与 time-bin 耦合。本文没有提供这个额外 thin-terminal 转换。

交换数据可取有限 A、B 的四维 δ-grid，T 为真正共同固定 clock 的 δ-bins，并保所有这些 bins；各方向 (1,A,B) 在 bounded graph chart 中与 slope bi-Lipschitz。可取常数倍稀疏 grid 使原物理方向 δ-separated，按常数倍 rebin 保记号。实际中点 (0,B,A)，单位方向归一化，取固定短共同 graph clock 使所用段都落在原单位轴内。只使用原单位段的这个固定比例 marks，不向外延长；near-full 门槛 δ^η 在 δ 足够小时允许此固定比例。

若把时间规范为 source 的 τ=t/ℓ+1/2，则 U1′=ℓA、V1′=B−(ℓ/2)A，U2′=ℓB、V2′=A−(ℓ/2)B；反解有 U1′=ℓV2′+(ℓ/2)U2′、V1′=(1/ℓ−ℓ/4)U2′−(ℓ/2)V2′。因此两个第二块椭圆支持仍把第一块放在固定倍同形椭圆内，常数不依 aspect 或 δ。选固定 D≥2，固定覆盖中最小半轴 cδ≥δ^D（δ 小）即可落实 source floor，不依赖 D 逃逸。

有限版本中 μ_AB 是均匀计数概率，g 为非负 dominated 原 incidence 权；(7)–(8) 是求和恒等式。K_j 的支持测试仍承载概率1，(9) 对虚拟连续 slabs 积分，因此不依赖把原 discrete prior 宣成 continuous。O(δ) jitter 可另作 bounded cover，但核心费用无需它。固定 chart、固定 clock 的常数缩放使两块支持椭圆只扩固定倍，由 (6) 记录；不因此声称任意 global rotation 后仍是同一 coordinate split 的全称定理。

实际 round endcaps 若保留，仅增加固定数邻接 time/spatial bins；也可只使用单位轴内部已有固定比例 marks。本文不删选某个有利 endpoint 后把其 mass 重置。连续原律和有限计数各自有完整原分母，不能把虚拟 slab 面积当原 shading 体积。

## 9. 与 CP/PM 旧量词的排重

已实际重读 R0015_mass_pruning_attempt §§2–4 和 R0015_uniform_shading_closure §§1–3。旧 CP 对全部原 dense selections 一致成立时，可删 low cells 后再调用；若 high cells 保至少一半原 incidence，high-cell 数 upper 与 CP gain lower 矛盾。因此 CP(σ)⇒任意 τ<σ 的常数比例 PM(τ)，反向由 low multiplicity 除质量得 CP。whole-cell 删选保原几何、方向、anchors 和平均 dense 输入，未必保逐管长 marks。

所以“条件时间后的联合增益”“低重数质量”“restricted weak-type”若对相同全部原 shadings 统一且闭包可用，不可只换名称当不同数学目标。本轮只因新 Th2.2 的实际 all-s 输入而测试一个尚未付费的具体证明架构；(2) 给该架构的真实全分区费用，不是重新提出 CP/PM 等价目标，也不反驳未解 CP。

## 10. 已读范围、可审查成果与停止

本稿完整证明 (2)，包括任意可测 base partition、任意 time-dependent dominated 子律、独立中心/同椭圆、原 p0_j 和 p_j、可数求和与 endpoint 常数。它只阻止以当前 guaranteed singleblock 指数配完整 slabs 的 subpower-retention H5 证书。对新的 joint support 机制、非 base 的动态 partition、适应坐标或更强 source 指数，必须另给新的原质量估计，不能把本文称其不可能性。

未重证 elliptic103页，未给 ordinary 高维维数改进、Kakeya 反例或新颖性认证。独立复核尚待 root/B 最终全文与正式 review；本人不自行将此稿列为外部已发表定理。本轮按 spec 停止该带费 slab 组合，长期 Goal 仍 active。
