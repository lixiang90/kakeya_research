# R0045 独立审查：真实原star、Kakeya–BL与计数范围

审查者：audit_four_dimensional，2026-10-17。独立于 root 主稿和 B 有限star/LW证明作者。本人 source/primary 稿不在本文件被当作自己的独立审查。这里只认证所列初等推导与具名高级定理的接口，未经外部同行评审。

结论：**通过本轮主稿、B稿、macro 和下一 gate 的所述范围，可归档。** 已实际读 root 主稿10节、B稿9节、macro8节及 next5节；没有待修的实质数学问题。不通过 actual BL-good/rank mass、不通过 `kappa<=zeta` 或任何新的 Kakeya 维数声明。

## 1. 实际阅读范围与准确输入

逐式读取 root `notes/40_multiscale/R0045_actual_four_arm_BL_gate_and_rank_budget.md` §§1–10，以及 B `notes/40_multiscale/R0045_four_arm_mass_and_transversality_counterattack.md` §§1–9。另直接读 Zorin-Kranich 1807.09604v4 正文 PDF1–16，核心 application 独核 Definition1.1/1.4、Theorems1.3/1.5、式(1.5)/(1.6)/(1.9)/(1.14)–(1.16)，并对照官方 HTML；不只依 root/B 转述。实际 WZ Def17.2–17.4、§19.1 的(148)–(151)亦重读。

ZK 的 `k_i=3` 是 kernel/仿射平面维数，本题 normal 秩为2；`p_i=5/8,P=5/2` 的 scaling 正确。Theorem1.3 确需全部混合 tuples，Theorem1.5 没有该限制。原 PDF5 的 `A`/应有 `A^{-1}` 单行倒数排字不进入本证明；项目直接从1.5和定义导出 selected-tuples 估计，未据排字宣称高级主定理错误。

## 2. 原 incidence 图的重筛、时间和角 law

root §2/B §5 的两次 heavy 筛选在同一原有限图中合法。light-T 的总 incidence 至多 I/2（B 使用 I/4 亦可），再删 low-heavy-degree base 至多 I/4；余 base 数由原 row upper 回收 inverse-subpower 的 `|E|`。所保管的 endpoint degree 仍使用 **筛选前全部原 marks**，故没有把 base 筛选反复反馈到 endpoint degree 而循环失去 lower。

四臂原选择 law 是给定 base 后四个真实 `(T,endpoint)` 集合的乘积；这只是原计数的定义，未拆成独立的 `phi` 与 time。每原 fine phi-bin 的 witness 重数 O(1)，每 `(T,time)` 的 point 重数 O(1)，连同 heavy row/endpoint lower，给该 law 对 `uniform Phi_p × full delta-time grid` 的 `K^C` domination。乘上 `D_T` 权重和 heavy 限制只损 `K^C`。故使用 slab cap 删除近角/重复 T、使用逐管 time upper 删除近 time，真实损失为 `K^C(r^gamma+r)`；按 `eta<<alpha gamma` 选择 `r=delta^alpha` 可付。没有凭平均 density 偷取原逐管 dense。

若另有非该原集合定义的额外相关 g，仍须保其原质量与 domination denominator；root/B 均保留这条边界。

## 3. 物理平面近交和 finite-grid 实现

root §3/B §6 的源式符号正确：`xi_i=xi_0+(F_0-F_i)phi_i+O(delta)`。`B_i=(-F_i,I,-xi_i)` 的两个奇异值统一上下有界，因为 `B_iB_i^*=I+F_iF_i^*+xi_i xi_i^*`。原 `p,p_i` 同在一根整管，且 wholeclock 有界，故 `|B_i(p-p_i)|<=Cdelta`，四个仿射三平面的 `Cdelta` 邻域真实覆盖共同起点。

root 的固定有限 ambient grid translations 可合法把每个近平面改成与原 base cube 真相交的 plane copy；保留 `(endpoint,translation)` 标签，则每 family 只扩大固定倍，directions/BL 不变，原 endpoint fibre 界不丢失。一个选中原 tuple 可挑一个 translated tuple，不会以消掉原 labels 产生虚假增益。等价使用有限 shifted coarser grids亦可。

ZK1.5 是仿射平面上界，故这里不要求 plane 内已有真实 filled shading。反过来，本步骤也不创造原 source 的 filled3plank；后续若另用要求 shading density 的定理须重新付。

## 4. Fremlin selected-tuples、权重和尺度

root §4 的计算完整：四个 Fremlin 因子为 `ell^4`，rank-one domination 对四次幂求和后取 infimum，给其 norm 至少 product-space `ell^4`。对 `BL^{-1/P}` 取 `P=5/2` 次幂恰得内层 `BL^{-8/5}`、外层 `5/8`。在 good tuples 上 `BL_reg<=A`，故左边至少 `A^{-1}|Gamma_Q|^{5/8}`。

允许任意选中 hypergraph，不需再提 Cartesian 四族；重复 planes 必须保 multiplicity。带独立 family 权重可由复制/有理逼近或 weighted norm 付出；共享起点的任意 law 不能免费声称 product domination。root 采用原 endpoint counting 字母表，避免了这一跳步。

全局 `(1,R)` 的 `R~delta^{-1}` 和局部 `R~rho/delta` 已分开。写物理积分时共同 `delta^5` 在两边，写 cube count 时两边都不带，主稿指数没有漏此因子。

## 5. 条件有限 BL 桥与全部子空间责任

root §5 的必要充分判据在 `F_i-F_j` 两两可逆范围成立。固定 i，真实 `G_i intersect G_j` 方向是 `(a_ij,1)`，`a_ij=(F_i-F_j)^{-1}(xi_j-xi_i)`，符号正确。若三条线张成二维，则该空间的 BL 右边至多15/8<2；若只一维，则为四个共同 kernel。因此任一 `D_i=0` 必退化。

反向 proof 没只调用 stacked rank：坐标 `(x,y,t)->(x,B_iX,t)` 的 Jacobian 恰1；其余 maps 是 `(F_i-F_j)(x-a_ij t)+s`。以三 kernel columns 作 fibre frame 后，两个非 kernel columns 的 target determinant 是 `|det(F_i-F_j)| |D_i|`。三维 LW 后 domain determinant 和三个 target determinants 的 powers 合并，准确得到

`C_i=|D_i|^{-1/2} prod_{j!=i}|det(F_i-F_j)|^{-1/2}`。

四个权向量 `(1,1/2,1/2,1/2)` 经 Hölder 均分为 `(5/8)^4`，常数 `(prod C_i)^{1/4}`。这给所有输入函数的完整 BL inequality，因而确实支付全部 subspace conditions。

root §6/B §9 的有限概率桥同样通过：固定 times，先要求五矩阵全部 pair det 至少 sigma；条件 phi_i 后各 `a_ij` 是其它 phi_j 的独立 reference affine image，最小奇异值至少 `c sigma`。小三角面积由“前两点近”或“第三点近直线”覆盖，各只用一次 slab cap，故费用是 `K max(delta,C sqrt(tau)/sigma)^gamma`，没有免费丢 K，也没有错误多乘 K。实际 O(delta) xi error 引起 `D_i` 误差 `O(delta sigma^{-2})`；在 tau 较大后，actual upper为 `C tau^{-1/2}sigma^{-3/2}`。参数 `2a<beta<1-2a`、随后 eta 小于 `gamma(beta/2-a)` 非循环。

以上是条件桥，原 time-rank 好质量仍未证明。实际原角/time 相关性通过 `K^C` domination 支付，不能由 reference 的好概率倒推出实际 rank-good lower。

## 6. B 的真实有限校准与原 rho 费用

B §3 的 `c_i=i/8,phi_i=(c_i,c_i^2),t_i=rho c_i,f(t)=tI` 是四根不同真实直线的精确同源 star。`G_i intersect G_j` 的方向为 `(c_i+c_j,c_i^2+c_ic_j+c_j^2,1)`，其三列 determinant 是非零三节点 Vandermonde。按§5同一 fibre 推导得到 upper `C rho^{-3}`，单位 quotient inputs 在共同近三维 kernel 上的圆柱给 matching lower。因此同源因子不强迫四臂 BL 无限，且局部 rho 成本可以真实达到。

root §8/B §4 的 regularized 版本使用 `min(R,rho^{-1})^3`，没有越过积分域截断；只有 `R>=C/rho` 才读成 `rho^{-3}`。适配 tangent3/normal2 的变元 determinant `rho^7`，四 target 同除 `rho^2` 的总因素 `rho^{10}`，故 `BL'=rho^3 BL` 正确；不能只保归一化收益而删掉物理 Jacobian/宽度。

额外局部兼容：若有限矩阵桥也放在同 rho time-world，原 dyadic Lip 给 `|det(F_i-F_j)|<=C rho^2`，所以 sigma 不能独立选得大于该尺度。当前主稿没有作这种不合法调用；后续若调用须同步 `sigma=delta^a,rho=delta^mu` 的 `a>=2mu-o(1)` 责任。

## 7. Endpoint fibres、5/4 阈值和无增益范围

root §9/B §7 给定 base/endpoint 和 timegap r 后，方向在 `Cdelta/r` 球内；fine `Phi_p` 的 AD upper 及每 fine bin witness O(1)，给每臂最多 `K^C r^{-kappa}` 原管，四臂 fibre 为 `K^C r^{-4kappa}`。这笔费用原封保留，未把所有 raw witnesses 当不同 endpoint tuples。

若另给 global goodraw 比例 g，先用已知 raw per-base upper 做 density 筛选可保 `gK^{-C}|E|` 个 base、每个至少 `gK^{-C}` 相对 good tuples；不能对 concave `x^{5/8}` 反用 Jensen。两笔 g 因子分别为 `g` 与 `g^{5/8}`，所以 root 的 `g^{-13/8}` 正确。`r^{-(5/2)kappa}`、最终 `(4-5alpha/2)kappa<=5+a_BL+O(eta)` 均正确。

此结果只是一份 **尚缺 goodraw 输入** 的条件计数 certificate。即使该输入理想化，极限阈值仍为5/4；固定 m 臂的 `P/m=5/(2m)` 正好抵消 raw exponent 中 m，阈值不改。它不能完成任意小 zeta，不能被读成新的 ordinary 五维维数界，也没有证明所有未来多线性/混合范数方法均失败。

## 8. 宏观/下一任务与最终范围

实际全文读取 `research/reviews/R0045_macro.md` §§1–8 与 `notes/20_dimension_lifting/R0045_next_rational_mixed_norm_seed_gate.md` §§1–5。macro 正确执行一主轮停止四臂/rank/固定加臂/局部 rho 迭代；两项假阻塞（非Cartesian、没有filledgrain）被撤回，真实未付 good-rank 质量和 endpoint 账本阈值均保留。没有把普通五维投影基线免费用于任意 jointAD/CW 类，也没有把有限桥登记为新的高维结果。

对下一文献入口，已直接打开 Zhang2608.17952v2 官方 primary，并读取本地精确 PDF/text：Def3.1、Lemma3.2、Theorem3.3、Lemma4.2、Theorem5.3/5.8 statements 及所需 §3–4 接口。PDF 首页 literal date 是08-20，version banner 为08-19；HTML date 的显示差异不改变项目使用已存 PDF 版本。没有在此审查中独立认证其整篇高级证明/附录A。

原 q=7/4,r=7/3、p=(2/7,2/7,2/7,1/7) 确送出 `M^{1/4}` 和 projection powers `(1/2,1/2,1/2,1/4)`；新候选 q=5/3,r=5/2 满足 `1/q+1/r=1`，`1-q/r=1/3`，`p_j q=(10/21,10/21,10/21,5/21)`，next 的式子量纲正确。在 full n-by-n arithmetic grid 上 `M~n,|S_j|~n` 时右边与 `|Z|~n^2` 同幂，没有立即的总次数矛盾；这只检验必要量纲，不证明该强化真实可行。

该候选要求任意 torsion-free G、其 rank 和 tensor 次数上的同一常数；这是 Th3.3 可用的真实假设。Cartesian power 也说明若全称常数独立 tensor，则固定 finite cardinality test 的坏比值不能藏在该常数中。仅在一个固定 group/dimension 上有限枚举通过、或把旧 q=7/4 的 logarithm 去掉，都不产生 q=5/3。next 明确区分 equal-cardinality 弱版、全 asymmetric 式以及 strong mixed-norm，未免费互相升级。

其 exact rational forms/算术机制与本轮变化 normals 的 classical KBL 不同；Th5.8 对自然扰动版的否定没有直接否掉 next 的固定 exact 形式，反而禁止从旧逐管扰动 upper 硬接新形式。四维 finite 种子要应用到原任意 Z，仍须支付真实方向分离/bin cap、共同 clock、shading mass 与 all-G uniformity；next 已列低rank集中、Freiman 编码不保 angular 丰富、tensor 常数等反攻和一轮失败即停条件。它不是已完成的桥，也没有未经证明清掉 frozen CP/PM 或 action 责任。

若 next 真得到所需强输入，Th5.3 的条件读出是 **compact** Kakeya 的 `1+3(d-1)/5`；其是否胜过现有各维界、非紧/不可测扩张与新颖性另核。当前不得把这个条件数值写成新界。通过的是下一任务范围/量词和停止设计，不是可行性认证。

最终：root/B 的有限数学和原source接口已核通过；原 good-BL 质量、目标小 kappa saving、完整五维/一般 Kakeya 均仍未解决。本轮没有优先权/重大性认证，没有完整 positive-kappa source counterexample。两指定文件完成，停止编辑，不操作 Git。
