# R0067：共同原trunk、hybrid质量与native输出纤维

2026-10-18，A。实际读GOAL／STATE／ROADMAP／registry78、R66交接、R67先写spec5／macro3；重读原WZ2609.22035v1 Def17.2–17.4、§19.1及§22.1，另对照R16原计数、R24 mixed43、R27 observed、R28同base box。只编辑本assigned文件，无Git／spawn／元数据修改。下面自证原有限core和共享前两条管的hybrid计数，并实际核其AFF用途的恢复费用；§§8–13保初步粗恢复的失败账本，§§14–18为随后两端匹配的自然尺度修补，不能把旧初检当当前最终否定。没有证明AFF₃、完整mixed43或ordinary新界，未经外部同行评审。

## 1. 实际源位置和本轮不能预设的输入

原§19.1（text4033–4122，PDF76–78）定义W：同p、同两根初管到s层的p_i，分别再沿末管到同u层，末方向ρ-close；(151)给(x,ξ)两块真实位移。原§22.1（4923–5072，PDF93–96）才是一般k-planar／ell-linear的native V/J/L，不能只把§20.1的k=ell证明改字母当完整mixed接口。其(174)为b=c+da，(176)为native scalar残差，(179)是固定τ后的raw norm假设，(180)另使用§19.3的tilde斜率Lip。

本轮d5/k4/ell3，f=(a;b)为2×2，tildef=(c,d)为1×3，a、b、c为row2。ell横向Y为2−κ维，native横向tildeY为1−κ维，两个原filled水平维数为2和3，原Φκ／slabγ、ξ coherence、T joint4-AD／CW均保留。不能给ell Y免费line-KT，亦不能把ξ₂−dξ₁当整native grain上的常数。τ在角选择前固定，并以

    E(t,s)=b(t)−b(s)−d(s)[a(t)−a(s)]
    ρ max_(同q times)||E(t,s)||≤cτ， δ≤τ≤ρ                         (1)

控制全部有关初始角；这不是只对将来保留的ψ重新定义τ。计数不需要AFF／nonquad或额外smooth。R66的tiny raw门槛不把used edges升级成(1)，本稿保留(1)这个原τ选择条件。

## 2. good-q原数据：只用原upper和真实总质量

固定合法good-q及其原时间集合Z_q。记

    m=#Z_q，e=#E_q，D=δ^(−κ)，L=ρ/δ，N=L³。

K=δ^(−Cη)，固定γ或此前固定参数的费用可入C；任何固定ρ幂都不冒K。原每个p、每个fine Φ-bin只取一根实际见证管，固定倍碰撞入K。已有good-q平均接口给

    K^(−1)m L^(4−κ)≤e≤K m L^(4−κ)，
    I=Σ_p deg(p)≈K^±1 eD，d_max:=max deg(p)≤KD，
    #T_q≤Kρ^(−κ)L⁴，#G_q≤K m L^(1−κ)。                           (2)

G_q是原native grain标签(s,tilde y)，每个原点归属其实际标签。后一个upper只需固定s时bounded tildef：q中的tilde y落长度Cρ区间，完整tildeY_s的fine AD upper给其δ-cover≤K L^(1−κ)。若原标签未先δ-separated，同一δ-bin的标签数仍至多K：每个完整native grain原有K^(−1)δ^(−3)个点，而这些标签的全grain都在一个厚Cδ、水平bounded的区域，原E_s的δ-separation总容量≤Cδ^(−3)。此处使用完整原grain作重数upper，不合并标签、也不为q裁切grain赋AD lower。

一根原tube在一个固定时间切片只含O(1)个原δ-separated关联点。q内所有tube的ρ-direction bins至多Kρ^(−κ)，来自原f本尺度Lip、Φ_q cover与ξ_q coherence。任意给定p的方向τ-bin最多K(τ/δ)^κ根所选管；这些都是原upper，不是给选后管族重新正则化。

## 3. 三类有限peeling：同时最低度而不换原分母

考虑原0/1 point–tube关联和每点唯一的native grain归属。令e、T_q、G_q、I均指删除前对象。阈值取

    d_*=I/(100e)， b_*=I/(100#T_q)，
    n_*=I/(100#G_q d_max)。                                      (3)

反复删除：当前tube-degree<d_*的point及其边；当前point-degree<b_*的tube及其边；当前点数<n_*的native grain及其当前点／边。finite过程终止，不需要随机或平稳假设。三类删除的边数分别至多ed_*、#T_q b_*、#G_q n_*d_max：每个原vertex至多删一次，后一类只按其当时剩余点数收费，重叠边不重复要求等式。因此总损失≤3I/100。

余core原边I_c≥97I/100。每个余point有至少d_*个余tube，每个余tube有至少b_*个余point，每个余grain有至少n_*个余point；由(2)

    d_*≥K^(−C)D，b_*≥K^(−C)m，n_*≥K^(−C)N，
    e_c≥I_c/d_max≥K^(−C)e。                                    (4)

所有余对象都是真原labels、原边、原q内点。core不是新的Def17配置，角／grain／tube的AD lower均未继承。原whole T的AD／CW仍存在，但不给以core为新分母的CW常数；后面只用其原upper和(4)实际最低度。若初数据只有平均shading，(4)是在这个core上新付的local逐管marked-degree，不等于原每根管全clock的density不变。

## 4. 共享初arm与native τ簇的真实几何

固定余p于t层。初arm为α=(p,T,p_s)，其中p_s在s层，T在p、p_s处均是余原关联。不同s／T／p_s全保，允许tube–slice的O(1)多重性。写p的前两方向坐标为φ(T)，同一p的实际差ψ=φ(T₂)−φ(T₁)不在两种续接间更换。

native投影label记η_s(x₁,x₂,w₁,w₂)=w₂−c(s)x−d(s)w₁。原straightline和b=c+da直接给

    η_s(p_{s,2})−η_s(p_{s,1})=(s−t)E(t,s)ψ+O(δ)。                (5)

因(1)，固定p、s的所有可能p_s的native labels落同一Cτ区间；在同一native grain内跳不改该label。故再按native前三个水平坐标的cτ-box分箱时，所有候选jump点位于一个Cτ物理ball。bounded tildef足够，**这一步不需跨time tilde-Lip**。

在这个ball上用原coherence，所有余末管的cτ-direction bins至多Kτ^(−κ)。若τ不是allowed格，用上邻allowed格再细分回τ，只付δ^(−Oη)；不把τ改大，也不要求两个指定点的角集有大交。q边界不生成新点：jump只选core内已有原点，(4)已给每grain至少n_*个此类选择；native τ-bins总数≤C(ρ/τ)³。

## 5. Tensor Gram：真正共享前两条管的hybrid计数

对同一个初arm α，记录非负整数向量X_α和Y_α。

- X_α(u,c_W)：从p_s选余T^W到余w∈E_u，末管方向属于cρ-bin c_W的实际路径数。
- Y_α(v,h_τ,c_L)：从p_s在其余native grain跳到余tilde p_s，再选余T^L到余l∈E_v；jump水平坐标属于h_τ，末方向属于cτ-bin c_L的实际路径数。

由实际最低度，||X_α||₁≥d_*b_*、||Y_α||₁≥n_*d_*b_*。可用的初arms总数至少e_c d_*b_*。对每个α取Z_α=X_α⊗Y_α，故

    Σ_(p,s,α)||Z_α||₁≥e_c n_*d_*³b_*³。                          (6)

定义H为Σ_(p,s) Σ_(c_W,u,h_τ,c_L,v)(Σ_α Z_α)²。展开后正是两arm共享p、t、s，各自W／L续接的真实有序hybrid；两个W末time同u、ρ-close；两个L末time同v、jump水平τ-close、末方向τ-close。u、v可不同。由于使用同一个α的tensor，没有把分别大W／L集合免费取交。

非零签名总数由§2、§4至多

    K e m³ ρ^(−κ)(ρ/τ)³τ^(−κ)。                                (7)

这里p已含其t；三个独立time坐标是s、u、v。对实际签名数用CS，(4)–(7)给

    #H≥K^(−C)e D⁶m³ρ^κτ^κ N²(τ/ρ)³
       =K^(−C)e D⁶m³ρ^κτ^κ(ρ/δ)³(τ/δ)³。                        (8)

这证明spec候选的原hybrid lower，有限常数bins若需fixed coloring只多K。它不是把W与L末time设相同，也不是在coarse共同base复制R28的16条边；初p、T₁、T₂、s及exact ψ均为同一原labels。归一前质量(8)可用于后续任何实际code，而不是任意指定条件slice仍有同下界。

## 6. 两种位移、physical blur和tilde-Lip责任

W两个末点w_i处的observable满足原(151)：

    x(w₂)−x(w₁)=(s−t)ψ+O(ρ²+δ)，
    ξ(w₂)−ξ(w₁)=[f(t)−f(s)]ψ+O(ρ||f(s)−f(u)||+δ)。              (9)

原f的本ρ尺度Lip使两块blur≤Kρ²，ell横向末label差也≤Kρ²；取σ_W=C Kρ²可吸δ，因为ρ≥δ^(1/4)。没有把native填满维数3误代入这个observable的visible x维数2。

L方面，jump点在s层相距Cτ、native label差由(5)控制。真实末label恒等式为

    η_v(l₂)−η_v(l₁)=(s−t)E(t,s)ψ
       +O(τρ+τ||tildef(s)−tildef(v)||+δ)。                       (10)

仅bounded tildef时误差可达Cτ，不能直接给τρ的细output。原§22.1开头4927及(180)5052–5055明确调用19.5；若需要e_L=C(Kτρ+δ)，应先在原ρ作named19.5整time细化，付δ^O(η/γ)原质量，再用R22和good-q平均重建(2)，之后才peeling。该准备不需要AFF／nonquad，但其高级wholeproof保named范围。计数(8)本身不需它。

即使付了该准备，也必须保δ-floor：全δ≤τ≤ρ范围只有

    e_L=C(Kτρ+δ)≤C′τ，                                        (11)

不能在τ=δ时把δ消掉。只有另知Kτρ≥δ才可简写e_L≈Kτρ。若Kρ未足小或常数使e_L≥τ，则native τ-patch已无细分信息，不能用不合法fine-base强行补增益。

## 7. 原角与time prior：只作dominating reference

固定一原初incidence(p,T₁)，hybrid的逐项恢复upper为

    K m³D⁵ρ^κτ^κ N(τ/δ)³。                                    (12)

依次选s、T₂；W第一末管、ρ-close第二末管及u；两个native jumps、L第一末管、τ-close第二末管及v，即得。除(8)后，归一hybrid的每个初incidence边际被K倍原incidence均匀law支配；第二臂亦同。因而R16／R24的heavy-used-ρ-cells步骤可保(8)的K次幂质量，取得同一H_ρ，#H_ρ≈K^±Cρ^(−κ)，Uniform(H_ρ)有q≥Cρ的slabγ upper。这里不授unused Φ_q slab，也不授选后H完整AD lower。

原fine time仍取Z_q上uniform law，normalized到长度ρ后interval cap≤K(|I|+δ/ρ)。原fine φ换H_ρ proxy只误Oρ；(9)误差增Kρ²，而(10)的kernel误差由(1)增Oτρ。raw exact ψ仍保在每个原hybrid；proxy是之后code的统一近似，不是新独立角。以上只给dominating产品reference所需upper，原time／角／endpoint相关性仍必须由真实g携带。

## 8. 同时输出的恢复检验：原分母不能隐藏

真正用于AFF不能仅有(8)。先测试最直接的共同frame：固定W末time u和L末time v；W第一末点在ell-label厚σ_W桶Q，native L第一末label在长度τ的patchB；W joint observable以σ_W分箱，L scalar label以e_L分箱。全原AD packing给两种桶数upper

    A=(ρ/σ_W)^(2−κ)K， B_num=(ρ/τ)^(1−κ)K。                    (13)

来自完整Y的packing，不给q裁切Y新的lower。两个旧单图的full-size carriers分别有参考大小

    #A_W≈K^±C(ρ/σ_W)²， #A_L≈K^±C(τ/e_L)^(1−κ)，               (14)

再乘同一原time²和H_ρ²。这些可以作为包含实际inputs的原full carriers；若要对某个joint-selected子桶声同样lower，必须另做原质量heavy修剪，不能由(13)upper倒推。

现有直接恢复从W第一point cell开始，容量C_W=K(σ_W/δ)^(4−κ)。逆选W第一末管D，两个初角bin内原初管各Dρ^κ，W第二末管Dρ^κ，恢复同一trunk。随后第一native jump至多N、L第一末管D，另一jump至多(τ/δ)³、L第二末管Dτ^κ。因此共同code的已证upper是

    M_joint≤K C_W D⁶ρ^(3κ)τ^κ N(τ/δ)³。                         (15)

关键是这里指定η_v(l₁)的e_L-cell尚未减少第一native continuation的N D容量。不能把原Y_v的AD upper直接代成这个**给定trunk的transition**上界。

## 9. 实际product-frame费用与缺的条件纤维估计

将(8)按u、v及(13)的两种桶平均，再除(15)及(14)×m²×#H_ρ²，已有计数所能保证的product-reference平均至多在下界证明中留下

    K^(−C)(e_L/ρ)^(1−κ)。                                     (16)

具体消元：C_W A(ρ/σ_W)²≈K^±C L^(4−κ)≈K^±C e/m；另一桶数B_num乘#A_L≈K^±C(ρ/e_L)^(1−κ)。故(16)不是可冒K的空常数。若e_L≈Kτρ，则为K^(−C)τ^(1−κ)；全范围应保(Kτ+δ/ρ)^(1−κ)的physical floor。这只是**现有恢复upper／计数保证的不足**，不是对实际best graph mass的upper，不证明所有编码都一定损此幂。

修复该直接证明需要一个真实条件输出分散结论：给定W恢复的trunk及相关code，L第一continuation进入某native e_L-cell的数量应比N D少约(e_L/ρ)^(1−κ)，或有足够的联合平均替代。完整scalar Y_v的AD upper只控制其自身点数，不控制按trunk／point-dependent ξ偏置后的此transition概率。两单图各有dense g亦不能推出它们的product endpoint law有dense共同g。

可以保实际joint endpoint law或引入依trunk的conditional prior，但这会失去固定产品carrier／共同time-reference；若重新归一，其实际mass与容量成本必须再付。不能以定义该prior就完成AFF，也不把这样的disintegration冒成原独立θ／ν条件。R57已排若干免费容量组合，这里未新增一个公设去绕过它。

## 10. 条件纤维的真实局部聚焦校准

点态形式的上述纤维cap不是单凭filled3就真。固定s、v及一native grainη=y，取局部tildef=0、a=b=c=d=0，令native horizontal坐标为(x₁,x₂,w₁)。沿该grain所有jump点tilde p取原straight continuation方向(φ₁,φ₂,0,0)，则η_v(l)=y对全部jump／角成立。native水平可为完整三维δ-grid，Φ可取R²中的κ-AD产品Cantor，带γ≤κ/2的slab upper；每jump有D级真管选择，第一continuation可确有N D个，全部落同一δ-native-label cell。

这是实际空间／直线的局部校准，不是抽象两图交集玩具；它严格反对给定exact trunk的无条件(e_L/ρ)^(1−κ)分散断言。可在固定时窗填满这些平行native hyperplanes并保两种filled grain和constant ξ coherence。但它**未保全配置的正κ、η≪κ原CW**：若如此平行结构延至全部原times，全族会在native薄slabs中超浓集，正是19.4所排的低速情形。故不称完整Def17／Kakeya反例，也不否定利用global CW／不同v共同平均可能得到更细条件估计。

同理，这只反per-trunk cap，不反对W-coarse-code下更弱的平均纤维结论；不同exact trunks也许提供额外spread。本稿没有把(16)的粗恢复损失当作all-strategies impossibility。若新proof要用这类spread，须把它作为真正原联合几何步骤证明，不能从单Y AD或core最低度自动读出。

## 11. 对AFF₃的实际尝试：新增scalar坐标并非独立增量

两输出保同一fine ψ、t、s，但native kernel在代数上是W竖直增量的time-dependent contraction。令Δξ_W=[f(t)−f(s)]ψ，则

    (s−t)E(t,s)ψ=(s−t)(−d(s),1)Δξ_W。                         (17)

因此不能把native输出看成另一个独立方向样本或free-rank第三分量；固定t、s后它是已有matrix increment的一个线性函数。若对实际joint carrier用sum-product／ABC，须处理该time-dependent系数和同一原g的条件分母，不能直接套scalar Theorem21.2证明whole f affine。

现有R27 A_W约r^(−2)，R24 scalar carrier约w^(−1+κ)。单独用前者仍遇matrix AFF₃障碍；用后者的scalar engine仍需已有whole-f AFF／nonquad，不能循环。将二者做成独立产品会先遇(16)；保相关joint carrier又没有已证统一逆定理能在这些具体标签／误差下输出whole-matrix fit。本轮已实际完成这一步恢复与kernel检查，未仅凭hybrid count宣AFF用途完成。

## 12. 合法restriction、旧等价及具名依赖

core是有限原关联子图，(8)为真实原tuple数量。原ambient upper／slab在未归一分母下继承；任意后续取桶、选time／角／ψ都须以(8)收费。(12)支付了初始角heavy步骤，不支付指定endpoint后条件slab。平均原mass保留与core局部逐管最低度已分别证明，原whole配置／原全family逐管shading没有被免费继承。

原R16 good-q／AD与coherence接口按已审有限范围使用；若作细blur准备，19.5仍具名source，不声高级wholeproof全独证。这里不调用19.2／19.4排完整分支，也不以R66 tiny阈值把g变raw pairs。原W单图与L单图恢复作为对照已实际读回R27／R24，并非把它们密度相乘。

同trunk tensor统计比R28仅coarse同base有限box多了实际exact初管／中点，但还没有growth或新的全称gain。不能作为stationarity、W／BSG、fixed arms或CP／PM的换名方向；只记录此次完整原计数和明确条件纤维责任。无新ID／novelty／major／ordinary界。

## 13. 初步检查及随后修补的边界

目标hybrid lower(8)已给完整有限证明，原native几何、共同time／exact ψ、q边界、粗方向支持及三个最低度均付。对AFF的最直接产品恢复尚欠真实normal transition分散，(15)–(17)给出精确所在及固定幂费用，局部聚焦只排过强pointwise修补，不反全source。不能把计数准备称完整mixed43进展或拿conditional prior定义补洞。

不能因此宣布全joint编码失败：以上只否给定exact trunk的单边normal分散修补，(15)也只是粗恢复upper。root随后在天然尺度提出同时使用W与L第一末点的normal匹配，B独立核通；数学前spec已补精确范围。以下实际独核这个更细恢复，替代“必须另添条件cap”的初步思路，而不是在(16)上续调参数。

## 14. 自然尺度的两端patch兼容

先付§6的named19.5整time准备，再good-q和core。取σ=ρ²，天然τ满足

    σ≈_Kτ≈_Kρ²， ρ max||E||≤cτ，
    e_L≈_Kρσ≈_Kρτ≥δ。                                         (18)

例如取足够大的K次幂乘ρ²，使(1)成立；η相对µ及所有固定指数最后小，保证τ≤ρ、e_L≤σ并且Kρ≪1。δ≤ρ⁴使本自然尺度的δ误差确可吸入e_L。σ若不是原allowed，σ-coherence借上邻格并细分／固定邻接，只付K；本节不把genericτ的floor问题删除。

记native水平U∈R³、native labelη，原ell ξ=(ξ₁,ξ₂)，ζ_z=ξ₂−d(z)ξ₁。q的同一coarse ξ_q给各点ξ=ξ_q+O(Kρ)，19.5给tildef_s−tildef_z=O(Kρ)。分别沿p_s→w@u及tilde p_s→l@v，且中间native label相同，将两条native输运式相减，得到

    η_v(l)−η_u(w)
       =(v−u)ζ_q+[tildef(u)−tildef(v)]U_q+O(Kρ²)。              (19)

ζ_q可用固定q-anchor的d值定义；改成d(s)只变O(Kρ)，再乘长度ρ，仍O(Kρ²)。原各horizontal坐标距U_q仅Oρ，斜率差乘它也只有O(Kρ²)。方向项的剩余差包含同等级ρ·O(ρ)，无需两末管方向彼此接近。

因此固定u、v与W第一ell-label桶Qσ后，η_u(w)在O(σ)区间，η_v(l)只落一个已知中心的O(Kσ)区间。τ≈_Kσ时它仅遇K^C个native τ-patches，**不能再按(ρ/τ)^(1−κ)独立枚举**。中心依固定u、v、Q与q-anchor，不依初t、s／ψ／fine η_u。所有点仍是原labels，边界只多固定邻接patch；没有把完整Y_v免费裁成AD子集。

## 15. 同一W／L两端normal匹配的完整恢复

固定共同code的W输入a_W=(x_w,ξ_w)σ-cell、ell桶Qσ、native第一末labelη_v的e_L-cell，以及t、s、u、v和两个初角ρ-cells。先枚举W第一末管与L第一末管的ρ-angle packets，每种至多Kρ^(−κ)；再枚举第一native jump的水平δ-cell Ũ，至多KN。它们不是新code坐标，其费用要进恢复upper。

令v_h^W为W管的native前三方向，原straightline反向到s给

    η_s=η_w+(s−u)ζ_w
       +[tildef(u)−tildef(s)](U_w+(s−u)v_h^W)+O(δ)。             (20)

Qσ与visible xσ共同确定U_w到Cσ，a_W确定ξ_w到Cσ；固定W末ρ包后v_h^W的proxy误差O(Kρ)。式(20)中ζ误差乘ρ为O(Kρσ)，U误差乘斜率差Kρ同级，方向proxy误差乘时间ρ及斜率差Kρ仍为O(Kρ³)。于是

    η_s=η_w+C_W+O(Kρσ+δ)，                                    (21)

其中C_W不依fine η_w。该误差小而不要求ξ随η连续。

固定Ũ后，η_w原本只在Q给的O(σ)区间，故(21)使所有可能tilde p_s仅占K个物理σ-cubes；逐cube枚举原coherence代表ξ_C，ξ_tilde p=ξ_C+O(Kσ)。这是有限cube分组，未假point-dependent ξ是一条Lipschitz函数。沿L第一末管正向，用其已固定ρ包，完全相同的误差核算给

    η_v=η_s+C_L+O(Kρσ+δ)
        =η_w+C_W+C_L+O(Kρσ+δ)。                              (22)

C_L依Ũ、所枚举cube／ρ包及固定times，不依fine η_w。由于指定了η_v的e_L-cell且e_L≥K^(−C)(ρσ+δ)，(22)把η_w限制在长度Ke_L的一个区间。

现在用的是**native Y_u**的1−κ AD upper。U_w三水平坐标在Cσ盒，η_w在Ke_L区间，原fine w的容量变为

    C'_W≤K(σ/δ)³(e_L/δ)^(1−κ)，                               (23)

比旧C_W节约(e_L/σ)^(1−κ)。没有沿ell Y⊂R²查询免费line-KT。原δ-separated points确保每水平δ-cell／nativeδ-label组合仅O(1)点；标签δ-bin重数按§2吸K。

此后再选具体w、W末管fine子包、原初管与点、Ljump及L末管等，均是原恢复。两种ρ末包各ρ^(−κ)，其fine管各≤K(ρ/δ)^κ，乘积仍为K D²，不能先按fine D选后又免费固定包。

## 16. 新恢复上界、product reference与同图质量

严格计入上述枚举，新共同code最大重数为

    M_new≤K C'_W D⁶ρ^(3κ)τ^κ N(τ/δ)³
          =K(σ/δ)³(e_L/δ)^(1−κ)
             ρ^(−2κ)L^(5κ+3)(τ/δ)^(3+κ)。                     (24)

与(15)只差(23)的真实normal节约；两个末管ρ包的总fine费用已在(24)中。

按u、v各m个times、每u的W桶数≤K(ρ/σ)^(2−κ)及(19)的K个兼容nativepatch平均。存在真实(u,v,Q,R)使保留原H质量至少

    H_QR≥K^(−C)#H/[m²(ρ/σ)^(2−κ)]。                           (25)

取原observed carrier A_W的σ-cells、原native Y_v在兼容R中及固定邻接的e_L-cells A_L；两个input／output桶可固定倍扩大，保真实末点。其最大card分别≤K(ρ/σ)²与K(τ/e_L)^(1−κ)。依(8)、(24)–(25)，

    H_QR/[M_new·(ρ/σ)²(τ/e_L)^(1−κ)m²ρ^(−2κ)]
        ≥K^(−C)(σ/τ)^(1−κ)≥K^(−C)。                          (26)

最后一步**仅用天然τ≈_Kσ**。这是(16)的真实修复：兼容patch免B_num，fine w节约(e_L/σ)^(1−κ)，两者共同抵消原fixed power，未给exact trunk单边正常cap。

令每code原重数除以M_new，所得0≤g≤1，均值相对

    Uniform(A_W)×Uniform(A_L)×Uniform(Z_q)²×Uniform(H_ρ)²

至少K^(−C)。这里只说**参考产品law**，实际原hybrid全部相关性仍在g。若actual carrier card比upper小，均值只更大；(26)和g≤1反而迫两种card各达其upper的K倍范围，不能反过来仅由AD upper宣lower。full Y的packing也允许扩native input／output patch只多K，不给裁切Y重授AD lower。

## 17. 获得的joint关系及AFF仍未付的步骤

自然尺度下两个working resolutions一致：W空间除ρ，native空间除τ，σ/ρ≈_K e_L/τ≈_Kρ。同步将ξ observable及f同除L_fρ，定义M(t)=(f(z₀+ρt)−f(z₀))/(L_fρ)，d保原值。规范化后每个positive joint code同时满足W矩阵作用及native scalar作用，原time／原角参考和g相同。native增量的式(17)仍成立；它不是独立的第三normal rank样本。

因此§11初检中的“共同product graph尚未建立”在此天然尺度已被(26)支付；但“由它推出whole-matrix AFF₃”仍未付。不能直接把d(s)的skew E核视为13.5的单函数对称核，或把scalar Y的低维结论倒过来作为已有AFF准备。保joint g后某个slice g可能质量小，选ψ／time／W-variable再调旧scalar引理都须逐项给原reference mass。

一个实际可测试的简化是由19.5在本窗d(s)=d₀+O(Kρ)，令h=b−d₀a。则ρE(t,s)=ρ[h(t)−h(s)]+O(Kρ³)，该误差在天然e_L内。故native单图可尝试对row h的scalar projections调用原13.5的nonfit反证，得到某种部分affine关系；这最多控制b−d₀a而非两row全f。将其宣成whole AFF或把剩余a的矩阵作用免费降为ell2均不成立。本稿没有完成该新的uniform nonfit／global time／full inverse责任，不将这个简化登记为结果。

## 18. 最终阶段结论与待互审

已实际自证core、allτ的hybrid count，并独立逐项核root提出的天然τ两端normal匹配和共同bounded product-reference g。修复只用原tilde-Lip准备／σ-cube coherence／两套grain与native scalar AD，没有新增smoothness、conditional AD、good-rank、ξ沿grain常量或per-trunk cap。它严格超过把两旧单图密度相乘的未证论断，但仍是完整AFF责任的前端联合接口，未给增长／ordinary维数界／major或新ID。

下一不得以重复core、Gram或调τ微参数结案；真正剩余是这个已付共同g上的whole-matrix逆结论及其原全局time回传。若只是R28有限box或给g添独立性，立即记旧责任而停止。root／B最终稿待实际全文互读，A参与正证不自算独审；未经外部同行评审，Goal active。
