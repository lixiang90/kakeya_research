# R0093：互补数字参数、真实单位线段与稳健投影反攻

2026-10-18，B。恰八个编号二级节。以下反驳“联合4AD＋各球同一方向投影大，自动给PBP/BPLG”的免费接口；不反ordinary Kakeya或完整critical source。未经外部同行评审，无newID/major声明。

## 1. 实际输入、源阅读与命题边界

实际全文读R93 reselection_spec五节及STATE；前轮已读GOAL/全ROADMAP/registry78/R92 next的恢复记录不伪作新证明。固定

    A={Σ_(j≥1) a_j4^(−j): a_j∈{0,1}},
    B={Σ_(j≥1) b_j4^(−j): b_j∈{0,2}},   F=A×B。

下文F^4视为R^8中四组(x_i,y_i)，并令`L(x,y)=(a,v)=(x−y,x+y)`、`Z=L(F^4)`。完整angular首先指bounded graph chart中的四维open patch及每个参数球的原投影lower，不把它写成一个bounded slope chart字面覆盖整个S4。

实际打开作者[Urs Lang, Notes on Rectifiability](https://people.math.ethz.ch/~lang/rect_notes.pdf)，网页原件标December15,2023版、35物理页；读§10 Th10.6及其证明、Th10.8的精确BF声明和Examples10.9–10.10。Th10.8给纯H^m不可整流且有限H^m时，Haar-a.e. m-plane投影零；它作为经典具名输入。没有下载或新认证整35页、高级BF证明。Lang例10.10已说明Cantor参数造零体积Besicovitch的经典用途，不将本文应用冒新发现。维数下界另给energy/slicing证明，不采用未读的Marstrand高级证明。

## 2. 数字恒等式、联合4AD和所有球的固定大投影

每位`a_j+b_j`恰且唯一遍历0,1,2,3，没有carry。因此`A+B=[0,1]`，端点1取全3展开；A⊂[0,1/3]、B⊂[0,2/3]。给每个二字母Cantor等权Bernoulli概率。F由四个比例1/4的严格分离相似副本组成，自然μ_F为1AD：level k子块质量4^−k、直径C4^−k、彼此间隔至少c4^−k。球半径r≈4^−k交O(1)块给upper；中心所在的再细固定层子块包含于球给lower。故`μ_F(B(z,r))≈r`。

四重乘积μ=μ_F^4为4AD；同样level k有256^k个分离副本、每块质量4^−4k。特别`0<H^4(F^4)<∞`，自然μ与H^4 restricted measure可比（Frostman给lower，层cover给finite upper，再局部cover比较）。L满足`|Lz−Lz′|=√2|z−z′|`，故Z仍4AD、有限正H^4，并非只证明参数个数上界。

投影`π_v Z=[0,1]^4`，自然概率的π_v像也恰为该cube上的Lebesgue概率。更强，任意z∈Z和`0<r≤diam Z`，选一个含z的level k副本，其直径≤r且4^−k≈r。整个副本在B(z,r)内，其π_v像是边长4^−k的平移cube。因此

    L^4(π_v(Z∩B(z,r)))≥c r^4。                    (1)

这不是只在global ball有一个好投影。方向`Θ(v)=(v,1)/√(1+|v|²)`在[0,1]^4上为光滑bi-Lipschitz angular chart，其Jacobian有固定双边界，所以(1)也给同一chart的真实angular四维质量lower。

## 3. 逐步纯不可整流证明和PBP/BPLG失败

同时处理`E_d=F^d⊂R^(2d)`、d=1或4，自然测度为dAD。E_d含0及2d个坐标端点`s_j e_j`，其中s_j为1/3或2/3；这些点affinely span全部R^(2d)。存在固定c_0>0，使任意affine d-plane W至少距其中一点≥c_0：否则各坐标向量至W的方向plane的距离都很小，与正交余维d的projection矩阵Hilbert–Schmidt范数平方为d矛盾。这里允许W有任意offset，不只是过原点plane。

每个level k副本是平移4^−k E_d。把任意W反变换，某个相应端点距W≥c_04^−k；其半径c_04^−k/4小球内的副本质量由AD lower至少c4^−dk，且全距W≥c_04^−k/2。对任意z∈E_d，取其level k副本，包含于`B(z,C4^−k)`。故对每个过z的d-plane，沿这些半径都有固定比例r^d质量离plane至少cr，统一反approximate tangent。

纯性还需排正质量rectifiable子集，不能只说全E没有tangent。若一个countably d-rectifiable R与E_d有正H^d交，则在μ|E_d的几乎每个该交点，R有相对μ-density一；有限H^d的rectifiable交集又由标准切平面定理有approximate d-tangent。μ与H^d|E_d可比，所以R外质量为o(r^d)、R内切平面外质量也为o(r^d)，反上段统一lower。因此E_d纯d不可整流，特别F纯1、Z纯4。

经典BF现在合法应用：`H^4(π_V Z)=0`对G(8,4)中Haar-a.e. V成立。每个Grassmann open neighborhood有正Haar measure，故不可能在某个固定η-neighborhood中所有投影都有`≥ηr^4`质量；local子集投影更小。于是Z没有PBP。纯4还直接给它与任意4维Lipschitz graph的H^4交为零，所以也无BPLG，不需把单球BP误作PBP。有限δ近似若声称统一η，准确指投影的δ-thickening具有相应Leb4下界（有限点投影本身H4恒为零）；令候选中心planes取收敛子列，选附近generic零投影V，再用compact projected Z的δ-neighborhood体积趋零，也会矛盾。不能以有限样本的正投影替代连续结论。

## 4. 精确有限网格、方向分离与John证明的CW

取δ=4^−m，A_m/B_m为m位数字后接零。每位的唯一数字分解给

    A_m+B_m=δ{0,1,…,4^m−1},
    #Z_m=δ^−4，  π_v Z_m=(δ{0,…,4^m−1})^4。

联合点集在`δ≤r≤1`满足`#(Z_m∩B(z,r))≈(r/δ)^4`；可由上述分离层结构直接证明，或用截断耦合把自然μ移动Oδ并在r≥Cδ比较，余δ≤r≤Cδ由单点和packing吸收常数。r<δ不声连续AD lower。Θ的bi-Lipschitz性给cδ分离和每个δ angular cap O(1) labels；如需字面δ分离，可删去固定数末位层取4^lδ子网，规模仍≈δ^−4，所有费用固定，不赠新的参数。

令T_i为这些真实unit axes的半径δ管。它们有normalized convex-Wolff whole-containment界，不必额外假设。证明：取包含某些T_i的凸body W，John ellipsoid E中心c、半轴ℓ_1,…,ℓ_5，`E⊂W⊂c+5(E−c)`。若W含一个T_i，它含半径cδ球，故所有ℓ_j≥cδ；unit轴端点差属于W−W，给`|(Θ_i)_j|≤Cℓ_j`。

对每个方向选`|(Θ_i)_j|≥1/√5`，相应ℓ_j≥c。在这个sphere chart作δ-packing，四个其余坐标范围至多Cℓ_i，且ℓ_i≥cδ，所以该类方向数

    ≤Cδ^−4 ∏_(i≠j)ℓ_i ≤Cδ^−4 ∏_iℓ_i ≤Cδ^−4 |W|。

chart的surface Jacobian有固定界，δ-neighborhood的坐标膨胀被ℓ_i≥cδ吸收；再对j求和。因为N≈δ^−4，得到`#{i:T_i⊂W}≤C N|W|`。无管时平凡，体积无限也平凡。此为整个凸类的whole-containment CW，不是只对axis-aligned boxes；未证明partial-intersection/fullPW、critical small-footprint或原source的其它输入。

## 5. 同一compact集合内的真实单位线段

对每个(a,v)∈Z置

    ℓ_(a,v)={(a+t v,t):0≤t≤(1+|v|²)^−1/2}，
    K=∪_(a,v)∈Z ℓ_(a,v)。                          (2)

切向量为(v,1)，所以arclength严格为1，而不是把time长度1误称unit length。a、v bounded，终time连续依v，(2)是compact参数域的连续像，故K compact、可测。它供应Θ([0,1]^4)的全部方向，包含非空open angular patch。所有labels至少共同保`0≤t≤T_0=1/√5`；有限Z_m的整unit segments原样包含于K，无额外clock补全。

写a=x−y、v=x+y，则物理slice为

    a+t v=(1+t)x+(t−1)y， C_t=(1+t)A+(t−1)B。

对`0≤t≤T_0`，K_t恰为C_t^4；对所有`0≤t≤1`，K_t⊂C_t^4，t外为空。t超过T_0时不声完整product slice，因为各label终time不同。time0的C_0=A−B实际上是interval，这不阻其余a.e. slice为零长度，不能由单一clock误判整体体积。

## 6. 零Lebesgue体积而满Hausdorff五维

F纯1且有限H^1，BF给其a.e.一维orthogonal projection长度零。`(x,y)↦(1+t)x+(t−1)y`的方向随t∈[0,1]光滑变化、角导数非零，只有固定nonzero scalar系数变化。因此`L^1(C_t)=0`对a.e. t成立；compactness和Fubini给`L^5(K)=0`。

Hausdorff lower可不用Marstrand作额外输入。记μ_F为1AD概率，任意0<s<1有I_s(μ_F)<∞。对差向量z=(dx,dy)≠0，置a=dx−dy、b=dx+dy。在固定bounded time interval I上，若b相对a小则|a+tb|≳|z|；否则|b|≳_I|z|并对一元线性函数积分。因此

    ∫_I |(1+t)dx+(t−1)dy|^(−s)dt ≤ C_(s,I)|z|^(−s)。

Tonelli得对a.e. t，投影概率ν_t的I_s有限；对所有rational s<1取共同conull集合，得到`dim_H C_t=1`。又对四个差值r_i，`(Σr_i²)^(−2s)≤∏|r_i|^(−s)`，故

    I_(4s)(ν_t^4)≤I_s(ν_t)^4<∞，  dim_H(C_t^4)=4。

于是(0,T_0)中a.e. actual slice K_t维数4。若`max(1,dim_H K)<q<5`，取H^q零的细球cover；slice-cover的(q−1)费用对t积分至多`2Σr_i^q`。取费用可求和趋零的一列covers，再Tonelli，给a.e. slice `H^(q−1)(K_t)=0`，与维数4矛盾。因此`dim_H K=5`。这是完整同集/真clock结论：零体积并不等于严格低维，没有构造Kakeya维数反例。

## 7. 方向补齐、平均/逐管marks和未保条件

Θ((0,1)^4)是S4中非空open patch。用紧性选有限个physical rotations R_j使其rotated patches覆盖S4；`K_full=∪_j R_jK`仍compact、Lebesgue零、Hausdorff五维，并包含每方向真实unit segment。不是按方向另换集合或按clock拼段。该步骤是经典方向补齐，不能据它说原一个bounded slope chart覆盖水平全部方向，也不另认新颖性。

有限δ原tube族以Y_i=T_i取λ=1，逐管与平均均完整，因此免费PBP桥在最强density下已失败。任意shading后仍可用原direction-separation CW upper，但retained parameter子集未必有AD lower/full angular；平均heavy只保原incidence和相应权比例，不能保每球固定投影lower。反过来，slice energy/Hausdorff论证用完整共同clock，不能改称任意shading定理。

令K_m为Z_m的整unit段并，E_m=N_δK_m。截断参数距原参数Oδ，且`(a,v,u)↦(a+uT(v)v,uT(v))`、`T(v)=(1+|v|²)^−1/2`在原bounded域Lipschitz，所以K_m⊂K且`d_H(K_m,K)≤Cδ`。固定倍邻域有`|N_(Cδ)K_m|≤C′|N_δK_m|`（取δ-separated最大点网，δ/2球不交再覆盖），故`|N_δK|≤C′|E_m|`。因此E_m确随δ趋零，却没有沿小δ序列的fixed δ^c upper：若有，则同尺度cover即迫`dim_H K≤5−c`。不是仅凭K_m⊂K就倒推体积lower。

也未验证完整critical source的filledX、pointΦ、selectedξ/coherence及原跨块mass。联合4AD/满chart方向/whole-containment CW本身不付这些条件；此反攻严格不升级成该source反例或ordinary失败。

## 8. 资格判定、依赖与本轮停止

已自含付数字分解、AD/局部固定BP、纯不可整流的nonflat-child/tangent论证、finite方向和CW、真实单位段compact并集，以及energy/product/slicing的满维结论。具名高级输入只保经典rectifiable切平面事实与BF投影定理的实际阅读范围，不冒wholeproof认证。PBP/BPLG失败是对明列免费接口的真实反攻，不是仅一个抽象topological模型。

据spec应停止“联合AD＋固定好投影自动稳健PBP”的桥，不加smooth/unique selector或desired PBP成功公设，不把finite样本正投影当稳健下界。ordinary/directHRZ/完整sticky及真严格低维反例四路仍open；无新维数界、数学ID或major。A/root主文落盘后再实际逐式交叉读并记录；当前未预写formal、metadata、Git或同步状态。
