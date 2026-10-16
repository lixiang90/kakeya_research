# R0026：large-τ 的全局 time candidate、原窗口与 good-q 审计

2026-10-17，子任务 A。主任务 N5-MIXED43-NQ01。本稿审计 WZ §22.5 的全局稳定化，证明一个保原时间质量的修补接口；不把逐 q 的 scalar τ 改名为 vector τ。mixed43 的 whole-matrix AFF₃ 仍是显式条件，完整五维、其他分支与 Hausdorff 未解决。只编辑本文件；高级原图/闭包输入具名列出，未全篇重证 source。

## 1. 原文定位与量词

文献为 `literature/primary/wang_zakharov_2026_sticky.pdf`，arXiv:2609.22035v1。行号是 extracted 同名 txt 按 `split('\n')` 的一基编号。已逐行读下列范围。

| 位置 | 准确输入或断点 |
|---|---|
| Def17.2，PDF65，3365–3381 | 原 time 为 δ-separated Z、`#Z≥δ^(η-1)`；窗口是固定 **dyadic** ρ-intervals；f 的本尺度 Lip、跨时间 Y-union AD、原 ξ/Φ coherence。 |
| Def17.4，PDF66，3408起 | d5/k4/ell3 的两个 grain 坐标分解；本轮 u,v 为 row2，b 为 scalar，`E(z,s)=v(z)-v(s)-b(s)[u(z)-u(s)]`。 |
| Lemma22.1，PDF95，5005–5027 | (179) 只要求 `||E(z,s)||≤cτ/ρ` 的 **upper**。计数证明用它令两中点 y 差 O(τ)，再用原 grain/τ-coherence；没有要求所选 q 中 E 达到 τ/ρ。 |
| 原 additive relation，PDF95–96，5030–5072 | 原 (180) 的误差 `O(Kτρ+δ)`；(181)–(183) 是重建原 L 图，不是任意删图后自动保密度。 |
| Lemma22.5，PDF100，5273–5286 | (196) 对每个原 anchor z₀、其 dyadic ρ-window 和所有 coefficients，fit upper 相对 **原 Z∩J**；τ_j 是全局 time subsets 的最小化，不是 q 内最小化。 |
| PDF100，5288–5306 | 小 τ 与物理 nonquad 矛盾、有限 j 稳定化。可以用保守常数 `ρ^(2/m)` 代替未留端点余量的 `ρ^(1/m)`。 |
| PDF101–102，5345–5395 | large-τ 先拟合 F、迫 slope 小，再由一个 q 内 (199) 写 `τ_(j+1)≲ρ^ε τ_j`。这里需要一个达到全局候选门槛的 time union；单个 q 中 rich subset 本身不足。 |

原 Lemma22.5 是 scalar 特定尺寸；本文只把其可直接检查的 vector algebra 及全局计数接口推广至 row2，不能据此调用整个 lemma 代替证明。以下物理 vector nonquad 和 AFF 输入必须在同一个基准 time set Z 上成立。

## 2. 固定基准、窗口函数和全局最小化

固定原 dyadic ρ partition `𝒥_ρ`，ρ 在原允许范围 `[δ^(1/4),δ^µ]`。记 `N=#Z`、`N_J=#(Z∩J)`。所有 j 使用同一个原 Z、同一个 f/tildef 和窗口 partition。假设本轮条件准备已给：

- 每 J 的 whole-matrix AFF，特别 `u(z)=u(c)+r_J(z-c)+O(Kρ^(1+ε₀))`；各所用系数及 b 的本尺度差≤K，`|b(z)-b(s)|≤Kρ`。
- 每原 c∈Z∩J 的 row 函数 `h_c=v-b(c)u`，对所有 row coefficients A₀,A₁,A₂，有物理 upper

\[
\#\{z\in Z\cap J:\|h_c(z)-A_0-A_1(z-c)-A_2(z-c)^2\|\le
\rho^{\epsilon_1}(\rho^2+\rho\|A_1\|+\rho^2\|A_2\|)\}
\le\rho^{\epsilon_2}N_J. \tag{1}
\]

这里采用固定 row norm；更换范数只须预留常数余量。若 AFF 是从更早 time set Z_old 取出的子集，而 (1) 仍以 `#(Z_old∩J)` 为分母，必须先付每窗口密度删除或把其 K 损失显式带入 (1)；不能直接把两个不同的“原 Z”合并。以下假设该接口已经落实。

对任意 A⊂Z 定义单一全局泛函

\[
T_\rho(A)=\rho\max_{J\in\mathcal J_\rho}\max_{z,s\in A\cap J}\|E(z,s)\|,
\quad E(z,s)=v(z)-v(s)-b(s)[u(z)-u(s)]. \tag{2}
\]

空或 singleton 窗口贡献零。取递增固定小参数 η_j，定义

\[
\tau_j=\min\{T_\rho(A):A\subset Z,\ \#A\ge\delta^{\eta_j}N\},
\quad Z_j\text{ 为一个实现极小值的集合}. \tag{3}
\]

有限 Z 使极小值存在；j 增加则 τ_j 不增。窗内 anchor 可各不相同，但 **T 的定义不随 q、ψ 或新拟合函数改变**。

对每非空 `Z_j∩J` 任选一个原 anchor c_J，定义

\[
F_J(t)={\rho\over\tau_j}[h_{c_J}(c_J+\rho t)-h_{c_J}(c_J)]
       ={\rho\over\tau_j}E(c_J+\rho t,c_J),\quad t=(z-c_J)/\rho. \tag{4}
\]

由 (2)–(3) 直接 `||F_J||≤1`。因此同一 J 内的所有空间 q 都可使用这个 F_J；空间平移只改常数，角 ψ 在以后才选择。没有必要另设 `τ_q≈τ_j`。相应 G_J 的上界由 b 的原本尺度差和 r_J 给出；large-τ 下它可按诚实 mesh 删除。

## 3. 全局 τ_j 的两端和有限稳定化

原 dyadic Lip 与 b bounded 给 `||E(z,s)||≤Kρ`，所以 `τ_j≤Kρ²`。另一方面，若 `τ_j≤ρ^(3+2ε₁)`，取一个满足 `#(Z_j∩J)≥δ^η_j N_J` 的原窗口（按 N_J 加权平均总能找到）。固定 c,s∈Z_j∩J，由 E 小及 whole-u AFF，

\[
h_c(z)=C+[b(s)-b(c)]r_J(z-c)
 +O(\rho^{2+2\epsilon_1}+K^2\rho^{2+\epsilon_0})\quad(z\in Z_j\cap J). \tag{5}
\]

当 `2ε₁<ε₀`、K loss 后取小时，error 小于 (1) 的 `ρ^(2+ε₁)`。若 `η_j<µ ε₂/2`，则 `δ^η_j>ρ^ε₂`，与 (1) 矛盾。于是所有 finitely many j 均有

\[
\rho^{3+2\epsilon_1}<\tau_j\le K\rho^2. \tag{6}
\]

取固定 m 足够大。若每个 j<m 都有 `τ_(j+1)<ρ^(2/m)τ_j`，则 `τ_m<Kρ⁴`，与 (6)（小 ε₁<1/4、K loss 小）冲突。因此存在 j 满足

\[
\tau_{j+1}\ge\rho^{2/m}\tau_j. \tag{7}
\]

这里 2/m 是保守选择；只用 drop ρ 的链不足以仅由 (6) 的上下端立即矛盾，因为仍可能落在 `ρ³` 与 `ρ^(3+2ε₁)` 之间。之后取 `2/m<c_shrink/2` 即够，不影响机制。

## 4. rich affine fit 迫近常数：物理阈值与 vector 缩小

固定满足 (7) 的 j。先删 `m_J=#(Z_j∩J)<θ N_J` 的 windows，取 `θ=δ^(2η_j)`。所删原 times 总数≤θN，相对 Z_j 至多 `δ^η_j`，趋零。余窗 m_J≥θN_J。

在 large-τ alternative `τ_j>ρ^(3-ζ₁)` 中使用

\[
w_L=K_L[\rho+\rho^3/\tau_j],\qquad
c\rho\le w_L\le 2K_L\rho^{\zeta_1}. \tag{8}
\]

K_L 是原有限小幂，必须最后小；不能用带 ε₀ 的更细 mesh。给定 a,b>0，令 `h=w_L^a`、`β=w_L^b`。设某 window 的 vector affine fit

\[
A_J=\{z\in Z_j\cap J:\|F_J((z-c_J)/\rho)-C-R(z-c_J)/\rho\|\le h\}
\]

满足 `#A_J≥β m_J`。若

\[
\beta\theta>\rho^{\epsilon_2}, \tag{9}
\]

则该 fit 的物理宽 `(τ_j/ρ)h` **不能**小于等于 (1) 的允许宽，否则 (1) 直接冲突。代入物理 slope `A₁=(τ_j/ρ²)R` 得

\[
\|R\|<\rho^{-\epsilon_1}h. \tag{10}
\]

此推导适用于所有 real row C,R，不假定其中某坐标非零、bounded-slope 或 scalar 投影。于是同 A_J 内

\[
\|F_J(t)-F_J(s)\|\le C\rho^{-\epsilon_1}w_L^a
\le CK_L^a\rho^{a\zeta_1-\epsilon_1}.
\]

又由 (4) 的定义，固定原 anchor c_J 后

\[
E(z,s)=h_{c_J}(z)-h_{c_J}(s)-[b(s)-b(c_J)][u(z)-u(s)].
\]

原本尺度 Lip 给最后一项≤K²ρ²。因此整个 A_J 的 vector E 满足

\[
T_\rho(A_J)\le C\tau_j K_L^a\rho^{a\zeta_1-\epsilon_1}+K^2\rho^3
\le\rho^{c_*}\tau_j. \tag{11}
\]

最后一步须先取 `ε₁≪aζ₁`，再取原 K/K_L loss 小；例如可留 `c_*=aζ₁/4`（a<1、常数由更小 loss 吸收）。这缩小的是完整 row/vector E，不是 `E·ψ`。

## 5. 全局最大 fibers 的二分：合法候选或可支付删窗

每余窗令 M_J 为上述 precision h 的 **最大** affine-fit cardinality。finite times 的可能 subsets 有限，所以可选择达到 M_J 的实际 fit。记 bad windows 为 `M_J≥βm_J`，选各自最大 fiber A_J。

若 `Σ_bad M_J≥δ^(η_(j+1))N`，则

\[
A=\bigcup_{J\ bad}A_J
\]

是 (3) 中 j+1 的一个合法全局原 time candidate。由于 J 是固定 dyadic partition，(2) 只比较同一个 J 内的对，(11) 对所有贡献 windows 同时成立，故 `Tρ(A)≤ρ^(c_*)τ_j`。结合 (7)，当 `c_*>2/m` 与 δ 小时矛盾。这里每窗 fit 可不同；T 只需每窗自己的 E 上界，根本不要求全局同一 affine polynomial。

反之 `Σ_bad M_J<δ^(η_(j+1))N`，于是 bad windows 的全部当前 times 数满足

\[
\sum_{J\ bad}m_J<\beta^{-1}\delta^{\eta_{j+1}}N. \tag{12}
\]

若

\[
\delta^{\eta_{j+1}-\eta_j}/\beta=o(1), \tag{13}
\]

就可删去全部 bad windows，而只损 Z_j 的 o(1) 比例；加上第4节 sparse 原窗删除仍保 `#Z_good≥(1-o(1))#Z_j`。每个剩余窗均有同 F_J 的 all-real vector affine nonfit

\[
\#\{z\in Z_{good}\cap J:\|F_J-C-Rt\|\le h\}<\beta\,m_J. \tag{14}
\]

这就是原文从 local (199) 到 global τ_(j+1) 所需补入的 mass dichotomy。只有某 q 内一个 rich fit，并不能直接取代这里的 global union。

### 指数相容性

(9)、(13) 可同时满足。写 `x=logρ/logδ∈[µ,1/4]`。由 w_L≥cρ，β≥c^bρ^b；所以充分条件是

\[
b+2\eta_j/\mu<\epsilon_2,\qquad
\eta_{j+1}-\eta_j>b/4. \tag{15}
\]

可先固定 η_(j+1) 足够小于 µε₂，再取 `b≪η_(j+1)`，最后 η_j 足够小于 b、所有 finite/ABC 阈值。若 K_L 在 (8) 的 lower 也取后小幂，(15) 只多一个后取小量。source 的 h-recurrence必须实际安排这个次序，不能既先固定 b 又要求所有 η_(j+1) 任意更小。有限 m 后可递归选择，原 η 最后小。

## 6. 原整 time 闭包、重新选 q 与 g

第5节所留 Z_good 是**删整时间层**：每保留 z 的全部原 E_z、Y_z、X、Φ、witness 和 T 不改。R22 `R0022_time_restriction_closure.md` 的闭包适用，参数为 `K=δ^-O(η_j)`：跨时间 Y-union 的 upper 由原 union 继承，lower 由每个自身 centre 所属原单层 Y_z 的 AD lower 提供；tube AD/CW 因 T 不改而保留。不宣称任意 spatial/fiber subset 自己获得 AD lower，也不要求每条管都有相同比例 surviving marks。

为获得 m_q 的绝对 lower，可再删 `#(Z_good∩J)<δ^(Bη_j)ρ/δ` 的稀窗，B 固定充分大。它们总数至多 C/ρ，所删 times≤`Cδ^(Bη_j-1)`，相对 `#Z_good≥cδ^(η_j+η-1)` 趋零。这个操作也是删整窗，故 (14) 不变。

然后在所保原 window 中用 cross-time Y-union cover 和原 incidence averaging **重新**选择 good-q。具名接口是 R16/R24 的原权重计数：在其实际 time set `Z(q)⊂Z_good∩J` 上

\[
m_q\ge K^{-1}\#(Z_{good}\cap J),\quad m_q\ge K^{-1}\rho/\delta,
\]

且点数、管 upper、原水平 grain 的恢复计数足以重新生成 bounded L graph g，密度≥K^-C。不能沿用删除前固定 q 的 graph 密度：它可能全部支撑在已删窗。

由 (14)，同 F_J 在新 q 的 conditional affine-fit mass 至多 **Kβ**，不是 β；此 K 要由 η_j≪b 吸收。ν_q 的 cap来自原 time packing和 m_q lower。窗口基准 F_J 的 affine nonfit 在 restriction 上有确定 upper，因此可在此后选择原角 ψ；没有把 q-dependent fit 直接并回 (3)。

allowed-scale 格的变化按 R22 第3节处理：新参数可取原 η 的整数倍以查询旧格；若取整 ρ，须将有限倍 `δ^-O(η_j)` 比例计入 K。用于 (2) 的固定原 dyadic partition不应在候选并集中悄悄改成滑动 balls。原ρ尺度的 coherence/union properties事实上仍由原数据保存，使用更大参数的声明不抹去这些额外已知控制。

## 7. global τ 可用于新 q 的 L-count；诚实 mesh

原 Lemma22.1 的 (179) 在全 Z_j 每窗成立。取 fixed/allowed 向上倍数 `τ_L≥c^-1τ_j`，使 cτ_L/ρ 覆盖 global E upper；`τ_L≈Kτ_j` 的有限格费用保留。由 (6) 及 `τ_j>ρ^(3-ζ₁)`，有 `δ≤τ_L≤ρ`（后取小 loss）。

计数证明 5018–5024 只需要 `|z-s|≤ρ`、angles bounded、两中点 y 差 O(τ_L)，随后使用 τ_L-coherence Cauchy–Schwarz 和 full horizontal3 grain。并不需要新 q 内的 E 最大值与 τ_j 可比。若实际局部 E 更小，几何入同一 τ_L-ball的条件仍成立，τ_L^κ 等计数因子按实际选择的 τ_L 保留。原 proof 的终端 marked-degree 不能逐管免费设为 m_q；R16/R24 已付的 weighted averaging才是调用基础。

删除 b 项时，u AFF 的 r_J 有界且 b 本尺度差 O(Kρ)，乘 `|z-s|≤ρ` 的 scalar-Y increment 误差为 **O(Kρ³)**。再加 L relation 的 `O(Kτ_Lρ+δ)` 与角 proxy Oρ 误差，除工作 physical patch τ_L 后是

\[
w_L=K[\rho+\rho^3/\tau_L]. \tag{16}
\]

原带 ε₀ 的 `K[ρ+ρ^(3+ε₀)/τ]` 不能吸收一般 Kρ³。因 τ_L>ρ^(3-ζ₁)，这里只能用 `w_L≤Kρ^ζ₁` 的诚实上界。physical scalar-Y base `δ/τ_L` 被 (16) 覆盖：δ≤ρ⁴、τ_L>ρ^(3-ζ₁) 给 `δ/τ_L≪ρ`。fine time base δ/ρ 也远小于 w_L。

这对后续 scalar13.5 的 nonfit 精度门槛有实际影响：physical `ε₁` 须相对 `aζ₁` 后选小，不能继续依赖原 ε₀-controlled mesh。13.5 的两个不同 η 阈值仍须分别付；三点标量化与 fine weighted 归约另由本轮其余稿审查，本稿不把它们当成已经由原 Step3 一句话完成。

## 8. 结论及认证范围

全局 maximal-fiber 二分提供真实修补：在 (1) 同原基准、固定 partition、合法整 time 闭包、原 good-q/L-count 接口及相容参数 (15) 下，large-τ 可在选角前给原 vector F_J 的逐剩余窗口 affine nonfit，同时保固定比例的全局 Z_j；原 g 在保留数据上重新生成。它不是只在一个 q 缩 scalar E 的等价重写。

原文 local (199) 单独不足以证明 global τ_(j+1) 缩小；本稿指出的是这一中间量词责任及带质量修补，不是四维主定理反例。whole-matrix AFF₃ 与 vector nonquad 本身仍为本轮明确条件，full mixed43、其他五维 branch 和一般 Kakeya 未解决。具名原高级计数/闭包输入未在这里全量重证，不宣称新的维数界或重大结果。
