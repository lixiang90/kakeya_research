# R0025 finite engine、sampling 与 conditional source application 审查

2026-10-17，`audit_four_dimensional`。审查结论：**通过，可按下述具名输入及条件边界归档**。本文逐步检查 root 的 `R0025_scalar_curvature_engine.md`、`R0025_weighted_time_reduction.md`、`R0025_conditional_mixed43_middle_tau.md`，并交叉核对 B 的 `R0025_weighted_engine_counterattack.md`。已指出的 full-Y covering 归因与 chart 归一化费用，root 均已在终稿明确补入。

独立性说明：uniform-P/common-neighbor 修补及 weighted Kaufman law 是本审查者本轮源稿中的证明，故本文对这两项的自有推导不算新增独立认证；root 另行复核它们。这里对 root 的合成、独立抽样证明、参数次序与 actual source 应用作独立检查。本文未独立重证 named scalar BSG13.7、radial22.2 的完整高级证明。

## 1. root 的 fine-weighted 代表选择：通过

1. 长度 w 的原 cell 质量 `p_j≤C K_t w`；删 `p_j<c m w` 的总 ν 质量≤m/100，故两个 time 坐标至多损 2m/100 的原 g 积分。剩余 cell 数 `c/(K_tw)≤N≤C/w` 正确。
2. prepared mixture `ν_hat=N^-1 Σν_j` 相对保留原 ν 的 density 在 `[c/K_t,C K_t/m]`。所以 graph mean 下界 `c m/K_t²`、所有原 fit 事件质量上界 `C K_t a/m` 均成立。这里保留的是实际原 labels/F/G，未先换函数。
3. 跨 cells 的代表独立；同一 cell 的双时间项不能当独立。root 直接将全部 diagonal graph 置零，损≤1/N，因 `K_t w≪m/K_t²` 可支付。E Z 的下界及 `Pr{Z≥c m/K_t²}≥c m/K_t²` 只需 Z≤1，正确。
4. 全部实系数 quadratics 的 finite net 证明有效。归一变量 `λ=1/(1+|p₁|+|p₂|)`、`z_i=λp_i` 满足 `λ>0, λ+|z₁|+|z₂|=1`。非空 coarse fit 使 z₀ 在固定 box；该有界、未必闭的 admissible set 仍可按 O(h) cells 每格选一个**实际 λ>0** 点，cardinality O(h^-4)。不需要给 λ 加正下界，不会使用非法 λ=0 原事件。
5. normalized clock error≤Cw，net error≤ch；prepared precision `h_B=w^(2ε₁)` 满足 `h_B+Cw≪h`。每个 net event 是原 all-real weighted fit 的子事件，故其 prepared mean≤`C K_t a/m`。Hoeffding 和 finite union 的坏概率 `C h^-4 exp(-c N w^(2β))` 胜过 good-graph 的固定小幂概率；`β=min(ε₂/4,1/10)` 保证 `1-η-2β>0`。
6. 同一组代表提供 t/F/G。clock 移至 cell centres 后，无须 F/G 振荡控制：

   `S=(s-t)(F_i-F_j)+(s-t)²G_j`，

   time prefactors 的改变≤Cw，故 unit norm 下 S 只改 O(w)。新的 uniform B 确实 w-separated，其 interval cap 由 N 的下界和 cell packing 得到。

因此 root reduction 是合法存在性归约，**不是原 ν 的 dense restriction**。在 prepared carrier 上重新生成全部 C₄/K₄,₂ 正是必要做法。

## 2. B 的独立 sampling 证明：通过

逐 cell 按原权重 p_j 抽样的版本同样有效：

- graph 的 diagonal expectation 差≤`V=Σp_j²`；改变第 j 个代表使 Z 至多变 `2p_j`，bounded-difference tail 正确。
- quadratic fit 在 p₁,p₂ 的四个 sign orthants 内是 R³ 参数的两族 affine inequalities。O(n) planes 的全部 faces/sign patterns 为 O(n³)，可包含 equality 边界，不依赖原 fine-label 总数。
- ghost 法对一个 bad witness 的 conditional expectation≤a、variance≤V/4；`u²≥2V` 使 ghost≤a+u/2 的概率≥1/2。固定 paired samples 后逐 cell 交换，联合分布不变；Rademacher 系数≤p_j，故 union tail `C(n+1)³ exp(-c u²/V)` 合法。
- heavy-cell 删除后改 uniform prior 时明确付 `K_t/τ` 的 fit 费用和 graph `K_t²` 费用。实际抽样点未必 separated，故通过**只 round clock**来分离，比按颜色保一个子图更稳妥；same-F/G、所有 weighted fits 和 S 的 O(Mw) 误差均有证明。

该证明与 root 有限 admissible-net 证明为两条可替代的有限方法。两者都不声称 sampled indices 在旧 atomic ν 下仍有小幂质量；B §7 的反例恰说明此捷径不合法。

## 3. separated scalar engine：逐环节核查通过

### 3.1 small S 与 BSG

`H₀={E_xg≥m/2}` 有 edge mass≥m/2；balanced S-cell 层的原 pair density 至少 `m/(C log(1/w))`。w-separated B 给 N≤C/w，因此只有 O(log(1/w)) 重数层。

固定 s₁,s₂,t₂ 后，Q 对 F(t₁) 的系数恰为 s₁-s₂。删差≤`Cw/h` 的原 pair mass≤`C K_t w/h`，余下 Q 的任意 Cw-interval 强迫一个 uniform h-quadratic fit。所以根稿 (2) 的 small-S 下界由原 C₄ mass 及 `#S_j⁴` cover 得到，不循环调用 radial。

每个 S-cell 的关系至少有 m/2 的 x mass。用 sums 的 w-cell Cauchy–Schwarz 给 `E≥w^O(η₀)#A #S_j²`，归一与 Lemma13.7 的 `ν_BSG#X²#Y` 匹配；addition/difference energy 可交换两个 A 标签。small-S lower 也支付 `#A≤#S_j^C`。BSG 输出的 S′ 按**原 balanced 层**拉回 H，故原 H 密度保固定小幂。不能从未平衡的 image-cardinality fraction 得同样结论。

n=m=4 的 13.7 结论本身已控制两个 cycle 的 Q 差；固定一个 a′ 把 `4S′-4S′` 嵌入小 sumset。root 不需要另把某个自由 S-set 套回原 Y 的 tube-KT。

### 3.2 uniform P 与新的周期 prior

平均 common-right degree≥p²，所以 `degree≥p²/2` 的左 pairs 有原 μ² mass≥p²/2。删近对角时间对代价为 `C K_t w^(C₀l)`；C₀ 固定充分大、η₀ 后小，确实远小于 p²。

在保留 gap 上，前两坐标 `(t₁-t₂,t₁²-t₂²)` 的逆常数为 gap⁻¹。由 w-separated B，任一 w-ball 原 pair 重数为 gap 的固定负幂；r-ball 的 normalized pair upper 为 `w^-O(l+η₀)r²`。actual net、Prop5.1 subset 均仍是实际 V-differences，且保原 pair witness 的共同邻居 degree，F/G 未被新函数替换。

root 的 `h_P` 在 **Uniform(P)×μ** 上重建 C₄，质量下界是

`d₀⁴=(p²/2)⁴=p⁸/16`。

核对：先平均一个 shared-right 得 d₀²，再对两 shared-right 的 codegree 作平方得到 d₀⁴；原来 d₀² 不能当六时间量。新 W 的所有八条原 H 边成立，所以其输出仍在原 BSG 小集内。radial 几乎处处只应用于当前 Uniform(P)²，不继承原 B⁴ 的几乎处处。

### 3.3 radial 参数与 slab

root 取 slab width `r_s=w^(4α)` 可用。normal 最后一坐标≥√r_s 时，quadratic fit 精度≤`Cw^(2α)≪w^α`；反之 (t,t²) 的非零 quadratic sublevel 长度≤`Cw^α`，所以 raw slab upper 为 `w^b+Cw^(α-η₀)`。除以 uniform-P 保留比例后，`b_r=min(α,b)/2` 在 `u+O(l+η₀)≪min(α,b)` 下合法。

顺序是先 α,b,ζ_r，得到 22.2 的 η₀^rad，再取 u、η_r=4u、l、η₀。uniform 和 ball cap 实际≤`w^-2u`，小于允许 `w^-4u`；slab 也满足。`4α≤ζ_r/100` 与定理原限制一致。删小 norm `|v|<w^(10u)` 损≤`w^(20u-2u)`，远小于 W 的 p⁸，l 最后小即可。

### 3.4 angular law、原 multiplicity 与最终宽度

终稿 §7 明确至多六 charts，light chart mass<w^u 的总损≤6w^u；heavy chart 归一后的 parameter law cap≤`Cw^(-ζ_r-u)r²`。理由是参数球的整个 bounded cone 落到一个 actual good radial tube，随后除 chart 质量。此法不需要先额外选 good pins，也不需要参数先成为另一个 uniform set。

U 的某个坐标是原 right time，所以原 U-label law 有 1-Frostman upper；置换坐标不改变 ball cap。weighted Kaufman 证明控制的是同 right-label law 的 projection mass，不是 distinct image-set cardinal。`ζ_r+u+η₀<β_K/8` 及 root 显式 χ 次序足以支付两次 Markov、charts 和目标删选。

maximal-component chart 保 `|v_i|≥c w^q`。原 w-output interval 对 π_λ 的宽是 `O(w/|v_i|)`，所以 root (6) 正确地付 `w^-q`。这避免原文本中固定第一坐标分母可能为零的遗漏。good-right 对差的 cap 由固定第二 time 后积分获得，无需独立化 g。

所有 exception 都是对同 `μ_P²×μ²` 的绝对 mass upper，足够小后可与任意相关 W 相交。small-output cover≤`w^-1+κ-Cl` 与 right-law cap≤`Cw^(1-β_K-q)` 的指数矛盾成立。`β_K=κ/10`、q≪κ、Cl≪κ 的选择可实现，且 BSG 常数先于原 η。

## 4. conditional actual mixed43 应用：通过

已核 root 最终稿 §4 的 full-Y lower/upper packing 补句。以下实际预算均成立：

1. 同 ψ、同 vector τ 先得到 Fψ/Gψ 和原 g；τ 不在 ψ 选择后重新定义。空间同时除 L 后，S 也除 L、误差从 e 降为 `w=e/L`；原 reference probability 不改。
2. 新 fine spatial base 为 `r₀=δ/(τL)`。查询 `r₀≤w` 等价于 `δ≤τe`。实际 e 含 `Kρ^(3+ε₀)/τ`，ρ≥δ^(1/4)、原小 ε₀<1 给 `τe≥ρ^(3+ε₀)≫δ`。这使用最终误差项，不是原早期那条不普遍成立的 `δ≤Kτρ`。
3. `w≥K^-Cρ`，故原 fine time base `d=δ/ρ` 满足 `d/w≤K^Cδ/ρ²≤K^Cδ^(1/2)≪1`；所有 engine time-cap 查询≥w 均在原合法范围。τL≤1 由 τ≤ρ^(3-ζ₁) 和后取小 loss 得到。
4. 新 weighted fit 回原 F 的误差至多 `L h_new A(LP)`，所以 root 正确要求 `L h_new≤σ`；只要求 h_new≤σ 不够。coefficients 任意大也已由 A(LP) 支付。
5. 空间 occupied-bin cover 的 upper 现由**全原Y**的 AD lower 作分离小 ball packing，再用扩大 patch 的 AD upper 得到。裁切 input patch只用已付的 fine-total lower，未给它重新赋 AD lower。fine capacity upper 加 heavy occupancy lower 才允许从原 fine-input law 改 uniform A₋；target A₊ 用同样 full-Y cover，故 cardinal ratio≤K^C。
6. κ_engine=min(κ/2,1/2) 为 K 的全部 fixed powers 留出了真缓冲；κ=1 的零维 Y 边界也可用该缓冲。engine 只需 input upper 及 target/input ratio，未假定新 A 是完整原 AD 配置。
7. engine 允许的 precision 指数先依 κ_engine 固定；physical ε₁、ζ₁ 后选，使 `p=2ε₁+ζ₁` 足够小、`6ε₁+2ζ₁<ε₀`，再取 QSC 的 β、最后所有 AFF/source η loss。由于 `ρ²≤w≤ρ^c`，`cε_engine>2p` 有余量即得 `Lw^ε_engine≤ρ^(2p)`；`ρ^β≤w^(β/4)` 给正确 mass threshold。engine 的精度门槛只依 κ，mass 指数 β/4 可后给，所以这里没有把 β 依赖循环进 physical p。

因此，具名高级输入及真实准备条件全部满足时，root 所列 **middle vector-τ** alternative 的 conditional 排除可归档。

## 5. 限制与最终 verdict

本审查认可的是：原 fine weighted finite engine 的严格归约与合成，以及已列全部 source 准备条件之下的 middle-τ 应用。它修补了原 source 的 uniform P/原 (208) multiplicity 接口，不是对整篇 source 的全量证明审核。

未支付的 ell3 whole-matrix AFF、large-τ vector stability、mixed43 quadratic case 和其他五维 case 仍明确开放；named scalar BSG/radial 的高级证明仍只是具名条件。没有新 Kakeya 维数界、真实 Kakeya 反例、一般维证明或重大性认证。无需为本 review 新增数学子任务。
