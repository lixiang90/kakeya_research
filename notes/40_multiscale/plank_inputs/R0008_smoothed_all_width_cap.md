# R0008：同一平滑先验的全部宽度 cap 与短块外推

日期：2026-10-17。作者：`lifting_obstructions`。状态：独立证明完成，供内部交叉审查；本笔记不作 horizon 或 cap-class 资格声明。

## 0. 精确结论与本轮边界

将 PLK-001 的 quadric 参数 δ-grid 归一为概率，每个 index 的质量约 δ³，再在**全部六个可见 affine coefficients** `(b,u)` 上加独立均匀噪声 `[-δ,δ]`。对得到的同一可见轨道概率 ν_vis，证明：

\[
 \boxed{\nu_{\rm vis}(\hbox{whole-time }P)
 \le C\delta^{-1/2}\prod_{j=1}^3 w_j}
 \tag{0.1}
\]

对任意正交 frame、任意 affine center、任意**正的 physical half-widths** wⱼ 成立；不要求 wⱼ≥δ，也不要求 wⱼ≤1。

对任意长度 0<q≤1 的短时间块 I，若一个固定 frame 的空间框有半宽 wⱼ，则

\[
 \boxed{\nu_{\rm vis}(\hbox{轨道在 }I\hbox{ 上完整落入该框})
 \le C\delta^{-1/2}q^{-3}\prod_j w_j.}
 \tag{0.2}
\]

对一般 invertible chart matrix D、J=|detD|，以及 `sup_I|D^{-1}(Y-y_c)|≤K`，推得

\[
 \boxed{\nu_{\rm vis}(\hbox{whole-block spatial fit})
 \le C K^3\delta^{-1/2}q^{-3}J.}
 \tag{0.3}
\]

常数独立于 δ、q、frame、center、widths、D 和 K。可以再与概率的平凡上界 1 取 min。所有式子均使用同一原始概率 prior，不能无代价替换成条件化后的 G-prior。

## 1. 统一模型与离散输入

令 δ 为足够小的 dyadic 数，参数盒与迹线沿用 PLK-001：

\[
 \Omega=[1,2]\times[-1/10,1/10]^2,
\]
\[
 b(s,p,q)=(s,-sq-p/s,1/s),\qquad
 u(s,p,q)=(p,-pq,q).
 \tag{1.1}
\]

取 Ω 中固定的 δ-grid，记 index 集合为 Γδ，数量 Nδ≈δ⁻³。每个 index 的概率为

\[
 \pi_i=1/N_\delta\asymp\delta^3.
 \tag{1.2}
\]

条件于 index i，取独立

\[
 \xi_b,\xi_u\sim U[-\delta,\delta]^3,
\]

六个坐标也全部独立，定义

\[
 Y_i(t)=b_i+\xi_b+t(u_i+\xi_u),\qquad 0\le t\le1.
 \tag{1.3}
\]

这正是本轮统一的 noise 半宽常数 ρ=1。记 `(b_i+ξ_b,u_i+ξ_u)` 的混合概率律为 ν_vis。它是完整六系数空间上有限个 axis-aligned boxes 的常密度混合，具有 full-dimensional、有限半代数、原始多项式有限性。这里不把 R0007 的反例权 `δ^{1/2}/C_cap` 当作概率 index 权；本轮实际权是 (1.2)。

使用 R0007 已独立证明的全部 frame/center count 输入：对 `δ≤W₁≤W₂≤W₃≤C₀`，

\[
 \#\{i:b_i+tu_i\subset P_W\}
 \le C(C_0)\delta^{-1/2}
          (W_1W_2W_3/\delta^3).
 \tag{1.4}
\]

其证明为连续参数估计 `μ(P_W)≤CW₁min(W₂,W₃²)`，加不相交参数 δ-cubes 的固定扩大；完整记录见 [R0007 全框证明](../../50_counterexamples/R0007_weighted_plank_obstructions.md) §§2–3。它对任意 affine center 和任意正交 frame 都成立，没有排除相切框。

## 2. 宽于支撑范围的轴：可以裁剪，常数不依赖 widths

原离散族及平滑族的 b、u 都落在一个固定有界盒内，故存在绝对 R，使全部轨道在 [0,1] 上有 |Y(t)|≤R。

对任何 fulltime plank P，若它不含支撑中的轨道，则所需 cap 为零。否则固定一条支撑轨道 Y*⊂P。任意另一条支撑轨道 Y⊂P 逐轴满足

\[
 |n_j\cdot(Y-Y^*)|\le2w_j,
 \qquad |n_j\cdot(Y-Y^*)|\le2R.
\]

因此支撑中落于 P 的轨道全部落于 affine center Y*、同一 frame、半宽

\[
 v_j=\min(2w_j,2R)
 \tag{2.1}
\]

的新 plank。排序不变，且 `∏vⱼ≤8∏wⱼ`。新中心确为 affine 轨道，仍在允许的中心类中。

由此可先将任意超大宽度裁到固定 C₀，再使用 (1.4)；若原宽度均≥δ，裁后仍≥δ（δ 足够小）。所以离散输入可以统一写成

\[
 \sum_{i:\,b_i+tu_i\subset P_W}\pi_i
 \le C\delta^{-1/2}\prod_j W_j,
 \qquad W_j\ge\delta,
 \tag{2.2}
\]

**不再有最大宽度的上界**，且 C 与这些宽度无关。此裁剪也可直接作用于平滑族；后文直接使用 (2.2)。

## 3. 旋转细框的小概率因子

固定一个 index i，再固定 u-noise ξᵤ。fulltime inclusion 特别要求 t=0 时

\[
 |n_j\cdot(b_i+\xi_b-c(0))|\le w_j,
 \quad j=1,2,3.
 \tag{3.1}
\]

ξ_b 的密度为 `(2δ)^{-3}`，支撑于半径 √3δ 的球。旋转到 frame nⱼ 后，密度仍是同一个常数，支撑仍在该球内。因此 (3.1) 的概率至多

\[
 C\delta^{-3}\prod_j\min(w_j,\delta)
 =C\prod_j\min(1,w_j/\delta).
 \tag{3.2}
\]

这里没有假设旋转后的三个坐标仍相互独立；只使用三维 joint density 与“球交正交框”的体积上界。因此任意 frame 都被覆盖。

该上界对 i、ξᵤ 和 center 均统一。由于 ξ_b 与 ξᵤ 独立，它在固定 ξᵤ 后有效，随后可以对原来的 ξᵤ 律积分。没有条件化成另一份噪声 prior。

## 4. 全部正宽度 cap：扩大与小概率逐轴抵消

若某组噪声使 `b_i+ξ_b+t(u_i+ξ_u)` 全时间落于 P，则对所有 t∈[0,1]，

\[
 |n_j\cdot(\xi_b+t\xi_u)|\le2\sqrt3\delta.
\]

所以其原始格点迹线 `b_i+tu_i` 必须落于**同一中心、同一 frame** 的扩大 plank P⁺，半宽

\[
 W_j=w_j+2\sqrt3\delta\asymp\max(w_j,\delta).
 \tag{4.1}
\]

这个原格点 eligibility 条件对全部可能噪声统一成立，不是在命中后重选格点子族或重新归一化。

将 (3.2) 对 eligible 格点求和，再用同一 index 律 (2.2)，

\[
 \begin{aligned}
 \nu_{\rm vis}(P)
 &\le C\left[\prod_j\min(1,w_j/\delta)\right]
       \sum_{i:\,b_i+tu_i\subset P^+}\pi_i\\
 &\le C\delta^{-1/2}
       \prod_j\left[W_j\min(1,w_j/\delta)\right]\\
 &\le C\delta^{-1/2}\prod_j w_j.
 \end{aligned}
 \tag{4.2}
\]

最后一步逐轴成立：wⱼ≥δ 时 Wⱼ≤Cwⱼ；wⱼ<δ 时 Wⱼ≤Cδ，小概率因子 wⱼ/δ 恰抵消 δ 扩大。

这证明 (0.1)，包括仅一个、两个或三个轴小于 δ 的所有情形；宽度可以任意接近零。若某轴恰为零，完整六维 prior 给包含概率零，也可由正宽度单调取极限得到，但本轮命题只需正 widths。

## 5. 短时间块的 affine 外推

令 `I=[τ,τ+q]⊂[0,1]`，0<q≤1。固定 frame nⱼ、affine center c(t)，设一条轨道在 I 上逐轴满足

\[
 |n_j\cdot(Y(t)-c(t))|\le w_j.
\]

每个 `f_j(t)=n_j·(Y(t)−c(t))` 都是 affine。以两个端点插值，对任意 t∈[0,1] 有

\[
 f_j(t)=\left(1-\frac{t-\tau}{q}\right)f_j(\tau)
        +\frac{t-\tau}{q}f_j(\tau+q),
\]

从而

\[
 \sup_{[0,1]}|f_j|\le3w_j/q.
 \tag{5.1}
\]

因此短块 fit 的轨道集合包含于一个 whole-unit-time plank 的轨道集合，后者中心仍为原 affine c、frame 仍固定，半宽为 `3wⱼ/q`。应用对全部正宽度成立的 (0.1)，得到

\[
 \nu_{\rm vis}(P_I)
 \le C\delta^{-1/2}q^{-3}\prod_jw_j.
 \tag{5.2}
\]

即使 `wⱼ/q<δ` 或 `wⱼ/q≫1` 也不需要另分情况：极窄轴已由第 4 节处理，极宽轴已由第 2 节裁剪处理。没有把仅在短块成立的空间约束错用成原宽度的全时间约束。

### 一般 chart matrix 与 determinant

对 invertible D 作 SVD `D=UΣV^T`，奇异值 σⱼ>0。若

\[
 \sup_{t\in I}|D^{-1}(Y(t)-y_c(t))|\le K,
 \tag{5.3}
\]

则在 U 的左奇异 frame 中有半宽 `wⱼ≤C Kσⱼ` 的外包正交框；固定维度的 norm 选择只改变 C。于是

\[
 \prod_jw_j\le CK^3\prod_j\sigma_j=CK^3J.
\]

将其代入 (5.2) 即证 (0.3)。这里保留**原来的** J=|detD|，没有先逐轴放大再把放大后的 determinant 当成原 J。

源 chart 定义的 `||D||≤Kq` 与上述结果相容，但本上界并不依赖它：若轴上界缺失或某个 σⱼ 过大，全部宽度 cap 仍可用。需要保留的是固定 invertible D、固定 frame、affine center，以及 assignments 的 whole-block fit；若只在被选中的零散 incidences 上成立，(5.1) 没有依据。

## 6. 同一 prior、restriction 与条件化成本

(0.1)–(0.3) 的 ν_vis 始终是 (1.2)–(1.3) 的原始概率。它们对任意未归一化 submeasure `\widetildeν≤ν_vis` 仍成立；若 `\widetildeν≤D_0ν_vis`，右侧须乘 D₀。

特别地，对任意轨道事件 G，条件概率 `ν_vis(·|G)` 的 cap 至少要写成

\[
 \nu_{\rm vis}(P\mid G)
 \le\frac{C\delta^{-1/2}\prod_jw_j}{\nu_{\rm vis}(G)},
 \tag{6.1}
\]

此式指whole-unit-time正交框；一般短块chart右侧仍须保留CK³δ^-1/2q^-3|detD|/ν_vis(G)。不能把这一分母删除。父 chart 的重归一化、world 的条件律、另一份先验 G，都必须先与本 ν_vis 建立明确的支配关系。

若完整轨道 prior 另外独立带 hidden 参数，而当前 incidence selection 只是其 product-prior×dt 的一个事件，则选中 measure 仍被原 prior×dt 支配。后续要以 (0.3) 计某个 chart 的原始分配质量时，必须使用它的**完整 whole-block spatial assignment**；不能先在 selected incidences 上归一化再套几何 cap。

本笔记没有证明 hidden density profile、angular cap、任意二次 test 的 hidden sublevel 估计、true floor 或 horizon 下界。它仅交付本轮所需的同-prior 全宽度几何 cap 与短块外推接口。
