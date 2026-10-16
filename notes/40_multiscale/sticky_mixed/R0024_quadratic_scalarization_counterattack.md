# R0024：原 slab 角差先验下的 quadratic scalarization

2026-10-17，`lifting_obstructions`。已读 R24 working spec、R23 next mixed43 target、恢复入口和 SCAL001。实际 d5/k4/ell3 中，hidden Y 是标量而角差 ψ∈R²；本文件独立检验 finite scalarization，不假定 ell3 的 affine 准备或实际 coarse Φ 的 slab law 已免费取得。

**有限结论通过，且 uniform-error 版本更强：** 候选中 `K_t²/b²` 的间隔损失可以去掉。方法是把四时刻 quadratic-annihilating weights 按绝对值最大的项归一化，所得其它三个系数均≤1。保留四时刻原 product 权重后，对全部 adaptive scalar quadratic fits 同时有

    π(Bad_b)≤C b⁻⁴[a+K_ψ(Cw/h)^γ],                         (A)

只需 query scale 合法以及 `b≥C K_t d_t`。这不是声称 coefficient-weighted 误差也自动无损；后者仍需另付多项式系数控制。没有新颖/重大性或完整 mixed43 结论声明。

## 1. 全部输入和 finite labels

令 Ω 为有限原时间标签空间，带原概率 ν；每个标签 i 有 time position t_i∈[−1,1] 和 F_i∈R²。允许 repeated labels/同一时刻的不同原 objects。设 base d_t>0、K_t≥1，满足

    ν{ i:t_i∈I }≤K_t |I|    对所有长度 |I|≥d_t 的interval I。  (1)

假设存在 h>0、0<a≤1，使对所有实向量 P₀,P₁,P₂∈R²，

    ν{ i: |F_i−P₀−P₁t_i−P₂t_i²|≤h }≤a.                   (2)

范数取 Euclidean；max norm 可在 h 中付固定维数常数。F 不需要连续、Euclidean Lip 或 bounded norm。实际 coefficient-weighted source nonfit 必须先合法缩弱成 (2)，不能省略物理缩放。

角差标签另有原概率 π，标签映为 ψ∈R²，保留重复 ψ 的权重。假设对于所有 unit n、real c 和所有合法 q∈[q_min,q_max]，

    π{ ψ: |n·ψ−c|≤q }≤K_ψ q^γ,       0<γ≤1。             (3)

这里的 π 不是 ψ-image 的 uniform counting。所有证明只查询 central slabs c=0；实际 source 可有更强的全 slabs 版本。g 与 ψ 的相关性允许完全任意，由第6节的 bounded graph 保留。

给定 w>0、0<b≤1，定义 Bad_b：存在任意 real scalar coefficients p₀,p₁,p₂，使

    ν{ i: |ψ·F_i−p₀−p₁t_i−p₂t_i²|≤w }≥b。                (4)

系数不预先有界，fit 可以随 ψ 自适应。此处是**vertical scalar polynomial error**，不是一根 arbitrary Euclidean tube；不混用其法向垂直化费用。

## 2. 原富集集合的四个 distinct time positions

由 (1)，每个 exact time atom 的总原质量至多 K_td_t：取一个长 d_t、包含该 time 的 interval 即可。这包含所有重复标签，不能以单一 index atom upper 代替。

若 S⊂Ω 的原质量 β≥b，则 S⁴ 的 product 质量为 β⁴。任意一对坐标具有同一 time position 的质量至多

    Σ_t ν(S∩{t})² ·β²≤K_t d_t β³。

六对求和，若

    b≥12 K_t d_t,                                           (5)

S⁴ 中四个 time positions 互异的原质量至少 β⁴/2≥b⁴/2。无需把 S 归一化为新的 AD 集，也无需四时刻有某个幂级 time gap。

因此离散 atoms/重复时刻已经有显式费用。若 (5) 不成立，本证明不适用：只凭三种 time positions 的富集集合可被任意 scalar quadratic 精确插值，不能免费拿到第四个约束。

## 3. 最大归一化 annihilating weights：无 gap 逆幂

对四个 distinct positions t₁,…,t₄，定义

    α_j=1/∏_{k≠j}(t_j−t_k),       j=1,…,4。

三次 Lagrange 插值的最高项系数给

    Σ_j α_j t_j^k=0,        k=0,1,2。                       (6)

选 j_* 使 |α_j_*| 最大，tie 用最小 index 打破。设

    c_i=α_i/α_j_*,
    R(t₁,…,t₄)=Σ_i c_i F_i。

则 c_j_*=1、|c_i|≤1，且所有 scalar/vector quadratics 被同一个线性泛函消灭。若四个标签都属于某个 scalar w-fit 的 S，由 (6) 得

    |ψ·R|≤wΣ_i|c_i|≤4w。                                  (7)

固定其它三时刻时，`−c_i` 正是通过该三点的 quadratic 插值在 t_j_* 的 Lagrange 系数。因此

    R=F_j_*−P_other-three(t_j_*)。                           (8)

这是 exact algebra。不能先固定一个端点再粗估三次 Vandermonde determinant 的 g⁻³；二次 Lagrange系数本就至多需要 g⁻²，而且选择最大 annihilating coefficient 后连该费用也不需要。α 本身可以极大，只有其比值被使用；本数学证明不依赖浮点数运算。

## 4. 小 vector residual 和原 slab 概率

在原 ν⁴ 上只计四个 distinct time positions。对每个可能选择 j，固定其它三个原标签，(8)给一个完全固定的 vector quadratic P。由 (2)，

    ν{ i_j: |R|≤h, j_*=j }≤a。

选择 j_* 的条件只缩小该 fit set；即使 j_* 随四时刻改变，也没有新增插值系数的 union。四种 j 求和得

    ν⁴{ distinct times, |R|≤h }≤4a。                       (9)

对 |R|>h，n=R/|R| 为 unit vector，(7)蕴含

    |n·ψ|≤4w/|R|≤4w/h。

若存在合法 q≥4w/h，(3)给这个 fixed quadruple 的 π 概率≤`min(1,K_ψq^γ)`。没有要求 ψ 与原数据独立生成；这里是 dominating product reference π×ν⁴ 上的 Fubini。

令 T(ψ) 为 distinct quadruples 满足 (7) 的原 ν⁴ 质量。由 (9)，

    E_π T≤4a+min(1,K_ψq^γ)。                                (10)

而 ψ∈Bad_b 时，第2节给 T(ψ)≥b⁴/2。Markov 得精确可用的界

    π(Bad_b)≤min{1, 2b⁻⁴[4a+min(1,K_ψq^γ)]}。              (11)

如果 q=4w/h 已在合法范围，得到 (A)。它同时控制所有 adaptive coefficients。有限 Ω 下，(4)可按 finitely many subsets 的线性不等式可行性写成事件，故可测；没有对无限三系数做粗 union bound。

## 5. slab scale、small norm 和原候选

若 4w/h<q_min，只能取 `q=q_min`，或一个合法更大尺度；不得外推 below-base slab cap。若 `max(q_min,4w/h)>q_max`，本轮可用的通用 upper 仅为1，不能宣称有选择增益。

原目标中令

    q_cand=C K_t² w/(h b²)。

因 K_t≥1、b≤1，C≥4 时 q_cand≥4w/h。因此只要 q_cand 在实际合法 slab 范围，(11)直接推出该候选

    π(Bad_b)≤C b⁻⁴[a+K_ψ(C K_t²w/(h b²))^γ]。              (12)

即使 stronger q=4w/h 低于原 working base，仍可在更大的合法 q_cand 上使用候选；两种 statement 的 range 不应混同。

small |ψ| 不需要另外假设为零：任意合法 q 都有 `π{|ψ|≤q}≤K_ψq^γ`，由任一个 central slab 包含该 ball 得到。若实际后续还需 |ψ|≥q₀，可另删除这批质量；须把 `K_ψq₀^γ` 加入损失。不能把选出的 actual ψ 免费归一化成 unit vector而改变 scalar fit error。

## 6. 与原 bounded graph 的相关性及保质量

设其它原变量空间 X 有概率 σ，原联合图满足

    0≤g(x,i,j,ψ)≤1,
    ∫g dσ(x)dν(i)dν(j)dπ(ψ)≥m>0。                         (13)

g 可以与 ψ、两个 times 任意相关；原 translations、A-output、Φ 标签等关系均保在 g 的正支集。定义 `G(ψ)=∫g(x,i,j,ψ)dσdν²`，则0≤G≤1。若 (11) 的 upper≤m/4，删除全部 Bad_b 至多损 m/4 原 graph mass，故

    ∫_{good ψ}G(ψ)dπ≥3m/4。                                (14)

进一步删 `G(ψ)<m/4` 的 good labels，损失至多m/4，仍有至少m/2 absolute graph mass。因此有正 π 质量的**实际** good ψ 满足 `G(ψ)≥m/4`。固定任意其中一个，scalar ψ·F 的所有 quadratic w-fits 质量<b，原 g_ψ 在原 σ×ν² frame 中仍有 mean≥m/4。

这不是断言原正权 tuples 的 times 或 angles 独立；product reference 只是已支付的 domination，全部相关性在 g 中。若来源的 angle/time law 还不是这个同一 reference，或路径 multiplicity 归一尚不能保证 g≤1，(14) 不能免费使用。选择 ψ 后也不重新给其 positive-time subset 赋AD lower。

若还删小 norm labels，只须把其 slab upper 与 (11) 相加后维持≤m/4；同一计算仍有效。重复 ψ 的标签继续按 π 原权计，不换成 uniform distinct differences。

## 7. 精度扰动和 coefficient-weighted 的边界

若 time positions **不动**、仅 F 的实际观察误差≤e_F，并且原 |ψ|≤L，uniform scalar fit width 可换成 `w+L e_F`；vector nonfit从 true F 传到 observed F 须把 h 缩为 `h−e_F`。最大归一化 residual 的向量误差≤4e_F，不会产生 time gap 逆幂。

若 time 自身被 rounded，不能用这个结论抹掉任意 quadratic coefficients 产生的误差。必须直接保 original positions，或另给 coefficient-weighted nonfit、真实系数 bound及全部 graph/coarse 权费用。本 lemma 没有解决 source fine B→working-grid representatives 的责任。

实际目标若 scalar fit error 是 `w(1+|p₁|+|p₂|)`，也不是 (4) 的 uniform w。bounded |F|≤M、|ψ|≤L 时，可用三个 gap≈b/K_t 的 rich times控制 scalar coefficients，但必须先有 `w≪(b/K_t)²` 才能吸收 self-dependent error；root 另稿证明这项 extension，本文件不把它归入无损式(A)。

该条件有直接边界：对任何 bounded scalar signal，在一个长 c√w 的 interval 中，取巨大 R 的 `P_R(t)=R(t−t₀)²`，即可按误差 `w(1+|p₁|+|p₂|)` 拟合该 interval 内全部信号。均匀 fine time 实例中，该质量约√w，完全不依赖真正 quadratic structure；故即使 K_t 为绝对常数，w 与 b² 同量级时也不能免费声称所有 rich fits 的 coefficients 已有一致 bound。这只是 weighted-fit 归一化门槛的边界，不是主 scalarization 反例。

## 8. 与SCAL001和actual mixed43的差别

SCAL001以三时刻的 affine residual、可选择 Lebesgue λ 及 Euclidean scalar tube垂直化为输入。这里采用四时刻 quadratic annihilator、**原给定 slab-Frostman π**及原 correlated g；输出是全部 vertical quadratic fits。其基础仍是有限插值与Fubini，不把 elementary degree extension称新颖或重大。

实际用途的新增 gate 是：若 mixed43 确有同一 original angle-difference prior 满足 (3)，而且 vector nonquad已在这个原 time frame 中给 (2)，则可以选择**实际角差**而非外加generic projection，保其原 g mean。此处 hidden Y 本来就是标量，未通过投影丢掉二维 Y 的 deficit。

但本文件不证明 original coarse Φ 的 unused cells 有 slab law，也不把 ell2 AFF001 自动当成 ell3 准备。actual τ 的 vector选择、coefficient rescaling、source small/large-τ误差、fine/coarse选择与 named scalar projection inputs仍须逐项支付。有限结论通过不等于完整 N5-MIXED43-NQ01、五维 sticky 或 Hausdorff 完成；这是本文件的停止范围。
