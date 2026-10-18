# R0100：三角 Hilbert annular variation 的真实共享 clock 准入

2026-10-19，C。依 R0100 working §1–5 审计。以下区分原文声称的高级定理、本稿逐项核过的定义与初等推导、以及尚未支付的原 Kakeya 应用。没有审完外部 37 页 whole proof；OpenAI 署名不保证正确，未经外部同行评审。本稿不是 n≥5 Kakeya 证明、full source 反例或新维数界。

## 1. 原始来源、版本和实际读域

官方固定仓库 commit 为 `1581d4cbdd69a0faf34b2089614fe2a814316a6a`。目录是 `preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/`，其中 [README](../../literature/primary/R0100_openai_triangular_annular_README.md) 只有题名、Author OpenAI、2026-10-05 和 BibTeX，没有 Lean 或独立证明认证说明。本文题名是 *Annular variation of the triangular Hilbert transform at the symmetric point*；CONTENTS 的检索题名不能取代 PDF 真实定义。

采用的 [原 PDF](../../literature/primary/R0100_openai_triangular_annular_variation_2026_10_05.pdf) 为 37 页、523253 bytes，SHA256 `f5857c58037fa5289f2f9fe1fe4421af11df8d9fa9b2914ba041469f1195ea31`，原 Git blob `b84bc5405b3714f613563e0bb1b5e7f8d1618a77`；这些字节核由 root 统一执行，本稿未重复下载。C 实际读取 README 全文及 PDF 抽取的第 2–6 页、31–32 页：Th1.1–1.2、(1.1)–(1.5)、Lem2.1、§2.1 与 §8 linearization/rank summation。抽取已归 `literature/extracted/R0100_openai_triangular_annular_variation_2026_10_05.txt`。中间 matrix/heat/frequency/rough-kernel 高级 whole proof 未由 C 全部独证，后文使用 Th1.1–1.2 时始终是具名 source claim 下的应用。

## 2. 真实 kernel、abs 顺序和量词

对 complex \(F,G\in L^3(\mathbb R^2)\)，原 (1.1) 定义

\[
B_{\varepsilon,R}(F,G)(x,y)
 =\int_{\varepsilon<|t|<R}F(x+t,y)G(x,y+t)\,\frac{dt}{t},
\qquad 0<\varepsilon<R<\infty.
\]

这是正负 \(t\) 同时出现的 odd kernel。把 \(f_{x,y}(t)=F(x+t,y)G(x,y+t)\)，则同一有限积分等于 \(\int_\varepsilon^R[f_{x,y}(t)-f_{x,y}(-t)]dt/t\)。有限 annulus 的绝对可积性不使它变成正 kernel。

原 \(V_r\) 是先算每个 signed \(B_{t_{j-1},t_j}\)、再取模和 \(\ell^r\)；partition 在每个 output \((x,y)\) 可分别选择，端点不必 dyadic、同一 dyadic 段内数量不限。原 \(S_N\) 是在至多 N 个两两不交的正 radius 区间上取 \(\sum_j|B_{\varepsilon_j,R_j}|\) 的 pointwise supremum。它不是 \(\sum_j\int |f|dt/|t|\)，也不是正向 \(\int_{t>0}fdt/t\)。Lem2.1 给公共 null set、端点连续性与 rational exhaustion，因此这些 supremum 可测。

原 Th1.1 声称 \(r>2\) 时 \(\|V_r\|_{3/2}\le C_r\|F\|_3\|G\|_3\)。Th1.2 声称 \(\|S_N\|_{3/2}\le C\sqrt N\log(2+N)\|F\|_3\|G\|_3\)。这里 N 是 disjoint-annulus 数目，不是管数、点数或自动等于 physical 尺度比。

## 3. 三角坐标和真正合法的 entangled pairwise 用途

原 §2.1 的换元是

\[
x=-a,\qquad y=-b,\qquad t=a+b+c.
\]

其绝对 Jacobian 为 1。若用第三输入 H 配对，令

\[
G_0(a,b)=H(-a,-b),\quad
G_1(b,c)=F(b+c,-b),\quad
G_2(c,a)=G(-a,c+a).
\]

三个二维 pair map 的绝对 determinant 都是 1，故分别保 \(L^3\) norm，且原三重积分成为

\[
\iiint G_0(a,b)G_1(b,c)G_2(c,a)
 \frac{\mathbf1_{\varepsilon<|a+b+c|<R}}{a+b+c}\,da\,db\,dc.
\]

这是一个真实 shared 三变量、pairwise entangled 的用途。没有把它粗拒为普通独立乘积；三因子共享变量，已允许强相关。反向 pair map 也可逆，所以任意 \(L^3\) 三个 pair inputs 都合法。若要用于原几何模型，仍须实际构造这些 pair inputs、控制它们的 norms，并证明 physical clock 对应此同一换元；单有“三点”或“共享 clock”名称不够。

## 4. 用 source claim 可得的实际 signed 质量估计

设每个 output 可测地选择至多 N 个 disjoint radius intervals，并选择 complex \(\beta_j(x,y)\)、\(|\beta_j|\le1\)。由 pointwise domination 与 Hölder，在 Th1.2 source claim 下确有

\[
\left|\int H(x,y)\sum_j\beta_j(x,y)
 B_{\varepsilon_j(x,y),R_j(x,y)}(F,G)(x,y)\,dx\,dy\right|
\le C\sqrt N\log(2+N)\|H\|_3\|F\|_3\|G\|_3.
\]

还可把左侧改为 \(\int|H|\sum_j|B_j|\)。这是 signed annular correlations 的模之和；不要求 annuli 在各 output 一致。由 §3 可直接改写为真实三角 pairwise form 的 bound。C 核过此 Hölder 与坐标推导，不以此声称独立证明 Th1.2。

若后来另行付出 physical annuli 数 \(N\asymp\log(1/\delta)\)，本式只给 \(\sqrt{\log(1/\delta)}\log\log(1/\delta)\) 级的计数费用，而不是自动给 \(\delta^\epsilon\) 正幂增益；还需比较原 lower、全部 norms、原正量到 signed 量的桥。使用 Th1.1 可去掉 signed variation 的 N 依赖，但同一正量桥仍未出现。

## 5. 平滑共同 core 对免费 positive 版本的严格反攻

取固定 \(0\le\psi\in C_c^\infty(\mathbb R)\)，在 \([-1,1]\) 恒 1，令 \(F(x,y)=G(x,y)=\psi(x)\psi(y)\)。取 \(E=[-1/4,1/4]^2\)，以及 N 个 disjoint annuli

\[
(\varepsilon_j,R_j)=(2^{-j-3},2^{-j-2}),\quad j=1,\ldots,N.
\]

它们均在 radius≤1/8，且对每个 \((x,y)\in E\)、每个所列 annulus 的正负 t，有 \(F(x+t,y)G(x,y+t)=1\)。因此所列每个 signed \(B_j(x,y)=0\)，但正向量

\[
P_j(x,y)=\int_{\varepsilon_j}^{R_j}F(x+t,y)G(x,y+t)\,dt/t=\log2
\]

在 E 上恒等。故 \(\|\sum_{j=1}^NP_j\|_{3/2}\ge N\log2\,|E|^{2/3}\)，而 \(\|F\|_3\|G\|_3\) 与 N 无关。免费把 Th1.2 换成 positive-forward 版本会迫 \(N\lesssim\sqrt N\log(2+N)\)，对大 N 不可能。positive \(r\)-variation 同样至少为 \(N^{1/r}\log2\)，不可能有与 N 无关的 Th1.1 类 bound。

若把绝对值放到积分内、用双边 \(dt/|t|\)，每个 annulus 则为 \(2\log2\)。取固定非负非零 \(H\in C_c^\infty(E^\circ)\) 配对，positive scalar mass 是 \(N\log2\int H\)，所列 signed scalar annuli 全零。这是固定 smooth inputs 上任意 N 的连续积分证明，不是有限样本数值。只声称这些**所列** \(B_j\) 在 core 为零；full \(S_N\) 仍可选别的远 annuli，未声称 full \(S_N\) 在 E 为零。

## 6. 为什么 output-only 线性化没有正 clock mask 权限

原 §2.1 和 §8 允许 annulus 列表及 \(\beta_j\) 随 output \((a,b)\) 变；它们在对 c 积分时必须按同一 output 固定。核

\[
K_{a,b}(t)=\sum_j\beta_j(a,b)\mathbf1_{\varepsilon_j(a,b)<|t|<R_j(a,b)}/t
\]

对 t 仍为 odd。即使 radius 选择非常细，它也在同一 radius 的 ±t 上使用相同 coefficient。故 \(\beta_j(a,b)\) 不等于任意 \(\beta(a,b,c)\)，不能取为 \(\operatorname{sgn}(a+b+c)\) 而宣称原 theorem 已包含 positive kernel。core 上同一 output 的每个所列 signed integral 为零，任何此类 \(\beta_j\) 组合仍零。

原正 clock mask \(\mathbf1_{t>0}\) 给核 \(\mathbf1_{\varepsilon<t<R}/t\)，不在这个 odd-annular kernel 类中。更一般的 shading \(\chi(a,b,c)\) 可令 \(\chi(t)\ne\chi(-t)\)，所以把它直接乘进原核需新 theorem 或额外桥。若某个具体 shading 恰好可吸收进三个合法 pair inputs 且 norms 受控，仍可应用 §4；本稿不否认这种个别情形，也未证明所有原来源都不可能有 cancellation。

## 7. 原 selected g 的实际定位与未支付接口

C 实际读回 WZ sticky 抽取 §20.3 的 (164)–(165) 与 §21.1 的 (172)–(173)：前者由同一 L-tuples 构造 dense selected graph \(G\subset Y_{z''}(q)\times Z(q)^2\times\Phi_q^2\)，后者由原 Lem19.1 得 dense graph \(G\subset A\times B^2\times\Phi_q^2\)，small image 只在这些 selected edges 上断言。它们没有把 graph indicator 写为三组 pair factors。

另实际读 [R76 主稿](../40_multiscale/sticky_matrix/R0076_two_end_native_product_full_clock_reduction.md) §1–9：在其明确的 det-large 分支，真实 \(g(y,y',u)=M_0^{-1}\#\{T\in H^*: \text{native endpoints}=(y,y'),u\in S_T\}\) 满足 \(0\le g\le1\)，相对完整 \(Y_t\times Y_s\times Z\) 有 \(L^{-1}\) density，保每根已选 T 的全部原 \(S_T\)；但原全 T 质量仅为 \(L^{-1}\delta^2\) 级，不能改成 \(K^{-C}\) 全局比例。第三 clock 权可与两端相关，不能自动用三角 pair product 取代。

相关性本身并不排除 THT，§3 本来允许 entanglement。严格缺口是：尚无保持这些原 positive edges、原 lower 和原全部预算的表示/控制，使目标等于或可从下由 §4 的 signed annular correlations 获得。原 incidence domination \(\mu_{act}\le K\nu\otimes dt\) 也不使这个 lower 自动成立；它可给正量上界，但 signed kernel 没有正序 domination。不能以“g 任意相关”直接断言完整原 source 已被反驳。

## 8. 真正有权的 positive 上界及其费用

Lem2.1 的 (2.1) 只用平移、Hölder、Minkowski，就给

\[
\left\|\int_{\varepsilon<|t|<R}
 |F(x+t,y)G(x,y+t)|\,dt/|t|\right\|_{3/2}
\le 2\log(R/\varepsilon)\|F\|_3\|G\|_3.
\]

正向版本常数为 \(\log(R/\varepsilon)\)。§5 core 说明这种随 log 尺度增长不能在此一般正模型中免费去掉。对 \(0\le g\le1\)，正 forward 积分可由无 g 的正积分支配，但所得就是该 log 费用；不能先丢 g 再把 abs-kernel 偷换回 signed kernel取得 cancellation。若 clock 离奇点固定距离、尺度比有固定上界，此正 bound 本来只有常数费，新的 signed theorem 不自动提供额外 \(\delta\) 幂。physical clock 到 \(a+b+c\) 的参数/权变换、隐藏参数的 Fubini norms 和误差，仍须逐项付出。

## 9. Restriction、shading 密度和双向排重责任

原选管或选 marks 后，非负 incidence 仍可受旧 prior upper 支配，但其 retained lower 必须以原总质量为分母计；从平均 density 不能白得每条原管同等 density，逐管删选后要重计管数、clock 与方向权。THT output-dependent 选择只解决其自身 output annuli 可测线性化，不证明原 shading 或 N/I/marks 闭包，也不证明每个删选后仍有可见的 odd imbalance。

若存在一个旧估计对全部原 positive 选择统一有效，删选后再次调用可能已经给同一正幂结论，必须先检查双向蕴含与原费用。当前这里没有得到新的 positive 全称上界，所以不能因 annular-variation 新题名给旧 joint-mass 公设换名，也不能把未付表示当新条件定理的实质突破。合法 root/B 原量词审计仍需保原 full CW、filled X、全部 \(\Phi\)/coherence、误差与尺度。

## 10. 严格结论、反例范围和停止条件

已核的实质是：真实 signed 双边定义；output-dependent radius/coefficients 的权限；Jacobian1、norm-preserving 三角 pair coordinates；在具名 Th1.2 下的实际 scalar signed 应用；固定 smooth core 对免费 positive-forward/abs-inside 两种替换的严格反攻。所用 smooth inputs 或抽象 g 接口不携原小 footprint、full CW、full directions 和全部 WZ 数据，**不是完整 source 反例**，更不是 Kakeya 反例。

当前直接 THT→原 positive joint mass 的桥严格未支付，故不能宣得 ordinary/HRZ、完整 sticky 剩余 branch 的正幂 saving。停止本直接桥的 r、partition、mask、frequency 或另加 regularity 参数续轮；重开须有保持原全部数据和质量的真实 cancellation/representation 机制。外部 Th1.1–1.2 whole proof 仍是未全独证的 source claim；本稿初等核验与应用范围可供独立审查，formal review 另由 root 授权，不预写 reviewed、major、novelty 或 Goal 完成。
