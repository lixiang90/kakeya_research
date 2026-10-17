# R0047：真实四循环放置的全时几何、合法子类及未闭合接口

2026-10-17，A 独立稿。已读固定入口、本轮 working spec、R46 next 及 R41 实际体积/熵稿。本轮只研究原有限表模型，不添加连续性、单调性或公共随机结构。下述可证片段并不解决一般 CYCL，也没有得到 fixed-power 构造；不是新高维维数界或重大结果，未经外部同行评审。

## 1. 原模型、量词与删选闭包

令 δ=1/N，D={0,δ,...,1−δ}，A=(a1,...,a4)∈D⁴，a5=a1，b_i:D→[−1,1] 任意。原集合是

    K_N=∪_{A∈D⁴}{(t,F_t(A)):0≤t≤1},
    F_t(A)_i=t a_i+b_i(a_(i+1)).                         (1)

每条都是完整共同 clock 的真实直线段，方向 (1,A) 在固定 graph chart 中构成满 δ-net；该线段长至少1。目标是固定 C0≥10 时对所有 N 和所有四张表有 |N_(C0δ)K_N|≥c log(2N)^−A0；反攻则须在无穷 N_j→∞ 上给同一 κ,C 的实际体积 upper C N_j^−κ。

任意方向删选不保 D⁴ 的 product law；任意部分时间 marks 不保本稿使用的全 [1/2,1] clock。因此后面的 product/counting 论证只用于原全族或明确保留的 Cartesian 子族。某个 t 的强压缩不等于全时压缩。R46 已付 finite-net continuous fill、有限旋转与 FD Prop5.4 的 compact 桥；若真有无穷尺度统一 power，不能重新虚列未知的 coherence 缺口，但本轮尚无该 power 输入。

R41 的 S=ΣH(floor(B_i/δ)|A_i) 在这里可以达到4 log N：若四表的 δ-bins 各自单射，则 B_i=b_i(A_(i+1)) 独立于 A_i，条件熵为 log N。TC(A)=0 不抵消这个 S。故不能直接引用 R41 small-S 或坐标可分离 log lower。

## 2. 实际切片体积返回：全稿共用的有限几何事实

若 F_t(D⁴) 中有 m 个点两两 ℓ∞ 距离至少 cδ，则以它们为中心取边长 cδ/2 的4维 cubes，内部互不交且都位于同 t 切片的 N_(C0δ)K_N 内，因 Euclidean radius 为 cδ/2。故该切片4维测度至少 c′mδ⁴。对任何正长度可测 t 集积分，给实际5维 neighborhood lower。

所有表只有有限个值，有限直线段并及其 neighborhood 都是可测的。这里不用给任意非可测 selector 额外施加 Fubini，也不将“抽样时刻切片大”升级成全时测度大；每次都证明整个 interval 上的切片结论。

## 3. 一张表恒定时：constant-volume 完整证明

假 b_j 恒定，其余三表任意。固定 t≥1/2，若 A≠A′ 且 ||F_t(A)−F_t(A′)||∞<tδ，则第 j 坐标给 |t(a_j−a_j′)|<tδ，故 a_j=a_j′。第 j−1 坐标的 b_(j−1) 项因而完全相等，得到 a_(j−1)=a_(j−1)′。逆循环继续，四个 a 都相等，矛盾。

于是全 N⁴ 个像点 tδ-separated。取边长 δ/4 cubes，逐 t∈[1/2,1] 切片测度至少4^−4，实际5维体积至少 1/(2·4⁴)。常数不依赖其余表的振荡、palette 或 N。

这是有限循环有一个真正断口的情形，不是一般循环的归约。把“给定一个 a_j 可恢复其余坐标”误说成“该 a_j 只有常数种可能”，正好会免费丢掉 N 的反馈费用。

## 4. 单调负反馈：不需要光滑性或斜率界

设每个 b_i 单调，选方向符号 s_i∈{−1,+1} 使 s_i b_i 非减，并假 ∏s_i=−1。允许非严格单调、平段、任意跳跃。任一 b_i 恒定已在§3处理；有平段仍可按以下证明。

固定 t≥1/2，反设 A≠A′ 且所有输出差绝对值<tδ。记 d_i=a_i−a_i′。从任一非零 d_i 开始，|t d_i|≥tδ，故 Δb_i=b_i(a_(i+1))−b_i(a_(i+1)′) 必非零且符号与 d_i 相反。这迫 d_(i+1) 非零，而且单调性给

    sign d_i=−s_i sign d_(i+1).                        (2)

沿四环传播并相乘得到 ∏s_i=+1，矛盾。因此 F_t(D⁴) 仍 tδ-separated，§3同一全时正体积 lower 成立。没有对有限表作连续插值，跳跃不会破坏符号推论。

此片段不是一般 CYCL。若正反馈 ∏s_i=+1，(2) 没有矛盾；例如 b_i(a)=−a 在 t=1 的像有真实一维 kernel。这个单时退化本身也不证全时小体积。

从粗表先抽单调子表不能免费应用本节：N=m² 时，将 m 个块按值递增排列，每块内部按值递减，得到 permutation 表；任何递增或递减子序列至多 m。四张表分别用这种结构，逐表单调抽取至多保 N² 个 Cartesian 方向，原 N⁴ 的密度损 N^−2。该严格例只否掉这个抽取捷径，不是 CYCL 反例。

## 5. 任意 affine 表：实际 constant-volume，含网格费用

假 b_i(a)=c_i a+d_i 在 D 上精确成立。N≥2 及表值[-1,1] 给 |c_i|≤2/(1−δ)≤4。将同一 affine 公式延到 A∈[0,1]⁴，令 K_c 为对应连续方向全时集合。其固定 t 的线性矩阵 M_t 有 diagonal t、循环 superdiagonal c_i，故

    det M_t=t⁴−P,  P=∏c_i.                            (3)

除至多有限个 t，线性变换可逆，连续 slice 体积恰 |t⁴−P|。即使奇异时刻，也不影响 Fubini 积分。对任意实 P，凸函数 g(P)=∫_0¹|t⁴−P|dt 在 t⁴ 的 median P=1/16 处最小；直接分 t=1/2 积分得

    ∫_0¹|t⁴−P|dt≥3/16.                               (4)

不想用 median 事实，也可分别在 P≤0、P≥1、0<P<1 时求导 g′(P)=2P^(1/4)−1 得同结论。

对任一 A∈[0,1]⁴，取各坐标不大于它的最近 D 值，端点 A_i=1 取1−δ。各输入差≤δ，故每个输出坐标差≤(1+|c_i|)δ≤5δ，Euclidean 差≤10δ。保持 t 不变，因此 K_c⊂N_(C0δ)K_N，C0≥10 足够，(4) 给

    |N_(C0δ)K_N|≥3/16.                               (5)

这是 wholeclock、全连续 slice 体积的证明，不是只算某个 determinant 或单 t。该 affine 类已包含正反馈单时 singular 情形，却不能覆盖任意有限表。

## 6. 一个小 palette 的完整版本与一般 N^−1 边界

令 L_i 为 b_i(D) 遇到的半开 δ-bins 数。固定 t∈[1/2,1] 及一个输出 δ-cube，先指定 b_i(a_(i+1)) 的 δ-bin，输出 i 迫 a_i 落长度≤4δ 的 interval，故至多5个网格候选。每个确定的 a_i 使 b_(i−1)(a_i) 完全已知，输出 i−1 给至多3个候选 a_(i−1)；逆环继续，至多固定 C 个 A。因此该输出 cube 的 fibre≤C L_i，亦≤C min_i L_i。

N⁴ 原输入故占据至少 cN⁴/min L_i 个输出 δ-cubes。每个 occupied cube 全含于同切片的 N_(2δ)K_N：选其中一个像点，cube直径2δ。因 cubes 不交，积分得

    |N_(C0δ)K_N|≥c/(min_i L_i).                       (6)

polylog palette 子类满足 CYCL；一般 L_i≤N 仅给 c/N。也可以不枚举 palette，而直接枚举 a_i 的 N 个可能值，再逆环恢复，得到同一个 N^−1。此项是反馈切断的旧层级，不能改名成一般闭环增益。

## 7. 对一般粗表，尚未闭合的精确碰撞积分

取原 A 上 uniform law，将 F_t(A) 的 law 与 spatial cube [−δ/2,δ/2]⁴ 的 uniform density 卷积，记 density μ_t。它的 support 在同 t 的 Euclidean δ-neighborhood 内。若

    C(t)=#{(A,A′): ||F_t(A)−F_t(A′)||∞≤δ},

则各平移 cube 的 L² overlap≤δ^−4，故

    ∫μ_t²≤N^−4 C(t).                                 (7)

对 t∈I=[1/2,1] 整体 Cauchy，∫_I∫μ_t=1/2，得

    |N_δK_N|≥N⁴/[4∫_I C(t)dt].                       (8)

所以 ∫_I C(t)dt≤C N⁴ log(2N)^A 是足够的真实全时联合目标。它不是已证结论。一般 fibre≤CN 只给 ∫C≤CN⁵，返回 N^−1；单个平面 marginal 的 harmonic L² 不能直接相乘来填(8)。

为了显示四环的耦合，写 d_i=a_i−a_i′、e_i=b_i(a_(i+1))−b_i(a_(i+1)′)。同一 t 必须同时满足 |t d_i+e_i|≤δ。将每对 (a_i,a_i′) 按 d_i 分组，定义 transfer matrix

    T_i(t)[d_i,d_(i+1)]
      =#{(a,a′):a−a′=d_(i+1),
            |t d_i+b_i(a)−b_i(a′)|≤δ}.

则 C(t)=tr(T_1(t)T_2(t)T_3(t)T_4(t))，原有限 pair 一一对应循环中的四个实际坐标对。trace 不是四个独立 marginal 能量的乘积。仅用各 row/column 容量或“给定一个坐标可恢复”仍留下 N；目前没有解析地消去这个因子。

## 8. 有限连续时间证书实际核查的范围

实际读 root 的 `experiments/arithmetic/R0047_cyclic_continuous_volume_certificate.py`。它对 b_i=k_i/N 的整数表，预计算每张表的精确 difference histogram。时间 cell [j/Q,(j+1)/Q] 内，真实碰撞必有

    |j d+Q e|≤Q+|d|,

其中 d,e 是原整数差，因此 transfer trace 是该整个 cell 的 C(t) upper，而非 time samples。对 Q=N，若总 upper 为 U，(8) 给 QN⁴/(4U)。所有 matrix 中间计数≤N⁸，N≤64 时 int64 无溢出；总和及有理数用 Python int/Fraction。N=4 时另用原方向对直接重算十种表，校验 trace 对应。

程序覆盖50张明确表族（N=4,8,16,32,64 各十种），所得都是实际 continuous neighborhood **lower**。这些证书不能建立 arbitrary N/表的统一 trace upper，更不是 asymptotic volume upper。本文只审代码与公式对应；没有第三次重跑整组实验，也没有把读到的 finite success 当 CYCL 认证。

## 9. primary 有限比对与禁止的插值捷径

本轮重新打开并核一手版本：

- Rafael J. Fernández-Delgado、Mikael de la Salle，*A construction of Kakeya Sets in Arbitrary Dimension*，arXiv:2607.14824v3，2026-09-17，https://arxiv.org/html/2607.14824v3 。本轮读 introduction/Thm1.3 与已有本库全文§§4–5的适用范围；Thm1.3 是某个全方向 compact set 的 log^(−(d−1)) neighborhood **upper**，没有任意四循环表的 lower。Prop5.4 负责合格 finite input 到 compact 输出，不给本轮尚缺的 power input。
- Ruixiang Zhang，*Mixed-norm Brascamp-Lieb inequalities*，arXiv:2608.17952v2，https://arxiv.org/html/2608.17952v2 。本轮核§§2–4与 R46 已读的 fixed rational finite slicing statement 的对象；旧 q=7/4、四投影及 fibre 条件不等于全连续 clock 的 cyclic collision integral(8)。R46 的 q=5/3 算术候选也仍未证，不能在本轮借题名当输入。

另作有限检索 Kakeya/cyclic、Kakeya/separable、Kakeya/product/shears，所得 finite cyclic-ring、Lie-group continuous configuration 等并非本模型。不以有限无命中认证新颖性，不声称文献不存在相关定理。本轮没有申请新增 PDF 或依赖未读二手结论。

任意表作 piecewise-linear 插值可能在一个 δ-gap 上跳 O(1)，新 continuous image 不在原 N_(C0δ)K_N 内；不能对该新 map 计算 Jacobian 后给原 set lower。piecewise-constant 插值则保近似，但有 discontinuity，不得免费用 smooth change-of-variables/global degree。按坐标依次作 shear 的 composition 也不同于(1)：最后一步会读到已修改的 a1，不能把 simultaneous cycle 宣称体积保持。

## 10. 本轮退出边界

已完整证明常值断环、负反馈单调、affine、polylog palette 子类的实际下界，并把一般 joint collision 的真实未付量写成(8)。尚无 arbitrary 表的 uniform log lower、无无穷尺度统一 power upper、无 Kakeya 反例。上述子类不保合法任意 restriction，不能反推原 CYCL；旧 general positive-power conjecture 也不会给这里的 log 强度。

按本轮停止条件，若 root/B 也无新的 general trace 信息，冻结仅循环长度/表 alphabet/高 S 参数重命名的局部迭代；不继续用有限枚举代替 asymptotic 证明。正式全文 review 待 root 主稿及 B 主稿落盘后完成，本文不提前认证整轮或一般维度 Goal。
