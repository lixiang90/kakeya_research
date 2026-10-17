# R0065：有理双时间曲率、原输出图与物理尺度审计

2026-10-18，A。仅本assigned文件，不操作Git／spawn或文献／元数据。已实际读working_spec原4节及先写补充§5、macro4、STATE首部、R64 next6；重读R16 original tuple／source linewise application／finite vector命题和R58 secant主稿。本稿独立核有限命题及source接口，不把fixed rational input授给完整WZ配置，不声普通高维／major或外部同行认证。

## 1. 正式原量词与额外输入

固定D、M、C0，0<r<1；F=P/Q在固定time interval上为2×2有理矩阵，degree≤D、系数≤M、|Q|≥1/M。ν为原时间概率，ν(I)≤K(|I|+r)；π为原差标签概率，|ψ|≤M，宽w≥r的任意slab质量≤K w^γ。σ为任意原输入y概率。0≤g≤1可以任意相关，每个正权tuple满足y+Tψ(t,s)距Aplus≤C0r，Tψ=(t−s)(F(t)−F(s))ψ；N_r(Aplus)≤K r^(−2+κ)。没有把g边缘独立化。

Jacobian采用Jψ=N/[Q(t)^3Q(s)^3]。某一个固定time monomial系数作为ψ的homogeneous quadratic，其coefficient maxnorm≥r^θ，0<θ<min(1/6,κ/6)。此为定量额外输入，不是仅“某处rank2”，亦不从原SM、slab或bounded g自动推出。

spec§5另有两个固定interval、两个有理式F1(t)、F2(s)的矩形版本，各原概率保持各自cap；长度、denominator扩展与格式费用按spec支付。R64双曲线只符合这种两chart描述，不能偷称一个跨gap全域P/Q。

## 2. Jacobian分母、degree与角二次型

对单chart写Δ=P(t)Q(s)−P(s)Q(t)。∂tT的矩阵numerator可取

    U=Δ Q(t)+(t−s)[P′(t)Q(t)−P(t)Q′(t)]Q(s)，

denominator为Q(t)^2Q(s)；∂s对应denominator Q(t)Q(s)^2。故N=det(Uψ,Vψ)，time total degree≤6D，关于ψ恰homogeneous quadratic。spec使用d=6D+4是安全统一上界。两chart按同一乘法逐项成立，不能用det(Ft−Fs)代替该双时间Jacobian。

取指定time系数q(ψ)，设其norm为L≥r^θ。任意实homogeneous quadratic在有界ψ盒中满足：{|q|≤uL}可由至多两个宽C_M√u的slabs覆盖。证明为固定orthogonal diagonalization：definite情形最大绝对eigenvalue控制一个坐标；indefinite情形写成两个实linear factors，norm较大的eigenvalue保证每个factor的normal norm有固定lower，乘积小迫至少一个factor小。退化rank1包含在第一种；不需要两个eigenvalues均有lower。

于是角坏集|q(ψ)|≤r^(2θ)质量≤C_M K r^(θγ/2)。查询宽度r^(θ/2)≥r，slab floor合法；原重复ψ标签及权保持，不取distinct ψ后改uniform。

## 3. 两变量sublevel的自含核查

一元degree≤d polynomial若coefficient maxnorm≥A，则在固定bounded interval上，|p|≤b的集合长度≤C_d(b/A)^(1/d)，右边大时取trivial常数。可从该集合按长度分位选d+1个互距≥c_d length的实际点；Lagrange公式给每个coefficient≤C_d b length^(−d)，即得。零测端点不影响该Lebesgue论证，degree0也由trivial／empty两支包含。

对角good的Nψ，某time coefficient≥r^(2θ)。按t展开，选一个s-polynomial a_i(s)仍有此coefficient lower。|a_i(s)|≤r^(5θ/2)的s集合长度≤C_d r^(θ/(2d))。其余s上，N作为t-polynomial有coefficient≥r^(5θ/2)，故|N|≤r^(3θ)的t集合长度同样≤C_d r^(θ/(2d))。Fubini给二维Lebesgue坏集≤C_d r^(θ/(2d))。这里只用固定格式coefficient lower，不假每个time section都非退化。

## 4. 原离散ν的smearing与相关g

不能直接把ν²替成Lebesgue。给每个原time加独立Uniform[−r,r] jitter，ν_r的density≤ν([t−r,t+r])/(2r)≤CK。对two-chart分别作同样jitter；固定r小于C(D,M)保证各自denominator仍≥1/(2M)，函数及一阶导有统一C(D,M) bound。较大r用trivial m≤1并扩大固定常数覆盖。

精确测度写法是把原σ×ν1×ν2×π及jitter共同乘g再推前。所得原总质量仍m，且相对σ×ν1,r×ν2,r×π有某可测density ghat∈[0,1]；这是domination／Radon–Nikodym结论，不声原条件时间独立。T的固定Lip bound使所有正权新tuple满足同一Aplus的C(D,M,C0)r邻域条件。原标签、y、ψ原权没有丢失。

因此§3坏时间集合在新原reference下质量≤C K² r^(θ/(2d))；这一步已支付原atoms和r-floor，不能另要求原ν无atoms。某些原times在critical curve上也由同一jitter收费，而非直接忽略。

## 5. good Jacobian与实际输出面积

在余下点|N|>r^(3θ)，Q bounded给|J|≥c(D,M)r^(3θ)。对每个固定ψ和target z，Tψ=z是两个degree≤2D+1的polynomial equations。Jacobian非零的解为regular isolated intersections，其个数由经典Bézout的regular-isolated版本统一≤C_D；允许两方程有公共component，不错误地声整个fiber有限或map全局injective。area formula给任意Borel target B

    Leb{(t,s):Tψ(t,s)∈B, |N|>r^(3θ)}
        ≤C(D,M)r^(−3θ)|B|。

对每个原y，Aplus−y的Cr邻域可由K r^(−2+κ)个固定倍r-balls包住，面积≤CKr^κ，即使Aplus自身未指定可测也可先固定该有限Borel包络。乘ν1,r×ν2,r的density bound CK²再积分σ、π，所有good tuple质量≤C K³r^(κ−3θ)。这里估计的是原bounded图能占的product-reference质量，非Jacobian积分直接等于union面积。

连同前两坏集得到spec目标

    m≤C(D,M,C0)[K r^(θγ/2)+K²r^(θ/(2d))+K³r^(κ−3θ)]。

常数可以统一于0<γ≤1，因slab固定倍宽的C^γ≤max(1,C)。固定θ后再选h<min{θγ/8, θ/(12d), (κ−3θ)/8}，K≤r^(−h)、m≥r^h时小r矛盾。此只核本有限命题，不称完整source满足其extra hypotheses。

## 6. R16原fine graph可直接使用，不重置prior

R16已付：某good q、实际fine time B_f=Z_q、used方向H、endpoint z*与good τ-window，τ=Cδ^(−Oη)ρ²；原fine输入A_f^−及输出A_f^+=Y_(z*)∩CQ，图G在A_f^−×B_f²×H²密度≥K⁻C。原每个edge满足

    y2−y1=(z−z′)(f(z)−f(z′))(φ1−φ2)+O(τρ+δ)，

且m_f=#B_f≥K⁻¹ρ/δ。这里H来自used incidence-mixture的heavy bins，非unused coarse Φ_q自动slab。该原bounded图已由逐项tuple-fiber upper支付，不是直接把多重L-tuples当indicator。

本命题允许任意σ和非separated ν，故可直接取σ=Uniform(A_f^−)、ν为B_f经t=(z−z0)/ρ的原uniform标签，不必重做R16时间／空间coarsening。fine时间cap为K(|I|+δ/ρ)；取r=ρ，source允许ρ≥δ^(1/4)，于是δ/ρ≤r。π保原H×H ordered差标签，其slab在宽≥ρ=r上有效。额外自由度只受原g限制，未改reference或引入条件AD。

## 7. Aplus绝对cover来自完整Y，不仅来自ratio

仅有#Aplus≤K#Aminus不足以套本命题。实际R16 good τ-window的输出是完整原Y_(z*)在O(τ) patch内，因此可使用full Y的AD lower／upper packing。取其中最大τρ-separated centers；每个中心的τρ/10-ball含≥K⁻¹(τρ/δ)^(2−κ)原fine点，互不交且都在放大的C′Q内。full Y在C′Q的upper≤K(τ/δ)^(2−κ)，故

    N_(τρ)(A_f^+)≤K²ρ^(−2+κ)。

因τρ≈δ^(−Oη)ρ³≥δ，此为合法原尺度；κ=2时exponent0仍成立，不除以2−κ。若grain-label有近重复，R16已付的K重数可再吸入固定次幂。归一y/τ后即N_r(Aplus)≤K^Cr^(−2+κ)。没有给裁切A_f^−或A_f^+重新授AD lower；用的是周围完整Y，输入σ自身不需任何AD。

## 8. 物理单位与有理近似的准确额外责任

以y_norm=(y−y0)/τ，t=(z−z0)/ρ，取

    F_norm(t)=(ρ/τ)[f(z0+ρt)−f_ref]。

则真实平移严格变为(t−s)(F_norm(t)−F_norm(s))ψ。原输出误差除τ为O(ρ+δ/τ)=O(r)，因为sourceρ≥δ^(1/4)保证δ≤τρ。原dyadic f-Lip给F_norm幅度O(ρ²/τ)，有固定上界；但这不意味着它有固定degree rational extension。

若另有本轮P/Q模型R(t)在全部相关fine time labels上满足||F_norm−R||≤c r，则替换T误差O(r)，原g与Aplus原权保持，只有C0变固定倍。写回physical f，所需误差是

    e_phys≤c τr/ρ，r=ρ时即e_phys≤cτ。

不能把物理O(r)误差当规范O(r)，也不要求原f具有可微导数；Jacobian使用的是所给rational model。模型还必须在固定time interval上有denominator／coefficients／degree统一控制，并自身满足N系数≥r^θ。C0值近似不自动给该导数或coefficient lower。R16 coarse time centers并非原定义域时更不能把所选representatives免费称该中心上的同一有理函数；本fine版避开此问题。

K=δ^(−Cη)，ρ=δ^a_ρ、a_ρ∈[μ,1/4]，故K≤r^(−Cη/μ)。D、M、θ、κ、γ先固定，η最后小到Cη/μ≪h即可支付上述固定次损失。未证明实际source能提供rational model／N lower，故这是一个诚实的条件接口，不是commonkernel整体排除。

## 9. 与旧linewise及普遍D-Frostman的不同量词

若F=F0+v r(t)^T为固定common-image，或F=F0+h(t)M为任意matrix pencil，则对每个固定ψ，Tψ(t,s)在一条固定line内，Jψ恒0，故本定理不覆盖R16已排分支；反过来R16标量Th13.5也不直接给此处二维area-formula估计。R58的uniform Lip plateau复杂度随r增长，没有本轮固定D及coefficient条件；本命题不反该旧反例。

一个明确覆盖的新条件子类是commonkernel F=u(t)e1^T、u(t)=(t,t²)。此时

    Tψ=((t−s)²,(t−s)²(t+s))ψ1，
    Jψ=4(t−s)³ψ1²。

因此N有fixed非零系数，但F(t)ψ并不沿单line，旧linewise不适用。这也严格说明不能将本命题声为全raw law的2-Frostman：取uniform time与ψ1处于固定离0区间的slab-Frostman角law，|t−s|≤c√r的原质量≈√r，而T在O(r)-ball内。critical对角必须在本证明按bad-J费用处理，不能全局忽略。

整个有理非退化子类未从真实source提取，故普通高维／全PW4／完整A-D gain不能反向由本界直接推出。任意Lip数据的Bernstein／Taylor近似往往令degree或coefficient控制随r增长；本C(D,M)不授这种uniform控制，也不继续旧R44 degree／palette路线。

## 10. 两chart测试、restriction及停止范围

R64负branch用u=2t+3、F_−=c diag(u,u⁻¹)，正branch用v=2s、F_+=c[[0,v],[v⁻¹,0]]，c=1/8。各可取D=2、M固定；两个interval分别长1/2。取ψ=e2，t=−3/4、s=3/4，直接微分得Jψ=−1/8，因此其Jacobian numerator不是零polynomial，coefficient norm有固定正lower（由固定degree的evaluation bound）。这是two-chart模型，不能当单一全域有理式。

对任意原ν／π，restriction或删shading只把g换成0≤g′≤g，结论上界原样成立，支持条件及reference均保留；平均图质量可如此闭包。若另把time子集或angle子集归一，K须分别除该原质量，不能声保逐管density或AD lower。对两个固定branch先限制时也必须用原branch mass支付，R64各为1/2，只固定常数；任意δ-dependent tiny chart不免费。

已实际全文读root最终14节及B最终9节：两种先smear全部g或先删original bad-J再smear的证明均合法；root面积e的两次Fubini／Lagrange给1/(2d)，B的系数切片法同指数。独核B完整cross因式式及[t⁵s]N=2ψ1²，以及真实H−H角law的nearzero mass≳r；这些校准只否全law2Fst，无一反有限三项上界。未见强制数学修改。

已实际打开[Terence Tao, Bezout’s inequality, 2011-03-23](https://terrytao.wordpress.com/2011/03/23/bezouts-inequality/)，阅读Theorem1／Corollary2及共同因子说明：它给代数闭域内两平面多项式的零维components个数上界。此处清分母后的Jac非零使每个所用real解同时是complex isolated解，故应用合法；并非任意real isolated set都能如此嵌入。其高维推广与高级证明不作为本轮新认证。

已完成独立推导、实际fine-source条件接口和root／B数学全文审查；最终macro／next范围另记指定formal。未声原source有理化已付，未独证Th13.5／完整WZ或ordinary Kakeya，未经外部同行评审，不认证新颖／major／新ID。完成本轮正式独审后停止D／M／θ／h参数，不借换名字重开旧普遍D2Fst、linewise或raw分类。
