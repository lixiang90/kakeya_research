# R0053：三维完整 maximal 输入、原平均密度及双向闭包审计

2026-10-17。本稿核 R0053 的精确单位直线／regular quadric 模型、修订 spec §6 的固定抛物柱近 contained 子类及具名输入的应用；不重证 OpenAI 三维论文全部 97 页，不证明一般四维 maximal 或高维 Kakeya。原权、实际可测 shading、整个单位轴及端点均保留。内部逐步审查不等于外部同行评审。正式全文审查另见本轮指定 review。

## 1. 当前命题、量词和停止条件

固定 $c>0$、有界空间及管厚常数。$P:\mathbb R^4\to\mathbb R$ 非零、次数至多二、系数绝对值至多一。有限单位轴 $\ell_i\subset\{P=0\}\cap B(0,10)$ 的固定邻域满足 $|\nabla P|\ge c$；$T_i=N_\delta\ell_i$ 是真实管，体积 $v_4(\delta)\asymp\delta^3$ 与 $i$ 无关。给非负原权 $w_i$、$W=\sum_iw_i>0$、可测 $Y_i\subset T_i$，以及 physical $S^3$ 上任意半径 $C\delta$ 帽的原总权不超过 $\alpha$。记

$$E=\bigcup_iY_i,\qquad I=\sum_iw_i|Y_i|,\qquad \lambda=I/[v_4(\delta)W].$$

(Q3) 要求 $\forall\varepsilon>0\ \exists c_{\varepsilon,c}>0,\delta_0>0$，对所有这些数据及任意 $0<\lambda\le1$，

$$|E|\ge c_{\varepsilon,c}\delta^{3+\varepsilon}\lambda^3 W/\alpha.\tag{1}$$

常数不依赖 $P,\delta,\lambda$、权重分布、管数或最小非零权。先核这一命题的完整应用或其真实障碍；§11 再核修订 spec §6 的固定近 contained 子类；不以逐管 near-full 替换平均密度，不续调阈值。下文同时证明超平面子例已反推出三维完整 $L^3$ 输入，因此此模型闭包不另登记新数学 ID／独立高维机制。

## 2. 一手输入与当前版本责任

本地实际重读 `literature/extracted/openai_2026_three_dimensional_kakeya_maximal.txt`，按 `split('\n')`：80–146（PDF 2–3，Theorem 1.1 及 (1.1)）、4705–4803（PDF 90–92，§10.2 的离散／函数转换）、4867–4884（PDF 93，可测性及 Theorem 1.1 完成）；§11 的有限范围已在 R51 读核，本轮不追审其高级证明。原输入为

$$T_\delta(a,\omega)=\{a+t\omega+u:|t|\le1/2,\ u\perp\omega,\ |u|\le\delta\},\quad |T_\delta|=\pi\delta^2,$$

$$K_\delta f(\omega)=\sup_a(\pi\delta^2)^{-1}\int_{T_\delta(a,\omega)}|f|,\qquad
\|K_\delta f\|_{L^3(S^2)}\le C_\eta\delta^{-\eta}\|f\|_3\quad(\forall\eta>0).\tag{2}$$

这是任意 $f\in L^3$、所有中心和任意密度的完整定理声明。PDF 3 的 (1.1) 明写 $\lambda^3$，并区别只适用 $\lambda\ge\delta^{\eta(\varepsilon)}$ 的 set 输入。§10.2 先得 $(10.19)$ 中 $N^{-\xi}nN\max(N^{-1},\lambda)^{p+1}$，再作函数转换及 $p\downarrow2$；不能把 near-full 有限读出直接改名为 (2)。§11 对固定三维常曲率／特定平移不变 phase 的扩展不自动覆盖任意 $f(t)$ 或高维曲面近切管。本稿只调用欧氏 (2)。

官方 [README](https://raw.githubusercontent.com/openai/math/main/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/README.md) 的标题／日期和 [PDF 项目页](https://github.com/openai/math/blob/main/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/paper.pdf) 本轮在线复核；本地 PDF 925416 bytes，SHA256 `49cc52aa3de89f0e91d181b00ee8050fb29635ee0da9f29145d52318e7168204`。root 本轮逐级官方 Git API 核 root tree `1581d4cbdd69a0faf34b2089614fe2a814316a6a` → preprints `df0564b2deaab87e07854b6344d8c2f037682e77` → manuscript `b3ef56e6408c303f96e3f3d8f9771cbea2ec703b` → PDF blob `fa215607c58ade54fc6d60dec81530b33f15ab0c`，与库存一致。网页元数据自身不代替字节核验。仍将 (2) 列为具名文献输入，未认证整篇 proof。

## 3. 物理纤维：可依赖实际事件，无须缩短轴

写 $P(x)=x^THx+l\cdot x+c_0$，$H$ 对称。系数及空间有界给 $|P(p)|\le A\delta$（$p\in T_i$），$A$ 固定。给单位 kernel $e$ 和固定 $b>0$，仅保留实际事件

$$Y_i^e\subset Y_i\cap\{|P|\le A\delta,\ \partial_eP\ge b\},\qquad E_e=\bigcup_iY_i^e;\tag{3}$$

负号同理。同一纤维上的 $q(s)=P(z+se)$ 至多二次，故对任意 $s,s'$ 有精确恒等式

$$q(s')-q(s)=\frac{s'-s}{2}\,[q'(s')+q'(s)].$$

若两点同属 (3)，则 $|s'-s|\le2A\delta/b$。无需点集连通或知道其分支；每个同号集合的直径已足够。两号并集的总长度至多 $4A\delta/b$。定义

$$f_e(z)=\delta^{-1}\int_{\mathbb R}1_{E_e}(z+se)\,ds,\quad z\in e^\perp.$$

由 Fubini，$0\le f_e\le L:=4A/b$，$\int f_e=\delta^{-1}|E_e|$，于是

$$\|f_e\|_3^3\le L^2\delta^{-1}|E_e|.\tag{4}$$

必须用 $E_e$；若使用全部 $E$，其余物理 normal 分支可能令纤维长 $O(1)$，不能继续写 $f_e\le L$。事件可在一条轴不同时间选择不同 kernel；轴本身仍是原单位轴，不对其 marks 作端点或 clock 裁切。

## 4. 方向 cap 的精确几何接口及独立核验

原 contained line 条件是 $P(a)=0$、$(2Ha+l)\cdot v=0$、$v^THv=0$。当 $Hv\ne0$，选有限固定精度 $S^3$ kernel 网；对任意两单位 normal，总能从该网找到同时与二者内积绝对值 $\ge\kappa$ 的 $e$，$\kappa>0$ 绝对固定。两 normal 取实际物理 $\nabla P(p)$ 及 $Hv$。将两个符号分别分组后，物理 (3) 成立，且

$$|e\cdot Hv|\ge\kappa|Hv|.$$

对 $p\in T_i$，$\nabla P(p)\cdot v_i=O(\delta)$，而 $|e\cdot\nabla P(p)|\ge\kappa c$、$|\nabla P(p)|\le C$，故 $|\pi_ev_i|\ge c_1(c)>0$。这里只用相对 cone-normal，不付 Hessian 最小奇异值。

将 $w=v/|\pi_ev|=u+te$，$u\in S^2\subset e^\perp$。同一 cone-normal 符号的两个零点 $w,w'$ 满足

$$0=(Hw+Hw')\cdot[(u'-u)+(t'-t)e],\qquad
|t'-t|\le\kappa^{-1}|u'-u|.\tag{5}$$

因此 $u\mapsto v=w/|w|$ 在整个该符号集合上有统一 Lipschitz 逆。每个 projected $C\delta$ 帽的原方向直径 $O(\delta)$，可用固定数原 $C_0\delta$ 帽覆盖，总权 $\le C\alpha$；无需局部 root-stability、CAD 或方向距离奇集的下界。

当 $Hv=0$，原线条件给 $v\in V:=\ker H\cap l^\perp$。所有物理 normal $2Hx+l$ 属 $V^\perp$。只在 $V^\perp$ 选有限 kernel 网使物理导数下界成立，则 $\pi_e|_V$ 为等距，方向 cap 直接保留。因 $P$ 非零而有 regular 轴，$V^\perp\ne0$；若 $V=0$ 则无此类轴。这些网可依赖 $P$ 的子空间，但个数与常数只依赖维数和 $c$，不受 $P=P_\delta$ 退化影响。

上述选择均是有限可测实际 incidence 分区。它不声称同一轴所有点属于同一物理 chart，也不声称原投影是全曲面的全局微分同胚；(4)、(5) 已分别支付所需的纤维和原 cap。

## 5. 完整投影管道：端点、原权与三次 Jensen

现在固定一组 (3)，令 active 轴的 projected 单位方向为 $\omega_i$，并有 $|\pi_ev_i|\ge c_1$、任意 projected $C\delta$ 帽的原权和 $\le A_e\le C\alpha$。$\pi_eY_i^e$ 落在投影轴的 $O(\delta)$ 邻域，轴长在 $[c_1,1]$。对每个 $|\omega-\omega_i|\le c_2\delta$，该邻域可用固定数半径 $C_2\delta$、长度一、方向 $\omega$ 的三维圆柱覆盖。保持所有端点和全部 $Y_i^e$；不把旋转后的一个同长圆柱误称为完整覆盖，也不删除 $O(\delta)$ 的端点 shading。

投影 Fubini 给这些圆柱上 $f_e$ 的积分和至少 $\delta^{-1}|Y_i^e|$，故

$$K_{C_2\delta}f_e(\omega)\ge c\beta_i,\qquad \beta_i=|Y_i^e|/v_4(\delta).$$

每个小帽面积 $\asymp\delta^2$，其原权重叠 $\le CA_e$。乘 $w_i\beta_i^3$ 后求和、积分，再用 (2)、(4)，得

$$\delta^2\sum_iw_i\beta_i^3
\le CA_e\|K_{C_2\delta}f_e\|_3^3
\le C_\eta A_e\delta^{-3\eta}L^2\delta^{-1}|E_e|.$$

取 $\eta=\varepsilon/3$，固定半径倍数吸入常数：

$$|E_e|\ge c_{\varepsilon,c}\delta^{3+\varepsilon}\alpha^{-1}\sum_iw_i\beta_i^3.\tag{6}$$

任意重复方向／重合管均合法：权仍进入 angular cap，$E_e$ 只算一次 indicator，而帽积分按原权求和。无需等权化、权重 dyadic pigeonhole 或有限最小权。记 $W_e=\sum_{i\text{ active}}w_i$、$I_e=\sum_iw_i|Y_i^e|$，则精确 weighted Jensen 是

$$\sum_iw_i\beta_i^3\ge I_e^3/[v_4(\delta)^3W_e^2].\tag{7}$$

这里没有第二个 $\lambda$ heavy 提取损失；(2) 对整个函数和所有密度有效。

## 6. 合法 restriction／shading 与原总质量回传

上述有限分区数 $J=O_c(1)$，把每个实际 $Y_i$ 按首个可用 chart 分配，得 $\sum_rI_r=I$。选择 $I_r\ge I/J$，且 active $W_r\le W$。由 (7)

$$\sum_iw_i(|Y_i^r|/v_4)^3\ge I^3/(J^3v_4^3W^2)=J^{-3}\lambda^3W.$$

代入 (6) 即 (1)。因此只要求保留原 incidence 的固定比例；不要求 active 家族保留固定比例 $W$，更不要求每条管保留相同密度。一般 $I'\ge\theta I$、$W'\le W$ 时，原目标的 Jensen 因子至少保留 $\theta^3$，这是平均版本的合法闭包。

若原输入是逐管 $|Y_i|\ge\lambda_0v_4$，可每管选最重 chart 保至少 $\lambda_0/J$，再按 chart 分族；也可直接使用平均论证。两种闭包不能互相省略。任意进一步缩小 shadings 本身不保原 $\lambda$，必须记录 $I'$。非负权整体缩放不改 $W/\alpha$；零权可删。

固定短轴长度 $q_0>0$ 只改变覆盖常数，(6) 可直接作用其实际事件而单位原轴仍在。若改为 $q=\delta^a$（$\delta\ll q\le1$）并重新归一化短管，必须支付新尺度 $\delta/q$、四维 Jacobian $q^4$、更粗方向帽的 $\alpha'$ 及密度定义；仅当归一后的有界 chart／系数／regularity 常数也已统一支付时，按短管密度 $\lambda_{\rm short}$ 的体积尺度形式才为 $c\delta^{3+\varepsilon}q^{1-\varepsilon}\lambda_{\rm short}^3W/\alpha'$。不能把该固定幂费用或未核的新模型常数称作已付常数，当前证明完全不需它。

## 7. 超平面反向嵌入：先得完整 restricted weak 型

现假设 (Q3) 的全部固定 regular 常数量词成立；反向仅使用 $c_0=1/2$ 的子例，特别取 $P(x)=x_4$。先令可测 $F\subset\mathbb R^3$ 支持于一个固定单位 cube。给 $0<\lambda\le1$，从 $\{K_\delta1_F>\lambda\}$ 取极大 $\delta$ 分离方向 $\omega_1,\ldots,\omega_N$，逐个选取平均值 $>\lambda$ 的真实三维单位圆柱 $T_i^3$。每个轴距该 cube 有界，平移后均在原 $B(0,10)$，不需可测选择整个方向族。极大性给 level 的球面测度 $\le C\delta^2N$。

在 $x_4=0$ 嵌入这些轴，取四维半径 $2\delta$ 的管以及

$$Y_i^4=(F\cap T_i^3)\times[-\delta,\delta].$$

因距离平方相加，$Y_i^4$ 确实在该四维管内，包含原圆柱全部端点。$|Y_i^4|>2\pi\lambda\delta^3$；$\delta$ 分离方向在每个固定倍数帽中的数量 $O(1)$，故 $\alpha=O(1)$、$W=N$，平均密度 $\ge c\lambda$。并集体积 $\le2\delta|F|$。由 (Q3)，对任意 $\eta>0$

$$\sigma\{K_\delta1_F>\lambda\}\le C_\eta\delta^{-\eta}\lambda^{-3}|F|.\tag{8}$$

(8) 的所有中心、位置、$\lambda$ 常数统一。圆柱积分对中心和方向连续（indicator 的平移／旋转在 $L^{3/2}$ 连续），故 level 可测；选取只发生在有限 separated 集合上。这里只证明文献输入的反向蕴含，不宣本轮首先发现该传统 restricted→strong 思路。

## 8. restricted→strong 的完整小幂预算，不能略称“standard”

对支持于同一单位 cube 的 $f\ge0$，齐次归一 $\|f\|_3=1$。分出 $f_{\rm lo}=f1_{f\le\delta^2}$ 和 $f_{\rm hi}=f1_{f>\delta^{-2}}$。前者 $Kf_{\rm lo}\le\delta^2$；后者 $\int f_{\rm hi}\le\delta^4\int f^3=\delta^4$，故 $Kf_{\rm hi}\le C\delta^2$。中间仅 $J\le C\log(2/\delta)$ 个 dyadic 层 $F_j=\{2^j\le f<2^{j+1}\}$，并有 $\sum_j2^{3j}|F_j|\le1$。

若 $t\ge C\delta^2$ 且 $Kf>t$，由次可加性及 pigeonhole 存在 $j$ 使 $K1_{F_j}>ct/(J2^j)$。若右边超过一，该项为空；其余用 (8) 并对 $j$ 求和：

$$\sigma\{Kf>t\}\le C_\eta\delta^{-\eta}J^3t^{-3}.\tag{9}$$

Hölder 给所有 $t$ 的硬上界 $Kf\le C\delta^{-2/3}$。因此 layer cake 在 $[C\delta^2,C\delta^{-2/3}]$ 上仅多一个对数，低段贡献 $O(\delta^6)$：

$$\|K_\delta f\|_3^3\le C_\eta\delta^{-\eta}\log^4(2/\delta)+O(\delta^6).\tag{10}$$

给任意目标 $\varepsilon>0$，例如取 $\eta=\varepsilon$，吸收 $\log^4\le C_\varepsilon\delta^{-2\varepsilon}$，得 $\|K_\delta f\|_3\le C_\varepsilon\delta^{-\varepsilon}\|f\|_3$。

最后去掉 bounded support：把空间分为不交单位 cubes，$f_j=f1_{Q_j}$。每个长度一、半径 $\delta<1$ 圆柱仅交固定数 cubes，因此逐方向

$$K_\delta f\le C\sup_jK_\delta f_j,\qquad
\|K_\delta f\|_3^3\le C\sum_j\|K_\delta f_j\|_3^3.$$

对每个 cube 的平移版使用刚得的局部强型，右边 $\le C_\varepsilon\delta^{-3\varepsilon}\sum_j\|f_j\|_3^3$。所有级数非负，可用单调收敛；复值输入取绝对值即可。剩余 $\delta\ge\delta_0(\varepsilon)$ 用 $K_\delta f\le C\delta^{-2/3}\|f\|_3$ 直接吸入常数，补齐全部 $0<\delta<1$。故 (Q3) 的超平面部分已推出完整 (2)，没有未付强型 endpoint 或空间局部化。结合 §§3–6 的二次几何应用，在任意小幂损失意义上 (Q3) 与具名三维完整 maximal 输入双向等价；不另立结果 ID 或称独立新机制。

## 9. 与旧 frozen 命题的量词比较

本轮实际重读 `results/reviewed/DIR-003_weighted_direction_mass_input.md`、`results/reviewed/FSD-001_conditional_arbitrary_ambient_finite_seed.md`、`notes/40_multiscale/coupled_projections/R0015_mass_pruning_attempt.md`。DIR 的原全称仍要求每线至少 $\delta^{-1+\eta}$ marks；FSD 的 $\lambda^2$ 还带 $\lambda\ge\delta^{\eta(\varepsilon)}$ 和角 Frostman 输入。它们不在已付参数模数下自动给 (8) 的任意 $\lambda$ 三次幂，不能从 $\forall\varepsilon\exists\eta$ 偷换线性 $\eta$ 模数。CP↔PM 已在同一 coupled-projection 原模型、所有 admissible $P_j$ 上用合法删选证明正 gain 等价；本轮不以重新命名强制重开。

Q3 原方向满足 $v^THv=0$（线性情形还满足 $l\cdot v=0$）；这不是任意四维 separated 方向族的默认输入。现有旧 CP/PM 没有给原族嵌入一个固定 exact regular quadric、保原方向／shading 的映射；反向也不能把仅此模型的结论免费施于所有 coupled anchors。这里审计的是缺少已付桥，不声称证明抽象逻辑上的永不等价。

R50 的 full-smooth lift 分类给的是全参数保 clock 的存在／不可能与第一变分正规化；没有自动给物理 Jacobian、原角 cap、shading Fubini 或逆向维数增益。本稿没有用其免费降维，也不以二次曲面名义重新打开该 frozen 存在分类。真正的双向重复已在 §§7–8 明确定位为新具名三维 maximal 的应用闭包。

## 10. 独立反攻、结论及剩余边界

极不均匀权和重复管：只用原帽 upper 与 weighted Jensen，未偷逐管等密度。极小 $\lambda\ll\delta$：端点全覆盖、无删 caps／先 heavy 而多损一份密度。$P=P_\delta$ 接近 Hessian 退化：方向 (5) 只需相对 normal；$Hv=0$ 独立等距处理，没有最小非零特征值费用。物理不同叶片：每同号纤维直径由精确二次 secant 统一约束，先裁实际事件再作 $f_e$，不需整曲面单叶片。

在具名 (2) 下，本稿已完整支付 arbitrary average $\lambda$、原权／$\alpha$、有限事件分区、投影端点和均匀二次几何的模型应用。其正幂强度反向等价于 (2)，所以不注册新数学 ID／major。主稿的完整一般 quadric 联合证明仍须全文独立审查后统一归档；本稿不能代整篇 OpenAI3D 外部认证。

一般情形仍未包含的是：轴只落在任意 variety 的 $\delta$ 邻域而非 exact contained（§11 固定抛物柱子类另付）、degree 随尺度增长、梯度无统一下界、变化短 clock／异向归一、或一般高维原族的原质量提取。它们会改变方向 secant、纤维长度或原 $W/\alpha$；不能把 exact 模型重新命名为这些未付桥，也不能据本模型声称 n5 改进。长期 Goal 保持 active，本轮完成后关闭这一 exact 模型应用，不调 degree／regularity／密度门槛续轮。

## 11. 修订 spec §6：真正近 contained 的固定抛物柱，组数无损相加

此处额外假设固定 $P(x)=x_4-x_1^2$；每条原单位轴 $a_i+tv_i$（$|t|\le1/2$，$|v_i|=1$，$a_i$ 为中点）在 $B(0,10)$，且仅要求整轴包含于 $N_{C\delta}\{P=0\}$。保留全部原 $Y_i\subset N_\delta\ell_i$、$w_i,W,\alpha,I,\lambda$。不作 $O(\delta)$ exact snapping，不改原时钟，也不从某些 marks 位于邻域推出整轴条件。

**精确系数预算。** bounded geometry 与邻域假设给 $|P(a_i+tv_i)|\le A\delta$，$A$ 仅依赖固定邻域常数。展开

$$P(a+tv)=a_4-a_1^2+t(v_4-2a_1v_1)-t^2v_1^2.$$

在 $t=0,\pm1/2$ 计算，得到

$$|a_4-a_1^2|\le A\delta,\quad |v_4-2a_1v_1|\le2A\delta,\quad v_1^2\le8A\delta.\tag{11}$$

尤其 $|v_4|\le C\sqrt\delta$，足够小的 $\delta$ 下 $\ell_i'=|\pi v_i|\ge1/2$，其中 $\pi$ 丢掉 $x_4$。这些常数不依赖标签、密度或权。

**原空间分组和 overlap。** 令 $r=\sqrt\delta$，将中点 $a_{i,1}$ 分到不交半开 $r$-bins $B_j$，以其中点 $b_j$ 记中心。原标签恰分一组；定义 $W_j=\sum_{i\in j}w_i$、$I_j=\sum_{i\in j}w_i|Y_i|$、$E_j=\bigcup_{i\in j}Y_i$。有精确 $\sum_jW_j=W$、$\sum_jI_j=I$。由 (11)，整条轴的 $x_1$ 在 $a_{i,1}+[-Cr,Cr]$，所有端帽仅再添 $\delta\le r$。因此 $E_j$ 在 $B_j$ 的 $C r$ 扩大内，遂逐点

$$\sum_j1_{E_j}\le C1_E,\qquad \sum_j|E_j|\le C|E|.\tag{12}$$

这里没有假定 $Y_i$ 填满，也没有直接以 $O(r^{-1})$ 组数相乘。保持所有原事件，包括极小 $\lambda$ 时可集中的端帽。

**每组的真实角 cap。** 对 $i\in j$ 设 $u_i=\pi v_i/\ell_i'\in S^2$、$q_i=v_{i,4}/\ell_i'$。由 (11)、$|a_{i,1}-b_j|\le r$、$|u_{i,1}|\le Cr$，

$$q_i=2a_{i,1}u_{i,1}+O(\delta)=2b_ju_{i,1}+O(\delta).\tag{13}$$

同组两个 $u_i,u_k$ 若距不超过 $C_0\delta$，则由有界 $b_j$ 得 $|q_i-q_k|\le C\delta$。原方向为 $(u_i,q_i)/\sqrt{1+q_i^2}$，故原方向彼此距 $O(\delta)$。每组任一 projected 邻帽的原权至多 $C\alpha$，没有投影 $\delta^{-1/2}$ 重数费用。只有 $q(v)=O(\delta)$ 而不分 midpoint packet 时不能免费得到此结论；真正支付了 $r\,|u_1|=O(\delta)$。

**每组物理纤维和 M3。** 每个 $p\in E_j$ 仍有 $|p_4-p_1^2|\le A'\delta$。固定 $(p_1,p_2,p_3)$ 的 $x_4$ 纤维长度至多 $2A'\delta$。令 $f_j=\delta^{-1}\int1_{E_j}\,dx_4$，则 $0\le f_j\le2A'$、$\int f_j^3\le C\delta^{-1}|E_j|$。由 §5 的全部端点覆盖及原权邻帽立方积分，逐组有

$$|E_j|\ge c_\varepsilon\delta^{3+\varepsilon}\alpha^{-1}\frac{I_j^3}{\delta^9W_j^2}.\tag{14}$$

零权组忽略，$I_j=0$ 的项取零。所有常数统一于 $j$，即使组数随尺度增长，也不用在 source 定理中把 loss 除以组数。

**原平均质量无损合并。** Hölder 精确给

$$I=\sum_j(I_j/W_j^{2/3})W_j^{2/3}
\le\left(\sum_j I_j^3/W_j^2\right)^{1/3}W^{2/3}.$$

结合 (12)、(14) 和 $I=\lambda v_4(\delta)W$，得到

$$|E|\ge c_\varepsilon\delta^{3+\varepsilon}\lambda^3W/\alpha.\tag{15}$$

所以该固定 parabolic-cylinder 的 genuinely near-contained 子类，已在具名 M3 下完整保原方向、所有平均密度和权。式 (11) 容许 $|v_1|\asymp\sqrt\delta$ 的轴；它们与任何 exact-contained 方向相距 $\asymp\sqrt\delta$，本论证没有取消之前的 snapping 障碍。新支付的是 midpoint 空间 packet、(13) 的原角 cap 和 (12) 的有界 overlap；没有声称一般近 quadric 的统一分类／条件数，也没有声称 high-dimensional 原族已可提取此模型。按本轮范围不新立 ID／major，不继续用 degree／梯度／时钟小改反复开同应用。
