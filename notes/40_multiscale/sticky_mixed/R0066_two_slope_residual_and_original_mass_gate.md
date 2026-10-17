# R0066：两套斜率、原残差和全局质量门槛

2026-10-18，root。先写R66 spec§5后施工。完整目标仍为ordinary欧氏n≥5/general；本稿只支付完整mixed43的一项必要门槛，未得到AFF₃、中/大残差排除或新维数界。有限代数部分自证；source应用明确引用WZ2609.22035v1 Lemma19.2、19.4及R22整时间闭包，它们的全部高级证明没有在本轮独立重证。未经外部同行评审。

## 1. 原对象、量词与本轮新增责任

固定完整Def17.2–17.4的d=5、k=4、ell=3。原T joint4-AD、C_CW(T)≤δ^−η；全部E_z、两套水平grains、原点ξ_p/Φ_p、used角slabγ和原直管访问均不改。写

    f(z)=(a(z);b(z)),  tildef(z)=(c(z),d(z)),
    b(z)=c(z)+d(z)a(z),

a、b、c为row2，d为scalar。各坐标绝对值≤固定M≥1；原定义M为固定维常数。行范数及矩阵范数取entry max；换Euclidean只多固定维常数。

具体保留：ell横向Y_z⊂R²为2−κ维AD，native横向tildeY_z⊂R为1−κ维AD及tube-KT(1−γ)，两个水平grain的原filled维数分别2和3，Φ_p⊂R²为κ维AD并有slabγ。κ≤1属于native scalar AD的自然范围；不为ell Y另授line-KT。所有这些原条件都作为named低速引理的完整输入，而非声本有限代数独自用到了每一项。

对同原时间labels定义row residual

    E(t,s)=b(t)−b(s)−d(s)[a(t)−a(s)].             (1)

实际V/L原路径的scalar native output位移为(s−t)E(t,s)ψ，加源已记的误差。该恒等式不授任意原管对每个指定time的访问，也不把g内的角或clock独立化。本稿要证的是raw全部ordered pairs小的逆结论；从“used g边小”到它的提取不在结论内。

R24–26旧tinyτ排除以whole-f AFF及nonquad为准备。本稿测试另一条责任：利用原native3grain对应的tildef低速定理，能否在不付AFF的情况下直接排极小raw residual。它并不推出全称正gain，反向也不能由本必要条件得到AFF；没有把旧gain换名登记。

## 2. 有限两斜率逆引理：阈值形式

令Z₀为任意非空有限labels，bounded a,b,c,d满足上述兼容式。设ε≥0，全部t,s∈Z₀满足||E(t,s)||≤ε。记D=diam d。对任意h>0，至少下列之一成立：

    D≤h:  diam tildef ≤ ε+(M+1)h;
    D>h:  diam f ≤ ε+12(M+1)ε/h.                (2)

这里diam以全部labels对计算，不要求time分离、连续、可微、AD或density。证明的两个恒等式是

    E(t,s)+E(s,t)=[d(t)−d(s)][a(t)−a(s)],       (3)
    c(t)−c(s)=E(t,s)−[d(t)−d(s)]a(t).          (4)

若D≤h，(4)给diam c≤ε+MD，直接得第一支。若D>h，取实际anchors z₀,z₁使|d(z₁)−d(z₀)|=D。(3)给||a(z₁)−a(z₀)||≤2ε/D。任意t至少距其中一个d-anchor≥D/2，故其a距相应a-anchor≤4ε/D，距a(z₀)≤6ε/D。于是diam a≤12ε/D；再由Δb=E+d(s)Δa给diam b≤ε+12Mε/D，得到第二支。没有选择依赖于ψ的anchors。

## 3. 平方根形式、精确零点及尺度检验

当0<ε≤1，取h=√ε，(2)得

    min(diam f,diam tildef)≤C_M√ε.             (5)

ε=0需单列：D=0时由(4)得tildef常数；D>0时由(3)和两anchors得a常数，再由E=0得b常数，即f常数。不能把ε=0的式子解释为除以h=0。

平方根的数量级不能由纯代数假设普遍改进。取labels t∈[0,1]的任意包含0、1的有限集，a(t)=q t(1,0)、d(t)=q t、b(t)=0、c(t)=−q²t²(1,0)，0<q≤1。则b=c+da，E(t,s)=−q²s(t−s)(1,0)，其sup≤q²，而diam f≥q、diam tildef≥q。因此只由residual≤ε不能强制二者之一为o(√ε)。该校准没有T/E/ξ/AD/CW，绝非完整source反例或新Kakeya反例。

## 4. 对原时间删选的绝对轻窗修剪

固定S⊂Z、#S≥δ^α#Z、α>0，所有质量以原#Z为分母。原#Z≥δ^(η−1)，原time bounded且δ-separated。固定dyadicρ，令J为ρ-windows；其个数≤C₀/ρ，每窗原#(Z∩J)≤C₁ρ/δ（ρ≥δ）。删掉

    #(S∩J)<c₀ δ^(α+η)ρ/δ                       (6)

的全部windows，c₀固定充分小。所删数≤C₀c₀δ^(α+η)/δ≤#S/4，故保留整时间层S_*有#S_*≥3#S/4≥(3/4)δ^α#Z。每个保留窗同时满足

    #S_J≥c₀δ^(α+η)ρ/δ,
    #S_J/#(Z∩J)≥(c₀/C₁)δ^(α+η).               (7)

第一式支付绝对local clock；第二式支付在原配置中调用local cluster定理的密度。仅对relative density作剪裁不足以展示第一式，故本稿不依赖19.4印刷statement外的免费local满密度。任意两套分支轮流出现都保这个预算。

## 5. 原配置闭包、shading与allowed scale的精确范围

只删整时间层。T不删，joint4-AD和原CW不变；保留层的E_z、X、Y、tildeY、ξ/Φ和原witness不变。跨time Y-union的upper由subset继承，lower由包含的某个完整保留层的原AD给，详R22 time-restriction closure；不对任意Y/角/管子子族免费赋AD lower。若#S_*≥δ^(α+η)#Z（δ小后由上式成立），可取η_*=Lη≥C(α+η)，L正整数，且η_*≤C'(α+η)，使新allowed格δ^(η_* Z)包含于原格。所有损失，包括heavy窗常数与可能的1/γ，均明记于最终δ小幂。

原allowedρ未必是restriction后的newallowed。A的独立核查给如下付费解法：在f支取newallowed dyadic上邻尺度R，使ρ≤R≤Cδ^−η_*ρ。每个旧ρ-window J包含于其R-parent；对每个z₀∈S_*，**只用自身旧J内的times**给f(z₀)的σ-cluster。由(7)和δ-separated time upper，cluster在新的R-window内比例至少

    c δ^(α+η)ρ/R ≥ c'δ^(α+η+η_*).              (7a)

这不把不同旧J的拟合常数合并；named19.2(154)只要求每个z₀有一小比例cluster，不要求新parent中全部times靠同一常数。其ε_den取C(α+η)，实际支付(7a)。η_*≪µ(1−β)确保R²≤σ=ρ^(1+β)；R≥ρ≥δ^(1/3)、σ≤R也成立。η_*≪µ使R≤1。

σ若不在allowed格，可用named源引理的任意尺度statement；若实施其dyadic属性需向上取σ_+≤Cδ^−η_*σ，δ^−O(η_*)损失计入CW指数。η_*≪µβ保证σ_+≤ρ≤R，R²≤σ仍成立。增益(R/σ_+)^κ≥cδ^(η_*κ)ρ^(−βκ)，κ≤1将这个费用吸入δ^O(η_*)。因此本稿最终覆盖**任意原allowedρ**，没有免费跨窗合并。

整层restriction的平均shading由所有原incidences重新计数；原每层每点witness保留，不保证每条原T在新times上的density都保。若需逐管density，必须另用实际degree pruning及质量账；本稿两named引理接受的是完整配置与原witness，不附加逐管新密度假设，故未偷授该结论。

## 6. 无AFF的全source极小残差门槛

固定0<µ<1/4、0<β<1/4、0<ζ≤κ≤1及0<γ≤1；若原slab exponent更大，先降至1，以下γ指降后值。选α、η>0在这些参数后充分小，δ最后小。取任意原allowed ρ∈[δ^(1/4),δ^µ]，实施第5节网格费用。假设S及全部原同窗ordered pairs满足

    ||E(t,s)||≤ρ^(2+4β), t,s∈S∩J.              (8)

将ε=ρ^(2+4β)代(5)，固定M及δ小给每个保留窗J至少一支：

    diam f(S_J)≤σ 或 diam tildef(S_J)≤σ,
    σ=ρ^(1+β), ρ²≤σ≤ρ.                       (9)

这里C_Mρ^(1+2β)≤ρ^(1+β)由ρ≤δ^µ和β先固定支付，不藏成任意subpower。两分支的常数与Φ维数无关；没有假f/tildef仿射或高阶可微。

若存在一个tildef慢的保留窗，取真实z₀∈S_J。以**原完整配置**调用named Lemma19.4，cluster就是S_J；(7)提供原local density与absolute clock，源ε_den可取C(α+η)。由ρ≥δ^(1/4)≥δ^(1/3)、σ∈[ρ²,ρ]得

    C_CW(T)≥c δ^(C(α+η)/γ)ρ^(−βκ).            (10)

否则所有保留窗都为f慢。对完整整层restriction S_*调用named Lemma19.2，使用第5节newallowed R和每个time z₀自身旧ρ-window中的cluster，(154)比例为(7a)，而非跨新parent的100%。η_*<γ由参数次序保障。仍得(10)，常数调整吸收η_*、ε_den、allowed σ取整和固定维数费用。原T及其CW始终同一个，没有对子管族重新应用原upper。

因此不论各窗如何轮流二择，(8)均推出(10)。取α、η使C(α+η)/γ+η<µβζ/2（并满足全部named源小参数阈值），因为ρ≤δ^µ、κ≥ζ，(10)与原C_CW(T)≤δ^−η矛盾。高级source的存在常数不在本轮数值化；本结论是**相对于named19.2/19.4的条件应用**，不作其wholeproof新独证。

## 7. 原vector τ下界及真正改变的范围

在上述任意原allowed尺度上定义原raw supremum

    τ_ρ(S)=max(δ, ρ max_J max_(t,s∈S_J)||E(t,s)||).

第6节给

    τ_ρ(S)>ρ^(3+4β).                           (11)

这里δ不是下界的伪来源：β<1/4和ρ≥δ^(1/4)给δ≤ρ⁴<ρ^(3+4β)。所以τ若≤右边确会使全部E≤ρ^(2+4β)，与(10)矛盾。原f本尺度Lip及bounded d给τ≤C_MKρ²，但本稿只为比较记录此upper，不以它另造平稳或conditional time law。

(11)不需要AFF₃或nonquad，是对全部δ^α-dense整time删选的一个必要门槛；它没有把全部E小从g低维输出中提取出来。R24–26旧smallτ条件排除因此有一个不同前端检查，但其middle/large接口仍需whole-f AFF、nonquad、共同prior及各自的原质量，不因(11)解除。完整ordinary五维仍无strict>4新界。

## 8. 独立反攻、等价筛查与停止

全部ordered pairs是关键。若只在有向used图G上有E小，则(3)未必可用；密度本身不保证反向交，也不能以g+g_swap保原输出。严格两label校准：a(0)=0、a(1)=(1,0)，d(0)=0、d(1)=1，b(0)=b(1)=0，c=b−da。则E(1,0)=0而E(0,1)=(1,0)，f和tildef都不常数。它只否edge-only代数引理，不是完整配置反例。对任意dense g宣称(11)作用于g所见最大值的步骤没有证明。

旧raw矩阵rank一分类R64控制det(F_t−F_s)，不包含native兼容及E的两项；本稿不从其结论重调一个全称gain。旧E+swap在有AFF/二次准备下证明tildef慢，本稿改为f/tildef二择并分别付global/local责任，所得仅是这一代数加named-source应用；不认证首创/重大或新增数学结果ID。R27/28的wholematrix增长仍未支付。

停止本引理的阈值常数、√ε与τ指数微调；不以近常d或有理/光滑模型续轮。下一任务必须直接面对(11)之外的实际native输出或完整ordinary责任，不能假raw全pair小或免费标量化后再次调用本门槛。

## 9. 审查状态

root已实际全文读A15/B12、两formal各6节并核原式及应用；A/B各实际全文互读root9及对方稿、spec5/macro6/next6。已落实原ρ范围和γ先降至min(γ,1)的字面澄清，补明原ell/native AD/KT输入；无剩余必修数学项。正式记录见research/reviews/R0066_native_source_and_mass_review.md、R0066_two_slope_counterexample_review.md及R0066_root_integration_review.md。

有限证明与named-source条件应用分别通过内部审查，未经外部同行评审。source高级wholeproof未新独证；无实验替代证明，无新PDF或新ID，无ordinary维数增益，无major/novelty认证，Goal active。归档和远端同步另依实际验证，不由本节预认证。
