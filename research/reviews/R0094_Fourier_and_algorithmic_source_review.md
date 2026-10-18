# R0094：真实时钟谱边界与算法来源独立审查

2026-10-18，A。内部逐步终审，未经外部同行评审；仅认可下列明确范围，不认证未来元数据、提交或同步。Goal active。

## 1. 实际全文对象、来源与分工

本次fresh实际全文读当前root主稿`notes/40_multiscale/R0094_sharp_Fourier_boundary_and_algorithmic_input_scope.md`全部10节、B稿`notes/00_map/R0094_complete_routes_and_new_mechanism_countergate.md`全部8节、自身A gate `notes/00_map/R0094_primary_frontier_and_original_input_gate.md`全部8节、reselection_spec与working_spec各5节，以及终macro、next、`literature/notes/R0094_Fourier_and_algorithmic_primary_scope.md`各6节。主稿的n=2两极、任意支持测度、PZ精确singleton反攻及shading区别均为实际读取后的审查对象，未以早期计划替代终稿。

四篇primary的实际读域分别为：FHK 2105.11414 current v2=2021-09-27的Fourier维定义、β-scaling、Th2.1/Cor2.4及§3对应smooth-clock方法；Fraser 2505.09464 only v1=2025-05-14的Euclidean比较intro；Lutz–Lutz 1511.00442 current v4=2016-12-01的§3 point-to-set、§4 conditional/chain-rule声明、§5及appendix Claim3对应harmonic/Borel–Cantelli证明；PZ 2603.25611 only v1=2026-03-26的§2–3 Prop1条件和正反编码proof、Cor2及§4.3。本次又实际读回本地Lutz物理12及PZ物理7以核高维限制与字面网格步骤。没有声称读完四篇全部高级证明。arXiv Lutz原30页与STACS另排13页分开，PZ25/FHK13/Fraser8的归档事实按root记录，不冒本人逐文件字节核验。

A gate的来源筛查及推导不算自己的独立审查；本formal重点逐式核root/B的实际谱、全方向产品、原mass与反攻链，A正证已由root/B另核。经典来源声称、接受具名定理、项目有限推导、内部独审及外部同行评审分层。

## 2. Compact选择、真实概率与endpoint衰减

root第2节的关系C={(θ,a):a+[0,1]θ⊂K}确为compact：anchor在compact K，有理clock条件闭，再由原K闭补全所有clock。每方向有非空compact fiber。对anchor开集O，C∩(S^{n−1}×O)在compact关系中为Fσ，可分解为可数compact层；其投影为Fσ，所以这里的compact-valued弱可测性确已付，标准可测选择可用。采用完成球面概率及a.e. Borel版本也足够。pushforward给Borel概率且μ(K)=1；K闭才保证support包含于K。没有把同维Gδ hull上的概率support冒作任意非Borel原K的support。

固定φ∈C_c^∞((0,1))、φ≥0、积分1，所有质量都在每条原unit segment内。先对t积分得到anchor phase乘φhat(ξ·θ)，然后取绝对值，不需anchor连续或可微。对R=|ξ|≥1，在|ω·θ|≤1/2的球面坐标density有统一上界，∫(1+R|u|)^(-M)du≤C/R；外侧integrand≤CR^(-M)，直接乘总球面质量。n=2的密度只在两极发散，外侧估计避开该问题，主稿没有把它误作全域有界。M>1遂给同一个原概率的|μhat(ξ)|≤C_n(1+|ξ|)^(-1)，常数不依原anchors或位置。

固定smooth内部clock消去裸区间绝对值估计中的log，不是假删log。由Riesz energy的标准Fourier表示，0<s<2时高频radial幂为R^(s−3)，原点附近则为可积的R^(s−1)，所以I_s有限。s=2的二维平方积分仍log临界，不能推出L²或正面积。该完整谱下界2与FHK k=1既有Cor2.4一致，不是本项目的新n5/n6下界或maximal估计。

## 3. 真全方向产品与对所有支持测度的上限

root/B取同一compact planar Lebesgue-null Kakeya P及E=P×[0,1]^(n−2)，n≥3。对任意unit θ=(u,w)，u≠0时在P中取沿u/|u|的unit段的前|u|部分，按共同t∈[0,1]写a+tu；额外每坐标选合适初值使b_i+tw_i始终在[0,1]。root选b_i=max(0,−w_i)，B负号时选1，二者都合法。u=0时固定任意平面点。整段切向量正是θ，physical长度1，故已供应所有真实n维方向，而非只显示坐标或proper方向族。E紧且Lebesgue零。

满Hausdorff维亦已独立支付。平面概率ν的I_s有限，s<2；cube Lebesgue概率η的I_q有限，q<n−2。乘积范数不等式给I_(s+q)(ν⊗η)≤I_s(ν)I_q(η)，令s、q分别逼近端点得dim_H E=n。B改用平面s-Frostman概率再乘cube亦给相同真实下界。没有从纯Minkowski计数或只从full方向断言该高维维数。

上限对任意Borel概率ρ、support⊂E成立：若有s>2的Fourier衰减，投影τ到前两坐标满足τ(P)=1且τhat(ζ)=ρhat(ζ,0)，其平方在R²可积。将有限measure视为tempered distribution，Plancherel及Fourier唯一性使τ具有L² Lebesgue密度；P零测迫τ(P)=0，矛盾。故没有任何支持ρ可达到s>2，配第2节得dim_F E=2。它不只反某个occupation概率，也未排临界s=2。该对象同时真全方向、零体积、dim_H=n，所以不是Kakeya严格低维反例。Fraser intro已记录高维exact2谱边界，不能宣新颖或major。

## 4. 算法输入与PZ字面proof步骤的精确反攻

Lutz point-to-set对任意E的min_oracle sup_point恒等式是合法Hausdorff工具，必须保“任意oracle”的下界责任。实际平面proof另付标量候选壳的harmonic求和和a.e. clock上的sublinear index，再以chain rule消去anchor条件描述。它不假设anchor可计算或低复杂度。原文物理12明确直接高维扩张会有2^((n−1)r)候选、index可能Ω((n−2)r)；不能把方向(n−1)r和clock r直接当作原点nr信息。本轮未支付这项新的高维列表估计。

PZ的Prop1则原本要求整个ψ有效joint双Lipschitz、injective和computable，并非仅e↦a(e)有某种正则性。若full-dimensional参数域已joint双Lipschitz，经典几何本已保持其满维；不能赠送该输入后将条件后果称原rough Kakeya归约。其原始proof没有作为项目已认证输入采用。

root的精确proof-step反攻有效。取n≥2、α=√2/2，Z={(α,0,…,0)}、U=[0,1]、X=Z×U，ψ(z,u)=(z,u)，a(z)=(z,0)、φ=e_n。该identity限制满足列明compact、有效joint双Lipschitz、injective及computable条件，甚至其singleton是可计算紧的；但Z∩2^(-s)Z^(n−1)对每个整数s为空。因此原物理7所写G_s始终空，nearest-grid-point与搜索必停止的字面步骤确失败。此证书只否那个步骤，不否Prop1结论，不否所有可计算逆像方法；真正修复须使用合法近似nets/编码及实际可计算性，不能将修proper步骤当完整目标成果。本formal没有替该外文献作整篇真假认证。

## 5. 原label、shading与闭包的不同责任

正球面质量a的可测方向子集用σ|Ω/a仍可沿原anchors、同一φ得到C/a的衰减常数；a损不能删除，也不再声称满方向。一般权重law需实际付uniform hyperplane-band上界。任意概率ν若对所有ω、r有band质量≤Cr^β，Haar平均该band事件恒≈c_nr，故β>1不可能；这是root第9节对取anchor相位绝对值/strip预算方法的实际端点，不是对所有相位抵消或所有谱工具的否定。

逐管正density不保smooth clock。dense开集覆盖所有有理点且总长<1/2，其闭补F有正长度而空内点，任何非零连续函数都不可能support在F内。在圆柱主体保t∈F给原round δ-tube统一正逐管体积比例，但没有这条现有证明所用的纵向smooth权；平均density更只控总incidence。root/B据此仅否免费重用同一φ，没有声称这类marks均不支持其它衰减测度。保留原indexed I、W及方向权的费用；小label族重新归一会改变CW等常数，不能由一个存在的好概率控制全部原Y_i。

FHK的k-plane结论也需要真实规定orientation的统一尺度k-ball；局部filledgrain、δ厚片或rank3场不是full (5,3)-set。原尺度、方向law及shading返回没有在本轮被支付。算法、谱和有限域题名没有建立新CP/PM/PW正幂结论，亦未证明所有这些工具互相等价；现有统一gain的旧闭包不得改名重开。compact-support傅里叶结论不扩到任意原集合的Gδ hull，符合当前规格。

## 6. 结论、实际读域与停止范围

root10及B8在上述有限范围内全文通过，无未解决强制项。尤其已实际核compact selector、同一个原measure的endpoint、n=2外侧处理、全θ产品unitclock、任意ρ的投影L²矛盾、product Hausdorff下界，以及PZ空网格严格例的hyp和限制。来源高级point-to-set基础、完整FHK cone部分、Fraser有限域wholeproof等未因本内部审查获重新认证；自身A gate不算自己的独审。未经外部同行评审。

终macro6/next6/source6均已actual全文读回。四条完整路径保持：ordinary原多尺度、directHRZ全费用、sticky临界κ1/余mixed及ordinary桥、同一全方向严格低维构造。已知Fourier2和完整exact2谱反攻没有带来ordinary增益、fullbranch saving、新ID或重大结果；拒锁相应gain及保守streak17与实际资格工作并不矛盾。下一未预选定新主命题，不以更改smooth clock、band指数、产品参数或desired joint-biLip续轮，也不把PZ局部修复列作高维突破。

本review认可的是已知谱边界的原对象证明、合法来源层级和明确停止结论，Goal仍active。不认证后续档案数更新、验证、Git或同SHA/fulltree同步；相关数目仅属root实际档案记录。本文件完成后停止编辑与检索。
