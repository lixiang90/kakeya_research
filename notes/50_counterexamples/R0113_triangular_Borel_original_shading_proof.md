# R0113：任意 Borel 三角截距的原质量估计

2026-10-26，root。按 working spec 证明的 proper 类结果；未经外部同行评审，不声首次、重大或普通高维维数改善。本文的 independent review 另列，不以本文自核代替。三角性是强结构假设，未从任意 Kakeya 原族提取。

## 1. 精确有限命题与真实几何

固定 m>=1、0<s<1、固定非退化有界区间 J⊂R、R>0，0<δ<=1，整数 L>=1 满足 c0<=Lδ<=C0。取 v_k=k/L，0<=k<L，N=L^m。对每个 i，a_i(k_1,...,k_i) 为任意实数表。写 k_≤i=(k_1,...,k_i)。原 indexed cylinders 为

    C_k = { (x,t): t∈J, |x_i−a_i(k_≤i)−t v_(k_i)|<=Rδ, 1<=i<=m }.

对各自任意 Lebesgue 可测 Y_k⊂C_k，记 E=union_k Y_k、I=Σ_k |Y_k| 和 λ=I/[N(2Rδ)^m]，0<λ<=|J|。则存在只依 m,s,J,R,c0,C0 的 c>0，使

    |E| >= c λ^(m+1) δ^(m(1−s)).                 (F)

特别每 ε>0 可先选 s∈(0,1) 满足 m(1−s)<=ε，得到 |E|>=c_ε λ^(m+1)δ^ε。常数不依表的振荡、幅度、L、δ或各 marks 的形状。

真实单位轴采用方向 (v_k,1)/sqrt(1+|v_k|²)；斜率图 v∈[0,1]^m 上方向映射固定双Lipschitz，产品网有约δ角分离及全尺度m维帽界。若轴的clock在一个固定有界J内、与t=0的截距有上面的三角表结构，其round δ管包含于增大固定R和J后的C_k。故(F)直接对原round管内的Y_k成立。单位段可从t∈[0,1]的轴中取，因为该轴长度>=1；反向不把任意单位段免费延长并增加原marks。round endcaps仅改变固定envelope常数。

以下直接估计原 |E|，没有把 |N_δ E| 下界误回传到 |E|。

## 2. 标量共同时间能量界

记 U_s μ(z)=∫|z−w|^(−s)dμ(w)，I_s(μ)=∫U_s μ dμ。对任意实 A、B≠0，长度为ℓ的区间J有

    ∫_J |A+tB|^(−s)dt <= [2^s ℓ^(1−s)/(1−s)] |B|^(−s).       (1)

这是变量代换后，把固定长度区间移到0两侧得到的最大积分；s<1是必要范围。

固定一个prefix p=(k_1,...,k_(i−1))。令 u_δ 为区间[−Rδ,Rδ]上的均匀概率，

    μ_(p,t) = (1/L) Σ_(k=0)^(L−1) τ_(a_i(p,k)+t k/L) u_δ .  (2)

它是当前坐标在真实cylinder横截先验下的概率law，ρ_(p,t)是其密度。断言

    ∫_J I_s(μ_(p,t))dt <= C_s,                             (3)

对所有prefix及所有表统一，C_s还可依J,R,c0,C0。

证明：能量展开为L²对intervals。k=l的项先积噪声z,w：均匀长度2Rδ的interval自能量为

    [2/((1−s)(2−s))] (2Rδ)^(−s).

乘L个对角及L^(−2)、|J|，总为 O_s(L^(−1)δ^(−s))=O_s(δ^(1−s))，由Lδ>=c0统一有界。k≠l的项，对每对噪声先用(1)，再积分噪声，得到不依a和噪声的 O_s(|(k−l)/L|^(−s))。因此非对角总额不超过

    C_s L^(s−2) Σ_(d=1)^(L−1) 2(L−d)d^(−s) <= C'_s.

最后一步用Σ_(d<=L)d^(−s)<=C_s L^(1−s)。L=1时仅对角且Lδ>=c0，亦成立。Tonelli适用于非负extended kernels，无须先假有限能量。至此(3)是在同一J的积分，不是为每个prefix另选一个好t。

## 3. 真实原marks的一次潜势筛选

在源空间选全标签均匀law N^(−1)、t的Lebesgue以及m个独立u_δ噪声z_i。物理输出

    x_i=a_i(k_≤i)+t v_(k_i)+z_i.

其含marks的质量为 exactly λ，因为每label横截密度为(2Rδ)^(−m)。把Lebesgue marks换成Borel代表只改零集，有限union和I不变。

对T>0，声明坐标i为good当

    U_s μ_(k_<i,t)(x_i) <= T.                            (4)

在全先验中，该坐标的bad质量<=C_s/T：先固定prefix，当前k_i,z_i的law恰为(2)，再用Markov和(3)；其它过去/未来标签与噪声积分成1。故所有坐标坏事件的并质量<=mC_s/T。取

    T=2mC_s/λ,

则即使原marks集中于最坏处，marks∩全部good仍保至少λ/2源质量。这里按原I收费，没有删labels后偷偷重用原λ，也不要求每管marks都有正保留率。

## 4. good密度上界与逆序求和

对任意x，如果某个(2)中的interval含x，那么该interval的每个点距x<=2Rδ。所有这些interval的质量给出

    U_s μ_(p,t)(x) >= (2Rδ)^(1−s) ρ_(p,t)(x).             (5)

故在good处，ρ_(p,t)(x)<=(2Rδ)^(s−1)T。边界取代表不影响Lebesgue密度。

good且marked的推送密度为

    q(x,t)= [N(2Rδ)^m]^(−1) Σ_k 1_(Y_k)(x,t)
              × Π_(i=1)^m 1_{U_s μ_(k_<i,t)(x_i)<=T}.

它的总质量>=λ/2，且由(1)节的cylinder包含关系，1_Yk可以先上界为相应m个interval的indicator。固定t,x，从k_m开始求和：其所有因子中除第m个interval外，剩余i<m的因子不含k_m；第m个good条件也只含prefix k_<m、t及x_m。于是归一化的最后一层和正好是good×ρ_(prefix,t)(x_m)，由(5)至多T(2Rδ)^(s−1)。同样逐层到k_1，得到

    q(x,t) <= [T(2Rδ)^(s−1)]^m 1_J(t).                  (6)

被先丢弃的1_Yk可以依全部标签、全部x及t；它不需要分解。逆序求和利用的是剩余包络及good的三角性，不是伪称原marks有乘积结构。

q由原Y_k携带，因此

    λ/2 <= ∫_E q <= |E| T^m(2Rδ)^(−m(1−s)).

代入T即(F)。这是针对原实体shading的Lebesgue体积证明，未使用finite计算代替连续估计。

## 5. 连续 Borel 命题：直接 Hausdorff 返回

令 f_i:[0,1]^i→R 为任意Borel函数（可不有界），X(v,t)=(f_i(v_≤i)+tv_i,t)。对任意Borel Z⊂[0,1]^m×J，|Z|=λ>0，断言

    dim_H X(Z)=m+1.                                     (H)

对固定0<s<1，把(2)换为

    μ_(v_<i,t)=(w↦f_i(v_<i,w)+tw)_#(Leb|[0,1]).

其能量对t和全部prefix的平均统一有限：用(1)和

    ∫_[0,1]^2 |w−w'|^(−s)dw dw'=2/[(1−s)(2−s)]。

全部函数和核是Borel、积分为extended Borel函数，Tonelli/Markov合法。取T=2mC_s/λ，按与(4)相同条件保Z的至少λ/2质量，记推送有限测度为ν_s。不能假它有Lebesgue密度；下面证明球界。

固定prefix,t及任意区间Q长r。若good输出在Q内有正质量，任选Q内一个good输出z0，则

    μ_(prefix,t)(Q) <= r^s U_s μ_(prefix,t)(z0) <= T r^s.

因此只计good输出的质量也<=T r^s；若无good输出，结论直接成立。无需以可测方式选z0，此处是逐实例数值不等式。

对于物理盒Q_1×...×Q_m×Q_t、各边长<=r，丢原Z后，按v_m至v_1逆序积分，逐步使用上式；最后对t∈Q_t∩J积分。故

    ν_s(box) <= T^m r^(ms+1).                            (7)

同样有ν_s(B(z,r))<=C_m T^m r^(ms+1)，适用于所有r>0。ν_s总质量>=λ/2，且被Borel map的analytic像X(Z)携带（不是只被其closure携带）。对X(Z)的任意球覆盖应用(7)并求和，得H^(ms+1)_∞(X(Z))>=c_m λ/T^m>0。于是dim_H X(Z)>=ms+1；令s↑1得(H)，上界是ambient m+1。这里每个s可有不同ν_s，不声一个统一endpoint Frostman常数或正Lebesgue体积。

## 6. 原分母、restriction 和权重

保留 q 比例whole labels及其中 p 比例原I时，原平均密度以新条数归一为λ'=(p/q)λ；方向law重新归一也须除q。最安全调用(F)是把未保留labels设为零shading，保完整产品表和原N。若新I=pI，则(F)读作 |E'|>=c(pλ)^(m+1)δ^(m(1−s))。不能把不成产品的剩余labels当新的饱和 L'^m 网格，再免费使用同c。

原逐管λ0下界蕴含平均λ≳λ0，但潜势筛选只保证总I保留，不保证每管保留固定比例；若后续工具要逐管，需heavy并显写其条数与质量损失。删任意marks后只以新总λ重新调用，平均类闭包成立。

0<=w_k(x,t)<=1的fractional marks也可在相同证明中用w代indicator，总质量与密度上界照旧。无界权重或非均匀方向law不在本命题；若需bounded weights可先按其上界归一并收费。时间稀疏、每管不同clock和位置相关shading均已允许，只须都在固定J内。

## 7. 独立校准与不可外推项

真bush取全部a_i=0、J含[0,1]，marks为C_k∩{0<=t<=r}，δ<<r<=r0，固定r0可取小于min(1/4,Rc0)。λ=r（固定R）。原union在该clock内的横截box边长O(t+δ)，上界|E|≲r^(m+1)；在t∈[r/2,r]用h=1/L≈δ的斜率网格，相邻横截intervals的间隔th<=r0δ/c0<=Rδ，使union覆盖边长ct的box，故|E|≳r^(m+1)。若要marks直接属于round单位管，另取固定小R及r0小于单位轴clock长度的固定下界即可。这检验λ^(m+1)是自然收费；本例不否定某些不同δ/λ组合下的更强式。

只取有限个clock点时Z质量为0，(H)不适用；逐prefix挑好t也未被使用。若f_i允许依赖未来v_(i+1)...v_m，最后坐标求和之后较早的interval因子一般仍含k_m，(6)/(7)就没有依据。连续regularity不足或足够与此是不同输入，不能从Borel自动补三角性。

本类不是单纯Cartesian：例如f_2(v1,v2)可为任意联合Borel且同样f_3依前三参，不能作为各坐标独立集的Cartesian乘积。它也不覆盖旧cyclic闭环：若f_1真正依赖v_m，缺乏当前的有向无环prefix顺序。源里别处的系数三角消元不自动给物理方向截距此结构。

还有一个实际的输入反攻，不只说“没有证明三角化”。在m=4取

    A=diag(J0,J0), J0=[[0,−1],[1,0]], a(v)=Av,

方向取一个开cube，原单位轴按第1节。对任意固定实可逆S，共同空间坐标变换x'=Sx、v'=Sv使截距矩阵成为B=SAS^(−1)。它无实特征值，故第一行不可能只有B11一项非零（否则e1^T B=B11 e1^T是实左特征向量）。存在future系数B1j≠0，j>=2。

若在某个正Lebesgue角质量的可测集合D上能写 (Bv')_1=g(v'_1)，g为任意Borel，则固定v'_1后，D的剩余坐标fibre落在一个非零线性functional的level超平面中，(m−1)维Lebesgue测度为0。Fubini迫|D|=0，矛盾。因此即使完全光滑的真实全方向patch，也不能靠固定共同空间线性变换加正角质量删选免费进入三角类。这个例子本身有full-dimensional union：det(A+tI)=(1+t²)^2>0。它只反所述精确提取规则，不反任意δ近似、不同坐标类型、射影/非线性变换或整个普通Kakeya；不由缺三角性推低维。

## 8. 与旧闭包及文献的关系

R41已处理Cartesian熵；R93有标量投影能量的经典计算。当前新增的具体推导是：对任意Borel前缀耦合及原任意平均shading，统一潜势筛选后可合法逆序积分，直接得全物理有限体积式与独立Hausdorff式。它不是把R93同clock边际相乘，也没有借未付的好base维数。

最初 projection_slicing/首轮障碍与严格命题.md 的 LIFT-NEXT-01 是更广的Borel片段扩展问题；本证明只处理完整参数cube及三角截距，不给该一般F的好基点集合或原任意lift。不得把这个proper类当已解决整个LIFT-NEXT。

四维FSD/KT在m+1>4没有直接给所述full exponent；但已知平面投影能量加三角条件的迭代可能是经典初等后果。本稿不因新的归档措辞声首创。已实读Fu–Gan 2009.09108v2 Def1、Th1/2及§1 Lipschitz area-formula段（库内原件），其输入是连续与边界正则并得positive measure；这里无该正则、只得full Hausdorff/δ^ε，不能互相冒用。[固定版本](https://arxiv.org/abs/2009.09108v2)。有限检索未发现同述不构成新颖性证明。

## 9. 本轮结论与剩余主目标

(F)/(H)证明排除了任意粗糙三角prefix构造的维数亏损，并支付真实原shading质量；这是严格受限类的工具。普通高维族没有三角结构，真实非三角共同作用/HRZ及fullrough source仍未付。没有新普通维数界、完整source正gain、反例或重大成果，不完成Goal，不注册新的major ID。

本轮在独审后冻结此类后续常数、s与λ优化；下一轮不能简单把未来依赖另附小假设作ordinary成功归约。需对原full family给新的结构证据或不同机制。
