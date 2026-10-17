# R0028：原 factorized action 的平均进位门槛

2026-10-17，`lifting_obstructions`。已读 R28 spec、R27 next/current STATE 及 R17/R18 的冻结边界。唯一 main 仍 actual ell3 AFF₃。原 finite 输入要保共同 time ν、同一 Mat2 函数 M、原 H 的κ-cover/Frostman-upper/slabγ及同一个 bounded correlated g；κAD lower未证明且本稿未使用。真实作用为

    D(t,s,ψ)=((t−s)ψ, −[M(t)−M(s)]ψ)。

**本稿没有完整 factorized 反模型，也没有证明 AFF₃。新严格信息是原参考质量下的乘法进位下界：对任意固定坐标，原 time-gap与原 angle差相乘，只有 o(N) 个 raw overflow 的 tuples 至多占固定正幂质量。** 因此 R27 数字加法模型不能通过“无进位/极少进位的真实乘法”以任意小损升级。允许大量真实carry和多值修正的模型仍未排除；不能把下述门槛说成整个有限主命题已证。

## 1. 全部有限量词与仍保留的原先验

令 ν 为 [-1,1] 上有限原time概率；允许重复labels，且每个长度 ℓ≥d 的 interval I 都满足

    ν(I)≤K_t ℓ。

令 ψ:Λ→[-1,1]² 为原角标签差，π₀为有限原标签概率，π=ψ_*π₀。重复ψ保原权重。假设对所有 unit n、所有实c及 `q_base≤q≤1`，

    π{|n·ψ−c|≤q}≤K_ψ q^γ， 0<γ≤1。               (1)

实际可取 Λ=H²、π₀=Uniform(H)²、ψ=φ₂−φ₁。以下只需原slab upper；原H另有κ-cover及Frostman upper，不能据此声称κAD lower已付。本稿不要求π有独立digits。若 ψ 的固定bound大于1，只增加下述 mod1 folding的固定次数。

固定整数B≥3、偶数N，定义

    r=B^(−N)， n=N/2， q=B^(−n)=sqrt(r)，
    d≤r， q_base≤q。

B将依固定γ选得足够大，此后固定，N可任意大。取实际原变量

    X=frac(|t−s|)， Y=frac(|ψ_j|)， j∈{1,2}固定，

其前N位标准非负base-B digits为 `d_i,c_i∈{0,...,B−1}`。整数端点采用终止展开，frac取[0,1)，反射/折叠涉及有限多个interval，见下一节。j预先固定，不按tuple挑一个有利坐标。

定义前n个对角项的overflow数

    Z_N= #{1≤i≤n: d_i c_i≥B}。                       (2)

两个N位截断的真实实数乘积raw coefficient为

    a_k=Σ_(u+v=k)d_u c_v。

所以 `a_(2i)≥d_i c_i`。Z_N个不同even positions必有raw coefficient≥B；标准非负carry归一时，来自更低位的incoming carry非负，因此每一个这类位置都必须向上进位。若再包含非负整数部分，其附加coefficients也只增加raw coefficient。

这不是把真实乘法改成digitwise group：a_k是实际实数截断乘积的精确未归一表达。本稿只利用**必要的overflow事件**作upper，不假定没有overflow就足以避免从更细位传来的carry。

## 2. 原时间不是独立digits：用合法density domination

对任意固定s，X的一个长度r的aligned prefix-cell之原像，是有限多个长度r的t-intervals：绝对值给至多两支，|t−s|∈[0,2]的frac再给有限支。由 d≤r，合法time upper给

    Pr_(ν²){(d₁,...,d_N)=u}≤C K_t B^(−N)            (3)

对全部N位words u一致。故实际time-gap的digit law被 `C K_t×Uniform({0,...,B−1}^N)` 支配。下面用uniform digits计算乘积概率，只是这个已证domination的upper，不是给原ν新增独立性。

同理，Y的前n位prefix v 对应 |ψ_j|的一个长度q interval，再由abs/frac拆成有限多个原坐标interval。取unit normal e_j调用原slab (1)，查询q≥q_base合法，得

    Pr_π{(c₁,...,c_n)=v}≤C K_ψ B^(−γn)。            (4)

ψ_j恰为整数时仍落在这些interval的端点中，(4)处理该原子，无须删除或伪造连续law。这里同样没有假设角digits独立。

## 3. 完全无进位策略的平均质量upper

对一个固定angle digit c，令

    w_B(0)=1， w_B(c)=min(1,2/c)  (1≤c≤B−1)，
    L_B=Σ_(c=0)^(B−1)w_B(c)≤C log(2B)。

uniform time digit d 中满足 dc<B的比例为

    [floor((B−1)/c)+1]/B≤w_B(c)  (c≥1)。

因此固定angle prefix，(3)给 `Pr{Z_N=0 | prefix}≤C K_t ∏_(i≤n)w_B(c_i)`。在原产品reference ν²×π上用 (4)求和，严格有

    Pr{Z_N=0}
       ≤C K_t K_ψ B^(−γn) L_B^n。                  (5)

选择固定 `B≥B₀(γ)` 使 `log_B L_B≤γ/2`，便得

    Pr{Z_N=0}≤C K_t K_ψ r^(γ/4)。                  (6)

任何要求两个真实非负digit乘积在前N位完全没有raw overflow的形式实现，必属于 Z_N=0。因此 (6)是原平均质量上界，不是 R17 单tuple carry反例。B增大只使 `log_B L_B` 更小，不能把右侧的fixed正指数退成R27加法模型中趋于0的 `log_B 2`。

## 4. 强化：少于固定比例overflow仍只有固定正幂质量

对 `0≤θ≤1`，若 Z_N≤θn，至少n−floor(θn)个位置满足 `d_i c_i<B`。对可能例外集S作union，并按 (3)–(4)支配，得完整finite bound

    Pr{Z_N≤θn}
      ≤C K_t K_ψ B^(−γn)
           Σ_(k=0)^floor(θn) binom(n,k) B^k L_B^(n−k)
      ≤C K_t K_ψ [2 B^θ L_B / B^γ]^n。             (7)

第一式中，S内的angle digits自由求和至多B^k，其余digits的加权和恰为L_B^(n−k)。这一步允许所有angle correlations；只用每个prefix的原质量upper，不使用product Cantor假设。

固定 `θ=γ/4`，再选固定B使 `log_B(2L_B)≤γ/4`，则

    Pr{Z_N≤γN/8}≤C K_t K_ψ r^(γ/4)。              (8)

floor不改变式子：事件左端即整数Z_N≤floor(γN/8)。其外有严格多于γN/8个不同even raw positions需要向上进位。这是实际乘法所需carry数量的必要下界，不仅说至少某一个tuple存在某一次carry。

## 5. 原bounded g的相关性与真实graph质量

令 µ_A 为任意observed labels概率，并保原reference

    µ_A×ν²×π₀， 0≤g≤1， m_g=∫g。

π₀可以是原Uniform(H)²，g可与a,t,s及全部原角labels任意相关。由 (8)只对原reference事件计费，

    ∫g 1_(Z_N≤γN/8)≤C K_t K_ψ r^(γ/4)，
    Pr_g{Z_N≤γN/8}≤C K_t K_ψ r^(γ/4)/m_g。        (9)

没有给g条件下的ψ边际虚构slabcap。特别若 `K_t,K_ψ≤r^(−η)`、`m_g≥r^η` 且 `η<γ/12`，则低overflow部分占g的比例至多 `C r^(γ/4−3η)=o(1)`。不只“全g不能无进位”，而是g的绝大多数质量必须允许上述正比例真实overflows。

实际source的各K固定幂及mean下界可分别记为 `r^(−C_tη_src)`、`r^(−C_ψη_src)`、`r^(C_gη_src)`；只需最后取 `(C_t+C_ψ+C_g)η_src<γ/4`，并保严格常数余量。ρ与r转换、allowed格费用由既有K支付；不能直接把δ小幂当无损常数。

在本轮实际observable接口，fine time base `d=δ/ρ≪r≈K₀ρ`，原angle cap base `Cρ≪sqrt(r)`，故 (3)–(4)确在允许范围。若r并非B的偶次幂，可取最近偶N，使r仅变B²的固定倍；B已先固定，fine/base查询和指数有同样余量。原H的κ-cover/Frostman upper、M的fixed matrix nonfit及observed A约束仍保留，但本证明尚未使用它们来迫image增长；不假设未证明的κAD lower。

## 6. 对数字factorization与factorized主命题的准确责任

R27 mask可形式地写：只让angle使用even blocks时，若真实乘法无carry，odd-block projection与该乘法相容。R27真实加法的代价是每位有限carry patterns，指数可随base增大变小；不能据此声称真实乘法也有任意小损。式 (8)–(9)严格排除**原slab prior下完全无进位或o(N) raw-overflow的实现策略**，包括将其隐藏在原g删选中。

但是实际factorized反模型可以允许carry、增加合法输出fibres，或利用carry修正之间的相关性。正比例overflow **不等于**指数多个不同修正值：它们可能产生相同mask修正或被其它项抵消。本文没有从carry数量推得修正熵、输出card、all-scale fibre预算或whole-matrix affine fit。也未将standard非负digits的论证无证明扩展到任意balanced signed-digit算法。

特别，本文没有证明任何满足真实作用的g必须落在Z_N很小的事件。相反，(9)说明一个完整成功模型若存在，必须承担大量carry。故它不是factorized有限命题的完整反例或正向证明，更不是source/Kakeya反例。M(t)可任意；把M、A或原角的额外作用一致性接入carry-correction预算仍未完成。

## 7. 共同clock/angle与停止边界

式 (9)保共同原ν与原H²差prior，可直接核查一个no-carry提取是否支付原质量。它不允许先为每个time pair或A点挑一个低carry角、再把这些不同choices叫同一个angle作用；这些choices的原总质量已经由 (9)限制。同样，先固定一条ψ再给每个clock换不同time子集，不能免费继承原产品reference的densegraph。

未找到满足全部matrix-time/原角cover与upper/slab/observedgraph/nonfit量词的strict finite反模型。若root的原action提取仍未付新的共同clock/多角质量，必须按本轮macro停止局部迭代；不能将 (8)改名为vector sum-product或generic entropy inverse后声称AFF₃已付。本稿不另加C²、irreducibility或统计假设。

本轮严格信息是有真实原质量的平均carry门槛。实际AFF₃、>2增长、完整mixed43与一般五维仍未解决；无新维数界、真实Kakeya反例或重大/新颖性认证。长期Goal active。
