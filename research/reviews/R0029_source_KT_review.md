# R0029 独审：四维 finite 读出、原着色量词与 KT 衔接

2026-10-17，审查者 `audit_four_dimensional`。审 root 的 `R0029_conditional_seed_and_six_dimensional_bound.md`，以及 B 的 KT/前沿稿（末节记录完成情况）。投影稿由本审查者撰写，对该部分只作接口复核，不计独立证明；B 另审完整投影。对四维整篇 proof 和 KT6.2 只在明确具名依赖下调用，没有独立重证其全部高级内容。

## 1. SRC-001/DIR-003 的实际条件

已有 SRC-001 的输入是：固定 bounded R⁴ graph chart，先给目标 union deficit σ>0，再得容差 η_src 和尺度阈值；directions separated、数量近 δ^-3、每线长 marks。它不是无方向的 weighted convex-clustering 命题。已有 DIR-003 以其为条件，给任意稀疏方向数和正权的 `Σω#J≤Cαδ^-ε_D#E`，但仍有逐线 long-mark 门槛。

root §§1、4 保留了所有这些限制：没有以 ordinary Hausdorff statement 直接升级 finite，没有把方向格 cap 改成无方向 plank cap，也没有删掉 shading exponent 对 η_D 的依赖。原 weights/重复 indices 的 R9 化约在本轮未重证，但其已存具名结论被准确使用。

## 2. Theorem2.17 在 finite selection 之后的依赖

逐段重新核本地四维原文 PDF pp.20–25；文本 `openai_2026_four_dimensional_kakeya.txt` 用 `split('\n')` 的约 1065–1332 行。该 theorem 前半通过 Hausdorff cover 和 outer direction measure 取得 finite witnesses；其后责任如下。

- 原 1122–1135 行：独立扰动全部三个 intercept 和 slope 坐标；分离 slopes 给 full three-slope ceiling，条件于 full slope 的 y-intercept density 由 independent intercept boxes 控制。
- 原 1138–1184 行：(2.27) 的第一项只用 observation support 的 cell 数和 inverse-subpower incidence mass；第三项用 full slope 与 conditional y-intercept ceiling；zero-depth 项用原二维 WP3/Lemma2.15 及由 full visible slope 推出的 (2.28)。
- 原 1186–1225 行：homogenization、endpoint/angular maximization 产生 C(1−R) profile 与严格正 gain。这里没有再次使用同一个跨尺度 K。
- 原 1230–1328 行：true chart 的 floor 返回原未归一化 prior；crop mass、物理 Jacobian、hidden scale 在 (2.33)/(2.34) 比较时消去，full slope ceiling 将 slope-volume 转成 original-prior mass，得 `m(r₀,u₀)≤K₀q^-3` 及 H≥σ/6。
- 原 1330–1332 行：矛盾仍依赖后续对所有 bad exact problems 的排除，不能只核 2.17 就声称完整四维 finite bound 已独立证明。

对任意 small-loss finite countersequence，原 δ-time marks 可先扩为 cδ 的 time intervals，固定扩大其 visited cells 后这些 intervals 的轨迹点全落入扩大 union。每条原 marks 数给 duration≥cδ^η。之后 intercept/slope 各扰动 O(δ)，全部这些 incidences 仍落入固定扩大 union。因此不是以离散点的零 Lebesgue time 直接冒充 selected duration。

若 `#T≥δ^-3+η`，δ-separated slopes 的平滑密度至多 `C/(#T δ³)≤Cδ^-η`。取反证序列 η_k→0、δ_k→0，它成为 subpower；selected mass 为 inverse-subpower。indices≤Cδ^-3、visited cells≤Cδ^-4，平滑的 density heights、boxes 和 union predicates 均有固定 polynomial bound。单个 counterfamily 的任意原 anchors 只作为 bounded box centres，不需可测 witness map。故 root 对 SRC-001 的 proof-level 读出与 R7 的原条件一致。

这项检查不能消除完整 OAI4 proof/引用输入的条件，也没有从仅有一个固定 shading exponent 的 finite 估计推出任意小损版本。

## 3. root (6)–(7)：unsaturated family 与两个 λ

给原 m 条线、cap exponent s、平均 density λ。heavy threshold λ/(2δ) 保 `m_h≥cλm`；projection lemma 对任意条数成立，故输出

    m'≥cλm/[K δ^(3−s)(1+log(1/δ))]。

每条输出各有 `cλδ^-1` 个自己的旧 marks。固定 graph patch、共同单位 clock、相当 mesh 与 fixed cell enlargement 只耗常数；延长 supporting line 不新增 marks。输出 direction separation 使 unit weights 的格总权 α≤C，不需要输出条数已饱和。

对这些实际 indices 用 DIR-003，得

    #E≥c λ²m K^-1 δ^(s−4+ε_D)/(1+log(1/δ))。

两 λ 分别来自 heavy 条数和逐线 mark lower，正是 root (6)。若 `K≤δ^-η`、`λ≥δ^η`，费用为 ε_D+3η 加 log。先取 ε_D<ε/4，再取 η<min(η_D/2,ε/16)，足以得 (7)。fixed mesh 常数在 η<η_D/2 的严格余量中被吸收，没有把 mean-density family 免费当逐线 family。

令 s=n−1、δ=1/N，(7) 是 `#E≥c m N^(4−s−ε)`。它正具有 KT (40) 的 unsaturated factor `m/N^s`；当右端很小时依然合法。root 没有假定 m≈N^s，也没用 original saturated m 偷替中间 pivot family。这里 λ 仍需 inverse-small-power，不能解释成任意 λ 的 sharp maximal estimate。

## 4. ∀目标 ε∃输入 η 与 KT 记号的严格范围

KT §5（文本约 750–753 行）固定一个 small ε，用 `A≲B` 表示容许 `C_εN^{Cε}` 的费用；§6 的 saturated direction collection 和 shading 都使用该记号。本文有限种子的 quantifier 是 `∀目标 ε_out>0 ∃输入 η_in>0`，没有证明 η_in 随 ε_out 的线性模数。

因此不可额外登记一个“给定 source ε 时，输出必只损 Cε 且 C 统一”的新定量结论。root §5 终稿仅陈述临界 4 的序列性 soft-loss lower，实际 Theorem6.2 调用始终是严格次临界 `K(n,4−ζ)`，并明确没有 literal 临界 K(n,4) 的统一线性模数；这一区分足够。

固定 ζ>0 后，可先把 finite seed 的输出损失选为 ζ 的严格小部分，再令 KT 的底层 ε 足够小，使原 cap/λ/m 的所有固定 `N^{Cε}` 费用落入相应 η_in 门槛；中间调用次数有限，取所需阈值的最小值。亦可用固定 ambient 的 exact sequence 表述：`K=N^{o(1)}`、`λ=N^{-o(1)}` 时，对每个固定 ε_D 终将满足门槛，再令 ε_D→0 得 (6) 的 soft-loss lower。无需线性 modulus。

此说明不是把一个 fixed positive loss 当 o(1)。fixed ambient M 的常数及阈值可依 M；KT 实际 lift 只把固定 M 改成 M+1，没有让 ambient 随 N 无界增长而仍假设统一常数。

## 5. KT 第二输入的真实调用点

重新核 KT 原文 Def5.1/5.2、§6 Def6.1/Th6.2 与 Lemma6.6–6.7：文本约 768–799、985–1022、1178–1227 行。允许 real n/d；shading saturation 是 total mass≈N#T，不是每条整线。原 proof 先合法 refinement 出 density≈1 的线，再在 Lemma6.7 中对 remaining high-multiplicity shading 作相同 refinement。

Lemma6.6 的 lifted family 在 R^(M+1)，方向由原 i_{α,z} 仿射决定；固定 z 后 f=(z,i) 的单值性给 separation。其 direction cap 是 E' 的 ball count `(Nθ)^d`，所以是 d-collection，即第二输入 n'=d+1。原 proof display 写 d−1，而 statement 及紧接的 E' cap 是 d；root 将其明确隔离为疑似排印，没有据此认证整篇 KT 已逐步无误。修成所需 exponent d 的局部证明与原 statement 相合。

该 family 不必有 N^d 条线，故 Lemma6.7 确实需要 (40)：剩余 saturated shading 的 union 至少 `#T(z) N^{d'−d−o(1)}`。若高重数阈值是 `N^{d+1−d'+strict loss}`，乘 union lower 后与总 incidence≤N#T(z) 矛盾。本轮 (7) 在 s=d、arbitrary fixed ambient、任意原条数上正好提供这个形式。

本审查没有重新证明 KT 的全部 pivot/Córdoba/L² 步骤；最终递推仍用具名完整 Theorem6.2。上述核对只确认本轮新增 seed/unsaturated 输入没有错维、漏 saturation 或误用 real parameter。

## 6. (8)–(9) 的条件算术及集合范围

取 `0<ζ<1`，已述 finite seed 给 `K(6,4−ζ)` 与 `K(5−ζ,4−ζ)`；后者的角指数 `s=4−ζ≥3`，任意 ambient lemma 正适用。KT6.2 的 n=6、d=4−ζ、d'=4−ζ 均满足 `0<d<n`，输出 `(13+4−ζ)/4=17/4−ζ/4`，无须借旧六维起点或另付 direction-dimension monotonicity。

对所有 ζ→0，KT 具名 Hausdorff 转移给 root 所写 compact 六维 Kakeya scope 的条件下界 17/4。该推导没有扩大到任意不可测集合，也没有证明 full 五维或一般猜想。17/4 与旧 `7−2√2≈4.171573` 的大小关系只是算术；最新全前沿与新颖性须另核。

## 7. B 稿：独立 weighted thinning 与前沿 scope

已逐式核 B 的 `R0029_KT_seed_and_frontier_audit.md`。其 §3 是额外的有限稀疏化校准，本轮主链已可用直接 s≥3 投影免去该步骤：

- p=3 时原族本身满足较宽输出 τ。p>3 时独立选取率 `q=N^{3−p}`，count mean 为 qm≥N^{3−η}；固定 ambient sphere 的有限 cap cover 给其上界 `C_MN^{3+η}`。
- 任意 cap 的 mean 上界 `qN^η(Nθ)^p≤N^η(Nθ)^3`。N^-1-net centres 加 dyadic radii 共 polynomial 个测试；阈值 `C N^{τ/2}(Nθ)^3` 最小仍为正幂 N^{τ/2}，足使 Chernoff 与 polynomial union bound 合法。任意 centre/scale 用固定扩大测试覆盖，费用吸收进剩余 τ。
- 原 weights 是 deterministic mark counts，彼此不需独立；随机 index selection 才独立。`Var Z≤C_M NqS`、`qS≥N^{4−2η}`，故质量失败概率≤`C_MN^{-3+2η}`。同时与 count/cap 好事件交集，`Z/X≥S/(4m)` 保平均原 shading，不声称每线 heavy。
- 原 marks 全保，所以新 union 是原 union 子集。两 λ 预算及 §5 的 real parameter/第二输入/17/4 算术与 §§3–6 的独立核算相符。

前沿数值另核本地 GLX `gao_liu_xi_2025_curved_kakeya_v1.txt` Table1（PDF12，约 548–568 行）和 HRZ `hickman_rogers_zhang_2019_v1.txt` Figure5（约 2347–2354 行）：其 Euclidean 对照确列六维 `7−2√2`，并列五维18/5、七维34/7。GLX 的主线是 curved/Nikodym，不被当前比较冒充一般 line 定理。差值 `17/4−(7−2√2)=2√2−11/4≈0.078427125` 正确。

为核 scope，本审查另直接读取官方摘要：

- [2610.10603v1](https://arxiv.org/abs/2610.10603v1) 研究 codimension-two plane flakes/CW 与相应四维 plane 问题，不能作为普通六维 line bound。
- [2505.05709v2](https://arxiv.org/abs/2505.05709v2) 约束 midpoint set A 的 packing dimension，给 restricted Kakeya 的 Hausdorff lower；packing 是该先验的限制，不是把一般 line Kakeya 的 Hausdorff 问题换成 packing 结论。
- [2609.22035v1](https://arxiv.org/abs/2609.22035v1) 为 Hong Wang–Dmitrii Zakharov 的 sticky tube 论文，摘要只声称其 sticky/CW 范围；B 初稿表内误写 Wang–Zahl，已回报作者并复核终稿改正。这是书目修正，不改变本轮数学链。
- [1908.05589v1](https://arxiv.org/abs/1908.05589v1) 摘要将 maximal 改进维数列为 n=5 或 n≥7，与其 Figure5 六维沿用 KT 相合。

没有重跑穷尽式 2026 文献检索，也未独立核每个被 B 排除来源的全文。B/root 明确不声称最新最优或优先权，符合实际比对范围。

**最终意见：通过，可归档；已核书目姓名修正。** root source/KT 链保留完整 OAI4→SRC/DIR 与具名 KT6.2 条件，finite projection 与 unsaturated shading 接口已支付；仍非无条件六维新定理、full 五维或一般猜想的完成，未经外部同行评审或重大/新颖性认证。没有必要继续改投影常数或 thinning 名称，本轮后按 R30 macro 审实际共同源输入符合剩余责任。
