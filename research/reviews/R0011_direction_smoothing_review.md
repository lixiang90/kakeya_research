# R0011：方向平滑反例稿的逐步交叉审查

日期：2026-10-17。审查者：audit_four_dimensional。被审稿：`notes/50_counterexamples/R0011_direction_smoothing_attack.md`，主范围 §§1–8，另核 §9 的概率结论范围。该构造的 level-dependent shear 最初由本审查者提出；本次是对另一代理完整证明稿的逐步复核，不能将提出构造或重复自身稿件视为额外独立认证。root 另有独立初核，统一随机标签引理由 root 编写并已在 R0010 经本审查者逐步审查。仍是内部交叉核验，非外部同行评审。

**结论：主链通过，未发现阻断性缺口。** 实际 visible density \(A=O(1)\)、full8 tempered prior、全 depth 的 \(f\equiv0\)、\(S=1\)、单 level cap、重新选择好标签表、原 true floor 与有限 atlas 的接口一致。因此形式 \(j=3\) 模型中 \(M/6\le H\le M\) 与 \(\kappa=0\) 可同时成立。§9 只证明典型随机标签表的独立-copy 攻击变成 \(d=1\)，不能扩大成任意确定性表或所有 copy 方案的不可能定理。

## 1. 恒等式、同一 prior 与 full8 性

被审稿使用

\[
 b=(s,-sq-\lambda p/s,\lambda/s),\quad
 u=(p,\alpha\lambda-pq,q),\quad \alpha=1/10.
\]

直接展开确为 \(tY_2+Y_1Y_3=\lambda(1+\alpha t^2)\)。六个 coefficient noises 都为独立 \(U[-\delta,\delta]\)，所以新层恰为旧层加 \(\alpha\lambda t e_2\)，并非仅在无噪声 centers 上近似成立。

四参数 grid 总数 \(\asymp\delta^{-4}\)、单 index 权 \(\asymp\delta^4\)、level 权 \(\pi_\lambda\asymp\delta\)。hidden offset 与 \(W\) 在给定 level 后独立于整个 visible block；固定表 \(c_\lambda\) 把两块经 level 耦合。证明未错误使用 unconditional hidden/visible 独立性。

full8 density 的逐 box 贡献 \(C\delta^{-2}\eta^{-2}\) 正确。对实际 coefficient point，\(B_1,V_1,V_3\) 先限定 \(s,p,q\) 各 \(O(1)\) 候选，\(B_3\) 再限定 \(\lambda\)，所以实际重叠也是 \(O(1)\)。内部 copies 或共同 axis-facet refinement 都只有固定 polynomial 数；微噪声逆尺度、pieces 高度与数量在每个 sequence 内是固定 \(N_0\) 幂。tags 只是源 Definition 2.2 允许的有限实常数。

native \(P_*=w,B=1\)、selected event \(t\in[1/2,3/4]\) 及原质量 \(1/4\) 一致，没有观察到的 level-world 或 group 内概率正规化。

## 2. A=O(1) 是实际 Lebesgue density upper

\((\lambda,p,q)\mapsto(p,\alpha\lambda-pq,q)\) 的 Jacobian 绝对值为 \(\alpha\)，但关键的 finite-grid 论证也已写出：给定实际 \(v\)，\(v_1,v_3\) 只允许 \(O(1)\) 个 \(p,q\)，随后 \(v_2\) 只允许 \(O(1+\alpha^{-1})\) 个 levels。

对 \(s\) 求和以后，每个 \((\lambda,p,q)\) 概率 \(\asymp\delta^3\)，独立 velocity-noise density 为 \((2\delta)^{-3}\)。故

\[
 f_V(v)=\sum_{\lambda,p,q}\pi_{\lambda,p,q}
 (2\delta)^{-3}1_{\{|v-u_{\lambda,p,q}|_\infty\le\delta\}}
 \le C_\alpha.
\]

该式在原坐标、原 probability law 下逐 \(v\) 成立，不是 atomic bin cap，也没有先做未授权的 bin 内再分布。常数不依赖 \(M,U\)，所以 \(\kappa=0\) 确实满足本轮假设。

## 3. 全 r 的实际 profile 与两个 angular 尺度

加入噪声后

\[
 |Q(t,Y)-(1+\alpha t^2)\lambda|\le C\delta.
\]

分母至少1，故 fixed exact \((t,Y)\) 只有 \(O(1)\) 个 contributing levels。\(t\in I_0\) 时，固定 \(\lambda,s\) 后的 \(Y_1,Y_3\) 两式使 \(p,q\) 各只有 \(O(1)\) 个候选。将 \(O(\delta^{-1})\) 个 \(s\)、position-noise density \(O(\delta^{-3})\) 和 index 权 \(O(\delta^4)\) 相乘，确得 \(g_t\le C\)。

每层 hidden support 长 \(O(\eta)\ll a_L\)，所以每个 exact base 上全部 \(a_r\)-bins 数只有 \(O(1)\)，对所有 \(0\le r\le L\) 一致。原 observation density \(G_r\le C\)，reference support 体积 \(\le C\)。因此

\[
 \mu\{G_r<K^{-1}\}\le C/K
\]

给的是 source 意义的 sampled typical lower，并未从 support 体积直接断言 pointwise lower。于是实际 \(f(r)=0\)，不只是 \(f(0)=0\)，也没有把旧 exponent 整体平移。

对于 \(\rho\ge\delta\)，\(V_1\)-bin 加 \(Y_1\) 将 \(s\) 候选降到 \(O(\rho/\delta)\)，给 joint upper \(C\rho\)。对于 \(\rho<\delta\)，\(V_1,V_3,Y_1\) 与 level 定位留下 \(O(1)\) 个 indices，完整 \((Y,V)\) noise Jacobian 为1，得到 \(C\delta^{-2}\rho^3\le C\rho\)。加入一个 hidden bin 只将逐 index 贡献乘至多1的条件概率。故 \(S=1\) 的 joint upper 在全部正 widths 上成立，angular range 可固定。

## 4. 单 level cap 保留同一个 D、J 和原概率权

对 fixed level，whole-block fit 的 pullback 只是

\[
 y_c(t)\longmapsto y_c(t)-\alpha\lambda t e_2.
\]

旧 cap 允许任意 affine center，因此 \(D\)、\(J=|\det D|\)、\(q\) 和 spatial slack 完全不变。不需要将 spacetime shear 的 operator norm 混进原 \(J\)，更不需要从 actual visible density 上界反推 anisotropic plank cap。

乘回原 \(\pi_\lambda\asymp\delta\) 后，旧 conditional-level \(\delta^{-1/2}\) 成为单层未归一化 \(\delta^{1/2}\)：

\[
 \pi_\lambda\nu_\lambda(G)
 \le CK^3\delta^{1/2}q^{-3}J.
\]

原 all-positive-width 与任意 frame 的结论全部保留，短块外推所付 \(q^{-3}\) 也一致。这里有界 \(\lambda\)-dependent center 不破坏旧 cap 的统一常数。

## 5. 新 priors 上重新选统一标签表是合法复用

R0010 RL4 的证明对 \(\Pi_\lambda\) 只要求它固定且与自身 tag 无关；没有要求旧 slope cone 与 level 无关。新 visible centers 仍只是 \(z\) 的一部分，chart 参数 \(\theta\) 维数与 predicates 次数未增加。\(\tau\in[0,1]\) 仍取 fixed law，\(t=t_0+q\tau\) 位于 \(\theta\)-tests 内。\(G\) 仍不含 tag；tag 对 hidden coordinate 仍是系数1的平移，所以一元 quadratic sublevel 仍有效。

被审稿明确**在新 \(\Pi_\lambda\) 上重选一张好表**，而不是沿用旧模型的具体好表。先选 forall-\((\theta,c)\) 的辅助 quadrature、再取随机 tags、计入 \(G\) 分母 patterns 的 ghost/swap 步骤均有原证明保证。所有 \(\theta\) 的统一性覆盖事后选择的任意二次测试；任意复杂 assignment 先扩大为单 chart 的 geometry/current-test 事件，不增加 fixed-dimensional pattern 数。

故 (6.1) 可合法复用。由 \(g_{t_*}\le C\) 得 \(\nu_{\rm vis}(G)\le CK^3J\)，再用第4节单层 cap，正好得到

\[
 m/q\le CK^C[a+(\log N_0)^2\delta^{1/2}q^{-3}]J+r_N.
\]

\(r_N\) superpolynomial 小，而任意 competing tempered system 都有自己的固定 \(J\ge N_0^{-B}\)。原 floor \(m/q\ge K^{-1}n(L)J\)、\(n(L)\sim_{\log}1\) 迫 \(q^3\le N_0^{o(1)}\delta^{1/2}\)，即 \(H\ge M/6\)。进一步 inverse-subpower selections、arbitrary subsequences 及原坐标 horizon infimum 的量词都被该统一 upper 覆盖。

## 6. 有限 upper 的 current floor、完整 assignment 与 own-list

\(q=\delta\) blocks 上的完整 assignments 为 midpoint \(Y\)-cube \(Q\) 与原 \(w_0\)-terminal bin \(C\) 的 pair。一个 \(\delta\)-cube 内 \(Q(t_I,Y)/(1+\alpha t_I^2)\) 变化 \(O(\delta)\)，所以只遇 \(O(1)\) 个 levels；每层 \(w_0\) 微区间只遇 \(O(1)\) 个 bins。每 block 因而至多 \(C\delta^{-3}\) 个 pairs。

删 prior mass 小于 \(\tau\delta^3\) 的 pairs 损失至多 \(C\tau\)，小固定 \(\tau\) 保常量覆盖。每个 good pair 的原质量至少 \(\tau\delta^3\)；它并未被除以自身质量。\(D=C_1\delta I\) 的原 \(J=C_1^3\delta^3\)，整个 block 的 selected incidence mass 满足 \(m/q=\nu(A)\)。\(P=w-c_C\) 的 whole-block small value、\(P_w=1\)、\(P_{ww}=0\) 全部直接成立。扩大固定 slack 后每个 pair 都有正确的原 true floor。

current exact \(t,Y(t)\) 加 bounded velocity 给 midpoint cube 的 \(O(1)\) 选项；current terminal \(w\)-bin 加 \(|w_0-w(t)|\ll a\) 给原 \(w_0\)-bin 的 \(O(1)\) 选项。输出 label 不含内部 \(\lambda\) 或不可观察 noise。assignments 在每 block 内互不相交，编码数和 widths inverse 都为固定 \(N_0\) 幂。因此 \(H\le M\) 已直接证明，不依赖 generic completion，也不是 true system 集合为空的 vacuity。

## 7. 命题量词、full slope 成本与次要 §9 范围

先固定 \(L=1,d_0=1/2,S=1\) 与 angular range，再在不同 exact sequences 中选任意大的固定 \(M\)。每个 sequence 内 \(M,U\) 不发散，实际 \(\kappa=0\)，但 \(H/(L+\kappa)\ge M/6\)。因此不存在只依赖指定 cap 参数的统一有限常数。构造、cap 和随机标签工具均不调用 DIR-003/SRC-001 或四维深定理。

完整 \((V,W)\) 方向 marginal 没有 subpower ceiling。\(W\) 独立于 \(V\)，均匀在宽 \(\eta\) 的区间；bounded-support 单位概率 \(f_V\) 的 ess sup 有正的常数 lower，所以 full ceiling 在 \([c\eta^{-1},C_\alpha\eta^{-1}]\) 内。这个模型缺少原始 full-direction 来源；不能把 visible 三维 density 当成完整四维 slope density。

§9 的 L2 检查也核对成立：\(\max b_\lambda\le C/K_c\) 控制 diagonal，独立 uniform colors 的 off-diagonal 给 \(Ca\)，所以期望 \(\int\sum G_a^2\le C(a+K_c^{-1})\)。按 incidence mass 的 high-density tail 再除以 \(N_0^\tau a\)，正好得到 (9.3)，配 sampled lower 给典型随机表的 \(f(r)=r\)。该量词不能推广为“任何确定性 color table 都必变成 \(d=1\)”或“所有 copy 平滑方案都失败”；主反例不需要这种扩大。

最终通过的是 literal \(j=3\) 的 visible-direction-cost completion 反例。原论文实际 \(j=2\) 未被反驳；未构造全方向 Kakeya 集合，未解决 \(n\ge5\) Kakeya，也无新的维数下界或重大结果声明。按本轮停止规则，应冻结此 completion 策略并换几何任务，而不是在该反模型后继续追加同义条件。
