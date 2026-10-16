# R0004：真实 assignment、own-depth 列表与 true floor 仍不等于小全局 palette

日期：2026-10-16。独立反例攻击：`lifting_obstructions`。状态：以下明确边界命题有完整证明，待交叉审查；未经外部同行评审。

## 0. 宏观目标、结论范围与停止条件

本轮检验 N5-POLY-CAP-01：源稿真实 assignment、点态标签知识和 true floors，是否已经迫使同一原始坐标中的二次方向多项式只有 subpower 个有效选择？已读 STATE.md、DIR-001、PRI-001，以及 Definitions 2.1–2.2、2.8、Lemma 2.10 和 2.11。

本文件不再只给任意速度分带。构造在**一个 world、每个实际时间层**中有常数总覆盖，assignment 在整个时间块内不变，标签由 own-depth 观测恢复到固定常数列表，每个 chart 都满足真实质量 floor。它还保留密度恰为 1 的完整原始斜率边缘。

明确限制：其隐藏密度是 `n(a)≈a`，即 d=1 的边界，**不满足 d<1 的密度亏损**；没有验证临界路径，也没有计算 horizon。模型的方向二次式来自真实可恢复的分带 assignment，尚未证明它们就是某个临界分支的 native Hessian 多项式。因而它严格排除“仅由 assignment/list/floor 就得到小 palette”的命题，不排除加上 d<1、特定 native 来源或临界性的新命题。

停止条件：上述反模型一旦成立，不再把点态列表常数直接替换成全局多项式数；必须使用新输入或真实的质量预算。

## 1. 单 world 的完整八维原始 prior

取独立均匀参数

\[
\theta\in[1,2],\quad z,v,W\in[0,1],\quad
x,c\in[-2,2],\quad \zeta_1,\zeta_2\in[-\sigma,\sigma].
\]

令轨道系数为

\[
V=(\theta,\theta^2+z,v),\qquad
y_0=(\theta^2+z+\zeta_1,\theta+\zeta_2,x),
\]
\[
w_0=c,\qquad w(t)=c+tW,\qquad Y(t)=y_0+tV.
\tag{1.1}
\]

这是到完整八个系数 `(y₀,V,w₀,W)` 的可逆映射，Jacobian 绝对值为 1。逆映射直接用

\[
\theta=V_1,\quad z=V_2-V_1^2,\quad
\zeta_1=(y_0)_1-V_2,\quad\zeta_2=(y_0)_2-V_1.
\]

所以 prior 在完整系数空间上为一个有限半代数区域内的常密度 `1/[16(2σ)²]`，其边界次数不超过 2。若 σ 是原始 N₀ 的固定负幂，就满足 Definition 2.2 的相应有限性要求。

**完整斜率** `(V,W)` 的密度恰为 1，位于一个固定有界半代数区域：`V₁∈[1,2]`、`0≤V₂−V₁²≤1`、`V₃,W∈[0,1]`。因此这里没有以高度为 σ⁻¹ 的方向密度偷付条件化成本；大的完整系数密度只在截距方向。

取 native 测试 `P_*=w`、B=1。全部时间上 |w|≤3、隐藏导数为 1、隐藏曲率为 0，base 与速度也都固定有界。

incidence event 固定为

\[
E=\{0\le t\le1/2,\ |Y_3(t)|\le1,\ |w(t)|\le1\}.
\tag{1.2}
\]

其 prior×time 质量为 1/8，故是常数而非幂小量。

## 2. 标签确实由观测恢复，不是不可见的内部 index

前两个当前 base 坐标满足

\[
Y_1=\theta^2+z+t\theta+\zeta_1,\qquad
Y_2=\theta+t(\theta^2+z)+\zeta_2.
\]

当 t≤1/2 时，矩阵行列式 `1−t²≥3/4`，故由 exact base 定义

\[
\widehat\theta=\frac{Y_2-tY_1}{1-t^2},\qquad
\widehat B=\frac{Y_1-tY_2}{1-t^2},\qquad
\widehat z=\widehat B-\widehat\theta^2.
\tag{2.1}
\]

它们分别与 θ、θ²+z、z 相差 O(σ)，常数固定。因此，只要 σ≪η，宽 η 的 z-band index 可由 exact `(t,Y)` 恢复到 O(1) 个选项；宽 q 的 θ-bin 也可如此恢复。这是实际观测给出的信息，不依赖 knowing 轨道的完整速度。

## 3. 实际 chart layer 与固定空间框架

取 dyadic q≤1/8，令 depth 厚度 a=q，取 dyadic η 满足

\[
q^2\le\eta\le q,\qquad \sigma\ll\eta.
\tag{3.1}
\]

以 q 为共同时间块宽度分割 `[0,1/2]`。固定一块 `I=[t₀,t₀+q)`。assignment 标签是以下四个实际轨道参数的 bins：

1. θ 的 q-bin；
2. z 的 η-bin；
3. `Y₃(t₀)=x+t₀v` 在 `[-1/2,1/2]` 内的 q-bin；
4. `w(t₀)=c+t₀W` 在 `[-1/2,1/2]` 内的 q-bin。

这些 assignments 在整个 I 内不变，且在同一 world/time 层两两不交。令各 bin 中心为 θ_c,z_c,b_c,e_c，取 affine base 中心

\[
y_c(t)=(\theta_c^2+z_c+t\theta_c,
\theta_c+t(\theta_c^2+z_c),
b_c+(t-t_0)/2).
\]

在前两个空间坐标取固定列向量

\[
A=(2\theta_c+t_0,\ 1+2t_0\theta_c),\qquad B=(1,t_0).
\]

令空间矩阵 D 的三列为 `(qA, ηB, q e₃)`。由于

\[
\det[A,B]=t_0^2-1,
\]

它始终可逆，且

\[
\|D\|\le Cq,\qquad J=|\det D|=q^2\eta(1-t_0^2)\asymp q^2\eta.
\tag{3.2}
\]

**全时间块的 containment 核查。** 写 θ=θ_c+s、z=z_c+r、t=t₀+τ。前两坐标与中心之差为

\[
A s+B(s^2+r)
\quad+\quad(\tau s,\ 2\tau\theta_cs+\tau(s^2+r))
\quad+\quad(\zeta_1,\zeta_2).
\]

其中 |s|≤q/2、|r|≤η/2、|τ|≤q。主项的 A 方向宽度 O(q)，B 方向宽度 O(η)；固定框架变化和曲率造成的额外法向误差为 `O(q²+qη+σ)=O(η)`。第三坐标因 v∈[0,1] 而在 q 级范围内。故整块上 `|D⁻¹(Y−y_c)|≤C`。

这一步使用 η≥q²；若只靠 z-band 极薄却忽略 θ 曲率，就不能得到这个 true chart。

取 quadratic/affine 测试

\[
P_c(t,Y,w)=w-e_c-(t-t_0)/2.
\]

整块上 `|P_c|≤q=a`，隐藏导数为 1，隐藏曲率为 0。所有 assigned trajectories 在整个 I 内也满足 event E。

## 4. 真实 n(a)、质量 floor 与半时间总覆盖

对 t≤1/2，(θ,z) 到无噪声 `(Y₁,Y₂)` 的 Jacobian 为 `1−t²`，其绝对值在 `[3/4,1]` 内。加入 ζ 只作一个小盒卷积，因此该二维当前密度 g_t 有统一上界；在原无噪声像离边界 Cσ 以外还有固定正下界。边界层的 incidence 质量 O(σ)。

在 event E 的 `Y₃,w∈[-1,1]` 上，由 x,c 的宽盒先验，当前 Y₃ 密度恒为 1/4，当前 w 密度也恒为 1/4，且 v、W 条件后仍均匀。故 dyadic hidden bin 宽度 a=q 时，观测 `(t,Y,[w]_a)` 的密度为

\[
g_t(Y_1,Y_2)\,a/16.
\]

除去 O(σ) 边界质量，密度在固定常数倍 a 之间，故真正的 homogeneous 尺度是 `n(a)≈a`。同样证明适用于预定隐藏 dyadic 深度表，得到 `f(b)=b`；其斜率是 1，不能伪装成 d<1。

每个 assignment 的**原始先验质量**精确为

\[
\nu_c=q\cdot\eta\cdot(q/4)\cdot(q/4)
=q^3\eta/16.
\tag{4.1}
\]

这里 v、W、ζ 都没有被额外条件化；因初始 x,c 在宽盒内，给定 t₀ 后对 `Y₃(t₀),w(t₀)` 的 q-bin 积分确为 q/4。

选择整个 I 的 incidences，得 `m_c=qν_c`。由 (3.2)，

\[
m_c/q=\nu_c\asymp aJ.
\tag{4.2}
\]

这就是 Definition 2.8 的真实 floor 及 saturation，常数不依赖 q、η、σ。

每个时间块里，所选 θ、z 覆盖全部各自先验；`Y₃(t₀),w(t₀)` 各覆盖长度 1，因此所选原始 prior 总质量为 1/16。所有 q-blocks 覆盖半时间，故系统总 selected incidence 质量为 **1/32**。这不是只在一个幂小时间块内获得的局部质量。

## 5. Own-depth 知识与完整列表大小

给定 own-depth 观测 `p_b=(t,Y,[w]_q)`，首先由 t 确定当前块 I。由 (2.1)，θ、z 的实际 bins 各只有 O(1) 个候选。

第三坐标的块起点为 `Y₃(t₀)=Y₃(t)−(t−t₀)v`。尽管 v 未知，v∈[0,1]、`0≤t−t₀≤q` 使它落在长度至多 q 的区间内，因此只有 O(1) 个 q-bin。

同理 `w(t₀)=w(t)−(t−t₀)W`。当前 w 仅知道一个宽 q 的 bin，但 W∈[0,1]，所以起点落在长度至多 2q 的区间内，仍只有 O(1) 个 q-bin。

四个候选列表取乘积，完整 chart 标签仅有**固定常数个**候选。若 terminal hidden 观测比 q 更细，也保持相同结论。列表可用有界分母的有理表达式 (2.1) 及有限 bin inequalities 编码；清分母后是固定次数半代数谓词，表大小是原始尺度多项式。因此这里满足真实 pointwise knowledge，而非只说全局标签数有限。

在 event E 的内部，条件 v 仍均匀于 [0,1]，故 conditional visible ball cap 还有 `Cr` 的正指数。这并不改变 d=1 的密度边界。

## 6. 全局原始方向多项式 palette 仍然很大

对每个 z-band j，令

\[
Q_j(V)=V_2-V_1^2-z_j,
\]

其中 z_j 是该 band 的左端点。所有属于该 assignment 的方向均满足

\[
0\le Q_j(V)<\eta.
\]

这些多项式的最大系数范数均为 1。不同 band 的系数距离至少 η，所以在系数精度 ξ≤η/4 下，一个球至多覆盖一个 Q_j。每个同一 world/time 层都需要

\[
R\ge\eta^{-1}
\]

个中心。取 η=q²，便有 R=q⁻²；这可为原始固定正幂，远非 subpower。与此相对，第 5 节的点态列表大小始终为常数。

实际 chart normalization 的 visible 仿射矩阵是 `F_c=D_c/q`。把 Q_j 按该**真实** F_c 拉回局部坐标，仍得到一个二次式；退回同一原始坐标后就是上述不同 Q_j。因此这个例子不依赖另造一个不对应 chart 的任意 visible frame。但没有证明这些二次式是临界 native 分支的 Hessian，不能越过这一来源限制。

DIR-001 的平方根并集准则在这里给 `R√η≈η^(-1/2)`，不会迫使总质量趋零；不能通过把 pointwise O(1) 替换成 R 来制造矛盾。

## 7. True floor 能提供的正向父预算

本轮源审计代理提出的下式经独立核查正确。设同一 world/time 层长度为 q，父 prior 质量 ρ_c、空间 Jacobian J_c，并有真实 floor

\[
\rho_c\ge n(b)J_c/K_{\rm sat}.
\]

原始 visible 方向密度至多 L，真实仿射规范化为 `V=v_c+(D_c/q)V'`，`|V'|∞≤T`。对 canonical parabola 薄层宽度 δ，原始 prior 坏质量 β_c 满足

\[
\beta_c\le\rho_c\min\left\{1,
\frac{8K_{\rm sat}LT^2\delta}{n(b)q^3}\right\}.
\tag{7.1}
\]

证明：先按方向密度和换元得 `β_c≤8L(J_c/q³)T²δ`，再代入 `J_c≤K_sat ρ_c/n(b)`，同时保留平凡界 β_c≤ρ_c。

若当前 incidence `µ≤Gνdt`，在 world/time 权重中求和，并用真实 assignment budget `Σω qρ_c≤1`，得到 uniform 参数时

\[
M_{\rm bad}\le G\min\left\{1,
\frac{8K_{\rm sat}LT^2\delta}{n(b)q^3}\right\}.
\tag{7.2}
\]

因此 floor **确实**消除了显式父数量；代价变成可核查的 `n(b)q³`。若只有质量比例 f 的子族被证明属于薄层，应使用必要条件 `f≤8K_sat LT²δ/[n(b)q³]`，不能把任意子族免费当成全父质量。

本例不反驳这个正向预算：它既在 d=1 边界，又没有提供小于实际 floor 成本的 canonical 薄层精度。它仅反驳无额外尺度条件的全局 palette 数结论。

## 8. 本轮精确边界与下一步

新验证的是：真实全块 assignments、固定框架 containment、同一原始完整斜率密度、own-depth 常数列表、逐 packet true floor 与常数总覆盖可以同时成立，而原始方向二次式 palette 仍有固定幂数量。

未验证并且不能省去的是：d<1、特定 native Hessian 来源、positive/optimal horizon、原始与切线尺度的统一成本。**H 在本文件中没有计算，也不宣称 H=0。** 原生 full-dimensional incidence 的 `n(a)≈a` 不自动给零 horizon。

该模型有一个五维正体积的 incidence 支撑区域，故不可能是小于五维的 Kakeya 反例。它提供的是一个真实 list/floor 的边界测试；它要求下一步使用 (7.2) 的精确尺度预算或完整密度亏损，而不是继续用点态知识代替全局 palette。
