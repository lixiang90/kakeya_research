# R0088：锥面几何、原质量与源范数的正式独立审查

2026-10-18，审查者A。限定内部逐步审查，未经外部同行评审；不是新的普通Kakeya界或高级来源wholeproof认证。

## 1. 实际全文对象、primary读域与独立性

本次actual fresh全文读root《R0088_cone_packet_original_mass_transfer_and_stop》十节、B《R0088_null_lift_geometry_and_counteraudit》十节、working_spec五节、终macro六节、next《R0088_next_full_goal_reselection》六节、source_scope《R0088_cone_and_full_goal_source_scope》六节，以及阶段I A《R0088_DIM001_actual_scope_and_frontier_audit》八节、B《R0088_primary_full_goal_input_gate》八节。本人数学稿《R0088_cone_packet_and_source_normalization_audit》十节亦完整读回，但不把自己的正算当作本formal的独立审查；其正证已由root/B实际全文独核，本formal的数学独核对象是root/B的独立链。

primary实际读Xiangyu Wang [2411.02961v8](https://arxiv.org/html/2411.02961v8) §1.1的完整Th1.5/Prop1.7及相关定义、§1.2开头、完整§2.1；本地extracted PDF物理1–6相应段亦实际读过。核到current v8=2026-09-30，源n6的2≤q≤p、2≤k≤4及各p,q分支条件均保留，Cor1.6的渐近范围不代替固定n6。只具名接受Prop1.7的统一Schwartz局部估计，未新独证29页高级递归proof，未本轮独立渲染PDF或核全部bytes。

阶段I已付DIM001/R38/R80/R85的范围与新主数学分开；GLX旧表的7−2√2低于17/4不等于2026最优或major，source的未全文新自证也不是新增内部application gap。B的其它来源全文读域按其真实记录，不由本formal冒认本人重新全文读了这些外文献。

## 2. 共同null-map与residue-clock反攻逐式通过

root§2/B§2的量词是同一共同affine/C1 map，在每一点都有球面非空开方向的局部线送成null切向。令J=diag(I5,−1)，二次型v↦vᵀDFᵀJDFv在开锥上为零，所以矩阵恒为0。其image是totally isotropic子空间；最后坐标投影单射，因而rank≤1，确排rank5 immersion。未把有限Kakeya族每点都授予开方向，也未排按label不同、非光滑或更一般clock/map。初等Lorentz观察不升级独立重大结构结果。

root§7/B§4的真实反攻亦独算通过：取ρ=δ^a、0<a<1/4，原δ方向网有N≈δ^-4；以M≈ρ^-1的四residue单射编码设midpoint a_k=c_kv_k、c_k=K0δ code(k)。max|c_k|≤Cδρ^-4→0，故ρ≤|x|≤2ρ的实际annular marks在原unit段内部；每管marks≈ρδ4，原E体积≈ρ5。角网密度足覆盖内侧fixed angular annulus，反向体积上界也成立。

同一x的两个命中方向只差O(δ/ρ)，故整数indices差<M，residues必不同。|c_k−c_k′|≥K0δ，而|x·(v_k−v_k′)|≤Cδ。K0固定足大便使所有半径cr≤cδ的lift-clock区间逐点不交。于是|Z|=Σ|S_k|≈rρ，|Z|/(r|E|)≈ρ^-4发散。原方向真实分离，a可取任意足小固定数以符合nearfull门槛；不是重复标签，也不是ordinary反例。该例只否统一免费r纤维，未证明|Z|≤C|E|对所有配置常数sharp，更不排全部可能lift。

## 3. 原marks、整端帽与packet下界通过

root§§3–4/B§§3、5保未clamp的t_i(x)=(x−a_i)·v_i。round tube内|t_i|≤1/2+δ、垂直残差≤δ，因此端帽无需删去，任意可测Yi都完整保留。S_i={(x,t_i(x)+h):x∈Yi,|h|≤cr}的shear Jacobian为1，|S_i|=2cr|Yi|，Z确属E×固定interval，非NδE或mark代理。并集vertical fibre不同中心，不能由逐片长度r推统一r上界。

对角宽cδ、radial宽cτ的非负bump，真实频率体积A≈δ4τ；Rpacket=δ^-2时四个中轴δ、长轴1、mini轴r=δ²/τ。源§2.1是plank几何，不能换成round管。modulation exp(−iRpacket a_i·ξ)定位原midpoint；扣除Rpacketρ0h这个积分变量无关的carrier后，相对phase分别为angular二次项O(c²)、横向项O(c)、radial项O(cτrδ^-2)=O(c)。固定小常数使实部正，故整Si上|Ef_i(Rpacket X)|≥cA。

B的spherical坐标展开与root的同式正确；本人的Cartesian坐标核验给相同结果。phase下界是实际积分证明，不由“essential support”倒推；大carrier本身可快转，不能漏其扣除。τ全范围[δ,1]统一，round端帽的稍大clock仍为固定长度，没有隐性λ损。

## 4. 原N、源L²/L∞、六维Jacobian及Hölder预算通过

原方向分离使频率supports可取互不交，故每组random signs均有||f_ε||∞≤1、||f_ε||2²≈NA。空间原管重叠不影响此频率预算；若方向重复便不能继续授L∞≤1。Khintchine处理跨packet复相位，不要求几何labels独立。

本人独立核得root式(3)等价于

    A^p∫M^(p/2)≤C δ^(12−2pεs)(N A)^(p/q)，M=Σ1Si。

δ12来自R6的Rpacket^-6，不是原R5的δ10。源L²的2/q幂在p次方后是(NA)^(p/q)，没有漏一半。另一侧真实L1为2crI≈rλNδ4；p>2时Hölder给

    ∫M^(p/2)≥(rλNδ4)^(p/2)|Z|^(1−p/2)
             ≥c(rλNδ4)^(p/2)|E|^(1−p/2)。

后一负幂使用|Z|≤C|E|的方向正确。代A=δ4τ、r=δ²/τ后，升幂前δ指数为7p−12−4p/q，N与τ均为p/2−p/q。故对每ν>0，root式(4)/B式(12)确为

    |E|≥cν λ^[p/(p−2)] δ^[β+ν] (Nδ4τ)^b，
    β=(10p−24)/(p−2)，b=p(1−2/q)/(p−2)∈[0,1]。

非饱和N原样保留；等价raw δ幂为(14p−24−8p/q)/(p−2)。Th1.5严格范围改用全空间Lq范数只消R^ε，不改善主幂；不是以一次有限样本或数值实验代替上述算术。

## 5. 必要p、显示式的用途与两种密度闭包通过

必要p不是从cone conjecture的声称充分区间取来：固定smooth annular bump，在相应light shell的stationary angular direction上，四维角驻相主项≈L^-2；选法向固定小厚度及一个角patch使radial主系数不抵消。正负clock只换选择相反角度／shell。半径ρ壳体积≈ρ4dρ，p<5/2时局部Lp norm至少A^(5/p−2)。对每任意小εs的源估计因此必要p≥5/2；全空间endpoint另有log发散，未冒endpoint已证。

β=10−4/(p−2)单调增加，故必要区间给β≥2。b≥0且τ≤1，使显示式在τ=1最有利；稀疏Nδ4≤C及λ≤1也不会补出δ固定正幂。要由这同一标量公式给目标δ^(1−σ)，需p<22/9，与必要性冲突。这里仅说该显示lower的保证不足，不给真实体积upper、不否其他bilinear/多尺度cone机制，更不是Kakeya反例。

平均版直接由I使用同式，根本不必heavy，所以没有平均⇒逐管的偷渡。若另选择重管，则I_H≥I/2、N_H≥λN/2，必须把实际N_H放回公式；不能免费保持原N饱和。任意删labels保原方向分离，但N/I/λ重记；删marks也只按实际剩余质量调用。近满λ≥δ^η只增加正亏损，不能把β2降到小于1。

## 6. 最终限定结论、宏观／后继及审查层级

root10与B10的完整有限来源应用及两种具体桥反攻全文通过本次独立逐步审查，未发现未解决强制修正项。自己的A10不计自身独审；它已由root/B的实际全文审查另行覆盖。主数学没有fullsource或all-dimensional theorem条件的偷换，也没有借old DIM推论充本轮新成果。

终spec5、macro6、next6和source_scope6的停止范围与实际证明一致：冻结共同open-direction null-map捷径及独立label-lift＋单次scalar extension/Hölder读出，不续τ/q/k/p数字或desired共同纤维；不否一切未来cone方法。ordinary初始化、directHRZ实际倍率、完整sticky与ordinary桥、同一full方向低维构造四路仍开放。当前无qualified新gain、Goal active；保守ordinary/fullbranch streak11与本轮真实来源／费用信息分开，没有complete/blocked或major/newID声明。

此为内部有限范围reviewed，未经外部同行评审。新源Th1.5/Prop1.7及其高级proof层次仍具名；本formal不认证作者AI披露、root的下载身份或未来metadata/Git/sync。本人只写授权formal，完成后停止编辑与检索。
