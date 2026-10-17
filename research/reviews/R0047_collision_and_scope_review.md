# R0047 独立审查：循环碰撞、实际体积与停止范围

2026-10-17，`lifting_obstructions`。结论：root/A、macro 和 next 的明确范围通过内部独立逐步审查；未经外部同行评审。一般 CYCL 未证，未得无穷尺度统一 power upper，没有 Kakeya 反例、新高维界或重大结果。

## 1. 实际阅读与验证范围

已实际全文阅读 root `R0047_cyclic_actual_volume_and_closed_loop_boundary.md` 八节、A `R0047_cyclic_geometry_and_primary_audit.md` 十节、`R0047_macro.md` 八节及 `R0047_next_HRZ_finite_seed_interface_gate.md` 五节；自己的七节反攻稿不计独立证书。已读完整实验代码，并对完整 JSON 的50个 records 逐项解析核对，而非只看工具显示的截断片段。

只读独核全部已存 maps 的长度/整数界、每个 time-cell count 的合法范围、总和、精确 Fraction、显示值和 source SHA256。JSON 的 SHA256 为 `15827ba14f66084d9c2bf79ef6cbcd8b8a0fa878596086d8ad2fdc68407f9ffb`。没有无故重跑整组实验；N=4 direct-pair 校验是 root 已实际运行并保存的独立计数方法，代码及其对应范围已审。

## 2. 完整原族与可证明的子类

全 `D_N^4` 的 uniform law 及 wholeclock 是实际输入，不是从任意 restriction/shading 免费恢复。`TC=0` 不消去可达 `4log N` 的 `S`，所以 R41 small-S 结论不直接解决本模型。反向本受限放置类不含任意 intercept，也无旧 CP/PM 的所有删选闭包；未付双向正幂等价，macro 的排重范围正确。

palette 计数的精确 `135L` 正确：第一个 bin choice 后 interval 长至多 `4delta` 给至多5个 grid 值，之后三行各至多3个；最后剩余 row 只检验不添选择。occupied cube 直径 `2delta`，时间积分原长度为1/2，故 root 的 `1/(270 min L_i)` 是真实邻域 lower。一般 `L_i<=N` 仅回 `N^-1`；polylog palette 是明确子类，未被当成一般 reduction。

常值断环及单调负反馈证明使用输出残差 `<t delta`，一旦某个方向差为0就逆循环恢复全部值；其余情形的非零 intercept 差符号绕环迫 `product s_i=+1`，与假设矛盾。平段和任意跳跃均已处理，不需要光滑性。`t delta` separation、side `delta/4` cubes 与半个 clock 确给 `1/512`，无需边际体积相乘。

分块反序 permutation 的递增/递减子序列均至多 `sqrt N`，四表分别抽单调子表至多留下 `N^2` 方向，密度 `N^-2`。这是真实抽取费用，不能把子类定理无费推广回全网；稿件没有这样做。

## 3. Affine 与单时共振的精确几何

bounded affine 表的 `|c_i|<=4`、连续 cell 填充的 Euclidean 误差 `10delta` 均正确，题设固定 `C0>=10` 足够。连续 slice 的矩阵 determinant 为 `t^4-product c_i`，线性变换的实际体积等于绝对 determinant，奇异时刻不影响积分。全实参数上的积分最小在 `P=1/16`，值 `3/16`，因此该子类的 wholeclock constant lower 完整成立。

这不允许对任意 rough 表免费插值。表值可在一个 `delta` gap 内跳常数，新的插值 image 不在原固定厚度内；非线性 Jacobian 积分还需 multiplicity。将 simultaneous cycle 换成依次 shear 的 composition 也会改变最后一项的输入。root/A 对两种捷径的拒绝正确。

`b_i(a)=-tau a`、`tau in(1/2,1)` 在 `t=tau` 有真实 rank3，单时 occupied volume 为 `Theta(N^-1)`，故 pointwise log lower 不成立；它不反驳 wholeclock CYCL。cube 平滑密度的支撑含于三长轴固定、第四轴 `O(|t-tau|+delta)` 的 box，质量1，因此能量至少 `c/(|t-tau|+delta)`，积分确有 `log N` 必要发散。这仅排 raw 能量 `O(1)` 的过强版本，不排待证 polylog upper，也不把大能量反向当小体积。

## 4. Transfer、连续时间和整数实现

取整数方向差 `k_i`、intercept index 差 `d_i`，真实截面差为 `(t k_i+d_i)/N`。矩阵 row 为当前 `k_i`、column 为下一 `k_(i+1)`，该 column 的 histogram 恰计下一坐标的原 ordered pair。四乘 trace 每个原方向 pair 恰计一次，不是将四个输出独立化。

在 `[j/Q,(j+1)/Q]` 的任意真实碰撞满足 `|j k+Q d|<=Q+|k|`。所以代码是整个 time cell 的 upper envelope，非在 `t=j/Q` 的 quadrature。整数窗口下界准确为 `-floor((Q+|k|+jk)/Q)`，上界为 `floor((Q+|k|-jk)/Q)`；Python 对负数的 floor 和 inclusive prefix endpoints 均正确。

side-`delta` 的四维 cube density 半径为 `delta`，故平滑 support 在真实 `N_delta K_N`。L2 overlap 至多 `delta^-4`，原 ordered pair 总权 `N^-8`，于是 `E(t)<=N^-4 C(t)`。在长度1/2的整个 time-space 对质量1/2作 Cauchy，得到 `Q N^4/(4 sum C_j)`；系数与方向正确。它是实际连续 Lebesgue volume lower，不是上界，也不与 CYCL 已证双向等价。

所有矩阵 entries 非负；二/三/四乘的 entry 分别计相应 partial coordinate pairs，至多 `N^4,N^6,N^8`，trace 总数也至多全部原 pairs `N^8`。因此 `N<=64` 时中间乘积和非负累加均不会 int64 溢出；totals 和 Fraction 使用 Python integer。代码的十种具体 tables 满足原取值界，50族的有限正有理证书有效。最小 display 约 `.002463` 仅是这份有限表单的最小值，不是所有 N/表的常数。

## 5. 仍未付的闭环与停止

一般重构或逐列容量留下一个 N 因子，只有 `N^-1`；root/A 没有声称它已被消去。`t^4` 与 chord slopes 的单个形式恒等式、逐矩阵 norm 或有限数值趋势均不支付共同时间、四个差分尺度及 lookup 闭环的原质量。没有一般 trace polylog upper，也没有实际 power upper。

因此本轮退出为停止这份 cyclic construction gate，保留已证断环、符号、affine、低 palette 子类，不宣称任意循环构造不可能。冻结后不以循环长度、alphabet、正反馈子类或新 S 阈值重命名继续，符合原 spec；没有降低长期 Goal 完成标准。

## 6. 下一HRZ接口的量词

next 明确先 R48 macro/有限 primary frontier，再实际定位 HRZ 的 broad/narrow、recursive pieces 和终止位置，未假设存在可替换的4D terminal。历史 `p>18/13` 的共轭为 `18/5`，不当作2026最佳值。H5 的 `#E>=c delta^(-4-sigma+epsilon)` 是严格高于4的待证有限目标，非已得结果；额外 Hausdorff 读出及任意集合范围仍明列。

DIR/FSD 的真实方向、共同 clock、near-full shading 量词不等于完整 maximal Lp 或任意 lambda 幂，稿件明确禁止给缺少的输入添假设。曲面 flatten、短 piece 重缩、父子重复、复杂度及 eta/epsilon 顺序也都列为必须实际支付的责任。新组织是一次有界接口检验；如果只能旧 HRZ/四维投影 baseline 或需未给 maximal/flatten 输入，就一轮停止，不以 k、degree 或 radii 调参续轮。未发现当前四篇终稿的剩余必修数学或 scope 错误；停止编辑。
