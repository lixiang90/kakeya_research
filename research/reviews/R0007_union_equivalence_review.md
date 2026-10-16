# R0007：WP、加权阴影并集与平均密度输入的独立复核

日期：2026-10-17（Asia/Shanghai）。审查人：`audit_four_dimensional`。被审文件：`notes/40_multiscale/plank_inputs/R0007_weighted_union_equivalence.md`。只核对条件互推、可测 shading、权重/重复索引与几何转换；未独立重证 WP4 反例的全部框上界，其审查另见本轮 quadric review。本文件不把本项目的条件工具或既有反例当作新颖性/重大结果。

结论：**在文中固定 bounded-chart、固定维度、固定长度/半径比较的范围内，P\(_n\)、W\(_n\)、U\(_n\) 的调整容差互推通过独立审查。** 不能将其读成相同 \(\eta\) 的逐式等价；不能把固定时间窗转换免费用于 \(\delta\)-依赖的小窗口。下面补清各量词与这一范围条件。

## 1. Plank 与 convex cap 的两个方向均正确

若整个 graph trace 落在物理半宽 \(r_j=a_j\delta\ge\delta\) 的 fulltime plank，其 chart tube 落在半宽 \(r_j+\delta\le2r_j\) 的凸 moving box。该 box 体积 \(\lesssim\prod r_j\)，除以 \(|T_i|=v_m\delta^m\) 即得 fulltime-plank cap。只包含 shade 不足以做这一步，原文已明确。

反方向取含完整 tubes 的 convex body、与 bounded 环境球相交、用 outer John ellipsoid 包围。时间跨度至少1；最大水平截面体积为 ellipsoid 总体积除以该跨度再乘维数常数。切片中心仿射、主轴固定，所以最大 slice 的正交外接矩形沿这些中心移动就是允许的 fulltime plank。tube 的空间 \(\delta\)-球保证每根宽度下限；固定图界保证上限只差固定倍。原 cap 给 weighted clustering \(\lesssim A\)，没有缺失一个 \(\delta\) 因子。

超出固定倍宽度范围时，对 bounded endpoints 作有限分组的总乘积成本是固定图常数。这里每次测试的是全轨道；非轴对齐凸体没有被替换成仅若干时刻的测试。

## 2. W 到 P 的标记球转换正确

在每个 time-bin center 放半径 \(c_R\delta\) 的球，取 \(c_R\) 足够小，可同时保证在 chart tube 内、离时间端面足够远、同一 index 的不同球不交。因此

\[
|Y_i|\asymp\#J_i\delta^n,
\quad |\cup Y_i|\lesssim\delta^n\#E.
\]

选择 \(\eta_P<\eta_W\) 的固定余量，吸收球体积常数，直接约去 \(\delta^n\) 得 P。需要的是每 index 长 marks；没有用平均 occupation 冒充这个假设。

## 3. P 到任意 measurable W 的 heavy-cell 步骤正确

令 \(Q\) heavy 当 \(|U\cap Q|\ge\delta^{n+\kappa}\)。一个 bounded-speed tube 总共只碰 \(O_R(\delta^{-1})\) 个 cubes，所以对**每个** index，light cells 内的 shade 至多

\[
O_R(\delta^{-1})\delta^{n+\kappa}
=O_R(\delta^\kappa)|T_i|.
\]

这使用 \(Y_i\subset U\)，与 index 权重及其 shade 在截面内是否均匀无关。\(\eta_W\le\kappa/2\) 保证小 \(\delta\) 时每条至少保留其自身 shade 的一半，而不是只保留平均一半。

每 time bin 的 tube volume 为 \(O_R(\delta^n)\)，故 \(\#J_i\ge c_R\delta^{-1+\eta_W}\)。取 \(\eta_W\le\eta_P/2\)，固定前因子在充分小 \(\delta\) 时可吸收，P 的逐 index 门槛成立。若 shade 在一个 time bin 仅零测度地相交，标记它至多增加计数；无损于该下界或下面的覆盖上界。

由某一 shade 点到其 trace 的 bin-center point 的距离为 \(O_R(\delta)\)，所有被访问 cells 都在 heavy cells 的固定邻域，所以

\[
\delta^n\#E\lesssim\delta^n\#\{Q\text{ heavy}\}
\le\delta^{-\kappa}|U|.
\]

同时 \(|Y_i|\le2|Y_i^H|\lesssim\#J_i\delta^n\)。应用 P 的损失 \(\varepsilon_P=\varepsilon/3\) 后，最终损失为 \(\varepsilon_P+\kappa<\varepsilon\)。这正是任意 measurable shading 所需的一次 mesh-density 成本；没有把 \(|N_\delta(U)|\) 免费等同于 \(|U|\)。

剩余 bounded \(\delta\) 范围也可用环境 convex cap 给 \(\sum\omega_i\lesssim A\delta^{-(n-1)}\)，再逐点控制 weighted multiplicity，放大常数处理。互推量词正确。

## 4. U 到 W 的权重抽样与 average density 没有偷换

取 \(v_i=\omega_i/A\)。以凸体 \(T_i\) 测试给 \(v_i\le1\)，环境球给 \(S=\sum v_i\lesssim\delta^{-(n-1)}\)。有限 box-net、Chernoff 与 union bound 得样本 convex clustering \(O(\log(1/\delta))\)；大 \(S\) 时样本数 \(\gtrsim S\)。完全重复 tubes 的样本重数也由同一 convex cap 控制，故每条只留一项后仍有 \(\gtrsim S/\log(1/\delta)\) 个不同 tubes。

关键是此方向的 W 假设本来是**每 index** \(|Y_i|\ge\delta^{\eta_W}|T_i|\)。抽样、对重复 tube 仅保留任意一条原 index 连同原 shade，都保留这个下界。因此抽样后的 **U 的平均密度** 自动不小于逐 index 下界，不需要额外证明 weighted shade 总量在抽样中集中。另一方面，目标 weighted 总量可直接用 \(\sum\omega_i|Y_i|\le C A S\delta^{n-1}\) 上界。两个逻辑不能混为“抽样保持所有 weighted shade 质量”。

小 \(S\lesssim\log(1/\delta)\) 时逐点重数 \(\le AS\) 处理，避免不成立的样本下尾。所有 constants 与原始 indices 数量、重复数和权重极差无关。

若 U 对标准 Euclidean tubes 陈述，§5 先将每个 chart tube **扩大**为共同固定长度的 Euclidean tube，原 shade 不变。包含扩大 tube 的 convex body 也包含原 tube，所以 cap 的推理方向正确；tube volumes 相差固定倍，shade density 只损失固定倍。随后共同 isotropic scaling 到长度1不改变 convex-clustering 比值。此方向没有非法使用“缩短后 cap 自动继承”。

## 5. W 到平均密度 U 的两次 \(\eta\) 成本正确

若平均 density 为 \(\ge\delta^{\eta_U}\)，删去 density \(<\delta^{\eta_U}/2\) 的 tubes，失去的 shade 至多原总量一半。不是要求剩下 tube 数达到原数一半。剩下每个 shade 的密度满足 W 门槛，只需选 \(\eta_U<\eta_W\) 并以固定余量吸收 \(1/2\)。

令 \(A=\delta^{-\eta_U}\)，对 W 取目标损失 \(\varepsilon/4\)，得到

\[
|U|\gtrsim\delta^{\varepsilon/4+\eta_U}
\sum_{\rm retained}|Y_i|
\gtrsim\delta^{\varepsilon/4+2\eta_U}\sum_{\rm original}|T_i|.
\]

一个 \(\eta_U\) 来自 convex clustering，另一个来自平均 shade 下界，原稿均保留。\(\eta_U\le\varepsilon/8\) 留出固定指数余量，所以前因子在小 \(\delta\) 时吸收，得到 U 的目标损失 \(\varepsilon\)。量词顺序是先 W 对 \(\varepsilon/4\) 给 \(\eta_W\)，再选 \(\eta_U\)，没有循环依赖。

## 6. 缩到 graph time window 时的额外范围条件

对 arbitrary standard Euclidean tubes 如需先选一个共同 graph time window，不能单凭 \(T_i^{\rm short}\subset T_i^{\rm long}\) 就宣称短 tubes 的 convex cap 保留：测试短 tubes 所用的 convex body 不必包含长 tubes。

固定长度 \(\ell\ge c_R>0\) 的窗口可以严格转换。若 \(K\) 包含这些完整 short tubes，取 outer John ellipsoid \(\mathcal E\supset K\)，\(|\mathcal E|\lesssim|K|\)。原 full trace 的点可由两个 short endpoints 以系数 \(O(\ell^{-1})\) 仿射外推，故 full tubes 被 \(C_R\ell^{-1}\) 倍 ellipsoid 包含；固定 \(\delta\) thickness 同样被吸收，因为 \(\mathcal E\) 含一个 \(c_R\delta\)-ball。于是 full convex cap 给

\[
\sum_{i:T_i^{\rm short}\subset K}
\omega_i|T_i^{\rm short}|
\le C_R\ell^{1-n}A|K|.
\]

当 \(\ell\) 固定这是图常数；若 \(\ell\) 随 \(\delta\) 缩小则会有真实 power 成本，不能称作 fixed comparison。标准管到共同 chart 的 finite partition 还要保留一个有足够 shade 的固定比例组，并重新吸收 density 常数。被审文本已把结论限于 fixed bounded-chart/fixed length comparisons，因此不与此限制冲突；这里仅补清使用时必须核对的方向。

本次未把任意 \(\delta\)-依赖的小窗转换登记为已获 uniform theorem，也未把几个分离窗口的平均 shade 当作每条同一窗口的密度。

## 7. 结论与独立性范围

互推的几何、measurable-shading 处理、正权/重复 indices 抽样以及平均密度门槛的调整均通过。真正缺失的高维输入仍是 U\(_4\)/W\(_4\)/WP4 的无方向几何陈述，它们的互推不能使一个已被 quadric 反例否定的输入成立。

本审查没有独立核验 quadric 参数族的 allplank cap，也没有把四维 Hausdorff 主结论升级为无方向 shaded-union 定理；这两件事与上述纯条件互推分开记录。
