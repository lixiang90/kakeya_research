# R0057：任意椭圆分包与原保留质量的联合费用反攻

2026-10-17，B。实际读AGENTS／GOAL／STATE／ROADMAP／registry78全状态、R56next及R57先写的macro／working_spec6后施工。唯一主任务是新Th2.2的带费用singleblock→joint组合，不重记旧free-cap交换例。以下证明对全部指定partition和全部dominated time-dependent保留同时成立；只否定所写slab-sup envelope，不反H5、Th2.2或全部joint策略。未经外部同行评审。

## 1. 原law、可测分包与待测架构

取固定小square Q⊂R2，A、B独立uniform于Q，T独立uniform于固定dyadic区间I⊂[0,1/4)。记μ=ρ(dA,dB)dt/|I|，U=(A,B)、V=(B,A)，X1=B+tA、X2=A+tB。原4维slope law是满维；本稿还会说明真正unit axes与finite网，不把只看一个t当wholeclock。

设Γ_j为base (A,B)空间的任意有限或可数可测partition，允许其中非零项含于

    A∈a_j+E_j， B∈b_j+E_j，
    E_j=R_j diag(L_j,w_j) B2， δ≤w_j≤L_j≤C0。              (1)

中心、方向、尺度全可自适应；Γ_j不必等于box、更不要求其conditional law为乘积。令p0_j=ρ(Γ_j)，任意ν≤μ的总质量为m，p_j=ν(Γ_j×I)。只讨论p_j>0的项，此时p0_j>0。K_j为固定原block坐标下实际调用的normalized第一block (U1,V1)=(A,B) prior的jointellipse常数；可以在原Γ_j law上定义，也可以是其最终保留law重新归一后的常数。两者都支持于(1)，故下面的必要下界均成立。若每包另作anisotropic空间归一化，原δ-cell与测试类的回传费用必须另证，不无费纳入本架构。

定义A_j为ν_j的essential time support，或包含它的原δ-bin并。聚合只使用第二block slab

    S_j={(t,x):t∈A_j， x∈a_j+t b_j+C1 E_j}，
    C(t,x)=Σ_j p_j K_j 1_(S_j)(t,x)。                       (2)

C1为固定正数，实际containment需取足够大。若原source上界前系数为p0_j或更早质量而非p_j，本稿故意使用更小的p_j，给这套架构最有利预算。待证结果是sup C≥cδ^κm²，而不是“实际joint cell的质量有这个下界”。

## 2. 条件容量的必要下界，不使用uniform conditional

令Wκ(E)=L^(1+κ)w^(1−κ)，固定0<κ<1/10。在任一normalized第一block prior下，测试U1∈a_j+E_j、V1∈b_j+E_j捕获全质量，故

    K_j≥c/Wκ(E_j)。                                      (3)

这个证明只使用support，没有将Γ_j假作乘积或将ν独立化。Th2.2初始测试floor为δ^D、D≥1，(1)的w_j≥δ保证该形状在允许初始精度内。若原测试规定L≤1而L_j≤C0，则把每个长ellipse分成O_(C0)(1)个允许测试，再对两因子用有限覆盖；至少一对捕获固定质量，测试capacity≤C Wκ(E_j)，所以(3)仍成立。若某K_j=∞，后面的费用下界更直接。

必须区别：这是实际normalized prior的K，不能在已经条件Γ_j后继续使用原unconditional K。ν的time-dependent保留只改变该prior，不改变它仍支持(1)的事实。

## 3. 原time domination给保留支持的费用

写dν=h dμ，0≤h≤1。令f_j(t)=∫_(Γ_j)h(A,B,t)dρ，则0≤f_j(t)≤p0_j，且p_j=|I|⁻¹∫_I f_j(t)dt。取A_j={f_j>0}，Fubini给可测代表及

    |A_j|≥|I| p_j/p0_j。                                 (4)

任意更大的time support也满足(4)，故无需假它是interval、具有Frostman profile或与base独立。countable partition和ν任意correlation均未改变分母p0_j。

若source用δ-bin左端点v，则定义A_j^δ为有正ν_j质量的原time bins并，(4)仍成立。相应slab在每bin中取中心a_j+v b_j，作固定Cδ增厚。w_j≥δ与b_j有界使它包含实际a_j+t b_j+C E_j。该step-function版的积分与sup在grid左端点上同样有效；不能以连续sup替代source根本未测试的time点。更薄terminal ellipse的rounding不能自动沿用此结论，本稿(1)的secondblock envelope只使用w≥δ。

## 4. 全partition、全retention的总费用下界

所有非空Γ_j均位于固定Q×Q，L_j≤C0使a_j、b_j在固定bounded box；因此全部S_j包含于一个固定体积的(t,x)窗口Ω。每个time截面的面积为常数倍L_jw_j。Tonelli、(3)、(4)给

    ∫_Ω C ≥ c Σ_j p_j K_j |A_j| L_jw_j
           ≥ c Σ_j p_j |A_j| (w_j/L_j)^κ
           ≥ cδ^κ Σ_j p_j²/p0_j
           ≥ cδ^κ (Σ_jp_j)²/(Σ_jp0_j)
           ≥ cδ^κ m²。                                   (5)

最后一步是原权Cauchy，Σp0_j=1；未把最终p_j重新当作原均匀质量。若和无穷，Tonelli或有限partial sums再取极限即可。于是

    sup_(t,x) C(t,x)≥cδ^κm²。                             (6)

可将hard partition换成原base上的fractional partition of unity，证明不变；若是R重cover，仅得到右侧除R，不能让原质量重复而不收费。这里实际证明了任意多包、自适应orientation／anisotropy及任意ν均不能把该uniform envelope做成固定正幂小于(6)，而非仅证明一个指定packet失败。

## 5. 所保证singleblock指数不能完成这个joint envelope

Th2.2所保证的是任意严格q_j<1+2s_j−10κ，s_j≤1；它不是声称q*≤该值。实际source汇总的upper RHS形如R=Σ_j θ_j δ^(q_j)K_j 1_(S_j)，其中调用前的原权θ_j≥p_j。下式B只是R的lower envelope，**不能把它反写成真实atom≤B**。若只使用具名保证，给所有包最乐观端点q=3−10κ并忽略其余subpower损失，则

    B(t,x)=Σ_j p_j δ^(q_j) K_j 1_(S_j)(t,x)，
    sup B≥δ^(3−10κ) sup C≥cδ^(3−9κ)m²。                  (7)

原bound若用更早质量、再加source rounding或小time-profile损失，upper envelope只会变大。对ν/m归一，sup(B/m)≥cδ^(3−9κ)m；m≥δ^η时指数最多3−9κ+η，不能成为H5所需δ^(4+σ−ε)的uniform cell cap。即使额外慷慨把每包的数值rate改为3，该同一汇总式仍有下界cδ^(3+κ)m²，在κ<1/10、η小的H5范围也不足；这只是更乐观数值测试，不声称source实际提供该更强rate。

这是特定证明certificate的失败：所构造upper envelope的sup过大，不是ν在这些点的真实joint质量必大。用full joint support缩小S_j、让输出系数随x1变化、采用非sup的weighted积分、改变坐标split等策略没有在(2)内，本文不排除它们。也没有将两个marginal upper bounds相乘。

## 6. 真unit axes、finite directions与原shading

选Q足小，c(A,B)=|(1,A,B)|在[1,C]，I长度取固定小于1/(4C)。真实unit axis是

    L_(A,B)=(0,B,A)+[-1/2,1/2] (1,A,B)/c(A,B)。

I内graph点(t,B+tA,A+tB)恰在该axis上；不延长unitlength，也不把t=1的focus纳入。只保这一共同clock段已有常数量级arclength、每label≈δ⁻¹原marks。其对应原tube shading取该段附近固定fraction横截即可有平均和逐管λ≥c；未从仅m平均保留推逐管near-full。所有真实round端帽可保原tube定义，所用common clock本身在unitaxis内部，不靠删某个可能唯一含marks的端帽证明lower。

取A、B的Cδ-grid，方向映射(A,B)↦(1,A,B)/|(1,A,B)|在固定chart bi-Lipschitz，选网步常数足够大即physical δ-separated且N≈δ⁻⁴。对这个离散ρ，上面(3)–(6)原样成立：它们只用support、time domination及Σp0=1，不用连续base密度。任意Oδ coefficient jitter或incidence横截blur只把(1)与slabs作固定扩大，w_j≥δ吸收此误差；input D=1、output unitellipse时source左端time误差同样只需固定邻格。

这是一个正方向chart的原law测试，不自称它已覆盖所有S4或排除任意adaptive atlas。有限rotations可补全物理方向，却改变split／交换关系时必须重核，不能由一个chart的certificate失败推全H5算法失败。若原law带任意正weights，(3)–(6)仍按该原probability成立，但“满网且每label权1”的几何验收与任意权全称要分开。

## 7. 下界的anisotropy校准与实际joint质量

m=1时，δ^κ幂可由该架构真实达到（常数不求最优）。取Q=[0,c]^2，δ整除c；按A₂、B₂的δ strips作Γ_(k,l)，不切A₁、B₁。每原mass≈δ²、E的semiaxes≈(1,δ)。在初始D=1的测试范围w≥δ内，任意长轴L的ellipse与一个strip相交面积≤CδL，因此normalized单strip marginal≤CL，两独立strip的joint≤CL²。又δ^(−1+κ)Wκ(Etest)≥L^(1+κ)≥L²（L≤1），所以K_j≤Cδ^(−1+κ)；(3)给反向同阶。

continuous strip law还可核所有更细测试，而非只D=1：两个long coordinates的联合边际密度有界，4D全密度≤Cδ⁻²，所以任意rotated测试F、semiaxes L,w，都有

    Pr(U1∈u+F,V1∈v+F)≤C L² min{1,(w/δ)²}。

第一界由两long projections长O(L)给出，第二界由4D density乘|F|²；不假测试方向沿strip。除以Wκ(F)，w≥δ时≤Cδ^(−1+κ)，w<δ时为C L^(1−κ)w^(1+κ)/δ²≤Cδ^(−1+κ)。因此continuous K的同阶上界对所有fixed D成立。若把共同clock归一到[0,1]，(U1,V1)只作固定scalar可逆mix，该mix不混空间long／normal坐标，两个density界仍成立。变换后第二block slab的normal center为kδ+ℓ(τ−1/2)lδ，所以下面的overlap计数不变。这个all-fine上界不能原样用于未jitter的finite atomic网；后者在w<δ可能有额外atom费，本文只声其floorδ版本同阶。

S_(k,l)在x2的normal coordinate约kδ+t lδ的Cδ带。固定t,x2时，对每l只有O(1)个k能命中，故最多Cδ⁻¹个包；每项p_jK_j≈δ^(1+κ)，得sup C≤Cδ^κ，与(6)同阶。边条或固定c只改常数。这个校准既可连续ρ，也可采用每strip一排的原finite网，未依赖数值搜索。

与之相反，实际map (A,B)↦(X1,X2)=(B+tA,A+tB)在I⊂[0,1/4)的Jacobian绝对值为(1−t²)²，统一远离0。故continuous真实joint(T,X1,X2) density≤C、δ-cells质量≤Cδ⁵。这直接说明(7)的δ³级数值下界属于宽slab certificate，不是actual law cell cap的障碍；本族本就有常量union，不是small-union或Kakeya反例。

## 8. 闭包、实质信息与停止

与R56已知swap校准的区别是：这里以原p0_j为分母，证明了全可测partition／任意time-dependent保留后的sum-envelope总费(5)–(7)，并实际核anisotropic自适应包和finiteunitaxis；不只展示某个conditional K坏。dominated删选、packet后再heavy或两次顺序调用都落在量词内，只要最终仍用(2)的slab-sup聚合。更多joint信息或不同coordinate策略不在此否定内。

单block source整体仍具名高级输入，本文没有证明其全篇或给新高维界。CP/PM全称shading闭包不能因新名称消失，不登记新方向或重大／新颖结果。按spec停止这个直接conditional-capacity slab-envelope组合，不续κ／s／partition阈值；不能附“conditional capacity好”公设后称H5完成。实际读回最终root10／A10／macro6／next6／spec6后的正式审查见research/reviews/R0057_joint_budget_review.md，自审本文不计独审。Goal active。
