# R0026：原vector τ的跨窗口质量二择

2026-10-17，root。main N5-MIXED43-NQ01。本稿补的是R25明确缺少的global gate；单窗口近常不能直接改进global τ。高级几何及whole-matrix AFF₃仍按下列范围条件化。

## 1. 固定原对象与可检验有限命题

取0<δ≪1、δ^(1/4)≤ρ≤δ^µ，0<µ≤1/4。Z是经过明确whole-matrix AFF准备的原有限time集合；删整time层而不删所留层的空间/角/管数据。固定同一半开dyadic ρ-partition J，不使用滑动balls。对每z定义row u(z),v(z)∈R²和scalar b(z)。记

    E(z,s)=v(z)−v(s)−b(s)[u(z)−u(s)]。

在同一J内有 |u(z)−u(s)|≤Kρ、|b(z)−b(s)|≤Kρ。对每actual anchor c∈Z∩J，h_c=v−b(c)u满足原coefficient-weighted nonquad：所有row coefficients A_i∈R²的fit

    |h_c(z)−A₀−A₁(z−c)−A₂(z−c)²|
       ≤ρ^ε₁[ρ²+ρ|A₁|+ρ²|A₂|]                    (1)

至多有ρ^ε₂|Z∩J|个z。若原(1)是更早母集的statement，须先把已付retention factor显式并入K/ε₂余量；本文以此Z为分母，不自动重置nonfit。

对S⊂Z定义

    T(S)=max(δ, ρ max_J max_{z,s∈S∩J}|E(z,s)|)，

空/单点窗口内max=0。令T_j为所有 |S|≥δ^η_j|Z| 的S上的最小值，S_j为实际minimizer。有限集合保证minimum存在。η_j递增，T_j递减；候选只能删原time。固定j使

    T_(j+1)≥ρ^(2/M)T_j， T_j>ρ^(3−ζ₁)。            (2)

δ-floor在本large范围无害，但在候选并中仍保留。归一化所有mass均相对同一Uniform(Z)，而非每窗口重置为全局质量。

## 2. 丰富affine fit迫vector近常

取ξ=ρ^A，0<ε₁<A/10，0<A<ζ₁/10。先删locally-light窗口

    |S_j∩J|<λ |Z∩J|， λ=δ^(2η_j)。

这些窗口携带的当前time总数≤λ|Z|。对其它J选任一actual anchor c_J∈S_j∩J，令t=(z−c_J)/ρ及

    F_J(t)=(ρ/T_j)[h_cJ(z)−h_cJ(c_J)]
          =(ρ/T_j)E(z,c_J)， |F_J|≤1。              (3)

t在固定长度的有界区间内。若有row R,C的fitfiber W_J⊂S_j∩J满足

    |W_J|≥β|S_j∩J|， |F_J(t)−Rt−C|≤ξ，
    β λ>ρ^ε₂，                                    (4)

则物理线性coefficients为A₁=T_j R/ρ²，A₀取相应平移，A₂=0，raw error为(T_j/ρ)ξ。若该error≤(1)的允许误差，则|W_J|>ρ^ε₂|Z∩J|矛盾。因而

    (T_j/ρ)ξ>ρ^ε₁[ρ²+(T_j/ρ)|R|]，
    |R|<ξρ^(−ε₁)。                                (5)

所以W_J上diam(F_J)≤Cξρ^(−ε₁)。对z,s∈W_J，原恒等式

    E(z,s)=h_cJ(z)−h_cJ(s)−[b(s)−b(c_J)][u(z)−u(s)]

给

    ρ|E(z,s)|≤C T_j ξρ^(−ε₁)+K²ρ³
              ≤T_j[Cρ^(A−ε₁)+K²ρ^ζ₁]。           (6)

取所有原small losses使K²≤ρ^(−A/10)，δ小，(6)≤ρ^(A/2)T_j；δ≤ρ⁴且T_j>ρ^(3−ζ₁)也给δ≤ρ^(A/2)T_j。因此任意多个这样的fiber的并W满足

    T(W)≤ρ^(A/2)T_j。                              (7)

关键是T只查同一固定J内pairs，各J可有不同R,C、anchor；并集没有跨窗pair费用。可将bad J定义为对**任一**actual anchor有(4)的窗口，每J选一见证，(6)仍成立。这里只需固定c_J的较弱版本，足供后面所有q共用同一F_J。

## 3. 全局质量二择：不把一个q的fiber冒充候选

称非light窗口bad，若存在(4)；给每bad J选一fitfiber W_J。若

    Σ_bad |W_J|≥δ^η_(j+1)|Z|，

W=∪W_J就是下一minimum的合法candidate。由(7)、(2)及A/2>2/M矛盾。因此

    Σ_bad |W_J|<δ^η_(j+1)|Z|，
    Σ_bad |S_j∩J|<δ^η_(j+1)β⁻¹|Z|。              (8)

若λ+δ^η_(j+1)/β≤δ^η_j/2，删light和bad windows后原time集S^sharp满足

    |S^sharp|≥δ^η_j|Z|/2，                         (9)

且每个剩余J、每个row affine Rt+C都有

    #{z∈S_j∩J: |F_J(t)−Rt−C|≤ρ^A}
                   <β |S_j∩J|。                  (10)

由于删的是完整窗口，在保留J中S^sharp∩J=S_j∩J。原good-q只提供Z(q)⊂S^sharp∩J及 |Z(q)|≥K⁻¹|S_j∩J|时，(10)在其Uniform(Z(q))下的bound为Kβ；不可仍写β。

这证明真实global gate。它不声称旧g在删窗后有质量；任意旧g可全部集中bad windows。下一节调用原time配置闭包后**重新构造**good-q、L与g。

## 4. 低端、有限稳定化和非循环参数

为避免把(2)本身当新结构假设，也记录其取得。在全部time上T(Z)≤Kρ²。whole-u AFF在各J给u(z)−u(c)=r_J(z−c)+O(Kρ^(1+ε₀))、|r_J|≤K。若某T_j≤ρ^(3+2ε₁)，global density保证至少一J有 |S_j∩J|≥δ^η_j|Z∩J|。取c,s∈S_j∩J，E(z,s)小而b(s)−b(c)=O(Kρ)，得到h_c在整个S_j∩J上一个row affine fit，error

    O(ρ^(2+2ε₁)+K²ρ^(2+ε₀))≪ρ^(2+ε₁)。

η_j≪µε₂、loss≪ε₁、2ε₁<ε₀时其质量超过原(1)，矛盾。因此所有T_j>ρ^(3+2ε₁)。对j=0,...,M，若每相邻比值小于ρ^(2/M)，则T_M<ρ²T_0≤Kρ⁴，与低端矛盾。因此存在(2)的稳定比值；该j的τ可能在middle或large范围，分别进入R25或本文large接口。2/M留足端点余量，不直接照用源文1/M。

明确可行顺序如下。先依κ_engine固定named13.5的affine precision exponent 0<e<1/4，同时记录R25 scalar-curvature engine的已固定precision阈值e_quad>0。再固定0<ζ₁≪min(ε₀ e_quad,1)，令A=ζ₁e/100，ε₁≪A并使R25的2(2ε₁+ζ₁)≪(ε₀−2ε₁)e_quad、6ε₁+2ζ₁<ε₀，取M>16/A；ε₂>0按原nonquad分支固定且足够小。如此同一稳定链的middle/large两范围均有兼容参数。取terminal η_M≪µε₂，并从后向前定义η_j；令

    β_j=ρ^b_j， b_j=η_(j+1)/100。

要求η_j≪µ b_j及η_j≪η_(j+1)，并使本j后续三点gate/13.5的全部loss阈值成立。这些阈值只依已固定b_j、A、κ、γ、µ等，故可严格取正η_j，没有循环。原source及AFF实际损失最后取到小于最小η₀及各阈值。

因ρ=δ^s，µ≤s≤1/4，β_jλ=ρ^(b_j+2η_j/s)>ρ^ε₂只需 b_j+2η_j/µ<ε₂；且δ^η_(j+1)/β_j≤δ^(η_(j+1)−b_j/4)≪δ^η_j。故(4)、(8)、(9)同时成立。NQ固定ε₂与finite13.5使用的质量指数不是同一个参数。

## 5. 原geometry责任与认证范围

R22_time_restriction_closure第1–3节适用于(9)：保留整time层，原T、每层Y/X/Φ、tildeY tube-KT和grain witnesses不改；union AD以单层lower和原unionupper保持，allowed-scale取整付Cη_j。全局几何参数仍为small loss，不给任意管子子族新AD。原R16/R24 good-q平均及L计数在这一合法配置重新运行。

为取得good-q的绝对time lower，还可先删 |S^sharp∩J|<δ^(Bη_j)ρ/δ 的窗口，B固定充分大。原 |Z|≥δ^(η_src−1)、η_src≤η_j，而J数≤C/ρ，所以此次总损≤Cδ^(Bη_j−1)，相对(9)至多Cδ^((B−1)η_j−η_src)=o(1)。仍只删整窗，(10)原样保持，保留globaldensity只多固定倍。余窗在good-q平均后满足 |Z(q)|≥K⁻¹|S^sharp∩J| 及 |Z(q)|≥K⁻¹ρ/δ，K含真实δ^(−Cη_j)费。这不是从相对dense任意小window直接声称绝对lower。

WZ22.1的(179)和证明只用E≤cτ/ρ，不用该q内sup达到τ/ρ。故取原τ为T_j的足够大固定倍（及允许格点向上取整，损K），即使选中窗口actual sup很小，仍能构图；不需要τ_q≈T_j。选ψ之前的同一globalvectorτ保留。取整和固定倍只改变上面的K余量。

本文已证明全局质量引理及在whole-matrix AFF/原NQ条件下的真实time准备；不是AFF₃存在或完整mixed43。后续large-τ排除还须原角与标量13.5接口，另稿逐项支付。无新高维维数界、真实Kakeya反例或重大性认证。
