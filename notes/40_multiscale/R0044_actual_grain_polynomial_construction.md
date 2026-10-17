# R0044：actual grain测试的延拓、共同标签与精确费用

2026-10-17，A（audit_four_dimensional）。运行context.py并读GOAL/STATE/ROADMAP/registry78/latestR43/AGENTS及本轮指定目标。只编辑本分配文件，不Git、不另开代理。当前主任务是实际d5,k=ℓ=3、另有R43有界uniform-PW的原配置；总目标仍为普通高维Kakeya，以下不认证完整κ≤ζ或新颖/重大结果，未经外部同行评审。

源位置：WZ Def17.2–17.4，PDF65–66/text3362–3434；局部原incidence和coherence为§19.1 (146)，PDF76–77/text4033–4084；精确matrix affine已在Lemma20.2，PDF86/text4522–4538；small variation为19.2，PDF78/text4127–4131。原good-q/原权证明使用项目R0016_original_tuple_audit §§1–3，不假原(146)对任意q自动有lower。R43的PW原权/无权/clock限定全部保留。

**本轮实际结论：** 可合法删极少原时间使f成为subpower-Lipschitz，给出不假C²的共同Bernstein近似；更重要的是，原heavy tubes可选共同原endpoint时间，实际offset palette来自单一完整Y_{z*}，不需跨Y_z细尺度同一性。自然e≈ρ²的测试已可取P=f(z*)常矩阵；细尺度另付二维法向slope网即可构造全体测试，但PW预算仅回到native κ≤2，且这些affine pieces的逐片界已由原CW给出。没有把这个失败升级为所有非affine包络均不可能。

## 1. 原命题、raw law与一轮停止

固定ζ,γ>0，η足够小、δ随后足够小。原f:Z→Mat(2,2)仅有allowed dyadic scales r∈[δ,1]∩δ^{ηZ}上的dyadic-Lip；所有entry有界1。每层Y_z完整δ-AD维b=2−κ，各Φ_p有κ-AD/slab，ξ_p在原ρ-cube中一致到O(ρ)。不假公共Y_z、C¹/C²、逐管dense或每管独立frame。K以下表示δ^(−Cη)的真实固定幂，可随记账增加固定C。

原whole-T uniform lawν保持不变，必要时只限制index子族，质量一律用原ν。marked raw mass记δ times原point–tube incidence数除以#T；每tube每δ-time band仅O(1)原δ-cubes，所以该law的time marginal在每band至多Cδ。总mass由原平均shading至少δ^{C_*η}。不把局部incidence law归一化成新的uniform prior。

目标是实际构造S_j并付presentation、volume、原tube事件质量及相交时长；若仅回四维/CW基准或度数费用吃尽，立即停止该polynomial-envelope尝试，不再另选ρ/e/D追参。

## 2. dyadic-Lip到Euclidean-Lip：删选必须先于world选择

令相邻allowed scales比例a=δ^η，层数L≤1+η^(−1)（端部取邻接dyadic尺度仅付K）。取β=δ^{Bη}，B为足够大的固定常数。只对allowed r≥Cδ/β，删除距任何r-grid边界≤βr+Cδ的z；删除的是**整个原z-layer**。每scale有O(1/r)边界，每个边界附近至多Cβr/δ个δ-separated原times，故

    #Z_bad≤CLβ/δ，
    raw marked mass deleted≤CLβ。                      (1)

第二式用原time-bin upper Cδ，未假条件于q后的clock重新独立。取B>C_*+3后，删去原marked mass的o(1)比例。因为#Z≥δ^{η−1}，cardinality同样只删o(1)。先全局删，再重选good q；不能先选一个恰好贴在dyadic边界的q后免费宣同一比例。

原whole-layer删选保各Y_z/Φ_p不变。cross-time Y-union的upper来自原union，lower由每个occupied coarse center所属的一整Y_z的fine-AD packing提供，必要时增加η的固定倍；这是R22已经支付的合法time-restriction闭包，不给裁切后的任意point subset添加AD lower。

对保留z,z′，设它们最细共同allowed ancestor长r，下一子层长ar。若ar≥Cδ/β，二者距分界至少βar，故|z−z′|≥cβar，而|f(z)−f(z′)|≤Cr。若ar更小，则r≤Cδ/(βa)，用δ-separation同得该比值。若没有共同unit interval，用coarsest boundary删除及entry bounded处理。因此

    |f(z)−f(z′)|≤K_f |z−z′|，
    K_f≤Cβ^(−1)a^(−1)=δ^{−O(Bη)}。                   (2)

最细层不能把每个δ-grid点附近δ都删掉；(1)只从r≥Cδ/β开始，较细尺度由δ-separation处理，正是避免这一错误。

## 3. 自包含共同多项式近似及其导数

对每个matrix entry g=f_ab|Z_good，McShane公式g_ext(t)=inf_z[g(z)+K_f|t−z|]给K_f-Lip延拓；再clamp到[−1,1]仍保常数且在原Z上相等。不是C²延拓，也未声称解析。

在J=[t0,t0+q]上写F(s)=g_ext(t0+qs)。Bernstein多项式

    P_D(t0+qs)=Σ_{j=0}^D F(j/D) binom(D,j)s^j(1−s)^{D−j}

有|P_D−g_ext|≤K_fq E|Bin(D,s)/D−s|≤K_fq/(2√D)。四entry同步取同一D。若|u|≤Cρ，目标matrix误差e/(Cρ)可由

    D≥C[1+(K_f qρ/e)^2]                              (3)

支付，degree真正进入presentation，不叫fixed complexity。由Bernstein差分公式，|P_D′|≤K_f：D/q乘相邻F差≤K_f。若h_j为常数，接点δ-ball仅通过f-approx贴入测试所需buffer至多Cδ(1+K_fρ)；若h_j另有time-Lipschitz常数L_h，还须加CδL_h，degree本身不能代替这个界。须e大于真实buffer，不能只看轴上一点误差。后文实际h_j常数或affine slope O(ρ)，以及完整axis段覆盖，均已支付这一点；自然ρ≥δ^(1/4)、e≈ρ²时条件由η充分小保证。

每个测试若|v−P_D(t)u−h_j(t)|∞≤Ce、h_j polynomial degreeD_h，则presentation E_j≤C[1+D+D_h]，因为每个normal表达式总次数≤1+max(D,D_h)。体积Fubini给|S_j|≤Cqρ²e²，与degree无关，但PW另有(1+E_j)^A。平均许多polynomial tests不是一个免费低复杂度并。

## 4. 先排已有matrix-affine输入，不把Taylor改名

原Lemma20.2本来针对任意Mat(d−k,k−1)，不是scalar专属。若实际保留原times上已付

    |f(z)−rz−u|≤ρ^{1+ε0}|r|，

满足其原mass和scale条件，则由它与CW已排相应κ，根本不需要新PW test。|r|小的责任是原19.2，不能把r=0直接塞进相对误差式。

对fixed D，若f在原times恰等于一个degreeD多项式P，#Z≥δ^{η−1}且|f|≤1，选D+1个按原time次序等量分开的点，间距≥c_Dδ^η。Lagrange公式给||P^{(j)}||∞≤C_Dδ^{−Dη}。故Taylor余项≤C_Dδ^{−Dη}ρ²；若另有approx误差h，则总误差h+C_Dδ^{−Dη}ρ²。只有当这确实小于ρ^{1+ε0}|r|才可调用20.2。这样说明不少fixed-degree精确分支已被旧工具覆盖，**不**说明自然精度h≈ρ的任何局部degree0拟合已满足它。

增长D或仅dyadic-Lip不能免费给上述C² budget；(3)只是诚实的近似构造，不独自给新κ结论。

## 5. 真实good q与共同endpoint的whole-tube选择

先完成§2全局删时，再用R16原加权关联平均选allowed ρ-world q，J为其time interval，ρ∈[δ^(1/4),δ^µ]，δ≤ρ²。记d_T为T在q内原used marked incidences（每time O(1)），I_q=Σ_Td_T。原good-q lower和coherence/AD upper为

    I_q≥K^(−1)ρ^{5−κ}δ^(−5)，
    N_q=#T(q)≤Kρ^{4−κ}δ^(−4)，
    d_T≤Cρ/δ。                                      (4)

由最后一式还有N_q≥K^(−1)ρ^{4−κ}δ^(−4)。这不是声称任意q或每grain局部都dense。

取heavy tubes d_T≥I_q/(2N_q)≥K^(−C)ρ/δ，保至少I_q/2总incidences。其数量≥K^(−C)N_q。按q内至多Cρ/δ个原times平均，存在**原实际**z*，有至少K^(−C)N_q heavy tubes在该层used。保这些whole indices，记T*；每条旧d_T依然≥K^(−C)ρ/δ，没有把marks只剩z*。原whole ν的质量

    p*=ν(T*)≥K^(−C)ρ^{4−κ}，
    m*=δΣ_{T∈T*}d_T/#T≥K^(−C)p*ρ。                  (5)

对每T选一个原z*接点，O(1)重数只影响K。这个endpoint selector保的是同一批真实tubes、原q-marks和原whole prior；没有另造Cartesian family，也未赋新AD lower给T*。

## 6. 共同reference shear与natural label精度

取一个原reference tube T0∈T(q)，用其实际轴(x0(t),y0(t),t)作**共同**affine shear u=x−x0(t)、v=y−y0(t)。det=1，原whole clock及PW原law保持，所有selected axes在J上有|u|≤Cρ。参考点与q内所有used p具有ξ_p=ξ_q+O(ρ)，而f在同一allowed J内变动O(ρ)。因此对T∈T*，写a_T=θ_{T,x}−θ_{0,x}、b_T=θ_{T,y}−θ_{0,y}、F*=f(z*)，有

    η_T=b_T−F*a_T=O(ρ)。                             (6)

这里用T0的实际used点固定θ0，误差O(δ)由δ≤ρ²吸收。并非每T各自换frame。

定义h*_T=v_T(z*)−F*u_T(z*)。**整条line恒等式**为

    v_T(t)−F*u_T(t)=h*_T+(t−z*)η_T。                 (7)

故在J上drift≤Cρ²。自然e≥Cρ²时，对h*按e-grid一次选j(T)，整短clock轴及其δ-tube均落在

    S_j={t∈J, |u|≤Cρ, |v−F*u−h_j|≤Ce}。

这是P=F*常矩阵、h_j常数、degree0的测试；不必先近似全f。实际f-normal offsetH_T(t)=v_T(t)−f(t)u_T(t)也因(7)、|Δf|≤Cρ和u≤Cρ有O(ρ²) drift，但这项只能用于e≥Cρ²，不能推到更细e。全部轴段被覆盖还给|T∩S_j|/|T|≥cρ，比旧marked-duration lower更强；原marks只用于合法选出T*和anchor。

## 7. palette来自单一完整Y_{z*}，不是跨time细coherence

h*_T等于原native y-label加上共同向量F*x0(z*)−y0(z*)再加O(δ)：actual p只在δ-tube内，不必恰在选定axis上。原接点在q，故它来自实际完整Y_{z*}∩B(Cρ)的一次平移及O(δ)扰动。对e≥δ，这只增固定数邻接bins，不改变下述packing。对δ≤e≤ρ，fine-AD packing给

    N_h(e)≤K^C(ρ/e)^{b}，b=2−κ。                (8)

证明：在所有occupied e-cells挑固定color的分离representatives，每个代表所属的完整Y_{z*}在B(代表,ce)内有≥K^(−1)(e/δ)^b个fine点；这些ball互不交且落在扩大B(Cρ)内，其总fine点数≤K(Cρ/δ)^b。除得(8)。没有给裁切Y∩Bρ补lower；lower来自完整Y的balls，upper在扩大window使用。

这正是endpoint selector解决的共同label问题。Def17.2跨time union只有baseρ的AD，不能直接用来查询e≪ρ；本稿没有这样用。自然e≈ρ²时(8)是真实的优于ambient二维网的palette。

## 8. natural budget：仍只回native κ≤2

每piece体积≤Cρ³e²，E_j=O(1)。对同一label原whole tube事件，λ_j≥cρ。PW给p_j≤C C0ρ³e²ρ^(−5)。这些events按j(T)形成原index partition，Σp_j=p*，故由(5)/(8)

    ρ^{4−κ}≤K^C C0 (ρ/e)^{2−κ}ρ³e²ρ^(−5)，
    ρ^4≤K^C C0 e^κ。                               (9)

e≈ρ²仅给2κ≤4加subpower误差，即κ≤2；e更大更弱。b=2−κ非负本就是native维数范围（fixed κ>2与η充分小时Y-AD相矛盾）。自然精度的曲面degree预算并无新作用，因为degree0已完成同一覆盖。

若不用整axis覆盖而只用原marks，也可对label事件保实际质量p_j，用restricted PW mean得m_j^5≤C C0P(E_j)|S_j|p_j^4，再Hölder总和得到相同预算；不能把m_j/p_j误当uniform整段duration，亦不能把同一tube质量重复收费。

## 9. e≪ρ²的诚实共同slope网施工

细尺度δ≤e<ρ²时，不继续把h*当共同常数标签。由(6)/(7)，对η_T∈B(Cρ)取mesh e/ρ的二维网，同时对h*取(8)的e-grid。以这两个实际bin定义

    h_j(t)=h_j*+(t−z*)η_j，P(t)=F*。

每个T固定一次bin-pair，误差≤Ce在整个J成立，所有q-marks保留，甚至整轴段被覆盖。δ-tube横截面误差≤Cδ，因为P有界；e≥Cδ（固定倍端部可放宽Ce）即可，不需新的time-dependent frame。实际palette、degree和volume为

    N(e)≤K^C(ρ/e)^{2−κ}(ρ²/e)^2，
    E_j=O(1)，|S_j|≤Cρ³e²。                    (10)

二维slope费用不可因ξ_p在q中O(ρ)一致而消失；这只给rangeρ，不给在mesh e/ρ上只有subpower个值。PW加原p* lower得到

    1≤K^C C0 e^{κ−2}。                              (11)

对κ≤2、e≤1，这没有strict saving；bounded chart里全ambient测试也强制C0至少一个固定常数。细e越小只放大右端，并没有一条可继续调参的出口。单anchor更细offset window若损失原质量，须与palette同步支付，不能固定p*而只减N_h。

## 10. 这些最便宜的pieces已被原CW覆盖

对(10)一个label的任意T，anchor normal误差≤Ce、normal slope误差≤Ce/ρ。把它延到原whole clock（这里只分析原本已有的整管，不新造线段），其距同一affine3-plane的normal偏差≤Ce/ρ。u及clock全范围有界，故整T在John axes约1,1,1,e/ρ,e/ρ的凸box中，volume≤C(e/ρ)^2。原CW直接给

    p_j≤C C_CW(e/ρ)^2。

这与PW短片λ≈ρ、volumeρ³e²给的p_j≤CC0(e/ρ)^2是**相同尺度幂**。e≥ρ²的未标slope测试也可用宽e/ρ≥ρ的wholebox比较。因此本施工不只是“暂时没调出gain”，其affine分片约束已经回到旧CW；不能换成polynomial标题登记新机制。它并不证明所有真正nonaffine P、不同actual h_j聚类或更强原相关性都被CW覆盖。

## 11. 真正nonaffine近似仍未付的责任

(2)/(3)确实可构造共同P，但不能自动减少actual h-label自由度。对原tube在J上定义h_T^P(t)=v_T(t)−P(t)u_T(t)虽然是degreeD+1 polynomial，却依赖该tube的anchor位置和方向；给每管独立一个h_T不等于少量共同grain labels。若将这些系数quantize，必须付实际piece数和原事件质量，不能只报告P的一变量degree。

若强行用constant h_j和非affine P，仍只能从原O(ρ²)稳定性出发；到e≪ρ²时误差没有被(P≈f)抹掉。先把clock剪至q≤e/(K_fρ)可恢复constant-offset稳定，但clock费用和pieces数必须付，而且那时常矩阵近似已足够，不能免费获得新curvature gain。以上只是明确的未付必要步骤，不是所有nonaffine envelopes的反例。

### 11.1 一个真正nonaffine的actual certificate：local-clamp及访问全收费

B提出、本文独立核验的补充能把nonaffine测试也完成到一个诚实费用式。对§3每entry的McShane延拓，再clamp到J∩Z_good上原f该entry的[min,max]；不改任何原fine值、不增K_f。dyadic-Lip在J上给range≤Cρ。Bernstein是这些样本的凸平均，故不仅在原times，**整个J**都有|P(t)−F*|≤Cρ，仍保(3)的近似与导数。没有从稀疏times的bounded值免费推出polynomial gap内bounded。

对同一实际T*，精确恒等式

    h_T^P(t)=h*_T+(t−z*)η_T+[F*−P(t)]u_T(t)

使whole-J range包含于h*_T+B(Cρ²)。先按单Y_{z*}的ρ²-anchor grid将每T唯一分给coarse label c，数量≤Kρ^{−(2−κ)}；再为每c填覆盖B(c,Cρ²)的fine e-grid。对Cδ≤e≤ρ²，这是真实共同constant-offset polynomial tests，总数及体积满足

    N≤K^Cρ^{2+κ}e^(−2)，
    Σ_j|S_j|≤K^Cρ^{5+κ}，E_j≤C(D+1)。           (12)

这是一个实际已施工的upper，不是optimal palette的lower。每T只属于一个coarse anchor class，但可访问其中很多fine cells。对H_j取原class中实际访问该cell的tubes，不伪称A_tot≤p*。固定t的fine cells partition及tube截面误差O((1+||P||)δ)≤Ce给真实M=Σ∫_{H_j}q_T(S_j)dν≥cp*ρ。每坐标h_T^P为degree≤D+1的多项式，range O(ρ²)；按两坐标导数零点分至O(D+2)个单调段，格边界计数或bounding rectangle给

    A_tot=Σ_jν(H_j)≤p* L，
    L≤C min((D+2)(1+ρ²/e),(1+ρ²/e)^2)。              (13)

δ-thick截面只加固定邻格；这里P全J bounded已真实证明，移动h_j不另出现。可能不同coarse c使用相同几何fine cell，volume上界重复计费是允许的，而每T的coarse class唯一，M不因此重复。

原restricted mean与Hölder（B完整推导）为

    M^5≤(5/4)^5 C0[Σ_jP(E_j)|S_j|]A_tot^4。

用(5)/(12)/(13)约去p*^4ρ^5，得到

    ρ^{4−2κ}≤K^C C0(D+1)^A L^4。                    (14)

对κ≤2左边≤1，右边没有强制小量，即使理想化L=1也无strict κ收益。细e需要更大D和L，只会恶化这个已付certificate。该nonaffine施工不属于§10的凸box逐片直接比较，但其完整原mass/volume/degree/访问预算仍回native baseline；不据此否定所有更优joint palette或其他包络。

## 12. 本轮出口

已付合法time trimming、Lipschitz延拓/Bernstein degree与derivative预算、原good-q到heavy共同endpoint、单一完整Y_z*的fine palette、natural和细尺度共同labels及真实整管mass/clock，以及§11.1真正nonaffine local-clamp certificate的完整访问费用。最便宜affine施工的PW界被原CW重复；nonaffine证书(14)也只有native基准。未获得κ≤ζ、dim>4、完整mixed/general Kakeya或major。

按开轮停止条件停止该polynomial-envelope局部尝试，不再优化ρ/e/D，也不把公共Y_z、C²、低complexity或免费slopepalette当公设救回。若以后重开真正nonaffine测试，须有新的原质量兼容结构来减少h_T^P聚类费用；这不是本轮已证输入。待root整合全文及B稿实际独审后正式归档。
