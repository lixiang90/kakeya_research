# R0053：regular quadric 的统一转移与三维 maximal 等价

2026-10-17，root。证明条件于明确的三维 L³ Kakeya maximal 具名输入 M3。以下支付真正非平面几何、全部退化 Hessian 和原平均密度；不认证来源97页全proof。完整Q3在任意小幂损失层面与M3等价，因此不另立新数学ID、不称新高维增益/重大成果。未经外部同行评审。

## 1. 命题、量词和具名输入

记 P(z)=d+b·z+(1/2)zᵀAz，A实对称，degree≤2、原多项式系数abs≤1，P非零。固定c>0，有限真正单位线段ℓ_i⊂{P=0}∩B(0,10)，其上|∇P|≥c；原spec要求固定邻域regular，故满足这里较弱条件。T_i为半径δ的4D单位管，固定tube形状下|T_i|≍δ³。Y_i⊂T_i可测，E=∪Y_i。原非负权w_i，总W>0；每半径C0δ的physical方向球总权≤α。所有常数可依c、ε及固定geometry，不依P、δ、λ、族数、权或Hessian非零奇异值。

定义原incidence I=Σw_i|Y_i|，原平均λ=I/(Σw_i|T_i|)>0。Q3为

    |E| ≥ c_(ε,c) δ^ε λ³ δ³ W/α.                     (Q3)

M3为官方3D companion Theorem1.1：K_r按真正单位半径r圆柱的πr²平均定义，∀η>0，||K_r f||_(L³(S²))≤Cη r^−η ||f||_(L³(R³))。本轮实际重读原statement/归一及§10.2接口；官方当前tree/blob另核。正向只调用M3，不用曲线phase、Nikodym或不合格§11变换。

## 2. 先核restriction、原质量及双向强度

删管只保原方向cap上界，不保W或I；删shading只保包含关系，不保λ。下面仅作固定有限事件覆盖，每组W_j≤W、α_j≤Cα，并先保Σ_j I_j≥I，再选I_j≥I/J；不会把平均λ当每管下界。逐管原密度若有则是特殊情形，不反推删后逐管密度。权从始至终保原w_i，重合管/方向不会去重冒充质量。

DIR/FSDnearfull只适用于λ≥δ^η(ε)，不能直接给所有λ³；CP/PM及R50lift未提供这里的physical hypersurface模型与原cap。但Q3含超平面子例，§9完整反推M3；因此逻辑强度并未超出新具名输入。全模型成立只登记为该输入的已付几何应用，关闭exact quadric任务，不以新名开独立结果。R4/R5一般近切族不自动属于exact-contained类。

## 3. 管内基本几何与有限共同kernel

系数有界且管在固定球内，有绝对L使||A||≤L、|∇P(z)|≤L。每z∈T_i距其轴点≤Cδ，故

    |P(z)|≤C1δ， |∇P(z)|≥c/2                         (1)

当δ≤c/(C L)时成立，端帽也只改C。令n(z)=Az+b，h_i=Av_i，其中v_i是原轴的单位physical方向。整段在P0精确给

    P(a_i)=0， n(a_i)·v_i=0， v_iᵀAv_i=0.             (2)

在h_i≠0时取unit n̂(z)、ĥ_i。对任意两个unit向量，选择其和或差并归一，能使与二者的绝对内积均≥1/√2。固定足够细的有限S³ net，某个e满足二者内积abs均≥κ（例如κ=1/4）。无需n(z)精确垂直v_i。由h_i⊥v_i及|e·h_i|≥κ|h_i|，还得|π_e v_i|≥κ，其中π_e正交投影到e⊥。

该kernel net固定有限，与P、δ无关。下文按e和directional sign分管，再按physical derivative sign分原事件；无需先以短clock删原质量，也不需把一整根轴的normal冻结。

## 4. 二次割线恒等式支付全局方向逆

固定e，q(w)=wᵀAw。两个q-zero写w=u+te、w'=u'+t'e，假定Aw、Aw'非零且同号条件

    σ e·Aw≥κ|Aw|， σ e·Aw'≥κ|Aw'|。

精确恒等式 q(w')−q(w)=(Aw'+Aw)·(w'−w) 给

    |t'−t|≤κ^−1|u'−u|.                              (3)

因为分母abs≥κ(|Aw|+|Aw'|)，分子≤(|Aw|+|Aw'|)|u'−u|。没有除以任何最小非零特征值，也没有仅用“每纤维至多2根”偷推小球重数。

对unit v，取r=|π_ev|≥κ、w=v/r，则u=π_ev/r∈S²、|t|≤κ^−1。q(w)=0，relative normal/sign条件在正缩放下保留。由(3)及归一映射在|w|≥1上的2-Lipschitz界，

    |v−v'|≤Cκ |u−u'|.                               (4)

所以每一个同e/同σ组的投影方向O(δ)球，原方向全在一个Oκ(δ)球内，可用固定数C0δ球覆盖。其总原权≤Cκ α。域可不连通，不需要沿域连路径；(3)是任意两点的全局secant界。Hessian可随δ任意退化，仍无条件数费用。

## 5. singular direction 并非丢弃项

令V=ker A∩b⊥。若h_i=0，(2)给v_i∈V；而对每个z，n(z)=Az+b∈V⊥。P非零且存在regular轴时V≠R4，所以dimV≤3；V0没有unit singular方向，忽略空族即可。

取V⊥单位球的固定精度有限net，数目有绝对上界但可随P旋转。对每个z∈Y_i有某个e∈V⊥满足|e·n(z)|≥κ|n(z)|。投影π_e在V上等距，故投影direction cap保原α，且|π_ev_i|=1。三维M3旋转不变，允许该有限kernel随P变化而不引入条件数常数。

线性P、半正定A只有kernel方向、A极小等均被此分支或§4覆盖。不是预设Hessian非退化后遗漏奇方向。

## 6. 可测事件覆盖及统一物理纤维界

非奇组以j=(e,σ,τ)编号：管满足σ e·Av_i≥κ|Av_i|>0，事件取

    Y_(i,j)=Y_i∩{τ e·∇P≥κc/2}， E_j=∪_iY_(i,j).

奇组以e∈V⊥ net和τ编号，取对应奇管及同样的physical事件。由§3/§5，原每个事件至少属于一组，故Σ_j I_j≥I，其中I_j=Σ_(i∈group)w_i|Y_(i,j)|。组数J固定有限；W_j≤W，投影角cap≤Cα。选择I_j≥I/J的一组，必W_j>0。重叠覆盖只付固定J，不需要选择覆盖的可测nearest-footpoint；多项式阈值和有限union已保证可测。

固定u∈e⊥、两个fiber点z=u+te、z'=u+t'e∈E_j。由(1)，|P(z)|,|P(z')|≤C1δ，且同τ的∂_eP均≥κc/2。二次的精确割线恒等式为

    P(z')−P(z)=(t'−t)[∂_eP(z')+∂_eP(z)]/2。

所以该fiber中任意两点距离≤4C1δ/(κc)。fiber的Lebesgue长度不大于其直径，即使shading极碎也成立。因此

    f_j(u)=δ^−1 ∫_R 1_(E_j)(u+te)dt

可测，0≤f_j≤C_c，且∫f_j=δ^−1|E_j|，故∫f_j³≤C_c² δ^−1|E_j|。不能用未切normal区域的global E代替E_j，那会破坏这个L∞界。

## 7. 真投影管、邻角帽与原加权立方

π_eY_(i,j)包含于原4D管的3D投影。原轴投影仍是直线、长度≤1，|π_ev_i|≥κ；投影管含于固定数单位C2δ圆柱的并。对每个半径c2δ内的邻近方向ω，同样用固定数单位C3δ圆柱覆盖，端点/端帽/角扰动都只改C3。

Fubini给投影包围区域上的∫f_j≥δ^−1|Y_(i,j)|。于是对该整角帽

    K_(C3δ) f_j(ω) ≥ c ρ_i， ρ_i=|Y_(i,j)|/δ³.        (5)

这是单位圆柱归一化，不能把短投影轴的平均免费当单位平均。固定数覆盖已支付损失，不使用未核的曲线直化。

角帽面积≍δ²，重叠权≤Cα。将(5)立方、乘原w_i并积分，调用M3时取η=ε/3，得到

    δ² Σw_iρ_i³ ≤ Cα ∫(K_(C3δ)f_j)³
                 ≤ Cε α δ^−ε ∫f_j³
                 ≤ Cε,c α δ^(−1−ε)|E_j|。

故

    |E_j|≥cε,c δ^(3+ε) α^−1 Σw_iρ_i³.                (6)

零shading管可保原权，它们只使后续Jensen的W_j偏大，安全。无需δ-separated directions、去重或heavy到逐管λ。

## 8. 原平均密度闭合与实际非平面模型

加权Jensen为Σw_iρ_i³≥(Σw_iρ_i)³/W_j²=(I_j/δ³)³/W_j²。用I_j≥I/J、W_j≤W和I=λΣw_i|T_i|≥cλδ³W，(6)给

    |E|≥|E_j|≥cε,c δ^(3+ε) α^−1
                    (I/(Jδ³))³/W²
                ≥cε,c δ^ε λ³δ³W/α。

这证明全部声明的Q3，所有退化P、原非均匀权和任意平均λ均包括。没有把I_j/W_j误等于原λ，也未用未证的subfamily质量下界。

非平面校准一：P=x4−x1x2。真实line条件为v1v2=0、v4=a1v2+a2v1；v1=0时轴在{x1=a1,x4=a1x2}的2D平面内，v2=0同理。公共x3方向属于singular分支；不是把整个曲面当固定hyperplane。

非平面校准二：P=x1x4−x2x3。rank-one矩阵M(a)和M(v)的整段rank1条件，除P(a)=P(v)=0外还需mixed determinant为0；在regular非零M(a)处，等价于二者共享左因子或右因子。它有两类2D平面ruling，方向cone非线性且Hessian满rank，§4而非§5处理。一般proof不要求从这些例子猜测全分类。

超平面bush显示λ³不能统一改为λ^p、p<3：取3D方向δ-net，W/α≍δ^−2，原shading是共同初始λ时段的4D tube部分，δ≤λ≤1时union≤Cλ³δ；若λ=δ^a，任意ε小于a(3−p)将与改进式冲突。此只是模型的密度校准，不是欧氏Kakeya反例。

## 9. 完整双向：Q3反推三维M3的任意小幂

先在R3固定单位cube内取任意可测F。对level set {Kδ1_F>λ}取最大δ-separated方向集，N个；每方向选单位管使|F∩T_i|≥(λ/2)|T_i|。这些管若交F便位于固定球内。嵌入H={x4=0}，4D半径2δ管包含Y_i=(F∩T_i)×[−δ,δ]；原方向帽权α=O(1)，平均4D密度≥cλ，|∪Y_i|≤2δ|F|。Q3给

    σ{Kδ1_F>λ} ≤ Cη δ^−η λ^−3 |F|, 0<λ≤1.            (7)

packing/covering使level面积≤Cδ²N；fixed-radius变化只改常数。嵌入用P=x4、c=1，完全合法，不免费嵌入一般R4族。

这里还支付restricted→strong，而非凭一句standard宣称endpoint。局部f≥0且||f||3=1。删f≤δ²，K的贡献≤δ²；删f>δ^−2，∫f_high≤δ⁴，所以Kf_high≤Cδ²。中间分Jδ=O(logδ^−1)个dyadic层2^k1_Fk，Σ2^(3k)|F_k|≤C。pigeonhole与(7)给中间函数的level上界Cη δ^−η Jδ³ t^−3。另Hölder直接给Kf≤Cδ^−2/3。以layercake积分t∈[Cδ²,Cδ^−2/3]，只增一个log，故

    ||Kδf||3³ ≤ Cη δ^−η (1+logδ^−1)^4。

η可任意小，log吸收到更小幂，得到任意ε的M3。全空间按单位cube分f_k；一根单位tube只交绝对常数个cube，所以Kf≤C sup_k Kf_k，立方范数和≤CΣ||Kf_k||3³，输入cube范数³也可加。这付清global范围。可先截断/近似处理无限层及一般L³，单调性保持所有估计。

Q3只需小δ；剩余δ≥δ0(ε)直接由Hölder的Kδf≤Cδ^−2/3||f||3吸入依ε的常数。因此M3⇒Q3且Q3⇒M3（每次允许任意小幂），精确说明为什么本轮不新增数学ID或宣新的高维强度。模型转移的几何责任真正已付，但长期Goal仍未实现。

## 10. 剩余高维责任与停止

本轮关闭exact-contained regular quadric任务，不续同一secant/λ/退化Hessian阈值。实际高维narrow终点是近切、近contained管及多尺度variety族，不必有q(v)=0；本证明的方向割线零差正是新缺口所在。它也未处理任意degree、singular physical patch、P复杂度增长或原质量的全递归费用。

一个明确的非免费桥校准：P=x4−x1²，unit v=(√δ,√(1−δ),0,0)，中心0、t∈[−1/2,1/2]。轴距P0≤δ/4，整个δ管在N_(2δ)(P0)，且grad≥1；但所有exact-contained unitline都要求v1=v4=0，所以这根方向距任何exact方向≳√δ，不能O(δ)逐管snap。它不反近contained版Q3，只否定一种免费套本轮定理的步骤。按working_spec修订，本轮§11继续支付这个真实近contained子类的空间packet机制；一般nearquadric仍待后继，不能以Lojasiewicz的δ^θ误差当δ分辨率保真。

两正式全文审查及root整合后归档，macro与唯一后继另存；相关source/38PDF/40sources/78IDs保持，无新ordinary高维界/major。同步以canonical同commit/完整tree/每blobSHA256/clean回执为准。Goal active，未经外部同行评审。

## 11. 真正近contained抛物柱面：空间packet相加没有幂损

这里另付一个超出exact类的实际子例，不作一般nearquadric声明。固定C≥1，P=x4−x1²，允许单位轴ℓ_i仅在N_(Cδ){P0}∩B(0,10)，原tube、权、α、Y、λ定义不变。目标仍同Q3，常数另可依C。梯度始终≥1，regular不是新增假设。按spec修订先承认exact逐管Oδ snapping失败，再给合法空间转移。

写轴为a_i+t v_i，|v_i|=1，|t|≤1/2。靠近bounded零集及梯度有界给sup_t |P(a_i+tv_i)|≤K_Cδ。展开

    P(a+tv)=P(a)+(v4−2a1v1)t−v1²t²。

取t=0,±1/2可严格得

    |v1|≤(8K_Cδ)^(1/2)， |v4−2a1v1|≤2K_Cδ。          (8)

由于|a1|≤10，|v4|≤C_C√δ，故投影π丢去x4时s=|πv|≥1/2（小δ）。每个Y_i点还满足|P(z)|≤K'_Cδ，因此任意组E_j的f_j=δ^−1∫_(x4)1_(E_j)有f_j≤2K'_C，无需知道该组tube精确包含于曲面。

令r=√δ，将每根管按轴midpoint的a1唯一归入interval[b_j,b_j+r)，b_j∈rZ。设W_j=Σ_(该组)w_i、I_j=Σw_i|Y_i|、E_j=∪_(该组)Y_i。索引分区恰有

    ΣW_j=W， ΣI_j=I。

由(8)，整段轴的x1只走O_C(r)，管半径δ≤r；所以E_j位于x1∈[b_j−C_Cr,b_j+(1+C_C)r]。这些interval在任意点最多O_C(1)个重叠，因此

    Σ_j |E_j|≤C_C |E|。                              (9)

这一步保整个单位clock；没有把每管切成r^−1短段，也没有随组数直接pigeonhole丢r幂。

每组projected direction u=πv/s∈S²，写t4=v4/s。由(8)，|u1|≤C_Cr，且

    t4=2a1 u1+O_C(δ)=2b_j u1+O_C(δ)，                 (10)

因为|a1−b_j|≤r且r²=δ。若同组两个u在一个Oδ方向球内，则(10)给|t4−t4'|≤C_Cδ；|b_j|≤11，归一v=(u,t4)/|(u,t4)|遂给|v−v'|≤C_Cδ。故每组投影帽总原权≤C_Cα，**不**乘组数O(δ^−1/2)。这是实证cap，未使用q(v)=0。

现在对每组用§7的函数管道：它只需f_j∞≤C_C、投影轴不短和原cap，三项已分别支付，故

    |E_j|≥cε,C δ^(3+ε) α^−1 I_j³/(δ^9 W_j²)。

空权组忽略。Hölder或加权Jensen严格给Σ I_j³/W_j²≥(ΣI_j)³/(ΣW_j)²=I³/W²。结合(9)和原I≥cλδ³W，得到

    |E|≥cε,C δ^ε λ³δ³W/α。

因此nearcontained抛物柱面子类完整成立，仍只条件于M3。实际新付的是原单位段的慢x1漂移、空间组有界重叠与(10)的角cap相容；单纯exact模型的等价改名或删shading闭包不能替代这些计算。不新增ID/major或n5界，且不把它泛化为所有quadric。非退化不定型的unit null方向可沿曲面漂移O1，不能直接套这里的全时√δ packet；那是剩余真实门槛。
