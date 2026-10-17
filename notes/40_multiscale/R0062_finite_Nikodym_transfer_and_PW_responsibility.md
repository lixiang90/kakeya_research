# R0062：有限Nikodym转移、一般维度PW延轴闭包与射影等价停止

2026-10-18，root整合。Goal active。spec先写，phase I未解后正式§7/§8选取实际有限转移和闭包。以下给真实原集合的估计，不以NδE代理Lebesgue体积。四维部分依具名SRC001/DIR003，不能以OpenAI署名认证；一般维度半代数闭包另自证桥梁。未经外部同行评审，无新数学ID/重大性/优先权认证。

## 1. 本轮完整结论和未完成目标

ordinary n≥5/general Kakeya或重大中间结果仍未完成。本轮证明三项接口：(i)具名四维有限方向输入推出任意管族的逐管nearfull阴影与固定倍管扩张的体积比较；(ii)每个固定n≥2的全部polynomial-Wolff类在同半径、有界同轴延长下，只损log^n；(iii)完整PW4的unshaded体积下界、nearfull shaded下界和R61的adaptive合法射影门槛，在正幂量词层面是同一难题。第三项触发停止改名，未证明这些等价难题本身。

## 2. 四维定量有限结论

固定R,C及σ∈(0,1)。存在η>0、δ0>0及c>0，使δ<δ0、λ∈[δη,1]时成立。先在共同graphchart/超平面H={t=s}给有限原unitδ轴L_i=(b_i+(t−s)u_i,t)，原非负权wi，总W>0，bounded参数，所有实际Yi⊂Ti Lebesgue可测，|Yi|≥λVδ。Vδ是实际共同tube体积，含roundcaps。假每个C0δ截距帽中的原权≤α；重复labels不删，则E=∪Yi满足

    |E|≥c δ^(3+σ) λ⁵ W/[α(1+log(2/λ))]。        (1)

更宽的basepoint版本允许H上基点距其实际支持线≤Cδ、原unit段在固定纵向距离内；此时α对实际支持线截距计数，有限邻格费只改常数。由其无权版和base packing，任意有限四维原unitδ族、逐管|Yi|≥λVδ，都有

    |E|≥c_R δ^σ λ⁵/[1+log(2/λ)] · |X|，         (2)

其中X可取其固定R倍同心同轴扩张RT_i之并，或在共同有界区域的同轴固定长度continuations之并。无需PW/Σ/原方向分离。故每ε>0取η足小，有

    |∪RT_i|≤C_R,ε δ^−ε |∪Yi|。                  (3)

R固定，δ0、常数允许依R；未声R依δ增长时费用为R⁴或其它sharp幂。平均密度输入只能先heavy限制labels，(3)不控制原零阴影labels的扩张。

## 3. 具名有限方向输入及其强度

DIR003/SRC001的实际已审读出：对每a>0可取ηsrc>0，使任意有界四维indexed affine graphs、非负权、每个h-slope帽权≤β、每个index至少h^−1+ηsrc个时间marks满足

    I_marks≤C β h^−a #E_h。                     (4)

允许任意稀疏方向条数M和重复labels，常数无权跨度依赖。该任意M版本来自R9有界shear放大，不只满方向headline。所有source高级wholeproof依赖保留，R38完整内部assembly不等于外部同行认证。定性Hausdorff/Keleti–Máthé的维数延长本身不提供(4)。

## 4. 共同随机格保真实Lebesgue体积

先固定原basepoints/截距和witness管，不按mark格另造prior。取共同shift ζ∈[0,δ)^4，Gζ=δZ4+ζ。令Zi=#(Yi∩Gζ)。固定单位δ管在该格上总点数≤Cδ^−1，且

    Eζ Zi=δ^−4|Yi|≥cλδ^−1。

故Pr{Zi≥c0λδ^−1}≥c1λ；不同indices不需独立。令rich权Wζ=Σwi1_(Zi≥c0λδ^-1)，则E Wζ≥cλW。共同格保证

    Eζ #(E∩Gζ)=δ^−4|E|。                       (5)

若E有无关无界部分，先截共同bounded区域，只使目标更强。所有点选取/finite计数可测。每个原clock层至多固定点数，固定slots可把空间grid点转为indexed time marks，原权重复仅固定倍。

## 5. 内部pole、全局shell与原权质量

对rich线删|t−s|<cλ的格点；每clock层O(1)点且δ≪λ，足小c使每线只损固定比例。所有余点按sign及τ≤|t−s|≤2τ分层，cλ≤τ≤C_R，层数L≤C_R[1+log(2/λ)]。

总weighted points≥cλδ^−1Wζ。先按总weighted points选一个全局shell，保≥cλδ^−1Wζ/L，再删该shell中点数<c′λδ^−1/L的indices，只损一半。这样只付一个L，不再按label数选层或对权重分层。所有保留points均是真实Yi点，pole可以穿原axes，但不在所用shell上；此构造不满足R61 whole-axis统一map域，不能冒原gate已经证明。

## 6. 真射影图、分辨率和截距帽权

对选中的同一s/τ/sign使用

    Gτ(x,t)=(τx/(t−s), τ/(t−s))， h=δ/τ。

原线精确变为y=τu_i+b_i z，新斜率恰b_i。在该shell上z处于一个固定非零clock区间，图形位置/斜率固定有界，D Gτ≤C_R/τ。每个原δ-cell在该shell的像直径≤C_Rh。对实际grid点，每点只用同一个Gτ，故新occupied h-cells数≤C_R #(E∩Gζ)，与重复index数无关。

原δ截距帽权≤α，每个h帽涵盖≤C_Rτ^−3个原δ帽，所以新β≤C_Rατ^−3。原clock步长δ在新clock步长≈h，time合并及slots仅固定费。每保留线至少cλδ^−1/L marks；相对新h^−1=τ/δ的密度≥cλ/(τL)。先取η<ηsrc/2、δ0后取，这些marks满足(4)。τ≥cλ还保证h≤Cδ^(1−η)→0；没有把极小shell当原δ分辨率使用。

## 7. 格计数、唯一log及λ⁵回传

在(4)取a=σ。保留原weighted visits≥cλδ^−1Wζ/L，得到

    #(E∩Gζ)≥c δ^σ τ^(3−σ) λδ^−1Wζ/(αL)
                 ≥c δ^−1+σ λ⁴ Wζ/(αL)。        (6)

最后τ≥cλ、σ<1，常数可依固定R。对共同ζ取期望，用E Wζ≥cλW及(5)，即(1)。只有这里rich概率多付一次λ。若E本来是occupied原δ-cells且每线已知足够marked cells，可直接有限格论证得到λ⁴版本；不能把它无证明地称为真实Lebesgue λ⁴。

共同格使用实际点，不先填满所有与E相交的δ-cubes。映后standard单位模型只作为真实点的固定误差包络，actual clock padding/fixed homothety含端帽，原marks不clamp。它未证明四维全λ临界maximal估计；必须λ≥δη且η依σ选取。

## 8. 从超平面模块到任意固定扩张管族

对X取一个δ-separated极大有限net，点数≥c|X|δ^−4。每点选一个原witness Ti：距其支持线≤C_Rδ，纵向位置固定有界，Ti保原阴影密度。按有限方向charts选base数大的一组，使该原线clock分量≥c。再按baseclock分δ厚slabs，选一层保

    M≥c_R |X|δ^−3

个bases。设层中心s。每base距其实际线在H_s上的交点≤C_Rδ；同一截距δ帽内的这些δ-separated bases都在一个C_Rδ四维球内，故重数O_R(1)。有限邻格/着色后可用(1)的W=M、α=O_R(1)。不需要base点在原Ti内，也不移动实际Yi。得(2)，再吸收λ^−5和log得(3)。

RT_i在这里可同时扩大长度和半径，法向距原线只增固定C_Rδ，base版本已收费；它不是下面PW延轴定理中免费加宽原管。逐管witness是必要scope：若若干labels的Yi空，X不能仍取其全部扩张。

## 9. 标准有限转移的双向与文献边界

包含超平面base估计(1)的完整有限模块，在nearfull正幂量词上可反推DIR003。对原方向v_i，取固定远pole外变换G(x,t)=(x/(t+R0),1/(t+R0))，实际marks域uniform biLip；像支持线在z=0的截距为v_i。将witness单位支持段固定延至这些bases，marks不添加，固定homothety后用(1)。原方向帽权α成为base截距帽权α，λ⁵可由η足小吸收。原cell marks可用固定倍cells构造真实tube阴影后回传。只含relative-union(2)的弱表述本身未单独证明与DIR等价。

因此(1)–(3)是已给finite源的实际可用转移，不登记新数学ID或独立突破。KMv3§1.2是定性extension，§1.1还区分positive-measure line subsets；Wang–Zahl2502v1§1.6/Th1.12′证明R3的更广R范围doubling。这里是R4、固定R、具名源条件推论，不能把R3定理当R4证明，也不据有限检索认证priority。

## 10. 任意固定n的半代数Nikodym shadow

下面不使用四维finite源。固定n≥2、bounded区域、L及格式D。S是bounded semialgebraic集合，系数任意。定义

    M_S(x)=sup_(|v|=1)(2L)^−1∫_[−L,L]1_S(x+sv)ds，
    H_t={x:M_S(x)>t}。

线截S只有固定数intervals/points，总长度可由有限端点经QE表达；H_t及active-direction witness关系固定格式。Definable choice选unit v_t(x)，再C¹分层，n维层外零测部分不影响体积；不依赖S的系数height或t。目标为

    |H_t|≤C_D,n,L t^−n |S|，0<t<1。              (7)

固定格式不可删除，任意可测S不享uniform multiplicity常数。

## 11. 多项式active-set下界与真实area公式

unit条件给vᵀDv=0，故rankDv≤n−1，P_x(s)=det(I+sDv)的次数≤n−1、P_x(0)=1。对active A_x={s:x+sv(x)∈S}，长度>2Lt，有

    ∫_(A_x)|P_x(s)|ds≥c_n,L t^n。               (8)

自证：删去|P|超过其两倍平均的部分，余集长≥|A|/2；从中取n个间隔≥c_n|A|的点。Lagrange在0评价，分母≥c|A|^(n−1)、分子有固定L界，得1≤C|A|^−n∫A|P|。不假系数bounded，也无需外加Remez结论。

对固定s，Φ_s(x)=x+s v(x)。它的regular preimages是固定格式fiber的孤立点，数目≤C_D,n；正维fiber处的非零Jacobian不可能发生。局部C¹紧耗尽应用area formula，所有strata总数统一：

    ∫_(H_t)∫_(A_x)|det DΦ_s(x)|ds dx≤C_D,n,L|S|。

不需要Dv在全domain上有统一界；紧耗尽后单调极限即可。与(8)合并即(7)。这个临界弱Ln只对固定格式S，不能冒一般Nikodym maximal猜想已经无条件解决。

## 12. 原PW的restricted mean

原unitδ族满足全部fixed-format H、r≥δ的计数

    #{i:|Ti∩H|≥r|Ti|}≤C_D K δ^(1−n)|H|r^−n。    (9)

任意原子族有m个labels，实际p_i(H)=|Ti∩H|/Vδ。tail积分min(m,Ar^−n)给

    Σp_i(H)≤δm+C_D m^(1−1/n)
                       (Kδ^(1−n)|H|)^(1/n)。     (10)

whole-ball查询还给总N≤C Kδ^(1−n)。这些是absolute原计数，restriction不重设K，也不需m近满。对n=4用shadow t^-4后(10)的四次根只生t^-1，这是保持PW幂的关键；若先heavy rays再双付a^-4将得到错误的a^-8接口。

## 13. 有界同轴延长的PW/log^n闭包

P_i是同一原支持线上的unitδ-tube，中心沿轴移动距离≤固定R；同半径δ，原labels/重复均保留。对固定格式S、a≥δ，令J={i:|P_i∩S|≥a|P_i|}、m=#J。则

    m≤C_D,n,R Kδ^(1−n)|S| a^−n
                                  [1+log(2/a)]^n。 (11)

小a≤C_Rδ时，J非空即|S|≥caδ^(n−1)；总N界使(11)右侧≥cK a^(1−n)≥c′Kδ^(1−n)，粗付全部m。大a时先去P_i roundcaps，损Oδ体积比例可吸；原Ti核心cylinder的平行offset rays覆盖P_i核心的同一法向crosssection。选L只依R，Fubini给

    Vδ^−1∫_(Ti) M_S≥c_R a，i∈J。               (12)

这是原实体平均，不先按ray删选。令b=c_Ra/2，t<b层最多贡献bm。把(10)/(7)代入剩余所有levels，得

    a m≤C_Rδm+C_D,n,R m^(1−1/n)
                (Kδ^(1−n)|S|)^(1/n)[1+log(2/a)]。

a≫δ时吸δm、取n次方即(11)。H_t的格式对t统一，故原C_D′只依S格式与固定量。log^n可用预留δ^−e吸收，K=δ^−η仍是放宽参数的同一PW类。

这里没有让法向半径固定倍自动享原core证明；若需该闭包须另作有限共同translations覆盖。也不允许R随δ变大而隐去其费用，更不抹掉HRZ长ρ归一化的ρ^(1−n)成本。

## 14. 三个完整PW4命题及量词

U4：对每γ>0存在足小ηU、δ0，使bounded原unitδ族、N∈[δ^−3+ηU,δ^−3−ηU]、全部fixed-format PW系数δ^−ηU时，whole union≥cδ^γ。等价的δ^γ Nδ³写法只差ηU余量。

S4：同类、任意原Lebesgue Yi平均≥δηU时，shaded union≥cδ^γ。P4：R61完整adaptive whole-axis uniformly bounded projective门槛，保δ^ε原I且新角帽原count≤δ^−ε。三个命题目前均未证明。不能将N管union当fixed-format测试来声U4已付。

所有uniform量词都包括合法原restriction：保δ^eI只给N_J≥δ^(e+η)N及平均密度相应lower；不能在删选后照抄原η。以下每次先取目标loss、再输入容差和各项小loss，δ0最后吸常数。

## 15. U4到完整合法射影门槛的真实逆向

假设U4。原平均λ≥δη，删|Yi|<λVδ/2的labels保I/2，每剩原label都有逐管density≥cδη。选固定bounded-slope方向chart保cI，因此N_c≥cδ^ηN≥cδ^−3+2η。

选固定farclock slab[T,T+1]远离全部原axes。每条支持线以clock T+1/2为中心取真实physical unit段P_i，clock分量有固定lower且≤1，所以其完整unit轴都在该far slab；中心位移固定有界，半径仍δ。由(11)它们满足PW，小log预留e/constant/N放宽均先取≪ηU。U4给|U_far|≥cδ^γ。

包含真实roundcaps的far union在[T−δ,T+1+δ]内。Fubini存在该区间中的s使slice三体积≥cδ^γ。每P_i截面都在B_Cδ(b_i+s u_i)内，故从实际原labels中选M≥cδ^−3+γ个C_Rδ-separated截距，近重复计入；M个labels彼此不同。令

    F_s(x,t)=(x,t)/(1−t/s)。

pole=t=s远离全部原完整axes，F_s及逆在原共同bounded域uniform biLip。新斜率u_i+b_i/s=(b_i+s u_i)/s，因此选中原labels新δ方向分离，帽重数固定。其**原**incidence≥cδηδ³M，原I≤NVδ≤Cδ^−η，故保原比例≥cδ^(γ+2η)。先γ≪ε、再η/e≪ηU,ε，得P4。

另有独立交叉验证：U4先用于原heavy族，再用(3)令E=U_far、witness=far P_i、X包含原whole Ti，双向fixed continuation比较也迫far union大。它仍用具名DIR而非PW/log闭包。主证明(11)路径的反向不需四维finite源。

## 16. 正向、shading移除及双向等价停止

P4加具名DIR003推出S4：选中原I≥δ^eI、N′≤N，先heavy其逐管密度至少δ^(e+η)固定倍；bounded projective的实际marks和固定长度cover可回传，角帽原count≤δ^−e作为α成本。DIR需Lebesgue连续转移时用R60共同格/finite slots程序，不用假像proxy PW。各项loss先小于目标γ余量即得原E≥δ^γ。S4⇒U4令Yi=Ti立即。

U4⇒S4还可直接：先原heavy保I/2，对该合法子族用U4；以(2)取X为其wholeunion、E为原shaded union，λ≥cδη。取η足小吸λ⁻⁵/log。没有把零阴影labels的wholeunion加进X。

所以在具名四维finite源下，U4⇔S4⇔P4为**同一正幂主要障碍**。此前R61逆向未付是当时的状态，现由完整延轴/切片证明补上。依AGENTS，停止把far-angular/rich-cap/结构提取改名成独立新方向，不新增数学ID。等价式本身不是新高维结果；实际成果是(1)–(3)/(7)/(11)的合法有限接口。

## 17. 一手来源、反攻与审查范围

新增KM2203.15731v3原PDF15页及已登记Wang–Zahl2502.17655v1原PDF127页（原为web-only），各自官方history核、raw bytes/hash/pdfinfo/text；root实际render/read KM PDF3/§1.2，WZ PDF14/§1.6及PDF114/Th1.12′。合计53PDF/53sources。WZ三维更强R范围和KM定性结论均不作为本文四维finite证明输入。

A证明weighted hyperplane/randomgrid/finite转移，B独立核格质量、base/mark phases及扩张scope；B自证semialgebraic shadow/PW continuation及far逆向，A独立逐式核一般n。root实际整合sourceη、原体积、同半径、smalla、平均/逐管及正gain双向。最终formal记录实际全文版本。未认证所有高级wholeproof/穷尽priority，未经外部同行评审。

## 18. 停止和下一完整责任

本轮并未由PW证明U4，也未证明或反驳ordinary n≥5/general。R61 Σ子类范围保留，但不续其图形常数；direct source norm、ρ/D/k、pair尾部、finiteNikodym的λ/log/R优化和已付延轴闭包都停止。

R63须先周期宏观，返回真正的高维/完整PW几何缺口，选择一个有真实新估计机会的可证伪机制。若仍以PW4为入口，必须面对unshaded原族的多尺度退化/载体问题，不再以方向提取或原阴影重命名绕回它。下一唯一 notes/00_map/R0062_next_macro_and_cross_carrier_selection.md，先核真实cross-carrier来源及R44/45/R48冻结；没有新输入即换完整高维分支。Goal保持active。
