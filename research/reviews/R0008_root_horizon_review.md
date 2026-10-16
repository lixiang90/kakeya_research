# R0008整合独立复核：完整模型的高horizon

2026-10-17。root复核三份R0008笔记；prior/profile另经lifting_obstructions独审，spatial cap另经audit_four_dimensional独审。horizon floor与显式upper稿由literature_frontier逐定义独立推导，本文件逐步核验其HF3–HF8。未经外部同行评审，不声称新颖性。

## 原始模型与几何接口

visible系数是同一均匀δ-grid先验加六维独立U[-δ,δ]噪声，index概率约δ³；不能误用R7的反例权δ^1/2。完整visible block与隐藏C,W三组独立，B,V内部经index耦合。finite Cantor直接有分段常Lebesgue密度，未再作破坏piecewise-constant性的卷积。全8维pieces数、高度、倒尺度是固定N幂。

固定内层t时，near-Y grid计数Oδ^-1、单noise density Oδ^-3与index权δ³给g_t≤Cδ^-1。quadric厚度约δ给支撑volume≤Cδ；小density sampled质量≤C/K由积分得出，不声称所有支撑点lower。隐藏bin的upper与occupiedcount分别证明，合并给n(r)≈log δ^-1 a^d。角cap r≥δ与r<δ计数分别给joint上界Cδ^-1r，乘隐藏bin上界得S=1。原定义不限制f(0)≥0。

root独核全宽度cap：固定index与u-noise后，rotated bnoise只需joint-density而非坐标独立；薄轴概率∏min(1,w/δ)对所有index统一。能命中者的无noise格点迹线必落扩大P，各宽max(w,δ)，乘两界逐轴抵消。超宽轴以有界参考轨道为center裁剪；短块外推至全时各宽乘3/q；SVD给原J乘K³，不换成放大J。

## 任意二次test与真实floor

固定一个chart后，其P是固定多项式。固定visible trace与t，P(t,Y(t),w)为一元degree≤2；选中small-value/derivative条件把w限制在至多两个区间，总长≤4K²a。原C+tW法则具有平移统一Frostman upper，故原隐藏概率≤CK^{2d}a^d（或逐bin粗界CK²a^d）。assignment可以复杂耦合，但把它扩大到完整visible spatial-fit事件后，在原product prior积分仍得

m_c/q≤CK^C a^d ν_vis(P_I)≤CK^C a^d δ^-1/2q^-3J。

源定义真实floor是m_c/q≥K^-1 n(r)J，B在此原problem固定1。代入n(r)=δ^-1a^d并约去正a^dJ，得q³≤CK^Cδ^1/2。因此每个非空true packet都满足h≥M/6；不依赖label总数，也不把选中时刻空间条件冒充完整assignment的全块条件。进一步inverse-subpower选择保持支配与profile指数，任何subsequence仍受同界。

## 直接upper与定义范围

q=δ时，每个midpoint可见支撑在光滑二维surface的Cδ邻域，故δ-cells数≤Cδ^-2；这一步使用Lipschitz图，非仅支撑体积。每cell概率≤Cδ²，删除质量<τδ²的cells至多失Cτ。goodcells×原c的a-bin有完整prior质量约δ²a^d，与J约δ³、n(r)约δ^-1a^d相配。native test w−c_C、空间矩阵CδI、整块incidence满足全部定义，覆盖常量；current exactY及bounded V给midcell O1列表，current w-bin给c-bin O1列表。不可观察grid index不输出。编码count与inverse宽度都固定N幂。

故终端真实系统存在，M/6≤H≤M。取L1/M12给2≤H≤12，真正反驳formal j3 H≤L，不是因为真系统集合空。profile与S1也核完，故此反例位于literal j3 cap-class数值条件中；它不是原论文实际j2版本的反例。

完整raw(V,W)密度不具subpower来源，visible slopes亦聚在代数薄层。没有全方向Kakeya集合、新维数下界或major-result认证。停止优化此模型，后续须回到真实source方向约束。

## 下一任务的单位复核

audit_four_dimensional另只读复核HOR-001与下一轮spec，指出物理visible-slope密度A的目标应含δ³；原草案漏项会成为平凡time计数。已统一为每δ方向bin质量≤α时Σω#J≤Cε αδ^-ε#E；实际Lebesgue密度A可推出α=C Aδ³。原子方向律只有bin cap，不与实际Lebesgue密度界等价。

检查满方向均匀概率(A≈1、α≈δ³)、单线质量m(α=m)及R8可见model(A≈δ^-1、α≈δ²)均量纲一致。任意大A假设本身不排除R8，只有subpower ceiling排除，或目标明确支付大A。旋转复制后SRC-001的方向丰富度、逐线marks和union控制能否同时保持仍是下一轮实质任务，不在本轮预先声称。
