# R0045 独立审查：原四臂质量、精确BL及下一固定有理模式的范围

2026-10-17，审查者 `lifting_obstructions`。结论：下列修正后终稿在其明确条件范围内通过内部独立逐步审查；未经外部同行评审。没有证明实际 good-BL 质量、`kappa<=zeta`、新五维维数界或一般 Kakeya。

## 1. 实际阅读范围与具名责任

已实际全文阅读 root `R0045_actual_four_arm_BL_gate_and_rank_budget.md` 十节、A `R0045_primary_Kakeya_BL_and_source_audit.md` 十一节、`R0045_macro.md` 八节及 `R0045_next_rational_mixed_norm_seed_gate.md` 五节。自己的九节反攻稿不计独立证书。

一手输入实际核对 Zorin-Kranich arXiv:1807.09604v4 的 PDF1–6 对应提取文本：Definition1.1/1.4、Theorems1.3/1.5、尺度公式及 Fremlin 与 product-space norm 比较。对 Zhang arXiv:2608.17952v2 核对本地 §3–4、Theorems5.3/5.8 及相关定义/证明段落。两篇深层完整证明仍是具名高级输入；本 review 不冒充重新证明。

## 2. 原质量和实际几何接口

heavy tube、heavy base 两次删除的阈值和分母正确。端点继续取保留管的原全部 marks，避免二次删除破坏逐管下界。固定原点后的四个原臂 product 是实际四臂集合的定义，不等于将每臂内部的 angle/time 独立化。

原 row slab cap、每个 `(phi-bin,time)` 的有界见证重数、heavy 下界共同支付 `K^C` 的参考 law 支配；时间 cap 来自端点 time 格点计数。重复管、近角以及端点/原点间近时间删除只需这些条件 upper，能在 `eta<<alpha gamma` 时保原质量。新增相关选择 `g` 的 lower 则不得由此免费获得。

`B_i=(-F_i,I,-xi_i)` 及 `xi_i=xi_0+(F_0-F_i)phi_i+O(delta)` 符号正确。原同管两点关系和 `B_i v_T=O(delta)` 给 `dist(p,Pi_i)<=C delta`，且奇异值有固定上下界。有限邻格或固定有限平移能将近交送入精确同 cube incidence；保留原 endpoint 标签和有限平移标签后，字母表、纤维界仅付常数。这里使用完整仿射平面的合法过覆盖，不需要虚构 filled grain shading。

## 3. 精确KBL与横截判据

`p_i=5/8`、`P=5/2` 时，Th1.5 的四个 Fremlin 因子恰为 `ell^4`；其不小于 product-space `ell^4`，故任意选中 good tuples 均可得 root 式(4)–(5)。不必提取笛卡尔四族。重复平面须按原标签计数，不能只数几何不同 planes。物理 `delta^5` 两边同乘或都不乘；regularized 半径必须与全局/局部 frame 相同。

所有 pair `F_i-F_j` 可逆的范围内，`D_i` 三根 pair-kernel 线的判据和精确常数

`C_i=|D_i|^(-1/2) product_(j!=i)|det(F_i-F_j)|^(-1/2)`

经三维 LW 和四次 Hölder 的推导正确。`(x,y,t)->(x,B_i X,t)` 的行列式为1。必要性用二维子空间的 `15/8<2` 或公共一维核；这里说的是 full scale-invariant BL，不是有限 `R` 时常数字面无穷。不可逆 pair 情形没有被认证。

五矩阵的 pairdet 假设下，角 affine image 的最小奇异值至少 `c sigma`；小三角面积的两分支各只需一次条件 slab cap。查询宽度截到原 base `delta`，并可整体截到概率1。`O(delta)` 原误差引起 `D_i` 变化 `O(delta sigma^-2)`；先取 `tau>>delta sigma^-2` 后得 `BL<=C tau^-1/2 sigma^-3/2`。参数 `2a<beta<1-2a` 可相容。此桥是带清楚充分假设的有限结论，不是实际 rank-good time 质量定理；参考角 product 的 bad upper 转回原相关 law 必须付 `K^C` 并小于 retained 总质量。

真实有限 star 的 Vandermonde 检验说明同源因子本身不强迫 BL 退化，但没有完整正 `kappa` source。共同 kernel 的非 affine 矩阵例也只否免费横截捷径。两种校准均未被升格成源反例。

## 4. 尺度、端点计数和停止判断

同 `rho` world 的下界是 `c min(R,rho^-1)^3`；同一原管则至少 `c min(R,delta^-1)`。局部 `R~rho/delta` 不能套全局更长圆柱。切线三维/法线二维的 parabolic 变元确有 `BL'=rho^3 BL`，但同时改变 Jacobian、宽度和 overlap。root/A 终稿已经保留这些费用。

固定原 base 和 timegap 至少 `r` 的端点，AD upper 及唯一 used witness 给每臂纤维至多 `K^C r^-kappa`。good raw 总质量 `g` 需先按 base density 再筛，不能反用凹性 Jensen。代入 selected-tuple KBL 的完整式为

`delta^(5-4 kappa)<=K^C A g^(-13/8) r^(-(5/2)kappa)`。

所以即使额外补足 inverse-subpower good-BL 质量，当前字母表仍只给理想阈值 `kappa<=5/4`；固定增加臂数在相同编码下不改指数。未付 good mass，连该条件界也不能写成实际无条件新结果。普通五维的四维投影基线不自动适用于任意无满方向的 joint-AD/CW 类。停止这份四臂证书、而非宣称所有多线性方法不可能，符合本轮退出条件。

## 5. 下一候选的量词与量纲

固定有理四模式的 `q=5/3,r=5/2,p=(2/7,2/7,2/7,1/7)` 满足齐次性；Zhang 定义(12)给 `1-q/r=1/3` 和 `p_j q=(10/21,10/21,10/21,5/21)`，故 nextspec 的 `(R5/3)` 没有立即量纲错误。全二维格子、单投影核方向及矩形伸缩校准未构成立即反例；这不是证明该不等式。

其常数必须对所有 torsion-free `G`、rank 和 tensor 次数统一。旧 `q=7/4` restricted weak estimate 的 tensor 强型化只去 log，不改善 `q`。任意代数等式编码也不免费提供四维几何的 angular separation、共同 clock、原 shading 或任意小幂常数；nextspec 已逐项列为必须实际施工的门槛，没有把它们假定完成。

Th5.3 的 compact Hausdorff 结论仍具名、条件于新 mixed-norm 估计；不从一句四维 Hausdorff 满维数免费推出新算术式。Th5.8 否定的是允许逐管小角扰动的加强版本，不否固定 exact rational 模式；nextspec 正确禁止把变化 frame 的 classical KBL 冒充该模式。equal-cardinality 弱接口与完整 asymmetric/strong 结论区分明确。

macro 的四臂冻结、新任务一主轮停止条件及不新增结果ID的边界均通过。若没有合法的新几何编码或费用仅复原旧界，应按所写规则停止，不能以调整固定权重/臂数续名。未发现修后四篇稿件的剩余必修数学错误；本轮没有高维正幂增益，长期 Goal 继续 active。
