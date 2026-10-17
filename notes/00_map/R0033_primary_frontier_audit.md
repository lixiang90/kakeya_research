# R0033：普通 Euclidean line Kakeya 与六维前沿的一手复核

2026-10-17，A / audit_four_dimensional，phase0 macro 子任务。已读 GOAL/STATE/ROADMAP/registry、AGENTS、R33 spec 和 R29 既有前沿记录，运行 context.py。本稿只做文献声明/范围核验，不开始 critical-path 数学，不修改 controls/Git。新 PDF 由 root 统一归档，A 未下载。

**结论：本轮实际读到的一手材料仍未给出可直接使用的、一般普通六维 line Kakeya 的 Hausdorff 下界≥17/4。正面核到的六维历史/2025对照基线仍为 7−2√2。** 这只描述下面列出的读范围；不是2026全部论文的穷尽认证、没有该定理的证明或本项目新颖性认证。R29 的17/4仍依完整 OAI4/SRC001/DIR003及具名 KT 输入，不能因本次检索而去掉条件。近期确有新四维论文，但已核声明没有填成一般六维结论。

## 1. 对象与审查门槛

目标是普通实 Euclidean line Kakeya：包含每个方向一个单位直线段的集合，维数用 Hausdorff。compact、任意集合、有限 tubes/marks 的版本分别标记。restricted directions、midpoint/parameter 限制、sticky、curved/geodesic、plane Kakeya、有限域、单尺度 whole-tube union 或 Minkowski 结论不能直接计入该基线。

maximal 输入须有原作者实际的全族估计与 Hausdorff 转移：不能把一条 whole-union volume 估计或一个指数名当作 Hausdorff theorem。论文明确陈述仍只算文献 claim；本轮未逐式重证其全部 proofs。

## 2. 正面六维基线与 maximal→Hausdorff 接口

### 2.1 Katz–Tao：具名 Hausdorff 结果

[Katz–Tao, *New bounds on Kakeya problems*, math/0102135v1](https://arxiv.org/abs/math/0102135v1)，v1=2001-02-16，发表于 J. Anal. Math.87 (2002),231–263。既有原文 `literature/primary/katz_tao_2001_v1_new_bounds.pdf`、提取文本同名；本轮复读 Theorem1.1及§6入口（提取35–50、968–1034行）。其 Hausdorff 下界是 `(2−√2)(n−4)+3`，n=6 给 `7−2√2≈4.171572875`。不能把其不同的 Minkowski/SD 指数套作同一结论。

R29 对 KT6.2 的任意 ambient、实方向参数、unsaturated shading 量词审查保持有效范围，本轮不重新登记为新结果，也不以本段阅读宣称完整 KT 证明已审。

### 2.2 Hickman–Rogers–Zhang：实际 maximal theorem 与六维数值

[Hickman–Rogers–Zhang, *Improved bounds for the Kakeya maximal conjecture in higher dimensions*,1908.05589v1](https://arxiv.org/abs/1908.05589v1)，v1=2019-08-14，发表于 Amer. J. Math.144 (2022),1511–1560；本次 arXiv history 仍只列 v1。已入库，另读[原 HTML](https://arxiv.org/html/1908.05589v1) intro、Theorem1.2、§9.2/Figure5。

作者在 intro/§9.2 明确将其 K_p 全族 maximal estimate 转为 compact Kakeya 的 Hausdorff lower `p′`。Theorem1.2在n=6的最小增量是1/3（k=3或4），故其 maximal 参数 p=4/3 对应 Hausdorff4，不超过 KT 的六维值；Figure5确将n=6列为7−2√2。不能从“高维改进”推断每个维度都改进。旧 v1 表格的其它维度历史数字不作为2026现状背书。

### 2.3 Zahl 的独立 polynomial 方法

[Joshua Zahl, *New Kakeya estimates using Gromov’s algebraic lemma*,1908.05314](https://arxiv.org/abs/1908.05314)，current v4=2021-01-12；v1=2019-08-14、v2=2019-09-23、v3=2020-10-07。先筛v2后改读[current v4 HTML](https://arxiv.org/html/1908.05314v4) intro、Theorem1.5/数值说明；未读全证明。

其线性 maximal theorem 给

`d(n)=max_(2≤k≤n) min(n−k+2,(n²+k²+n−k)/(2n))`，

并明确 maximal dimension d 蕴含 Hausdorff lower d。n=6 为4，且作者说明改进不包括n=6。该式与HRZ的范围一致，不能额外提供六维17/4。这里 web-only 核声明，未增加新的数学输入。

### 2.4 Gao–Liu–Xi 的2025独立对照

[Gao–Liu–Xi, *Curved Kakeya sets and Nikodym problems on manifolds*,2503.11574v1](https://arxiv.org/abs/2503.11574v1)，v1=2025-03-14；current history仍只列v1。[Table1](https://arxiv.org/html/2503.11574v1)（本地PDF12，R29已视觉核）明确将 Euclidean Kakeya 的n=6列为7−2√2，归因KT02。本轮复查表和intro范围，不以其 curved/Nikodym 新定理冒充新的普通线段六维估计。

这是2025正面证据；不是截至2026-10-17的完整前沿表。

## 3. 2026近期四维工作：逐篇范围与版本疑点

### 3.1 Choudhuri 的新普通四维下界

[Mukul Rai Choudhuri, *New bound on the Hausdorff dimension of Kakeya sets in R4*,2610.12480v1](https://arxiv.org/abs/2610.12480)，[versioned HTML](https://arxiv.org/html/2610.12480v1)。已读 abstract、intro/Theorem1、§4 Proposition17与范围说明；未认证 graphical decomposition、三线性/planebrush 完整 proof。

Theorem1 对 compact Besicovitch sets in R4 给

`dim_H≥13/4−(12951−54√10593)/41972≈3.073854`。

intro明确工作 ambient 为R4。正文中的 three-dimensional Wang–Zahl input 在代数 variety 厚邻域内使用，不是一般六维 line theorem。本次对 full HTML 查 six/higher 的定位，未见六维17/4 statement；此有限文本检查不排除另文推论。

**元数据异常须保留：** primary abs 的 Submitted/history 与 HTML header 均显示 v1=2026-08-30 23:56:18 UTC，而 ID 为2610.12480，browse context为2026-10；搜索摘要也呈现冲突日期。不能把 arXiv编号月份、搜索索引的相对日期或重复镜像当校正依据。本稿原样记录，不自行修日期，也不以此疑点否定正文数学。已告 root 统一保存 [versioned PDF](https://arxiv.org/pdf/2610.12480v1)。root另报入库PDF首图正文日期为2026-10-12、sidebanner为Aug30；这是root的视觉核验而非A独立render，亦未消除该literal异常。

### 3.2 Moreira：restriction/Kakeya 四维范围

[Tiago Moreira, *Refinements on the Restriction and Kakeya problems range in R4*,2610.06181v1](https://arxiv.org/abs/2610.06181v1)，v1=2026-10-05 12:00:51 UTC，25页。[HTML](https://arxiv.org/html/2610.06181v1)已读intro、Kakeya定量定义及Corollary2，未读完整bootstrap proof。

Corollary2给 ordinary R4 Kakeya 的 Hausdorff lower `26343/8588≈3.06741`。标题中的restriction与maximal估计本身不等于六维结论；本次明确引用的是它自己陈述的四维Hausdorff推论。没有把它扩到n≥5。已告root保存 [versioned PDF](https://arxiv.org/pdf/2610.06181v1)。

### 3.3 Hua–Yao–Yang：结构 factoring 并非维数改进

[Zhixu Hua, Xinshun Yao, Xiufan Yang, *Profile-Stable Buffered Multiplicity Factoring in Four Dimensions*,2608.18693v2](https://arxiv.org/abs/2608.18693v2)，v1=2026-08-19，current v2=2026-08-27。[v2 HTML](https://arxiv.org/html/2608.18693v2)读 abstract、intro、Theorem2.2 hypotheses/conclusion及末尾source-role说明，未审proof。

v1题名是 *Buffered Shading-Compatible Multiplicity Factoring in Four Dimensions*；其§7有 conditional dimension-raising schema。**不能把v1的题名/§7文字混进v2的已证结论。** v2定理对indexed convex parent–child families inR4给含 weighted Frostman/profile/efficiency 的coarse density和multiplicity-factoring结论；intro明确还需额外analytic ingredients才有新的 maximal或Hausdorff估计。它没有无条件给六维17/4，也不能不支付profile就当本项目旧WP4通用猜想。已告root存 [v2 PDF](https://arxiv.org/pdf/2608.18693v2)。

### 3.4 Wang–Zakharov 的 sticky 范围

[Hong Wang, Dmitrii Zakharov, *Kakeya and Furstenberg problems for sticky sets of tubes*,2609.22035v1](https://arxiv.org/abs/2609.22035v1)，primary v1=2026-09-18 17:28:26 UTC，117页。已入库、前轮有详细source审计；本轮仅复核官方abstract/history。它的R4 full result明列 sticky sets of tubes satisfying convex Wolff axioms，不能免费移除sticky/CW条件或当一般六维结论。高维matrix/mixed缺口仍按旧冻结账处理。

## 4. 不同 Kakeya 对象的隔离

### 4.1 Fraser–Yang：所有方向仍在，但 midpoint 受限

[Jonathan M. Fraser, Lijian Yang, *Hausdorff dimension of restricted Kakeya sets*,2505.05709v2](https://arxiv.org/abs/2505.05709v2)，v1=2025-05-09，v2=2025-06-25。[HTML](https://arxiv.org/html/2505.05709v2)复读Definitions1.1/1.2、PropositionA、Theorem2.6/Cor2.7及abstract范围。

这是每个方向的单位线段，但须让其 midpoints 属于某固定A，并对A的packing/box维数付条件。Hausdorff lower包括n−s及依低维maximal输入的n−g_n(s)。不能称“方向受限所以没所有方向”，也不能因所有方向存在就删掉midpoint假设。本项目的一般六维配置没有证明所需小s；本轮不调用它作一般六维下界。

### 4.2 curved、geodesic、plane、有限域

[Arian Nadjimzadah, *Lifting curved Kakeya sets to linear Kakeya sets*,2609.06299](https://arxiv.org/abs/2609.06299) 的方向是以更高维 classical Kakeya 输入得到特定 curved 后果；它不是先提供更高维 classical conjecture 的解答。本轮只复核abstract，既有lifting窄类冻结不重开。

另筛到 [*Bourgain’s condition, sticky Kakeya, and new examples*,2511.10918](https://arxiv.org/abs/2511.10918)，current v4=2026-08-18，abstract是满足Bourgain条件的 curved sticky 到 classical sticky 的 reduction；不是一般普通line六维定理。CC-geodesic/Heisenberg、plane unions、codimension-two plane Kakeya及有限域结果也不用于本轮六维基线。这里为scope筛选，未全文认证。

## 5. 算术前沿筛选，不作为新几何输入

[Terence Tao, *Sum-difference exponents for boundedly many slopes, and rational complexity*,2511.15135v1](https://arxiv.org/abs/2511.15135v1)，v1=2025-11-19；[HTML](https://arxiv.org/html/2511.15135v1)读abstract、intro至Theorems1.3/1.4。其当前全局SD infimum upper仍引用1.67513…；新结果讨论固定有限slopes与rational complexity变化时SD向2的行为，不是宣称改进一般六维Hausdorff至17/4。本轮不从intro的维数转换语句重建新Hausdorff输入，未读全部entropy proof，也未以AlphaEvolve数值充当连续结果。

该项只是避免把2025算术新论文漏看后误报“无后续研究”；不重开已冻结Y-only/BSG路线。若以后真用它，须另外付原scalar/entropy/实际source接口及Hausdorff转移。

## 6. 四维主结果后的高维推论：目前实际核到什么

本地OAI4 §11.2（PDF169附近；提取9073–9080行）明确只写：对d≥4普通Kakeya E投影任意四维子空间，得到 `dim_H E≥4`，特别包括五维。该论证对任意集合，靠projection不增covering diameters，不需要measurability。

这段不包含六维17/4。§11其它 direction-set/Nikodym/curved后果具有各自 transfer 假设，不能把它们直接接成任意ambient有限KT种子。R29既有FSD001已另行支付 finite direction/shading/任意ambient/unsaturated 接口；只有保其全部来源条件后，才有条件的compact六维17/4链。**这是一条有实际证明责任的候选收益，文献检索不能替代源认证，也未证明其优先权。**

## 7. 检索范围、归档与宏观意见

本轮实际queries包括：Kakeya+six/six-dimensional/R6+Hausdorff；Kakeya+17/4/4.25；Kakeya+higher dimensions+2025/2026+maximal/lower bound；four-dimensional+OpenAI+higher-dimensional consequences。随后打开上表primary abs/versioned HTML，核history、正式statement和scope。学术数据库/综述/搜索结果只作定位；未用百科、二手AI摘要、博客或镜像证明数学。搜索亦出现未经核验的“所有维度已证”自发布声明；未认证其proof，不能拿来宣告Goal已解决，也不能据不采用它们断言所有此类文献都错误。

新三篇PDF的versioned URLs与读范围已发root，root已报统一下载/pdfinfo/text/首图核验：Choudhuri19页325031bytes、Moreira25页446662bytes、Hua–Yao–Yang39页558008bytes；准确归档路径/hash由root的metadata记录，A未独立下载。其它web-only条目不自动变成数学inputs。现有KT/HRZ/GLX/Survey/WZ原文仍在专门文献库。对2610.12480的日期异常、2608.18693的v1/v2题名与范围变化须随metadata保存。

**宏观建议：** 本轮一手证据没有正面消除R29条件收益，但也不够认证“最新最优/首次17/4”。若继续source audit，下一main应针对真正剩余critical-path/normalization量词，并保持逐段可证伪停止条件；不再改进已付TCM/ASM/TEX的局部常数，也不因查无同界就延长整篇源审计为默认最终路线。是否选该main由root合并官方版本与B依赖审计后决定。本稿不先启动4.3证明。Goal保持active。
