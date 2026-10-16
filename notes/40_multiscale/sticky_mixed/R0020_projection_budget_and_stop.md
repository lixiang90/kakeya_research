# R0020：完整父管的抵消、稀疏时钟障碍与局部投影停止决定

2026-10-17。主任务仍为 N5-MIXED42-Q01。本稿整合两个独立方向的审查；证明的是特定 transfer 的预算和适用边界，未解决完整 mixed42，更未解决五维 Kakeya。

## 1. 固定原对象，先支付合法的抵消

用 K 记录本轮明确保留的 δ 的小幂损失；κ、ε 等先固定，不能将固定的 ρ 幂任意吸收进 K。完整原管族 joint 四维 AD，且 normalized whole-tube convex Wolff 常数至多 K。对于一个真实 τ-parent，若保留其完整子管族，质量为 K^{±C}τ⁴。减去参考轴，再将四个空间轴除以 τ，时钟保持原值。此固定仿射变换的体积行列式是 τ⁻⁴。

若变换后的凸集 U 含完整变换原管，它的逆像凸集体积是 τ⁴|U|。原 CW 和父族质量下界因此给条件原权

    ν_parent{T': T'⊂U} ≤ K^C |U|.

这是实际的抵消，优于不看父族来源而直接写 τ⁻⁴。它只对完整 parent 成立。任意按 q、marks 或标签删出的子族，不能借此免费重置成同一 AD/CW 概率。更不能将包含短片段的凸集，误认成包含原完整管。

## 2. 保持时钟：可证的误差分辨率与真正的 shading 门槛

R19 的保守局部归约只在长度 ρ 的时间窗口 J 上有效。已知平行 row 的振荡至多 w=K^Cρ^{1+cε}，正交 row 可以保留为 β(t)。本段取 τ≤ρ，尤其 A 稿实际选出的 τ=ρ parent。参考轴之外的空间变量宽度为 O(τ)；剔除已知 row 的常值部分后，已付误差为 O(τw)。空间除 τ 后，现有证明只认证 O(w) 的误差。因此，在没有新消去式或更强实际误差估计前，稳健工作半径必须取 s≳w。减小 τ 不改善这个比率。τ>ρ 时 q 内变量可更窄，这个误差比率不能照抄；其 active 子族质量也须另付，见 A 稿的较大 parent 讨论。

完整原时钟上的 marks 只在 J 中，每个 s-time cell 占有量有界，于是当 s≤ρ 时粗 shading 密度至多 Cρ；一般 upper 是 C(ρ+s)。该 upper 也适用于原 marks 在 J 内很密的最有利情形。不能由整管几何推出 λ≈1。

GWZ 2601.14411v2 Lemma3.7、KKT 参数 β=0 的输入要求 λ≥s^{η_G(ε_G)}；其结论为 μ≤s^{-ε_G}Δ_max。η_G 不是可以按需要放大的参数。以下校准给出必要条件

    η_G(ε_G) ≤ ε_G/2，  0<ε_G<1.

取三维图方向 v∈[−c,c]² 的 s-grid，普通单位 s 管轴 x=t v 全部过原点。在 t=1/4 的端点双 Lipschitz 及凸锥体积比较，给 Δ_max≤C；管数 N≈s⁻²。标记 |t|≤r 内的部分，s≪r≪1，则每管密度≈r、总标记体积≈r、union≈r³，所以 μ≈r⁻²。若 η_G≥1，先取 r≈s 即已与 ε_G<1 矛盾。因此 η_G<1；再取 r=s^{η_G}，令 s→0，结论迫 2η_G≤ε_G。固定常数可由任意严格指数余量吸收，不改变必要不等式。

欲与 κ 缺口冲突需要 ε_G<κ<1，而 cε 足够小。现有稳健 s≳K^Cρ^{1+cε} 使

    λ≤Cρ ≪ s^{η_G(ε_G)}

（这里 s≤ρ；先使 K 的指数足够小，且 (1+cε)ε_G/2<1）。所以“完整 parent、小 CW、单局部窗口、原时钟、直接套 Lemma3.7”的接口失败。更粗且仍小于 ρ 的 s 只提高 density 门槛；若 s≥ρ，λ≤Cs 仍不足 s^{η_G}，因为 η_G<1。更细 s 则超出现有误差认证。这里否定的是已知误差下的直接调用，不断言真实 row 误差一定达到 w，也不排除不同投影、不同 marks 分配或更强 source 消去。

## 3. 放大时钟：真正从 source 得到的端点成本

将时间窗口也除以 ρ，可把原 dense marks 变成 λ≥K^{-C}。但此时必须重新估计完整 projected short tubes 的凸集中；不能沿用第1节的 whole-parent 结论。

A 稿 R0020_parent_packet_audit.md 给出两种合法 upper：完整管的凸包延长法给 D≤K^Cρ⁻²；利用实际原点集 (5−κ)-AD upper、一个 good parent 内的点方向 degree cap 和原 incidence 双计数，进一步给

    D_s ≤ K^C min(ρ⁻², s⁻κ),    λ≥K^{-C}.

第二项的几何本质是：三维 unit-length 凸 U 的 John 轴长为 (a,b,1)，s≤a≤b≤1。其五维 lift 的两个自由坐标有界，以 O(b a⁻⁴) 个五维 a-cubes 覆盖。实际点概率对一个 a-cube 的 upper 为 K^C a^{5−κ}。原 incidences 除以同一个 parent 管数和原每管 marks 后，得到 tube-weight upper K^C b a^{1−κ}。再除凸体体积≈ab 即为 K^C a⁻κ≤K^C s⁻κ。整个证明只数被凸集包含的完整 projected 短轴对应的原 marks；没有偷用 original whole-tube CW 到短片段上。

这是真正改善，不再是未知 p⁻¹ 的代数改写。然而在当前 s≈ρ^{1+cε} 下，s⁻κ 是较好的项，因而所能保证的 λ/D 只有 K^{-C}s^κ。GWZ 下界 s^{ε_G}λ/D 与 slice upper s^{κ−a} 不矛盾：没有留下严格的 κ 余量。

点 AD 的这个 covering 步骤本身不能免费增强。取 R⁵ 中四维 Lebesgue 概率与一个 α=1−κ 的常数界 AD Cantor 概率的积；一个 Cantor 方向宽度 a 的 slab 的质量≈a^{1−κ}，体积≈a，故其集中比≈a⁻κ。这只是 AD-cover 校准，不是带满方向、Φ coherence 和 tube CW 的 source 反例。

## 4. 真有限管族进一步否定免费 transfer

B 稿 R0020_local_transfer_counterattack.md 构造

    ℓ_{a,b,c,d}(t)=(d+ta, tb, (1+t)c, td, t).

原族有满四维方向、joint4-AD、常数界 whole-tube CW。一个真实 ρ-cube 内的自然 packet 原质量≈ρ²，且有同一组 ≈ρ/δ 个原 marks。cube 归一化后 λ≈1，局部水平三 grain 完整；保留全部原权、明确合并 projected representatives 后，指定固定三维投影的最优 D≈ρ⁻¹，union≈ρ。

令 ρ≈s^{κ_*}，则单尺度薄集 cover 缺口是 s^{κ_*}，而 λ/D≈s^{κ_*} 恰饱和。故环境 CW/AD、满方向、满三 grain、原共同时间与单尺度 slice cover 这组输入不足以给严格余量。反例没有实际 source 的跨尺度薄集 AD 和宏观 Φ-AD；B 稿量化这两个缺项。它不是完整 source 反例，也不是 Kakeya 反例。

## 5. 宏观决定

R19 允许的一轮 local GWZ 扩展已完成。所得新 source upper 与两个严格接口校准改变了认识，但未闭合完整 mixed42。现在冻结该局部 extension；不以不同 threshold、parent 半径、相同 λ/D 条件或新名称继续同一个 budget。重开须使用额外实际 Φ/ξ/跨尺度结构给严格的 D 改善、额外 marks，或证明不同的真实几何机制。

下一唯一候选换到实际 d5/k3/ell2 quadratic 分支：水平 grain2、scalar Φ、二维薄集。测试 bounded-degree vector polynomial 与原 tube Katz–Tao 是否能代替 source22.4 的 scalar interval argument。这改变实际分支和使用的几何输入；不假设任意 dyadic-Lipschitz 曲线是 C²，不重开矩阵 W/BSG 迭代。精确待证规范见 R0020_next_mixed32_polynomial_target.md。该候选尚未证明；长期 Goal active，完成标准不变。
