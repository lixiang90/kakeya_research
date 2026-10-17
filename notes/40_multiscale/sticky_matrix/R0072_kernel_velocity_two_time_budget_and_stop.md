# R0072：共同核速度的原双时刻响应及停止

2026-10-18，root。唯一规格先存research/rounds/R0072_working_spec.md§2。完整ordinary n≥5/general Goal active。本稿检验actual d5/k=ell3 common-kernel分支中的kernel速度basicness机制；不是R71细packet、R59商3AD断言重述或新增smooth/rational类。未经外部同行评审，最终独审另列。

## 1. 源、量词及真正目标

保Wang–Zakharov2609.22035v1 Definitions17.2–17.4全部原T joint4AD/CW、Z/绝对clock、Y_t AD(2−κ)/tubeKT(1−γ)、filled X、pointΦ κAD/slabγ与跨尺度ξ/Φ coherence。κ>ζ>0、γ>0先固定，η最后小，δ最后小。原u仅dyadic Lipschitz。在原common-kernel alternative f(t)=F0+u(t)eᵀ下，经共同bounded shear/rotation可写f=u(t)e1ᵀ。u若共线回R16已付linewise；本轮不假u有曲率或预选good-rank pairs。

目标是从同一原管两个终时的响应迫ξ在固定(y,x1,t)的长kernel fibre上近乎basic，继而真正付R59典型invisible fibre、商AD lower/密度/亏损，或直接排正κ。所求不是一个ρ-point cube内ξ的ρ-bin upper：后者早由coherence有界；长kernel fibre横跨许多这种cube。

## 2. 先行旧账、闭包与来源修正

R58–59已给商3-Frostman upper及每occupied商ρ-bin最多K^C/ρ个lifted bins，未给相反典型lower。重复这个商upper不算新结果。R16排common-image/pencil，但不排任意二维u。R64 raw分类、R65 fixed rational排除不供应本轮basicness。点态光滑Burgers/导数论证不能从dyadicLip和稀疏原visits推出；不使用Markov/BSG或独立time-angle替换。

整label限制保其已有shading；删marks仅保实际重算的平均与逐active tube下界，point Φ lower/AD也须重新付。新core只继承原T上界/CW，不宣新complete configuration。两个时刻必须取同一原管的实际selected visits，不能从两个独立arm图求交。

初稿spec所写简式漏了native标签的x1项；A在施工前半程指出，已及时修spec。以下并列原标签与固定root中心化量，跨root不移去这项。

## 3. 同管两终时的精确响应

固定原p=(x1,x2,y+u(t)x1,t)及其真实管T，水平斜率φ=(φ1,φ2)，法向斜率ξ_p+u(t)φ1+Oδ。h=s−t，终点水平x1,s=x1+hφ1+Oδ，native grain label满足

    y_s=y+hξ_p+[u(t)−u(s)](x1+hφ1)+Oδ.             (1)

对固定root(y,x1,t)，定义hat y_s=y_s−[u(t)−u(s)]x1，才有

    hat y_s=y+hξ_p+h[u(t)−u(s)]φ1+Oδ.              (2)

φ2、实际管、所有重复root/终点标签均保留。(1)只在该管确为终点原selected incidence时可同时使用终点ξ兼容；单有轴线穿过E不够。

若n_s⊥u(t)−u(s)，则n_s·(hat y_s−y)=h n_s·ξ_p+Oδ。π_nY_s可有满一维投影，tubeKT给细条带内绝对cover upper，不能将其改成该投影的低维upper。两个不同n_s也没有自动的乘积推前law。

## 4. 原质量：能付同管双终时，不能付basicness

在原ρ-time窗J保全空间，先按原incidence阈值做point、tube及kernel-fibre core。这里fibre严格指(t,原y,x1的dyadicδ-bin)，保组内全部actual p；δ-separated X不授exact实数x1纤维lower。以bin中心代x1只增O(Kδ)响应误差。令m≈#(Z∩J)，D0=δ^-κ，I为保留原incidence总数；K含原δ^-Cη及实际已付损失。相应原全carrier计数为

    #points≤K m δ^(−4+κ),  #T≤Kδ^-4,
    #kernel fibres≤K m δ^(−3+κ),  I≥K^-1 mδ^-4.

按足小K^-C阈值迭代删degree低的三类顶点，每个顶点只删一次，用原三类数量上界合计控制删除，保I固定比例。余下每point至少K^-C D0角/管incidences，每active T至少K^-C m visits，每active kernel fibre至少K^-Cδ^(−1−κ) incidences，因每point最多K D0条selected directions，故有至少K^-Cδ^-1个原x2点。阈值和type数固定，所有费用仍K固定幂；不将每fibre的degree当每x2的新AD lower。

若m_T为active T访问数，则同一tube、一个root和两个终时的真tuple数

    sum_T m_T^3 ≥K^-C I m².                       (3)

原reference保tube/root标签，有限分离clock端帽可用δ-separation上界付掉；不把长kernel fibre缩成单个ρ-point cube。A稿给完整source及named19.4的可选u-gap筛选。仅平均density不足以直接断每tube平方矩lower，故上面的active tube threshold是必要步骤。任意后续删shading必须重核这一步。

## 5. 两终时恢复、实际误差与不可见变量

设|h_i|≥qρ，|u(s2)−u(s1)|=d>0，u在该窗振幅≤Cρ。两终native y labels的误差≤ε（含δ，且root原坐标固定）。令

    R_i=(y_si−y−[u(t)−u(si)]x1)/h_i.

则R_i=ξ_p+[u(t)−u(si)]φ1+O(ε/(qρ))，因此

    R1−R2=[u(s2)−u(s1)]φ1+O(ε/(qρ)).

用这个真实非零向量内积恢复标量φ1，进而恢复ξ，精度分别至多

    errφ1≤Cε/(qρd),   errξ≤Cε/(qd).              (4)

无须Δu与另一个向量构成2×2 determinant；要除的是同一非零向量长度。但d的原质量下界不能先假。即使通过原19.4付d≥ρ^(1+b)，若同时要φ1和ξ到ρ精度，仍需ε≤c qρ²d，约qρ^(3+b)；天然ρ²编码并不自动够细。nativeδ floor另核，不能以取更细proxy改变observable误差。

即使(4)精确可逆，它不恢复x2或φ2。没有新原质量断言使x2在固定(ξ,φ1)纤维有ρ^-1种选择；这正是所求而非恢复公式的后果。

## 6. 真实输出cover与tubeKT用途测试

两个终时各有AD(2−κ)的Y载体，固定窗/patch半径R内ε-cover的已付upper是K(R/ε)^(2−κ)各一份，乘积upper为K^C(R/ε)^(4−2κ)。恢复(ξ,φ1)把它限制到一个三参数响应像，但没有把实际carrier压成K个ξ bins；更没有原x2纤维lower。乘积upper是允许过覆盖，不能倒过来称实际输出lower或不可能性。

固定p后，每个终时的(1)沿u(t)−u(s)的一条线变化φ1，长度ℓ≈|s−t||u(t)−u(s)|。原tubeKT给该条δ细管内≤K(ℓ/δ)^(1−γ)个Y bins；point Φ投影φ1的slab upper给每个output bin最多K D0(δ/ℓ)^γ条原角/管。保留φ2重数，故fixed(p,t,s)实际selected visits数至多

    K^C D0 (δ/ℓ)^(2γ−1).                         (6)

原方向误差、label Oδ和相邻线管只改固定倍；KT查询δ≤ℓ≤1，细角slab宽δ/ℓ≥δ。小γ时不矛盾，但γ>1/2有真实saving，不能漏掉这项原source参数子范围。

具体在A§3–4的good同管pair中，|u(s2)−u(s1)|≥σ=ρ^(1+b0)，|s_i−t|≥qρ，至少一个i有|u(t)−u(si)|≥σ/2。于是该分量ℓ≥c qρ^(2+b0)。取q=δ^b1、0<b0<1、b1<(2−b0)/8；ρ≥δ^(1/4)给

    δ/ℓ≤Cδ^c0,  c0=(2−b0)/4−b1>0.

对所有p求和，选good终时i有至多两种，另一free终时至多m；(6)给总tuple upper K^C #P D0 m² δ^[c0(2γ−1)]，而(3)与原I≈_K #P D0给lower K^-C #P D0 m²。固定γ>1/2先选，原η及core损失最后小，矛盾。因此在named19.4及全部原source输入下，**完整common-kernel配置的γ>1/2子范围被排除**。未使用rational/smooth假设、未缩κ，未从R70 mixed43搬参数结论。

当前commonkernel原量词仍为0<κ≤2、0<γ≤1，不能错误套R70的γ≤1−κ；该限制属不同mixed43分支。pointΦ κAD与slab还给γ≤κ+O(η)，因此γ>1/2只触及κ+γ>1的额外子范围。对γ≤1/2，(6)无positive saving；把两终时各自的upper与一份原φ1 law相乘不产生两个独立φ1，原basicness/wholecommonkernel仍未付。

因此确实支付了原同管多时质量及恢复，但到basicness/商lower或κ结论仍断。以下反攻检验常被暗用的local coercivity，而不拿toy否全source。

## 7. near-full kernel dust及多bin Lipschitz响应

取b为足够大20倍整数，B=2^b，h=B^-N，细source δ=B^-(N+4)，N为5倍。M=2^(b−5)，L=2^(b−8)。所有数用base B有限小数sum d_j B^-j，位数N；字母范围至多B/16，首个不同digit主项远大于后续tail，故digit映射及下述定标均有固定Lipschitz常数。固定B⁴细buffer保所有线性缩放后的terminal Y/Φ字面δ-separated，计数指数只改依b的固定倍。b在η之后选，N再充分大，常数可依b而不依N。

令X2的每位digit为0,...,L−1，#X2=L^N≈_b δ^(−1+8/b)。令

    Vdigits=2^(13b/20+3), β=13/20+3/b,
    v(x2)=c sum floor(d_j/(L/Vdigits)) B^-j,

其中c>0固定充分小，b≥40使L/Vdigits为正整幂2。首位差估计使v在X2上有统一Lipschitz upper；可取c吸收固定常数。其image是β-AD的finite Cantor V，均匀X2推前到均匀V，每个image point恰有(L/Vdigits)^N个preimages。取ξ=e2 v。

在每个allowed/coarseρ-bin有N_ρ(V)≈_b ρ^-β。因此只保K^C个ξ的ρ-bins，能保的原均匀x2质量至多C_b K^C ρ^β；当η远小于固定µβ且ρ=δ^µ时，达不到任意小δ^a原保留量。这严格否定‘near-full kernel dust+Lipschitz/coherence本身迫ξ basic’。只在一个ρ-point cube中数ξ bins仍当然有界，两者不矛盾。

## 8. 同一真直线的双终时、pointΦ及两个低维terminal carriers

下面给更严格local校准，使单纯两时恢复也不独自迫basicness。每5个digit位置有A-only两位、B-only两位、overlap一位。设a1,a2的自由digit支集分别为A-only∪overlap及B-only∪overlap，各自由digit允许0,...,M−1，其载体A1,A2均为a-AD，a=3/5−3/b。

逐digit定义x1=2a1−a2及φ1=4(a2−a1)：A-only令a1∈[0,L)、a2=0；B-only令a1=0、a2∈[0,L)；overlap令x1 digit k∈[0,L)，a1 digit M/4+j，0≤j<M/32，a2=2a1−k。后者确在[0,M)。代数在真实实数加法成立，允许x1为有符号digit表示，不需假无carry。首位分离保证#X1=L^N≈_b δ^(−1+8/b)且dimension1−8/b。

对固定x1，仅overlap j可变，故φ1为一份平移的β1-AD Cantor集，β1=(b−10)/(5b)=1/5−2/b；平移随x1 Lipschitz。另令φ2独立取每位2^(11b/20+2)个初始整数digits的Cantor集，dimensionβ2=11/20+2/b。于是每p的Φ_p=(φ1,φ2)为κ-AD，κ=β1+β2=3/4。产品在任意slab的upper用至少一个大的法向分量逐坐标条件化，指数min(β1,β2)>1/10，故可取固定γ=1/10。跨point粗Φ用Lipschitz平移及固定倍相邻网格cover可付coherence，不从不同point的fineΦ免费造全局fineκ prior。

初时t=0、单grain y=0，X=X1×X2满足#X≈_b δ^(−2+16/b)≥δ^(−2+η)（b>32/η，N后足大）。取s1=1/4、s2=1/2，u(t)=(t,t²)，真实直线从p=(x1,x2,0,0)出发，方向为(φ1,φ2,e2v(x2))。它的同一条轴在两终时满足x1+s1φ1=a1、x1+s2φ1=a2，native标签严格为

    y_s=−u(s)a_s+s e2 v(x2),  s=s1,s2.             (5)

各terminal carrier可取线性像Y_s=−u(s)A_s+s e2V。u(s)首分量非零，线性map可逆，故它为AD(a+β)=AD(5/4)=AD(2−κ)。产品A_s×V的tube cap指数max(a,β)<9/10=1−γ：对长τ宽ε管，以在一个坐标范围Oε的截面逐格数，得≤C_b(τ/ε)^max(a,β)，固定线性map只改常数。u(s1),u(s2)独立，恢复(4)没有rank障碍，ξ仍有正β熵。

所有坐标/斜率在固定小盒内，固定homothety可使单位直管和端帽约定一致。此构造不是有限数值实验；digit计数证明覆盖所有N的有限代数族。它没有证明任何连续Kakeya反例。

## 9. 校准的严格边界及terminal selected-incidence冲突

该模型只保一个初grain、near-full X、初point ξ/Φ coherence及真实同管两次落入具指定AD/tubeKT的terminal carriers。没有构造完整Z近满clock、整T joint4AD/CW、所有terminal point的Φ/ξ selected incidences及全尺度跨timeY条件。可人为填充terminal horizontal grains，但这不供应这些缺失数据。

尤其在s1，固定a1、x2、φ2而变动B-only digits的a2，物理终点完全相同，原管的y斜率e2v(x2)也相同，但φ1有多值。若把所有这些访问同时当成一个terminal selected point的原兼容incidences，则必须有同一ξ_terminal满足

    e2v=ξ_terminal+u(s1)φ1+Oδ,

这使φ1只在Oδ范围，不能保所有原B-only变化。这个显式冲突说明本校准**不能反驳完整source basicness**；它同时定位双time-output marginal之外仍需使用的terminal ξ联合约束。选一部分φ1并重新分配原weight会损mass，不能宣免费修复。

初time完整Y0 AD未构造，T joint4AD/CW也未保；不以κ=0 padding冒正κ反例。β像lower反例本身只作用§7 local claim，§8的两个marginal carrier检验只否少用条件的推理。全过程不把(3)的真实fullsource质量搬给这个三时toy。

## 10. 结论、失败分类与停止

真实原同管双时质量、长kernel fibre core与精确恢复均已写出；原KT用途实际排掉完整commonkernel的γ>1/2参数子范围，仍没有spec所需basicness/商lower或全正κ结论。此子范围依named19.4和完整source，不是将R70参数范围挪用；亦不认证新颖或重大。local dust否定仅由density/Lip推出ξ一维像lower或basicness；更强两terminal calibration仍不保terminal ξ全兼容，不能作fullsource反例。原whole联合责任仍open。

按预设关于‘只得κ+γ>1额外子范围而未付basicness’的停止标准，主机制仍归no-information toward selected target；真实子范围排除另如实记录，不以初等准备登记新ID/新颖/重大结果。冻结当前‘kernel response+两marginal恢复迫basicness’推断，不续digit参数、更多fixedtimes、Markov/BSG或goodrank公设。R71与R72连续两轮未达所选机制可用增益，R73必须先宏观审视，再选真正不同原联合机制；不能从本稿最后公式直接继续小修。

ordinary初始化、其余matrix/mixed、general-to-sticky/Hausdorff均未解决。文献作者声明、本项目内部审查及外部同行评审层次分开，Goal active。A/B formal及root整合审读后再定最终记录；source高级19.4等wholeproof仍具名。
