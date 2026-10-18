# R0095：实际平面Furstenberg转移与原生轨迹的直化边界

2026-10-19，root。研究前量词/反攻/停止条件见两spec。本稿是原接口资格及停止记录；交独立全文审查后才标内部已审，未经外部同行评审。未获ordinary维数改善、完整mixed42排除或重大结果。

## 1. 原对象、定理与已用工具排重

固定0<κ<1、γ>0，η最后小、δ最后小。保bounded完整WZ2609.22035v1 Def17.2–17.4 d5/k4/ell2全部数据、原T joint4AD、N≈K^±1δ^-4、normalized whole-tube CW≤K、原Z近满δ-clock、两grains/ξ/Φ/coherence；K表示有限原损失δ^-Cη。源的细点坐标为p=(x,y+f(t)x,t)，x∈R、y∈R3；另一套grain用x_H∈R3、β(t)=tildef(t)∈R3和scalar原label。

Ren–Wang2308.08819v3 Def3.1/Th4.1（原PDF8–9）输入一个实际平面point Frostman集合P（维t_P）及逐point的实际dyadic tube-pencil（维s，大小≈M），输出

    #L ≳ε δ^{−min{t_P,(s+t_P)/2,1}+ε} M。

该高级定理wholeproof具名，未本轮新独证。R77已经证明加权坏方向/所有大细子集的robust有限接口；不是本轮新primary或新机制。最新abs/history核仍v3，2025-01-19；原28物理页不同于abs comment23页。原PDF不重复下载。

## 2. 真正合法的共同平面投影

π(x,y,t)=(x,t)把原直管axis送到真实直线x=a_1+t b_1。每个t选一个实际native y_t，再取原filled X_y_t,t；其card≥K^-1δ^-1。投到共同平面得到δ-separated P，#P≥K^-Cδ^-2，因为#Z≥K^-1δ^-1。按固定常数grid/color处理原坐标和dyadic边界，只损K固定幂。任意r≥δ的平面ball至多含C(r/δ)^2个点，故UniformP(B_r)≤K^C r²，确为(δ,2,K^C)-Frostman。

每个投影point只选一个实际preimage p，不合并多个p的条件law。原scalar Φ_p是ADκ，真实方向投影为φ+Oδ。不同φ的固定倍δ分离可用有限着色取得；通过p的原δ管投影用固定倍δ dyadic slope/intercept邻格覆盖，碰撞固定有界。于是每p有≈K^±Cδ^-κ个不同真实projected pencils。取同一整数M≈K^-Cδ^-κ个实际pencils使nice配置的大小一致；任意这种subselection相对原Φ只损K固定幂，故Frostman upper仍K^C r^κ。可先改尺度为可比的dyadicδ′，所有次数和指数不变。

这是完整source提供的合法共同平面接口，不能声称原数据根本不给共同平面。只构造witness图；没有把其preimages重新声明为满足Φ lower的完整删选configuration。单preimage选择不声称保留原全部incidence权或全部(T,p)关联，故本节只认证RW输入存在，不认证可回传新gain。

## 3. 尖锐定理在此已饱和，没有新增益

在§2，t_P=2、s=κ，所以min{2,(κ+2)/2,1}=1。RW仅给

    #L ≳ε δ^-1+ε M。

一个原固定time t0就有≥K^-1δ^-1个横排points，每point M条不同δ slope/intercept tubes；一条这样的平面tube在该time仅碰O(1)个δ-separated横排points。因此初等计数已给

    #L ≥K^-Cδ^-1 M。

这个lower在幂次上至少与上述RW相同。全projected affine-line space在bounded slope/intercept chart容许Cδ^-2条line cells，而δ^-1M≈K^-Cδ^-(1+κ)未超过该ambient预算。原压缩的scalar label Ytilde_t（维1−κ）已在π中丢失；不能把它的cover upper挪给P或L。对任意正密度删选套RW只是已饱和的同一估计，非新正幂source gain。

## 4. 固定法向的真实CW投影上界

写原graph参数λ=(a,b)∈R4×R4，axis x_T(t)=a+tb。固定bounded β、n=(-β,1)，令qβ(λ)=(n·a,n·b)。若qβ在一个r-ball中，则每条对应whole原axis在bounded完整clock内满足

    |n·x−u−tv|≤Cr。

原chart bounded、||n||≥1，故所有这些完整δ管在一个真实bounded长轴、宽Cr的凸slab U内，|U|≤Cr（δ≤r，round caps用固定倍r支付）。原全部T为分母的CW给

    μ{qβ∈B_r}≤CKr，   δ≤r≤1。

这是1-Frostman upper；没有声称必须2-Frostman才能用RW。尤其β恒定时，tube-heavy的nearfull clock fibre配合足1维line law就能走平面出口，属于旧19.4/固定normal闭包，不是本轮缺口。

具体旧用途由A§4/B§7各自重核：对heavy原T的qδ-cells按原质量分O(logN)层，选一层和每格一条实际heavy代表，得到uniform 1-Frostman point law。对偶point为(n·b,−n·a)、原native标签(t,η)对应dual line v=t u−η；每代表原nearfullclock给s=1 pencil，RW的(t_P,s)=(1,1)使dual lines≥K^-Cδ^-2+ε，而全原标签upper≤Kδ^-2+κ，ε<κ且η最后小即矛盾。质量层/逐代表clock必须实付，不能仅因q1就跳到此结论。这是原固定normal源应用，不解一般β。

## 5. joint4AD与wholeCW不自动授q的2-Frostman

取b∈(3δ Z)^4∩[-c,c]^4，c=1/16，所有axis从同一原点出发：

    {(tb,t):0≤t≤L_b}, L_b=(1+|b|²)^-1/2。

axis是真实physical单位线段，其δ邻域为原tube；N≈δ^-4，λ=(0,b)是真joint4AD、angularδ-separated的四参数族。由于L_b>3/4，对任意子族S的所有原whole tubes，任意clock t∈[1/4,1/2]上的horizontal δ/10 disks互不相交，均在所含原tube内。因此任意集合W若包含这些whole tubes，

    |W|≥c #S δ^4。

这甚至不需W凸；除以N≈δ^-4给normalized wholeCW≤C。取β=0，q=(0,b_4)，原q-law在每个内部occupied中心的半径r ball中质量≈r，δ≤r≤c/10，故不满足常数统一的2-Frostman。

此模型的whole union有固定正5维体积。它只是严格反驳joint4AD+CW免费升级q2，不满足完整source的smallfootprint/filled双grain/每pointΦκ等，不是source反例或低维Kakeya反例。它也不阻止§4的1维law已经可用于固定normal平面定理。

## 6. 原生标签轨迹的精确共同线性直化判据

令J有至少三个不同times，n_t=(-β(t),1)，V_t=(n_t,t n_t)∈R8。则

    dim span{V_t:t∈J}≤2 ⇔ β在J恒定。

证明：V_t的两个固定坐标是1和t，故rank至少2。若rank≤2，则所有其余coordinate函数在J上属于span{1,t}，特别每个β_i(t)=A_i+B_i t、tβ_i(t)=C_i+D_i t。相减得二次多项式B_i t²+(A_i−D_i)t−C_i在至少三个不同点为0，故B_i=C_i=0且A_i=D_i，β_i恒定。反向直接由V_t=(n,t n)成立。

更一般，若有共同非零scale c(t)及injective共同clock h(t)，使对**每个ambient λ∈R8**，c(t)V_tλ都是h(t)的affine函数，则向量c(t)V_t属于固定二维row span；逐row非零scale不改rank，仍迫β恒定。恒定时取c=1,h=t给反向。此结论仅限共同linear observable和全ambient λ；没有证明任意nonlinear plane diffeo不可能，更没有排原T子族落在特殊参数carrier后可直化。

这一scope有严格真实管校准：β(t)=t e1，取a在固定四维δ-grid、b=0的平行单位轴(t↦(a,t))。joint4AD和wholeCW由各水平slice的δ-ball bounded overlap积分直接成立；其所有原native轨迹F_t=a4−t a1确是直线，尽管ambient V包含t²项而rank3。该族同样不满足完整source的Φκ/小label等，仅说明不能将ambient判据升级成actual-family不可直化。

## 7. 两端插值的真实fine误差

令t0<t1，h=t1−t0，θ=(t−t0)/h，βlin=(1−θ)β0+θβ1，F_tλ=n_t·(a+tb)。直接展开得

    F_tλ−[(1−θ)F_t0λ+θF_t1λ]
    =−(β(t)−βlin(t))·(a_H+t b_H)
     +θ(1−θ)h(β1−β0)·b_H。

第二项符号为正；即使β本身affine，仍可能非零。取β(t)=t e1、a=0、b=(e1,0)，实际单位axis为(t e1,0,t)，0≤t≤L=1/√2。此时F_t=−t²，两端chord缺陷为t(L−t)，midpoint为L²/4=1/8。β bounded且Lip，但轨迹不是δ直线。此单管只是observable反攻，未满足完整source。

仅用bounded Lip β和bounded λ，window长度ρ内第一项至多Cρ，第二项至多Cρ²；没有C²或特定joint结构就不能把第一项免费写成ρ²。即使在affine校准里，midpoint误差≈ρ²迫ρ≲√δ才能达fineδ；单个此窗的原time比例至多K(ρ+δ)，返回全clock需支付幂损失。若真实管满足特殊(b_H,β)耦合，误差也许较小，必须从原source真证，不能以此例否定全部方案。

## 8. 另一个方向平面接口与删选量词

对每个固定time，投影方向到(φ,θ_j)时，原point p的Φ_p落在一条斜率f_j(t)、intercept ξ_{p,j}的直线上，κ是线上point维度，不是该point处一族不同lines的pencil维度。跨time这些lines当然在同一个方向平面，但需另外付line-parameter law；原全部方向投影的诚实upper仅ambient2，本轮没有从source得到更小upper。不能把‘线上有κ维points’与RW nice逐point pencil假设互换。

只删whole T labels可重用原CW分母upper，但不保归一后原常数；比例p付1/p。平均selected visits先heavy化才有逐active管time lower，后续time限制不自动保逐管密度。Φ和native label删后只继承原upper，ADlower另付；不能把一组有限witness当新Def17配置。R77 weighted/robust工具已处理合法相关图，不需要再把图独立化；它不供应这里尚欠的曲线直化/小global方向upper。

## 9. 与四完整路线和旧失败的关系

§2–3是实际source接口，但输出被ambient/横排计数饱和。§4–7精确划定不同native接口，未从source支付特殊carrier；§6不构成该carrier不可能性定理。R74 AD0通过少label的原质量提取，不自动扩到正维label；R45 fixedarm成本及R19局部CW旧闭包不解冻，R77现成robust投影不新命名。

ordinary all-scale jointAD/smallfootprint初始化、HRZ全部parent/terminal/coarse/narrow费用、sticky完整κ1/余mixed/ordinary桥仍open；本轮真bush是正体积，不是同集严格低维full方向构造。DIM001/R38/R80旧条件读出、CP⇔PM等正幂等价和旧spectral/digital/arithmetic/normal冻结均保持。若未来有实际新联合结构可重新评估，但不是再添C²、goodrank、共同plane或desiredgain公设。

## 10. 结论、独审和停止

本轮可审的成果是实际平面转移的全部hypotheses、饱和预算、原CW q1上界及sharp弱输入反攻、精确rank直化判据和fine interpolation defect。它们是原接口检查及初等工具，不登记新数学ID/重大结果/优先权。高级RW/WZ wholeproof仍具名，不将内部独审冒外部同行评审。

停止此次直接sharp planar接法，不续β/κ/window/CW指数微调或R74正维阈值。完整mixed42未证未否，未给ordinary新Hausdorff界。两独立全文review通过后本稿仅记限定接口内部已审；root统一更新状态、literature范围、验证与同commit/fulltree同步。Goal active。

当前两actual全文formal及root实际整合已通过，见research/reviews/R0095_original_source_and_Furstenberg_transfer_review.md、research/reviews/R0095_CW_straightening_and_scope_review.md与research/reviews/R0095_root_integration_review.md。此状态只覆盖上述有限接口，未经外部同行评审，不改变完整Goal未达。
