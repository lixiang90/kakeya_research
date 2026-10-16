# R0023：向量 polarization 的原 cycle 点球估计与共同线还原

2026-10-17，`lifting_obstructions`。已读 GOAL、STATE、ROADMAP、AGENTS、R23 working spec、R22 next target 和原 WZ §22.5。唯一目标是实际 d5/k3/ell2 非二次分支的 rank/linewise 门槛；不重开冻结的 Y-only BSG、独立 W 卷积或 CP/PM。本文给出两项有限、保原质量的严格接口，不声称完成非二次分支。

**结果：** uniform vector quadratic nonfit 给 Q 的点球 cap，可作用于任何受原四时间 product prior 支配的实际 cycle 权。若一个原 dense graph 的**全部 H-cycles**的 Q 落共同线邻域，则可保留一批真实左时间，恢复垂直于该线的 quadratic fit，并把原 vector nonfit 还原成沿线的 scalar quadratic nonfit；原 bounded graph 仍有明确正幂密度。后一接口不直接满足 MNL001：左右时间载体不同，且 Q 沿线不是 S 沿线。

## 1. 实际 finite frame 与明确条件

令 B⊂[−1,1] 为有限原时间标签集，ν 是其**原**概率权重。不同标签允许具有同一位置；所有以下积分都保留原标签和权重。设 base d_t>0、K_t≥1，且

    ν(I)≤K_t |I|     对所有长度 |I|≥d_t 的 interval I。       (1)

F,G:B→R² 有界，不假设 Euclidean C²、Lip 或不可约。令

    S(t,s)=(s−t)[F(t)−F(s)−G(s)(t−s)],
    Q(t₁,t₂,s₁,s₂)=S(t₁,s₁)−S(t₁,s₂)
                    −S(t₂,s₁)+S(t₂,s₂).                     (2)

定义 A_s=F(s₁)−F(s₂)−2s₁G(s₁)+2s₂G(s₂)、B_s=G(s₁)−G(s₂)。精确恒等式为

    Q=(s₁−s₂)[F(t₁)−F(t₂)]
             +(t₁−t₂)A_s+(t₁²−t₂²)B_s.                    (3)

它等价于 V(t)=(t,t²,F(t))∈R⁴ 和 U(s)=[F(s)−2sG(s),G(s),sI₂] 的矩阵乘积。本文后面的证明直接用 (3)，不从形式 rank 推出质量。

固定 h>0、0<a<1，输入是如下 **uniform precision** 的向量 quadratic nonfit：

    ν{t: |F(t)−P₀−P₁t−P₂t²|≤h}≤a
                     对所有实向量 P₀,P₁,P₂∈R²。             (NQ_h)

范数取 Euclidean；若源文使用 max norm，只须在 h 中预留固定维常数。

为说明原 graph 没被抹掉，另可携带原有限 A₋,A₊⊂R²、A₋ 的原概率 µ，以及

    0≤g(x,t,s)≤1,
    ∫g dµ(x)dν(t)dν(s)≥d,        0<d≤1,
    g>0 ⇒ dist(x+S(t,s), A₊)≤r.                            (4)

在实际来源中 µ 可以是已付 coarse input frame 的 uniform prior，A₋ 是原 tildeY 的局部 patch，保其 AD(2−κ)、tube-KT(1−γ)，且 #A₊≤K#A₋。本文件的估计**不删除 A₋、A₊ 的点，也不改变其几何**；不把不需要用到的 source 条件从主命题中移除。式 (4) 必须由原 L-tuples 的 multiplicity 上界归一得到，不能免费设 g≤1。

本文不是实际配置的构造反例。原 T 的 joint AD/CW、Φ/ξ coherence、τ/w 缩放和 (NQ_h) 的源接口仍由 root/A 的实际 source 审计承担。以下命题一旦输入已经支付，就保留同一 prior 和实际正权关系。

## 2. Q 的点球 cap：全部原四时间质量

**命题1。** 任取 q₀∈R²、e>0 和 gap u，若

    u≥d_t,       e≤u h,

则

    ν⁴{ |Q(t₁,t₂,s₁,s₂)−q₀|≤e }
                              ≤a+2K_t u.                  (5)

证明：先删 |s₁−s₂|<u 的 pairs。固定 s₂ 后，该集合在 s₁ 的 interval 长2u中，由 (1) 概率至多2K_tu。对其余固定 s₁,s₂,t₂，(3) 中 F(t₁) 的系数为非零标量 (s₁−s₂) 乘 I₂。于是 Q 命中该球意味着

    F(t₁) 在某个 vector quadratic P(t₁) 的
                   e/|s₁−s₂|≤h 邻域内。

P 的三个系数允许依赖已固定的 s₁,s₂,t₂,q₀，且可以很大；(NQ_h) 的 all-real 量词正好覆盖它们。该 t₁-fibre 的原 ν 质量≤a。对其余原权积分即得 (5)。没有先把重复 Q 值改成均匀 law，也没有假设 Q 的任一 Jacobian 满秩。

更一般地，对任意 0≤c(t₁,t₂,s₁,s₂)≤1 的原 cycle 权，若总质量 D=∫c dν⁴>0，其 conditional Q-law 满足

    Pr_c{Q∈B_e(q₀)}≤min(1,(a+2K_tu)/D).                    (6)

若 c 的支撑的 Q-image 可由 N 个半径 e 的球覆盖，则

    N≥D/(a+2K_tu).                                         (7)

此处 c 可以是合法提取后的 indicator 或 bounded weight；若只有一个大重数 cycle measure，须先支付 domination 常数，不能直接使用 (6)。

## 3. 从原 g 到有质量的 H-cycles

在 (4) 的同一 frame 中令

    f_H(t,s)=∫g(x,t,s)dµ(x),
    H={(t,s):f_H(t,s)≥d/2}.

因为 f_H≤1，ν²(H)≥d/2。对 H 的全部四 cycles 用原权

    c_H(t₁,t₂,s₁,s₂)=∏_{i,j∈{1,2}}1_H(t_i,s_j).

两次 CS 给

    D_H=∫c_H dν⁴≥ν²(H)⁴≥d⁴/16.                            (8)

因此命题1可直接控制这一**实际由 g 得到**的 cycle law。它不要求不同 cycle 独立于原 L graph；product ν⁴只是 dominating reference，相关性留在 c_H 中。

例如工作分辨率 r、d_t≤r，若 h=r^α、0<α<1，取 u=r^{1−α}，则 e=r 可用。若

    a≤r^β,   K_t≤r^{−ℓ},   d≥r^ℓ,

由 (7)/(8) 得

    N_r(Q(H-cycles))≥c r^{4ℓ}/(r^β+2r^{1−α−ℓ}).             (9)

当 ℓ 足够小于 min(β,1−α)，右边给明确的正幂 covering 下界。它排除 Q 落一个或很少的小球；**它没有给 r^{-2+o(1)}，也没有超过 A 的 r^{-2+κ} 预算。** 不得把 (9) 改称 full rank2 输出。

## 4. supportwise common-Q-line 的保原质量还原

以下命题的共同线假设作用于**全部 H-cycles**。只有一个 dense cycle subset 落线，不能自动套用；这一区别是实际 rank 分支的一项未付提取责任。

**命题2。** 设 (1)、(NQ_h)、(4) 成立，ν²(H)≥d/2，且所有 H-cycles 的 Q 距同一 affine line L₀⊂R² 至多 e。令

    u₀=d²/(1024K_t),
    u₀≥d_t,      0≤e≤u₀h/1000.                             (10)

则存在真实左时间集 T⊂B、正交 unit vectors v,n（v 平行 L₀），以及一个 scalar quadratic P_⊥，满足：

    ν(T)≥d²/32,
    |n·F(t)−P_⊥(t)|≤2e/u₀      对所有t∈T；                 (11)

对 ν_T=ν|T/ν(T)，任何实 scalar quadratic P 都有

    ν_T{t: |v·F(t)−P(t)|≤h/100}
                                    ≤32a/d².                (12)

原 g restriction 仍满足

    ∫g dµ(x)dν_T(t)dν(s)≥d²/8.                             (13)

ν_T 对长≥d_t 的 intervals 的 cap 至多 `32K_t/d²` 倍长度。没有把 T 重置为 AD lower 载体。

此外 H|T×B 的原 conditional edge density≥d/4，其全部 cycles 相对 ν_T²×ν² 的质量≥d⁴/256；换回 ν⁴ 至少 d⁸/2¹⁸。它们仍是原 H-cycles，因而继承共同线假设。

### 4.1 Row filtering 和分离共邻域

令 r_H(t)=ν{s:(t,s)∈H}，删掉 r_H(t)<d/4 的 rows，得到 H₀。所删边质量≤d/4，所以 ν²(H₀)≥d/4。写

    C(s₁,s₂)=ν{t:(t,s₁),(t,s₂)∈H₀}.

原 CS 给 `∫C dν²=∫r_H₀(t)²dν(t)≥d²/16`。close pairs |s₁−s₂|<u₀ 所贡献至多其 ν² 质量 `2K_tu₀=d²/512`，因为 C≤1。因而存在分离 s₁,s₂，使

    |s₁−s₂|≥u₀,
    T={t:(t,s₁),(t,s₂)∈H₀},   ν(T)≥d²/32.                 (14)

每个 T 内 row 均有原 H-degree≥d/4。这个选择是按原 ν 平均，不挑最大 unweighted fibre，也没有选一个只含两列而其余 graph 已空的假载体。

### 4.2 从共同 Q 线恢复 normal quadratic

先把 affine line 化为经过0的线：H-cycle 在交换 t₁,t₂ 后仍是 H-cycle，而 Q 反号。若 n·L₀=k，则同一个 q 与 −q 均距 L₀≤e，故 |k|≤e，且每个 Q 满足 |n·Q|≤2e。无需假设对角 cycle 有足够质量。

固定任意 t₀∈T。对每个 t∈T，(t,t₀,s₁,s₂) 是原 H₀-cycle，故 (3) 给

    P_⊥(t)=n·F(t₀)
          −(t−t₀)n·A_s/(s₁−s₂)
          −(t²−t₀²)n·B_s/(s₁−s₂),
    |n·F(t)−P_⊥(t)|≤2e/u₀.

若 F/G 的有界范数为 M，所获 coefficients 至多 C M/u₀；不把大系数当作 bounded。all-real nonfit 条件对此没有障碍。

若某 scalar quadratic P 在 T 上以误差 h/100 拟合 v·F，则 vector quadratic `vP+nP_⊥` 在同一组原 times 上拟合 F，误差由 (10) 小于 h。因此原 ν 命中质量≤a；除以 ν(T) 即得 (12)。这是在保留原质量后得出的 **scalar quadratic nonfit**，不是宣称 F 的每个 scalar projection 原先就非二次。

### 4.3 原 g 和 cycles 没有丢掉

对每个 t∈T，至少 d/4 的原 s 质量属于 H，而这些 pairs 上 f_H≥d/2。因此 `∫f_H(t,s)dν(s)≥d²/8`；对 ν_T 平均得到 (13)。原 x+S(t,s) 距 A₊≤r 的关系未改，A₋/A₊及其 AD/tube-KT/cardratio 也未动。

同一 row-degree lower 给 H|T×B 的 edge density≥d/4；两次 CS 给 conditional cycle 质量≥(d/4)⁴。乘以 ν(T)²≥d⁴/1024 得原 cycle 质量≥d⁸/2¹⁸。这里只对两个左时间条件化，右时间仍是原 B，故不将 A×T×B 冒充一个左右载体相同的新完整 Kakeya 配置。

## 5. 为什么这尚不能调用 MNL001 或判满 rank2

MNL001 的实际输入包含一个矩阵函数的 all-real affine nonfit、差标签的原 slab-Frostman law，以及 `(b−b')(F(b)−F(b'))ψ` 沿线的同一 bounded translation graph。本轮 Q 是四差，且含独立的 G(s)。以下步骤均未自动成立：

- Q 沿共同线，不等于 S(t,s) 本身沿线。mixed difference 消去任意 left/right coboundary；不能在原 g 的 x+S 关系里删掉它们。
- (12) 是左载体 T 上的 scalar **quadratic** nonfit，原 g 仍作用于 A×T×B。它不直接是 MNL001 的同 B、affine-SM 结构。
- 本实际分支的 Φ 差是标量，source 固定角对后更只剩一个实际 scalar multiplier；MNL001 重构 Mat(2,2) 时用的是二维差向量 law 的 slab line-cap。把当前标量 ψ 嵌成 (ψ,0) 会把全部质量放在一条线，违反那个输入，不能冒充已付的二维先验。
- 共同线若只捕捉一个 dense cycle 子集，(14) 的所有共邻域 cycles 未必仍落该线；命题2没有支付从“很多 cycles”到“整个保留 rectangle/cycle graph”的提取。
- 非共同线部分也未得到两维 covering。命题1仅排点球集中，不排曲线、有限多条线、尺度随变的各向异性输出或 rank1 的不同局部载体。

因此本稿给的是合法 mass reduction，可以供真正 scalar-polarization projection 输入或另一个联合展开定理使用。它未提供该高级输入，也不以已冻结的 Y-only small-sumset 闭包代替。tube-KT 的一维条带 upper 只能在已经支付实际共同线/graph/输出比后使用；一个 scalar projection 的 covering 不能替代 A 的二维预算。

## 6. 源 nonquad 精度、prior 和停止点

原 (196) 的容差是 coefficient-weighted 的 Δ，而 (NQ_h) 是统一绝对精度。若某已完成的源 normalization 给所有 vector quadratics 的非集中精度至少 `h(1+|P₁|+|P₂|)`，则其蕴含 (NQ_h)。反方向不能省略。特别不能把原 physical Δ 里的 ρ²、τ、原角差和 coefficient rescaling 一概写成 h=ρ^{ε₁}；root/A 必须先在实际 τ 范围给 uniform h 接口。

命题2除以 gap u₀ 的误差也已明确：需 `e/u₀≪h`，同时 `u₀≥d_t`。若 actual working e 太粗或原 time base 太大，该分支尚不可用。原 graph loss d=r^{O(loss)} 时，u₀ 和 conditional interval cap 只再付 loss 的固定幂；非二次精度和质量指数须先固定，不能通过缩小 κ 获得。

已证明：任意 bounded 原 cycle 权的点球 cap，以及 supportwise 共同 Q 线的保原 g/共邻域还原。尚未证明：全部 source cycles 的 rank2-or-commonline alternative、dense-subset line 提取、所需 vector projection-growth，或实际非二次 alternative 的排除。本文不是完整 source/Kakeya 反例，不增加统计假设后声称原目标已证；这是本轮该任务的停止点。
