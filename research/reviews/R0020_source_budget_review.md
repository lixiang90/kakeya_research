# R0020 独审：parent 抵消、source incidence 端点与停止边界

2026-10-17，`lifting_obstructions`。审查对象：

- `notes/40_multiscale/sticky_mixed/R0020_parent_packet_audit.md`；
- `notes/40_multiscale/sticky_mixed/R0020_projection_budget_and_stop.md`。

**审定：所写 parent/clock/source 预算通过，没有得到严格 κ-gap。** 核验保留原 parent 质量、原 witness incidence 和真实 marks；没有把局部片段当完整原管。root 单一 J 的直接调用失败，只针对当前已认证误差的稳健投影机制，未被扩大为整个 source 的不可能性。GWZ Theorem 1.1、Lemma 3.7 仍为命名外部输入，未重证全文。

## 1. 原 good-q 到完整 parent 的质量

A 稿使用合法 good-q 的

    m≥K⁻¹h/δ，e≈K^(±1)m(h/δ)^(4−κ)，I_q≈K^(±1)eδ⁻κ。

原 Φ_q 的 coarse cardinal 和 ξ coherence 把 q-family 方向限在至多 Kh⁻κ 个 h-direction bins；同一 spatial h-cube 将每 bin 的 intercept parents 限为 K 的固定幂个，已允许吸收于 K。每条 fine witness 管每 time 只有 O(1) 个原 points，所以 L_T≤Cm。

删除 L_T<K⁻B m 的轻管，损失由 q-family 的原 upper 控制；B 足够大后保住固定比例的原 incidence。剩余 good 管数≥K⁻C h⁻κ(h/δ)⁴，在至多 Kh⁻κ 个真实 parents 中平均，得到一个 parent 内

    #S≥K⁻C(h/δ)⁴，每 T∈S 有 L_T≥K⁻C m。

完整 parent 原成员数≤K(h/δ)⁴，因此 S 是原完整 parent 的 K⁻C 比例。这里没有给 S 新的 AD lower；只需要其概率由 parent 概率以 K^C 支配。这是真实的费用改善，不等于给任意 q-subset 免费完整 parent 质量。

## 2. Whole-parent 质量与 determinant 的方向

空间 shear 后的 parent map 为

    Ψ_h(y,t)=((y−b_P−ta_P)/h,t)，det Ψ_h=h⁻⁴。

原 parent 质量≈K^(±C)h⁴。若 U 含完整变换管，逆像凸集体积为 h⁴|U|；原 CW 除以 parent 质量确实抵消 h⁴。再限制到 S 只付 K^C，故完整 clock 下 parent normalized CW≤K^C。

变换后用普通半径 u=δ/h 管作固定倍外罩时，U 包含该外罩也就包含实际 affine image，逆像仍含整条原管。tube endpoint、dyadic parent 与 bounded slope chart 的常数外罩不会改变 h 的指数。不能反向把只含 J 短段的 U 放进原整管 CW；A 和 root 都明确没有这样做。

## 3. Clock zoom 的一般 whole-tube 费用

追加 (t−t0)/h 后，原完整管的 clock 长度为 h⁻¹，只有 J 段变为单位长度。对含单位短段的三维凸 U，用固定 John 外罩延长到 h⁻¹ 轴长，可花 h⁻³ 体积；逆 clock map 的 determinant h 留下 h⁻²。其余两空间坐标仍按 parent 完整图表的固定盒提升，故一般 projected upper D≤K h⁻² 合法。

完整五维凸体直接同样处理是 h⁻⁵·h=h⁻⁴；不能与三维 lift 的 h⁻² 混同，也不能只用 isotropic map 的 determinant 而省略轴的延长。原 projected line 的整个旧 clock 由延长凸体罩住后，才能使用 parent CW。

三维均匀方向 bush 的短 clock 校准确有 D≈h⁻²。它只认证这个一般 transfer 费用，不携带完整 mixed Φ/薄集条件。A 对其范围标记正确。

## 4. 实际 point upper、parent degree 与 incidence 抵消

在 isotropic Q_h 图表，原 Eq 的计数概率 μ_E 满足，对 A≥u，

    μ_E(B_A)≤K A^(5−κ)。

理由是：时间球内最多 C Ah/δ≤KAm 个原 times；各层在原 radius Ah 球内的点数≤K(Ah/δ)^(4−κ)，由 scalar tilde Y 的 AD upper 和水平三变量 packing 得到。除以合法 good-q 的 e lower 即给上述 upper。不需要 selected S 的 marks 均匀分布于 Eq。

单个 parent 的 first slope 在长 O(h) 区间，scalar Φ_p 的 κ-AD upper 及每 fine Φ-bin 只取一原 witness，给

    deg_P(p)≤K(h/δ)^κ。

不能把这一项替成全部原 degree δ⁻κ；保留这个 parent degree 正是抵消的重要输入。

若 U 的 John axes 为 (A,B,1)，A≥cs，u≤s，则其两自由空间坐标的五维 lift 用 O(BA⁻⁴) 个 A-cubes 覆盖。故 μ_E(lift U)≤KBA^(1−κ)。这里对实际 marks 的 margin 可精确取 U+B_(Cu)，或使用已包住 assigned axes 的 s-representative；因为 A≥s≥u，John axes 和覆盖数只变常数，不能解释成与 A 无关的固定绝对厚度。

通过 short projection 轴落在 U 的每条 S 管有至少 K⁻C m 个原 marks，逐点按 deg_P 求和：

    ν_S{short projected tube⊂U}
      ≤ K e·B A^(1−κ)·(h/δ)^κ / [m(h/δ)⁴]
      ≤ K^C B A^(1−κ)。

e 的 m(h/δ)^(4−κ) 与 parent 管数、degree 正好抵消。再除 |U|≈AB，得到 D_s≤K^C s⁻κ。该推导没有偷用原 CW 到短片段，也没有更换原概率。

## 5. Coarse representatives 和真实 λ_s

bounded R4 projected parameter 网有 O(s⁻⁴) 个 reps；删除权重<s⁵ 的 reps 至多丢 O(s) 原质量。dyadic comparable-weight bin 只丢 log，uniform bin 的 D 仍至多 K^C s⁻κ。包含 rep 的凸 U 同时包含其 assigned 原短轴，故上一节的 weighted upper 合法支配代表 law。

每条被选 good 原管有至少 K⁻C/u 个 fine times，而每个 working s-time cell 最多含 Cs/u 个，因此至少 K⁻C/s 个 coarse levels。选有限颜色的 separated 子集，保留一条 assigned 原管的原 marks，得到 λ_s≥K⁻C。没有 product law、独立时钟或多管拼接参与。

换算 K 到 s 的小幂必须保留 allowed h≥δ^(1/4)、h≤δ^μ；先固定 GWZ 密度阈值，再令所有 retained-loss 指数 θ 足够小于 μ 乘该阈值，即可使 λ_s 满足该命名输入。不能把固定 h 幂加入 K。A 的选择顺序允许这样支付。

因此可证的组合确为

    D_s≤K^C min(h⁻²,s⁻κ)，
    λ_s/D_s≥K⁻C max(h²,s^κ)。

在 s≈h^(1+cε)、κ≤1、小 cε 的工作区间，主项是 K⁻C s^κ，未留下 strict κ-gap。

## 6. 原时钟的 shading 门槛与已修正的 coarse upper

root 当前已把不缩 clock 时的 coarse shading upper 改成 C(ρ+s)，并分两段论证。该修复正确：若 s≤ρ，最多 O(ρ/s) 个时间 cells，密度≤Cρ；若 s≥ρ，可有一个 cell，故应为 Cs，不能仍写 Cρ。

GWZ multiplicity ε_G∈(0,1) 的任何有效密度阈值指数 η_G 必满足 η_G≤ε_G/2。原点 bush 的全部方向为二维 s-grid，whole-tube Δ_max≤C。裁 |t|≤r 给 sum shading≈r、union≈r³，故 multiplicity≈r⁻²。若 η_G>ε_G/2，选

    ε_G/2<a<min(η_G,1)，r=s^a。

则 λ≈s^a≥s^{η_G}（最后取 s 小吸收常数），却 μ≈s⁻²a≫s⁻ε_G，矛盾。这也给出不受边界常数影响的必要不等式；η_G≥1 时亦可用 r≈s 的球形近原点 shading 直接排除。

在 root 声明的当前误差认证中，s≳K^Cρ^(1+cε)。对 s≤ρ，只要 (1+cε)ε_G/2<1，就有 ρ≪s^{η_G}；s≥ρ 且 s 足够小时，Cs≪s^{η_G} 同样成立。因此已修稿的单窗口、原时钟、稳健投影无法直接满足 GWZ density input。没有把 η_G 当可自由放大的数。

该结论只说现有 O(w) error upper 所认证的方法需要按 w 取分辨率。它没有证明真实误差必达到 w；更强消去、其他投影、跨窗口 marks 或新的 source 机制仍可能改变结论。

## 7. Sharpness 校准、未付 upper 与宏观范围

A 的 Lebesgue⁴×ν_(1−κ) 只证明 point-cover 步骤的端点质量 a^(1−κ)/a=a⁻κ 可以实现；没有为它补出实际原管、Φ/ξ 或 CW。B 的有限真管例同时保环境满方向/4AD/CW和 local3grain，却明确缺 source 薄集 AD 与宏观 Φ；root 对二者都保持了准确范围，未称完整 source 反例。

另外，scalar tilde Y 的逐层 AD 不自动给工作尺度粗时间 cell 内的并集 upper。A 第8节正确区分原 Def17.2 的 ℓ-Y 跨时间假设与 Def17.4 的 scalar tilde Y；当前不能只把逐 time cover 数乘 s⁻¹。即使给予最有利 slice upper，已证 λ/D 端点仍不足 strict κ-gap，所以停止决定不依赖假装填好这个 upper。

审查结论支持冻结本轮 local-GWZ extension；未宣称主 mixed42 等价失败或已经被反例否定。后续 d5/k3/ℓ2 scalar-Φ、vector-Y bounded-degree polynomial 候选改变了实际分支和几何输入，但目前尚未证明，本审查不预先认证其结论。
