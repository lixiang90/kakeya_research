# R0013 独立审查：共享时钟投影与原四平面包接口

2026-10-17。审查人：`lifting_obstructions`。对象为 `R0013_coupled_projection_interface.md`，并交叉核 `R0013_primary_narrow_audit.md` §6 的实际原 marks 投影替代；后读 root 补充后的 §4、`R0013_next_coupled_target.md` 及 `R0013_packet_input_limit.md` §1。结论：代数、光滑场、单块来源及条件式 D–F 通过。有限 CP 的体积对应在明确的共同 clock/原质量限制下通过；该限制和 projected-cube fatness 已由补充稿显式覆盖，无待修正条目。没有证明 (NG)、(CP) 或新维数界。

## 1. D 场、直线与括号

沿 L(t)=(t,bt−d,ct−e,f+dt,g+et)，tb−x₂=d、tc−x₃=e，故方向 (1,b,c,d,e) 确实在 D_x。f、g 仅改变另外两个位置坐标，不影响这两个恒等式。D_x 是 R³→R² 的 graph，在固定有界盒中始终维数3并 uniformly Lipschitz；轴点与同 cube 中心相差 Oδ，因此真实 cubical participation 都满足 Oδ-narrow。

X₀、X₁、X₂ 的前三坐标为标准基，所以本身独立。直接作用于系数，得到 [X₀,X₁]=2∂z₁、[X₀,X₂]=2∂z₂，符号与系数2正确。这两个新向量与 D 张满五维；把 D 当作三维积分叶的切空间不合法。该括号计算本身不产生任何定量体积下界，root 稿没有作这种跳跃。

方向图 u↦(1,u)/√(1+|u|²) 只是在固定盒上 biLipschitz；若要求字面 δ-separated，应取足够大的常数倍 δ-grid，或作固定着色。root 末段已要求下一 spec 固定这些常数。这只改固定系数，不改 δ⁻⁴。

## 2. 固定 P、kernel 与 FO 的精确线性等价

对参数顺序 (b,d,f,c,e,g)，A_t=[[t,−1,0],[0,t,1]] 的 kernel 恰为 span(1,t,−t²)。Π_t=A_t⊕A_t 的四个 outputs 与 (C1) 的横截坐标仅差固定坐标置换；两个 blocks 没有独立的时间参数。

单块经 (t,X,Z)↦(X,t,−Z/2) 成为 (bt−d,t,−dt/2−f/2)。这恰是 Fässler–Orponen 的 horizontal line，parameters (a,b₀,c₀)=(b,−d,−f/2)；空间变换与 parameter 变换都为固定可逆线性映射。因此 source 的 Hausdorff statement 与原 family 的参数维数、unit segments 到 positive-length segments 的转换合法。已核本地 v1 的 Theorem1.5/Remark1.7，并交叉读出版全文的对应 statement；不将 source 引用当作其 restricted-projection 证明已被本项目重证。

P 为 Borel 时，[t,p]↦(t,Π_t p) 连续，故 E_I(P) analytic。若一组正 Lebesgue 测度的 t 上 dim Π_tP≥3+σ，标准 slicing lower 给 dim E≥4+σ。root 只作条件推论，没有声称该 slice gain 已证。

## 3. 耦合缺口与 product 检查

f=c、g=0 的例子确有 full D(P)=(b,d,c,e)，但固定第一 parameter block (b,d,f) 后只余 e 一个自由度。其 Π_t 在 (b,d,c,e) 上 determinant=t⁴，所以它不是 gain 反例。root 正确只用它排除“固定第一 block 后第二 block 自动有二维 fiber”的前提。

对真正 first output A_t p₁ 条件化后，second parameter fibers 随 t 改变。source 是对一个固定 set 的 a.e.-t theorem，不能直接用于该随 t 变动的条件族，更不能各取不同的 favorable times。两个 marginal union 的维数也不能相加为 joint 维数。

在确实 product 且所有 segments 共同覆盖 I 的 sanity check 中，两个固定 parameter sets 的 full-measure good-time sets 可在 I 中取交；两块 slices 都维数2，积至少维数4且不超过ambient4，所以 E_I 维数5。这个有限的 product 陈述通过，没有把 product/conditional independence 施加在一般 P 上。

## 4. 有限 CP 与 cubical volume：精确对应版本

固定一个与 δ 无关、长度正的 clock interval J，要求以下两点：全部待计 line segments 覆盖 J；所计原 marks 在 J 中已具有声明的总密度。只用满足 I_j=[jδ,(j+1)δ)⊂J 的完整 clock slabs，并令 t_j 为 midpoint。忽略 J 的 O(1) 个边界 slabs 每 tube 至多丢 O(1) cubes，相对 δ^η/δ marks 可忽略（η<1，δ小）。

对原 shading 定义 P_j 为“在该 slab 至少有一个原 marked cube”的 line parameters。斜率有固定界，每条 graph line 在一个 δ-clock slab 至多经过 C 个原 cubes，故

\[
 \sum_j\#P_j\asymp\#\{(T,Q):Q\subset Y(T),\ Q\text{的clock slab在}J\}.
\]

这是原 incidences 的计数，没有扩大参与关系。每个原五维 cube 是 I_j×Q′，其中 Q′ 为四维 δ-cube。记 R_j 为所有出现过的 Q′，则原 union 恰有

\[
 |U_J|=\delta^5\sum_j\#R_j.              \tag{4.1}
\]

若 Q′ 被 p∈P_j 标记，其轴在某 t∈I_j 穿过该 cube。由于 t_j−t=Oδ，Π_(t_j)p 距 Q′ 为 Oδ。反过来，每个 p∈P_j 至少有这样一个原 Q′。因此 R_j 的 centers 与 Π_(t_j)P_j 双向 Hausdorff 距离为 Oδ。R_j 是 δ-separated grid centers，由固定尺度 covering/packing 比较可得

\[
 \#R_j\asymp N_{C\delta}(\Pi_{t_j}P_j)
          \asymp N_\delta(\Pi_{t_j}P_j),                 \tag{4.2}
\]

其中任一固定 C>0 只改变固定维度常数。由 (4.1)–(4.2)，root 的 δ⁵ΣN 与原 cubical volume 比较正确，且 (CP) 的指数正好给 δ^{1−σ+ε}。

反向从 arbitrary P_j 实现原 shading 也合法：在每个 j 为该 line 选择包含其 t_j 轴点的原 cube。每个 pair 至少一个、至多常数个实际 incidences，原 directions 与轴都不变。若选所有该 slab 的原轴 cubes，同样仅为固定多重数；依然只给该子类的真实系统。

**必须保留的量词限制。** Euclidean unit length 对 slopes u 给 clock 长度 1/√(1+|u|²)，随 u 变化。可先固定 J 为全部这些 unit axes 的共同子区间，并只研究 marks 已在 J 中有原密度的子类；也可从 CP 数据构造包含 J 的单位轴并仅 shade J。不能从原单位管的总 dense shading 自动推出任意预先选择 J 内仍有 dense mass：marks 可能集中在不同方向的 endpoint tails。root 已在 coupled §4 补明此限定；`R0013_next_coupled_target.md` 进一步固定实际长度1、J=[1/4,3/4)、midpoint δ网、同一 Ωδ/P 及该窗口内的原 density。r 足够小时 J 的确包含在所有轴的 clock range 中。上述精确有限目标通过；若以后覆盖全部任意单位管 shading，仍须另外证明 window/endpoint reduction，不能倒删该限定。

## 5. Primary audit §6 的 fixed H⁴ packet：方向与原 marks

只审其明确假设的局部 packet：全部原单位轴在同一 fixed affine H⁴ 的 Cδ-neighborhood，实际保留 Y_j(T) 是原 whole cubes，每管密度≥λ≥δ^θ。该假设没有由任意 pointwise V_Q 自动推出；本审查也不补这项提取定理。

整条单位轴在 H 的薄邻域，故其 direction 的法向分量 Oδ，投影轴长度≥1−O(δ²)。任何一个 projected δ-direction bin 中的原 unit directions 都在原 S⁴ 的 Cδ-ball 中，δ-separation 因而把数量限制为 O(1)。有限着色后仍方向分离；也可直接用 DIR-003 的 direction-bin mass α=O(1)。不需要 packet 自身有 δ⁻³ 满量级 directions。

对同一根 tube，若两个原 cubes 投到同一 H 中 δ-cell 的固定扩大，它们的轴点投影相距 Oδ。因 tangential speed≥c，其沿轴参数也相距 Oδ，原 cubes 总数至多常数。因此每管原 λ/δ 个 marked cubes 只丢固定重数；有限 orientation charts 可把它们写成 H 内 bounded graph line 的 ≥cλ/δ 个 marks。只重分实际访问时标，不填入未着色点。为了共用 graph clock，可在分析中延长 affine line 到固定 bounded interval，但 marks 仍只有原标签；没有声称新增的轴线段有 shading。

DIR-003 本来对任意稀疏数量及原 dense marks 成立，条件于完整四维证明正确。固定 ε 后，θ 取其允许门槛的一半等，便可在小 δ 吸收固定常数 c；所得 occupied-cell lower 是

\[
 N_\delta(\pi_H E_j)\gtrsim_\epsilon
 \delta^{-1+\epsilon}\lambda\#\mathbb T_j.
                                                        \tag{5.1}
\]

## 6. 投影体积与固定扩大：补齐常数比较

DIR-003 允许固定 cell 扩大；不能仅从扩大后的 footprint 大，就不加解释地报原投影体积大。这里因原 whole cubes 的 fatness，这个比较确实可补齐。

每个原五维 δ-cube 的正交投影到 H 都包含以 projected center 为心的 radius δ/2 ball，并包含于 radius Cδ ball。对这些 projected centers 取 maximal δ-separated 子集，其 radius δ/4 balls 不交且包含于 π_HE_j；它们的 Cδ-balls 又覆盖全部投影。因此

\[
 |\pi_HE_j|\asymp\delta^4N_\delta(\pi_HE_j),
\]

且任何固定倍 δ-neighborhood 或 fixed cell enlargement 的 covering number 只改变常数。结合 (5.1)，primary (D) 的实际原投影体积 lower 正确：

\[
 |\pi_HE_j|\gtrsim_\epsilon
 \delta^{3+\epsilon}\lambda\#\mathbb T_j.
\]

另一方面，原 E_j 是互不相交 whole δ-cubes 的并，对各 cube 投影体积求和直接给

\[
 |\pi_HE_j|\le C\delta^{-1}|E_j|.
\]

这个 upper 不需要 fibre 连续填满，也不会因为多个原 cubes 投影重合而失效。故 primary (F) 的

\[
 |E_j|\gtrsim_\epsilon\delta^{4+\epsilon}
      \lambda\#\mathbb T_j
\]

是合法的**局部条件性**结论。原 packet 的 whole-cube 性、每管真实保留密度和 DIR-003 的 source 条件都不可省略。

若另假设该稿 (G) 的 brush count 及各 E_j 的常数重叠，代入以上式子确实仅给 |U|³≳δ^{3+ε}λ⁴ρ。该算术仍停在 δ^{1+o(1)} 基线，没有偷偷产生 σ>0；整个刷提取/删除算法及其参数损失尚未因此得到独审。

## 7. 审查结论

root 接口的已证几何/代数及 primary §6 的显式局部 packet 替代均通过。CP 的 common-clock/原质量条件、fixed P 的 coupling、time-dependent fibers 与有限 dense-mark 定量缺口必须继续保持显式；任意 V_Q 到该 global D-field 的提取也未证明。所核内容是一项精确接口和障碍，不是 (NG)/(CP) 证明、反例或五维 Kakeya 新结果。

root 的 `R0013_packet_input_limit.md` §1 已补入第6节使用的 projected whole-cube fatness/固定扩大比较，与本审查一致。因此本轮所指出的范围及常数比较均已覆盖，无需再开主研究或改动量词以外的数学内容。
