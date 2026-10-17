# R0054：共同因子近图的两 ruling、原角权及低维闭包

2026-10-17，B。已实际恢复 GOAL/STATE/ROADMAP、registry78状态、R53 next与R54 working_spec。只核指定真实五维近图模型，不Git、不spawn、不改元数据。下面自含证明强于原目标的平面闭包；不调用三维M3，不宣一般五维严格下界/重大性或新颖性。仍需root/A独立审查，未经外部同行评审。

## 1. 原命题、闭包和本轮停止

固定C₀及B(0,10)，Z={(x₁,x₂,x₃,x₁x₂,x₁x₃)}⊂R⁵。有限原单位轴ℓ_i=a_i+t v_i，|v_i|=1、|t|≤1/2，逐点在N_(C₀δ)Z；T_i=N_δℓ_i为真管，|T_i|=v₅(δ)≈δ⁴。给原w_i≥0、W=Σw_i>0，可测Y_i⊂T_i，E=∪Y_i、I=Σw_i|Y_i|、λ=I/(v₅W)>0。physical S⁴上任何固定C₁δ帽的原总权≤α。证明

    |E|≥c_C₀ λ² δ⁴ W/[α log(2/δ)]。               (1)

常数不依原族数、权跨度、λ或δ。因为0<λ≤1，(1)还给原任意ε的δ^(4+ε)λ³W/α目标。删管/缩shading不保I、W或λ；本证始终用原计数权，按整label分支/分包，不把平均免费换成逐管密度。目标只包含此near-whole-axis模型；一般near-tangent marks、一般variety或一般R5原族不被默认纳入。一主轮完成即冻结整个common-factor模板，不续输出/ambient/rank小改。

## 2. 真near图到全部系数：没有中间方向尺度

令P₄=x₄−x₁x₂、P₅=x₅−x₁x₃。bounded域及整轴距离假设给sup_|t|≤1/2 |P_j(a+tv)|≤Kδ，K只依C₀。展开两个二次式，比较t=0,±1/2，严格得

    |a₄−a₁a₂|, |a₅−a₁a₃|≤Kδ，
    |v₄−a₁v₂−a₂v₁|, |v₅−a₁v₃−a₃v₁|≤2Kδ，
    |v₁v₂|, |v₁v₃|≤8Kδ。                         (2)

最后常数8是可用上界：p(1/2)+p(−1/2)−2p(0)为−v₁v_j/2。不能从少量shading近Z推出(2)，本证使用原整段unit clock。

由|a|≤10与两个linear residual，|v|≤K₁|(v₁,v₂,v₃)|+K₂δ。取δ₀固定足够小，unitnorm给

    |(v₁,v₂,v₃)|≥η:=1/(2K₁)>0。                 (3)

按|v₁|≥η/2归B支，则|v₂|,|v₃|≤16Kδ/η。其余归A支，|(v₂,v₃)|≥√3η/2；由|(v₁v₂,v₁v₃)|≤8√2Kδ得|v₁|≤K₃δ。故全部原labels恰分为

    A：|v₁|≤K₃δ；  B：|v₂|,|v₃|≤K₃δ。           (4)

边界/同时满足时以先前判据唯一归类，不重复计原权。对足够小δ，三方向分量不可能同时O(δ)。原spec的dyadic h设想在unitnorm和有界base点下可消去，不需中间δ^θ尺度。若δ∈[δ₀,1]，固定数方向帽覆盖S⁴给W≤Kα，而|E|≥I/W≈λδ⁴；用λ≤1与log(2/δ)≥log2也得(1)。以下处理小δ。

## 3. A支：整单位轴近二维平面，原方向而非参数方向

把a₁唯一归入δ宽半开格，格中心b。记

    P_b={x₁=b, x₄=b x₂, x₅=b x₃}，
    V_b={v₁=0, v₄=b v₂, v₅=b v₃}。

原轴每点x的x₁−b=O(δ)；P₄(x)、P₅(x)=O(δ)，故x₄−b x₂=P₄(x)+(x₁−b)x₂=O(δ)，同理x₅−b x₃=O(δ)。tube厚度仅多固定倍δ，因而整个T_i⊂N_(K₄δ)P_b。三个约束相对正交距离的比较uniform于|b|≤11：先改x₁到b，再改x₄/x₅，已显式构造O(δ)近点。

方向亦有dist(v_i,V_b)≤K₅δ，直接由(2)、|v₁|≤K₃δ和|a₁−b|≤δ核出v₄−b v₂、v₅−b v₃=O(δ)。令Π_b为正交投影到V_b，u_i=Π_bv_i/|Π_bv_i|，则|Π_bv_i|≥1/2且|v_i−u_i|≤K₆δ。same projected S¹的Cδ帽中原physical方向全落一个K₇δ帽，固定数原帽覆盖给总权≤K₈α。没有用参数角代替physical S⁴角；正交投影的方向归一也已支付。

设E_b为该包原shadings的并。每包实际点都在x₁∈[b−K₉δ,b+K₉δ]，所以

    Σ_b1_Eb≤K₁₀1_EA，  Σ_b|E_b|≤K₁₀|E_A|。     (5)

一条原label只归一个b，ΣW_b=W_A、ΣI_b=I_A。所用actual overlap与包数无关；不把O(δ⁻¹)包数当常数。

## 4. 平面weighted L²：antipodal、端帽及任意原权

在P_b固定基点z_b，点的投影取仿射映射x↦z_b+Π_b(x−z_b)，方向映射仍为Π_b。将该真实投影T_i包入固定半径Kδ、轴长≤1的planar capsules S_i。投影轴长≥1/2，端帽不删除。对两个这样的包，令θ为两无向轴的锐角（即同时接近u和−u都算near parallel），有自含几何界

    |S_i∩S_j|≤K δ²/(δ+θ)。                       (6)

θ≤δ时用|S_i|≤Kδ；θ>δ时用两条无限strip的parallelogram面积≤Kδ²/sinθ≤K′δ²/θ，capsule可先放入固定宽strip，端帽不增加上界。沿S¹把θ≈2ᵏδ的区域按δ帽覆盖，所需O(2ᵏ)个帽（在±u附近各计一次）。§3原cap给相应原权≤Kα2ᵏ。因此对固定i，将(6)逐dyadic annulus求和，每层≤Kαδ，至多Klog(2/δ)层。

令μ_b=Σ_(i∈b)w_i1_Si，L=log(2/δ)，则

    ∫_(P_b) μ_b²≤K α δ W_b L。                  (7)

重复方向、反向定向、重合轴与极小权都在这同一个原加权求和内；未假等权或逐管分离。若原帽仅按有向S⁴给出，antipodal只是两组帽，费用固定2，非漏项。

因为E_b⊂N_(Kδ)P_b，沿V_b⊥的三维normal纤维体积≤Kδ³。令f_b=δ⁻³∫_(V_b⊥)1_Eb，得0≤f_b≤K、‖f_b‖₂²≤Kδ⁻³|E_b|。Fubini保实际shadings：∫f_b μ_b≥δ⁻³I_b。CS与(7)给

    |E_b|≥c I_b²/[α δ⁴ W_b L]。                 (8)

将(8)求和，用(5)及ΣI_b²/W_b≥I_A²/W_A，得到

    |E_A|≥c I_A²/[α δ⁴ W_A L]。                 (9)

W_b=0空包跳过，I_b=0取零。没有先抽某一个包而损包数，也没有对原λ多作一次heavy。

## 5. B支：近一维线，两个orientation帽足够

将midpoint(a₂,a₃)唯一归入边长δ的二维方格，中心(b₂,b₃)。由(4)，整轴的x₂,x₃只走O(δ)。又用P₄(x)、P₅(x)=O(δ)，全T_i落在O(δ)邻域

    L_b={(s,b₂,b₃,b₂s,b₃s):s∈R}。

原方向满足v₂,v₃=O(δ)、v₄−b₂v₁=O(δ)、v₅−b₃v₁=O(δ)。归一后距±d_b两个帽之一为O(δ)，其中d_b=(1,0,0,b₂,b₃)/√(1+b₂²+b₃²)。所以该包总原权

    W_b≤Kα。                                     (10)

两正负方向必须都保留；若只计一个帽是不合法的。直接点态Σ_(i∈b)w_i1_Yi≤W_b1_Eb给|E_b|≥I_b/W_b≥cI_b/α。不同b的实际E_b在(x₂,x₃)坐标仅处于各δ格的固定扩大，overlap有绝对上界，故

    |E_B|≥c I_B/α。                              (11)

这里不需要管间不重叠、原shading填满或同方向只一条line；所有重复都由原α支付。原midpoint包保完整clock和端帽。

## 6. 两支回传原平均λ，不损额外密度

I_A+I_B=I、W_A+W_B=W。若I_A≥I/2，由(9)、W_A≤W给|E|≥cI²/[αδ⁴WL]。否则(11)给|E|≥cI/α；而I≤v₅W≤Kδ⁴W、L≥1，故也有同一下界。代入I=λv₅W≈λδ⁴W，得(1)。这是原任意平均λ，不声称删后逐管密度等于原λ。

若原本每管|Y_i|≥λ₀v₅，则整label分支/分包后原每管shading完整保留，逐管条件仍成立；本证明仍可仅用其原平均。任意后续缩shading须重算I，不能把(1)的旧λ继续套用。两支只按固定比例选incidence，不作δ^η质量删选。

## 7. λ²校准、真实边界与低维等价纠偏

在精确P₀={x₁=x₄=x₅=0}取S¹的δ方向网，W/α≈δ⁻¹。unit axes从同一原点出发，令原shading为各管共同初始长度s的一段，δ≤s≤c。可选真tube子集使λ≈s，且union在P₀的半径Cs圆盘之O(δ)三维normal邻域，故

    |E|≤K s² δ³。                               (12)

(1)的λ²δ⁴W/α≈s²δ³，仅相差L。若试将λ²换成λᵖ、p<2并保统一常数/log损，取s=δᵃ、0<a≤1即矛盾；若另容δ^ε，只需ε<a(2−p)。这是密度指数校准，不是Kakeya反例或一般模型的体积下界反例。

完整近Z模型已归为二维平面/一维直线与原shading的elementary闭包，M3/原四维完整proof均未使用。其ambient为5不带来新高维强度，不新增数学ID。相反，本轮纠正了R53 next中似需anisotropic多层/M3的预期：unitnorm的(3)消掉中间层，真正近轴也可由(2)全clock O(δ)近相应ruling。这不否R53抛物柱面√δ snapping失败，因为那是不同二次几何。

一般degree/variety不具有(4)，原near-tangent marks也不含整轴近Z；不能把这些假设删除后声称已有五维narrow输入。该结果没有满S⁴方向族，不是H5/HRZ严格terminal，也不解决一般→sticky原质量提取。成功即停止整个common-factor模板，不续更多输出/ambient/系数/rank。

## 8. 独立审查及下一真实缺口

root/A须实际全文核(2)→(4)、两正负orientation、δ-packet实际重叠、原cap与(7)–(11)，再统一归档。B正式review待root/A/macro/next最终稿齐后实际全文审，不以自审替独审。

下一不能把R48停下的nearfull DIR重读为fullLp terminal，也不能把R49已条件支付的parent/window/Jacobian/去重再命名为已找到general→sticky parent。任何实际一般R5候选必须保其原输入并有新可付机制；若暂无新来源，先宏观查证缺口比再选一个共同因子toy更合适。当前长期Goal仍active，未达一般n≥5或重大中间结果完成标准。
