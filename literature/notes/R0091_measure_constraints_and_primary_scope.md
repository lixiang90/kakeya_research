# R0091：微分约束、normal currents与可测选择来源范围

2026-10-18。以下是已有primary/标准工具的首次正式项目存档与应用核，不是2026新发现或新Kakeya结果。

## 1. DPR版本与原始文件

[De Philippis–Rindler official history](https://arxiv.org/abs/1601.06543)：v1 2016-01-25，currentv2 2016-04-11；[原PDF](https://arxiv.org/pdf/1601.06543v2)实际18物理页/274624bytes，SHA256 bddc75f09d5f4b294d08a5916cbe9fe1eba842ac42dff6a164c8319275fb81ac，blob fee3b3571bfc9ab2818538ac86efb45585c30187。abs17页/HTML重编Date不替原文件版本或物理页数。

root实际读原PDF1/2/4/5/13–15，以及HTML Th1.1/Remark1.3/Th1.10/Cor1.12–13相应应用；view physical5。主§2全PDE proof没有新独证。A/B具体阅读在各gate/formal，不以作者署名或应用核宣称wholeproof正确性认证。

## 2. DPR实际被采用的唯一出口

Cor1.13允许矩阵测度的row-Div为有限测度，奇异部分的polar秩≤d−1。项目实际证明全线段S满足前提，且PSD trace使|S|与μ可比。Remark1.3有限RHS不能漏掉。Cor1.12所需同一measure及局部独立方向未由global I5/5提供，不能借文献结论省去原输入。

## 3. AMS版本、页数与实际使用范围

[Alberti–Massaccesi–Stepanov history](https://arxiv.org/abs/1907.07456)：currentv3 2022-11-21（v1 2019-07-17/v2 2020-04-16）。[原v3 PDF](https://arxiv.org/pdf/1907.07456v3)实际27物理页/366293bytes，SHA256 f5a93eba03d4f5bab76d40c6407802e81cf2b3db23af8da3a889cd8f9c5a87f1，blob c789c50ab6f973996e287a657ac7299d1770a671。期刊JDG122(1),1–33页为不同版式，不写成本PDF33页。

root实际PDF1–3/6–7及§2.11–2.16提取文本，view3/12（后者核原文字而非仅提取）；B另实际§2.10/2.12/2.14和§3接口。采用其Th1.3的**前提筛查**：C1 plane distribution和真实normal k-current，未将高级wholeproof或其新Kakeya应用认证。normality在本项目始终以current与boundary两mass有限的定义及直接计算判断，不依赖§2.11(iii)对一般L1 density所写的过强iff；例如e1·1_{x1>0}L5在有界open box有finite surface-measure边界而div非L1。该局部文字问题不被升级成主定理已否证或项目新重大结果。

## 4. Moore作者讲义与标准选择定理

[Justin Moore, MATH7870 author-hosted notes](https://pi.math.cornell.edu/~justin/Limited2Cornell/DST_lecture_notes.pdf)为unversioned作者PDF，本次83物理页/521467bytes；SHA256 ea1b32718ef99df21f5f1c126c8ee19cccabd12514f3030587e30e13ef9bfde8，blob d9a77cd78393103d250f6f018e552088559345dc。PDF metadata CreationDate2019-01-23不是已核出版日期，网页crawl/date也不当研究新版本。

root实际读47–48 Th49及证明文字，view47；采用标准JvN的analytic关系universally measurable selector声明。原讲义证明中composition等排印失误未逐条修订，不冒whole83页证明认证。项目自行核关系Gδ/满投影、同维hull、完成σ的Borel版本及Radon carrier，不声称一般Gδ关系有Borel uniformization。B额外有作者Bertsekas appendix statement比对，仅其独立阅读记录，本项目证明不依该额外版本。

## 5. 与原四维paper及旧结果的边界

本轮fresh official OpenAI main ref/canonical tree核与此前不变；最后实际三核心整bytes检查仍R75。本轮不重称wholePDF byte identity或数学正确性已新认证。δfinite marks/filledX不是连续normal3-current；可测kernel不授C1场。R90polar端点、R89cut、cone与跨块旧责任不因本轮新文献名称解冻。没有一手比对支持的重大/新颖声明。

## 6. 归档、独审与结论

三原PDF未修改；default pypdf extract_text逐物理页标记，规范控制字符/行末空白，非layout提取。现69PDF/73sources/78IDs。root主文10、两gate8与后续两formal6区分来源具名输入、初等构造及未付出口，未经外部同行评审。任意K资格和若干免费桥反攻已得；无ordinary维数增益/fullbranch saving/真正低维full方向反例/新ID或major，Goal active。
