# R0096：原CW观测商、固定多项式法向与有限受限投影

2026-10-19，A。按R96两份五节规格施工，仅编辑本稿。下文证明的是原whole-tube概率的观测商上界，以及固定多项式β的完整source条件应用；不宣称完整mixed42或ordinary增益，未经外部同行评审。

## 1. 实际读域、原对象与旧接口

已实际读GOAL、STATE当前交接、ROADMAP四路及旧冻结记录、registry全部78个ID/status、R95 next及R96 reselection/working各5节。实际全文读R14 primary projection audit、R19 global residual主稿全部6节，R19 source稿的原坐标/质量输入；实际全文读R74 singular-pencil稿10节以独核所需精确compression。原WZ Def17.2–17.4、Remark17.1及相关19.4/19.5输入沿R95实际读域复用，不冒本轮重证其高级wholeproof。

GGW已有原件`R0014_gan_guo_wang_2211_09508_v2`，本轮实际读原PDF对应text §§1–2至Th2.1及随后证明Th1.2的有限推论段；未独证全文decoupling算法。fresh[官方history](https://arxiv.org/abs/2211.09508)仍v2，2024-01-21，v1为2022-11-17；没有重新下载。源§2先固定factorial moment curve，Th2.1的literal形式正用于本稿；一般smooth曲线的finite推广需读其紧邻的perturbation说明和依曲线的常数，不能把printed moment常数当任意δ-dependent族的统一常数。

保持bounded原R5 physical单位δ管、graph参数λ=(a,b)∈R4×R4、原μ=Uniform(T)、原N及normalized whole-CW≤K。原δ分离Z在固定clock盒中，平均selected visits≥K^-1δ^-1。mixed42另供scalar native标签Y_t的δ-cover≤Kδ^(-1+κ)，0<κ<1固定；原观测为F_tλ=n_t·(a+tb)，n_t=(-β_t,1)，V_t=(n_t,t n_t)。K=δ^-Cη，η最后小。既不赠physical方向分离，也不把used family的分母代原N。

## 2. 平均访问到逐原管，完整clock不替换

写m(T)为原selected-time数；m(T)≤Cδ^-1且Σ_Tm(T)≥K^-1Nδ^-1。删m(T)<(2K)^-1δ^-1的轻管，剩H满足

    #H≥cK^-1 N； m(T)≥(2K)^-1δ^-1  (T∈H)。

此后每T保其全部原visits S_T；原ξ、Φ、两grain和标记不重造。若用μ_H=Uniform(H)，则原whole-CW和joint4AD upper至多各乘N/#H≤CK，成为K固定幂。若用未归一restriction，则总质量≥cK^-1、原upper不变，在GGW的μ(total)/c_α比值中相同收费。下文采用前者。

对原每个visit t，tube-to-axis及原native标记误差给

    F_tλ∈N_(Cδ)Y_t。

β有固定界时C固定；对固定polynomial允许C依β，均不依δ。不同管的S_T可以相关、不同，不选独立时钟。若只在事后某interval中找到好曲线而没有该处原访问质量，不能据此套本证明；本稿的polynomial公式覆盖所有原Z。

## 3. 任意五个time的精确观测商，不要高阶jet

取至少五个不同实times J，β_t任意有界，令S=span{V_t:t∈J}、K_0=S^⊥⊂R8、m=dimK_0。取K_0的原Euclidean正交参数化Q，分成两块Q=[A;B]，physical evaluation为A+tB。

每t∈J有n_t(A+tB)=0，而n_t末坐标为1，故rank(A+tB)≤3。若m≤3这本来成立；若m≥4，每个4×4 minor是次数≤4的t多项式，在五个不同times全为零，所以对所有实t恒零。设

    r_0=max_t rank(A+tB)≤3。

这一步只用精确零点，不用Remez，不除J的最小gap，也不声原管曾同时访问这些times或有同label子族。J用于定义线性商，不用于未经支付的incidence提取。若K_0={0}，采用m=r_0=0。由joint(A,B)单射，m≤2r_0；因此非零K_0不可能有r_0=0。以下证明的常数不依S/J/β的conditioning。

## 4. 精确compression在任意m的独立重建

取t_0使rank(A+t_0B)=r_0，先把A换成A+t_0B，再用临时可逆row/column变换写

    A=[I_r0 0;0 0]； B=[C D;F G]。

在小t时I+tC可逆，max-rank给Schur恒等式tG−t²F(I+tC)^(-1)D≡0。于是G=0、FC^jD=0对全部j≥0。令U=span{imD,…,im(C^(r_0−1)D)}、e=dimU。Cayley–Hamilton使CU⊂U，且FU=0。故在这些临时坐标中

    K_1=U×R^(m−r_0)； E=U×{0}，
    dimK_1=m−r_0+e， dimE=e， AK_1+BK_1⊂E。

还原到原空间后，这仍是真实子空间包含关系；A的t_0平移不影响AK_1+BK_1⊂E。随后一律用原Euclidean正交投影，不带临时GL基底的条件数。K_0/K_1的正交补维数仅r_0−e≤3，0≤e≤r_0。ker0边界取K_1=E={0}。此精确Schur论证与R74经典compression相同，不是新分类或需另加goodrank假设的工具。

## 5. 原CW给uniform观测商Frostman上界

令ν=(P_S)_#μ。固定δ≤r≤1及一个非空query B_S(z,r)，选其中一个原参数λ_*。所有query参数可写

    λ=λ_*+k+u， k∈K_0， |u|≤2r， |k|≤C_R。

对K_0中正交补K_1^⊥的r_0−e个坐标作r网，至多C_R r^(-(r_0−e))个bins。在一个bin中，k的K_1部分在physical evaluation始终属于E；余参数误差O(r)。整原axis因而处于某个真实affine(e+1)-plane的Cr邻域，reference轴斜率/位置固定有界。加原round δ厚度、端帽及完整bounded clock后，有真实凸box包含该bin的全部原whole tubes，体积≤C_R r^(4−e)。长轴e+1个固定，短轴4−e个为O(r)。

用原N/CW逐bin求和得

    ν(B_S(z,r))≤C_R K r^(4−r_0)≤C_R K r。                 (1)

大r只改变C_R；S={0}不可能（V含常坐标1），K_0=0时无补参数bin、box体积O(r⁴)，同式仍成立。低m使用同一个精确compression，不要求m≥4。全程没有选择原tube subfamily后重置概率，也没有隐含依J gap、S的singular value或β导数的常数。若先heavy化，则把K换K固定幂即可。这是真正统一于原观测span的upper，但不是每个单time投影的1Fst，也不包含高阶非退化结论。

## 6. 固定多项式系数商与唯一真实条件数

现在额外固定degree≤D的R3值多项式β(t)，其系数不随δ改变。F_tλ是degree≤D+1的标量多项式，写

    F_tλ=Σ_(j=0)^(D+1) c_j(λ)t^j； C_βλ=(c_0,…,c_(D+1))。

原clock经固定affine变换到[-1,1]仅作固定系数换坐标。令S=(kerC_β)^⊥，它等于所有V_t的span；可从一个interval取有限个至少五times生成同一span，D小时重复添加不同times不变。故(1)适用。C_β|S单射，令L=max{1,s_min(C_β|S)^(-1)}，这是固定β的有限常数。若系数落B(z,r)，相应P_S参数落半径≤2Lr的ball（非空时以一个原点为中心），得到

    (C_β)_#μ(B(z,r))≤C_β K r^(4−r_0)≤C_β K r， δ≤r≤1。 (2)

若Lr大于固定chart尺度，用trivial概率≤1并增大C_β；不假L≤δ^-Oη。系数support也在固定β决定的盒中，固定homothety可归一到unit ball。C_β至少rank2，因为限制a_H=b_H=0时常数/一次项可独立取值。D=0包含旧常法向；ker0也无问题。

这是fixed-β量词：η阈值可依κ,D及固定chart，δ_0另可依β/L。对任意δ-dependent bounded系数多项式，非零singular值可能趋零，不能由此宣称统一C_β。也没有从原dyadicLip source提取这样的固定degree/profile。

## 7. literal moment finite GGW与全八维校准

原GGW Th2.1：在ambient n，moment curve Γ(θ)=(θ,θ²/2!,…,θⁿ/n!)，取m=1、0<α<1、finite nonzero Borel μ支持unit ball，c_α(μ)<∞；在完整δ-net上选择短边沿Γ′、尺寸δ×1^(n−1)的标准disjoint plates，且每个support点参与至少cδ^(ε−1)个plates，则

    #W≥c_(ε,n,α) μ(R^n)c_α(μ)^(-1)
                     δ^(-1−α+L_n√ε)， L_n可取10^(10n)。 (3)

μ(total)和c_α同次缩放，不能以归一抹掉heavy损失。只知道定性a.e.投影维数不代替(3)。本稿n=D+2，系数monomial row(1,θ,…,θ^(D+1))用固定diagonal变换对齐Γ′的factorials；其V规范和曲线全是固定的。高级finite theorem具名，不独证其decoupling。

若专取β=(t²,t⁴,t⁶)，原R8的V=(-t²,−t⁴,−t⁶,1,−t³,−t⁵,−t⁷,t)经固定signed permutation就是(1,t,…,t⁷)，Wronskian绝对值为∏_(j=0)^7 j!。这个透明模型可以直接用n=8的moment定理；它只作校准，full8jet不是(2)–(3)一般系数方法的必要条件。相反，任意smooth β若想直接用R8一般curve版，还须固定smooth规范/非退化常数，不能从Γ′=V这个形式自动获得。

## 8. 原系数测度的平滑与全部support参与

用第2节的原H及ν_H=(C_β)_#μ_H，不把同系数的不同原管当无权点。由(2)，δ以上ball质量≤C_βK^Cr；将其与半径cδ的光滑概率kernel卷积得\widetildeν。δ以上仍同upper；若0<r<δ，ambient n=D+2中密度≤C_βK^Cδ^(1−n)，所以

    \widetildeν(B(z,r))≤C_βK^Cδ^(1−n)r^n≤C_βK^C r。

于是每个固定α<1都有c_α(\widetildeν)≤C_βK^C，固定support归一只改C_β。全support中任一点距至少一个原heavy系数点O(δ)；对该原管的每个旧visit，monomial row有固定bounded norm，因此相位只变O_β(δ)。把相应target intervals扩大固定倍后，该点仍参与该管原nearfull的全部times。

这里不需要把一个系数cell的不同S_T取交；取其union已有至少一个heavy管的card lower，而共同W使用所有原labels，允许这种union。原H有限、平滑compact support，使边界support点同样归某个闭Oδ系数球。未产生新的原source配置或独立g。

## 9. 同一fine网格、actual plates和诚实总upper

固定affine clock后，把原δ-separated Z round到完整可比Δ网格，Δ=C_β,Dδ；每个新time接收至多C_β,D个原times，各heavy管保至少C_β,D^(-1)K^(-C)δ^-1个不同新times。在固定coefficient盒内，monomial row随time有固定Lip upper；原t到新θ只损O_β,D(δ)相位。将分配到同θ的原Y_t的Oδ-neighborhood取union，仍可用≤C_β,D Kδ^(-1+κ)个长度O_β,D(δ) intervals覆盖。

对每个θ选全部遇该phase target和unit coefficient support的标准plates。短normal方向为spanΓ′，与标量monomial phase只差一个固定有界非零norm；每target只需O_β,D(1)个normal格和long-direction格。取固定倍Δ处理所有邻格/边界，不改变幂次。由此

    #W≤C_β,D K^C δ^(-2+κ)。                            (4)

每个\widetildeν-support点至少参与C_β,D^(-1)K^-Cδ^-1个不同time plates。完整regular网有空targets的times也可保留，避免将原Z的δ分离误当自动满足源特殊(2.4)的net定义。这里没有把actual标记只在axis上的Oδ近似当成更细精度，也没有将不同time影像独立化。平均到逐管的唯一质量损失已在第2节支付。

## 10. 指数、阈值与固定polynomial完整用途

选α=1−κ/4、n=D+2。先取ε>0使L_n√ε<κ/8，再取原η足小，使(3)–(4)中全部K费用在exponent中小于κ/16，且Cη<ε/4，最后δ小于依固定β的阈值。逐点参与于是满足(3)的Δ^(ε−1)要求。结合(3)和第8节，得到

    #W≥C_β,D^(-1)K^-C δ^(-2+κ/4+L_n√ε)
       ≥δ^(-2+κ/2)，

而(4)≤δ^(-2+7κ/8)，δ足小时矛盾。固定常数依δ_0吸收，不伪装成uniform in β。参数顺序无循环：κ,D/chart先，ε后，η更后，δ最后；L只影响δ_0。

因此在具名finite GGW输入下，每个固定bounded polynomial R3 row β都不可能支持上述完整nearfull-small-native-label/CW配置。实际原ξ/Φ和两grain并未被换掉；本用途只用其中供给的wholeCW、marks及native upper，不额外假它们独立。这是fixed-profile proper-class排除，不是完整κ<1 mixed42或ordinary定理。

## 11. 旧R19、δ-dependent输入和真正未付责任

R19§§1–4已经付一方向残差的三个fixed-profile finite GGW模型；§6更强以weighted GWZ3排任意bounded单一残差shear。当前β的三个分量任意固定polynomial，不能仅靠那个固定physical R3投影删除其余horizontal坐标；这里的完整row系数商/CW compression是更宽的原输入转移。不过其exact compression来自R74，finite theorem早已具名，不将proper类扩展冒为完整gain、新数学ID或major。

原source只给dyadic/coarse Lip准备，不授固定polynomial、全clock统一smooth规范或Wronskian下界。即使global span全8也不推出逐time jet非退化；即使每δ非零torsion，也不提供独立于δ的GGW常数。允许β随δ改变时，(1)仍uniform成立，(2)的系数坐标条件数和固定moment解码却未免费统一。近似polynomial还必须另付actual Oδ phase误差和原质量；较粗ρ误差不能塞进第9节。选一个小好interval也不保证原S_T在其上有足访问。

只删whole T labels保原upper且重归一付质量倒数；删time之后逐tube下界须重计，point-Φ ADlower不自动继承。若未来只是所有合法restriction下重调用R19/R74/R77同一正幂工具，先核等价而不换名登记。weak curve/measure反攻若未有原wholeCW或fullsource，不反(1)或本稿fixed-polynomial结论。

## 12. 固定阶段判定与实际B10互读

已完成的数学为：五个精确time定义的观测商uniform Frostman；任意m的exact compression和原whole管cover；固定β系数条件数的显式费用；原heavy/mollify/全部support参与/原time网格/finite plates到实际native upper的完整矛盾。没有将全8jet设为必要条件，也没有用未付smoothness补完整source。

已实际全文读B最初10节，独核其原商/Schur及fixed-polynomial用途、全row-span8但处处零jet的smooth bump反攻、δ-dependent torsion的短线段measure反攻，无强制项。后两例没有原whole-CW/fullsource，不反本稿(1)。本人推导不计本人独审，root主稿及B新增统一阶段仍须实际全文互读，正式review须另授权。

施工前另收到并实际全文读`R0096_uniform_polynomial_spec.md`5节，以下按该补充规格支付此前未有的原coarse标签上界；它不是把第6节的C_β条件数直接删除。完整mixed42与四完整路线仍open，不宣ordinary新界、新ID/major，不预认证元数据、Git或同步。

## 13. 两套actual grains给原coarse native标签上界

固定D,B，现允许β=β_δ为degree≤D、monomial系数≤B的多项式，故在固定clock盒有统一C¹ upper C_(D,B)。取原allowed ρ≥δ和一个dyadic ρ-time窗J，令E_J^sp为其中所有原E_t的空间坐标union。重新实际读Def17.2(2)(3)与Def17.4(2)的原全文：前者只有第一套global Y_union的coarse AD；后者并未直接授native Ỹ_union的coarse AD。

第一套为(x,y+f(t)x)，x∈R、y∈R³。选t_J∈J∩Z，源dyadic Lip给|f(t)−f(t_J)|≤Cρ，所有x bounded。故E_J^sp在

    {(x,y+f(t_J)x): |x|≤1， y∈∪_(t∈J∩Z)Y_t^global}

的Cρ邻域。global union的(ρ,3−κ,K)-AD upper在固定盒给cover≤K^Cρ^(-3+κ)，再乘scalar x的Cρ^-1个格，得到

    N_ρ(E_J^sp)≤K^C ρ^(-4+κ)。                           (5)

在同一空间union上作固定native坐标变换L_J(X_H,X_N)=(X_H,X_N−β(t_J)X_H)，算子及逆有统一上界。对某实际native label ỹ∈Ỹ_t，t∈J，它的所有原filled horizontal点在L_J坐标为

    (x̃,ỹ+[β(t)−β(t_J)]x̃)， |normal−ỹ|≤C_(D,B)ρ。

Def17.4的fine cardinal≥K^-1δ^-3，ambient packing每horizontal ρ-cell最多C(ρ/δ)^3个fine cells，故该同一原grain有≥K^-1ρ^-3个不同horizontal ρ-cells。这不需要grain在各局部ρ盒AD lower，也不需要对time删选重建lower。

从native union选C_(D,B)ρ-separated实际labels，card≥c_(D,B)N_ρ(∪Ỹ_t)。每个label只选其一个原time/grain；扩大分离常数后，上述normal厚C_(D,B)ρ slabs的ρ-cells互不重叠。因此同一个L_J(E_J^sp)的cover至少是这些labels各自K^-1ρ^-3个cells之和。与(5)及L_J固定bi-Lip合并给

    N_ρ(∪_(t∈J∩Z)Ỹ_t)≤C_(D,B)K^C ρ^(-1+κ)。            (6)

这是actual两套表示导出的upper，不是Def17.4附加假设。分离/有限着色只用固定D,B常数，保留所有原labels的cover；没有把所选labels声明为新的完整配置。若一个coarse time槽相交固定个dyadic J，逐窗用(6)后相加，仍同主幂。

## 14. 九个allowed谱带与统一弱核费用的独立检查

以下同时独核B负责的量化接口，不把它作为新原hyp。C_δ为第6节系数map，||C_δ||≤C_(D,B)，至多8个singular values。选固定ε_*≪κ及大M，使M c_*>2，其中c_*为R74在固定m≤8、||A||+||B||≤2上的半代数compression幂。取a_j=a_0(ε_*/(4M))^j，j=0,…,8，a_0∈(0,1/8)固定；η<a_8后，在原allowed格取ρ_j=δ^(b_j)，b_j∈[a_j,2a_j]。可取b_j为向上最近的η格点，原dyadic版本的固定比较只改常数。

因M b_(j+1)≤ε_*a_j/2<ε_*b_j，开谱带(ρ_j^M,ρ_j^ε_*)两两不交；九带中某一带没有singular value。选该ρ，把边界值分别放入weak或strong，使

    C_δ=C_s+C_w， ||C_w||≤ρ^M，quad
    s_min(C_s|_(ker C_s)^⊥)≥ρ^ε_*。

这里不是假定原C_δ有singular lower。其a_N,b_N两列含常数/一次项identity，故至少两个singular values≥1；ρ小后strong rank≥2。ker的维数m≤6；ker0单列，1≤m≤3直接用全ker补网。

令K=kerC_s并取原orthogonal basisQ=[A;B]。对每实t∈[-1,1]，n_t(A+tB)=p_D(t)C_wQ，norm≤C_(D,B)ρ^M，||n_t||≥1。A+tB有固定norm upper，于是全部4-minors值≤C_(D,B)ρ^M；它们degree≤4，在五个固定分离测试times插值给全部系数同upper。这里测试的是已给全域polynomial，不声测试times属于原selected Z。

R74固定维幂稳定给K_1/E，dimK_1=m−3+e、dimE=e，physical泄漏≤C_(D,B)ρ^(Mc_*)≪ρ。若C_sλ落一个r≥ρ的ball，则λ距同一affine ker C_s≤C rρ^-ε_*。令h=C(rρ^-ε_*+ρ^(Mc_*)+δ)。按K/K_1的3−e维h格覆盖，whole凸box为h^(4−e)，故原概率≤CKh。m≤3改用m维全ker网，得到h^(4−m)≤h；ker0用h⁴。h≥1时概率≤1同样够。于是

    (C_s)_#μ(B_r)≤C_(D,B)K^C ρ^-ε_* r， r≥ρ。         (7)

此处conditioning只损ρ^-ε_*，不是任意L_β。弱核的exact rank可能全4；实际调用的是近compression和ρ级厚度，不把它误写成精确分类。

## 15. 全原clock的ρ级GGW矛盾，统一于δ-dependent系数

先按第2节保原heavy tubes和全部旧S_T。每个ρ-time槽至多含Cρ/δ个原δ分离times，所以每T仍给≥K^-Cρ^-1个不同coarse times。原selectedtime不需要与strong/weak谱选择独立；同一原管的weak相位≤C_(D,B)ρ^M，C_sλ的monomial相位有统一Lip upperC_(D,B)，round t只损O_(D,B)(ρ)。

对每个槽用第13节(6)覆盖其固定个原dyadic窗的native labels。每槽targets只需≤C_(D,B)K^Cρ^(-1+κ)个ρ intervals。把strong系数概率在ρ小球上mollify；(7)在ρ以下给密度≤C_(D,B)K^Cρ^-ε_*ρ^(1−n)，故任意α<1的全尺度c_α≤C_(D,B)K^Cρ^-ε_*。每support点继承某条原heavy管的全部coarse visits，weak、clock rounding和mollification都已由Oρ目标增厚支付。

在literal fixed n=D+2 moment family中构造ρ plates如第9节，得到

    #W≤C_(D,B)K^Cρ^(-2+κ)，
    #W≥C_(D,B)^(-1)K^-Cρ^(ε_*−1−α+L_n√ε_th)。             (8)

所有原K=δ^-Cη需转换成所选ρ的损失：ρ=δ^b、b≥a_min=a_8，故K^C≤ρ^(-Cη/a_min)。先α=1−κ/4、ε_*<κ/32，ε_th使L_n√ε_th<κ/16，M和九target尺度随后固定，再η≪a_min·min{κ,ε_th}，δ最后小。参与数K^-Cρ^-1支配ρ^(ε_th−1)，(8)lower的总损失仍小于κ/2，而upper保持至少7κ/8，矛盾。固定D,B常数由统一δ_0吸收。

因此这一补充链不再要求β非零singular values固定：在实际coarse闭包(6)及近compression(7)全部独审通过的条件下，可排所有degree≤D、coeff≤B的δ-dependent polynomial β源配置，η_0/δ_0均依固定κ,D,B及源chart/γ，而非具体β的L。不是把一般δ-dependent smooth曲线塞入uniform GGW；曲线始终是固定moment，变化和弱误差在原测度/目标上诚实收费。

## 16. 统一阶段范围、实际最终互读与停止

本补充独证了实际E两套grain给出的coarse native upper、原clock降到ρ及literal GGW用途，并独立检查九谱带/近compression的whole-CW费用。此前第6节fixed C_β的非统一性仍是该直接fine坐标转换的真实边界，不能倒改成它本来uniform；第13–15节用不同的原coarse输入支付该责任。

已fresh实际全文读root统一主稿`R0096_uniform_polynomial_native_exclusion.md`12节和B最终10节（含新§9的(10)–(16)及§10记录）。独立核root/B的空谱带、weak核degree4 minors、定维正交近compression、whole原box/补参数cover只付一幂、ρ以下smear、原time向ρ槽及全部support参与、η/a_min和GGW严格指数gap，当前无未解决强制项。B的两种弱反攻也已实际逐式独核，未把它们升fullsource counter。本稿的原coarse闭包与有限用途由root/B分别实际全文独审，不将自己的推导算本人的独审。正式review另在已授权路径按最终macro/next/source实际阅读后完成。

仍没有从完整dyadicLip β提取bounded-degree polynomial或足fine精度的保原质量近似。故这只是统一bounded-degree proper分支的已有高级工具应用，不是完整mixed42/ordinary增益，不宣新ID或major。不得以此续D/κ/ρ阈值或把desired polynomial当新原公设，未经外部同行评审，不预认证metadata/Git/sync。
