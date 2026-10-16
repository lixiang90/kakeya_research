# R0027：保多尺度visible graph与非平面law仍不足固定加法增长

2026-10-17，root。此为**弱化接口**的严格counterexample，不是矩阵时间作用、source配置或Kakeya反例。目的是阻止把本轮已付D-plane gate误当一般加法flattening定理。独立构造/核查见R0027_matrix_observed_counterattack.md。

## 1. 全部量词

任意η>0、固定0<ε<1，选择足够大的固定B=2^L，再取任意足够大偶数N，r=B⁻N。构造A⊂[0,2]^4、平移概率λ及0≤g≤1，使：

- r-separated cardinal K⁻¹r⁻²≤#A≤K r⁻²，K≤r⁻η；UniformA为(r,2,K)Frostman。
- 每个dyadic R∈[r,1]、每visible x∈R²的R-cell Q，N_R(A∩{x∈Q})≤K；包括原base与全部较粗尺度。
- λ在有界R⁴，对所有affine hyperplanes V（从而所有affine2planes）及q∈[r,1]，λ(N_qV)≤C_B q^(1/2)。在q=r^ε处，N大后≤r^(ε/3)，是独立η的fixed正幂。
- product-reference UniformA×λ上的g density≥r^η，且g支持a+d∈A，输出card没有增长。

这与D原先有的2plane nonfit相比甚至更强，但λ不声称有原D=((t−s)ψ,−∆Mψ)分解。禁止以此反驳wholematrixAFF₃/source。

## 2. 二进制block mask：真实实数定义

令

    X={Σ_(i=1)^N d_i B⁻i: d_i∈{0,...,B−1}}，
    f(x)=Σ_(i odd) d_i B⁻i，
    A₀={(x₁,x₂,f(x₁),f(x₂)):x₁,x₂∈X}。

每x取长度LN的终止二进制展开，f保留奇数blocks中的bits、把偶数blocks清零，不用有歧义的无限展开。#A₀=B^(2N)=r⁻²，x-grid使A₀ r-separated。共用任意dyadic prefix的x，共用同长度prefix的f(x)，因为逐bit mask不产生carry。因此每visible dyadic R-square的A₀落一个joint R-cube；不局限于B-adic尺度。UniformA₀的ball质量≤C R²，由水平fullgrid直接得到。

## 3. λ=UniformA₀的统一hyperplane cap

对unit normal n=(α₁,α₂,β₁,β₂)，

    n·a=Σ_j [Σ_(i odd)(α_j+β_j)d_(j,i)B⁻i
                   +Σ_(i even)α_j d_(j,i)B⁻i]。

四个系数 α₁,α₂,α₁+β₁,α₂+β₂ 中至少一个绝对值≥c>0，否则n非unit。condition其余三组独立digits，只留该一组（同一坐标的奇或偶blocks）。这组是有限base-B²、每level有B个digits的Cantor变量，维数1/2，且

    Pr{Z∈I}≤C_B |I|^(1/2)， |I|≥r。              (1)

可直接按first differing block/相邻basic intervals计数：(B^-2k)尺度每basic interval质量B^-k；任意q位于两个相邻scale之间只损固定C_B。N偶，末奇组最细spacing为Br、末偶组为r，原子质量均r^(1/2)，故q=r端点也合法。整体coefficient≥c仅改常数，对任意slab中心成立。于是λ(N_qV)≤C_B q^(1/2)。无需对无限normal族概率union。

## 4. 真正实数加法、小增长与carry完整保留

令S=A₀+A₀，A=A₀∪S，λ=UniformA₀。每个坐标pair的实数和可精确表示成

    (Σ e_i B⁻i, Σ_(i odd)e_i B⁻i)， e_i∈{0,...,2B−2}。

这是原两个数字和的真实等式，没有假设raw e_i已经是canonical digits，也未漏掉进位。用于upper只需所有raw sequences的数目，故

    #S≤(2B−1)^(2N)，
    #A≤2r⁻² r^(−θ_B)， θ_B=2log_B(2−1/B)→0。    (2)

定义g(a,d)=1_{a∈A₀}。对UniformA×λ，mean(g)=#A₀/#A≥r^θ_B/2，且a+d∈S⊂A，所以是同一carrier上的exact small-image relation。角/time没有被隐含假定；这是一个一般加法law例子。

## 5. 和集A也保全部多尺度visible fibres

不能只核A₀后给S免费graph属性。对一个坐标pair的raw sums e_i，真实base-B normalization的carry只能在{0,1}；给定完整carry vector和x和的canonical digits，raw digits唯一，由

    e_i=a_i+B k_(i−1)−k_i

恢复（首位integer carry单列，索引方向约定固定）。于是对应y和等于f(x_mod1)加一个仅依carry vector的常数。换言之S在一个坐标上包含于至多C2^N条**translated digit-mask graphs**；两坐标合计≤C4^N条。integer部分及边界只多固定倍。

每一translated mask graph对任意dyadic horizontal R-cell只有O(1)个joint R-cells：整数平移不会改prefix，vertical固定平移最多多相邻格。故

    N_R(A∩{x∈Q_R})≤C4^N=C r^(−log_B4)。          (3)

估计一般ball B_R中的fine质量时还需base fibre，不能只从R-cover推fine计数。用(3)在R=r时每个visible r-cell中≤C4^N个points，而ball水平grid有≤C(R/r)²个cells，因此

    #(A∩B_R)≤C4^N(R/r)²，
    UniformA(B_R)≤C4^N R²，                       (4)

因为#A≥r⁻²。不以coarse coverupper直接冒充fine massupper；(4)明确使用base fibre。

选择B使max(θ_B,log_B4)<η/4，再令N大吸收固定C/C_B、2与r^η余量，(2)–(4)全在K≤r⁻η内，mean(g)≥r^η。hyperplane cap (1)在q=r^ε处≤r^(ε/3)，与η可任意更小兼容。

## 6. 所否定的步骤及不能推出的结论

严格否定：任意小loss的visible multiscalegraph/coherence、2Frostman、card≈r⁻²、原平移law的全2plane nonfit，就必然给只依fixed nonfit指数的>2 additive-growth。这些条件全部可在本模型同时成立。实数进位已经逐项包含，未使用digit derivative或Leibniz规则；与R17非法real multiplication跳步不同。

没有否定：λ具有真实matrix-time/角差分解、原jointtube AD/CW/两grain一致性时的AFF₃或维数结论。本模型不提供ν、M、Φ，也不验证κAD的原角law或真实W witnesses。下一任务必须保这些丢失对象，不能只再强化一般additive-law的planecap后重复同一弱接口。

无真实Kakeya反例或重大性/新颖性认证；这是保原目标、防止错误generic flattening的一项可复核边界。
