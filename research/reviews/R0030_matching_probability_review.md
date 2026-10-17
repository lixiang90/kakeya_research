# R0030 独审：general matching proof 与完整反攻模型

2026-10-17，审查者 `/root/lifting_obstructions`。逐段读取 root `R0030_matching_full_proof.md` 和 A `R0030_matching_counterattack.md`，并对照 OAI4 §3.2 PDF29–35；不是将作者自审计作独审。以下审查覆盖固定一般 D、J>D、d₀<1 的完整链；本人的 prior/refresh 主稿只作为展开，不替代对 root 最终符号的独立核验。

**结论：root 的 general Lemma3.3 重证通过本次内部独审；A 的 pair upper、d=1 校准、oscillatory fixed-power 模型及只控到 D 阶的 singleton 边界也通过，其 scope 没有反驳原 subpower 或 sufficiently-small-fixed-power 引理。§5 简单模型已明确 ε<1/2 的指数范围，root 亦已补全局 entropy 预算，两项均已核修复。** 本结论未经外部同行评审，不认证整篇四维证明或无条件六维 17/4。

## 1. 尺度与 jet 前提

原 gap pigeonhole 可用固定 cutoff B>1，配合 finite logarithmic classes 只损 subpower mass；固定 J 后可取 subsequence 令 β_j 稳定。cutoff orders 只需 upper，不参与 active term；β_j=0 的某 j≤D 给 r(a)≥a/D。

对历史最大 l_j，root (3) 的两项需分别看：在 l_j 最大点 x，以 l_{j+i}(a)≥x−(j+i)r(x) 得 l_j−l_{j+i}≤ir(a)；由 J+1>D、r(x)≥x/D 得 remainder 严格 gap。active m-piece 上此前 r′≤1/m，所以 j≤m 的历史 max 正是当前 a−jr(a)；j>m 在本 piece 左移会严格增大，故其历史 max 严格大于当前值。m>D 不可能 active，因为 β_m≥0 时 (a−β_m)/m<a/D≤r(a)。

trim 后严格 gaps 有正下界；可先取 b 小、再选 grid/state/mass。因此所有 Taylor errors 真有固定正幂余量，不是把 N^{o(1)} 与 b 同时变动。nested dyadic intervals、finite earlier histories 及 child-centre translation 均合法。coarse-neighbour counts 为 fixed-grid 的 subpower，允许常数依 grid。

## 2. (6)–(8)：pre-selection 与原质量分母

一个 arm index 与 finest interval 决定它的全部 histories；另一 arm 每级只在 subpower 邻 bins 中，故 #supp F₁≤N^{d₀+r(1)+o(1)}。此处只数实际 records，不数 index pairs，更没有用 conditional independence。

设 p_pre 是 homogeneous selection 前 law。删极轻 finest atoms 后，对固定有限 levels 的原 atom masses 作 joint log-pigeonhole，可保 subpower mass并有 p_pre(F_a)=N^{-u_a+o(1)}。父原 mass≥child 原 mass，故 u_a 非减、u₁≤d₀+r(1)。原 (8) 的 child count 来自 disjoint children 的 p_pre masses 求和，完全不要求最终 normalized P 的 atom masses 均匀。

每次 restriction mass q 使 marginal ceiling K 乘 q⁻¹；前置 selections 均 q=N^{-o(1)}，可吸入 K，并保同一组原 π。没有免费换成条件 π。之后路径 kills 保留 unnormalized submeasure，不再除 survival mass。

## 3. L_a 信息扣费及明确 b^{5/4} 余量

palette 在 A₀ 的两个 m-th derivative bins 从 N^{-β_m} 细到 N^{-β_m−D₁b}，条件 entropy≤2D₁b log N+O(1)。L_a 的 expectation 是 conditional mutual information；overlap≤C 后总预算由 entropy chain rule 支配。负部≤1/e，故并非错误地将 L_a 当逐点非负。

为使 root §10 的 O_J 常数与 trim 兼容，应将至多 J 个 active pieces 的 entropy budgets**先相加**：总 O_J(b log N)，保留区间总长≥1/2 时总 steps≈1/b，所以全局平均 positive part 为 O_J(b²log N+1)。单个短 piece 的平均常数可以依该 piece 长度，但不必这样逐段估计。root 最新 §4 已明确采用这项全局汇总，修复通过。

在 b^{5/4}log N threshold 上先 Markov 得平均坏 probability O_J(b^{3/4})+o_N(1)，再用 b^{1/4} 作 step-good 门槛，排除 steps 比例 O_J(b^{1/2})+o_N(1)。这证明 root (9) 的实际 sampled-value 版本；未声称对每个 palette 都成立。每个 kernel 增加 N^{b^{5/4}}，m+1 legs 总 exponent loss 是 (m+1)b^{5/4}。root (14) 保留 C_Jb^{5/4}，全 O(1/b) steps 累加后才是 O_J(b^{1/4})，正确避免不可求和的含糊 o_b(1)。

## 4. 原 law 下的成功质量，且只在平均意义

任意 state heat-bath R_F 保 P；对 ν≤cP 有 νR_F≤cP。每个 color-index/I_a heat-bath 也保 P。adaptive color 可依完整 history/event，但以两个 kernels 的和 upper 后，raw current/refreshed marginals≤2^pP。因此所有 bad palette values 的概率用原 P 扣费合法。

对每色，bad arm atoms 的 thresholds π_i|I_a|/log N 在所有 indices/intervals 上总和为 1/log N。retained arm 的 actual denominator为其 P-mass，故 conditional time density≤K log N/|I_a|。π_i 可任意小，甚至有零权；实际正质量 arm 才参与，分母完整支付。

normalized time density B_N=N^{o(1)} 后，选择 separation 1/(B_N log N) 只损 O_J(1/log N)，且 Jacobian 仍仅损 subpower。good step 的 averaged survival≥c_J；proof 没有宣称每个 exact start 都有 survival lower，也没有将条件于 future survival 的 law 当原 law。

## 5. (10)：共同 Λ、hidden history 与 backward product

refresh 保 fine state，traversal 保 chosen index/I_a 与其 whole earlier history，另一 arm 各级 bins 为 subpower 邻居。因此 bounded legs 的 coarse states 都在 exact-start-determined 的 subpower 集合中。

对每个该 coarse state，把其 **P(Z|coarse)** 经两 deterministic control maps 推前，再对 states/colors 求和，即得同一 Λ_start，mass≤K。control maps 的精度只依 coarse earlier data、palette 和 fixed Taylor frame：palette 提供 m-th term，higher bins/余项有 trim 的 strict gap；无需 actual index 与其他 hidden data进入 control code。

给完整过去 H_p，refresh 的 law 恰为 P(.|current fine atom)。在 good palette 值上由 (9) 支配 coarse palette law；选色用两 candidate maps 的和支配，retained actual index 的新 time 用上一节支配，遂得未归一化 (10)。共同 Λ 对任意同 start 的 admissible H_p 有效。

对只依 start/displayed U,t 的非负 test，从末 step 倒推：每次 uniform kernel upper 积分后结果只依较早 displayed variables，因此下一步可再用同一 upper。hidden state 仍可影响后续事件，只因 test 已去掉 hidden success 细节且每一步 domination 对完整 past uniform，才可得到 product upper。没有断言 full event law 为 product，也没有凭 dense graph 提取大 Cartesian 域。

## 6. 真实 target、Jacobian 及 lower/upper 的接合

constant-control endpoint (11) 的 telescope 对 signed increments 仍正确。固定 controls 时 internal-time 导数为 −ΔU_p(s−s_p)^{m−j−1}/(m−j−1)!；把 final time s 同时作为输出，determinant 正是 (12) 的 consecutive ΔU 和 Vandermonde。no need internal times 与 final s 相隔；Jacobian 只需 internal times 彼此分离。regular fibers 的 isolated roots 由 fixed degree/dimension 给统一 multiplicity，允许其他 singular components存在。

normalized chain 是 nilpotent 积分系统；有限 signed legs 中 control/switch errors只积累 O_J(N^{-2b})，不需要 exp(K) 型 Gronwall。真实 final child F_{a+b} 必须用自己的 I_{a+b} 翻译 jets；其 fiber widths N^{−(1−j/m)b} 与 time width N^{-b/m} 给 α_m=1/m+(m+1)/2。simulation error N^{-2b} 比所有 widths 更小，中心随 final time 快速移动不影响 Fubini 体积。

所有可能 final children 已按 (8) 和 coarse-neighbour set 求 union，final color 也取两者。因此 target membership/separations 只依 start 与 displayed endpoint，是 §5 backward upper 的合法 necessary test，未遗漏 hidden index dependence。

每个 fixed control tuple 的 time-domain preimage measure由 area formula≤N^{o(1)} target volume；再对可能原子的 Λ^{m+1} 积分。所得 conditional upper对 exact start uniform，而 averaged survival lower才在最后按 P(start) 积分接合。因此并未将 averaged lower 偷换成 pointwise lower。推出 Δu≥bα_m−(m+1)b^{5/4}，再用 α_m≥1+1/m 正确。

fixed grid 先 N→∞，再选 b/trim 小；good-step loss、明确 b^{5/4} 误差和 omitted intervals 的总费用均→0，u₁≤d₀+r(1) 与 u₁≥1+r(1) 矛盾。不同 grids 的 homogeneous laws 不必相同，统一 upper 足够。fixed-power 版本由反例损失趋零的对角化得到，未得显式最佳 ε_*。

## 7. A 全部有限模型与必要假设校准

### 7.1 Pair upper 与 d=1

pair estimate 的每格长度 cK⁻² 使某 q-th derivative 保号且≥1/(2K)。sublevel 集可选 q+1 个相距 c_q times其测度的点，divided differences 给每格 measure≤C_q(K²/N)^{1/q}。乘 O(K²) 格后≤C_DK⁴N^{-1/D}；由第一色 marginal 和第二 list union 得 (5)。只闭合 d₀<1/D，D=1 才覆盖全部 d₀<1，scope 准确。

d=1 模型 t∼Uniform[1/2,1)、k=⌊Nt⌋、i∼Uniform{0,…,k}、j=k−i，使两个 index–time marginals 均≤4dt/N，π 两色 uniform。值误差≤N⁻¹、一阶 gap=1、高阶导数0 全成立，只违反 d₀<1。

### 7.2 简单 fixed-power 模型

Δ=K/N、m=⌈N/K²⌉、f₁=iΔ、f₂=mΔt−jΔ，用上例将 N 换 m 的 law。derivative mΔ≥K⁻¹、值误差≤Δ、两色 marginal≤4πdt。指数 m=N^{1−2ε+o(1)} 的公式在 0<ε<1/2 使用；ε≥1/2 则 m=O(1)，指数为0。A 最新稿已明确该范围，修复通过。

取 0<d₀<1 的临界 ε=(1−d₀)/2∈(0,1/2) 已足以给必要容差上界；更宽允许损失包含该实例，无需错误延长指数公式。因此该小修不改变必要边界或原引理真假。

### 7.3 一般 D,J 的 oscillatory 构造

记 L=J+1−D，ω=(K²/16)^{1/L}，A=4/(Kω^D)，Δ=K/N，m=⌊4A/Δ⌋。两 lists 为 iΔ 与 A(2+sinωt)−jΔ。phase 集 sin≥0 且 |sin(ωt+Dπ/2)|≥1/2 每周期占至少1/3，ω≥12π 保 |E|≥1/6。

在 E 上 g∈[2A,3A]，m≥16 时 k=⌊g/Δ⌋ 满足 0≤k<m 且 k+1≥cm。给定 t，uniform anti-diagonal i+j=k 的任一 color index 概率≤C/m；乘 normalized time density≤6 后，两色完整 marginals均≤Cπ_i dt。值差≤Δ、D-gap≥2/K；最高导数 Aω^{J+1}=K/4，较低导数≤此，order0≤4A≤K。全部条件逐条成立。

由 m≈N K^{-2(J+1)/(J+1−D)}，K=N^{(1−d₀)(J+1−D)/(2(J+1))} 给 lists N^{d₀+o(1)}。它只表明 existential sufficiently-small-power 容差不可任意大；K=N^{o(1)} 时 lists 指数回到1，非原反例。没有由此推出各种独立 displayed loss 参数的最佳阈值。

### 7.4 只控到 D 阶时的 singleton 边界

A 新增 §6.1 取 f₁=0、f₂=N⁻¹sin(N^{1/D}t)，两色各一个 index。0…D 阶导数均≤1，值差≤N⁻¹；在 |sin(N^{1/D}t+Dπ/2)|≥1/2 的 time set 上 D-gap≥1/2。该集合测度趋于2/3，N 足够大时≥1/4，normalized Lebesgue law 的两个 singleton marginals 均≤4dt，所以 K=4 合法。

D+1 阶导数达到 N^{1/D}，违原 J>D 的高阶 upper。故它严格否定删去全部 D 以上控制后的弱化命题，并不反驳原 Lemma3.3，也不说明原 J 最小。该模型全部相关量已核，无需数值抽样。

## 8. 验收界限

上述审查给一般 fixed-order Lemma3.3 的内部独立认证，非只 D=1 或一对函数验证；保留全部原 derivative/marginal/cardinality 假设。A 的模型帮助校准 d₀ gap、higher derivatives 和 fixed-power tolerances，不应登记为原命题反例。

Cor3.4 的 algebraic norm-to-jet/holomorphic inputs、Lemma3.5 atlas/knowledge 回传和后续 critical alternatives 仍有独立源责任。本次通过一个 matching gateway不消除 DIM-001 的完整 OAI4 条件，不认证六维无条件新界或新颖性，Goal active。
