# R0114：完整 rough source 的 ξ 球 cap 旧闭包与真实整管压力测试

2026-10-26，new_projection_gate。只写本分配稿；root统一整合。Goal仍active，六维17/4、ordinary五维严格超过4及完整rough/mixed出口均未改变。本稿不登记新ID、ordinary维数界或major，未经外部同行评审。

## 1. 目标恢复、首个候选及资格结论

恢复GOAL/STATE/ROADMAP/registry摘要和R113 next，运行context；定向读R104–108原code、same-T、moving-row、all-strip、terminal-ξ和各反攻范围。当前需要同时保原same T、filled二维X、point Φ/selected ξ、native Y及其各尺度联合、whole-T的4AD/CW和原N/I。完整矩阵33的κ=1端点未付；不回到CP/PM改名、两锚、同fibre免费collision、固定sections或三角迭代。

先检验的具体候选是：是否由完整输入得到一个新的原质量估计，限制整粒horizontal X上ξ集中于半径r球的比例，继而控制“bad grain”的总质量？结果为**拒绝其新输入资格**：更强的逐grain球cap已经是原Lemma19.4证明的concentration⇒CW半段。下面逐笔保原N证明这一点，不能把重新调用改名成新gain。Lemma19.2本身还有slow-variation前提，不对任意F直接套它；这里仅重用19.4中不依赖slow-F的充分性论证。

随后做一项不同的真实物理压力测试：构造同一组真实unit whole tubes，使其joint4AD、whole-containment CW，以及一个初始层的native Y tube-KT、filled X₂、Φ的AD/slab和ξ-coherence全部成立；整粒ξ的球cap达标，某一scalar投影却完全原子。再对这**同一原T**证明任何source-size后继点层的原访问密度均损固定正幂。这只否“初层数据＋wholeCW已给scalar耦合”的免费桥，不是完整source或ordinary反例。

停止条件：球cap若为旧统一重调用，不锁正候选；测试缺完整clock质量就明确记失败，不能替换Y、另换管或附欲证jointlaw救活它。本稿两条件都触发，无qualified新的完整source正gain。

## 2. 完整原输入与逐grain ξ-ball 的原N账

使用库内Wang–Zakharov 2609.22035v1，Def17.1–17.4；实际重读Def17.1–17.4、Lemma19.2 statement及19.4 proof的本段和后续。固定d=5、k=ell=3、0<κ≤2。以K=δ^{-Cη}统一有限次源费用；固定幂r^c不得吸入K。原whole T在bounded joint管参数chart中4AD，N=#T≈_Kδ^{-4}，CCW(T)≤K。原管不要求physical方向分离。

固定一个原时钟t及原native y。写

    p_x=(x,y+F_t x,t),  x∈X=X_(y,t),  #X≥K^{-1}δ^{-2},
    θ(T_(x,φ))=(φ,ξ_(p_x)+F_tφ)+Oδ,  φ∈Φ_(p_x),

其中每Φ为κAD，每个角有真实原管witness。对任意ξ₀及δ≤r≤c，令

    A={x∈X: |ξ_(p_x)−ξ₀|≤r},   β=#A/#X.             (2.1)

以下仅需本grain，不需要另假相邻grain上的ξ相同。δ分离packing给A中至少βK^{-1}r^{-2}个Cr分离水平位置；每个相应Φ的AD upper/总质量给至少K^{-C}r^{-κ}个Cr分离角。取分离常数充分大，得到至少

    M≥βK^{-C}r^{-2−κ}                                (2.2)

个原witness在**联合管参数**中cr分离。理由是固定t处的(point, slope)决定bounded graph轴，且从该chart回到(point at t, slope)有固定双边界；不同水平位置或角不能在此被合并。r≈δ的常数端点由packing吸收。

所有这些witness的**整段轴**均在下列affine 3-plane的Cr邻域：

    S={ (X, F_tX+y+(u−t)ξ₀, u): X∈R²,u∈R }.          (2.3)

确实，同一管的point+clock increment公式将normal偏差写成(u−t)(ξ_(p_x)−ξ₀)+Oδ。整轴的clock span有固定上界，所以误差O(r)；不是只将一个mark放入一粒。截取bounded区域并取固定倍凸prism U，|U|≤Cr²。

在(2.2)各中心附近取两两不交的cr联合参数球。原whole T的4AD **lower**给每球至少K^{-C}Nr⁴个原δ管；这些管的整轴亦在稍扩大的同一U内。故

    #{T∈原T:T⊂U}≥βK^{-C}N r^{2−κ}.
    CW: #{T∈原T:T⊂U}≤K N|U|≤CKNr².
    因而 β≤K^C r^κ.                                 (2.4)

整个膨胀仍以原N为分母，可包括原来未选为witness的原管，正是合法的CW测试。若只数(2.2)的fine管而漏掉4AD lower，会错丢(r/δ)⁴。若先删管再用删后族的AD lower，也不合法。

κ=1时，整粒ξ pushforward有r球质量≤K^Cr。于是在K^Cr<1的非平凡尺度，整粒ξ不可能全落一r-ball；这比初提的bad-grain平均估计更强，已旧付。原19.4在得到某grain的ξ集中后，正是用这一几何推出CW大；它后来使用slow-F、same-T和native tube-KT去**产生**集中。不得把后一部分的前提删掉后声整个19.4适用。

## 3. 合法restriction、平均与逐管及未付方向

(2.4)对原grain中任何满足同一ξ-ball条件的A统一成立，所以先选一组原points或原witness再重调用不会产生新的正幂。保留水平质量β时原分母仍是#X；归一到A后球cap常数至多除β。它也不保任意删管族的AD lower。

一般删管比例q、保原总访问比例p时，平均λ'=(p/q)λ，归一概率cap除q；平均heavy不能使每条原管都逐管稠密。本段只付原**水平质量**的球cap，没有声对每条原管的时钟质量。

尤其球cap不蕴含任意scalar ξ投影cap。一个1维分布可全部位于一条直线，仍有球质量O(r)；垂直scalar投影全为一个点。R72要求的是固定某horizontal坐标后的kernel-fibre basicness；R107所缺的是transverse row/secant law。它们都不是(2.4)的全二维grain球cap。下面用实际unit-T几何检验这个区分，而非只画抽象ξ toy。

## 4. 数字native Y与Φ：全部尺度的KT/slab先付清

复用R93已经记录的互补数字恒等式，不引用新的未读文献：

    A={Σ a_j4^{-j}:a_j∈{0,1}},
    B={Σ b_j4^{-j}:b_j∈{0,2}}.

自然独立等权Bernoulli法下，A×B是1AD；每位a_j+b_j唯一且均匀遍历0,1,2,3，故r+s是[0,1]上的Lebesgue概率。除可数4-adic歧义外，r−s是r+s的Borel函数。固定小常数c=4^{-h}，置

    Y=c{(r+s,r−s):(r,s)∈A×B},
    Φ=c{(u−v,u+v):(u,v)∈A×B}.                       (4.1)

两者仍1AD。写y₂=h(y₁)、φ₁=g(φ₂)只为概率计算；端点歧义集合零测，不假g/h连续或Lipschitz。y₁、φ₂各自均匀于[0,c]。

这里必须核native tube-KT，不能重复R106光滑抛物线的切线失败。将A×B作固定有界仿射归一化后，四个第一代子rectangle位于parent四角，各边比例1/4。对任意unit normal n，四个子rectangle中心投影的极差为(3/4)(|n₁|+|n₂|)倍parent尺度；每个子rectangle投影半宽为(1/8)(|n₁|+|n₂|)倍该尺度。因此足够窄于parent的strip不能同时碰四个子rectangle，统一最多碰三个。固定仿射变化只改常数。

宽ρ、长τ的tube包含于一个Cτ球。先用AD分离性在τ尺度取O(1)个parent，再从τ到ρ逐层最多三支；最后O(1)层及ρ-cover常数吸收。令

    α=log3/log4<1,   γ=1−α>0,

便有对全部δ≤ρ≤τ≤1的有限截断

    |Y_δ∩tube(ρ,τ)|_ρ≤C(τ/ρ)^α.                    (4.2)

故Y_δ满足原tube-KT(1−γ)。同样迭代，在宽ρ、长O(1) slab中至多C3^j个第j代块，占总4^j比例≤Cρ^γ；故Φ_δ满足slab-γ。有限δ以下不声连续lower。两者的1AD及全部尺度cover是同一数字构造，不借smooth Y来通过KT。

## 5. 同一真实unit whole-T，及其初层完整局部输入

令a=(a₁,a₂)均匀于[0,c]²，y∈Y、φ∈Φ独立，取真实直线

    x₁(t)=a₁+tφ₁,    x₂(t)=a₂+tφ₂,
    z₁(t)=y₁,        z₂(t)=y₂+t a₂.                 (5.1)

θ=(φ₁,φ₂,0,a₂)，L=(1+|θ|²)^{1/2}。每条轴严格截为−1/(2L)≤t≤1/(2L)，所以arclength为1；所有原轴有共同clock J=[−1/3,1/3]，并在固定bounded box内。T是该轴的固定半径δ管。不同t始终使用同一条原轴，没有换管/拼段。

初层t=0取E₀={(a,y,0)}，F₀=0、每个y的X_y为完整a-grid，且

    ξ_(a,y,0)=(0,a₂),   Φ_(a,y,0)=Φ.               (5.2)

每φ有(5.1)的真实witness。ξ场为真Lipschitz，Φ同一AD1/slabγ carrier，故初层所有allowed coarse-cube的ξ/Φ coherence成立。Y满足(4.2)，X₂满。ξ的整grain球概率≤Cr而第一scalar ξ₁≡0，正是(2.4)与scalar耦合之间的差别。

有限实现取δ=c4^{-n}，a在步δ网格上，A/B取n位截断；由数字分离，每Y、Φ有≈δ^{-1}个labels，X有≈δ^{-2}个，原N≈δ^{-4}。联合几何管参数与(a,y,φ)在固定bounded chart中bi-Lipschitz：从截距恢复a、y，从前两斜率恢复φ，余斜率为(0,a₂)。因此原T在所有δ≤r≤1是4AD，固定常数的管/point格重数均有界。本测试采用Def3.9明确允许的usual-tube版本：相近联合参数管整含于N_rT，反向由两个共同clock处的点恢复参数，故(20)与参数球计数可比。不额外把任意dyadic rounding宣成每个parent都保AD lower；格仅用于有限cover/marks，N不重置。

本族physical方向只有Φ和a₂提供的二维自由度，未供应ordinary四维完整角网。这里不做方向补齐并声仍保source。

## 6. Whole-containment CW 的原概率与有限原N证明

给上述原label空间自然概率μ。固定t≠0时，(5.1)的物理R⁴点分布具有

    ||dμ_t/dLeb₄||_∞≤C|t|^{-2}.                    (6.1)

逐步核算：y₁均匀，y₂=h(y₁)；φ₂独立均匀，φ₁=g(φ₂)。条件在y₁后，(a₂,φ₂)到(x₂,z₂−h(y₁))的矩阵为[[1,t],[t,0]]，det=−t²。a₁只将x₁平移t g(φ₂)，对a₁作Fubini即得(6.1)。g/h的粗糙性不影响这一条件积分；未作无依据的smooth Jacobian操作。

取共同far clock J_far=[1/8,1/4]。若整个原轴含于任意凸U，则对每个t∈J_far，其物理点在U_t。由(6.1)积分得到

    μ{whole axis⊂U}≤|J_far|^{-1}∫_(J_far) μ_t(U_t)dt
                  ≤C|U|.                         (6.2)

这是whole轴包含，不是只计某一mark；原概率未因U或t改变。

将自然label按finite截断对应的cylinder和a-grid cell分割，每个cell质量≈δ⁴，finite representative对应的整轴与cell内自然整轴Hausdorff距Oδ，因为(5.1)及unit截段端点对**几何参数**(a,y,φ) Lipschitz。若某finite δ管含于凸U，则对应cell的自然轴含于U+B_(Cδ)。U只要含一条δ管就含一δ球，凸性使|U+B_(Cδ)|≤C|U|：以该球中心作固定倍膨胀即可。由(6.2)

    δ⁴ #{T∈原T:T⊂U}≤C μ{whole axis⊂U+B_(Cδ)}≤C|U|,
    #{T∈原T:T⊂U}≤C N|U|.                         (6.3)

无管或无限体积时平凡。故这是所有凸测试体的原whole-T CW，常数独立δ；没有仅测axis-aligned boxes，也没有假physical方向分离。label-cylinder用于证明概率，实际计数仍是原finite distinct tubes。

## 7. 真实后继clock的原I损失：为何不能补成fullsource

这一步明确反攻本测试自身，而非把未验证输入留成清单。对任意固定t≠0，(6.1)与同一δ⁴-cylinder比较给：任意physical Cδ-ball至多碰

    C|t|^{-2}                                     (7.1)

条原finite T。比较可用未截的straight graph点来给upper，因而单位段端点不会增加访问数。δ≤|t|≤O(1)时常数统一。

现在允许任意δ-separated Z、m=#Z≥K^{-1}δ^{-1}，以及每个t上**任意**候选点层E_t，只有source要求的#E_t≤Kδ^{-3}；不要求其形状是特定Y/filled-X。令I_cnt为这些层与上述**同一原T**的实际selected visits，单管/单time重数有界。对δ≪r≪1，近clock |t|<r，每条管最多C(r/δ+1)次；远clock用(7.1)。因此

    I_cnt/(Nm)≤K^C (r+δ+δ r^{-2}).                 (7.2)

选择r=δ^{1/3}，得到

    I_cnt/(Nm)≤K^C δ^{1/3}.                        (7.3)

原N≈δ^{-4}始终未变。若要求原source I_cnt≥K^{-C}Nm，先取η充分小、后δ小便矛盾；不是把每个后继time单独换成新管族。即使允许任意E_t，其δ^{-3}容量亦无法承受原整管bulk nearfull访问，更不可能无损修成全部nativeY/coarse-union/filledX/Φ/ξ数据。

体积与计数分母另核：δ-cube marks每visit体积Oδ⁵，单管体积≈δ⁴，故I_vol≤Cδ⁵ I_cnt，平均λ=I_vol/(Nδ⁴)≤Cδ I_cnt/N≤K^Cδ^{1/3}，因为mδ≤C。并非I_cnt=I_vol，也非把正的point count误认为物理体积。任意更小可测marks只会减小此upper。

此模型通过的范围准确为初层原数据＋真实whole-T4AD/CW；它在fullsource要求的bulk时钟质量上**严格失败**。(7.3)只说这个构造不能提供fullsource反例，不能据其失败证明任意fullsource的scalar row cap。它和R106两锚抛物线的测试不同：这里初始nativeY的全尺度tube-KT和wholeCW已实付，失败由真实far-clock的四维点密度与原I容量给出；没有替换成Cantor Y后复用旧smooth Jacobian。

## 8. 宏观收缩与本轮止点

ordinary初始化/HRZ、完整rough/mixed、新finite输入和严格低维真实反例四个出口均仍需新的实际耦合。本稿识别出的full-grain ξ-ball估计已有原19.4闭包，拒绝新名称和newID；测试严格区分全vector cap与scalar/kernel-fibre cap。完整source的same-T跨时高密度正是本测试不能满足、且(7.2)定量排除的部分，不以desired jointlaw作附加已付假设。

这给一个具体止点：不再用“filled X₂＋Φ₁＋wholeCW”单层计数重复争取vector球cap；其最强直接用途已在(2.4)。也不把(5.2)当完整source row-cap反例。若将来重开，须从bulk same-T/coarse nativeY与原ξ场的**共同**作用推出不同的原质量机制，并同时通过restriction重调用检查；不是只添加一个scalar cap欲证假设。

没有新PDF/source，未认证前沿最新版或原论文wholeproof。实际新推导仅为上述旧cap账的明确化和不同真实压力测试；它们不产生Goal完成证据。root另选主任务，本文不自行开下一轮、不修改metadata、不作Git声明。

## 9. 留给后继的精确资格责任，而非新增成功假设

root要求保留一个可检验缺口。以下只给**强版审查标尺**，未锁新研究轮，更未证明其真或其为最弱充分输入：给定γ>0，是否存在a,τ>0及有限C，使η充分小于这些固定参数后，任意上述d5、matrix33、κ1的**完整**原source，在allowed尺度

    ρ∈R_η={δ^{jη}:j∈Z}∩[δ^a,ρ₀],  ρ₀<1固定，

对所有原t∈Z、y∈Y_t、固定unit row ν∈S¹和b∈R，都有

    #{x∈X_(y,t): |ν·ξ_(x,y,t)−b|≤ρ}
          ≤K^C ρ^τ #X_(y,t)?                       (9.1)

ν可以在不同grain另取，但在本grain的x/φ上必须固定；不许让ν依x选择零方向。若只要原I意义正质量的good grains，须另给其原计数及I下界，并支付删选p/q，不能将“存在一个good grain”视为(9.1)。moving row若依t，由事先固定的真实code functional及原F/anchors产生，也必须先写其依赖，不能事后按每个point最优选row。

完整输入的数量级不可省：每层native Y_t是AD1且tube-KT(1−γ)，#Y_t≈_Kδ^{-1}；每grain至少K^{-1}δ^{-2}个原水平点且至多Cδ^{-2}，故#E_t≈_Kδ^{-3}；每point Φ_p是AD1/slabγ，提供≈_Kδ^{-1}个实际原witness；m≥K^{-1}δ^{-1}，同一原T的总selected I_cnt≈_KNm。各allowed time cube的Y-union AD1及Φ/ξ coarse coherence全部保。usual/dyadic管规范和原bounded N≈_Kδ^{-4}、4AD/CW也须固定。γ不许跟δ先行趋零，ρ不得低于未经证明的原误差。

**旧lemma覆盖检查：**把ν通过一个固定有界normal rotation变为第一坐标，只将ξ分为(ν·ξ,ν_perp·ξ)；第二分量仍自由。scalar集中时整管至多近一个4-plane，测试体积≈ρ，联合packing/4AD inflation同样只给βK^{-C}Nρ，CW upper≈KNρ，正幂抵消。因此(2.4)不能坐标复用成(9.1)。原19.2要求整f在所有相关clock窗slow，19.4要求整tilde-f在某窗的正比例clock上slow，并随后以nativeKT制造**整vector**ξ集中；(9.1)的反设没有给这些整矩阵slow前提。降一normal维投影后也不能免费保商4AD、原CW及filled三维X来重新套19.4。

所以“从完整bulk point-size＋same-T Φ₁＋wholeCW推出(9.1)”若能成立，仍需实际新推导；目前不是旧19.2/19.4 statement的直接旋转调用。不过这尚不证明其正幂强度与旧完整gain不等价，亦未证明(9.1)能解决所有row/code出口；二者须在任何未来锁题前分别做restriction闭包与双向蕴含审计。§5–7的dust family只能说明缺bulk不可省，不能预认能补成fullsource，更不能把(9.1)当已付hyp。
