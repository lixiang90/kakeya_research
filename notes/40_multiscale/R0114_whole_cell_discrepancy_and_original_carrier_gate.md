# R0114：整δ格随机筛选、原质量与固定格式实体载体

2026-10-26，root。此为任意原平均shading类的closure测试。条件smallfootprint若存在可保留，不是构造了未解范围反例；无ordinary维数改善、major或优先权声明，未经外部同行评审。主working记录了精确量词。

## 1. 一个与几何无关的整格discrepancy引理

固定有界盒B⊂R^n、边长δ的半开格，令Q_1,...,Q_K为与B相交的格（K<=C_Bδ^−n，δ<=1）。所有积分可将g零延到这些格。H_{s,D}由至多s个degree<=D实多项式的符号作Boolean组合给出；等号也允许，系数任意。

给非负g∈L1(B)，w_j=∫Qj g。独立ξ_j∈{0,1}，P(ξ_j=1)=p，0<p<1，M_ξ=union_{ξj=1}Qj。断言

    E sup_(H∈H_{s,D}) |∫g1_H(1_Mξ−p)|
       <= C_(n,s,D) sqrt[log(2K) Σ_j w_j²].             (1)

这只是绝对误差，不是相对∫_H g误差。由于ξ只有2^K个可能值，外层随机变量可逐值定义为确定实数sup，因此可测；以下内层采样需要处理的sup亦见第3节。

## 2. 固定点云上的格式计数与随机最大值

degree<=D的多项式有b=binom(n+D,n)个系数。在任意K点上，其取值是这b个系数的线性函数；系数空间的K个hyperplanes把它分为至多C_b(2K)^b种三值符号（包含0）。理由：超平面arrangement的所有维faces数满足F(K,b)<=F(K−1,b)+2F(K−1,b−1)，退化只减少，归纳得Σ_(j<=b)2^j binom(K,j)。也可在所用span中降维，不假general position。

s个多项式的符号patterns至多C(2K)^(sb)。对每个固定符号tuple，任意Boolean选择至多2^(3^s)种，故所有membership patterns≤C_s(2K)^(sb)。B的固定格式intersection只改变常数；要包括H=R^n可用常数多项式。

固定点云u_j及weights w_j，令P为其有限membership patterns。对每A∈P，Z_A=Σ_j(ξ_j−p)w_j1_A(j)是独立零均值有界随机和，Hoeffding的exponential moment由区间长度w_j给

    E exp(t Z_A) <= exp(t² Σ_j w_j²/8).

同时计±Z_A，log-sum-exp加Jensen给

    E max_A |Z_A| <= C sqrt[Σ_jw_j² log(2|P|)]
                    <= C_(n,s,D) sqrt[Σ_jw_j² log(2K)].    (2)

该步不需p下界，未声最优p方差；本轮p会先固定。

## 3. 每cell积分：Jensen没有产生boundary误差

对w_j>0，在Qj内按概率g(x)dx/w_j选独立U_j；零质量格略去。对每份ξ，

    ∫g1_H(1_Mξ−p) = E_U Σ_j(ξ_j−p)w_j1_H(U_j).

所以sup绝对值<=E_U sup_H|Σ(ξ−p)w_j1_H(U_j)|。交换有限ξ平均和U积分，再用对每个点云成立的(2)，即(1)。不需要H边界与grid横截，也没有额外O(δ)体积误差。

严谨的可测性处理：H可用有限维实系数及有限Boolean式参数化；对Borel非负g，积分与采样test都是Borel参数函数。sup的strict上水平集为analytic投影，故对有限Radon产品概率的completion可测；boundedness<=Σw_j使积分合法。若原g仅Lebesgue可测，先取Borel代表；所有integrals仅依a.e.类。也可全程用outer expectation，上界(2)不变。本证不把uncountable sup默作Borel。

## 4. 同一份mask同时筛体积和原incidence

设A⊂B可测、V=|A|>0，g=f1_A，a<=f<2a在A，a>0，J_A=∫A f，故aV<=J_A<=2aV。用(1)分别对1_A、g，且

    Σ(∫Qj 1_A)² <= δ^n V,
    Σ(∫Qj g)² <= (2aδ^n)J_A <=4a²δ^n V.

定义两个sup分别除V、aV后的和。其期望<=C sqrt(δ^n log(2K)/V)。因此存在**同一份**ξ，使两个sup分别满足

    sup_H ||A∩M∩H|−p|A∩H|| <= rV,
    sup_H |∫_(A∩M∩H)f−p∫_(A∩H)f| <= raV,
    r=C_(n,s,D) sqrt[δ^n log(2K)/V].                    (3)

这是存在于所有2^K份mask中的一次选择，不按H或按管另重选。取H=R^n，若r<=p/4，则E'=A∩M、I'=∫E'f满足

    |E'| <=(p+r)V <=5pV/4,
    I'>=pJ_A−raV >=3pJ_A/4.                          (4)

若需与另一个概率趋1事件联合，可在r的常数中再吸收4倍，由Markov令(3)两个sup之和的控制事件概率至少3/4；(4)的代数不变。第7节的可选逐管mask陈述采用这一版本。

## 5. 同体积fixed-format实体carrier的严格压力

固定C>=1、0<θ<1。先取0<p<=θ/(16C)，然后要求δ或V使r<=θp/8。对任意H∈H_{s,D}且|H|<=C|E'|，由(3)、f<2a及(4)，

    I'(H) <= p∫_(A∩H) f + raV
           <=2ap|H|+raV
           <=(5/2)aCp²V+raV.

又I'>=3paV/4，所以

    I'(H)/I' <= (10/3)Cp+(4/3)r/p
                <=4Cp+2r/p < θ.                     (5)

由此，原marks可在只花固定p原层质量时，变得不能被任何指定固定格式、体积<=C|E'|的实体H捕获θ比例incidence。不是说E'没有任何结构，也不是说其whole supporting axes无代数载体。

## 6. 真正返回原真实管、smallfootprint和密度

现在取任意N根真实单位δ管T_i⊂B、各自可测Y_i⊂T_i，f=Σ_i1_Yi、E=union Yi、I=Σ|Yi|。用dyadic层A={a<=f<2a}（a为2的非负整数幂），层数L0<=1+ceil(log2 N)，选一层使J_A>=I/L0。显然f<=N，因而

    V>=J_A/(2N)>=I/(2NL0).

以I=λNδ^(n−1)、λ>=δ^η、0<η<1，得

    V/δ^n >= λ/(2δL0),
    r² <= C δ L0 log(2K)/λ ->0                     (6)

若N<=Cδ^(−(n−1))。所以每个固定n,s,D,C,θ,p及η<1，在δ足够小时确能用第5节。取Y_i'=Yi∩A∩M，E'=A∩M（a.e.），Σ1_Yi'=f1_E'，于是

    I'>=3pI/(4L0),   |E'|<=5p|A|/4<=5p|E|/4,

且(5)对全部H同时成立。N、原轴、方向、角帽、共同clock、真实marks来源均不改。若原E满足某smallfootprint upper，E'⊂E继续满足；这是**对任何已有原配置的合法变换**，没有凭空构造未解范围的小footprint full-direction例。

平均密度按原N为λ_new=I'/(Nδ^(n−1))>=cpλ/L0。对任意η'>η，δ足够小可得λ_new>=δ^η'；不能声原同一个η门槛逐字不变。各Y_i'可为空，故本命题不自动保每管density、AD lower、point pencil下界、filled X或selectedξ。保管q/保原I比例p_I时一般公式仍λ'=(p_I/q)λ，归一方向cap除q。

mask M是wholeδ-cells的并。若原shadings和管模型以同grid完整cells给出，则f层A及Y_i'仍是同δ-cell类，未用subδ孔洞。对一般round管marks，A未必格并，但只是其真实子集，不被填成格；所有Y_i'仍在原round管内。fixed mesh/tube宽度常数不从该概率论证授予额外几何。

## 7. 逐管删选、量词边界和HRZ隔离

只做mask而不做layer时，有限tube的每个g_i=1_Yi也可用同类独立和控制。cell权<=δ^n，故

    P(|∫Yi 1_M−p|Yi||>p|Yi|/4)
       <=2 exp[−c p² |Yi|/δ^n].

若每管|Yi|>=δ^ηδ^(n−1)、η<1且N是多项式量级，union bound使同一mask逐管保3p/4比例的事件概率趋1，可与第4节的正概率事件联合（把存在常数放大）。**这不让layer+mask得到逐管保留**：原layer可能已删光某些管。主载体压力声明始终是平均类，未偷换。

此外C,s,D先固定再选p和δ。本证明不否C依新λ_new任意恶化（如C≈1/p或更大）的carrier，也不无条件覆盖随δ增长的degree/格式预算；如要扩展须重新比较(2)/(6)，不本轮续参数。它不否HRZ实际nested polynomial partition、whole-axis near-variety、PW/CW upper或付费的多个carrier之和。这些流程没有承诺对每个合法任意marks给**同体积固定格式实体H捕获固定比例I**。只能拒该literal自动初始化，不能由此宣HRZ反例。

尤其要区分无条件carrier规则与smallfootprint反设内的条件规则。对所有任意平均marks无条件声此fixedC规则，会被上述实际筛后原族反驳；但若规则只对尚未证明存在的power-small族声称，则不能从本稿说其为假。下面给其准确逻辑强度。

固定一个小footprint幂β>0和饱和N≈δ^(−(n−1))的原类。假设存在固定s,D,C,θ、某η∈(0,1)及δ0，使每个λ>=δ^η、|E|<=δ^β的原平均shading实例均有上述carrier。若在任意小δ存在λ>=δ^(η/2)、|E|<=δ^β的实例，则按第6节筛得λ_new>=cpδ^(η/2)/L0>=δ^η、E'⊂E；原N/方向仍饱和。于是新实例仍可调用所假定carrier规则，却与(5)矛盾。因此该条件规则本身已排掉这些小footprint实例（η换成η/2）。反过来，若某个η的这些实例根本不存在，同条件carrier规则当然真空成立。按‘先输出幂、再存在足够小输入η’的finite正幂量词，两者具有相同的排除强度；**本稿没有证明任一者成立**。

## 8. 排重与完整目标

R101是原native细见证关系的编码、产品分母及完整witness box质量上界，消费原AD/tubeKT；这里对任意物理Lebesgue shading，按wholeδ-cell的随机法同时控全部fixed-format实体H。不是把该source witness命题改名，也不由R101全称重调用给出。但当前推导是经典signpattern/随机取样的初等后果，不认证新颖、重大或新ID。

本轮因此实质厘清一条初始化捷径的责任：任意平均marks的无条件fixedC规则已被反攻；smallfootprint反设内的同一规则，在合法density余量下已承担欲证finite排除强度，不能列作免费预处理。ordinary高维增益仍需新的真实几何约束；完整rough/mixed源也不能用本mask自动保所有下界。主Goal没有完成。独立逐步review另存，不以此自证或档案check代替。
