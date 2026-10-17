# R0029：KT 有限种子、方向稀疏化与高维前沿审计

2026-10-17，子任务 B。按恢复协议读取 GOAL、STATE、ROADMAP、registry、AGENTS、R29 spec、R28 next，以及既有 SRC-001、DIR-003。本轮只审计有限种子到 Katz–Tao 递推的真实接口；不把 R7/R9 的既有条件输入重新登记为新结果。以下独立有限论证和原文量词审查仍未经外部同行评审。

**结论。** KT 的第二输入确实要求任意固定 ambient、实方向参数和平均 saturated shading，不能由四维集合的 Hausdorff 维数句子直接替代。若接受 SRC-001/DIR-003 所依完整四维证明，则 A/root 的实际投影与稀疏族估计给出所需输入，KT6.2 的六维条件链是 17/4。本稿另给不依赖“免费单调性”的保遮蔽质量方向稀疏化。已核一手基线为六维 7−2√2；本轮有限检索不认证 2026 年全部前沿或新颖性。

## 1. 固定命题、源条件与停止条件

固定 ambient 整数 M≥4、空间界 R、实 n≥4，以及目标损失 ε>0。令 N=δ⁻¹，T 为 bounded box 中单位尺度 discretized lines，方向 δ-separated。所需显式有限输入为：存在 η>0、C、N₀，使 N≥N₀ 且

\[
\#T\ge N^{n-1-\eta},\qquad
\#\{T:\angle(v_T,u)\le\theta\}
 \le N^\eta(N\theta)^{n-1},\quad N^{-1}\le\theta\le1,
\]

对所有方向中心成立，且原 shading 满足

\[
\sum_{T\in T}\#Y(T)\ge N^{1-\eta}\#T,
\qquad \#Y(T)\le C_MN,
\]

则其 union cover/cardinality 至少 C⁻¹N^{4−ε}。所有 marks 都属于其原 line；只允许有限常数的 grid/cell 转换。本稿称此为显式强有限种子，不声称它与各种只给单一固定损失的命题等价。

源责任分开：SRC-001 是 R7 对完整 OAI4 proof 的有限后半段读出；DIR-003 是 R9 从该输入得到的加权任意条数放大。二者不是由集合 dim_H=4 单句逻辑推出。本稿不独立重证完整四维证明，故所有使用它们的高维结果保留该条件。若没有这类 proof-level 有限输入，稀疏化、投影和 KT 记号都不能修补缺失。

## 2. KT Definitions 5.1、5.2、6.1 的精确责任

原件为 Katz–Tao, *New bounds on Kakeya problems*, arXiv math/0102135v1，2001-02-16，后发表于 J. Anal. Math. 87 (2002), 231–263。库内 PDF 24 页，§6 为 PDF19–24。一手链接：[原文与版本](https://arxiv.org/abs/math/0102135v1)。

1. **离散线并非只取一条精确格点直线。** Def5.1 把线定义为 bounded lattice 中距一条近竖直直线 CN⁻¹ 内的点，单线 cardinality ∼N。方向只有 O(N⁻¹) 精度。有限方向 charts、网格常数和近线误差需要支付；固定 M、R 时这些只是固定常数。
2. **shading 是逐 index 的子集。** Def5.2 的 density λ 是逐线 #Y(T)≈λN；但是 saturated shading 的定义只要求总 mass≈N#T。因此调用 Def6.1 不能未经删选就声称每条原线都有 N^{1−o(1)} 个 marks。heavy-line 选择是必要的一步。
3. **符号含任意小幂。** §5 固定一个可任意小选取的 ε，≲ 容许 C_εN^{Cε}；≈ 为双向。它不是“只差 log”或固定常数。一个单一固定 η 的有限结论并不自动等于全部 K(n,d)。安全使用方式是 ∀目标损失 ∃输入容差，先选目标与 source tolerances，再取 N 大。
4. **ambient 不是 n。** §6 明写在某个较大 Rᴹ 内工作，M 不必为 n，常数可依 M。Def6.1 的 n、d 为实数；(n−1)-collection 指 angular upper exponent n−1，且族 saturated 意为 #T≈N^{n−1}。无需该族填满 ambient sphere，也没有新增 AD lower、CW 或 sticky 条件。
5. **arbitrary ambient 是递推的实际需要。** 证明在 Lemma6.6 前把配置 lift 至 R^{M+1}；第二输入 K(d+1,d′) 用于这个新环境中的 d-collection。只在 R⁴ 内成立的 K(4,4−ε) 不能直接替代 arbitrary-ambient 版本。

本稿 §1 的 ∀ε∃η 形式足以处理上述 soft-loss 定义；不在此反向证明任意其他 K 记号都能推出相同的显式 uniform statement。M 在每次调用中固定，未要求所有 ambient 共用同一常数或阈值。

## 3. 独立方向稀疏化：不是自动的维数单调性

这里证明一个有限桥。即使 A 的直接 s≥3 投影可免除此步骤，该桥仍说明“把方向指数降到 3”需要怎样保原质量。

固定 p=n−1≥3、M、R、C_M。设 T 满足

\[
m:=\#T\ge N^{p-\eta},\quad
\#(T\cap\operatorname{Cap}(u,\theta))
 \le N^\eta(N\theta)^p,\quad
S:=\sum_T w_T\ge N^{1-\eta}m,
\quad 0\le w_T\le C_MN. \tag{1}
\]

w_T 为原 marks 数。给定输出容差 τ>0，存在足够小的 η=η(τ,p,M)>0，使 N 足够大时有原子族 T′，保留每个所选 index 的**全部原 marks**，满足

\[
\#T'\ge N^{3-\tau},\quad
\#(T'\cap\operatorname{Cap}(u,\theta))
 \le N^\tau(N\theta)^3,\quad
\frac{\sum_{T' }w_T}{\#T'}\ge N^{1-\tau}. \tag{2}
\]

并且新 union 是原 union 的子集。此处无需 w_T 之间独立。

**证明。** p=3 时直接保 T，固定常数用 τ−η 余量吸收。p>3 时独立以 q=N^{3−p} 选每个 index。由有限多个半径 1 angular caps 覆盖 sphere，m≤C_MN^{p+η}。随机条数 X 的均值 qm 介于 N^{3−η} 与 C_MN^{3+η}，Chernoff 给 X∈[qm/2,2qm] 的失败概率趋于零。

对任意 cap、N⁻¹≤θ≤1，选中条数的期望至多

\[
qN^\eta(N\theta)^p
 =N^\eta(N\theta)^3\theta^{p-3}
 \le N^\eta(N\theta)^3. \tag{3}
\]

取 angular centres 的 N⁻¹-net 和 dyadic radii，再允许固定倍扩大，只有 O_M(N^{M−1}log N) 个测试 caps。每个任意 cap 包含于一个测试 cap，后者半径最多为原半径的固定倍；大半径 cap 用总数处理。对测试 cap 取阈值 C_{p,M}N^{τ/2}(Nθ)^3。η<τ/8 时该阈值远大于期望，且最小阈值也为 cN^{τ/2}。Chernoff upper tail 与 polynomial union bound 给所有测试同时成立，失败概率小于任意固定 N 负幂。把固定扩大常数吸收入 N^{τ/2} 后即得 (2) 的所有 centres/all scales cap。

随机原 mass Z 满足

\[
\mathbb E Z=qS\ge N^{4-2\eta},\qquad
\operatorname{Var}Z
 \le q\sum_Tw_T^2\le C_MN\,qS.
\]

所以 Chebyshev 给

\[
\Pr\{Z<qS/2\}\le C_M N/(qS)
 \le C_MN^{-3+2\eta}\longrightarrow0. \tag{4}
\]

可同时选择 cap、count、mass 三事件成立的一个 realization。于是

\[
\#T'\ge qm/2\ge\tfrac12N^{3-\eta},\qquad
\frac{Z}{\#T'}\ge\frac{qS/2}{2qm}
 =\frac{S}{4m}\ge\tfrac14N^{1-\eta}.
\]

η<τ 且 N 大，得到 (2)。不对 union 作任何随机独立假设。证毕。

因此，若已有任意固定 ambient 的 §1 n=4 强种子，则选输出 τ 为该种子的输入容差，(2) 给每个实 n≥4 的强种子。这是实证的有限稀疏化；**不是**从 dim_H≥4 或从 direction-parameter 的名称推得“单调”。输出抽样数约 N³，p>3 时不声称保同一绝对总 mass，而保合法调用所需的平均原 mass。

## 4. DIR-003 给 KT(40) 的任意条数形式：独立核号

KT 在 Def6.1 后写：删去总方向数饱和要求，K(n,d) 可给

\[
\#\bigcup_TY(T)\gtrsim \frac{\#T}{N^{n-1}}N^d. \tag{5}
\]

原文以 random rotations/factorization 解释 (40)。不能只核 saturated 输入就忽略递推第二处真正使用的 (5)。本轮 root/A 则直接从已有 DIR-003 支付它，无需另把 factorization 当未说明的新假设。

其有限几何输入是 A 已证明的任意 m 条投影 lemma：原 angular exponent s≥3、upper constant K 时，经 bounded Gaussian P:Rᴹ→R⁴、删短方向、collision independent set、共同 graph chart 后保

\[
m_*\ge \frac{cm}{K\delta^{3-s}(1+\log(1/\delta))}. \tag{6}
\]

这是任意 m 的估计，不预先用 m≈δ⁻ˢ。设原平均 shading≥λδ⁻¹、λ≥δ^η。先用逐线 cardinality upper 删 light lines，有至少 cλm 条，每条至少 cλδ⁻¹ marks。对这些 heavy lines 使用 (6)，并保共同 clock 中固定比例的各自旧 marks。最后 DIR-003 在 R⁴ separated slopes 上的 unit weights 使 α≤C，给

\[
\#E\ge
\frac{c\lambda^2m}{K(1+\log(1/\delta))}
\delta^{s-4+\varepsilon_D}. \tag{7}
\]

式中两个 λ 分别是 heavy 条数和每条 marks；3−s 在 (6) 的分母，故最终 δ 指数为 **s−4+ε_D**，符号无反转。当 K≤δ⁻η 时 K⁻¹≥δ^η，λ²≥δ^{2η}，总额外幂为 3η。

对固定目标 ε，先选 DIR-003 的 ε_D<ε/4 及其 long-mark 门槛 η_D，再取 η<min(η_D/2,ε/16)，最后 δ 小。此时 cλδ⁻¹≥δ^{−1+η_D}，固定 mesh/clock 常数可吸收；log 和其余常数也可用 ε 的剩余吸收。因此

\[
\#E\ge c m\delta^{s-4+\varepsilon}. \tag{8}
\]

令 s=n−1、δ=N⁻¹，右端为 cmN^{4−s−ε}，正是 (5) 的 4−ε 版本。若 m≥δ^{−s+η}，把 η 再取小，可得 saturated 的 δ^{−4+ε_target}。不能把 η 先固定成较大值，也不能声称 (7) 已给任意小 λ 的完整 maximal-function 范围。

## 5. Theorem6.2：六维链及未审责任

具名原定理为

\[
K(n,d)\ \&\ K(d+1,d')\quad\Longrightarrow\quad
K\left(n,\frac{2n+1+d'}4\right),\qquad 0<d<n. \tag{9}
\]

已逐段核其调用位置：第一输入参与删 heavy balls/构造 d-dimensional cover；Lemma6.6 在 R^{M+1} 构造 d-collection；Lemma6.7 对其 residual saturated shading 用第二输入和 (40) 排高 multiplicity。原定义中没有另藏 CW、sticky 或逐线 AD lower。原 Lemma6.6 proof 的 displayed exponent d−1 与 statement d-collection/随后 d 维 ball upper 不一致，疑为排印问题；本项目未据此宣布整篇 KT proof 逐步重证或定理失效，(9) 仍作为具名高级输入列出。

接受完整四维 proof→SRC/DIR，并接受 A/root 本轮有限转移后，对每个固定实 n≥4、ζ>0 得 K(n,4−ζ)。取 0<ζ<1，已有

\[
K(6,4-\zeta),\qquad K(5-\zeta,4-\zeta).
\]

在 (9) 取 n=6、d=4−ζ、d′=4−ζ，得到

\[
K(6,17/4-\zeta/4). \tag{10}
\]

这里第二输入参数 5−ζ 为实数，且在已付 n≥4 范围；不需要先拿经典六维 bound 作起点。原证明若在极值步骤提高 d，本轮全体 n≥4 的同一输入也覆盖相应第二参数；不将只在单个 n 成立的输入扩到未付范围。

固定 ζ 后依次选择有限次源容差和 N₀，再让 ζ→0。依原 Def6.1 后的 Hausdorff 转移，对其 compact Kakeya convention 条件性有 dim_H E≥17/4。一般不可测集合的 scope 不在本稿扩大。此链仍依完整 OAI4/SRC/DIR 以及 KT6.2，未经外部同行评审，不能登记无条件新六维定理。

五维方面，该递推若仅能取 d′≤d+1，则更新不超过 (12+d)/4，d=4 是固定点；本输入不解决五维满维数，也不解决一般维度猜想。

## 6. 一手高维前沿：正面比对与范围排除

本轮确实做了在线一手检索，核对版本、摘要和相关表格；“没有搜到更强六维界”不等于没有该文，更不等于优先权证明。以下表只登记实际核到的结论和适用范围。

| 一手来源 | 已核内容 | 对本轮六维链的作用 |
|---|---|---|
| [Katz–Tao math/0102135v1](https://arxiv.org/abs/math/0102135v1)，§6/Th1.1 | 经典 Hausdorff 维数表达式在 n=6 给 7−2√2≈4.171572875 | 具名递推输入与历史 baseline，不是本轮新证明 |
| [Hickman–Rogers–Zhang 1908.05589v1](https://arxiv.org/html/1908.05589v1)，Figure5 | 表中 n=5 为 18/5，n=6 为 7−2√2，n=7 为 34/7 | 明确较高维改进并不一律改善六维；不能把 maximal 的对偶 p 指数读成维数 |
| [Gao–Liu–Xi 2503.11574v1](https://arxiv.org/html/2503.11574v1)，Table1 | 2025-03-14 版本的 Euclidean 对照表仍把六维列为 7−2√2 | 独立较新 baseline；其 curved/Nikodym 主结论不当普通 line Kakeya 结论 |
| [Zahl survey 2512.09397v1](https://arxiv.org/abs/2512.09397v1)，§4 | 2025-12 的综述区分某些 n≥7 的 polynomial-partitioning 改进 | 综述不是“所有 n≥5 有同一增益”的输入，也不代替 primary theorem |
| [Wang–Zakharov 2609.22035v1](https://arxiv.org/abs/2609.22035v1) | sticky 四维/CW 范围；作者 Hong Wang、Dmitrii Zakharov | 不作为无条件一般六维新界 |
| [Lai–Pang–Sethi–Wang 2610.10603v1](https://arxiv.org/abs/2610.10603v1) | codimension-two plane Kakeya/CW 及四维 plane 问题范围 | 不是普通六维 line Kakeya 的同一命题 |
| [Fraser–Yang 2505.05709v2](https://arxiv.org/html/2505.05709v2) | 所有方向仍在；限制每线 midpoint 属于 packing 维数≤s 的固定集 A，推出 Kakeya 集 Hausdorff lower | midpoint 限制未由本轮一般配置给出，不能直接当一般六维 baseline |

另核到 [Kulkarni 2025 工作坊摘要](https://alexiosevich.com/neerajakulkarni.pdf) 声称高维 sticky 改进，但该对象为一页 talk abstract，不能当已核完整定理或一般非 sticky 六维结果。R⁴-only 的 2026 摘要、特定曲线 lifting、受限方向结论也不能填这一空缺。

因此能作的明确数值比较只有

\[
17/4-(7-2\sqrt2)=2\sqrt2-11/4\approx0.078427125>0.
\]

这说明**若全部条件输入有效**，(10) 超过已正面核到的上述六维 baseline。没有完成 exhaustive 2026 literature certification；不写“最新最优”、新颖性、重大结果或一般猜想已解决。

新 Gao–Liu–Xi 原件已由 root 入 literature/primary，23 页；本子任务未另建文献文件。其余已存文献沿既有库引用，网页摘要核验的对象与已下载原件明确区分。

## 7. 本轮验收与停止

已完成：KT 实量词/任意 ambient/平均 shading 的实际审计；独立保原 marks 的方向稀疏化；对任意条数 DIR 预算及两次 λ/η 符号的核验；六维精确参数链；一手正面 baseline 与 scope 比较。该有限接口有真实内容，不是把集合结论重命名成 finite estimate。

未完成：独立认证完整四维高级证明与全部源输入、KT 全文重新证明、2026 全部高维前沿穷尽、新颖性认证、无条件六维 17/4 或任何五维满维数结果。下一步由 root 的投影/source 交叉审查和宏观决策承担；不继续以 thinning/ε 等价变形登记新方向。长期 Goal 保持 active。
