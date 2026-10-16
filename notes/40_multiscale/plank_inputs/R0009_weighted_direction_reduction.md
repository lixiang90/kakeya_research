# R0009：方向 bin 质量约束到任意权重输入的严格化约

日期：2026-10-17。作者：`lifting_obstructions`。状态：以下有限组合化约为自包含工具；已接入本轮经独审通过的 shear amplification，整体结论仍条件于 SRC-001 及完整四维证明输入正确。

## 0. 结论与条件输入

固定 bounded 四维 graph chart，迹线为

\[
 L_i(t)=(t,b_i+t v_i),\quad t\in[0,1],
 \qquad b_i,v_i\in[-R,R]^3,
\]

R 是固定常数。取时间 mesh δ，D=δ⁻¹ 为整数；端点取整只改固定常数。每条有限 index i 的 marks 集为 Jᵢ，有

\[
 \delta^{-1+\eta}\le\#J_i\le D.
 \tag{0.1}
\]

令 E 是全部 marked visits 的 δ-cells，固定 cell enlargement 约定贯穿所有输入。indices 可以重复，正权 ωᵢ 可以具有任意跨度。

把 v 空间按半开 side-δ cubes 分箱，假设每个方向 bin Q 满足

\[
 \beta_Q:=\sum_{i:v_i\in Q}\omega_i\le\alpha.
 \tag{0.2}
\]

本笔记的**条件输入 U(ε₀)** 是：对固定 ε₀>0，存在 η₀>0、C₀、δ₀，使任意 0<δ<δ₀、任意数量 M 的 δ-direction-separated finite family，若每条 marks≥δ⁻¹⁺η₀，则

\[
 M\le C_0\delta^{1-\varepsilon_0}\#E_{\rm family}.
 \tag{U}
\]

等价地，`#E_family≥C₀⁻¹Mδ⁻¹⁺ε₀`。U 必须对**任意 M**成立，不能只对 `M≥δ⁻³⁺η₀` 成立。SRC-001 直接给出的只是后一种 direction-rich 输入；本轮 [shear amplification](R0009_sparse_direction_amplification.md) 已独立证明从 SRC-001 到 U 的桥接，独审见 `research/reviews/R0009_amplification_review.md`。下面的组合命题仍把 U 单列为精确输入，不把它与 SRC-001 的原始陈述混同。

### 命题 WDR

若 U(ε₀) 成立，则对 η≤η₀，同一 δ₀ 范围内所有满足 (0.1)–(0.2) 的 finite weighted families 都有

\[
 \boxed{\sum_i\omega_i\#J_i
 \le C(R)C_0\,\alpha\delta^{-\varepsilon_0}\#E.}
 \tag{0.3}
\]

常数不依赖 index 数、重复次数、总权、最小正权或权重跨度。weighted 化约不额外消耗 η，也没有 log(weight range) 损失。

## 1. 固定有限 coloring：任意代表都方向分离

若 U 的方向距离就是 slope 距离，按 grid index `k∈Z³` 模 m 染色即可；例如 m≥3 使同色不同 bins 中的任意 slope 都相距至少 δ。

若 U 使用四维单位方向

\[
 \Theta(v)=(1,v)/\sqrt{1+|v|^2},
\]

bounded chart 上此映射有统一 Lipschitz 逆，所以存在 c_R>0，

\[
 |\Theta(v)-\Theta(v')|\ge c_R|v-v'|.
\]

同色的不同 bins 至少有一个坐标 index 差 m，故任意 v、v′ 的距离≥(m−1)δ。选固定 m 使 `c_R(m−1)≥2`，便得到 U 所需的 δ-direction separation，兼容 Euclidean/angular 的固定比较因子。

颜色数 B_R=m³ 仅依赖固定 chart。没有将 δ 换成 cδ，因此时间 bins、marks 阈值及 footprint 不必重新标度。

其它 regular angular δ-grids 只要具有通常的 bounded-overlap/local-packing 性质，可以用固定个相邻 slope bins 比较，付固定常数；本笔记不对任意病态 partition 声明这种等价。

## 2. 确定性证明：其实不需要权重分层或随机抽样

固定一个颜色。对该色每个非空方向 bin Q，任选一条原 index `i(Q)`，保留它自己的完整 mark set。由于所有原 indices 均满足 (0.1)，所有代表也满足 U 的逐线 marks 下界；由于同色不同 bins 的任意代表都方向分离，U 可直接用于这些代表。

记该色非空 bins 数为 M_c，其代表 footprint E_c⊂E。于是

\[
 M_c\le C_0\delta^{1-\varepsilon_0}\#E_c
       \le C_0\delta^{1-\varepsilon_0}\#E.
 \tag{2.1}
\]

该颜色中的总权至多 αM_c，所以

\[
 \sum_{i\in c}\omega_i\#J_i
 \le D\sum_{Q\in c}\beta_Q
 \le D\alpha M_c
 \le C_0\alpha\delta^{-\varepsilon_0}\#E.
 \tag{2.2}
\]

最后对 B_R 个颜色求和即得 (0.3)。

**marks_count 差异没有被忽略**：左侧仍是每个原 index 的实际 #Jᵢ，只是在唯一一步使用全局上界 #Jᵢ≤D。所选代表可能 marks 少于同 bin 的别的 indices，但仍符合 U 的逐线下界；这已足以控制 occupied-bin 数。没有将代表的 marks 数直接当成 bin 中所有 indices 的 marks 数。

一个几乎无权的非空 bin 也可产生一个代表；这不会引入损失，因为它的 visited cells 本来就是原 E 的一部分。极小权重并不要求 E 跟着缩小。

## 3. 可选的按权抽样检查；主证明不依赖它

若希望让每个原 index 的纳入概率精确跟随权重，也可固定一个颜色：每个 bin Q 以概率 β_Q/α 被选中，再按 ωᵢ/β_Q 选其中一条 index，保留其原 marks。

因此

\[
 \Pr\{i\hbox{ 被选中}\}=\omega_i/\alpha,
 \qquad
 \mathbb E M_{\rm sample}
 =\alpha^{-1}\sum_{i\in c}\omega_i.
 \tag{3.1}
\]

每个 outcome 均符合 U，且 footprint⊂E，所以 `M_sample≤C₀δ¹⁻ε₀#E`；取期望给同一个 total-weight bound。marks 差异也可以直接核对：

\[
 \mathbb E\sum_{i\in S}\#J_i
 =\alpha^{-1}\sum_{i\in c}\omega_i\#J_i
 \le D\,\mathbb E M_{\rm sample},
\]

从而直接回到原加权访问量。

这没有以总权归一化。总权远小于 α、绝大部分 outcomes 为空也无妨；不需要期望样本数≥1或集中不等式。主证明第 2 节已经完全避免抽样。

若 α=0，正权条件迫 family 为空，结论平凡；非空 family 可直接取 α>0。所有数量有限即可，不要求原 indices 数是 δ 的固定多项式。

## 4. ε/η 的实际预算与物理密度单位

给定目标 ε>0，只要 amplification 子任务从 SRC-001 得到 U(ε₀)，其中 0<ε₀≤ε，则本化约在其 η₀ 内成立。可取 ε₀=ε/2 留出后续固定几何、subpower 范围及 finite-approximation 成本；本 weighted 证明本身只有 B_R 个颜色的固定损失，不再改变 η₀。

若实际未归一化 visible-slope measure 满足

\[
 \nu_V\le A\,dv\quad(v\in\mathbb R^3),
\]

则每个 physical side-δ bin 质量≤Aδ³；固定角网格或 fixed enlargement 只再乘固定常数。应代入

\[
 \alpha=C A\delta^3,
\]

而非 α=A。于是 (0.3) 的物理单位为

\[
 \boxed{\sum_i\omega_i\#J_i
 \le C_\varepsilon A\delta^{3-\varepsilon}\#E.}
 \tag{4.1}
\]

两个边界核验：单方向、总权 m 时必须 α≥m，故单线 dense-shading 情形不会产生虚假的 δ³ 小因子；单位质量均匀分布于约 δ⁻³ 个方向 bins 时 α≈δ³，得到预期的方向丰富单位。

R0008 的 quadric 平滑例具有可见完整方向 density A≈δ⁻¹，若此 upper 已单独核验，它在 (4.1) 中仍需支付 δ⁻¹；不能因其正 conditional angular exponent 就把 A 改成常数或 subpower。本笔记不重算该模型的最优 A。

## 5. 实际 source 的两个调用位置：能用到哪里

已对照原四维论文 Theorem 2.17 的 (2.26)–(2.28)、Proposition 2.16 的 groups G 与 greedy residual，以及 SRC-001 的现有源审计。以下只陈述本桥接完成后允许的调用范围。

### 5.1 源 zero-depth 步骤：有方向来源，可条件调用

源最初 full-slope smoothing 给 subpower full-slope density；积分 bounded hidden-slope range 后，visible slope marginal 仍有 subpower ceiling。五维拟版对应三维 visible slopes，若记其实际 ceiling 为 A≤K₀，则在细 mesh `ρ=N₀^{-D_*}` 上，每个方向 bin 的**原始未归一化**质量≤C Aρ³。对轨道或 incidence 作未归一化 restriction 只会保留这个 upper。

在 source 的 finite weighted approximation 中，须保留该 bin 质量上界和每个保留 index 的长 duration。若 representative coefficient rounding 的误差≤Cρ，一个新方向 bin 的原质量来自固定个相邻旧 bins，故只付固定常数；footprint 也只使用同一 visited union 的固定 enlargement。取实际线为 representatives 而不改变 slope，同样可直接保持。

在这些有限化接口已经完成的前提下，(4.1) 给

\[
 \frac{\sum_i\omega_i\#J_i}{\#E}
 \le C_\varepsilon A\rho^{3-\varepsilon}.
 \tag{5.1}
\]

若 projected zero-depth density 有固定幂增益 N₀^κ，原 whole-cell witness 与长 duration 下界会给相反的 raw multiplicity lower

\[
 \frac{\sum_i\omega_i\#J_i}{\#E}
 \gtrsim K_0^{-C}N_0^\kappa\rho^3.
 \tag{5.2}
\]

当 A 为 subpower，选择固定 ε 使 `D_*ε<κ/2` 即得到矛盾。这与 SRC-001 所记录的专用 zero-depth 替代路线一致。

若 A≤N₀^{β+o(1)} 带固定幂，则 (5.1) 的成本是 N₀^β；让固定 ε 足够小后，只能排除大于 β 的 density 增益。也就是说，在上述同一 source finite-approximation/典型 cell 接口成立时，zero-depth 典型可见 base-density 的指数至多 β；只有 A 为 subpower 才恢复专用 `g(0,0)≤0`。这里 β 是方向成本，不能删除。

bounded chart 若仅为 subpower 范围，应先分成 subpower 个固定 intercept/slope charts 并记录 cell enlargement/shear 的 subpower 成本；不能把固定 R 的常数无说明地视为对所有 R 一致。本有限引理没有此类范围损失。

### 5.2 Universal parent/group/residual 调用：没有自动修复

原 Proposition 2.16 中，G 是在一个短 block 上按 midpoint position 与 native X-bin 分组；随后还作 greedy residual restrictions。其分析使用旧未归一化轨道权重，没有把它们变成方向均匀的新概率。

本方向输入可用于某个**实际给出了 direction-bin upper α_G** 的 group，但一般 cap-class/natural G label 并不单独提供所需 subpower A_G。若当前 residual 只作为同一旧 prior 的未归一化 restriction，旧 upper 可以保留；若换成归一化 conditional prior，必须支付 group mass 分母。

更一般地，在 visible 维数3的 parent normalization

\[
 t=t_c+q\tau,\qquad Y=y_c(t)+D Z,
\]

对原 visible-slope ceiling A，conditional parent prior 的新 visible-slope density 只能直接给

\[
 A_{\rm new}\le
 \frac{A|\det D|}{q^3\nu(A_{\rm parent})}.
 \tag{5.3}
\]

若保留完整 `(V,W)` slope density 并使用 version 2 的 `W_new=qW_old`，则对应 full-slope ceiling 的变换成本为

\[
 C_{\rm full,new}\le
 \frac{C_{\rm full,old}|\det D|}
      {q^4\nu(A_{\rm parent})}.
 \tag{5.4}
\]

这两个公式针对不同 marginal，不能相互替代；还须核对原 hidden-slope 范围。对于 prepared true parent，质量与 n(b)|detD| 可比，也不使 q 与 n(b) 的固定幂成本自动消失。

### 5.3 对照原 (2.20)–(2.23)：方向输入不能产生 greedy 所需全框集中

原 2.16 的一个 q-block 内，空间除以 Rq、时间除以 q，R 是 subpower 放大。新 visible slope 为 `V_old/R`；由于使用旧 prior 在 G 内的**未归一化** restriction，若旧 visible-slope ceiling 为 A，新坐标中的可用 ceiling 是 `A R³`，而非 A。原空间 Jacobian `J₀=(Rq)³`，典型 group base-density lower 为 `n(L)J₀`。

令 θ 表示保留的 normalized incidence mass 与原 group mass m_G 的比例（源 averaging/duration pruning 给 inverse-subpower θ）。按原 (2.21) 的 whole-cell witness 及相应 (2.22)，方向版调用前的 raw multiplicity lower 具有形式

\[
 \frac{\sum\omega_i\#J_i}{\#E}
 \gtrsim \theta N_0^{-\xi/4}n(L)(Rq)^3\rho^3,
\]

本方向输入的 upper 则为 `C_ερ^{3−ε} A R³`。比较并消去 R³ρ³，只得到

\[
 n(L)q^3\lesssim
 C_\varepsilon\theta^{-1}N_0^{\xi/4}A\rho^{-\varepsilon}.
 \tag{5.5}
\]

这里只给密度、时间与已有方向成本之间的比较；它没有像原无方向 WP3 的 (2.23) 那样，逼出某个**空间框的质量/体积比**超过 greedy 停止阈值。不能从 (5.5) 直接完成所有 group/residual 的 true spatial extraction。θ、固定容差及近似成本也必须保留，不能把 m_G 或后验分母默默设为1。

因此即使本轮 U 与 WDR 全部成立，也只提供带真实方向成本的 finite 输入，不能修复已经被 HOR-001 否定的 generic j=3 H≤L，更没有证明一个受限极值类在 normalization、coarsening、selection、completion 中闭合。

## 6. 本任务交付与仍待独审的接口

已完成：任意正权、重复 indices、任意权重跨度及极小总权的严格有限化约；marks_count 差异、固定 coloring、期望与方向质量单位均已逐项保留。该部分是初等工具，不是新的几何估计或重大中间结果。

本轮 amplification 子任务已完成并经独审：有界 spacetime shear 用 O_R(δ⁻³/M) copies，把任意稀疏方向 family 放大为固定 chart 中常数比例满方向的实际 separated family，time 保留、footprint 至多线性增加；由 SRC-001 推出对任意 M 的 U。因此 WDR 已接入这条条件链。不能把确定性选代表或按权抽样本身当作稀疏放大的替代，也不能删除整条链条件于完整四维 proof 及输入正确这一限制。
