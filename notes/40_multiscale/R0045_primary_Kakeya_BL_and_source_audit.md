# R0045：原四臂、精确 Kakeya–BL 输入与原计数预算

日期：2026-10-17。范围：实际 WZ `d=5,k=ell=3`，以及所需的有限仿射平面估计。本稿不是完整分支证明；没有得到五维新维数界或 `kappa<=zeta`。以下初等推导待本轮独立审查，未经外部同行评审。

## 1. 当前命题、原假设和停止条件

先读恢复入口、R0045 opening macro/spec 和 R0044 退出稿。当前唯一缺口是：能否从原 good-q、原整管、原 marks 和原角先验中，保留 inverse-subpower 的四臂质量，使四个 rank-2 正态映射的 **有限尺度 BL 常数** 足够小，并在实际端点字母表/纤维预算之后产生严格增益。

固定 `zeta,gamma>0`，然后选择小 `eta`，再选小 `delta`；`kappa>=zeta`。保留 Def17.2–17.4 的 AD4、CW、bounded joint chart、逐点 used `Phi_p` 的 slab cap、逐层 `Y_z` 的 tube-KT 和原均匀整管 law。PW 只可在 R43 已付的同 law/共同 affine 操作范围调用。本轮不能把这些先验替换为独立的时间/角/端点 product law。

独立反攻包括：三臂、同时间、同原管、同原起点的不同管；有限尺度与 scale-invariant BL 的区别；任意选中 tuples 与笛卡尔四族的区别；平面过覆盖与真实 filled shading 的区别；端点去重及纤维费用。若只有已有定理的合法接口、或现有计数没有到达任意小 `kappa`，则记录精确未付项并停止，不通过增加固定臂数或改归一化继续同义迭代。

## 2. 一手文献版本和实际阅读范围

输入为 Pavel Zorin-Kranich, **Kakeya–Brascamp–Lieb inequalities**, arXiv:1807.09604v4，2019-09-11；[官方 HTML](https://arxiv.org/html/1807.09604v4)、[官方 PDF](https://arxiv.org/pdf/1807.09604v4)。本地 PDF 为 `literature/primary/zorin_kranich_2019_kakeya_brascamp_lieb_1807_09604_v4.pdf`，SHA256 `e9046375f7019aab9f7b88123d870fbf3d71f9b264b338394d7d67e6a77fd831`；对应 extracted text 同 stem。

已实际读该版本正文 PDF1–16（含 §2–3 的证明结构）、PDF17–18 参考文献；本轮精确使用和逐式接口核查为 PDF1–6 的 Definition1.1、Theorems1.2/1.3/1.5、Definition1.4、式(1.5)/(1.6)/(1.9)/(1.14)–(1.16)。这是已发表高级输入的 statement/application 审查，不声称本轮独立重证其全部高级证明。文本行号按 `split('\n')`：Definition1.1 为26–39；Theorem1.3 为164–182；Definition1.4/Thm1.5 为220–272；Fremlin 与 product-space norm 比较为297–302。

Zhang arXiv:1510.09132 的精确关联在该文 PDF3/6：其 endpoint scale-invariant KBL 已被这里的 Theorem1.3/1.5 覆盖。本轮不另加未读版本或新的 mixed-norm 定理作为输入。

实际 WZ 来源为 arXiv:2609.22035v1：Def17.2–17.4，PDF65–66/text3361–3434；§19.1 的原直线关联，PDF78/式(148)–(151)，text4094–4114；R16 原 good-q/加权计数只按已审接口使用。

## 3. 四个 rank-2 映射所需的精确 KBL 形式

令 `H_i<=R^5` 是三维线性子空间，`p_i=5/8`，于是 `P=sum p_i=5/2`。ZK 的 `k_i` 是 **平面维数3**，不是正态映射的秩2。尺度齐次条件为

\[
\sum_{i=1}^4p_i(5-\dim H_i)=4\frac58\,2=5.
\tag{1}
\]

scale-invariant BL 有限还必须对每个线性子空间 `V` 有

\[
\dim V\le\frac58\sum_i\dim(B_iV),\qquad\ker B_i=H_i.
\tag{2}
\]

不能用堆叠映射的 rank=5 代替(2)。这里实际主定理允许更一般的 regularized `BL(H,p,(1,R))`，不要求先证明 scale-invariant 常数有限。常数随几何和 `R` 的增长是实费用。

Theorem1.3 的假设是四个 families 的 **全部混合 tuple** 均满足同一 `BL(1,R)<=A`；其结论的损失是 `C_5^P A`，没有额外任意小 `R^epsilon`。rank2/三维平面及本题有理权重完全在其范围内。但仅知道原选中四元组 good，不能直接调用1.3。

## 4. Theorem1.5 可直接处理任意选中四元组

取四个有限仿射三平面 families `mathcal P_i`，允许重复，并记 `N_i=|mathcal P_i|`。Theorem1.5 的四个 Fremlin 因子均是 `ell^{P/p_i}=ell^4`。由定义，若非负 `F(a_1,...,a_4)<=prod F_i(a_i)`，则

\[
\|F\|_{\ell^4(\prod X_i)}
\le\prod_i\|F_i\|_{\ell^4(X_i)};
\tag{3}
\]

取所有 domination 的 infimum，便得 Fremlin norm 不小于 product-space `ell^4` norm。将 `F=BL^{-1/P}` 代入，ZK 直接给出

\[
\sum_Q\left(\sum_{\substack{a_i:\Pi_{i,a_i}\cap Q\ne\varnothing\ (\forall i)}}
   BL(\vec H,\vec p,(1,R))^{-8/5}\right)^{5/8}
\le C\prod_iN_i^{5/8}.
\tag{4}
\]

若只选 `Gamma_Q` 个 incident tuples，且这些 tuples 上 `BL<=A`，则(4)仍给

\[
\sum_Q|\Gamma_Q|^{5/8}\le CA\prod_iN_i^{5/8}.
\tag{5}
\]

因此“原选中 tuples 非 Cartesian”本身不是精确 primary 输入的绝对障碍。真正需要的是其局部 tuple mass、四个 marginal 字母表及 multiplicity 的真实比较。

允许每个 family 的原权重 `w_i(a)>=0`：先复制有理权平面，再取极限，或直接在四个 `ell^4` 因子使用 weighted counting measure，(4)右边成为 `C prod_i W_i^{5/8}`，内层 tuple 使用 `prod_i w_i`。若原选中 tuple 测度 `lambda_Q` 在 good 集上满足

\[
\lambda_Q(\vec a)\le G\prod_iw_i(a_i),\quad M_Q=\sum_{\vec a}\lambda_Q(\vec a),
\]

则可用下界 `A^{-1}(M_Q/G)^{5/8}`。这里的 `G` 和四个 `W_i` 必须支付；原共享起点的相关 law 不会自动给 `G=K`。也可完全保留原有限标签，不去重，把所有重复直接计入 `N_i`。

物理 cube 宽 `r`、ambient ball 半径 `L` 时，先整体缩放 `r^{-1}`，`R` 取 `C L/r`。若写成积分量，(4)/(5)两边共同乘 `r^5`；若写成 cube 计数，二者均不乘。不同 frame 不能混用。

## 5. 原四臂的真实正态映射和物理 incidence

令原共同点 `p` 位于时间 `z`，四根不同原管 `T_i in T_p`，各自沿原 marks 选端点 `p_i=(x_i,y_i^phys,z_i)`。记 `f_i=f(z_i),xi_i=xi_{p_i}`，并定义

\[
B_i=(-f_i,I_2,-\xi_i),\qquad
\Pi_i=\{X:B_iX=B_ip_i\}.
\tag{6}
\]

因为 `B_iB_i^*=I_2+f_if_i^*+xi_i xi_i^*`，所有非零奇异值有绝对上下界（原 Mat entries 和 `xi` 均在[-1,1]）。故用 `B_i` 定义 BL 与使用正交 quotient metric 的 `ker B_i` 定义仅差固定常数；这个因子不是任意小 `delta` 幂。

原方向关系给 `B_i v_{T_i}=O(delta)`，其中 `v_T=(theta(T),1)`。而两点都在同原管内，故

\[
p-p_i=(z-z_i)v_{T_i}+O(\delta),\qquad
|B_ip-B_ip_i|\le C\delta.
\tag{7}
\]

因此四个完整仿射平面的 `C delta` 邻域均覆盖原共同点。这是合法的 quotient-indicator 过覆盖；**不需要**证明三维平面内有真实 filled grain shading，也不把它说成已经有 filled shading。平面无界亦无妨，KBL 在规定 ball 内积分，quotient 输入有有限二维面积。

为从近交变成 Thm1.5 的 `Pi_i intersect Q`，选固定大常数 `C_*` 和有限个 shifted `C_*delta` grids：每个原 `delta` cube 的 `Cdelta` 邻域包含在其中某个较粗 cube 内。先按有限 grids 分组，再计该 cube；原 `delta`-separated 点在一个较粗 cube 内仅固定个数。所有 affine plane 确有点落入同 cube，损失固定，且 `R=C rho/(C_*delta)` 或全局 `C/(C_*delta)` 要和 good-BL 定义一致。不能把有 `O(delta)` 距离的平面直接写成恰交原同一 dyadic cube。

## 6. 原直线关联没有允许丢弃的额外独立性

WZ 原(148)逐臂给出

\[
\xi_i=\xi_p+(f(z)-f_i)\phi_i+O(\delta).
\tag{8}
\]

将共同起点 grain 的坐标 gauge 为 `y=f(z)x+xi_p t`，令 `A_i=f_i-f(z)`，则 `B_i` 在该三维 grain 方向上的限制是

\[
(u,t)\longmapsto-A_i(u-t\phi_i)+O(\delta)|t|.
\tag{9}
\]

这说明不同原管的四臂不能套用“同一原管的共同核”论证。如果 `A_i` 可逆，`A_i` 与 `phi_i` 的参数已经描述一般图形三平面的开集；(9)不强迫所有四元组点态退化。反过来，slab cap 只控制 `phi_i` 的线性 slab 浓集，并不单独给全部子空间(2)或 good-BL mass。

例如若所有 `A_i` 的 image 位于同一固定一维 `L<=R^2`，则存在非零 `omega annihilates L`；gauge 后四个 `B_i` 都有同一行 normal `omega dy`。其 kernel 四维子空间上，各 `B_i` 的 rank 至多1，于是(2)右边至多5/2而左边为4，BL无限。此例仅说明角 slab 与(8)不足以免费推出横截；不是完整 AD/CW/tube-KT 来源反例。与旧 MNL001 已处理的 linewise/common-image 特殊支路应排重，不能重新记为新结果。

## 7. 三个既有硬筛选和一个原 rho-world 下界

**三臂。** 三个 rank2 maps 若等权5/6满足齐次性，任意前两个三维 kernels 有共同一维。该线上第三个 rank 至多1，右边至多5/6<1，故 scale-invariant BL 永远无限。

**同时间。** 四个 `f_i=f(z)` 时，共有二维水平 kernel `(u,f(z)u,0)`，故 BL无限。

**同一原管。** 只可从原 source 推 `B_i v_T=O(delta)`，不能直接称精确共同核。单位 quotient 输入的逆像交至少含沿 `v_T` 长 `c min(R,delta^{-1})`、横向固定宽的圆柱。因此 regularized `BL(1,R)>=c min(R,delta^{-1})`（或更大）。全局 `R~delta^{-1}` 给 `c delta^{-1}`，局部 `R~rho/delta` 只能无条件写 `c rho/delta`。把每个 `xi_i` 改为实际 `theta_T^y-f_i theta_T^x`，是 `O(delta)` 修改，修改后的 maps 才有精确共同核。

**同一原 rho-world。** 由实际 dyadic clock interval 和 `xi` coherence，可选 `B_q=(-f_*,I,-xi_q)` 使 `||B_i-B_q||<=C rho`。在三维 `H_q=ker B_q` 上，四 maps 范数均 `O(rho)`。固定 quotient cubes 的逆像交含三根长轴 `c min(R,rho^{-1})` 和两根固定短轴的圆柱，故

\[
BL(1,R)\ge c\min(R,\rho^{-1})^3.
\tag{10}
\]

在 `R~rho/delta`、`delta<<rho^2` 时下界为 `c rho^{-3}`。这不是四臂策略的绝对反例：若 `rho=delta^mu` 且 `mu` 选小，`3mu` 的成本也许能付。但不能在此 frame 免费宣称近单位 BL，或混用全局 `R` 来获得不合法的长圆柱。

## 8. 原端点计数的准确 fibre 费用

以下审计 root/B 正在构造的 global 原 star 计数接口，而不假定每点原度都已逐点 homogenize。若已合法保留原质量，并在保留点上有

\[
N_E\asymp_K\delta^{-(5-\kappa)},\qquad
\#\{(T,p'):T\in T_p,\ p'\text{ 为该原管 mark}\}
\ge K^{-1}\delta^{-\kappa-1},
\tag{11}
\]

并删除同管/过近 time 等只损已付比例，则四个原臂的有序见证数至少 `K^{-C}delta^{-4(kappa+1)}`。保留 `|z_i-z|>=r=delta^alpha`。给定原起点 `p` 与端点 `p_i`，原方向在半径 `C delta/r` 的 angular ball 内。`Phi_p` 的 fine AD upper、每 fine phi bin 只选一个原 witness 以及过 `p` 的 intercept packing 给

\[
\#\{T\in T_p:p_i\text{ 为对应 mark}\}\le K^C r^{-\kappa}.
\tag{12}
\]

四臂 fibres 至多 `K^C r^{-4kappa}`，故不同 endpoint-label tuples 数

\[
|\Gamma_p|\ge K^{-C}\delta^{-4\kappa-4+4\alpha\kappa}.
\tag{13}
\]

不能去重后继续沿用原见证数；也不能将任意 coarse `Phi_q` 的未使用点当作原角 prior。每个 endpoint plane 可用原点本身作 label，故每个 family 的总字母表至多 `N_E`，同平面多次出现允许计 multiplicity。若换成更少的 plane labels，必须另外给原 multiplicity 和 fibre 上界，不能假设 `xi_p` 与水平 `x` 无关。

## 9. 即使 good-BL mass 已付，当前编码仍只到 5/4

暂且假定(13)的 inverse-subpower 比例在每个保留源 cube 上满足 `BL<=A`。原点 `delta` packing 和有限格网并组付固定常数后，(5)给

\[
K^{-C}\delta^{-(5-\kappa)}
 \delta^{-(5/8)(4\kappa+4)+O(\alpha\kappa)}
\le CA\delta^{-(5/2)(5-\kappa)}.
\]

即

\[
\delta^{5-4\kappa+O(\eta)+O(\alpha\kappa)}\le C A.
\tag{14}
\]

若 `A<=delta^{-c}` 且各损失很小，最多得 `kappa<=5/4+O(c+eta+alpha kappa)`，没有接近任意预先给定 `zeta`。本轮尚未证明其中 good-BL mass；(14)也不是新的五维 ordinary Kakeya 下界。ordinary 集合已有四维投影基线，但该 ordinary statement 不能未经接口证明就直接用于任意无方向 AD/CW 抽象配置。

在相同 endpoint 字母表编码下增加固定 `m` 臂也不修复指数：等权 `p_i=5/(2m)`，`P=5/2`，局部 witness 数为 `delta^{-m(kappa+1)}`，其 `P/m` 次幂仍是 `delta^{-(5/2)(kappa+1)}`。若这些权重的 BL/KBL 数据本身合法，最终仍是(14)同一阈值。因此“只再加固定臂数”不构成本轮之后的新 main。

## 10. 可完整付出的条件性五矩阵/四角有限桥

本节核查 root/B 本轮的有限提取，不能反过来当作原 source 已有的 time-rank 结论。设 `F_0,...,F_4` 为有界2乘2矩阵，并另有强假设

\[
|\det(F_i-F_j)|\ge\sigma>0\quad(0\le i<j\le4).
\tag{15}
\]

在固定原起点角先验 `pi` 下取四个角变量，理想 endpoint 参数为 `xi_i=xi_0+(F_0-F_i)phi_i`。定义

\[
a_{ij}=(F_i-F_j)^{-1}[(F_i-F_0)\phi_i-(F_j-F_0)\phi_j],\qquad
D_i=\det((a_{ij},1)_{j\ne i}).
\tag{16}
\]

条件于 `phi_i`，每个 `a_ij` 是 `phi_j` 的可逆 affine image，其线性部分最小奇异值至少 `c sigma`：因为 `||F_i-F_j||<=C`、`s_min(F_j-F_0)>=c sigma`。三个 `a_ij` 构成二维三角形。如果其面积 `|D_i|<=tau`，则前两点距至多 `sqrt(tau)`，或第三点到其直线距离至多 `sqrt(tau)`。第一项可由任意包含该小球的 slab 控，第二项在条件于前两点后用原 slab 控。故在 **product reference law** 下

\[
\Pr(\min_i|D_i|\le\tau)
\le CK_\pi(\sqrt\tau/\sigma+\delta)^\gamma.
\tag{17}
\]

查询宽度小于原 fine base 时须截到 `delta`。这只是用 product reference 积分证明 bad-set upper；若真实 tuple density `g<=G`，真实坏质量至多上式乘 `G`，须小于 retained 总质量，不能宣称真实四角独立。

原 `xi_i` 只有 `O(delta)` 方向误差。由 `a_ij=O(sigma^{-1})`、其误差 `O(delta sigma^{-1})` 及 determinant 的二次形式，`D_i` 改变至多 `C delta sigma^{-2}`。因此必须先安排 `tau>>delta sigma^{-2}`；通过后 actual `|D_i|>=tau/2`。

对 actual 参数，采用原坐标 `(x,y,t)->(x,B_i(x,y,t),t)`，Jacobian **恰为1**，不需要额外概率归一化。固定 `B_i X=b` 后，其余映射是

\[
B_jX=(F_i-F_j)(x-a_{ij}t)+b.
\]

三维 fibre 内三根 kernel directions `(a_ij,1)` 的经典三线 Loomis–Whitney 给权向量 `p^(i)_i=1,p^(i)_j=1/2` 的 BL 常数

\[
C_i=|D_i|^{-1/2}\prod_{j\ne i}|\det(F_i-F_j)|^{-1/2}.
\tag{18}
\]

四个这样的积分式经 Hölder 等权相乘，所有输入指数变为5/8；得到

\[
BL(\vec B,(5/8)^4)\le(\prod_i C_i)^{1/4}
\le C\tau^{-1/2}\sigma^{-3/2}.
\tag{19}
\]

这里使用已知三线 LW/BL 的确切常数，且原矩阵-normal与正交 quotient 只差§5已付固定因子。它是比“堆叠 rank=5”强得多的完整有限判据。

在 pairwise `F_i-F_j` 可逆的范围，`D_i!=0`（所有 i）还是必要条件：若某个 `D_i=0`，三根实际 `H_i intersect H_j` 的一维 kernel lines 在 `H_i` 内张成至多二维。张成二维时取该二维 `V`，`B_i V=0`，其余三 images rank 至多1，(2)右边至多15/8<2；若三线同一条，则是四个共同 kernel line。故 scale-invariant BL 无限。这个判据未声称覆盖不可逆 pair-difference 情形。

未支付步骤恰是：(15)或其能替代的几何条件，能否从实际 source 的原时间/角/管 law 保留下足够质量。`f` dyadic Lip、非 affine 和原 `Phi_p` 的 slab cap 本身都不直接提供(15)。即便(15)已付，也还受到§9原端点计数阈值的限制。

## 11. 仍未支付的真步骤与本轮结论

1. 原 full source 是否强迫足够多 **不同原管、不同原时间** tuples 满足可用的 `BL(1,R)` 上界，仍需真正的子空间/小奇异值质量估计。`f` 非 affine、角 slab、四根方向独立分别都不能替代这一步。
2. 平面 overcover 的物理 incidence 已付；不必制造不存在的 filled3plank。四个 prior/字母表与原相关 g 的费用仍须保留，任意 tuple 可用 Theorem1.5，非 Cartesian 本身不构成失败理由。
3. 即使上一步完全成功，目前单一 endpoint 字母表的真实计数只给(14)。要有 `kappa<=zeta`，需要具体不同的可检验信息改变该计数预算；不能把缺口重新命名为多臂横截性后登记为新数学成果。

结论仅为原来源接口/精确 primary 输入/当前计数的审计。full `d5,k=ell=3`、其它 mixed branches、普通五维及一般维 Kakeya 仍未解决；具名外部结果按其原假设使用，本稿不是整篇 source 或全部高级证明的外部认证。
