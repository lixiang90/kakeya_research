# R0080：KT提升核心的保留遮蔽证书

2026-10-18，root阶段II整合。先锁working_spec§2后施工。仅复核KT math/0102135v1 §6的归一化pivot核心；不是新定理或整个Th6.2的独立新证明。root12/A12/B12及两formal6已实际全文逐步独审，限定通过；未经外部同行评审。

## 1. 命题、量词与原分母

固定ambient M和实n,d,d′，0<d<n。令N→∞、δ=N^-1、H=H_N≥log N且log H/log N→0；可把固定次幂和固定常数吸入H，本文所有C只依固定参数。方向分离的原直线族T在固定有界盒中，每条线的原遮蔽Y(T)⊂E由δ格点组成，位于其Cδ邻域，每条N/H≤#Y(T)≤CN；#E≤H N^d，且

    #(E∩B(a,r))≤H (Nr)^d， δ≤r≤C。

有原角族A={(x,T1,T2)}，x为两遮蔽的同一原格点，∠(T1,T2)≥c>0、#A≥N^(2n−d)/H。每个角的x及T1,T2均取原标签，不能增加重复方向标签。原方向δ分离保证一方向只有O(1)条原管，交点格选择亦只有O(1)种。

最后独立输入为**非饱和**种子S(d,d′)：任意固定ambient内、方向δ分离且cap≤N^o(1)(Nθ)^d的任意条数m直线及每条N^(1−o(1))个原marks，支集至少m N^(d′−d−o(1))。其准确意义是∀固定输出损失ε>0，∃输入容差η(ε)>0与门槛；不能假设η线性。固定次数的subpower盒、换尺度、着色及marks亏损仍在该量词内。一般符号d′时这是具名K(d+1,d′)的真实unsaturated版本；d≥3、d′=4−ζ的项目应用可用已审FSD001，不从四维Hausdorff一句话倒推。

本证书在这些**归一化critical数据**下构造Ω′与删后lift multiplicity μ_z，证明

    |Ω′|≥N^(2n−d+2)/H^C，
    Σ_z||μ_z||₂²≤N^(d+2−d′+o(1))|Ω′|，
    Σ_z||μ_z||₂²≥H^-C N^(1−2d)|Ω′|²。

故4d≥2n+1+d′−o(1)。Ω′与每个z的原lift labels是后续质量分母；不把每pivot的旧N个pairs假装在删后逐pivot保留。

## 2. 细格约定与几何条件数

原points以实际δ格标签计数。高ambient中的原轴可以异面，不能假装存在精确交点。为计算，先把每个角的两轴各平移O(δ)到通过其原共同格点x，再把其遮蔽点投到这两条代表轴；所有点改动O(δ)。原label和方向仍保留，最终lift线用同一个原x，全部差额单独保为H^Cδ。所有新z按确定最近δ格选取。空间、时间的最近格选择均固定，任何H^Cδ-ball只有H^C个fine格；未把它叫O(1)。

后文所有坐标、逆Jacobian、分母绝对值在[H^-C,H^C]内；因此这些投影/舍入误差经有限次四则运算仍≤H^Cδ。若某一步仅有近似等式，它表示这一明确宽度。H^Cδ邻域的二维平面在H^C盒内只有H^C N²格；有向线段只有H^C N格。原精确线的fine marks上界仍CN。

lift mark可选在**精确lift线**的Cδ-neighbourhood：先算未舍入的t，把t舍入δ格，再把精确空间坐标x+t(z−i)舍入δ格。原端点y2与该空间格的距离允许H^Cδ。这样种子使用真实细管marks，回拉用带H^C有限重数的近似，而非把厚管当细管。

## 3. 每角的真实好三元组与pivot数

令局部交点为0，T1=R a、T2=R b，|a|=|b|=1、|a∧b|≥c。写i=s a、y1=t a、y2=r b。先仅取原三元组中

    |s|,|t|,|r|,|s−t|≥H^-C0。

每个被排除的短区间最多CN H^-C0个原marks；C0先取大于原质量亏损的固定倍数，故保≥N³/H^C个真三元组。特别|y1−y2|≥H^-C；这一条件随原pair进入lift mark，并在全部删选后保留，不在最后凭空追加。

令未舍入pivot

    z=s a+r(1−s/t)b， i=s a。

它同时在y1y2的直线和i+R b上。|z−i|、dist(z,T1)、dist(z,T2)、|z−yj|均≥H^-C，|z|≤H^C。舍入z后上述性质带H^Cδ误差成立。固定z的i投影到T1由沿b方向恢复，至多H^C种原fine i；给定y1，y2由z y1与T2交点恢复，亦至多H^C种。故三元组→z纤维≤H^C N，像最多H^C N²。丢掉纤维小于N/H^C的z，仍保≥N²/H^C个z；再在各z的H^C种i中选最重一个，保≥N/H^C个原好pairs。

以这些z及所选原i_(α,z)定义Ω。每个(α,z)保存其实际好pair关系P_(α,z)，N/H^C≤#P≤H^C N；不改原E，也不凭空填其line。于是

    |Ω|≥N²|A|/H^C≥N^(2n−d+2)/H^C。

## 4. f=(z,i)的Córdoba能量与真正单值子族

由|z−i|≥H^-C及z−i近乎平行T2，给定f最多H^C种原T2方向/标签；逐纤维选最重T2，先保H^-C原Ω。以下只比较同T2。

固定角α与θ∈[δ,1]的dyadic角距。若另一(α′,z)有同f且∠(T1,T1′)≈θ，则i属于两T1 fine邻域，其位置至多H^C/θ格。因i离T2≥H^-C，T1′必须在T1,T2所张平面的H^Cδ角邻域；原方向分离给T1′至多H^C Nθ种。每个i的z沿i+R dir(T2)至多H^C N格。T1′、T2给原交点标签x′仅H^C种。因此每α每θ的碰撞数≤H^C N²。最小角bin与相同T1同样≤H^C N²，不遗漏对角。

求和O(logN)并吸入H后，E_f=Σ_v|f^-1(v)|²≤H^C N²|A|。另一方面|Ω|≥N²|A|/H^C，故E_f≤H^C|Ω|。Cauchy–Schwarz给|f(Ω)|≥|Ω|/H^C。每个f值只取一个原(α,z)，得到f真正injective的Ω′，仍

    |Ω′|≥N^(2n−d+2)/H^C。

这是合法原label删选，不能由旧函数图条件直接跳到无损单值。后续只在此Ω′上工作。

## 5. 正确lift端点、原pairs与实际marks

对(α,z)∈Ω′定义精确lift线

    L_(α,z)(q)=(x_α+q(z−i_(α,z)),q)。

局部坐标中q=r/[r(1−s/t)]=t/(t−s)，所以空间端点是**T2上的y2**。同时

    z=(1−1/q)y1+(1/q)y2，
    y2=qz−(q−1)y1， y1=(qz−y2)/(q−1)。       (R)

|q|、|q−1|在[H^-C,H^C]。原文lift first coordinate的y1指标不能照抄：z−i平行T2，实际几何给上述y2。

每个P_(α,z)原pair按§2送到实际lift finecell w=(p,[q])；w空间p与其原y2距离≤H^Cδ。单个w反解原y2和y1各至多H^C格，故像至少N/H^C。去重复后定义原lift遮蔽Ybar_(α,z)，每cell预先固定一个真正原好pair作为witness。每条N/H^C≤#Ybar≤H^C N；整个support在H^C盒内。所有witness永久保|y1−y2|、|q−1|≥H^-C，且满足(R)误差≤H^Cδ。

## 6. d-collection与种子适用的实际整理

固定z，f单值给不同lift labels有不同原i∈E。方向由v=z−i经图(v,1)归一化决定；在H^C盒中该map双向条件数H^C。角θ-cap只允许i落在H^Cθ-ball，因此

    #cap≤H^C (Nθ)^d， δ≤θ≤1。

正确指数是d，正好对应K(d+1,d′)，E球上界不能给d−1。原PDF Lem6.6 statement与这一指数一致；proof中的d−1不作为加强输入。

若lift方向仅δ/H^C分离，以局部邻接图着色为H^C个δ分离类：每个δ-cap的原i数至多H^C，故最大度H^C。support若非固定盒，分成H^C个固定盒，每线取marks最多的一盒；如用更粗fine scale或固定长度段，再损H^C个marks/labels即可。选定固定盒中的子族后，方向cap仍H^C(Nθ)^d、各线marks≥N/H^C。尺度如变Ntilde=N/H^C=N^(1−o(1))，card幂相差仅H^C。以下种子每次真正作用于这样的一块/一色及原marks子集；它不要求此子族条数饱和。

## 7. 高重数截断保原mass，不保逐pivot密度

固定z，m_z=#Ω′_z，μbar_z为原Ybar的finecell乘数，原mass W_z=Σ_w μbar_z(w)在[Nm_z/H^C,H^C Nm_z]。非空族的种子S已经要求d′≤d+1：否则只取一条近满线便以其O(N)总marks反S，输入不相容，命题属空情形。以下取d′≤d+1。给定固定ε>0，定义

    bad_z={w: μbar_z(w)>N^(d+1−d′+ε)}。

若badmass≥W_z/2，heavy筛选给至少m_z/H^C条原lift labels，每条至少N/H^C个badmarks。§6着色和盒划分再保m_z/H^C条、每条N/H^C marks；对这一真实badmark族调用S(d,d′)，在足够大N给

    #bad_z≥m_z N^(d′−d−ε/4)/H^C。

于是W_z≥N^(d+1−d′+ε)#bad_z≥m_z N^(1+3ε/4)/H^C，与W_z≤H^C Nm_z矛盾。因此在所有足够大N，每z低重数部分保≥W_z/2。设Ybar′=Ybar∖bad_z，μ_z为其乘数；删的是同z原support上的点，非另造pair。总retained mass

    W′=Σ_z||μ_z||₁≥N|Ω′|/H^C。

可集中于少数角，**不声每个(α,z)仍有N/H^C marks**。这种集中不妨碍后面的全局Cauchy–Schwarz。

## 8. 上二阶矩与small-loss次序

每z ||μ_z||∞≤N^(d+1−d′+ε)、Σ_z||μ_z||₁≤H^C N|Ω′|，故

    Σ_z||μ_z||₂²≤H^C N^(d+2−d′+ε)|Ω′|。       (U)

所有几何C固定后，先固定ε，取种子输出ε/4及其输入η(ε/4)，再令N大到H^C≤N^η且所有种子常数/门槛有效。若写ε_N↓0，使用对ε_j=1/j的对角门槛N_j，同时压H^C与常数；不假设η线性，也不在有限N让ε任意趋零。于是(U)可写N^(d+2−d′+o(1))|Ω′|。该整理同时涵盖Ntilde与固定ambient M+1，绝不让ambient随N增长。

## 9. 带保留指标的真实三元组关系

只对每个**已保留**的(α,z,w)取§5预先固定的原witness (y1,y2)。记记录关系R⊂{(α,z,w,y1,y2)}；每个保留mark恰一个record，所以#R=W′，不会因删选后再要求好pair而损mass。令

    r(z,y1,y2)=# {R中的records投到该(z,y1,y2)}。

这等价于在原pair关系中保留实际的1_(Ybar′_(α,z))(w)；不能把它换成全部原collinear pairs。

支集Σ由z∈H^C盒、y1,y2∈E、|y1−y2|≥H^-C且三点在H^Cδ同线邻域组成。给定有分离的原y1,y2，其直线在该盒内允许至多H^C N个z格，故

    #Σ≤H^C N |E|²。                         (S)

若漏掉原pair分离，此式在近重合端点处不成立。这里分离从§3穿过全部真实marks而来。

## 10. 同triple与同liftcell的双向有限恢复

固定(z,y1,y2)，(R)及|y1−y2|≥H^-C唯一决定连续q并把所有对应w约束在一个H^Cδ邻域：q可由y2−y1=q(z−y1)的任一条件良好分量恢复，|z−y1|≥H^-C。故该triple涉及至多H^C个fine liftcells；不论α为何，都落在同一有限邻域。

反过来，固定(z,w=(p,[q]))，原y2在p的H^Cδ邻域，至多H^C种；再用|q−1|≥H^-C的(R)恢复y1至H^Cδ，至多H^C种。每(α,z,w)只一个record。因此将r按w再分解、两次有限重数Cauchy–Schwarz得到

    Σ_(z,y1,y2) r(z,y1,y2)² ≤ H^C Σ_z||μ_z||₂²。       (P)

更明确地，r²≤H^CΣ_w r_(z,y1,y2,w)²；固定(z,w)至多H^C个triple且r_(...)≤μ_z(w)，故求和即(P)。误差既没有冒同一exactcell，也没有把多个原witness重复计为独立mark。

## 11. 下二阶矩、比较与反攻范围

由#R=W′、(S)及Cauchy–Schwarz，结合(P)得

    Σ_z||μ_z||₂² ≥ H^-C (W′)²/[N|E|²]
                  ≥ H^-C N |Ω′|²/|E|²
                  ≥ H^-C N^(1−2d)|Ω′|²。             (L)

比较(U)、(L)并约去非零|Ω′|，得|Ω′|≤N^(3d+1−d′+o(1))。再代§4原下界2n−d+2，给4d≥2n+1+d′−o(1)。原文附近的upper/lower文字不用于判断方向，(U)/(L)由实际计数决定。

反攻项都在证明中有对应：浓集删选只保全局W′；t近1、小z−i和近重合pair在原好三元组中付；fiber用原方向分离/交点恢复；fine邻格损H^C；unsaturated种子而非满方向假定；小损失按∀ε∃η/门槛。有限计算不替代任何连续或Hausdorff步骤，本轮无需用数值测试冒这些证明。

## 12. 独立输入、现有六维后果与停止边界

本证书**没有独立新证**KT proof开头的critical raisingd、heavy-ball regularization、bilinear角尺度归一化及一般K(n,d)→unsaturated的factorization。它把准确normalized输入写在§1并实际付之后的几何/删选/二阶矩。advanced wholeproof仍具名，不把三处书写澄清包装成wholeKT6.2已经全独证。

R29/R38已审链中FSD001有fixed任意ambient和real angular s≥3、原K及λ²费用；足以给全real n≥4的K(n,4−ζ)，包括raisingd涉及的第二输入。具名KT6.2代n=6,d=d′=4−ζ，再已有任意set finite→Hausdorff桥得dim_H K≥17/4。此为既有DIM001条件后果；本轮没有新的finite/ambient/Hausdorff桥，没有证明2026最新最优或优先权，更无ordinary R5改进/一般满维/major。

完整source jointAD4/CW、filledX2、pointΦ/selectedξ的κ1缺口和其他完整路径继续open。本轮停止于该具体core证书或独审暴露的精确剩余gap；不续改数字模型/更多anchors，也不递归重证所有高级文献。A/B实际全文交叉及root终审已限定通过，见research/reviews/R0080_density_and_scope_review.md、research/reviews/R0080_geometry_and_retained_mass_review.md与research/reviews/R0080_root_integration_review.md；仅所列normalized核心内部reviewed，未经外部同行评审，Goal active。
