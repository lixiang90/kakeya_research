# R0072：原双终时质量、恢复精度与局部校准正式独审

2026-10-18，B。仅写本授权 review；无 Git、spawn、metadata 或额外检索。

## 1. 实际全文读取与独审对象

fresh 全文读最终 root `R0072_kernel_velocity_two_time_budget_and_stop.md`10节、A `R0072_native_two_time_response_source_audit.md`8节、B `R0072_kernel_response_counteraudit.md`9节；阶段 I 的 A `R0072_primary_sources_and_goal_audit.md`8节、B `R0072_global_paths_and_equivalence_audit.md`7节；working spec5、macro6、next `R0072_next_full_goal_reset_after_two_stops.md`6节。另读回原 Def17.2–17.4、Lemma19.4 的 statement/相应 proof 输入及 R59 quotient/R16 linewise 范围。

本 formal 独审 A/root 的源 core、原同管多时质量、恢复、KT 最终用途及整合范围；B 自己的数字校准由 A/root 另作独立审查，本 formal 不把自审替代独立认证。三核心版本身份采用 A 本轮 fresh 原件核对，不在这里冒已重审其全部高级 wholeproof。

## 2. 原质量、两时刻与实际恢复逐式核

原 native 标签必须为 `y_s=y+(s−t)xi+[u(t)−u(s)](x1+(s−t)phi1)+O(delta)`；中心化只对固定 root 有效。最终 root/A/spec/B phase I 均已保 x1 项，不再以跨 root 的免费坐标变换抹掉它。

point/tube/厚 kernel fibre 的数量上界分别为 `K m delta^(−4+kappa)`、`K delta^−4`、`K m delta^(−3+kappa)`，原 incidence≥`K^−1 m delta^−4`。三个阈值的 peeling 各 vertex 只充电一次，合计损≤原 I/2；以 point degree upper 除 fibre edge lower 才得到 active 厚 fibre 的真实 x2-cell lower。这里固定的是 x1 的 delta-bin，不是没有依据的 exact Cartesian fibre。

active tube 有≥`K^−C m`个 visits 后，同一管 root加两终时为 `sum_T n_T^3≥K^−C I m²`。原 δ-clock packing 可删短时间；具名19.4在原完整配置、原窗分母和 absolute heavy-time 下给 u-ball cap，再删近 u 对。两次均可在 η最后小的顺序内保固定比例；不是两个 dense arms 求交。fixed root incidence 与 fixed terminal pair 的 domination 分别由 `n_T²≤Km²` 和 `sum_T n_T=I` 重算，未授给任意条件图。

恢复只需 `|u(s2)−u(s1)|=d>0`，不要求 rank2；精度为 `err(phi1)≤C e/(q rho d)`、`err(xi)≤C e/(q d)`。第二式使用同窗 `|u(t)−u(s_i)|≤C rho` 和 `d≤C rho`。若同要 rho 精度，必须保 `e≲q rho²d` 及 fine delta floor，不能由粗 rho² 标签无损声称。恢复没有恢复 x2、phi2，更没有产生 R59 典型 invisible fibre lower。以上原量纲、重数及分母通过。

## 3. KT/角 slab 的真实正结论与未闭合区间

fixed(p,t,s)的输出沿长度 `ell≈|s−t||u(t)−u(s)|` 的线段变化。原 Y 的 tube-KT 给 `K(ell/delta)^(1−gamma)`个细 output cells；每个 cell 的 phi1-strip 宽 `O(delta/ell)`，原 point slab 给 `K D0(delta/ell)^gamma`根角/管。phi2仍包含在 D0 中，fixed fine角穿 p 的管碰撞为常数。因此 actual selected visits 的 upper 是

    K^C D0 (delta/ell)^(2gamma−1)。

good 同管 pair 至少一终满足 `ell≥c q rho sigma`，另一个终时仅付 m。取 `sigma=rho^(1+b0)`、`q=delta^b1`、`b1<(2−b0)/8`，原 `rho≥delta^(1/4)` 给 `delta/ell≤C delta^c0`，`c0=(2−b0)/4−b1>0`。KT宽度、line长及 slab查询均在原 base 范围内，O(delta)误差/端帽只需固定邻格。与第2节 lower 比较，固定 gamma>1/2 后 η最后小得到矛盾。

所以在具名19.4与全部原 Def17 条件下，**完整 common-kernel 的 gamma>1/2 子范围排除通过**。这是本 source 的独立计算，不借 R70 mixed43 范围；正确参数为 `0<kappa≤2、0<gamma≤1`。Phi AD/slab另给 `gamma≤kappa+O(eta)`，所以这一结果落在额外 kappa+gamma>1区间，不能替代全参数目标。

对 gamma≤1/2，当前 upper 没有正 saving。两 terminal Y 的允许 product cover仍可为 `K(R/e)^(4−2kappa)`，投影 Y 可满一维；同一 phi1 law不能独立相乘两次。root/A正确没有从 upper不足断言 actual outputs 必然大，亦未从数值可逆性推出 basicness。

## 4. 局部校准的保真、碰撞及严格限制

root/B 的5周期有限构造逐位恒等式保真实实数加法。b为20倍、B=2^b，近满 X 的亏损16/b可任意小；自由角维数 `(1/5−2/b)+(11/20+2/b)=3/4`，slab可取 gamma=1/10。digit response的像维数 `13/20+3/b`，字母均匀 preimages 保原计数 law。首位整数差大于所有后尾部给真 Lipschitz与 coarse coherence；不是 full-grid 不连续 mask。

`a1=x1+phi1、a2=x1+2phi1` 的逐位表保证两个 terminal carriers维数 `(3/5−3/b)+(13/20+3/b)=5/4=2−kappa`，并以坐标截面数出 tube-KT exponent≤9/10。fine δ=h/B⁴的固定 buffer 已补，所有线性缩放后的 literal δ分离与 AD/KT base 只损 B 相关常数；N最后足大吸入 δ^−eta。原物理 clock 的两时刻、真实同一单位轴和实际 initial angles 均保，不是 formal endpoint等式。

同一 terminal物理点固定 a1/x2/phi2而多值 a2时，normal物理斜率相同但 phi1不同；一个 terminal selected xi要同时满足 `xi_initial=xi_terminal+u(s1)phi1+O(delta)` 不可能保全部变化。root/B明确这个冲突。模型也不保 full Z、全部 y/grains/terminal point Φ、whole T joint4AD/CW和跨time union AD；B更明确所有轴位于 physical y1=0所以 CW至少 delta^−1。故它只反局部 density/Lip及两个 marginal carriers→basicness跳步，不反完整 source/Kakeya。任意 dominated 保质量子图的 response-bin下界有真实原 reference，未把该 toy 的 g=1搬成 fullsource 质量。

## 5. 修订、具名依赖与当前必修项

本次实际核到并已修的责任包括：native x1项及只固定root中心化；不得挪 R70 的 `kappa≤1、gamma≤1−kappa` 到当前 matrix source；局部构造的 fine δ分离 buffer；terminal轴线穿点不等于原 selected incidence。B phase I 的结构式和第二阶段原误措辞也已读回修订。**当前无尚待强制修改的数学项。**

19.4 的全 proof保具名输入；原 Def17 配置存在/已审 tuple工具、OAI4/DIR 等既有输入保持各自原范围，本轮没有新独证其所有高级 wholeproof。A三核心 current身份与文献有限筛查只能说明实际所读版本/statement范围，不认证全文正确、穷尽优先权或新颖性。formal不认证未来 metadata、registry、Git、safe sync 的执行结果。

## 6. 限定通过与停止结论

root/A 的原 same-tube质量、恢复及 gamma>1/2 子范围排除在上述具名条件和最终修订范围内通过；局部反攻只在明确保留的有限数据上通过，不能升级全源反例。**选定的 ξ-basicness/商3AD-lower 或完整正 kappa 排除仍未实现。**按数学前已写停止条件，主机制应记 no-information并冻结，不因 proper 子范围改写为完成；不续 mask/多 fixedtimes/Markov-BSG/packet阈值。

macro与next正确保完整 ordinary/general、其余 matrix/mixed、general-to-sticky/Hausdorff和真全方向构造 open，R73先完整宏观后锁不同实际数学；不把终点 ξ碰撞重新命名即开同一方向。无 ordinary新界、newID、major、优先权或 Goal完成认证。以上为内部逐步独审，**未经外部同行评审**。
