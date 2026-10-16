# R0011：方向成本正向候选的审计；level-dependent shear 反例接口

日期：2026-10-17。任务 N5-DIR-COST-01。作者：audit_four_dimensional。最初独立尝试正向证明，发现下列精确 level-dependent shear 后，按 root 指示将本稿收束为主反例的接口审计。root 已初核，反例代理正独立审查；本稿不把自身推导登记为独立外部审定。

**结论。** 没有得到所拟 \(H\le C(L+\kappa)\) 正向证明。相反，R0010 的 level-coloring 模型经下列有界 shear 后，原 visible-slope prior 的**实际 Lebesgue density** 为 \(O(1)\)，即 \(\kappa=0\)，但先前统一随机标签引理仍适用，给

\[
 M/6\le H(E)\le M
 \qquad\text{对任意固定 }M>6L.
 \tag{0.1}
\]

取 \(L=1,d_0=d=1/2,S=1\) 及任意固定 angular depth range，令 \(M\) 任意大，即排除独立于 tempered complexity exponent 的有限常数 \(C\)。这里是 literal \(j=3\) version 2 的模型反例，仍不是原 \(j=2\) 论文反例、Kakeya 反例或新维数下界。

## 1. 精确 shear 与不丢失 level 的恒等式

固定 \(\alpha=1/10\)，\(\delta\asymp N_0^{-M}\) 为 dyadic 宽度。沿用 R0010 四参数格点

\[
 \lambda,s\in[1,2]\cap\delta\mathbb Z,
 \qquad p,q\in[-1/10,1/10]\cap\delta\mathbb Z,
\]

全部四参数均匀、相互独立。每个四参数 index 概率 \(\asymp\delta^4\)，level 邊缘概率 \(\pi_\lambda\asymp\delta\)。定义

\[
 b=(s,-sq-\lambda p/s,\lambda/s),\qquad
 u=(p,\alpha\lambda-pq,q).
 \tag{1.1}
\]

可见完整 coefficients 为

\[
 B=b+\xi,\quad V=u+\zeta,\qquad
 \xi,\zeta\sim U[-\delta,\delta]^3
 \tag{1.2}
\]

并且这六个 noise coordinates 独立。无噪声时直接展开得到

\[
 t(b_2+tu_2)+(b_1+tu_1)(b_3+tu_3)
   =\lambda(1+\alpha t^2).
 \tag{1.3}
\]

等价地，这就是将原 \(Q=\lambda\) 族中的 \(Y_2\) 改成 \(Y_2+\alpha\lambda t\)。这是每个 level 内固定的有界 affine shear，**不是**在每条轨道上独立随机选择一个任意 shear。

加入 (1.2) 后，所有 bounded coordinates 上仍有

\[
 \left|\frac{tY_2+Y_1Y_3}{1+\alpha t^2}-\lambda\right|
 \le C\delta.
 \tag{1.4}
\]

因为分母在 \([1,1+\alpha]\) 内，fixed exact \((t,Y)\) 仍只接收 \(O(1)\) 个 \(\lambda\)-grid levels。这里没有出现独立 shear 混合通常造成的 level 隐藏、conditional hidden dimension 变1的问题。

恒等式 (1.3) 及下一节 slope Jacobian 已用独立于文件的 Sympy 精确展开辅助核验，残差为0、Jacobian 为 \(-\alpha\)；连续估计以下面的解析证明为准。

## 2. 实际 visible-slope density A=O(1)，不是 bin-only 假设

无噪声 slope map 为

\[
 (\lambda,p,q)\longmapsto(p,\alpha\lambda-pq,q),
 \qquad
 \left|\det\frac{\partial u}{\partial(\lambda,p,q)}\right|=\alpha.
 \tag{2.1}
\]

不过，仅有连续 Jacobian 还不能代替有限 grid 平滑后的密度证明。下面直接算本模型的 Lebesgue density。

\(s\) 完全不影响 \(u\)，对其求和后每个 \((\lambda,p,q)\) 的概率为

\[
 \pi_{\lambda,p,q}
   =(N_\lambda N_pN_q)^{-1}\asymp\delta^3.
\]

原 \(V\) 的实际三维 density 精确为

\[
 f_V(v)=\sum_{\lambda,p,q}\pi_{\lambda,p,q}
    (2\delta)^{-3}
    1_{\{|v-(p,\alpha\lambda-pq,q)|_\infty\le\delta\}}.
 \tag{2.2}
\]

固定任意 \(v\)。第一、第三 coordinates 分别把 \(p,q\) 限在长度 \(2\delta\) 的区间，所以各只有 \(O(1)\) 个候选。再由第二 coordinate，\(\lambda\) 落在长 \(2\delta/\alpha\) 的区间，只有 \(O(1+\alpha^{-1})\) 个候选。因此

\[
 \boxed{f_V(v)\le C(1+\alpha^{-1})=O(1)
       \quad\text{对所有 }v.}
 \tag{2.3}
\]

这是同一原概率 prior、原可见速度坐标下的 full-dimensional Lebesgue upper，未先在 \(\delta\)-bins 中均匀重分布，也未条件化任何 small group。\(\xi\) 的加入不改变该 marginal；\(\zeta\) 正是 (2.2) 中的实际独立三维盒噪声。故单 world 确实满足本轮 \(N_0^{\kappa+o(1)}\) 条件，\(\kappa=0\)。

## 3. 完整八系数 prior、实际 profile 与 angular cap

选终端 \(a_L=N_0^{-L}\)。固定 \(U>M+L+10\)，令 \(\eta_{\rm noise}\asymp N_0^{-U}\)。每个 level 只对应一个稍后固定的 \(c_\lambda\in[0,1]\)，取

\[
 w_0=c_\lambda+e,\quad e\sim U[-\eta_{\rm noise},\eta_{\rm noise}],
 \qquad W\sim U[\eta_{\rm noise},2\eta_{\rm noise}],
 \qquad w(t)=w_0+tW.
 \tag{3.1}
\]

给定 level/index，\(e,W,\xi,\zeta\) 相互独立。visible block 与 \(w_0\) 经 \(\lambda\) 耦合，不能使用 R0008 的 unconditional product-hidden 论证。native \(P_*=w,B=1\)，selected event 只为 \(t\in I_0=[1/2,3/4]\)，总质量 \(1/4\)。

**Tempered 性。** 每个四参数 index 给完整 \((B,V,w_0,W)\) 八维 box。density 贡献 \(O(\delta^{-2}\eta_{\rm noise}^{-2})\)，pieces 数 \(O(\delta^{-4})\)。重叠数有统一 bound：\(B_1,V_1,V_3\) 分别限制 \(s,p,q\)，再由 \(B_3\approx\lambda/s\) 限制 \(\lambda\)，每个坐标条件只有固定多个 grid 候选。可以使用内部 copies，或共同矩形 refinement；两者都是固定 polynomial 有限性。tags 只为固定实常数，不是 worlds/observed features。所有 native bounds 为绝对常数。

**可见 exact-base density。** fixed \(t\in I_0\)、\(Y\) 时，(1.4) 先限制 \(\lambda\) 为 \(O(1)\) 个。fixed \(\lambda,s\) 后，

\[
 Y_1=s+tp+O(\delta),\qquad
 Y_3=\lambda/s+tq+O(\delta)
\]

使 \(p,q\) 各只有 \(O(1)\) 个格点。\(s\) 有 \(O(\delta^{-1})\) 个候选，单 index position-noise density 为 \(O(\delta^{-3})\)，原 index 权 \(O(\delta^4)\)，故

\[
 g_t(Y)\le C\delta^{-1}\delta^{-3}\delta^4=C.
 \tag{3.2}
\]

**实际 profile。** 所有 \(Y\) 在固定有界盒内。对每个 contributing level，\(w(t)\in c_\lambda+[-\eta_{\rm noise},3\eta_{\rm noise}]\)，因此任意 \(a_r\ge a_L\gg\eta_{\rm noise}\) 时只有 \(O(1)\) 个 hidden bins。结合 (1.4)，每个 exact base 上的全部 contributing bins 仍是 \(O(1)\)。于是原 observation density \(G_r\) 有

\[
 G_r\le g_t\le C,
 \qquad
 |\operatorname{supp}G_r|_{dt\,dY\times\#B}\le C.
\]

从同一 density 的小值集合积分，\(\mu\{G_r<K^{-1}\}\le C/K\)。取 \(K=N_0^\tau\) 得全 depth range 的 typical

\[
 \boxed{n(r)\sim_{\log}1,\qquad f(r)=0.}
 \tag{3.3}
\]

它不是给旧 exponent 平移，也不是通过 world weights 改变 within-world density。

**Angular。** fixed \((t,Y)\) 的 possible levels 仍是 \(O(1)\)。当 velocity width \(\rho\ge\delta\)，其第一 coordinate 给 \(p\) 宽 \(O(\rho)\)，再由 \(Y_1\) 约束使 \(s\) 有 \(O(\rho/\delta)\) 个 grid 候选；各 \(\lambda,s\) 只给 \(O(1)\) 个 \(p,q\)。所以 joint density 上界为

\[
 C\delta^4(\rho/\delta)\delta^{-3}=C\rho.
\]

当 \(\rho<\delta\)，velocity 第一、第三 coordinates 与 \(Y_1\) 使所有 \(s,p,q,\lambda\) 候选共 \(O(1)\) 个。单 index \((Y,V)\) density 为 \(O(\delta^{-6})\)，故积分 velocity bin 得 \(C\delta^{-2}\rho^3\le C\rho\)。再加指定 hidden bin 只会减小这些 upper。因此全尺度

\[
 G_{r,\rho}(t,Y,B,J)\le C\rho.
 \tag{3.4}
\]

可固定 \(S=1\)，任意固定 angular depth range。\(f\equiv0\) 满足任意合法 \(d\ge0\) 的 cap-profile upper；取 \(d=d_0=1/2\) 即已足以测试主命题。以上对任意 fixed tag table 成立。

## 4. 单 level 空间 cap 原封保留；原 J 不变

记旧 \(Q=\lambda\) level law 为 \(\nu_\lambda^{\rm old}\)，新 law 是其有界 shear 的 pushforward。对任意固定 whole-block chart geometry \((I,D,y_c)\)，

\[
 \nu_\lambda^{\rm new}\{\sup_I|D^{-1}(Y-y_c)|\le K\}
 =\nu_\lambda^{\rm old}
   \{\sup_I|D^{-1}(Y-(y_c-\alpha\lambda t e_2))|\le K\}.
 \tag{4.1}
\]

旧单 level cap 本来对任意 affine center 成立。所以上式只改变 center，连 spatial matrix \(D\) 都不用改变；原 \(J=|\det D|\) 完全相同。R0010/R0008 的 all-width cap 给

\[
 \boxed{\pi_\lambda\nu_\lambda^{\rm new}(G_\theta)
 \le CK^3\delta^{1/2}q^{-3}J.}
 \tag{4.2}
\]

这里乘回了原 level probability \(\pi_\lambda\asymp\delta\)。不能把它当成 conditional-on-level 的同阶 upper。另一方面，若 block 与 \(I_0\) 有 positive selected time，由 (3.2) 在其中任一时刻取截面，得

\[
 \nu_{\rm vis}^{\rm new}(G_\theta)\le CK^3J.
 \tag{4.3}
\]

两个估计所用 law 与 (2.2)–(3.4) 完全相同。没有给每个 level 或 competing assignment 另作 conditional 归一化。

## 5. R0010 uniform random-tag 引理复用的严格条件

R0010 `R0010_uniform_random_level_labels.md` 的证明所需的是：fixed \(\Pi_\lambda\)、fixed-dimensional bounded-degree chart tests、\(G\) 不含 tag、\(H\subset G\)、tag \(c\) 对 hidden coordinate 是系数1的平移，以及 (4.2)–(4.3)。它没有使用旧 slope cone 必须与 \(\lambda\) 无关。

这里把 \(z\) 中 visible trajectory 改为新 coefficients，其余 normalized time \(\tau\in[0,1]\)、\(t=t_0+q\tau\) 及 \(e,W\) 仍取 fixed law。\(P(t,Y,c+e+tW)\) 对 tag 仍是一元 degree≤2，current derivative 仍是 \(P_w\)。不论 \(\lambda\) 如何进入可见 coefficients，参数 \(\theta\) 的维数、polynomial tests 数和次数都没有增加。

因此可对这些新 \(\Pi_\lambda\) **重新一次性选择**一张好 tag table；不声称旧模型已选的同一张表自动适用新模型。先选 forall-\((\theta,c)\) 的辅助 quadrature、再选 tags、将 \(G\) patterns 纳入归一化分母、ghost/swap 及 superpolynomial 小误差的全部步骤直接保留。得到

\[
 \frac{m_c}{q}\le CK^C
   \left[a_L+(\log N_0)^2\delta^{1/2}q^{-3}\right]J+r_N,
 \qquad r_N=N_0^{-\omega(1)}.
 \tag{5.1}
\]

这个 upper 对所有二次 tests、原坐标中的全部 competing tempered charts 及任意复杂 assignment/current selection 同时成立。复杂 assignments 先扩大为单 chart 的 complete spatial fit 加 current-test 事件；它们不进入 fixed-dimensional pattern bound。

原 true floor 是 \(m_c/q\ge K^{-1}n(L)J\)，本模型 \(n(L)\sim_{\log}1\)。任意 competing tempered system 都有其固定 \(J\ge N_0^{-B}\)，且 \(K=N_0^{o(1)}\)，所以 (5.1) 迫

\[
 q^3\le N_0^{o(1)}\delta^{1/2},
 \qquad H(E)\ge M/6.
 \tag{5.2}
\]

Further inverse-subpower incidence restriction 保留原 prior 支配与 profile exponent，subsequences 也不改变该 fixed-power lower。没有调用 DIR-003、SRC-001 或已被否定的 WP4；这里的随机标签概率论证是独立的初等 finite-parameter 工具。

## 6. 有限 horizon 的原始 true system 仍存在

沿用 R0010 的直接 \(q=\delta\) 构造，不借用 generic completion。对每个完全位于 \(I_0\) 的 time block，在 midpoint 按 \(Y\) 的 \(\delta\)-cube 和 \(w_0\) 的 terminal \(a_L\)-bin 分组。

bounded support 给 \(O(\delta^{-3})\) 个 \(Y\)-cubes。由 (1.4)，一个这样的 midpoint cube 只遇到 \(O(1)\) 个 levels，每个 level 的 \(w_0\) 只碰到 \(O(1)\) 个 terminal bins，所以总 groups 数 \(O(\delta^{-3})\)。删 prior mass 小于 \(\tau\delta^3\) 的 groups，损失 \(\le C\tau\)；小固定 \(\tau\) 留常量质量。

每个保留 group 用 \(D=C\delta I_3\)、静态 midpoint cube center、测试 \(w-b_B\)。bounded velocity 与 \(W\ll a_L\) 给 whole-block fit 与 small-value，\(P_w=1\)。其 \(m/q\ge\tau\delta^3\) 与 \(n(L)J\asymp\delta^3\) 匹配。原 current exact \(Y\) 给 midpoint cube 的 \(O(1)\) 列表；当前 terminal \(w\)-bin给 \(w_0\)-bin 的 \(O(1)\) 列表。没有输出内部 \(\lambda\) label。所有 assignments 与数据都固定 polynomial 有限，因此 \(H(E)\le M\)。

这证明 (0.1) 的有限 upper；不是以 true system 集合为空制造无限 horizon。

## 7. 正向路线因此排除的捷径与 source 边界

本构造同时具有：actual visible density \(A=O(1)\)、actual \(f\equiv0\)、正 angular cap、full8 prior，仍有任意大 \(H/L\)。所以 long native-label profile 加 DIR-003 所控制的 projected visible directions，不足以产生本轮所需 true spatial extraction。再应用相同 projected finite input 并重算已知 Jacobian，不会消去 (5.2) 的 counterexample。

原 source 的 **完整** \((V,W)\) 方向来源并未满足。这里 \(W\) 在长 \(\eta_{\rm noise}\) 的区间均匀，且与整个 visible block 独立，所以完整 slope density 是

\[
 f_{V,W}(v,w)=f_V(v)\,\eta_{\rm noise}^{-1}
 1_{[\eta_{\rm noise},2\eta_{\rm noise}]}(w).
\]

其 ceiling 为 \(\asymp\eta_{\rm noise}^{-1}=N_0^U\)：upper 由 (2.3) 给出，lower 因 \(f_V\) 是 bounded support 上的单位概率而成立。可见 \(\kappa=0\) 没有约束这个 hidden-slope 成本。Theorem 2.17 的初始 full-slope density 与后续 slope-volume 比较使用的正是更强数据；不能由本稿 flat visible marginal 代替。

按本轮停止规则，这是否定 proposed visible-cost uniform completion 的实质证据，不能继续给同一泛类追加同义统计条件或把结果宣称为高维 Kakeya 反例。下一宏观转向由 root 统一决定；本稿不自动重开其它模板或要求新的模型假设。
