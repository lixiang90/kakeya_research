# R0028 独审：平均 carry、原作用整合与下一种子目标

2026-10-17，审查者 `audit_four_dimensional`。逐式审查 B 的 `R0028_factorized_action_counterattack.md` (3)–(9)、root 的 `R0028_actual_action_boundary.md`，并只核下一 finite-seed 目标的量词及条件算术。**结论：这些有限结果和所列停止边界可归档，未发现必须修正的数学问题；未验证 AFF₃、完整 factorized 反例或任何新维数界。**

独立性说明：本审查者是十六边 box 源稿的作者，故下文对 root 的 box 部分只是逐式接口复核，不冒称该部分的第二个独立证明。B 的平均 carry 证明及下一候选的条件算术由本审查者独立核算。没有重证四维 175 页论文或 He/KT 全部高级证明。

## 1. B (3)–(4)：原参考先验的 domination

固定 s。映射 `t↦frac(|t−s|)` 在原有固定 bounded time 区间中只有固定有限个平移/反射分支。一个前 N 位 word 的原像是固定有限个长度 `r=B^-N` 的区间。`d≤r` 使原 interval upper 可查询，因此其条件概率至多 `C K_t r`。再积分 s，得到 (3)；更强地，该 domination 对每个固定 s 都成立。

由此把任意非负 digit 测试函数按 `C K_t×Uniform(B^N)` 上界是合法的。这里没有把原 time digits 宣称为独立：独立均匀 digits 只是一个已证明的支配参考。事件只用前 n=N/2 位时，求和其余 N−n 位同样得到 `C K_t×Uniform(B^n)` 的上界。

角前 n 位的原像也只需固定有限次 abs/mod 分支。每支是一个固定坐标宽 `q=B^-n` 的 slab，取原法向 e_j 即可；`q≥q_base` 保查询合法。故每个 angle prefix 的原质量至多 `C K_ψ B^-γn`。端点使用终止展开，只落入相应闭区间，原 slab upper 已控制这些原子；无需假连续分布。

上述两步可相乘，原因仅是 **raw reference** 为 `ν²×π`。原 π 的 digits 可任意相关，后续 g 条件 law 也无需独立。

## 2. B (5)–(8)：加权 prefix 求和、少 overflow 与固定 base

对 `c≥1`，uniform time digit 中 `dc<B` 的比例为

    (floor((B−1)/c)+1)/B ≤ min(1,2/c)=w_B(c)。

`w_B(0)=1`，所以 `L_B=Σ_c w_B(c)≤C log(2B)`。先固定一个完整 angle prefix，用上节的 time domination，再对所有 angle words 用每个 word 的质量 upper 求和，恰得

    Pr(Z_N=0) ≤ C K_t K_ψ B^-γn L_B^n。

没有把原 angle prefix 概率写成逐位 product。逐位 product 只出现在支配后的权函数求和 `Σ_{c_1,...,c_n}∏_i w_B(c_i)=L_B^n`。

若 `Z_N≤floor(θn)`，存在一个例外集 S、`|S|≤floor(θn)`，其补集全部满足 `d_i c_i<B`。对固定 S，其内 angle digits 自由求和贡献 `B^|S|`，其外贡献 `L_B^(n−|S|)`。对 S 作 union upper，正好得到 B (7) 第一式。再用 `L_B≥1`、`Σ_k binom(n,k)≤2^n`，其第二式

    C K_t K_ψ [2 B^θ L_B/B^γ]^n

也成立。取 `θ=γ/4`，先固定足够大的 `B=B(γ)` 使 `log_B(2L_B)≤γ/4`，括号至多 `B^-γ/2`；`n=N/2` 给 `r^γ/4`。floor 不增加阈值，亦不需要 N 与 γ 的分母整除。

正确顺序为 γ 固定、B 先固定、N 后趋大、source small-loss 指数最后小于固定 γ 余量；不能让 B 随 N 增大后还把隐常数当统一常数。当前稿已明确该顺序。把一般工作尺度改成相邻偶次幂只改变固定 B² 因子，不改变该指数结论。

## 3. B (9)：原 g 的相关性、真实乘法及范围

对两个 N 位非负截断，真实乘积的未归一 coefficient 是 `a_k=Σ_{u+v=k}d_u c_v`。`d_i c_i≥B` 蕴含不同 even position `a_2i≥B`。标准非负 carry 从更低位进入时不会减小该 coefficient，故这些位置各自必须有向上 carry。它是实际实数乘法的必要 overflow 信息，并非 digitwise 群运算。非负整数部分只增加相关 raw coefficient。

这一结论没有说每个 carry 产生新的不同修正值，也没有证明 output entropy、cardinality 或 coarse-fibre lower。许多 carry 可能相关；signed/balanced 表示的相消也未被本证明控制。B §§6–7 和 root §4 都明确保留这些边界，故没有由“正比例 overflow”偷跳到“固定维数增长”。

由于 `0≤g≤1`，对原参考中的坏事件 E 直接有

    ∫g 1_E ≤ Pr_raw(E)，   Pr_g(E) ≤ Pr_raw(E)/m_g。

这完全允许 g 与 a、time 及全部原 angle labels 相关；没有重新给条件 π 边际套 slab。若两个 K 各至多 `r^-η`、mean 至少 `r^η`，损失确为 `r^-3η`，故 `η<γ/12` 留出严格正指数。各 K 有不同 source 常数时，稿中的 `(C_t+C_ψ+C_g)η_src<γ/4` 是正确一般形式。实际 fine base 与 slab base 的检查也明示，不在 sub-base 免费调用。

因此所证的是：原 dense g 无法主要由完全无 carry 或 o(N) raw-overflow tuples 实现。它既不排除允许大量 carry 的成功模型，也不证明真实 matrix-time 图必须低 carry。该限制与全文 main 尚 open 的叙述一致。

## 4. root 原作用整合：逐式接口核对

root §2 的 fixed-a 四变量 box 及再对 a 的 Jensen 给 `m^16`，仅共享一次 a；没有把它误记成原单个 W 的同质量子集。横截角来自原两份独立差 law，原 box 权至多 1，因此 raw-prior 坏事件可直接扣除。合法 `λ≥q_base`、time gap `b≥d` 与相应质量门槛均列为条件。

索引号也正确：`u1−u0=V` 时，`y_ij00−y_ij10=L_ts V+O(E₀)`；`y_ij01−y_ij00=L_ts W+O(E₀)`。因此其矩阵式的符号、`E₀ λ^-2` 回收误差及 secant 另付 `b^-1` 均正确。当前 `E₀=Kr` 没有再误写成免费 r 精度。angle/time parallelogram 只耗固定多个 E₀。

自然 shears 的公共 vertical 子空间逐点固定、horizontal quotient 作用恒等，因此相应 He irreducibility/P(G) 输入确实不满足。稿件没有由 whole-M nonaffine 消掉这个表示论障碍，也没有把加入 dilation 的新作用先验当原图已有。

used H 的 κ-cover/Frostman-upper/slab 与 κ-AD lower 已区分。box 是有限共同作用图案，不是 output-to-input 迭代闭包。OBS002 的 generic 数字模型也没有被称为完整 factorized/source 反例。以上 scope 均准确。

## 5. 下一 finite-seed 目标：只作量词和条件算术核查

对照本地 KT 原文 `katz_tao_2001_v1_new_bounds.txt`：§5 记号说明约 750–753 行、Def5.1/5.2 约 768–799 行、§6 ambient 与 n−1 collection 约 985–1006 行、Theorem6.2 约 1021–1022 行。原 finite 类允许任意固定 ambient M、实 n/d、direction-cap upper 和 total saturated shading；`≈` 确允许 `C_ε N^{Cε}` 费用，不限于 log，也不要求每条线完整可见。下一稿将这些列为必须重新展开的输入，正确。

KT 的递推式为 `(2n+1+d')/4`。若尚未证明的 arbitrary-ambient 四维 finite seed 及 thinning 转移均能合法提供 `d'=4−O(ε)`，n=6 的条件输出是 `17/4−O(ε)`；与 `7−2√2≈4.171573` 的比较算术正确。这里没有已得新六维 bound，也没有最新前沿/优先权认证。

若第二输入只允许 `d'≤d+1`，则递推不超过 `(2n+2+d)/4`，固定点为 `(2n+2)/3`，n=5 恰为 4。该计算只限制所述递推路线，不能推广成所有四维输入或全部高维方法的 upper barrier。当前稿保持了这一区别。

Hausdorff 集合结论、任意 ambient finite K 种子、real direction dimension、随机 thinning、平均 shading 与逐管删选之间的桥都仍列作未付主任务。R28 没有提前启动或完成它。本 review 通过的是候选表述及条件算术，不是该桥的可行性。

最终意见：可按当前范围归档；本轮只得到原质量下的有限 box 与平均 raw-carry 门槛。AFF₃、>2 gain、完整高维 Kakeya 均未解决，提前 macro 冻结原局部迭代符合本轮已证范围。
