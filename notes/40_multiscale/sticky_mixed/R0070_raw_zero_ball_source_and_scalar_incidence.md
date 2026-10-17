# R0070：原向量零球的质量排除与native标量关联

2026-10-18，root。先写spec5、再明确其中source零球/最终用途后施工。本稿支付全source下的一项raw pair估计，并完成κ+γ>1参数子范围的实际排除；小γ的完整mixed43及ordinary高维目标仍未解。具名高级源输入与有限证明分开，无重大/新颖性声明，已通过两份全文内部独审，未经外部同行评审。

## 1. 完整输入、参数与本轮量词

完整WZ Def17.2–17.4 d5/k4/ell3、原T joint4AD/CW≤δ^-η、两套grain、ξ/Φκ/slabγ、native scalar Y的AD维数α=1−κ及tube-KT全部保留。0<κ≤1、0<γ≤1固定，f=(a;b)、tildef=(c,d)，b=c+da，a,b,c row2、d scalar。

指定原allowedρ∈[δ^(1/4),δ^µ]，µ∈(0,1/4)。先定β>0、B>β、b*>0满足b*<B−β及B<1/2，ζ∈(0,1/10)。R68取任意小a0给同一原整time S≥δ^a0 Z及全部原同窗E upper，T≤ρ^(3−ζ)；R69在该同S给宽Cρ^(1+β)的d簇绝对count<δ^uρ/δ，u>0在source小损失前固定。下文取B=3β、b*=β即可；不取不同ρ的S交。

定义原ordered row核

    E(t,s)=b_t−b_s−d_s(a_t−a_s)，
    D(t,s)=(s−t)E(t,s)，r0=ρ^(3+B)。                 (1)

目标零球估计：存在固定v>0，a0、η后小，删去总原time质量小于O(δ^v)|Z|的坏整ρ窗，并另删第2节的absolute-light窗后保S′≥δ^a0 Z/2，使每保留原窗J的Uniform(S′∩J)²满足P{|D|≤r0}<δ^v。并将它诚实传到随后重构的q/native L，而非把一小q当新global配置。

## 2. 原分母的absolute-heavy窗

置a1=C0(a0+η)，C0为固定足大常数，原损失在v后小使a1≪v≪u。删#(S∩J)<δ^a1ρ/δ的整窗。窗数≤C/ρ，所以所删≤Cδ^a1/δ≤Cδ^(a1−η)|Z|，在a1>a0+η且δ小时小于#S/8。每余窗mJ≥δ^a1ρ/δ，同时mJ≤Cρ/δ；所有heavy-clock费用均为原source损失的固定倍，不另把v灌入final K。

νJ=Uniform(S∩J)有原intervalcap νJ(I)≤Cδ^-a1(|I|/ρ+δ/ρ)，而R69原d-cap变成νJ{|d−z|≤Cρ^(1+β)}≤Cδ^(u−a1)。它只供本尺度bad-set删除，不授d-clock1Fst。所有原层及点/管/角数据未改，平均shading和逐管供应另计。

## 3. 有向零球边的同reference双锚点

若某heavy J有νJ²{|D|≤r0}≥p=δ^v，令g0为该有向边indicator。先删|t−s|<qρ，q=δ^(4v)，原reference损≤Cδ^-a1(q+δ/ρ)=o(p)。δ/ρ≤ρ³≤δ^(3µ)且v≪µ，故floor也已付，余边mass≥p/2。

沿原s作CS，两个边共享t的fan均值≥p²/4。再删|d(s1)−d(s2)|<h=ρ^(1+β)，因g0≤1代价≤Cδ^(u−a1)=o(p²)。这没有使用反向边。Fubini固定实际s1,s2，留下T_J⊂S∩J，#T_J≥c p²mJ，并对每t∈T_J有

    |t−si|≥qρ，|d(s2)−d(s1)|≥h，
    ||E(t,si)||≤r0/(qρ)。                           (2)

原g0参考只含原times，不含native输入labels，故本次近零恢复不会引入随t变化的四输出主项。

## 4. 双法向近零方程直接迫whole f近常

令Hi=b(si)−d(si)a(si)、di=d(si)。由(2)

    b_t−di a_t=Hi+O(r0/(qρ))，i=1,2。

相减解a，再恢复b，均在一个固定矩阵中心F_J附近，误差≤C_M r0/(qρh)。因此

    diam f(T_J)≤Cδ^-4vρ^(1+B−β)≤σ=ρ^(1+b*)。        (3)

最后一步取4v≪µ(B−β−b*)，δ最后小。这里(3)是整个原a,b两row，不是一个scalar projection；非零Hi是常数，误差而非rational主项随t变化。没有假AFF、smooth或rank，也没有将d改成新clock。

## 5. global坏窗见证并与原19.2

称满足第3节的heavy J为bad。反设Σ_bad mJ≥δ^v|Z|。每bad J选上述T_J，W=∪T_J给#W≥cδ^(3v)|Z|。各J的矩阵中心可不同；W只删整time层，T及CW分母不改，R22整time闭包给新参数ηW=C(η+v)（可取原η的整数倍，使newallowed格嵌套）。

取newallowed上邻R∈[ρ,Cδ^-ηWρ]，保dyadic parent嵌套。对每z0∈T_J，仅用其自己的旧T_J作σ-cluster：f-diameter由(3)控制，其count≥cδ^(a1+2v)ρ/δ，而原δ-separated W∩R至多CR/δ。因此在**新配置的原局部分母**中比例≥cδ^(a1+2v+ηW)。不合并不同J的中心，不声整个R窗f振幅小。

ηW≪µ(1−b*)确保R²≤σ≤R，R≥ρ≥δ^(1/4)≥δ^(1/3)，ηW<γ。具名19.2遂给

    CW(T)≥cδ^{C(η+a1+v)/γ}ρ^(-b*κ)。             (4)

allowed σ如需向上取格，δ^-O(ηW)费用并入(4)，先保正b*余量。先v,a1足小依µ b*κγ，再a0,η小，使C(η+a1+v)/γ+η<µ b*κ/2，则(4)违原CW≤δ^-η。高级19.2/19.4/19.5 wholeproof未本轮重新独证。

## 6. 删whole坏窗后重构原q与零球cap

故Σ_bad mJ<δ^v|Z|。a0≪v且δ小，连同absolute-light删除仍保#S′≥#S/2。每保留J未改其S∩J的times，νJ²{|D|≤r0}<δ^v。

随后在S′重做good-q/core/native L，不保旧图。对q times Zq⊂S′∩J，原供应#Zq≥K^-Cρ/δ，故Uniform(Zq)被K^CνJ支配，给

    νq²{|D|≤r0}≤K^Cδ^v。                        (5)

**预算区分**：反设坏窗并时可用ηW含v；最终native图的K=δ^-C(η+a0)/γ来自S′保常比例原质量，不把v回灌K。选择a0、η后小使K^Cδ^v远小于本图m_g≥K^-C。不同q自己的角prior仍分别从其实际used原边际重构，不共用未付条件law。

## 7. 原native图的scalar关联上界

本次q图保0≤g(x,t,s,ω)≤1、Eg=m_g≥K^-C，原νq²×Ω及π=ψ_*Ω有slabγ（查询宽≥Cρ），

    g>0 ⇒ x+D(t,s)ψ∈N_e A_out，
    e=K^Cτρ+Cδ，τ≤K^Cρ^(3−ζ)。                   (6)

A_out位于长Kτ的完整native Y patch，α=1−κ；r≥Ce时，完整Y的AD packing给N_r(A_out)≤K^C max(1,τ/r)^α，不能为裁切patch授AD lower。

先按原reference删||D||≤r0，损g mass≤K^Cδ^v。对余每个固定t,s和每个input x，输出r-balls的每一个平移I−x，在ψ上是一条宽Cr/||D||的slab。若r/||D||≥Cρ且r≪r0，own π给其质量≤K^C(r/r0)^γ。先逐条cover再在x,t,s积分，得到

    m_g≤K^Cδ^v+K^C(τ/r)^α(r/r0)^γ。              (7)

smallD项在cover之前删除，**不乘(τ/r)^α**。g任意相关，使用的是原product reference和g≤1，不对g条件角边际赋独立性。输出与input的native patches可以不同，本upper对每个真实x统一。

## 8. 实际选择分辨率、floor及查询范围

(5)小于1，故存在q原pair使||D||>r0。由|s−t|≤ρ及T=max(δ,ρsupE)，T≥c r0；native τ≈K T给τ≥K^-C r0。取

    r=τ√ρ。                                             (8)

B<1/2、δ≤ρ⁴使δ/r≤K^Cρ^(1/2−B)≪1；e/r≤K^C[√ρ+ρ^(1/2−B)]≪1。全部原source损失在正指数后小即可支付，所以δ≤Ce≪r≪τ，r是比native原e更粗的物理mesh。

另一方面D在同J的upper≤K^Cτ，故slab宽r/||D||≥K^-C√ρ≫Cρ；其upper≤r/r0≤K^Cρ^(1/2−ζ−B)≪1，先取ζ+B<1/2。所有查询在own π的合法base以上，不需fine exact-angle独立slice。

## 9. 完成κ+γ>1的fullsource参数子范围用途

将(8)、τ≤Kρ^(3−ζ)、r0=ρ^(3+B)代(7)：

    m_g≤K^Cδ^v+K^Cρ^{(γ−α)/2−γ(ζ+B)}。          (9)

若γ>α=1−κ，先令Δ=γ−α>0，选β>0、B=3β、b*=β、ζ>0足小，使B<1/2且γ(ζ+B)<Δ/4。第二项指数≥Δ/4。再先定u/v/a1满足第2–6节所有正阈值，最后a0/η足小，使(9)两项均小于m_g/3，矛盾。

所以在列明完整source及具名输入下，mixed43配置不能满足κ+γ>1。这是原参数子范围的实际排除，无wholeAFF前提；不是普通五维维数新界，不声为已认证的新颖结构定理或重大中间结果。完整source原问题允许γ极小，该情形不在本结论内。

## 10. γ≤α时的精确未付责任

当γ≤α，(9)的证书不产生正指数。它仅显示当前原angular slab+output cover方法不足；不是所有策略的必要lower，也不否完整source可能提供更强相关性。不能靠调整β/ζ/r再把γ−α的符号变正，不能把(5)的零球cap当所有offset的χ>α cap。

本轮没有证明γ≤α时的原input平均cap、wholeAFF3或完整mixed43。平均shading按原T分母重计，core逐active tube lower另用实际peeling；单q g的条件质量不冒全原Z。没有把新必要κ+γ≤1当新的长期目标或反Kakeya结果。

## 11. R69校准保全变量s后的独立攻击

R69中央模型a=−2ρ/(4−T²)e1、b=ρ²T/(4−T²)e1、d=ρT/2，physical t=t0+ρT/8。对中央T,S∈[−1/2,1/2]，实际算得

    E/ρ²=(T−S) H(T,S)e1，
    H=(4+2ST+S²)/[(4−T²)(4−S²)]≈1，
    D=−ρ³(T−S)² H(T,S)e1/8。                    (10)

未冻结的零球有平方根集中；但对固定S、|T−S|≥q，∂T[(T−S)²H]同(T−S)号且绝对值≥c|T−S|。再删|ψ·e1|<v0，原slab成本K v0^γ，原fine clock删短gap成本K(q+δ/ρ)。余每interval r′的preimage概率≤K[r′/(ρ³qv0)+δ/ρ]，因为每侧单调且导数lower已付。

## 12. 校准不能补成全变量dense native输出图

若有任意input概率及bounded g，原slab law、fine uniform clock与AD α输出carrier A（长O_Kρ³ patch）满足x+Dψ∈N_e A，则在r′≥Ce、x0=r′/ρ³下，(10)和完整Y packing给

    Eg≤K^C[q+v0^γ+x0^κ/(qv0)+x0^-α δ/ρ]。       (11)

取x0=ρ^(1/2)、q=v0=x0^(κ/4)，因κ>0、γ>0及δ/ρ≤ρ³，右侧是K乘固定正ρ幂。r′=ρ^(7/2)≫e=O_Kρ⁴+Cδ、q,v0≫Cρ均合法。source损失最后小便与K^-C dense原图矛盾。因此R69**中央模型**不能扩成此全变量s的native低维输出图；它的固定两anchor反攻仍正确。这里不是先前固定更多anchors，不把该固定光滑模型另开成proper研究类；一般rough source的相应单调/导数界未获。

## 13. 等价、文献范围与下一停止线

(5)是原向量零球的真实pair估计，强于仅allpairs tiny gate的形式，但只支付旧mixed责任的一部分；不由它反向推出旧全称gain。source full positive-gain若已成立当然可排原类，不据此把任何必要条件换名新注册。γ>α子范围只使用原source+具名输入的完整应用，不称文献首创/重大；53PDF/54sources/78原ID状态不变。

停止本zero-ball指数、κ+γ阈值、B/β/r优化及R69有理模型续轮。下一必须用γ≤α时尚未读取的原实际联合几何或另一真机制，不能继续把区间Fst公设当source结论。ordinary初始化、其余matrix/mixed及general-to-sticky/Hausdorff均仍open，Goal active。

## 14. 当前审查与归档边界

A10/B8及两formal各6节实际全文互审通过，root已全文读回双方及两formal并集成。§2明确a1=C0(a0+η)，heavy-clock费用为source损失固定倍，避免finalK预算字面遗漏；无剩余必修数学项。原19.2/19.4/19.5/good-q/22.1等高级wholeproof未新独证。本文未得完整mixed/ordinary新界或fullsource反例，未经外部同行评审；归档/验证/safe sync按实际执行另记。
