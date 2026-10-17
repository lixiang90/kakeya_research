# R0059：原共同核审计与三维图形–PW联合接口

2026-10-17，A。已读 GOAL／STATE／ROADMAP、registry 全78项状态、R58 round／next、R59开轮spec／macro及正式转题§7；实际重读WZ Def17.2–4、21.2／Remark21.3、Choudhuri §4、Zahl §3.1与GWZ主定理和Lemma3.7。仅编辑assigned文件，不Git／spawn。以下外部定理为具名输入，其wholeproof没有由本轮认证；本项目推导未经外部同行评审。

## 1. phase I原共同核：正确上界与尚缺lower

完整Def17的d5、k=ell=3、κ≥ζ>0、γ>0配置中，若 f(z)=F0+u(z)eᵀ，经共同bounded shear与水平rotation可取F0=0、e=e1。原grain点为

    (x1,x2,y+u(z)x1,z)，y∈Y_z，x∈X_(y,z)。           (1)

删除x2保原clock，原整直管投为R4整直管。kernel点占据不自动成为同一投影管的label占据：ξ_p可依x2；Def17.2的coherence仅比较同物理粗格内ξ，未给沿整kernel纤维常性。

原joint4-AD与whole-CW已给商参数3-Frostman **upper**。一个商r-bin的整管恢复bounded x2后落在R5凸棱柱，体积O(r³)，故原概率≤K^C r³。每个occupied lifted r-bin由AD4 lower带质量≥K^−C r⁴，因此该商bin至多K^C/r个lifted bins。这个方向不新；未付的是典型纤维至少K^−C/r，从而商3-AD lower／support≤K^C r^−3。CW只迫商support至少K^−C r^−3。

另一方面，原marked footprint确有上界：每个z的商点由一维x1和Y_z参数化，故N_δ(πE)≤K^C δ^(−4+κ)。若真能以subpower损失提取商joint3-AD及原dense marks，便可能调用原四维sticky输入；本轮没有支付这个提取。固定φ1后把角集κ质量放到φ2条件law也非法：原Φ可为斜Cantor graph，slab upper不保证该条件law非原子。

WZ21.2／Remark21.3允许A、B的更高维generic projection，但乘子C仍标量；不是随意vector multiplier定理。它也不能只凭Y维数2−κ自动排任意κ>0。B的κ=γ=0与unused-label padding只校准“whole T自动3AD”过强，不是完整正κ配置反例。phase I据此停止，未作为本轮完整主成果结案。

## 2. 正式选题及来源历史

R59 spec§7正式改为：固定n≥5、格式A、R,C、ε>0，S=S_δ⊂B_R⊂R^n为实半代数维数≤3、格式≤A，系数可依δ。N根unit δ-tubes的物理方向δ-separated，整轴在N_(Cδ)S；Y_i⊂T_i任意可测，平均密度

    Σ_i |Y_i| ≥ δ^η Σ_i |T_i|。                    (2)

欲对η足够小、δ后足够小证明

    |∪_iY_i| ≥ c δ^(n−1+ε) N。                     (3)

不预含任意原权／方向帽α推广，也不预称全λ³估计。整label删选保原逐管shading；对shading另作限制则只保实际重新计算的密度。

实际触发源是早于本轮已入库的Mukul Rai Choudhuri arXiv2610.12480v1 §4 Prop17／Lemma19。R33已核其声明／scope，R59首次详细使用该节联合空间测试；fresh官方bytes与旧件SHA256 d7e2f0bf…一致，不增加PDF／source数。其Lemma19只写R4余维一，Prop17只显示whole-tube union，不能字面当(3)。本轮用原PW测试H∩π^−1(U)，因此与R55只索取projected angular cap的失败接口不同。

精确本地位置：Choudhuri PDF5–7，txt245–265为Lemma19，268–308为Prop17证明，314–363为图形分解证明。官方primary为 https://arxiv.org/html/2610.12480v1 。本轮不以该文R4数值结论作普通高维已解或最优性认证。

## 3. 真正需要的图形引理与引用修复

所需引理：固定n、A、R，存在J,L,A′仅依这些参数，使任意上述S可由≤J个半代数Γ_j覆盖，Γ_j格式≤A′；每个Γ_j在某个正交坐标投影π_j:R^n→R³下为全局L-Lipschitz图。domain可低维、非凸或非闭。所有常数不依δ或多项式系数height。

Choudhuri从切空间斜率界直接引用Zahl Prop3.6时，有一项省略的域准备：Zahl实际命题要求域是regular L-cell。普通CAD cell或连通域上的bounded derivative单独不足以给global Lipschitz；绕长孔洞的短弦不能用直线积分。这里明确补正则域分解，不把该省略冒原定理反例。

Zahl primary https://arxiv.org/html/2307.05894v3 §3.1，Definitions3.3–3.5、Prop3.6：regular L-cell上的C¹ L-function是n!L^n-Lipschitz。其Lemma3.10另带小投影坏集，不是精确全覆盖的现成替代；坏集不能免费丢掉所有原marks。Zahl的曲线maximal主定理不是本轮输入。

用于精确补全的具名几何输入为Wiesław Pawłucki，*Lipschitz cell decomposition in o-minimal structures. I*，Illinois J.Math52(2008)1045–1063，作者2007-09-04 preprint https://modnet.imj-prg.fr/preprints/papers/archive/47.pdf 。已实读PDF1–3的Prop1及Theorem3_n声明／算法范围（本地text71–97、104–122亦读回）；没有声称重证20页wholeproof。Theorem3_n把任意open definable域分成regular M_n-cells与lower-dimensional residual，仅须空间坐标permutation，M_n只依n；Prop1给任意L-function在每regular M-cell上的global Lip≤n!M^(n−1)L。

## 4. 固定格式的一致性：不添加系数下界

上述正则域输入可按固定semialgebraic格式统一piece数与各piece格式。一个严格的存在性理由如下：若固定原格式下不存在统一界，取越来越坏的系数序列并作非主ultraproduct。所得real-closed field上的纯半代数结构仍o-minimal；原公式格式固定，得到同一open域D。Pawłucki定理在该field上给有限个regular M_n-cells，使用有限标准长度公式和有限个field参数。覆盖、regular边界C¹／导数界、lower-dimensional residual及global Lipschitz均可用一阶断言表达。把这有限公式及参数按Łos回传，则原序列几乎处处具有同一有限piece数／格式／M_n，矛盾。

这里lower-dimensional residual在open R^m域中可表达为closure无内点；一般半代数维数的投影判据同样一阶。每个定义式由real-closed-field量词消去换成固定格式无量词式。此论证只证明某个有限C_(n,A)，不声称degree的最优多项式依赖。允许tiny／large coefficients，δ只是系数参数，不增加变量阶数或格式。

## 5. 一般n中完整global图分解

先按有界格式半代数stratification把S分为C¹ manifolds M，m=dim M≤3。固定p∈M，取TpM正交frame矩阵Q。Cauchy–Binet给

    Σ_(|I|=m) |det Q_I|²=1。

故有一个m坐标集合I，其投影π_I在TpM上最小singular value≥c_n。按此判据分成有限半代数区域，在每个相对内部保持该界；边界维数下降后留待递归。π_I为local diffeomorphism，其离散半代数fibres有统一有限card。对其有限-to-one图关系作CAD／definable选择，可分为有限个open D⊂R^m上的C¹图F:D→R^(n−m)，其余图关系维数<m。微分逆界给||DF||≤C_n。

对D应用§3–4正则域分解。只permutation基坐标不会增加||DF||；对F每个分量用Pawłucki Prop1，得到Γ={(x,F(x)):x∈D_ν}的全局L_(n)-Lipschitz界。D的剩余lower-dimensional部分和先前CAD边界对应到S中仍维数<m，重新stratify并从头选坐标投影。每次维数严格下降，至多4层，连同m=0点层全部覆盖S，没有把奇异／boundary层按Lebesgue零测免费删除。

最后把m基坐标I补到3坐标集合J。若Γ为I坐标上的L图，则π_J在Γ上单射，而且|x−x′|≤|π_Jp−π_Jp′|；余下坐标差≤L|x−x′|。所以Γ仍是π_J:R^n→R³上的global L图，只是domain维数m≤3。需要时取closure仍global Lip且格式有界。由§4，各层piece数／格式对δ系数统一，得到§3的引理。

## 6. 正常纤维upper与任意joint凸测试

令H_j=N_(C′δ)Γ_j∩B_(R+2)。取C′固定足够大，使整原δ管落在∪H_j。H_j经存在量词定义距离，仍固定格式；非闭Γ可先closure，不改变所需upper。对任意z∈R³，(π_j)^−1(z)∩H_j的正常(n−3)维体积≤Cδ^(n−3)：与该fiber相邻的任意两个graph点的base距≤2C′δ，global Lip迫其正常坐标距≤2LC′δ，故整fiber落在O_L(δ)球中。

于是任意可测U⊂R³有

    |H_j∩π_j^−1(U)|≤Cδ^(n−3)|U|。                 (4)

这是fiber upper，绝不是lower；domain有孔洞、dim<3、boundary、tiny coefficients均不影响。若U是John外接长方体，它与H_j交为统一格式半代数集，任意转向／轴长／平移只改系数。

## 7. 任意平均marks、global Lip和非短投影

由(2)删掉密度<δ^η/2的labels；保留的labels数≥cδ^ηN，每条完整Y_i仍在。每条管选一个j(i)使|Y_i∩H_j|≥cδ^ηδ^(n−1)，再取同一j的labels数≥cδ^ηN。这里没有假shading含时间interval，也没预设共同短clock。

每管选两个实际shaded points，使用未clamp的正交坐标s(q)=v_i·(q−a_i)，其坐标间距ℓ≥cδ^η。这由每个s-level截面体积≤Cδ^(n−1)及Y_i∩H_j原体积推出；圆端帽仍用该未截断坐标，不将其正体积映到端点单值。令v_i是unit方向，全局graph界给

    |(I−π_j)v_i|ℓ ≤ L|π_jv_i|ℓ+Cδ。

η<1、δ充分小时δ/ℓ=o(1)，从而|π_jv_i|≥c_L。故原整轴投影仍为固定正长度的直轴，而非极短片；不需把图形拉直为非线性空间映射，也不需短clock异向重缩。将其投影包入固定δ参数网的unit C_Lδ-tube P_i，常数尺度差／端帽可通过固定homothety及沿同直轴延长包络支付，所保实际marks不删除。

## 8. 原PW→绝对三维convex Wolff

设U⊂R³凸且包含若干P_i。若|U|有限且包含实心tube，取John ellipsoid外接长方体Q，U⊂Q、|Q|≤C|U|；无穷体积时计数upper平凡。测试S_U=H_j∩π_j^−1(Q)满足(4)。每个所计原i有|T_i∩S_U|≥|Y_i∩H_j|≥cδ^η|T_i|。任取小σ>0，具名一般n方向分离PW给

    #{原 i:P_i⊂U} ≤ Cδ^(1−n−σ)·δ^(n−3)|U|·δ^(−nη)
                   = Cδ^(−2−σ−nη)|U|。           (5)

PW查询cδ^η≥δ在η<1、δ后足小成立。使用原实体marks来证明intersection比例，不要求一条整管在单Γ_j邻域，也不把global|NδS|当joint测试。

(5)直接是absolute convex count；不需要声称投影方向δ-separated。若只先证明rectangular linear Wolff，同一John box论证可以转convex；含单位实心tube的box长轴≳1、两短轴≳δ，所以其clipped体积比较合法。源Choudhuri Th15中的δ^−σ不能漏掉，其Prop17显示时的常数省略不能按精确无loss复用。

## 9. GWZ实际具名输入、重复与normal回传

实际读GWZ2601.14411v2 PDF1–2、6–7（本地txt35–85、279–358）。Th1.1：任意β>0，存在η_G>0；R³ unitδ-tube集合若绝对Δ_max=sup_convexU Σ_(P⊂U)|P|/|U|≤δ^−η_G，任意可测平均shading密度≥δ^η_G，则union≥δ^β δ²#P。它不是normalized Frostman CF结论。其Lemma3.7记录arbitrary Δ_max的乘性损失；本轮只用主定理及显式去重，不默认任意重复indexed family满足“set”。wholeproof仍具名。

由(5)对单一网格tube U=P查询，原相同包络multiplicity≤Cδ^(−σ−nη)。每bin取任一assigned代表仍保逐管cδ^η质量；distinct包络数N′≥cδ^(σ+(n+1)η)N。固定近邻着色可再得essentially distinct，不用投影方向分离。其Δ_max仍≤Cδ^(−σ−nη)。

令E_j=(∪Y_i)∩H_j，定义真实fiber积分

    f(z)=δ^(−(n−3))∫_(π_j^−1(z))1_(E_j)，0≤f≤C。

Fubini给每条代表∫_(P_i)f≥cδ^ηδ²。取统一τ=c0δ^η、c0充分小，则Y′(P_i)=P_i∩{f≥τ}有密度≥cδ^η。令F={f≥τ}，有

    |∪Y_i|≥δ^(n−3)∫f≥δ^(n−3)τ|F|。               (6)

这是从原质量和fiber upper构造真实level shading，然后回传；不是把projected union体积直接乘δ^(n−3)的非法fiber lower。包络unit长度和B1范围可先共同固定homothety，再沿同轴扩为unit tube；contains新包络⇒contains旧投影，因此(5)仍保，原marks在内、密度仅损常数。

先取β<ε/3，再取σ<min(ε/3,η_G/4)，最后取η使nη+σ<η_G/2、(n+2)η<ε−β−σ，并令δ足够小吸收固定常数。GWZ与(6)给

    |∪Y_i|≥cδ^(n−1+β+σ+(n+2)η)N，                (7)

从而(3)。所有参数先后不循环；低维S、δ-dependent coefficients、boundary和任意原可测Y均已覆盖。任意平均λ若不满足δ^η，仅得到另付density loss的有限式，不能由(7)声称全λ³。

## 10. 与R55及完整Goal的关系

R55 product-parabola族的projected angular bin可能有δ^−1重数，与(5)无冲突：同方向不同截距的tube并不都落同一个unitδ-tube。R59的新付项是联合空间凸测试和normal-fiber函数，而非改名索取旧方向cap或复用scalar M3。源Choudhuri §4有原型，所以本轮不认证新颖／major，四维／PW／GWZ外部wholeproof仍为具名依赖。

root最终稿的同证明加强也已核：实际只需原Yi⊂N_(Cδ)S；所有图形选择、PW查询与积分都使用Yi，不使用整Ti近S。heavy Yi非空使对应unit轴仍在共同bounded box内。若原族不是方向分离而已具absolute PW计数常数≤δ^−ηPW，同式(5)将σ换成ηPW即可，前提是该PW对本图形测试的固定格式合法、ηPW也在GWZ容许余量内；这不是免费给任意原族PW。

这只关闭固定格式real dim≤3、原δ方向分离（或明确absolute PW小常数）、任意near-full平均marks近S的局部类。不证明ordinary R5所有管都有这种归属；HRZ真实递归leaf的尺度／marks／重数须另核，不能免费替换其所有terminal。没有把phase I common-kernel提取补成已证，也没有把(3)当general Hausdorff完成。

当前独立主链已写完，待root整合稿／B最终稿／macro／next实际全文后另写assigned正式review；自稿不计独立审查。若后继只是新增regular normal／per-tube density／自由flattening公设，不作为本结论扩张。
