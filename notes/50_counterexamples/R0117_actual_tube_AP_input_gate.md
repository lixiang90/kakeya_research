# R0117：真实单位圆管的近似3AP反攻与条件输入闭包

2026-10-27，constructive_gate。先实读 research/rounds/R0117_AP_input_qualification_spec.md，再展开本稿；仅编辑本分配文件，不改controls、文献metadata或Git。下述AP-free配方是经典方法的自含应用，不登记新major/数学ID，不以此完成高维Kakeya Goal；独立审查另行安排。

## 1. 恢复、经典来源与精确对象

已运行python scripts/context.py，读GOAL、STATE、ROADMAP当前表、registry/最近轮次入口；完整读回R116两份uniform-codec独审、R116 next及后继选择审查。R114 whole-cell质量筛法、R115 full-source graft的实际已读闭包沿用，不重跑其证明。当前总目标仍须超出旧六维Hausdorff17/4；本轮只审Dahia式AP预处理能否由原near-full marks免费提供。

经典来源比对为Ben Green–Julia Wolf，[A note on Elkin's improvement of Behrend's construction，0810.0732v1](https://arxiv.org/abs/0810.0732v1)。已实读本地提取intro及§2目标段，知其报告经典Behrend/Elkin型高密度3AP-free构造；本稿不使用其优化界或torus精化作黑箱，不声新颖性/最优性。以下仅自证整数无进位球层和真实管应用。

固定a∈(0,1)、C≥0。真实管为R⁵中单位线段的半径δ **Euclidean圆邻域**

    T=N_δ(b_T+[0,1]θ_T),       |θ_T|=1.

clock统一指各原轴自身的单位arclength坐标

    τ_T(x)=<x−b_T,θ_T>.

round caps使τ_T(T)=[−δ,1+δ]，不会将caps裁掉后仍冒原质量。若ω_j是R^j单位球体积，则精确

    |T|=ω₄δ⁴+ω₅δ⁵=ω₄δ⁴(1+16δ/15).                       (1.1)

两端caps合成一个R⁵ δ-ball体积。所有管体积相同，原N与I=Σ_T|Y(T)|均按这些实际管归一。

主类别M是任意Lebesgue可测Y(T)⊂T。另给格式保留类别P：Y(T)是原dyadic δ-cell pieces Q∩T的字面并，或已给的whole cells Q⊂T的并；piece直径≤Dδ，D=√5。它们均仍是实际T内marks。**不**把所有intersecting cells的完整Q union默称⊂T，不扩大T半径，不将thin slab交误叫同δ whole-cell shading。若某外部finite theorem要求另一种未截断cube规范，必须另核其hyp；本稿不声该格式已自动覆盖。

测试AP为clock支持中存在τ₀<τ₁<τ₂，满足

    |τ₀+τ₂−2τ₁|≤Cδ，
    min(τ₁−τ₀,τ₂−τ₁)≥δ^a。                               (1.2)

本稿输出的支持在整个R上均无此AP，因此无论测试包含caps clocks还是仅取[0,1]，反攻都成立。

## 2. 无进位整数球层：精确3AP-free

固定整数d>2、m≥2，令B=2m、n=B^d。对向量v∈{0,…,m−1}^d按平方范数分层。可能值至多d(m−1)²+1；某层V满足

    |V|≥m^d/[d(m−1)²+1]
        ≥c_d m^(d−2)=c'_d n^(1−2/d).                      (2.1)

定义base-B编码

    k(v)=Σ_(j=0)^(d−1) v_j B^j，       A={k(v):v∈V}⊂{0,…,n−1}.

若k(v₀)+k(v₂)=2k(v₁)，每位左右digits均在{0,…,2m−2}，严格小于B；两边都无进位，base-B唯一性迫v₀+v₂=2v₁。三向量同一平方范数，且

    ||v₀||²+||v₂||²
      =2||v₁||²+(1/2)||v₀−v₂||²，

故v₀=v₁=v₂。A没有非平凡整数3AP；这里不要求先指定AP间隔或只验有限样本。

另有粗upper |V|≤m^(d−1)：前d−1坐标固定后，最后的非负整数坐标由平方范数至多唯一确定。此upper只用来准确报告marks体积可以缩小，不优化经典配方。

## 3. 全部足小dyadic δ的时钟模型与容差

先固定任意s>0，取整数d>max(2,2/s)。令c=1、H=c+D=1+√5，并固定一个二幂L=2^ℓ，满足

    L>C+4H+2.                                             (3.1)

这些参数先于δ固定。对每个足小dyadic δ=2^(−k)，置

    q=floor((k−ℓ−3)/d)， m=2^(q−1)，
    n=(2m)^d=2^(dq)， h=Lδ。

δ足小时q≥2。直接由floor得到

    (2^(d+3)Lδ)^(-1)<n≤(8Lδ)^(-1).                         (3.2)

因此不是只在δ=n⁻¹的子序列上施工；每个足小dyadic δ都有一个相差固定常数的n。取§2的A，并定义

    S_δ=∪_(j∈A) [3/8+h j−δ, 3/8+h j+δ].                  (3.3)

h n≤1/8，故δ足小时S_δ⊂[1/4,3/4]。L>2使各区间不交，且

    |S_δ|=2δ|A|≥c_(d,L)δ^(2/d)≥c_(s,C)δ^s，
    |S_δ|≤C_(d,L)δ^(1/d).                                 (3.4)

最后的upper来自§2粗upper；全是固定d,L下的真实幂和常数，无o(1)替代量词。

保留更宽的集合

    S_δ^+=∪_(j∈A) [3/8+h j−Hδ, 3/8+h j+Hδ].

任意phase v∈R和任意τ_i∈S_δ^++v，写τ_i=3/8+h j_i+v+e_i、|e_i|≤Hδ。若满足(1.2)的第一式，则

    |h(j₀+j₂−2j₁)|≤(C+4H)δ，
    |j₀+j₂−2j₁|≤(C+4H)/L<1。                             (3.5)

整数只能为0；§2迫j₀=j₁=j₂。所以三个clocks都在同一长度2Hδ区间。因固定a<1，δ足小时δ^a>2Hδ，长gap条件不可能。因此**每个translate S_δ^++v**均无(1.2)；S_δ及其任意subset也如此。这里已预付Cδ及whole-piece额外clock误差，没有把exact整数AP-free直接冒作任意近似AP-free。

## 4. 真实R⁵全方向原管上的无条件反攻

给定任意η>0，取0<s<η，再按§3固定d,L。对RP⁴取一个maximal δ-separated δ-net，选单位代表θ_T，N≈δ^(−4)；这是物理无向方向的全δ-net，不是低维方向曲线。令各原单位轴为[0,1]θ_T，所有真实T=N_δ[0,1]θ_T均在固定bounded box内。单位长度、δ和N从未随marks改变。

在M类别中取

    Y(T)={τθ_T+z: τ∈S_δ， z⊥θ_T， |z|≤δ}.

S_δ位于原轴内区间，所以这些marks字面包含于同一实际T，cross-section是真R⁴半径δ球。clock投影恰为S_δ。精确体积与密度为

    |Y(T)|=ω₄δ⁴|S_δ|，
    |Y(T)|/|T|=|S_δ|/(1+16δ/15)，
    I=Nω₄δ⁴|S_δ|。                                       (4.1)

由(3.4)、s<η，δ足小时含固定常数的density真正≥δ^η，**每根原管都成立**，而每根的clock支持都无(1.2)。这同时严格否定逐管假设下“至少一管有AP”，以及仅平均λ=I/(Σ|T|)≥δ^η下的同一无条件结论；不是由平均倒推逐管。

P类别也有实际版本：从每根T的原piece partition出发，保留所有与上述Y(T)有正质量交的原pieces，记为Y_P(T)。它们的并仍⊂T，质量至少(4.1)，且每点clock距S_δ至多Dδ。因此支持⊂S_δ^+，同样无(1.2)。δ足小时S_δ^+仍在(0,1)，故

    ω₄δ⁴|S_δ|≤|Y_P(T)|≤Hω₄δ⁴|S_δ|.                       (4.2)

上式使用不交的宽区间及每slice截面≤ω₄δ⁴；没有假完整axis-aligned δ-cube能装入任意方向半径δ圆管。若只允许whole Q⊂T且不给足够多此类cells，本稿不免费声它们填满T；格式闭包见下一节。

整管bush union体积是固定常数量级，marked union则**可以**随δ以小幂缩小：由(3.4)、(4.1)/(4.2)，|∪Y|≤I≤Cδ^(1/d)。不能声marks union有固定正体积。相反，也未由此取得预先固定β、任意小η门下的bad footprint，更不是samecompact strict Hausdorff反例。

为明确参数限制，本bush模型还满足|∪Y|≈|S_δ|≈λ，P版在固定H费用内同样成立。lower可取每个θ_T半径cδ的互不交角cap，总球面质量≈Nδ⁴≈1；半径r取每个S区间的中央半长部分，r≈1，角cap中的rω仍有τ∈S及垂距<δ。polar积分给|∪Y|≥c|S_δ|。因此当η<β时，density≥δ^η与该模型的|∪Y|≤δ^β不能同时成立于足小δ。这里排的是本模型的参数使用，不能据此证明一般small-footprint配置不存在。

## 5. 任意原marks的逐管phase筛选：含caps且union不增

现在原T可以任意放置，方向、N和所有单位轴均已给定；不要求bush或small footprint。对每根管给任意原可测Y(T)⊂T。采用§3同一S_δ，但各管独立选phase v_T。

固定x∈T，其clock τ=τ_T(x)∈[−δ,1+δ]。S_δ⊂[1/4,3/4]，δ足小时τ−S_δ⊂[−2,2]。故按真实Lebesgue phase有

    ∫_(-2)^2 1_{S_δ+v}(τ)dv=|S_δ|。

Tonelli/Fubini在原R⁵ marks上给

    ∫_(-2)^2 |Y(T)∩{τ_T∈S_δ+v}|dv
      =|S_δ| |Y(T)|.                                     (5.1)

由平均值原理，存在一个phase v_T，使

    |Y_f(T)|≥r_δ|Y(T)|，       r_δ=|S_δ|/4≥cδ^s，
    Y_f(T)=Y(T)∩{τ_T∈S_δ+v_T}.                            (5.2)

有限N根管逐个选择即可，不需要方向参数上的可测选择，也不按point换phase。caps的全部原质量已在(5.1)中计算，没有先删τ∉[0,1]再冒同一个I。即使某管质量为0也可任取phase。

每个Y_f的clock支持⊂S_δ+v_T，故无长gap近似AP；又Y_f(T)⊂Y(T)，所以**真实marked union不增**。原管、方向、单位长度、半径及N均不变。

若原Y属于P格式，薄slab交Y_f未必仍是该格式，不能直接重调用只给pieces的输入。此时定义Y'(T)为所有与Y_f(T)有正质量交的**原pieces**之并；每个piece都是原Y的一部分，所以

    Y_f(T)⊂Y'(T)  模零测，   Y'(T)⊂Y(T)，
    |Y'(T)|≥|Y_f(T)|≥r_δ|Y(T)|.                           (5.3)

这里的第一包含只用于质量，不把null点的存在性忽略掉：对任意保留piece确有一个实际交点，其clock在S_δ+v_T内；piece直径≤Dδ，故其**所有**点的clock都在S_δ^++v_T中。于是Y'的实际支持亦无(1.2)，不是只对a.e. clock成立。whole Q⊂T格式若已给，也用相同保整原Q操作合法；不会凭空补不存在的Q。

这一rounding只向原Y内恢复pieces，不取新的邻域或加新cells。因此union仍⊂原union，实际Tδ不变，未将tube宽度换成固定倍后省略分母。M类别直接取Y'=Y_f；P类别取(5.3)。两类各自都支付合法格式。

## 6. 原N/I、逐管与平均分别核

记原V_T=|T|，所有真实单位round δ管的V_T都等于(1.1)。令I'=Σ|Y'(T)|。由逐管(5.2)/(5.3)，

    r_δ I≤I'≤I，
    λ'=I'/(ΣV_T)≥r_δ λ，
    λ'_T=|Y'(T)|/V_T≥r_δ λ_T。                            (6.1)

所以若旧每管λ_T≥δ^u，新每管都≥cδ^(u+s)；若旧**仅平均**λ≥δ^u，只有平均lower同样得到，未赠旧或新每管δ^u。这里无需删低密度管或heavy pruning：逐管相对保留率本身就统一。

原q=1、p=I'/I∈[r_δ,1]，因此精确λ'=pλ。一般另删到qN根等体积原管且保pI时才是λ'=(p/q)λ；caps已包含在等体积V_T中，不另藏常数。AP-free对进一步marks restriction保留，但density和原I需重新计费。

各管phase独立不是WZ source的共享time-layer筛选。若原T已有joint4AD/whole-CW，原管不动就精确保留它们；ordinary方向net本身不自动提供joint-AD lower。若保原坐标/labels并取E'⊂E、Φ'_p⊂Φ_p，原矩阵variation、coarse Φ覆盖和strict ξ的upper一致性亦继承，nativeY的absolute tube-KT/AD upper对子集也保。真正首个未付门是将surviving canonical访问重组为逐点Φ'_p的实际witness及每尺度AD lower，再同时付filled X、nativeY的fine及全部coarse-Y union AD lower；逐管积分保量没有给这些条件。若原E/Φ/ξ全不改，则完整source仍真，但其canonical shading不自动变成新的AP-free marks。准确范围另见 notes/00_map/R0117_AP_source_scope_gate.md；本稿不据普通删选重调用完整source定理，闭包仅作用于§1的ordinary marks类别。

## 7. Small-footprint条件AP输入已经承担finite排除责任

固定β>0以及同一a,C。分别在M和P类别、分别对逐管密度(pt)或平均密度(av)，定义：

    AP_β^type(η)：所有足小dyadicδ，对原全方向δ-net真实单位管，
      若density门≥δ^η且|∪Y(T)|≤δ^β，则至少一管有(1.2)；

    FE_β^type(η)：在这些原对象、同density门和footprint门内无实例。

type在此固定为pt或av，不在论证中改换；N≈δ^-4的固定常数、所有方向/round-tube/piece约定也保持原样。若某input给自己的固定a,C，先固定它们再选L，不允许C随δ无限增长或a先随δ趋1。

假设AP_β^type(η)成立。反设原实例有较强density门δ^(η/2)及相同footprint。取s=η/4，按§3–6在**每根原管**独立phase并保原格式。δ足小时

    density_new≥c δ^(η/2+s)
                =c δ^(3η/4)≥δ^η。                        (7.1)

含常数的最后一步因η固定、δ后足小成立。原union不增，故仍≤δ^β；原N、方向及unit T全保；每管都无(1.2)，与AP输入矛盾。因此

    AP_β^type(η) ⇒ FE_β^type(η/2).                         (7.2)

pt版本用逐管(6.1)，av版本只用平均(6.1)，两者分别完整证明。没有通过删管把av改成pt并暗失全方向δ-net。

反向同η有

    FE_β^type(η) ⇒ AP_β^type(η)                            (7.3)

因为前提域为空。故按“固定β后存在足小η”的正幂量词，两者等强：存在某η的条件AP输入已承担存在较小η的ordinary finite排除责任。不是同一数值η逐字双向，也没有证明任一为真。η/2、s=η/4、d,L及常数均在δ之前固定，δ阈值可依这些固定参数和原input阈值取更小。

这里的finite排除仅为上述明确ordinary类和固定β的命题，不自行声已经完成全部Hausdorff桥或一般猜想。§4无条件反攻不自动提供预先固定β、任意小η的实例；(7.2)是合法删选的**条件强度审计**，不是实际造出开放small-footprint反例。

## 8. 与旧闭包、来源及更强AP命题的关系

本证明否定最低“至少一管有近似3AP”，所以在同一无条件hyp下，声称正幂数量、many differences或能返回原I的更强统一超饱和同样不能成立。它不否Dahia在固定整数密度下的具名Varnavides输入；δ^η随δ趋零与固定密度是不同量词。经典球层不是新结构工具，不调m/d/L、AP长度或常数续轮。

R114整格mask针对fixed-format carrier，R115 conditional graft针对强∀grain source cap，R116针对uniform codec；本次具体性质是原真实管clock的长gap AP。新性质不意味着新正gain：(7.2)已经指出其small-footprint版若对全部合法原marks统一可重调用，就承担相应finite排除，拒绝将其另名为廉价初始化。

可测marks与原piece/whole-cell格式已分别支付，不声任意shading格式或完整source闭包。平均/逐管没有混用；原I是实际R⁵体积之和，不是clock点数；独立phases没有换原管。有限整数证明只负责§2的全参数代数，真实连续AP-free和全部dyadic尺度另由§3、真实管质量由§4–6支付，没有以有限实验代替它们。

## 9. 停止与审查边界

实际已完成：经典无进位球层；全部足小dyadicδ的Cδ容差/长gap模型；真实全方向R⁵单位round tubes的逐管及平均无条件反攻；含caps、保原格式、逐管质量r_δ≥cδ^s的独立phase删选；以及small-footprint条件AP到ordinary finite排除的η/2责任和反向真空。

停止无条件AP前端及经典配方常数续轮，不把“改成只在small footprint成立”登记成新局部输入。若要新正机制，仍需此前未付的原方向—空间重叠联合信息；本稿没有给它。无新ordinary/Hausdorff下界、完整source正gain、samecompact严格低维全方向反例、major或Goal完成证据。

自证不计本人独审；待未参与施工代理实际逐式审查本稿raw版本。未经外部同行评审，不预认证metadata、Git或同步，root统一整合。
