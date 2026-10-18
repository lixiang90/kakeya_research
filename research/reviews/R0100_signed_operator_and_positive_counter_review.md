# R0100：signed共享clock算子与原正质量的独立终审

2026-10-19，A。以下是有限来源应用与严格反攻的审查，未经外部同行评审。

## 1. 实际全文范围与来源层级

已 fresh 实际全文读 root 主稿 notes/40_multiscale/R0100_shared_clock_annular_operator_and_positive_mass_gate.md（10节）、B 稿 notes/00_map/R0100_joint_geometry_and_full_goal_reselection.md（10节）、C 稿 notes/00_map/R0100_shared_clock_triangular_operator_gate.md（10节）、A 稿 notes/00_map/R0100_ordinary_and_source_outlet_reselection.md（8节）、两 spec 各5节及终 macro／next／source-scope／round 各6节。本人 A 的正证不是自身独审，已经由 root／B 实际全文核查；本 formal 的独立对象为 root／B／C 的完整有限链及整合范围。

本人实际读新 primary 提取的 PDF1–6：Th1.1／1.2、式(1.1)–(1.5)、完整 Lem2.1、§2.1／2.2；另实际全文读原 README。没有读取全部37页高级 matrix／heat／frequency／rough-kernel 证明，也不将 C 读过的 §8 自动计入本人读域。README 只有作者、日期和 citation，不含 Lean 或正确性认证。root 的原字节／图页校验不当作本人的新校验。

原 source Th1.1／1.2 在全文中正确标为尚未完整独证的 source claim；本项目的 Hölder／坐标应用条件于它们正确，连续反攻不依赖它们。没有把 OpenAI 署名、官方仓库或正式排版当作已经建立的数学定理。

## 2. 原声明、可测选择与无符号预算

核对 source 与 root §§2–3、C §§2–4：B_(ε,R) 对 ε<|t|<R 同时积分正负 t，kernel 为 dt/t；abs 在各 signed 积分之后。Th1.1 声每个 r>2 的 pointwise annular variation，Th1.2 声至多 N 个 disjoint positive-radius intervals 的 S_N，L^(3/2) upper 为 C√N log(2+N)||F||₃||G||₃。N 是环带数，不能换成管数或尺度比；未取 r=2 或赠其 uniform endpoint 常数。

有限积分的 common null set／endpoint continuity 由 Lem2.1 的 countable exhaustion 和绝对连续积分付齐；rational endpoints 使 supremum 可测，实端点可由连续性逼近。output-dependent intervals 和系数是源声称的真实权限，未被不必要地缩成固定 dyadic 列表；它们依然不是任意第三变量 mask。

另独核无需高级 claim 的正估计：固定 t 的 Hölder／平移给 ||F(x+t,y)G(x,y+t)||_(3/2)≤||F||₃||G||₃，再 Minkowski 给 unsigned 积分的 2log(R/ε) 因子。它与 signed count 的 √N logN 是不同估计；原文、root／B／C 没有把有限绝对可积性误读为可消除该 log。

## 3. 三角几何与实际可用的条件正用途

独算 (x,y,t)=(-a,-b,a+b+c) 的三维 determinant 为1。pair maps (b,c)↦(b+c,-b)、(c,a)↦(-a,c+a) 的 determinants 都为1，output map (a,b)↦(-a,-b) 亦为1；因此三个 Lebesgue L³ norms 逐个保持，得到 G₀(a,b)G₁(b,c)G₂(c,a) 的真实 cyclic entanglement，不要求三变量统计独立。

在 source claim 下，pointwise domination 和 Hölder 确给

    ∫|H| Σ_j |B_j(F,G)| ≤ C√N log(2+N)||H||₃||F||₃||G||₃。

这也控制合法 output-only β_j 的 signed 配对。固定 output 时，β_j 同时作用 ±t，kernel 仍 odd；不能将其写成任意 β(a,b,c)，尤其不能免费乘 sgn(a+b+c) 来变成正 kernel。

root §5 保留的正用途正确而必要：对真实非负 pair factors，若 H 所测 output 的负时间支乘积确实全零，B_j=A_j⁺，上述条件估计便能控制该正量。正化的一般反攻不否定这个合法特例。但尚未从原 WZ／ordinary 配置提取这种支持事实，也没有以它为成功公设；仅有原 incidence domination 或 density 不足以给该用途。

## 4. 连续反攻及 supremum 的精确边界

独核 root §4、B §10、C §5：固定 compact smooth plateau F=G，固定正面积 core Q，取任意 N 个全部位于 plateau 半径内的 dyadic annuli。正负 shifted inputs 在 Q 上均恒1，故每个所列 signed B_j=0，正半轴积分为 log2，双边 unsigned 为2log2。原 L³ norms 与 |Q| 不依 N，因而正 sum 的 L^(3/2) norm≳N，不能有 C√N log(2+N) 的统一正版本。固定非负 smooth H 在 core 中支撑给同样 scalar lower。

positive r-variation 在这些 N 个增量上至少 N^(1/r)log2，因此也不能使用原 Th1.1 的 N-independent 正版本；这不要求有限数值或离散模型。每条环带只说“指定的小环带上 signed 零”，没有声 entire S_N 或全 variation 在 Q 上为零；远环带仍可非零。原 signed source claim 未被此例反驳。

奇偶分解 A_j⁺−A_j⁻ 与原正量 A_j⁺+A_j⁻ 的区别是实际阻碍。m(t)=1_(t>0) 便可破配对；output-only β 无此权限。该连续例不保原 small footprint、full CW／filled X／selected ξ，也未构造严格低维全方向集；root／B／C 均未升级其范围。

## 5. 原 g、半clock阴影、范数与尺度费用

为核 B／C 的原接口，本轮另实际读 WZ §20.3(164)–(165)、§21.1(172)–(173)、Th21.2／Remark21.3 的相关原段，并读回 R76 主稿 §§6–8。它们确给 selected dense graph，不要求抽象统计独立；R76 已付同 T 的完整第三 clock、g≤1 和完整 native-product 上的密度，不能重列为尚无 product reference。但自然单 block 仍只有约 δ² 的原全族质量，未给三个 THT pair factors或全局质量重接。Th21.2 的 multiplier 仍 scalar，不能由扩 A／B ambient 自动升级 matrix。

所以不因“g相关”粗拒 THT，真正未付是保原 N／I／λ及误差的 pair 表示或允许的线性化、并使目标正量在 signed 积分中不相消。g≤1／μ_act≤Kν⊗dt 只能用于正序 domination，不能反向比较 signed 量。源 L³ 是二维 Lebesgue 规范，原离散／Frostman priors 的平滑密度和三因子总 norm 须实付；没有免费从前者转到后者。

root §6 的实体几何也核过：roundδtube 关于单位轴中点中心对称，垂直中分平面分出等体积两半，故取正半 clock marks 可使每管及原加权平均 density 恰1/2，方向／whole axes／weights 不变。这只检基本可测 shading 闭包；未说任意已有 Y 删半都保1/2，也未说保完整 WZ 的 AD／ξ／fullness。

root §8 的尺度校准正确：原 ds 质量与 dt/t 在 r<|t|<2r 上相差1/r的 kernel weight，原质量要带 r 回求和，不能每环带各记一份相同原 I。N≈log(1/δ) 的指定 dyadic 使用只贡献 subpower，不自动给 δ 正幂；不扩大为一切 output-dependent partitions 的 no-go。固定有限 J 上的非负 ds 三对量本来由 fixed-t Hölder／Minkowski 得 |J| 乘三 L³norm上界，不需要新 singular claim。

## 6. 判定、完整路线与停止

限定有限范围全文通过，无未解决 mandatory。root 的合法负支零用途、Lebesgue L³ 对原 priors 的范数区分、逐环带 clock 费用和 fixed-J 旧正上界均已经逐式核过；没有以一般正版本失败强拒该合法用途，也没有强迫 source 高级证明通过。

终 macro／next／source／round 已实际全文读。OAI4 §11 的同维／低维后果、DIM／FSD 旧闭包与 HRZ 原窄项不被新名称解冻；ordinary／HRZ 全预算、sticky 全 rough 及普通桥、真同集全方向严格低维四路仍 open。直接 THT→原正 joint mass 的桥未支付，停止 r／partition／frequency／mask 参数续轮；不声所有 oscillatory 方法无用。streak23 只计未获 ordinary／完整 branch-saving，与本轮实际来源资格和反攻信息分开。

本审认可 conditional signed 应用、初等连续反攻及其明确停止，不是 new result ID、major、ordinary 新界或完整 source 反例。外部37页 wholeproof 未新独证，未经外部同行评审，不认证未来 metadata、Git、同步或档案计数。Goal 保持 active。
