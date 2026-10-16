# R0014 独立审查：联合闭环的秩层级

2026-10-17。审查人：`lifting_obstructions`。对象为 `notes/40_multiscale/coupled_projections/R0014_cycle_rank_hierarchy.md`。独立逐步核验结论：三、四、五 cycle 的精确约束、O(ερ⁻²) 稳定及六 cycle 的实际 full-rank 例均通过，无需数学修正。它是有限联合代数几何结果，不是 (CP)/(NG) 证明或新 Kakeya 维数界。

## 1. 联合参数、闭环与显式条件数

把 block 顺序 (b,d,f,c,e,g) 重排为 R³⊗R² 后，Δp_i=γ(t_i)⊗u_i，其中 u_i=(Δb_i,Δc_i)，γ=(1,t,−t²)，与 Π_t kernel 完全一致。近交 residual≤ε 时，每个 block 的 residual error 是 (0,−r₁,r₂+t r₁)，两个 blocks 合起来 norm<4ε。因此闭环 moment residual≤4kε；没有引入不属于原 direction graph 的 latent label。

对任意三个 ρ-separated times，Lagrange polynomials 的分母≥ρ²，系数绝对值分别≤1、2、1（全部 t∈[1/4,3/4]）。G⁻¹ 的 Frobenius norm≤√18ρ⁻²<5ρ⁻²，故 σ_min(G)≥ρ²/5。该条件数可直接用于 root §2；无需 determinant⁻¹ 的更差 ρ⁻³，也没有除以方向差。

保留前 k−3 个 u_i、修正后三个的步骤合法：moment residual 经 G⁻¹ 后，三个向量 combined error≤20kερ⁻²。精确修正 edges 闭合，以同一个原 p₁ 为起点累加得到 p_i*。所有 vertices 的原参数误差可统一界为 40k²ερ⁻²（k≤6），所以 root 写 O_k(ερ⁻²) 正确。

修正点只用于证明存在一个靠近原 vertices 的低维 affine plane；不能把 p_i* 当作原 P 的新 indices 或新的 shading contacts。root 稿没有这样调用。原 directions 的 packing 使用的是原 p_i 到该 plane 的距离，故不丢原来源。

## 2. 三、四 cycle

三列 γ 可逆，精确 moment equations 只容许全部 u_i=0，因而各参数相等。近似版全部 p_i 聚于 Cερ⁻² 球，正确。这不禁止共时刻大 bush，因为 hypothesis 是三个分离的 times。

四列 Γ rank3、kernel1维；两个 blocks 的 coefficients 都在同一个 kernel，故全部 u_i 共线，参数差在 R³⊗u，方向差在 R²⊗u 中。固定首边版本也正确：取 u₁ 为原首边的 first-coordinate vector，反解另外三列，u_i=−L_i(t₁)u₁+O(ερ⁻²)。这个 plane 不依赖其他 times，且不需首边长度/角度下界。u₁=0 时全部 vertices 聚于小球，是已覆盖退化。

对 ε=Cδ、同一固定有向首边，全部四环的其他 vertices 因而只可能来自一个固定 affine 2-plane 的 Cδρ⁻² 邻域。原 directions 在 bounded chart 中 δ-separated，packing 数≤Cρ⁻⁴δ⁻²；当宽度已超过常数时该 bound 变得无信息，但仍成立。不能省略 ρ 的损失。

## 3. 五 cycle 的精确 kernel 与稳定性

五个 distinct times 的 barycentric weights w_i=1/∏_(j≠i)(t_i−t_j) 全非零。四次 Lagrange 插值的最高次项给 Σ_iw_it_i^m=0，m=0,1,2,3。因此 w 与 tw 均在 Γ 的 kernel；它们独立（否则所有 t_i 相同），kernel 又恰为2维，故它们是整个 kernel 的基。

两个 blocks 使用同一 kernel basis，存在 a,b∈R² 使 u_i=w_i(a+t_i b)。于是方向 edges 恰为

\[
 \Delta D_i=w_i[(a,0)+t_i(b,a)+t_i^2(0,b)].
\]

所以全部 direction vertices 在一个 affine ≤3-plane 中。a,b 独立时，(a,0)、(b,a)、(0,b) 独立；乘非零 w_i 的 quadratic Vandermonde 有 rank3，故边张成3维，不能统一改称2维。

最重要的稳定检查通过：root 先以第1节把近环修正为 exact moment kernel，再仅用 exact basis 推出某个3-plane，最后用 vertex error 回到原点。不需要控制可能很大的 w_i 或逆解 a,b；因此不存在把 w_i 的 ρ⁻⁴ 等尺度误乘进 vertex error 的漏洞，O(ερ⁻²) 确实成立。这个 plane 可以随整个 cycle 改变；不能以单个 cycle 的容量对全部 five-cycles 免费求和。

## 4. 六 cycle：moment、方向 rank 与 vertices 区分

令 t_i=a+hi，i=0,…,5，a=1/4、h=1/12。全部 times 位于 [1/4,2/3]⊂共同 I。q=(-1,5,−10,10,−5,1) 是 fifth finite difference 权，故 Σq_it_i^m=0，m=0,…,4。

u_i=sq_i(1,t_i²) 的两个分量分别给 0…2 与 2…4 次 moments，因此 Σγ_i⊗u_i=0 精确成立。方向 edges 是 sq_i(1,t_i²,t_i,t_i³)；列置换后为 degree0…3 Vandermonde，六个 times distinct 且 q_i非零，rank恰4。闭环所有 vertices 的 affine direction span 与全部 edges 的 linear span 相同，故确为4维。

第一方向坐标的六个前缀是 s(0,−1,4,−6,4,−1)。仅需再区分重复的两对。第三方向坐标前缀分别为

\[
 s(0,-a,4a+5h,-6a-15h,4a+15h,-a-5h).
\]

故 −1 的一对相差5sh、4的一对相差10sh，都非零；其余 pairs 已由第一坐标区分。这不仅证明 parameters 不同，也证明六个实际 directions 不同。

取固定 s 足够小，把 directions 放进指定小 slope box、anchors 放进给定 bounded box，且 unit axes 的 clock 终点大于3/4。邻接差满足 Π_(t_i)Δp_i=0，所以两根实际 unit axes 在该 shared time 相交。六方向最小距离是固定正数，δ充分小时真方向分离。

之后用同一 D-field 水平线公式为剩余 direction cap 的 maximal δ-separated set 指定 bounded anchors，即可补成 δ⁻⁴ 满量级真单位管，且所有 full cubical marks 仍满足 Oδ三平面窄性。补全不提供 small union 或大比例六环 mass；root 已明确不将此例称为 CP 反例。

## 5. 结论及未闭合的质量输入

root 的 packing 公式 δ⁻ˡ max(1,ρ⁻²)^(4−l) 正是 bounded l-plane tube 的方向 packing；它不能去掉 ρ 因子，也不能把 five-cycle 的可变 plane 当作统一给定 plane。

三/四/五环约束不意味着原 dense P_j 必有足量 separated-time、非退化 cycle。第5节的 tree 数 D²m²≤N 只标为启发式阈值，没有冒充已证一般图计数。六环例又严格阻止“继续增加闭环长度必然继续退化”的无限归纳。

因此本轮 hierarchy 的全部数学陈述通过，仍明确缺少从原 marks 推出的实际 cycle mass lower、退化剪枝及可支付的角/时间损失。本 review 不据此认证 CP、NG、五维 Kakeya 或重大中间结果。

## 6. Primary projection audit 的交叉核查

追加审查对象为 `R0014_primary_projection_audit.md` §3–6；已对照本地 GGW Theorem2.1、CSWZ Definition1.5/Theorem1.7，核下列接口，不声称重证这些整篇论文。

**全尺度 Frostman 与参与质量。** 原 full four-direction graph 在六维半径ρ≥δ球中的点数≤C(ρ/δ)⁴，除以 #P≈δ⁻⁴ 给 Cρ⁴。每点平滑成 radius cδ 的六维球，权≈δ⁴、density≤Cδ⁻²；ρ<δ时 Cδ⁻²ρ⁶≤Cρ⁴。因此 full-scale four-Frostman upper 的论证通过。保留 m(p)≥(1/2)δ^{−1+η} 的点，至少有 cδ^η 原质量；不正规化 restriction 保 Frostman upper，正规化才需付 δ⁻η。每个保留点的小球在其原 marked times 的固定扩大 plates 中，足以提供有限 incidence 定理的逐点长参与。没有由这一步推出 conditional fibers 正则。

**GGW 几何不匹配。** 对单块 rowspace H_t=γ(t)⊥，basis (t,−1,0)、(0,t,1) 的 derivatives 在 quotient 的分量分别为1、t，秩为1。两个独立 blocks 的 quotient directions 不同，联合 rank为2。一个非退化曲线的4-dimensional osculating space，其前三个 basis derivatives 都留在原空间内，仅第四个可能逸出，且非退化保证逸出，故 rank恰1。固定 GL、regular 时间换元及正交取补保持该 Grassmann tangent map 的秩，因此不能按 source 的单条 osculating curve 假设直接识别本族。该必要性检查正确，不否定未来适合重复 block 的新估计。

**CSWZ 的精确 model hyperplane。** 输出变换 (X,Z)↦(−X,Z+tX) 确实把本族化为 x+θ(t)y，其中 θ 的两个 column 分别为 (−t,t²,0,0)、(0,0,−t,t²)。θ₁₂恒0，正是 a=e₁、b=e₂ 的 rank-one model hyperplane；并非任意矩阵超平面被误当作 model hyperplane。所有 covering cells 仍在该 hyperplane 的 Cδ邻域；任意子选择在 r≥C_*δ/β 的全部尺度上 singular，Definition1.5 对整族 J′=J 迫 C≥c_βδ⁻β。故 small-loss ε<β 的 C=δ⁻ε 条件明确失败。

初稿用“可把 theorem ε 再减小”推定所有可选损失都失败，单独看不充分；作者现已改成上述 small-loss 范围，并用 §6 独立校准排除任何本应产生输出维数>3的 universal-theorem 调用。该修正通过。校准 Z=B₁⊕span(e_c) 的维数4、每时刻输出维数3，原方向投影仅维数3，因此它既能排除“任意 four-Frostman 参数集合”的联合结论，又不是 CP 的 full-direction graph 反例。

对 source 后增的 BL profile 讨论，仅核其代数测试：若 BL deficit 为 sup_Z(dim Z−(p/J)ΣdimΠ_tiZ)，上述同一个 Z 直接给 lower 4−3p。没有借该代数式认证一项相对于原 full-direction graph 的新定理，也没有在本次重审中重证 Gan 的完整 exceptional-set 结果。

## 7. 下一 PM 候选的指数与 derived cap 审查

追加对象为 `R0014_next_pruned_multiplicity_target.md`，只审蕴含与数据一致性，不证明 PM。它继续使用原 P、原 P_j、同一 clock 及原每个 (p,j) 的唯一 output cell；低重数部分是原 incidences 的子集，没有新增几何 contacts。因此是一个新的待证明质量命题，不是预先施加的统计假设。

设阈值 M=Cε δ^{−1+τ−ε}，PM 保留质量≥cε δ^ε S。低重数 occupied cells 至少

\[
 \frac{c_\varepsilon\delta^\varepsilon S}{M}
 \ge c'\delta^{1-\tau+2\varepsilon}
       \delta^{-5+\eta}
 =c'\delta^{-4-\tau+\eta+2\varepsilon}.
\]

所以取 σ=τ 的 CP 蕴含及 exponent 都正确。对最终误差 ε₀，内部 ε 取小于 min(ε₀/4,τ/4)，再把 PM 允许的 η 缩至≤ε₀/4，得到 η+2ε<ε₀。缩小 η 是更强 density hypothesis，故同一个 PM 保证仍可用；不是在结论后免费改变原数据。CP 单独只控制 cells 数，确实不能由计数本身自动推出占 δ^ε 比例的原质量，作者没有声称等价。

**Derived relative cap。** 对任意 affine 参数子空间 Z，设其方向投影 D(Z) 的维数为 l<4。若 p∈Nρ(Z)，坐标投影 D 为1-Lipschitz，故 D(p) 距 affine l-plane D(Z)≤ρ。原 directions 分离，在 bounded R⁴ chart 对 ρ≥δ 作 packing 给

\[
 \#(P\cap N_\rho(Z))
 \le C\delta^{-4}(\rho+\delta)^{4-l}.
\]

除以原 #P≈δ⁻⁴，得到原计数概率 upper≤Cρ^{4−l}，与候选稿一致。常数对 affine plane 的位置、方向统一；对ρ>1该界可用概率≤1补成平凡式。该 cap 来自原数据，未增加新 regularity。若以后在小质量 subset 中正规化，它应再付 subset 原质量的倒数，不能直接沿用原 upper。

作者正确指出：这个 derived cap 并未证明“PM失败就集中于某种 D-deficient Z”的逆命题。尚需实际的质量收缩/修剪证明，不能将它当作已经获得的新输入。PM⇒CP、cap 及本轮交接边界均通过；未认证 PM 本身或新维数结果。
