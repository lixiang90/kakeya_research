# R0050：非线性 coherent lift 的第一变分与旧适用范围纠正

2026-10-17，A。任务为原时钟、一般 smooth 空间 submersion 的完整 (1,0)-lift，固定 B=diag(1,2)。**指定 class 的答案是否定。关键是将原全时恒等式在一个固定参数点求第一变分，而不是证明原 π 本身为空间仿射。** 下述论证是 R12 已有代数证明的适用范围补全，不新立结果 ID，不声称 Kakeya 维数新界、重大性或文献优先权；须独立逐步审查，未经外部同行评审。

## 1. 固定入口、原命题和 source 范围

已读本轮 working_spec、GOAL/STATE 和 R49 下一任务；实际重读 R12 的 A/root/B 三份完整证明。仍保一般/高维 Kakeya 长期 Goal，不将这一机制排除误写为一般五维证明。

真正来源是 Nadjimzadah，*Lifting curved Kakeya sets to linear Kakeya sets*，arXiv2609.06299v1；R49 官方核只有2026-09-05的v1。本文实读已存 PDF4–9 的 Remark1.5、Def2.1、完整 Prop2.2 证明及 Prop2.5(i) 构造；对应 extracted `split('\n')` 一基 lines195–223、277–445。2511.10918/GAFA00750-4 是另篇 Bourgain-condition 文，不能混同。

Def2.1（PDF6）允许一般 smooth time-preserving submersion

\[
 \pi(z,t)=(\pi_t(z),t),\qquad
 \pi_t:\mathbb R^{m+s}\longrightarrow\mathbb R^m,
\]

定义在含全部所选线段的开集 Ω 上；a=a(y,w,ρ)，Θ=Θ(y,ρ) 不依赖 w。整个共同参数域上每个 ρ 的 line 都须投到同一 γy,w，且 Θ 的 rank 是原定义的一部分，不能改为只看一个 selector w(y) 或 ρ(y,w)。

本任务 m=2、s=1，y,w∈R²、ρ∈R，各域有内点，时间 I 含0且非退化。要求

\[
 \pi_t\big(a(y,w,\rho)+t\Theta(y,\rho)\big)
   =w+F(t)y,\qquad F(t)=tI_m+t^2B,
 \tag{1}
\]

对所有参数、所有 t∈I 成立，rank Dzπt=m，rank D(y,ρ)Θ=m+s。没有预设 π 或 a,Θ 对参数线性。

## 2. 核心第一变分：同一条基线、同一个矩阵

固定一个内部参数点 P=(y*,w*,ρ*)，其方向 rank 满足题设。定义真实 lifted 基线

\[
 z_P(t)=a(P)+t\Theta(P),\qquad
 T_P(t)=D_z\pi_t(z_P(t)).
 \tag{2}
\]

T_P 是沿**同一条**原线读取的矩阵函数；允许它任意依 t 变化。π 可以在空间上真正非线性。所有下述参数导数均在这个固定 P 取值，所以它们是与 t 无关的数值矩阵：

\[
 W=\partial_w a(P),\quad U=\partial_y a(P),\quad
 V=\partial_y\Theta(P),\quad
 R=\partial_\rho a(P),\quad S=\partial_\rho\Theta(P).
\]

对原(1)求 w、y、ρ 导数，仅用 chain rule，得到对**全部 t∈I**同时成立的三个恒等式：

\[
 T_P(t)W=I_m,\qquad
 T_P(t)(U+tV)=F(t),\qquad
 T_P(t)(R+tS)=0.
 \tag{3}
\]

第一式用到 Θw=0。没有遗漏 π 的 Hessian：这里只求一次参数导数，πt 没有独立的 y,w,ρ 参数。非线性空间微分已经完整包含于 T_P(t)，同一 P 的三种导数使用的正是同一个 T_P(t)。

**这是 R12 scope 的纠正。** 旧稿称“非线性 π 的空间微分随基点改变，所以旧共同矩阵论证不适用”。该判断过强：跨不同参数点的矩阵确实不同，但 R12 的必要性证明只在一个 P 上使用(3)，从未要求跨 P 共用 T。因而原空间 affine 假设不是该必要性推导所需。不能将旧范围陈述当作另一个已证反向障碍。

## 3. 第一变分本身是一套真正的全时 affine lift

令新参数 u=(u_y,u_w,u_ρ)，定义

\[
 a_{\rm lin}(u)=D a(P)u,
 \qquad
 \Theta_{\rm lin}(u_y,u_\rho)
       =D_{(y,\rho)}\Theta(P)(u_y,u_\rho),
 \qquad
 \pi_{{\rm lin},t}(z)=T_P(t)z.
 \tag{4}
\]

由于目标 w+F(t)y 对原参数本身是 affine，(3)的线性组合直接给

\[
 \pi_{{\rm lin},t}
   (a_{\rm lin}(u)+t\Theta_{\rm lin}(u_y,u_\rho))
       =u_w+F(t)u_y
 \tag{5}
\]

对所有新 u、所有原 t 成立。T_P W=I 保证 πlin 是 submersion；Θlin 的 rank 恰为原 P 处的 rank。新小参数 balls 与整段时间均可放在 `R^(m+s)×I` 的开邻域里，满足真正定义的域要求。

(5)不是只到有限阶的 t-jet 匹配，也没有声称原 nonlinear π 等于 πlin。它是另一套 exact affine model：先对每个 t 的原恒等式求参数导数，再线性组合，故误差恒为0。无需解析性、Taylor remainder 控制或将非线性坐标强行用于原 straight lines。

由此对参数 affine 的本目标族，任何原 nonlinear lift 都产生同 codimension、同方向 rank 的 affine lift。相反 affine 本来是 smooth 类的子类。因此两种 class 的**存在性**在本问题上相同；不是两种投影函数本体相同。

## 4. 更直接的同轮推论：任意 codimension 都有 rank B≤s

这是 root 独立提出、A 逐式独核的自然推论；它无需 ρ/full Θ rank，避免将本次结论夸成新的参数方向。

由(3)的 W 共同右逆，rank W=m。选 m+s 维空间的一组**常数**补基，使线性坐标下

\[
 T_P(t)=[I_m\ \ H(t)],\quad
 U=\begin{bmatrix}C\\R_0\end{bmatrix},\quad
 V=\begin{bmatrix}D\\L\end{bmatrix},
\]

其中 H 为 m×s，R0,L 为 s×m；C,D,R0,L 全是固定矩阵。于是

\[
 P(t):=t^2B+t(I_m-D)-C=H(t)(R_0+tL).
 \tag{6}
\]

右边每个 t 的 rank≤s。若 s<m，任一(s+1)阶 minor 的左边是一个标量多项式，且在非退化 I 上恒为0，因而作为多项式恒为0。其最高次 `t^(2(s+1))` 系数就是对应 B-minor，所以 B 的所有(s+1)-minors 都为0，得到

\[
 \boxed{\operatorname{rank}B\le s.}
 \tag{7}
\]

s≥m 时(7)本来平凡。没有把 H 延拓到无穷，也没有让 t→∞：比较的是已在开区间恒零的**左边多项式 minor**的系数，H 本身只需在 I 有定义。

因此 B=diag(1,2) 的 rank2 迫 s≥2，整个 nonlinear s=1 类不可能，甚至无须额外使用方向满秩来排除。source Prop2.5(i) 恰构造 s=rankB、ν=rankB−rankB² 的 lift，故在保原时钟、全开 w、Θw=0 的这一精确定义内，允许方向 loss 时的最小 codimension 为 rankB。对本 B，它给真正 (2,0)-lift，未与源构造矛盾。

## 5. codimension-one 的完整方向 rank：旧判别仍适用

为完整核题设的(1,0)而非只有 codimension，重写旧必要充分判别。设 s=1、B≠0，在(3)的同一 P 固定导数；选常数基使 W 是前 m 个坐标，且最后基向量属于 ker T_P(0)，得到 T_P(t)=[I_m,h(t)]、h(0)=0。由 t=0 的 y、ρ 恒等式，记

\[
 U=\begin{bmatrix}0\\r\end{bmatrix},\quad
 V=\begin{bmatrix}D\\\ell\end{bmatrix},\quad
 R=\begin{bmatrix}0\\u\end{bmatrix},\quad
 S=\begin{bmatrix}q\\v\end{bmatrix}.
\]

r,ℓ 是行向量，u,v 是 scalar，q 是 m 维列。恒等式成为

\[
 tD+h(t)(r+t\ell)=tI_m+t^2B,
 \qquad t q+h(t)(u+t v)=0.
 \tag{8}
\]

`u+tv`不能是零多项式，否则第二式给 q=0，S=0，与方向 Jacobian 的 ρ 列非零矛盾。将第一式乘 u+tv，用第二式代换，得到 polynomial identity

\[
 (u+tv)(tI_m+t^2B)
    =(u+tv)tD-tq(r+t\ell).
 \tag{9}
\]

比较 t³ 得 vB=0；B≠0 迫 v=0，再有 u≠0。至此才可除以非零常数 u；没有遗漏时间分母零点。第二式给 h(t)=−tq/u，第一式给

\[
 D=I_m+qr/u,\qquad B=-q\ell/u.
 \tag{10}
\]

方向 Jacobian 在此常坐标下是

\[
 J_\Theta=\begin{bmatrix}I_m+qr/u&q\\\ell&0\end{bmatrix}.
\]

其前 m 列分别减去最后一列的 r/u 倍，得到 `[[I,q],[ℓ,0]]`，所以

\[
 \det J_\Theta=-\ell q=u\,\operatorname{tr}B.
 \tag{11}
\]

满秩迫 trB≠0。(10)又给 rankB=1；对 rank-one B，有 B²=(trB)B，所以条件等价于 rankB=rankB²=1。

充分性完全由旧/source 构造支付：B=0 时 πt(x,z)=x，a=(w,0)，Θ=(y,ρ)，方向 Jacobian=I；B=kℓ、ℓk≠0 时 πt(x,z)=x+tkz，a=(w,ρ)，Θ=(y−kρ,ℓy)，投影为 w+ty+t²By，det DΘ=ℓk≠0。

故原 smooth 非线性 class 的同一判别是

\[
 \boxed{B=0\quad\text{或}\quad
    \operatorname{rank}B=\operatorname{rank}B^2=1.}
 \tag{12}
\]

这只是 R12 必要性证明经真实第一变分后的完整范围；不是再开 rank-one 分类轮次。

## 6. 真非线性合法例：不能声称原 π 逼成 affine

B 独立给出以下两例，A 已逐项展开核验；它们防止将存在性线性化错误升级为原投影函数 rigidity。

**B=0。** 在 |t|<1/2 取

\[
 \pi_t(z)=\left(z_1+\frac{z_3^2}{1+t},z_2\right),\quad
 a=(w_1-\rho^2,w_2,\rho),\quad
 \Theta=(y_1-\rho^2,y_2,\rho).
 \tag{13}
\]

z3(t)=ρ(1+t)，其平方项抵消 z1 中的 −ρ²(1+t)，恰投影为 w+ty。Dzπt 对 z1,z2 的两列为 I2；方向 Jacobian 是上三角且 determinant1。πt 的空间 Hessian 非零，确是真 nonlinear example。

**B=diag(1,0)。** 取 y1 近0，k(y1)=(-1+sqrt(1+4y1))/2，即 k+k²=y1、(1+2k)k′=1。定义

\[
 \pi_t(z)=(z_1+t z_3+z_3^2,z_2),\quad
 a=(w_1-\rho^2,w_2,\rho),\quad
 \Theta=(y_1-\rho(1+2k),y_2,k).
 \tag{14}
\]

代入 z3=ρ+tk，tρ 和 tρk 交叉项全部消去，得到 `(w1+ty1+t²(k+k²),w2+ty2)`。Dzπt 仍由前两列给 rank2，det DΘ=(1+2k)k′=1。所有参数可取共同小开 balls，π 定义在含全部相应线段的开集，故不是逐点 jet 或 selector 例。

## 7. 原 Prop2.2 的应用方向和必要 buffer

这里的 no-go 本身不使用任何 Kakeya 输入。为了不把它倒读为高维进展，实际核 Prop2.2（PDF6–9，lines293–417）如下：

1. 对一个 X-Kakeya 集 K，可逐 y 任取 w(y)；lift 的全 ρ-coherence 保所有这些 lifted lines 都包含于 `Ktilde=π^(-1)(K)∩Ω0`。没有要求 selector 连续或可测才得几何包含。
2. 先将全部参数域取 compact 子域；所有线段的 image 是 compact，Ω open，故可选 Ω0 为**有正 buffer**的 compact 邻域。submersion 的有限坐标图给 Ktilde 的 Hausdorff 上界 dimHK+s。product 上界可直接用 K 的 balls 盖与每条 s 维 bounded fiber 的 r 网给出，不需任意纤维 Hausdorff 维数自动相加的错误定理。
3. Θ 满秩时其方向 image 含 open patch；有 lossν 时先取 coordinate projection保其 rank，再得到 R^(n+s−ν) 中 open patch directions。固定线长与有限 rotations/dilation 送 ordinary Kakeya，故是 `dKak(X)≥dlin(n+s−ν)−s` 的 forward 方向。
4. maximal 部分通过 compact submersion charts 的 coarea 和 uniform fiber-ball lower 比较 tubes；Ω0 应包含上述 buffer 才能在端点附近作(3.10)。ν0 时 Θ 为 compact 参数域上的局部 diffeomorphism，有限 cover 支付 image multiplicity，不能无证假它全局单射。有限 charts、常数倍 tube 宽度和 fiber measure upper 都是固定费用。

因此即使某 (1,0)-lift 存在，也只是用 R4 直线输入导出某 R3 曲线族结论。当前 B 的排除不能逆向证明 R5，也不否 source 原 (2,0)-lift 或改时钟的 Remark1.5。

## 8. 全 class 的潜在逃逸逐项核

* **有限 time jets。** 本文从原每个 t 恒等式求参数导数，(3)/(5)对整段 I exact；没有以有限个 jets 宣称存在原 lift。
* **π 只 smooth、非解析。** 多项式比较只用于(6)/(9)左边的真实多项式；不要求 T/H 或 π 解析。
* **不同基线/右逆。** 固定 P 后不再变更它。W=aw(P) 对全部 t 固定，三种参数导数使用同一个 TP(t)；不能把只给某个 t 的 arbitrary right inverse 当此 W。
* **ruling 锚点退化。** B≠0 时(9)强迫 v=0、u≠0；B0 合法例可以 aρ=0，不被错误排除。
* **Θ 依赖 w。** 若放开，第一式变为 TP(t)(aw+tΘw)=I，不再有本证的固定共同右逆；不在本文范围。
* **只选 w(y) 或 ρ(y,w)。** 没有开 w/ρ 域就不能按那些变量求导；不在本任务或 Def2.1 的全 coherence 量词内。
* **非线性坐标拉直 π。** 本文没有这样做；它会弯原线的旧警告仍对，但不妨碍沿固定基线求微分。
* **改 clock。** 对 B=bI 可用 τ=t+bt² 把曲线变直线，正是 source Remark1.5；它改变题设，不能绕过此保 t 的 rank bound，也未被本文反驳。

## 9. 一手比对和旧 scope 的更正责任

在已读 primary Def2.1/Prop2.2/Prop2.5(i)/Remark1.5 中，明确写的是一般 smooth projection 定义、forward 维数与 maximal 推论、s=rankB 的构造及改时钟例外；未在这些段落读到“保时钟任意 smooth lift 必有 s≥rankB”的必要性声明。这里的最小 codimension 指的是完整精确定义内的几何存在性，不是 source Theorem1.3 所称曲线 Kakeya 集的最小 Hausdorff 维数，两者不能混用。

本轮三条有界检索仅比对 exact necessary/minimal-codimension/first-variation 术语，没有将二手或机器 review 当证明输入；有限未命中不认证新颖。证明只由上述 chain rule 和旧代数给出，按 root 决定更新既有 LIFT005 的 scope，不新立 ID 或将其称重大新 rigidity。

R12 三稿中“空间 affine 是必要的 scope”“不能覆盖一般 nonlinear projection”的旧限制，以及 R49 next 以此作为严格未覆盖 class 的判断，都应由 root 加更正说明。事实是：函数 class 确实更大，(13)/(14)也展示真非线性成员；但**对此参数 affine 目标族的存在性，旧第一变分代数已经给出同一结论**。不能保留旧过度保守边界再额外注册一次相同代数。

## 10. 本轮结论与停止

指定 B=diag(1,2) 的整个 smooth time-preserving coherent (1,0)-lift class 已排除；任意 s 的同一 variation 系统更给 rankB≤s，source 的 rankB 构造达 codimension 下界。完整 codimension-one 方向 rank 判别仍是(12)。这些是已有论证适用范围的补全，必须以独审和 scope 更正归档，不提升到 ordinary Kakeya 维数或重大结果。

本轮已完成可检验任务，应停止此窄类，不再续 Hessian/Taylor 阶数、改时钟或弱 selector 参数轮。长期高维/一般 Kakeya Goal active；下一唯一机制由 macro 另选。A 仅编辑本分配文件及后续指定 review，不操作 Git。
