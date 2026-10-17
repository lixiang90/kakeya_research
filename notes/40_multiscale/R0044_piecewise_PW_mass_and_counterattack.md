# R0044：ruled-grain分片的原质量、重数及clock费用

2026-10-17，lifting_obstructions。读固定入口/context、R43证明与nextspec；本轮只攻击actual多项式测试的质量接口，不另开代理、不Git。长期目标仍高维Kakeya。下文证明原权求和式、真实直管的assignment损失及polynomial-offset访问数；明确它们不能构成完整positive-κ source反例，也没有给出五维增益。未经外部同行评审，不宣新颖/重大。

## 1. 当前实际命题与独立停止条件

同一physical R5内，有限whole-tube probability ν满足R43的PW，常数C0，presentation费用P(E)=(1+E)^A。实际候选tests为

    S_j={t∈J_j, x∈Q_j, |y−P_j(t)x−h_j(t)|≤e_j},

x,y各R²。每个S_j是固定测试，不可对每条tube另选h_j而仍用同一个PW事件。选原tube事件H_j或原权fraction θ_j(i)∈[0,1]，a_j=∫θ_jdν。记

    M_j=∫θ_j(i) q_i(S_j)dν(i),
    M=Σ_j M_j,   A_tot=Σ_j a_j,
    V_P=Σ_j P(E_j)|S_j|.                             (1)

若同一点可被多个S_j覆盖，M可能重复计费；必须从真实marks给M lower，另核pointwise overlap或使用合法partition。即使S_j两两不交，也不能自动A_tot≤1：一根whole tube可在不同时间访问多个pieces。当前缺口是保实际marked mass的同时，A_tot和degree/clock费用是否真能留出strict κ saving。

独立反攻：原index分配与time-dependent分配混用；将pointprior当tube law；短clock免费归一；P只在稀疏times近似却把whole-J range当有界；高degree或moving h_j的自由参数被省略。若仅得到条件预算，或所有实际费用吃尽余量，就停止该测试，不把预算不等式登记为新高维定理。

## 2. 原PW的分片求和：精确重数为A_tot

对每个j，θ_jν是被原ν支配、总质量a_j的submeasure。其q_i(S_j) tail≤min(a_j,C0P(E_j)|S_j|s^(−5))。R43的layer cake逐式给

    M_j≤(5/4)[C0P(E_j)|S_j|]^(1/5)a_j^(4/5).

对有限j求和，Hölder(5,5/4)给

    M≤(5/4)(C0V_P)^(1/5) A_tot^(4/5),
    M^5≤(5/4)^5 C0 V_P A_tot^4.                      (2)

该式对相关H_j、任意原权和fractional assignment都成立；没有把不同j的laws独立化。a_j=0项直接删去。若M=0亦平凡。

可在逐项上界中使用已知q_i(S_j)≤q_j，得M_j≤a_jq_j，但这不是把a_j改成q_ja_j后仍使用同一PW常数的许可。也可保留未作Hölder的Σ[P(E_j)|S_j|]^(1/5)a_j^(4/5)；它能利用真实不均匀性，却不能无条件删去重数。

## 3. 严格的原law校准：assignment确实丢访问密度

取δ dyadic，δ≤e/100，e dyadic。令ν为下列真实vertical graph δ-tubes的uniform counting probability，clock为[0,1]：

    T_b={(b+v,t): |v|≤δ, 0≤t≤1},
    b=(x1,x2,y1,y2)∈δZ⁴∩([1/2,1)×[0,1)³).

固定bounded parameter chart中，该族joint4-AD常数O(1)：slope恒0，intercepts是四维规则网；每occupied dyadic parent的计数在常数倍(ρ/δ)^4内。所有截面仅有O(1)重叠，uniform visit law的Lebesgue density≤C。因此任意可测S有∫q_i(S)dν≤C|S|，进一步给PW tail≤C|S|λ^(−1)≤C|S|λ^(−5)。对whole-tube containment也有ν{T⊂U}≤C|U|，故CW常数O(1)，不是只检查ball cap。全管shading为1-dense。

取P(t)=diag(t,0)，沿axis的真实native offset为

    H_b(t)=(y1−t x1,y2).

将offset R²分为半开e-squares Q_j，取足够大的固定x-box及所有会被上述T_b命中的Q_j，测试

    S_j={0≤t≤1, x∈Q_x, y−P(t)x∈Q_j}.

S_j在各time的offset坐标中两两不交，其并覆盖整个管族，所以Σ_j q_b(S_j)=1。任意具体横向点v满足x1+v1≥0.49，第一offset坐标关于t的导数为−(x1+v1)，故它在一个长e的interval内停留≤3e。逐v积分便有q_b(S_j)≤3e。每根axis的offset第一坐标跨越≥1/2，至少命中c/e个格；截面扰动仅增加固定邻格。所以按访问定义H_j时A_tot≳e^(−1)，总M=1。

更强地，对任何原index fractional assignment θ_j(b)≥0、Σ_jθ_j(b)≤1，

    Σ_j∫θ_j(b)q_b(S_j)dν(b)≤3e.                      (3)

证明只需每根管上用max_j q_b(S_j)≤3e。故原tube只能选一个piece，或把单位原权分给pieces，无法同时保M≈1并声称A_tot≤1。随机选择j也受同一(3)约束。为支持time-dependent selection而复制(tube,time-block)为新indices，则已经改变law，须按下一节付clock费用。

本例保真实straight tubes、原uniform law、jointAD4/CW/PW、共同完整clock和平均density1；但union有常数量级、κ=0，且不满足positive-γ的实际slab/TubeKT等全部source条件。P还是原旧matrix-affine机制已覆盖的分支。它**只校准不可免费的assignment步骤**，不是新polynomial分支成果、positive-κ反例或Kakeya反例。

## 4. 时间切分不能把原tube质量改成incidence质量

若将clock切成interval J_j，长度q_j，定义normalized piece visit为q_i(S_j)/q_j，则原PW只推出

    q_j ν{q_i(S_j)/q_j≥λ}
       ≤C0 q_j^(−4)P(E_j)|S_j|λ^(−5).                (4)

左边把复制的新index质量赋q_jν；这时总index质量可为1，但常数出现q_j^(−4)。若先对whole pieces取原ν，不乘q_j，则是更大的q_j^(−5) tail费用。共同time normalization的准确式仍为C_new=C0 r^4/(p q^4)，不能因记号改动免除。

该q^(−4)有真实geometry校准：取δ≪q≤1，uniform δ-separated四维方向bush的whole tubes经过同一点，BS给原PW常数O(1)。取共同clock[0,q]，再仅time÷q；新unit-clock全族落在横宽O(q)的box内，测试整个box体积O(q^4)、每管占比1，迫PW常数≳q^(−4)。若q≪δ，box宽须写O(q+δ)，不能用此例声称q^(−4)的sharpness；一般tail公式(4)仍适用。同时spatial÷q当然可抵消，但必须将测试体积、管宽和frame同步改变；不是原physical测试下的免费优化。这个旧公式的校准亦不作新的positive-κ source counter。

另一种普遍“去重数”猜测也可严格排除：若对任意常复杂度piece partition都可把(2)的A_tot替成1且保原M，则真实方向-separated Kakeya tubes会得到正体积下界。取已入库FD–deLaSalle2607.14824v3 Thm1.3的compact零体积Kakeya set；在固定方向chart的有限δ网选原unit-segment witnesses，按有限clock buckets留常比例方向并归一化到同一固定clock，方向间隔只需初始扩大固定倍。所得N≳δ^(−4)、PW常数O(1)的真实管全在共同affine image的N_CδK内，其体积仍趋0。对凸U以固定复杂度的外John椭球测试，PW还给CW常数O(1)。将管并以δ-cubes partition，单piece复杂度恒定、M=1而Σ_j|S_j|→0，正与无重数的普遍版本矛盾。此论证只重用已核compact构造及BS输入，未假无限可测选线；不保证jointAD lower、positive κ或actual Def17.4，所以只否定普遍shortcut，不能否主命题。

## 5. 实际polynomial native offset的访问上界

设实际axis在同一J上为x_i(t)=a_i+t u_i、y_i(t)=b_i+t v_i，P(t)为2×2 polynomial matrix、degree≤D。则

    H_i(t)=y_i(t)−P(t)x_i(t)

是R²-valued polynomial，degree≤d=D+1；不是一般degree≤D。若测试还减去同一个moving offset h(t)，把d换成max(D+1,deg h)。不同j用不同h_j时，以下单曲线的constant-grid计数不能直接套用。

令每坐标在整个J上的oscillation≤R。δ/mark误差传到offset的厚度为σ；若σ≤C e，则原曲线的Ce-neighborhood命中的e-grid squares数量满足

    N_i≤C(d+1)(1+R/e),
    N_i≤C(1+R/e)^2.                                 (5)

常数依上述固定C。证明：每个非恒坐标的导数至多d−1个零点。将J按所有这些零点分成≤2d−1个interval，两坐标在各段均单调。一个monotone arc穿越网格时，每换格必跨某一坐标grid boundary；两坐标总跨越数≤C(1+R/e)。沿grid boundary恒定只多固定邻格，不产生无限重复。对所有单调段求和得第一式；bounding rectangle直接得第二式。Ce thickening只增加固定邻格。d=0的常曲线单独处理，仍满足所写d+1版本。

若σ/e不受固定上界控制，至少须保相应邻格费用；不能继续引用(5)的固定常数。实际tube截面经offset map的误差约(1+||P||)δ，另加原P近似f的误差乘实际|x|，故二者都须≤Ce。R是whole-J的polynomial range，不是fine retained times上原f的bounded range；增长degree的插值可在空隙暴涨。用bounded延拓/Bernstein构造能额外证明range控制时方可使用，不能免费Remez或C²。

对constant-offset pieces且H_j按真实访问定义，在这些已证误差条件下(5)给

    A_tot=∫N_i dν(i)
      ≤C min((D+2)(1+R/e),(1+R/e)^2).                (6)

如果只在原marks的时间子集访问，访问数只会减少，上界仍成立；但这不证明该子集的原ν×time mass大。若h_j各自moving，piece数和交叉判定须另做，不能借(6)免掉原h_j参数。

## 6. Degree、体积与实际阈值：不把有界式当gain

每个固定constant-offset test在R5中可用O(1)个degree≤D+1的polynomial inequalities表示，故E_j≤C(D+1)（用平方范数则degree倍增仍固定倍）。若h_j的degree为D_h，还须计入D_h。对共同J、固定Q_x，有|S_j|≤C|J||Q_x|e²，domain边界/ambient clipping只能减少体积但也要如实计presentation。

因而若实际construct已经证明Jpieces数N、D、R及M lower，则(2)/(6)才可合法给

    M^5 ≤ C C0 (D+1)^A N|J||Q_x|e²
                ·[min((D+2)(1+R/e),(1+R/e)^2)]^4.    (7)

没有单独证明这些实际来源时，(7)只是一张预算表。典型N约e^(−2+κ)而R/e≫1时，multiplicity因子可抵消e^κ体积saving；时间切得足够短令R/e≈1，又要付(4)及piece数。不是声称所有可能actual branches都不可能，而是不存在免费改原weights的替代。

本次真正完成的是(2)、(3)及带全range/error条件的(5)/(6)，并严格排除普遍无重数shortcut；没有构造actual positive-κ配置。下一节核对本轮root/A真正取得的endpoint输入，不把所有参数留成自由公设。

## 7. 实际endpoint palette的指数与finer-e修复

本节采用本轮root/A从原source law实际选出的H*与z*：原质量p≈_Kρ^(4−κ)，每条selected T在共同J（长度≈ρ）保至少K^(−C)ρ的原marked time；endpoint位于同一个ρ-world。原Y_{z*}的AD上下界，以full Y下界作分离球packing而非给裁切Y重设lower，给所需endpoint e-palette数

    N_y≤K^C(ρ/e)^(2−κ),  δ≲e≤ρ.                     (8)

这些来源及H*选择已实际对读本轮root/A全文；这里没有从平均density擅自宣布它们。取P0=f(z*)。原ξ_q相容性给沿真实T的constant native slope

    β_T=v_y−P0v_x ∈ ξ_q+[-Cρ,Cρ]².

endpoint误差为O(δ)，整个J的native漂移（减公共ξ_q(t−z*)后）至多Cρ²。因此e≈ρ²时，endpoint e-cell加公共affine offset便覆盖该T在整个J的marks；每管只assign一个piece，a-sum=p，M≥K^(−C)pρ，degree固定，Q_x面积O(ρ²)。真实volume求和与(2)给

    V_P≤K^C P(O(1)) ρ³ e²(ρ/e)^(2−κ)
        =K^C P(O(1))ρ^(5−κ)e^κ,
    (pρ)^5≤K^C C0 V_P p⁴
       ⇒ρ⁴≤K^C C0 P(O(1))e^κ.                       (9)

e≈ρ²只给κ≤2加原小幂损失；这是Y/Φ所在R²已有的维数范围，不是新的四维baseline或任何新κ限制。该测试的原质量没有多记，结论仍弱，不能以一次合法construction便宣主任务成功。

若e≪ρ²，保整个J且仍每管assign一个piece的直接合法方案，是额外将β_T−ξ_q以mesh e/ρ离散。slope palette数至多

    L_v≤C(1+ρ²/e)².

选h_{c,v}(t)=c+(t−z*)(ξ_q+v)，c来自(8)，则每条真实T跟随某个固定h_{c,v}，误差≤Ce；degree依旧常数。原ν与M、a-sum不变，但piece数至多N_yL_v。得到的已付certificate仅为

    ρ⁴≤K^C C0 P(O(1)) e^κ(1+ρ²/e)².

当e≤ρ²时，它至多给1≤K^C C0 e^(κ−2)，没有更强κ界。这里L_v是采用整个product palette的上界，**不是证明任何actual joint palette都有该下界**；若原source给严格更少的联合(c,v)，可能有不同信息。本轮没有免费加入这种改善。

改切clock至q≈e/ρ也不免费：每T有≥K^(−C)ρ的原marked time，每块最多容q，故其至少访问K^(−C)ρ/q个time blocks。即使每块空间内只assign一piece，原tube-piece质量仍至少K^(−C)pρ/q。若最乐观地每块都能另付同(8)的palette，其总volume为同阶N_yρ³e²，但(2)的重数费达到(ρ/q)^4≈(ρ²/e)^4；或以incidence law重写，正付(4)。实际重选endpoint/保留质量只会另需核算，不能据此声称所有分片方案同样坏。

本轮mass核验形成一个诚实的actual certificate失败：原constant-freeze endpoint方案及其直接slope/time细化，没有verified strict gain。它不证明高degree/联合label的所有改造不可能，也没有反驳完整source branch。按一主轮停止条件，若root/A的actual polynomial施工没有新的实质联合信息，就冻结本次envelope尝试，不继续调e/ρ/D。

## 8. 真正nonaffine P的完整local-clamp证书

再将A的Lipschitz延拓在每个实际allowed J内，各entry clamp到原f(Z_good∩J)的最小值/最大值区间。它不改保留原值，不增加K_f，且source同J dyadic-Lip使该区间长≤Cρ。Bernstein多项式是这些延拓值的convex combination，所以全实J均有

    |P(t)−F*|≤Cρ,  |P(t)|≤C,
    ||P−f||_{Z_good∩J}≤e/(Cρ)

可由degree D=ceil(C[1+(K_fρ²/e)^2])这张具体证书支付；不声称这是所有近似的必要degree lower。对原H*轴，保共同reference及§7的精确量，有

    H_T^P(t)=v_T(t)−P(t)u_T(t)
      =h_T*+(t−z*)η_T+(F*−P(t))u_T(t).

于是**整个实J**上H_T^P距其真实endpoint标签h_T*至多Cρ²，而不是仅retained fine times上成立。whole-J range因此≤Cρ²，P有界还使tube截面误差O(δ)≤Ce，无新增h′或point-ball假设。

先用单个完整Y_{z*}在尺度ρ²的palette覆盖所有h_T*，其数≤K^C(ρ/ρ²)^(2−κ)；每个Cρ²-ball再填e-grid（Cδ≤e≤cρ²）。得到一个真实共同constant-offset palette，去重后

    N≤K^C(ρ/ρ²)^(2−κ)(ρ²/e)^2
      =K^Cρ^(2+κ)e^(−2),
    Σ_j|S_j|≤Cρ³e²N≤K^Cρ^(5+κ).                   (10)

所有selected T在整个原J都处于这些tests的并中，M≥cp*ρ。可用half-open offset格partition；若加Ce buffer，只多固定overlap，并不降低该lower。按访问选H_j，不强行给每管一个constant label，§5得到

    A_tot≤p*L,
    L=C min((D+2)(1+ρ²/e),(1+ρ²/e)^2).

每个test的presentation费用≤C(D+1)^A，故原(2)给

    (p*ρ)^5≤K^C C0(D+1)^Aρ^(5+κ)(p*L)^4,
    ρ^(4−2κ)≤K^C C0(D+1)^A L^4.                   (11)

对0≤κ≤2，此已付certificate没有strict saving：左边不超过常数量级，degree和访问数只能增大右端。固定常数的兼容性由整个bounded ambient测试对C0的lower保证。更细e虽然产生更多pieces，其总体积上界没有缩小；只剩degree与重数费用。这是一个真实constructed nonaffine测试的失败结果，不只是“可能缺公共标签”的口头阻碍。

(10)是选用的inflated-anchor palette及其volume的**上界**，不是所有actual joint offsets的packing下界；(11)也没有证明所有nonaffine P或更精细真实label聚类都失败。这里只完成本轮要求的一次合法近似、共同S_j、原mass/clock和degree预算，并按既定停止规则冻结该证书路线。
