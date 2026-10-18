# R0084：真实凸 factoring 的 polynomial containment 与原 shading 接口审计

2026-10-18，A 阶段 I。仅核实际具名 factoring 与原 ordinary 管族的接口，尚未锁定新增益命题。本稿的有限计数推导供独立逐步审查，不将其登记为新数学 ID，不宣普通 n≥5 维数改善、重大性或已完成 Goal；未经外部同行评审。

## 1. 实际阅读、来源层次与两种 child 量词

已实际读当前 GOAL、STATE、ROADMAP 顶部、registry 全部 78 项状态、R83 next 六节、R84 working_spec 五节，以及 R42 主稿八节、R43 主稿十节及反攻七节。新读 [Hong Wang 的 ICM2026 正式网页](https://epubs.siam.org/doi/full/10.1137/25M1806156) §6，特别 Definitions6.4/6.8、Lemma6.10、后续 planks 讨论与 Definition6.13/Conjecture6.14；核其 references15/46 指向 Guth outline 和 Wang–Zahl2502.17655。网页符号有转换问题，以下以显式常数 L≥2 代替容易误读的近似记号，不宣本机已有该出版 PDF。

实际全文读库存 [GWZ streamlined v2 的 §4](../../literature/extracted/guth_wang_zahl_2026_streamlined_v2.txt) Lemma4.1 的 greedy proof、Remark4.2/4.3，以及 §3 Definitions3.1/3.2、Remark3.3、§5 Proposition5.1、Remarks5.2–5.4、Lemma5.9 全证明和 Remark5.10。另读 [LPSW v1](../../literature/extracted/lai_pang_sethi_wang_2026_codimension_two_2610_10603_v1.txt) Lemma4.5 及前后定义：它明确引用 GWZ Lemma4.1，并追溯 Wang–Zahl 的 factoring。故这是已有具名输入的新一次实际使用检查，不能把综述的发表日期当新定理日期。

两种版本必须区分。ICM6.10 写几何上全部 contained children 的数量及每个 child 被约常数个 parents 包含；GWZ4.1 的实际 proof 则给指定归属的 partition

    T′ = ⊔_{P∈P} C_P，  C_P ⊂ {T∈T′: T⊂P}。

后者没有凭这段 proof 额外证明全部几何 containment 的 multiplicity 为 O(1)。本稿完全使用 assigned C_P，足以完成以下计数；绝不把 assigned multiplicity1 冒充 geometric multiplicity1。高级 Kakeya/多尺度 wholeproof 仍是具名外部责任，本稿未新独证。

## 2. 原 N、fine polynomial 输入与平均／逐管删选

固定 n≥2、R≥1，0<δ<1/2。原 T 为 N 根同宽 δ、单位轴、全体落 B_R 的真实凸 tubes，体积 v_δ≈_nδ^(n−1)。对共同半代数 W，复杂度 E 固定而系数可随 δ 变，假设

    #T[W] ≤ K_N(E) N |W|，  T[W]:={T: T⊂W}。       (1)

这是 normalized polynomial containment。若从 R42 的 sharp PW 及 δ-direction separation 调用它，须保 K_N(E) 的实际归一项 C_n P_n(E)/(Nδ^(n−1))；只有 Nδ^(n−1) 足大才是 subpower。不能在稀疏子族中把它写成常数1。以下不要求每个 P 本身半代数，因为每次查询的是同一个 W。原 ordinary δ-direction separation 给 N≲δ^(1−n)，所以 GWZ Remark4.2 的 log N 可并入 polylog(1/δ)；若只给 (1) 而允许无 N 上界的任意 indexed 输入，则所有 L 必须保留 log N 等原费用，不能一概称 polylog(1/δ)。

设原 measurable Y(T)⊂T，I=Σ_T|Y(T)|，λ=I/(Nv_δ)>0。丢掉 |Y(T)|<λv_δ/2 的 labels 只损至多 I/2；再在余下 O(1+log(2/λ)) 个 dyadic density 层中取一层 T0，记 J=C(1+log(2/λ))，使 I0≥I/(2J)，且 μ≤|Y(T)|/v_δ<2μ，μ≥λ/4。于是 N0≥λN/(4Jμ)≥λN/(4J)。

对 T0 应用 factoring，保 N′≥N0/L；因整 label 的 Y 完整保留，I′≥μv_δN′≥I/(4JL)。每条保留管仍有 density≥μ。故平均输入先分层可保原 incidence 的 polylog 比例，而 cardinal 比例至少 λ/polylog；(1) 的新 normalized 常数须乘 N/N′≤4JL/λ。若原本逐管 density≥λ_*，任意整 label restriction 仍保 λ_*，无需上述分层。若进一步裁 shading 则另核，不能从原平均值推每管下界。

这里的 factoring 是 unweighted label/volume 命题。任意跨度的原权不因复制或权层自动只损 log(1/δ)；本稿没有免费升级它为任意 weighted factoring。原普通均匀管族满足本节的计数设定。

## 3. 真 parent 的有界性与 Mv：不免费假 ambient

把 source 的全部 harmless losses 放进 L。令 M=#P，m≤#C_P≤Lm，v≤|P|≤Lv；N′=Σ_P#C_P，所以

    mM ≤ N′ ≤ LmM。                              (2)

每个 C_P relative convex-Frostman，即任意凸 Q⊂P 有

    #C_P[Q] ≤ L (|Q|/|P|) #C_P；                 (3)

parents absolute convex-Katz–Tao 可写 Σ_{P⊂Q}|P|≤L|Q|。不用未经证明的父 ambient，直接在 (3) 取 Q=P∩B_R：所有 assigned children 已落 B_R，故 |P∩B_R|≥|P|/L。

独立证明这一体积分数控制直径。固定单位 e，P 沿 e 的 projection width 为 w，垂直截面积 A(t)，A_max=sup A(t)。凸性及 Brunn–Minkowski 的截面凹性（或从近最大截面到两端的两个锥）给 |P|≥w A_max/n；而 |P∩B_R|≤2R A_max。因此 w≤2nRL。对全部 e 取 supremum 得 diam P≤2nRL。又 P 与 B_R 相交，故所有 parents 在共同 B_{R+2nRL} 中，进而

    Mv ≤ Σ_P|P| ≤ C_n R^n L^(n+1)。               (4)

不需 P∩B_R 为低复杂度集，因为这里合法查询的是 source 的任意凸 Q，不是 (1) 的半代数查询。也没有把剪裁后的 parents 误称仍保原 absolute KT。

GWZ greedy proof 另给交叉验证：maximizer W_j 可替为其所含 assigned children 的 convex hull，contained labels 不变、体积不增；原 children 在 B_R，故可选择这种 maximizer 在 B_R 内。若随后取 John 外盒，仅固定 C_n 扩大。此为特定构造的选择，不是所有 factoring parents 原字面 bounded 的宣称。

## 4. Parents 的 normalized／absolute polynomial containment 完整推导

对同一个半代数 W，利用 assigned partition 而非几何重数，

    m #P[W] ≤ Σ_{P⊂W}#C_P ≤ #T′[W] ≤ K_N(E)N|W|。

配 (2) 得

    #P[W]/M ≤ L K_N(E)(N/N′)|W|。                 (5)

这是 normalized parent polynomial containment。若用 ICM 的非 partition 版本，同一算式需显式乘其 geometric multiplicity B；不把两种版本混用。

absolute 形式则是

    #P[W] ≤ K_N(E)(Nv/m) |W|/v，
    Nv/m ≤ C_n R^n L^(n+2) N/N′。                (6)

所以实际 factoring 的 m 与 (4) 确实把该项压到 polylog·N/N′；从平均 λ≥δ^η 起步也只多 λ^-1 的 subpower 费用。这里 |P|≈v 的全部比较常数都已放进 L；不能把 normalized K 与 absolute K 直接等同而漏掉 Mv。

这是对真正选出的 parents 的有限继承，和“任取 ρ-tube 包络仍有这些 m、Mv”不同。不过证明是原 fine 输入对所有 restriction 和同一 W 的直接再调用，加上 factoring 已有输出；它本身没有新的 positive power，也不形成独立高维机制。

## 5. 同一 parent 下 affine children 及已知 all-λ 闭包

固定 P，用同一个仿射 G_P 将其 John 椭球归一到固定球，Jacobian J_P≈_n|P|^-1。对任意半代数 W′，其 pullback G_P^-1W′ 的 presentation degree/format 不增，体积≤C_n|P||W′|。无需将 W′ 与非半代数 P 相交。于是

    #{T∈C_P: G_PT⊂W′}/#C_P
      ≤ C_n K_N(E) N|P|/#C_P ·|W′|
      ≤ C_{n,R} K_N(E)L^(n+3)(N/N′)|W′|。         (7)

这就是 rescaled assigned children 的 normalized polynomial containment。不能给不同 child 各用不同 frame 后仍叫同一个 W′；也不能把任意 G_PT 冒称同宽、单位长的 round δ′-tube。

partial intersection 分两层。若原输入只有 (1)，(7) 仍只证明 full containment。若原 fine 输入本来是 R42 的 all-λ tail

    #{T: |T∩S|/|T|≥a} ≤ K_N(E)N|S| a^(-n)，

那么在固定 C_P 内作同一 G_P 后，fraction 因 Jacobian 同比而完全不变，直接得到 (7) 同常数的 a^(-n) tail。这个 child 结论已是 R42/R43 restriction+共同仿射的旧闭包；若另裁 clock，仍付旧 q^(1−n) 费用。

但是 parent 的 |P∩S|/|P|≥a 并不等于 assigned children 中有相应比例整管 contained S 或相应 partial visits；(5) 不能直接替成此事件。短段 S 可与一个 parent 有正比例体积，却不含任何 whole child。这个例子只指出证明缺失的 incidence 方向，不声称反证某个带充分 a-loss 的普遍 parent tail。R43 的 common-clock translation kernel 也不是任意形状、各向异性凸 parent 的免费 replacement。

## 6. 真实原 shading 出口：GWZ5.9 用了什么

实际 Lemma5.9 在 R3 把 parent W 的短宽记 w1，将 assigned convex children V 增厚 w1；其尺寸变成 p_i=max(v_i,w1)，再用 relative convexFW 控制 overlap。关键几何是二维 Córdoba L2：overlap fraction θ 的另一个 thick child 被一个体积约 θ^-1|P_child| 的 prism 收容，逐 θ 求和抵消 θ，从而得到 induced parent shading

    Y_P(P)=P∩N_{w1}(∪_{T∈C_P}Y(T))，
    |Y_P(P)| ≳ C_F^-1 λ(C_P,Y)^2 |P|             (8)

及 Proposition5.1 的 compatible multiplicity product。此处 Y_P 是真实原 shading 的邻域，不是任意重新填满 parent；原文还要 refinement/常 multiplicity 等步骤。

Remark5.2 明写 Proposition5.1 只在 R3，此 lower 在 Rn 需要 R^(n−1) 的适当 Kakeya estimate；Remark5.10 只放宽到增厚 children relativeFW，未提供任何维的自动密度式。为核输入，本稿另外实际读 DIR003 全文以及 R53–55 的投影／原密度相关段落。不能因 Lemma4.1 本身任意 n，就将 (8) 的 λ² 或同等 near-full parent 密度直接写在 n5。

原 fine incidence I′ 和 small footprint 保留，不代表 U(P,Y_P) 仍在原 fine footprint，邻域可膨胀；反之用 Y_P=P 会丢失所有同原 footprint 的关联。n5 的下一真实责任是为这些实际 anisotropic children 和原 Y 付相容的 parent-density/multiplicity estimate，而不是复述 (5)–(7)。本阶段尚未证明该责任，也未将所需高维结论偷加为假设。

## 7. n5 的投影输入、OAI4 实际不匹配处及旧障碍

仿照 (8) 投影到 parent 最短方向的正交补，在 n5 得到 R4 中一般 p2×p3×p4×p5 的凸 planks。relative convexFW 能给相对的 projected convex containment；若 parent 取真实 box，利用 common prism pullback 和 (7) 还可付 fixed-format projected polynomial containment。两者都不自动给 DIR003：它要求真实四维 graph-tubes、每个 slope 格的原权上界 α、逐管 near-full marked bins，并保所有端点。OAI4 的 Hausdorff statement 本身也不是任意凸 planks 的 maximal 定理。

即使只看本轮最初的 fine δ-tubes，增厚 w1 后在非短投影情形可成为四维 w1-tubes，角 cap 也须真的算。令 w1≤c，原整轴含 parent，故轴在最短方向的分量≤Cw1。投影的任一 Cw1-cap 对应原 S4 上 O(w1)-cap，δ-separated 方向只给 count≤C(w1/δ)^4。除 actual m_P，并用 (2)–(4) 的 m_P≳L^(-C)N′v 后，normalized cap 最多

    α_P ≲ L^C (N/N′) w1^4/(Nδ^4 v)。                   (9)

对于满方向 Nδ^4≈1，保留 N/N′ 后，要把它写成 L^C(N/N′)w1^3，须另有 v≳w1；这在其余四轴≈1的 slab 范围成立，在任意 parent 并不成立。tube-like 或中间形状会留 w1/v 的真实费用。若先将 parent 各轴分别归一，原 round tubes 又变成 anisotropic tubes，不能用这一变换同时抹掉 shape 和 cap。将 δ 上的 near-full 密度改写成 w1 上 source 门槛，还须控制 log(w1)/log(δ) 的下界或另分尺度范围，R43 已审此费用。

这不是宣所有 slab／tube／intermediate 情形都失败，而是当前 Lemma5.9 generalization 的具体缺项。R53 exact quadric／near-parabolic 的正结论用了真实方向恢复；R55 product-parabola 反攻已证明少数 global projections 无法免费保原 cap 与大 incidence。它们不反 G3，也不能被当前 generic parent 论据跳过。R4 convex-CW-alone full union 另有 source 所述 quadric 集中障碍；补 polynomial containment 也不因此授 direction cap 或已证明的 full PW4 gain。综述6.14仍明确是 conjecture，不能当本轮输入。

## 8. 阶段 I 结论、停止条件与实际审查边界

本阶段实际完成的候选接口是 (3)–(7)：用已有 maximal-density assigned partition，保原 N，derive bounded parents 和 Mv，继承 parents normalized／absolute polynomial containment，以及每个 parent 同 frame children 的 normalized containment；若原有 all-λ PW，child tail 也按旧 closure 保留。平均 λ 分层和逐管 restriction 已分别收费。

这一应用实质区别于任意无质量规范的粗 parent，但仍是具名 factoring 加原全称输入的有限继承，没有产生新正幂或 ordinary gain。旧 R43 本来已付 common-clock partial PW coarsening，不能倒说它尚未解决 basic thickening。GWZ 原 proof 已库存，当前不是发现一个新的 factoring 定理。完整 mean shading→真实 anisotropic parent lower／4D 投影输入的责任尚在，且当前无已锁 phaseII 证明；不以 count closure 本身另开方向、登记 ID 或宣重大。

后续若 root 选择施工，必须先锁原 Y 的相容父密度、actual shape/cap、relative scale 和最终原 footprint 用途，接受 R53–55 与 PW4 等价性反攻；若只是添加所需 density／angular law 为公设或重复 arbitrary thickening，就按本轮 spec 停止。当前 advanced wholeproof 未新独证，source 版本身份不等于证明正确性。现已实际全文交叉读 root 主稿九节、B 八节、spec 五节、最终 macro 六节、next 六节及 source scope 六节；独核 B 的原 mass／同核正闭包／免费 parent 事件与中心 bush 校准通过限定范围。root/B 也已实际全文核 A 正证，A 不将自身施工算自身独审。实际读回 A §7 保 N/N′、§2 保 log N 的修订，及 macro §2 的 N′≥λN/polylog 修复。正式终审另见 research/reviews/R0084_factoring_counts_and_four_dimensional_input_review.md；不预认证未来 metadata/Git/sync。
