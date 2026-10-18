# R0097：原scalar观测的局部Segre门与有限投影适用边界

2026-10-19。研究方向：一般维度Kakeya → 原WZ bounded mixed42 → 实际rough native scalar。施工规格research/rounds/R0097_working_spec.md。本文是精确适用性证书及条件转移，未经外部同行评审；不是完整mixed42排除、维数增益或重大结果。

## 1. 原目标、来源及量词

保原Def17.2/17.4全部输入：d=5、k=4、ell=2；固定0<κ<1、γ>0，η最后小、δ最后小。原T及N、whole convex-Wolff、joint4AD、两grain表示、Z、ξ/Φ与coherence均保留。K=δ^-Cη统记原有限次损失。任意β_t=tilde f(t)∈R³满足原bounded数据；本局部证书甚至不要求其连续、单调或dyadic Lip。没有增添polynomial/jet/globalcap/parameter spreadout公设。

CSWZ2610.13682v1（2026-10-09）Def1.4–1.5/Th1.2/1.6/1.7实际重读；freshabs仍v1，原PDF6图实际查看。以下引用其finite定理为具名输入，未独立审其完整高级证明。R96已证任意≥5原观测的exactspan上原point law至少1Fst，此处不改写为每单观测law。

## 2. 原scalar映射和模型超平面

原line参数λ=(a_H,a4,b_H,b4)∈R⁸，F_t(λ)=a4−β_t·a_H−tβ_t·b_H+t b4。令x=a4、y=(a_H,b_H,b4)∈R⁷，θ(t)=(-β_t,-tβ_t,t)，则F_t=x+θ(t)·y。固定bounded chart的归一化/δcell舍入只改维数常数及δ倍精度。

在CSWZ Th1.7取d=8、k=7，输出d−k=1；其spreadout下标为(8,1)，bigcell=R^{1×7}。Def1.4 modelH={xθy=u}中x为非零scalar、y任意非零R⁷向量，所以模型族恰是全部普通affine hyperplanes。不能把一般Grassmannian rank-one模型限制误搬来削弱此scalar情形。

## 3. 二次流形与精确切H恒等式

写z=(u,v,w)∈R³×R³×R。全部原θ均在Σ={v_i=w u_i,i=1,2,3}。Σ是光滑四维图形，与β粗糙程度无关。对z0=(u0,w0u0,w0)∈Σ定义

L_i(z;z0)=v_i−w0 u_i−u0_i w+w0u0_i，H_i(z0)={L_i=0}。

法向g_i=(-w0 e_i,e_i,-u0_i)非零且||g_i||≥1。在Σ上直接展开得到L_i(z;z0)=(w−w0)(u_i−u0_i)。因此若|z−z0|≤r，则dist(z,H_i)≤r²。这里H随z0移动，并非存在一个固定全局H；global affine span可以是整个R⁷。

## 4. δ厚化、所有删选和全部局部尺度

设J非空、有限，所有δcells均实际交Σ的同一bounded图块。任取非空J′⊂J、θ∈∪J′，取θ所在cube内z0∈Σ，则|θ−z0|≤√7δ。任取ω∈(∪J′)∩B(θ,r)，其cube内另取z∈Σ。于是|z−z0|≤r+2√7δ，且|ω−z|≤√7δ。bounded图块令||g_i||≤C，精确恒等式给

dist(ω,H_i(z0))≤C(r²+δ)，δ≤r≤1。

固定b∈(0,1]，选择维数/chart常数c足小、C0足大，使Cδ/b≤r≤cb时C(r²+δ)<br。所有此区间dyadic尺度均Def1.5的b-singular，对每个J′、每个θ同时成立。dyadic尺度个数s≥log₂δ⁻¹−2log₂b⁻¹−C1。若区间空则不作渐近结论；固定b且δ充分小时非空。

## 5. spreadout常数下界与不可越过的ε边界

若J满足(δ,b,Cspread)_{8,1}，Def1.5可取J′=J，得到1≤Cspread·2^-bs。故Cspread≥c_b δ^-b。对每个非空子家族本身也成立，完全不依赖保留比例。因此固定b及ε<b时，Cspread=δ^-ε在δ充分小时不可能。

此不等式不排ε≥b；尤其不能由定理容许把存在ε取小，就推出所有更大ε输入均不可能。此处冻结的是直接原ambient scalar参数在固定b、ε<b下的small-loss调用。没有否定CSWZ结论，没有宣布所有其数值参数或所有restricted projection方法失效。

## 6. finite结论的强度确实足够

Th1.7：对spreadout Θ及(δ,tpoint,δ^-ε)-Frostman原point集合P，保留至少1−δ^ε参数后，对每个保留θ及每个|P′|≥δ^ε|P|的subset，Nδ πθ(P′)≥δ^{ζ−tpoint}。此处0<tpoint≤1；它是nearfull标量输出，不是点维数除8或仅half-plus。Th1.6允许point-dependent shadings，给Nδ F(P,Θ)≥δ^{ζ−tpoint}M；其kernel7 affine-plane配置同属scalar模型。

为原source留裕量可取tpoint=1−κ/4、0<ζ<κ/4。则ζ−tpoint<−1+κ/2，而原每time标签upper为K^Cδ^{-1+κ}。若实际参数输入和质量都付齐，η足小就有严格κ指数矛盾。强度不是当前门的不足；不能把文献的附加parameter hypothesis默认为原定理的一部分。

## 7. 实际原质量转移

原joint4AD与N≈K^{±1}δ^-4给原λ的uniformδcell点集至少(δ,tpoint,K^C)-Frostman，事实上ball upper为K^C r⁴。原管到同一δ参数cell的重数可由joint4AD付K^C，故|P|≥K^-C N；不冒逐cell绝对常数。η足小使K^C≤δ^-ε。

原每t第一套globalgrain给|E_t|≥K^-Cδ^{-4+κ}，每p原Φκ给≥K^-Cδ^-κ个分离角。选择每(p,φ)原witness tube，一根tube在固定t只遇O(1)位置格，且固定p/tube的graph slope只容O(1)分离φ，故visited原T_t≥K^-Cδ^-4≥K^-C N，不只总平均。round后的P_t仍≥K^-C|P|，其所有scalar图像都由各自原witness付Oδ标签误差；未假同一参数cell在各t由同一原管访问。A稿逐项核原Def17与常数，不假删后ADlower。

θ的最后坐标t使δ-separated原times到parametercells只有O(1)碰撞，故原time数量与cell数量可比。重碰撞时一个cell选一个原time，其自身visited质量仍K^-C N；这已足Th1.7。访问T_t对应P_t⊂P，|P_t|≥K^-C|P|≥δ^ε|P|，其scalar图像位于原Ytilde_t的Oδ邻域，cover upper≤K^Cδ^{-1+κ}。若Θ满足所需spreadout且非空，定理保留至少一cell，robust输出便与该upper矛盾。所有η在κ、ζ、b和定理ε之后小。没有重新归一化conditional point law，也没有给独立times或marks。

## 8. 平均、逐管shading和原商不能修本门

原总incidence到heavy tubes的选择，及每time原lower到visited tubes的计数，是两种不同质量语句；Th1.7的实际用途由第7节逐time语句支付。若改Th1.6逐point/shaded参数，均匀M需要原heavy计数和dyadic pigeonhole另付；然而每个非空shading仍是交Σ的cells，由第4–5节本身不能有ε<b的small-loss spreadout。

因此任意合法parameter restriction，包括按point、marks或density筛选，都不能消掉这个几何输入障碍。此断言无需假其保留原质量，更不声称这些restriction后的原ADlower自动闭包。R96 exactspan point商1Fst只约束point变量；它不会把Σ上的parameter family变成spreadout。由此再提出‘adapted’投影命题，必须实际证明其额外相对假设与正确输出，不能只换名称登记。

## 9. 固定有界坐标变换的范围

固定invertible ambient R⁸线性变换在法向projective空间诱导光滑diffeomorphism。限制在分母远离0、变换及逆的前两阶导数有固定界的chart，Σ映成光滑codimension3子流形；local Taylor展开到任一切超平面给C r²误差，δ厚化仍Cδ。scalar模型是所有affine H，故第4–5节结论保留，只改c_b等固定常数。

此论不覆盖非可逆有效quotient，因为维数及模型族可能变；亦不准把δ-dependent illconditioned变换的导数/厚化/质量费用当常数。后者若用，必须重开全部费用而不能宣称本证书已排。

## 10. global power cap、fullspan及fulljet仍不能替代local条件

取β(t)=(t²,t⁴,t⁶)，t在固定[-1,1]δgrid。θ(t)为(t,t²,…,t⁷)的signed permutation。因此任意unit-normal affineH的p(t)=N·θ(t)−u有degree≤7，七个非恒项系数平方和1。若E={|p|≤r}测度m>0，在E中按Lebesgue分位选8点，间距≥c m。Lagrange插值每系数≤C r m^-7，故m≤Cr^{1/7}。sublevel是至多15个interval/point组件（p²−r²非零、degree≤14），均匀δgrid比例≤C(m+δ)。对r≥δ便得

νδ{dist(θ,H)≤r}≤C r^{1/7}。

cube舍入使r添Cδ，不改界；每cell含O(1)timegrid点，uniformcell权重亦可比。参数curve是full moment，齐次观测V_t spanR⁸，Wronskian满秩。尽管如此它仍在Σ上，局部singular结论全成立。此例精确区分globalcap与localspreadout，不是fullsource反例；其smalllabels/Φ尚未给，且R96 polynomial类已在完整source下排除。

## 11. 与旧失败的双向与文献比较

R14 double-block CP、R76 common-root code是固定global Schubert/modelH障碍；本原m1参数可globalspan8且globalcap成立，故不能把二者论证直接抄来。R96 polynomial统一排除是具名GGW与原coarse数据的正用途，本轮局部障碍涵盖所有rough β但只审一个文献输入；两者互不构成全source saving的双向等价。

本证书的代数内容是标准光滑图形的二阶切平面估计。primary对比以实际CSWZ定义和原WZ接口为限；不认证新定理优先权、重大性或完整restricted projection理论已穷尽。不增registry ID、不改78旧ID状态。所有旧equivalent gain冻结保持。

## 12. 结论、停止与下一完整缺口

付得实际nearfull theorem的原质量桥，同时原parameter的所有非空删选都有local二次平坦性，故固定b且ε<b的直接small-loss CSWZ桥关闭。完整rough mixed42、ordinary初始化、HRZ全费用、sticky其余分支和ordinary桥、同一full方向集合严格低维构造仍未解决。

不续b/ε阈值、局部切H常数或bounded可逆变换优化；ε≥b也不在本证书下冒称已排。下一只接受真正不同的原联合约束/有效quotient的全费用应用，或改变完整路线的一手定理，并先独立反攻与双向gain排重。数学证书可内部逐步审，完整Goal继续active。
