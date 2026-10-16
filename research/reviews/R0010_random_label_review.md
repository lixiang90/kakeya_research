# R0010：统一随机层标签质量界的独立逐步审查

日期：2026-10-17。审查者：audit_four_dimensional。被审稿：`notes/50_counterexamples/R0010_uniform_random_level_labels.md`，重点 RL1–RL6。另读取 `R0010_zero_depth_counterexample_attack.md` 核对被调用的 prior/profile、混合 density 与单 level cap 接口。未修改两份被审稿。

**结论：RL1–RL6 的统一概率论证与 chart/floor 接口通过本次内部独立审查，未发现需要阻断的缺口。** 不把辅助 quadrature 当作输出 data，不把最终 fixed tags 当成逐轨道重采样的 hidden law，是两个必要边界。本文未独立重证原四维论文，未证明新的 Kakeya 结果；整个形式模型的有限 horizon upper 还应由直接 true-system 构造单独确认。

## 1. 固定概率空间与 m/q 的单位正确

每个 level 的概率权为 \(\pi_\lambda=1/n\asymp\delta\)，不是条件化后又被省掉的权重。\(\Pi_\lambda\) 是下列固定变量的 product law：该 level 的可见 trajectory、微小 hidden offset \(e\)、微小 \(W\)、以及 \(\tau\sim U[0,1]\)。原时刻写作 \(t=t_0+q\tau\)，\(t_0,q\) 属于当前 chart 参数。

所以 \(\Pi_\lambda\) 本身不随 \(q,t_0\) 改变，而原 incidence integral 的 \(dt=q\,d\tau\) 正好与 \(m/q\) 相消。对于已固定的 tag table，

\[
 m_c/q\le\sum_\lambda F_{\lambda,\theta}(c_\lambda)
\]

是在原 probability prior 上的直接 upper。时间块与 \(I_0\) 的相交条件已经留在 \(H\) 中，没有隐含把短时 block 的 prior 重新归一化。

\(G_\theta\) 只要求完整 visible trace 的 whole-block spatial fit，不含 tag \(c\)。\(H_\theta(c,z)\subset G_\theta(z)\) 再要求当前时刻 small-value、导数 lower 和 \(t\in I_0\)。这恰好允许丢掉任意复杂 assignment/selection 来作 upper；复杂 assignment 的 polynomial-count predicates **没有进入** 统一计数的参数维数。

## 2. Hyperplane lift 和先选 quadrature

一个 chart 的 \(\theta\) 只含固定维参数：\(D^{-1}\) 的 entries、affine center、\(q,t_0,K\) 和一个 total-degree≤2 的测试系数。whole-block spatial fit 只需两个端点：偏差沿时间 affine，norm 凸。将 norm-square、small-value 与 derivative-square 条件写出后，所得 polynomial tests 数目和次数均固定。

例如 derivative 条件可写为 \(K^2P_w^2\ge1\)，不需要把 \(1/K\) 作为额外函数近似。以 \(D^{-1}\) 的 entries 直接参数化也避免了 inverse matrix 对参数的分母问题。admissibility 限制只缩小参数集合，不增加模式数。

在固定输入点上，每个 polynomial test 是 \(\theta\) 的一个有界次数多项式。将所有 \(\theta\)-monomials 提升为固定维坐标后，所有符号模式受一个固定维 hyperplane arrangement 的全部 faces 数控制，包括等号边界。故 \(m\) 点上的模式数 \(\le(Cm)^V\)，常数不依赖 coefficients 的高度、大小或 \(N_0\)。把 \(c\) 也列为参数仍是固定维。

由此得到的 distribution-free \(\varepsilon\)-approximation 可对每个 \(\Pi_\lambda\) 使用；该分布可以含离散 visible grid index 和连续噪声，不需要 Lebesgue 假设。标准 two-sample/swap 加 Hoeffding 的证明给 \(m_\varepsilon\le C_V\varepsilon^{-2}\log(2/\varepsilon)\) 的足够大固定常数选择。

原稿是 **先** 在每层选 quadrature，使其同时逼近所有 \((\theta,c)\) 的 \(H\) 与所有 \(G\)，**后** 随机选择 tags。次序正确。共同使用这些点也保证离散化后逐点仍有 \(\widetilde F\le\widetilde b\)。\(m_N\) 虽为 quasipolynomial，只是存在性分析工具；最终 prior 仍只有 polynomial 多个 level/grid/noise pieces，输出数据不包含 quadrature。

## 3. 归一化后的数值向量仍只有有限 patterns

对给定 \(\theta\)，\(\widetilde b_*\) 完全由 \(G\) 在预选 quadrature 上的 Boolean values 决定；因为 \(G\) 不含 \(c\)，该分母与当前随机 tags、ghost tags 都无关。

固定任意 \(2n\) 个 tags \((c_\lambda,c'_\lambda)\)，一并记录

\[
 H_\theta(c_\lambda,z_{\lambda,j}),\quad
 H_\theta(c'_\lambda,z_{\lambda,j}),\quad
 G_\theta(z_{\lambda,j}).
\]

原稿把三类 tests 同时计入 \((Cnm_N)^V\)，是必要且充分的。一个完整 sign pattern 固定所有加权 quadrature counts，继而固定 \(\widetilde b_*\) 及每个 \(g=\widetilde F/\widetilde b_*\) 数值。因此除法没有使模式集合变成不可控制的连续数值 family。

\(\widetilde b_*=0\) 时所有 \(\widetilde F\) 恒零，原积分之和最多 \(\varepsilon_N\)，已经单独覆盖。若没有把 \(G\) 的 patterns 计入，或让分母含随机 tag，此处的论证会失效；被审稿没有犯这两种错误。

## 4. Ghost／swap tail 的量词和常数

令 \(S=\sum g_\lambda(c_\lambda)\)、\(\mu=\sum E g_\lambda\)。对坏样本和它的某个 witness \(\theta\)，\(S>2\mu+t\)。独立 ghost 满足

\[
 \Pr\{S'\le3S/4\}\ge1-\frac{\mu}{3S/4}\ge1/3.
\]

在该事件上，\(D=S-S'\ge S/4\)，\(T=S+S'\le7S/4\)，所以 \(D\ge T/7\)；同时 \(T\ge S>t\)。因此一次 symmetrization 把原坏事件转成至多三倍的两样本事件。期望 \(\mu_\theta\) 已在这一步被移除，之后的事件只需两样本上的数值向量，无需对期望函数另作有限 pattern 假设。

条件于每对未排序 tags 后，独立交换的符号为独立 Rademacher variables；不要求不同 level 的 \(g_\lambda\) 同分布。固定一个数值向量时，

\[
 D=\sum_\lambda\epsilon_\lambda d_\lambda,
 \qquad
 \sum_\lambda d_\lambda^2
 \le\sum_\lambda(g_\lambda+g'_\lambda)=T.
\]

用 \(\prod\cosh(sd_\lambda)\le\exp(s^2\sum d_\lambda^2/2)\) 得

\[
 \Pr\{D\ge T/7\}\le e^{-T/98}\le e^{-t/98}.
\]

零差向量的情形概率为零，也符合此 bound。对至多 \(R=(Cnm_N)^V\) 个两样本数值向量 union bound 后，正好是 RL2 的 \(3R e^{-t/98}\)。witness 可以依赖原样本，swap 后也允许事后选参数；有限 pattern 的 union bound 已处理这种依赖。

原稿明确允许 outer-probability 版本，足以推出好 tag 向量存在。无需额外宣称含 \(\mu_\theta\) 的原坏事件本身是 semialgebraic：\(\mu_\theta\) 是参数积分，一般未必 semialgebraic。使用 outer-probability 或适当 universally measurable formulation 即可；该点不阻断证明。

取 \(t_N\) 为足够大常数乘 \(\log(Cnm_N)+\log N_0\)，失败概率小于 \(1/2\)。由 \(n\asymp N_0^M\)、\(\log m_N=O((\log N_0)^2)\)，有 \(t_N\le C_M(\log N_0)^2\)。因此一组确定 tags 同时适用于所有 chart 参数，而不是每个 chart 另选一组 tags。

## 5. 一元期望与 quadrature 误差回传

固定 \(z\) 时，tag \(c\mapsto P(t,Y,c+e+tW)\) 为一元次数≤2 多项式，导数正是 \(P_w\)。所以 small-value／导数事件在 \([0,1]\) 中的概率不超过

\[
 p_K=\min(1,4K^2a).
\]

由于 \(G\) 与 \(c\) 无关，逐 quadrature 点直接有

\[
 \sum E\widetilde F\le p_K\sum\widetilde b.
\]

这一步不需要假设最终 prior 的 hidden tag 在每条轨道上独立重采样；它只是寻找固定表的概率方法。

原积分与离散积分之差逐层乘 \(\pi_\lambda\) 后求和至多 \(\varepsilon_N\)，而非 \(n\varepsilon_N\)，因为 \(\sum\pi_\lambda=1\)。同理最大 \(b\) 的误差为 \(\pi_{\max}\varepsilon_N\)。故总回传误差为

\[
 (1+2p_K+t_N\pi_{\max})\varepsilon_N
 \le(3+t_N)\varepsilon_N,
\]

即 RL4。这里特别利用 \(p_K\le1\)，所以 additive error 对所有 \(K\) 统一；不需要为超大 \(K\) 改换 tags。

\(\varepsilon_N=\exp[-(\log N_0)^2]\) 使 \(r_N=(3+t_N)\varepsilon_N\) 比任意固定负幂小。quadrature approximation 已对任意实参数成立，故不需要预先猜测某个竞争 chart sequence 的 coefficient-height exponent 或 determinant 下界 exponent。

## 6. 从 RL4 到任意 chart/floor：原坐标的两个 cap

若 chart 对 \(I_0\) 有正 incidence mass，取 \(t_*\in I\cap I_0\)。whole-block spatial assignment 使可见 trace 属于 \(G_\theta\)。由混合可见 density \(g_{t_*}\le C\)，空间椭球的体积为 \(C K^3J\)，得到

\[
 \sum b_\lambda=\nu_{\rm vis}(G_\theta)\le C K^3J.
\]

另一方面，单层未归一化 cap 必须乘原 \(\pi_\lambda\asymp\delta\)：条件单层 cap 为 \(C\delta^{-1/2}q^{-3}K^3J\)，乘回来正是

\[
 b_*\le C K^3\delta^{1/2}q^{-3}J.
\]

这是同一 \(D\) 的原 \(J=|\det D|\)，不重新条件化 level，不改变 hidden derivative unit \(B=1\)。代入 RL4 后得 RL5，\(K\) 只出现固定次幂。任意复杂 assignment 和 current selection 都已被扩大到这一个 fixed-parameter \(H\)，没有使用“条件于该 assignment 后 hidden 独立”的假设。

本次已核对单层 \(\lambda\in[1,2]\) 的 cap 接口：固定条件数有界的 diagonal map 将其变成 Q=1 族，参数盒与 noise scales 仅作固定比较；任意原正交框可用 SVD 外包，ordered widths 与 determinant 只改变固定因子。这里没有只验证一个坏框就反推所有 frames。

## 7. Tempered J、进一步选择和 RL6

每个允许的 competing tempered chart system 有其固定有限 exponent \(B_*\)，使全部使用的 \(J\ge N_0^{-B_*}\)。该 exponent 可以很大，且不必与本构造的 \(M,U\) 相同；RL4 已对所有参数成立，因此仍用同一 tag table。\(r_N/J\) 仍比任意固定负幂小。

本模型 \(n(L)\sim_{\log}1\)，原 true floor 为 \(m/q\ge K^{-1}J\)。\(K=N_0^{o(1)}\) 时，\(K^Ca\to0\)，additive error 相对 \(K^{-1}J\) 也趋零。于是 RL5 迫

\[
 q^3\le N_0^{o(1)}\delta^{1/2},
 \qquad h\ge M/6.
\]

如果时间块与 \(I_0\) 不相交，则 \(m=0\) 且不能给 true 覆盖，未留下例外。进一步 inverse-subpower incidence selection 保留原支配关系及 density exponent；任意 subsequence 也保留 fixed-power 约束。允许的 horizon 竞争是在原问题坐标与原 mass floor 中进行，不能通过另选新 native \(B\)、另换 conditional prior 或 superpolynomial 薄 \(D\) 来规避。

因此 RL6 的 \(H\ge M/6>L\) 下界在形式模型内成立。确认有限 horizon 上界还需一份直接 true-system 构造；无 full-direction/source 资格、无 Kakeya 反例，也没有经外部同行审定的新维数结果。
