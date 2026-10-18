# R0091：全单位线段矩阵测度、任意原集资格及局部秩出口

2026-10-18。具名输入是DPR arXiv1601.06543v2 Cor1.13与标准Jankov–von Neumann选择定理；后者见Moore原讲义Th49。以下初等构造独立写全。**未证明ordinary/general Kakeya或新的维数增益，未经外部同行评审。**

## 1. 首要缺口和本轮量词

首要目标仍是由真实full方向Kakeya条件推出R5 Hausdorff维数>4乃至5，或同一集full方向且严格低维的真实反例。固定任意K⊂R5，每个v∈S4有a+[0,1]v⊂K；方向取归一化球面概率σ。可定向重复同一无向方向，不影响定义。以下假设h=dimH K<5，构造一个**同维包络G内**的全线段law，检验微分约束定理能给什么。原K非可测时，不伪称在K上已经有Borel law。

这与原paper Def17的δ管、finite marks、jointAD和κ1结构不是同一输入接口。本轮不把该source的filledX自动提升为连续current，也不把旧polar/hyperplane端点重名。

## 2. 任意K的同维Gδ包络与选择

取s_j=h+1/j。因H^{s_j}(K)=0，可取开球cover {B_ji}，diamB_ji≤2^{-j}，且Σ_i(diamB_ji)^{s_j}≤2^{-j}（从通常Hausdorff覆盖稍扩开球并预留常数即可）。令U_j=∪_iB_ji、G=∩_jU_j。则K⊂G。对任意s>h及充分大j，s_j<s且diam≤1，于是H^s_{2^{-j}}(G)≤Σ_i diam(B_ji)^s≤2^{-j}。任取固定尺度ρ，再用j→∞且2^{-j}<ρ，得H^s_ρ(G)=0，故H^s(G)=0。因此dimH G=h；当h<5，G为Borel Lebesgue零集。

在Polish空间S4×R5上定义R_U={(v,a):a+[0,1]v⊂U}。U开时，紧线段至闭集U^c有正距离（U=R5情形平凡）；小幅改变(v,a)不破包含，故R_U开。于是R=∩_jR_{U_j}为Gδ且投影等于S4。标准JvN定理给universally measurable a(v)，对**每个v**满足(v,a(v))∈R。这里只调用该标准选择定理，不声称一般R有Borel uniformization。

相对于完成σ，a可测；可用简单函数逼近逐坐标取得Borel版本a_0，与a在σ-conull集合相等。以下标准Borel pushforward用a_0；它的线段属于G在σ-a.e. v成立，足以保证概率law由G承载，全方向边际仍严格等于σ。没有给a_0加有界或一阶矩假设。特别注意：**μ(G)=1不等于sptμ⊂G**，选出的段在G中，不保证在任意非可测原K中。G的维数等于K，故这是合法的维数归约，不是改强原假设。

## 3. 全clock联合law与真正可付Frostman界

令F(v,t)=(a_0(v)+tv,v)，t∈[0,1]取Lebesgue概率，ν=F_#(σ⊗dt)，μ=(π_x)_#ν。二者是Polish空间上的Borel概率，因而有限Radon测度；μ(G)=1。即使a_0无界，仍有限，所有后面的v权重绝对值≤1，不需anchor矩。

对任意位置球B_r(x)，单条单位直线在球内的clock长度≤min(1,2r)，因此μ(B_r(x))≤2r，0<r≤1。若在R5×S4取product Euclidean球半径r，则只有v落在O(r)球面cap才可命中，σ(cap)≤Cr4；每个这样的v仍只有≤2r clock。因此ν(B_r(x,v_0))≤Cr5。**joint5-Fst不会因位置投影自动变成μ4/5-Fst**。这是全clock计数，不借方向selector任何连续性。

## 4. PSD矩阵与端点项的完整计算

对Borel B⊂R5定义

S(B)=∫_{S4}∫_0^1 1_B(a_0(v)+tv) v⊗v dt dσ(v).

则S为有限对称PSD矩阵值Radon测度，trS=μ，总矩S(R5)=∫v⊗v dσ=I5/5。定义row-wise (DivS)_i=Σ_j∂_jS_ij。对ψ∈C_c^1(R5;R5)，

⟨DivS,ψ⟩=−∫∫ v·Dψ(a_0(v)+tv)v dt dσ
=∫ v·[ψ(a_0(v))−ψ(a_0(v)+v)]dσ.

所以DivS=∫v(δ_{a_0(v)}−δ_{a_0(v)+v})dσ，是TV≤2的向量测度，端点同样由G承载a.e.。Fubini/分部积分合法，因为ψ和Dψ有界，积分域概率且|v|=1。一般端点项非零；本构造不是homogeneous DivS=0。但DPR Remark1.3/Cor1.13**允许有限measure RHS**，故端点不是该定理的阻断项。

## 5. 从具名结构定理实际得到的结论

Radon–Nikodým写S=Aμ。PSD与trS=μ给A(x)≥0、trA=1 μ-a.e.。用Frobenius范数，1/√5≤|A|≤1，所以|S|=|A|μ与μ互相绝对连续，二者奇异部分同零集。row-Div的symbol为M↦2πiMξ，wave cone恰{M:rankM≤4}。具名DPR Cor1.13于是给rankA≤4，在μ_s-a.e.成立。若h<5，μ由Leb零G承载，μ_s=μ，结论覆盖μ-a.e.。此处不新认证DPR主§2 PDE证明；实际独核的是应用前提、symbol和极测度转换。

对ν关于x的标准disintegration，ν=ν_x(dv)μ(dx)，A(x)=∫v⊗v dν_x(v)。若ξ∈kerA(x)\{0}，则0=ξ^TAξ=∫(ξ·v)^2dν_x，故ν_x由ξ^⊥∩S4承载。只得到**在几乎每个位置的条件方向law**位于某4平面。没有固定全局平面，没有可用C1法向场，没有跨尺度共同chart，也没有按某4平面组织的完整R4 Kakeya全方向族。更没有从rank≤4推出μ绝对连续或Hausdorff维数5。

## 6. 真full方向bush：全局矩阵不授局部rank或位置4-Fst

取a(v)=0，G=K=闭单位球，所有线段[0,v]是真unit直段，方向law严格σ。对0<r<1有μ(B_r(0))=r；因而任何统一μ(B_r)≤Cr4均失败。极坐标计算在0<|x|<1给

dμ/dL5(x)=1/(|S4| |x|4)， A(x)=x̂⊗x̂.

这里μ**绝对连续**但密度在原点无界，A为rank1 μ-a.e.，同时S(R5)=I5/5。故连真实wholeclock/full角边际也不保证位置处五个独立方向，或共同五current局部span。该例K有正5维体积，**不是Kakeya低维反例，也不是原Def17 κ1配置反例**。它只排除展示的局部满秩/4-Fst免费推断。

## 7. 纯PDE与全局二阶矩的4维校准

令Q_i={x_i=0, |x_j|≤1(j≠i)}，P_i=I5−e_i⊗e_i。H4(Q_i)=16；不同Q_i交集H4零。定义

S_*=(1/320)Σ_{i=1}^5 P_i H4⌞Q_i， μ_*=trS_*.

总矩ΣP_i/20=I5/5，总trace=1；μ_*由有限4平面片承载，纯奇异，且dS_*/dμ_*=P_i/4在Q_i一般点rank4。分布Div(P_iH4⌞Q_i)仅为该4cube各面的有限有符号向量H3测度：沿i法向无导数，沿其余坐标做一维分部积分；故DivS_*有限。由此，**PSD+tr概率+全局I5/5+有限Div**本身允许真实4维carrier。缺失的是原全部方向的whole straightline transport，不能据此证伪Kakeya，不能把此例当§2–5完整原门的反例。

本轮只检验明列的二阶矩/PDE shortcut，不声称所有有限moment工具、所有A-free方法或所有多尺度机制均无效。未注册新数学结果ID，以上是标准输入应用与明确校准。

## 8. Whole-label和任意shading的闭包必须分开

对Borel方向label Ω且m=σ(Ω)>0，限制σ再除m，仍是全unit clock概率；同样TV(DivS_Ω)≤2。joint5-Fst常数至多C/m；总矩变成m^{-1}∫_Ωv⊗v dσ，不能仍写I5/5，也没有统一ellipticity常数。若不归一化，质量m、端点TV≤2m。此类whole-label选择闭合。

任意Y(v,t)∈{0,1}的shading即便平均密度λ、或更强每条管密度都等于λ，均不控制clock BV variation。令每条线同用E_m=∪_{j=0}^{m−1}[j/m,(j+1/2)/m]，每条密度严格1/2，但1_{E_m}的分布导数TV=2m。单条直线的相应current边界即2m个端点。要避免多方向端点抵消的疑问，全方向a=0 radial bush也精确给DivS_sh由不同半径球面上的±v σ组成；r=0端点向量∫vσ=0，其余2m−1个球面互异，TV=2m−1。归一化质量后还乘2。令δ≈1/m，就是δ^{-1}边界费；方向平均和逐管density均未改善它。故有限δ选点/marks不能无费得到uniformly normal wholeclock substitute。BV不受控的更一般mask甚至可有无限边界。

## 9. Normal-current/Frobenius直接桥未付输入

DPR Cor1.12用五个normal1-currents时，需同一正测度η对每个current mass绝对连续，并且五个方向在η-a.e.处张成R5。原线段方向全局分成五cones，只给五个位置边际μ_i；bush里它们可在角域上几乎不重叠，不能赠共同η或局部span。S的五rows虽有有限Div，奇异部分依同一ξ落四平面正是§5，没有额外第五方向。

AMS1907.07456v3 Th1.3在**C1的k平面分布V**与真实有限boundary的normal k-current T=τμ且spanτ=V μ-a.e.下，按一阶commutator扩大维数的区域给更高Hausdorff绝对连续性。若要用于source中的rank3几何，须先构造normal3-current、证明其质量由原点/marks支配并返回原质量，再付C1及真实non-involutivity。三个normal1-currents的形式wedge没有一般可乘定义或normal-boundary控制；即使它们都有Lebesgue密度并可作形式wedge，各自有限div也不控制wedge引入的横向分布导数（见B8具体校准）。这不是声称有界BV函数的乘积不保BV。k=1的C1 line distribution本就involutive，不能靠原线段normal1-current自动取得更高维结论。filledX/coarse coherence没有支付上述输入。

## 10. 停止判定与保留的完整目标

实际正向资格已经包括任意非可测原K的同维归约、真实full方向/fullclock构造、有限端点RHS、joint与投影Fst区别，以及DPR只给singular-rank的精确scope。直接出口失败有三个不同层次：真实bush反局部rank/Fst；4flat例反弱PDE+globalmoment的5维推断；真实full方向mask反density⇒uniformboundary。三者均没有构造低维Kakeya。

因此拒锁phaseII新gain，停止全局矩阵矩/标准rank约束直达ordinary5、以及未付normal3/C1的Frobenius桥。四维paper/G4完整κ1、ordinary初始化与marks质量、directHRZ完整费用、同一full方向严格低维构造仍未证未否；条件DIM001/R38/R80不重排。不用平滑、椭圆性或新density公设重命名原缺口。本轮无ordinary新界/完整branch-saving/重大或新颖认证，Goal active。下一轮先完整四路宏观重选，若无qualified gain须如实记录，而非把困难当external blocker。
