# R0006：两法向到全时 flag 的原始列表接口

日期：2026-10-16。任务：N5-FLAG-01。已读 GOAL、STATE、R0006 macro、原稿 §§10.1–10.3 与 Lemma 2.13。本笔记用已入库 PDF 和抽取文本；未下载源码。原文 version 2 为 \(j=2\)，本文 \(j=3\) 命题均是拟推广的条件引理或明确的部分条件反模型，不宣称高维 critical 路径已排除。

问题不是两个 strip 相交后还剩什么维数，而是：在**任意当前 counted incidence 的原始 \(p_L\)** 上，能否恢复整个全时 label，包括法向、法向位置和法向中心速度，并保留完整轨道 assignments 与实际覆盖质量？

## 1. 原二维证明用了两次不同的 near-parallel

以下行号指 `literature/extracted/openai_2026_four_dimensional_kakeya.txt`；PDF 页码同时给出，避免把抽取文本当作 TeX 源码。

| 位置 | 实际结论与用途 |
|---|---|
| PDF p.155，文本 8317–8330，(10.4)–(10.5) | full-layer assignments 保留，\(\nu(Q_j)\asymp n(r_j)q_j^2g_j\)；每条 assigned line 在整个本 block 满足位置与 endpoint velocity tests；later path 不继承每个旧 floor |
| PDF p.155，文本 8334–8339，(10.6) | **同一时刻的嵌套 \(Q_1,Q_2\)**：由 \(D_2=D_1R\)、相对最大轴上界和 child major-axis fullness，得 \(n_1\) 与 \(n_2\) 近。此处尚不是两个时刻的比较 |
| PDF p.156，文本 8360–8394，(10.9)–(10.11) | **同一轨道的两个时刻 \(Q_2(t_0),Q_2(t)\)**：若法向不近，二维两个 velocity strips 交于小球；用当前原始 \(p_1\) 的实际 label list、angular joint cap 及第一 label 的 full prior 数量控制 failure mass |
| PDF pp.156–157，文本 8395–8414 | 固定 \(t_0\)，把第一 label 的 normal 与 normal-center 的两个 affine coefficients 分箱。关键：当前 \(Q_2(t)\) 与第一 label 的**三套数据全都近**，故当前 list 可列出该全时 label 的邻 bins |
| PDF p.157，文本 8415–8427 | \(g_C/g_1\to0\) 的指数来自 \(\alpha_2-\alpha_1\to\infty\)，并将全时 normal 与旧 \(Q_1\) normal 对齐；实际输出仍是原始 tempered predicates |
| PDF pp.157–159，文本 8455–8543 | Lemma 10.3 在已经 known 的全时 atlas 内归一化；不预先要求每个 \(C\) 饱和。完整 priors、世界权重及终端 density factor 精确取消；新的 true packets 才作 saturation |

### 1.1 嵌套 near-parallel 的 \(j=3\) 条件

若 child 在 \(\mathbb R^3\) 真有**两个**长度 \(\ge q_2/K_0\) 的长轴，且 parent 的 minor normal 为 \(n_1\)，原文同样给

\[
\|n_1^TD_2\|\le K_0q_2g_1.
\]

它使 \(n_1\) 在 child 两个长轴上的分量都为 \(O(K_0g_1)\)，故仍与 child 的唯一短轴 normal 近。若只知道 child **最大轴**是 full，则另一个轴可能短，不能作此推断。这不是记号问题：在三维 \(J/q^3\) 只记录两个短轴相对宽度的乘积，不能区分

\[
(q,q,qg)\quad\text{与}\quad(q,q\sqrt g,q\sqrt g).
\]

因此原稿二维的单个 narrowness 优化不能不加证明地变成三维 two-long-one-short 优化。

### 1.2 两时刻 near-parallel 同时负责 label 数据匹配

写一个 normal strip 的 affine signature 为

\[
S(Q)=(n,b,c),\qquad
|n\cdot Y(t)-(b+tc)|\le K_0g
\quad(0\le t\le1).
\]

这里全时误差由 (10.5) 的 block 位置误差 \(K_0qg\) 与 normal velocity 误差 \(K_0g\) 外推得到；\(Y_0,V\) 有界。原稿证明的是当前 \(S(Q_2(t))\) 与参考 \(S(Q_2(t_0))\) 全部相差 \(O(K_0g_2N_0^u)=o(g_C)\)，而不是只知道当前 normal 落在某个 plane 内。即使 normals 已知，漏掉 \(b,c\) 仍不足以重建全时 chart。

在三维，两个独立 velocity strips 交于一个细柱。若柱宽为 \(r\)，有界长方向需 \(O(K_0/r)\) 个 \(r\)-balls 覆盖；只有 \(\pi(B_r)\le K_0r^S\) 时，总 angular 上界为 \(K_0r^{S-1}\)。原假设仅 \(S>0\)，不足以仿照二维得到 power-small mass。如果另有同 prior/原始 point 条件下的 cylinder cap，或 \(S>1\) 且参数有足够余量，这一统计步骤才有新的输入；它仍不是独立法向自动给全时 label 的证明。

## 2. 给定两个参考 signatures，几何与全 prior 可以严格构造

以下是正向的条件引理。每条 eligible 轨道 \(Y_l(t)=Y_{0,l}+tV_l\) 在两个 reference labels 中有全时外推 tests

\[
|n_i\cdot Y_l(t)-b_i-tc_i|\le K_0g_i,
\quad i=0,1,
\quad |n_0\times n_1|\ge\sigma>0.
\tag{F1}
\]

所有参数、\(\sigma^{-1}\) 及坐标变换只有 fixed-exact-problem 的 polynomial bounds。令 \(N\) 为两行 normals 组成的 \(2\times3\) 矩阵。其最小非零 singular value \(\gtrsim\sigma\)。取

\[
y_C(t)=N^T(NN^T)^{-1}
\begin{pmatrix}b_0+tc_0\\b_1+tc_1\end{pmatrix}.
\]

加任意固定的 kernel 方向中心后，(F1) 给一条全时长轴、两个短轴。使用 dual columns 的精确 spatial determinant 为

\[
J_C\asymp \frac{g_0g_1}{|n_0\times n_1|},
\tag{F2}
\]

长轴取固定有界长度，两个短轴长度至多 \(K_0\max(g_0,g_1)/\sigma\)。若统一作正交方截面的 flag，可放大到短宽 \(\varepsilon\ge K_0\max(g_i)/\sigma\)。法向与 \((b_i,c_i)\) 的 rounding 还要小于 \(\sigma\varepsilon/K_0\)，不能只按 \(\varepsilon\) 精度盲目 rounding 后不记 inverse-angle 损失。

固定两个 reference times。其 ordered label pairs 的完整 trajectory assignments 是旧 full assignments 的交集，因各 reference time 的 assignments 不交，这些 intersections 也不交。按 rounded flag signature 合并，仍有

\[
\sum_C\nu_\gamma(C)\le1.
\tag{F3}
\]

完整 \(\nu_\gamma(C)\) 必须是这些完整交集的质量，不是后来某一时刻成功 incidence 的归一化质量。旧单 label floors 不自动给每个交集一个新的 true floor；但 depth-zero fulltime known atlas **不需要**预先具有该 floor，正如原 Lemma 10.3。

### 2.1 reference sampling 的质量成本

对原始 probability priors 与 world weights，令当前路径在轨道上的 duration 为 \(\ell_\gamma(l)\in[0,1]\)，总质量 \(m=\sum\omega_\gamma\int\ell_\gamma d\nu_\gamma\)。三个独立时间全成功的总质量为

\[
\sum_\gamma\omega_\gamma\int\ell_\gamma^3d\nu_\gamma\ge m^3.
\]

若一个可用 independent-normal/reference-signature 事件保留其中 \(\beta\ge K_0^{-1}\) 的总质量，平均可固定两个 reference times，保留当前 incidence 质量 \(\ge\beta\)。仅采 reference pair 的事件质量为 \(\beta\) 时，其轨道权重 \(a(l)\le\ell(l)^2\)；再保留一个 current success，积分 \(a(l)\ell(l)\ge a(l)^{3/2}\)，总质量至少 \(\beta^{3/2}\)。因此 finite 次 sampling 的 inverse-subpower 成本本身不是缺口。需要的话可再按 ordinary/weighted occupation 作源式删轻；不可为后来每个交集登记旧 floor。

### 2.2 真正额外需要的当前-point 条件

若在每个保留的**当前** \(p_L(t)\) 上，有实际 \(L_{\mathrm{pair}}=N_0^{o(1)}\) 列表，可把分配给该轨道的两套参考 signatures（或等价的 flag normal plane 及其两组 affine center coefficients）定位到上述 rounding 邻域，则 (F1)–(F3) 构成 fulltime known flag atlas。把固定符号/normal-plane orientation charts 和有限邻 bins 并入，列表最多增大 \(K_0^C L_{\mathrm{pair}}\)。此处并不需要当前实际出现两条 reference labels，但必须有**恢复两套数据**的 theorem。

一个更便于对照原文的充分条件是：当前 old label 列表大小为 \(L\)，每个当前 label 至多有 \(R\) 个可恢复的 partner signatures，且真实 pair 必在其中；则新列表为 \(K_0^C LR\)。只有 \(R\) actual-subpower 时才是原始 known atlas。旧 assignments 总预算 (F3) 并不控制这个 pointwise partner count；每个单 parent 的 prior floor 也不控制交集的最小质量。

这就是可归约的 **plane-family matching 接口**：不仅匹配 normal plane，还须匹配它的完整 affine normal motion。一个单独固定光滑 plane-family 内能造局部 true atlas，不等于不同 \(Q\)-families 的匹配已经在原始 \(p_L\) 上完成。

## 3. 边界反模型：方向 plane 全局已知，中心运动仍无法低列表恢复

下述模型在拟 \(j=3\) 的 affine-hidden 版本中有完整 8 维 tempered Lebesgue prior、单位时间路径、真 two-long-one-short assignments、own-depth 常数列表与真实 floors。它的真实观测 profile 是 **\(d=1\)**，且没有 \(\alpha_2-\alpha_1\to\infty\) 或 critical certification。它只反驳去掉这些额外几何输入后的通用 “two reference normals + old lists/floors 自动给 fulltime known flag” 命题，**不是**原 Proposition 10.2、高维 \(\mathcal C(d<1)\) 或 Kakeya 的反例。

### 3.1 prior、native test 与旧真 charts

取 \(Y_0\) 均匀于 \([-10,10]^3\)，\(V\) 均匀于 \([-1,1]^3\)，\(\zeta_0,\zeta_1\) 独立均匀于 \([-\eta,\eta]\)。定义

\[
Y(t)=Y_0+tV,
\quad w_0=V_1+\zeta_0,
\quad W=V_2+\zeta_1,
\quad w(t)=V_1+tV_2+\zeta_0+t\zeta_1.
\tag{M1}
\]

取 \(P_*=w\)、\(B=1\)。全部 native bounds 为常数；从 \((Y_0,V,\zeta_0,\zeta_1)\) 到 \((Y_0,V,w_0,W)\) 的 Jacobian 为 1。\(\eta\) 取固定原始幂，故 prior 为 full8 有限半代数、分段常 Lebesgue density，绝非低维奇异 prior。其 raw full-slope density 为 \(\asymp\eta^{-1}\)，所以并不保留最初 Kakeya source 的 subpower 完整斜率密度。

取 dyadic \(q=g\to0\)、\(\eta\le g^2\)，按长度 \(q\) 分块，block 中心为 \(t_i\)。令

\[
n_i=\frac{(1,t_i,0)}{\sqrt{1+t_i^2}},
\quad s_i=\frac{(-t_i,1,0)}{\sqrt{1+t_i^2}},
\quad e_3=(0,0,1).
\]

轨道在本 block 的 label 为：\(n_i\cdot Y(t_i)\) 的 \(qg\)-bin，\(s_i\cdot Y(t_i),Y_3(t_i)\) 的 \(q\)-bins，以及 \(n_i\cdot V\) 的 \(g\)-bin。取这些 bins 的代表值为 \(b_i,b_i^\top,b_i^3,c_i\)，定义中心

\[
y_Q(t)=(b_i+(t-t_i)c_i)n_i+b_i^\top s_i+b_i^3e_3.
\]

每个完整 assigned trajectory 在整个 block 都位于 axes \((q,q,qg)\) 的固定倍盒内；两个 tangent velocities 无需放进 label。测试

\[
P_Q=w-\sqrt{1+t_i^2}\,c_i
\]

误差为 \(O(g+q+\eta)=O(g)\)，hidden derivative 为 1、curvature 为 0。因此 thickness 为 \(a=g\)，spatial determinant \(J_Q\asymp q^3g\)。

在当前 \((t,Y,w\text{-bin})\) 上，即使 hidden-bin 宽仅要求 \(\delta\le g\)，也有

\[
n_i\cdot V=\frac{w(t)}{\sqrt{1+t_i^2}}+O(q+\eta)=\frac{w(t)}{\sqrt{1+t_i^2}}+O(g).
\]

所以 \(c_i\) 只有 \(O(1)\) 个 bins。再用

\[
n_i\cdot Y(t_i)=n_i\cdot Y(t)-(t-t_i)n_i\cdot V
\]

定位 normal anchor，误差为 \(O(qg)\)；tangent anchors 因 bounded speed 定位至 \(O(q)\)。因此 label 在**自身厚度 \(g\)** 的 observation 上已具有 \(O(1)\) 列表，原 terminal \(\delta\le g\) 当然也有。这里严格使用 source 的 exact visible base，未偷用两个时刻观察。

保留 anchor cells 在固定 interior、normal velocity cells 在 \([-1/4,1/4]\) 的那些 labels。在 \((Y(t_i),V)\) 坐标中 prior 密度于该 interior 为固定常数，故

\[
\nu(Q)\asymp(q^3g)g=q^3g^2.
\tag{M2}
\]

每块 assignments 不交；将该 label 的**所有**轨道在整个本块计入，\(m_Q=q\nu(Q)\)。保留路径有固定正质量，例如更小固定盒的 \(Y_0,V\) 在每块始终处于这些 interiors。此模型中 interior 的 native hidden-bin density 为 \(n(a)\asymp a\)，即真实 \(d=1\)，因此

\[
\nu(Q)\asymp n(g)J_Q,
\quad m_Q/q\asymp n(g)J_Q.
\tag{M3}
\]

所以这里并非任意小质量父分割，而是有原始 full-prior true floors 与单位时间总覆盖的边界模型。

\(d=1\) 的 typical-density 说法也可不依赖逐点光滑性严格验证：用 §3.3 的同一 coarea 变换，对全部 \(V_2,V_3\) 积分，\((t,Y,w)\) 的推前 Lebesgue 密度有固定上界，支持处于固定有界盒；任何保留路径 submeasure 仍有这个上界。所以每个宽 \(a\) 的 hidden bin 的 base density 至多 \(Ca\)。而在每个 exact base 上至多有 \(C/a\) 个 bins，总 bounded base volume 给出所有密度小于 \(a/K_0\) 的 sampled entries 的总质量至多 \(C/K_0\)。在所需有限网格上同时删去这些异常后，typical density 的指数就是 1；没有把形式参数误作实际 \(d<1\)。

### 3.2 参考 pair 有真正全时 flag，但当前列表不够

参考时刻相隔固定距离时，\(|n_i\times n_j|\gtrsim1\)。两条全时外推 strip 的交给两个短方向，长轴为 **全局同一个 \(e_3\)**。按完整 reference-pair assignments 分组，可得到几何 fulltime flags 与正总 prior/当前 incidence 质量。

但当前观测只给一个 velocity combination \(V_1+tV_2\)；两套 reference normal-center slopes 一起则定位 \((V_1,V_2)\)。全局 normal plane 已完全匹配并不能补足缺少的 center motion。

### 3.3 任意 fulltime known flag 的覆盖上界

严格量词如下：对任意 \(0<\varepsilon\le1\)，考虑任意 family 的 fulltime spatial charts，其一个轴长至多 \(K\)、另两个轴长至多 \(K\varepsilon\)，全时拟合误差也只允许固定 \(K\) 倍；其完整 trajectory assignments 可任意，当前 counted incidences 为 \(\lambda_{\rm atlas}\le\nu dt\)。假设每个真实原始 \(p_L=(t,Y,[w]_\delta)\) 上有一个至多 \(L\) 项的确定列表，包含真实 assigned label。则

\[
\boxed{\|\lambda_{\rm atlas}\|\le C K^C L\varepsilon.}
\tag{M4}
\]

该上界不要求输出 atlas 有 true floors，也不限制其 hidden test；因此已经排除了仅靠更换 tests 恢复足够质量的几何 known atlas。若作为 depth-zero atlas，原 native \(P_*=w\) 本来已可沿完整单位轨道使用。

**证明。** 全时 chart 的 endpoint position tests 使其所有 assigned velocities 落在一个有界长、两 transverse widths 至多 \(K^C\varepsilon\) 的固定 velocity parallelepiped \(T_A\)。方向可随 label 任意改变。任意平面对 \(T_A\) 的二维截面积至多 \(CK^C\varepsilon\)：将盒投影到该平面，其投影面积至多三对相邻边所张面积之和，即 \(O(K^C(\varepsilon+\varepsilon^2))\)，截面积不超过投影面积。

将 measure 从 \((Y_0,V,\zeta_0,\zeta_1,t)\) 变为 \((Y,V,\zeta_0,\zeta_1,t)\)，Jacobian 仍为 1。固定 \(t,Y\) 与噪声 \(\zeta\)，再令

\[
s=w=V_1+tV_2+\zeta_0+t\zeta_1.
\]

从 \((V_1,V_2,V_3)\) 到 \((s,V_2,V_3)\) 的 Jacobian 为 1。固定 \(s\) 后，\(V\) 落在 normal 为 \((1,t,0)\) 的平面上；其 Euclidean 面积与 \(dV_2dV_3\) 只差 \(\sqrt{1+t^2}\in[1,\sqrt2]\)。每一个可用 atlas label 的积分因而至多 \(CK^C\varepsilon\)。已知 exact \((t,Y,s)\) 时，原 terminal list 仍只有 \(L\) 项——它只取决于 \([s]_\delta\)，而非噪声或未观测的 \(V\)。取并集上界得 \(CK^C L\varepsilon\)。

最后对有界 \(Y,s,t\) 积分，并对**归一化**的两个 noise densities 积分；噪声高度 \(\eta^{-2}\) 不产生额外损失。得到 (M4)。等价地，直接在每个 terminal \(w\)-bin 上积分得到 numerator \(CK^C L\delta\varepsilon\)，再对 \(O(\delta^{-1})\) 个 bins 求和。故此证明明确适用于真实终端 bin，不是只控制某个原 reference-pair label，也不依赖 \(\eta\ll\varepsilon\) 或 \(\delta\ll\varepsilon\)。\(q=g\)、\(\eta\le g^2\)、\(\delta\le g\) 只用于建立旧 charts 与其列表，不用于 (M4)。证毕。

若 \(K,L=N_0^{o(1)}\)、\(\varepsilon=N_0^{-c}\)（\(c>0\) 固定），(M4) 是 power-small，不能是 permitted inverse-subpower atlas 的覆盖。甚至允许 exact hidden value 也无助于恢复第二组 velocity/center 数据。

## 4. 若 matching 已给出，10.3 的质量取消可条件性延续

假设前面额外的 matching theorem 确实造出原始 \(p_L\)-known fulltime flag atlas，spatial determinant 为 \(J_C\)，全赋值不交且总 selected mass \(\ge K_0^{-1}\)，native 测试在 spatial normalization 后保持原 hidden coordinate 与 derivative unit。则 Lemma 2.13 的密度换元和世界权重计算本身不依赖 \(j=2\)：

\[
W=\sum_{\gamma,C}\omega_\gamma\nu_\gamma(C)\in[K_0^{-1},1],
\qquad
n'_i(1)\asymp n_i(1)J_C/\nu_\gamma(C).
\]

新 prior 是完整 \(\nu_\gamma(\cdot\mid C)\)，新 world 权重为 \(\omega_\gamma\nu_\gamma(C)/W\)。在已建立相应 \(j=3\) cap class、极值与 true-system 存在理论的条件下，原稿 near-zero packets 的推导给

\[
\frac{\nu_\gamma(A)}{J_A}
\asymp n_i(1)\frac{n'_i(b_i)}{n'_i(1)}
=N_0^{-db_i+o_i(1)+o_{N_0}(1)}.
\]

这里全部 \(\nu(C)\) 与 \(J_C\) shift 精确取消，不要求每个原始 \(C\) 自带 floor。该结果仍只有两极限指数趋零，不是每个固定 exact problem 的 actual-subpower 质量面积比。

标签恢复也按原 PDF p.159 的顺序：在旧 \(p_L\) 先列 \(C\)，其存储 spatial map 确定新 exact base；hidden coordinate、\(B\) 未变，旧终端 hidden bin 对较粗 \(b_i\)-bin 只有有界邻选；再接新 true packet 的 own-depth list。新列表至多 \(2L_C L_{A'}\)。原世界时间预算是 \(\sum\omega_\gamma q_A\nu_\gamma(A)\le1\)，不能替换成逐 parent 归一化后无权求和。

这说明一旦拿到真正的 current-point matching，后续 mass bookkeeping 没有立刻否定 flag 路线；但它也不能反向制造缺失的匹配。三维 flag/narrowness 极值闭合、跨 families 的中心运动匹配及丢短轴后的 native-test 敏感度，仍须各自建立。单一 plane-family 的局部 fulltime 构造不等于这些全局输入已完成。

## 5. 本轮结论

本轮新增了两项可核验内容：

1. fulltime flag known-atlas 的正向条件引理：完整 reference assignments 与足够 paired/current mass 能保留，额外真正需要的是原始当前 \(p_L\) 上的双 signature/normal-motion matching；其后的条件化、密度与标签取消可按 2.13/10.3 精确追踪。
2. full8、真实单位时间、own-depth 常数列表与真实 floors 的 **\(d=1\) 边界反模型**，证明任意 fulltime two-short flag 的 known-list 覆盖至多 \(CK^C L\varepsilon\)。其 long axis 甚至全局固定，故只匹配 normal plane 仍不足，必须匹配中心运动。

仍未得到适用于 \(d<1\)、unbounded optimized flag/positive-horizon critical 路径的 matching theorem，也没有新 Kakeya 维数结论。不可把边界模型冒充该关键路径的反例；若没有新的真实几何输入，应按本轮停止规则冻结此版本，不能只重写双 signature 缺口继续延长。
