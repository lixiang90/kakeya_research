# R0092：有限域加权转移、真实阴影与单轨道精度预算

2026-10-18。固定n≥2；主输入是已有Ellenberg–Oberlin–Tao0903.1879v2 Th1.3（EOT），本稿独立证明具体Euclidean转移。所得s_n=n²/(2n−1)，n5仅25/9，**不是新维数界/重大结果**。未经外部同行评审。

## 1. 原目标、量词与明确模型

目标仍是ordinary n≥5/general Hausdorff Kakeya的证明、真同集full方向低维反例或重大中间结果。本轮检验全方向实单位段到有限域完整方向的真实转移，非R56近jet conditioning，亦非R91rank/C1续门。

令p为充分大prime，α=2−1/n，h=c_n p^{-α}，c_n>0固定足够小。T族为有限单位长半径h圆截面管，可用flat-ended圆柱或单位线段的h-neighborhood（带圆帽）；轴方向构成S^{n−1}上的h-separated h-net。允许有向球面参数，换无向参数只改常数。各Y_T⊂T Lebesgue可测，E=∪_T Y_T，λ=N^{-1}Σ_T |Y_T|/|T|。所有管体积均≈_n h^{n−1}（统一管形时相等），λ∈[0,1]。位置可任意；有限族的E有界，常数不依位置。证明

    |E| ≥ c_n λ^n p^n h^n = c'_n λ^n h^{n−s_n},
    s_n=n²/(2n−1).                                      (1)

本命题不是任意稀疏/任意带权方向law的无损结论。Hausdorff读出另在§9支付；裸box计数不能代它。

## 2. 全模方向的短整数代表

每个L∈P^{n−1}(F_p)取非零v∈L。p个点tv（t∈F_p）取canonical整数代表在[0,p)^n。分成q^n个半开cube，q=floor((p−1)^{1/n})，q^n<p。同盒两个点差b_L满足

    b_L mod p ∈ L\{0},  0<|b_L|∞≤p/q≤C_n p^{1−1/n}=:M.

差的field scalar非零是prime性质，不能直接搬到composite。置θ_L=b_L/|b_L|。不同模projective方向不可能有实平行整数代表：若两整数向量共实直线，写成同一primitive整数向量的整数倍；因两者modp都非零，倍数均为unit，故mod方向相同。因此不同L的非零整数二阶minor给

    sin angle(θ_L,θ_{L'}) ≥ c_n/M².

而hM²≤C_n p^{-1/n}→0。故所选真实方向在h尺度远分离，且p h|b_L|≤C_n c_n。选c_n使后者≤1/10，连续p个物理step可放在单位段固定短内段。所有误差都是同一各向同性h格，不赠独立方向和clock的网格精度。

## 3. Haar旋转支付平均density

设V_T为原h-net的球面Voronoi cells，边界作可测tie-break。每cell含h/2球面cap且包含于h-cap，故σ(V_T)≈_n h^{n−1}，N≈_n h^{1−n}。定义f(v)=λ_T=|Y_T|/|T|于V_T。则∫f dσ≥c_n λ。

Haar随机R∈O(n)时，每个Rθ_L均匀于球面。因此某个R满足

    D^{-1}Σ_L λ_{T(L)} ≥ c_n λ,  D=|P^{n−1}(F_p)|≈p^{n−1},

其中T(L)是Rθ_L的最近原direction管。角差≤h，且由§2间距，L↦T(L)对充分大p为单射。这不是固定稀疏方向抽样的平均闭包：指定抽样labels可以全删而全族平均趋1。这里R依实际λ_T自适应选择；单射与Voronoi质量已分别付费。下文物理格也取旋转格RhZ^n。

## 4. 真实cell occupancy与整格包含

令Q_A=Rh(A+[0,1)^n)，A∈Z^n，定义

    w_A=h^{-n}|E∩Q_A|∈[0,1],  Σ_Aw_A=h^{-n}|E|,
    g(x)=w_A  (x∈Q_A).

取固定足够大的整数J=J_n，w_A^+=Σ_{|B−A|∞≤J}w_B。则0≤w_A^+≤C_n，Σ_Aw_A^+≤C_n h^{-n}|E|。若x距网格node RhA≤C_n h，含x的cube就在这个固定邻域，因此g(x)≤w_A^+；J最后按以下统一舍入常数选定。

对T=T(L)，所有与T相交的h-cubes的并包含在一条沿Rθ_L、半径C_n h、长度C_n的cylinder C_L内，因为原角差≤h。并且

    ∫_{C_L}g ≥ Σ_{Q_A∩T≠∅}w_A h^n ≥ |Y_T|.

**不声称直接∫_Tg≥|Y_T|**，细胞平均可能来自T外。将相交格整格放进C_L才是合法步骤。Fubini在C_n h横盘上给一条精确平行Rθ_L的直线x_L+tRθ_L，在某长度≤C_n的interval I_L上

    ∫_{I_L}g(x_L+tRθ_L)dt ≥ c_n λ_{T(L)}.          (2)

真实原E质量始终以w计，没有将|E|替成较大邻域体积。

## 5. Clockphase、共同anchor和mod重数

记τ_L=h|b_L|，于是pτ_L≤1/10。对s∈[0,τ_L)积分，phase恒等式给

    ∫_0^{τ_L} Σ_{j:s+jτ_L∈I_L} g(x_L+(s+jτ_L)Rθ_L)ds
      = ∫_{I_L}g(x_L+tRθ_L)dt.

故可选s_L使sample和≥c_n λ_{T(L)}/τ_L。将x_L+s_LRθ_L舍入成RhA_L，误差≤C_nh。每个sample对应node Rh(A_L+j b_L)，其与sample差是同一Oh向量，§4邻格和逐点支配。

所有sample j位于长度≤C_n/τ_L的整数interval。对同一residue j modp，重复数≤1+C_n/(pτ_L)。不能免费乘bounded-box内lift数量；这里恰支付clock碰撞。定义同一个有限域函数

    F(z)=max_{A modp=z} w_A^+,  z∈F_p^n.

E由有限管族承载，w有限支撑，max有定义（全零取0）。modp的A_L+j b_L沿方向L，因为b_L modp≠0。于是

    p^{-1}Σ_{z∈A_L+L} F(z)
      ≥ (c λ_{T(L)}/τ_L)/(p+C_n/τ_L)
      ≥ c_n λ_{T(L)}.                              (3)

这没有将任意shading变成完整fieldline；只得到完整fieldline上的**函数平均**。选中physical sample可跨多个period，重数已在式(3)收费。

## 6. EOT归一化与原Lebesgue体积返回

EOT Th1.3用unnormalized counting ℓ^n和line sum。对F≥0，令F*(L)=sup_a p^{-1}Σ_{z∈a+L}F(z)，精确等价形式为

    Σ_L F*(L)^n ≤ C_n p^{-1} Σ_z F(z)^n.             (4)

本稿将其作为标准具名输入，未新认证其整25页高级证明。由(3)、§3及Jensen，左侧≥c_n λ^n D≥c_n λ^n p^{n−1}。另一方面，F≤C_n且max≤sum，故

    Σ_z F(z)^n ≤ C_n Σ_A w_A^+ ≤ C_n h^{-n}|E|.

代入(4)得式(1)，包括λ=0和任意小λ，不需λp≥1额外门槛。整个proof没有使用独立fibres、无损full角抽取、PW/CW、局部椭圆性或特殊可测shading形状。

只用Dvir集合版时也可先取体积≥cλh^n的heavycells、好方向/partialline richness，再用低degree polynomial得到λ^{n+1}p^nh^n；此为A/B已独核备份。EOT的函数输入支付了去掉该额外λ，不能把集合版直接当函数版。有限n时两者的Hausdorff弱指数相同，不另开λ小改方向。

## 7. 精度预算和不允许的扩大声明

考虑本轮指定的共同h格/直算术progression接口：每个模projective方向需一个整数step b≠0 modp，并要求连续p步在某真实长度≤C_n的clock中（允许Oh误差）。若max|b|∞=M_0，则

    #P^{n−1}(F_p) ≤ #(Z^n∩[−M_0,M_0]^n) ≤ C_n(M_0+1)^n,
    M_0≥c_n p^{1−1/n},  (p−1)hM_0≤C_n,
    h≤C_n p^{−(2−1/n)}.                            (5)

短代表构造达到该最坏幂。仅由模影像总点数（最多p^n），或本轮F≤C、max-lift规范得到p^n h^n的volume证书，在这一完整orbit尺度安排下，其指数至多s_n。它不是某个原Kakeya集合实际维数≤s_n的上界，更不是所有有限域/有限环/各向异性/多块/多尺度算术法的不可能定理；额外原lift重数或不同编码不在此接口内。p^-2仅直接长代表方案，不能冒所有策略的精度必要性。

对于Z/p^kZ，pigeonhole的标量差未必为unit。例v=(1,p^{k−1},0,…)是primitive方向，每个unit倍的第二坐标centered大小至少p^{k−1}=N/p。固定p、k→∞时，该单完整N-orbit primitive代表方案有M_0≳N，故h≲N^-2。这里只是实数转移费用，不能用更强环计数抹去；也不否所有环编码。

## 8. Restriction、方向与体积反攻范围

逐管density≥λ当然给平均density≥λ，式(1)直接适用；平均则经Haar/Jensen处理，不能先声选中所有mod方向每个都有密度λ。指定稀疏sampling可全删、删一个clock点即可破完整fieldline，这些严格反攻与本稿自适应函数平均桥不矛盾。

删label后一般不再是满h-net；没有免费的arbitrary sparse/weighted闭包。若要调用式(1)，可保留原h-net labels并令删掉的Y为空，均值按**原N分母**变成retained mass/N，不能按剩余N重新声同λ。一般权重或任意方向family需要独立公式，本文不赠。Wholeclock对象的mod影像≤实际nodes，只能作lower返回；不能将每residue至多若干lift反过来乘进lower。

常见斜率chart错误亦排除：取方向(k/p,1)、clock j/p、乘p²再modp时vertical增量p变零，不能当全F_p^n方向。本稿直接整数向量b_L与物理步h b_L避开它，不依错chart来声25/9。

## 9. 任意K的Hausdorff读出必须另付

下面只复得弱界dimH K≥s_n，不称新结果。若任意K包含所有方向unit segments且dimH K<s_n，取t满足dimH K<t<s_n。R91同维Gδ hull/开段关系/JvN的构造在Rn原样适用（其证明不使用n=5的特殊性质），得同维G和标准Borel a.e段选择a(v)。令x_v(u)=a(v)+uv，u∈[0,1]，σ-a.e.整段在G。该选择不需有界，也不声spt⊂G。

因H^t(G)=0，可选全半径<2^{-K_0}的开球覆盖，Σ_i r_i^t<1。按2^{-(k+1)}<r_i≤2^{-k}分组，U_k为该组球并，M_k为其数；每M_k有限且Σ_k M_k2^{-kt}≤2^t。定义ℓ_k(v)=∫_0^1 1_{U_k}(x_v(u))du，m_k=∫ℓ_k dσ。它们可测，Σ_{k≥K_0}m_k≥1，因此某k≥K_0有m_k≥c/(k+1)^2。

由Bertrand在P与2P之间取prime，P=(c_n/2^{-k})^{1/α}，使h=c_n p^{-α}与2^{-k}同常数可比。固定一个h-net，Haar旋转后其有限方向集的平均ℓ_k至少m_k/2，且避开选择异常零方向（有限多个方向的bad事件概率零）。每个方向取其真实G内单位段并加半径h的flat-ended圆柱管，Y_T=T∩(U_k)_{+h}。每个marked axis-clock的整h截面属于该shading，故λ_T≥ℓ_k(v_T)；平均λ≥m_k/2。若统一改带圆帽管则同样有λ_T≥c_nℓ_k、λ≥c_nm_k，以下仅改常数；没有删帽而丢小λ质量。

应用式(1)，同时(U_k)_{+h}只需M_k个半径C_n h球覆盖，得

    C_n M_k h^n ≥ |∪Y_T| ≥ c_n m_k^n p^n h^n,
    M_k2^{-kt} ≥ c_n(k+1)^{-2n}2^{k(s_n−t)}.

取K_0足够大，右侧对所有k≥K_0均>2^t，与覆盖总费用上界矛盾。这里用到了全λ的真实平均shading估计、可测选择、prime尺度可比和t<s_n正gap；**不是从单尺度cover下界自动得到Hausdorff**。没有复用或更改DIM001条件六维17/4，所得弱界在本项目已知范围内严格无改进。

## 10. 宏观判定和停止

本轮正向链已从真实平均Lebesgue阴影回原E，并付任意K的弱Hausdorff读出；有限域输入不是欧氏一般猜想的证明。n5仅25/9，甚至弱于经典一般下界，不能作新ordinary增益、完整branch saving、重大中间结果或新数学ID。R56近jet、旧FSD/DIR和本轮算术资格不同，但最终未提供更强K(n,d)或实际critical κ1输入。

停止这个共同格/完整orbit/mod影像或bounded max-lift的直接转移，不续prime/λ/代表norm常数小改。ordinary/directHRZ/sticky余branch/真同集反例四完整路及原Goal仍open，旧PDE/cut/cone/polar和CP/PM/PW正幂冻结保持。若重开，必须有不同的原多尺度lift质量或编码，不可假设它再称新gain。来源高级证明保具名，项目应用须两份实际全文独审，未经外部同行评审。
