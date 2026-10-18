# R0076阶段II：临界同管双端code到完整native乘积时钟

2026-10-18，A。实际全文读本轮working_spec五节的阶段II锁题，沿用R16原witness选择和R75 GLOBAL同管重管规范；本稿独立核具体计数和fine误差，不把阶段I的归一化核清当主数学。只编辑本授权稿，无Git、下载、元数据或新代理。输入高级source及外部定理wholeproof仍具名，未经外部同行评审。

## 1. 完整原输入、所证命题与参数单位

输入为显式bounded原whole joint chart的WZ Def17.2–17.4、d5/k=ell3、κ=1配置。m=#Z≥K^-1δ^-1，原N=#T≈_Kδ^-4、normalized CW≤δ^-η。F_t∈Mat2 entries bounded；E_t={(x,y+F_t x,t):y∈Y_t,x∈X_(y,t)}，各Y_t原AD1，X为二维filled，point Φ_p原AD1/slabγ、ξ及dyadic coherence均保。K=Cδ^-Cη统一有限次源费用，不能吞下后选fixed a,b。

固定目标损失β>0，先取a,b>0足小，再η足小，δ最后；记σ0=δ^b、L=K^C0 δ^-C0(a+b)，C0只依固定维数和选择规范，可一次固定足大。下文所有polynomial condition-number损失均列入L。主张只针对实际sameT长clock、det-large分支：原重管H保每条T的全部selected访问时刻S_T，n_T≥K^-C m；且

    Σ_(T∈H) #{(t,s)∈S_T²: |s−t|≥σ0,
                         s_min(F_t−F_s)≥σ0}
       ≥δ^a δ^-4 m²。                                      (1)

本稿证明在此分支下存在原t,s、一族原重管H*、精确native端点labels和0≤g≤1，使#H*≥L^-1δ^-2且每管保完整旧S_T，g相对完整Y_t×Y_s×Z的均匀reference密度≥L^-1，全u的实际native输出在Oδ内落Y_u，并给出共同系数公式。没有证明(1)在完整κ1源中必出现，也没有从该模型取得κgain。

## 2. 原GLOBAL关联、重管与全时钟先验

每个原point及每个occupied fine Φ_p-bin选Def17.2已给的一根管作见证。固定tube/time截面直径Oδ，原E_t是δ-separated，所以该tube/time只有固定数实际points；取一个canonical point只损固定倍计数。记所得selected图G⊂T×Z。它的每time点数≈_Kδ^-3、每point管度≈_Kδ^-1，故

    I=|G|≈_K mδ^-4，N≤Kδ^-4。

以I/(2N)为阈值删除light tubes而保余管全部原访问，余H满足Σ_H n_T≥I/2、n_T≥K^-C m及#H≥K^-Cδ^-4。两时刻必须来自同一实际原管；Σ_H n_T²≥K^-Cδ^-4m²是真sameT Gram。分支(1)是这个原图内的真实计数，不是任意edge g或两个独立arms。

这里平均incidence给tube-heavy，重管之后则每留下的T都有逐管访问数lower。后续只选whole tubes，不改其S_T，所以这个逐管下界真正保留。原whole T和CW分母始终未被替换；H及下文H*均不被重新宣为AD4或原CW常数不变。

## 3. 固定实际两时的图与平行边重数

由(1)在至多m²个有序times中平均，选一个实际(t,s)，令h=s−t、A=F_t−F_s，满足|h|≥σ0、s_min(A)≥σ0，且这些times都有访问的重管数M≥δ^aδ^-4。每条T确定canonical p_T@t、q_T@s，边label就是T，因而同一T只出现一次。

左／右vertices均为原E_t/E_s的selected points，#P+#Q≤CKδ^-3，每个point的selected管degree≤Kδ^-1。但这是带平行边的图：固定实际p,q，tube slope在R4中被其两端点限制到半径Cδ/|h|；每个fine slope-cell只有固定数intercept-cells。故

    mult(p,q)≤C|h|^-4≤Cσ0^-4。                            (2)

也可用point Φ upper改善部分费用，但本证无需此改进。不能把δ-near两端点当作只确定一根δ管；缺失的h^-4会影响下文block数。原tube参数是δ-separated dyadic cells；共同有界chart变换只改固定常数。

## 4. 双端selected ξ恒等式及有限cell offset

用原native精确labels写

    p=(x,y+F_t x,t)，q=(x′,y′+F_s x′,s)。

同管方向的horizontal分量为φ，原两端selected兼容给

    x′=x+hφ+Oδ， ξ_q=ξ_p+Aφ+Oδ，
    y′=y+hξ_p+A x′+Oδ。

这里全部为fine实际δ误差；F、ξ、clock bounded，未换ρ-proxy。于是

    C_L(p)=(y+A x, y+hξ_p)，
    C_R(q)=(y′−hξ_q, y′−A x′)，
    C_L(p)=C_R(q)+Oδ。                                    (3)

将两个R4 codes都放入同一半开δ-grid。其cell-index差只取固定有限个offset。先选保至少固定比例M的一个offset，再作下节peeling。这样左code cell j只与右code cell j+k相连，blocks确不交；不是把“相距Oδ”当作精确等价关系的传递闭包。

每point的code由它本身固定，选offset只删边、不复制vertices。之后边数M0≥cδ^aδ^-4，点数／度upper及平行重数(2)仍有效。

## 5. 双边peeling、真实block数与端点纤维

在所选offset图反复删当前degree<d0的左或右point，degree按原T平行边计，取d0=M0/[4(#P+#Q)]。总删除边≤d0(#P+#Q)≤M0/4，故余图至少M0/2边，且每非空vertex度≥

    d0≥cK^-1δ^aδ^-1。                                    (4)

所有邻居在同一code block。由(2)，每occupied block至少含d0/(Cσ0^-4)个右vertices；blocks的右vertices不交，所以

    #blocks≤CK²δ^-2-aσ0^-4≤Lδ^-2。                         (5)

另有固定code的native纤维upper。若左code在一个δ-cell中，给定**精确**y∈Y_t，第一坐标y+A x限制x于半径Cδ/σ0的ball，故其δ-separated x点数≤Cσ0^-2。每(x,y)确定一个physical p；第二坐标只再限制ξ而不增加points。因此左fiber≤CKσ0^-2δ^-1，右fiber同理。总记

    #P_j,#Q_j≤Lδ^-1。                                      (6)

这个upper不授active Y-labels的ADlower或原filled X；peeling后的vertices可能很稀疏。原完整Y_t、Y_s继续作为reference，未被替换成这些active fibres。

## 6. 选一个code块的原管质量与本地乘积尺度

由(5)取一个block，其真实原边／管数M1至少

    M1≥cK^-2δ^{2a}σ0^4δ^-2≥L^-1δ^-2。                     (7)

其左、右codes的centers记(U,V)和(U′,V′)，两者相差Oδ；以下共同使用左center U,V，offset误差保在Oδ。每条所选T仍有原完整S_T，n_T≥K^-C m。由(6)及point degree upper，M1≤Lδ^-2；与原N≈_Kδ^-4相比，该单block仅有

    L^-1δ²≤#T_block/N≤Lδ²。                                (8)

这是自然δ²原全管质量，不能写成K^-C比例。局部完整native product有#Y_t#Y_s≈_Kδ^-2，故(7)正好匹配这个本地frame。后续在此frame的nearfull并不把稀有单块提升成原全局nearfull配置。

精确labels y、y′均保原实值，不以code中心或更粗native格代替；若原记法含有限重复native标签，可先沿R16固定δ-separated代表并将有界/K重数全列入L。模型不要求所选active labels自己AD正则。

## 7. 用精确native labels重建理想whole axis

对每条block管的两端native labels (y,y′)，定义理想horizontal端点

    x_t^0=A^-1(U−y)，x_s^0=A^-1(y′−V)，
    p_t^0=(x_t^0,y+F_t x_t^0)，
    p_s^0=(x_s^0,y′+F_s x_s^0)。

理想空间轴α^0_(y,y′)(u)=b^0_(y,y′)+u v^0_(y,y′)是通过(t,p_t^0)、(s,p_s^0)的真正affine line。由code定义、offset和s_min(A)≥σ0，实际两端points与理想点相差≤Cδσ0^-1。原管center axisα_T(u)=b_T+u v_T与实际selected endpoints相距Oδ，因此

    |v_T−v^0|+|b_T−b^0|≤Cδσ0^-2。                        (9)

这里t,s∈[-1,1]、|h|≥σ0，intercept的费用与slope同阶。只知道端点O(δσ0^-1)不能直接宣所有原u上的fine Oδ；(9)正是待修的全clock残差。取b足小，例如b<1/10，δσ0^-2→0，理想axes仍在固定稍大有界chart，但后面系数可以有δ^-2b增长。

## 8. 八维轴残差一次分桶，统一修复全部u

将每条T的真实joint axis残差

    R_T=(b_T−b^0_(y,y′),v_T−v^0_(y,y′))∈R8

按δ-grid分桶。由(9)至多Cσ0^-16桶。选一个桶，保M2≥cσ0^16 M1条原管，故

    M2≥cK^-2δ^{2a}σ0^20δ^-2≥L^-1δ^-2。                    (10)

桶center记(e0,e1)∈R4×R4。对每条余管和**所有**原bounded u∈[-1,1]同时有

    α_T(u)=α^0_(y,y′)(u)+e0+u e1+Oδ。                    (11)

这是对joint parameters一次分桶，不随u另选中心，不消耗#Z或管的访问质量。若要求最后的两侧min-degree，在此桶的原图内再以M2/[4(#P_j+#Q_j)]peel，保至少M2/2边，最终度≥L^-1δ^-1；code和residual条件均不变。每条留下T仍保全部S_T。

关键恢复重数也因此变好：固定精确(y,y′)，理想joint axis唯一，实际T参数在该轴加共同(e0,e1)的一个Oδ box内，故原dyadic tube labels至多固定数C0。若只用坐标已变换的AD上界形式，可保C0K固定幂，仍入L；绝无h^-4或δ^-Cb新损失。这一条是最终g≤1的实际依据，不是仅靠两端点可逆。

## 9. 全原时钟的精确系数与native输出误差

令λ_u=(u−t)/h，分别写e_j=(e_j^x,e_j^y)∈R2×R2。将(11)减F_u倍horizontal坐标，理想native输出为

    B_u+C_t(u)y+C_s(u)y′，
    C_t(u)=(1−λ_u)(F_u−F_s)A^-1，
    C_s(u)=λ_u(F_t−F_u)A^-1，                                (12)

其中共同baseline必须完整写为

    B_u=(1−λ_u)(F_t−F_u)A^-1 U
        −λ_u(F_s−F_u)A^-1 V
        +e0^y+u e1^y−F_u(e0^x+u e1^x)。                     (13)

最后一行是actual-axis残差对native坐标的贡献，不能只作一个constant y平移。F_u bounded，所以(11)的spatial Oδ经native变换后仍Oδ。每个u∈S_T有canonical原selected point p_u，其native label属于原Y_u，离α_T(u)为Oδ。因此(12)对每条保留原管的每个旧u同时落在N_(Cδ)Y_u。

没有给C_t/C_s uniform bounded范数：|λ_u|≤Cσ0^-1，||A^-1||≤σ0^-1，故系数／baseline可至Cσ0^-2。对g-positive输入输出实际有界不等于所有product输入的像有界。u=t,s时系数分别(I,0)、(0,I)，残差baseline在两端只Oδ，这与精确native labels一致；不能由端点值推中间coefficients满秩。

## 10. 真实有界g、完整product×Z密度和闭包

记最终管族H*。对精确(y,y′,u)∈Y_t×Y_s×Z，令n(y,y′,u)为H*中具有这两端labels且u∈S_T的原管数。取第8节的统一multiplicity上界M0，定义g=n/M0，则0≤g≤1。它保的是实际全tube访问权，未将edges改成独立pair或新Markov路径。由(10)、原n_T≥K^-C m和完整Y两边card upper，

    Σg=M0^-1Σ_(T∈H*) n_T≥L^-1δ^-2 m，
    E_(UniformY_t×UniformY_s×UniformZ)g≥L^-1。             (14)

每个g-positive三元组都有(12)–(13)的同一fine输出。各original tubes的全部旧S_T都在计数中；不要求任何T访问所有Z，也不将其时钟置换为uniform Z。由g≤1和mean lower可得其归一化law对完整product reference的L-domination，但不能反向得lower、独立性或每个conditional角prior的slab upper。原Y_t、Y_s及每个Y_u的AD／KT作为完整环境集合保留；active子集不继承ADlower，g-shading也不是新的Def17配置。

参数可一次闭合：显式计数给总δ损失至多固定倍(a+b)加Cη，例如(10)含2a+20b，最终degree可再多2b；取a,b≪β/C0，η最后小，即L≤δ^-β乘固定常数。全u误差仍固定Cδ而不是Lδ；L只计质量和条件数。平均density由(14)按总incidence成立，逐管visits由保全部S_T成立，这两个理由分别有效。

## 11. 增长接口反攻：Schubert、降秩与独立化均未自动付

固定t的共同Σ_t={(x,y,ξ_p)}⊂R6携带normalized3-Frostman upper，来源是Y¹与X二维packing、完整slice cardinal，非ξ光滑。不同s的左code是同一点集上的线性L_s。但kernel K_s={(-A_s^-1v,v,-h_s^-1v)}始终与固定W_l={l·y=l·ξ=0}这4-plane有非零交。primary的output4对应normal 4-plane K_s⊥，上述包含等价于K_s⊥与固定2-plane W_l⊥有非零交，不能混淆k。将输出左乘diag(A_s^-1,h_s^-1I)后，π_θ((x,ξ),y)=(x,ξ)+θ_sy，θ_s=(A_s^-1;h_s^-1I)∈Mat4×2，其两个off-diagonal坐标恒0。因此whole family落CSWZ model Schubert hyperplane；Def1.5全尺度spread-out字面失败（cell厚度与σ条件数只付L，不去掉exact结构零）。此点不是待用SM自动去掉的小坏事件，不能直接调用Th1.7。

native三时模型也不自动给nondegenerate C_t/C_s：它们分别含F_u−F_s、F_t−F_u，即使端点A可逆，某些中间u仍能降秩，甚至不同Y因子的互补rank1投影可使和像维数仍1。只有AD1 product和dense g不赠sumset增长；R18的独立convolution shortcut及冻结的BSG／action域问题继续有效。这里模型是实际原tube数据的新有限应用，不是证明全部κ1 det-large分支不存在。

本稿未构造完整source反例，未向环境加入smooth／rational、goodrank、Schubert spread-out、共同fine Φ、independent g或额外time访问公设。若反攻只在某个standalone rank1/Cantor模型成立，必须另注明它不保原SM／全T／CW，不能拿它否完整source。

## 12. 实际结论、互审入口与停止

本稿独立完成所锁source模型：真实sameT分支→原fixedpair／finite-offset图→平行边收费的双边peeling→稀有native code块→精确labels理想whole axis→八维joint残差一次分桶→全原u的fine Oδ输出和有界g。单块原管比例δ²已明付，完整product的L^-1密度没有冒原全局mass或active ADlower。

当前结论仅是原分支的完整finite product-clock提取，不是κgain、wholematrix排除、literal K5(1)或ordinary／Hausdorff新界。高级source原wholeproof未新独证；A正算的独立审查由root/B承担，不以自己推导充独审。后续已实际全文读取root终版12节与B终版10节：B的Schubert正常4plane／kernel2plane转换、buffered四进Cantor全orientation tube-KT½、同block wholeclock直线实现及其AD2／CW≥δ^-2／内部Φ与filledX失败边界逐式核通过。root主证明的原质量、fine残差、B符号和restricted energy亦读回通过；其中第7节optional再次peeling的初稿分母漏σ^-2，由A提出，root已改真实端点数分母并实际读回，无遗留必修。原He1611.09639v2 Th2–3及He–de Saxcé1806.06375v3 Th1.1/2.4/Prop2.5的本地statement接口另实际重读，确认不能从本g直接授共同X、quantitative irreducibility或quotient nonconcentration。正式意见见另获授权的R0076_source_precision_and_clock_review；不预认证未写归档或Git。

本轮停止线保持：模型成功后若增长端只能重用旧全称gain或需额外goodrank／independent completion，不以它新名开方向；如模型fine误差或全时钟失败则明确失败，不退成只有code恒等式。这里不另注册数学ID、重大性或新颖性，未经外部同行评审，Goal active。
