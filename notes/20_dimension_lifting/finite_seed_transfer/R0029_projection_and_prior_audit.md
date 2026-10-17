# R0029：任意 ambient 的原方向、着色与四维有限输入

2026-10-17，子任务 A。已按恢复协议读 GOAL/STATE/ROADMAP/registry/latest round/AGENTS、R29 spec、R28 next，以及已有 SRC-001、DIR-003。唯一 main 是 quantitative finite seed；本稿不重开 projection+kernel 加维或 matrix action。首要问题是：三维角 Frostman 上界的有限方向族能否投影到 R⁴，保任意小损的方向数、分离、长度和原着色质量，再合法调用已有四维 finite readout。

**结论：该投影/删选接口成立，并可统一处理所有固定实角指数 s≥3。结合已有 SRC-001，可得到本稿 §7 的任意固定 ambient 有限 4−ε 下界，但它明确条件于整篇四维证明及 SRC-001 的正确性。不是由 Hausdorff 维数结论自动推出，也没有在本稿独立验证四维论文或 KT 完整递推。**

## 1. 有限输入、量词与停止条件

固定整数 ambient M≥4、空间 bound R、实数 s≥3、固定的 mark/tube 网格常数。δ∈(0,1/2)。有限 indexed unit-segment family T 位于 B_R⊂Rᴹ，方向在 projective sphere 上 δ-separated；每方向只留一个 index。对任意方向中心及 δ≤θ≤1，假定

\[
\#\{T\in\mathcal T:\angle(u_T,u)\le\theta\}
 \le K(\theta/\delta)^s,\qquad K\ge1. \tag{1}
\]

每个 J_T 是原 segment 上的 δ-time marks，或与该 segment 的固定 Cδ 邻域相交的原 δ-cells；第二种计数可先按最近线参数作常数重数删选，见 §5。均有 `#J_T≤C_{M,R}δ^-1`。E 为所有原 marked cells；所有扩大只用固定常数。

本稿先证明实际有限预算，不要求逐管 AD lower 或总方向数恰为 δ^-s。为调用种子，另设对某 η>0

\[
\#\mathcal T\ge\delta^{-s+\eta},\quad K\le\delta^{-\eta},\quad
 S:=\sum_T\#J_T\ge\delta^{-1+\eta}\#\mathcal T. \tag{2}
\]

输出须是原 indices 的子族，仅保原 marks；允许延长其 supporting lines 以适配共同 graph clock，不能把新增线段部分当着色。若只能保集合 a.e. projection 或需未经证明的 AD lower，则本步骤失败。下文直接给有限证明，所以不依普通 Hausdorff projection 定理。

## 2. 一般随机投影的有限碰撞引理

令 P:Rᴹ→R⁴ 的矩阵 entries 为独立标准实 Gaussian。取固定 `C_M` 足够大，使

    Pr(||P||>C_M)<1/32。

例如用 `E||P||_F²=4M` 和 Markov 即够。对任意 fixed unit u，Pu 是标准 R⁴ Gaussian，故选固定 c>0 足够小可使

    Pr(|Pu|<c)<1/128。

现在固定两个原方向，projective angle 为 θ∈(0,π/2]。改 v 的符号不影响 direction，可写

\[
Pv=\cos\theta\,Pu+\sin\theta\,H,
\]

其中 H 是与 Pu 独立的标准 R⁴ Gaussian。条件于 Pu，其正交补中的 `H_perp` 是标准三维 Gaussian。若 `||P||≤C_M` 且 projected projective angle 至多 aδ（a 为任意预定固定常数），则

\[
\sin\theta\,|H_\perp|
 =|\operatorname{proj}_{(Pu)^\perp}Pv|
 \le C_{M,a}\delta.
\]

因此三维 Gaussian 小球 upper 给

\[
\Pr\{\|P\|\le C_M,\ \angle(Pu,Pv)\le a\delta\}
 \le C_{M,a}\min\{1,(\delta/\theta)^3\}. \tag{3}
\]

这里只用 norm bound 把角度事件送入三维 perpendicular 小球，没有把 `||P||≤C_M` 当独立事件。Pu=0 的事件概率零；短方向稍后另删。(3) 也同时控制 projected 平行与反平行。

原 cap (1) 按 `θ≈2^jδ` 求和，对每个原 u 得

\[
\sum_{v\ne u}\Pr\{\|P\|\le C_M,\angle(Pu,Pv)\le a\delta\}
 \le Q:=C_{M,R,s,a}K\delta^{3-s}(1+\log(1/\delta)). \tag{4}
\]

小角部分确切的和为 `CK Σ_{j≤log₂(1/δ)}2^{j(s−3)}`；θ≥1 的部分用 projective sphere 的固定有限个 radius-1 caps 得 `#T≤C_MKδ^-s`，另付 `C_MKδ^{3-s}`。s=3 是 log 端点；s>3 可用更好的 geometric sum，但 (4) 对每个固定 s≥3 已足够。所有中心及所有原尺度的 cap 都只通过 (1) 使用一次，没有假设投影后的 cap 传承。

## 3. 同时保 nonshort 与 separated 输出

对任何 m 条原线的子族，上节的短方向期望数至多 m/128；在 bounded-P 事件上，collision graph 的总边数期望至多 mQ。分别用 Markov，可同时选一个 P 满足

\[
\|P\|\le C_M,\quad
 \#\{T:|Pu_T|\ge c\}\ge3m/4,\quad
 \#\{\text{projected angle}\le a\delta\text{ pairs}\}\le C mQ. \tag{5}
\]

比如三种失败概率之和可小于 1/2；没有要求每条线单独以高概率好再作全族 union bound。

在 nonshort vertices 中取 collision graph 独立集。由 `α(G)≥v(G)²/[2e(G)+v(G)]`（随机排序选局部最早点，再作 Cauchy–Schwarz），得到

\[
\#\mathcal T_*\ge c_{M,R,s,a}\,
 \frac{m}{K\delta^{3-s}(1+\log(1/\delta))}. \tag{6}
\]

所选 projected directions 两两距大于 aδ，且每个原 unit segment 的 projected length 至少 c。这是原 indices 子集，无额外 copies、重设 prior 或多重数遗漏。

特别，当 s=3 时仅损 `K log(1/δ)`。**输出在 R⁴ 的 separated directions 自动满足每个中心、所有尺度的三维 angular cap**：对固定 ρ≈δ，若分离至少 cρ，则

\[
\#\{T\in\mathcal T_*:\angle(Pu_T,e)\le\Theta\}
 \le C_{M,R}(\Theta/\rho)^3,\quad \rho\le\Theta\le1. \tag{7}
\]

这是 S³ 的球体积 packing，非只对随机中心或 dyadic centres。故不必先证明 arbitrary projected measure 的 uniform cap，再删各尺度坏点。投影 law 原本可有重数，(6) 正是支付该重数的步骤。

## 4. 平均 shading 到逐线：先删选再投影

设 (2) 成立。令 heavy family 为

    T_h={T:#J_T≥(1/2)δ^(-1+η)}。

轻线总质量至多 S/2。由每条线上界 `C δ^-1`，

\[
m:=\#\mathcal T_h\ge c_{M,R}\delta^\eta\#\mathcal T
 \ge c_{M,R}\delta^{-s+2\eta}. \tag{8}
\]

对整个 heavy family 一次使用 §§2–3。由 (6)、`K≤δ^-η`，

\[
\#\mathcal T_*\ge
 c_{M,R,s}\delta^{-3+3\eta}/(1+\log(1/\delta)). \tag{9}
\]

每一条输出仍保至少 `c δ^-1+η` 个原 marks，常数损失由下一节的 clock/cell 转换支付。这里不声称选出的线仍满足原逐点 AD lower；也不要求保旧每个 direction cap 的相对密度。

若 s=3，输出总 mark mass 至少

\[
S_*\ge c\,\frac{\delta^{2\eta}}{K(1+\log(1/\delta))}\,S. \tag{10}
\]

证明只需 `S≤Cδ^-1#T`、(8) 及逐线 heavy lower。因此三维角输入确实以任意小幂保原总 shading，而不只是保方向数。一般 s≥3 的同一预算另有自然 sampling 因子 `δ^{s−3}`；不能声称在从 δ^-s 条线减至 δ^-3 条线时仍保相同绝对总质量。所有情形都保近满的**相对逐线** marks，已足供 SRC-001。

## 5. 真 cell marks、graph clock 与端点

若输入 marks 是 tube 附近的 ambient δ-grid points/cells，先给每点一个距原 segment 至多 Cδ 的最近线参数。任一长度 δ 参数 bin 只对应 `C_M` 个原 cells，因为 segment 的这段 Cδ 邻域只覆盖固定多个 ambient δ-cubes。故改成 separated 参数 bins 至多损固定因子；所选真实线点仍在固定扩大 E 中。无需把整条 projected tube 的所有 cells 都加入 E。

在 (5) 后，选 projected direction 的最大坐标及其符号，只需八个固定 graph charts。有一个 chart 保 (9) 的固定比例。该坐标速度满足 `|e_0·Pu_T|≥c/2`，其余 slope 均固定有界。原参数间隔 δ 的 marks 在 projected time 的每个 ρ-bin（ρ=Cδ，C 预先固定）中只合并 `C_{M,R}` 个。因此每条仍有至少 `c δ^-1+η` 个 projected marked bins。

所有 projected points 位于固定 bounded ball。把其 time 范围分成固定有限个半开单位窗，每条线选 marks 最多的一个窗，再按窗 pigeonhole；每条及线总数各损固定因子。把该共同 clock 平移为 `[0,1]`。supporting line 可延长到整个 graph interval，`|b|+|v|≤R'=R'(M,R)`；只保窗内旧 marks。即使原着色集中在原 segment 端点，以上最多损固定因子，没有假设 interior shading，也没有给延长段新增 marks。

固定 angular threshold a 可事先取足够大，使最终 graph slopes 在工作网格 ρ 上 separated；projective direction 到本固定 chart 的 slope 是双 Lipschitz。所有后续坐标只是有限 orthogonal permutation、固定 translation、固定比例网格。

若 P bounded，则一个原 δ-cube 的像直径为 `C_M δ`，可用固定多个四维 ρ-cells 覆盖。最近线点的固定扩大、clock/bin center 移动也只增固定次数。因此最终 marked union E' 满足

\[
\#E'\le C_{M,R}\#E. \tag{11}
\]

以半径 C_Mδ 的 balls 计数甚至可对每个原 cube 只用一个 image ball；转换到固定四维 lattice 才有 (11) 的固定常数。没有 δ 的负幂增长。全部 marks 的实际支持包含于原 E 的固定扩大之像，故这是有用的 upper，不是把 union 换成另一更大的任意 shading。

## 6. 反攻与必要边界

1. 只说 projected direction 仍 3-Frostman 不够：原子 collision 必须删选。这里用 (3)–(6) 支付它；端点 s=3 的 log 不可在求和中漏掉。
2. 原 cap 必须控制**所有** centres、δ≤θ≤1；仅有总条数和 fine separation 时，directions 可集中到极小低维 cap，(4) 不成立。没有在此使用逐管/角 AD lower。
3. nonshort 是 projected length 和 time marks 的共同必要输入。若不删短方向，marks 可挤入一个 projected time-bin；(5) 以原 line count 保常数比例，重数删选后才进入 graph chart。
4. 平均 shading 先变 heavy lines，损失为 (8)。不能用“总质量近满”直接声称每条原线都有长 marks；也不能在每条线任意裁内核区间后假设着色仍长。
5. 本投影不增加输出维数、没有 kernel 免费加维结论，只把真实有限族送入已存在的四维有限命题。单独 (11) 和 direction packing 不能推出四维 finite lower；后者仍是实质数学输入。

## 7. 结合已有 SRC-001 的诚实条件推论

固定 M,R,s≥3 和目标 ε>0。**假设 SRC-001 精确的 finite readout 成立**，即其全部四维证明及输入正确。对目标 `σ=ε/2` 取得容差 `η_src>0`。先选 `0<η<η_src/10`，再取 δ 足够小以吸收本稿所有固定常数和 log。

由 (9)、§5 最终有 R⁴ bounded graph 族，网格 `ρ≈δ`、ρ-separated directions，且

    #T'≥ρ^(-3+η_src)，
    每条 #J'_T≥ρ^(-1+η_src)，
    #E'≤C_{M,R}#E。

因此 SRC-001 直接给 `#E'>ρ^(-4+σ)`。固定常数再由 `ε−σ>0` 吸收，得到

\[
\#E\ge c_{M,R,s,\varepsilon}\delta^{-4+\varepsilon}. \tag{12}
\]

(12) 对 (1)–(2) 的所有原 anchors/合法 finite shading 统一，不要求 directions 恰满 S³，也不要求逐线完整着色。所有实 s≥3 都已由同一碰撞和处理，不必先额外证明随机 thinning；把它放回 KT 对实 n=s+1 的 `K(n,d)` 记号时，原 ε、cap 费用和 saturation 的量词由 root/B 的原 KT 审计另核。

SRC-001 已在 R7 登记，本稿只拼其原结论，不把重读它称作新四维定理。DIR-003 是其加权方向版本；本证明所需 unweighted heavy/independent-set 路径已足够，不以 DIR-003 反过来掩盖投影 multiplicity。未从普通 Hausdorff 集合定理、投影 a.e. 或 compactness 推出 (12)。

## 8. 任意原条数的 DIR-003 推论与 unsaturated 预算

§§2–3 的投影 lemma 保留任意 m，没有借饱和总条数。若原平均 mark density 为 λ，即

    S≥λδ^-1 #T，  δ^η≤λ≤1，

则 heavy threshold 改为 `λ/(2δ)`，得到 `m≥cλ#T`。同一投影/clock 删选给

\[
m'\ge c\,\frac{\lambda\#\mathcal T}
 {K\delta^{3-s}(1+\log(1/\delta))},\qquad
\#J'_T\ge c\lambda\delta^{-1}. \tag{13}
\]

先固定 DIR-003 的目标损失 ε_D，再取 `η<η_DIR/2`，small δ 使每条满足其 long-mark 门槛。输出 separation 使每个 slope δ-cube 的 unit index 总权 `α≤C_{M,R}`。故 **已有** DIR-003 给

\[
\#E\ge c_{M,R,s,\varepsilon_D}
 \frac{\lambda^2\#\mathcal T}{K(1+\log(1/\delta))}
 \delta^{s-4+\varepsilon_D}. \tag{14}
\]

两个 λ 分别来自平均转 heavy 条数及每条保留 marks，不可只记一个。`λ≥δ^η`、`K≤δ^-η` 时，除 log 外的额外费用是 δ^{3η}。依次取 `ε_D` 和 η 足够小并吸收 log，(14) 给 `#E≥c#T δ^{s-4+ε}`，这正是把 finite 4−ε 种子放入 unsaturated direction collection 所需的按原条数比例形式；原 KT (40) 的精确参数转换仍由 root/B 另核。

这个推论继续条件于 DIR-003→SRC-001→完整四维 proof，不是重证 R9 或用饱和输出暗代任意原条数。

本轮子任务完成的是实际 finite 投影/删选及 conditional seed 接口。四维主证明、高级源全部正确性和 KT 递推的完整应用仍须明列条件；一般 Kakeya、五维新界、六维 17/4 的最终有效性/最新前沿/新颖性均未由本稿单独认证。
