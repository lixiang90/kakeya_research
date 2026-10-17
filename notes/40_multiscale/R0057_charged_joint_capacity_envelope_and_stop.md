# R0057：同一H5的conditional-capacity带费组合及全partition障碍

2026-10-17。先周期macro/spec，再本证明。仍以原ordinary R5 H5固定正幂增益为目标；本稿未证明/否定H5，未反Th2.2，未声重大或新颖。只允许一次新all-s输入的实际机制检验，不为同一目标新增ID。未经外部同行评审，最终独审另存。

## 1. 原问题与真正检验的组合

δ=M^-1→0，原R5物理轴方向δ分离，原positions任意、whole unit segments及near-full原marks保留。固定有限graph charts可写为(t,V+tU)，U,V∈R4，各拆为两个R2 block；两个block共享同一T和原label。

新具名输入是官方elliptic Th2.2：fixed0<s≤1、0<κ<1/10、有限D，原条件time support/maxweight的all-dyadic双profile、独立center/同shape的初始jointellipse cap；结论dominated subpower质量，终端用X_v=V+vU、v=T1左端，q<1+2s−10κ，initial floorδ^D、terminal floorδ^(D−1)。原103页wholeproof未独证，不能因作者署名认证。

本轮实际组合（仅采用Th2.2所保证的指数，不声其最优q的上界）：按另一block的(U2,V2)把原base law分成可测椭圆包，对每包调用第一block传播，最后用第二block的确定性椭圆slab覆盖来聚合pointwise cap。我们证明一项全partition/全dominated保留的费用下界，严格阻止此**仅以scalar K与slab envelope付联合增益**的版本。它不阻止利用joint support、空间更细分解、其它坐标chart/源base或新的多尺度几何。旧free-cap交换例只作原族；新工作是整个带费组合的任意包/任意阴影预算。

## 2. 两次不条件化的调用确有合法闭包

先区分可付部分。若原U有有界4D密度且坐标有界，则其两个2D边际有界；故任意ellipse E，Pr(Uj∈u+E,Vj∈v+E)≤C|E|≤C Wκ(E)，不需要V独立。对离散满δ方向族，原方向δ-box内独立jitter后可得该密度，基数/权cap的subpower费用保留。wholeclock上jitter只动Oδ，原marks经固定邻格增厚回传，不换原label。

假原law为有界base prior×uniform时间（near-full原time shadings只多M^η误差）。令ν≤μ，总质量r>0，密度f(P,t)∈[0,1]；g(P)=∫f(P,t)dt（clock先仅用于概率归一为长1，不改变物理轴）。删g<r/2的base labels，至多删r/2原ν质量。剩余每base conditional time对任意dyadic J有Prν(T∈J|P)≤2|J|/r，support≤2^j。归一化ν后jointellipse initial cap≤2C/r。

若r=M^-o1，time error和K仅M^o1。因而顺序对两个block调用Th2.2、每次heavy原base并保共同最终子律，可以合法保subpower质量；第一次upper由domination保留。两unitellipse终端边际各可到M^-(3−10κ)+o1。**这里没有证明联合指数，两个边际不能相乘。** 本轮没有把这个初等闭包当成果终点；真正要算的是以下conditioned组合。

## 3. 原交换族、真实单位轴与统一source clock

取a,b独立uniform于固定小square Q⊂R2，令原slope U=(a,b)、intercept V=(b,a)。原物理单位轴是以(0,b,a)为midpoint、direction (1,a,b)/sqrt(1+|a|²+|b|²)的长度1轴。固定足小ℓ>0，使全部轴包含原graph t∈[−ℓ/2,ℓ/2]；这保固定比例完整原shading，未延长轴。原Y=T全阴影，unit端帽不受任何证明假设删去。

为调用source设τ=t/ℓ+1/2∈[0,1)，只重参数化共同子clock。于是

    U1'=ℓa,       V1'=b−(ℓ/2)a,
    U2'=ℓb,       V2'=a−(ℓ/2)b.                              (1)

特别第一block是第二block参数的固定scalar线性组合：

    U1'=ℓ V2'+(ℓ/2)U2',
    V1'=(1/ℓ−ℓ/4)U2'−(ℓ/2)V2'.                           (2)

常数只依固定ℓ，不依δ、ellipse aspect或partition。物理direction参数(a,b)有完整4维图像而非被压低；本族并集体积为常数量级（例如t=0的(a,b)↦(b,a)可逆，整个小固定t区间Jacobian有下界）。所以它绝非Kakeya小并集反例。

## 4. 任意椭圆partition、保留law与容量下界

对上述**同一原族**，任取有限或可数可测base partition Γ_j（μP-a.e.分完；可另计未保留部分），Γ_j⊂{U2'∈b_j+E_j,V2'∈a_j+E_j}。E_j中心在0、任意orientation，semiaxes δ≤w_j≤L_j≤C0；各j的scale/shape可不同，Γ_j不要求乘积或均匀。ellipse中心可选与原bounded参数相交者，故a_j,b_j统一有界。令p0_j=μP(Γ_j)。

任意最终ν≤μP×dτ（允许依P,T的任意删选），质量m>0，p_j=ν(Γ_j×[0,1))。零prior项p0_j=0则p_j=0。把源调用的pre-law normalized后，若其支持在Γ_j，(2)迫(U1',V1')分别落于两个独立center、同shape的Cℓ E_j。对**实际**源jointellipse capacity常数K_j，必有

    K_j ≥ c_ℓ / Wκ(E_j),       Wκ(E)=L^(1+κ)w^(1−κ).        (3)

因为一个固定倍ellipse product包住全部条件质量1。若Cℓ L_j>1不合原测试最大轴，把该product用O_(ℓ,C0)(1)个允许ellipse products覆盖，取一项有固定比例质量；其W与W(E_j)固定可比，得(3)。选固定D≥2且δ充分小使固定缩小后的最短轴仍≥δ^D，故没有偷用initial floor之外的测试。权跨度不影响支持性论证。

ν也可为source调用后保留的共同子律；真实调用的pre-weight q_j≥p_j，真实K_j仍满足(3)。以下甚至乐观地将coefficient减成p_j，而非较大的q_j。若有time-profile或归一化额外费用，只会使所检验的给定包络更大；不假它们自动付清。

## 5. 原time支持与不可丢的二次质量

用原δ-bins I_v，v为左端点。令A_j为ν(Γ_j×I_v)>0的bins之并，a_j^time=δ×active bin个数（避免与ellipse center a_j混淆）。原T独立uniform及ν≤μ给

    p_j ≤ p0_j a_j^time.                                   (4)

连续版本也可用可测密度h_j(t)=∫Γj f(P,t)dμP，A_j={h_j>0}，同式成立。不是拿某个potential whole time支撑充原shading，也不将global m说成逐label密度。

于是Cauchy–Schwarz及Σp0_j≤1给

    Σ_j p_j a_j^time ≥ Σ_(p0j>0) p_j²/p0_j
                       ≥ (Σ_j p_j)² = m².                  (5)

countable情形用finite部分和极限或Tonelli；无独立性、等权或每包质量下界。若不是partition而是原base上重复packets、Σp0_j≤B且保留mass按真实重复计，则相同推导为≥m²/B；不能把重复数免费归一。本文主要结论用B=1。

## 6. 任意scale/orientation的joint envelope严格下界

设S_j(v)为空（v∉A_j），或为a_j+v b_j+C1 E_j（v∈A_j），C1固定足大以含Γ_j所有第二block终端位置及原fixedδ误差。minwidth≥δ使左bin/真实time的Oδ误差可固定扩大，不冒thinellipse δw级误差。定义被检验的最乐观费用

    C_ν(v,x2)=Σ_j p_j K_j 1_(S_j(v))(x2).                    (6)

用δΣ_v∫dx2这一3维volume归一，(3)–(5)给

    δΣ_v∫ C_ν(v,x2)dx2
       ≥ c Σ_j p_j a_j^time |E_j|/Wκ(E_j)
       = c' Σ_j p_j a_j^time (w_j/L_j)^κ
       ≥ c'' δ^κ m².                                      (7)

所有slabs在固定bounded (time,x2) box内，故

    ||C_ν||∞ ≥ c δ^κ m²,
    ||C_ν||Lp ≥ c_p δ^κ m²      (1≤p≤∞).                   (8)

这是全可测partition、全orientation、任意自适应axis lengths、全time-dependent dominated保留law的严格预算，非一个固定split取K=1的旧错误。即使m=δ^o1，费用也不能小到δ^(1+c)。κ的eccentricity benefit至多δ^κ，不能被漏作任意固定大gain。真实preweight≥p_j或其它正费只增大给定包络。

这个δ^κ幂在本架构内还可同轮饱和，不是证明中的松常数。把原a、b各按其第二坐标分成宽Δ≈δ的strips，第一坐标不分。Γ_(k,l)为这两个strips的乘积，p0_(k,l)≈δ²，原T全部保留，m=1。选共同长轴为第一坐标、semiaxes≈(1,δ)的E_(k,l)。在(1)的固定scalar变换后，条件(U1',V1')的joint4D密度≤Cδ^-2，且其两个long-coordinate的联合边际有界，独立于短坐标。任意orientation、semiaxes L≥w的source测试F有

    Pr(U1'∈u+F,V1'∈v+F)
       ≤C L² min{1,(w/δ)²}.

第一界用两long projections长度≤CL，第二界用joint4D密度及|F|²。除以Wκ(F)，w≥δ及w<δ分别给至多Cδ^(-1+κ)；因此continuous strip prior的真实K≈δ^(-1+κ)，对所有fixedD允许的小测试均成立。反向是(3)。

第二block短坐标slab的center是kΔ+ℓ(v−1/2)lΔ，宽Cδ；固定v、x2时，每l只有O(1)个k可覆盖，故至多Cδ^-1个包。每项p_jK_j≈δ^(1+κ)，于是||C_ν||∞≤Cδ^κ，与(8)匹配。这个sharpness是连续原prior版本；未jitter的有限δ-grid在w<δ时有原子，不能免费声同K上界。若按原δ-label cells作Oδ jitter，则恢复连续strip law且只需原fixed邻格空间费用；不重置marks。该饱和校准只完成本轮费用审计，不开下一条strip/template方向。


## 7. 把新的all-s源指数真正代入

每包调用后，若仅用源unitellipse的uniform第一block cap，再经第二block slab cover聚合，得到的upper形状是

    joint_atom(v,x1,x2) ≤ Cε δ^q Σ_j θ_j K_j 1_(S_j(v))(x2), (9)

其中θ_j≥p_j是该次调用前实际未归一化权，q<1+2s−10κ≤3−10κ仅是本次采用的保证指数。Th2.2只声称q*下界，不禁止其它论证获得更强指数。实际preweights、source常数、保留归一化可能更差；不能把θ_j无费换成较小p_j后仍声(9)成立。为了否掉这种预算，我们只考察更乐观的数值表达式δ^q C_ν，它是(9)右端的下界，**不是已知的真实joint atom upper**。允许各包s_j不同，使用该具名定理直接保证的指数仍均小于3−10κ；各项数值包络因此≥δ^(3−10κ)p_jK_j1Sj。

要只靠这个envelope uniform证明joint atom≤δ^(4+σ)，需费用≤δ^(4+σ−q)。然而(8)使这个候选upper envelope的sup至少c δ^(3−9κ) m²（严格q的余量只使upper envelope更大）。m≥δ^η且η充分小时，3−9κ+2η<4+σ。因此所给数值预算不能得到H5级均匀atom cap；改κ/s/包数或保留subpower质量不闭合。这里是对**某个upper-bound表达式的下界**，不是说真实joint atom达到该表达式，更不是体积counterexample。

即使额外慷慨假给每包q=3，这个乐观数值包络的sup仍≥cδ^(3+κ)m²；κ<1/10、η小仍不足δ^(4+σ)。因此失败不依把10κ误读为singleblock最佳指数上限。

如果再无条件对另一block也用source，得到两个边际uniform caps，不能将其乘成δ^5。对两个不同包络取pointwise min，或只在实际joint support上积分，可能依赖额外信息；(7)不自动否定这种方法，也不证明两个各自sup大就min的sup大。本文没有这种逻辑跳跃。未支付的正是原joint support/条件重叠关系，不能附为公设后称完成。

## 8. 有限原方向、实际阴影与单位几何

取a,b各在小Q的Lδ-grid，L固定大；物理direction(1,a,b)的归一化在该bounded chart为固定双Lipschitz，给N≈δ^-4的原δ-separated方向、固定常数cap。原轴是§3实际unit轴，不是标签或曲线。完整Y_i=T_i，限制共同I只取固定比例原质量，符合near-full门槛；没有用端帽附近任意旧shading免费裁剪。

把base prior改为有限等权或任意原权后，(2)–(8)仍逐字成立：只需Σp0=1和独立uniform time。源initialK在细于δ的tests可能更大，不会破(3)；若需δjitter调用可付的边际步骤，保持original label并记录Oδ几何误差。离散time用δ#activebins而非假连续时长，故极少的time bins不能保subpower m而逃过(5)。数学证明未用有限数值计算。

本countertest覆盖的是一个正角度4维direction chart内的合法原族。可用固定rotations的多个这样的族覆盖全部方向，但若packet允许跨charts改split，(2)的统一关系未必仍成立；我们**不**据此声称所有global adaptive decomposition已被否定。甚至本chart真实union也常数量级。需要ordinary Hausdorff结论的覆盖/跨尺度责任没有被此模型替代。

## 9. 与旧冻结、等价和内部结果的区别

本轮不是以新名称提出另一个正gain命题；目标始终旧H5。CP/PM全称shading闭包使其正gain版本互相导出时不登记新ID。新all-s输入只使一次原law组合尝试合法；其完整条件没有被粗降成“任意λ的3D结论”。旧swap free-K例本身已在R56知道，本轮新增的是包含p_j/p0_j、m²、ellipse aspect及任意partition/retention的(3)–(8)连续量化，改变是否继续该具体组合的决策。

这些是方法失败审计，不是重大中间结果或新颖定理。H5/general G3/general-to-sticky及各actualmixed仍未解；四维source已付内部assembly与DIM001既有KT定位保持。源Th2.2具名wholeproof未审和本application可否付费是不同责任。

## 10. 停止与下一选择门槛

停止在相同source base、scalar K与确定性椭圆slab envelope中继续调s/κ/partition。若要重开，需实际利用joint support/原crossblock重叠或不同的新几何输入，不能再假“条件caps良好”、改用平均成本名字或重复交换toy。下一宏观必须围绕完整高维目标选择不同关键机制；本稿不预认证后继，不让初等负结果替代长期终点。

最终两独审及root整合实际读回后才归档reviewed范围，未经外部同行评审。Goal active，无新数学ID、ordinary维数界、Euclidean反例或重大性认证。
