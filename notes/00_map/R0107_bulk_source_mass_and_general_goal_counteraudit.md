# R0107：全窄片原访问预算及横向残余独立反攻

2026-10-19，B。先按reselection完成资格比较，后实际读取working5才展开下列条件有限计算。唯一分配文件，十个编号节；不把附加横向law改写为原source，不宣新ID、major或完整branch saving。

## 1. 实际恢复、完整四路与本轮准入

实际读GOAL、当前STATE、完整ROADMAP（第一次合并输出中段被截，另分段补读）、registry的78项及R106 next6。R106 root10、A/B10和两formal6沿刚完成的同会话全文读域复用，另读回A正式拒选范围。实际全文读取本轮reselection5、working5及A《complete_goal_and_seed_strength_reselection》10节；本稿落盘时root主10已全文读，§8仍在整合原shell预算，最终cross另于本节末和§10记录。

ordinary初始化/直接HRZ仍须原small footprint、全部方向和完整parent/λ费用，不能用一个native有限lemma替代；DIM001的具名输入、内部assembly及任意集合17/4读出已付，本轮未获新seed；fullrough仍须同一原T的filled X、Φ、ξ及native Y/CW联合；真正反例须同一Euclidean集合含全部方向unit段且strict低Hausdorff维。R106 parabola nativeY tubeKT失败永久保留，不能换网回收Jac/CW成成功构造。

本轮新增的可检验责任是同时求和全部x2窄片的原访问。它可能避免单片固定h质量损失，但须写出共享root图、同一原T的真实终clock、原cell重数和原N/I分母。无working时只提出此门；以下有限lemma施工以已锁working为界，不倒填成此前已审结论。

## 2. 真实same-T公式及两种不同未付输入

在固定normal chart anchors0/1、F0=I、F1=0，令原斜率与轴参数为(φ,ψ)、(a,b)，code C(T)=(U,V)=(b,b−a+ψ−φ)。只有当所选原管确实还满足U2−V2=c，并且

    F_u=[[f1(u),f2(u)],[0,1−u]]

时，才可在其真实访问点写ξ2=x2−c。nᵀG_u=0单独只约束系数，不给该code offset或point场。写H=v−u、ki=(fi(v)−fi(u))/H，同一原T精确满足

    Y1(v)=Y1(u)+H[ξ1−k1 x1−k2 x2]−H²(k1φ1+k2φ2),
    Y2(v)=Y2(u)+H(2x2−c)+H²φ2.                  (1)

fine物理访问与native标签误差O(δ)在下文δ≤H²后另吸收。第一行不能丢k2x2；同一x2条内该项作为平移消去，跨条则未必消去。

本轮条件分支有两个来源门，均未赠予完整source：足够原T同时具有上述code/row约束；横向secant k1具有正指数概率upper。第二门不能由wholeF非拟合直接代替。在所检bulk时窗上f1恒定、f2粗糙时，wholeF可能有非拟合而k1仍是atom；这不要求已固定的两个外部anchors处f1也相等。这里不声这种形式已实现完整Def17，只指出一个合法的逻辑缺项。

## 3. 有限锁题与共享图的实际精度

有限lemma取0<τ<1、mesh H、Q⊂[-1,1]²同一坐标H格、预先固定g:Q→[-B,B]。clock σ为概率或总质量≤1的有限测度；每v有d_v∈[H,2H]、|ki|,|c|≤B。要求对所有中心q0和H≤r≤1，

    σ{|k1−q0|≤r}≤A r^τ.                        (2)

每实际(v,q,T)访问的原输出距

    y_v+d_v(g(a,b)−k1 a−k2 b, 2b−c)

至多B H²；每(v,q)原重数≤D。所用Y_v在CB²H球内的H²-cover≤KB^C/H。Q可以缺任意格，访问子集Q_v可随v任意变化，g必须在选v前固定。这是条件输入，不要求每strip大、每cell共同clock或原g独立。

source匹配时固定root(u,原native y)。H-input cell里的physical点不一定落同一dyadic H-cube，且H未必sourceallowed。取上邻allowed R，H≤R≤δ^-η H；每input cell分成其相交physical R-cube的有限标签，数目固定有界。每标签由原Def17.2 coarse ξ给振荡O(R)≤K H，选一个实际代表g。替换x和ξ引起d_v O(KH)=O(KH²)误差。图多值问题用标签分开，不能免费假全实Lip。若d_v/H仅在[K^-C,K^C]，同理付入B；选共同dyadic shell后可恢复[H,2H]。

## 4. 全图collision energy，不先丢一个strip

对同一b，令

    E_(v,b)=Σ_(a,a'∈Q_b)
      1{|g(a,b)−g(a',b)−k1(v)(a−a')|≤C0 B H},
    E_v=Σ_b E_(v,b).

这是完整原图，而不是Q_v的energy；同b时k2b精确抵消。a≠a'、距离jH的事件把k1限制在半径C0B/j的区间。半径>1用σ总质量≤1，其余用(2)，统一概率≤C A B^τ j^-τ。每a在距离jH处至多两个a'；每b有O(H^-1)点且b行O(H^-1)，所以

    ∫E_v dσ≤C_τ A B^τ H^(τ−3).                 (3)

对角O(H^-2)可吸收，因为τ<1。这里点packing本身足够，不需要额外point angular Frostman或projection大定理。τ=1有log，按锁题不优化该端点。

不能直接对邻b行碰撞套(2)：k2(v)(b−b')会与k1相关而抵消。正确做法始终先算同b energy，下一节只用第二输出限制不同b的输出格重叠。也可按b-index分O(B)色后算同样上界，但不必预丢一个颜色。

## 5. 终端容量一次使用，控制任意clock-dependent删选

对每v、每个有访问的q，仅取一个实际输出，记该行原占点数n_b及输出H²格数m_b。同输出格的两点属于上节碰撞事件，故

    n_b²≤m_b E_(v,b).

第二输出距(y_v)2+d_v(2b−c)≤BH²；相邻b中心相距≥2H²，因此任一终端格只能来自O(B)个b。原Y_v容量给Σ_b m_b≤K B^C/H。对全部行一次CS即

    n_v²≤K B^C H^-1 E_v,
    ∫n_v dσ≤C_τ (AK)^1/2 B^C H^(-2+τ/2).       (4)

这里σ总质量≤1已足够，不必把一个稀疏root的clock重归一。不同v可选完全不同Q_v；用全图energy已经同时控制所有子集，因而无须先找每strip共同活跃的v，也无须对所有大子集作额外union bound。

原访问数J_v≤D n_v，于是(4)右侧再乘D。这一步不能从occupied cells改称原incidence而省D。终端AD1给的是不同Y_v标签cover，未授每label只有一个原终点；重复在此被CS和原D支付，不再免费乘一个terminal degree增益。

## 6. 原same-T pairs在共同shell的lower

设原管族有N条、m=|Z|，m≥K^-1δ^-1、N≈K^±Cδ^-4。先对每p、每Φ_p方向δ-bin选一根原定义实际存在的witness，合并重复(p,T)，并令每(T,u)仅有一个canonical访问，产生所用图S_T。固定point/方向的物理碰撞及一个T在同u穿过的fine point数均有界，所以保I=Σ_T|S_T|≥K^-C Nm。这里只给所用图degree upper，不赠未用全部过p管的upper；所有量仍用原N而不重设分母。

取δ^(1/8)的上邻allowed粗时间mesh h0∈[δ^(1/8),K^Cδ^(1/8)]。将每S_T按至多C/h0个h0-window分解，先对窗、再对T两次CS给Σ_(T,J)|S_T∩J|²≥c h0 I²/N≥K^-C N h0 m²；不需要每T duration lower。取正向u<v只损固定倍，并去除对角。每管距u小于q h0的候选终clock数≤C(qh0/δ+1)，故全部近对角pair损失≤C N m(qh0/δ+1)。q=K^-C先足小、δ/h0随后足小，可保原lower固定比例。

剩余gap落[ qh0, C h0 ]；分O(log K)个dyadic shell后，某共同H满足

    # {(T,u,v):u,v∈S_T,同h0窗,H≤v−u<2H}
        ≥K^-C N H m².                           (5)

得到(5)不声每T在同一shell都有lower，它是同原分母的平均pair lower。h0→H损失未藏成常数：H≥q h0，logK及q^-1均并入K^C。H可能非allowed，§3的上邻R负责空间coherence；始终保原同h0-window标签以使用时间dyadicLip，|ΔF|≲h0而H≥qh0，故|ki|≤K^C。η最后小使H≥δ^(1/4)，H²≫δ，原δ误差可吸收。没有重取source或把两time独立化。

## 7. 原root和cell重数，与pair lower真正同量纲

固定u及native标签y，一个H-input cell有至多C(H/δ)²个原fine points。通过§6固定的selected Φ-witness图、κ1 AD上界及固定point/angle的O(1)物理重数，所用degree≤Kδ^-1；故每个(v,cell)实际原访问重数

    D≤K H²δ^-3.                                (6)

只计已固定的原witness usedgraph，不对all T_p或任意过p的外来T赠upper。每(T,u)的canonical访问与终native标签沿用同一原管；实际Y_v中Oδ近点的误差由H²支付。physical R-cube标签及fine offset均只损K^C。

全部roots(u,y)数≤K mδ^-1≤Kδ^-2。对一个root，用

    dσ_u(v)=δ/(C H) Σ_(H≤v−u<2H) δ_v

作为总质量≤1的共同clock测度。所需额外law是针对原Z的(2)，等价于原clock计数≤A(H/δ)r^τ；不是沿每管ST加权后免费继承cap。将(4)乘D和CH/δ，再对全部roots相加，得同shell原pair upper

    I_H≤K^C sqrt(A) δ^-6 H^(1+τ/2).              (7)

对比(5)及原N m²≥K^-Cδ^-6，只有当K^C sqrt(A) H^(τ/2)趋0时才矛盾。此处D H^-2=Kδ^-3与每root原量纲真实可比，无须公设densityflat或每strip有许多cell。假如A=H^-a，须a<τ并让全部K预算随后小；A任意大不会产生source saving。

## 8. 横向cap如何测试，以及目前不能免费得到什么

若一个h0-window对f1的所有实affine函数均有h0^(1+ε0)近拟合点数≤h0^θ h0/δ，则固定u的k1-ball半径h0^ε0命中也受此upper。粗端用总质量≤1可换成很弱正幂cap，但会产生A的真实h0幂及H/h0、原Z稀疏比例费用；不能写成无费的(2)。要让(7)有saving，必须逐项比较这些费用与τ/2。

在exact diagonal f2=0的特定分支，该scalar fit等价wholeF相应拟合，R77统一NF准备或可提供它；仍须匹配good windows的原pair质量、root条件和allowed尺度。本稿不把“可尝试”认证为已完成的原source推论，也不假good f1窗占原I正比例。一般所检bulk窗的f1恒定而f2 rough时，wholeF nonfit没有横向信息；更换名字称transverse regularity仍是附加假设。

因此本轮已付的是(3)–(7)条件计数，未付的是原一般row/code归约及实际横向clocklaw。不能以NF并非全平凡就声这些门必有，也不能用一组任意rough函数自称完整Def17反例。

## 9. 独立反攻、删选闭包和旧等价排重

删除(2)时，取g(a,b)=q0 a、k1≡q0、k2≡0及全格Q，输出只有O(H^-1)个H²标签而n_v≈H^-2。它满足其余有限cover输入，严格否免费正幂upper；其直线nativeY不满足原tubeKT，所以不反fullsource。若g随v改为k1(v)a，即使k1有好law也可取消，故共享coarse图不可删。复制原标签M次使J乘M，证明D不是装饰参数。

任意删marks或whole-T子族保同图、同原D和未归一σ时upper单调；它不保point Φ/filledX lower。限制clock到质量p后若归一为概率，cap常数必须除p；(5)的平均pair也不能逐管读出。若最后要逐T duration，须对原平均I重新heavy并扣原管数和duration，不会从本lemma自动恢复完整source。

R22付whole-time重源而未付任意pair条件化；R64 raw ν²结构不适用于selected sameT pairs；R72 basicness及γ>1/2出口未含本全strip能量；R75 CW/Kakeya基线、R76单code块和R80跨块账均不授(2)。R77的fullmatrix非拟合不授一般f1非拟合。旧CP/PM全称gain也许可重调推出某些条件后果，但本有限lemma不能反推完整gain，因code/row、横向law及原source提取仍缺。故不是新完整gain命题的等价改名，也不是新理论登记。

## 10. 当前判定、交叉范围与停止

已实际全文读root主10初稿及working5，随后再次全文读取root§8最终canonical-usedgraph/双CS平均pair版，独立逐式核(3)–(7)、same-T公式和原shell计数，无数学阻断。两次读取的时间与版本分开，不把锁后计算倒填成reselection时已证。A完整重选10节已读，其未获不同seed判断与本稿一致。本人的计算不算本人独审，等待root/A对本稿逐步核查。

本轮的有限条件机制可施工且具有真实原N/I比较：全部strips一次使用终端容量，全图energy容许任意依v删选，真实D与共同shell保留原分母。它修正单strip计数的需求，但并未证明完整rowcap、fullrough、ordinary或真低维反例。若不能从原source给横向law，必须保留该残余，不能附成功假设后声原目标完成。

停止重复本energy、逐strip选择、更多fixedtime与R106标签改造。后继须面对一般f2驱动的不可见横向分量及code/row原提取，或进行完整重选。未经外部同行评审；具名源wholeproof未在本轮重证，不预认证metadata、Git或同步，Goal active。
