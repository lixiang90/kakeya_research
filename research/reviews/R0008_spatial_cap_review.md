# R0008：平滑全宽度 spatial cap 独立审查

日期：2026-10-17。审查者：audit_four_dimensional。被审稿：`notes/40_multiscale/plank_inputs/R0008_smoothed_all_width_cap.md`。审查范围：在 R0007 已核验的 all-frame 格点计数输入之上，逐步审查概率归一化、六系数噪声、全部宽度、短时间窗和一般固定 chart matrix。没有重新独立证明 R0007 整个 quadric cap，也没有审查本轮 horizon 主结论。

结论：§§1–5 的 (0.1)–(0.3) 推导成立；§6 的同先验与支配关系说明成立。(6.1) 须按其 whole-unit-time、单位 chart slack 的简写理解，具体范围见下文第6节。

## 1. 概率权与 R0007 反例权不同

当前参数 grid 有 \(N_\delta\asymp\delta^{-3}\) 个 indices，每个概率 \(\pi_i=N_\delta^{-1}\asymp\delta^3\)。R0007 的 count 输入是

\[
 \#\{i:M_i\subset P_W\}
 \le C\delta^{-1/2}\delta^{-3}\prod_jW_j
 \qquad(\delta\le W_j\le C_0).
\]

乘本轮 \(\pi_i\) 后正好得到 \(C\delta^{-1/2}\prod_jW_j\)。不存在遗失 \(\delta^3\)、把 R0007 的反例权 \(\delta^{1/2}\) 当成概率，或条件化到命中 indices 后重新归一化的问题。它与 `R0008_smoothed_quadric_prior.md` 的统一可见模型一致：每个 \(b,u\) 坐标独立加 \(U[-\delta,\delta]\) 噪声。

## 2. 宽轴 clipping 的量词与常数

全部支撑轨道有统一位置上界 \(|Y(t)|\le R\)。若原 plank 含任一支撑轨道 \(Y_*\)，则任意另一命中轨道满足每轴

\[
 |n_j\cdot(Y-Y_*)|\le \min(2w_j,2R).
\]

所以只需对一个同 frame、affine 中心 \(Y_*\)、半宽 \(v_j=\min(2w_j,2R)\) 的固定有界 plank 使用旧输入。\(v_j\le2w_j\)，宽度排序保留；当原 \(w_j\ge\delta\) 时，\(v_j\ge\delta\) 对足够小 \(\delta\) 成立。故乘积至多放大8倍，输入常数仅依赖固定 \(R\)，不依赖原 widths 或原 center 的大小。

这里选 \(Y_*\) 只是为了证明对任意 plank 的数值上界；新中心仍是原 all-center 计数允许的 affine center，无需把该选择编码为 observation label。空命中事件直接给零。

## 3. 旋转薄轴因子不需要旋转后的独立性

固定 index 和 velocity noise 后，whole-time inclusion 的必要条件在 \(t=0\) 仅约束 \(\xi_b\)。其原三维 joint density 是 \((2\delta)^{-3}\)，旋转后 Jacobian 为1，support 位于半径 \(\sqrt3\delta\) 的球内。球与任意移位正交框交的体积至多

\[
 C\prod_j\min(w_j,\delta).
\]

因此每个 index 的命中概率统一不超过

\[
 C\prod_j\min(1,w_j/\delta).
\]

这由 joint density 与体积得到，没有把旋转后三个噪声坐标错误地视为独立。\(\xi_b\) 与 \(\xi_u\) 在原模型中独立，所以固定 \(\xi_u\) 后的同一上界可以直接积分回原 \(\xi_u\) law。

## 4. 统一 eligibility 后才能乘薄轴因子

对任意可能的噪声实现，\(\sup_t|\xi_b+t\xi_u|\le2\sqrt3\delta\)。若 noisy line 命中原 \(P\)，其 grid center line 必然属于同一 frame/center 的 \(P^+\)，宽 \(W_j=w_j+2\sqrt3\delta\)。这个必要 index 集合在求概率前已经固定，不依赖某个命中噪声或后选 conditional law。

因而可逐 index 先用第3节概率 upper，再对同一个 \(\pi_i\) 求和。利用第1–2节，得到

\[
 \begin{aligned}
 \nu_{\rm vis}(P)
 &\le C\prod_j\min(1,w_j/\delta)
       \sum_{i:M_i\subset P^+}\pi_i\\
 &\le C\delta^{-1/2}
       \prod_j\left[(w_j+2\sqrt3\delta)
                         \min(1,w_j/\delta)\right]\\
 &\le C\delta^{-1/2}\prod_jw_j.
 \end{aligned}
\]

最后一项逐轴成立，故同时覆盖一、二、三个薄于 \(\delta\) 的轴，不要求 widths 有统一正下界。输入扩大后的宽度均超过 \(\delta\)，大于固定支撑范围的轴则由第2节处理。全宽度 clipping 与薄轴概率因子没有留下未覆盖的中间区间。

## 5. 短块外推与一般 \(D\) 的原 determinant

令 \(I=[\tau,\tau+q]\subset[0,1]\)。固定 frame、固定 affine center 下，每轴偏差 \(f_j(t)\) 是 affine。由两个端点插值，\(\sup_I|f_j|\le w_j\) 蕴含 \(\sup_{[0,1]}|f_j|\le3w_j/q\)。代入已经对全部正宽度证明的 fulltime cap，便得

\[
 \nu_{\rm vis}(P_I)\le
 C\delta^{-1/2}q^{-3}\prod_jw_j.
\]

这里三个空间轴分别贡献一个 \(q^{-1}\)，没有额外的 time-probability 因子；上式计算的是轨道 prior 概率，尚未乘 incidence time。若只在零散 selected incidences 上命中，没有 whole-block assignment，则该端点外推不能使用。

对于固定 invertible \(D=U\Sigma V^T\)，若 \(\sup_I|D^{-1}(Y-y_c)|\le K\)，则左奇异 frame \(U\) 的每轴半宽可取 \(C K\sigma_j\)。所以

\[
 \prod_jw_j\le C K^3\prod_j\sigma_j
   =C K^3|\det D|.
\]

此处 \(J=|\det D|\) 始终是同一个原坐标 chart 的 determinant；没有将外包框或 clipping 后的新体积误记为原 \(J\)。无需假定 \(D\) 的轴长度大于 smoothing scale，亦无需 \(\|D\|\le Kq\) 才能使用这个 upper。

## 6. 同 prior 与 (6.1) 的简写范围

上述 upper 对任意未归一化 submeasure \(\widetilde\nu\le\nu_{\rm vis}\) 保持；若仅有 \(\widetilde\nu\le D_0\nu_{\rm vis}\)，右侧乘 \(D_0\)。若条件化为 \(\nu_{\rm vis}(\cdot\mid G)\)，则必须除以原 \(\nu_{\rm vis}(G)\)。

被审稿 (6.1) 的 \(C\delta^{-1/2}J/\nu_{\rm vis}(G)\) 可读作 full unit time、单位 slack，且 \(J=\prod_jw_j\) 的示例。它不是任意短块 chart 的完整公式；一般情形应保留

\[
 \nu_{\rm vis}(P_I\mid G)
 \le \min\left(1,
    \frac{C K^3\delta^{-1/2}q^{-3}|\det D|}
         {\nu_{\rm vis}(G)}\right).
\]

这是对 (6.1) 记号范围的澄清，不影响前述 (0.1)–(0.3) 的证明。加入独立 hidden 参数之后，visible projection 仍为此同一 \(\nu_{\rm vis}\)；任意 selected incidence measure 被原 product prior\(\times dt\) 支配，但不能先按 selected event 归一化，再免费调用本 cap。

通过本次审查的仅是这组几何概率 upper。任意二次测试的 hidden sublevel、典型 pure-density floor、true-chart 质量比较与 horizon 结论仍需分别审查；本文不据几何 cap 自行宣布 generic \(H\le L\) 已被否定。
