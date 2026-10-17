# R0045：实际四臂Kakeya–BL接口、有限横截桥与剩余rank质量

2026-10-17，root。周期macro先执行，本稿针对R44指定的一次四臂gate。原四臂分离/near-plane overlap与Kakeya–BL接口确可支付；不能把“需要笛卡尔子族”或“plane没有filled shading”误列为绝对障碍。下面证明一个带明确matrix-rank条件的有限横截桥，但没有从完整source获得所需good-BL质量。即使理想化该质量，当前单endpoint字母表账本也只到κ≤5/4加损失，不能闭κ≤ζ。一般/五维Kakeya未解决，外部同行评审false，不宣重大/新颖。

## 1. 原量词与文献输入

固定ζ,γ>0，η足够小、δ随后小，完整WZ d5,k=ell3 Def17.2–17.4（需要CW则明列原C_CW≤δ^-η），有界jointchart的原uniform whole-T law ν、N_T≈_Kδ^-4。κ≥ζ、b=2−κ≥0，K=δ^-Cη只吸固定幂。源原used witnesses按R16每p/Φδ-bin保一根，sameT,time重数O1；不用任意q lower。原|E|≈_Kδ^{-(5−κ)}，deg(p)≈_Kδ^-κ，I≈_Kδ^-5。

新primary为P. Zorin-Kranich arXiv:1807.09604v4，2019-09-11，Collect. Math.71(2020)。本地PDF18页、638678bytes、SHA256 e9046375f7019aab9f7b88123d870fbf3d71f9b264b338394d7d67e6a77fd831，root实看PDF3–5。准确调用其Theorem1.5及Def1.4，whole external proof作为具名输入；本项目独立推导下面的选中tuple推论。不是声称已独证其全部polynomial方法。

Th1.3需要四个family全部混合tuples的统一regularized BL界；Th1.5不需。v4 PDF5从1.5推1.3的单行把该lower写为A倍，按定义应为A^-1倍；下面直接从1.5/定义推，不依该倒数排字。不据这一行宣主定理错误。

## 2. 原heavy到四臂：时间/角分离是可付步骤

记D_T为T的全部原used marks数，D_T≤Cδ^-1。以I/(2N_T)为阈值删light tubes，保至少I/2；heavy各D_T≥K^-Cδ^-1。再删heavy-degree小于I/(4|E|)的base points，其heavy incidences总至多I/4。因此有P⊂E，

    |P|≥K^-Cδ^{-(5−κ)},
    d_p^H≥K^-Cδ^-κ， D_T≥K^-Cδ^-1 (T∈H)。          (1)

端点仍从这些T的**原全部marks**取，不在删base后再删端点。对固定p，每臂为原pairs(T,p′)，T∈T_p∩H、p′为其原mark。每臂数≈_Kδ^-(κ+1)。条件于p形成四个这样的原臂的product只是定义真实四臂集合，不把φ和time各自独立化。

原row Φ_p的slabγ cap，限制heavy并按D_T加权后只损K^C；任意T的端点time-law有cap K^C(r+δ)，来自sameT,z O1及D_T lower。故取r=δ^α、η≪αγ，union bound可删角近重/重复T、四端点time互距<r或距base time<r者，只损o(1)原star质量。即使原φ和endpoint time相关，此结论仍由条件upper成立；不预设每管原来逐管dense。

## 3. 同源normal maps及真实physical overlap

原base p在time z0，F0=f(z0)、ξ0=ξ_p；臂i端点p_i在time z_i，F_i=f(z_i)、ξ_i=ξ_(p_i)。取实际axis方向v_i=(φ_i,θ_i^y,1)，φ_i为实际前两slope（距原Φ_p Oδ）。源见证在两端给

    θ_i^y=ξ0+F0φ_i+Oδ=ξ_i+F_iφ_i+Oδ,
    ξ_i=ξ0+(F0−F_i)φ_i+Oδ。                       (2)

B_i=(-F_i,I2,−ξ_i)，G_i=ker B_i维3，singular values在固定绝对上下界内。原affine plane Π_i={X:B_i X=B_i p_i}，因p,p_i与同一原T_i相距Oδ且wholeclock有界，

    |B_i(p−p_i)|≤Cδ，dist(p,Π_i)≤Cδ。              (3)

故可直接使用这些无限affine3-planes的δ邻域。无需宣Π_i真实filled shading。若用Th1.5的“plane intersects cube”形式，给每个带原endpoint标签的Π_i添加固定有限个ambient δ-grid translations：在距离Q_p固定邻接的cube中挑实际相交cube再平移到Q_p。family只多固定倍，directions/BL不变，原label不合并。一个endpoint tuple可选出相交同一Q_p的translated tuple，纤维界保持；过覆盖合法，但不变成原source filled plank结论。

## 4. Theorem1.5给选中tuples而非仅笛卡尔族

四个带multiplicity的plane families大小N_i，p_i=5/8、P=5/2，Fremlin各指数P/p_i=4。由定义，任意F≥0有Fremlin norm≥l4(F)：若F≤F1⊗…⊗F4，对F^4求和即得。Th1.5在δ-rescaled bounded domain中因此给

    Σ_Q (Σ_(tuple at Q) BL_reg(tuple)^(-8/5))^(5/8)
       ≤C∏_(i=1)^4 N_i^(5/8)。                    (4)

这里BL_reg是方向quotient的(1,R)常数，R≈δ^-1（局部ρ域则R≈ρ/δ），不是漏去normal δ厚度的scale-invariant替代。若选中Γ_Q上full BL≤A，则BL_reg≤A，由(4)

    Σ_Q |Γ_Q|^(5/8)≤C A∏N_i^(5/8)。              (5)

物理δ5乘在两边后相消。任意选中hypergraph可用，不必另提笛卡尔子族，也不必对未选中的全部tuple有A界。重复plane仍按原labels计N_i；不能只数几何不同planes而抹掉原mass。

## 5. 满秩pair类中的精确BL判据

以下是本项目独立有限线性代数/积分论证，不依原source是否存在。假设四张bounded B_i=(-F_i,I,−ξ_i)，所有A_ij=F_i−F_j (i≠j)可逆。Gi中用(x,t)坐标，Gi∩Gj是一条线，方向

    l_ij=(a_ij,1)，a_ij=A_ij^-1(ξ_j−ξ_i)。
    D_i=det[l_ij]_(j≠i)。                         (6)

若D_i=0，三条pair-kernel线张成W⊂Gi维≤2。维2时B_iW=0而其余三个image维≤1，BL dimension inequality右边≤15/8<2；维1时三线相同，W被四张B全部杀掉。故BL无限。

反之若各D_i≠0，先在B_i X=s的fiber积分：变元(X)→(x,s,t)的det=1，B_j X=A_ij(x−a_ij t)+s。令M_i三列为l_ij，u=(x,t)=M_i w。第j张map杀掉w_j，其剩余2×2 determinant的绝对值为|det A_ij|·|D_i|。三维Loomis–Whitney（两次Cauchy–Schwarz即可）给

    ∫ g_i(B_iX)∏_(j≠i)g_j(B_jX)^(1/2)dX
      ≤ C_i ||g_i||1 ∏_(j≠i)||g_j||1^(1/2),
    C_i=|D_i|^(-1/2)∏_(j≠i)|det A_ij|^(-1/2)。     (7)

对四个(7)以Hölder均分，权重每张变为(1+3/2)/4=5/8。因此

    BL_B≤∏C_i^(1/4)。                              (8)

B_i的coarea Jacobian均在固定上下界，map版本与orthogonal quotient版本只差固定因子。故在pair-difference可逆类，所有D_i非零是有限BL的必要充分判据，已经包含全部subspace条件，不能仅凭stacked rank5代替。

## 6. 条件于rank分离的slab角横截桥

另给F0，假设五张bounded矩阵的所有不同pair满足

    |det(F_i−F_j)|≥σ，0≤i<j≤4。                   (9)

理想同源ξ_i=ξ0+(F0−F_i)φ_i，φ_i独立取同一个原row Φ（仅本有限product参考law），Φ为baseδ、slabγ常数K的probability。固定φ_i后，j≠i的a_ij是φ_j的affine image，其linear coefficient

    C_ij=(F_i−F_j)^-1(F0−F_j)

满足s_min≥cσ、norm≤Cσ^-1。三个independent affine images的三角面积小于τ，只可能前两点相距≤√τ，或第三点到其连线≤√τ。因此

    Prob(|D_i|≤τ)≤C K max(δ,C√τ/σ)^γ，
    Prob(min_i|D_i|≤τ)≤C K max(δ,C√τ/σ)^γ。        (10)

每一步只用一次条件slab cap，不需把K平方；查询小于baseδ时必须clip。若actual ξ_i与理想值差Oδ，则a扰动≤Cδσ^-1、|a|≤Cσ^-1，故D扰动≤Cδσ^-2。取τ≥Cδσ^-2，在理想|D_i|≥2τ处实际D_i≥τ，并由(8)/(9)

    BL≤C τ^-1/2 σ^-3/2。                           (11)

例如σ=δ^a、τ=δ^β，2a<β<1−2a且η≪γ(β/2−a)可付bad角质量与小power BL损失；这只证明参数相容，不给(9)的source time质量。

actual angle-time law并非独立。若某真实joint law被product参考law以G支配，bad upper须再乘G；本轮原per-T/time upper和heavy lower只给G≤K^C，不能改成1。对固定rank-good times先用(10)，再积分/支配可以合法处理相关性；但必须先证明真实raw star中rank-good time tuples有足够质量。条件(9)是本有限桥的充分条件，不是所有BL-good数据的必要条件。

## 7. 可证的校准与不可偷补的rank质量

B稿给真实有限star说明(2)不强制BL退化：取c_i=i/8，z_i=ρc_i，φ_i=(c_i,c_i²)，f(t)=tI、ξ0=0、ξ_i=−ρc_iφ_i，真实T_i(t)=(tφ_i,0,t)。pair-kernel l_ij在Gi坐标为(c_i+c_j,c_i²+c_ic_j+c_j²,1)，三个不同c_j的Vandermonde使各D_i非零。(7)给BL≤Cρ^-3，下节给匹配lower。该有限star不保完整AD/CW/Y/positiveκ source；尤其f affine旧20.2已覆盖相应完整配置，不能宣新高维分支。

另一方面，矩阵曲线F(t)=F0+v(t)r（固定row r、v向量非affine）具有公共horizontal kernel。任何按(2)形成的Gi都含(u,F0u,0)，u∈ker r；故BL无限。这个代数例仅说明“f非affine、times/φ分离与同源因子”不自动蕴含rank/BL分离；未构造完整正κ source，也没有声称它满足旧全尺度SM。排除完整source的此类或更一般rank集中需要额外实际论证，不能从(10)倒推。

本轮没有证明(9)在原四臂中有δ^Cη质量，也没有其它覆盖rank-singular但BL-good数据的actual质量定理。原slabγ约束角、time density约束times，本身不约束矩阵差的det；原其余Y/TubeKT及多尺度结构是否能提供它仍是新责任，不能设为公理。

## 8. 局部固有BL费用及frame

同一个source允许ρ-world中，F_i−F*、ξ_i−ξ_q=Oρ，所以B_i在共同3D G0上范数Oρ。单位quotient-ball输入（或固定阶梯cube外包）的joint inverse images含G0方向长min(R,c/ρ)、normal2维固定宽的cylinder，给

    BL_reg(1,R)≥c min(R,ρ^-1)^3。                  (12)

scale-invariant也≥cρ^-3。局部R≈ρ/δ且δ≪ρ²时下界ρ^-3真可见。不能在同world免费宣O1横截常数；ρ=δ^µ时3µ虽可小，也必须计。

在adapted tangent3/normal2坐标取L缩tangentρ、normalρ²，detL=ρ7，输出normal统一除ρ²；BL变元给BL′=ρ3 BL（原输出coarea固定因子仍需保持）。这恰可消(12)的归一化退化，却同时改变physical Jacobian、tube宽及overlap，不能把三个费用都删去。上节有限star说明ρ^-3阶可达，不是仅粗下界。

若把§6充分桥也放进ρ=δ^µ的同time-world，source还给|det(F_i−F_j)|≤Cρ²。因此σ=δ^a需a≥2µ−o(1)，β与a_BL=(3a+β)/2不能独立于µ选得无限小；须与(12)同账。本稿§6先作global有限陈述，没有以该局部选参免费越过ρ^-3。

## 9. 原endpoint字母表的完整条件账本

给每个实际endpoint p_i一个plane label，四family各N_i≤Kδ^{-(5−κ)}（固定translations不改幂）。在timegap≥r时，固定base p及endpoint p_i后，实际T方向在半径Cδ/r ball内；原Φ_p的AD upper及bounded witness multiplicity给至多K r^-κ根T。故一个四endpoint tuple的raw-star fiber≤K^C r^-4κ。

假设另已证明goodraw质量≥g的tuples有full BL≤A，g≥K^-C；这是假设输入，前几节没有把它补齐。按base density再筛（不能反用concavity Jensen），保至少gK^-C|E|个base，并在每base保至少gK^-Cδ^-4(κ+1) good raw tuples。因而

    |Γ_Qp|≥gK^-C r^4κ δ^-4(κ+1)。

代(5)，给

    δ^(5−4κ)≤K^C A g^(-13/8) r^(-(5/2)κ)。         (13)

若A≤δ^-a_BL、r=δ^α，得到

    (4−5α/2)κ≤5+a_BL+O(η)。                        (14)

即使理想化所有损失趋0，当前certificate只给κ≤5/4。普通五维Kakeya由四维投影有dim≥4，不可自动套到任意无方向net的jointAD/CW类；本稿也不认证(14)是该加强类的新最优界，因为关键goodraw输入未证。不能把这个条件3.75读成无条件高维改进。

更换任何固定m臂、rank2/equalweight5/(2m)也不改善这一字母表阈值：raw perbase幂m(κ+1)，Fremlin给P/m=5/(2m)次幂相消为(5/2)(κ+1)，RHS总plane幂P=5/2不变。此仅排这份计数certificate的固定臂数微调，不排所有多线性/混合范数方法。

## 10. 本轮停止及范围

实际heavy四臂、不同angle/time、physical near-plane、selected-tuple KBL及因子rank条件下的BL桥均明确了；没有以未填plank或非Cartesian为假阻塞。真正余责是actual good-BL/rank质量；当前endpoint计数即使理想也不能闭小κ。按一轮gate停止此四臂主线，不连续加臂/调阈值/重开旧CP⇔PM或W/BSG行动循环。

不登记新的Kakeya结果ID，不宣新颖/重大；未证κ≤ζ、完整(3,3)、任何一般高维满维数或反例。新primary和独立全文reviews归档，宏观下一步需据不同真实输入决定，Goal active。
