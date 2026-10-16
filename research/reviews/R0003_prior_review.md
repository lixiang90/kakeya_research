# R0003 独立审查：同一 global prior、系数箱双边界与有限半代数厚化

日期：2026-10-16（Asia/Shanghai）。审查对象：`notes/30_algebraic_geometry/native_quadratic_coupling/R0003_系数先验与有限层模型.md`。审查者：`audit_four_dimensional` 子任务。原文对照为 §6.2，pp.88–89 的 (6.6)、(6.9)，以及 Definition 2.2，p.8。

**结论：下述明确限定的有限预备网格命题通过独立审查。** 同一个未归一化前置 prior 可以同时具有所给参与系数箱双边界、确定性列表，并由全系数 Lebesgue 密度的有限半代数厚化实现。结论不是所有尺度统一估计，也不是完整临界路径或五维 Kakeya 模型认证。

原式 (6.6) 在四维稿为 \(p^{j+d}\pi([V]_p)\)，原稿 \(j=2\)。被审笔记使用 \(j=3\) 的五维拟推广形式。不能把这一区别隐藏在引用中。

## 1. 参数条件与物理系数：通过

逐项核对采用的是物理坐标 \(z=(t,Y)\)，而非局部 \(u=z/h\)：

\[
\beta=S/h^2,\quad\kappa=a/h^3,\quad\rho=a/(Sh),\quad\beta\rho=\kappa.
\]

当 \(\kappa\le1\)、\(\rho\le1\)、初始 \(y\) 有界、\(\theta\in[1,2]\) 时，精确轨道给出

\[
V=(\theta,\theta^2,\theta^3-\rho(y_2-2\theta y_1)),
\]

\[
(x_0,x_1,x_2)=(c,-\kappa y_1^2,\kappa(y_2-2\theta y_1)).
\]

native \(X\) 的二次项由 \(\kappa\)，不是由局部 \(a\)，控制。因而笔记限制 \(a/h^3\le1\) 是真实条件；不能用 R0002 只保证 \(a/h^2\le1\) 的参数范围替代。

观测系数映射 \((y,\theta,c)\mapsto(y,V,x_0,x_1,x_2)\) 的正向 Lipschitz 常数只依赖有界域与 \(\kappa,\rho\le1\)，不依赖巨大 \(\beta\)。逆映射投影到 \((y,V_1,x_0)\)，故一致双 Lipschitz 的陈述正确。这里双 Lipschitz 的对象是观测系数图面，不是对全部原始 \((w_0,W)\) 系数宣称统一 Lipschitz。

## 2. 原式 (6.9) 与完整系数箱列表：通过

给定物理 \((t,Y,X)\) 的 \(p\)-cell 及 \(V\) 的 \(p\)-bin，有

\[
y=Y-tV,\qquad\theta=V_1
\]

到 \(O(p)\) 精度。由 \(\kappa\le1\)，\(x_1,x_2\) 也到 \(O(p)\) 精度；由 \(x_0=X-tx_1-t^2x_2\) 得到 \(x_0\) 的 \(O(p)\) 精度。因此每个系数只对应固定数量的 \(p\)-bins，完整参与 \(B_p\) 的数目为 \(O(1)\)，进而 \(X'\) 的列表也为 \(O(1)\)。

这是真正的确定性列表证明，不依赖按箱重新归一化、隐藏 prior 条件或与时间相关的删除。厚化后需要噪声放大低于 \(p_{\min}\)，见 §5。

## 3. 有限层 Cantor prior 与统一 light-bin core：通过

### 3.1 有限层近似

取固定 \(d\in(0,1)\)、\(\xi=2^{-1/d}<1/2\)，第 \(L\) 层 \(2^L\) 个柱区间的长度为 \(\ell=\xi^L\)，每柱质量为 \(\ell^d\)。把每柱质量均匀铺在该区间上，得到分段常密度概率。

在 \(p\ge\ell\) 时，其区间上界 \(Cp^d\)、支持点中心的球下界 \(cp^d\) 和覆盖数 \(Cp^{-d}\) 均成立，常数只依赖 \(d\)。被审笔记正确指出：球下界不保证每一个非空对齐箱有同样下界；非常短的端片不能忽略，必须用后续删除处理。

若 \(p_{\min}\ge N_0^{-C}\)，可选 \(\ell\) 为更小的固定原始幂，保持 \(L=O(\log N_0)\)。片数、密度高度、区间长度倒数因此均为固定原始多项式。不能把这个结论不加说明地换成统一切线幂。

### 3.2 上界与全部阈值的总预算

先固定有限系数/速度网格，再取 \(\rho\) 足够小并删除 moment-curve 网格边界附近的方向参数。保留后的 velocity bin 只依赖 \(\theta\)。对 \(B_p\)，忽略 \(x_1,x_2\) 的额外约束，独立 \(y\)、\(\theta\)、\(c\) 给出

\[
\nu^0(B_p)\le Cp^{3+d}\pi([V]_p).
\]

对每个 \(y\)-bin 和 \(V\)-bin，\(x_1,x_2\) 仅有 \(O(1)\) 个选项，\(c\) 有 \(O(p^{-d})\) 个箱。对所有初始有质量的箱求和，得到

\[
\sum_{B_p}p^{3+d}\pi([V]_p)\le C.
\]

该预算不要求每个 \(\pi(J)\) 可比于 \(p\)，只用到 \(\sum_J\pi(J)=1\)，所以边界删除造成不规则 bin 权重不影响证明。

### 3.3 一份 prior 上的迭代删除

每次删除当前质量低于 \(\tau_0p^{3+d}\pi(J)\) 的一个正质量箱的全部当前轨道。每个初始箱至多删除一次；对 \(G\) 个网格，累计删除至多 \(CG\tau_0\)。即使其它尺度的删除产生新轻箱，继续同样操作，有限箱数保证停止。

停止后的同一个 \(\nu^\circ\)，未经归一化，满足所有剩余正质量参与箱的

\[
\tau_0p^{3+d}\pi(J)\le\nu^\circ(B_p)\le Cp^{3+d}\pi(J).
\]

因此同-prior 双边界没有循环或逐尺度偷换分母。\(\pi\) 是删除前已经固定的 reference palette，并不宣称它在删除后仍恰等于 \(\nu^\circ\) 的速度边缘分布。原 exact problem 可取概率 prior \(\nu^0\)，把 core 作为 trajectory-level incidence selection；\(\nu^\circ=\nu^0|_{\rm core}\) 则是源稿所需的未归一化前置长线 prior。

删除的是完整轨道，且允许全时 incidence，因此保留轨道仍有完整 unit-time 占据。这一项确实补上了 R0002 只在单一短 block 中有质量的不足；但不自动提供临界路径或所有历史标签。

## 4. aᵈh³ 的质量：通过，但须区分 assignment 与 true packet

全局 \(c\) prior 的宽度是 1。对一个 \(A\) 层 Cantor cylinder 取 \(a=\xi^A\)，质量恰为 \(a^d\)；对初始 \(y\) 取一只 \(h\)-cube，质量可比于 \(h^3\)。独立性给出分组的原始质量 \(a^dh^3\)。

把这些分组作为一个分割，若全局 core 总删除量为 \(\eta\)，加权 Markov 不等式说明损失比例超过 \(\sqrt\eta\) 的分组总原始权重至多 \(\sqrt\eta\)。故确实存在仍保留 \(\asymp a^dh^3\) 质量的分组。普通盒边界的不足整格可用 dyadic rounding 或舍弃 \(O(h)\) 边界层处理，不影响这一存在结论。

**必要限定：分组质量不等于原文 true packet floor。** 若使用任意 \(y\)-cube 中心 \(y_Q\)，不能直接以 \(P_*-c_0\) 声称宽度为 \(a\)：在 \([0,h]\) 上 \(\kappa r(z)\) 的低次部分可大于 \(a\)。

一个单-chart 几何修补是以 \(z_Q=(0,y_Q)\) 为中心，取

\[
P_Q(z,w)=P_*(z,w)-\kappa T_{2,z_Q}r(z)-c_0.
\]

因为 \(r\) 为齐三次式，\(r(z_Q+hu)-T_{2,z_Q}r(z_Q+hu)=h^3r(u)\)，故 \(|P_Q|\le Ca\) 于 \([0,h]\) 的有界 normalized box，隐藏导数恒 1、曲率恒 0，空间宽度为 \(O(h)\)。这给出该分组的一个允许的局部二次 chart。

但是 Markov 质量论证和上述 Taylor chart 都不证明终端 \(n(r)J\) 的 true floor、全 time 的 substantial coverage、原始 \(p_L\) label knowledge 或嵌套系统。它们必须继续作为未核验项，不能把 §5.4 的“packet 质量”登记为这些条件已经成立。

## 5. Full coefficient 半代数厚化：通过

加入独立盒噪声 \(\zeta_2,\zeta_3,\zeta_W\in[-\eta,\eta]\)。从

\[
(y_1,y_2,y_3,\theta,c,\zeta_2,\zeta_3,\zeta_W)
\]

到全部八个轨道系数的映射按 \((y,V_1,w_0,V_2,V_3,W)\) 排列是三角多项式映射，对角 Jacobian 为 1；其逆为逐个解出三个噪声及 \(c=w_0+\beta y_1y_2\)。所以推前并非仅有光滑但非常数的密度：Jacobian 恰为 1，输入分段常密度会成为 full-coefficient coordinates 上的分段常密度。

独立展开 native signal，得到

\[
x_0=c,
\quad x_1=-\kappa y_1^2+\beta y_1\zeta_2+\zeta_W,
\quad x_2=\kappa(y_2-2\theta y_1)+\beta(\theta\zeta_2-\zeta_3),
\]

与被审笔记 (6.1) 一致。\(x_0\) 完全不受噪声影响；其余额外摆动为 \(O((1+\beta)\eta)\)。因此在

\[
(1+\beta)\eta\ll\min(p_{\min},a_2)
\]

下，有限网格列表、参与箱计数与 upper-cap 预算均保留，再重新执行同一个 light-bin core 即得厚化后的统一双边界。

固定 \((t,\theta,\zeta)\) 时，初始 \(y\) 到当前 \(Y\) 的 Jacobian 仍为 1。图面误差直接为

\[
t\zeta_W-\beta t^2\zeta_3+\beta tY_1\zeta_2-\kappa t^3\zeta_2,
\]

在固定有界域上为 \(O((1+\beta)\eta)\)。\(\partial_wP_*=1\)、\(\partial_{ww}P_*=0\) 保持精确；\(X\) 的全部 unit-time 系数保持有界。完整 prior 和 native bounds 的这部分原始条件得到实质核验。

有限层 Cantor 区间、方向边界删除、盒噪声及有限箱 core 都可在原始系数坐标用有限个有界次数多项式不等式表达。当其数量、倒宽和 \(\beta\) 具有固定 \(N_0\) 幂界时，Definition 2.2 的原始复杂度成立。大 \(\beta\) 会迫使 \(\eta\) 更小，但在一个先固定的 exact sequence 内仍可选固定原始幂；本审查没有把它误说成统一切线幂。

## 6. 有限网格的附加参数要求

\(\rho\le1\) 本身不够保证网格 index 与 \(y\) 无关，还必须有

\[
\rho\sum_g(1+\delta_g^{-1})\ll1
\]

及噪声边界余量；这些已在被审笔记 §5.1、§6 单列。其“\(S=h,a=h^{M+1}\)”只是满足 \(\kappa,\rho\le1\) 的例子，不能保证任意先给定极细表的兼容性。要处理这样的表，必须按其实际最小宽度再选择更小 \(\rho\)（例如增大 \(S\)）及 \(\eta\)。

这仍是“先给有限表，再选模型参数”的命题。它不等于一个固定模型对所有无限细网格满足同样的参考 palette 联合上界。

## 7. 可以登记的结论与宏观去向

可以登记：在 \(\kappa=a/h^3\le1\)、明确有限网格及安全余量内，原始全局长线 prior、同-prior 系数箱饱和、确定性列表与 full-coefficient 有限半代数厚化同时兼容。原始分组质量 \(a^dh^3\) 也可保留，不以归一化 packet 概率 1 替代。

不能登记：完整 \(\mathcal C(d)\)、true packet hierarchy、critical horizon/优化、原始 label knowledge、全部尺度 joint domination 或一般全方向 Kakeya。该构造本身仍有多项式方向约束，原始全方向约化能否付得起条件化到这种集合的质量代价，是新的实质问题。

因此本审查支持父任务的宏观转向：下一轮使用原始全方向的 polynomial nonconcentration 及 parent-selection 质量预算作为新输入，而不是继续在同一 \(S_0\)/网格语义上作等价改写。
