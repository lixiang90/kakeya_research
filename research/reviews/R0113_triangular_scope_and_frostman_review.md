# R0113：三角Borel原shading、Frostman与范围的独立审查

2026-10-26（Asia/Shanghai）。reviewer：new_projection_gate，独立于root主稿作者。只新增本文件，不改主证明／元数据／Git。本次实际读到的当前working及主稿九节，在下述范围内**通过，无未解决必须修正项**。这是内部逐步审查，不是外部同行评审、优先权或重大性认证。

## 1. 实际对象、读域和精确声明

实际全文读research/rounds/R0113_working_spec.md及notes/50_counterexamples/R0113_triangular_Borel_original_shading_proof.md当前九节，包括root后来写入的bush取t∈[r/2,r]和固定real similarity提取反攻。为排重，实读R41 source_construction_and_parameter_budget §6的Cartesian实际论证、R93 digit_product_unit_segment_countergate与robust_projection_source_and_closure_gate的相关完整结论、R1 projection_slicing的LIFT003／004及LIFT-NEXT全文。Fu–Gan库内原文的Lipschitz area-formula段已在本轮同会话实读，不再次下载或认证其wholeproof。

有限命题的输入确为满产品方向grid k∈{0,…,L−1}^m、Lδ在固定正上下界内，a_i只依k_1,…,k_i，原Y_k是各自cylinder内任意Lebesgue可测集合。时间J固定有界，λ=Σ|Y_k|/[L^m(2Rδ)^m]是平均marked**时间量**，0<λ≤|J|；没有把它误写为全先验概率或逐管下界。

连续命题的f_i只需Borel、可无界；Z⊂[0,1]^m×J任意Borel且参数Lebesgue质量λ>0。结论是X(Z)满Hausdorff维数m+1，不是其closure满维，不是正Lebesgue体积，也不覆盖非三角截距。

## 2. 共同时间标量能量：对角和非对角均通过

固定0<s<1。对A∈R、B≠0，变量u=A+tB给

\[
\int_J|A+tB|^{-s}\,dt\le
\frac{2^s|J|^{1-s}}{1-s}|B|^{-s}.
\]

常数与A及J的位置无关：固定长度区间的|u|^{-s}积分在以0为中点时最大。这容许表值任意振荡／任意幅度。

有限μ_{p,t}是L个实际宽2Rδ区间概率的均匀混合。每个自项的精确能量为2(2Rδ)^{-s}/[(1−s)(2−s)]；L个自项乘L^{-2}|J|，总O(L^{-1}δ^{-s})≤Cδ^{1−s}，由Lδ≥c0统一有界。没有省略atomic diagonal：噪声区间正是处理它的真实横截来源。

非对角在噪声固定后用上式，B=(k−l)/L，故总和≤C L^{s−2}Σ_{d=1}^{L−1}2(L−d)d^{-s}≤C_s。噪声再平均不增加该界。L=1时由δ≥c0直接付自项。Tonelli先用于非负extended kernel，不循环假定能量有限。

连续版把方向当前坐标换成Leb[0,1]，w=w'的对角是二维Lebesgue零集，余下只需∫∫|w−w'|^{-s}dw dw'=2/[(1−s)(2−s)]。对每prefix同样有共同J的积分界，继而对prefix平均也统一。这与“每prefix挑各自好t”不同，后者不能替本证明。

## 3. 一次潜势筛选确保原marks质量

有限源测度是uniform全部L^m labels、m个真实横向区间噪声和dt。对固定label的(z,t)→(x,t)是Jacobian1的affine shear，源中marks质量精确为λ。Lebesgue Y_k可换Borel代表，只改变有限个零测集，I和|E|均不变。

坐标i的坏事件为U_s μ_{k_<i,t}(x_i)>T。先固定prefix，当前k_i,z_i的分布就是μ_{p,t}；其余标签／噪声积分为1。因此坏源质量≤T^{-1}∫_J I_s(μ_{p,t})dt≤C_s/T，随后prefix平均不改常数。

取T=2mC_s/λ，并集上界只丢≤λ/2**总源质量**，所以任意相关marks仍保≥λ/2。marks可以集中在坏处，此估计仍有效。没有先删掉管再沿用原λ，也没有断言每根原管的good比例固定。连续版对Z同样成立，good∩Z为Borel且正参数质量。

## 4. 有限逆序求和确给原实体|E|

若某混合区间包含x，则该整区间距x≤2Rδ；每个active interval给U_s至少(2Rδ)^{-s}/L。相加得到

\[
U_s\mu_{p,t}(x)\ge(2R\delta)^{1-s}\rho_{p,t}(x),
\quad
\rho_{p,t}(x)1_{\rm good}\le T(2R\delta)^{s-1}.
\]

真实marked-good推送有主稿给出的显式密度q。先把1_{Y_k}上界为对应全部cylinder interval的乘积；这一步只用于**密度upper**，没有把包络填进E。剩余第m个good条件只依k_<m,t,x_m，不依k_m，且所有i<m因子均不含k_m，因此最后一层和恰是good×ρ_{prefix,t}(x_m)。其余坐标同理逆序，得到q≤[T(2Rδ)^{s−1}]^m。

原marks本身完全不需要factorize，能依全部x、t和labels；三角性只用于丢marks后的包络和good条件。此处没有隐藏的marginal独立性。

q确由原E携带，故λ/2≤∫_E q≤|E|T^m(2Rδ)^{-m(1−s)}，代入T给

\[
|E|\ge c\lambda^{m+1}\delta^{m(1-s)}.
\]

这直接证明实际Lebesgue并集体积，不是δ-neighborhood或occupied-cells代理。对每目标ε先选s使m(1−s)≤ε，δ≤1时方向正确。有限C_s随s趋1可发散，不影响该量词。

## 5. 连续Borel／analytic像／全r Frostman逐步通过

对于Borel f_i，(prefix,t,z,w)↦|z−f_i(prefix,w)−tw|^{-s}是extended Borel非负函数；对固定Lebesgue变量积分仍Borel。条件概率kernel和good集合均合法。推送ν_s是有限Borel测度，质量≥λ/2；不假它有Lebesgue密度。

固定prefix,t及任意长度r>0的interval Q。若good输出在Q内有正质量，则存在某个good z0∈Q；对所有w∈Q有|z0−w|≤r，于是

\[
\mu_{p,t}(Q)\le r^s U_s\mu_{p,t}(z_0)\le Tr^s.
\]

若无good输出则good限制质量为0。这是逐实例数值upper，不需全局可测选择z0。特别适用于μ存在原子或对某些t有无限能量的情形：这些点仅可能不good，正质量已经由平均筛选保证。

对任意边长≤r的物理盒，先丢Z后按v_m,…,v_1逆序积分，每层至多Tr^s；最后真实时间Q_t∩J长度≤r。因此ν_s(box)≤T^m r^{ms+1}。球放入边长2r的盒，给ν_s(B)≤C_mT^m r^{ms+1}，**所有r>0**均成立。这里没有只证离散r或某一个尺度，也未用finite(F)推Hausdorff。

X为Borel map，Borel Z的像X(Z)为analytic，故对ν_s的completion可测；ν_s被其携带。更直接的覆盖核验是：X(Z)的任意可数球覆盖拉回覆盖Z∩good，故λ/2≤Σν_s(B_j)≤C_mT^mΣr_j^{ms+1}。这不依赖image是否closed，更不以其closure代原像。

故原X(Z)的(ms+1)-Hausdorff content有正lower，dim_H X(Z)≥ms+1。沿任意s↑1序列取上确界得m+1。每个s可有不同good集和ν_s，这完全足够，不给端点s=1的统一Frostman常数或正体积结论。f_i无界只使像可能无界，不影响有限源测度和上述任意球cover论证。

## 6. 原N、平均与逐管restriction没有被偷换

主稿始终保N=L^m。删管／删marks后以旧N计的新质量为pλ；若只对剩N'=qN算平均，才有λ'=(p/q)λ。对不成产品的label子族，不能直接声它是更小完整grid；将未保留labels置零shading，则(F)确给c(pλ)^{m+1}δ^{m(1−s)}。absolute direction cap继承，概率归一须另付1/q。

一次good筛选仅保总I/2，不给每管lower。若另一个下游工具要求逐管，举例可在筛后取每管good体积≥I_good/(2N)的labels：保≥I_good/2原质量，条数至少I_good/[2(2Rδ)^m|J|]≥c_JλN；每根余管有原cross-section单位下的cλ时长。这个额外label损失及概率cap费用必须记录；本证明本身无需此步骤。

fractional marks扩展在0≤w_k≤1且各自支于C_k的范围内成立；无界weights和任意非uniform方向law没有被现有proof自动覆盖。真正round δ管只需固定矩形／clock envelope，原marks原样保留，λ按新envelope交叉体积仅变固定倍；不添加单位段之外的marks。

## 7. 实际bush校准与固定linear三角化反攻

当前主稿已把bush的lower区间明确写为[r/2,r]，并取r0≤min(1/4,Rc0)。对a_i=0、marks为C_k∩{0≤t≤r}，λ=r。横向格间距t/L≤r0δ/c0≤Rδ，使每coordinate intervals相接；横截覆盖边长ct的box，体积≈t^m。与上界(t+δ)^m积分合并，δ≪r时|E|≈r^{m+1}。选择固定小R及r0可使这些marks直接落入真实round单位管内。该例支持λ^{m+1}的自然费用，主稿没有越界声所有δ/λ混合指数的最优性。

新增反攻A=diag(J0,J0)、J0=[[0,−1],[1,0]]通过。任意固定实可逆S，B=SAS^{-1}无实特征值。若第一行未来coeff全0，则e1^TB=B11e1^T给实左特征值，矛盾；故某B1j≠0、j≥2。对任意Borel g，关系(Bv')_1=g(v'_1)在固定v'_1 fibre上约束一个非零linear functional的level，在R³中Lebesgue零。正Lebesgue D不可能全满足它，Fubini无需D本身为产品。固定S的direction-chart变换保持正angular质量，因此不能靠固定共同real S和正角度mass restriction免费取scalar三角性；坐标permutation已含于S。

该反攻的量词很窄而准确：是精确三角化、共同空间linear change、固定S、正测度restriction。未覆盖δ近似三角化、非线性／projective变换、改变clock类型或改变原family。并且det(A+tI)=(1+t²)²>0，原smooth方向patch的union有5D内部；它不是Kakeya反例，也不从“非三角”推出任何低维结论。

## 8. R41／R93闭包、新工具范围和ordinary隔离

R41 §6原statement要求每坐标截距只依自己的方向index，实际同clock footprint是Cartesian product；R93的数字模型也以各coordinate共同能量、乘积和slicing处理完整clock。它们记录的结论没有任意prefix依赖及任意原平均shading的统一量词。固定一个prefix逐次调用标量energy是合法旧工具，但将每prefix自己的好t直接相乘并不合法；主稿用共同原先验的总坏质量筛选和逆序积分，实际完成了这个不同的组装步骤。

因此不能把当前(F)/(H)说成R41完整Cartesian statement对某个免费合法删选的一次重调用，尤其冻结prefix通常损固定方向幂／连续正参数质量。也不能声它与旧结果正幂双向等价：主稿允许更多Borel前缀耦合，反向Cartesian当然是特例，但旧稿并未记录前向推广所需的筛选证明。

同时，这个推导只消费经典标量投影energy和三角条件；它可能是已有理论的初等后果，未有一手优先权证明。四维FSD／KT的普通任意ambient调用没有免费给m+1>4时的full exponent；这并不使该proper类自动成为重大中间结果。源的三角消元或regular selection也没有证明ordinary截距表具有本物理三角结构。

LIFT-NEXT原问题是更广的四维Borel线片段扩展／好base返回。本稿从完整方向cube参数Lebesgue质量和三角性构造Frostman，不解决那个一般问题，也不把此工具当做LIFT004免费平滑化的替代归约。普通全耦合、HRZ和fullrough所缺原共同质量仍未支付。

## 9. 最终意见与不认证项

当前(F)的原实际shading volume证明、(H)对任意正参数质量Borel Z的全Hausdorff维数证明，以及A=diag(J0,J0)的精确提取反攻，均通过本次独立逐步审查。没有必须修改的逻辑、分母、可测性或尺度错误。

结论应保持为任意Borel**三角prefix**的受限工具；不是任意方向截距构造定理、ordinary新下界、完整source gain、严格低维反例或major。不得据此完成Goal或登记新的major ID。本文不预认证未来root整合、文献穷尽比较、registry、Git提交或远端同步；若后续改变三角输入、权重或image／shading量词，须重新审查相应步骤。
