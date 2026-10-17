# R0065：有理双时间曲率与原低维输出图

2026-10-18，root。先写research/rounds/R0065_working_spec.md §§1–5后施工。本文证明有额外定量有理曲率输入的有限图排除，实际核其原source接口；不从完整配置提取该输入，不声普通高维增益、重大性或首创。未经外部同行评审，最终独审另记。

## 1. 两个量词和本轮实际不同输入

R64的近秩一差分类控制整个原nu²，而dense used graph未必满足它；双曲线反例准确显示此差别，但没有构造同一个低维输出集Aplus。这里保原g的全部相关性，使用每条used平移确落N_Cr(Aplus)的条件。

新增的是fixed rational degree/denominator和一个量化Jacobian coefficient，而非由ordinary Lip/SM或非共线推出二维Frostman。R58 plateau复杂度随r增长，故不满足该额外输入；R16已付linewise可有Jacobian恒零，与本轮不同。全source f不假设有此有理格式。

## 2. 正式定理及两branch版本

固定D>=1、M>=2、gamma∈(0,1]、kappa∈(0,2]及C0。I1,I2⊂[-1,1]为固定interval，长度>=1/M。取F_i=P_i/Q_i，matrix P_i与scalar Q_i的degree<=D、coefficients绝对值<=M，|Q_i|>=1/M于I_i。所有coefficients可随r变化，D/M固定。原nu_i为I_i上的概率，任意interval I满足

    nu_i(I)<=K(|I|+r), K>=1.                         (2.1)

原pi为带原标签omega的概率，|psi_omega|<=M，任意width w>=r slab质量<=K w^gamma；sigma为任意输入y概率。定义

    Tpsi(t,s)=(t-s)[F1(t)-F2(s)]psi,
    Jpsi=det(∂tTpsi,∂sTpsi)=N(t,s;psi)/(Q1(t)^3 Q2(s)^3).

N的time degree<=d:=6D+4，关于psi为homogeneous quadratic。设某一个time monomial的psi二次型系数maxnorm>=lambda，lambda>=r^theta，0<theta<min(1/6,kappa/6)。

设Aplus可由至多K r^(-2+kappa)个r-balls覆盖。若0<=g(y,t,s,omega)<=1且g>0时dist(y+Tpsi,Aplus)<=C0 r，则原product概率下

    m:=integral g <= C[D,M,C0] (K r^(theta gamma/2)
                         +K² r^(theta/(2d))+K³ r^(kappa-3theta)).   (2.2)

同一全域有理F只是F1=F2的special case。两branch是用于R64的fixed chart，而非声其piecewise F为一个全域P/Q。

## 3. 分母、degree与一致导数界

写W=(t-s)[P1(t)Q2(s)-Q1(t)P2(s)]，Tpsi=Wpsi/(Q1Q2)，time degree(W)<=2D+1。令

    U=Q1 ∂tW-Q1' W, V=Q2 ∂sW-Q2' W.

则∂tTpsi=Upsi/(Q1²Q2)、∂sTpsi=Vpsi/(Q1Q2²)，故N=det(Upsi,Vpsi)，degree<=6D<=d。其所有coefficients、time一阶导数均由D/M控制；Tpsi的前二阶导数亦在对应interval上有统一界。

coefficients固定有界和denominator lower保证在I_i的r-小扩展内仍|Q_i|>=1/(2M)，只需r足够小依D/M。以下smearing只在此扩展计算模型，不把原f本身作smooth延拓。常数一律允许依D/M/C0，不依coefficients的具体r变化。

## 4. homogeneous quadratic的角小值集

若q(psi)=a psi1²+b psi1psi2+c psi2²的coefficient maxnorm L>0，则对0<epsilon<1，{psi:|q(psi)|<=L epsilon}包含于至多两条width C sqrt(epsilon)的过原点slabs。证明：对应对称matrix有最大绝对eigenvalue>=L/2。若同号半定，由最大eigenvector坐标平方给单slab；若异号，以两个unit linear forms分解q，外系数为两个eigenvalue绝对值之和>=L/2，product小迫至少一个factor小。退化rank1同样成立。

取§2选定的time coefficient q和angular bad set Eang={|q(psi)|<lambda r^theta}。因L>=lambda、r^(theta/2)>=r，原slab cap给

    pi(Eang)<=C K r^(theta gamma/2).                 (4.1)

未去掉标签重数，未以角law的二维Lebesgue密度代slab。其余psi使N(.,.;psi)至少一个time coefficient绝对值>=lambda r^theta>=r^(2theta)。

## 5. 二元polynomial小值集的自含估计

若p(t,s)的time degree<=d且至少一个coefficient绝对值>=L>0，则在[-2,2]²上

    area{|p|<=epsilon} <= C_d (epsilon/L)^(1/(2d)).   (5.1)

比例较大时用trivial box area。证明所需一元事实：在有界interval上，degree<=d的polynomial若在测度e的集合E上绝对值<=epsilon，可在E中逐次选择d+1个彼此距离>=e/[4(d+1)]的点。Lagrange插值使每个coefficient绝对值<=C_d epsilon e^(-d)。逐选时已排区间的总长度小于e，故每一步合法，零测极限不需选点。

二元情形记小值集面积e。Fubini给一组t、测度>=c e，其s-fiber测度>=c e。第一次一元插值控制所有s-coefficients p_j(t) <=C_d epsilon e^(-d)；在这组t上再插值p_j，得全部time coefficients<=C_d epsilon e^(-2d)。与L比较即(5.1)。此处不是用Jacobian几乎处处非零直接推均匀熵。

## 6. 原离散time的尺度r smearing

把每个原nu_i与Uniform([-r,r])卷积得nu_i^r。由(2.1)其Lebesgue density<=3K/2。即使原nu_i有atoms/repeated labels，该推导不变；nu1/nu2仍取原product reference，原g的相关性完全未移除。

对任意原事件E，如果原(t,s)∈E时它的所有r-jitters都落Eplus，则

    (nu1×nu2)(E) <= (nu1^r×nu2^r)(Eplus)
                  <= C K² area(Eplus).             (6.1)

这是在原事件上积分概率kernel得到的上界，不声g就是smoothed law，也不生成原source新点。T和N的统一Lipschitz界保证所需的expanded output/J事件；下面只对此模型使用连续换元。

## 7. 删临界参数的完整费用

取s0=r^(3theta)。对psi∉Eang，N至少有coefficient>=r^(2theta)。原|N|<=s0的参数，r-jitters满足|N|<=s0+C r<=2s0（r充分小、3theta<1）。由(5.1)/(6.1)得到

    (nu1×nu2){|N|<=s0} <= C K² r^(theta/(2d)).       (7.1)

常数变化吸入C，原质量上界对所有剩余psi统一。这里收费删去near-zero/critical curves；不声整个raw T-law有二维Frostman。任意0<=g<=1在这些参数上的质量不超过(4.1)+(7.1)，无需g的条件独立。

## 8. good-J的有限重数与小球推前

对固定psi、任意z∈R²，fiber Tpsi=z由两个time polynomials

    (Wpsi)_j-z_j Q1Q2=0, j=1,2

切出，各degree<=2D+1。在Jpsi非零处，两个方程的Jacobian为(Q1Q2)²Jpsi非零，故该点也是其复零集的孤立零点。经典plane Bézout零维分支界给regular preimages数量<=B_D=(2D+1)²，哪怕还有其它singular positive-dimensional fiber components。采用的具名经典输入见§14，不将所有real isolated components在无regularity下冒充复零维分支。

原good事件|N|>s0、Tpsi∈B(z,C1r)经所有r-jitters后有|N|>=s0/2，Tpsi∈B(z,C2r)。该expanded set上|Jpsi|>=c[D,M]s0。由inverse function theorem取可数局部一一charts，Borel分割后逐chart换元；总image重数<=B_D，故

    area(expanded set) <= C B_D r²/s0.

由(6.1)即

    (nu1×nu2){|N|>s0, Tpsi∈B(z,C1r)}
                         <= C K² r^(2-3theta).      (8.1)

未忽略multiplicity，也未以连续新像的体积给原union lower；这里只把原事件概率由合法jitter上界比较。singular fibers已在§7预算内。

## 9. 真正使用Aplus而得到主式

固定原y、psi，在good参数上，g>0迫Tpsi落在最多K r^(-2+kappa)个半径C1r的ball之并，centers为Aplus的cover centers减y。对(8.1)求和得<=C K³ r^(kappa-3theta)，统一于任意y。再积分原sigma和pi，加§7/§4坏质量即得(2.2)。sigma无density、维数或分离假设，原Aminus不需乘积；输出card绝对上界才是使用的几何信息，只有Aplus/Aminus比值不足。

例如先选theta<min(1/6,kappa/6)，再取

    0<h<min(theta gamma/8, theta/(16d), (kappa-3theta)/8).

若K<=r^-h且m>=r^h，则右端各项至多C r^(2h)，小r矛盾。一般原费用K的固定次幂和图密度反幂，可先统一成这个h-budget再选source eta足够小。

## 10. 实际R16 fine图直接接口

沿R16_original_tuple_audit及source_linewise_application §§1–2已付good q、used H及good tau-window，取r=rho、tau=C delta^-eta rho²。保原fine times z∈Z_q，不必为本定理重做coarse-time代表或heavy-fiber quotient。令

    t=(z-z0)/rho, F_norm(t)=(rho/tau)[f(z)-f_ref],
    y_norm=(y-y0)/tau.

原bounded G图仍以sigma=Uniform(A_f^-)、nu=Uniform(Z_q)、pi=原used H×H差标签为reference，密度>=K^-C。time cap由delta-grid及#Z_q>=K^-1rho/delta给K(|I|+delta/rho)<=K(|I|+r)，因为rho>=delta^(1/4)故delta/rho<=rho。used H的slab floor正是rho=r；原fine角替H已在tuple审计收费，不借unused粗cells。

输出A_f^+=Y_(z*)∩CQ在normal单位tau下满足绝对N_r<=K^C r^(-2+kappa)：用full Y在每个tau r-separated中心的AD lower，disjoint小balls均在C'Q，再用full Y于tau的AD upper；tau r>=delta，kappa=2的指数0亦合法。clipped输入未被授新AD lower。原误差( tau rho+delta )/tau=O(r)，因为delta/tau<=r（rho>=delta^(1/4)）。

所以若此实际fine F_norm在全部所用times上O(r)近某fixed-degree/controlled-denominator有理模型，并且其N系数>=r^theta，本有限定理排除该配置。无须额外SM、tube-KT或标量Th13.5来证明本条curved分支；原tuple准备和完整source假设仍按既有审查层次引用。完整配置没有自动给该有理模型或系数lower。

## 11. 模型误差、restriction与双向范围

若原F_norm与模型的sup差<=C r，则原bounded times/psi使T误差<=C' r，只放大C0。以物理f误差e_phys表示，normal平移误差为C rho e_phys/tau，必须<=Cr，即e_phys<=C tau；不能把物理小误差直接作规范r。任意不同frame须重算s_t s_F/s_y。本文不把r^a、a<1的粗近似免费吃进本结论。

任意dominated shading/restriction可保(2.2)的原未归一上界。若重归一time或angle子集质量p_i，其cap分别付p_i^-1，graph/reference质量也按原product转换；没有AD lower或逐管density闭包。若只在rare time-rectangle上有模型，必须支付该rectangle原质量，不说自动保subpower。

此定理不反向推出所有source的曲率下界，也不推出完整Kakeya正幂gain；fixed-degree approximation和lambda>=r^theta是不由任意旧全称shading再调用获得的额外输入。若试图下一轮仅把该输入命名成desired generic expansion，须按旧等价/冻结拒绝。定性J非零而lambda趋零任意快亦不足。

## 12. common-kernel抛物线与global小球校准

取F(t)=(t,t²)^T e^T，unit e固定。它的F(t)psi=(e·psi)(t,t²)通常不落直线，R16 exact linewise不覆盖。直接计算

    Tpsi=(t-s)² (1,t+s)^T(e·psi),
    Jpsi=4(t-s)^3(e·psi)².

故N有固定非零二次型系数，符合本定理。另一方面，uniform time和任何bounded原psi下，|t-s|<=c sqrt(r)给T∈B(0,C r)，原概率>=c sqrt(r)。所以本模型本身否“整个raw law有near2-Frostman”；已收费的good-J子图与低维Aplus才产生矛盾。R58 plateau是随r增加pieces的Lip近抛物线，不满足本固定有理格式，故未被反例否定。

若F=F0+h(t)M或F=F0+v r(t)^T，则对每psi的T总沿一条固定方向，J恒零；本curved定理不能调用，仍是R16具名linewise输入的范围。方向law全压J二次型的零线或time出现常量大atom也不能冒满足本定理slab/time cap与小K预算。

## 13. R64双曲线确不能补低维输出图

在其negative/positive fixed chart上，u=2t+3、v=2s∈[1,2)，c=1/8，F1=c diag(u,u^-1)、F2=c[[0,v],[v^-1,0]]。写p=psi1、q=psi2、A=up-vq、b=u-v-3，则

    T=(c/2)b A (1,-1/(uv))^T,
    J=c² A b [2pu²-3pu-2qv²-3qv]/(u²v²).

采用Q1=u、Q2=v表示，N=c²uv A b[2pu²-3pu-2qv²-3qv]。其中u^5v的p²系数为2c²，因此t^5s系数恰128c²p²=2p²，固定非零。每个cross chart均满足定量criterion。原time两branch各质量1/2，任意g'<=R64 cross g若有subpower原质量，至少一个ordered cross chart有subpower密度；归一只固定费。因此在任意原sigma及slab pi下，它不能同时有K=r^-h、N_r(Aplus)<=K r^-2+kappa和真实output relation。

这只是排R64反图的低维output完成，未证明完整source一定落该模型。这里的critical A=0及另一bracket为零不能忽略：真实H-H差law若在正坐标盒有固定density，u,v,p在适当固定小interval，q在up/v的width Cr带内即|T|<=Cr，原概率>=c r。故整个cross rawlaw也不具有统一2-Frostman；pi不需取一个违规的固定psi原子。

## 14. 具名输入、一手比对及停止

有限证明的代数输入仅经典plane Bézout的isolated complex zeros界；实际核[Terence Tao, Bezout’s inequality, 2011-03-23, Theorem1/Corollary2](https://terrytao.wordpress.com/2011/03/23/bezouts-inequality/)及其common-factor处理。regular实fiber通过complex inverse function theorem确属该零维部分；不是把任意real component直接套复定理。其高维推广未用。polynomial小值集的插值论证、角quadratic和原probability smearing已在本文完整给出；分析换元采用标准局部inverse-function/change-of-variables。

此为经典工具下的条件proper-subclass排除，不认证新颖或major，不新增数学ID。没有证明全source的fixed rational approximation/quantitative curvature、common-kernel一般扩张、mixed/general-to-sticky或ordinary n>=5/general。停止D/M/theta/h、critical阈值及同义“有曲率就2Fst”的轮；下一宏观复核须回完整无regularity配置的实际未付输入，不能把上述额外假设默授或再做pencil近似阈值微调。Goal active。
