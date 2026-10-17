# R0048：有限一手前沿、正式版本与递归输入的范围

2026-10-17，A。已读 GOAL/STATE/ROADMAP、本轮 macro/working spec、R47 next 与 R42 前沿稿，并完成一轮有界 primary 检索。本文不替 root 操作文献库或 Git。先报告结论：**本轮实际打开的一手声明中，没有找到已覆盖 H5 的 ordinary Euclidean theorem；这不证明不存在该定理，不认证 first/best/major。HRZ 已有2022正式发表版本，应核 accepted manuscript 与库内v1，而不是把历史表作为现行前沿。**

本轮 H5 是满4参数 δ-direction net 的真实R5单位图管、逐管至少 δ^(−1+η) 原 time marks 下，存在固定 σ>0，∀ε>0∃η/δ0/c 使 #E≥c δ^(−4−σ+ε)。普通集合 Hausdorff 结论、完整 Lp maximal、near-full finite shading 三者分开；不能看到某个维数数字就跳过实际输入。

## 1. 有界检索、读取范围与不作的推断

本轮查询 ordinary Kakeya/five-dimensional/six-dimensional/higher-dimensions/2025/2026/17/4，并核 HRZ 正式 DOI、institution 页面、arXiv history，随后打开本节以下 primary。有限域、环、Heisenberg、一般曲线/圆、限制估计应用和数值数据集均先按对象筛掉。二手报道只作索引，没有用来认定定理已证或适用于 H5。

已核 R33/R39/R42 历史范围，未重下所有旧文献或无尽扩大 query。搜索无命中不排除未索引材料、未显式写出数字的直接推论或专家熟知应用。作者自己的预印本声明与本项目的逐步证明/具名输入、外部同行评审三层分开。

## 2. HRZ：当前 arXiv、正式发表与应该使用的版本

[Jonathan Hickman、Keith M. Rogers、Ruixiang Zhang, *Improved bounds for the Kakeya maximal conjecture in higher dimensions*](https://arxiv.org/abs/1908.05589) 的官方 history 本轮仍仅 v1，时间2019-08-14。本库 `hickman_rogers_zhang_2019_v1.pdf` 就是此版本；已实际读其PDF1–3/原Thm1.2/表、目录定位，并用本地文本逐式核字面。

但 [University of Edinburgh 的作者机构 primary 页面](https://www.research.ed.ac.uk/en/publications/improved-bounds-for-the-kakeya-maximal-conjecture-in-higher-dimen-2/) 明确标为 peer-reviewed journal article：*American Journal of Mathematics*144(6)(2022),1511–1560，出版日2022-12-06，DOI [10.1353/ajm.2022.0037](https://doi.org/10.1353/ajm.2022.0037)。该页另提供 accepted author manuscript [PDF](https://www.research.ed.ac.uk/files/348574117/1908.05589.pdf)。已把准确链接交 root 统一下载/版本对照；A 不因 arXiv 只有v1就声称没有后续正式版本。

机构页的“43页”字段与期刊1511–1560的页码跨度不是同一排版，不能据此判断正文数学不同。arXiv题名页和机构页作者均为三人；工具某些自动摘要的“1 other authors”不是实际作者数。

后续 root 找到并且 A 也实际打开了 [JHU/AJM 官方43页PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-hickman-rogers-zhang.pdf)。本轮A独立读其PDF1–3/Thm1.2、PDF16/Thm4.1及PDF33–35的tiny/式(51)–(53)/多尺度PW接口，并与本库v1相应段对照。这些主接口字面对应，不能据此宣整份bytes全同；明确可见的差异是v1四维历史表1.4794...在该官方PDF为1.4854...，资助/致谢亦有修订。n5的18/13与递归终点没有因这项表修订自动改善。

下载边界也分开记录：Edinburgh默认CLI Win10013、升级请求403，JHU CLI同样403；web工具确实可以读取JHU全文。root没有拿到可入库的新PDF bytes，故本轮不伪报已离线保存accepted manuscript/hash。正式source依据精确URL与本轮实际读scope记录，而本地逐式施工仍用已存versioned v1，相关接口已作上述对照。

v1 Thm1.2 的 maximal range为

    p>1+min_(2≤k≤n) max{ 2n/[(n−1)n+(k−1)k], 1/(n−k+1) }.

n5优化给 p>18/13，conjugate极限18/5；其n6表仍 p>4/3，而更好的 ordinary Hausdorff n6基线来自 KT 的不同输入。原摘要的 n5 或 n≥7 改善不是2026每维最优保证，也没有 full4D maximal。

R13早已核过 n5/k4 broad21/5、narrow2p−3与理想planebrush边界。R48不能把再算这个 narrow 障碍登记为新信息；唯一未重复的本轮接点是实际 alg1/alg2 的 tiny terminal、原多尺度管子族及直接 near-full restricted-weak-type 质量接口。

## 3. Ordinary 维数/有限基线的正面对照

| 一手资料及本轮读取 | 精确对象与数值 | 能否直接供应 H5 |
| --- | --- | --- |
| Katz–Tao，[*New bounds on Kakeya problems*, math/0102135v1](https://arxiv.org/abs/math/0102135v1)，本库Thm1.1、R29/R38已付调用，本轮核其现有记录 | ordinary Hausdorff ≥(2−√2)(n−4)+3；n6为7−2√2≈4.17157，n5公式约3.58579 | 不是严格>4的五维 finite 原输入 |
| HRZ1908.05589v1及正式发表页面，本轮读取范围见§2 | n5 maximal p>18/13，对应集合18/5；n6该maximal表为4 | 18/5<4；题名higher dimensions不使其自动覆盖H5 |
| Joshua Zahl，[*New Kakeya estimates using Gromov's algebraic lemma*,1908.05314v4](https://arxiv.org/html/1908.05314v4)，官方v4=2021-01-12，本轮读intro/Thm1.5范围 | ordinary maximal/dimension参数与HRZ相关；n5为18/5，n6该方法参数4 | 不给H5 |
| Gao–Liu–Xi，[*Curved Kakeya sets and Nikodym problems on manifolds*,2503.11574v1](https://arxiv.org/html/2503.11574v1)，当前history仍v1=2025-03-14；本轮重读本地PDF12 Table1/Thm1.5 | Table1明确ordinary n5 18/5，引HRZ22/Zahl21；n6 7−2√2，引KT02。新结论是向constant-curvature Nikodym转移 | 不是ordinary新维数改进；2025表不能当2026穷尽表 |
| OpenAI四维原稿及本项目 RED/DIR/FSD 输入，见§4 | 原声明全4D Hausdorff；项目已付条件finite链给n5≥4，以及具名KT递推的条件n6≥17/4 | n5已有4，H5要求真实固定σ>0的新增五维finite增益 |

17/4与7−2√2的差约0.078427125仅是正面对照，不认证优先权。由n6下界17/4不能免费推出n5严格>4：即便用K×interval加一维，返回的也至多是13/4这类更弱比较；不能逆向投影凭空得到维数纤维增益。

## 4. 当前 OpenAI 原稿及项目依赖状态

本轮实际打开 [OpenAI 官方 manuscript README](https://raw.githubusercontent.com/openai/math/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/README.md)，题名、作者OpenAI、日期2026-09-24不变，没有在该README看到增添的更高维statement。原§11只给向R4投影的高维≥4后果，不是n5>4或完整4D maximal。

A尝试 GitHub contents/history API 的 web 工具入口不可访问，CLI urllib 因sandbox网络返回WinError10013，因此不把自己的失败伪报成功。随后 **root 通过官方Git API逐级tree独立完成当前核验**：main root tree `1581d4cbdd69a0faf34b2089614fe2a814316a6a` → preprints tree `df0564b2deaab87e07854b6344d8c2f037682e77` → manuscript directory tree `807c97661f95850b7c324356febc3774e7c51c86` → `paper.pdf` blob `45ec20e423db2a9c70fd6303510bac361e6e9e8a`，size1371486，与本库原PDF相同。这个结果来自本轮root的authoritative JSON核验；不是仅凭README日期沿用历史hash，也不是A自己已读取API bytes。早先recursive API断连/直接PDF contents的UTF8拒绝不推翻其后逐级JSON成功。

本项目 RED001 已完成内部4D组装、finite SRC/DIR读出、任意集合outermeasure有限见证和Hausdorff桥；FSD001支付 arbitrary fixedambient/real-s angular projection及unsaturated/two-λ预算；DIM001的具名KT链与内部application已付。不能把R29历史“仅compact/assembly待审”重新当当前数学缺口。

仍保具名高级定理责任和新2026输入/预印本层次，不将内部独审自动变外部评审，也不把“未从零重证每个已发表高级proof”机械当必须无限递归的工作。对本轮HRZ来说，DIR/FSD只有原straightline、direction cap/分离、共同clock、near-full density及∀ε∃η输入；它们没有全Lp/任意λ强度。

## 5. 2025–26相关新输入与适用边界

[Binyamini–Salant2609.24135](https://arxiv.org/html/2609.24135v1) 当前history仍v1=2026-09-21。本轮重读Main Thm1/Cor2/overview：对角δ-separated真管及同一复杂度E的semialgebraic S，逐管fraction≥λ给 |S|≥#T λ^nδ^(n−1)/poly_n(E)，并有degreeD、k-variety内contained管数≤poly_n(D)δ^(1−k)。去掉旧δ^ε并显式控制复杂度是实际输入，但不是ordinary n5新维数界。R42/43已审原权/共同affine/细粗推前边界；R44 growing-degree envelope无strict saving，不因“exact”再自动重开那些阈值。

[Lai–Pang–Sethi–Wang2610.10603](https://arxiv.org/abs/2610.10603) 本轮官方history仍v1=2026-10-07；对象是codimension-two flat flakes满足convex Wolff，不是任意ordinary lines。R40已核fine-wholeclock flat提取门槛与fixed-loss边界；不能把HRZ的4D variety邻域直接改称其合格flake输入。

[Wang–Zakharov2609.22035](https://arxiv.org/abs/2609.22035) 官方当前仍v1=2026-09-18，作者Hong Wang/Dmitrii Zakharov。原摘要明确sticky/CW R3 Furstenberg及sticky/CW R4 Kakeya；既有高维框架中尚未支付的matrix/mixed alternatives没有因摘要出现“Kakeya”被完成。不是新无条件R5 theorem。

[Moreira2610.06181v1](https://arxiv.org/html/2610.06181v1) 是R4 restriction/maximal的改进，本轮核intro/声明：所报maximal维参数约3.06737，非full4D Lp。Choudhuri2610.12480的R4 3.073及其日期异常已在R33保存，不会变成R5>4声明。Zhang2608.17952v2的四有理投影mixed-norm与FD–deLaSalle2607.14824v3的log上界构造已在R45–47付scope，当前不把其题名重新当HRZ terminal强输入。

新检索还返回曲线压缩2610.05404、p-adic/finite-field、Heisenberg和周期数值模型；对象不合本轮ordinary straightline H5，没有将它们加入主数学依赖。

## 6. 真实递归检验应当保留的责任

有限前沿没有提供可直接替代本轮任务的新ordinary theorem，故可以继续一次真实HRZ alg1/2接口核查。但下列是假设清单，不是已经完成的桥：

1. terminal仍在原R5、带原角分离/权重的tube子族上，或者真能有可支付的straightline R4模型；variety维数4本身不等于已flatten的R4线族。
2. 逐管δ^η marks在ball/window裁切、重缩、wall/tangent/transverse父子重数后仍合法，平均mass与逐管density分别heavy。
3. DIR/FSD只控制原δ-direction bin cap；投影/重分箱/重复祖先须付真实多重性。新曲面参数化可能弯线，不能免费调用原seed。
4. HRZ原Lp递归与只需near-full finite原目标的强弱要分开；若只能证明“没有完整Lp所以不能用”，仍未排直接finite方法。反之，不能为方便给DIR补未证任意λ或fullLp。
5. 所有ε/η及relative-scale参数顺序保持∀target ε∃source η；不得把任意小ε当任意η模数，或以未控制的δ_new损失假装subpower。

这些实际账本由root/B主施工，本稿不重复其所有递归证明。已知R13 broad/narrow numerology只作历史排重；本轮信息增益必须来自实际tiny终点/质量或严格新缺口。

## 7. 本phase结论与停止

有界primary phase完成：推荐保存正式accepted HRZ供版本对照；没有新增可直接覆盖H5的ordinary theorem。此判断允许进入唯一已选真实递归检验，并不预认证成功、优先权或新界；没有理由无尽扩大搜索。

若最终只原HRZ界/4D投影基线、缺真实flatten/原mass/更强maximal，按working spec一轮停止，不续k/radii/degree/η阈值；旧cyclic/PW/mixed等冻结不改。formal review等root完整主稿、macro/next与B终稿后实际全文读完才写。Goal仍active，一般高维目标不降低，未经外部同行评审。
