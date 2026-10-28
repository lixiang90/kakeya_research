# 格点误差、圆问题与辅助 PDE：真正的应用接口

2026-10-29，R0120，ant_lattice_method。只编辑本分工稿；这是 source / method audit，不恢复旧 Goal、不声称经典数论问题已解决。本页不施工 root 的 translated-ball Parseval 方差或 torus Schrödinger 转移；那些计算及其独审另存。

## 1. 原稿中可以确实调用的输出

依据固定 OpenAI 59 页稿的 §§10–12 及本仓库辅助 PDE 读解，实际有以下区别。

* §10 Theorem10.1：欧氏 Bochner–Riesz 算子在
  \(\alpha>\max\{0,n|1/p-1/2|-1/2\}\) 时一致 \(L^p\) 有界。\(p\ge2\) 时还给相应 maximal 估计。严格阶数留下 Sobolev 损失空间，不含所有无损端点。
* §11 Theorem11.1：Stein square function 在 \(2\le p<\infty\)、\(\alpha>\max\{1/2,n(1/2-1/p)\}\) 时有界。
* §12 Corollary12.1：**已经明确包含抛物面与 Schrödinger 演化**，不能再把“从波到抛物面”的连续桥列成尚未证明。令 \(d\) 为 Schrödinger 空间维数，\(p_c=2(d+1)/d\)，紧支频率球上的初值满足临界时空 \(L^{p_c}\) 对数界，输入是初值的 \(L^{p_c}\) 范数。

这些是 Fourier / 谱求和和指数和平均的实用工具。最接近算术的输出包括：Riesz 权重的格点计数生成函数、环壳频率和的平均、连续/离散曲率相位的 superlevel-set 或 mixed-moment 问题。它们的范数、观察域、权重和原点取值费用必须另算。

原稿是欧氏符号 \(|\xi|\) 的定理。球和固定正定二次型可经线性变化联系；任意光滑凸体的支持函数/对偶范数是另一种 1-homogeneous 符号，不能仅因都有曲率就免费调用本定理。变系数/退化曲率域也不在这一免费范围。

## 2. Gauss circle：值得关注，但本次没有得到新点态指数

写平方半径变量

\[
E(X)=\#\{m\in\mathbb Z^2:|m|^2\le X\}-\pi X.
\]

经典目标是 \(E(X)\ll_\varepsilon X^{1/4+\varepsilon}\)；用半径 \(R\) 写则是 \(E(R^2)\ll R^{1/2+\varepsilon}\)。两个指数必须区分。

Poisson / Bessel 变换使误差对应有径向权重的振荡格点和，因此新的 shell、square function、局部光滑和 restriction 输入在结构上相关。但“控制时空或参数平均”并不直接给固定中心、固定半径的最大值。取径向/平移平均常能杀掉交叉项；经典原点计数恰需要控制这些交叉项、近同长度频率、以及有理聚焦。

作为一个直接的代入警示：格点计数的 torus 生成对象在初始时刻是 Dirac comb，而不是统一有界的 \(L^p\) 数据。将单位质量 Dirac 用宽 \(\epsilon\) 的 bump 逼近时，\(1<p<\infty\) 的输入范数按 \(\epsilon^{-n(1-1/p)}\) 发散。故一个连续 \(L^p\) 算子结论不能通过令 \(\epsilon\to0\) 自动给其原点核值的统一误差界；还需算术抵消或有效 point-evaluation / maximal 参数预算。这是接口费用，不是所有可能应用的不可能定理。

另外，\(2+1\) 维 wave 的 sharp local-smoothing **幂指数范围**此前已有 Guth–Wang–Zhang 的 cone square-function 证明，见 [1909.10693](https://arxiv.org/abs/1909.10693)。本次全维结果在更高维取得的新范围，不能不经计算就声称改进平面圆问题的幂指数；精细对数改善或不同高阶矩仍可单独核算。

## 3. 一个早已存在的平均基线，不能误报为新应用

[Iosevich–Sawyer–Seeger, math/0205127v1](https://arxiv.org/abs/math/0205127v1)，作者版 [disc.pdf](https://people.math.wisc.edu/~aseeger/papers/disc.pdf)，18 页。实际读引言、Thms1.1/1.2.1/1.2.2 与 §4 的平均估计框架，不认证全部证明。

该文用相对误差
\(\Delta_\Omega(t)=[N_\Omega(t)-t^d|\Omega|]/[t^d|\Omega|]\)。对平面光滑、处处非零曲率的凸体，Thm1.2.1 已给

\[
\left(\frac1h\int_R^{R+h}|\Delta_\Omega(t)|^2dt\right)^{1/2}
 \lesssim_\Omega R^{-3/2},\qquad \log R\le h\le R,
\]

即未归一误差的 radius-RMS 为 \(O_\Omega(R^{1/2})\)；更短区间还有相应 \((\log R/h)^{1/2}\) 费用。这里中心始终固定，平均的是 dilation radius。它与对 torus 平移中心的 Parseval 平均不同，更不能与 pointwise Hardy 猜想混称。

所以任何从新波估计得到的“平均具有平方根量级”都应先与这些旧定理比较。只有短区间长度、高阶矩、例外集大小、低正则域或维数范围有明确改善，才有可讨论的新增算术内容。作者旧引言中的“当时最好”点态指数不用于认证2026前沿。

## 4. 一条已经实际用于圆问题的现代 Fourier 桥

[Li–Yang 2308.14859v2](https://arxiv.org/abs/2308.14859v2) 将 cone small-cap decoupling 作为 Bombieri–Iwaniec first-spacing 输入，并结合 Huxley second-spacing，给圆和除数问题平方半径指数 \(0.3144831759741\ldots\) 的预印本结果。实际读 §1 的 reductions、§3 的 first-spacing 定义及 Prop3.1。这里需要的不是一般连续 restriction 一句话，而是任意有界系数、各向异性盒上的离散和及精细尺度依赖。

更新的 [Cen–Gao–Zhang–Zhang 2610.21730v1](https://arxiv.org/abs/2610.21730v1)，2026-10-15，34 页，在 Thm1.1 声明

\[
|E(X)|\ll_\varepsilon X^{209/670+\varepsilon}.
\]

本页只核声明、§1 reductions 和 §6 Thm6.1 的接口/方法，不独立认证34页全证或绝对最优性。其提交早于新 OpenAI 局部光滑发布，不能写成这次新证明的已完成应用。它是“改进曲率分布估计可进入经典圆问题”的具体现成先例。

**重要版本边界。** [Bourgain–Watt1709.04340v2](https://arxiv.org/abs/1709.04340v2) 已在2023撤回，官方说明相关命题证明有缺口，Theorems1–3失去 theorem 地位。不能引用其 \(517/824\) 半径指数作为当前已证基线，也不能因二手网页仍重复就恢复其地位。本轮不下载该撤回证明作输入。

## 5. CGZZ 的明确 first-spacing 门：同一个 cone 并不代表同一个估计

以下逐项来自 CGZZ §6，保留原记号。令

\[
1\le L<K\le\eta^{-1}\le KL,\quad Z=\eta K^2,
\quad |c_{kl}|\le1,
\]
\[
F_c(x)=\sum_{k\approx K,\ l\approx L}c_{kl}
 e(lx_1+klx_2+l\sqrt{k}\,x_3),
\quad
\mathcal B=[-1,1]^2\times[-(\eta L\sqrt K)^{-1},(\eta L\sqrt K)^{-1}],
\]
\[
\mathcal D(\lambda)=\sup_{|c_{kl}|\le1}
\frac{|\{x\in\mathcal B:|F_c(x)|>\lambda\}|}{|\mathcal B|}.
\]

Thm6.1 的实际输入是

\[
\mathcal D(\lambda)\lesssim_\varepsilon (KL)^\varepsilon
\big[(KL)^3\lambda^{-6}+KL^2(L+Z)\lambda^{-4}\big].
\tag{5.1}
\]

频率归一化为
\((l/L,kl/(KL),l\sqrt{k}/(L\sqrt K))\)，恰满足 \(\xi_1\xi_2=\xi_3^2\)。这是 \(\mathbb R^3\) 的二维 cone；相应归一化物理盒的边长为 \((L,KL,\eta^{-1})\)。源 Cor9.3 的连续 cone extension 在该维度对应 \(2+1\) wave；从 smooth surface density 的 \(L^a\) 输入转到这里的原子频率、任意系数和 amplitude-dependent 两项分布式，需要支付 cap mollification / anisotropic box / integer-spacing 等费用。不能凭几何同名就声源 Cor9.3 已证明或改善(5.1)。

这里有一个可直接检验的 coherent-pressure 例：取全部 \(c_{kl}=1\)，令

\[
|x_1|\le c/L,\quad |x_2|\le c/(KL),\quad
|x_3|\le c/(L\sqrt K)
\]

且 \(c>0\) 足够小。各项相位一致接近0，故 \(|F_c|\gtrsim KL\)。此小盒占 \(\mathcal B\) 的比例为 \(\asymp\eta/(KL^2)\)，因此

\[
\mathcal D(c_0KL)\gtrsim\frac{\eta}{KL^2}.
\tag{5.2}
\]

若把(5.1)误改成只有 pure-sixth 项，则在这个 level 右端仅 \((KL)^{-3}\)（忽略任意小幂），两者的比为 \(\eta K^2L\ge K\)。例如 \(L\asymp K\)、\(\eta=K^{-1}\) 时比为 \(\asymp K^2\)，不能靠任意小 \((KL)^\varepsilon\) 吸收。原 fourth 项中的 \(Z=\eta K^2\) 正好覆盖这类聚焦。这个初等测试只阻止错误删项；不独立重证(5.1)，也不认证经典误差的新指数。

CGZZ 的证明保留 fourth / sixth 两种贡献，借 amplitude-dependent wave envelopes 和整数等式计数，经 distributional double large sieve 与第二 spacing 合并。故最值得尝试的是：新 PDE 是否能给在这里**更强且聚焦兼容**的分布式或不同参数区间，而不是把已有 global cone restriction 重新命名成 first-spacing improvement。

## 6. 辅助 PDE 方法的候选重构及验收门

有限 Fourier 和能产生真正演化。例如
\(u(x,t)=\sum a_m e^{i(m\cdot x-t|m|^2)}\) 解自由 Schrödinger 方程，存在质量守恒流；这只提供起点。原稿的成功还需要 PSD 守恒张量、与符号相容的不变量 \(\Phi\)、rank-one 背景、Dirichlet/cofactor/边界相消和临界能量下界同时成立。给平方和取 Gram 矩阵并不自动支付逐列散度零。

若进一步研究，可把验收门固定为：

1. 对上述 first-spacing 原子和及所有 \(|c_{kl}|\le1\)、区间删选、合法权重，构造能保干涉的正能量；输入预算必须与算术应用所需系数范数相同，不能换成更大的物理 \(L^p\) Dirichlet 核范数后隐去费用。
2. 在指定 \((K,L,\eta,\lambda)\) 范围，证明该能量真正改进(5.1)或其对后续 large sieve 有用的版本；必须通过(5.2)及对角算术计数压力。
3. 将新输入放回 double large sieve、second-spacing 和参数优化，给出严格新的 exponent 或真正更短区间；单独多一个 endpoint / logarithm 不预先叫重大结果。
4. 若目标改为格点高阶矩/例外集，则保留原 center/radius 量词，和 ISS 旧 radius-RMS 或 root 平移方差分别比较；从平均到固定原点的任何 Sobolev/maximal 损失另列。

当前未完成这些门。它们是有明确数学测试的候选，而非“用 MA 解数论”的笼统宣言。原稿 §12 连续 Schrödinger 结论可立即用于适合的 \(L^p\) 数据；向算术 \(\ell^2\)、small-cap 分布及固定半径问题的改进，需要新增结构。

## 7. 供主代理归档的来源与实际读域

* ISS：`https://arxiv.org/pdf/math/0205127v1`；可靠作者版 `https://people.math.wisc.edu/~aseeger/papers/disc.pdf`，18页。本代理实际读官方 HTML 的 Introduction、Thms1.1/1.2.1/1.2.2 与§4框架，作者PDF相应statement文本对照；未全文审证，未校验两PDF字节同一性。建议元数据保留相对误差归一化。
* CGZZ：`https://arxiv.org/pdf/2610.21730v1`，34页；实际读官方HTML §1、§6 Thm6.1及局部分布→spacing的用途。未全文审证。与新OpenAI稿不同作者、不同时间、不同输入机制。
* Li–Yang：`https://arxiv.org/pdf/2308.14859v2`；实际读官方HTML §1及§3 first-spacing 定义/Prop3.1，尚未下载本地PDF、不声期刊peer-review完成。若本轮预算只归档上述两PDF，保留此web-primary阅读条目即可。
* BW撤回：`https://arxiv.org/abs/1709.04340v2`；仅官方withdrawal状态和理由，不能作为仍有效theorem输入。
* 原二维先例 GWZ1909.10693、amplitude-dependent方法 GM2206.01093：本页仅实际读官方摘要/方法范围，未逐证。它们支持机制/历史对照，不作为本页新高级输入认证。

本页核心为 source / model-selection；(5.2)是自含必要压力计算，主代理须独立核其尺度后再援引。未外部同行评审，不认证本文计算新颖、经典猜想已解或穷尽2026文献。
