# R0115 主审定：强局部 cap 已承担完整 κ1 排除

2026-10-26，root。主稿为 `notes/40_multiscale/sticky_matrix/R0115_fixed_row_full_source_countergate.md`；本稿实读其全部九节以及原 Def3/17/19、R22 时间闭包和 R114 数字模型。本轮是资格审定，不是新的 ordinary 下界、source 正 gain、major 或真实 Kakeya 反例。Goal 保持 active，六维 Hausdorff 基线仍 17/4，未经外部同行评审。

## 1. 证明的实际对象

假设给定 d5、k=ℓ3、κ1、本项目所用 bounded joint chart 内的完整 source（原 N≈_Kδ^{-4}）。管用原(19)/Def3.9 usual bounded graph，clock 为 [−1,1]；没有附加每段 arclength 恰为 1，也没有从这个管规范免费推出 ordinary 完整物理方向。T 的原 joint4AD/whole-CW、所有完整 point 层及 native Y/Φ/ξ 责任均为给定输入，不把此证明扩充为未核的无界参数族。

从原 Z 取一个最富的长度 1/4 半轴区间 I，保留其中全部时间层和每层全部数据，原 T 不动。在与 I 相距至少 1/2 的 t*=±1/2 加入 R114 数字组件的一个完整初层，并把该组件已有 CW/4AD 的 whole 管族加入 T。δ 不变；整数 η'=Mη 只取原 allowed 格的子格。

这个操作之所以合法，有四个不可省的理由。完整旧层给保留 Y-union 的 coarse AD lower，不能仅借 subset upper；纯旧/纯新细窗保持各自原一致性；混合 time 窗或 physical cube 的尺度必为宏观 ρ≥1/2，bounded F/ξ 的 jump 因而真为 O(ρ)；只在这些宏观尺度用的 Φ bounded box 容器才确实是 AD1（原 AD 使用 ρ-cover 计数）。没有用 δ^{-O(η)} 偷吞几何 O(ρ) 常数，没有修改 δ 后冒用旧尺度格。

新 whole-T CW 是实际全部凸体包含估计：相对 dust clock 的固定远时钟段上，物理截面密度 ≤C|u−t*|^{-2}，对真实轴积分，再用每个 finite 参数 cell 的概率约 δ⁴转回原有限计数。旧 T 与 dust T 的有限并直接给 CW/4AD，不删 witness、不重新取 net 来赠 AD lower。数字 Y 的 native tube-KT 和 Φ slab 条件已付，不以光滑切线模型替代。

## 2. 强标尺与排除的双向量词

数字 γ_d=1−log3/log4。原 γ≤γ_d 时构造保同 γ；更高 γ 只能降至 γ*=min(γ,γ_d)，随后调用 γ* 处的命题。

新层每个 grain 都有 ξ=(0,a₂)，故固定 row e₁ 上的集中比例为 1。若强∀grain cap 给固定 a,τ>0、有限 C，可先缩小尺度区间把 a 换为 min(a,1/2)，WLOG 0<a<1。后取 η'=Mη 足小，再取 j=floor(a/η')、ρ=δ^{jη'}，则 δ^a≤ρ≤δ^{a/2} 且 ρ≥δ，是实际 allowed 尺度；而 K^Cρ^τ<1，这是实际矛盾。

因此在所列 fixed γ≤γ_d、∃aτC、足小η再足小δ的量词下，strong∀grain cap 已承担 κ1 完整 source 不存在的责任。反向 source 不存在时它真空成立。两者均未获证明；这是一个条件构造闭包及逻辑强度判定。不能把“如果存在 full source 就可造 bad grain”说成无条件 full source 反例，不能把 κ1 分支排除说成整个 ordinary/一般维 Goal 等价。

## 3. 原质量账及本轮没有新增的输入

增管后保原 N 的分母；设 q=N_old/N_new、p=I_retained/I_old，则体积平均密度至少保 pq，而另一个删管场景才用 p/q。保留区间有原近满点/角层，所以 bulk 平均访问质量由旧 source 支付；新增管可只在新 clock 有 marks。源定义没有逐管多时钟下界，不能替它附加。

新 clock 约只占总原 I 的 1/m，典型为 δ；单个 grain 则约 δ/m，典型为 δ²。因此本构造不反加权 good-grain 结论。它亦未证明任何该类正幂结论。heavy 只保总 I/duration，不免费保 filled X、每 point Φ、Y AD 或全部 native coarse 下界。

本轮另两稿的 endpoint-phase 双向换算、ranked-multiplicity 容量与 p² same-T pairs 都是经典计数/排重，无独立新 source 信息。特别 whole-T 的 δ^{-1} 高点重数早由 point Φ₁ 给出；新增 necessary-capacity 写法不算一次正增益。R107 的 F-secants clock law 没有由 ξ 的 phase 运输给出。旧 vector ξ 球 cap 仍是19.4半段，normal rotation 只到4-plane，其 ρ 幂抵消。

## 4. 决策、独审与后继

拒绝将 strong∀grain scalar cap 当成一个比完整 κ1 排除更弱的免费新局部输入；冻结 endpoint-phase、加权平均重命名和这个数字模型的参数优化作为下一主路线。加权版本没有被单层 graft 反驳，但“未反驳”也不是已找到可行方向。

两份独立逐步审查分别存 `research/reviews/R0115_full_source_graft_independent_review.md`、`research/reviews/R0115_full_source_graft_second_review.md`，须以实际通过记录和对应主稿 SHA256 为准；参与 graft 提出者的核对不代正式独审。本人辅助 phase 推导不计本人独审。

下一轮提前 R0116 宏观重选，入口 `R0115_next_macro_without_local_cap_renaming.md`。要求四出口的新资格依据，而非从这个被拒强标尺自动改名继续。无新数学 ID、ordinary/full-source gain 或 major，不完成 Goal；保存真实失败和闭包结果后，按用户指定 10808 代理统一提交同步。
