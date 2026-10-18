# R0076：实际双端码到原生乘积的全时钟细尺度模型

2026-10-18，root。先锁research/rounds/R0076_working_spec.md§2后施工。以下是完整bounded matrix33、κ=1源的一个实际det-large分支的归约和两个直接增长出口的反攻，不是κ1排除或重大结果。原WZ/CSWZ高级定理与本项目证明分开；未经外部同行评审。正式独审完成情况另记，不预写通过。

## 1. 量词、原数据和分支

取WZ2609.22035v1 Def17.2–17.4的d=5、k=ell=3、κ=1全部数据，另明确原whole T处于一个固定bounded joint chart，N=#T在K^-1δ^-4与Kδ^-4间，原normalized CW≤K。F_t为bounded 2×2矩阵，Z⊂[-1,1]、m=#Z；各Y_t为native δ-separated AD1，#Y_t∈[K^-1δ^-1,Kδ^-1]，X填充二维，point Φ AD1/slabγ和selected ξ/coherence均为原数据。K=δ^-C0η吸收固定有限次原费用；不假physical direction separation、smoothness、商ADlower或goodrank。

每根原heavy管T有完整原访问集S_T⊂Z，#S_T≥K^-C0 m；在每个访问时刻确定地选一个原p_t(T)∈E_t和其原ξ，只有Oδ物理误差，保留后仍不删S_T。令σ=δ^b、τ=δ^a，0<a,b小。分支输入是原计数

    Σ_(t,s) #{T heavy:t,s∈S_T, |s−t|≥σ,
                        smin(F_t−F_s)≥σ} ≥ τ δ^-4 m².       (1)

这不是独立F-pairs假设，不声称该分支涵盖全部源。设L=C K^C τ^-C σ^-C，其中C是下文有限计数所需固定维数常数。给定β>0，先选a,b，再η足小、δ最后，可令L≤δ^-β；不能将a,b费用藏进K。

## 2. 精确结论和不能推出的内容

由(1)可选一对原t,s及一个实际原管子族H*，使

    L^-1δ^-2 ≤ #H* ≤ Lδ^-2,
    L^-1δ² ≤ #H*/N ≤ Lδ².                           (2)

H*保每条原T的全部S_T。在完整、未经替换的Y_t×Y_s×Z上存在0≤g≤1，且

    Σg ≥ L^-1 |Y_t||Y_s|m.                           (3)

若g(y,y',u)>0，则

    B_u+C_t(u)y+C_s(u)y' ∈ N_(Cδ)(Y_u),              (4)
    λ=(u−t)/(s−t), A=F_t−F_s,
    C_t=(1−λ)(F_u−F_s)A^-1,
    C_s=λ(F_t−F_u)A^-1.

B_u明确包含一个共同joint residual轴的normal correction。系数范数≤Cσ^-2，并非统一O1。实际g由原同管visits构造，没有独立化；不保active Y-subset的ADlower或原filled X/Φ lower，不将(2)说成原T的δ^o(1)大比例。此结论本身没有任何fixed-power增长。

## 3. 实际两端selected ξ恒等式

选(1)中边数≥τδ^-4的一对t,s，h=s−t。原同管端点写p=(x,y+F_t x,t)、q=(x',y'+F_s x',s)，其原斜率为(φ,ξ_p+F_tφ)+Oδ，也是(φ,ξ_q+F_sφ)+Oδ。bounded原坐标保证所有直接乘法误差Oδ。于是

    x'=x+hφ+Oδ,
    ξ_q=ξ_p+Aφ+Oδ,
    y'=y+hξ_p+A x'+Oδ.

定义CL(p)=(y+Ax,y+hξ_p)、CR(q)=(y'−hξ_q,y'−Ax')，得到CL=CR+Oδ。同一原T仅计一条带T-label的边；若原访问可选多个points，事先确定选一个，不能在不同用途重选相互不兼容端点。这一恒等式是后面真实参数重建的来源，不是假graph completion。

## 4. Fine code、重边和双侧剥离

将CL/CR取δ网格cell号。相差Oδ意味着右号减左号仅有限O(1)个offset；先选一个offset保固定比例总边。此后每个左cell只配一个右cell，反向亦然。再对这一实际多重图做双侧weighted-degree peeling：顶点总数≤CKδ^-3，阈值D=cτK^-Cδ^-1，所有被删顶点总计带走≤D·CKδ^-3，不超过初始边一半。剩余非孤立端点weighted degree≥D。没有授予这些端点filled X、Φ或ADlower。

固定(p,q)的原T重数≤C|h|^-4：两个物理点将四维slope局限在半径Cδ/|h|，每δ-slope格只有O(1)个through-p的dyadic intercept选择。故重数M≤Cσ^-4，不能把多重图weighted degree直接等同邻点数。每个非空code块两侧各至少D/M个顶点，所以块数

    ≤ CKδ^-3 M/D ≤ Lδ^-2.                           (5)

保留边数≥cτδ^-4，故某块实际不同T数≥L^-1δ^-2。左右码cell均距一个共同中心(U,V)为Oδ；不是将近码误写精确等码。

## 5. Native标签纤维与原质量

固定左码块及native y，则x∈A^-1(U−y)+B_(Cδσ^-1)，二维δ-packing给≤Cσ^-2个原端点。右侧固定y'也同样。每侧全部端点数≤CKσ^-2δ^-1。结合每pair原T重数≤Cσ^-4，该块全部T≤Lδ^-2，给(2)的上界；下界还将在残差选择中付损失。原N仍是全部原N，因而(2)的δ²不能抹去。

本块相对native两个AD1满域有可用密度，原CW若重归一到该块最多乘N/#H*，可能为Lδ^-2；绝不称原CW常数保留。我们只使用继承绝对count/upper和原T轴，不将该块当新的完整Def17配置。平均shading和逐管dense不同：本论证用的是每条已选heavy T的#S_T下界，不由全体平均直接赠给全部active T。

## 6. 理想两端轴与全局参数误差

保留每条边的精确native y,y'；不要先将它们coarse round。令

    x̃_t=A^-1(U−y),     x̃_s=A^-1(y'−V),
    z̃_t=y+F_t x̃_t,   z̃_s=y'+F_s x̃_s.

由这两个端点唯一确定理想四维physical axis ℓ_(y,y')(u)=(1−λ)(x̃_t,z̃_t)+λ(x̃_s,z̃_s)。真实原轴ℓ_T在t,s与原端点Oδ接近，fine code及||A^-1||≤σ^-1给端点真实−理想误差≤Cδσ^-1。转为全局参数ℓ(u)=b+uv，再付|h|^-1，所以

    |(b_T,v_T)−(b_(y,y'),v_(y,y'))| ≤ Cδσ^-2.       (6)

这只是δ^(1−2b)参数精度，不能据此宣称(4)为fine Oδ。即使两个anchor输出精确，所有bounded u的误差也可能被1/h放大；下一步必须实际执行。

## 7. Joint residual分桶真正修复fine δ

把(6)中八维residual r_T=(b_T−b_(y,y'),v_T−v_(y,y'))按边长δ的网格分桶；至多Cσ^-16桶。选择包含最多原T的一桶，保≥C^-1σ^16比例；共同桶代表记(e_0,e_1)∈R4×R4。对桶内每条原T以及**全部**u∈[-1,1]，

    ℓ_T(u)=ℓ_(y,y')(u)+e_0+u e_1+Oδ.               (7)

没有删任何原S_T，也不对每u重新选residual。损失只进L，所选H*仍满足(2)。若同(y,y')有多条T，理想参数固定，(7)将其真实dyadic八维参数限在固定Oδ盒，故重数≤一个只依维数/固定常数的M0。这一有界重数不需要原T方向δ分离或商ADlower；不同joint δ-cell的原dyadic管本来唯一。

如果还要把双侧min-degree作为最终图的附加性质，可在此桶内再peel，阈值c#H*/(#P_block+#Q_block)，由第5节端点upper至少c#H*/(CKσ^-2δ^-1)，保固定比例边、再付L；(2)–(4)不依赖额外peel。最终g不是此前粗度数图的任意补全。A实际独审指出初稿optional阈值漏σ^-2，本终稿已按真实端点数修复。

## 8. 全第三时钟输出与g的实际构造

将e_j=(e_j^x,e_j^z)分成两组R²。理想轴的native normal为z̃(u)−F_u x̃(u)，展开并合并y,y'得(4)的C_t/C_s，常数为

    B_u=(1−λ)(F_t−F_u)A^-1U
          −λ(F_s−F_u)A^-1V
          +e_0^z+u e_1^z−F_u(e_0^x+u e_1^x).        (8)

特别是第二项负号不可反。原T在u∈S_T有真实原native Y_u访问，(7)及F_u bounded给(4)的Oδ；这里不需F_u smooth，global u只需bounded。λ可大，||C_t||+||C_s||≤Cσ^-2，已付费用。

定义

    g(y,y',u)=M0^-1 #{T∈H*:native endpoints=(y,y'),u∈S_T}.

由第7节g≤1，且Σg=M0^-1Σ_(T∈H*)#S_T≥L^-1δ^-2m。完整native域大小≤K²δ^-2m，吸收K得(3)。每个positive weight对应实际同一原T的三个访问，仍保原clock的联合相关；各u的边权可以不同，不存在一张自动对所有u独立的满乘积图。

## 9. 自然能量范围和旧闭包排重

令n=δ^-1，G_u=Σ_(y,y')g(y,y',u)。把(4)的输出分配给覆盖N_CδY_u的O(Kn)个fine δ-cells，记权r_u(w)。Cauchy–Schwarz给Σ_w r_u(w)²≥G_u²/(CKn)。再对原u求和，用(3)，得到总restricted weighted collision energy≥L^-1 m n³。单个有G_u≥L^-1n²的u也有≥L^-1n³。该自然n³预算不同于R18二维observed W＋角维1的旧预算；没有用数值代连续证明。

但这是随u、随两个不同matrix coefficient的restricted能量。Y_u随u变，g_u随u变，C_t或C_s可降秩；它不授共同作用集合、加法闭包或独立卷积small image。实际对照He1611.09639v2 Th2–3：矩阵algebra版需away from every proper subalgebra，action版需quantitative irreducibility和同一个X，结论还含X+X或X+aX；这些不是(3)–(4)的输入。He–de Saxcé1806.06375v3 Th1.1/2.4/Prop2.5另需quotient nonconcentration、away from subgroup/stabilizer等，亦未付。这里只核接口，未重证高级wholeproof。反向从任意满足(3)–(4)的g重建原full T、CW、filled X、全部Φ/coherence也未证。因此不是旧全称gain的双向等价改名，也不是证明了新增长定理。R18/23/28旧BSG/action/carry和R71/72basicness/更多fixedtime冻结不撤。

## 10. 共同点law的直接CSWZ出口严格不适用

固定root t，Σ_t={(x,y,ξ_p):p∈E_t}的原均匀law有3-Frostman upper：joint(x,y,ξ)小球必约束physical(x,y+F_t x)小球；Y AD1与X二维packing给Cr³K，相对#E_t≥K^-Cδ^-3计。不要求Σ_t光滑。不同s的左码是同一law上的L_s(x,y,ξ)=(y+A_sx,y+h_sξ)，核为

    K_s={(-A_s^-1v,v,-h_s^-1v):v∈R²}.

对固定非零l，W_l={l·y=l·ξ=0}为R6中4-plane；取非零v⊥l，必有K_s∩W_l≠{0}。注意primary的output4参数是normal 4-plane K_s⊥，对应与固定2-plane W_l⊥相交，不能混淆k。将L_s输出左乘diag(A_s^-1,h_s^-1I2)，得到primary形式π_θ((x,ξ),y)=(x,ξ)+θ_s y，其中θ_s=(A_s^-1;h_s^-1I2)∈R^(4×2)。两个offdiagonal恒零；一个坐标为零即CSWZ Def1.5前的rank-one-normal model hyperplane。对任何子族、每个中心、所有大于fine-cell厚度的尺度均singular。要满足(δ,s,δ^-ε)-spread-out，须ε至少支付s数量级的整尺度奇异费用，不能满足所需小ε接口；系数chart若先按σ费用归一，结构零仍在。

所以[CSWZ v1 Def1.4–1.5/Th1.7](https://arxiv.org/html/2610.13682v1)不能直接用于这族码投影，哪怕det-large、time AD和原SM均成立。几何固定Schubert包含也不会因换一个bounded chart消失。不能把vary-root t当共同点law不变，亦不能把“有共同law”说成已给spread-out。此为严格调用障碍，不是fullsource反例或所有商因子方法不可能。

## 11. Native自动满秩接口的独立反例范围

仅检验更弱断言：两个AD1/tubeKT native集、全第三clock和dense g是否自动迫使C_t,C_s满秩或输出增长。取t=0,s=1,F_t=I,F_s=0，故A=I、h=1；在U=[1/4,3/4]的全δ-clock上令F_u=P=diag(1,0)。设C为标准四进Cantor集的δ-net，dim C=1/2，Y_t=Y_s=C×C；取Y_u=(1−u)C×uC，g≡1、B=0。则

    C_t=(1−u)P, C_s=u(I−P),
    C_t(y_1,y_2)+C_s(y'_1,y'_2)=((1−u)y_1,u y'_2)∈Y_u.

两个系数各rank1，输出仍AD1，没有增长。C×C的δ-net为AD1，并有tubeKT1/2（适用于要求1−γ≥1/2的弱接口）：任意r×τ管按长方向横/纵二选一分r格，另坐标截面O(r)，乘Cantor半维计数得O((τ/r)^(1/2))；中间u的缩放常数统一有界。B独稿§8用buffered四进Cantor有限集使所有scaled输出也δ-separated，给出了全部尺度的确定性证明，而非数值样本。

该校准甚至保同一批真实whole-clock直线：x(u)=−(1−u)y+uy'、z(u)=uy'，原两端ξ分别−y、y'，CL=CR=0，且在全U实现上述输出。但原管参数仅AD2、#T≈δ^-2；单根δ-tube凸罩测试给CW≥cδ^-2，内部point仅固定根管、horizontal native fibre只有维1而非filled X2；F_u平台也不满足原SM/19.4。故它只是否决所列弱接口，不是Def17反例，未证明原全clock/Y/Φ/CW源可如此实现。

## 12. 本轮结论、独审责任和停止

本轮实际付出的是：(1)原sameT分支→native双端块，带真实δ²原全T质量；(2)八维joint residual细分，保全部原第三clock，给fineδ、bounded multiplicity和真实g；(3)restricted自然能量；(4)直接CSWZ奇异障碍及自动rank弱接口反例。它超过code恒等式/peeling的摘要，但仍没有critical κ1 fixedgain、完整Def17反例、ordinary/general结论、重大性/新颖性或新数学ID。

正式独审须全文核第4节offset/多重度、第7–8节fine residual/B符号/全clock/重数、第10节primary尺度和第11节反例范围。原归一化是R43旧闭包，本轮只核原§18输出bounded；literal无界首调用不能倒推已付。停止再以本模型换名desired inverse、free BSG/commonA/goodrank或更多fixedtime续轮；下一需对完整原条件作有实际用途的不同结构提取或换总目标路径。Goal active，未经外部同行评审。
