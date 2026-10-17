# R0047：真实四循环线段族的体积校准与闭环缺口

2026-10-17，root。总目标仍为欧氏n≥5/一般Kakeya的解决或重大中间结果。本轮未证明CYCL、未找到真实power压缩、未构造Kakeya反例。下文完整证明若干明确子类与有限连续体积证书；不宣重大性/新颖性，未经外部同行评审。

## 1. 原对象、量词和排重

N≥2 dyadic，δ=1/N，D_N={0,...,N−1}/N。A满D_N⁴，b_i:D_N→[−1,1]任意，a5=a1，B_i(A)=b_i(a_(i+1))。实际集合

    K_N=union_A{(t,X_t(A)):0≤t≤1},  X_t(A)=tA+B(A).

候选CYCL是存在c>0,A0<∞，统一于N及四表，使V_N=|N_(C0δ)(K_N)|≥c[log(2N)]^(−A0)，C0≥10固定。反攻目标可为N_j→∞同κ>0的真实V_(N_j)≤C N_j^-κ；没有这样的构造。

四方向坐标独立，TC=0，但ΣH(floor(B_i/δ)|Ai)可4logN；R41的small-S或separable假设没有自动成立。任意删direction破fullproduct，任意删shading破wholeclock，平均/逐管density须分别付原质量，不能免费重新生成本类。受限CYCL不反推旧全称CP/PM；未知全称positivegain也不自动供log lower。本轮不是已有正幂增益等价式的新名字，不另增数学ID。

## 2. 低palette的真实恢复界和一般N^-1基线

令L_i=# {floor(b_i(a)/δ):a∈D_N}，1≤L_i≤N。固定t∈[1/2,1]及一个半开side-δ输出cube。枚举b_i(a_(i+1))的一个bin后，第i个输出坐标把a_i限制在长度2δ/t≤4δ的interval，至多5个grid值。一旦某个a_i准确已知，就能查原表b_(i−1)(a_i)，由输出row i−1确定a_(i−1)至多3个值；沿逆cycle重复三次得到全部A。

故每个输出cube最多5·3³ L_i=135 L_i个原方向，无需各边际独立或额外regularity。取最小L_i，至少N⁴/(135 min L_i)个occupied cubes。每个这样的cube都在同t的N_(2δ)(K_N)横截面内；四维cube直径2δ，面积δ⁴。对t∈[1/2,1]积分得

    V_N ≥ 1/(270 min_i L_i).                              (1)

因此polylog palette子类确满足CYCL；一般min L_i≈N仅回N^-1基线，没有新严格高维saving。用粗bin或删大部分方向强求小L必须付原质量，不能借(1)升级一般情形。此恢复也说明给输出和任一完整A坐标可以逆向查表；缺的是闭环剩余自由度，而非三坐标恢复。

## 3. 负反馈单调或断环子类有constant volume

若某个b_i恒定，第i row直接以t≥1/2恢复a_i；逆向逐行恢复使任意不同A,A′的输出至少有一个坐标差≥tδ。

若每个b_i弱单调，记单调方向s_i∈{+1,−1}，且∏s_i=−1，同样有

    ||X_t(A)−X_t(A′)||_∞ ≥ tδ  (A≠A′).                 (2)

证明反设所有残差|t d_i+Δb_i|<tδ，其中d_i=a_i−a_i′，Δb_i=b_i(a_(i+1))−b_i(a_(i+1)′)。若某d_i=0，则Δb_(i−1)=0，前一row迫|d_(i−1)|<δ，故为0，绕环得A=A′。否则全部|d_i|≥δ；残差小于|t d_i|，迫Δb_i非零、与d_i异号。弱单调且Δb_i≠0给sign Δb_i=s_i sign d_(i+1)，绕环便要求∏s_i=+1，矛盾。平段没有例外。

由(2)，各点周围side-δ/4的四维cubes互不交，并在N_δ(K_N)同t切片内。N⁴个cube总体积为1/256。积分半个clock得V_N≥1/512，常数独立N、表的跳跃及变化率。

这不适用于任意rough表。若N=m²，分m个递增值域块、每块内部反序的permutation，其递增或递减子序列都至多m。分别抽四张表的monotone子表可能只留N²个方向，失去N^-2原density及fullproduct网。不得用Erdős–Szekeres的名称抹掉这个幂损失；也不追加同义monotone阈值轮。

## 4. 所有affine表的wholeclock体积下界

若b_i(a)=c_i a+d_i在D_N上affine，range条件给|c_i|(1−δ)≤2，故|c_i|≤4。把同一affine公式延至[0,1]，得到连续参数集合K^cont。每个a∈[0,1]选所在闭δ-cell的lowergrid代表，误差≤δ；固定t的每个输出坐标误差≤(1+|c_i|)δ≤5δ，四维Euclidean误差≤10δ。所以K^cont⊂N_(C0δ)(K_N)，没有免费填任意rough表。

连续slice是单位4-cube的线性像加平移，矩阵M_t=tI+C_cycle，detM_t=t⁴−P，P=∏c_i。除有限个t外线性可逆，所以slice体积恰|t⁴−P|；没有把非线性Jacobian积分错误当成无multiplicity的volume。Fubini给

    V_N ≥ ∫_0^1 |t⁴−P|dt ≥ 3/16.                       (3)

最后一步：对P∈[0,1]，函数为1/5−P+(8/5)P^(5/4)，导数−1+2P^(1/4)，在P=1/16最小且值3/16；P<0或P>1更大。故任意affine slopes/signs，包括正反馈共振，都不能产生power压缩。该结论是明确子类的初等校准，不是一般CYCL。

## 5. 单时共振和raw L²方法的界限

取b_i(a)=−τa，固定τ∈(1/2,1)，例如τ=3/4。在t=τ，X_t=τ(a_i−a_(i+1))，其坐标和为0；连续矩阵rank3，离散fibres可Θ(N)，side-δ occupied volume为Θ(N^-1)。所以逐时统一的pointwise log lower或O1 fibre估计已经失败，即使wholeclock volume仍由(3)≥3/16。

对side-δ cube平滑的概率密度μ_t，support在一个三个轴O1、剩余轴O(|t−τ|+δ)的box内，故Cauchy给E(t)=∫μ_t²≥c/(|t−τ|+δ)。于是∫_[1/2,1]E(t)dt≥c logN。不能要求raw能量uniform O1来证明constant-volume；polylog能量upper没有被这个校准否定，但一般rough循环的这种upper尚未证明。大能量本身也不推出小volume。

仅写t⁴≈∏chord slopes不足以计数全部闭环：四个差分尺度、原点/lookup约束及共同t要同时满足。用Hölder把四矩阵norm独立化会遗失正/负反馈及共振时集信息。本轮不把这个待证计数换名字作新主张。

## 6. 具有连续体积意义的精确有限证书

代码experiments/arithmetic/R0047_cyclic_continuous_volume_certificate.py，输出experiments/arithmetic/outputs/R0047_continuous_volume_certificates.json。实验只取b_i(a)=integer_index/N，并保存全部具体表；N∈{4,8,16,32,64}。令各coordinate pair差为k_i∈{1−N,...,N−1}，对应b_i差的整数index为d_i。H_i[l,d]准确数满足a−a′=l、b_i-index差=d的有序pairs。

取Q=N，time cell [j/Q,(j+1)/Q]，j=Q/2,...,Q−1。若cell内某t有|t k_i+d_i|≤1，则

    |j k_i+Q d_i|≤Q+|k_i|.

这是整个cell的上包络，非time sample volume。定义

    M_i(j)[k_i,k_(i+1)]=Σ_d H_i[k_(i+1),d]
                         1{|j k_i+Qd|≤Q+|k_i|}.

trace(M1M2M3M4)=C_j准确数满足四个上包络的完整有序direction pairs，各坐标pair恰计一次。prefix histogram通过整数ceil/floor计算所有窗口。总pair数≤N⁸，非负矩阵中间entry至多相应partial coordinate-pair数≤N⁸；N≤64时int64全部安全，求和及Fraction另用Python integers。

μ_t为X_t(A)的uniform law与side-δ cube density的卷积。其support在N_δ(K_N)的同t切片内，质量1，且

    E(t)≤δ^-4 N^-8 #pairs{|t k_i+d_i|≤1, all i}.

故∫_[1/2,1]E(t)dt≤ΣC_j/(Q N⁴)。在整个time-space上对μ_t作Cauchy，质量为1/2，得到真实连续Lebesgue volume

    |N_δ(K_N)| ≥ Q N⁴/(4ΣC_j).                           (4)

N_(C0δ)更大，故同lower也适用。没有由time采样点数估计连续上界，没有把大collision或小下界反向当power上界。

## 7. 实验结果和有限边界

十类实际表：constant、affine±、rounded3/4 resonance、negative orientation、bit reversal、Gray code、modular permutations、seeded random permutations、weighted binary digits。共50个有限族，全部得到(4)的正有理证书。N=4的十类另直接枚举N⁸有序pairs，逐time cell与矩阵trace完全一致；不复用histogram/矩阵索引。

N=64的证书display约为：constant .004586，affine± .009082，rounded3/4 .002903，negative orientation .015507，bit reversal .026821，Gray .016024，modular .029785，random .029318，weighted digits .004233。所有真实判断用整数/有理数；小数只显示。最小所列finite lower约.002463（N4 constant）；它不是统一所有N的常数。

这些只是50个具体实际tube unions的连续volume lower，不证明CYCL、任何asymptotic scaling或没有其他rough表反例。对affine等子类，解析(2)/(3)远强于粗能量证书，说明证书弱不代表真实volume小。程序显式LF写出JSON并记录source SHA256；归档hash验证不替数学证明。

## 8. 缺口、停止和后继选择

一般rough循环仍缺一个真正闭环的多尺度/共同t估计；完整CYCL未证，真实无穷scale power也未构造。原质量不能靠monotone/palette抽样免费降复杂度；finite traces只给有限lower。按一主轮设计停止当前cyclic construction尝试，不续cycle length/alphabet/S阈值，不以(1)的N^-1基线换新名。保留明确已证子类，非所有cyclic策略不可能。

提前macro见research/reviews/R0047_macro.md。R48按周期规则先作宏观/有限一手前沿核，再检验HRZ1908.05589v1真实broad/narrow递归是否存在可合法接四维finite种子的接口；不先假设有4D terminal或完整Lp输入。此为不同递归架构的有界接口审查，不是新已证高维界。

root主稿、A/B施工、实验code/fulloutput、macro/next须两代理实际全文独审；root读正式reviews后统一元数据/STATE/ROADMAP/registry/round并safe sync。没有新数学ID、major/novelty/priority认证或Goal完成。外部具名输入与项目内部证明层次继续分开。
