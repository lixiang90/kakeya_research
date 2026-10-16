# R0022：原 observed A/B 图、粗化权重与 fixed-ρ ABC 接口

2026-10-17，`audit_four_dimensional`。已读本轮 working spec、R21 next target、GOAL/STATE/ROADMAP/registry、AGENTS，以及 WZ arXiv:2609.22035v1 Definitions17.2–17.4、§19.1–19.2、§21.1；重新渲染原 PDF91、92页核对公式。只研究 LOCAL-AFF 的 source 接口，不重开 PCT 或旧冻结路线。

**审计结论：** 原 A 确有可支付的每个 coarse-x fibre cap；它不必是真正的全局 Lipschitz 图，也不需要这个额外性质。原 W 权可经明确的恢复上界、时间 heavy-cell 删除和聚合，送入均匀 coarse frame 中的 bounded graph。固定ρ的这段证明仅使用同一窗口的 affine nonconcentration；regularity/coherence仍查询ρ²及其他子尺度。(151)到(170)有可反射修复的vertical符号错配，印刷(172)另有可同步缩放修复的anisotropic normalization错配。scalarization本身与全局 time-restriction 闭包由本轮其他稿另付，本文不以 Remark21.3 的一行 generic projection 代替。

## 1. 原文定位与被审量词

本库全文行号使用文本以换行符`\n`切分，保留form-feed：

| 输入 | PDF页 | 文本行 |
| --- | --- | --- |
| 原Z、dyadic Lip、跨时间Y-union、ξ/Φ coherence | 65 | 3362–3381 |
| W定义、原路径计数与向量恒等式 | 76–78 | 4033–4122 |
| low-variation Lemma19.2 | 78–80 | 4124–4241 |
| Lemma21.1的all-scale印刷声明 | 90 | 4751–4758 |
| scalar ABC Theorem21.2 | 91 | 4780–4837 |
| Remark21.3 | 92 | 4840–4842 |
| observed A、(170)、A-cover、B、(171)/(172) | 92 | 4844–4901 |
| dense graph、(173)、二维投影与ABC调用 | 93 | 4904–4916 |

实际本轮 d5/ℓ2 的 observed 坐标为 `(x,ξ)∈R×R³`，B坐标为 `(t,F(t))∈R×R³`；Φ仍是标量。本文K表示δ的固定小幂，允许吸收有限维、allowed-grid取整和合法time删选的费用。须先固定µ、κ、所需nonfit指数，再令原η及其他损失足够小。

## 2. A的真实 fibre cap，而非额外Lip假设

原92页定义固定终层z、grain标签y，取厚度σ=Cρ²：

    A_phys={ (x',ξ_p') : p'=(x',y'+f(z)x',z)∈E(q),
                              |y'−y|≤Cρ² }.

固定一个x的ρ²-cell时，所有相关p'落在O(1)个物理C'ρ²-cubes：f有界，z已固定，且y'只动O(ρ²)。每个物理cube由原Def17.2(4)的ξ-coherence控制。若C'ρ²非allowed，向上取最近allowed尺度w，满足`C'ρ²≤w≤δ^(−Cη)ρ²`；逐维覆盖/packing后，每个x-cell至多K个joint `(x,ξ)` 的ρ²-cells。因此

    N_(ρ²)(A_phys∩{x∈I_(ρ²)})≤K,
    N_(ρ²)(A_phys)≤Kρ⁻¹.                    (1)

这里x在q内只占O(ρ)区间。若终层厚邻域因(152)需放大至Kρ²，仍仅多付K固定幂。原文4866–4868“固定x就固定ξ”的字面说法过强；证明所需是(1)的coarse纤维上界，已经足够。

不能由(1)断言存在单值的全局Euclidean-Lipschitz ξ(x)。厚grain包含不同y'，同一个exact x也可有多个ξ；dyadic coherence还不提供跨所有dyadic边界的Euclidean Lip延拓。后续ABC对A没有Lip要求，因此不必补这个更强命题。

将x、ξ作第4节的同步归一后，在mesh r≈Kρ上仍有每个x-r-cell≤K个A-cells。对任何有界λ，`Π_λ(x,ξ)=(x,λ·ξ)`保持第一坐标；一个二维r-ball的preimage只遇O(1)个x-r-cells，所以

    K⁻¹N_r(A)≤N_(Cr)(Π_λ A)≤C N_r(A).      (2)

固定C的mesh差与端帽可由有限覆盖吸收。这个cardinality保留对所有有界λ成立，不用随机投影、A的AD-lower或全局Lip。projection后的同cell聚合重数至多K，故原coupled graph也只损K；不能直接把原各点映成独立均匀prior。

## 3. 原W权到 observed bounded graph：恢复表

采用R16原incidence证明取得的合法good-q，而非声称任意q都有局部lower。记m=#Z(q)、e=#E(q)，d5中

    m≥K⁻¹ρ/δ,
    e≈K^(±1)m(ρ/δ)^(4−κ),
    #T(q)≤Kρ⁻κ(ρ/δ)^4.

每个原fine Φ_p-bin取一个实际witness，O(1)碰撞；selected对象只保ambient upper，不重置AD-lower。原W路径CS给

    #W≥K⁻¹e δ⁻⁴κρ^κm².                    (3)

这是实际每条tuple权1的总数，不要求每条管在q内有m个marks。按第一终端的z''与y''的σ-cell Q分桶，σ=ρ²。单层至多`K(ρ/σ)^(3−κ)`个桶；第一终端原点上界是`M_Q=K(ρ/δ)(σ/δ)^(3−κ)`。固定原第一终端u时，反向逐选T₁'、z₂、T₁、z₁、T₂、ρ-close的T₂'，其原W重数至多`Kδ⁻⁴κρ^κm²`。因此删除`e_Q<K⁻B M_Q`的轻桶，只损K^(C−B)比例的原W。剩余桶按W_Q/e_Q平均，可选同一桶满足

    e_Q≥K⁻¹(ρ/δ)(σ/δ)^(3−κ),
    W_Q≥K⁻¹e_Qδ⁻⁴κρ^κm².

每个joint σ-cell的原点upper为`K(σ/δ)^(4−κ)`，故桶的A-support下界是`K⁻¹ρ/σ=K⁻¹ρ⁻¹`，与(1)的upper配合。单桶保留全局W的比例可能是`K⁻¹/[m(ρ/σ)^(3−κ)]`，本文不把它称为全局K⁻¹质量。这里只须在桶自身的原frame中保dense graph。

给定code `(a_(ρ²),z₁,z₂,φ₁_ρ,φ₂_ρ)`，固定z''、Q；a是第一终端的实际joint cell。每个code的原W恢复上界为

| 原选择 | 个数upper |
| --- | --- |
| 第一终端p₁''在其x-cell和厚y桶中 | K(σ/δ)^(4−κ) |
| 其原末管T₁'及z₂处交点 | Kδ⁻κ，交点仅O(1) |
| T₁在给定coarse φ₁-bin；z₁处起点 | K(ρ/δ)^κ，交点仅O(1) |
| T₂在给定coarse φ₂-bin；z₂处点 | K(ρ/δ)^κ，交点仅O(1) |
| 与T₁'方向ρ-close的T₂'；z''处终点 | K(ρ/δ)^κ，交点仅O(1) |

故

    M_code≤K(σ/δ)^(4−κ)δ⁻⁴κρ^(3κ).

定义g为该code的原路径数除此upper，得到0≤g≤1。利用(3)、厚桶选择和`#A≈K^(±1)ρ⁻¹、#Φ_q≈K^(±1)ρ⁻κ`，其在同一个

    A × Z(q) × Z(q) × Φ_q × Φ_q

均匀reference frame上的mean≥K⁻¹。输出A取固定倍厚桶的扩大版本；其cardinality与input A只差K，所以可把两者并成一个A，密度仍只损K。未将原路径law假定为上述product law；所有原相关性仍由g承载。

按(151)/(152)，每个正权code满足真实增量`(z₂−z₁,f(z₁)−f(z₂))(φ₂−φ₁)+O(Kρ²)`，与印刷(170)的vertical符号差异在下节处理。coarse φ的误差为O(Kρ²)，并且两个终层grain标签仅需相距O(Kρ²)，不必落同一个exact grain。这些费用已经进M_code、A的厚化和下节误差。

## 4. 印刷(170)/(172)的反射与同步归一修复

原PDF78的(149)/(151)逐步给`Δξ=(f(z₁)−f(z₂))Δφ+O(Kρ²)`、`Δx=(z₂−z₁)Δφ+O(ρ²)`；而PDF92的(170)将vertical block印为`f(z₂)−f(z₁)`。两页均已渲染核对。因此先反射observed ξ-block，或等价地把B的F改成−F，才能与真实原路径一致。反射不改变first coordinate、cover、tube cap或原质量。

PDF92已渲染确认：原F分母为`δ⁻ηρ`，但A定义的ξ坐标仍以ρ缩放；随后的(172)将两者当同一缩放。按其字面定义，(170)的增量实际是`diag(1,δ⁻η I)(b₂−b₁)(φ₂−φ₁)`，并非印刷(172)。这是局部normalization错配，不是PDF提取错误，也不是主定理反例。

保守修复取`1≤L_f≤K`，足以控制原f振幅及q内ξ振幅；同步定义

    a=((x−x₀)/ρ, −(ξ−ξ₀)/(L_fρ)),
    b=((z−z₀)/ρ, (f(z)−f(z₀))/(L_fρ)).

两者在固定bounded box，真实(151)正确变为

    a'=a+(b₂−b₁)(φ₂−φ₁)+O(Kρ).             (4)

这是同一个anisotropic线性map作用于观察量及增量，不能只缩B。A的observable-x保持，(1)/(2)不受破坏。可以令working mesh `r=C K₀ρ`吸收明确误差，其中K₀为已选固定小幂；下面K继续容纳其有限次幂。由η足够小于µ，r仍趋0，且log r/logδ与logρ/logδ只差小量。Φ也在该mesh重分箱，κ-AD给每个image cell至多K个原ρ-cells；cardinality、regularity与graph只损K。

## 5. fine times→coarse B：upper与lower capacity都要付

原细时间spacing是δ/ρ，不是r。B先取原fine graph `(t,F(t))`，按r-cells聚合。一个time-cell可遇O(1)个相邻allowed dyadic time-cells；只在每个子片内用原dyadic Lip，再合并K个vertical clusters。无需跨dyadic边界的Euclidean Lip。原time packing与此局部cover在物理尺度rρ（allowed向上取整）给：

    每个coarse B-cell含原times数 n_b≤P,
    P=K rρ/δ;
    每个coarse time-r-cell至多K个B-cells;
    #B_c≤K/r,   m/P≥K⁻¹/r.                 (5)

对g的两个time fibres求和后除P²，可得coarse frame上的0≤g_c≤1；由m/P及#B_c的upper，mean仍≥K⁻C。A、Φ的聚合仅增加K次数。由于first time坐标，B_c还保cover ball cap及cardinality≥K⁻C/r。

**但(5)的upper capacity单独不能传递uniform B_c的tube非集中。** 某个fit可在很多coarse cells各取一个fine time，fine质量虽小，coarse cardinal却大；这是必须支付的接口。

删掉`n_b<P K^(−B)`的light B-cells。其原fine time质量至多

    (#B_c)P K^(−B)≤K^(C−B)m.

因为原g≤1，两个time坐标上被删的coupled graph质量也至多这个reference质量的两倍。先把固定B选大于原graph密度loss常数，保mean≥K⁻C。剩余carrier满足

    P K^(−B)≤n_b≤P,
    K⁻C/r≤#B_h≤K/r.                         (6)

这时任意粗Euclidean tube中的uniform coarse cardinal，可用其Cr增厚tube对应的原fine数量除以`P K^(−B)`，从而只损K的固定幂地继承nonconcentration。对affine band单独转移时，误差是`C(1+|R|)r`，不能无条件忽略任意大斜率；可先用下节的Euclidean tube cap，或由richness/time-gap另控斜率。B_h的(r,1,K)性质由first time坐标、每time cell≤K个B-cells和cardinality lower得到。这是合法heavy-cell选择，不是把原weights免费改成均匀weights；原正权路径关系仍由coarse g保留。

第2节的time-preserving投影也只以K重数合并B-cells。投影后的first time坐标仍在，可用同样的bounded聚合和heavy筛选；不能仅从投影support的大小推出原coupled density。

## 6. fixed-ρ nonfit如何变成B的tube cap

在一个合法good-q所在窗口中，假设原whole f对任意向量R,U的ρ^(1+ε₀)-fit最多占a比例原times；用m lower相对原window计数换算只多付K。对normalized F，相应band宽为

    h=ρ^ε₀/L_f.

取vector B的tube宽`w=ρ^(4ε₀)`。若tube单位轴的time分量≥√w，则tube中的点满足某个vector affine band，误差≤C√w≤h，故原time质量≤Ka。若轴的time分量<√w，则整个tube的time投影长度≤C√w，原time packing给质量≤K(√w+δ/ρ)。因此

    fine-time mass(B∩tube_w)≤K[a+ρ^(2ε₀)+δ/ρ].             (7)

把coarsening误差O(Kr)计入w，且r≪w；同一推导容许w乘K的固定幂，因而也覆盖working mesh所需的`r^(4ε₀)`。再经(6)，uniform coarse B_h也仅多损K。若a≤ρ^ε，则可取tube exponent `ε₁=4ε₀`、mass exponent小于`min(ε,ε₀)/2`，令所有source损失相对µ、ε、ε₀足够小。这避免把原(171)的宽δ^(2ε₀)直接换成ρ尺度、平白产生ε₀/µ费用。ε₁只须相对ABC的ζ小，regularity/graph损失再相对µ等小。

本节得到的是R4中的vector tube cap。它**不是**二维scalarization定理；要使同一个有界λ下的 `(t,λ·F(t))`对所有scalar affine tubes仍有正幂nonconcentration，须另付本轮rich-triple论证。该论证必须采用bounded-range版本，不能预设F是全局Euclidean-Lipschitz；rich scalar tube的time跨度需由first-coordinate packing另给。不能将原Remark21.3或Mattila的Hausdorff a.e.结论直接当作本有限、带质量的量词输入。

## 7. scalar ABC的精确参数与本图的接入

原PDF91有两个不同的小参数，全文提取去掉bar会混淆：

- regularity参数`η_reg<η₀(κ,ζ,ε₁)`，用于B的(r,1,r^(−η_reg))-set及C的(r,κ,r^(−η_reg))-set；
- graph/小像参数`barη_graph<barη(κ,ζ,ε₁,ε₂)`，要求graph density≥r^(barη_graph)、像cover≤r^(−barη_graph)#A。

还需ε₁足够小于ζ、ε₂>0，最后r足够小于所有参数。结论是`#A≥r^(ζ−1)#C`。A只要求r-separated及bounded；C是**标量**，B∈R²。原高级radialprojection13.2、BSG13.7等未在本轮完整重证，Theorem21.2仍是named输入；不能由Remark21.3把scalar multiplier变成vector multiplier。

本轮若rich-triple scalarization已付，(2)保A cardinality，B的first time坐标保(r,1,K)，scalar Φ的κ-AD保C。对原coarse g平均固定一个b₁、φ₁，得到dense graph于

    A × (B−b₁) × (Φ_q−φ₁).

(4)使其小像落在A的Cr邻域，cover≤K#A。product frame只是dominating reference；graph是由原路径数归一得到，不是新独立shading。投影/粗化的K费用合并后，`η_reg,barη_graph=O(loss/µ)`，须分别低于上述两个阈值，不能只检查其中一个。

若κ>ζ而所有损失小，ABC给`#A≥K⁻¹r^(ζ/2−1−κ)`，与`#A≤K/r`矛盾。原proof21.1的比较就在此处。它并不需要A下界等于ρ⁻¹，只需要已证upper与投影前后K倍可比。

## 8. fixed-ρ使用的尺度，以及低速度的另一项责任

逐行查看4844–4916：固定ρ后的W构造、A、B、(170)–(173)及ABC调用，只使用**当前同一ρ-window**的whole-f affine nonconcentration。没有再在另一ρ'窗口上调用(167)。不过原regularity/coherence使用ρ、ρ²、相邻allowed尺度以及ABC内部的多宽度regularity；“固定ρ”不等于只需单尺度原配置。

因此若LOCAL-AFF的全局反证能合法删坏windows、删低密windows并保持原time-restriction闭包，本段提供的是fixed-ρ证明接口。本文不通过形式否定all-scale21.1取得它；source的(146)/任意q local-lower也不能代替合法good-q averaging。

whole-velocity下界是另一项责任，本段ABC没有证明它。设各window的实际affine fit已选，某些低速fit满足`|R_J|≤δ^b`，且这些fit times占原Z至少δ^θ质量。若root的time-restriction闭包成立，保T不变、只取这些原times，得到参数`η'=O(η+θ)`的合法原子配置。每个保留window中

    osc f≤C(δ^bρ+ρ^(1+ε₀))≤σ,
    σ=ρδ^(b/2),

只要`b≪µε₀`且δ小。还可令b/2<µ，使ρ²≤σ≤ρ。对该真实restricted配置调用named Lemma19.2，得到

    C_CW(T)≥δ^(C(η'/γ+ε_den)) δ^(−bκ/2).

κ≥ζ时，选`b=C₁(η+θ)/(γζ)`、C₁充分大，再令η、θ足够小以满足b≪µε₀，产生与原CW upper的冲突。因此可排除带足够原质量的低whole-velocity windows；它不直接给首坐标r非零，后者仍是R21 E+swap链中的后续推导。

该调用需要低速fit集合的真实全局density、time-restriction闭包，以及Lemma19.2的原高级证明；不能只凭一个小window慢变就照用19.2。Lemma19.4才有另一个local-cluster形式，两者量词不应混同。

## 9. 当前范围

已具体支付/定位：A的coarse fibre cap与保observable-x投影、原W恢复上界、fine/coarse weights及必需heavy-cell lower、(170)符号反射与(172)同步归一修复、fixedρ与ABC两个损失参数的接口、low-speed删除的独立责任。

本文没有认证单凭generic projection即可保存两端全部量词，也没有在本文件证明rich-triple scalarization或time-restriction闭包。若这些由本轮其他稿支付，可结合本审计形成实际fixed-scale LOCAL-AFF准备；即使准备通过，完整五维sticky其余分支、general归约及Hausdorff仍未解决。不存在新维数界、真实Kakeya反例或已确认重大中间结果声明。
