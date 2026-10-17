# R0072：原核坐标响应的双时刻恢复与局部反攻

2026-10-18，B。先实际读 R72 spec5/macro 的 phase II 锁题及本轮 phase I 全目标审计，重读原 Def17.2–17.4 与 R16 单管公式。以下保真实 straight line、同一 tube 的两个终时，不把两个独立 arms 拼起来。结论是局部 coercivity 反攻及恢复责任，**不是完整 source 或 Kakeya 反例**；无 ordinary 新界、major 或新颖性认证。仅编辑本 assigned 文件，不 Git、不 spawn。

## 1. 原同管公式必须保 x1 项

取 common-kernel f(t)=u(t)e1^T，初点为 p=(x1,x2,y+u(t)x1,t)，其原 witness 方向为 (phi,xi_p+u(t)phi1)+O(delta)。沿同一原管到 s，令 l=s−t，其 normal grain 坐标满足

    y_s = y+l xi_p+[u(t)−u(s)](x1+l phi1)+O(delta).       (1)

因此没有先中心化 x1 时，不能删掉 [u(t)−u(s)]x1。下面的反攻使用 (1) 的精确版，不忽略初始位置。两个终时所见的 xi/phi 必须属于同一原 label；若某个终时没有原 shading/point witness，只能称该真实直线在该时刻的几何交点，不能免费称 source 访问。

令 c_i=u(t)−u(s_i)，且 |s_i−t|≥g。若 y、x1 和两个实际 y_(s_i) 已知，定义

    R_i=(y_(s_i)−y)/(s_i−t)−c_i x1/(s_i−t)。

则 R_i=xi_p+c_i phi1+O(delta/g)，所以

    R_1−R_2=(c_1−c_2)phi1+O(delta/g).                     (2)

若 |u(s1)−u(s2)|≥h，(2) 给 phi1 误差 O(delta/(gh))；代回后 xi 误差 O(delta/g+M delta/(gh))，M 为 u 的固定界。若输入 normal 输出只在 e 尺度已知，应把 delta 换 e。这个恢复只需向量差非零，不需要 det(c1,c2) 非零；相反，它不自动给 xi basicness，因为两个输出都是自适应 normal labels，仍有各自的 carrier 自由度。

## 2. 有限模型的固定参数与原质量

取 b 为足够大的20倍整数，B=2^b，N 为5的倍数。以下均是实际有限实数数字和，不使用无进位形式乘法。设

    M=2^(b−5)=B/32， Q=M/8=2^(b−8)， K1=M/32=2^(b−10)，
    K2=2^(11b/20+2)， V=2^(13b/20+3)， R=Q/V=2^(7b/20−11)。

取 b≥100，则这些都是整数，R≥1。数字长度为 N，记 h=B^−N；实际 fine scale 取 delta=B^(−N−4)。这个固定四位 buffer 只改变 B 相关常数，并保证下面所有物理点、角集及 terminal carriers 的最小分离均大于 delta。b 固定后 N 最后趋大。

把数字位置分为周期5的三类：A 位占2/5，B 位占2/5，O 位占1/5。对每个 q_i∈{0,...,Q−1}，定义 x1 的该位数字

    A位：2q_i； B位：−q_i； O位：q_i。

这些 signed digits 定义有限集合 X1。另令 X2 的每位为独立 q_i∈{0,...,Q−1}，并取 X=X1×X2。所有 q 字母独立均匀。signed digit 的总尾部跨度小于 3Q/(B−1)<1/50，故第一不同位置的整数数字差不会被后续尾部消去；这些表示单射，而且各尺度都是固定 B 常数的 Ahlfors 集。

写 d_X=log_B Q=1−8/b，有

    #X ≍_B delta^(−2+16/b)，  dim-scale X1=dim-scale X2=d_X。  (3)

任给需要的 arbitrarily small eta>0，先取 b 使16/b<eta/2，再取 N 足够大，(3) 蕴含 #X≥delta^(−2+eta)。所以它满足 source 要求的单 grain 水平数量，不是固定正幂稀疏 domain。

## 3. point angles：kappa=3/4、slab gamma=1/10及 coarse coherence

给定初点的 x1 数字 q_i，在每个 O 位另取 k_i∈{0,...,K1−1}，并定义 coded phi1 数字

    A位：−q_i； B位：q_i； O位：M/4+k_i−q_i。                (4)

phi2 每位独立取 {0,...,K2−1}。实际角集合为 Phi_p=8(Phi1(x1)×Phi2)。所有角有界且远离盒边界；缩放8是固定常数，不依 delta。Phi1(x1) 是一个固定 O 位 Cantor 集的平移，维数

    beta1=(1/5)log_B K1=1/5−2/b； beta2=log_B K2=11/20+2/b。

于是每个 Phi_p 都有 kappa=beta1+beta2=3/4 的 AD 数量与全尺度 AD 常数 C_B，且 #Phi_p 与 p 无关。任一单位 normal 至少有一个坐标绝对值≥1/sqrt(2)；条件化另一独立角坐标，使用该一维 Cantor 的 interval cap，可得任意宽 w≥delta 的 affine slab 的归一质量≤C_B w^min(beta1,beta2)≤C_B w^(1/10)。这里是原 pointwise product law，不给条件化后的任意子图额外 lower。故 gamma=1/10，且数值上 kappa+gamma<1；本 k=ell=3 matrix source 不借用 R70 的 mixed43 参数结论。

coarse coherence 也有实际验证。若两个 x1 的第一不同 q 位为 k，主数字差至少 |Delta q|B^−k，尾部至多(3Q/(B−1))B^−k；(4) 的平移部分差至多(|Delta q|+2Q/(B−1))B^−k。所以 Phi1 的平移量是 x1 的固定 Lipschitz 函数，常数可取绝对数；相同 free k-digits 使两集合逐点对应。在一个物理 rho-cube 内，各 Phi_p 都落在某 Phi_(p0) 的 C rho 邻域中。取该邻域的 rho-net 作 Phi_q，厚度仅 C rho，所以在所有尺度≥rho 上仍为 (rho,kappa,C_B)-AD，且覆盖全部 Phi_p 的 rho 邻域包含责任可付固定邻格。没有假 unused coarse cells 自动具有另一个 slab lower。

## 4. 真 Lipschitz digit response，其像仍有 fixed positive dimension

对 X2 的每位 q_i，写 r_i=floor(q_i/R)∈{0,...,V−1}，定义

    zeta(x2)=B^−1 sum_(i=1)^N r_i B^−i， xi_p=(0,zeta(x2))。 (5)

每个 r_i 恰有 R 个原 q_i preimages，故 uniform X2 的 zeta law 是 uniform V-letter Cantor，维数

    beta=log_B V=13/20+3/b。

它不是常数，且 beta≥13/20，与 domain 亏损16/b可任意小同时成立。若两个 x2 的第一不同位为 k、该位差 d≥1，则

    |Delta x2|≥(d−Q/(B−1))B^−k，
    |Delta zeta|≤B^−1[d/R+1+V/(B−1)]B^−k≤|Delta x2|。

因此 (5) 真正为1-Lipschitz，不是 full-grid 上不连续的旧 digit mask。它可作1-Lipschitz实值延拓并裁到有界区间；原 physical cube 的 xi coherence 因而逐尺度成立。

对所有 delta≤rho≤1，uniform 原 reference 下有

    Pr{zeta∈I}≤C_B(rho+delta)^beta  （|I|≤C rho）。          (6)

原 reference 是 uniform X、每个 p 的 uniform Phi_p；所有点的角数相等，故也等于初始 actual tube labels 的 uniform counting law，至多固定邻格碰撞。若任意相关0≤g'≤1保原质量 m，且 xi-image由 L 个 rho-bins 覆盖，则

    m≤C_B L(rho+delta)^beta，  N_rho(xi(supp g'))≥c_B m rho^−beta。 (7)

例如 rho∈[delta^(1/4),delta^mu]、m≥delta^a 时，只要 a+A eta<mu beta，(7) 就不允许用 delta^(−A eta) 个 bins 覆盖。这同时容许 eta任意小、a相对 fixed mu任意小。它只否定从 filled X、point angles/coherence 及以下两个终时条件推出 basicness 的局部跳步；不声 full source 有这样的反例。

## 5. 同一真实 unit tube 的两个终时与精确输出

在 R5 取原 initial grain y=0、t=0；令 u(t)=(t,t²)，f(t)=u(t)e1^T，global bounded Lipschitz，且 u 的像非直线。每个 p=(x1,x2,0,0,0) 和 Phi_p 的每个实际角 (8phi1,8phi2)，取支持线

    ell_(p,phi)(t)=(x1+8t phi1, x2+8t phi2, t xi_p, t)。    (8)

所有斜率绝对有界且很小，取以初点为中心的 Euclidean unit segment，实际包含 clock s1=1/8、s2=1/4。原方向条件在 t=0 精确成立，因为 f(0)=0；两个输出使用同一个 p、phi、xi 和同一条 (8)，并非独立 arms。沿 (8) 的 normal 坐标为

    y_s=s xi_p−u(s)(x1+8s phi1)。                           (9)

写 a1=x1+phi1、a2=x1+2phi1。由 (4) 逐位直接算得

| 位置 | x1数字 | phi1数字 | a1数字 | a2数字 |
| --- | --- | --- | --- | --- |
| A | 2q | −q | q | 0 |
| B | −q | q | 0 | q |
| O | q | M/4+k−q | M/4+k | M/2+2k−q |

这些是实数数字和的精确恒等式；O 位的 a2 数字介于 3M/8 与9M/16内，均在 {0,...,M−1}，没有省略 carry 的误差。a1、a2 各仅在3/5位置非零。令 A1、A2 分别在这些活跃位允许全部 M 字母、其余为0，则所有实际 a_i∈A_i；各 A_i 的 AD 维数为

    alpha_A=(3/5)log_B M=3/5−3/b。

令 V0=zeta(X2)，取两个 terminal carriers

    Y_(s_i)=−u(s_i) A_i+s_i V0 e2。                         (10)

u(s_i) 的第一坐标非零，故 (a,z)→−u(s_i)a+s_i z e2 为固定 invertible linear map。因此 (9) 对全部初点/角都精确落 (10)，而

    dim-scale Y_(s_i)=alpha_A+beta=5/4=2−kappa。             (11)

这已经保两个终时输出的实际关联及正确 normal carrier 的 AD 指数；不是仅仅计算一个 formal point。

## 6. 两个 terminal carriers 也有正确 tube Katz–Tao

先对 A_i×V0。在一个 rho×tau tube 中选 long-axis 最大分量对应的坐标，其投影长 O(tau)，每个该坐标 rho-bin 仅对应 O(1) 个另一坐标 rho-bins。于是 AD interval upper 给

    N_rho[(A_i×V0)∩tube]≤C_B(tau/rho)^max(alpha_A,beta)，
    delta≤rho≤tau≤1。

两一维 Cantor 虽每5位的活跃模式不同，但周期固定，任意中间尺度只损 C_B，并不损 N 相关幂。固定 invertible linear map把管送入固定倍长宽管，故 (10) 继承同界。b≥100 时 max(alpha_A,beta)<9/10=1−gamma，得到 source 所需的 (delta,1−gamma,C_B)-tube Katz–Tao。所有固定 C_B 在 N 最后足大时可小于 delta^−eta。

由此，本模型同时具有：near-full horizontal X；nonconstant Lipschitz xi；每个初点的正确 kappa-AD/slab gamma 角；初点 coarse coherence；全部这些原 labels 的同一真实 tube 在两个 fixed terminal clocks 的 exact outputs；两个 terminal Y 的 AD2−kappa 与 tube-KT1−gamma。raw reference取 g=1，不靠删成稀薄的成功子图。即便允许 arbitrary dominated g' 保 delta^a 质量，(7) 仍阻止局部 basicness。

## 7. 两时刻线性恢复不降低 normal outputs 的自由度

本例中 u(s1)−u(s2) 为固定非零向量，故 (2) 的恢复条件最有利；沿 c1−c2 方向取内积即可在固定误差内恢复 phi1、xi。恢复可逆并不意味着它们原来近常。

输出 pair (y_(s1),y_(s2)) 由 (a1,a2,zeta) 参数化。由两块中的第一 normal coordinate 可分别恢复 a1、a2，再由任一第二 normal coordinate 恢复 zeta，所以在该3维线性 image 上为双 Lipschitz。允许的 normal pair 不是一个固定常量；其三个参数具有真实自由度。固定一个输出或某标签后再把另一个输出当自动同 law，会丢掉这个自由度。

实际 joint (a1,a2) 的独立原字母数是 Q^N K1^(N/5)，即维数 (1−8/b)+(1/5−2/b)=6/5−10/b；再加 beta，actual joint output pair 的维数为37/20−7/b，正常大于任一个 terminal 的5/4维。相比 product target Y_(s1)×Y_(s2) 的5/2维，它是相关的低维子集，但这并不迫 xi 在 subpower 个 bins。所有这些维数均是固定 B 数字计数加上述线性 inverse 得到，不把 Jacobian rank 当原 law Frostman。

## 8. 完整 source 的缺失条件和不能作出的推论

本模型**不**是 Def17 的完整配置，且有具体不能忽略的失败：

- 只给一个初始 normal grain 的全 X 与初点 Φ/ξ；没有给每个原 z、每个 y∈Y_z 的 filled X 与 point Φ。Z不是 nearfull clock。对一般其他 clock，(9) 未被证明仍落具有(11)指数的 Y_s，跨 time 的 AD union 更未验证。
- 原 initial y=0 且 xi 的第一 normal 分量为0，故全部物理 lines (8) 都位于 hyperplane physical y1=0；whole-tube CW 常数至少 c delta^−1，严重违反源的 subpower CW。不能用 unused labels/padding 修复而仍称原主质量满足源。
- 初始 actual tube labels 的参数维数为 (2−16/b)+kappa=11/4−16/b，不是所需 joint4-AD。没有把终时粗 carrier 的虚 labels 当作真实 T 补齐。
- 两个 terminal Y 的正确 AD/KT 只验证其自身与实际 endpoint containment，不给这些 endpoint 的 pointwise κ 个 witness directions、ξ coherence、所有 allowed windows 或平均 nearfull whole configuration。

最后一项还有精确的 selected-incidence 冲突，不能只写成“未检查”。固定 a1、x2、phi2 和全部 O/A 位数据，仅改变 B 位 q。a1 保持不变而 a2、phi1 改变；在 s1=1/8，物理终点是 (a1,x2+phi2,s1 xi_p,s1)，故它完全相同，各原管的 normal 物理斜率也同为 xi_p。但若这些 tube 都是该终点的 selected incidences，同一 xi_terminal 必须满足

    xi_p=xi_terminal+u(s1)(8phi1)+O(delta)。

u(s1) 的第一坐标非零，所以这只允许 phi1 在 O(delta) 区间内；B 位造成的多值变化不能全部保留。其 conditional 字母数 Q^(2N/5) 是固定正幂，不是固定邻格碰撞。只挑一种 phi1 并重设终点 law 会真实损失原质量，不能把它当作 full source 完成。这是模型与完整原 terminal ξ 兼容条件的明确分界。

所以 (7) 不反完整 common-kernel 分支，更不反 ordinary Kakeya。它严格否定的是：仅凭 filled initial X、Lipschitz/coherent ξ、pointwise Φ 以及一对同管终时正确 normal carriers，便迫 ξ basic 或迫商纤维 lower 的推理。full whole-clock/CW 仍可能提供真正额外限制，必须实际证明后才能使用。

## 9. 原质量闭包及本机制停止线

同管两个终时在原 source 中应从每条实际 T 的原 shading 取样：若每 tube 的细访问数为 d(T)，ordered 两时刻总数是 sum d(T)^2，CS 可给全局 lower；但固定 p、kernel fibre、终时或 grain labels 后没有自动 lower。带权 g 的不等式须以原总 incidence 为分母，不能将几次 Fubini 最优选择误写成同一局部 full conditional law。原 q 的 coarse coherence 仅对同 physical cube 生效，并不比较整 x2-fibre 上的 ξ。

保 whole labels 会保这些 labels 的逐管原 density；若为比较两个终时删 shading，须重新计算 per-tube/average density。任意 dominated subgraph 的质量可用 (6) upper，但反向图密度与 fibres lower 不由这个 upper 产生。两时刻输出在 Y 中可恢复变量，未必减少其 joint cover；本例逐项展示了这一点。

现已实际全文读 root10 与 A8。root§6/A§7 用同一原图排除完整 common-kernel 的 gamma>1/2 子范围：KT×slab 对 fixed(p,t,s) 给 K D(delta/ell)^(2gamma−1)，good pair 至少一支 ell≥c q rho sigma；delta/(q rho sigma)为固定正幂，余一终时只付 m，自原tuple lower即矛盾。它依原19.4和全部source，未预设rational或smooth，也没有从 R70搬结论。原本matrix范围是0<kappa≤2、0<gamma≤1；小gamma不能删掉。本稿负责的局部反攻与此子范围正证相容。

仍未由全 Def17 得到足以支付 R59 的 basicness/典型 fibre lower，也没有对全正 kappa 的排除。依已锁 spec，当前仅排 gamma>1/2 子范围而未付其余范围/basicness，主机制归 no-information并冻结；不续 mask 参数、更多 fixed times 或 generic inverse 名称。本模型仅作为该停止所依据的一项严格局部反攻，不新增数学 ID/major，不降低长期 Goal。最终独审与具名输入范围另记正式 review。
