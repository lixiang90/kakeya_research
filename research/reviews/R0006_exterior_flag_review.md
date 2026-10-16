# R0006：外积 flag 目标的独立审查与有限修补

日期：2026-10-16。审查人：`audit_four_dimensional`。被审文件：`notes/70_flags/R0006_flag_objective.md`。本轮只核验其中的有限维线性代数、给定假设下的列表/质量推论，不验证它们在五维真实 critical 路径上的全部输入，也不声明新颖性或 Kakeya 维数改进。

**结论：主体条件定理通过独立逐步审查。** 审查过程中指出并获主代理授权修改三处：相等幂指数时不保证短法向唯一/稳定；共同时间块的 floor 写回 \(m/q\) 并注明 \(J_1\asymp a\) 的同坐标归一化；一般交框补 bounded clipping，以确保最大奇异轴有界。最后一项补证由本审查人撰写，不能同时记为其独立审查；由 root 另行复核。以下清楚区分原主体与补证。

## 1. F6.1–F6.3：超可加与有限网格夹逼通过

对 \(A\in GL_3\)，\(\|\wedge^2 A\|=\sigma_1\sigma_2\)，故 determinant 成本 \(v\) 精确可加、外积成本 \(b\) 超可加。由 \(\sigma_1\sigma_2\ge\sigma_3^2\)，有 \(b\le2v/3\)；若 \(\sigma_1=N^{o(1)}\) 且下界也为 subpower，则 \(b\le v/2+o(1)\)。这些排序不等式即使部分成本为负也成立。

给定各段 \(b(A_i)\ge\ell\Delta r_i-\epsilon_i\) 及终端 \(b(P_m)\le\ell+\epsilon_0\)，前缀下界直接由超可加得出。上界用

\[
b(P_m)\ge b(P_k)+\sum_{i>k}b(A_i)
\]

移项，恰得 F6.2。任意连续段同理将其外侧各段先作下界。总缺陷

\[
0\le b(P_m)-\sum_i b(A_i)
\le\epsilon_0+\sum_i\epsilon_i=E
\]

即 F6.3；累计拼接缺陷望远镜相加等于该总缺陷，所以各项均不超过 \(E\)。任意两个相邻连续块先分组也一样。未发现遗漏可加性假设或符号反向。

这只证明已取得两端输入后的夹逼。原稿 \(j=3\) cap class、restricted determinant/secondary optimization 的闭合、同一批 systems 上同步选择两个目标，都没有由这段矩阵论证建立；原文件 §3.1 明确保留它们，正确。

## 2. F6.4 与一般外积版本通过

设 \(M=\wedge^2A\)。当 \(\sigma_2(A)>\sigma_3(A)\) 时，其 top-left singular line 唯一，次大/最大奇异值之比为 \(r_A=\sigma_3/\sigma_2\)。对 top line 的正交补投影 \(\Pi_\perp\)，

\[
\|\Pi_\perp M\|=r_A\|M\|.
\]

对 \(ML\) 的任意 top-right unit vector \(z\)，其归一化输出为 top-left vector。因此

\[
\|\Pi_\perp MLz/\|ML\|\|
\le r_A\|M\|\|L\|/\|ML\|
\le r_A/\rho.
\]

Hodge 是等距的，实际 top-left 二维 singular plane 的法向就是最短左奇异轴。这严格证明 F6.4；没有把 relative child normal 误当作实际 composite normal。若 composite 的 top 外积奇异值重根，每个 top-left vector 仍满足同一个投影界。足够小的 \(r_A/\rho\) 会与两条正交 top-left vectors 矛盾，故原文关于重根的有限说明也成立。

一般 \(\wedge^k\) 中，boundary gap \(\sigma_k>\sigma_{k+1}\) 保证 top-left Plücker line 唯一，次大比为 \(\sigma_{k+1}/\sigma_k\)，同一证明适用。实际 top-\(k\) singular plane 的 wedge 为 decomposable top vector；无需把重根空间中的任意向量都解释为 plane。主角满足

\[
\sin^2\theta_{\max}\le1-\prod_i\cos^2\theta_i,
\]

所以 Plücker line 的角度界确实控制最大 principal angle，没有方向反转。

将 \(\rho=N^{-\delta}\)、\(r_A\le N^{-\gamma}\)、\(\delta\le E<\gamma\) 代入得 F6.5。若只有 subpower gap，原文没有夸大成固定幂对齐，正确。

## 3. 条件 flag 分类与反例通过

对固定正 depth/segment length，最大轴 full 与给定 \(v,b\) 节点成本，严格得到三个幂指数 \(0,\mu r,(\ell_{\det}-\mu)r\)。\(k=1\) gap 控长轴，\(k=2\) gap 控短法向，范围与表格一致。相等幂指数并不意味着实际 \(\sigma_2=\sigma_3\)；仍可有常数或 subpower 谱隙。因此已将表格改为“不保证唯一或固定幂稳定的短法向”，而非断言绝无唯一法向。在零 depth 不应宣称固定幂 gap。

三项反例核查无误：

- \(\operatorname{diag}(1,1,\varepsilon)\) 与其自身复合、与 \(\operatorname{diag}(1,\varepsilon,1)\) 复合，分别给 \((1,1,\varepsilon^2)\)、\((1,\varepsilon,\varepsilon)\)，相同 determinant 成本而第二轴成本不同。
- 45 度旋转 child 的 relative top planes 可以成常角，但实际 composite 的 top-plane 法向误差为 \(O(\varepsilon)\)，且外积缺陷只有 \(O(1/\log N)\)；不反驳 F6.4。
- normals 夹角 \(\asymp\varepsilon\)、strip widths 也为 \(\varepsilon\) 时，交集仍有两根常数长方向；纯 rank 2 不提供 flag 增益。

## 4. 交框 determinant、列表与 floor 成本

对正 strip widths \(a,b\)，双 normals 的对偶向量满足 \(\|u\|=\|v\|=1/\tau\)，且

\[
\left|\det(e_0,au,bv)\right|=ab/\tau.
\]

原 dual-frame 证明在目标薄区间 \(\max(a,b)/\tau\ll1\) 已经足够，第二奇异轴至多 \(C_R\max(a,b)/\tau\)，外积成本下界正确。在一般宽度下，该直接 frame 的最大轴可能很大，因此不能仅凭此 frame 宣称最大轴 \(O(R+1)\)。现已补 bounded clipping：以一条实际 affine 轨道为 center，对差轨道使用 weighted normals 的 SVD，并将每轴截到 \(2(R+1)\)。这保留 determinant 上界和短轴上界。**该 clipping 补证为本审查人所写，待 root 独立核验，未将自查登记为独审。**

同一当前原始 observation 能以 \(L_1,L_2\) 列出两个输入 labels，且输出是其确定函数时，pair 列表至多 \(L_1L_2\)，正确。不同参考时刻的两次知识不满足这个前提。

真实质量推论应使用共同时间块 \(q\)：

\[
m_1/q\ge nJ_1/K,
\quad m_{\rm new}\ge f m_1
\ \Longrightarrow\
m_{\rm new}/q\ge fnJ_1/K.
\]

所以一般充分损失为 \(\max\{1,KJ_{\rm new}/(fJ_1)\}\)。当所有 widths 与 Jacobians 均在**同一单位 tangential 坐标**中，\(J_1\asymp a\) 才给 \(J_{\rm new}/J_1\le C_Rb/\tau\)；从而所印 \(K_{\rm new}\) 正确。比较常数必须包含原 \(J_1\asymp a\) 的损失。未经归一化的 raw 短时间框一般带两根 tangential widths，不能跳过它们直接代入。现版已经补清，共同 \(q\) 无遗漏地取消。

不同深度、不同时间块或旧 \(n(r)\) 与新 \(n(0)\) 不同的情形不能套这个同层 floor 推论；原文件的限制正确。

## 5. 审查范围与未解决输入

主体线性代数定理及明确前提下的 list/floor 推论成立。修补后的 clipping 证明由 root 另核验；它不负责原始 \(p_L\) 的 global pair matching。完整三维 critical class、极值同步选择、真实 source 是否给足够谱隙与 near-product 比、以及 candidate 是否为合法 terminal competitor，均未在此完成。

没有高维 Kakeya 维数结论，也没有将部分条件反例升级为完整 critical/Kakeya 反例。
