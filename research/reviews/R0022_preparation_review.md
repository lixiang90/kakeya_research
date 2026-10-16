# R0022 独审：原时间闭包、observed graph 与 fixed-scale affine 准备

2026-10-17，`lifting_obstructions`。独立审查最终版本：

- `notes/40_multiscale/sticky_mixed/R0022_time_restriction_closure.md`；
- `notes/40_multiscale/sticky_mixed/R0022_observed_graph_source_audit.md`；
- `notes/40_multiscale/sticky_mixed/R0022_fixed_scale_affine_preparation.md`。

另对照本库 WZ arXiv:2609.22035v1 原 Definitions17.2–17.4、§19.1–19.2、PDF91–93 的 Theorem21.2 与 (170)–(173)，以及 R16 已保存的原关联 good-q 证明。本文不重证 Theorem21.2 的高级 radial/BSG 输入或 Lemma19.2 的全部凸集扩张。

**结论：在稿件明确的命名输入和参数次序下通过。** 已核实际原路径质量、heavy-cell 下界、保持时钟的投影、bounded-range scalarization、整层时间 restriction 和 low-whole-velocity 删除。特别核过最终修复：既没有假设源 F 全局 Euclidean Lipschitz，也没有把任意斜率的 vertical band 直接通过 time rounding。通过的是 allowed-ρ 的实际 LOCAL-AFF 准备及相应有费用版本；不是一般五维 sticky 或 Kakeya 的完成认证。

## 1. 删整时间层的闭包

fine AD 到 coarse AD 的证明方向正确。对 coarse 分离 centres，fine 小球的 AD lower 给每个 coarse cell 所占 fine mass 的下界，求和后得到 coarse upper；fine 大球 mass 再除以单 coarse cell 的 fine upper，得到 coarse lower。它不是仅凭 subset 继承 AD lower。

对一个原 time interval J，删选后的 union `S_J=∪_{z∈Z'∩J}Y_z`：upper 由原 union 的 coarse upper 得到；任意 S_J 的自身 centre 属于某个保留的完整 Y_z，后者的 fine AD lower 经 coarse 化提供所需 lower。小于固定倍 coarse 尺度的端点由至少一个 cell 处理。因此删**完整层**的论证有效，不要求 Z' 在每一个旧窗口都 dense。

T、所有保留层的 X/Y/tildeY、原 Φ_p 和 ξ witnesses 均未删；cross-time lower 是本次闭包中唯一不由字面 restriction 立即保持的部分，已单独支付。保留 `#Z'≥δ^a#Z` 后，只需把配置损失增至 `η'=O(η+a)`。选 η' 为原 η 的整数倍，新的 allowed grid 是旧格的子格；相邻尺度取整只付 `δ^{-O(η')}`。旧格点的原性质本身也继续成立。

这一闭包不适用于任意空间点、管或 Φ 子族。稿件保持 T 的原 joint AD/CW，不重置所选管的 AD lower；其范围正确。

## 2. good-q 与实际 W 质量

原 source 对任意 q 写局部 lower 的字面步骤没有被当成免费输入。对一个原时间窗口，cross-time Y-cover 和 dyadic f oscillation 给 `N_ρ E≤Kρ^{-(4−κ)}`；全 X 的 dense lower 与 Y 的 AD 给窗口总原关联量。按原关联平均可选 q，使

    e≈K^{±1}m(ρ/δ)^{4−κ},   m≥K⁻¹#(Z∩J).

局部管 upper 为 `#T(q)≤Kρ^{-κ}(ρ/δ)^4`，由共同 coarse Φ_q、ξ_q 和原 T 的 joint4-AD upper 得到。设 d_T 是原 marked degree，`Σd_T²≥(Σd_T)²/#T(q)`；再以共同中点作 CS，得到两边 path 数至少 `K⁻¹eδ^{-2κ}m²`。按原起点、两个时间和末方向 ρ-bin 再作 CS，得

    #W≥K⁻¹ e δ^{-4κ}ρ^κ m².

这个推导没有使用逐管 dense marks。每个 fine Φ-bin 只取原存在的 witness，使 degree upper 和恢复 upper 都针对原 pointwise 关联，而非针对所有穿过一点的环境管。

## 3. 末桶选择和 bounded graph 的幂次

令 σ=ρ²。一个终层的 y-桶总数至多 `K(ρ/σ)^{3−κ}`，每桶原 endpoint 上界

    M_Q=K(ρ/δ)(σ/δ)^{3−κ}.

固定 endpoint 的 W 重数 upper 与总 W lower 有相同的 `δ^{-4κ}ρ^κm²` 主因子，故删除 endpoint 数不足 `K^{-B}M_Q` 的轻桶可以按原 W 质量支付。再按 `W_Q/e_Q` 平均，得到同时 endpoint 重、W 密的一个桶。这里可能只有很小的全局桶质量，稿件没有把它称为全局 K⁻¹ 质量。

给定 code `(a_σ,z₁,z₂,φ₁,ρ,φ₂,ρ)`，A 稿五项恢复表给

    M_code≤K(σ/δ)^{4−κ}δ^{-4κ}ρ^{3κ}.

直接相除检查：

    W_Q/M_code ≥K⁻¹(ρ/σ)ρ^{-2κ}m²
                 =K⁻¹ρ^{-1-2κ}m².

这正是 `#A·m²·#Φ_q²` 的主量级，因为 `#A≈K^{±1}ρ⁻¹`、`#Φ_q≈K^{±1}ρ^{-κ}`。因此除恢复上界后的 g 满足 `0≤g≤1` 且在**同一个** product reference frame 中均值为 K 的负固定幂。原相关性仍全部在 g 中，不要求原路径 law 独立。厚桶的 input/output 支持合并只付 K。

## 4. 印刷符号和归一化的局部修复

原 (151) 的两块增量是

    Δx=(z₂−z₁)Δφ+O(Kρ²),
    Δξ=(f(z₁)−f(z₂))Δφ+O(Kρ²).

所以在使用正号 B=(t,+F) 时应反射 observed ξ。最终定义

    a=((x−x₀)/ρ, −(ξ−ξ₀)/(L_fρ)),
    b=((z−z₀)/ρ, +(f(z)−f(z₀))/(L_fρ))

确给 `a'=a+(b₂−b₁)Δφ+O(Kρ)`。同时在 A 与 B 的 vertical block 除以 L_f，修复印刷 (172) 的缩放错配；只缩 B 会留下一个不可忽略的 anisotropic factor。

反射和同步线性缩放保 first coordinate、cardinality 的小幂比较及 affine nonfit。它们是原局部接口的修复，不能称作源主定理反例。

固定 x 的 σ-cell 时，厚 grain 中的原点只遇 K 个物理 σ-cubes；原 ξ coherence 因而给每 x-cell 至多 K 个 A-cells。投影 `Π_λ(x,ξ)=(x,λ·ξ)` 对所有有界 λ 的 image cell preimage 重数至多 K。这提供实际 A 的 cardinality 保留；任意 finite graph 没有此性质，本审查未使用那种错误概括。

## 5. 粗化必须保 lower capacity；final 版本已支付

对原 fine times 分 coarse B-cells，upper `n_b≤P=Ksρ/δ`、`#B_c≤K/s`、`m/P≥K⁻¹/s` 足以把两个 time fibres 聚合并除以 P²，保 bounded graph 和 K⁻C mean；它们单独不足以把 fine nonfit 传成 uniform coarse nonfit。

最终稿删 `n_b<P K^{-B₀}` 的轻 cells。其原 time 质量上界 `K^{C−B₀}`，g≤1 使两个 time coordinates 的总图损失至多该量的两倍。先选 B₀ 大于原图密度损失常数，得到每个保留 cell 的真实 lower capacity，才允许 uniform coarse cardinality 上界。此处没有免费改 prior。

每个保留 cell 选**实际 fine time/F 代表**；不同 cells 原 indices 不交，time 可取不同，但未必 s-separated。有限 scalarization 只需所有长度≥s 的 interval 满足 `ν(I)≤K_t|I|`，由每 time-s-cell 至多 K 个 B-cells和总数 lower 已得。最后投影并 round 到 s-grid 才提供 ABC 的 separated set，碰撞重数仍为 K。

## 6. 大斜率舍入漏洞已通过欧氏 tube 修复

旧式说法“coarse error O(s) 远小于 h，所以任意 vertical affine fit 可传回”不成立：slope R 会产生 `|R|s`。root 最终 §5 已删除这个捷径。

现取 `h_v=ρ^{4ε₀}`。fine vector tube 若 time-axis 分量≥sqrt(h_v)，其点满足误差 O(sqrt(h_v)) 的 vector vertical fit；反之 time 投影长 O(sqrt(h_v))，用原 time packing。二者给 fine tube cap

    K[δ^{a/2}+ρ^{2ε₀}+δ/ρ].

欧氏 tube 在 coarse 舍入下只增 O(s)，不乘 R。先用上一节 lower capacity 得 uniform coarse tube cap。然后 bounded box 中任意 vertical h_v-band 都包含于一根向量直线的 Ch_v 邻域，该直线与扩大 box 的交段长度有固定上界，故用固定数 unit Euclidean tubes 即可覆盖。由此得到所有 vector vertical h_v-fits 的质量≤`ρ^χ`，`χ=min(a,ε₀)`。

指数余量正确：ρ≥δ^{1/4} 给 `δ^{a/2}≤ρ^{2a}`、`δ/ρ≤ρ³`；因此 K 与固定常数可在 η 后取小时吸收。整个步骤只需 bounded F 和 dyadic 结构提供的 cell cap，不假设跨边界的 Euclidean Lip。

## 7. finite scalarization 与 ABC 两参数

本轮独立 finite lemma 的 bounded-range 版适用于上述 actual-time representatives、uniform coarse 权重及 interval cap。对 `a₀=ρ^χ`、`h=h_v`、`w=ρ^{8ε₀}`、`b=ρ^{χ/100}`，有

    Pr(Bad_b)≤C[a₀/b³+K_t w/(h b⁴)]
             ≤C[ρ^{χ−3χ/100}+K^Cρ^{4ε₀−4χ/100}]→0.

`b≫K_t(s+w)` 也有正幂余量。额外 b⁻¹ 是 bounded-range 下 rich Euclidean tube 垂直化的真实 gap 费用；ordered-middle convex residual 本身没有 gap 逆幂。该统计量同时控制全部 adaptive lines，没有对无限 r,u 作粗 union bound。

同一个 λ 投影 A、B 和原图。A/B 的 first-coordinate fibre cap、Φ 的 κ-AD 粗化都只付 K 次幂。fixed b₁、φ₁ 的平均保持 bounded dense graph；其输出在同一 A₂ 的 O(s) 邻域。原 Theorem21.2 中 regularity 参数与 graph/small-image 参数必须分别足够小，最终稿有明确分开检查。

取 `ζ₀=ζ/4`、`ε₁=9ε₀`、`ε₂=χ/400` 后，η 充分小使 `s^{ε₁}+Cs≪w`，且保守 scalar mass cap 小于 `s^{ε₂}`。named ABC 给

    #A₂≥K⁻C s^{-1−κ+ζ₀},

与 `#A₂≤K/s` 冲突，因 κ>ζ。图的 K 损失只来自 original η 和固定粗化次数，没有把 a 伪装为可任意小的 η；a 只决定 scalar nonfit 的正幂参数。

## 8. 全局反证、low velocity 和最终范围

反设 `Σ M_J<δ^a#Z`，删 `M_J>δ^{a/2}#Z_J` 的窗口损失≤δ^{a/2}#Z；再删过低 time-density 的窗口损失可控，保留至少固定比例原 times。整层闭包使之仍为合法原配置。good-q 的 m lower 把窗口 nonfit 只放大 K。因此这是真正 fixed-ρ 的反证，不是对 all-scale 印刷 Lemma21.1 作形式否定。

原最大 fits 选出的 times 全局 δ^a-dense；删过稀窗口可给各窗口足够 time span，从 pairwise fit 和 dyadic f upper 得 whole speed 的 K-upper。若低速窗口携带至少 δ^a 比例 selected times，再按整层闭包得到参数 O(η+a) 的原配置。令

    b=C₀(η+a)/(γζ),   σ=ρδ^{b/2}.

须先令 a 足够小依赖 `γζµε₀`，再令 η 更小，保证 `b≪µε₀`、`b<µ`。于是 `ρ²≤σ≤ρ`、`ρ≥δ^{1/3}` 且同窗口 f oscillation≤σ。named Lemma19.2 给的 CW lower 幂为 `C(η+a)/γ−bκ/2`；C₀ 大后与原 CW upper 冲突。此处只证明 **whole vector speed** lower，首坐标非零仍须 R21 后续 E+swap。

allowed ρ 的常数1容差 (LA) 与任意 ρ 的 K 倍/略损指数版本已区分，不能把相邻 allowed-scale 取整说成保完全相同的常数1容差。R21 接收的是有费用版本，未见此处接口冲突。

本次通过为实际 affine/whole-speed/stable-time preparation。接到 R21 时仍须一个**实际、全局 dense、可作整层 restriction 的 quadratic alternative**，且其 density 损失符合上述参数预算；本稿没有自动提供该 alternative，也不处理非二次分支。Theorem21.2、19.2、19.4 等高级输入仍为命名引用，未独立重跑全篇证明。没有新 Hausdorff 维数界、完整五维 sticky 结论、Kakeya 反例或重大性认证。
