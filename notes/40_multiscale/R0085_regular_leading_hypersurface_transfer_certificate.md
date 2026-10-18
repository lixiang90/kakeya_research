# R0085：原高维近轴的regular-leading转移与旧DIR等价边界

2026-10-18，root。root/A/B及两formal已实际全文逐式审过，限定通过。它是具名4D有限输入的一次真实几何应用，不作为新gain phaseII、不新增ID/major/novelty；完整ordinary和全G4仍未解，未经外部同行评审。

## 1. 命题、原对象及条件

固定D≥1、R≥2、C≥1、κ∈(0,1]，degree d∈[1,D]的非零实P可随δ变，全部系数绝对值和≤1；P_d为真实最高次齐次项。原unit轴ℓ_i=a_i+t v_i, |t|≤1/2, |v_i|=1，整轴在B_R∩N_(Cδ) Z(P)，T_i=N_δℓ_i。原非负权w_i，总W>0；每个固定C0δ物理无向角帽原权≤α，indices可重复。要求每原label |∇P_d(v_i)|≥κ；这不是由physical regularity免费给。可测Y_i⊂T_i，E=∪Y_i，逐管|Y_i|≥λu_δ，λ∈[δ^η,1]，u_δ≈δ4。对每σ>0，取η,δ0足小，依具名DIR003有 |E|≥c δ^(4+σ)λ^(2D+1)W/α。平均版λ=Σw_i|Y_i|/(u_δ W)多付λ一次。取σ=ε/2、η≪ε/(2D+2)得nearfull δ^(4+ε)W/α。绝不声全部λ同常数critical maximal。

## 2. 已有源与不锁新增益的理由

R29/R38/R80的DIM001内部桥已经付，M3全λ不改变KT饱和入口的d参数；FY仍需固定midpoint/hitting-set packing而ordinary不授。此certificate不同于R61的R4 line-parameter Σ⊂R6 dim≤3假设，也不由R60 dim≤3物理载体直接覆盖；但其正幂强度与旧DIR4相互推出（§10），不能换名成为新方向。只核从真实P到该既有输入的全部接口；完整G4没有leading-gradient假设，尚未锁新gain。外部高级proof引用层次保持。

## 3. unitclock最高系数与同坐标非短投影

bounded coefficients使B_(R+2)全部固定阶derivatives≤M=M_D,R。距离假设给wholeaxis和T_i上|P|≤Aδ。对p_i(t)=P(a_i+t v_i)取d+1个固定分离节点，Lagrange最高系数得到|P_d(v_i)|≤A_Dδ；这是wholeclock数据，不是shading点插值。令g_i=∇P_d(v_i)，选j(i)∈{1,…,5}使|g_ij|≥κ/√5。Euler g_i·v_i=dP_d(v_i)=Oδ。由|g_i|≤M和该非零坐标，δ足小推出r_i=|π_j v_i|≥c_D,R κ（否则v近±e_j而内积不能小）。按j分五个whole-label组；每组使用同一正交π_j，原权和质量不改归一。

## 4. 投影帽恢复：近零而非exactzero

固定j，写u_i=π_jv_i/r_i∈S3，s_i=v_ij/r_i，|s_i|≤C_κ。齐次性给|P_d(u_i+s_i e_j)|≤C_κδ，|∂_jP_d(u_i+s_i e_j)|≥κ/√5。任一projected Cδ帽内选中心u0；系数与s范围有界，p(s)=P_d(u0+s e_j)满足在所有s_i处|p(s_i)|≤A_κδ、|p′(s_i)|≥cκ。把有界s区间按p′=±cκ和p=±A_κδ分成O_D(1)段；在满足这两不等式的段上p单调且导数至少cκ，每段长≤C_κδ。故所有原v_i落固定数个O_κδ原角帽，总原权≤C_D,κ α。有限有向charts和相邻格覆盖只改固定常数；没有假projected δ-directions separation或去重。

## 5. 同坐标多项式sublevel与原端帽

D≥2时h_i(t)=∂_jP(a_i+t v_i)次数≤d−1，最高t^(d−1)系数恰g_ij，绝对值≥κ/√5。若d=1，h_i是该非零常数，单列不必sublevel。对次数m=d−1≥1的一元h，其最高系数≥κ/√5，而|h|≤2τ的集合长度b，则从该集合选m+1个彼此相隔≥c_m b的分位点，Lagrange最高系数给κ≤C_m τ b^(−m)，即b≤C_m(τ/κ)^(1/m)。取τ=c_D,R,κ λ^(d−1)，常数c足小，使bad clock长度≤c0λ。实体roundtube先删两个端帽的O(δu_δ)质量；其余以正交clock t=v_i·(x−a_i)积分，bad clock损≤C b u_δ。选c0小、δ≪λ及Mδ≪τ，保留Y′_i⊂Y_i且|Y′_i|≥cλu_δ，并有|P(x)|≤Aδ、|∂_jP(x)|≥τ。原点没有被移动或填满阴影。τ≥cδ^(η(d−1))使δ误差可吸收。

## 6. 真实物理纤维与阈值阴影

令E_j=∪_(j(i)=j)Y′_i。固定z∈e_j^⊥，一元q(t)=P(z+t e_j) degree≤D。集合|q|≤Aδ且|q′|≥τ至多O_D(1)单调段，每段长≤2Aδ/τ。因此沿同一kernel的E_j纤维长≤C_Dδ/τ；这用实际点集合，不是δ-neighborhood代理。定义f_j(z)=(τ/δ)∫1_Ej(z+t e_j)dt，故0≤f_j≤C_D。每π_jT_i被一个长≤1、宽C_κδ且体积≤C_κδ³的roundtube S_i包住；非短r_i给固定下界，可固定extend其轴，不添加marks。由Fubini ∫_(S_i) f_j≥(τ/δ)|Y′_i|≥cτλδ³。取F_j={f_j≥c1τλ}，常数c1足小，则|F_j∩S_i|≥c2τλδ³。记θ=c2τλ≈λ^d；所有原indices及投影帽权Cα保留。

## 7. 具名DIR的真实Lebesgue桥：θ²而非填格

固定一个有界4D graphchart，S_i的真实阴影Z_i=F_j∩S_i密度≥cθ，方向格权≤Cα。共同随机shift ζ∈[0,h)^4，h=C_κδ（固定比较），G_ζ=hZ4+ζ。每管总格点≤C h^-1，而E_ζ #(Z_i∩G_ζ)=h^-4|Z_i|≥cθh^-1，故rich事件 #(Z_i∩G_ζ)≥c′θh^-1的概率≥c″θ。对所有rich indices，固定数clock-slots将这些真实点送到原支持line的h时间marks；每clock层点数O1，选一个slot只损固定倍。源occupiedcells数≤C #(F_j∩G_ζ)，方向bin权≤Cα。选η使θ≥cλ^d≥h^(ηsrc/2)，所有rich线满足DIR003门槛。DIR给 #(F_j∩G_ζ)≥c θ h^(σ−1) W_rich(ζ)/α。取期望，E W_rich≥cθ W_j，且E #(F_j∩G_ζ)=h^-4|F_j|，得 |F_j|≥cδ^(3+σ) θ² W_j/α。不同indices从未假独立，权跨度不限；常数clock-padding、homothety和finitecharts均固定。此处确有两次θ，不能用occupied Nδ(F)代实际体积。

## 8. 回原E、平均与量词闭包

从阈值定义 |E_j|=(δ/τ)∫f_j≥c(δ/τ)(τλ)|F_j|，故 |E_j|≥c δ^(4+σ) λ(τλ)²W_j/α≥c δ^(4+σ)λ^(2D+1)W_j/α。所有E_j⊂E且j仅五个，Σ|E_j|≤5|E|、ΣW_j=W，合并得到§1。平均密度先删|Y_i|<λu_δ/2的labels，保留weight W1≥λW/2，逐管λ/2；角帽原α继承，得λ^(2D+2)W/α，不偷保W或N。whole-label restriction保P/κ/α（未归一）；任意裁shading须重算density。全λ不因λ显式幂次就免费获得，η依σ且δ0依参数；source依赖和ε/η/δ顺序明确。

## 9. 真实缺假设校准与不声反G4

P=x5−x1²（固定倍缩放令coeffnorm≤1）physical gradient≥c，却不能给fixed leadingκ。可取a在[-c,c]的L√δ格，r在[τ0√δ,2τ0√δ]的Lδ格，b,c′在[-c,c]的Lδ格；v=(r,b,c′,sqrt(1−(1+4a²)r²−b²−c′²),2ar)，中心A=(a,0,0,0,a²)。原unit轴满足P(A+t v)=−t²r²，故整轴nearZ(P)，全Y=T，N≈δ^-3。不同r/b/c′由自身坐标分离，只有a变时v5差≥2τ0Lδ，所以取L大给原δ方向分离；全部|∇P_2(v)|≈√δ，不能保任何fixedκ labels。union上界≤Cδ。反向固定x4=s∈[1/8,1/4]，同a的(r,b,c′)→(r,b,c′)/v4有uniform Lip逆z→z/sqrt(1+(1+4a²)z1²+z2²+z3²)；异a包x1间隔L√δ而位移O(τ0√δ)。slice centers因而δ分离，原tube内4D cδ球两两不交，积分给union≥cNδ4≈δ。该校准是R53/R55已知parabolic模板的ambient扩充，仅拒免费leadingregularization，不是新数学counter、非完整ordinary Kakeya或反全G4。

## 10. 双向正幂排重、完整缺口与停止

正向是上述DIR4应用。反向取P=x5、把任意4D source管族与真实shading乘法向区间[-cδ,cδ]嵌入R5的Cδ管：|∇P_1|=1，方向帽权保持，E5体积≈δ|E4|；应用nearfull regular结论、除δ返回4D nearfull finite方向输入。固定倍cells/marks包装同DIR003/R62。因此该命题在正幂量词上是既有source的几何transfer，不能新立方向/ID或major。它未证明全G4的singular或δ退化leadingform，也没有ordinary新界。R56 Euclidean nearjet leadingform障碍不因这里输入κ而消失；R61参数Σ假设不被冒用。完成certificate后停止regular proof的D/κ/模型迭代，完整macro回四路径；目前无合格新增益主命题，Goal active。
