# R0043：原§18操作、原质量与fine-PW闭包审计

2026-10-17，A（audit_four_dimensional）。运行context.py并读GOAL/STATE/ROADMAP/registry78/latestR42/AGENTS、R43 spec及R42 nextspec。实际全文读versioned WZ2609.22035v1 Def17.1–17.4、Prop18.2全部六步及18.1升级到(145)之后的consistency完成；对照原(19)/(20)、Obs3.2–3.4。必要页PDF70/72已render实看，未只凭抽取上标。本文只编辑分配文件，不Git、不另开代理。

本轮主问题是原§18的额外PW条件能否闭合，不是再证明已付的平均BS形式，也不是宣布五维κ≤ζ。**正面结论：共同横移平均确实能保whole-family fine-PW到coarse weighted law；再用原AD的双边fiber计数，可保实际unweighted coarse law。原共同whole-clock parent的体积与质量也抵消。** 以下完整付出这些有限步骤，并列原§18相应位置、尺度及递归责任。高级Lemmas4.2/5.3等原几何提取仍按具名原输入，不以本次PW审计认证它们的全部proof；未经外部同行评审，不作新颖/重大声明。

## 1. 命题、全部law与停止条件

原Def17.1（PDF65，text3354–3360）是无权joint(d−1)-AD、CW及**平均**δ^η shading的全称命题。加强类必须用实际whole-tube uniform counting probability

    ν_T=N^(−1) Σ_{T∈T} δ_T，N=#T，

或另付与该law的双边subpower比较。仅要求“存在某个概率ν”不够：它可以把绝大多数实际counted tubes忽略，无法支持原无权Kd递归。以下有限lemma允许任意权，但应用到source时每次都回到上述真实无权law。

固定整数d≥2、固定presentation指数A，P(E)=(1+E)^A。设对每个半代数S、每个E≥1和0<λ≤1，

    ν{T:q_T(S)≥λ}≤C0 P(E)|S| λ^(−d),
    q_T(S)=|T∩S|/|T|。                               (PW)

P必须对所有系数统一；不限制coefficient height。目标是原实际coarsening/parent/refinement后保持同一个A，C0只付可显式吸收的subpower。独立反攻包括tinyλ、任意相关权、parent mass、coarse无权重计数、短clock、不同frame、输出小于原尺度的loss。若只得N_ρS体积而未证明它可支付，不叫反例；若需另加all-coarse PW公设，不叫原命题闭包。

## 2. 受限质量平均式：必须先固定坏事件

对任何原index集合I，a=ν(I)，tail由(PW)和总质量给

    ν(I∩{q_T(S)≥s})≤min(a,C0P(E)|S|s^(−d))。

精确layer-cake（d>1）得

    ∫_I q_T(S)dν(T)
      ≤c_d [C0P(E)|S|]^(1/d) a^(1−1/d)。           (A)

体积右端大于a时用平凡上界即可，a=0亦平凡。这里没有把I归一化再漏掉a因子；I可以由以后选出的coarse high-visit事件决定，与任何原角、位置、shading相关。

只对整个ν的mean作普通Markov会丢掉正确的λ指数，不能代替(A)。后面每次先固定coarse坏事件的preimage I，再逐个共同平移使用(A)。

## 3. fine到coarse：共同translation kernel的完整证明

暂在原(19)共同clock t∈[−1,1]上写graph cylinders

    T_i^δ={(c_i(t)+x,t):|x|≤δ}。

粗管U_{b(i)}^ρ具有同一clock、截面半径ρ，且对所有t有|c_i(t)−c_{b(i)}(t)|≤C_dρ；δ≤ρ。dyadic参数D_ρ恰满足此条件。取共同u均匀于B(0,Lρ)⊂R^(d−1)，L足够大。对任意x∈B(c_b(t),ρ)，所有v∈B(c_i(t),δ)均满足|x−v|≤Lρ。故卷积kernel满足

    [1_{B(Lρ)}/|B(Lρ)|]*[1_{B(δ)}/|B(δ)|](x−c_i(t))
       ≥c_d ρ^(−d+1) 1_{B(c_b(t),ρ)}(x)。

对t及S积分，得到逐fine index的点态比较

    q_{U_b^ρ}(S)≤C_d E_u q_{T_i^δ}(S−(u,0))。     (B)

这不要求所有parents有同一axis，不给每parent另选S_i：u的概率law对所有indices相同，且每个测试确实是同一个S−(u,0)。半代数S的volume和presentation次数总和在平移下不变；有限tube与半代数S保证所有积分可测。无ρ/δ费用，也不删除clock端段。

设μ=b_*ν为coarse pushforward，H={b:q_{U_b^ρ}(S)≥λ}，I=b^(−1)(H)，a=μ(H)。把(B)对I积分，并对每个共同u用(A)：

    λa≤C_d E_u ∫_I q_{T_i^δ}(S−(u,0))dν
       ≤C_d[C0P(E)|S|]^(1/d)a^(1−1/d)。

消去a可得

    μ{b:q_{U_b^ρ}(S)≥λ}≤C_d C0P(E)|S|λ^(−d)。    (C)

所以**whole-family fine-PW足够保weighted coarse PW**。N_ρS的直接外包络可能有巨大体积，但不是这里必须走的证明。这也不是从angle Frostman再次调用BS：证明只用已给的(PW)，平行族同样适用。

原Def3.6 dyadic tube截面不是严格ball：在固定clock内，它被以参数中心为轴的C_dρ-cylinder覆盖，也包含c_dρ截面。用同样kernel上界其normalized indicator即可得到(B)；选粗轴/参数代表时O(ρ)误差只增加L的固定常数。所有结果仍是same-clock，不声称任意旋转后延长新clock的整管免费闭合。

## 4. 无权coarse counting law：双边fiber确切费用

原Def3.9(20)（PDF17，text860–864）给每个occupied coarse parent B∈D_ρT：

    K^(−1)(ρ/δ)^(d−1)≤n_B=#T[B]≤K(ρ/δ)^(d−1)。

设M=#D_ρT。coarse pushforward权是n_B/N，实际uniform coarse权是1/M。因为N/M是所有n_B的平均值，

    (1/M)/(n_B/N)=(N/M)/n_B≤K²。

反向比较也≤K²。因此(C)给实际无权coarse PW常数至多C_d C0K²，而不是免费把incidence权当counting权。此证明只用occupied fiber双边计数，若只有upper或只知平均parentmass，不能照抄。

原Step2–3的point-line uniformization（PDF68–69，(106)前，text3537–3581）真实提供了后来T′的这项责任：每条active fine tube的|Y′(T)|约相同，且每个occupiedρ-parent的Σ_{T∈T′[B]}|Y′(T)|约相同，由MX′(1,ρ,ρ)表出。再用原总dense incidence及原AD upper/lower得到(3566)–(3572)的T′为(d−1,δ_ℓ^(−2η_ℓ))-AD。不能仅以Y′保大incidence mass便断言任意subset T′继承原AD lower；此处source另付了uniformization。

## 5. whole-clock共同parent与coarse-parent的合成

原Obs3.2的实际map为

    ψ_B(x,t)=((x−b−at)/τ,t)。

取原τ-parent B，p=ν_T(T[B])。这里使用source的固定有界joint-parameter chart（或直接假N≤C_dKδ^(−d+1)）；原Obs3.4(22)也明用这一全局管数。仅有局部r≤1的Def3.9 AD、却允许无界空间许多远隔copies，并不推出N的上界。下述取消只在该bounded setup内。由原AD和N∈[K^(−1)δ^(−d+1),C_dKδ^(−d+1)]有p≥c_dK^(−2)τ^(d−1)。该map只缩transverse，不缩clock；新S′的pullback体积为τ^(d−1)|S′|，占比不变，复杂度不变。因此conditional uniform fine parent的PW常数

    C_parent≤C_d C0 τ^(d−1)/p≤C_d C0K²。          (D)

再粗化至ρ并改uniform coarse law付另一个K²；或先粗化再选同一parent，给

    C_new≤C_d C0K^4，δ_new=ρ/τ。             (E)

这是原Obs3.2–3.4实际whole-clock操作，**没有q^(−4)**。若另把clock截成q再归一化，原R42公式仍是C0 r^4/(pq^4)，不能把(E)推广到那种操作。

bounded-parameter责任不能略去：若把一个parallel transverse满网复制L份到远隔位置，局部AD常数仍固定，global visit law的PW常数可约为1/L；选一个unit parent后PW常数却为常数。故无界多copy的泛命题不能保C0K²取消，必须留真实p。该例只校准有限lemma的bounded范围，不反source固定box的应用。

若只知所有marks在固定box而whole T还可能含未见管，也有诚实替代：平均density≥λ0使active tube数至少cλ0N；所有active axes在固定有界参数chart中，局部AD给其数至多C_dKδ^(−d+1)。于是N≤C_dKλ0^(−1)δ^(−d+1)，(D)/(E)分别多付λ0^(−1)。actual λ0≥δ^{O(η)}时仍只多一个已量化δ^{−O(η)}，无需谎称未见管没有质量。这个替代不改变无限散布的泛命题反攻。

原文字在PDF72说“rotation使parent竖直”；PW回传可统一采用精确ψ_B而非把旋转后的短投影段延长为全clock。ψ_B将该parent内所有axes变成有界slope，同时保持affine planes、incidences和各尺度邻近关系；在grain记号中仍可对transverse坐标作共同有界旋转/有限chart选择。plane与t=constant的ℓ−1维截面仍可编码成horizontal graph。不需要每管另换frame，也没有额外物理time裁切；若另作真实spacetime旋转，必须只传其实际tube image，不能免费延长它。

## 6. Prop18.2真实操作账本：PDF67–74

| 原位置 | whole-family/prior操作 | PW费用与marks责任 |
| --- | --- | --- |
| (104)–(105)，PDF67–68，text3489–3502 | 从新κ_PW的失败选uniform T与平均dense Y；不选角分离祖先 | 起点须本来在加强类；不能用旧κ的failure sequence后补PW |
| Step1，PDF68，text3508–3526 | 按point multiplicity/ℓ-plane浓度删shading得Y0 | whole T不变，PW不变；只知平均密度≥δ^{O(η)}δ_ℓ^{η_ℓ}，不是每管dense |
| ℓ=1排除，text3527–3536 | T[2T_{δ1}]共同parent ψ；必要时Kd调用 | (D)配AD双边质量；2-parent为固定数邻接parent只付固定常数。保原clock，不补未见端段 |
| Step2–3，PDF68–69，text3537–3572 | X→X′删incidences，再取active T′ | 不逐层normalize incidence law。整体T′一次restriction质量至少原平均dense incidence，PW先付p_{T′}^{−1}；source另证AD以备(E) |
| (106)，text3573–3581 | Y′(Tρ)=DρU(T′[Tρ],Y′) | 改shading并coarse；(C)保whole coarse pushforward，§4改真实无权law；不要以Y′长度作为whole-tube先验 |
| (107)–(112)，PDF69–70 | 两次Kd：whole Tρ与共同parent T[Tρ] | 原coarse uniform law付C0K²；parent付(D)。须用新κ_PW，所有其它原AD/CW/density条件照旧付 |
| (113)，text3601–3603 | 两尺度extremal multiplicity恢复 | 这是前述两次调用加原uniformity，未新生成tube prior；PW费用不会再逐point相乘 |
| Step5 (114)–(126)，PDF70–72 | ℓ-tuple、slab/point refinements生成E1和Y′′ | 这些改变marks不改变T′whole geometry。总体loss按sourceδ_ℓ^{O(η_ℓ)}，不能在J约1/η层每次再条件化whole prior |
| PDF72 text3754–3758 | 取τ=√δ_ℓ parent、ρ=δ_ℓ粗管，ψ得到δ̃=√δ_ℓ | 对T′用(E)；实际新family是uniform D_{δ_ℓ}(T′)[T_{√δ_ℓ}]的image |
| Step6 (127)–(140)，PDF72–74 | 横层/AD fibers/时间与x-y点删选 | 这是shading/point配置组织；保同一whole T̃可不再付PW。若删无用tubes需再付其真实质量，不能代入点质量 |

Step4的average→parent不能偷换成“每parent原shading dense”。Step1已使每个active p的fine/coarse incident-fiber数在p间可比，所以对应parent multiplicity可比；由原总平均dense shading及AD parent计数先选一个dense代表parent调用Kd，再把同尺度multiplicity估计传回其它parents。whole coarse family则由整体平均dense调用。新增PW对每parent都已由(D)支付，并不使这个旧平均责任消失。

## 7. 原尺度费用：不能只写“都是subpower”

统一K=δ^(−η)、C0≤δ^(−η)时，(E)至多C_d δ^(−5η)。若δ_new=ρ/τ≤δ^χ且χ>0已固定，则

    C_new≤C_d δ_new^(−5η/χ)。                     (F)

因此先固定target新loss及χ，再取η≪χ·target_loss。δ_new接近1时(F)不能用；原递归调用本来也必须把旧AD/CW的δ^(−O(η))改成新尺度小损失。PW只增加固定O_d倍，不引入新的ρ/δ幂。

原(107)明写ρ^{ε1/2}≤δ^η，(109)另要求δ/ρ充分小（text3583–3589）。这些不是给任意ρ无条件使用Kd的许可。近endpoint尺度需原平凡计数吸收，非平凡调用须先留relative-mesh buffer，且把η按新增固定倍缩小。不能靠事后称“subpower”越过source层级。

Prop18.2最终τ=√δ_ℓ、ρ=δ_ℓ时，Step3后的K′=δ_ℓ^(−O(η_ℓ))，active T′ mass≥δ^{O(η)}δ_ℓ^{O(η_ℓ)}。故从原uniform T算起，(E)给C_final≤δ^{−O(η)}δ_ℓ^{−O(η_ℓ)}。原选择δ^η≥δ_ℓ^{η_ℓ}（text3571–3572）可把前者吸收，转新δ̃=√δ_ℓ得到C_final≤δ̃^{−O(η_ℓ)}；原几何输出η̃=Cη_ℓ/η_{ℓ−1}更宽，增加其固定常数即可。

可把source模糊尺度选择落实为无循环的power schedule：取阈值ϱ_j=δ^{a_j}，0<a_1≪…≪a_{d−1}<η0，使a_jη_j/η_{j−1}≫a_{j−1}；再取原η≪min_j a_jη_j及所有Kd允许loss。实际δ_ℓ≤ϱ_ℓ保证logδ_ℓ/logδ≥a_ℓ，故原δ-loss可按固定比率吸收到δ_ℓ-loss，且δ̃≤δ^{a_ℓ/2}→0。所有a_j在取δ前固定；不依赖之后某个未知countersequence来选择η。此只是给PW费用一个合法预留，不重新认证source其它几何参数的全部最佳模数。

## 8. Prop18.1升级：PDF74–76至(145)之后

### 8.1 AD结构与higher planar grains

text3880–3930调用Lemma5.3对每个Y_z做结构提取。按(ρ,τ) pigeonhole和Z1/Y′删选，marks平均loss为δ^{2η}(ρ/τ)^ζ；它不把T本身换成按point-incidence加权的概率。选一个Tτ，实际T1=ψ_{Tτ}(DρT[Tτ])，仍恰是(E)的whole-clock、uniform coarse family。source有τ/ρ≥δ^(−χ(ζ))，所以δ1≤δ^{χ(ζ)}，选η≪χ(ζ)·target_loss即可使用(F)。

每个z/point的φ_{y,τ}仅用于描述horizontal AD结构；whole tube family真正施加的是所选同一个ψ_{Tτ}，不能把前者误当每tube各自的物理变换后还用同一PW测试。若Y1记号保留了原未删Y，或采用已删Y′，whole T1的PW证明相同；但(141)/(142)及dense shading必须用相应真实marks，不靠PW补这一几何责任。

若γ_j小而增加grain维，最多增加d次；下一次原η需相对下一ζ/χ足够小。新增PW常数仅是前一C0乘固定AD幂，次数由d界定，presentation exponent A从未被提升。

### 8.2 slab-Frostman升级

text3932–3987重做linear-points分类、(144)浓度删选，再用Prop18.2型parent/coarse操作；若ℓ′下降，最多d次。只改变marks时whole PW不变；出现真实tube family替换时仍逐次(E)。不能把Φ_q未使用角的AD误认为原used-angle下界；PW处理whole T，与此slab提取各自独立。

原参数序列要求10η̃_{ℓ′}/ε_j≤g(η̃_{ℓ′−1})并使δ′<h(η′,γ′)。PW固定幂费用可先吸收进几何η′的常数，随后把原允许g/h函数收紧；有限次数、没有复杂度指数递归，故没有额外量词循环。这个说法依赖原source确实选择相对尺度有正power gap，不能推到任意微小scale改动。

### 8.3 consistency的最后厚化

(145)及text3996–4020比较两种horizontal表示，先得到f2†=fj1+fj2f1†+O(δ′^{1−5η′/ε_j})，再厚化到r=δ′^{1−5η′/ε_j}并调整E′。这里whole tubes若用D_rT′的uniform coarse family，正是§3–4的正向结论；调整参数O(r)也可由同一kernel支配，固定数量mesh邻居的多对一比较须保留，不能任意重权。新PW≤C C0K²，在新mesh r上只把loss除以1−5η′/ε_j；原η′≪ε_j已预留。

## 9. 原页尺度记号与clock范围的审计限度

PDF70实图写Δ_J约δ_ℓ，PDF72在“p∈E′_{p_j,θ_j}”的同一j=J叙述却又写Δ_j=δ̃=√δ_ℓ；这不是抽取上标错。本文PW证明只使用明确写出的最终family D_{δ_ℓ}T′[T_{√δ_ℓ}]，不把两尺度免费等同。若复写完整grain几何，应在hierarchy中取Δ_j约δ̃的中间层、重新核后续density，或校正索引；该旧几何记号问题本身既不是PW coarsening反例，也不是四维主结论反驳。

source无真实short-clock归一化是本次闭包的重要范围。所有T都按(19)共享[−1,1]；point cubes和Y′的短marks不意味着tube whole interval被裁短。共同clock-preserving shear足以执行所列whole-tube operations。本文不额外证明任意spacetime rotation后选新unit interval、任意time-dependent frame或projective reconstruction的PW闭包。

## 10. κ递归、排重及本轮真实出口

把原K_d替成K_{d,PW}必须从**加强类本身**的failure sequence开始。若κ_PW是成立指数的infimum，任意目标ε先选一个成立κ′<κ_PW+ε/2，并用其ε/2估计，即得所需κ_PW精度；这是原infimum端点的合法调用，不借旧κ。每次coarse/parent输入都需原AD/CW、真实平均density及本文已付的uniform PW，方可在(107)/(109)重用同一个κ_PW。初始一般K如何进入jointAD/CW/PW加强类仍另欠，不由BS一次送出。

新增信息不是把all-scale方向Frostman再调用BS：§3的推导只用fine-PW并保相同presentation指数，可覆盖并不满足angle Frostman的law。但若实际所选ancestor及全部输出本就保full方向law，则这一应用仍可能完全重复旧角cap；不能凭抽象类较宽就宣布新的高维机制。

在原§18几何提取及其具名工具的范围内，**PW这一额外uniform-law不再被fine→coarse的N_ρS表面障碍挡住；所列whole-clock操作和有限递归的PW费用可支付**。本稿没有单独从零认证原§18完整高级几何proof，也没有构造actual半代数S使原质量/marks/复杂度留出strictκ saving。即使最终加强类闭包被整合通过，五维κ≤ζ、其它mixed、一般到sticky及Hausdorff仍未解决；不以本次有限接口完成长期Goal，不新增重大性声明。
