# R0075：真实同管 GLOBAL clock、raw 秩一差缩减及近共同像用途

2026-10-18，A。实际全文读终版working_spec5的阶段II锁题、R64主稿12节、R16 linewise／weighted-coarsening／原tuple三稿及其finite theorem、R22整时间闭包5节，并重新读取原19.2／19.4／20.2的statement及相关proof输入。只编辑本分配稿，无Git／spawn／元数据。本轮目标是完整bounded matrix33在κ>1的范围，不能以given-raw分类或κ1 proper类替代。

## 1. 完整输入、原分母和参数先后

固定ζ>0、κ∈[1+ζ,2]、原γ∈(0,1]。输入是WZ2609.22035v1 Def17.2–17.4 d5/k=ell3的全部原数据，并显式保原全T bounded jointchart、N_orig≈_Kδ^-4及normalized CW≤δ^-η的R43规范。F:Z→Mat2 entries bounded，E_t={(x,y+F_t x,t):y∈Y_t,x∈X_(y,t)}，Y_t为AD(2-κ)，X有δ^-2的次幂filled量，Φ_p为ADκ／slabγ，ξ／coherence不变。κ不因投影／删选而改。

先固定b>0足小依ζ，例如b<min(ζ/100,1/100)，之后固定raw classification所得误差指数c>0（可放宽取c=b/10）。后选µ>0足小使4µ<c，µ<1/8；再选linewise标量输入允许的ε0、SM质量指数ε_SM和坏窗质量指数a_B；所有这些先于源η，δ最后。具体SM不等式在第8节列出，不能把fixed b或µ费用塞进K。K始终为Cδ^-Cη的固定幂，若调用最终time-restricted配置可统一写δ^-Cη_g，η_g=Mη且M固定足大。

原T/N/CW分母始终保留。若仅给used T bounded而原unused padding无界，下面实际原概率及最终sticky读出均不自动成立；不把这一不同范围默认为已证。无physical方向δ分离、smooth／rational、goodrank或kernel-basicness公设。

## 2. Fine native单管响应和全部标签重数

固定原p=(x,y+F_t x,t)、实际原T∈T_p及其细方向φ∈Φ_p。若同一T在s还有实际selected point，h=s-t，则

    y_s=y+hξ_p+(F_t-F_s)(x+hφ)+O(δ)。               (1)

F、ξ和原slope bounded，故tube／point邻格的误差是固定常倍δ；这是fine实际公式，不是coarse L误差ρ³。式(1)保 root坐标x和原ξ，不能仅剩h(F_t-F_s)φ。

每个p及fine Φ δ-bin选一根源已给的实际管见证；固定φ-bin只有固定数dyadic tubes through p，一个tube／time只有固定数δ-separated实际点。若原grain labels在同δ-ball重叠，按R16原filled和E packing给至多K重数。所有这些原点／角／管碰撞均统一计K，不把原labels去重后改用无来源prior。

令D0=δ^-κ、P_t=#E_t≈_Kδ^(-4+κ)。每point实际初管度≈_K D0，因此每time原selected incidences≈_Kδ^-4。固定T/time选择一个实际canonical visit，损固定倍，得到原GLOBAL图G⊂T×Z，m=#Z≥δ^{η-1}，|G|≥K^-Cδ^-4m，且每T/time至多一边。

## 3. Invertible two-time bound的实际fine尺度

固定(p,t,s)，设D(t,s)=h(F_t-F_s)，smin D≥H、0<H≤1。对任一原Y_s的δ-cell，(1)允许的φ落在半径Cδ/H的ball内。原Φ_p的κ-AD upper直接给至多K H^-κ个fine角labels（H很小时取全Φ upper亦不更坏）；每个角cell的实际管重数K已付。因此

    # {T∈T_p:该T在s有selected visit}
       ≤K H^-κ #Y_s
       ≤K H^-κ δ^(-(2-κ))
       =K D0 H^-κ δ^(2κ-2)。                         (2)

这里只用**全部**Y_s的绝对card upper，不假两Y独立、projection Y降维或pruned Φ保ADlower。物理逆像ball半径是δ/H，不是δ，也没有从可逆解式就宣一根管。若H<cδ，式(2)可退为全D0；实际用途H≈δ^(2b)≫δ，因此查询合法。

若|t-s|≥δ^b且|det(F_t-F_s)|>δ^b，因||F_t-F_s||≤C，smin(F_t-F_s)≥cδ^b，故可取H=cδ^(2b)。式(2)为K D0 δ^(2κ-2-2bκ)，κ≤2时saving≥2ζ-4b。这是κ>1的真维数差，κ1时不提供正saving，不能据此重开其basicness。

## 4. 原tube-heavy和真实sameT Gram

从第2节原GLOBAL图删degree小于其平均一半的light tubes，得H0⊂原T；每条余管的**全部原访问**Z_T满足 n_T≥K^-Cm，#H0≈_Kδ^-4、μ_orig(H0)≥K^-C。原未用T和CW分母不动。

定义真正的sameT pair measure

    M(t,s)=Σ_(T∈H0)1_(Z_T)(t)1_(Z_T)(s)，
    Btot=Σ_(t,s)M(t,s)=Σ_(T∈H0)n_T²≥K^-Cδ^-4m²。 (3)

两个终时属于同一条原T；不是从两个独立arms或一个任意related g拼出来。上界每个time pair ≤#H0，但最终选clock不靠抹去该measure的边权。

短clock：固定T，δ-separated原Z使每个t附近|s-t|<δ^b只有C(δ^b/δ+1)个s；除n_T≥K^-Cm且m≥K^-1δ^-1，短pair≤K(δ^b+δ)n_T²。长clock且det-large：按t,s及该管在t的canonical p计数，第3节给

    Blarge≤K m² δ^(-4+κ)δ^(-(2-κ))δ^(-2bκ)
          =K m²δ^(-6+2κ-2bκ)。

同一tube/time点的固定多重性已在第2节支付。结合(3)，把短clock也记坏边，得到

    Bbad/Btot≤K[δ^b+δ^(2κ-2-2bκ)]
             ≤K[δ^b+δ^(2ζ-4b)]≤δ^(b/2)。           (4)

最后一步以η在b后足小、δ最后实现。没有把全time raw badpair比例直接当原tube pair比例；(4)正是实际源计数给出的Gram加权比例。

## 5. 一条原heavy管返回GLOBAL raw全pair先验

将(4)按各实际T的n_T²分解，存在原T*∈H0，其完整原访问clock

    S=Z_T*， #S≥K^-Cm≥K^-C#Z，

在Uniform(S)²下满足

    Pr{|det(F_t-F_s)|>δ^b}≤q， q≤δ^(b/2)。          (5)

短clock已在(4)坏预算中收费，(5)可以忽略其标记，只使upper更弱。选择的是**一根原管的全部访问times**，不是再挑一个cross-only edge子图；每个S-time随后保原E_t整层，绝不把T*本身当新AD4管族。

这是R64 arbitrary g-edge hyperbola反例不直接适用的关键：本次det只依t,s，而实际选出的pair reference确实是一个集合S的完整自乘积。T*可有非均匀来源，但选择完成后采用Uniform(S)，其interval cap由δ分离和#S≥K^-Cδ^-1直接给K(|I|+δ)。没有假所有管有共同clock，也没有对任意相关g免费换raw law。

## 6. Raw分类、原质量保留与整time闭包

以ε=δ^b、a=δ^(b/8)在S的raw prior调用已内部审的R64有限定理；q≤δ^(b/2)给删除至多4√q。余W⊂S有#W≥(1-o(1))#S≥K^-C#Z，并落以下之一：

    近常：||F_t-F0||≤δ^(b/8)；
    近kernel：dist(F_t,F0+{u eᵀ})≤Cδ^(3b/8)；
    近image：dist(F_t,F0+{v rᵀ})≤Cδ^(3b/8)。         (6)

e／v为同一个fixed unit vector，original coordinates中范数常数固定。统一误差可放宽为ε_alg=δ^c，c=b/10；近常归近kernel也合法。本分类需要的q／ε／a及operator norm参数全部真实，不预假原det多数小。

只删**整时间层**至W，保原T、每层原X／Y／Φ／ξ与全部witnesses。R22说明跨time Y-union lower由任一保留单层lower给出、upper由原union继承；原Φ_q coarse集合不删、coherence及tube-KT upper保留。原N／CW完全不变。新time数与所有常数只损K固定幂，可预取η_g=Mη、M固定足大，且为原η整数倍，使新allowed格为旧格子格。

后续所有near-full删whole windows可预留在同一个η_g预算内；先确定有限总loss常数再固定M，并选ρ∈δ^(η_g Z)∩[δ^(2µ),δ^µ]。η_g≪µ时存在该格点，2µ<1/4保ρ≥δ^(1/4)。这样不合并不同fit窗口冒慢变，也不因之后一次常数比例删层另换ρ。有限图删选与完整time配置的用途在此严格区分。

## 7. 近常出口和近image的真实working误差

若近常支，W上F_t均距F0≤ε_alg。µ选到4µ<c，故ε_alg≪ρ²。任意W anchor在其ρ-window中，对全部保留times有|F_t-F_anchor|≤ρ²。named19.2在该完整W配置上取σ=Cρ²给CW≥δ^Cη_g/γ ρ^-κ，与原CW upper冲突；all-anchor量词不是一个好q的局部替代。

近image支以正交投影到该固定affine plane取barF_t，||F_t-barF_t||≤ε_alg，且每个固定ψ的barF_tψ曲线恰在同一仿射line。barF不被称新source slope：实际管、marks、ξ和tuple关系仍按原F。对同一ρ-window的实际L输出，仅替换斜率造成

    |(t-s)[(F_t-F_s)-(barF_t-barF_s)]ψ|≤Cρ ε_alg。

R16 working误差为O(τρ+δ)、τ≈Kρ²；因ε_alg≪ρ²，上式≤Cρ³，可被**实际**τρ支付。normal y按τ归一、time按ρ归一，F按τ/ρ归一时，误差成为O(ρ)，不是免费fineδ。µ≪c确保此处和之后SM容差均有真幂余量。

barF在ρ-window的amplitude及fine代表oscillation由原F的dyadicLip加2ε_alg控制；取old允许timecell尺度s≈Kρ²时，ε_alg≪ρ²≤s，故R16 coarse时间小幅抵消仍成立。不假barF自身全尺度Lip或改动原source。

## 8. All-real SM由完整源付：最终K不吞fit代价

先固定ε0足小依γ，使R16 finite scalar输入可用，并可取ε0<1/10。取ε_SM和a_B均充分小于 **µε0κγ²** 除全部固定证明常数，源η最后更小；不是只分别小于µκ和ε0κγ。对每个原ρ-window J，若有all-real matrix affine fit

    |F_t-tR_J-U_J|≤ρ^(1+ε0)

命中多于ρ^(ε_SM)(ρ/δ)个W-times，记J为bad并选一组实际fit witnesses。若|R_J|≤ρ^(ε0/3)，选中的值彼此variation≤Cρ^(1+ε0/3)。该fit集对原W∩J的比例≥cρ^(ε_SM)，因为#(W∩J)≤Cρ/δ。named19.4可直接用该原分母／anchor、σ=Cρ^(1+ε0/3)∈[ρ²,ρ]，给

    CW≥δ^{Cη_g/γ}ρ^{Cε_SM/γ-ε0κ/3}，

参数后小使矛盾。因此所有bad选中fits可认为|R_J|>ρ^(ε0/3)。其absolute error至多ρ^(1+ε0/2)|R_J|，固定常数用指数gap吸收，正好进入named20.2的relative-slope容差。

此处必须纠正原named20.2的literal范围：它写R／U∈Mat，不能把Mat的有界定义直接冒为all-real。本次另付其proof的有界多项式增长系数扩展。badfit点数给两个实际extreme times的span≥cρ^(1+ε_SM)，原F在同一allowedρ-window的振幅≤Cρ；故

    ||R_J||≤Cρ^(-ε_SM)， ||U_J||≤C(1+||R_J||)。       (7)

选集很大，span远超δ；不是一个bin里用任意大slope作弊。U只以常数差出现，在V恒等式中消失。high branch有||R_J||≥ρ^(ε0/3)≥ρ，按R16 original-tuple第7节已核geometry，对所选global fit并重取实际good-q／V endpoint与own-incidence auxiliary H，而不是对任意q假局部filled。若所选并的原time比例≥δ^ε_fit，所有这些费用写K_fit=δ^-C(η_g+ε_fit)。own-H的slab边际去掉小|R_Jψ|后可固定一个实际ψ及endpoint，保K_fit^-C个原times，且 |R_Jψ|≥K_fit^-C/γ ||R_J||。

在这个固定J和R_J上，真实输出落在原native Y的

    y1+(t-t0)²R_Jψ+O(Δ)，
    Δ=Cρ^(2+ε0/2)||R_J||， L=Cρ²||R_J||

邻域。fine方向换ρ-proxy的误差Cρ³||R_J||≤Δ，fit误差亦≤Δ。由(7)及high lower，L≤Cρ^(2-ε_SM)<1，Δ≥cρ^(2+5ε0/6)≫δ，故原tube-KT的长度／宽度／δ floor均合法；没有把||R||当常数省略。删掉|t-t0|<K_fit^-Cρ的clock只损可支付原mass。二次time映射在两侧分别单调，原δ-separation和所保times数量给原Y在该长L、宽CΔ tube内的Δ-cover lower≥K_fit^-C/γ L/Δ。tube-KT upper≤K_fit^C(L/Δ)^(1-γ)，比较得

    ρ^(-ε0γ/2)≤δ^-C(η_g+ε_fit)/γ，

与ε_fit、η_g≪µε0γ²矛盾。大R在L/Δ中抵消；这个扩展由实际geometry支付，不称原statement已经全real，也不认证其wholeproof。

若bad whole windows合计承载至少δ^(a_B)#W，所选fit并Z_fit的原W质量至少cδ^(a_B)ρ^(ε_SM)≥δ^{2a_B+ε_SM/4}。每个保留fit time所在J共享一个R_J／U_J，取ε_fit=2a_B+ε_SM/4，正满足上述扩展的global比例。无需宣Z_fit是新完整配置，也无fitconfig新allowed换格。对literal有界R/U的情形也可直接在现有W完整配置内以Ztilde=Z_fit调用named20.2；其给

    CW≥δ^{C(η_g+2a_B+ε_SM/4)}ρ^-κ，

上述全real扩展及有界statement各在所需小参数范围给矛盾。于是删去全部bad windows只损δ^(a_B)#W。余W_good仍保≥#W/2，原η_g预算只依η的固定倍，**不含**ε_SM／a_B的fixed power；这些仅在反设调用中收费，不能回灌R16最终graph的K。

每个余window由定义满足原all-real absolute SM upper ρ^(ε_SM)(ρ/δ)。近image替换误差ε_alg≪ρ^(1+2ε0)，故barF的更严格fit会转成原F在ρ^(1+ε0)内fit；SM同样传给barF。原point Φ／nativeY lower只在完整W_good层上保，之后good-q／heavy-fibre按R16原质量重新取，不给任意clipped对象新ADlower。

## 9. Common-image完整R16调用与所有原prior

选一个余SM window内实际time数≥K^-Cρ/δ的J：W_good全局量仍K^-C#Z，按原window平均可取，不能先任取q。R16原tuple审计给真实good physical q、足原time B_f、原endpoint Y0及原L-graph；原incidence-mixture删heavy方向bins得到共同H，其own差law有slabγ cap，并对该L-graph的边际费用已付，不假unused Φ_q全体slab。

按τ≈Kρ²分grain cells，先删light Y／time fibres，再用原最大fibre数归一化图权。得到共同coarse B（r=ρ-separated，exponent1 interval upper）、A_-／A_+及0≤g≤1，density≥K^-C、#A_+≤K^C#A_-。A_-的tube-KT直接查询完整原Y，物理宽度≥τρ≫δ；不是从clipped A_-免费给lower。原Φ差保重复labels与原权，不把两point的条件law独立拼接。

实际F替换barF后只增第7节已付O(r)误差。SM从第8节经R16 span／all-real slope计算传到coarse B：命中多的coarse fit先有span≥r^{b0}K^-C，故R的大小可界，time代表误差才可反推fine fit；不先假fit coefficients bounded。取finite theorem要求的较严格精度指数，ε_SM／η_g依次小可保持余量。

barF(B)每个固定used ψ的像为line，故R16有限linewise命题适用：逐ψ把输入Y沿该line分strip，保原g平均和输出／输入card比；标量13.5迫每good ψ在足同原B上affine；用own slab law及原B上的CS选两个独立差在同一time子集相交，重构all-real matrix affine fit，反SM。此完整用途仍具名依赖原Th13.5及20.2／19.4等wholeproof，没有本轮重证全部高级结论。当前近image支已实际闭合，无需额外AFF／NQ／rational或uniform二维增长。

## 10. 近kernel接口及已完成的独立出口复核

近kernel可在fixed bounded shear／horizontal rotation后写F_t≈u(t)e1ᵀ，误差ε_alg。选择coarse r≫δ+ε_alg。保原whole projected tubes至R4坐标(x1,y1,y2,t)，每原label带原质量1/N_orig，允许重复coarse projected管而不免费去重。原CW可经有界凸棱柱提升查询转为该weighted投影族的normalized-CW upper；不能由projection自动授方向分离或joint3-ADlower。

投影marked footprint的实际已核上界为N_r≤K r^(-4+κ)：原全Y-union AD(2-κ)、一水平坐标和clock各一维；ε_alg被r支付。原每heavy管m个fine-clock访问经每coarse timebin至多Cr/δ访问，给至少K^-Cr^-1个真实coarse marked cells，因而投影族平均density≥K^-C；不能只以一个点增粗冒整clock dense。

真正最终工具须是**R4 weighted normalized-CW、无方向分离、任意平均nearfull shading**的维数3基线，给marked volume≥r^(1+o(1))而与upper≤Kr^κ冲突（κ≥1+ζ）。仅引用方向分离maximal、或未经证明的weights／重复族版本不足。现已实际全文读取B10和root12，并实际读Zahl2512.09397v1本地§2 Def2.1／Th2.2(2.2)及上下文；下面是A对非自推出口的逐项独核。

固定线性商保whole clock，随后固定homothety使实际整投影轴在unit proxy内留端部margin；proxy包含原fine投影及实际mark小r-balls。若proxy⊂凸U，则原whole T⊂对应有界kernel棱柱，体积≤C|U|；此**反向containment**查询原CW，不是unit延长自动保PW的错误说法。rounding需U+B_Cr时，Johnbox最短轴≥cr使体积只付常数。原H若先heavy，其概率归一费用1/p已算进K，而非改称原全T概率。

对任意indexed probability和可重复proxies，在bounded chart用John外box、center／frame有限网和dyadic轴长，至多r^-D个固定体积可比测试Q覆盖全部convex tests；至少含一unit r-tube者u_Q=|Q|r^-3≥c。取M=floor(r^(-3+a))次有放回iid原索引；若K0≤r^-a/2，每Q期望≤C r^(a/2)u_Q，Chernoff在固定阈值L u_Q给失败≤r^(c a L)。先L≫D/a，全部tests同时通过，得到**固定**KT常数L，不需要经典Wolff常数对原K0的polynomial依赖。

sample平均shading密度的下尾由独立bounded变量／Chebyshev或Chernoff给失败o(1)，因Mλ→∞；不依原权重跨度或#index。重复proxy最多CL次由其体积≈r³的containingbox直接控制，合并后shade取并，summed marked volume至少c_a λMr³≈c_a λr^a。经典Wolff（无方向分离，绝对KT、固定L）在R4给 ||Σ1_P||_(3/2)≤C_(a,ε)r^(-1/3-ε)，Hölder遂给

    |union coarse marks|≥c_(a,ε) λ³r^(1+3a+3ε)。      (8)

原marks union仍包含于实际粗footprint，不因fake延长区域获得下界。先令3a+3ε≪ζ，再η小使upper常数K≤r^-ζ/8及λ^-3≤r^-ζ/8并满足sampling条件，(8)与upper≤Kr^κ冲突。参数r=δ^s、s<c/2固定后η最后，故原δ^Oη能成为任意小r幂。B的完整kernel出口在上述scope独核通过，没有未解决必修；不赋商ADlower或OAI4 fullvolume输入。

## 11. 反攻、闭包与extremal读出上限

R64 cross-only反例不能冒本次sameT返回的clique-law反例；反之，一个任意dense selected graph也不授本次clique。fine inverse中的δ/H放大、短clock的δ floor、κ1零saving和原Φlabel重数均是必要测试。global S不先缩ρ，避免shortclock固定ρ幂吃尽ζsaving；R64 finite删除只损o(1)S，不改变最终K的源阶。

原whole-time restriction保整层及原T；重新派出point／tube／q图必须重新付mass，平均density与逐管下界分开。R16 coarse graph不能拿actualsource为r-separated time，它的heavy quotient已有明确费用；近image也不能将δ^c误差冒fineδ。本证明没有追加smooth或goodrank假设。

若matrix33 κ>1全部出口通过，欲读sticky Kd5(1)还须核原17.2极值提取能否保当前bounded原全T/N/CW规范。literal local-AD与bounded used labels本身不控制无界unused T总数，单取一bounded chart也会放大normalizedCW。没有该归一化补证，最多给有该规范的extremal source条件推论；不能无条件宣布全Kd5(1)或ordinary5新界。其它(k,ell)的维数约束κ≤ell-1及κ≤5-k可定位κ>1仅matrix33，但这不自动解决归一化入口。

## 12. 当前完成、独审责任与停止

已独立付fine native invertible bound、原sameT平方质量、真实原heavy T*的完整GLOBAL clock raw前提、整time闭包、R64近似结构与nearconstant／common-image完整用途。新增的是从完整原source实取raw前提；既有R64分类与R16 linewise作为已审工具重调用，不登记新的rank／scalar机制或重大性。

近kernel粗化／weighted-CW基线现已由A实际全文独核B10及root12的非自推部分，第10节记录实际推导。现已fresh实际读回root12第6节的终版展开：8µ<c、ε_SM/a_B乘积级预算、all-real fit的R／U界、实际Δ／L／δ floor及KT抵消均已明写，明确区别literal有界Mat statement。该此前强制澄清已解决；不把原Mat有界定义悄改全real。A自证由root／B独立审，不把自己证明计自己的独审。

已实际全文读终版macro6和next6：均保bounded κ>1源应用、不宣literal全Kd5(1)，κ1零saving／generalMat2／commonkernel、ordinary初始化／Hausdorff仍open；没有把经典Wolff或raw分类换名新ID。当前完整主链在所列具名输入和bounded源范围内无未解决必修。正式review另获授权单独写，高级wholeproof仍具名，未经外部同行评审。停止本族阈值／采样常数优化，无major／ordinary声明，无Git／元数据预认证。
