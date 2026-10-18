# R0083：原直线族测度、维数阈值与删选类型终审

2026-10-18，A。内部正式审查；“通过”只认证下述输入匹配、应用代数及停止范围。未经外部同行评审，不是两篇高级 wholeproof 的新独证，亦非新高维维数界、major 或未来同步认证。

## 1. 实际全文对象、来源读取及独立分工

已 fresh 实际全文逐式读终版 root《R0083_direct_line_union_input_gate》九节、A《R0083_Zahl_line_union_input_audit》八节、B《R0083_HKM_Fubini_and_restricted_projection_input_audit》八节、working_spec 五节、source scope《R0083_direct_line_union_sources》六节、终 macro 六节及 notes/00_map/R0083_next_full_goal_reselection.md 六节。没有用 root 预期通过或旧版阅读代这些当前对象。

Zahl2208.02913v1：本人已实际读官方 abs/history、HTML 全文及本地八页正文，包括 Th1.2、§2和完整§3应用；只读核其本地 PDF bytes/hash/blob，与 source6 的记录一致。前述 A8 是本人主要施工，不算自身独立审查；已由 root/B 对实际量词、应用代数及范围另行核查。

为独立核 root/B 的 HKM 声明，本正式终审又直接完整读本地 HKM2106.09661v3 提取文本的§2起至§3末（PDF3–10），含 definitions、主定理 statements、3.1/3.2 全部应用 statements/proofs、Conj3.11/Th3.12 证明及3.15–16证明。A8此前“本人尚未新全文读该段”是其成稿时的历史状态，现只在本formal记录新增实际读域，不改冻结文件。HKM§5–7与Appendix主证明仍未新全文读或独证；没有冒HKM原PDF视觉/字节或官方history的新核。

## 2. 原 compact fibres、可测选择与实际 angular mass

独核 root 的 nested compact-fibre construction：π:C→RP5 连续满射；每层在已选 compact 前缀中用更小有限闭球cover，选首个与该 fibre 相交者。可行方向集是固定 compact set 的 π-image，因而 closed；首次可行 index 的事件为 Borel。嵌套 witnesses 非空、直径趋零，极限 selector s 为 Borel 且 πs=id。它并不连续，也不授 R82 已否的任意正质量 Hölder 抽取。

推 angular-uniform σ 得 ν=s_*σ；任何 canonical line-space ball 只投进半径 Cr 的方向 cap，故 ν(B_L(ℓ,r))≤C r^5。原方向满射也由 Lipschitz projection 给 dim_H C≥5。这是真实原概率 upper，不是 ADlower、support全部C、position-angle独立或更高 exponent。对正 angular 子集归一会付其质量分母；closed restriction保紧致/不交但不必满方向，measurable正质量 restriction亦不必紧致，三者未混同。

原真实方向上可抽 fixed-multiple-δ separated net并为每个direction选原line，给相应 finite line-space球count upper；这只是合法删选得到的新finite族，不能把原所有label称方向分离。compact offsets允许固定physical缩放及取真正整线内的unit pieces，无需segment-extension猜想。δ-neighborhoods仍可大幅overlap，不从整线不交赠 tube disjoint、PW/CW 或 endpoint inverse 模量。

## 3. Zahl：完整 threshold、finite density 和不能放大的 entropy

canonical projector metric与 source 的 nearest-offset加unsigned wedge metric可比。Th1.2 的 finite输入是 unweighted tube集合的 line-space球 upper，s=2(d−1)+β、d<n整数、β∈[0,1]；输出 p′=q=d+β。源集合结论的 d≤n 与有限版 d<n 是不同合法范围，当前 d=3、n=6 无端点问题。r≥δ 是非空离散计数的自然范围，literal r<δ、RHS<1不作为有意义的原子假设。

以 V=Σ|T|、λ=Σ|Y_T|/V，(1.3) 与 Hölder 真给

    |∪Y_T|≥c λ^(d+β) δ^(d−1+(d+β)ε)V。

它使用重新计算的平均λ；保整label及其全部Y时可继承原逐管lower，进一步削shading则不免费保逐管。源码§3经 common Hausdorff-cover尺度、原概率质量分层/抽样及逐line polylog长度下界，才从finite式回到Hausdorff维数；不是单尺度邻域或packing的替换。本人实际读完整路径，但未把源中 r≈δ 的 sampling简述/全部constant重新独证；高级CV仍具名，不因字面简述声原主定理反例。

n6原输入只达s=5，d=3、β=1给并集下界4；严格超过条件17/4需实际 dim_H C>25/4，得到5需dim_H C≥7。t∈[6,7]的相应输出t−2及所有阈值已独立代数核。finite count上界改用更大s会更宽松，但原 #T仍约δ^−5，不自动变成δ^−s；将d改4只能由同一N得较弱physical主幂，不能凭上界指数制造4+β。duplicated axes/纵向rawanchors也不能补canonical参数entropy。当前4不超既有四维/KT条件链17/4，后者仍保完整具名输入与非优先权认证边界。

## 4. HKM：直接核 statements、应用与真实删选范围

已对照原§2：ADregularity要求在 clock base T，而非 line labels；Γα-null测试每个Lipschitz graph上的base Hα零集。Th2.12/Cor2.13给的是删后 B\G 的维数等式，右侧为原sections的essential supremum；Th2.14给所有section共同upper下的删后upper。bounded nonvertical whole-line chart为Borel union，projection是全R clock，各line为全球Lipschitz graph，故此项确实可用，不是因假设不匹配而全盘拒绝。

独核 B/root 的自含校准：G0=B∩(Q×R5) 是 Borel Γ1-null，每条原nonvertical line只失countable clock，Tonelli也给任何Borel line概率ν与Leb clock的product零损；然而删后没有任何nondegenerate nonvertical segment，亦可删尽原dyadic finite marks。该例只否“Γ-null自动保整线/finite marks”的中间蕴含，不声HKM所选的特殊G必为G0或本例反其定理。closure可能回B但Hausdorff维数可能增加，所以这不是whole-label紧致子族restriction。

完整§3应用也核过：Cor3.4通过正measure compact clock set及Γ-null保持每plane正Hk质量，才反r(E)定义；Cor3.10要求参数dim≤1。3.16的graph-code/plane metric及compact approximation给a.e. Leb clock section lower s/(k+1)；当前k=1、s≥5只保并集≥1+s/2≥7/2，低于4及17/4。conjectural未删Fubini是原文Conj3.11，不能用已证删后等式代它。Th3.12是条件应用：固定m的猜想给Hausdorff≥m−1，所有m的猜想才给所有维度full upper-Minkowski；proof的projective missing-hyperplane/high-dimensional graph不能从删后等式无费恢复。此处只核原文status/逻辑，不认证2022以后全球文献中该猜想仍未解。

## 5. 独立反攻、量词闭包与高级输入边界

Zahl确授当前fullcompact C下界4，HKM确授相应删后/a.e.-clock输出；两项都是实际正面工具。未产生新gain不等于说假设均不满足。反过来，现有工具没有从不交/compact/fullD赠更高line-space Hausdorff维数、全line Fubini、同维closed恢复或finite-source质量。source sharpness例也通常不保原不交/全方向，不能拿它反完整C上任何未来更强定理。

KM典型Hausdorff n−1、packing2n−2的具名范围已分开，canonical quotient不增Hausdorff维数；原n6的5与10不能相加或互换。countably多族取Hausdorff sup、rawanchor重复和analytical enlargement亦不授dim≥7。generic clock/Grassmann结论不能指定为某个原singular time prior，也不解除既有Schubert非集中责任。任意positive-angular restriction的实际质量分母与原逐line/平均质量各自核算，没有从平均赠每line lower。

源输入的真实层级为：本人实际读 Zahl八页及HKM§2–3应用；CV endpoint、HKM主定理§5–7/Appendix、旧KM和RED/FSD/KT高级wholeproof均仍具名，不在本轮新独证。root/B的PDF视觉、HKM版本/bytes记录与我的read_scope明确分列。来源已发表或作者身份不代应用核查，也不把source6的计数/路径核验当数学正确性证明。未发现未解决的必须修正项。

## 6. 最终限定 verdict 与宏观/next 的实际读回

限定通过：root9/A8/B8的原输入匹配、可测angularlift及r^5 upper、Zahl threshold/finite entropy辨别、HKMΓ删选与一般投影输出的范围一致，应用计算没有未解决mandatory。自己的A8不算自身独审，已由root/B实际全文核；本formal独核root/B及直接原statements/应用。全部内部审查仍未经外部同行评审，不是完整高级source正确性认证，没有新ID、ordinary维数界、branchsaving、major或priority结论。

终macro6已实际全文读：原direct-line输入门按预先stop拒phaseII，立刻重比ordinary初始化/directHRZ/matrix-mixed全部κ/真反例；实际来源信息进展与保守主gainstreak6分开。C10仅总cycle与五点span4没有送distinct labels/clockgap/共享carrier及原mass，不锁gain，也不回R45固定endpoint；原κ<1不是因重读题名突然出现的新数据。无强行main或降低Goal的字面问题。

next6已实际全文读：当前诚实写尚无已锁/合格后继主命题；下一只先完整重新选择不同原几何量/原图或真实新source，取得责任前不补phaseII。它不再续两篇source abstract检索、endpoint/h/更多anchors、KT数表或把欲证jointmass/Fubini作公设，不声所有方法不可能，也不因难置blocked/complete。该scope无必修。本文不预认证未来metadata、Git、同步或尚未写出的结果；按授权完成后停止编辑检索。
