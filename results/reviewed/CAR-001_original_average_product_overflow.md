# CAR-001：原time×angle真实乘法的平均overflow门槛

2026-10-17。内部独审有限结果，未认证新颖性或重大性。完整证明notes/40_multiscale/sticky_mixed/R0028_factorized_action_counterattack.md；独审research/reviews/R0028_carry_and_boundary_review.md及R0028_original_action_review.md，root整合另存。

原time概率ν满足interval cap Ktℓ（ℓ≥d），原angle差lawπ对每个affine slab在q≥qbase有Kπq^γ upper。B≥B₀(γ)固定、N偶、r=B^-N，d≤r、qbase≤sqrt(r)。固定j，X=frac(|t−s|)、Y=frac(|ψ_j|)的标准非负base-B digits记d_i,c_i，定义Z=#{i≤N/2:d_i c_i≥B}。则

    Pr_{ν²×π}(Z≤γN/8)≤CKtKπ r^(γ/4)。

任何原μ_A×ν²×μ_H² reference上的bounded相关g只付mean(g)^-1；不为条件law假独立digits或slab。每个所计even raw position在真实非负乘积中必有向上carry，故完全无carry或o(N) raw-overflow的实现只能占固定正幂质量。

carry数量不推出carry-correction熵、输出cover或growth。没有构造/排除全部允许carry的factorized反模型，未证明AFF₃，没有Kakeya反例或新维数界。仅用原slab upper，H的未证κ-AD lower没有被使用。
