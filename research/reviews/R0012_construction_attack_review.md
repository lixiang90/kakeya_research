# R0012：非标准 affine-lift 构造攻击稿的独立审查

日期：2026-10-17。审查者：audit_four_dimensional。被审稿：`notes/20_dimension_lifting/curved_lifting/R0012_construction_attack.md`。重点为任意 \(c(t)\)、\(t=0\) 与分母退化、完整光滑类，以及 root 提出的自然 rank-one 必要充分补充。未编辑被审稿，也未展开新的分类任务。

**结论：通过。** 主 \(B=\operatorname{diag}(1,2)\) 的不可能证明覆盖本轮指定的任意光滑空间仿射、保留原时钟类。补充分类

\[
 B=0\quad\text{或}\quad
 \operatorname{rank}B=\operatorname{rank}B^2=1
\]

在同一 \(2\times2\)、codimension-one、满方向秩类中也成立。本文独立核对其 kernel／局部有理正规形证明；我的另稿采用无除法的系数消元，两条证明不同但结论兼容。均不涉及一般 nonlinear spatial submersion 或 nonlinear time change，不产生 Kakeya 维数结论。

## 1. 共同右逆与 T(0) 正规化均由原 identity 推出

固定一个 parameter interior point \(P\)。由于 \(\Theta\) 不依赖 \(w\)，对全时间投影恒等式作 \(w\) 微分确给

\[
 T(t)M=I_2,\qquad M=\partial_w a(P).
\]

\(M\) 是一个固定 rank2 矩阵，不能按不同时间另选。选 \(0\ne k_0\in\ker T(0)\) 后，\(S=[M,k_0]\) 可逆：对 \(Mv+rk_0=0\) 左乘 \(T(0)\) 即得 \(v=0\)，继而 \(r=0\)。常数坐标变化因此严格给 \(T(t)=[I_2,g(t)]\)、\(g(0)=0\)。

该变化保留 \(\Theta\) 对 \(w\) 的独立性、direction rank、coherent 参数恒等式和原 time coordinate。没有以 rank \(T=2\) 单独冒充共同右逆，也没有预设 \(g(t)=tk\)。

## 2. c(t) 未被无权设零

在 \(t=0\)，正规化后的恒等式直接给全参数域上的

\[
 a_{12}(y,w,\rho)=w-c(0).
\]

因此其 \(y,\rho\) 导数确为零。此后 \(c(t)\) 在 \(y,\rho,w\) 导数中都消失；证明不需要设 \(c\equiv0\)，也未把其时间变化编码成依赖 \(y\) 的补偿。

第三分量 \(a_3\) 仍可任意光滑、非线性。所有导数只在同一个 parameter point 取值，因此未把原参数函数错误地限制为 affine。

## 3. h=0、除 t 与局部分母均无遗漏

记 \(h=\partial_\rho a_3\)、\(b=\partial_\rho\Theta_3\)、\(r_\rho=\partial_\rho\Theta_{12}\)、\(k=g'(0)\)。coherent ruling 的必要关系为

\[
 (h+tb)g(t)+tr_\rho=0.
\]

在零点取一次时间导数得到 \(r_\rho=-hk\)，使用了 \(g(0)=0\) 且全部函数 smooth，故合法。

若 \(h=0\)，则 \(r_\rho=0\)。direction Jacobian 满秩使其 \(\rho\) 列非零，所以 \(b\ne0\)。由 \(tb\,g(t)=0\)，先在所有非零 \(t\) 得 \(g=0\)，再由连续性补零点。此时 \(y\) identity 是 \(tD=tI_2+t^2B\)，在开区间上迫 \(B=0\)。故当 \(B\ne0\) 时证明先排除 \(h=0\)，才除以 \(h\)。

令 \(\beta=b/h\)。因 \(1+\beta t\) 在零点为1，可在一个含0小区间合法写

\[
 g(t)=\frac{t}{1+\beta t}k.
\]

若 \(k=0\)，同一局部 identity 仍迫 \(B=0\)。所以主情形 \(k\ne0\)。rank2 矛盾仅需该小时间区间；原题在整个 \(I\) 成立，当然也必须在小区间成立。远处可能的分母零点不能规避局部矛盾。

选择非零 row \(n\) 消去 \(k\)，得到 \(ng(t)=0\)。左乘 \(y\) identity 后仅在非零 \(t\) 除 \(t\)，再比较两个时间得 \(nB=0\)，所以 \(\operatorname{rank}B\le1\)。没有用 \(t=0\) 的非法除法，也没有假定整个 \(I\) 上该分母预先非零。

## 4. 非零 rank-one 情形的 trace 必要性

记 \(R=\partial_y a_3\)、\(L=\partial_y\Theta_3\)、\(D=\partial_y\Theta_{12}\)。将上式代入 \(y\) identity，除非零 \(t\) 并令 \(t\to0\)，确得

\[
 D=I_2-kR.
\]

代回后精确为

\[
 B=\frac{k(L-\beta R)}{1+\beta t}.
\]

因 \(B\) 是非零常矩阵，比较两个局部时间即迫 \(\beta B=0\)，故 \(\beta=0\)、\(b=0\)。随后原 \(h\,g(t)=thk\) 对全部 \(I\) 给 \(g(t)=tk\)，不再存在局部分母零点的问题。

因此 \(B=k\ell\)，\(\ell=L\)，且完整 direction derivative 为

\[
 \begin{pmatrix}I_2-kR&-kh\\\ell&0\end{pmatrix}
 =\begin{pmatrix}I_2&-k\\\ell&0\end{pmatrix}
  \begin{pmatrix}I_2&0\\R&h\end{pmatrix}.
\]

两个 determinant 分别为 \(\ell k\) 和 \(h\)，所以满秩恰要求 \(h\,\operatorname{tr}B\ne0\)。由于 \(h\ne0\)，必要条件是 \(\operatorname{tr}B\ne0\)。对非零 rank-one 矩阵，\(B^2=(\operatorname{tr}B)B\)，正好等价于 \(\operatorname{rank}B^2=1\)。包括非零 nilpotent rank-one 在内的退化情形已被真正处理。

## 5. 两个充分构造完整符合原量词

\(B=0\) 时，\(T=[I_2,0]\)、\(a=(w,0)\)、\(\Theta=(y,\rho)\) 给投影 \(w+ty\)，direction derivative 为 \(I_3\)。额外 direction 不因其投影不可见而被错误丢弃；这正是合法 fibre ruling。

非零 \(B=k\ell\)、\(\ell k\ne0\) 时，

\[
 T(t)=[I_2,tk],\qquad
 a=(w,\rho),\qquad \Theta=(y-k\rho,\ell y)
\]

给

\[
 T(t)(a+t\Theta)=w+ty+t^2k\ell y,
 \qquad \det D_{(y,\rho)}\Theta=\ell k\ne0.
\]

\(T\) 始终 rank2，\(\Theta\) 独立 \(w\)，整个 ruling 域投影相同，所有函数 smooth。故补充不只是必要条件，充分性也已直接核验；它与一手文献标准 rank-one 构造一致。

## 6. 时间原点、标量例外与结论边界

本题原来就有 \(0\in I\)、\(F(0)=0\)、\(F'(0)=I_2\)，所以无需更换时间原点。稿中次要 time-origin 检查也正确：若平移到 regular \(t_*\)，必须同时令 \(w'=w+F(t_*)y\)、\(y'=(I_2+2t_*B)y\)，并把 lifted line 的新截距设为旧 \(a+t_*\Theta\)。后者仍可依赖 \(w'\)，新 \(\Theta\) 仍独立 \(w'\)。新 quadratic matrix 为 \(B(I_2+2t_*B)^{-1}\)，在所声明的可逆情形保 rank。不能仅平移 \(t\) 而漏掉这些参数改变；本主证明没有依赖该扩展。

标量 \(B=bI_2\ne0\) 在保留原时钟的空间仿射类中同样 rank2，不存在本类 lift；\(\tau=t+bt^2\) 则可把目标曲线换成直线，这是不同 clock 的等价，故不矛盾。一般空间 nonlinear submersion 不共享本证明的单一 \(T(t)\)，也不受本结果排除。

主 \(B=\operatorname{diag}(1,2)\) 因而已在整个指定光滑类中严格排除。该补充分类是同一核约束的自然收尾，不应转成继续研究更一般 clocks／nonlinear maps 的细节迭代。它没有将 curved-to-linear 的 forward 维数结论倒转，也没有证明或证伪高维 Kakeya。按本轮停止规则，归档后冻结此窄类。
