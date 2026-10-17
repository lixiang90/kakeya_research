# R0067：联合纤维、原质量及 AFF 分辨率边界独立审查

2026-10-18，B。独立逐式审查终稿；未经外部同行评审。

## 1. 实际读取范围与审查对象

已 fresh 实际全文读取 root `R0067_shared_trunk_hybrid_and_affine_attempt.md` 14 节、A `R0067_common_trunk_source_and_mass_audit.md` 18 节、本轮 spec 5 节、macro 6 节、next `R0067_next_whole_matrix_affine_from_original_joint_data.md` 6 节，并读回 B 自身 10 节。另实际核对 WZ2609.22035v1 Def17.2–17.4、§19.1 的 W 恒等式及 §22.1 的 native V/J/L 恒等式。

本正式审查独核 root/A 的完整有限 core、Gram、初角边际、两端 matching、共同码恢复、原分母及 AFF 停止点；B 自身施工不计作对自己的独审。A 对 B 及 root 的反向审查另行归档。没有认证尚未写入的元数据、Git/sync 或外部同行审查。

## 2. 共同主干计数与原先验核算

三类有限 peeling 的损失均按原 vertex 充电一次，而非按迭代次数付费。root 的 edge-threshold 版本及 A 的 point/tube/grain-point 版本都保常比例原 incidences，并确给点管数、管实际 local visits、grain 实际点数三个 K 次幂 lower。原 grain 数只由 native Y 的原 AD packing 作 upper；未给裁切 grain 免费 filled lower，core 亦没有被重新宣成 Def17 配置。

对同一初 arm 使用 `X_α⊗Y_α`，恒等式 `Σ_(α,β)<X_α,X_β><Y_α,Y_β>=||Σ_αX_α⊗Y_α||₂²` 保同一 p,t,s,T₁,T₂。native 标签簇来自原全 q 残差条件与 V 公式，方向签名 carrier 的 τ-coherence 查询已付邻接 allowed-grid 费用。因此 root (7)/A (8) 的

    #H≥K^(−C)eD⁶m³ρ^κτ^κ(ρ/δ)³(τ/δ)³

成立；没有把两个分别 dense 的图免费相交，也没有假任意两个原 grains 有大交。

root (8)/A (12) 对固定初 incidence 的上数与总 lower 匹配，足以重做 hybrid 自己的两初角 marginal。heavy used ρ-bins 的删除保 K 次幂 hybrid mass，Uniform(H) 的 slab upper 来自原逐点 Φ、原 incidence mixture 与实际 heavy lower，而非 unused Φ_q。fine times 保原 Uniform(Z_q)，相关性全部留在 g；未赋任意条件 slice 的独立 time/angle 或 AD lower。平均原 incidence 与 core 局部逐管 lower 的分母分别交代正确。

## 3. 两端 normal 匹配、完整纤维与产品图

独核 root (10)–(16)、A (19)–(26)。固定 u,v,Q_W 后，`η_u=q₂−d_uq₁` 不依 W 的 visible x；一臂输运相减给 `η_v−η_u=(v−u)ζ_q+(F_u−F_v)U_q+O_K(ρ²)`，故 native τ-patch 只需 K 个 compatible 选择，确可作为共同 B carrier，而非依 A_W 的 conditional patch。

先枚举 W/L 第一末管的两个 ρ 包及第一 fine jump 水平坐标。反向 W 输运给 `η_s=η_u+C_W+O_K(ρσ+δ)`。此时固定 jump 的 p̃₁ 只占 K 个原 σ-cubes；逐 cube 的原 ξ representative 给正向 `η_v=η_s+C_L+O_K(ρσ+δ)`。C_L 在该有限分包内不依未观测 fine η_u。证明未假 ξ 沿 grain 恒定、对 η 连续或全局 Euclidean Lipschitz。指定 native e_L-bin 因而以 native Y_u AD upper 把 w₁ 容量降至

    K(σ/δ)³(e_L/δ)^(1−κ)。

两个粗包与包内 fine 管的费用恰是 `ρ^(−2κ)L^(2κ)=D²`。其余原管、两 jump、原 fixed-time 交点皆已计入 root (15) 的

    M_H≤K^C(σ/δ)³(e_L/δ)^(1−κ)
                 ρ^(−2κ)L^(5κ+3)(τ/δ)^(3+κ)。

完整 frame 包含 u,v 的 m²、W 的 `(ρ/σ)^(2−κ)` 标签桶、A_W 的 `(ρ/σ)²`、native 的 `(τ/e_L)^(1−κ)`、原 t,s 的 m² 和 H²。与总 H lower 相除，净额确为 `K^(−C)(σ/τ)^(1−κ)`。天然 `τ≈_Kσ≈_Kρ²`、`e_L≥C_K(ρσ+δ)` 时这是 K 费；δ≤ρ⁴ 支付 floor。一般 τ 接近 δ 的陈述仍保 `τρ+δ`，没有越过 fine base。

每码原重数除统一 M_H 得真正 `0≤g≤1` 的同 product-reference 图，平均 ≥K^(−C)。input lower 来自 g≤1 与真实码 lower；不是从 AD upper 倒推。邻接扩大两种 output 桶后同样有 packing upper，output/input ratio 可付 K。此处两端条件限制的是尚未枚举的 w₁ normal 纤维，不是错误的 exact-trunk 单边 normal diffuse cap。

## 4. 反攻、AFF 用途与下一任务边界

parallel-native 校准保 grains、straight clock、angle/coherence 与原局部度数，却在 δ-plate 上 CW 损 δ^(−κ)。它只否单边 cap，既不是完整正 κ source counter，也不反两端 matching。历史 generic recovery 的固定幂损失只是过粗保证，root/A 已明确撤去其“天然图仍未付”的旧解释。

联合主位移仍满足 `S_L=(s−t)(V_b−d_sV_a)`。写 `h=b−d₀a` 后，coupled 项的 physical 位移为 O_K(ρ³)，在天然 native 归一化后落入 O_K(ρ) 工作误差。即便日后另付 h-row fit，也不控制自由 row a；当前稿未声称 h-fit 已由 scalar inverse 完成。ell Y 没有额外 line-KT，不能借 R16 的不同 source case 排除剩余自由度。

finer τ 时 `ρ³/τ` 是现有 matching 证书的 blur upper，不是所有方案的必然 lower。sub-ρ 末角 packing 的环境成本同样只描述当前证书。root §12 已补本审查提出的另一责任：ell normal-label 主项 `(s−t)(f_t−f_u)ψ` 仍为 O_K(ρ²)，不能随末角 α 免费把 Q_W 与 Q_W^+ 同缩到 ρα。此修补防止误用，不影响天然尺度正证。

macro/next 保 whole-matrix AFF₃ 的原完整量词、整 time 回传及 shading 质量；没有以 partial h 后果、附加 regularity、条件化独立性或旧 uniform gain 换名作完成。停止重做 core/Gram/天然尺度常数，下一必须付第二 row 或原质量上的 coupled 信息，边界合适。

## 5. 依赖、修正与未认证责任

本轮 finite 数学在以上原供应下通过。仍具名依赖原 good-q 数据、Def17 的 AD/coherence，以及 Lemma19.5 整 time 细化和 R22 restriction 闭包；必须先付这些准备再重新 good-q/core。其高级 wholeproof 没有在本轮重新独证，亦未从本图认证整篇 WZ 或一般高维 Kakeya。

已核修正包括：generic τ 的 δ-floor；天然尺度才用两端细 matching；两 terminal bucket 的原 m² 和 patch 费用；hybrid 自己的初角 marginal；coarse ρ 包拆 D²；finer 方案的 ell normal 主项；原 upper 证书与普遍不可行 lower 的区分。**当前终稿无强制修改项。**

## 6. 正式结论

在列明的完整 source 供应及天然尺度范围内，root14/A18 的 shared-trunk hybrid lower、原角/time reference、两端 normal 纤维引理及 bounded product-reference 联合图通过本次独立逐式审查。AFF₃、完整 mixed43、ordinary/general 增益仍未证明；本轮可归档为已付联合接口及精确用途边界，不认证新 ID、新颖性或 major。

未经外部同行评审。Goal active；本审查完成后停止编辑与检索，元数据、验证和同步由 root 按真实结果统一处理。
