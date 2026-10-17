# R0029：条件finite种子转移与六维17/4推论

2026-10-17，root。**本稿完成的是有明确源条件的推导：假设SRC-001/DIR-003所依整篇四维proof及输入正确，则任意ambient的KT种子与六维Hausdorff下界17/4可由下述链推出。没有独立重证175页原proof，不登记无条件新维数界、重大性或优先权。** 两独审见research/reviews/R0029_projection_transfer_review.md与R0029_source_KT_review.md。

## 1. 旧输入先定位，不重复登记有限读出

R0007的SRC-001已给proof-level finite输入：每个固定有界四维graph chart、每σ>0，存在η_src>0、δ₀，使δ-separated directions的family若条数≥δ^(-3+η_src)、每条有≥δ^(-1+η_src)个δ-time marks，则visited δ-cell union不能≤δ^(-4+σ)。它**条件于完整OAI4 proof和全部输入**，不是由Theorem1.1的集合dim_H statement单独推得。

R0009的DIR-003已把它放大为稀疏/加权估计：∀ε_D>0存在η_D>0、δ₀和常数C，使bounded graph family每条marks≥δ^(-1+η_D)、每direction δ-cube总权≤α时，

    Σ_i ω_i #J_i ≤ C α δ^(-ε_D) #E。              (1)

原marks是各index自己的，重复与任意小权重允许。SRC001和DIR003不是本轮新结果；本轮复查其实际源链后才使用。具体source复查如下。

OAI4 Theorem2.17在PDF20–25先由Hausdorff覆盖选有限witnesses；选出以后不再使用同一个跨尺度原K。若finite输入对某σ及所有η均失败，可选η_k→0、δ_k→0的countersequence，在全部intercepts/slopes各独立δ_k-box平滑。full three-slope density≤C/(#T δ³)≤δ^(-η_k)=N₀^o(1)，长marks给inverse-subpower incidence mass，union亏损给g(1,0)≥σ。indices/cells/predicates数量皆有统一多项式界，故满足tempered要求。

原(2.27)的zero-depth bound使用Lemma2.15及full-slope推出的二维visible-slope cap；并非从四维集合主定理倒推。endpoint (2.29)–(2.32)给C(1−R)和g(r₀,u₀)≥σ/2。原massfloor (2.33)与slopevolume (2.34)抵消physical Jacobian、crop mass和a_r，得m(r₀,u₀)≤K₀q^-3，迫H≥σ/6>0。再调用原后续对所有bad exact problems的排除才产生矛盾。这正是R7有限读出的完整条件责任；本项目没有重证最后的高级排除。

## 2. 有限几何输入与任意ambient的投影lemma

固定整数ambient M≥4、bounded spatial box R、实s≥3、0<δ≪1。T为方向δ-separated的有限unit-length tube/line indices，m=#T；在任意projective angular ball、δ≤θ≤1上

    #{T: angle(v_T,u)≤θ}≤K(θ/δ)^s， K≥1。        (2)

Y(T)为原δ-grid tube中的shading，E=⋃Y(T)，每tube全grid点数≤C_M δ^-1。设总mass

    Σ_T #Y(T) ≥ λ δ^-1 m， 0<λ≤1。              (3)

可用cover数代替grid点数；单位δ-cell内点数/沿line最近点投影只付固定M,R常数。A稿逐项证明以下lemma，root亦独立核概率与符号。

任意m条原directions在(2)下，存在linear P:R^M→R⁴，||P||≤C_M；从其中|Pv_T|≥c_M的nonshort lines抽出方向c_Mδ-separated子族，数量至少

    c_{M,s} m/[K δ^(3−s)(1+log(1/δ))]。          (4)

证明要点是4×M Gaussian matrix。对原单位directions u,v，θ=projective angle，条件Pu后Pv的三维正交分量有variance sin²θ。在||P||≤C_M时，投影角≤Cδ迫该分量norm≤C_Mδ。因此该collision事件概率≤C_M min(1,(δ/θ)³)。用(2)作dyadic annuli求和，每line expected degree≤C_{M,s} K δ^(3−s)(1+log(1/δ))。

另由Gaussian χ₄小球估计，每direction短投影概率可选为小常数；operator norm大概率有固定bound。Markov和union bound同时给固定比例nonshort及O(mKδ^(3−s)log)总collision edges的一个P。图的independent-set bound m₀²/(m₀+2e)给(4)。不是把投影Frostman当免费继承；输出在RP³中δ-separated以后，所有centres/allscales cap3才由packing自动给出。

## 3. 平均shading、clock、短线与cover预算

先删#Y(T)<(λ/2)δ^-1的light lines。由(3)和逐tube上界，余下m_h≥c_M λm条，每条≥c_M λδ^-1旧marks。原cap(2)对这个子族继续成立，不能归一化后假ADlower。

对heavy族用(4)，得projected separated子族

    m' ≥ c_{M,s} λm/[K δ^(3−s)(1+log(1/δ))]。    (5)

每条projected length≥c_M。固定有限方向patch可使一个共同coordinate的direction分量≥c_M，仍仅丢固定比例。原δ-tube lattice points先移至center line至多C_Mδ，同一个projected time-bin只合并固定个原longitudinal δ-bins，所以各projected line在相当δ的mesh上仍有≥c_Mλδ^-1自己的marks。

所有旧marked points在固定bounded box。用有限个共同clock窗分箱、每line选最富窗再pigeonhole，只损固定常数；延长supporting graph lines到该共同窗并不加入新marks。尤其不能删去line endpoint附近shading再假仍有长duration。A稿提供完整有限分窗和mesh/coloring参数，源DIR003只需visited旧marks，不要求延长部分被shaded。

bounded P及固定chart/time归一化使新union E'的δ'-cells满足#E'≤C_{M,s,R}#E，δ'为δ的固定倍；近line误差仅用固定cell enlargement支付。未将不同原lines的shading拼到一个新line。所有常数与δ、m、权重跨度无关，可依固定M,s,R。

## 4. 真正的uniform finite seed，且有unsaturated形式

对projected δ'-separated lines以unit ω使用DIR003。它们的direction δ'-cube cap α≤C_{M,R}，不需near-full数量。若λ≥δ^η、η<η_D/2且δ充分小，固定mesh/mark常数可吸收，满足(1)逐line门槛。由(1)、(5)得

    #E ≥ c_{M,s,R,ε_D}
         λ² m K^-1 δ^(s−4+ε_D)/(1+log(1/δ))。     (6)

两个λ分别来自heavy line数量和每个输出line自身marks，不能漏掉一个。K源自原cap，未被输出normalized law消去。此式没有要求原m饱和；当右端小于1时仍为合法但弱的下界。

故∀ε>0，先选ε_D<ε/4、相应η_D，再取η<min(η_D/2,ε/16)，存在δ₀和C，使K≤δ^-η、λ≥δ^η时

    #E ≥ C^-1 m δ^(s−4+ε)。                     (7)

式(6)中损失至多ε_D+3η和log，均小于ε，余量吸收所有固定常数。取s=n−1、m≥δ^(-s+η)，还可把η再缩小，得到#E≥δ^(-4+ε_target)。因此对每个固定实n≥4、任意固定ambient，条件性得到KT意义的K(n,4−ζ)，∀ζ>0。对于不允许这样多方向的ambient，饱和family为空，陈述自然空真。

unsaturated(7)正是KT(40)所需m/N^(n−1)因子：δ=1/N时#E≥m N^(4−s−ε)。这里不必另把一般factorization theorem作为种子桥假设；原DIR003已付稀疏family。不把它当任意λ的尖锐maximal estimate，λ仍受η_D门槛限制。

## 5. 与KT原K量词及Theorem6.2的衔接

KT§5–6允许fixed ambient R^M的constants、real n/d、direction separation及total saturated shading，≈容许任意小幂费用，不限于log。用显式∀targetε∃inputη的形式记录(7)，或在固定ambient exact sequence中K=N^o(1)、λ=N^-o(1)，则(6)对每固定ε_D均可用，给#E≥m N^(4−s−o(1))。saturated m=N^(s+o(1))给临界4的序列性soft-loss结论。本稿只调用严格次临界K(n,4−ζ)：固定ζ后先取target亏损<ζ/2，再取KT的input小幂低于对应sourceη，可利用固定ζ余量吸收费用。没有从∀target ε∃η推得η(ε)线性模数，也不声称literal K(n,4)有统一N^(Cε)模数。不能预先让sourceη为一个过大的固定值。

KT6.2（具名原高级输入，未全文独立重证）：K(n,d)和K(d+1,d')在0<d<n时推出K(n,(2n+1+d')/4)。本次核其实际第二输入在Lemma6.6–6.7的R^(M+1) pivot family，并使用unsaturated(40)和其saturated residual shading；因此本稿arbitraryambient与(7)恰对准实际使用处。Lemma6.6 proof里d−1疑似原排印，不据此自称源全文已验证；statement d-collection及E ball cap的d维计数相合，使用的是named6.2完整定理。

标准small-loss/ε量词的选择可先固定最终target，再在有限次K调用中选源门槛的最小值；fixed ambient的常数和阈值可相应放大。B稿核原记号和recurrence责任。本稿不以只有单一固定精度的finite bound调用soft-loss K。

## 6. 六维条件结论及其边界

固定0<ζ<1。由§4有K(6,4−ζ)和K(5−ζ,4−ζ)。取n=6、d=4−ζ、d'=4−ζ调用KT6.2，得

    K(6,17/4−ζ/4)。                             (8)

这一步不需经典KT六维起点，也不需未经支付的‘方向维单调性’；§4已对每个实n≥4给出所需两输入。由KT Definition6.1后的Hausdorff转移，对compact六维Kakeya set E有dim_H E≥17/4−ζ/4。对所有ζ>0取极限，条件性得

    dim_H E ≥ 17/4 = 4.25。                     (9)

当前结论保KT已核的compact convention，不把任意不可测高维集合推广隐含进去。若要扩大该scope需另给cover/outer-direction argument。五维在这条递推的固定点上限仍为4，(9)没有解决五维或一般满维数猜想。

已有一手基线KT及2025 Gao–Liu–Xi Table1记录六维7−2sqrt(2)≈4.171573；17/4更大。但2025表不认证2026全部前沿，有限搜索空结果也不证新颖性。R29新文献原件已入literature，完整source/版本/校验及比对范围见metadata/R0029_source_check.json。**式(9)始终条件于SRC001/DIR003所依全部四维proof正确及KT6.2；不得在登记中删除条件或认证重大结果。**

## 7. 验收及宏观意义

本轮不再只剩‘集合Hausdorff⇒finite’口头跳步：旧SRC/DIR提供实际proof-level输入，新Gaussian碰撞/independent-set与clock/shading预算把它转到arbitraryambient和实direction维，(6)还付unsaturated第二输入。源条件没有被消除，所以无条件新高维bound与Goal最终标准仍未达到。

内部逐式审查应分别核投影/质量、旧finite source读出、KT量词与Hausdorff结论。下一宏观任务须围绕剩余源验证与真正更高维后果选择，不回到R28已冻结的action/carry常数。R30常规macro保留，长期Goal active。
