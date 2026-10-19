# R0101：半代数密度、原选边质量与见证分母

2026-10-19，A。先实际 source gate，root 锁 working5 后施工第4节以后的有限应用／反攻；不以新题名预认 Kakeya 增益。未经外部同行评审。

## 1. 实际读域、版本和原目标

实际全文读 R0101 reselection5、锁后 working5 和当前 STATE；旧 GOAL／完整 ROADMAP／registry78 与 R100 的本会话实际恢复不重跑 context。原 ordinary／HRZ、sticky 全 rough 与 ordinary 桥、真同集 full-direction 严格低维四路不缩小。

实际打开 FPS [官方 history](https://arxiv.org/abs/1502.01730) 与 [v3全文](https://arxiv.org/html/1502.01730v3)，current v3 为2016-10-14；按段读 §§1–2、4，包括 Th1.1／1.3、Veronese／cutting 的使用、齐次 product-volume 分割及 equitable refinement。实际打开 Rubin [history](https://arxiv.org/abs/2407.15518) 与 [v2全文](https://arxiv.org/html/2407.15518v2)，current v2 为2024-08-14；读完整相关定义、Th1.3／1.6 和 §5.2（Th5.1／density proof），不声已独证其全部 polynomial partition 高级 proof。没有下载新 PDF 或认证其字节。

另实际读 R44 原 polynomial-envelope 主稿、R45 selected-tuple KBL 接口及停止段、R76 主稿12节，核原 N／I、wholeclock、重复 labels 与 native 变量。随后实际全文读本轮 root12／B10、终 macro6／next6及两 spec5。本人以下有限推导不充自身独审；root／B 的独立链按第10节记实际互读。

## 2. FPS 精确关系、次数与有限不等大部

源定义要求有限点部 P_i 的 **exact** edge relation，由固定数 t 个多项式及 Boolean formula 决定；不是只给 E 包含于一个可定义关系。其 D 控制每个 vertex block 单独的次数，故总次数可到 kD。vertex sets 自身不需半代数、正则或等大，源也没有 coefficient height／condition-number 假设。

写 m=binom(d+D,d)−1，Th1.1 给每侧相对大小至少 c_(d,k,t,D) θ^(m+1) 的完整 edge product；原显示常数可写成 [2^(20km log(m+1))t^m]⁻¹。Th1.3 给 fixed k,d,t,D 下 polynomial-size equitable homogeneous regularity。§4 的中间 Th4.1 更直接控制非齐次 boxes 的总 product volume，而不只控制一个未经加权的 bad-box 数目。

因此：有限 unequal N_i 可直接进入 density theorem；空部／θ=0 无正结论，小部可取 singleton而不能暗改比例。若 t 或 D 随 physical δ 增长，常数和指数必须重算，不得因每个有限图都能用很多多项式编码便声 uniform fixed-format。Th2.4 给提取区本身可定义的版本，其区域复杂度还可依 θ，不能冒与 θ 无关。

## 3. Rubin 的正文、abstract 排字与真正 unequal 接口

Rubin 用 total degree Δ、谓词数 s 的固定类 Ψ_(d,k,Δ,s)。Th1.3 对同一 P 给同时适用于该类关系的 partition，K≤C ε^(−d−1−ζ)，ζ>0固定；它不使任意 chosen mask 自动成为该类。更尖锐 d+1 版本另需 source 的 sharpness／可扰动条件，原等式或 near-threshold数据不免费符合。

abstract 写 |Q_i|≥|P_i|/ε^(d+1+ζ)，ε小时甚至大于整个 P_i，是其字面排字；body Th1.6／§5.2 是 |Q_i|≥c ε^(d+1+ζ)|P_i|，本文只用正文正幂。初始 Th1.6 的 n-point 文字不作为只准等大部的障碍：§5.2 Th5.1 对每个各自大小的 P_i 直接作 partition，至多 C ε^(−d−ζ) 部，bad boxes 总 product size≤ε∏N_i；小部有 singleton处理。density proof 也逐个使用 |P_i|。

本轮需要的是这个 unequal product-volume statement，不需要实现其算法或以运行时间冒数学质量。hidden C 仍依 d,k,Δ,s,ζ；“exponent 与复杂度分开”不等于复杂度随 δ 任意增长无代价。

## 4. 任意原 mask 的正面 box-mass 引理

令 R⊂P₁×⋯×P_k 是 fixed-format 几何关系，N_i=|P_i|>0；0≤h≤1 支撑于 R，Σh=θ∏N_i>0，不要求 h 本身可定义。取 ε=θ/2，用 Th5.1 得 partitions Π_i，r_i=|Π_i|≤C ε^(−d−ζ)。令 V=∏N_i。

非齐次 boxes 的 h-mass≤其 product volume总和≤εV；齐次 nonedge boxes 上 h=0。因此所有齐次 edge boxes 合计保留至少 θV/2 的 **原 h** 质量，并非只保几何边数。总 box 数 B=∏r_i≤C^k ε^(−k(d+ζ))，故存在完整几何 box U₁×⋯×U_k⊂R 使

    Σ_(U₁×⋯×U_k)h ≥ c θ^[1+k(d+ζ)] V。       (1)

其占原 h-mass比例至少 c θ^[k(d+ζ)]。因 h≤1 且其他侧大小≤N_j，(1)还给每侧 |U_i|/N_i≥c θ^[1+k(d+ζ)]。θ≥δ^o(1) 且格式固定时，这些都是 subpower 损失；相关 h 不构成否定理由。

但是 (1) 不声 h=1 或 h>0 于整个 box，不给所选 edges 的 Cartesian completion，也不保原 tube 的所有 times。这正区分“几何完整且保原选边质量”和“原 selected relation 完整”。只用 Th1.1 任取一个几何 complete box 未必保原 h；以上 product-volume argument补了这一步。

## 5. 权重、重复顶点与安全的有限扩展

两源字面主要是未加权的 finite point sets；不能将大量原 label 合并而丢 multiplicity。安全扩展如下。把每个带标签的 p 嵌入 (physical coordinates, unique label height)∈R^(d+1)，所有定义多项式忽略新坐标；不同 parts 亦用不同 height ranges。精确等式仍保持，不需会改变关系的 generic perturbation。代价是 dimension d→d+1，故 density／partition 的指数必须同步替换。

对有限非负 vertex weights，先按各部总权归一。若权是有理数，把每个 p 复制为相应个 clone，原 h 在每个 clone tuple上保持原值；几何关系忽略 clone height。第4节用于 clone counting 后，将所选 clones 投影回原带标签 vertices：每个原点的全权至少其所选 clone 权，h≥0保证映回后的原 product h-mass不小，几何 completeness也保留。因原 support有限，实权用有理逼近并在有限种输出子集中取定子列，得到同一固定幂型结论。零权点可删，总权不为1时按 ∏W_i 回尺度。

这不把任意 edge weight h 变成 vertex product weight；h 的 [0,1] domination仍不可少。若只知 h≤M，应先除 M，density是 θ/M。原 tuple 法则若仅由 product reference 以 K 支配，必须付此 K。没有额外标签维度或直接 weighted版本的证明时，不保留源最尖 d+ζ 指数。

## 6. Selected completeness 的严格反攻与闭包

第4节的正面结论不能被“mask任意”粗拒，但更强 selected completion确实是假的。给三部各 n 个数字点，几何 R取全 product（固定格式）。独立以概率1/2选每个 triple 为 h=1。令 l=ceil(sqrt(8log₂n))；任一指定 l×l×l box全选中的概率2^(−l³)，总 box数≤n^(3l)，故有这种box的概率≤2^[3l log₂n−l³]→0。总选边数 X 的均值为 n³/2、方差为 n³/4；Chebyshev 给 P(X<n³/4)≤4/n³。因此 n 足大时两项坏概率和小于1，存在 density≥1/4 的 mask，却没有三个侧均≥l的完整 selected box。

它只反“dense mask继承全 selected product”，不反第4节，亦不保 Def17／真实 Kakeya全部条件。vertex restriction会保持 fixed-format 几何 R；任意 h restriction一般不保持 selected格式，但仍可在新真实 density下重用(1)。删到 θ′ 后应代 θ′，不能沿用旧 θ。

对原 tube-time 访问，保总 I_B 不自动逐管保 density。若原 H每管至少 λ₀m 个访问，box留下 I_B≥p I_H，则以 I_B/(2|H|)阈值 heavy 可保 I_B/2，每条新 heavy管至少 pλ₀m/2 个 selected times，新heavy管数至少 pλ₀|H|/2。这里平均到逐管和 retained family 两项均收费；未保每根原管全部 S_T。相对 CW／AD lower不能在重新归一后白送。

## 7. R76 增广关系真实 fixed-format，但分母改变

R76 保原 H* 的全部 S_T，并给 native y∈Y_t、y′∈Y_s、u∈Z 的 g，Σg=θ|Y_t||Y_s|m、θ≥L⁻¹，及

    Q_u(y,y′)=B_u+C_t(u)y+C_s(u)y′ ∈ N_(Cδ)Y_u。

用每条原 T 在 u 的实际 native witness w_u(T)∈Y_u，取第三顶点

    z=(u,C_t(u),C_s(u),B_u,w)，w∈Y_u。          (2)

它在 R¹³；必要时加一标签坐标至 R¹⁴。三部 padded 到同一维。定义 R 的四个 inequalities为 |(C_ty+C_sy′+B−w)_j|≤C′δ，j=1,2。用 L∞扩固定半径只改常数；它们 total degree≤2，FPS 每个 block的 degree≤1，predicate数固定。矩阵／Y_u虽 rough、系数可δ依赖，均只作为 vertex坐标；没有因为 F rough便拒绝这个关系，也没有暗加 s_min lower。原σ费用可能影响几何后继，不影响这项 fixed-format资格。

以 M₀⁻¹计同一原T、实际w和u的访问构 h(y,y′,z)，则0≤h≤1、支撑R，且 Σ_w h=g。没有重选非原witness，也没伪造几何边为原tube。第三部大小

    M₃=Σ_(u∈Z)|Y_u| ∈[K⁻¹δ⁻¹m,Kδ⁻¹m]，
    θ_aug=(Σh)/(|Y_t||Y_s|M₃)=θ m/M₃ ≍_K θδ。  (3)

因此真实格式可用，但原 near-full θ 变成含固定δ幂的 density。若消去 w 而写 Q_u(y,y′)∈N_(Cδ)Y_u，任意有限 Y_u 的成员关系不因此得到与 |Y_u|无关的 fixed-format；QE只对已给定复杂度的公式工作，不免费删除对每个w的并集成本。

## 8. Witness box 的第三边际与额外原质量上界

设 A×B×U 是(2)关系的一个非空完整几何 box。固定任一 y₀∈A、y′₀∈B；同一个 u 的所有 z∈U，其 w 必须落在 Q_u(y₀,y′₀) 的 C′δ球。Y_u δ-separated，故每 u至多 q₀=O(1)个w。因此

    |U|≤q₀m，   |U|/M₃≤q₀Kδ。                  (4)

这是实际上界，不只是某个 theorem保证太弱。但它只对增广第三部的 product-reference比例，不证明原 h-mass必损δ；全部 selected mass可能本来每 u就用同一个w。投影 U到clock也可能保全部u，不能从(4)推 |proj_u U|≪m。

将 (3) 代(1)时，所得保留保证只为 (θδ/K) 的固定高次幂，不能读成原每侧 δ^o(1)／原I的大比例。FPS或Rubin更好的固定 exponent、clone weights或不同 part基数都不自动消掉这个实际 witness域分母。不过(4)本身没有证明原质量损失；本轮 root§6–8／B§6–7另从真实原 tube-KT 给出了如下更强结论，已实际全文独核。

取 r=δ^c，0<c<1，删去 |u−t|<r 或 |u−s|<r 的原 visits。Z 的 δ分离和各 T 原 |S_T|≥K^−C m、m≥K^−Cδ^−1，使各管相对删量≤K^C(r+δ)；η相对c足小、δ最后小，故逐管保一半，亦保总 M_f≥M/2。仍有 Σ_w h_f=g_f≤1。对承载正 h_f质量的完整 box，可先把第三部交 far clocks；固定其一个 u，λ=(u−t)/(s−t) 满足 |λ|,|1−λ|≥r/2，并有精确恒等式

    C_t/(1−λ)+C_s/λ=I₂。

因此 max(||C_t||,||C_s||)≥cr。固定另一端与该第三 witness，至少一端全部落在宽 a=Cδ/r、长 O(1) 的 strip。原 native Y 的 tube-KT(δ,1−γ,K) 给该 strip 内 a-cover≤CKa^−(1−γ)，AD1 upper 给每 a-ball至多 CKa/δ 点；除原 |Y|≥K^−1δ^−1后，该端比例≤CK³a^γ。用 Σ_w h_f≤1 消掉 witness重数，即得

    h_f(box)/M_f ≤ CK³ θ^−1(δ/r)^γ。             (5)

若 θ≥L^−1、L≤δ^−β，先取 β<γ(1−c)/4，再取η足小，(5)是固定正幂δ。任意 δ^−o(1)个完整 witness boxes合计也不能保固定比例原 h_f；重叠求和只会放宽这个 upper。这里无需最小奇异值／goodrank，且 a≥δ未用 sub-δ KT。它是额外原输入下真正的质量限制，不能再写“本轮尚未证明”。其范围仍只限同一第三 w适用于全部端点对的完整见证box；w随端点变化的原输出关系、所有其他几何方法及 fullsource本身未被否定。

## 9. R44–45 排重和完整源的责任

R44已在原 used visits上付共同 tests／whole-index选择，但 affine或polynomial包络的真实体积、degree、piece重数回到原 CW；本次density theorem没有无费降低这些 common tests 的 complexity或 jointpalette。R45 §4 的 Kakeya–BL Th1.5推论已经可直接控制任意 selected hypergraph tuples，不需要先找 Cartesian子族。真正未付的是 good-BL／rank质量，且固定臂计数有自己的κ阈值；“先半代数补全所以现在KBL合法”不是新输入。

本次(1)是一个真实可调用的保原mask几何box工具，不等价于完整Kakeya正幂，也没有反向从抽象box/h恢复原 Def17 的 full CW、filled X、Φ与selected ξ。把几何 supgraph完整当 selected完整，或把δ²原全T的单block当subpower全族，均仍非法。对(2)关系的 box施原source后继还要面对(3)–(4)及原CW重归一；不能添 wanted goodrank／irreducibility来完成。

## 10. 当前判定、实际审查与停止

已付不同层次结论：fixed-format几何 R 上任意 bounded mask确有保原mass的完整几何box，第4–5节给原权／重复标签资格；真实 R76 witness编码确实 fixed-format，却引入 θ_aug≈_Kθδ。第三边际上界本身不是质量上界，但第8节另用 far clock／原tube-KT／Σ_w h≤1，确证单完整见证box保原质量的固定幂上界及 subpower数量不足。随机mask只反 selected completion，不反第一个正用途；这项 actual mass upper亦不升级为所有原几何利用或fullsource反例。

原 κ1完整分支／ordinary／HRZ／Hausdorff和真低维反例均未解。按 working停止把“g本身bounded-format”、无费QE、相同density重用或完整selectedproduct当新公设；没有新ID／major／novelty声明。实际全文独核 root12／B10：第4–8节原几何编码、逐管删选、端点strip、单box质量及全部原分母均通过；B§5 sampled真假交替的根数下界原漏1/2，已通知并实际修为每根至多两次变化，root§9原即正确。两spec5／终macro6／next6已实际全文读，冻结与四完整路边界一致。本人有限证明不计自身独审，其独立审查由root／B承担。高级定理仍具名，未经外部同行评审，不预认证元数据、下载或Git。
