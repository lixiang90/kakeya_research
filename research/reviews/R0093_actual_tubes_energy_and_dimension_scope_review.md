# R0093：真实管族、能量与维数范围独立终审

2026-10-18，B。内部有限范围审查，**未经外部同行评审**。本轮是经典投影阻碍的原单位线段接口核验，不含新维数界、完整source反例或major。

## 1. 实际全文对象、来源与独审分工

已实际全文读终root主稿`R0093_robust_projection_and_actual_unit_segment_scope.md`十节、A稿`R0093_robust_projection_source_and_closure_gate.md`八节、两spec各五节，及终macro/next/source-scope各六节。root最新§5非空chart、§7有限footprint耦合及§8 actual参数域均已fresh读回。自身B gate八节不计作独立审查；以下正式意见主核root/A的推导，自己的构造由parent/A独审。

另实际读库存Orponen2008.08843v3提取文本physical1–5：Def1.2、主Th1.6、经典Cantor讨论、Question1及Grassmann metric/常数规范。正确入口是closed全尺度regular＋PBP，不是BP；(1.3)是式号，单ball问题不是已证局部版。实际读Lang作者讲义§10 Th10.6及proof、Th10.8和Examples10.9–10.10；最后另读回root/source的具体citation并实际读库存Th8.3面积公式statement（physical21–22），适用于本轮实际可测Q。接受这些标准具名工具，未新认证Orponen全部40页、Lang全部35页或BF高级证明。没有把served版本日期、档案字节或官方身份当数学正确性保证。

## 2. 联合AD、每球固定BP与纯不可整流

数字和的四种值0、1、2、3唯一且无carry，确给`A+B=[0,1]`和自然概率的Lebesgue像。F有四个ratio1/4分离副本，F^4有256个；层质量`4^(−4k)`及层间距给真实4AD，不只是维数上界。L为√2相似，故Z有限正H^4、自然测度与H^4|Z可比。每个球包含一个同尺度完整副本，其v像为四维cube，故同一π_v在每个球内都有`≥cr^4`投影质量；bounded slope chart的方向图亦保真实四维angular质量。

纯4证明完整：0及八个坐标轴端点affinely span R8，任意affine4-plane不能同时靠近九点；AD lower把一个远点升级为固定比例远plane质量。每个层副本缩放同一证书，在趋零半径上统一排approximate4-tangent。若有正H^4 rectifiable交，取该交集的相对AD密度一点和rectifiable切点，rectifiable部分及其补集的远切面质量都应为o(r^4)，与证书矛盾。不是仅从全Z没有切平面便无解释宣布纯性；d=1同理给F纯1。

于是BF给Haar-a.e.四平面投影零，任何Grassmann开邻域都含这样的plane，PBP确失败；纯4也直接排positive-H^4 Lipschitz graph piece及BPLG。此与一个固定π_v满cube完全相容。Orponen前提缺失不是调用其定理后获得的新维数结果。

## 3. 有限AD、真实单位clock与whole-containment CW

δ=4^−m截断后，方向v恰为四维δ-grid，每v唯一数字分解、N=δ^−4；联合计数在r≥δ有`≈(r/δ)^4`，r<δ没有连续AD lower。归一化Θ(v)在cube上bi-Lipschitz，给固定常数δ分离和δ-cap有界重数；如需字面单位常数的δ分离，只改固定层子网/尺度，不能把此常数问题升级成质量缺口。

真实段终time`L_v=(1+|v|²)^−1/2`使其arclength恰一，且共同包含`[0,1/√5]`。compact参数域的连续像给K compact。它最初供应一个open angular patch；有限physical rotations的同一个有限并可补齐S4，所有原段仍完整，不能把一个bounded slope chart本身声称为全S4。

John证明已付：先以包含所有原管的固定ball截凸W；若有contained管，所有半轴ρ_j≳δ、ρ_1≳1且有固定upper。在每个实际非空sphere chart，`|θ_i|≥c`及`|θ_i|≤Cρ_i`迫ρ_i≳1。故四坐标packing面积可由`C∏_(j≥2)ρ_j`控制，再以ρ_1≳1比较ellipsoid体积，得到`#{T⊂W}≤Cδ^−4|W|=CN|W|`。已读回主稿明确非空chart条件，未再仅用排序作不成立的中间比较。该结论只是convex whole-containment，不赠partial-intersection/fullPW、small-footprint或Def17其余假设。

## 4. 零体积、满Hausdorff维与有限whole-footprint

对每个t，K_t⊂C_t^4；仅在共同clock内部才等于完整product。F的finiteH^1/pure1符合BF，系数方向`(1+t,t−1)`随t的角变化非退化，因此a.e. t有L^1(C_t)=0。K compact，Fubini给L^5(K)=0；有限旋转仍零体积。这不是Hausdorff严格低维的结论。

主稿满维链不依额外Marstrand输入：1AD给I_s(μ_F)<∞，s<1；差向量置a=dx−dy、b=dx+dy后，b小则线性式远零，b不小则换元积分，确有`∫_I|a+tb|^−s dt≤C_s|(dx,dy)|^−s`。Tonelli及可数s↑1给a.e. t投影维数一。四坐标不等式`|w|^−4s≤∏|w_i|^−s`给product energy有限、slice维数四。球cover的slice费用对t积分≤CΣr_i^q，选可求和cover序列即给标准slicing结论；取dim_H K<q<5矛盾。因此K及其full方向有限旋转并均为Hausdorff五维。

K_m⊂K且整unit段的归一参数化在bounded域Lipschitz，故`d_H(K_m,K)≤Cδ`，包括可变终time。δ-separated最大网的固定倍邻域体积比较给`|N_δK|≤C|N_δK_m|`。所以有限whole-tube并虽体积趋零，也不能沿小δ序列有固定δ^c upper；否则原K同尺度cover会迫维数≤5−c。此处不是从K_m⊂K倒推体积lower，更不排任意partial shadings另有小footprint。

## 5. 条件整流出口、密度闭包与强制修正

主稿§8条件出口合法。Z′ Borel、有限H^4且countably4-rectifiable，遗漏的H^4零集之v像为零；正方向像迫一张chart在**实际映入Z′**的参数域中有positive measure且detDv≠0。可取有界可测Q（按零集修订可取Borel）保该性质。`Φ(q,t)=(a(q)+tv(q),t)`在该有界域Lipschitz，5-Jac为`|det(Da+tDv)|`；非零最高项detDv使每个好q至多四个根。面积公式只用于Q×原公共clock，其像在原并中，正Jac积分确给正五维体积。没有将延拓后整像误计为原集合。

一块BPLG graph的base未必是v平面、其v像可为零；root的countable全覆盖及actualQ补齐这个责任，A提出的方向graph分解仅作标准条件解释。该定性出口不给随δ统一的体积常数，也不自动返回原shading。λ=1时免费PBP桥已失败；任意label/shading删选虽保相应upper，不保AD lower、全方向或整流性资格，平均和逐管的原质量责任不能互换。

当前无未解决强制修正项。root非空chart补句、有限footprint耦合及实际有界Q范围均已核；B gate已按parent建议明确有限δ投影指其thickening的Leb4，而非finite点本身H4，并把slicing的q明确取大于max(1,dim_H K)。高级输入和项目具体推导分层清楚。本文未构造完整critical source的filledX、pointΦ、selectedξ/coherence或原small-footprint条件，不能把此例当其反例。

## 6. 限定终审结论与停止范围

在上述实际全文、标准切平面/BF/面积公式及具名Orponen范围内，**全文通过**。真实联合AD、local固定BP、unitclock和convex CW仍不授PBP；真实并集零Lebesgue但满Hausdorff五维，非Kakeya维数反例。正向rectifiable参数出口也只在其明列条件下通过。

终macro/next/source各六节已实际全文核：经典模板地位、无newID/major/ordinary新增益/fullbranch saving、保守streak16、Goal active及四完整路径保持一致。停止BP→PBP的数字/角邻域/密度续轮，不宣所有整流性方法失败。仍**未经外部同行评审**，不新认证全部高级wholeproof或74PDF/78sources/78IDs档案，也不预认证未来metadata、Git、验证或同步。按授权至此停止编辑与检索。
