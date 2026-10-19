# R0102：全局双端码、原rich fibres与受限投影

2026-10-19，root，按working5锁后施工。与R76选出的单code块不同，本轮保留δ^o(1)原全T质量和所有code块；从原第三点的pencil取得同一P的实际受限small projections。具名CSWZ定理排除其真实方向满足spread-out输入的分支；没有从完整source证明该输入，未排完整κ1、ordinary或一般Kakeya。内部独审另存，未经外部同行评审，无newID/major/novelty声明。

## 1. 原数据、量词与损失顺序

采用WZ2609.22035v1 Def17.2–17.4的bounded d5/k=ell3、κ1完整配置及R76 det-large分支(1)。原N≈Kδ^-4、CW≤K；K=δ^-C0η，原Zδ-separated、m=|Z|≥K^-Cδ^-1，native Y_u为AD1，原E点数≤K^Cδ^-4，used point-pencils的Φ_p为AD1/slabγ且每δ角bin的原T重数O1。每条heavy T的原S_T≥K^-C m，访问点p_u(T)和原ξ事先固定。

取τ=δ^a、σ=δ^b，det-large分支可选原anchors t,s满足h=s−t、|h|≥σ、A=F_t−F_s且sminA≥σ，并有≥τδ^-4同T双访问。再取r=δ^c删第三clock锚窗。L≥2统一记录有限次K、τ^-1、σ^-1、r^-1和log(1/δ)费用；所有公式的L^C为固定次幂，不把a/b/c塞回原K。给任意小ℓ>0，先选a,b,c小、再η≪c并足小、δ最后小，可令本轮全部L^C≤δ^-ℓ。选择的det-large分支须真的有上述质量；不声称覆盖所有原source。

## 2. 不选单块的全局双端码

实际两端同T恒等式沿R76§3–4：p_t=(x,y+F_t x,t)、p_s=(x′,y′+F_s x′,s)，令

    C(T)=CL(p_t)=(U,V)=(y+A x, y+h ξ_(p_t)),
    CR(p_s)=(y′−h ξ_(p_s),y′−A x′),
    CL(p_t)=CR(p_s)+Oδ.                              (1)

固定一个δ-cell offset保固定比例边；左右codecell此后配对唯一。双侧weighted-degree peeling阈值D_0≥L^-Cδ^-1，保≥L^-Cδ^-4原T；每个固定(p_t,p_s)原T重数≤Cσ^-4。每个非空块两侧各至少D_0/(Cσ^-4)个端点，原两侧点总数≤K^Cδ^-3，所以非空codecell总数≤L^Cδ^-2。记保留管族H_0及其code support P_0；

    |H_0|≥L^-Cδ^-4,   |P_0|≤L^Cδ^-2.              (2)

这里停在选‘最大一个块’之前，也没有做单块的joint residual桶。故仍有原全T的δ^o(1)比例，而非R76最终H*/N≈δ²。每T全部原S_T均保留；H_0不是重新归一后免费完整Def17配置。

## 3. 真正二维的全局code概率上界

设一个code ball B_ρ⊂R4，δ≤ρ≤1。只用其首U约束：固定原y∈Y_t后，U=y+A x∈该球迫x落在半径Cρ/σ二维球。二维δ-packing及|Y_t|≤K^Cδ^-1给这样的原p_t至多CK^Cσ^-2ρ²δ^-3；每p_t的used管数≤CK^Cδ^-1。因此

    #{T∈H_0:C(T)∈B_ρ}≤L^Cρ²δ^-4,
    μ_0(B_ρ)≤L^Cρ²,   μ_0=|H_0|^-1Σ_T δ_(C(T)).  (3)

codecell中心与精确C(T)只差Oδ，扩大球固定倍即可。ρ/σ>1时用trivial二维packing也服从显示upper；ρ≥δ未调用更细AD。此结论不用ξ_p的正则性或q-offset2Fst，也不要求全局code law的AD lower；原point角degree upper不能用全部未选择穿点管代替。

## 4. Code权层与同一个uniform P

令w(Q)为H_0在codecell Q的实际T数。w∈[1,Cδ^-4]，按二幂值分O(log1/δ)层，选保至少1/log管数的一层。记H为其原T、P为其codecell中心，N_H=|H|。存在整数w≥1使各Q∈P有w≤w(Q)<2w，且

    N_H≥L^-Cδ^-4,   L^-Cδ^-2≤|P|≤L^Cδ^-2,
    |P∩B_ρ|/|P|≤L^Cρ².                            (4)

证明：保量lower直接由层选择；conditioned μ_H的(3)只再损log，uniform P law与μ_H在2倍内可比。取ρ=δ得每code atom≤L^Cδ²，因而|P|≥L^-Cδ^-2；upper沿(2)。每T继续保全部S_T，这不是只挑一套后验点law。code范围O1，有界固定平移/缩放可置[0,1]^4；后面另付chart旋转/regrid固定倍，不改变指数。

## 5. 第三点恒等式与满秩二维plane

在原访问p=(x,y+F_u x,u)，令φ为该T的原前两slope。用同T在u和anchors的斜率一致性，展开(1)得

    C(T)=Γ_p+G_u φ+Oδ,
    Γ_p=(y+(F_u−F_s)x+(t−u)ξ_p,
         y+(F_u−F_t)x+(s−u)ξ_p),
    G_u=((t−u)(F_u−F_s); (s−u)(F_u−F_t)).          (5)

例如左首码展开为y+(Fu−Fs)x+(t−u)ξ_p+(t−u)(Fu−Fs)φ；右末码同理，未将每点ξ换成独立变量。所有直接系数bounded，Oδ不含A^-1，因此无需R76单块fine residual修复。这里w/native y随原p改变，未把一个见证强加给整个乘积。

在far clocks |u−t|,|u−s|≥r，G_1/(t−u)−G_2/(s−u)=A；故对每v∈R²，σ|v|≤2r^-1|G_uv|，

    smin(G_u)≥rσ/2,
    V_u=im G_u∈Gr(4,2).                            (6)

每个p上的实际codes位于Γ_p+V_u的Cδ邻域。V_u按u可变，但在固定u，所有p的planes平行；这是后续计数的关键。

## 6. Far clock与point-heavy的原质量预算

先对每T∈H删其S_T中距anchors小于r的times。至多删C(r/δ+1)，相对原|S_T|≤K^C(r+δ)，η≪c、δ足小即逐管保至少一半。记原far访问总数I_f≥L^-C N_H m≥L^-Cδ^-5。

在所有原p∈E上按H的实际far visits定义degree，阈值D=I_f/(2|E|)≥L^-Cδ^-1。删degree<D的点访问至多I_f/2。此后仅宣平均保量，不向每T赠新的逐管lower。固定u每T至多一个原访问，记I_u为留在heavy p的T数，Σ_u I_u≥I_f/2、I_u≤N_H。

取U={u:I_u≥I_f/(4m)}，则

    |U|≥L^-C m,   I_u≥L^-C N_H (u∈U).             (7)

这是实际第三clock的保量集合，未以独立u参考law代selected marks。各留heavy p仍有至少D条原T；方向仅是原Φ_p的一个子集，不能声保完整Φ或AD lower。

## 7. 每个heavy p上的实际rich code fibre

固定far u、heavy p。若两条原T的code落同一δ-cell，(5)–(6)使其φ相差≤Cδ/(rσ)。原Φ_p的AD1 upper及每φ δ-bin的O1原T重数给一个codecell容纳至多CK^C/(rσ)条原T（半径超过1时用trivial bound，亦由L吸收；选c+b<1可保持fine范围）。因此该p访问至少

    R_0≥L^-Cδ^-1                                  (8)

个不同P-cells，均在Γ_p+V_u的Cδ邻域。此处用的是实际保留方向数D和upper，多删选不会产生新lower。没有要求q_p=Π_(V_u⊥)Γ_p的分布为2Fst，也没有要求p→q_p可逆。

固定u，按q_p所在的δ-output cells分组。每个active q-cell选一个heavy p，其R_0个codes都投影到该cell的固定邻接；每个code投影只落固定数量邻接cells。故active outputcell数≤C|P|/R_0≤L^Cδ^-1。若P_u为在u留heavy visits的所有codecells，Σcell管数<2w及(7)给

    |P_u|≥I_u/(2w)≥L^-C|P|,
    |Π_(V_u⊥)(P_u)|_δ≤L^Cδ^-1  (u∈U).             (9)

q-cells分组不独立化原T；p可以共享codes，邻接bounded overlap已经付。式(9)同时用全局P的二维cardinality和每point的一维rich slice，是R79单block模型未具的完整point-pencil输入。

## 8. Bounded chart、参数重复与实际一手输入

采用库存CSWZ2610.13682v1 Def1.4–1.5/Th1.7，root actual本地PDF4–6对应全文及HTML读取；A另核§2与§3.16。其高级wholeproof仍具名。以固定有限小Grassmann charts覆盖V_u⊥，至少一个chart含≥L^-C m个原U时刻。做该chart的固定正交code变换及固定平移/缩放，再δ-grid化P；每cell合并数O1，(4)/(9)只付固定因子。小chart可使参数θ(u)∈[-1/2,1/2]^(2×2)，留出dyadic cell位于literal[-1,1]^4的margin。它代表normal plane V_u⊥，π_θ(x,y)=x+θy，kernel为V_u。π_θ与orthogonal projection之间的output变换及逆均固定有界。

定义Θ_rich为这个chart内由u∈U实际实现的不同δ-parameter cells。每cell只需选一个实际rich u代表；其P_u可以不同。重复times不当不同θ计数，亦不凭|U|大赠|Θ_rich|大。将参数换到cell角点会使bounded P上输出移Oδ，(9)upper仍只固定倍。

Th1.7的准确强度：给s∈(0,1]、point exponent t=2和outputlossα=1/4，有ε_*>0，使(δ,s,δ^-ε_*)_(4,2)-spread-out的非空Θ上，同一个(δ,2,δ^-ε_*)-Frostman P存在占≥1−δ^ε_*的good θ，且对每个|P′|≥δ^ε_*|P|都有|π_θ P′|δ≥δ^-7/4。这是all-large-subsets结论；P_u随u变合法。源§3.16甚至按cell中‘存在一个实际代表及大子集使像小’定义bad cell，不需要cell所有times都rich。

## 9. 真正付清的条件SPREAD排除

先固定s和上述ε_*，再选本轮a/b/c/η，使所有损失L^C≤δ^-ℓ，0<ℓ<min(ε_*/10,1/10)。则P为所需Frostman，任一rich代表P_u≥δ^ε_*|P|，而其像≤δ^-1-ℓ<δ^-7/4（δ足小）。于是Θ_rich中每个cell都是bad。

因此：**Θ_rich不含任何满足上述small-loss spread-out输入的非空子族。** 若有这样的Θ⊂Θ_rich，则Th1.7给至少一个good θ，与该cell实际rich代表的(9)矛盾。这是从完整source的det-large原分支得出的真实必要退化，不是假设q2Fst之后的推论，也没有仅保δ²单block质量。

本表述不须把good参数比例搬回u，因为每个被考虑cell已有一个rich代表并且全部bad。若改为只假‘全部原times的pushforward law spread-out’，再试图用bad δ^ε比例控制|U|或I_u，则必须另付权重、重复cell、合法restriction/归一及源Lemma2.7/2.11等；本轮不免费作此升级。原全time族是否spread-out、是否可抽出合格子族，仍是实质未付输入。

## 10. 新plane族与旧结构障碍的区别及反攻

R76直接projection用的是固定root point-law上的K_s⊂R6/normal4planes，θ=(A^-1;h^-1I2)有结构零项，故universal Schubert障碍。本轮点law换为原多块Ccode law⊂R4，kernel V_u=imG_u是另一对象。固定far u，若Fu−Fs可逆，graph slope

    Z_u=q(F_u−F_t)(F_u−F_s)^-1, q=(s−u)/(t−u),
    F_u=(Z_u−qI)^-1(Z_u F_s−qF_t).                 (10)

在可逆域是实际局部双向公式；例如t=−1/2,s=1/2,u=0、Ft=I/2,Fs=−I/2,Fu=0处各分母可逆，Fu小扰动使Z取Grassmann开chart。这里Z是kernel G的下block-over上block graph，不是第8节的normal/projection参数θ；固定交换两个code blocks后可取π_θ kernel参数θ=−Z，符号与对偶不能混。SPREAD始终在最终fixed bounded chart直接作假设，不凭任意bilipschitz坐标变换宣不变。故不存在由此公式对所有Fu强制的一张固定Schubert超曲面；不能沿旧零项直接拒绝。此仅coefficient资格测试，不构造完整WZ配置，也不证明某条原time曲线spread-out。

反之取标量仿射Fu=uI，则G_1=G_2=−(u−t)(u−s)I，V_u恒定，任何大子时钟族也不自动spread-out。该coefficient例本已在旧scalar source机制处理，不保完整κ1 source，不是其反例。一般rough F的timeAD、SM或rank2均不单独赠局部spread-out；R97特定Segre参数模型的局部障碍也不能未经实际map核对移植到(10)。

## 11. 删选闭包、旧等价排重及保留缺口

code层为whole-index选择，保原T全部S_T及其逐管lower；far先逐管半保，point-heavy后只平均保量。每一步仍以原N/I/m分母记，CW绝对count继承、归一常数至多按N/N_H损L，不声新完整Def17 lower。第三点codes的φ upper和rich degree不同责任；没有在nativeY-only图中补point-pencil。

R44共同tests/PW体积、R45 selected KBL及R78–80单块common-X/action均没有自动提供本轮全局P2Fst和原point-rich restricted projections；若仅回那些结论不新立方向。CP/PM全称gain等价冻结也不解冻：本轮是不同实际family在明确SPREAD输入下的具名定理应用，不是对任意旧CP对象宣新全称正gain。反向由抽象P、planes、P_u重建full T/CW/Y/X/Φ仍未证；(10)开chart不作该反向构造。

真正新增的是原多块sameT质量→同一2Fst码集→actual各u的大子集一维投影，再以具名工具得必要nonspread退化。完整rough族及rank-singular分支、SPREAD失败的几何分类/恢复、ordinary到sticky与ambient Hausdorff返回均未付，不能称完整κ1排除。

## 12. 审查、停止与宏观接口

无数值计算代连续证明；本轮是有限δ原配置的符号计数及具名投影应用。独立审查须全文核(2)多块保量、(3)原degree upper、code权层、far与平均/逐管区别、(5)符号、rich fibre碰撞及(9)output计数、chart/重复参数和Th1.7量词。源45页高级wholeproof未从零独证，内部应用不替外部同行评审。

若上述链通过，仅登记真实条件SPREAD source应用/必要退化，不newID/major/novelty、无ordinary或完整rough saving。按working停止r/σ/ε参数续轮；后继若处理nonspread须给真实原质量的不同机制，不把spreadout、公用offsetlaw或逆分类公设化。完整Goal保持active，宏观/归档/Git同SHA/fulltree另核。
