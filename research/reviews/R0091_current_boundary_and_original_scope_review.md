# R0091：current边界与原始whole-segment范围独立终审

2026-10-18，B。以下为内部逐步审查，**未经外部同行评审**。只审资格构造、具名定理的应用条件及明确的接口反攻，不认证ordinary增益或高级来源的完整证明。

## 1. 实际全文对象与独审分工

本次fresh全文读取root主稿`R0091_whole_segment_matrix_measure_and_current_exit.md`十节、A稿`R0091_transport_measure_and_source_gate.md`八节、working/reselection两spec各五节、终macro/next/source-scope各六节。另实际读取Moore提取文本physical47–48的Th49及相应证明文字。自身B gate八节的先前施工与源阅读记录可复用，但不将自证计作独立审查；本formal的独审对象是root/A的构造及整合。

Moore Th49的analytic关系Souslin measurable选择声明正合本次用途；原证明文字有composition等排印问题，此处采用标准Jankov–von Neumann定理，不声称修订或认证全部证明。DPR v2的finite-RHS/normal-current应用与AMS v3的C1/normal-current前提沿各gate实际读域核，未新独证DPR主PDE证明、AMS高级wholeproof或Moore八十三页。文献字节、归档数量与远端核验是parent记录，本人未另作下载、Git或元数据验证。

## 2. 任意原K、全clock概率和有限端点

同维包络合法：对每个`s_j=h+1/j`取足够小的开球cover，`G=∩U_j`含K；对固定`s>h`和固定尺度，令j趋无穷即得`H^s(G)=0`，故`dim_H G=h`。这不要求K先可测或有界。compact段包含于开U的关系对方向和anchor开放，所以段关系为Gδ且方向投影满S4，JvN适用。

全方向选择可取universally measurable版；相对完成球面概率，它有Borel a.e.版本。后者只保证σ-a.e.所选段在G内，已经足以保持严格球面方向边际、`μ(G)=1`和后续Radon概率。没有将此升级成每方向Borel选择、原非可测K内的选择，或`spt μ⊂G`。无界anchor不影响有限质量与compact-test计算，不需一阶矩。

对root的全unit clock联合law逐项核算：位置球clock长度至多2r，给`μ(B_r)≤2r`；joint球同时限方向cap质量`O(r^4)`，给`ν(B_r)≤Cr^5`。矩阵S为PSD、`tr S=μ`、总矩`I_5/5`。沿同一真实clock分部积分的符号正确，`Div S=∫v(δ_a−δ_{a+v})dσ`，总变差至多2。有限Borel测度在Polish空间的Radon性、Borel版本和条件分解为标准工具；此处没有把joint Frostman界投影成位置四维界。

## 3. DPR出口、normal-current前提和原source质量

有限endpoint RHS符合DPR Remark1.3/Cor1.13，不能误要求齐次`Div S=0`。独算row-Div主符号为`Mξ`，其wave cone为奇异矩阵。写`S=Aμ`，PSD及trace一给Frobenius界`1/√5≤|A|≤1`，从而`|S|=|A|μ`与μ等价；polar缩放不改rank。若`h<5`，μ由Lebesgue零G承载，具名结论确覆盖μ-a.e.且仅给`rank A≤4`。条件方向二阶矩的非负性给可变kernel的正交支撑，未产生共同固定四平面、C1法向或原四维全方向族。

A关于五个normal1-current的检查正确：必须在同一正质量测度上共同支配并局部张满，五个全局方向cones不付此条件。AMS的入口还需真实normal k-current、C1平面分布和相应non-involutivity；finite filledX及ξ/coarse coherence没有交付这些输入。root§9现明确“有限向量div不控制形式wedge的横向分布导数”，没有误说有界BV函数的乘积不保BV。B的具体wedge校准由root/A审查，不在此自计独审。

这些连续whole-segment概率也未提供原finite marks的N/I、共同局部质量或normal3-current返回。源scope不依AMS§2.11(iii)对一般L1密度的过强iff文字；采用normality的有限mass与boundary定义及直接计算，不据该局部文字宣布高级主定理失效。

## 4. 实体反攻与平均、逐管闭包

root径向bush和A中心bush各自的密度、全局`I_5/5`及局部rank一均独算正确。位置原点球质量分别为r和2r，故真实全方向wholeclock不赠位置四维Frostman或局部五方向独立；两例本身具有正五维体积，不能反small K或原Def17配置。

root四平面例的常数确为`1/320`：每Q_i四维面积16，`ΣP_i=4I`，于是总矩`(16/320)4I=I/5`、trace总质量一。交集四维零测，局部密度`P_i/4`为rank四；切向各坐标分部积分仅给有限面测度边界。A球面例亦有trace概率、总矩`I/5`、rank四及`Div S_sph=−ωσ_4`。这两者只反纯PDE/global-moment直接迫五维，缺原全部方向的whole straightline transport。

whole-label限制后未归一质量m、端点TV≤2m；归一后TV≤2，但joint常数付`1/m`、总矩改变，不能保全局ellipticity。任意shading则不同：每线半clock mask有`2m`个一维边界；root全方向radial例中原点项抵消，余`2m−1`个不同正半径球面互不抵消，故TV严格为`2m−1`，归一后为`4m−2`。此例同时有平均和逐管密度1/2；A的逐线趋满密度删小interval例亦不给uniform边界。因此两种density都不付uniform normality，whole-label闭包不能替换为任意clock删选。

## 5. 强制修正、依赖与未覆盖范围

本次终版未发现未解决的强制修正项。已实际读回root§9的有限div/wedge收紧，source关于载体与support、有限RHS、矩阵范数、Moore标准选择及高级wholeproof范围的区分，与正文一致。

通过依赖标准JvN、Radon–Nikodým/disintegration及DPR Cor1.13；AMS仅用于前提筛查，未调用其结论解决原source。没有认证原Gδ关系一般可Borel uniformize、bounded anchors、局部满秩、C1/BV、共同normal3-current、全R4方向或保marked footprint。三个反攻对象不能拼成同一full方向低维Kakeya集合，也不排一切current/PDE或多尺度机制。

## 6. 有限范围终审结论与宏观停止

在上述实际全文和具名依赖范围内，**全文通过**：任意原K同维归约、wholeclock矩阵及有限边界资格已付，DPR只到singular-rank的边界和具体免费桥反攻均正确。它是known-theorem application与资格完成，仍**未经外部同行评审**，不含新ID、major、ordinary改善或完整branch saving。

终macro六节与next六节均已实际全文核：保守streak14、拒phaseII gain、Goal active、完整ordinary/directHRZ/sticky余branch/真同集反例四路仍open，与本轮数学一致。下一不续global-moment/local-rank、未付normal3/C1或density-to-BV旧桥，不以困难充外部阻塞。本formal不预认证未来metadata、验证、Git或同步；至此停止编辑与检索。
