# R0115 独立逐步审查：完整 usual-source 的单 clock graft

2026-10-26，r0115_graft_review。审查者未参与本轮 graft 机制的提出、作者证明或前轮 dust 的构造；只编辑本审查文件，root 统一整合。本文是内部独立数学审查，**未经外部同行评审**，不认证 WZ 整篇证明或一般 Kakeya 猜想。

## 1. 对象、恢复和审查范围

实际读 AGENTS、GOAL、STATE、ROADMAP 当前入口、registry 最近项、R0114 轮次、`research/rounds/R0115_full_source_scalar_qualification_spec.md`，及以下证明依据：

- WZ 原文 `literature/extracted/wang_zakharov_2026_sticky.txt` 的 Def3.3、Eq(19)、Def3.9、Def17.2–17.4、Remark17.1，以及 Lemma19.2/19.4 的 statement 和相关 proof。
- `notes/40_multiscale/sticky_mixed/R0022_time_restriction_closure.md` §§1–3；R22 的整 time restriction 是旧已付输入，不计本轮新数学。
- `notes/00_map/R0114_complete_rough_source_new_input_gate.md` §§4–7 的数字 dust、真实整管 CW 和其自身 bulk 失败。
- 本轮作者稿 `notes/40_multiscale/sticky_matrix/R0115_fixed_row_full_source_countergate.md` 全文，及本审查指出的小修后的最终版本。

结论只涵盖作者 §2 明确给定的 bounded joint chart、usual Eq(19) 管规范、d=5、k=ℓ=3、κ=1 的完整 source 类。Eq(19) 是共同 clock u∈[−1,1] 的 bounded-slope 厚 graph；不能把本审查改写成精确 arclength=1 的版本、任意 dyadic parent 的 lower，或对任意无界额外管集的结论。

## 2. 待审条件命题和不存在声明的区别

给定一个假想完整输入 S₀，参数 η、γ₀，K₀=δ⁻η，保原 δ 不变。作者从一个富短 time 区间 I 保留所有整层和全部原 T₀，再在与 I 距离至少 1/2 的 t* 添加单 clock 数字 dust，取 T₊=T₀∪T_d。结论是另一个完整 source S₊，η′=Mη，γ̄≤min(γ₀,γ_d)，其中 γ_d=1−log3/log4，且新增层固定 row e₁ 满足 ξ₁≡0。

此命题是 **S₀ 存在 ⇒ S₊ 存在** 的闭包。它没有证明 S₀ 存在，没有无条件完整 source 或普通 Kakeya 反例，也没有正 source gain。R114 dust 单独缺少 bulk 的反攻仍然有效；本轮 bulk 来自假想 S₀，而非来自 dust 的后继访问。

## 3. Clock restriction 和 coarse Y-union：独立计算

八个长度 1/4 的区间中选 Z₀ 最富的 I，m_I≥m₀/8；t*=±1/2 置于另一半轴，距 I≥1/2。全部旧层内部点、Y、X、Φ、ξ 和 selected witnesses 不动，T₀ 也不删。δ-separated clock 和 E 的分离保持。

最初审查了一个可能的边界风险：I 不必与每个 allowed time 窗嵌套。然而无需这个额外假设。固定原 allowed ρ 窗 J，令 A=∪_{t∈Z₀∩J}Y_t，A′=∪_{t∈Z_I∩J}Y_t。

upper 由 A′⊂A 继承。对 A′ 的任意中心，选一个包含该中心的完整 Y_t。其 B_R 中 fine δ-cover 至少 K₀⁻¹(R/δ)，任一 ρ-ball 至多承载 K₀(ρ/δ) 个 fine cells；故 A′ 的 ρ-cover 至少 K₀⁻²(R/ρ)。R≈ρ 的边界由一个 cell 处理，中心和球半径作固定倍调整即可。因此任意整 time restriction 的 coarse AD lower 成立；这正是 R22 的旧计数证明，未使用任意子集的错误 lower 继承。

η′=Mη 且 M 为固定整数，使新 allowed 格 {δ^{jMη}} 精确为旧格子集。没有把邻近尺度的误差、固定尺度幂或新粗格性质免费赠予新对象。固定 clock 损失由 δ 足小后的 η′ 余量支付。

## 4. 数字 dust、全部尺度 KT/slab 和全 δ 有限化

A 的 base4 digits 为 {0,1}，B 为 {0,2}。固定有界仿射图像 Y_d=c{(r+s,r−s)} 与 Φ_d=c{(v−w,v+w)} 都是 1-AD。每位和均匀遍历四个 digits，故 y₁ 和 φ₂ 各为均匀一维变量，另外坐标可作为该变量的 Borel 函数处理；不假设这些函数光滑。

四角 child rectangle 的每边比为 1/4；宽度足窄于 parent 的任意 strip 至多交三个 child。长 s、宽 r 的 tube 在 s 层只遇固定个 parent，从 s 到 r 的至多三支计数给 tube-KT exponent log3/log4；同一计数给 Φ_d slab exponent γ_d。末端固定层和有界仿射变化只增加固定常数。这核的是 native tube-KT 的全部 r≤s，不是仅全局 slab。

对每个足小 dyadic δ 取 maximal Lδ-separated nets 及 a-grid。Voronoi cells 的自然质量分别 ≈δ、≈δ、≈δ²，support 直径 O(δ)，由 AD lower/upper 和 maximality 得出。产品 cell 质量 ≈δ⁴，故不是仅沿一个4-adic子序列成立。finite AD、KT/slab 通过固定倍扩大的测试 tube/slab、cell 质量和分离继承；r≈δ 用固定维 packing。未见此处连续到有限计数的缺口。

## 5. Dust whole T：joint4AD 与所有凸 U 的 CW

真实同一 graph 为 x(u)=a+(u−t*)φ、z₁(u)=y₁、z₂(u)=y₂+(u−t*)a₂。联合参数与 (a,y,φ) 在固定 chart 双 Lip：由斜率恢复 φ,a₂，再由截距恢复 a,y。故 N_d≈δ⁻⁴，usual N_rT 的计数与参数 r-ball 可比，得到 joint4AD。

CW 独立于 AD 验证。令 v=u−t*≠0，条件在均匀 y₁ 后，(a₂,φ₂)↦(x₂,z₂−h(y₁)) 的矩阵为 [[1,v],[v,0]]，det=−v²；a₁ 的平移经 Fubini 处理。因此 physical R⁴ 点分布密度 ≤C|v|⁻²。固定 v∈[1/8,1/4] 始终落在 u∈[−1,1]，whole graph⊂U 推出这些 slices 均在 U，积分得 μ{whole graph⊂U}≤C|U|。

有限 cell 内 whole graphs 距代表轴 O(δ)。若有限 δ 管⊂凸 U，cell 中轴⊂U+B_{Cδ}。这里正确几何是 U 含一个 **固定 c₁δ-ball**，不是精确半径 δ 的球；凸性遂给 |U+B_{Cδ}|≤C|U|。作者已按审查意见修正。产品 cell 质量 ≈δ⁴ 得 #T_d[U]≤CN_d|U|，适用于所有凸 U，非仅 boxes 或某一 mark。

## 6. Graft 后逐项完整性

有限并的 joint4AD lower 从含中心的 component 继承；另一 component 的 upper 由一个相交中心的固定倍球给出。exact duplicates 只计一次，max(N₀,N_d)≤N₊≤N₀+N_d，故 N₊/N₀≤K₀^C。两个 component 的 CW 分别成立，且 N₀+N_d≤2N₊，所以 union 的 CW 仍为 CK₀。没有再取 maximal tube net 而丢 selected witness。

新层 F=0、p=(a,y,t*)、filled X 为真实 a-grid、ξ=(0,a₂)、Φ=Φ_d；每个 φ 都由上述同一 T_d 见证。旧层原样保持；γ̄ 下的 fine KT/slab 由指数单调性保持。

任一同时含新旧 clocks 的 allowed time 窗，以及任一同时含新旧 E 的 physical ρ-cube，必有 ρ≥1/2。因此 F 跳跃 ≤1≤2ρ，ξ 以 ξ_q=0 容纳时也满足 ≤2ρ；是 strict O(ρ)，未用 Kρ 吞固定 jump。

纯旧 coarse ξ/Φ 用原 carrier；纯 dust 用真实 Lip 的 ξ=(0,a₂) 和恒定 Φ_d 的合法 coarse AD carrier。最终稿明确在每个与 Φ_d 相交的 dyadic ρ-cell 中选一个原 Φ_d 点，故 dyadic ρ-neighborhood 严格覆盖 Φ_d；AD 由 fine-to-coarse 计数及中心的 O(ρ) 移动给出。mixed Φ_q 取完整 [-1,1]²：原定义以 ρ-cover 规定 AD，且未要求 coarse carrier ρ-separated；当 ρ≥1/2，r∈[ρ,1]，其 cover 量和 r/ρ 都只有固定范围，故它确为 (ρ,1,C)-AD，且覆盖所有 fine Φ。不能把这个仅宏观尺度的事实外推至小ρ；作者已明确范围。

coarse Y-union 的纯旧部分见 §3，纯 dust 由单层 coarsening；mixed 部分 ρ≥1/2 时任一非空 bounded Y 集的 coarse cover 都有固定 AD1 常数。k=ℓ 时 consistency 为空块恒等式。上述有限幂和固定常数由 Mη 支付，δ 坐标和真实管长度均未重置。

## 7. 原 N、访问 I 和平均/逐管的核对

每个留存旧层有 ≥K₀⁻Cδ⁻³ 个 points，每 point 至少 K₀⁻Cδ⁻¹ 个 distinct witnesses（将 Φ 先取固定倍δ分离，吸收原 O(δ) slope 误差）。一根管在固定 time 只碰固定个 δ-separated points，故 I_t≥K₀⁻CN₀，且 I₀≤CN₀m₀。因此 I_I≥K₀⁻CI₀；不能称保原 I 的固定比例或不损失。

N₊≤K₀^CN₀、m₊≈m_I 给 I₊≥K₀⁻CN₊m₊。canonical δ-cube marks 的体积是每 incidence ≈δ⁵，whole graph 管体积 ≈δ⁴，故平均 shading density ≥K₀⁻Cm₊δ≥δ^{C′η}。只得到平均；新增 dust tubes 在旧 clocks 可完全没有 selected visits，未假装每管稠密。

这里增管时 q=N₀/N₊，保访问 p=I_I/I₀，密度至少保 pq 倍；一般删管公式 p/q 不适用于此增管步骤。新增 clock 的原 I 比例 ≤K₀^C/m₊≤K₀^Cδ，η 小时为固定正幂小量。因此本构造只反强 ∀grain 标尺的廉价资格，未反“原 I 正质量 good grains”的版本，也不证明那个版本。

## 8. 强标尺与 source 排除的双向量词

新增每 grain 固定 ν=e₁、b=0，任意ρ>0 都有 scalar cap 左侧为1。作者最后自检补了合法尺度端点：可无损令 0<a<1；若原 a 任意正，取 a₀=min(a,1/2) 只缩小原 cap 的测试尺度区间 [δ^a,ρ₀]，不增强假设。故下文ρ≥δ^a>δ，确在 source 的 allowed [δ,1] 内。这个修订已再次实际读回并核对。

若强标尺预先固定此 a,τ,C，则先取 η′=Mη 足小，再取 j=⌊a/η′⌋，ρ=δ^{jη′}∈[δ^a,δ^{a/2}] 且最终 ≤ρ₀。K 费用写 δ⁻C₁η′，有 K^Cρ^τ≤δ^{aτ/2−C₁η′}<1，与新增层矛盾。

固定 0<γ≤γ_d 时 graft 保同 γ：cap 在某个全体足小 η、δ 域统一成立，便排除一个 η 缩小固定倍数后的完整 source 域；反向该 source 域不存在时 cap 真空成立。因此按通常“存在充分小 η”的正幂量词，二者具有同一排除强度，未证明其中任一真。

γ₀>γ_d 时 graft 降级至 γ_d 或更小正 γ；正确推论是低 γ cap⇒高 γ source 排除，不能直接拿只在高 γ 类成立的 cap 测试已降级的新源。这里也没有把完整 κ1 source 排除等同 ordinary 五维满维或本长期 Goal。

## 9. 独审结论及最终版本凭据

**最终通过，限于本文明确范围。** 主构造、严格 coarse coherence、原质量和两向量词通过上述逐项检查。请求的小修是 c₁δ 内球的准确半径及 coarse carrier 的无歧义实现；作者另补 pure-dust carrier 的逐 cell 严格包含和 0<a<1 的合法尺度端点。我已再次实际读回最终稿全文，确认这些修订均已落实，无未决必修项。

最终作者稿 raw SHA256：`3031421946416e39e8f00299192e9e48f5f1645f13a86859b675519598997314`。这是本次实读字节的凭据，不替代数学审查；后续实质改稿须重新审查，LF 规范化导致的字节变化应另行注明。

无 ordinary 新下界、无完整 source 正增益、无真实 Kakeya 反例；不应据本内部审查登记重大结果或完成 Goal。若实际 source 的额外逐管密度、不同 tube 规范或更强指定 γ 被提出，应重新审查，不能以本结论自动覆盖。
