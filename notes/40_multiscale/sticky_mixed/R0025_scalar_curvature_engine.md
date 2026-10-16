# R0025：保prepared先验的scalar curvature nonexpansion engine

2026-10-17，root。目标是实际mixed43的一个conditional middle-τ alternative。以下有限定理条件于明确的既有高级输入，不是自包含重证四维论文，也不是完整高维Kakeya。

## 1. 有限定理、输入与量词

固定0<κ<1。存在ε_*(κ)>0，使对每个0<ε<ε_*、ε₂>0，存在η_*(κ,ε,ε₂)>0，以下数据在η<η_*、w足够小时不可能同时存在：

1. 原有限time probability ν于[-1,1]，长r≥w的interval cap≤w^(-η)r；fine positions不必w-separated。
2. 同一原time标签的scalar F,G，|F|,|G|≤1；对所有real quadratic p，weighted fit满足

       ν{|F−p|≤w^ε(1+|p₁|+|p₂|)}≤w^ε₂。

3. 非空scalar w-separated A_minus,A_plus于固定bounded box，#A_minus≤w^(-1+κ)、#A_plus≤w^(-η)#A_minus。
4. 同一个0≤g(x,t,s)≤1，在Uniform(A_minus)×ν²下mean≥w^η；其正支撑满足

       dist(x+S(t,s),A_plus)≤Cw，
       S(t,s)=(s−t)[F(t)−F(s)−G(s)(t−s)]。

固定C可进小参数阈值。唯一高级named输入：WZ scalar asymmetric BSG Lemma13.7、uniform refinement Proposition5.1、radial Theorem22.2。Kaufman所需的是本轮独立证明的weighted pushforward-law版本（A稿），不把单纯image-set Frostman免费解释为原重数law。高级named输入的完整证明尚未全独立重跑。

## 2. 第一步确实处理原fine weighted ν

调用R0025_weighted_time_reduction.md及B独立proof，得到同F/G细代表、rounded w-separated B、uniform time prior μ，及g_B：

    #B≈w^(-1+O(η))，μ(I)≤w^(-O(η))|I|，
    mean g_B≥w^O(η)，原S关系误差仍O(w)，
    μ{|F_B−p|≤w^(2ε)(1+|p₁|+|p₂|)}<w^β，
    β=min(ε₂/4,1/10)>0。

所有旧fine/time原子数已经消失于阈值。μ是经过证明的prepared prior，不声称代表集旧ν质量有lower。以下完全在μ=Uniform(B)上重新生成周期。为简化记号将2ε、β、O(η)重命名为α、b、η₀，F_B/G_B记F/G；选择原ε足够小使α仍在后文radial许可范围。weighted nonfit蕴含uniform precision h=w^α、质量a=w^b的all-real quadratic nonfit。

## 3. 原S层的小基数lower，不偷用radial

设m=mean g_B≥w^η₀，H₀={(t,s):E_xg_B≥m/2}，则μ²(H₀)≥m/2。按S的w-cells及各cell的H₀-pair重数作dyadic层。可选一层S_j，所有占用cell的pair数在[M,2M]，其pullback H_j的edge massp_j≥w^O(η₀)（log损失吸进小幂）。每个H_j pair仍有≥m/2的input-x graph mass。

定义四差Q；直接展开有

    Q=Δs[F(t₁)−F(t₂)]
       +Δt[F(s₁)−F(s₂)−2s₁G(s₁)+2s₂G(s₂)]
       +(t₁²−t₂²)[G(s₁)−G(s₂)]。                 (1)

R23的原权point-ball proof在scalar同样成立：固定s₁,s₂,t₂，|Δs|≥u时Q命中Cw-interval强迫F(t₁)在同一quadratic的Cw/u邻域。取u=Cw/h≥w，得每个Cw-Q interval的μ⁴质量≤a+Cw^(1−α−η₀)。H_j的完整四环质量≥p_j⁴，其Q像在2S_j−2S_j+O(w)，至多C#S_j⁴个working intervals。因此

    #S_j⁴≥p_j⁴/[C(a+w^(1−α−η₀))]，
    #S_j≥w^(-c₀)，c₀>0固定。                   (2)

可先取c₀为min(b,1−α)/16再令η₀小。故#A_minus≤#S_j^C对一个固定C成立，支付asymmetric BSG的cardinality-power前提。

## 4. BSG保平衡pair层，取得真正H

将每个S-cell内原H_j-pairs的g_B平均，得到A_minus×S_j的bounded graph，其density≥m/2，且x+s落A_plus的固定w邻域。Cauchy–Schwarz按output w-cell计数给full additive energy

    E(A_minus,S_j)≥w^O(η₀)#A_minus #S_j²。

这是Lemma13.7以X=S_j、Y=A_minus的正确归一，不先把原S-image改成无权均匀差再丢pair重数。给定任意small τ_B>0，BSG在η₀充分小时给A'⊂A_minus、S'⊂S_j及小loss参数l_H，可使l_H任意小且

    #S'≥w^l_H#S_j，#A'≥w^l_H#A_minus，
    N_w(A'+nS'−mS')≤w^(-C_(n,m)l_H)#A'
                                        对所需固定n,m≤4。 (3)

l_H包含BSG内部精度及依其而定常数乘η₀，不能把它当免费零。平衡层保证原μ²下H={(t,s)∈H_j:S(t,s)在S'的w-neighbourhood}有edge massp≥w^l，其中l是固定倍l_H+η₀，可后取任意小。

H的全部四环C中Q∈2S'−2S'+O(w)。固定任意a'∈A'，(3)以n=m=4即给

    N_w(Q(C)−Q(C))≤w^(-C l)#A_minus
                         ≤w^(-1+κ−C l)。          (4)

只用有限iterates，不需另假加法闭包或把这个sumset放回原Y套tube-KT。

## 5. 合法均匀P：先保每个witness的共同邻居

置N=#B、V(t)=(t,t²,F(t))，U(s)=(F(s)−2sG(s),G(s),s)。令

    L={(t₁,t₂): μ(N_H(t₁)∩N_H(t₂))≥p²/2}。

两次平均中第一次CS给μ²(L)≥p²/2。删|t₁−t₂|<w^(C₀l)，C₀充分大，time cap给的损失远小于p²；每个剩余pair的共同邻居质量仍≥d₀=p²/2。

将这些pairs映成V(t₁)−V(t₂)，选w-separated实际image points，每点保一个原pair witness。前两坐标(t₁−t₂,t₁²−t₂²)在gap≥w^(C₀l)上逆Lipschitz常数≤Cw^(-C₀l)，故任意w-cell的pair重数≤w^(-O(l+η₀))，且ball半径r≥w的原pair数≤w^(-O(l+η₀))r²N²。得到actual separated P₀，

    #P₀≥w^O(l+η₀)N²。

调用named Prop5.1取uniform子集P⊂P₀，fraction≥w^u、uniform constant≤w^-u，其中u>0可任意小、w最后小。**所有保留点仍携带同一个实际pair witness及共同邻居degree lower d₀**，不需要P在旧B² prior中almost-all。

其normalized ball cap≤w^(-u−O(l+η₀))r²。对slab宽r_s=w^(4α)，固定第二time后：若法向最后坐标≥√r_s，命中slab给F的uniform quadratic fit精度≤√r_s≤h，质量≤a；否则(t,t²)的非零quadratic sublevel由time cap给≤Cw^(-η₀)r_s^(1/4)。除以P的保留比例得到

    μ_P(slab_(r_s))≤w^(-u−O(l+η₀))[w^b+w^(α−η₀)]。

先选u≪min(α,b)，再选l、η₀≪u，故P满足radial所需slab cap w^b_r，b_r可取min(α,b)/2。它是分离的真正set及uniform prior，不再以source一句multiset直接套22.2。

## 6. 同P prior中重新生成周期，再做radial

对每个p∈P的pair witness(t₁,t₂)，定义

    h_P(p,s)=1_H(t₁,s)1_H(t₂,s)，
    μ{s:h_P(p,s)=1}≥d₀。

因此h_P在μ_P×μ上edge density≥d₀，重新做两次CS得到

    W={(p,p',s₁,s₂):h_P(p,s_j)=h_P(p',s_j)=1, j=1,2}，
    (μ_P²×μ²)(W)≥d₀⁴≥p⁸/16。                 (5)

这里是d₀⁴，不是只算一个shared right time时的d₀²。对W每个tuple，两个原H四环的Q差为

    (p−p')·(U(s₁)−U(s₂))，

故其像仍受(4)控制。新周期law由当前witness图CS生成，未声称均匀化P后原B⁴-law不变。

选radial thin指数ζ_r≪κ，要求4α≤ζ_r/100。先固定radial η₀^rad(4α,b_r,ζ_r)，再取u≪η₀^rad、κ；令radial输入η_r=4u，l、η₀≪u。前节ball/uniform/slab条件满足named22.2（固定bounded-box homothety及常数以strict幂余量吸收）。取得D⊂P²，bad质量≤w^(η_r/10)，且D每pair有全尺度2-dimensional thin-tube upper w^-ζ_r r²。

另删|p−p'|<w^q，q=10u；P的ball cap给损失≤w^(2q−2u)，小于(5)。l再足够小使这些bad质量均远小于p⁸，而非用uniform化所失质量去声称原B⁴ almost-all。

## 7. Weighted Kaufman：保target重数及归一宽度

由U的最后坐标为s，target lawμ_U=U_*μ满足ball cap≤Cw^-η₀ r于r≥w，即使G粗糙也成立。

对每个pin p，按v=p−p'的最大绝对坐标及其sign分至多6个charts。删每个质量<w^u的light chart，对所有pins的绝对总loss≤6w^u。其余chart归一成probability后，radial方向在bounded slope λ∈R²上的2-Frostman cap≤Cw^(-ζ_r−u)r²：一个非空slope ball取其中actual good p'_0，其bounded cone落入T_(p,p'_0)(Cr)，用radial thin upper再除chart质量。这里不要求U最后time坐标恰好是normalizing坐标；对U作相应固定坐标置换，ball cap不变。

A稿本轮weighted Kaufman引理给：取β_K=κ/10，要求ζ_r+u+η₀<β_K/8，则每个heavy chart归一law的bad参数及每个good参数下的bad target质量均≤w^(β_K/8)。平均回当前μ_P² prior仍为这个量级；选χ小于min(η_r/10,u,β_K/8,2q−2u)的一半，l≪χ，吸收固定常数后可统一用w^χ计费。剩余v在同一右time μ下的good target投影law有全尺度interval cap≤C w^-β_K r。该引理由parameter slab cover、target pair collision积分、两次Markov及dyadic scales证明；不要求U-image的uniformcardinality，不把投影setcap误当原重数law。

对|v|≥w^q的chart有|v_i|≥c w^q，真正v·U命中一个w-interval时，π_λU落宽≤Cw/|v_i|的interval。因此右time对的命中质量≤

    C w^(1−β_K−q)。                              (6)

不是未经归一就用宽w。radial/lightchart/Kaufman/target删选总loss在同μ_P²×μ²上，小于(5)的一半；W的剩余质量≥c p⁸。

## 8. 用scalar A的亏损收矛盾

(4)只用≤w^(-1+κ−C l)个w-intervals盖住全部W像。平均固定一个good(p,p')并选其中一个interval，可得右time对质量≥

    c p⁸ w^(1−κ+C l)≥w^(1−κ+C' l)。

但(6)给upper Cw^(1−β_K−q)。比较得到κ≤β_K+q+C'l+o(1)。先β_K=κ/10、u及q=10u≪κ，再l、η₀小，矛盾。

参数顺序明确：κ固定→β_K、ζ_r→α足够小、b固定→radial threshold→u与norm/chart预算→BSG内部精度使l≪u、χ→原η₀/抽样η小→w小。named BSG常数可依前项，不能反向取η。固定box homothety可预留α、b、κ的固定倍余量，不改变该顺序。

故finite separated engine在named输入下闭合，结合第2节已证明的weighted reduction，得到第1节原fine-weighted finite定理。实际mixed43的matrix AFF及large-τ仍非本定理结论，源中全高级输入也未独立全文重证；不主张新维数界或重大性。
