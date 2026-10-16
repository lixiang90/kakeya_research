# R0009：加权方向归约及 source 范围的独立审查

日期：2026-10-17。审查者：audit_four_dimensional。被审稿：`notes/40_multiscale/plank_inputs/R0009_weighted_direction_reduction.md`。只读审查该稿，并核对本地四维论文 Proposition 2.16、Theorem 2.17、Lemma 2.13；未修改被审稿。独立核查范围包括同色任意代表、重复与任意权重、source §§5.1–5.3 的量词，以及 visible/full-slope 两个 Jacobian。

结论：WDR 是正确的有限组合归约；source 的专用调用与一般 group/residual 调用边界区分正确，两个斜率密度变换也正确。WDR 的几何输入仍为 U；由 SRC-001 得到 U 的放大稿是我本人编写的另一份证明，**本 review 不把自己对该部分的使用登记为独立复核**。完整正向结论仍条件于 SRC-001，进而条件于完整四维证明及其输入正确。

## 1. 同色任意代表确实方向分离

在 side-\(\delta\) slope cubes 的 index 上作模 \(m\) 染色。同色不同 cubes 至少有一个坐标的 index 差为 \(m\) 的非零倍数，故其中任意两 slopes 的距离至少 \((m-1)\delta\)。bounded chart 上

\[
 \Theta(v)=\frac{(1,v)}{\sqrt{1+|v|^2}}
\]

有统一 Lipschitz 逆，因而取固定 \(m=m(R)\) 可保证所需单位方向分离。若采用 projective metric，所有方向的正时间分量有统一正下界；对足够小 \(\delta\)，也不会发生近 antipodal 混淆。颜色数只依赖固定 chart。

因此每个非空 bin 中确可**任意**选一个原 index，包括极小权重的 index。选取保留该 index 自己的完整 mark set，而不是把同 bin 其它 lines 的 marks 嫁接到它上面。逐线 marks 下界对所有原 indices 都成立，所以代表自动符合 U 的下界。代表 footprint 是原 \(E\) 的子集。

## 2. 确定性加权步骤没有暗藏总质量或最小权重条件

固定颜色的 occupied-bin 数为 \(M_c\)。U 给

\[
 M_c\le C_0\delta^{1-\varepsilon_0}\#E_c
      \le C_0\delta^{1-\varepsilon_0}\#E.
\]

同色所有原 indices 的实际加权访问量满足

\[
 \sum_{i\text{ in color }c}\omega_i\#J_i
 \le \delta^{-1}\sum_{Q\text{ in color }c}\beta_Q
 \le \delta^{-1}\alpha M_c
 \le C_0\alpha\delta^{-\varepsilon_0}\#E.
\]

求和有限个颜色即得 WDR。这里仅以 \(\#J_i\le\delta^{-1}\) 作一次共同 upper，不要求各代表 marks 与同 bin 其他 indices 的 marks 一样多。下界用于 U，上界用于加权总和，角色没有混淆。

重复 indices 只增加某个 \(\beta_Q\)，其总和仍受 \(\alpha\) 约束。极小正权只会让原 footprint 可能增大；代表本来就在该 footprint 中，所以不会引入任何反向损失。原 index 数可以任意有限；抽出的代表数至多为 bounded chart 的 \(O_R(\delta^{-3})\) 个 bins，不需要原 index 数是一个固定 \(\delta\) 幂。

## 3. 可选抽样与极小总权边界

被审稿的 sampling 定义给每个 index 精确纳入概率

\[
 (\beta_Q/\alpha)(\omega_i/\beta_Q)=\omega_i/\alpha.
\]

因为 \(0<\omega_i\le\beta_Q\le\alpha\)，这是合法概率；每 bin 至多选一条，每个非空 outcome 符合 U，空 outcome 的相应不等式为零。可以对逐 outcome 的 \(M_{\rm sample}\le C_0\delta^{1-\varepsilon_0}\#E\) 直接取期望，无需期望样本数大于1、无需 concentration，也无需把总权归一化。再用每条最多 \(\delta^{-1}\) 个 marks，得到与确定性证明相同的 bound。

故任意权重跨度、\(\sum_i\omega_i\ll\alpha\)、大量重复及 \(\alpha=0\) 的空 family 边界都处理正确。这个可选抽样没有给主证明增加新的假设。

## 4. 方向单位及容差

\(\eta\le\eta_0\) 时，\(0<\delta<1\) 给 \(\delta^{-1+\eta}\ge\delta^{-1+\eta_0}\)，所以原逐线条件足以调用 U。有限 coloring 不改变 mesh，也不消耗额外的 \(\eta\)。使用 \(\varepsilon_0\le\varepsilon\) 后，\(\delta^{-\varepsilon_0}\le\delta^{-\varepsilon}\)；主任务可留出余量处理其它固定或 subpower 成本。

物理方向 measure upper \(\nu_V\le A\,dv\) 确实推出每个 side-\(\delta\) bin 的质量至多 \(A\delta^3\)。代入的是 \(\alpha=C A\delta^3\)，不是 \(A\)。反向把 arbitrary finite bin cap 称为实际 Lebesgue density upper 则不成立，被审稿未作此反向使用。

单 bin 总权 \(m\) 时必须 \(\alpha\ge m\)；均匀单位质量约 \(\delta^{-3}\) 个 bins 时 \(\alpha\asymp\delta^3\)。R0008 的大物理 ceiling \(A\asymp\delta^{-1}\) 若被调用，必须显式付出该幂成本，不能被 conditional angular exponent 代替。

## 5. Source 专用 zero-depth 调用的范围正确

原论文 Theorem 2.17，PDF pp.21–22，(2.26)–(2.28)：原 full-slope smoothing 给 subpower density upper；visible marginal 的 upper 通过积分 bounded hidden-slope range 获得。五维拟版 visible slope 为三维，因此细 mesh \(\rho\) 的原始未归一化 bin 质量应为 \(C A\rho^3\)。对原轨道先验作未归一化 restriction 保留该 upper；任意 current incidence restriction 只被原 product prior\(\times dt\) 支配，不会产生免费的 conditional probability law。

被审稿 §5.1 明确把 finite weighted approximation、preserved bin upper、long duration 和固定 cell enlargement 作为调用前提。这是适当的边界，未将连续 source 到有限 family 的整个编码过程宣布为本组合 lemma 的推论。

三维 visible base 在 time 一起为四维。若 source 有原 whole-cell density lower \(N_0^\kappa\)，则 visited cell count 与 long-duration mark numerator 正确给出 raw multiplicity lower

\[
 K_0^{-C}N_0^\kappa\rho^3.
\]

方向版 upper 为 \(C_\varepsilon A\rho^{3-\varepsilon}\)。对于 \(\rho=N_0^{-D_*}\)，两者可在 \(A\le N_0^{\beta+o(1)}\)、\(\kappa>\beta\) 时，以 \(D_*\varepsilon<\kappa-\beta\) 的余量排斥。subpower \(A\) 恢复专用 zero-depth 上界；大 \(A\) 只能给 shifted 上界。不能据此补足 generic group/residual 的所有用途。

固定 bounded chart 是实质输入。subpower 大范围必须先分 chart、作有限变换并计入相应 subpower cell 成本；稿中已经说明，未声称 \(C(R)\) 对变化的 \(R\) 自动一致。

## 6. Visible 与完整 slope 的 Jacobian 分别核算

固定 parent normalization

\[
 t=t_c+q\tau,\qquad Y=y_c(t)+D Z,
 \qquad J=|\det D|,
\]

visible velocities 满足

\[
 V_{\rm old}=y_c'+(D/q)V_{\rm new},
 \qquad dV_{\rm old}=(J/q^3)\,dV_{\rm new}.
\]

条件于完整 parent assignment \(A_{\rm parent}\) 后，未归一化 marginal 被原 marginal 支配，再除以 \(\nu(A_{\rm parent})\)，因此

\[
 A_{\rm new}\le
 \frac{A J}{q^3\nu(A_{\rm parent})}.
\]

version 2 保留 hidden coordinate \(w\)。沿新时间的 hidden velocity 为 \(W_{\rm new}=qW_{\rm old}\)，因此旧完整 \((V,W)\) 相对于新完整 slope 的 Jacobian 另多 \(q^{-1}\)：

\[
 C_{\rm full,new}\le
 \frac{C_{\rm full,old}J}
      {q^4\nu(A_{\rm parent})}.
\]

两式均与原 Lemma 2.13 的坐标变化一致。不能将完整 slope 的 \(q^{-4}\) 用作 visible marginal 的成本；积分完整 bound 时须跟踪 hidden-slope range，新的 \(W\) 范围也缩短了 \(q\) 倍。稿中保留了这个提醒。

若 true parent 使 \(\nu(A_{\rm parent})\) 与 \(n(b)J\) 可比，仍分别留下 \(1/[n(b)q^3]\) 或 \(1/[n(b)q^4]\) 的成本。真实 floor 不会自动使它们 subpower。

## 7. Greedy residual 的比较没有冒充空间框抽取

原 Proposition 2.16，PDF pp.18–20，(2.20)–(2.23)，在一个 block 中用旧轨道先验在 \(G\) 内的**未归一化** restriction。拟版 \(j=3\) 除空间以 \(Rq\)、除时间以 \(q\) 后，\(V_{\rm new}=V_{\rm old}/R\)，所以可见 direction-density upper 是 \(A R^3\)，不含免费的 conditional \(\nu(G)^{-1}\)，也不能误写成原 \(A\)。

由 (2.21) 的原 whole-cell witness，令 \(m_G\) 为原 normalized **incidence** mass、\(m_{\rm ret}=\theta m_G\)，则原 marks 与 cell count 给

\[
 \frac{\sum\omega_i\#J_i}{\#E}
 \gtrsim\theta N_0^{-\xi/4}n(L)(Rq)^3\rho^3.
\]

与方向 upper 比较后约去 \(R^3\rho^3\)，正好得到稿中的

\[
 n(L)q^3\lesssim C_\varepsilon\theta^{-1}
                 N_0^{\xi/4}A\rho^{-\varepsilon}.
\]

这里 \(\theta\) 为 inverse-subpower 是原 weighted averaging 挑出的有利 group 的结论，**不是任意单个 group 都有相同 retained fraction**。按该源选择理解，§5.3 的使用正确。该式仅比较已有方向成本、密度与时间尺度；它没有输出某个空间 plank 的质量/体积比，因而不能替换原 (2.23) 对 greedy stopping 的反证。

被审稿因此恰当地没有声称：修复 generic \(j=3\) 的 \(H\le L\)、排除 HOR-001、或建立 source 受限优化类在 normalization/coarsening/completion 中闭合。这些边界与已证范围一致。
