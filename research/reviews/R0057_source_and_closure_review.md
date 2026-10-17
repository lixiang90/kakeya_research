# R0057：source、原质量与全分区费用的正式独立审查

2026-10-17，A。实际完整读取 root《R0057_charged_joint_capacity_envelope_and_stop》10节、B《R0057_joint_packet_budget_counteraudit》8节、A主稿10节、最终 macro6、next6 与 working_spec6；root/B 新增 continuous all-fine sharpness 段亦逐式读回。A 主稿由本人撰写，不把它计为独立审查。下面对 root/B 的证明与整合范围作独立核验。结论是**在明确的 fixed-block scalar-K/full-slab 聚合范围内通过**，无尚待修复的数学项；没有证明 H5 或 source103页，未经外部同行评审。不预认证尚未生成的元数据、Git 或远端状态。

## 1. 一手 source 的实际量词与条件时间

本轮实际重读已入库 elliptic 原文 PDF9–12、抽取 `split('\n')` 411–630行。Def2.1/Th2.2 只在 fixed 0<s≤1、0<κ<1/10、fixed finite D、bounded U/V 下给 universal retained-law 估计；base label 决定 U/V，time 的 maxweight 与 support-count 两界在每 dyadic depth 都是条件式。独立中心、同 ellipse shape/orientation，initial floor M^−D、terminal floor M^−(D−1)、X_v 且 v=T1 左端，均在 root/spec 中准确保留。

q*≥1+2s−10κ 是 lower statement，不能推最优 q* 的 upper。root§1/7 与 B§5 已正确限制为“只调用具名陈述所保证的严格 q”。每个 fixed q 的小 ε 阈值可对所有有限 D 一致，而大 base 阈值仍可依 fixed D；root 选 fixed D≥2 来覆盖固定坐标变换后的 cδ 测试，合法，不令 D 沿内层 base 无界。

root§2 的两次无条件顺序调用也只声称可付闭包：若 ν≤μ 的质量为 r，先删原 base retained fraction<r/2，损≤r/2；余 label 的 conditional time density≤2/r，归一 spatial cap 亦多≤2/r。r=M^−o(1) 时是 subpower；fixed-power 原密度须令 η 进入 source 容许误差。它不赋予每个任意小包免费 time profile，更不能把两 marginal caps 相乘。Lemma2.3 仅对其原 reference/有限 prefix/whole-fiber 修剪量词使用，未扩大成任意 conditioning 定理。

## 2. 原 unit axes、共同 clock 与可测分区

独立重算 root§3：原真轴中点(0,b,a)，单位方向(1,a,b)/|(1,a,b)|；固定共同短 clock 位于所有原 unit axes 内，使用原完整 shading 的固定比例，不延长轴。τ=t/ℓ+1/2 后

    U1′=ℓa，V1′=b−ℓa/2，U2′=ℓb，V2′=a−ℓb/2；
    U1′=ℓV2′+(ℓ/2)U2′，
    V1′=(1/ℓ−ℓ/4)U2′−(ℓ/2)V2′。

两式正确，系数只依 fixed ℓ，不依 ellipse eccentricity。故任意 base Γ_j 支持于第二块两个 E_j 平移，就使第一块支持于两个 fixed-dilate 同形椭圆，不需要 Γ_j 乘积、均匀或条件后独立。

K_j 属于同一个 fixed original block 坐标，含上面的共同 scalar clock 变换。它若来自较早 source prior，该 prior 仍支持 Γ_j；一个 fixed-cover 测试承载固定正概率，故 K_j≥c/Wκ(E_j)。root 的 D2 与最大轴≤1覆盖费用足够。perpacket anisotropic 空间归一化需重付物理终端 tests/cells；macro 明确未否定这一未定义架构，不能将其默认为已纳入全称。

δ-grid 的方向映射在 bounded chart 双 Lipschitz，固定稀疏网步给真实 δsep 与≈δ^−4 labels。有限版以原计数概率和 uniform time bins 重做同一证明；source在 finer-than-δ 测试有 atomic 费用时只令 K 更大。没有将 Oδ jitter 当原 marks 全新选择。补全 S4 的 rotations 若改变 block split，不能据一个 chart 反攻推全部 adaptive atlas 失败；root/B 已准确说明。

## 3. 全 partition、任意 dominated ν 的费用证明

独立核 root§§4–6 与 B§§2–4。写 dν=g dμ，0≤g≤1，原 p0_j=μ_P(Γ_j)、p_j=ν(Γ_j×clock)。令 h_j(t)=∫Γj g(P,t)dμ_P(P)，则 h_j≤p0_j；可测时间支持 A_j={h_j>0} 或正质量 δ-bin 并都给

    p_j≤p0_j |A_j|，
    Σ p_j|A_j|≥Σ_(p0j>0) p_j²/p0_j≥m²。

这里 clock 已归一长1；原 I 版本只多固定 |I|。零 p0 强制零 p；countable 求和用非负部分和、Tonelli。没有把最终 p_j 重新当原 prior 分母，亦未因删除时间而免费缩短 clock。

完整 slabs 面积为常数倍 |A_j|L_jw_j，全部支持于同一个固定 bounded box。故以连续 dt dx2 或 δΣ_v dx2 作相同归一，

    ∫Σp_jK_j1Sj
      ≥cΣp_j|A_j|(w_j/L_j)^κ
      ≥cδ^κm²，
    ||Σp_jK_j1Sj||∞≥cδ^κm²。

这真实覆盖全部可测 base partitions、自适应 ellipses 与任意 time-dependent dominated ν；不是只有一个 fixed packet 的 bad conditional K。固定 B 重复 cover 只能把二次质量下界除 B，不能重复原 mass 无费。Lp 推论仅由 fixed-volume Hölder，正确。

## 4. sharpness、新 guaranteed rate 与 RHS 的逻辑方向

fresh 核 root§6 与 B§7 的 continuous all-fixed-D 扩展：按 A2、B2 的 δ-strips 分包，p_j≈δ²。原 conditional 4D density≤Cδ^−2，两个 long-coordinate 联合边缘密度≤C；共同 clock 的 scalar 可逆 mix 不混 long/normal，保这两界。任意旋转 F、半轴 L,w，两个估计给

    Pr(U1′∈u+F,V1′∈v+F)≤CL²min{1,(w/δ)²}。

除 Wκ(F)，w≥δ 时≤CL^(1−κ)w^(κ−1)≤Cδ^(−1+κ)；w<δ 时≤Cδ^−2L^(1−κ)w^(1+κ)≤Cδ^(−1+κ)。所以 continuous K≈δ^−1+κ，all fixed D 合法。normal slab center kΔ+ℓ(v−1/2)lΔ；fixed v,x2 每 l 仅 O(1) 个 k，overlap≤Cδ^−1，得 sup envelope≤Cδ^κ，与 lower 同阶。未 jitter 的 finite atomic law 在 w<δ 不能免费继承此 upper，root/B 已明确；D1 sharpness 与 D2 lower 不混淆。

实际 source upper RHS 的系数是调用前 θ_j≥p_j。δ^qΣp_jK_j1Sj 只是这个 RHS 的乐观数值 lower，**不是实际 atom 的有效 upper，更不是 atom lower**。所保证 q_j<1+2s_j−10κ≤3−10κ 给这一数值表达式的 sup≥cδ^(3−9κ)m²；即使假给 q=3，仍≥cδ^(3+κ)m²。m≥δ^η、η足够小时均不能作 δ^(4+σ) cap 证书。两种归一化 ν 或 ν/m 均保这个固定指数差。

真实交换 map 在小 clock 上 Jacobian=(1−t²)²，density 有界、δ-cells mass O(δ^5)，证明本负结论仅属于该 upper expression 的损失。root 没有据两项各自 sup 大就断 min 的 sup 大，也没排除实际 joint-support 上的更精细利用。

## 5. 原权、密度闭包与旧等价目标

全量 m 是原 incidence 平均 retention，非每管密度。整 label 分包且完整 Y_i 保留时，每根余管继承原逐管 λ_i；进一步按时间缩 shading 后要 heavy-fiber 重收，不能由 m 直接声称逐管 near-full。所有 p0_j、θ_j、p_j 均来自原 μ/ν，没有任意重新归一成等权 packets。

已实际重读 R15 两稿：对全部原 shadings 一致的 CP gain 可在 high-cell 删选后再次调用，给任意稍小 gain 的常数比例 PM；PM 以 mass/threshold 反推 CP。因此不把本轮“条件联合 gain”当另一个独立总目标。当前是同一 H5 的一次新具名输入应用测试，其实质新信息是全 partition/全 ν 的 charged envelope 与连续 sharpness；无新 ID、重大性或优先权认证。

## 6. 最终 macro/next 与审查结论

实际读回最终 macro6、next6 与 spec6：停止 fixed-base/split 的 scalar-K/full-slab-sup 架构，不续 κ/s/strip/包数，未声称所有 conditional 或 joint 策略不可能。未覆盖 adaptive charts、perpacket metric、真实 joint support、不同原几何或更强 singleblock 定理。elliptic103页仍是具名输入未 wholeproof 独证，H5/G3/general-to-sticky/actualmixed 未解；已付四维内部 assembly 和既有 KT/DIM 定位未被重写成新缺口。

next 诚实注明 R58 尚未选中一个已检验数学命题，要求开轮重选完整目标的真正未付 joint 几何并同轮执行；不能把宏观选择、survey、strip 支持缩小或 CP/PM 改名作为研究完成。这与本轮停止条件一致，不预认证后继可行或降低 Goal。

**最终通过范围：**root/B 的 source 接口、原 unitclock 与 weights、任意分区/保留的费用下界、continuous sharpness、certificate 失败及宏观停止范围。无待修数学项；不通过普通高维 Kakeya 结论、Th2.2 全证明、所有联合方法失败、新颖性/重大性或未来同步状态。本人停止本轮编辑与检索，由 root 统一整合归档。
