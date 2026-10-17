# R0073：mixed32原零球与fine单管的完整用途

2026-10-18，root。先完成全目标宏观并在spec§2锁原命题后施工。本稿是既有19.2/19.4、R22闭包与R70有限机制在不同完整source中的应用补全，不立新方向/ID，不认证新颖或重大。Goal仍为ordinary n≥5/general，未经外部同行评审。

## 1. 完整命题与依赖

固定0<κ≤1、0<γ≤1且Δ=κ+γ−1>0，µ∈(0,1/4)。存在η0>0，使η<η0、δ后足小时，完整WZ2609.22035v1 Definitions17.2–17.4的d5/k3/ell2配置不存在。保原T joint4AD/CW≤δ^-η、Z/absoluteclock、两套grain、pointξ/Φ及coherence、scalarΦ κAD、native tildeY⊂R² AD(2−κ)/tubeKT(1−γ)。不加AFF/quadratic/NQ、smooth/rational、goodrank或a/d非集中假设。

写f=(a;b)、tildef=(c,d)，a scalar，b,c,d∈R²，原一致性b=c+da。指定原allowedρ∈[δ^(1/4),δ^µ]；下文先得原time零球cap再用fine实际单管，完全不经过coarse L的ρ³误差。高级Lemma19.2/19.4仍为具名输入，wholeproof未本轮重新独证。平均shading和逐active tube供应分别核，原T/CW分母不改。

## 2. 排重、量词和参数

R70 raw代数可转置左右time：a'=d、b'=cᵀ、c'=bᵀ、d'=−aᵀ，得E32'(s,t)=−E43(t,s)ᵀ、b'=c'+d'a'。这是旧有限工具，不是ambient source对偶：whole-f/tildef簇的19.2全局与19.4局部量词不能互换，Y/Φ维数也不同。旧R22 AFF/NQ准备可产生某些零球后果，仍需本稿原图/δ精度和最终用途，不宣新独立gain。

先取小β>0、B=3β<1、b*=β。记

    E(t,s)=b_t−c_s−d_s a_t， D(t,s)=(s−t)E(t,s)，
    r0=ρ^(3+B)， h=ρ^(1+β)， q=δ^(4v)。           (1)

v>0在µ、β、κ、γ及具名引理常数之后充分小，η最后小，a1=C0η（C0固定大）≪v，δ最后小。需要4v≪µ(B−β−b*)、v≪µβκγ、v≪µ、η≪v以及第11节Δ saving；可依次满足。最终K=δ^-Cη只含原source固定幂和a1，不含坏窗反设见证v。

## 3. 原absolute-heavy时间窗

删掉#(Z∩J)<δ^a1ρ/δ的整ρ窗。窗数≤C/ρ，故所删原time数≤Cδ^a1/δ≤Cδ^(a1−η)|Z|，δ后小可小于|Z|/8。未删除的m_J满足

    δ^a1ρ/δ≤m_J≤Cρ/δ。

ν_J=Uniform(Z∩J)保原time及重复标签，无新clock：ν_J(I)≤Cδ^-a1(|I|/ρ+δ/ρ)。定义bad heavy J为ν_J²{|D|≤r0}≥p=δ^v。最终只删整个bad窗，因此每余窗内部的全部原层不改。

## 4. 有向近零边与条件whole-tildef簇

固定bad J，先删|t−s|<qρ的近零edges，损原ν_J²质量≤Cδ^-a1(q+δ/ρ)=o(p)。δ/ρ≤δ^(3/4)，v小、a1≪v保证floor合法。余H(t,s)的质量≥p/2，每edge有

    |E(t,s)|≤e=r0/(qρ)=δ^-4v ρ^(2+B)。           (2)

同一个left t上的two-right fan H(t,s1)H(t,s2)总质量≥p²/4。若其中|d(s1)−d(s2)|≤h的贡献≥p²/8，Fubini给实际t,s1，使至少cp²m_J个s2同时满足H(t,s_i)=1及该d近条件。原(2)给

    c(s2)−c(s1)=−[d(s2)−d(s1)]a_t+O(e)。

因a_t有原固定上界，整tildef=(c,d)在这些s2距实际tildef(s1)≤C(h+e)≤σ_tilde=ρ^(1+β/2)。不是仅d簇，也没有先假原d-cap。

这是原窗J中相对比例≥cp²的簇，19.4只需一个实际anchor的局部条件；σ_tilde∈[ρ²,ρ]、ρ≥δ^(1/4)≥δ^(1/3)。吸固定常数取源ε=3v，可得

    CW(T)≥cδ^[C(η+v)/γ] ρ^(−βκ/2)。              (3)

先v≪µβκγ再η小，与原CW≤δ^-η矛盾。因此这种near-d fan贡献严格小于p²/8，余d-separated fan有质量≥p²/8。没有将原d单变量law改成1-Frostman。

## 5. 分离两个right anchors恢复whole f簇

选实际s1,s2，|d2−d1|>h，共同left邻居S_J⊂Z∩J有#S_J≥cp²m_J，且

    b_t−d_i a_t=c_i+O(e)， i=1,2， t∈S_J。

取其中实际t0比较，相减给非零向量(d2−d1)乘scalar(a_t−a_t0)=O(e)，所以

    |a_t−a_t0|≤Ce/h， |b_t−b_t0|≤C_M e/h。

这是整个原f=(a;b)的簇，不是投影或AFF拟合；无需2×2 det/goodrank。由参数余量

    diam f(S_J)≤Cδ^-4vρ^(1+B−β)≤σ_f=ρ^(1+b*)。

各bad窗可有不同实际中心f(t0,J)，不会在后续并窗时强行合为同一中心。此有限恢复属于旧R70工具的合法向量应用，本稿新需核的是下面全局every-anchor责任。

## 6. 坏窗全局并和19.2的every-anchor量词

反设Σ_bad m_J≥δ^v|Z|。W=∪_bad S_J有#W≥cδ^(3v)|Z|≥δ^(4v)|Z|。只保这些整time层，T及各保留层的Y/X/Φ/ξ不动；R22闭包给参数η_W≤C(η+v)，取η的整数倍使newallowed格嵌旧格。

取newallowed上邻dyadic R，ρ≤R≤Cδ^-η_Wρ，保原dyadic父格嵌套。对每z0∈S_J，仅取自己的旧S_J作f近σ_f见证；count≥cδ^(a1+2v)ρ/δ，原δ-separation给W∩R最多CR/δ个。因此该anchor在**新配置的原局部分母**中的命中比例≥cδ^(a1+2v+η_W)。不要求整个R父窗f近常，不交不同J的中心。

η_W≪µ(1−b*)给R²≤σ_f≤R、R≥δ^(1/3)，η_W<γ；若需取邻格的固定倍损失按R22记δ^-O(η_W)，预留正b*。named19.2对所有retained z0满足其(154)，得到

    CW(T)≥cδ^[C(η+a1+v)/γ] ρ^(−b*κ)。           (4)

v先足小依µb*κγ，再η小，(4)违原CW上界。故Σ_bad m_J<δ^v|Z|。此步才使local f簇成为合法global矛盾；不能用单一好窗直接调用19.2。

## 7. 最终time限制、raw cap及K预算

删除bad与第3节light整窗得Z′≥|Z|/2；每余J内部仍是完整Z∩J，且

    ν_J²{|D|≤r0}<δ^v。                            (5)

Z′的时间保留为原常数比例，最终source参数只需Cη；(6)反设中的η_W含v不回灌最终K。跨time AD union的lower由R22对整层删选保留，原point Φ并未删成新law，T/CW仍原分母。平均shading可从原witness重计；逐active tube下界在下一节单独heavy，不假所有原管仍同密度。

不交不同ρ所造Z′，(5)只在本指定ρ。任何后续条件图若要用(5)须另付原marginal upper；下面直接在global原fine incidences计，不借q代理或native L。

## 8. 原fine同管pair质量及坏pair删除

取任一余heavy J，m=m_J。在该time窗保全空间原E_t，给每p、fine φ∈原Φ_p选一个真实witness T，固定fine angle/point碰撞有界，保原标签。P=#E_J≈_K mδ^(−4+κ)，D0=δ^-κ，原incidences I≈_K P D0≈_K mδ^-4。used T≤Kδ^-4来自原joint4AD及bounded参数盒。

只做tube-heavy：删访问数<I/(4#used T)的T，总incidences损≤I/4。余active n_T≥K^-C m，I_core≥I/2，故同一实际T的ordered root/terminal pairs

    #C=sum_T n_T²≥K^-C I m≥K^-C δ^-4m²。        (6)

一个T/time只有固定数δ-separated E点；对任何fixed(t,s)，所有原root incidences及terminal见证重数至多Kδ^-4。用(5)，D小的实际C贡献≤Kδ^vδ^-4m²，η最后远小于v后少于(6)一半。这不是每p的条件timecap，也没有把两独立dense图求交。删后core若另作限制不自动保逐管原density；本证明只用已支付的总pair lower。

## 9. 真native输出与完整baseline

原p坐标写为

    p=(x,w, ytilde+c_t x+d_t w,t)，
    θ(T)=(φ, ξ1,p+a_t φ, ξ2,p+b_t φ)+Oδ。

ξ1 scalar、ξ2 vec2。同一原T的实际terminal p_s@s满足

    ytilde_s = ytilde+(c_t−c_s)x+(d_t−d_s)w
               +(s−t)(ξ2,p−d_s ξ1,p)+D(t,s)φ+Oδ。 (7)

baseline依p,t,s，但不依φ。不能把它省成一个跨root共同常量；然而fixed(p,t,s)计数时它是已知平移，tubeKT对任意位置的线管统一可用。p_s必须真为原selected visit，不能仅轴线穿点；(6)以同一原incidence edges生成，故这一点已保。

本式用实际fine φ和native Y，Oδ误差只来自原tube/δ点，不产生coarseρ³项；不使用R68的大τ上界或R21–23的AFF/NQ准备。保所有fineφ/管标签，原Φ upper可用于任意删后edge，未授删后Φ AD lower。

## 10. 原scalarΦ κ乘native tubeKT的细计数

对D不小的fixed(p,t,s)，令ℓ=|D|>r0。原dyadicLip及兼容使|E|≤Cρ，故ℓ≤Cρ²<1。normal输出沿一条长Oℓ的line，位于原Ytilde_s的Oδ邻域。tubeKT给至多K(ℓ/δ)^(1−γ)个δ-output cells。

每个cell的φ反像为长O(δ/ℓ)的interval。scalarΦ的原κ-AD upper给至多K D0(δ/ℓ)^κ个fine angles；每fineφ穿p的原管数固定倍，terminal同time重数也固定倍。因δ≤δ/ℓ≤Cδ/r0≪1，全部查询在原base以上，邻cells/加宽δ管只改K。因此

    #selected visits at(p,t,s)
        ≤K^C D0 (δ/ℓ)^(κ+γ−1)
        ≤K^C D0 (δ/r0)^Δ。                         (8)

这里用κ而不是较弱的γ角cap；Φ是一维时该upper是真的。两个终点law从未独立化，二维Y也没有投成低维scalar。

## 11. 完整用途、κ=1及scope

将(8)在p∈E_t和s∈Z_J求和，用P D0 m≤Kδ^-4m²，得到(6)删小D后tuple的upper

    #C_good≤K^C δ^-4m² (δ/r0)^Δ。

ρ≥δ^(1/4)、B<1使

    δ/r0≤δ^[(1−B)/4]。

固定Δ>0先定，最终η足小使K固定幂小于此saving，upper违(6)的K^-C lower。故第1节完整source参数子范围κ+γ>1排除；κ=1时覆盖任意固定γ>0。没有改变κ，也没有把具名输入的条件藏掉。

这是原工具在不同mixed case的实际应用，非新增finite转置定理或新颖性认证；不增ID。它缩小mixed32当前范围，但不解κ+γ≤1、不解一般matrix/mixed42或ordinary初始化，更不自动给ordinary R5>4/Hausdorff。R70 mixed43结果和本mixed32各保自己的source/native角维数，不能交换参数或直接宣ambient对偶。

## 12. 独立反攻和停止边界

反攻重点已逐项支付：近d仅在同left原fan中变whole tildef，19.4用真实local分母；whole f簇只能经global坏窗并和every-anchor新父格调用19.2；最终K不含v；原sameT平方lower与fixedpair upper分别算；nativebaseline的ξ1d_s项保留；细δ误差不用粗L；Φ删后只用upper，平均和逐tube密度分开。

本轮不构造toy反例，不重跑旧有限计算。量词/参数/原图待A/B两正式逐步审及root整合后才归内部已审，仍未经外部同行评审；19.2/19.4 wholeproof具名。完成后停止本zero球/κ+γ阈值优化，不以其再开新独立方向。下一须回完整高维目标及κ=1时剩余matrix/mixed42和ordinary前端的真实责任，不能把本子范围当最终Goal。Goal active。
