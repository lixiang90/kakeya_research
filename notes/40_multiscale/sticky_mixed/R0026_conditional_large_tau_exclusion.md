# R0026：带明确AFF₃准备的actual mixed43大τ排除

2026-10-17，root。依R0026_global_vector_tau_gate.md的真实全局质量门槛；不以单窗口fit改进τ，不重定义投影τ。结论仍条件于未证明存在的whole-matrix AFF₃准备、原row nonquad alternative及具名原几何输入。

## 1. 原配置与诚实workingmesh

原d5/k4/ell3、u/v/a row2、bscalar、v=a+bu、scalar tildeY ADα_Y=1−κ，0<κ≤1；Φ在R²上的原slabγ及原T、ξ、两套grain全部保留。取R26 global gate后的整time配置S^sharp，重新运行原good-q与R24的used-angle incidence/heavycell构图。ν=Uniform(Z(q))，fine base d=δ/ρ，intervalcap K_t r（r≥d），原H的μ=Uniform(H)，π=(差)_*(μ²)在q≥Cρ满足slabcap K_ψ q^γ。

同一个选角前global T_j取固定倍/允许格点τ，K⁻¹T_j≤τ≤KT_j；22.1只需upper(179)，不要求局部τ达到。若取整factor进入K，large下端为τ≥K⁻¹ρ^(3−ζ₁)，以下全部有严格loss余量。固定每J anchor c_J，F_row=(ρ/τ)[h_cJ(z)−h_cJ(c_J)]、G_row=(ρ²/τ)[b(z)−b(c_J)]r_J。|F_row|≤K，|G_row|≤K³ρ³/τ。由globalgate的(10)，同q的所有vector affine fit在precision K⁻¹ρ^A处质量≤Kρ^b，b=b_j。

原bounded g在fine scalar patch×ν²×μ²上mean≥K⁻C，支持

    x+(s−t)[F_row(t)−F_row(s)−G_row(s)(t−s)]·ψ
                      ∈N_(Ce₀) A_out,fine，
    e₀=K[ρ+ρ^(3+ε₀)/τ]， ψ=φ₁−φ₂。

现在删G仅得额外K³ρ³/τ，故取

    e_L=K^C[ρ+ρ³/τ]。                              (1)

原更细mesh和ε₀-controlled上界不再使用。选一次固定L∈[1,K^C]，同时将A_input/out、F_row·ψ除L至unitbounded，设w=e_L/L。损失后小可保

    ρ²≤w≤ρ^(ζ₁/2)， d≪w。                         (2)

fine scalar空间base为r₀=δ/(τL)≤w；δ≤ρ⁴及τ≥K⁻¹ρ^(3−ζ₁)足以支付原δ-error。代理角的细差误差Oρ仍在Kτρ内，未声称fixed exact fine角slice有density。

## 2. 同原slab先验的三点affine gate

记录所用有限式，避免假vector nonfit给每个scalar projection。若原ν下所有vector affine fits在precision h处质量≤a，ν原atoms≤K_t d，则对存在scalar affine p且fit质量≥b_s的角集合Bad(σ,b_s)，有

    π(Bad)≤C b_s⁻³[a+min(1,K_ψ max(q_base,3σ/h)^γ)]。   (3)

b_s≥C K_t d。证明与R24四点式同一原prior，但用三个distincttimes消灭affine。取α_i=1/∏_(k≠i)(t_i−t_k)，按max|α_i|归一，每ratio≤1；三个richfit时刻给|ψ·R|≤3σ。固定另两个time时R是F(t_i)减其vector affine interpolant，小|R|≤h的原ν³质量≤3a；大残差由原π slabcap。rich distincttriples质量≥b_s³/2，Fubini即得(3)。没有timegap倒数或p系数限制。

取h=K⁻Cρ^A、σ=ρ^(2A)，b_s=ρ^v，0<v<min(b,γA)/100，最后令所有Kloss≪min(b−3v,γA−3v)。q_base=Cρ，且3σ/h≤K^Cρ^A；用合法查询Q=Cρ^(A−smallloss)≥max(Cρ,3σ/h)，Q≤1。于是(3)的两个指数 b−3v−smallloss、γA−3v−smallloss均正，且远大于原graphloss，bad概率<mean(g)/4。

因g≤1，存在同一good proxy角对ψ，conditional fine graph density≥K⁻C，且F_ψ=F_row·ψ对所有scalar affine p有

    ν{|F_ψ−p|≤σ}<ρ^v。                             (4)

这是unweighted affine nonfit，足供13.5；不需要声称coefficient-weighted affine/quadratic版本。原g与角任意相关，坏角损失只由原reference概率和g≤1计，不给其g边际虚构slab。

## 3. 空间粗化与同F细time抽样

空间部分逐项用R25 actual middleτ第3–4节的**已证计数操作**，将τ换成此τ、mesh换成(1)：原full Y的两侧AD packing给#occupied w-cells≤K w^(-α_Y)，每cellfine容量≤K(w/r₀)^α_Y，inputpatchfine总质量≥K⁻C r₀^(-α_Y)。删light occupancy后g≤1支付loss，重数两侧K可比，得到uniform A_minus、A_plus及

    K⁻C w^(-1+κ)≤#A_minus≤K w^(-1+κ)，
    #A_plus/#A_minus≤K^C， mean(g_c)≥K⁻C。          (5)

未给任意裁切patch赋AD lower；coverupper使用full原Y的disjointball lower+扩大patchupper。同A/F同步除L保关系误差O(w)。

需要在相同随机代表上保g_c与**所有unweighted affine fits**；R25 weightedquad sampler不能只改结论名字。这里给其简化独立证明。记m=mean g_c，ν的w-cell质量p_i。删p_i<c m w的轻cells，损≤m/100，剩N∈[c/(K_t w),C/w]。每cell选一个原time/同F值，独立依conditional ν；prepared mixture νhat=(1/N)Σν|cell相对原ν density在[c/K_t, C K_t/m]内。两time graphmean在prepared prior≥cm/K_t²，sampled diagonal设0只损1/N；bounded随机mean以概率≥cm/K_t²达到其固定比例。

由(4)及L归一，νhat对precision σ/L的任意affine fit质量≤C K_t ρ^v/m。设q=w^(v/10)，desired coarse precision h_c=w^e，其中e是named13.5先固定的指数。若uniform sampled clock（每cell中心）有q比例h_c-fit，Uniform(B)的intervalcap C K_t r使该fit上存在两个gap≥c q/K_t的clockpoints。|F/L|≤1、h_c≤1遂给slope/intercept≤C K_t/q。原time离clock≤Cw，因此同标签原time fit误差≤h_c+C K_t w/q≤2h_c。

先取e<1/4、v<1/10、timecaploss后小，使1−v/10−timecaploss>e，故上面的K_t w/q≪h_c确实成立。在系数box |r|,|u|≤C K_t/q上取mesh h_c/20，netcard≤C[K_t/(q h_c)]²。每可能coarse fit都被某netpoint在原time以3h_c捕获。令

    4L h_c≤σ。                                    (6)

对每netpoint，prepared expected fine-fit频率≤C K_t ρ^v/m≪q/4；独立Bernoulli Hoeffding给其频率≥q的概率≤exp(−cNq²)，再乘上述netcard仍超多项式小。Nq²≥w^(−1+v/5+smallloss)；v≪1。小于graphgood概率cm/K_t²，所以有同一次代表选择兼保graph和全部affine q-nonfit。注意netcoefbound依sampled richfit但其box已统一确定；没有按#fine times求和。

clockrounding保持同一原F值，S=(s−t)(F(t)−F(s))只改O(w)，因为unitnorm；若在归一前做会有O(Lw)，这里同步归一后执行。可把clockframe再用固定常数缩放/稍加mesh，使B⊂[-1,1]且真正w-separated，常数吸收。(5)的A关系和bounded g支持只多O(w)。这不是旧ν restriction，后续13.5是独立finite配置，不要求代表携带旧atomicmass。

## 4. named13.5的两个阈值与矛盾

设α=1−κ_engine，κ_engine=min(κ/2,1/2)，β_time=1，C={1}、γ_C=0。先依α固定13.5允许的小e；其regularity阈值η_reg=η₀(α,1,0,e) **不依nonfit mass指数**，graph阈值η_graph=barη₀(α,1,0,e,v/10)另取，不能混用。

按globalgate参数A=ζ₁e/100，(2)给Lw^e≤K^Cρ^(ζ₁e/2)≪ρ^(2A)=σ，故(6)。空间/times cap K固定幂及mean g在两阈值之后取小，使Uniform(B)为(w,1,w^(−η_reg))集、#A_plus/#A_minus≤w^(−η_graph)且graphdensity≥w^η_graph。由g threshold可改成真正set G，只损小幂；outputerrorO(w)用有限邻cellcover。抽样给所有scalar affine h_c-fit至多w^(v/10)比例，完整满足13.5(78)。该定理推出#A_minus≥w^(-α)，与(5)及α>1−κ的固定κ/2余量矛盾。

原drop-G translation是(s−t)(F(t)−F(s))，而13.5(79)采用(t−s)(F(t)−F(s))。实际调用取F̃=−F；norm与所有affine nonfit保持，C仍是合法{1}，不暗用不在[1,2]中的−1。

η_j可依已知b_j和v再取小，见globalgate的backward hierarchy；原AFF和source loss最后小，不预设不存在的低损AFF。诚实w由ζ₁控制，e先定而ε₁≪ζ₁e后定，没有沿用源文ε₀-controlled mesh。ζ₁同时小于R25 e_quad阈值所需ε₀固定倍，使同一组参数能接middle分支。

因此在明确原几何与AFF₃/nonquad准备、具名13.5输入下，large-T_j alternative被排除。连同R25 middle与本轮tiny端线性fit论证，给一个**带准备的mixed43非二次分支**排除；不证明准备存在、非二次alternative必得或完整五维。

高级13.5全文未在本轮独立重证；source计数/时层闭包的已审范围见R24/R22。无新维数界、真实Kakeya反例、重大性/新颖性认证。原Goal active。
