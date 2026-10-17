# R0068：不预设whole AFF的原mixed43大残差门槛

2026-10-18，root；先写spec5/macro3再施工。目标仍ordinary n≥5/general。本稿使用原V/native scalar KT代替旧large分支的AFF/NQ准备，给出列明具名输入下的全source近contact upper gate；有限计数、具名高级源输入及最终目标分开。两代理逐式全文内部审查通过，未经外部同行评审。

## 1. 原命题、量词与非等价范围

完整WZ2609.22035v1 Def17.2–17.4，d5/k4/ell3：原T joint4-AD、CW≤δ^-η，Z与两grain/ξ/Φκ、slabγ及native scalar Y的tube-KT1−γ保留。0<κ≤1、0<γ≤1固定。记f=(a;b)、tildef=(c,d)，a,b,c row2、d scalar，b=c+da。

固定µ∈(0,1/4)、0<ζ<1/10及任意目标time loss a_*>0。η在这些参数和下面具名定理阈值后充分小，δ最后小。对**任意指定原allowed**ρ∈[δ^(1/4),δ^µ]，欲证存在原整time S⊂Z、#S≥δ^(a_*)#Z，满足同一原半开dyadicρ-partition J上的

    T(S):=max(δ,ρ max_J max_(t,s∈S∩J)||E(t,s)||)
          ≤ρ^(3−ζ),
    E(t,s)=b_t−b_s−d_s(a_t−a_s).                (1)

空/单点窗max=0，ordered pairs不替换成used graph edges。本结论不证明whole-matrix AFF3、contact-scale联合图或完整mixed；R66仅给tiny lower，不给(1)；R26 large证明需AFF/NQ，本稿必须实际取消那些依赖。无新数学ID/major/新颖性认证。

## 2. 具名准备、原质量和K的两种用法

先具名19.5作整time细化、用R22闭包，付δ^O(η/γ)原mass，使同ρ窗f、tildef variation≤K_srcρ。随后每次整time限制都重新good-q，不沿用删前图。保留原所有allowed-scale upper/coherence；不授裁切AD lower或新CW分母。源good-q和19.5高级wholeproof不在本轮全量独证。

若当前整time集mass≥δ^u原Z，删掉绝对light窗口后仍保其常比例质量；余good-q有m=#Zq≥K(u)^-1ρ/δ、e≈K(u)^±1mL^(4−κ)、D=δ^-κ、L=ρ/δ，point/tube/nativegrain有限core可照R67实际peeling，保point度D、tube访问m、grain点L³至K(u)幂。K(u)=δ^-C(η+u)/γ，C可依固定阈值但有限。

**预算区别**：fastfit反证限制到见证并时允许K_fast=K(η_(j+1))；nonfit分支只用S_j/整窗删除重构，所以K_graph=K(η_j)，绝不能把β_j的loss回灌graph source参数。平均shading按原whole T分母重计，core逐active tube visits lower来自已付peeling，不声称所有原tube逐管density保留。

## 3. 一个全source fast-fit排除引理

设某原整time W有#W≥δ^u#Z，每个非空ρ-window J有固定actual旧anchor c_J、d0,J=d(c_J)，h_J=b−d0,J a，并有row r_J、C_J使对所有z∈W∩J

    |h_J(z)−r_J z−C_J|≤C Tρ^(A−1),
    |r_J|≥(T/ρ²)ρ^(A/2),
    ρ^(3−ζ)<T≤K_srcρ²,   0<A<ζ/10,
    ρ max_(t,s∈W∩J)||E(t,s)||≤T.               (2)

actual anchor不必保留在W，值固定来自原数据，故|d_s−d0,J|≤K_srcρ。若u及η足够小依A,ζ,κ,γ,µ，则(2)不可能。此引理需W的**global**原mass，未声称孤立小窗可免费当新全局配置。

在W上合法删整层及absolute light窗，重新good-q/core；所有q times处于同J且满足同一fit。m≥K_fast^-1ρ/δ使其time span≥K_fast^-Cρ。h_J在窗内variation≤K_srcρ，fit error≤K_srcρ^(1+A)，故该q的|r_J|≤K_fast^C。fit斜率没有预设有界，系由真实clock span取得。

## 4. 原V码、自己的角先验与rich endpoint

在上述core中计V=(p@t,p1@ s,p2@ s,T1,T2)，两初arms共享p,s且都是真core管访问。按每point每tube最低度及CS，

    #V≥K_fast^-C eD²m.                          (3)

固定初incidence(p,T1)时，s及另一初管最多K_fast Dm，除(3)使V初incidence边际被K_fast^C Uniform(I_core)支配。后者从原point Φ upper/slab、度数upper和core I lower保slab与ρ-ball upper。照R67自己的边际删light usedρ-angle bins，得共同carrier H：#H≈K_fast^±Cρ^-κ，Uniform(H)对宽≥Cρ slab upper K_fast^C w^γ，初差lawπ保原有序pair重数。未赋unused Φ_q slab。

码为(p1,t,h1,h2)，p1保完整原point label（决定s），h_i∈H。固定p1后T1在其初ρ-bin内至多K_fast L^κ，决定p@t；再T2在p的ρ-bin内至多K_fast L^κ，决定p2@s。故fibre≤K_fast^C L^(2κ)。以真实fibre除这个upper，(3)给

    0≤g_V≤1，mean_(Uniform(P_core)×ν×Uniform(H)^2) g_V
                  ≥K_fast^-C,  ν=Uniform(Zq). (4)

这里#P_core≤e，D²/L^(2κ)=ρ^-2κ，故full reference分母全部抵消。用原slab删|r_J·ψ|<K_fast^-C|r_J|的角对，只损小于(4)一半质量，再固定真正good proxy pair及p1，留下≥K_fast^-C比例的**原fine** t。t=s或靠vertex的短区间可用ν intervalcap删掉，再留一侧；无条件time/angle独立性假设。

## 5. V恒等式的误差、quadratic image和native KT

对(4)每原V，原(176)给η(p2)−η(p1)=(s−t)E(t,s)ψ_fine+O(δ)。(2)保全部ordered原bound ρ||E||≤T；先在这份原式换fine角为ρ-proxy只错O(Tρ)。由(2)及原Lip，

    (s−t)E(t,s)=(s−t)(t−s)r_J
                        +O(K_fast[Tρ^A+ρ³]).  (5)

先换proxy的误差Tρ被Tρ^A吸收（A<1）。若先fit再换，也需另记ρ³|r_J|，但可由第3节span估计支付；本证采用前一顺序。所有选中的原t满足（按符号可反射）

    η1−(t−s)²(r_J·ψ)∈N_Δ tildeY_s,
    Δ=C K_fast^C[Tρ^A+ρ³+δ].                   (6)

记B=ρ²|r_J·ψ|。good角及(2)给B≥K_fast^-C Tρ^(A/2)，且B≤K_fast^Cρ²。δ≤ρ⁴、A<ζ/10及η,u最后小给

    δ≤Δ≪B≤1，  Δ/B≤ρ^(A/3).                  (7)

在距vertex≥K_fast^-Cρ的一侧，quadratic map导数≥K_fast^-C B/ρ。任何长度Δ的image interval，其原ν preimage mass≤K_fast^C(Δ/B+δ/ρ)。B≤K_fast^Cρ²且Δ≥δ使δ/ρ可被Δ/B吸收。选中times原ν质量≥K_fast^-C，故

    N_Δ(image)≥K_fast^-C B/Δ.                  (8)

全部image在长度CB区间内，(6)把它送进原native scalar tildeY_s的CΔ邻域。原tube-KT给N_Δ≤K_fast^C(B/Δ)^(1−γ)。与(8)合得(B/Δ)^γ≤K_fast^C，违(7)及η,u≪µAγ。未用ell Y的不存在的line-KT，未给裁切Y新lower，也未需whole a affine。引理(2)得证。

## 6. 原最小值链：不再依NQ提供tiny lower

在19.5准备后的同一原Z上，取0<η0≪η1≪…≪ηM≪a_*，定义T_j为所有#S≥δ^(ηj)#Z的原S上(1)之minimum，S_j取真实minimizer。有限集保证存在。若某T_j≤ρ^(3−ζ)，即得目标；以下反设全部大于该值。原Lip只给T_0≤K_srcρ²，仍足够。

取A稍后由13.5阈值先定、M>100/A。若每个T_(j+1)<ρ^(A/8)T_j，则T_M≤K_srcρ^(2+MA/8)<ρ^(3−ζ)，矛盾。因此某j满足

    T_(j+1)≥ρ^(A/8)T_j>ρ^(3−ζ+A/8).           (9)

不同于R26，不需要用AFF/NQ排tiny端来制造(9)；反设整个候选失败本身已给lower。固定此j，β_j=ρ^b_j、b_j=η_(j+1)/100。令ηM先小于Aγ和a_*阈值，再从后向前选ηj，使K_graph费用远小于b_j及所有三点/13.5阈值；详见第12节。

## 7. 所有rich affine fits的全局见证二择

先删locally-light窗|S_j∩J|<δ^(2ηj)|Z∩J|，总损≤δ^(2ηj)#Z。每余J取c_J∈S_j∩J，h_J=b−d(c_J)a，并对t=(z−c_J)/ρ定义

    F_J(t)=(ρ/T_j)[h_J(z)−h_J(c_J)]
                         =(ρ/T_j)E(z,c_J).     (10)

故|F_J|≤1。称J bad若某row affine Rt+C以precisionρ^A捕获≥β_j|S_j∩J|个原times，选一真见证W_J。按|R|≥ρ^(A/2)与否分fast/slow。

若fast见证并W_fast有≥δ^(η_(j+1))#Z原mass，其physical斜率r=T_jR/ρ²满足(2)，第3–5节直接全source矛盾。因此其总mass不足该值，fastbad窗总mass<δ^(η_(j+1))β_j^-1#Z。

对slow见证，原E=Δh−(d_s−d0)Δa给同一W_J中

    ρ|E(t,s)|≤C T_jρ^(A/2)+K_srcρ³
                    ≤T_jρ^(A/3),             (11)

δ也小于右侧。若slow见证并有≥δ^(η_(j+1))#Z，它是下一minimum的合法candidate；(11)与(9)矛盾。不同窗可用不同常数/斜率，T只查同J pairs，所以并没有跨窗fit误差。故slowbad窗总mass同样<δ^(η_(j+1))β_j^-1#Z。

删bad全窗后保至少S_j一半原time，余J对全部row affine fit都有mass<β_j。再去absolute light窗，重做good-q、L图；其ν=Uniform(Zq)下nonfit bound为K_graphβ_j，不能仍写β_j。源K_graph不含β删选loss，因没有限制到W_fast或W_slow。

## 8. 无AFF的native L图及诚实mesh

在上述合法整time数据上，选角前对同q全部ordered pairs仍有ρ||E||≤T_j。取τ≈K_graph T_j（允许格及固定倍计K），ρ^(3−ζ)/K≤τ≤Kρ²≤ρ。原22.1只要upper，不需所选q达到global supremum。原L计数及used角incidence图按R24/R26原表重新构造。

这里明确取消旧AFF用法：不写a=r t+error，而直接用

    E(t,s)=h_J(t)−h_J(s)−(d_s−d0)[a_t−a_s],
    |(d_s−d0)(a_t−a_s)|≤K_srcρ².                (12)

原L scalar位移**除T_j**、clock除ρ，(12)给位于K_graph有界盒的correlated fine graph，mean≥K_graph^-C，支持

    x+(s−t)[F_J(t)−F_J(s)]·ψ
                         ∈N_(Cw0) A_out,
    w0=C K_graph^C(ρ+ρ³/T_j).                   (13)

此处t,s已归一化，空间patch长τ/T_j≤K_graph^C。第10节把空间和F·ψ同步除1≤L0≤K_graph^C至unitbounded，最终mesh w=w0/L0仍满足ρ²≤w≤ρ^(ζ/2)；δ/T_j floor≤ρ^(1+ζ)已吸收。若先除τ，主项必有T_j/τ系数，不能漏；本稿始终先除T_j。proxy初角误差Oρ以原ρ||E||≤T_j支付，无AFF。fine原ν和角pair law均保留。大τ是在此指T_j>ρ^(3−ζ)，不是把window内τ改成投影sup。

## 9. 同一个原角prior上的三点标量化

第7节原ν的全部row affine fit precision h=K_graph^-Cρ^A处mass≤a=K_graphβ_j。原π slab query floor Cρ。R26独立三点annihilator引理给：若某scalar affine precisionσ的fit mass≥b_s，则坏角概率

    ≤C b_s^-3[a+K_graph^C max(Cρ,3σ/h)^γ].      (14)

三个distinct原times质量及annihilator归一化系数≤1，无最小gap逆费；π与g可任意相关，以g≤1删坏角。取σ=ρ^(2A)、b_s=ρ^v，0<v≪min(b_j,γA)，K_graph最后小。合法较宽slab查询≥Cρ，(14)小于graphmean/4。故有同一个good proxy ψ，原fine图conditional mean≥K_graph^-C，并对全部scalar affine p有

    ν{|F_J·ψ−p|≤σ}<ρ^v.                        (15)

这不是vector nonfit给每个投影，也没有把proxy slice冒fixed exactfine-angle slice。

## 10. 空间粗化、细time抽样及named13.5

使用R26第3节的已证计数/抽样操作，核其所需输入仅是(13)、(15)、原native full-Y AD packing、原ν intervalcap及δ/T_j floor（与旧δ/τ只差K），完全不查AFF/NQ。删light spatial occupancy后，uniform A_minus/A_plus满足#A_minus≈K_graph^±C w^(-1+κ)、output/input ratio≤K_graph^C，graphmean≥K_graph^-C；这些lower来自原fine质量和cell capacity，不是给裁切set授AD lower。

在w-time cells独立选同一个原F值的representative：先删light time cells，prepared mixture与原ν只差K_graph幂。若coarse有q=w^(v/10)比例的w^e affine fit，time cap与bounded F使系数≤K_graph/q，故其原time误差≤w^e+K_graph w/q≤2w^e。统一系数net及Hoeffding，坏概率超多项式小于保graphmean的概率；同一次抽样同时保graph和所有affine nonfit。需要的precision是

    4L0 w^e≤σ.                                (16)

先固定named13.5对α=1−min(κ/2,1/2)、βtime=1、C={1}允许的0<e<1/4；取A=ζe/1000，(13)即支付(16)。time-rounding只改clock、保持原F值，由bounded F使位移再错O(w)，无F全局Euclidean Lip假设。

分别把K_graph regularity loss和graphmean/output loss取小于13.5两个独立阈值（graph阈值可依v）。若translation符号与13.5相反，取−F而非非法负C。该具名定理推出#A_minus≥w^-α，与#A_minus≤K_graph w^(-1+κ)固定正gap矛盾。高级13.5全部证明未在本轮重新独证。

## 11. 原upper gate及实际用途

因此反设所有T_j>ρ^(3−ζ)不成立，某真实整time S_j满足(1)。选择ηM和19.5源loss之和<a_*，即#S_j≥δ^(a_*)#Z_original。指定ρ从未改变，仅相邻allowed取整费用计K；不能由此声所有ρ共享同一个S。每ρ可有自己的S，原量词明确。

这给完整mixed43未经AFF/NQ的原大残差upper门槛。可在该S上用R66必要lower进一步定位接近contact的未解区间，但不能令不同ρ或不同S免费求交。wholeAFF3、contact内coupled项、middle完整排除及ordinary新维数界均未证。原joint R67接口仍保留，其细分辨率尚不因(1)自动解决。

## 12. 全部参数的无循环顺序

固定κ,γ,µ,ζ,a_*。先由13.5固定e，定A=ζe/1000、M>100/A。ηM先小于a_*/10，并使fast分支所有已固定有限次数都满足K_fast^C<ρ^(-Aγ/1000)。若字面K_fast=δ^(-C(η+ηM)/γ)，可取η+ηM<c µAγ²/C，常数可继续依固定γ；不把它误读为uniform γ的一次幂条件。从后向前，对每j已知η_(j+1)后取b_j=η_(j+1)/100、v_j≪min(b_j,γA)，固定本j scalar非fit及13.5的graph阈值，再取η_j充分小于这些阈值及µ b_j。

各j fastbranch允许η_(j+1)损失，全部已由terminalηM小控制；nonfitbranch源loss仅η_j，从而v_j虽小仍能压K_graph。β_j=ρ^b_j、µ≤logρ/logδ≤1/4确保δ^(η_(j+1))β_j^-1≪δ^ηj，light窗和常比例删除可付。最后原η小于最小η0及准备/rounding全部阈值，δ最后。没有先用graphloss选择β，再让β反向扩大同一graphloss。

## 13. 反攻、restriction与旧等价筛查

孤立fastfit不免费globalize；本稿只对其见证并达到原mass阈值时调完整source。原V端点p1保完整label，故无需给标量ηslice重新AD或假其ξ恒定。π来自本V或本L自己的边际；两个图无需共同独立prior，更未在同一world取交。time-rich fit系数经真实span约束，vertex及δfloor单列。parallel-native局部守恒坏CW仍非完整反例。

本gate不从R66 tiny lower推出，也不从R26全称结论直接重调，因为旧前提AFF/NQ没有来源；新增实际步骤是原V/nativeKT在global fastfit见证并上的应用。它仍是旧mixed43未付责任的部分源准备，不用新名称或ID登记重大结果。停止fastfit阈值/ρ/τ常数迭代；下一须面对完整contact/middle原耦合，不用本结论自动宣wholeAFF。

## 14. 审查和认证状态

A12/B10独立施工及互审，两formal各6节fresh实际全文核root14/对方稿/spec5/macro6/next6，无剩余强制数学修复项；root已实际读两formal并集成。修正包括raw upper、先原E换proxy、native exact T_j单位及fixed-γ预算。具名源供应/13.5等高级wholeproof未新独证；无新PDF、frontier/priority或外部同行评审认证。结论限(1)量词，普通高维/major未达，Goal active。
