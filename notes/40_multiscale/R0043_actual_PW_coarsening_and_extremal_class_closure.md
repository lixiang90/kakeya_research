# R0043：PW粗化、无权先验与实际§18的闭包预算

2026-10-17，root。研究总目标仍为普通高维Kakeya。本文补R42尚未支付的coarse接口，检验WZ实际§18是否能携带新BS条件；不宣五维κ≤ζ或新维数界。BS及WZ其余结构定理/高级输入仍按文献具名使用；有限核与原质量推导交两独立全文审查。未经外部同行评审，不认证新颖/重大，不增同义结果ID。

## 1. 本轮命题与必要范围修正

固定整数n≥2、m=n−1和presentation指数A，P(E)=(1+E)^A。所有管在同一clock I=[−1,1]上，初始graph tube宽δ；允许dyadic parameter tubes，只比较整个clock截面。原有限law ν满足：对所有半代数S、presentation复杂度E≥1、0<λ≤1，

    ν{i:q_i(S)≥λ} ≤ C0 P(E)|S|λ^(−n),
    q_i(S)=|T_i∩S|/|T_i|.                           (PW)

有限coarsening引理可用任意原权，甚至subprobability；但WZ K_d及其极值类用**无权管计数**。因此actual加强类中ν必须是同一T的uniform counting probability，或显式支付该计数对ν的domination G。parent K⁴结论还须fixed bounded joint chart/总count量级；原Def17.1字面R^d与Def3.6的b∈R^m没有明写该全局限制，不能只从local AD推出。本轮的加强极值类明确采用有界chart规范；无界类免费限制到单chart并未证明。R42 nextspec仅说whole-tubeprob而未明注这些点，本轮不认证任意不相关ν/无界local-AD的字面class闭包。这些是已标出的scope实修，不把自由改先验或localization当合法步骤。

主要结论是：共同clock粗管原权pushforward保PW，常数只乘固定维数/管形常数；AD(m,K)下无权coarse及coarse-in-parent新常数分别≤C_n C0K²、C_n C0K⁴。presentation指数A不变，无ρ/δ或额外λ费。随后逐项匹配§18；条件性更换极值类必须用其自身κ_PW，不能用旧κ。

先作restriction、平均/逐管、双向排重；独立反攻极小λ、微小S、重复indices、不同parentaxes、dyadic边缘、shortclock、相对新尺度及无权化。若闭包成立仍须尝试actual S/M/E strictsaving，没有saving不认证高维gain。

## 2. 任意原子族的平均形式：事件质量不可丢

对任意原index集合H，原质量a=ν(H)，记B=C0P(E)|S|。原PW在H上给tail≤min(a,Bs^(−n))。在s0=(B/a)^(1/n)处分裂积分（B≥a、B=0直接处理），得

    ∫_H q_i(S)dν ≤ c_n B^(1/n)a^(1−1/n),
    c_n=n/(n−1).                                    (1)

H可由即将测试的粗管/S/λ决定，无独立性要求。不将H归一化；否则C0/a须显式保留。反取H={q_i≥λ}又恢复PW至固定常数。因此tail与原子族mean在固定n下等价，单独这一重述不算新机制。粗化证明必须保a因子；整族mean后直接Markov不够。

## 3. 共同平移核：fine PW真的推出coarse PW

设k_r为R^m中B_r的归一化指标函数。δ≤R时，在|y|≤R有B(y,δ)⊂B_{R+δ}，故

    k_R(y)≤2^m (k_{R+δ}*k_δ)(y)                    (2)

在整个空间成立。对同一细轴c_i(t)=b_i+t a_i及同一clock积分，Tonelli给

    q_i^R(S)≤2^m average_{u∈B_{R+δ}}
                       q_i^δ(S−(u,0)).              (3)

现在固定H={i:q_i^R(S)≥λ}及a=ν(H)，先用(1)测试每个S−(u,0)，再对u平均。所有测试体积、presentation均与S相同；无穷平均没有被当作一个集合并。因此

    λa≤C_n [C0P(E)|S|]^(1/n)a^(1−1/n),
    ν{q_i^R(S)≥λ}≤C_n C0P(E)|S|λ^(−n).             (4)

无R/δ、λ或权跨度损失。它比仅测N_RS的粗推断强；R42的NρS困难并非不可能性证明，本轮已用(3)补齐。

实际coarse map i↦j将每细管分到一个ρ管，其轴与细轴在整个I内距离≤Cρ。粗管包含于原细轴宽R=C'ρ的inflated graph tube，体积之比固定，故q_j^coarse(S)≤C_nq_i^R(S)。将阈值改λ/C_n并用(4)，得到raw pushforward ν_ρ(j)=Σ_{i↦j}ν_i的PW常数≤C_nC0。不同轴误差无需不同S_i：先固定倍包住，再对所有原轴使用同一个u分布。

dyadic D(p)在|t|≤1的截面为intercept cube加t倍slope cube，围绕中心参数轴内含c_nδ球、外含C_nδ球，整管体积≈δ^m。以其内接fine graph作(2)输入、外接coarse graph作输出，比较q只花固定常数。无需NρT留在dyadic parent内，无需删端部，所有微小λ均适用。原(19)的clock与此完全一致。

## 4. 无权coarse、parent与K⁴费用

令原fine集合T uniform，joint AD(m,K)如原Def3.9。对每occupiedρparent，finecount n_j∈[K^(−1)L,KL]，L=(ρ/δ)^m。若J为coarse管数、N=Σn_j，则uniformcoarse对rawpushforward的密度比为

    (1/J)/(n_j/N)=N/(J n_j)≤K².                     (5)

因此uniform DρT的PW常数≤C_n C0K²。该比较是实际parent的双边计数，不是默认pushforward均匀；若删成T'，须用T'自己已证的AD常数。

以下parent常数还要求原joint参数在固定有界chart中，等价地此处显式用N≤C_nKδ^(−m)；只有局部r≤1 AD而允许无界远隔copies不够。actual§18采用固定box的X/原Obs3.4(22)总count规范，本结论将其列作实际使用的额外全局输入，不伪称原Def17.1字面已写。对wholeτparent，原质量p_τ=N_τ/N≥c_nK^(−2)τ^m。这里(a_τ,b_τ)取原Obs3.2 dyadic parameter cube的lowercorner，令原ψ精确送dyadic网到新dyadic网；第3节的center只用于内外圆截面/kernel比较，不能混用后免费沿用occupied-bin lower。使用原(20)的共同变换

    ψ_τ(x,t)=((x−b_τ−a_τt)/τ,t).

clock保持，volumeJac=τ^(−m)，R42已证公式给新constant≤C0 τ^m/p_τ≤C_n C0K²。condition在该parent后仍uniform、AD常数K；再coarsen至ρ/τ并用(5)，故

    C_PW(ψ_τ(DρT[Tτ]))≤C_n C0K⁴.                  (6)

这与CW Obs3.4的K⁴费用同量级。原law若只有arbitrary weighted AD而非cardinalAD，(5)不自动成立；必须保实际权的parent比较。shortclock q<1时原C r^m/(p q^m)仍适用，(6)没有豁免q^(−m)。这里全部为whole-clock操作。

若只知所有marks在一个固定box，且平均density≥δ^η，则active管intercepts有界、#active≤C_nKδ^−m，而#active≥cδ^ηN，故N≤C_nKδ^(−m−η)。此版本p_τ≥cδ^ηK^-2τ^m，(6)额外付δ^-η，仍可进后述subpower预算；它没有将全局marks免费局部化进box。无界远隔L份parallel满网local AD不变、global最优PW常数约1/L，而单parent常数约1，说明无界时精确C0K²表述确实过广。保真实τ^m/p公式始终有效。

## 5. Shading、tube restriction与actual§18对应

原shading删选只改Y，不改whole-tube ν，PW不花shading密度。若删掉整条管只保T'，p=#T'/#T，则uniform T'的常数C0/p。原平均density为λ0、保留的总shading incidence比例为f，每管shading至多|T|，所以p≥c fλ0；不能由平均density断言每管都dense。

实际Def17.1/18.2起点现在取uniform-PW加强类。Steps1–3的Y0与X' uniformization保留至少δ^{O(η)}δ_ell^{O(η_ell)}原incidences，故T'的p有同阶lower；原(3566)–(3572)还给T'自身AD常数≤Cδ_ell^{−O(η_ell)}。由(1)–(6)，T'及其coarse、parent可携带PW，额外费用仍为δ^{−O(η)}δ_ell^{−O(η_ell)}。source参数先选η足够小，使δ^{−O(η)}可吸收到δ_ell^{−o(η_ell)}，不能只说“都是subpower”。

Step4 (107)–(113)有两种平均责任：wholecoarse family的平均shading与parent内的平均shading。**(107)/(109)实际调用未按ell删成T'的原T_ρ、原T[T_ρ]及原Y**，其新增PW/AD费用为δ^{−O(η)}；不能拿T'的δ_ell^{−O(η_ell)}去声称可吸入更小ε1，原hierarchy ε1≪η_d≤η_ell不允许那样做。随后(110)用Y'≤Y和uniformity回传。原Step1使每p的incident coarse纤维数在activeparents间uniform；先以global平均density和AD计数选一个dense parent调用极值估计，再用multiplicity uniform传回其它parents。PW在(6)对任意parent均已成立，故此原平均→代表parent机制不新增PW费用。没有给每parent或每管免费逐管dense。

Steps5–6的点/slab剪枝、横slice AD整理改变的是E和shading；无需每层将whole prior重新归一。最终实际tube操作是τ=√δ_ell、ρ=δ_ell的coarse-in-parent，(6)适用。原内部点剪枝层数J可随η变化，但没有J次PW重归一；真正tube coarse/parent链在18.1后至多固定维数控制的有限次数。

## 6. Clock、相对尺度与极值量词

本节保留原(19)/(20)的共同clock。PDF72将parent转竖直时可使用其已有ψ_τ：先共同bounded shear x↦x−b_τ−a_τt，再横向归一。a_τ有界，前一shear只固定畸变；空间旋转可在t=constant中选横向basis。point/plane、横截面及dyadicLip的固定常数随之调整，whole-line段无需延长。coarse计数始终沿原dyadic tree（或连同其共同image树）进行；改变描述basis不许可默换任意新axis-aligned网格后免费使用occupied-bin AD lower。本文不宣任意旋转后新建更长clock的管也自动保PW。若坚持其它clock选择，须额外证明实际管比较并支付crop费用。

设δ'=ρ/τ≤δ^χ，χ>0由实际参数选定，则δ^{−Bη}≤(δ')^{−Bη/χ}。为目标loss η_*，选η≪χη_*/B后才可归入新类。原18.1 PDF74 Lemma5.3明确τ/ρ≥δ^{−χ(ζ)}，所以此处有真实正χ；原18.2对最终δ'=√δ_ell则需δ_ell≤δ^χ_ell。可先取阈值ρ_j=δ^{a_j}，0<a_1≪…≪a_{n−1}<η0且a_jη_j/η_{j−1}≫a_{j−1}，再取原η≪min_j a_jη_j及所有调用的允许loss。于是δ_ell≤ρ_ell保证χ_ell≥a_ell>0，δ^{−O(η)}可吸进δ_ell损失。所有a_j在δ前固定，不能事后依赖未知countersequence调η。此处只付新增PW的预留，不认证原全部几何最佳模数。不能将δ'接近1的任意scale也叫subpower无损。

全尺度multiplicity估计可用screen补边界：若δ^{−Bη}≤(δ')^{−η_*}且δ'够小，使用加强类极值性质；若不满足，则log(1/δ')<Bηlog(1/δ)/η_*，AD的trivial管数≤δ^{−O(η)}(δ')^{−m}≤δ^{−O(Bη/η_*)}。选择η更小，将其吸收到预留δ^{−ε1}即可。在原(111)–(113)最终δ_ell误差预算中取ε1≪χ_ell η_ell，不能在未付范围机械使用(107)的ρ-only误差。

定义K_{n,PW,A}(κ)时使用同一**有界joint-chart、uniform counting-PW**加强类，η控制AD、CW、PW和平均shading；不使用旧κ。该类的κ_PW下确界具有原∀ε量词：从任意κ'<κ_PW+ε/2的有效估计吸收κ'−κ_PW，可得endpointκ_PW的ε形式。原§18只调用此极值性质及结构/均匀化输入；(5)–(6)、restriction及scale screen正支付新增PW hypothesis。因而**在原§18其余结构推导与具名输入成立、采用上述保clock实现及有界规范的条件下**，其抽取可以带出同指数A、任意小loss的PW。不是把原κ或任意现成Def17.4配置追认为新类后代，也不认证所有无界local-AD原class的同一抽取。

## 7. 18.1升级及未冒称的source修复

18.1 Step1 (141)–(142)按Lemma5.3选ρ<τ、只在Y/Y_z中删选，再作Dρ与ψτ。只保shading不花PW，若丢wholeindices则按原density记p；(6)和真实χ(ζ)将费用纳入下一η_j。全维grains矛盾及Step2的ell下降至多有限维次数，输出PW常数仍为原常数、AD常数和保留质量的固定幂，A不增长。slice的ϕ_{y,τ}只分析点集，不拿每个y的frame作PW测试。

Step2重新按18.2抽取与Step3 (145)的一致性调整，tube层仍只有上述restriction/coarse/ψ；最后将δ'厚至(δ')^{1−O(η'/ε_j)}，用(3)–(5)处理真实粗管并保持shading。调整E的低量级误差不等于给任意pipe另选S_i。故无需加入all-coarse PW公设，也没有complexity指数迭代增长。

版本化原文PDF70定义Δ_J≈δ_ell，PDF72却在同j=J处又写Δ_j=√δ_ell；这是实际index措辞不一致。本文只核明确的最终tube操作D_{δ_ell}[T_{√δ_ell}]，不把两尺度强说相等。若重证全部grain几何，应在已有层级中使用Δ_j≈√δ_ell的中间层并核其密度；本轮不为结束任务伪称已完整修复源proof每个几何细节。上述结构抽取表述仍列原其余结构推导为输入，有限PW闭包本身不依赖此index。

## 8. 实际strict-saving尝试：直接测试visited union

通过closure后，按停止条件实际选Sδ为原输出shading的δ-cubes并，再加固定数邻接δ-cubes。它是有限半代数集，volume |Sδ|≤C_nδ^n|E|δ≤δ^{κ−O(η)}。原marked cube只与T相交，不可直接把其整块体积当|T∩S|。这里邻接扩张确实修复：把标记cubes有限着色，每色互距≥10δ；每cube选一个与T的接点p，Sδ包含B(p,cδ)，而bounded-slope graph cylinder在该球内体积≥c_nδ^n（clock或截面边界处也有固定体积分数）。同色小球不交，故|T∩Sδ|≥c_nδ^n #Y(T)。这保真实平均M≥δ^{O(η)}，无需把平均shading改成逐管dense。PW mean给

    |Sδ|≥c δ^{O(nη)+η}/P(Eδ).                       (7)

但一个N-cell presentation复杂度最多C_nN，N≈δ^{−n+κ−O(η)}；这只是巨大已付复杂度上界，不给P(Eδ)=δ^{−o(1)}。以BS当前有界poly budget直接代入，只能保证lower约δ^{A(n−κ)+O(η)}，没有一般可验证的strictκ余量。native grains可将每个X-slab写成一piece，计数约δ^{−(n−ell+1−κ)}，仍不能从原AD/dyadicLip得到低复杂度或严格余量。未知的minimal presentation复杂度不能被宣小，也不能由我们选的粗上界倒推“所有包络都不可能”。

因此这次真实S/M/E尝试未排κ>0。closure是可用性进展，不是full(3,3)或ordinary高维gain。未证明一般K进入jointAD/CW加强类；满方向网只给PW的R42校准继续保留。没有用lowcomplexity公设替代待证提取。

## 9. 排重与本轮停止

若另有满维angleFst，coarse和parent后再次调用BS也给PW；不能把那一子类的重述叫新机制。本轮核证明不要求angleFst，平行满transverse family已有PW却方向单点，故是较宽class的实际闭包。原PW全称S/H再加共同kernel是数学原因，并未证明旧CP⇔PM或CW全称already给新正gain。

本轮完成有限任意权粗化、AD无权化/wholeparent、实际操作与相对scale预算；原结构抽取仍按第6–7节条件边界，不声fullsource独证。下一不再调PW closure常数或加allscale定义；直接visited-union的complexity尚未付，须找实际不同结构测试。提前macro据此选下一真正高维机制。无新数学结果ID、priority/major认证，Goal active。

## 10. 独审状态

A/B须实际全文读本文10节、双方稿、macro与nextspec，逐项审任意权事件质量a、dyadicshape、K⁴、uniform-law修正、平均shading、clock和source条件边界。最终以正式reviews/rootintegration为准；归档哈希检查不替数学。新BS输入与本项目有限推导、条件source抽取、高维gain四种状态分别记录。
