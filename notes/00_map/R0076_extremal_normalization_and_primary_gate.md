# R0076阶段I：极值归一化的原量词与临界联合输入筛查

2026-10-18，A。Goal active。本稿只核源入口和候选可用性，不把阶段I当本轮主数学，不先证明尚未锁定的临界新命题。仅编辑本文件；未做Git、下载、元数据修改或新代理。高级原证明保留具名输入，未经外部同行评审。

## 1. 实际读域与本轮量词

已实际读GOAL、STATE/ROADMAP当前交接、registry当前键及状态入口，R76 working_spec五节、macro六节及R75 next六节；实际重读R43主稿十节中无权prior、bounded-mark lemma、parent/coarse、§18和相对尺度预算。原文使用本地Wang–Zakharov 2609.22035v1全文提取，实际读Def3.1–3.10、Obs3.2–3.4、Obs4.1、Def17.1–17.4、Prop17.2及§18 Prop18.2六步和Prop18.1三步，重点核(104)–(145)的原T、shading与重标度。这里的全文阅读不是重新独证全部§18几何或高级输入。

临界候选另外实际对照R18 W-mass/inverse主稿与R72同管双时边界；重读已存CSWZ 2610.13682v1引言、Def1.4–1.5及Th1.6–1.7的完整声明。没有本轮新远端identity检查或新PDF；R75的官方三核心identity是root已完成的记录，不能写成本稿独立fresh API核。原来源：[WZ v1](https://arxiv.org/abs/2609.22035v1)、[CSWZ v1](https://arxiv.org/abs/2610.13682v1)。未命中新来源不认证前沿穷尽或新颖性。

## 2. 原literal类、bounded marks与构造输出是三个范围

Def3.6的joint参数为slope a∈[-1,1]^(d−1)、intercept b∈R^(d−1)，Def3.9只规定各occupied parent在r≤1的AD双边计数，未排无界远隔copies。Def17.1对R^d中的T和平均δ^η-dense shading作全称，未单列U(T,Y)在一个固定盒中。相比之下Def17.2明确E⊂[-1,1]^d，却未字面写T等于全部used tubes或whole joint参数有界。不能把这三句话合并成同一规范。

Obs4.1的前提确为p∈[-1,1]^d。它用固定数rigid charts处理斜率方向，不能仅凭此把任意无界point-line family的全部原质量放进同一fixed box。§18.2 Step2直接定义X⊂Ω_d为bounded (x,t,θ)，并引用该观察表示原pairs；若从literal无界counter开始，这一入口仍需要原约定或额外localization说明。这里不凭OCR或padding例宣原定理错误，也不将未审的global localization追认为已完成。

下文体积density统一指原(19)的bounded whole clock，或其共同clock内的等价dyadic管形。不能把Def3.6的无限支撑line-union当有限体积tube直接代入平均density。

## 3. Bounded marks直接给N上界：这是R43旧闭包

设全部原marks在固定盒B_R，原whole tubes体积≈δ^m，m=d−1，原平均density为λ，原AD upper常数K。记A为有mark的原labels。每active管的slope有界，intercept由其一个bounded marked point有界，故其joint参数落固定有界区域；用固定数unit joint cubes和AD upper得

    #A≤C_R K δ^(−m).

每管mark体积≤Cδ^m，而Σ_T |Y(T)|≥cλNδ^m，故

    #A≥cλN，N≤C_R K λ^(−1)δ^(−m).                 (1)

这是R43§4倒数段已明确写出的lemma，不是R76新结果。平均density只给active比例，不给每active tube逐管λ；若要逐管下界，tube-heavy阈值cλ能保固定比例总incidence，但其余label及原AD lower不能顺便重置。

删whole labels到比例p的uniform子族，normalized CW最多乘p^(−1)，原AD upper以绝对计数保留；AD lower一般不保。只删shading而不改whole T，CW不变，但平均density须按实际incidence另算。若输入原为逐管density，整label分区且保全部Y_i时逐管原下界保留；缩shading则不自动保留。

## 4. Parent归一化的真实分母、AD lower和whole bounded用途

保原whole family且由(1)知道N≤CKλ^(−1)δ^(−m)。对occupied τ-parent，原AD lower给N_τ≥K^(−1)(τ/δ)^m，故其原质量

    p_τ=N_τ/N≥cλK^(−2)τ^m.                         (2)

共同clock shear ψ_τ(x,t)=((x−b_τ−a_τt)/τ,t)的体积Jac为τ^(−m)。因此parent normalized CW/PW常数的真实费用为C0 τ^m/p_τ，代(2)至多C C0 K²/λ；无权coarsening再付K²，成C C0 K⁴/λ。parent lowercorner用来保原dyadic树；不能以轴中心比较代替occupied-bin lower。R43已付这些原操作和相对新尺度预算。

N upper和wholeT bounded不同：(1)允许少量unused管非常远，它只限制总count；另一方面，把每条实际输出管都置于一个bounded parent再重标度，才给whole joint coordinates有界。R75近kernel footprint/原N分母等用途若引用bounded wholeT，必须由后一个实际构造提供，不能只引用N≤Kδ^-4。AD upper付bounded active count，AD lower付occupied-parent count；二者角色也不能倒置。

## 5. §18实际保什么，尚未认证什么

§18.2的初始(104)是small global union，(105)改写为multiplicity。Steps1–3依次保原Y0、X′及Y′，T′确为has-X′-marks的原active集合，因bounded X′而joint参数有界；原uniformization另外证明T′自身AD，不能仅从任意active restriction得到它。Step4 (107)/(109)用的是原T_ρ,Y及原parent family，不是免费让T′以较差η_ell替原η。

决定whole bounded的实际步骤在§18.2 Step5末：取δtilde=√δ_ell，选原T_{δtilde}使Y″在该parent内平均dense，再令Ttilde=φ(T_{δtilde²}[T_{δtilde}])。每一条输出whole axis都来自同一parent，φ送parent到单位管；因此输出whole管族有固定bounded chart。Step6中的E/Y/Φ/f整理没有把远隔unused labels重新添回去。原量词是平均density选parent，并非每管原来都dense。

§18.1 Step1明确再次选T_τ，T1=T^ρ_{Tτ}；迭代次数受d控制。Step2若ℓ下降，再按18.2取parent/coarse与shading refinement；Step3 (145)调整兼容关系、最终厚化。故这些实际构造输出的whole bounded规范是可追踪的，不是额外物理方向分离。CW继承仍用原parent分母和相对scale损失，非无费删除全部unusedT。

据此可补清“对实际normalized extremal输出适用”的范围；它本身是已存在构造/闭包的核清，不算不同主数学。由literal Def17.1任意无界counter到首次bounded X的入口并未在本稿新增证明，R43还保留Δ_J/√δ_ell等原几何层级边界。不能因本稿读到最后parent就宣全部literal K_d极值proof已独证或自动全K5(1)。

## 6. 全目标四路径与候选排重

ordinary初始化仍缺从一般full directions原集合到所需joint AD/CW全层的保亏损提取；R49条件regularization不授该入口。直接ordinary窄几何中R48/61 HRZ terminal规范有真实固定幂饱和，R60全λ三维carrier估计/R63同轴桥不解决非同轴四维narrow。四维finite seed及KT递推已经R29/R38核过有限范围，重算六维17/4或更多维数不是新机制。真构造仍缺同一全方向compact set的固定power cover，R47 cyclic方法已冻结。

源侧R75在bounded规范下付κ>1，κ=1时native Y和Φ均维1，fine det-large bound的δ^(2κ−2)消失。R74 AD0、R71packet/R72更多time/basicness与R18/W任意图独立化不能改名续题。selected兼容 ξ_q−ξ_p=(F_t−F_s)φ+Oδ虽是真原信息，但rough原E不授Rademacher/Dorronsoro好点落在原mass、smooth flow或Markov mixing。

本轮没有找到一个新primary全称定理直接填ordinary/general入口。候选若采用现有投影primary，必须实际满足它的local Schubert/spread-out，而不能仅用time AD、SM或det-large代替。

## 7. 唯一可锁的不同实际图：临界root-code与其严格primary反攻

建议仅检验完整matrix33 κ=1的actual det-large两时访问图，不先假其成立于全clock。固定原t,s，h=s−t，A=F_t−F_s，假设|h|、s_min(A)有显式δ^b lower并付全部K误差。对真实同管selected p@t、q@s，以native坐标写p=(x,y+F_t x,t)、q=(x′,y′+F_s x′,s)，则

    x′=x+hφ+Oδ，ξ_q=ξ_p+Aφ+Oδ，
    y′=y+hξ_p+Ax+hAφ+Oδ，
    (y+Ax, y+hξ_p)=(y′−hξ_q, y′−Ax′)+O(Kδ).       (3)

这是两端selected ξ共同出现的code，不是R18单一厚W endpoint。固定code后，左右根各由其原Y-label决定x、ξ，故fine纤维upper≤K^Cδ^-1；K依h/A的已付逆幂。若实际sameT图在足量(t,s)有≥K^-Cδ^-4 edges，可检验双边peeling到degree≥K^-Cδ^-1，返回同一原t-slice point law的dense子图，而非固定一个好tuple。于是候选主责任是：这些原label近满code纤维和真实四矩形，能否与filled X及空间Φ-coherence联合得到有正幂用途的多尺度估计。只有恒等式、peeling或期望rectangle completion都不能结案。

这里有现成投影调用的严格障碍。固定root t的共同图Σ_t={(x,y,ξ_p)}⊂R6有3维Frostman upper（原packing X²、Y¹与ξ coherence；没有Σ光滑假设）。code是线性投影L_s(x,y,ξ)=(y+A_sx,y+h_sξ)。其kernel以v∈R²参数化为

    K_s={(-A_s^(-1)v, v, -h_s^(-1)v)}.             (4)

在以y作base的big cell，矩阵Θ_s=(-A_s^(-1); -h_s^(-1)I_2)的两个off-diagonal ξ/y坐标恒0。因此整个family位于CSWZ Def1.5的model hyperplane（一坐标rank-one测试）中，每个scale都是singular。等价地，任意固定非零线性l，所有K_s均与固定W_l={l·y=l·ξ=0}这4-plane有非零交。换有界linear chart不能消掉这个Schubert包含。故CSWZ Th1.7不能被直接调用；time AD、SM乃至任意F的det-large也不会去掉这个结构零。

这仍可能需要真正point-adapted Schubert factor或不同root联合law，但尚未支付；改变t后Σ_t变动，不能冒同一P的投影族。它给一个可证伪、原质量明确的新图筛查，而不是已证projection gain。严格停止：若仅(3)/code数、假公共fine Φ、假independent endpoints、或将(4)直接授spread-out，即记无信息增益并冻结该用法；不以增加fixedtimes或conditional projection公设补它。

## 8. 阶段I结论与后续授权界线

归一化结论是R43旧bounded-mark闭包加原§18实际parent输出的核清；whole normalized输出与literal无界起点须分别保留。没有据此新立ID、宣全K5(1)、ordinary新界、重大性或proof正确性认证。完整高级结构抽取与其外部输入仍具名，内部阅读不能替代独立wholeproof或外部同行评审。

当前唯一建议是第7节actual两端root-code候选，其直接CSWZ调用已被结构Schubert包含严格挡住。是否锁为本轮phaseII、以及要证明真实新估计还是构造保持全部原有限输入的反攻，由root在spec先锁定；本稿未先施工未授权定理。若该候选只产生旧W/BSG、basicness或更多fixedtime的等价重述，立即停止，不把阶段I筛查当主数学完成。Goal保持active。
