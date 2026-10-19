# R0103：原访问质量的Schubert集中与native多项式薄层

2026-10-19，root；按working5锁后施工。使用R102已付的全局码与实际rich fibres，以及具名He1710.00795v2 Th1。结论是原det-large分支必须出现带尺度—质量下界的全局Schubert集中，不再额外假设原方向非集中。高级投影定理wholeproof未从零独证；本稿终版独审另记，非外部同行评审，无新ID/major/ordinary或完整κ1声明。

## 1. 完整源、量词与继承对象

沿R102§§1–7完整WZ Def17 matrix33的bounded d5/k=ell3/κ1配置，原管数N、clock数m及K=δ^-C0η、原CW/AD/filled-X/native-Y/point-Φ/slab/coherence均保其原义。只在已实际提取的det-large分支讨论：原anchors t,s，h=s−t、A=F_t−F_s满足|h|≥σ、smin A≥σ、σ=δ^b。有限次原提取费用记L，H为保有≥L^-C N原管的code同权层，未挑单block。

R102给同一个有界δ网格点集P⊂R4及实际far/heavy clocks U⊂Z：

    L^-Cδ^-2≤|P|≤L^Cδ^-2,
    |P∩B(z,ρ)|≤L^Cρ²|P|  (ρ≥δ),
    |P_u|≥L^-C|P|,
    Nδ(Π_(G_u⊥) P_u)≤L^Cδ^-1  (u∈U),             (1)
    G_u=((t−u)(F_u−F_s); (s−u)(F_u−F_t)),
    smin G_u≥rσ/2,
    I_U=Σ_(u∈U) I_u≥L^-C N m,  0<I_u≤|H|.

I_u只数H在u的实际保留heavy点访问；每T每u至多一次。far删除曾逐管半保，point-heavy后仅平均保量。本稿不把H/这些marks授为新的完整Def17。使用R102 chart选取之前的全部U/P，因He在整个Grassmannian表述，不需丢chart或将重复时间当不同方向。

## 2. 新一手定理与小参数顺序

He, Orthogonal projections of discretized sets，[固定v2原稿](https://arxiv.org/abs/1710.00795v2)，Th1。官方PDF33页，history版本日期2018-05-09，PDF自身Date为May10；JFG正式2020卷7页271–317的47页版未与本PDF逐字同一认证。HTML重编译Date不作版本日期。

准确接口：给n>m、0<α<n和q>0有ε_H>0。A0⊂B1，NδA0≥δ^(-α+ε_H)、球上界≤δ^-ε_H ρ^q NδA0，并且概率µ on Gr(n,m)满足

    µ{V:d_angle(V,W)≤ρ}≤δ^-ε_H ρ^q
       (所有ρ≥δ、W∈Gr(n,n−m)),                    (2)

则µ质量≥1−δ^ε_H的V对所有NδA′≥δ^ε_H NδA0的A′⊂A0有Nδπ_VA′≥δ^(-mα/n−ε_H)。d_angle为两正交列基拼合的det绝对值；n4/m2时是两个principal sines之积，不能直接当到Schubert cycle的metric距离。

本稿固定任意q∈(0,1/4)，取n4/m2/α2。可把ε_H减成任意0<e≤min(ε_H,q/4,1/100)：e较小时，三项假设更强、允许A′更大，源结论也强于δ^-1-e，故该单调化合法。之后选a,b,c、η使(1)全部L^C≤δ^-ℓ，ℓ<e/20，且4bq<e/8、4b<e/(4q)，δ最后小。所有固定常数也吸收到δ^-ℓ。取小q还避免把普通Lip的product-sine二阶接触在q>1/2时产生的profile误报为新信息。

将P固定缩放进B1，不改变normal；在同一δ尺度每球至多固定数点，cover数与原cardinality可比。(1)因此支付He的点数下界和q-Frostman球上界，且每个实际P_u都达到其大子集门槛、小像上界严格小于δ^-1-e。有限网格δ-cover与球cover只付维数常数，不调用连续或Hausdorff推论。

## 3. 任意原权重支持上的全局cap必须失败

令W_u=G_u⊥∈Gr(4,2)。给U上的任意概率权重a_u，允许有些为零，令µ=Σ a_u δ_(W_u)。若对全部W和ρ≥δ有

    µ{V:d_angle(V,W)≤ρ}≤δ^-eρ^q,                  (3)

则He给µ正质量的good V。该V至少对应一个正权原u；He对所有大P′有效，故它必须对那个实际P_u有效，反(1)。即便同一个V由多个u实现、各P_u不同，这一论证仍成立。没有uniform parametercell或坏参数比例返回time的免费步骤。

所以每个这样的µ都有某W与ρ≥δ使(3)严格失败。因µ为概率，失败迫δ^-eρ^q<1，即

    δ≤ρ<δ^(e/q),
    µ{V:d_angle(V,W)≤ρ}>δ^-eρ^q≥δ^(q−e).          (4)

这是对实际原支持的无额外cap假设之必要集中；仅以He为具名高级输入。它严格区分于R102的local-SPREAD条件排除：较弱的全局cap本身已不可能，且当前结论带原权与单个实际尺度。并未声称(4)与完整source存在性等价。

## 4. 按原访问权剥取：正质量覆盖与每簇profile

取µ_0在U上的原权I_u/I_U。在剩余clock集R上仍用I_u归一；由§3反设，取一个违反cap的W_j、ρ_j，并令U_j为R中该cap内的全部实际u，然后删除U_j。各U_j时钟不交；多条T/点可共享同u，I_u始终是原实际访问数。

仅在剩余原质量≥I_U/2时继续。此时每步绝对原权满足

    Σ_(u∈U_j)I_u/I_U > (1/2)δ^-eρ_j^q
                                  ≥(1/2)δ^(q−e). (5)

故至多J≤⌈2δ^(-(q−e))⌉≤3δ^-q步便覆盖至少I_U/2；若已覆盖则停止，有限U无需无穷选择/可测性假设。对每簇同时保留(4)(5)，不只说‘少量薄层cover’。

特别每簇时间数≥I_U µ_0(U_j)/|H|≥L^-C m µ_0(U_j)。重复normal的权不被删去；这是原I分母的集中profile，非distinct方向数估计。最后一个簇仍是在移除前剩余≥half时选出，所以也满足(5)。

## 5. 全局Schubert条件的精确native多项式

对第j个W_j取任意正交列基B_j=(B_1;B_2)∈R^(4×2)。对独立formal变量v∈R、F∈Mat(2,2)，定义

    G(v,F)=((t−v)(F−F_s); (s−v)(F−F_t)),
    P_B(v,F)=det(G(v,F)^T B).                      (6)

每entry为总degree≤2，所以P_B总degree≤4、v-degree≤2、F-degree≤2；所有系数绝对值≤固定C。对实际u、其G满秩，正交化G得到

    |P_B(u,F_u)|=sqrt(det(G_u^T G_u))
                         ·d_angle(G_u⊥,W_j)≤Cρ_j. (7)

等式用的是normal G⊥，而非kernel G本身；B变正交基只改det符号。也可写成det[(t−u)B_1^T(F_u−F_s)+(s−u)B_2^T(F_u−F_t)]。bounded G给(7)upper，不需要把小singular value倒置进误差。

## 6. 系数范数lower：薄层条件不是恒零多项式

采用普通monomial系数的max范数。取formal中点v0=(t+s)/2，它不必属于原Z，F保持独立变量：

    G(v0,F)=(h/2)(F_s−F; F−F_t).

令S(a,b)=(-A^-1(a+b),b)，则S G(v0,F)=(h/2)(I;F−F_t)。||S||≤Cσ^-1、||S^-1||≤C，故B′=S^-T B的两个singular values均≥cσ，其wedge范数≥cσ²。

由Cauchy–Binet，det((I;X)^T B′)的六个Plücker坐标分别配对独立的{1,X11,X12,X21,X22,detX}，只差符号和排列。因此其普通系数max范数≥c||wedge²B′||≥cσ²。X=F−F_t的bounded平移在这六维多项式空间上有bounded逆，不破该lower。乘(h/2)²并用|h|≥σ得

    ||coef_F P_B(v0,F)||≥c h²σ²≥cσ⁴.

formal代入|v0|≤1的线性系数映射norm固定有界，故

    cσ⁴≤||coef_(v,F)P_B||≤C.                      (8)

这没有延拓原rough F，也没有用原time插值。定义Q_B=P_B/||coef P_B||，得到真正norm1、degree≤4的native条件

    |Q_B(u,F_u)|≤a_j:=Cσ^-4ρ_j,
    δ≤a_j≤δ^(e/(2q))  (δ足小).                   (9)

C固定足大；最大厚度由ρ_j<δ^(e/q)、4b<e/(4q)支付。这里是多项式值的sublevel set，不未经梯度lower就称Euclidean距离a_j的零集邻域。

## 7. 归一厚度后的原质量异常与平凡分窗比较

(5)和a_j=Cσ^-4ρ_j给

    µ_0(U_j)>(1/2)C^-qσ^(4q)δ^-e a_j^q
                         ≥δ^(-e/2)a_j^q           (10)

当4bq<e/8、δ足小时成立。每个簇同时满足(9)(10)，这些是本稿需保存的结构信息。

只说J≤δ^-q、各在非零低degree薄层，可能已经由dyadic Lipschitz分窗得到；那种表述不计新gain。普通半径a的原time窗口在原richI权下至多L^C(a+δ)：I_u≤|H|、U⊂原δ-separated clock、I_U≥L^-C|H|m及m≥K^-Cδ^-1给此upper。因此若把a_j-sized单个time窗口直接当U_j，(10)要求的δ^-e/2 a_j^q远大于L^C a_j，不能支付。

还须测试较强的平凡构造：取W等于窗心normal，两principal sines均随plane距变化，故在Lip窗可有d_angle≤L^C l²，而非只O(l)。仅使用这个upper的通用施工可取窗长l为带L费用的sqrt(a_j)量级；取q<1/4时(10)仍远大于这种所选窗口的L^C sqrt(a_j)质量上界。这里没有把l≤L^C sqrt(a_j)声称为真实Schubert cap的窗口长度upper，曲线沿该cycle时可能有更长cap。若取q>1/2而只报此profile，可能已经平凡；本稿不使用该范围。此比较仅拒绝这些朴素分窗证书，不证明任意Lip曲线不可能有(10)：曲线可以沿某Schubert locus运行，正是未解余责。

多项式sublevel无条件的Euclidean厚度转换、所有U_j落同一zero set、全局有理F、固定image/kernel均非(10)的结论；不得删掉ρ_j/µ_j后升级这些结论。若只优化q/e/ρ，不另计信息。

A提出、B独核的严格plane-law校准再排自动profile：令K(z)=graph T(z)，T(z)=((z,z²);(z³,z⁵))、z∈[0,1]，normal V(z)=K(z)⊥。六Plücker函数{1,z,z²,z³,z⁵,z⁶−z⁵}线性独立，故任意W正交基B所给det((I;T(z))^TB)为degree≤6且系数norm统一≥c的多项式。其小值集长度≤Cρ^(1/6)：若长度为l，可在其中选7个相隔≥cl的点，Lagrange插值给sup|p|≤Cρ l^-6，而系数lower给sup≥c。小值集只有固定数intervals，uniform δ-net计数再多Cδ；有界Gram因子遂给每W的det-cap质量≤Cρ^(1/6)（ρ≥δ）。固定q<1/6、δ小便不可能满足(5)的异常lower。该例只是Lip plane-law的资格测试，不同时携带(1)的全坏P_u或完整Def17，不是source反例。

## 8. 原T与平均、逐管mark闭包

令D=∪U_j，只保H中原far/heavy访问且u∈D，总marks J_tot≥I_U/2≥θ N m，θ=L^-C。每原T的这些marks数J_T≤m。按阈值J_tot/(2N)删低J_T管，低管总量≤J_tot/2，故剩下至少J_tot/(2m)≥θN/2条原T，每条至少θm/2个原marks。

这是合法whole-index及shading选择，原absolute CW上界继承；若再归一，按N/N′≤2/θ付费。原tube ADlower、每point完整Φ、filled-X及层Y lower并不自动继承，不能以此称新完整Def17。逐管lower只对union D，单个U_j仅有(5)平均质量；单簇再threshold可以做但须另付其mass成本，且不同j的保留管可不同。

若另限制整个原time层为某U_j以重调source lemma，新的源η、allowed尺度、每层完整数据与平均marks必须按R22闭包重付。尤其q和He未知e(q)之间没有足够的免费强弱比例，不能把δ^-q数量损失冒δ^(e/q)正增益。这是当前不能返回完整branch saving的实质预算，非技术常数已解决的假象。

## 9. 旧指纹、严格反攻与不可越过的范围

R78在R76最终δ²原mass单block上，经共同X、He1611矩阵sumproduct得一个fractional invariant-line cone；本稿用另一He1710投影定理、全局P2Fst和每原u的大P_u，在原full incidence的L^-C比例上给带每簇尺度mass的cover。旧单block结论没有自动支付这一原分母；反向由本cover恢复R78共同X或原fullsource也未证，故不声双向等价或新增全称正gain。

R79 rough上三角native模型可使所有G_u也上三角；W=span(e2,e4)时B^T G_u首列为零，P_B(u,F_u)恒零。它满足所审弱接口而缺完整point-Φ/filled-X/joint4AD-CW，故只反‘原timeAD/SM/满秩自动给全局cap’，不是完整Def17/Kakeya反例。形式Q_B仍非零，但可在原F的proper algebraic族上恒零，吻合§6。

R102中scalar affine F_u=uI同样可给恒定G-plane，且(4)允许对一点质量1选细ρ；这仅校准cap失败，非新counter。R97某固定Segre的local切平面障碍不等于本global cap，本稿不续该参数，也不解冻CP/PM/PW/BSG/action的全称gain改名。

## 10. 结论、审查与停止

实际付清候选：在完整源的既定det-large分支和具名He Th1下，R102全局码小投影迫(4)任意支持原权的cap异常；由此在至少L^-C原N m上得有限不交clock簇、非真空native degree≤4 sublevel条件与逐簇(5)/(10)，并可在union上恢复许多原T的逐管marks。不是无条件对所有rough F的一般定理，也不覆盖未提取det-large的余分支。

审查应全文核源Th1/all-large-subsets、减e单调化、原P同δ cover、任意原权/重复normal、half停止、normal对偶、formal中点及Plücker系数lower、sublevel与metric分清、尺度mass非平凡性和平均/逐管闭包。He33页advanced wholeproof保具名责任，独立应用审查不等外部同行评审。

若终审通过，只登记真实原质量集中用途，不新ID/major/novelty/ordinary或fullκ1。后续需要利用完整原point-pencil/filled-X/CW对这些Schubert集中簇取得新几何或返回ambient，不能用增加cap/有理F假设、少簇cover表象或q/e/ρ微调结束下一轮。完整Goal保持active。
