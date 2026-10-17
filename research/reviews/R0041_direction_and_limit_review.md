# R0041：方向、实际体积与同一紧集的独立审查

2026-10-17，B。实际全文读取 root `R0041_actual_volume_and_coupling_entropy_boundary.md` §§1–10、`R0041_macro.md` §§1–8、`R0041_next_macro_and_nonseparable_route_gate.md` 全文，以及 A `R0041_source_construction_and_parameter_budget.md` §§1–10。独立读取原 FD–deLaSalle2607.14824v3 的相关完整§2–5和 Appendices A/B；自己的反攻稿不计独立审查。无 Git 操作。

**结论：上述完整稿在明列范围内通过。** 原 log→power 主任务未完成；没有真实 Kakeya 反例或低维 Hausdorff 构造。actual product lower 与 EG 是严格范围信息，不证明所有构造不可改进，不认证新颖性或重大性，未经外部同行评审。

## 1. 原递归、方向与证书的分离

源 Prop3.9/4.1 保留的是各叶完整 pyramid 的平移，clock 长度未被 core 的缩放替换。完整 base partition 保一个固定非退化方向 patch 的每个连续方向，之后有限旋转并才给全部球面方向。反射 cones 的分离是另一输入，不能再算一次体积 saving。

root(1)/A(1) 的误差是 core 外 branches 的求和；x_i=P_{i−1}−P_i 与最后 P_n 构成和为1的非负向量，故 Hölder 的 (n+1)^{1−d} 仅是该 upper certificate 的下界。level-dependent c_i 的 weighted 版本也正确，前提是每层实际允许同样归纳；没有把每个 node 任意选择冒充已证统一公式。公平分支数≥2、natural scale 与深度的关系已保留；identity branch 不能在无细分时提供 c_i<1 的正压缩。

原证书的最优性已经在 Remark4.5，不被当作本轮新定理；尤其未由 |U|≤B 倒推 actual |U|≥B。

## 2. 实际压缩失败与可分离下界

A 的任意公共 t_i 显式系数与原 recursion 相符：最外 bit 的系数为 (1−P_{n−1})/2+P_{n−1}t_n，归纳恢复 q_j=1+P_{n−j}−2P_{n−j+1}。t_i=1/2 时 q_j=1，w=−α。因此 h∈[1/4,1/2] 的真实 interval union 长度 h+r(1−2h)≥1/4，确得 actual volume≥4^{-d}；所有连续方向和 clock 仍在，不靠删除目标假设制造失败。

root§4/A§6–7 的更广 lower 亦核过。固定同一 clock interval，对每坐标 r-separated slopes 的 strips，任意 intercepts 下两条交面积≤Cr²/|Δslope|；原 marginal 总质量保持常数量级，harmonic sum 给 integrated L²≤Clog(2/r)。同时控制各坐标的 energies（或 reciprocal union lengths）再取公共 good-time 集，避免了“分别很多时间”不能相乘的问题。

全部 Cartesian combinations 的存在才使 product slice 落在真实 N_rK 中。此假设确实由 canonical cube 的可分离 placements 保证，却不由一般每个 joint direction 存在某个 intercept 自动保证。结论 uniform 于目标 r 和递归深度，可排 n(r)≫log(1/r) 的同类捷径。不同坐标深度的 actual ∏(n_i+1)^{-1} 式用各自内含 strip 宽及同 clock Markov 得到，B稿已补精确说明，root 引用闭合。

## 3. 连续方向 seed 与 embedding 符号

A§8 的 half-height 点 q_α=((α+r/2)/2,1/2) 距各侧面至少 c_dr，故有真实 inscribed ball。凸性给 N_{2r}T_α⊂CT_α−(C−1)q_α；因此新 placement 必取 **v_α=Cw_α+(C−1)q_α**，正号才取消该平移。修后 root 使用同一正号。

q_α 的竖坐标一致，水平各坐标可分，故这个明确合法的 canonical G_r 的 fixed-clock patch 仍受 actual log lower 约束。有限旋转并只增大 neighborhood，且保每方向单位段。这里没有以 U_n 的 lower 给任意 subset lower，也没有断言 Lemma2.5 的所有其它 embedding 选择都可分离。

## 4. EG：任意原有限 joint law 的量词与平面估计

EG 的输入明确是有限 law(A,B)、每 A_i 的已付 atom cap≤K0/M，以及其每个正质量 support pair 的完整共同 clock segment。允许 A_i 相关，B 任意依赖全部 A；未假造独立 conditional law，也未将 dense marks 填满成整段。

给两份原边际 law 计算平面 smooth-density L²：相同 slope 的时间积分≤C_ℓ/r，概率≤K0/M；不同 slope 的时间积分≤C/|a−a'|，逐行使用 atom cap 作 harmonic sum。M≈r^{-1}，故总体≤C_ℓK0log(2/r)，没有 K0 的遗漏，也不需 intercepts 不相关。Markov 明确给同一个长度至少 ℓ/2 的 G，同步控制所有 coordinates。

对量化 X_i=floor((B_i+tA_i)/r)，第 k 个原 bin 的卷积质量支持于长度3r的 enlargement；Cauchy 后按固定重数叠加，确有 Σp_k²≤Cr e_i(t)。Shannon≥collision entropy，于是 root(7) 的 marginal lower 成立。

## 5. Joint entropy、TC 与空间返回

关键不等式的方向正确：

    ΣI(A_i;X_i) ≤ TC(A)+I(A;X) ≤ TC(A)+H(X)。

这是 conditional subadditivity 和 data processing，不是直接把 marginal entropies 相加。给定**精确** A_i 以及 floor(B_i/r)，X_i 至多两值，所以 H(X_i|A_i)≤H(floor(B_i/r)|A_i)+log2。原 correlated A 的 TC 与原 B 的条件熵 S_r 都实际保留，结合 marginal lower 得 root(8)。

每个正质量 X-bin 含一个真实 K_t 点，整个 spatial cube 在同 t 的 N_{C_mr}K 中；互不重叠 cube 体积 r^m，#support≥expH(X)。再对原公共 good times 积分即得 EG。可将 K 换为有限 support segments 的并，所有积分/事件皆可测，不需未付方向 selector。

## 6. 一般 compact Kakeya 的 common clock 与 p 成本

root§8 已补原先不能免费的步骤。固定 clock-transverse 小方向 chart，从每个 finite grid direction 只选一个真实单位段；bounded K 保有限 clock 区间总数，而每根段 clock 长度有固定正下界。有限个预备 J 能使每段完整覆盖其中一个，pigeonhole 保 p≥p0(K,m)>0 的方向。无需给不可数方向可测选择。

保留 S⊂grid^m 并非 Cartesian product。uniform-S law 的 atom cap≤1/(pM)，且

    log(1/p)=TC(A)+ΣD(P_Ai||U_i) ≥ TC(A)。

所以 EG 真实给 p^{m+1}e^{-S_r}log(2/r)^{-m}，相关方向损失没有消失。J 可保原时钟；若换原点，given 精确 A_i 的 intercept-bin entropy 两向仅差 O(1)。原 workmesh r=r_j/C_m 也正确，防止把较大邻域 lower 与只在 r_j 的 upper 直接比较。

因此 fixed-power neighborhood upper 的必要条件确为 S_r≥κlog(1/r)−m loglog(2/r)−O_{K,m,κ}(1)，对任意合法 retained-density witness/bucket 选择成立。但没有任何一步证明一般 K 能选到小 S；高 S 情形仍开放。仅 Hausdorff 低维但 neighborhoods 不满足 fixed power 的可能性不被这个必要条件排除。

## 7. 真实紧集桥与停止边界

完整核原5.3/5.5/5.4：crossing segments 保 anisotropic image 的单位长度；minsingular 与半径 δ/ε 被支付；ε^{-m} direction net 数与 ε^m determinant 相消。nested closed neighborhoods（或相同固定倍闭包约定）给同一个 bounded compact E；对每个固定方向，有限阶段的 segment-start 非空紧集嵌套，极限仍是完整单位段。没有仅凭任意 Hausdorff 子列宣称其误差已小于工作半径。

其最终 estimate 是 Cf(Cr^{1/4})，并非各阶段 f 相乘。power seed 真满足输入时会保正幂；原 log seed 不因重用该桥而成为 power。另一方面，本轮没有由证书未变强推断最终 E 的 actual lower；任意最终 patched E 不自动满足全局可分离模型。

macro 如实保主目标失败，冻结的是已排或仅重排原证书的参数循环，不声称冻结项覆盖所有真实 nonseparable 构造。R42 nextgate 要先查 primary/priority、原信息与 frozen equivalences，再选唯一 main；没有自动把小 S 当新公设，也不以两个 marginal 高熵换 joint。该门槛与一主轮失败停止规则一致。

正式全文审查完成，相关文件可交 root 统一归档。长期 Goal 仍 active；不标反例、一般维度证明或重大中间结果完成。
