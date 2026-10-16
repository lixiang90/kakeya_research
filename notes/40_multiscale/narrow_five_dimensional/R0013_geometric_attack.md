# R0013：真实五维管的三平面兼容性攻击

2026-10-17。作者：`lifting_obstructions`。任务 N5-NARROW-GAIN-01。以下构造是实际 R⁵ 单位线段、δ-separated 满量级方向与原 full shading 的构型；它严格排除一项沿 central line 的平面一致性捷径。它的 union 体积为常数阶，**不是 (NG) 的反例**。主幂 gain 仍未解决，不声称新维数界或重大中间结果。

## 1. 已检验与未解决的命题

主任务要求：#T≈δ⁻⁴、原 shading δ^η-dense，且每个 shaded cubical δ-cube Q 的全部参与方向落在某三维线性子空间 V_Q 的 O(δ) 邻域，能否推出 |U|≥δ^{1−σ+ε} 的固定 σ>0 gain。

一种可能误用的更强捷径是：若同一 central tube 在许多 cubes 中都遇到近最大数量的参与 tubes，那么这些 cubes 的三平面必须 O(δ)-接近同一个三平面。下面反例同时具备：

- 真正的 δ-separated #T≈δ⁻⁴ 个单位方向与单位管，全部原 cubes 被 shading；
- 一个 central tube 上正比例的 δ-cubes，各自有≈δ⁻² 个参与 tubes，达到三平面窄条件允许的最大量级；
- 每个这些 rich cubes 的可行 V_Q 被实际参与方向强制为一条不断变化的三平面族；任意固定三平面只能 O(δ)-匹配 O(1) 个 rich cubes。

所以 full direction source 与 central line 上的点态 richness，本身不提供上述沿线一致性。构造没有否定允许丢弃全局小 incidence mass 的 averaged 兼容性定理；第6节明确计算该边界。

## 2. 一个容纳真实直线的光滑三平面场

坐标写成 x=(t,x₂,x₃,z₁,z₂)。对每个 x，定义三维线性子空间

\[
 D_x=\{(a,b,c,tb-x_2a,tc-x_3a):a,b,c\in\mathbb R\}.
                                                        \tag{2.1}
\]

其前三坐标为恒等图，故维数始终为3；在任意固定有界盒中，x↦D_x 对 Grassmann 距离有固定 Lipschitz 界。

任取 slopes u=(b,c,d,e) 在一个固定小盒 K=[−r,r]⁴ 中，其中 r>0 为固定小常数。另可任取 bounded anchors f,g。考虑真实直线

\[
 L_{u,f,g}(t)
  =(t,-d+bt,-e+ct,f+dt,g+et).             \tag{2.2}
\]

其未归一化方向为 v_u=(1,b,c,d,e)。沿整条直线，t b−x₂=d、t c−x₃=e，故

\[
 v_u\in D_{L_{u,f,g}(t)}\quad\text{对全部 }t.
                                                        \tag{2.3}
\]

取轴线段为 (2.2) 在 0≤t≤1/|v_u| 的部分，它的 Euclidean 长度恰为1；不是把 graph-time length1误当成单位 Euclidean length。r 可取足够小，使所有这些单位线段都包含 clock interval [1/4,3/4]，并位于同一个固定有界盒。anchors 的特殊选择见第3节。

把每条轴线段变成 spec 中的 cubical δ-tube：所有与轴线相交的半开 dyadic δ-cubes 的并。取 full marks Y(T)=T。对任意参与 cube Q，记其中心 x_Q，设 V_Q=D_{x_Q}。每个参与 T 都有轴点 x_T∈Q；由 (2.3) 及 D 的 Lipschitz 性，

\[
 \operatorname{dist}(\widehat v_u,V_Q)
 \le C_r|x_T-x_Q|\le C_r\delta.           \tag{2.4}
\]

因此**所有新产生的实际 cubical incidences**都满足同一窄条件，不需把 tubes 互相交的新增点删除，也没有换成不同 shading label。进一步地，(2.4) 可直接从 (2.1) 看出：前三分量不动，把后两分量改成中心点的 graph 值，误差≤Cδ；该向量就在 D_{x_Q} 中。

## 3. 方向分离的连续 rich bushes 与满量级补全

固定一个小的 dyadic β>0，令 2β<r。取固定充分大 A>0，并取

\[
 \tau\in[1/4,3/4]\cap A\delta\mathbb Z,
 \qquad b,c\in[\beta,2\beta]\cap A\delta\mathbb Z.
\]

端点格点取整只改变固定常数。对这些三参数 indices，指定 hot slopes 和 anchors

\[
 u=(b,c,\tau b,\tau c),\qquad
 f=-\tau^2b,\quad g=-\tau^2c.             \tag{3.1}
\]

于是对应单位轴线在 t=τ 精确通过 central point

\[
 L_{u,f,g}(\tau)=(\tau,0,0,0,0)=P_\tau.   \tag{3.2}
\]

同时加入 central 单位轴线 L₀(t)=(t,0,0,0,0)，0≤t≤1。

必须核查方向分离，而非只数参数。映射

\[
 H(\tau,b,c)=(b,c,\tau b,\tau c)
\]

在上述 compact box 上为 biLipschitz embedding：前两坐标恢复 b,c，第三坐标除以 b≥β 恢复 τ；映射本身的导数也统一有界。u↦(1,u)/√(1+|u|²) 在 K 上同样 biLipschitz。选固定 A 足够大后，hot grid directions 彼此至少 2δ-separated。它们与 central direction e₁ 距离≥cβ，所以所有这些 directions 共同 δ-separated。hot directions 共≈δ⁻³ 个。

将该有限集合扩成 direction cap κ(K) 中的一个 maximal δ-separated set，其中 κ(u)=(1,u)/√(1+|u|²)。球面 packing 与 δ-covering 给总数

\[
 c_r\delta^{-4}\le\#\mathbb T\le C_r\delta^{-4}.
                                                        \tag{3.3}
\]

对补入的 directions 使用 (2.2) 并取 f=g=0；对 hot directions 保留 (3.1)。全部轴线都仍满足 (2.3)，所以补全不会破坏任何 cube 的窄条件。得到主任务形式的满量级方向族，对某些固定 C₀、C 成立；这些常数都独立于 δ。这里满量级是 spec 的 #T≈δ⁻⁴，并不偷换成每个球面方向都出现。

每根实际 cubical tube 有≈δ⁻¹ 个 cubes、体积≈δ⁴。full marks 因而有 Σ|Y(T)|=Σ|T|≈1，满足任意固定 η>0 的原 dense shading 条件。不能将这一步改说成仅局部有δ⁻²个方向、缺 full source 的旧 quadric 模型。

## 4. Rich cubes 的平面由真实方向强迫

令 Qτ 为包含 Pτ 的唯一半开 dyadic cube。所有 clock τ 都为 Aδ-separated，故这些 cubes 彼此不同，且都属于 central T₀。每个 Qτ 有≈δ⁻² 个 hot tube labels 参与：固定 τ，b,c 各有≈δ⁻¹ 格点，全部轴线都经过同一个 Pτ。不存在靠小的边界交集冒充 whole-cube shading 的问题；tube 与 full shading 均包含该整个 Qτ。

三平面窄条件下方向 δ-separated 的球面 packing upper 为 Cδ⁻²：S⁴ 中某 S² 的 Cδ 邻域体积为 O(δ²)，每个分离方向有体积≈δ⁴ 的不交小球。因此本构造的 richness 达到该局部 upper 的量级。

在 Pτ 上定义

\[
 E_\tau=D_{P_\tau}
 =\operatorname{span}\{e_1,e_2+\tau e_4,e_3+\tau e_5\}.
                                                        \tag{4.1}
\]

其 hot directions 为归一化的

\[
 e_1+b(e_2+\tau e_4)+c(e_3+\tau e_5).
\]

从 hot grid 选择三个固定间隔的 (b,c) 值，即得到 Eτ 内一个最小奇异值≥cβ的3向量 frame；也可使用 central e₁ 和两个非共线 hot directions。δ 足够小后，格点逼近不损此界。

所以任意三维 W 若把该 cube 中所有参与方向都包含在 C′δ 邻域内，都必须满足

\[
 \|P_W-P_{E_\tau}\|\le C_{\beta,C'}\delta.
                                                        \tag{4.2}
\]

证明是把 Eτ 中任意单位向量用 conditioned frame 展开：其在 W⊥ 的投影≤Cβ C′δ；两个同维子空间的 projection gap 等于最大 principal sine。因而这里不能任意另选一组几乎恒定的 V_Q 来躲避旋转；实际参与的方向已迫使 (4.2)。

## 5. 沿一根 rich central tube 的平面发生常量级变化

对 τ,σ∈[1/4,3/4]，Eτ 与 Eσ 共享 e₁，另外两组 basis 分别在互相正交的 (e₂,e₄)、(e₃,e₅) 平面中旋转。直接计算得

\[
 \|P_{E_\tau}-P_{E_\sigma}\|
 =\frac{|\tau-\sigma|}
 {\sqrt{(1+\tau^2)(1+\sigma^2)}}
 \asymp |\tau-\sigma|.                   \tag{5.1}
\]

因此相距常数的两 hot cubes，其全部可行 V_Q 也相距常数，不能 O(δ)-匹配同一三平面。更强地，固定任意 W 与固定常数 C′，若 W 在两个 hot cubes 都满足方向 C′δ-narrow，则 (4.2)–(5.1) 迫 |τ−σ|≤Cβ,C′δ。故 W 只能匹配 Oβ,C′,A(1) 个 hot cubes，而 central T₀ 上共有≈δ⁻¹ 个 hot cubes。

hot clock grid 间距 Aδ，A 是固定数，因此这些 cubes 占 central tube 的固定正比例，不能仅以“这根 central tube 上的 rich cubes 太稀疏”为理由排除构造。事实上任意两个不同 Eτ、Eσ 的交恰为 span(e₁)，共同包含 central line 的方向并不约束其他两个维度。

这个例子严格否定以下不带额外 derived mass 条件的捷径：

> 完整方向分离、full shading、三平面 Oδ-narrow，以及一根 tube 在正比例 cubes 上具有≈δ⁻²重数，便迫使沿该 tube 的三平面 Oδ接近一个固定三平面。

plane field (2.1) 甚至是光滑的，所以单独假定局部 Lipschitz 变化也不会修复这项错误推理。该观察不作为新的任意统计假设建议；需要从真实总体 incidence 推导何种可用结构，仍须另证。

## 6. 为什么它不反驳 (NG)，也不排除合法 averaged pruning

本构造的 union 体积为常数阶。验证 lower 也很直接：除 O(δ⁻³) 个 hot directions 外，有≈δ⁻⁴ 个 completion directions，其 anchors f=g=0。对每个 fixed t∈[1/4,1/2]，它们在 transverse space 的位置由

\[
 (b,c,d,e)\longmapsto(-d+bt,-e+ct,dt,et)
                                                        \tag{6.1}
\]

给出。此线性映射 determinant=t⁴，且在该时间区间 uniformly biLipschitz。completion directions δ-separated，故每个 transverse δ-cube 最多接收 O(1) 个这些点。截面 union 体积≥cδ⁻⁴δ⁴=c；积分该公共时间区间便得 |U|≥c。固定有界盒给 upper≤C。因此它远大于 (NG) 所求的 vanishing lower bound。

全族 incidence mass≈1，但 hot tubes 共≈δ⁻³根，只占 tube/shading 总质量 O(δ)。central rich cubes 的 hot incidence mass为

\[
 \#\{\tau\}\,\#\{(b,c)\}\,\delta^5
 \asymp\delta^{-1}\delta^{-2}\delta^5=\delta^2.
\]

所以一个允许从全局丢掉小质量再抽取均匀 high-multiplicity 部分的有效论证，完全可能删除这个 rich skeleton。本稿不把沿单根 central tube 的反例升级成该 averaged 论证的反例，也不声称所有大贡献 tubes 都有旋转障碍。

真正未解决的是：若假设 |U|≤δ^{1−σ+ε}，原总 shading mass≥δ^η，所导出的多数 incidence 的重数、空间 spread 与这些 V_Q 的沿线变化，能否迫使一个带固定幂 gain 的 planebrush estimate。仅从“同一 root tube 穿过多个 rich cubes”直接识别共同三平面是不合法的；如何利用小 union 和原质量排除低全局贡献的旋转 skeleton，仍是所需的新 incidence 输入。

## 7. 本轮攻击结论与审查接口

没有找到满足全部假设且 union 体积≤δ^{1-o(1)} 的真实反例，也没有证明 (NG)。已得到的严格结果是：在真实满量级方向与 full marks 下，点态三平面窄结构、甚至 central tube 上持续最大量级的 richness，均不自动给沿线平面一致性。此结果使用新的 actual tube 构造，未复用缺完整方向来源的旧 j3 模型。

下一项只对 root 的实际几何推导交叉审查，重点检查它是否从原 mass 获得足够的 averaged 信息，是否把 tube/cube participation 与新增几何交混用，以及 plane comparison 的尺度/角损失是否真实可支付。主任务仍按本轮 spec 的停止规则处理，不追加任意 irreducibility 或统计条件。

## 8. 新代数接口：共享时钟的两个 horizontal blocks

按 root 的后续接口核查任务，把 (2.2) 的 line parameters 写为 P⊂R⁶，坐标顺序为 (b,d,f,c,e,g)。同一 fixed time 的 transverse image 是

\[
 \Pi_tP=\{(tb-d,f+td,tc-e,g+te):(b,d,f,c,e,g)\in P\}.
                                                        \tag{8.1}
\]

每个单块的矩阵和 kernel 精确为

\[
 M_t=\begin{pmatrix}t&-1&0\\0&t&1\end{pmatrix},
 \qquad\ker M_t=\operatorname{span}(1,t,-t^2).
                                                        \tag{8.2}
\]

因此 Π_t=diag(M_t,M_t) 是一条**共享同一个 t**的 restricted projection family，不能改为独立的 (t₁,t₂) 平均。对连续 bounded 参数集，方向投影 D(P)=(b,d,c,e) 正四维测度是适当 full-direction 输入；对本轮 finite δ-net，只有分离与计数，不能把 finite P 的 Hausdorff dimension 0 偷换成4。

独立打开 [Fässler–Orponen, DOI10.1112/blms.12844](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12844)，核对 Theorem 1.5 及 Remark 1.7：其 horizontal line family 的 union dimension 为 min(dim_H parameters+1,3)，并允许每线取 positive-length segment。我们的单块经固定线性空间变换

\[
 (t,X,Z)\longmapsto(X,t,-Z/2)
\]

变成其标准线 (a t+b₀,t,b₀t/2+c₀)，其中 (a,b₀,c₀)=(b,−d,−f/2)。所以单块适用性没有符号或1/2系数障碍。以下缺口来自两个 blocks 的耦合，并非该变换失效。

1. **两个 marginal 的满维不能相加。** 如 P={(p,p):p∈[0,1]³}，两块各自 union 满三维，但 joint union 只是 diagonal 子空间中的三维集。这个例子的 D(P) 仅二维，不反驳本轮 full-direction 输入；它精确否定只引用两条 marginal 结论的逻辑。
2. **Full D(P) 不保证固定第一参数 block 后第二块仍有二维 fiber。** 取 P={(b,d,c,c,e,0):(b,d,c,e)∈[0,1]⁴}。D(P) 为完整四维盒，但固定 (b,d,f) 就固定 c=f，第二 parameter fiber 只有 e 一个自由度。该例的 joint projection 实际仍满四维，因为 Π_t 在 (b,d,c,e) 上 determinant=t⁴；它不是反例，只证明不能免费给 conditional fiber 赋维数2。
3. **同一 t 的条件化与 almost-every-t 不能交换。** 目标是对 ν 在 P 上的同一 measure，控制第二 output 在条件于 first projected output M_t p₁ 后的维数/能量。这些条件 fibers 本身依赖 t。单块定理对每个固定 Borel parameter set 的 a.e. t 结论，没有直接提供这些随 t 改变的 conditional estimates 或共同的可用时间集合。
4. **Dense finite shading 仍需定量输入。** 上述 Hausdorff theorem 与 positive segments 不是对任意 δ^η-dense 零散 cubical marks 的统一 finite-scale estimate；exceptional-time、Frostman/energy 常数及原质量损失必须从实际输入重算。即使对全参数集合证明某个 joint Hausdorff 结论，也不能直接报为 (NG) 的 δ-power gain。
5. **从一般 V_Q 到 (8.1) 的结构未证。** 本构造给出主任务的一个真实子类，不是任意 pointwise three-plane field 的 normal form。没有从 arbitrary V_Q 的窄条件推导 Π_t representation 的步骤，便不能把该 projection 子问题当作一般 (NG) 的等价命题。

因此 singleblock 一手结果是合法参考，但目前无法无损 tensorize 为本轮五维估计。该接口提供一个具体的同 prior、共享时钟 conditional-projection 缺口，不新增任意统计假设，也不宣称已经闭合主任务。
