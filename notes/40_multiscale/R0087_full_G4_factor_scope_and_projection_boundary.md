# R0087：全G4的原质量归约、精确类闭包与投影边界

2026-10-18，root。全near-contained G4仍未证、未否。下面区分一项等价范围归约、旧输入应用和两个失败的具体桥；均不新立ID、方向或重大结果。未经外部同行评审。

## 1. 原完整命题与当前结论

G4的量词见research/rounds/R0087_working_spec.md：固定D,R,C,C0，任意δ依赖非零实degree≤D的P，原R5单位roundδ管轴whole metric-near Z(P)，原非负权W及δ角帽权α，可测阴影逐管density≥δ^η，问∀ε>0∃η,c,δ0使|E|≥cδ^(4+ε)W/α。没有physical/leading正则假设。下文没有证明这条全类结论。

条件于已存G3输入，§2–4严格证明完整G4与其中实不可约、real-dim4的情形在正幂量词上等价；§5的exact轴情形已由旧FSD001统一输入推得，不是另一新方向。剩余不能只改名为‘不可约G4’再续同门。

## 2. 近零集并的原marks时间分配

实因式分解P=c∏Q_j^(m_j)，非空实零集因子数J≤D，重数不改Z(P)。对每个原label和j，设B_ij={t∈[−1/2,1/2]:dist(a_i+t v_i,Z(Q_j))≤Cδ}。其存在量词公式为∃z，Q_j(z)=0且|z−a_i−t v_i|²≤C²δ²。标准实闭域QE给一维集合统一有限个区间/点，格式常数只依D和固定维度，不依系数或δ。取所有端点的共同细分，并给每个开区间指定一个包含它的j；这些区间覆盖clock除有限端点，不要求一个因子包含整根原轴。

令λ=δ^η、η<1。roundtube两个球帽的总体积O(δ⁵)=O(δ Vδ)，小δ时每管先删帽仍保≥λVδ/2。body的正交clock横截面≤Cδ⁴，有限端点没有5D质量。每label可选一条assigned interval，保原marks≥c_Dλδ⁴，其长度ℓ_i≥c_Dλ。取dyadic r_i≤ℓ_i<2r_i；区间可用首尾两条长度r_i、仍含于原区间的子段覆盖，取marks较多者。新轴长恰r_i，whole近某Q_j，保同一原点集合Y_i′且|Y_i′|≥cλδ⁴。

## 3. 共同尺度、空间重叠与可调用的逐管密度

r_i∈[cλ,1]仅O(log(2/λ))层。按原权选一层r，保W_r≥W/O(log(2/λ))，而每剩余label已各自保上述marks。按片轴中点所在的半开r格和指定factor分组。所有E_g=∪Y_i′都含于原E，且支持在相应格的固定倍放大中；这些支持的重叠≤C_D，故Σ_g|E_g|≤C_D|E|，不付r^−5个格数。

每组以格中心作x=c_g+r x′，h=δ/r。每新轴长恰1、round半径h、位置落固定球B_R′，whole近变换后的非零不可约Q_j(c_g+r x′)。系数可再归一，零集不变。新实际tube体积≈h⁴，保留marks体积≥cλδ⁴r^−5，所以新density≥cλ/r≥cλ。若所调用近full输入的门槛为h^η0，取η<min(η0/4,1/4)，由r≥cδ^η给h≤Cδ^(1−η)，固定常数可由δ0余量吸收，故cδ^η≥h^η0。δ0还保证h在输入的小尺度范围。

## 4. 原方向帽、回尺度及双向范围

方向没有改变，但h帽比原δ帽大。S4维数4的角帽覆盖给α_h≤Cα(h/δ)^4=Cαr^−4，按原权计全部重复labels。若对每个实不可约4维Q已经有G4(σ)，并对低维因子使用现成G3，则缩放后可用同一个nearfull门槛η0，回原得

    |E_g|≥c r^5 h^(4+σ)W_g/α_h
          ≥c δ^(4+σ)r^(5−σ)W_g/α.

低实维因子的Z(Q)截到固定略大球，格式统一且dim≤3，R60全G3的λ³界在nearfull门槛下给所需相同形式；其高级输入仍具名。取σ=min(ε/4,1/4)，η<min(η0/4,1/4,ε/40)，则r≥cδ^η和一个log层费用可吸入ε，Σ_gW_g=W_r，得到原G4。degree1同样是flat DIR4已付应用。反向all-P显然包含不可约4维类，因此这只是等价范围缩减，不能新登记为另一研究方向。

平均版独立付：若λ_av≥δ^η_av，取density≥λ_av/2的原labels，原权至少λ_avW/2，α不归一且继承。以ε/2版本的逐管命题，选η_av≤η_per/2并小于ε/4，吸λ_av权损后得ε版。任意再次删marks须重算density；没有保原W/I不变或全λ强型声明。完整G4含flat P=x5，仍可反推旧DIR4 nearfull正幂输入，即使全转移成功也不能冒新的普通维数界。

## 5. exact轴只是旧FSD的统一再调用

若原轴exact contained于Z(P)，P_d(v_i)=0。P_d非零齐次，Σ={P_d=0}∩S4是固定degree的proper代数方向集。有限固定stereographic charts把它映成R4里非零degree≤2D多项式的零集；若numerator在chart恒零，则P_d在球面开集恒零进而齐次P_d恒零，矛盾。chart正反导数在选定紧patch有统一界。

对一个r角帽、δ≤r≤1，Wongkew1993 Main Theorem在R4、半径Cr球和厚度Cδ给volume≤C_Dδr³（更高次δ^jr^(4−j)均由δ≤r吸收）。δ分离方向周围不交小4球在这个tube邻域里，故Σ∩该r帽可由≤C_D(r/δ)^3个δ帽覆盖。原帽权α遂给weighted 3-Katz–Tao上界C_Dα(r/δ)^3，不依leading系数最小值或奇异点。

这恰是R29 FSD001已经统一允许的s=3输入。先有限着色δ角bins使不同bin代表分离，每bin按w_i/(Cα)抽原label，再用共同δ随机格：每label有≥cλ/δ真实点的概率≥cλ；rich labels用FSD的已有λ²有限下界，期望给保守|E|≥cδ^(4+σ)λ³W/[αlog(2/δ)]，近full阈值取η足小即为exact版G4。真实格的E计数期望恰δ^−5|E|，不以NδE代体积；低权或重合labels都保原抽样账本。这是旧全称输入的直接应用，不以重新搭物理分层证明而新注册。它没有说明near轴方向在Σ的Oδ邻域。

## 6. 两个严格失败接口不反G4

B完整验证的Pδ=(x5²−e x1)/(1+e)，e=δ^A，A>2，是实不可约、Sing为空。x1∈[1,2]的单位水平轴whole近其零集，距离≤√(2e)≪δ；近轴最近零点的梯度O(√e)。令A任大可否任何预先固定δ^c绝对梯度floor，故不能以远离Sing免费授regular-leading或physical-gradient门。

另一实不可约曲面Pδ=(x5−e|x′|²)/(1+4e)，A>1、physical梯度≥c。其exact affine line的t²系数迫v′=0，再t系数迫v5=0，所以没有任何非恒定exactline。却有S3水平δ-net的N≈δ^−3条单位轴whole近Z(Pδ)、full原marks、角帽权O1、实际union≈δ。原P2零方向只有±e5，水平原方向距它固定常数，故任何δ^θ snap到原exact-Fano或原leadingzero的桥均失败。这不反G4：其要求的lower只有δ^(1+ε)，且换成低degree平面x5可描述这个例子；本轮未证明一般合法低degree替换。不能据这两个specific例子否定全部分解/packet方法。

## 7. 泛投影所得与真实HRZ范围

A检验的R60多数投影/同π全局Lip图方法可推广到物理dim4，统一处理奇点及任意δ系数，保常数原whole-volume与marks、非短projection和实际normalfiber≤Cδ。原方向分离/KR对lifted凸测试给projected indexed absolute-CW上界；同一个查询也给固定格式半代数U的whole-shadow包含计数Σ_(S_i⊂U)w_i≤Cασδ^(-3−σ)|U|，因为H_j∩π^−1U格式固定、体积≤Cδ|U|且承载原管常数体积。这个wholecontainment不授partial-fraction PW4，也不允许U的复杂度随管数增长；是原查询的旧闭包。不能从中读出每个全局projected δ方向帽权≤Cα。任意CW4 nearfull估计甚至有既有quadric障碍；附加fullPW4亦不是已付DIR4的替代接口。原代数graph与原方向的额外兼容性尚未化成可调用增益，不加desired angular公设。

若某个实际全局Lip graph上的投影轴另whole近固定格式3fold，可用半代数McShane延拓把该3fold lift成dim≤3 carrier，再用旧G3/marked-only nearfull处理相应原marks；但这是假定了真实低维集中后的合法调用，不是已经从原G4输入抽出了足够集中质量。没有完整递归/分解账本，不能宣G4通过。

root实际再读HRZ v1原Theorem4.1/Prop4.2完整proof(27)及e(p,n,k)=(n−k+1)p−(n−k+2)，和§8原(51)–(53)/nested计数。n5下旧Bourgain–Guth窄转线性对k≥3要求p≥4/3，不能由替一个terminal就授dim>4所需p<4/3；k2仍欠其它真实terminal。近fullG4量词本身也非全λ的sharp强L4/3。局部ρ轴归一、原α_h/absolutePW和parent重复都须重付。这些是已有HRZ范围的实际复核，非新的否定所有方法定理。

## 8. 审查、全目标与停止

当前完整G4既无证明亦无反例；已付的是factor时间分配/原marks/尺度/角权的等价缩减，exact版的旧输入闭包，和specific免费桥的连续反攻。A8/B10及本root8实际全文互审后才可归档内部reviewed，外部高级输入仍具名，非外部同行评审。

macro/next保持ordinaryjoint初始化、directHRZ、sticky完整κ、真全方向counter四主路。当前无qualified新gain，保守no-newordinary/fullbranchsaving streak10。停止本次generic physical graph/CW4接法，不续irreducible重命名、低degree/κ/λ/D或另一个quadric模板。若将来重开fullG4，必须有真正的新原位置—方向耦合机制及完整质量证明；不能因尚未解决便标Goal blocked或降低完成标准。
