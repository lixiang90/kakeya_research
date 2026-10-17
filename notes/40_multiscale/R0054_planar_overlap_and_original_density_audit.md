# R0054：平面重叠、原平均密度与共同因子图的低维闭包

2026-10-17，A。已读 GOAL／STATE／ROADMAP／AGENTS、registry 全部 78 个状态、本轮 working_spec 及 R53 唯一 next。下文为实际五维单位管的完整原量词证明；所有用到的平面估计在此逐步证明，**不依赖三维 M3 或任何未重证的高级来源**。无有限实验代连续证明。正式全文独审须另读 root／B／macro／next 最终稿；本稿不以自审代独审。未经外部同行评审。

## 1. 对象、强目标及原体积归一

固定 $C_0\ge1$。令

$$Z=\{x\in\mathbb R^5:x_4=x_1x_2,\ x_5=x_1x_3\}.$$

原有限单位轴 $\ell_i=\{a_i+tv_i:|t|\le1/2\}$ 满足 $|v_i|=1$、$\ell_i\subset B(0,10)\cap N_{C_0\delta}Z$。$T_i=N_\delta\ell_i$ 是真正半径 $\delta$ 管，可测 $Y_i\subset T_i$，$E=\bigcup_iY_i$；给原非负权 $w_i$、$W=\sum_iw_i>0$。任意 fixed-radius $C_1\delta$ physical $S^4$ 方向帽的原权和不超过 $\alpha$，重复方向／管不去重。常数可依 $C_0,C_1$ 和原有界 chart，不依 $\delta$、权跨度、族数或密度。

对 round tube，精确体积为 $v_5(\delta)=\omega_4\delta^4+\omega_5\delta^5$；若原统一形状采用 flat cylinder，则为 $\omega_4\delta^4$。两者均所有标签同体积、$v_5\asymp\delta^4$，全部端帽都要保留。定义

$$I=\sum_iw_i|Y_i|=\lambda v_5(\delta)W,\qquad 0<\lambda\le1.$$

证明更强的 uniform 结论

$$|E|\ge c\,\frac{\lambda^2\delta^4W}{\alpha\log(2/\delta)}.\tag{1}$$

因为 $1/\log(2/\delta)\ge c_\varepsilon\delta^\varepsilon$ 且 $\lambda^2\ge\lambda^3$，(1) 包含上一 spec 的 $\delta^{4+\varepsilon}\lambda^3W/\alpha$。它若成立仍是平面／直线闭包，不新立 ID／高维增益／novelty；完整共同因子模板本轮后冻结。

## 2. whole-axis 系数迫使只有平面支和直线支

记 $P_2=x_4-x_1x_2$、$P_3=x_5-x_1x_3$。对 $x\in\ell_i$，取近 $Z$ 点，因 bounded chart 内两 $P_k$ 的梯度有固定上界，距离假设给 $|P_k(a+tv)|\le K\delta$。实际全 $T_i$ 也满足此类界（邻域常数只增加固定量）。展开

$$P_k(a+tv)=P_k(a)+t(v_{k+2}-a_1v_k-a_kv_1)-t^2v_1v_k,\qquad k=2,3.$$

在 $t=0,\pm1/2$ 比较，严格给

$$|P_k(a)|\le K\delta,\quad |v_{k+2}-a_1v_k-a_kv_1|\le2K\delta,\quad |v_1v_k|\le8K\delta.\tag{2}$$

前两项说明 $|v_4|+|v_5|\le C|(v_1,v_2,v_3)|+C\delta$。由 $|v|=1$，取小的固定 $\delta_0$ 后

$$s:=|(v_1,v_2,v_3)|\ge\eta>0.\tag{3}$$

设 $u=|v_1|$、$q=|(v_2,v_3)|$；则 $u^2+q^2\ge\eta^2$，$uq\le C\delta$。若 $q\ge\eta/\sqrt2$，则 $u\le K_1\delta$；否则 $u\ge\eta/\sqrt2$，从而 $q\le K_1\delta$。据此将每个原标签恰分到

- A 支：$|v_1|\le K_1\delta$ 且 $|(v_2,v_3)|\ge\eta/\sqrt2$；
- B 支：$|(v_2,v_3)|\le K_1\delta$ 且 $|v_1|\ge\eta/\sqrt2$。

可按上述 $q$ 阈值消除所有边界歧义。小 $\delta$ 时无漏掉的 intermediate $|v_1|$ dyadic 层。此判断用的是全单位轴；稀疏 marks 不能提供 (2)。剩余 $\delta\in[\delta_0,1]$，固定数 $C_1\delta$ 帽覆盖 $S^4$ 给 $W\le K\alpha$，而 $|E|\ge I/W\asymp\lambda\delta^4$，用 $\lambda\le1$ 和 $\log(2/\delta)\ge\log2$ 直接得到 (1)；故以下小尺度分支覆盖了完整范围。

## 3. A 支实际近平面，端帽和空间 overlap

按 midpoint $a_1$ 的半开 $\delta$-bins 唯一分包，以左端点 $b\in\delta\mathbb Z$ 标记。$|a_1-b|\le\delta$，整轴 $x_1$ 漂移至多 $K_1\delta/2$，真正管的端帽再添 $\delta$。因此所有实际 $Y_i$ 在 $|x_1-b|\le K_2\delta$ 内。

又由实际 tube 上的 $|P_2|,|P_3|\le K\delta$ 与 $|x_2|,|x_3|\le11$，

$$|x_4-bx_2|\le K_3\delta,\qquad |x_5-bx_3|\le K_3\delta.\tag{4}$$

这证明整条原 tube 在固定 $O(\delta)$ 的 affine 2-plane

$$\mathcal P_b=\{x_1=b,\ x_4=bx_2,\ x_5=bx_3\}$$

邻域内，常数统一于 bounded $b$。它没有把只有零集关系的两个 normal 免费当三个 normal；第三约束来自 A 支慢 $x_1$ 运动和真实 midpoint 包。

令 $E_b=\bigcup_{i\in b}Y_i$，$I_b=\sum_{i\in b}w_i|Y_i|$，$W_b=\sum_{i\in b}w_i$。原标签不拆，故 $\sum_b I_b=I_A$、$\sum_bW_b=W_A$。包的 $x_1$ 支撑是固定倍 $\delta$ 格扩大，因而

$$\sum_b1_{E_b}\le K_4 1_{E_A},\qquad \sum_b|E_b|\le K_4|E_A|.\tag{5}$$

这是 actual union 的空间重叠，不把包数 $O(\delta^{-1})$ 当常数，不对 shadings 作填充。

## 4. A 支投影保 physical angular cap，含正反方向

投影 $\pi_A(x)=(x_2,x_3)$，置 $r_i=|(v_{i,2},v_{i,3})|\ge\eta/\sqrt2$、$\theta_i=(v_{i,2},v_{i,3})/r_i\in S^1$。由 (2) 和 A 支条件，同包内

$$v_1=O(\delta),\quad v_4=bv_2+O(\delta),\quad v_5=bv_3+O(\delta).$$

除以 $r_i$ 后，$v_i/r_i=(O(\delta),\theta_{i,1},\theta_{i,2},b\theta_{i,1}+O(\delta),b\theta_{i,2}+O(\delta))$。归一映射在 $|v_i/r_i|\ge1$ 上 Lipschitz，所以一个 oriented $O(\delta)$ projected 帽的原方向预像直径 $O(\delta)$，其原权 $\le C\alpha$。物理大一点的 $C\delta$ 帽可用固定数原 $C_1\delta$ 帽覆盖，不需预设同一格。

下文用 projective 角 $\chi(\theta,\theta')=\arccos|\theta\cdot\theta'|\in[0,\pi/2]$。一个 projective 小帽分成 $\theta$ 和 $-\theta$ 两个 oriented 帽，所以总权仍 $\le C\alpha$，不假定所有方向位于同一半圆。由一维角段覆盖，对所有 $\delta\le h\le1$

$$\sum_{\chi(\theta_i,\theta_k)\le h}w_k\le C\alpha h/\delta.\tag{6}$$

(6) 由 finest angular cap 推出，不是额外 all-scale Frostman 输入。重复位置／方向及极不均匀权均由同一个原帽 cap 计入。

## 5. 自含平面两管相交与完整 weighted $L^2$

取 $D_i$ 为含 $\pi_A T_i$ 的平面 rectangle：中心在原 projected midpoint，方向 $\theta_i$，长度不超过二、宽度 $C\delta$。原 projected segment 长 $r_i\le1$，round cap 可以完整放入这个 rectangle；无需丢端帽或改时钟。对两条 rectangle，平行或近乎平行时面积不超过 $C\delta$；非平行时被两条无限 strip 的相交控制，面积不超过 $C\delta^2/\sin\chi$。两者合并为

$$|D_i\cap D_k|\le C\frac{\delta^2}{\delta+\chi(\theta_i,\theta_k)}.\tag{7}$$

当 $\chi\le\delta$ 用单 rectangle 面积；否则在 $[0,\pi/2]$ 上 $\sin\chi\asymp\chi$。中心可任意，反向平行已由 projective 角处理。

固定 $i$，将 $\chi$ 分为 $\chi\le\delta$ 和 $2^m\delta<\chi\le2^{m+1}\delta$，共 $O(\log(2/\delta))$ 层。用 (6)，每层对 $\sum_kw_k|D_i\cap D_k|$ 的贡献至多 $C\alpha\delta$；低角层也是此界。因此对 $L=\log(2/\delta)$、$F_b=\sum_{i\in b}w_i1_{D_i}$，

$$\|F_b\|_2^2=\sum_{i,k\in b}w_iw_k|D_i\cap D_k|
\le C\alpha\delta W_bL.\tag{8}$$

包括 $i=k$ 的项；其 $w_i^2$ 由同 cap 的 $w_i\le\alpha$ 控制。没有先 uniformize 原权、没有用有限 separated 样本代一般族。

## 6. 三维纤维、实际 incidence 与二次 Jensen

以纯坐标 splitting $(x_2,x_3)$／$(x_1,x_4,x_5)$ 作 Fubini，Jacobian 恰一。由 (4) 及 $x_1$ 包界，每个 $E_b$ 的三维 coordinate 纤维体积 $\le C\delta^3$。无需把这些坐标纤维误称为 $\mathcal P_b$ 的正交 normal。令

$$f_b(u)=\delta^{-3}\int_{\mathbb R^3}1_{E_b}(x_1,u_1,u_2,x_4,x_5)\,dx_1dx_4dx_5.$$

则 $0\le f_b\le C$、$\int f_b=\delta^{-3}|E_b|$，故

$$\|f_b\|_2^2\le C\delta^{-3}|E_b|.\tag{9}$$

因为 $\pi_A Y_i\subset D_i$ 而 $E_b\supset Y_i$，Fubini 对每个原标签给 $\int_{D_i}f_b\ge\delta^{-3}|Y_i|$，遂

$$\int f_bF_b\ge\delta^{-3}I_b.$$

Cauchy–Schwarz、(8)、(9) 得

$$\delta^{-6}I_b^2\le C\alpha\delta^{-2}|E_b|W_bL,
\qquad |E_b|\ge c\frac{I_b^2}{\alpha\delta^4W_bL}.\tag{10}$$

零权包忽略。该推导只有 $I_b$，未以逐管 $\lambda_b$ 下界代替平均，也未假 $Y_i$ 连通／regular／沿整轴均匀。$\lambda\ll\delta$、仅端帽有 marks 或每条原权相差任意大都适用。

用 $\sum_bI_b^2/W_b\ge I_A^2/W_A$ 和 (5)，A 支整体满足

$$|E_A|\ge c\frac{I_A^2}{\alpha\delta^4W_A L}.\tag{11}$$

若 $I_A\ge I/2$，$W_A\le W$，代 $I=\lambda v_5W\asymp\lambda\delta^4W$ 即得 (1)；无需 A 支保固定比例 $W$。

## 7. B 支直线包：原角 cap 直接控制全部包权

B 支按 midpoint $(a_2,a_3)$ 的半开 $\delta$-squares 唯一分包，左端点 $(b_2,b_3)$。由 $v_2,v_3=O(\delta)$、near-graph 及真实 tube 厚度，全部实际事件满足

$$|x_2-b_2|,|x_3-b_3|\le C\delta,\quad
|x_4-b_2x_1|,|x_5-b_3x_1|\le C\delta.$$

所以 tube 近同一 affine line $\mathcal L_b=(s,b_2,b_3,b_2s,b_3s)$。投影 $x_1$ 速度非短，且原方向由 (2) 给

$$v_i=v_{i,1}(1,0,0,b_2,b_3)+O(\delta).$$

单位化后，所有该包方向在 $\pm d_b$ 的 $O(\delta)$ 帽中，$d_b=(1,0,0,b_2,b_3)/\sqrt{1+b_2^2+b_3^2}$。故 $W_b\le C\alpha$，不因不同轴位置而失效；原 angular 假设按 directions 计所有标签权。

逐点 $\sum_{i\in b}w_i1_{Y_i}\le W_b1_{E_b}$，故 $|E_b|\ge I_b/W_b\ge I_b/(C\alpha)$。这些包的 actual 支撑在 $(x_2,x_3)$ 的固定倍 $\delta$-squares 中，有界 overlap，遂

$$|E_B|\ge c I_B/\alpha.\tag{12}$$

若 $I_B\ge I/2$，则 $|E|\ge c\lambda\delta^4W/\alpha$，强于 (1)。A/B 是原标签分区，必有一个 incidence 至少 $I/2$；不把两个分支并集的体积当可加，不要求原 indices 各保同样比例 marks。

## 8. restriction／shading 的双向范围及来源层次

对于任意子族／更小 shading，所有几何和 angular upper 仍有效，但必须按新的 $I',W',\lambda'$ 重算。若额外证明 $I'\ge\theta I$、$W'\le W$，(1) 的原二次因子至少保 $I'^2/W'\ge\theta^2I^2/W$；没有 retained-incidence 下界就不能声称保原平均密度。逐管输入当然蕴含平均版本；本轮分支／包只作整 label 唯一划分并完整保留每个 $Y_i$，所以若原逐管密度至少 $\lambda_*$，各分支／包内剩余管仍保相同逐管下界。只有另行缩小 shading 才不自动保原 $\lambda_*$；平均证明则独立使用上述 $I^2/W$ 预算，不需要逐管输入。

最初 M3 的全密度 $\lambda^3$ 工具在这里并非必要：actual 图的全单位轴迫近平面／近直线，(7)–(10) 已自含推出更强 $\lambda^2/\log$。这不是 R53 exact Q3⇔M3 的再次命名，也不是一般 R5 原族已转到本图；它是一个严格更低维的特殊来源闭包。旧 CP/PM、PW、general→sticky、matrix/mixed 或 smooth-lift 冻结不因此重开。不从两条 bilateral residual 形式看似耦合就预认一般高维增长。

因所有解析输入在这里证明，无需重审 OpenAI3D 97 页或新增一手 PDF；也不把此初等 source 应用声明为新颖／重大数学成果。对一般三维 variety、不同二次图或任意原 narrow family 的提取没有证明；不能用本模型替代这些责任。

## 9. $p<2$ 密度指数的完整实际校准

在 $Z$ 内固定 2-plane $\mathcal P_0=\{(0,x_2,x_3,0,0)\}$，取原方向圆上的一个半圆 $\delta$-separated net，$W\asymp\delta^{-1}$、$w_i=1$，每个 physical $C_1\delta$ 帽至多固定个方向，$\alpha=O(1)$。所有单位轴以原点为中点，整轴 exact 位于 $Z\cap B(0,10)$，故也满足全部 near-contained 假设。

令 $\delta\le\tau\le1$，对每根轴取 $|t|\le\tau/2$、垂直轴的四维半径 $\delta$ flat cylinder 作为真实 $Y_i\subset T_i$。其体积恰 $\omega_4\tau\delta^4$，实际 round-tube 密度 $\lambda=\tau/[1+(\omega_5/\omega_4)\delta]\asymp\tau$。并集位于此 2-plane 的半径 $O(\tau+\delta)$ disk 乘三维 normal $\delta$-ball中，故

$$|E|\le C\delta^3(\tau+\delta)^2\le C\delta^3\tau^2.\tag{13}$$

若把目标中的 $\lambda^2$ 换成任意 $\lambda^p$、$p<2$，即使仍允许 $\delta^\varepsilon/\log(2/\delta)$，取 $\tau=\delta^a$（$0<a<1$）和 $0<\varepsilon<a(2-p)$。改进式的右边是 $\gtrsim\delta^{3+\varepsilon+ap}/\log(2/\delta)$，与 (13) 的 $\lesssim\delta^{3+2a}$ 矛盾，因 $\delta^{a(2-p)-\varepsilon}\log(2/\delta)\to0$。这是全部输入合法的密度校准，不是 Kakeya 反例，也不单独证明 log 因子不可去。

## 10. 本轮结论与停止

(1) 已由 whole-axis 两支几何、自含平面 overlap、原权 Cauchy–Schwarz 与空间 bounded overlap 完整证明；所有端帽、任意平均密度和重复方向均已支付。它当然包含原 $\lambda^3\delta^{4+\varepsilon}$ 待证模型，但归为低维平面／直线闭包，无新数学 ID／新颖性／major／普通五维界。

只在 root／B 最终全文及 macro／next 实际读审后写正式 review；不能用本稿作为独立验证自己。本轮结束即冻结整个共同因子模板，不续第三输出、ambient、rank 或系数微调。下一唯一任务须由宏观比较选择真实一般 n5 缺口，长期 Goal 保持 active。无需额外数学实验，未经外部同行评审。

本轮最终 macro／next 已全文实读。下一 G3 是任意固定 format、degree≤D、real dimension≤3 的五维代数集（含奇点、$\delta$ 依赖系数）的整单位轴近邻域估计；本轮与 R53 的已付全称范围均不覆盖它。registry 中现有有限 seed、PW／CP／mixed 或一般→sticky条目也未给该全部原选择的任意 $\lambda^3$ 转移；这只是“尚无已付桥”，不是已证明不存在已知一手定理。下轮必须先查实际一般代数管定理，若已是既有全称输入的推论则调用后停止，不认证新颖性。flat 三维平面子例反向含 M3，但并未支付任意奇／退化近簇的正向一般转移。

局部重读 HRZ 库内 v1 Def5.1／5.2、(29)、Lemma5.3（extracted 按 `split('\n')` 1016–1056，PDF19）：原对象为 transverse complete intersection，切向条件给 $T\cap B(x_0,2r)\subset N_{4\delta}Z$；维数≤$k-1$ 时 $k$-broad vanishing 的尺度条件另列。故 next 留出的真实 $r$-轴片、端点／球边、$h=\delta/r$ 时的原 $\alpha_h$、entry 与 shading 预算确为必要，不能把 local G3 当 $k=4,m=3$ 的直接 tiny 替换。G3 尚未证也未否；本稿不在本轮研究它。
