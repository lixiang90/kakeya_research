# R0030：two-color matching 的反攻与必要损失门槛

2026-10-17，子任务 A。恢复入口及 R30 macro/spec 已读。主命题为原 OAI4 Lemma3.3（PDF29 起，文本约 1512–1537 行），不是任意一对函数的 sublevel 引理。长期高维目标的共同源认证仍未完成。本稿只反攻该精确命题，不重开 R29 投影或旧 matrix action。

**结论：未找到满足固定 d≤d₀<1、K=N^{o(1)} 和全部双边缘的反例。给出两项严格可核边界：一般固定 D 的 pair estimate 只能直接认证 d₀<1/D；另有对每个固定 D,J 的完整 fixed-power 合法构造，迫 uniform 损失阈值依赖阶数和 1−d₀。后者不反驳原“足够小 fixed power”或 subpower statement。**

## 1. 精确输入与本轮停止条件

固定 D≥1、整数 J>D、d₀<1，N→∞。两 indexed lists 各有至多 `N^{d+o(1)}` 个实 C^{J+1} functions，d≤d₀；每个 function 的导数 0…J+1 都至多 K=N^{o(1)}。事件 probability P(i₁,i₂,t) 的两个边缘分别满足

\[
P(i_\kappa\in\{i\},t\in dt)
 \le K\pi_{\kappa,i}\,dt,\qquad
 \sum_i\pi_{\kappa,i}=1. \tag{1}
\]

每个 retained event 有

\[
|f_{1,i}(t)-f_{2,j}(t)|\le K/N,\qquad
\max_{1\le q\le D}|f_{1,i}^{(q)}(t)-f_{2,j}^{(q)}(t)|\ge1/K. \tag{2}
\]

反例必须同时验证 (1) 的两色和所有原 indices；不能只控制 t-marginal，也不能把 P 条件化后免费继承原 π。若只在 fixed-power K 达到边界才有例子，必须写出它不满足原 subpower 假设。只检验数值 samples、D 随 N 增长或高阶导数超过 K 不算反例。未得反例时以严格边界结束，不把 D=1 的证明登记成一般 Lemma3.3 已认证。

## 2. 双边缘的直接容量测试

记某 color index i 可参与事件的时间集合为 E_{κ,i}。由 (1)，任意 π（包括极不均匀或含零项）均满足

\[
1=P(\text{all})\le K\sum_i\pi_{\kappa,i}|E_{\kappa,i}|.
\tag{3}
\]

故若该 color 每个 E_{κ,i} 都只有 N 的固定负幂长度，则无论如何选择 π 或在 pair 之间相关，都不能得到 probability law。只在一个很短的高阶接触窗中归一化事件的例子，正是违反 (3)，不是利用非均匀权重绕过它。

合法 restriction 到 P-mass a>0 后，normalized law 的边缘至多 `(K/a)π_i dt`。原 π 仍可用，但 K 付 a^-1；若改 π 也必须重新写支配证明。只有 a 为 subpower 才保持原 subpower regime。

## 3. 一般 D 的严格 pair upper 及其局限

令 g=f_{1,i}−f_{2,j}。其导数到 D+1 均至多 2K。对

    E(g)={t:|g(t)|≤K/N，max_{1≤q≤D}|g^(q)(t)|≥1/K}

有（当 K²/N≤1）

\[
|E(g)|\le C_D K^4 N^{-1/D}. \tag{4}
\]

完整证明：把 unit interval 切成 O(K²) 个长度≤cK^-2 的格。若一格中某 retained t₀ 有 `|g^(q)(t₀)|≥1/K`，由 `|g^(q+1)|≤2K`，整格有 `|g^(q)|≥1/(2K)`，且符号不变。若格内 sublevel 集的长度为 a，则从该集合选 q+1 个相距≥c_q a 的点；q 阶 divided difference 一边至多 `C_q(K/N)a^-q`，另一边由 mean-value theorem 至少 `1/(2Kq!)`。故该格的长度至多 `C_q(K²/N)^{1/q}`。对 O(K²) 格及有限 q 求和，因 q≤D、K²/N≤1，得 `C_D K^{2+2/D}N^-1/D≤C_DK⁴N^-1/D`。这对任意 C^{J+1} 函数成立，不用 algebraicity 或有限零点数。

固定第一色 index i，对第二色所有 indices 作 union。再用第一色 marginal 并求 π，得到

\[
1\le C_D K^5\,\#I_2\,N^{-1/D}. \tag{5}
\]

故在原 subpower regime，d₀<1/D 时一般 D 已不可能；D=1 则覆盖全部 d₀<1。但 D≥2、d₀≥1/D 时，(5) 不闭合，不能从它认证完整引理。

pair exponent 本身不能统一改成 N^-1：`g(t)=(t−t₀)^D` 在 t₀ 附近有 sublevel 长度约 N^-1/D，D 阶导数为 D!，更高导数为零。该例仅说明 pair upper 的真实高阶切触尺度；将这个窗归一化为 probability 时，两个 index-time marginals 要付约 N^{1/D}，不满足 K=subpower。

## 4. d=1 的 exact 双边缘校准

令 N 为偶整数，两色 indices 为 i,j=0,…,N−1，

    f₁,i(t)=i/N，       f₂,j(t)=t−j/N。

在 t∈[1/2,1) 上均匀取 t（density 2），令 k=floor(Nt)，再在 `i=0,…,k` 中均匀取 i、置 j=k−i。此时 i,j 都是合法 indices；每个 pair value gap≤1/N，first derivative gap=1，其余高阶 gap为零。

两色 π 均为 Uniform(N indices)。对每个 t，任一 index 的 conditional 概率至多 `1/(k+1)≤2/N`，故每个 `(i,t)` marginal 至多 `4π_i dt`，两色同时成立。取 K=4（或任何更大常数）即可验证所有 derivatives 和 (1)–(2)。

两 lists 的 cardinality 是 N，故仅在 d=1。它显示 d₀<1 是实际边界，不能无 gap 地换成 d₀≤1；未构成原反例。

## 5. 简单 fixed-power 构造：K 必须小于 dimension gap 的尺度

令 Δ=K/N，m≈N/K²，设

    f₁,i(t)=iΔ，       f₂,j(t)=(mΔ)t−jΔ，
    i,j=0,…,m−1。

沿 §4 的同一 law（将 N 改成 m）有双边缘≤4π_i dt、value gap≤Δ。若 mΔ≥1/K，则 derivative gap≥1/K。取 K=N^ε、m=ceil(N/K²)，导数和 values 均≤K；当 `0<ε<1/2` 时 lists 的指数为 `d=1−2ε+o(1)`，ε≥1/2 时 m=O(1)、指数为 0。

对于 `0<d₀<1`，必要边界只需取 `ε=(1−d₀)/2∈(0,1/2)`；更宽的 fixed-power 容差包含这个 equality 构造。因此若 uniform 版本允许至少该 loss 范围，此族可进入 d≤d₀，不能继续声称不可能。原文只声称存在足够小的 fixed-power 容差，故该必要上界与其不矛盾。

## 6. 所有固定 D,J 的 oscillatory fixed-power 校准

下面同时检验高阶导数、恒比例事件时间、全部双边缘。固定 D,J，记 `L=J+1−D≥2`。让 K→∞，选

\[
\omega=(K^2/16)^{1/L},\qquad
A=\frac4{K\omega^D},\qquad
\Delta=K/N,\qquad m=\lfloor4A/\Delta\rfloor. \tag{6}
\]

取 m≥16、ω≥12π，定义

\[
g(t)=A(2+\sin\omega t),\quad
f_{1,i}(t)=i\Delta,\quad f_{2,j}(t)=g(t)-j\Delta,
\quad 0\le i,j<m. \tag{7}
\]

令合法 time set

\[
E=\{t\in[0,1]:\sin(\omega t)\ge0,
 |\sin(\omega t+D\pi/2)|\ge1/2\}. \tag{8}
\]

每个完整 period 中该 phase set 占至少 1/3；ω≥12π 给 |E|≥1/6。其上 g∈[2A,3A]，故 `k(t)=floor(g(t)/Δ)` 满足 `m/2−O(1)≤k≤3m/4+O(1)<m`，而 `k+1≥c m`。在 E 上按 normalized Lebesgue 取 t，再在 i=0,…,k(t) 均匀取 i，置 j=k(t)−i。只要 m≥16，上述常数可统一取固定值。

对任一 color index，

\[
P(i_\kappa\in\{i\},t\in dt)
 \le C\,m^{-1}dt=C\pi_{\kappa,i}dt,
\quad\pi_{\kappa,i}=1/m. \tag{9}
\]

所以 K 足够大时，两个完整边缘都满足原 (1)，并非只有 t-marginal bounded；也没有要求非均匀 π 才成立。index pair 与 t 高度相关，这种相关性已在 (9) 实际核算。

值差为 `kΔ−g(t)`，绝对值≤Δ=K/N。第 D 阶 gap 则为 `|g^(D)(t)|≥Aω^D/2=2/K`。对每个 1≤q≤J+1，因 ω≥1，

\[
|g^{(q)}|\le A\omega^{J+1}
 =\frac4K\omega^{J+1-D}=K/4. \tag{10}
\]

函数值≤4A（至多再一个固定因子），且 A→0，故 order 0 和所有高阶导数也≤K。全部 functions 是 real analytic，所以 C^{J+1} 要求没有问题。

最后

\[
m\asymp_{D,J}N K^{-p},\qquad
p=2+2D/L=\frac{2(J+1)}{J+1-D}. \tag{11}
\]

取任意固定 0<d₀<1，`K=N^ε`、`ε=(1−d₀)/p`，则 m=`N^{d₀+o(1)}`，m→∞，且所有 (1)–(2)、derivative upper 都已验证。故若 fixed-power uniform 指同一个 K 容许 N^ε，必要门槛不得超过

\[
\varepsilon_{\rm threshold}
 =\frac{(1-d_0)(J+1-D)}{2(J+1)}. \tag{12}
\]

准确说，此构造在 (12) 达到合法例子，因此不可能在该阈值及更宽 loss 范围内统一排除；原引理仍可在一个更小的 D,J,d₀ 依赖阈值成立。多种 displayed losses 分别取 fixed powers 时，本例只是其中一个同时选择，不能推出所有参数的最佳边界。

**本例绝不是原 subpower 反例。** 若 K=N^{o(1)}，(11) 的列表指数趋于 1，不能固定 d≤d₀<1。若强行减少 lists 到 N^{d₀}，同时还要保 (9) 的时间容量，就不再由本构造满足原事件概率。把 ω 当固定幂 N 而仍写 K=subpower，会直接违反 (10)。

### 6.1 为什么 D 以上的导数控制不可直接删去

如果只控制 0…D 阶导数，singleton lists 已有真正的反例：`f₁=0`、`f₂=N^-1 sin(N^{1/D}t)`。其 0…D 阶导数均≤1、value gap≤N^-1；在 `|sin(N^{1/D}t+Dπ/2)|≥1/2` 的恒比例 time set 上 D 阶 gap≥1/2。对该 time set 取 normalized Lebesgue law、两 π 都为单点 probability，固定 K=4（N 足够大）即可满足全部双边缘。两 lists card=1。

但是 D+1 阶导数上界为 N^{1/D}，所以此例不满足原 J>D 的假设。它只说明不能把一般证明的高阶 Taylor remainder 输入删成仅 0…D 阶；不是原 Lemma3.3 的 counter，也不声称原 J 的最小性。

## 7. 对 correlated events、高阶切触和非均匀 π 的归档结论

最直接的高阶接触窗 `|(t−t₀)^D|≤N^-1` 长度虽为 N^-1/D，但每个使用该窗的 index-time 边缘有固定负幂总时间，(3) 排除其被归一化成原 law。为每个 i 搭很多不同 j 的窗口只得到 (5)；当 d≥1/D 时，要阻止这些窗口在两个 colors 同时高效铺满时间，需要原证明中真正的 alternating matching 信息。

非均匀 π 并不撤销 (3)。本稿也没有发现利用相关 events 同时满足两个边缘的 subpower 反例；§6 的 correlated law 特别显示，相关本身不是禁项，关键是 loss 是否进入固定正幂。

本轮反攻所认证的只是：(4)–(5) 的一般边界、d=1 的 exact 校准和 (6)–(12) 的 fixed-power 必要阈值。不能据此认证完整 d₀<1 一般 D 的 Lemma3.3；仍需 root/B 对 jet scales、refresh、endpoint map 和真实事件 law 的一般证明审查。也不据此宣布原引理错误、四维定理错误或 R29 条件链已消除源依赖。一般 Kakeya 与所有最终标准继续保持原状态。
