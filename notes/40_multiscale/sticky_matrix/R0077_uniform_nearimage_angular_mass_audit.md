# R0077：统一近共像代价、原时钟角质量与双近秩一反攻

2026-10-18，B。仅编辑本分配稿；阶段II先锁题，不改原source，不Git／spawn／元数据。输入、用途与停止依当前R0077 working_spec第2节。以下先独证统一near-image预算及其角质量用途；Ren–Wang的weighted finite投影和最后native增长由A另证，未经其实际全文互审不预称整个阶段II完成。所有高级wholeproof仍具名，未经外部同行评审。

## 1. 完整输入与要证明的统一陈述

保完整bounded WZ2609.22035v1 Def17.2–17.4的d5、k=ell3、kappa=1配置：原whole T的joint4-AD、N原分母、CW、每层Y的AD1及tube-KT(1-gamma)、filled X、point Phi的AD1／slab gamma、selected xi与coherence全保。gamma固定且0<gamma<=1。记K=C delta^(-C eta)。本稿不从任意native模型或given raw edge law反推这些输入。

要实付的命题是：存在只依固定gamma、维数及R16/13.5具名阈值的B0>4、c0>0、rho0>0，使对**每个**source损失eta_*及原allowed rho，只要

    delta^(1/4)<=rho<=rho0，
    eta_* <= c0 log(1/rho)/log(1/delta)，
    dist(F_z,F0+{v r:r in R^(1x2)})<=e<=rho^B0 对所有原z，   (1)

就有矛盾。v为fixed unit向量，F0可取某个原有界矩阵值。这里c0、B0不随mu=log(rho)/log(delta)重新选择；小性用实际K_*^C<=rho^h判定，而不只说“eta依mu足小”。允许rho0最后依先固定的有限定理参数。原delta的floor均由delta<=rho^4支付。

该统一命题再作用于合法whole-time restriction，推出在所需e>=delta^d0范围内

    Uniform_Z{F_z距某affine common-image plane<=e}
       <= C K^C e^tau，                             (2)

tau>0固定。太粗e使右侧>=1时不调用源定理。(2)不是假设angular AD，而是第3–7节从完整source得出的proper结构质量上界。

## 2. R76的实际clock domination与原delta²选管质量

R76在一组选定原端点、code block和8维axis残差桶后，仍保每条选中heavy原T的全部原访问S_T，且n_T=#S_T>=K^-C #Z。选管相对原whole T仅约delta² L^(±C)，不准将其当nearfull新T配置；本节不作这种重置。其exact native pair (y,y')在固定残差桶内只对应O(1)根原T；g是这些原访问的实际计数除固定最大重数，取值0..1。

令q=E_(Yt x Ys x Z)g。对任意time集合J，分子、分母中共同的native product大小和残差重数都消去，得到

    E(g 1_J)/q
      <= C sum_T #(S_T cap J)/sum_T n_T
      <= K^C #J/#Z。                               (3)

因此主导常数是原heavy访问损失K，**不是**L=delta^-C(a+b+eta)，也不乘native Y-cover。每个非空exact native pair的conditional clock也满足K^C Uniform_Z domination，因为它只混合固定数原heavy T。不同pair的S_T仍可完全不同；(3)不给pointwise下界、独立g或公共clock。

原Uniform_Z的interval cap<=K(|J|+delta)。故可删u距原t或s小于sigma=delta^b的times，所删g质量<=K^C(sigma+delta)q。先固定c=b/10、eta最后小，则此量o(delta^c q)。block的delta²原质量没有在此收费两次，也未被(3)抹去。

## 3. 固定rho质量阈值与慢拟合的19.4排除

先固定epsilon0>0，使a_MNL=3epsilon0在R16有限定理允许区间内，并取epsilon0<1/20。再固定theta>0足小，依epsilon0、gamma及以下有限损失常数；它不依mu。每个原dyadic rho-window J若存在all-real R,U使

    # {z in Z cap J: |F_z-zR-U|<=rho^(1+epsilon0)}
       >rho^theta rho/delta，                       (4)

就称bad，选其实际fit witnesses。norm取max-entry，固定等价norm只付常数。#(Z cap J)<=C rho/delta，故fit相对原J的比例至少c rho^theta。

若|R|<=rho^(epsilon0/3)，这些fit值的直径<=C rho^(1+epsilon0/3)。选实际fit anchor即可在**原配置**直接调用19.4，sigma_*=C rho^(1+epsilon0/3)位于[rho²,rho]。原19.4的明确幂结论给

    CW >= K_*^(-C/gamma)
          rho^(C theta/gamma-epsilon0/(3))。         (5)

这里kappa=1；fit质量写成delta^(theta mu+O(1/log delta))，故它的损失是rho^(C theta/gamma)，不是delta^(C theta)。先theta<<epsilon0 gamma/C，再令eta_*/mu足小，(5)反原CW upper。19.4只有single-anchor量词，在此确只用了一个真实anchor，不借19.2 every-anchor。

## 4. 快拟合：全局并、all-real斜率和真实二次KT

余bad fits有|R|>rho^(epsilon0/3)。其fit点span>=c rho^(1+theta)，因为原times delta-separated；原allowed rho上的dyadicLip给F振幅O(rho)。取两个extreme fit times得

    |R|<=C rho^-theta， |U|<=C(1+|R|)。             (6)

所以不得把原20.2的literal bounded-Mat statement冒为all-real。本节另用R16原tuple审计的实际V／own-incidence H几何证明该扩展。

若bad whole windows承载至少rho^theta #Z个原times，其fit并至少c rho^(2theta)#Z。直接在这些整层原times上作good-q／V计数；不把fit并宣布为新完整配置。R16原tuple第2、3、5、7节的每一步仅有有限个CS、最大fibre除法、heavy删除和own-slab查询。把原time质量rho^(2theta)保留在这些式子中，它们给

    K_fit <= K_*^C rho^(-C theta)，                 (7)

而非先把rho^(2theta)粗化为delta^(theta/4)。原Phi_q unused bins不被赋slab：H由原incidence mixture构造，V边际upper保证删heavy方向确实保质量。固定实际endpoint、自己使用的差psi后，保K_fit^-C比例的原times，且|R psi|>=K_fit^(-C/gamma)|R|。

物理输出在实际native Y的二次轨道邻域，取

    Delta=C rho^(2+epsilon0/2)|R|， L=C rho²|R|。

fine换rho角proxy误差C rho³|R|、fit误差C rho^(2+epsilon0)都在Delta内。由(6)及fast下界，L<1且Delta>=c rho^(2+5epsilon0/6)>>delta；这些是原physical KT查询，不把fine delta改成粗尺度。删近endpoint times的clock质量同样计入(7)，两侧各自单调的二次time映射给Delta-cover lower K_fit^(-C/gamma)L/Delta。完整Y的tube-KT upper为K_*^C(L/Delta)^(1-gamma)。比较迫

    rho^(-epsilon0 gamma/2)
       <= K_*^(C/gamma) rho^(-C theta/gamma)。      (8)

|R|在L/Delta中精确抵消。theta<<epsilon0 gamma²/C、eta_*/mu后小即可反(8)，无需theta<<mu。所有bad whole windows合计因此少于rho^theta #Z；删它们只损o(1)原time层。final graph的K不含theta：rho^theta只在反设几何中进入K_fit，没有回灌保留配置。

## 5. R16实际linewise调用也无mu循环

令Z_good为原完整配置中的whole-time witness subset，删bad windows只损o(1)。此处**不另改名source参数／newallowed格**：仍在第1节原eta_*完整配置及其原allowed rho、rho² coherence上重取R16 good-q，所用各保留层Y/X/Phi/xi全部不变。至少一个good rho-window有K_*^-C rho/delta个原times；否则全局#Z下界与rho-window数矛盾。若固定倍端点需借原邻allowed尺度，比例delta^-C eta_*计入K_*。第7节才把原S作为新完整配置并选其newallowed rho，二者不能混用。

投影F到所给affine common-image plane，记barF，误差e<=rho^B0。它不是新source；实际tuples、原Y和selected xi均不改。working tau=C K_*^C rho²，time除rho、normal除tau、矩阵除tau/rho。替换造成物理误差C rho e<=C rho³，归一后O(rho)；源delta floor由tau rho>=c rho³>>delta付。barF的bounded amplitude及source-cell oscillation由原F加2e控制，不假其任意细尺度Lip。

R16 actual tuple／heavy weighted quotient得到共同rho-separated B、actual input/output A_-、A_+、共同own H difference prior和0<=g_c<=1，密度、KT、card ratio及Fst常数全是K_*固定幂。原fine times不能直接冒rho-separated；time-cell误差的K_*因子乘小矩阵幅度，仍为O(rho)。

MNL取固定a_MNL=3epsilon0、b0=theta/2；13.5和R16给固定h_MNL>0、rho_MNL>0，不含原mu。若coarse affine fit命中rho^b0比例，span>=K_*^-C rho^b0迫all-real slope<=K_*^C rho^-b0；lift回fine的**归一矩阵**误差<=rho^(3epsilon0)+K_*^C rho^(1-b0)，质量>=K_*^-C rho^b0 rho/delta。反归一要乘tau/rho<=K_*^C rho并补原F-barF的e；所得物理矩阵误差小于rho^(1+epsilon0)，质量大于(4)阈值。这在eta_*/mu足小时严格违反(4)。所以barF满足有限MNL的SM；每个used psi上barF(B)psi恰沿一条line。取K_*^C<=rho^-h_MNL，R16 finite结论矛盾。

这里只调用已核有限接口及具名13.5wholeproof；不把一般二维F(B)psi增长当已证。rho_MNL依固定theta等参数而非mu；rho<=rho0<=rho_MNL即可。所有fixed常数C也由缩小rho0吸收，避免仅引用“delta0依mu”而偷失uniform性。

## 6. 统一NI引理的量化收尾与floor

归并第3–5节有限个K_*幂，存在固定H0>0，使全部比较只要求

    K_*^C <= rho^-H0， rho<=rho0， delta<=rho^4。

选theta足小满足(5)(8)；再固定B0>max(5,3+3epsilon0)，最后固定c0使eta_*<=c0 mu蕴含上述K_*比较。顺序不含mu回选epsilon0／theta／MNL参数。若K_*=C delta^-C eta_*，固定C通过rho0统一吸收。working tau<rho、barF扰动小于coarse source-cell幅度、原KT最小宽度tau rho>=delta也在此条件内。

这是第1节(1)的实际证明，而非另加NI公设。唯一具名高级输入是原19.4的明确幂结论、原native KT、13.5和已经逐步审过的R16 finite接口；没有用literal20.2的all-real扩张声明替代第4节。原19.2 wholeproof不是本引理的必要输入。

## 7. Whole-time restriction把误差变成原质量幂

设S是原time集合，p=#S/#Z，F_S距某affine common-image plane<=e。只删整time层；原T、N、CW及每层所有数据不改。R22以

    eta_* <= C1(eta+ell_p)，
    ell_p=log(1/p)/log(1/delta)

给合法参数，选原eta的整数倍确保newallowed是旧格子格。平均marks由保留整层原访问重新计，不宣每条管逐管密度全保。令d_e=log(1/e)/log(1/delta)，先选固定tau_NI>0充分小，使C1 B0 tau_NI<<c0。

反设p>C2 K^C e^tau_NI。非平凡情形强迫d_e>=C3 eta；否则增大K幂已使右侧>=1。于是ell_p<=tau_NI d_e+C eta。取目标rho_*=e^(1/B0)，再取newallowed上邻rho，满足

    rho_*<=rho<=C delta^-eta_* rho_*，
    mu=log(1/rho)/log(1/delta)
       >=d_e/B0-C eta_* >=d_e/(2B0)。              (9)

反设及tau_NI的先选保证eta_*<=c0 mu。若e>=delta^d0，选固定d0/B0<1/4，故rho>=delta^(1/4)；若e足小固定，rho<=rho0。较粗的e由C2 e^tau_NI>=1处理。新格距不是免费常数，而是(9)内真实eta_*费用。由e<=rho^B0与统一NI矛盾，得到(2)。每个S可不同，结论统一于原选择；没有固定mu后才选择tau_NI。

## 8. 双近奇异M的真实谱投影

R76有A=F_t-F_s，smin A、|s-t|>=sigma，M_u=(F_u-F_s)A^-1，||M||<=C sigma^-1。若

    |det M|、|det(I-M)|<=epsilon=delta^d，

则tr M=1+det M-det(I-M)=1+O(epsilon)。特征判别式为1+O(epsilon)，所以两实根lambda1=1+O(epsilon)、lambda0=O(epsilon)。定义

    P=(M-lambda0 I)/(lambda1-lambda0)。

由Cayley–Hamilton，P²=P、rankP=rank(I-P)=1，并有

    ||P-M||<=C epsilon sigma^-C，
    ||P||<=C sigma^-C，
    sin angle(imP,kerP)>=c sigma^C。               (10)

最后一个式子是二维斜投影norm与两线夹角的关系，不能因秩一就授统一横截。选b在d后足小，epsilon sigma^-C<<R=delta^(d/10)。这个代数只给每个u的投影；R64 raw全对small-det分类不适用，且未被调用。

## 9. Image与kernel角团簇均返回affine common-image

若imP_u落在projective w-ball内，固定unit代表v0。由于||P||<=C sigma^-C，P_u距{v0 r}<=C sigma^-C w；因此原F_u距F_s+{v0 r A}<=C sigma^-C(w+delta^d)。A可逆，{rA}仍是全部rows，故这是第7节的common-image平面。

若kerP_u落在w-ball，以unit row r0垂直中心line。写P_u=v_u r_u，r_u v_u=1；经符号和正规化可取r_u=r0+O(w)、|v_u|<=C sigma^-C。固定一个实际P_*后，trace条件给r0(v_u-v_*)=O(sigma^-C w)，故v_u-v_*距ker r0为O(sigma^-C w)。于是

    P_u-P_* 距 {v0 r:r任意} <=C sigma^-C w，

v0沿ker r0。乘A并用(10)，原F_u距F_*+{v0 r}<=C sigma^-C(w+delta^d)。这说明fixed kernel也给**差矩阵共同像**；不是把未解common-kernel出口悄当nearimage。

所以在本轮needed w>=R的全部角尺度上，第7节分别给原time law

    nu_Z{u in V:imP_u in J_w}，
    nu_Z{u in V:kerP_u in J_w}
       <=C K^C sigma^-C w^tau_NI。                (11)

choose d0覆盖e=C sigma^-C(w+delta^d)的最细needed值；太粗角尺度用右侧>=1。无全局angle ADlower、无两角独立、无自由Schubert spreadout。

## 10. 实际V质量、角归一与不能赠给g的步骤

若反设E(g1_V)>=delta^c q，由(3)有

    nu_Z(V)>=K^-C delta^c。

故normalized nu_V的两个marginal在w>=R各满足

    cap(J_w)<=C K^C delta^-c sigma^-C w^tau_NI。    (12)

该费用须进入A的finite RW异常角质量；不能把未归一的(11)直接当nu_V概率Fst。u近anchors已由第2节删，且同一u上两角good只能由union bound保，不能独立相乘。原g_u可以随u任意变化。

所需RW是v3 Def3.1／Th4.1的finite niceconfig，需实付weighted角和all-large-native-subsets的robust lower。若该lower为k，则heavy fibre阈值是w^-e #Y/k；其heavy bins不足w^e k才可由robust性删小inputmass。两侧余fibre给输出lower含w^(2e)损失，不是w^(-2e)增益。只知道两个projection cover各大，不能直接把它们乘起来支配相关g。

本稿目前证明的是(1)–(12)及其真实source边界；最终coarse输出R-cover upper、exact fine Y的w重聚合、weighted RW和g质量相加由A另证并须实际全文互审，不能据(12)提前宣布main结论。

## 11. 独立反攻与完整闭包检查

global二次非affine例不等于原local SM：任意rho-window的Taylor误差O(rho²)小于rho^(1+epsilon0)。所以本稿不以M(u)=[1,u²;0,0]反完整source。缓慢转动斜投影、某侧角恒定、两侧近平行都由第9节返回nearimage原time集合；其排除确实需要第3–7节，单独矩阵nonfit或角Fst名称不足。

nearimage集合上的time删选保持完整层，不对clipped native Y授ADlower；重新取good-q／heavy-H都从原质量计。平均marks、逐heavy管visits和每native pair时钟三种归一分开：前者在R22重计，第二种支持(3)，第三种不被授独立性。source K只依eta，反设K_fit含theta但最终图不含theta；最终角概率另付sigma、delta^c。这是防止“先把所有fixed幂藏K再取eta小”的必要区分。

如果源wholeproof的19.4幂结论或13.5有限阈值失效，则本稿条件链随之失效；这里不因作者署名认证它们。本文没有新增smooth／rational／goodrank／κ阈值公设，也不把所证明proper第三时质量命题当ordinary高维目标。

## 12. 当前交叉读取、判定与停止

已实际全文读本轮spec5、phaseI A8/B7，R75 A12的source-SM与nearimage用途，R16 original-tuple8／weighted-coarsening5／finite MNL7／linewise-application5，R22 whole-time5；又实际读原19.4 statement及proof入口、20.2完整linear proof的相关页文本。没有虚报本轮官方byte重新核查或新PDF全文审查。

随后实际全文读A阶段II12节及root整合14节，并对照本地RW v3 Def3.1和Th4.1原文。A第3–6节的完整Y Voronoi权、坏方向归一／w²小权截断／log层、point-heavy后任选同M方向的Fst费用、nice configuration及总管upper均逐式核过；其对“存在任一大细子集投影小”的坏事件一次量化，确给robust而非逐子集不同好角。A第8–9节保exact细g、负e重纤维阈值、同u两角union bound、w=C R sigma^-C和完整native输出R^-1均通过。root的uniform NI及source整合与本稿一致，两个case的角cluster都真返回common-image；未见未解决必修。

A独核本稿时指出第5节应保原allowed rho而不重命名newallowed；已实修为原配置内Z_good witness subset，且把coarse矩阵误差反归一单位写出。该文字责任已经解决。统一NI不再是待证公设；但本稿的自证不计自己的独审，A/root另行独核。最终macro／next及正式review尚待授权与fresh全文读取；不提前认证其状态、未写元数据或未来Git／sync。具名高级wholeproof仍保留，未经外部同行评审。停止改参数和更多fixedtime校准，后续只作指定终审。
