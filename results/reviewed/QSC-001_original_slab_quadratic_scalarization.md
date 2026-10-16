# QSC-001：原slab角先验的二次标量化

2026-10-17，内部交叉审查，未经外部同行评审；不认证新颖性或重大性。证明与实际条件应用见notes/40_multiscale/sticky_mixed/R0024_original_angle_scalarization.md；独立有限证明及反例边界见R0024_quadratic_scalarization_counterattack.md；actual source见R0024_mixed43_source_audit.md。

同一原time ν满足interval cap K_t|I|（|I|≥d），所有vector quadratic h-fits质量≤a，原角差law π在q≥q_base有slabγ cap K_ψq^γ。b≥C K_td时，所有adaptive scalar quadratic uniform w-fits的bad角概率≤

    C b⁻⁴[a+min(1,K_ψ max(q_base,4w/h)^γ)]。

若query超出slab上界则仅用trivial1。四点annihilator按最大Vandermonde系数归一化，避免全部time-gap逆幂；重复时刻有K_td费用。

bounded |F|≤M、|ψ|≤L且w≤c b²/K_t²时，系数加权fit误差w(1+|p₁|+|p₂|)可转uniform误差C(1+ML)K_t²w/b²并用同一界。此门槛不能免费省：任意bounded signal可在长c√w的interval内由巨大系数quadratic按该加权容差拟合。

对同一原correlated boundedg，bad角prob≤m/4则保≥3m/4 graph mass，存在good label的conditional mean≥m/2。实际mixed43的π由原L-incidence marginal domination和heavy-used coarse角cells构造；选择used-cell proxy pair保原coarseg及已付O(τρ)误差，不声称固定exactfine pair原slice有同样密度。

条件于whole matrix AFF、vector nonquad和真实retainedmass，small/middle vectorτ中h₀≈K⁻Cρ^p、p=2ε₁+ζ₁，可取scalar weighted precisionρ^(2p)、fit massρ^β，β≪min(ε₂,γp)，再取损失小。全部坏角prob小于原g密度，支付实际original-angle gate。

尚未付：ℓ3 AFF、原weighted fine-time scalar growth/projection输入、largeτ projected stability或fullmixed43。没有新维数界、真实Kakeya反例或重大性认证。
