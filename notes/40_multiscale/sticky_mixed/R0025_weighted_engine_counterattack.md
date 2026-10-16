# R0025：保原图与全部二次 nonfit 的时间代表抽样

2026-10-17，`lifting_obstructions`。已读R25 working spec、R24 next weighted-engine target、STATE、恢复协议和root的本轮指派。本文件只研究原fine time到合法separated set的操作，不重复QSC插值常数，不把scalar22.5整段作为新的四维配置调用。

**结论：没有找到保全部finite输入的反例；证明了所需分层代表选择的一项严格版本。** 它同时保一个给定bounded graph的密度，以及**所有实系数**的coefficient-weighted quadratic nonfit，且同一个原index提供time/F/G。精细时间标签数可以任意大，概率费用只依赖working time-cell数。抽样后的先验是带**原格权重**的显式新先验，不是旧fine原子质量的自动继承。后者有严格反例，见第7节。完整scalar曲率引擎仍须root/A接通其余named输入。

## 1. 有限设置和量化选择命题

Ω为有限原标签空间，ν为原概率。每个标签带 `t∈[-1,1]`、同一原标量值对 `(F,G)`，允许同位置不同标签。设working w∈(0,1)，对所有长度r≥w的interval I，

    ν{t∈I}≤K_t r,    K_t≥1。                              (1)

对任意实quadratic `P(t)=p₀+p₁t+p₂t²`，令 `A(P)=1+|p₁|+|p₂|`，假设

    ν(E_P)≤a,
    E_P={|F−P(t)|≤h A(P)}。                               (2)

设有限A₋带原概率µ（实际可为Uniform A₋），原图满足

    0≤g(x,i,j)≤1,
    ∫g dµdν²≥m>0,
    g>0 ⇒ dist(x+S(t_i,t_j),A₊)≤C₀w,
    S(t,s)=(s−t)[F(t)−F(s)−G(s)(t−s)]。                    (3)

将[-1,1]按长度w的半开cells分箱，n为正质量cells数，p_j为其原质量；端点只付固定常数。由(1)，

    n≤C/w,    p_*=max p_j≤C K_tw,
    V=Σp_j²≤p_*。                                         (4)

各cell独立按原conditional ν抽一个标签 `I_j`。重要的是一起抽取

    (T_j,F_j,G_j)=(t(I_j),F(I_j),G(I_j))，
    ν̂=Σ_j p_j δ_(I_j)。

**命题1。** 若 `V≤m/4`、`u²≥2V`，则存在同时满足

    ∫g dµdν̂²≥m/2,
    sup_P ν̂(E_P)≤a+u                                    (5)

的抽样，前提

    exp(−c m²/V)+C(n+1)³ exp(−c u²/V)<1。                 (6)

常数绝对；不依赖原fine标签总数，不预先限制p₀,p₁,p₂，也不假设cell内F/G近常。式(3)在所抽实际indices上原样成立，未拼接两个不同标签的F和G。

## 2. 一个给定原图的密度：diagonal和有界差分

令 `Z=∫g dµdν̂²`。不同cells的代表独立，故off-diagonal terms的期望等于原cell-product积分；同cell两time使用同一代表，不能误称仍独立。那部分原总质量≤V，所以

    E Z≥m−V≥3m/4。

更改单个I_j至多影响两个time坐标，Z的变化≤2p_j。因此独立bounded-difference估计给

    Pr{Z<m/2}≤exp(−c m²/V)。                              (7)

该估计可以由逐cell Doob martingale与Hoeffding指数界直接得到；只用原g≤1。一个给定g的mean就够，不需控制任意graph类。

## 3. 全部weighted quadratic fits：不依赖#fine的分类数

这里不能对原fine标签的所有subsets作union，也不能未经证明把p系数限制到一个小网。采用三实参数的有限arrangement。

给任意N个观察点 `(t_i,F_i)`，在p₁、p₂的四种sign orthants中，`h(1+|p₁|+|p₂|)`是参数的affine函数。每个membership `|F_i−p₀−p₁t_i−p₂t_i²|≤h A(P)`由两个参数空间R³中的affine inequalities判定。包含orthant边界和所有lower-dimensional faces，O(N)个planes的arrangement只有 `C(N+1)³` 种membership patterns。因此

    growth_function_(E_P)(N)≤C(N+1)³。                    (8)

这对所有实coefficients和任意粗糙F成立；不要求F(t)单值延拓。有限Ω使所有events可测，可从有限distinct subsets中作deterministic tie选择。

给原抽样再配一个独立同分布的逐cell ghost抽样I_j'，记ν̂'。若某P满足ν̂(E_P)>a+u，ghost的mean为ν(E_P)≤a、variance≤V/4。Chebyshev在u²≥2V时给

    Pr{ν̂'(E_P)≤a+u/2}≥1/2。

选一个见证bad P后对此conditional ghost积分，得到bad概率至多

    2Pr{存在P: ν̂(E_P)−ν̂'(E_P)>u/2}。

每个pair `(I_j,I_j')`可独立随机交换，联合分布不变。固定2n个样本后，(8)给至多C(n+1)³个patterns；对每个pattern，差是独立Rademacher和，j项幅度≤p_j，故Hoeffding给tail `exp(−c u²/V)`。union得到

    Pr{sup_P ν̂(E_P)>a+u}
                ≤C(n+1)³ exp(−c u²/V)。                   (9)

(7)+(9)即证命题1。该同时控制不是为每个P分别选代表：所有P使用**同一个**抽样与同一组F/G。

## 4. small-power输入中的阈值检查

若K_t≤w⁻η、m≥w^η、a=w^ε₂，取u=a，则

    m²/V≥c w^(3η−1),
    u²/V≥c w^(2ε₂+η−1)。                                 (10)

所以η<1/3且2ε₂+η<1时，两概率以负幂指数衰减，胜过(n+1)³≤Cw⁻³；(6)对w小成立。V≤m/4和u²≥2V也随之成立。若各loss有不同固定次数，替换为相应O(η)即可，不能直接当常数。

ε₂阈值不会免费添加到非空bounded信号输入：若|F|≤M固定、h=w^ε₁，则constant h-fits可用O(M/h)个区间覆盖值域，故(2)迫 `a≥c_M h`。ε₂>ε₁时，w足够小原输入已经矛盾。余下ε₂≤ε₁，而原scalar引擎本就先取ε₁充分小，故可以支付2ε₂+O(η)<1。这不是缩小固定κ。

## 5. 原格权重到uniform set：必须删轻格并计费用

选(5)的同一抽样后，删 `p_j<τw` 的time cells。其原格总质量q≤Cτ；若q≤m/16，两个time坐标所能损失的g mass≤2q。归一化剩余权为ν̂_H，得

    mean_(µ×ν̂_H²)g≥m/4,
    ν̂_H(E_P)≤2(a+u)。                                    (11)

每个heavy cell仍只有一个实际原标签，N为其数，

    c/(K_tw)≤N≤C/w,
    τw≤p_j^H≤C K_tw。

因此ν̂_H对Uniform(B_H)的density在 `cτ/K_t` 与 `C K_t` 之间。保同一个g和所有P，有

    mean_(µ×Uniform(B_H)²)g≥c m/K_t²,
    Uniform(B_H)(E_P)≤C K_t(a+u)/τ。                       (12)

这明确支付了uniformization，不把one-rep的原cell权重免费改成均匀原子。对长r≥w的interval，B_H每cell至多一个代表、N有lower，故其uniform cap≤C K_t r。

例如τ=w^{Lη}，L固定充分大可令删格损失≪m；再取η≪ε₂/L，(12)仍给正幂quadratic nonfit，graph mean为w^{O(η)}。所有阈值须先于最后w→0固定。

## 6. separation与rounding：weighted精度正好支付未知coefficients

相邻time cells的实际代表可能任意接近，不能直接叫w-separated。不能只选一个time-bin颜色：g可集中在cross-color pairs，而同色graph全空。

令q_j为其原cell centre，把clock改为q_j，但保留同一原F_j、G_j及(12)的uniform graph。clock q_j是w-separated。若新clock上的weighted fit误差≤`(h/2)A(P)`，则

    |P(T_j)−P(q_j)|≤Cw A(P)。

当Cw≤h/2时，该fit对应原抽样clock上的h A(P)-fit，所以仍由(12)控制。无需给p系数bound、F/G的cell-Lip或不同sample representatives。

若|F|,|G|≤M，则S的time prefactors是低次多项式，直接相减给

    |S_original(T_i,T_j)−S_rounded(q_i,q_j)|≤C M w。         (13)

所以g的近输出关系变成A₊的 `C(C₀+M)w` 邻域。M固定时，只改working constant；M为small-power K时，**不能**把它写成absolute O(w)。可在scale/cover预算中另付该K，或取更细time bins并重计cap、A₊邻域cover与最终resolution。本文保留(13)，没有隐去实际幅度。

h=w^ε₁、0<ε₁<1时，Cw≪h；若named输入坚持纯幂精度，可用w^{2ε₁}≤h/2，而非免费声称精度常数完全不变。所有集合仍bounded，固定端点缩放只付常数。

## 7. cycle/K_(4,2)质量与旧原子先验的严格边界

prepared Uniform(B_H)上的g若mean=d₀，则令 `H={(t,s):E_µg≥d₀/2}`，其edge probability≥d₀/2。weighted CS给完整H四环质量≥(d₀/2)⁴，K_(4,2)六time pattern质量≥(d₀/2)⁸。四环公式是对codegree平方积分；K_(4,2)公式是对同一codegree四次方积分，再用Jensen。均为同一个prepared carrier，未从不同F/G先验拼接。

这些是经过明确sampling、heavy-cell、uniformization后得到的概率，不是原fine ν的原子质量自动保留。严格边界：令原ν均匀分布在N个fine time points，约n=1/w个working cells各有同样许多points。每格取一个代表后，所选点在旧ν下总质量为n/N，N可任意大；旧ν⁴和ν⁶在全部所选points上的质量至多(n/N)⁴与(n/N)⁶，可比任何固定小幂都小。

这否定“代表集合在旧atomic prior下仍dense”的捷径，并不否定命题1或目标engine：命题1显式证明一个新weighted sampling prior满足全部所需输入，有限set engine可在这个已验证模型上运行。不能把这种证明性选择表述成原measure的无损restriction。

此外，dense H的CS本身不提供 `A'+Q(C₄)` 的small-image upper。后者需原S重数层、scalar BSG13.7、输出/input比和rounding的真实步骤；任意按g平均取得的H不能自动冒充BSG的H。source radial/Kaufman要求的uniformity、slab及almost-all参数也未由本段CS证明。

## 8. 对本轮主目标的意义与停止范围

此处已付的门槛是：无论fine标签数多大、F/G在cell内如何粗糙，都可用同一组实际F/G代表，保一个给定g及所有weighted quadratic nonfits，随后合法变成separated uniform time set。原细time到working time不能免费粗化的问题因此有一个定量解决方案；loss阈值、cell权重、clock误差和cycle reference均明确。

未构造保全部A-budget/nonquad/g等条件的目标反例；也未单凭sampling就证明scalar曲率nonexpansion engine。后者还需root/A逐项接source的scalar BSG、R³ radial22.2、Kaufman22.3及输出cover矛盾。actual mixed43应用仍条件于whole-matrix AFF和middle vectorτ，不处理largeτ稳定、其它五维配置或Hausdorff。没有新Kakeya维数界、真实Kakeya反例或重大性认证。
