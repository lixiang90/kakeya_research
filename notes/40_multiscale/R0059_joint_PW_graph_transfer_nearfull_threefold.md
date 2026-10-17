# R0059：用原联合PW计数支付一般余维三维颗粒的近满阴影

2026-10-17，root。先宏观及phase-I排重，working_spec §7锁定此任务后施工。下面是具名外部输入下的完整应用证明，未经外部同行评审；不是普通五维Kakeya证明或重大性/新颖性认证。共同核quotient的joint3AD提取没有解决，也不作为本证明假设。

## 1. 定理、量词与原目标

固定 n≥4、R,C≥1、半代数格式 A、ε>0。存在 η>0、δ0>0、c>0，只依上述固定量，使对0<δ<δ0成立。S=Sδ⊂B_R⊂R^n 是格式≤A、实半代数维数≤3的集合，系数可任意依δ；无光滑、不可约、正则曲率或系数height下界。T是N根原单位δ-tubes，物理方向δ-separated。Yi⊂Ti为任意Lebesgue可测shadings，且

    Yi⊂N_(Cδ)(S),  Σi |Yi| ≥ δ^η Σi |Ti|.

则 E=∪i Yi 满足

    |E| ≥ c δ^(n−1+ε) N.                              (1)

特别，若原整轴都在N_(Cδ)S，任意满足平均近满密度的Yi自动满足稍大C的支撑条件。主命题实际只需阴影近S，不需整管或每个t都在同一图形piece。n=5给R55全类G3的near-full密度区域；全部λ的统一λ³式未据此证明。

## 2. 外部输入和文献范围

使用 Katz–Rogers 1802.09094v3 Theorem1.1：原δ方向分离单位管对任意固定格式半代数H，若|Ti∩H|≥λ|Ti|、λ≥δ，则数量≤C_(n,format,σ) δ^(1−n−σ)|H|λ^(-n)，σ>0任取。原方向/原单位管始终是这项计数的对象。

使用 Guth–Wang–Zahl 2601.14411v2 Theorem1.1：给β>0，存在a=a(β)>0，使三维单位r-tubes族P若绝对凸浓集 Δmax(P)=sup_U Σ_(P⊂U)|P|/|U|≤r^(-a)，且任意可测shading的平均密度≥r^a，则union≥r^β Σ|P|。该输入不要求投影方向分离，且§2.1明确shading可测。其完整深层证明及作者报告的Lean formalization未在本轮重跑。

图形分解使用半代数光滑分层/CAD与Pawłucki作者2007稿的Theorem3_m、Proposition1（对任意实闭域的o-minimal结构）。Zahl 2307.05894v3 §3.1/Proposition3.6说明regular cell的必要性。不是仅由局部梯度有界便推出任意非凸域全局Lip。

Choudhuri 2610.12480v1已在R33入库，本轮实际展开§4 Proposition17/Lemma19。原文是四维余维一whole-tube union；这里独立补一般n→R3的图形、可测阴影、原PW和重复投影费用。不调用其整篇四维数值结论；fresh原PDF与R33 hash相同，不新增该paper/source。

## 3. 一般维度的全局Lipschitz图形覆盖

存在仅依n,A,R的J,L,A′，使S可由J个半代数pieces Γj 的闭包覆盖；每Γj是某个coordinate orthogonal projection πj:R^n→R³上的全局L-Lipschitz图，图格式≤A′。domain可为R³中的低维半代数子集。

证明衔接如下。先光滑分层，每层维m≤3。对其正交切空间框架用Cauchy–Binet，某size-m coordinate minor绝对值≥binom(n,m)^(-1/2)。按有限坐标选择细分good patches，π_I在切空间上的最小奇异值有统一lower；CAD/有限-to-one分解把满维部分写成open D⊂R^m上的C¹图F，||DF||≤C_n。遗漏部分实维<m。

对D应用Pawłucki regular M_m-cell分解；只置换base坐标，M_m只依m。Prop1给每个F坐标全局Lip≤m!M_m^(m−1)C_n。剩余nowhere-dense base上图的维数<m，回到分层步骤递归，深度≤3。m=0时有限点直接处理。把m个base坐标补至3个，π_J仍injective；|π_J(p−q)|≥|π_I(p−q)|，故原normal coordinates仍是π_J域上的全局Lip函数。

取pieces闭包只将Lip函数连续延到domain闭包，维数和格式仍有统一界。没有忽略domain boundary附近的管。

## 4. δ依赖系数的uniform格式责任

上述分层/CAD的数量和格式按固定输入格式可统一。Pawłucki定理没在本文引用显式degree幂界；只需一个有限uniform界。其开篇明确在任意实闭域的o-minimal结构成立。若固定输入公式的regular-cell分解数/格式无统一界，取违反所有标准有限界的系数序列及非主ultraproduct。所得实闭域中的同一半代数D仍适用该定理；其有限分解使用有限个标准半代数公式，因而有某个标准数目和格式。

覆盖、disjoint/almost覆盖、regular cell、C¹/导数界及全局Lip都可用有序域一阶公式表达；remaining dim<m由半代数dimension的固定公式条件表达。将这一有限公式连同其系数按Łos回传，在几乎所有序列成员中给同一标准界，矛盾。故uniform界存在。不声算法最优复杂度、可计算常数或已重证Pawłucki完整20页主定理；该具名输入是本证明依赖。

## 5. 正常纤维上界与真正局部PW测试

令 Hj=N_(C1δ)(Γj闭包)，C1固定足够大。QE给其格式只依n,A,C1；E⊂∪j Hj。全局Lip给每个z∈R³

    H^(n−3)(Hj∩πj^(-1)(z))≤C2 δ^(n−3).              (2)

因为对应图点的base都距z为Oδ，normal函数值的直径O_Lδ，整个fiber装在normal半径O_Lδ球内。低维domain、边界和奇异原层不破此upper。它不是任何阴影的fiber lower。

若U⊂R³是含一个投影管的有限体积凸集，用John外接矩形Q_U⊃U、|Q_U|≤C|U|。Hj∩πj^(-1)(Q_U)为固定格式半代数集，且

    |Hj∩πj^(-1)(Q_U)|≤C δ^(n−3)|U|.                  (3)

无管时所需计数为空；无限体积时upper平凡。John box任意旋转/尺度只改变系数，不改变格式。此joint空间测试比global |NδS|上界多保了实际投影位置。

## 6. 原平均密度、图形选择和非短投影

先保|Yi|≥δ^η|Ti|/2的原labels，数≥cδ^ηN。每根选j(i)使|Yi∩Hj(i)|≥c_Aδ^ηδ^(n−1)，再固定一个j，保

    Nj≥c_Aδ^ηN,  |Yi^j|:=|Yi∩Hj|≥c_Aδ^ηδ^(n−1).   (4)

必要时对原方向的有限2n charts和midpoint固定有限box同时选一类，避免antipodal计数及PW bounded-support规范，仅损常数。原tube、方向和实际Yi^j没有改造成独立prior。

设原轴a+tvi，|vi|=1。用未clamp的正交坐标s=vi·(q−a)，其截面积≤Cδ^(n−1)，即便端帽中s超出原单位参数区间Oδ仍成立。由(4)实际Yi^j点的s-span≥cδ^η。取两点，其支持直线点距离Γj为Oδ、参数差ℓ≥cδ^η。全局Lip给

    |(I−πj)vi|ℓ≤L|πj vi|ℓ+Cδ.

η<1、δ后足够小时，|πj vi|≥c_L。这里只用无限支持线来估计projection速度，未延长原段或声明端帽在原轴内；原实际点和PW体积全未改变。投影原轴的长度在[c_L,1]。

## 7. 投影包络、参数网与原label重数

在有限direction chart中选一个主坐标k，使投影单位方向的第k分量≥c>0。投影支持直线用x_k=0处的两个intercepts和两个direction坐标参数化。它们有固定bounds。把这四个参数round到Oδ网，取固定大半径Aδ与固定长轴长度L0的管P_i，轴center钉在该坐标平面；L0只依R和chart，足以覆盖全部πj Ti。故πj Yi^j⊂P_i。长轴参数没有另设δ网，避免人为产生δ^-1个近相同longitudinal labels。

可以先把共同bounded chart作固定homothety缩进B1/4，再将这些固定长度短轴以相同center/direction延长为unit轴，全部包络仍在B1。半径r3与δ相差固定倍，密度只付固定倍。为免坐标混淆，§§8–9仍在未缩放的三维坐标中使用固定长度L0、体积≈δ²的P_i与正交πj；仅§10调用GWZ时执行此共同缩放/延长，并同步推forward F和shadings。未延长任何原R^n轴。有限chart/固定倍参数网只改常数。

## 8. 原PW传absolute凸浓集并量化去重

若P_i⊂U，则原Yi^j在(3)的半代数test内；原Ti与test的体积比例≥c_Aδ^η。PW以λ=c_Aδ^η≥δ查询，任取σ>0，得到

    #{assigned原i:P_i⊂U}≤C δ^(-2−σ−nη)|U|.          (5)

原δ方向分离在R^n中使用，绝未假投影方向分离。对相同包络P，以U=P代入(5)，其原label重数≤Cδ^(-σ−nη)。每个非空包络选一个原代表，得到distinct三维tube族P，

    #P≥c δ^(σ+nη)Nj≥cδ^(σ+(n+1)η)N,                (6)
    Δmax(P)≤Cδ^(-σ−nη).                             (7)

(7)是absolute Σ|P|/|U|，不是normalized probability Frostman；不插入#P≈δ^-2。近相同网格邻居可有限着色，或直接由(5)计入Δmax，均无正幂额外费。每个代表仍有(4)的原shading证据，去重没有免费遗忘原数目。

## 9. 任意可测阴影的fiber积分与level set

令Ej=E∩Hj，按正交fiber积分定义

    f(z)=δ^(-(n−3))∫_(πj^(-1)(z))1_Ej,  0≤f≤C2.

Fubini给可测f（选a.e.代表），并由(4)与πjYi^j⊂P_i给

    ∫_(P_i) f≥δ^(-(n−3))|Yi^j|≥c_Aδ^ηδ².

取固定c0足够小，F={f≥c0δ^η}，则对每个保留包络

    |P_i∩F|≥cδ^η|P_i|.                             (8)

因为阈值以下部分贡献≤c0δ^η|P_i|，其余f≤C2。三维shading Y′(P_i)=P_i∩F可以包含来自其他原管的投影点；这是同一个实际E的level set，不声为每个原Yi的literal保留。原Yi只提供(5)及积分的真实证据。最终

    |E|≥|Ej|=δ^(n−3)∫f≥c0 δ^(n−3+η)|F|.            (9)

因此没有从(2)的fiber upper推出假fiber lower，也不需要把任意可测Yi填成δ-cubes。GWZ原文允许可测shading，正好覆盖(8)。

## 10. 参数顺序和(1)的完整结论

先取β<ε/3，令a=a(β)为GWZ阈值。取σ<min(ε/3,a/4)，再取η>0足够小，使σ+nη<a/2、η<a/2、β+σ+(n+2)η<ε，并η<1/2。固定图形/PW/包络常数都在此之后由δ0吸收。

具体执行§7的固定homothety h：未缩放的P_i变为固定短轴hP_i，再以同center/direction延长为unit包络P_i*，半径r3≈δ，h(P_i∩F)保作shading。若P_i*⊂U，则P_i⊂h^(-1)U，故(5)给Δmax(P*)≤Cδ^(-σ−nη)；体积缩放仅为固定h的常数。其shading density仍≥cδ^η，且union⊂hF。四个线参数的固定网格在共同缩放和同center延长后仍无exact碰撞（必要时有限chart分别使用）。由(7)(8)与参数余量，满足GWZ的Δmax≤r3^(-a)及平均shading density≥r3^a。将得到的union下界按固定h回传，故

    |F|≥cδ^β δ²#P,
    |E|≥cδ^(n−1+β+σ+(n+2)η)N≥cδ^(n−1+ε)N.

所有选择常数均只依n,A,R,C,ε和具名定理；对任意δ依赖系数、非正则S、measurableYi统一成立。平均密度通过先heavy labels收费转换成每个所选label的密度；未给全部原管或任何后继剪裁免费逐管下界。

## 11. 与R55反攻、旧等价和高维缺口的关系

R55 product-parabola近轴例使有限global projections的方向bin重数很大；本证明完全不声那些angular caps成立。许多同方向、不同截距的投影管可以满足(5)的joint凸浓集；若实际包络相同则(6)明确付重数。新联合PW test与原空间fiber同处一个chart，正是此前仅把两个分别图形/方向覆盖并列所没有支付的信息。

本轮付的是全类near-full三维颗粒估计；不重新命名M3⇔Q3、不重开旧global angular投影gate，也不把图形分解添作未证packet公设。关键高级输入PW、GWZ、Pawłucki仍具名，本项目未独证其wholeproof；只对本应用独立逐步审查。

证明实际只在(5)调用一次原PW。因此同一结论还适用于已独立给出absolute polynomial-Wolff计数、常数≤δ^(-ηPW)的原管族：把σ换成ηPW，并先要求ηPW+nη<a/2及β+ηPW+(n+2)η<ε。只需对本证明固定格式测试集合有这一计数。此为同一证明的输入范围，不另取新名字或结果ID；不能据此声HRZ所有后继叶自动具该小常数。

全λ统一λ³、任意原weights/fine-cap α、HRZ某递归叶的原方向/局部尺度费用，以及五维四维窄分支仍未由(1)解决。k=4/m=3 broad vanishing的旧事实不因(1)消失；不能只把(1)插入一个空终端便宣布H5。ordinary n≥5、general→sticky和最终Goal保持未完成。

## 12. 审查、来源与停止

A按原primary实际补全regular-cell/global-Lip/uniform-format衔接，B独立证明(4)–(10)并反攻端帽、重复和可测fiber；最终另存全文formal reviews。Pawłucki20页、Zahl66页新原PDF进入库，Choudhuri原19页保持同bytes。这里不作重大/首创或新普通维数声明。

停止本轮图形/投影证明的局部常数迭代。下一应正面检验(1)在原高维多尺度中的有效终端/尺度接口，或全λ密度是否需要真新输入；不把尚未付接口直接添作公设。完整归档、独审与safe sync后保持Goal active。
