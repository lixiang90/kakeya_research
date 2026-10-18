# R0078：fractional算子原质量、全尺度输入与真实稳定锥出口

2026-10-18，B，阶段II。仅编辑本授权稿，恰十二个编号二级节；不Git／元数据／下载／spawn。working_spec第2节已先锁三目标，A负责actual retained-h BSG与共同X，本稿负责第二、三目标及其反攻。首次落盘不把A尚待完成的第一目标默认为公设；最终须actual全文互审。具名wholeproof未全部重新独证，未经外部同行评审。

## 1. 完整原输入、独立满秩尺度与三个质量

原输入为bounded Def17 matrix33 kappa1，原T/N/CW、Y/X/Phi/xi及coherence不改；R76真native模型保每选管全部S_T、exact细g<=1、q=Eg>=delta^C(a+b+eta)。固定原t,s，h=s-t、A=F_t-F_s，|h|、smin A>=sigma=delta^b。令lambda=(u-t)/h、M_u=(F_u-F_s)A^-1。

本轮只处理独立选定的

    U_r={dist(u,{t,s})>=sigma，
         smin M_u,smin(I-M_u)>=delta^r}。

反设q_*=E(g1_Ur)>=delta^a q，否则仅此子支质量小。r在He的有限epsilon之后取小，绝不是从R77固定d=1/50的余集免费取得。记beta0=b+r、H0=C delta^-C beta0、H=C delta^-C(a+b+r+eta)；H含所有fixed conditioning和q损失，不能改写成只依原eta的K。source原K仍为C delta^-C eta。

阶段II第一目标的U'将是原clock中的集合、nu(U')>=H^-C，且原g在真实rectangle与U'上保H^-C的绝对产品参考质量。它不等于全T近满选管；原delta²单块质量不重置。本文第二目标的T-ball cap则对原Uniform_Z直接成立，不用free conditional time law。

## 2. 需要的uniform非拟合准备是已付源推导

固定gamma，再固定epsilon0、theta及rho0，均与后面的mu、a,b,r无关。对任一完整参数eta_src的whole-time配置，只要原allowed rho满足delta^(1/4)<=rho<=rho0、eta_src<=c_N log(rho)/log(delta)，R77第3–4节实际证明：命中数>rho^theta rho/delta、误差rho^(1+epsilon0)的all-real matrix fits所在whole rho-windows，合计原time质量<rho^theta。

为核统一性，慢fit由19.4的单anchor cluster给CW>=delta^(C eta_src/gamma) rho^(Ctheta/gamma-epsilon0/3)。快fit的真实span迫|R_J|<=C rho^-theta；若bad窗比例>=rho^theta，其fit并比例>=c rho^(2theta)，故good-q/V/own-H代价K_fit=delta^-C eta_src rho^-Ctheta。物理二次KT取L≈rho²|R_J|、Delta≈rho^(2+epsilon0/2)|R_J|，R_J在L/Delta消掉；最后迫rho^(-epsilon0 gamma/2)<=delta^-C eta_src/gamma rho^-Ctheta/gamma。theta先固定小、eta_src/mu再小即可矛盾。

此处并不调用nearimage的linewise结论；只是R77已实际付的**一般F非拟合准备**。all-real扩展由原V／own-slab／物理KT承担，非literal20.2的bounded-Mat改字。own-slab最小宽、短clock和Delta的floor以eta_src/mu、theta固定小及delta<=rho^4支付。删bad窗后的witness不改原allowed格；只有下一节的whole-time S反设才改参数并取子格。

## 3. Fractional矩阵恒等式与真实条件数

在U_r上C_t=(1-lambda)M_u、C_s=lambda(I-M_u)皆可逆，定义

    T_u=C_t^-1 C_s
       =lambda/(1-lambda)(M_u^-1-I)。               (1)

u离两anchors及|h|>=sigma给|lambda|、|1-lambda|在[ c sigma,C sigma^-1 ]内。F bounded、A^-1<=sigma^-1、两smin>=delta^r，故T_u、T_u^-1、M_u、M_u^-1的norm均<=H0，放大固定幂不改notation。T_u不是仅norm有界的自由算子，它与同一个原clock的lambda有(1)的刚性关系。

令f(u)=(1-lambda)/lambda=(s-u)/(u-t)。若D为一个nonempty e-ball的中心、0<e<=1，则|D|<=H0。对u属于S={u∈U_r:|T_u-D|<=e}，有

    N_u=I+f(u)T_u=M_u^-1，
    G_D(u)=F_s+[I+f(u)D]^-1 A。                   (2)

这里G_D只是反设中用的有理时间函数，不将原F加rational假设，也不先在所有real times宣分母有界。后文逐实际S-anchor控制分母。

## 4. Pole与局部C²：在原anchor处建立，不能口头删极点

选S中的任一u0。真实M_u0的norm<=H0，故smin N_u0>=H0^-1。若e<=c H0^-C，则|f(u0)(D-T_u0)|<=H0 e足小，N_D(u0)=I+f(u0)D可逆、inverse norm<=2H0。u0离t至少sigma；在|u-u0|<=2rho、rho<=c H0^-C内，仍离t至少sigma/2。

f的前两导数由h/(u-t)求导显式控制为H0固定幂；N_D的norm及其前两导数亦然。Neumann比较使该整窗口内smin N_D>=c H0^-C。逆矩阵导数

    (N^-1)'=-N^-1 N' N^-1，
    (N^-1)''=2N^-1 N' N^-1 N' N^-1-N^-1 N'' N^-1

因此给||G_D||_(C²窗口)<=H0^C。此保证是每个实际S-anchor统一的，不要求原S填满区间、不用S与原g独立，也不把可能位于S外的pole忽略为measure0。

在S cap J中，逆矩阵resolvent恒等式又给|F_u-G_D(u)|<=H0^C e。因此同一rho-window J任选S-anchor作Taylor，有all-real R_J,U_J满足

    |F_u-uR_J-U_J|<=H0^C(e+rho²)， u∈S cap J。      (3)

R_J可很大，(3)进入第2节的是已另付all-real几何，不是bounded slope版本。

## 5. 原S限制、newallowed与统一T-ball质量上界

固定小d0>0，例如d0<1/50。拟证存在固定tau>0、C，使delta^d0<=e<=1时

    nu_Z(S)<=C K^C delta^-C(b+r) e^tau。             (4)

coarse e使右侧>=1时结论平凡。反设p=nu(S)大于右侧，并将其fixed prefactor幂统一加大至delta^-L(eta+beta0)。记d_e=log(1/e)/log(1/delta)。非平凡情形给eta+beta0<=tau d_e/L；R22保完整S-time层、原T/N/CW及各层全部数据，eta_src<=C(eta+log(1/p)/log(1/delta))。由反设的负(eta+beta0)项，或直接合并上述两式，得到

    eta_src+C_pole beta0 <=C1 tau d_e。             (5)

参数eta_src取原eta整数倍，newallowed为oldallowed子格。先固定B0>10，取目标rho_*=e^(1/B0)，选newallowed上邻rho。其指数mu=log(1/rho)/log(1/delta)与d_e/B0差<=C eta_src。先tau足小，(5)给

    d_e/(2B0)<=mu<=d_e/B0，
    eta_src/mu小于第2节阈值， beta0/mu任意固定小。

故rho<=cH0^-C，且H0^C(e+rho²)<=rho^(1+epsilon0)；同一预算确保e<=cH0^-C。e>=delta^d0及B0大给rho>=delta^(1/4)，e固定足小给rho<=rho0。较粗固定e再用(4)的常数概率界处理。这里mu随e变化，但epsilon0、theta、B0、tau均先固定，不依mu回选。

在完整S配置中，原time下界#S>=delta^(eta_src-1)。少于2rho^theta rho/delta点的light windows总共只有C rho^theta/delta个times，比例<=C delta^-eta_src rho^theta=o(1)。余窗都因(3)成为第2节的bad窗，并承载至少一半S；这与bad窗质量<rho^theta矛盾。遂得(4)。平均marks由整层源闭包重计，逐管S_T不被宣限制后仍nearfull；本证明不需要该错误断言。

## 6. 粗端、fine floor及rank参数的顺序

(4)不外推e<delta^d0。若e很粗，prefactor K^C delta^-C beta0 e^tau>=1就只用概率<=1；非平凡e才以(5)同时付newallowed、无pole和Taylor。若e球空则无需选D或G_D。tau和d0固定于完整source及其具名工具，与原选管的a,b,r无关。

后续He先取kappa_op<=tau d0/8，再取其epsilon_H；之后才选r以及a,b,eta，使所有H固定幂<=delta^-epsilon_H/100。不能拿R77的固定1/50阈值藏conditioning。本轮U_r可能不是R77余集全部；其质量是假定q_*>=delta^a q后作结构归约，否则只记录这一子支的质量小。

source allowed rho的上邻费已在(5)中付，而不是在每个e上任选无来源尺度。delta floor只使用delta<=rho^4；T模型O(delta H0)的physical输出误差属于A的metric BSG，不用本节cap将其冒O(delta)绝对常数。

## 7. 原mass到算子族所有尺度coverlower

待A第一目标实际提供U'⊂U_r、nu_Z(U')>=H^-C及u0∈U_r。置T0=T_u0、S_u=T_u T0^-1，算子集合mathcalS={S_u:u∈U'}保distinct值，但查询始终用原time质量。因此不因重复Tu而免费改用uniform distinct prior。

S-ball半径ell的原inverse落在T-ball半径||T0||ell<=H0 ell中。先取ell>=ell_*=delta^(d0/2)。该查询半径不小于delta^d0；大于1时用平凡界，(4)的prefactor可统一吸收。对任意ell-cover求和得

    N_ell(mathcalS)>=H^-C ell^-tau， ell_*<=ell<=1。 (6)

对delta<=ell<ell_*只用单调性：N_ell>=H^-C delta^(-tau d0/2)。取kappa_op<=tau d0/8及H足小后，这在全部delta<=ell<=1给

    N_ell(mathcalS)>=delta^epsilon_H ell^-kappa_op。 (7)

ell>=1时非空即可；mathcalS norm<=H^C。fine段是降低指数后的真实coverlower，绝非把(4)的Fst ball cap补到delta。原U'质量H^-C、K和T0 conditioning都在(6)的H中，未乘遗漏的原delta²选管损失。

## 8. He其余输入与共同X的实际验收标准

He1611.09639v2 Th3已实际读原声明和相关proof入口，取n=2、sigma_X=3/2、kappa<=min(1/2,kappa_op)。先得epsilon_H，再缩小它保epsilon_H<kappa/100。A须从真实g而非假定独立卷积构造X，满足

    X⊂B(0,H^C)， N_delta X<=H^C delta^-1，
    N_ell X>=H^-C ell^-1（或足以推出(7)的同型降指数），
    N_delta(X+X)+max_(u∈U')N_delta(X+S_uX)
       <=H^C N_delta X。                            (8)

all-scale lower应由X包含／覆盖原Y_t的大子集及其AD upper直接计得；不能给active子集ADlower。若coarse／metric构造只到delta H，必须在更细ell用单调性并降低kappa，不能省掉这一段。upper H^C delta^-1小于delta^(-3/2-epsilon_H)，norm和(7)也在a,b,r,eta后小的同一预算内。

(8)的A第一目标首次落盘尚待其证明与actual全文互审，本稿不将其作为新外加公设收轮。尤其weighted-anchor的BSG必须保h rectangle质量，manyu在同一A0×B0的密度、第二BSG及Ruzsa共同X都要真付。若它们失败，本稿只能保(4)／(7)及给定(8)的后果，完整phaseII判未达。

## 9. Contrapositive返回原矩阵的完整量词

若A实际付(8)，且mathcalS为delta^epsilon_H-irreducible，He的六项输入均满足；其growth>=delta^-epsilon_H N_delta X却反(8)，因为H^C<<delta^-epsilon_H。因此存在同一line W，使每个u∈U'、每个w∈W都有

    dist(S_u w,W)<=delta^epsilon_H |w|。             (9)

这不只是有manyu各保不同line。取unit v0∈T0^-1 W、unit row ell垂直W；|T0v0|∈[H0^-1,H0]，(9)给|ell T_u v0|<=H0 delta^epsilon_H。代(1)，lambda比率的inverse和|detM|上界都只付H0固定幂，得到对**全部原u∈U'**

    |ell adj(M_u)v0-(ell v0)det M_u|
       <=delta^(epsilon_H-C(b+r))。                (10)

linear系数的Frobenius norm为|ell||v0|=1，所以(10)不是恒零多项式；但它是带det的二次cone，而非共同像／核。若要直接写原F，乘detA得

    |ell A adj(F_u-F_s)v0
         -(ell v0)det(F_u-F_s)|
       <=C delta^(epsilon_H-C(b+r))。              (11)

此时linear系数下界仅sminA>=sigma，归一若需再付sigma^-1。U'的原time质量和原rectangle g质量由A回传，不能称全Z都满足(10)，更不能改为R64 raw全pair small det。

## 10. 两种稳定line校准：不等于nearimage或commonkernel

先给有界diagonal模型。取t=0、s=1，F_s=0、F_t=I，并在u∈[1/4,3/4]令

    M_u=F_u=diag(1/4+u/8, 1/2+u²/8)。

M、I-M uniformly fullrank，T_u为diagonal、T_u T0^-1保两coordinate lines。不同u,v的M差为diagonal两entry皆非零，所以没有共同像／核的rank1差结构。T的第一entry严格单调、derivative固定正下界，Uniform delta-grid clock甚至给point-ball cap C(e+delta)。故point cap、fullrank和He稳定line可以同时成立，不能用前者直接宣布不可约。

再看W0≠W的真正二次情形。固定z=1/2，x(u)=1/4+u/8、y(u)=1/4+u²/8，令

    M_u=[[1+x y,x z],[y,z]]。

detM=z、det(I-M)=-xy皆远离0，且M−diag(1,0)=[[xy,xz],[y,z]] rank1。M^-1−I的第一column为(0,-y/z)，所以T_u e1沿e2，S_u保W=e2而W0=e1。取ell=e1^T、v0=e1，(10)精确为M22−detM=0。两time差的det=-z(x_u-x_v)(y_u-y_v)非零，仍非共同像／核。为使原F entries在[-1,1]可取A=I/2、F_u=M_u/2、F_t=A、F_s=0。

两例仅是出口代数的校准：可在其余固定clock段作bounded smooth延拓，但小rho-window Taylor误差O(rho²)不保原local SM；未构造共同X small sums、完整T AD4/CW、filledX、selected Phi/xi或真实g。它们不反本轮完整source结构归约，更不是Kakeya反例。禁止沿其proper smooth参数继续新轮。

## 11. 反攻、restriction及与旧冻结的严格区别

Tcap使用原whole-time集合S重建完整source，并非原native block的条件gclock；原T和CW分母从未改。A共同集只来自真实fixed native endpoints与带权anchor h，不能先取manyu各自BSG subsets再强求交。U'所保原g质量不授其逐管dense，不授active Y的ADlower，也不授两个端点或times独立。

scalar族和triangular族可有大量算子并全保line；complex族是否不可约须按He原condition逐项核。T-ball cap只付He coverlower，不能冒CSWZ model-hyperplane spreadout。若W0=W，(10)仅变成ell M v0≈0，仍是共同linepair／triangular限制；W0≠W若ell v0很小，不可除它而免费得到bounded projection中心。保留(10)的未除多项式可避免该condition数漏洞。

当前native作用表示是R2上实际T_u T0^-1，不是R28有trivial quotient的R4自然shear；但除非共同X由原图实付，这一点仍只是名称区别。R18/28/free BSG、更多anchors、R64 raw全对、R72 basicness、R77 NI常数优化继续冻结。新实际结构若通过也不等于完整growth或ordinary界，不新增数学ID。

## 12. 首次落盘的实际阅读、互审责任与停止

已actual全文读R78 spec5最新三目标、opening macro6、phaseI A8/B7，及R77 root14/A12/B12和其actual source非拟合准备、R22 whole-time闭包；又实际读本地He1611.09639v2 Th3及small-sum contrapositive用法。没有下载／重核官方bytes，未冒外部wholeproof全部复证。

本稿完整自证的是原T-ball uniform质量、pole／Taylor／newallowed及全尺度operator coverlower，以及He所有输入与真实原cone返回。随后已actual全文读A阶段II12节及root整合14节：A第3节坏pair／sqrt-epsilon删选与Q'余邻居给retained p^6边、p^11三路径；第4节原细label的H² cell-triple重数与J³／原规模分母正确。weighted h阈值真的保原rectangle质量，未以大vertex数替代。第8节两次Ruzsa triangle显式保N_delta(T_u B_u)压缩分母；第9节A0的cover经S_u后、3Z_u-3Z_u给同一个X全部small sums；第10节X含A0平移，仅用原完整Y upper便付全部尺度lower。这一非自推第一目标已逐式核完，无未解决必修。

root14第9–13节的dimensionless负(eta+beta0)预算、原S／newallowed、每anchor无pole及Taylor、heavy窗反一般NF、fine floor单调降指数、He全输入和原F多项式回写均与本稿独立链一致。B自证部分由root/A另作独审，不计自己的独审。当前完整三目标在所列原source与具名输入范围内通过本次交叉核验；正式review、终macro／next另待授权与actual全文读取，不预认证元数据或Git/sync。

此结论仍只是有原质量的共同作用集与fractional稳定cone alternative，没有满秩质量saving或完整growth；不宣完整kappa1／ordinary／major。按先锁spec保守主gain noinfo1，停止BSG／Ruzsa／rank常数优化；具名wholeproof保留，未经外部同行评审。
