# R0036：高维一手前沿、六维条件出口与路线复核

2026-10-17，独立宏观审查 B。读取 GOAL、STATE、ROADMAP、registry、R36 working spec、R29 KT/frontier audit、R33 macro 及 R35 remaining-responsibilities。此稿只评估下一行动；没有重新认证完整 OAI4、KT 或一般五维定理，也不认证优先权。

**结论。** 本轮正面核到的一手来源仍支持六维旧 Hausdorff 基线 7−2√2；没有核到一项可以直接覆盖条件 17/4、或支付实际 AFF₃/二维 growth 的新定理。这个有限检索结论不等于完整前沿认证。建议维持直接五维旧路线冻结，选择一个有界完整的“原 scalar projection 8.2 → unbounded narrowness 排除 10.1”阶段，单独检验真实 law/标签/外推；不能因论文还有下一节而无限续审。

## 1. 原条件出口仍有实际数学区别

OAI4 当前本地原文 §11.2（PDF169）仅陈述：正交投影到 R⁴，使任意 n≥4 的 Kakeya 集满足 dim_H≥4。该处不陈述六维 17/4。R29 的额外内容是 proof-level finite readout/SRC-001、DIR-003、任意固定 ambient/实方向参数的投影转移，以及 KT6.2，而不是重复这一普通投影句子。

R29 finite bridge 的关键预算仍为

\[
\#E\ \ge\ \frac{c\lambda^2m}{K(1+\log(1/\delta))}
\delta^{s-4+\varepsilon},\qquad s\ge3.
\]

两个 λ 分别来自 heavy 原管数与逐管原 marks；K≤δ⁻η、λ≥δ^η 时额外损失为 3η。任意条数、平均 shading 与全 angular caps 不能省成集合 Hausdorff 句子或“ambient 单调性”。这里不重证已通过的 R29 桥。

[Katz–Tao, *New bounds on Kakeya problems*, math/0102135v1](https://arxiv.org/abs/math/0102135v1)，Def6.1/Thm6.2 的真实输入是 arbitrary fixed ambient、实 n,d、saturated average shading；递推为

\[
K(n,d)\ \&\ K(d+1,d')\ \Longrightarrow\
K\bigl(n,(2n+1+d')/4\bigr).
\]

若完整 source 确实提供所有实 n≥4 的 K(n,4−ζ)，取 n=6、d=d′=4−ζ 得 17/4−ζ/4，进而得到 compact 六维的条件 Hausdorff 下界 17/4。全部源分支、finite 读出、named advanced inputs、KT6.2 责任均保留。仅靠该种子与递推，五维更新以 4 为固定点，不能解决五维满维数。

因此，17/4 不是 OAI4 §11.2 已明述的结论；但“本文未明述”也不证明它未在其他文献或公开讨论中出现，更不认证新颖性。

## 2. Hausdorff、Minkowski 与 maximal 的正面比对

| 一手版本及位置 | 实际核到的内容 | 六维比较 |
| --- | --- | --- |
| [KT math/0102135v1](https://arxiv.org/abs/math/0102135v1)，Thm1.1、§6 | Hausdorff 为 (2−√2)(n−4)+3；同定理另外给 Minkowski 和 maximal，三者数值不相同 | n=6 给 7−2√2≈4.171573 |
| [HRZ 1908.05589v1](https://arxiv.org/html/1908.05589v1)，Thm1.2、§9.2/Fig5 | maximal 改进范围是 n=5 或 n≥7；§9.2 单列它对 Hausdorff 的后果，并说明与 KT 优劣随维数变化 | Fig5 明列六维仍为 KT 的 7−2√2，五维为 18/5 |
| [Gao–Liu–Xi 2503.11574v1](https://arxiv.org/html/2503.11574v1)，Table1 | 2025-03-14 原稿，普通 Euclidean Kakeya 对照列与 constant-curvature Nikodym 列分开 | 六维 Kakeya 栏仍是 7−2√2；其 manifold reduction 不给更强 Euclidean 六维界 |

KT 原文 introduction 引述的更早值中，Bourgain 1999 的 (13n+12)/25 在 n6 为 18/5；Katz–Tao 1999 的 (6n+5)/11 为 41/11；Wolff (n+2)/2 为 4。它们均低于上述六维 KT 值。此处按 KT 对这些旧结果的正面引述校准，不声称本轮重新审过三篇深层证明。

HRZ 用 tube-overlap L^p 的记法时，维数读出是 p′，不可直接把显示的 p 当维数；经典 maximal-operator L^p 的另一记法也不能与它混用。Minkowski 下界优于某数不自动推出相同 Hausdorff 下界。条件 17/4 与正面核到的六维 Hausdorff 基线相差

\[
17/4-(7-2\sqrt2)=2\sqrt2-11/4\approx0.078427.
\]

这只是明确条件下的潜在数值收益，不是无条件新界。

## 3. 本轮新增核查：Gan 的 2026 出版不能按年份升级

[Gan, *Hausdorff dimension of unions of k-planes*](https://arxiv.org/html/2305.14544v2)，arXiv2305.14544v2 为 2023-07-24；[期刊页](https://doi.org/10.1112/mtk.70071) 为 2026 出版。核其开篇主命题及 Thm5：仿射 k-plane 参数族维数为 (k+1)(d−k)+β 时，union 下界是 d+min(1,β)；有限估计要求仿射 Grassmannian 的全部参数球 packing cap。不是只给方向 cap。

取普通六维 line 族 k=1、参数维数仅已知≥5，d=3、β=1 的直接读出仅为 4；五维参数维数≥4 的对应读出仅为 3。这不覆盖条件 17/4。若要更强数值，必须先付额外参数维数或结构。k>1 不能用于只含原直线、尚未构成整片平面的配置。

因此它不是新的 AFF₃ 原 matrix-time/gain 定理。它的 BL/broad-narrow 方法可能启发研究，但必须另外证明真实原 prior 满足所需参数 cap 及同一 g 的作用接口；不能把现有 visible graph/plane cap 替成这些条件。

## 4. 另一个 2026 primary 的实际范围

[Germain–Latocca 2606.29993v1](https://arxiv.org/html/2606.29993v1)，arXiv 提交日 2026-06-29，核 §1.3.2/Thm1.4：对象是圆柱 R×T^d，长度 R、宽 δ、δ/R 分离方向，p>2 的 tube-overlap 估计；含空间环绕造成的额外项。固定有界 R 可回到局部 Euclidean 比较，但这个 p 范围不覆盖六维维数 17/4 对应的共轭指数 17/13。它没有支付 AFF₃、共同时间原 action 或二维非二次增长。没有下载额外 PDF，也没有当高级输入加入项目。

已在 R12/R28 审过的 [Nadjimzadah 2609.06299](https://arxiv.org/abs/2609.06299) 是从更高维 classical Kakeya 假设推出较低维 curved 问题的 forward lifting；不能反向用于解决原五维 classical 缺口。没有因本轮再次命中就登记新机制。

## 5. “所有维度已解决”声称的具体筛查

按 root 提示核 [Tang–Ionescu, preprints.org/202602.1025v1](https://www.preprints.org/manuscript/202602.1025)，2026-02-15。Def2.3 是每方向含单位线段的普通定义；Thm2.6 宣称 Lebesgue 体积至少 sphere-area×ζ(n−1)。这不是 dim_H=n 的等价表述。

不用任何外部反例即可排除该体积结论：取各方向的中心单位线段，其并为闭球 B(0,1/2)。在 n3 体积是 π/6，而其下界是 4πζ(2)=2π³/3。即使只用从原点出发的单位线段，并集 B(0,1) 也仍违反该下界。该检验针对 §2 的通常 sweep/ordinary Kakeya 解释；若另改为 §3.1 全部平移之并，则集合已是整个 Rⁿ，更不能证明普通问题。故不能调用 Thm2.6，不以作者、平台或未同行评审身份作否定理由。

## 6. 有限检索范围与未获得的输入

本轮在 arXiv/primary publisher 核题名、版本、abstract 和上述具体定理/表格；查询包括 Kakeya+Hausdorff+six/17/4/4.25、Gan+maximal+higher dimensions、2026+five dimensions，以及最新 curved/lifting/cylinder 命中。有限查询的空结果只作为检索日志，不是数学或书目不存在证明。R33 已核的四维 Choudhuri、Moreira、Hua–Yao–Yang 与 R29 sticky/codimension-two/midpoint-restricted 条目不重新充作本轮新结果。

实际缺口仍是：AFF₃ 保真实 D=((t−s)ψ,−[M(t)−M(s)]ψ) 的 clock/angle/原 g；或原 vector-Y 的二维 growth。现有 plane nonconcentration、一般 graph/coherence、原 finite CS box 及 average carry 已有明确边界，不能仅因检索未找到解法而改名重启。没有核到可直接清掉这些责任的新 primary theorem。

## 7. 唯一下一阶段建议、closure 排重与退出

建议选择**原 Theorem8.2 完整 scalar mesh projection，并将它真正接入 Proposition10.1 的无限优化窄度排除**，作为一个有界责任阶段。8.2 的输入是同一 probability trajectory prior、dominated active law、全部 scalar bin cap、终端 occupied-cell count；输出必须是互不相交的 whole-trajectory assignments、whole-unit-time quadratic fits 和真实 label floor。10.1 还要求 nested true systems、original/tangent subpower 两类常数、终端 known-list 的实际回传。不能仅证明标量集合投影或最后一个时间的拟合。

选择理由：ISO 已支付 scalar zero-horizon 这一真实新输入，因而有机会用一个完整阶段缩减既有 finite→KT 路线的分支责任。它没有消除正有限窄度或 full-source，仍须列出剩余 §7/§9、2.17/readout 与 named KT 等条件。直接五维原 action 无本轮新可用 input，继续 BSG/CP/数字局部量的期望收益低于这个有实际接口的阶段。

closure 排重必须先核：8.2 是否只是已付 ISO 加平滑/选择的严格推论，若是，只把该有限接口当依赖认证；本阶段真正验收放在 10.1 的原系统/极限与可用 atlas，而不登记新 scalarization 或新结构定理。不能把 10.1 的“∞ 不发生”误写为正有限窄度也已闭合。

停止条件为：完整固定命题与全部保留条件通过独立逐步审查；或找到不能由原假设补救的 smoothing/prior/coverage/标签/极限错误，并标明对 SRC/DIM 的影响；或缺一项高级输入而将该项明确保为条件。不得以再补一个常数、重命名小量或隐含假设缩小命题来逐轮续审。若此完整阶段之后又出现两轮无实质输入收益，应重做路线选择，不自动转入下一个编号。

本稿不提前进入上述证明。长期 Goal 仍 active；macro、源责任认证及条件数字比较均不满足最终或重大成果验收。
