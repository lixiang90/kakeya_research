# R0013：真实五维管的点态三平面窄端点

2026-10-17。起点R0012 commit fe5670596a8aff74971b1b20552f623c9dce469b，185文件回执和干净树已核。上一Goal turn分类progress：LIFT-005完整受限类分类、独立审查、宏观转向及远端同步均已完成。Goal active，最终标准不变。

## 唯一主任务：N5-NARROW-GAIN-01

固定C₀,C≥1和一个有界盒。在R5取长度1的轴线段ℓ_T，单位方向v_T彼此δ-separated，C₀⁻¹δ⁻⁴≤#T≤C₀δ⁻⁴。用cubical δ-tube表示原管：T为所有与ℓ_T相交的半开dyadic δ-cubes的并，故|T|≈δ⁴，且包含在轴线的C₅δ-neighborhood内。每个Y(T)是T中选定的whole δ-cubes的并，参与定义固定为Q⊂Y(T)，不使用任意小的边界交。原shading满足

    Σ_T |Y(T)| ≥ δ^η Σ_T |T|.

每个参与cube Q有一个线性三维子空间V_Q，使所有Q⊂Y(T)的T都满足dist(v_T,V_Q)≤Cδ。V_Q可以随Q任意变化，无连续/可积/全局一致假设。

是否存在固定σ∈(0,1)，使对每ε>0可选η>0、δ₀>0，对所有0<δ<δ₀，有

    |U(T,Y)| ≥ c_(ε,C,C₀) δ^(1−σ+ε)？        (NG)

采用cubical formulation固定边界，保持每个参与label和原质量。若换round tubes，仅作常数半径扩大并保同一Y标签；不得将新增几何交强加为shading incidence。若证明只处理full marks，必须单列限制，不能冒充上述dense版本。

## 总目标关联与分工

primary HRZ Theorem4.1的n5/k4 broad对偶阈值21/5，关键未知是窄结构能否给超越四维底线的幂gain。即使本端点成立，中间角宽、多尺度重标度及Hausdorff覆盖仍未自动解决。旧formal j3模型缺完整方向来源，不是本任务反例；一般direction-separated不自动sticky/AD正则。

root研究真实planebrush/沿线V_Q兼容性；互补审查1核一手现有planebrush和高维narrow估计是否已经覆盖(NG)，核shading与量词；互补审查2独立尝试真实满方向构造及几何攻击，识别任何拟用兼容性引理的精确缺口。不得改回completion或对旧反例作统计修补。

## 本轮验收及停止

给(NG)证明、真实管反例、已有一手定理的精确适用结论，或从实际原管推出有新信息且损失明确的几何命题。仅整理旧Jacobian、假设matrix irreducibility、重复旧投影障碍都不计结果。若未闭合，明确仍缺哪项新的 incidence estimate，进行macro后决定是否有新机制再给一轮。每轮归档、独审、更新并同步同一local/remote commit。
