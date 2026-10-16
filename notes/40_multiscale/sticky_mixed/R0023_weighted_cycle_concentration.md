# R0023：原加权四环的点球上界与近直线提取

2026-10-17。主任务 N5-MIXED32-NQ01 的有限接口。以下证明保留同一个原 time probability，不用独立卷积替代图，也不把 vector nonquadratic 解释为每个 scalar projection nonquadratic。它们限制一部分退化情形；没有得到排除 actual mixed32 非二次 alternative 所需的二维增长。

## 1. 原权有限设置与恒等式

B 是 [-1,1] 中有限带权时间集，概率 ν 满足：对长度 |I|≥d 的每个区间，ν(I)≤K_t |I|。K_t≥1，d>0 是原时间分辨率。F,G:B→R² 可任意粗糙；不假设连续或欧氏 Lipschitz。假设对于每个 vector quadratic P(t)=p₀+p₁t+p₂t²，

    ν{t: |F(t)−P(t)|≤h} ≤ a.                         (NQ)

0<h≤1，0<a≤1。这个 uniform h 条件可以由 small-τ 分支的 coefficient-weighted nonfit 缩弱获得，实际转换另见 source audit；large-τ 不自动具有该接口。有限定理本身不需要 F/G bounded，source normalization 则需要。

定义

    S(t,s)=(s−t)[F(t)−F(s)−G(s)(t−s)],
    Q=S(t₁,s₁)−S(t₁,s₂)−S(t₂,s₁)+S(t₂,s₂).

置 Δt=t₁−t₂、Δs=s₁−s₂，直接展开给

    Q=Δs[F(t₁)−F(t₂)]
      +Δt[F(s₁)−F(s₂)−2s₁G(s₁)+2s₂G(s₂)]
      +(t₁²−t₂²)[G(s₁)−G(s₂)].                    (1)

因此 V(t)=(t,t²,F(t))∈R⁴、U(s)=[F(s)−2sG(s),G(s),sI₂]∈Mat(2,4) 确有 Q=(U(s₁)−U(s₂))(V(t₁)−V(t₂))。式(1)比“rank 至少多少”的说法更有用：固定 s₁,s₂,t₂ 后，Q 对 F(t₁) 的系数正是非零标量 Δs。

## 2. 小球质量：同一 cycle prior 下的严格结论

若 g₀≥d、e≤g₀h，对每个 q∈R²，

    ν⁴{|Q−q|≤e} ≤ a+2K_t g₀.                       (2)

这里 g₀ 是时间间隔参数，与平移图 g 无关。

证明：|s₁−s₂|≤g₀ 的概率至多 2K_tg₀，因为固定 s₂ 后查询长度2g₀的区间。其余 s₁,s₂,t₂ 固定时，把(1)中的 Q 替换为 q 并除以 Δs，得到唯一 vector quadratic P(t₁)。|Q−q|≤e 强迫 |F(t₁)−P(t₁)|≤e/g₀≤h，故其 ν-质量≤a。对剩余变量积分即得(2)。没有以 Q 的边际分布重新设独立性。

特别地，任意 0≤c(t₁,t₂,s₁,s₂)≤1、D=∫c dν⁴>0，按原权定义 μ_c=Q_*(cν⁴/D)，都有

    μ_c(B(q,e)) ≤ D⁻¹(a+2K_tg₀).                  (3)

c 可以是原 dense graph 的四环、其任意删选或 soft weights。由 M 个 e-balls 覆盖全部 c>0 的 Q 像，则

    M ≥ D/(a+2K_tg₀).                              (4)

选 g₀=max(d,e/h)（若该值>2则结论只是平凡上界）得到显式 cap。小球分支要被排除，必须实际有 D>a+2K_tg₀；不能忘掉 D⁻¹。

## 3. 只有大量 cycles 近同一 affine line 时能提取什么

现设 H⊂B×B 是原 bipartite graph。c 的支集包含于其四环：c>0⇒H(t_i,s_j)=1 对所有 i,j。假设 D=∫c>0，且 c>0 时

    dist(Q,q₀+L)≤e,                                (5)

L 是固定一维线性子空间，q₀+L 可为 affine line。取参数

    r=√D/4，g₀≥d，2K_tg₀≤D/8，e/g₀≤h/4.          (6)

则存在 T⊂B、m=ν(T)≥3D/4，及单位法向量 n⊥L、scalar quadratic p，使

    |n·F(t)−p(t)|≤e/g₀  对所有 t∈T；              (7)
    ν{s:H(t,s)=1}≥r  对所有 t∈T.                   (8)

对 L 上任意单位向量 ℓ，每个 scalar quadratic q 满足

    ν_T{|ℓ·F(t)−q(t)|≤h/4}≤a/m≤4a/(3D),           (9)

其中 ν_T=ν|T/m。同一 conditioned prior 满足区间 cap K_t/m，不把它当新的免费均匀时间集。

证明：记 k(t)=∫H(t,s)dν(s)。删去 t₁ 或 t₂ 满足 k(t)<r 的 c-tuples。固定一个这样的 t，两个 s 均属于它的邻域，故这类四环的原质量至多 r²；两端合计≤2r²=D/8。这是对四环用 degree 的平方，并非拿边密度估计任意 cycle 权。再删 |Δs|≤g₀，损失至多2K_tg₀≤D/8。剩余 c_* 原质量≥3D/4。

Fubini 先给一对 |s₁−s₂|>g₀，使 ∫c_*(t₁,t₂,s₁,s₂)dν²≥3D/4，再给某个 t₀，使 ∫c_*(t,t₀,s₁,s₂)dν(t)≥3D/4。令 T 为这个函数的正支集；因 c_*≤1，有 m≥3D/4，所有 t 的 row degree≥r。由(1)、(5)，

    |Δs[n·F(t)−n·F(t₀)]
      +(t−t₀)n·[F(s₁)−F(s₂)−2s₁G(s₁)+2s₂G(s₂)]
      +(t²−t₀²)n·[G(s₁)−G(s₂)]−n·q₀|≤e.

除以 Δs 即得(7)，常数 n·q₀/Δs 被纳入 p₀，不需要声称 affine line 通过0。若 scalar q 的 h/4-fit 在 T 上成立，则 vector polynomial ℓ q+n p 对 F 的误差≤√2 h/4<h；用(NQ)即得(9)。这没有声称所有 scalar projections nonquad，只产生一个经过质量付费的方向。

## 4. 保住原平移图能得到的预算，以及不能得到的结论

令 A 带原概率 σ，原 0≤g(a,t,s)≤1，并以

    H={(t,s): ∫g(a,t,s)dσ(a)≥λ}, λ>0

构造上述 graph。T 的每一行都有 degree≥r，因此

    ∫_{A×T×B}g dσdνdν ≥λrm≥(3/16)λD^{3/2};      (10)
    ∫g dσdν_Tdν≥λr.                               (11)

A 及其 AD/tube-KT 输入完全不删。H|T×B 用新 prior ν_T×ν 的 edge density≥r，所以 Cauchy–Schwarz 两次给其完整四环相对质量≥r⁴=D²/256；其原 ν⁴-质量≥m²r⁴≥9D⁴/4096。这里得到的是 H 上重新生成的四环，不是原 c 在 T²×B² 上必保这些质量。

必须保留下列三项限制：

1. 由 F 的一个 normal component 近 quadratic，并不能推出 S 或原 translations 近 L。right carrier 上的 G(s) 未受(7)控制。MNL-001 的 linewise translations 假设仍未获得。
2. 原 c 不保证在 T²×B² 上仍 dense；重新生成的 H-cycles 不保证继续满足(5)。不能把固定 s₁,s₂,t₀ 的 Fubini 选择写成原四环 prior 的无损闭包。
3. scalar ℓ·A 可以有满一维投影；A 的维数2−κ及 absolute tube-KT 并不直接给投影维数<1。因此(9)本身不足以接 scalar Theorem13.5 或22.5的原标量基数矛盾。left carrier T 与 right carrier B 也不同。

上述限制是真正剩余接口；(2)–(11)不声称付清它们。

## 5. actual mixed32 应用范围

原 L relation 空间缩τ、时间缩ρ，产生原 fine-index ν、vector F/G 和工作误差 w。小τ分支中源(200)的 vector 版本给 h≈K⁻Cρ^{2ε₁+ζ₁} 的 uniform quadratic cap a≤K^Cρ^{ε₂}/θ（θ是此前实际 retained mass，另有 angle/K费用）。之后应在实际 θ/η 次序下选 g₀=max(d,w/h)，检查 2K_tg₀≪D；有限公式没有删除这些费用。

这些检查在 small-τ 的原 weighted graph 上确可支付点球退化：δ≤ρ⁴ 给 d=δ/ρ≤ρ³；ρ^{3+2ε₁}<τ≤ρ^{3−ζ₁} 给

    w/h ≤K^C[ρ^{1−2ε₁−ζ₁}+ρ^{ε₀−4ε₁−ζ₁}].       (12)

先选 ζ₁+4ε₁<ε₀ 且 2ε₁+ζ₁<1，以上两幂都正。这里直接从原 bounded L-graph g 取 H={(t,s):E_Ag≥(E g)/2}，不使用尚未付的 vector BSG。H 的 edge density≥K⁻C，故 Cauchy–Schwarz 给原 full-cycle mass D≥K⁻C；B 不粗化。K 含已经实际支付的 η/τ-stability/retention losses，不能视为绝对常数；AFF loss、原 η 以及有限 stability chain 的 loss 需要在 ε₂ 和(12)正幂之后选得足够小。此时 a+2K_t max(d,w/h)<D，(2)严格排除全部这些原cycles的 Q 像落入一个 w-ball。使用 c 作后来进一步删选时，必须重新核其 D 的预算，不能一概继承。

这排除“全部原 dense cycles 的 Q 在一个 w-ball 中”这类强退化，并把任何给定 dense-cycle common-affine-line 分支化为有真实质量的部分 scalar nonquad 模型。它没有二维 cover exponent、translation gain 或 κ>ζ 矛盾。S/G 的原图分支与 higher-dimensional restricted projection 仍需新输入；原 fine B 不自动 w-separated。

本轮不新增维数界，不把 elementary Fubini/CS 引理列为重大或已认证新颖结果。NQP-001只登记这些原权接口；N5-MIXED32-NQ01保持 open。
