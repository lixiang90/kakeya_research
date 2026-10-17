# R0064：原联合质量、精确平稳链与phase I反攻

2026-10-18，B。仅编辑assigned文件，无Git／spawn。已读先写working_spec4／macro6、STATE顶部／R63next，实际读WZ2609.22035v1 Def3.6／3.9／17.2–17.4及(157)–(159)，对照R18、R23、R28、R45、R58冻结。§§1–4保phase I历史筛查、非本轮结果；root正式追加spec§§5–7后，唯一phase II为raw weighted rank-one-difference分类及edge-only误扩张反攻，实际数学见§§5起。未经外部同行评审，不声高维／重大结果。

## 1. 原对象及不能免费替换的量

d5、k=ℓ3时p=(x,y+f(z)x,z)，x,y∈R²，f(z)∈Mat(2,2)。原X_y,z具有δ^η-full二维水平质量，Y_z为2−κ维AD并在原跨time尺度保union-AD；Φ_p为κ-AD且γ-slab Frostman。原T是joint参数4-AD／CW族，θ(T)=(φ,ξ_p+f(z)φ)+Oδ。粗cell中ξ与used Φ的关联由Def17.2(4)给，不是可按管独立重选的f／ξ。

管p→p′使用同一原T的真实访问；水平p↔p̃使用同一原(y,z)-grain。原(157)的matrix-time-angle平移仅在这些共同tuples上成立，原(159)是总路径数，不表示每个给定起点、条件clock或条件angle都均匀。原AD4是整tube参数的尺度计数，也不是在这些条件化后的AD下界。

Def3.6的dyadic参数与usual bounded-clock graph tube可固定倍转换，不能因此把一个原tube的δ^η-dense visits补成全clock。R18原W已保联合observed A及marginal恢复费用；R28同base十六边box已付，但不产生迭代作用域或fresh端点独立。R58反模型未造原A／g，所以不能单凭它否本轮完整源。

## 2. 精确平稳联合算子可造，但它本身没有新几何

在真实有限E上记incidence R={(p,T):T∈T_p}，d_p=#T_p，d_T=#{p:T∈T_p}；忽略d_T=0的管。令D=max_p d_p。定义subkernel

    S_T(p,p′)=D⁻¹ Σ_(T∈T_p∩T_p′) d_T⁻¹。

它对称，row sum恰d_p/D≤1。加上对角self-loop 1−d_p/D得到Markov kernel P_T，因对称而以uniform(E)为精确平稳law。点数常数K的比较不在此处按链长累计；AD used-angle给d_p≈_Kδ⁻κ时，非loop总概率仅保证≥K⁻C，不应称固定常数。

水平grains按(y,z)分割E，定义P_H(p,p′)=1/#G(p)（p′∈G(p)）亦对称、row sum1。P_TP_H保持uniform(E)；P_TP_HP_T还自伴。所有跳转是原同管访问／原水平grain，没有新points、smooth f或independent angle／clock。

必须另记原prior：上述active-step的normalized tube marginal为d_T／Σ_Td_T，**不是**原uniform(T)。wholeline给d_T≤Cδ⁻¹，原总incidence lower若已付到Σd_T≥K⁻C Nδ⁻¹，可得此tube law≤K^C Uniform(T)，但不保逐管lower或原AD lower。先筛heavy tubes再重生链又会改变各点degree，不能照抄原point／conditionalclock下界。精确stationarity在这里仅指原point-count marginal；不声tube／angle／time参考同时无损平稳。

但这套构造适用于任意有限incidence graph及任意点partition，完全未使用CW、tube-KT、matrix非线性或wholeline跨scale信息。故仅有平稳性、守恒或算子命名不能作为新高维机制。L步path history相对fresh参考的支配也不能由终点平稳性改成O(K)：即使generic uniform K-state identity chain每一步joint density≤K，相对L+1份独立uniform prior的整条history density仍为K^L。此为一般probability责任，不是已保全部原source的正κ反例。

## 3. κ=0的literal完整配置：平稳不送全局mixing

给δ dyadic足小及固定η>0，取γ=η/2。所有坐标取[0,1/2)内δ-grid，Z为该time grid，E为满五维grid。取f=0、ξ_p=0，Y_z满二维grid、X_y,z满二维grid；每p取Φ_p={0}，其原tube为支持线(b,z)、b=(x,y)固定的vertical graph tube。T由所有四维intercept b组成，原canonical slope θ(T)=0。通常／dyadictube转换只固定倍，保整个bounded clock。

原joint tube参数是固定斜率×满四维intercept网，故4-AD常数O(1)：ρ≤1/2的occupied dyadic parent恰有(ρ/δ)^4 children，较大ρ只差固定边长常数。任意convex U含M根whole tubes时，各clock截面的δ-intercept boxes有bounded overlap，给|U|≥cMδ⁴；#T≈δ⁻⁴，所以原CW常数O(1)。E／Z／X／Y及跨time union-AD均满足Def17.2的κ0版本，ξ和粗used-angle关联精确不变。原实际shading有固定正密度。

singleton Φ是0-AD。对宽r≥δ的任意slab，含0时其normalized mass1≤δ⁻ηr^γ；Y_z满二维网在r×τ tube的r-cover≤C(τ/r)，而(τ/r)^γ≤δ⁻γ≤δ⁻η，故tube-KT(1−γ)成立，固定C用γ<η的余量吸收。因此这是literal Def17.4参数范围内的κ0配置。

这个配置中P_T只改变time，P_H只改变x，两者及任意长composition都保持y∈R²。E有约δ⁻²个不沟通分量，不存在全局Doeblin lower或全局mixing，尽管uniform(E)精确平稳、whole T为AD4／CW、水平grains全满且ξ完全coherent。

范围不能偷扩：γ随η取η/2，不满足正κ source应用所要求的η≪固定γ；κ0本来也无dimension deficit。因此该例只严排“literal全部配置的平稳⇒全局mixing”，不反完整正κ分支、所需η(γ)小参定理或Kakeya。不能把它记成本轮主任务已结案。

## 4. phase I候选的拒绝和真正未付门槛

直接选择“存在平稳链／原marginal不涨K^L”应拒绝：§2对任何图成立，§3显示它不带空间增长。每step计数多、uniform marginal或(159)不能替原条件clock／angle／跨grain的混合下界；将原g抹成独立reference会回R18／23／28失败责任。

若继续联合算子，唯一可能有新内容的形式应是有原量词的近不变集逆定理：某F⊂E有中间原质量，管与水平两类actual edge的外流都小，是否迫原f在保质量clock片近affine／linewise，或产生真实convex tube concentration？这会同时使用whole straightline visits与full horizontal grains，不能只读standalone D-law。不过当前尚无这项inverse的证明／完整反例，也未证其不等价于旧全称gain或旧action／rank提取；仅作为给root的待筛建议，不擅自立phase II命题。

正式数学前还须明确保留的原measure、每step active概率、time-support、γ／κ／η次序、链长及其K^{CL}费用，并排R13点态/bracket平滑捷径、R23cycle prior、R45有限endpoint及CP⇔PM。该链筛查现已按root决策停止，不以spectral／mixing名称重开已有障碍；它不算本轮数学成果。以下只推进已正式锁定的矩阵门槛。

## 5. phase II：具体矩阵双曲线与真1AD有限time

固定c=1/8，δ=2⁻ᴺ，N≥3。取

    I_−=[−1,−1/2)， I_+=[1/2,1)，
    Zδ=(I_−∪I_+)∩δZ， #Zδ=δ⁻¹，νδ=Uniform(Zδ)。

这是尺度δ至1的真1AD概率：任意occupied中心的r-ball质量在c₀r与C₀r之间，任意interval upper≤C₀r，r≥δ，常数不依δ。两branch各质量1/2。写u=2t+3∈[1,2)（t∈I_−），v=2t∈[1,2)（t∈I_+），定义

    F_−(t)=c diag(u,u⁻¹)，
    F_+(t)=c [[0,v],[v⁻¹,0]]。                  (10)

两branch间有固定gap，故F在整个Zδ上有固定Lipschitz常数，且||F||≤1。若要全[-1,1]的smooth bounded延拓，可在gap内用固定smooth cutoffs接合；νδ不在gap放质量，所有下述恒等式和常数均不变。不能据此假原source f有光滑性，这只是反模型自身更强性质。

令g(t,s)=1_(t,s在不同branch)，对任何额外独立概率reference变量也取同一g。它对称、0≤g≤1，原质量精确1/2。diagonal／offdiagonal两平面在det的polar form下正交，且det F_−=c²、det F_+=−c²。因此每个cross pair准确满足

    det(F_−(t)−F_+(s))=c²−c²=0。               (11)

同branch的精确式为

    det(F_−(t)−F_−(s))=−c²(u−u′)²/(uu′)，
    det(F_+(t)−F_+(s))= c²(v−v′)²/(vv′)。       (12)

于是同branch不同时间的差全rank2，而且绝对det≥c²|t−s|²。全raw pair的bad概率在epsilon0下精确为1/2−δ，不在raw定理的小q regime；原g边上的bad概率则精确0。这就是必须保留的量词差别。

## 6. 全real affine weighted非拟合：有限δ格误差

本节||·||明确取max-entry norm，某entry达到其值；若改operator／Frobenius norm，2×2中的等价常数并入Ch，结论相同。对任意real矩阵R,U、0<h<h₀，采用bounded-clock常见归一精度h(1+||R||)，有

    νδ{||F(t)−Rt−U||≤h(1+||R||)}
                         ≤C√h+Cδ。             (13)

证明：F在全部Zδ有固定Lip常数L。若||R||≥max{2L,1}，取达到max norm的entry；任意两个fit times由该entry差式给

    (||R||−L)|t−s|≤2h(1+||R||)，

故全部fit times位于长Ch的interval，1AD给≤C(h+δ)。若||R|| bounded，允许误差≤Ch。负branch的F₂₂=c/(2t+3)、正branch的F₂₁=c/(2t)二阶导数均有固定正lower；减任意affine函数仍保持该lower。每branch的|scalar residual|≤Ch集合至多两个interval，强凸性使各interval长度≤C√h（两端／中点二次差即证）。每interval与δ格相交数≤length/δ+1，故得到(13)。如归一还包含||U||，任意非空fit与bounded t、F先给||U||≤C(1+||R||)，小h后同结论。

因此任意fixed a_*>0及0<b₀<min{a_*/2,1}，在δ充分小时，h=δ^a_*的全部real affine fit质量≤δ^b₀。有限格的单atom δ下限已显式保留。它不是仅排bounded slope或某预选affine拟合，也未把数值样本当证明。

## 7. 任意保原g质量选择的单plane障碍

设L为任意affine common-image或common-kernel plane，因而L内任意两矩阵之差det=0。若F(t),F(s)都在N_τL且τ≤1，取相近L点并用bounded F上的det Lipschitz，得

    |det(F(t)−F(s))|≤Cτ。

同branch结合(12)，fit time集直径≤C√τ，故每branch

    νδ{t∈I_±:dist(F(t),L)≤τ}≤C(√τ+δ)。

对任意0≤g′≤g，只要两端均限制于该同一plane邻域，不论g′如何依赖额外原变量，积分仍有

    ∫g′≤C(τ+δ²)。                              (14)

τ0时每branch至多一个time，故最多Oδ²原g质量。若τ为fixed正幂δ^b，(14)排任意小lossδ^o(1)的保质量提取，而不是仅排一个固定time subset。即使容许adaptive选择L，常数也对所有L统一。

nearconstant分支亦不能救edge-only结论：负branch F₁₁≥c，正branch F₁₁=0，故一个半径r₀<c/3的matrix ball不可能含cross两端，保g质量精确0。若输出是C a-ball，只需取允许的a<c/(3C)。所以把raw“几乎所有原pairs determinant小”改成“仅g用过pairs determinant小”是严格错误，不因真1AD、bounded smooth可延拓F或(13)而修复。

本例可附任意独立AD／slab角law，定义真实代数D=(t−s)(F(t)−F(s))ψ，但未构造A-output relation、原T／xi／CW及Def17全数据。结论仅否这个weighted finite门槛，不反完整source、raw分类或Kakeya。

## 8. sqrt(q)删除量的raw sharp校准

另取raw probability law μ=(1−2p)δ₀+pδ_(E12)+pδ_(E21)，0<p<1/20，F bounded。只有两个ordered rare cross pairs的det为1，其余det0；故epsilon0时q=2p²<1/100。任意affine image／kernel plane不能同时含E12、E21，因为它们的差rank2，所以至少删p质量；保原0及一个rare点可恰只删p。

一个半径<1/10的nearconstant ball也不能同时含这些不同atoms，至少删2p。对固定充分小plane邻域仍由det Lipschitz排两rare点同时拟合。故在raw定理已允许的任意概率空间中，所需删除量至少c√q，不能统一改为o(√q)。它不需要time1AD或SM，因为raw分类本来没有这些假设；不是source反例。

## 9. raw定量分类的实际独审与当前范围

已actual全文读A13并逐式独核§§8–12，raw分类无必修。H={bad-degree≤√q}质量≥1−√q；三个合法原anchors各删≤√q，最后保≥1−4√q。非nearconstant支先选||A||op>a，再SVD得diag(σ,τ)，σ≥a、τ≤epsilon/a；所有good原点B满足|B22|≤6R epsilon/a²，不能漏a次幂。自product与两good点的difference-product分别≤epsilon+2Rd、epsilon+8Rd，均由β=64R²epsilon/a²覆盖。

β≥1时大误差平凡；β<1时d≤√β。若B12皆≤4√β即统一common-kernel，否则取一个B12>4√β的good anchor，任何C21>4√β会使difference-product>(15/4)²β，矛盾。因此保留集在同一common-image plane附近，不按time另选row／column。q0只删有限个零测邻居；epsilon0用精确消元、不除√epsilon，同样分类，原atom／重复labels全合法。

原reference明确为概率σ×ν²×π，0≤g≤1在两个time坐标限制到Z0时，未归一质量至少m−8√q；不能当独立事件写成mν(Z0)²。归一后time上界与SM命中率付ν(Z0)⁻¹，AD lower不自动保。矩阵plane误差e0=O_R(√epsilon/a)在规范D中仅给O_R(e0)，真实时空换尺度另付s_t s_F/s_y；只有该误差小于working r且原SM／KT／floor均对齐时，才能接R16。common-kernel仍为原二维耦合，不由此排除。

因此本轮raw条件结构缩减与本稿edge-only反例相容：前者假设整个independent原ν²下badpairs≤q，后者raw bad≈1/2却让g全避badpairs。源bounded g不提供这个raw假设，raw badmass大也不送actual good-rank stars。主稿／macro／next最终全文范围另见指定formal，不认证source全分支κgain、重大性或新颖。原grain-chain候选已停止，不续概率／threshold常数轮。
