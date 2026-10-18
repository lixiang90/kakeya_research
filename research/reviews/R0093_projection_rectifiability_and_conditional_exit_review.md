# R0093：稳健投影、纯不可整流参数与条件出口独立审查

2026-10-18，A。以下为内部逐步审查，未经外部同行评审；不认证未来元数据、Git提交或同步。Goal仍active。

## 1. 实际全文对象、来源版本与审查分工

本次fresh实际全文读取当前主稿`notes/40_multiscale/R0093_robust_projection_and_actual_unit_segment_scope.md`全部10节、A gate `notes/00_map/R0093_robust_projection_source_and_closure_gate.md`全部8节、B gate `notes/00_map/R0093_digit_product_unit_segment_countergate.md`全部8节；另全文读取R0093 reselection_spec与working_spec各5节、macro与next各6节，以及`literature/notes/R0093_projection_rectifiability_and_classical_Cantor_scope.md`全部6节。B稿包括末节前新增的有限K_m逼近与邻域体积比较；主稿包括CW非空chart及第8节实际Borel参数域的最终修订，均非仅据旧版通过。

来源上，阶段I已fresh核官方arXiv history：Orponen 2008.08843 current v3为2021-06-21，正文June22不另算版本。实际读原40页PDF物理1–5完整定义、引言、定理、Question1与notation，本次以本地原文读回；阶段I另核Prop4.2的常数声明及§7.3收尾接口，未全文独证全部高级proof。准确入口是Def1.2、主Th1.6；(1.3)是BP不等式，不是Th1.3。本次另实际读取Lang作者讲义本地物理31–33：Th10.6及该处证明、Th10.8的精确声明、Examples10.9–10.10；最后又读回root第1节的citation更新，实际核物理21–22的Th8.3声明及Euclidean specialization。没有把这些局部阅读说成读完35页或独证整个面积公式，也未认证Besicovitch–Federer深定理全部证明；Lang是经典课程讲义来源，不是本轮新研究定理。

A参与了gate中的来源与纯性核算，自己的A8不作为自己的独立审查。本formal正证对象为root和B的实际论证及整合范围，逐式重算其CW、真实clock、energy/slicing和条件面积公式；A主稿的独立核验由root/B承担。来源身份核验、接受具名定理、项目有限推导、内部独审与外部同行评审分开。

## 2. PBP的完整量词与数字族的真实反攻

Orponen的n-regular要求closed E及同一C_0在每个中心和所有0<r<diam E的上下r^n界。BP是每个球至少一个plane投影大；PBP要求同一球所选plane的一个固定Grassmann邻域内所有planes都投影大。BPLG的graph base可以随ball变化，亦不保证是原v平面。Th1.6给PBP⇒BPLG；BP需另有WGL才能走源Th1.5，不能赠送WGL。原文Question1及其说明明确其proof还使用更小balls，故一个大ball或有限mesh信息不是该全尺度定理。notation所隐藏的d、C_0及PBP常数依赖，不提供本轮随工作δ退化时可直接采用的统一幂式。

Orponen物理3解释BF时印为“purely 1-rectifiable”，漏掉un的措辞不作为本轮定理输入；实际采用的精确purely unrectifiable、finite H^m和Haar-a.e.投影零量词，以Lang Th10.8为准。该校准不要求本轮重证BF或判定Orponen主定理失败。

独立核数字恒等式：A、B的每位和唯一遍历0,1,2,3，故A+B=[0,1]，自然概率之和为Lebesgue概率。F=A×B强分离且1-AD，F^4每层256个ratio1/4 copies，自然质量上下≈r^4；L(x,y)=(x−y,x+y)为√2倍正交映射，所以Z=L(F^4)有有限正H^4及真实4-AD。每个原ball含尺度≈r的完整cylinder，其v像是相同尺度cube，支付同一个固定π_v的局部BP，而非只有global大投影。原方向像为完整cube，图形角映射有固定双Lipschitz界。

纯性证明亦成立：0和八个坐标端点的affine span为R^8，任意affine4-plane必统一远离其中一点；固定小球的AD下界把这一距离变成远plane的正质量。在每个cylinder内缩放后，任意候选近似切平面都有固定比例r^4质量离开其cr邻域。若与一个countably4-rectifiable集有正交质量，取相对AD密度1点和该交集的近似切点，余集质量及切锥外质量都为o(r^4)，矛盾。因此不是仅以“没有整体切平面”跳到pure结论。F的三点版本同样给pure1。接受精确具名BF或Orponen1.6，均可排除PBP；前者保证任何Grassmann开球都有零投影plane，后者与纯性反BPLG。这是经典BP/PBP阻碍的实际接口校准，不是新发现，也不反含额外small-footprint、filledX等条件的完整Def17。

## 3. 单位线段、CW原分母与零体积满维出口

主稿的L_v=(1+|v|^2)^(-1/2)使(a+tv,t)的physical长度恰1，并给全部原labels共同clock[0,1/√5]；compactness来自实际有界参数的连续单位段像。δ=4^(-m)截断产生N=δ^(-4)个不同v及唯一标签，角方向为cδ分离，每个δ帽O(1) labels；需要字面δ分离时只付固定尺度或固定着色常数。有限AD仅在r≥δ声明。Y_T=T令逐管及平均λ都等于1，没有借删选制造反攻。

重核whole-round-tube CW：W∩固定物理球仍含所数整管，John半轴均≥cδ且最长轴≥c、≤C。任何实际非空sphere chart |θ_i|≥1/√5还迫ρ_i≥c，故ρ_1/ρ_i有固定上界；四个剩余坐标的packing给δ^(-4)∏_(j≠i)min(1,ρ_j)，再由该chart条件和John体积改写为Cδ^(-4)|W|=CN|W|。帽增厚由ρ_j≥cδ吸收。最终补句确修掉了把任意chart的被省略半轴免费视为长轴的风险。这里只计整管包含，不授partial-intersection/full polynomial-Wolff。

体积与维数两个出口须同时保留。有限H^1、pure1的F使a.e.一维投影零；t↦(1+t,t−1)的角参数非退化，故具名BF经Fubini给compact K零Lebesgue5体积。另一方面，1-AD保证I_s(μ_F)<∞，0<s<1。令a=dx−dy、b=dx+dy：b小于a的固定倍时分母统一≥c|a|；否则|b|≥c|h|，换变量对有界区间积分|u|^(-s)给统一C_s|h|^(-s)。Tonelli及countable s↑1给a.e.实际clock的C_t维数1；乘积不等式|w|^(-4s)≤∏|w_i|^(-s)给C_t^4维数4。共同clock使它正是K_t。细球cover的slice (q−1)-cost积分≤CΣr_i^q，再取可求和趋零的cover序列，即排除dim_H K<5。没有以boxcount代替Hausdorff证明。

有限旋转补齐S4供应同一compact K_full，仍零Lebesgue且Hausdorff5。截断K_m⊂K并Hausdorff距Oδ，固定倍邻域比较由最大δ网的packing给出，足以把假设|N_δK_m|≤Cδ^c返回K的同尺度cover，反满维。故其finite全marks并集虽趋零，却没有固定正幂footprint序列；该结论没有推广到任意partial shading。Lang例10.10已给经典Cantor参数—零投影—Fubini的Besicovitch模板，不能将本轮真实clock或CW的比较称为新Kakeya反例。

## 4. 条件整流性出口的实际参数域与面积公式

root第8节采用的足够条件是有界Borel Z'、有限H^4、countably4-rectifiable、正Lebesgue4的π_v像，以及每个原参数的统一正clock。它不假定连续selector或原graph base已是v平面。countable Lipschitz charts覆盖H^4-a.e. Z'，遗漏集的v像为零。在每个chart中只取实际映入Z'的Borel参数域；若所有这些实际域上的det Dv均a.e.零，4维面积公式使全部v像零，矛盾。故可选一个chart和有界实际Q，正测度上det Dv≠0。

对该chart的Lipschitz延拓，Φ(q,t)=(a(q)+tv(q),t)的5维Jacobian恰为|det(Da+tDv)|。a.e. q∈Q的最高项det Dv非零，故t多项式至多有4个根，在正clock上a.e.非零。Q有界使积分可控，且为正；5维面积公式迫Φ(Q×(0,c))有正Lebesgue5测度。关键是这一像仍由实际Q及原clock生成，包含于原段并，不能计入延拓在Q外的额外像。主稿最终Borel/actual-subset措辞已读回，当前无此缺口。

单个BPLG块可能完全在position方向而v像零，故不能直接选它作a(v)图。此处用整个countable rectifiable覆盖与原正方向像另付该责任。PBP的全尺度具名后果可以提供整流资格，但本轮原输入未给PBP；本条件结论没有对有限δ、条件数或shading给统一正幂常数，也没有完成ordinary或完整critical分支。

## 5. 原质量、删选闭包与旧等价边界

反攻对象保完整原N、每个真实unit clock和λ=1。因此仅为免费PBP桥添加平均或逐管density不能修复这个已列输入。label子族保AD upper与whole-containment CW upper，却不自动保AD lower、满方向像、局部BP/PBP；归一一个很小子族不能恢复原N比例。只删marks而不删labels时，参数Z本身的PBP不会因clock变化而消失，但条件面积公式的实际支持与Jacobian质量是否在原marks内需另证。逐管density至少给每个保留label自己的质量，平均density只给总incidence；二者均不自动重建全尺度连续整流参数及原clock。主文没有混用这些量词。

阶段I实际重读的R15全称shading闭包及R62 §§14–18说明旧CP/PM与PW4相关正幂责任为何不能改名重开；本轮并未建立PBP与这些旧gain的双向等价。本结论较窄：明列joint4-AD、完整方向、各球固定π_v大投影及整管CW不能免费推出所需的PBP。其失败不证明所有整流性方法无效，尤其原small-footprint、filledX、pointΦ、selectedξ/coherence及跨尺度数据的可能贡献仍未解决。不得反过来把欲证PBP作为原公设后以条件出口登记增益。

## 6. 最终范围、修正状态与停止判定

上述root10与B8在所列有限范围内全文通过，无未解决强制项。已核修正包括Orponen主编号Th1.6、版本日期与正文日期的区分、CW非空chart迫相应半轴≥c，以及条件出口仅对实际有界Borel参数子集应用面积公式。B最终两处字面收紧也已fresh全文读回：有限投影的统一下界指δ-thickening的Lebesgue4测度，非有限点集本身的H^4；slicing取max(1,dim_H K)<q<5。源辅助范围只按实际读域记录；BF、Orponen高级wholeproof及标准rectifiability/面积公式没有因本内部审查而获重新认证，亦未作不存在的官方PDF新字节核验。

终macro6/next6/source6均已实际全文读回：ordinary原多尺度、directHRZ全费用、完整sticky临界κ1/余mixed及ordinary桥、同一全方向严格低维构造四路仍开。R93不是完整Def17反例，K_full满Hausdorff5；定性条件正体积也不是finiteδ维数gain。下一入口诚实保持未选定，要求新候选先核原量词、restriction/shading与双向排重，没有预认证未来机制。停止固定BP→PBP的角邻域、数字或density续改；保守streak16与Goal active不变。

本formal仅认可经典来源的正确应用、真实接口反攻及上述条件推论。无newID、ordinary改善、fullbranch saving、低维Kakeya反例或major声明；未经外部同行评审。不预认证后续归档、验证、提交或同SHA同步。本文件完成后停止编辑与检索。
