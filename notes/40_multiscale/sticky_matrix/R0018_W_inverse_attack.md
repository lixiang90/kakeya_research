# R0018：原 joint 增量的非集中与独立化障碍

2026-10-17，lifting_obstructions。主目标仍为完整原 d5/k=ℓ3矩阵配置的 κ≤ζ；本稿攻击原 W联合逆命题。已读本轮 spec、STATE及恢复协议，不重开R17的Y-only BSG/carry局部路线。

结论：没有满足SM的完整 joint反模型，也没有证明主逆命题。但有两项严格有限事实：同一个原g保半质量后，水平增量 law具有(1+γ)维球Frostman upper；另一个满足实际matrix-time action的constant-density双图模型，否定从相关图直接把两个global marginals独立卷积化。后者明确不满足SM，不能否定主任务。

## 1. 可证伪的有限候选及本稿保留的量词

一个足够强的有限 joint候选可精确写为：固定 slab指数γ>0、矩阵SM质量指数b₀>0及允许范围内的精度指数a>0，是否存在h₀>0，使每个h<h₀及足够小r均不存在以下数据？

- B⊂[−1,1]为r-separated的(r,1,r⁻ʰ)-set；明确使用 normalized upper：每个长度w≥r的区间I满足#(B∩I)/#B≤C r⁻ʰw。
- 有限原差标签空间Λ与概率ν，ψ_s∈R²有固定上界，且对每条仿射直线L及r≤w≤1，ν{ψ_s∈N_wL}≤C r⁻ʰw^γ。标签保原重数。
- A₋、A₊⊂R⁴包含于同一个有界水平图Γ={(x,χ(x))}，x∈R²。原水平样本近满二维，如#A₋≥r^(−2+h)，其原counting概率满足球upper C r⁻ʰw²；各尺度graph cover≤C r⁻ʰw⁻²；#A₊≤r⁻ʰ#A₋。这些是需由原W提取得到的有限输入，不在这里从“graph”二字自动推得。
- F:B→Mat(2,2)有固定范数upper，且对所有实R,U，#{b:||F(b)−bR−U||≤r^a}≤r^(b₀)#B。
- 0≤g(a,b,c,s)≤1，在同一个 A₋×B²×ν product参考计数下总质量至少r^h#A₋(#B)²，所有正权tuples满足

      a+T(b,c,s)∈N_(Cr)A₊,
      T=((c−b)ψ_s, (F(b)−F(c))ψ_s).          (1.1)

候选欲排除这些数据，从而得到矩阵affine concentration违例。它是待检验的有限充分版本；实际source是否已给全部图与权重输入须独立核验，不宣称与完整配置等价。下面第一命题只需B、ν、g三项；第二个模型除SM外满足相应joint图条件，所以只否定一个独立化捷径。

## 2. 同原g的(1+γ)维水平增量 upper

令m=#B、n=#A₋，原总权W≥r^h n m²。取

    0<h<min(1/6,γ/6),
    τ=r^(3h),  σ=r^(3h/γ).

r足够小可依赖h、γ和固定常数。把g限制到

    |c−b|≥τ,  |ψ_s|≥σ,

记所得原权为g₀、总权W₀。时间Frostman给被删短差的原B²概率≤C r⁻ʰτ=C r^(2h)；小向量球包含在宽Cσ的slab中，原ν质量≤C r⁻ʰσ^γ=C r^(2h)。因为g≤1，两个删除合计最多C r^(2h)n m²，而不是某个重置后的conditional比例。因此

    W₀≥W/2.                                  (2.1)

按g₀/W₀定义水平增量v=(c−b)ψ_s的概率law λ。对任意v₀∈R²、r≤w≤1，记L为经过0和v₀的直线；v₀=0时取任意原点直线。事件|v−v₀|≤w迫ψ_s落在宽Cw/τ的L邻域，故可用标签质量至多

    C r⁻ʰ(w/τ)^γ.

若该宽度超过1，用概率≤1得到相同的较弱upper。固定这样的ψ_s，时间差必须在长度≤Cw/|ψ_s|≤Cw/σ的区间中。对每个b用原B的upper，时间对概率至多C r⁻ʰw/σ。所有查询宽度都≥r，因为τ、σ≤1；过大区间同样以概率≤1处理。对原 product参考先验积分、再除W₀≥r^hnm²/2，得到

    λ(B(v₀,w))
      ≤ C r⁻³ʰ τ^(−γ)σ⁻¹ w^(1+γ)
      = C r^(−C_γ h) w^(1+γ),
    C_γ=3+3γ+3/γ.                             (2.2)

这没有把g条件下的time与ψ假设为独立；独立仅用于原 product参考计数，实际g以其已知upper支配并支付了密度成本。F可任意，证明没有使用smoothness、curvature或SM。

本证明实际上不使用r-separation，只使用B概率在长度≥r区间上的上述upper。原source fine times归一化后虽spacing为δ/ρ，若m≥K⁻¹ρ/δ，则对w≥r=ρ有#(B_f∩I)/m≤K w，因为原物理区间长ρw≥ρ²≫δ。于是当K次损失已吸收入r⁻ʰ时，(2.1)–(2.2)可直接用于选中桶的bounded quotient图；不必只为这一估计先把B_f变成r-grid。所保一半是该局部桶的原图权重，不是整个原W族的一半。

全R⁴增量T的law投影为λ，所以其ball upper也满足(2.2)。真正终端差若只与T相差O(r)，固定扩大查询ball后同样成立。若再取0≤g₁≤g₀且总权≥pW₀，其normalized increment law的upper只再乘p⁻¹；不免费改prior。

## 3. 熵结论仅是平均信息，不是公共平面

固定有界support与r-grid量化后，(2.2)给每个cell概率≤C r^(1+γ−C_γh)。因此Shannon及Rényi-2 entropy都至少

    (1+γ−C_γh)log(1/r)−O(1).                (3.1)

再要求h<γ/(2C_γ)，可写为至少(1+γ/2)log(1/r)−O(1)。后续保相对质量p的restriction只损log(1/p)。这是超过一维的原增量信息，仍不推出每个scale/component都有此指数，也不把Hochman逆定理中的公共V_i变成同一个global二维平面。

尤其，(3.1)没有证明独立卷积small growth。原相关输出a+T落入小A₊，并不表示把a、T的两个global marginals独立后仍有同样小的entropy。下一节在实际matrix-time作用式内给严格反例。

## 4. 实际matrix-time双图模型：相关与独立卷积不同

先取dyadic r趋0。令X₀=[−2,−1]²∩rZ²、X₁=[1,2]²∩rZ²，L₀=0、L₁=I₂，

    A_i={(x,L_i x):x∈X_i}, A₋=A₀∪A₁.

A₊在固定扩大的水平boxes[-9/4,−3/4]²、[3/4,9/4]²上取相同两graph。两个水平域不交；可视为同一个bounded χ的图。它们全尺度cover≤Cw⁻²，input水平Frostman≤Cw²，#A₋≈r⁻²且#A₊≤C#A₋。不存在clipped ADlower假设。

取B₀=[−1,−1/2]∩rZ、B₁=[1/2,1]∩rZ，B=B₀∪B₁，设F(b)=−bL_i于B_i。F有界、B近满一维。先取H=[0,1]²∩rZ²，标签为原uniform H×H对，ψ=φ−φ′。这是AD维数2的H，差law有固定常数line-cap指数1（从而任意γ≤1）；并非把distinct差改成uniform。

定义原权g为下列事件的indicator：a∈A_i且b,c∈B_i，并且

    c−b∈[1/16,1/8].

其product参考密度有一个不依赖r的正lower，故对任意固定h>0及充分小r都≥r^h。对正权tuple，真实(1.1)为

    T=(v,L_i v), v=(c−b)ψ,
    a+T=(x+v,L_i(x+v)).                     (4.1)

|v|∞≤1/8，输出距实际A₊至多Cr（仅因rounding到r-grid）。共同B、同一prior、同一个g及same graph全部保留。

归一化g的a-marginal为μ=(μ₀+μ₁)/2，各μ_i为A_i的uniform law；T-marginal为λ_T=(λ₀+λ₁)/2，其中λ_i由同一个二维v-law通过v→(v,L_i v)得到。v有r-cell upper Cr²，因为时间差bounded away from0、H×H差law有r-cell upper Cr²；因此H_r(v)=2log(1/r)+O(1)。

独立μ_i*λ_i位于二维plane，entropy为2log(1/r)+O(1)。i≠j时，从独立(x,v)到和的映射

    (x,v)→(x+v,L_i x+L_j v)

可逆，det(L_j−L_i)=±1。因此cross entropy为4log(1/r)+O(1)。有限mixture的entropy与各component平均相差≤log4，故

    H_r(μ*λ_T)=3log(1/r)+O(1),
    H_r(μ)=2log(1/r)+O(1).                  (4.2)

实际相关输出仍只用两个二维graphs。于是即使原g为constant-density，也不能从它推出这两个global marginals的独立卷积defect为O(h)log(1/r)。必须先合法选择匹配的worlds或作保原权BSG，不能直接独立化。

本实例H维数2，与固定κ<2的source prior不符；更关键是F在每个半时间集上恰affine，明显违反SM。它不是本稿§1的反例，更不是source/Kakeya反例。

## 5. 相同捷径反例也可保固定κ=1/2先验

若只要否定独立化捷径，并非要求(4.2)的精确系数3，可取R17固定base的Cantor H_n，AD维数1/2、slab指数γ=1/4，仍用其原uniform H_n×H_n差prior。固定足够小σ₀>0，使ν{|ψ|≥σ₀}有不依赖depth的正lower；例如取两端第一位digits相隔的子集即可。把这个额外事件放入原g，仍保固定正density，并对两个worlds完全相同。

时间差与向量norm都bounded away from0后，§2证明不再有r幂截断成本，直接给v-law的ballupper Cw^(1+γ)，常数只依已固定base与σ₀。因此H_r(v)≥(1+γ)log(1/r)−O(1)。self convolution仍有二维entropy，cross convolution的可逆map给至少(3+γ)log(1/r)−O(1)。

self分支的二维lower来自uniform full二维端点：对每个固定v，sum的r-cell质量≤Cr²；bounded平面support又给二维upper。这里不要求Cantor增量本身具有二维entropy。因此

    H_r(μ*λ_T)−H_r(μ)
       ≥ ((1+γ)/2)log(1/r)−O(1).           (5.1)

κ=1/2、γ=1/4时lower系数为5/8。这里只换prior，A仍full二维horizontal graph；所有constant-density与cover条件保留，F仍违反SM。固定base后r取其任意深度，故这不是只在某个h之外出现的损失。

## 6. 主逆命题的未闭合部分

新球upper(2.2)保实际同g质量；模型(4)–(5)严格排除global marginal独立化的直接推论。两者都没有给SM下的完整countermodel或共同plane mass theorem。

Hochman的逆定理若要调用，仍须先从原相关图得到适当独立卷积或其合法受限版本，并保support界、参数顺序、共用subspace的真正结论。再从组件的平均信息恢复F的matrix affine fit也未完成。不能把(3.1)自动改成每个component的二维saturation或整个A的global flatness。

本稿没有添加C²、irreducibility或clipped ADlower，不回到R17carry toy。完整原W extraction是否给上述bounded g及共同graph由另一source审查负责；没有原输入便不能宣称源主命题已被严格收缩或否定。下一行动服从本轮macro与实际新估计，长期Goal仍active。
