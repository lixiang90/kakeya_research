# R0025 独审：原加权时间归约及 scalar engine 接口

2026-10-17，`lifting_obstructions`。本节独立审查 `notes/40_multiscale/sticky_mixed/R0025_weighted_time_reduction.md`；与本人通过weighted arrangement/double-sampling得到的独立证明比较。本文区分已验证的归约操作、prepared cycle prior和高级曲率输入，不把代表选择说成旧measure的dense restriction。

## 1. 原fine prior到prepared mixture：通过

轻格threshold `p_j<cmw`、总格数≤C/w，令c足够小确使删除质量≤m/100。两个原time坐标的g损失≤2m/100；原图内部可任意相关，g≤1足够。

保留格数 `c/(K_tw)≤N≤C/w`，且 `cmw≤p_j≤C K_tw`。prepared mixture `ν_hat=N⁻¹Σν_j` 对旧ν的density `1/(Np_j)`在 `[c/K_t,C K_t/m]`，所以graph mean lower为 `c m/K_t²`，任意原fit事件的mass upper为 `C K_t a/m`。upper和lower两种capacity均实际支付；只用timecell的最大容量不足以得到后一uniformization结论。

## 2. 同一实际F/G代表和graph期望：通过

每格独立抽一个完整原标签，携带(t,F,G)，不同格的off-diagonal原g期望与prepared mixture一致。同格的两个原conditional times本来独立，抽样后不能免费替换；root把这些diagonal tuples置0，其总uniform-cell质量≤1/N。η小使 `1/N≤C K_tw≪m/K_t²`，故式(3)成立。

Z∈[0,1]且EZ≥d₀时，`Pr(Z≥d₀/2)≥d₀/2` 是直接平均估计，因此root不必使用我的较强bounded-difference尾界。这里只要求找到一组样本；将其正幂good probability与super-polynomial small的nonfit失败概率比较，逻辑充分。

## 3. 任意系数的normalized parameter net：通过

`λ=1/A(p)>0`、`z_i=p_i/A(p)`且 `λ+|z₁|+|z₂|=1`。任意命中至少一个sample的coarse fit，因|F|≤1、coarseclock bounded且precision≤1，有|z₀|≤5。于是可以在固定bounded的admissible subset上取ch-net，card≤C h⁻⁴。

必要细节在最终稿已满足：net centres自身仍admissible且λ>0。每个net点因此对应一个真正all-real quadratic p_q，且 `A(p_q)=1/λ`。不能把λ=0 ambient gridcentre当作原fit。λ任意接近0并不损坏这个有限覆盖：admissible集合虽非闭，但totally bounded，可在每个相交小格中选真实点。

E_q的normalized error h/2对应原weighted precision (h/2)A(p_q)，故原mass≤a。prepared mixture upper给期望≤C K_t a/m。coarse weightedfit的clock扰动仅为Cw，因为归一后的 `|z₁|+|z₂|≤1`；net扰动O(ch)。取radius常数小，再用 `w^{2ε₁}+Cw≪h=w^{ε₁}`，所有badfit命中点均被某个E_q覆盖。这一步没有bounded原quadratic系数的假设。

令β=min(ε₂/4,1/10)，η相对固定参数小，使 `w^β≥4C K_t a/m`。独立非同分布Bernoulli的Hoeffding给每net点tail `exp(−cNw^{2β})`。N lower使该指数增长为负幂；net只是polynomial h⁻⁴。因此式(5)小于上一节的goodgraph probability，可同时保一个g和全部adaptive quadratics。未依赖fine标签总数。

## 4. clock rounding、norm和旧atomic质量：通过

同一原F/G只换clock到各格centre，得到w-separated set。quadratic的weighted target已在normalizednet阶段计入clock误差，不能再把它说成F/G的Lip；当前稿没有这个错误。

直接展开 `S=(s−t)(F_t−F_s)+(s−t)²G_s`，unit norm下换两时钟的误差为Cw，故g的原near-output支持保留。若norm仅≤M，则确是CMw；最终稿显式保留M并把actual normalization留给应用，不免费省掉幅度。

prepared set的循环必须重新在Uniform(B)下生成。代表集合旧ν质量可任意小的n/N_fine例准确，故不能声称原ν⁴或ν⁶质量自动继承。通过明确的mixture/抽样/选取而验证prepared输入，再用set engine作反证是合法的；它不要求prepared law对旧fine原子law有uniform domination。

**以上sampler归约通过。** 它没有单独支付BSG的小image、radial22.2的uniform-P提取、Kaufman参数先验或最终A-budget矛盾；这些输入必须由engine证明分别核实。

## 5. 完整engine：small-S与asymmetric BSG通过

继续独审 `R0025_scalar_curvature_engine.md`、A稿 `R0025_scalar_engine_source_audit.md`，并对照本库原 Lemma13.7、Prop5.1及Theorem22.2精确statement。本轮不重证这三项named高级输入的全部证明。

prepared B上的all-quadratic uniform nonfit由weighted版本缩弱得到，precision h=w^α、mass a=w^b。固定s₁,s₂,t₂、删|Δs|<Cw/h后，Q落任意working interval迫F(t₁)的quadratic fit，故point cap `a+Cw^{1−α−η₀}`。H_j cycles的质量≥p_j⁴，其Q可用C#S_j⁴个working intervals覆盖，确给原balanced层的正幂基数lower。它先于BSG和radial，不循环使用待证曲率增长。

每S-cell的pair multiplicity在[M,2M]，pair均从E_xg≥m/2的H₀中取，故平均到A×S_j得到bounded dense relation而不丢原边比例。输出只占C#A₊ cells，CS给energy≥`w^{O(η₀)}#A₋#S_j²`。这正是Lemma13.7以X=S_j、Y=A₋的归一；energy正负号可交换两A标签处理。small-S lower支付`#Y≤#X^C`。

原BSG右侧为#A₋，换成#A'只多付已选的small loss。保平衡层后S'的card fraction才给其pullback H的真正edge density p≥w^l。四环Q差落4S'−4S'的O(w)邻域，直接用BSG的n=m=4结论即可得root式(4)。不需要给sumset新的AD/tube-KT，也不额外偷用Plünnecke闭包。

## 6. uniform P、共同邻居witness及新cycle prior：通过

H的edge density p给left-pair codegree平均≥p²，因此codegree≥p²/2的pairs具有至少p²/2质量。丢近time diagonal只损time cap计出的w正幂；各剩余pair的**原右邻居**质量lower不变。

前两坐标`(d,e)=(t₁−t₂,t₁²−t₂²)`在|d|≥g₀上反解 `(t₁,t₂)=((e/d+d)/2,(e/d−d)/2)`，逆Lipschitz为C/g₀。故w-ball中pair数≤Cg₀⁻²，r-ball原pair probability≤`Cw^{-2η₀}g₀⁻²r²`。选择真实w-separated像并作named uniform refinement时，每点保一个实际pair witness；P的保留率及Frostman损失因而可明确计算，不是把multiset名称改成set。

A稿给的保留率 `Δ_P≥cw^u p²g₀²` 与normalized ball constant `Cw^{-2η₀-u}p⁻²g₀⁻⁴` 一致。均匀P等于所选distinct witnesses在prepared B²中的conditional uniform law；不等于原fine时间measure，也不是原B²的almost-all。

每P点有共同邻居degree d₀=p²/2。新h_P图两次CS确给`(µ_P²×µ_B²)(W)≥d₀⁴=p⁸/16`，**不是d₀²**。W支撑的Q差仍由同一个BSG小image覆盖。均匀化以后radial坏对和right-time删除均只需在这个新reference下控绝对质量；root/A没有继续声称原式(208)对旧B⁴无损成立。

slab cap也已支付：固定第二time，若normal最后分量≥sqrt(slabwidth)，便给F的quadratic fit；否则由(t,t²)的非零quadratic sublevel加time cap控制。root取slabwidth=w^{4α}，得到`a+O(w^{α−η₀})`，除以P保留率。u先小于min(α,b)，l、η₀更小，就得到radial所需的slab指数。4α≤ζ_r/100、uniform/Frostman参数小于真正η₀^rad及固定box homothety的幂余量均有明确次序。

## 7. weighted Kaufman law及多个charts：通过

A稿§7给了独立的law证明，不只引用Lemma22.3的distinct-image counting。target和parameter可有原标签/重数，分别具有1-和2-Frostman cap。对距离约r的target pair，若projection差≤q，则horizontal displacement至少c r，参数落宽Cq/r的strip；2-Frostman用O(r/q)个balls盖strip，给质量≤C K_Λq/r。乘target shell的C K_Ur并求dyadic和，得到collision积分≤`C K_UK_Λ q log(2/w)`。

对每个q用point-local mass Markov，再对parameter作Markov，统一所有dyadic q。`K_UK_Λ≤w^{-β_K/8}`时，坏parameter和每个好parameter的坏target质量都可控为w^{β_K/8}；保留的原target pushforward law具有`w^{-β_K}|I|`的interval cap。该证明不需要target image均匀分离，也不把无重数setcap误当law cap。

径向thin-tube给每pin的actual angular law的2-Frostman upper。在最大坐标chart中，斜率bounded且可对U作相应坐标置换。root终稿显式删mass<w^u的至多6个light charts，总绝对质量≤6w^u；heavy chart归一后的参数cap损失为ζ_r+u。要求ζ_r+u+η₀<β_K/8，WK的bad参数/target各≤w^{β_K/8}。取χ小于min(η_r/10,u,β_K/8,2q−2u)的一半，再l≪χ，全部常数和删除量都可小于p⁸。有限charts不需免费固定第一坐标。

另删|v|<w^q的质量由P的ball cap控制。余下|v_i|≥c w^q，所以原v·U的O(w)-interval对应归一投影宽O(w/|v_i|)，upper为`Cw^{1−β_K−q}`。这是真正对原右time对的质量估计；root没有遗漏norm分母。所有bad-pair/right-time质量均在µ_P²×µ_B²上，以W≤1计费，l后选小可小于p⁸/2。

## 8. final cover矛盾和参数次序：通过

剩余W仍有cp⁸质量，输出只占`w^{-1+κ−Cl}`个working intervals。平均固定一个good pin pair和一个interval，得到right-time pair lower≥`w^{1−κ+C'l}`，与上一节`Cw^{1−β_K−q}`冲突。等价地，把upper乘全局cover数，也直接小于W的lower。

参数能按root所写顺序实现：κ固定，先取β_K、ζ_r及chart预算；α sufficiently small，b固定；取radial threshold（确依slab指数b_r）；再取u及norm预算；BSG内部精度选到l远小于u、Kaufman exception指数；最后选原η₀/抽样η，再令w小。BSG的常数取得之后才选原graph loss，未见参数循环。原ε₂任意固定，sampling输出的b=min(ε₂/4,1/10)>0足够；ε_*只需先依κ缩小。

**因此完整finite weighted engine在明确named BSG/uniform/radial输入下通过。** WK法则及抽样/先验/矩阵恒等式/周期质量是本轮已展开部分，不把整个WZ高级证明说成已独立重跑。

## 9. actual conditional middle-τ application：通过其条件范围

另审 `R0025_conditional_mixed43_middle_tau.md`。F/G、空间input/output同步除L，working w=e/L，确保持unit norm与near-output误差O(w)；仅缩F/G而不缩A或working resolution会错误，当前稿没有此问题。

new weightedfit回原F的误差至多`L h_new A(LP)`，所以确需`L h_new≤σ`。root显式支付此条件，没有漏掉L。先固定engine的允许ε，再选physical ε₁、ζ₁，使`2p≪(ε₀−2ε₁)ε_engine`，最后小取loss，就有c ε_engine>2p和额外L余量。

τe≥δ由保留的最终误差项保证；所以缩τL后的spatial base r₀=δ/(τL)≤w，所有AD查询合法。另一方面source ν的fine base d=δ/ρ≤ρ³，loss小后w≥ρ²，故d≪w，timecap在新engine所需全部r≥w可用。w≤ρ^c保证precision(2)；w≥ρ²使旧nonfit mass ρ^β≤w^{β/4}，engine质量指数可取β/4。

空间heavy-frame计算通过：真实τ-patch的fine质量lower、每working cell容量upper及全cover upper都来自原AD/已付heavy patch。occupied-cell数量upper不能只凭fine point-count upper；root终稿已明确用full original Y的AD lower，在各occupied cells附近作分离小ball packing，再以常数扩大patch的AD upper求和。input/output都这样处理，未给任意裁切patch免费AD lower。删light bins只损K固定幂的reference质量；g≤1允许按其density选threshold。保留bin有上下capacity，才能换Uniform A_minus；按fine input conditional average取g并round x只增O(w)。A_minus的card lower从保留fine总数除单binupper得到，output扩大patch的packing upper给A_plus/A_minus≤K^C。

κ_engine=min(κ/2,1/2)为cardinality里的K余量留严格buffer，也处理κ=1端点；所有K换成w小幂后再低于finite η阈值。所有actual AFF/retention/stability损失必须可在这些fixed精度之后小取，稿件明确保留这个前提，未制造尚未证明的ell3 AFF。

因此实际application只排除**满足已列whole-matrix AFF等准备的middle vector-τ alternative**。large-τ的投影稳定、matrix AFF存在、mixed43其它alternatives、其它五维cases和general/Hausdorff仍未由此解决。没有新维数界、真实Kakeya反例或重大/新颖性认证。
