# R0066正式独审：两斜率、原整层质量与tiny残差门槛

2026-10-18，B独立审root／A；未经外部同行评审。仅编辑指定B稿及本review，无Git／spawn。本formal通过的是有限逆引理与具名source工具下的必要门槛，不能解释为AFF₃、中／大τ、普通五维或general维数定理。

## 1. 实际全文范围与独立责任

已fresh全文读root主稿R0066_two_slope_residual_and_original_mass_gate.md九节、A稿R0066_primary_and_full_goal_audit.md十五节、B稿十二节、working_spec五节、最终macro六节及next六节。另实际对照WZ2609.22035v1 Def17.2–17.4、(157)–(166)、原Lemma19.2／19.4 statement和相关proof、R22 time-restriction closure及R24–28旧责任。

最后已读回root§6明确ρ∈[δ^(1/4),δ^µ]，以及root／spec把γ降至min(γ,1)再简称γ的补充。原slab与tube-KT相应上界在降阶后均只变弱，故合法。root§1最后补入ell Y的2−κ AD、native scalar tildeY的1−κ AD／tube-KT、filled2／3及Φ的κ-AD／slabγ，亦已读回；没有给ell Y另授line-KT。A对官方blob／版本的一手读取记录已实际读；本formal没有重复网络校验，也不将有界搜索的未命中当不存在或优先权证明。

B正证／有限校准已由A独立逐式审查，不以作者自审作独审。本formal独立核root全九节及A的原source应用、newallowed网格与mass账。

## 2. finite threshold、ε=0及严格反攻

以entry max norm，b=c+da给Ets+Est=Δd·Δa及Δc=Ets−Δd·a(t)。D=diam d≤h直接得diam tildef≤ε+(M+1)h；D>h时取实际d-diameter双anchors，每个label至少距一anchor≥D/2，故a距固定anchor≤6ε/D、diam a≤12ε/D，再由Δb=Ets+d(s)Δa得diam f≤ε+12(M+1)ε/h。没有条件角或time参数参与anchor选择，重复labels／任意原权无隐藏分母。

h=√ε给C_M√ε二择；ε=0独立按D=0／D>0处理，不除h=0。a(t)=qte1、d(t)=qt、b=0、c=−q²t²e1给残差≤q²而两种diam皆≥q，平方根数量级正确，不能一般改善成o(√ε)。此只校准有限代数，不保原T／ξ／AD／CW，不是source反例。

两个原labels的directed例E(1,0)=0、E(0,1)=e1且两diam皆1，严排把used g-edge假设替代全部ordered pairs。正质量有向图不保证反向交，g+swap也不保原skew output。root及A／B均未据本反攻否完整source，未将本轮raw门槛作用于g所见最大值。

## 3. 原轻窗、local tildef及整层闭包

原#Z≥δ^(η−1)、δ-separation与≤C/ρ个windows，给删#S_J<c0δ^(α+η)ρ/δ总损≤#S/4。每个余窗同时有absolute #S_J≥c0δ^(α+η)ρ/δ及相对原#Z_J的比例≥cδ^(α+η)。这比只选relative dense的薄窗严格，支付原local proof实际使用的nearfull clock。

有限二择在ε=ρ^(2+4β)下给C_Mρ^(1+2β)，δ小后≤σ=ρ^(1+β)。若任一heavy窗为tildef慢，原Lemma19.4只需该一个window和真实anchor，故直接在原完整配置调用；relative exponent C(η+α)、absolute lower及ρ≥δ^(1/3)、σ∈[ρ²,ρ]均已付。无需把这个local window另当完整配置。

若无这种窗，全部余窗为f慢，才能保其整层并后用19.2。原T完全不改；保留层的Y／X／tildeY／Φ／ξ／原witness不改。跨time union-AD的upper继承，lower由某个完整保留Y层提供，故R22闭包以η*=Lη≈C(η+α)、L整数合法。原平均shading由保留incidences重计；不保证每条T保原density，也没有给子管族新AD lower。

## 4. newallowed比例、σ范围、CW冲突与floor

原ρ未必在restriction后的新格。root／A的正确方案是newallowed上邻R，ρ≤R≤Cδ^(−η*)ρ；共同dyadic嵌套使每个anchor的旧heavyρ窗含于其R-parent。它只用自己旧窗的nearconstant points，不合并不同窗的常数。由分母≤CR/δ，原cluster比例≥cδ^(α+η)ρ/R≥c′δ^(α+η+η*)，对所有新配置anchors统一满足19.2(154)，不是100%近常。

η*≪µ(1−β)保证R²≤σ≤R、R≥δ^(1/3)、R≤1。若σ实施时需上格σ+，其≤Cδ^(−η*)σ；η*≪µβ使σ+≤ρ，增益只多δ^(η*κ)，κ≤1可吸。于是local19.4或global19.2均给原whole T的

    C_CW(T)≥c δ^[C(η+α)/γ]ρ^(−βκ)。

先定µ、β、ζ、γ，再取α、η使C(η+α)/γ+η<µβζ/2，ρ≤δ^µ及κ≥ζ即反原C_CW(T)≤δ^(−η)。所有损失可按该顺序支付，没有固定power的parent再归一。

β<1/4、ρ≥δ^(1/4)给δ≤ρ⁴<ρ^(3+4β)，所以τ=max(δ,ρ max_sameJ||E||)≤ρ^(3+4β)确等价于原全部同窗E≤ρ^(2+4β)。floor不能伪造(严格)下界；empty／singleton窗及大量light窗已单列处理。所得τ>ρ^(3+4β)统一于所有所述原dense整time S，但不是used-edge版本。

## 5. 具名条件、旧闭包及必修项

本轮有限代数完整自证；source应用仍具名使用WZ Lemma19.2／19.4及R22已核整层闭包。没有新独证19.2的完整graph-neighborhood／convex-growth或19.4的完整ξ集中／tube-KT证明，不应以“已应用”擦去该层次。原tildef-Lip另由§19.3支付；本门槛本身不需要先授tildef-Lip、AFF／nonquad、光滑或有理模型。

R19／R21的E+swap和R26旧tiny-τ链都有原AFF／二次／非二次准备；本轮增加的是f／tildef二择及global／local分工，可无该准备支付前端必要门槛。它没有反推AFF₃或完整扩张，也未改写CP／PM或PW4全称gain另立方向。R58／R64的弱反图不保全部source，范围继续分明。

无强制修复项。原ρ范围与γ≤1的字面修复已读回；new R的实际比例、σ+费用、原mass／average-versus-per-tube distinction及δ-floor均通过。53PDF／54sources／78IDs为root统一归档口径，本formal不提前认证元数据、验证或Git同步。

## 6. 正式结论与停止边界

在所列原假设及named-source责任内通过有限两斜率threshold／sqrt ε逆引理、sharp／edge-only反攻，以及完整mixed43对所有原dense整time删选的tiny raw residual必要门槛。内部独审通过，外部同行评审 false；无ordinary n≥5／general新界、major／首创或新数学ID，Goal active。

最终macro6／next6诚实回到同一个未付AFF₃，不以本下界预证中／大τ或偷加whole-f affine准备。下一同源native L与ell W图如需共同正质量，必须实际核同一label／clock／horizontal变量及恢复重数，不能把图并列或旧R28 box当新gain。R66的平方根、β、轻窗、R比例与τfloor微调停止。本formal终稿后停止编辑／检索，由root统一整合、验证及safe sync。
