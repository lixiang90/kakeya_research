# BND-001：真实列表与真实floor不自动压缩全局palette

日期：2026-10-16，R0004。状态：内部独立复核通过，见research/reviews/R0004_boundary_entropy_review.md。未经外部同行评审，不声称新颖性。

存在五维仿射轨道的单world有限半代数full-coefficient prior，同时具有：完整四维斜率边缘密度1；整块不变、同层互斥的真实assignments；own-depth常数列表；逐chart真实floor与saturation；总质量1/32的系统覆盖；而同一原始坐标下方向二次式在精度η/4仍需要至少η^-1个palette中心。

完整构造与证明见notes/50_counterexamples/R0004_list_floor_palette.md。参数满足a=q、q²≤η≤q、σ≪η。空间矩阵列为qA、ηB、q e3，J=q²η(1−t0²)，完整prior质量ν=q³η/16，selected mass=qν，hidden观测的真实密度n(a)≈a。

取η=q²时，全局palette数至少q^-2，点态列表仍为固定常数。原始slopes完整有界密度，大的full-coefficient密度只在截距方向，并未偷换为方向浓度。

**必要边界：** 这是d=1模型，不满足d<1的密度亏损；H未计算，未认证native Hessian来源或临界最优化。它否定的是仅靠assignment/list/floor的小palette结论，不是完整高维Kakeya反例，也不排除加入d<1后的新机制。
