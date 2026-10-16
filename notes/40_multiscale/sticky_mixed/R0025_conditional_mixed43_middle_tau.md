# R0025：actual mixed43在明确准备下的middle-τ排除

2026-10-17，root。依R24原used-angle gate与本轮finite scalar engine。这里只关闭一个proper alternative；whole-matrix AFF、大τ和完整五维仍不在结论内。

## 1. 原配置与保留条件

保完整actual d5/k4/ell3配置：joint tube AD4、原whole-tube CW、共同原time、Φ/ξ、两套grain。记u,v,a为row2，b scalar，v=a+bu。tildeY_z原本是R内AD维α_Y=1−κ，0<κ≤1；不把vectorY投成scalar缺口。

仍明确条件于原allowedρ∈[δ^(1/4),δ^µ]上的globally dense whole-matrix affine准备，其error Kρ^(1+ε₀)、whole速度lower、原tildeb本尺度upper、合法整time闭包和有限τ稳定删选均已支付。AFF-001只ell2，本文未证明此ell3准备的存在。

原row h(z)=v(z)−b(z₀)u(z)具有vector coefficient-weighted nonquad，所有所用retention losses在physical ε₁、ε₂后取小。vectorτ在选角之前固定，且

    ρ^(3+2ε₁)<τ≤ρ^(3−ζ₁)。                    (1)

上端定义middle-τ范围；更大的τ不使用本结论。

## 2. R24给同一个used-cell proxy下的原图

由R0024 source/angle proof，horizontal3原L/code和incidence-heavy角H给bounded g，存在一个used-cell proxy ψ，保conditional density≥K⁻C，原scalar fine patch×原ν²上的正图满足

    x+S_ψ(t,s)∈N_(Ce) A_out,fine，
    e=K[ρ+ρ^(3+ε₀)/τ]，
    S_ψ=(s−t)[F_ψ(t)−F_ψ(s)−G_ψ(s)(t−s)]。

F/G使用同一ψ与vectorτ，不重设投影τ；exact fine角差随原code可不同，Oρ已进O(τρ)原误差。norm≤K。令p=2ε₁+ζ₁，QSC001同时给原ν下所有scalar quadratic的weighted nonfit：precision σ=ρ^(2p)、质量threshold ρ^β，β≪min(ε₂,γp)。ν有fine base d=δ/ρ、time cap K。

## 3. 先同步空间归一，不能丢F/G幅度

取1≤L≤K^C使|F_ψ|,|G_ψ|≤L，同时将A_input,fine、A_out,fine、F_ψ、G_ψ均除L。新working scale

    w=e/L，F'=F_ψ/L，G'=G_ψ/L

给unit norm和原relation误差O(w)。physical y比例由τ变为τL，fine spatial base r₀=δ/(τL)。ρ小且K loss后小使τL≤1、r₀≤w；并有d≪w，所以原ν的interval cap在所有r≥w可查询。

对新quadratic P，若|F'−P|≤h_new(1+|P₁|+|P₂|)，回原F的误差≤L h_new(1+|(LP)₁|+|(LP)₂|)。因此必须选

    L h_new≤σ，                                   (2)

而不是只说h_new≤σ。空间归一不会改变ν或g的概率prior。

## 4. scalarY的fine输入到w-grid：heavy空间cell而非免费AD-lower

R24的真实τ-patch输入fine cardinal≥K⁻C(τ/δ)^α_Y，输出enlarged patch的fine/card upper及全Y的两侧AD已付。缩τL后，input fine总数N_f≥K⁻C r₀^(-α_Y)；L^α_Y费用在K。每个w-cell含fine labels至多

    P≤K(w/r₀)^α_Y，

carrier w-cell数≤K w^(-α_Y)，此处用full original Y的两侧AD作packing：在每个occupied cell附近选一个原Y点，以固定colour取分离小balls，原AD lower给每ball的fine质量；把这些disjoint balls放入常数扩大patch，以原AD upper求和。不是只凭point-count upper推cover upper，也未给裁切patch重新赋AD-lower。删occupancy<K⁻B(w/r₀)^α_Y的轻cell，总fine参考质量≤K^(C−B)。因g≤1，取B大可使原g损失小于其density一半。保留cells取A_minus的w-grid proxies；每cell occupancy有上下两个K固定幂，因此fineinput law与Uniform(A_minus)双向density可比K^C。按原cell细点平均g、round x≤Cw，得到同ν²上的0≤g_c≤1、mean≥K⁻C。

对输出的常数扩大patch使用相同的full-Y AD-lower/upper packing，得到w-grid A_plus，且

    #A_minus≤K w^(-1+κ)，
    #A_minus≥K⁻C w^(-1+κ)，
    #A_plus≤K w^(-1+κ)≤K^C#A_minus。             (3)

lower来自保留fine总质量与每cell容量upper；没有给任意裁切patch重设AD-lower。原output依关系round增加O(w)，故g_c仍支持x+S'(t,s)近A_plus。α_Y=0时相同计数以指数0成立，所有K费用保留。

## 5. 付所有finite engine参数

取κ_engine=min(κ/2,1/2)。finite engine给允许ε_engine>0，先固定该足够小的数。再令physical ε₁、ζ₁足够小，依ε₀、κ、γ及此engine阈值，使

    6ε₁+2ζ₁<ε₀，
    2p≪(ε₀−2ε₁) ε_engine。                     (4)

非quad质量ε₂以及QSC的β随后固定，最后才取AFF/稳定化/原η损失小。由(1)，w在ρ的两个fixed正幂之间，loss足够小时可保

    ρ²≤w≤ρ^c，c=(ε₀−2ε₁)/2>0。

所以h_new=w^ε_engine满足(2)，因为L≤ρ^(-smallloss)、c ε_engine>2p有严格余量。原nonfit massρ^β≤w^(β/4)，可取engine ε₂=β/4。

再把所有原K固定幂取到小于finite η阈值，(3)给#A_minus≤w^(-1+κ_engine)、#A_plus/#A_minus≤w^(-η_engine)，ν time cap≤w^(-η_engine)、mean g_c≥w^η_engine。δ最后小。真实whole-matrix-AFF loss必须在(4)等fixed精度之后足够小；本文不制造不存在的低损AFF输入。

此时原细time图满足R0025_scalar_curvature_engine.md的全部finite条件，矛盾。因此在明确named BSG/uniform/radial输入及本节真实准备条件下，actual mixed43的(1) alternative被排除。

## 6. 认证边界

本轮支付fine空间heavyframe、同F/G时间sampling、原nonfit与graph的合法preparedprior，以及uniformP共同邻居再生周期/weightedKaufman等finite投影接口。它不需要selected细代表仍有旧atomic ν质量，也不把代表集叫新完整配置。

未证：ell3 wholematrixAFF的存在，large-τ的vector稳定与标量化，mixed43二次alternative、其他五维case、general-to-sticky/Hausdorff。完整高级named证明未全独立重跑；无新维数界、真实Kakeya反例或重大/新颖认证。长期Goal保持active。
