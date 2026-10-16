# R0012宏观转向：真实五维管的三平面窄端点

2026-10-17。新主任务ID N5-NARROW-GAIN-01，尚未证明。不是LIFT-005的进一步分类，也不重开已经冻结的j3 completion。

## 总目标关联与可用文献

在真实R5方向分离管族中，四横截broad部分已有严格超过4的文献维数阈值。主文献HRZ Theorem4.1取n5,k4给p>21/16，对偶阈值21/5；Zahl综述Theorem4.4/Corollary4.5亦列该数。这里是已知broad估计，不能把它直接当一般线性Hausdorff界。HRZ Proposition4.2的broad-to-linear条件另有损失，当前未被突破。

Wang–Zakharov 2026 §2.3指出，高维中间grain情形出现matrix slope。d5、三维方向span对应f(z)∈Mat₂×₂、Φ⊂R²和二维横向集合；不能逐字套标量情形。该文Definitions17.2–17.4及identity(157)可为sticky配置提供参照，但一般方向分离管不自动具有其AD-regularity/global grains。新任务必须保留真实原管和原shading，禁止以泛类模型或新增统计假设冒充几何结论。

## 下一轮要检验的精确端点

固定有界盒、常数C₀,C≥1。是否存在绝对σ∈(0,1)，使对每个ε>0存在η>0、δ₀>0，对所有0<δ<δ₀满足如下结论？

1. T是R5中长度1、半径δ的管族，轴线有向单位方向δ-separated，C₀⁻¹δ⁻⁴≤#T≤C₀δ⁻⁴，全部管在固定有界盒内。
2. Y(T)是管内可测shading，可用相交dyadic δ-cubes表示并只改变固定常数；Σ_T|Y(T)|≥δ^η Σ_T|T|。
3. 每个参与shading的δ-cube Q存在一个**线性三维子空间**V_Q⊂R5，对每个在Q上参与的T有dist(dirT,V_Q)≤Cδ。V_Q可随Q任意变化，不假定连续、可积或globally constant。

目标为

    |U(T,Y)| ≥ c_(ε,C,C₀) δ^(1−σ+ε).       (NG)

具体dyadic formulation需在开轮spec中固定是“Q⊂Y(T)”还是有正测度交，并处理边界常数，不在证明中暗中切换。完整marks是特殊情形，不可证明后只据此声称dense shading版本。

这是真实R5管族的幂增益问题，直接检验能否超越四维投影底线。若只能先证明一个明确较弱但有新几何增益的版本，必须保留实际损失并解释未解决的(NG)接口，不降低Goal最终标准。反例需要真实方向分离管及dense shading；旧quadric随机标签模型缺完整方向来源，不能用于否定此命题。

## 验收与停止条件

一轮主尝试，独立攻击并行。先核四横截文献阈值及已有planebrush结果是否已覆盖此端点，再尝试真正使用沿线的V_Q兼容性或合法的four-dimensional finite input。若遇到二维matrix-growth缺口，要从原几何推导出准确带损失的命题，不能仅重写抽象sum-product或补任意irreducibility假设。

即使(NG)成立，它仍只是角宽Oδ的极窄端点；δ≪ρ≪1的中间角宽、重标度、direction separation/质量损失和多尺度Hausdorff覆盖均未自动处理。不宣称单尺度估计已经解决一般n5或产生Hausdorff改进。若无新几何信息，不继续围绕同一条件做等价Jacobian或density改写，宏观重新选路。
