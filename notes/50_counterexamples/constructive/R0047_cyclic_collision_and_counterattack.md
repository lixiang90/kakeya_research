# R0047：真实四循环的碰撞、可完整排除的子类及一般门槛

2026-10-17，`lifting_obstructions`。已运行恢复入口并读 R47 working spec、R46 macro/next。仅编辑分配文件，不操作 Git 或新增代理。本轮目标为固定四循环真实构造的 uniform log lower 或同一正幂的无穷尺度 upper；以下没有证明一般 CYCL，也没有构造高维 Kakeya 反例。未经外部同行评审。

## 1. 对象、原质量和闭包

令 `delta=1/N`、`D_N={0,...,N-1}/N`、`A` 遍历完整 `D_N^4`，四个任意表 `b_i:D_N->[-1,1]`，下标模4。真实截面为

`X_i(A,t)=t a_i+b_i(a_(i+1)), 0<=t<=1`，

`K_N={(t,X(A,t)):A in D_N^4,0<=t<=1}`。

每一条是真实 wholeclock segment，方向网与 prior 均为原满笛卡尔网格。任意方向删选不保 full product，时间删选不保 wholeclock，故下面的全网推导不能免费传到任意 dense shading；平均密度也不等于逐管密度。该类不包含任意 intercept `B(A)`，也没有给旧全称 CP/PM 所需闭包。反向旧 positive-power 估计也不自动给所问 uniform log 下界。因此不以旧正幂等价重命名本轮。

`TC(A)=0` 但各 intercept 依赖另一个独立坐标，条件熵之和可达 `4log N`。直接重用 R41 的 `exp(-S)` 只给弱下界。任何证明必须使用本轮更具体的循环依赖；大熵本身不是压缩证明。

## 2. 从原 pair 碰撞到真实连续体积

在每个 `t`，令 `mu_t` 为原 `N^4` 个截面点的均匀概率，各点再卷积边长 `delta`、中心在零的四维 cube 的均匀密度。于是 `int mu_t=1`。该 cube 的欧氏半径是 `delta`，所以 `mu_t` 支撑在原 `N_delta(K_N)` 的同一时间截面；没有插值或虚拟填充。

记原有序方向 pairs 的碰撞数

`C(t)=#{(A,A'): |t q_i+beta_i|<=1, i=1,...,4}`，

其中 `q_i=N(a_i-a_i')`，`beta_i=N[b_i(a_(i+1))-b_i(a'_(i+1))]`。两个 cube 均匀密度的内积至多 `delta^-4` 乘四个上述 indicators，因此

`int mu_t^2 <= N^-4 C(t)`。 (1)

在 `I=[1/2,1]` 对 `mu(t,x)=mu_t(x)1_I(t)` 应用 Cauchy–Schwarz，原总质量是 `1/2`，得到

`|N_delta(K_N)| >= N^4/[4 int_I C(t)dt]`。 (2)

这是合法的 wholeclock 邻域体积 lower certificate；`C(t)` 使用 upper 只使所得 lower 更小。它不是从有限时间采样得到 volume upper。反过来，即使 CYCL 成立，也没有仅凭 Cauchy 反推出这一特定 `L^2` energy upper；该 certificate 是充分方法而非已付双向等价。

## 3. 精确四循环 transfer 与时间 cell 上包络

先给一般实数表的有限公式。令 `Q` 偶数，`j=Q/2,...,Q-1`，`I_j=[j/Q,(j+1)/Q]`。定义非负矩阵，row/column 均由 `-(N-1),...,N-1` 编号：

`M_(i,j)[q,q'] = #{(u,v) in {0,...,N-1}^2: u-v=q', |j q+Q N[b_i(u/N)-b_i(v/N)]|<=Q+|q|}`。 (3)

若 `t in I_j` 且原 row-i 碰撞 `|t q_i+beta_i|<=1`，则 `|j q_i+Q beta_i|<=Q+|q_i|`。原坐标 pair `(a_(i+1),a'_(i+1))` 被 `(3)` 的 column `q_(i+1)` 计一次；四个坐标 pair 独立计数，循环相乘得

`C(t) <= tr(M_(1,j)M_(2,j)M_(3,j)M_(4,j))=:C_j`，`t in I_j`。 (4)

这不是假定四个输出独立；正是原 full-grid pair 集合的精确计数 factorization。代(2)得

`|N_delta(K_N)| >= Q N^4/[4 sum_j C_j]`。 (5)

当 `b_i(u/N)=k_i(u)/N`、整数 `|k_i(u)|<=N` 时，预计算 histogram

`H_i[q',d]=#{(u,v):u-v=q', k_i(u)-k_i(v)=d}`。

对 row `q`，允许的 `d` 区间是

`ceil((-Q-|q|-jq)/Q) <= d <= floor((Q+|q|-jq)/Q)`。 (6)

下端准确为 `-floor((Q+|q|+jq)/Q)`，负数也须使用数学 floor；与 `[-2N,2N]` 相交后可用 histogram 的 prefix sum。此离散优化仅用于已给整数表的实验，不把任意表的 round 免费当同厚度 volume upper。

完整 uniform CYCL 的一个充分新估计会是对所有原表证明 `sum_j C_j<=C Q N^4 log(2N)^A`；本稿没有该估计。把每张矩阵先独立取范数会丢弃循环共同 clock 的 dilation 关系，不能以一般矩阵范数名称替代这个缺口。

## 4. 一般 reconstruction：低 palette 真子类与基线

设 `L_i` 为 `b_i(D_N)` 占用的半开 `delta`-bins 数。固定 `t in[1/2,1]` 和一个四维 output `delta`-cube，先选择 `b_i(a_(i+1))` 所在 bin，共 `L_i` 种。row i 于是把 `t a_i` 限在长度 `2delta` 的区间，故 `a_i` 只有绝对常数种。

一旦 `a_i` 精确给定，真实 lookup `b_(i-1)(a_i)` 已知；row i-1 将 `a_(i-1)` 限定绝对常数种。继续沿逆循环恢复其余三个值，最后那一 row 只作检验，不增加 choices。故每个 output cube 至多 `C L_i` 个原方向，四个 i 均可选择，得到 occupied cubes 至少 `c N^4/min_i L_i`。

每个 occupied cube 内取一个真实截面点，整 cube 在其 `2delta` 球内。对 `t in[1/2,1]` 积分因此给

`|N_(C0 delta)(K_N)| >= c/min_i L_i`，`C0>=10`。 (7)

它完整适用于任意 rough 表，不需要 smoothness、变换 prior 或边际体积相乘。某个 palette 是 polylog 时确给 CYCL 子类；一般 `L_i<=2N+1` 只回 `c/N`。这不是一般目标的解决，也不因给 palette 加新阈值续开下一轮。

同一个基线也可由(3)看出：当 `Q=N`、`j/Q>=1/2`，固定 column `q'` 和一个原 `(u,v)`，可行 row `q` 只有绝对常数个；每 column sum 至多 `CN`。四乘积的每 column sum 至多 `(CN)^4`，trace 至多 `C N^5`，故(5)仅给 `c/N`。真正需要的是平均于原共同时间的额外控制，不能把这种逐时基线称为 log 增益。

## 5. 两种完整的 constant-volume 子类

**单调负反馈。** 若每个 `b_i` 单调（允许弱单调），赋方向符号 `s_i in{+1,-1}`，且 `product s_i=-1`，则每个 `t in[1/2,1]` 的原 `N^4` 个 output points 在 `ell^infinity` 中至少 `delta/2` 分离。

证明假设两个不同原方向的四个 output 差都严格小于 `delta/2`。若某 `a_i=a_i'`，则前一 row 的 intercept 差为0，故 `t|a_(i-1)-a'_(i-1)|<delta/2`；网格间隔和 `t>=1/2` 迫该坐标也相等，逆循环迫全相等。若某 intercept 差为0，同样先迫对应方向差为0。余下所有方向差/intercept 差均非零，且 `t|a_i-a_i'|>=delta/2`，所以 row i 的两项必须异号。

由单调性，`sgn Delta b_i=s_i sgn Delta a_(i+1)`，故 `sgn Delta a_i=-s_i sgn Delta a_(i+1)`。乘四式得 `product s_i=+1`，矛盾。于是分离成立。中心边长 `delta/2` cubes 的内部不交，单时总体积 `N^4(delta/2)^4=1/16`，欧氏半径 `delta/2`；时间积分给 `|N_(C0delta)K_N|>=1/32`。

**任意一表常值。** 不要求其余三表单调。row i 先迫 `a_i=a_i'`，再逆循环与上一段同样恢复，仍是逐时 `delta/2` 分离和下界 `1/32`。它也被(7)覆盖，但这里给出更准确的常数。两段都保原满方向网和全部 clock，不是仅单 tuple 的形式校准；只排这些构造子类。

## 6. Affine 子类、临界单时与非法插值

若四表各为 `b_i(a)=alpha_i a+beta_i`，原取值范围给 `|alpha_i|<=2/(1-delta)<=4`。连续参数 `a' in[0,1]^4` 的截面是矩阵 `tI+P_alpha` 的平行多面体，`P_alpha` row i 的非零项为 column i+1 的 `alpha_i`；其 determinant 是 `t^4-product alpha_i`。

对每个 `a'` 复用所在网格 cell 的代表 a，此处整个 affine 截面（含 intercept）与原有限截面距离至多 `(t+max|alpha_i|)||a'-a||<=10delta`，确被题设固定厚度包含。故实际五维邻域有下界

`int_0^1 |t^4-c|dt >=3/16`，其中 `c=product alpha_i`。 (8)

最小值在 `c=1/16`：对 `0<=c<=1` 积分是 `1/5-c+(8/5)c^(5/4)`，其最小为3/16；区间外更大。这证明任意 bounded affine 表不能给本题幂次体积压缩。

同时 `b_i(a)=-t_0 a`、固定 `t_0 in(0,1)` 在单时 `t=t_0` 有矩阵 `t_0(I-P)` rank3，全部输出位于有界三平面，其 `delta` 邻域的四维体积为 `O(delta)`。这说明逐时 constant lower 是假的，但全时(8)仍成立；不能以临界时刻证明 asymptotic power upper。

任意 rough 表的线性/平滑插值则不满足上述误差：相邻 grid slopes 的 intercept 跳跃可为常数，插值产生的新 segments 可能远离原 `C0delta` 邻域。对插值 derivative 写 `det=t^4-product b_i'`，再以面积公式或 topological degree 处理，不能免费回传原 finite union；即使有 determinant 积分 lower，还需 multiplicity upper。这里仅对误差已显式支付的 affine 表作了填充。

## 7. 有限证书及本轮未解决项

root 的 `R0047_cyclic_continuous_volume_certificate.py` 使用(3)–(6)在50个明确有限族计算真实连续体积 lower certificate，不是 volume upper。已独立读程序：matrix row 为当前 q、column 为下一 q；histogram 的坐标 pairs 恰各计一次；floor/ceil 与 prefix 的 inclusive endpoints 正确。每个非负矩阵乘积 entry 计至多相应 partial coordinate pairs，二/三/四乘分别至多 `N^4,N^6,N^8`；trace 的和也由全部原 direction pairs `N^8` 控，故 `N<=64` 的 int64 安全。总和改 Python integer，最终 lower 为准确 Fraction。N=4 的 direct-pair 检验不使用 histogram/trace，正核同一个连续 cell 上包络。

完整一般 CYCL 所需的 uniform time-integrated collision 控制仍未证明；也没有同一正 `kappa` 的无穷尺度真实体积 upper。上述 palette/符号/affine 子类是完整真实排除，但并不覆盖任意四表。一般 cut-cycle reconstruction 仅给 `N^-1`，不能用它宣布主候选成功。若整轮仍没有越过这一步，按 spec 宏观停止循环施工，不换循环长度、alphabet 或新熵阈值继续；高维/一般 Kakeya 目标保持 active。
