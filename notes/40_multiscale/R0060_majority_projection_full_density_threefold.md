# R0060：大多数投影支付一般三维颗粒的全密度立方估计

2026-10-17开轮，跨午夜至2026-10-18。root整合。先周期macro及HRZ真实价值核验，working_spec§7锁定新机制后施工。本稿使用明确具名的外部深层定理；其wholeproof没有由本项目独立认证。未经外部同行评审，不认证首创/重大性或ordinary高维Kakeya完成。

## 1. 完整结论和不可删除的假设

固定n≥4、R,C≥1、半代数格式A及ε>0。存在c,δ0>0只依这些固定量，使任意0<δ<δ0满足下述命题。S=Sδ⊂B_R⊂R^n为格式≤A、实半代数维数≤3的集合，系数可任意依δ，允许奇点、低维层及非闭集合。T_i是N根原unitδ-tubes，物理方向δ-separated，**每根整单位轴都在N_(Cδ)S内**。Y_i⊂T_i是任意Lebesgue可测集合，令

    E=∪Y_i， λ=Σ|Y_i|/Σ|T_i|∈(0,1]。

则常数独立λ，并且

    |E|≥c δ^(n−1+ε) λ³N。                         (1)

同一结论的已审all-subfamily闭包给任意原非负权w_i，总W>0、每个C0δ方向帽权≤α、λ=Σw_i|Y_i|/(Vδ W)时，其中Vδ=|unitδ-tube|为共同**实际**体积、Vδ≈δ^(n−1)，允许round端帽的δ依赖常数，

    |E|≥c δ^(n−1+ε) λ³W/α，                       (2)

常数另依固定C0。这关闭R55完整G3（n=5）而不只nearfull区。R59“仅Yi近S”的更宽支撑类不能在这里免费替换整轴条件。普通高维全部管没有这种三维载体；本文未证明新ordinary Hausdorff下界。

## 2. 实际具名输入与独立证明范围

输入KR：Katz–Rogers1802.09094v3 Th1.1。固定σ>0与半代数格式B，原unitδ方向分离管满足

    #{i:|T_i∩H|≥a|T_i|}≤C δ^(1−n−σ)|H|a^(−n)，a≥δ。

本轮最终只查询固定a=1/2，而非阴影密度λ。

输入OAI3-critical：已存OpenAI2026-09-23三维稿，Definition2.3、Lemma2.6及Proposition10.1。存在p>2任意接近2，使h(p,0)=0。它对全部bounded-matrix **weighted indexed** affine graphs及uniform temporal profiles断言m≤exp N^(pF(1))Δ0，其中Δ0=sup_B n_B/(ab)，B是full-time planks、1≤a≤b≤N。重复参数允许，权保持，δ方向分离不是此临界结论的假设。本文不能只由方向分离的headline Theorem1.1跳到这个更宽输入。

输入Paw：作者2007稿Prop1/Theorem3_m及其任意实闭域适用性；标准半代数光滑分层、有限-to-one CAD与QE。R59已付regular-cell/globalLip与RCF固定格式一致性。本轮在同一π下补选good strata，下面解释低维层为何保π。

实际读取OAI3 PDF6–10、86的Prop10.1声明及90–94归约；非97页wholeproof审定或Lean重跑。KR/Paw也仍是具名定理输入。本文自证的桥是§§3–10及权闭包，最终由互补代理逐步独审；来源署名不是正确性保证。

## 3. 从指数式临界结论到有限保Δ0不等式

固定上述一个p与ξ>0。对任意有限weighted indexed affine图、N个时间bins、每个index/time至多一次mark，记W=Σw_i、I=Σw_i|S_i|、λ_d=I/(NW)、E_d为真实trace事件cells。则

    #E_d≥c_(p,ξ) N^(−ξ) λ_d^(p+1) N W/Δ0。        (3)

空图按0处理，Δ0>0时才非平凡。常数不依#index或权跨度。证明如下。先删|S_i|<I/(2W)的indices，仅损I/2；剩余mark数分O(logN)个二进层，选保事件质量≥cI/logN的一层，再把每index截到同一整数k，仍保常数比例。该k≥cλ_d N，层总权W0满足kW0≥I N^−o(1)。

若(3)对某ξ无统一常数，取违反序列。N有界不能导致此事：共同widestplank包含全部bounded traces，Δ0≥cW/N²，m=I/#E_d≤NW，故比值至多C N³。于是N→∞。上一步得到的同k图再用Lemma2.6保subpower事件质量并取uniform profile。active权≤W0、每index mark≤k及总事件≥kW0N^−o(1)，迫最终每index mark=kN^−o(1)，因此N^(1−F(1))=exp k。

最终m′≥mN^−o(1)，Δ0′≤Δ0（只删events/indices、保权）；临界输入给m′≤(N/k)^p N^o(1)Δ0≤λ_d^−p N^o(1)Δ0，与违反m>N^ξ λ_d^−p Δ0矛盾。没有把原平均mark数免费称原逐管下界，也没有对权重作dyadic分层。

## 4. 共同随机格：任意Lebesgue阴影的连续转移

设P_i是R³共同有界区域内的unit r-tubes，任意有限正权w_i，W=Σw_i，定义**绝对**

    D=sup_(convex U) [Σ_(P_i⊂U) w_i|P_i|]/|U|。

重复tube逐index计权。任意可测Z_i⊂P_i，E3=∪Z_i，λ3=Σw_i|Z_i|/(V_r W)，V_r=|P_i|≈r²为共同实际体积。先分固定数方向charts并选incidence大者，W只减、D只减；故可在一个bounded-slope graph chart证明。共同bounded clock经固定仿射归一至[0,1]，只延长模型支持线、不移动原Z_i。选择dyadic N使h=1/N≈r，取共同shift ξ∈[0,h)^3的格Gξ=hZ³+ξ。

共同clock先取固定padding，使全部原P_i和Z_i落其内部固定margin；归一后ξ_t的相位吸入intercept、ξ_space作为共同空间平移，模型事件恰位于source bins的centers。故N层足以包含全部实际格点，没有漏掉首末边层，也不把原端帽质量映成单时刻。

对每个i在每个clock层t_j统计Z_i∩Gξ中的点。横截面半径O(r)，每层至多固定C个格点，按固定字典序分成C个slot；slot视为同一原轴、相同原权的重复index，每slot/time至多一个mark。空slot删去。总slot权Wξ≤CW。每个实际格点离其原支持线O(h)，故exact支持线事件cells的union至多C倍 #(E3∩Gξ)，而事件质量恰为

    Iξ=Σ_i w_i #(Z_i∩Gξ)。

whole-time plank含slot支持线⇒原实体P_i含于固定倍加宽plank，后者凸、体积≤C h²ab；由于a,b≥1，厚度加O(h)仅常数费。故slot的Δ0≤CD，计入所有重复slot。时间shift吸入共同intercept，trace仍在固定bounded matrix chart；不把端帽体积clamp到轴端点。用含端帽的固定共同clock即可。

逐ξ用(3)，并以Wξ≤CW，得到

    #(E3∩Gξ)≥c h^(p+ξ0) Iξ^(p+1)/(D W^p)。         (4)

空图平凡。所有集合/计数为Lebesgue可测，有限bounded图不存在无穷求和问题。对共同shift积分的准确恒等式是

    Eξ #(E3∩Gξ)=h^(−3)|E3|，
    Eξ Iξ=h^(−3)Σw_i|Z_i|。

Jensen代入(4)给

    |E3|≥c r^(2+ξ0) λ3^(p+1) W/D。                (5)

这没有以所有“与E相交的r-cubes”填满原E；使用的是随机格**落在真实E里的点**。没有取h≪r造成不受控h^−ξ，也没有对每个index独立抽空间prior。

## 5. 全密度立方absolute-CW结论

对每个a>0可先从Prop10.1选p−2<a/4，再取ξ0<a/4。若λ3≥r，则λ3^(p−2)≥r^(p−2)，(5)给

    |E3|≥c r^(2+a) λ3³W/D。                       (6)

若0<λ3<r，因共同bounded凸球包含全部P_i，D≥c r²W；同时trivial |E3|≥Σw_i|Z_i|/W=V_r λ3≥c r²λ3。于是(6)也成立：其右边≤C r^a λ3³≤C r²λ3。常数统一吸收，bounded r区间亦可粗估。

故(6)对任意indexed positive weights、arbitrary measurable shadings及全部λ成立，D没有先授smallness；缩放全部权使W,D同步变化。原tube长度为任意固定L0也可经固定homothety使用同结论。此是具名强临界结论的应用，不以它宣一般3D深层证明已由本项目认证。

## 6. 固定大多数良好投影的存在

固定e0<1/16。存在τ>0及固定有限等权正交投影π_j:R^n→R³，j=1,…,J，仅依n,e0，使对每个m≤3平面V，至少(1−e0)J个j满足smin(π_j|V)≥τ。m=0全为good。

证明：Haar随机3-plane的投影在固定m≤3平面上几乎必injective。由旋转不变性，坏概率只依m，且当τ↓0时P{smin<2τ}→0，统一选m=1,2,3使其<e0/4。取连续cutoff ψ(s)，在s≤τ为0、s≥2τ为1。其Haar均值≥1−e0/4。Grassmann各m空间及投影参数空间紧，ψ(smin)一致连续。取有限V-net，再按有限次大数律选一个等权投影样本，使net上平均误差<e0/4；取net足够细使所有V误差再<e0/4。于是所有V的样本平均≥1−e0，且ψ≤1_(smin≥τ)，给结论。这是一次固定的确定性存在选择，不依δ、S、T或Y。

## 7. 同一π的good层、全局图形与点wise覆盖

将S按固定格式C¹半代数strata M分层。对每π_j，仅取G_j={x∈M:smin(π_j|T_xM)≥τ}之并。它们仍固定格式。每个S点按自己所在stratum的切空间使用§6，故属于至少(1−e0)J个G_j。

每个G_j可由有限个**同π_j**上的global L-Lipschitz半代数graphs闭包覆盖，piece数、L、格式只依n,A,τ。具体：若stratum维m≤3，π_j在其切空间有统一逆界。在π_j目标R³里再选m个坐标minor，Cauchy–Binet给统一逆界；finite-to-one CAD在open R^m域上给C¹图，所有剩余坐标梯度有界。Paw regularcells把梯度界转globalLip。残余lowerdim部分重新stratify，切空间在原stratum切空间内，所以同π_j的τ-bound仍保；维数递降至0。补回π_j目标中未选坐标，normal函数相对完整π_j距离仍globalLip。这里不另选ambient投影，所以保多数指标j。

uniform piece数/格式由R59同一RCF compactness/QE理由付出，允许δ系数；闭包延Lip且保格式。令H_j为这些graph闭包的N_(C+2)δ邻域之并。每个normal fiber有

    |H_j∩π_j^−1(z)|_(n−3)≤M δ^(n−3)。              (7)

有限union仅改变M。对任意q∈N_(C+1)δ S，任选一个足够近p∈S，p属于至少(1−e0)J个G_j，故q也落在至少这么多个H_j。非闭S可用严格稍大C+2取近点。**不需一个可测最近点选择**，这是逐点的计数命题。

## 8. 同时保整管与任意原阴影，支付非短投影

整轴近S使Ti⊂N_(C+1)δS。将上一逐点坏比例分别在Ti与Yi积分：其平均相对坏体积均≤e0。Markov说明坏体积>1/2的j各不超过2e0J；因4e0<1，对每个非零Yi可选同一j(i)，使

    |Ti∩H_j(i)|≥|Ti|/2， |Yi∩H_j(i)|≥|Yi|/2。      (8)

注意H_j是同π的多图union，不要求整Ti或Yi在单一图上。将indices按j以及下述有限投影方向chart分区，选一组使实际I_j=Σ|Yi∩H_j|≥c I，I=Σ|Yi|；令其原label数N_j≤N。没有heavy density过滤或λ的label损失。

由(7)，

    |Ti∩H_j|≤Mδ^(n−3)|π_j Ti|
             ≤C Mδ^(n−1)(|π_j v_i|+δ)。

与(8)比较，δ足小给|π_j v_i|≥c_M>0。故非短投影由整管常数体积支付，完全独立Yi的密度或时间形状。端帽的投影是δ-neighborhood projected segment，上式已包含δ³端项。

## 9. 原常数占比PW传indexed absolute凸浓集

在一个投影方向chart内，以主坐标平面x_k=0处的交点pin中心，把原投影支持线延为固定长度L0、固定半径Aδ的三维包络P_i，覆盖π_j Ti。所有包络在共同bounded区域内，共同实际体积|P_i|=V_P(δ)≈δ²；保持每个原index，**不去重**，不添加纵向网格labels。临界indexed输入允许重复。

若P_i⊂凸U，则Ti∩H_j⊂H_j∩π_j^−1(U)，并由(8)有原Ti一半体积证据。对有限体积U用John外接box Q_U⊃U、|Q_U|≤C|U|，测试H=H_j∩π_j^−1(Q_U)统一格式，(7)给|H|≤Cδ^(n−3)|U|。KR以固定a=1/2查询：

    #{原i:P_i⊂U}≤C δ^(−2−σ)|U|，
    D(P indexed)≤Cδ^(−σ)。                         (9)

无管/无限体积U平凡。原midpoints在共同bounded区域，若KR规范要求B2，可先按固定数小box分原midpoints并仅平移，各box的完整unitδ管落B2内；总计数只付固定常数，不缩原unitclock。所有原重复labels均计入(9)，不用假投影方向分离，不出现λ^−n；这正是R59单个shadechart选择尚没有支付的wholeT/Y兼容信息。

## 10. 所有level积分：没有额外阴影密度费

在未缩放的正交π_j frame令E_j=E∩H_j，

    f(z)=δ^(−(n−3))∫_(π_j^−1(z))1_Ej， 0≤f≤M。

Fubini给Σ∫P_i f≥δ^(−(n−3)) I_j。对0<t<M，令F_t={f>t}、Z_i,t=P_i∩F_t，Λ(t)=Σ|Z_i,t|/(N_j V_P(δ))。由(6)及(9)，

    |F_t|≥c δ^(2+a+σ) N_j Λ(t)³。

由于这些是真实f的levels，layercake及Jensen给

    ∫_0^M Λ(t)dt≥c I_j/(δ^(n−1)N_j)，
    |E|≥δ^(n−3)∫f
       ≥c δ^(n−1+a+σ) N_j [I_j/(δ^(n−1)N_j)]³
       ≥c δ^(n−1+a+σ) N λ³。                      (10)

最后用I_j≥cI、N_j≤N。这里不选一个t≈λ后再额外乘λ，而是积分全部levels。f的fiber upper只用于构造和有界积分区间，没有倒推fake fiber lower。空间同一frame，调用固定长度版(6)仅隐含共同固定homothety，其Jacobian已在常数内；没有混用变化后的π。

先取a,σ>0且a+σ<ε，再选(6)中的p,ξ0，δ0最后取吸收固定常数。(10)得到(1)，全部λ统一。

## 11. 任意原权和方向帽的合法闭包

将原方向按细δ bins及有限邻接着色，兼顾antipodal charts；单色不同bins中的任意原代表无向角δ分离。每bin原权≤Cα，选一色保I_c≥cI，W_c≤W。每bin独立以w_i/(Cα)概率选一个原index i，其余概率为空；每次样本是(1)的合法原子族，shadings仍为原Yi。

对每个样本，令I_s=Σ_selected |Yi|、N_s为index数；(1)写成|E|≥cδ^(n−1+ε)I_s³/[Vδ³N_s²]，空样本记0。取期望并用Holder：

    E[I_s³/N_s²]≥(E I_s)³/(E N_s)²
                  =c I_c³/(α W_c²)≥c I³/(αW²)。

即得(2)。没有权跨度log，也不为每个direction bin移动原tube或换几何代表。平均与逐管全λ版本属原合法闭包，不新起名字或数学ID。进一步任意shading restriction仍须重算I和λ。

## 12. 同证明PW范围及真实递推的费用

若原indexed族（可带权）已独立对本文固定格式半代数test满足absolute计数Σ_(|Ti∩H|≥|Ti|/2) w_i≤Kp δ^(1−n)|H|，则(9)变D≤C Kp，同一证明给

    |E|≥c δ^(n−1+a) λ³ W/Kp。

这是同一证明的输入范围，不另命名结果。KR的Kp=Cσδ^−σ恢复(1)；不免费授予任意族PW。HRZ局部长ρ归一时Kp可真达ρ^(−(n−1))δ^−σ，本文不会使该费用消失。旧wholebroad选法也不自动保原marks。因此全G3闭合不等于ordinary高维递推已取得fixed gain。

## 13. 旧反攻、文献比对和未经证明的范围

R55 regular product-parabola例只否有限global投影的angular cap；本轮不使用它，使用indexed joint convex cap且保原重复。多数π也不是选一个π使所有点都good：允许少量坏点，再同时对Ti/Yi积分。正是允许sameπ多graph union才兼容whole占比和任意shading。

bounded primary比对涉及Choudhuri§4 codim1 wholeunion原型、KR、Zahl Gromov多尺度计数、Di Plinio–Parissis方向variety L²与OAI3 strong critical indexed输入；不能把有限搜索当无先例/最优证明。未认证novelty或major。源OAI3完整97页深层证明是具名条件，不因OpenAI署名自动认证。

本文不解决四维颗粒、任意一般载体、高维general→sticky初始化、mixed矩阵分支或ordinary n≥5 Kakeya/Hausdorff。R59仅Yi近S范围在全部小λ时不能自动扩大为本立方定理。无新ordinary界，Goal active。

## 14. 独审与停止

A提出并逐步证多数投影/同π图形与wholeT/Y；B独立反攻并证明finite critical及randomgrid/Lebesgue连续转移，root整合全部层积分及原权闭包。最终formal需实际全文读root/A/B/macro/next，不以各自自审代独审。归档测试只核引用/原件/JSON，不代数学。

停止本轮多数投影/slot/端帽常数微调。下一应评估全G3新闭合对真实高维几何的新增责任，尤其m4或不同完整机制；不能再次仅重复HRZ数值或给未证leaf添PW公设。归档同步后Goal仍active。
