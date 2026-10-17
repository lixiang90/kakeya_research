# R0045：同源四臂的因子、真实star质量与BL费用

2026-10-17，lifting_obstructions。读固定入口/context、R45周期macro/spec及R44停止边界。只编辑分配文件，不Git、不另开代理。目标是实际d5,k=ell3的原四臂机制；有限真实star不等于完整positive-κ source，raw四臂数量不等于BL-good质量。以下有自包含有限证明及明确的未付责任，不宣新颖/重大，未经外部同行评审。

## 1. 精确同源因子与原Oδ误差

记base point p的time为t0、f0=f(t0)、ξ0=ξ_p。arm T_i的actual axis方向为v_i=(φ_i,ψ_i,1)，原见证给ψ_i=ξ0+f0φ_i+Oδ；endpoint p_i在time t_i，另有ψ_i=ξ_i+f_iφ_i+Oδ。因此

    ξ_i=ξ0+(f0−f_i)φ_i+Oδ,
    B_i=(-f_i,I₂,−ξ_i)。                            (1)

共同线性gauge y′=y−f0x−ξ0t后，理想无误差map为

    L_i(x,y′,t)=y′+(f0−f_i)(x−φ_i t)。             (2)

不能把(1)中的Oδ无条件删去，亦不能用generic无因子maps代替它。下面先对exact数据给充分BL判据和一组真实直线实现，回答因子本身是否必退化；后面原计数始终保source误差及旧law。

## 2. 四个rank2 maps的自包含充分判据

设L_i:R5→R²满rank，G_i=ker L_i。若每对G_i∩G_j恰为一条线，且固定i时三条G_i∩G_j（j≠i）在三维G_i中线性独立，则

    ∫R5 ∏_{i=1}⁴ f_i(L_i z)^(5/8) dz
       ≤C_L ∏_{i=1}⁴ (∫R² f_i)^(5/8)             (3)

对所有非负可积f_i成立。在本段“各pair交恰为一条线”的假设下，它亦必要：若固定i的三线只张成二维V，则L_iV=0、其余三张在V上rank≤1，BL dimension inequality右边≤15/8<2；若只张成一维，则该线是四张共同kernel。因此BL有限时三线必须独立。不能将这个特定判据换成stacked rank或不带pair假设的普遍描述。

证明：固定i，坐标写z=R_i w+K_i u，其中L_iR_i=I₂、K_i:R³→G_i为线性同构，Jacobian固定。对j≠i，L_jK_i是rank2 map，其三条kernel在R³内独立。以这些kernel作三条坐标轴后，三个map分别只读其余两个变量，外加可逆R²变换及依w的平移。三维Loomis–Whitney即给

    ∫R5 f_i(L_i z)∏_{j≠i} f_j(L_j z)^(1/2) dz
       ≤C_i (∫f_i)∏_{j≠i}(∫f_j)^(1/2)。          (4)

这里所需LW可由两次Cauchy–Schwarz直接证：先对s1积分两项平方根，再对(s2,s3)把第三项与分离乘积作CS。可逆二维变换的行列式及domain Jacobian均保入C_i，不能免费取1。对四个(4)的integrands作四项Hölder，每个f_j的指数变成(1+3/2)/4=5/8，得到(3)，常数≤∏C_i^(1/4)。因此无须仅凭未知generic-BL定理来认证下面的有限例。

## 3. 满足同源因子的真实四线例及sharp ρ费用

取c_i=i/8（i=1,…,4），0<ρ≤1，base p=0、f0=0、ξ0=0。令

    f(t)=t I₂,  φ_i=(c_i,c_i²),
    T_i(t)=(tφ_i,0,t),  t_i=ρc_i,
    f_i=ρc_i I₂,  ξ_i=−ρc_iφ_i。

四条T_i是真直线，p_i=T_i(t_i)；原grain plane {B_i(z−p_i)=0}确含p和整条T_i，所有系数/方向均在固定有界box内，(1)无误差精确成立。maps为

    L_i(x,y,t)=y−ρc_i x+ρc_iφ_i t。

在G_i的坐标(x,t)中，G_i∩G_j的generator为

    ℓ_ij=(c_i+c_j, c_i²+c_ic_j+c_j²,1)。             (5)

固定i，将三个j≠i的generators作列得M_i。其det绝对值为三节点c_j的Vandermonde ∏_{j<k;j,k≠i}|c_j−c_k|，非零且与ρ无关。故§2判据适用。

还可完整算常数：固定L_i=w后，余map在(x,t)上为ρ(c_i−c_j)(x−x_ij t)。换到M_i坐标，两个非kernel列的二维行列式绝对值为ρ²(c_i−c_j)²|det M_i|。domain坐标(w,x,t)到原(x,y,t)的Jacobian为1。因此(4)可取

    C_i=ρ^(−3)|det M_i|^(−1/2)
                  ∏_{j≠i}|c_i−c_j|^(−1)，
    BL(L,5/8)≤Cρ^(−3)。                            (6)

另一方面所有L_i在base三维G0={y=0}上范数Oρ。以固定R² unit-box indicators测试，其joint preimage含沿G0长c/ρ、normal二维宽c的柱，给BL≥cρ^(−3)。故此有限real-star例的BL常数确为ρ^(−3)量级，而非被因子强迫∞。

这个例子没有完整Def17.2–17.4的δ-AD/CW、positiveκ、原tuple law及所有times/grains；其f还是旧matrix-affine分支。它只证明“同源因子必使四臂BL∞”这一步是错的，并校准near-parallel费用；不提供实际source中的good-BL比例，不是五维Kakeya反例或增益。

## 4. 实际同world必付BL费用与共同frame

若实际四endpoints与base在同一个allowed time-ρ ancestor，原dyadic-Lip及(1)给||B_i−B0||≤Cρ（δ≤ρ）。B0有统一right inverse，因为y-block是I₂，故G0=kerB0为三维且有固定condition数。unit-box测试同样使

    BL(B_i,5/8)≥cρ^(−3)  （或∞）。                   (7)

这不是一根近共同方向的ρ^(−1)，而是整个三维near-kernel。若使用在domain ball半径R内的truncated constant，上述lower仍有效，只要R≥C/ρ；本次natural R≈ρ/δ、δ≪ρ²时满足。若只知R更小，须保min(R,ρ^(−1))³，不能越过截断。

parabolic frame能改变数值但不免费：domain L在三条tangent方向缩ρ、两条normal方向缩ρ²，detL=ρ⁷；同时各target除ρ²，记B_i′=ρ^(−2)B_iL。对无限BL由变量代换精确有

    BL(B′,5/8)=ρ³ BL(B,5/8)。                       (8)

因为四target determinant贡献ρ^(4Σp_i)=ρ¹⁰，domain贡献ρ^(−7)。因此局部O(1) datum与原ρ^(−3)并不矛盾；physical Jacobian、plank厚度和积分域要同步改变。对truncated版本还须同步域半径，不能只改常数。(7)本身未必吃尽gain：ρ=δ^µ可预留小µ，是否可支付要看完整账本。

## 5. 实际raw四臂数量：不同T/time可付，横截质量仍未付

使用R16已核used-incidence graph，固定T,z仅O(1)点、每point/φ-bin仅O(1)tube见证。source给#T≈_Kδ^(−4)、#E≈_Kδ^(−5+κ)、point degree≈_Kδ^(−κ)、总incidence I≈_Kδ^(−5)，其中K=δ^(−Oη)。每T的原endpoint degree D_T≤Cδ^(−1)。以下是同一图上的真实有限计数，不预设四张maps独立。

先删D_T<I/(4#T)的tubes，丢≤I/4 incidences；再仅对base points删remaining row degree<I/(4#E)，再丢≤I/4。保留base p有d_p′≥K^(−C)δ^(−κ)，所用T的**原**D_T≥K^(−C)δ^(−1)。端点仍在这些T的原全部marks中选择，不把base删选再反馈成endpoint剪枝，故没有循环丢掉D_T lower。

对每保留p、四个row choices T_i、每条T_i上的原endpoint choices p_i计数，真实raw mass为Σ_p Σ_(T_i)∏_iD_(T_i)。由上下界，所得总量至少K^(−C)δ^(−9−3κ)，并保原完整star count的K^(−C)比例。这个star参考law就是这些实际有限关联的counting law；若另有额外bounded g约束，不能凭此断言g也保该lower。

原Φ_p slabγ经row删选只损K^C，因此pair φ-distance≤r的比例≤K^C r^γ。条件于每条实际T，端点time law满足mass(I)≤K^C(|I|+δ)，来自sameT,z upper与D_T lower。raw endpoint choices给定(p,T_1,…,T_4)正是四个有限选择集合的乘积，这是该raw tuple计数的定义，不是将别的相关g独立化。union bound可删φ近邻、相同T及|t_i−t_j|≤r、|t_i−t0|≤r的tuples，损失≤K^C(r^γ+r)，D_T的K^C比较照付。

取r=δ^α≥δ、η≪αγ，可保K^(−C)原star质量且四T不同、四endpoint times分离。这部分不是主要未知。**BL-good tuples的质量仍无lower**：分离φ/time及(1)均不自动保证§2充分判据或任何全BL界。source ξ/φ/time的其它相关性必须保留，不能拿§3有限校准或随机maps替代提取。

## 6. 真physical overlap可由近incidence付，不要求filled grain

对endpoint原affine plane Π_i={z:B_i(z−p_i)=0}，同一actualT_i的p与p_i满足p_i−p=(t_i−t0)v_i+Oδ。由B_i v_i=Oδ及bounded clock，|B_i(p−p_i)|≤Cδ。B_i的两个非零singular values在固定上下界内，所以p距Π_i≤Cδ；固定数量邻接δ-cubes处理即可让四plane-neighborhoods在base cube附近确实相遇。

这里是对affine-plane neighborhoods作上界估计，可以用完整virtual planes或其实际需要的bounded部分；**并不要求这些plane里面已有source filled shading**。因此不应仅以“沿T平移未送filledgrain”作为这个ZK上界版本的失败理由。若后续另用要求plank shading density的定理，那项责任才需另付。当前真正要付的是plane-label/index数、near-incidence的固定邻格重复、BL-good原tuples与endpoint fibres。

重复labels也不能产生免费gain：若每个四family中的index重复k次，选中tuple count乘k⁴，5/8幂乘k^(5/2)；upper中的∏N_i^(5/8)同乘k^(5/2)。故把原raw tuple数直接当大量不同plane labels，会在这里精确抵消；应保原weights或证明fibre upper。

## 7. 可用选中tuple形式下的条件指数

已实际读Zorin-Kranich1807.09604v4 PDF1–6对应text的Def1.1、1.4及Theorem1.3、1.5：Fremlin形式允许选中tuples，并非只对四个Cartesian families全部横截才可用；本稿不以那个较弱障碍提前停止。这里用regularized BL(1,R)，不把它无条件换成scale-invariant常数。按本题P=5/2、p_i=5/8，各Fremlin因子为ℓ⁴，其norm至少product ℓ⁴。于是对原base-cube选中endpoint tuples Γ_Q且BL(1,R)≤A_B，有所需lower A_B^(−1)|Γ_Q|^(5/8)。quotient maps与B_i因singular values统一可比只差固定因子；物理δ-grid全局用R≈δ^(−1)，局部用R≈ρ/δ，须分别对应积分域。本节独立核原count与符号指数，不声称重证其高级KBL theorem。

每个family可用所有原endpoint points作label，N_i≤K|E|≈_Kδ^(−5+κ)。给定base p、endpoint p_i、gap≥r，T_i方向在secant的O(δ/r) ball内；原Φ_p的κ-AD upper及有限witness重数给每arm最多K^C r^(−κ)原T，四臂fibre≤K^C r^(−4κ)。若good-BL raw tuples在K^(−C)比例base上逐p占K^(−C)比例，则去T labels后

    |Γ_p|≥K^(−C)r^(4κ)δ^(−4κ−4)。                  (9)

若只知global goodmass，先按base密度重筛支付其实际比例，或用已知max Γ_p及x^(5/8)≥x/max(Γ)^(3/8)得lower；不能以concave Jensen逆推逐p lower。

将(9)、base数δ^(−5+κ)与ZK的endpoint family upper比较，所有physical δ⁵因子两边相消，得到

    A_B^(−1) K^(−C) δ^(−5+κ)
       ·[r^(4κ)δ^(−4κ−4)]^(5/8)
       ≤C [Kδ^(−5+κ)]^(5/2),
    δ^(5−4κ)≤A_B δ^(−O(η+ακ))。                   (10)

所以即使尚未证明的good-BL比例和A_B≤δ^(−a)都成立，这张global endpoint账本也只给κ≤5/4+a/4+O(η+ακ)，不是κ≤ζ。若maps全在同ρ-world，还须结合(7)或同步frame费用，不把A_B取常数。普通Kakeya的已有4D finite/KT种子并不自动适用于这个任意jointAD/CW类，不能据数值3.75宣布此类的新界或与其全部baseline关系；本轮更没有证明goodmass，故不登记条件算术为新成果。

## 8. 本轮实际出口与停止边界

已证：同源因子不必导致四臂BL∞的真实有限star及自包含LW判据；local近共同核必付且可达的ρ^(−3)；原used graph中不同arms和分离times的raw质量提取；plane-neighborhood真实近incidence及endpoint fibre/条件global指数。没有证明BL-good原tuple lower，也没有严格κ saving或完整source反例。

只要本轮actual提取仍缺good-BL质量、或完整计数仅(10)而无目标增益，就按一主轮停止gate，不追加α/ρ/tuple名称。generic校准不升级为positiveκ/Kakeya反例；原CP⇔PM、BSG/action/carry和polynomial-envelope冻结保持。正式审查待root/A全文完成后另写分配review，Goal不缩小。

## 9. 固定rank-separated times的有条件finite桥

root提出的进一步有限桥可严格核验。固定base F0和四个Fi，所有矩阵范数有统一界，并要求包括F0在内的全部相关pair差满足|det(F_i−F_j)|≥σ>0。给fixed times后的**reference**四个φ_i来自原Φ的product law，其slabγ upper为K max(δ,q)^γ；这不是宣实际条件于times后仍独立。

固定φ_i，在Gi的坐标u=(x,t)中，Lj u=A_ij(x−a_ij t)，其中

    A_ij=Fi−Fj,
    a_ij=A_ij^(−1)[(Fi−F0)φ_i−(Fj−F0)φ_j]。

所以φ_j的系数C_ij=A_ij^(−1)(F0−Fj)可逆，s_min(C_ij)≥cσ、||C_ij||≤Cσ^(−1)。条件于φ_i，三个a_ij独立，each strip宽q的mass≤C K max(δ,q/σ)^γ（宽超过1时用trivial1）。记D_i=det[(a_ij,1)]_{j≠i}。

若|D_i|≤τ，或者前两点距离≤√τ，或者第三点到前两点连线的距离≤√τ。对前一种ball事件及后一种strip事件分别条件于另外点，用同一slab cap，得到

    Prob(|D_i|≤τ)
       ≤min(1,C K max(δ,C√τ/σ)^γ)。                 (11)

固定另点后只用一次cap，不需错误地乘两个K。四个i作union bound即可。源ξ误差Oδ使a_ij扰动≤Cδσ^(−1)，|a_ij|≤Cσ^(−1)使D_i扰动≤Cδσ^(−2)。因此τ≫δσ^(−2)时，可用ideal |D_i|≥2τ保证actual |D_i|≥τ；不从原Oδ关系免费变exact。

对actual D_i≥τ，取Mi的三列(a_ij,1)。除去对应kernel列后的2×2行列式绝对值为|det A_ij|·|D_i|。§2条件LW给准确费用

    C_i=|D_i|^(−1/2)∏_{j≠i}|det A_ij|^(−1/2),
    BL(B,5/8)≤τ^(−1/2)σ^(−3/2)。                  (12)

它是scale-invariant upper，故也控制所需regularized常数（再作quotient固定比较）。例如σ=δ^a、τ=δ^β，先取2a<β<1−2a，再η≪γ(β/2−a)，可同时付source误差、bad概率及BL费用δ^(−(β+3a)/2)。这些参数预留相容，但没有证明source time-rank事件的质量。

实际arm law可不独立：保留base row后，原(T,endpoint-time)有限选择law被K^C倍的“原uniform Φ_p × full δ-time-grid counting probability”支配，来自per φ-bin/time witness O(1)及row/endpoint lower。四臂作原真实product choices，仍有K^C domination。若rank-separated time tuples在实际raw law中有质量g，则bad-angle质量≤K^C乘(11)，选参数使其≪g便能保good-BL质量。该upper允许原angle/time相关；reference好time质量不能反推actual g lower。若另有相关bounded g核，使用其原未归一化质量，不能忽略相应denominator。

本桥真正在有限数据上把“rank-separated times＋原slab upper”送到定量BL；它不是新的source公理，亦未证明所缺的actual time-rank lower。即使将来g已付，当前endpoint计数仍只有(10)，故本轮没有κ≤ζ。停止边界不因这个有限桥改成继续调a/β/σ。
