# R0053：二次secant图、真实方向bin与regular quadric任意密度转移

2026-10-17，B。读固定恢复入口、registry78状态、R53 working_spec与R52 nextgate。以下在具名三维L³ Kakeya maximal输入下证明指定(Q3)；不重证该97页高级输入，不声称一般四维maximal、五维新界、重大性或新颖性，未经外部同行评审。只编辑分配文件，不Git、不另开代理。

## 1. 命题、闭包和旧路线排重

P:R⁴→R为非零次数≤2实多项式，系数abs≤1；有限unit segments ℓ_i⊂{P=0}位于固定有界域，在指定邻域|∇P|≥c>0。T_i是对应半径δ真管，Y_i⊂T_i可测，E=∪Y_i，w_i≥0，W=Σw_i>0。任何半径Cδ的physical S³方向bin中总权≤α。设I=Σw_i|Y_i|，λ=I/Σw_i|T_i|>0。目标为

    |E|≥c_(ε,c) δ^ε λ³ δ³ W/α。                  (Q3)

删管只保α上界，不保W或I；删shading不保λ。本证不均匀化权重、不将平均免费变逐管，也不抹原label。事件分组以实际incidence I计费，所有分组总数固定，不随δ/P/λ变化。

旧DIR/FSD近满密度量词不能直接给任意λ³；CP/PM的正gain等价是不同full-family来源，未有保原方向/质量的quadric嵌入。R50是parameter-linear曲线目标的全参数coherent lift存在性等价，不是本证明的任意shading投影。新3D full maximal确比这些已用nearfull输入多全密度强度；本稿只处理指定exact quadric类，不据名称认证新颖性。

反向闭包也必须说明：任意R³半径δ单位管/原shadingY_i嵌入H={x₄=0}，用R⁴半径2δ的管和Y_i×[−δ,δ]。乘积位于该真4D管中，原angular cap只损固定覆盖常数，λ₄≈λ₃且|E₄|=2δ|E₃|。所以(Q3)直接包含三维同λ³任意平均密度restricted-shading估计。仅此embedding不自动证明endpoint fullL³强型等价；A稿《R0053_primary_density_and_closure_audit》§§7–8已另付完整restricted-to-strong小幂预算，本人实际全文独核通过：归一||f||₃=1后截低δ²与高δ⁻²均只损maximal量O(δ²)，中间O(logδ⁻¹)层给weak level损log³，Hölder cutoff δ^(-2/3)及layercake只再损一个log；全空间用单位管交O(1)个cube及范数立方求和闭合。故(Q3)与具名fullL³在任意小幂损失层面双向等价。本轮是已知强输入的实际几何transfer，不另立独立新路线或数学ID。

## 2. 二次secant全局图引理——消除“有限根但δ-bin失控”的门槛

记P(z)=zᵀHz/2+ℓ·z+b，H实对称。任意z,z′有准确恒等式

    P(z′)−P(z)=1/2[∇P(z)+∇P(z′)]·(z′−z)。        (1)

固定unit e及0<κ<1。对σ=±1，定义

    Z_(e,σ)={z:P(z)=0，σ e·∇P(z)≥κ|∇P(z)|>0}。

写z=u+te、z′=u′+t′e，u,u′∈e⊥。由(1)和两个法向分量同号，

    |t′−t|≤κ^(-1)|u′−u|。                       (2)

因为分母|e·(∇P(z)+∇P(z′))|至少κ(|∇P(z)|+|∇P(z′)|)，而水平项至多(|∇P(z)|+|∇P(z′)|)|u′−u|。因此每个σ类是其投影域上的**全局**κ^(-1)-Lipschitz图，投影单射。域不必连通；无须穿越bad域沿局部根分支作延拓。这一步完全uniform于退化H、微小系数及δ依赖P。

它还给纤维结论：N_(Cδ)(Z_(e,σ))在任一平行e的直线上的交集直径≤C_κδ。若两个点在同一纤维，选其各自距离≤Cδ的真实zero footpoint；其水平差≤2Cδ，由(2)控制footpoint高度差，再付两端Cδ。故纤维长度≤C_κδ，哪怕图域有孔。没有使用“degree2最多两个根”代替这项尺度一致结论。

## 3. 方向cone的全局逆图与原angular cap

exact line a+tv包含于P=0当且仅当

    P(a)=0，(Ha+ℓ)·v=0，vᵀHv=0。                (3)

令h=Hv。先看h≠0的方向。固定e，限制到|π_ev|≥κ和σe·Hv≥κ|Hv|，其中π_e为到e⊥的正交投影。置

    u=π_ev/|π_ev|∈S²，t=(e·v)/|π_ev|，
    z=v/|π_ev|=u+te。

z属于齐次二次q(z)=zᵀHz/2=0，且梯度Hz是Hv的正倍数，同号横截条件保持。对同一σ的两个方向用§2，得到

    |t−t′|≤κ^(-1)|u−u′|，|z−z′|≤C_κ|u−u′|。

再归一化z/|z|=v（|z|≥1），得|v−v′|≤C_κ|u−u′|。所以每个投影S²的δ-bin，其该σ类原方向预像直径≤C_κδ，可由固定个原Cδ-bin覆盖。该组投影方向总权≤C_κα。

这是对全部原positive weights、重复positions/labels都合法的cap，不只cardinality或generic finite-to-one。H很小或秩下降时，两个normal的共同尺度在(2)中取消，没有倒数最小特征值费用。

## 4. 同时选择physical和direction横截的有限kernel

对某条line方向v及其任意footpoint a+tv，令n=∇P(a+tv)。由(3)，n⊥v；h=Hv也⊥v。n≠0由regular假设保证。

h≠0时，将n、h单位化，选±使它们内积非负，再取两者和的unit方向e₀。于是e₀⊥v，且|e₀·n|≥|n|/√2、|e₀·h|≥|h|/√2。取S³一个固定足够细的net，每个e₀有一个net点e仍满足两项≥κ相对横截及|π_ev|≥κ，例如取一个小的固定κ。net数量只依维数，不依P/c/δ。physical sign和direction sign各取±，有限分组。

这里可以直接按原incidence point分组，不必先用c大小切clock并付新质量。对每个x∈T_i，取到原segment的唯一最近点a_i(x)，这是连续的clamped orthogonal projection。按a_i(x)处n、固定h_i，选择第一个合法net kernel及两个sign。与Y_i相交给有限可测事件分割；每个非空组中i的whole direction自动满足§3条件。原Y_i全部保留，包括round endcaps任意小λ的质量。

h=0时必须另论，不能令h/|h|。所有此类v属于

    V=kerH∩ℓ⊥，因为(3)化为ℓ·v=0。

V是proper线性子空间，dimV≤3：H非零时kerH proper；H=0且ℓ=0将P变常数，与有regular zero line不相容。任一physical normalHa+ℓ在V⊥。取S(V⊥)的固定精度有限net，选择e使|e·n|≥κ|n|；e恰在V⊥，故π_e在V上等距，方向bin cap原样保留。再按physical sign分组，§2同样给纤维长度控制。

此singular处理覆盖整个semidefinite情形（vᵀHv=0迫Hv=0）及indefinite退化型的核方向，没有小特征值或漏掉方向质量。

## 5. 原incidence预算、fiber integral与3D输入

记上述有限组数为G=O(1)，原incidence按point事件精确分割。至少一组g有I_g=Σw_i|Y_(i,g)|≥I/G。只保其非空labels，则W_g≤W，原方向cap仍≤α；投影后由§3或§4得到Cα。不能把所有组的whole-tube权重重复后仍声称总权为W，本证只用这个有原incidence下界的组。

设E_g=∪Y_(i,g)⊂E，选定其kernel e。每个Y_(i,g)都距具有该physical sign的真实quadric zero footpoint≤δ，所以§2给E_g每个e-fiber长度≤Cδ。令

    f(u)=δ^(-1)∫_R 1_(E_g)(u+se)ds。

则0≤f≤C、∫f=δ^(-1)|E_g|，从而||f||³_L³≤Cδ^(-1)|E_g|。这里没有把Y填成整条fiber，只对实际union积分。

原T_i投影落在长度≤1、半径Cδ的真实3D tube区域中；用固定数个单位圆柱覆盖，包括端帽。于是对投影direction附近cδ角帽的3D maximal，有

    K_(Cδ)f≥c β_i，β_i=|Y_(i,g)|/δ³。

理由是δ^(-1)|Y_(i,g)|给该投影区域内f积分的lower，sup的固定数圆柱至少捕获固定比例。非短投影由§4保证，投影direction perturbation只增加固定倍半径。平均λ任意小时也不删端点或短时间质量。

调用具名3D L³ maximal（将loss改名为ε/3）并积分原weighted angular caps，得到

    δ² Σw_i β_i³≤Cε αδ^(−ε)||f||³_L³
                 ≤Cε αδ^(−ε−1)|E_g|。

由Jensen，Σw_iβ_i³≥(I_g/δ³)³/W_g²≥(I/(Gδ³))³/W²。又Σw_i|T_i|≈δ³W，所以

    |E|≥|E_g|≥cε δ^(ε+3)λ³W/α。

这完成指定(Q3)，条件仅为所列3D full maximal输入及本稿实际几何。平均与逐管密度没有混换，权重跨度不进常数。可再作合法任意Y restriction，但新λ必须按实际保留incidence重算。

## 6. 两个真非平面模型与一般退化型

P=x₄−x₁x₂时，grad=(-x₂,−x₁,0,1)，自动regular；exactline条件是v₁v₂=0、v₄=a₂v₁+a₁v₂。v₁=0的一支落在x₁=a₁、x₄=a₁x₂的2-plane，v₂=0的另一支对称；不同叶片不是免费同一plane。Hv=0仅给v₁=v₂=0，再由linear条件v₄=0，即v沿e₃。它们正分别进入§3与§4。

P=x₁x₄−x₂x₃时H可逆，故无非零singular direction；gradnorm=|a|，regular patch排开vertex。把坐标视为2×2矩阵，非零rank-one a=u rᵀ、rank-one v=u′r′ᵀ的polar条件等价det(u,u′)det(r,r′)=0，故line属于固定左因子或固定右因子的两类2-plane rulings。root的实际模型无需将这些叶片免费合并：simultaneous kernel及cone逆图统一处理它们。

正定/负定H没有非零null v，族为空；半定型全部在singular V；一般indefinite型将h0与h非0分开即可。没有依赖某一种Witt标准形的有界条件数，故允许P随δ退化，常数仍符合原命题。

## 7. 独立反攻、sharpness与严格未覆盖部分

超平面中的full2维方向bush取共同clock段长度λ（δ≤λ≤c），可使真实四维union至多Cδλ³；W/α≈δ^(−2)，(Q3)右边为δ^(1+ε)λ³量级。因此λ³是自然密度指数，不能无新信息换成更强的λ^p、p<3并保任意ε。更小λ及极不均匀权在§5由原积分和Jensen处理，不靠丢端帽恢复。

near-contained不由本证免费推出：例如P=x₃+x₄²的regular曲面，v=√(1−s²)e₁+se₄、|s|≤√δ的unitlines沿整段满足|P(tv)|≤δ，却并不满足exact q(v)=0。drop e₄时其projected方向全相同，可有δ^(−1/2)个原δ方向。这个投影又不横截physical normal，故不是对(Q3)或所有合法转移的反例；它严格说明只把exact cone identity改成O(δ)并沿用旧bin论证不合法。

高degree没有(1)的二点secant normal恒等式，一般曲面/actual source ruled slices也未满足本class。singular physical points、近切而非exact contained、任意短clock重缩、growing degree和原source质量提取均需另证明，不能从本模型删去。这些未覆盖部分不是(Q3)的缺口。

## 8. 本轮结论与独审责任

本稿给了完整uniform cone graph lemma及指定regular quadric模型的条件证明，核心是二次secant和same-sign分母，而非generic projection的口头有限重数。root/A须独立全文核后才能列internally reviewed；正式review再实际读root/A/macro/next，不以本稿自审计独审。反向hyperplane嵌入及另付的小幂restricted-to-strong预算已表明本模型等价于所用三维完整强输入；不另立同义数学ID。

本结果只是窄几何模型输入，不宣普通R⁵严格>4、full HRZ、高维Kakeya已解或新颖/重大。Goal active；不因exact class可证就不断换degree/λ/regularity小改续轮。spec§6明确追加的同轮近contained抛物柱面检验单列于下节，不把它冒充一般nearquadric转移。

## 9. 同轮近contained抛物柱面：真实空间packet补回原角权

实际读working_spec新增§6后，固定Z={x₄=x₁²}，原unit axes只假设ℓ_i⊂N_(C₀δ)Z∩B(0,10)，不假exact contained。保留§1的所有原权、任意平均λ、angular cap α和实际Y_i。本节证明这一子类的同(Q3)，条件仍仅为具名M3；不推广到一般nearquadric，也不赋新结果ID。

将每轴写成a+tv，|v|=1、t∈[−1/2,1/2]。Z在固定球附近的P=x₄−x₁²有固定Lip常数；距离假设故给整段

    |P(a+tv)|=|a₄−a₁²+(v₄−2a₁v₁)t−v₁²t²|≤C₁δ。

比较t=0,±1/2：两端值之差等于v₄−2a₁v₁，两端和减两倍中心值等于−v₁²/2。因此

    |v₁|≤C₂√δ， |v₄−2a₁v₁|≤C₂δ， |v₄|≤C₃√δ。 (8)

这里的系数比较保整段unit clock，并非在一个单时刻Taylor或删除大部分shading。取δ₀固定足够小，drop-x₄投影π的r_v=|πv|≥1/2。把轴midpoint的a₁按间隔r=√δ的half-open格分包j，中心b_j；一条原轴只归一个包，权与shading不拆。

对该包令u=πv/r_v∈S²，s=v₄/r_v。由(8)与|a₁−b_j|≤r/2，

    |s−2b_j u₁|
      ≤r_v^(-1)(|v₄−2a₁v₁|+2|a₁−b_j||v₁|)
      ≤C₄δ。                                      (9)

同包任意两个投影方向若|u−u′|≤Cδ，则|s−s′|≤2|b_j||u₁−u₁′|+2C₄δ≤C₅δ；b_j有固定绝对界。原方向v=(u,s)/√(1+s²)，归一映射在|(u,s)|≥1上uniform Lip，故|v−v′|≤C₆δ。于是该包每个projected δ帽的原方向预像在一个C₆δ帽中，按固定数原方向帽覆盖后，投影权上界≤C₇α。没有O(δ) exact方向snapping；保角权靠的是每包a₁的r精度与v₁的r上界相乘成δ，不能跨包直接并掉这个标签。

另一方面每T_i∈j的x₁坐标始终落在[b_j−C₈r,b_j+C₈r]：轴运动≤|v₁|/2，管厚多δ≤r，再付midpoint rounding。设E_j为该包原shadings的并集，则

    Σ_j 1_(E_j)(x)≤C₉，故Σ_j|E_j|≤C₉|E|。       (10)

这是实际空间重叠数；不把O(r⁻¹)包数当常数，也不按包数作pigeonhole而损δ^(-1/2)。T_i⊂N_((C₀+1)δ)Z，故在固定球内|x₄−x₁²|≤C₁₀δ。每个E_j的vertical fiber长度≤2C₁₀δ，令f_j=δ⁻¹∫vertical1_Ej，则0≤f_j≤C、||f_j||₃³≤Cδ⁻¹|E_j|。

每包投影仍是原直管的真正3D投影，长度≥1/2；单位圆柱固定数覆盖保住端帽和极小λ。重复§5的原角帽加权积分及M3，记W_j=Σ_(i∈j)w_i、I_j=Σ_(i∈j)w_i|Y_i|，得

    |E_j|≥c_ε δ^(3+ε) α⁻¹ (I_j/δ³)³/W_j²。       (11)

空权包跳过。所有原labels和完整Y_i仅归一包，所以ΣW_j=W、ΣI_j=I。weighted Hölder给

    Σ_j I_j³/W_j²≥(Σ_jI_j)³/(Σ_jW_j)²=I³/W²。

将(11)求和并用(10)，得到|E|≥c_ε δ^(ε−6)I³/(αW²)≥c_ε δ^(3+ε)λ³W/α，即近contained抛物柱面子类的(Q3)。无逐管heavy、等权化、包数、方向去重或独立prior损失。

反攻边界：(9)使用的是该固定二次柱面的实际系数；一般quadric并无已付的单坐标a₁ packet或(10)空间重叠界。更粗a₁包会令角误差大于δ，更细包若仍直接求和可能有非固定overlap。非零管厚、round endcaps和任意碎shading均已在(8)–(11)内支付；此前√δ exact-snapping失败未被否定，而是以不同packet机制绕过。这是同一几何任务的一个真实近contained子类转移，不是普通R⁵界或一般variety/HRZ闭包，也不声称独立新颖性。
