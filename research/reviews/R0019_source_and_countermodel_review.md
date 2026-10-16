# R0019：全局 residual 投影与实际直线攻击交叉审查

2026-10-17，审查者 `/root/audit_four_dimensional`。对象为 root 的 `R0019_global_residual_projection.md`（含新 §6）与 B 的 `R0019_residual_counterattack.md`。**结论：两稿按其明确的全局/固定运输范围通过，可归档为依赖已列外部输入的 proper-branch 应用与构造类排除。没有完整 mixed42 二次结论或新的 Kakeya 维数界。** 自己的 `R0019_source_and_mass_audit.md` 不算本审查的独立对象，交由 root/B 核验。

## 1. 原先验、共同 times 和 CW 的全局含义

root §1 当前已明确所有 marks 来自同一个全局 δ-separated 集 Z。此条件对 §§4、6 都必要：若只逐管 separated 而全局时钟可任意稠密，一个 δ-time cell 内可能合并无数不同 thin Y_t，不能由 `max #Y_t` 推 union 上界。实际 source 的共同 Z 正好提供所需条件。

由平均 marks `≥cδ⁻¹⁺η` 和逐管 `≤Cδ⁻¹`，先删 light tubes，确能保 `#S≥cδ^η#T`，且 S 中每管有 `≥c'δ⁻¹⁺η` 原 marks。均匀 S law 对原均匀 T law 的 domination 至多 `Cδ⁻η`，故 normalized CW 从 `Cδ⁻η|U|` 变为 `Cδ⁻²η|U|`。这里没有将 projected distinct images 免费 uniformize。

完整 source 的 tube count 与 Remark17.1 的 shading 只改变固定倍 η；将这些固定倍并入预算后，root 的实际 source 应用接口成立。没有假设每条原 source 管一开始就有逐管 dense marks。

## 2. Root §§2–4：GGW 有限投影调用通过

将同一原管 law 推到实际投影轴参数 `(a₃,a₄,v₃,v₄)`。半径 w 的参数球对应 `(x₃,x₄,t)` 中一条完整固定长度轴的 O(w) 邻域。提升并允许另外两空间坐标取固定盒，得到体积 O(w²) 的真实凸集，包含整条原管。故带原重数的参数 law 有 `Cδ⁻²ηw²` ball upper。

三个 coefficient map 均已重算：

    β=t:       (a₄,v₄−a₃,−v₃),
    β=t²:      (a₄,v₄,−a₃,−v₃),
    β=t/(1+t): (a₄,a₄+v₄−a₃,v₄−v₃).

首、末 map 的 kernel 维数为 1，bounded fibre 可用 O(w⁻¹) 个参数球覆盖，因此 pushforward 保指数 1 的 Frostman upper；中间 map 可逆，保指数 2。分式情形的 `(1+t)` 在指定 `[0,1]` 有双侧常数界，乘 target 不改变覆盖数的幂。

δ-mollification 后，R3 中小球 upper 为 `Cδ⁻²ηδ⁻²w³`；R4 的 exponent-2 情形为 `Cδ⁻²ηδ⁻²w⁴`。结合 w≥δ 的 bound，对每个固定 α<1 都有 `c_α≤Cδ⁻Aη`，没有把 Frostman 常数设为 1。每个 mollified support 点邻近某个实际 good tube 的 coefficient；有界相位范数使该管的原 mark levels 对这个点仍成立，只须固定扩大目标区间。共享 coefficient 的不同 marks 取并不会减少逐点参与数。

已独立读本库 GGW arXiv:2211.09508v2 Theorem2.1 文字并渲染、目视核 PDF3：它确为有限 incidence 定理，对全部 support 点要求 `Σ1_W≥δ^(ε−1)`，结论 `#W≥C c_α⁻¹δ^(−1−α+10^(10n)√ε)`，不是仅 Hausdorff a.e. 结论。本审查未重证完整 decoupling 证明。

相位 `(1,t,t²)`、`(1,t,t²,t³)` 是相应 moment curve 的 tangent 方向，经固定对角 coefficient 变换即可使用 factorial 标准化。root 已修为把共同原 times 舍入固定 regular net，每格只收 O(1) 个原 time；相位误差 O(δ)，marks 数仅损常数，target 数也仅增常数。这避免了把任意原 separated set 直接当字面 source(2.4) net。bounded coefficient 支撑在每个 normal-target interval 上只遇 O(1) 个 long-direction boxes，故 `#W≤Cδ⁻²⁺κ⁻η`。

取 `α=1−κ/4`、再令 `10^(10n)√ε<κ/8`、最后 Aη<κ/8，GGW lower 至少为 `cδ⁻²⁺κ/2`，与 upper 冲突。原 mark exponent 经 η<ε/2 与 δ 小亦满足点态假设。整个证明保原 pushforward law；三个 global profile 子例的条件性排除成立。

## 3. Root §6：任意 bounded global β 的更强归约通过

### 3.1 Weighted image 到可用的 tube family

把每条原 S 管的**整条**投影装入有固定 margin 的 comparable-δ 标准投影管 P_j，然后按原赋值权 `w_j=#fibre/#S` 计数。若 P_j⊂U，所赋原管的投影亦在 U；提升到 free `(x₁,x₂)` prism 即得体积 O(|U|) 的凸集，原 CW 可用。若采用近邻代表而非包含代表，则先取固定倍凸膨胀：U 已含 δ 内球和固定长度轴，bounded chart 内相近参数的完整原投影均在 C U；体积仍 O(|U|)。不能只取 marked 短段的 preimage。当前稿明确采用完整包含和 margin，符合这个要求。

每个非零权为 `1/#S` 的整数倍，`#S≤δ⁻M` 给 O_M(log(1/δ)) 个 dyadic weight bins。某层原质量 `p≥c/log(1/δ)`，层内 comparable weights 使 uniform P_j law 被 restriction/p 常数支配。因此 `C_F≤Cδ⁻²ηp⁻¹≤δ⁻Aη`。param-net 近邻有限重叠可用固定多种颜色确保 essentially distinct，只损常数；没有舍弃原 mass denominator。每个代表取一个 assigned good original tube 的 marks，逐管 shading density 仍为 `≥cδ^η`，也无需 projected coefficients 独立或 full-dimensional。

### 3.2 三维有限输入与指数

已核本库 GWZ arXiv:2601.14411v2 的 Theorem1.1（PDF2）、Definition3.4（PDF6）及 Lemma3.7（PDF7）声明。Theorem1.1 等价提供 KKT(0)；Lemma3.7 在 β_KKT=0 给任意 Δ_max 下

    μ(P,Y)≤δ⁻εΔ_max(P)

并只需原 shading 的平均 density≥δ^η_GWZ。参数 β_KKT 与 residual β(t) 不同。此审查没有重新证明完整三维 Kakeya 输入，也未运行作者报告的 Lean formalization。

uniform projected family 的 normalized CW 恰给

    Δ_max(P)≤Cδ⁻Aη #P δ².

故 `Σ|Y(P)|/μ(P,Y)≥cδ^(ε+(A+1)η)`；管数 #P 消掉，无需另外假设约 δ⁻² 条投影方向。这一步是 Frostman 与 Katz–Tao 归一化间的实际换算，没有把 normalized CW 直接误写为 Δ_max≤δ⁻Aη。

另一侧，每个共同 time 的投影 marks 位于 bounded x₃ 区间和 `w−β(t)x₃∈N_(Cδ)Y_t`。bounded β 足以使该层占至多 `Cδ⁻²⁺κ⁻η` 个 spatial δ-cells。各层 thickening 只遇固定数个 time cells，共同 Z≤Cδ⁻¹，所以 union volume≤Cδ^(κ−η)。不需要 β 的连续性，亦没有用连续时间 surface 代替离散 marks。ε=κ/4、再把 η 取小，lower≥cδ^(κ/2)，与 upper 冲突。

因此 §6 在原完整全局 fixed-frame 几何内确排除**任意 bounded β**，强于三种显式 profile。这是已有三维定理的实质、带原权接口应用，仍非完整 mixed42 结果。

## 4. B 稿：真实构造与固定运输类范围通过

### 4.1 实际直线和有限 AD

逐项代入 `ℓ(t)=(A+tφ,B−tA,(1+t)C,c+tC,t)`，确有 `w=c+β(t)Z`、`β=t/(1+t)`。在当前点的 `ξ=(-x,C,C)` 与 `f=(t,0,0)` 给方向 `(φ,−x+tφ,C,C)`；沿同一条线该方向不变。`v=a+bu=0`、`h_(t₀)=0`，而正交 β 非线性，故它确实排除“这些逐点几何自动令 residual 常量”的推断。

实际 slope–intercept 参数双 Lipschitz 读回 `(A,B,C,c,φ)`，三满变量加两个 1/2-Cantor 因子给 joint AD 维数 4；方向边缘仅维数 5/2，作者没有误称满四维方向。两种 grain 的线性表示、ξ coarse coherence、内部 patch 每个 φ 的 O(δ) 见证与标量 Φ cap 均正确。全局边界上是否仍有全文 Def17.2–17.4 的 dense shading 未被声称，不能据此认证整个模型是完整 source。

限制 `|C−C₀|≤h,|c−c₀|≤h` 的原参数质量为 `≥ch^(2−κ)`，对应整个原线段落在两条独立 affine 条件组成的体积 O(h²) 凸框。故 CW≥ch⁻κ，h≈δ 时违反源小损失。没有条件化后把 fibre mass 误写为 1。

### 4.2 连续运输刚性与任意原权的 CW

完整时钟、连续 λ≠0 与无区间 H 使每条线的 hidden label `c(t)` 连续且恒定。同标签两条不同横位置线相减给 `β(t)(ΔA+ΔDt)=ΔB+ΔEt`。若分母在 I 有根，连续性迫使分子共享根，两 affine 多项式成比例，β 恒定；非恒定分支因此无极点、为 fractional-linear。

对非恒定分支，互素的 affine 分子分母给 `dim ker L_β=1`。用两个不同 c 的实际代表线插值，全部 projected coefficient 落在 `P₀+cP₁+sV`；H singleton 时用一条参考线和同一 kernel coset，当前稿亦已单列。bounded 原系数与 H 的固定正直径使 covering 常数不随 depth 变。于是 `N_h≤C K_Hh^(−2+κ)`。

这个 cover 对任意原正权先作互斥 assignment，再鸽巢得某系数球原质量≥cK_H⁻¹h^(2−κ)。球中的**整条** projected axes 在同一个 O(h) 二法向 tube 中，提升自由两坐标得凸体积 O(h²)，所以 CW≥cK_H⁻¹h⁻κ。无需投影权独立、均匀或 AD。有限 e 邻域版本在 h≥C max(e,δ) 同样成立。

恒定 β 且 H 至少两点时 λ、μ 分别 affine；singleton 时只需其唯一组合 `c₀λ+μ` affine。当前稿已区分这两个情形；各自给共同 slab，仍有相应 CW 损失。没有除以 β' 或假设 C²。

**范围不可放宽：** 这些刚性使用共同固定 Cantor 运输和完整连续时钟。源只给离散 dense shading、可能随 t 改变的 thin Y_t；未 marked 间隙允许 hidden label 穿过 Cantor 缝隙。因此不能把命题4.1当原 source 引理，也不能把作者内部 patch 的边界误报为完整源反例。

## 5. 全局结论与实际 local 目标的严格隔离

root §6 只有在所有 slices 共享一个固定二维 spatial projection kernel、并保持 whole-source CW 与长 marks 时适用。源审计取得的是某原窗口上的慢变 a、慢变 b 平行分量和未知 residual β；这些误差为 Kρ²/Kρ^(1+cε)，远大于 δ。直接忽略它们会扩大 projected thin slices，也可能丢失 Y 的亏损。

另外，单 q 的管质量可以只有 fixed power `ρ^(4−κ)`；以它条件化的原 normalized CW 只能再除这个原质量，不能标为 K。任何 rescaling、parent-tube 或 patched-frame 方案必须另付这些实际费用。两稿都没有跨过该门槛，因而没有将 global canonical exclusion 冒充 full mixed quadratic exclusion。

可归档结论为：原显式残余几何可兼容真实线和 joint AD，却由同原权凸框排除；整个固定运输/完整时钟类也被排除；更一般的全局固定 kernel、任意 bounded β 类由已列三维输入排除。一般实际局部 mixed42 仍 open，新颖性和重大性均未声称。
