# R0116 真实构造出口：uniform 全clock仿射 codec 的固定误差门

2026-10-26，constructive_gate。宏观后由root锁定 research/rounds/R0116_uniform_clock_codec_working_spec.md，再展开本稿。本文给一种构造转移接口的严格资格反攻，不是Kakeya反例，也不以初等no-go完成长期Goal。本代理只编辑本分配稿，不改controls、文献metadata或Git；独立审查另安排。

## 1. 恢复、旧构造范围与本轮首要缺口

已运行python scripts/context.py，读当前GOAL、STATE、ROADMAP当前表、registry最近项/旧项入口、R115 round与R116 macro spec，及上述锁定working。此前实读的R81/82/83全compact/selector门沿用其真实scope；本轮定向实读R82开角度无Hölder反攻、R93互补数字真实unit段及满维证明、R94 Fourier/全方向边界，核R112非sticky/LW与R114restricted-center失败记录。没有重跑旧计算或把摘要冒作高级wholeproof。

构造出口的总量词仍是同一个实欧氏compact K⊂Rⁿ，每个物理方向含真实unit segment，并证明dim_H K<n。零体积、低维labels、只在某些时刻压缩、不同尺度不同集合、有限域或p-adic小集合均不足。R93已给真实满方向零体积而dim_H=5的严格数字校准；不重开Cartesian/乘积/finite-clock包装。R115 conditional source graft只反强∀grain标尺的便宜性，未造任何无条件完整source或Kakeya反例。

先查98-source目录，再作有限primary筛查。此次命中的[FD–de la Salle构造](https://arxiv.org/abs/2607.14824)仍是已入库的logarithmic neighborhood-volume upper；[Du曲线压缩](https://arxiv.org/abs/2610.05404)仍是已入库curved、proper-direction对象。Germain–Latocca 2606.29993也已在R55/R88筛过，未作为新构造输入。有限检索没有给新的可采用strict Hausdorff upper，不认证前沿穷尽；本稿不新增PDF或把来源标题当证明。

本轮实际检验另一明确机制：能否使用一个随δ任意变化、甚至非连续/不可测的codec，把p-adic unit-ball中**全部仿射插值关系**统一送成同一真实[0,1]时钟，且误差o(1)？这比只保一个Kakeya选线子族的相关tuples强。下述有限certificate排除此uniform接口，并明确其不能反推更稀疏的构造路线。

## 2. 精确命题、量词与所用元组

固定素数p。Z_p为p-adic整数环。给任意函数

    c:Z_p→[0,1],       c(0)=0, c(1)=1,

定义一致barycentric defect

    D(c)=sup_(a,b,t∈Z_p)
      |c((1−t)a+t b)−[(1−c(t))c(a)+c(t)c(b)]|.             (2.1)

不给连续性、可测性、injectivity或ring-map假设；同一个c必须用于全部a,b,t。函数可以随研究尺度δ变化。主张：

    p odd： D(c)≥1/3；
    p=2： 若存在z且|c(z)−1/2|≤ζ<1/2，
          则D(c)≥(1/2−ζ)/4。                              (2.2)

exact D(c)=0时，odd p无解，p=2恰为parity函数c(a)=a mod2∈{0,1}；该parity不是到R的ring homomorphism。特别exact完整实clock的满射不可能。

为便于逐式独审，把tuple固定按(a,b,t)顺序记：

| 名称 | tuple | p-adic输入表达式 | 条件 |
| --- | --- | --- | --- |
| T₁ | (0,−1,−1) | 1 | 所有p合法 |
| T₂ | (1,0,−1) | 2 | 所有p合法 |
| T₃ | (0,1/2,2) | 1 | 只在odd p使用 |
| T_even(b) | (0,b,2) | 2b | b∈Z₂ |
| T_odd(b) | (−1,b,2) | 1+2b | b∈Z₂ |

所有−1、2均在Z_p。odd p时2为unit，故1/2∈Z_p；p=2时不使用1/2，也不偷偷把它当unit-ball clock。p2的任意z恰为2b或1+2b，所需b仍在Z₂。

证明只需假设(2.1)每个tuple误差≤某ε，导出ε的固定lower。若sup不达到，可令ε>D(c)再取ε下降到D(c)，无最大值/紧性或可测性假设。

## 3. 两个共同tuple产生的数值约束

设全部tuple误差≤ε，记

    q=c(−1)∈[0,1],       r=c(2)∈[0,1].

只需研究0≤ε<1；更大ε时(2.2)已平凡。T₁给

    |1−q²|≤ε,       所以q≥sqrt(1−ε)≥1−ε。                 (3.1)

T₂给

    |r−(1−q)|≤ε,    所以r≤1−q+ε≤2ε。                     (3.2)

端点归一与range均实际使用：T₁的RHS为q²需要c(0)=0；T₂的RHS为1−q需要c(1)=1；q≥0及后续凸权估计来自c∈[0,1]。不能把结论声为任意无界real-valued函数的同一数值界。

## 4. Odd p：三个合法tuple给ε≥1/3

odd p下T₃合法。其输入值为1，RHS为r c(1/2)，因此

    |1−r c(1/2)|≤ε.

由0≤c(1/2)≤1和(3.2)，

    1≤r c(1/2)+ε≤r+ε≤3ε。                               (4.1)

所以ε≥1/3，进而D(c)≥1/3。证书仅T₁、T₂、T₃三个tuple；不借Hensel、field embedding、拓扑、连续延拓或Hausdorff定理。特别D(c)=0无解。

这不是p-adic域到R的标准field-map no-go换名：本hyp没有假加法或乘法同态，目标只是有界实clock，证明直接消费三个具体插值关系。下一节的p2 parity例更说明不能无条件把该hyp先叫ring homomorphism。

## 5. p2：range二簇、midclock门与exact parity分类

先不假满射。对任意b∈Z₂，用T_even(b)得

    |c(2b)−r c(b)|≤ε,
    c(2b)≤r+ε≤3ε。                                       (5.1)

用T_odd(b)得

    |c(1+2b)−[(1−r)q+r c(b)]|≤ε,
    c(1+2b)≥q−r−ε≥1−4ε。                                (5.2)

故整个range满足

    c(2Z₂)⊂[0,3ε]，
    c(1+2Z₂)⊂[1−4ε,1]。                                  (5.3)

若存在z使u=c(z)∈[1/2−ζ,1/2+ζ]，则：

    z even： 1/2−ζ≤u≤3ε ⇒ ε≥(1/2−ζ)/3；
    z odd：  1−4ε≤u≤1/2+ζ ⇒ ε≥(1/2−ζ)/4。

统一取(2.2)的保守lower，不优化常数。给定一个midclock见证z后，除了T₁、T₂，只需对应的一个T_even或T_odd；后者的b由z的even/odd分解确定，不要求选择连续或measurable。

exact ε=0时，(5.1)迫全部even值为0，(5.2)迫全部odd值为1，所以parity是唯一候选。还须核其确满足**每个**tuple：若t even，则(1−t)a+t b≡a mod2，实RHS为(1−0)c(a)+0 c(b)=c(a)；若t odd，p-adic输入≡b mod2，实RHS为c(b)。两种情况下都是0/1的精确real等式，绝不只是“mod2相等便可把任意加法搬到R”。

parity不供whole real clock；其像仅{0,1}。它也不是unital ring homomorphism到R，因为c(1+1)=c(2)=0而c(1)+c(1)=2。exact分类因此与常见field-map论证有一个必须保留的例外，不能在证明前把它排掉。

## 6. 非coordinatewise的真实目标空间扩展：三个误差

现取任意d,n≥1、任意H:Z_p^d→Rⁿ，不假它逐坐标作用、连续或可测。取非塌陷pair P₀,Q₀，记

    D₀=||H(Q₀)−H(P₀)||>0,
    v=[H(Q₀)−H(P₀)]/D₀.

同一normalized clock c:Z_p→[0,1]用于全部P,Q,t，且假设

    ||H((1−t)P+tQ)
       −[(1−c(t))H(P)+c(t)H(Q)]||≤e D₀                 (6.1)

对全部P,Q∈Z_p^d、t∈Z_p成立。误差分母始终是这个明确D₀，不按tuple另选，不能在physical unit要求前偷换尺度。令

    L(a)=P₀+a(Q₀−P₀)∈Z_p^d,
    h(a)=<H(L(a))−H(P₀),v>/D₀.

向量坐标的线性投影不把p-adic数送到R；这里只投影**已经定义的real输出**。把(P,Q,t)=(P₀,Q₀,a)代入(6.1)，得到

    |h(a)−c(a)|≤e，       h(0)=0，h(1)=1。                 (6.2)

再对真实输入pair(L(a),L(b))调用同一(6.1)。p-adic端严格有

    (1−t)L(a)+tL(b)=L((1−t)a+t b).

沿v投影并除D₀，故

    |h((1−t)a+t b)−[(1−c(t))h(a)+c(t)h(b)]|≤e。           (6.3)

以(6.2)替换left的h只损e；替换RHS两项的h，因0≤c(t)≤1，其**凸权和**误差≤e；再加(6.3)自身的e，得到

    D(c)≤3e。                                             (6.4)

因此

    p odd： e≥1/9；
    p=2且有midclock见证ζ： e≥(1/2−ζ)/12。                  (6.5)

没有多花一个免费的独立clock，也没有只证一个pair后赠全部L(a),L(b)关系。H不coordinatewise的反馈不能绕过这个**uniform-all-pairs**门；原因正是其hyp已允许在同一p-adic line内任意换两个anchors。实际Kakeya选线子族一般没有这个闭包，故不可倒用。

exact e=0且c供[0,1] wholeclock时，不可能有这样的非塌陷pair。若去掉wholeclock要求，p2 parity以及任意只依模2 residue vector的finite-image H确可满足(6.1)：t even保P residue，t odd保Q residue，实系数各为0/1。它们不包含真实正长度Euclidean段。constant H亦总可塌陷通过，所以D₀>0不是装饰hyp。

## 7. 一个真正compact/full-clock而defect大的显式codec

给出独立校准，不能只说“转移尚缺”。每个x∈Z_p有唯一展开x=Σ_(j≥0)a_jp^j，a_j∈{0,…,p−1}。定义digit-reversal map

    M_p(x)=Σ_(j≥0)a_j p^{−j−1},
    c_p(t)=M_p(−t)。                                      (7.1)

值域在[0,1]；c_p(0)=0，c_p(1)=M_p(−1)=1，因为−1的所有digits均p−1。若两个p-adic数同余mod p^k，M_p的实值差至多p^{−k}，故M_p连续，负号也连续。每个y∈[0,1]选一个实base-p展开（y=1用全p−1），把同一digits按p-adic正幂读成−t，就有c_p(t)=y。因此这是同一compact Z_p上的连续、normalized、满实clock codec，不因端点缺失或非紧而失败。

但T₁给一个实做的常数误差：

    c_p(1)=1，
    c_p(−1)=M_p(1)=1/p，
    |c_p(1)−c_p(−1)^2|=1−p^{−2}≥3/4。                    (7.2)

所以compactness、连续full-clock覆盖均成立，uniform仿射组合却明确失败。它不是unit-reparam修补，不是把curve straighten后声straight Kakeya，更没有证明任何低维全方向集合。若只看t↦c_p(t)覆盖[0,1]而丢掉(7.2)，就会把“数码时钟满射”错当“保全部原直线关系”。

## 8. δ-dependent量词、restriction与旧R92的准确差别

允许每个δ另选任意c_δ、H_δ；无需先有极限函数。若c_δ的像ζ_δ-dense于[0,1]且ζ_δ→0，则上述固定tuple证明逐δ成立。若dense按dist(1/2,image c_δ)≤ζ_δ定义且inf未达到，先对任意ζ'>ζ_δ、ζ'<1/2选近似midpoint见证，再令ζ'下降到ζ_δ；lower不变。这也覆盖ζ_δ=0而dense像并非满射的情形：

    odd p： D(c_δ)≥1/3；
    p2： D(c_δ)≥(1/2−ζ_δ)/4。

故D(c_δ)不能趋零；向量版e_δ同样不能趋零。D₀,δ可随δ变，但(6.1)按该非塌陷输出长度归一；若absolute error虽小而D₀,δ更小，不能在之后放大成unit segment却仍说相对误差小。D₀=0的完全collapse不供所需physical方向或unit长度。

这是**sup error**结论，不能改读为average error。所用有限certificate tuples可在Haar乘积测度下是零测集合；删去这些tuple、只保稀疏/相关incidences、只在构造实际使用的lines上给clock，均可能使本certificate不再存在。本稿未证明这些较弱hyp也失败。若c或H按tuple/line分别重选，也已换成另一个问题。

R92的原对象是真实Euclidean有限管、共同h-grid、有限field/ring轨道、方向代表长度与mod采样，失败是其精度/primitive representative/方向计数预算；本稿的hyp是单一codec对全部p-adic affine tuples的uniform intertwining，失败已在有限个normalizedreal等式上出现。二者不是同一个待证lower换名，也不借此否定R92已付finite transfer、所有p-adic方法或所有多尺度构造。尤其没有从全tuple障碍倒推某个actual source一定含这些tuple。

这里没有一族原Euclidean T和marks可报告正gain；不能把(2.2)的数值lower装成阴影体积lower或Hausdorff定理。若以后用于finite原管问题，仍须另付真实T/N/I、共同clock、全部physical方向、point restriction及shading density。一般保管q、保I比例p时λ'=(p/q)λ；该账不会因codec是全称命题而消失。平均/逐管都没有在本稿被免费生成。

## 9. 构造资格决定与停止

本轮实际得到exact分类、定量finite certificate、非coordinatewise uniform目标空间扩展，以及一个连续compact/full-clock codec的显式失败。它们共同改变下一行动：停止“先统一保全部p-adic仿射关系，再以任意δ-dependent数码clock无损搬到real”的接口，不再优化常数或更多p分类。

本稿没有给samecompact K、全部物理方向unitsegments及strict dim_H upper的正候选；scalar/fullspace codec obstruction亦不是这种反例。稀疏、相关tuple的real多尺度转移并未被本稿排除，若未来重开须写实际选线、保量和缺失certificate的不同机制，不能只把uniform改名。R81/82/83 selector、R91/PDE、R94–99 currents、R112零测和R114原公式等冻结保持。

不登记新维数下界或major，不以本轮初等资格结果结束Goal；无新ordinary/source正gain。本人证明不计本人独审，root安排未参与机制的代理逐式审查实际raw版本后再整合状态和同步；未经外部同行评审。
