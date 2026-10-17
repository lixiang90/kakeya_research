# R0032：原Lemma3.5的基础与完整terminal extension重证

2026-10-17，root。对象OAI4 Lemma3.5（PDF36–46），只在原version1 j=1、version2 j=2及原degree2 tests中；不是高维推广。TCM001/ASM001已支付原3.1–3.4。A稿R0032_frame_graph_matching_audit展开本稿前半，B稿R0032_anchor_assignment_audit展开anchor/assignment后半。本稿补基础2.3/2.4、2.9/2.10、**实际还调用的2.12**并逐项整合。两终稿独审research/reviews/R0032_geometry_extension_review.md、R0032_prior_frame_review.md均通过，登记TEX-001；未经外部同行评审。

## 1. 原命题、单位与固定量词

固定d₀<1、S/η>0和原model维数/degree。给E∈C(d)、d≤d₀、length L、true terminal system的h>0。目标固定C/c，仅依上述数据，使每个固定0<e<min(h,cL)在retained subsequence有h−e known atlas，labels由旧p_L给subpower lists，thickness a_(L′)、0<L′<L、L−L′≤Ce，全部输出在原exact N=N₀ sequence tempered。e先固定再N→∞；不额外宣称对e=e_N→0统一收敛。C独立于E、L和E的polynomial complexity exponent。

按Defs2.1/2.2/2.6/2.8：世界weights和为1，trajectory prior νγ独立uniform time；原selected law为未归一化event restriction。density n(r)=N^-f(r)按fixed-tolerance typical含power-small例外，endpointcap n(r)≤n(L)(a_r/a_L)^d，joint terminal/angular cap n(L)N^-Su。priors在full coefficient coords为piecewise constant Lebesgue densities、polynomial ranges/heights/counts，predicates由polynomially many bounded-degree tests及任意Boolean组合给出，fixed test变量数；realconstants无height限制。

每world作w_new=B w_old，使derivative unit1、旧terminal hiddenbins宽δ=N^-L。old charts全interval拟合、disjointtrajectoryassignments，truefloor m_c/q≥n(L)J_c/K；known atlas不要求newtruefloor。本证明始终保原assignedprior，不condition pair survival。world/time权重与within-world normalizedblocklaw分开。

## 2. 原2.3/2.4：restriction与tempered列表实现

若观察原density g、restriction后g′≤g，则∫_{g′<εg}g′≤ε∫g。refine成≤Dlabels时在同一旧state求和，低于εg的refinedmass≤εD∫g。故inverse-subpower restrictions/subpower lists保typical exponents；所有例外先删再对小域/小条件概率积分，不能把typical upper直接当max upper。

Lemma2.4可直接证明：转到(t,y,V,其余coefficients)，y₀=y−tV的Jacobian1。每个旧polynomial test经替换仍bounded-degree；固定其余变量后，在任一base轴只于polynomially many roots处改变（identically zero条件无改变）。joint discrete entries/labels加入其有限bin predicates，同样只有polynomial数boundaries。延零后，height×jump数×其余变量rangevolume及internalcopies/world总数均≤N^A，因此joint density G满足

    ||G(·+h)−G||_L1 ≤ C N^A |h|，             (1)

先在单轴用bounded step function每jump贡献≤2height|h|，再积分并加各base轴。对宽ρ的base-cell averaging，L1差≤ρ^-m∫_|h|∞≤ρ ||G(·+h)−G||₁ dh≤C N^Aρ。取fixed D>A+T+1、ρ≈N^-D给O(N^-T) TV误差。A/D可依E的复杂度，下面N^Ce中C无需依它。

flattened law对exact base在每cell内posterior恒定，故每cell/conditioning-bin可存一个最大成功质量的固定长度label list。cells/entries数polynomial，lookup table tempered，TV误差对后来任意selector统一。转回原law只损同样TV，并用actual discrete label∈stored list作真正tempered selection。这支付2.10中可能只可测的crossing-list筛选；无须把分析density mask直接编码进最终选择。

## 3. 原2.9/2.10的真floor与旧label知识

degree≤2的实Q，{|Q|≤ε,|Q′|≥b}在至多两个monotone intervals上，各长≤2ε/b；总长≤4ε/b且碰≤C(1+ε/(bδ_bin))个gridbins。这是原2.9。

对true系统，Σω qν_c≤1、m_c≤qν_c。删qν_c>H m_c的wholecharts损≤H^-1；选H subpower、其逆远小于系统mass。对去掉pr密度例外的goodmeasure，2.9给每chart在base上至多K个hiddenbins（ε=K a_r,b=B/K,δ_bin=a_r/B），basevolume≤K qJ_c，故good m_c≤K n(r)qJ_c。wholechart fullmass超过此upper两倍者，其mass至少一半来自例外，删掉全体只损≤2×global omittedmass。配合truefloor和第一次删除，得到

    m_c/q ∼log ν_c ∼log n(r)J_c。               (2)

跨过某observation的chart label必须满足其time/spatial/value/selected-derivative兼容。令crossing数T(p_r)；在原capped incidence law上积分（不只是已assignedchart）给

    ∫T dμ_cap≤KΣω n(r)qJ_c≤KΣω m_c。           (3)

Markov选subpower listlength后，只损相对系统mass可忽略的量；用§2的joint-cell table取代只可测selector。这里2.4的输入是**原tempered joint law（actual chart label,p_r）**，分析cap只证明存在高success的可测short-list selector；不把density-masked goodmeasure当成tempered输入。原jointlaw的uniform TV保证先换flat posterior最大表再转回仍有同等success，最终actual label∈table是temperedselection，无需保留cap masks。

最后删失去超过一半mass的charts，再扩大K，(2)和truefloor同时保留、labels known by p_r。assignedtrajectory prior仍是νγ|A_c，不按新selectedmass条件化。terminal r=L时得到旧p_L知识。

## 4. 实际还需的2.12与whole-label同质化

Def2.8仅给||D_c||≤qK，不能直接把最大空间轴写q。准备旧p_L知识后，若在inverse-subpower质量上||D_c||/q≤N^-α（α>0 fixed），wholeinterval空间拟合将V限制到以y_c′为心、半径K N^-α的ball。取0<u<α/2、u≤ηL，ball仅需K个N^-u速度bins；旧p_L list只有K候选labels，因此每个retained观察只有subpower候选速度bins。

先移除joint angular cap与pure p_L典型lower的例外。在goodmeasure上，每候选angular numerator≤n(L)N^-Su+τ，而old pure denominator≥n(L)N^-τ。先sum这些subpower候选再积分原purelaw，deficientchart质量≤K N^-Su+2τ，取τ<Su/4为power-small，矛盾。这证明原2.12的largest-axis fullness，无额外breadth假设。

选wholelabels并homogenize其polynomially bounded singularvalue ratios只损inverse-subpower质量，不改每个保留oldchart的truefloor。于是旧time q₀=N^-h+o(1)，空间axes为q₀（version1）或q₀,q₀g（version2），g=N^-β+o(1)、β≥0；所有subpower误差入K。设n_Q=n(L)q₀^j g，v1置g=1。每usedoldlabel的normalized-q₀ incidence mass≥n_Q/K。保留label集合作为finite table tempered。

## 5. 双时间原law、oldlabel数与共同frame

q₁/q₀≈N^e、q₁=N^{-(h−e)+o(1)}取dyadiccoarsening。每world/block I按νγ dt₀/q₁ dt/q₁采样，双端都旧selected时保留，外权ωγ q₁。令s_I(ℓ)为trajectory的旧selected timefraction，则总pairmass=Σω q₁∫s_I²dν≥(Σω q₁∫s_Idν)²=N^-o(1)。任一one-time marginal≤旧selected law（在block相同归一化）。不归一化pair law。

旧floor/disjointness给每world/newblock oldlabels≤K N^e/n_Q。沿trajectory P及Pw分别是degree≤2和≤1，旧subblock全fit外推到I给value≤δN^(C₀e)、derivativeupper≤N^(C₀e)。固定trajectory及某端own-selectedincidence后，其test derivative affine、blockmax≥K^-1；对侧time仍uniform，|Pw|<N^-e只占O(K N^-e)相对长度，两色删除power-small。

先加原one-time深度gridcap N^e n(r)及jointangularcap n(L)N^{(1−SR)e}，grid含0/L且spacing≤e，Re≤ηL。它们只是analytic masks，用one-time domination可付power-small绝对mass。

v2若old normals的sineangle>gN^(Re)，两个widthKg速度strips交成diam≤K N^-Re的ball。固定source A，witness A′由其own pL给K候选；each candidate仅K velocitybins。source extrapolated spatialarea≤q₀²gN^(C₀e)，2.9/对侧floor给≤N^(C₀e)terminal hiddenbins。乘oldlabel数及capped jointdensity得

    badmass≤K N^[(2+2C₀−SR)e]。                (4)

选R fixed足够大，使其power-small。这里二维strip交成ball是原j=2事实，未延伸到j3。

置g#=min(1,gN^(Re))。deterministically从A圆整normal于spacingg#，normal center-velocity于g#，midpoint于q₁/q₁g# grids，tangent center-velocity取0；g#=1时固定axes/staticmidpoint。wholetrace进D、axes q₁/q₁g#乘subpower。A′可列K个compatible D：中心/速度差先用共同line控制，再round；rotation只作用这些差，未乘无控制absolute midpoint。normalizedbase z=(τ,ξ)的spatialJacobian J_D≤N^(C_base e)q₀^j g。A稿展开所有frame误差。

## 6. source-base密度、heavy entries及stablegraphs

固定(A,D)或(A′,D)，把pair restriction push到sourcebase z₀、积分另一time。own或witness-extrapolated test在source给小value+对应derivativefloor，所以2.9给N^O(e) hiddenbins；source-vertexone-time cap仍是原的N^e n(L)，不是condition A′后的density。dt₀dy/q₁=J_D dτ₀dξ₀，故每entrysourcebase density≤n_Q N^(C_base e)。  (5)

常数顺序必须显式分名：先选**C_entry**，删mass<n_Q N^(-C_entry e)的(A,D)/(A′,D) entries；由oldlabel数×subpoweroptions，totalcostpower-small。用这些**pre-deletion entry masses**及(5)得到projectionvolume≥N^-O(e)。以下discriminantcoefficients、stable radiusC_U均先由此固定；后面的groupindex阈值**C_index**是不同常数，不能后增C_entry而不重选C_U。

对normalizedtest P，若|Pww|≥δ^-1N^(-C_Ae)，以affinecenter test w−F_ctr替代；其wholeblock error|Pw/Pww|≤δN^O(e)。否则保P，取C_A>C₀+3，使sourcepoint的|2PwwP|≪|Pw|²，D=P_w²−2PwwP在source为N^-O(e)…N^O(e)，与w无关。heavyentryprojection正volume加polynomialRemez给D在fixedcomplexbox的coefficients/derivatives≤N^O(e)。选radiusN^(-C_Ue) realballnet；每pair可选U使两disc在8U皆nonzero，不要求一球避全方程。

在8U的simple real-on-real branches取离w(t₀)最近者，completing-square公式给|w−f(z₀)|≤δN^O(e)。不使用unused far root。Pww=0是linear唯一分支。

## 7. 真group预算到Cor3.4

若paired normdifference on2U在[M,2M]且M≥δN^(C_*e)，按M/D/U/world/block和两centerjets（scaledU coords、spacingM、固定足够阶）分组。finitejet normcomparison使两jet cubes为boundedneighbors，同组所有members距一个actualreference norm≤CM。一个oldlabel有≤N^(C_opt e) options；C_opt由此前固定数据决定，不依之后C_*，M range polynomial只贡献O(logN)choices（range exponent可依E，吸入同一N^e成本）。

groupmass m_G：在每sourcebase所有w处于widthO(M) band。M≤1时选a_r∈[M,MN^e]的capped grid，用n(r)≤n(L)(a_r/δ)^d和(5)对应的Jacobian给

    m_G≤n_Q N^(C_mass e)(M/δ)^d。               (6)

M>1时使用depth0；v1 w subpower，v2原native小值/selected-derivative tests经2.9只容subpower个unit hiddenbins。不能用O(M)bin数替代。非空capclass有d≥0，于是depth0同样给(6)。

现在选**C_index>C_opt+3**（含oldlabelcount费用），每色删该group中pre-joint-deletion marginalmass<n_QN^(-C_indexe)的(label,branch)indices。globalcostpower-small。若全部大discrepancy pairmass≥N^-e，则有group在两色删除后m_G′≥m_G/2；否则global删除量至少原badmass一半，矛盾。无需该group有绝对mass≥N^-O(e)。

每色retainedindices个数≤N^(C_indexe)m_G/n_Q，再用(6)得≤N^O(e)(M/δ)^d。normalize survivinggroup bym_G′；先取rawweights n_Q/m_G′，其和≤2N^(C_indexe)，再normalize为probabilityπ。由(5)及U-rescale Jacobian，每index-base density≤N^O(e)π_i；实际m_G′分母被rawweights及其总和完整支付，未假conditionalπ。

于是Cor3.4输入：R=M/δ≥N^(C_*e)、pairnorm≥M、valuegap≤δN^O(e)、listcard≤R^dN^O(e)、common-reference norm≤CM、概率mass1、双原π式density。取C_*在所有费用后足够大，使N^O(e)均≤R^ε_*，套ASM001矛盾。因此除power-small pairmass外

    ||f_A−f_A′||_(2U)≤δN^(C_*e)。              (7)

这里只在group内付一次normalize；其外原pairmeasure始终未归一化。A稿独立展开M>1、groupoptions/π所有细节。

## 8. 随机commonanchor及实际continuation

每D选boundedcomplexbox内α_D及boundedcomplexdisk内σ_D；从source z₀沿line z=z₀+s(α_D−z₀)取0→σ_D→1。disc coeff≤N^O(e)、sourceval≥N^-O(e)，polynomialsublevel使anchorval≥N^-O(e)失败概率power-small。line restriction degreefixed，非零endpointvalues与derivativeupper使endpoint距boundedregionzeros≥N^-O(e)。去更小N^-B e零点disks，randomdetoursegment命中概率≤其radius/endpointdist的fixed multiple；boundedzeros使总失败power-small。因σ有bounded二维density，积分radialdistance的界常数fixed。

路径避零后factorization比较每因子与source值，附近zeros只损N^O(e)、远zeros只损fixedfactor；得到linepath上disc≥N^-O(e)。full z derivativeupper再给full-base tube radiusN^-O(e)。exceptions先对randomchoices再对原pairlaw平均，不给每trajectory free probability lower。

取endpointballs含fixed relativemargins，ASM001原3.1/3.2把(7)传至anchor及fixedjets。sourceanchorjets按common spacingδN^(C_b e)分real/imag bins，paired bins是boundedneighbors；chosen branch norms/jets有polynomialrange，unusedfarroot不入range。给A′，D有K候选，每converted equation在anchor至多2root/jet tuples，邻binsbounded，因此可列**subpower**个(D,b)，不是N^O(e)的list。

## 9. 先建representative table、只返回source evaluations

对每(D,b)在所有converted real sourceequations中选firsteligible P_b：disc coeffbounds/anchorlower及某simplebranch jet在bin内，table只依anchors/D/bin，不依t₀或trajectory。每retainedsource自身eligible。

同anchorball上，finitejet control给sourcebranch f与representativebranch fhat差norm≤δN^O(e)；|P_b,w(z,fhat)|≤N^O(e)、|P_b,ww|≤δ^-1，所以

    |P_b(z,f)|≤δN^O(e)， |P_b,w(z,f)|≤N^O(e)。 (8)

只将这两个sourcebranch的polynomial evaluations沿**source-safe**路径续回；不续representativebranch，不要求它在real source有root。evaluation fixeddegree，ASM001费用无coefficientheight依赖。

在source附近relativeblock长度≥N^-O(e)的realtrajectorysegment上，ownsourcePw(t₀)≥K^-1、其affine-time upper及bounded z-speed保证samebranch持续；completing-square给|w−f|≤δN^O(e)。以|P_b,ww|≤δ^-1替actualw，(8)仍同阶，再沿degree≤2 trajectorypolynomial extrapolate到整I，得到

    sup_I |P_b|≤δN^(C₂e)， sup_I |P_b,w|≤N^(C₂e)。 (9)

source临block端点时取one-sided shortsegment。source与representative可无共同return-safe path，这里不需要。

## 10. representative disc的source lower必须在freeze前支付

固定anchor/table，每sourceA的D固定；其equation在anchor至多2root/jet tuples，故至多2bins及representatives，路径homotopy再多不增加此数。representative disc atanchor≥N^(-b_anc e)，fixed-degree polynomialnormcomparison给realboxnorm同阶lower。polynomialsublevel给{|D_b(z)|<N^(-C₃e)}体积≤C N^[-θ(C₃−b_anc)e]。

对每sourceA用(5)乘该volume，再sumoldlabels≤KNe/n_Q，得到badpairmass≤K N^[C_base+1−θ(C₃−b_anc)]e。选C₃>b_anc+(C_base+3)/θ，即power-small；**这在t₀仍平均、table已先建时成立，C₃先于latercurvatureT固定**。无须按全bin数sum，也未用未来表。

## 11. freeze与原pL知识：重新建整个assignment

在每world/block联合选anchors/detour和t_src，使冻结后successmass至少其平均；weighted totalM_fr≥N^-o(1)。不要求逐block下界。冻结successful measure仍是νγ dt/q₁的未归一化restriction。

在fixedt_src，旧selected sourcechart membership唯一给A，从它求D、nearestsourcebranch、safecontinuation和anchorjetbinb。要求storedranges/representativeentry、wholeblock空间及(9)、source disc≥N^-C₃e等，给trajectory至多一个c₀=(D,b)，独立later t，merge掉oldA。

再保原later旧selectedincidences中whoseactualwitnessA′的compatibilitylists包含D/b者。此selection含冻结successes、mass≥M_fr，仍≤原νγ dt/q₁；analytic density masks未作为outputpredicate。旧pL的A′候选subpower，逐个列D和两anchorroot邻bins，取finite range交，故new c₀ genuine known by oldpL。不是只知道posterior熵小或N^O(e)labelcount。

## 12. low/high curvature与Def2.8全条件

先固定C₂、C₃，再取C₄>C₃/2+2、C_s>C₂+C₄+1，最后T>max(C₂+C₃+1,C_s+C₄+1)。若|P_b,ww|≤δ^-1N^-Te，则source上P_b,w²=D_b+2P_b,wwP_b；error小于|D_b|，因左边非负迫D_b>0，并给|P_b,w|≥N^-C₄e。

其blockmaximumM_∂∈[N^-C₄e,N^C₂e]。取dyadiclowerendpointv，refinelabel c=(D,b,v)，testP_b/v。只有O(logN)个v，因此仍oldpL-subpowerknown；blockderivmax∈[1,2)。value≤δN^[(C₂+C₄)e]、curvature≤δ^-1N^[(-T+C₄)e]，同时fit δ_s=δN^(C_s e)。selectedtimes删normalizedderivative<κ=N^-o(1)，affine derivative的order-one max给relativebadtime O(κ)；disjointassignments下globalrawprior损≤Cκ。选κ=o(M_fr)，仍逆subpower，mass保持。未对pairsuccess law假uniform time。

若|P_b,ww|>δ^-1N^-Te，用affinecriticalcenter testw−F_ctr；(9)给wholeblockerror≤δN^[(T+C₂)e]，fit δ_h=δN^[(T+C₂+1)e]，derivative1、curvature0。v1仅lowcurvature且导数恒1。选承至少halfremainingmass的一个case，得共同L′=L−A_case e；取C≥max(C_s,T+C₂+1)及c足小，使L−Ce>0、Re≤ηL。h−e timecost、0<L′<L及L−L′≤Ce全部成立。

## 13. tempered编码、还原单位及剩余责任

oldlabels/frames/stableball grids/anchorbins/representativeentries/v bins数均polynomial；chosenbranchjets的range exponent可依E，但jetorder/continuationformatfixed。witness原quadratic coefficient可极小，unusedfarroot可超polynomial；“至多两根”仅为knowledge计数，实际table实现用原二次方程和root/jet落stored polynomial bins的有界量词，不储存farroot或巨大1/c。implicit jet relations只用已付lower的Pw=±sqrt(discriminant)，不除tiny quadratic coefficient。

finite sourcetime/anchors/table可用任意realconstants编码，Def2.2允许search只用于定位它们。sourcecontinuation/nearestroot/fixedjets由ASM001固定格式谓词给出；wholeblockfit只量化一个timevariable（degree≤2），QE或显式extrema编码仍bounded-degree/polynomialcount。oldsource alternatives作polynomial-sizeddisjunction，assignment仍trajectorypredicate，later selection是oldincidence谓词与storedlisttable/geometry的组合，不含分析density masks。

original test/coord coefficients polynomial；inversecurvature仅在δ^-1N^-Te cutoff之上使用，lowcurvature normalizationv≥N^-C₄e/2；baseframe/time/inversewidths皆polynomial。Def2.2的polynomial exponent可依E/L，**N^Ce中的C**不依它：degree/model固定决定所有extrapolation/Remez/continuation powers，polynomialrange只在O(logN)choices及有限编码中出现，可对每fixed e吸入同一Ne费用。阈值N₀可依E/e，不冒称统一。

compose realaffinebase z(t,y)，还原w_new=Bw_old。v1保持w−F(t,y)，v2保持totaldegree2，derivscale恢复B、curvatureB²/δ_case。空间matrix最大轴≤q₁K，wholetracefit/assignmentsdisjoint/globalmass/selectedderivlower/oldpL list/temperedness均满足Def2.8。因此得到所需knownatlas；**不额外声称newtruefloor**。

完整数学链与两支证明经root逐式整合、两正式独审通过。只认证原Lemma3.5及本稿明确支付的基础，不认证criticalpaths/其它高级排除；完整OAI4/SRC/DIR/FSD/DIM条件未清空，无无条件新高维结论或重大性认证，Goal active。
