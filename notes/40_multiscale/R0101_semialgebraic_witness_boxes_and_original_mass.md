# R0101：半代数见证乘积与原管质量

2026-10-19，root。按R0101 working5施工。新的具名密度定理有真实加权用途，但原native关系的见证编码使完整乘积过强；下面在原AD1/tubeKT输入下证明每个完整见证box只能保固定幂小的原访问质量。此为直接调用路线的严格资格结论，不是Kakeya维数增益或反例；不登记新ID、不宣新颖/重大。独立全文审另存，未经外部同行评审。

## 1. 原量词、分母及目标

固定WZ2609.22035v1 Def17.2–17.4的d5/k=ell3、κ1完整配置，原whole管N≈Kδ^-4、normalized CW≤K，并限R76的bounded chart/det-large分支。所有source高级输入具名，不在本轮全证。取R76实际anchors t,s、H*、native A=Y_t、B=Y_s、Z，m=|Z|，n_A=|A|、n_B=|B|≈Kδ^-1；m≈Kδ^-1表示上下均容K固定幂。每T∈H*有原S_T⊂Z，|S_T|≥K^-C m，H*/N≈Lδ²，不能删δ²。K=δ^-C0η，L为R76固定次σ/τ/η费用，可先选其小幂再令η小而使L≤δ^-β。

R76已从同一T和共同fine residual得到

    0≤g(a,b,u)≤1,  M=Σg=θ n_A n_B m, θ≥L^-1,
    g>0 ⇒ ||C_t(u)a+C_s(u)b+B_u−w||∞≤Cδ,
                       某个原w∈Y_u.                         (1)

每个g权来自实际T的原访问，误差为fine Oδ。欲测试的是：能否保δ^o(1)原M，用δ^-o(1)个完整几何乘积取得后继common-X输入。不会把‘g支撑于几何关系’误作g本身完整，亦不将单block当原全T的大比例。

## 2. 实际一手定理及版本范围

[Fox–Pach–Suk1502.01730v3](https://arxiv.org/abs/1502.01730v3)，2016-10-14，27页。其格式是精确边关系由t个polynomial符号的Boolean组合决定，每个顶点block次数≤D。Th1.1给密度θ的kpartite关系各侧≥θ^binom(d+D,d)|P_i|/C^k的完整box；Th1.3给fixed-format图的多项式数量齐次划分。没有说任意子边集也服从同一个格式。PDF3原图核过。

[Rubin2407.15518v2](https://arxiv.org/abs/2407.15518v2)，2024-08-14，32页。Def使用固定ambient d、总degree Δ和polynomial数量s。Th1.6正文给Ω(θ^(d+1+ζ)|P_i|)，ζ>0固定；abstract印成倒数幂，不能字面采用。§5.2 Th5.1给不等大各P_i的划分，每侧≤Cε^-(d+ζ)部分，非齐次box的总产品计数≤ε∏|P_i|。其proof sketch到density选择步骤实际读，PDF5/25/26原图核过。下面仅具名用此partition结论，不认证两篇全部高级proof或算法实现。

## 3. 任意原选边的真实加权正用途

设R⊂∏_(i=1)^k P_i为上述fixed-format关系，0≤h≤1且supp h⊂R；令V=∏|P_i|，Σh=θV>0。h本身可以任意相关、非半代数。用Rubin Th5.1取ε=θ/2，划分Π_i，r_i≤Cε^-(d+ζ)。所有非齐次boxes上的h质量≤其产品volume总和≤θV/2；齐次nonedge boxes上的h为0。因此齐次edge boxes总保≥θV/2的原h质量。

至多B_0=∏r_i≤C^k(2/θ)^(k(d+ζ))个boxes，故其中某个Q=∏Q_i⊂R有

    Σ_Q h≥c θ^(1+k(d+ζ)) V,
    (Σ_Q h)/(Σh)≥c θ^(k(d+ζ)).                    (2)

又Σ_Q h≤|Q_j|∏_(i≠j)|P_i|，所以每侧|Q_j|/|P_j|≥cθ^(1+k(d+ζ))。这是实际保原质量的几何完整乘积，不只纯density定理找一个可能没有原h的box。它不保证h在Q上恒正，也不补全原T/ST。原tube multiplicity先通过R76的M0归一到h≤1；无需给顶点加clone或扰动边界。

若另处理非uniform顶点priors，可另加不进入polynomial的label坐标并复制有理权，再取有限集合极限；ambient d与所有指数必须随之增加。当前结论不需要该扩展，不把它当原Frostman概率的免费强版本。

## 4. 原见证的固定格式编码确实合法

给每条原访问确定一个原w(T,u)∈Y_u，不对不同用途重新挑互不相容point。第三域

    P_3={(u,C_t(u),C_s(u),B_u,w):u∈Z,w∈Y_u}⊂R^13,
    W=|P_3|=Σ_u |Y_u|≈K mδ^-1.                    (3)

两端A、B补零并用固定平移/tag使三域不交，仍可在R13完成：第三域首坐标u平移1000，两端首坐标仍在[-1,1]；两端的闲置第三坐标分别置100和200。关系只读两端前两坐标和第三域存储的coefficient/B/w，不读tag或移后的u。故F任意rough、Y任意离散都可放入顶点集合，本身不使公式复杂。

取R为(1)的两个坐标各一对线性厚度不等式。其总degree≤2，四个polynomials，按FPS每个block次数D=1，按Rubin为Δ=2。所有系数值大小可含σ费用，但定理的格式计数不靠其数值有界；不凭此删除后继几何常数。该R只是几何supgraph，未声称每条edge有原T。

定义实际lifted权

    h(a,b,u,w)=M0^-1 #{T∈H*:ends=(a,b),u∈S_T,w(T,u)=w}.

有Σ_w h=g、0≤h≤1、supp h⊂R、Σh=M。固定(a,b,u)只有O(1)个δ-separated w能在Cδ误差中，故几何edge数≤C n_A n_B m。实际归一密度为

    θ_w=M/(n_A n_B W)=θ m/W≈K θδ,                 (4)

不是θ。原g的domination、同T和所有原访问均保留；这是产品分母的真实变化。

## 5. 加权定理应用到真实见证图的全部费用

对第4节R/h，(2)确适用；取d13、k3和任意固定0<ζ≤1，有几何完整box保原M至少cθ_w^(3(13+ζ))比例，各侧prior比例至少cθ_w^(1+3(13+ζ))。因此不能说此source‘完全不可用’。但θ_w约θδ，源给出的保量只有固定幂δ量级，远离所需δ^o(1)。这是现有保证的强度，单看这个下界弱并不证明所有实际配置都必损这么多；严格上界在第7–8节另证。

纯FPS D1密度结论虽给各侧≥cθ_w^14，也可能只找得到原h质量很小的完整box；若需要保量应使用第3节论证或另证质量机制。不得把纯supgraph edge数和原marks权混为一谈。编码后仍以原N及原m计账，原H*/N的δ²未自动消失。

## 6. 合法删远离anchors的第三clock

为给严格上界，取r=δ^c，0<c<1固定且η≪c。保留每T的

    S_T^far={u∈S_T:|u−t|≥r,|u−s|≥r}.

Z为δ-separated，删去至多C(r/δ+1)个原times。m≥K^-Cδ^-1、|S_T|≥K^-C m使相对删量≤K^C(r+δ)，η足小、δ随后小即可≤1/2。故对每条原T分别有|S_T^far|≥|S_T|/2；求和亦保至少M/2。这里先用逐管heavy lower，再推出平均保量，没有从平均反推所有T。

记h_far按第4节同一个原T/point分配仅删第三marks，Σ_w h_far=g_far≤1，总M_far=θ_f n_A n_B m、θ_f≥θ/2。原anchors/端点标签仍保留为坐标定义；没有重新宣删后的shading具有完整Def17 lower/coherence。原CW只继承绝对count，不在H*或新weights重归一后免费保持。

## 7. 每个完整见证box强迫一侧落细条带

取非空Q=Q_A×Q_B×Q_3⊂R，且其h_far质量>0。可把Q_3先交far clocks，不改该质量且仍完整。固定其中v0=(u0,C_t,C_s,B,w0)及a0∈Q_A、b0∈Q_B。记λ=(u0−t)/(s−t)。由R76的真实系数

    C_t=(1−λ)(F_u−F_s)(F_t−F_s)^-1,
    C_s=λ(F_t−F_u)(F_t−F_s)^-1,
    C_t/(1−λ)+C_s/λ=I.                            (5)

far使|λ|,|1−λ|≥r/2，因为|s−t|≤2。故max(||C_t||,||C_s||)≥cr。若前者大，固定b0并对a,a0用R的不等式相减，||C_t(a−a0)||∞≤Cδ。取C_t一个长度≥cr的row，Q_A落在宽ρ=C′δ/r的strip中；后者大则Q_B如此。无需最小singular value或两矩阵满秩。

现在实际用原Y的AD1 upper与Def17.3/17.4 tubeKT(δ,1−γ,K)。在δ≤ρ≤1、长O1的strip内，以O(Kρ^-(1−γ))个ρ-balls覆盖Y∩strip；每ball按AD1含≤CKρ/δ个δ点。长度O1的有界域可分固定个长度≤1 tubes。因此

    |Y∩strip|≤CK²ρ^γδ^-1,
    |Y∩strip|/|Y|≤CK³ρ^γ.                         (6)

δ最后小保证ρ≤1；norm/坐标固定常数吸C。至少一侧满足|Q_A|/n_A或|Q_B|/n_B≤CK³(δ/r)^γ。这是从完整原native输入得出的固定幂限制，不是某个弱toy的秩猜测。

## 8. 严格的原访问质量上界与box数下界

关键不是第4节稀释分母本身，而是原lifted权满足Σ_w h_far(a,b,u,w)≤1。因此无论Q_3有多少w，

    Σ_Q h_far≤|Q_A||Q_B|m
               ≤CK³(δ/r)^γ n_A n_B m,
    (Σ_Q h_far)/M_far≤CK³ θ_f^-1(δ/r)^γ.            (7)

用θ_f≥L^-1/2、L≤δ^-β，右侧≤Cδ^(γ(1−c)−β−3C0η)。先选R76小幂使β<γ(1−c)/4，再取η小，指数可≥γ(1−c)/2>0。任意B_1个完整见证boxes覆盖的原h_far质量比例至多B_1乘(7)，重叠也只会让此上界宽松。故δ^-o(1)个这样的boxes不能保固定比例；保固定比例需至少cK^-3 θ_f (r/δ)^γ个。不是仅‘现有定理下界较弱’，而是所测试完整见证编码的确有固定幂原质量费用。

另有独立的第三prior限制：固定任一(a0,b0)，Q_3在每个u仅能含O(1)个w，故|Q_3|≤Cm，除W得≤CKδ。但这项prior稀释单独不能推原marks质量必丢δ；(7)另用了native tubeKT及Σ_w h≤1。完整见证box把同一个w强加给全部端点pairs；它不同于允许w随(a,b,u)变化的原‘输出落Y_u’关系，(7)不排后者存在大的完整box。

## 9. 任意选边不能免费补全：独立通用测试

为隔离‘R可定义就令selected E完整’的错误，取两n点域，每pair独立以概率1/2保留。令q=ceil(4log2 n)。存在q×q完整子图的概率≤n^(2q)2^(-q²)≤2^(-q²/2)；边数低于n²/4由Chebyshev概率≤4/n²。n足够大时两者之和<1，故存在密度≥1/4且无此完整子图的确定图G。令E=G×Z，R为恒真的半代数关系；各active pair的S=Z完全dense，仍无两侧大小q的complete selected box。此为概率存在的精确有限命题，不是运行有限样本替代连续证明。

它不反第3节：在那里complete的是R，并可在整个R保全部E。此例也不满足完整WZ small shadow/CW/filled X等，不能冒source或Kakeya反例。若在一条有序一维slice用s个degree≤D多项式描述一个交替mask，非零多项式根总数≤sD，每根至多触发两次相邻sample符号变化；n点交替需sD≥(n−1)/2。这只表明任意mask/任意离散成员消去不继承统一格式，并非声称所有实际Y都达到该下界。

## 10. 原关系消去、合法闭包及双向排重

第三顶点只存(u,C_t,C_s,B)而要求‘存在w∈Y_u’时，任意Y_u仍在边公式内；有限并或quantifier elimination必须带入其全部description，不能凭ambient低维宣格式统一。若能证明实际Y_u存在适合原质量的低格式替代，则是另一个实质新输入，本轮未证；不能先作为公设写完后继gain。相反，F_u任意rough但存入顶点是第4节合法正用途，不把rough一概当复杂度反例。

精确半代数R对顶点restriction保同公式；任意tube restriction或每管删marks会形成任意mask，不能说selected边格式闭包。第3节却始终允许这种mask，只须原h upper与实际density重新付清。只有全局平均density时，heavy peeling可先保至少半总质量并取得逐管下界，但原N和density费用保留，不能向所有原T赠lower。

R44的共同测试degree/label/wholeclock预算与本轮定义性不同，非同一定理换名；R45 Th1.5 selected-tuple上界本已接受任意选中超图，无需提取Cartesian才能调用。因此本轮若目的仅用旧KBL，没有新准入收益。新box候选也未反向重建完整原T/CW/filled X/Φ，不能登记成原critical κ1排除的等价结果。

## 11. 主缺口、失败范围与宏观重选

本轮付清：具名regularity到任意选边权的实际正用途；原sameT见证固定格式；密度分母；每管远离anchors删选；实际AD1/tubeKT下单box原质量固定幂上界及cover数下界。没有证明不经witness编码的native output关系也须同损，更没有证明所有半代数/多尺度结构提取均失败。原普通高维、sticky全部rough与ordinary桥、严格full-direction反例四完整路线仍open。

依working停止直接witness completebox提取，不以减d/改D/ζ/θ或换‘distal regularity’名称续轮。若以后重开，须给新的原joint结构，尤其w能随端点变化而仍有可用共同作用/原质量；不能只把成功条件重写成定义性公设。主失败触发即时macro，下一轮重新完整目标选择，不自动接上一句补技术细节。

## 12. 核验和声明边界

两篇原PDF、完整提取及逐篇metadata归literature；key公式原图核，有限证明为第3、6–10节符号论证，无数值代连续。A/B互补稿及两formal全文审具体责任另存；源高级wholeproof仍具名，不混成内部已验证全定理。外部同行评审false、novelty/major false、newID0、无ordinary或完整rough分支saving。Goal active；归档/Git/sameSHA/fulltree同步另核。
