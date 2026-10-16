# OBS-002：generic nonplanar law与多尺度observed粗图不足固定增长

2026-10-17，严格finite反例，内部交叉审查。完整证明 notes/40_multiscale/sticky_mixed/R0027_digital_observed_boundary.md，独立证明R0027_matrix_observed_counterattack.md；两独审在research/reviews。

任意预给small loss η>0、固定nonfit精度指数ε>0，取足够大固定B=2^L及任意深偶数N，r=B⁻N。f为二进制奇block保留mask，A₀={(x₁,x₂,f(x₁),f(x₂))}有r⁻²点；A=A₀+A₀包含A₀，λ=UniformA₀，g=1_(a∈A₀)。真product reference上mean(g)≥r^η，所有正权满足exact a+d∈A。

同一A保card在r⁻²的小η幂内、UniformA 2Fst及每个dyadic R≥r的visible R-cell上joint R-cover≤r⁻η。carry-pattern显式恢复，不假没有进位。λ对所有affinehyperplanes有C_B q^1/2 cap，故在q=r^ε处对所有affine2planes有fixed正幂cap，独立于η。仍有#A≤r⁻²⁻θB，θB=2logB(2−1/B)→0，否定只依fixednonfit参数的uniform >2gain。

本模型没有λ的共同ν/M/原Φ matrix-time分解，也不验证jointtube AD/CW/两grain/W witnesses。因此没有反驳OBS-001、actualAFF₃或Kakeya；它否定的是把原增量换成任意非平面law的增长桥。不是digit derivative/Leibniz，所有运算是真实实数加法。无重大/新颖性认证。
