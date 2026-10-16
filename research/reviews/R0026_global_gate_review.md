# R0026 独审：全局 vector-τ 质量门槛与大τ应用

2026-10-17，`lifting_obstructions`。独审 root 的 `R0026_global_vector_tau_gate.md`、`R0026_conditional_large_tau_exclusion.md`，并交叉核 A 的 `R0026_global_tau_source_audit.md`。本轮自身有限反攻在 `R0026_global_tau_counterattack.md`，其 weighted 原质量证明独立得到同一主门槛。

**结论：主有限 global gate 通过；大τ排除在明确的 whole-matrix AFF₃、同基准 physical vector nonquad、合法原时层闭包及具名原计数/13.5 输入下通过。** 未证明 AFF₃ 的存在、完整 mixed43、五维或一般 Kakeya。高级 WZ 证明未在本轮全量重证，无新维数界、真实 Kakeya 反例或重大/新颖性认证。

## 1. 审查对象、原质量与候选族

固定同一个原 time 集 Z、同一 dyadic ρ-partition 及同一个 residual

    E(z,s)=v(z)−v(s)−b(s)[u(z)−u(s)]。

原 nonquad 分母为 `#(Z∩J)`，global minimum 的门槛为 `δ^η_j #Z`。root 已明确：若 AFF 后 Z 是更早母集的删选，必须先付原窗口 retention 比例；不能在 nonfit 的右端免费换成当前集合。这一条件对实际结论必要，当前稿保留了它。

T(S) 只比较同一固定 J 中的 pairs；δ-floor 保留。下一候选族包括全部达到质量门槛的原 time subsets，故按各个 J 选不同 anchor/affine fit 后取 fibre 并，确是合法候选。有限 Z 保证 minimum 取得；不需要控制拟合系数、窗口数或 fine time 总数。若改成 sliding pairs、强制保留每个窗口或固定某个 q，则这一步不成立；当前稿没有这些改变。

## 2. rich fit、physical nonquad 与 vector 收缩：通过

先删 `#(S_j∩J)<λ #(Z∩J)` 的轻窗，总损失至多 `λ #Z`。其余窗的 rich fibre W_J 满足 `#W_J≥β #(S_j∩J)`，所以 `βλ>ρ^ε₂` 才能调用原 nonquad，不能仅凭当前窗中的相对丰富性。

对同窗实际 anchor c_J，`F_J=(ρ/T_j)(h_cJ−h_cJ(c_J))`。由 global 定义直接 `|F_J|≤1`，无须要求 c_J 属于以后所选 q。affine fit 的物理 slope 为 `A₁=T_j R/ρ²`，raw error 为 `(T_j/ρ)ξ`。若这个 upper 不超过原 coefficient-weighted 允许误差，整条 rich fibre 就违反原质量 cap；因而它严格大于允许误差，得到 `|R|<ξρ^(−ε₁)`。这一推导适用于所有 real row 系数及零 slope，不是假定某一坐标非零的标量推导。

原恒等式给同 fibre 内

    ρ|E(z,s)|≤C T_j ξρ^(−ε₁)+K²ρ³。

取 `ξ=ρ^A`、`ε₁<A/10`、`A<ζ₁/10`、large 下端 `T_j>ρ^(3−ζ₁)`，再使原 K-loss 后小，确有 `T(W)≤ρ^(A/2)T_j`。δ-floor 也已核：`δ≤ρ⁴`，所以 `δ/T_j<ρ^(1+ζ₁)`，比所需 `ρ^(A/2)` 小。固定常数由严格正幂余量吸收。

若各 bad 窗的 fibre 总数达到 `δ^η_(j+1) #Z`，它们的并与稳定比值冲突；否则 bad 窗的完整当前质量至多 `δ^η_(j+1) β^(−1)#Z`。删的是整窗，因此保留窗的当前 fibre 没有进一步相对损失；后选 good-q 若只占该窗 K⁻¹ 比例，nonfit cap 必须为 **Kβ**。root 已写明这一费用。

这是保原质量的全局二择，不是从一个 q 的 rich fit 直接推 global τ 缩小。未找到满足上述全部假设却破坏该结论的有限模型。

## 3. tiny 端、2/M 稳定与参数次序：通过

若某 `T_j≤ρ^(3+2ε₁)`，按原窗口质量加权平均，可找 `#(S_j∩J)≥δ^η_j #(Z∩J)` 的 J。实际 anchors 及 whole-u AFF 给同一 row affine fit，error 为

    O(ρ^(2+2ε₁)+K²ρ^(2+ε₀))≪ρ^(2+ε₁)。

条件 `2ε₁<ε₀`、原 loss 足够小、`η_j≪µε₂` 保证质量超过原 nonquad 上界。实际 c,s 均来自该原窗，无额外 anchor 量词。故全部有限层都有 `T_j>ρ^(3+2ε₁)`。

另一方面 `T_0≤Kρ²`。若 M 个相邻比值均小于 `ρ^(2/M)`，则 `T_M<Kρ⁴`，与上述低端冲突。以 2/M 代替没有端点余量的 1/M 正确；取 `M>16/A` 后，又有 `A/2>2/M`。j 的索引只需包含 0 到 M，未超出有限链。

写 `ρ=δ^s`、`µ≤s≤1/4`，root 的两个费用分别为

    βλ=ρ^(b_j+2η_j/s)>ρ^ε₂，
    δ^η_(j+1)/β≤δ^(η_(j+1)−b_j/4)≪δ^η_j。

先定 terminal η_M，再取 `b_j=η_(j+1)/100`，最后向后选 η_j，能同时满足这些式及后续依 b_j 的高级阈值。不能先随意用 sqrt-recurrence 再声称任意依赖都可付；当前稿没有这样做。named13.5 的 e 和 R25 engine 精度先固定，ζ₁、A、physical ε₁随后固定，原 source/AFF loss 最后小，未见循环。

## 4. 原时层、good-q 与 global τ 使用范围：通过其具名接口

R22 time restriction 的对象是保留层的全部原点、Y/X/Φ、witness 与原 T；并非任意空间或管子子族。跨时间 union 的 lower 来自保留的完整单层 Y 的 AD lower，upper 来自旧 union，allowed-scale 换格需计入 K。这一闭包与当前删整 time/整窗相容。

旧 g 可以全部集中于被删窗，time 质量不推出旧 g 的存活。root/A 已明确在合法剩余配置重新平均 good-q、used-cell angle prior 和 L 图。A 稿对再删 time 绝对质量过小的窗也给了损失：至多 C/ρ 个窗，每窗低于 `δ^(Bη_j)ρ/δ`，总损失可小于保留的 global time 质量。

直接对照本库 WZ 原文 22.1 的 (179) 及其证明，条件只为 `|E|≤cτ/ρ`。中点 y 差 O(τ)、horizontal grain 选点及 τ-coherence 计数都不要求当前 q 的 sup 达到 τ/ρ。因此取 global T_j 的足够大 fixed/allowed 向上倍数可用；取整费用保留在 K。large 范围内 `δ≤τ≤ρ`，不需要假设 `τ_q≈T_j`。

R16/R24 原 good-q 与 used-angle recovery 的完整高级计数沿用已审接口；本轮核的是其所需 upper、母集与时层质量相容，不声称重新证明全部源几何。

## 5. 诚实 mesh 与三点原角 gate：通过

删除 G 的代价是 `K³ρ³/τ`；不能继续用带 ε₀ 的旧误差代替它。root 取

    e_L=K^C[ρ+ρ³/τ]， w=e_L/L，

并同步除 L 缩放 input/output A 和 F，正确保留幅度。后小 loss 下 `ρ²≤w≤ρ^(ζ₁/2)`，time base `δ/ρ≪w`，physical spatial base `δ/(τL)≤w`；δ-error 未丢掉。

三点 gate 的 max-normalized Vandermonde 系数可消去所有 scalar affine fits，归一后每个系数绝对值至多 1。按最大系数的位置分三类；固定其余两时刻，小 vector residual 事件就是同一个 vector affine fit，原质量至多 a。distinct rich triples 的质量至少 `b_s³/2`，只需 `b_s≥C K_t d`；没有无偿的 time-gap 倒数。

大 residual 通过原 ψ-law 的 slab cap 估计。source 只给 `q≥Cρ`，当前稿用合法查询 `Q≥max(Cρ,3σ/h)`，且 Q≤1；没有把 raw 查询的下界或 Kψ 的幂免费抹掉。坏角按原 reference 概率计费，g≤1 支付与 g 的任意相关性，再选同一 good proxy angle pair；不声称选中了固定 exact fine angle pair。

## 6. affine time sampler：通过

这是独立 uniform-affine sampler，而不是将 R25 weighted-quadratic 结论改名。原 ν 的 w-cell 最大质量为 `K_t w`；删质量小于 `c m w` 的 cell 只损 O(m)。剩 N 在 `[c/(K_t w),C/w]`，uniform-cell prepared mixture 相对原 ν 的密度在 `[c/K_t,C K_t/m]`。故其 graph mean 至少 `c m/K_t²`。随机每 cell 选一个原 time/同 F 值，diagonal 的 1/N 后小可忽略；bounded 随机 graph mean 有至少 `c m/K_t²` 的成功概率，不需假定其 concentration。

需要统一防止所有 adaptive affine fits。若 sampled clocks 上有 q-rich `h_c=w^e` fit，uniform cell 数的 interval cap 给两点距离至少 `c q/K_t`；unit F 因而迫 slope/intercept 在固定 box `C K_t/q` 内。time 取整误差为 `C K_t w/q`。现稿显式取 `e<1/4`、`v<1/10`、`q=w^(v/10)` 及最后小取 loss，所以该误差确小于 h_c。

在该 box 作 h_c-net，card 为 `O([K_t/(q h_c)]²)`。事件查询的 fine 误差 3h_c 在 `4L h_c≤σ` 下属于原 scalar nonfit 范围。prepared expectation 至多 `C K_t ρ^v/m≪q/4`；独立代表给 Hoeffding，`Nq²≥w^(−1+v/5+smallloss)`，有限 net 总坏概率超多项式小，可小于 graph 成功概率。所有 fitted coefficients 都被同一个预定 box 覆盖，没有对 fine index 总数求和，也不需要 F 连续或 Lip。

同一代表同时保 graph 和 nonfit。随后只移动 clock、保原 F 值，unit norm 使 S 误差为 O(w)。prepared Uniform(B) 并不保旧原子质量，当前稿没有作此错误声明。

## 7. named13.5、精度与结论范围：通过

对照原 Theorem13.5 statement，C={1}、γ=0 合法；其 regularity η₀ 不依 nonfit 质量指数，而 graph 阈值 barη₀ 依该指数，当前稿分开支付。先依 `α=1−min(κ/2,1/2)` 固定充分小 e，再选 `A=ζ₁e/100`，有

    Lw^e≤K^Cρ^(ζ₁e/2)≪ρ^(2A)=σ。

这同时支付 sampler 的查询精度。K 的全部固定幂和 graph loss 最后小到两个不同阈值之下。near-output 的有限相邻 cell cover 只增固定常数。13.5 推出的 `#A_minus≥w^(−α)` 与真实 scalar-Y upper `K w^(−1+κ)` 之间有固定 κ-buffer。

原 drop-G translation 的时间符号与13.5相反；现稿已明确用 `F̃=−F`，norm 与 all-real affine nonfit 不变，仍取合法 C={1}，没有使用不在[1,2]的 −1。

空间 heavy frame 沿用 R25 已证 full-Y AD lower/upper packing、bin 容量及同原 g 平均；没有给任意裁切 patch 新 AD lower。上述审查确认该操作在新 τ、诚实 w 和同步 L 下仍可用。

由此，large 分支可在已列准备下排除；与 R25 middle 分支和 tiny 端相接的参数余量也已明确列出。**通过范围仅为带 whole-matrix AFF₃/原 nonquad/具名源输入的条件排除。** 不能据此宣布已得 AFF₃、所有 alternatives、完整五维，或将本轮有限质量引理当作长期 Goal 达成。
