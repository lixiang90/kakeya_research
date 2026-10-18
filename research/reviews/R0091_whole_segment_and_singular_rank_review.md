# R0091 独审：全线段原测度、奇异秩与直接出口

2026-10-18，A。以下是限定命题的逐步内部独审，未经外部同行评审；不是ordinary/general Kakeya、新维数增益、完整branch-saving或重大性认证。

## 1. 实际全文范围、分工与具名输入

本次fresh实际全文读最终root主稿 R0091_whole_segment_matrix_measure_and_current_exit.md 十节、B稿 R0091_normal_current_and_original_mass_countergate.md 八节、本人A稿 R0091_transport_measure_and_source_gate.md 八节，以及R91 reselection_spec五节、working_spec五节、macro六节、next六节和来源范围 R0091_measure_constraints_and_primary_scope.md 六节。root§9关于有限vector-div与wedge横向导数的最终收紧已读回。本文独审对象主要为root/B完整链；A本人参与的hull、测度与校准计算不算自身独立审查，它们已经由root/B实际全文独核，B的真实反馈无未决必修。

来源实际阅读采用DPR arXiv1601.06543v2的Th1.1、Remarks1.2–1.4、Th1.10、Cor1.12–1.13及§3相应normal-current定义和应用证明；本次再次核本地提取的原声明及§3证明。Moore作者讲义physical47–48的Th49及证明文字已实际读；采用标准Jankov–von Neumann声明，不把其中composition排印问题说成已修订完整外部证明。AMS arXiv1907.07456v3实际读引言Th1.1/1.3、Cor1.4/Th1.7和§2.10–2.14定义，并在本次核对应提取文本；没有新独证其高级wholeproof。Radon–Nikodým、Polish空间概率的Radon性、disintegration与完成测度的Borel版本仍属明确具名标准输入。

版本、页数和root归档信息按source6所记范围使用：DPRv2实际18页、AMSv3实际27页、Moore83页，不混abs或期刊版式。本人没有重新下载、核整PDF字节或fresh官方ref，也没有将root的此类记录冒作本人的检查。两种稿件的阅读、具体应用证明和外部主定理接受分开记录。

## 2. 同维Gδ包络、选择与原carrier的逐步核验

原量词确是任意K⊂R5，不要求K可测或有界，且每个v∈S4有一条长1段。h=dimH K<5时，取s_j=h+1/j，开球cover的直径及s_j费用分别不超过2^{-j}；令G为各层开集之交。对任意s>h及任意固定尺度ρ，充分大j满足s_j<s与2^{-j}<ρ，同一cover给H^s_ρ(G)≤2^{-j}，再令j→∞。这支付H^s(G)=0，连同K⊂G给dimH G=h；不是仅在一个尺度上得小content。故h<5时G是Borel Lebesgue零集。

对每个开U，紧单位段包含于U意味着到U的闭补集有正距离，故R_U={(v,a):a+[0,1]v⊂U}在S4×R5中开。R=∩R_U为Gδ且方向投影满S4，符合具名JvN关系的假设。universally measurable选择在完成σ上可测；改取σ-a.e.相等的Borel版本a_0可定义标准Borel pushforward。改值只发生在一个零方向集，其与整个clock的product仍为零，因而方向边际仍严格σ，段包含于G在σ-a.e.方向成立，μ(G)=1。

root/B均没有将a_0在异常零集上的选择性质保为逐方向声明，也没有将G内新选择冒作不可测原K内的选择。μ由G承载不等于闭support包含于G。compact K时另有compact关系的Borel选择和support结论；任意K版本不靠这项compact性。无界a_0不妨碍有限概率pushforward成为Radon，也不需要anchor矩。此归约保同一Hausdorff维数、真实单位clock和全部方向边际，范围通过。

## 3. Endpoint、PSD极分解及DPR真正给出的秩

直接沿原clock对紧支撑C1向量test积分，row-wise约定给

Div S=∫v(δ_{a_0(v)}−δ_{a_0(v)+v})dσ(v)，TV≤2。

test及一阶导数有界、总积分为概率、|v|=1，所以无界anchor不产生积分或端点矩缺口。此项一般非零；root/B正确调用DPR Remark1.3的finite-measure RHS，或直接Cor1.13，没有假Div S=0。trS=μ与S(R5)=I5/5也由真实全单位clock计算，没有按位置重新选择方向law。

写S=Aμ，PSD及trace1给1/√5≤|A|_F≤1，故|S|=|A|_F μ与μ等价，奇异载体相同，polar缩放不改rank。Div符号为Mξ，限制到Sym5的wave cone仍是奇异矩阵，即rank≤4。具名Cor1.13只给这一秩上界于奇异部分；h<5使μ(G)=1且G为Leb零集，才覆盖本构造的μ-a.e.处。

位置disintegration给A(x)=∫vvᵀdν_x(v)。kerA内非零ξ满足∫(ξ·v)^2dν_x=0，所以条件方向law位于ξ的正交4平面。该平面可随位置变化；没有因此取得固定4D carrier、C1法向、原δ管子族或可调用DIR4的局部全方向输入。由PSD的全局I5/5也不能倒推局部rank5。该应用链通过，但其结论未越过标准singular-rank barrier。

## 4. Root/B校准的真实质量和反例边界

root同原点全方向bush取a=0、t∈[0,1]。极坐标给μ密度1/(|S4||x|^4)，μ(B_r(0))=r，A=x̂x̂ᵀ为rank1，而总矩仍I5/5。它是实际同集、全方向、whole-unit-clock族，但μ绝对连续、K体积大；只反全局方向矩推出局部满秩或physical4-Fst。A稿的居中单位段及B核过的球面校准使用不同clock/载体，未在root结论中混用。

root四平面例的常数独算无误：每个Q_i的H4面积16，Σ_iP_i=4I，因此(1/320)Σ_iP_iH4⌞Q_i总矩为I/5、总trace为1；一般点polar为P_i/4、rank4。P_i消去垂直Q_i的导数，剩下沿四个切向坐标的cube面H3边界，Div有限。它真实有4维carrier，却没有全方向whole-segment transport；不能作为完整Kakeya反例或将不同校准拼成该反例。

B的wedge校准也独立核过：T_1=e_1L5、T_2=(e_2+f(x3)e_4)L5、T_3=e_3L5在有界Ω上各finite mass且Div0；取bounded二值f不属BV，形式3-current的boundary含非measure的D_3f e_1∧e_4。因此三个normal1-currents即使对同一Lebesgue测度独立，也不自动给normal3-current。这里f本来非BV，绝非“有界BV函数乘积不保BV”。root§9已按此精确修复，无遗留必修。

## 5. 原restriction、两种density与高级current出口

whole-label限制至σ(Ω)=m后保完整clock：未归一端点TV≤2m，归一后≤2；joint5-Fst常数付m^{-1}，总矩改成条件方向矩，不保I5/5或统一ellipticity。原joint5-Fst的r^4方向cap乘至多2r clock核算正确，位置边际却只自动1-Fst；bush给严格校准。全局分五cones只给不同位置边际，没有同一正质量measure共同被五current mass支配。

对root/B同一全方向radial bush，所有方向取m个交替半clock区间，每条density恰1/2。单线有2m个端点；原点项∫v dσ=0，其余2m−1个正半径sphere互不交，且每sphere上v由位置唯一恢复，每项variation恰1。因此原矩阵mask的Div TV=2m−1，归一总质量再乘2。这个计算同时保平均与逐管density，却不保uniform boundary；nearfull删许多小holes同样不控制BV。whole-label闭包不能替任意clock/可测marks闭包，保wholeclock又不能声trace仍集中原小shading。

DPR Cor1.12需同一支配measure及其a.e.独立方向；AMS Th1.3需真实normal k-current、C1 k-plane distribution及实际non-involutivity区域。原filledX和粗coherence没有支付这些条件。k=1的C1分布本来involutive，不能凭normal1直接升维。source6已准确说明normality依current及boundary两mass有限判断，没有依AMS§2.11(iii)关于一般L1系数的过强iff，也没有由该局部文字问题否主定理。B反攻和root修订均保持此层级。

## 6. 全文结论、宏观范围与停止

最终root10/B8和全部授权终稿范围实际全文通过上述限定核验，**无未解决强制项**。本轮实付的是任意K的同维carrier与可测选择、原全clock矩阵测度的有限端点资格、具名DPR的准确秩出口，以及几类免费推断的严格校准。A自证没有在本文冒作独立审；root/B对A的实际独核和本文对root/B的逐步审分列。高级DPR主§2、AMS wholeproof和一般GMT基础仍具名，未被项目应用核替代。

终macro6及next6实际全文核过：四完整路径保持，DIM001/R38/R80已付不重排，旧polar/cut/cone/跨块及CP/PM/PW正幂冻结不因current名称解冻；可测性资格既已付，不能再列为唯一主缺口。没有预选合格gain，也没有以假ellipticity、C1、BV或normal3输入降低原目标。保守ordinary/完整branch-saving时钟14与本轮实际资格信息分开，不把无qualified机制当external blocker。

本结论不是ordinary/general维数改善、完整κ1/余mixed排除、同集full方向低维反例、新ID、重大或新颖性认证；完整目标仍未证未否，Goal active。**未经外部同行评审**。本人只新增本授权formal六节，未改metadata、Git、其他文稿或进行新检索，不预认证未来归档、验证、提交或同步。
