# R0021：实际 mixed32 二次 alternative 的条件排除

2026-10-17，root。主任务 N5-MIXED32-Q01。结论条件于下列明确的实际 source 准备与 named Lemmas19.2/19.4/19.5；不将其全局可获得性当已解决，也不声称完整五维 Kakeya。有限多项式输入 PCT 在本轮另有自包含证明和独立反例审查。

## 1. 假设与结论的边界

原对象为 WZ2609.22035v1 Definitions17.2–17.4 的 d5/k3/ell2 配置；原 T 的 joint4-AD 和 convex Wolff、Φ/ξ 的原 coarse coherence、两套 grains、common Z 与全部原 witness marks 均保留。写

    f=(u,v), u∈R, v∈R²;
    tildef=(a,b), a,b∈R², v=a+b u.

固定 κ>ζ>0、γ>0、µ∈(0,1/4]，ρ∈[δ^{1/4},δ^µ]。明确假设以下固定尺度准备可用：

1. 存在全局 δ^{θ₀}-dense retained times；可删低密窗口，保留窗口内 time packing/density 和原 Eq good-q 选择。两 slope 在这些 ρ-windows 的 pairwise Lipschitz bound 为 Kρ。
2. 每个保留 window J 有完整 f 的 affine velocity (r,s)∈R×R²，满足 f(z)−f(z')=(r,s)(z−z')+O(Kρ^{1+ε₀})，且 K⁻¹≤|(r,s)|≤K。这里**没有**预设 r≠0。该完整速度非退化是 source 准备输入；其全局选择责任与 Lemma21.1 的量词问题不在本定理中被抹去。
3. 选 z₀∈J，h(z)=v(z)−b(z₀)u(z)。存在 A₀,A₁,A₂∈R²，使 h(z) 以 error Δ=ρ^ε(ρ²+ρ|A₁|+ρ²|A₂|) 被 A₀+A₁(z−z₀)+A₂(z−z₀)² 逼近，作用于该 window 的原 retained times。ε 足够小且 ε≤ε₀/2。
4. 原 V/J/L graph 的合法删选和 good-q averages 适用于以下有限次 stable refinement；详细 source 计数见 R0021_mixed32_source_audit.md，不重新赋予 selected 管族 AD lower。保留原 tube-KT tildeY 的指数1−γ。
5. named Lemma19.4（任意 d,k,ell）可对原配置的一个 dense local time cluster 调用；它的全部高级证明未在本轮重证。

K 代表每一步明列的小幂，次数可依固定 γ、κ、ε 等改变。先固定 ζ、γ、µ、ε₀、ε；再选全部 source/retained/stability loss θ 足够小，最后 δ 小。结论：这些假设不能与 C_CW(T)≤δ⁻η、κ>ζ 同时成立。它是所列**固定尺度条件版二次分支排除**，不是自动证明从任意原配置必进入此 alternative。

## 2. 原 graph 与真正向量 cubic

记 E(z,z')=v(z)−v(z')−b(z')(u(z)−u(z'))，τ≥δ 为 ρ max|E| 的固定倍。原 V/J/L、horizontal2 和 scalar Φ 给一个 bounded graph

    g(y,z,z',φ₁,φ₂)∈[0,1],
    mean g≥K⁻¹,
    y+(z'−z)E(z,z')(φ₁−φ₂)∈N_{Kτρ+Cδ} tildeY_{z''}(q).

这里 y∈R²，z,z' 为原 δ-time，φ_i 为原 Φ 的 ρ-bin；y 的 vector 性不改变 code 恢复的 horizontal2 幂。合法 averaging 和 scalar Φ 的 κ-AD 可固定 y,z',φ₁,φ₂，保住≥K⁻¹ρ/δ 个 z 与 |ψ|=|φ₁−φ₂|≥K⁻¹。不需要假设这些 z 均匀，亦不需要每条原管独立有满数目 marks。下文明确取 ψ=φ₂−φ₁，所以 (z'−z)E(z,z')(φ₁−φ₂) 代入 E 后正好是正号的 P；只是固定角标签的反向差，不改变原 graph 质量。

设 c(z')=b(z')−b(z₀)。由 affine u 和 quadratic h，

    E(z,z')=(z−z')[A₁+A₂(z+z'−2z₀)−c(z')r]+O(KΔ).

ρ^{2+ε₀} 的混合误差可被 Δ 吸收（ε≤ε₀/2）。因此真正的二维 cubic

    P(z)=(z−z')²[A₁+A₂(z+z'−2z₀)−c(z')r]ψ

在上述原 dense samples 上落入 N_e(tildeY_{z''}(q)−y)，

    e=K^C(τρ+δ+ρΔ).                           (1)

graph 中所有点和 Φ 都仍来自同一原质量，φ coarsening 的附加误差 O(τρ) 已在(1)中。

## 3. PCT 的全部尺度在原空间可支付

只将 polynomial domain 的 J 长度ρ归一到[0,1]，d=δ/ρ；不缩空间 tildeY。因此原 Def17.4 的 tube-KT 对所有 δ≤e'≤L≤1 直接可用，子集/平移保持 upper，不冒充被切 Y 的 AD lower。

先付整个 polynomial window 的系数 upper。h 在原 samples 上 bounded by Kρ（减去一个值即可），有限次插值/Remez 给

    ρ|A₁|+ρ²|A₂|≤K^C(ρ+Δ).

将 Δ 的定义代入，因 K^Cρ^ε≪1 可吸收，故

    ρ|A₁|+ρ²|A₂|≤K^Cρ,  Δ≤K^Cρ^{1+ε}.

再用 |c(z')r|≤K^Cρ，得完整 cubic 的振幅 R≤K^Cρ²≤1。于是

    dR≤K^Cδρ≤δ≤e.

这一步没有仅凭离散样本的小值推整个 window 小；用了固定次数的系数范数。若(1)给 e≥固定常数，可把它取为平凡上界并直接用 R≤1；在当前参数和 δ 小的非平凡分支，e<1，故满足 PCT 所有假设。P(z')=0，故振幅 bound 同时控制绝对值。

修正版 PCT 给

    osc_JP≤K_γ(τρ+δ+ρΔ),                     (2)

其中 K_γ=δ^{-Cθ/γ} 及固定常数，先固定 γ、再令 θ 小。不能把原草案幂外 C 的错误 uniform-γ 版本拿来用。由 vector cubic 系数范数和 |ψ|≥K⁻¹，(2)给

    |A₂|≤K_γ(τ/ρ²+δ/ρ³+Δ/ρ²),
    |A₁−c(z')r|≤K_γ(τ/ρ+δ/ρ²+Δ/ρ).         (3)

这些估计对 graph averaging 保住的 K_γ⁻¹比例 z' 成立。z' 外的任意 retained z 代回同一 quadratic，得

    ρ|E(z,z')|≤K_γ(ρτ+δ+ρΔ).                (4)

## 4. 稳定细化与 τ-collapse

用 source 的有限稳定化：取 θ_{j+1}=sqrt(θ_j)，初始 θ₀包括所有既有 loss，最后 θ_{M+1} 仍足够小；固定 M≥20/ε。τ_j 在满足相应全局 retained density 的原 time 子集中最小化；允许删低密 windows 并同尺度 pigeonhole。有限多个 loss 的系数可依 γ，因此需 θ₀ 更小，不能把1/γ删除。

若某 τ_j≤ρ^{3+ε/2} 已得到所需。否则所有 τ_j 在该下界与 Kρ²之间；由乘积比较存在 j，使 τ_{j+1}≥ρ^{ε/10}τ_j。上节从 τ_j 数据提取的 good z' 在每个保留 window 均有 K_γ⁻¹比例，取其全局并仍是下一最小化的合法候选，因为 θ_{j+1}≫C_γθ_j。由(4)得到

    τ≤K_γρ^{-ε/10}(δ+ρΔ).                  (5)

由(3)、|c r|≤Kρ 和 Δ 定义，

    Δ≤K_γρ^ε(ρ²+τ+δ/ρ+Δ),
    Δ≤K_γρ^ε(ρ²+τ+δ/ρ).                    (6)

第二式用 θ_j 足够小于 µε 吸收。把(6)代入(5)，并先选择 θ_j 使 K_γ≤ρ^{-o(ε)}，吸收 τ 项。ρ≥δ^{1/4} 保证 δ≤ρ⁴，最终得

    τ≤ρ^{3+ε/2}.                             (7)

所有 surviving data 都仍是原 time/points/tubes；这里只改受审候选的 time density，没有把它重置为完整新 AD 配置。稳定化的 source 准备属于第1节明确输入，不能从一个单独 window 推全局密度。

## 5. scalar r 非退化、整列 b 与原 tildef

原 times 有≥K⁻¹ρ 的 span。选一对 gap≥K⁻¹ρ 的 times，由 whole-f affine approximation 和(7)，

    |s|≤K|r|+K_γ[τ/ρ²+ρ^{ε₀}].             (8)

后项比第1节的 whole velocity lower K⁻¹ 小；结合 |(r,s)|≥K⁻¹，得 |r|≥K⁻C。r 非零是推出来的，没有从向量 (r,s) 非零直接偷换。

精确恒等式

    E(z,z')+E(z',z)=(b(z)−b(z'))(u(z)−u(z'))

与 affine u、osc b≤Kρ 给分离 pair

    |(b(z)−b(z'))r|≤K_γ[τ/ρ²+ρ^{1+ε₀}]
                       ≤K_γρ^{1+ε/2}.

r 是标量，所以可合法除以 r 控制整个二维列 b。对近 pair 用同一个远 anchor；dense original times 的 packing 确保可选，不重置权重。于是 osc b≤K_γρ^{1+ε/2}。

在原有界坐标中，consistency 直接给

    a(z)−a(z')=E(z,z')+[b(z')−b(z)]u(z).

因 u 有界，osc a≤K_γρ^{1+ε/2}。若另付固定轴对齐 u(z₀)=0，则可强化 a 的ρ²，但终步不需要，也不用它改善 b 的保守指数。故整个原 tildef=(a,b) 在一个 dense 原 window 上振荡≤K_γρ^{1+ε/2}。

## 6. named Lemma19.4 产生真实正 CW gain

取 σ=ρ^{1+ε/4}。令所有 θ 足够小，whole tildef 振荡≤σ，且 σ∈[ρ²,ρ]、ρ≥δ^{1/3}。保留时间相对原 Z∩J 的 density≥δ^{C_γθ} 已包括在 K_γ；无需给删选管族新 AD。原 Lemma19.4 给

    C_CW(T)≥δ^{C_γθ/γ}(ρ/σ)^κ
             =δ^{C_γθ/γ}ρ^{-κε/4}
             ≥δ^{C_γθ/γ−µζε/4}.

先固定 γ、µ、ζ、ε，再选全部 loss使 C_γθ/γ+η<µζε/8，最后 δ 小；这与 C_CW(T)≤δ⁻η 冲突。没有使用原PDF99未补证的更强ρ^{2+ε/2} row估计或ρ⁻κ CW强化。

## 7. 当前真正推进与尚未完成部分

本轮给 vector-Y 二次压缩新增一项实质几何输入，且在 scalar-u/r 分支把整列 tildef 慢变和正 CW gain 接通。它不重复 mixed42 的 orthogonal-row 归约。有限 PCT 已自包含证明；上面是实际-source条件应用，完整 source 高级 Lemma19.4、固定尺度 whole-f affine/非退化准备及 stable graph 量词仍各列责任。

若这些准备不是已付 source 后果，不能把条件定理登记成整个 N5-MIXED32-Q01 已无条件解决。下一步优先审实际 alternative 的获得与图的全局删选闭包；若只是重述同一条件，须 macro 选不同实质任务。非二次、其他 mixed、更高维一般归约和 Hausdorff 均未完成；无新维数界或已确认重大中间结果。
