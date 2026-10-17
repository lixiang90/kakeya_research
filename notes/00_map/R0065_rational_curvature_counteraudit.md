# R0065：有理双时间曲率、原离散质量与双曲线反攻

2026-10-18，B。实际读R65先写spec（含§5双chart补充）、macro、GOAL／STATE／ROADMAP／registry78及R64next。仅编辑assigned文件，无Git／spawn。以下给有限命题的独立证明与具体反攻，不把固定有理格式授给原WZ source；未经外部同行评审，不声ordinary高维增益、首创或major。符号计算只辅助展开，§7的因式恒等式另有直接推导。

## 1. 命题、原law与最先需保的范围

固定D、M、C0，0<r<1，0<γ≤1，0<κ≤2，0<θ<min(1/6,κ/6)。原time概率ν1、ν2支持固定intervals I1、I2⊂[−1,1]，每interval满足νi(I)≤K(|I|+r)，K≥1。原标签概率π保留重复labels，ψ=ψ(ω)∈R²、|ψ|≤M，任意width w≥r的slab有π质量≤K w^γ；σ为任意输入y概率。各参考的乘积是σ×ν1×ν2×π，g∈[0,1]可任意相关，不独立化g。

两chart Fi=Pi/Qi，degree≤D、coeff≤M，相关interval及其O(r)邻域有|Qi|≥1/(2M)。原spec单F为特例；区间内|Qi|≥1/M配固定degree／coeff可保证足够小r时上述邻域性质。令

    Tψ(t,s)=(t−s)(F1(t)−F2(s))ψ，
    Jψ(t,s)=det(∂tTψ,∂sTψ)=N(t,s;ψ)/(Q1(t)³Q2(s)³)。

N的time总degree≤d=6D+4，关于ψ为齐次二次。假设某个time monomial系数q(ψ)的coefficient maxnorm≥r^θ。A+有≤K r^(−2+κ)个r-ball覆盖，且g>0只在dist(y+Tψ,A+)≤C0r发生。以下独证

    ∫g ≤ C[D,M,C0] {K r^(θγ/2)
                    +K² r^(θ/(2d))+K³ r^(κ−3θ)}。       (1)

常数不依原标签数、time atoms、g的相关性、A+的位置及各权跨度。参数r不够小时调固定常数即可，右边第一项已由固定r下界控制1。双chart各自原prior不需要条件化成uniform Lebesgue，也不需要interval AD lower。

## 2. 齐次二次角小值集确由至多两条slab控制

设q(ψ)=ψᵀHψ，H实对称，coefficient maxnorm≥ℓ。某eigenvalue绝对值≥cℓ。乘整体符号、作正交变换后写q=A x²+B y²，A≥cℓ且|B|≤A。若B≥0，|q|≤τ迫|x|≤(τ/A)^(1/2)。若B<0，分解

    q=(√A x−√(−B)y)(√A x+√(−B)y)。

两factor的法向长度均≥√A，乘积绝对值≤τ则至少一factor绝对值≤√τ。因此小值集包含至多两条width C√(τ/ℓ)的slab。没有把π换成二维面积或要求H非退化。

取τ=r^(2θ)、ℓ≥r^θ，删角事件Ωbad={|q(ψ)|≤r^(2θ)}，原质量

    π(Ωbad)≤C K r^(θγ/2)。                    (2)

所查询width C r^(θ/2)≥r，恰在原slab假设范围；C^γ由γ≤1统一吸收。其余每个原label的N至少有一个time系数绝对值≥r^(2θ)。π不去重，(2)直接在原labels上收费。

## 3. 二维polynomial小值集：两次一元插值及原ν-smearing

一元degree≤d多项式p若某coefficient绝对值≥A，则固定bounded interval上

    |{x:|p(x)|≤b}| ≤ C_d (b/A)^(1/d)，          (3)

右边≥常数时取平凡界。证明可在小值集长度L中按quantiles取d+1点，点间距≥c_d L；Lagrange插值得全部coeff≤C_d b L^(−d)，反解即得(3)。degree0用同一平凡分支。无需导数先有lower。

若二维P有一coeff≥A，写P(t,s)=Σ_i p_i(s)t^i并选含该coeff的p_i。删|p_i(s)|≤√(Ab)的s集合，用(3)付C_d(b/A)^(1/(2d))；其余s再对t用(3)，亦付同指数。故

    |{(t,s)∈[−2,2]²:|P(t,s)|≤b}|
       ≤C_d(b/A)^(1/(2d))。                   (4)

这比可用的更强多元Remez指数保守，但已足目标。

原νi与Uniform[−r,r]卷积得ν̃i，密度≤νi([x−r,x+r])/(2r)≤3K/2。Fi、Tψ、Jψ、N在相关固定小扩展上所有此次使用的导数由D、M统一控制。因ψ bounded，|N(t+u,s+v)−N(t,s)|≤Cr。取j0=r^(3θ)。原坏time事件|Jψ|≤j0的每个r-smear点满足|N|≤C(j0+r)≤C′r^(3θ)。余角的N-coeff≥r^(2θ)，(4)给

    (ν1×ν2){|Jψ|≤j0}≤C K² r^(θ/(2d))。        (5)

这里是将原坏点全部smear入增厚的小值集后用ν̃1ν̃2的density上界，不是把原atomic law宣称有Lebesgue density。θ<1/6给r≪r^(3θ)，所需小r常数可统一由1−3θ>1/2支付。

## 4. good-J、真实g-smearing与regular fiber重数

先保原角good、原|Jψ|>j0的g。对每个保留tuple仅time两坐标独立加Uniform[−r,r]噪声，保留其原权；得到同质量的smear submeasure。对每固定y、ψ，其density≤C K²，因为原g≤1。每个像点满足

    |Jψ(t′,s′)|≥j0/2，
    dist(y+Tψ(t′,s′),A+)≤C′r。                (6)

这保留了g与输入、time和angle的所有相关性，只给其time条件submeasure做domination；不声smear后的g重新为独立乘积。

固定ψ、输出z。方程Tψ=z清分母成为两条degree≤2D+1多项式方程。J≠0的解是regular isolated解。Bézout给其个数≤(2D+1)²：即便某fiber另有共同curve component，component上不可能有rank2；也可任取有限多个regular解的小邻域，作共同generic输出微扰保留这些解，再应用无共同component的Bézout界。因此regular fiber multiplicity只依D，不依δ、ψ或z。这里只用有限degree交点界，未用source的代数复杂度假设。

面积公式在good部分给任意可测输出B

    |{(t,s):|Jψ|≥j0/2, Tψ(t,s)∈B}|
       ≤C_D j0^(−1)|B|。                    (7)

A+的C′r邻域面积≤C K r^κ，平移y不改面积。将(6)(7)与smear density合并，保留g质量≤C K³ r^(κ−3θ)。再加(2)(5)即(1)。不把Jac积分下界当union面积，也不假全fiber有限；只在regular部分使用重数。

## 5. 参数、原mass及restriction的实际含义

例如取固定θ后，h<min(θγ/8,θ/(12d),(κ−3θ)/8)，K≤r^(−h)时(1)右边为o(r^h)，所以不能同时有原∫g≥r^h。更精确指数不是本轮目标，不续阈值。

限制原g／shading仍由同product reference支配，故(1)对所有这种限制统一成立。若另外条件化time或angle，须以保留probability归一并重付interval／slab常数，不能原样保K或AD lower。若σ／π不是概率，须先归一或明确乘总质量。本命题只需A+覆盖，不需A−cardinality；因而它确实使用了R64反例缺失的低维原output条件。

O(r)的原F近似可在bounded原time、ψ单位下吸入C0；若原normal或clock另缩放，须如R64付s_t s_F/s_y。固定D、M、denominator lower及量化N-coeff均是额外输入，不由dyadicLip、SM、原AD4／CW自动获得。

## 6. pencil／image／angle零线及time atoms反攻

F=F0+h(t)M时，每个固定ψ的T总沿Mψ的一条线，故J恒0，纵使M可逆；F=F0+v r(t)ᵀ时亦沿固定image v，N恒0。这些不是(1)的反例，而是明确违反曲率前提。common-kernel F=F0+u(t)eᵀ则未必退化，u二维曲率仍可给J≠0，不能仅凭matrix rank-one就否曲率。

π全在某q=0方向线、或ψ=0时，可让N全退化；但固定K、固定γ>0的slab cap在width r只许该线有≤K r^γ质量，不能把方向atom免费加入。若K随r大到r^(−γ)，(1)不再提供小质量矛盾，正是应付费用。

时间单个atom可重K r，ν=δ_t0需要K≳r^(−1)，亦使目标界不小。一般finite ν atoms由§3合法smearing处理，不需偷加连续或non-atomic假设。F近常但N-coeff低于r^θ时同样不能套定理；没有靠清分母伪造N下界，Q有统一上下控制是必要的格式约束。

## 7. R64双branch双曲线的J恒等式与非零系数

保R64固定c=1/8，t∈I−=[−1,−1/2]、s∈I+=[1/2,1]；ν可取原δ-grid（端点取半开不影响）。令

    u=2t+3∈[1,2]，v=2s∈[1,2]，p=ψ1，q=ψ2，
    F−=c diag(u,u⁻¹)， F+=c [[0,v],[v⁻¹,0]]，
    d0=u−v−3， A=up−vq， B=2pu²−3pu−2qv²−3qv。

则cross矩形精确有

    T=(c/2)d0 A (1,−1/(uv))，
    J=c² A d0 B/(u²v²)，
    N=u³v³J=c²uv A d0 B。                    (8)

直接核法：记X=(c/2)d0 A，Y=−X/(uv)。

    det(∂uT,∂vT)=X(u X_u−v X_v)/(u²v²)，
    u X_u−v X_v=(c/2)B。

再乘du/dt·dv/ds=4即得(8)。因此不是以符号软件输出代证明。展开只需观察N中u⁵v的p²系数为2c²，其余terms不能贡献t⁵s；代u=2t+3、v=2s得

    [t⁵s]N=128c² p²=2p²。                   (9)

量化非零系数为固定正量，D=2、M取固定足大即可。两个Fi各在其固定chart有P/Q，不能把它们误称同一个全域rational F；spec§5矩形版正好覆盖。反向cross矩形由交换t、s及labels同样处理，只固定倍费用。

此domain |d0|≥2且u、v≥1，critical集合恰A=0或B=0。ψ≠0时两者均为非零多项式；ψ=0由角删除收费。删near-critical必须按§2–4原prior收费，不能直接宣raw整个推前二维Frostman。R64原g只取cross，mass1/2；若再有本轮A+／K／γ及小h条件，则两个cross矩形各由(1)排除其固定质量A-output补全。这个结论不需要其raw独立pair det差非退化，恰是与R64edge-only分类不同的信息。

## 8. 真difference-angle law下raw零点小球仍可有一维质量

这个校准说明§4good-J删除绝不可略。取H=Uniform([0,3]²)，原labels为独立(H1,H2)、ψ=H1−H2。π在[−3,3]²有密度

    fπ(p,q)=(3−|p|)(3−|q|)/81，

并保任意方向的slab exponent1、常数固定；[1,1.8]²上density有固定正lower。取原νδ在R64两branch上的uniform δ-grid，u、v限制[1.2,1.4]，仍保固定time质量。p∈[1.2,1.4]时q*=up/v在[1.028,1.634]，故|q−q*|≤c₁r的小条带落于[1,1.8]²且π质量≥c₂r。

条带上|A|=v|q−q*|≤Cr，(8)迫|T|≤C′r。因此对δ≤r、δ足小，原νδ²×π的cross推前满足

    Pr{|T|≤C′r}≥c r。                       (10)

它排除原whole raw output law的uniform二维ball upper C r²，虽然π确为真正difference law，ν是真1AD网且(9)非退化。这不是固定ψ原子或单critical point的虚假反例；恰是正质量time和angle纤维上靠近A=0的原质量。H本身为二维，未声κ<1的全部source angle AD。这里只校准“整law2Fst”的错误升级，不反good-J推前、不反(1)，更不反Kakeya。

## 9. 独立结论及待全文交审边界

有限有理命题在原离散／weighted product reference、任意相关g下可完整证明；§§2–4给所有指数及smearing／regular-fiber责任。R64cross双曲线确满足双chart量化曲率，其低维A-output补全在相应small-loss参数下被排；同时(10)严禁将结论扩成整raw推前2Fst。原source的固定格式／非零N输入未提取，原wholeT／xi／AD4／CW仍不能由这些模型代替。

本稿已由A实际逐式独审通过，作者自证不计独审。B另已fresh全文读root14／A10／spec5／macro6／next6及Tao具名输入范围记录，数学及范围无强制修复项；具体正式结论见research/reviews/R0065_discrete_curvature_and_counterexample_review.md。无新数学ID、无ordinary n≥5或general界、无major／首创认证，Goal active。终稿后停止degree、θ、near-critical阈值及其它数学施工，交root统一整合归档。
