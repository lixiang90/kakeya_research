# R0031：原Corollary3.4的完整代数图匹配重证

2026-10-17，root。对象OAI4原Cor3.4（PDF35–36）；使用原Lemma3.1及bounded-degree closure、已内部独审重证TCM001（原Lemma3.3）。**不调用Lemma3.2**；该continuation输入独立服务后续terminal extension。A稿R0031_algebraic_norm_audit展开3.1，B稿R0031_continuation_and_slice_audit分别展开3.2及slice。来源原工具结果，非新的高维Kakeya定理或重大结果。

## 1. 量词与固定几何

固定base维度n、代数总次数D、实comparison ball B及同一个固定complex holomorphic域Ω（ball或polydisc），B有非空实内部。incident basepoint域Q在固定compact K⊂⊂Ω∩R^n，B/Q均有固定holomorphic margins；原comparison domain Q=B是直接特例。B和Q在这个同一connected Ω内，后文finite boxes只是其内部的cover，不引入不连通的额外domain。所有函数real-on-real、在整个Ω holomorphic；函数的关系式可有任意大小/任意小的非零系数，不设height lower。

给d₀<1，可将其增大到max(d₀,0)，故以下设0≤d₀<1。欲证存在ε_*>0及R₀，使任意M,Δ>0、R=M/Δ≥R₀、0<ε≤ε_*、d≤d₀不能同时满足：

1. 两indexed lists各card≤R^(d+ε)，每member距同一个代数reference sheet在B上的sup norm≤MR^ε。
2. 有subprobability μ(i,j,z)，total mass q≥R^-ε，每color index-base marginal≤R^ε πκ,i dz，各Σ_iπκ,i=1；π可极不均匀或有零项，indices/time可相关。
3. μ-a.e. event上，|f₁,i(z)−f₂,j(z)|≤ΔR^ε，且||f₁,i−f₂,j||_B≥MR^-ε。

全部常数只依固定geometry/n/D/d₀，独立于M/Δ、π最小正权、lists及系数height。μ-a.e.不满足条件的零质量部分可删。

## 2. 有界次数闭包与norm/jet输入

若u/v各满足非零total-degree≤D关系，先取在其analytic graph上恒零的一个irreducible因子。该因子必含W：不含W的非零base polynomial不能在Ω的开集恒零。设关系为P(z,W)、Q(z,W)，则

    Res_W(P(z,W),Q(z,W−T))

是u−v的非零polynomial relation。对generic z以两collections的roots乘积表达即可见其作为T polynomial不恒零；Sylvester determinant的size≤2D、entry degree≤D，故total degree≤2D²。base leading coefficients只在proper algebraic subset为零，关系在其补集成立后由holomorphic identity延至全域。除以任意M>0仅替T为MT，不增degree。故可统一取D′=max(1,2D²)，不需要coefficients的定量下界。

把K预先扩大到包含§4全部固定cover boxes的闭包，仍有K⊂⊂Ω；这项选择只用原fixed margin，不依R或事件分布。Lemma3.1的齐次形式给任意此类holomorphic h、任意固定q：

    max_(|α|≤q)||∂^α h||_K ≤ C_q ||h||_B，
    max_(|α|≤D′)|∂^α h(z)| ≥ c ||h||_B，z∈K。  (1)

这里h≡0单独平凡处理。A稿给完整normal-family/finitejet/sublevel论证：coefficient vector归一极限不得W-independent；在limiting leading coefficient非零处由root-free大圆、chosen branch连续性控制escaping roots，再用复线disk max principle跨其零集。holomorphic compact limit在B保持norm1；约去W幂后constant coefficient非零，vanishing order≤D′，连同Cauchy及points compactness给(1)。此处不假代数函数的所有branches都bounded，也不要求chosen sheet有irreducible smooth relation。

Cor3.4只需(1)与differences degree closure，Remez和3.2不是其额外输入。它们的源审查责任与(1)分开标明。

## 3. 减真实member及每个event的directional jet

q>0使两lists非空。选其中一个真实member f_*，设hκ,i=(fκ,i−f_*)/M。由共同reference三角不等式，||hκ,i||_B≤2R^ε。所有h degree≤D′，由(1)给通过任意固定阶q的derivative upper C_q R^ε；零h不例外。

对每个incident pair，g_ij=h₁,i−h₂,j=(f₁,i−f₂,j)/M本身也是两原degree≤D sheets之差，degree仍≤D′，不必反复扩大degree。因此

    ||g_ij||_B≥R^-ε， |g_ij(z)|≤R^(-1+ε)，
    max_(|α|≤D′)|∂^α g_ij(z)|≥c R^-ε。         (2)

选ε_*<1/4及固定R₀大后，zeroth-order上界不足以达到(2)，故有某1≤p≤D′的p-th derivative tensor大小≥cR^-ε。在Sym^p(R^n)^*中，diagonal evaluations T(v,…,v)张成对偶；可固定一个有限unit-vector集合V，使对每p≤D′，max_v∈V|∂_v^p g|≥c′max_|α|=p|∂^αg|。函数real-on-real保证这些数均实；V及常数只依n,D′。

以固定顺序把每event分到第一个满足

    |∂_v^p g_ij(z)|≥c₁ R^-ε                  (3)

的(p,v)。这是一组measurable events，finite pigeonhole选择一个class保至少q/L质量；L固定，不依lists或R。

## 4. 固定product box与边界质量

对每个v，固定有限个沿v的product boxes覆盖Q，每盒写成z=x+sv（可含固定offset），x∈X⊂v^⊥、s∈I=[s₀,s₀+ℓ]，X bounded，ℓ>0固定。盒及小complex enlargement均在Ω内，ℓ及margins有fixed下界；Jacobian取orthonormal坐标为1。

**盒可稍伸出原real ball B/Q。** 只需函数在盒上有共同fixed holomorphic margin；把μ在原Q外延为0。若要求有限个fixed boxes全包含于B内部，可能漏掉随R集中于边界collar的事件质量。固定compact complex margin允许上述外伸覆盖，因而没有漏失该质量。

再finite pigeonhole选一个盒及上一节同一个p/v，restrict μ到所选class与盒；新submeasure记ν。其total≥q/C₀≥C₀^-1R^-ε，双marginal仍≤R^ε π_i dz，**此时不归一化**。

## 5. Joint densities的Fubini切片及原π

finite index lists使每pair componentν_ij对dz绝对连续：ν_ij≤第一色i的marginal。取joint densitiesa_ij(x,s)≥0；Fubini前先用原marginal domination，得在a.e.(x,s)

    Σ_j a_ij(x,s)≤R^ε π₁,i，
    Σ_i a_ij(x,s)≤R^ε π₂,j。                    (4)

对每个固定R，indices虽可很多但有限；对所有i/j取finite null-set union，再Fubini，得a.e.x上(4)对a.e.s同时成立。event条件(2)/(3)也在a.e.x的sliced measure上成立。并非condition在一个概率零basepoint后免费继承marginal。

置m(x)=Σ_ij∫_I a_ij(x,s)ds。由

    ∫_X m(x)dx=ν(total)≥C₀^-1 R^-ε

与|X|固定，存在满足全部a.e.条件的x=x_R，且m(x)≥[2C₀|X|]^-1R^-ε。n=1时横向R^0视为单点、volume1，直接使用原整fiber。

在该fiber定义probabilityP(i,j,ds)=a_ij(x_R,s)ds/m(x_R)。于是两色的index-time marginals均≤C R^(2ε)πκ,i ds。只在这一步付实际分母m(x_R)^-1；π为原来的同一个概率weights，没有换成conditional weights，也未要求joint product。

## 6. 仿射rescale及TCM001的统一常数

置s=s₀+ℓt、0≤t≤1，Hκ,i(t)=hκ,i(x_R+(s₀+ℓt)v)。取matching导数阶D_m=D′、J=D_m+1>D_m。由§3、fixedℓ和fixed boxes，全列表0…J+1阶导数≤C_*R^ε；fiber probability的两色marginals≤C_*R^(2ε) πκ,i dt。events上

    |H₁,i−H₂,j|≤R^(-1+ε)，
    |(H₁,i−H₂,j)^(p)|≥c₁ℓ^pR^-ε。

可统一选择K_R=C′R^(2ε)≥1，使derivatives≤K_R、marginals≤K_Rπ_i dt、valuegap≤K_R/R、positive-order gap≥1/K_R。C′只依fixed data，也可放大处理finite constants；每个R的selectedx/p/v/box不同不影响C′ uniform。

保留列表card≤R^(d₀+ε)。取d₁=(1+d₀)/2<1。TCM001对固定D_m/J/d₁给existential tolerance η>0和thresholdN₀：lists各card≤N^d₁、所有displayed losses被K≤N^η控制时不可能。选

    ε_*≤min(1/4, (d₁−d₀)/2, η/4)，

再取R₀≥N₀，使C′≤R₀^(η/2)，并满足§3排zeroth所需的fixed阈值。于是对**所有**0<ε≤ε_*和R≥R₀有card≤R^d₁、K_R≤R^η；与TCM001（N=R）矛盾。

此处没有用C′≤R^ε的非uniform吸收：当ε→0时该说法不统一。实际把固定常数吸入预先固定的η/2，再用2ε_*≤η/2，故R₀独立于ε，量词正确。TCM001在real N上可直接使用，或取N=⌊R⌋并把固定比值吸入同一常数预算。

## 7. 两项完整假设删除测试

以下均取n=1、两lists各一个index、π两色为单点weights、M=1、Δ=R^-1、d=0和任意固定ε>0；R充分大即可令固定density2≤R^ε。它们不是原Cor3.4反例。

**删除fixed-degree后失败。** 取B=[0,1]、固定complex disk Ω包含B及fixed margin，f₁=0、f₂(z)=z^k，k=ceil(2log₂R)。common reference0，两个norm≤1，pair difference norm_B=1；在[0,1/2]取normalized Lebesgue probability，值差≤2^-k≤R^-2≤R^-1+ε，两个index-base marginals均2dt。质量1≥R^-ε、card1≤R^ε，全满足，但degree k→∞，违固定D。

**删除fixed holomorphic margin后失败。** 取固定B=[0,1]、a=R^-2，f₁=0、f₂(z)=a/(1+a−z)，令Ω_a={|z|<1+a/2}。这些域仍是complex balls，f₂在整个Ω_a holomorphic且real-on-real；关系(1+a−z)W−a=0的total degree2固定，norm_B=1。在[0,1/2]上同样取density2的probability，值差≤2a≤R^-1+ε，其余全部预算如上。但pole1+a逼近B端点1，B到Ω_a边界的距离a/2→0，没有uniform holomorphic margin。若硬用这些shrinking-margin Ω_a套(1)，uniform derivative/norm常数恰会失效。此修订保留ball域形状，仅删除fixed margin；不借用带内部holes的域。

两个tests分别保另一项假设，说明degree和complex margin均有独立实际作用。它们不删除原假设、不削弱验收范围、不作为新Kakeya结果登记。

## 8. 结论与独审边界

因此原Cor3.4在固定geometry/degree/holomorphic margins下完整成立，保任意原π和相关pair/common-basepoint law。subprobability mass、degree、reference、norm-to-each-point jet、finite direction/box、Fubini fiber分母及所有loss已逐项支付，不只是单fiber或数值例。

两份独立终稿research/reviews/R0031_analytic_matching_review.md、R0031_prior_norm_review.md均已通过；A/B分别核本主稿及对方必要输入，root逐式整合。登记ASM-001，仍未经外部同行评审。Lemma3.5真正terminal atlas与knowledge传回、critical paths及其它高级排除未因此认证。SRC001/DIR003/FSD001/DIM001保完整源条件，六维17/4仍条件，五维/一般Kakeya及重大性/新颖性标准保持，Goal active。
