# R0014：联合四环的秩下降与未截断 L² 能量障碍

2026-10-17。作者：`lifting_obstructions`。任务 N5-COUPLED-PROJ-01。以下给出一个真正使用两个共享时间 blocks 的严格新约束：四条参数线在四个分离时刻组成近似闭环，则全部方向必须接近由首边确定的同一个二维 affine plane；同时给出全部原量词下未截断 L² 不能直接给幂 gain 的实际有限构型。两项均不证明或反驳 (CP)，不声称新颖性、五维 Kakeya 新界或重大结果。

## 1. 数据、方向与参与定义

固定本轮 spec 的同一个有限图

\[
 P=\{(b,d,f(v),c,e,g(v)):v=(b,c,d,e)\in\Omega_\delta\},
\]

其中 κ(v)=(1,v)/√(1+|v|²) 彼此 δ-separated，#P≈δ⁻⁴，slopes 位于固定小盒，anchors 有固定界。记实际方向坐标投影为

\[
 q(p)=(b,c,d,e)\in\mathbb R^2\oplus\mathbb R^2.
\]

这与上一轮 D(P)=(b,d,c,e) 只差固定置换。本稿使用 q 的顺序，使两个第一系数 (b,c) 和第二系数 (d,e) 各为一个二维向量。

令 γ(t)=(1,t,−t²)，A_t=[[t,−1,0],[0,t,1]]，Π_t=A_t⊕A_t。全部 t 在 I=[1/4,3/4]。原 shading 的 P_j 只能从固定 P 选择；本稿不改 anchors，不引入独立 t₁,t₂。

## 2. 三列抛物线矩阵的显式条件数

若 s₁,s₂,s₃∈I 互距至少 ρ>0，令 G=[γ(s₁),γ(s₂),γ(s₃)]。则

\[
 \boxed{\|G^{-1}\|_{2\to2}\le5\rho^{-2},\qquad
 \sigma_{\min}(G)\ge\rho^2/5.}            \tag{2.1}
\]

证明：令 L_i(s)=∏_{k≠i}(s−s_k)/∏_{k≠i}(s_i−s_k) 为 Lagrange polynomials。每个 denominator 绝对值≥ρ²；分子的常数、一次、二次系数绝对值分别≤1、2、1。G⁻¹ 的第 i 行正是这些系数、仅第三项改符号，所以其 row norm≤√6ρ⁻²，整个 Frobenius norm≤√18ρ⁻²<5ρ⁻²。无需用粗的 determinant⁻¹ ρ⁻³。

这个界对三个时刻的任意排列都成立，不要求它们按 cycle 的时间顺序递增。

## 3. 联合四环：固定首边决定方向平面

**命题。** 给 p₁,p₂,p₃,p₄∈R⁶，置 p₅=p₁。给四个时刻 t₁,…,t₄∈I，任意两个时刻相距≥ρ。假设每个相邻 pair 在自己的同一时刻 joint-close：

\[
 \|\Pi_{t_i}(p_{i+1}-p_i)\|_\infty\le\varepsilon
 \quad(1\le i\le4).                      \tag{3.1}
\]

定义首边的两个 first-coefficient differences

\[
 u_1=(b_2-b_1,c_2-c_1)\in\mathbb R^2.
\]

若 u₁≠0，令 e=u₁/|u₁|，并置

\[
 W_e=\{(\alpha e,\beta e):\alpha,\beta\in\mathbb R\}
       \subset\mathbb R^4.
\]

则所有四个实际方向坐标都满足

\[
 \boxed{\operatorname{dist}
   (q(p_j),q(p_1)+W_e)\le500\varepsilon\rho^{-2},
        \quad1\le j\le4.}                \tag{3.2}
\]

更强地，在 R³⊕R³ 中，它们到 p₁ 加一个三维子空间

\[
 S_e=\{(e_1 z,e_2 z):z\in\mathbb R^3\}
\]

的距离同样≤500ερ⁻²。若 u₁=0，则所有 p_j 在 radius500ερ⁻² 的球中；这种退化不允许逃过结论。特别是一个固定首边的全部 eligible four-cycles 共用同一个 W_e，时刻可以随 cycle 任意变化，只需保持给定 separation ρ。

### 3.1 证明及常数

写 Δp_i=p_{i+1}−p_i，令 u_i=(Δb_i,Δc_i)。单块 residual 写为 r₁=tΔb−Δd、r₂=Δf+tΔd；由 |r₁|,|r₂|≤ε，

\[
 (\Delta b,\Delta d,\Delta f)
 =\gamma(t)\Delta b+(0,-r_1,r_2+t r_1).
\]

一个 block 的 error norm≤√5ε，两个 blocks 合起来≤√10ε<4ε。因而

\[
 \Delta p_i=(\gamma(t_i)u_{i,1},\gamma(t_i)u_{i,2})+E_i,
 \qquad |E_i|\le4\varepsilon.             \tag{3.3}
\]

闭环 ΣΔp_i=0 给两个 coordinate-wise 向量关系，其 combined residual norm≤16ε。对 G=[γ(t₂),γ(t₃),γ(t₄)] 使用 (2.1)，直接解后三个 u_i，得到

\[
 u_i=-L_i(t_1)u_1+\eta_i\quad(i=2,3,4),
 \qquad \left(\sum_{i=2}^4|\eta_i|^2\right)^{1/2}
        \le80\varepsilon\rho^{-2}.       \tag{3.4}
\]

这里 L_i 是以 t₂,t₃,t₄ 为 nodes 的 Lagrange polynomials，|L_i(t₁)|≤ρ⁻²；首边系数为1。没有除以 |u₁|，所以 (3.4) 的 error 不含首边角度的逆幂。

每条 Δp_i 到 S_e 的距离≤√3·80ερ⁻²+4ε<143ερ⁻²；一个 vertex 与 p₁ 之差最多由三个 edges 相加，所以 500ερ⁻² 足够。q 只是坐标删除/置换，不增范数，得到 (3.2)。若 u₁=0，则 (3.4) 使所有 u_i 都是 error 量，连同 (3.3) 给同样的球半径界。

### 3.2 精确情形与真正的两块信息

ε=0 时，四个 Δp_i=(e₁z_i,e₂z_i)，全部 block coefficient vectors u_i 共线。这来自四列 γ(t_i) 的唯一一次线性相关：三行 Vandermonde matrix 的 kernel 为一维，而两个 blocks 必须使用同一条 kernel relation。四环因此被压进一个嵌入的三维 horizontal 子空间。

若只有一个 block，u_i 为 scalars，“共线”不给额外信息；它不是单块结论或参数 fiber 的改写。两块独立 first-coefficient differences 的非零楔积，与四个分离时间的精确 closed cycle 不兼容。近似时由 (3.4) 还得

\[
 |\det(u_1,u_i)|\le80|u_1|\varepsilon\rho^{-2}.
                                                        \tag{3.5}
\]

三环是自然校验：三个互距≥ρ的 t 的 Γ 可逆，闭环直接迫全部 u_i=O(ερ⁻²)。精确情况下没有三个不同参数的 separated-time triangle；并非把共时刻大 bush 当作禁止的 triangle。

## 4. 原完整方向来源给出的 packing 后果

若 p_i 是本轮固定图中的参数，则 q(p) 的 raw slope points 也 δ-separated：κ 在固定盒上 Lipschitz，单位方向分离至少迫 raw slopes 相距一个固定倍δ。固定一个有向首边 (p₁,p₂)，在所有满足 (3.1) 且 time gap≥ρ 的四环中，出现的第三、第四方向都位于 (3.2) 的同一个 affine two-plane tube 中。

对 bounded R⁴ 盒内 δ-separated points，width w 的 affine 2-plane neighborhood 最多容纳

\[
 C_r\min\{\delta^{-4},\ \delta^{-2}(1+w/\delta)^2\}
                                                        \tag{4.1}
\]

个点。证明是对 disjoint radius cδ balls 作四维体积比较；plane 的两个 tangential directions 有 bounded extent，两个 normal directions 宽≤C(w+δ)。

因此当 ε=Cδ 时，固定首边全部 time-separated four-cycles 能使用的第三、第四 tube directions 总共最多

\[
 \boxed{C_{r,C}\min\{\delta^{-4},\rho^{-4}\delta^{-2}\}.}
                                                        \tag{4.2}
\]

这比无约束的 δ⁻⁴ candidate vertices 有真实的秩损失。它使用同一 direction graph 的每方向一个 anchor 及原 separation；若允许同一方向任意多个 anchors，则不能由 direction packing 控制参数数目。若 u₁=0，可进一步用球 packing 得 C(1+ερ⁻²/δ)⁴，通常更小。

原 joint δ-cell incidence 若给出四个 pairwise contacts，必满足 (3.1)，ε 是固定倍δ；用 midpoint 而非轴的某个邻近 clock 时刻仅改变该固定倍。该 lemma 是必要上界，不会将几何近交反向新增为原 shading label。它也没有证明原 dense P_j 产生足够多、时刻真正分离且方向非退化的四环。

## 5. 未截断 L²：全部原量词下的 caustic 构型

下面严格否定另一项可能的捷径：直接给原全部 marks 的 joint collision energy 一个固定幂改善。取 Ωδ 为固定小四维盒中的足够大常数倍δ-grid，故方向 κ(v) δ-separated、#P=N≈δ⁻⁴。固定 τ=1/2，anchors 取

\[
 f(v)=-\tau d,\qquad g(v)=-\tau e.
\]

anchors bounded，单位轴及共同 I 与本轮完全一致。用二维向量 X=(b,c)、Y=(d,e) 和 h=t−τ 重排 outputs，得到

\[
 \Pi_t p=(tX-Y,hY).                      \tag{5.1}
\]

可取全部 P_j=P；也可只取 |t_j−τ|≤λ，其中 λ=δ^η、0<η<1，为 active times，其他 P_j=∅。后一选择满足原总 dense mass≥cλNδ⁻¹；固定常数可由先 ε 后 η 的门槛吸收。

令 n_j(Q) 为 joint output δ-cell 中的 active indices 数，S=Σ_jΣ_Q n_j(Q)，E₂=Σ_jΣ_Q n_j(Q)²。closest midpoint time 有 |h|≤δ/2，此时 hY 只占 O(1) 个二维δ-cells，tX−Y 只占 O(δ⁻²) 个 cells。所以该一时刻已有

\[
 E_2\ge cN^2\delta^2\asymp\delta^{-6}.   \tag{5.2}
\]

也有 matching upper。固定一个 index 的 joint-close partners 必满足每个 coordinate 的

\[
 |t\Delta X-\Delta Y|\le C\delta,
 \qquad |h\Delta Y|\le C\delta.
\]

ΔY 每 coordinate 至多 C[1+min(δ⁻¹,|h|⁻¹)] 个 grid choices；固定后 ΔX 仅 O(1) choices，因 t≥1/4。两个 coordinates 合起来，每 index 的 partner count≤C(|h|+δ)⁻²。对 δ-spaced midpoint times 求和，

\[
 E_2\le CN\sum_j(|t_j-\tau|+\delta)^{-2}
       \le CN\delta^{-2}\asymp\delta^{-6}.
                                                        \tag{5.3}
\]

故即使 full marks，也有 E₂≈δ⁻⁶；任何不剪 caustic 的统一 upper E₂≤Cδ^{−6+σ}、σ>0 都是假。窗口选择时 S≈λδ⁻⁵，普通 Cauchy 从这项实际 energy 只能给

\[
 \sum_j\#\{Q:n_j(Q)>0\}\ge S^2/E_2
       \asymp\lambda^2\delta^{-4},       \tag{5.4}
\]

停在 CP 的四维底线，不能凭更乐观的 untruncated energy 结束证明。

这不是 CP 反例：直接对 (5.1) 的两个网格 blocks 作 covering/packing，可得每时刻

\[
 N_\delta(\Pi_tP)\asymp
       \delta^{-4}(|h|+\delta)^2,
\]

于是窗口总 cover 为≈δ⁻⁵λ³；当 η 可任意小，这仍接近完整五维 exponent，而非 δ⁻⁴。

## 6. Caustic 可剪，故仍缺什么

若 δ≪s≪λ，删除 |t−τ|<s 的 marks，原 incidence mass 只损 O(s/λ) 比例；保留部分 energy 满足

\[
 E_{2,\rm keep}\le C\delta^{-5}s^{-1}.
\]

Cauchy 随即给 cover≥cλ²δ⁻⁵s。取 s=δ^a、固定 a>η，就可能得到固定幂 gain。因此第5节只排除**未截断**的能量捷径，不能当作允许原质量修剪的能量路线反例。

目前的两个可审查结果互相兼容：caustics 说明原 energy 会集中在短时间退化部分；四环秩下降说明 separated-time 的真正 joint cycles 有固定首边的二维 direction packing 限制。尚未证明的是：任意 bounded anchors、任意 dense P_j 下，能否在保留足够原 mass 后获得足量这样的 four-cycles，或用该 packing 上界直接控制合适的 truncated energy。

没有将该缺口改名为假设，也没有以 full direction projection 自动给 conditional independence。本轮 joint 结果是 (3.2)/(4.2) 的实际代数几何约束及 (5.2)–(5.4) 的 energy 门槛；CP 的 σ>0 仍未闭合，后续交 root 独审及共同量词检查。
