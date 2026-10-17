# R0074：原零维native标签到whole-tube CW矛盾

2026-10-18，root。完整规格已在研究前写research/rounds/R0074_working_spec.md。本稿完成原目标mixed42 κ1的源应用候选，交A/B逐式独审后才记内部reviewed，未经外部同行评审。标准半代数幂稳定不是新定理，旧有限矩/线性代数不宣重大或优先权。一般维度Kakeya Goal active。

## 1. 完整源命题和范围

固定γ>0、κ=1。η足够小、δ最后小，则不存在bounded原joint管参数图表中的完整WZ2609.22035v1 Def17.2–17.4 d5/k4/ell2配置，且C_CW(T)≤δ^-η。这里保两套grains、Z/absoluteclock、原T joint4AD、ξ/Φ/coherence和原selected witnesses等全部输入，不加AFF/quadratic/NQ、smooth/rational、good tuples/rank或原T physical方向分离。证中只需这些原数据提供的一部分上界和原质量，但不能因此略去完整源命题的适用范围。

bounded setup明确如既有R43及源Obs3.4(22)：原全部T在固定bounded joint-parameter盒，故N=#T∈[K^-1δ^-4,Kδ^-4]，K=δ^-Cη。不能只给usedT上界却将无界unused padding的分母重置成它。全部凸查询包含**完整原管**，原T分母始终保留；无界多copy泛命题不是这里的输入。

κ1使native tildeY_t⊂R为AD0，故每t的原δ-label数量≤K。原native三水平轴充分填充给#E_t≈_Kδ^-3，scalarΦ κAD供应每point≈_Kδ^-1个真实tube witnesses。原tube/time点碰撞和fineΦ-cell碰撞有界，所以每t至少K^-1δ^-4个不同原T有真实selected visit。不是只在轴线上任意构造一个终点，也不用tildef的smooth或Lip。

## 2. 可直接使用的原关联输入

令m=#Z≥K^-1δ^-1，ν=Uniform(Z)，μ=Uniform(T)。由δ-separation，ν(I)≤K(|I|+δ)。对每原(T,t)若有selected visit，选一个真实p及其native grain label y_t(T)∈tildeY_t；固定邻格/标签多重性仅K或固定倍，可固定一次选择，不删原供应的不同T。写G⊂T×Z为此二部图，则

    |G|≥K^-C N m，  deg_G(T)≤m。                     (1)

每个t的labels≤K。原whole管写x_T(t)=a_T+t b_T∈R4，λ(T)=(a_T,b_T)∈R8 bounded；β_t=tildef(t)∈R3 bounded。定义

    n_t=(-β_t,1)， V_t=(n_t,t n_t)，
    F_t(λ)=V_t λ。

一次真实边满足

    |V_t λ(T)−y_t(T)|≤Cδ。                          (2)

把a/b的normal分量写出即b0+t w−β_t·a0−tβ_t·v。V有一坐标恒1，norm在固定上下界内。原AD4给任何joint球B_r，δ≤r≤1，μ(B_r)≤K r4；这是joint参数的upper，未假任意子族有AD lower或physical角度分离。

## 3. root独立提取：有限row-greedy保真实tube子族

先删原degree<K^-C m的light T，阈值取(1)平均的一半。保真实H0⊂T，μ(H0)≥K^-C，且每T∈H0的**原全部**visits≥K^-C m。后续仅限制tube labels，不删它们的其它原visits，所以任意H⊂H0仍有|G∩(H×Z)|≥K^-C |H|m。这是实际逐管heavy，不从平均直接假每管dense。

取τ=δ^a，固定a∈(0,1/20)后于维数/基础常数、先于η。维护j个已选原times t1,..,tj，rows V_ti逐次距旧span>τ，L_j=span{V_ti}，以及真实Hj⊂H0：所有T在各anchor time有selected visit且取同一个原grain label yi。每一步保μ(Hj)≥K^-Cj，j≤5时Cj仅固定有限数。

令I_j为Hj的原全部visits。若dist(V_t,L_j)>τ的bad times所含edges≥I_j/2，则选一个实际badtime，使≥K^-C|Hj|管有visit；再按该time至多K个原labels选一label，得到Hj+1，比例损失仅K固定幂。所有既有anchor约束保留。若bad edges<I_j/2则停止；W={t:dist(V_t,L_j)≤τ}含至少I_j/2条原edges，因每time至多|Hj|条，

    ν(W)≥K^-C。                                    (3)

此时Hj是真实tube子族，不是单个好tuple。共同label只用于已选anchors，不要求label数值跨time相同，也不假不同times的访问独立。条件化time图没有免费变成ν正则law；(3)始终对原ν。

## 4. 4AD upper阻止第五个独立row

有界rows逐次距旧span>τ，j≤5的row矩阵R_j最小非零singular value≥cτ^j：row体积为Gram-Schmidt距离乘积≥τ^j，其他singular values上界固定。因此所有Hj由(2)距affine solution plane

    S_j={λ:R_j λ=(y1,...,yj)}

至多w_j=Cδτ^-j。row满秩，方程有解；可选一个实际T的正交投影作reference，故S_j的相关参数部分仍在固定bounded球。dimS_j=8−j。

若j=5，dimS5=3，其w5邻域在原bounded盒内可由Cw5^-3个半径Cw5 joint球覆盖。原AD4 upper给

    μ(H5)≤K w5≤K Cδ^(1−5a)。                         (4)

η最后小使(4)与μ(H5)≥K^-C矛盾。w5≥δ、≤1，查询合法。故第3节必在某j≤4停止（j0不可能，因||V_t||≥1）。得到mS=8−j≥4的同一affine S、真实H=Hj、原p=μ(H)≥K^-C，参数距S的误差

    ε_par≤Cδτ^-4， ν(W)≥K^-C。                     (5)

A另给tube-anchor/common-right矩提取：可在r4..7维affine carrier早停，原nearcarrier质量和commonclock均K固定幂，误差δτ^-C后同样接下文。两种提取是互补逐式检查，不以不同符号立两个方向。

## 5. 正交参数基、全4minors和原clock插值

用S的原joint Euclidean正交基Q∈R^(8×mS)，取bounded λ*∈S，则λ=λ*+Qz、|z|≤C。将Q按intercept/slope分块为[A;B]，A/B∈R^(4×mS)，norm固定有界，joint为isometry。物理evaluation pencil C(t)=A+tB。

对t∈W，V_t到L_j距离≤τ，而Q⊂kerR_j=L_j⊥，故

    ||n_t^T C(t)||=||V_tQ||≤τ。

||n_t||≥1，C(t)有固定upper，全部4×4 minors在W上≤Cτ。它们是次数至多4的多项式。由(3)和原ν interval upper，在W选5个两两gap≥cν(W)/K≥K^-C的原times；δ floor因δ≪K^-C可支付。Lagrange插值每个分母为4个gap的积，得到全部minor的全部系数最大值

    D(A,B)≤K^C τ。                                  (6)

这里只用5个真实原times，不声V的光滑/有理形式，不从一个孤立det坏点推出全pencil。mS≥7时isometric joint与近singular也会直接冲突，但下述统一处理所有mS。

## 6. 精确singular pencil的完整压缩证书

对bounded任意A/B∈R^(4×mS)，若rank(A+tB)≤3对全部实t，存在e∈{0,1,2,3}与原子空间K⊂R^mS、E⊂R4，满足

    dimK=mS−3+e， dimE=e， AK+BK⊂E。                (7)

证明：取最大rank r≤3的t0，替A为A+t0B，再用固定可逆基化A=[I_r 0;0 0]，B=[C D;F G]。在0邻域Schur complement恒零给G=0及FC^qD=0全部q≥0。U=span{C^q imD:0≤q≤r−1}有e=dimU≤r，Cayley–Hamilton给CU⊂U且FU=0。于是K0=U×R^(mS−r)，E0=U×0满足AK0+BK0⊂E0，dimK0=mS−r+e。还原原基后取K0中维mS−3+e子空间得(7)。r0时A=B=0直接成立。反向(7)使每个evaluation image至多e+(3−e)=3维。

证明存在K/E后，立即回原Euclidean orthogonal projectors，不用GL化基底覆盖原管；因此分类基底可能很坏不产生未计条件数。此压缩证书同时含多个right-minimal、regular/left退化，不只取一个Kronecker块而丢mS>4的费用。B给独立逐式同一证明及全部维数边界。

一手比对已实际读IKQS arXiv1307.6429v2的PDF1/3–5/20并视觉核1/20；§6.2明确二维matrix spaces是compression spaces，并追溯Atkinson–Stephens。故(7)为经典工具的重证，不是新的矩阵秩结构。完整25页PDF及提取文本已存literature；该文算法及其wholeproof未本轮独审，也未作为未付Kakeya输入。

## 7. 统一定量稳定：固定半代数基础明列

固定mS∈{4,..,8}及A/B的norm bound，定义

    Ψ(A,B)²=min_(e,K,E)
      [||(I−P_E)A P_K||_F²+||(I−P_E)B P_K||_F²]，     (8)

维数同(7)。Grassmann用P=Pᵀ=P²、trP=dim的compact多项式集合表示。最小化得连续半代数Ψ；D=0时(7)给Ψ=0。固定real quantifier elimination为具名标准基础（R31已使用）。以下实际证明所需power步骤，不以逐点连续性冒统一幂。

令H(s)=max{Ψ²:||A||+||B||≤C,D≤s}。compactness保证H(s)→0；QE保证其graph半代数。有限polynomial sign分解中，graph无二维interior，每点须落某个非零多项式零集，乘积给非零P(s,H(s))=0。除掉最大的公共s因子后，P(0,y)非零。若H不恒0，P(0,0)=0；最低非零y次j≥1给|P(0,y)|≥c y^j，而|P(s,y)−P(0,y)|≤Cs。因此H(s)≤Cs^(1/j)，即存在维数固定c*>0、C*，

    Ψ(A,B)≤C*D(A,B)^c*。                             (9)

若H在0邻域恒0则平凡。此经典半代数幂引理另与Coste作者2002讲义Theorem2.12实际网页缓存statement/proof比对；直接PDF请求403、镜像404，未声已下载或视觉核。本文重证(8)–(9)所需特殊步骤，但QE基础不声新独证或创新。固定mS/norm域使C*/c*不依δ或某最小非零minor。

## 8. 近压缩的真实whole-tube凸box

由(6)(9)选真实orthogonal K/E，使K方向在E⊥的evaluation泄漏≤K^Cτ^c*。取

    h≥C[δ+ε_par+K^Cτ^c*]， h≤c。

dimK⊥=3−e。原H参数的bounded z在K⊥投影以h-grid覆盖至多Ch^-(3−e)个格，某格所含**原μ质量**≥c p h^(3−e)。固定格中心z0，vary K只扫E+O(h)，所以这些原tube的whole axes均在真实(e+1)-affine plane

    {(a*+Az0+u+t(b*+Bz0),t):u∈E,t∈R}

的Ch邻域内。bounded clock、slopes和参数给e+1个长轴固定，余4−e轴宽Ch；δ半径及ε_par已由h支付。存在包含全部这些**完整原管**的凸box U，|U|≤Ch^(4−e)。于是对原全T

    C_CW(T)≥μ(T[U])/|U|≥c p/h≥K^-C h^-1。           (10)

不将T[U]分母改成H，不假H在S上均匀或有AD lower。若只控制短clock片段不能如此调用；本证由whole λ近S保证原整条unit tubes近Π，无R20 clock延长费用。

## 9. 参数顺序和完整κ1源矛盾

先固定维数/chart和(9)常数，调整c*≤1。取固定a∈(0,1/20)，τ=δ^a。root提取(5)有ε_par≤Cδ^(1−4a)，(6)(9)有泄漏≤K^Cδ^(a c*)。取s>0固定足小，例如s<min{(1−4a)/2,a c*/2}，h=δ^s。最后η足小，使所有有限K^C成本小于δ^(−s/4)，δ最后小吸固定常数；则h满足第8节，p≥K^-C且

    C_CW(T)≥K^-C δ^-s>δ^-η，

矛盾。第4节AD4矛盾同时因η后小、1−5a>0合法。γ可先任意固定；本方法未使用其更强额外信息，故仍覆盖完整规定γ的源。没有κ更改、没有假原tildef regularity、没有额外goodrank。

因此完整bounded d5/k4/ell2、κ1 source在所列标准QE基础及完整原输入下排除。A用不同anchor迭代亦能给同级ε_par/ε_min/p，交B的(9)(10)得到相同结论，须在正式全文互审后才归内部已审。

## 10. 一般维数读出及没有完成的加强

本链的有限关联形式可将4替n=d−1、8替2n：n+1个τ-independent rows会把原n-Frostman tube law困于(n−1)-plane；停止后mS≥n，n-minors次数≤n，n+1个分离clock点插值。精确maxrank r≤n−1的同一Schur可达空间证明给dimK=mS−(n−1)+e、dimE=e≤n−1。固定维半代数最小化和正交cover给补参数n−1−e、物理凸体短轴n−e，仍一幂CW差。

故对每固定d，上述同型有限关联命题可排除bounded原n-Frostman/CW管族在近满原clock以次幂少量移动hyperplane labels承载次幂dense真实visits。用于Def17的k=d−1、κ1时，原point/grain供应亦为每timeδ^-n，因此相同方法覆盖这些限定源case。常数依d，未宣dimension-uniform或新的ordinary Kakeya下界；有限线性代数不代全部source/general-to-sticky/Hausdorff。

没有证明所有κ<1，也没有以本端点自动得定量uniform邻域或κ≤1−ε的新结论；如需该加强须完整重新计label正维成本，不在本轮另开阈值方向。ordinary小union仍未自动给这里的global moving-hyperplane AD0合同。Goal完成标准不变。

## 11. 反攻、旧账与实际意义

R19任意单残差β的wholeclock三维投影是有paid normalform的旧源应用；R20的local窗口不能代本whole图。R45正维endpoint字母表和good-star成本未被免费省掉，本轮真正额外原输入是AD0标签≤K。R64的edge-only rank反例不适用，因为这里先付同一个真实tube子族S和足原clock的同pencil；R72两marginal/basicness冻结没有撤销。本证不从raw V span冒claim无原质量，也不假所有labels的值恒定。

constantβ、parallel/commonridge、含left-minimal的singular pencils由(7)(10)实际原CW收费排除；joint基mS≥7时的小minor甚至常数不可能。没有构造fullsource或Kakeya反例。若无bounded原N/原质量或只短片段，则(1)(10)范围不适用；这些旧scope要求明确保留。

当前实际收缩的是完整mixed42 κ1源case，并有固定维同型有限关联应用；不认证新颖/major或普通五维增益。精确compression、QE幂和有限矩均是基础工具，需一手优先权比对才可能谈新独立结构；本轮不增数学ID，不降低长期Goal。

## 12. 独审与停止合同

待A/B实际全文逐式审root12和对方稿、spec5、文献范围及next后，两formal及root整合分别归档。须独核原N/CW分母、label和time重复、row条件数、近3planecover、fixeddegree插值floor、Ψ连续半代数及zero implication、whole管凸box和固定参数先后。未经外部同行评审。

完成后停止本AD0 endpoint/finiteanchor优化，不把增加固定times、正维label阈值或proper rational类别改名成下一机制。完整高维目标中的其余κ/matrix/ordinary责任继续；下一唯一须有真实不同原输入或高级估计并先排旧等价。文献/状态/registry与同步按真实执行另记，Goal active。
