# R0012：任意光滑空间仿射、保留原时钟的 codimension-one lift 障碍

> **R0050范围更正（2026-10-17）：** 下文保留开轮/历史论述。对目标 `w+F(t)y`，在同一个参数点沿同一条lift直线取第一变分，可构造同codimension和方向rank的真正全时affine lift。因此一般smooth与affine的**存在性等价**，旧文“空间affine为实质限制/一般nonlinear未排除/需逼原π affine”的判断不再成立；原π本身仍可真正非线性。完整更正见 [R50主证明](R0050_variational_equivalence_and_full_smooth_lift_classification.md)，当前登记为 `results/reviewed/LIFT-005_full_smooth_variational_classification.md`。不新增ID或重大性声明，换clock/selector/Θ依赖w等边界保留。

日期：2026-10-17。任务 N5-CURVE-LIFT-01。作者：audit_four_dimensional。状态：完整自包含必要条件证明，已由lifting_obstructions交叉独审，见research/reviews/R0012_affine_classification_review.md，另有root独立核验。本文解决指定 lifting 类的可行性，不使用任何未证 Kakeya 输入，不声称新维数界、重大结果或文献新颖性。

## 1. 精确结论与一手定义的范围

Nadjimzadah, *Lifting curved Kakeya sets to linear Kakeya sets*, arXiv:2609.06299v1，Definition 2.1（PDF p.6）允许任意光滑 submersion；其线斜率 \(\Theta(y,\rho)\) 独立于 anchor 参数 \(w\)，且整个 ruling 参数域上的所有线都投影到同一条 \(\gamma_{y,w}\)。本文另限定 submersion 为保留原时钟、空间仿射：

\[
 \pi_t(z)=T(t)z+c(t).
\]

不预先限制 \(T,c,a,\Theta\) 的函数形式；特别没有假定 \(T=[I,tU]\)，也没有假定 \(a,\Theta\) 对参数线性。

**主结论。** 对 \(B=\operatorname{diag}(1,2)\)，不存在本轮 spec 中的 \((1,0)\)-lift：不可能有任意光滑

\[
 T:I\to\operatorname{Mat}_{2\times3}(\mathbb R),\quad
 c:I\to\mathbb R^2,\quad
 a(y,w,\rho),\ \Theta(y,\rho)\in\mathbb R^3
\]

在有内点的参数域及含0的开时间区间上满足

\[
 T(t)[a(y,w,\rho)+t\Theta(y,\rho)]+c(t)
 =w+(tI_2+t^2B)y,
 \tag{1.1}
\]

同时 \(D_{(y,\rho)}\Theta\) 有 rank3。事实上下面证明更强的自然必要条件：若 \(B\ne0\)，且某个 interior point 上 \(\partial_\rho\Theta\ne0\)，则 \(\operatorname{rank}B\le1\)。

## 2. 一般的 codimension-one 必要条件

为使矩阵来源清楚，直接在 \(m=n-1\ge2\) 写同一证明。\(y,w\in\mathbb R^m\)，\(\rho\in\mathbb R\)，lifted spatial variable 属于 \(\mathbb R^{m+1}\)。\(T(t)\) 为 \(m\times(m+1)\) 矩阵，目标为

\[
 T(t)[a(y,w,\rho)+t\Theta(y,\rho)]+c(t)
 =w+(tI_m+t^2B)y.
 \tag{2.1}
\]

所有 identity 对一个 open product neighborhood 的全部参数和所有 \(t\in I\) 成立。对一般有内点参数域，可先限制到这样一个 neighborhood。只需 \(a,\Theta\) 对参数可微；原文的 smooth 假设充分。

**定理。** 若 (2.1) 成立且 \(\Theta\) 独立于 \(w\)，则对 \(\operatorname{rank}B\ge2\)，必有 \(\partial_\rho\Theta=0\) 在整个参数域内点成立。因而 \(D_{(y,\rho)}\Theta\) 的 rank 至多为 \(m\)，不能实现 \((1,0)\)-lift 所需的 \(m+1\)。

### 2.1 Anchor 微分给同一个、与时间无关的右逆

反设某个参数点 \(\zeta_*=(y_*,w_*,\rho_*)\) 上 \(\partial_\rho\Theta\ne0\)。所有参数微分在该固定点取值。对 (2.1) 作 \(w\) 微分，因为 \(\Theta\) 独立于 \(w\)，得到

\[
 T(t)A=I_m\quad\text{对全部 }t\in I,
 \qquad A:=D_w a(\zeta_*)\in\mathbb R^{(m+1)\times m}.
 \tag{2.2}
\]

这一个固定矩阵 \(A\) 对所有时间都有效，且 rank 为 \(m\)。选择 \(h\notin\operatorname{im}A\)，令 \(S=[A\ h]\in GL_{m+1}(\mathbb R)\)。仅作 lifted spatial coordinates 的**常矩阵**变化

\[
 z=S\widehat z,\quad \widehat a=S^{-1}a,\quad
 \widehat\Theta=S^{-1}\Theta,\quad \widehat T(t)=T(t)S.
\]

于是

\[
 \widehat T(t)=[I_m\ \beta(t)],\qquad \beta(t)\in\mathbb R^m.
 \tag{2.3}
\]

这不是 ansatz：它是 (2.2) 强迫的 constant-coordinate normal form。它不改变原 \(t,y,w\)、目标 \(B\)、\(\Theta\) 的 \(w\)-独立性或任何 direction rank。以下略去 hats。

### 2.2 Coherent ruling 给核内 affine-time 向量

按 \(\mathbb R^{m+1}=\mathbb R^m\times\mathbb R\) 分块，记

\[
 r=\partial_\rho a(\zeta_*)=(r_h,r_v),\qquad
 s=\partial_\rho\Theta(\zeta_*)=(s_h,s_v),
 \quad s\ne0.
\]

目标与 \(\rho\) 无关，因此

\[
 r_h+t s_h+\beta(t)(r_v+t s_v)=0
 \quad(t\in I).
 \tag{2.4}
\]

同时记 \(y\) 微分的矩阵 blocks 为

\[
 D_y a(\zeta_*)=
 \begin{pmatrix}U_h\\U_v\end{pmatrix},\qquad
 D_y\Theta(\zeta_*)=
 \begin{pmatrix}V_h\\V_v\end{pmatrix},
\]

其中 \(U_h,V_h\) 为 \(m\times m\)，\(U_v,V_v\) 为 \(1\times m\)。由 (2.1)，

\[
 U_h+tV_h+\beta(t)(U_v+tV_v)=tI_m+t^2B.
 \tag{2.5}
\]

这里 \(r,s,U,V\) 都只是任意光滑参数函数在一个点的一阶导数；没有把原 \(a,\Theta\) 替换成全局线性函数。

### 2.3 不除以可能为零的分母，先消去 beta

令 scalar polynomial \(d(t)=r_v+t s_v\)。将 (2.5) 乘 \(d(t)\)，再由 (2.4) 代换 \(d(t)\beta(t)=-(r_h+t s_h)\)，得到

\[
 d(t)(U_h+tV_h)
 -(r_h+t s_h)(U_v+tV_v)
 =d(t)(tI_m+t^2B).
 \tag{2.6}
\]

左边次数至多2，右边 \(t^3\) 系数为 \(s_vB\)。等式在开区间上成立，故它是 polynomial identity，给

\[
 s_vB=0.
 \tag{2.7}
\]

若 \(B\ne0\)，由于 \(s_v\) 是 scalar，必有 \(s_v=0\)。若再有 \(r_v=0\)，(2.4) 变成 \(r_h+t s_h=0\) 对所有 \(t\) 成立，从而 \(s_h=0\)，矛盾于 \(s\ne0\)。所以

\[
 s_v=0,\qquad r_v\ne0.
 \tag{2.8}
\]

直到此处才可以合法除以非零**常数** \(r_v\)，于是

\[
 \beta(t)=-r_h/r_v-t s_h/r_v=\beta_0+t\beta_1.
 \tag{2.9}
\]

该消元没有假定 \(d(t)\) 预先非零；允许 ruling 的参数微分在个别时刻消失，也覆盖 \(r=0\) 等潜在退化情况。不曾对光滑 \(T\) 取形式幂级数或假设它解析。

### 2.4 二次系数必须是 rank-one 外积

把 (2.9) 代回 (2.5)，比较 \(t^2\) 系数：

\[
 \boxed{B=\beta_1 V_v.}
 \tag{2.10}
\]

右边为 \(m\times1\) 与 \(1\times m\) 的外积，rank 至多1。故当 \(\operatorname{rank}B\ge2\) 时矛盾，定理得证。

## 3. 应用于本轮 B=diag(1,2)

\(B=\operatorname{diag}(1,2)\) 的 rank 为2。若 \(D_{(y,\rho)}\Theta\) 为 rank3，则其 \(\rho\) 列 \(\partial_\rho\Theta\) 必非零；第2节给出矛盾。因此在本轮允许的**整个任意光滑空间仿射、保留原时钟的类**中都没有候选 lift。

实际上，只要 direction map 在某一个 interior point 有 rank3，就足以在该点运行上述证明。否定结论不是单独检查几个标准公式，也不依赖 numerical rank sample。

一手文献 Proposition 2.5(i)（PDF p.9，(4.1)–(4.9)）对该 \(B\) 构造的是 \((2,0)\)-lift，使用 \(\pi(x,z,t)=(x+tUz,t)\)。本文排除的是在更大的任意 smooth 空间仿射类中将这个任务降为 \((1,0)\)-lift；没有反驳文献的现有构造或其 rank 公式。

## 4. 必须保留的边界与停止点

- **Theta 独立于 w 是实质条件。** 否则 (2.2) 变成 \(T(t)[D_wa+tD_w\Theta]=I\)，共同 constant 右逆不再由本证明得到。
- **整个 ruling 域的 coherence 是实质条件。** 只有选定某个 \(\rho(y,w)\) 的线投影正确，不能对 \(\rho\) 微分得到 (2.4)。
- **空间仿射是实质条件。** 一般 nonlinear \(\pi_t\) 的空间微分依赖沿线的 base point，不再是本证明同一个 \(T(t)\)。本文不排除一般光滑 submersion 的 \((1,0)\)-lift。
- **保留原时钟是实质条件。** 标量 \(B=bI\) 经 \(s=t+bt^2\) 可在小时间区间把曲线变为直线；这是文献 Remark 1.5 的时间换元现象。即使 \(bI\) 在本限定类中也受 rank≥2 障碍，它仍可由上述不同 clock 的等价获得低维结果，两者不矛盾。
- \(c(t)\) 未被假设为零：它在参数微分中消失。任意 nonlinear 参数依赖的 \(a,\Theta\) 均已被覆盖；此处只使用一阶参数微分。

本轮主任务已严格解决所指定的窄类，应按 spec 停止其细节分类。没有声称 rank-one \(B\) 的完整分类、任意 codimension 的最优性，或时间重参数／一般 nonlinear 空间映射下的最小 lift 维数。也没有由 forward curved-to-linear lifting 倒推五维 Kakeya；长期 Goal 仍未达到。
