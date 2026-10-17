# R0046：固定有理四投影、原有限种子及几何编码审计

2026-10-17，audit_four_dimensional。已读恢复入口、registry/latest、R45精确同步记录、R46 spec 和 R45 next。只编辑分配文件，不操作 Git、不另开代理。本轮目标是全称 R5/3；以下没有证明该候选，也没有构造其严格反例，更不是 Kakeya 反例或高维新界。未经外部同行评审。

## 1. 全称候选、量词和停止条件

对任意 torsion-free abelian group G 和有限 `Z subset G^2`，令 `n=|Z|`、`M=max_x |{y:(x,y) in Z}|`，四个实际像集为 `S_1=x+y,S_2=-x+y,S_3=y,S_4=x+3y`，记其基数 `s_i`。唯一候选为

\[
n\le C M^{1/3}(s_1s_2s_3)^{10/21}s_4^{5/21}.
\tag{R5/3}
\]

C 必须独立 G、rank、tensor 次数、基数和任意编码。若有限精确反例出现，立即停止该式；若没有合法的 DIR003/FSD001 方向/mark/cover/常数编码，也一轮停止，不能调 q/权重继续同名任务。有限检索没有找到反例不等于证明全称式。

## 2. 一手版本、必要条件和确实已有的估计

Ruixiang Zhang, *Mixed-norm Brascamp–Lieb inequalities*, [arXiv:2608.17952v2](https://arxiv.org/abs/2608.17952v2)，version 2026-08-19，本地 PDF 首页日期08-20。本轮实际读本地 PDF/text §§2–4（PDF5–10），并对照[官方 HTML](https://arxiv.org/html/2608.17952v2)。精读 Definition3.1、Lemma3.2、Theorem3.3、Lemma4.2/Remark4.3；§5 的 compact Hausdorff 接口仍依原 statement/具名附录，不在本轮独证全文。

§2 的基本条件是 `sum p_i=1`、`1/q+1/r=1`；q<2 的有趣情形必须有至少三张不同 projections。本题四张 fixed rational forms 不受“两张不可能”这一立即障碍。q=5/3,r=5/2、p=(2/7,2/7,2/7,1/7) 给 `1-q/r=1/3`，以及 `p_i q=(10/21,10/21,10/21,5/21)`，量纲正确。必要条件不是充分证明。

§3 的 transference 真要求 **每个无挠 G 上统一常数** 的 restricted 式（先在非空 x-fibres 约为同一 M 的情形）。先 dyadic pigeonhole 产生 logarithm，后对 `G^N` 和函数的 tensor power 使用同一常数，才可去 log、得到同一 q 的 strong mixed norm。不能把去 log 当成 q7/4 到 q5/3 的改进；也不能用固定 rank 的几何隐常数替代 all-G uniformity。

Lemma4.2 已有的严格有限式是

\[
n^4\le M(s_1s_2s_3)^2s_4.
\tag{1}
\]

它只需 G 无2阶元，故本候选的无挠假设足够。该式并非本文首次提出；primary Remark4.3 明确归于既有 Katz–Tao/Tao entropy/PZ sharpening。不能把本轮重证记作新结果。

完整有限计数可直接写清：先取所有满足 `L_1 z_1=L_1 z_2` 的 pair，数量至少 `n^2/s_1`；按 `(L_2 z_1,L_3 z_2)` 分组后再作 Cauchy–Schwarz，得到至少 `n^4/(s_1^2s_2s_3)` 个四环，满足

`L_1 z_1=L_1 z_2, L_1 z_3=L_1 z_4, L_2 z_1=L_2 z_3, L_3 z_2=L_3 z_4`。

每个环的 signature 为 `(L_2 z_2,L_3 z_3,L_4 z_4)`；原恒等式

`2x_1=-L_2z_2-2L_3z_3+L_4z_4`

唯一确定 x_1（乘2单射），从而 z_1 至多 M 种，再由 signature 和环等式唯一恢复其余三点。因此四环至多 `M s_2s_3s_4`，即(1)。没有把 fibres 先改成 uniform 或忘掉 M。

一个精确排重域：将(1)取五次方并乘 n，若 `n<=M^2`，则

\[
n^{21}\le nM^5(s_1s_2s_3)^{10}s_4^5
\le M^7(s_1s_2s_3)^{10}s_4^5.
\tag{2}
\]

因此 R5/3 在 `n<=M^2` 已被旧 q7/4 覆盖；新的困难至少包括 `n>M^2`，特别是 M=1 graph。这个域缩减不证明其余情形，也不改变本轮候选。

本轮 bounded 一手检索只查固定式/相关 sum-difference/mixed-norm 的准确入口；未获得能直接证明全 R5/3 的新 primary theorem。有限空检索不认证“没有已有结果”或新颖性。

## 3. 全称统一 C 强制常数1；有限证书和全称失败分开

固定任意一个有限 Z，取 `G^N` 和 `Z^N`。四个像集及最大 x-fibre 恰为各自 N 次 Cartesian power，所以 n、M、s_i 全部取 N 次幂。若原全称式有同一个 C，则对每个 N

\[
\left[\frac{n}{M^{1/3}(s_1s_2s_3)^{10/21}s_4^{5/21}}\right]^N\le C.
\]

取 N 次根、令 N 趋无穷，括号必须至多1。因此全称式等价于所有有限数据的 sharp 常数1版本；精确有限证书

\[
n^{21}>M^7(s_1s_2s_3)^{10}s_4^5
\tag{3}
\]

一旦被实际找到，借上述独立 tensor 证明即可否全称 C。有限计算只核其整数证书；推广责任是本节论证，不能混为有限样本已证明一般连续定理。

当 Z restriction 后，四个 s_i 和 M 的 upper 都不增；原 n 可能大幅减少。near-uniform-fibre 选择若丢质量，须保该损失；不能由一个小 subset 的式子免费升级回原 Z。equal-cardinality bound 也不自动给不对称 s_i 式。

## 4. 真实几何编码：四个 rational times 只有四个 marks

取包含有限数据的无挠子群，选择 additive homomorphism `F:G_0->R^3`，在所需有限差集上注入，使四个 integer forms 的等式与不同值均被保留。归一化到固定 bounded chart 后，自然直线是

\[
L_{x,y}(t)=(t,F(y)+tF(x)).
\tag{4}
\]

四个原像值只控制 t=1,-1,0,1/3 的位置；第四个位置乘3是 `F(x+3y)`。可对 t 作一次共同 affine 变换，使四时位于[1/4,3/4]，保持真实直线和共同 clock，仍然只有四个时标。

DIR003 的真实假设是每条保留 line 至少 `delta^{-1+eta_src}` 个非空时间 bins；FSD001 的平均版先 heavy 亦要求原密度 `lambda>=delta^{eta_src}`。固定 `0<eta_src<1` 时，四个时标或每时固定邻接格仅给 O(1) bins，即 `lambda=O(delta)`，小 delta 时不合法。重复 indices 或增大权重不增加单条 line 的原 marked duration。

若把四个时间片加厚为宽 w 的区间，要满足 long-duration 门槛便需 `w>=c delta^{eta_src}`。但实际 line 在这些新区间读的是

`F(y)+t_jF(x)+(t-t_j)F(x)`，

后一个项不在四个 S_j 控制内。在统一 bounded slope box 中，诚实的朴素 cover 为

\[
\#E\le C\sum_j s_j(1+w/\delta)^4:
\tag{5}
\]

每个旧像点的三维 spatial drift box 有 `O((1+w/delta)^3)` 格，乘 `O(1+w/delta)` 时间格。若确有 slope-bin ceiling `alpha<=CM`，DIR 插入该 cover 也只给带额外 `(w/delta)^3 delta^{-epsilon}` 的 sum-of-sizes 界，而不是 R5/3。式(5)只是这份 cover 的合法 upper，不是最优 lower；不能据其费用宣称任何几何编码都不可能。

把 slope 进一步压缩以使 line 在旧节点附近停留较久，会同步降低 direction separation/方向数，且改变 delta 与输入基数的关系。这些代价不能以“可以把 epsilon 任意选小”消除，因为 eta_src 是在 epsilon 之后给定，而非反向自由选择；第7节给真实必要性校准。

## 5. 低 rank：归一化丰富方向与绝对 sparse cap 不同

若 `G_0=Z`，任何 additive `F:G_0->R^3` 都有 `F(n)=nv`；斜率落在一条直线。固定 bounded chart 内最多 `O(delta^{-1})` 个 separated slopes，不能产生 near-full `delta^{-3+o(1)}` 数量；均匀概率 law 的 fine-bin atom 约 delta，也不能免费写成有界三维 density 的 `O(delta^3)`。

但这 **不禁止** unsaturated DIR003/FSD001：任何已 delta-separated 的三维 slopes 都满足绝对 packing upper `#(B(theta))<=C(theta/delta)^3`，即使它们实际只在一维。DIR 明确允许任意 m，只保其真实 m 和 `alpha`。低 rank 本身不能当成反例或绝对失败理由；它阻止的是偷来的 full-direction 数量/归一化3-Frostman ceiling。

多重 x-fibre 本来有至多 M 个 line indices 同 slope；若 F 在 x 集上注入且 min separation 已到 delta，可有 `alpha<=CM`。若压缩/舍入使更多 x 撞 bin，须支付真实更大的 alpha。Freiman/additive 编码保 integer forms 不自动控制这个几何尺度，更没有给 all-G/tensor 的 uniform delta 代价。

## 6. 用两维自由方向补 fullnet 的最直接产品恰好抵消

对此可作精确有限检验而不泛称“低rank不能用”。先有平面 line family `(t,u_i(t))`，共用 t∈[c,1]，原共同 marks 任意；取固定二维 delta-grid `W subset[-1,1]^2`，构造四维真线

\[
\widetilde L_{i,w}(t)=(t,u_i(t),tw_1,tw_2).
\tag{6}
\]

时间不变、每条 mark 数不变。每个原 base time/spatial delta-cell 对应的辅助格数与 `|W|` 可比：对固定 t>=c，映射 `w->tw` 的 separated packing 数为 `Theta(|W|)`；同一时间 bin 内 t 的变化只造成固定邻格增厚。故固定尺度扩大后

\[
\sum_{i,w}\#J_i=|W|\sum_i\#J_i,\qquad
\#E_4\asymp_c |W|\#E_2.
\tag{7}
\]

若原一维 slope 已 delta-separated，新增方向 grid 的 bin mass ceiling 不高于原重数的固定倍，数量确可增加 `|W|~delta^{-2}`。但是 DIR 代入(7)后，左右同一 `|W|` 精确相消；四个旧节点 cover 也各乘该因子，没有 R5/3 新 saving。自由辅助方向不修复原四 marks 太短的问题。本结论只排该直接产品施工，不排需要新算术/几何信息的耦合辅助 construction。

## 7. 原 finite 种子的 epsilon/eta 顺序有真实 bush 下界

这是对 **DIR003** 可用参数的必要条件校准，不是其反例，也不声称有最优可选 eta 下界。固定 target `epsilon>0`，假设某 `eta_src in(0,1)`、常数 C 与 delta_0 确使 DIR 对所有所述 bounded families 成立。

取 `v in delta Z^3 intersect[0,c]^3`，共有 `m asymp delta^{-3}` 根 `L_v(t)=(t,tv)`；权重1，每个半开 delta-slope cube 有固定个数，故 `alpha<=C_0`。所有线均在同固定 bounded chart。令 `lambda=2delta^{eta_src}`、`n_t=floor(lambda/delta)`，delta 小到 `Cdelta<=lambda<1`，取所有 `t=kdelta,1<=k<=n_t` 为每根线的 marks。于是

\[
\#J_v\ge\delta^{-1+\eta_{src}},\qquad
\sum_v\#J_v\gtrsim\lambda\delta^{-4}.
\tag{8}
\]

固定 time-bin k，所有 visits 的 spatial 坐标在边长 `C kdelta` 盒中，故其 delta-cells 至多 `C(k+1)^3`；固定邻接扩大不改数量幂。因此

\[
\#E\le C\sum_{k=1}^{n_t}(k+1)^3
\le C(\lambda/\delta)^4.
\tag{9}
\]

将(8)–(9)代入 DIR，只能有

\[
1\le C'_{\epsilon}\delta^{3\eta_{src}-\epsilon}.
\]

若 `3eta_src>epsilon`，令 delta 趋零就矛盾。任何有效的该 DIR 参数必须满足

\[
\eta_{src}\le\epsilon/3.
\tag{10}
\]

这与现有 DIR 选更小 eta 完全相容；不要求线段可测选择、轨道 AD lower 或逐管 two-ends。它仅说明不能在 encoding 中免费先令 `epsilon<<eta_src`，也没有给 eta_src 与 epsilon 的正向线性可用模数，更不能把 delta^{-epsilon} tensor 消去时忽略 delta 随 G/rank/tensor 的实际变化。

## 8. 本轮出口和宏观边界

已付 primary 式(1)、旧覆盖域(2)、sharp-C1 tensor必要性、四 rational times 的实际 straightline编码及其 duration缺口、直接补角产品抵消和合法 bush 参数校准。没有证明全 R5/3，也没有其有限严格反例；是否出现反例由 root/B 精确实验及其独立整数证书判断，不能用本稿的 cover upper 冒充反例。

目前没有保四个原像集预算、同时满足 long marks/方向 bin cap/scale/统一 tensor常数的实际新编码。按一主轮停止设计，不追加 q/weights 或将缺口改名为新SD估计。下一宏观应选真正不同的可检验机制，不能把本轮必要条件/源重证登记重大结果。一般五维与一般维 Kakeya 的完整 Goal 保持 active。
