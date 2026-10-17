# R0031：原 Lemma3.1 的无 coefficient-height 下界重证

2026-10-17，子任务 A。已读恢复入口、R31 spec 和原 OAI4 PDF26–27 对应文本约 1351–1449 行。唯一 main 是 Cor3.4 的实际标量图匹配；本稿只完整支付其代数 norm/finite-jet/closure 输入。它是原作者已有工具的重证，未主张新颖性或重大性，不认证整篇四维 proof 或无条件六维结论。

**结论：在原固定 complex domain、固定 real normalization ball 和 compact interior margins 下，Lemma3.1 成立，不需任一非零 polynomial coefficient 的 height lower。** 以下逐步证明 normal family、jet order、方向检测、sublevel/Remez 和所需 closure，并给 tiny coefficient/unused branch/shrinking margin 的严格边界。

## 1. 精确类与停止条件

固定 n、D≥1；Ω⊂Cⁿ 为固定 open ball 或 polydisc，B⊂Ω∩Rⁿ 为固定 closed real ball、非空实 interior，K⊂⊂Ω 为任意固定 compact。f 在整个 Ω 单值 holomorphic，满足某个非零 polynomial

\[
P(z,f(z))=0,\qquad \deg_{total}P\le D,
\qquad \|f\|_B=1. \tag{1}
\]

P 可以 reducible、其 W-degree 可降、任意非零 coefficients 可趋零；不要求其它 roots 全有界或全 simple。f 不必 real-on-real，本引理允许 complex values；Cor3.4 的实值要求另由原应用保留。

目标是对每个 fixed q 有 `max_{|α|≤q}||∂^αf||_K≤C_q`，且对每个 z∈K 有 `max_{|α|≤D}|∂^αf(z)|≥c_K>0`。所有常数仅依固定 geometry/n/D/q，不依 polynomial heights 或 f。若只证 coefficients 不退化时的界、或把 shrinking domain 当固定 margin，均不验收。

## 2. normalized relation 的极限必含 W

对任意 sequence f_ν，选择 relations P_ν，将各自 coefficient vector 除以其 Euclidean norm。total degree≤D 的 coefficient 空间有限维，故取 subsequence 使

    P_ν→P， coefficient norm(P)=1。

若 P 与 W 无关，则对每个 x∈B，因 |f_ν(x)|≤1、P_ν coefficient convergence，

    P(x)=lim_ν P_ν(x,f_ν(x))=0。

一个 complex polynomial 若在 real ball 的实开集上恒零，逐个实变量应用 univariate polynomial identity 即所有 coefficients 为零。这与 norm(P)=1 矛盾。所以

\[
P(z,W)=a_m(z)W^m+\cdots+a_0(z),\quad m\ge1,
\quad a_m\not\equiv0. \tag{2}
\]

此步只用了 B 上 chosen sheets 的界，尚未假定 f_ν 在 complex domain locally bounded，也未把 f_ν 先取 holomorphic limit，因而不循环。

## 3. Ω\Z 上的 root barrier：允许 unused roots 逃逸

令 `Z={a_m=0}`。给任一 compact C⊂Ω\Z，a_m 的绝对值有正 lower，其它 limit coefficients 有上界。由基本 root bound，P(z,·) 的全部 roots 在一个固定圆内：例如若

    R>1+max_{z∈C,k<m}|a_k(z)/a_m(z)|，

则 |W|≥R 时最高项压过其余项的 geometric sum，故无 root。取更大的固定 R，使 P 在 `C×{|W|=R}` 无零；连续性给该 compact 上 |P| 正 lower。P_ν 均匀趋 P，所以大 ν 时同一个圆对 P_ν 也 root-free。P_ν 可能有额外 roots 在圆外趋无穷，这不影响这个 barrier。

取 p∈int_R(B)\Z，存在性由 a_m 不能在实开 B 上恒零。起点 |f_ν(p)|≤1。Ω\Z 是 path connected，且此处可直接证明：对任意 q∈Ω\Z，complex line `p+ζ(q−p)` 上 a_m 不是零 polynomial（在 ζ=0 非零），只有有限个 roots。实 segment ζ∈[0,1] 的像 compactly 位于 convex Ω 中，可在 complex ζ-plane 绕开这有限个 roots，仍留在 Ω，得到 path。

对该 path 加一个足够小 neighbourhood 得 compact C⊂Ω\Z；上述 root-free 圆可取 R>1。沿 path，chosen f_ν 连续且起点在圆内，因 P_ν(z,f_ν(z))=0 不能穿过 root-free 圆。故沿整个 path 及目标 q 的一个 neighbourhood 都有 |f_ν|<R。通过 finite cover，sequence 在 Ω\Z 的每个 compact 上 uniformly bounded。

这里传播的是**chosen sheet**，并非断言 P_ν 的全部 roots 有统一界；也没有使用所有 branches 的简单性或系数 lower。

## 4. 跨 Z 的全维小平移 disks 与最大模

固定 q∈Z。因 a_m 是非零 polynomial，存在 complex direction v，使 `ζ↦a_m(q+ζv)` 不是零 polynomial。取小 ρ>0，使 closed disk `q+{ζv:|ζ|≤ρ}` 在 Ω 内，并避开有限个 root radii，使其 boundary 不交 Z。

boundary 上 |a_m| 的最小值为正。故可取 ε>0，使所有 |w−q|≤ε 的平移 disk 仍位于 Ω，且

\[
C_q=\{w+\rho e^{i\theta}v:|w-q|\le\varepsilon,
0\le\theta\le2\pi\}
\]

是 Ω\Z 的 compact。§3 已给 `sup_{C_q}|f_ν|≤M_q`。对每个 w，函数 `ζ↦f_ν(w+ζv)` holomorphic，最大模原理给 `|f_ν(w)|≤M_q`。所以 q 的**全维** neighbourhood 有统一界，不只是那一条 line 上。

有限个 q-neighbourhoods 与 Ω\Z 的 compact bounds 覆盖任意 compact K。于是 sequence f_ν 在 Ω 每个 compact 上 locally uniformly bounded。若原 normalized family 在某 fixed K 上没有 uniform bound，可先选 `||f_ν||_K→∞`；上述 argument 对其 coefficient subsequence 给 uniform bound，矛盾。因此整个 normalized family 对 fixed K 有 uniform upper，常数 independent of heights。

这里得到的常数可以依所抽极限 P 的中间 barrier，但反证排除任一 unbounded sequence，最终推出原 family 的 uniform 常数。未声称可从每个 a_m 的数值 lower 直接读出一个统一显式公式。

## 5. derivatives、holomorphic compactness 与 order≤D

对 K 的 fixed compact neighbourhood K'⊂⊂Ω 用 §4 的 upper，再在每个点的 fixed complex polydisc 用 Cauchy integral formula，得所有 fixed q 的 derivative upper。由这些 upper，compact exhaustion 上各 family 等度连续；逐 compact 使用 Arzelà–Ascoli/对角选择得到 compact-uniform limit f。Cauchy integrals 保证 f holomorphic 及全部 fixed derivatives 同时收敛。这是 normal-family 步骤的实际由来，不把“代数所以紧”当证明。

取前述 P_ν→P 的同一 subsequence，relation 在 limit 保持 `P(z,f(z))=0`。B 上均匀收敛保 `||f||_B=1`，所以 f 不恒零。令 `P=W^rQ`，r 是 W 的最大整体 polynomial factor，

\[
Q(z,W)=b_0(z)+b_1(z)W+\cdots,\qquad b_0\not\equiv0.
\]

在 f≠0 的非空开集上 Q(z,f)=0，由 holomorphic identity 在整个 connected Ω 上成立。若 f 在 z₀ vanishes to order h，则每个 `b_k f^k`（k≥1）的 order≥h，故

    b₀=−Σ_{k≥1}b_k f^k

在 z₀ 的 order≥h。但非零 polynomial b₀ 的 total degree≤D，其在任一点的 vanishing order≤D。因此 h≤D。

若 uniform jet lower 失败，取 f_ν、z_ν∈K 使其全部≤D jets→0。再抽 `z_ν→z₀` 及 compact-holomorphic f_ν→f；Cauchy derivative convergence 给 f 在 z₀ 的≤D jets 全零，与 order≤D 矛盾。因此 jet lower 的 c_K 对整个 normalized family 一致。

## 6. 有限实方向检测和 sublevel

在 fixed real compact neighbourhood 上，对每个 order 1≤q≤D，`v↦D_v^q f(x)` 是 v 的 homogeneous polynomial，coefficients 为 mixed q-jets。可取固定有限 real directions V_q 使 evaluation injective：例如取 grid `{0,…,q}^n\{0}` 各向量归一化；若 homogeneous degree q polynomial 在这些方向全零，则它在整个 tensor grid 全零，逐变量 univariate interpolation 得 polynomial 恒零。有限维 inverse matrix 给

    max_{|α|=q}|∂^α f(x)|≤C_{n,q}max_{v∈V_q}|D_v^q f(x)|。

order 0 直接使用 |f(x)|，不需 direction。结合 §5 的 jet lower，每个 x 都有某 q≤D、某 v（q>0 时）、以及 Re f 或 Im f 的 scalar directional q-derivative≥c>0。q+1 阶 uniform derivative upper 使此 lower 在统一 small real neighbourhood 内保持 c/2。用统一有限个 balls 覆盖 fixed comparison ball，每个 ball 对当前 f 可选择有限候选中的一个 q/v/component；ball 数和 radius independent of f。

q≥1 时，沿 v 切片，对 derivative 的 fixed lower 施 divided difference：若一维 sublevel set 长度 a，则可选 q+1 个相距≥c_q a 的点。其 divided difference 由 values≤u 得 upper `C_q u a^-q`，而 real mean-value theorem 给 lower `c/q!`。故 a≤C_q u^{1/q}。q=0 时 small u sublevel 为空，其余 u 用 trivial upper。

积分横向 slices，并和有限 balls 求和，对归一化非零 sheets 得

\[
|\{x\in B_1:|f(x)|\le u\}|\le C u^{1/D},\quad0<u<1, \tag{3}
\]

其中 B₁、周围 margins 固定。这里只用了 `u^{1/q}≤u^{1/D}`，没有假代数函数的实零点数有直接一维上界。重新以 ||f||_{B₁}=1 归一化，得原 (3.2) 的 relative-norm 版本，可取某 exponent c（本证明给 1/D）；zero function 的 norm comparison 平凡处理，不把其全零集合误写成该非零 sublevel bound。

## 7. norm comparison、Remez 和 finite jets

对两个 fixed real balls B/B₁，分别以各自 norm 归一化并用 §5 upper，得双向 norm comparison（非零 f）。若 E⊂B measurable、θ=|E|/|B|>0，(3) 应用于 B normalization 给

\[
\|f\|_B\le C\theta^{-D}\|f\|_E. \tag{4}
\]

当 ratio ||f||_E/||f||_B≥1 时 trivial；否则令 u 为该 ratio，θ≤C u^{1/D} 即得 (4)。若 ||f||_E=0，令 u↓0 推出非零 f 不可能；zero f 单独满足。再用 fixed B→B₁ derivative upper，得到原 (3.1)，其 θ exponent 可写 C 而无需保持本稿的具体 D。

以另一 fixed comparison ball 为 normalization ball，再在其中心使用 finite-jet lower，给 `||f||_ball≤C max_{|α|≤D}|∂^αf(center)|`。更长 fixed jet 当然也控制 norm。所有陈述 homogeneous；常数缩放 f 不改变 relation 的 total degree。

affine base translation/rescaling 以对应 scaled derivatives 表达：在新 coordinates 中 domain、real balls、compact margins 为固定几何时，重复同一证明；polynomial total degree 不增加。平移到 parallel real slice 穿过 complex point 时 f 可能 complex-valued，但 §§5–7 已允许这一点。不能声称任意 ill-conditioned map 或 shrinking margin 后 physical derivatives 仍有同一个未缩放常数。

## 8. sums/differences 和固定 polynomial evaluations 的 degree closure

给 fixed s 个 sheets f_l、各 relation `P_l(z,W)` total degree≤D。在 field C(z) 中将 P_l 按最高 W coefficient 除成 monic，W-degree q_l≤D；roots 记 α_{l,j}，允许重根。若 Q(z,W₁,…,W_s) 的 degree≤e，令 q=∏q_l，形成

\[
H(z,W)=\prod_{j_1=1}^{q_1}\cdots\prod_{j_s=1}^{q_s}
[W-Q(z,\alpha_{1,j_1},\ldots,\alpha_{s,j_s})]. \tag{5}
\]

该 polynomial monic W-degree q，coefficients 分别在每一 root set 对称。基本对称多项式展开把它们写成 relations 的 coefficient ratios。每 coefficient 对 roots 的 degree≤eq，故各 leading denominator 的 exponent 可取≤eq；乘所有 leading coefficients 的 fixed eq 次幂即可清 denominators。所得 nonzero polynomial 的 total z/W degree 仅依 s,D,e；leading coefficient 是非零 polynomial，故不会消成零 relation。

chosen f_l 是相应 roots，在 leading coefficients 非零的开集代入，其中一个 factor为零；清分母后的 identity 由 holomorphic continuation 延伸到 Ω。因而 sums、differences 和固定 evaluations 都有 bounded-degree relation，且无 numerical height lower。即使输入 relation 带 unused factors，也不会使 monic product (5) 消成零 polynomial。

## 9. fixed derivatives 的 closure：显式 elimination

甚至无需只限 simple quadratic。把 P 的 irreducible polynomial factors 代入 chosen f；holomorphic functions 的乘积恒零，在 connected Ω 上必有一个 factor P₀(z,f)恒零。它不可能 W-independent，total degree≤D。其 primitive part 在 C(z)[W] irreducible，char 0 给 `gcd(P₀,∂_WP₀)=1`。

微分 relation 得

    P₀,z_j(z,f)+P₀,W(z,f)∂_j f=0。

用 W 的 Sylvester determinant 消元：

\[
R(z,Y)=\operatorname{Res}_W
 (P_0(z,W),\ YP_{0,W}(z,W)+P_{0,z_j}(z,W)). \tag{6}
\]

其 Y 最高 coefficient（up to 非零 factors）为 `Res(P₀,P₀,W)≠0`，故 R不是零 polynomial；`R(z,∂_j f)=0`。矩阵 size≤2D、entries degree bounded by D，所以 R 的 total degree≤C D²。重复 fixed q 次给 C(D,q) 的 bound，不依 coefficient heights。这个 identity 不需在每点除 P₀,W：在分母/derivative 零点仍由 holomorphic identity 成立。

对原 simple linear/quadratic sheets，此证明尤其适用。线性式可直接用 quotient rule，simple quadratic 的 fixed derivatives 在 field C(z,√disc) 中；tiny constant quadratic coefficient 只改变数值 coefficients，不改变以上 degree bound。原使用的任意 fixed 次 derivatives、differences、evaluations 再按 §8 closure，故 Lemma3.1 可重新用于它们。

## 10. affine-line specialization：不能直接用零 relation

令 complex affine line `ℓ(ζ)=z₀+ζv` 的 fixed closed disk 有 fixed margin 位于 Ω。若 `P(ℓ(ζ),W)` 非零，它即为 degree≤D 的 relation。若其 identically zero，取 z_ν→z₀ 使 `P(z_ν,W)` 非零（某 nonzero coefficient 的零集无 interior）；平行 lines `ℓ_ν(ζ)=z_ν+ζv` 的同一稍小 closed disk 仍在 Ω。

每个 `Q_ν(ζ,W)=P(ℓ_ν(ζ),W)` 非零、degree≤D。归一化 coefficients 并取 unit-vector limit Q≠0。固定 f holomorphic 给 `f∘ℓ_ν→f∘ℓ` 在 disk 上均匀，故 `Q(ζ,f(ℓ(ζ)))=0`。若 Q 与 W 无关，它在整个 ζ-disk 为零，矛盾。因此 Q 是有效 relation，degree仍≤D。

这一步不从一个完全零的 specialized relation 宣称 degree control；也没有让 line disk margin 随 ν 缩掉。相同 argument 适用于 parallel lower-dimensional affine slices（系数 finite-dimensional 且 slice 有 complex interior）。

## 11. tiny coefficients/escaping roots/margins 的严格反攻

**tiny coefficient 与 unused root。** 在 Ω 为 z=1 周围 fixed 小 disk 时，`εW²+zW+1=0` 的 bounded chosen branch 可写

    f_small=−2/[z+sqrt(z²−4ε)] → −1/z。

另一个 root约 −z/ε 逃逸。chosen bounded branch 的 norm ratios/derivatives不因此坏掉，§3 的 root barrier 恰只追它。若选大 root，其 norm_B 同样约 ε^-1，归一化后也没有违反 homogeneous bounds。若把 Ω 扩到包含其 simple discriminant branch points，就不再有原假设的 global chosen holomorphic sheet，不能当反例。

**shrinking holomorphic margin。** 固定 Ω={|z|<1}，令 `f_ε(z)=ε/(1−z)`，relation `(1−z)W−ε=0` total degree 2。在 variable real ball `B_ε=[−1+ε,1−ε]` 上 norm=1，但在 fixed K={0}，任何 fixed q 的全部 jets 都是 `ε q!→0`。所以不固定 B 的 complex margin 时，uniform finite-jet lower 确实失败；原 fixed B 排除此例。

**shrinking real normalization ball。** Ω fixed、`B_ε=[−ε,ε]`、`f_ε=z/ε` 给 norm_Bε=1，而 fixed point 1/2 的值发散。故 normalization ball 的非退化固定尺寸亦为实际输入，不能只写“每个 B 有非空 interior”却要求对可变 B 统一。

**多余 relation factors。** 若 P 乘了某个只在一条 line 上消失的 base factor，则 direct specialization 可能零；§10 扰动和归一化后取 limit 处理它。不需先假 relation irreducible 才能证明主 normal-family 界；§9 在 derivatives closure 中选择 primitive factor 是另一个合法步骤。

未找到保原 fixed Ω/B/K/margins 的合法 counter。以上 boundary models 明确各违反哪一项固定几何假设，不动摇原 Lemma3.1。

## 12. 对 Cor3.4 的可调用接口与范围

实际应用减真实 reference、除 M 后，difference/normalized functions 先经 §§8–9 得固定 degree bound D'。其 fixed-order derivative upper 由 §5 给出，与 reference/coefficients 退化无关。pair norm lower 在每个 incident point由≤D' jet lower 转成 finite jet lower；finite real directions 的检测由 §6 支付。norm/Remez 与 affine slices 都已保 fixed margins，Cor3.4 的 Fubini/index-prior 分母仍由 root/B 另核，不能由本稿自动略去。

本稿完整重证原 Lemma3.1 及所需 closure；不因此认证原 Lemma3.2 的 polynomial continuation、Cor3.4 全部概率切片、Lemma3.5 atlas 或后续高级 branches。来源已有工具、未经外部同行评审，无无条件新高维界或重大性声明。到此停止主稿扩展，交独立审查。
