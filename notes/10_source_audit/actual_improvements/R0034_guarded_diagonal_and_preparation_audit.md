# R0034：guarded diagonal、prepared law 与有限条件化审计

2026-10-17，A。已读R34 spec/最新STATE及原4.4–4.9、4.11 coverage/4.12（PDF50–63，抽取2679–3421行）；相关源行按split('\n')。本稿只处理此接口，candidate geometric construction另由B/root审。已核CRP/TCM/ASM/TEX为具名既有输入；原后续branches、GWZ集合估计、KT全文均未因本稿认证。仅编辑分配文件，无Git。

**独立结论：4.4–4.9的guard/量词、原prior与entropy/conditioning链可以按下列精确形式成立；countable scenario提取不能用普通无限抽屉代替其residual反证。** 原SCL的原尺度/切尺度警示仍有效，但没有直接否定此处预声明guard。4.11整体验收还须逐项支付B/root的candidate与原law recovery构造，本稿不提前宣布完整通过。

## 1. 原4.4：depth-zero和vanishing-depth的不同极限

depth-zero、horizon-zero known normalization Fi保C(di)、length1、actual inverse-subpower mass与old terminal knowledge；CRP composition给H(Ei)≤H(Fi)≤k(di)。两侧→k，故Fi仍maximizing，relativeprofile结论适用，不要求fFi(0)有统一界。

vanishing node先固定b=1/m>0，由4.3取actualdepths b_i→b、horizons→kb及actualprofile/narrowness等有限要求。只有完成这项outer convergence后才令m慢增：在每阶段选i足够大，使depth/horizon errors≤1/m，及所需profileerror=o(b)等，再选一个actual exact problem。所得b_i>0→0、horizon→0。它不是声称4.3对任意给定的b_i→0自动uniform，更不是取一个sample (i,N₀)替代各i的exact systems。

## 2. 原4.5：被排除的必须是actual known atlas

固定finitegrid、base maximizing sequence及width toleranceζ。设node实际depth r_i、cumulativehorizon h_i→kr，output被旧pL以subpowerlist知，geometry/coverage在每fixedi内actualsubpower，且gainΔ_i≥Δ₀>0、remaininglength正。

thickness output的timecost≤h_i+kΔ_i/2。原2.13仅需terminal equality可normalize剩余；其horizon upper≤k(di)(1−r_i−Δ_i)，故H(Ei)≤k−kΔ_i/2+o_i(1)，反k>0/maximization。此处即使Δ_i变化，只要有fixed lower和boundeddepth，可抽subseq后完成同一估计。

width output保持**actual node depth/time**且各outputlabels均有extraΔ_i。剩余仍maximizing：其cost lower H(Ei)−h_i、upper k(di)(1−r_i)。选其terminal widths≥(ℓ−ζ)×actualremaininglength，lift后最终terminal horizon→k；node原lower+extra gain+remaininglower使总width超过base ω≤ℓ+ζ（如Δ₀>4ζ，预留errors）。近似knowledge、无subpowercoverage或仅某些labels有gain均不自动满足此排除。

## 3. 原4.6：固定n/i后才取finite sample cutoff

对fixedstage n先定ε_n、Dn/Un/有限grid、γ_n、ζ≪γ_nε_n。4.5对这个fixedpositive gain γ_nε_n排除所有足够late outer i的actual输出：若无限多个i仍可输出，可取one finitegrid node与outer subseq回到§2反证。因此可先选i=i_n，再固定其exact path subsequence。

令K_path=N₀^{o_{N₀|i}(1)}包含此固定path几何/lists/reciprocal pathmass/preparation成本，p_path≥K_path^{-1}。声明一个fixed original exponent M#后，若无限多个N₀有finiteoutputs，均满足counts/heights/width-inverses/pieces/degrees≤N₀^{M#}，slack/list≤(K_path logN₀)^n、mass≥p_path/logN₀，则这些outputs本身可组成同一exact subsequence的tempered atlas。

homogenize其depth/horizon/width exponent，bufferedgain保留。若a_actual=N₀^{-r+o(1)}，换为a_r只增N₀^{o(1)} slack；value和curvature界两向都可吸收。固定n的(K_path logN₀)^n仍原subpower，mass也inverse-subpower。因此反4.5，存在**依n/i/M#的**finitecutoff。没有获得对全部M#共同的cutoff。

## 4. 预声明guard为何可覆盖posthoc固定scenario

先选path与M_path，再声明 `M#=2^{(M_path+n)^2}`，最后N₀。对每个fixedscenario S，实际实现须证明original complexity≤P_S(M_path)，其中P_S(M)≤C_S(1+M)^{d_S}，S固定、M≥1。则

`sup_(M≥1)[log₂C_S+d_S log₂(1+M)−M²]<∞`，

所以存在n_S，使所有M≥1且n≥n_S都有P_S(M)≤2^{(M+n)^2}。这正是uniform-in-M的关键，允许M_path沿stages不有界。scenario的fixedslack/list power r_S也最终≤n。不能在看到outputs后改M#或重选sample；这里只丢前finite多个stages。

必须另证P_S的控制确实只依**原geometry/outputmap**，而不依arbitrary analytic masks/posterior rule；4.12提供这种回收，不能先把它当自动。对随n变化的S_n，没有共同n_S，故必须先通过§11的residual量词固定scenario。

## 5. Stage与tangent因子的两种小量

选Dn,Un→∞、ε_n→0且UnDnε_n→0，在fixed interior interval放m_n≳1/(Dnε_n)个successivewindows。所有grid finite。选outeri使relativeprofile/horizon/width errors为o_n(ε_n)，再选N₀越过fixedM# cutoff，并满足Gn/logN₀→0、N₀^{-1}K_path logN₀→0及

`n log(K_path logN₀)/(ε_n logN₀)→0`。

于是N=N₀^{ε_n}，实际path/log因子是N^{o(1)}。**analytic K=N^{o(1)}**可以包含tangentprofile errors，它未必被某fixedpower K_path控制；输出允许的却是(K_path logN₀)^{r_S}。两者不能互换，candidateconversion须另行付actualslack。本稿与SCL的原警示一致，没有从N₀^M免费推出N^C。

## 6. 所有potential parents先准备同一reference law

parent A的原full prior mass ν_old(A)∼n_old(b)J_A、time q_A。normalize后prior仍ν_old(.|full assignment A)，不是path条件prior；v2作hiddenunitB=1，但w值/斜率未因此有tangentsubpower上界，只有native X=P_*有界。

先对**所有potentialparent和finitegrids**删原highdensity例外。widthp=N^{-r}对应old depth b+ε_n r、bounded-grid-overlap。within-world factorJ_A/ν_old(A)及relativeprofile给raw ceiling≤Kp^d，native P_* 的derivativeupper/selectedlower/curvature使X-bin与w-bin的有限覆盖同阶（按2.9求preimages，nativeimage用Taylor）。这些是restricted numerator ceilings，之后任意删除都保。

angular preparation先用原terminalknownparent label refinement保terminalpure lower，再对同goodmeasure求oldjointangular numerator。在ℓ>0时，只投影major normalized velocity v=Z′：parent physical minor velocityrange≤K_path N₀^{-χ_A}，χ_A有fixedpositive lower（parent interior、ζ/outererrors已小），而ε_nUn→0，所以比所有tested p细得多。major v-bin宽p映到oldvelocityball Kp，遗漏minor分量也在此球；这样才可继承π的p^S上界。它不是任意二维law投影后自动保同Frostman exponent。

major-row fullness也有真实原尺度理由。累计child largest axis/q为actualsubpower，parent major axis/q full、minor axis/q fixedpower薄。若relative D_s的major Z-row/q_s fixedpower亏损，而另一row/q_s≤K_path，则parentmatrix×D_s的operator/q_total也fixedpower亏损，反2.12。故ρ_s=∥D_s^T e_Z∥≥q_s/K_path；row subtraction系数≤∥Y-row∥/ρ_s是actualsubpower，transverse rowlength=|detD_s|/ρ_s，tilted strip速度式合法。

## 7. 一份µprep选entropy window，parent law随后冻结

normalize一次删例外后的reference path为µprep。对每potentialparent A，λ_A^0=(ν_A×dt)|preparedpath/s_A、p_A=µprep{A}；同一node p_A∝oldweight×q_Aν_old(A)s_A。小s_A父的总质量以Σoldweight q_Aν_old(A)≤1计，再除总rawpathmass；取subpower阈值足低即可忽略。mask后denominator掉太多的父以pre-mask父质量计费。留下λ_A^0≤Kν_A dt，angular numerator除s_A也只付K。

所有windows必须用**同一µprep**的nested histories。可将chartlabels记录whole ancestor history，使start history正是parent A；若A省略start信息，就不能由conditional MI直接推出对A的声明。令V*为oldcoordinates中precision depth ε_nUn的有限velocitybin，则H(V*)≤C Un logN+o(logN)。successivewindow的I(V*;end|start)非负、总和≤H(V*)，平均窗口≤C UnDnε_n logN+o(logN)，故可选o(logN)窗口。

给A，requested v-bin从V*至多K choices（ℓ0用两轴tangentfull，ℓ>0用majorfullness）；故I([v];end|A)≤I(V*;end|A)+logK。这里不要求v是V*的精确函数。选窗后p_A、λ_A^0、π_A永久冻结，后续graph/likelihood/sparse masks只取submeasure，不能重新normalize后重用原entropy或cap。

## 8. True path scales、base cap与本轮完整floor修复

actualpacket Q在parenttime的q_s、J_s、ν_Q满足ν_Q∼a_s^dJ_s，base-unit pushforward cap≤Ka_s^d q_sJ_s≤Kq_sν_Q。除blocktime q_s才得normalizedQ-time capKν_Q；再condition fullassignment ν_Q时才除ν_Q。ν_Q不是current incidence mass。

需要current floor时使用如下完整finite peeling，**不是追认R32/33证过2.11**。设finite layers t，各layer的whole-assignment budget B_t=Σ_c ω_c q_cν_c≤1，每chart至多D_t个entries。选ε_t>0、Σ_tε_t≤ε，固定threshold ε_t q_cν_c/D_t。对当前同一selectedmeasure，若某positive entry的currentmass低于其threshold，删除该entry的全部current incidences；重复检查所有layers。

每entry一经删除永为空、最多收费一次，整layer weightedcharge≤D_t×Σ_cω_c(ε_t q_cν_c/D_t)≤ε_t。finiteentries使过程终止，最终每positive entry满足其**current**floor，总损≤ε。若使用不同parent normalizedlaws，先在共同raw reference measure做同一计算，或显式乘其fixeddomination/normalization成本后缩ε_t；不能把不同prior的floor混算。ε取低于specified inverse-subpower current mass，可选subpower阈值。deletedentries只是原finite predicates的table；若输入selected predicate本来tempered，此新增删除保持tempered。它不把已存在的arbitrary analytic mask变成tempered；那项责任仍归4.12回收。

4.7初次用该预算删m_Q≪q_sν_Q的labels，baseprojection volume≥m_Q/(Kq_sν_Q)是inverse-subpower；discriminant upper在projection上为K，polynomialRemez给其fixedcomplexbox coeff/derivatives为K。按|P_ww|=(a_QH)^{-1}分高曲率affinecenter与低曲率stablebranch，H/K_g³→∞，使低曲率D≥cK_g^{-2}。cores/branches每label仅K个，可按同budget再删轻。

compose各graph与nativeP_*，以retained entry的positive basevolume及|X|≤K/approximationerrorKa付Lemma3.1/Remez，得固定graph的interior native-X derivatives≤K。以后稀疏删除无需维持旧currentfloor来保这个**已经固定的graph bound**。深endhistory的base uncertainty≤K q_end/q_s，选thickness/endpoint先于mesh足细，则每endhistory仅K个(t,y,X)pointstates。oldpL→pathchart→finitepointstates的实际lists由精确base和原terminal hiddenbin/nativebounds恢复，输出无新增unobserved feature。

存储full-layercap witnesses时，若label因capmask损≥一半，saturation给qν_Q≤K×lostwitnessmass；sum旧worldweights后删掉其pathincidences的成本亦可忽略。剩下floor仍对**旧witness**，不是finalpath，也不产生several-time independence。

## 9. 4.8 likelihood/state conditioning逐式证明

设R_A(E,b)原概率joint、Q_A=λ_pre(E)π_A(b)。其logratio负部期望≤ΣQ_A/e≤1/e，因此mixture MI=o(logN)推出正部也是o(logN)。选δ_N↓0比该比率慢，删log(R/Q)>δ_NlogN，Markov损o1，剩余joint≤N^{δ_N}λ_pre(E)π_A(b)。没有逐A小损要求，只有weightedmixture小损；numerator cap对后来restriction保留。

append label d′在每E至多D choices，preomit mass m(E,d′)固定。删m<λ_pre(E)/K1的wholeentries，mixture损≤D/K1。对留下entries，joint(E,d′,b)≤Kπ_A(b)λ_pre(E)≤KK1π_A(b)m(E,d′)。sum到C=C(E,d′)得到joint(C,b)≤KK1π_A(b)w_A(C)，reference w是preomit marginals，不能用免费newlaw替换。

对进一步TA≤该measure，删TA(C)<w_A(C)/K2的states，损≤1/K2，剩下TA(b|C)≤KK1K2π_A(b)。K1/K2可选大subpower、损相对指定current inverse-subpowermass negligible。arbitrary sparse restriction本身不保conditional cap，只有unnormalized numerator一直保；本句防止把joint bound当多时刻乘积先验。

## 10. 4.9 retained duration与fixedtime active prior

λ=Gνdt、0≤G≤K。对time partition I，保L_I={l:∫_I G≥|I|/K2}。删掉其complement的mass≤Σ_I |I|ν(all)/K2=1/K2。若Ct(l)⇒C^+_τ(l)对所有τ∈I，则在L_I∩Ct积分durationfloor，得

`ν(L_I∩Ct)≤K2/|I| ∫_I∫ 1_(C^+_τ)G dνdτ`。

after-duration restricted instantaneousmass≤Kν(L_I∩Ct) a.e.t。prior始终是ν，只给**active subset**的upper，不重设成当前成功prior。finite meshes的timepartition先细于bounded-motion (t,y,X)及所用affine quantities，fixedcell enlargement使上述implication成立。w的value/velocity未有K upper时不能拿同一运动理由应用于w-bins；原文这里只需nativeX/可控quantities，未假w time regularity。

## 11. Countable scenario覆盖的真实量词

每fixedscenario规定type、gainc>0、boundeddepthrange和小σ。priority assignment在每Q收所有满足wholeblockline inequalities及某处derivative lower的available trajectories，只以原residual incidence量认证threshold；timecase至多N^{dc+σ}、stripcase至多N^σ个tests（subpower normalization入slack），所以finite max可实现，谓词不包含分析质量计算。

**coverage应取assigned trajectory pieces上的全部reference incidences**；若先用derivative-counted coverage，须额外比较。固定scenario后max|Pw|≥N^{-σ}使|Pw|<N^{-2σ}的timefraction O(N^{-σ})，λ_A^0≤Kν_A dt及disjointness付o(β_n)，才转countedcoverage。

假每fixedfinite menu的fullpiece-union coverage→0，选J_n→∞足慢使firstJ_n仍→0。删其所有assignedpieces的全部incidences后仍有substantialresidual。**每subsequence的每substantialresidual**candidate假设在进一步子列给positive finite limitinggain和boundeddepth，gain/slack按固定compactrange可匹配某fixedmenu S。最终S≤J_n，而其witnesspieces对S仍free，违反S的maximality。这才得到fixedfinitemenu positivecoverage，再finitepigeonhole固定一个S；不是对countably many scenarios直接无限抽屉。

每sample再选一个node仅损G_n，β_n≥η0/(J G_n)。Gn/logN₀→0给β_n logN₀→∞，而diagonal late choice另给β_n^{-1}=N^{o1}。前者支付实际p_path/logN₀ outputmass，后者支付analyticcomparison；二者不能混成一句“subpower即可”。若删掉every-residual或every-subsequence量词，此反证不再成立。

## 12. SCL边界与停止

SCL说明原polynomial height N₀^M未必是uniform tangent N^C；4.6/4.11并未要求后一假结论，而要求fixedscenario原complexity polynomial P_S(M_path)与实际path-powered slack。PS uniform-in-M、fixedscenario提取及4.12原law joint-TV回收是新增真实责任；它们一项未付就不能援guard。本稿不以SCL旧弱化counter代替保此次全假设的counter，也不因原guard较大就宣称所有candidate自动合格。

目前未找到保原全部条件的guard/preparedlaw/4.8/4.9反例。4.11后半fullmodel candidate→originalknownatlas、properdegree/wholeassignment/actualslacks/height/TV复杂度须由B/root完整核验后再审。finiteanalysis masks不自动tempered，须用原geometric map和4.12恢复；本稿到此不先通过完整4.11。一般/五维Kakeya仍open，六维17/4及完整source高级输入条件保持，未经外部同行评审，不称新颖/重大结果。
