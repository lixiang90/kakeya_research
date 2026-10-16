# R0016：矩阵跨度边界与保原权粗化的独立审查

2026-10-17，lifting_obstructions。审查 `R0016_matrix_span_boundary.md`、`R0016_weighted_coarsening.md` 的当前修订稿。结论：有限矩阵分类及条件粗化命题通过；前稿曾保守扩大分辨率，现已正确用归一化小幅度抵消保留 r=ρ。原实际图的裁剪质量、L-tuple下界与方向差 marginal 接口仍是独立验收项，不由本审查补出。

一手核对 WZ arXiv2609.22035v1 Definitions3.1–3.3、17.2–17.4、Theorem13.5、§20，以及已入库 Shmerkin arXiv2308.09846v3 Definition4.2、Theorems1.2/1.5、Proposition4.3。审查没有独立重证这些文献输入，也没有开展新的主研究。

## 1. 精确矩阵跨度分类通过

设线性空间 L 满足每个 ψ 上的 Lψ 维数≤1。若其中有可逆 A，则 A⁻¹B 把每个向量映回其自身 span；代入 e₁、e₂、e₁+e₂即得它为标量，故 dim L≤1。若无可逆元素，每个非零元素为 rank1；对异像方向的 A=u aᵀ、B=v bᵀ，det(Aψ,Bψ)=det(u,v)(aᵀψ)(bᵀψ)为非零多项式，不能对全部 ψ 消失。因此只能是共同像直线。逆命题直接成立。

对 F 的增量 span 使用这项结论，确实分别给出一维 matrix pencil 与共同像方向两类，未假定 L 为代数，也未加入 irreducibility。常值 F、零矩阵及 dim L=0 边界均包含在内。

正 slab-Frostman 差对质量的精确版本也成立：非零二元齐二次多项式的实零集至多两条原点直线；对每个固定 φ₁，落在其中的差只把 φ₂限制在两条细 slab。只要原 good pair 数超过稿中明确阈值，每个 det(Aψ,Bψ)便必须恒为零。证明不能从小 determinant 直接变成一致近分类；主稿已明确不作该推广。

这个 finite statement 的 Φ slab 假设没有在本审查中从粗 Φ_q 自动导出。若改用有 line-cap 的原差标签先验 ν，同一零集论证也成立，但实际 L-tuples 是否被该先验支配仍须另核。主稿中“source Φ_q若满足该条件”的句子应始终按条件式读取。

## 2. 加权 quotient 与 heavy-fiber 删除通过

原0≤g≤1对每个 coarse triple 的和除以 M_A M_B²，确实得到0≤g_c≤1，总权等于原权除以同一量。若三个 vertex counting 比各≥θ、原 density≥θ，则 coarse density≥θ⁴；参数概率先验保持原样，没有从路径 marginal 改换为 uniform prior。

对小于 dM_A/(10K)、dM_B/(10K)的 fibers，删除的原 A、B质量各≤d/10。用 g≤1作三坐标 union bound，原 graph normalized mass 最多损3d/10。剩余 fibers 的下界与原 maxima 形成的所有比例都是 d、K 的明确幂；若它们是δ^O(η)，coarse graph仍只付δ^O(η)。这不等于删选后所有 source 正则条件自动恢复，主稿的范围限定正确。

## 3. 原分辨率保留：抵消与共同时间网均已修正

令完整 J 为 source-allowed 的 dyadic ρ-cell，z*∈J。由整段 source dyadic Lipschitz，f(z)−f(z*)=O(ρ)。对 τ=Cδ⁻ηρ²，归一化 F 的全段范数因此为 O(δ^η)，不只是 O(1)。

选择允许细尺度 ρ²≤s≤Cδ⁻ηρ²时，同一 s-cell 内的 F 振幅≤Cρ；fine time到该 cell 归一化中心的误差≤Cδ⁻ηρ。写 S=(b′−b)(F(b′)−F(b))，其取代表误差可分成

    O(δ⁻ηρ)·O(δ^η) + O(1)·O(ρ) = O(ρ).

因此当前稿正确保持 r=ρ，不必仅为此增大最终分辨率。必要前提是完整 J 本身属于允许尺度；如果只有一个更大的允许父 cell，上述 F 小幅度不能原样假定。当前稿已明确这一条件。

每个 s-cell 以其中心作为 coarse domain time，并赋予该 cell 中一个原 F-value，得到同一个 spacing s/ρ≥ρ 的 B。两个时间坐标因此共享同一ρ-separated集合，不需要对两端独立 coloring。精确 linewise 条件只约束 F 的像曲线，保留原 F-values足够；coarse domain times本身不必是原 fine times。

该构造也避免了把非常靠近的相邻 cell 原代表直接合并时可能跨越 Lipschitz cell 边界的问题。原 fine vertices始终附在自己的 coarse中心，SM lifting中支付实际 time displacement。

## 4. Grain 支撑、裁剪质量门槛与方向先验边界

在明确具有δ^O(η) usual AD mass的 τ-ball/局部窗口内，Y 的 AD upper给每个 coarse cell的 fine maximum，AD lower配合有限重叠 packing给 occupied cell数 upper。结合窗口总质量 lower，足以支付 quotient 的 K成本及 heavy-cell 删除。

这一步不允许仅因窗口“非空”就赋予 usual mass lower。任意裁剪 q、时间切片或 graph重权可能只留下一个边缘薄片；若实际 source构造用到这种裁剪，必须从原 graph权重证明存在满足所需质量与 density 的好窗口。当前主稿以显式假设保留了这一 gate，没有声称由粗化引理自动完成。

tube Katz–Tao 的 support upper可以直接缩放：ρ≥δ^(1/4)使 τρ=Cδ⁻ηρ³≫δ；小η且 μ>0又保证 τ≪1。故对ρ≤w≤t≤O(1)，原宽τρ≥δ及长度范围可用，得到 normalized N_w≤δ⁻O(η)(t/w)^(1−γ)。coarse代表距原支撑 O(ρ)，只需有限倍 tube扩大；这不自动等于一个重新归一化后概率先验的同常数估计。

同样，Φ_p⊂N_ρΦ_q不控制额外未用 coarse cells。最终适用逐差 fiber lemma前，仍需原 L-tuple差 law对满足 line-cap的 ν 的定量支配。本审查没有把粗化后的好 time/Y网格当成这项方向先验修复。

## 5. 全实 affine fit 的精度与质量回传通过

设 coarse fit命中≥ρ^b#B_c个 centers，且误差≤ρ^a。exponent-one counting upper使这些命中 centers的 span≥δ^O(η)ρ^b；η小到保证命中数≫1。用最远两个 centers的 bounded F-values及 fit误差可得

    ||R||≤δ⁻O(η)ρ⁻ᵇ.

fine time位移≤δ⁻ηρ、同 cell F误差≤Cρ，故附属 fine times的拟合误差≤ρ^a+δ⁻O(η)ρ^(1−b)。条件1−b>a及足够小η足以把它压到2ρ^a。大 R并未被事先丢弃，而是从大命中数推出所需界；这里确实需要源 SM 对所有实 R,U 的量词。

源 forbidden normalized tolerance是 C⁻¹δ^ηρ^(ε₀)。取 coarse a=3ε₀，明确要求3ε₀<1−b，并令η足够小依赖με₀及1−b−3ε₀，便有2ρ^(3ε₀)小于原 forbidden tolerance。与此同时，coarse linewise lemma还要求3ε₀<a₀(γ)，所以 ε₀须先明确选小，不能声称此调用适用于任意固定 ε₀。

质量端，heavy time fibers给 lifted fine命中数至少

    δ^(Cη)ρ^b (ρ/δ),

而 source SM upper为ρ^ε(ρ/δ)。选 b=b₀=ε/2，并保证 Cη<μ ε/2（实际可留严格余量），就严格超过上界。故该常用选择在保留全部η损失后可行；不能仅因ρ^b比ρ^ε大而省掉 local fine总质量与 fiber成本。

若使用 fiber lemma从多个标量 fits重构矩阵，所产生的 matrix fit mass已按同一原 B、ν×ν计数。上述回传只要应用于它已给出的 SM_r违例门槛即可，不要求不同差的拟合时间集相同或重新具 AD。

本轮独审确认的是精确 linewise分类和附明确输入的有限接口；一般二维增量分支、实际源 marginal及裁剪 gate未由它们解决。没有新增一般 Kakeya界或完整反例，长期 Goal仍 active。
