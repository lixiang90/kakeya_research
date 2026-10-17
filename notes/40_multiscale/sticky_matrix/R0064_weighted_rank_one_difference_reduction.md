# R0064：几乎全时间对的秩一差缩减及原图量词边界

2026-10-18，root。数学前锁定 research/rounds/R0064_working_spec.md §§5–7。本稿为自含有限维结构证明和严格时间图反例；不声五维Kakeya增益、重大性或首创，未经外部同行评审。A/B实际独审与最终结论另记。

## 1. 当前责任和两个不同的命题

真实五维source仍是WZ2609.22035v1 Def17.2–17.4原whole tubes、joint4-AD/CW、grains、xi及f共同数据；其原L图有相关输出A和bounded g。R58反攻没有该完整耦合。本轮先停止仅stationarity的grain/tube路径候选，再证明完整原时间先验nu²上的近秩一差分类，独立检验将其前提换成仅g边的说法。二者不能混为同一量词。

没有以raw满秩差自动给R45 good-star质量，没有为剩余common-kernel类补上未证扩张；此处不是完整source的新排除。所有time restriction保原labels/权，原平均图质量与逐管下界分开。

## 2. 定量命题和符号

固定R>=1，任意概率空间(Z,nu)，可测F:Z→Mat2(R)，operator norm ||F||<=R；0<a<=1，epsilon>=0，0<=q<1/100。设

    (nu×nu){(t,s): |det(F(t)-F(s))|>epsilon} <= q.       (2.1)

则存在可测Z0，nu(Z0)>=1-4sqrt(q)，以及以下之一：

- F(Z0)在某M0的operator a-ball内；
- 距某固定affine common-kernel plane M0+{u e^T:u∈R²}不超过 e0=100R²sqrt(epsilon)/a；
- 距某固定affine common-image plane M0+{v r^T:r∈R²}不超过e0。

e、v均为固定unit vector，plane距离可取Frobenius。常数独立于标签数、最小原子权、连续性、AD或g。近常值第一支以operator norm计；改全为Frobenius只放大固定常数。若epsilon=0，更可不取近常支，直接取exact affine plane，仍损至多4sqrt(q)；特别q=epsilon=0得nu-full精确分类。

## 3. 三个真实anchors和原先验删选

令b(t)=nu{s:|det(F(t)-F(s))|>epsilon}。当q>0，H={b<=sqrt(q)}有质量>=1-sqrt(q)；q=0则用H={b=0}，质量1。取t0∈H，F0=F(t0)，S1为H中与t0非坏对的点，质量>=1-2sqrt(q)。

若S1中||F-F0||>a仅零测，删去该零测集即近常值支。否则在其正质量子集选t1，A=F(t1)-F0，||A||>a、|det A|<=epsilon。再删t1的坏邻点得S2，nu(S2)>=1-3sqrt(q)。对S2中每个B=F(t)-F0，均有|det B|和|det(B-A)|<=epsilon。

只有有限个真实anchors，没有可测选择场或无原子假设；所有最终集合均由可测norm/det阈值定义。以下零测例外均可一次删净。原权未重置，也未合并重复labels。

## 4. 固定SVD下的定量消元

固定左右orthogonal坐标使A=diag(sigma,tau)，sigma>a，0<=tau<=epsilon/a。B同基且||B||<=2R。恒等式

    det(B-A)=det B-sigma B22-tau B11+sigma tau

给 |B22|<=6R epsilon/a²=:d。由det B小又得|B12 B21|<=epsilon+2Rd；若B,C还满足|det(B-C)|<=epsilon，则

    |(B12-C12)(B21-C21)|<=epsilon+8Rd.

取beta=64R²epsilon/a²，以上两product均<=beta，d<=beta。若beta>=1，则e0>=12.5R，原有界F距任意过0的指定plane已足够小，直接取Z0=Z。故只需beta<1，此时d<=sqrt(beta)。这一步并未预假A秩恰一或generic满秩。

## 5. row或column的一致选择与零阈值

先设epsilon>0。若S2上|B12|<=4sqrt(beta)几乎处处，第二column长度<=5sqrt(beta)，故在固定column2=0平面的5sqrt(beta)邻域内；返回原基就是common-kernel plane。

否则取真实t2∈S2且其|B12|>4sqrt(beta)，再删其坏邻点得S3，质量>=1-4sqrt(q)。若C∈S3有|C21|>4sqrt(beta)，两单点product界迫|B21|、|C12|<sqrt(beta)/4，故差product>(15/4)²beta，矛盾。因此全部|C21|<=4sqrt(beta)，第二row小，得到common-image plane。误差5sqrt(beta)=40R sqrt(epsilon)/a<=e0。左右orthogonal坐标只用一次，不按时间改变frame。

epsilon=0时，若S1上F本质常值则已exact落任意过该值plane；否则选任意非零A，无须||A||>a。其SVD有sigma>0、tau=0，消元得B22=0、B12B21=0。若B12本质全零，得exact kernel支；否则取B12非零的第三anchor，good差的det为零迫所有剩余C21=0，得exact image支。q=0照样只删有限个零测邻集。由此证明§2全部量词。

## 6. 原bounded图质量及restriction闭包

设sigma、pi亦为概率先验，原reference为sigma(dy)nu(dt)nu(ds)pi(domega)，0<=g<=1、质量m，允许任意相关。令P=nu(Z0)，g0=g 1_Z0(t)1_Z0(s)，则

    m0=integral g0 >= m-2(1-P) >= m-8sqrt(q).       (6.1)

故8sqrt(q)<=m/2才保证保至少m/2。归一nu0=nu|Z0/P时density=m0/P²，g值仍<=1。时间interval cap K及原all-real fit命中上界均至多付P^-1；不声删选后仍有AD lower、逐管density或完整Def17。若nu有time重复labels，该证明不变。

反向仅有结构也不能按任意小epsilon推出(2.1)：若dist(F,P)<=e0且||F||<=R，则同plane两点差det=0及2×2 determinant稳定性仅给|det(Ft-Fs)|<=C(R+e0)e0；近常a-ball只给<=4a²。删去theta质量的结论至多给另外2theta坏对预算。由此标明两向实际误差，不把它开成正幂增益新方向。

## 7. 输出误差与source应用的条件界

以固定plane正交投影定义可测Ftilde，||F-Ftilde||<=e0。若规范|t|、|psi|有固定上界，则

    |(t-s)(F(t)-F(s))psi-(t-s)(Ftilde(t)-Ftilde(s))psi|
        <= C e0.                                      (7.1)

若物理z=z0+s_t t、f_phys=M+s_F F、normal输出除s_y，误差为C s_t s_F e0/s_y。必须<=working resolution r才保O(r)的原输出A；不能把coarse近平面免费接R16。若F原h_SM-affine-fit质量<=b_SM，仅当h_new+e0<=h_SM时，Ftilde的h_new-fit在nu0下才<=b_SM/P。

common-image时(Ftilde(t)-Ftilde(s))psi严格沿同一v。只有(6.1)、(7.1)、原KT/time/slab/nonfit及参数余量均满足，才能重用R16 linewise finite theorem，其高级标量输入仍具名WZ Th13.5，wholeproof未本轮独证。nearconstant也须a在原禁止fit阈值内；否则本分类不排除。common-kernel时输出=(t-s)(u(t)-u(s))(e·psi)，仍是R58未解真实A-D耦合。本稿没有证明实际完整source一定满足足够小q或适当epsilon。

## 8. sqrt(q)删质量尺度不能普遍提高

在矩阵0、E12、E21上分别置原权1-2p、p、p，0<p<1/20。对epsilon<1/2，只有E12/E21交叉两种有序对坏，其质量q=2p²。若保质量>1-p则三个原子全在支持内，但det(E12-E21)=1，不可能全落同一exact image/kernel affine plane。对足够小固定plane-neighborhood，det稳定性仍反对；足够小固定a-ball同样不能包含三个矩阵。

故一般必须删至少p=sqrt(q/2)。对dominated submeasure也一样：总保质量>1-p迫三值均保正权。此例仅校准raw定理，不满足source非拟合等全条件，不反Kakeya或完整Def17。

## 9. 仅g边为秩一：真实1-AD时间的严格反例

取delta=1/(2M)，M为正整数；Z为[-1,-1/2)及[1/2,1)的delta-grid，nu为均匀概率，两branch质量各1/2，具有固定常数的全尺度(delta,1)-AD及interval cap。令c=1/8，负branch u=2t+3，正branch v=2t，均在[1,2)，定义

    F_-(t)=c diag(u,u^-1),
    F_+(t)=c [[0,v],[v^-1,0]].                     (9.1)

F有固定有界norm与Lipschitz常数，gap只固定长度，必要时可在gap内作固定Lip延拓。取g(t,s)=1当且仅当两端branch相反；其对称原图质量m=1/2。直接相乘得

    det(F_-(t)-F_+(s))=c²-c²=0.

所以图上坏对质量严格0。但同branch有

    |det(F(t)-F(s))|=c² |w(t)-w(s)|²/[w(t)w(s)]
                    >= c² |t-s|².               (9.2)

此式对全部实参数成立，不是数值有限抽检。原nu²有大量同branch满秩差，raw前提q小并未满足。

## 10. 任意保图删选都不能救出统一plane

任意affine image或kernel plane P中的两矩阵差det=0。若bounded F(t),F(s)均距P<=h<=1，选对应plane点，用det稳定性得|det(Ft-Fs)|<=C h。由(9.2)，同branch中所有靠近P的时间直径<=C sqrt(h)。原interval cap于是给

    nu{dist(F,P)<=h} <= C(sqrt(h)+delta).

更准确两branch各有该上界，因此任何0<=g'<=g、两端都落在同一P的h邻域者，原图质量<=C(h+delta²)。这里g'可任意相关、任意删边，非仅矩形restriction。h→0、delta→0时无法保任一固定比例m。h=0每branch至多一个grid点，图质量O(delta²)。

cross两branch矩阵Frobenius距离>=2c；因此半径a<c（operator半径a<c/2也足够）的单个matrix ball不能同时容两branch值，保g质量为0。故edge-only前提即使q=epsilon=0也不能给原m的nearconstant/image/kernel统一提取。

## 11. all-real affine非拟合亦成立

任意实矩阵R0,U0，若||F(t)-(tR0+U0)||<=h，则负branch的22-entry、正branch的21-entry分别满足|c/w(t)-affine(t)|<=h。相应scalar function二阶导8c/w³>=c，减去任意affine不变。

对二阶导>=c的函数phi，{|phi|<=h}在固定interval内至多两段。若其中一段长L，强凸性在其中点给phi(mid)<=(phi(left)+phi(right))/2-cL²/8，配合三值处于[-h,h]得L<=4sqrt(h/c)；端点用极限处理。故每branch fit集合由至多两段总长C sqrt(h)覆盖，grid命中率<=C(sqrt(h)+delta)，统一于所有实系数。取h=delta^a和任意b<a/2（且0<a<2）时，小delta下<=delta^b。

若fit tolerance采用h(1+||R0||)，结论仍<=C(sqrt(h)+delta)。为核量词，先用max-entry norm N=||R0||max。N>=2L时选斜率绝对值为N的entry，F的同entry为L-Lip；任意两个fit times满足(N-L)|t-s|<=2h(1+N)，故全fit集落长Ch的interval。N有固定界时回到上述强凸证明。operator与max-entry norm等价只改固定费；若tolerance还含||U0||，任一非空fit先给||U0||<=C(1+N)，在小h下吸收同一项即可。故取任意a>0、0<b<min(a/2,1)，h=delta^a时weighted全real fit质量亦<=delta^b。

所以反例同时有真1-AD time、bounded Lip F和all-real SM型nonfit。这里证明的是finite/continuum time-graph量词；没有构造g为A的输出关联，更未构造whole T、joint4-AD、xi、CW或完整Def17，因此不反完整五维source。其两branch也不是原source自动给定的分解。

## 12. 一手比对、审查和本轮停止

官方 arXiv:1402.4790v2（de Seguins Pazzis–Šemrl，2015版本）§2的maximal adjacent sets讨论已给精确affine row/column分类，见 https://arxiv.org/html/1402.4790v2 。本轮只补自含weighted approximate论证与原g作用范围；有界检索不认证该定量版本首创，更不把精确分类登记为新结果。比对记录保于literature/metadata/R0064_source_check.json，未引进其高级adjacency-preserver定理作证明依赖。

停止raw分类的常数/epsilon/a/q及edge-only同义版本；不新开ID。下一有意义责任仍须包含原A输出及wholeline/xi联合结构，或原source能付出的量化rank图输入，先查旧固定arms/box/linewise闭包及双向gain等价。普通n>=5/general、common-kernel扩张、mixed与general-to-sticky仍open，原Goal active。
