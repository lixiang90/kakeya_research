# R0007：全部plank上界与WP4反例的独立复核

日期：2026-10-16。审查人：`literature_frontier`。被审文本：`notes/50_counterexamples/R0007_weighted_plank_obstructions.md`。本次独立核验显式线族、QCAP的全部frame/center上界、离散化及满时间标记后的WP4矛盾。没有用survey对坏框的下界替代全部框上界。

结论：明示有界图内的加权WP4反例通过内部独立复核，未经外部同行评审。这是已知quadric障碍的具体有限尺度核算，不声称新型Kakeya反例或重大中间结果。

## 1. 显式族和一阶薄轴估计

对$s\in[1,2]$、$p,q$在小固定盒内，$b=(s,-sq-p/s,1/s)$、$u=(p,-pq,q)$确有$ty+xz\equiv1$。反向读$s=b_x,p=u_x,q=u_z$，所以不同参数格点不会被重复记成不同的同一条线。

任意单位空间向量$n$的最薄轴条件同时约束$F_b=n\cdot b$和$F_u=n\cdot u$到宽$O(w_1)$区间。若$|n_y|\ge1/4$，$|\partial_pF_b|=|n_y|/s$有统一下界；否则$\max(|n_x|,|n_z|)>2/3$，在扩大参数盒内$\partial_pF_u=n_x-n_yq$或$\partial_qF_u=n_z-n_yp$有统一下界。被选方向上函数都是一次式，故任意边长$Cr$参数cube内测度至多$Cw_1r^2$。这一步对任意frame和center成立。

## 2. 两种局部化均通过

最大的空间宽度$w_3$控制两个endpoint之差，从而控制完整$(b,u)$系数差；由上述线性逆读参数，所有参数落在一个$O(w_3)$ cube内。薄轴Fubini因此给$Cw_1w_3^2$。

投影到最长轴正交plane后，两短轴条件把其affine系数固定到$O(w_2)$。沿最长轴的未知affine函数$\zeta$满足

$$\|A\zeta^2+B\zeta+C\|_{\rm coeff}\le Cw_2,
\quad A=n_xn_z,$$

而参考$\zeta_0$精确使该二次多项式为0。大$|A|$时完成平方并用一次多项式乘积范数下界，得到至多两个$O(\sqrt{w_2})$系数团。

小$|A|$时，参考线上的法向导数

$$L_0(t)=n_x(1/s_0+q_0t)+n_yt+n_z(s_0+p_0t)$$

在$A=0$处不可能为零多项式：常数项先迫使剩余的$n_x$或$n_z$为0，再由单位向量条件得$n_y\ne0$。紧性给统一下界；选足够小固定$a_0$后，$A(\zeta+\zeta_0)+B$仍有统一范数下界。两式相减及乘积范数下界给$\zeta-\zeta_0=O(w_2)$，更强于所需平方根团。

这些团退回参数后至多两个$O(\sqrt{w_2})$ cubes，再用最薄轴Fubini给$Cw_1w_2$。与上一种局部化取小值，确得

$$\mu(\Omega(P))\le Cw_1\min(w_2,w_3^2).$$

最后$\min(1/w_3,w_3/w_2)\le w_2^{-1/2}\le\delta^{-1/2}$仅用$w_2\ge\delta$。没有遗漏相切或$A$近零的frame。

## 3. 离散化与权重

每个$\delta$格点旁取互不相交的小参数cubes。统一Lipschitz界把该cube的所有traces送入宽度各增$O(\delta)$的$P^+$；扩大参数盒上前述连续证明仍成立。因全部$w_j\ge\delta$，扩大宽度只变固定倍。因此

$$\#\{M_i\subset P\}\le C_{\rm cap}\delta^{-1/2}
\frac{w_1w_2w_3}{\delta^3}$$

对所有允许frame、affine center和尺度同时成立。取统一固定权$\omega_i=C_{\rm cap}^{-1}\delta^{1/2}$，即得工作命题WP4的$A=1$。该权重不随被测试框改变，也不需要概率抽样。

## 4. 量纲和量词

参数格点数$\asymp\delta^{-3}$。所有traces在$x\ge9/10$的quadric图$z=(1-ty)/x$上；有界Lipschitz图的四维访问cell数至多$C\delta^{-3}$。每条标满$D=\delta^{-1}$个time bins后，

$$\sum_i\omega_i\#J_i\gtrsim\delta^{-7/2},\qquad\#E\lesssim\delta^{-3}.$$

所以任意固定$\varepsilon<1/2$都会使WP4要求的比值上界失败。所有indices密度都是1，故任意事前选定的$\eta>0$均无助；不是调错$\varepsilon/\eta$顺序导致的反例。

族的空间斜率满足$u_y+u_xu_z=0$，只在真二次方向薄层内。故它严格否定无方向WP4，不提供所有四维方向，也不否定任何完整方向Kakeya维数命题。原稿$j=3$初始化的其他带方向来源版本仍需分别分析。
