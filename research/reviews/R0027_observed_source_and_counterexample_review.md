# R0027 独审：actual observed matrix、联合平面门槛及数字边界

2026-10-17，`lifting_obstructions`。审查 root 的 `R0027_matrix_translation_plane_gate.md`、`R0027_digital_observed_boundary.md`，交叉核 A 的 `R0027_observed_matrix_source_audit.md`，对照本库 WZ §19.1 原 (148)–(153) 和 §21.1 原 observed 构造。本人的独立有限证明与反攻为 `R0027_matrix_observed_counterattack.md`。

**结论：三稿在其明示范围通过。** actual source给 observed A、原 reference bounded g、正确 matrix-time action、used-angle slab law、2-Frostman 与多尺度 visible fibre；原 whole-matrix nonfit可在fine law上给 D的affine2plane cap。真实数字加法反例严格否定删去matrix-time分解后的泛增长推论。未证明 actual ell3 AFF₃、`#A>r⁻²` 或完整五维；不把数字模型称 source/Kakeya 反例。高级源配置及既有 weighted good-q/路径平均输入未在本轮全量重证。

## 1. 原路径符号、两维厚桶与ρ幂：通过

原 (148) 在两段方向共点后给 `Δξ′=[f(z₁)−f(z₂)](φ₂−φ₁)+O(ρ|Δf|+δ)`，原 (150) 给 `Δx′=(z₂−z₁)(φ₂−φ₁)+O(ρ²+δ)`。因此不反射 ξ 的实际作用为

    ((t−s)ψ, −[M(t)−M(s)]ψ)。

源稿与 root 同时保留负号，并将 M 与 observable ξ 同步除以 `L_fρ`；没有沿用原印刷 (170) 的反号或 (172) 缺 L_f 的缩放。原 (152) 给的是两终点二维 ell-label相距 O(Kρ²)，不是 exact 同 grain。

记σ=ρ²。实际 d5/ell3 的 visible x维2，ell-label Y维2−κ。因此每末层厚y桶数为 `K(ρ/σ)^(2−κ)`，每桶 endpoint容量为

    P_Q=K(ρ/δ)²(σ/δ)^(2−κ)。

乘末层数 m 后，所有桶容量上界为 K倍 `e≈m(ρ/δ)^(4−κ)`。固定一个第一endpoint的原 W恢复上界为 `Kδ^(−4κ)ρ^κm²`，它来自四条实际witness管及两自由times；无需逐管 marked degree相等。故删除低occupancy桶、再平均，确得到源稿 (9) 的真实 endpoint及W质量下界。

固定code的恢复表也正确：endpoint cell容量 `(σ/δ)^(4−κ)`，第一末管 δ⁻κ，已给两初角ρ-bins各付 `(ρ/δ)^κ`，ρ-close第二末管再付 `(ρ/δ)^κ`。合计

    P_code≤K(σ/δ)^(4−κ)δ^(−4κ)ρ^(3κ)。

与 heavy桶 W下界相除，ρ/σ及角的剩余幂恰为

    K⁻C(ρ/σ)²ρ^(−2κ)m²。

这正匹配 `A_σ×Z_q²×H²` 的 reference大小，无额外遗失ρ幂，也没有把四维point维数错当 ell-label维数。按真实code重数除统一upper得到0≤g≤1及mean≥K⁻C，是保原相关性的构造。

## 2. 原W角边际与 used law：通过

不能把 raw unused Φ_q叫 slab。源稿用 `β=e⁻¹Σ_p Uniform(Φ_p)`，其slab与κ-AD cell upper来自实际原 Φ_p。固定原 p,T₁的W恢复 upper为 `Km²δ^(−3κ)ρ^κ`；除总W lower后，初角边际被 Kβ支配。第二角对称成立。

因此删 β_c过小的 used ρ-cells，其损失是**原W质量**，而非只删一个无关角计数集合。heavy H的 cell质量有上下K容量，card≈K^±Cρ⁻κ，并从 β 的原slab cap继承Uniform(H)的合法cap。其差law是原Uniform(H)²的pushforward；固定一端平移slab证明差law cap，无须 distinct differences uniform化。

角pair在原图中仍可能任意相关。产品 law `Uniform(H)²`只是 bounded g的 dominating reference；固定proxy角不等于固定 exact fine角。fine到proxy的Oρ误差乘原Oρ时间或f差后为O(Kρ²)，已在原误差中。

## 3. observed A的真lower、多尺度fibre和2-Frostman：通过

每jointσ-cell的endpoint容量≤`K(σ/δ)^(4−κ)`，故 heavy桶点数给 `N_σ(A_phys)≥K⁻C(ρ/σ)²`；visible σ-cell内由物理σ-cube数与ξ-coherence给joint cover≤K，因而matching upper成立。合并 input/output厚桶只多K，原输出/输入ratio因此有依据。

同步归一后，R≥r的 visible cell物理宽Rρ，末层厚y为Kρ²，不超过有限K倍Rρ；其点只遇有限K个物理Rρ-cubes。原ξ-coherence给联合R-cover≤K^C，allowed-scale向上取整费用亦计入K。故全coarse visible fibre是真正的source约束；不等同于全局Euclidean Lip或单值延拓。

Uniform(A_r)的2-Frostman upper不能只由coarse cover二字得到。源稿实际用base visible r-cell的joint标签upper，按水平R-ball内O((R/r)²)个cells求和，再除真实 `#A_r≥K⁻Cr⁻²`，得到 `K^CR²`。这没有给裁切patch免费AD lower。

水平3-grain的 `v=a+bu`与末label关系不迫 `ξ₂−bξ₁`为常数。源稿明确保留此限制；没有通过虚构constant offset把Mat2退化成标量。

## 4. 细时间非拟合与D事件粗化：修正后通过

一个time-r interval可能遇多个matrix graph cells，dyadic Lip和allowed取整给其数≤K、每cell fine容量≤P及总cell数≤K/r。删除容量 `<P K⁻B` 的轻cells后，两time坐标按原g≤1计损，余heavy cells的真实occupancy上下可比K。

**但这不免费传 all-real matrix affine-band nonfit。** 未知slope乘clock位移可以很大；不能将一条coarse rich affinefit直接厚化O(r)便送回fine。本人指出源稿§8原来的泛称后，作者已收紧为：heavy lower只支配完整fine-preimage事件；仅传已付增厚的interval/Euclidean事件或§9的D事件。当前§8–9无冲突。

实际应用先在原fine law上使用wholeM nonfit。取 `h=ρ^(2ε₀)`，在 `L_f` loss≪ε₀时小于源精度 `h₀=ρ^ε₀/L_f`。先定 `ε₀<1/32`、最后小取source loss，有

    d=δ/ρ≤ρ³≪h， q_base=Cρ≪h， Kr≪h⁴。

两time和角的coarse proxy改D仅O(Kr)。一个coarse平面事件的全部fine preimages因此都属于固定倍厚化的fine事件；heavy occupancy与角重分箱collision bounds给uniform coarse产品 law被原fine产品 law以K^C支配。所传的是D事件，非任意slope的M-band。conditioned g事件只另付其mean⁻¹≤K^C。

## 5. affine2plane gate逐式核验：通过

任意affine2plane写成 `Qz=c_P`、`QQ*=I₂`，Q=(A,B)，所以 `AA*+BB*=I₂`。令ε=h⁴、λ=h²、g=h。

若σ_min(B)≥λ，乘B⁻¹得到root (4)，offset确为 `+B⁻¹c_P`。固定s后，residual norm≤h正是slope B⁻¹A、intercept `M(s)−sB⁻¹A`的whole-matrix affinefit，原mass≤a；系数可任意大，已由all-real量词覆盖。其余residual取最大奇异值的左方向，用原ψ affine slab宽ε/(λh)=h。没有假设residual rank2或B⁻¹c_P bounded。

若σ_min(B)<λ，取小left singular向量w；正交性给 `|A*w|²=1−|B*w|²≥1−λ²`。root (5)误差ε+2λ正确。删短差|t−s|<g付K_t g，余下原角slab宽C(ε+λ)/g≤Ch。time查询合法需g≥d；角查询不足base时clip，超过1时trivial1。所有plane包括投影近退化的plane均已覆盖。

由g≤1按原reference积分，再除graphmean，可以保同一个任意相关g。对每个P有同一个upper，不是对无限plane族作概率union。fine误差厚化及K损失后，actual source取得正幂plane cap所需的指数均有明确余量。

此结论只控制2planes；一个affine row允许D落在3plane，root未过度推广。它也没有从plane cap推出observed集合growth。

## 6. 数字mask模型的全部量词：通过

对任意η>0先取固定大B=2^L，再取任意深偶数N，r=B⁻N。A₀取full二维x-grid及逐binary-block mask f，λ=Uniform(A₀)。其每个dyadic R-cell都共享完整binary prefix，所以全尺度coherence成立，不局限于B-adic尺度；fine与所有coarse edge均用终止二进制展开及半开cells处理。

任意unit normal的四个奇偶系数中至少一项bounded below。条件化其余digits后，剩一组B²-base、B个字母的finite Cantor变量，interval cap `C_Bq^(1/2)`对q≥r成立；末奇组spacing Br、末偶组r，二者末层原子质量r^(1/2)，所以q=r也合法。这给**全部affine hyperplanes**，从而所有2planes的一致cap；不作无限normal union。

真实实数和以raw digits e_i∈[0,2B−2]表示，故 `#(A₀+A₀)≤(2B−1)^(2N)`，与digitwise group或无carry假设无关。root的carry递推可明确取 `k₀`为首位整数carry、`k_N=0`，则 `e_i=a_i+B k_(i−1)−k_i`；每k_i∈{0,1}。给定carry vector后，vertical sum为f(x mod1)加固定常数。每scalar coordinate至多C2^N条translated mask graphs，二维≤C4^N。因此和集本身的**每个**dyadic visible fibre有uniform upper，不是只给A₀的属性。

Uniform(A)的2-Frostman确由fine visible-cell上至多C4^N个points与base-grid packing得到；未从coarse-cover直接声称fine质量upper。A₀⊂A₀+A₀因0∈A₀成立，root保守取并集仍不影响任何界。g=1_{a∈A₀}对Uniform(A)×λ有真实mean≥r^θ_B/2，且正权tuples精确落回A；这是保同carrier的小image关系。

先选B使θ_B与log_B4均小于η/4，再令N大吸收固定C_B及常数，就同时有K≤r⁻η、graphmean≥r^η。固定查询q=r^ε时的cap≤r^(ε/3)与η可任意小兼容；没有随η缩小这个fixed非集中指数。因此该例严格排除由plane cap/coarsegraph/2-Frostman alone推出fixed正growth的泛化。

## 7. source与弱化模型边界：通过其准确范围

数字模型未构造共同ν、M和原角law，使其λ等于 `((t−s)ψ,−[M(t)−M(s)]ψ)`；也未给真实T的jointAD/CW、W witnesses或两套grain coherence。它明确不是actual observed matrix接口的完整反例。反之，source稿与plane稿明确保留这个matrix-time分解，未把任意非平面law当原D。

因此本轮有两项可核信息：实际新增D的平面非集中；严格否定丢失D分解后的通用增长桥。**AFF₃及>2基数增长仍open。** 下一步若要有实质推进，必须使用原matrix-time关系或另一个实际未用约束，不能把一般additive law flattening、Y-only或global marginal独立化再次改名。上述scope不降低长期Goal标准，也不证明新高维维数界。
