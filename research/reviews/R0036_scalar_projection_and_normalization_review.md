# R0036：完整 scalar projection 与无穷窄度分支独立审查

2026-10-17。A正式review。已实际读 root `notes/10_source_audit/unbounded_narrowness/R0036_unbounded_narrowness_full_proof.md` §§1–17（237行）和 B `R0036_native_graphs_and_actual_recovery_audit.md` §§1–11（155行），并与原8.2及§10.1–10.7的PDF/提取文本对应。自己的8.2/normalization稿不计为对自己的独立审查，本review对root全稿及B后半给独立逐步判定。

**通过，可归档为原Theorem8.2与Prop10.1在明确列明输入下的内部复现。** 本次全文审查未发现必须修补的原law/分母/actual-encoding缺口或保全部原假设的反例。未经外部同行评审；不认证正有限窄度、完整2.17/finite读出、OpenAI整篇证明、新GWZ2026全proof或无条件高维界，不认证新颖/重大性。

## 1. 命题完整性与closure排重

root §1覆盖真正目标：原version2 CRP setup，d_i→d<1、H→k>0，假global optimizedℓ=∞；构造fixed positive c′、timeexponent→0、原p1-known actual atlas反extremality。8.2不是只输出一条好trajectory：它给dense原active质量、disjoint whole assignments、fullunit-time moving interval/quadratic fit、每label cadβ/K与optionalβ∼1。prop10.1不是只证明normal近parallel：还付center motion、mass/area balance、scalar occupied support、originalknowledge与actualcoverage。

已发表WZ/CV可作已知具名定理，不机械要求全重证。新GWZ2026及原OAI4其余责任仍明确保留。完整∞分支不由ISO/AIM一步推出，也不蕴含finiteℓ；root没有把新名称当新数学方向或以本轮清除高维条件。

## 2. 8.2 smoothing：任意weights、µ_act和额外坐标

root §§3–5的mark对象是整tag×σ-timebin的**原µ_act质量**，不用每条原trajectory逐管marked。未marked成本≤Σω_jσ/K1；µ_act≤Kνdt使marked law仍dense。tag只round y/x的五coeff，内部j保留；额外坐标可以与全部几何相关，返回时仍按原tag条件prior恢复，无伪独立或伪密度。tinyω_j不违反tempered upper-density：noise density≤σ^{-5}，tag数poly，定义无ω_j inverse lower。

exact-base cap独立重算：所有eligible tags的原active量落入K个扩大(σ,σ,p)格；markthreshold给Σω_j≤Kσcp^d，再乘y-interceptnoise densityσ^{-1}。slopenoise独立性仅在取interceptdensity upper后使用，合法给min(1,ρ/σ)，没有在exact-y条件化后免费假独立。optional原角cap只在u<min(u1,M)的小正范围继承，已足够C(d)。terminal noisy support来自原occupied cells的K邻格，不是cap推出support。

同一marked law的terminal density upper与support upper夹出n(s)∼ca^d；intermediate upper给f(s)−f(r)≤d(s−r)。这无需原prior AD lower。root最后按B建议明确d<0的独立排除：用**p=1的unit-width cap**，每basecell仅K个unit xbins，basecell数≤terminal triplecell数，故总mass≤Ka^{-d}，与dense矛盾；terminal a-cap乘terminal support本身会使a幂相消，不能单独证d≥0。已实读该最终补丁，正确。

## 3. 8.2 crop、world density与回原质量

无角时joint-profile maximizer的三界正确：R=(1−d)/2使在(s,0)值C0+Rs，noise upper给r0接近s、u0≤M/(1−ε)及f(r0,u0)≤f(s,0)+εU。U=4(M+s+1)确保u0+r0≤U；optimality分别给terminal cap1−R与positive角ε。

crop world按prior p_C加权，within-world priorν(.|C)，不是给每tiny C质量1后求uniform平均。给exactbase/oldvelocitybin时interceptcrop只有bounded options，所以f′(r)=f(r,u0)+u0−α的Jacobian/conditional分母均正确。lift的active floor确是

`p_C N^{-f′(r0)}(β/G)=βN^{-f(r0,u0)}`，

没有遗留p_C^{-1}或G^{-1}。Cor6.9每fixed tolerance先给exact subsequence，ε及horizon再慢降；不假inf attained。误差N^{-r0}与mass的N^{-εU}在慢对角都仅K。

β≥σ/K的证明用**原true active floor**和noise slope gain，q≥1/K把packet velocity宽度降为Kβ。optionalβ的任何fixed-power缺损都与一小正u的角因子矛盾。F适配norm的Remez数据来自mass除base cap的inverse-subpower投影面积；unit-time外推因q≥1/K只付K，不把fixed-power短时见证直接延unit。

共同jitter回收的次序是关键且已支付：先由全部noisy labels的disjoint floors得固定Σca^dβ≤K，再Fubini固定**一个共同u**保globaldensity；此时不能追认各label旧floor。对selectedtag赋wholelabel、undo共同∆y/∆x、用β≥σ/K与σ′≪σa²付unrounding；恢复每marked-bin全部原active part，最后按固定Σnumerator预算删light restored labels，再dyadic β同质化。这给原µ_act的逐label新floor。raw arbitrary-µ_act无需R35那种反传weightedcap的lowerdensity假设，因为本构造直接用其mass做mark。

## 4. 10.1–10.3原nested objects与fulltime知识

root §§6–8按own-depth true normalization取得原n_i(0)∼1，再CRP relativeprofile给f_i(r)→dr。globalℓ∞在normalized maximizing segments上给实际α2−α1→∞，不是任意挑一个narrow chart。full-layer priorsν(Qj)∼n(rj)qj²gj和earlier assignments保持，后删不把它们追认为current floors。

pairedtime原law有Jensen质量≥p_path²；异常entries在first-label计数**之前**删。first label数≤K0/[n(r2)q2²g2]，失败角的velocity intersection ball半径K0N0^{-u}，原p1列表只K0 bins。用permitted good p0 ancestors积分pure density，再用full first-label strip面积K0g2，恰消g2。失败质量指数为 `−Su/2+(d+2k)s2+o_i+o_N<−Su/4+o`，相对paired inverse-subpower为零。不存在把异常质量乘巨大label数的错误。

固定t0后C-label包含normal、normal-center intercept、normal-center velocity。原全time affine trajectory bounds使late Q2能恢复三者至Kg2N0^u=o(g_C)，故原p1可知的是**完整中心运动**，不是只有normal。g_C/g1小及同V比较给10.8；finite slicing/bin/角tests的tempered责任保留，分析masks不必编码。

C-normalization的worldweightsωγν(C)/W与conditionalprior精确相消。terminal equality与intermediate upper只共享g_C/ν(C)因子；不假f′(0)有界。H(E)≤H(E′)只用terminal true系统可lift，intermediate不用lower。A′小bi系统饱和后

`ν(A)/J_A∼n_i(1)n′_i(b_i)/n′_i(1)`，

所以absolute shift取消，指数−db_i+o_i。root明确这是two-limit K，不是fixed-i actualK0。A own-depth知识通过原C-list、hidden-coarse-bin和primed列表组合；largest tangent width lower用原angular/list实际排球，不从det upper免费推出。

## 5. B后半：native graphs与projected cap/support独立核

root §§9–11与B §§2–6已实读，并对照原8657–8847。gain/matching容差/δ/c′先固定，complexitybound先于N0，analysisK与actualKpath分开。两个旧witness分别用于whole-domain计数与core norm；都在tiny A/projectedcell条件化前冻结，不伪造条件floor。

native true P在z=Bw的discriminant D=P_z²−2P_zzP与z无关。large-curvature用affine center近似actualz，small-curvature才选simple root与positive D；tinyleadingcoeff的unused farroot不被宣称bounded。nativeP*复合误差由其一/二阶hidden界的exact Taylor给Ka_fit，ASM先给G及∇G的绝对K界，随后才做support比较，未加coefficient-height lower。

projected λ_A始终除q_Aν(A)，RA=ωγq_Aν(A)总和≤1；每residual可由global平均选dense A。density部分按∥D_A^TeZ∥/q_A的真实lower取面积≤K0J_Ab，再乘JA/νA的two-limit balance。角cap只在预删good old entries求和，未让exception乘tiny角因子。

support部分独立使用whole Q1 domains：所有兼容label的**完整**旧witness都在同一movingbox面积Kq1²g1，zero-depth cap+disjointness给L1≤K/n(r1)≤Ka^{-d}。不需条件于A的witnessfloor。坐标比较先减共同y1′∆t，normal误差为K(g1 qAσ+g_C)；除q1g1后是 `K[qAσ/q1+g_C/(q1g1)]`。time项g1已取消，所以fixed M与α2−α1→∞足够，不要求任意小g1有fixed lower。乘每label K graphs给同一个λ_A的terminal occupiedsupport，cap与support没有混用。

## 6. 每residual候选、raw posterior与actual atlas

root §§12–15和B §§7–10独立核过。fresh8.2输入固定ν(.|A)、c=1、rawcap/support、terminal角与dense mass均已核，不把subprobability按currentmass免费归一。optionalβ∼1与boundedcenter使普通F coefficients K。greedy每插入countedmass≥qAνA a^dN^{-δ}，由duration≤qA移走wholeprior≥νA a^dN^{-δ}，故次数≤N^δa^{-d}。若覆盖比例趋0，every-substantial-residual又产生eligible test反终止，才得fixedfraction覆盖；单个inverse-subpower成功没有冒充coverage。

Π的base measure是未归一m_c=O_*µ_c，两marginals正是µ_c。bad pairs只在global RA预算找b_A≥qAνA/K后归一，marginals≤Kλ_A。individual index-base cap来自graph只容N^{Cδ}个x_a bins；uniformρ_f是Cor3.4的**参考law**，由listcount≤N^δa^{-d}推出a^d≤N^δρ_f，不假posterior uniform或minposterior lower。

K范围resize、norm upper、value discrepancy、listcount、density losses均为R=a^{-1}的小幂，Cδ/s1<ε/2；coefficientgap给normgapR^{-2θ}/K>R^{-ε}。Cor3.4允许两color相关，适用确切原pairlaw。good coefficient-bin pairs再按aggregate posterior最大邻域给bounded列表，最后compose actual A-list，未知A不交给selector。

P_new=P*−binnedF不含新hidden项，native derivative/curvature直接继承；value的fixed positive buffer吃掉analysisK，未把N^δ当actualslack。whole trajectory assignment与每incidence selectedtests/failure分开，failure不进任何posteriorlist。orderedtests、逐test fixed-degree time elimination、merge/priority有限表给事先polynomialcomplexity；不对N-dependent巨型Boolean式误用fixed-format QE。4.12使用原µ_ref与未归一µ_c、jointTV而非normalizedposteriors，errorO(N0^{-1})小于p_path/logN0，实际coverage和列表/geometry全达predeclaredexclusion。

## 7. 最后ν_c分母与真正10.19矛盾

root §16与B §11明确newlabel c=(A,b)的fullν_c通常≠ν(A)，且无parent truefloor。newworldweightsωγqAν_c/Z，Z≥actualsuccess≥p_path/logN0；selected mass与Z^{-1}是actualsubpower。terminal p1 knowledge给n′(1−c′)∼n(1)JA/ν_c，intermediate只有≤n(c′+r)JA/ν_c，absolute shift消去后remaining class仍C(d_i)。角cap亦同因子。

remaining terminal truechild lift时 `m_old/(q_Aq_child)≥ν_c n′(1−c′)J_child/K=n(1)JAJ_child/K`，ν_c恰取消，故parent不真也能恢复原terminaltruefloor。于是H(E_i)≤h_A,i+k(d_i)(1−c′)，h_A,i<kc′/2时outer limit严格小于k，形成真正矛盾。没有借最终atlas的新n′(0)常数化或中间密度equality。

## 8. 最终scope与停止

本轮通过的是shared8.2及完整∞排除，均为原来源责任；finiteℓ尚需§7–9、原2.17/finite/高维出口与新GWZ条件仍未清。普通Kakeya n≥5/general Goal保持active；不把macro或已有定理复现算重大。两份分工稿的相互独审身份清晰，自己的前端proof不冒独审。审查完成后停止编辑，由root统一整合/验证/同步。
