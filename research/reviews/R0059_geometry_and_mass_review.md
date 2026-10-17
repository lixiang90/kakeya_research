# R0059：联合PW图形转移的原质量与范围独审

2026-10-17，B。实际全文读root主稿12节、A主稿10节、B主稿10节、macro6节、next6节及working_spec7节；实际读Choudhuri原§4、Pawłucki primary开篇／Prop1／Th3_n、GWZ Th1.1和Lemma3.7相应原文。以下为对root／A的独立逐步审查，B自稿不替代其他代理独审。具名高级wholeproof仍为依赖，未经外部同行评审，不预认证本轮metadata／Git／远端状态。

## 1. phase I原提取门槛及正式转题

通过phase I的范围判断。原whole-CW凸棱柱已给商joint3-Frostman upper及invisible fibre最多K^C/r；缺的是相反的典型fiber lower／商support upper。不能把上界重复证明冒新提取。κ=γ=0模型、conditional unused-label并入均未反正κ全源的保质量提取；common-kernel仍未解决。

spec§7先锁定PW–graph–GWZ新接口再施工。Choudhuri原件已于R33入库，本轮不是新paper发现；只首次展开其§4机制，并补general n、可测平均marks和原joint计数。这不是续R58 standalone D或索取R55已否的projected angular cap。

## 2. 全局图形、δ系数与下维层完整覆盖

通过root§§3–5和A§§3–6。单由连通域上的bounded derivative不能推global Lip；补regular-cell是必要的。Pawłucki原文明确适用于任意real-closed field上的o-minimal结构，Th3_m分open域、Prop1给regular-cell上的全局Lip。切空间Cauchy–Binet选coordinate minor、有限-to-one图关系、open域正则化及lower-dimensional递归，能够覆盖全部层及boundary；m=0另处理，没有按ambient零测删除可能承载全部marks的层。

固定格式的一致性通过所写RCF compactness论证合法：ultraproduct里的有限分解使用标准有限公式；regular-cell、C¹／导数／Lip、覆盖及lower-dimensional residual均有一阶表达，Łos和QE回传同一有限格式上界。Paw的常数只依维数，不暗含δ-dependent height。补m个坐标至3个仍保projection injectivity及全局Lip；closure只连续延伸已全局Lip的graph。由此正常fiber体积≤Cδ^(n−3)对低维domain也成立，但它仅为upper。

## 3. 原平均质量、未clamp端帽与四线参数包络

通过root§§6–7。原平均δ^η密度先保至少cδ^ηN个heavy labels，再逐管选chart、固定同chart；每个剩余原Yi^j保cδ^ηδ^(n−1)体积。这里只保所选逐管密度，没有给后继任意删选免费闭包。

非短投影确由两个实际shaded points支付：未clamp正交坐标s=v·(q−a)的截面积≤Cδ^(n−1)，故s-span≥cδ^η。支持直线点允许越原unit端点Oδ，距graph仍Oδ；global Lip及δ/δ^η→0迫|πv|≥c。没有假shading含interval、也没有把非线性坐标变换后的曲线当原轴。

root把支持线center固定在主坐标横截面x_k=0，两个intercepts加两个direction参数作四维δ网，固定长L0包络覆盖原投影。未增纵向center网，故缩放／同center延长后没有exact参数碰撞。调用GWZ才共同缩入B1／延为unit轴；原R^n管、原marks与PW对象均未延长，正交fiber积分在此前的未缩放frame进行，长度规范无偷换。

## 4. 联合PW测试、原重复及绝对浓集

通过root§§5、8及A§8。对任意凸U取John外接矩形Q_U，使|Q_U|≤C|U|；H_j∩π⁻¹Q_U是统一格式半代数test，体积≤Cδ^(n−3)|U|。P_i⊂U使实际Yi^j落该test，原direction-separated Ti有至少cδ^η的实体体积比例。PW在原R^n中的计数因此为

    #{原assigned i:P_i⊂U}≤Cδ^(−2−σ−nη)|U|。

没有从projected方向cap调用PW，也没有用global |NδS|替换joint test。原λ=cδ^η≥δ的合法范围已付。以U=P查询得duplicate upper Cδ^(−σ−nη)；每bin任取一个原heavy代表仍保真实marks。去重后数≥cδ^(σ+(n+1)η)N，且Δ_max≤Cδ^(−σ−nη)是**绝对**Σ|P|/|U|，不是normalized probability cap，不需要#P≈δ⁻²。固定邻格着色仅常数loss。

## 5. 任意可测shading的fiber回传与完整指数

通过root§§9–10。f(z)=δ^(−(n−3))正常∫1_(E∩H_j)可取a.e.可测代表，0≤f≤C；原Yi^j先给每个包络∫P_i f≥cδ^ηδ²。统一level F={f≥c0δ^η}于是构成每个包络上的真实δ^η-dense shading。它可以接收其他原Yi贡献，仍是同一原E的level set，不声每条三维shading都是该原Yi的literal投影。

物理下界由|E|≥δ^(n−3)∫f≥cδ^(n−3+η)|F|支付，绝未由fiber upper伪造fiber lower。GWZ允许可测shading；绝对Δ_max及density满足其阈值后，合计为δ^(n−1+β+σ+(n+2)η)N。先β，再σ及其GWZ余量，最后η、δ，参数不循环。固定homothety后的unit延长保持“新包络⊂U⇒旧包络⊂h⁻¹U”，所以原计数、原shading和frame费用都保留。

root实际加强到仅Yi近S而不用wholeaxis近S也成立，因为所有选择／PW查询／积分只使用Yi。原输入若另已给小常数absolute PW计数，同证明σ换ηPW及明确阈值即可；这不是免费给任意管族或HRZ叶该输入。

## 6. 结论、旧反攻与下一轮边界

本轮全类near-full局部结论在具名PW／GWZ／Paw输入下通过独立审查。它处理fixed-format realdim≤3的δ-dependent、singular载体与任意可测平均marks。R55的projected angular重数反攻仍正确：同方向不同截距不等于落在同一个joint凸管内，未与本轮新计数冲突。n≥4同一证明合法，特别覆盖所选n≥5。

macro与next准确保留ordinary H5／general-to-sticky／common-kernel未解；全λ³、任意原weights／α及真实HRZ叶的尺度／PW／marks没有自动支付。下一只能先周期macro及真实递归价值核验；若旧narrow或m4门槛已封住收益，应当轮改选实际数学，不续常数。next§2已补“原物理δ方向分离的unitδ管”并fresh全文读回通过；替代输入须明确独立给absolute PW小常数，不能读成无假设管族。无新ordinary维数界／重大／新颖认证，Goal active；本轮审查结束后停止编辑，由root统一归档同步。
