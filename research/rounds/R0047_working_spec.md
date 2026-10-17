# R0047 working specification：真实四循环placement的体积门槛

2026-10-17，Goal active。context.py→tmp/R0047_context.txt，GOAL/STATE/ROADMAP/registry78全部状态/latestR46/AGENTS/round/macro/next已读。R46 HEAD=origin=remote 8ba7252cb0eb7ad64291847bd854f56502949b13，tree 7b7bc905a5950d9ae9b1ebd3d700a895835ab62d，694files/clean及receipt全项开轮核。上一Goalturn为progress：精确算术/自然编码失败和稀疏compact桥改变下一动作并已同步；不是verified wait/no-progress。R46提前macro已做，常规下一R48，主候选失败则立即macro。

## 1. 唯一任务与明确候选

本轮依据R46唯一next，检验一般Kakeya反例候选的一个真实高entropy构造类，而非缩减长期目标。固定R5，N dyadic、δ=1/N、D_N={0,...,N−1}/N，A满D_N⁴，B_i(A)=b_i(a_(i+1))，a5=a1，b_i任意D_N→[−1,1]。K_N=union_A{(t,B+tA):t∈[0,1]}是真实wholeclock segments。

首要候选CYCL：存在c>0,A0<∞对所有N/所有b都有 |N_(C0δ)K_N|≥c[log(2N)]^(−A0)，C0≥10固定。反攻可寻无穷N_j→∞上同κ/C的实际volume≤C N_j^-κ，有限样本不够。所有方向网、time厚度、upper/lower属性必须付；不以边际乘积、单t碰撞或time sampling替连续volume。

## 2. 排重与合法闭包先检

本类TC(A)=0，但S=ΣH(floor(B_i/δ)|Ai)可4logN，R41小S/separable lower不能直接用。任意删direction破fullproduct，删time/shading破wholeclock；平均/逐管density各自付heavy损失。cyclic restricted lower不含任意B(A)，不能反推旧全称CP/PM；旧全称positivegain也不自动给log下界。若发现完整正幂等价或仅旧EG重述，停止而不登记新方向/ID。

## 3. 证明、反攻与常数

先实际slice/碰撞：常数及affine、循环可逆/退化、随机/digit模式；解析处理full joint occupied cover，必要时明示对每t的权重/可测性。b_i只有有限表无需正则，若插值/平滑/舍入必须证明对C0δ-neighborhood的双向费用。有限计算只证其有限比较/认证体积，若不能得uniform新信息不扩大样本代替证明。

fullgrid在闭direction cells连续fill误差≤2δ，N_(2r)厚度与C0预算同付，finite rotations给fullG。每scale统一power经FD2607.14824v3 Prop5.4得同compactE及κ/4上Minkowski；无穷稀疏δ_j也能以step-f(r)=C min{δ_j^κ:δ_j≥r}供应∀r，输出r_j=(δ_j/Cd)^4的power给Hausdorff/下Minkowski≤5−κ/4，非上Minkowski。此桥已付，不能虚报未知coherence，也不能宣已构造maps。

## 4. 分工与独立审查

root主稿、真实实验（若需要）、元数据/状态/Git。A只 notes/50_counterexamples/constructive/R0047_cyclic_geometry_and_primary_audit.md 与 research/reviews/R0047_geometry_and_volume_review.md，负责真实geometry/fullclock/lower及primary比对。B只 notes/50_counterexamples/constructive/R0047_cyclic_collision_and_counterattack.md 与 research/reviews/R0047_collision_and_scope_review.md，独立碰撞/熵/反例攻击。最多两互补代理，不编辑其它文件、不Git、不再spawn。新reviewed命题须实际全文独审，不以作者署名或有限样本认证。

## 5. 一主轮停止

完整uniform lower或真实asymptotic power构造须独立逐步审+一手比对；若只旧EG/4D投影N^-1/单t压缩或没有新估计，执行macro停止此cycle施工，不续循环长度/alphabet/branch/S阈值调参。只证明明确有限/条件片段也须准确限定，不把初等校准称major。归档/验证/根提交/安全sync后Goal完整active；高维一般目标不因此完成。
