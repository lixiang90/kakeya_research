# R0007：WP4 的加权二次曲面反例；所有 fulltime 空间框的 cap 核验

日期：2026-10-16。作者：`lifting_obstructions`。状态：完整自包含证明，主代理已初核核心估计，待最终内部交叉审查。

## 0. 结论与文献归属

`research/rounds/R0007_working_spec.md` 中的 WP4 **不成立**。对任意大 dyadic D，令 δ=D^{-1}，可构造有界仿射迹线 `M_i:[0,1]→R³`、正权重 ωᵢ，使：

- 对所有正交空间框、所有仿射中心及所有 cell 宽 `1≤a₁≤a₂≤a₃≤D`，其完整时间 plank 满足 `Σ_{M_i⊂P}ω_i≤a₁a₂a₃`，即 A=1；
- 每条迹线取全部 D 个 time bins，所以任何 `#J_i≥D^{1−η}` 条件均满足；
- 所访四维 mesh cells 组成 E，有 `#E≤C D³`；
- `Σ_i ω_i #J_i≥cD^{7/2}`。

因此目标 `Σ_iω_i#J_i≤CA D^ε#E` 对每个固定 ε<1/2 都失败，且不能通过选择更小的 η 挽救。

这属于已知的 signature (2,2) quadric 障碍，不是本项目的新型 Kakeya 反例。Joshua Zahl 的综述 §4.1 明确讨论 `{ad−bc=1}` 的三参数线族、完整族的坏凸框、稀疏后的 convex Wolff 反例；见 [arXiv 2512.09397v1 §4.1](https://arxiv.org/html/2512.09397v1#S4.SS1) 及 [正式 ICM 版本](https://epubs.siam.org/doi/full/10.1137/25M1805965)。

以下直接核验 WP4 实际需要的**所有 fulltime 正交空间框**，并利用 WP4 允许任意正权重的条件，省去随机 thinning 与 copies。证明没有从某个最坏框的下界反推全体框上界。

## 1. 显式有界线族

在四维时空 `(t,x,y,z)` 中取

\[
 \mathcal Q(t,x,y,z)=ty+xz-1.
\]

它由 `{ad−bc=1}` 线性换名得到。取固定参数盒

\[
 \Omega=[1,2]\times[-c_0,c_0]^2,\qquad c_0=1/10,
\]

参数为 `(s,p,q)`，定义

\[
 b(s,p,q)=(s,-sq-p/s,1/s),
 \qquad u(s,p,q)=(p,-pq,q),
\]
\[
 M_{s,p,q}(t)=b+t u.
 \tag{1.1}
\]

逐项计算得

\[
 t(-sq-p/s-pqt)+(s+pt)(1/s+qt)-1=0.
 \tag{1.2}
\]

故全部完整迹线位于光滑三维 hypersurface `{\mathcal Q=0}` 上。位置、速度及所有参数导数在固定稍大的盒内都有绝对常数界，且

\[
 s=b_x,\qquad p=u_x,\qquad q=u_z.
 \tag{1.3}
\]

因此参数到完整 affine coefficients 的映射有定量 Lipschitz 逆，不存在把重复参数当作大量不同线的计数问题。

下面所有连续估计在例如 `[1/2,3]×[-1/5,1/5]²` 这样的固定扩大参数盒上也成立，常数仍绝对。令 μ 表示参数 Lebesgue 测度。

## 2. 所有 fulltime 空间框的连续聚集估计

令 `0<w₁≤w₂≤w₃≤C₀`。取任意正交单位轴 `n₁,n₂,n₃`，及任意仿射中心 `c(t)=c_b+t c_u`。定义 fulltime plank

\[
 P=\{(t,X):0\le t\le1,
 |n_j\cdot(X-c(t))|\le w_j,\ j=1,2,3\}.
\]

用 `\Omega(P)` 表示完整迹线 M⊂P 的参数集合。常数 C₀ 固定，允许由固定 chart 放大产生。

### 命题 QCAP

所有上述框均满足

\[
 \boxed{\mu(\Omega(P))\le C w_1\min(w_2,w_3^2).}
 \tag{2.1}
\]

特别地，若 w₂≥δ，则

\[
 \mu(\Omega(P))\le
 C\delta^{-1/2}w_1w_2w_3.
 \tag{2.2}
\]

最后一步只用

\[
 \frac{\min(w_2,w_3^2)}{w_2w_3}
 =\min(1/w_3,w_3/w_2)
 \le w_2^{-1/2}\le\delta^{-1/2}.
 \tag{2.3}
\]

证明分成三个初等引理。

### 2.1 最薄轴的一阶约束

对任意单位空间向量 `n=(n_x,n_y,n_z)`，令

\[
 F_b=n\cdot b=n_xs-n_y(sq+p/s)+n_z/s,
\]
\[
 F_u=n\cdot u=n_xp-n_ypq+n_zq.
\]

若 `|n_y|≥1/4`，则在整个扩大参数盒内

\[
 |\partial_p F_b|=|n_y|/s\ge c.
\]

若 `|n_y|<1/4`，则 `max(|n_x|,|n_z|)>2/3`；分别使用

\[
 \partial_pF_u=n_x-n_yq,
 \qquad \partial_qF_u=n_z-n_yp,
\]

至少一个在整个扩大盒内的绝对值有统一正下界。这些函数沿选定 p 或 q 方向都是**严格一次式**，无需隐藏的多分支/复杂性论证。

完整 M⊂P 的端点约束给 `F_b` 和 `F_u` 各一个长 O(w₁) 的允许区间（速度区间由 t=0,1 相减）。故在任何参数 cube，边长 Cr，最薄轴约束的参数测度至多

\[
 C w_1 r^2.
 \tag{2.4}
\]

这是直接 Fubini：选定方向的 fiber 长 O(w₁)，另外两方向各长 O(r)。

### 2.2 最大宽度的局部化

若 Ω(P) 非空，固定其中一条参考线 M₀。任何另一条 M∈Ω(P) 有

\[
 \|b-b_0\|+\|u-u_0\|\le C w_3.
\]

由 (1.3)，其参数全部落在一个边长 O(w₃) 的 cube。应用 (2.4)，得

\[
 \mu(\Omega(P))\le C w_1 w_3^2.
 \tag{2.5}
\]

### 2.3 两个短轴给至多两个平方根尺度的系数团

令 n=n₃ 为最长轴，π 为投影到 n⊥。对每条 M∈Ω(P)，

\[
 \|\pi M-\pi M_0\|_{\rm coeff}\le C w_2,
 \tag{2.6}
\]

此处 coefficient norm 是 affine t 多项式系数的最大值。写

\[
 \zeta(t)=n\cdot M(t),\qquad \zeta_0(t)=n\cdot M_0(t).
\]

把短轴部分固定为 πM₀，代入 quadric 得

\[
 \mathcal Q(t,\pi M_0(t)+z n)
 =A z^2+B(t)z+C(t),\qquad A=n_xn_z,
 \tag{2.7}
\]

B 为 affine 多项式，C 次数至多二。所有实际 ζ 的系数均有固定常数界。由 (2.6)、quadric 的固定系数及有界范围，

\[
 \|A\zeta^2+B\zeta+C\|_{\rm coeff}\le Cw_2,
 \qquad A\zeta_0^2+B\zeta_0+C=0.
 \tag{2.8}
\]

我们使用固定次数的 elementary polynomial norm fact：若 f,g 次数≤1，则

\[
 \|fg\|_{\rm coeff}\ge c\|f\|_{\rm coeff}\|g\|_{\rm coeff}.
 \tag{2.9}
\]

证明：把两者系数范数归一化为 1；紧集上乘积范数若趋于零，极限就是两个非零实多项式乘积为零，与整环性质矛盾。故存在统一正下界。

**情形一：|A|≥a₀。** a₀ 是下述固定的小常数。完成平方，令 `R=ζ+B/(2A),R₀=ζ₀+B/(2A)`。由 (2.8)，

\[
 \|(R-R_0)(R+R_0)\|_{\rm coeff}\le Cw_2.
\]

(2.9) 推出

\[
 \min(\|R-R_0\|_{\rm coeff},
          \|R+R_0\|_{\rm coeff})\le C\sqrt{w_2}.
 \tag{2.10}
\]

因此全部 ζ 在至多两个 affine coefficient balls 内，半径 O(√w₂)。结合短轴误差 (2.6)，全部完整 `(b,u)` 也在至多两个同尺度的 balls 内；由 (1.3)，参数在至多两个边长 O(√w₂) 的 cubes 内。w₂ 在固定有界范围内，故 O(w₂) 短轴误差可吸收进 O(√w₂)。

**情形二：|A|<a₀。** 此时不除以 A。沿参考线的空间法向导数是 affine 多项式

\[
 L_0(t)=n_x(1/s_0+q_0t)+n_yt+n_z(s_0+p_0t)
        =B(t)+2A\zeta_0(t).
 \tag{2.11}
\]

当 A=0 时，L₀ 不可能是零多项式：若 nₓ=0，则常数项 `n_zs₀=0` 迫 n_z=0，继而一次项 n_y≠0；若 n_z=0 同理。单位 n 与参考参数所在的集合紧，故在 A=0 上 `||L₀||coeff≥c₀>0`，并在足够小的 |A| 邻域仍有统一正下界。再缩小固定 a₀，利用实际 ζ、ζ₀ 的统一系数界，可保证

\[
 \|A(\zeta+\zeta_0)+B\|_{\rm coeff}
 =\|L_0+A(\zeta-\zeta_0)\|_{\rm coeff}\ge c_0/2.
\]

两式 (2.8) 相减并用 (2.9)，得

\[
 \|\zeta-\zeta_0\|_{\rm coeff}\le Cw_2.
 \tag{2.12}
\]

这是更强的单团局部化，也蕴含上述至多两个 O(√w₂) cubes 的结论。

综上，用 (2.4) 作用于至多两个参数 cubes，得到

\[
 \mu(\Omega(P))\le Cw_1(\sqrt{w_2})^2
 =Cw_1w_2.
 \tag{2.13}
\]

与 (2.5) 合并即证 (2.1)，继而证明全部框的 (2.2)。没有排除与 quadric 相切、长轴接近 null direction 或 affine center 特殊的框；这些分别由平方根双分支和 small-A 情形覆盖。

## 3. 连续估计到全部离散 planks

取 Ω 中的 δ 参数格点，记线族为 `\mathbb M_δ`，数量

\[
 \#\mathbb M_\delta\asymp\delta^{-3}.
 \tag{3.1}
\]

对每个格点取边长 cδ 的互不相交小参数 cubes，全部置于前述固定扩大参数盒 Ω⁺ 内。在 Ω⁺ 内，参数变动 cδ 令整个迹线的变化为 O(δ)。因此，若一个格点迹线完整包含于 P，则该 cube 中的所有迹线包含于 P 的固定扩大 `P^+`，其中每个宽度 `w_j^+≤C(w_j+δ)`。因 w_j≥δ，这与 w_j 常数可比，并保持宽度排序。

应用上一节全部框估计及 disjoint 参数 cubes 的体积，

\[
 \#\{M_i\subset P\}\,c\delta^3
 \le \mu(\Omega^+(P^+))
 \le C\delta^{-1/2} w_1w_2w_3.
\]

故对所有 frames、affine centers 和 `δ≤w₁≤w₂≤w₃≤1`，

\[
 \boxed{\#\{M_i\subset P\}
 \le C_{\rm cap}\delta^{-1/2}
       (w_1w_2w_3/\delta^3).}
 \tag{3.2}
\]

此常数与 δ 及 P 无关。P^+ 偶尔宽于 1 只改变固定常数；连续引理本来允许固定 C₀ 范围。

令每个 index 的权重为

\[
 \omega_i=C_{\rm cap}^{-1}\delta^{1/2}.
 \tag{3.3}
\]

对 cell 宽 a_j，取 physical w_j=δ a_j。式 (3.2) 立刻给

\[
 \sum_{M_i\subset P}\omega_i
 \le a_1a_2a_3.
 \tag{3.4}
\]

这正是 WP4 的 A=1 cap，且对其要求的**所有**框成立。无需随机 thinning、概率失败事件、按框重选子族或按框改变权重。

若“有界 chart”被固定写为单位空间盒，可对所有空间坐标施一个固定 scalar 缩放和平移，把该族放进盒内；(3.2) 及 (3.4) 只改变固定 C_cap，所有 D 指数不变。

## 4. 阴影与加权访问量：WP4 矛盾

对每条迹线使用全部 time bins，`J_i={0,…,D−1}`。在各 time-bin center 记录 Mᵢ 所在空间 δ-cell。令 E 为全部记录的四维 δ-cells；若约定把完整迹线相交的所有 cells 均纳入 E，以下上界也完全相同。

全部迹线在 `\mathcal Q=0` 上，且

\[
 x(t)=s+pt\ge 9/10.
\]

因此在有界区域内 hypersurface 可以写为有统一 Lipschitz 界的图

\[
 z=(1-ty)/x.
\]

每个 `(t,x,y)` 的 δ-grid cube 上，该图只跨 O(1) 个 z-cells；一共只有 O(δ^{-3}) 个前三坐标 cubes，所以

\[
 \#E\le C\delta^{-3}=CD^3.
 \tag{4.1}
\]

另一方面，由 (3.1)、(3.3)，

\[
 \sum_i\omega_i\#J_i
 \ge c\delta^{1/2}\delta^{-3}\delta^{-1}
 =c\delta^{-7/2}=cD^{7/2}.
 \tag{4.2}
\]

WP4 若对某 ε<1/2 成立，(3.4)、(4.1)、(4.2) 将推出

\[
 cD^{7/2}\le C_\varepsilon D^{3+\varepsilon},
\]

对任意大 D 不可能。由于每条轨道阴影密度为 1，反例同时击中所有允许的 η，包含任何“先选 ε，再取很小 η”的量词。

## 5. 为什么完整未加权族不能声称 A=1

作为全框 upper 的独立一致性检查，令

\[
 s=1+\sigma,\quad |\sigma|,|p|\le c\sqrt\delta,
 \quad q=-p+r,\quad |r|\le c\delta.
\]

沿整个 t∈[0,1]，直接展开有

\[
 x-z=O(\sqrt\delta),\qquad
 x+z-2=O(\delta),\qquad y=O(\delta).
 \tag{5.1}
\]

因此一个宽度 `(Cδ,Cδ,C√δ)` 的固定正交空间框含有参数质量约 δ² 的完整线。相应 δ-grid 中已有约 δ^{-1} 条线，例如取 q=−p、独立的 σ,p 网格值；而未加权 A=1 cap 只允许 O(δ^{-1/2})。所以完整族的 clustering loss 至少 δ^{-1/2}，与 (3.2) 的 upper 同阶。

此处只用于防止误引完整族更强的 cap；第 2–3 节已经独立证明 upper，不依赖这个特定坏框。

## 6. 结论边界与下一步接口

本结果否定的是本轮候选 WP4：**仅有所有 fulltime 正交空间框的加权 cap，不能在四维时空推出 D^ε 级的密集阴影访问估计。** 原三维时空输入不能以相同假设直接加一维。

这不反驳任何 Kakeya dimension 定理。该线族的完整 spacetime 方向为 `(1,p,−pq,q)`，只占三维可见斜率空间中的二维 algebraic surface `u_y+u_xu_z=0`；它不提供所有方向的线段。已经核验 cap 的权重也没有改变方向缺失这一事实。

要把四维时空 plank 输入作为五维 Kakeya 初始化，必须增加真正排除该 quadric 聚集的条件，例如某个合适的 polynomial non-concentration 假设，并验证它能由实际源 prior、全部阴影及权重推出。单纯把 orthogonal plank cap 改写成等价的 convex-box cap 不会排除 (3.2)–(4.2) 的族。

本轮不提出未经核验的新正向 WP4′，不把已知近反例称为重大中间结果。可复用的具体工作是：QCAP 的自包含 all-frame/all-center 上界、它的加权离散化，以及完整阴影量词下对 WP4 的严格否定。
