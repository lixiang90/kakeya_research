# 下一候选：N5-PRUNED-MULTIPLICITY-01

2026-10-17，root。CP未解。该候选保持R0014全部数据和任意耦合anchors，不缩为product或光滑selector，不新增统计假设。它是一个尚未证明的质量命题，足以给CP；目前未证与CP等价，单凭union计数不能形式反推所需质量。

固定P、Ωδ、共同I、Π_t及原P_j如R0014_working_spec。以固定半开四维δ网格给每个输出Π_tj p分配唯一cell Q，令

    m(j,Q)=#{p∈P_j:Π_tj p∈Q}, S=Σ_(j,Q)m(j,Q).

因此δ^η#P δ⁻¹≤S≤C#P δ⁻¹，#P≈δ⁻⁴。每个(p,j)仍是原选择，没有增加几何近交或改变anchors。候选PM为：

    存在固定τ∈(0,1)，使每ε∈(0,τ/4)可选η>0、δ₀>0及Cε,cε>0，
    Σ_{m(j,Q)≤Cε δ^(−1+τ−ε)} m(j,Q) ≥ cε δ^ε S.    (PM)

σ=τ的CP随即成立（误差可重命名）：所计低重数cells数至少

    cε δ^ε S/[Cε δ^(−1+τ−ε)]
       ≥ cε δ^(−4−τ+η+2ε).

对CP给定的最终误差ε₀，内部ε≤ε₀/4且η≤ε₀/4便足够。可以进一步减小η，因为dense hypothesis随η减小更强。候选只要求保留subpower比例原incidence mass，没有免费要求常数比例管数。一个union计数下界可能来自质量极小的cells，所以仅该数值下界不自动给PM；这里未给真实CP系统中二者不等价的反例，也不声称已证明严格逻辑分离。

## 新机制与已知攻击

R0014 caustic构造严格阻止不剪原marks的统一L2改善，但其坏时刻可丢去相对很小质量。故新任务是**从所有实际数据证明可保留的低重数质量**，不是再次猜未经修剪E₂ upper。可尝试四cycle固定首边packing、时间两端/重数分层与full方向cap；五cycle退化可作辅助，不继续增加polygon长度。δ近环损失Cδρ⁻²必须记录，取ρ=δ^a时只能付δ^(1−2a)，不能免费取细时间网。

完整方向投影对所有D-deficient affine sets给derived upper：若一个bounded参数子空间Z的方向投影维数l<4，则D(P∩N_ρ(Z))在一个l-plane的Cρ邻域内，原分离packing给概率≤Cρ^(4−l)，ρ≥δ。这只是直接可用的上界，尚未导出高重数质量的逆定理；不能把“PM失败便集中于此类Z”未经证明加入假设。

一手GGW/CSWZ/Du/Gan的已核定理没有直接提供这项相对质量结论；新primary审计所列pencil退化不能靠删dense time family消掉。若用新文献，需要重新核其对原图与原shading的量词。

只给一主轮：检验PM证明或保所有原量词的反例，至少须得到严格的质量收缩/修剪估计。重复caustic算术、只改阈值、smooth例、先假定无坏cycles、仅将目标叫relative nonconcentration都不计信息增益。无实质质量进展则macro冻结此子类的局部迭代，回到一般五维几何/源证明新机制。没有新维数界或重大结果，长期Goal active。

2026-10-17 R0015更正：上文“未证等价”是R0014当时状态。原CP量化所有P_j，允许保留完整high cells后再次调用，故CP(σ)推出任意τ<σ的PM，甚至常数1/2低重数质量。结合反向，存在正gain层面等价；详见R0015_uniform_shading_closure.md及独审。未证明其中任何一个，停止把PM当独立新机制的局部迭代。
