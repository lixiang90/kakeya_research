# R0116 后继选择审查：Dahia 小覆盖的真实启动责任

2026-10-26，algebraic_gate。只作后继准入审查，不启动 R0117；不改已完成的 R0116 主证明、独审或同步。恢复 context、GOAL/STATE/ROADMAP/registry 最近项，并读 R114 whole-cell 主证和 R116 新 primary 稿。当前目标仍是超出六维 Hausdorff 17/4，ordinary 五维或完整 source 无新正 gain。

## 1. 实读的新输入究竟是什么

本次读本地 [Dahia v1](https://arxiv.org/abs/2610.18859v1) 提取全文，重点物理页 2–4 的 Lemma 1.2、Theorem 2.1/2.2 和 cover proof；版本 2026-10-13，5 页。使用已归档 PDF/text/metadata，没有新下载，也不声独立重证 Green–Ruzsa 原论文。以下把源文的整数密度 δ 改记 ε，免与管宽混淆。

固定 k≥3、ε>0，Lemma 1.2 给事先固定于 [n] 的有限族 F：

    log #F <= n^(1−c/loglog k)+O_k(log n);
    每个 |S|>=εn 含某个 F∈F；
    每个 F 有至少 γ(ε,k)n 个 k-AP differences。

这里的 cover 是 contained certificate，不是“少量实体覆盖 S”或“捕获固定比例原 incidence”。证明先消费 Green–Ruzsa 的已知构造：Y⊂[C(k)n]、|Y|≤n^(1−c/loglog k)，每个 d∈[n] 已在 Y 中有一个指定 P_d。Varnavides 再给 dense S 至少 ε_AP(ε,k)n² 个 AP；按平移参数 t 抽屉，得 F=(t+Y)∩S 有 γn 种差分。编码量来自平移选择与 Y 的任意子集：O_k(n)2^|Y|。

所以两个先付输入是 **稀小的通用模型 Y** 和 **固定密度下的 AP 超饱和**。γ、充分大 n 的门及随机定理的 C(ε,k) 没有本项目可用的 ε=δ^η 预算；k 固定也不能当作长约 δ^-1 的整个单位段。源证明不供物理方向、原 T/N/I 或 marks 的相应平移计数恒等式。

## 2. R114 对非固定格式的准确作用

测试原类应为：真实 R5 单位 δ 管全方向 δ-net，N≈δ^-4；任意原 marks Y(T)，I=Σ|Y(T)|，λ=I/(Nδ^4)≥δ^η。平均与逐管门分别声明，不能靠“prototype”一词省略 q、p 和 λ'=(p/q)λ。

非 fixed-format 本身不被 R114 否定。若候选实体族 H_1,...,H_L **在 mask 前已固定**（允许依原整管 T，不能再依筛后的 marks 任意重选），同一随机和的 finite union bound 只把 R114 的 log K 换成 log(2L)。multiplicity 层 A 的 V=|A| 给归一绝对误差

    r² <= C δ^5 log(2L)/V
       <= C δ log N log(2L)/λ.

若右端趋零，其“同体积 fixed C 实体捕获 θI”规则仍受同一 whole-cell mask 压力；不是由于实体需半代数。若只在 power-small-footprint 反设内声该规则，且相同编码预算在合法删选后仍统一成立，它已承担相应 finite 排除责任，不能当免费初始化。这里引用 R114 的闭包计算，不新开 mask 参数轮。

反之，log L 超过此预算、C 随 λ 恶化、或族可按筛后 marks 自适应时，以上反攻没有覆盖它；不能宣一切有限 prototype cover 都与原 Goal 等价。Dahia 本身也没有给这些类的几何 cover 定理、编码预算及原 I 捕获。若仅保“有很多方向证书”，则还须另付这些证书对原 I 的 domination，不能套用实体 carrier 的否定或增益。

## 3. 启动判定

**目前资格 0；建议不启动“用 Dahia 建 ordinary prototype cover”作唯一主轮。** 字面模仿若先要求一个具有各方向非短整段的 power-small Euclidean Y，已经要求实际 Kakeya 小集构造；若只要 fixed-k 点模型，则没有回到单位管、λ 和 Hausdorff 的桥。另行假设“原 small footprint 自动给一个小编码、保 I 的 cover”，又可能已消费上节欲证的 finite 排除。不能把任一者写为成功 hyp 后将余下 union bound 当作新机制。

重开至少需要事先明确不同于上述两种循环的 **模型来源、编码预算、ε→0 常数和原 I 返回**，并在真实原对象上证明其中一项；本轮没有这种输入。未被 R114 反驳不等于已获得准入。

## 4. 更原生的一项待执行证伪测试

若必须锁一个下一任务，建议先检 **原 near-full marks 是否强制具有中等 clock 间隔的同轴 3AP 超饱和**，而不预设 prototype。精确试验是：先固定 0<a<1，任意足小 η；对上述全方向真实单位管，甚至要求每管 |Y(T)|≥δ^η|T|，是否能强制在原 marks 的轴向 clock 中出现间隔 h≥δ^a 的 3AP，并有可返回原 I 的统一正幂数量。它直接检 Dahia 所需 supersaturation 在原 λ 门是否还存在，不涉及 codec 或 exact-entropy 精度。

一个可实际落到全管的攻击配方是：在每根原管自身单位 arclength clock 用同一 AP-free 整数格集合的短区间并作 marks，横截面保原 δ 宽。可用无进位整数球层：固定大维 d，取 {0,...,m−1}^d 的等平方范数层，在 base 2m 编成 [n]（n=(2m)^d）；抽屉给至少 c_d n^(1−2/d) 个点，严格凸性排非平凡整数 3AP。将每格只加厚 c/n，c<1/4，任何真实 clock 3AP 的格指标必须仍是整数 3AP，故间隔至多 c/n。选 d>2/η 后，δ=1/n 的逐管密度仍超过 δ^η，全部方向、原 N 和单位轴保留。下一任务应独立核这一真实 round-tube、dyadic 子序列、端点及原 I 账后停止；这里不预认证为已审结果。

这个测试即便成功，也只排掉一个 **无条件的宏观 AP 预处理**，不产生 small footprint，更不否 small-footprint 条件下可能新增的几何联合信息。若后继只把这一经典 AP-free 配方调常数或换名，应直接停止，而不再延长为主研究；下一正机制仍须来自原方向与空间重叠的共同约束。
