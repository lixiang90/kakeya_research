# R0041：真实构造的体积门槛及坐标耦合熵

2026-10-17，root。主任务为将FD–deLaSalle2607.14824v3真实构造从log衰减改为fixed power，**未实现**。以下给出实际集合的障碍及一个有限概率条件估计，区别于只优化原upper certificate。不宣新颖性/重大性，不增同义结果ID，未经外部同行评审。

## 1. 原构造与本轮尝试

实际读原PDF1–19、Appendix相关scope，并以PDF13/15/17–19核公式。固定d=m+1，优先d5。原cube base Q=[0,1]^m、apex (0,1)，n次dyadic subdivision。原Prop4.1令P_i=∏_{j≤i}(1−t_j)，0<t_j≤1−c，得到

    |U_n|≤|T|[P_n^d+(1−c)^{-d}Σ_{i=1}^n(P_{i−1}−P_i)^d].    (1)

原调参t_i=1/[n−i+(1−c)^{-1}]给O(n^{1−d})，不是n个独立体积压缩因子的乘积。原Remark4.5已用Hölder说明这个upper证书至少(n+1)^{1−d}；本轮不把重证此句当新结果。

尝试包括：每级最大固定压缩；不同层/不同坐标的参数与深度；非齐次公平branching的证书；允许一定坐标耦合的全方向placement。前两类有下面实际volume或neighborhood lower，最后只在耦合熵足小时有条件lower，没有产生反例。

## 2. 最大固定压缩的真实失败

cube取每级t_i=1/2，虽P_n=2^{-n}，原递归给每leaf translation w_k=−k r（逐坐标），r=2^{-n}。在clock h，单坐标slice为

    A(h)=∪_{k=0}^{2^n−1}[−hkr,−hkr+(1−h)r].

h∈[1/4,1/2]时相邻intervals重叠，故|A(h)|=h+r(1−2h)≥1/4。高维slice是A(h)^m，于是

    |U_n|≥4^{-d}.                                      (2)

这是完整连续方向、unit-clock线段、有界centers的实际失败，不只是(1)不够精。取指数小core并未把冒出的branches整体volume同步压小。

## 3. 可变公平层数：仅证书的范围

若第i层用可合法迭代的fair partition、收缩常数c_i，而同一归纳给出证书

    B=P_n^d+Σ(1−c_i)^{-d}(P_{i−1}−P_i)^d,

令Δ_i=P_{i−1}−P_i、Δ_{n+1}=P_n，则ΣΔ_i=1。weighted Hölder给

    B≥[1+Σ(1−c_i)^{d/(d−1)}]^{−(d−1)}≥(n+1)^{−(d−1)}. (3)

若每次为真partition，branch count≥2；共同fair尺度的leaf宽r_nat≈(∏|I_i|)^{-1/m}，则n≤C_m log(1/r_nat)。identity branch没有c_i<1的正压缩。故此证书不能输出fixed power于其真实工作半径。若把n任意取远大于log(1/r_target)，须另估更粗r_target-neighborhood；不能仍用r_nat的upper。

(3)不是所有非product构造的实际体积lower。与其混用，会错误地排除未研究的隐藏overlap；下面的实际lower有另外的几何假设。

## 4. 任意坐标可分离放置的实际邻域下界

设K包含全部clock图段

    ((a1 t+b1(a1),...,am t+bm(am)),t),  t∈J,

其中a_i独立遍历一个固定非退化有界interval，J为固定正长度interval，b_i可任意（无需可测性；论证只选有限网）。则存在c,C>0，使每个充分小r满足

    |N_{C r}(K)|≥c[log(2/r)]^{−m}.                    (4)

常数只依m、固定intervals/J；intercepts bounded时K可包含于固定ball。不能从(4)声称K的Hausdorff维数满维；这里排除的是本轮拟议的fixed-power neighborhood upper。若是有限depth的实际product pyramids，取各坐标内含的common-clock strips，可另得|U|≥c∏(n_i+1)^{-1}，见B完整稿。

(4)将由更广的§§5–7推出。它uniform于递归深度，因此即便n(r)≫log(1/r)，只要仍coordinate-separable，实际r-neighborhood也不能成为r^κ。

## 5. 有限概率估计的全部假设

固定r小。A=(A1,...,Am)的每坐标位于固定有界interval的r-separated等距网，共M≈r^{-1}个值。允许任意有限joint law (A,B)，B∈R^m；方向坐标A可相关，B可同时依赖所有A。假每个Ai atom probability≤K0/M。设K含每个positive-probability support (a,b)的完整共同clock段

    {(b+t a,t):t∈J},

J长度ℓ>0固定。定义（natural-log entropy）

    S_r=Σ_i H(floor(B_i/r)|A_i),
    TC(A)=Σ_i H(A_i)−H(A)≥0.

将证明

    |N_{C_m r}(K)|≥c_{m,ℓ} exp(−S_r−TC(A))
                         [K0 log(2/r)]^{−m}.           (EG)

K可由有限segments的并替代，所以可测性没有漏洞。一般方向分离、只知平均marks、或每条段不同clock端点不能免费赋给本命题；§8另付实际common-clock删选。这里不允许把部分dense时间marks填成完整segments。

## 6. 完整平面L²计算与同时good times

对第i坐标，令μ_{i,t}为B_i+tA_i的law与uniform[-r,r] density的卷积，e_i(t)=∫μ_{i,t}²。取独立两份(a,b),(a',b')的同一边际law。若a=a'，两平移interval的L² kernel积分于J至多C_ℓ/r；若a≠a'，碰撞时间长度≤Cr/|a−a'|，每时kernel≤C/r，故时间积分≤C/|a−a'|，uniform于intercepts。

对固定a，另一Ai'的每atom≤K0/M，所以harmonic sum给

    ∫_J e_i(t)dt≤C_ℓ K0[1+log M]≤C_ℓ K0 log(2/r).     (5)

同斜率项用1/(Mr)=O(1)，异斜率按距离kr求Σ1/k。B的任意条件相关没有进入此上界。由Markov及有限并集，存在|G|≥ℓ/2，使所有i在t∈G都有

    e_i(t)≤C_{m,ℓ} K0 log(2/r).                        (6)

令X_i(t)=floor((B_i+tA_i)/r)。若p_k=P(X_i=k)，来自第k个bin的全部质量卷积后落在长度3r的enlarged bin。Cauchy后sum，enlarged bins重叠至多固定次数，得Σp_k²≤C r e_i(t)。Shannon entropy≥collision entropy，故在G上

    H(X_i(t))≥log(1/r)−log[C_{m,ℓ}K0 log(2/r)].        (7)

这给同一good-time集上的所有marginals，不把不同t的结论相乘。

## 7. 坐标相关的真实费用与体积返回

记X=(X1,...,Xm)。conditional subadditivity及data processing给

    ΣI(A_i;X_i)≤ΣI(A_i;X)
      =ΣH(A_i)−ΣH(A_i|X)
      ≤TC(A)+I(A;X)≤TC(A)+H(X).

给定精确Ai和floor(B_i/r)，X_i最多有两个可能值；因此H(X_i|Ai)≤H(floor(B_i/r)|Ai)+log2。结合(7)，

    H(X)≥m log(1/r)−m log[C K0 log(2/r)]−S_r−TC(A)−m log2. (8)

每个positive-probability X-bin都含某个K_t点。该r-cube整个在fixed C_m r-neighborhood of K的同t切片内；这些cube互不重叠。所以切片体积≥r^m #supp X≥r^m exp H(X)。对G积分即得(EG)。没有把sum of marginal entropies直接当joint entropy，TC及S均未被抹去。

若Ai独立、B_i=b_i(Ai)，TC=S=0，得到(4)。这里有限网选择来自完整Cartesian方向family，不需为任意非可测b_i作Fubini；实际积分对象是有限segments的并。

## 8. 从真实Kakeya集合取共同clock：支付方向相关

对一般bounded compact Kakeya K⊂R^{m+1}，先固定clock横截方向patch v=(a,1)/sqrt(1+|a|²)，a∈固定小m-box。在每r-grid方向中仅作有限witness选择。每单位段的clock长度≥固定ℓ0，所有端点clock在固定bounded interval。取有限组长度ℓ0/4的clock intervals，保证每条段至少完整覆盖其中一个。

某个J因而保留至少p≥p0(K,m)>0比例的原grid directions。**保留方向不是Cartesian product**。令A在保留S⊂grid^m上uniform，density p；其每marginal atom≤1/(pM)。相对原uniform product U^m，

    D(P_A||U^m)=log(1/p)
       =TC(A)+Σ_i D(P_{A_i}||U),

所以TC≤log(1/p)，K0=1/p可用。把保留segments写b+t a，(EG)给

    |N_{C_m r}(K)|≥c p^{m+1} exp(−S_r)[log(2/r)]^{−m}.  (9)

所有clock/方向crop费用真实保留。无需方向→segment的measurable selector，只有有限choice。若换clock原点，givenAi后intercept-bin entropy最多差O(1)，也不隐藏大费用。

于是，若同一个K真有|N_{r_j}(K)|≤C r_j^κ，κ>0，则在workmesh r=r_j/C_m上，对任何上述保留density≥p0的witness选择，必有

    S_r≥κ log(1/r)−m log log(2/r)−C_{K,m,κ}.            (10)

反之，若存在这种witness/bucket选择使S_r=o(log(1/r))，则沿该尺度不可能有fixed-power neighborhood upper。这是必要coupling-entropy门槛，**并未证明任意K的S_r小**，也没有覆盖所有Hausdorff-dimension counterexamples（其neighborhood可不满足本轮power目标）。

## 9. 回到原FD对象与compact patching

原cube的共同每层参数给coordinate-separable translations，允许各坐标不同schedule/depth仍属于§4。A稿给Lemma2.5可显式选择保product的shifts：若half-height basecenter q_i有B(q_i,c r)⊂T_i，则N_{2r}(T_i)⊂C T_i−(C−1)q_i；为contained于C T_i+Cw_i应取新placement v_i=Cw_i+(C−1)q_i。q_i的horizontal坐标逐坐标可分，vertical恒定，故该canonical continuous-direction patch仍不能power。有限旋转并只会增大neighborhood；已有一个固定patch lower便足限制该单尺度family。

原5.4从合格全δ的Gδ及nondecreasing f，经局部方向net/anisotropicpatching给同一compactE、f(Cd δ1/4)。directionnet数ε^{−m}与patchdet ε^m抵消，产生f(δ/ε)而非旧volume乘新volume。nested neighborhoods保证同K；每个固定direction的segment endpoints有compact相容链，极限保unitlength。fixedpower输入会保正幂，但原log输入不会因重复引用5.4自行变power。

**范围限制：** (4)不适用于任意最终patched E，因各patch的clock/frame可不同、intercepts可耦合；(3)也不排nonproduct实际geometry。本文排的是明确的调参/可分离复制方案，不是反原FD定理，也不证明更一般power构造不存在。

## 10. 本轮停止与下一宏观责任

本轮未找到fixedpower构造或Hausdorff反例。原source/canonicalcube/各坐标独立异速参数不能借隐藏overlap过关；有实际lower及最大压缩实际失败作为证据。低couplingentropy的有限law也过不了(9)，但高S耦合情形开放。

按一轮停止条件冻结仅改变t_i/coordinate depth/公平branching上界/独立productpatching的log→power局部路线，不继续把S、clock或branch参数改名作新方向。§§5–8是条件概率推论与必要门槛，不是从真实source已提取的新小S输入，不登记重大成果。R42须按既定宏观规则评估仍活跃的非可分离机制、已可用4D输入与高维目标，先查旧CP/PM/shared-time失败等价性再选main；不能自动续本轮entropy常数或certificate优化。

两代理已实际全文读本文10节、macro8节、nextgate及对方稿，正式 R0041_source_and_mass_review.md、R0041_direction_and_limit_review.md 均通过明确范围；root实读两稿及两份正式review后完成 R0041_root_integration_review.md。外部primary及本项目证明层次分开，未经外部同行评审。
