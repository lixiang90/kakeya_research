# R0072阶段II：原common-kernel的同管双终时响应与原质量

2026-10-18，A。已实际读本轮spec5中先锁的阶段II。只编辑获授权文件，无Git／spawn／metadata。完整Goal不变；以下真正使用原same tube，而非把两个独立arms拼成图。当前没有证明kernel basicness或完整common-kernel排除；第7节实际排除其γ>1/2参数子范围，有限恢复公式不冒原商3-AD。

## 1. 原模型、单位与不能删掉的root坐标

完整WZ Def17.2–17.4，d5／k=ell3，0<ζ<κ≤2、0<γ≤1固定，η最后小，δ最后。这里Y为二维AD(2−κ)，**不是**R70 mixed43的scalar Y；不能挪用其κ≤1或γ≤1−κ剩余范围。考察真实common-kernel f(t)=F0+u(t)eᵀ；共同bounded shear／horizontal rotation后写f(t)=u(t)e1ᵀ。u仅原dyadic Lip，不假smooth／rational／goodrank。若u整个像共线，已有common-image／pencil接口另按其已审范围使用，不把它另立成果。

原点坐标写

    p=(x1,x2,y+u(t)x1,t)， y∈Y_t⊂R²，
    θ(T)=(φ1,φ2,ξ_p+u(t)φ1)+O(δ)。

沿同一原T到actual mark p_s@s，h=s−t，原native标签是

    y_s=y+hξ_p+[u(t)−u(s)](x1+hφ1)+O(δ)。          (1)

式(1)不能无声删除[u(t)−u(s)]x1。固定root (y,x1,t)时，可定义中心化response

    yhat_s=y_s−[u(t)−u(s)]x1，
    yhat_s=y+hξ_p+h[u(t)−u(s)]φ1+O(δ)。             (2)

这是依root已知数据的改写，不是所有root共享的全局坐标变换。φ2没有出现在(1)／(2)，但原tube／angle labels全部保留；不能把不同φ2管视为一个管。

原X_y,t只有δ-separated、δ^η-full cardinal，不保证exact实数x1 fibres大：可微扰每个x1使之全不同。以下finite kernel fibres均指原y、t及**dyadic δ-bin of x1**固定的厚fibres。用bin代表替换x1在(1)只增O(δ)，这足以研究ρ分辨率basicness；它不是新exact Cartesian lower。

## 2. 原空间不缩q的三类core

固定原allowed ρ及其time窗J，记Z_J、m=#Z_J。保该time窗内**全部空间**E_J，不先把x2缩进一个physical ρ-cube；后一做法在同cube内ξ的ρ-bin O(K)本已是原coherence，不能解决global kernel basicness。

由full Y的2−κ AD、filled X的二维card和原point方向供应，K=δ^-O(η/γ)记有限源费用，可写

    P=#E_J≈_K mδ^(-4+κ)， I≈_K P D， D=δ^-κ。

used tubes穿过bounded E且方向bounded，落在固定多个unit joint-parameter boxes；原T joint4-AD upper给#used T≤Kδ^-4。unused T／原CW分母不删改。厚kernel fibre数至多

    F≤K mδ^(-3+κ)。

在实际incidence edges上，对point、tube、厚kernel fibre三类peeling，阈值分别取I/(6P)、I/(6#used T)、I/(6F)。一个vertex仅充电一次，保≥I/2 edges。每active point度≥K^-C D、每active tube访问≥K^-C m、每active厚kernel fibre至少K^-C δ^-1个actual points（以原point degree upper KD除其edge lower）。组内x1宽δ，故一个x2 δ-cell只有固定个δ-separated points；也有同阶真实x2-cell lower。

此core只给其明确的原count lower，不授新Def17／AD lower、不把pruned Φ说成完整AD族。原Φ的ball／slab upper仍可在active point按其K^-C比例保留。完整原label若Y不动，逐管密度可保；本次time／edge删选只给逐active tube已付访问lower及原总平均incidence，不保证每个原tube原逐管密度。

## 3. 不先假Δu非退化：可由原local19.4付一次clock筛选

k=ell3时tildef=f，named Lemma19.4的native Y tube-KT输入确为本完整模型。设0<β<1、σ=ρ^(1+β)，ρ∈[δ^(1/4),δ^µ]。若某原窗J、某ball B_σ有

    #{s∈Z_J:u(s)∈B_σ}≥δ^v ρ/δ，

取该集合中实际s0作anchor，全部u与u(s0)距离≤2σ；原#Z_J≤Cρ/δ，故满足19.4的原分母比例cδ^v。σ∈[ρ²,ρ]、ρ≥δ^(1/3)，得到CW lower

    δ^{C(η+v)/γ}ρ^(-βκ)。

先取v≪µβκγ，再η小，与原CW upper矛盾。故每个width Cσ的u-ball有absolute time upper Cδ^vρ/δ。这里调用原完整配置／原分母，不把单q或两个孤立times当global新配置，也没有重证19.4 wholeproof。它是common-kernel模型下的已知小variation工具应用，不等于本轮主目标。

为取两终时，轻time窗可先按全局#Z阈值合法删整窗，保证所用m≥K^-Cρ/δ；或者对已有满足该absolute lower的窗直接工作。若某窗没有此lower，不能把relative fraction代替它。下文只在这个实际已付范围计数。

## 4. 真same-tube的双终时质量和边际

令active tube的实际visited time set为Z_T，n_T=#Z_T≈_K m；固定T／time交点有限重数计K。对每个实际root incidence (p@t,T)，取同一T上的ordered s1,s2∈Z_T。先删|s_i−t|<qρ，原δ-separated clock及n_T lower给比例upper K^C(q+δ/ρ)；再删|u(s1)−u(s2)|<σ，由第3节absolute cap给比例upper K^Cδ^v。q=δ^b中b先固定小，源损失最后小，且δ/ρ floor保留，故每个active (p,T)仍有≥K^-C m²个真实pairs。

总量直接为Σ_T n_T³，故

    #C≥K^-C I m²。                                  (3)

所有三次都在同一tube的visited set上，没有以两个独立arms、Markov闭包或分别dense图取交替代。固定root incidence的upper≤K m²，故其边际受K^C Uniform(I_core)支配，own Φ/slab mixture按原point最低度可付。固定terminal pair (s1,s2)后，root incidence数至多Σ_T n_T≤K I，故新terminal-pair marginal也有

    law(s1,s2)≤K^C Uniform(Z_J)²。                    (4)

这两项domination来自本图重新计数，不来自R70或R67名称。再固定一个厚kernel fibre、或一个time pair，通常会改变这些边际；只能按真实保留质量重算，不能把(4)无损授给所有条件图。

## 5. 双响应的有限恢复与实际分辨率

对good pair设h_i=s_i−t，A_i=u(t)−u(s_i)，|h_i|≥qρ，|A_1−A_2|≥σ。以原native labels计算

    R_i=[y_si−y−A_i x1]/h_i
       =ξ_p+A_i φ1+O(δ/(qρ))。

从而

    R_1−R_2=[u(s2)−u(s1)]φ1+O(δ/(qρ))，
    ξ_p=R_1−A_1 φ1+O(δ/(qρ))。                       (5)

只需一个nonzero向量Δu即可恢复scalar φ1，不需要两个u-vectors spanning R²或额外goodrank。若各terminal native label只知到ε≥Cδ，则两组未知参数可能值的diameter upper为

    diam φ1≲K ε/(qρσ)，
    diam ξ≲K ε/(qσ)，                               (6)

其中|A_i|≤Kρ，所有坐标在同原time窗；没有使用smooth derivative。若要分别恢复到φ1的ρ-bin、ξ的ρ-bin，足够取ε≤c qρ²σ、ε≤c qρσ。原fine δ可以在参数后小范围满足这些floor，不能把它说成任意粗Y网格均可逆；若clock很短或Δu很小，必须保(6)的实际代价。

φ2仍完全不可见。即使(ξ,φ1)已定位，原point Φ_p在一个φ1-strip内仍可有多条φ2不同的管，只有原slab upper K w^γ D可用，不是假定一个tube。精确输出对三个变量的injectivity不等于tube-label fibre为常数。

## 6. 恢复不是basicness：实际label与count尝试

对固定厚root fibre (y,x1-bin,t)，basicness要控制的是其**全x2长度上的**ξ_p image在ρ的bins；每个physical ρ小段内O(K) bins只是原coherence，不能用它覆盖整个kernel fibre而省掉约ρ^-1段。

(5)把不同ξ_p送到不同响应，并未使响应相同或稀少。两终时的actual output为两个原Y_si的labels，各为2−κ维AD，数据落在Y_s1×Y_s2而非一个共同低维scalar carrier。它们可以与root／time／tube全部相关；固定两个终时不能直接给它们乘积独立性，更不能从投影π_nY_s得到1−κ维upper。native Y是二维，投影可以是一维满集。

对每root fibre、times和ε网格，最直接的upper仅是两个Y-patches各自的cover乘积；全局可达ε^(-4+2κ)，在局部有已知ρ² response range时也只是K(ρ²/ε)^(4−2κ)。即使再用(6)恢复，也没有得到ξ在ρ的K-bin upper。新core只保输入x2点多，不给非constant ξ像一维lower或一个固定line内的均匀image law。不能以“Lip且非constant”替代这一点。

若先把terminal labels固定到同两个bins，确可迫ξ近同值；但为固定这些labels付的原count／cover与选中质量必须计入。当前没有证明可保δ^a（a相对后续参数任意小）的原访问且只固定K个label pair。把固定数据后的代数恢复冒该质量提取，就是需要避免的跳步。

## 7. 原Y tube-KT实际排除γ>1/2子范围

固定root p、ξ_p、t和s后，φ1变化的(1)输出沿方向A_s=u(t)−u(s)的一条line，长度约ℓ=|h_s||A_s|≤Kρ²。若A_s=0，此输出不含φ1；good双响应至少有一个|A_s|≥σ/2，但仍须保非短clock。

对ε∈[δ,ℓ]，原Y_s tube-KT给line-neighborhood的ε-cell数≤K(ℓ/ε)^(1−γ)。原point Φ_p在一个φ1-strip、宽w=ε/ℓ内的管数upper≤K w^γ D。因此逐cell恢复和相加的直接upper是

    K D (ℓ/ε)^(1−2γ)。                              (7)

取真正fine ε=Cδ，固定常倍tube宽度及δ-separated Y只改K／维数常数。沿line长度ℓ的每个terminal Y-cell反推φ1区间长O(δ/ℓ)；ℓ≤Kρ²<1使该slab查询宽度不低于原δ-base。原selected方向的每个fine φ-cell只对应固定数穿过p的δ-tubes，故不会漏管label重数。δ-tube／point Oδ误差用固定邻接cells和加宽Cδ管包含；不能令误差为零，但它不改幂。

对第4节good triple，至少一个i满足|A_i|≥σ/2、|h_i|≥qρ，故ℓ_i≥c qρσ。按这个terminal index分成至多两类。每类固定root p及s_i后，用(7)界可能T，再让另一terminal time任取至多Km个实际visits，得到

    #C_good≤K^C P D m² [δ/(qρσ)]^(2γ−1)。             (8)

另一方面(3)及原I≥K^-C P D给#C_good≥K^-C P Dm²。置q=δ^b、σ=ρ^(1+β)，ρ≥δ^(1/4)给

    δ/(qρσ)≤δ^((2−β)/4−b)。                         (9)

先取β∈(0,1)、b<(2−β)/8，并在第3节v及这些固定参数后使源损失小。若γ>1/2是固定正gap，(8)的δ正幂比(3)的任意小源损失更强，矛盾。因此完整common-kernel源在具名19.4等输入下确排除γ>1/2；没有借R70的mixed43结论。它不要求ξ basic、smooth、goodrank或φ1有κ维投影。

对γ≤1/2，(7)的直接upper没有positive saving，不能把KT exponent写成1−κ或把φ1投影免费升成κ维law。原point AD／slab另要求γ≤κ也不把γ≤1/2情形排掉。

两个不同消φ1 normals在两终时能联合恢复ξ，却对应不同二维Y_s／不同line测试；它们不能无证当同一个scalar低维output交叉。要处理γ≤1/2仍须真正原coupling的平均几何估计，当前双time响应本身没有提供。

## 8. 审计终点、独立攻击与范围

已付：原native标签的完整x1项、合法中心化；保持global kernel范围的厚fibre／point／tube core；同一tube两终时原质量及两个真实marginal；不先假rank的u-separation source筛选；精确恢复误差／φ2余重数；以及原KT真正排γ>1/2的子范围。曾误将mixed43的κ／γ范围移来，经root指出已修，数学判断以本稿第1／7节终版为准。没有以单管两time数值公式就宣primary目标完成。

独立反攻应保full X只为card，不假连续interval；nonconstant dyadic-Lip ξ可以用digit masks隐藏image尺寸和局部线性coercivity。B负责这种局部校准，其结果须明确哪些Φ／coherence／同管关系真正保留，不能升级fullgrain／全T CW反例。本稿尚未凭校准断言完整common-kernel不可能。

截至本文，尚未从双time图给global kernel basicness、R59典型invisible fibre lower、商joint3AD／密度／κ亏损，或γ≤1/2的完整common-kernel矛盾。γ>1/2子范围应用不能替代这个目标。若root／B没有另付足量的新共同质量，则依先写spec应将basicness主机制记no-information并冻结，不续更多fixedtimes／mask阈值／Markov-BSG或增加smooth等proper假设。高级19.4／good-q等wholeproof仍具名，未经外部同行评审；ordinary初始化、其它matrix／mixed及general Goal保持open，无新ID／major或普通新界声明。
