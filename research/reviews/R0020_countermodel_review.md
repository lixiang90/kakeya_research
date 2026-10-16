# R0020：实际局部投影 transfer 反例独审

2026-10-17，审查者 `/root/audit_four_dimensional`。审查对象为 B 的 `notes/40_multiscale/sticky_mixed/R0020_local_transfer_counterattack.md`。**结论：按稿件第1节明确列出的较弱 transfer 输入通过，可归档。它不满足实际 source 的薄集 AD 和宏观 Φ 条件，不是完整 mixed42 或 Kakeya 反例。** 自己的 parent/source 预算由另外代理审查，不算本文件独立核验对象。

## 1. 有限环境真管与整个凸集的 CW

实际斜率是 `(a,b,c,d)`，固定盒的 δ-grid 有 `N=(r₀/δ)^4` 个参数。截距 `(d,0,c,0)` 与斜率共同双 Lipschitz 读回这四个参数；故 joint 管参数 AD4 是真的。斜率到单位方向的映射在该小盒内双 Lipschitz，因而确有固定体积四维方向盒中的 `≈δ⁻⁴` 个分离方向；不只是形式索引数。

物理单位线段以 t=0 为中心，其 last-direction 分量接近 1，所以全都包含 t=±1/4 的共同轴点。重算固定 time 的 spatial parameter map，行列式为 `t³(1+t)`；在 1/4 是固定非零常数。于是所有轴点周围的 spatial δ-balls 重叠有固定上界，且完整管包含这些 balls。

对于包含若干**整条**原管的凸 U，其 t=1/4 截面面积至少 `c #T[U]δ⁴`。任取被含原管的 t=−1/4 点，与整个截面取凸锥；高度 1/2，5D 体积是该4D截面积的 1/10。故 `#T[U]/N≤C|U|`，没有只证明 marked pieces 的条件。该证明也避开了“方向分离必然给这种凸 bound”未经展开的代用。

## 2. 原 q 子族及 marks 的质量

`c,d∈[r₀ρ,2r₀ρ)` 各占原区间恰 ρ 比例，dyadic 端点和网格对齐，因此 selected S 的原质量恰为 ρ²。按所有共同原 times `t∈[ρ/4,ρ/2]∩δZ` 代入，五个 coordinates 都落 `[0,ρ]` 内部；最小边界距离是第四坐标 `≳r₀ρ²`，而 `n>2m+20` 保它远大于 δ。每管的 `≈ρ/δ` 个标记球是真实原 shading 的子集。

反过来，原管与 q 相交时 clock 只能在 `[-O(δ),ρ+O(δ)]`，由第一和第三空间坐标得 `c,d≤Cρ`，故自然相交族的原质量≤Cρ²。S 是其固定比例的内部 packet，不是另取一个任意小稀有 fibre。

相对原完整单位管，这些 marks 的 density 是 `≈ρ`；常数 density 只在显式裁短 clock 并 isotropic zoom 后出现。稿件没有混用这两个 λ。

## 3. 归一化图、工作尺度与原权代表

isotropic `1/ρ` 缩放后，轴为

    (β+τa,τb,(1+ρτ)α,ρτβ,τ),
    α=c/ρ, β=d/ρ, s=δ/ρ.

这是普通直线，管半径和原时间间距均变为 s。对每个 β 和 τ∈[1/4,1/2]，三个变量 `(a,b,α)` 给三维水平 patch；其三个边长有固定正下界，工作 s-cover 有 `≈s⁻³` cells。a、b 的实际网更细为 δ=ρs，这只增加同 cell 的索引重数，不减少 cover；α 的步长恰为 s。

投影轴 `(X₃,W,τ)=((1+ρτ)α,τd,τ)` 与其参数关系已核。将 d 的范围按 s 半开 bins 分，端点对齐来自 `n−2m−10>0`；每 bin 恰含 `s/δ=1/ρ` 个原 d-values。α 已为 s-grid，a、b 的原 multiplicity 相同，所以 representatives 的**原 pushforward 权**恰均匀，数量 `r₀²ρs⁻²`。不需要未经支付的 image uniformization。若为某外部定理另作固定颜色选择以确保 essentially distinct，只有常数损失，本文双边 estimates 不变。

每代表取 assigned 原管的原 marks；中心 d_j 可用最近原 d（误差 O(δ)），投影 marks 与代表轴相距 O(s)。固定 margin 的 s-tubes 装下这些 marks，没有创造时间。每代表有 `≈s⁻¹` 个 marks，投影 shading volume≈s²，故 λ≈1。

## 4. 最优 projected CF 和 union 的双边值

全部完整代表在共同 W-width Cρ slab 中，因 s≪ρ，体积 O(ρ)、总原权1，给 D≥cρ⁻¹。

上界在 τ=1/4 用 `(α,d)↦((1+ρ/4)α,d/4)`：它固定双 Lipschitz、两个网格步长均为 s，所以截面 s-balls 的重叠有固定上界。代表数≈ρs⁻²，故 contained family 概率≤Cρ⁻¹乘截面积。若凸 U 非空，还含任一代表在 τ=3/4 的点；锥体积比较把截面积压到 C|U|，得到 D≤Cρ⁻¹。fixed-length tube 定义的常数归一化不改此幂。

对于 union 下界，保留时间 τ∈[1/4,1/2]。参数—位置—时间映射

    (α,d,τ)↦((1+ρτ)α,τd,τ)

的 Jacobian 为 `(1+ρτ)τ`，双侧有固定常数界；其逆也一致有界。所选 marks 因而有 bounded overlap，体积 `≈N_P s⁻¹s³≈ρ`。同一 slab 给相反上界。由此稿件的

    D≈ρ⁻¹,  λ≈1,  |union|≈ρ,  λ/D≈ρ

全部成立；这是真实最佳 CF 值，比只写 packet mass 的粗 `ρ⁻²` 条件化上界更精确。

## 5. 单尺度 κ_* 与实际 source 必须严格区分

任意固定 0<κ_*<1 都可用 dyadic 序列令 `ρ≈s^(κ_*)、δ=ρs`；`s≪ρ` 和所需网格条件随 depth 成立。隐藏集为长度≈ρ、工作 s 内已填满的 interval，故其工作 cover 数 `≈ρ/s≈s^(−1+κ_*)`。于是 `D≈s^(−κ_*)` 恰耗尽该**单尺度** deficit，不能自动得固定 b<κ_* 的 λ/D。

但这个 interval 在整个 `[s,ρ]` 范围内局部维数是1。在半径≈ρ 的球中已有总概率1，normalized `(1−κ_*)`-Frostman 常数至少 `cρ^(−1+κ_*)`。若用 AD 的非归一计数 convention，至多把常数变为平方；仍是固定幂，不能化成任意小 η 的 source 常数。

点方向条件也定量失败。t≈ρ 的位置 map 逆范数≤Cρ⁻²，故同一 δ-point ball 的所有原方向落在直径 `w=Cδ/ρ²=C s/ρ` 的盒中。若它们仍满足 source 的全尺度 scalar κ-AD 与常数 K，利用尺度1的 lower 和尺度 w 的 upper 必有 `K²≥c w⁻κ`。代 `ρ≈s^(κ_*)`、`δ≈s^(1+κ_*)`，要求

    η ≥ κ(1−κ_*)/[2(1+κ_*)] + o(1)

才可能有 K=δ⁻η。固定 κ、κ_* 时为严格正数，和 source 可取任意小 η 不兼容。精确点上甚至只通过一条轴；这种微观近邻的有限重数不能补出宏观 κ-AD fibre。ξ coarse coherence 未被额外认证，稿件也未声称它成立。

## 6. 可归档结论和不可推出的结论

本例反驳的是：环境满方向、joint AD4、whole-tube CW、自然 local cube、同一原时间 marks、局部 full3 grain，以及单工作尺度 slice cover，就自动给 subpower projected CF 或低于该 cover deficit 的 λ/D。它不反驳使用真正薄集全尺度 AD、Φ fibre、两 slope/ξ coherence 的 source 定理，也不构成完整实际配置。

全局原整管 shading 的 union 在 t=1/4 附近已有固定正体积；小 union 仅在原质量ρ²、原时间长ρ的局部 packet 出现。不能拿它作 Euclidean Kakeya 反例，亦没有排除其他投影/原多尺度机制。与 A 的 source端点预算相容：A 使用了本例明确缺失的真正 point/grain/Φ 输入，所得仍只是另一个需严格 gain 的端点。

## 7. Root 整合稿与下一候选的范围核验

已读 `R0020_projection_budget_and_stop.md`。原 clock 的3D bush 校准确给 named uniform multiplicity 形式的必要阈值 `η_G(ε_G)≤ε_G/2`：其 Δ_max 有固定 upper，短 clock density≈r、union≈r³、总 shade≈r，故 μ≈r⁻²；取 `r=C s^(η_G)`，严格指数余量排 `2η_G>ε_G`。η_G≥1 则可直接取 r≈s，亦矛盾。常数可由选择 C 和 δ 小支付。

这正是当前 fixed-clock、小 CW、稳健 blur≥ρ^(1+cε) 的单窗口调用失败，不是所有可能 projection 的不可能性定理。root 已确认将该直接方案限于 parent width τ≤ρ，并指向 A 的 larger-parent tradeoff；不能在 τ≫ρ 时既用 q 的较小 marked spatial宽又免费保持整个 τ-parent 小 CW。整合稿对 source point-cover sharp calibration与 B 反例的边界均正确。此处未以自己 A 稿代替其独立证明审查。

另已只读 `R0020_next_mixed32_polynomial_target.md`。它明确改为实际 `d5,k3,ℓ2`：水平 grain2、scalar Φ、vector Y∈R²，`u,r` 标量而 `v,a,b` 为二维列；剩余问题从正交 row 转为实际有限次数向量 polynomial 的 tube-KT 压缩。这与冻结的 local-GWZ budget、vector-Φ W/BSG 机制在原对象和额外几何输入上不同。

PCT 的定量界、离散 θ/d₀ 质量、boundary bins、`e≥d₀R`、source γ 与后续 r 非退化/19.4 回传都仍列**待证**，没有当作 R20 成果使用，也没有把一般 dyadic-Lipschitz 曲线设成 C²。本审查只认证这个任务边界清楚，不认证尚未展开的 PCT 证明、精确指数或 mixed32 结论；R20 不开展该下一轮数学。局部 GWZ 按本轮 spec 冻结、等待新实质分支的宏观决定，与已证明范围一致。
