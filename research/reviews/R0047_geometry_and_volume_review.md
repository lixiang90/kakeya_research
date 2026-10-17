# R0047：全时几何、连续碰撞证书与停止范围的独立审查

2026-10-17，A。已实际全文读 root《R0047_cyclic_actual_volume_and_closed_loop_boundary》8节、B《R0047_cyclic_collision_and_counterattack》7节、macro8节、HRZ next5节，及实验代码和完整 JSON 的50条 records。A自己的施工稿不计独立审查。结论：**这些稿件的明确片段、finite certificates 及停止/后继范围通过；一般 CYCL 和 asymptotic power upper 均未证。** 无必须修正的数学问题。未经外部同行评审，不认证新颖性/重大性。

## 1. 同一原族、prior 与闭包

逐项核原 N⁴ 个方向的 uniform law、共同 t∈[0,1]、有限真实直线段与固定 C0≥10。所有几何返回都使用原 full grid 和 wholeclock，没有把原依赖改成独立 marginals，也没有填补部分 shading。R41 的 TC=0 不能抹去这里可达4logN的 S；两稿明确 paid small-S input 不适用。

任意删方向破 product，任意删时间破 wholeclock；受限 CYCL 不给旧全称 CP/PM，未知全称 fixed-power lower 也不直接给 log 强度。因此本轮没有以已有正幂等价式改名开方向。finite-net 到 compact 的 FD 桥已在 R46 支付，当前没有把它重新虚列为未知问题；缺的确为本轮有限 power 输入。

## 2. Palette、断环及负反馈证明

root §2/B §4：指定一个 b_i 的 δ-bin 后，输出 i 给 a_i 至多5种；查表逆向恢复另外三坐标，各至多3种，135L_i 原 fibre 上界正确。occupied δ-cube 整体距其中一个真点≤2δ，对半个 clock 积分给1/(270 min L_i)。其余三表可完全粗糙，原 prior 无重置；一般 min L_i≈N 只基线 N^−1。

root §3/B §5：假两像的各 row 残差<tδ，任何一个方向坐标差为0会沿逆环迫全0；否则每个 intercept 差非零且与对应方向差异号。弱单调方向 s_i 遂迫四个 sign 关系，其乘积要求 ∏s_i=+1。因此负反馈 ∏s_i=−1 确给逐 t≥1/2 的 tδ 分离。任一常值表则直接断环恢复，不需要其他表单调。

实际切片内 disjoint cubes 的 Euclidean radius、时间长度均核过。root 较弱常数1/512与 B 较强1/32都成立，不能以常数不同误判矛盾。分块反序 N=m² permutation 的最长递增/递减子序列至多m，四表逐表抽取可只保 N² 方向；该 N^−2 损失真实，不能借单调抽样免费覆盖任意表。

## 3. 所有 affine 表的3/16下界

root §4/B §6：由有限表 range 得 |c_i|≤2/(1−δ)≤4；连续参数 A∈[0,1]⁴ 的 lowergrid 误差各≤δ，输出 Euclidean 差≤2(1+max|c_i|)δ≤10δ。因此包含关系确在题设固定厚度内。

矩阵 determinant 为 t⁴−P，P=∏c_i。几乎每时刻为可逆线性映射，故 slice volume 恰 |t⁴−P|，没有 nonlinear multiplicity 漏项。函数 ∫_0¹|t⁴−P|dt 在 P=1/16 最小；直接分 t=1/2 积分为3/16，区间外更大。Fubini 给实际全时体积，不是 sampling 或单时 rank 推断。

任意粗表的线性插值可能在 δ-gap 内跳 O(1)，并不在原 C0δ-neighborhood 内；两稿均正确阻止用 Jacobian/degree 免费回传。composition of shears 也不等于 simultaneous cycle。

## 4. 单时共振及能量下界的正确方向

root §5 的 b_i(a)=−τa，τ=3/4，在 t=τ 为 rank3 循环差矩阵；原 fibres 可ΘN，δ-cell slice volume ΘN^−1，故一般逐时 constant/log lower 是假的。全clock仍适用 affine 的3/16下界。

平滑 density 的 support 在三个 O(1) 轴及剩余 O(|t−τ|+δ) 轴的 box 中；质量1的 Cauchy 给 E(t)≥c/(|t−τ|+δ)，积分≥c logN。该式只否定 uniform O(1) raw-energy upper，不是 volume upper，也不否定 polylog-energy 充分方法。root/B均未从能量大或证书弱反推实际幂压缩。

## 5. 原 pair、trace 及连续时间 Cauchy 的逐步核对

平滑用 side-δ 的4维 cube，Euclidean radius正好δ；每个 t 质量1。原有序 pair 的 overlap integral≤δ^−4乘四个碰撞 indicators，uniform prior 权重 N^−8，故 E(t)≤N^−4 C(t)。I=[1/2,1] 原总质量1/2，再在整个 time-space 上 Cauchy 得 volume≥N⁴/[4∫_I C(t)dt]。

对整数表、timecell [j/Q,(j+1)/Q]，真实 |t k+d|≤1 确迫 |j k+Qd|≤Q+|k|。矩阵 row 为当前 k_i，column 为下一 k_(i+1)，四个实际 coordinate pairs 恰被各自 histogram 计一次，trace 正是全部四约束同时成立的上包络 pair 数。没有假定四个输出独立。

ceil/floor 的 lower endpoint −floor((Q+|k|+jk)/Q) 与 code 相符；prefix 的 inclusive upper 索引正确。时间cell平均费1/Q，遂 volume lower QN⁴/(4ΣC_j)，没有将 time samples 估计成连续 upper。固定 column 后每个原 pair 允许常数个 row，粗容量至多给 trace≤CN⁵；B指出这仅返回 N^−1 是正确的未闭环边界。

## 6. 实验 code/full-output 实际审查

全文读 code，并完整 parse JSON，而非只读被截断的工具前缀。读取并检查全部50张四表、N/Q、全部 collision counts/总和、每个 rational numerator/denominator/display、flags及 source SHA256；结果一致。N=4十类 direct-pair 字段全部为true，其计数路径不复用 histogram/trace。本人没有第三次重跑整组实验。

每个非负 matrix 部分乘积 entry 可按其实际 partial coordinate pairs 计数，分别≤N⁴、N⁶、N⁸；完整 trace 也≤原 N⁸ pairs。N≤64 时 int64 安全，跨time求和用 Python int，最后 Fraction 精确。JSON50条 flags均没有宣称 uniform CYCL、power construction 或 Kakeya counterexample。最弱 lower、N64显示值及 root §7 finite scope一致；这些证书仅覆盖明示有限表族。

## 7. 一手范围及下一HRZ任务的强度

本轮核 FD2607.14824v3 与 Zhang2608.17952v2 primary 范围：FD 的某个全方向构造 log upper、Prop5.4 compact transfer 和 Zhang 的旧 fixed rational mixed-norm theorem 都不直接给这里任意四循环表的 wholeclock lower。有限检索无命中不认证新颖性；没有引入未读二手结果。

另实读本地 HRZ1908.05589v1 PDF1–3/extracted行1–175核后继的基本定位：Thm1.2/表在 n5 为 p>18/13，其 conjugate 为18/5；该数字是2019历史 maximal 声明，不是2026最优认证。next正确要求先核现行版本、真实递归/terminal与 finite DIR/FSD 的接口，而非假装已有可替换的4D terminal。

H5 的 #E≥δ^(−4−σ+ε)、满4参数方向网、逐管原 marks≥δ^(−1+η)、∀ε∃η/δ0/c 均明确；它是待证严格>4的 finite 目标，仍需 Hausdorff读出，不是本轮成果。next明确曲面 flatten 可能弯线、短clock重缩/复杂度/逐管与平均密度都须支付，也没有把未给 full Lp/任意λ当输入。未发现即时量纲矛盾；这不预认证 HRZ 架构可完成该接口。

## 8. 正式结论与停止

通过上述已证子类、有限 continuous-volume lower certificate、反向误用排除及 macro/next 的明确范围。当前没有一般 rough-cycle log lower、无穷统一 power upper、新5D界、Kakeya反例或重大/优先权声明。root/B均遵守一主轮停止，不续 alphabet/cycle length/palette/S/trace重命名迭代；R48先周期macro和有限primary前沿核，再只检验一个不同的实际递归接口。

本 review 完成后停止编辑；无 Git/元数据变更。数学通过仅是本项目内部逐步审查，未经外部同行评审。长期一般/高维 Kakeya Goal 保持 active。
