# R0115 scalar ξ cap：原相位双向闭包、真实 pair 前向与目标强度审计

2026-10-26。仅本稿为本代理分工；不改公共状态或Git。本轮的相位关系是**排重与原质量核算**，不另开方向，不登记新数学ID，不声完整source gain、ordinary下界或重大结果。

## 1. 恢复、首要缺口与本稿可证伪范围

沿用当前GOAL、STATE、ROADMAP、registry及R114 next。首要缺口是完整五维matrix33、κ=1原source中的bulk同T耦合，或真正不同的ordinary机制；不是再证旧六维17/4。本稿读取R114 rough §9的强标尺，并对照R104–108原质量/失败、实际本地Wang–Zakharov Def17.1–17.4及Lemma19.2、19.4的下述范围。

固定γ>0、K=δ^{-C₀η}，η在所有固定指数之后充分小。待审强标尺S为：存在a,τ>0和有限C，对每个完整source、每个原grain g=(u,y)、每个固定ν∈S¹和b∈R，在allowed ρ∈R_η∩[δ^a,ρ₀]有

    #{x∈X_g: |ν·ξ_(x,y,u)−b|≤ρ}
        ≤K^C ρ^τ #X_g.                                      (1.1)

ν可随grain改变，但不能随x或φ改变。S尚未证明，也没有锁为排除完整branch的充分或最弱输入。本稿可检验任务是：(i) 它与同grain原pencil的线参数相位cap是否只是双向改写；(ii) 它究竟给什么**实际同T两次访问**的前向结论；(iii) 反向和删选在哪一步需要新的lower。独立攻击为δ/|v−u|误差、重复访问、稀质量grain、终点degree偏置，以及把全局平均误读成∀grain。若仅得相位改写或未付新clock law，立即停止主增益登记。

## 2. 原source与用于核算的真实witness图

取d=5、k=ℓ=3、κ=1。写物理点为p=(x,z,u)，其中x,z∈R²，

    E_u={(x,y+F_u x,u): y∈Y_u, x∈X_(y,u)}.

原N=#T≈_Kδ^{-4}，T为joint-4AD且whole-containment CW≤K；本稿采用源(19)/Def3.9的usual管规范，clock段为[−1,1]，不额外要求arclength恰为1。Z是δ-separated共同clock，m=#Z≥K^{-C}δ^{-1}、m≤Cδ^{-1}。各Y_u为AD1、tube-KT(1−γ)，各X_g为δ-separated且#X_g≈_Kδ^{-2}。每point的Φ_p为AD1/slabγ，#Φ_p≈_Kδ^{-1}，每φ有**原T中的实际witness**，斜率为

    θ(T)=(φ,ψ),       ψ=ξ_p+F_u φ+O(δ).                      (2.1)

allowed coarse time windows的Y-union AD下界、point Φ/ξ coarse coherence仍是完整输入。本文没有把它们从单层构造补齐。每slice #E_u≈_Kδ^{-3}，而整个E跨m clocks有#E≈_K mδ^{-3}，在m≈_Kδ^{-1}时是δ^{-4}，不是δ^{-3}。

为保每point的pencil lower，对每point、每Φ_p的δ角bin选一个实际witness，再合并重复(p,T)，得到边图G。设d_p为point degree，则

    K^{-C}δ^{-1}≤d_p≤K^Cδ^{-1}.

一个原T在固定u只穿过O(1)个δ-separated E_u点；记其所用重数为w_Tu≤B，其中B只依固定几何常数。**此处不再每(T,u)强选一个canonical point**：那种选择可用于只需总I的pair计数，却不能自动保每个point的degree lower。本文全程保有界重数。

令G_g为origin在grain g的边，M_g=#G_g，M_u=Σ_yM_(u,y)，n_T=Σ_uw_Tu，并记

    I=Σ_T n_T=Σ_g M_g,       M_g≈_Kδ^{-3},
    M_u≈_KN,                I≈_KNm.                         (2.2)

这都是同一原N和真实原访问的selected下界图，不是重设N为使用管数，也不是声所有未选过p管的degree有同样upper。若沿用更大的原shading计数，则G是其中明确保留的子图；不能把两种I未经比较互换。后文I专指(2.2)。计数I亦不等于物理shading体积；δ-cube版本每visit的体积尺度另为δ⁵。

## 3. 每grain pencil相位cap与(1.1)的双向等价

固定原grain g=(u,y)、0<|h|≤2。以原管T的同一条支撑轴表示x_T(t),z_T(t)，定义线参数functional

    Q_(g,h)(T)=[z_T(u+h)−F_u x_T(u+h)−y]/h.                 (3.1)

因轴在u处距p为Oδ、斜率满足(2.1)，逐项相减得

    Q_(g,h)(T)=ψ−F_uφ+O(δ/|h|)
              =ξ_p+O(δ/|h|),       (p,T)∈G_g.             (3.2)

如果u+h不在原管的clock段上或不是selected clock，(3.1)只是在**既有支撑线参数**上求值，不是新造实际mark，也不能用于未来访问lower。

令A_g(b,r)=#{x∈X_g: |ν·ξ_p−b|≤r}，令

    L_g(b,r)=#{(p,T)∈G_g: |ν·Q_(g,h)(T)−b|≤r}.

取ε_h=Cδ/|h|，对r≥ε_h，

    K^{-C} A_g(b,r−ε_h)/#X_g
        ≤L_g(b,r)/M_g
        ≤K^C A_g(b,r+ε_h)/#X_g.                            (3.3)

证明不是概率独立性：左侧每个内带point的全部d_p条边都落phase带；右侧phase带的每条边，其point必落外带；再用d_min、d_max和M_g≈d_p#X_g。反向同样将point半径r的带包含于phase半径r+ε_h的带。因此统一的point scalar cap与统一的**完整原pencil边图**phase cap，在K费用、误差floor及半径调整内双向等价。

在allowed离散半径上，只能在相邻allowed上尺度仍≤ρ₀时付该调整，其倍率至多Cδ^{-η}并入K^C；不把最低误差以下或超出顶尺度的式子声为同一结论。最干净的调用是ε_h≤ρ/2时，以phase半径ρ/2向point半径ρ比较。

故把ν·ξ改名为ν·(ψ−F_uφ)、endpoint phase、normal response或kernel scalarization，**没有产生新的正幂输入**。该双向关系不允许只保一部分未来可达边后仍宣反向：未来删选可能完全偏置point degree。

## 4. 已实做的前向：S给实际原same-T far-pair phase cap

这一步不靠虚拟u+h，且保(2.2)的原I。取r=δ^b、0<b<1，η充分小。令P_far为所有有序pairs

    (p,T,q),  (p,T)∈G at u, (q,T)∈G at v, |v−u|≥r.

两端都是同一原usual tube的实际selected访问。Cauchy–Schwarz与δ-separated clocks给

    P_all=Σ_T n_T²≥I²/N,
    P_near≤B C(r/δ+1) I.

由I≥K^{-C}Nm和m≥K^{-C}δ^{-1}，有P_near/P_all≤K^C(r+δ)→0，故

    P_far≥I²/(2N)≥K^{-C}Nm².                              (4.1)

这里没有逐管duration lower，也没有把u,v独立抽样。即使若干管无marks，其原N仍留在CS分母。

对实际pair，令g=(u,y)为origin grain，并定义可直接从实际终点读取的response

    R(p,T,q)=[z_q−F_u x_q−y]/(v−u).

同一原轴关系及两端Oδ误差给

    R(p,T,q)=ξ_p+O(δ/r).                                  (4.2)

给每个grain任意预先固定的ν_g,b_g；不得依pair另选ν。对allowed ρ满足Cδ/r≤ρ/2，若(1.1)成立，则

    #{far pairs: |ν_g·R(p,T,q)−b_g|≤ρ/2}
        ≤K^Cρ^τ m I
        ≤K^Cρ^τ P_far.                                    (4.3)

证明：该pair的origin point由(4.2)落入原半径ρ的scalar带；(1.1)及原d_p比较使这些origin edges总数≤K^Cρ^τ I。每条origin edge至多有Bm个实际terminal edges，乘此上界，再以(4.1)、I≈_KNm比较。没有新增终端管或clock，亦未删X、Y或Φ来生成新source。

例如若a+b<1，则在ρ≥δ^a时δ/r≪ρ；仍须满足ρ是原allowed尺度。这个前向是真实原I的量词推导，但**不是证明S**，也不是新pair gain：它只是说明若S已付，则其实际phase运输后果可用。尤其R是ξ的同管运输，不是R107关于F-secants的clock observable。

反向未付。P_far的origin分布被n_T及实际future可达性加权；总(4.1)并不保证每个grain、point或pencil edge都有定量多future partners。因此即使知道(4.3)，也不能从实际pair边数读回(1.1)。只有§3保留全部pencil边、未以未来可达性筛过的phase cap才有上述双向结论。

## 5. 与19.2/19.4、R104–108及完整gain的强度边界

原Lemma19.2的前提是在每个相关ϱ-window中有δ^ε比例clock使**整f矩阵**变化≤σ，σ∈[ϱ²,ϱ]；19.4是在某window有这类**整tilde-f**的clock集中。19.4先用nativeY tube-KT、coarse ξ与真实same-T制造whole-vector ξ集中，再以CW排它。不能从一个固定scalar ξ带直接赠送任一整矩阵slow前提。

whole-vector ξ-ball cap β≤K^Cρ^κ已是19.4“concentration⇒CW”半段闭包：本κ=1时为K^Cρ。R114明确核过原4AD lower膨胀回原N。固定ν的scalar集中只把原整管推近4-plane，包装/4AD给βK^{-C}Nρ，而CW upper同为KNρ，幂抵消；旋转ν或丢掉另一normal坐标不能复用vector cap。投影后商管族joint-4AD、CW和filled X亦不免费保。

R104完整affine-2plane code cap消费两条独立code normal；一条normal只给moving row，不能恢复whole F。R105 projected-line方向集中同样只迫code3plane/单row，其time-plane ball cap不授point scalar cap。R106 exact ξ₂=x₂的字段及两锚模型缺nativeY/完整bulk，不能作完整source反例。R108 terminal ξ联合式本是same-T旧式；它不免费给初始kernel fibre的碰撞lower。

R107的可用条件law是对**原clock测度**的

    σ_u{v: |k₁(v)−c|≤s}≤A s^α,
    k₁(v)=(f₁(v)−f₁(u))/(v−u),

还要共享coarse图、row/code原提取及其真实D上界。条件energy才给同shell原pair upper

    I_H≤K^C sqrt(A) δ^{-6} H^{1+α/2};

与lower≈_Kδ^{-6}H相比，需K^Csqrt(A)H^{α/2}→0。这里k₁只依F,u,v；S及(4.3)则控制grain内ξ或其同管运输。两者参考测度和变量不同，**没有证明任一从另一推出**；不能把(4.2)的“跨时刻”措辞当成已付R107 transverse clock law，也未给满足完整source的反例来宣逻辑不可比。

记B为“在所需小η顺序下不存在这种完整matrix33 κ=1 source”的branch排除。B当然使S真空成立；本稿没有S⇒B，因为尚无从S导出矛盾的原coupling。更没有S与全部ordinary/一般Hausdorff目标的双向等价：后者还有ordinary初始化、其他mixed/κ等责任。若将来声S足够，必须补具体原计数链，而不能把想要的clock law附入成功hyp。§3已证明的是相位重写的双向等价，§4是单向实际pair后果，两者不能混成完整gain。

**本轮锁后整合注：**上段记录的是本稿phase计算自身的阶段责任，已由本轮另一项实际构造补上资格结论。algebraic主稿 notes/40_multiscale/sticky_matrix/R0115_fixed_row_full_source_countergate.md 从任意假想完整source，保旧bulk层并加入singleclock dust；在准确的bounded-chart usual Eq19类、固定0<γ≤γ_d=1−log₄3范围，graft仅损η的固定整数倍，故S⇒B按“存在足小η”的正幂量词成立，反向真空成立。γ>γ_d时只能先降级，不能声该较强指定γ的同参数等价。该构造已由本代理在额外授权review中独立逐式检查并读回修后版本，见 research/reviews/R0115_full_source_graft_second_review.md；不把本人的phase计算自计独审。因而本轮最终判定不是“S比source排除便宜但尚缺一个引理”，而是这个强∀grain标尺在上述范围已承担branch排除责任。两者均未被证明为真，也未等价ordinary或长期Goal。

## 6. 合法restriction：upper继承不等于完整source可重调用

对固定旧grain，原scalar带的**绝对**point/edge upper在删选后单调；若保p_g比例point或边再归一，概率upper至多损1/p_g。全局保pI的marks亦只给全局1/p费用，不能给每个旧grain统一p_g下界。

whole-T子族T'大小qN时，原absolute CW upper仍是KN|U|，改以N'归一要付q^{-1}；原AD upper亦可按此付费，而AD lower不对任意子族自动继承。若同保pI，平均shading密度变为λ'=(p/q)λ。逐管密度须另做heavy threshold，不能从平均直接读出。

要对删后数据重新调用全称S、19.2或19.4，必须确认删后仍是完整source，并核η'是否仍足够小。任意删marks/points可能使某X_g低于K^{-C}δ^{-2}，Φ_p的实际原witness lower消失；任意删Y可能失AD lower和allowed time-window Y-union lower。旧tube-KT/slab等upper在旧绝对基准下可保，重新归一要付损失；coarse ξ一致性作为既有点的upper会继承，却不能补出缺失的point、Φ或Y下界。不能仅以“都是合法shading”跳过这些source lower。

这也解释为何旧CP/PM等**对全部合法原shadings**统一成立的完整正gain仍可重调用，须拒绝其改名；但本S的定义域是带全部lower的complete source。任意新shading不是其定义域内对象，不能以不存在的闭包取得双向等价。

## 7. 全局平均、∀grain与真实原I下的稀质量floor

定义degree加权grain带浓度

    F_g(ρ)=sup_(ν∈S¹,b∈R)
           M_g^{-1} Σ_((p,T)∈G_g) 1_{|ν·ξ_p−b|≤ρ}.

它与uniform-X浓度仅差K^C。若已付的是

    Σ_g (M_g/I) F_g(ρ)≤Aρ^τ,                               (7.1)

则Markov只给

    Σ_(g:F_g(ρ)>Lρ^{τ/2}) M_g/I
        ≤(A/L)ρ^{τ/2}.                                    (7.2)

这对一固定尺度真实保原I；多尺度须对实际有限allowed尺度数另付union费用。注意(7.1)已是**每grain分别取sup再平均**；仅对一个全局共同ν,b的边分布有cap，不自动给(7.1)，因为grain最坏row可各不相同。反向∀grain S推出(7.1)，而(7.2)只有good-grain质量，绝非∀grain S。

由(2.2)可精确定位平均无法看见的量级：

    单一clock： M_u/I≈_K1/m；
    单一grain： M_g/I≈_Kδ/m。                              (7.3)

典型m≈_Kδ^{-1}时分别是δ及δ²。故一个全局坏质量upper若大于这些floor，就不能凭该upper否定单clock或单grain的完全坏事件。这里是完整source若存在时的**原测度算术**，不是已构造出一个可任意嫁接坏grain的完整source；共享F、all-scale Y-union及Φ/ξ coherence仍须实核。不能将“平均允许这种质量”写成“污染模型已满足所有source假设”。

## 8. Heavy prune实算：能恢复总duration，不能填满每grain

为明确反向边界，设C⊂G为任意真实origin-event，J=#C=pI。删去总degree n_T<J/(2N)的原管；C-incidence至多损J/2，留下的C edges各有至少J/(2N)个实际terminal edges。因此

    # {C-origin与同T任意terminal的pairs}
        ≥J²/(4N).                                         (8.1)

扣掉|v−u|<r的近pairs，损失≤CB(r/δ+1)J。只有在

    CB(r/δ+1)≤J/(8N)

时，才得到C-origin far pairs≥J²/(8N)。这是可直接检查的原N/I重计数，未将event概率p误当成线性的pair概率；给的是p² I²/N量级。

单clock事件p≈_K1/m时，pm≈_K1；单grain事件p≈_Kδ/m时，pm≈_Kδ。这样的全局小事件不自动有任何正幂远clock的terminal lower，heavy门槛甚至可低于一条访问。即使p较大并满足(8.1)，heavy操作也只保C的总I与所留管的duration；不能保证每个旧x仍有原δ^{-1}方向pencil、每个grain仍有δ^{-2}个points，或每个Y_u及其all-scale union仍AD1。这是从平均到∀grain的实际断点。

因此本文不以heavy prune后“重生一个完整source”来反推S，也不把(8.1)声为排除坏grain的定理。与兄弟代理的physical multiplicity容量审计互补：那里核任意source-size点层可承多少原访问，本文核相位cap与这些访问之间的量词，不重复其新增容量公式。

## 9. 实读范围、资格结论与停止

本轮恢复实际读取GOAL、STATE、ROADMAP当前入口及registry最新记录，完整R114 next/rough稿，R104–108上述原proof与停止段；本地源text实读Def17.1–17.4、19.2 statement与所需proof段、19.4 statement和concentration/CW proof。没有声重新认证源高级wholeproof、最新官方byte或文献优先权。R107旧canonical图仅承担其总pair计数，本稿不倒填为每point degree lower；§2有界重数图专为避免该误用。

实际支付了两项限定推导：完整grain pencil phase与scalar cap的双向闭包(3.3)，以及S对真实原same-T far-pair相位带的前向(4.3)。前者拒绝改名，后者只说明将来若付S可用哪种原I后果；没有获得R107所缺的clock law或source矛盾。平均good-grain的准确floor与heavy门槛亦已列式，未宣完整污染反例。

资格判定：本稿**不构成独立新正方向**，不把相位运输、平均重述、参数调整或初等计数登记成新数学结果。强∀grain S尚未证明；结合§5锁后整合注，另一主稿已付它在准确γ/规范范围内与完整κ1 source排除的∃小η等强，故拒绝将其登记成更便宜的局部新输入。S对全部ordinary/一般目标的充分性仍未付；原I正质量good-grain版本没有被graft否定或证明。停止本相位类续轮，交root整合真正的新source输入。没有新ordinary/Hausdorff下界、完整κ1 gain、实际全方向低维反例或Goal完成依据；未经外部同行评审，本人推导不算本人独审。
