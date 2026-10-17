# R0068：原V、native scalar KT与无AFF的大残差门槛

2026-10-18，A。实际读working_spec5／opening macro3、R67交接、STATE及固定目标，重读原WZ2609.22035v1 Def17.2–17.4、19.5、(176)／22.1、13.5声明和旧R26全局／抽样证明。只编辑本assigned稿，无Git／spawn／元数据。本稿独立施工fast-fit原质量证明及其全局用途；named高级wholeproof未在本轮新独证，未经外部同行评审。

## 1. 原命题、prepared baseline与source范围

完整d5/k4/ell3，原T joint4-AD／CW，ell Y维2−κ、native scalar tildeY维1−κ及tube-KT(1−γ)，两grain、原ξ／Φκ／slabγ全保。写f=(a;b)、tildef=(c,d)、b=c+da。固定µ∈(0,1/4)、0<ζ<1/10及任意a_*>0；κ、γ固定正，必要先降γ至min(γ,1)。不假AFF、nonquad、smooth／rational或某角非退化。

对任意指定原allowedρ∈[δ^(1/4),δ^µ]，目标存在S_ρ⊂Z_original，#S_ρ≥δ^(a_*)#Z_original，且对同一原dyadicρ-partition

    T(S_ρ)=max{δ, ρ max_J max_(t,s∈S_ρ∩J)||E(t,s)||}
             ≤ρ^(3−ζ)，
    E(t,s)=b(t)−b(s)−d(s)[a(t)−a(s)]。                         (1)

先named19.5在该ρ作整time准备，R22付δ^O(η/γ)原mass，记prepared baseline为Z⁰。其每ρ窗内f、tildef振荡≤K_srcρ，原whole T不改。后文所有minimum／全局见证并均以同一Z⁰为分母，最后才恢复Z_original；不混用两个分母。原ρ的extra coherence／union-AD在整层restriction后仍真实保留，不因新参数格改变而抹掉；V／L计数可直接在原ρ使用这些实际属性，无需合并不同ρ窗。

R16／R24已付的good-q与原V／L计数接口按实际范围使用，19.5和13.5仍具名。这里不引用整个22.5、AFF₃存在、原coefficient-weighted非二次或scalar quadratic engine代替本证明。

## 2. Fast-fit引理的精确global输入

设一个整time W⊂Z⁰有#W≥δ^u#Z⁰。每个非空原ρ窗J有固定旧actual anchor c_J、d0,J=d(c_J)及h_J=b−d0,J a；anchor可在之后删去但值固定。对所有z∈W∩J有

    ||h_J(z)−r_J z−C_J||≤C Tρ^(A−1)，
    ||r_J||≥(T/ρ²)ρ^(A/2)，
    ρ^(3−ζ)<T≤K_srcρ²， 0<A<ζ/10。                            (2)

另保原同窗raw上界ρ||E||≤T；应用时W是某minimum集合的子集，自动成立。若η、u充分小依固定A、ζ、κ、γ、µ，本引理结论是(2)不可能。它只对足量global W调用完整source，未把孤立稀窗假成新全局配置。

在W删absolute light窗，再重新good-q。若#W≥δ^u#Z⁰且#Z⁰≥δ^O(η/γ)δ^(η−1)，可删#(W∩J)<cδ^(u+O(η/γ))ρ/δ的窗，损不足W的固定比例。对所选J、q，原incidence平均给

    m=#Z_q≥K_f^(−C)ρ/δ，e≈K_f^±C m(ρ/δ)^(4−κ)，
    D=δ^(−κ)，L=ρ/δ，K_f=δ^(−C(η+u)/γ)。                       (3)

可重新作R67 point／tube／nativegrain core，或对V直接用已付weighted CS；都不赋新AD lower或CW。q的全部times来自同一个J，因此沿用同一r_J、C_J与h_J。

## 3. Rich fit的系数上界与物理单位

source原h_J在该ρ窗内振荡≤K_srcρ。由m≥K_f^(−C)ρ/δ及原time δ-separation，Z_q的physical diameter≥K_f^(−C)ρ。比较两个相隔如此远的fit点并用(2)，得到

    ||r_J||≤K_f^C，                                           (4)

因为Tρ^(A−1)≤K_srcρ^(1+A)。这不是预设bounded slope：上界由真实local clock跨度支付。若先在一个β-rich孤立fit上估系数，会出现β及绝对窗口密度的倒数，不能偷偷算K_src；global见证并的重做q使这些费用统一落K_f。

记normalized R=ρ²r_J/T，正是F=(ρ/T)(h−h_anchor)的affine slope。fast阈值||R||≥ρ^(A/2)等价(2)。真正V二次主幅是T|Rψ|=ρ²|r_Jψ|，不是T|r_Jψ|；normalized与physical斜率不能混写。

## 4. 原V自己的先验与固定rich endpoint

在新q的真实V=(p@t,p₁@s,p₂@s,T₁,T₂)上，用weighted incidence CS或新core得到

    #V≥K_f^(−C)eD²m。                                         (5)

固定初incidence(p,T₁)，选择s和T₂给upper K_f Dm，因此V初角边际由K_f^C倍原incidence mixture支配。原逐point Φ的slabγ／κ-ball upper，加heavy-used-ρ-cells修剪，产生#H≈K_f^±Cρ^(−κ)及Uniform(H)的slabγ，查询base为Cρ。这里重新支付的是本V自己的边际；不借R67 hybrid的边际，也不赋unused Φ_q slab。

code为(p₁,t,h₁,h₂)，p₁保完整point label、故s固定；h_i为原初管ρ-angle proxy。给定code，T₁在p₁的ρ包内至多K_f L^κ，决定p@t；T₂在p的ρ包内至多K_f L^κ，决定p₂@s。fibre≤K_f^C L^(2κ)。除(5)得到

    0≤g_V≤1，mean_(Uniform(P_endpoint)×Uniform(Z_q)×Uniform(H)²)
                 g_V≥K_f^(−C)。                              (6)

P_endpoint可含所有core／原q点，card≤e，分母D²/L^(2κ)=ρ^(−2κ)完全抵消。原point、clock、角的相关性留g，未独立化真实V。

对π=(差)_*Uniform(H)²，删|r_Jψ|<q_a||r_J||的角对，q_a可取ρ^(A/8)或足够小的K_f固定幂。均有q_a≥Cρ，且K_f q_a^γ小于(6)质量：η+u相对µAγ足够小即可。g≤1支付删除后，再选一个真实endpoint p₁及good proxy pair，使原fine t中≥K_f^(−C)比例保留。不能先固定endpoint再给其角law免费slab。留下的每个positive code均有一组实际V见证，fine角pair可随code不同，后面显式付proxy误差。

## 5. 二次轨迹：先换原E的角proxy再代fit

设固定endpoint p₁@s的native label为η₁，ψ为上一节固定的ρ-proxy差。对每个实际V原(176)给

    η(p₂)−η₁=(s−t)E(t,s)ψ_fine+O(δ)。

优先利用原raw bound ρ||E||≤T，把fine ψ换成ψ：误差≤Cρ·(T/ρ)·ρ=CTρ。再代fit和原Lip cross项，而不先对r_J作角替换，于是

    η(p₂)−η₁=−(t−s)² r_Jψ+O(Δ)，
    Δ=C K_f^C[Tρ^A+ρ³+δ]≥δ。                                (7)

Tρ≤Tρ^A因A<1。若次序相反，需另付ρ³||r_J||=T||R||ρ；它由(4)可吸收，但不能漏写后声任意real slope皆常数费。上述先换raw E避免该多余项。

主幅B=ρ²|r_Jψ|≥K_f^(−C)Tρ^(A/2)，且由(4)有B≤K_f^Cρ²。A<ζ/10、T>ρ^(3−ζ)、δ≤ρ⁴及小loss给

    δ≤Δ≪B≪ρ， Δ/B≤ρ^(cA)，                                  (8)

可保c=1/3（q_a=ρ^(A/8)时留固定余量，再取loss小）。例如ρ³/(Tρ^(A/2)q_a)≤ρ^(ζ−A/2−A/8)，Tρ^A主项给ρ^(A/2−A/8)，均有正幂。物理tube-KT查询的∆、B都≥原fine δ；不是在normalized假base查询。

## 6. 真time覆盖、抛物线vertex与native scalar KT

选中的原fine times有≥K_f^(−C)m个，m≥K_f^(−C)ρ/δ。删|t−s|<g₀ρ，其中g₀为足小K_f固定幂；原δ-separation／ν interval upper使损失不足一半。再保s一侧，平方函数单调，t=s或顶点邻域不再伪造丰富image。

在该侧，quadratic Q(t)=η₁−(t−s)²r_Jψ的physical derivative至少K_f^(−C)B/ρ。任意∆-interval的time preimage长度≤K_f^C∆ρ/B，所以原δ-separated times数≤K_f^C[1+∆ρ/(Bδ)]。∆≥δ、B≪ρ使常数项可吸收；选中time总数≥K_f^(−C)ρ/δ。因此实际Y-label的∆-cover至少

    N_Δ(tildeY_s∩I_{CB})≥K_f^(−C)B/Δ。                        (9)

原approximation(7)只把cover常数厚化，s仍固定，全部η(p₂)属于原native scalar tildeY_s。该集合原tube-KT(1−γ)给

    N_Δ(tildeY_s∩I_{CB})≤K_f^C(B/Δ)^(1−γ)。                   (10)

(9)–(10)迫(B/∆)^γ≤K_f^C，违(8)及η+u≪µAγ。没有使用ell二维Y的不存在的line-KT，没有给裁切native Y新AD lower，没有假每条原管访问每个fit时间。fast-fit引理完整得证，所有原mass损失计在K_f。

## 7. Minimum链与所有原窗口：不依赖旧NQ下界

在prepared Z⁰上对同一原partition定义T(S)如(1)。取η₀≪…≪η_M且η_M及prep loss之和<a_*，令T_j为#S≥δ^(η_j)#Z⁰的真正minimum，S_j为有限集minimizer。若任何T_j≤ρ^(3−ζ)，已得到最终目标。反设全j都large；这本身给所需lower，不再用AFF／NQ去排tiny端。

原Lip给T₀≤K_srcρ²。取M>100/A，若每次T_(j+1)<ρ^(A/8)T_j，则T_M≤K_srcρ^(2+MA/8)<ρ^(3−ζ)，矛盾。故有j满足

    T_(j+1)≥ρ^(A/8)T_j。                                     (11)

ρ、原Z⁰分母及原f均固定；没有按q或ψ重定义minimum。δ-floor在large范围无害，但在候选并内仍保留。

## 8. Fast／slow rich fits的global并与删窗

删S_j的relative light窗m_J<δ^(2η_j)#(Z⁰∩J)，总损≤δ^(2η_j)#Z⁰。取各余窗旧actual anchor c_J∈S_j∩J，d0=d(c_J)，定义

    F_J((z−c_J)/ρ)=(ρ/T_j)[h_J(z)−h_J(c_J)]
                         =(ρ/T_j)E(z,c_J)， ||F_J||≤1。         (12)

称J bad若有某row affine Rt+C在precisionρ^A捕获≥β_j m_J，β_j=ρ^(b_j)。选一个实际见证W_J（可取最大card fit，有限可能subsets保证存在），按||R||≥ρ^(A/2)或<该值分fast／slow。anchor虽可能不在见证中，始终使用同一固定值，后面不重新选F。

若fast见证并有≥δ^(η_(j+1))#Z⁰，§§2–6适用：新的source loss是η_(j+1)，重新q后所选J仍用自己的same fit，故矛盾。否则fastbad窗总mass<δ^(η_(j+1))β_j^(−1)#Z⁰。这里没有说每个孤立fastfit都可调global引理。

slow见证上diam F_J≤Cρ^(A/2)，原E=Δh−(d_s−d0)Δa及Lip给

    T(W_J)≤C T_jρ^(A/2)+K_srcρ³≤T_jρ^(A/3)。                  (13)

δ也小于右侧。若slow见证并达下一global门槛，该并在原固定各J内(13)均成立，且T不查跨窗pairs；即是下一minimum的合法candidate，违(11)。于是slowbad窗mass同样<δ^(η_(j+1))β_j^(−1)#Z⁰。不同窗拟合常数可不同，没有免费global polynomial。

删全部bad窗口只损≤2δ^(η_(j+1))β_j^(−1)#Z⁰；只要η_j≪b_j≪η_(j+1)，它小于S_j的o(1)比例。再删absolute light窗，重新good-q／native L图。每保留J对**全部real row affine**在precisionρ^A有fit mass<β_j，传到新q law后为K_graphβ_j。K_graph只含η_j及source loss，不含β_j；fast引理才使用更大的η_(j+1)。这是参数顺序的关键区别。

## 9. 取消AFF的L图与同步空间归一

在余whole-time数据上，raw T_j upper仍对全部同J ordered pairs成立。取τ=C T_j或允许取整后的τ≈_K T_j，22.1只需upper(179)，不要求新q内sup达到T_j。原L／used-angle构造重做，native scalar patch长τ。直接用

    E(t,s)=h_J(t)−h_J(s)−(d_s−d0)[a_t−a_s]，
    ||(d_s−d0)(a_t−a_s)||≤K_srcρ²，                            (14)

不用a=affine＋error。乘timeρ后丢cross只多Kρ³，原L误差Kτρ+δ和角proxy误差KT_jρ均明列。

为保持同一个F_J，native原空间先除T_j（而非除τ却忘乘T_j/τ）；patch长度τ/T_j≤K。再把空间和F_J同除一个L₀≤K使bounded。这样图支持为x+(s−t)(F_J(t)−F_J(s))ψ，clock已除ρ，统一误差可取

    w=K_graph^C(ρ+ρ³/T_j)， ρ²≤w≤ρ^(ζ/2)。                    (15)

若先除τ，则须改F为(T_j/τ)F_J且同步改nonfit precision；二种做法等价但不能混用。physical fine base δ/T_j≤ρ^(1+ζ)被w覆盖，fine time δ/ρ≤ρ³也远小于w。此图不需要R67双端joint matching的contact-scale推广，原native单L足够，未把W和L两个不同g假交。

## 10. Same-prior标量化与13.5的实际输入

对同F_J及原fine ν、H差lawπ，用R26已独证三点annihilator式：vector affine precision h₀=K_graph^(−C)ρ^A的mass upper a=K_graphβ_j，scalar precisionσ₀=ρ^(2A)、richness b_s=ρ^v，则坏角概率≤C b_s^(−3)[a+K_graph^C max(Cρ,3σ₀/h₀)^γ]。先选v≪min(b_j,γA)，再取graph loss小，概率小于本g均值。以g≤1支付坏角后选一个good proxy ψ，同时保原fine graph与所有scalar affine nonfit。不是vector nonfit给每个投影。

R26空间heavy-occupancy和same-F time sampler的所需输入，逐项只有：此fine graph、full native Y的AD packing、原ν intervalcap、bounded F及所有affine nonfit。故在这里也可用，不再查AFF／NQ：full Y lower＋cell capacity给input carrier lower，upper给output；独立time代表及uniform coefficient net／Hoeffding同时保g和全affine nonfit，clockrounding保同一原F值。

设named13.5的允许precision指数为e_ABC>0，取A=ζ e_ABC/1000。其scalar fine precisionσ₀须满足4L₀ w^(e_ABC)≤σ₀，(15)给出ζ e_ABC/2≫2A的固定余量。engine用α=1−min(κ/2,1/2)、β_time=1、C={1}、γ_C=0；regularity阈值不依nonfit mass指数，graph阈值可依v，分开后取graph loss。结果#A≥w^(−α)与原#A≤K_graph w^(−1+κ)矛盾。符号需要时用−F，不用非法负C。

上述finite操作的完整证明引用R26已经逐步支付的相同输入版本；原13.5高级wholeproof仍具名。原22.5整体未被用作新模型的捷径。

## 11. 无循环参数和最终全局量词

先固定κ、γ、µ、ζ、a_*，依13.5先取e_ABC，再定A、M。terminal η_M取小于a_*/10、fast KT的µAγ阈值及regularity阈值。由后向前：已知η_(j+1)，取b_j=η_(j+1)/100、v_j≪min(b_j,γA)，固定scalar非fit／13.5 graph阈值，再取η_j充分小于这些阈值和µ b_j。原η最后小，δ最后。fastbranch使用η_(j+1)但只需fast KT固定阈值；nonfit图使用η_j，可压过其后已知b_j、v_j。没有让β反向增大同一graph source loss。

ρ=δ^s、µ≤s≤1/4给δ^(η_(j+1))β_j^(−1)≤δ^[η_(j+1)−b_j/4]，确为δ^η_j的o(1)。absolute窗删除、常比例与19.5准备可由η_M＋prep loss<a_*吸收。nonfit inverse矛盾排掉“所有T_j都large”的反设，所以某原minimizer S_j即满足(1)。

指定ρ从未改变；本证明在整个原allowed区间的估计统一，故是**每个指定ρ可选自己的S_ρ**，不是仅某个空间q或某窗有小残差，也不保证所有ρ共享同一个S。没有合并不同窗口的fit常数，没有从used g升级raw小：最后T(S_j)小来自原global minimum本身。

## 12. 闭包、与旧证明的差别和当前状态

所有删选均为原整time或原tuple／角质量删除。保留层的E／Y／X／Φ／ξ及原whole T不改；平均shading重计，不保证原每根管逐管density。若用core，其local逐active tube visits下界由有限peeling获得，非原平均免费提升。native KT在原superset查询，无裁切AD lower，CW／AD不用core新分母。δ-floor、顶点、粗角proxy及fit系数界已分别支付。

与R26不同，fastfit被原V＋native scalar KT排除，不再用coefficient-weighted NQ；反设目标失败本身供应minimum链下端，不再用AFF给tiny lower；drop-cross直接用Lip，不写a的affine fit。因此得到的是旧完整mixed43责任的一项无AFF／NQ大残差upper gate，不是给原source另加proper regularity。R66 tiny lower与此upper方向不同，二者不能免费求共同全尺度时间集；whole AFF／contact内coupled项／完整mixed及ordinary高维仍未解。

已实际独读root14初稿；其proxy次序与归一化建议已反馈parent，待最终root／B／macro／next实际全文审后出获授权formal。只编辑本稿，不预认证元数据、同步或新颖性／major；无新PDF／ID，未经外部同行评审，Goal active。
