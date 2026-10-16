# R0010：实际 n(0)~1 的正向尝试；terminal group 的具体缺口

日期：2026-10-17。任务 N5-HOR-ZERO-01 的正向互补核查。作者：audit_four_dimensional。已读本轮 spec、恢复入口、原 Definitions 2.1、2.6、2.8，Lemmas 2.9–2.13 与 Proposition 2.16，并沿用已审 DIR-003 的方向成本边界。

结论：本稿没有证明 \(H\le L\)，也没有给该命题的反例。正向尝试得到一个明确的非循环缺口：\(n(0)\sim_{\log}1\) 控制 **exact base 上** terminal bins 的数量，不能直接控制它们在一个 terminal 空间 cube 内的联合标签数。下文给出可严格完成 cube extraction 的充分 lemma，以及一个 full8、\(n(r)\sim_{\log}1\)、正 angular cap 的边界例，证明原假设仍不保证这个 cube 步骤。该例本身有 \(H=0\)，所以不能误记为本轮主命题反例。

## 1. 零深度条件实际提供什么

原稿 Definition 2.1 的 native bounds 与 Lemma 2.9 表明，每个 selected exact base \((t,Y)\) 上只有 subpower 个宽 \(1/B\) 的可用 hidden bins：对 \(P_*(t,Y,w)\) 使用 \(|P_*|\le K_0\)、\(|\partial_wP_*|\ge B/K_0\)，可用区间总长 \(O(K_0^2/B)\)，故 bins 数 \(O(K_0^2)\)。bounded base 及足够 selected mass 给典型 \(n(0)\gtrsim_{\log}1\)。本轮额外 upper 才使它等于 \(1\) 的 logarithmic exponent；不是给 profile 免费减常数。

对 homogeneous profile，原 Lemma 2.5 的单调性与 cap-class 条件给

\[
 0=f(0)\le f(L)\le dL,
 \qquad a_L^d\lesssim_{\log}n(L)\lesssim_{\log}1.
 \tag{1.1}
\]

在 pure zero-depth density upper 与 terminal density lower 都经过适当 pruning 的 fixed exact base 上，terminal hidden bins 的数量至多

\[
 K_0/n(L).
 \tag{1.2}
\]

这是把 terminal good-entry density 下界相加、再用 zero-depth density upper 得到的逐 base 计数；有 subpower 个单位 hidden bins 也只增加 subpower 因子。它不控制随着 \(Y\) 改变而不断替换的 bin labels 的并。

## 2. 直接 terminal cube 法：数量预算在哪里失效

记 \(a=a_L\)，取 \(q\asymp a\)。像原 Proposition 2.16 一样，在每个 \(q\)-time block \(I\) 按

\[
 G=(\text{midpoint }Y\text{ 的 width-}q\text{ cube},
       \text{midpoint native }X\text{ 的 width-}a\text{ bin})
 \tag{2.1}
\]

分组。完整 assignments 在每个 block 内互不相交。由 bounded velocity、native quadratic coefficients 和当前 terminal observation，\(G\) 有 subpower 原始 \(p_L\) 列表。用 \(D=qI_3\)、静态 cube center 和测试 \(P_*-x_G\)，它们已经满足 whole-block 几何、small-value、导数和 tempered 输入；尚缺 true mass floor。

令 \(m_G\) 为该 group 的当前 selected incidence mass。期望每个 used group 有

\[
 m_G/q\gtrsim_{\log}n(L)q^3.
 \tag{2.2}
\]

但不加新结构时，每个 block 的粗计数仍是 \(K_0q^{-4}\)：空间 cubes 有 \(K_0q^{-3}\) 个，native \(X\) 有界仅给 \(K_0q^{-1}\) 个 terminal bins。删除低于 \(\epsilon n(L)q^3\) 的 normalized group mass，跨所有 blocks、原 world weights 的总损失 upper 为

\[
 \epsilon n(L)q^4\cdot K_0q^{-5}
   =K_0\epsilon\,n(L)/q.
 \tag{2.3}
\]

\(n(0)\sim_{\log}1\) 及 (1.1) 不会使 \(n(L)/q\) subpower；例如 \(n(L)=q^d\)、\(d<1\) 时，它是 \(q^{d-1}\)。所以不能选择 inverse-subpower \(\epsilon\) 就宣布保留足够质量。把 (1.2) 直接当作每个空间 cube 的 bin-count upper，恰好是未被证明的一步。

## 3. 一个确实足够的局部 coherence lemma

以下是可直接调用的有限充分条件，不是本轮原假设已经推出的结论。仍取 (2.1) 的真实 midpoint groups；用 \(N_{\gamma,I}\) 表示具有正 selected mass 的 groups 数。若在同一原始 measure 上有

\[
 \sum_{\gamma,I}\omega_\gamma q N_{\gamma,I}
 \le K_0 n(L)^{-1}q^{-3},
 \tag{3.1}
\]

则仅凭 cube groups 即可构造 horizon \(L\) 的真实 terminal system。一个更强但易理解的输入是：每个 block、每个 midpoint spatial cube 中，参与的 midpoint native bins 至多 \(K_0/n(L)\) 个。

**证明。** 删去 \(m_G/q<\epsilon n(L)q^3\) 的 groups。其 weighted incidence 总质量至多

\[
 \epsilon n(L)q^3
   \sum_{\gamma,I}\omega_\gamma qN_{\gamma,I}
 \le\epsilon K_0.
\]

扩大 \(K_0\) 以包含原质量下界，取 \(\epsilon\) 为足够小的 inverse-subpower，损失可小于原质量的一半。其余 groups 满足 (2.2)，只是 true-floor slack 增加 \(\epsilon^{-1}\)。whole-block 性质由第2节说明；\(P_*-x_G\) 的二阶 hidden 导数仍是 native 导数，故原 bound \(K_0B^2\) 比 terminal chart 允许的 \(K_0B^2/a\) 更强。所有 group predicates、finite pruning 和 widths 均 tempered，原 \(p_L\) 列表也保留。因而 \(q\asymp a_L\) 给 \(H\le L\)。证毕。

这个充分条件针对 **同一空间 cube 中标签的联合出现**，严格强于 (1.2) 的逐 exact-base 数量。它不把“存在 true system”换个名字作为假设；(3.1) 是一个直接的 midpoint histogram 计数。但本稿未能从 \(n(0)\sim1\)、profile 与 angular cap 推出它。

## 4. 完整边界例：profile 与角 cap 仍不能保证 isotropic cubes 为真

这个例子只否定第2节的快捷步骤，不否定 \(H\le L\)。设 \(N=2^n\)、\(L=1\)，并记

\[
 a=q=N^{-1},\qquad h=N^{-3},\qquad e=N^{-10}.
\]

其中 \(q\) 是待检验的 terminal time length，\(h\) 是更细的 stripe 宽度。取独立变量

\[
 B_1\sim U[0,1],\quad B_2,B_3\sim U[-2,2],\quad
 V_1\sim U[-e,e],\quad V_2,V_3\sim U[-1,1].
\]

令 \(j=\lfloor B_1/h\rfloor\)、\(k=j\bmod N\)，另取独立 \(z,W\sim U[-e,e]\)，并定义

\[
 Y(t)=B+tV,\qquad
 w_0=(k+1/2)q+z,\quad w(t)=w_0+tW,\qquad P_*=w, B=1.
 \tag{4.1}
\]

这在完整八系数空间有 piecewise constant Lebesgue density：按 \(B_1\) 的 \(h\)-stripes 分为 \(N^3\) 个 pieces，各 piece 的 \(w_0\) 为长度 \(2e\) 的区间。所有 heights、pieces 与 reciprocal widths 为固定 \(N\) 幂。

选择事件为

\[
 t\in[1/2,3/4],\quad Y_2,Y_3\in[-1/2,1/2],\quad
 \operatorname{dist}(Y_1,h\mathbb Z)\ge4e.
 \tag{4.2}
\]

并保持 \(Y_1\in[0,1]\)。这是 polynomial-count、bounded-degree 的有限谓词。其质量趋于 \(1/64\)。selected 点上 \(B_1\) 与当前 \(Y_1\) 位于同一个 \(h\)-stripe，所以 exact \(Y_1\) 确定 \(j\) 和 \(k\)。\(w(t)\) 始终距 \((k+1/2)q\) 不超过 \(2e\)，故在所有 dyadic hidden widths \(a_r\ge q\) 上，当前 hidden bin 都由 exact base 确定。

在 selected base 上，\(Y_1\) density 是1，\(Y_2,Y_3\) 各为 \(1/4\)：给定 \(t\le3/4\)、\(|Y_i|\le1/2\)、\(|V_i|\le1\)，反推的 \(B_i\) 总在 \([-2,2]\) 内。因此每个 \(r\in[0,1]\) 的 nonzero observation density 恰为 \(1/16\)。所以

\[
 n(r)\sim_{\log}1,\qquad f(r)=0.
 \tag{4.3}
\]

原 native bounds 均成立，故它满足 literal \(j=3\) 的 profile 部分，对任意固定 \(0\le d<1\) 都可用。

**正 angular cap。** 给定 selected exact base，\(V_2,V_3\) 仍各自在固定长度区间均匀，\(V_1\) 在长度 \(2e\) 区间均匀；stripe 条件已保证其所有可能值对应同一 hidden bin。任意 width-\(\rho\) velocity cube 的 joint probability 因子不超过

\[
 C\min(1,\rho/e)\rho^2\le C\rho^2.
 \tag{4.4}
\]

因此 pure terminal density 为常数时，形式 (2.6) 可取 \(S=2\)，且包括 \(\rho<e\) 的尺度。

**Isotropic terminal groups 的不足。** 每个 width-\(q\) 的 midpoint \(Y_1\)-interval 含 \(N^2\) 个 \(h\)-stripes。每个 \(k\in\{0,\ldots,N-1\}\) 重复约 \(N\) 次，所以对应 \(B_1\) 总长度约 \(Nh=q^2\)。再乘 midpoint \(Y_2,Y_3\) 的 \(q^2\) 面积，得到

\[
 \nu(G)\le Cq^4,
 \qquad m_G/q\le Cq^4.
 \tag{4.5}
\]

对于远离 selected boundary 的 cells，相应 lower 也成立；boundary 删除只损失 \(O(e/h)+O(q)\) 質量。可是 \(D=qI_3\) 的 true floor 为 \(n(L)J\sim_{\log}q^3\)。因此这些 groups 欠一个固定幂 \(q\)，不能用 subpower slack 直接修复。每个 midpoint 空间 cube 实际有 \(N=q^{-1}\) 个 native terminal labels，而每个 exact base 只有一个。

**该例仍有 \(H=0\)。** 在全时间块上按原 \(B_1\) 的每个 \(h\)-stripe 赋不同 label，取 \(D=\operatorname{diag}(h,1,1)\)、相应静态第一坐标中心及测试 \(w-(k+1/2)q\)。whole-time spatial fit 有固定 slack，small-value 误差 \(O(e)\ll q\)，hidden derivative 为1。每个 stripe 的 assigned prior 与 selected mass 都是 \(\asymp h\)，而 \(n(L)|\det D|\asymp h\)。这些是覆盖常量质量的全时 true packets；在 (4.2) 的 selected event 上，当前 exact \(Y_1\) 也识别 stripe label。故不能把 (4.5) 升级为本轮命题的反例。

此例给出了正向缺口的实际数学证据：即使满足本轮 density/profile/angular 条件，仍可能必须提取高度 anisotropic 的空间框。\(n(0)\sim1\) 本身没有让该几何步骤自动消失。

## 5. 与 DIR-003、closure 及本轮反例攻击的接口

DIR-003 只有在同一原 prior 存在实际 visible-slope/bin upper 时可用。将它用于 normalized terminal group，原 direction-density 成本是旧成本乘空间/时间 Jacobian，并在条件化时除以完整 group prior mass；不能用 \(n(0)\sim1\) 替代这个方向输入。R0009 已核的比较最多给 \(n(L)q^3\) 与已有方向成本之间的关系，不输出所需空间框。

因此尚未闭合的正向问题是：从现有 exact/profile/angular 数据中，取得 anisotropic whole-block spatial assignments 的 current true floor，而不调用已否定的无方向 WP4。第3节给了一种可检验的充分 coherence 输入，第4节严格说明它不由现有条件直接成立；本稿在这里停止，不把这一缺口反复重命名为结论。

即使未来对本轮类证明 \(H\le L\)，也须另核 closure：原 Lemma 2.13 的 prepared true parent 保 \(n'(0)\sim1\)，但 §4.2 extension 中 known、未必 true 的 atlas normalization 没有该保证。原 §4.1 对所有 \(\mathcal C(d)\) 优化不能直接改为受限类后沿用旧极值论证。

root 的 random-label quadric-level 反例方向若最终完成，必须另行证明对所有二次测试与所有 competing charts 的统一质量 upper；本稿的 stripe 例没有承担该任务，也没有把隐藏标签在 selected exact base 上可恢复误写成任意完整 chart label 已知。

收尾状态：统一随机标签及finite true atlas现已另证并独审，见HOR-002入口。本稿仍只作为正向shortcut缺口和H0 stripe边界例，不将自身充作该整体反例。
