# R0088：锥面波包的原质量转移及直接读出边界

2026-10-18，root。新采用primary为Xiangyu Wang2411.02961v8的cone extension接口。下述是具体转移的来源应用和费用审计，不是新的高维界；未经外部同行评审。普通n≥5/general目标未解决。

## 1. 原任务与具名输入

原R5单位round δ管T_i⊂B_R，方向v_i在固定有向小chart中δ分离，N≤Cδ^-4；有限chart/颜色损失只常数。原可测Y_i⊂T_i，令E=∪Y_i、I=Σ|Y_i|，逐管|Y_i|≥λ|T_i|，或平均I≥cλNδ⁴单独处理。位置、chart和R固定，0<δ≪1、0<λ≤1。ordinary入口先取N≈δ^-4、λ≥δ^η，欲得|E|≥cδ^(1−σ)某固定σ>0，才有五维strict>4所需的有限强度。

仅条件调用新源Prop1.7：n=6、admissible p,q,k、2≤q≤p，任意ε>0有

    ||Ef||_{L^p(B_L)}≤C_ε L^ε ||f||_2^(2/q)||f||_∞^(1−2/q),
    Ef(y)=∫ exp(i(y′·ξ+y6|ξ|)) f(ξ)dξ,

f是频率annulus内Schwartz函数。原Th1.5的p,q及k条件、§2.1 mini-direction另实际核；不把cone conjecture当已证，也不新认证29页wholeproof。即使给理想必要端点p=5/2，下面同一scalar读出仍不足；当前源的范围更弱。

## 2. 共同map捷径的精确否定范围

令J=diag(I5,−1)。若一个共同affine map F(x)=Ax+b把开原方向集的所有线送为cone-null方向，则v^T A^TJA v=0在球面开集成立。齐次二次恒等性给A^TJA=0。im A是Lorentz全isotropic子空间；其向最后坐标的投影单射（最后坐标0而null迫全部为0），故rank A≤1。

若C1共同F在每个x和一个开方向集的所有原局部线都映为null曲线，同理DF(x)^TJDF(x)=0，rank DF(x)≤1，因而不存在R5的C1 immersion满足此输入。这里只用null切向必要性，不需完整直线保持分类。

这不排按label不同的lift，也不适用于仅在某个有限Kakeya选择上才有方向的map，更不排一般非光滑selector。其作用只是阻止把共同等距/仿射嵌入当作免费转移。属于初等已知Lorentz线性代数，不立ID或宣major。

## 3. 按label提升保真实marks，统一薄纤维尚未保

写x=a_i+t_i(x)v_i+u_i(x)，u_i⊥v_i。对round端帽亦有|t_i|≤1/2+δ、|u_i|≤δ，故不必丢可测marks或假其在body。取整个radial bandwidth范围δ≤τ≤1，设r=δ²/τ∈[δ²,δ]，定义

    S_i={(x,s):x∈Y_i, |s−t_i(x)|≤cr},  Z=∪S_i⊂R6。

每S_i是实际可测提升阴影，Jacobian 1给|S_i|=2cr|Y_i|，保原labels及同一clock；light长方向(v_i,1)与原v_i的角映射固定bi-Lipschitz。Σ|S_i|=2cr I。因为t_i范围固定，Z⊂E×[−C,C]，所以

    |Z|≤C|E|。                                      (1)

每label的纤维长2cr不推出整个Z每纤维长O(r)，也不推出|Z|≤Cr|E|。后者在§7给真实δ分离反攻，不以重复labels或体积代理构造。

## 4. 实际频率packet与短轴

令ω_i=−v_i。取非负smooth bump b_i，角支持在ω_i附近cδ，radial支持在3/2附近cτ，幅度≤1，积分A_δ≈δ⁴τ。小固定c使支持在annulus内部且各b_i角支持互不交（必要时固定颜色）。令

    f_i(ξ)=exp(−iδ^-2 a_i·ξ)b_i(ξ),   L=C_Rδ^-2。

在y=δ^-2(x,s)、(x,s)∈S_i上，消去共同中心载波后，phase的变动由

    δ^-2 [ ρ(t_i(1+v_i·ω)+u_i·ω+h) ],

控制：ω−ω_i=O(cδ)，1+v_i·ω=O(c²δ²)，u_i·ω=u_i·(ω−ω_i)=O(cδ²)，radial变动乘h给O(cτ rδ^-2)=O(c)。固定常数选择后所有相对phase落短弧，故

    |Ef_i(δ^-2(x,s))|≥c A_δ  在全部S_i上。             (2)

常载波可能快速旋转，只去其共同phase，不假整个complex值正。此构造直接付了packet下界，不把“essentially supported”自动当pointwise lower。物理大尺度长轴δ^-2、中轴δ^-1、short轴τ^-1；回unit尺度是1、δ、δ²/τ。源τ≈1的packet是mini-direction plank，τ=δ才是round尺度；不能免费把二者体积当一样。

## 5. Random signs、原N与真实Lebesgue返回

令f_ε=Σε_i f_i，ε_i独立Rademacher。频率支持不交给每个ε

    ||f_ε||_∞≤1， ||f_ε||_2²≈N A_δ。

用具名Prop1.7并取符号期望，Khintchine和(2)给M=Σ1_{S_i}：

    A_δ ||M||_{p/2}^{1/2}
       ≤C_ε δ^(12/p−2ε)(N A_δ)^(1/q)。               (3)

δ^(12/p)是R6真实dyadic isotropic回尺度，不是R5体积因子。∫M=2cr I≥c rλNδ⁴。Hölder在真实Z上写∫M≤||M||_{p/2}|Z|^(1−2/p)，再用(1)。对任意输出ζ>0，先选source ε足小，得到

    |E|≥c_ζ λ^A (Nδ⁴)^B δ^(β+ζ) τ^B，              (4)
    A=p/(p−2)， B=p(1−2/q)/(p−2)≥0，
    β=(10p−24)/(p−2)=10−4/(p−2)。

等价未饱和式为λ^A (Nτ)^B δ^((14p−24−8p/q)/(p−2)+ζ)。所有N、radial频率体积、short轴、λ和δ幂保留；没有把#occupied cells当Lebesgue体积或从projection体积免费加一维。

## 6. 近full读出、平均闭包与停止阈值

在N≈δ^-4时(4)的唯一bandwidth项τ^B≤1，故τ=1在该scalar公式中最强。cone extension的必要p≥5/2（下一节）给β≥2。即便理想端点且近full λ=δ^η、η趋足小，(4)也只是δ^(2+small-loss)的弱下界，不能给目标δ^(1−σ)。这是(4)这族实际scalar/Hölder读出的代数范围，不是断言一切别的wave-packet估计都只能如此。

平均I/(N|T|)≥λ_av时，§5直接用总I，不需heavy，所以同一λ_av^A式有效。若改用逐管调用，heavy density≥λ_av/2的原labels至少有λ_avN/2，须将此N′真代入(N′δ⁴)^B，额外付λ_av^B，而不是仍声N饱和。整label restriction保δ角分离却不保N；删marks须重算I/逐管密度。权重/重复方向不在本锁定独立分离输入里，不能以同sector任意重数仍||f||∞≤1；普通full方向finite选择已可取分离族，故此范围足以检验入口强度。

在近full用途里，已有四维finite seed/FSD给更强主幂，(4)不是新gain或可独立登记的新方向。完整all-λ估计的精细范数不由此宣与旧输入等价；这里只拒其作为当前ordinary新维数种子。

## 7. 必要p与免费r纤维的实体反攻

对固定非零smooth radial/角patch bump，cone extension在|y′|≈−y6≈L的固定厚shell上，angular stationary phase给幅度≈L^-2，shell体积≈L^5。局部R^ε对每ε成立于是必要5−2p≤0，即p≥5/2。可以在一个角patch和固定法向厚度内选phase主项非零，避免振荡零；这是标准cone decay必要性，不调用未证cone conjecture。当前源的admissible范围也不能越过此必要门槛。

实际否|Z|≤Cr|E|如下。取ρ=δ^a、0<a<1/4，固定小open角chart的δ网v_k（k∈Z4，N≈δ^-4）。原axis line都过0，但单位段中心a_k=c_kv_k。令Y_k=T_k∩{ρ≤|x|≤2ρ}在对应正向cone patch；每|Y_k|≈ρδ⁴，E体积≈ρ⁵。取整数M>C/ρ，给四tuple k mod M用单射code∈{0,…,M⁴−1}编码，c_k=Kδ code。

δM⁴≈δρ^-4趋0，故|c_k|≪1，全部annulus marks确在原单位段内部。同一x命中的两个不同方向满足|k−k′|≤C/ρ<M，故residue/code不同、|c_k−c_k′|≥Kδ；而|(v_k−v_k′)·x|≤C′δ。选K固定足大，则s=t_k(x)附近半径cr≤cδ的interval两两不交。因此

    |Z|=Σ|S_k|≈rρ， |E|≈ρ⁵， |Z|/(r|E|)≈ρ^-4→∞。

原directions真实δ分离、shading逐管density≈ρ且可取任意小固定a，是nearfull费用反攻；不是小方向、重复labels或Kakeya反例。该例只拒统一r纤维上界，也不声(1)已对所有source配置sharp到常数。若假有更强共享纤维条件，必须从原族另外证明且付款，不能补作成功公设。

## 8. 来源身份、实际读域与核验层级

官方abs/history显示v1=2024-11-05，currentv8=2026-09-30。本轮新增原PDF29页/495117bytes，SHA256 2f65aa8601906de65ff80f03dc80891628309957ea4241f32cadd71b685d339d，blob b3d5ccb90189f6e5fbbe94b58ef3166f96c533ec。root实际HTML§1.1、§2.1至Spatial Concentration、PDF1–5text、render/view2–3；此读域不是29页高级wholeproof独审。作者AI使用说明只作为来源信息，不能保证正确。

新文献入库为64PDF/68sources，既有78 IDs不变。A/B主稿负责实际重算与反攻，root随后实际全文读两稿及两份正式审查才归档有限内部reviewed；哈希、来源身份与数学证明分别记录。既有DIM001与GLX基线仅排重，不当本轮新成果。

## 9. 与完整目标的关系

新source确是高维cone restriction改进，但其cone、sector、mini-direction和scalar norm对象不同于原ordinaryR5。当前已付的只是一次实际输入转移及两处具体免费桥的拒绝。没有给出ordinary>4、fullG4、完整stickyκ、full方向低维集合或重大新结果。不能从本稿推出cone工具对一切未来几何、bilinear或multiscale方法无用。

四完整路径保持：ordinary同时保方向与small footprint/jointAD，directHRZ真实parent/terminal/local倍率，sticky全未闭分支及ordinary桥，同一full方向低维counter。R38/R80/17/4已付内部链不伪列缺口，旧冻结也不由新标题解冻。

## 10. 停止与审查要求

停止本次共同null-map或独立label-lift＋单次scalar extension/Hölder接法，不续τ/q/k/p数值、共纤维公设或低维toy。该费用证书属于旧线性代数和具名extension的实际应用，不新注册ID；保守no-newordinary/fullbranch-saving streak11，不由源归档清零。最终macro/next保完整Goal且当前无qualified新gain，不complete/blocked。

任何有限认可限于明确量词与此两种桥。A/B正式独审必须分别读原source接口、root10/A/B/spec/macro/next，核phase、真实marks/端帽、所有N/λ/τ/δ幂与平均闭包及反例原方向，不以本人主稿为自身独审。结轮统一更新并按protocol同commit/fulltree同步。
