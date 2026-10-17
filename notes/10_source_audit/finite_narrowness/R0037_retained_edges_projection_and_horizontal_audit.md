# R0037：retained edges、三投影比较与完整 horizontal 前端

2026-10-17，A独立源审计。唯一主任务为原version2正有限窄度完整分支；本稿支付其§7及§8前端，不把它独自当§9已通过。实读原PDF页109–137/提取5803–7332行，以及官方 `06a-retained-edge.tex`、`07-finite-narrowness.tex` 的相应公式；8.2复用UNB证书，不重命名新scalar结果。GOAL/STATE/R37spec及冻结账已读。具名高级输入的确切statement/application与其全proof分开；未经外部同行评审，无新维数/重大性声明。

## 1. 命题依赖、closure与反攻入口

前端图为：7.1保原graph edges →7.3共同endpoint sets与固定长度scalar expression closure →外部乘法卷积Fourier定理/7.4 flat coefficients →7.5 collision强迫parallel strips →7.6 retained-edge rigidity →7.7原line-incidence affine–skew row。另一方面UNB的8.2 →8.3 true/projected双向列表 →8.4三wideinterval给proper candidate，或8.5变horizontal k=ℓ →8.6 hidden sheets affine →8.7 bounded residual/deep states →8.8 slope bounds →8.9 fulltime coefficient counts。后者交给§9的critical/bootstrap/returnwide，收到全稿才正式审整branch。

合法restriction只保原raw upper/support；新conditional palettes/current floors逐次用reference预算重付。uniform graph抽样只作有限组合论，回incidences必须保original edges并存原point weights；Σqν_Q预算、完整ν_Q、ordinary time分别核。旧OBS002没有这里真实scalar parameters/first-coordinate rectangle cap与原edge回传，不反本source。若完整原uniform工具再次调用即推出候选，只登记复用，不把G(u)/阈值改名新方向。

独立反攻重点：只保BSG vertices却丢edges；固定κ丢原prior；fixed expression length与慢对角混淆；pointuniform与rawµ混用；不同Φ的marginal witnesses按pair数复制；thin sliced label中免费续floor；共同coefficient field只在两axis却未去bilinear项；huge affine L导致fine state/ joint cap缺失；wholebox只计最后交集；success-L条件prior冒fullassignment。以下逐项支付；未发现当前前端合法counter。

## 2. 原7.1：三条路径而非只保顶点

G⊂A×B有≥θa0b0 edges。先删A侧degree<θb0/2，剩A0及≥θa0b0/2 edges。τ=θ³/512；uniform v0∈B令U=N(v0)∩A0。Jensen给E|U|²≥θ²a0²/4；bad ordered pairs（common-neighbor<τb0）被同v0覆盖概率≤τ，故E Bad(U)≤τa0²。存在U满足`|U|²−(32/θ)Bad(U)≥3θ²a0²/16`。

删badpartners>θ|U|/16的vertices，至多半数，得|A′|≥cθa0。令B′中每v与A′至少θ|A′|/4邻居。A′旧degree≥θb0/2，故保原edges≥θ|A′|b0/4≥cθ²a0b0，且|B′|≥θb0/4。对每u∈A′,v∈B′，至少cθ²a0个u1既邻v且与u nonbad，每个有τb0个共同v1；得到≥cθ⁵a0b0个原三步walk。

walk↦(u+v1,u1+v1,u1+v)∈C³对固定(u,v)injective，alternating sum是u+v；不同sum的triples不交。因此`|A′+B′|≤Cθ^{-5}|C|³/(a0b0)`，同时原edge下界仍在。round A、κB到h-grid时vertex/edge multiplicity最多K/K²，pull back所有selected vertices保原edges；不把多重index silently合并。得到7.4。

## 3. 原7.3：共同sets与固定长度scalar closure

L=h^{-1}，Aκ×Bκ都在大小≤K²L²的同一universe。独立κ,κ′的intersection期望≥L²/K⁶。选represented κ0及mass≥1/(2K⁸)的indices，使intersection≥L²/(2K⁶)；各单侧intersection≥L/(2K⁷)。置A*=Aκ0、B*=Bκ0，原Gκ0在其中的edges≥L²/K。保留/归一κ-law只付subpower，κ/κ0仍正exponent interval cap。

写 `d_h(U,V)=log[N_h(U−V)/(N_h(U)N_h(V))^{1/2}]`。Ruzsa triangle的cover版本由代表差值+separated V的injective pair计数证明；round/mesh改变只付K。小cross sum给Aκ、Bκ的small self-difference，large intersection再用triangle连接到A*,B*。E=A*、F=−κ0B*满足 `d_h(E,F),d_h(E,tF),d_h(E,tE)=O(logK)`（t=κ/κ0）。对固定长度product p_j=t1…tj，以common dilation的K^{O(j)}费用归纳得d_h(E,p_jE)、d_h(E,p_jF)=O_j(logK)。

固定-iterate Plünnecke–Ruzsa以标准具名形式使用（原7.6），不从generic small doubling声称无限closure。它给E+E小，故负product也可用triangle。对每signed-product dilate U，cover lemma把U放进K_H个E−E的translates加K_H h-neighborhood。任意固定数量这些dilates的和再由fixed-iterate bound覆盖≤K_{m,H}L个h-cells。若c是≤H个signed products之和，`cX⊂Σ ε_jα_jX`（左侧同一个X点，不需右侧独立），即使c=0也合法；从不除消去后的c。由此7.8的**所有固定长度表达式**uniformly成立。

所有product factors范数/逆范数K，只需fixed次数的mesh细化。最后common dilation K不改exponent。m,H若随N无限增长，不能直接调用；先每fixed tolerance选finite m,H，再慢对角吸收常数。后面正是此顺序。

## 4. 原7.4/7.5：flat law与collision proof

真实新具名输入为Orponen–de Saxcé–Shmerkin，[*On the Fourier decay of multiplicative convolutions*, arXiv2309.03068v2](https://arxiv.org/abs/2309.03068v2)，v2=2024-02-27。已网页核定义与Thm1.5/Remarks1.8–1.9，并由root统一下载；只认证statement/application，不重证其全proof。其输入为[-1,1] Borel probabilities、s_j∈(0,1]、Σs_j>1与**single-scale smoothed** energies≤r^{-ε0}，输出在r^{-1}≤|ξ|≤2r^{-1}的乘法卷积power Fourier decay；不要求support避0。恰对原7.10，而不是只用finite full-energy corollary。

取R≥sup|T|为subpower，λ=Law(T/R)。原ratio interval cap在h≤u≤1给λ(B(x,u))≤K′u^S；Ru>1时trivial bound与R^S吸收。选0<s<min(S,1)、fixed n满足ns>1。dyadic annuli给`I_s^r(λ)≤C_sK′`，h≤r≤1；r∈[h,h^{e0}]时K′≤r^{-ε0}，e0>0 fixed、N足够晚。因此ω=λ^{⊠n}在h^{-e0}≤|ξ|≤h^{-1}有|ωhat|≤|ξ|^{-τ}。fixed kτ>2，C为k份乘积的和；compact-Fourier-support非负majorant给

`P(C∈[x−h,x+h])≤Ch∫_{|ξ|≤h^{-1}}|ωhat(ξ)|^k dξ≤Ch^{1−e0}≤C_e h^{1−e}`。

n,k先fixed，所有C都是7.8允许的expression乘共同R^{-n}。独立C_i,D_i可外部采样，既不依赖原endpoint law，也不要求sourceκ与edges独立；这里只用对每coeff tuple都成立的support closure。

对7.5，µ为至少h^{-2}/K个**原Gκ0 edges**的uniform law，保first-coordinate rectangle capKh²。设width w=h^{1−ε}的parallelstrip-pair最大质量p(w)≤h^c。取m个独立edge pairs，v_i=a_i−a_i′、u_i=b_i−b_i′，q=h^{ε/2}、Δ=qw/10。矩形cap求边缘给P(|v_i|<q)≤CKD(q+h)。若有|v_i|≥q且全部wedges≤Δ，fixanchor和primededges后，其余每unprimededge落一个parallelstrippair，概率≤p(w)，彼此独立。因此bad-small-wedge概率≤[CKD(q+h)]^m+m p(w)^{m−1}≤h³，m先取足够大。

对每coeff tuple，两个同µendpoint sums Z,Z′独立、共同support≤K_m h^{-1}，CS给P(|Z−Z′|∞≤h)≥h/K_m。反向先fixendpoints；有wedge>Δ时只留两个相应flat coefficients随机，它们仍独立。preimage是area O(h²/Δ)、perimeterO(Dh/Δ)的parallelogram，至多K/Δ个h-squares；每square概率≤C_e²h^{2−2e}。于是collision≤h³+K_m h^{1+ε/2−2e}=o(h/K_m)（e<ε/8），矛盾。不能把overflow数量或generic加法entropy当此wedge概率。

每fixed ε,c遂有p(h^{1−ε})>h^c；慢对角给widthK*h与mass1/K*，K*subpower但不声称是旧K固定幂。first-coordinate cap又给`m0≤CK(D|q01|+w+h)²`，因此strip方向的horizontal分量inverse-subpower，common slope/interceptsK*。undo F=−κ0B*保持slope与原edges，得到7.6。

## 5. 原7.7：两份冻结law、第三投影与恢复点质量

row T boundedK，每positionξ-cell至多K个E-bins（E≥ξ），T·(1,v)沿indexed trajectory近constant至KE。令V0=(ξ/E)T，point cells为(z,V0)_ξ，总数≤Kξ^{-2}。对directionbin d，投影 `P_u(z,V0)=(z·Ju,V0·u)`，真实line两个坐标均constant upKξ。

**第一份law µ_cov**先删weight/ordinarytime太短的indexed lines。prior×dt domination使剩每line有ordinary witness长度≥1/K，走过≥1/(Kξ)个pointcells。相隔Kξ的投影值使用不交witness pointsets，故每direction整个当前projection只需Kξ^{-1}格。此support cover冻结，后删方向不需要重新有长line。

删π(d)<ξ²的bins，其总µcost≤Kξ；paletteweight dyadic pigeonhole保M个comparablebins，总πmass≥1/K，所以其uniform direction-law继承positive exponent cap。归一当前µ为**第二份law µ_pt**；每point-directioncell质量≤Kξ²/M。删light point marginal<ξ²/K1与lightedges<ξ²/(K1M)，再删lowdegree points，保≥ξ^{-2}/K点、degree≥M/K。所有点的floor是**冻结µ_pt**的旧marginal，不是uniform graph新造的prior。

在每点，direction interval cap给≥M³/K个三元separatedslopes。average固定v1,v2及≥M/K个third directions，各third有≥ξ^{-2}/K commonpointneighbors。两投影endpoint A,B各≤Kξ^{-1}，pair有K pointpreimages；第三投影写

`u_d=c1u1+c2u2`，`κ=c2/c1=(v_d−v1)/(v2−v_d)`，`a+κb=c1^{-1}P_{u_d}(z,V0)`。

κ及逆K，third uniformlaw通过inverse-Lipschitz bound继承intervalcap。prescribe(a1,b1)两个ξ-interval把z限制K个cells，每position上V0仅K选项，因此Gκ的first-coordinate rectangle含K原edges；uniform law capKξ²。是7.2全部hypotheses，而非只知道总endpointcardinality。

7.6保原edge≥ξ^{-2}/K*，故有≥ξ^{-2}/K*个原pointcells。其strip等式 `V0·u_i=b_i+λ0 z·Ju_i+O(Kξ)` 反演，注意 `z·Ju=−Jz·u`，令λ=−(E/ξ)λ0即可得原结论 `T=B+λJz+O(KE)`，无源sign错误。恢复这些pointcells的**全部µ_pt incidences**，用其冻结marginalfloor ξ²/K1回dense原质量；方向可以在selected graph之外，因为row估计只依point，且未恢复冻结µ_pt之前已删的incidences。

undo后B,λ初可能大；若|λ|≥N^c fixedpower，|T|≤K把dense selected base质量放入radiusK/|λ|球，jointcap求和给质量≤K(K/|λ|+ξ)²为power-small，矛盾。故|λ|≤K，一occupiedpoint再给|B|≤K。原time t始终不改，不用再选择新的endpointlaw。

## 6. §8.2 projected groups：8.2的真实c与weighted support

有限ℓ数据a_s=N^{-s},h_s=N^{-ks},g_s=N^{-ℓs},b_s=h_sg_s；原true Q_s质量ν_Q∼a_s^d h_s b_s，whole assignments在每timeblock disjoint。开始任意substantial residual，按原parentweights平均选dense typical parent；其后µ≤Kνdt，π仍原majorvelocity palette。

α=([v]_χ,[Z0]_χ)，weight wα=π([v]_χ)χ；γ把(Y0,Y′)分g_s bins，prior pαγ。normalize Y by g_s且condition full groupprior，scalar8.2的c为 `wα g_s/pαγ`。在normalized(t,Y) σ-cell内积分原jointcap，Z宽χ、Y宽g_sσ、timeσ给numerator≤Kσ²wαg_s p^d，除pαγ即inputcap。

support不能由此cap推：一个Q_s给某velocitybin至多Kh_s/χ个Z0 bins，每α只有K compatible γ，normalized(t,Y) area≤Kq_s b_s/g_s；stable Q_s graphs每σ-cell只K个X_{a_s} bins（χ、σ先细于所有axis/graph误差）。乘wαg_s再对α、vel bins求和，单true labelcost≤Kq_s h_s b_s。用Σq_sν_Q≤1和ν_Q∼a_s^d h_s b_s得总weighted support≤Ka_s^{-d}。

删weighted-support相对pαγ过大的groups按此总和收费；再删poorconditional-success groups按prior预算收费。非空remaininggroup的cap/support/dense质量还给c±1 fixed-polynomial bounds，故UNB的8.2可uniformly调用。输出Φ_s的原active floor `wα a_s^d β_s/K`，β_s为原Y宽，`g_sσ/K≤β_s≤Kg_s`，wholeunit fit与adaptednormK。whole assignments在原(α,γ)groups之间也disjoint；有限depth顺次调用时refloor其current marginals，既有floors只作storedwitness。Σ_Φwαa_s^dβ_s≤K。

## 7. Lemma8.3：共同domain、两色reference与双向列表

短domain D的time q=min(h_s,β_s/g_s)、midpointY宽m=qg_s、Y′宽g_s。entry reference为 `T_D=q wα a_s^d m`。true-label侧：对subblocks、α、K slopechoices、Kb_s/m positionslices求和≤Kq_sν_Q；projected侧≤Kwαa_s^dβ_s。所有floors先按此summable budget准备，stable common subboxes也仅K重数，不按partner个数复制witness。

两图在同normalized D-comparison ball上holomorphic algebraic、normK、value在pairedpoint相差Ka_s。原jointcap沿α积分给每index-base marginal≤K T_D times normalizedarea；共同eventpoint在极细cell内jitter后成为exactdensity，不换trajectoryprior，margins保证value误差仍Ka_s。

若discrepancy M0/a_s有fixedpower，则按neighboring finite center-jet bins分组，所有图离同参考O(M0)，每index在fixed M0只进入bounded多个groups。每色存储witnessfloor T_D/K，cap在KM0宽度给groupcard≤K(M0/a_s)^d。rawbadmassB及两色reference totals W_c满足某group `B≥(W1+W2)/K`（总reference预算K、全badmassdense）；另B≤KW_c。给色c用prior p_i=T_i/W_c，normalizepair后index-base density≤Kp_i。Cor3.4因此在**真实badpairlaw**上适用，排fixedpower discrepancy；慢阈值给normKa_s。

最后每retained Φ的整个stored marginalwitness在commonball内，且其图接近固定Q图Ka_s，故把floors在purecap下求和只容K个Φ；反色同理。这给given(α,D,Q)的Φ短列表与反列表，不需要每index在current pairlaw有lowerfloor，也不比较neighbor paletteweights。

## 8. Proposition8.4：三wideinterval的两尺寸比较

在s,s+u,s+c2投影，a1=aN^{-u},a2=aN^{-c2}；c2<(1−d)u/4。β_max≤Kg_s，`b_s/β_min+h_sβ_max/β_min≤N^{−(C_d+3)u}`，C_d=10/(1−d)。short D此时time∼q_s、Y宽b_s；给Q,α只K coarseΦ。

另取longdomain timeρ=β_min/β_max、Ywidthβ_min，JacobianA；色i reference是A wα a_i^d，仍有summable floors/marginalceilings。若M0/a≥N^{C_du}，其card

`(M0/a_i)^d≤(M0/a)^d N^{du}≤(M0/a)^{d+d/C_d}<(M0/a)^{(1+d)/2}`。

所以Cor3.4可用严格小于1的统一dimension，保每色自己的a_i^d factor；normdiscrepancy≤KaN^{C_du}。长→短的normalizeddiameter≤K(h_s/ρ+b_s/β_min)有额外N^{−(C_d+3)u}，故difference在whole短fiberbox变化≪a_i。得到 `X=F_Φ(t,Y)+D_i+O(Ka_i)`，D_i常数≤Ka；givenQ,α,Φ仅K(a/a_i)^d offsets，反向Φ_i→Φ仅K。source finestΦ1 entries的rawreference `q_s wα a1^d b_s`预算K。

展开Q坐标z=(t−t*,Z−Z*)/q_s，U=(Y−Y_Q)/b_s：`F_Φ=f0Φ(z)+f1Φ(z)U+f2Φ U²`。f1 affine、f2 constant。目标误差e=aN^{−(1−d)u/2}≪a2。

### 8.1 同fine state的nonconstant coefficients确实相同

先用fine state(Q,z,U,X)原deep-history K知识、summable floor重付conditionalv≤Kπ。采source，再按同state条件独立采target；保source rawΦ1 ceiling，不除每sourceentry currentmass。fixsourceentry/target χ-velocitybin，先把time切足够细，targetintercept只K α选择；wholeQbox只K shortdomains/coarseΦ。fine Φ1 label仅新增K N^{du} offsets，不改变derivativepolynomial，故targetcoarsepolynomiallist只有K。

若f1/f2差≥e，固定tinytime后U上的derivative gap除长度K N^{-τ}外≥eN^{-τ}，τ=(1−d)u/8。逐offset的matching length≤Ka1N^τ/e，乘N^{du}得K N^{-3(1−d)u/8}；两项都power-save。按tinytimebin长度积分，不乘bin数；rawsource normalized (time,U) ceiling≤K q_s wα a1^d b_s，targetkernel≤Kπ。对reference budgets求和，排negligible coefficient-disagreement pairmass。这一步没有假source/target与projected label独立。

### 8.2 共同field：Cartesian后必须去mixed term

条件平均在每fine state选一coefficient pair并保dense mass；再refloor palettes、选Q相对q_sν_Q dense。原z-marginal≤Karea。palette平均固定两separated细velocitybins，grid步ω≪χ先定，directions/states比ω更细；故每axis fiber只K α及K Φ，其pair为affine/constant的K列表。各fiber选一项保dense vertices，lightvertexfloor回mass。3×3 Cartesian全顶点概率用两次Jensen≥density^9，anchors separated后固定fouranchors/dense targets，bilinear interpolation给first coefficient、constant给second。

不能把bilinear直接称affine。用**fiber选择前**µ_Q的原角bound `µ_Q(v近任一axis)<K m_Q r^S`，选inverse-subpower r慢到该质量低于最终fittedmass。剩dense non-axis rawfamily由fullν_Q×dt domination有某indexedline ordinaryduration q_s/K；其fixedα,Q onlyK coarseΦ，故一Φ在q_s/K时间成立。bilinear的两basiscomponents都inverse-subpower非零，其沿line quadratic系数= mixedcoeff×两components。与affine f1Φ的差在long times≤Ke，Remez迫mixedcoeff≤Ke。删除它后才得真正affine C1、constant C2。

### 8.3 减P_nc后的second scalar projection与proper candidate

`P_nc=C1(z)U+C2U²`总degree2。给fine z与fixed v_χ，residualX−P_nc在a2只K(a/a2)^d bins，来自K coarseΦ与D2 offsets；e≪a2。去velocity条件另append(z,residualbin)state，原endhistory只有K选项，lightdenominator成本以Σweights≤Kq_sν_Q付；每state兼容πmass≥1/K，对π积分给同bin count。不能只取每velocity的列表union。

normalize原质量byq_sν_Q，沿U积分，原basevolume q_s²b_s乘p^d再除q_sν_Q（ν_Q∼a^d h_s b_s）给scalar cap K(p/a)^d，含角π。UNB8.2输入c=a^{-d}、terminala2、same fixed fullν_Q条件prior；若需bounded轨迹只condition参加且coeffbounded者，其prior≥1/K，不给新AD下界，输出原mass只损K。optional角使horizontalwidth∼1，某label normalizedmass≥(a2/a)^d/K、wholeQblock quadratic prediction；恢复P_nc得full-base quadratic、原mass q_sν_Q(a2/a)^d/K。

X若nativeP*，newtest=P*−predictor，hidden一/二阶derivative继承，nativecurvatureK≤K/a2；X若bounded residual(w−L)/a_r，restore w=L+a_r x给special affinehidden derivative1/curvature0。都是proper同block time-candidate，不是只有goodpoint。AIM负责回原尺度，不把analysisK当actualslack。

## 9. Proposition8.5：否则变horizontal且k=ℓ

若三depth全β∼g，取u>0够小使ks>(ℓ+C_d+3)u，8.4宽度条件成立。否则somefixed s有β_s=N^{-B0+o(1)}、ℓs<B0≤ℓs+M。取r>s且 `(k+ℓ)r>B0>ℓr`，故b_r≪β_s而g_r≫β_s。givenQr/Qs-history及finehorizontalposition/velocity（含currenttime），comparison shortD midpoint/slope只有K选项，8.3给K Φ_s，全time interval将Y′限在K个β_s bins。Qr可跨很多D，但position里的time指定当前D；不要求整Qr block只有K D。

normalizeQr：time/Z除q_r，Y减Y_Q并除q_rg_r。transversevelocity `(Y′−A_QV1)/g_r`有K个accuracy E=N^{−(B0−ℓr)}列表。deep row T=(A_deep−A_Q)/g_r的evaluation预测该**轨迹常数**至≪E，尽管T本身可随deep时label变化。以deep-row/location状态palette抽两个velocities先给T normK，再用两evaluation列表及productpalette counting给每horizontalpoint仅K E-rowbins。原horizontaljoint cap归一前Kξ²q_rν_Qπ，heavy Q及fullprior后完全满足7.7。

7.7输出B+λJz。λ fixed-power小就改善原strip；否则λ∼log1，减B·z、除λ得 `|Y′−Jz·V1|≤N^{-e0}`，左侧沿每affine trajectory为常数。childdepths′小时其fixedrow在fine location由两separated v与Jz比较，rowerror≤K(N^{-ℓs′}+N^{-e0})。原child massbudget refloor后timeprojection长≥H/K，second rowcomponent却把t限宽K N^{-ℓs′}，故H=N^{-ks′}≤K N^{-ℓs′}，即k≥ℓ。k>ℓ时freezeJz在childcenter改善nominal velocitywidth g_{s′}，mass仍用H fullνchild/K，给stripcandidate；否则k=ℓ。

在k=ℓ时truechildrow与Jz_center差KH、nominaltransversewidthH²。以 `z_b=(z−z_c)/H`、`Y_b=(Y−Yc−Jz_c·(z−z_c))/H²` 描述**整个true tiltedbox**：slopeKH×horizontalH只多KH²。不是只逼近retainedtrajectory集合。normalize时间为Qr fulltime，prior仍其fullassignment；以后child参考预算不conditionL成功。

## 10. Lemma8.6：先减affine再用contact commutator

在任一smallchild及s′=0的stablebranch/core，误差∆=a_r a_{s′}。highcurvaturecenter已affine；其余simplebranch f holomorphic、有fixedmargin。删短ball/branch linepieces及lightentries按fullchild budget求和，得到long chord与inverse-subpower basefilling；必要fine-state删后重新refloor，但保earlier长witness。

令M_f=dist(f,affine)。ASM在减affine后给所有order≥2 derivatives≤K M_f，不给affine part绝对界。actualdirectionW=(1,v,Jz·V1+O(KN^{-e0}/h_{s′}))，small prescribed depths使error≤N^{-e}。沿longchord f与affine hiddenline差K∆，onevariableASM给Hess_f(W,W)≤K∆。fine state有三separated actualv witnesses，transfer到同point/idealcontactdirection只付K M_f N^{-e}，不付hugeaffinegrad。

记X=∂t−Z∂Y、Zop=∂Z+t∂Y。因(X+vZop)(−Z+tv)=0，(X+vZop)²f恰frozen Hessian test，affine function贡献0。三点插值后 `X²f,Zop²f,(XZop+ZopX)f` 及所需fixed derivatives≤E_f=K(∆+M_fN^{-e})。central T=[X,Zop]=2∂Y，精确恒等式

`X(XZop+ZopX)−2ZopX²=3TX`，
`Zop(XZop+ZopX)−2XZop²=−3TZop`，
`T²f=X(TZopf)−Zop(TXf)`。

依次得f_YY、f_tY、f_ZY，再由X²/Zop²/symcross得全部Hessian≤E_f。Taylor给 `M_f≤K∆+K M_f N^{-e}`，后项可吸收，即使M_f巨大也合法。affinefit与每hiddentrajectory差affine，stored q/K witness只向同block外推；每label K fits。没有引入SCL式绝对高度假设。

## 11. Lemma8.7：fine residual states不受horizontal误差floor限制

选一个parentfit L，x=(w−L)/a_r在参加轨迹上affine且全unitparenttime |x|+|x′|≤K。µ仍按q_rν_Qr归一；ν^flat=ν(.|完整Qr assignment)，**不condition成功L**，µ≤Kν^flatdt。

对任意预声明fixed-power residual/base/velocity meshes，先在bounded-residual currentlaw中以原deep true assignment预算删light ball/branch entries。其true-axis realfilling≥1/K；analytic `g_R=(f_R−L)/a_r`在filledpoints有界K，ASM给norm/derivativesK，即使L的原coeff极大。更深grapherror低于所求residualmesh，再更深label给其true-axis位置accuracy，从g_R恢复K个fine bins。这不用近似horizontal方程超出N^{-e0}的精度，也不需把L在旧tangent mesh上近似constant。

随后append该fine state到旧endhistory，每history只K选项；referenceweights R_e总和≤Kq_rν_Qr。current entry低于R_e/Kcut者按总预算删，给conditional v≤Kπ。purecap在exactbase直接积分width p a_r、中心为L(t,Z,Y)的hiddeninterval，Jacobian/priorfactor消成Kp^d。对pre-deletion weights此purecap也成立；current conditional domination再乘该purecap即joint Kp^dπ。不是把两个无关marginal upper直接相乘。因fine状态知识先由真实g_R支付，不需限制L绝对斜率。

fullchild参考为 `ν^flat(Q_s)∼a_s^d h_s³`、`m_Qs=H_sν^flat(Q_s)`、Σm_Qs≤1。所有后续floors/whole-domain counts用它；bounded participating probabilityprior若另需可花K，但不能换掉这份参考。

## 12. Lemma8.8/8.9：slope telescope与fulltime coefficients

相邻depths的affineentries按childhistory只K配对，先以child完整m_Q预算反复lightpair删除，保wholechild-domain witnesses。twofits在此接近x，affineRemez给差≤K a_prev于wholechildbox；horizontal/transverse斜率分别≤Ka_prev/h_child、Ka_prev/h_child²。在active深点评估horizontalrow，Jz在child中变动Kh_child，误差仍前者量级。从零prediction telescope；对p=1,2，`a_prev/h_child^p=N^{(pk−1)s_child+(s_child−s_prev)}`，depthgap慢趋零使比 `1+a_s/h_s^p` 多的因子为K。grid/pair预算先finite再慢增，得到8.5而非免费相邻点微分。

k≤1/2时ordinaryL_s slopes全部K。按fine d0与P_D=(Z0,Y0)分group，D=a_s^u,u≥1 bounded，WG=π(d0)D²；horizontal误差与d0mesh都细于D。原jointcaps积分moving areaKD²给 timeband cap `K|I| WG ρ^d`，a_s≤ρ≤1。Σ_GWG≤K；删µ(G)≪WG与µ(G)≪ν^flat(G)，得到active/prior都∼_K WG。ν^flat没有先conditionL成功。

support独立用pre-group bounded-residual law的frozen trueQ_s witnesses，mass≥m_Qs/K。D≤a_s≤h_s²（k≤1/2），groupreference motion `Z=p_c+tv_d0,Y=q_c−tp_c` exact horizontal。任何touchgroup的整个truechildbox在同一horizontal enlargement：basevolumeK h_s⁴，而非只最后intersection。unit residualcap+|x|≤K给其base densityK；whole-disjoint witnesses各mass≥a_s^d h_s⁴/K，故每meeting block≤K a_s^{-d} labels。a_s-timebin至多碰O(1) blocks；ordinaryslopesK、D≤a_s使每entry只K scalarbins，总(t,x)cover≤K a_s^{-1-d}。

normalizegroup byWG。coefficient-ball radiusρ的affine trajectories落入widthKρ polynomial band，band cap给active≤Kρ^d；在每dense residual先删相对ν^flat/WG integrated duration太短的轨迹后，转为该restrictedprior的ballcap。5.1（quadraticcoeff=0）给a_s-bin active≥a_s^d/K。若fixed-power light coefficientbins仍有非vanishingglobalmass，ΣWG预算选densebadgroup，再在这些坏bins应用同clustering矛盾。慢阈值得每bin原activefloorWG a_s^d/K、每group≤K a_s^{-d} bins，fullunit-time coefficient assignments。

最后time η≪a_s，按η WG a_s^d/Kcut删entry，总threshold预算Σgroups/time/coefficient≤K。若某storedentry在同timebin碰一个x_{a_s}格，则其整个storedsubbinmass都在K倍scalarband（coeffbin宽a_s、slopesK、timeη）；cap KηWG a_s^d除entryfloor给K compatiblecoeffbins。这是§9所需真实fulltime derivative列表，不能只由pointcount或一次重coeffbin取代。

## 13. 当前结论、具名输入及待全分支审查

前端逐步链未发现保原hypotheses的counter。7.1–7.7保original edges/pointmass/clock；8.3两色reference matching、8.4共同field非axis检验、8.5 actual horizontal wholeboxes、8.6 relative-Hessian吸收、8.7超horizonequation精度fine states、8.9 frozenwholebox/ fullν^flat coefficients均已独立支付。新的Orponen–de Saxcé–Shmerkin Th1.5只核确切statement/application，保具名；标准fixed-iterate Plünnecke–Ruzsa与既有ASM/ISO/UNB输入各明列，不无证清全部source。

此判定还不是完整R37目标。§9 criticalsame-law paths、G(u)每dense inputbootstrap/endpoint、2k>1/2k<1回wide及最终AIM连接，由root/B完成后本代理须实读全稿与B独稿，在另指定review给真正fullbranch审定；不得仅本前端通过登记完整finite窄度或高维结论。
