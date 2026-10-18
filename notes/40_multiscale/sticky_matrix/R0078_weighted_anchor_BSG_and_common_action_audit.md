# R0078：带原权anchor、metric三路径与共同small-doubling作用集

2026-10-18，A，phaseII，恰十二个编号二级节。实际全文读R78终spec五节（含§2已锁三目标）、phaseI A8/B7、opening macro六节。只编辑本授权文件；无Git／元数据／下载／新代理。本文第一目标实际证明，不把given-commonX或自由不可约性当输入。高级源wholeproof具名，未经外部同行评审。

## 1. 完整原模型、both-full范围与统一费用H

保bounded Def17 matrix33κ=1的原T/N/CW、全部Y/X/Φ/ξ/coherence和R76真实fine g；每条原heavy管保全部S_T。原t,s、h=s−t、A=F_t−F_s满足|h|、smin A≥σ=δ^b。置M_u=(F_u−F_s)A^-1、λ=(u−t)/h，C_t=(1−λ)M_u、C_s=λ(I−M_u)。原g≤1满足

    B_u+C_t y+C_s y′∈N_CδY_u，   q=Eg≥δ^C(a+b+η)。

令U_r={|u−t|,|u−s|≥σ，smin M_u,smin(I−M_u)≥δ^r}；只在q_*=E(g1_Ur)≥δ^a q时施工，否则该子支质量已小。r须在He阈值后选，不把R77固定1/50免费当本U_r。one-full／small-det（包括rank0）不由本稿覆盖。

写n=δ^-1、A_f=Y_t、B_f=Y_s，二者完整AD1给#A_f,#B_f=K^±C n。取H=δ^-C0(a+b+r+η)足大，固定C0涵盖q_*^-1、全部矩阵norm／逆和源K；后文H^C总为有限固定幂。H不伪称仅含η。对u∈U_r，T_u=C_t^-1C_s及其逆均norm≤H，原细输出归一成

    y+T_u y′∈S_u^(err)，
    N_δ S_u^(err)≤H^C n，                           (1)

其中S_u^(err)=C_t^-1(Y_u−B_u)+B_(CδH)。这是对原正边的cover，不是统一carrier，也非fine误差仍Oδ绝对常数。H二维球膨胀及线性变换的cover费均在(1)。

## 2. Metric覆盖/Ruzsa的fine单位

N_δ始终为physical Euclidean δ-cover，常数球／cube等价只付固定维数。若||L||≤H，则N_δ(LE)≤CH²N_δE；若||L^-1||≤H且E为δ分离，N_δ(LE)≥cH^-2#E。有限倍和差及δH膨胀也只多H^C，不把它们当O(1)。

以下使用三条有限Ruzsa规则，均可在δ格中验证：

    N_δ(E−G) ≤C N_δ(E−F)N_δ(F−G)/N_δF；              (2)
    E⊂F0+(B−B)+B_(Cδ)， #F0≤C N_δ(E+B)/N_δB；        (3)
    N_δ(kZ−lZ)≤C_(k,l) Kd^C_(k,l) N_δZ，
                   若N_δ(Z+Z)≤Kd N_δZ。            (4)

(2)在每个E−G格选一个实际差见证，再让一个δ-separated F-net通过两个difference cells编码；每对格只对固定数目标格相容，得到乘积／分母。用于有限点集时N_δF不被精确card冒替，尤其F=L B时要付H^-2。

(3)贪心取尽量多不交的e+(B+B_δ)，每个体积≈δ²N_δB，全集位于E+B+B_δ；maximality给误差Cδ的覆盖。(4)将Z snap到δZ²，每个和差格的实际误差仅固定(k+l)δ，再用有限abelian Plünnecke–Ruzsa。相同方法允许先有small difference而后得固定倍sum/difference的多项式控制。没有rounding后新增边或独立性。

## 3. 保留边的有限三路径引理：独立证明

给有限二部图G⊂P×Q、边密度≥p。先取P1为degree≥p#Q/2者，保至少一半总边且#P1≥p#P/2。对子图P1×Q，随机取q∈Q并令R=N(q)。记p1≥p/2为其密度。E#R²≥p1²#P1²；若一对P1点的共同Q邻居数少于ε p1²#Q/2，则它同时落入R的概率至多ε p1²/2。故存在P2=R，使#P2≥c p²#P且其内部坏pair至多ε#P2²。

删P2中坏伙伴数>sqrt(ε)#P2的点，余P′损失≤sqrt(ε)#P2。每个P2点仍有原degree≥p#Q/2；所以可取Q′⊂Q，#Q′≥cp³#Q，每q′的原P2邻居数≥cp³#P。取ε=c0 p^6且c0固定小，则删点不吞这些邻居，每q′仍有≥cp³#P条**原边**入P′。因此

    #G∩(P′×Q′)≥cp^6#P#Q。                         (5)

对任意p′∈P′、q′∈Q′，其中≥cp³#P个中间p2既邻接q′又与p′不是坏pair；每对有≥cεp²#Q个共同中间q2。因此该任意端点pair有≥cp^11#P#Q条实际三路径。上述明确补出retained-edge，并非只保大vertex sets。作者Tao2012 Notes4 Lemma3/4给此标准图论框架；这里独立写出了保(5)所需删除余量，不引用13.7的literal scalar形式升级。

## 4. 三条原partial sums到二维metric full-sum

设P,Q原δ-separated，||L||,||L^-1||≤H，图G密度p，所有边p+Lq落在J个δ-cells中。对第3节给出的任意(p′,q′)三路径p′—q2—p2—q′，有精确恒等式

    p′+Lq′=(p′+Lq2)−(p2+Lq2)+(p2+Lq′)。            (6)

每个右侧项都在原partial sum cells。固定端点pair及三个cells，第一项把q2限制在L^-1的δbox内，至多CH²个原δ-separated Q标签；第二项再给O(1)个p2。因此路径对cell-triple的重数≤CH²，而非injective免费。反过来，一个triple的交替和只相容固定数full-output δ-cells。

每个full-output cell选一个端点见证，利用三路径数和此重数，得到

    N_δ(P′+LQ′) ≤ C H² J³/(p^11 #P#Q)。             (7)

若#P,#Q≥H^-C n、J≤H^C n、p≥H^-C，则full sum≤H^C n；(5)也保H^-C n²条原边。整个proof在原native细标签上作，不先合并同格权，也不要求L保lattice。原source误差δH已通过partial-cover J收费；(6)本身用实际点值无误差。

若一个权h0∈[0,1]的均值≥d，先取h0≥d/2的边图，密度≥d/2；这些原边每条权≥d/2。应用(5)–(7)后保留h0质量≥d^C原产品。这正是所需weighted-retained版本，不是只能给large subsets的普通existence输出。

## 5. 实际anchor h：原clock与原产品质量

令g_r=g1_Ur，v(y,y′)=E_(u∈原νZ)g_r(y,y′,u)，q_*=Ev。原产品CS/Jensen给

    E_(u0,y,y′) g_r(y,y′,u0)v(y,y′)=E v²≥q_*²。

所以有真实u0∈U_r，使h0(y,y′)=g_r(y,y′,u0)v(y,y′)原均值≥q_*²。且逐点h0≤g_u0、h0≤v。u0确在both-full，故T0=T_u0及其逆norm均≤H；没有以only C_t可逆冒T0可逆。

h0是原exact细pair的权，不替换成其两个marginals产品。对h0≥q_*²/2的边图，所有partial y+T0y′都继承u0的实际(1)。由第4节weighted版本，在原native labels上可取A0⊂A_f、B0⊂B_f，满足

    #A0,#B0≥H^-C n，
    N_δ(A0+T0B0)≤H^C n，
    E_(原A_f×B_f) h0·1_(A0×B0)≥H^-C。              (8)

(8)最后一项并非凭顶点大小推出，而是retained原边权。其原参考分母一直#A_f#B_f，随后不得将它冒原wholeT质量H^-C。

## 6. 第一rectangle的doubling与很多原u

由metric Ruzsa triangle及(8)，

    N_δ(A0−A0)≤H^C n，
    N_δ(T0(B0−B0))≤H^C n。

把第二式通过T0^-1映回并付H²，得N_δ(B0−B0)≤H^C n。固定倍self sums/differences均由第2节付H^C n；原N_δA0,N_δB0至少H^-C n。这些是实际选集的small doubling，不宣它们ADlower。

因为h0≤v，(8)立刻给

    E_u E_(原A_f×B_f) g_r·1_(A0×B0)≥H^-C。          (9)

取原U′⊂U_r为内层均值≥(9)下界一半者；0≤g≤1给ν(U′)≥H^-C、保留整个(9)质量至少H^-C。同时可把阈值统一取为一个事先确定的H^-C，保证每u∈U′在A0×B0上的实际图密度≥H^-C，因为其分母只比原产品更小。不同u的图仍完全相关，不给公共边集或独立clock。

## 7. 每个u的第二BSG保持真实边输入

固定任意u∈U′。在同一exact A0×B0上阈值化g_r的正权，得原边密度≥H^-C，partial y+T_u y′仍由(1)以≤H^C n cells覆盖。Tu及其逆均≤H；再用第3–4节，得到A_u⊂A0、B_u⊂B0，

    #A_u,#B_u≥H^-C n，
    N_δ(A_u+T_u B_u)≤H^C n。                       (10)

该次仅需(10)，无需各u子集自己相交；真正共同A0/B0已由(8)保权选出。尽管可另保第二次边质量，后文不把它替换成完整子矩形的g；只使用full-sum结论(10)及A0/B0自身small doubling。

量词是每个u∈同一U′都各有其A_u/B_u，有限原times可逐个选择；不存在未支付的measurable selection或逐u输入ADlower。所有lower／upper和norm费用为统一H固定幂。

## 8. 两次Ruzsa triangle真得完整A0+T_uB0

应用(2)，先以中间A_u，再以−T_u B_u，得到

    N_δ(A0+T_u B0)
      ≤ C N_δ(A0−A_u) N_δ(A_u+T_u B_u)
           ·N_δ(T_u(B0−B_u))
           /(N_δA_u ·N_δ(T_u B_u))。                (11)

A0−A_u⊂A0−A0，B0−B_u⊂B0−B0；第6节给其cover≤H^C n，线性Tu付H²。中间small sum由(10)，分母第一项≥H^-C n，第二项因Tu^-1≤H和Bu原δ-separation也≥H^-C n。因此

    N_δ(A0+T_u B0)≤H^C n       对所有u∈U′。         (12)

这一步没有假A_u/B_u的intersection，也不需要从其input mass推full source regularity。若直接以#B_u替N_δ(T_u B_u)，会漏矩阵压缩费；(11)显式保此分母。所有sets是实际有限native点，不是先取整生成的虚边。

## 9. 共同X及真正operator的construction

定义同一个实际有限集X=A0−A0。对第8节每u，S_u=T_u T0^-1。由(8)的metric covering (3)，存在#F≤H^C的有限F⊂A0，使

    A0⊂F+T0(B0−B0)+B_(Cδ)。                       (13)

应用S_u并取差，得

    S_u X ⊂ S_u(F−F)+T_u(2B0−2B0)+B_(CδH)。        (14)

令Z_u=A0∪T_u B0。由第6节两端self-sum和(12)，N_δ(Z_u+Z_u)≤H^C n，且N_δZ_u≥H^-C n。故第2节(4)给N_δ(3Z_u−3Z_u)≤H^C n。

X+T_u(2B0−2B0)⊂3Z_u−3Z_u；(14)的translations个数及δH膨胀只付H^C。因此

    N_δ(X+S_u X)≤H^C n， N_δ(X+X)≤H^C n。          (15)

这里S_u次序必须是T_u T0^-1；没有把T_u本身与T_uT0^-1混同，也未擅加任何生成算子到真实u集合。(13)的细δ误差在(14)后变δH，已经在(15)付掉，不说其仍fineδ绝对常数。

## 10. X的norm、上card和所有尺度coverlower

X⊂[-2,2]²，所以norm有固定界。由第6／9节，N_δX≤H^C n；取任一a*∈A0，X包含A0−a*，故N_δX≥c#A0≥H^-C n。于是(15)可除以真实N_δX，得到

    N_δ(X+X)+N_δ(X+S_uX)≤H^C N_δX。                (16)

对任意δ≤ρ≤1，完整原Y_t的AD upper给每ρ-ball中A0点数≤CK(ρ/δ)。因#A0≥H^-Cδ^-1，至少H^-Cρ^-1个ρ-balls才能覆盖A0。X含其平移，故

    N_ρX≥H^-C ρ^-1       对全部δ≤ρ≤1。             (17)

只用完整环境upper和原保留质量，没把A0或X宣ADlower。X是finite difference set，不是概率measure的熵符号；He接受bounded subset及cover数。若改取δ-net以便形式，也可在固定倍ρ上得相同(17)，不需要新的原标签。

## 11. 原mass／source闭包与He出口边界

总结第一目标：u0∈U_r，#A0,#B0=H^±Cδ^-1，ν(U′)≥H^-C，E g1_(A0×B0×U′)≥H^-C；X满足(16)(17)及N_δX=H^±Cδ^-1，Su和norm已真实支付。所有概率均相对原UniformYt×UniformYs×UniformZ，没有从分别BSG subsets强取交，也没有凭原每Theavy便宣任意time删选后逐管heavy。

所保g仍由原T及exact native pair／旧S_T产生，原wholeT/N/CW不变。若将原边数换回tube标签，最多只能从每T≤m个visits及每pair固定重数得δ²H^±C原管比例，不能说本rectangle是新nearfull AD4管族。Whole-time U′另用于source反设时仍按R22付η′及newallowed；当前有限提取不改原point Φ/slab或selected ξ。

第二／三目标需B/root实际给Tu-ball uniform cap及其floor到globalcoverlower、He参数次序。本文不把(17)当算子族coverlower，也不假Su irreducible。若Hecontrapositive给共同近稳定line W，真实返回是Tu把W0=T0^-1W近送W；两线可不同，不自动commonkernel／nearimage。phaseI的一满秩一rank1容量预算还需rank1端nonzero norm下界，否则strip宽另除该norm；本both-full证明不使用该未付子支。

## 12. 当前proof判定、独立反攻与待互审

第一目标已在上述原输入下实际证明：weighted anchor→retained-h metric三路径→共同rectangle的many原u→第二BSG／两次Ruzsa fullsum→同一X的small action。主要有限工具的保权和二维δ-conditioning都已显式写，不是原13.7 scalar statement的无证升级。关键高级外部输入在本目标前端为R76真实fine源模型；有限BSG/Ruzsa部分给了所需推导，不因作者名认证剩余whole source。

反攻已纳入h被选顶点丢光、原(u0)不在both-full、不同u子集不相交、metric中间标签碰撞、Tu压缩分母、Su施于δ误差、原q与δ²wholeT分母、X只有globalcover而非新ADlower。上述均在(5)–(17)处理。没有以自由native模型反例冒fullsource反例。

现已实际全文逐式读root十四节 notes/40_multiscale/sticky_matrix/R0078_native_common_action_and_fractional_stabilizer_application.md 和B十二节 notes/40_multiscale/sticky_matrix/R0078_fractional_operator_law_and_source_stabilizer_audit.md。B的原Tu-ball反设／pole／Taylor／whole-time newallowed／uniform比率与light-window绝对clock已独核：负(η+b+r)项确同时付ξ/µ及conditioning/µ，ρ与δfloor一致。算子cap不被外推到fineδ，而由δ^(d0/2) cutoff单调降κH给全部尺度coverlower；He在τ,d0之后、r/a/b/η之前选阈值，无参数循环。root全篇实际拼接和原mass／X输入也核过。没有发现未解决mandatory。

共同近稳定line的真实出口W0=T0^-1W未被冒成原commonkernel；未除ellv的二次cone保conditioning。B原F的adj表达式通过adj((F−Fs)A^-1)=A adj(F−Fs)/detA得到，linear项非零而归一需σ。两个fullrank代数校准的det／Te1／line及差矩阵均独算通过；它们缺fullsource，不反本结构归约。A第一目标的原retained-h／metric／Ruzsa／X链已由B和root实际全文独核通过，不将自身施工计作独审。

因此当前三目标不再停在given-X或given-cap：在原列明输入与具名高级工具下，真实g已给共同作用集，原source已给算子全尺度输入，He真返回有原质量的fractional二次cone alternative。此是结构应用，无fullrank branch-saving／完整κ1／ordinary gain。正式review及最终macro／next另待实际全文授权，不预认证metadata或同步；具名wholeproof及未经外部同行评审边界保持。按spec主gain机制仍保守noinfo1，不增ID／major／优先权，Goal active。
