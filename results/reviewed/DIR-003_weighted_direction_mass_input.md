# DIR-003：方向格质量控制下的加权有限尺度输入

2026-10-17，R0009，N4-DIR-01。**条件结论：依赖SRC-001，因而依赖整篇所给四维证明及其全部输入正确。** 本项目没有独立重证该论文。方向放大和加权化约是初等工具，不声称新颖性、重大中间结果或新的Kakeya维数界。已内部独审，未经外部同行评审：research/reviews/R0009_amplification_review.md、R0009_weighted_source_review.md；root接口复核见R0009_root_integration_review.md。

## 精确结论

固定R及四维graph chart，L_i(t)=(t,b_i+t v_i)，0≤t≤1，|b_i|+|v_i|≤R。对每ε>0，存在η>0、δ0及Cε,R，使0<δ<δ0时，下述有限indexed family满足

Σ_i ω_i #J_i ≤ Cε,R α δ^-ε #E。

这里ω_i>0任意，indices允许重复；J_i为δ时间网格中至少δ^(-1+η)个marks；E为全部marked visits的四维δ-cells（允许固定扩大）。每个半开边长δ的slope cube Q满足Σ_{v_i∈Q}ω_i≤α。常数不依赖总权、最小权、权重跨度或indices数。

若轨道未归一化law的实际三维visible-slope密度≤A·Lebesgue，则方向格质量≤Aδ³，结论成为Σω_i#J_i≤Cε,R Aδ^(3−ε)#E。对于原子方向律，只有bin质量陈述，不声称与Lebesgue密度等价。

## 证明链与量词

1. 对M个δ-separated slopes，以有界shear S_a(t,y)=(t,y+t a)复制。其方向δ邻域体积≈Mδ³，K≤C_Rδ^-3/M个独立均匀slope shifts可在期望中覆盖固定正方向体积。故存在这样的有限shifts，并能取出≈δ^-3个固定尺度separated directions。时间不变，重分ρ=Cδ网格每bin仅合并固定个marks，union cells≤C_R K#E。
2. 对目标σ=ε/2调用SRC-001取得ηsrc，原η≤min(ηsrc/2,σ/2,1/4)。小δ吸收全部固定常数后，放大family满足SRC-001的near-full数量及逐线marks门槛。因此#E≥c_R,σ Mδ^(-1+σ)，对所有1≤M≤C_Rδ^-3一致。
3. 将方向格作固定有限coloring，使同色不同格中的任意代表都δ-separated。每个非空格任选一个原index，保留其自己的marks；代表footprint包含于E。第2步对每个颜色给非空格数≤Cδ^(1−σ)#E。所有原marks数≤δ^-1、每格总权≤α，故Σω#J≤Cαδ^-σ#E≤Cαδ^-ε#E。

无需按权重分层、样本数集中或以小总质量归一化。即使一个格只有极小权重，其代表的footprint本来就在E中，非空格计数仍然合法。

完整几何与参数证明：notes/40_multiscale/plank_inputs/R0009_sparse_direction_amplification.md。权重、重复indices与实际source调用审计：notes/40_multiscale/plank_inputs/R0009_weighted_direction_reduction.md。

## 连续law的分析性版本

同样结论适用于固定有界chart中的有限正测度ν：几乎每个保留轨道的marked bins不少于δ^(-1+η)，E包含其全部marked visits，ν的每个方向格质量≤α。正质量格有限；在每个格内从上述full-measure轨道集合任选一个实际代表，即可逐字使用第3步；∫#J(l)dν≤δ^-1ν(all)≤δ^-1α×正质量格数。未假设原轨道离散，也不需要把所有可能mark patterns作为输出labels。

如果从可测incidence selection生成marks，先保留时长≥δ^η的轨道，则每条至少δ^(-1+η)个非空时间bins；把实际selected点移到bin center只需固定cell扩大。所用代表仅为估计，未声称是满足原观察知识约束的chart labels。若仅有平均长时密度，必须先删轻并跟踪损失。

## 原始source中能得什么

源初始三维visible-slope ceiling A为subpower时，本估计与原whole-cell witness及逐线长duration结合，排除projected zero-depth density的固定幂增益。若A=N0^κ则只排除超过κ的增益；固定分析网格ρ=N0^-D上的损失是Dε，须先固定D再选ε及慢对角。

一般parent的visible ceiling变换为A_new≤A_old|det D|/[q³ν(parent)]；full(V,W) ceiling另为C_new≤C_old|det D|/[q⁴ν(parent)]。二者不同。原始未归一化restriction保留旧cap，normalized parent必须支付分母及坐标成本。

因此该条件工具能严格实现有方向来源的专用zero-depth调用；不能替代无方向WP4，更未恢复generic j3 completion、critical optimization或高维几何论证。HOR-001允许大A≈δ^-1，本估计支付该代价，二者相容。
