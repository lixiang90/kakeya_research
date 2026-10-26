# R0116：ordinary与finite新输入的一手资格审计

2026-10-26，new_projection_gate。只编辑本分配稿，root统一归档/提交。Goal active，基线六维Hausdorff17/4；本稿没有取得ordinary n≥5新下界、完整source gain或major，未经外部同行评审。

## 1. 恢复、真正目标及本次不同依据

实际运行context，读GOAL/STATE/ROADMAP/registry当前摘要及R115 next、R116 macro spec。强∀grain scalar cap、weighted/phase重命名、已有seed/KT数表、fixed-format carrier及proper三角参数续线均不再作为本出口主候选。

ordinary输入必须明确保：真实单位δ管、物理方向δ分离或所需角帽、原N≈δ^{−(n−1)}、实际marks Y(T)及原I=Σ|Y(T)|、平均λ=I/(Nδ^{n−1})；先固定目标增益、后η小、δ小。单尺度volume不能直接叫Hausdorff，iid人为重采样的运算值也不自动属于原marks。

本次独立新依据是一篇此前98source目录未列的primary：Rupert Li的exact discrete entropic sum-product。下面不仅读标题，而且对其到物理δ尺度的接口给出完整精确反攻；另核一篇真正October的算术随机差分结果。有限检索无匹配不认证前沿穷尽，更不认证所有n≥5新定理不存在。

## 2. 有界检索的实际范围与排重

2026-10-26通过web实际查询arXiv的一手命中，包括“Kakeya 2026 October”“Kakeya Hausdorff higher dimensions 2026”“Kakeya density 2026”、2610/2609标识号定向查询及real/discretized entropic sum-product。镜像、新闻、自动review和GitHub综述只作定位，数学结论以下列primary为准。

| 真实primary | 本次实际读域 | 资格 |
| --- | --- | --- |
| [Rupert Li, 2607.29042v1](https://arxiv.org/abs/2607.29042v1)，2026-07-31 | 官方history、HTML Th1.5及1.6/1.7的范围，Lemma2.7及其证明 | 新source；精确离散熵输入，非已付的δ-scale/ordinary输入。root决定统一下载归档。 |
| [Gabriel Dahia, 2610.18859v1](https://arxiv.org/abs/2610.18859v1)，2026-10-13 | 官方history及完整短HTML：Th1.1、Lemma1.2、Theorem2.2引用及其cover证明 | 新命中，fixed-length整数AP/random differences；不授ordinary Kakeya/Hausdorff。此稿不自行下载或改catalog。 |
| [Moreira 2610.06181](https://arxiv.org/abs/2610.06181)、[Choudhuri 2610.12480](https://arxiv.org/abs/2610.12480) | fresh primary abstract/history定位，和目录中已有范围比对 | 已存R33及后续scope；不是本轮新输入，R4相应旧声明不覆盖n≥5。Choudhuri日期异常沿原metadata，不凭相对搜索日期订正。 |

检索还返回spread-out Furstenberg II、codim-two planes、Liouville on tori及curved compression等。既有前者的local spread-out缺口没有改变；平面维数、速度权/Euclidean cylinder、曲线族不能当作普通直线全方向n维输入。没有把重复98来源或新标题计作新增。root另读ICM survey及pencil-sensitive stickiness，本人不重复认证其wholeproof。

## 3. Li的精确statement与可用范围

[Li v1 HTML Theorem1.5](https://arxiv.org/html/2607.29042v1)对iid、离散、实值、有限Shannon熵的X,X′给

    max{H(X+X′),H(XX′)}
       ≥(8/7)H(X)−c₁log H(X)−c₂−(1/2)log C_R.       (3.1)

这里H是**精确值**的Shannon entropy，log底为2；general discrete版H≥6，可用c₁=18、c₂=65，C_R是文中具名point-plane incidence的绝对常数。finite-support版另有常数，不混用。官方history当前只列v1=2026-07-31；primary PDF为 `https://arxiv.org/pdf/2607.29042v1`，未由本人下载/核bytes。该高级定理作为作者声明/具名候选，未由本项目独立全证。

同文[ Lemma2.7及proof](https://arxiv.org/html/2607.29042v1)将finite-support law扩充为(X,L)：每个X|L=ell在一个2的整数幂大小的集合上均匀，且

    H(X|L)≥H(X)−[log(1+H(X))+log e+2].               (3.2)

原X的law不变，但L不必是X的可测函数。此平均conditional-entropy声明不等于给一个具有subpower原概率的label，更没有声明H(L)=O(log H)。读证明中的dyadic layer和uniform-mixture两步后仍须保这个区分。本文实读这些使用段，不认证整篇incidence/energy高级proof。

## 4. 同尺度8/7接口的远离零严格反攻

定义H_δ(Z)=H(floor(Z/δ))。取N=2^m、m≥3、δ=1/N，

    A_N={a/N:N/4≤a<3N/4, a∈Z},
    X∼Uniform(A_N),  M=#A_N=N/2,  H=log M.           (4.1)

这是固定非退化区间[1/4,3/4]内的δ-separated网，不靠近零、不随δ缩空间。X位于δ-lattice，故H_δ(X)=H。X+X′范围长度<1、XX′范围长度<1/2，因此

    H_δ(X+X′)≤log(2M+2)≤H+2,
    H_δ(XX′)≤log(M+2)≤H+2.                         (4.2)

所以任何不带饱和/分维假设的same-δ版本

    max{H_δ(X+X′),H_δ(XX′)}≥(1+c)H_δ(X)−O(log H_δ(X))

在任意固定c>0下都严格失败。不是只有一个小N数值例，而是全部大m。

精确product entropy大还可不依赖Li独立证明。令r(z)为正整数区间[N/4,3N/4)中ab=z的有序表示数，E=Σr(z)²。若ab=cd，写a=gu、c=gv、gcd(u,v)=1，则b=vh、d=uh。以r=max(u,v)分组，有≤2r对(u,v)，g,h各≤N/r；故

    E≤Σ_(1≤r≤N)2r(N/r)²≤C N²log N.

在M²个等权有序pairs上，collision probability≤C logN/N²。Shannon entropy不小于Rényi-2 entropy，所以

    H(XX′)≥−log(E/M⁴)≥2H−log(1+H)−C.               (4.3)

这一经典gcd能量计算自含、无数值实验。(4.2)与(4.3)说明约H bits的精确product信息隐藏在单个δ-bin内。源(3.1)并未错误；它允许完全由这些更细的信息支付。

该参数可直接放入真实ordinary方向patch校准：n≥5，令bounded graph slope v的第一坐标遍历A_N，其余n−2坐标遍历固定非空区间的δ网格；轴为t↦(tv,t)的严格unit截段，方向(v,1)/sqrt(1+|v|²)在该patch bi-Lipschitz，N_T≈δ^{−(n−1)}，原marks取全管、λ≈1。第一slope坐标正是(4.1)的law。若要求字面δ角分离而非c_nδ分离，取固定C_nδ子网即可；基数和上述熵只差固定因子/O(1)，gcd能量upper仍适用。此真实族本身满体积，不是smallfootprint/ordinary反例；它仅表明所测试的“从exact theorem免费得到same-scale scalar熵增益”连full-density方向patch也不能统一成立。若需要整个sphere δ-net，可先补其它directions，再合法限制回这个固定正角质量patch，q为固定常数；不能借此冒称低维K已造。

## 5. Critical分维校准：不泛否真正discretized sum-product

(4.1)的dimension参数是饱和端点t=1。不能用它否Bourgain型t∈(0,1)且附各尺度nonconcentration的结论。作一项真实critical dust校准：

    δ_k=4^{−(k+1)},
    X_k=1/4+(1/4)Σ_(j=1)^k ε_j4^{-j},
    ε_j独立Bernoulli(1/2).                          (5.1)

support在固定[1/4,1/3]，δ_k-separated且#support=2^k。标准四进位分离直接给全部δ_k≤r≤1的AD维数t=1/2，常数独立k；原概率均匀。

X_k/δ_k为整数，故H_(δ_k)(X_k)=k。和的各digit为0,1,2且无carry，其概率(1/4,1/2,1/4)，每digit熵3/2，且finite base-4展开唯一，因此

    H_(δ_k)(X_k+X_k′)=3k/2.                         (5.2)

这里same-scale已有严格增长，甚至不用Li；这是分维版本的正校准，不是本轮新Kakeya输入。没有计算一般critical law的product熵或证明所有t的discretized theorem，不以一个端点失败泛否它们。真正把(3.1)变成带分维/尺度nonconcentration的定理，仍需实际量化，当前没有这种新推导。

## 6. 可合法读出的two-scale结论及原误差门

若X**恰**在δZ上，和在δZ、积在δ²Z，故精确identity给

    H(X)=H_δ(X),
    H(X+X′)=H_δ(X+X′),
    H(XX′)=H_(δ²)(XX′).

于是具名(3.1)可合法写为

    max{H_δ(X+X′),H_(δ²)(XX′)}
            ≥(8/7)H_δ(X)−O(log H_δ(X)).             (6.1)

这保留其真实two-scale强度，但只是同一个定理的lattice表述，不登记新数学结果。若原参数只是距δ-grid Oδ，把它round成X并不能使原物理product误差变Oδ²；在[1/4,3/4]上product误差仍一般为Oδ。输出δ²熵不能直接回传原δ-tube/δ-mark，(4.1)–(4.3)已量化该损失能有一整幂。

要使用(6.1)，必须从实际原source/ordinary对象给更细解析精度或一个正确的跨尺度返回，同时保原I。只把mesh从δ改名δ²会改变方向数、管宽、clock及shading density，不是一个不收费的重调用。此处没有重启旧seed/KT数表，也没有靠所求fine返回假设完成条件论文。

## 7. 原λ、iid和restriction的闭包审查

对任意单一原离散law，(3.1)允许非uniform权重，这是可能有用的新具名工具；但iid X′是在product probability space上另取独立副本。原tube/point图一般只在同一原管、共同clock或相关pair上有marks；将其补成所有独立pairs会改变reference质量和可能的支撑。定理没有说XX′或X+X′自动落原物理E，不能把entropy support当作原union volume。

合法保管q、保I比例p时仍λ'=(p/q)λ；平均heavy不保每管密度。任意restriction后可以对**新law及其独立副本**重新调用(3.1)，但其输出又是新人工product law，原G到product law的domination、density或可达性仍须证明。反向(3.1)本身也不给ordinary的原N/I、所有方向/clock或small footprint，因此尚不构成已有完整gain的等价包装；当前是接口未付，不能把“不是旧同义式”误当已获可用性。

同样，(3.2)保原marginal law及平均conditional entropy，不授某uniform piece具有所需原I比例。若两个副本分别uniformize后只取相同label，事件概率ΣP(L=ell)²未给lower；若逐label全保再平均，必须证明后继算子对这些conditional laws及原coupling有一致、可加的用途。原density费用不从“uniformization损O(log H)熵”自动变为只损polylog质量。

本轮没有补这些缺口；也不再把它们列成成功hyp。实际的独立反攻是§4已否same-scale无条件接口，§5保留真正critical尺度问题。

## 8. October arithmetic输入为何仍不覆盖ordinary

[Dahia 2610.18859v1](https://arxiv.org/html/2610.18859v1)的Th1.1固定k≥3和整数dense-set density ε>0，随机差分率p≥C(ε,k)N^{−c/loglog k}时，高概率每个S⊂[N]、|S|≥εN含一个common difference落该随机集的k-AP。Lemma1.2及proof构造一个小cover，其成员有很多k-AP differences；关键引用的是Green–Ruzsa的**小算术Kakeya集合构造**，不是证明所有此类集合有新的强lower。

这里p是随机差分抽样率，ε为固定dense整数集密度，不是原tube平均λ=δ^η；C(ε,k)及相关supersaturation常数未给可供ε随δ趋零的预算。k先固定，不能令k≈δ^{-1}再把finite AP改称真实单位连续段。结论没有物理方向δ分离、原tube marks或Hausdorff各尺度返回；不是有限域定理，也不是ordinary实欧氏Kakeya新bound。故作为本轮ordinary/finite种子输入严格拒绝，尽管它是新的October primary。

Li与Dahia都可以在各自原格式下具名使用；拒绝的是此处未经支付的几何转换。没有依据作者是否使用AI作正确性判断。

## 9. 本出口判定与可选主任务边界

本轮找到此前目录未列且精确可读的新primary Li；实际给出远离零、δ分离、可嵌入真实unit方向patch的精确-vs-δ熵反攻，以及critical t=1/2正校准。它改变了下一可采用接口：不能把exact entropy的8/7直接注入same-δ物理体积/有限Kakeya种子；能用的literal结论是(6.1)的two-scale形式，原fine精度和质量返回尚无新推导。

因此当前没有qualified ordinary n≥5正候选或新的finite维数改善。root可将此作为新文献资格主题整合、另锁精确工作，但不能将归档/接口反攻说成原Goal正gain。新PDF与metadata由root统一保存literature；本人未下载、未修改其它文件、未声新库数量/bytes或Git同步。有限搜索不认证全前沿/最优/首创，Goal继续active。
