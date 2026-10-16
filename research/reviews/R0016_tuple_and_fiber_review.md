# R0016：逐差直线分支的有限加权纤维证明独审

2026-10-17。审查 notes/40_multiscale/sticky_matrix/R0016_vector_attack.md §§2–5，并核其 §§1、6–7 对来源与结论的边界。

**结论：有限加权命题通过，依赖 WZ Theorem13.5；未发现必须修正项。** 它排除“对每个被用到的差 ψ，F(B)ψ 落在某条仿射直线”的完整 graph 分支，也适用于文中 O(r) 稳定版本；不是完整 Mat(2,2) nonlinear theorem。实际源数据到其有限命题的 coarse graph/SM 接口由 root 另审，不能用本 review 代替。

本审者是 R0016_original_tuple_audit.md 的作者，所以本 review 不作为该 tuple 稿自身的独立验证。这里独立审查另一作者的 finite weighted fibre argument 和它真正需要的输入。

## 1. 外部标量输入与参数顺序

回查 WZ arXiv:2609.22035v1 Theorem13.5（PDF p52，抽取文件 2712–2724 行）。其 C={1} 特例允许 β=1、任意 α<1，但非线性精度指数 ε₁ 须足够小，依赖 α；graph density 与 output-cover 损失另须低于定理的两个 η 阈值。

作者取 α=1−γ_T/2、ε₁=4a、ε₂=b，先选 a₀(γ_T)，再 b，最后 h、r，顺序正确。a₀ 同时可取小于 1/12。h 允许依赖全部先前参数，足以同时满足 20h 小于定理阈值、h≪γ_T、h≪b 及后续 determinant 要求。没有使用一个对任意固定大 a 都成立的虚假 scalar theorem。

原标量定理针对 graph 集合。finite 命题的 0≤g≤1 使其 support 计数至少原权质量，所需 bounded multiplicity 映射后仍只付固定常数；故可以调用集合版本。该假设必须从 source tuple 上界证明，不能从“很多 L-tuples”直接省略。稿件已明确这一点。

## 2. 原标签权与合法条带质量

设 d_s 是每个原差标签上的平均 graph 权。由 ∫d_s dν≥r^h 和 d_s≤1，P={d_s≥r^h/2} 满足 ν(P)≥r^h/2；在小 r 时也有 ν(P)≥r^(2h)。此步保留 ν 标签重数，没有把重复 ψ 改成 uniform distinct vectors。

固定 s∈P。平移沿单位向量 v，垂直坐标只受原 O(r) 误差影响。半开输入条带与其 C r 扩大后的输出条带有固定重叠数，因此

    Σ_k#A_k⁺ ≤ C#A₊ ≤ Cr⁻ʰ#A₋.

删掉 #A_k⁺>r^(−5h)#A_k 的 strips，输入点数至多 Cr^(4h)#A₋。因 g≤1，所删原图权至多该点数乘 (#B)²，确实小于固定 s 的 r^h/2 密度质量的一半。剩余至少一个 strip 有作者 (3.3) 的 density 与 cardinal ratio。这是原质量的 averaging，不是挑最大 fibre 后重新假定 dense。

## 3. 标量化与 tube Katz–Tao 的实际作用

r 宽 strip 内的 r-separated 二维点，落在同一个沿 v 的标量 r-cell 的数量有固定上界；所以投影后 #D_s 与 #A_k 相差固定常数。它不能一般推广到任意宽 strip，但这里宽度恰为 O(r)。

原 weighted tuples 在此映射下的 scalar graph density 至少 r^(4h)，exact scalar outputs 位于输出 strip 投影的 O(r) 邻域，cover ≤r^(−6h)#D_s。固定倍坐标归一化把 A 与 H 同时缩放即可，不引入任何 |ψ| 或最小奇异值的逆。

输入 A₋ 的 tube Katz–Tao 给 #D_s≤Cr^(−1+γ_T−h)。若 H 在所有 affine 附近都只有 ≤r^b#B 个 r^(3a) 命中，则经过固定倍归一化仍满足 scalar theorem 的更细 r^(4a) nonaffinity；取 η 参数为 20h 足以覆盖 density、cover upper 和 B 的非集中。Theorem13.5 强制 #D_s≥c r^(−1+γ_T/2)，与 h<γ_T/10 的 upper 矛盾。

因此作者 (4.1) 的每标签实际时间子集 B_s 存在。常值曲线取全部 B 处理，不需要人为选择非零曲线斜率。这里 tube KT 用在同一个输入 fibre，本证明没有用“Y 的一个 projection 已满一维”去代替二维信息。

## 4. 两个独立差与共同时间交集

删 |ψ|<r^(4h/γ_Φ) 的标签，line-cap 给删量 ≤Cr^(3h)，小于 P 的质量。保留 ν(P)≥r^(2h) 可用余量吸收常数。

置 d=10b/γ_Φ≤a/10。固定第一差，det 小于 r^d 的第二差落在宽度 ≤Cr^(d−4h/γ_Φ) 的 strip；h≪b 保证这个宽度位于 [r,1]，line-cap 的查询合法。其总坏对质量 ≤Cr^(10b−5h)。

在同一个原 B 上令 u(b)=ν{s∈P:b∈B_s}。Cauchy–Schwarz 精确给

    Σ_b u(b)² ≥r^(2b)ν(P)²#B.

用 ν(P)²≥r^(4h)，并取 8b>9h，可使坏对贡献 ≤(1/2)r^(2b)ν(P)²#B。这里应保留这条含 ν(P)² 的较强式，再除以 good-pair 质量≤ν(P)²，才得到一个 good pair 的交集至少 (1/2)r^(2b)#B。作者 (5.2) 同时写了这条较强式，故 (5.3) 的常数/exponent 正确；不是仅凭其较弱 r^(2b+4h)#B 版本免费丢掉 4h。

该 pair 的 Ψ entries 有固定上界，det≥r^d，故 ||Ψ⁻¹||≤Cr⁻ᵈ。在共同时间交集上，两列 affine fits 合成矩阵 fit，误差 ≤Cr^(3a−d)≤r^a。因 3b<b₀、r 小时交集 ≥r^(3b)#B，违反 all-real-matrix SM_r。逆矩阵后 R,U 可很大，稿件准确保留任意实矩阵量词。

## 5. 稳定性、覆盖分支与实际接口

若 F(B)ψ 仅距直线 O(r)，沿 v 的标量化再添 O(r) 误差；右乘 Ψ⁻¹后至多 Cr^(1−d)，a₀<1/12、d≤a/10 使其仍远小于 r^a。文中只声称 O(r) 稳定邻域，没有把更粗各向异性退化自动并入。

F₀+v r(b) 的固定像分支，以及 F₀+h(b)M 的单矩阵 pencil，均确实满足逐差直线条件；M 可满秩或奇异。这里没有用 ||Mψ|| 的统一下界。它排除这些函数与全部有限 graph 输入的共存，不排除这些矩阵函数本身。

接回完整五维 source 时仍需同一 prior 的有界 graph 权、同一方向标签 law 的 cap、r-separated/coarsened B、同一 A₋ 的 tube KT、A₊/A₋ cardinal 比较和 all-real SM transfer。fine 原时间 spacing 是 δ/ρ，而非 ρ；稿件 §7 对此保留边界正确。不同输入/输出集合允许的是已证 cardinal 比较，不是自动的 Y+aY small doubling。

finite lemma 没有覆盖那些在足量 ψ 上令 F(B)ψ 真正二维的矩阵曲线。没有把“非 pencil”转换成未验证的 irreducibility。完整 N5-STICKY-MATRIX-01、其他 mixed sticky branches、一般五维 Kakeya 和长期 Goal 均仍未解决。

## 6. root 的真实源 application：补充交叉审查

另审 notes/40_multiscale/sticky_matrix/R0016_source_linewise_application.md，并逐项读其引用的 R0016_weighted_coarsening.md。**修正 §1 的符号后，实际 application 通过，范围是小 ε₀ 的 PENCIL / IMAGE 真源分支，仍依赖标量 Theorem13.5。** 符号现已核为

    y₂−y₁=(z−z')(f(z)−f(z'))(φ₁−φ₂)+error,

与 source (161) 及有限命题的 (b−b')(F(b)−F(b')) 一致。该交换不损失任何方向先验。本文作者是 tuple 稿作者；原 tuple 计数本身的独审另由 root / B 负责，本节审其向有限命题的应用。

### 6.1 good τ-window 确实按原图质量选择

令 α=2−κ。Y₀ 只有继承 upper 与 #Y₀≥K⁻¹(ρ/δ)^α；application 没有假设它本身重新 AD。完整 Y 的原 AD 上下界给其 O(ρ) ball 内的 τ-cover 数至多 K(ρ/τ)^α。删每个输入点数 <K^(−B)(τ/δ)^α 的 τ-cube，所删原点数至多 K^(C−B)#Y₀，乘最大 per-point graph degree m²#H² 即给原 graph mass 的可支付损失。

剩余图按原输入点数平均，得到同一个 Q 上的 density lower 和 #A_f⁻≥K⁻C(τ/δ)^α。原输出平移长度 O(ρ²)≤Cτ，故落在完整 Y∩CQ；其 upper ≤K(τ/δ)^α，得到 cardinal ratio K^C。这一选择不需要最大 fibre 假设，不重新给 Y₀ lower AD。α=0 时仍为上述数量界，没有除以 α。

### 6.2 同一 B 与 working resolution

coarsening 的 finite quotient 按每个实际 fibre 的原数量聚合并除以其最大值。heavy-fibre 删除在三个顶点坐标逐项支付原质量，最终 g≤1、density≥K⁻C。两个时间坐标使用同一 s-cell partition 和同一个 retained support B；没有分别着色再误当相同 B，也未增加独立原时间假设。

ρ 为 source allowed、ρ²≤s≤Cδ⁻ηρ²、τ=Cδ⁻ηρ²。完整 J 上 ||F||≤Cδ^η，而 cell 内 F oscillation≤Cρ。时间 rounding 是 O(δ⁻ηρ)，但乘的 F 差只有 O(δ^η)，所以平移表达式的总 rounding error 为 O(ρ)，无需把 resolution 放大成 Kρ。原物理 error O(τρ+δ) 除以 τ 后也为 O(ρ)，因 τρ≫δ。τ≤ρ 则由 η<µ 和小 δ 保证。

coarse A⁻ 的 tube KT 来自完整原 Y 在宽度 τw、长度 τt 的查询；w≥ρ 给 τw≥τρ≫δ，长度在固定窗口可取≤1。bin centers 的 O(ρ) 误差只需固定倍扩大 tubes，且 r-separated 支持在最小尺度的 packing 将 cover 界转为 point-count 界。A⁺ cardinal 与 A⁻ lower 分别来自完整 Y upper、输入 heavy fibres；没有付出未登记的 AD 重置。

辅助 H 在两个方向坐标使用 uniform ordered-pair law；其差 law 的 line-cap 由固定一个 φ 后应用 H 的 slab upper 得出。所有 quotient weights 保在此同一 prior 上。PENCIL / IMAGE 对任意 ψ 的像都 linewise，所以用 H 的 bin centers 和 actual fine F-values 不破坏这一 exact 条件。

### 6.3 all-real SM 的命中数和精度均可返回原时间

若 coarse affine fit 命中 >ρ^(ε/2)#B，#B≥K⁻Cρ⁻¹ 与 ρ-separation 给命中时间 span≥K⁻Cρ^(ε/2)，在小 δ 时命中数≫1。用该 span 的两个端点与 bounded F 界出 ||R||≤K^Cρ^(−ε/2)，因此提升到所有附着 fine points 的误差至多

    ρ^(3ε₀)+K^Cρ^(1−ε/2).

先选 ε 使 1−ε/2>3ε₀，再取 η 足够小，此误差≤2ρ^(3ε₀)，小于原 normalized SM 容差 C⁻¹δ^ηρ^ε₀。每个 surviving time fibre 的 lower 与 coarse 命中数给 lifted fine cardinal ≥K⁻Cρ^(ε/2)(ρ/δ)。η 最后选择，可令 K⁻Cρ^(ε/2)>ρ^ε；于是违反的是 source (SM) 的绝对门槛 ρ^ε(ρ/δ)，而非只比一个可能很小的新 B 的比例。

拟合 coefficients 返回原 f 时只作 affine 时间/值变换，仍为任意实矩阵；source 允许 all-real R,U，故无额外有界系数假设。单个 bin 中的巨大 slope 不是漏洞，因为用于反证的 fit 必须命中足够多分离 labels。

### 6.4 最终适用范围

以 a=3ε₀、b₀=ε/2 使用有限 lemma，ε₀ 先足够小依赖 γ，η 最后使所有 K^C≤ρ⁻ʰ，参数顺序闭合。其结论只排除在一个原 rich ρ-time interval 上 exact PENCIL / IMAGE（或明确附加的逐差 linewise）来源分支。没有处理一般二维 F(B)ψ；没有调用 Lemma19.2；没有把这一分支结果提升为完整矩阵非线性定理或新的 Kakeya 维数界。补充审查通过，可按此范围归档。
