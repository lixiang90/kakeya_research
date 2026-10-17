# R0063：同轴三维载体求和与真实 planebrush 插入

2026-10-18，root 整合稿。周期 macro/working_spec 先保存，独立 formal 结论以本轮 reviews 为准。使用 R60 所列具名三维强临界输入；未经外部同行评审，不认证新颖性、重大性或 ordinary 高维界。

## 1. 问题和输入范围

本轮不重开射影 gain。检验的是一个真实物理重叠步骤：同一个 affine 二维脊 Pi 上的三维 carriers，其局部三维界能否合法相加，以及 Katz–Zahl v3 Lemma30 是否确有这样的原管子族。W(T) 是方向盒，不能直接作为 affine carrier。以下先完整证明模型，再单列源映射；源中未给的假设不能补作结论。

具名输入是 R60 主稿 §§1–12 已审桥：固定 n>=4、任意 affine 三维 S，原 unit delta tubes 整轴在 N_(Cdelta)S 内，权和 W、每 C0delta 方向帽权<=alpha，任意 Lebesgue 阴影平均 lambda，则

    |union Y_i| >= c_e delta^(n−1+e) lambda^3 W/alpha.       (1)

同一证明若原 indexed 族有 absolute PW 系数 K，则 (1) 的 alpha 可替 K，见 R60 §12。系数统一于 carrier 的位置/方向，格式固定。这个局部定理是既有输入闭包，不新登记 ID；OAI3-critical/KR/Paw 的高级 wholeproof 层次不变。

## 2. 同轴模型的完整量词

固定 n>=4、R,C,C0、e>0，d=n−3。Pi 是 affine 二维平面，所有集合在 B_R。Sigma_j=Pi+ell_j 为包含 Pi 的 affine 三维平面；ell_j 是 Pi 正交商空间里的无向一维方向，彼此 projective angle>=h，delta<=h<=1。每根原 unit delta tube 只分到一个 j，整轴在 N_(Cdelta)Sigma_j。原方向帽权上界 alpha 对全族统一；重复原 labels 不合并。令 W=sum w_i>0、V_delta 为每管相同实际体积、I=sum w_i|Y_i|=lambda V_delta W>0，Y_i 为任意可测阴影。

先假设每管 |proj_(Pi-perp) v_i|>=a>0。要证

    |E| >= c_e delta^(n−1+e) lambda^3 W/alpha
                   * min{1,h a lambda/delta}^d,             (2)

E 为真实原阴影并集。全族 absolute PW 输入替代方向 cap 时，(2) 中 alpha 可替 K。lambda 是平均密度；不需原逐管 density，不需 two-ends 或任意权跨度上界。

## 3. 脊截断：对真实管体积没有 delta 地板

取单位 l=proj_(Pi-perp)v/|proj_(Pi-perp)v|。将包含 round-ended tube 的直圆柱写为 x=x0+s v+z，z perpendicular v、|z|<=delta，s 在长度 1+2delta 的区间。dist(x,Pi)<r 蕴含 |l dot (x−p0)|<r。对每个固定 z，这把 s 限制在长至多 2r/a 的区间。Jacobian=1，积分并用 V_delta comparable delta^(n−1)，得

    |T_i intersect N_r Pi| <= C min{1,r/a} V_delta.        (3)

因此 r=c a lambda、c 足够小，使全体被删 weighted incidence<=I/2。令 Z_i=Y_i outside N_r Pi，I_Z>=I/2。此结论即使 a lambda<<delta 也成立：把 tube 粗略投影到轴后写 (r+delta)/a 会失去这项精确 Lebesgue 信息。没有把截断后的每管 density 宣称为原 lambda。

## 4. 同一物理点的 carrier 重数

若 x in N_(C+1)delta Sigma_j 且 t=dist(x,Pi)>=r，则 quotient 向量 z=proj_(Pi-perp)(x−p0) 的长度 t，其与 ell_j 的角<=Cdelta/t。RP^(n−3) 上 h-separated 点在此角帽中至多

    M_r <= C [1+delta/(h r)]^d.                           (4)

当 delta/t>=常数，整个 projective 空间的 h^(-d) packing 也被右边控制，因所有 t<=C_R。故 (4) 对全部 r>0 有效。每个 tube 在对应加宽 carrier 内，故 (4) 也控制这些 packets 的真实 Z_i 并集的 multiplicity；没有数 tube 的点重数。

## 5. 所有 packets 相加，保平均密度

记 W_j=sum_(i in j)w_i，I_j=sum_(i in j)w_i|Z_i|，lambda_j=I_j/(V_delta W_j)，空包略去。用 (1) 各自 lower 和 (4) 的 overlap upper，

    M_r |E| >= sum_j |union_(i in j) Z_i|
             >= c_e delta^(n−1+e)/alpha sum_j W_j lambda_j^3
             >= c_e delta^(n−1+e)/alpha * I_Z^3/(V_delta^3 W^2).

最后一步是 weighted Jensen，I_Z>=I/2 给 (2)。整个过程不挑单一 density 层，不先假定所有 packets 的 lambda_j 下界；允许全部权跨度和零阴影 labels。absolute PW 版同理，因为原 upper 对任意限制族及每一个固定格式 carrier 测试继承，不重归一原权。

## 6. 一般维度的自动角删选版本

取 h=delta，Q=delta^(n−1)W/alpha<=C（全方向帽覆盖）。不预设 a；每个整轴只需近某个包含同一 Pi 的三维 affine plane。取 quotient 的 maximal delta-net，把原 carrier 移到最近 net plane，因 bounded domain 整轴误差仍 O(delta)，每根只分一次，不添 labels。

方向帽 packing 给 angle(v,Pi)<a 的管总权<=C alpha delta^(1−n)(a+delta)^(n−2)。若 lambda Q>=C delta^(n−2)，选 a=c(lambda Q)^(1/(n−2))，删掉这些管至多 I/4；保留族的原 I>=3I/4、总权<=W。再以原 lambda 为截断尺度应用 §§3–5，而不是把保留族平均下界当逐管。得到

    |E| >= c_e delta^e
       lambda^[3+(n−3)(n−1)/(n−2)]
       Q^[1+(n−3)/(n−2)].                                (5)

lambda Q<=Cdelta^(n−2) 时，右边<=C delta^e lambda^(n−1) delta^(2n−5)<=C lambda V_delta（n>=4），由 |E|>=I/W=lambda V_delta 即付。固定参数边界用常数合并。n=4 时 (5) 为 delta^e lambda^(9/2)Q^(3/2)；n=5 时为 delta^e lambda^(17/3)Q^(5/3)。当 Q 和 lambda 均只有 subpower 损失，这是该强结构类的满维单尺度估计；一般原 Kakeya 族并无共同 Pi，不能据此提升 ordinary 界或跳到 Hausdorff。

## 7. 独立反攻与损失校准

B 给出合法模型：delta<<lambda、h>=Cdelta，取 quotient 半径 cdelta/lambda 小 sector 中 h-separated carriers，J comparable (delta/(h lambda))^d；每个 carrier 内选避开 Pi 的 delta-separated 三维点刷方向，所有轴过同一脊点，权1，阴影取中央长度 comparable lambda 的真实段。相邻 carrier 实际按 h 分离，因 h>=Cdelta 故至少常数倍 delta；固定着色/加大网距可使全 ambient directions 仍 Cdelta 分离。W comparable Jdelta^-2，a comparable1，全部 E 在某单 Sigma0 的 Cdelta 邻域与 C lambda 球中，故 |E|<=Cdelta^(n−3)lambda^3。

(2) 的 factor (h lambda/delta)^d 恰好取消 J，使两侧主幂一致。于是这个求和架构的 overlap/density 费不能在全模型免费删除。此例不是 full KZ source、PW4 或 Kakeya 反例，也不认证全部 lambda 指数最优。

## 8. 原 R4 预处理下的 light-label 修补

以下采用 KZ Lemma30 的 theta 尺度及原编号。用 L>=1 统一记录固定幂 C_i、log(theta) 和 theta^(-c epsilon4) 损失，每步允许增大 L。原族记 N0、Omega0、lambda0，A0 comparable N0/|Omega0|。预处理族记 lambda1=lambda_(Y1)、mu1=mu_(Y1)、N1=|T1|。源 (37) 给每管 m comparable lambda1/theta 个 Y1-cubes，点度上界 dmax<=B mu1，B=C2 theta^(-epsilon4)；R1 comparable N1 m^3 mu1。

这里将源声称的 R4 预处理作为明确具名输入：同 W 的两臂及全部端点构成 R4，|R4|>=L^-1|R1|，每 tube 唯一归包，Y2 packets 的物理并集两两不交。不是宣称本轮独证整个 Lemma30。特别地，源 (63) 字面为完整 Y1 packet 并集的求和比较；前一全局 pair-moment lower 单独不足以用普通 Cauchy–Schwarz 推出这种支持集比较，一般 occupancy 矩阵可反攻。此提示不是完整 source 反例；本桥不调用 (63) 的 whole-Y1 求和形式，而直接明列所用 R4/disjoint 预处理责任。

令 q_T=#Y2(T)。删去 q_T<tau m 的全部 labels。坏 T 作第二臂时，固定 T 的 tuple 数至多 m dmax q_T^2；作第一臂亦同。因此两臂删除合计至多

    2m dmax sum_(q_T<tau m) q_T^2
       <= C tau N1 m^3 dmax <= C tau B |R1|.             (6)

取 tau<=c/(LB)，剩余 R4 仍保常数比例；每保留 tube 的完整 Y2(T) 有 density>=tau lambda1，而不是免费宣原 lambda1。这个 tau 损失可收入 L。重新按源 R5 取富 Q0，再对 W 重取 R6：每存活 W 内 Q0 的 tuple 数至少 L^-1 m^2 mu1^2。各单管原 tuple 上界<=C m^3 dmax，故新 T3 至少 L^-1N1 个 labels，每方向至多 CA0 个，覆盖至少 L^-1N1/A0 个方向。一般 shading refinement 不自动保 N1 comparable N0；不借源 (65) 将这项偷换成全原 |Omega0|。源方向盒尺寸 1 by p by q、q=Ltheta/rho，因而 rich W 数至少

    #W_rich >= L^-1 N1 theta^2 rho/(A0 p).               (7)

所有重取只删原 labels/原 cubes，disjoint 性、上界和几何分离都继承；lower 的损失已在 (6) 重付。无需 whole-Y1 各包并集不交，也不使用无证的 Y3 逐管 density。

## 9. 固定富 Q0 的真实共同脊及备用估计

T 经过 Q0,Q' 且方向在 Pi(Q0) 的 Otheta 邻域，因此 Q' 距 affine 脊 Pi_Q0（过 Q0 中心、方向 Pi(Q0)）为 Otheta。T' 经过 Q'，定义 Sigma=Pi_Q0+span(v(T'))，则整根原 T' 轴在它的 Otheta 邻域。没有平移原管或原阴影；也不需借 (48) 的辅助 L' 去付 clock 误差。不同 T' 分到 quotient theta-net，每 label 一次。

KZ Definition5 的阴影是与原管相交的完整 theta-cubes，并非原管实体的子集。这里保持所有原 Y2-cubes 不动，用同支持轴、固定半径 Ctheta 的包络管覆盖它们，必要时共同长度仅延固定 Otheta；密度/真实体积只变固定常数，原 theta 方向帽仍只需有限 cover。模型尺度为常数倍 theta，carrier net/overlap 亦只变常数。没有把原 cubes 再填厚。此 A0-cap 应用不要求包络 PW。

源 (70) 从 (42),(43) 给 angle(T',Pi_Q0)>=p/L；只有分离量大于 Otheta 几何误差的分支才用它，其余退回原 Lemma30。每 T' 的 (T,Q') 数<=L p^-1，每 T' 的 Q'' 数<=C m，故参与该刷的 distinct labelled tube 数

    M_W >= L^-1 p lambda1 mu1^2/theta.                    (8)

给这些 labels 使用刚才保留的完整 Y2(T')，逐管 density>=tau lambda1，方向帽权<=CA0。用 (2)，a=p/L、h=theta，并将 tau 收入 L 得

    |union_(brush W)Y2| >= L^-1 theta^(2+e)
                                  p^2 lambda1^5 mu1^2/A0. (9)

不同 W 的这些原 Y2 unions 实际不交。由 (7),(9) 相加，令 U1=|union Y1|，得到

    U1 >= L^-1 theta^(4+e) N1 rho p
                                      lambda1^5 mu1^2/A0^2.

再用 mu1 U1 comparable lambda1 theta^3 N1，得到独立审查所需的完整备用式

    U1^3 >= L^-1 theta^(10+e)rho p lambda1^7 N1^3/A0^2.   (10)

由真实 incidence refinement 有 N1lambda1>=L^-1N0lambda0，且 lambda1>=L^-1lambda0，所以 lambda1^7N1^3>=(L^-1lambda0)^4(L^-1N0lambda0)^3。这把 (10) 转回原参数，右侧为 L^-1theta^(10+e)rho p lambda0^7 N0^3/A0^2。

若原实体管另有 absolute PW 系数 K，不需也不声称加宽包络有全 PW。直接检验所需的三维凸浓集：固定 carrier Sigma_j，令 P_i 是包含投影包络的固定长度、半径 Ctheta 三维管。P_i subset convex U 时，原完整实体 T_i 在 H=N_(C'theta)Sigma_j intersect projection^(-1)(Q_U) intersect B_(C_R) 内，Q_U 是 John 外接 box，|Q_U|<=C|U|。此 H 固定格式、|H|<=Ctheta|U|，原 PW 以占比1 查询给数量<=CKtheta^-2|U|，故 indexed projected D_j<=CK。再用真实 Y2 的 normal-fiber levels 即得 (9) 以 K 代 A0、(10) 分母 A0 K。这个特定测试桥不授半径加粗后的全 fractional PW。

上述是从明确 R4/disjoint/angle/方向盒输入推导的桥，并未把这些 source 预处理的 wholeproof 全部独证。Lemma30 本身不假设 PW 输入，coarse/fine K 不免费传递。低分离分支仅保旧界，不声 (10) 对它无条件有效。

L 的压记可以展开：若 R4 原质量比例为 zeta，q<=L_q theta/rho，a>=p/L_a，(T,Q') choices<=L_path/p，dyadic W 选择层数 L_W，则整桥 prefactor 可取 c zeta^6/(L_W B^5 L_q L_a L_path)。源给这些量的 log、C_i 固定幂及 theta^(-C(epsilon_i)epsilon4) 范围，才允许先固定 epsilon_i 再取 epsilon4 足小收入 target e；本稿没有把 L 置为 uniform 常数。

## 10. 与旧估计的真正差别及边界

旧 (74) 在原参数的立方主幂为 theta^2 lambda0^4 (theta^3|Omega0|)(theta^3 N0)^2，即 theta^11lambda0^4N0^3/A0。(10) 转回原参数后，比它多因子 lambda0^3 rho p/(A0 theta)。只有该比值留固定正幂时才改善该分支。源没有统一给这项，rho 的 (49) 是 upper 而非所需 lower；A0 也不能去掉。PW 版倍率是 lambda0^3 rho p/(Ktheta)，方向计数中的 A0 未凭空消失。方向盒的 q comparable Ltheta/rho 不是物理 carrier 厚度，不能把 q/p 强行变成所需额外信息。

因此一般 planebrush 不能仅凭‘三维已经解决’直接升级到全局新界。本文不是只调源常数：确切新输入是完整三维临界估计与物理 carrier overlap；但它对所有源数据是否留下固定幂，尚未证明。不得用未证明的 good-carrier 或 rich-W 质量假设认证普通四/五维结果。

## 11. 闭包与冻结规则

restriction/shading 仅继承方向 cap 或 absolute PW upper，lambda/I 必须重算；模型以平均质量完整支付。局部 (1) 是 R60 闭包，(2)/(5) 是附加强结构的应用，不等价于已经冻结的全 PW4/projective gain；反之一般 gain 并不提供共同脊。当前源备用式是否严格强于旧式只看实际费用和量词，不登记新 theorem 名称。

停止模型的 h/lambda/a 常数优化及此源分支的参数迭代。已支付 R4 后 light-label 及真实共脊的桥；完整 source gain 仍无统一 ratio lower，不能宣新维数。一般维度结构类的实际数学已完成，不以接口说明结案。后继必须改变真实非同轴/多尺度兼容信息，而非把 (10) 所需 ratio 改名。

## 12. 审查与长期状态

A 审实际 KZ 源和原 label 责任；B 独证模型、平均截断与 n 维角删选，并给 overlap 饱和校准。root 整合后两正式全文互审。文献搜索只作 bounded primary 比较：已存 KZ v3/Choudhuri 2610v1；新查有限域 planebrush 2507.09605 的摘要，仅比较域范围，未采用其证明、不新下载作为输入。没有 ordinary 维数增益、重大/新颖性认证或目标解决，Goal active。

另实际比对已存 Wang–Zahl2502v1 Theorem1.2：其三维 CW 结论已有 delta^e lambda^K（K依e）的下界。故共同脊结构类在 near-full density 下的满维应用，不能仅因本轮推出便称重大新结果；本稿的具体全密度立方费用和索引/平均量词使用 R60 的更强具名输入。没有完成所有相关文献的优先权排查。
