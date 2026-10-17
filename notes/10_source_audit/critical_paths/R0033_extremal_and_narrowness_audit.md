# R0033：极值 relative profiles 与 narrowness paths 独立重证

2026-10-17，A。Phase0 macro 后按 R33 phase1 spec 研究原 Proposition4.3（PDF48–50，提取2557–2676行），并核实际依赖 Lemma2.7/2.13、4.1/4.2。只编辑本稿，未操作Git。TCM001/ASM001/TEX001为既有原工具认证；2.15/2.16由B另审，GWZ2026 Theorem1.1保具名高级集合输入，不在本稿重证。

**结论：下面给出原4.3四项的完整极值论证，条件为文中明确列出的原 normalization/initial-horizon 输入。未发现需假设 inf/sup attained、bounded absolute f(0)、或重设 parent prior 的步骤。** 不能把此结论扩展至j3或说完整OAI4已认证。后续 tangent diagonal / finite-sample guard 不属于本稿主命题。

## 1. 实际对象与 inner/outer 两层量词

固定原 model j1/version1 或 j2/version2，以及S、η。每个 exact problem 有自己的 N₀-sequence、fixed正length L、homogeneous profile f、H(E) infimum；H的竞争者已允许任意 exact subsequences 和合法 inverse-subpower incidence restrictions。相关 f/h/width exponent 必须先在**固定 E** 的原 N₀→∞ 中形成，然后才让外层 i→∞。

输入列表：

1. profiles 非降且1-Lipschitz，C(d) 的 terminal slope cap 与 terminal/angular cap；2.3/2.5/2.7给合法 restrictions、homogenization/coarsening。
2. 原2.13的 terminal density equality、intermediate upper、known-at-parent-depth时的intermediate equality、whole-model normalization/lifting。§2逐项说明。
3. 原2.10准备true parents，保full trajectory assignment/prior/old floor，并使label known by自己的 endpoint observation。
4. 原2.16：H(E)≤L。其finite construction由B审，本稿不从原 four-dimensional set theorem一句话代替此输入。
5. TEX001：每fixed d₀<1统一的原3.5，h→h−e known atlas、厚度depth损≤Ce、C独立problem/L/complexity。

无bad problem时本命题条件为空。以下假设有H>0的C(d),d<1问题。length-one单位以Ñ=N₀^L实现；depth/horizon/density exponents均除L，angular原u=L ũ所以S/η保留。这里L是固定 exact problem 的常数，不是外层目标的极限值。

## 2. 2.13中哪些等式真正可用

在depth r的terminal-known atlas，令Z=Σ_c ωγ(c)qν_c∈[M,1]、新world权ω′_c=ωγ(c)qν_c/Z、prior=νγ(·|A_c)。world c中 t=t_c+qτ、y=y_c(t)+D_c z。新selectedmeasure是原assigned selectedmeasure除qν_c，仍是新productprior的restriction；总weightedmass=M/Z inverse-subpower。

固定chart/base后hidden transported bins与旧宽a_(r+s)/B的grid有bounded overlap。base Jacobian qJ_c / prior normalization qν_c，故within-world density factor是 **J_c/ν_c**，不带ω/Z。homogenize J_c/ν_c 后记其指数为a，则

`f_F(L−r)=f_E(L)−a`，`f_F(s)≥f_E(r+s)−a`。

第一个用chart在旧pL known及finite-list refinement，第二个只用arbitrary label refinement不增加未归一化density。于是

`f_F(L−r)−f_F(s)≤f_E(L)−f_E(r+s)`。                         (1)

若chart label还known by pr（prepared true parent确有此性质），对所有s≥0有intermediate equality；饱和时 `n_F(s)∼n_E(r+s)/n_E(r)`、`n_F(0)∼1`。单凭terminal-known atlas不能宣称这些earlier equalities。

new V′ bin在旧V里落radiusK N₀^{-u}球，因为∥D_c∥≤qK，需K个oldangular bins。先对同一个good旧measure求joint numerator，再变换/处理例外，得到new jointcap n_F(L−r)N₀^{-Su}，u≤η(L−r)。(1)保terminal cap C(d)，不需新的absolute f_F(0) bound。

version1用w′=(w−F(t,y))/a_r，其coefficient map虽有base-dependent quadratic subtraction，但对w-coefficients是triangular、constant Jacobian；version2保w、native P/a_r、B′=B/a_r。whole assigned trajectories保native/fulltime bounds；conditioning轻world删除后density仍piecewise constant、pieces谓词tempered。这里不condition on每条trajectory的成功时间。

child time/spatialJac/mass为 `q_cd=q q_d, J_cd=J_c J_d, m_cd=qν_c m′_d`。所以terminal child true floor由terminal equality lift；**intermediate** floor须上述intermediate equality，不能仅用upper。本稿nested path只穿prepared true parents，故具备该条件。任意known atlas在§3仅用于terminal lift。

## 3. 4.1 composition与coarsening的合法范围

从depth r、horizon h的known atlas normalize剩余F。取F true terminal systems的cost任意接近H(F)，terminal equality lift后

`H(E)≤h+H(F)`。                                                   (2)

若H_out是旧问题coarsen至r的terminal infimum，取其near-inf true systems，用2.10使label known by pr，再view为原E的true intermediate parents。剩余问题由原E∈C(d)经(1)仍属C(d)，故

`H(E)≤H_out+k(d)(L−r)`。                                         (3)

(3)本身不要求该coarsening∈C(d)，只要求它作为同data的合法homogeneous exact problem且存在near-inf系统；后文若要以k(d′) bound H_out，会另核coarsened terminal slope cap。coarsened angular条件来自2.7：fine joint upper/pure lower先求conditional，再sum finebins，最后乘coarse pure typical density；不是沿用old n(L)作coarse pure density。

所有competitors可在subsequences/restrictions上存在，这些本已列入H(E) infimum。对restriction后的E^R，只能有H(E^R)≥H(E)，但它仍属C(d)，因此其upper≤k(d)L。这两向界足以保maximizing；没有假H对restriction严格不变。

## 4. 极值的存在形式与0<k≤1

置d*=inf{d<1:∃E∈C(d),H(E)>0}、k(d)=sup_E H(E)/L。C(d)随d非降，k(d)非降、≤1，right limit k=lim_(d↓d*)k(d)存在。非空capclass由f非降给d≥0，故0≤d*<1。

任取bad E，选0<e<min(H(E),cL)，再取actual true terminal horizon h<H(E)+e/4。h≥H(E)>e，TEX适用；它在depth t给h−e known atlas，0<L−t≤Ce。(2)给剩余F的H(F)>3e/4，所以H(F)/(L−t)>3/(4C)。bad d可任意趋d*，在一个fixed d₀<1范围内同C可用，故k≥3/(4C)>0。e在各个fixedE内选，不需外层统一。

对任意length-one maximizing sequence E_i∈C(d_i)、d_i→d*、H_i→k，比较任意fixed d>d*且eventually d_i≤d，得limsup k(d_i)≤k(d)。令d↓d*，合k(d_i)≥H_i得k(d_i)→k。existence只要对d趋d*选near-sup competitor，不需attainment。以后所有新问题都用此squeeze，未调用“最优问题存在”。

## 5. Relative-profile rigidity：完整lower-secant反证

令g_i(x)=f_i(x)−f_i(0)，则g_i(0)=0、0≤g_i≤1、1-Lipschitz。Arzelà–Ascoli只作用g_i，不作用可能无界f_i(0)。取uniform subsequential limit g。

假设某interior[a,b]的secant slope<d*。若d*=0不可能（非降）；否则选0<d″<d*严格高于该slope。令r_i是f_i(x)−d″x在[a,b]的minimizer。比较x=b和a有fixed负gap，1-Lipschitz迫r_i−a≥c>0。对x∈[a,r_i]，minimizer给

`f_i(r_i)−f_i(x)≤d″(r_i−x)`。

对x<a，Lipschitz给 `≤r_i−x−(1−d″)(r_i−a)`。除以r_i−x≤r_i可取global terminal cap

`d_Gi=1−(1−d″)(r_i−a)/r_i<1`。                                (4)

Gi=coarsen(E_i,r_i) angular条件按§3支付，所以它是某C(d_Gi)问题。若H(Gi)>0，**固定该i**，对其TEX常数C_i,c_i选

`0<e<min(H(Gi),c_i r_i,(r_i−a)/C_i)`，

取actual h<H(Gi)+e/4。延伸到depth t_i有r_i−t_i≤C_i e<r_i−a，故t_i>a。normalize这known atlas的剩余F；只用(1)及[a,r_i]的局部cap即得F∈C(d″)。而(2)迫H(F)>3e/4>0，反d*。所以每足够大i的H(Gi)=0。

再对原E_i用(3)：H_i≤k(d_i)(1−r_i)。r_i≥a+c>0、k(d_i)→k>0，反H_i→k。因此g所有interior secants≥d*。continuous延至0/1，而endpoint cap给g(1)≤d*，故g(x)=d*x。任意uniformsubseq如此，得到整列sup|g_i−d*x|→0。这证明4.3(1)，未假绝对density compactness。

## 6. 一个actual node及coarse/remaining都maximizing

固定0<r<1，令ε_i↓0满足profile error/ε_i→0，并d*+ε_i<1。r_i=minimizer_{[0,r]}(f_i−(d*+ε_i)x)。比较r与r_i给ε_i(r−r_i)≤2profileerror，故r_i→r。

此**actual** r_i的coarsening有terminal cap d*+ε_i。记其H_out,i；(3)与class upper给

`H_i−k(d_i)(1−r_i)≤H_out,i≤k(d*+ε_i)r_i`。                    (5)

左右趋kr，故coarsened horizon/r_i→k。选其actual true systems h_i=H_out,i+o_i(1)，并经2.10准备。原剩余F_i由(2)及C(d_i) upper夹在

`H_i−h_i≤H(F_i)≤k(d_i)(1−r_i)`。

以**各自actual length** 1−r_i归一，relative horizon→k、d_i→d*；故remaining也是maximizing。coarse长度r_i同理。任意后续inverse-subpowerrestriction可用§3的H下界/classupper再夹，maximizing结论不因此丢失。

## 7. 有限grid的嵌套与earlier floors责任

对固定0=r⁰<r¹<…<rᵐ=1，逐次在新remaining maximizing sequence选择fraction θ=(r^{j+1}−r^j)/(1−r^j)，实际选择θ_i→θ。新node实际depth r_i^{j+1}=r_i^j+(1−r_i^j)θ_i→target。最后θ=1直接选整个remaining的near-inf true terminal system，不再调用interior minimizer。

每步cost先在其remaining length-one单位为k+o_i(1)，返回旧单位乘actual segment length l_i^j。故累计horizon=Σ_j(k+o_i(1))l_i^j→kr^j，各段以自身正length归一后趋k。有限次outer subsequence与每fixedi的exact subsequences可共同保留；没有一次(i,N₀)混合极限来创建不存在的exact system。

每parent保full assignment、νγ conditioned on该**full**assignment、own selected incidence witness及true floor。child是该固定conditionalprior的restriction，whole-timefits/timepartitions/Jacobians按2.13 compose。final path可再与各层selected events相交，但其质量无须仍达到每个earlier chart floor；后续计数若用该floor须用earlier frozen witness，不得换成final path mass。

标签可记录whole history。parent label known by its endpoint，较fine observation可列parent；固定parent与exactbase后 transported hiddenbins仅bounded overlap，再组合child short list。因此cumulative true layer在原actualendpoint也known。intermediate lifts正是§2的equality-case，非只terminal-known父的一般upper-case。这证明4.3(2)的实际geometry/prior部分。

## 8. Narrowness目标：sup/inf都无需attained

version2定义每个fixed maximizing sequence的ω：所有terminal true systems、relative horizons趋k、可用outer subseq及各fixedi的exact subseq/restrictions、homogeneous narrowness exponent的attainable limsup之sup。每个fixedi的width exponent有限，由其tempered widths给出；随outer i可以无界。非负性来自J≤Kq²。ℓ=inf_sequencesω，可能∞。

对任一new maximizing sequence，ω≥ℓ。finiteℓ时，从sup定义可选某attainable limsup>ℓ−ζ/2，再取outer subseq使选中systems的relative width≥ℓ−ζ eventually，relative horizon仍趋k。若ω=∞，同样可以选高于该finite threshold；无须ω attained。

先从inf定义选base sequence ω_base≤ℓ+ζ。其任何subsequence/restriction上新构造的terminal systems，只要relative horizon趋k，都在原ω_base的competitor范围，故其terminal width limsup≤ω_base。base的这个upper不能在换一个任意maximizing sequence后沿用；本构造始终在所选base及其subseq内lift。

## 9. Finiteℓ：用terminal upper减其余段lower

在§7每个新coarsened/remaining maximizing sequence上，包括最后整段，用§8选true systems，其relative width u_i^j≥ℓ−ζ eventually。定义original units增量a_i^j=l_i^j u_i^j。determinant/time multiplication给精确additivity：`log_N(q_cd²/J_cd)=log_N(q_c²/J_c)+log_N(q_d²/J_d)`，不要求spatial axes平行。

最终terminal system的cumulative horizon趋k，所以A_i=Σ_j a_i^j满足limsupA_i≤ℓ+ζ。对任意segment collection with actual total lengthl_i，lower≥(ℓ−ζ)l_i；减其complement lower又给upper≤ℓ+ζ−(ℓ−ζ)(1−l_i)+o_i(1)。因此

`ℓ l_i−ζ l_i≤Σ_collection a_i^j≤ℓ l_i+2ζ+o_i(1)`。             (6)

该式同时控制任意node cumulative和相邻increment；l_i趋对应targetlength、ℓ有限，故可换成limiting linear value加o_i(1)。O(ζ)不需付grid点数，因为actual lengths总和1。原4.3(3)成立，无假定某limiting E实现目标，也未把近最优horizon换成exact attainedk。

## 10. Infiniteℓ：合法outer competitor diagonal

若ℓ=∞则每个maximizing sequence的ω=∞。对整数M，选一个attainable系统列，其width limsup>2M、horizon→k；在该列中选足够大的outer index，width≥M且horizon误差≤1/M，再令所选indices严格增加。每个所选index内部使用的仍是已经完成其原N₀极限的actual exact system。得到outer subseq上width→∞，不把innerN₀选择替代它。

对有限grid重复上述选择，每previous layer的原exponent/witness保留，在newremaining sequence选diverging relative widths。每个targetsegment length有fixed正极限，故original-unit增量也→∞；对vanishing-length段不能免费推此结论，本命题不作该要求。这证明4.3(4)。

## 11. 反攻结果、残余与停止

已排除的非法捷径：global coarsenedcap只用原endpointcap而不查minimizer；对arbitrary terminal-known parent套earlier equality；f(0)绝对compactness；假sup/inf attained；restriction后声称H不变；后续selection以final path mass代earlier true witness；normalization乘limiting长度；ℓ∞用一条sample diagonal而非outer competitor subseq；把version2 width公式与generic j3 AFF混用。

本稿的critical极值部分未发现严格反例或未付数学步骤。最终内部验收还须并读root整合及B的2.15/2.16/normalization审查；若该finite高级链仅有named输入则必须保留。原4.5–4.6 finiteguard与4.7prepared tangent laws以及后续geometric exclusions未因本稿而认证。研究目标一般/五维Kakeya保持open，六维17/4仍条件，未经外部同行评审，无新颖性/重大性声明。
