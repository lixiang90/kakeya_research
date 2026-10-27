# p-adic 类比：已知结果、模型和可用输入

2026-10-27，R0119 文献分工稿。问题是 OpenAI 欧氏局部光滑辅助 PDE 方法的可移植性；本页先排除已解决目标，并固定真正可研究的模型。这里只核对具名文献及其直接归一化推论，没有重新证明文献、声称新结果或恢复旧欧氏 Goal。

## 1. 已知结论先分层

| 对象 | 本次核到的结论 | 条件与证据边界 |
| --- | --- | --- |
| 有限域 \(\mathbb F_q^n\) | Kakeya 集和强 maximal 已有多项式方法解答 | 一个有限域不包含 \(k\to\infty\) 的赋值尺度；不能把它当成 \(\mathbb Z/p^k\mathbb Z\) |
| \(\mathbb Q_p^n\) 有界全方向单位段集合 | Hausdorff、Minkowski 维数均为 \(n\) | Arsovski arXiv v3 Thm 1；集合不须先假定紧，采用 max-product metric |
| \(\mathbb Q_p^n\) Kakeya maximal | 通常任意 \(\delta^{-\epsilon}\) 损失的猜想已有解答；下文从 Dhar Thm 1.6 明确推出 \(O_{p,n}(k+1)\) 强 \(L^n\) 界 | \(\delta=p^{-k}\)，固定 \(p,n\)；不是从 Arsovski v3 的 fragmented-set 式直接读出同一对数幂 |
| 有限扩域 \(K/\mathbb Q_p\) 的 Kakeya 集 | 满环境 Hausdorff、Minkowski 维数 | Arsovski Remark 2；“维数 \(n\)”须固定下述绝对值归一化。这里不把 \(\mathbb Q_p\) 的强 \(L^n\) 公式自动宣称为所有扩域的同常数公式 |
| \(\mathbb F_q((t))^n\) | 所有 compact \(c\)-Kakeya 集 Hausdorff 维数 \(n\)，并有 polylog-scale maximal 界 | Salvatore v3 Thms 1、4、5；任何 prime power \(q\)，本项不排除特征 2 |
| 曲面 restriction / extension | 存在成熟的明确模型、Stein–Tomas 型定理及 decoupling 结果 | 需指定曲面、指数及 \(p\)/尺度一致性；不能由 Kakeya 已解反推整个 restriction 猜想 |

Arsovski 的发表版是 *J. Amer. Math. Soc.* **37** (2024), 69–80，DOI [10.1090/jams/1021](https://doi.org/10.1090/jams/1021)。[作者目录](https://bodanarsovski.github.io/)明确说明部分 arXiv 稿与发表版有显著差别，并称发表论文还解决 p-adic Kakeya maximal。本次实际逐式读取的是 **2021-11-01 的 arXiv v3，7 页**；尚未读取 12 页发表版全文，因此强 maximal 的定量依据另取已存的 Dhar 定理，不把两个版本混引。

## 2. 统一度量、线段与方向

在 \(\mathbb Q_p^n\) 取 \(|p|_p=p^{-1}\)、\(\|x\|_p=\max_j|x_j|_p\)、\(|\mathbb Z_p^n|=1\)。单位线段和其厚化为

\[
 a+\mathbb Z_p v,\qquad
 T_k(a,v)=a+\mathbb Z_p v+p^k\mathbb Z_p^n,
 \qquad \|v\|_p=1.
\]

其 Haar 体积为 \(p^{-k(n-1)}\)。方向可用 primitive 向量模 \(\mathbb Z_p^\times\) 的射影类。尺度 \(k\) 时只需有限方向 \(P^{n-1}(\mathbb Z/p^k\mathbb Z)\)；均匀 primitive 向量下推正是均匀射影方向测度，因为每类的单位倍代表数相等。

一般局部域 \(K\) 的整数环为 \(\mathcal O\)，uniformizer 为 \(\pi\)，残余域大小为 \(Q\)。本页说 \(K^n\) 的维数 \(n\) 时取 **modulus 归一化** \(|\pi|_K=Q^{-1}\)、\(|\mathcal O^n|=1\)。若改用扩张通常 \(|p|_p\) 的绝对值，对于 \(d=[K:\mathbb Q_p]\)，两个距离互为 \(d\) 次幂，满环境 Hausdorff 维数改记为 \(dn\)。满维这一性质相同，数字依归一化改变；不能把 Qp 向量空间维数和 K 向量空间维数混合。

## 3. Arsovski v3 实际给了什么

[Arsovski v3](https://arxiv.org/abs/2108.03750v3) Thm 1 对每个 prime \(p\) 和 \(n\ge1\)，证明每个有界 \(\mathbb Q_p^n\) Kakeya 集满维。Thm 5（PDF 4）先处理 fragmented 集：在至少 \(\delta\) 测度的 \(x\in\mathbb Z_p^n\) 上，集合包含 \(b_x+\Lambda_x x\)，其中 \(|\Lambda_x|\ge\epsilon\)。令 \(q=p^k\)，其覆盖数下界印为

\[
 N(E,p^{-k})\ge {\epsilon\delta q/(pnk)+n-1\choose n}.
\]

上项在稿中没有 floor，按其广义二项式用法读取；特别有适当常数下的 \(N\gtrsim_{p,n}(\epsilon\delta)^n p^{kn}/k^n\)。之后借多尺度覆盖分组得到 Hausdorff，而不只同尺度 Minkowski 结论。这里方向比例为 \(\delta^n\)；仅此式不能被引用为带同一 \(k^{-n}\) 的精确强 maximal 定理。

方法是离散赋值环上的多项式方法：借 \(p^k\)-次单位根编码环上的线，并用赋值版 Schwartz–Zippel 控制。正特征的相应替代见下文；这些证明并未使用新的四元数辅助 PDE。

## 4. 一个可明确读取的强 maximal 输入

[Dhar 2209.11443v1](https://arxiv.org/abs/2209.11443v1) Thm 1.6（PDF 3）设 \(R=\mathbb Z/p^k\mathbb Z\)，非负整数函数 \(F:R^n\to\mathbb N\)，

\[
 F^*(u)=\sup_a\sum_{s\in R}F(a+su),\quad
 \sum_{x\in R^n}F(x)^n\ge [2L(F)]^{-n}
     \mathbb E_{u\in P^{n-1}(R)}F^*(u)^n,
\]
\[
 L(F)=\left\lceil\log_p\max_uF^*(u)+\log_p n\right\rceil.
\]

这里空间端是 **计数**，方向端是 **概率**；常数含函数高度，不能未处理高度就宣称是任意实函数的统一算子范数。该文也给 \(p>n\) 的改进式，本页不使用。

以下只是此定理的直接归一化推论，尚未另作项目新命题登记。置 \(q=p^k\)，空间改用概率 \(q^{-n}\sum\)，\(M_k f=q^{-1}f^*\)。对 \(f\ge0\) 先令 \(\|f\|_{L^n}=1\)，故 \(\|f\|_\infty\le q\)；取正整数 \(F=\lceil qf\rceil+1\)。于是

\[
 f\le F/q,\quad \|F/q\|_{L^n}\le1+2/q\le2,
 \quad\max F^*\le q^3+2q\le2q^3.
\]

定理给出 \(\|M_k F\|_{L^n(u)}\le2L(F)\|F\|_{L^n(x)}\)，从而恢复齐次性后有

\[
 \boxed{\ \|M_k f\|_{L^n(u)}
 \le4\bigl(3k+\lceil\log_p(2n)\rceil\bigr)\|f\|_{L^n(x)}.\ }
\]

\(f=0\) 单独平凡处理；任意复函数取模。每个 \(T_k\) 是尺度 \(p^{-k}\) 球的并，故对 \(f\in L^n(\mathbb Z_p^n)\)，管平均只依赖球上条件期望 \(\mathbb E_k|f|\)，而条件期望是 \(L^n\) 压缩。由此得到同一连续强界。对整个 \(\mathbb Q_p^n\)，每条单位管留在一个单位球陪集内；分割成 \(f_i\) 后用 \((\sup_i M_k f_i)^n\le\sum_i(M_k f_i)^n\)，得到全空间界。因此它包含每个 \(\epsilon>0\) 的 \(C_{p,n,\epsilon}\delta^{-\epsilon}\) 形式。

这里不主张最优 log 幂，也不把这段初等推论称为新的 p-adic Kakeya 解答。另一已存 [Dhar 2110.14889v3](https://arxiv.org/abs/2110.14889v3) 研究一般 \(\mathbb Z/N\mathbb Z\) 的 set / \((m,\epsilon)\)-Kakeya 界；它与本项使用的 2209.11443 强 maximal 文章不同。

## 5. 正特征不能省略：Salvatore

[Salvatore 2202.11344v3](https://arxiv.org/abs/2202.11344v3)，2022-09-02，13 页；发表 *Mathematika* **69** (2023), 1–16。取 \(K=\mathbb F_q((t))\)、\(A=\mathbb F_q[[t]]\)、\(|t|=q^{-1}\)。Thm 1 的 \(c\)-Kakeya 集按定义为 **compact**：每个 \(w\in A^n\) 都有 \(J_w\subset A\)、\(|J_w|\ge c>0\) 及 \(b_w\)，使 \(b_w+J_ww\subset E\)。结论是 \(\dim_H E=n\)。有限正特征局部域仍属 \(\mathbb F_{q'}((\pi))\) 这一类。

该稿 Thm 5（PDF 5）给每个尺度 \(\delta=q^{-k}\) 的分布估计，等价的连续写法为

\[
 |\{w:K_\delta\phi(w)\ge\lambda\}|
  \lesssim_{n,q} k^{n+1}\lambda^{-n}\|\phi\|_{L^n(A^n)}^n.
\]

\(K_\delta\) 取 \(b+Aw+(t^kA)^n\) 的归一化平均上确界，方向为 primitive \(w\)。root 已视觉核对 PDF 5、8：Thm 4 及其 layer-cake identity 的左边 norm 均漏印了 \(n\) 次幂，右边则是 \(n\) 次齐次式；不能照抄为算子不等式。由上面弱型及其 PDF 8 的分层论证，齐次正确的强型后果为

\[
 \|K_\delta\phi\|_{L^n}^n
  \lesssim_{n,q}k^{n+2}\|\phi\|_{L^n}^n,
 \qquad \|K_\delta\|_{L^n\to L^n}\lesssim_{n,q}k^{(n+2)/n}.
\]

常数独立于 \(k\)，可依赖固定 \(n,q\)；本文不声称和 Qp 同一最优 polylog 幂。其关键正特征处理是以 Lubin–Tate 全分歧扩张替代 cyclotomic 编码；特征 \(p\) 中没有可直接沿用的非平凡 \(p^k\)-次单位根。

## 6. 真正曲面模型及一个已知 restriction 定理

固定 conductor 为 \(\mathbb Z_p\) 的加性 character \(\psi:\mathbb Q_p\to\mathbb C\)，考虑

\[
 E_\varphi g(x,t)=\int_{\mathbb Z_p^{n-1}}
   g(\xi)\psi\bigl(x\cdot\xi+t\varphi(\xi)\bigr)d\xi,
 \qquad (x,t)\in\mathbb Q_p^{n-1}\times\mathbb Q_p.
\]

例如奇素数下 \(\varphi(\xi)=\sum\xi_j^2\) 有可用的非退化二次 Hessian。这里时间和多项式相位都在 Qp，输出仍是复数。它与实时间 \(e^{-it\|D\|_p^\alpha}\) 是两个算子。metric sphere \(\{\|\xi\|_p=1\}\) 是开闭、正 Haar 测度的壳，不能直接代替实欧氏余维一曲率球面。

[Hickman–Wright 1801.03176v2](https://arxiv.org/abs/1801.03176v2)，2018-05-28，54 页，§5.5 Prop 5.5（PDF 26–27）给严格对应：整数系数 polynomial graph \(\Sigma=\Gamma(\mathbb Z_p^d)\subset\mathbb Z_p^n\)，\(\mu=\Gamma_*d\xi\)，其连续 restriction

\[
 \|\widehat f|_\Sigma\|_{L^s(\mu)}\le C\|f\|_{L^r(\mathbb Q_p^n)}
\]

等价于 **所有** \(\alpha\ge0\) 上具有 **同一 \(C\)** 的有限环估计

\[
 \left({1\over|\Sigma_\alpha|}\sum_{\xi\in\Sigma_\alpha}
 |\widehat F(\xi)|^s\right)^{1/s}
 \le C\|F\|_{\ell^r((\mathbb Z/p^\alpha\mathbb Z)^n)}.
\]

此处空间为计数测度，有限 Fourier 变换为未归一化求和；曲面为概率测度。**带 \(p^{\alpha\epsilon}\) 的环估计不能冒充此 uniform 结论。** §5.6 把对应原则推广到一般非阿基米德局部域及 \(\mathcal O/\pi^\alpha\mathcal O\)，这不是从欧氏定理免费传递到 Qp。

同文 Thm 6.5（PDF 37）对抛物面、所有奇素数 \(p\) 及所有 \(\alpha\ge1\)，给独立于二者的 \(C_r\)：上式 \(s=2\) 成立当且仅当

\[
 1\le r\le{2(n+1)\over n+3}.
\]

对偶给连续 \(E_\varphi:L^2\to L^{2(n+1)/(n-1)}\)（及较大输出指数）的 Stein–Tomas 片段。Thm 6.4 对一般奇数 \(N\) 的对应版本则允许 \(N^\epsilon\)，二者不可混用。这是具体已知范围，未覆盖通常讨论的所有输入输出指数。文献中的方向是适当 restriction 可推出 Kakeya；本页不逆用这一蕴含，也不据 2018 论文单独宣告截至 2026 年一切曲面的最新开放状态。

## 7. 一个已有的正面移植实例与下一步边界

[Johnsrude 2409.09163v2](https://arxiv.org/abs/2409.09163v2)（2025-09-24，34 页）Thm 1.1 是非阿基米德抛物线 small-cap decoupling，方法为 high-low / wave-envelope。对 \(\operatorname{char}K\ne2\)，在合法赋值尺度 \(R,R^{1/2}\)、\(R\ge P_K^{32}\) 上，代入其 \(r=6,q=2,\beta=1/2\) 得

\[
 \|f\|_6^6\le {4Q^{-3}P_K^{10}\over(\log P_K)^{11}}
 (\log R)^{29}\left(\sum_\theta\|f_\theta\|_6^2\right)^3.
\]

\(\widehat f\) 支持在截断抛物线的 \(R^{-1}\) 邻域，\(\theta\) 是 \(R^{-1/2}\times R^{-1}\) caps；残余域大小为 \(Q\)，奇残余特征时 \(P_K=Q\)，\(K/\mathbb Q_2\) degree \(d\) 时 \(P_K=2^d\)。因此“欧氏曲率分析有部分机制能移植”有具体先例；它没有使用 OpenAI 2026 辅助 PDE，也没有解决所有维数、所有曲面的 restriction。

继续研究时应把问题固定为具体 \(\varphi\)、具体指数和尺度常数，比较已有 finite-ring、decoupling 输入，再找新 PDE 能补付的精确 identity/energy。实时间径向模型的反例测试及新稿的逐步骤可移植性见本目录其他分工稿。本页到此停止，不凭相似术语补上仍缺的分析定理。

## 实际读域与核查记录

- Arsovski v3：7 页全文的定理及主论证定位，重点 PDF 2–4；发表版只核出版信息和作者版本说明，未读其 maximal 证明。
- Dhar 2209.11443v1：定义 1.5、Thm 1.6、整数高度常数及用途；本页直接推论写全计数/概率因子。2110.14889v3 仅对照引言与定理范围。
- Salvatore v3：定义、Thms 1、3–5、PDF 8 分布到强型、§4–5 方法说明；root 另视觉核对 PDF 5、8 漏印的 norm 次幂，强型按齐次推导辨认。
- Hickman–Wright v2：§5.2、§5.5–5.6、Thms 6.4–6.5；未声称独立检查全 54 页。
- Johnsrude v2：官方 HTML 的 Thms 1.1–1.2、§1.2 和排除特征 2 的说明；上述式是已有定理的特例。尚未阅读 UCLA 2025 thesis 全文，故不据摘要补充更高维完整 theorem。

本页是 source audit / model selection，非新数学结果；精确公式的文献来源、直接推论和未核范围已分别标明。
