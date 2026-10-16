# R0004：真实 assignment 的父质量预算与来源审计

日期：2026-10-16（Asia/Shanghai）。任务：N5-POLY-CAP-01。开始时已读 GOAL、STATE、AGENTS、ROADMAP 与 DIR-001。本轮不重建 R0003 的任意父分割例子，不下载文献。

目标是检查原稿真正的 disjoint trajectory assignments、pointwise observation knowledge 和 true floors 能否改进 DIR-001。结果是一条 **Jacobian 消去的真实层加权不等式**；同时明确为什么 Corollary 4.4、当前极值类及 §6 的局部分支数尚不足以无条件关闭该不等式。

这不是一般 Kakeya 维数下界的提升，也不是满足全部临界路径假设的反模型。

## 1. 源文位置与记号对应

| 位置 | 本轮读取到的真实输入 |
|---|---|
| p.9，Lemma 2.3 后 | known by \(p_s\) 意味着在保留事件上由该点的 observation 决定大小 \(K_0\) 的确定性列表；不是全局标签总数 |
| Definition 2.8，pp.12–13，(2.7)–(2.10) | 同一 world/time block 内 assigned trajectory sets 两两不交；空间矩阵 \(D_c\)、块长 \(q\)；true floor \(m_c/q\ge K_0^{-1}n(b)J_c\)；\(\sum\omega_c q\nu_c\le1\) |
| Lemma 2.10，pp.13–14，(2.11) | 可准备到 \(m_c/q\asymp_{K_0}\nu_c\asymp_{K_0}n(b)J_c\)，并有自身深度 \(p_b\) 的标签知识；true floor 保留 |
| Lemma 2.11，p.14 | later restriction 不自动保留每个旧 floor；可用 frozen witness charging 或重新删轻恢复当前 floor |
| Lemma 2.13，pp.15–17，(2.13)–(2.16) | 父归一化改变 base density 的因子为 \(J_c/\nu_c\)，visible velocity 变换为 \(D_c/q\) |
| Theorem 2.17，p.21，(2.26) | 初始 full-slope density 为 subpower 有界；固定 bounded slope chart 给 initial visible marginal density 上界 |
| Theorem 2.17，pp.23–25，(2.31)–(2.39) | 把 true floor 返回原始 prior 时裁剪概率消去；原稿实际已在正 horizon 归约中保留过这种未归一化质量计算 |
| §4.1，pp.47–48，(4.1) | \(d_*,k(d)\) 对全部 \(\mathcal C(d)\) 优化；类定义不附带初始 full-slope source record |
| Proposition 4.3，pp.48–50 | 控制相对 profile；路径保留 full-layer assignments/priors/witnesses；final path 不自动饱和旧 chart |
| Corollary 4.4，pp.50–51，(4.9) | depth-zero known normalization 保持 maximizing，显式不要求绝对密度指数有界；可慢对角取 \(b_i\to0\) 的真实节点 |
| §4.3，pp.54–56，(4.18)–(4.20) | parent prior 条件于 full assignment；固定 mixture 权重；之后仅限制 incidence law；\(\lambda_A\le K\nu_A dt\) |

本文以 \(\rho_c=\nu_\gamma(A_c)\) 表示完整 assignment 的先验质量，以 \(m_c\) 表示源稿相应的 incidence mass，避免把两者混用。\(J_c=|\det D_c|\)。原文 version 2 的 \(j=2\)；下面公式按一般固定 \(j\ge2\) 写，\(j=3\) 是五维拟推广的条件性应用。

## 2. 新不等式：true floor 消去每父 Jacobian

### 2.1 精确假设

固定一个实际 chart 层；各 time blocks 长度均为 \(q\)，按定义在 \([0,1]\) 内构成 partition。world \(\gamma\) 的权重为 \(\omega_\gamma\)、trajectory prior 为概率 \(\nu_\gamma\)。在每个 block \(I\) 中，\(A_c\) 两两不交。

假设 incoming visible velocity \(V\in\mathbb R^j\) 的边缘有 Lebesgue 密度上界 \(L_\gamma\)。这里直接使用 visible marginal；不要求当前隐藏值或隐藏斜率有额外 boundedness。

每个 chart 的 normalized visible velocity 满足

\[
V=v'_c+F_cV'_c,\qquad F_c=D_c/q,
\qquad |V'_c|_\infty\le T_c\quad\text{在 }A_c\text{ 上}.
\]

此处 \(v'_c=y'_c\) 是固定于 chart 的中心速度，不能依赖被抽取的 trajectory。设准备后的完整 assignment mass 满足

\[
\rho_c\ge\frac{n_\gamma(b)J_c}{K_{{\rm sat},c}}.
\tag{1}
\]

源 Lemma 2.10 给出这样的 \(K_{{\rm sat},c}\)，为相应 exact problem 的 actual subpower。也可以直接由 true floor 推出：若 frozen reference incidence law 受 \(G_{\rm ref}\nu_\gamma dt\) 支配、\(m_c/q\ge n_\gamma(b)J_c/K_{\rm tr}\)，则可取 \(K_{{\rm sat},c}=G_{\rm ref}K_{\rm tr}\)。

令 current incidence submeasure 满足

\[
d\mu_{\gamma,\rm cur}\le G_\gamma\,d\nu_\gamma dt.
\]

它可以是后来的 sparse restriction；不假设其每个 current \(m_c\) 仍满足旧 floor。式 (1) 针对冻结的 full assignment mass。

### 2.2 逐父比例界

取 DIR-001 的规范二次式

\[
k(v')=v'_2-(v'_1)^2,
\qquad B_c=\{l\in A_c:|k(V'_c(l))|\le\eta_c\}.
\]

在 \([-T_c,T_c]^j\) 内，固定除 \(v'_2\) 外的坐标，对 \(v'_2\) 积分可得薄层体积至多

\[
2^jT_c^{j-1}\eta_c.
\]

仿射换元与 visible density 上界给出

\[
\nu_\gamma(B_c)
\le\min\left\{\rho_c,
2^jL_\gamma\frac{J_c}{q^j}T_c^{j-1}\eta_c\right\}.
\]

由 (1)，**每父的 \(J_c\) 精确消去**：

\[
\boxed{
\nu_\gamma(B_c)\le\rho_c\Lambda_c,
\quad
\Lambda_c=
\min\left\{1,
\frac{2^jK_{{\rm sat},c}L_\gamma T_c^{j-1}\eta_c}
{n_\gamma(b)q^j}\right\}.}
\tag{2}
\]

这比只知道“父数量 polynomial”更强。它使用真实 true floor/assignment 关系；R0003 任意父分割的 sharp 例子没有提供 (1)，不能据其否定 (2)。

### 2.3 同层的 world/time 加权界

先验薄层事件不依赖 block 内的当前时间，因而

\[
\mu_{\gamma,\rm cur}(B_c\times I)
\le G_\gamma q\rho_c\Lambda_c.
\]

使用所有 world 和 time block 的同一权重，得到

\[
\boxed{
\mathcal B_{\rm layer}
\le\sum_\gamma\omega_\gamma G_\gamma
\sum_{I}\sum_{c\text{ in }(\gamma,I)}q\rho_c\Lambda_c.}
\tag{3}
\]

同时，由 disjoint assignment 与 time partition，

\[
\sum_\gamma\omega_\gamma\sum_I\sum_cq\rho_c\le1.
\tag{4}
\]

如果该层的 \(n(b),q,L,T,K_{\rm sat},G\) 有共同上界/下界，则

\[
\boxed{
\mathcal B_{\rm layer}
\le G\min\left\{1,
\frac{2^jK_{\rm sat}LT^{j-1}\eta}{n(b)q^j}\right\}.}
\tag{5}
\]

原始 \(\mu\le\nu dt\) 时 \(G=1\)；prepared parent law 一般须保留 \(G\le K\)。不能丢掉这个因子，也不能把原 world 权重改成每个父的归一化概率后仍使用 (4)。

等价地，true saturation 与 assignment budget 给出加权体积预算

\[
\sum_{\gamma,I,c}\omega_\gamma qJ_c
\le\frac{K_{\rm sat}}{n(b)},
\]

再把 DIR-001 逐父 slope-volume bound 先乘 \(q\) 后求和，也得到 (5)。这个证明只使用冻结 prior；不从 final path 的小质量错误恢复每个旧 packet 的 floor。

### 2.4 一般方向二次式必须使用平方根薄层

上面的线性 \(\eta\) 只针对 \(k(v')=v'_2-(v'_1)^2\)。若改成在固定有界盒上系数归一化的任意非零次数不超过 2 多项式 \(Q(v')\)，统一可用的是

\[
|\{|Q(v')|\le\eta\}\cap[-T,T]^j|
\le C_{j,T}\sqrt\eta.
\]

系数范数上下界和盒尺度中的损失须一并计入 \(C_{j,T}\)；prepared 情形若这些量及其逆受 \(K\) 控制，可吸收为 \(K\) 的固定幂。平方线性式已经达到平方根量级，未证明横向一阶导数下界时不能改成线性界。式 (2)–(5) 对这样的事件仍成立，但应把 \(2^jT^{j-1}\eta\) 换成 \(C_{j,T}\sqrt\eta\)。若每父有 \(R\) 个不同多项式，则并集体积上界为 \(R C_{j,T}\sqrt\eta\)，不能写成 \(C_{j,T}\sqrt{R\eta}\)。统一记单事件体积模量为 \(\Psi(\eta)\)：特殊抛物式可取 \(\Psi=\eta\)，一般二次式只能取 \(\Psi=\sqrt\eta\)，常数另留。

## 3. 归一化如何保留同一代价

归一化到父 \(A_c\) 后，new prior 是 \(\nu_\gamma(\cdot\mid A_c)\)，visible coordinate 是 \(V'_c\)。因此其 visible density 上界可取

\[
L_c^{\rm new}
\le\frac{L_\gamma|\det F_c|}{\rho_c}
=\frac{L_\gamma J_c}{q^j\rho_c}
\le\frac{K_{{\rm sat},c}L_\gamma}{n_\gamma(b)q^j}.
\tag{6}
\]

这就是 (2) 中的代价。它不需要通过隐藏斜率范围再作一次粗估计。

当父为已准备 true parent、标签在自身深度可知时，Lemma 2.13 的等号情形给 \(n_c^{\rm new}(0)\asymp1\)。但这不使 full-direction density 成为 subpower；\(L_c^{\rm new}\) 已经吸收了 \(1/[n(b)q^j]\)。

更一般地，若 intermediate density equality 成立，则

\[
n_c^{\rm new}(0)\asymp n_\gamma(b)J_c/\rho_c,
\qquad
\frac{L_c^{\rm new}}{n_c^{\rm new}(0)}
\lesssim\frac{L_\gamma}{n_\gamma(b)q^j}.
\tag{7}
\]

因此把 \(n(0)\) 重置为 1 不是免费恢复原始 full-direction 信息；同一成本会出现在 visible palette 的密度上界中。

## 4. Corollary 4.4 的 near-depth-zero 能给什么

### 4.1 可以严格推出的条件性排除

设沿某个 maximizing sequence 有 near-zero true nodes \(b_i\to0\)，其 horizon exponents \(h_i\to0\)。Corollary 4.4 和 Proposition 4.3 给相对 profile

\[
f_i(b_i)-f_i(0)=o_i(1)
\]

（这里不需要未经检查地把所有 horizon errors 都写成 \(o(b_i)\)）。于是

\[
n_i(b_i)q_i^j
=n_i(0)N_0^{-o_i(1)+o_{N_0}(1)}.
\tag{8}
\]

如果额外具有

\[
L_i/n_i(0)\le N_0^{o_i(1)+o_{N_0}(1)},
\]

并保留 source actual-subpower 的 \(G,K_{\rm sat},T\)，则对任意固定 \(c>0\) 和 \(\eta_i\le N_0^{-c}\)，特殊抛物式的 (5) 给

\[
\mathcal B_{\rm layer}
\le N_0^{-c+o_i(1)+o_{N_0}(1)}.
\tag{9}
\]

先取 \(i\) 足够大，再取其 exact sequence 内的 \(N_0\) 足够大，就得到 power-small bad mass，不能承载 inverse-subpower 的原始路径质量。这是一条适用于真实 assignments/floors 的新充分条件，不是任意父的概率重述。

一般二次式在相同假设下把 (9) 的指数 \(-c\) 换成 \(-c/2\)，仍然 power-small。

若还额外把深度与 horizon 的相对误差慢对角到 \(o(b_i)\)，则可将 (8) 细写成

\[
n_i(b_i)q_i^j
=n_i(0)N_0^{-(d_*+jk)b_i+o_i(b_i)+o_{N_0}(1)}.
\]

这个更细形式需要该相对精度选择；本轮不把 Corollary 4.4 原陈述的“趋于 0”直接换成它。

### 4.2 原 Corollary 不提供缺失的额外条件

Corollary 4.4 明确不要求绝对 \(f_i(0)\) 有界，并只把 \(f_i(r)-f_i(0)\) 放入 profile 结论。\(n_i(0)=N_0^{-f_i(0)}\) 因而不能在 (8) 中删去。

此外，Corollary 的第一部分要求 depth-zero、horizon-zero known normalization 具有 actual subpower success 和 terminal knowledge；不是任意小父都可以作为这样的 normalization。即便 true-parent normalization 使 \(n^{\rm new}(0)\asymp1\)，(6) 也表明 full-direction density 的条件化代价没有消失。

所以原 Corollary 单独不推出 (9)。它提供一个明确、可使用的接口：需要控制的是同一坐标/先验下 \(L_i/n_i(0)\)，而非只要求 \(b_i\to0\)。

## 5. Full-slope 来源在当前优化中的位置

### 5.1 Theorem 2.17 真正保留过 raw 预算

最初 smoothed counterexample 的 full-slope density 在固定有界 chart 上受 (2.26) 控制，因此 initial visible marginal 可取 \(L\le K_0\)。但是 Theorem 2.17 随即按 full-time \((y_0,V)\) crops 条件化，并将 \(y\) 缩放。

原稿 (2.31)，p.23，给出了精确变换

\[
n_{\rm new}(s)\asymp n(s,u_0)\frac{a_{u_0}^{\,j}}{\nu(B)}.
\]

visible density 同样可估为

\[
L_{\rm new}\le L_{\rm old}\frac{a_{u_0}^{\,j}}{\nu(B)}.
\]

两者的 ratio 中 crop 质量再次消去，但留下 \(L_{\rm old}/n(0,u_0)\)，并不自动为 subpower。Theorem 2.17 后半 pp.23–25 正是把 true floor 返回未归一化 original prior，再用 full-slope volume 支付，而不是宣称每个 crop 的条件方向律仍然 subpower 密度有界。

### 5.2 当前 C(d) 优化没有自动携带这份来源

§4.1 的 (4.1) 对所有 \(\mathcal C(d)\) 中 bad problems 定义 \(d_*\) 和 \(k(d)\)。Theorem 2.17 只保证至少有一个带 raw Kakeya source 的 bad problem，不能据此证明任意实现该 infimum/supremum 的 maximizing sequence 都有同一 source 记录。

因此，不能把初始 (2.26) 直接套给 Proposition 4.3 的每个 world。该问题是优化类中未保留额外结构，不是 (2.26) 本身有误。

### 5.3 哪种增强类可能闭合，哪种并不闭合

简单增强类“每个当前 world 的 visible marginal 都有 \(L\le K_0\)”一般不在 chart normalization 下闭合，因为 (6) 的放大因子可以是固定原始幂。

但这**不证明所有保留来源的增强方案都不能闭合**。可以考虑显式记录：初始 raw trajectory prior、其 full-slope 密度、每个后继 world 的 raw assignment、累计 visible affine map、累计 time map、world 权重与条件化质量。原稿 Lemma 2.13 的 operations 是条件化及固定 affine base/time changes，形式上可把这些 records 继续复合，逐层保留原始加权预算。

尚缺的是将这种增强类正式定义后，检查它在 coarsening、再归一化、长度换底、进一步 selection 和 outer maximizing subsequences 下均保留可用的统一预算，并重新建立 Proposition 4.3 所需的极值/相对 profile 论证。原稿没有完成这一增强版证明，本笔记也没有把“可记录祖先”直接当成“增强优化闭合且给出 smallness”。

## 6. §6 的实际 q 家族还有哪些质量损失

以下 TeX 行号均指已入库、核对过版本的 `literature/primary/openai_4d_source/06-isotropic.tex`。

- 行 54：每个状态包含 parent world 与标签；它们不是被整个证明统一掉的背景。
- 行 93–100：\(\nu_Q\asymp a^dh^j\)，是该 parent prior 内的完整 assignment 质量。
- 行 937–958 起（PDF p.97）：先选一个 parent 和 \(Q\)，再开始固定插值用方向 tuple。
- 行 1272–1286（PDF p.101）：势 \(P\) 从这个局部 field \(T\) 构造。
- 行 1289–1303：截距 \(C\) 按每条轨道中点分箱，组内 base ceiling 为 \(K(a_2/a)^d\)。
- 行 1344–1354：heavy group floor 为 \(h\nu_Q(a_2/a)^d/K\)。
- 行 1655–1668（PDF p.105）：在固定本次 \(P,Q\) 后有至多 \(K(a/a_2)^d\) 个 group/core/sign choices，选中一支获得对应质量与长见证。
- 行 1763–1776（PDF pp.106–107）：\(q\) 是该选择的分支 \(f\) 在其 core center 的 Hessian，按 \(S_0\) 归一化。

因此 \(q\) 不是每个 full true parent 上唯一先验给定的多项式。令

\[
\vartheta=(a_2/a)^d.
\]

一个选中 branch 的 prior mass 只能由 incidence floor 推出 \(\gtrsim\nu_Q\vartheta/K\)，不能未经说明换成 \(\nu_Q\asymp n(b)J_Q\)。在使用 (2) 时，要么显式支付 \(\vartheta^{-1}\) 的条件化代价，要么用在固定 \(P,Q\) 内至多 \(K\vartheta^{-1}\) 个 choice 的计数。

这里的 prior 下界使用同一支的 \(\lambda\le K\nu\,dt\) 与块长 \(h\)，故所有 domination 和 branch-floor 常数都要保留。更直接地，若固定每父一支 \(B_Q\)，其 incidence mass 至少 \(h\nu_Q\vartheta/K_{\rm br}\)，而逐父先验薄层比例上界为 \(\beta_Q\)，则该支落在薄层的 incidence 比例至多 \(\min\{1,GK_{\rm br}\beta_Q/\vartheta\}\)。不必给这支登记原父的 true floor；同一个 \(G\) 只支付一次。

后一计数**不跨越所有 residual、所有插值 choices 与所有 potential \(P\)**。原稿候选的存在性和 Proposition 4.11 的 greedy implementation 不给出一个所有可能 \(q\) 共用的 \(K\vartheta^{-1}\) 全局 palette。

更具体地，如果一个后续证明确实给出每个 true parent 至多 \(R_Q\) 个固定的方向二次式，每个事件的原始 thin-volume 估计都适用，那么 (5) 中的单事件体积要替换为 \(R_Q\Psi(\eta)\) 的相应 union budget。若可用 \(R_Q\le K/\vartheta\)，便出现

\[
\frac{K L\Psi(\eta)}{n(b)q^j\vartheta}.
\tag{10}
\]

源稿 (6.34)–(6.36) 一般只给 primary-quadric 集中精度 \(\eta=Kh\)，没有自动给出 ALG-004 特殊模型中的超细 shear 精度。以一个已归一化 parent 内的 \(n\asymp a^d\)、\(q=h=a^k\)、\(a_2/a=h^e\) 为例，(10) 对任意归一化 primary Hessian 的主要幂为

\[
\frac{h^{1/2-ed}}{a^d h^j}.
\]

即使额外证明特殊抛物型的线性薄层估计，所得也只是 \(h^{1-ed}/(a^dh^j)\)。当 \(j\ge2\)、\(d\ge0\)、\(k>0\) 时，两者均不趋于 0。这个计算不是证明整个路线无效，而是防止把真实 branch 阈值和可用 thin precision 在应用 DIR-001 时漏掉。

### 6.1 \(Kh\) 薄层实际上约束哪一批轨道

行 1780 只显式写了被选中的七个 tuple 方向，不能直接把这一句当成 full prior 上的事件。但同一支的其余已计贡献轨道也满足相同阈值，理由如下：

1. 行 1661–1668（PDF p.105）的一个固定 branch/core 中，每条 contributing line 有同一选择内的长见证，见证及当前计数点在 \(U\)，chords 在受控域。行 1699–1708（PDF p.106）因此对**每条这样的线**在其 incidence \(u\) 给出 \(|D_{\mathbf v}^2 f(u)|\le Ka_2\)。这里 \(\mathbf v=(1,v)\) 为 normalized base-time direction；行 942–945 对时间、空间同时用 \(u=(z-z_c)/h\)，无 velocity shear，故不会再出现单独的时间缩放因子。\(v\) 对同一 affine trajectory 是常数，且 prepared directions 受 \(K\) 控制。
2. 用选中七个方向完成张量反演后，行 1740–1754 给出整个 \(U\) 的 \(\|\nabla^3f\|\le K(a_2+S_0h)\)。这是场的统一导数界，不仅是在七条线上。对任意上述 contributing line，把 Hessian 从其 incidence \(u\) 沿 \(U\) 的线段移到 core center \(u_c\)。\(U\) convex、其直径及方向范数为 \(K\)-有界，故

   \[
   |\nabla^2 f(u_c)[\mathbf v,\mathbf v]|
   \le Ka_2+K(a_2+S_0h).
   \]

3. 在行 1763 的 conic case 中 \(S_0>a_2/h\)，按行 1767 定义 \(q_{\rm Hess}(x)=\nabla^2 f(u_c)[x,x]/(2S_0)\)，于是对**此固定支内所有仍计数的 contributing trajectories**，

   \[
   |q_{\rm Hess}(1,v)|\le K(a_2/S_0+h)\le Kh.
   \tag{11}
   \]

\(q_{\rm Hess}\) 对这一支是固定的；其系数范数由行 1774–1779 夹在 \(K^{-1}\) 与 \(K\) 间。故在 fixed bounded velocity box 上可对式 (11) 用 §2.4 的通用平方根薄层。这个推导允许把当前 **branch incidence mass** 放入方向事件，不声称同一 full assignment 中尚未入该支、缺少此 branch 见证的轨道都满足 (11)。五维拟推广要先另证对应的三阶导数界；R0001 五方向引理只补其代数反演步骤，并未补齐全部几何准备。

## 7. Pointwise knowledge 不等于原始多项式数量

Lemma 2.10 的 crossing argument 控制的是在同一 observation 上同时兼容的标签数量，积分形式为

\[
\int T(p_b)\,d\mu_{\rm cap}
\le K_0\sum_c\omega_{\gamma(c)}n(b)qJ_c
\le K_0\sum_c\omega_{\gamma(c)}m_c.
\]

Markov 给 pointwise \(K_0\)-lists。这里 observation 含连续的 exact base，标签可以在互不相交的空间区域改变；积分交叠界不限制所有不同区域出现了多少不同系数多项式。

源 Proposition 4.3 又明确保留 full-layer assignments 与先验，final path 可能只是它们的小子集。不能用 later incidence intersection 的小质量来减少原 full-label family，也不能对每个原标签重新归一化后声称总 mass 仍为 1。

若把一个局部方向二次式退回原始 visible 坐标，必须写

\[
\widetilde q_c(V)=q_c\bigl(1,F_c^{-1}(V-v'_c)\bigr),
\]

再除以其系数范数；thin threshold 同时除以该范数。chart 的 \(\|F_c\|\le K_0\) 和中心速度界可以防止一个已规范化的局部二次式退回后系数范数任意变小，但不把不同父的这些多项式自动匹配为少量共同 centers。

所以 DIR-001 的 global coefficient-palette 准则仍需要真正的新匹配、低数量或加权 covering 定理。现有 pointwise knowledge、polynomial 总标签数和 true floors 单独没有给出该准则中的小 \(R\)。本轮没有构造满足全部 bad critical-path 条件而使 palette 大的反例，因此不把这个“尚未推出”夸大为完整不可推出定理。

## 8. 本轮验收与下一输入

本轮新增的严格结果是 (2)–(5)：在实际 disjoint assignments 与 frozen true-floor 下，父质量下界消去逐父 visible Jacobian，得到与父数量无关的 weighted 层预算。另给出归一化成本公式 (6)–(7) 和 near-zero 的明确充分条件 (9)。这些是可供接入真实数据的条件不等式，没有宣称新颖性。

当前未闭合的三个接口是：

1. 极值类是否保留足够强的 raw full-direction 祖先记录及其加权密度预算；
2. 真实选择中 \(L/n(0)\) 与 branch 条件化阈值能否同时被控制；
3. 能否获得比源稿普遍 \(Kh\) 更强的方向多项式精度，或一个真正小的原始 coefficient palette。

按本项目的单主轮停止条件，本轮不继续以相同素材反复改写 palette。若没有额外来源约束闭合以上接口，应转向同一原始分辨率的全斜率 \((V,W)\) 信息预算；不得把可见方向的熵再次误当作空间纤维维数。
