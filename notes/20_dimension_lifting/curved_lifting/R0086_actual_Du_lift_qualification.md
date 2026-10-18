# R0086：Du 实际曲线、全时变分与直线 lift 资格

2026-10-18，A。仅审原来源与完整欧氏反例之间的真实接口；本文的必要条件是 R50 同点第一变分方法的具体应用，不新增数学 ID、重大性或 ordinary 反例声明。实际独审另记；未经外部同行评审。

## 1. 恢复、实际阅读与本轮准确问题

已读 R86 working_spec5、GOAL、STATE 当前入口、ROADMAP 路线与冻结记录、registry 全部78状态及 R50 lift 字段、R85 next。实际全文读 [Du2610.05404v1 HTML](https://arxiv.org/html/2610.05404v1) 的 §§1–3、证明及参考文献；随后完整读 root 归档的 `literature/extracted/du_2026_fraction_dimensional_compression_2610_05404_v1.txt`。该当前 text 有 physical pages1–5，不冒先前预期8页、PDF视觉核验或本代理的字节认证。HTML Date 为 October4，served PDF 正文 Date 为 October6，而版本标签仍 v1 October4；身份由 root 统一记录。本来源 R81 已有全文 HTML 阅读，不称本轮首次发现。

实际又读库存 Nadjimzadah2609.06299v1 §1 的 compact X-Kakeya 定义、完整 Def2.1、Prop2.2 及其 §3 证明、Prop2.5(ii) 与相应构造；对照 R50 root8、A10 的全时变分／适用范围。没有重新全文独证 Nadjimzadah2503.15760 的高级 coney projection theorem；Du 的 matching lower 若调用它，保留具名层级。

问题是同一紧 K 的严格维数上界能否送到真实满方向 Euclidean 直线集，不能将曲线方向参数 (p,q) 与拉直后的直线方向等同。以下实际计算 Ψ、方向、维数预算，并排除 Def2.1 内所有有限 codimension 的零方向损失 lift；不宣排除任意改 clock、只在 E 上的非全平移构造或未知反例方法。

## 2. 原 E、原 clock 与维数输入的独立核算

写 ε=1/100、s0=4ε。Du 的原族为

    X(w,t;p,q)=(w1−tp−t²(q+p²/2)−t³p, w2−tq−t²p)， |t|≤ε。

构造的紧 Q 由两个二进制序列给 (x,y,z)，z=Σ_(i<j)2^(−i−j)e_i f_j。固定前 n 位，r=2^-n 后精确尾式为

    (x,y,z)=(x0+rx′, y0+ry′, z0+r x0 y′+r²z′)。             (1)

因此4^n个 pieces 直径 O(r)，且投影 (x,y) 满 [0,1]²。用投影 lower 和 cover upper 可独立得到 Q 的 Hausdorff、packing、upper-box 维数均为2。仿射缩放

    (p,a,b)=(s0(x−1/2), s0(y−1/2), s0²(z−y/2))

给 Q_s0。E 的坐标为 (w1,w2,p,q)=(−a,b,p,a−p²/2)。这是有 Lipschitz 逆的固定光滑嵌入，故 E 的上述三种维数也是2。每 (p,q)∈B_ε² 对应 a=q+p²/2∈[−s0/2,s0/2]，再用 Q_s0 对 (p,a) 的满投影取 b；这是真的每曲线方向参数都有原位置，不是由一张局部光滑 graph 选择器给出。

K 是所有 E-label 的整个固定 clock 曲线段之并，因紧性而紧。clock 长2ε是固定常数；拉直后可统一 dilation 得至少单位长，不涉及随 δ 变短或按 label 改 clock。E 的小维数不是 K 的维数上界直接相加就给2.5，后者须实际用下述各向异性 cover。

## 3. Ψ 的实际作用与原方向缺维

Ψ(x1,x2,t)=(−x1/(1+t²),x2−t x1/(1+t²),t)，逆为

    Ψ^-1(A,B,t)= (−(1+t²)A, B−tA, t)。

在原 bounded 区域二者都是固定 bi-Lipschitz。对 E 中 w1=−a、q=a−p²/2，直接代入得到整 clock 上的真直线

    Ψ(Φ(w,t;p,q))=(a+tp, b+t p²/2, t)。                    (2)

故原 displayed label 直线族的真实无向方向是 [(p,p²/2,1)]，只由 p 决定；在小 bounded 区间其单位化 map 有非零导数，是 RP² 内的一维光滑弧。q 的变化变成位置 a 的变化。原二维 (p,q) 方向球不被这些 labels 送成二维角度域；Jacobian 对 q 的一列是0。源确有真直线化，但这批原直线所供应的方向不满，也无正角测度。此处不分类 K′ 内所有偶然附加线段；例如其实际矩形就另含斜线，不能把 displayed direction map 当 K′ 的全部线方向集。

若从原 (p,q) 平面取 δ-net，约 δ^-2 个曲线 labels 只占 O(δ^-1) 个直线方向 δ 帽；固定 p 而 q 变动可在同一帽有 ≍δ^-1 个 labels。原方向先验、分离或权帽 upper 因而不能免费送到拉直族。finite 或 countable rotations 的这些 displayed label 方向像仍至多一维，不会自行填 RP²；不以此断言旋转后点集内没有其它线段。

## 4. 2.5 的实际上界与高级 lower 的层级

由 (1) 缩放可得每 piece 上

    |Δp|+|Δa|+|Δb|≤C R， |Δb−p0Δa|≤C R²， R=s0 2^-n。

对 (2) 减该 piece 的中心线，令 U=Δa+tΔp、V=Δb+t(p²−p0²)/2，则

    |U|≤CR， |V−p0U|=|Δb−p0Δa+t(Δp)²/2|≤CR²。

因此 O(R^-2) 个固定倾斜 boxes、每个边长 O(1),O(R),O(R²) 覆盖整个同一 K′=Ψ(K)。以 R² 球盖每 box 需 O(R^-3)，总 O(R^-5)，故 upper-box K′≤5/2，进而 Hausdorff K≤5/2。各 R² 尺度相邻比固定，确给全 upper-box upper 而非仅稀疏尺度。

matching Hausdorff lower 用 source Cor3.4 所调用的外部 coney projection 输入：这里 velocity curve 的一、二阶导数行列式为1；源据此对几乎每 t 得 slice 维数≥3/2，再加时间。本文未独证其外部高级定理全部 basic hypotheses／proof，故“维数等于2.5”仍标来源定理；本资格反攻实际仅需已经独立核过的≤2.5。

## 5. Def2.1 的真实量词与 Prop2.2 的方向

按 [Nadjimzadah2609.06299v1](https://arxiv.org/abs/2609.06299)，设 N=3+s。原定义要求同一 smooth submersion π(z,t)=(π_t(z),t)、maps a(p,q,w,ρ) 与 Θ(p,q,ρ)，对全部开参数中的 (p,q)、w∈R²、ρ∈R^s 及整个非退化 I 有

    π_t(a(p,q,w,ρ)+tΘ(p,q,ρ))=X(w,t;p,q)，
    rank D_(p,q,ρ)Θ=N−1−ν。                               (3)

Θ 独立 w；π 的域必须含所有这些完整线段。compact 参数 balls 允许选 interior 并延伸到开邻域，不能仅在 E 的粗糙子集取导数。

Prop2.2 从高维 classical lower 得 curved lower：d_Kak(X)≥d_lin(3+s−ν)−s。对一个实际 K，证明使用有正 buffer 的 compact Ω0 和 π^-1(K)∩Ω0；有限 submersion charts 给 Hausdorff upper dim_H K+s。ν=0 的方向 map 含 open patch，固定 rotations/dilation 才补 full directions；ν>0 先坐标投影至 R^(3+s−ν)。这不是“曲线方向满所以任意 lift 都满”的定义。

因此若 Du 有 (s,0)-lift，实际 K 将给 classical set dim≤s+2.5=(3+s)−0.5，确有严格反例潜力；不应未算先拒。但 (3) 的全平移／全 clock／满方向 rank 正是必须证明的输入。下一节对此整个允许类给必要性反证，不只说当前文献没写构造。

## 6. 同一参数点的全时第一变分

反设 (3) 中 ν=0，固定一个 interior P=(p0,q0,w0,ρ0)。令 m=2+s=N−1，

    T(t)=D_zπ_t(a(P)+tΘ(P))， W=D_w a(P)，
    J=D_(p,q,ρ)Θ(P)， A=D_(p,q,ρ)a(P)。

J 是 m×m 可逆常矩阵。Du 的 w 导数恰 I2，原参数一次微分给每一个原 t 的精确等式

    T(t)W=I2， T(t)(A+tJ)=F_p0(t)P0，                      (4)

其中 P0=[I2 0]，

    F_p0(t)=−t [[1+p0 t+t², t], [t,1]]。                  (5)

(4) 未对 t 取有限 jet，T(t) 可随 t 任意 smooth 变；每一式在同一 P 处使用同一 T(t)。w 全开与 Θ_w=0 是第一式的关键，不能对一个选出的 w(p,q) 冒同样右逆。

R50 的“存在性与 affine lift 等价”只对原目标 parameter-linear 的情形双向成立；当前 p² 不能直接套那条双向结论或 F=tI+t²B 分类。但任何本 nonlinear 目标的 lift 都必须满足其同点变分 (4)。这里仅用这一必要方向，既未假原 π affine，也未把一阶变分 model 误当原曲线本体。

## 7. 任意有限 codimension 的 resolvent 必要条件及矛盾

令 C=AJ^-1、P=P0J^-1。(4) 成为

    T(t)(C+tI_m)=F_p0(t)P， T(t)W=I2。

det(C+tI_m) 是首一多项式，只有限多个零点；F_p0 的行列式为 t²(1+p0t)。可在原非空开时间区间中删去这些有限点，留下非空开子区间。于是

    F_p0(t)^-1=P(C+tI_m)^-1W。                            (6)

两边均为有理函数，在一个开区间相等即清分母后多项式恒等。右边是 strictly proper resolvent，在形式无穷远为 O(1/t)，因为 (C+tI)^-1=t^-1(I+C/t)^-1。左边直接为

    −1/[t(1+p0t)] [[1,−t], [−t,1+p0t+t²]]。                (7)

当 p0≠0，(7) 的 (2,2) 项趋向 −1/p0≠0；p0=0 时为 −t−1/t，也非 O(1/t)。矛盾。这只是有理恒等式／次数比较，不把原 π 或时间域延拓到无穷；也不需要解析 π。

因此，对每个有限 s≥0，Du 全族在原 t、全开 w、Θ 独立 w 的 Def2.1 类中没有 (s,0)-lift。任何这样的 smooth coherent lift 若存在，必须 ν≥1。结论覆盖每个 p0 的情况，不能靠避开 p=0 或取更小非空方向开集绕过。它是同点变分方法的具体必要条件应用；不登记新 ID，不将这一初等资格证书称重大新 rigidity。

## 8. 有损 lift 的真实可行校准和维数预算

为避免把上一节过强读成“Du 完全不能 lift”，可以直接给一个合法 (3,1)-lift。取 ρ=(r1,r2,r3)，z∈R5，定义

    π_t(z)=(z1+t z3+t²z5, z2+t z4)，
    a=(w1,w2,−p−r1,−q−r2,−q−p²/2−r3)，
    Θ=(r1,r2,r3,−p,−p)。                                 (8)

π 的前两列给 rank2；代入 a+tΘ 恰是 Du 的两个 X 坐标，全部参数和原 clock exact。D_(p,q,ρ)Θ 的 rank 是4，而 N−1=5，故 ν=1，Θ 独立 w，原线段可放在共同 compact-buffer 的开域。这里没有假最高 cubic coefficient 的二维 Jacobian 可逆；原 Prop2.5(ii) 的该假设确不适用于 Du，(8) 是单独验算的构造。

对这个 specific lift 还可付更强的实际检查，不只 upper 预算。投影掉 z5 后，原 E 的整 clock lines 成为

    (−a+t r1, b+t r2, −p−r1+t r3, −q−r2−tp, t)。           (9)

方向 (r1,r2,r3,−p,1) 真含 R5 的 open patch，因为原 E 的 p 满一个 interval、ρ 含三维内 ball。但 (9) 的同一原 union 有正五维 Lebesgue measure：Qs0 中确有 p=0、b=0、q=a、a∈[−s0/2,0] 的整一维片。证明是取 e1=1、其它 ej=0 使 x=1/2；每 y∈[0,1/2] 可取 f1=0 的二进制展开，故 z=y/2、b=s0²(z−y/2)=0，a=s0(y−1/2)。在这片上，固定 t 的四个空间坐标关于 (a,r1,r2,r3) 的矩阵为

    [[−1,t,0,0],[0,0,t,0],[0,−1,0,t],[−1,0,−1,0]]，

其 determinant=t³。任取 a 的内 interval I_a 与 ρ-ball 内小 box R0，固定 t≠0 的 affine map 是一一的；不同 t 的最后坐标不同。因此原实际 projected union 的体积至少

    |I_a| |R0| ∫_[ε/4,ε/2] t³ dt >0。

这并未增加新的自由位置或把 source E 换成任意参数集，且全用原 clock 内点。它严格排除这个已构造 full-direction 有损 lift 本身作为低维 ordinary counter，不声称每一种其它有损 lift 都有同样实际体积。

对 dim_H K≤2.5，(8) 的原 R6 逆像 upper≤5.5。ν=1 后 source 可送到 R5 full directions，但这个 upper 已超过目标维5，不能给严格低维反例。一般任何 Def2.1 lift 的现有预算为

    effective ambient M=3+s−ν， source upper=s+2.5=M+ν−0.5。

§7 迫 ν≥1，故仅凭此 source 的 fiber upper，永远没有 upper<M。这里只排“已给维数预算自动成功”，不证明每个特殊 inverse subset 实际维数等于该上界；若另有更小 fiber 原质量机制，须独立证明，原文未提供。本文不继续优化最小 s 或损失参数。

## 9. 原 marks、权重、平均及逐管闭包

Du 的实际成功对象包含每个 E-label 的整个 fixed clock，故本文的 whole-segment 转换无需 finite shading theorem。若另考察原 δ 曲线 tubes 中的任意 measurable Y_i，Ψ 在 bounded region 的 Jacobian 和逆导数均固定，体积／每管 density 只变常数，影像包含于对应固定倍宽直线 tube；但方向帽重数按 §3 真会退化。

逐管 density≥λ 只给影像逐管可比 density，不能补没有的方向。平均 λ 先取 density≥λ/2 的 whole labels 至少保 λW/2 原权；未归一帽 upper 可继承，原方向覆盖却可能损失，不能继续声全方向或原 N 全保。任意进一步裁 shading 不保一条完整单位段，更不能由 finite near-full marks 自动得同一个 Hausdorff Kakeya 集。全 E 的几何包含与选出 subset 的质量／维数是不同量词。

Def2.1 对全部 w 的 coherence 正是 Prop2.2 可从任意 w(p,q) 选择 lift 的原因。若仅对 E 的 w1=−q−p²/2 等约束成立，W 的右逆不再可微使用；§7 不排这种另类构造，但它不匹配该来源的 lifting theorem，也未由 Ψ 提供 full-rank direction map。不能在做完 selector 后冒全平移空间。

## 10. 补齐方向的实际预算反攻

把 K′ 乘 k 个固定区间得到 R^(3+k) 中集合的 upper-box≤2.5+k。原直线可配额外 slopes β∈R^k，其明显继承的 label 方向形如 (p,p²/2,β,1)，只有 k+1 维，仍比 RP^(k+2) 少一维；这不是产品点集内所有额外线段的分类。产品确有严格低 ambient 的 cover upper，但缺方向不能略过。

有限或 countable rotations 保这些方向的 Hausdorff 维数≤k+1。若用连续旋转／独立参数补足角度，原已知 cover 只给“2.5+k 加参数维”的 upper；至少一维的常规参数补齐就不再给小于3+k的严格 upper。这个预算不反所有可能协同重叠的 rotations，也不认证每种 completion 实际满维，只说明原 source 未给所需更强压缩。

对最直接的独立旋转并，可以用原集合本身给更强反攻。§8 已核 K′ 真含 {(a,0,t):a∈[−s0/2,0], |t|≤ε}。绕 t 轴取任意非空 open φ 区间，对 a 的负内区间和 t 的内区间，map (a,φ,t)↦(a cosφ,a sinφ,t) 的绝对 Jacobian 为 |a|>0；必要时缩 φ 区间使其一一。因此这一实际旋转并含正三维体积的扇柱，乘 k 维内盒后有正3+k维体积。它只排这种独立旋转并，仍不排更精细的依赖参数选择或另一构造。

同理，任意 smooth diffeomorphism 不保直线方向，任何自由 fiber 不自动保直线／满方向。要从实际紧 E 另造 ordinary 反例，必须在同一集合中给全部方向的 exact unit lines、严格 Hausdorff upper 和额外 fiber/parameter 代价，不能只拿原 packing E=2 加一个未核 lift 口号。Def2.1 零损失路径已经严格排除，source 的有损路径又无严格维数余量。

## 11. 原 source 证明、条件方向与旧范围的精确边界

Du Lem2.1 的 polynomial determinant 比较和 mixed partials 矛盾可直接核；两个候选 Jacobian branches 在实小邻域分开，C2 连续性允许局部固定其一，W2 的混合偏导遂冲突。它排的是 open parameter graph 上的二维 surface compression，不声普通直线 Kakeya 反例。phase 的 mixed x/y matrix 为 I，另一 Hörmander determinant 在小域非零；这不意味着其方向在 Ψ 后仍为二维。

Du 上界的二进制／box 计算已在 §§2–4 实核，matching lower 的高级 projection 引用未全部新独证。Nadjimzadah Prop2.2 是高维 classical 输入推出 curved 下界的 forward theorem；只有先付实际零损失 lift，才可将严格 curved upper 反读为 classical counter。本例精确缺项不只是“文献未写”，而是 §7 在本定义下不存在该 lift。R50 的旧参数线性分类不能整条搬到含 p² 的目标，然而其必要性微分方法正好给这次完整类反证。

其它 clock、只在实际 E 上的 selector／非全 w lift、非 smooth 或不保原 parameter law 的方法未被本证排除；当前源也没有支付它们。不能把这些未覆盖可能性立即换名为新一轮 narrow task，亦不把方法排除当原 Du 定理错误。

## 12. 资格结论、真实交叉状态与停止

本轮实际找到的 positive 对象是 compact 的2.5维 curved set，以及 Ψ 后同样低维、但原 displayed labels 只供应抛物线一维方向弧的真直线集；不声称分类该点集全部偶然线段。对 Nadjimzadah 原定义的任何有限 codimension，§7 排除 ν0；§8 给 ν1 的实际可行校准，并在同一原 E 的投影后证明正五维体积；一般 source 维数预算也不够。因此原来源不能经所要求的 qualified lift 自动给 n≥5 full-direction 低维 Euclidean Kakeya。

已实际全文读 root8、终 macro6/next6，独核 root 的 resolvent 整合、独立旋转扇柱及 specific lift 的 t³ 体积证明，无强制修改。root 已实际全文读 A12，B 已收到全部公式待实际全文互审。本稿自己的证明不计自身独审，完整 root/B 稿完成后再记录实际 cross，不预填 reviewed。root 统一 source 字节、版本与后续 formal；本文未操作 Git/meta 或下载。

按 working_spec 停止把此 proper-direction family 当 ordinary 反例入口，不续 products／rotations／codimension 优化或 R85 regular-leading 模型。没有新 ID、major、ordinary 维数改进或 Goal 完成；来源主张、本文初等必要性证书与未新独证高级 wholeproof 分开，未经外部同行评审。长期完整高维／一般 Kakeya Goal 保持 active。
