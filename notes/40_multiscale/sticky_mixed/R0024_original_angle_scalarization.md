# R0024：原slab角先验的二次标量化与实际mixed43接口

2026-10-17，root。唯一main N5-MIXED43-NQ01。B的独立有限证明见R0024_quadratic_scalarization_counterattack.md；A的原图/角law来源见R0024_mixed43_source_audit.md。以下是一个真实角选择gate，不是完整非二次或五维证明。

## 1. 同一原先验上的较强有限引理

ν为有限原时间概率，位置在[-1,1]，相同位置可有多个标签。长≥d的区间I满足ν(I)≤K_t|I|。F:B→R²，不需连续；对每个vector quadratic P，

    ν{|F(t)−P(t)|≤h}≤a.                               (1)

原角差概率π支持bounded R²。假设所有unit n及c∈R、q≥q_base且q≤1满足π{|n·ψ−c|≤q}≤K_ψq^γ，γ>0。超过1的查询用trivial1；低于q_base只能以q_base替代。所有fit系数任意实数。

令 Bad(w,b) 为存在scalar quadratic p使

    ν{|ψ·F(t)−p(t)|≤w}≥b

的角。b≥C K_td、b≤1时，有

    π(Bad(w,b))
       ≤C b⁻⁴[a+min(1,K_ψ max(q_base,4w/h)^γ)].        (2)

固定常数C不依赖time gap、F振荡或p系数。若max参数>1，括号第二项直接取1，不在slab假设范围外调用。

证明要点（完整独立版本见B稿）：time atom质量≤K_td；mass≥b的任一fit中，四个time位置均不同的原ν⁴质量≥b⁴/2。对四distinct时刻，取α_i=1/∏_{j≠i}(t_i−t_j)，按时间位置固定tie-breaking选|α_j|最大。归一化残差

    R=F(t_j)+Σ_{i≠j}(α_i/α_j)F(t_i)

消灭所有quadratic，且每个ratio绝对值≤1。所以scalar w-fit中的四tuple必有|ψ·R|≤4w，无需除最小gap。小残差|R|≤h时，按j=1,2,3,4分别固定其它三个anchors；R=F(t_j)−P_other(t_j)，每项原质量≤a，总≤4a。选j的条件只缩小事件，不改变这个upper。大残差时用原π的slab cap。Fubini并除以fit四tuple lower b⁴/2得(2)。π与原graph不要求独立。

这严格强于R23 spec的uniform-fit候选：该候选多付K_t²/b²。新结果不是由SCAL001 affine证明直接改符号，它使用四点quadratic annihilator及原任意slab先验；仍属初等有限插值，不认证新颖性或重大性。

## 2. 论文所需的系数加权fit：门槛和证明

进一步设|F|≤M、|ψ|≤L于原支集，M,L有限。令A(p)=1+|p₁|+|p₂|；定义 Bad_wt(w,b) 为存在p₀,p₁,p₂，使

    ν{|ψ·F(t)−p₀−p₁t−p₂t²|≤w A(p)}≥b.               (3)

若b≥C K_td且

    w≤c b²/K_t²,                                    (4)

则可用(2)并代w_u=C(1+ML)K_t²w/b²，得到

    π(Bad_wt(w,b))
      ≤C b⁻⁴[a+min(1,K_ψ max(q_base,
                   C(1+ML)K_t²w/(hb²))^γ)].          (5)

这里正是spec中原较弱uniform候选的形状，但现在支付的是更强的coefficient-weighted目标；bounded range和(4)不能省略。

证明：在(3)的fit集合中，用time cap选三个gap≥g=b/(C₀K_t)的真实时刻，C₀固定充分大且g≥d。固定三个value，Lagrange插值的线性/二次系数绝对值之和至多C g⁻² max_i|p(t_i)|；因|t_i|≤1，分母是两个gap，分子系数固定有界。于是

    A(p)≤1+Cg⁻²(ML+wA(p)).                           (6)

(4)保证Cw/g²≤1/2，吸收后A(p)≤C(1+ML)g⁻²。故同一fit以uniform误差w_u成立，再用(2)。三个anchors在每个bad ψ/fit中可不同，因(6)是确定性uniform结论，不导致额外选择概率费用。

### 2.1 精度门槛有实际边界

对任何bounded scalar signal f，任意t₀，令p_R(t)=R(t−t₀)²。A(p_R)≥R。当|t−t₀|≤√w/4且R≥C||f||∞/w时，|f(t)−p_R(t)|≤w A(p_R)。所以只要该短区间有mass约√w，任何signal都存在该质量的系数加权fit，不依赖其非二次结构。

因此不能在无精度门槛时，把uniform scalar nonfit直接称coefficient-weighted nonfit。对uniform time且K_t≈1，b≫√w（等价w≪b²）的当前条件具有正确数量级；这里不宣称常数或所有先验下的必要充分性。

## 3. 原correlated bounded graph的角选择

设原reference为σ_A×ν²×μ×μ，ψ=φ₁−φ₂，π=(差)_*(μ²)。携带0≤g(x,t,s,φ₁,φ₂)≤1，mean=m。它可以任意依赖全部变量；不设独立性。若(2)或(5)给bad angle probability≤m/4，则

    ∫g 1_good ≥3m/4.

并可选择一个真正good角对，使g在剩余x,t,s上的conditional mean≥m/2。更强地，good且conditional mean≥m/4的角对承载至少m/2原graph质量。证明仅用g≤1和概率reference：bad角损≤m/4，good但conditionalmean<m/4再损≤m/4。没有把g-weighted角边际直接当新的独立Frostman先验。

如果在g之前另做time/patch/refinement，须对当时原ν、π、m、K_t、K_ψ重新计费。π若只有带domination常数的slab cap，把常数明确放K_ψ；不能使用unused coarse Phi的虚构cap。

## 4. 实际mixed43的精确条件应用

完整d5/k4/ell3源配置中，u,v,a是row2，b是scalar，v=a+bu；tildeY scalar AD维1−κ，Phi原在R²上有slabγ。先保原time/point/tube AD、CW、Phi/xi与所有grain witnesses。

以下whole-matrix affine准备在本轮仍是明确条件：原allowedρ∈[δ^(1/4),δ^µ]，全局真实retainedtimes上f=(u;v)有affine误差Kρ^(1+ε₀)、whole速度lower，并已付整time闭包及tildeb本尺度osc≤Kρ。AFF001只给ell2；不能把它替换到这里。另假原row-vector h(z)=v(z)−b(z₀)u(z)满足(196)的vector coefficient-weighted quadratic nonfit及真实retainedmass。

在选择ψ前定义

    E_row(z,s)=v(z)−v(s)−b(s)[u(z)−u(s)],
    τ=max(δ,Cρ max|E_row|),
    F_row(t)=(ρ/τ)[h(z₀+ρt)−h(z₀)],
    G_row(t)=(ρ²/τ)[b(z₀+ρt)−b(z₀)]r,

r为u的row2 affine速度。τ、原time删选及τ-patch均用vector norm，不能等选ψ后改τ并沿用原稳定化。原small-τ linearfit排除使τ>ρ^(3+2ε₁)；本应用限定τ≤ρ^(3−ζ₁)。原误差仍保δ直到最终工作e=K[ρ+ρ^(3+ε₀)/τ]。

A稿从原L及used-angle incidence-mixture构造实际used coarse角集H，不给unused Phi_q重设slab；原g在A×B²×H²上bounded/dense，μ=uniformH，π是这些used-cell proxies的差law，有slabγ cap（查询q≥Cρ）和bounded support |ψ|≤C。它仍来自原角质量，但不是exact fine-angle image的uniform law。平移为

    x+(s−t)[F_row(t)−F_row(s)−G_row(s)(t−s)]·ψ
                                  ∈N_(Ce) A_out.     (7)

原ν是fine-index prior，base d=δ/ρ，不强迫B已e-separated。F_row/G_row norm≤K的锚定证明不除以r；为(5)取M≤K、L≤C。由physical nonquad及τupper得到

    h₀≥K⁻Cρ^p，p=2ε₁+ζ₁，
    a≤K^Cρ^ε₂/θ，                                   (8)

θ是相对所引原window的真实retained比例。这里只缩弱成uniform vector h₀-nonfit，所有原小幂费用须后取小。

选σ=ρ^(2p)、b_fit=ρ^β，0<β<min(ε₂,γp)/100；所有K、θ及stablechain损失使K^C/θ≤ρ^(−ℓ)，ℓ再足够小。m≥K⁻C。式(5)的两个principal指数是

    ε₂−4β−O(ℓ)，
    γ(p−2β)−4β−O_γ(ℓ)，                             (9)

都正且可远大于原graph loss；O_γ(ℓ)同时包括K_ψ在幂外的费用，γ先固定后选ℓ≪γp等阈值。base d≤ρ³给b_fit≥C K_td；σK_t²/b_fit²→0付(4)。实际raw slab宽q_raw只须有上界；选合法查询Q_*=Cρ^(p−2β−Cℓ)，令0<p−2β−Cℓ<1，则Q_*≥max(Cρ,q_raw)，且δ小后Q_*≤1。以此更大的slab使用cap即可；不从h₀的lower错误推q_raw的lower。低base clipping因而不妨碍(9)，bad角概率<m/4。

因此存在同一实际used-cell proxy角对ψ，保原coarse g conditional mean≥m/2，且对所有scalar p₀,p₁,p₂，

    ν{|F_row(t)·ψ−p₀−p₁t−p₂t²|
         ≤ρ^(2p)(1+|p₁|+|p₂|)}<ρ^β.                (10)

同时G_ψ=G_row·ψ保原(7)，F/G的选择不使用两个不同的角世界。每个code下的exact fine-angle差可以不同；由proxy到这些细角的Oρ误差已计入原平移O(τρ)。这里没有声称一个固定exact fine-angle pair的原slice仍有K⁻C密度。若还需graph error小于nonfit precision，先选6ε₁+2ζ₁<ε₀，则e≤Kρ^(ε₀−2ε₁)≪ρ^(2p)。全部fixed ε/γ先定、retention/η损失后取小。此门槛是本轮实际原角选择的可付部分。

## 5. 已改变的输入及尚未改变的全局障碍

(10)给实际标量输出分支所需的一个original-prior scalar nonquad输入，且原g关系保留；无需假vector nonquad给每个scalar投影，或把二维Y投成标量亏损。原mixed32做不到这一点是因为其Y本身二维；mixed43从源就是scalarY。

但不能据此宣布scalar22.5/fullmixed43已成：whole matrix AFF来源未付；fine-index代表/weighted projection输入未付；largeτ scalar近常并不使原vectorτ缩小，投影后稳定量与参数仍需另证。source scalar高级定理也未全独立重跑。A另指出ell3 observed A初始只有Nρ≤Kρ^-2，标量ABC21.2的ρ^-1-κ下界在κ<1时不足，这不是ell2 AFF的免费推论。

本轮认证为原slab先验的quadratic scalarization及明确条件下的实际mixed43 gate。无新Kakeya维数界、真实Kakeya反例或重大性/新颖性认证。
