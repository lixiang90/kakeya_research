# 下一主目标：N5-STICKY-MATRIX-01

2026-10-17，R0015宏观换路。未证明，不作为已有输入。目标是真实sticky五维配置中尚缺的2×2矩阵非线性分支；不是一般管族已有sticky归约，也不是CP/PM改名。

固定ζ,κ>0、γ∈(0,1)、ε₀>0和μ∈(0,1/4)，参数κ限在source配置可定义的范围0<κ≤2。是否存在ε>0，继而存在η₀>0，使每个η<η₀均可取δ₀(η及全部先前参数)>0而有以下结论？参数依赖必须保持source Lemma20.3顺序，必要时明确细化ε₀的上界，不能途中把固定亏损κ变小，也不声称δ₀对η统一。

给任意η<η₀及δ<δ₀，一个R5中3-planar、3-linear的(δ,η,κ,γ)-Kakeya配置，**完全满足Wang–Zakharov Definitions17.2–17.4**，特别保原(4,δ⁻η)-AD tube family、原管通过关系、CCW≤δ⁻η、跨尺度Φ_p/ξ_p相容、Y_z的tube Katz–Tao、跨时间AD及dense horizontal grains。其f:Z→Mat(2,2)。

对某个source允许的ρ∈[δ^(1/4),δ^μ]，假设对每z₀∈Z、包含z₀的dyadicρ-interval J及每R,U∈R^(2×2)（任意实矩阵，不限entries），都有矩阵nonaffinity

    #{z∈Z∩J: ||f(z)−zR−U||_∞≤ρ^(1+ε₀)}
        ≤ρ^ε (ρ/δ).                                  (SM)

目标结论κ≤ζ。这是将原Lemma20.3的真实配置和(163)逐项改到d5/k3的字面候选，而非任意matrix graph定理。原Lemma20.2对Mat2已处理dense local-affine分支，调用前还要核完整source依赖和细尺度损失。

主目标是整项(SM)排除结论。新向量和积引理若只适用于额外irreducible系数，必须同时说明可约分支如何从原source推出grain改善；不能据此宣布主目标成立。He及He–de Saxcé工具的假设/闭包成本在R0015_source_matrix_reset.md列出，未验证前不能直接使用。

下一轮先working_spec，至多两个互补审查：一项核真实L-tuples/线性branch及原权重，另一项攻击向量和积或可约分支。须有真实联合扩张估计、原配置反例或严格收缩的未闭合分支；不以线性代数校准或scalar projection满维充数。若一主轮无实质新信息，宏观换机制，不退回无来源的formal j3模型。成功也只解sticky关键分支，不自动完成mixed cases、一般五维/Hausdorff或长期Goal。
