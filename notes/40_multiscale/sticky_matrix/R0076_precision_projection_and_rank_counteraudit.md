# R0076阶段II：fine轴残差、共同核奇异与互补rank-one反攻

2026-10-18，B。仅编辑本授权稿，恰十个编号二级节，无Git／元数据／下载／新代理。已实际全文读R76 working_spec阶段II新增第2节，依所锁完整bounded matrix33 κ1的det-large同管分支施工；不把所提取乘积模型称κ1排除，也不把下述校准冒完整source反例。高级wholeproof及外部同行评审边界分开。

## 1. 全部原变量、支撑与显式费用

保原全T、N≈_Kδ^-4、CW≤K、完整Y_t AD1、filled X2、point Φ_p AD1／slabγ、selected ξ及其coherence。K=δ^-Cη。原time数m=#Z，H为已heavy但**保每条原管全部旧visits**的族，S_T⊂Z且#S_T≥K^-C m。分支输入为

    Σ_(t,s: |h|≥δ^b, s_min A≥δ^b)
         #{T∈H:t,s∈S_T} ≥δ^a δ^-4m²，
    h=s−t，A=F_t−F_s。

这不是raw独立矩阵对假设。先给目标loss β，再取a,b足小，η最后小，δ最后；以下L=δ^-C(η+a+b)，C可增固定倍，不能把δ^-Cb藏在仅依η的K内。记σ=min(|h|,s_min A,1)≥cδ^b，原F和whole管slope有固定上界。

按(t,s)平均可选一实际pair，其原tube edges数E_0≥δ^aδ^-4。每T两端选原canonical visit p∈E_t、q∈E_s；固定T／time只有固定数δ邻格误差，损常数而非更换原law。左右vertices各≤Kδ^-3，native y_t／y_s是原数据标签，不先替为code中心。

## 2. 实际双端code与固定pair的管重数

写p=(x,y+F_t x,t)、q=(x′,y′+F_s x′,s)。同一原T给

    x′=x+hφ+Oδ，
    y′=y+hξ_p+A x′+Oδ，
    ξ_q=ξ_p+Aφ+Oδ。

故

    C_L(p)=(U,V)=(y+Ax,y+hξ_p)，
    C_R(q)=(y′−hξ_q,y′−Ax′)，
    C_L(p)=C_R(q)+Oδ。                            (1)

式(1)实际用两端selected ξ，并保native baseline，不是R18单终点厚桶，也不是从任意related graph声同管。

固定(p,q)，原轴slope在半径Cδ/|h|的R4球内；其δ-slope格数≤C|h|^-4。固定slope后intercept在Cδ盒内，仅固定数原δ-tube格。因此实际multigraph的pair重数

    M_pair≤C|h|^-4≤L。                            (2)

不能把两点决定exact直线就写重数1；δ误差和短clock已在(2)支付。

## 3. 有限offset、双边peeling与真实block数

将C_L／C_R按同一R4 δ-grid取半开cells。(1)只给固定数可能的整数offset；先选一个offset保固定比例原edges，再固定其两侧cell匹配。一个left code格只连唯一right格，反之亦然，形成不混同的code blocks。此操作不是把Oδ近似相等视作精确连通。

在该原多重图上反复删除degree<d的vertices及其incident edges，取d为E_0／[8(#E_t+#E_s)]的适当固定倍。总删除≤d(#E_t+#E_s)，故保E≥cE_0、两侧min-degree≥d≥L^-1δ^-1。没有删余管的第三时钟visits，也没有授active point新的ADlower／filled X。

固定left code格(U,V)，每个原native y∈Y_t的x落A^-1(U−y+Oδ)；其δ-packing≤Cσ^-2。故left block point数≤Kσ^-2δ^-1，right由V=y′−Ax′同得≤Kσ^-2δ^-1。另一方面，任一active block中的一个right vertex有d条边、每left-right pair至多M_pair，故该block至少d/M_pair个left vertices；右侧同理。不同blocks的point sets不交，所以

    #active blocks≤(#E_t)M_pair/d≤Lδ^-2，
    E_block≥d²/M_pair≥L^-1δ^-2。                  (3)

同样以两端point fibre upper和(2)得E_block≤Lδ^-2。故可选自然大小的真实block，原tube数≈_Lδ^-2；其占原全部T的比例约δ²L^±1，**不是K^-C**。只用Σedge多而不付pair重数，不能得到(3)。

## 4. Exact native标签理想轴与八维joint residual

在选中block取共同code中心(U_0,V_0)。对一条所留原T，保其exact原native标签(y,y′)，定义理想端点

    x_0=A^-1(U_0−y)， x_1=A^-1(y′−V_0)，
    z_0=y+F_t x_0， z_1=y′+F_s x_1。

以原clock参数u插值，λ_u=(u−t)/h，得理想轴ℓ^0_(y,y′)(u)=((1−λ_u)x_0+λ_u x_1,(1−λ_u)z_0+λ_u z_1,u)。实际原轴在t,s距这些理想端点≤Cδσ^-1；再除|h|恢复slope，因此在固定whole clock上的spatial截距／slope差均≤Cδσ^-2。

这正说明coarse code本身只给O(δσ^-2)，不能声fine Oδ。将这八个真实轴参数差按δ-grid**联合**分桶，至多Cσ^-16种。保一个bucket便仍有

    #T_block,res≥L^-1δ^-2。                       (4)

固定该bucket的共同spatial affine residual R(u)=r_0+u r_1∈R4后，对每条余原T及其所有原u∈S_T，同有

    ℓ_T(u)=ℓ^0_(y,y′)(u)+(R(u),0)+Oδ。            (5)

不是对每个u另选偏移，更不是以ρ-coarse近似作fineδ。若需重新双边peel，可在该bucket的两端有限点集上按剩余E和同样upper再做；只删whole tubes，余管全部S_T不删，费用仍L固定幂。

## 5. 全原第三时钟、有界g与真实native输出

固定exact(y,y′)后理想轴唯一；同residual bucket的原轴参数均落一个Cδ jointbox。原dyadicδ-tubes的parameter separation给至多C条实际T；这里可用常数而非未付的无限label fibre。对每一(y,y′,u)，数这些T中真正有u∈S_T的原visits，并除以上述固定重数C，得到0≤g≤1。它定义在**完整原**Y_t×Y_s×Z上，其余处零，不把active Y子集授新ADlower。

由(4)及每条余管原#S_T≥K^-Cm，

    Σ_(y,y′,u)g≥L^-1δ^-2m，
    mean_(Uniform Y_t×Uniform Y_s×Uniform Z)g≥L^-1。 (6)

任意原管权／label若在前面存在，须先按其实际fine tube计数付domination，不能从(6)另授任意先验；本轮对象是已锁原无权计数源。这里所保是average product-clock density，未声每个(y,y′)逐clock nearfull，更未取不同管clock的大交集。

由(5)，实际native输出满足

    y_u=B_u+C_t(u)y+C_s(u)y′+Oδ ∈N_(Cδ)Y_u，
    C_t(u)=(1−λ_u)(F_u−F_s)A^-1，
    C_s(u)=λ_u(F_t−F_u)A^-1，                     (7)

其中

    B_u=(1−λ_u)(F_t−F_u)A^-1U_0
          −λ_u(F_s−F_u)A^-1V_0+R_y(u)−F_uR_x(u)。

原F_u bounded使residual最后只加Oδ。两个矩阵及translation只保证明确的σ^-C上界，特别||C_t||+||C_s||≤Cσ^-2；不能假uniform bounded、更不能预假rank2。式(6)(7)已达到锁题的全时钟fine模型，而不是只给code恒等式或两个终时的边缘。

## 6. 共同point-law与固定Schubert divisor的完整证明

固定root t，原Σ_t={(x,y,ξ_p)}⊂R6的均匀point-law有normalized3-Frostman upper：一个r-ball只给≤K(r/δ)^3个(x,y)点，原#E_t≥K^-1δ^-3；ξ不增加这个upper。它不授Σ_t光滑／ADlower，也不授所有s使用同一active subset。

对h≠0、A可逆，线性code L_s(x,y,ξ)=(y+Ax,y+hξ)的kernel是

    K_s={(-A^-1v,v,-h^-1v):v∈R2}。                (8)

取任意固定nonzero row l∈(R2)^*，定义fixed 4-plane

    W_l={(x,y,ξ):l·y=0，l·ξ=0}⊂R6。

两个条件独立，故dim W_l=4。取v∈ker l\{0}，(8)给nonzero K_s向量且其y=v、ξ=−h^-1v均被l消掉，因此K_s∩W_l≠{0}，对**全部**s、全部F成立。该W_l不随s／δ／selected graph变。于是V_s=K_s^⊥的4-plane满足V_s∩W_l^⊥≠{0}；这是Grassmannian投影族中的固定Schubert divisor。共同bounded ambient chart变换只把W_l一起变换，不会消掉包含关系。

还可在实际big cell上看精确model hyperplane。重排坐标为(z,v)=((x,ξ),y)∈R4×R2，把code作可逆output变换得到

    π_(Θ_s)(z,v)=z+Θ_s v，
    Θ_s=(A^-1 ; h^-1 I_2)∈R^(4×2)。

所以Θ_(3,2)=Θ_(4,1)=0。每个等式都形如e_i^T Θ e_j=0的rank-one model hyperplane。F的SM、det-large或time AD不可能移除这些结构零。condition number只影响把该图放进bounded坐标盒的费用，不影响精确包含。

## 7. CSWZ primary的精确接口与不适用范围

本轮实际读已有CSWZ arXiv2610.13682v1本地提取的引言、Def1.4／1.5、Th1.6／1.7及big-cell定义；没有新下载或重证wholeproof。Def1.5的β-singular scale要求局部族被某model hyperplane的βr邻域包含；(δ,β,C)-spread-out要求若一子族每点有s个此类scales，其比例≤C2^-βs。Th1.7还明确要求该spread-out输入，才对共同point集合的所有大子集给投影lower。

由第6节，精确Θ_s在同一model hyperplane内；取其δ-cube family，局部union至多距该hyperplane Cδ。因此在所有r≥Cδ/β的dyadic scales都β-singular，数量为log_2(1/δ)−O_β(1)。对J′=J，spread-out会迫C≥c_βδ^-β；不能以足小loss δ^-ε、ε<β来满足该条件。对子族或在有界condition下重选坐标，这个包含仍在，不是概率坏小集。

故原time AD、det-large或SM均不足直接调用Th1.7；Th1.6的逐point plane configuration也要逐point spread-out，不能把它当另一免费入口。这里证明的是**所用投影primary缺假设**，不是证明这些原code不可能增长，也不是构造完整source counter。若另作point-adapted Schubert factor／多root联合law，必须新付其原质量及定理输入；本轮不加这个公设。

## 8. 全U的互补rank-one Cantor模型

令Δ=4^-n、c_0=1/16，取

    C_n=c_0{Σ_(j=1)^n d_j4^-j:d_j∈{0,3}}，
    δ=c_0Δ/16。

则#C_n=2^n≈δ^-1/2，最小gap≥3c_0Δ，C_n在[δ,1]各尺度是uniform AD1/2，且所有常数独立n。置t=0、s=1、F_t=I_2、F_s=0、U=[1/4,3/4]，对所有u∈U取F_u=P=diag(1,0)。这个matrix函数可在其余times作fixed-Lipschitz插值，但U上精确constant，不能当满足原SM的全source。

取完整native inputs Y_t=Y_s=C_n×C_n，输出Y_u=(1−u)C_n×uC_n，g(y,y′,u)=1及B_u=0。由于A=I、h=1，(7)成为

    C_t(u)=(1−u)P， C_s(u)=u(I_2−P)，
    C_t(u)(a,b)+C_s(u)(c,d)=((1−u)a,ud)∈Y_u。     (9)

两矩阵对整个U都rank1，互补images；两端输入和每个输出card都≈δ^-1，time可取整个Lebesgue U或任意uniform δ-grid。所有δ-separation由上述buffer保证，特别scaled output最小gap≥12δ；没有借近重合点虚增card。

Y_t／Y_s／Y_u均uniform AD1；对任何width w、length R、δ≤w≤R≤1的tube，选long direction投影较长的一坐标。该坐标的C_n在length CR区间只有C(R/w)^1/2个w格；每个格内tube使另一坐标落O(w)区间，仅固定数w格。因此

    N_w(Y_u∩tube)≤C(R/w)^1/2，                   (10)

输入同样。u∈U的两坐标缩放有uniform condition number，所以常数统一。这正给native tube-KT(1/2)，不是只核横／竖tube。还可逐一条件一个坐标得slab exponent1/2。模型在全U有g=1、完整平均／逐对clock密度、两个AD1 inputs及AD1 tube-KT output，却没有自动rank2或二维growth。

## 9. 真实单block直线实现、未保源条件与能量误读

(9)甚至可用同一批真实whole-clock直线实现：对y=(a,b)、y′=(c,d)，取初端physical p=(-y,0,0)、终端q=(y′,y′,1)，中间轴为

    x(u)=−(1−u)y+uy′， z(u)=uy′。

其u-native normal z(u)−P x(u)=((1−u)a,ud)，对所有u∈U与(9)相同。初ξ=−y、终ξ=y′，code U_0=V_0=0；因此不是每个u另造一根线。固定homothety／whole-clock常数可使全部坐标和physical slopes在原bounded盒内。

这仍远非完整source：该joint tube family是四个AD1/2坐标的fixed injective linear image，故只有≈δ^-2条δ-separated管、AD维2，非所需AD4。测试一个single δ-tube的凸外罩，概率约δ²而体积约δ⁴，normalized CW至少cδ^-2，不是任意小loss。对u∈U，physical point恢复y′=z/u、y=(z−x)/(1−u)，所以内部point只有一根／固定数管；pointΦ AD1也不成立。固定native output后horizontal自由度只有两份Cantor共维1，非filled X2。F在U精确constant，亦不保原SM。没有用padding修造这些缺失，不是Kakeya或fullsource反例。

自然乘积energy的误用也可精确定位：令N≈δ^-1为两native inputs的card，输出card≈N，未投影标签的collision数确可达N³；但C_t Y_t只有≈N^1/2点、C_s Y_s亦≈N^1/2，且分处互补坐标轴，其sum map对两个有效inputs是一一的。native的大fibres来自rank1核中丢掉的另外两个Cantor坐标，并非得到一个有small-doubling的共同N点集。He类不可约作用条件在共同diagonal algebra下失败；BSG不自动恢复被kernel抹掉的原labels／clock，亦不给所有u同一共同A。故不能仅从“AD1×AD1到AD1”直接宣所需独立卷积或action增长。

## 10. 当前实际结论、互审接口与停止

独立核得所锁原det-large分支可以实付：实际pair选择、有限code offset、pair multiplicity、双边peeling／自然δ²全管比例、exact native理想轴、八维joint residual、全bounded原clock的fine Oδ输出及0≤g≤1的真实product-clock密度。L的所有condition和原质量成本明确为δ^-C(η+a+b)，a,b,η按目标loss后小。平均density与逐pair clock、原point-law与条件子图没有混同。

进一步已完整反攻两种自动出口：直接CSWZ调用受固定Schubert model hyperplane阻挡；自动full-rank／仅native product维数就增长受第8–9节全U互补rank1模型反驳。后者只覆盖所列弱接口，完整source中的SM、filledX、pointΦ和whole AD4/CW可能另给信息，本稿没有否其全部量词。没有证明κ1排除或ordinary增益。

已actual全文独读root整合12节和A阶段II12节：A的fixedpair平行管h^-4、offset先选再peel、M1／M2实际原管质量、exact native理想轴、σ^-16 joint residual、同(y,y′)有界恢复及全旧S_T构造g均逐式通过；root的B_u负号、σ^-2系数、原δ²全族比例和restricted energy范围也与本稿独算一致，当前未见未解决必修。A的source正证在此由B独核，B的自推及校准仍须A／root独核，不以自己再读作独审。正式review另授权。

目前不再扩Cantor参数／更多times或加好rank、Schubert factor、独立化公设以收轮。具名高级wholeproof未本轮全复证，未经外部同行评审，无newID／major／Goal完成或后续元数据／Git预认证。
