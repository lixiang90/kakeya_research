# R0029 独审：投影、原遮蔽与 KT 稀疏种子转移

2026-10-17，审查者 `/root/lifting_obstructions`。独立逐式读取：

- `notes/20_dimension_lifting/finite_seed_transfer/R0029_projection_and_prior_audit.md`（A，含 §8 任意条数形式）；
- `notes/20_dimension_lifting/finite_seed_transfer/R0029_conditional_seed_and_six_dimensional_bound.md`（root，§1–7）；
- 既有 `results/reviewed/SRC-001_direction_rich_finite_readout.md`、`DIR-003_weighted_direction_mass_input.md`；
- KT 原文 Definitions5.1、5.2、6.1、Theorem6.2、Lemma6.6–6.7 及相关 proof 调用位置。

**结论：有限 Gaussian 投影、删选/原 marks、任意条数两次密度预算及其 KT 参数接口通过本次内部独审。六维 17/4 始终条件于完整 OAI4/SRC-001/DIR-003 的正确性及具名 KT6.2，没有在本次重证完整高级源；未经外部同行评审，也未认证新颖性或无条件新维数界。**

## 1. 概率引理：三维小球及所有原角尺度

固定 projective directions u、v，将夹角 θ 取在 [0,π/2] 并改 v 符号，有

\[
Pv=\cos\theta\,Pu+\sin\theta\,H,
\]

H 与 Pu 为独立标准 R⁴ Gaussian。条件于 Pu，其三维 perpendicular component 是标准 R³ Gaussian。若 ||P||≤C_M 且投影夹角≤aδ，则

\[
\sin\theta\,|H_\perp|
 =|\operatorname{proj}_{Pu^\perp}Pv|
 \le C_{M,a}\delta.
\]

因此交事件概率≤Cmin(1,(δ/θ)³) 正确；未将 ||P||≤C_M 当独立 conditioning。Pu=0 为零概率事件，θ 接近 π/2 时也有 sinθ≈θ。

对 δ≤θ≤1 以原 cap K(θ/δ)^s 分 dyadic annuli，和为

\[
CK\sum_{j\le\log_2(1/\delta)}2^{j(s-3)}
 \le C_sK\delta^{3-s}(1+\log(1/\delta)),\quad s\ge3.
\]

θ≥1 的剩余 directions 不可漏掉：projective sphere 用固定多个 radius-1 caps 覆盖，故总数≤C_MKδ⁻ˢ；对应概率≤Cδ³，正贡献 C_MKδ^{3−s}。A 已明确支付这一项。端点 s=3 的 log 保留；s>3 的较松 log 不妨碍后续小幂预算。

## 2. 同时 nonshort、bounded norm 与 independent set

短投影每 index 概率可由 χ₄ 小球取得≤1/128；operator norm 超固定 C_M 的概率≤1/32。若 collision 数期望≤mQ，则取阈值 32mQ 的 Markov 失败概率≤1/32。短方向数超过 m/4 的概率≤1/32。因此三事件失败概率之和<1，存在一个 P 同时保≥3m/4 nonshort vertices 和 O(mQ) edges。

在这些 vertices 上，图论 independent-set bound v²/(v+2e) 给

\[
m_*\ge c m/[K\delta^{3-s}(1+\log(1/\delta))]. \tag{1}
\]

Q≥1 可吸 denominator 的 v 项。该证明对任意 m 条原子族有效，不使用饱和总数；子族继续满足原未归一化 cap。m/Q<1 时结论仍合法且非矛盾。所选是原 indices，非重采样 line law。

输出的 R⁴ all-centres/all-scales cap3 来自 RP³ 中真正分离后的 sphere packing，不是把原 Frostman 推前上界当自动继承。碰撞 graph 正是为此付费。原始阈值 a 可在固定 c_M、C_M、最终 mesh 倍数确定后选足够大；它只增固定常数，没有 δ 依赖或循环。

## 3. 原 cells、长度、共同 clock 与 cover

原 unit segment 的 ambient δ-neighbourhood 在任何 longitudinal δ-bin 中只有 O_M(1) 个 cells。因此先转成真实线参数 marks 只损固定重数；真实线点距原 marked cell 为 O_Mδ。

nonshort 给 |Pu|≥c_M。按最大坐标与符号分八个固定 charts，可保固定比例 indices，且新 time derivative≥c_M/2。原参数间隔 δ 的 marks 在每个 ρ=Cδ 的新 time-bin 只合并固定多个。projected length、time mark 数和 graph slope 的控制使用同一 nonshort 事件，不能分别取不同 P；现稿没有此错误。

projected points 全在固定 bounded box。每线先选最富的一个半开单位 time 窗，再按窗筛 indices，损失均为固定常数。延长 supporting graph line 只用于表示，不新增 marks；没有要求 shading 避开 endpoint 或在某预定内半段仍长。新 intercept/slopes 的界可依 M、R。

bounded P 把每个原 δ-cube 送入直径 O_Mδ 的集合；改成真实线点、time-bin centre、固定 chart 只作固定扩大。故输出 cell union 满足 #E′≤C_{M,R}#E。此估计是逐原 cube 的 cover upper；未借助维数投影定理，也未把各 index 的 marks 混成别条线的遮蔽。

## 4. 平均质量、两个 λ 与 η 的方向

设原总 mass≥λδ⁻¹m，逐线 mass≤Cδ⁻¹。heavy threshold λ/(2δ) 时，heavy 族至少 cλm 条，每条≥cλδ⁻¹ marks。对该族应用 (1) 和 §3，输出

\[
m'\ge c\lambda m/[K\delta^{3-s}(1+\log(1/\delta))],
\quad \#J'_T\ge c\lambda\delta^{-1}.
\]

DIR-003 对输出 unit weights 的 slope cube mass α≤C，故

\[
\#E\ge c\lambda m'\delta^{-1+\varepsilon_D}
 \ge \frac{c\lambda^2m}{K(1+\log(1/\delta))}
       \delta^{s-4+\varepsilon_D}. \tag{2}
\]

root (6)、A (14) 的指数及两次 λ 正确。若 K≤δ⁻η、λ≥δ^η，则 K⁻¹λ²≥δ^{3η}；这一费用不能写成 δ^{−3η}。先选 ε_D，再得源 η_D，之后 η<η_D/2 保 cλδ⁻¹≥δ^{−1+η_D}，最后 δ 小吸固定 mesh/clock 常数。目标 ε 的剩余余量可吸 ε_D+3η、log 及常数。

因此任意条数形式 #E≥cmδ^{s−4+ε} 合法。代入 δ=N⁻¹、s=n−1，成为 mN^{4−(n−1)−ε}，正是 KT(40) 的 proportional unsaturated 形式。取 m≥δ^{−s+η} 后再把 η 缩小，得到 saturated δ^{−4+ε_target}。这里没有把平均长时输入偷换成逐管输入，也没有把两次重筛损失取消。

## 5. 与 KT 原 K 的量词和六维链

已核 KT §6：n、d 可实数，ambient M 固定但任意，常数可依 M；shading saturated 只要求总 mass≈N#T；soft ≲ 允许任意小幂。root 的 ∀target ε∃source η 和 exact-sequence subpower 两种表述均尊重先后顺序。后者没有预先把固定较大的 η 当 o(1)。

原 Lemma6.6 的 d-collection 被用于 R^{M+1}，Lemma6.7 确实使用第二输入 K(d+1,d′) 的 unsaturated 版本。现稿同时支付 arbitrary ambient 和 (2)，故不是只核纸面的 pair of exponents。KT 原 proof exponent 的疑似排印已明记；本次不据此自称全文验证，而把具名6.2保为源条件。

固定 0<ζ<1，已付全体实 n≥4 的 seed 给 K(6,4−ζ)、K(5−ζ,4−ζ)，满足 0<4−ζ<6。KT6.2 的结果确为

\[
(2\cdot6+1+4-\zeta)/4=17/4-\zeta/4.
\]

不需经典六维起点，不需从整数 n 向实 n 免费延拓。先固定 ζ、有限次选择 source 门槛，再取 N 大及 ζ→0 的顺序合法。root 将 Hausdorff scope 限于 compact convention，未擅自扩至任意不可测集合；五维 ceiling4 也准确限定为当前递推路线，而非所有可能方法。

## 6. 保留的条件与归档边界

1. SRC-001 是 proof-level 条件读出，DIR-003 是其既有放大。本次只核其准确接口与当前使用，不替完整四维高级排除证明签发无条件认证。
2. KT6.2 作为具名高级输入使用；本次核了定义、实际第二调用和参数，没有重证其每项 combinatorial estimate。
3. 主稿 17/4 结论是有实际有限桥的条件推论；未认证其新颖性或将其登记为无条件六维新界。2025 表格只能正面证明已核 baseline，搜索未命中不能证明无更强 2026 论文。
4. 本审查时 root 所引用 `literature/metadata/R0029_source_check.json` 尚未写盘，已通知 root 后补统一归档；这属于引用完成项，不是数学证明缺口。新 Gao–Liu–Xi 原件与 extracted 文本已在库。

在上述条件和 scope 下，本次内部独审通过。没有发现需改变投影/稀疏预算或六维条件参数链的未修数学错误；不由此宣布长期 Goal 完成。

root归档附记（2026-10-17）：上述第6.4项所述metadata引用已补齐并实读核验，literature/metadata/R0029_source_check.json、catalog与GLX原件/全文均在盘；该项归档责任已完成，不改变作者先前数学审查范围。
