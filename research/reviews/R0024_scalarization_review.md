# R0024 独审：原角先验 quadratic scalarization

2026-10-17，`lifting_obstructions`。独立审查 root 的 `notes/40_multiscale/sticky_mixed/R0024_original_angle_scalarization.md` 最终版本，参照本人的独立 finite proof 和 A 的 `R0024_mixed43_source_audit.md`。核 all-adaptive fits、slab base、系数加权目标、原图三项质量及 actual middle-τ 的精度预算。不在本文件补做 whole-matrix AFF 或高级 projection。

**结论：经下述两处修复后通过。** finite uniform/weighted scalarization 成立；actual middle-τ 的角选择是条件于稿件明列的 matrix-AFF、retained mass、原 nonquad 等输入的实际 used-cell proxy gate。它不产生固定 exact fine-angle pair 的 dense 原切片，也不完成 mixed43。

## 1. 较强 uniform 版和所有 adaptive coefficients

原 time interval cap 给每个 exact time position（合并该位置全部重复标签）的 atom≤K_td。mass β≥b 的 fit set，其四重 product 中任何一对位置重合的质量≤K_td β³；六对 union 后，b≥C K_td 保至少 b⁴/2 的 distinct-position tuples。

对四个 distinct positions 的 `α_i=1/∏_{j≠i}(t_i−t_j)`，二次消去恒等式准确。选 |α_j| 最大并归一化，所有其余系数的绝对值≤1，因此 scalar w-fit 导致 residual 的 scalar值≤4w。不存在 gap⁻³，也没有必要付 gap⁻²。

small vector residual 不能只按一个固定 test index 积分；最终稿按 j=1,2,3,4 分别固定其它三个 anchors，每项落同一个 vector quadratic h-fit，upper≤a。所选 j 的额外条件只减事件，总 upper 为4a。large residual 经 unit normal R/|R| 查询原 ψ-slab，Fubini/Markov 给式(2)，对任意实拟合系数同时成立。

这里输出是 vertical quadratic error，不是 arbitrary Euclidean tube；不需要 SCAL001 的垂直化假设。F 无 bounded norm/Lip 要求仅限 uniform finite 版本，不能移给下一节。

## 2. slab base、trivial1和small norms

uniform query 是至少4w/h的合法宽度。若它低于q_base，只能在q_base上查询；若大于1，正文明确用trivial1。式(2)的max和min并未把原先验外推至working base以下，也没有在q>1调用未给的slab假设。

近零 ψ 本来就在 central slabs 中。该 finite bound 不要求先把 ψ 归一成 unit vector；那样会改变 scalar error。若后续另需 norm lower，应明确删小 norm 的原质量，而不能暗加条件。当前实际应用只用 bounded |ψ|，没有做此无费用归一。

## 3. coefficient-weighted extension

对误差 `w A(p)`、`A(p)=1+|p₁|+|p₂|`，rich set 中可以按原interval cap选三个真实times，pairwise gap≥g≈b/K_t且g≥d。Lagrange quadratic每个系数的分母是两个gap；t∈[−1,1]给 numerator coefficient 固定上界，故

    A(p)≤1+Cg⁻²(ML+w A(p)).

`w≤c b²/K_t²` 确能吸收右侧的 A 项，得到 `A≤C(1+ML)K_t²/b²`。三个anchors随ψ或拟合变化只用于确定性 bound，不新增概率union。代入uniform版本即为正文式(5)，其中max(q_base,...)和trivial1须继续保留。

短interval边界也成立：`p_R(t)=R(t−t₀)²` 的A≥R，在 |t−t₀|≤√w/4 上 polynomial值≤Rw/16，R足够大就可吸收任意bounded signal。因此uniform-time实例中有约√w质量的weighted fits，而无需真正quadratic结构。它证明不能免费删掉当前精度门槛；正文没有夸称所有先验下的必要充分性。

## 4. 原 correlated graph 的三个常数

g≤1、mean=m，bad角对的原µ²概率≤m/4，故good原 graph absolute mass≥3m/4。由其平均至少有一个实际good角对的conditional graph mean≥m/2。进一步删good但mean<m/4的角对，至多损m/4，所以good且mean≥m/4的角对仍承载至少m/2原 graph质量。

这些陈述均是原 product **reference** 上带g的积分，不是把实际路径angles与times变成独立。Bad只依赖ψ时，µ²经过差映射的π恰给bad pair概率；无需给g-weighted边际重新赋Frostman。

## 5. actual used-angle prior 的源接口

A稿通过真正initial incidences定义β。conditional于p的原Φ_p slab upper按任意p权混合仍成立；coarseρ-cell upper为Kρ^κ。固定initial incidence的原L扩展upper为 `Kδ^κ F_Lm²`，除总L lower给其 marginal受K times β支配。两initial arms都可这样计费。

因此按β质量删light-used cells会支付真实原L质量；在原Φ_q仅用support/cardinality upper，未使用其unused cells的slab upper。保留H每cell的β lower与#H lower共同给Uniform(H)的slab cap。其query须为q≥Cρ，cellproxy偏移ρ才能吸收。差π=Uniform(H)²的slab upper可固定一个角再积分得到；它是bounded支配reference，actual关联仍在g中。

这一构造足以支持root的conditional gate。它没有证明H²中任意pair都由同一p见证，也不需要如此：许多reference pairs的g可以为0。

## 6. middle-τ指数和修复后的合法查询

在matrix-AFF及原nonquad条件已经给定时，vector τ必须先于ψ选定。τ-ball/time框、F_row/G_row、原ν和π均固定，再选同一个proxyψ标量化。空间是本来就scalar的tildeY，不投影vector Y制造亏损。

由τ≤ρ^{3−ζ₁}，physical coefficient-weighted vector nonfit可缩弱为

    h₀≥K⁻Cρ^p,   p=2ε₁+ζ₁,
    a≤K^Cρ^{ε₂}/θ.

取目标weighted precision σ=ρ^{2p}、b_fit=ρ^β，β<min(ε₂,γp)/100。有限weighted式的raw slab参数有 upper `K^Cρ^{p−2β}`，但仅由h₀的lower**不能**推这个raw参数也有同阶lower。root已修复为明确查询

    Q_*=Cρ^{p−2β−Cℓ},
    0<p−2β−Cℓ<1,
    Q_*≥max(Cρ,q_raw),    Q_*≤1。

故式(5)中max项可用这个更大的合法slab upper控制；实际raw scale即使低于Cρ也不造成漏洞。此前“raw查询约该幂所以必高于base”的不足已修复。

K_ψ在γ幂外的损失也须保留。root已将第二principal exponent改为

    γ(p−2β)−4β−O_γ(ℓ),

与第一项 `ε₂−4β−O(ℓ)` 分别检查。必须先固定γ、ε各参数，再令ℓ相对它们足够小；不能对γ无条件抹去O(ℓ)。β的严格余量使两指数都正且大于原m的loss，从而bad概率<m/4。

`d=δ/ρ≤ρ³` 给four-times原子门槛，`σ K_t²/b_fit²→0` 给weighted系数吸收。若还要求原graph error `e=K[ρ+ρ^{3+ε₀}/τ]` 小于目标precision，则τ>ρ^{3+2ε₁}给 `e≤Kρ^{ε₀−2ε₁}`；先选 `6ε₁+2ζ₁<ε₀`，再小取loss，确有e≪ρ^{2p}。root式(10)的precision因此与同一g的近似关系兼容。

## 7. proxy修复和仍未付的准备

最终稿已将actual应用中的“同一真实角对”收紧为**同一实际 used-cell proxy角对**。每个code的exact fine差可以不同，Oρ差别进入已付O(τρ)平移误差；没有声称某一固定exact fine-angle pair的原slice仍有K⁻C mean。式(10)是该选定proxy下的scalar nonfit，原coarse g依然保密度。这一限定必要且已落实。

whole-matrix globally dense AFF仍是本应用的条件。ell3 observed A只有Kρ⁻² upper，原scalarABC的ρ^{-1−κ+ζ} lower在κ≤1时不能击败它；AFF001的ell2证明没有被自动推广。time restriction闭包可推广，不等于affine准备已存在。

fine time→working-grid代表/weighted projection、高级scalar22.5各实际条件、large-τ删除G的误差及投影后τ稳定性均未由本轮支付。固定vectorτ不能因选中ψ下scalar近常就缩小。scalar finite graph也不是一个新的完整四维Kakeya配置。

审查通过的是finite原slab quadratic scalarization、weighted extension及明确准备条件下的actual middle-τ used-proxy角选择。没有得到完整mixed43、五维sticky、Hausdorff维数新界或真实Kakeya反例，不认证新颖性/重大性。
