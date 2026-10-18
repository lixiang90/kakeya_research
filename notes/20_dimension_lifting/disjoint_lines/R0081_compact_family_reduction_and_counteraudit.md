# R0081：紧致全方向不交直线族归约的独立重构与反攻

2026-10-18。B 独立稿；只重构 Keleti 2026-04-20 BME 讲义所报告的归约，不主张新定理、维数改进或重大结果。高级最小维输入具名保留；下列拓扑拼接给出完整证明，仍须独立逐步审查，未经外部同行评审。

## 1. 精确输入、来源与停止目标

固定整数 \(n\ge2\)，令 \(C=[0,1]^n\)、\(D=\mathbb {RP}^{n-1}\)。本文使用 Keleti–Máthé 2203.15731v3 Theorem 1.1、Lemmas 2.1–2.2 的具名结论：存在共同最小 Hausdorff 维数 \(d_n\)，覆盖原文所列 Besicovitch 变体，且在下面完整紧致 code 空间中，
\[
\mathcal R_{\rm dim}=\{K:\dim_H S(K)=d_n\}
\]
为 residual。其 whole proof 不在本轮重新独证。因而若原来有任意 Besicovitch 集维数小于 \(n-1\)，可由该具名变体定理得到 \(d_n<n-1\)；不能直接从任意不可测集抽取未经证明的 compact selector。

本轮自证的条件归约为：若 \(d_n<n-1\)，则存在可数个紧致几何直线族 \(\mathcal C_i\)，每个覆盖全部无向方向，且所有 \(\bigcup_i\mathcal C_i\) 中的 distinct lines 两两不交。本文不证明这些族不可能存在，也不证明 \(d_n\ge n-1\) 或 Kakeya 全维。

实际已完整读取新讲义的 21 页提取文本，尤其 PDF15–18 的主张及 PDF19–20 的非紧致构造范围；另实际核 KM 源 Theorem 1.1、Lemmas 2.1–2.2 的 statement 与相应 proof 读域。本稿不宣称 B 新做了 PDF 逐页视觉审查或官方字节检查。

## 2. 完备 code 空间与 distinct line 的规范参数

定义
\[
\mathcal K(C,D)=\{K\subset C\times D:K\ne\varnothing\text{ compact},\ \operatorname {proj}_D K=D\},
\qquad S(K)=\bigcup_{(p,e)\in K}\ell(p,e).
\]
在 \(D\) 上取 \(d_D(e,f)=\|P_e-P_f\|\)，其中 \(P_e\) 是投影到无向一维子空间 \(e\) 的正交投影。非空紧子集 hyperspace 对 Hausdorff 距离完备；\(\operatorname {proj}_D K=D\) 在 Hausdorff 极限下保持，故 \(\mathcal K(C,D)\) 是非空完备度量空间，可用 Baire 定理。

raw code \((p,e)\) 不唯一表示直线。用
\[
c(p,e)=(P_e,(I-P_e)p),\qquad
d_{\mathcal L}(c(p,e),c(q,f))=\|P_e-P_f\|+|(I-P_e)p-(I-P_f)q|
\tag{1}
\]
给出规范直线参数。距离为零恰当且仅当是同一几何直线；平行异线仍有正距离。\(c(C\times D)\) 紧致，且 \(c\) 在该有界 chart 上 Lipschitz。以下远对按 (1) 测试，绝不把同一直线的不同 raw positions 当成相交的 distinct lines。

本文无每方向唯一性、连续或可测 selector、有限维 code manifold 假设。最后几何族取 \(c(K)\)，连续像仍紧致并覆盖 \(D\)。

## 3. Whole-line union 的闭性及 σ 紧致分解

空间点 \(x\) 在 \(\ell(p,e)\) 上，等价于
\[
(I-P_e)(x-p)=0.
\tag{2}
\]
这是闭 incidence 关系。若 \(x_j\in S(K)\) 且 \(x_j\to x\)，从紧致 \(K\) 中取其 codes 的收敛子列，(2) 给出 \(x\in S(K)\)。因此即使每条线无限长，\(S(K)\) 仍闭。

于是
\[
S(K)=\bigcup_{R=1}^{\infty}\bigl(S(K)\cap\overline B(0,R)\bigr)
\tag{3}
\]
为 σ 紧致分解，每项紧致。若 \(\dim_H S(K)<n-1\)，则 (3) 每一项向任意 \(n-1\)-子空间的正交投影均为紧致、Hausdorff 维数小于 \(n-1\) 的集，故无 interior。这里投影 Lipschitz；只对固定 compact truncations 用 nowhere-density，而不把无限 union 的投影直接称 nowhere-dense。

## 4. 固定紧致障碍的避交集是开集

设固定紧致 \(B\subset\mathbb R^n\) 满足所有超平面正交投影无 interior。令
\[
\mathcal O_B=\{K:S(K)\cap B=\varnothing\},\qquad
f_B(p,e)=\min_{b\in B}|(I-P_e)(b-p)|.
\tag{4}
\]
空 \(B\) 平凡处理。非空时 \(f_B\) 在 compact \(C\times D\) 连续。\(K\in\mathcal O_B\) 当且仅当 \(\min_Kf_B>0\)：零最小值由 \(B,K\) 紧致实现，才等价真实交点。正最小值由一致连续性在 Hausdorff 小扰动下保持，故 \(\mathcal O_B\) 开。

这不使用无限集合 \(S(K)\) 的 Hausdorff 距离，也不把任意两个不交闭集距离正误作一般事实；正间隔来自 \(B\) 与有界 codes 的共同紧致性。

## 5. 固定障碍的密度：真 closed caps 的有限子盖

给 \(K_0\in\mathcal K(C,D)\) 及 Hausdorff 精度 \(\varepsilon>0\)。对每个原 code \(k=(p,e)\in K_0\)，先在 \(\operatorname {int}C\cap B(p,\varepsilon/10)\) 选 \(q_k\)，使
\[
(I-P_e)q_k\notin (I-P_e)B.
\tag{5}
\]
这可行：原投影是 compact nowhere-dense；正交投影把非空空间开集映成超平面开集，故其逆像的补集在任意小位置开球中非空。边界 \(p\) 可先任意小地向 cube 内移动，不需在原边界保持位置。

由 \(f_B(q_k,e)>0\) 和连续性，可选 \(0<r_k<\varepsilon/10\)，使所有 \(e'\in\overline {\operatorname {cap}}(e,r_k)\) 的 \(\ell(q_k,e')\) 都避开 \(B\)。乘积开邻域
\[
U_k=(C\cap B(p,\varepsilon/10))\times\operatorname {cap}(e,r_k/2)
\]
覆盖 \(K_0\)。取有限子盖 \(U_{k_i}\)，并置
\[
K'=\bigcup_i\{q_{k_i}\}\times\overline {\operatorname {cap}}(e_i,r_{k_i}).
\tag{6}
\]
每个新 code 接近原中心 \((p_i,e_i)\)，故 new-to-old 距离小于 \(\varepsilon\)。反向，对每个 \((p,e)\in K_0\)，取包含它的 \(U_{k_i}\)，则 \((q_{k_i},e)\in K'\)，位置误差小于 \(\varepsilon/5\)。因此 \(d_H(K',K_0)<\varepsilon\)。同一事实还给全部方向：每个 \(e\in D\) 在 \(K_0\) 有 witness，故属于至少一个 (6) 的 closed cap。有限 union 紧致，且全避 \(B\)。故 \(\mathcal O_B\) dense。

选择顺序重要：先对每个原 code 得真实 good cap，再从乘积开覆盖抽有限子盖；不能先取 finite direction net，再免费假未知的小 good caps 仍覆盖所有 \(D\)。

## 6. σ 紧致障碍、局部位置盒与低维 residual

若 \(B=\bigcup_mB_m\)，每个 \(B_m\) compact 且投影无 interior，则
\[
\{K:S(K)\cap B=\varnothing\}=\bigcap_m\mathcal O_{B_m}
\tag{7}
\]
为 dense \(G_\delta\)，一般不是开集。尤其可逐避任何固定 \(\dim_H B<n-1\) 的 σ 紧致障碍。

下一步需在任意小位置 cube \(Q\subset\operatorname {int}C\) 中选完整全方向低维族。取正边长 cube \(Q=a+rC\)，固定 homothety \(p\mapsto a+rp\) 在两个 code 空间间给 homeomorphism，且 whole unions 满足 \(S(K_Q)=a+rS(K)\)，维数不变。因此具名 \(\mathcal R_{\rm dim}\) 的像是 \(\mathcal K(Q,D)\) 中 residual。§§4–5 的避交论证同样适用于 \(Q\)。

所以在任意这样 \(Q\) 中，可同时选择维数 \(d_n\) 的全方向族，并避开先前有限多个低维 whole unions 的所有 compact truncations。这里只用 fixed full-direction localization；后来限制到 closed direction caps 只会降低维数，不需要任意方向子集的最小维等号。

## 7. 有界交点的 far-pair 坏集是闭集

固定正整数 \(j,R\)，令 \(\mathcal F_{j,R}\) 为所有存在 codes \(k,k'\in K\) 满足
\[
d_{\mathcal L}(c(k),c(k'))\ge1/j,
\qquad \ell(k)\cap\ell(k')\cap\overline B(0,R)\ne\varnothing
\tag{8}
\]
的 \(K\)。若 \(K_m\to K\) 且每个 \(K_m\) 有 (8) 的 witnesses，则 codes 与交点分别在 compact \(C\times D\) 与 \(\overline B_R\) 中取子列；Hausdorff 收敛使极限 codes 属 \(K\)，(1)(2) 的连续性保 (8)。故 \(\mathcal F_{j,R}\) 闭，\(\mathcal V_{j,R}=\mathcal K\setminus\mathcal F_{j,R}\) 开。

不能直接说“存在任意位置交点”的坏集闭：两条交线可以趋于不同平行线而交点逃到无穷。分列 \(R\) 正是为保闭性；分列 \(j\) 则排除同一 geometric line 的 raw 重复。

## 8. Far-pair 避交密度：解内部自依赖

固定 \(K_0,\varepsilon,j\)。取 \(\eta>0\) 足小，使 \(\eta\ll\varepsilon\)，且 \(c\) 的 Lipschitz 常数乘 \(3\eta\) 小于 \(1/j\)。取 \(K_0\) 的有限 \(\eta/4\)-code net \((p_i,e_i)\)，令 \(E_i=\overline {\operatorname {cap}}(e_i,\eta/2)\)。这些 closed caps 覆盖 \(D\)。为各 \(i\) 选正边长 closed cube \(Q_i\subset\operatorname {int}C\)，使 \(\operatorname {diam}Q_i<\eta/4\) 且每点距 \(p_i\) 小于 \(\eta/2\)；包括原 \(p_i\) 在边界的情形。

按 \(i\) 归纳选 **全方向** \(L_i\in\mathcal K(Q_i,D)\)：维数 \(\dim_H S(L_i)=d_n<n-1\)，并令 \(S(L_i)\) 避开先前每个 **whole** \(S(L_h)\)。§6 中 residual 的可数交保证每一步存在。选定后仅保 piece
\[
K_i=L_i\cap(Q_i\times E_i),\qquad K'=\bigcup_iK_i.
\tag{9}
\]

不同 pieces 的 whole lines 无交点；每个单 piece 的 canonical line 直径小于 \(1/j\)，所以内部即使有交线也不触发 (8)。因此 \(K'\in\mathcal V_{j,R}\) 对所有 \(R\) 均成立。\(K'\) 紧致、全部方向，且 new-to-old 由中心 code、old-to-new 由 net 与同一 direction witness 分别给 \(d_H(K',K_0)<\varepsilon\)。故每个 \(\mathcal V_{j,R}\) dense。

这里没有将 fixed-obstacle lemma 直接用于自依赖的 \(B=S(K)\)。障碍在归纳每一步都是已选定的前族；内部剩余问题由小 canonical diameter 延后到 countable intersection 解决。也没有预假每个 \(L_i\) 已 internally disjoint。

## 9. 同一 residual 与单族内部全直线不交

取 \(\mathcal R_{\rm dim}\) 中的 dense \(G_\delta\) 子集 \(\mathcal R^0_{\rm dim}\)；这可由 residual 的定义选择，不需它字面已是 \(G_\delta\)。置
\[
\mathcal R=\mathcal R^0_{\rm dim}\cap\bigcap_{j=1}^{\infty}\bigcap_{R=1}^{\infty}\mathcal V_{j,R}.
\tag{10}
\]
完备空间的 Baire 定理给 (10) residual 非空。每个 \(K\in\mathcal R\) 有维数 \(d_n\)，且其 distinct geometric lines 两两不交：若两线不同，(1) 距离正，取足大 \(j\)；若有交点，取足大 \(R\)，则违反 (8)。

这是所有 \(j,R\) 共同的同一个选择，不是各自取一族后误并。平行多线当然允许；raw 重复 codes 可在 \(c(K)\) 取像时合并，不影响方向覆盖或紧致性。

## 10. 可数个全方向紧致族同时互不交

先取 \(K_1\in\mathcal R\)。已取 \(K_1,\ldots,K_m\) 后，用 (3) 将所有 \(S(K_i)\) 分成可数 compact truncations。每个 truncation 维数小于 \(n-1\)，故其避交集 open dense。于是
\[
\mathcal R\cap\bigcap_{i\le m}\bigcap_{R\ge1}
\mathcal O_{S(K_i)\cap\overline B_R}
\tag{11}
\]
residual 非空，可取 \(K_{m+1}\)。它内部由 (10) 保不交，与此前 whole unions 由 (11) 保完全不交。

令 \(\mathcal C_i=c(K_i)\)。每个 \(\mathcal C_i\) 是 canonical line space 的 compact full-direction family；整个 \(\bigcup_i\mathcal C_i\) 的 distinct lines 两两不交。跨族连同一条线也不能重复，否则 whole unions 相交。得到 §1 的完整条件结论，不要求各方向唯一或图形化。

## 11. 严格阈值、拓扑及旧等价反攻

严格 \(d_n<n-1\) 在本证明中真实使用。端点反攻：取超平面 \(x_n=1/2\) 内小 closed \(n-1\)-disk \(B\)，其中心 \(p\in\operatorname {int}C\)。令 \(K_0=\{p\}\times D\)。任何足近 \(K_0\) 的 full-direction \(K'\) 必有竖直方向 code，其直线仍穿该 disk；所以 \(\mathcal O_B\) 不在 \(K_0\) 附近 dense。不能把 \(\dim_H B\le n-1\) 免费代入。

非紧致开性反攻：在二维坐标内取 \(B=\{(k,1/k):k\ge1\}\)，这是闭非紧致零维集。直线 \(y=0\) 避 \(B\)，而 \(y=1/k\) 交 \(B\) 且趋于前者；故 line-level avoidance 没有一般开性。本文 (7) 仅主张 residual。另例 \(y=0\) 与 \(y=1+x/m\) 的交点为 \((-m,0)\)，极限为两条平行线，说明 §7 的交点截断不可漏。以上不冒作 complete full-direction space 的更强反定理。

紧致 surjection 到 \(D\) 不授连续 selector；(6)(9) 全保 fibres，故没有偷用这一点。有限 direction net 只有经 closed caps 真覆盖才保全方向。arbitrary 非闭 restriction 不保 compact，本文只用 closed products。原 PDF19–20 的 closed、不必 compact 的构造明确为 \(\mathbb R^3\) 及类似 odd \(n>3\)，不可泛化全部维度或拿来解决 compact 问题。

该定性归约没有有限 \(\delta\) marks、平均或逐管 density 输入，不是 CP/PM、PW4 或 uniform positive-gain 的换名。原始 Besicovitch 全方向输入经具名最小维定理进入；不宣 arbitrary shading restriction 保 all-directions。no-compact-family 若将来成立，只经逆否得固定 \(n\) 的 \(d_n\ge n-1\)；existence of disjoint families 的反向低维结论未证明，不能声与 full Kakeya 等价。

## 12. 当前证明状态与实际交叉审查边界

§§2–10 给出完整 Baire 重构：fixed compact avoidance、σ 紧致障碍、局部低维族、far-pair 闭性与密度、自依赖消除、同一 residual、可数 whole-family 选择均已展开。原 KM typical-minimality 为具名高级输入；不以作者身份替代其数学依赖。Keleti 2026 讲义是已报告结论的来源，本稿仅复核其省略步骤。

现已实际全文逐式读取 root12《R0081_baire_reduction_to_compact_disjoint_families》、A12《R0081_code_space_and_baire_avoidance_audit》，以及终版 macro6、next6 和锁题 spec5。root/A 的 fixed-B 两步 finite good-code 网加 closed direction cover 合法；其 global residual 与非空 open position 条件相交，与本文 homothety 局部 residual 是两个合法证法。canonical far-pair 闭性、内部小 piece 与跨 whole unions 避让、所有 j/R 同一 residual、可数全族递归均独立核过，当前无强制数学修改。root/A 又已实际全文独核本 B12，B 自证不计作独立审查。本文公式括号的字面格式问题已修，未改变数学。下一题仍只作完整 compact 多 fibre 门的阶段 I 筛查；无新界、branch saving、new ID/major 或 no-family 结论，外部同行评审仍未有。
