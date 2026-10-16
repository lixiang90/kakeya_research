# R0007：四维定理能否提供 WP4 的量词源审计

日期：2026-10-16。主任务：N4-PLANK-01。已读 R0007 working spec、GOAL、STATE、旧 `三维plank输入初审.md`、四维论文 pp.3–6、8–25、47–56、72–73、86–89、168–169，以及已归档 companion `05-inputs.tex` 与 Zahl 2025 survey §4.1。未下载新文献，未独立重审175页主证明或完整 quadric 反例的所有凸框测试。

本轮不是重新发现“高维 convex-Wolff 版本可能失败”：旧 plank 初审末段已经提示该障碍。这里新增审计的是 **WP4 的原始调用量词、四维证明中真正使用的方向/密度来源，以及哪些初始化步骤能被较弱但合法的输入替换**。

## 1. 精确输入与两个初始化调用点

WP4 的空间是 \(\mathbb R^3\)，时空是 \(\mathbb R^4\)。在固定 bounded affine graph chart 内，索引 trace \(M_i(t)=b_i+tu_i\)，\(0\le t\le1\)，\(\delta=D^{-1}\)。它假设所有全时 spatial planks 都满足

\[
\sum_{M_i\subset P}\omega_i\le A a_1a_2a_3,
\quad 1\le a_1\le a_2\le a_3\le D,
\]

而只要求每条 index 的 shading 有 \(\#J_i\ge D^{1-\eta}\) 个时间 bins。目标对任意正权、重复索引及标记形式统一成立，不能让常数依赖原始方向数量或权重离散级数。

四维原稿实际使用的是三维时空输入 WP3，即 Lemma 2.15（PDF pp.17–18，抽取文本 897–953）：\(M_i\in\mathbb R^2\)，cap 为 \(Aab\)，目标为 \(\sum\omega_i\#J_i\le C_\varepsilon A D^\varepsilon\#E\)。量词是固定 chart 与 enlargement 后，先 \(\varepsilon>0\)，再 \(\eta_\varepsilon,C_\varepsilon\)，最后对所有 \(D\)、indices、weights、marks。连续 prior 的舍入与 subpower chart 扩展只用于估计，不要求这些分析性 mark sets 成为输出 labels。

### 1.1 Proposition 2.16 的 universal horizon 上界确实需要无方向输入

PDF pp.18–20、文本 954–1063：在**任意 homogeneous exact problem** 中，先取 \(q\asymp a_L\)，按 block midpoint 的 \(y\)-bin 与 \(X\)-bin 分组 \(G\)。固定 test 已由 native signal 给出；剩下要找有足够质量的 spatial planks。

- 每组用的是旧轨道权重的未归一化 restriction，不是一个方向均匀的新 prior。
- greedy residual 中，每次可取的 plank 阈值为 (2.20) 的 \(N_0^{-\xi}n(L)J_0\prod r_i\)，后期再慢取 \(\xi\downarrow0\)。
- 若 residual 仍重，**原 whole-cell witness** 给 visited-cell 数 (2.21)，不是 residual 当前 density floor；按 preceding/current duration 删轻后每条使用轨道有 \(K_0^{-1}\) 的 normalized time。
- WP3 把高 raw mark multiplicity 转成 fulltime plank 集中 (2.23)，再用同一长 duration 把 trajectory weight 转回 incidence mass，违反 greedy stopping。

原文 \(j=1\) 用静态 dummy coordinate 补到 \(j=2\)；\(j=2\) 直接用 WP3。若把此 proof 改成 \(j=3\)，需要的恰是无方向假设的 WP4；一般 group \(G\) 及残余的完整 projected-slope density 没有源文上界。故不能在这里用“方向分离的四维 Kakeya 估计”取代 WP4 而不补假设。

WP4 的否定否掉的是这段**维度直接替换的 greedy proof**，并不单独证明每一种三维可见模型的 \(H\le L\) 结论都为假。用其他 quadratic-chart 几何能否证明某个受限版本，是不同命题。

### 1.2 Theorem 2.17 的 zero-depth 步骤使用一个更窄的源类

PDF p.22、文本 1141–1185：为了证明 \(g(0,0)\le0\)，原稿用 (2.28) 的 fulltime cap，再用 WP3 排除原始 projected base 在极细 \(\rho\) 网格上的 power-large multiplicity。这里 projected lines 的**完整 visible slope marginal 密度有 \(K_0\) 上界**，由最初完整 slope density (2.26) 积去 bounded hidden slope 得到；cap (2.28) 也正由这份方向密度及两个端点约束推出。

因此五维拟版 Theorem 2.17 的这个特定步骤，不一定需要 general WP4：其 projected \((t,Y\in\mathbb R^3)\) 仍有 full three-slope density 上界，可以尝试用四维证明的 direction-rich finite-scale 读出替代，见 §4。它不能自动修复 2.16 的 universal group/residual 调用。

另一个 WP3 调用是 Lemma 5.1（PDF pp.72–73，文本 3831–3880）：把一个 scalar quadratic 加 dummy variable 提升成 \(\mathbb R^2\) 的 affine motion，再由 plank 提取系数集中。这个提升始终只有二维空间，不因外层 \(y\) 从2变3就自动变成 WP4；不可把所有 plank 调用一概升级。

## 2. WP4 与四维 weighted convex-clustering 的准确接口

已归档 companion `05-inputs.tex` 的 `lem:weighted-convex-set` 与 `lem:weighted-set` 证明分成三个步骤：

1. unweighted dense-shading union theorem，经 weighted Bernoulli sampling、有限 convex-box 测试与重复 tube 删重，变成任意正权、重复 indices 的 weighted convex-clustering 结论；
2. 将包含完整 trace tubes 的任意凸体用 John ellipsoid 包住。ellipsoid 的水平切片具有固定主轴、仿射中心和公共 scalar shape；时间跨度至少1，使最大 slice 三维体积 \(\lesssim |K|\)。这在时空4维的几何步骤本身仍成立；
3. 每个标记时间 bin 放一个不相交 \(c\delta\)-ball；四维中 \(|Y_i|\asymp\#J_i\delta^4\)，\(|\cup Y_i|\lesssim\delta^4\#E\)，tube volume 为 \(\asymp\delta^3\)，故 shading density \(\gtrsim\delta^\eta\)。

若有四维的同型 **无方向 dense-shading convex-clustering theorem**，这些步骤才可给 WP4。权重、重复、cell enlargement 与 \(\varepsilon/\eta\) 的损失都能按 companion proof 保留；不存在一个通过“加权”就绕开其几何前提的捷径。

反之，convex-Wolff family 本身也给所需 all-fulltime-plank cap：固定 bounded graph chart 的 fulltime moving plank 是凸体，体积 \(\asymp\delta^3 a_1a_2a_3\)；一个略扩大的 plank 包含其 trace 的 \(C\delta\)-tube。因 \(a_i\ge1\)，enlargement 只损失固定常数。于是 unit weights 的 convex cap 就给 \(A=O(1)\) 的 WP4 测试。这个转化不增加方向假设。

本笔记不重证 quadric 构造对**所有** convex bodies 的 cap；文献可采用已稀疏化 family，本轮也已在 `notes/50_counterexamples/R0007_weighted_plank_obstructions.md` 核验 full \(\delta\)-grid family 的全部 fulltime-plank upper cap，并以统一权 \(\asymp\delta^{1/2}\) 归一化。两者都不采用未经核对的 unweighted full-quadric \(\Delta_{\max}=1\) 断言。

## 3. 四维源定理实际说了什么

### 3.1 主结论、方向集推论与内部 contradiction 不是 WP4

- Theorem 1.1，PDF p.3：一个固定集合含每个 \(S^3\) 方向的完整非退化线段，结论为 Hausdorff dimension 4。没有任意 finite-index weighted/shading convex-clustering 输入。
- §11.1，PDF pp.168–169：同一个 bounded Kakeya set 的 lower/upper Minkowski dimension 为4；没有声明对任意凸聚类 family 的统一分辨率常数。
- Corollary 11.1，PDF p.169：由外部 transfer theorem 得 \(\dim_H E\ge1+\dim_H D\)。其假设仍是每个 \(D\) 方向中的非退化完整 segment，不是任意 densely shaded 部分；方向维数小于3时结论也允许 union 小于4。
- 论文 §§3–10 排除的是 **\(\mathcal C(d<1)\) 且 \(H>0\)** 的 bad exact problems。PDF p.25、文本 1330–1333 明写这个范围。不是“任意低维 weighted tube union 都不存在”。

例如固定 smooth quadric patch 上的 affine lines，可以具有非凸 algebraic concentration；在隐藏导数非零的 patch，quadric 本身是一个全时 quadratic test，因而可能有零 horizon。即使相应 signal profile 小于1、某种正 angular exponent 成立，也不能因此把它登记为源证明排除的 positive-horizon problem。这里仅解释量词，不宣称完整 quadric/copies family 的所有 observation 列表均已审查。

### 3.2 正 horizon 的原始方向来源：不是 angular cap 的改名

Theorem 2.17 的具体依赖如下。

| 来源 | 获得的输入 |
|---|---|
| PDF p.21，(2.24)–(2.25) | 同一 Hausdorff cover scale 上，eligible full slopes 有正 outer measure；选 \(M\ge\delta^{-3}/K_0\) 个 \(\delta\)-separated directions，且每条 witness 有 inverse-subpower 时间落入小 covering union |
| PDF p.21，(2.26) | 对全 slope 与 intercept 各自独立 \(O(\delta)\) 平滑后，完整 three-slope prior 密度 \(d\nu_s/ds\le K_0\)；给定 full slope，\(y\)-intercept density \(\le C\delta^{-2}\) |
| PDF p.22，(2.27) | support deficit 给 \(g(1,0)\ge\sigma\)；投影 cap/WP3 给 \(g(0,0)\le0\)；full direction + intercept smoothing 给 \(g(r,u)\le r+2-2u\) |
| PDF pp.22–23，(2.29)–(2.32) | maximize \(g(r,u)-Rr+Su\)，同时选出正 endpoint、\(d=1-R<1\) profile 和 terminal conditional visible-angular cap。这不是由 planks 直接推出 (2.6) |
| PDF p.23，(2.33) | 把 crop 内的 true floor 返回**原未归一化 prior**，crop mass 消去 |
| PDF pp.24–25，(2.34)–(2.39) | 对每个 chart，只用其几何/二次 tests 定义 eligible full-slope 集合 \(\Sigma\)；semialgebraic intercept choice 的 monic cubic Jacobian 给 \(|\Sigma|\le K_0a_{r_0}J_{\rm phys}/q^3\) |
| PDF p.25 | **再使用 (2.26)**，把 slope volume 转成 original prior mass 上界，与 floor 比较得到 \(m(r_0,u_0)\le K_0q^{-3}\)，从而 \(H\ge\sigma/6>0\) |

最后一行是不能漏掉的结构：若 full-slope density 只能控制为 \(N_0^\kappa\) 而非 subpower，同一计算只给

\[
m(r_0,u_0)\le K_0N_0^\kappa q^{-3}.
\tag{S1}
\]

于是只有 observation gain 的指数超过 \(\kappa\) 才迫使正 horizon。用 convex cap 替代这里的 slope density，不能直接测试非凸 quadratic chart 上的全部 eligible traces。

更早的角落界也会改变：visible slope density 为 \(N_0^\kappa\) 时，第三个 (2.27) 变成 \(g(r,u)\le r+2-2u+\kappa\)；用同一 projected-plank 路线最多给相应 shifted zero-depth bound，不再自动有原来的全部 endpoint-selection 输入。

## 4. 从四维 proof 读出的受限 finite-scale 结论

不能仅以“主定理是 Hausdorff”结束审计。Theorem 2.17 在选出有限见证之后，后续 argument 实际不再用一个固定跨尺度的原集合 \(K\)。因此，**若四维主证明及其所有引用输入成立**，其 proof 可作如下受限读出：

> 对每个固定 \(\sigma>0\)，存在小 \(\eta>0\) 与 \(\delta_0>0\)，使 bounded graph chart 内具有 \(\delta\)-separated directions、数量 \(M\ge\delta^{-3+\eta}\) 的 finite line family，若每条有至少 \(\delta^{-1+\eta}\) 个 marked time bins，则 sufficiently small \(\delta\) 时，其 visited-cell union 不能只有 \(\delta^{-4+\sigma}\) 个 cells（固定 constants/enlargements 可吸收）。

这段是 proof-level conditional consequence，未声称论文把它单列为定理，更未宣称本项目已独立证明完整四维结论。

严格的反证读出是：若对某 \(\sigma\) 所有 \(\eta\) 都失败，取 \(\eta_n\downarrow0\)、\(\delta_n\downarrow0\) 的 counterfamily，平滑 full slopes/intercepts 到 \(O(\delta_n)\)。方向 separation 与 cardinality 给 full-slope density \(\le C\delta_n^{-\eta_n}=N_0^{o(1)}\)，marks 给 selected mass \(\ge\delta_n^{\eta_n}\)，cell count 给 \(g(1,0)\ge\sigma\)。finite indices 至多 \(C\delta_n^{-3}\)，cells 至多 \(C\delta_n^{-4}\)，故 smoothing 与 enlarged union predicates 有统一 polynomial tempered bounds。原 2.17 的后续 homogenization、WP3、endpoint selection 与 slope-volume 比较因此构造一个 bad exact problem，与四维 proof 的排除相矛盾。此处 \(\eta\) 的量词正是先固定目标亏损，再以反证对角线选得容差，不能预先固定一个过大的 shading exponent。

### 4.1 它能修补哪个五维初始化步骤

假设 j3版2.17 的最初 source 真有 bounded full three-dimensional **visible** slope density。定义 \(\rho=N_0^{-D}\) 后，保留 normalized duration \(\ge K_0^{-1}\) 的 projected traces；其未归一化 prior 仍受原 full-V density 控制。总质量 inverse-subpower，每个 \(\rho\)-velocity cell 的 prior 质量至多 \(K_0\rho^3\)，所以有至少 \(\rho^{-3}/K_0^C\) 个 occupied velocity cells。选固定 coloring 的一类并取每 cell 一条长-shaded representative，即得 \(\rho\)-separated、direction-rich finite family，全部 shaded cells 都来自原 visited union 的固定 enlargement。

若 \(g(0,0)\) 正，则 visited count 至多 \(K_0N_0^{-\alpha}\rho^{-4}\)，相对于 \(\rho\) 是固定 dimension deficit \(\alpha/D\)；上面的受限 finite-scale consequence 会排除它。subpower chart 范围与代表选择可按源文同样缓慢放宽，损失仍 subpower。

因此 **Theorem 2.17 的专用 zero-depth bound 有一个保留 source 方向密度的替代路径**；不能据 general WP4 失败就断言此专用初始化必然失败。相反，它不适用于 Proposition 2.16 中任意 conditional group/residual，因为那里没有 full-V density 上界。两个调用不能混为一谈。

## 5. Plank cap 为什么不提供上述方向输入

一个满足全部 fulltime-plank 测试的简单例子是：所有 traces 都平行，\(u_i=0\)，intercepts 为 unit spatial box 内的 \(\delta\)-grid，unit weights。任意 rotated spatial box 的边长至少 \(\delta\)，packing 计数给 \(\#\{b_i\text{ in box}\}\le C a_1a_2a_3\)。fulltime containment 只会进一步减少它，故 WP4 的 cap 以 \(A=C\) 成立；direction measure 却为单个原子，不满足任何正 Frostman exponent。

一般对一个 radius-\(r\) slope ball，若仅有 fulltime-plank cap，把 intercepts 分成 \(O(r^{-3})\) 个 boxes，再逐个测试 width \(r\) 的 plank，只得到

\[
\text{slope-ball weight}\le
Cr^{-3}A(r/\delta)^3=CA\delta^{-3},
\]

没有任何 \(r\) 衰减。这是空间 convex clustering 与方向 density 的实际断点，不是措辞差异。

Zahl 2025 survey §4.1（PDF pp.11–12，抽取文本 589–623）给更 relevant 的低 union obstruction：完整 \(SL_2\) quadric family 先有 \(\delta^{-1/2}\) 的凸框超聚集，经 thinning 到 \(\asymp\delta^{-5/2}\) tubes，再取 \(\asymp\delta^{-1/2}\) copies，得满足 convex Wolff 的 \(\asymp\delta^{-3}\) tubes、union volume \(\asymp\delta^{1/2}\)。可以使用此已稀疏文献版本，或本轮已核验 allplank cap 的统一加权 fullfamily 版本；后者以 \(\asymp\delta^{1/2}\) 权重支付原 fullfamily 的坏框，不是忽略它。

方向上的精确区别可单独计算：一条 line 包含于 \(ad-bc=1\)，其 direction \(v\) 必满足 \(v_av_d-v_bv_c=0\)。这在 projective direction space 是二维 quadric，单 copy 只占 \(O(\delta^{-2})\) 个 direction bins；\(O(\delta^{-1/2})\) rotated/trans-lated copies 总计仍只需 \(O(\delta^{-5/2})\) bins。将整族权重归一化并 \(\delta\)-平滑后，完整 three-slope density 必至少为 \(\gtrsim\delta^{-1/2}\)，而非 subpower。其 \(\delta^{1/2}\) union deficit 与 (S1) 的 \(\kappa=1/2\) 正好同阶；不能从这里获得原 2.17 的严格正 horizon 增益。这里的 direction 计数只解释 source 区别，不代替 counterexample agent 对全部 cap/graph-chart/shading 常数的核验。

原稿内部的 positive conditional angular exponent (2.6) 也不等于 full three-slope density，更不等于方向维数3。即使某个 quadric family 可满足一个正 angular exponent，它仍可能被 fulltime quadratic tests 处理为零 horizon，因而与四维主证明相容。

## 6. 更强 polynomial/source 结构没有自动进入一般极值类

Survey §4.1 把排除低复杂度 quadric concentration 的更强条件称为 polynomial Wolff axioms，并指出 direction-separated families 是其来源。这里的引用只说明2025 survey中的结构区分，不声称本轮已核验所有相关 primary proofs 或2026年的最强结果。四维原稿实际采用的是 (2.26) 加特殊 semialgebraic slope-volume argument，而非给每个后继 world 公设一个 uniform polynomial-Wolff bound。

具体归一化成本说明为何不能免费保留最初 full-slope 结构。原 version 2 chart 改变量是

\[
t=t_c+q\tau,\quad y=y_c(t)+Dz,
\quad w\text{ 保留}.
\]

visible slopes 满足 \(V_{\rm old}=y'_c+(D/q)V_{\rm new}\)，hidden slope 满足 \(W_{\rm new}=qW_{\rm old}\)。若旧完整 \((V,W)\) slope density 至多 \(C\)，父完整 prior mass 为 \(\nu(A)\)，则新 conditional prior 的 slope density 只能直接估计为

\[
C_{\rm new}\le
\frac{C|\det D|}{q^{j+1}\nu(A)}.
\tag{S2}
\]

对 true parent \(\nu(A)\asymp n(b)|\det D|\)，其成本是 \(C/[n(b)q^{j+1}]\)，可以是固定原始幂。fulltime crop 的对应成本是 \(C a_u^j/\nu(B)\)。这些并不被原 terminal profile/positive angular cap 删除。原 slope bound 可以在**未归一化祖先 law**上继续保留，但不等于每个当前 normalized world 都有同一个 subpower slope density。

polynomial nonconcentration 也不能不记成本地替换：unnormalized restriction 保留旧 upper bound；conditioning 除以 \(\nu(A)\)，anisotropic affine/time normalization 把新的 isotropic tubes/tests 拉回旧 anisotropic neighborhoods。必须记录相应 determinant、轴长、半代数测试和原始 prior，而不是只调用新世界的 \(\mathcal C(d)\) 两条 axioms。

更直接的逻辑断点是 §4.1（PDF pp.47–48，(4.1)）：\(d_*\)、\(k(d)\) 对 **所有** \(\mathcal C(d)\) 问题优化；Definition 2.6 只有 profile 与 terminal joint angular cap，没有 full raw slope density 或 polynomial Wolff 来源记录。Theorem 2.17 只证明至少存在一个有 source 的 bad problem，不保证实现一般 infimum/supremum 的 sequences 仍有它。即使只沿原 source 做有限次操作，也需保留 (S2) 的加权成本；不能把一般 maximizing sequence 称作原 Kakeya tube family。

可以尝试定义记录祖先的更强类，但必须另证它在 chart normalization、coarsening、terminal completion、subsequences 与同一有限网格 near-optimal selection 中闭合，并重作 universal horizon/critical path。本文没有证明任何此类增强方案不可能；只确认原稿当前的极值类没有提供它。

## 7. 早期 support/cap 不能倒过来填补缺失输入

§6 的物理 support 与 coefficient estimates 已有强前提。官方入库 `06-isotropic.tex` 116–192 行（PDF pp.87–88）证明 \(\#W_p\le Kp^{-(m+d)}\) 时，使用 true packets 的 \(\nu_Q\asymp p^dH^j\)、stable graph lists、每线长 witnesses、joint caps 与 isotropic breadth；梯度 bound 又调用 Corollary 4.13 的真实 \(p_L\) 状态列表和 narrowness 极值。它不是“任意 convex-clustered family 的低 support 定理”。

依赖顺序包含

\[
\text{WP3}\longrightarrow\text{2.16 universal horizon}\longrightarrow
\text{4.3 critical true paths}\longrightarrow
\text{4.7 tangent caps/graphs}\longrightarrow
\text{§6 support/counts}.
\]

因此在 \(j=3\) 升级中，不能先借 §6 support 证明缺少的 WP4 或 universal 2.16，再用它初始化同一 critical path。scalar clustering 的独立二维提升仍可保留，但它不负责填这个四维 projected geometry 缺口。

## 8. 审计结论

1. 现有四维主结论与原稿已核对的中间陈述，不覆盖无方向假设的 WP4。具体缺项是 full source slope density、由此产生的 endpoint/angular selection 与严格正 horizon，而非仅一个“uniform”字样。
2. universal 2.16 的 \(j=3\) 直接证明需要 general WP4；专用 2.17 的 zero-depth 步骤有更强 initial direction source，可能用四维 proof-level restricted finite estimate修补。两者必须分开。
3. known convex-Wolff quadric obstruction 与 source theorem 的方向量词相容；全部 cap 到 WP4 的严格反例转化由本轮并行任务负责。这里没有将较弱或未经核对的 full-quadric 数字当作证据。
4. 新增 polynomial/source 类不是给现有 optimizer 加一句假设：需重证带祖先、尺度、质量和 anisotropic 变换成本的闭合。若没有新的可检验结构，应在本轮源审计结束后改选任务，不把相同断点再等价改写延长。

未完成高维 Kakeya、未给新维数下界，未把旧 survey 反例声称为本项目的新发现。
