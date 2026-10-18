# R0099：行列式、原shading与Michael–Simon接口独立审查

2026-10-19，B。有限应用与接口审查，未经外部同行评审。自身B稿不算自身的独立审查；本review主核root／A的原算子、质量、平移浓集和整合范围。

## 1. 实际全文对象和来源层级

已实际全文读终root `notes/40_multiscale/R0099_concentration_wholeclock_and_known_determinant_gate.md` 共12节、A `notes/00_map/R0099_concentration_primary_and_operator_gate.md` 共12节、B稿12节；reselection／working两spec各5节；终macro、next、source scope、round各6节。另fresh读回root§9的BV／trace修订、§11及macro§4的同ambient PSD barrier旧覆盖。没有以消息、摘要或自己的推导代替对方全文审查。

本人实际官方HTML核GR2608.20899v2的Def1.3／Rem1.5、Th1.6–1.10与1.12及部分组装证明接口；FT2608.31164v2的主定理、一般matrix-measure Prop3.4／Cor3.5、Th4.1及其应用证明。实际读库存CV1205.6371v1 Theorem1及其footnote的任意方向weighted endpoint原量词。热流核心、广义Youngmeasure表征、完整Choquet高级证明和CV全证明仍具名；不冒逐页视觉读新PDF、全部高级wholeproof独证或下载／SHA验证。旧R91／R94的selector、planar compact null Kakeya与product范围按已审具名输入复用。

另已实际读回终source§1／3的日期区别：GR官方v2 history／HTML及PDF侧栏为9月11日、固定原件正文首页为9月14日；FT相应为9月9日与正文9月10日。root已看原图且不改原件，本review保留该来源记录，不把两种日期伪装一致，也不冒本人独立视觉核过首页或哈希。数学输入仍按明列固定v2及实际声明，未因日期记法变化扩展wholeproof读域。

## 2. GR原输入、Sym_n算子和三种场景

GR的新内容确是浓集序列值分布，而非只重述DPR单measure奇异polar。Def1.3的L¹归一、趋零于measure、弱星极限无边界质量和Frobenius值球law均被保留；Rem1.5允许的非零RHS还须L¹一致有界且趋零于measure，不能只说finite-TV便跳过后一条件。

Sym_n上的row-Div符号Mξ满射Rⁿ：b⊗ξ+ξ⊗b−(b·ξ)ξ⊗ξ送unit ξ到b，故constant rank n；rank1 vvᵀ在wave cone且张成Sym_n，满足Th1.7另需的spanning。PSD不是线性值空间，不另改算子。原wholeclock stress端点为Σw_i v_i(δ_(a_i)−δ_(a_i+v_i))，TV≤2W；PSD给trace与Frobenius相差至多√n，归一无失控。

随δ全tube union小与Nδⁿ→0分别支付场和端点RHS的趋零于measure，共同大cube内支撑支付边界零。原direction-separated N≲δ^(1−n)足够；带K时还需Kδ→0，root已显式写出。仅原marks小不能替换whole axes小。固定null源中，singular measure卷积趋零a.e.及strict-polar连续性合法，实际law已由旧DPR支撑Λ；root的单hyperplane spike和A的细周期stripe均可生成δ_A，且无边界质量。只排重这一实际fixed-null用途，不否GR更广定理。

PSD专属Choquet后果也成立：正分解保各component support在PSD，奇异barycenter B的kernel e满足∫eᵀAe=0，故Ae=0几乎处处。这仅给每component共同kernel及值law奇异；e可随component变，无需偷偷选可测e，也不能推出总barycenter奇异或保原tube全clock的restriction。

## 3. 旧CV有限估计、marked自身broad和原密度

root／A的Cauchy–Binet式、wedge权和全部δ幂逐项通过。令k_i=∫₀¹ρδ(x−a_i−tv_i)dt，则k_i≤Cδ^(1−n)1_(Cδ无限管)，包含unitclock端帽。精确ordered-tuple公式为

\[
\det M_\delta=\frac1{n!}\sum_{i_1,\dots,i_n}
\prod_j(w_{i_j}k_{i_j})\,|\det(v_{i_1},\dots,v_{i_n})|^2.
\]

unit方向的det²≤|det|；CV的n个family全用同一原族合法，重复label项为零。取1/(n−1)后系数δ^(−n)恰抵消endpoint右侧δⁿ，得到

\[
\int(\det M_\delta)^{1/(n-1)}\le C_nW^{n/(n-1)}.
\]

不需要方向分离、CW、AD、Div或浓集。对任意物理可测h_i∈[0,1]，Mδ^h≤Mδ为PSD，det单调；故其**自身**ε-broad trace的L^(n/(n−1))范数≤C_n ε^(−1)W，E上mass≤C_n ε^(−1)W|E|^(1/n)。marked-broad不必包含于whole-broad，终稿没有使用这个假包含。若需连续angle law，可在有界(a,v)参数空间作finite atomic逼近；固定δ下卷积核连续、共同紧支撑，Fatou返回相同upper，不要求selector连续。

kernel支撑B₃、在B₂有正lower时，原roundδtube上nearest axis clock及长度≥cδ的单侧区间给k_i≥cδ^(1−n)，包括两帽，不以删帽损失小λ。于是Σw_i|Y_i|的真实加权平均直接给∫trMδ^Y≥cλW；逐管lower逐项也给同式。无heavy化费用被隐藏。删管／marks保absolute upper但未必保原λ，重归一按所留W收费。该估计只把small footprint的大部分原质量送向局部narrow，不送到一个共同平面或完整原clock分组。

## 4. 真full-direction平移序列与值law／空间极限区别

A§8–10和root§10的校准逐式核过。经典compact planar null P乘(n−2)-cube仍包含每个原单位方向的整unitsegment：平面速度长度≤1，额外坐标按速度符号选起点，不单独改变clock。Fubini给null；P上的s-Frostman law乘cube再令s↑2给Hausdorff满n，故不是strict低维反例。

S0的trace mass1、总矩I/n、端点TV≤2。固定大cube上的finite uniform translation grids保真实copy×方向×clock law、每个方向总权重和全部unitaxes；Sj仍载finite compact null translates，并不因此成为one-per-direction无权δ-separated族。ηj弱趋均匀cube时，Sj弱趋S0*η=F dx；common core内所有y∈K0都有x−y∈cube，故F=I/(nV)，是真位置处full-rank ac密度，不仅global矩。

逐j用compact-null载体选足小εj，使其3εj邻域volume→0；mollified场和端点RHS均由该邻域承载，因此两者趋零于measure。cj∈[1/√n,1]、RHS L¹≤2√n、共同支撑与boundary零全部成立；M_j−S_j弱趋零由测试函数的一致连续性付齐。子列cj→c后，Θ的总barycenter I/(nc)满秩，空间弱limit在core为I/(ncV)，同时各Choquet component barycenter可奇异，二者无矛盾。

此例保wholeclock／完整角law而无原δ-power footprint控制，每个载体本来满Hausdorff维数；不反Kakeya。B的equator角law混合亦只是概率校准，不能当正原方向质量的tube restriction或共同affine carrier。生成任意A-free浓集场不附带原(a,v,t)耦合，这是本轮真实剩余责任。

## 5. FT一般barrier、ribbon费用和shading修复

FT不只是一条rectifiable-varifold定理：Prop3.4／Cor3.5先对一般matrix measures给nonconcentration及carrier体积×Div下界。不能因为原Div仅有界不趋零就拒Cor3.5，其缩放已处理这一点。Th1.1／4.1再付rectifiable m-sheet、finite anisotropic variation和平均positive barrier，2≤m<N；没有从原line occupation免费取得这些hypotheses。

终root§11的更强旧覆盖正确。有限concave正1齐次φ由superadditivity及|φ(Z)|≤L|Z|得global Lipschitz。PSD M的B=M−λmin(M)I奇异，故

\[
\phi_+(M)\le L\sqrt n\lambda_{\min}(M)
\le L\sqrt n(\det M)^{1/n}.
\]

因此同ambient PSD wholefield和marked field的此类barrier正部已有CV给的uniform L^(n/(n−1))及E上|E|^(1/n)控制，不需Div。只覆盖该straightline PSD实例；不否FT一般signed matrix、真实anisotropic varifold或另需支付的projected carrier方法。global正矩经凹性也不能反向赠local Φ lower。

单m-ribbon [0,1]×[−δ,δ]^(m−1)的质量(2δ)^(m−1)、boundary TV=2(2δ)^(m−1)+2(m−1)(2δ)^(m−2)，故variation／mass=2+(m−1)/δ。constant multiplicity归一不降该费用，MS右侧相对归一mass为δ^(−1/m)，不是新增益。只反免费line→sheet转换，不反所有varifold路线。

唯一报告的字面必修已修：root§9 endpoint+Dt h公式现限BV(0,1)，端点取一侧trace、Dt为内部导数；一般仅可测mask用零延拓分布导数，不假trace且不重复端点。m段TV2m、单段mass归一后2/λ均成立。原平均或逐管density不授GR的uniform RHS；CV对marks绕过BV不等于修好了PDE闭包。

## 6. 最终有限判定、四路与停止

**上述终root12／A12及两spec、macro／next／source／round的有限范围全文通过；当前无未解决mandatory。** 本review独立核对方的operator／端点／浓集规范、CV原质量、真实平移序列、FT与shading范围；自身B12的数学由root／A另行独核，不自计双审。

GR实质超旧单measure定理；但fixed-null应用由旧DPR闭包重获，原straightline PSD的finite broad及同ambient barrier输出又被更强旧CV覆盖，不能登记新主gain。相反，不能据这种包含说整个GR与CV双向等价、全FT失效或所有PDE无用。原samepoint／跨fiber／全clock联合质量和ambient／Hausdorff返回仍未付。

ordinary初始化、HRZ全费用、sticky全部rough与ordinary桥、同集full方向严格低维四路仍open。终macro／next无已付下一gain候选，停止本PSD浓集的moment／算子／端点／cone／ribbon厚度续轮，不以欲证质量改名。无新数学ID、ordinary界、完整branchsaving、major或Goal完成；时钟22与实际信息progress分开。高级wholeproof仍具名，明确**未经外部同行评审**；不预认证任何未来metadata、Git或同步。
