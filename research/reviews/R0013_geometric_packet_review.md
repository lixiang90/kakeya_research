# R0013：真实构型与四平面包接口交叉审查

2026-10-17。审查者：audit_four_dimensional。审查对象：

- notes/40_multiscale/narrow_five_dimensional/R0013_geometric_attack.md；
- notes/40_multiscale/narrow_five_dimensional/R0013_packet_input_limit.md。

**结论：通过，可按两稿当前限定范围归档。未发现必须修正的数学问题。** 真实构型只否定沿一根 rich central tube 自动识别固定三平面的捷径；它不反驳主任务 (NG) 或允许全局小质量修剪的兼容性命题。包估计条件于 SRC-001/DIR-003，即完整四维证明及其输入正确；刷计数、包密度保持与全刷有界重叠均仍是显式假设。主五维幂 gain 未证明。

审查者在 primary-source audit 中也独立推导了固定四平面包的有限输入接口。本报告核对 root 稿的完整量词与原构型，不把互相引用计作新增的来源验证或第二个独立定理。

## 1. 实际单位线段、满量级方向和所有 cubical incidences

构型的
\[
 L(t)=(t,-d+bt,-e+ct,f+dt,g+et)
\]
具有常向量 \(v=(1,b,c,d,e)\)，而
\[
 D_x=\{(a,b',c',tb'-x_2a,tc'-x_3a)\}
\]
沿 \(L(t)\) 确实含 \(v\)：后两分量分别是
\(tb-(-d+bt)=d\)、\(tc-(-e+ct)=e\)。

轴取 \(0\le t\le|v|^{-1}\) 时 Euclidean 长度恰为 1。固定小 \(r\) 可以保证所有轴包含共同的 \([1/4,3/4]\) 时钟区间；anchors 也统一有界。故原稿没有把 graph-time 长度误作 Euclidean 单位长度。

在有界盒内，\(D_x\) 为系数有界且 Lipschitz 的 graph。若轴穿过原半开 cube \(Q\)，取实际轴点 \(x_T\in Q\)，则
\[
 \operatorname{dist}(\widehat v,D_{x_Q})\le C|x_T-x_Q|\le C\delta.
\]
这对每一个实际产生的 cube label 都成立，包括补全方向后新出现的共同 cubes；没有只核精确轴交点而漏掉近交，也没有删除原 full shading 的标签。half-open 约定使 \(P_\tau\) 的所属 cube 唯一；轴通过 cube 边界点也仍是原 spec 的合法 whole-cube incidence。

hot map
\[
 (\tau,b,c)\mapsto (b,c,\tau b,\tau c)
\]
在 \(b\ge\beta>0\) 的固定盒上双 Lipschitz：前两坐标给 \(b,c\)，第三坐标除 \(b\) 给 \(\tau\)。归一化方向 chart 同样双 Lipschitz，因此大固定 \(A\) 的 \(A\delta\)-grid 确保方向分离，共 \(\asymp\delta^{-3}\) 个。把它与 central direction 扩为固定四维方向 patch 中的 maximal \(\delta\)-separated set，覆盖与 packing 两边都给 \(\#\mathbb T\asymp\delta^{-4}\)。每个补入方向仍使用同一条直线公式，所以没有方向来源缺口。

所有单位 cubical tubes 均有 \(\asymp\delta^{-1}\) 个 cubes、体积 \(\asymp\delta^4\)。全 shading 的总 incidence mass 因而 \(\asymp1\)，满足原始平均 dense 条件。

## 2. Richness、强制平面和沿线旋转

指定 \(d=\tau b,e=\tau c,f=-\tau^2b,g=-\tau^2c\) 后，轴在 \(t=\tau\) 精确过 \(P_\tau=(\tau,0,0,0,0)\)。固定 \(\tau\) 的 \((b,c)\)-grid 给至少 \(c\delta^{-2}\) 个不同参与 labels。

反向 upper 也正确：在 \(S^4\) 上，某三平面的 \(C\delta\)-方向邻域体积 \(O(\delta^2)\)，每个分离方向占体积 \(\gtrsim\delta^4\)，故任何窄 cube 的总参与数至多 \(C'\delta^{-2}\)。因此这些 cubes 达到局部最大量级，且未漏计补入的 tubes。

在
\[
 E_\tau=\operatorname{span}(e_1,e_2+\tau e_4,e_3+\tau e_5)
\]
内可选择三个统一 conditioned 的实际方向。若另一个三平面 \(W\) 把所有这些方向包含在 \(C'\delta\) 邻域，按该 frame 展开并投影到 \(W^\perp\)，得到
\[
 \|P_W-P_{E_\tau}\|\le C_{\beta,C'}\delta.
\]
同维子空间的双向 projector gap 可由最大 principal angle 表示，因此这个条件足以强迫 \(W\) 接近整个 \(E_\tau\)，不是只强迫其中一条轴。

两组旋转发生在相互正交的二维坐标块内，故
\[
 \|P_{E_\tau}-P_{E_\sigma}\|
 =|\sin(\arctan\tau-\arctan\sigma)|
 =\frac{|\tau-\sigma|}
 {\sqrt{(1+\tau^2)(1+\sigma^2)}}.
\]
固定 \(W\) 只能匹配长度 \(O(\delta)\) 的 \(\tau\)-区间，即 \(O(1)\) 个 \(A\delta\)-grid cubes。共有 \(\asymp\delta^{-1}\) 个这样的 central rich cubes，确实占 central tube 的固定正比例。以上足以反驳原稿明示的“沿该单根管自动固定平面”捷径。

## 3. 体积与质量边界防止误升级

completion 部分仍有 \(\asymp\delta^{-4}\) 个方向，且 \(f=g=0\)。固定 \(t\in[1/4,1/2]\)，位置映射
\[
 (b,c,d,e)\mapsto(tb-d,tc-e,td,te)
\]
的 determinant 是 \(t^4\)，在共同时间区间上统一双 Lipschitz。一个 transverse \(\delta\)-cube 只容纳 \(O(1)\) 个这些点。每个点所属原五维 cube 的固定 \(t\) 截面有四维体积 \(\delta^4\)，所以截面 union 体积 \(\gtrsim1\)，积分得 \(|U|\gtrsim1\)。统一有界盒给 upper，故 \(|U|\asymp1\)。

hot tubes 的总质量 \(\asymp\delta^{-3}\delta^4=\delta\)。central rich cubes 与其 hot labels 的 incidence mass 上下均为 \(\asymp\delta^2\)：下界来自所指定的 \(\delta^{-1}\times\delta^{-2}\) 个 pairs；上界由每个 cube 的 \(\delta^{-2}\) packing upper。故原稿完全允许 averaged pruning 删除这一 skeleton。它没有证明小 union 情况下的大贡献 incidence 会具有同样旋转障碍。

## 4. 固定四平面包：DIR-003 的实际调用

令原管全部处于固定仿射 \(H^4\) 的 \(C\delta\)-邻域。原方向法向分量 \(O(\delta)\)，投影长度与 1 可比；一个投影方向 \(\delta\)-bin 中只能有 \(O_C(1)\) 个原分离方向。有限球面 charts 内，这也给 graph-slope bin 的质量 \(\alpha=O_C(1)\)，不是误用实际 Lebesgue 密度。

各 projected axis 的某个 chart 时间分量有固定下界。原轴在一个 projected \(\delta\)-time bin 内的长度 \(O(\delta)\)，只会穿过常数个原 cubes；所以原 \(\lambda/\delta\) 个访问时标在投影后保留常数比例。若需要分固定时间窗，每根轴可选择保留最多 marks 的窗并作直线延长，仍只使用原 marked visits。常数损失可通过先把 \(\theta\) 取小于 DIR-003 的 density threshold 吸收。

DIR-003 对投影 marked cell 集给
\[
 \#E^{(4)}\gtrsim_\epsilon
 \delta^{-1+\epsilon}\lambda\#\mathbb T_j.
\]
这里投影与固定网格重分箱只损固定常数：每个原 cube 的四维投影直径 \(O(\delta)\) 且含半径 \(c\delta\) 的四球，其常数扩大后的网格 covering 数与投影 union 体积除以 \(\delta^4\) 可比。故获得原稿 P2，而不是只有扩大后 footprint 的体积界。

对原不交 whole-cube 并，逐 cube 求投影体积上界便有
\[
 |\pi_HE_j|\le C\delta^{-1}|E_j|.
\]
从而 P1 的 ambient 因子准确为
\[
 |E_j|\gtrsim_\epsilon
 \delta^{4+\epsilon}\lambda\#\mathbb T_j.
\]
没有把投影满维直接当成五维满维，也没有在 packet restriction 后免费归一化概率。只有同一原保留 shading 达到逐管密度 threshold 才适用；原稿已将其列作实际假设。

## 5. Brush 指数与包级 sharp 校准

在 P3、密度保留和 bounded overlap 都另外成立时，P1 给
\[
 |U|\gtrsim_\epsilon\delta^{4+\epsilon}\lambda N,
 \qquad
 |U|^3\gtrsim_\epsilon
 \delta^{3+\epsilon}\lambda^4\rho.
\]
代数无漏项；它只回到维数四基线，不能通过把 \(\eta,\epsilon\) 取小得到固定 \(\sigma>0\)。

固定 \(H^4\) 中 \(\delta^{-3}\) 个方向的真实单位 star，作为五维管的 total volume \(\asymp\delta\)，union 又在 bounded \(H\) 的 \(O(\delta)\) 邻域内，体积至多 \(C\delta\)。因此对所有四平面包统一把 \(\delta^4\) 改成 \(\delta^{4-\sigma}\) 确实不可能。这个例子只有 \(\delta^{-3}\) 个方向，原稿正确区分了包级 sharpness 与主任务的 \(\delta^{-4}\) 方向数。

## 6. 三轴闭合与共享时钟补充接口

root 的精确三轴事实通过：三条独立轴从 \(y\notin P^3\) 交 \(P\)，三交点不能共线；因此 \(P\cap(y+W^3)\) 恰为二维仿射平面。\(y+W\) 内任何不平行此平面的线都与之相交。两轴例中 \(y+\mathbb Re_4\) 始终有第五坐标 1，确实不交 \(P\)。这没有提供三轴事件的 incidence mass，也没有定量近似成本。

几何攻击稿 §8 的线性接口亦已核：

- \(M_t=\bigl(\begin{smallmatrix}t&-1&0\\0&t&1\end{smallmatrix}\bigr)\) 的 kernel 是 \(\operatorname{span}(1,t,-t^2)\)，两个 blocks 必须使用共同 \(t\)。
- \((t,X,Z)\mapsto(X,t,-Z/2)\) 给参数 \((a,b_0,c_0)=(b,-d,-f/2)\) 的标准 horizontal line。已核官方 Fässler–Orponen Theorem1.5/Remark1.7 的声明及本地原文；没有复核其全部证明。
- diagonal \(P\) 的两个 marginal 都可满三维，但 joint union 仍三维；该例方向投影仅二维，原稿没有误报为主任务反例。
- \(P=(b,d,c,c,e,0)\) 的方向投影满四维，但固定第一 parameter block 后第二 block 只剩一维；其 joint projection determinant 仍为 \(t^4\)，边界正确。
- a.e. 时间的单块结论不能直接套到随 \(t\) 改变的 conditional fibers；positive segments/Hausdorff 声明也不是本轮任意零散 dense marks 的统一有限尺度估计。

第 8 节只是合法的专用模型接口，不是任意 \(V_Q\) 的已证 normal form。两稿均明确这一限制，可按当前结论归档。
