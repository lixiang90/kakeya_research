# R0062：真实四维有限输入、Nikodym质量与PW延长闭包

2026-10-18，A。已运行context并实际恢复GOAL／STATE／ROADMAP、78状态、R61 round／macro／next／receipt及R62先写spec／macro；原任务后按正式spec§7转finite Nikodym，§8补semialgebraic shadow／continuation。仅编辑assigned文件，不Git／spawn。具名四维完整证明仍是输入，未经外部同行评审，不声ordinary高维／major已达。

## 1. 原命题、排重与本轮真实转题

原完整PW4 bounded-projective gate仍要求map在包含完整原unit axes的共同域上有uniform pole margin／biLip；inside-pole裁剪不能冒完成它。C(a,M)只是原gate的等价量化，不新ID。R61 fixed-format line-parameter Σ子类不提供一般Σ，亦不再重证其常数。

本轮实际证明目标先为：对任意bounded R4原unitδ管族、逐管Lebesgue阴影密度≥λ≥δ^η，是否能以真实finite输入给

    |E|≥cσ δ^σ λ^5/[1+log(2/λ)] · |∪Ti|？       (1)

不假PW／Σ／原方向分离。原平均密度只先产生heavy-label族。之后核uniform wholeunion-PW4、nearfull shaded-PW4及完整adaptive gate的真正双向关系，不将同难题换名登记。

## 2. 实际来源：定性结论与finite输入严格分开

实际读OAI4 text9050–9142：原§11.3 Cor11.1给dim_H E≥1+dim_H D，随后借Keleti–Máthé同维推出segment union与supporting-line union的Hausdorff维数相等；原§11.4 Cor11.2借Gao–Liu–Xi给Nikodym set dim_H=4。它们没有字面给任意单尺度measurable Yi的统一质量估计。

root新存KM2203.15731v3（2023-07-17），本轮actual读text1–300／原前4页。§1.1 text111–121明确其法不处理“每方向上一条线与集合交正1D Lebesgue measure”的一般问题，也不证明Kakeya set猜想推出maximal猜想；§1.2的extension证明用dimension切片及可能穿原族的hyperplane，未付uniform finite常数。不能把非degenerate完整segments替换任意positive-measure marks。

实际读GLX2503.11574v1 text1–350及526–649：Th1.5是Hausdorff／Minkowski维数转移；Prop2.3的maximal等价则另要求完整K(p0)／N(p0)估计，不能由OAI4 headline dim_H=4授K(4)。其projective标准机制可用，但本轮须从DIR003真finite输入另付。

实际读WZ2502.17655v1 §1.6 text661–699及§12 text6439–6495：Th1.12′已经在R3给任意管族逐管δη shadings与任意R≥1 dilates的有限tube-doubling结论，费用R³δ^−ε。这是本轮四维fixed-R条件应用的已知三维类比，不以新名字冒优先权。本文不凭该R3定理直接给R4。

真正finite输入为SRC001／DIR003：对每σ>0有η_src>0，bounded R4 graph indexed原权ω_i允许重复，每条≥h^(−1+η_src)个真实visits，h-slope bin权≤α，则

    Σω_i #J_i ≤ Cσ α h^−σ #E_h。                (2)

其任意条数／partial-directions版本已由R9／R38 source读出支付；依赖完整四维证明及列明高级输入。本文只重读实际statement／量词，不重证175页wholeproof。

## 3. 更强的hyperplane-base有限Nikodym命题

固定bounded ambient／clock常数R、非短常数c0>0及σ∈(0,1)。存在η0,δ0>0使以下成立。原finite indexed unitδ tubes Ti的axes和所有Yi在固定bounded区域；支持线相对H={t=0}写

    L_i(t)=(b_i+t u_i,t)， |b_i|+|u_i|≤C_R。

给H内bounded witness bases a_i，使|a_i−b_i|≤C_Rδ。bases不必落在原unit轴内：只需靠近其完整支持线，实际轴／marks在共同bounded clock内。任意原正权w_i，总W；H上的每δ-grid bin原base权≤α。每条Yi⊂Ti可测，E=∪Yi，且|Yi|≥λ|Ti|、δ^η0≤λ≤1。则

    |E|≥cσ,R δ^(3+σ) λ^5 W/[α Lλ]，
    Lλ=1+log(2/λ)。                              (3)

常数不依#index、最小权、权跨度、重复支持线或λ。改变normal方向为有限coordinate directions、fixed-scale chart／homothety只改常数。若bases为Cδ-separated，α=O(1)，W=M即为hyperplane point-count版。

## 4. 共同真实格点与rich原权：不以NδE代|E|

取共同random grid Gξ=δZ4+ξ，ξ∈[0,δ)^4均匀。每个原tube在一个t-layer的空间截面直径O_Rδ，故最多C_R格点；其全部clock层至多C_Rδ^−1。记Z_i(ξ)为Yi中的格点数。准确Tonelli给

    Eξ Z_i = δ^−4|Yi|≥c_Rλδ^−1，
    0≤Z_i≤C_Rδ^−1。

取固定小c1，rich为Z_i≥c1λδ^−1，得P(i rich)≥c_Rλ。记rich原权W_r(ξ)=Σ_rich w_i，因而

    Eξ W_r≥c_RλW。                              (4)

无需不同i的rich事件独立。每个rich i每time层只取一个实际Yi格点（固定字典序），其数仍≥c_Rλδ^−1。所有这些是真实E格点；固定规则保证计数可测，有限样本自适应选shell不重置原prior。

## 5. pole剪切、shell、实际新分辨率与方向帽

在每个rich label的真实points中删|t|<c2λ；每层最多一个，丢≤C c2λδ^−1+O(1)。先取c2足小，λ/δ→∞后每rich原label仍留≥c_Rλδ^−1 marks。将其按sign(t)和dyadic τ≤|t|<2τ分壳，c_Rλ≤τ≤C_R，shell数≤C_RLλ。

按所有rich原权的**总mark质量**选一shell，使其≥c_Rλδ^−1W_r/Lλ；再删该shell内mark数< c3λδ^−1/Lλ的labels，只损至多一半该总量，因为待删原权≤W_r。保留族中每index均有此明确lower，且该shell的Σw_i marks≥c_Rλδ^−1W_r/Lλ。不会“每line选shell再按原权选class”而漏掉第二个log。

对选中shell只在真实points处用

    Gτ(x,t)=(τx/t, τ/t)。

其支持线准确变为(x′,s)=(τu_i+b_i s,s)。clock s∈[1/2,1]或[−1,−1/2]，后者作固定反射；whole model clock是固定有界区间，intercepts τu_i与slopes b_i均bounded。Jacob det DGτ=±τ4/t5，导数≤C_R/τ；这是cropped shell上的界，不声pole穿原完整轴仍uniform biLip。

取dyadic h≈C_Rδ/τ（常数选大使h≥δ）。每新h-time bin仅合并固定多个原δ-time层；实际points距image支持线O(h)，所以保每条≥c_Rλδ^−1/Lλ marks及其原权加权总量。像的h-slope bin只涉及b_i在Ch球，因b_i距base a_i≤Cδ，原base δ-bin权上界给

    α_h≤C_R α(h/δ)³≤C_R ατ^−3。                 (5)

这正是从δ-separated bases抽h-separated方向需付τ³的weighted形式，未免费保原α。τ可能依配置／grid，均在该uniform范围内。

## 6. DIR003调用与真实Lebesgue回传

选η0相对η_src足小，例如η0<min(1/10,η_src/4)。新perline density≥c_Rλ/(τLλ)≥c_Rλ/Lλ；当λ≥δ^η0，h≤Cδ^(1−η0)，δ充分小则上述density≥h^η_src。常数及log由严格η余量吸收，不假η_src对σ有线性模数。

记E′_h为image exact支持线事件的h-cells。每个实际原gridpoint只映为一个点，exact事件cell距它至多固定h邻接，所以#E′_h≤C_R#(E∩Gξ)。这是**点计数**，不以image邻域体积、Jacobian或NδE代原|E|。用(2)(5)及shell的总mark lower，逐grid实现有

    #(E∩Gξ)
      ≥ c h^σ α_h^−1 Σw_i#J′_i
      ≥ c δ^(−1+σ) λ τ^(3−σ)W_r/(αLλ)
      ≥ c δ^(−1+σ) λ4 W_r/(αLλ)。                (6)

σ<1、τ≥c_Rλ保证最后一步。空rich样本右侧0平凡。再用E#(E∩Gξ)=δ^−4|E|和(4)，得到(3)。多出的第五个λ来自rich概率lower，是保守可用费用；不将cell版λ4混为真实Lebesgue版λ4。任何点在端帽／clock边层仍按未clamp坐标选取，bounded clock先留fixed padding；没有按参数单点零测丢实体端帽。

若输入本来是δ-cells footprint、每条已给≥λδ^−1个axis visits，则无需共同grid rich概率，可直接从总marked mass开始，得到相应λ4/Lλ版本。该版本只控制footprint volume，不能反推任意Lebesgue E的volume。

## 7. 任意原管族、可测bases及fixed-R延长

令X为共同bounded可测base集合，每个x∈X有某原witness Ti及Yi密度≥λ，且x距Ti完整支持线≤C_Rδ，x与原unit轴的纵向距离有fixed bound；不假全局可测line selection。对X取最大L_Rδ-separated有限点集，数≥c_R|X|δ^−4，每点只选一个实际witness。固定四个coordinate normals中，每witness至少一个使方向time component≥1/2；按base点数选此chart，保固定比例。按δ-thick time slabs再选一层，保

    M≥c_R|X|δ^−3。

该slab中每base点距其轴在中心hyperplane的真实截距b_i为O_Rδ；原4D base separation与slab宽δ使每δ-intercept bin只含固定多个bases（或固定着色后δ-separated）。重复原witness在此最多固定次，不能保有无界同截距重复。应用(3)并以该H作pole，得

    |E|≥cσ,R δ^σ λ5 |X|/Lλ。                    (7)

只用了有限选择，且X若为有限管族的wholeunion则自动可测。更一般可测X只用于packing volume，选择的有限witness可任意，不构造不合法measurable field。

取X=∪Ti得(1)。还可取原axes的fixed bounded same-axis continuations或每个Ti的fixed R-fold dilate：这些bases离原完整支持线≤C_Rδ、纵向距离fixed，常数／着色均只依fixed R。故对每target ε>0，先σ<ε/4，再η0≪min(η_src,ε)，吸收λ5、Lλ及固定常数，可得

    |∪ R Ti|≤Cε,R δ^−ε |∪Yi|， R固定。          (8)

它是具名四维finite输入的条件性tube-doubling／extension应用，不声R依δ增长时还能免费保常数或最优R4。与WZ R3 Th1.12′的任意R及R³费用范围分开。

## 8. 平均密度只能先控制heavy-label扩张

若原给任意非负权及平均λ=Σw_i|Yi|/(VδW)，令H={i:|Yi|≥λVδ/2}。原I_H≥I/2；每条heavy有明确perline λ/2，(7)(8)控制U_H或其fixed dilates，不自动控制全部原zero／light shadow labels的扩张。整label partition与进一步删shading的密度责任分开。

不能省略这一步：无PW／角条件的一般族中，取N≈δ^−3，令δηN根不同但Oδ-near-identical的heavy管共用同一Cδ-tube阴影，其余labels为近平行满grid的light管、阴影空。平均≈δη，全部wholeunion体积≈1，但E体积Oδ³。故一般平均版本不能把U_H换U_all。此例不满足全PW，非本轮PW4／Kakeya反例；它只核真实任意族Nikodym结论的闭包边界。

## 9. 与DIR003的双向：用完整hyperplane模块，不夸relative-U版本

DIR003⇒(3)已完整证明。反向是近满密度正幂意义上的标准有限transfer：给原δ-separated graph slopes v_i、L_i(t)=(b_i+t v_i,t)、bounded参数、原perline≥λδ^−1 visits的δ-cell footprint。将每visit加固定小δ-ball可构成原Yi，|Yi|≥cλδ³且union volume≤Cδ4#E（端帽取真实轴point球，重叠只固定费）。

取固定R0>2R+10，以G(x,t)=(x/(t+R0),1/(t+R0))变换真实marks。原marks域上G及逆uniform biLip；image支持线写

    x′=v_i+s(b_i−R0v_i)， s=1/(t+R0)。

故完整支持线在s=0的base为(v_i,0)，δ-separated，且新slope bounded。可用固定长axis包络同时含这些base和全部image marks，统一fixed homothety后调用(3)。这不是给外包授PW，base也不必在原image marked segment内。得到|E|≥cδ^(3+σ)λ5 M/Lλ；λ≥δ^η且η充分小即恢复任意M的DIR nearfull union版本，进一步原direction-bin着色／权闭包就是R9原证明。

因此包含hyperplane-base估计的完整finite Nikodym模块与已付DIR在任意小正幂强度上互推，不新ID。单独relative-U inequality不在本文声称独立反推出DIR；它是该更强模块的推论。更不把nearfull λ≥δ^η的结论称4D full maximal all-λ／L4，η(σ)模数未知，中间密度不能免费补齐。

## 10. uniform whole-PW与任意nearfull shaded-PW同一正幂问题

记U4为：对每β>0有η_U>0，使全部本轮原PW4类Nδ^−3±η_U的wholeunion volume≥δ^β。记S4为同量词并允许任意平均≥δ^η的Yi，union≥δ^β。S4⇒U4取Yi=Ti即得。

反向固定target ε，先选β、σ≪ε并取U4给η_U、(7)给η_N。原η取小于η_U/10、η_N/2及ε/100。heavy H的原I_H≥I/2且N_H≥cλN≥cδ^(−3+2η)；restriction保原PW upper，常数／小幂余量使它满足U4的η_U类。因此|U_H|≥δ^β。用(7)及λ_H≥λ/2，得

    |E|≥cδ^(σ+β) λ5/Lλ ≥δ^ε。

这是全称restriction＋真实finite transfer，不是定性Hausdorff推uniform finite。U4本身仍open：测试H=∪Ti的格式随N增长，原PWA仅对fixed D且C_D可用，不能以a=1免费测试这个高复杂度union。该等价为同一主要gain问题的已付source桥，非新独立方向。

## 11. 一般n的fixed-format semialgebraic shadow估计

root／B正式§8给出另一个全类闭包，A独立核如下。固定n≥2、bounded S⊂Rn、半代数格式D，固定L足大，定义

    M_S(x)=sup_|v|=1 (2L)^−1∫_[−L,L]1_S(x+s v)ds，
    H_t={x∈B_R:M_S(x)>t}。

一维半代数fiber是uniform有限interval／point并，endpoint lengths经QE可描述，因此H_t及一个definable选择v(x)的格式统一，只依D,n,L,R，不依系数或t。选择使active s-set长度≥c_Lt。分层后在full-dimensional C¹ strata上|v|=1，故vᵀDv=0，Dv有left kernel。因此

    P_x(s)=det(I+sDv(x))，deg_s P_x≤n−1，P_x(0)=1。

若A⊂[−L,L]测度ℓ≥ct，则先在A中保|P|≤2ℓ^−1∫A|P|的一半测度，再取n个间距≥c_nℓ的点。Lagrange评价P(0)的系数≤C_Lℓ^(−n+1)，给

    ∫A |P_x(s)|ds≥c_Lℓ^n≥c_Lt^n。

对fixed s，map x→x+s v(x)在regular points的fibers由fixed-format半代数零维components给uniform multiplicity C_D。C¹ strata上先在compact subsets用area formula，再单调穷尽，避免免费global derivative bound；critical预像的Jac为0。故

    ∫_(H_t∩{x+sv(x)∈S}) |det(I+sDv)|dx≤C_D|S|。

积分s，再用逐x下界，得到

    |H_t|≤C_D t^−n |S|。                         (9)

低维x strata体积0不影响上界，仍包含在固定格式H_t中供后续PW测；不将其从原tube事件里任意删除。此lemma不是任意measurable S的maximal估计：fixed-format使uniform regular-fiber multiplicity成立。无新PW／角假设。

## 12. 原PW在bounded same-axis continuation下的真实闭包

设原unitδ indexed族在Rn满足PW #{avg_T1_H≥s}≤C_DKδ^(1−n)|H|s^−n，s≥δ。对任意原子族大小M，tail积分给

    Σ avg_T1_H ≤ δM+C_D M^(1−1/n)(Kδ^(1−n)|H|)^(1/n)。 (10)

新Pi为同半径δ、同支持线、长度上下固定且纵向位移fixed的continuation tubes。若avg_Pi1_S≥a，则沿同normal offset的parallel ray，原Ti每根横向fiber的轴向长度≥1（round unit tube），选择L含原Ti至Pi的全纵向范围，Fubini准确给avg_Ti M_S≥c a。这里保持相同normal δ-disk；若Pi半径扩大Cδ，outer annulus不能免费由原core ray捕捉，须另用R43 fixed-factor translation-kernel或直接(8)。far-unit continuation主应用没有此半径问题。

对M个满足新test的原indices，layercake先删t<ca/2的低层，再对H_t用(9)(10)。若a≫δ，δM项可吸，得到

    aM≤C_D M^(1−1/n)(Kδ^(1−n)|S|)^(1/n)
                           ×∫_[ca/2,1]dt/t，
    M≤C_D Kδ^(1−n)|S| a^−n log^n(2/a)。          (11)

若a∈[δ,Cδ]，原whole-ball PW给N≤CKδ^(1−n)，而只要M>0便|S|≥a|Pi|≥c aδ^(n−1)，(11)的无log右边已≥cKδ^(1−n)，粗付全部N。所有a≥δ因此覆盖，无漏threshold。

H_t fixed format只增长D依赖，log^n≤δ^−o(1)可按小幂余量吸收。结论只fixed bounded length／shift；不能以之删HRZ的ρ^(1−n) isotropic-zoom费用或R依δ增长的常数。没有去重、换原weights或给fake indefinite extensions授PW。

## 13. 全PW4 positive-gain与原whole-axis projective gate的逆向

完整gate⇒S4的正向沿DIR真实finite输入／共同格可付（保原访问、再只删light labels，角cap收费），S4⇔U4见§10。反向U4⇒gate现在可用(11)严格支付，先前缺口不再只作conditional框架。

原平均先heavy再选bounded-slope chart，保I_c≥cI，N_c≥cδ^(−3+2η)。固定far clock T>10R+10，把每根原支持线上的新**unit、同半径δ**轴中心放在t=T+1/2，完整新unit轴clock含于[T,T+1]。原PW经(11)与log小幂余量仍属U4的较宽η_U类，原N不去重。故far union U_far体积≥δ^β。

Fubini有t0∈[T−δ,T+1+δ]使3D截面体积≥cδ^β。截面每点距某完整支持线在t0的真实交点x_i(t0)=b_i+t0u_i至多Cδ；roundcaps只改此常数，不需恰在原far轴time内部。最大Cδ-separated交点子族因此有M≥cδ^(−3+β)。每个对应label都来自原heavy族，原|Yi|≥λVδ/2，所以

    I_sel/I ≥ c[MλVδ]/[NVδ]
             ≥ cδ^(β+2η)。                     (12)

取β、η≪target ε即保δ^ε原incidence。真实projective F_(−e_t/t0)在全部原boundeddomain分母1−t/t0≥c>0、biLip常数固定；新slope u_i+b_i/t0=x_i(t0)/t0，故选中的δ-separated交点给新角帽O(1)原label数。完整原Yi及whole axes均在合法pole-margin域，没有inside-pole裁剪。这证明U4⇒原adaptive gate的正向构造，输出有限fixed chart／map／piece费用已明确。

因此在具名四维finite输入下，U4、S4与完整adaptive bounded-projective gate在任意小正幂量词上同一难题；η需依次取小、不能宣线性模数。这次补的是全类continuation闭包／真逆向，不是已证明U4，更不是一般PW自动给大wholeunion。按AGENTS该projective gate不能再作为不同独立方向改名续轮。

## 14. 当前范围、停止与下一建议

本轮实际新付完整有限Nikodym原Lebesgue质量与fixed-R doubling／bounded continuation、semialgebraic shadow和PW continuation闭包，并借此严格识别原三种gain表述的双向。都是具名源输入的应用／结构闭包，未证明其中共同未解的完整PW4 gain；不新ID／重大性／高维维数声称，未经外部同行评审。当前whole-axis gate的pole要求仅在§13反向构造中使用，§§3–7 inside-pole工具明确不是直接gate输出。

下一R63须先周期macro。若继续共同PW4难题，建议只选一个原Guth–Zahl／Katz–Zahl真实四维broad-narrow中的**原三维carrier及跨carrier质量**步骤：先列已有有限输入、原directions／marks及所有piece费用，再问本轮same-axis PW continuation能否支付此前未付的global carrier匹配。不能只假局部wholeunion、再次新名rich-cap／pencil，或重算本轮τ／grid／λ常数；无真新跨carrier机制即换完整高维实际分支。此为一段候选建议，不在本轮另开数学或新primary检索。原Goal仍active，正式互审待root最终main／B／macro／next齐后完成。
