# R0034：actual-improvement 全稿独立量词审查

内部独立审查，未经外部同行评审；不声明新颖性或重大性。

2026-10-17，A / audit_four_dimensional。逐式读取root `R0034_actual_improvement_full_proof.md` §§1–12（首次148行含末空行），对照原4.4–4.12、Def4.10（PDF50–70，提取2679–3726行），含strip/time构造，未只自审A的guard/preparation稿。A独立proof存 `R0034_guarded_diagonal_and_preparation_audit.md`，作者自审不计独审。只编辑指定review，无Git。

**最终结论：通过修补后版本的本次独立审查，无剩余必须修正项。** 下述原law selected-eligibility接口由A指出、root修补；A已重新实读root §11的failure map、排除failure的最大列表及质量不等式，确认修补闭合。具名CRP/TCM/ASM/TEX及其高级集合输入仍条件；本轮不证明每个substantial residual实际有candidate，也不认证完整OAI4/无条件六维界。

## 1. 已报告的必要明确化：4.12的failure map

原law list recovery最大化的是原µ质量。若geomlabelmapA只检查whole-trajectory fits，而最终derivative lower留到recovery之后再删，新增raw list successes可能均落lower不合格的incidences，无法保证最终成功质量。已向root提出直接修法：wholetrajectoryassignment不变；incidence map A(l,t)仅在wholefits及全部final selected-eligibility（原selection、final derivative lower等）满足时给assignedlabel，否则failure，且failure永不进list。

此map允许依incidence，仍由有限原geometric predicates定义；它不改变block-invariant assignment。在analytical ν上仍与已有successfullabels一致，故4.12 domination/TV每步保原成功质量。没有增加观测特征或analytic mask。root现稿已按此明确修补，A复核通过。root新增同一observation下无效label占9/10、有效label占1/10的有限边界校准也正确：错误recovery可选无效项后损失全部，先赋failure再排除便保有效质量；它不是原定理或Kakeya反例。

## 2. Forbidden outputs与finite cutoff

root §2按CRP先证4.4 depth0 normalization maximizing与慢vanishing nodes，不假bounded absolute f0。4.5 thicknesscase通过terminal-known atlas normalize剩余、time加法得uniformpositivegap；widthcase保持实际depth/time，以remaining maximizing和最终terminalwidth upper反证。两个case都未索取new true floor。

fixed n的γ_nε_n是positive常数，ζ先小，之后outeri足够大，使相应actualatlases不存在。固定i及任意fixedM#后，若无限lateN0有guardedfiniteoutputs，counts/coeffs/width-inverses/degrees统一polynomial、slack/mass原subpower；geometry homogenization形成actualexact atlas，strictbuffer不丢。depth替limit引起N0^{o1}倍率可同时吸收value/curvature。故每M#有cutoff，未断言对所有M#共同cutoff。

## 3. Predeclared guard与posthoc fixedscenario

M#=2^{(M_path+n)^2}在N0前声明。每fixedS有P_S(M)≤C_S(1+M)^{d_S}时，logarithmic bound被M² uniform支配，故n≥n_S后对所有M≥1有P_S(M)≤M#；不要求M_path bounded。fixedslackpower r_S也最终≤n。只对§6已经固定的S适用，不允许S_n随n变后重设guard/重抽样。

stage/grid→outerproblem/path→M_path/M#→lateN0顺序明确。G_n/logN0、N0^{-1}K_path logN0、n log(K_path logN0)/(ε_nlogN0)三约束用途不同，均在fixed n/i可满足。analytic K与actual K_path^r始终分开；SCL001警示未被撤销。

## 4. 本轮2.11预算及fixed parentlaw

root §3实际证明finite weighted peeling：每层fixedentries/fixedthreshold，删当前不足阈值的entry一次后永空，layer总charge≤ε层；finite层Σ ε层小于目标损失。循环检查各层使**最终current**floors同时成立，不拿pre-deletionfloor代替currentfloor。若输入law是analytic，只得到analytic预算；其mask不因此tempered。本轮新增proof不追认R32/33已有2.11。

parent prior仍oldν conditioned on full assignment，densityfactorJ_A/ν_old(A)，native signal为X而w可巨大。highdensity及angular异常在全部potentialparents/finitegrids统一先删；nu saturation与relativeprofile给Kp^d numerator ceilings。ℓ>0 majorvelocity投影合法是因为原parentminor已fixedpower薄、ε_nUn→0；并非任意Frostman projection定理。小s_A/小survivingdenominator成本用原qν/parentmass预算，留下λ_A^0≤Kν_A dt。

major row实际fullness的composition反证正确：若relative Z-row固定幂deficient，parentminor也固定幂薄，累计child operator/time必deficient，反2.12。row orthogonalization给transversewidth J_s/q_s，实际strip coefficients由K_path控制。

## 5. 一份µprep的entropy窗口与有限条件化

start/end标签包含wholehistory，在同一µprep上chain rule给disjointwindow increments总和≤H(V*)。windows数与U_nD_nε_n→0给某increment=o(logN)。requiredv-bin由V*至多K歧义，信息只多logK。p_A、λ_A^0、π_A在这一步固定；之后不重置为graph/likelihood/sparse-conditioned prior。

4.8中logratio负部≤1/e，故MI小控制正部；Markov保joint numerator≤Kλ_pre(E)π_A(b)，只承诺weightedmixture小损。append d′按preomitmass floor付D/K1，coarser C先sum同一goodjoint/referenceweights；后来T(C)小需再付1/K2。没有由jointcap宣称several-time independence。

4.9按integrated duration保active lines：删除≤1/K2，Ct⇒Cτ+的逐trajectory implication使ν(active∩Ct)≤K2/|I| times integratedmass。固定time incidence upper再用G≤K。ν未改，所得只是active-prior cap；timepartition对(t,y,X)/boundedmotion细化，未假unboundedw有K速率。

## 6. Stable graphs与earlier witnesses

baseQ pushforward cap是Kq_sν_Q，parenttime与unitQtime差q_s、fullassignment normalization再差ν_Q，root未漏分母。currententryfloor给inverse-subpower projectionvolume后，discriminantRemez、曲率split/cores/simplebranches与nativeP_* composition的ASM控制合法。固定graph bounds在后来restrictions下不需重新currentfloor。

deep history pointstate ambiguity先由geometry/native-X graph控制，再供4.8追加entry使用，未循环依赖palettefloor。originalpL实际lists则另由exactbase/pathlabels/finehiddenbin得。wholelayer witnesses的capmask半损失用saturation把qν预算charged到lostwitnessmass，未把finalpath当这些旧floors的witness。

## 7. Countable菜单、wholepiece coverage与greedy

fixedscenario/time每Q的test数≤KN^{dc+σ}，strip≤KN^σ，来自normalizedresidualmass≤Kν_Q及eligibility门槛；fulltrajectorypriority predicates固定，不记录分析mass calculation。gain向menu rounding同时支付N^{-dc}和curvature/value变化，不是免费向下取整。

root已明确coverage为assigned wholepieces上的全部reference incidences。若每fixedfinite menu覆盖→0，可慢选J_n→∞仍覆盖→0，删其整片后残余substantial；全subsequence/全residual假设给fixedpositive limitinggain candidate，匹配一个fixedS，最终仍在freepieces上，反S的maximality。这不是countablymany普通抽屉。

fixedscenario后才删|Pw|<N^{-2σ}；max≥N^{-σ}的affinePw使坏timefraction O(N^{-σ})，λ_A^0≤Kν_A dt与disjointness给oβ_n。nodepigeonhole得β_n≥η0/(JG_n)；β_n=N^{-o1}供comparison，β_nlogN0→∞供actualmass，两者均单独保。

## 8. Strip constructor的原law与actual窄度

deepactualrow A_deep与R不贴近时，其差限制v在width≤N^{-c/3} interval；每history最多N^σ rows，原goodjoint against λ_pre(E)π_A和palettecap总charge≤KN^{σ−Sc/3}=oβ_n。未先除tinyhistorymass，也未用不付分母的conditionalpalette。

rawrow coefficient太大亦把v限制于足够窄fixedpowerinterval，以λ_A^0(Q)≤Kq_sν_Q及greedythreshold排除，故stored rawrows original-polynomial。alignedrows与actualdeep row近，binwidthτ=(J_s/q_s²)N^{-c/4}给actualpL短list及actualK_path coefficientbound。positionbin宽q_sτ，由currentexactbase/velocityprediction给actualshortlist。wholepriority assignment merge后新spatialcolumns determinant恰J_sN^{-c/4}，保旧time/depth/test，得到合法widthgain而无需新floor。

## 9. Time pairing与tiny badgroup

(T1)逐indexbasecap来自candidate smallvalue/derivative只容N^{Cσ}个a′ hiddenbins、capK(a′)^d、Jacobianq_sJ_s及ν_Q∼a^dJ_s。原eligibilitywitness满足同cap，floor÷ceiling给projectionvolume≥N^{-Cσ}；不需为每后来subbox假新truefloor。

wholeblockcandidate graph split只在curvcutoff以上求inversecurvature。其余D atcountedpoints lower、initialwitness Remez upper允许fixed C′取ρ=N^{-C′σ}，comparisondomain包actualpiece并有稳定branches。midpoint spatialsubbox ambiguity依motion K_pathρ除以ρ，故仅actualK_path幂，未付N^{Cσ}列表。

pairlaw在O=(pL,Q,subbox,truebranch/history)抽两个posterior，marginals均µ_cov，totalmass仍coverage。lightentries cost用Σm_Q≤1、index/subboxcounts计power-small。badfraction不消时存在group B≥m_QN^{-Cσ}；normalize后indexprobweights N^{-dc}/W_color，其multiplier含m_QW_color/B，root完整支付tiny B。commonreference f0的absoluteheight可很大，但matchedprojection+ASM控制difference normaN^{Cσ}。Cor3.4的R=N^c、θ=ε*/8、badgap>MR^{-ε*/2}及σ后取小全部留严格余量。

## 10. Representative实际slack，而非analyticK偷换

posterior-neighbor maximization保aggregatecoveredmass，无须选一tinycandidate。geomlabel不含candidateindex，priority及branchsign在whole shortblock不变，merge可用fixedrepresentative。

低curv代表以branch center |Pw|归一，D稳定使整个comparisonbox branch derivative固定倍可比；从branch到memberw的derivative扰动≤N^{-θc/2+Cσ}→0。因此**实际**derivative可order1，而不是沿用analyticK。value/curvature分别由aN^{-θc+Cσ}及a^{-1}N^{θc/2+Cσ}控制，以actual a_Q N^{-2θc/3}留buffer。高curv用affinecenter、actual a_QN^{-θc/3}。选择σ令所有Cσ≪θc且C′σ<kθc/12，timecost严格小于half k×depthgain。

actualframe D_sρ、time q_sρ及wholeblockchecks由pathgeometry控制。v1保specialw−F，v2还原B/B²尺度。最终lower-derivative及oldselection的incidenceeligibility须如§1明确进入failuremap，以便recovery后仍是真chart selection。

## 11. Coefficient P_S与原law TV recovery

初始matchedwitness的baseprojection≥N^{-Cσ}，而w仅需原W≤N0^{P0(M_path)}。P=A w²+B(u)w+C(u)的curv给A bound，derivative/value给B,C在projection上的原polynomial bound；Remez恢复其coefficients。这正面支付SCL未允许的absolute tangent height，不假w≤N^C。cutoff inverses、branch normalizer及oldcoordinate inverses都原polynomial；priority/counts/固定维逐test消元保持scenario-polynomial P_S(M_path)。

µprep为probability时T≤µprep必须乘p_prep再有ν≤µ，root §1/§11已明确。geomlabelmap及全部unobservedtags joint保留，listselector只看original exactbase和observed discrete tags；unknown tags未加入观察。domination给原µ上同列表success≥m，flattenedlaw在每cell/observedtag内posterior恒定，最大D_list表不劣；两次TV共损2e。

translation estimate在原coefficientcoords用y0→y(t) Jac1，fiber上每polynomial仅boundeddegree根，priority/table不增边界位置；marginalization收缩L1。高度、ranges、copies、condition-count均原N0^{P_S(M_path)}，因此mesh exponent与tablecount仍scenario-polynomial；任意posterior内容不出现导数或reciprocalprobability。original hiddenbin作为tag，不需与basecell对齐。

## 12. 原预算兑现与审查范围

constructor保c0η0/(JG_n)的referencefraction，乘回p_prep∼p_path再减O(N0^{-1})，由两实际diagonal约束得>p_path/logN0。lists/geometric constants为actual(K_path logN0)^{r_S}，最终落固定n allowance；P_S落预声明guard，positivefixed tangentgain最终>γ_n，strip保actualtime/depth、timecase有严格timebuffer。只丢有限早stages，不重抽已选sample。

§1的failuremap接口已修并复核，本review支持归档原4.11及已列4.4–4.10/4.12的内部重证。具名高级source输入、完整2.17及后续candidate existence/几何branches仍未由此支付；无一般/五维满维度或无条件六维17/4、无新颖性/重大性认证。到此停止本轮编辑。
