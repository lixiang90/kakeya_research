# R0099：浓集值分布、原直线耦合与既有有限broad估计

2026-10-19，B。先读reselection5并报告两primary的实际声明，后实际全文读施工前锁定的working5，再作以下证明。仅编辑本稿，无Git、元数据、PDF下载或新代理。高级来源wholeproof仍具名，未经外部同行评审。

## 1. 恢复、读域与四完整路

实际读当前STATE、R98 next6／root integration review6、旧R91 root10及R99两spec各5节。GOAL、registry78和完整ROADMAP既有冻结的本会话审查范围复用；root已运行本轮一次context，本人不重跑或把截断的context长输出冒作完整新读取。R98真实测度应用与更强旧strong-L²排重是progress，ordinary／完整branchsaving时钟21另计。

四完整路仍须保留：ordinary任意原K的初始化及Hausdorff返回；HRZ全部parent／terminal／narrow费用；sticky完整rough分支与ordinary桥；同一集合full方向unitsegments的严格低维构造。GR不被粗称R91的同一定理，FT不被按题名或R3旧范围拒绝；反过来，新paper也不自动提供原质量或ambient出口。

实际网页读GR `2608.20899v2`（2026-09-11）Def1.3／Rem1.5、Th1.6–1.10及1.12、§4主定理的Choquet／生成接口；FT `2608.31164v2`（2026-09-09）§1主声明、§3 Prop3.4／Cor3.5和证明接口、§4 Th4.1及应用证明。两者current history已核，不声高级heat-flow／Choquet全证明独证。另实际读库存CV `1205.6371v1` intro及weighted Theorem1的任意方向wedge版本。

## 2. 两个GR结论与实际输入，不能混成一个

令A为一阶常系数算子，值空间有限维。原Def1.3的浓集序列须有L¹范数1、趋零于measure、弱星measure极限无domain边界质量，并收敛其Frobenius／Euclidean单位值球上的质量加权值分布。Rem1.5允许非零A u_j=w_j，但仍须w_j的L¹一致有界且趋零于measure，不能换成任意bounded distributional RHS。[实际来源](https://arxiv.org/html/2608.20899v2)。

Th1.6的分解只约束各component的barycenter落wave cone；并非每个原值都落wave cone、总barycenter奇异，或component保留空间位置。Th1.7再要constant rank及wave cone张成整个值空间，才可令component自身也由相同PDE的浓集序列生成。后者确超出R91单measure奇异polar的范围，不能因旧DPR已知便否定它；但其生成序列没有被声明为原unitsegments、原tube restriction或同一个位置—角度—时钟law。

GR1.9的cone/equiintegrability另要求closed convex cone避开wave cone及其反向；PSD cone含全部rank1矩阵，不能直接塞入该假设。本文不靠新增ellipticity cone把原问题改成已成功情形。

## 3. 原wholeclock应力与真正可付的算子资格

以bounded chart内真实单位段a_i+[0,1]v_i、|v_i|=1、w_i≥0、W=Σw_i=1定义正PSD应力

\[
S=\sum_iw_i\int_0^1v_i v_i^T\,\delta_{a_i+tv_i}\,dt,
\quad M_\delta=S*\rho_\delta,
\quad f_\delta=\operatorname{tr}M_\delta.
\tag{1}
\]

ρ为固定非负smooth概率核，support在B₃且在B₂有正lower；这些固定半径只改维数常数，并在第7节真正支付原roundcaps。trace S总质量1，PSD给1/√n≤|S|(Rⁿ)≤1；卷积后同样有∫fδ=1和1/√n≤∫|Mδ|≤1。row-Div端点为Σw_i v_i(δ_(a_i)−δ_(a_i+v_i))，TV≤2，不能错误添一个额外方向因子或默认齐次A-free。

在Sym_n上符号为M↦Mξ。对unit ξ和任意b，矩阵b⊗ξ+ξ⊗b−(b·ξ)ξ⊗ξ送ξ到b，故constant rank为n。wave cone是singular symmetric matrices；n≥2时rank1 vvᵀ都在其中，且张成Sym_n。因此GR1.7的两项算子条件在此确可付，不需将Sym_n偷换成全matrix或给PSD另造线性值空间。

若whole-tube union Eδ的Lebesgue量趋零，则Mδ由固定倍tube union承载并趋零于measure；有限Nδ时，smooth端点RHS由2Nδ个Cδ球承载，其volume≤C Nδ δⁿ。working另给Nδδⁿ→0才付其趋零于measure。除以cδ=∫|Mδ|的Frobenius归一化只付√n；选大cube使全部轴和核在内部，极限无边界质量。没有遗漏normalization／边界或将原trace law误当Frobenius law。

## 4. 固定null原K入口可付，但其polar law属于旧闭包

对真正包含整段的Leb-null原K或R91同维Borel hull，原S和端点均由该零集承载。固定S mollify时，Lebesgue微分给Mδ及DivMδ趋零a.e.，后者L¹≤2；无需要求null集的δ-neighborhood也小，非闭的dense null hull尤其不能用该错误支持论证。选bounded whole-label chart及内部cube后，GR资格成立；若作方向restriction，须保其真实质量，不能仍声global I/n不变。

固定measure的正核mollification严格收敛TV；配合标准Reshetnyak连续性，其值分布极限就是S的polar按|S|推前、再归一化。旧DPR对finite Div的singular S已给该polar在wave cone中，故这个特定law已有supportΛ。它的Choquet存在性并不额外给原clock信息。

可直接校准每个Dirac component的生成：给|A|=1且Ae=0，转到e=e_n的cube，用正smooth周期spikes h_j(x_n)，每period平均1、占比趋零、period趋零。u_j=A h_j满足Div u_j=0、L¹=1、趋零于measure且弱极限A dx，无边界质量；其值分布恒为δ_A。故“各δ_A自身属于浓集类”在此也是可直接付的旧结构应用，不意味着这些新spikes就是原线段子族。

## 5. 真正varying序列的PSD后果及不该扩大之处

设已付第3节资格且某subsequence的归一化值law为Θ。其support在PSD单位球。GR给Θ=∫ν dπ，ν的barycenter奇异。因Θ对PSD补集质量零，π-a.e. component仍由PSD承载。取其singular barycenter B的unit kernel vector e，则

\[
0=e^TBe=\int e^T A e\,d\nu(A).
\]

每项非负，故Ae=0对ν-a.e. A成立。这里e可随component变化，不必预先选一个全局e。因此Θ由singular PSD承载；这确是一条整序列值law后果，不局限弱limit measure的奇异部分。

不能反推所有原tube方向落同一个固定4plane、总barycenter奇异、存在一个保subpower原质量的whole-clock component，或得到随δ的固定幂收敛率。Θ是单位matrix值分布，不是原ν(x,v,t)。同点的应力值是多个角的二阶和，极限／Choquet先后均不能免费恢复这些角如何沿原T续接。

## 6. 既有weighted endpoint直接给更强有限估计

无需GR或Div，旧CV Theorem1已能控制(1)的broad部分。记k_i(x)=∫₀¹ρδ(x−a_i−tv_i)dt，则0≤k_i≤C_n δ^(1−n)1_(T_i^+)；T_i^+是轴线的固定倍δ无限管，roundcaps及unitclock均被包含，不删端帽或假shading占满。由Cauchy–Binet，

\[
\det M_\delta(x)=\frac1{n!}
\sum_{i_1,\ldots,i_n}\prod_{j=1}^n(w_{i_j}k_{i_j}(x))
|\det(v_{i_1},\ldots,v_{i_n})|^2.
\tag{2}
\]

unit方向使det²≤|det|。CV的n个family全取同一原族，重复label允许且其det为零；其原statement已容许非负weights和任意方向wedge。δ重缩后，外部δ^(−n)和endpoint积分δⁿ恰抵消，得到

\[
\int_{\mathbb R^n}(\det M_\delta)^{1/(n-1)}
\le C_n W^{n/(n-1)}.
\tag{3}
\]

未用原方向分离、AD、CW或新的uniform transversality。若改走finite transverse cones，elliptic covariance可greedy选择n个固定小cap、各local mass为c_ε fδ，再对有限tuple求和；(2)–(3)则直接省去该选择的常数账。CV高级endpoint proof仍具名，本文只独推其原weighted应用。

## 7. 原broad质量、任意shadings和旧覆盖结论

0<ε≤1/n，定义Bε={λmin(Mδ)≥ε fδ}。在此detMδ≥εⁿ fδⁿ，由(3)，p=n/(n−1)，

\[
\|1_{B_\epsilon}f_\delta\|_{L^p}
\le C_n\epsilon^{-1}W,
\qquad
\int_{E\cap B_\epsilon}f_\delta
\le C_n\epsilon^{-1}W|E|^{1/n}
\tag{4}
\]

对任意Lebesgue可测footprint E成立。原clock mask 0≤m_i(t)≤1的occupation density gδ=Σw_i∫m_i(t)ρδ有gδ≤fδ，故(4)可测试其落在wholefield broad区的部分。但marked matrix自身broad不必whole Mδ broad，不能声两broad区包含。

原任意Lebesgue marks还可更强直接处理。令Y_i⊂原roundδtube T_i、E=∪Y_i，定义非transport的pointwise矩阵

\[
M_\delta^Y(x)=\sum_iw_i1_{Y_i}(x)k_i(x)v_iv_i^T,
\qquad 0\le M_\delta^Y\le M_\delta.
\tag{4a}
\]

它不需Div或BV。PSD Loewner序给det Mδ^Y≤det Mδ，故(3)及(4)对Mδ^Y自己的ε-broad区同样成立。若x∈T_i，距单位axis segment≤δ；取nearest t₀，并在[0,1]内取长度≥cδ的单侧或双侧clock interval，其中距离≤2δ。因此所选核给k_i(x)≥cδ^(1−n)，含两端roundcaps，不删帽或损λ。于是

\[
\int\operatorname{tr}M_\delta^Y
\asymp\delta^{1-n}\sum_iw_i|Y_i|
\asymp\lambda W,
\quad
\int_{E\cap B_\epsilon(M_\delta^Y)}\operatorname{tr}M_\delta^Y
\le C_n\epsilon^{-1}W|E|^{1/n}.
\tag{4b}
\]

λ按真实管体积的加权平均定义；逐管版本自然含于平均，不需heavy化。该证明保pointwise原marks和全部weights，却没有声MY的总mass有固定比例在其broad区。narrow／conditional-plane出口仍未付。

当wholefield集中在小Eδ、或趋零于measure且总质量受控时，先选承载几乎全部mass的小level-set，(4)使每个固定ε的broadmass趋零。正是本轮GR-PSD singular-value结论所需的finite信息，而且给显式|E|^(1/n)预算。(4b)还直接适用于任意原shading而没有RHS边界要求。一般GR涵盖更多算子／值分布，未被CV取代；但本锁定straight wholeline PSD桥已有更强旧有限输入覆盖，不能登记新的ordinary gain。

## 8. 满角law可精确混成proper-plane角laws

取n≥3球面概率σ，先均匀选e∈S^(n−1)，再在e⊥∩S^(n−1)均匀选v。其v边际具有O(n)不变性且总质量1，故正是σ。令Θ_e=(v↦vvᵀ)#σ_(e⊥)，则

\[
\Theta=\int\Theta_e\,d\sigma(e),\qquad
[\Theta_e]=(I-ee^T)/(n-1),\qquad
[\Theta]=I/n.
\tag{5}
\]

每component barycenter singular，而总矩full rank；这与新分解完全相容。该精确概率校准不声所有Choquet分解必为此形式，也不是完整Kakeya反例。各equator在原σ中为零measure；不能将component当一个保固定原方向质量的restriction。即使原K全方向都有段、可以额外条件化方向，anchor的normal坐标仍随v变化，角度位于e⊥不等于所有原线位于同一affine e⊥-plane。原位置、offset和全clock的共同耦合仍须另证。

因此仅在value sphere生成任意同PDE spikes，或把全角边际拆成proper-plane laws，都没有自动得到实际R4方向全满、同一个平面carrier及保原mass的模型。不能将(5)的简单分解夸成所有浓集策略失败；这里只反所列免费恢复。

## 9. FT确有一般measure出口，不按rectifiable标题粗拒

[FT v2](https://arxiv.org/html/2608.31164v2) Th1.1适用于任意2≤m<N的rectifiable m-varifold，输入包括finite mass／anisotropic first variation、stress近plane；正density版另有θ0，不能赠给原occupation。Th4.1给更广的平均concave-barrier positivity条件。原rank4 PSD极性本身不等于rectifiable4-varifold或其first variation。

更重要的是，其Prop3.4／Cor3.5在进入varifold前已处理一般matrix measures，故缺rectifiability不是整paper的统一拒绝理由。对给定barrier φ，有限mass与Φ(A)≥η>0给carrier面积与Div的定量下界；source随后用rectifiable projected stress付该positive Φ与投影carrier。

但其barrier在singular matrices上≤0。m≥2时每个rank1 projected directional stress仍singular，故原方向数／总矩正定不授积分Φ>0。凹性只给Φ(平均)≥平均Φ，不能将global正矩的barrier值当local积分lower。多个角实际同点相加可能产生positive barrier，这正需原质量；对straightline wholefield的该broad责任已有(3)–(4)。未否FT一般工具或真实MS新定理。

## 10. m维ribbon的firstvariation不能从两个端点免费取得

即便尝试把一条真实unitline加宽为rectifiable m-sheet，也要付long sides。取正交v,e₁,…,e_(m−1)，Rδ={a+tv+Σs_j e_j:0≤t≤1, |s_j|≤δ}，采用isotropic area varifold。其

\[
\mathcal H^m(R_\delta)=(2\delta)^{m-1},\qquad
|\delta V|=2(2\delta)^{m-1}+2(m-1)(2\delta)^{m-2}.
\tag{6}
\]

各face conormal在face内部给boundary，edges低维不加额外mass，因此TV／sheet mass=2+(m−1)/δ。用constant multiplicity归一mass后ratio不变。FT的first variation不是原rank1 current仅两个clock端点；m≥2有真实δ^−1费用，carrier Hm也不是原n维small footprint volume。单ribbon校准只否该免费构造，不声所有多sheet边界抵消或更精确varifold方法不可能。

## 11. Wholeclock、small marked footprint和Hausdorff出口分开

固定null K确含整unitsegments时，第4节可合法进入GR；有限ordinary/FSD只给每管或平均λ≥δ^η的marks时，small marked E不控制wholeaxis field的carrier，δ^η并非1−o(1)。mask field的新增内部端点仍是R98的真实2m费用。subpower归一因子也不等于GR要求的序列uniform L¹ bound；不能将两种入口混写。

(4)直接测marked E而保wholefield，绕开上述BV障碍，但没有从source赠broadmass lower，所以仍不解决original narrow／conditional-plane分支。Choquet给的是qualitative subsequence structure，不自带原angularδ与mollifyδ的同尺度关系、δ^ε量、真实unitaxis标签返回或一般Hausdorff cover提取。固定null资格若只回旧polar约束，不可称新的Hausdorff增维。

restriction减非负原weights保(3)–(4)，homogeneity保W；归一后的常数／directionlaw要按剩余mass收费。平均及逐管marked lower均不能独立保原point条件方向分布。旧全称gain对全部合法选择重调用即可推出的改名门仍先排等价；本轮不续R91 normal3／C¹、R98cone／endpoint，或以新Youngmeasure名称恢复旧欲证混合。

## 12. 当前通过范围、待互审与停止线

已独立支付：Sym_n rowDiv的constant-rank／spanning、原wholeclock及端点归一、PSD Choquet共同kernel的值law后果、固定null strictmollify旧化、旧CV weighted finite determinant／broad质量估计、(5)的full-angular概率校准及ribbon费用。本人推导不算独立审查，root／A须实际全文逐式互读后再定reviewed。

现已实际全文独读A12：§8–10以经典compact null满维K0=P×cube的真wholeclock stress S0，对finite translation grids作Sj=S0*ηj。相同copy×direction×clock权保trace1、全σ角边际与Div≤2；ηj趋均匀cube law，common core上弱limit F=I/(nV)。各finite-nullKj独选εj使mollified场和端点RHS均趋零于measure；Frobenius cj∈[1/√n,1]、共同cube boundaryzero和Θ barycenter I/(nc)全部核过，当前未见A强制修改项。该例是真weighted-copy/fullangular序列而非unweighted δ-direction-separated同尺度小shadow模型；每Kj本来Hausdorff满n，不是低维反例。

另已fresh实际全文独读终root12、两spec5与macro／next／source／round各6；root§9按意见补BV一侧trace／内部D_t及任意可测mask的零延拓分布区分，已读回。root§11和A§11的同ambientPSD barrier加强另独算：finite concave正1齐次给superadditive及global Lipschitz；以M−λmin(M)I奇异，得φ₊(M)≤L√n λmin(M)≤L√n det(M)^(1/n)，故本稿(3)直接给其Lp和E上|E|^(1/n)输出，MY亦同。只覆盖该原PSD实例，不扩大为FT一般signed matrix或未付projection carrier no-go。当前无遗留mandatory，正式有限结论见已授权六节review；自己的推导仍不充自身独立审查。

真实新source范围超R91单measure，但当前straight wholeline PSD用途已被既有endpoint有限输入更强覆盖；未得到ordinary新界、完整rough分支saving、strict低维反例或新ID／major。若无保原line／point／clock耦合的新输出，就按working停止此PSD／moment／barrier直接桥，不续operator阶数、cone、thickness或抽象分解参数。完整Goal保持active，formal与元数据／Git不由本稿预认证。
