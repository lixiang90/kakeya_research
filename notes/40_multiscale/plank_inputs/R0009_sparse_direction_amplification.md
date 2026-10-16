# R0009：稀疏方向放大；有界 shear 复制与 SRC-001 接口

日期：2026-10-17。主任务 N4-DIR-01 的互补核查1。作者：audit_four_dimensional。状态：下列放大 lemma 为自包含初等论证，已经lifting_obstructions独审及root接口复核，见research/reviews/R0009_amplification_review.md及R0009_root_integration_review.md。最后一步使用 SRC-001，始终以完整四维论文及其输入正确为条件；本项目没有独立重证175页证明，也不据本 lemma 宣称新 Kakeya 结果。

本稿按 root 的后续指导采用有界 spacetime shear，替代最初提议的欧氏旋转。输出仍是 SRC-001 允许的有界四维 graph family，且原 time coordinate 保持不变。因而不必解决旋转后切换 time chart、丢失短段或 marks 集中在坏时窗的问题；下文也不声称已另外证明“只准欧氏旋转”的版本。

## 1. 精确输入、输出与允许的常数

固定 \(R\ge1\)。输入 \(M\ge1\) 条 indexed graph lines

\[
 L_i(t)=(t,b_i+t v_i),\qquad 0\le t\le1,
 \qquad |b_i|+|v_i|\le R.
 \tag{1.1}
\]

假设 slopes \(v_i\) 彼此 \(\delta\)-separated；若输入按单位方向或 projective direction metric 表述，可由 bounded-chart bi-Lipschitz 等价将 \(\delta\) 乘一个只依赖 \(R\) 的常数。每个 \(J_i\) 为 \(\delta\)-time bins 的子集，\(\#J_i\ge\delta^{-1+\eta}\)。原 marks 在 time-bin centers 上记录，\(E\) 为所有 marked visits 所在四维 \(\delta\)-cells。允许将与 marked trace 相交的所有 cells 纳入 \(E\)，这只加强以下 upper。

**放大结论。** 取一个固定 dyadic 倍数 \(\rho=C_*\delta\)，例如 \(C_*=8\)。存在

\[
 K\le C_R\frac{\delta^{-3}}{M}
 \tag{1.2}
\]

个有界 shifts \(a_k\in\mathbb R^3\)，从其 shear copies

\[
 S_{a_k}(t,y)=(t,y+t a_k),\qquad
 S_{a_k}L_i(t)=(t,b_i+t(v_i+a_k))
 \tag{1.3}
\]

中可抽出一个 family \(\mathcal F\)，使：

1. 所有输出 lines 在同一个仅依赖 \(R\) 的 bounded graph chart 中；其单位方向彼此至少 \(\rho\)-separated。
2. \(\#\mathcal F\ge c_R\rho^{-3}\asymp_R\delta^{-3}\)。不要求每个方向都出现，只要求常数比例的最大可能数量。
3. 每条输出 line 在 \(\rho\)-time 网格上保留至少 \(c_R\delta^{-1+\eta}\) 个 marks。
4. 输出 marked union \(E_\rho'\) 满足

\[
 \#E_\rho'\le C_R K\#E.
 \tag{1.4}
\]

常数不依赖 \(M,\delta\)、截距与具体 marks 的分布。只需 \(\delta\) 小于一个固定 chart 常数。\(M\le C_R\delta^{-3}\) 本已由输入 separation 与 bounded slopes 得到，因此 (1.2) 包含极稀疏 \(M=1\) 和近满方向两端。

## 2. 随机平移只填正方向体积，不需要 coupon collector

令

\[
 U=\bigcup_{i=1}^M B(v_i,\delta/10)\subset\mathbb R^3.
\]

这些球互不相交，所以

\[
 |U|=c_3 M\delta^3.
 \tag{2.1}
\]

取固定目标盒 \(Z=[-1,1]^3\)，以及足够大的固定 shift 盒 \(Q_R=[-A_R,A_R]^3\)，使每个 \(z\in Z\) 都有 \(z-U\subset Q_R\)。例如 \(A_R=2R+4\) 足够。若 \(a\) 在 \(Q_R\) 上均匀，则对每个 \(z\in Z\)，

\[
 \Pr\{z\in U+a\}=\frac{|U|}{|Q_R|}=:p.
 \tag{2.2}
\]

取独立 \(a_1,\ldots,a_K\)，其中 \(K=\lceil1/p\rceil\)。于是

\[
 K\le C_R(M\delta^3)^{-1},
 \qquad
 \Pr\{z\in\bigcup_{k=1}^K(U+a_k)\}
 =1-(1-p)^K\ge1-e^{-1}.
 \tag{2.3}
\]

对 \(z\in Z\) 积分可知，存在一个确定的 shift 选择使

\[
 \left|Z\cap\bigcup_{k=1}^K(U+a_k)\right|
 \ge (1-e^{-1})|Z|.
 \tag{2.4}
\]

这是方向邻域的正体积覆盖。没有声称覆盖全部方向，也没有要求同时命中所有方向 cells，所以不需要再乘 \(\log\delta^{-1}\)。常数中包含固定 \(|Q_R|\)，并不依赖原方向集合的形状或稀疏程度。

## 3. 提取 near-full separated family

所有复制后的 slopes 都在固定盒 \(\{|v|\le B_R\}\) 中。单位正时间方向

\[
 d(v)=\frac{(1,v)}{\sqrt{1+|v|^2}}
\]

在这个盒上与 slope distance 定量 bi-Lipschitz。取固定 \(H_R\ge1\)，使 \(|v-v'|\ge H_R\rho\) 蕴含单位方向距离至少 \(\rho\)。

在有限 center 集合 \(\{v_i+a_k\}_{i,k}\) 中抽一个 maximal \(H_R\rho\)-separated 子集 \(T\)。若同一个 slope 有多个 indices，只取其中一个；其对应 line 原有 marks 完整保留。极大性说明每个 center 距 \(T\) 中某点小于 \(H_R\rho\)。因此

\[
 \bigcup_k(U+a_k)
 \subset\bigcup_{v\in T} B(v,H_R\rho+\delta/10).
\]

由 (2.4)，

\[
 c_R\le C_R\#T\,\rho^3,
 \qquad \#T\ge c_R\rho^{-3}.
 \tag{3.1}
\]

每个 \(v\in T\) 选择一个实际 pair \((i,k)\)，并取实际 line \(S_{a_k}L_i\)，得到 \(\mathcal F\)。该抽取不需要恢复截距标签，也不对原先验重新赋权；本 lemma 处理的是有限 unweighted representatives。所有 output directions 均在 graph chart 内且单位方向 separated；没有借 projective chart 边界处的退化实现虚假的 separation。

## 4. Time marks、重新分箱与 cell union

### 4.1 原时间保留

Shear 的第一个坐标正是 \(t\)。故每个原 \(\delta\)-time mark 仍在同一个 \(t\) 上；不会因 direction 旋转而变成极短时间窗，也不会因选择 common chart 而丢弃 marks。截距仍为 \(b_i\)，slopes 有界于 \(R+A_R\)，所以整条输出 graph line 在 \([0,1]\) 上有统一位置与速度界。

### 4.2 固定尺度 \(\rho=C_*\delta\) 重分箱

令 \(J'_{i,k}\) 为含至少一个原 marked center 的 \(\rho\)-time bins。在每个这种 bin 的新 center 上记录输出 line。每个 \(\rho\)-bin 最多包含 \(C_*+1\) 个原 \(\delta\)-time centers，因此

\[
 \#J'_{i,k}\ge\frac{\#J_i}{C_*+1}
 \ge c_R\delta^{-1+\eta}.
 \tag{4.1}
\]

这不要求 marks 均匀分布：即使全部 marks 集中在一个短时窗，单个新 bin 能合并的原 marks 仍至多固定个。

### 4.3 新 time-bin center 的空间误差也有统一控制

原标记点是 \(L_i(t_j)\)，shear 后为 \(S_{a_k}L_i(t_j)\)。将其移到同一个 \(\rho\)-bin 的新 center，time 距离至多 \(\rho/2\)，整条 graph 的 Euclidean 速度统一有界，所以新四维点距该 shear image 至多 \(C_R\rho\)。

对每个 \(a_k\)，线性图 \(S_{a_k}\) 的 operator norm 统一有界。一个原四维 \(\delta\)-cell 经其像，再扩大 \(C_R\rho\)，至多碰到 \(C_R\) 个四维 \(\rho\)-cells，因为 \(\rho/\delta=C_*\) 固定。故所有复制后的 visits 满足

\[
 \#E_\rho'\le C_R K\#E.
 \tag{4.2}
\]

再抽 separated 子族只会减少 union。不需要把 \(\delta\)-cell 的精确 image 当作 axis-aligned cell，也没有对每条 line 单独计算一遍原 \(E\) 而额外付出 \(M\) 倍。

## 5. SRC-001 的精确量词接口

现在才引入条件输入。假设 SRC-001 成立：对任意固定 \(\sigma>0\)，存在 \(\eta_{\rm src}>0\) 与小尺度阈值，使 bounded four-dimensional graph chart 中，若方向 \(\rho\)-separated 数量至少 \(\rho^{-3+\eta_{\rm src}}\)、每条至少 \(\rho^{-1+\eta_{\rm src}}\) 个 time marks，则

\[
 \#E_\rho'\ge\rho^{-4+\sigma}.
 \tag{5.1}
\]

这里的 chart 常数固定为前文的 \(B_R\)，因此 \(\eta_{\rm src}\) 与 threshold 可以依赖原 \(R\)，但不依赖 \(M\) 或具体 family。

在原输入选

\[
 0<\eta\le\min(\eta_{\rm src}/2,\sigma/2,1/4).
 \tag{5.2}
\]

则对足够小 \(\delta\)，(3.1) 给 \(\#\mathcal F\ge\rho^{-3+\eta_{\rm src}}\)，(4.1) 给每条 \(\#J'\ge\rho^{-1+\eta_{\rm src}}\)。固定倍数、固定 coloring/separation 常数与新网格原点都已被 \(\eta_{\rm src}-\eta>0\) 的幂余量吸收，不能在没有余量时直接删除这些常数。

由 (1.2)、(4.2)、(5.1)，得到

\[
 \boxed{\#E\ge c_{R,\sigma}\,M\delta^{-1+\sigma}.}
 \tag{5.3}
\]

这是对任意稀疏 \(1\le M\le C_R\delta^{-3}\) 都一致的 conditional unweighted consequence。特别地 \(\sum_i\#J_i\le M\delta^{-1}\) 给

\[
 \sum_i\#J_i\le C_{R,\sigma}\delta^{-\sigma}\#E.
 \tag{5.4}
\]

若主任务需要最终 \(\varepsilon\) 损失，可以先以更小 \(\sigma\) 调用 SRC-001，再把余量留给权重分组/方向抽样；本稿不擅自把这个余量用完后宣称 arbitrary-weight 版本已经证明。

## 6. 已核验的边界与未证明内容

- \(M=1\) 时可以使用 \(O_R(\delta^{-3})\) copies；原单线 marks 在每个 copy 上仍满足同一逐线条件。没有暗中要求 \(M\) 接近最大方向数。
- 近满方向时 \(K=O_R(1)\)。任意几何形状的稀疏方向集合均由 (2.2) 同一平移概率处理。
- 不追求每个方向都覆盖，故正方向体积足以且无需对数 copies；这是 SRC-001 的 near-full cardinality 量词所允许的。
- 截距、斜率、空间位置和 shear operator norm 都是固定 chart 常数；不会引入 \(\delta\) 的幂成本。
- marks 可以完全不均匀；保留它们只用了固定 time 网格的 bounded merging。
- 本稿没有证明加权 indices 的代表抽样、任意权重跨度处理，亦没有将 direction-bin cap 偷换成 actual Lebesgue density。那是主任务的另一接口。
- 本稿的初等放大本身无条件；只有从 (5.1) 到 (5.3) 的四维几何下界依赖 SRC-001，进而依赖完整四维证明及其输入。无方向 WP4、原 generic \(j=3\) horizon 上界均未被重新使用。
