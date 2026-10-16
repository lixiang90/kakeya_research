# R0020：原 parent packet 的真实抵消、时钟与端点预算

2026-10-17，`audit_four_dimensional`。已读 AGENTS/GOAL/STATE/ROADMAP/registry、本轮 spec、R19 handoff 与原 source rescaling 部分。主目标仍是完整 N5-MIXED42-Q01，本稿只审实际 packet 的可支付估计。**确有 parent mass–determinant 抵消；进一步用原点集/marks 可取得 D_s≤K s⁻κ 的端点。未取得严格 κ-gap，没有解决 mixed 分支或 Kakeya。**

## 1. 准确源位置和证明范围

本库 WZ arXiv:2609.22035v1，文本行号按 `split('\n')`。

| 位置 | 页码、行号 | 可用事实 |
| --- | --- | --- |
| graph tube 与 dyadic tube | pp.16–17，799–849 | 有界 slope 图表；fine tube 有唯一 coarse parent；边界需常数/允许尺度损失 |
| Def3.9、map (20) 后 | pp.17–18，860–872 | joint slope–intercept AD；parent map `(y,t)↦((y−b−at)/h,t)` |
| Observations3.2、3.3 | p.18，875–901 | 完整 parent 的 rescaling、thickening 保 AD；没有裁短 clock |
| Observation3.4 | pp.18–19，909–939 | 印刷声明是 R3 的 `(2t,K)` 与 `C_(t,t')`；其证明按 AD 计数和 transverse Jacobian 抵消 |
| Definitions17.2–17.4 | pp.65–66，3362–3434 | d5 原 T 为 AD4、标量 Φ 为 κ-AD、ξ/Φ coarse coherence、每层 E 的空间 AD upper、共同 Z |
| 高维 setup 的使用 | p.74，3869–3872 | 原文援引 Obs3.4；本稿对 d5 标准 normalized convex bound 直接重算，不把 R3 的印刷公式当无条件任意维定理 |

完整 Lemma19.2/19.4、高级 scalar inputs 及 general-to-sticky 仍有 R19 所列审查边界。这里未重新证明它们。以下只需 R19 合法 good-q、原 incidences、完整 ambient T 的 AD/CW 和保留的正常形误差。

## 2. 原 good-q 到一个真正厚 parent：不用丢整个 q 的自然质量

记原窗口长度 `h=ρ∈[δ^(1/4),δ^µ]`，`m=#Z(q)`、`e=#E(q)`，κ∈(0,1) 固定；端点 κ=1 可同式理解。K 为 `δ^(−Cθ)`，含全部原 retained-time、normalization 与本轮常数幂损失，θ 最后选小。R19 的合法 q 满足

    m≥K⁻¹h/δ,
    e≈K^(±1)m(h/δ)^(4−κ),
    I_q=Σ_(p∈E(q))deg(p)≈K^(±1)eδ⁻κ.

使用每个 fine Φ_p-bin 的原 witness，故一条管每个原 time 有 O(1) marked points；不赋新独立时钟。q 内 coarse h-direction bins 至多 `Kh⁻κ`：Φ_q 提供该数，ξ_q coherence 控制其余 slope。每个方向 bin 的管还通过同一个 spatial h-cube，故只需 O(1) 个 h-intercept parent bins。于是 q 所涉及的实际 h-parents 数至多 `Kh⁻κ`。

令 L_T 为 T 的 q 内原 marks 数。逐管 `L_T≤Cm`，总和至少 `K⁻¹m(h/δ)^4 h⁻κ`。删除 `L_T<K⁻B m` 的轻管，选 B 充分大；由 q-family 的原 T upper，损失不足一半原 incidence。剩余 good 原管数至少

    K⁻C h⁻κ(h/δ)^4.

在至多 Kh⁻κ 个原 h-parents 中平均，存在 parent P，其 good members S 满足

    #S≥K⁻C(h/δ)^4,
    L_T≥K⁻C m  (T∈S).                        (1)

原完整 parent `T[P]` 由 ambient T 的 AD4 只有 `≈K^(±1)(h/δ)^4` 个成员。因此 S 是这个**原完整 parent**的 K⁻C 比例，而非先给任意 q-subset 新 AD lower。S 不必 AD lower；其均匀 law 受原 parent 均匀 law 支配 K^C 即够。

这实质改善了直接给 q-family 条件化的 `h^(4−κ)` 分母：可以选一个真正 AD parent，再用其横向行列式抵消。不能把这项真正抵消漏掉后只重述 p⁻¹。

## 3. 完整 parent 的 normalized CW 确实保住

取原 parent 中心轴 `y=b_P+t a_P`，其中 y∈R4；固定 bounded slope shear 后定义

    Ψ_h(y,t)=((y−b_P−t a_P)/h,t),
    det Ψ_h=h⁻4.                             (2)

它保持**完整 clock**，把整个 P 中的原 unit δ-tubes 送成 bounded chart 中的 full-clock、半径 u=δ/h 的 tubes。对整条 rescaled 管所在的凸 U，原像是凸集，体积 `h⁴|U|`。原 normalized CW 与

    #T[P]/#T≈K^(±1)h⁴

遂给条件 parent law 的 bound `K^C|U|`；再限制到 (1) 的 S 只再付 K^C。固定 margins、dyadic parent 边界与允许尺度取整只改变这些明确 K/常数，不产生 h 的额外 fixed power。

这是 Obs3.4 的 d5 标准 convex-volume 证明。AD exponent4与四个 transverse axes 的 determinant 完全相等；若 AD exponent 不等于4，不能照抄取消。它没有把 parent map 变成 isotropic q zoom，也没有改变原 marks 只在长度 h 窗口内的事实。

## 4. clock 不缩时：CW 已付，但所保留的 shading 很短

在 Ψ_h 图表内，完整管 length≈1；(1) 保住的只是一个原 h-window 的 marks，所以可保下界为 `λ≥K⁻C h`，且任何完全留在该 window 的这种 shading 也有 `λ≤Ch`。外窗 marks 可存在，却没有该窗口正常形给的 thin-slice upper，不能免费加回。

R19 的轴对齐与 r 旋转由有界或 K 条件数的固定 affine 变换完成，保留

    osc a≤Kh², osc b_parallel≤Kh^(1+cε), osc β≤Kh.

q 中三个 horizontal variables 的宽均为 O(h)。空间除 h 后，a 的影响至多 Kh²，parallel row 的影响至多 `Kh^(1+cε)`，故该方法的 robust spatial resolution 至少约

    s≥K h^(1+cε)≥u                            (3)

（若某具体数据误差更小可另计，不能一概降低保证的 upper）。这里 cε 可取 R19 所付的 ε/2 或更小固定正数。把 (3) 的 h 写成 s 的幂，并不能把 λ≈h 自动变成 named GWZ 的小指数 dense shading。

尤其不能只说“parent CW=K、因此可用 MIX001”：MIX001/GWZ 的逐管/平均 shading threshold 仍须核。root 的独立 clock-density 校准负责给出该 threshold 的必要界，本稿不把未满足的阈值当已满足。

### 4.1 较大 parent 的真实 tradeoff，ρ≤τ≤1

此处恢复窗口记号 ρ=h，另用 τ 表示更大的 parent 宽。一个 τ-parent 的第一 slope 坐标局限在长 O(τ) 的 interval。q 内 Φ_q 的 scalar κ-AD 给其中至多 `K(τ/ρ)^κ` 个 coarse ρ-bins。给定其中一个 bin，由 ξ_q coherence 和 `f(z)=f(z₀)+O(ρ)`，其余 slope 只遇 O(1) 个 ρ-bins；因整管经过同一个 q，截距 `b=y−ta` 也只遇 O(1) 个 ρ-bins。因此 τ-parent 中的 q-family 至多涉及 `K(τ/ρ)^κ` 个实际 ρ-parent phase cells。dyadic 相邻边界只付固定倍，不把空间球和 phase parent 混同。

每个这样的 ρ-parent 由原 AD4 含至多 `K(ρ/δ)^4` 条 fine管；完整 τ-parent 含 `≈K^(±1)(τ/δ)^4` 条。故

    #T(q)∩T[P_τ] ≤K(τ/ρ)^κ(ρ/δ)^4,
    active fraction ≤K(ρ/τ)^(4−κ).             (3a)

另一方面，q 所有 τ-parents 数至多 `Kτ⁻κ`，因为 coarse Φ_q 的 τ-cover 和上述 slope/intercept argument。对第2节保留的全部 long-mark good管平均，可选某个 τ-parent，使 (3a) 的 fine-count lower 亦成立到 K 幂，即其实际 good 子族在整个 τ-parent 内的比例

    f_τ≈K^(±C)(ρ/τ)^(4−κ).                    (3b)

所以通过完整 parent CW 后再限制这个 good 子族，真实可认证 `D≤K(τ/ρ)^(4−κ)`。它不是 τ≫ρ 时的 K-dense parent。若利用 marked q 的 spatial 宽只有 ρ，则减去一条经过 q 中心的平行参考轴、将 target 作已知逐时 scalar 平移后，可把已付 blur改善为 `s_τ≈Kρ^(2+cε)/τ`；却必须同时保留 (3b) 的实际 law 费用。单凭这里没有证明任何更优 D 的**下界**，不排除以后额外 source 结构独立改善条件 law；只是不能既用较小 q-width blur，又免费保 τ-parent 的小 CW。本稿最有利的 K-dense whole-parent 方案限于 τ≤K^Cρ，符合前述自然选择。

## 5. 追加 clock zoom：tube 形状、det 与 whole-old-tube 回传

定义

    Q_h(y,t)=((y−b_P−t a_P)/h,(t−t₀)/h),
    det Q_h=h⁻5.                              (4)

它把原 J 上的**短轴段**变为 unit-clock tubes，半径 u=δ/h，新的 spatial slopes 是 `θ(T)−a_P=O(h)`。原完整管则变为长约 h⁻1 的 tube，不能把 unit-clock 凸 U 的原像直接放入原 T[U]，因为该原像只含短段。

仅用整 parent 的已付 CW，可以延长 convex U 到包含长轴。对 full5D tube bound，John ellipsoid 给放大 O(h⁻1) 的体积 factor h⁻5；clock 逆变换的 determinant h 留下 crude D≤K h⁻4。**但实际三维投影可更好**：另两 spatial coordinates 始终在 parent 的固定盒自由取值，只需对投影的3D U 做同样延长。体积放大 h⁻3，再乘 clock 逆 determinant h，故

    D_projected≤K h⁻2.                       (5)

此 convex continuation 罩的是 whole old projected tubes，提升自由两坐标后才能调用 parent CW。U 含一条 fixed-length new tube，故其 John ellipsoid 与固定倍 dilates 足够控制 axes 的 h⁻1 延长；薄到 tube 半径以下的无管凸集无需查询。

一般 clock transfer 的这个 h⁻2 费用不能只靠“det Q_h=h⁻5”省去。uniform 3D direction bush 是相应**接口**校准：整 clock 均匀二维方向的线束有 bounded whole-tube CW；裁长 h 的共同 clock 后 zoom，全部 new tubes 落在 transverse h×h box 内，normalized CW≈h⁻2。该校准不满足当前 mixed Φ/source 全假设，只说明一般 whole-tube-CW transfer 的时钟费用不是无根据的估计松弛。

## 6. 用原 Eq 与 marks 进一步抵消到 D_s≤K s⁻κ

这一步保留了实际 source 的额外点集 AD和 pointwise tube multiplicity，强于 (5)。不需要由 whole-old-tube 凸原像偷换 short tubes。

先看 Q_h 后的原 Eq 计数概率。对 normalized radius A≥u 的5D ball，time packing最多 `C A h/δ≤K A m` 个原 times；每层 E_z 由 scalar tilde Y 的 α=1−κ AD upper 与三维 X packing，spatial ball 中原点数至多 `K(Ah/δ)^(4−κ)`。由 e 的 lower 得

    μ_E(B_A)≤K A^(5−κ).                       (6)

这里 μ_E 是原 Eq 的均匀点计数；没有把 selected S 的 marks 改成 uniform Eq，只将在 upper 中支配它。旋转或固定 bounded shear 不影响 (6)，K 条件数则付相应 K。

任意一个原点 p 属于当前 h-parent 的 witness 管数满足

    deg_P(p)≤K(h/δ)^κ,                        (7)

因为 parent 的 first slope φ 位于一个 h-interval，而原 Φ_p 是 scalar κ-AD。此处原 single-witness 约定保证不额外加入同 fine Φ-bin 的任意多管。

令 U 为3D convex body，含一个 working s-tube，`u≤s≤1`，John axes 可记 `(A,B,1)`，其中 `A≥cs`、`A≤B≤C`。拉起另两 normalized spatial coordinates 的固定盒，所得5D凸 body 有 axes 受 `(cA,cB,C,C,C)` 控制；用 A-cubes 覆盖至多 `C B A⁻4` 个。由 (6)，

    μ_E(lift U)≤K B A^(1−κ).                  (8)

对于 **short projected whole axis** 落 U 的原 S 管，至少 K⁻C m 个原 marks 均在 lift `(U+B_(Cu))` 中。该 margin 是原点/管半径对应的 Cu，不是绝对固定厚度；因 A≥cs≥cu，John 轴长和覆盖数只变固定倍。用 (7) 逐点求和，再除 `#S·K⁻C m`，由 (1) 和 `e≈K^(±1)m(h/δ)^(4−κ)` 得原 weighted law

    ν_S{short projected T⊂U}≤K B A^(1−κ).      (9)

归一化体积是 `|U|≈AB`，故 (9) 给

    D_s≤K s⁻κ.                               (10)

每个 s-representative 装下赋给它的原 short projected axes，(9) 也支配其带原重数的 law。再删极轻 reps、选 comparable-weight bin（bounded R4 projected parameter 网只有 O(s⁻4) 个 reps，删 weight<s⁵ 仅损 O(s)），uniform family 的 D 再付 K/log 小损失。不依赖原 fine T 数目额外有多项式上界，不把原 image 随意改成 uniform distinct image。

working s-time cell 至多含 `C s/u` 个原 fine time levels；每管 (1) 的 marks 数至少 `K⁻C/u`。因此至少 `K⁻C/s` 个不同 coarse levels survives，选择固定 separated 子集并放 s-balls作 shading，得到

    λ_s≥K⁻C.                                 (11)

这是同一条所选原 tube 的 marks；没有独立抽样。结合 (5)、(10)，实际可证预算为

    D_s≤K min(h⁻2,s⁻κ),
    λ_s/D_s≥K⁻C max(h²,s^κ).                  (12)

在 robust s≈h^(1+cε)、小 cε、κ≤1 的范围中，s⁻κ 是更强 upper，(12) 给的主项是 `K⁻C s^κ`。

## 7. point-cover 端点本身 sharp；不是 full-source 反例

只看 (6) 的维数 upper 与 lift 的覆盖，指数 κ 无法统一改进。取 normalized 5D point probability

    μ=Lebesgue_[0,1]^4 × ν_α,
    α=1−κ,

其中四个 Lebesgue coordinates 对应三水平轴和 time，ν_α 是固定 α-AD Cantor（有限时取足够深的 regular approximation）。它满足 fixed-constant `(5−κ)`-Frostman upper，也有完整水平三维 grains和共同满时钟。在 Cantor support 点附近取 lifted projected slab，thin width A、另一个 projected spatial width1、time length1，则

    μ(lift U)≈A^α,
    |U|≈A,
    μ(lift U)/|U|≈A⁻κ.                        (13)

所以任何只从 point-AD/John-cover 要把 (10) 改成 `s^(−κ+c)` 的论证都缺额外信息。该例没有构造满足完整原 T/CW/ξ/Φ 的 tube family；它不否定完整 source 的潜在改善，只给这一实际推理步骤的严格界限。

## 8. projected union upper 也不能在 coarsening 时免费继承

原 common Z 在 fine δ-resolution 足够。空间 parent rescaling却不缩clock时，working s 的原 spatial尺度是 hs，time cell长s，原 Def17.2 的同尺度跨时间 union AD 只直接给原 ℓ-Y（R3），不直接给 scalar tilde Y 在 hs尺度的跨 s-window union upper。

追加 Q_h 的 isotropic clock后，working s 同时对应原 space/time hs，恢复了尺度匹配；但 scalar tilde Y 的跨时间 union仍不是 Def17.4 明列假设。可尝试从原 ℓ-Y union、full横向 grains、在hs尺度重新支付的 tilde f normalization 得到，但须证明其 fibre/时间删选，不可只把逐 time #tildeY_t 乘 s⁻1。特别，Lemma19.5每个指定ρ给一个 retained set；不能免费说 R19 的同一个 set 已在所有更细尺度 dyadic-Lipschitz。

本稿的 (9)–(12) 不需要先填这个 source-upper 接口。即便按最有利情况假设已证 `|U_shade|≤C s^(κ−a)`、a≥0，现有预算也只有 b=κ+小损失，GWZ 的额外 s^ε 不能给所需 `ε+a+b<κ`。若 union upper 还需损失，情况只更弱；不把这一 sufficient-budget 失败说成整个 mixed42 命题等价失败。

## 9. 原条件真正抵消了什么，以及停止点

parent AD/coherence 实际允许选到一个 K-dense parent 子族，完整 clock 下的 h⁴ mass 由 determinant h⁻4 真正抵消。裁短clock之后，generic projected whole-CW transfer 另付 h⁻2；利用原 point AD与 parent 内度数，可真正改善为 s⁻κ 并保密 shading。这个端点是本轮新得到的 source预算，不是只重述 p⁻¹，也不是新的 κ 改进。

未取得超出 (12) 的 strict gap。point-cover 单独改善已被 (13) 排除；原 f/ξ 更深关联、原 tube CW 的跨窗口信息或另外几何输入仍可能改善，但没有证明。本轮若 root/B 也无额外真 gain，应按 spec 冻结这一 local GWZ extension，不再用新阈值、换时钟或 parent 名称延续同一端点计算。主 mixed42、其他五维分支、general-to-sticky 与 Hausdorff 最终目标仍开放。
