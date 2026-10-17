# R0056：原五维格点插值、可付的近轴误差与不可免费的最高次项

2026-10-17。主任务在working_spec §7先声明后执行。以下是一次直接Euclidean高重数多项式证明尝试及其停止证据；不声称H5、一般Kakeya或exact-kernel方法已被否定。基础有限域结果已有文献，初等估计不登记新数学ID。内部审查记录另存，未经外部同行评审。

## 1. 原数据、要反证的规模与合法闭包

固定0<σ<1，a=(4+σ)/5<1，δ→0。原单位轴L_i=b_i+[-1/2,1/2]v_i在固定有界盒中，v_i为原S4的δ-separated满网，T_i=N_δL_i，Y_i⊂T_i可测。主目标仍从原near-full marks得到固定正幂的五维体积增益；没有换成原点bush或假设代数化selector。

本方法实际以δ-grid **cell footprint** Q为输入，K=#Q，E_Q为这些整格的并。反设规模K≤Cδ^{-(4+σ)}，等价|E_Q|≤Cδ^{1−σ}。任意可测E体积小不能单独推出这个覆盖数；从原离散marks到Q使用原定义的格，不重选方向、位置或clock。每管有δ^{-1+η}个原访问格时，本文保留其原访问，不补出独立time或满直线格点。一般tube shading转此模型另需原真实marks与固定格扩张预算。

whole-label/原marks删选使Q变小，故插值约束不会增多，但不保证剩余每管marks。平均与逐管不能互换：若平均访问≥λM、每index≤M，删访问<λM/2者后保至少一半总incidence，保留index比例至少λ/2；若有原权，完全相同论证只给原权质量≥λW/2。此后仍用其原Q/方向；不能重置成全部满网。本文的负门槛测试λ=1，不靠任何这类损失。

## 2. 真实exact interpolation与次数的方向

令S为Q的原中心，取整数m≥1。对每c∈S施加∂^βP(c)=0（|β|<m）；共至多K binom(m+4,5)个齐次线性约束。总次数≤D的未知数binom(D+5,5)，只要后者严格较大，就有非零实多项式。可取

    D=ceil[2(m+4)K^(1/5)],       D/m≤C K^(1/5)≤Cδ^−a.             (1)

这是自包含实数线性代数，不需数值求核；重复中心只减约束。记实际次数d≤D，必d≥m（任一中心的m重零点且P非零）。**(1)是上界，不是d≥cmδ^−a的下界。** 如能用原方向兼容性找远低于(1)次数且有良好范数的核向量，将是新输入；本稿没有排除。

有限域Dvir原稿§3/Th1.5使用degree≤q−1、每field line上的q个exact zeros，得到一元限制恒零，最高次齐次项在全部field directions exact为零。DKSS §2–3则使用Hasse derivatives和exact multiplicity。Euclidean格中心一般不在原轴上；不能把它们当q个exact共线点。这正是下面要支付的连续步骤。

## 3. exact中心到原轴：误差可以真实支付

保持原physical coordinates和unit clock。固定R≥1使全部原中心及轴点位于内cube[-R,R]^5，外cube为[-2R,2R]^5，原距离≤Cδ。只在Chebyshev基使用坐标x/(2R)，不缩放原轴或最高次项。归一化||P||_outer=1；以下固定常数可依R。

对多重Chebyshev基展开P。各系数绝对值≤2^5，非零基项的总次数≤d，共≤(d+1)^5项。对实中心|c_j|≤R、实向量||w||∞≤1，在复圆|z|≤ρ≤ρ0(R)有

    |P(c+zw)|≤C(d+1)^5 exp(Cdρ).                               (2)

证明单变量界：在固定内区间的复邻域，arccos的导数有固定上界；T_k(z)=cos(k arccos z)，故|T_k((c_j+zw_j)/(2R))|≤exp(Ckρ)。相乘后Σk_j≤d。Chebyshev系数界来自逐坐标余弦正交积分，有限展开不含任何δ损失。

q(z)=P(c+zw)在0有阶≥m的零点，q/z^m全纯。最大模原理和(2)，取ρ=m/(C0d)≤ρ0，给对原轴点x=c+ew（0≤e≤Cδ、e<ρ）

    |P(x)|≤C(d+1)^5(Cdδ/m)^m
           ≤C(D+1)^5(Cδ^(1−a))^m =: ε_δ.                      (3)

C0足大，exp(Cdρ)的固定exp(Cm)已吸入括号。若e≥ρ，式(3)的小误差用途不成立；(1)与δ足小时保证e<ρ。可选固定m大于常数/(1−a)先吸收poly(D)，或让m慢增，使(3)是真正的δ正幂。这里不是粗用Markov d²而误报第一步失败。任意原marks与其中心的距离界都有效，端点同样有效。

## 4. 沿实数单位clock抽系数的确切最优费用

对次数≤d、leading coefficient A的一元实多项式q，单位clockI=[−1/2,1/2]上最优不等式为

    |A|≤2^(2d−1)||q||_I    (d≥1).                             (4)

证：T_d(2t)的leading coefficient是2^(2d−1)，在I上sup1。若一个monic q的sup严格小于2^(1−2d)，将q与monic版本T_d(2t)/2^(2d−1)相减；在d+1个交替极值点上符号交替，差多项式有至少d个不同零点，但次数≤d−1，矛盾。非严格界取极限。因此(4)既有上界又有达到等号的连续例；不能用exp[o(d)]统一替换，即使整个unit clock而非稀疏marks上都小。

若只在可测S⊂I、|S|=λ>0上|q|≤ε，仍有足用的

    |A|≤(C/λ)^d ε.                                            (5)

自包含证明：按S的Lebesgue质量取d+1个等质量分位点，作任意小扰动落在|q|≤ε的有效点。累积分布1-Lipschitz，间距至少cλ|j−k|/(d+1)。Lagrange插值的td系数是Σ_j q(t_j)/∏_{k≠j}(t_j−t_k)。分母≥[cλ/(d+1)]^d j!(d−j)!，求和用Σ1/[j!(d−j)!]=2^d/d!以及d!≥(d/e)^d，得到(5)。实际离散marks不能未经处理被当Lebesgue集合；原相应短时间格可给有界重复度的集合，额外微小误差需按真实轴点处理。

## 5. 全原方向、整单位轴及端帽的近jet反例

取任意原S4 δ-separated满网，全部原位置b_i=0，Y_i=T_i，故逐管及平均λ=1。P_d(x)=x_1^d，其top homogeneous form H_d在S4的sup为1。在任何真实round tube T_i内，|x1|≤1/2+δ。对任意j≤d，

    δ^j |∂_1^jP_d(x)|/j!
       =binom(d,j)δ^j|x1|^(d−j)
       ≤(|x1|+δ)^d≤(1/2+2δ)^d.                               (6)

有其它坐标导数时该项为0。因此所有总阶<m的δ-scaled jets同时满足(6)，包括两端round caps，不需m log d≪d。给任意固定B>0，若d/m≥cδ^−a（a>0），δ足小时(6)≤δ^(Bm)，而H_d(e1)=1。若要求原δ-net确取到e1，可先包含它再取极大分离网；即使不含，δd≪1时邻近方向也保宏观H值。

这严格否定“近jet数据≤δ^(Bm)可无exp(cd)费迫top form小”的无条件gate。在最有利的全部方向、全部whole clocks、全部shadings都成立；不是只有有限样本验证。**这个bush的并集体积≈1，格数≈δ^−5，也未满足原S上exact jets=0。** 所以它不是小footprint的H5/Kakeya反例，更没有否定额外利用exactkernel关系的证明。本文没有把(1)误称为迫此d/m比例。

## 6. 回放完整尝试的两个独立范数责任

设q_i(t)=P(b_i+t v_i)，其td系数正是H_d(v_i)，与原位置无关。即使给最有利的全部I上的(3)，(4)也只得

    max_i |H_d(v_i)|≤2^(2d−1) C(d+1)^5(Cdδ/m)^m.              (7)

在最坏允许d/m≈δ^−a时，log右侧含c d−(1−a)m log(1/δ)+O(m+log d)；第一项压过第二项。若λ=δ^η，(5)还额外付dηlog(1/δ)，不会改善。改变m同时线性改变允许d；仅提高multiplicity不使δ^−a/log(1/δ)变小。**这是所用uniform估计预算不闭合，不是所有exactkernel向量都达到坏界。**

此外(3)归一化的是outer sup，而目标若把||H_d||_S4归一化为1，需支付比值A(P)=||P||_outer/||H_d||_S4。只知道P≠0并不控制此比值；例如1+εx1^d的top norm可任意小（此例不满足exactkernel，仅说明一般norm逻辑）。不能在(3)与(7)之间无费更换归一化。minimal-degree kernel及全family exact constraints可能约束A(P)，本轮没有证明相应condition number。

## 7. 方向离散到最高次齐次项也有门槛

若有来自其它方法的sup原方向H_d小，仍需δd≪1才可直接恢复S4 sup。沿great circle，H_d限制是次数≤d的trigonometric polynomial，Bernstein给导数≤d||H_d||_S4；故δ-net满足

    ||H_d||_S4≤max_i|H_d(v_i)|+Cδd||H_d||_S4.                 (8)

可以选m固定或足慢增，使(1)给δd≤Cmδ^(1−a)→0；所以这一费本身可付。不可同时任意大取m再无证用(8)。本稿不把可付的方向采样、中心Taylor或固定端点费用当主障碍；真正未付是exactkernel与原incidence共同给的特殊范数/外推信息。

## 8. 最新source输入筛选的实际结论

官方elliptic原PDF103页，Th1.1为E:L∞(S2)→Lp(R3)、p>3；Th1.2相位变量ξ与位置z都在R2；Cor1.3是三维L3 Kakeya maximal。它没有R5的E:L∞(S4)→Lp(R5)。源作者署名不是完整证明审查，全文高级proof未独证。

为定量排除误用，若另有五维球面local restriction ||Ef||Lp(B_R)≤C R^ζ||f||∞，取原δ-separated cap、调制到原位置、R=δ^−2、小固定cap半径cδ。球面恒等式vi·(ω−vi)=−|ω−vi|²/2使每个包在**整真实round tube** RT_i上模≥cδ4。独立随机符号和cap有限着色给||Σsign f_i||∞≤C，无须独立化原位置。Khintchine及缩放得multiplicity μ=Σ1_Ti的||μ||_(p/2)≤Cδ^(20/p−8−4ζ)。Hölder与原incidence≥λδ4 N、N≈δ^−4给

    |E|≳λ^[p/(p−2)] δ^[(8p−20+4pζ)/(p−2)].                  (9)

因此超过当前五维4基线需p<18/7并选ζ足小，sharp开放范围p>5/2可给full5的有限near-full结论；这是已知restriction→Kakeya机制的实际预算，不是新独立方向。HR1807.10940v3 Th2.1配Prop2.2及Figure1在n5给p>50/19，实际表面是truncated paraboloid，不是sphere。对该表面也可单独作同指数的包转移：相位(ξ,|ξ|²)，方向(−2ξ,1)归一化，沿法向的频率一阶项取消，余项O(Rδ²)；小cδ-cap及原位置调制保整管模下界δ4。有限旋转normal charts覆盖原方向，频率/方向Jacobian固定可比，无需声称paraboloid estimate等于sphere estimate。因此其平行版本(9)只到10/3，不能提供本项目新gain；此为一个明确历史输入，非2026最优认证。当前official3D结论不能换n调用(9)。

## 9. 与旧命题、独审及成果登记的边界

这次任务是直接对原footprint的exact linear kernel，不是G3、generic AD、CP/PM、四time或matrix门槛改名。若把“所有小footprint原family都有一个足够好conditioned kernel”直接当新公设，可因没有小footprint家族而被H5平凡蕴含；没有新的线性代数或几何内容前不能给它新方向ID。合法删选也不自动给这样的conditioned kernel。

已付实质信息是(1)–(8)的完整连续证明尝试、sharp exponential gate反例及两种norm区别，和actual primary新输入范围核验。没有新高维维数界、没有Euclidean Kakeya反例、没有新颖性/重大性认证。exactkernel专用condition和一般H5仍未证未否。独立A/B实际source与反攻记录必须以最终全文formal reviews为准，不预认证。

## 10. 停止决策和后继

停止仅凭高重数插值、通用Taylor/Remez及full方向抽top coefficient的uniform路线；不续Chebyshev常数、m/次数小调或把approximate counterexample升成exactkernel反例。重开至少要来自原straight-line incidences的额外kernel结构，并真实控制A(P)及exp(cd)损失；单写一个“良好核存在”公设不算输入。

宏观重新比较后，下一实际任务应回完整source机制而非这条标量外推的局部变体。全部旧冻结、G3中密度/一般→sticky入口以及高维Goal保持。未找到新可调用primary不是猜想的否证；本轮以可审查的失败和已付费用归档，Goal active。
