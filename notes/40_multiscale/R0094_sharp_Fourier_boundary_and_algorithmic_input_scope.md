# R0094：真实whole-clock的锋利傅里叶边界与算法输入审查

2026-10-18，Goal active。已知谱边界的完整原对象核算及源接口反攻，非新Hausdorff界/重大结果；未经外部同行评审。

## 1. 完整任务、定义与一手比较

完整目标仍为n≥5/general Hausdorff Kakeya或真正重大中间结果。本轮检验不同输入：能否借完整方向线段的Fourier衰减或point-to-set编码直接取得高维结论？下文证明谱下界2及其完整全方向sharp反攻，拒锁新gain。不续R93数字参数、R92模轨道或旧CP/PM/PW正幂等价。

对compact E⊂Rn，定义dim_F E=sup{s∈[0,n]:存在Borel概率μ、suppμ⊂E，|μhat(ξ)|≤C_s(1+|ξ|)^{-s/2}}。Fourier变换取exp(−2πiξ·x)。FHK2105.11414 currentv2=2021-09-27，物理3–4定义/Th2.1/Cor2.4、§3是具名既有Oberlin型方法：compact(d,k)-set的k≤d/2给dimF≥2k。Fraser2505.09464v1原文物理1–2明确Euclidean Kakeya至少Fourier2且高维可exact2，引用其Fr24+产品论文；本轮结论不是新发现。该2025文章的主要finitefield定理不作Euclidean transfer，亦不把2026期刊日期误认新arXiv版本。

## 2. Compact原线段的真实可测选择

固定n≥2及compact Kakeya K。对θ∈S^{n−1}定义C_θ={a∈K:a+tθ∈K对所有t∈[0,1]}。C={(θ,a):a∈C_θ}闭于compact S^{n−1}×K：可只查可数有理t，再由K闭补全，因此C compact、每fiber非空compact。标准compact-valued可测选择（亦可用R91已付JvN及a.e.Borel version）给σ-a.e.的Borel anchor a(θ)∈C_θ，σ为球面概率。可测多值关系的开集逆像为Borel：compact C与开anchor集合的交是Fσ，投影为Fσ。故可用标准Kuratowski–Ryll-Nardzewski选择定理。

不要求a连续或一阶导数。坏方向零集任取原合法a，采用完成σ；其pushforward仍给Rn上的Borel概率。原K compact，所以若所得μ(K)=1则suppμ⊂K。本段仅对compact K陈述Fourier支持结论；任意原集合的同维Gδ hull虽可用于Hausdorff证明，不能把hull上measure的support说成包含于原非Borel K。

## 3. Smooth clock直接给endpoint R^{-1}

固定非负φ∈C_c∞((0,1))，∫φ=1，定义μ为(a(θ)+tθ)在σ(dθ)φ(t)dt下的pushforward。它是实际原段内部的概率，suppμ⊂K，没有增加邻域、补段或换载体。先作真实clock积分，

μhat(ξ)=∫_{S^{n−1}}exp(−2πiξ·a(θ)) φhat(ξ·θ)dσ(θ)。

对任意M>1，|φhat(u)|≤C_M(1+|u|)^{-M}。设R=|ξ|≥1、ω=ξ/R。取绝对值后的球面积分≤C_M∫(1+R|ω·θ|)^{-M}dσ(θ)。在|ω·θ|≤1/2，球面坐标u=ω·θ的density有固定上界（含n=2）；积分≤C∫_0^{1/2}(1+Ru)^{-M}du≤C/R。其余球面部分≤CR^{-M}，无需把n=2两极的坐标density冒称全域有界。于是

|μhat(ξ)|≤C_n(1+|ξ|)^{-1}。

常数只依n及固定φ，不依anchor正则性或K的位置。若用裸uniform clock，粗绝对值min(1,|ξ·θ|^{-1})可给logR/R；内部smooth权实际消去此额外log，不以忽略log冒endpoint。该方法及dimF≥2是经典既有结果的原对象推导。

## 4. 从衰减到维数：临界处不授正体积

标准Riesz energy Fourier公式给0<s<2时I_s(μ)<∞（s<n时使用；n=2也取s<2）：原点附近积分有限，∞处radial幂为R^{s−3}。因此dimH K≥2，且§3本身在Fourier定义中达到s=2。n=2给dimH=dimF=2，但不推出Lebesgue正测度；|μhat|²的R2积分在上界R^{-2}处为log临界，不是L2。

在n≥5，上述2仅为弱已知下界，不能替代已审四维Hausdorff输入，更不能把Hausdorff full dimension自动当Salem/fullFourier。这里证明的是一个真实原measure，不是有限δ近似的极限support无证归属。

## 5. 真正全方向的产品Kakeya对象

取一个compact planar Besicovitch集P⊂R2，Leb2(P)=0且含每方向unitsegment；其存在为经典Besicovitch定理，也已在本项目早期来源/Lang经典构造中具名使用。不用R93互补数字F参数作新方向。令m=n−2≥1，E=P×[0,1]^m。

给任意unit θ=(u,w)∈R2×Rm。若u≠0，在P中选方向u/|u|的unit段a+s u/|u|，0≤s≤1；其子段a+t u、0≤t≤1仍在P。对每个w_i，取b_i=0若w_i≥0，b_i=−w_i若w_i<0；因|w_i|≤1，b_i+t w_i∈[0,1]。故(a,b)+tθ全在E，physical长度恰1。若u=0，任取a∈P同样构造。这逐一供应全部sphere方向，不只是平面或产品坐标方向。E compact且Lebn(E)=0。

§3在P上给支持P的概率ν且I_s(ν)<∞，s<2。cube上Leb概率η有I_q(η)<∞，0<q<m。因|(x,y)|^{-(s+q)}≤|x|^{-s}|y|^{-q}，I_{s+q}(ν⊗η)≤I_s(ν)I_q(η)<∞。取s↑2、q↑m给dimH E≥n，故dimH E=n。这是该同一对象的完整满维校准，不是对所有高维Kakeya的新证明。

## 6. 任意支持measure的Fourier维数上限

假设E上任何Borel概率ρ有某s>2的衰减|ρhat(ξ)|≤C(1+|ξ|)^{-s/2}。投影π:Rn→R2到P，τ=π_#ρ为概率且suppτ⊂P，τhat(ζ)=ρhat(ζ,0)。于是∫_{R2}|τhat(ζ)|²dζ<∞。由Plancherel（有限measure视为tempered distribution及Fourier唯一性）τ有L2 Lebesgue density，故τ(P)=0，与τ(P)=1矛盾。

所以dimF E≤2；§3又给≥2，得到dimF E=2、dimH E=n。上限排的是**所有**支持measure，不只§3选中的occupation measure；不允许靠换一个更聪明的概率、取正权或普通affine坐标消去这个普遍反攻。s=2本身未被排，正是二维L2临界。n≥3的全体Kakeya不能普遍要求Fourier维数>2，尤不能普遍要求Salem；这是文献已知边界，非新严格低维Kakeya反例。

## 7. Algorithmic新源的实际资格和精确反攻

Lutz–Lutz1511.00442官方currentv4=2016-12-01，原PDF30页。Th1 point-to-set对任意E⊂Rn确给dimH E=min_A sup_{x∈E}dim^A(x)，无普通可测假设。§5 Th5/Lemma6/Claim3给平面Davies证明；物理12直接说明高维候选数可达2^{(n−1)r}，索引成本可能Ω((n−2)r)，不能把平面harmonic/Borel–Cantelli步骤无费推广。高级算法维数工具具名，不凭恒等式获n5新估计。

Polson–Zantedeschi2603.25611v1（2026-03-26）《Kakeya Conjecture and Conditional Kolmogorov Complexity》，原25页，Prop1假设整张ψ:Z×U→X有效bi-Lipschitz、injective和computable，不是仅anchor a(e)正则。若Z方向维n−1且U为区间，jointbiLip本来就几何保持product满维，原rough Kakeya未授此输入；只证明此条件后果不算新的结构提取。

另有独立精确proof-step反攻：Prop1物理7取G_s=(Z∩2^{-s}Z^{n−1})×(U∩2^{-s}Z)，声称每参数有O(2^{-s})近邻并可枚举。取α=√2/2，Z={(α,0,…,0)}，U=[0,1]，X=Z×U，ψ(z,u)=(z,u)；a(z)=(z,0)、φ=e_n。所有列明compact/computable/jointbiLip/injective条件均满足，甚至是identity限制，但G_s始终为空，所写搜索不停止。该精确对象否定字面网格步骤，不否定Prop1结论本身；修复需合法有效nets/可计算紧性及approximation编码，不能据此说整篇定理已假，更不能为了Goal把修这个proper proof当高维突破。本项目不采用其Prop1作为已认证输入。

## 8. Label与shading闭包：保什么、未保什么

对球面可测方向子集Ω、σ(Ω)=a>0，归一化σ|Ω/a及同一φ/原anchors仍有§3衰减上界C_n a^{-1}(1+|ξ|)^{-1}。不保常数独立a，不说剩余全方向；任意带权law需另付band非集中。此为实际合法label闭包，不需PBP/jointAD，且不能倒推原全部shadings的gain。

clock删选则不同。逐管正density λ不保证包含非零smooth timeweight：枚举(0,1)内有理数，用总长<1/2的开区间覆盖它们，令F为其在[0,1]中的闭补集。则|F|≥1/2而F空内点，没有任何非零连续非负φ且supportφ⊂F。真实roundδ管的圆柱主体上取Y_T={a+tθ+w:t∈F,w⊥θ,|w|≤δ}，保体积≥(1/2)主体体积，即对充分小δ有统一正逐管density；任何非零smooth纵向weight仍不可能全部落这些原marks。若每label保这样的times，密度仍正却没有本证明的smoothclock输入。平均λ连逐label的clock质量亦不保；heavy-label提取只保原方向权的相应比例，不能恢复共同φ。这里仅否免费重用本构造，不声称这些shadings不支持其他Fourier measure。R91关于振荡mask/BV的旧失败不重名登记。

§6反攻有全原unitclock，λ=1，所以提高平均或逐管density不能修普遍dimF>2。若主张在原smallfootprint/完整Def17等额外条件下得到不同谱估计，须实际核全部输入；本产品不宣完整source反例。任意原非Borel K的Hausdorff同维hull也不付suppμ⊂K的Fourier责任。

## 9. Band预算与不同问题的停止界线

§3的推广若方向概率ν满足对所有unit ω及0<r<1，ν{|θ·ω|≤r}≤C r^β，则同样分层给|μhat(ξ)|≤C'(1+|ξ|)^{-β}，取smooth φ的M>β；Fourier下界至多2β。此uniform band指数不可能β>1：对ω的球面Haar积分、Tonelli及旋转对称性给∫ν{|θ·ω|≤r}dσ(ω)=σ{|θ0·ω|≤r}≈c_nr，矛盾于Cr^β。故这一取anchor相位绝对值/strip预算的机制不能产生>2普遍指数，范围不是所有带相位抵消的Fourier方法；而§6另外已对普遍dimF>2结论给真全族反例。

FHK的k-plane结论需要每个所需Grassmann方向有真实统一尺度k-ball，k>n/2才能由其β=k谱估计跨Lebesgue L2门。原unitline输入k=1；rank3的局部filledgrain、δ厚片或某稀疏orientation族不是(5,3)-set。不能把细grain重标为unit3-ball而不计方向law、原shading、尺度与返回费用，亦不据此解冻R40/R61。旧CP/PM/PW均未由本轮导出新正幂，算法或谱语言不可当等价改名的新方向。

## 10. 本轮结论、独审与下一完整目标

本轮实际付compact witness/原smoothclock及sharpR^{-1}单measure、完整full方向产品、dimH=n而任意measure dimF≤2的L2反攻，以及算法文献的真实输入与精确grid反攻。均先primary比较，不登记数学新ID或宣major。资料入库与源proof读域分层，四维官方身份非正确性认证。

本轮拒phaseII新gain、ordinary维数改善、完整branchsaving或严格低维Kakeya反例；保守streak17，完整ordinary初始化、HRZ全部费用、sticky临界κ1/余mixed及ordinary桥、同集full方向严格低维构造仍open。停止普遍Salem/更大band指数和算法directextension/desiredjointbiLip续轮，不续R93数字/PBP、R92singleorbit等旧冻结。两actual全文独审、档案验证与同SHA/fulltree同步完成后Goal仍active；未达最终目标不作complete。
