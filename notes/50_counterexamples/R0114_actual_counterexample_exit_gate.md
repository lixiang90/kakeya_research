# R0114：真实反例出口、新构造来源与中心关联输运反攻

2026-10-26。constructive_gate 周期宏观分工，只编辑本文件，不提交 Git。结论为 **no qualified strict-dimension construction / new ordinary finite input**。本轮有一项新一手来源的具体生成公式反攻；不把可修复的公式问题说成其主定理为假，也不把局部拒桥当 Kakeya 反例或重大结果。未经外部同行评审。

## 1. 恢复、原对象与本轮停止门

实际读当前 GOAL、STATE、R113 next；回读 R41 Perron 原构造与参数责任、R47 rough cycle 停止范围、R83 selector/acyclic 冻结、R93 同集全方向零体积满维例。主目标仍为同一个实欧氏集合含每方向实际单位段且有严格 Hausdorff 上界，或严格超出 DIM001 的完整新输入。没有从“零体积”“某个 clock 强碰撞”“参数像的 lower”改写完成门槛。

本分工没有续 R113 三角/DAG/block 势能证明、LW Cartesian、R47 rough cycle、acyclic 或 KT 数表。root 另研究完整紧致多纤维 straight-line 问题，本稿不重开该任务。先给候选 statement/可行性，再作资格核验；没有 source 主幂或实际 whole-clock upper 就停止，不追加待证联合质量作成功公设。

## 2. 快速否决的 scalar-J 候选不成为新方向

曾向 root 报告非 Cartesian 的候选 \(a(v)=c(v)Jv\)，其中 \(\mathbb R^4\simeq\mathbb C^2\)、\(J\) 为固定复结构、\(c\) 为任意 bounded Borel 标量。它包含上一轮无 fixed real flag 的线性校准，所以字面上不是实坐标前缀表。但每条实际线都留在 \(L\times\mathbb R\)，\(L=\mathbb Cv\)；非零物理 horizontal 点 \(x\) 的商 \([x]\in\mathbb{CP}^1\) 恰恢复 \(L\)。

在 annular slope 域和固定正 clock 子区间上，\(|x|=|t+ic(v)|\,|v|\ge t|v|\) 统一离 0。每个 \(L\)-纤维是具有开方向 patch 的真实三维线段族，具名三维 Kakeya 定理加 ordinary slicing 直接给 \(3+2=5\)。这只是在真实 Hopf 纤维上迭代已有低维完整输入，不作用任意 ordinary/source 对象。按 root 指示拒绝锁题，不为一个可直接排除的 proper 类写新 formal 或登记结果。

## 3. Perron 非产品反馈：原 common-core 身份不能省

实际重新读本库 Fernández-Delgado–de la Salle **2607.14824v3** 抽取的 Proposition 4.1 完整 induction（原 PDF11–12 对应段），并与 R41 §§4、6、10 比较。R41 的确没有排除跨 node/跨坐标的 genuine feedback；不能声称“所有非产品 Perron 算法不可能”。但该源实际 induction 同时使用一个共同 \(P_{n-1}\)：
\[
 w_i=w^{(i_n)}_{i'}+P_{n-1}w'_{i_n},\qquad
 H_o^{P_{n-1}}(T_{i_n}+w'_{i_n}),
\]
借此才能把第二批漏出集合写成**同一 homothety 对一个 union**的像，再提出 \(P_{n-1}^n\)。给各 node 分别代入 \(P_i\) 后，这个等式已不是原命题。

一个直接的实际 core-containment 反攻是：原高度为 1、中心 \(o\) 在 base hyperplane，两个 child core 的比例为 \(P_1=1/2\)、\(P_2=1/4\)。它们的 apex 高度分别为 \(1/2\)、\(1/4\)。若以平均比例 \(\bar P=3/8\) 当共同 parent core，则第一 apex 在其高度范围外；源允许的 horizontal translations 不改变这个矛盾。必要的共同高度比例至少是 \(\max_i P_i\)，不能由平均 shrink 预算免费替代。

这反的是一个具体偷用原 induction 的接口，不是所有 adaptive algorithm 的 volume lower。若仍把每条 direction path 的残余 core 与各次漏出按非负数 \(x_j\) 求和，\(\sum x_j=1\) 的 Hölder 障碍逐 path 就已是 R41 的旧闭包；不把这句改叫“自适应新障碍”。真正可能超出旧范围的算法须有**实际生成位置及新的交叠 upper**，同时保全部原 whole segments；本轮没有取得这种新 upper，故没有伪锁“反馈能省一幂”的主张。

## 4. 新 primary：固定版本、实际读取与采用层级

有界检索得到本库先前未登记的 Chen–Li–Li–Liu–Sun–Wang–Zhou，*Some constructions of restricted Kakeya sets*，arXiv **2609.06556v1，2026-09-06**。实际核[版本页](https://arxiv.org/abs/2609.06556)当前仅 v1；读[官方 HTML](https://arxiv.org/html/2609.06556v1) Theorems1.1–1.3、§3 的 \(D,E_n\) 定义与 compactness 段、§4 的中心关联、slopes 平移及最后拼接。作者声称的主要对象是指定中心集的零体积构造；未给高维严格 Hausdorff upper。高维返回实际包含自由盒乘积，不是本轮所需的不同主幂。

本稿所用新证据是下面针对原显示公式的代入核验，不采用其 irregular-set construction 的高级正确性，也不借第三方评论作为数学依据。随后实际读取 root 下载 PDF 的本地提取目标段：原 PDF4 的 §3 拼接及 compactness、PDF6 的 §4 新 slope-window 与 Hausdorff 拼接、PDF6–7 的中心归一化及 \(D_0=[0,1]^2\)。这些关键公式与 HTML 一致。固定原件为 [R0114_chen_li_li_liu_sun_wang_zhou_2609_06556_v1.pdf](../../literature/primary/R0114_chen_li_li_liu_sun_wang_zhou_2609_06556_v1.pdf)，10页、336056B（页数/字节由 root 实际下载提供）；本稿不声称逐页视觉审查、wholeproof 认证或自行哈希核验。

## 5. 共 clock 与准确单位段：原 §3 compact 公式的实际测试

源 §3 使用紧参数 \(D\subset[0,1]^2\)，第一坐标投影为 \([0,1]\)、第二坐标为给定中心集 \(A\subset[0,1]\)。原显示的 slope 拼接为
\[
 E_n=\{(a,0)+t(b,1):(b,a)\in D+(n,0),\ |t|\le1/2\}.
 \tag{1}
\]
任取 \((b_0,a_0)\in D\)，真实点
\[
 p_n=(a_0+(b_0+n)/2,\ 1/2)\in E_n
\]
随 \(n\to+\infty\) 无界。因此该原公式的 \(\bigcup_n E_n\) 即使添一个 bounded horizontal segment，也不可能 compact。这不依赖 \(D\) 是否 irregular，不是有限采样猜测。问题是把 vertical clock 的长 1 与 arclength 的长 1 混用：该方向的段实际长度为 \(\sqrt{1+b^2}\)。

此项本身可修。若把 (1) 改为
\[
 \widehat E_n=\{(a,0)+\tau (b,1)/\sqrt{1+b^2}:
                 (b,a)\in D+(n,0),\ |\tau|\le1/2\}, \tag{2}
\]
则每条是准确单位段，并保原中心。若 \(D\) 紧且第二投影为 compact \(A\)，(2) 的 countable union 加上 \([-1,2]\times\{0\}\) 确实紧：\(n\) 有界时取固定有限 index 和 compact 参数子列；\(|n|\to\infty\) 时 vertical 坐标趋 0，horizontal 坐标始终在 \([-1/2,3/2]\)，极限落在添加段内。horizontal 单位段亦可在添加段中以 \(A\) 中一点为中心取得。所有非水平 slopes 由 \([0,1]+\mathbb Z=\mathbb R\) 覆盖。

若原各 \(E_n\) 零面积，(2) 只是其真实子集，故仍零面积；但此处没有独立认证该前提。这个有限修复说明不能由 (1) 的 compactness 失败宣布主定理 false，更不能据此声称严格低维反例。

## 6. 非共线中心的生成关联：只改单位 clock 仍不修

源 §4 的有限构造是中心关联
\[
 (b_0,\alpha)\in D_A,\qquad
 \alpha=x-yb_0,\quad (x,y)\in A,\quad b_0\in[0,1]. \tag{3}
\]
其后为覆盖新 slope window，显示定义要求
\[
 b\in[n,n+1],\quad (b,x-yb)\in D_{A_n}+(n,0),
 \quad (x,y)\in A_n\subset A. \tag{4}
\]
原构造从 \(D_0=[0,1]^2\) 作递减紧集，故每个 \(D_{A_n}\subset[0,1]^2\)。同时只平移 \(b\) 不保持 (3)：若 \(b=b_0+n\)，同一实际中心要求
\[
 \alpha_{\mathrm{new}}=x-y(b_0+n)=\alpha-ny, \tag{5}
\]
而 (4) 保持旧第二坐标 \(\alpha\)。这是原 **joint center–direction incidence** 的改变，不是 Lebesgue/维数换名。

可用完全明确、符合源归一化的中心集检验：取圆周
\[
 A=\{(1/4,5/32)+(\cos\theta,\sin\theta)/32:
                  0\le\theta\le2\pi\}. \tag{6}
\]
它 compact、perfect、非直线，包含源举作归一化起点的 \((1/4,1/8)\)，且处在源指定的 \(0<y<x<1/2\) 区域；有
\(x\le9/32\)、\(y\ge1/8\)。对每个 \(A_n\subset A\)、整数 \(n\ge3\) 及 \(b\in[n,n+1]\)，
\[
 x-yb\le9/32-3(1/8)=-3/32<0. \tag{7}
\]
但 \(D_{A_n}+(n,0)\) 的第二坐标仍在 \([0,1]\)。故 (4) 对这些新 slope windows 没有**任何**生成见证，所显示的 \(E_n\) 全空。这一代入不依赖 \(D_{A_n}\) 的 irregularity、所选 nested \(A_n\)、面积估计或 limit 顺序。

只把 clock 换成 (2) 的准确 arclength 无法修 (7)。若保每条 center 标签，须在联合参数上作 (5)；\(y\) 通常不是单凭旧 \((b_0,\alpha)\) 可恢复的统一值。另一选择是直接在新 slope window 重建 \(D\)。这两种修复均须重付实际 center incidence 和所需零面积/irregular 输入，不能直接重用“平移 preserves irregularity”这一个旧声明。

本稿只否定所显示的生成 transport 及其当前 proof 用法。没有分类物理集合意外包含的其他 lines，故不声称已经构造了主定理的反例，也不以缺所需生成 witnesses 推出所有修复都不可能。源的中心限制定理可能另有正确证明；本轮未提供该完整修复。

## 7. 高维、有限输入与 restriction 的真实费用

即使上述来源完全修复，其高维出口使用一个平面 Kakeya 集 \(P\) 乘自由 \((n-2)\)-盒。已有平面 Kakeya 定理给 \(\dim_H P=2\)；取 \(s<2\) 的 Frostman 概率乘盒内 Lebesgue 概率，球质量为 \(O(r^{s+n-2})\)，故该高维集合维数为 \(n\)。这不是严格低维反例，也不是新的普通有限 gain。单纯零体积没有所需 fixed-power cover upper。

有限源若使用很多整数 slope windows，还必须按真实角度计数：\(\theta(b)=\arctan b\)，其导数为 \((1+b^2)^{-1}\)。在 \(b\asymp B\) 的 window，slope 网距 \(h\) 只给角距 \(\asymp h/B^2\)，不能把相同 slope label 数免费当成共同 \(\delta\)-角分离原 \(N\)。单位 arclength 修复又改变各 window 的 vertical-clock 长度；必须使用真实单位参数或实际 marks，不能把小 vertical 高度误算成删掉绝大部分单位质量后的无费收益。

原 restriction 始终按 \(N'=qN\)、\(I'=pI\) 收费，平均 \(\lambda'=(p/q)\lambda\)、概率 cap upper 除 \(q\)；逐管 density 另核。保 whole generating labels 可保各该原单位段，不能在丢失 window witnesses 后仍称 full direction。删 clock marks 不保全段；取闭包也不免费保严格 Hausdorff upper。本文没有通过限制 \(A\)、样本有限化或给旧 \(D\) 添任意联合中心 law 绕开这些责任。

## 8. 本轮判定及唯一可负责的后继边界

本轮实际执行了两个不同的几何反攻：Perron node-dependent core 不能以平均比例代共同 homothety；新 restricted-center 来源的整数 slope 平移破坏原 center incidence，且有 (6)–(7) 的具体合法中心集见证。另将易修的原 whole-clock compactness 公式与其有限单位段修复分开。它们改变 source 是否可采用的决策，不是新的 ordinary 下界、严格低维构造或重大结果。

对真实反例出口，目前尚无保全方向单位段、同一集合和 strict Hausdorff upper 的 qualified 新机制。Perron 真跨 node 反馈未被本稿全排，但也没有一个可实际执行的新交叠 upper；不把“还需 joint overlap”另起名称登记为下一定理。scalar-J proper 类按低维输入闭包拒选，R41/47/83/93 冻结范围均保留。

root 统一安排实际独审、文献库元数据、公共状态与同步；本稿已完成上述 PDF 提取目标原式与 HTML 的比对，不预认证其余后续步骤。完整长期 Goal 保持 active。
