# R0030：原Lemma3.3的完整固定阶重证

2026-10-17，root。对象是OAI4原Lemma3.3（PDF29–35），不是新的Kakeya定理。下文只用statement中的C^(J+1)、列表cardinality、双index-time marginal和value/jet gap；经典Taylor、entropy chain rule、条件概率、area formula及固定次数多项式孤立解数界作为基础工具。无需代数性、均匀index权重、joint product或未来成功条件的独立性。B稿逐项展开probability kernels，A稿独立反攻必要假设；两独审在research/reviews/R0030_matching_geometry_review.md与R0030_matching_probability_review.md。

## 1. 命题与反证准备

固定D≥1、整数J>D、d₀<1。两indexed实C^(J+1) lists在[0,1]，各card≤N^(d₀+o(1))，导数0…J+1均≤K=N^o(1)。有event probability P⁰(i₁,i₂,t)，每colorκ的(iκ,t)-marginal≤Kπκ,i dt，Σ_iπκ,i=1。events上

    |f₁,i₁(t)−f₂,i₂(t)|≤K/N，
    max_(1≤j≤D)|f₁,i₁^(j)(t)−f₂,i₂^(j)(t)|≥1/K。   (1)

欲证不存在这样的N→∞序列。D的导数索引取整数，非整数D可替为floorD。K可随固定有限步骤扩大但始终subpower；所有分母为零的条件核在原概率零集合上任意定义。

先有限pigeonhole选择一个j≤D承载常数比例events，再按各order gap的log尺度pigeonhole/取subsequence。只损inverse-subpower质量，得到固定β_j≥0，β₀≥1，某β_j=0（j≤D）；未截断gap为N^(-β_j+o(1))，所有gap至少有该upper。大于固定B>1的指数作upper-only cutoff；cutoff项在下面a>0的最大值中不可能active。归一化这次restriction将双marginal的K只乘inverse-subpower，不改原π为虚构的条件先验。

## 2. jet尺度、余项和history

对0≤a≤1定义

    r(a)=max_(1≤j≤J) (a−β_j)/j，
    l_j(a)=max_(0≤x≤a) [x−j r(x)]，0≤j≤J。       (2)

r(0)=0，r为递增convex piecewise-linear，r(a)≥a/D。并有

    l₀(a)=a，0≤l_j(a)≤β_j，
    l_j(a)−l_(j+i)(a)≤i r(a)，
    (J+1−j)r(a)>l_j(a)（a>0）。                  (3)

第三式在l_j最大点x处用l_(j+i)(a)≥x−(j+i)r(x)；末式若x>0用(J+1)r(x)>x，否则l_j=0而r(a)>0。所有严格性来自J>D，不需函数解析性。

在r的一个unique active m-piece，

    r(a)=(a−β_m)/m，l_j(a)=a−j r(a)（j≤m），
    l_j(a)>a−j r(a)（j>m），l_m=β_m。             (4)

因r'在此前不大于1/m，x−jr(x)对j≤m此前非减；j>m在本piece严格下降，故其历史max严格大于当前值。active m≤D≤J，因为一个β_j=0、j≤D的term压过所有m>D的term。该额外上界不是证明必须的新假设。

从每个piece两端和a=0裁掉小fixed trim，忽略太短pieces。compact剩余上所有

    l_(m+i)(a)+i r(a)−β_m>0

及(3)的Taylor余项差有统一正下界。取C>5J及足够小common step b，使a到a+Cb留在piece且这些gaps大于例如4b。**先选finite grid，后做state mass选择**；该grid含1、主步端点a/a+b和a+Cb。可以在不同b-grid上重新做选择，证明不用跨grid同一个homogeneous law。

F_a记录含t的nested dyadic interval I_a（|I_a|≈N^-r(a)）、两arms在其中心的0…J derivative bins（width N^-l_j(a)）及全部更早grid histories。Taylor translation的bin/remainder误差至多

    K Σ_(i=0)^(J−j) N^(-l_(j+i)(a)−i r(a))
       + K N^(-(J+1−j)r(a)) ≤ K N^-l_j(a)。       (5)

对两arms的gap同样用β_(j+i)≥l_(j+i)得同一界；所以两arms的各级bins只差K个邻格。一个arm index与I₁决定该arm所有earlier history，另一arm只有K个（fixed grid的subpower）邻选。因此

    #supp F₁ ≤ N^(d₀+r(1)+o(1))。                (6)

## 3. pre-selection质量而非条件posterior的后代数

记此时law为p_pre。对已固定grid再做一次inverse-subpower restriction，使出现的F_a atoms的**p_pre质量**统一为N^(-u_a+o(1))。极轻atoms先用(6)删，finite log-pigeonhole后取subsequence即可。nested atoms给u_a非减、u_a≥0；(6)和restriction仍有inverse-subpower质量给

    u₁≤d₀+r(1)。                                (7)

若retained粗atom A在a层有c>a层retained children，每个child的p_pre mass≥N^(-u_c-o(1))、parent mass≤N^(-u_a+o(1))，故

    #children≤N^(u_c−u_a+o(1))。                 (8)

不需要任何child在final normalized law中的mass lower。最终normalized law记P，双marginal仍≤Kπ_i dt。后续所有选择与heat-bath均针对这个同一个P；成功路径保持subprobability，不按未来成功重归一化。

## 4. palette的低信息增量

在当前m-piece起点A₀，palette Z是两arms的m-th derivative bins，width N^(-β_m−D₁b)，D₁>5固定。F_A₀已知width N^-β_m的bins，故

    H(Z|F_A₀)≤2D₁b logN+O(1)。

对步a定义L_a=log[P(Z|F_(a+Cb))/P(Z|F_a)]在实际sampled Z处取值。nested states的chain rule与每段overlap≤C给Σ_a E L_a≤C H(Z|F_A₀)。负部E(L_a)^-≤1/e：条件fine state，用p(z)log(q(z)/p(z))≤q(z)/e在p<q处求和。

先把至多J个piece的entropy预算相加：每个预算O_J(b logN)，总预算仍O_J(b logN)。把总trim长度选小于1/2后，保留steps总数与1/b可比；不按某个可能很短的piece单独平均。因此全局平均E(L_a)^+≤O_J(b²logN+1)，常数不依trim后单个piece的长度。两次Markov给：除O_J(b^(1/2))+o_N(1)比例的steps之外，每一步以P-probability≥1−O_J(b^(1/4))−o_N(1)满足

    P(Z=z|F_(a+Cb))≤N^(b^(5/4))P(Z=z|F_a)。        (9)

这里不是对所有z一律成立；下节明确kill坏palette values，并靠真实marginal domination扣平均failure。

## 5. 交替sampling及真实质量下界

固定good step及E⁰∼P，在同一个I_a内做m+1 legs。每leg先按当前fine F_(a+Cb)条件刷新一份event E~，但保持running time t_p不变；选择其中一个arm φ，再从P条件于该arm实际color/index及I_a重新sample下一event/arrival time。

若输入event submeasure≤cP，按任意state进行heat-bath仍≤cP。对adaptive color选择，以两个color-index/I_a heat-bath kernels之和上界，每个都保P。所以raw E^p及刷新event的marginal≤2^pP。此上界只用于平均failure扣除，不假条件于exact start仍有相同density。

选色使相邻离散controls间距≥1/K：fresh pair两m-th controls之差为N^β_m times原gap，加上小于fixed power的近似误差，故至少1/K；给定preceding control，二者中至少一个距它≥1/(2K)。首leg任取一个color。此规则允许依完整history和整个fresh event。

kill (9)失败的refresh；再kill chosen(κ,i,I_a)的P-mass小于πκ,i |I_a|/logN的pair。对每color，后者在P下总probability≤1/logN，因为threshold在所有indices/time intervals之和为1/logN。raw marginal≤2^pP使全部有限legs这些failures至多O_J(b^(1/4))+o_N(1)。

retained pair下新time density≤Kπ_i/[π_i|I_a|/logN]≤K/|I_a|（log已入K）。归一化time s=(t−centerI_a)N^r(a)的density≤B_N=N^o(1)。令内部arrival times两两gap至少1/(B_N logN)，每个新time避先前有限个坏interval只损O_J(1/logN)。该gap仍是N^-o(1)。因此对b足够小、N大，successful experiment的平均probability≥固定c>0。

## 6. normalized dynamics及switch errors

固定exact start，令T为其一个arm在t_a=centerI_a的J阶Taylor polynomial；T及start time s₀固定。对j<m，沿chosen φ置

    Y_j=N^l_j(a) ∂_t^j(φ−T)，s=(t−t_a)N^r(a)。

由(4)，dY_j/ds=Y_(j+1)（j<m−1），最后dY_(m−1)/ds=U+O(N^-2b)。残余m-th derivative的variation和J+1 remainder由§2严格trimmed gaps支付。U由coarse history、A₀ higher-jet bin centres、fresh palette和color离散决定，可显式取

    U=N^β_m [palette_m(A₀)+Σ_(i=1)^(J−m) higherbin_(m+i)(A₀)(t_a−t_A₀)^i/i!−T^(m)(t_a)]。

从I_A₀中心Taylor到t_a的palette误差N^-D₁b，其余higher-bin/remainder errors均小于N^-2b。同一trimmed gaps也支付(φ−T)在整个I_a内的m-th variation，故U不依隐藏index。不是直接把fresh实际函数当成独立constant control。

每次refresh保持fine state，old arm是当前event的一arm；old/new各fine jets只差K邻格，running/witness times也在同一个fine interval。因此switch在actual running time的normalized jump≤K N^(l_j(a)−l_j(a+Cb))=K N^(-(1−j/m)Cb)≤N^-2b（C>5J且K subpower）。这也包括first switch与start frame的差。

有限m+1 signed legs内，chain dynamics为nilpotent积分系统，switch及control errors只积累O_J(N^-2b)，无需exp(K)的Gronwall费用。times可向前或后，始终在同一I_a。

## 7. 同一Λ与完整past下的product upper

所有coarse states沿有限legs留在start确定的K个邻states：refresh保coarse，traversal保chosen arm的全coarse history，另一arm各level只差K邻格，fixed grid/leg数使总仍subpower。对每个可能F_a和两colors，把其P(Z|F_a)推到上述discretized U；求和得共同measure Λ_(start)，mass≤K。

给定完整hidden history H_p，下一refresh只条件于当前fine state，故在(9)的good values上palette law被N^(b^(5/4))倍coarse law支配。adaptive chosen arm的point mass可由两个candidate pushforwards之和支配；再给定实际index，new-time density≤K ds。故未归一化successful一步kernel满足

    Q_(H_p)(dU ds)≤N^(b^(5/4)+o(1)) Λ_(start)(dU) ds。  (10)

Λ与hidden past无关而仅依exact start。对只依start、displayed U/time序列的非负必要test，从末step向前逐步积分(10)：末step上界的结果只依较早displayed序列，所以可继续迭代；没有conditional-on-future-survival或重新归一化。可把hidden成功约束全部丢掉作upper。B稿§§2–8给formal kernel proof。

## 8. endpoint Jacobian及固定次数regular multiplicity

以exact constant controls U₁,…,U_(m+1)解系统，无switch误差。令s为final arrival、internal times s₁,…,s_m，start s₀固定。final j-th low jet的control项为

    [U₁(s−s₀)^(m−j)
      +Σ_(p=1)^m (U_(p+1)−U_p)(s−s_p)^(m−j)]/(m−j)!， 0≤j<m。 (11)

其余项仅依start和s。对s_p的导数为−(U_(p+1)−U_p)(s−s_p)^(m−j−1)/(m−j−1)!。time输出本身为s，所以全map (s₁,…,s_m,s)→(s,Y₀,…,Y_(m−1))的absolute determinant为

    [∏_(p=1)^m |U_(p+1)−U_p|]
      [∏_(p<q)|s_p−s_q|]/[∏_(k=0)^(m−1)k!]。   (12)

success时controls及internal times均N^-o(1)分离，故det≥N^-o(1)。polynomial degree/dimension只依m：固定输出s后，m个方程degrees≤1,…,m，regular solutions是isolated，经典Bézout的孤立解数界给≤C_m（例如m!）的regular multiplicity，允许其它singular components存在。未假全map全局一一。area formula因此对任意measurable target V有time integral≤N^o(1)|V|，uniform于满足separation的controls。

## 9. 真child target体积与可求和误差

令c=a+b。一个retained child F_c记final interval I_c和全部jet bins。按**child自己的I_c**在finaltime翻译，subtract固定T并coarse normalize，用(5)得每j<m target fiber width

    ≤K N^(l_j(a)−l_j(c))=K N^(-(1−j/m)b)。

normalized finaltime interval length≤K N^-b/m；N^-2b simulation误差可吸。尽管target中心随finaltime移动，Fubini仅需fiber widths，所以该child target volume≤

    N^(-α_m b+o(1))，α_m=1/m+(m+1)/2。          (13)

由(8)、有限coarse-neighbor set和两finalcolors，total target volume≤N^(u_c−u_a−α_m b+o(1))。target membership加上(12)所需separations仅依exact start和displayed controls/times，是(10)允许的必要test。

fix controls应用(12)/area formula，再对Λ^(m+1)积分，其mass仍N^o(1)。conditional successful probability uniform上界为

    N^(u_c−u_a−α_m b+(m+1)b^(5/4)+o_N(1))。

与§5平均success≥c矛盾除非

    u_(a+b)−u_a ≥ b(1+1/m)−C_J b^(5/4)。          (14)

这里使用α_m≥1+1/m。**保留明确的每步b^(5/4)误差**，不能以任意o_b(1)写法后直接相加；O(1/b)步的总误差O_J(b^(1/4))才确实趋零。

## 10. fixed-grid求和、uniform版本与结论

在一个已固定trimmed grid上先N→∞，good steps失败比例≤O_J(b^(1/2))，其余increments非负；固定grid内所有o_N(1)总和趋零。各piece r'=1/m，故对disjoint主steps累加(14)，再取b小、trim小，给

    u₁ ≥ 1+r(1)−O_J(trim+b^(1/4)+b^(1/2)+b)。

不需不同grid间u_a来自同一law：每个grid均有统一upper(7)。以1−d₀的fixed gap先选trim和b使总error<(1−d₀)/2，即在该单一grid上与(7)矛盾。因此原subpower sequence不存在。

若不存在任何足够小fixed-power tolerance，则对η_k→0选任意大N_k的counterfamilies，把所有loss均记入K_k=N_k^o(1)、card≤N_k^(d₀+o(1))，形成刚排除的subpower sequence。故原statement中的existential uniform small-power版本亦成立，**未给显式η(D,J,d₀)模数**。A的fixed-power边界说明不能删除其order/gap依赖；不构成原lemma反例。

验收：一般fixedD/J/d₀的原Lemma3.3在这些假设下完成内部逐步重证，未使用后续Kakeya排除或假设全四维proof。它只认证一个共同源gateway；Cor3.4的代数norm-to-jet/holomorphic continuation、Lemma3.5 atlas回传、critical paths及其它branches仍未全面独审。DIM001依完整OAI4的条件并未因此消除，Goal active，无新的无条件高维定理或重大性认证。
