# R0100：共享时间环带算子与原正质量准入

2026-10-19，锁working后施工；sourceclaim与项目推导分开，两独立限定全文审查及root整合已通过，本有限应用账内部reviewed，未经外部同行评审。没有新的高维维数界。

## 1. 完整目标和本轮命题

目标仍是ordinary n≥5/general Kakeya、真同集全方向strict低维反例，或一手比对支持的重大中间结果。A实际复核OAI4完整§11、HRZ原窄转线性、DIM/FSD/KT等旧全称闭包，未找不同新出口；B核完整sticky scalar出口与matrix剩余责任。此次选择此前未采用的共享clock三角Hilbert环带估计，检验其是否能提供原sameT联合质量输入；不续R99 PSD/operator系数路线。主命题是支付实际signed用途，严格检验其向非负incidences和合法shading转移，若不闭则停止直接套用。

## 2. 官方原件与声明层级

OpenAI署名《Annular variation of the triangular Hilbert transform at the symmetric point》，2026-10-05。固定官方commit1581d4cbdd69a0faf34b2089614fe2a814316a6a，目录README与原PDF Gitblob实际对照；PDF37页523253B，SHA256 f5857c58037fa5289f2f9fe1fe4421af11df8d9fa9b2914ba041469f1195ea31。README只给作者/日期/引文，不据此声已Lean认证。root实际PDF1–6定义/主声明/坐标与Lem2.1，PDF2/4原图核；外部37页高级proof未完整独审。下述正用途条件于源Th1.2/1.1正确，独立反攻不依赖它们；不将其当已建立文献定理。

源定义Bε,R(F,G)(x,y)=∫ε<|t|<R F(x+t,y)G(x,y+t)dt/t，对complex L³输入。Th1.1声每r>2 pointwise output-dependent全正radius partitions的annularvariation，L³/²≤Cr||F||₃||G||₃。Th1.2声至多N个disjoint radius intervals的S_N= supΣ|Bεj,Rj|满足||S_N||₃/₂≤C√N log(2+N)||F||₃||G||₃。这里radius为正，但每个积分仍含t两符号，abs在积分之后，不能读成正向dt/t或unsigned dt/|t|。

## 3. 真实三角坐标和条件正用途

对H,F,G∈L³及任意至多N个disjoint annuli（可依output点选择），源若成立，Hölder给

∫|H(x,y)|Σ_j|B_j(F,G)(x,y)|dxdy≤C√N log(2+N)||H||₃||F||₃||G||₃。

固定annuli时，Σ_j|∫H B_j|亦由同右侧控制。output-only系数β_j(x,y)、|β_j|≤1及合法annuli线性化包含在该bound内。取x=−a、y=−b、t=a+b+c，三维绝对Jacobian1；G₀(a,b)=H(−a,−b)、G₁(b,c)=F(b+c,−b)、G₂(c,a)=G(−a,c+a)，各二维pair map绝对Jacobian1、L³norm不变。故这是真正cyclic pairwise entangled signed三角形式的用途，不要求三坐标事件独立；但尚未声原WZ g已具有这些因子。

## 4. 独立连续反攻：正质量线性而所选signed值为零

固定0≤χ∈C_c^∞(R)、χ=1于[−2,2]、支撑[−3,3]，F(x,y)=G(x,y)=χ(x)χ(y)，norm均固定不依N。取Q=[−1,1]²，r₀=1/4，r_j=r₀2^{-j}，j=0,…,N。对(x,y)∈Q和|t|≤r₀，两translated inputs都恒1。因此每个所选annulus r_j<|t|<r_{j−1}有B_j=0；单正半轴积分A_j⁺=log2，负半轴按dt/|t|的A_j⁻=log2，unsigned A_j⁺+A_j⁻=2log2。于是Q上的正向sum=Nlog2、unsigned sum=2Nlog2，其L³/²norm≥常数N。

这给真实连续、任意多尺度的严格反例：不能把源Th1.2右侧C√N log(2+N)用于上述正/unsigned版本；也不能把Th1.1用于积分内取abs的正variation。固定F/G的norm和Q测度使N/(√NlogN)→∞。只说这N个小annuli的signed B_j为零，不声全sup S_N或全variation在Q为零（更大annuli可非零）。这不是对原sourceclaim的反例。

## 5. 奇偶分解显示真正未付的桥

对非负F,G，令A⁺_j,A⁻_j为两半轴上的非负积分。signed B_j=A⁺_j−A⁻_j，原正关联是A⁺_j+A⁻_j或仅A⁺_j；估计差不能反向估计和。源线性化kernel为Σβ_j(x,y)1_{εj(x,y)<|t|<Rj(x,y)}/t，它对t仍odd。选择β输出依赖或complex相位不使它在固定output上变为1/|t|。若用sgn(t)乘kernel则正化了，却不是同一允许类。

对一般mask m(t)，写m_e(t)=(m(t)+m(−t))/2、m_o(t)=(m(t)−m(−t))/2，则m_e/t为odd，m_o/t为even。仅仅0≤m≤1或m很平滑/少跳，不控制新增even部分。用m=1_{t>0}便在小annuli上将原signed零变成正Nlog2。若提出别的调制/分解来表示正量，须支付其真实范数与误差；本反攻不排尽所有未来编码。

保留真正可用的条件情形：对非负三对输入，若在H所测output和负时间支上乘积为零，则B_j=A_j⁺，§3确可给该正量上界。未证明原g/geometry具有此支持事实，不能授为新假设；也不能因为一般正化失败便否定这一合法用途。

## 6. 合法原shading和两种密度的闭包

对任意原unitaxis a_i+s v_i、s∈[0,1]，以中点为τ=s−1/2，保wholeaxis但只保τ>0的marks。圆帽δ管用垂直中分平面截其一半，中心反射将两半交换，因此每管体积密度恰1/2（分界超平面零测）；原direction separation、wholeaxis本身和非负weights未改，平均密度也恰1/2。故在原普通管族的基本shading类中，两种density都允许破坏t↔−t的配对；与R99许多内部BV跳点的障碍不同，这里只需一个半clock窗。

此操作未证明保完整WZ多尺度AD lower、selected ξ或所有local fullness，不能冒它为fullsource counterexample。它证明的是：若一条新operator桥只用全轴/平均或逐管density作假设，该桥不能免费假设odd cancellation在任意合法shading下保留。合法geometric restriction的单调性与signed estimate的闭包须分开；重归一还须付所留质量。

## 7. 真实原g为何尚未落入该算子类

WZ20.3的(164)–(165)和21.1的(172)–(173)使用原selected dense graph及共享point/time/angle关系；21.2允许G⊂A×B×C且dense，但c仍scalar。已付R76 §6–8更给两端原label product×第三uniformclock的g≤1及实际密度，保全部原S_T；OAI4 Def2.1/8.2也允许相关incidence event，仅需μ_act≤Kν⊗dt。不因‘g相关’本身拒用。

真正未付的是把该具体原g在同一个质量分母下表示成源三对L³因子，或放入只依output-pair的β而不依第三变量，并让其目标正量在odd积分中不相消。triple domination可用于unsigned上界，但abs后失去cancellation；不能由0≤g≤1反向比较signed积分。没有从这些原接口得到新mass lower、原δ-angle编码、规范与误差/ambient返回，故不声已应用Th1.2排完整matrix或mixed分支。

源L³是二维Lebesgue输入规范，原ν和方向/point Frostman priors不是免费同一规范；若先离散或平滑到此空间，三对函数的真实L³norm、原N/I分母、δ宽度与误差都要付，不以g≤1抹去这些费用。

## 8. 可用的无条件正上界及费用

原Lem2.1的unsigned estimate可直接独证：对固定t，Hölder和平移不变性给||F(x+t,y)G(x,y+t)||₃/₂≤||F||₃||G||₃，Minkowski积分给2log(R/ε)倍右侧；加|H|再Hölder给三L³norm乘同log。dominated g或合法marks可在这个正上界中删去，保absolute mass而不需因子分解。§4在R≤r₀的core同时给线性log下界，说明该直接unsigned费用不能uniform改为o(log)。

若使用常见dyadic物理scales[δ,r₀]，N≈log(1/δ)，signed count相对线性N改善至√N logN也只为δ^{o(1)}，没有自动给固定δ^η saving。源允许更细和output-dependent partitions，不能据此断言所有应用都只有log；若主张polynomial N的原族收益，还须真实给各annulus原mass lower、范数、尺度与正量恢复。本轮未获该输入，不以附加成功假设代替。

还必须分开原uniformclock ds与核dt/t：中心化t=s−s₀后，在r<|t|<2r上，正的dt/t计数相对原ds质量多1/r（常数范围内），原质量是带r权的annulus和。不能把每个加权环带log2当每个原clock窗保相同质量。若目标本来只是固定有限J上的非负Lebesgue ds三对相关量，最初的Hölder/Minkowski已经给≤|J|·||H||₃||F||₃||G||₃；不需要新singular算子，也没有额外正幂。只有真实新核编码与原范数预算才可能改变该判断。

## 9. 与完整高维路径和旧失败的关系

普通/HRZ：只知三角算子的新scalar signed强度，不改变原五维narrow/coarse主幂，原parent/terminal与marks责任仍在。sticky：原matrix33 κ1的nativeY AD1投scalar可饱和，mixed42的同T contact→scalar affine/quadratic轨道仍未付；新源不是matrix ABC sumproduct或全角直clock重接定理。反例路线：§4正operator反攻与半clock shading不构造严格低维full-direction集合，不能升级为Kakeya反例。

旧R99 PSD有限输出的CV覆盖不被新题名解冻；当前失败来自signed-to-positive/order依赖而非PSD秩。即使接受新THT主claim，未得到此前没有的原positive gain，所以不登记新resultID/major/ordinary界。此区别是实际新输入审查，不把旧完整定理泛称等价，也不声所有oscillatory方法无用。

## 10. 停止、独审和后继

完成条件signed用途、严格连续多尺度正反攻、原基本shading两density和真实g接口后，直接THT桥停止；不续r、partition数、频块、mask平滑或加公设factorization。当前没有qualified下一主gain候选；后继需真正原joint positive mass/ambient返回或不同完整机制，而非将其写成成功假设。需A/B/C实际独立全文读与formal，sourceclaim高级wholeproof未审仍保；仅本有限应用账可内部reviewed，未经外部同行评审。Goal active。
