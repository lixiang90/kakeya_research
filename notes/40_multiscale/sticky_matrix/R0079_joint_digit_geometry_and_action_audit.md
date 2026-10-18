# R0079：同一数字载体、原生几何和真实全clock作用的联合反攻审计

2026-10-18，A阶段II。先实际全文读终working_spec5（§2已锁）与B阶段I7，再独立施工本稿。所证是严格联合有限接口模型，绝不是完整Def17或Kakeya反例。没有ordinary新界、完整κ1排除、新ID或重大性认证；外部同行评审未有。

## 1. 量词、参数次序及两种小损失

固定α+β=1、α>β+τ、0<γ0<β、0<τ<1/2，可用(α,β,τ,γ0)=(3/4,1/4,1/8,1/8)。固定ε0∈(0,1/20)、0<θ<ε0τ/100、任意损失要求h>0及固定整数J。先取整数D足大，再取整数C*足大，最后取L为4C*的足大整数倍，使η=C*/L及本稿所有固定倍η小于h。D、C*、L均不随最后B变化。

令B=2^m→∞，m取使B^α、B^β、Q=B^τ、R=B^(1−τ)都是整数且Q可被4整除的倍数；δ=B^-L。允许所有只依L,D,J的常数C_(L,D,J)，B最后足大可将它吸收为一个B因子。几何常数先有C_(L,D,J)B^C，其中幂C可取不依L；提高C*后统一≤B^C*=δ^-η。固定高阶和集的阶数不得随δ发散。

原allowed ρ=δ^(jη)=B^(-jC*)，与dyadic格字面对齐；NF只要求ρ∈[δ^(1/4),δ^η]。不要把B固定后L→∞的另一极限与本量词混用，也不要把B^C误称无损常数。

## 2. 数字集、缓冲D及同一个共同carrier

对s∈{α,β,τ}写

    D_s={Σ_(i=1)^L e_i B^-i : 0≤e_i<B^s，e_i整数}。

取A=D(D_α×D_β)，n=|A|=B^L=δ^-1。D为固定整数，A⊂DδZ²；B足大时其支撑包含在任意预定小fixed box内。令N=E12。对任意b∈D_τ及y,y′∈A，y+(I+bN)y′的第一坐标raw前L位系数至多

    D[2B^α+L B^(β+τ)]≤D(L+3)B^α，

第二坐标至多2DB^β。定义一次固定、与b无关的有限product carrier

    C=D{Σ c_iB^-i:0≤c_i<(L+4)B^α}
        ×D{Σ e_iB^-i:0≤e_i<2B^β}。               (2)

所有digit上限B足大后均<B/8。乘积超过第L位的tail至多

    2DL B^(β+τ−1)δ=o(δ)，                         (3)

因为β+τ<α<1。因此全部y+(I+bN)y′同时落在N_(δ/100)C，B再大即得该固定数值。这里是实际实数乘法的raw系数/尾项证明；不是无carry公设。前L位raw整数已被(2)全部包住，不需要mod B消去真实进位。

|C|=[2(L+4)]^L n，故NδC≤C_L n；C⊂DδZ²仍有Dδ分离。不是为每个u换一张独立小集合。

## 3. 一维digit几何及全尺度AD1

考虑一般L位base-B集，每位连续整数区间长度M_s=c_sB^s，c_s为固定的正整数或固定有界倍；signed区间可先固定平移。只要M_s<B/8，两个不同j-prefix cylinder有间距≥cD B^-j，而单个j-prefix尾部直径≤C_DM_s B^(-j-1)。uniform digit概率在每个prefix上的质量M_s^-j。

故在r_j=D B^-j的尺度，任意r_j-ball只遇O(1)个prefix，而以集内点为中心的r_j-ball含其一个(j+1)-prefix。对相邻r_j用单调性插值，只多付固定幂B；c_s^±L均归入C_L。于是δ≤r≤1时，一维概率满足

    C_L^-1 B^-C r^s ≤ µ_s(B(x,r))
        ≤ C_L B^C r^s                              (4)

的集内lower与任意中心upper。Dδ以下不使用(4)。对A、C和任意固定阶signed-digit product，两个指数相加α+β=1；Euclidean ball与两个坐标interval比较，给(δ,1,C_LB^C)-AD regular，原fine cardinal与δ^-1的差只在C_L。

这也处理总diam随B缩小的粗端：K中保B^C，不能说支撑在fixed大box里就有绝对AD常数。将(4)写成fine标签计数时要乘实际各集cardinality，不能一律误用n替代|C|。

## 4. 任意方向tube-KT，而非仅坐标方向

设矩形长r、宽w，δ≤w≤r≤1。其单位normal某坐标绝对值≥1/√2。固定另一个坐标后，该坐标可用的interval长≤Cw；另一个坐标整体落在长Cr的interval。product概率和(4)给，按normal坐标分别为

    µ(rect)≤K w^αr^β，或≤K w^βr^α
           ≤K r^(1−γ0)w^γ0。                     (5)

若要转N_w，取矩形内原点的Cw-separated子集P。各点周围cw-ball互不交，每个由AD1 lower有概率≥K^-1w；这些ball全部落在固定倍expanded rectangle内。对expanded rectangle用(5)，得到

    N_w(A∩rect)，N_w(C∩rect)
        ≤K^C(r/w)^(1−γ0)。                        (6)

端部扩张、r≈w和w≈δ只增固定常数，K仍为C_L B^C；不能只用upper strip概率便跳到cover数。式(6)是所有方向的原native tube-KT。A0=B0=A的所有保留端点都使用同一原uniform标签，并未从ADlower虚构一个新的独立prior。

## 5. X、固定高阶和集及全部small actions

X=A−A是两个坐标各位完整signed digit区间的product。对固定1≤j≤J，jX每位digit仍为长O_J(B^α)、O_J(B^β)的连续signed区间，且各digit独立可实现；因此

    Nδ(jX)≤C_(J,L)n， N_wX=K^±C w^-1
        (δ≤w≤1)。                                (7)

任选实际bulk u0，b0=b(u0)。由于N²=0，S_u=(I+b(u)N)(I+b0N)^-1=I+(b(u)−b0)N。X+S_uX中第一坐标的product raw系数至多C_JL B^(β+τ)，小于C_JL B^α；第二坐标仍为signed短digit。与第2节同样的tail估计给

    Nδ(X+X)+sup_u Nδ(X+S_uX)≤C_(J,L)n。           (8)

任意固定阶Su的和/积作用亦只增C_(J,L)，因为unipotent乘法的nilpotent系数只是有限次b之和；不声δ相关阶数的闭包。B最后足大使以上prefactor及几何K均≤δ^-h。式(7)是真正全尺度cover，不只有fine cardinal；这里X本身的AD/KT可由显式digit构造证明，未假一般R78 X自动如此。

## 6. 原q/r clock、T-law及global/dyadic连续性核算

bulk time取u=Σd_iB^-i，其中d_i=R q_i+r_i，0≤q_i<Q，r_i∈{0,2,…,R−2}；首位q1限制在[Q/4,3Q/4−1]，其它q/r自由。加两孤立anchor0、1。bulk均在[1/4,3/4]，任两time至少2δ分离，cardinality为固定L倍的δ^-1。Uniform Z的intervalcap≤C_LB^C(|I|+δ)，原均值不改成Uniform(distinct b)。

定义b(u)=Σq_iB^-i。每个q-prefix的time重数相同（首位bulk限制已是完整q-block），所以b-law是相应τ维digit概率。故

    ν{|b−c|≤w}≤K(w+δ)^τ，
    N_w{I+bN}≥K^-1 w^-τ， δ≤w≤1。               (9)

anchors只在operator图中取g=0，损2/|Z|=o(1)。同一原time集合/重复operator权重始终保留。

独立核global Lip：若u,u′第一个不同digit在j位，数字皆为偶数，故|u−u′|≥c B^-j；而q_j之差最多对应R^-1|d_j−d′_j|+1，b尾差≤CQ B^(-j-1)。若d_j差大则直接比较其主差，若为最小2则even-digit cylinder gap仍给cB^-j，均有|b(u)−b(u′)|≤C|u−u′|。同allowedρ-prefix内更直接有|Δb|≤Cρ Q/B≤Cρ。此为实际离散集的证明，不预设可微性。

## 7. bulk F、Ct的精确代数与fine分离

anchors取F0=I、F1=0。bulk取

    F_u=uI−u(1−u)b(u)N， λ=u， M_u=F_u，
    C_t=(1−u)F_u， C_s=u(I−F_u)。

N²=0直接算得C_t^-1 C_s=I+bN=T_u。bulk的F、I−F、Ct及其逆的norm均由绝对常数控制；entries属于Mat字面[-1,1]，B足大时所有native集合亦在该fixed box。Ct随u在同ρ窗口变化≤Cρ；由第6节甚至在bulk原clock上global Lipschitz。anchors不强令此bulk公式连续延伸至0、1，source小allowed窗口亦不会同时碰bulk和anchor。

令Y0=Y1=A，bulk Y_u=C_t(u)C。先定D大于10倍所有Ct逆norm的统一上界；C的Dδ格分离经Ct后仍至少10δ，故这里可直接使用原线性像，不需要会改变cardinality/权的δ-net去重。C的raw tail经Ct只为Oδ，故y+T_u y′到C的共同近似确在原fine δ容差内，而不是一个δH大误差。

## 8. 整窗口coarse AD1的upper与lower

固定allowedρ≤B^-C*的一个dyadicρ窗口J0，先考虑含bulk的情形，取其中u0。Ct变化≤Cρ及C bounded给

    union_(u∈Z∩J0)Y_u ⊂ N_(Cρ)(C_t(u0)C)。       (10)

这给局部coarse upper：任意R≥ρ，利用单个C的AD1及expanded ball，可用≤K^C R/ρ个ρ-balls覆盖union在R-ball内的部分。

lower不能从(10)反推。对任何union的occupiedρ-cell选其某实际Y_u点p；单个Y_u的AD1 lower/upper比较给其R-ball内的ρ-cover≥K^-C R/ρ（R≫ρ取内半径，R≈ρ用非空）。该Y_u包含在同一union中，故union具有coarse lower。于是原wholewindow coarse AD1成立，但没有声该union在fine δ尺度仍AD1。仅含一个anchor的窗口用Y=A直接处理；ρ=1时有限big box比较亦只付K。

## 9. 全clock真实线、同一g及两种密度

对每个exact native pair y,y′∈A定义R5中的真实直线

    x(u)=−(1−u)y+u y′， z(u)=u y′， clock=u。

它的native值满足

    z(u)−F_u x(u)=C_t(u)y+C_s(u)y′
        =C_t(u)[y+(I+bN)y′]∈N_(Cδ)Y_u。          (11)

在anchor0、1处native值分别exact为y、y′；bulk误差只来自第2节显式tail。它是同一条wholeclock直线，不是对不同u拼接不同arms。clock长1，Euclidean长度在[1,C]；本稿不虚称一个长度恰1的axis免费含所有clock，也无需调用PW延长。

取g(y,y′,u)=1_bulk(u)，则0≤g≤1，原Uniform(A)²×Uniform(Z)下Eg→1，且每个pair的原bulk clock都近满。每条所构线也保全部同一bulk visits。这比只证明平均密度强，但没有声原source的point Φ/filled水平grain因之成立。A0=B0=A，h=g_u0 E_ug_u在任一bulk anchor也近1，故同一X、同一smallaction、同一rectangle和原g确可同时成立。

## 10. 共同稳定line、fractional cone及δ尺度范围

T_u及S_u都保W=e1，且在W上的字符恒1，商字符亦恒1。取ell=e2^T、v0=e1，有

    ell adj(M_u)v0−(ell v0)detM_u=0。             (12)

此时W0=T0^-1W=W，ell v0=0，不作除法。所有bulk M与I−M均定量满秩，独立both-fullrank U_r可含全部bulk；T-ball cap和原clock质量由(9)共同给。反之两个不同bulk times的F差是上三角且diagonal皆u−v，故det(F_u−F_v)=(u−v)²，模型不是raw all-pair rank1差族。

式(12)并未迫Y或X集中W，product native集合保持任意方向tube-KT；而active-character增量方法的必要非trivial字符在本例真实失败。这一反攻同时保共同X/作用/原g/原clock及cone，已强于R78仅有光滑diagonal曲线的校准。没有把它说成某个外部定理的反例，因为相关P(G)/irreducibility假设本来就失败。

## 11. 独立检验q/r线cap与all-real局部NF

本节先作独立推导，再在第12节记录对B终稿的实际交叉读。固定完整prefix的ρ窗口，除以ρ并去prefix后，剩N0=L−j位：U=RQ+V、b=Q，其中Q各位0…Q−1、V各位0,2,…,R−2，两者独立；此处符号Q在等式中指digit随机数，整数digit数仍为B^τ。

对任意实a,c，b−aU=(1−aR)Q−aV。若|1−aR|≥1/2，条件V后用τ维Q-cap；否则|a|≥1/(2R)，条件Q后用(1−τ−log_B2)维V-cap，缩放R只付固定幂B。τ<1/2且B大使后指数≥τ。因而相对strip宽w≥δ/ρ，有uniform all-real line bound≤C_L B^C(w+δ/ρ)^τ；不依a预设有界，也不赠q/r条件之外的独立性。

若某matrix affine fit在ρ窗内以误差ρ^(1+ε0)命中≥ρ^θρ/δ个原times，这些δ-separated times跨度≥cρ^(1+θ)。同窗F变化Oρ，故fit的offdiagonal slope≤Cρ^-θ，fit值在整窗bounded。将offdiagonal fit除以−u(1−u)，得到C²≤Cρ^-θ的rational target，Taylor误差≤Cρ^(2−θ)≤Cρ^(1+ε0)。因此同一命中集使b在宽Cρ^(1+ε0)内贴一条实line。

上述cap给命中数≤C_L B^Cρ^(ε0τ)ρ/δ；先选C*使C* (ε0τ−θ)>C+2，再B大吸C_L，严格小于ρ^θρ/δ。所有allowedρ≥δ^(1/4)使该strip宽≫δ，尚有至少3L/4个tail位；fitspan含至少两个点。孤立anchor窗命中至多1，亦小于目标。此证明是原absolute clock计数，不以全局非affine代替NF。B终稿若使用不同字母/较保守常数，应逐项对照而不只接受摘要。

## 12. 完整源缺项、交叉审查状态及停止

本稿同时构造native A/C/Y、同一个X与全部固定阶small actions、近满原g及wholeclock实际线、原operator law、dyadic窗口与局部all-real NF。它仍没有完整Def17输入：实际线由(y,y′)∈A²决定，只有约δ^-2条、参数维数约2；不能以unused padding得到原nearfull active joint AD4族。bulk实际点通常只对应一条构造线，没有point Φ的AD1/slab全角族，也没有filled水平X2、原selected ξ/coherence和全whole-T CW的联合验证。未验证条件不被简单称为必然失败，但绝不授予模型。

局部native AD1与tube-KT、g近满并不能补这些fullsource缺项。因此本轮若所有证明通过，验收仅为对“R78已提取联合接口足以增长”的严格有限反攻，不是source/Kakeya反例、κ1分支saving或ordinary新界。高级具名source proof未重证，未经外部同行评审。

随后已实际全文逐式读root《R0079_joint_native_unipotent_countermodel》12节和B《R0079_native_clock_and_all_real_nonfit_audit》12节。独立核B的q/r conditional law两case、s_R=1−τ−log_B2≥τ、全尺度Tcap取n=L、原time重复权与两anchor处理；even-digit首差gap确给global Lip，所以其NF fit slope实际O(1)、rational target C²也O(1)，比本稿第11节保守ρ^-θ链更强且相容。其linecap查询宽度、k≤L/4的tail floor、C*先于L/B及孤立anchor窗均已实核，无强制项。

root第3节任意orientation的product cap转N_w时确用了support-ball lower与expanded tube；第4节X allscale upper的heavy A-ball平移至2X，是可验证的packing，未把fine cardinal免费外推。其carrier第一坐标仅3B^α也成立：L先固定而B最后大，L B^(β+τ)≤B^α；本稿(L+4)B^α为较宽同型选择。Dδ分离、Ct公式、整窗coarse lower、真实同pair clock及未除cone逐式通过。

本稿主几何由B实际全文独核，root/B独立链与本人正证不重复算自身独审。本轮只得到列明联合接口的严格反攻，完整source缺项不因互审消失；无必修数学修正。只编辑本分配文件，之后按本轮宏观停止本局部inverse/mask参数续链，不以其改名下一机制。formal及最终macro/next范围待parent另授权，不预认证。
