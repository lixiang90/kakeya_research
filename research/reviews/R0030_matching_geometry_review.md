# R0030 独审：一般 fixed-order matching 的几何及真实概率接口

2026-10-17，审查者 `audit_four_dimensional`。逐式审 root 的 `R0030_matching_full_proof.md` 和 B 的 `R0030_matching_prior_refresh_audit.md`，并与原 OAI4 Lemma3.3/§3.2 对照。本人是反攻稿作者，未参与 root/B 两份 proof 撰写；反攻校准自身不计独立证明。

**结论：root 的一般固定 D、J>D、d₀<1 重证通过内部独立审查，B 的 prior/refresh/product upper 链亦通过。未发现需要修正的数学缺口。** 下文记录核验范围，尤其控制码、signed-leg Jacobian、regular multiplicity 及可求和误差。结论只认证 Lemma3.3 这一 gateway，未经外部同行评审，不认证整篇四维稿或无条件高维结论。

## 1. β、r/l 与先固定 grid

log pigeonhole 同时给有限 orders 的 gap upper，以及所有非 cutoff orders 的 lower。原 (3.5) 保某 j≤D 的 β_j=0；K=subpower 给 β_j≥0，value gap 给 β₀≥1。选固定 B>1 的 upper-only cutoff 不会进入 active maximum。

`r(a)=max_j(a−β_j)/j` 在 [0,1] 凸、非减，且有 β_j=0 的 j≤D，故 `a/D≤r(a)≤a`。其 finite pieces 的 active order m≤D：m>D 的 term 至多 a/m<a/D。不同 j 对应不同 slopes，a>0 仅有有限 breakpoints，故可裁端取 unique-active compact pieces。

对 `l_j(a)=max_{x≤a}(x−jr(x))`，历史 maximum 直接给 `l_j−l_{j+i}≤ir(a)`。在 active m-piece，r' 此前≤1/m，因此 j≤m 的 maximum 在当前 a，得 `l_j=a−jr(a)`、`l_m=β_m`；j>m 在该 piece 内严格下降，历史 maximum 严格大于当前值。用 `(J+1)r(x)>x` 得余项严格 gap，均适用于一般 fixed D/J。

因此 compact trim 后两类 gap

    l_(m+i)(a)+ir(a)−β_m，
    (J+1−j)r(a)−l_j(a)

均有正下界。先选 trim、common b 和全部 levels，再作 event mass selections，正是必要顺序。b 可依当前 β/trim 选，最终 uniform fixed-power 存在性用 diagonal argument，不需要未证的统一显式模数。

## 2. Taylor、嵌套 states 和真实 child 数

root (5) 中每项 exponent 的比较由 `l_j−l_{j+i}≤ir` 给出；Taylor remainder 由上一节严格 gap 给出。对两 arms 的 difference，event gaps 的 β upper 再给 center bins 的 K-neighbour bound。bins 的 dyadic rounding 和 nested time partitions 只损常数；加入全部 earlier history 后 states 真正嵌套。

一个 arm index 加 I₁ 决定其整个 history，另一 arm 每个 fixed-grid 坐标仅有 subpower 邻选，故 support bound `N^{d₀+r(1)+o(1)}` 正确。pre-selection uniformization 只作 finite 次 logarithmic pigeonhole；极轻 atoms 先用此 support upper 删除。得到的 u_a 是 **p_pre atom masses** 的 exponent，不是 final P 的 atom masses。

对 retained parent/children，以 disjoint children 的原 mass 求和得到 `#children≤N^{u_c−u_a+o(1)}`。即使最终 event selection 只保 atom 的一部分，结论仍成立；没有用未来 survival posterior 补一个不存在的 mass lower。u_a 非减、u₁≤d₀+r(1) 的两个方向均正确。

## 3. 控制码的显式复核：没有隐藏 index 依赖

令 t₀ 为 I_A₀ 中心、t_a 为 I_a 中心。对一个 coarse history C 和 palette z，记 c_{κ,m+i}(C) 为该 arm 在 t₀ 的 higher-jet bin centre，z_{κ,m} 为 fine m-th palette centre。可明确取

\[
U_\kappa(C,z;start)=N^{\beta_m}\left[
z_{\kappa,m}+\sum_{i=1}^{J-m}
c_{\kappa,m+i}(C)\frac{(t_a-t_0)^i}{i!}
-T^{(m)}(t_a)\right]. \tag{R1}
\]

其中 T 是 exact start 的一个 arm 在 t_a 的 J 阶 Taylor polynomial。此 U 确只依 coarse history、palette、color 和 exact start，不依另藏的 function index。

把 (R1) 与真实 `N^{β_m}(φ^(m)(t_a)−T^(m)(t_a))` 比较，误差逐项为

\[
O\!\left(N^{-D_1b}+
K\sum_{i\ge1}N^{\beta_m-l_{m+i}(A_0)-ir(A_0)}
+K N^{\beta_m-(J+1-m)r(A_0)}\right).
\]

trimmed gaps>4b、D₁>5 使其≤N^-2b。这里用的是 |t_a−t₀|≤C N^-r(A₀)，没有错用更短的当前 interval。

沿整个 I_a，chosen φ 与 start arm 的 higher-jet differences 在 t_a 由 coarse-neighbour histories 控制为 `K N^-l_{m+i}(a)`。T 在 t_a 的 derivatives 与 start arm 相等，所以同样展开 (φ−T) 得 normalized m-th derivative variation≤N^-2b。原函数各自可能有大公共 higher jet，此处必须先减 T 再使用 difference upper；root 采用了这个正确 frame。

fresh pair 的 normalized m-th gap 在其 witness time 为 N^-o(1)，active β_m 有真实 lower；将该 gap 转到控制码只增加 N^-2b。故两个候选 U 相距至少 1/K。给定前一个 U，可选其中一个距它至少 1/(2K)，常数吸收入 K 即可。不是要求每个 matrix/jet coordinate 非退化，也未假一开始就有独立控制。

## 4. switch 与 nilpotent dynamics

current event 与 refresh event 共用 finer F_{a+Cb}，old/new arms 在 fine interval 中的 jets 只差 K 邻格；running/witness times 也同在该 fine interval。由 §2 Taylor 比较，在 running time 的第 j<m 个 normalized jump≤

    K N^{l_j(a)−l_j(a+Cb)}
      =K N^{−(1−j/m)Cb}≤N^-2b。

最小 `1−j/m=1/m≥1/J`，所以 C>5J 足够。初始 start arm 与其 T 的 remainder 亦由 `(J+1−j)r−l_j>4b` 控制，故 first switch 没漏 initial error。

对 j<m−1，因 `l_j−r=l_(j+1)`，chain rule 恰给 dY_j/ds=Y_{j+1}；最后 dY_{m−1}/ds=U+O(N^-2b)。这是 fixed-size nilpotent linear system。所有 normalized times 在同一 bounded I_a 内，有限 signed legs 的 flow norms 有 fixed J bound，误差只积累 O_J(N^-2b)，不需 exp(K) 的 Gronwall。

## 5. B 的真实概率链：uniform π 或大矩形均未假设

独立核了 B §§2–8，未发现错误：

- subpower restriction 付实际分母；原 π 保留，零 π indices 为零 event mass。
- 任意 finite-state heat-bath 保 P，输入 submeasure≤cP 时输出仍≤cP。adaptive color 仅以两个 arm kernels 之和支配，故 raw current/refresh marginals≤2^pP；不是 given-exact-start 的同一密度主张。
- palette 的 entropy budget 为 O(b logN)，overlap≤C；negative log-ratio 部分≤1/e。两次 Markov 确给坏 step 比例 O(b^1/2)、每个 good step 的坏 palette probability O(b^1/4)。只 kill sampled bad values，不要求对所有 palette 点态成立。
- bad arm atom 阈值 `π_i|I_a|/logN` 在所有 i/I 上总 mass≤1/logN。retained atom 的 conditional time density 上界中 π_i 正确抵消，归一化时间后仅 subpower。separation 用 density upper 再乘 log 的**新** subpower K_sep，避免同一 K 的循环。
- 对 start 的所有 coarse neighbour states 和两个 colors 求和得到同一个 Λ，其 mass≤N^o(1)。给定完整 past，下一 refresh 的 palette 只由 fine state 条件 law 来；用上述点态 good-value domination、两个候选 U 的 pushforward 及新 time upper，得到 actual one-step subkernel upper。
- 从末步向前积分只依 start/displayed controls/times 的必要 test，隐藏的未来 survival 条件可丢掉作 upper。因此 product Λ×Lebesgue 支配的是原未归一化成功路径，而不是虚构的新独立 law。

原 π 可以任意不均匀，pair events 与 time 也可完全相关。stepwise failure 用 raw marginal 平均扣除；successful experiment 只需 averaged constant mass，不要求每个 exact start 都有 uniform survival lower。

另已实读 root 终稿 §4 的全局修补：先加至多 J 个 pieces 的 entropy budgets，再在总共 Θ(1/b) 个 steps 上平均。因此 O_J 常数不依单个 trimmed piece 的短长度；不会在最后求和时藏入一个发散的 piece-length 分母。

## 6. endpoint (11)–(12) 与 regular multiplicity

对 exact controls U₁,…,U_{m+1}，nilpotent Duhamel/telescoping 给 root (11)。该公式对 signed legs 仍成立，因 flow 的常系数 nilpotent 部分随总 signed time 组合；不需要 s₀<s₁<…<s。initial terms 只依 start 与 final s。

对每个 internal s_p 微分，得到列 `−(U_{p+1}−U_p)(s−s_p)^{m−j−1}/(m−j−1)!`。再加 final-time output s，block determinant 恰为 (12) 的 consecutive-control product × Vandermonde / factorial。只需 internal times 两两分离，和 consecutive controls 分离；final/start 与 internal time 的额外分离不是 Jacobian 公式必需。

fixed controls/output s 下，m 个低 jet 方程的 degrees≤m,…,1。Jacobian≠0 的 real 解在 complexification 中也是 isolated regular 解；经典 Bézout 的孤立解计数给至多 C_m（可取 m!）。其它 singular positive-dimensional components 可以存在，不影响 regular multiplicity upper。因此 area formula 在 success separation 域上给 `time-volume(preimage V)≤N^o(1)|V|`，无需全局 injective 或 coefficient-size compactness。

## 7. child targets、逐步误差和 fixed-grid 总和

每个 child 必须用其自己的 I_c 中心及 jet bins 翻译。Taylor bin uncertainty 给第 j<m 个 fiber width `K N^{−(1−j/m)b}`；final-time width 为 N^-b/m，故单 child volume exponent 为

    α_m=1/m+Σ_(j=0)^(m−1)(1−j/m)
       =1/m+(m+1)/2。

target centre 可随 final time 移动；Fubini 只积分 fiber widths，无须付 centre velocity。simulation N^-2b 小于最细 target width N^-b，可吸收。真实 child count、coarse neighbour 数和两 final colors 给 total target volume `N^{u_c−u_a−α_m b+o(1)}`，该 union 只依 start/displayed endpoint，不再含 hidden final index。

product-kernel upper 每个 leg 付 N^{b^{5/4}}。对固定 controls 用上一节 area bound，再积分 Λ^{m+1} 的 subpower mass，得 success upper

    N^{u_c−u_a−α_m b+(m+1)b^{5/4}+o_N(1)}。

和 constant averaged success lower 比较，先 N→∞，即 `u_c−u_a≥α_m b−(m+1)b^{5/4}`。由于 α_m≥1+1/m，得到 root (14)，**每步错误为 C_J b^{5/4}**。

对 O(1/b) 个 disjoint main steps 求和，总错误 O_J(b^{1/4})；good-step 缺失的 O(b^{1/2}) 比例因每步目标≤2b而只损 O_J(b^{1/2})。trimmed ends 和 a+Cb 留白另损 O_J(trim+b)。其它 increments 非负，可忽略；固定 grid 的所有 o_N(1) 在先取 N→∞ 时消失。故 `u₁≥1+r(1)−o(1)` 与 `u₁≤d₀+r(1)` 真正矛盾。不是把任意 o_b(1) 累加，也不要求不同 grids 的 u_a 属于同一个 law。

## 8. small fixed powers、反攻及认证边界

root 用 negation/diagonal 从不存在 subpower countersequence 推出存在足够小 fixed-power tolerance。这个逻辑要求失败时能选任意大 N；其 uniform statement 正是这个量词，所以成立。没有给 η(D,J,d₀) 显式或线性模数。

本人的 fixed-power oscillator 在 `ε=(1−d₀)(J+1−D)/[2(J+1)]` 达到合法例子，说明 tolerance 必须真正依阶数/gap，和 root 的 existential 更小 tolerance 不冲突。B 指出的简单线性例 ε<1/2 限定已修；新增 singleton 例仅否定“只控制到 D 阶”的弱化，原 J>D 已排除它。均不能被称原 Lemma3.3 反例。

最终可归档范围：一般固定阶原 Lemma3.3 完成内部逐步重证与独立反攻/概率审查。仍未认证 Cor3.4 的 algebraic norm/jet 输入、Lemma3.2 continuation、Lemma3.5 atlas 回传、critical paths及其余高级排除。R29 条件六维链的整篇 OAI4 条件未消除，无无条件新高维定理、真实反例或重大性/新颖性认证。到此停止本子任务编辑。
