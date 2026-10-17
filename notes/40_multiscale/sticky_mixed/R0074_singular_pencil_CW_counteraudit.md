# R0074：singular evaluation pencil 的全维压缩与原 CW 出口

2026-10-18，B。仅编辑本分配文件；不操作 Git、元数据或新代理。本稿不预设完整源已提取参数 pencil。证明下面全类线性代数及其定量 CW 用途，原 AD0 图的质量提取由 root/A 另付、互审后才合并。内部审查不等于外部同行评审。

## 1. 原命题、旧边界与停止条件

本轮对象是 bounded 原直管的物理参数 `(p,v)∈R⁴×R⁴`。假原管子族占**原**管概率质量 p>0，其参数在误差 ε_par 内靠近一个 affine m-plane，4≤m≤8。用原参数 Euclidean 正交基写该 plane 为

    (p(z),v(z))=(p0,v0)+(Az,Bz)， z∈R^m， |z|≤R，       (1)

其中 `[A;B]` 可取 isometry、A/B有固定上界，reference p0/v0也 bounded。物理 evaluation 为 `C(t)=A+tB`。本稿首先完整证明 `rank C(t)≤3` 对所有 t 的精确分类和原 CW 正幂出口；再从小 4-minor 系数给统一幂稳定。这里单射 joint embedding 明确是参数空间的事实，不把物理方向分离加到原 T。

已读回 R19全局残差/原权与R20 parent-clock边界、R45 fixed-arms/fibre范围、R64 raw与used-edge量词、R72 whole-time/basicness限制。当前方法不用GWZ局部时钟、不从相交tuple假定全部子族靠plane、不从used g-edge假全pair代数、不以数值可逆性授原AD lower。不同输入只有本轮拟从原AD0 labels提取的共同参数plane；若该输入未付，本稿不能单独排完整mixed42。

## 2. 精确分类：以 compression subspaces 代逐个 Kronecker 块

对任意固定0≤r≤min(4,m)，下述两件事等价：

    (i) rank(A+tB)≤r，对全部实数t；
    (ii) 存在0≤e≤r、K⊂R^m、E⊂R⁴，
         dimK=m−r+e，dimE=e，AK+BK⊂E。                (2)

(ii)⇒(i)立即：对补空间只增加m−dimK=r−e维像。反向先令r0=max_t rank(A+tB)≤r。取实际t0达到r0，把A换成A+t0B；固定可逆row/column变换化为

    A=[ I_r0  0 ; 0  0 ]， B=[ C  D ; F  G ]。

在t=0附近，I+tC可逆。Schur complement和全t秩上界给

    tG−t²F(I+tC)^−1D≡0。

故G=0，且 `F C^k D=0` 对全部k≥0。置

    U=span{imD,im(CD),...,im(C^(r0−1)D)}， e=dimU。

Cayley–Hamilton给CU⊂U，上述恒等给FU=0。于是

    K0=U×R^(m−r0)， E0=U×{0}，
    AK0+BK0⊂E0， dimK0=m−r0+e。                       (3)

还原row/column变换得到真实原子空间K0/E0。若r0<r，取K0中维数m−r+e的子空间即可；e≤r0≤r。r0=0时A=B=0，直接e=0、任选dimK=m−r，也包括此边界。不存在需遗漏的regular/left-minimal或多个right-minimal类型；(2)本身是所需精确全类分类。

**不把分解基底常数带入几何。** (3)只证明真实K/E存在。随后在原Euclidean空间中取它们的orthogonal projectors，直接做cover；不用上述GL基底参数化原管，因此不会出现随δ失控的Kronecker条件数。

## 3. joint单射、m>4与全部退化检查

joint(A,B)单射时，取两个不同t，stacked evaluations与joint(A,B)同rank，因此m≤2r0。另(3)在K0上仍单射到E0×E0，故m−r0≤e≤r0。m≥4且r0≤3的可能范围仅有：

| m | r0 | 可用e范围 |
| --- | --- | --- |
| 4 | 2 | 2 |
| 4 | 3 | 1、2或3 |
| 5 | 3 | 2或3 |
| 6 | 3 | 3 |

m≥7不可能精确singular；r0≤1也不可能。此表不声每个e是唯一或不交的canonical type，而是完整compression分类的充分维数清单。

只固定一个right-minimal块时，m>4可能错误地少算其余参数费用；(3)已同时合并全部右核变化。constant tildef产生的共超平面、parallel/commonridge以及含left-minimal退化都落在(2)中。L0形式的共同零参数列若存在则违joint单射；证明本身即使保留它也不失效。若拿有大joint核的重复参数当原四维管量而非真实标签，必须先纠正输入，不能靠本稿制造反例。

## 4. 精确 pencil 到原概率 CW：全m而非仅m=4

假原子族质量p，参数恰位于(1)，且精确rank≤r0≤3。取(3)的原orthogonal K/E，补空间维数d=r0−e。对bounded `P_(K⊥)z`用h-grid覆盖，0<h≤1，只有 `C_R h^(−d)` 个格。存在一格原质量至少 `c_R p h^d`。

固定该补坐标格的中心z0。格中全部原轴的物理位置都在

    {p0+Az0+t(v0+Bz0)+u : u∈E， |t|≤R， |u|≤C_R}

的Ch邻域内。这个集合位于真实(e+1)-affine plane；bounded管长和roundcaps只给δ增厚。故δ≤h时，存在包含这些**完整原管**的凸box，其e+1个长轴为O_R(1)，余4−e个短轴为O_R(h)，体积≤C_R h^(4−e)。原normalized CW因此满足

    C_CW(T) ≥ c_R p h^(r0−4) ≥ c_R p/h。                (4)

原T分母不换成所选子族，p不能省略；也未把incidence比例直接冒成管概率。m>4的补参数数是r0−e，而非m−e−1，所以全m仍有至少一幂。这里不需对子族重新假AD4 lower；原AD4只可能用于上游提取和确认p。若仅控制短clock片段而非整管参数，本段不成立，不能偷用whole-tube CW。

## 5. 统一幂稳定：在orthogonal Grassmann上直接最小化

设m固定、||A||+||B||≤R。令 `D(A,B)` 是所有4×4 minors `det(A+tB)_I` 的全部t系数的最大绝对值；每个minor次数至多4。定义

    Ψ(A,B)² = min_(e=0..3,K,E)
       {||(I−P_E)A P_K||_F²+||(I−P_E)B P_K||_F²}，    (5)

其中dimK=m−3+e、dimE=e，P_K/P_E为orthogonal projectors。对m≥4这些维数合法。projector条件 `P=Pᵀ=P²,trP=dim`为固定多项式条件，参数集compact。故Ψ连续且固定半代数；全部4minor系数为0时，第2节给Ψ=0。

**固定半代数幂引理的实际支付。** 置

    H(s)=max{Ψ(A,B)²: ||A||+||B||≤R， D(A,B)≤s}。

compactness使max存在，且H(s)→0（否则取收敛子列违D=0⇒Ψ=0）。real quantifier elimination给H为一元半代数函数，格式只依m/R。其图没有二维内部，QE的有限多项式sign分解中，每个图点必有一个非零多项式取零；有限乘积P(s,H(s))=0对足小s成立。将P除掉最大的公共s幂，得P(0,y)非零。若H不在0附近恒零，P(0,0)=0；取其最低非零y次j≥1，则对小y有 `|P(0,y)|≥c y^j`，而在0≤y≤1有 `|P(s,y)−P(0,y)|≤Cs`。所以 `H(s)≤C s^(1/j)`。若H恒零结论平凡。

由此存在只依固定m/R的c>0、C，使

    Ψ(A,B)≤C D(A,B)^c。                              (6)

此处具名基础是与R31相同的real quantifier elimination；已将所需一元growth逐项证明，不调用未给常数的pointwise连续性或无限个decomposition charts。矩阵域固定bounded，因此C/c不依δ、最小非零minor或某canonical basis condition number。上游若使用δ-dependent非正交基，须先回原S的orthonormal基并另付误差；(6)不能免费替那步。

## 6. 近singular到凸box的完整量化

若参数距S≤ε_par，而 `D(A,B)≤ε_min`，由(5)(6)选择真实orthogonal K/E，使每单位K方向的A/B到E泄漏≤`C ε_min^c`。令

    h ≥ C_R(δ+ε_par+ε_min^c)， h≤c_R。                (7)

用K⊥的h-grid，补维数恰3−e，得到原质量至少 `c_R p h^(3−e)` 的格。轴线的K部分在E⊥的误差至多C_Rε_min^c，参数距离误差O_Rε_par，再加真实δ半径，均由h支付。故相同whole-tube凸box计数给

    C_CW(T) ≥ c_R p/h。                              (8)

这里normal thickness是h而非强写δ；近singular至正幂box的责任已在(6)(7)中完整付出。若p≥δ^a、ε_par≤δ^b且ε_min≤δ^b，取固定s<min(b,bc,1)，h=Cδ^s，得CW≥cδ^(a−s)。a≪s时违原CW≤δ^−η。固定s先于原η；不可将h的固定幂成本收进δ^−Oη。

jointembedding有固定smin时，m≥7的近singular甚至存在固定正下界D≥c_m,R：否则compactness收敛到joint仍单射的exact singular，违第3节。这不是对源free goodrank假设，而是参数S用orthonormal joint基时的恒真性质。

## 7. 从原time正质量的小minors到(6)：离散floor明确

假原time probability ν满足 `ν(I)≤K_t(|I|+δ)`，在ν质量至少b的time集合G上，全部4minors值≤ε。若δ≤c b/K_t，greedy可在G中选5个实际time，两两gap至少 `g=c b/K_t`：每次删前面选点的2g邻域，至多4个，原质量损<Cb。无需G可测参数的连续选择，只作5次有限选择。

degree≤4的Lagrange插值中，每个分母含4个gap，time位于固定bounded interval，故所有系数

    D(A,B)≤C ε g^−4≤C ε(K_t/b)^4。                  (9)

ν可为原δ-grid原子law，正质量set也可依此前有限anchors；只要它的真实原分母与intervalupper在上游已付。本段未把同管访问的共同time集免费当uniformlaw，更未在重复label后抹去b。将(9)代(6)(7)后，所有输入费用是固定次幂；若ε仍为真δ精度乘subpower/小固定conditioning费，就可保一固定正幂h。

只有某个孤立时刻rank亏、某一4minor小或一个goodtuple存在均不够；需全部minors在足原time质量上统一小。rank≤3只在used-g边上的形式陈述也不自动给同一个A/B。本稿不把这些未付输入藏在Remez一词中。

## 8. 原AD0提取的接口及不能省的分母

当前root/A拟从实际tube×(time,AD0 label)二部图以有界次原矩/CS提取共同right neighbors和真实tube子族。用于本稿的最终接口必须逐项给出：

1. 实际原tube质量p≥δ^a（不是仅固定anchor tuple的质量）；
2. m≥4的同一个affine S、原orthonormal joint基及所有所用管距S的ε_par；
3. 同一共同right集合的原time质量b与K_t，label重数和不同time值均未抹；
4. 原F_t在S上的法向约束到全部4minors的小量ε，包含tuple条件数与Oδ放大；
5. a与输入误差指数足以满足(7)(8)的正幂不等式。

上游AD4 upper可排小于4维的早停carrier，但不会免费给高维S上的均匀law；本稿cover只需真实p，因此没有把高维plane误当m维Lebesgue。若同label限制打破逐管density，需重计平均访问/原tubeheavy后再把p交来。原CW概率和原#T分母保持，不靠改成稀子族来制造矛盾。

初稿时此接口尚待上游施工。现已实际全文读root12的独立row-greedy提取及A13的tube-anchor版本，第10节逐项核其完整返回。本稿的exact/近似分类不是完整Def17 source反例；源应用必须连同该原质量提取读。

## 9. 反攻校准与本稿数学verdict

parallel/commonridge导致的真低维wholeaxis集中按(4)确实CW过大，不是合法small-CW反例。含left-minimal项不会破本证，因为Schur可达空间已把regular/left部分计入固定补参数；仅取一个right块才会在m>4时错丢费用。若只得parameter joint3-Frostman或若干pairdet近零，均没有(9)所需共同pencil，R45/R64/R72停止线保持。

最坏rank3只保证p/h：p若本来≤h，则出口可完全被mass吃尽，不能宣所有任意稀subfamily都矛盾。clock截短再补成unittube也不继承本whole-tube box；本稿使用的是原管完整(p,v)接近S。定量(6)依固定格式/固定m≤8；degree或变量数随δ增长时没有相同c，不能接proper有理或高复杂度假设改名。

当前已完成的是**全m singular pencil的精确compression分类、统一幂稳定和保原分母的whole-tube CW出口**。root12现有原质量提取已按第10节独核，与此前条件CW结论合起来确有bounded完整mixed42 κ1用途；仍须A/B正式交叉审后才登记内部reviewed。无ordinary新界、新ID、major或优先权声明；半代数幂稳定是经典基础应用，不宣创新。标准QE基础和上游源责任各自列明，未经外部同行评审。

## 10. root12的原row-greedy接口与固定维推广独核

已实际全文读取 `R0074_AD0_native_labels_to_CW_exclusion.md`12节，并读回Def3.6/3.9/17.2–17.4及Remark17.1相应原段。root采用不同于tube-anchor的row-greedy正证，可完整付第8节接口。

原全部T的bounded jointchart是**必要输入**，root§1现已显式沿R43规范保留。localAD4本身不限制无界unused T总数；bounded usedT计数也不能代原N。当前原N≈_Kδ^-4已给，故每layer原visits≥K^-1δ^-4确实给 `I≥K^-CN#Z`。先tube-heavy到H0并保每管旧全部visits≥K^-C#Z。以后只按anchor label删wholeT，这个逐管下界继续成立，没有为条件图免费重建pointΦ lower。

维护真实H_j及j个原rows V_ti，同time同原label约束把H_j困于j个δ厚affine slabs。若距旧rowspan>τ的times携带至少半数当前原visits，实际time平均和该time的至多K labels给下一H_j+1≥K^-C H_j。否则W的原time比例≥K^-C：分母是#Z，不是邻接time重新归一后假满。row独立的Gram–Schmidt体积≥τ^j，其余singular values固定upper，给参数距S_j≤Cδτ^-j。

j=5时，S_j维数3，bounded θ'=Cδτ^-5 邻域以Cθ'^-3个joint balls覆盖；AD4upper给原质量≤Kθ'，与H5≥K^-C冲突。取τ=δ^a、a<1/20，再η后小可付此矛盾。因此某j≤4停止；j0因V含恒1坐标不可能，得到同一S维数4..7、原p≥K^-C、ε_par≤Cδτ^-4。

取S的原orthonormal joint basis Q=[A;B]。对原W，`||n_t C(t)||=||V_tQ||≤τ`，||n_t||≥1；固定upper下每个4minor≤Cτ。第7节5个原分隔times仅费K固定幂，给D≤K^Cτ。于是本稿第6节h可取δ^s，其中s>0先固定小于a c和1−4a，η最后小，原p/h违CW≤δ^-η。没有要求nearS的管在S上均匀，也没有用其marks重置原CW概率。

固定n=d−1时，相同root链的每layer供应为δ^-n；ADn阻止n+1个独立rows。S维数至少n，n-minors次数≤n，n+1个分隔times插值；Schur给K补维n−1−e，而物理d维凸box短轴为n−e，故仍CW≥cp/h。每个n固定后QE格式和常数固定，推广在所列bounded输入下成立；不声dimension-uniform、任意正维native labels或ordinary初始化已付。

另已实际全文读取A13 `R0074_AD0_label_source_and_mass_audit.md`。其独立tube-anchor proof保真实H0原visits，以right=(time,原δ-label)编码；`Σ deg_out deg_all≥Σdeg_out²≥I_r²/(4Km)`逐式正确，p_(r+1)≥p_r²/(4K)仅有限次。停止时用每管≤m边才返回原H≥p_rN/2，并非仅返回anchor tuple。r<4的θ-nearcarrier由原AD4upper排除；r8时共同right仍有正量且V含恒1，δθ^-8矛盾。共同right time数≥p_r m，故5节点原clock插值floor也已付。ε_par=θ与D≤K^Cδθ^-8共同选h，而不是把nearS误差强写δ。A13的完整上游返回无未解决必修项。

本次实际独核root12/A13没有未解决的强制数学修订项。wholeclock原管和原全N分母均保留；κ1完整源应用已不只是一个孤立pencil lemma。最终macro/next仍须按后续授权全文审查，不预认证未来文件或Git状态。
