# R0027：真实矩阵平移law的二维仿射平面非集中

2026-10-17，root。唯一main为ell3矩阵AFF₃前端。本稿证明一项带原质量的finite gate，并给actual source应用；**不**由此宣称observed集合已有>2的加法增长。与旧Y-only接口不同，这里的平移同时保二维visible x和二维ξ。

## 1. 有限命题与全部量词

ν为[-1,1]上有限时间概率，位置可带多个labels，所有长度r≥d的区间满足ν(I)≤K_t r。M(t)∈Mat(2,2)，operatornorm≤1；对每个real matrices R,C，

    ν{t: ||M(t)−tR−C||≤h}≤a，                     (1)

0<h<c，h≥d。π为bounded R²中原角差概率，|ψ|≤1（其它固定bounds只改常数），对所有unit n、all real c、q_base≤q≤1，

    π{|n·ψ−c|≤q}≤K_π q^γ， γ>0。                 (2)

不要求π是Lebesgue、time函数可微或R/C有界。本finite prior明确是ν²×π；原几何的相关性稍后全部以bounded g计，不对g-weighted边际另加独立假设。

定义原平移向量

    D(t,s,ψ)=((t−s)ψ, −[M(t)−M(s)]ψ)∈R⁴。

任意affine 2-plane P⊂R⁴都满足，若q_base≤h，

    (ν²×π){dist(D,P)≤h⁴}
           ≤a+C K_t h+C K_π h^γ。                (3)

更一般的base-clipped版本把h^γ换为max(q_base,Ch)^γ并在超出1时取trivial1。常数固定不依P、slope/intercept、fine-label数；γ先固定，所有固定倍可用C_γ记。dim≤2的plane可嵌入2plane，故也满足。

## 2. 用正交块分解而非假设plane投影可逆

写P={z:Qz=c_P}，Q:R⁴→R²正交quotient，QQ*=I₂，分块Q=(A,B)，A,B∈Mat(2,2)。于是

    AA*+BB*=I₂， ||A||,||B||≤1。

设ε=h⁴、λ=h²、g=h。下列两case穷尽所有P，包括几乎vertical或投影退化的plane；不能预设P是有界slope图。

若σ_min(B)≥λ，则D近P蕴含

    ||([M(t)−M(s)−(t−s)B⁻¹A]ψ)+B⁻¹c_P||
                            ≤ε/λ。                (4)

固定R=B⁻¹A。对每s，矩阵residual N(t,s)=M(t)−M(s)−(t−s)R的norm≤h事件，就是(1)中C=M(s)−sR的真实fit，故其ν²mass≤a。对norm>h的每个(t,s)，选unit output ℓ使 |N*ℓ|=||N||（finite labels可任意tie-break），将(4)左乘ℓ并除|N*ℓ|。它限制ψ到一个原affine slab，宽≤ε/(λh)=h。中心含B⁻¹c_P，可以任意大；(2)本来对所有中心成立，不限制P offset。对π先积分，再对ν²积分，该case≤a+K_π max(q_base,h)^γ。

若σ_min(B)<λ，取unit w∈R²使||B*w||<λ。由AA*+BB*=I₂，||A*w||≥sqrt(1−λ²)≥1/2。D近P给

    |(t−s)(A*w)·ψ−w·c_P|
          ≤ε+||B*w|| ||M(t)−M(s)|| |ψ|
          ≤ε+2λ。                                 (5)

先删|t−s|<g，ν²mass≤C K_t g（g≥d保证合法interval查询）。余下(5)是ψ的原affine slab，宽≤C(ε+λ)/g≤Ch。故该case≤C K_t h+C K_π max(q_base,Ch)^γ。固定h小使Ch≤1；若不小，只用trivial1。合并得(3)。

这证明**完整matrix** nonfit到二维plane nonfit，不把某个scalar row非线性当所有rows非线性。结论不扩展为所有3planes：若M有一个affine row，D完全可以落在一个3plane，(1)仍可能成立。

## 3. 原bounded g与coarse geometry：不能重置law

若原reference为σ_A×ν²×μ²，ψ=φ₁−φ₂且π=(差)_*(μ²)，0≤g≤1，任意P有

    ∫g 1_{dist(D,P)≤h⁴}≤a+C K_t h+C K_π h^γ。       (6)

不需要g与这些变量独立。若mean(g)=m，则conditioned graph概率upper为右端/m；特别右端≪m时原densegraph不能全部落在一固定2plane邻域。P可在看过原数据之后任意选择，因为(3)对所有P同时是一个确定性statement，不对无限plane族作非法概率union。

若fine D与每个所保原label的coarse proxy D_c相距≤r_err，事件dist(D_c,P)≤h⁴/2在r_err≤h⁴/2时包含于fine事件dist(D,P)≤h⁴。若换uniform coarse prior，须用heavycell occupancy的双向密度及角碰撞factor显式乘K固定幂；不能说all-real matrix affine nonfit自动经未知slope的clockrounding传递。本应用先在fine law证(3)，再传**D事件**。

## 4. actual d5/k4/ell3的真实接口

完整原W/observed/counting证明见R0027_observed_matrix_source_audit.md。沿原Definitions17.2–17.4、19.1(151)/(152)，在合法good-q和末层厚grain桶中保留

    A_phys={(x,ξ_p): x∈R², ξ_p∈R²，末y在σ=ρ²厚桶}。

同一个原W code给

    Δx=(z₂−z₁)ψ+O(Kρ²)，
    Δξ=−[f(z₂)−f(z₁)]ψ+O(Kρ²)。                  (7)

取实际1≤L_f≤K控制f/ξ窗口幅度，同步空间/函数归一

    a=((x−x₀)/ρ, (ξ−ξ₀)/(L_fρ))，
    t=(z−z₀)/ρ， M(t)=[f(z)−f(z₀)]/(L_fρ)。

可再固定倍缩放使M/ψ unitbounded；(7)成为a₂=a₁+D(t₂,t₁,ψ)+O(Kρ)。也可反射ξ同时取正M版本，但不能原式反号后单独换B而漏Lf。原A在working r=K₀ρ上card在K固定倍r⁻²内，每visible coarse x-cell fibre≤K；还可保多尺度coarse-x fibre upper及UniformA的(r,2,K)Frostman。它们不是任意点集的“graph”属性，来源是原ξ-coherence与真实bucket容量。

原W bounded dense g在A×fineν²×H²上构造，mean≥K⁻C；H是原incidence重角cells，UniformH及其差π有合法slabγ（q≥Cρ）。raw unused Φ_q不自动slab。g可任意相关，使用(6)而非g边际cap。

假设固定尺度反证准备已给whole f在原window的ρ^(1+ε₀)-affinefit至多a_phys比例；后选good-q付真实K因子。fine M在h₀=ρ^ε₀/L_f处fit≤K a_phys。取

    h=ρ^(2ε₀)， h⁴=ρ^(8ε₀)， ε₀<1/32，

所有source losses后取小，使h≤h₀、d=δ/ρ≪h、q_base=Cρ≪h以及Kρ≪h⁴。故(3)/(6)真可查询，右端≤K a_phys+C K^Cρ^(2ε₀)+C K^Cρ^(2γε₀)，在a_phys固定正幂、source loss足够小时是正幂且≪mean(g)。

若source选均匀coarse frame，按第3节先传fine D事件再付heavycell比率；没有从bounded F免费选代表或忽略|R|r。ρ不在allowed格的取整代价均在K，固定半开window/time闭包保持。矩阵AFF₃存在尚未从这些条件推出。

## 5. gate的真正边界

已付：保实际visible坐标和原角law的D不集中在任何固定2plane附近，且保真实原boundedgraph质量。这是一个不同于scalarABC lower≤2的可审matrix接口。

未付：由此推出A+restrictedD的>2增长、wholematrixAFF₃、source完整高维分支。R0027_digital_observed_boundary.md给严格模型：即使保所有多尺度visible fibres、2Frostman、D的更强hyperplane nonfit，仍可有任意小幂加法增长。该模型特意没有D的原matrix-time分解，因此不反驳本稿或完整source；它精确说明**下一步必须继续使用原(t,s,ψ,M)关系**，不能把D替换任意非平面law后引用flattening。

本文为内部证明/审查范围，无新Kakeya维数界、真实Kakeya反例或重大/新颖性认证。原named几何高级证明未全独审，长期Goal active。
