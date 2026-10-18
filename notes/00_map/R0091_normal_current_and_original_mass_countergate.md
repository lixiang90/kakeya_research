# R0091阶段I：全clock PSD测度、normal currents与原质量资格门

2026-10-18，B。只作已锁reselection阶段I的实际输入／反攻审查，恰八个编号节；不先锁新gain，不把高级定理的条件结论当ordinary完成。未经外部同行评审。

## 1. 实际恢复、来源版本与本轮可检验责任

实际全文读GOAL、当前STATE、全部ROADMAP、registry全部78条ID／状态、R90终macro六节和next六节、R91 reselection_spec五节。R90 root十节／两gate八节／两formal六节上轮已actual全文审，沿parent同提交恢复记录使用，不重新冒一次数学或官方bytes检查。parent核父c6a8c3a…／tree ded12…／1387 clean，本人未Git、改元数据、下载或创建代理。

实际官方history核Alberti–Massaccesi–Stepanov[1907.07456](https://arxiv.org/abs/1907.07456)最新v3=2022-11-21，不能将v1编号直接当当前稿；De Philippis–Rindler[1601.06543](https://arxiv.org/abs/1601.06543)最新v2=2016-04-11，不是v3。先打开的旧v1仅作定位，以下结论以actual打开的v3／v2为准。

actual读AMS v3引言Th1.1／1.3、Cor1.4／Th1.7和§2.10／2.12／2.14的normality、tangency与C1分布定义；另核Cartan公式及§3 key-identity的statement接口。DPR v2实际读Th1.1、Remark1.3、Th1.10、Cor1.12–1.13及§3相应normal-family／Div应用证明。不冒两文高级wholeproof、AMS所有§4或全部外部GMT基础已新独证；未下载／视觉核PDF。

任意集扩展另以经典Jankov–von Neumann选择为具名输入；有界一手比对实际读Bertsekas作者公开[Appendix A](https://www.mit.edu/~dimitrib/DP2_Measurability_Appendix.pdf)的Borel／analytic／universal定义及Prop A.5 statement：Borel空间的lower-semianalytic目标在取到minimum处有universally measurable exact selector。以下0／+∞目标正好落其假设，不冒其引用的全书proof新独证，也未下载该PDF。

本轮具体问题是：同一个真实K的全unit segments能否给一个满足这些定理的measure，并由其结论获得原局部满秩／可调用四维输入？有限任意marks若代替wholeclock，必须重新核边界；filled X与粗coherence若代替C1／normal高维current，必须给实际构造，不能只换术语。

## 2. 四完整路径、旧冻结与新增输入是否足量

ordinary初始化仍缺small Lebesgue footprint、原方向／位置／clock和全尺度联合结构的同时提取；direct-HRZ仍缺完整parent／terminal／narrow费用；sticky临界κ1、其余mixed及ordinary桥仍开；真实反例仍要同一个集合满方向与严格Hausdorff upper。DIM001／R38／R80已有链不重排，R90已付polar normal law亦不重名。

这次normal-current／A-free输入在形式上不同于cut／cone／polar和给定-g sum-product：它确读取完整clock的分布微分约束。但是否有用取决于原measure的**局部**polar、同一支配measure和真实boundary。若只得标准奇异部分rank约束，不给新原mass或源structure，就不是完整branch saving。

旧CP／PM／PW4的全称正幂闭包、R72 basicness／更多time、R76共同root law／Schubert障碍、R79–80共同域／cross-block责任均保持。将其所缺local rank、独立Alberti表示、C1 plane field或normal3-current放进成功假设，不是本轮新输入，也不能以“current observability”改名解冻。

## 3. 同维hull的全clock选择、PSD measure与endpoint公式

先限compact K⊂B_R，且每个unit direction v有一段a+[0,1]v⊂K。可行集

\[
 \mathcal A=\{(v,a)\in S^4\times K:a+[0,1]v\subset K\}
\]

是compact、各fiber非空；因K闭，只需检验所有有理clock。compact-fiber的标准可测选择给一个Borel a(v)；不授连续、Hölder或可微选择。方向用归一球面面积σ，clock为[0,1]的Lebesgue概率。令F(v,t)=a(v)+tv，定义

\[
 \Lambda=(F(v,t),v)_\#(\sigma\otimes dt),\qquad
 \mu=F_\#(\sigma\otimes dt),\qquad
 S=F_\#(v\otimes v\,\sigma\otimes dt).
\]

S是同K上的有限PSD矩阵measure，trace S=μ；若以Euclidean矩阵范数取total variation，则|S|与μ双边可比，不必误写成完全相等。对任意compactly-supported C1向量test field，沿每条真实线积分，得row-wise divergence

\[
 \operatorname{Div}S
 =\int_{S^4}v\,[\delta_{a(v)}-\delta_{a(v)+v}]\,d\sigma(v),
 \qquad |\operatorname{Div}S|(\mathbb R^5)\le2.
\]

正负号取Div对test的负导数定义；normal1-current boundary与之反号。这是finite measure RHS，通常非零；无需选择a(v)的导数。各行是normal1-currents，但某行可在一部分μ上消失，不能因此免费说μ同时被所有行mass支配。

总质量与局部数据要分开：全方向／全unit clock确给\(S(\mathbb R^5)=\int v\otimes v\,d\sigma=I_5/5\)。方向限制保原比例p时，未归一质量／endpoint上界均相应按p变；条件归一后方向cap常数付p^-1。这里原σ／clock由真实全segments给出，不由有限dense marks替代。

**这套资格构造可扩到任意原集合，而非必留compact缺口。** 设原K⊂R5不要求可测、有每方向unit segment，h=dim_H K<5。取s_j↓h且s_j>h，用Hausdorff外测度的open-ball covers构造Gδ hull G_j⊃K、H^(s_j)(G_j)=0；可同时令每层cover直径趋0、费用趋0。令G=∩_jG_j，则G为Gδ、K⊂G、dim_H G=h。写G=∩_mU_m，U_m open。关系

\[
 R=\{(v,a):a+[0,1]v\subset G\}
   =\bigcap_m\{(v,a):a+[0,1]v\subset U_m\}
\]

是Gδ：每条compact segment若包含于一个open U_m，与其闭补集有正距离，所以对应(v,a)条件开。R⊂S4×R5为Borel且投影满S4，Jankov–von Neumann给universally measurable a(v)，不要求fiber compact或a有界。等价地作者Prop A.5可对R上0、其外+∞的Borel目标精确选择，全部v的inf0已取到。

用完成的σ及σ⊗dt定义pushforwards。a的完成σ可测性使F在product完成measure上可测：零方向集乘[0,1]仍为零；故joint／physical pushforward在Polish目标上是有限Borel probability，从而Radon。S及endpoint向量measure同样finite Radon，因为v bounded而总概率1；test field紧支撑，积分分部和上述TV≤2、I5/5不需要anchor的一阶矩或boundedness。第4节joint5-Frostman及physical1-Frostman也不依赖anchor有界。

此时只能声\(\mu(G)=1\)，不能声spt μ⊂G，也不能声新选择的segments在不可测原K内。由于h<5，G为Lebesgue-null，S／μ全部奇异，足够DPR的原应用。若能由这套measure推出dim_H G=5才会反原h<5；本稿没有该推论。这个扩展支付了集合范围，属于资格正向闭包，不是新的gain，也不删除其它局部rank／regularity缺口。

## 4. Joint 5-Frostman不授physical 4-Frostman或local rank

对product metric的半径r球，v落S4的r-cap，σ质量≤Cr^4；固定v时F(v,t)落physical r-ball的clock长度≤2r。因此真实joint probability有\(\Lambda(B_r(p,v))\le Cr^5\)，无需a连续。投影到physical μ时却不能继续保r^4因子：方向不再受一个r-cap限制，只自动有μ(B_r(p))≤2r。这是projection降维信息的实际缺口。

严格校准用同一个full-direction全clock族：a(v)=0，0≤t≤1，K为闭unit ball。对0<r<1，μ(B_r(0))=r，不是4-Frostman。μ在punctured ball有density c|x|^-4；disintegration后的local matrix为

\[
 M(x)=\frac{dS}{d\mu}(x)=\widehat x\otimes\widehat x,
 \qquad \operatorname{rank}M(x)=1\quad\mu\text{-a.e.}
\]

但全局积分仍I5/5，K及union有正五维体积。故全局五个独立方向矩不推出μ-a.e.五个局部独立方向，也不推出存在uniform local ellipticity。该例保真实全方向、compact、unit clock和endpoint budget，但本身体积大；不是Kakeya／smallshadow／完整sticky反例。

将σ分成方向cones得到多个normal currents也不解决同measure问题。原点bush中不同方向cone在physical空间除原点外可互斥，原点μ为零；这些current即使各自有大mass，也未给一个正μ同时绝对连续于各个mass。不能拿global相交或总和满秩替DPR的共同分母。

## 5. DPR当前定理确适用，但结论只是奇异部分的rank上界

实际[当前v2](https://arxiv.org/html/1601.06543v2) Remark1.3允许Aμ为finite measure RHS，Cor1.13直接处理Div矩阵measure有限的情形。因此上述endpoint RHS非零**不是**DPR适用的障碍；不应将它误判成必须先闭合成cycle。

Div的symbol是Mξ，wave cone为rank≤4的5×5矩阵。故DPR给\(\operatorname{rank}(dS/d|S|)\le4\)在|S|的Lebesgue-singular部分a.e.成立。它不是rank1定理，也不约束绝对连续部分。若原K为Lebesgue-null，S全部奇异；由于PSD，选其kernel内非零ω时

\[
 0=\omega^TM(x)\omega
 =\int|\omega\cdot v|^2\,d\Lambda_x(v)
\]

说明该条件方向law支撑于一个局部hyperplane。然而ω仅可测、随x变，没有C1、统一hyperplane、逐scale power或原point-law lower；这是定性约束，不是DIR4／PW4输入。

DPR v2 Th1.10／Cor1.12还要求共同正μ满足μ≪||T_i||并有μ-a.e.的独立orientations，才能推出μ≪Leb5。若另外假S的polar在正μ部分full rank，矩阵结论同样可推出该部分绝对连续；这个额外局部满秩恰是原任务未证明的内容，不能由∫S满秩赠送。高级A-free proof本轮保具名，§3应用的symbol／共同分母已实际核。

## 6. AMS的C1 tangency与normal3-current缺项不能省略

[AMS当前v3](https://arxiv.org/html/1907.07456v3)的normal-current主结果需要一个真实normal k-current T=τμ，并切向于定义在open Ω上的C1 k-plane distribution V。它按V与第一commutators的张成维数给非involutive处的absolute-continuity结论；不是任意measurable plane law的Frobenius定理。k=1的C1 line distribution本来自动involutive，单条normal1-current不能直接提供k=3的应用。原finite filled X、ξ的dyadic粗coherence没有给这样的C1 extension或uniform BV边界。

“有三个独立normal1-currents，所以它们的wedge就是normal3-current”甚至作为一般current闭包也不成立。一个具体校准在Ω=(-1,1)^5：取bounded f(x3)∈{0,1}但f不属BV，例如无穷交替区间的indicator，令

\[
 T_1=e_1\,\mathcal L^5,
 \quad T_2=(e_2+f(x_3)e_4)\,\mathcal L^5,
 \quad T_3=e_3\,\mathcal L^5\quad\text{在}\Omega.
\]

三者finite mass、Div均为0，故在Ω都是normal，且对同一Lebesgue measure独立。形式3-current

\[
 Q=[e_1\wedge(e_2+f(x_3)e_4)\wedge e_3]\,\mathcal L^5
\]

的boundary含\(D_3f\,e_1\wedge e_4\)，不是finite measure，所以Q不normal。若先归一各orientation，两个binary-valued系数也仍非BV，不能修复。这个例子只否免费wedge操作，不排另作有证明的normal3-current，也不是原Kakeya配置反例。

因此即使source某point的方向张成一个3-plane，也不能据它定义3-current就默认normality；更不能将那个plane field默认C1、给Lie brackets或以ambient a.e.微分性返回δ^η满的原离散点集。AMS integral／normal、C1／finite-perimeter及边界条件的层级须保持，不能把其结论反过来当构造假设。

## 7. 任意稠密shading的boundary可为δ^-1，三类闭包分开

上述Div≤2来自完整unit clock的端点。若在一条线只保χ_J(t)dt，normality取决于χ_J的一维BV；有限个interval给boundary为所有端点，而任意可测J可根本无finite-variation boundary。仅有|J|≥λ不控制端点数。

这可在**真实全方向**族上同时验证，而非重复同dir标签。用第4节原点bush，取δ=1/(2m)，对每个v都取

\[
 J_\delta=\bigcup_{j=0}^{m-1}[2j\delta,(2j+1)\delta].
\]

每条真实线的clock density恰1/2，保原全部方向。相应PSD measure的Div是交替半径spheres上v加权的pushforward；不同正半径spheres互不交，且每sphere上v由physical point唯一确定，所以其variation各为1，不会通过方向积分相消。半径0项至多损一个固定量，于是\(|\operatorname{Div}S_{J_\delta}|\asymp m\asymp\delta^{-1}\)。原每条线平均／逐管density都好，却不保全clock的uniform boundary budget。该例K有大体积，只反免费boundary继承。

finite tubes的任意measurable三／五维shadings还不必是精确轴上的dt限制；若要从它们构造current，须写真实截面平均、mass／support和边界分布，而不能仅取cover shadow厚化替原Lebesgue E。Whole-label删选并保完整segments可以保endpoint总量（计原权重p）；删clock／marks则不保。平均λ转逐管heavy会损真实W／N，仍不能恢复BV或每pair相同clock。反向逐管到平均成立，但不是current boundary的闭包。

## 8. 阶段I资格结论与严格停止

已先消息parent报告：compact全clock PSD测度确有finite Div，DPR定理合法适用；normality不能因endpoint非零而被错误拒绝。但其singular rank≤4、全局moment满秩、joint5-Frostman都没有提供所需local rank／physical4-Frostman或四维source。真实bush及full-direction alternating clock分别检验这些免费推断；没有反完整H5或null Kakeya集合。

当前无qualified阶段II gain命题。若要继续该大路线，必须有不同且真实的原输入，例如从同一个原measure付出局部独立current／uniform regularity或不同PDE结构，而不是把它们写入成功前提。本轮不以三个normal1-current、filled X、假BV／C1、全局rank或正密度阴影完成它；也不将desired local ellipticity换名为新的关键定理。

已actual全文独读A `R0091_transport_measure_and_source_gate.md` 八节。逐式核其s_n open-cover同维hull、Gδ段关系／共同measure、PSD endpoint／wave cone、centered bush density及sphere校准：\(S_{\rm sph}=(I-\omega\otimes\omega)\sigma_4/4\)确有trace σ4、global I5/5、rank4和Div=−ωσ4。球面局部切向law虽可旋转平均成global全方向边际，却没有whole straight segment；不能将它用作完整Kakeya反例。A在本次实际应用范围未发现强制修改。B自身构造仍须由root／A独核，不以自审替代。

对compact K的选择／全clock构造及任意原K的同维Gδ hull／universally measurable selector扩展已逐项支付；后者不声compact化或选择仍在原K中。不能再把该已付扩展伪列为唯一缺口。真正未付仍是同一个原physical measure的局部独立性／regularity及最终增益。当前定性source资格判断不能当Hausdorff5、ordinary新界、完整branch-saving、新ID或major。有限检索和未找到合格机制不认证所有PDE／currents策略无用，也不证明文献absence。

本稿恰八个编号节，只有授权路径；未Git、元数据、下载、新代理或formal。原完整Goal与四路保持，R90 actualprogress和保守streak13分开，后续需parent先锁具体工作规格再施工。高级wholeproof／项目应用审查／外部同行评审三层未混同。
