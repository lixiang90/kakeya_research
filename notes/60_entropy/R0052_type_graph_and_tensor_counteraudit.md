# R0052：有理law到type图、整数编码与统一常数的完整反攻

2026-10-17，B。读固定恢复入口、registry78状态、R52 working_spec与R51 nextgate。本文仅编辑分配文件，不Git，不执行远程来源代码。目标是严格否定固定R46算术候选；不是欧氏Kakeya反例、维数改善或重大结果。前7节给一般验收管道；§8给本轮已找到的Q12实际证书及有限实例。law由root保存、A独立聚合，未经外部同行评审。

## 1. 固定候选、可接受输入与原质量

候选(R)要求一个与无挠群G、有限非空Z⊂G²、坐标大小及tensor次数无关的有限C，使

    N≤C M^(1/3)(S₁S₂S₃)^(10/21)S₄^(5/21)，
    N=|Z|，M=max_x|Z_x|，
    S₁=|{x+y}|，S₂=|{−x+y}|，S₃=|{y}|，S₄=|{x+3y}|。

输入是一张有限整数支持S⊂Z²上的同一jointlaw。每个(a,b)∈S有正整数权w_ab，总数Q。零权条目删除，重复支持先合并；不能拼接四张不同jointlaw的marginals。记D=A−B，四个controlled变量为A、B、A+B、A+2B，合并权分别记d_v与c_{r,v}，r=0,∞,1,2。

以下熵一律以自然log计算，0log0=0。只要某个可靠有向区间给

    Δ:=21H(D)−10[H(A)+H(B)+H(A+B)]−5H(A+2B)≥g>0， (1)

其中g是已证正的有理数，本稿就给明确有限type长度与严格反例seed。更强的H(D)>(5/3)max_r H(C_r)足够，却非必须。若source以bits计算，须先支付ln2转换，不能把不同log底的gap与本稿误差混用。

对原集合取子集只保S_j、M的upper，不保N。下文的代表选择特意保目标difference image，绝不宣称选择后的概率law仍为原law；这里所需的是真实基数，而非几何shading或条件先验的保真。

## 2. 熵gap可以用整数乘幂精确判定

定义P_D=∏_v d_v^(d_v)，P_r=∏_v c_{r,v}^(c_{r,v})，空因子不出现。展开H(C)=logQ−Q^(−1)Σc logc，得到

    QΔ=log[(P₀P_∞P₁)^10 P₂^5/(Q^(14Q)P_D^21)]。

故Δ>0准确等价于

    (P₀P_∞P₁)^10 P₂^5>Q^(14Q)P_D^21。            (2)

更强的四个条件3H(D)>5H(C_r)，分别等价于

    P_r^5>Q^(2Q)P_D^3。                           (3)

这些是准确整数比较，不是将浮点结果四舍五入为strict。若整数太大，可用可靠log上下界核(1)/(2)，但区间必须排开0。四个marginal均须从同一个保存的整数joint表独立重算。比率1.668的作者报告本身不替代(1)的本项目证书。

## 3. 每个目标type word均有真实joint实现

取任意正整数k，n=kQ。联合type类J_k由所有长度n的整数对序列(A^n,B^n)组成，其中每个原pair(a,b)恰出现kw_ab次。目标type类D_k由所有difference序列v^n组成，其中每个v出现kd_v次；因此

    N_k:=|D_k|=n!/∏_v(kd_v)!。                    (4)

**目标image准确覆盖D_k。** 给定任意v^n∈D_k，对每个v，将其出现位置按索引递增排列，并把S_v={(a,b):a−b=v}按lex顺序排列。将前kw_{a₁b₁}个位置填(a₁,b₁)，再填下一个pair，依次进行。因为Σ_(S_v)kw_ab=kd_v，所有位置恰填完。这样得到一个确定的jointword，属于J_k，且逐坐标difference正是v^n。

反向任何J_k的difference直方图都等于kd_v，所以image不只是包含，而恰等于D_k。每个controlled projection的word直方图也恒为kc_{r,v}；它的image因此包含于对应type类，其基数上界为

    K_{r,k}:=n!/∏_v(kc_{r,v})!。                  (5)

没有用jointentropy替换目标entropy，也没有用某个type的cardinality upper冒充目标image lower。由以上显式规则，只需每个difference word一个joint实现，不必列出整个天文规模的J_k。

## 4. 真实M=1图及四个原forms

对上述每个v^n只保一个构造出的jointword，作同一个线性变元

    x=B^n−A^n=−v^n，y=A^n+B^n。

得到Z_k⊂(Z^n)²。不同目标word给不同x，所以N=|Z_k|=N_k且M=1。四个原forms恰为

    x+y=2B^n，−x+y=2A^n，y=A^n+B^n，
    x+3y=2(A^n+2B^n)。

乘2在无挠整数群单射，故实际S₁≤K_{∞,k}、S₂≤K_{0,k}、S₃≤K_{1,k}、S₄≤K_{2,k}。第一二个交换不影响同权乘积。因此只要

    N_k^21>(K_{0,k}K_{∞,k}K_{1,k})^10 K_{2,k}^5， (6)

就有一个严格违反(R)的sharp C=1整数向量图seed。代表选择后其它image可以变小，只会加强失败；不要求它们仍覆盖全部marginal type类。也没有把有限图凭空送入full角方向的真实管族。

## 5. 显式有效长度：只需初等factorial积分界

给出一个不物化巨阶乘、也不借未量化Stirling误差的完全有效选择。对整数j≥1，由log单调可逐区间积分得

    jlogj−j+1≤log(j!)≤jlogj−j+1+logj。           (7)

令s为D的正权值个数。对(4)的正整数counts m_v=kd_v使用(7)，得到

    log N_k≥nH(D)−[(s−1)+Σ_v logm_v]
            ≥nH(D)−s(1+logn)。                  (8)

任意(5)的type类在其自身marginal product law下，每个word概率均为exp(−nH(C_r))。该type总概率≤1，所以

    log K_{r,k}≤nH(C_r)。                        (9)

由(8)/(9)，(6)左边除右边的log至少是

    nΔ−21s(1+logn)。                            (10)

对n≥1有1+logn≤2√n。若(1)已证Δ≥g>0，可取

    k=max{1, ceil((84s/g)²/Q)}，n=kQ。           (11)

于是√n≥84s/g，(10)≥ng−42s√n≥ng/2>0，严格证明(6)。所有ceil仅作用于明确的正有理数，可用整数除法准确计算；即使n极大也仍是一个明确有限长度。若更精细的可靠factorial区间找到较小k，可以替代(11)，但不是证明必需。

这给出了从strict有理gap到一个有效有限seed的完整闭合，不依赖将n→∞的口头极限。若程序只证明Δ>0却没给任何量化lower，也可由可靠区间取得有理g；不能把float显示的正末位直接当g。

## 6. 显式压回一个整数坐标并保所有等值关系

Z_k目前位于整数向量群。令L≥1为单坐标x、y及四个原forms全部可能值的abs上界，取整数β=2L+2，定义群同态

    ℓ(z₁,…,z_n)=Σ_(i=1)^n z_i β^(i−1)。

对于这些有限值域中的两个不同word，取最高非零差位j，主项abs至少β^(j−1)，所有低位abs之和不超过2L(β^(j−1)−1)/(β−1)，严格小于主项。故ℓ在所有相关finite word集合上单射。它与整数系数forms准确交换，因而

    Z̃_k={(ℓx,ℓy):(x,y)∈Z_k}⊂Z²

保N、全部四个实际S_j以及每个x的纤维；特别M仍为1。这是有限值域上的真实整数编码，不需要形式数字乘法、无carry假设或数值舍入。若最初支持为有理坐标，先共同清分母，所有一维linearforms均同比例伸缩，marginal计数不变，再应用此证明。

该压缩不保原欧氏尺度、方向分离或坐标条件数。允许非常大的整数并不削弱(R)的反例，因为其常数本来不允许依坐标大小。

## 7. 一个sharp seed如何否定任意统一C

设上节得到有限Z₀⊂Z²、M=1，令

    R=N₀/[(S₁S₂S₃)^(10/21)S₄^(5/21)]>1。

单个seed只直接反C=1，不会单独反所有大C。对任意m取Z₀的Cartesian m次幂，N和四个projection基数准确取m次幂，M仍为1，所以候选比率为R^m。再次用§6压回Z²仍准确保这些基数。给任何固定有限C，选择m使R^m>C，就得到(R)失败。

因此不存在统一有限C；甚至固定G=Z也不存在与数值大小无关的统一常数。没有假设tensor后的ambient几何估计常数不变：这里从始至终只使用原全称算术命题及准确整数编码，没有调用Euclidean有限种子。

## 8. 实际Q12 law、n240证书与不依浮点的解析备份

本轮B从R46旧六点支持手推自然权1,2,3,3,2,1，得到(A,B;权)六行

    (1,0;1)，(0,0;2)，(0,1;3)，(−1,1;3)，(−1,2;2)，(−2,2;1)。

总权Q=12。D在支持上单射，按值排序的权为(1,2,3,3,2,1)；A为(1,5,5,1)，B为(3,6,3)，A+B为(6,6)，A+2B为(2,4,4,2)。因此

    P_D=2⁴3⁶，P_A=5¹⁰，P_B=2⁶3¹²，
    P₁=2¹²3¹²，P₂=2²⁰，
    exp(12Δ)=5¹⁰⁰/(2¹⁴⁰3⁵⁴)>1。                 (12)

这不是从官方报告直接取得的SD≥1.668概率表。事实上该law的强测试3H(D)>5H(A+2B)失败，其整数比为2⁴⁰/3⁴²<1。因此本证书仅完成允许的较弱weighted目标，不能宣称复现该强SD报告。

实际输入为`experiments/arithmetic/inputs/R0052_rational_counterlaw.json`。root exact程序/输出为`R0052_exact_countercertificate.py`及`outputs/R0052_exact_countercertificate.json`；A独立程序/输出为`R0052_independent_certificate_verify.py`及`outputs/R0052_independent_verification.json`。本代理实际读输入、两完整程序和两完整输出，未修改或导入它们。

取k=20、n=240。因为D单坐标支持已经单射，整个jointtype与目标type一一对应，不需额外删代表。四controlled type upper分别使用counts

    A:(20,100,100,20)，B:(60,120,60)，
    A+B:(120,120)，A+2B:(40,80,80,40)。

两程序给(6)严格成立，left bit length12011、right11971。B另用独立的sequential-binomial product计算multinomial（未调用root的factorial聚合程序），得到相同N_k，确认left>right，甚至left>2³⁹right。这证明一个真正有限实例，而非只以entropy渐近取代有限误差。四实际projection仍只用相应安全upper，不虚称它们与完整边际type类相等。单坐标五种值域abs≤6，故§6可直接用base14；tensor后继续在长度240t用同一base14，保所有等值类。

还可完全不用log数值或大factorials给一个较大有限长度的纯证明备份。准确整数比较为

    5¹⁰⁰−2¹⁴⁰3⁵⁸
      =1323647806611649703349748236057412369408586593193509590897283622430961>0。

所以(12)的比大于81。由e<3，ln3>1，故12Δ>ln81>4，得到Δ>1/3。取k=400、n=4800。e>8/3且8⁹>4800·3⁹，故ln4800<9；s=6，(10)>4800/3−126·10=340>0。因此(6)在这个明确长度也严格成立，无需优化最小k。e的两个界仅由指数级数的初项和几何尾估计得到。

## 9. 完成范围与停止

反攻测试已覆盖同一jointlaw聚合、difference而非joint目标、π₂=A+2B、typeimage surjectivity、M=1、实际projection upper、log底、严格有限误差、整数编码及单seed与任意C的区别。实际Q12/n240实例连同§7的tensor给出原全称(R)失败，甚至固定G=Z也不成立；最终reviewed仍由正式全文独审与root整合决定。

本轮关闭R46候选，不改q、权重或其它slopes续轮，不优化小数。旧有限uniform网格结论保其范围；强SD1.668来源报告没有被此law独立复现，欧氏Kakeya和长期Goal仍未解决，不宣新颖或重大性。下一实际几何候选与独审由root另外整合，不以本算术反例清空任何原方向/clock/shading责任。
