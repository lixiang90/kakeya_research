# 下一主目标：N5-COUPLED-PROJ-01

2026-10-17，R0013 macro选定，未证明。只研究明确真实窄子类，主N5-NARROW-GAIN-01仍开放。下一轮须先写working_spec，核本目标是否被新的primary joint投影定理覆盖，不预设新颖。

固定足够小r>0及R,C₀≥1。δ=2⁻ᵐ充分小，Ω_δ⊂[−r,r]⁴；单位方向κ(v)=(1,b,c,d,e)/√(1+|v|²)两两δ-separated，#Ω_δ介于C₀⁻¹δ⁻⁴与C₀δ⁻⁴。每v=(b,c,d,e)指定任意一对anchors f(v),g(v)∈[−R,R]，不要求product、光滑或条件独立。

原axis L_v(t)=(t,bt−d,ct−e,f(v)+dt,g(v)+et)，0≤t≤1/√(1+|v|²)，所以实际长度1。r选得所有axes含公共I=[1/4,3/4)。原tube及参与仍为与axis相交的whole dyadic δ-cubes。只计clock坐标在I内的marks，并直接假设这些marks本身有下述dense mass；不从任意单位管shading丢endpoint tails推它。

把I按δ划成slabs，t_j为中点。令固定

    P={(b,d,f(v),c,e,g(v)):v∈Ω_δ},
    A_t=[[t,−1,0],[0,t,1]], Π_t=A_t⊕A_t.

每j允许任意subset P_j⊂P，要求Σ_j#P_j≥δ^η (#P)δ⁻¹。原方向来源与同一个固定P必须保留；两个blocks共享同一个t_j，不能放宽成独立t₁,t₂。N_δ为固定四维δ-cube covering number，常数改变尺度只损维度常数。

目标：是否有固定σ∈(0,1)，对每ε>0可选η>0、δ₀>0，使

    Σ_j N_δ(Π_(t_j)P_j) ≥ c_(ε,R,C₀,r) δ^(−4−σ+ε)？

在原shading语义中，P_j就是slab内至少有一个原marked cube的indices。每line在slab至多O1 cubes，原transverse cells与Π_tjP_j双向距Oδ，故总union5-volume≈δ⁵Σ_jN_(Cδ)(Π_tjP_j)，原incidence数亦与Σ_j#P_j可比。反向由任意P_j标出相应原axes在slab访问的全部cubes也成立。常数密度改变由先ε后η量词吸收。所有实际incidences满足光滑D场Oδ窄性。这是主NG的一个子类目标，并非一般V_Q的正规形定理。

独立攻击应保方向网δ⁻⁴、bounded anchors、unitlength和原dense mass。单块FO定理仅给固定集合的a.e.-t投影维数；条件化的fibres随t变化，不能直接再调用一次。Product sanity、smooth selector有内点及两marginal满维不算本轮进展。只给一轮joint估计/真实反例/严格新瓶颈尝试，无信息增益即macro换机制，不能靠任意统计条件缩小成已会的情况。
