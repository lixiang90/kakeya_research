# R0021：有限 PCT 与条件回传的独立审查

2026-10-17，`audit_four_dimensional`。审查对象为 root 的 `notes/40_multiscale/sticky_mixed/R0021_polynomial_tube_KT.md`，并只读核对 `R0021_conditional_quadratic_exclusion.md`。有限 PCT 的主体证明由 root 编写，本人独立逐步核验；source 接口稿 `R0021_mixed32_source_audit.md` 是本人所写，该部分不标作独立自审。

**结论：修正版有限 PCT 通过，可按其精确量词归档。** 已读的 root 条件应用没有发现必须修正的数学回传问题；它保留了固定尺度全局 affine、whole-velocity 非退化、合法稳定化 graph 和 named Lemma19.4 责任，未证明这些高级准备必然取得。没有认证完整 mixed32、五维 Kakeya或重大/新颖性结论。

## 1. 实际认证的命题

固定 D,m。P:[0,1]→R^m 是次数至多 D 的多项式，R=diam P([0,1])≤1；B 为 d-separated，#B≥θ/d；e≥dR，P(B)距同一 Y 不超过e。对任意 e≤e'≤L≤1，原 Y 在任意 e'×⋯×e'×L 直管中的 e'-cover number≤K(L/e')^(1−γ)。认证结论为

    R/e≤[C(D,m) K θ^(−C(D,m))]^(2/γ).

固定 C 在幂内。这不认证旧式 `C(D,m)[Kθ^(−C(D,m))]^(2/γ)` 对全部γ一致成立；两式在先固定γ时可互相吸收常数，却不是相同的有限一致量词。B 的反例稿保留旧式失败记录，root 终稿已清楚修正。

## 2. 有限次数事实与坏集的离散边界

减去 P(0)，D+1 个固定节点的插值确实给 `||P'||∞+||P''||∞≤C_(D,m)R`。diam 实现点的一项坐标差≥R/√m，所以存在分量 p 的 oscillation≥R/√m，积分上界给 `||p'||∞≥R/√m`；不要求该分量恰在某个样本达到极值。

次数≤n的非零 q，其 sublevel measure b 的 n+1 个测度分位点可选成相邻距离≥c_n b。Lagrange 分母下界遂给 `||q||∞≤C_n a b^(−n)`。该推导只用有限插值，不额外假设 B 均匀。q=±a 的根还保证 sublevel 只有 O_n(1) 个区间/孤立点；d-separated 点在其中至多 b/d+O_n(1)。

当 D≥2，取 α=cθ^(D−1)，可令坏集 `{|p'|≤αR}` 的测度≤θ/8。若 d≤c_Dθ，其边界项也≤θ/(8d)，因而仍留≥cθ/d个 good samples。若 d≥c_Dθ，则 `R/e≤1/d≤C_D/θ` 已被目标吸收，不能在此分支忽略边界项。D=1、q 为非零常数时另行直接处理；root 的分支完整。

## 3. Preimage 重数没有假设全局单射

good set 只有 O_D(1) 个分支；每个分支上 p' 同号且 |p'|≥αR。故对任何长度Ce的实区间I，每个分支内的原 samples 至多 `1+Ce/(αRd)`，对分支求和只付固定常数。由 e≥dR、α≤1，常数项可吸收入 `Ce/(αRd)`。

这恰好控制一个半径C'e的 Y-covering ball 所对应的所有原 B 样本：任意选择的近邻 witnesses 即使重合，也只能对应上述数量。向量曲线可以自交，标量分量可以跨分支折返；证明没有通过它们偷得单射。若 Y 不闭，用2e近邻和固定倍常数即可。

## 4. Taylor 短管与同一尺度的上下界

记 Q=R/e，Q 大于固定阈值时取 u=cQ^(−1/2)。O(1/u) 个 domain intervals 中有一个 J，内含至少 cθu/d 个 good samples。该结论是对原有限样本作平均，不把全局density换成每个window的density。

Taylor 余项≤CRu²=O(e)，切线段长度≤CRu=O(√(Re))。选固定 C₀,C₁ 后，所有实际 witnesses 同在宽 e'=C₀e、长 L=C₁√(Re) 的一根直管中。Q 阈值足够大、R≤1保证 e≤e'≤L≤1；Q 小时目标平凡。导数在切点为0也不构成除法问题，此时任意方向的同样外罩仍有效。

同一管内 cover 的每个球按第3节最多容纳 Ce/(αRd) 个样本，因此

    N_e'(Y∩tube)≥cθuαR/e≥cθ^D√Q.

假设恰在这个 e'、L 上给 upper `CKQ^((1−γ)/2)`，合并为 `Q^(γ/2)≤CKθ^(−D)`。加大只依 D,m 的 C，包含 Q 小与 d≥cθ 的分支，得到第1节的正确结论。没有在 proof 中把长度 L 偷换成1；平方根尺度对指数2/γ实质必要。

## 5. Source 尺度接口的只读核对

实际 carrier 是原二维 tildeY，而非原三维 ℓ-grain Y。WZ Def17.3（文本3386–3389）明确 tube-KT 的基准为δ，查询全部δ≤e'≤L≤1；Def17.4（3426–3429）给维度d−k的 tildeY 此性质。源5196–5198的局部AD“rescaled δ/ρ”措辞不能迫使另将本次PCT空间缩放。

root 条件稿只将 domain 除ρ，故 d=δ/ρ。先用固定次数插值和Δ定义吸收，得到完整窗口 `R≤K^Cρ²≤1`，于是 `dR≤K^Cδρ≤δ≤e`。该顺序正确，既没有以离散样本振幅代替全窗口振幅，也没有把q子集重新声明为AD-lower。子集与平移继承 tube-KT upper；e=C K^C(τρ+δ+ρΔ)≥δ使全部实际查询仍处于原假设范围。

固定γ后，PCT引入的常数及指数费用都进入 K_γ；其损失依γ，后续θ_j必须再取足够小。root没有声称可让γ随δ任意趋0后仍无费用。这个顺序与有限命题一致。

## 6. Root 条件应用的回传与边界

已逐式核对其向量 cubic 系数恢复、稳定化吸收、scalar r 非退化、E+swap和consistency终步。关键接口均保守处理：

- 一个固定 y,z',角差和同一个原z-fibre控制两个坐标，不能各坐标另选世界；P(z')=0使全窗口diam足以控制系数。
- 用有限稳定化后得到τ≤ρ^(3+ε/2)；相关全局删选/低密window责任列为明确输入，没有由单一good-q替代。
- whole `(r,s)` 非零不直接推出r非零；其式(8)先用τ-collapse及原有界b控制s，再合法推出标量r下界。
- E+swap先得整个二维列b的ρ^(1+ε/2)慢变；原坐标中的 `Δa=E+(b'−b)u` 再得a同样慢变。终步没有使用未补证的ρ^(2+ε/2)强化。
- σ=ρ^(1+ε/4)落在[ρ²,ρ]，ρ≥δ^(1/4)蕴含ρ≥δ^(1/3)，可送入所列 named Lemma19.4；γ与全局density的损失保留到最终正CW gain比较。

以上认证的是**所列固定尺度准备下的条件排除链**。固定尺度 globally dense affine alternative、whole-velocity准备和稳定化graph的全局闭包仍有独立source责任；原all-scale21.1声明的形式否定本身不提供它们。有限PCT通过不会自动取消这些边界，也不处理非二次、其他mixed分支或一般归约。
