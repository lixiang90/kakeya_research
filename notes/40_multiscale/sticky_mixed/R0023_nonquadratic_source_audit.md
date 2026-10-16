# R0023：实际 mixed32 非二次分支的尺度、原图与标量断点

2026-10-17，`audit_four_dimensional`。已读R23 spec、R22 handoff/STATE和本库WZ arXiv:2609.22035v1 §22.5全文、§22.1–22.3及Theorem13.5/Lemma13.7相关段落；PDF101原图已渲染核对。主任务仍是N5-MIXED32-NQ01。本稿不重做PCT或LOCAL-AFF，不宣称完整source/五维结论。

**结论：** 小τ分支及F/G的bounded归一可按原质量延伸到vector Y；非二次假设还可在已付AFF准备下直接推出标量r下界。实际τ-ball缩放保留absolute tube-KT，但不会把二维A变成标量维数缺口。原大τ步删除G项的误差未被其所写w覆盖，须另付较粗mesh；原细时间到w-separated B也不能仅以bounded F/G免费传回。真正后半段缺少的是原cycle prior下的vector增长/共同line机制；不是把scalar投影定理换个标题即可填入。

## 1. 精确源位置与当前数据

行号按本库extracted文本以`\n`切分：

| 原步骤 | PDF页 | 文本行 |
| --- | --- | --- |
| Lemma22.5非二次假设(196) | 100 | 5271–5276 |
| stable τ、小τ contradiction | 100 | 5278–5306 |
| L图、τ-patch、w与F/G | 100–101 | 5307–5344 |
| 大τ、scalar Theorem13.5 | 101–102 | 5345–5404 |
| F的系数加权二次nonfit(200) | 102 | 5405–5421 |
| S/Q、BSG、四cycles | 103 | 5424–5472 |
| radial22.2与Kaufman22.3调用 | 104–105 | 5475–5554 |
| scalar Theorem13.5 | 52 | 2712–2724 |
| asymmetric BSG Lemma13.7 | 54 | 2826–2831 |
| radial22.2、一般ambient scalar projection22.3 | 96–97 | 5074–5091 |

本轮实际d5/k3/ℓ2：`u,r∈R`，`v,a,b∈R²`，`v=a+bu`。令原窗口中实际保留anchor为z₀，记

    h(z)=v(z)−b(z₀)u(z),  c(z)=b(z)−b(z₀),
    E(z,z')=h(z)−h(z')−c(z')[u(z)−u(z')].

AFF给whole速度(r,s)∈R×R²、`|(r,s)|≥ν=K⁻¹`，且u,v的pairwise affine误差≤Kρ^(1+ε₀)。19.5支付后`osc b≤Kρ`，原b(z₀)仍有界。所有保留时间及q、L-path均为原对象，time子配置闭包由AFF-001明确支付。

非二次是假设：任意vector A₀,A₁,A₂的fit、容差

    Δ=ρ^ε₁(ρ²+ρ|A₁|+ρ²|A₂|),

至多占原window时间的ρ^ε₂比例。它不推出每个scalar λ·h非二次。须先固定ε₀、ε₁、ε₂，再使AFF损失及原η足够小；例如每个所用局部retained比例至少δ^ℓ，需`ℓ≪µε₂`，以使δ^ℓ≫ρ^ε₂。以下K包括这些已付小幂，不能忽略其ε/γ费用。

## 2. 非二次分支可先合法推出r非零

这项推导不用R21的τ-collapse。令`H=s−b(z₀)r∈R²`。原whole-f AFF直接给

    h(z)=h(z₀)+H(z−z₀)+O(Kρ^(1+ε₀))         (1)

于同一原retained times。若`|r|≤ν/[10(1+|b(z₀)|)]`，由whole速度lower得`|H|≥cν`。取A₀=h(z₀)、A₁=H、A₂=0，非二次容差满足

    Δ≥cνρ^(1+ε₁).

ε₁<ε₀/2与损失后取小保证`Kρ^(1+ε₀)≪νρ^(1+ε₁)`。于是(1)将整个AFF retained fibre置于这个允许的vector linear fit；其相对原window质量δ^ℓ大于ρ^ε₂，违背(196)。所以

    |r|≥cν/(1+|b(z₀)|)≥K⁻C.                 (2)

责任是**真实AFF质量、whole速度lower和系数加权nonquad容差**共同给出(2)。若只给抽象F/G/S图而无这些source输入，则r=0仍不能排除；不能将此结论当任意finite模型的免费假设。也没有由此取得任何scalar λ·h的非二次性质。

## 3. τ稳定化与小τ区间

以原time子集定义`τ_j=max(δ,Cρ max|E|)`，在全局δ^(η_j)-dense候选中最小化；有限层稳定化仍需全局并、低密窗删除和原time闭包，不能用单一q的局部质量冒充全局。若某j有`τ_j≤ρ^(3+2ε₁)`，固定原z'，由u-affine与`|c(z')|≤Kρ`得

    h(z)=h(z')+c(z')r(z−z')
                  +O(τ_j/ρ+Kρ^(2+ε₀)).     (3)

这是vector linear approximation。因为`ε₁<ε₀/2`，右误差远小于`ρ^(2+ε₁)`，而任意linear系数对应的Δ至少是此数。同一retained质量大于ρ^ε₂，所以(3)违背非二次。此步无需先除r。

因此非平凡区间为

    ρ^(3+2ε₁)<τ≤Kρ².                        (4)

相邻τ_j的ratio稳定按source5305–5306取得，允许后续有限δ^O(η_j)删选；η_j最终须小于µε₂等阈值。这里存在一个局部误差细节：源5315在进入patch时写`δ≤Kτρ`，由(4)本身并不成立；例如ρ=δ^(1/4)、τ≈ρ^(3+2ε₁)时τρ≈δ^(1+ε₁/2)<δ。应保留L误差中的δ直到下一步，不能在此直接扔掉。

## 4. 原L图、真实τ-patch和physical tube-KT

原§22.1水平维数为2的V/J/L计数已经在R21记录：恢复分母、angle-pair权和0≤g≤1均来自原路径，不把每条管假设成独立满time degree。当前图的输出仍满足

    y+(z'−z)E(z,z')ϕ ∈ N_(Kτρ+Cδ) tildeY_(z'')(q),
    ϕ=φ₁−φ₂,

且fine angle换coarseρ-bin只增加O(τρ)。原scalar Φ的κ-AD和g≤1允许删除过小|ϕ|并固定一对实际角，保`|ϕ|≥K⁻C`及K⁻C graph density。

写α=2−κ。原tildeY(q)的相关cover upper为`N_τ≤K(ρ/τ)^α`；合法good-q/L恢复同时给frame的fine cardinal≈K^(±1)(ρ/δ)^α。将input y按原τ-cells/balls分桶，每桶fine cardinal≤K(τ/δ)^α。先删低于`K⁻B(τ/δ)^α`的轻桶，其总fine reference质量和g质量都小；再按graph weight平均选择一个保留桶。于是input patch实际有≥K⁻C(τ/δ)^α个fine labels，graph在该patch×原time²的reference frame中仍dense。

不能对任意裁切patch重新赋AD-lower；以上是用全局carrier大小、patch cover upper和g≤1付出的heavy选择。output因|translation|≤Cτ只需取同一patch固定倍扩大，其cardinality upper与input比较仍仅差K。

将此空间patch除以τ、时间除以ρ，得到二维A。原tube-KT是**absolute covering cap**：若working width w≥δ/τ，normalized长L≤1对应原宽τw、长τL≤τ≤1，所以

    N_w(A∩tube_(w,L))≤K(L/w)^(1−γ).          (5)

没有额外τ^(−γ)概率归一因子。AD提供的是`N_w(A)≤K w^(−(2−κ))`；它不提供标量`w^(−(1−κ))`。output/input的裁切或平移保(5)的upper，不冒充被裁子集是新完整AD族。

## 5. w、F/G与有界norm：不依赖r非零

保留δ并代入u-affine，raw误差是

    K(τρ+δ+ρ^(3+ε₀)).

因为ρ≥δ^(1/4)、ε₀<1，`δ≤ρ⁴≤ρ^(3+ε₀)`。所以最终正确working width仍可取

    w₀=K[ρ+ρ^(3+ε₀)/τ],                    (6)

即源5322–5324的形式；它修复了第3节过早drop δ的步骤。由(4)，`w₀≤Kρ^(ε₀−2ε₁)→0`；同时τw₀≥δ，故(5)全部physical查询合法。

可直接定义而无需改原几何坐标：`t=(z−z₀)/ρ`，选z₀为q内一个实际保留time，故0∈B，令

    F(t)=(ρϕ/τ)[h(z₀+ρt)−h(z₀)],
    G(t)=(ρ²ϕ/τ)c(z₀+ρt)r.

于是F(0)=G(0)=0。定义

    D(t,s)=F(t)−F(s)−G(s)(t−s).

原E upper、u-affine误差和(6)给`|D|≤K`。特别D(t,0)=F(t)，所以|F|≤K。对任意s，原time packing/density可选距s≥K⁻C的一个t，因而由D恒等式得|G(s)|≤K。也可使用source的E+swap与共同远anchor。这个有界norm论证是vector成立的，且**不需要除以r**；即使抽象r=0，G=0也完全合法。

这里的bound是小幂K，不是免费unit bound。若所接finite定理要求|F|,|G|≤1，可取1≤L≤K并同步将A、F、G除L，working spatial mesh改为w₀/L；真实physical空间比例变为τL。参数后取小时τL≤1，absolute tube-KT仍可由原physical查询支付，fine base相应为δ/(τL)。nonquad容差也须同步除L，不能保留未经支付的相同base常数；其小幂费用需由ε余量吸收。不能只缩F或G而保持原A与误差不动。

L图正确变为

    a+S(t,s)∈N_(Cw₀) A_out,
    S(t,s)=(s−t)[F(t)−F(s)−G(s)(t−s)].        (7)

使用真实L符号和固定角差次序；整体反号只相当于反射A，不改变质量/cover。不能仅凭bounded F/G把原dyadic Lip升为Euclidean Lip。

## 6. 大τ步删G的误差须另付mesh

原Step3取`τ>ρ^(3−ζ₁)`，5346–5350由`|c|≤Kρ、|r|≤K`将G项从(198)删去，并仍写N_(2τw₀)。PDF101图已确认该文字。

但raw G贡献只知≤Kρ³，normalized贡献≤Kρ³/τ。它未必被(6)的`K[ρ+ρ^(3+ε₀)/τ]`覆盖；例如τ≈ρ^(3−ζ₁)时，前者约ρ^ζ₁，后者约ρ^(ε₀+ζ₁)，差一个固定幂。此处不能以“τ较大”直接忽略。

保守修复是继续保留G，或在此large分支改用

    w_L=K[ρ+ρ³/τ]≤Kρ^ζ₁.                   (8)

再重查nonconcentration、稳定化和高级输入的全部参数。新mesh不再有原5354所需的`w≤Kρ^ε₀`保证；它只由ζ₁控制。本文未补完scalar大τ证明，也未据这个中间省略否定原主定理。

即使scalar修补完成，Theorem13.5的原结论只有一维scalar A cover下界，不能和当前二维A的`w^(−(2−κ))`upper矛盾。原13.5明确要求A⊂R、F:B→R，β≤1且输出是scalar product increment；不能把vector字母直接代入其statement。

## 7. 小/中τ的vector nonquad传递与粗时间责任

在`τ≤ρ^(3−ζ₁)`区间，代入F可将源(200)的系数加权nonquad逐坐标同时传为vector版本：fit error可取

    Δ_F=ρ^(2ε₁+ζ₁)(1+|A₁|+|A₂|).

反推原系数`A_i'=(τ/(ρ^(1+i)ϕ))A_i`，并由τupper、|ϕ|≥K⁻C及另一个ρ^ε₁余量吸收K，确实落入原(196)容差。所用fit时间仍是同一原fibre，不能把两个vector坐标在不同子集上的近似拼成共同fit。

但是原B仍有fine spacingδ/ρ≪w₀。源5499称“we may assume B to be uniform on scale w”，需要实际coarsening/选择责任。F乘ρ/τ后，在一个w₀-time cell的variation至多只知`K(ρ²/τ)w₀`，通常远大于w₀；G也没有免费fine-scale Lip。故不能照R22观察图的bounded每time fibre直接取coarse F/G代表并认为误差O(w₀)。

合法选项是保留全部fine indices和原time概率ν，证明所需finite增长/投影输入的weighted版本；或另付stratified representative选择，同时保g density和**所有**系数加权vector quadratic nonfit。若后者已付，可把time坐标round到w₀-grid，因为S仅用F/G有界，time prefactors只增加O(Kw₀)误差；但nonquad转回有`w₀(|A₁|+|A₂|)`费用，须先在系数加权形式处理。本文不把这项选择当已证明，也不把它记作完整source反例。

## 8. BSG、四cycles与原prior

源Step6按pair-image S的w-cells和原pair重数作dyadic层S_j，再取S'。必须保留这个近等重数层：仅知道S'占image-cardinality比例，不能推出其pullback H⊂B²有相同原mass。原5470前另需`#S_j≥w^(−c₀)`，以控制Lemma13.7所需`log#A/log#S_j`；vector情形仍须真实证明这个lower，不能只由g dense宣布BSG已可调用。

Lemma13.7印刷statement的X,Y都在R。其abelian-group BSG思想不固有地限于标量，固定维vector离散版本可能通过网格化支付，但需明确原weights、rounding、energy和参数；本稿没有把source的scalar statement直接当作已验证vector定理。

若这些步骤已合法取得H，令ν为当时真正的time reference，`p=(ν×ν)(H)`。weighted CS给

    C₄={ (t₁,t₂,s₁,s₂): (t_i,s_j)∈H },
    ν⁴(C₄)≥p⁴.

同样K_(4,2) pattern的ν⁶质量≥p⁸。这些指数只付固定loss，允许沿原finite/weighted prior使用。归一后的cycle law由`p⁻⁴ ν⁴`支配；它不等于Q-image上的均匀law，更不使四个条件time独立。

合法BSG结论(206)使`A'+Q(C₄)`有小cover。但该sumset一般不仍在原A里，不能直接对其输出套原tube-KT。A'若仍是原A的subset/固定误差网格则继承**input**的absolute tube cap；若要从共同line得到增长，应使用这个input fibre cap及原Q的实际mass/cover，另作已付论证。

## 9. 真正scalar的polarization与projection断点

vector代数本身无问题：

    V(t)=(t,t²,F(t))∈R⁴,
    U(s)=[F(s)−2sG(s), G(s), s I₂]∈Mat(2,4),
    Q=(U(s₁)−U(s₂))(V(t₁)−V(t₂)).            (9)

源scalar版U,V∈R³，Q是一个scalar内积。后续使用scalar性至少有三处，不能只说“已有高维Kaufman”：

1. 源5489–5506以任意hyperplane normal的最后一个scalar分量n₃除法，将P=V(B)−V(B)的slab集中变成F的scalar quadratic fit。vector nonquad只排**共同vector** quadratic fit；F=(g,0)仍可能nonquad，但V及P全在最后坐标为0的hyperplane，故同样的slab假设不成立。
2. Theorem22.2只声明R³内2-Frostman、uniform且slab-nonconcentrated的P。它输出2-dimensional radial directions，正好接Lemma22.3在ambient3需要的full2 slope family。当前P⊂R⁴，(9)又是2×4矩阵作用，源中没有给这个matrix projection family所需的relative/rank-adapted有限定理。
3. Lemma22.3虽对任意ambient d声明，仍是`π_λ:R^d→R`的**标量**projection，要求参数Λ是full(d−1)-dimensional Frostman。它不是`U↦Uv∈R²`的共同v矩阵投影定理；即使得一个scalar一维image，仍不能击败A的2−κ预算。

因此不能免费将vector nonquad改为每个scalar projection nonquad，不能假设Q在任意dense cycles上full-rank2，也不能把Y投成标量后继续保1−κ维数缺口。当前可检验的新输入必须保原cycle prior：或证足量共同line输出并付input tube-KT增长，或证真正二维的增长/cover，且误差、选择mass均已支付。

## 10. 当前认证范围

本稿付出nonquad特有r下界、小τ排除、F/G有界的非除法证明，核实际patch与physical tube-KT，并定位原large-τ误差、fine/coarse选择和后半段matrix projection的精确责任。源局部印刷/误差省略只针对所引中间推导，不据此推翻整篇主定理。

未给完整vector nonquadratic增长定理，未完成一般matrix分支、其他五维配置或Hausdorff归约。root/B若取得新的same-prior球cap、linewise或rank-mass估计，应另列它们的实证输入与范围，不能由本文的形式(9)自动登记主分支完成。
