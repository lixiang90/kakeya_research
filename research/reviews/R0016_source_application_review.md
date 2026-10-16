# R0016：实际原配置 linewise 排除链的独立审查

2026-10-17，lifting_obstructions。已完整阅读 `R0016_original_tuple_audit.md` 与 `R0016_source_linewise_application.md`，并对照 WZ Definitions3.6、17.2–17.4、原§20.1的路径定义及(157)/(161)。结合已审的 weighted coarsening 和本代理的 finite linewise lemma，结论为：**当前限定的实际 source PENCIL、IMAGE 子族排除链通过**，以 WZ Theorem13.5 为明确的高级扩张输入。没有调用 Lemma19.2、任意 q 的原(146)字面版本或完整四维 Kakeya证明。

范围必须保留：完整原 d=5、k=ℓ=3配置，source-allowed ρ，实际 dense时间 cell J，ε₀先按γ明确选小，ε与η按顺序选小，且 SM对所有实矩阵成立。一般 Mat(2,2) nonlinear lemma仍未证明；这不是新 Kakeya维数界或完整反例。

## 1. 原关联与 good-q 选择

管关联使用原 Φ_p 的 fine witness graph。固定 p、一个 fine φ-bin，对应的完整 slope位于 O(δ)盒，经过 p 的 dyadic管参数也只占 O(1)个 cells，因而 degree在 K次幂内为δ⁻κ。若原记号 T_p允许额外关联，应先只保这些原 Φ witnesses；这是从同一个原 T选择合法关联，不是添加新管。以“全部任意额外管”代替该 witness graph时，degree upper不能未经检查套用。

原 grain填充和 Y_z AD给每个完整slice至少 K⁻¹δ^(−4+κ)个 E点。J内跨时间 Y union的ρ-cover upper与 f在J的 dyadic Lipschitz，使物理 E只需 Kρ^(−4+κ)个ρ-cubes覆盖。按原 incidence I_q加权平均选 q，再用 degreeupper，确实得到

    e≥K⁻¹n(ρ/δ)^(4−κ),
    m≥K⁻¹n,
    e≥K⁻¹m(ρ/δ)^(4−κ).

这里 n=#(Z∩J)，m为该 q实际占用时间数；没有把每个局部 grain 或每根管赋予未经证明的密度。

原 coherence使通过 q的实际管有至多 Kρ⁻κ个 coarse方向 bins。每个 bin经过 q时，方向—截距联合参数落在一个 O(ρ)盒；原 tube family的4-AD upper给每盒≤K(ρ/δ)⁴个 fine管。因此 #T_q≤Kρ⁻κ(ρ/δ)⁴合法，使用的是原 joint参数 AD，而非只用方向数替代。

## 2. 原 V、J、L 计数与 heavy方向辅助集

对原 d_T，R=Σd_T²≥I²/#T_q。代入上一节 good-q lower，得 R≥K⁻¹emδ⁻κ。随后 V的 CS以及 J=Σ_g B_g²、Σ_g B_g=R给出稿中(8)/(9)的 lower；J upper只用局部 grain点数 upper，因此两边都不依赖逐grain locally dense。B_g平方的左右两因子确实分别对应同一原grain内连接的两段原关联路径。

L的签名保相同 p、z′、z″、中间 x的τ-bin及终端方向的τ-bin。同码路径对满足实际 L条件。小 variation条件由ρ-Lipschitz及 τ=Cδ⁻ηρ²支付，故每个中间 x-bin的中间物理点落在 O(τ)ball；原τ尺度 coherence使签名数≤Ke m²(ρ/τ)²τ⁻κ。对实际 one-arm multiplicities作平方 CS给(12)，其尺度幂核对为

    F_L=δ⁻⁴κ τ^κ(ρ/δ)²(τ/δ)²,
    K⁻¹eF_Lm²≤#L≤KeF_Lm².

这补齐了平均计数，没有假定不同近点的方向集有大交。

原 incidence混合 μ的 binupper与slab upper来自各原 Φ_p，supportupper来自 q coherence。按 μ删除轻 coarse bins得到 H，并通过固定一个初始(p,T₁)后的 L扩展 upper Kδ^κF_Lm²，得(15)的边际支配。初始 incidence总数约 eδ⁻κ，两个δ^κ因子相消正确。故删任一初始方向不在 H的 L质量有明确 upper，能够保原 L质量；H uniform的 slab估计不是从原 Φ_q未用 cells猜出的。

## 3. Graph fibre(17)/(18)与终端修剪

固定 code(y₁″,z,z′,b₁,b₂)，恢复次序与每项参数数目均合法：先恢复 x₁″与T₁′、沿给定slice交点恢复中间grain，再恢复 T₁、起点、T₂、第二grain点及τ-close终端管。两次 coarse初始方向选择付(ρ/δ)^(2κ)，终端τ-close选择付(τ/δ)^κ。合并为

    K N_y F_Lρ^(2κ),

与(17)一致。固定第一终端实际点再对其余 labels求和，去掉 N_y并恢复两 coarse方向数，得(18)的 KF_Lm²；没有多出ρ或δ幂。

用(18)把低质量终端slices、低局部点数grains的原点数 upper转为原 L质量 upper，再按原 e_z加权选择终端时间，合法得到一个好slice与原 Y₀。除去逐code maximum后，#G≥K⁻¹#Y₀m²#H²，以及 #Y₀≥K⁻¹(ρ/δ)^(2−κ)均成立。使用的是原 image set的实计数lower，不是把原重数抹去后假定均匀。

原(161)在该 G上给实际输出 y₂″属于完整 Y_(z*)；coarse方向替代误差≤O(τρ)，加原O(δ)，所以归一化后是 O(ρ)。并未要求输出返回 Y₀，也没有导出 Y₀的 additive closure。

## 4. τ窗口补齐了此前保留的 clipping gate

Y₀在 O(ρ)ball内，但不宣称它本身有 ADlower。用完整原 Y的 ADpacking，至多 K(ρ/τ)^α个τ-cubes可遇到 Y₀，其中α=2−κ。删除低于 K⁻ᴮ(τ/δ)^α原输入点数的 cubes，所删 Y₀点数≤K^(C−B)#Y₀；G为indicator，其所能承载的 graph质量由这个原点数 upper控制。B先取大使损失小于原G质量一半，再按实际输入点数平均，得到所需dense好τ-window。

这是一次对原 G的显式质量删除与选择，足以通过此前审查的 clipping gate。输出平移长度≤Cρ²≤Cτ，所以完整输出落在固定扩大窗口内；原 Y的 ADupper给 output/input fine cardinal ratio K次幂。α=0时只用上述幂式计数，没有除以α，端点κ=2同样包含。

随后 coarse input数 lower来自保留 fine mass及最大cell upper；coarse output数 upper来自完整原Y的packing，故两者的 cardinal比仍为K次幂。标签在一个δ-cell中的K重数先聚合进quotient，没有当作 O(1)遗漏。

## 5. 粗化、原先验与 all-real SM 回传

前一独审 `R0016_fiber_interface_review.md` 已核 cell-center time网与小幅度抵消。当前应用中满足其前提：完整 J为允许ρ-cell，F=(f−f(z*))/(τ/ρ)具有 O(δ^η)幅度；允许s-cell上的 F振幅 O(ρ)，fine到center的位移 O(δ⁻ηρ)，因此平移误差仍 O(ρ)。选原 F-values保留PENCIL/IMAGE的精确像条件，new domain centers无需是源 f的定义点。

quotient g≤1及其K次幂 density由原 G与heavy fibers推出。先构造出的 H有实际uniform slabupper，故 uniform H×H差 law有 line-cap；这里恢复了 finite lemma可用的原标签先验，不再依赖未证明的 Φ_q uniform-slab。整体 countdensity来自(17)，不是把一个相关 marginal直接换成独立方向prior。

最后，coarse fit命中≥ρ^(ε/2)#B时，其span与 bounded F给 ||R||≤K^Cρ^(−ε/2)。附属fine times的误差≤ρ^(3ε₀)+K^Cρ^(1−ε/2)，在1−ε/2>3ε₀及小η下≤2ρ^(3ε₀)，小于 C⁻¹δ^ηρ^(ε₀)这个原SM门槛。heavy time fibers使 fine命中数≥K⁻ᶜρ^(ε/2)(ρ/δ)，当 Cη<με/2且留严格余量时超过原ρ^ε(ρ/δ)upper。所有 R,U均允许为实矩阵，因此大拟合slope没有被非法排除。

先按γ选择ε₀使3ε₀小于finite lemma允许的 a₀，之后选ε，再选η覆盖全部K次损失，顺序可实现且未缩小κ。这里确实排除了指定dense J上的实际PENCIL、IMAGE子族。

## 6. 验收范围

原q/tuple/marginal/终端与τ-window/quotient/SM接口已逐项闭合到本轮finite linewise lemma。其高级扩张输入仍只是所命名的 WZ Theorem13.5；本审查不把它或整篇源文当已独立完全重证。

结论不覆盖一般 F(B)ψ的二维变化、定量近分类以外的更粗误差、其他五维mixed分支、一般管到sticky的归约或Hausdorff闭包。本轮得到的是适当source子族的条件排除，尚无一般Kakeya进展完成标准，也不声称新颖性或重大中间结果。
