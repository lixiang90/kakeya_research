# R0055：一般近三维代数簇的一手范围与原密度审计

2026-10-17，A 独立审计。主命题 G3 仍未证未否；本稿完成来源量词、原权重／平均密度闭包、低密度区和具体转移责任的检查，不把未付的空间—方向分包假设登记为定理。具名外部输入的 whole proof 未由本轮重证，所有内部审查仍未经外部同行评审。

## 1. 恢复入口、完整命题与停止条件

已实际读本轮 working_spec、R54 macro／next、当前 STATE，并按固定入口恢复长期 Goal、既有登记和冻结路线。固定 D,C,C0；Z⊂R5 为至多 D 个次数≤D 实多项式的共同零集，实维数≤3，可奇异且系数可随 δ 变化。原轴 a_i+t v_i（|t|≤1/2，|v_i|=1）整个落在 B10∩N_(Cδ)Z；T_i 是真单位段的半径 δ 邻域，v5=|T_i|≈δ⁴。给有限原族非负权 w_i、W=Σw_i>0，physical S4 每 C0δ 帽原权≤α，以及可测 Y_i⊂T_i。记 E=∪Y_i、I=Σw_i|Y_i|、λ=I/(v5 W)。

G3 询问：∀ε>0 是否 |E|≥c_(ε,D,C,C0) δ^(4+ε) λ³ W/α？所有 ε 常数须统一于退化系数、原权跨度、δ 和任意 Y。全 3D L3 maximal M3 可具名调用。不得以一般簇可无损 flatten、近轴可 δ-snap 到 exact 轴，或每管不同 frame 代替待证步骤。若一手已有全称应用则按应用结束；若仅一个转移桥失败，也不能称 G3 被否定。一主轮未闭合即停止本 transfer 迭代，不继续 canonical toy。

## 2. 有界一手排重：实际版本、读段与对象

本轮一手检索及实际声明阅读有界完成；未命中全 G3 不构成“不存在既有定理”或新颖性证明。以下 PDF 由 root 统一归档，A 不认证尚未写出的 metadata／Git，也不称全篇高级证明已独证。

| Primary | 实际版本／读范围 | 可用结论与未覆盖项 |
|---|---|---|
| Katz–Rogers, *On the polynomial Wolff axioms*, [1802.09094v3](https://arxiv.org/pdf/1802.09094v3) | v3 2018-07-22，8 页；PDF1–4，Th1.1、Lem2.1–2.3、Th3.1／proof setup。v2、v3 分别保原件 | ambient n 的有界复杂度半代数 S，δ-separated tubes，λ≥δ，#rich tubes≤C|S|δ^(1−n−ε)λ^(−n)。n=5 的 λ⁵ 计数不是任意可测 E 的 λ³ 估计 |
| Binyamini–Salant, *Establishing the Polynomial Wolff Axioms for δ-Separated δ-Tubes With #o-minimality*, [2609.24135v1](https://arxiv.org/html/2609.24135v1) | arXiv v1 2026-09-21；Main Th1／Cor2，PDF1–3 与声明；已有 R42 来源 | 全 0<λ,δ≤1，复杂度以 poly(format,degree) 支付，无 δ^ε；仍是 ambient λ⁵／有复杂度的 S。可给完整近簇方向数界 |
| Zahl, *New Kakeya estimates using Gromov’s algebraic lemma*, [1908.05314v4](https://arxiv.org/pdf/1908.05314v4) | v4 2021-01-12；PDF1–6 的 Th1.3、1.7–1.9、2.1／2.4 | multilinear wedge-weighted overlap 与 nested-variety tube counting；额外横截和尺度计数不能省成 G3 的线性任意阴影 |
| Di Plinio–Parissis, *Maximal directional operators along algebraic varieties*, [1807.08255v2](https://arxiv.org/pdf/1807.08255v2) | v2 2020-08-17，34 页；PDF1–6，ThA/B/C 与算子定义 | 簇在 direction space；对 #V≤N^m 给 L² directional norm N^((m−1)/2+η)，Nikodym 版 δ^(-(m−1)/2−η)。不等于物理三维簇附近轴的原方向 cap／L³ 转移 |

对应本地原件：literature/primary/katz_rogers_2018_polynomial_wolff_v2.pdf、同 stem v3；binyamini_salant_2026_sharp_polynomial_wolff_2609_24135_v1.pdf；zahl_2021_gromov_kakeya_1908_05314_v4.pdf；di_plinio_parissis_2020_algebraic_directions_v2.pdf。各有 literature/extracted 同 stem 文本。Ellenberg–Oberlin–Tao [0903.1879v2](https://arxiv.org/abs/0903.1879v2) 只筛题名／摘要：finite-field maximal，未作 Euclidean 输入、未要求新 PDF。

KR 的 Lem2.1 以量词给“所有 contained tubes”参数集的统一半代数格式；Lem2.2 选每方向一个新代表；Lem2.3 给紧半代数集的有限 C^r 参数化。三步都不保证选中的新 tube 保原 Y_i／I。任意原有限族的析取复杂度可随 #T 增长，条件化任意 E 又可破坏半代数格式，所以不能把这些 source 操作直接用于原 shaded incidence。即使平面中同方向有两根不交管，只有第一根有原阴影，一个合法“每方向选一根”的存在选择仍可选第二根。这只反对免费质量回传，不反 KR 或 G3。

## 3. 原质量形式与合法删选

将 G3 写为

    |E| ≥ c_ε δ^(ε−8) I³/(α W²)。                 (1)

这是 v5≈δ⁴ 后的等价形式。原 tube 子族和可测 shading 子集仍属几何类，但须重新算 I、W、λ；不能在缩阴影后沿用旧平均 λ。整 label 唯一分区且 Y_i 不变时，每条余管的原逐管密度下界保持。若只是 I′≥θ I 且 W′≤W，则 I′³/W′²≥θ³ I³/W²，清楚支付 θ³；原 cap 仍≤α。零权可预删除。

本轮所需不是逐管 AD 下界，也没有可测方向选择问题：原族有限。后续若复制 label、重格或按空间事件划多包，W_j 和实际角帽权都要按该构造实计。

## 4. 无权 δ-separated 全平均版足以推出原任意权版

把 S4 划细的半开 δ-cells，直径≤C0δ；邻接“距离<δ”以及 antipodal 邻接图的度有统一上界。固定有限着色，使同色不同 cell 的实际方向集（按 projective 需要亦排 antipodal）相距≥δ。单 cell 权≤α，或固定细分／扩帽后≤Cα。某色 I_c≥I/J，W_c≤W，J 固定。

在同色每 cell 独立选择一个原 i，概率 w_i/(Cα)，余概率 empty。样本是真原子族，方向 δ 分离，样本阴影仍⊂E。设样本原 incidence I_s、管数 N_s，空样本定义 I_s³/N_s²=0。若无权全平均版给每样本 (1)，则对随机选择取期望，并由 Hölder

    E I_s ≤ (E[I_s³/N_s²])^(1/3)(E N_s)^(2/3)，
    E[I_s³/N_s²] ≥ (E I_s)³/(E N_s)²
                 = I_c³/(Cα W_c²)。             (2)

于是得原权版，只有固定 J³ 和 C。无须 dyadic 权层、最小正权或 log(weight ratio)。此论证说明“来源只写方向分离、无权”本身不是拒用理由；真正要核全 λ／物理簇／原阴影是否对应。

## 5. 全部逐管密度与平均密度：完整小幂闭包

平均版→逐管版直接。逆向先对无权 δ-separated 族证明，再用§4扩权。设来源对每 τ∈(0,1] 及所有管 λ_i≥τ 给目标，其常数只依 ε,D,C,C0，不能只给 τ≥δ^η。

N≤Cδ^-4。若 λ≤δ²，|E|≥I/N=λv5≥cλδ⁴，而目标≤Cδ^ε λ³，二者之比要求 δ^ε λ²δ^-4≤C，已成立。其余 λ≥δ²，删 λ_i<λ/2 的管只损 I/2。余管密度在 [λ/2,1]，有 J=O(log(2/δ)) 个 dyadic 层。某层 I_k≥I/(2J)，其 τ_k 与 λ_i 可比；因 N_k≤N，

    τ_k³N_k ≥ c(I_k/v5)³/N_k² ≥ c λ³N/J³。

用来源 ε/2 得 |E|≥cδ^(4+ε/2)λ³N/(α J³)，吸 log³ 到另一 ε/2 即目标。若用权版，完全同式把 N 改 W_k／W；§4已避免任意权跨度。全 τ→平均的证明不把 near-full 定理升级成 arbitrary λ。

## 6. 已有 sharp PW 真正覆盖 λ≤δ 的 G3

取 S=N_((C+1)δ)Z∩B11。量词消去给统一半代数格式（δ 与系数只是参数）。这里 dimension 确实是 real semialgebraic 维，不能错用某个 defining polynomial 的 complex codimension：例如 x4²+x5²=0 实维3而复维4。可直接由 KRv3 PDF4 Lem2.3（本地文本165–172行）证明所需 entropy／volume：A=Z∩closed B12 缩放到固定 cube，具名 Gromov lemma 用统一有限个 C¹norm≤1 的 [0,1]^m maps 覆盖，m=dim_R A≤3；domain δ网给 N_δ(A)≤C_D δ^-3，故 |N_((C+1)δ)A|≤C_D,C δ²。低维可补 dummy domain 坐标；零维也可用统一连通分支数。Zahlv4 PDF5 文本268–270先明定 real/topological 维，再在 Th2.1／(2.1) 给同一 Wongkew 上界。取 δ 足够小，S 的 nearest Z 点在 B12 中；较大 δ 由常数调整处理。因此 |S|≤C_D,C δ²，对 δ-dependent coefficients 统一，不需 normal／height 下界。每原 T_i⊂S。BS sharp PW 对方向 δ-separated 子族、density1 给 N≤C_D,C δ^-2。再对§4的选择样本取管数期望，有限颜色相加得

    W/α ≤ C_D,C δ^-2。                          (3)

KR 也可给 δ^-2−η；预取 η<ε 即足够小幂版本。原 B10／source fixed ball 的区别可按 midpoint 分固定数 unit boxes，使每整 unit axis 在平移后的固定 source ball 中；不短切阴影。所有常数固定。

若 λ≤δ，则 G3 右边≤Cδ^(2+ε)λ³≤Cδ^ε λδ⁴，而总有 |E|≥I/W=λv5。因此这一区间真实完成，无 M3 和原 E 复杂度假设。真正未付范围可缩为 δ≤λ≤1；KR 的 λ≥δ cutoff 本身不是全类失败的理由。对任意 E 直接套 PW 的障碍在 λ⁵与复杂度，不能忽略这一区间已闭合。

## 7. Flat reverse 与 M3 的关系

令 Z=R3×{0,0}，把任意 3D 单位 δ管及 Y_i 嵌入 5D，并以二维 δ-ball 作 normal 乘积；固定扩管常数不改目标。原物理 S2 caps 在 S4 中等距嵌入，帽权和 W 保持，|E5|≈δ²|E3|、λ5≈λ3。因此完整 G3 反推任意平均 λ 的 3D restricted λ³估计。

R53已另付 restricted→strong：||f||3=1 时截 f≤δ² 和 f>δ^-2，两端 Kδ f≤Cδ²；中间 O(log δ^-1) 层、restricted weak、Σ2^(3j)|E_j|≤C 给 weak 常数 log³；Hölder 截止 Kδf≤Cδ^-2/3，再 layercake 加一 log，选择更小 source ε 吸 log⁴。单位管交固定数空间 cubes，先逐 cube 后 norm³求和处理全空间。故 G3 至少有完整 M3 小幂强度。

反方向 M3⇒任意一般物理三维簇 G3 尚未付。R53 exact regular quadric 和 near parabolic cylinder、R54 common-factor graph都不是任意 D／奇点／δ退化情形。不能把此时 G3↔M3 写成已证，也不能仅凭 flat reverse 宣新的独立高维机制。

## 8. 法向纤维—原方向 packet 的准确共同预算

逐式核 root 当前主稿§4。若真实空间包 j 用配 orthonormal frame 的 orthogonal projection π_j:R5→R3 保 nonshort 轴，normal 二维纤维面积≤F_jδ²，实际投影 δ帽原权≤A_jα，令 E_j 为原事件并、I_j 为其原 incidence、W_j 为真实重复后的原权。f_j=δ^-2fiber(1_Ej) 满足

    f_j≤F_j， ||f_j||3³≤F_j²δ^-2|E_j|。

用固定数真单位投影圆柱覆盖所有端帽及邻 δ方向，不删 Y_ij，可得 K_(Cδ)f_j(u_i)≥cδ^-4|Y_ij|。M3、原帽积分和 weighted Jensen 给

    |E_j|≥c_ε δ^(ε−8) I_j³/(α A_j F_j² W_j²)。

若 Σ|E_j|≤K|E|，Hölder 的实际求和为

    |E|≥c_ε δ^(ε−8) (ΣI_j)³ /
       [Kα (Σ W_j sqrt(A_j)F_j)²]。              (4)

所以保留 incidence 只是一个条件；还须支付 K 和原加权和 ΣW_j sqrt(A_j)F_j。没有构造这些包，本式不是 G3。只声称单个方向图／物理图均可半代数参数化，不推出同一投影下的这些量。

B的完整 actual regular 簇反攻位于 R0055_near_threefold_geometry_counteraudit.md §§2–4：Z={(a,b,s,a²,b²)}；a,b 为 L√δ 网、p,q 为 Lδ 网且在 [τ√δ,2τ√δ]，v=(p,q,v3,2ap,2bq)。先 τ 相对 HRZ tangency 常数小，再 L≫(1+C0)/τ，后 δ 小。原 N≈δ^-2，α=1，λ=1，whole true unit tubes 合法，实际 |E|≈δ²。全部方向位于 √δ 帽，但任意 nonshort global R5→R3 投影只有 O(δ^-1) 个 δ方向帽。J 个组各 projected cap≤Aα，只能保 O(JAδ) 原 incidence 比例；J,A≤δ^-η 不能在 η<1/3 时保 δ^η 原比例。已实际读全 B8节并核截面 disjoint balls 和 inverse formula；这只否固定少 global 投影组的桥，不否空间分包／G3。

## 9. 真实 HRZ 局部类、端点与回尺度

已实际重核 B§§5–6（root§8）的原 Def5.2/(29) 接口。仅有 T∩B(x0,2r)⊂N_(4δ)Z、δ≤r/16。对原 Y_i∩B_r 取最近原 segment 参数；参数落长度≤2(r+δ) 的区间。用 r/8 cells 划原闭参数段：前格左闭右开，最后一格明确包含原右端点 +1/2，端部格可短；至多20个。右端 round cap 的正体积可全部映到参数 +1/2，不能按时间单点零测删去。各 cell 向内 clamp 到原段内长度 ℓ=r/4 的 interval，whole piece 在 B_(r+δ+ℓ)⊂B_2r，不向原轴外延伸。按原 nearest-time cell 唯一划原 Y，保所有事件；piece 新端帽可更大，但不填新 shading。

÷ℓ 后是真 unit axes，h=δ/ℓ=4δ/r，簇仍同固定格式／degree／dimension，I′=ℓ^-5 I_B、W′≤20W_B、实际新帽权≤20α_h。α_h 是原物理 h帽的实际权，不是 α_δ。若未来全 G3 成立，则回尺度为

    |E_B|≥c_ε δ^(4+ε) r^(1−ε) λ_loc³ W_B/α_h，
    λ_loc=I_B/(rδ⁴W_B)，

即 δ^(ε−8)r^(-2−ε) I_B³/(α_h W_B²)。原 finest cap 单独只给 α_h≤C r^-4 α_δ；不能免费设为 δ^o(1)α_δ。一个球的≤20 pieces 也未给全递归的 parent overlap；raw broad/count 不给原 I_B。k4/m3 broad 本来为零，以上只是诚实条件回尺度，不是 HRZ global gain。

## 10. 新 Hua–Yang primary 只作入口范围核验

Root新保存 Hua–Yang, *Cellular Maximal-Density Factoring: Joint Shadings, Stable Refinements, and a Conditional Kakeya Application*, [2608.18870v4](https://arxiv.org/pdf/2608.18870v4)，arXiv v4 2026-09-01；这是与已库 2608.18693v2 不同的论文。本轮实际读 PDF1–6 架构及 Prop10.19／Cor10.21 的条件声明（PDF73／76），未审全94页。

其 finite atomic factoring／Euclidean rectangular companion 从已给可比较 parents 及合法 source refinements 出发。三维 GWZ replacement 仍假设 K_KT(β)、K_F(β)、loss profile、近满原密度和中尺度 coarse count，以及 (I1) 有限 labelled ancestry、(I2) 保质量且各源尺度 local caps 的 reference refinement、(I3) 共 branching 的多尺度 source interface、(I4) 有界 fibres 的 carrier／ancestry 与受限后续协议。Cor10.21 保留这些输入；不是普通 R5 family 自动进入 joint AD4 的定理。故不能只因新题名重开 R49 初始化 gate；也不据作者的 proof-repair 叙述宣称旧定理错误。本轮不另开94页证明任务。

## 11. 结论与停止

本轮实际增加的可用信息是：全称逐管／平均／原权闭包的完整费用；已有 sharp PW 使 λ≤δ 区真实完成；一个完全合法 regular degree2 输入对有限 global projection bridge 的严格反攻；HRZ whole-piece／原 marks／α_h 的确切回尺度。没有 G3 全类证明，也没有反 G3、普通 n5 改善或新颖性认证。

未付项是中间密度下同时处理原空间、真实 near-direction metric 和 incidence 的一般分辨机制。(4) 不能改名为成功假设；任何后继必须真正支付其费用并检查与旧冻结路线的等价性。按一轮停止：不缩成另一个 regular／canonical 正例，不重做 PW degree、normal 阈值或原 R48/R49 公设。当前主 G3 未解未否、这一 transfer 轮已到停止点；后继宏观由 root 选择。指定正式 review 已实际 fresh 全文核 root10／A11／B8／macro6／next6／spec6，修后已列范围通过；G3保持未证未否，停止编辑／检索。
