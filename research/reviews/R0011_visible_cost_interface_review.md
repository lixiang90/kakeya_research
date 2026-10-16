# R0011 独立审查：actual visible-cost 与 level-dependent shear 接口

2026-10-17。审查人：`lifting_obstructions`。对象为 `notes/40_multiscale/plank_inputs/R0011_direction_cost_positive_audit.md`，并交叉核对已审定 R0010 RL4/RL5。结论：稿件第1–7节通过下列逐项独核；内部独审，不等于外部同行评审。

## 1. 实际方向密度，不是有限 bin 平均

无噪声 u=(p,αλ−pq,q)，λ,p,q 独立 δ-grid，s 求和后每个三参数 index 质量≈δ³。对任意 v，v₁、v₃ 各限制 O(1) 个 p、q；固定后二坐标把 λ 限在长 2δ/α 区间，共 O(1+α⁻¹) 个。真实 ζ∼U[-δ,δ]³ 的密度≤Cδ⁻³，所以 f_V(v)≤C(1+α⁻¹)。这是原概率、原坐标、每个 point 的 Lebesgue ceiling，α=1/10 固定后 κ=0。连续 Jacobian |det|=α 是一致检查，稿件并未用它替代 noisy discrete prior 的证明。

该 upper 与 M、U 无关，单 world 没有通过 observable world weights 改变 within-world density。不同固定 M 对应不同 tempered sequences；因此令 M 任大以排除常数独立于 complexity exponents 的候选，在量词上合法。

## 2. Profile、full8 与 angular 条件确实来自同一 law

恒等式 Q(t,Y)=λ(1+αt²)+O(δ) 正确；分母在[1,1.1]内，exact (t,Y) 只接收 O(1) 个 levels。t∈[1/2,3/4] 时 fixed λ,s 只接收 O(1) 个 p、q，所以 g_t≤C。每 level hidden 支撑宽 O(η)≪a_L，各深度只碰 O(1) 个 bins。由 G_r≤C 与 support reference-volume≤C 积分得到 typical lower，确实给实际 f(r)=0；没有把它误写成支撑逐点 lower。

ρ≥δ 和 ρ<δ 两段计数分别给 Cρ 与 Cδ⁻²ρ³≤Cρ。hidden-bin conditional probability≤1 是合法逐 index upper；稿件已明确无条件 visible/hidden 并不独立。

完整八维盒重叠通过 B₁、V₁、V₃、B₃ 逐项限制 s,p,q,λ，仍为 O(1)。full8 ceiling Cδ⁻²η⁻²、polynomial pieces、native w/B1 都符合原 tempered 界；新增 λ-dependent shear 没有降低 full8 维度。

## 3. 单 level shear 精确保留 D 与 J

在同一 index/noise 的 coupling 中，Y_new=Y_old+αλt e₂。对 fixed λ，whole-block fit 的 pullback 只将 center y_c 改为 y_c−αλt e₂。center 仍 affine，矩阵 D、slack K、block q 和 J=|detD| 一项都不变。因此原 uniformly-in-λ、all-positive-width cap 可以直接用于相同 J，不需要在每层另作 SVD 或引入 determinant 比率。

原 level 权 πλ≈δ 必须乘回，才是 b*≤CK³δ^1/2 q⁻³J。稿件 (4.2) 已保留该因子，未误用 conditional cap。mixed visible G 的 upper≤CK³J 来自任一 selected 时刻 g_t≤C，也使用同一原 law。

## 4. 重新选 tags 与 fixed-dimensional 参数界

R0010 RL4 的证明是关于任意 fixed layer distributions Πλ 的 uniform probability lemma，而非只关于旧 quadric 的某组 predictors。新 layer coefficients 是 Πλ 的数据，λ 在每层为常数；对 chart 参数 θ 的维数与 polynomial degree 不增加。whole-fit 仍由两个 endpoints 的 convex norm fit 表示；current P(t,Y,c+e+tW) 对 c 仍 degree≤2，导数恰为 Pw；G 不含 tag。故辅助 quadrature、包括 G 的 sign patterns、b* 归一化、ghost/swap 与一元 sublevel 全部适用。

稿件正确要求对新 Πλ **重新选择**一张好 tag table。原模型某张已固定好表并非自动保持好，这一点已经显式处理。uniform-in-θ 的结论允许 P 等在 tags 选定后决定，不遗漏隐藏二次项或事后选择的 mixed tests。

将第3节两个实际输入代入 RL4，得到 (5.1) 的 uniform m/q upper；与真实 n(L)J/K floor 比较，tempered J≥N₀⁻ᴮ 消掉 superpolynomial remainder，给 q³≤N₀^{o(1)}δ^1/2。这里 B 可因 competing sequence 而异，只须在该 sequence 内固定；不要求统一 B。其后 subsequence/incidence submeasure 量词与 R0010 已独审版本相同。

## 5. q=δ 的真实 upper 与 full-direction 边界

midpoint δ-cube 仍仅遇 O(1) levels，每 level 仅 O(1) 个原 w₀ terminal bins，所以每 block pairs≤Cδ⁻³。g_t≤C 给 pair 原质量≤Cδ³；删掉<τδ³ 的 pairs 至多丢 Cτ。这个明确删轻操作是 floor 的来源，不是假定每个 occupied bin 自动饱和。

取 D=CδI₃、静态 cube center、P=w−bincenter：bounded V 及 Wη≪a 给 whole-block 几何/值界，derivative1、curvature0；原 m/q≥τδ³ 匹配 n(L)J。真实 current exact Y 与 current hidden a-bin 分别给 midpoint cube、原 w₀-bin 的 O(1) 列表；不输出 λ。故 H≤M 非空且与第4节同一 table/prior 配套，H∈[M/6,M] 成立。

W 独立均匀于宽 η 区间，所以完整 slope density 是 f_V/η；其 ceiling≈η⁻¹。upper 由 actual f_V≤C 给，lower 由 bounded velocity support 上概率为1给。故结论只排除 literal j3 的 visible-cost uniform completion；不保留原 source 完整(V,W)来源，不是五维 Kakeya 反例。稿件未把已条件性的 DIR-003、未全面独审的四维长证明或 generic completion 当作本反例输入。

综上，本稿所述候选失败与边界陈述均通过；无需数学修正。后续应执行已定宏观转向，不再给同一 completion 泛类添加同义统计条件。
