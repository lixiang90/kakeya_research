# R0021：原 PCT 精确形式的有限反例与修正版独立核验

2026-10-17，`lifting_obstructions`。已读本轮 opening macro、working spec、R20 mixed32 handoff、GOAL/STATE 和 root 的 `R0021_polynomial_tube_KT.md`。只处理有限 polynomial 输入及其 source 尺度检查；长期 Goal 未解决。

## 1. 结论、覆盖约定与原式的区别

使用 root 终稿明确的约定：$N_r$ 为**半径 r 的欧氏球**的最少覆盖数；一维 tube 是长度 $L$ 的区间。原待证式

\[
 R/e\le C(D,m)\big(K\theta^{-C(D,m)}\big)^{2/\gamma}            \tag{1.1}
\]

对 $\gamma\in(0,1)$ 的一致性为假，已经有有限 $D=m=1$ 反例。不是只知道某个粗证明推不出该常数位置。

修正为

\[
 R/e\le\big[C(D,m)K\theta^{-C(D,m)}\big]^{2/\gamma}            \tag{1.2}
\]

则下文给出自包含有限证明，并逐项核过 root 证明的离散分支、preimage multiplicity 和 Taylor 尺度。该修正与 source 中先固定 $\gamma$、再取小误差指数、最后取 $\delta$ 小的参数顺序相容；不能说两种有限精确形式相同。

常数位置的反例依赖已经明确的球覆盖约定。换成边长 r 的 dyadic cubes 会改变具体常数，不能未经计算声称第2节同一 $K$ 仍成立。修正版 (1.2) 才对固定倍覆盖约定稳定。

## 2. 全部尺度 tube-KT 都通过的有限线性反例

对整数 $n\ge3$，取

\[
 \gamma=\frac1{2n},\quad e=d_0=2^{-n},\quad
 P(t)=t,\quad B=Y=\{j2^{-n}:0\le j\le2^n\},\quad\theta=1.
                                                                    \tag{2.1}
\]

于是 $D=m=1$，$R=1$，B 是 $d_0$-separated，$\#B\ge1/d_0$，$e=d_0R$，$P(B)=Y$。Y 本身为有限网格，未使用连续区间作为隐藏替代。

令 $e'\in[e,1]$，tube 为任意长 $L\in[e',1]$ 的区间。记 $x=L/e'\in[1,2^n]$。整个区间可以由 $\lceil x/2\rceil$ 个半径 $e'$ 的球覆盖，故

\[
 N_{e'}(Y\cap\mathrm{tube})\le\lceil x/2\rceil.               \tag{2.2}
\]

证明对所有这些 x 都有

\[
                 \lceil x/2\rceil\le2^\gamma x^{1-\gamma}.   \tag{2.3}
\]

当 $1\le x\le2$，左边为1。若 $2(k-1)<x\le2k$、$k\ge2$，比值的 supremum 至多

\[
 f(k)=\frac{k}{[2(k-1)]^{1-\gamma}},\quad
 2\le k\le2^{n-1}.
\]

把 k 暂当连续变量，有

\[
 (\log f)'(k)=\frac{\gamma k-1}{k(k-1)}.
\]

所以 f 先降后升，整个有限区间的最大值在两端之一。第一端 $f(2)=2^\gamma$；另一端为

\[
 f(2^{n-1})
   =2^{-1/2}(1-2^{1-n})^{-(1-\gamma)}
   \le\frac{4}{3\sqrt2}<1.                                  \tag{2.4}
\]

端点 $x=2(k-1)$ 的 ceiling 反而较小，不产生遗漏。由此 (2.3) 成立：题设任意宽度、任意长度、任意位置 tube-KT upper 均可取

\[
                           K=2^\gamma.                       \tag{2.5}
\]

若 (1.1) 有只依赖 D,m 的统一 C，则本例要求

\[
                       2^n\le C K^{2/\gamma}=4C,
\]

令 n 任意大即矛盾。$\gamma$ 的变化是必要的：此处否定的正是“不让 C 依赖 $\gamma$、却把它放在幂外”的原一致量词。没有否定 (1.2)，也没有否定固定 $\gamma$ 后容许常数依赖它的较弱表述。

## 3. 修正版的有限次数与离散坏集事实

下文固定 D,m，所有 C、c 只依赖它们。记 $Q=R/e$。若 R=0，结论平凡。减去 P(0) 后，Lagrange 固定结点插值给

\[
 \|P'\|_\infty+\|P''\|_\infty\le C R.                        \tag{3.1}
\]

存在标量分量 p 的 oscillation 至少 $R/\sqrt m$；由积分 bound，$\|p'\|_\infty\ge R/\sqrt m$。这避免“R 小或系数相消时导数必宏观”的错误：所有比较都相对于同一个 R 归一化。

对次数不超过 $D-1$ 的非零 polynomial $q=p'$，$D\ge2$ 时，用有限插值可得

\[
 |\{t:|q(t)|\le\alpha R\}|
                 \le C\alpha^{1/(D-1)}.                    \tag{3.2}
\]

简证：若该集合测度为 b，用其测度分位点选 D 个互距 $\gtrsim_D b$ 的点。Lagrange 分母下界给 $\|q\|_\infty\le C\alpha R b^{-(D-1)}$，与 $\|q\|_\infty\gtrsim_mR$ 比较。q 的实际次数更低时使用这个较弱指数即可；q 常数则直接检查。

坏集由至多 $C_D$ 个区间/孤立点组成，因为其边界由 $q=\pm\alpha R$ 的根给出。因此其 d₀-separated 样本数满足

\[
 \#(B\cap\mathrm{bad})
       \le |\mathrm{bad}|/d_0+C_D.                           \tag{3.3}
\]

这是不能丢掉的离散误差。若 $d_0\ge c\theta$，原条件 $e\ge d_0R$ 已给 $Q\le1/d_0\le C\theta^{-1}$，被 (1.2) 的平凡项吸收。其余取

\[
 \alpha=c\theta^{D-1},\quad d_0<c\theta,
\]

令坏集测度≤θ/8，并让 (3.3) 的边界项≤θ/(8d₀)。这样仍有至少 $c\theta/d_0$ 个 good 样本。D=1 时 p' 是绝对值≥R/√m 的常数，直接用固定 α、全部样本；无需假装使用 D−1 分母。

## 4. 像的重复次数：不要求全局单射

good set 有至多 $C_D$ 个 connected components，每个上 $|p'|\ge\alpha R$ 且符号固定。故对于任意长度 $C e$ 的实区间 J，

\[
 \#\{t\in B_{\rm good}:p(t)\in J\}
    \le C\left(1+\frac e{\alpha R d_0}\right)
    \le C\frac e{\alpha R d_0}.                             \tag{4.1}
\]

最后一步正好使用 $e\ge d_0R$。可以跨所有 good components 求和，只付固定 D；不需要把 vector P 的自交或 scalar p 的折返视为不可能。

如果半径 $C e$ 的球覆盖若干 Y-witnesses，则对应 P(t) 的标量分量落在长度 O(e) 的区间，故这些 samples 也服从 (4.1)。witnesses 可以重合、权重不均；这里只数原 B 的 preimages。

## 5. 短切管、局部样本和上、下 covering

只需考虑 Q 大于一个固定阈值。取

\[
                       h=c Q^{-1/2}.
\]

把 [0,1] 分为 $O(1/h)$ 个半开 intervals。某 interval I 含至少 $c\theta h/d_0$ 个 good 样本；不要求 B 在每个 h-window 中都稠密。以 I 的端点作 Taylor 展开，(3.1) 给余项 $O(Rh^2)=O(e)$，切段长度 $O(Rh)=O(\sqrt{Re})$。

所以所有选中 P(t) 的 Y-witnesses 都在某个直 tube 中，宽

\[
            e'=C_0 e,\qquad L=C_1\sqrt{Re}.                  \tag{5.1}
\]

选择 Q 的平凡阈值足够大，保证 $e\le e'\le L\le1$，没有在 tube-KT 未覆盖的长度范围使用它。若切点导数为0，则曲线在该窗口只靠 Taylor 余项已落入 O(e) 球；任选方向、同样长度 tube 外罩即可，不需要除以小导数。若 Y 不闭，witness 距离可由 e 改成 2e；$C_0$ 一并吸收。

对 $Y\cap\mathrm{tube}$ 的每个半径 e' covering 球用 (4.1) 计算 preimages，得到

\[
 N_{e'}(Y\cap\mathrm{tube})
    \ge c\frac{\theta h}{d_0}\frac{\alpha R d_0}{e}
    \ge c\theta^D Q^{1/2}.                                  \tag{5.2}
\]

同一个实际 tube 的 tube-KT upper 则给

\[
 N_{e'}(Y\cap\mathrm{tube})
       \le K(L/e')^{1-\gamma}
       \le C K Q^{(1-\gamma)/2}.                            \tag{5.3}
\]

合并得 $Q^{\gamma/2}\le C K\theta^{-D}$。将固定常数保留在幂内、加大 C 吸收 Q 小和小样本分支，得到 (1.2)。没有从 (5.2) 中漏掉一个随 $d_0$ 改变的边界点数，也没有假设曲线达到最大振幅的位置恰在 B 上。

## 6. 对 root 修正版的交叉核验

已逐步读 `R0021_polynomial_tube_KT.md`。其 fixed-degree derivative bound、sublevel 的有限分支数、$d\ge c\theta$ 的单列、全局 good-preimage 计数、单 window averaging、$e'=C_0e$、$L=C_1\sqrt{Re}$ 和最终指数全部通过。近常 polynomial、D=1、小导数切点、有限 Y 网格均不产生新反例。

关键是管长与宽必须在同一次调用中匹配：曲率给 h²，而 KT 给 $(L/e')^{1-\gamma}$；若只使用长度1的 tube，将失去这里的平方根增益。也不能从某个 vector 分量导数下界直接宣布 vector curve 全局单射；原证明实际通过 scalar preimage 上界正确绕过了它。

根稿已经明确修正常数位置，本稿认证的是 (1.2)。第2节保留原式的严格失败记录，不追溯称原精确命题已证明。

## 7. 回到实际 cubic 前需要继续核的量

本有限引理不自动关闭 mixed32。实际产生的 cubic 是固定 degree，故允许 (3.1)；源任意 dyadic-Lipschitz slope 本身则没有被赋予这种二阶导数 bound。

应用时应只归一化 z-window，保持 Y 的 physical 尺度。设 $d_0=\delta/\rho$，必须由原 polynomial 在稠密样本上的 bound 加固定-degree 插值，先控制**整个窗口**的 R；不能以样本点间 diameter 替代它。若实际仅得到 $R\le K^C(\tau+\rho\Delta)$，则要显式核

\[
 d_0R\le K^C(\tau\delta/\rho+\delta\Delta)
                \lesssim K^{C'}\tau\rho+\rho\Delta.          \tag{7.1}
\]

allowed $\rho\ge\delta^{1/4}$ 给 $\delta/\rho^2\le\delta^{1/2}$；在 retained losses 指数足够小后，K 的固定幂可被这个余量吸收。这解释了 $e\ge d_0R$ 为什么可能成立，但 (7.1) 的 R upper、实际 tube-KT base resolution、原同一个 Y 和 graph mass 仍要从 source 逐项取得。

结论中的 $1/\gamma$ 费用要进入 $K=\delta^{-O(\text{loss}/\gamma)}$，固定常数 $C^{2/\gamma}$ 也只能在先固定 γ、再令 δ 小的顺序中吸收。后续 τ 稳定化、非零 scalar r、整列 b 慢变、consistency 和19.4 不属于本有限证明；等待 source 独审和实际应用稿再认证，不能把 PCT 本身登记为完整 quadratic 分支。
