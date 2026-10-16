# R0026：large-τ conditional 应用独立审查

2026-10-17，`audit_four_dimensional`。审查对象为 root 的 `notes/40_multiscale/sticky_mixed/R0026_conditional_large_tau_exclusion.md`，并对照 `R0026_global_vector_tau_gate.md`、R25 scalar-Y coarsening/代表选择及原 WZ13.5、22.1、22.5。结论：**通过，可在文末所列具名输入和准备条件下归档**。审查中指出的 13.5 平移反号及 clock error 指数责任已由 root 明确补入终稿。

本审查者参与本轮源审计及 global-candidate 思路，故自有 `R0026_global_tau_source_audit.md` 不算对其自身的独立认证；global finite 主稿由 B 另审。这里独立核 root 的 source integration、角选择、空间/time 归约及定理参数。没有重证 named Theorem13.5 的整段高级证明。

## 1. 先验、时间删选及重建 g：通过

root 保持单一原基准 Z、dyadicρ partition、vector E 与全局 T_j；physical nonquad 的分母也明确是同一个 Z∩J。若从更早母集继承 nonquad，retention cost 须预先进入质量阈值，终稿没有免费重置这一分母。

global gate 删除的是整窗口及整时间层，所以保留每层 E_z、Y/X、Φ、原 witness 和 T；R22 time closure 的适用范围正确。它不声称旧 g 自动保密度，而是在合法剩余数据上重新选择 good-q、重建原 L graph。`m_q≥K^-1 m_J` 后，窗口 nonfit 质量 β 在 q 中变为 **Kβ**；large 稿已计入这一损失。

同一个 window-canonical F_row 在空间 q 选择前定义，anchor 不需要属于 Z(q)。代数上 `h_c=v-b(c)u` 是全 time 函数；对应有界坐标剪切保持水平 grain 的 scalar Y-label，并不需要 q 在 c-time 有 marked point。其 E 恒等式在该 q 的所有实际 times 上仍成立。τ 也未在选择 ψ 后重新定义。

## 2. global τ 与真实 L-count：通过，有原计数依赖

WZ22.1 的 (179)（原 PDF95、5005–5024）仅要求 E≤cτ/ρ。proof 使用它使 V-tuple 两个中点的 y 差为 O(τ)，随后以原 full horizontal grain 和 τ-coherence 作 Cauchy–Schwarz；没有“所选 q 必须达到 global τ”的下界条件。

因此 τ 取 T_j 的足够大固定倍、再允许格向上取整是合法的 upper parameter。`K^-1T_j≤τ≤KT_j` 的费用进入 K；原 δ≤τ≤ρ 由 large 下端、global Lip upper 与后取小 loss 成立。局部 E 远小于 τ/ρ 不破坏该 upper 条件。

计数的 marked-degree 下界仍依赖 R16/R24 已付的原 weighted averaging，不能对每条原 T 假设有 m_q 个 marks。large 稿仅调用这些原接口，没有重新赋管子 AD 或改用任意无方向 tube family。原高级计数未在本 review 全量重证。

## 3. 删除 G 的 mesh、norm 和物理底层：通过

原关系有误差 `O(Kτρ+δ)`。u 的 affine 主项乘 b 本尺度差给被删除项的 scalar-Y raw error `O(K³ρ³)`，故除 τ 后必须用

`e_L=K^C[ρ+ρ³/τ]`。

root 没有沿用 R25 的 ε₀-controlled 细 mesh。τ≥K^-1ρ^(3-ζ₁) 给 e_L≤K^Cρ^ζ₁；同步空间除 L 后 `w=e_L/L`，后小 loss 保 `ρ²≤w≤ρ^(ζ₁/2)`，正确。

scalar-Y physical base 为 `r₀=δ/(τL)`，`r₀≤w` 等价于 δ≤τe_L。因 δ≤ρ⁴ 且 e_L 含 K^Cρ³/τ，该界有严格余量。time base d=δ/ρ 也远小于 w，因为 w≥K^-Cρ、`δ/ρ²≤δ^(1/2)`。所以空间 AD packing、ν interval cap 的全部 working queries 都合法。

L 同时作用于 A_input/out 与 Fψ，关系误差确为 O(w)。F/G amplitude 的 K 费用没有在 round clock 时隐去；large 稿在 unit norm 后才做这一步。

## 4. 同原角 law 的三点 affine gate：通过

已核 (3) 的有限推导：

1. ν 的最大 position atom≤K_t d。若一个 scalar fit mass≥b_s，且 `b_s≥C K_t d`，则其 distinct-time triples 的质量至少 b_s³/2。
2. 三点 Vandermonde null weights 按最大绝对值归一。选中的 coefficient 为 1，其余两个绝对值≤1；scalar affine 项精确消去。因此 scalar residual≤3σ，不出现 time-gap 倒数。
3. 固定另两 times 后，vector residual≤h 是 F_row 命中一个真实 row affine fit，质量≤a；对三种最大 index 求和至多 3a。其余 residual≥h，由 **原 π** 的 slab law 支付 `K_ψ(3σ/h)^γ`。低于 base 时扩大到 q_base，超过 1 时用质量≤1，均已写入公式。
4. `h=K^-Cρ^A`、σ=ρ^(2A) 的 ratio 可由合法 `Q=Cρ^(A-smallloss)` 查询，Q≥Cρ。两项指数 `b-3v-smallloss` 与 `γA-3v-smallloss` 在 v 先选小、η_j 后小下均为正。
5. π 是原 used-heavy angle cells 的差先验，g 任意相关。Bad 只从 product reference 删除质量，g≤1 给 graph loss 上界；Bad probability<mean(g)/4 后，同一次选择有 positive good proxy-angle graph fibre。没有假设 g 的角边际也有 slab cap。

选择所得 Fψ 对所有 scalar affine p 有 **unweighted** precision σ nonfit；不需要在这里假称 weighted-affine 或 quadratic 版本。

## 5. scalar-Y 空间 coarsening：通过

R25 的操作适用于新的 τ、e_L：它只需要原 full scalar Y 的两侧 AD、已付 input patch fine-total lower、目标常数扩大 patch 的 cover 与 r₀≤w，不依赖旧 ε₀ mesh 的具体表达式。

occupied working-cell cover 使用 full-Y AD lower 的 disjoint-ball packing加扩大 patch AD upper，未从 fine-point upper 单独推出。fine容量 upper 与 heavy occupancy lower 使余下 bin 权重相对 Uniform(A_minus) 有双向 K^C 比较；删轻 bins 的 g-loss 由 g≤1 支付。input lower 及 target cover 得到 target/input ratio≤K^C。

因此 (5) 的 A_minus cardinal deficit、mean(g_c) 和 A_plus ratio 均有真实原权重来源。κ_engine=min(κ/2,1/2) 留有吸收所有 K 的固定亏损余量，也包含 κ=1 的零维 scalar-Y 边界。没有给裁切 patch 免费 AD lower。

## 6. unweighted affine 的同 F 抽样：完整检查通过

本节是 R25 之外必要的桥，root 已单独证明，不能仅引用 weighted-quadratic sampler 的名字。

- 删除质量 p_i<c m w 的轻 time cells，总 ν loss≤m/100；prepared uniform-cell mixture 相对保留原 ν 的 density在 `[c/K_t,C K_t/m]`。graph 两 time mean≥c m/K_t²。抽样同 cell 的 diagonal置零只损1/N；其余 distinct cells 独立。bounded mean有≥c m/K_t² 的 good-graph 概率。
- 在 uniform clock B 上，interval cap由 `N≥c/(K_t w)` 给出。一个 q-rich h_c-affine fit（q=w^(v/10)）有两个距离≥c q/K_t 的时刻；因 q≫K_t w，合法查询不会落到 base 以下。unitbounded F 限制其 slope≤C K_t/q，intercept同界。
- 这个系数 box 只依 q,K_t，虽由“存在 rich fit”推导，却不依随机代表的具体取值。故可预设统一 mesh h_c/20，cardinality≤`C[K_t/(q h_c)]²`，不需要对无限 coefficients 或 #fine labels 作非法 union。
- root 现明确 `e<1/4,v<1/10`，loss 后小满足 `1-v/10-timecaploss>e`。所以 clock→原time 的 affine error `h_c+C K_t w/q≤2h_c`；再加 net error仍≤3h_c。`4Lh_c≤σ` 使其成为原 (4) 可查询的 fit。
- prepared expected fine-fit频率≤`C K_tρ^v/m`。由 w≥ρ²，q≥ρ^(v/5)，故 expectation/q≤`K^Cρ^(4v/5)`，η_j≪v 时确实≪1/4。Hoeffding的 `Nq²≥w^(-1+v/5+smallloss)` 胜过 polynomial net 与固定小幂 graph probability。
- 因此有同一组实际 F/time representatives同时保 graph 和全部 affine q-nonfit。round clock只改 time prefactors，原 positive relation仍有 O(w) error。prepared B 是一个经过证明的新 finite frame，不声称代表集还带旧 ν 的 atomic mass。

## 7. Theorem13.5 与参数顺序：通过

原定理 PDF52，2712–2724：第一 threshold `η_reg(α,β_time,γ_C,e)` 不依 nonfit mass 指数；graph/output threshold 另依 ε₂。root 分别以 `α=1-κ_engine, β_time=1, C={1}, γ_C=0, ε₂=v/10` 支付它们，符合原文。

原 drop-G expression 是 `(s-t)[F(t)-F(s)]`，与 (79) 反号。终稿现明确取 `F̃=-F`，unit norm与 all-affine nonfit不变，C仍为合法 {1}。故不存在偷偷用不在[1,2]中的 C={-1}。

先依 κ_engine 固定真实 named允许的 e<1/4，再取 ζ₁、A=ζ₁e/100、physical ε₁≪A。由 w≤ρ^(ζ₁/2)，有 `Lw^e≤K^Cρ^(ζ₁e/2)≪ρ^(2A)=σ`。随后 ε₂phys、terminal η_M、各 b_j/v 与更小 η_j 按 backward hierarchy 固定；所有原 AFF/source loss最后小。η_j 可以依 v 再小，不存在 graph threshold 反向要求先固定 v 的循环。

global稿亦已把 ζ₁ 加上 R25 middle engine 的 ε_quad 兼容限制，因此同一稳定 j 落 middle 或 large 时可使用同一组参数；不把两个参数表各自存在误当可以同时存在。

g threshold成为真实 dense set G、output-error的固定邻 cell覆盖、固定 box缩放只付常数/小幂。13.5给 `#A_minus≥w^-α`，而 (5) 给 `#A_minus≤K w^(-1+κ)`，κ_engine<κ 的固定差足以吸收 K，矛盾成立。

## 8. 最终 scope

本 review 认可在 **whole-matrix AFF₃、同基准 row nonquad、具名原 geometry/counting/闭包及 scalar13.5** 输入下的 actual large-T_j alternative 排除。与 R25 middle 及本轮 tiny端论证结合，只得到**带准备的 mixed43 非二次分支**排除。

未证明 AFF₃ 的来源、非二次 alternative 必得、mixed43 quadratic、其他五维分支、general-to-sticky或 Hausdorff。高级 Theorem13.5 未全量独立重证。没有新维数界、真实 Kakeya 反例、重大性或新颖性认证；长期 Goal 未完成。
