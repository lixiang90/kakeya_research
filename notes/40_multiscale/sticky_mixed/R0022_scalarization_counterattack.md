# R0022：保留时间的 weighted rich-triple scalarization

2026-10-17，`lifting_obstructions`。任务为 LOCAL-AFF 的有限门槛，不重做 PCT、mixed42 或旧 W/BSG。已读 R22 spec、R21 handoff、恢复文件。本文证明一个有限原权版本；它本身不是完整 source affine alternative 或 Kakeya 结果。

## 1. 精确定理：vertical 输入、Euclidean scalar 输出

设 T⊂[0,1] 为有限时间集，ν 为其任意原概率权重；不要求等权。固定 d∈(0,1]、K_t≥1，假设对长至少 d 的任意 interval I，

\[
                         \nu(I)\le K_t|I|.                  \tag{1.1}
\]

令 F:T→R^m 是某个 [0,1] 上 L-Lipschitz 函数的限制；也可只要求 T 上同样的 pairwise Lipschitz bound。设 h>0，所有 R,U∈R^m 的 vector vertical affine fits 满足

\[
          \nu\{t:\ |F(t)-Rt-U|\le h\}\le a.                 \tag{1.2}
\]

取 λ 在固定 cube [1,2]^m 中均匀分布，Π_λ(t,F(t))=(t,λ·F(t))。令 Bad_b 为存在**任意**二维 affine line ℓ，使

\[
             \nu\{t:\Pi_\lambda(t,F(t))\in N_w\ell\}\ge b.  \tag{1.3}
\]

此处 N_w 是 Euclidean w-neighborhood，允许 ℓ vertical、倾斜或斜率极大。这个 Lip 版本是独立有限定理；原 source 仅有 dyadic Lipschitz，不能未经支付就套用。实际所需无 Euclidean Lip 版本另在第6节。存在只依赖 m 的 C_m，使当

\[
               b\ge C_mK_t(d+w),\quad 0<b\le1,              \tag{1.4}
\]

有

\[
 \mathbb P_\lambda(\mathrm{Bad}_b)
       \le C_m b^{-3}\left[a+\frac{(1+L)w}{h}\right].         \tag{1.5}
\]

特别，右边<1 时存在一个有界且范数不趋零的 λ，使**所有** scalar affine tubes 的原质量均<b。若 scalar 输出从一开始就是 vertical strip，则 (1+L) 可去掉，且 (1.4) 只需 b≥C_mK_td。原时间权不变，没有对无限 R,U 做 union bound。

## 2. Rich tube 的时间 gap 与垂直化

设某 λ 有 (1.3) 的 rich set S，记 β=ν(S)≥b。取

\[
                            g=\frac{b}{1000K_t}.
\]

加大 (1.4) 的常数可保 g≥d 及 w≤g/16。若 S 的所有时间落在长 g 的 interval 中，则 (1.1) 给 β≤K_tg<b，矛盾。所以存在 S 中两个时间相距≥g。

写 scalar tube 的单位法向为 (n_0,n_1)。scalar function λ·F 的 Lipschitz 常数≤2√mL。对上述两时刻相减，得到

\[
        |n_0|\le2\sqrt m L|n_1|+2w/g.
\]

因 |n_0|+|n_1|≥1、2w/g≤1/8，可推出

\[
 |n_1|\ge\frac{c_m}{1+L}.
\]

因此 rich set 全部满足一个 scalar vertical fit

\[
            |\lambda\cdot F(t)-rt-u|\le W,
            \qquad W=C_m(1+L)w.                            \tag{2.1}
\]

这一步单列排除了垂直 rich tube，也支付了 Euclidean width 与 vertical error 的区别。不能不经此步就把任意斜管当作宽 w 的 vertical strip。若输入输出本来使用 vertical strip，可直接令 W=w，完全不需要该垂直化条件。

## 3. 同一原质量下有 b³ 个分离 triples

在原乘积 ν³ 上，S³ 的质量为 β³。对任意一对时间，间距<g 的 S³ 质量至多

\[
     \beta^2\sup_t\nu([t-g,t+g])\le2K_tg\beta^2.
\]

三对求和至多 6K_tgβ²≤β³/100。删除这些 triples 后仍保固定比例 β³。按三时刻的六种顺序分解，得到

\[
 \nu^3\{t_1<t_2<t_3,\ \min_{i\ne j}|t_i-t_j|\ge g,
                    \ t_i\in S\}\ge c b^3.                 \tag{3.1}
\]

这是原 weights 的结论；没有把 S 归一化后免费赋予 AD。条件 g≥d 使离散 atoms 和网格边界都已由 (1.1) 计入。

对一组有序 triple 定义**中间点**的 vector residual

\[
 V(t_1,t_2,t_3)=F(t_2)
      -\frac{t_3-t_2}{t_3-t_1}F(t_1)
      -\frac{t_2-t_1}{t_3-t_1}F(t_3).                       \tag{3.2}
\]

两个系数非负且和为1。故 (2.1) 对三点成立时，

\[
                         |\lambda\cdot V|\le2W.             \tag{3.3}
\]

这里**没有 1/g 损失**。关键是用 ordered middle point 的凸插值残差，而不是一个无序端点外推残差。

## 4. 小 vector residual 和随机 λ 的实际概率

固定 t_1<t_3，经过 F(t_1)、F(t_3) 的 vector affine function 记为 A_13(t)。由 (1.2)，

\[
               \nu\{t_2:|F(t_2)-A_{13}(t_2)|\le h\}\le a.
\]

限制 t_2 在两端之间、再限制 gap 只会减质量。所以全部 ordered triples 中 |V|≤h 的原质量至多 a。

对 |V|>h，选坐标 j 使 |V_j|≥|V|/√m。固定其他 λ 坐标后，|λ·V|≤2W 允许的 λ_j 区间长至多4W/|V_j|。λ_j 在 [1,2] 均匀，故

\[
 \mathbb P_\lambda\{|\lambda\cdot V|\le2W\}
                        \le\min(1,C_m W/h).                 \tag{4.1}
\]

令 T(λ) 为 gap≥g、ordered triples 满足 (3.3) 的 ν³ 质量。Fubini 给

\[
                       \mathbb E T(\lambda)\le a+C_mW/h.    \tag{4.2}
\]

而 Bad_b 蕴含 T(λ)≥cb³，由 (3.1)。Markov 得 (1.5)。T 是有限 triples 对 λ-slabs 指标的加权和，可测；Bad_b 也可按有限 time subsets 的 rich-line 可行性表示。不存在针对所有 adaptive lines 的未经支付的无限 union。

该证明甚至不需要 vector F 有二阶导数；Lip只用来将 Euclidean scalar tubes 垂直化。vector residual 较小的部分严格调用原 vector affine nonconcentration，不以“向量不集中”口头代替。

## 5. 可直接使用的选择量与误差版本

例如，只要

\[
 b\ge C_m\left\{K_t(d+w)
            +\left[a+\frac{(1+L)w}{h}\right]^{1/3}\right\}
\]

且右边小于1，适当加大 C_m 就可取 good λ。这里不是声称三次方根 sharp，而是给足以检验 source 参数的明确费用。

若实际观察点为 $(\widehat t,\lambda\cdot\widehat F)$，但仍保原 time index 与原权，并满足

\[
       |\widehat t-t|\le d_{\rm round},\qquad
       |\widehat F-F(t)|\le e_{\rm round},
\]

则将输出宽替换为

\[
                 w_{\rm eff}=w+d_{\rm round}+C_m e_{\rm round}
                                                                    \tag{5.1}
\]

即可应用同一定理。这里不删除或重新均匀化同一个 coarse cell 中的重复 original indices。若只知道 rounded F 的 vector fit upper，而使用 true F 的 Lipschitz bound，则还要把 h 缩到 h−e_round；h≤e_round 时不能免费传回。

若原时钟窗口长ρ，需先明确 t=(z−z₀)/ρ、d=δ/ρ，所有原时间概率都 pushforward，(1.1) 的 K_t 由实际 density/packing支付。对 F 的 vertical normalization 也必须一致：若 B 的 vector block 除 L_fρ，则 observed A 的 ξ block 也要除 L_fρ，才能保持同一线性增量式。只在 B 一边除 L_f 会改变原 relation；原 source 该 normalization 的修复由 A/root 另稿审计，本有限定理不替代它。

## 6. 仅有 bounded range 的 source 可用版本

原 source 的 f 只在同一 allowed dyadic cell 中有 oscillation upper，跨相邻 cell 的跳变不能直接给上面用过的 Euclidean L-Lipschitz bound。本节完全删除该假设：只要求 finite F 的直径≤M，保 (1.1)、(1.2) 和原时间权。

同样令 g=b/(1000K_t)，假设 b≥C_mK_t(d+w)。rich Euclidean tube 中取 gap≥g 的两点，scalar值之差至多2√mM。因此单位法向满足

\[
 |n_0|g\le2\sqrt mM|n_1|+2w,
 \qquad |n_1|\ge\frac{c_mg}{1+M}.
\]

rich tube 于是包含在一个 vertical band 的原像中，其宽可取

\[
                  W=C_m(1+M)\frac{w}{g}.
\]

第3–4节原 weighted triples 的计数、固定 endpoints 的 vector residual upper 和随机 λ 小球概率均不使用 Lipschitz。因此得到

\[
 \boxed{\quad
 \mathbb P_\lambda(\mathrm{Bad}_b)
   \le C_m\left[\frac a{b^3}
       +\frac{(1+M)K_t w}{h b^4}\right].\quad}               \tag{6.1}
\]

这次 gap 费用真实地留在 Euclidean tube 垂直化中。ordered middle residual 本身仍无 1/g：不能将这两项混为同一个无损论断。若 scalar 输出是 vertical band，则不需要本次垂直化，也仍有第1节的较强 a+w/h 版本。

例如，假设 source 已支付归一化后 M≤1、a≤ρ^{2θ}、h≥K⁻¹ρ^{ε₀}、w≈ρ^{8ε₀}、K_t≤K，且每个 K 的损失指数相对 θ、ε₀、µ 足够小。取

\[
            \beta=\frac{\min(\theta,\epsilon_0)}{100},
            \qquad b=\rho^\beta.                            \tag{6.2}
\]

则 a/b³≤ρ^{2θ−3β}→0，另一项≤K²ρ^{7ε₀−4β}→0。若 d=δ/ρ、ρ≥δ^{1/4}，有 d≤ρ³，故 b≥CK_t(d+w) 也可满足。必须保留 min 外的固定小因子：若误取 β=min(θ,ε₀/100)，当 θ 很小时 β=θ，a/b³ 不趋零。

coarse rounding 仍用 (5.1)。若 d_round、e_round≤Kρ，而8ε₀<1，则把它们付入 w_eff 后仍有 w_eff≈ρ^{8ε₀}。这要求 explicit cover error；不允许用不存在的 Euclidean Lip bound 由 |t−t̂| 小自动宣称 |F(t)−F(t̂)| 小。

本节参数只是已支付相应实际输入时的量化示例，不替代 source 的 A/B/ABC 图及其 loss 证明。

## 7. 任意 A 的免费 projection cardinality 仍为假

给一个即便“集合意义上是 graph”也会失败的有限例子。取 r=1/n，枚举 ξ_j∈(rZ∩[0,1))³ 的 n³ 个点，令

\[
 x_j=j r^4/10,\qquad
 A=\{(x_j,\xi_j):0\le j<n^3\}\subset\mathbb R\times\mathbb R^3.
\]

x_j 全部不同且都在 [0,r/10] 内，所以 A 是一个函数的有限 graph。但 ξ 网格使

\[
                       N_r(A)\asymp r^{-3}.
\]

对任意有界 λ，Π_λA 的第一坐标都在同一个 O(r) 区间，第二坐标在固定有界区间，故

\[
                      N_r(\Pi_\lambda A)\lesssim r^{-1}.      \tag{7.1}
\]

因此没有为任意 A 或仅凭“graph”名称免费保 cardinality 的 bounded λ。这个 A **不满足**下段 coarse first-coordinate fibre cap，也没有声称是 source observed A；不能据它否定 root/A 从原 ξ coherence 证明的额外结构。

反之，若每个 r-first-coordinate bin 上，A 至多有 M 个 r-cells，则 Π_λ 保留第一坐标，立即给

\[
                   N_r(\Pi_\lambda A)\gtrsim M^{-1}N_r(A),   \tag{7.2}
\]

固定维数和 bounded λ 只付常数。理由是 image 的每个 r-ball 只跨 O(1) 个 first-coordinate bins，而每个该 bin 原来只有 M 个 r-cells。不需要 ξ 关于 x 全局 Lipschitz，也不需要随机 generic projection。

(7.2) 本身只是 covering，不把任意原权变成 uniform image law。若 A 的 r-cell 先验等权，则 image r-cell 的 preimage multiplicity≤C M，因而每 cell 的 pushforward atom≤CM/#A；非等权时须继续保原质量或另作已支付的 heavy-bin 选择。这是 actual observed graph 接口仍要单独核的部分。

## 8. 对本轮 source 目标的意义与停止点

本稿已证明新的有限 scalarization 门槛，且可处理全部 adaptive scalar affine tubes、原 time weights、离散 atoms、有限网和小舍入误差。若额外有 Euclidean Lip，gap 的费用只在 time deletion 和垂直化条件；实际 source 仅用 bounded range 时则明确支付 (6.1) 的 K_tw/(hb⁴)，不能引用前一个版本漏掉该项。两种情况下 ordered middle residual 均不产生额外 1/g。

没有在此证明 LOCAL-AFF。actual A 的 first-coordinate fibre cap、同一 A/B normalization、原 graph coarse 权重、scalar ABC 参数区间、删 times 后跨时间 Y-union AD 与 whole-velocity lower 都仍须由原 source 审计和 root 证明承担。若这些接口不给上述量化小量，不得把 finite 门槛单独升级成实际全局 affine alternative。主 mixed32 和最终 Kakeya Goal 保持原完成标准。
