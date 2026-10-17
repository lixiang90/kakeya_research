# R0058：原 common-kernel 割线 law 的 slab 门槛与二维上限

2026-10-17，root。主任务先在 working_spec §7 锁定。本文给出一个保原测度的有限门槛及其严格上限；不证明完整 Mat2 分支、普通五维 Kakeya 或新的维数下界。全部新推导须两位代理全文独审，未经外部同行评审。R57 标量容量包络、旧 Y-only/BSG 等冻结不变。

## 1. 实际源与本轮新增机制

Wang–Zakharov 2609.22035v1 Definitions17.2–17.4 的五维 k=ell=3 配置具有 f∈Mat(2,2)、二维 Y、原 used Φ、整管 AD/CW、跨尺度相容。R16 已核原 good-q/L-tuples、重数、heavy window、合法粗化，得到同一原图

    0≤g(y,t,s,φ,φ′)≤1,
    y+(t−s)[F(t)−F(s)](φ−φ′)∈N_(Cr) A_+,
    E g≥r^h, |A_+|≤r^(-h)|A_-|.

原 reference 是 A_-×ν×ν×used-angle-pair，而非 g 的独立边缘。F=F0+u(t)eᵀ 时，|e|=1，写 θ=e·(φ−φ′)，Q(t,s)=(t−s)(u(t)−u(s))，则平移严格为 D=θQ。R16 只直接覆盖 u 像共线的分支；任意二维 u 不由两次标量投影恢复二维亏损。本文新增的是 Q 在非零 offset slab 的双 anchor 消元，而非给旧统一 gain 改名。

下面门槛不需要输出 A/g 的全部源条件，故可独立证；反例也只攻击相应较弱的 standalone 预处理。原完整 source 仍开放。

## 2. 非零 offset slab：完整量词

设 0<r<1，ν 是 [-1,1] 上任意概率（可有原标签重数），每个长度 q≥r 的区间 I 满足 ν(I)≤Kq，K≥1。u:labels→R² 可测、有界；相同 time 可带多个 u 值，以下计数不去掉重数。对任意单位 ℓ、实 c≠0、ε>0，令

    p=(ν×ν){|(t−s)(ℓu(t)−ℓu(s))−c|≤ε}.

存在仅依有界 chart 的 C，使

    p ≤ min(1, C sqrt(K) [(ε/|c|)^(1/6)+sqrt(r)]).       (1)

右端较大时用 trivial 1。可将 c 范围限制到 Q 的固定有界范围；范围外事件为空。特别，ε=r^a、|c|≥r^b、0<b<a，则 p≤C sqrt(K)(r^((a−b)/6)+r^(1/2))。这是原 pair law 的上界；任意 0≤g≤1 在该事件的原质量也≤p，不要求 g 条件独立。对独立原角 law πθ 的 D=θQ 也成立：固定 θ≠0 后 ε/|c| 的比值不变，θ=0 在 |c|>ε 时无贡献；原 ν²×πθ 积分不重置 g。

## 3. 双 anchor 消元及有限尺度 floor

记 v=ℓu，E(t,s) 为上述对称事件。CS 给

    p² ≤ ∫ ν{z:E(t1,z),E(t2,z)} dν(t1)dν(t2).

删 |t1−t2|<ξ 的 anchor pairs，原质量≤CK max(ξ,r)。对其余 anchor，两个 E 方程消去 v(z)，得

    A(t1−z)(t2−z)−c(t2−t1)=O(ε), A=v(t1)−v(t2).       (2)

误差常数固定，因为 time 有界。若 |c|ξ≥C0 ε 且有共同 neighbor，由 |(t1−z)(t2−z)|≤4，得到 |A|≥c0 |c|ξ。除以 A 后，一个 monic quadratic 的 O(ε/(|c|ξ))-sublevel 集由至多两个区间覆盖，总长度≤C sqrt(ε/(|c|ξ))。ν 的 floor 版本给共同 neighbor 质量≤CK[sqrt(ε/(|c|ξ))+r]。

若 ε/|c| 小于固定常数，取 ξ=max(r,C1(ε/|c|)^(1/3))；ξ 过大则 (1) 已 trivial。于是

    p² ≤ CK[(ε/|c|)^(1/3)+r].

当 ξ=r 且 ε/|c|≤C r³，sqrt(ε/(|c|r))≤Cr，仍成立。开平方即 (1)。没有除以未知 slope、没有用 time 或 u 的光滑性、没有对无限 slab 作概率 union。对任意指定 ℓ,c 的同一确定性不等式均成立。

## 4. 零 offset 的真实 g 质量片

令额外 label Ω 带任意固定 reference 概率 β，h(ω,t,s)∈[0,1]，其支撑满足 |ℓQ(t,s)−c|≤ε，原总质量 σ=∫h>0。给 0<a<1，|c|≤ε^a，λ=ε^(a/2)≥r。若 σ≥C K λ（C 足够大），删 |t−s|<λ 至多损 CKλ，使余质量≥σ/2；余边有 |v(t)−v(s)|≤2λ。

把 v 轴分成 λ 半开格，令 B_j 是连续固定数量相邻格的原 time-label 逆像。可使所有余边被某 B_j×B_j 覆盖，每个 label 属于≤C 个 B_j。写 P_j=ν(B_j)，H_j=∫h1_(B_j×B_j)（用删后同 h），则

    ΣP_j≤C, ΣH_j≥σ/2, H_j≤P_j².

故某 j 有 H_j≥cσP_j，进而 P_j≥cσ、H_j≥cσ²。此 B_j 的 u 像在一条宽 Cλ 的 affine strip 内。归一化 ν|B_j 后，原 h 图相对 β×(ν|B_j)² 的密度≥cσ；time cap 付 K/P_j，原 SM fit 命中概率付 1/P_j。平均密度可这样闭包；没有给每根管新增逐管密度。

这只是 coarse strip，不是 r-strip。R16 已付 O(r) linewise 稳定性不能直接吃 λ≫r；若要在 λ 尺度重用，A 的 coarse 输入/输出比、tube-KT、图重数和 all-real SM 回传仍须另证。对真 D 的零 offset 片，先删 |θ|<ε^(a/4)，原 slab cap 付 C Kθ ε^(aγ/4)；再删 |t−s|<ε^(a/4)，付 C Kt ε^(a/4)。余边仍有 |v(t)−v(s)|≤2ε^(a/2)。若 σ 足够大于这两费，以上同片保质量结论原样成立，θ 及其他 Ω 标签始终保原权。本文不把这项未付闭包当完整二分增益。raw Q law 也可能被 h 未用的其他时间片主导；不能由这个 g 片声 raw 全 law 已有 slab Frostman。

## 5. 更强二维门槛及独立反攻参数

自然但错误的加强是：uniform Lipschitz、B 真1AD、所有实 affine vector fits 受 SM 限制，并且所有 coarse affine lines 都逃逸后，Q 或 D 可在 subpower 原质量上满足二维/2−ζ Frostman。下面反攻保原 matrix-time-angle 分解；R27 任意 digital D 反攻没有这一分解。

固定整数 m≥16，M=2^m，δ=M^(-L)，N=mL。取固定 0<a<d<1/2、0<e<d、0<b0<a/2，ρ=2^(-floor(dN))。B 是 [0,1] 每个 dyadic ρ-cell 左半的 δ-grid，均匀原概率；足够大 L 时 δ 整除 ρ/2。定义 hδ 在左半恒等于 (jρ)²，在右半线性连接到 ((j+1)ρ)²。令 u(t)=(t,hδ(t))，F(t)=u(t)e1ᵀ。

本文所有参数先固定、L 后趋∞。例如 d=1/16,a=e=1/32,b0=1/128,m=16，后面的 cover exponent 严格小于2。没有用有限样本计算代替全 L 证明。

## 6. 原 B、Lipschitz、SM 与 coarse line escape 全核

B 的 cardinal≈δ^-1，每个 B 点的 q-ball 在 δ≤q≤1 内有 c q/δ 至 C q/δ 个 B 点；当 q≤ρ/2 用同 plateau 的一侧，当 q≥ρ/2 用相邻周期占比。故 uniform B 真 (δ,1,C)-AD，常数依固定 chart、不依 L。δ-grid/半开端点只改变固定常数。

hδ 连续且 Lip≤4，|hδ(t)−t²|≤Cρ。因此 u uniform Lipschitz/有界。任意实 vector R,U 的 ||u(t)−tR−U||≤δ^a 事件，第二坐标给

    |t²−R2 t−U2|≤δ^a+Cρ≤Cδ^a.

monic quadratic 的 sublevel 是至多两个总长≤Cδ^(a/2)的区间；B 的原 cap 给命中质量≤C(δ^(a/2)+δ)≤δ^b0，L 足够大。系数无需有界；矩阵 all-real fit 的第二 row/第一 col 给相同结论。SM 不是仅对某一个预选 fit 成立。

对任意 affine line，单位 normal n 和任意 offset c，其 strip 条件变成 |n1 t+n2 t²−c|≤C(δ^e+ρ)≤Cδ^e。因为 max(|n1|,|n2|)≥1/sqrt(2)，该 degree≤2 多项式在 [0,1] 的 sublevel 总长≤Cδ^(e/2)。可由二次公式或一阶导数分区直接得出，常数对 n,c 统一。于是所有宽 Cδ^e affine strips 的原 u(B) 质量≤Cδ^(e/2)。所以没有原质量δ^h（h<e/2）的这种 coarse-line 片；这不限于仅 O(δ) line escape。

## 7. 原 secant 的全支撑 cover 上限

固定 t,s 所属 plateau j,k，令 z=t−s，c_jk=(jρ)²−(kρ)²，则严格

    Q(t,s)=(z²,c_jk z).                              (3)

z 在有界区间，|c_jk|≤1；每个 (j,k) 的像在统一 Lipschitz 抛物弧内，N_(Cδ)≤Cδ^-1。全部 plateau pairs≤ρ^-2，所以

    N_(Cδ) Q(B²)≤C δ^-1 ρ^-2=δ^(-1−2d+o(1)).         (4)

这覆盖所有原 ordered pairs，不挑低概率 Jacobian 区域。u 很接近一条非退化抛物线、并逃逸所有上述 coarse lines，但其细分辨率 secants 仍由 δ-dependent 多条一维弧承载。定性 rank2/非共线不能升级 full2 nearuniform entropy。

## 8. 真正原角 law 与 D=θQ

令 C_L 是 base M、L 位、digits {0,M−1} 的标准有限 Cantor 网，H=C_L×C_L，均匀原 φ、φ′ 独立。C_L 是 (δ,γ,C_M)-AD，γ=log_M2=1/m；H 是 (δ,κ,C_M)-AD，κ=2/m。任意二维 unit-normal slab，固定一个 normal 系数≥1/sqrt2 的另一坐标后，用 C_L interval cap，得到 H 的 γ-slab upper，含宽度 floor δ 的固定常数。e=e1 时 θ=φ1−φ1′。

差 digits 有三种，故 #supp θ≤3^L=δ^(-sθ)，sθ=log_M3。保原差权（零 digit 重数不同），不把它改 uniform；其 interval cap 由固定 φ′ 后原 C_L cap 得≤C_M q^γ。独立 scalar θ 与原 pair(t,s) 构成相同原 reference。

每个固定 θ 乘 (3) 仍是一条统一 Lip 弧。故整个真实平移 law 满足

    N_(Cδ) D≤C δ^-1 ρ^-2 3^L
              =δ^(-β+o(1)), β=1+2d+sθ<2.              (5)

取上述数值 β=1+1/8+log2(3)/16<1.225，甚至小于2−κ=1.875。这不是 A 的上界或任何 dense graph 的构造。

## 9. 任意 dominated restriction 的严格二维费用

设 μ 是 (4) 或 (5) 对应原 pushforward，ν′≤μ 任意可测 submeasure，质量 m′。若 ν′ 的 normalized law 在所有 Cδ-balls 上≤K′δ^(2−ζ)，由全支撑 cover 得

    1≤C N_(Cδ)(supp μ) K′δ^(2−ζ),
    K′≥c δ^(-(2−ζ−β)+o(1)).                          (6)

无论 m′ 多小，正质量 normalized restriction 都有这一 cover 障碍。若用未归一化 bound ν′(ball)≤K′δ^(2−ζ)，则 m′≤C K′δ^(2−ζ−β+o(1))。当 2−ζ>β、K′=δ^-o(1)，原 retained mass 必是固定正幂，不能达到 δ^o(1)。任意 adaptive measurable selection、相关的 g 删选也无法扩大整个支撑。这与 (1) 不矛盾：slab 正幂非集中远弱于二维 Frostman。

## 10. 新旧闭包、实际源范围和停止

已付新门槛：(1) 非零 affine offset slab 的全 raw law upper；(4) 零 offset 的同原 g 保质量片；(4)–(6) 在真1AD/Lip/all-realSM/coarselineescape/真角AD与slab/原factorization下，standalone 二维预处理仍失败。它们未经外部同行评审，不宣新颖或重大，不增加普通 Kakeya 维数界。

反模型没有构造 A_±/tube-KT/dense 输出 g，也没有完整 Def17 的实际直线、整管AD/CW和跨时间 Y。因此不反 full common-kernel、完整 Mat2、Th2.2 或 Kakeya。它要求下一步真正使用 A 与 D 的原关联及多尺度费用；不能只在 D 的非平面/原分解上加一个二维 Frostman 名称。本文也不否定条件容量、joint-support 或合法 anisotropic 方案。特别，二维 Frostman 并非 Th2.2 初始双椭圆容量的必要假设；低维 Q 与 Y 的独立联合有可能支付该容量，不能以 (6) 排除所有 ellipse 接口。

实际 quotient R5→R4 可保原 whole-CW 的凸棱柱上界，但 joint3-AD、近full方向不是自动的；OAI4 Hausdorff 结论不能直接替代任意 CW tube-law 的四维 union theorem。事实上 WZ 原 PDF4 明列一般四维 CW 管族的二次曲面浓集障碍，union 可≤Cδ^(1/2)；本文实际重读该段，只把它作为文献陈述，不冒重新构造/验证其全部例子。B 的 lift/quotient 校准只作范围审计，不能再拿 proper factorized 模型冒 main。

本轮停止单独 secant D 的2Fst/cover 升级与 ordinary-rank 推断；不继续 plateau、Cantor 参数微调。剩余真实任务是原 A-D 耦合下的二维 expansion 或具有实际原 metric 费用的新输入。能否从所有 source 数据排 common-kernel 正κ，仍未解决；不以本轮门槛替换长期 Goal。
