# R0088：共同 null 映射、逐标签提升与真实质量审计

2026-10-18。B 独立施工稿；只检验 working spec 预先锁定的共同映射和逐标签 cone packet 两桥。ordinary 五维目标未完成，不登记新数学 ID、major 或新颖性。本文自证部分须由 root/A 独立审查；高级 restriction wholeproof 仍是具名输入，未经外部同行评审。

## 1. 实际读取、原对象与具名输入

实际全文读 `research/rounds/R0088_working_spec.md` 五节；新源为 Xiangyu Wang, *On Cone Restriction Estimates in Higher Dimensions*, [arXiv:2411.02961v8](https://arxiv.org/html/2411.02961v8)，版本日期 2026-09-30。实际读 HTML §1.1、§2.1 的完整陈述与解释，并对照本地 `literature/extracted/wang_2026_cone_restriction_2411_02961_v8.txt` PDF1–6 的相应原文，包含 Theorem 1.5、Proposition 1.7、wave-packet long/short directions。没有新独证其 §3–4 递归与高级 restriction wholeproof。

本轮用其六维 extension

\[
\mathcal Ef(X,S)=\int_{1\le |\xi|\le2}e^{i(X\cdot\xi+S|\xi|)}f(\xi)\,d\xi,
\qquad
\|\mathcal Ef\|_{L^p(B_L)}\le C_{p,q,\epsilon}L^\epsilon
\|f\|_2^{2/q}\|f\|_\infty^{1-2/q}. \tag{1}
\]

输入必须是原文 admissible tuple，特别是 \(2\le q\le p\)、\(2\le k\le4\)。这是 Prop.1.7 的 local estimate；原文 Theorem1.5 的 global estimate有相应严格端点条件，不把猜想或 broad bound 单独当 (1)。

原管为 \(T_i=N_\delta(a_i+[-1/2,1/2]v_i)\subset B_R\)，\(|v_i|=1\)，方向在原 projective angular metric 上 \(\delta\)-分离。有限方向定向后频率中心为 \(-v_i\)；取足小固定 angular bump，频率 supports 两两不交。记 \(N=\#\{i\}\le C\delta^{-4}\)、\(E=\bigcup_iY_i\)，原 \(Y_i\subset T_i\) 任意 Lebesgue 可测。实际 round-tube 体积

\[
V_\delta=\omega_4\delta^4+\omega_5\delta^5\asymp\delta^4,
\qquad I=\sum_i|Y_i|,\qquad \lambda=I/(NV_\delta).
\]

逐管密度下界蕴含同一平均下界，反向删选的成本在 §9 单独列明。

## 2. 共同 C1 映射的 Lorentz 障碍及精确量词

令 \(F:U\subset\mathbb R^5\to\mathbb R^{5,1}\) 为同一个 \(C^1\) 映射，\(J=\operatorname{diag}(I_5,-1)\)。假设对每 \(x\in U\)，存在球面中非空开方向集 \(V_x\)，使经过 \(x\) 且方向为 \(v\in V_x\) 的局部线段被 \(F\) 送入某条 cone-null 直线。允许沿像线非匀速甚至导数为零。则

\[
v^T(DF_x)^TJDF_xv=0\qquad(v\in V_x).
\]

该齐次二次多项式在开锥上为零，故恒为零；由极化

\[
(DF_x)^TJDF_x=0. \tag{2}
\]

因此 \(W=\operatorname{im}DF_x\) 是 Lorentz signature \((5,1)\) 的 totally isotropic 子空间。若 \((u,t)\in W\setminus\{0\}\)，则 \(|u|=|t|\)、\(t\ne0\)。对任意 \((z,s)\in W\)，有 \(u\cdot z=ts\)、\(|z|=|s|\)，Cauchy 等号给 \((z,s)=(s/t)(u,t)\)。故

\[
\operatorname{rank}DF_x\le1. \tag{3}
\]

所以 rank 至少二的共同 affine map 或共同 \(C^1\) immersion 不可能满足上述逐点开方向条件。证明实际只需 null 切向，不需额外用整条像线的 straightness。

这不排除对有限原 Kakeya labels 分别定义映射。恰好 \(F_i(x)=(x,(x-a_i)\cdot v_i)\) 是 rank5 immersion，且只把第 \(i\) 条方向送成 null；其 pullback 为 \(I_5-v_iv_i^T\)，并不恒零。也没有证明有限原线族已经在每一点供应开方向，或排除不光滑/按 label 变化的整个 cone 策略。

## 3. 逐标签阴影提升：端帽、支持与实际体积

固定 \(\delta\le\tau\le1\)，定义

\[
r=\delta^2/\tau\in[\delta^2,\delta],\quad
t_i(x)=(x-a_i)\cdot v_i,\quad
u_i(x)=x-a_i-t_i(x)v_i,
\]
\[
S_i=\{(x,s):x\in Y_i,\ |s-t_i(x)|\le c_r r\},\quad
Z=\bigcup_iS_i,\quad M=\sum_i1_{S_i}.
\]

原 round 端帽给 \(|u_i|\le\delta\)、\(|t_i|\le1/2+\delta\)；不删除端帽或把端点体积忽略。连续 shear \((x,h)\mapsto(x,t_i(x)+h)\) 的 Jacobian 为1，因此原 Lebesgue 阴影合法且

\[
|S_i|=2c_r r|Y_i|,\qquad \int M=2c_r rI. \tag{4}
\]

长、短方向分别为 \((v_i,1)\) 与 \((v_i,-1)\)，其余四方向来自 \(v_i^\perp\)。提升点相对中心 \((a_i,0)\) 是

\[
(t_iv_i+u_i,t_i+h),\qquad |h|\le c_rr;
\]

故各片落在固定倍长1、中宽 \(\delta\)、短宽 \(r\) 的真实 anisotropic packet 内。由于原 \(a_i\) 和 \(t_i\) 有界，

\[
Z\subset E\times[-C_R,C_R],\qquad |Z|\le C_R|E|. \tag{5}
\]

这里横向投影严格属于原 \(E\)，不是 \(N_\delta E\)。但一般不同 labels 的新增 clock 不一致；(4) 是各片体积，不能把 (5) 免费加强成 \(|Z|\lesssim r|E|\)。

## 4. 原方向分离、近满阴影仍不授统一 r 纤维：实体校准

取固定 \(0<a<1/4\)，\(\rho=\delta^a\)，在 \(S^4\) 的小固定开角 chart 中取 \(\delta\)-网 \(v_k\)，\(k\in\mathbb Z^4\) 的有限盒，\(N\asymp\delta^{-4}\)。chart bi-Lipschitz，且避开相反方向。令 \(M_0\ge C_0/\rho\) 为整数，把四个 residues \(k\bmod M_0\) 单射编码为 \(\operatorname{code}(k)\in\{0,\ldots,M_0^4-1\}\)。取固定足大的 \(K_0\)，令

\[
c_k=K_0\delta\operatorname{code}(k),\quad a_k=c_kv_k,\quad
Y_k=T_k\cap\{\rho\le |x|\le2\rho\}.
\]

因为 \(\max c_k\lesssim\delta\rho^{-4}=\delta^{1-4a}\to0\)，这些 annular marks 全处于原单位段内部。每 \(|Y_k|\asymp\rho\delta^4\)，故逐管 \(\lambda\asymp\rho\)；原并集 \(E\) 是该固定角 cone 中的厚 annulus，\(|E|\asymp\rho^5\)。下界来自 chart 网的角间距 \(\delta\ll\delta/\rho\)，能覆盖一个更小固定角 annulus。

若同一 \(x\) 同时属于 \(Y_k,Y_{k'}\)，则两方向距离 \(\lesssim\delta/\rho\)，所以 \(|k-k'|_\infty<C_0/\rho<M_0\)。不同 \(k,k'\) 的 residue tuple 因而不同，\(|c_k-c_{k'}|\ge K_0\delta\)。另一方面

\[
|(v_k-v_{k'})\cdot x|\lesssim\delta.
\]

故选 \(K_0\) 足大后，各 \(t_k(x)=v_k\cdot x-c_k\) 的 \(c_rr\)-邻区间逐点两两不交，对全部 \(r\le\delta\) 均成立。于是

\[
|Z|=\sum_k|S_k|\asymp r\rho,
\qquad \frac{|Z|}{r|E|}\asymp\rho^{-4}\longrightarrow\infty. \tag{6}
\]

这保留严格原方向分离、原 whole unit axes、可测真实阴影和逐管 \(\lambda\asymp\delta^a\)。\(a\) 可任意小但固定。它仅否定无代价的共同 \(r\)-clock 纤维，不是 ordinary 反例，也不否定其他选取 lift 的方法。这里 \(|E|\asymp\rho^5\) 当然不违反 nearfull Kakeya 所需的小损失估计。

## 5. 手工频率包与去 carrier 相位：幅度不靠口头 packet 对应

取中心半径 \(\rho_0=3/2\)，每个 \(v_i\) 配正交基 \(e_{ij}\in v_i^\perp\)，写

\[
\xi=\varrho\big(-v_i\sqrt{1-|z|^2}+\sum_{j=1}^4z_je_{ij}\big),
\quad |z|\le c_a\delta,\quad |\varrho-\rho_0|\le c_b\tau.
\]

用非负光滑 bump \(\chi_i\le1\) 支于上述 sector，中心半大小区域等于1；其频率测度

\[
V_f\asymp\delta^4\tau.
\]

选 \(c_a\) 小使不同 labels 的 sectors 不交，令

\[
f_i(\xi)=e^{-i\delta^{-2}a_i\cdot\xi}\chi_i(\xi).
\]

在 \((x,s)\in S_i\)，\(x-a_i=t_iv_i+u_i\)、\(s=t_i+h\)。归一坐标为 \((X,S)=\delta^{-2}(x,s)\)。extension phase减去与积分变量无关的 carrier \(\delta^{-2}\rho_0h\) 后为

\[
\delta^{-2}\big[(\varrho-\rho_0)h+
\varrho t_i(1-\sqrt{1-|z|^2})+
\varrho u_i\cdot\sum_jz_je_{ij}\big].
\]

其绝对值至多 \(C(c_bc_r+c_a^2+c_a)\)；用 \(r\tau=\delta^2\) 及原端帽范围，固定小参数使之小于 \(\pi/10\)。故积分实部在去相位后为正，并有

\[
|\mathcal Ef_i(\delta^{-2}x,\delta^{-2}s)|\ge c\delta^4\tau\quad((x,s)\in S_i). \tag{7}
\]

不是要求原大相位本身 \(O(1)\)，也没有用邻域外包替代原阴影。此直接 bump 构造解释了原文 §2.1 unit-radial packet 在 \(L=\delta^{-2}\) 时的 long1/mid\(\delta\)/short\(\delta^2\)；减 radial bandwidth 至 \(\tau\) 只把 short 变成 \(\delta^2/\tau\)。

## 6. Random signs 的实际 L∞、L2 和六维缩放

令 \(f_\varepsilon=\sum_i\varepsilon_if_i\)，各 \(\varepsilon_i\) 为独立 Rademacher 符号。频率 supports 不交，故对每组符号均有

\[
\|f_\varepsilon\|_\infty\le1,
\qquad \|f_\varepsilon\|_2^2\asymp N\delta^4\tau. \tag{8}
\]

所有 \(\delta^{-2}Z\) 都位于半径 \(C_R\delta^{-2}\) 球内。Khintchine、(7)、(1) 与六维 Jacobian \(\delta^{12}\) 给

\[
(\delta^4\tau)^p\int M^{p/2}
\lesssim\mathbb E_\varepsilon\int_{\delta^2B_{C_R\delta^{-2}}}
|\mathcal Ef_\varepsilon(\delta^{-2}x,\delta^{-2}s)|^p\,dx\,ds
\lesssim\delta^{12-\omega}(N\delta^4\tau)^{p/q}. \tag{9}
\]

这里 \(\omega>0\) 可任意小，先在 (1) 取足小 \(\epsilon\)；常数可随 \(p,q,\omega,R\) 变化。因此

\[
\int M^{p/2}\lesssim
\delta^{12-4p+4p/q-\omega}\tau^{-p+p/q}N^{p/q}. \tag{10}
\]

这一步不是把 random signs 后的 \(L^\infty\) 当空间函数上界；(8) 是原频率函数的实际上界，靠原 angular 分离成立。非饱和 \(N\) 也原样保留。

## 7. Hölder 回传、一般 N 与饱和指数独算

设 \(p>2\)。由 (4)、\(I=\lambda NV_\delta\)、\(r=\delta^2/\tau\)，

\[
\int M\asymp\lambda N\delta^6/\tau,
\qquad
\int M^{p/2}\ge(\int M)^{p/2}|Z|^{1-p/2}.
\]

结合 (5)、(10)，得到本直接桥的真实有限估计

\[
|E|\gtrsim
\lambda^{p/(p-2)}
N^{p(1-2/q)/(p-2)}
\delta^{(14p-24-8p/q)/(p-2)+\nu}
\tau^{p(1-2/q)/(p-2)}, \tag{11}
\]

其中任意 \(\nu>0\) 可由源的 \(\omega\) 足小实现。等价记

\[
A=\frac p{p-2},\quad b=\frac{p(1-2/q)}{p-2}\in[0,1],\quad
\beta=\frac{10p-24}{p-2},
\]
\[
\boxed{|E|\gtrsim\lambda^A\delta^{\beta+\nu}(N\delta^4)^b\tau^b.} \tag{12}
\]

饱和 \(N\asymp\delta^{-4}\) 才可删去 \((N\delta^4)^b\)。当 \(q=2\) 时 \(b=0\)，当 \(q=p\) 时 \(b=1\)；这些是实际输入归一后的结果，不能先免费设 \(L^2\) 或 \(L^\infty\) 为任意方便的常数。原 \(r\)-质量在 (4) 已进入，随后只用了 \(|Z|\lesssim|E|\)，没有漏乘或再多乘一次 \(r\)。

## 8. 必要 p、当前 v8 范围与两个 radial 端点

径向非负光滑函数 \(f\)，支于固定 annulus 内，给出必要的 light-shell 校准。在 \(S\approx |X|\gg1\)、\(|S-|X||\le c\) 上，对四维 angular sphere 的 stationary phase 主项大小 \(\asymp |X|^{-2}\)；取小固定 shell 厚度后径向主项不为零。该 shell 每 radial 长度的体积 \(\asymp R^4\,dR\)，故

\[
\int_{B_L}|\mathcal Ef|^p\gtrsim\int_1^{cL}R^{4-2p}\,dR.
\]

若 local estimate 允许每个任意小 \(L^\epsilon\) 损失，则必有 \(p\ge5/2\)。这也是新源 Conj1.1 的必要端点；未把猜想的充分性当作已证。

另一个 sector/Knapp 检验：angular宽 \(\delta\)、radial宽1 时频率量 \(\delta^4\)，物理 packet 体积 \(\delta^{-6}\)，振幅 \(\delta^4\)。故 (1) 必需 \(6/p\le4(1-1/q)\)，即源的 \(q'\le(2/3)p\) 条件。它不提供小于上述 constant-function 端点的漏洞。

\(\beta(p)\) 单调递增，且 \(\beta(5/2)=2\)。要从本式得到目标 \(\delta^{1-\sigma}\)，即使 \(\lambda=1,N\asymp\delta^{-4},\tau=1\)，也要求 \(\beta<1\)，等价 \(p<22/9<5/2\)，与必要测试冲突。当前 v8 更不达到这个区间。例如 \(n=6,k=3,q=p\) 的 broad 阈值为 \(p(6,3)=1178/463\)，给 \(\beta=167/63>2\)；只将其作为一个合法 tuple 的算术对照，不另做参数优化路线。

由于 \(b\ge0\)，\(\tau=1\) 给本式最大的 lower bound；\(\tau=\delta\) 反而多 \(\delta^b\) 损失。任意 \(\tau\in[\delta,1]\)、稀疏 \(N\delta^4\lesssim1\) 和 \(\lambda\le1\) 均不能弥补指数。nearfull \(\lambda\ge\delta^\eta\) 仅再付 \(A\eta\)，不能把2降为小于1。

## 9. 原 restriction/shading、平均闭包与重复方向边界

(11)–(12) 仅通过总 \(I\) 使用阴影，故对原任意平均密度 \(\lambda\) 直接成立，无需先把全部 labels 声称为逐管重管，也不损 \(\lambda\) 倍 label 数。若外部只调用一个逐管结论，删去 \(|Y_i|<\lambda V_\delta/2\) 后保 \(I_H\ge I/2\)、\(N_H\ge\lambda N/2\)，但一般 \(N_H\not\gtrsim N\)；把 (12) 用在该子族会多付至少可见的 \(\lambda^b\)，不可藏入 subpower 常数。

任意原 label restriction 与任意更小 measurable shading 都保持几何输入，公式以其实际 \(N'\)、\(I'\)、\(\lambda'\) 重新计算；小 \(N'\) 不补成饱和。不从上述 restriction 自动推出任何旧 CP/PM uniform saving，也不重命名 frozen 的正幂等价命题。

若方向可重复，(8) 的频率 supports 不再不交，原 \(L^\infty\le1\) 不能保留。重复完全相同管和阴影任意多次显然不改变 \(E\)，所以不能把重复 label 数免费代进 \(N^b\)。原 angular cap 原则或正确频率 \(L^\infty\) 费用必须另付。本文主式保留 spec 的原 \(\delta\)-分离，不借一个重复方向弱例反驳已满足分离的主桥。

所有推导针对完整实际 Yi；既没有用 full-tube restriction 定理替代任意阴影，也没有从平均密度推每对标签的交叠或 common clock。§4 专门显示后者即使逐管近满也不免费。

## 10. 停止范围与待独立互审对象

本文自证了共同 \(C^1\) open-direction null-map 的 rank 障碍；构造真实 per-label lift 和 phase bump；从具名 Prop1.7 得到 (11)–(12)，并给原方向分离的 free-\(r\)-fiber 实体反攻。两桥均未给 ordinary R5 的固定 saving，按 spec 停止，不续调 \(\tau/q/k\)、附共同纤维假设或转到 source 的其他 proper 模型。

这不是新 Kakeya 反例，不否定整个 cone restriction 策略，也不声称任意按 label 变换都失败。下一独立审查将实际全文读 root/A 对源归一、packet 和指数的独立稿，再记录真实交叉范围；当前不预认证尚未写成的稿、formal、元数据或同步。
