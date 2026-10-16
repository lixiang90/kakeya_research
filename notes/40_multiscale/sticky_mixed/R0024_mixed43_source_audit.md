# R0024：mixed43 的实际L图、已使用角先验与条件标量化

2026-10-17，`audit_four_dimensional`。已读R23交接、STATE/GOAL/ROADMAP/registry、AGENTS与R24目标，以及本库WZ arXiv:2609.22035v1 Definitions17.2–17.4、§19、§22.1、§22.3–22.5。只核actual d5/k4/ℓ3接口；有限quadratic scalarization由root/B另证。长期Kakeya Goal未解决。

**结论范围：** 原V/J/L计数可以在horizontal3的真实质量上恢复bounded product-reference图；通过初始incidence角边际的domination和heavy-used-cells，可取得共同的二维角差slab先验，而不使用未参与原路径的coarse Φ cells。该项可以供本轮finite gate调用。whole matrix affine准备尚未由AFF-001支付，固定vector τ后的标量图也不是新的四维Kakeya配置；不能据本稿宣称完整mixed43已解。

## 1. 块几何与source位置

Def17.4（PDF66、文本3408–3434）在d5/k4/ℓ3给

    u=f₁∈Mat(1,2), v=f₂∈Mat(1,2),
    a=tilde f₁∈Mat(1,2), b=tilde f₂∈R,
    v=a+bu.

原global ℓ-grain水平维数2，Y_z⊂R²的维数2−κ；完整k-grain水平维数3，tildeY_z⊂R的维数1−κ。每层E的实际point exponent仍是4−κ。T的joint参数AD维数是4。Phi_p⊂R²为κ-AD且slab-Frostman γ>0；不是二维Lebesgue先验，也不能由Φ_q的κ-AD自动得到所有slab upper。

§22.1（PDF93–96、4923–5072行）本就对一般d,k,ℓ定义V/J/L，(176)/(180)是矩阵恒等式，适用于本块结构。原22.3以后专写d4/k3/ℓ2，不能将其预备结果随字母替换升级；其scalar22.5（PDF100–105、5271–5554）只能在已逐项核完有限输入后参考。

## 2. 尚须条件化的whole matrix affine准备

以下进入normalized F/G及nonquad容差时，明确条件于实际整层retained times上有

    f(z)−f(z')=(z−z')R+O(Kρ^(1+ε₀)),
    R=(r;s)∈Mat(2,2), r,s∈Mat(1,2),
    K⁻¹≤||R||≤K,
    osc_J tilde f≤Kρ,

全局retained mass≥δ^ℓ，局部density和后续finite删选loss均已支付。Lemma19.5（4331–4338）一般维数的本尺度upper与named19.2的low-whole-speed pruning可在**已有**这样的matrix-affine mass后使用；它们本身不产生affine mass。

AFF-001只证明实际d5/ℓ2。其观察集的first-coordinate维数为1，N_ρA≤Kρ⁻¹；改ℓ3时observable x∈R²、ξ∈R²，每x-cell fibre cap虽仍成立，但仅给N_ρA≤Kρ⁻²。原scalar ABC21.2的ρ^(−1−κ+ζ)下界在当前κ≤1范围不能击败这个upper。因此这不是省略一个维数常数的推广；ell3 globally dense whole-matrix AFF仍是未付准备。

R22的**整时间层restriction闭包**证明则按任意s=d−ℓ−κ工作：原cross-time Y子并upper继承、lower来自某个完整保留层的Y_z；T和各层Φ不改。这个操作性结论可以依原一般维数证明使用，不等于AFF结论也已推广。

## 3. vector τ必须在选择ψ之前固定

选q内一个实际保留anchor z₀，定义row-valued

    h(z)=v(z)−b(z₀)u(z), c(z)=b(z)−b(z₀),
    E(z,z')=h(z)−h(z')−c(z')[u(z)−u(z')].

令

    τ=max(δ,Cρ max_(同窗口原保留z,z') ||E(z,z')||).

稳定化的母集、全局density、good-q与τ都先于角选择固定。这个row norm保证(179)对全部有界φ成立；不会因最后选择了某个ψ就重新定义τ或免费取得投影后的稳定性。

若有原vector coefficient-weighted nonquad：每个row quadratic、容差Δ=ρ^ε₁(ρ²+ρ|A₁|+ρ²|A₂|)，命中原times比例≤ρ^ε₂，那么τ≤ρ^(3+2ε₁)给固定z'的row linear fit，error≤τ/ρ+Kρ^(2+ε₀)≪ρ^(2+ε₁)，与nonquad及真实retained density矛盾。故非平凡τ满足

    ρ^(3+2ε₁)<τ≤Kρ².

这项tiny-τ排除不除r。条件于whole R非退化时，nonquad也可证明||r||≥K⁻C：若r很小，则s−b(z₀)r有宏观row norm，原AFF给h的linear fit，其Δ中的ρ|A₁|项支配AFF误差。所需次序为AFF/稳定化loss≪µε₂及µ(ε₀−ε₁)。但||r||非零不意味着每个rψ非零；如需要，可另用第6节实际slab prior删除rψ过小的角，支付其g质量。

## 4. horizontal3的V/J/L：原权与packet维数

选合法good-q，沿用原incidence/cross-time平均，不能对任意q声称local lower。记m=#Z(q)、e=#E(q)，有

    m≥K⁻¹ρ/δ,
    e≈K^(±1)m(ρ/δ)^(4−κ),
    #T(q)≤Kρ⁻κ(ρ/δ)^4,
    deg(p)≈K^(±1)δ⁻κ.                       (1)

coarse方向packet数至多Kρ⁻κ，每个packet的fine joint4-AD upper是K(ρ/δ)^4；不能将κ换成二维角ambient维数2。原pointwise每个fine Φ-bin取一原witness，保所有ambient upper，不给删选T新的AD-lower。

令d_T为实际q内marked degree。I=Σd_T≈eδ⁻κ，原CS给Σd_T²≥K⁻¹eδ⁻κm。令B_p=Σ_(T∈T_p)d_T；原V和同horizontal3-grain的J平均给

    #V≥K⁻¹eδ⁻²κm,
    #J≥K⁻¹eδ⁻²κm²(ρ/δ)^3.

第二式只用原总质量和grain数upper `Km(ρ/δ)^(1−κ)`；不要求每个q截出的X locally满。按 `(p,z',z'',middle x_τ,terminal θ_τ)` 签名，签名数≤`K e m²(ρ/τ)^3τ⁻κ`。row E bound使两中间y近τ，x同τ-cell，故原ξ/Φ coherence可用。再次CS得

    #L≥K⁻¹eF_Lm²,
    F_L=δ⁻⁴κτ^κ(ρ/δ)^3(τ/δ)^3.              (2)

这里两处horizontal指数都是3，而非mixed32的2；其他κ来自原Φ的维数，不来自ambient2。

固定z''的code `(y_δ,z,z',φ₁_ρ,φ₂_ρ)` 的恢复上界为：第一终端horizontal x有(ρ/δ)^3，原T₁'有Kδ⁻κ；其z'交点确定；第一V-middle在同k-grain的x有(ρ/δ)^3；两initial管在各自coarse φ-bin各有K(ρ/δ)^κ；第二middle jump的x在τ-cell内有(τ/δ)^3；第二末管受terminal τ-close限制，有K(τ/δ)^κ。于是

    M_code≤K F_L ρ^(2κ)(ρ/δ)^3.               (3)

(2)/(3)与scalar output carrier的`#tildeY_z''(q)≤K(ρ/δ)^(1−κ)`、coarse角数ρ⁻κ精确相消，给某原z''上的0≤g≤1、mean≥K⁻C，reference为scalar Y×原time²×coarse angle²。这是原路径除恢复upper，不是赋原路径独立prior。

## 5. 初始incidence角law支配原L边际

不能给uniform unused Φ_q直接赋slab。改用真正初始incidences

    I_q={ (p,T):p∈E(q), T∈T_p },
    β=φ_* Uniform(I_q),  φ=原管前两方向坐标.

conditional于p的角是原Φ_p（至多fine δ误差和K碰撞），所以按任意实际p权重混合仍有

    β(slab_(n,c,qwidth))≤K qwidth^γ,
    β(ρ-cell)≤Kρ^κ,                          (4)

slab查询先取qwidth≥Cρ，故fine方向误差已吸收。

固定一个初始incidence (p,T₁)，其L扩展upper：T₂有Kδ⁻κ，原z'有m；两horizontal jumps至多(ρ/δ)^3(τ/δ)^3；T₁'有Kδ⁻κ、τ-close的T₂'有K(τ/δ)^κ；共用终层z''有m。故

    #L_(p,T₁)≤K δ^κ F_L m².

除(2)，原归一L的每个初始incidence质量≤`Kδ^κ/e≈K/#I_q`。两条initial arm均如此。因此对任意coarse角bad set U，

    P_L(φ_i∈U)≤Kβ(U), i=1,2.                (5)

这是真正的原L边际domination，不声称conditioned于任意time/endpoint后仍有相同upper。

## 6. heavy-used角carrier与共同product ψ prior

把β投到coarseρ-cells；其全部support被原coarse Φ_q的固定邻域覆盖，cell数≤Kρ⁻κ，只在此处用Φ_q的AD **upper/cardinality**。删掉β_i<K⁻Bρ^κ的cells。由support数upper，总β质量≤K^(C−B)，(5)使两臂原L损失也小。先取B大于全部既有L loss次数，再选实际保留carrier H，得

    #H≈K^(±1)ρ⁻κ,
    Uniform(H)(slab_q)≤K^C q^γ, q≥Cρ.        (6)

slab证明使用每个H-cell的β质量lower乘#H，再用(4)，不使用unused Φ_q的slab声明。

顺序须是：先在原q/time/τ上构造β并删轻角，保(2)；再按z''和output patch平均取得第4节g。由于恢复upper不依赖角值，g仍dense于

    (原scalar output patch)×(原ν time)²×H².

H²是**dominating product reference**；同一个原起点的实际角相关性仍在g里，可能很多reference pairs的g为0。它不等于声称实际两角独立。

令π为Uniform(H)²经`ψ=φ₁−φ₂`的pushforward。条件一个角再用(6)，得

    π{|n·ψ−c|≤q}≤K^C q^γ, q≥Cρ.             (7)

该law与选出的time/endpoint anchor共享一个product reference，anchor的偏好已记在g，不改π。coarseψ是**已使用原角cells的proxy差**，未必是所有code中同一个exact fine差；其距实际fine差O(ρ)给raw误差O(τρ)，已在L关系中。finite slab查询若小于ρ，必须改用max(q,Cρ)，不能越过真实prior base。

对同一ψ的多角pairs按conditional reference平均，可写0≤g_ψ≤1，且E_π E_(A,ν²)g_ψ=mean g。若finite gate的bad-ψ概率≤m_g/4，g≤1使删坏角损失≤m_g/4原reference graph质量；故存在一个正π质量的good ψ，conditional graph mean≥m_g/4。这正是保原g选ψ，不能只选一个对F好但g恒零的方向。

## 7. ψ之前的F/G、scalar output图和uniform h

所有规范化先对row变量定义，不带ψ：

    F_row(t)=(ρ/τ)[h(z₀+ρt)−h(z₀)],
    G_row(t)=(ρ²/τ)c(z₀+ρt)r,
    t=(z−z₀)/ρ.

F_row(0)=G_row(0)=0。由E upper与u-affine误差，`F_row(t)−F_row(s)−G_row(s)(t−s)`有K bound；取s=0及一个共同远time anchor即给两row norm≤K。不需要先除r，亦未把原dyadic Lip当作Euclidean Lip。

在选ψ后，只取`F_ψ=F_row ψ、G_ψ=G_row ψ`，输出scalar图为

    a+(s−t)[F_ψ(t)−F_ψ(s)−G_ψ(s)(t−s)]∈N_w A_out.

仍用同一个vector τ与原ν。先保留δ误差再代AFF，取

    w=K[ρ+ρ^(3+ε₀)/τ],

因为δ≤ρ⁴≤ρ^(3+ε₀)，原δ可吸收入该误差。τ-patch是scalar AD1−κ载体，真实heavy-patch平均保图密度；空间除τ后cover upper为K w^(−1+κ)。本分支scalar tube-KT与AD相容，但这里不借scalar投影来制造维数缺口。

在small/middle τ上界`τ≤ρ^(3−ζ₁)`时，row版(200)从原coefficient-weighted nonquad推出，uniform h可安全取

    h₀=K⁻Cρ^(2ε₁+ζ₁),
    a₀≤K^Cρ^ε₂/θ,

θ为此时实际retained time mass。finite gate若要求bounded F或系数加权的scalar目标，必须同步支付K归一、coefficient norm和query precision；不得只把它们写成绝对常数。特别先选`ζ₁+4ε₁<ε₀`，使w/h₀有正幂余量；再令AFF/stability等loss小于ε₂、该余量及finite gate的b指数。

ψ选择不重新最小化τ，不声称projected τ_ψ≈τ。finite gate取得的是同一vector τ-frame上的scalar quadratic nonfit和有质量图，这正可改变中τ的实际有限输入。

## 8. full mixed43仍未付的责任

1. whole-matrix globally dense AFF的实际存在尚未证明，ell2的AFF-001不能移用；只给它作输入时，本稿的normalized source应用是条件结果。
2. 原large-τ Step3删除G项产生Kρ³误差，不受原w覆盖；需保G或改mesh为K[ρ+ρ³/τ]并重付参数。即使对F_ψ得近常值，也只能缩projected Eψ，不能拿它违背预先固定的vector τ稳定性。
3. 原细time spacing δ/ρ不等于w-separated B；F/G归一后可在w-timecell内大幅变化。finite gate可直接用原ν，所以本轮不需要该未付coarsening；但调用source22.5后半段的finite radial/Kaufman定理时仍须明确其weighted/representative选择版本。
4. 取得scalar F_ψ、G_ψ与A⊂R只是一组有限translation图，不是构造了一个d4/ell2完整原配置。不能整段调用Lemma22.5而跳过(196)容差、τ稳定、共同prior与高级projection输入的实际hypotheses。

本轮已可支付的是**used角差slab prior＋同图retention**这一真实接口；finite quadratic scalarization是否成立由root/B独审，后续高级定理仍named。没有在此排除完整mixed43、其他五维分支或general/Hausdorff，亦无重大性或新维数界声明。
