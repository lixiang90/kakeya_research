# R0010：实际 n(0)≈log1 的 level-coloring 模型；先验与反例攻击核验

日期：2026-10-17。作者：`lifting_obstructions`。状态：以下 full8 prior、实际 profile、angular cap、单 level 几何 cap及§8真实atlas已由root独核，见research/reviews/R0010_root_model_review.md。统一随机标签步骤在本轮另稿，并经独审；本文件§9记录RL4/RL5的独立接口检查，整体入口为results/reviewed/HOR-002_zero_depth_one_high_horizon.md。未经外部同行评审，不声称Kakeya反例。

## 0. 本轮限制与已证范围

本轮对象是 literal j=3 version2，具有原始 exact/native/tempered 输入、C(d<1) 数值条件和**实际** n(0)≈log1。不能把 HOR-001 的 f(r) 整体平移，不能在 observable world 权重中平均旧 density。

本文件核验一个新的 internal-level mixture：可见线分别位于 `ty+xz=λ`，λ 在 [1,2] 的 δ-grid 上均匀取值；每个 level 的 hidden initial value 是一个任意预先固定的 color cλ∈[0,1]，再加完整密度微噪声。得到：

- 完整八系数、分段常密度、同一概率 prior 与 1/4 selected mass；
- 对每个 r∈[0,L]，实际 observation typical density 为常数阶，f(r)=0，尤其 n(0)≈log1；
- 所有 velocity-bin widths ρ 的 joint density 有 Cρ upper，故可取 S=1；
- 单 level 的未归一化全宽度 plank cap 为 `Cδ^{1/2}J`，短块再付 q⁻³；
- **有具体标签规律时 H=0**：cλ 不只 affine-in-λ，若 λ 是 cλ 的固定二次式，也有全局 total-quadratic 消去。

这些结论对任意 fixed color table 成立，不把随机性当作 prior 的额外变量。最后的高 horizon 反例必须另外排除所有二次测试对 colors 的拟合；不能仅凭“颜色看起来随机”或“不是 affine”宣布成立。

## 1. 模型、精确恒等式和统一概率

固定 L>0、M>6L，取 dyadic δ≈N₀⁻ᴹ，η≈N₀⁻ᵁ，U>M+L+1 即足够；核心需要 δ,η≪a_L=N₀⁻ᴸ。取

\[
 \lambda\in[1,2]\cap\delta\mathbb Z,\quad
 s\in[1,2]\cap\delta\mathbb Z,\quad
 p,q\in[-1/10,1/10]\cap\delta\mathbb Z.
\]

全部四参数 grid indices 等概率，总数 Nδ≈δ⁻⁴，每个 index 质量≈δ⁴；λ 的边缘质量 πλ≈δ。定义无噪声 coefficients

\[
 b_{\lambda,s,p,q}
   =(s,-sq-\lambda p/s,\lambda/s),
 \qquad u_{p,q}=(p,-pq,q).
 \tag{1.1}
\]

直接展开，所有 t∈[0,1] 上

\[
 t(-sq-\lambda p/s-pqt)
 +(s+pt)(\lambda/s+qt)=\lambda.
 \tag{1.2}
\]

独立取 ξ,ζ∼U[-δ,δ]³，设

\[
 B=b+\xi,\qquad V=u+\zeta,\qquad Y(t)=B+tV.
 \tag{1.3}
\]

固定一张任意 color table `(cλ)λ∈[0,1]^{#levels}`。再独立取

\[
 e\sim U[-\eta,\eta],\qquad W\sim U[\eta,2\eta],
 \qquad w_0=c_\lambda+e,\quad w(t)=w_0+tW.
 \tag{1.4}
\]

这里 e、W、ξ、ζ 在固定 index 后独立；w₀ 与 visible block 经 λ 耦合，**不使用 visible/hidden 整块独立的旧 R8 证明**。λ 仍是内部 index，不是观察到的 world。

取 native `P_*=w,B_derivative=1`；所有 native bounds 都是固定常数，特别 `Pw=1,Pww=0`。同一概率 prior 记为 ν，selected event 仅 `t∈I=[1/2,3/4]`，所以 `dμ=1_I dνdt`、总质量 1/4，不再归一化。

## 2. 完整八维 finite-piece prior：通过

每个四参数 grid index 给完整 `(B,V,w₀,W)` 的 axis-aligned 八维盒：六个 visible coefficients 半宽 δ，w₀ 半宽 η，W 宽 η。每个盒的 density 贡献至多

\[
 C N_\delta^{-1}\delta^{-6}\eta^{-2}
 \le C\delta^{-2}\eta^{-2}.
 \tag{2.1}
\]

其重叠数为固定常数。固定 coefficient point 时，B₁、V₁、V₃ 分别把 s,p,q 各限在长 2δ 的区间中，因此各只有 O(1) 个候选；固定这些 s 后，B₃ 条件 `|B₃−λ/s|≤δ` 将 λ 限在长 O(δ) 的区间，也只有 O(1) 个候选。这个 bound 完全不依赖颜色是否彼此接近。

因此全八维实际 density ceiling 仍为 (2.1) 同阶。内部 index copies 的实现有 Nδ 个八维矩形 pieces；不用 copies 时，将每个坐标的有限 facets 作共同 refinement，仍只有固定多项式数的矩形 pieces。所有 pieces 均为固定数量的线性条件，density、逆尺度、总 index 数与 coefficients 是原始 N₀ 的固定幂。

color table 可由随机方法寻找，但一旦选定就是有限个实常数；源 Definition 2.2 对这些常数没有 height 限制。不能把随机的 cλ 当作每条轨道额外重采样的 hidden law，否则 conditional observation 及后续统一标签问题都会改变。

## 3. 实际 observation profile f(r)=0：通过

记 `Q(t,Y)=tY₂+Y₁Y₃`。全参数与 noise 都有固定有界范围，由 (1.2) 得

\[
 |Q(t,Y(t))-\lambda|\le C\delta.
 \tag{3.1}
\]

所以固定 exact `(t,Y)`，至多 O(1) 个 λ-grid levels 能贡献 density。这是实际坐标中的有限 overlap，不是 world 平均。

### 3.1 可见 density upper

固定 t∈I、λ 及一个 s 格点，near-Y₁ 和 near-Y₃ 要求

\[
 s+tp=Y_1+O(\delta),\qquad
 \lambda/s+tq=Y_3+O(\delta).
\]

t≥1/2，故 p、q 各只有 O(1) 个格点。s 总共 O(δ⁻¹) 个，λ 又只有 O(1) 个，因此一个空间点只接收 O(δ⁻¹) 个 indices。单 index 的 ξ+tζ density≤Cδ⁻³，原 index 权≈δ⁴，得到

\[
 g_t(Y)\le C\delta^{-1}\delta^{-3}\delta^4=C.
 \tag{3.2}
\]

可见 support 位于固定有界盒，体积 O(1)；无需证明任何支撑点的 pointwise lower。

### 3.2 Hidden-bin support 与 sampling lower

对每个 contributing λ，`w(t)∈cλ+[-η,3η]`。对任意 a≥a_L≫η，这只碰到 O(1) 个 width-a hidden bins。结合 (3.1)，固定 exact `(t,Y)` 上全部 contributing hidden bins 数为 O(1)，与 a 无关。

令 G_r 是原 μ 在 `(t,Y,[w]_{a_r})` 上的 density。hidden 与 visible 在 λ 后才独立，正确展开为各 λ/index 贡献之和。每个 hidden-bin conditional probability≤1，故

\[
 G_r\le g_t\le C,\qquad
 |\operatorname{supp}G_r|_{dt\,dY\times\#B}\le C.
 \tag{3.3}
\]

对任意 K≥1，直接积分小密度集合得

\[
 \mu\{G_r<K^{-1}\}\le C/K.
 \tag{3.4}
\]

取 K=N₀^τ，这给 source 意义的双侧 typical density `n(r)≈log1`，即

\[
 \boxed{f(r)=0\quad(0\le r\le L).}
 \tag{3.5}
\]

常数对全 depth range 一致，有限 prepared grid 的 union bound 合法。没有在该论证中减去旧 f(0)、放大 base 或归一化一个小质量事件。每个 r 的 density 都来自同一个原概率 prior 与同一个 1/4 selected event。

因此 endpoint 数值条件 `f(L)−f(r)≤d(L−r)` 对任意固定 0≤d<1 成立；如需 d>0，可取 d=1/2。这里 profile 的实际斜率是 0，不能把它另说成斜率 1/2 的精确轮廓。

## 4. 全速度尺度的 joint-angular upper：通过

令 ρ∈(0,1] 为 velocity-bin 宽，J 是一个三维 velocity bin，记 joint `(Y,[V]ρ)` density 为 g_{t,ρ}(Y,J)。

**当 ρ≥δ。** (3.1) 仍使 contributing λ 只有 O(1) 个。V₁=p+ζ₁∈J₁ 使 p 位于长 O(ρ) 的区间，再由 near-Y₁ 使 s 位于长 O(ρ) 区间，所以 s 格点数 O(ρ/δ)。固定 λ,s 后 near-Y₁、near-Y₃ 各给 O(1) 个 p、q。单 index 的 joint-bin density 不超过其纯 Y-density Cδ⁻³，故

\[
 g_{t,\rho}(Y,J)
 \le C\delta^4(\rho/\delta)\delta^{-3}
 =C\rho.
 \tag{4.1}
\]

**当 ρ<δ。** λ 仍只有 O(1) 个；velocity bin 将 p,q 各限在 O(δ) 区间，near-Y₁ 将 s 限在 O(δ) 区间，因此总共 O(1) 个 indices。单 index 的 `(Y,V)` density≤Cδ⁻⁶，Jacobian 与 R8 相同为1。积分 J 的体积 ρ³，乘原 index 权 δ⁴，得

\[
 g_{t,\rho}(Y,J)
 \le C\delta^{-2}\rho^3
 \le C\rho.
 \tag{4.2}
\]

对某个 hidden bin，条件概率≤1，逐 index 求和只会减少这些 upper。因此原 joint observation density 满足

\[
 G_{r,\rho}(t,Y,B,J)\le C\rho.
 \tag{4.3}
\]

在 terminal r=L、ρ=N₀⁻ᵘ 时，n(L)≈log1，故可取固定 S=1，所有固定紧 u-range 的 cap-class upper 成立。此处是 joint-density upper；相对 pure observation 的 conditional upper 仍需结合 (3.4) 的典型 lower。没有要求任何 pointwise conditional ceiling。

## 5. 单 level QCAP：原 J 与常数均可统一

固定 λ∈[1,2]，在可见空间作固定 diagonal map

\[
 T_\lambda=\operatorname{diag}
 (\lambda^{-1/2},\lambda^{-1},\lambda^{-1/2}).
 \tag{5.1}
\]

时钟 t 不变，变换后 `tY′₂+Y′₁Y′₃=1`。参数变为

\[
 s'=s/\sqrt\lambda,\quad p'=p/\sqrt\lambda,
 \quad q'=q/\sqrt\lambda,
\]

且原式精确成为 R7 的 Q=1 族。其 grid spacing `δ/√λ∈[δ/√2,δ]`；s′∈[1/√2,2]、p′,q′ 在固定小盒中。R7 的最薄轴 Fubini 与 small-A/large-A 平方根局部化在这一 compact 上都保有统一常数；原证明只需 s′ 有统一正下界及有界 p′,q′，没有用 s′ 的端点恰为1、2。

Tλ 的 condition number≤2。任意原正交框的线性 image 可用 SVD 外包成正交框，其 ordered singular widths 与原 ordered widths 逐轴固定可比，体积至多原 J 的固定常数倍。变换后的 b-noise、u-noise 仍独立，半宽在 [δ/2,δ] 之间，joint density 与支撑界和 R8 proof 相同到固定常数。

所以 R7–R8 的 all-positive-width cap 逐 λ 给出

\[
 \nu_{\rm vis\mid\lambda}(P_{\rm full})
 \le C\delta^{-1/2}J,
 \tag{5.2}
\]

对全部 positive widths、frames 与 affine centers 成立，常数对 λ 统一。关键是把原 level 概率 πλ≈δ 乘回来，得到

\[
 \boxed{\nu\{\lambda,\ Y\subset P_{\rm full}\}
 \le C\delta^{1/2}J.}
 \tag{5.3}
\]

对 q 长 block 上一般 chart matrix D、J=|detD|、spatial slack K，R8 的 affine 外推与 SVD 给

\[
 \boxed{\nu\{\lambda,\ \hbox{whole-block spatial fit}\}
 \le CK^3\delta^{1/2}q^{-3}J.}
 \tag{5.4}
\]

这是原概率内单 level 的未归一化 cap。不能把 (5.3) 错当成 conditional-on-λ 的估计，也不能给 λ 原子改权后仍沿用它。

## 6. 具体反例攻击：某些标签会被全局二次测试消去，H=0

最容易失败的 color 选择是 cλ 恒定，或者 cλ affine-in-λ；此时全时间 quadratic predictor 显然存在。更强的陷阱是：若存在一个固定二次多项式

\[
 h(z)=Az^2+Bz+C,\qquad h(c_\lambda)=\lambda,
 \qquad |h'(c_\lambda)|\ge c_*>0,
 \tag{6.1}
\]

且系数有固定常数界，则

\[
 P(t,Y,w)=tY_2+Y_1Y_3-h(w)
 \tag{6.2}
\]

本身就是允许的 total-degree≤2 测试。由 (3.1)、(1.4)，完整单位时间上

\[
 |P|\le C(\delta+\eta)\ll a_L,
\]

隐藏导数 `Pw=−h′(w)` 在全部轨道上有固定常数上下界，曲率 `Pww=−2A` 也满足 terminal 要求。取覆盖所有有界可见轨道的一个固定大空间盒，全 prior 为一个 assignment，selected mass=1/4，n(L)≈log1、J 为固定常数，所以扩大固定 K 后真实 floor 成立。单一 label 自然 known，得到完整的 q=1 true terminal atlas，**H=0**。

例如 `h(z)=1+z+z²`、`cλ=(−1+√(4λ−3))/2` 就给非 affine 的 colors，但仍落入这个 H=0 情形。故仅证明 cλ 不接近 affine function of λ 不足以排除所有二次测试。

随机 coloring 的完整负面论证必须统一排除 (6.2) 及一般 mixed/hidden-quadratic tests；本文件没有以列举若干表达式替代这一工作。

另一个必须排除的假归一化：若只取原 R8 的多个**观察到的 worlds**，给每 world 小权，within-world n(0) 仍是旧的 δ⁻¹，不能变成1。本模型实际使用单 world internal λ mixture，(3.1)–(3.4) 已物理重算原 observation density，因此没有该问题。

## 7. n(0) 与 prepared true parent 的精确量词

源 native small-value 与 selected hidden derivative bounds 结合 Lemma 2.9，保证每个 exact base 的 selected 部分只需 subpower 个 width-1/B hidden bins。bounded base、总 selected mass inverse-subpower 和 homogeneous profile 因而只给 `n(0)≥inverse-subpower`；它本身不提供 opposite upper。实际 source 的 zero-depth argument 才给 upper，合起来才是 n(0)≈log1。

对 prepared true parent，源 Lemma 2.13 的密度变换和 own-depth label equality 给

\[
 n'(0)\asymp_{\log}n(b)\,J/\nu(A).
\]

再由 true saturation `ν(A)≈log n(b)J`，才得到 n′(0)≈log1。这不是任意已知 atlas 正规化都自动满足的性质。

若 parent 仅 terminal-known、未必 own-depth known 或 true，源只有相应中间密度 upper；即使有 own-depth equality，质量 ν(A) 未匹配 n(b)J 也不能删分母。因此 n0-only 修补若要进入 optimizer，还须逐操作证明 known-but-nontrue atlas normalization 的闭合。本文件不声称这项闭合。

## 8. 显式 q=δ true terminal atlas：H≤M，不调用 generic completion

本节在同一原始先验 ν、同一 selected event `I₀=[1/2,3/4]` 上构造真正的终端系统。令 terminal 厚度 `a=a_L`，共同 dyadic time length `q=δ`；δ 足够小时 I₀ 由完整 δ-blocks 组成。非精确对齐时只用内部完整 blocks，丢失 O(δ) 时间，结论相同。

### 8.1 只用 midpoint cube 与原 w₀-bin 的完整 assignments

固定一个 block I，midpoint 为 t_I。用 Y(t_I) 的空间 δ-cube Q 与 **w₀ 的原 terminal a-bin C** 分配全部轨道：

\[
 A_{I,Q,C}=\{Y(t_I)\in Q,\ w_0\in C\}.
 \tag{8.1}
\]

这是完整轨道 assignment，在整个 I 内不变；同 block 的 assignments 互不相交。label 只有 `(I,Q,C)`，不输出 λ，不输出各层原 s,p,q 或内部 trajectory index。

由 (3.1) 及 Q 的直径 O(δ)，固定 Q 只能接收 O(1) 个 λ。每层 w₀∈cλ+[-η,η]，因 η≪a，每层只碰到 O(1) 个 w₀ a-bins。故每个 Q 参与的 C 至多 O(1)。空间有界，全部 Q 数至多 Cδ⁻³，所以每个 block 中的参与 pairs 总数

\[
 \#\{(Q,C):\nu(A_{I,Q,C})>0\}\le C\delta^{-3}.
 \tag{8.2}
\]

固定 t_I∈I₀ 的 g_t≤C 还给

\[
 \nu(A_{I,Q,C})\le\nu\{Y(t_I)\in Q\}\le C\delta^3.
 \tag{8.3}
\]

任取充分小的固定 τ>0，删除质量 `<τδ³` 的 pairs。由 (8.2)，每个 block 删除的**原 prior**质量至多 Cτ；没有在 good pair 内归一化。所有 good pairs 均有

\[
 \tau\delta^3\le\nu(A_{I,Q,C})\le C\delta^3,
 \tag{8.4}
\]

并保留至少 1−Cτ 的完整 prior。

### 8.2 Whole-block 几何、测试与真实 floor

以 Q 中心为固定空间 center，取 `D=C₁δ I₃`，其中 C₁ 是覆盖全部统一速度界的固定大常数。对任何 assigned trajectory，midpoint 误差 O(δ)，沿半个 block 的位移也为 O(δ)，所以整个 I 上 spatial fit 成立。`||D||≤Kq` 对固定 K 成立，且

\[
 J=|\det D|=C_1^3\delta^3.
\]

取允许的测试

\[
 P_{I,Q,C}(t,Y,w)=w-c_C,
 \tag{8.5}
\]

c_C 为原 w₀-bin 的中点。沿全部 assignment 轨道及整个 I，

\[
 |P|\le a/2+2\eta\le Ca,\quad P_w=1,\quad P_{ww}=0.
\]

选中 good pair 的全部 block incidences，故 `m_{I,Q,C}=qν(A_{I,Q,C})`。由实际 n(L)≈log1 及 (8.4)，增大固定 K 后

\[
 \frac{m_{I,Q,C}}q=\nu(A_{I,Q,C})
 \ge \tau\delta^3
 =\frac\tau{C_1^3}J
 \ge K^{-1}n(L)J.
 \tag{8.6}
\]

因此每个使用的 pair 都是真 packet，而非仅赋予一个 assignment 名字。所有 blocks 的总 selected mass 至少 `(1/4)(1−Cτ)`，可取固定 τ 使其≥1/8。预算来自每 block 的原概率，不存在相加后免费放大。

### 8.3 实际 own-depth list、tempered 输出和上界

在当前 exact t∈I 上，block index 由 t 确定。可见速度有固定界，所以 exact Y(t) 将 midpoint Y(t_I) 限在 O(δ) 邻域，只有 O(1) 个候选 cubes Q。另一方面 `|w₀−w(t)|≤2η≪a`；当前 hidden a-bin 将原 w₀ a-bin C 限在 O(1) 个候选。故 `(I,Q,C)` 由真实 terminal/own-depth observation 以 O(1) 列表给出，恢复不使用 λ。

assignments (8.1) 是 coefficients 的线性 bin 测试；good-pair 删除只是有限常数表。blocks 数 O(δ⁻¹)、每 block pairs 数 O(δ⁻³)，总 labels 数 O(δ⁻⁴)，frame inverse 为固定倍 δ⁻¹；pieces、谓词数量和倒宽均为原 N₀ 固定幂。按固定 chart 参数搜索 heavy pairs 的存在不需要把积分算法写成新的 observed feature。

因此这是显式非空的 q=δ true terminal atlas，

\[
 \boxed{H\le M.}
 \tag{8.7}
\]

本上界只用于原模型的非空验收，不声称对任意后续 incidence restriction 仍直接保留每个 pair 的 floor；那需要另行应用对应的原预算与删轻规则。

## 9. 并行随机标签稿 RL4/RL5 的独立审查

对象为 `R0010_uniform_random_level_labels.md`。核查结论：RL4、RL5 及与本模型的接口通过；以下记录关键检查，而非重复随机选择证明。

1. 每层 quadrature 的分布只含原 visible trajectory、e,W 和 normalized block time，均与随机 cλ 独立。增加一个实 c 参数不破坏固定维、固定次数的 sign-pattern bound；同时包含 G 与 H 的 patterns 后，所有计数、最大 b̃* 和归一化 g 的取值均被 pattern 决定，除法没有引入新的连续自由度。
2. ghost/swap 事件中 `S>2μ+t` 与 ghost `S′≤3S/4` 给 `D=S−S′≥T/7,T=S+S′≥t`。固定 unordered pairs 后，`Σ(g−g′)²≤T`，Rademacher tail 为 exp(−T/98)；每次样本上的有限 pattern union bound 可以同时覆盖事后选择的参数。这个审查包含 b̃*=0 的独立零情形。
3. 固定 quadrature point 后，P 作为 c 的多项式次数≤2，导数就是 Pw。因此 `|P|≤Ka,|Pw|≥1/K` 的可用 c 总长≤4K²a。该判断包含 w² 与 mixed terms，不只针对某个旧 predictor。
4. 原积分与 quadrature 的 weighted 误差相加≤ε_N。RL4 的总误差精确可以估成 `[1+2p_K+t_Nπ_max]ε_N≤(3+t_N)ε_N`，所以其超多项式小 remainder 正确。quadrature 的 quasipolynomial 点数仅是分析工具，不进入 prior、labels 或 tempered 输出。
5. 对任意实际 chart，复杂 assignment/selection 可以先扩大为 whole-block geometry G 与当前二次测试 H。若 block 与 I₀ 有正交集，取其中任意固定 t*；whole-fit 使 Y(t*) 落于体积≤CK³J 的椭球，(3.2) 给 `ν_vis(G)≤CK³J`。单层最大质量必须使用原 πλ 乘回后的 (5.4)，是 `CK³δ^{1/2}q⁻³J`，不是 conditional-on-λ cap。

于是 RL5 的实际 chart 上界确为

\[
 \frac mq\le CK^C
 \bigl[a+(\log N_0)^2\delta^{1/2}q^{-3}\bigr]J+r_N.
 \tag{9.1}
\]

实际 n(L)≈log1 的 subpower 因子可吸收入 K。tempered J≥N₀⁻ᴮ（某个沿 exact sequence 固定的有限 B），故 r_N/J 仍比任何固定负幂小；不能用 superpolynomial 薄框规避，因为该框违反 tempered 条件。与 true floor 比较得到 `q³≤N₀^{o(1)}δ^{1/2}`，即 `H≥M/6`。此 lower 对 further incidence submeasure 与 subsequence 的处理亦正确：原 upper 保持，典型 profile 的指数由原选择引理保留，未将条件 prior 分母删除。

随机向量必须一次固定后再定义本 prior；并行稿的 uniform-in-θ 事件允许事后选择 P、D、center、block 和任意复杂 actual assignments，正好排除了第 6 节指出的特殊全局二次拟合陷阱。该随机步骤不是只验证了一组预先枚举的 predictors。

## 10. 本文件的接口与整体边界

可合法使用：原概率的 actual f≡0、S=1 joint-angular cap、full8 finite pieces、统一 single-level bound (5.4)，以及全部 indices 在全时间真实仿射。

固定 color table 的存在由并行统一随机标签稿给出，第 9 节已独审其 RL4/RL5 及模型接口；本文件第 8 节独立给有限 true systems。因此在该已固定标签模型上可合并为 `M/6≤H≤M`，M>6L 时 H>L。不得从“λ可由 exactY 列入 O(1) 选项”直接推断全时间 λ-charts 有足够 floor，也不能从“标签难以拟合”省略真实 floor。

这个模型的 visible slopes 仍近于二维曲面 `(p,−pq,q)`，完整方向 density 约含 δ⁻¹ 成本；不具备 Kakeya 的原始满方向来源。无论后续 horizon 结论如何，都不得称为 Kakeya 反例或重大维数改善。
