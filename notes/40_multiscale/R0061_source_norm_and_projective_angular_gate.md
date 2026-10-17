> R0062范围更新：本文Σ子类保持；当时未付的U4→fullgate逆向现由 notes/40_multiscale/R0062_finite_Nikodym_transfer_and_PW_responsibility.md 延轴/真实far-slice构造支付。三种gain表述同一主要障碍，未证明共同gain。

# R0061：真实范数饱和与低复杂度直线参数的射影方向恢复

2026-10-18，root整合。Goal active。working_spec先写、phase I失败后正式§7转题。以下区分旧输入的闭包、真实负向校准、经独立审查的受限几何结论和一般未证门槛。未经外部同行评审；不认证新颖性、重大性或高维猜想完成。

## 1. 完整目标及本轮改变

最终仍为ordinary Euclidean n≥5/general Hausdorff Kakeya或经文献比对的重大中间结果。R60已付整轴近三维半代数载体的全密度立方估计；它是否改善真实HRZ递推，必须把原absolute PW常数、局部长ρ、parent重复及maxleaf同时带入。该接法在本轮失败，不能仅将其对偶范数改名登记。随后检验真正保持直线的有界projective方向恢复，得到下面的固定格式参数载体子类，未解一般PW4族。

## 2. 全密度估计的强范数闭包

取原unitδ管整轴近固定格式realdim≤3载体，原非负权wi，总W；absolute PW常数Kp按R60§12定义。对全部可测F，令f=Σwi1_Ti、λF=∫Ff/(VδW)。R60给

    |F|≥c_a δ^(n−1+a) λF³ W/Kp，
    ∫Ff≤A|F|^(1/3)， A=C_a δ^[2(n−1)/3−a/3]Kp^(1/3)W^(2/3)。

共同实际tube体积Vδ≈δ^(n−1)，不把roundcaps常数写成精确幂。故μ(t)=|{f>t}|≤(A/t)^(3/2)。support在固定体积V0区域，且f≤W。以t0=A/V0^(2/3)分层，

    ∫f^(3/2)≤A^(3/2)[1+(3/2)log_+(W/t0)]。

whole-ball PW测试给W/Kp≤Cδ^(1−n)，因此正log≤C_a log(2/δ)，与最小权、权跨度及#index无关。先取a足小、再吸收log：对每ε>0，

    ∫f^(3/2)≤Cε δ^(n−1−ε)Kp^(1/2)W。             (1)

W=0平凡；t0≥W时直接低层估计。这是R60全λ的合法闭包，不新数学ID。

## 3. 真实长ρ终端和source接口

原unitδ管的长cρ pieces归一至h=δ/ρ。新测试比例a对应原比例cρa，原KR计数实际给Kp≤Cσδ_orig^−σρ^(1−n)。乘Jacobianρ^n后(1)为

    ∫Fρ^(3/2)≤C δ^(n−1−ε−σ/2)ρ^[(3−n)/2+ε]W；
    n=5时≤δ^(4−o(1))ρ^−1W。                      (2)

HRZ v1 alg2(45)、§8(51)–(56)的真实终端取p_m=m/(m−1)，故m3恰为3/2。旧tiny上界主幂δ⁵W_O^(3/2)，而PW最大W_O≈δ^−2ρ^−2处与(2)相同。source的ρ∈[cδ,δ^(1−ε°)]及δ^±O(ε°)只能给可调小幂；不能据此声有独立于ε°的fixed saving，也不作同常数的严格old≤new比较。

(51)控制Σ_O W_O，(52)控制max_O W_O，(53)同时调用二者；更高维parents的D_i费用和重复entries都保留。新linear-W写法带着ρ/Kp，不能在求和时把这些系数置1。更强nested maxcount只使旧证书更小，不免费改进新界。

## 4. 真实平坦饱和族及停止范围

R5取H3={x4=x5=0}，原unit轴过0，方向v=(sqrt(1−|α|²−|β|²),α,β)，α为固定二维box的Lδ网，β为宽cδ/ρ的二维Lδ网。原物理方向δ分离，N≈δ^−2ρ^−2，中心长cρ pieces整轴近H3且切向。所有pieces含B_cδ，所以

    ∫Fρ^(3/2)≥cδ⁵N^(3/2)=cδ²ρ^−3= cδ⁴ρ^−1N。

壳层积分上界同幂乘1+log(ρ/δ)。同族可取H3⊂H4、δ3≈δ4≈ρ，饱和原nested允许计数。它否定的是仅替raw强范数就自动改善最坏终端的步骤；没有证明每个global HRZ运行必选此leaf，没有否定整个算法或ordinary Kakeya。按spec停止Lp/ρ/D/p插值，不以这项闭包结案。

## 5. 一般projective门槛与精确全类边界

spec§7的完整候选：任意ε>0能否取η>0，使bounded R4原unitδ族、N∈[δ^−3+η,δ^−3−η]、原可测Yi平均≥δ^η及全部固定格式测试的absolute PW

    #{i:|Ti∩H|≥a|Ti|}≤C_D δ^−3−η |H|a^−4，a≥δ， (3)

可经固定数、uniform pole-margin/biLip的projective maps保δ^ε原incidence，且每map新δ角帽含原labels≤δ^−ε？maps允许依配置和δ。此完整候选未证明，也未被反例否定。

任意共同域含0的projective F=(Ax+b)/(1+a·x)都恰为b+L F_a，L=A−baᵀ=DF(0)，F_a=x/(1+a·x)。uniform biLip给L及逆固定界，故F_a涵盖全类的非仿射责任。原支持线p+tv的方向变为

    q_a=(1+a·p)v−(a·v)p，                         (4)

与p沿线选择无关。若a·v≠0，q_a平行远超平面H_a={1+a·x=0}上的交点X=p−(1+a·p)v/(a·v)。无假设时只可说visual angular bins；Euclidean δ-point bins固定可比还需|a·v|固定下界。a·v=0保原方向。不能免费丢掉近切向质量，或以某一个预定map的失败反驳adaptive候选。

## 6. 可证明子类的完整量词

固定R、参数近邻常数C、半代数格式A。存在固定C_A,c_A,J，使任意足小η>0、足小δ满足下述结论。除(3)、N范围和平均密度假设外，在固定数bounded-slope原方向charts内，假定每原支持线的参数p_i=(b_i,u_i)∈R³×R³，线为(x,t)=(b_i+t u_i,t)，到某bounded、格式≤A、realdim≤3的Σδ距离≤Cδ。允许Σδ任意δ系数、奇点、边界、非闭及重复原labels。

则可选一个chart、一个固定有限列表中的clock-projective map以及原label子族，保至少c_A原incidence；在该map的新每个C0δ角帽中，原label数至多C_A δ^−C_Aη。所有实际Yi随map保留，仅按原label删选；没有新增角分离假设。取η≪ε/C_A、δ0吸收固定常数，即得到§5所要求的δ^ε保存和δ^−ε帽计数的**这一子类**。

该参数载体是额外真实几何假设，不由(3)自动提供。不是所有N≈δ^−3有限点都可免费装进固定格式Σδ；degree/格式不得随δ无界增长。结论不宣一般PW4或高维维数改善。

## 7. 原质量与chart选择

按有限bounded-slope方向charts分原labels，选incidence I_c≥cI的一组。令Vδ为实际原共同tube体积，λ_c平均不先设逐管下界。只用|Yi|≤Vδ可知

    N_c≥I_c/Vδ≥cδ^ηN≥cδ^−3+2η。                (5)

不能仍给该chart原δ^−3+η下界。其absolute PW上界由原restriction继承，常数不恶化。全轴clock在固定[-R′,R′]内，参数bounded；轮换坐标为刚性变换，不缩原unitclock。以下每项bad-label成本相对原I计算，避免把平均密度免费换逐管密度。

## 8. 固定格式体积工具与δ系数一致性

Σ取闭包，bounded区域稍加固定margin，格式仍统一。用固定格式C¹分层。Cauchy–Crofton加一般仿射切片的uniform finite semialgebraic fiber bound，给所有三维层H³之和≤C_A；低维层不以三维体积冒正质量。

任意bounded固定格式半代数A0⊂R4有

    |N_r A0|≤|A0|+C_A r，0<r<1。                 (6)

证明：闭包不改4-volume；N_r闭包在其内部之外的点离边界≤r。QE后边界包含于固定数、统一degree的非零多项式零集之并；删去恒零多项式。Wongkew1993 Main Theorem在n4/codim1给这些零集在固定球内的r-neighborhood volume≤C_A r。若像只有≤3维，其4-volume为0，同样适用。此处依赖的是**固定格式**；“dim≤3”对任意集合不能代替它。

新原件 literature/primary/wongkew_1993_tubular_neighbourhoods.pdf，PDF3/印刷178的定理实际render/read；全文深层证明仍具名，不称独立重证。标准分层/QE/Crofton与Paw regular cells也明确作为输入。uniform bound仅依格式而非系数大小或δ，后面所有κ作额外实系数，不改degree。

## 9. 坏切空间的真实whole-tube收费

三维stratum每点取切空间正交frame (B;U)，B,U均3×3；定义

    D(p)=max_(|t|≤R′) |det(B+tU)|。

更换正交frame只改符号，D良定义；可用有限minors/QE表达，bad集合D≤κ格式统一。把全部≤2维strata归bad。考虑真直线扫出像

    A_bad={ (b+tu,t):p=(b,u)∈Σ_bad, |t|≤R′ }。

面积公式的4-Jacobian恰|det(B+tU)|：最后的clock列消去其空间u部分。自交只使像体积更小。故|A_bad|≤C_Aκ；低维层像体积0。有限每原label任选σ_i∈Σ距p_i≤Cδ，不需连续/可测最近点选择。若σ_i在bad，则整原unit轴和实体Ti都在N_C′δ A_bad。由(6)和原PW的a=1测试，

    N_bad≤C_A δ^−3−η (κ+δ)。                    (7)

这对真实原whole tubes计数，非形式tangent-plane toy。用(5)及I_c≥cI、|Yi|≤Vδ，

    I_bad/I_c≤C_A δ^−3η(κ+δ)。                   (8)

取κ=δ^(5η)、η<1/10，δ足小时只损O(δ^(2η))原incidence。nearest点在奇异层、good/bad邻域重叠、原参数误差δ均已被这一上界吸收；不重设原Yi或选新时间prior。

## 10. 有限clock值恢复good切空间的秩

取固定四个不同非零小c_j，使|c_j|R′<1/10。三次多项式的有限维norm等价给每个B,U

    max_j |det(U−c_jB)|≥c_R max_(|t|≤R′)|det(B+tU)|。

可直接由P(t)=det(B+tU)、Q(c)=det(U−cB)=(-c)^3P(-1/c)和四点插值验证；常数允许依这些固定c_j。令π_j(b,u)=u−c_jb。其operator norm固定有界，good点D>κ至少一个j的3-Jac≥cκ，从而smin(π_j|TΣ)≥cκ。选择一个j保good原incidence的固定比例。

对应真空间变换F_j(x,t)=(x,t)/(1+c_jt)有共同uniform pole margin和biLip界；原直线变为新斜率u−c_jb，仍真直线。这个有限列表依共同clock范围，非随机把自由点投影冒作方向。

## 11. 同π图形与角帽的原参数小球

在每j-good层，用目标coordinate minors、finite-to-one CAD及Paw regular-cell的准凸域分解，得到同一π_j上的有限global Lipschitz graphs。微分逆界为Cκ^−1，global bound可保守写K≤C_Aκ^−C_A；piece数/格式统一。κ作为实参数进入同一个固定公式；不能只说“每个κ有限”却让数量依δ任意增长。低维residual切空间继承原切空间上的逆界，递降补回边界，闭包保globalLip。

若某新C0δ角帽含一组实际参数p_i，则其新bounded slopes π_j(p_i)在Cδ球内。选定σ_i距p_i≤Cδ，故π_j(σ_i)也在C′δ球内。每个global graph上这些σ_i的直径≤C_Aδκ^−C_A；加回原参数误差后，全部p_i落在固定数半径

    r=C_A δ κ^−C_A                               (9)

的原joint参数球中。取η足小保证δ≤r≪1。这里保留全部同帽重复labels，不偷去重；global图形是解决跨分支/非凸域问题所需步骤，单纯局部inverse function theorem不足。

## 12. 从joint小球到原PW计数及原mark回传

若(b_i,u_i)在joint r球，则其整unit轴位于一个固定bounded长、半径Cr的直tube包络，实体Ti也在内；该原空间测试是固定格式，4-volume≤Cr³。原(3)以a=1给

    #cap≤C_A δ^−3−η r³≤C_A δ^−C_Aη。             (10)

有限graph并只付固定倍。故§6的方向恢复已由原PW支付，没有把probability Frostman或方向帽条件插入输入。

F_j对实际Yi的Jacobian上下固定有界，实际轴像长度也上下固定有界。按固定长度L0包络、有限clock pieces及一个共同固定homothety可转为unit tubes；可按实际incidence选piece，损固定倍。只承诺保留实际marks，未声标准unit延长的假端部自动满足全部新PW。应用四维方向分离/shading输入时可先在每角bin以最多δ^−C_Aη原labels收费取代表，或随机按原incidence抽样；angular separated调用不需要额外冒用新PW。四维来源的wholeproof责任仍具名，亦未在此据它宣高维维数结论。

## 13. 仿射三平面校准

若Σ是bounded affine3-plane，写p=p0+(B;U)z、frame正交，z bounded。原whole sweep的δ-neighborhood volume≤C(max_t|det(B+tU)|+δ)，因每slice厚化体积≤C∏(s_i(B+tU)+δ)。直接PW迫detmax≥cδ^(2η)（one-chart且原N下界），finitechart仅保incidence时为δ^(3η)。

某合法c给π_c参数逆Lip≤Cδ^−3η，故r=Cδ^(1−3η)，帽count≤Cδ^−10η；one-chart时δ^−7η。此子类甚至不需删bad labels，原marks全保至固定chart/piece费用。它独立校准一般Σ证明，不以平行族在identity下失败作反adaptive反例。

## 14. 合法删选、平均密度及双向蕴含排查

原label restriction保absolute PW upper和参数载体条件；进一步shading restriction必须重算I和平均λ。subclass结论对满足总质量下界的每个合法删选统一成立，未授任意极小子族仍有原N。平均→坏labels收费使用(8)，逐管δ^η假设没有添加；逐管版本只是更强输入的子情形。任意权若另有同权PW upper和W范围可同法收费，但本文不从unweighted PW免费推无限权版。

完整§5 gate经已存DIR003/SRC001可导相应近full PW4 shading增益；其反向并未证明。由union下界不能自动构造一个bounded projective map恢复角熵。因此不把完整gate与PW4猜想声称等价，也不因换名称登记新ID。§6在附加固定格式参数载体下给出实际选择构造，严格强于只对该子类重述一个union下界；仍不能认作一般新数学结果或重大性。

## 15. 一手比对与独立审查

实际主比较：HRZ真实alg2和终端公式；KR方向分离→polynomial-Wolff原定理；OAI4§11.3已含任意方向与segment extension，不重包装该推论；Paw原regular-cell/任意RCF范围；Wongkew1993 MainThm原statement/PDF3。有限primary检索只用于区分restricted projection与自由Grassmann投影及已有PW4问题，不认证穷尽优先权。新保存1PDF/1source，合计51PDF/52sources。

A独立源范数/仿射及一般Σ正证，B独立层积分/flat饱和/全projective边界并逐步核Σ推广，root全文整合；两正式review及root整合文件记录最终版本。数学审查与archive字节/引用验证分开；未经外部同行评审。

## 16. 当前停止与下一真门槛

原norm直接替换冻结；一般projective候选保持open。本轮真实新增是固定格式≤3维直线参数子类的方向恢复，不是所有管族的结构定理。下一应在完整PW4类中，证明或反驳能保原shading质量的固定复杂度参数结构提取；先核restriction闭包及与旧全称gain的双向关系。若该提取由旧命题统一重调用即等价，不另起名字登记。不得只推广affine常数/再证同π lemma或把任意有限点补成高degreeΣ。ordinary n≥5/general、四维颗粒、general→sticky与major目标未解，Goal active。
