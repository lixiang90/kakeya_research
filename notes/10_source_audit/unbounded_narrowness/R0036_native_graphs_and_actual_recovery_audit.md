# R0036：稳定 native 图、投影支持与原 law atlas 回传

2026-10-17，互补审查 B。独立实读原 §10.4–10.7（PDF159–168），并核 Lemma3.1、Cor3.4、Def2.2/2.8、Lemma4.12 及 R31/R34/R35 证书。只在原第二模型及原 §10.1–10.3 的 nested true systems、full-time C、balanced A 输入下证明后半；前半和 Theorem8.2 全部证明由另两位独立审查，不由本稿自我认证。结论仍是来源责任，不是新五维结构结果。

## 1. 固定量词、原对象与停止条件

设原 maximizing exact sequences E_i 满足 d_i→d<d₀<1、H(E_i)→k>0。反设 global optimized ℓ=∞。保原 world 权 ω_γ、原 prior ν_γ 和 final tempered path μ_ref=Σω_γμ_ref,γ，质量 p_path≥K₀⁻¹。Q₁,Q₂,C,A 均存 full-layer trajectory assignments；后续 incidence restriction 不改 ν_γ(Q₁)、ν_γ(A)。

输入为原(10.2)–(10.17)：q₁=N₀^{-ks₁+o_i(1)+o_N(1)}，g_j=N₀^{-α_j}，Δ_i=α₂−α₁→∞，g_C=g₂N₀^{2u}，q_A=N₀^{-h_A,i+o_N(1)}、h_A,i→0；A known by 原 p₁，有 actual K₀ geometry/list bounds，且

\[
\nu_\gamma(A)/J_A=N_0^{o_i(1)+o_N(1)},\quad
\|D_A^Te_Z\|\ge q_A/K_0,\quad
\sum_{\gamma,I,A}\omega_\gamma q_A\nu_\gamma(A)\le1.
\]

K₀ 只表示 fixed i exact sequence 的 actual subpower；K 表示选 diagonal 后的 subpower，不能据 ν_A/J_A 的两极限句子给 fixed i 的 actual K₀。输出须是 fixed positive c′ 的原 p₁-known atlas、whole-block assignments、actual lists/slacks 及 original coverage>p_path/log N₀。若其任一步仅在 masked/renormalized law 成立，停止“整个分支通过”。

## 2. 先定 gain 与 guard，后取 diagonal

固定 Cor3.4 在二维 base、quadratic degree、固定 comparison geometry 与 d₀ 下的 ε_*。选 0<θ<min(1,ε_*/4)，2θ<ε<ε_*，再取 δ>0 使 δ<θs₁/4 及 C_match δ/s₁<ε/2；置 c′=θs₁/2。所有 fixed losses 先计入 C_match。

对于 sufficiently large fixed i，h_A,i<kc′/2。若原 known atlas 深度 c′、time q_A 存在，normalization/completion 会使 H(E_i)≤kc′/2+k(d_i)(1−c′)，违 H(E_i)→k。按原 finite-sample exclusion，先固定输出几何构造的 polynomial complexity bound 和 actual (K_path log N₀)^C list/slack 上限，再从其排除区间内取 N₀ 任意晚。不能证明出新的测试后再修改已用样本的 guard。

这里允许 bound 随 fixed i 的已有 exact data/path/known A 系统改变；它在该 exact sequence 内固定。没有要求所有 i 的 tiny widths 共用一个数值下界。旧 A 数据及逆变换是预先固定的 tempered inputs；新 greedy tests 个数和每个 fixed-format whole-time 测试只增加确定的 polynomial 费用。

选 diagonal 时才令 ν_A/J_A、各 profile errors 与 actual path factors 归入 K=N^{o(1)}。新输出的 value 正幂 buffer 吸收这个 K；最终 derivative、frame 与实际 list 控制另回到 K_path，不能直接把 K 当 actual output slack。

## 3. 两次 light 删除与两个不同 witness

先对 depth≤s₁（含0和 r₁,i）纯 cap 与 terminal pure-lower/joint-upper 作 analytical preparation，损 o(p_path)。有限 depth grids 慢增、sample 够晚，cap 属指定 good old ancestors。对任意固定 i，每个固定容差的 exceptional mass 是 power-small，足以相对 p_path 收费。

若 Q₁ 在原 time block 的当前质量小于 q₁ν_γ(Q₁)/H，删整 label。由 Σω_γq₁ν_γ(Q₁)≤1，H⁻¹≪p_path，费用可忽略。保留下来的 W_γ,I,Q₁ 是**此时**的原 witness：质量≥q₁ν_γ(Q₁)/H，whole old domain 支持、同 block disjoint，并保 zero-depth cap。

随后 core/branch 条目的 light 删除也以同 q₁ν(Q₁) 预算收费，先乘每 label 至多 K 个条目，再把 reciprocal-subpower cutoff 取小。第二种 witness 用于 entry 的 norm；第一种 W 仍单独保存供 whole-domain 计数。没有对任何后来 A 或 projected cell 宣称重获这两个 floors。

## 4. 原 Lemma10.4：signed curvature、tiny coefficient 与 escaping root

在 Q₁ normalized coordinates û、z=Bw，P 为 total-degree≤2，a_fit=N^{-r₁,i}。原 retained incidences 满足 |P|≤K₀a_fit、K₀⁻¹≤|P_z|≤K₀、|P_zz|≤K₀/a_fit。depth-r₁ cap 及真 saturation给 û-base ceiling≤K q₁ν(Q₁)。因此第一个 floor 产生 measure≥1/K 的 real projection；不是由“某处有一条线”产生 Remez 数据。

写 P=A z²+B(û)z+C(û)。D=P_z²−2P_zzP=B²−4AC 独立 z，次数固定。它在上述 projection 上有 subpower upper，故 polynomial Remez 在所需 normalized box 的复 enlargement 上控制 D 及其固定阶 derivatives。leading sign 无须为正。

若 |P_zz|≥(a_fit H′)⁻¹，则 center z_c=−B/P_zz 为 affine，|z−z_c|=|P_z/P_zz|≤K a_fit。不把这个 center 当实际 root，也不要求它的第二导数符号。若 |P_zz| 较小，选 H′ 足够大，使 2|P_zzP|≪|P_z|²；于是 D≥1/K。在 used cores 上以已经得到的 D-derivative upper选 inverse-subpower 半径及固定相对 complex margin，D 不过零，两 simple roots 存 holomorphic branches。linear case单独保其非零 affine coefficient。

两个必要边界测试：P=εz²+z−ℓ(û) 的 unused root 可以到 ε⁻¹；证明只追被 incidence 选中的近 root，不声称全部 roots 有 uniform bound。P=±a_fit⁻¹(z−z_c)²∓a_fit 的大曲率 used roots距 center 为 a_fit，正好由 center 近似；强行要求 exact zero graph 或固定曲率符号都会多加假设。二者不反原命题。

对 small-curvature root，|P_z|=√D 在 core 邻域有 lower，从 incidence z 到对应 root 的误差≤K a_fit；用相应 derivative sign 选近支，避免 far root。与 native P_* 复合为 G(û)=P_*(t,y,z(û)/B)。在 incidence 处 native z-derivative upper与二阶 bound给 |X−G|≤K a_fit。G 在复 enlargement 上 holomorphic、关系次数固定。第二次条目 floor给 real norm 数据，Lemma3.1 将其 |G|、|∇G| 控为 K，margin以 core 尺度归一，原坐标 derivative 的 inverse-subpower费用仍为 K。

core lie strictly inside这些 interiors；用 bounded overlap cover或邻 core处理边界。有限 K 个 centers/roots 的 graph description只用于分析支持，最终 atlas 不编码这些 analytic branches 或 masks。该安排覆盖 tiny curvature 和 unused escaping root，不需新增 coefficient-height lower。

## 5. 固定 A 分母与 projected cap

T_A 把 t 改为 τ=(t−t_A)/q_A，把 Z=e_Z·y 改为 ζ=(Z−Z_*)/q_A，保 X=P_* 及原 trajectory index。定义

\[
\lambda_A=\frac{(T_A)_*(\mu_{\rm prep,\gamma}|_{I,A})}{q_A\nu_\gamma(A)},
\qquad R_A=\omega_\gamma q_A\nu_\gamma(A).
\]

因原 μ≤νdt，λ_A≤ν_γ(·|A)dτ，是 subprobability。ΣR_A≤1 且 ∥μ_prep∥=ΣR_A∥λ_A∥；所有 residual 使用同一 denominator，绝不除其 current success mass。

固定 original t，ζ 宽 b 的 strip在 A-domain 内面积≤K₀J_A b：其 normalized linear functional norm为 ∥D_A^Te_Z∥/q_A≥1/K₀。native lower与 quadratic monotonicity使 X 宽 p 只需 K₀ 个 old hidden bins，积分 pure cap、dt=q_A dτ 后 projected ceiling≤Kp^d J_A/ν_A≤Kp^d。最后一项只用 diagonal 的 (10.12)。

terminal ζ′=e_Z·V 给宽 N^{-v} 的 tangential velocity，C 又把 normal V 固定至 K₀g_C；v≤u₁<u 时需至多 K₀ 个 old full-V bins。只在 good sampled joint-upper entries用 N^{-Sv} 分子，并对 good s₁ ancestors 求 pure denominator和，再作同面积积分。不能把 exceptional mass 乘小 angular factor，不能用 all-world 平均代替 within-A ceiling。

## 6. 支持计数：whole-domain 收费和 time error 的抵消

固定 A/projected cell 及碰到它的 Q₁ time block。q_Aσ≪q₁，最多两个 blocks。每个 compatible Q₁ 的 center在接触时距该 cell 的 tangential 位置≤K₀q₁，normal 距 C affine center≤K₀q₁g₁。由 n_C·(y₁′−y_C′)=O(K₀g₁) 和 bounded tangent velocities，该关系在**整个 Q₁ block**保持。frame angle≤K₀g₁，使它的 whole spatial domain包含在同一 moving box，面积≤K₀q₁²g₁。

故可以收费的是原 W_γ,I,Q₁ 整质量，而不只是 cell 内最后交集。zero-depth cap及 disjointness给

\[
L_1 q_1\nu_\gamma(Q_1)/K\le K q_1^3g_1,
\quad\nu_\gamma(Q_1)\asymp_{\log}n(r_1)q_1^2g_1,
\quad L_1\le K/n(r_1)\le Ka^{-d}.
\]

这是同一个固定 A/cell 的估计，无须 sum all C 或 conditional-A witness floor。

对同一 graph entry 的两 occurrences，|Δt|+|ΔZ|≤K₀q_Aσ，且 n_C·Δy=n_C·y_C′Δt+O(K₀g_C)。写 n₁=c₁n_C+c₂e_Z，|c₂|≤K₀g₁，**先减同一个 y₁′Δt** 得

\[
|n_1\cdot(\Delta y-y_1'\Delta t)|\le K_0(g_1q_A\sigma+g_C),
\quad |\Delta\widehat u|\le K_0\left(q_A\sigma/q_1+g_C/(q_1g_1)\right).
\]

这里 time error 的 g₁ 在逆细轴前抵消。若只用 absolute center motion O(Δt)，会凭空引入 g₁⁻¹，无法控制任意 tiny g₁。原论证没有此错。

两项为 N^{-M+ks₁+o(1)} 与 N^{-Δ_i+2u+ks₁+o(1)}。M>1+s₁+ks₁、Δ_i→∞，使其≪a=N^{-s₁}。G 的 derivative upper及 |X−G|≤Ka_fit≤Ka（profile-depth差只添 diagonal K）表明每 entry在 projected cell 只遇 K 个 a-bins。乘 L₁和每label K条 graphs，得每cell Ka^{-d}、总 Ka^{-d}σ⁻²。μ_prep 从此固定，两 mesh 条件均在任何 residual下保持。

## 7. 每 residual 的 candidate 与 finite greedy coverage

取任意 μ_res≤μ_prep、质量≥c p_path，仍以 q_Aν_A 定 λ_A,res。由 ΣR_A≤1，某 A 有 ∥λ_A,res∥≥c p_path≥1/K。以固定 probability prior ν_γ(·|A)调用已完整支付的 8.2，c=1、terminal angular gain，得 β∼_log1、whole-unit-A-block fit F，系数≤K、误差 Ka、原 residual incidence mass≥q_Aν_Aa^d/K。center motion/ranges bounded K，故 adapted norm转 ordinary quadratic coefficient只费 K。

在每 A 预设 coeff≤N^δ、whole-block error≤aN^δ、residual mass≥q_Aν_Aa^dN^{-δ} 的资格。插入时把所有尚未分配且满足该 whole-block fit 的 A-trajectories给第一测试，assignment不依 incidence time。每次删去 trajectory mass≥ν_Aa^dN^{-δ}，最多 N^δa^{-d} 次。分析 residual只判 eligibility，不成为输出 predicate。

若 covered fraction/ p_path 沿所有进一步 subsequence趋0，未覆盖 measure仍 substantial；8.2 再给一条最终符合固定资格的测试，反 greedy终止。因此某 further subsequence有 ∥μ_c∥≥κp_path，κ>0固定。单candidate的小 floor只用于次数，不被误当最终 coverage。

## 8. 原 posterior pair、bad-group 分母与 Cor3.4

μ_c 是 unnormalized 原世界质量，o=(p₁,A) 的 pushforward m_c 也不归一。Π=∫π_o⊗π_o dm_c(o) 两 incidence marginals恰 μ_c，总 mass恰∥μ_c∥。只有 condition on 同一个 o 后独立重抽；原 indices/base 并无独立性。

同 exact original base和 terminal hidden bin，native derivative/curvature给 |X₁−X₂|≤K₀N₀⁻¹。whole fits给 |F−G|≤aN^{O(δ)}。若 coefficient distance>a^{2θ} 的 pairs占固定比例，以 Σωq_Aν_A≤1 找 γ,I,A，使 bad mass b_A≥q_Aν_A/K。除 b_A 后每色 marginal≤(q_Aν_A/b_A)λ_A≤Kλ_A。这一步支付 tiny-world/tiny-A 的真实分母。

固定 polynomial index 在 exact (τ,ζ) 只许 N^{O(δ)}个 X_a bins，因此 index-base ceiling≤KN^{O(δ)}a^d。每色列表≤N^δa^{-d}，取该列表 uniform probability ρ_f，则 a^d≤N^δρ_f；所以 Cor3.4 要求的原 index-base product upper确成立，不是免费重设 active conditional weights。

用 R=a⁻¹、M_norm=1、Δ_match=a、common reference0。bounded K 的 range变化给固定 comparison domain、关系次数2、holomorphic margin；coefficient discrepancy>a^{2θ}给 norm gap≥a^{2θ}/K>R^{-ε}。所有 norm/list/value/密度 losses为 N^{Cδ}K，Cδ/s₁<ε/2。列表 R^{d+δ/s₁}处于 Cor3.4 的 d+ε 范围，d≤d₀；normalized pair mass1足够。因而其匹配矛盾排 bad fraction。没有先强制 π_o 为 uniform，也没有丢掉 m_c(o) 的权重。

## 9. 合并 coefficient bins、实际原 test 与 lower failure

六coeff bin宽 a^θ，good pairs距离≤a^{2θ}≪a^θ，只需 bounded neighbor lists。对每 o 的 bin law β_o，max_b β_o(L(b))≥∫β_o(L(b))dβ_o(b)。积分保固定比例 aggregate μ_c，不选单一 tiny polynomial。再与 actual A-list at p₁复合，list大小只增 actual K_path 幂。

每 A/bin用 binned coefficients F̃，合并先前 whole assignments。原 test为

\[
P_{new}(t,y,w)=P_*(t,y,w)-\widetilde F\big((t-t_A)/q_A,(e_Z\cdot y-Z_*)/q_A\big).
\]

total degree≤2，whole-block value≤aN^δ+K a^θ≤N₀^{-c′}，因为 s₁−δ>c′、θs₁>c′有固定 buffer。P_new,w=P_*,w，P_new,ww=P_*,ww；原 native upper在wholeblock保持，lower在原 selected incidence保持，curvature K₀B²强于 K₀B²N₀^{c′}。frame/time保持原 A，故 geometry/derivative slack为 actual K_path 的 fixed powers，time exponent仍 h_A,i→0，不遗留 N^{δ} slack。

在原 μ_ref 上定义 geometric label map：固定 whole trajectory assignment及其 whole-fit/geometry/upper tests，并只在当前 incidence满足最终 derivative lower等 selected tests时输出(A,bin)，否则 failure。failure永不入列表。native inheritance使 μ_c 上这些测试自动成立；这个限定仍须显式保留，避免 original posterior选回无效事件。允许 incidence-dependent failure，不改变 trajectory assignment本身的 whole-block性质。

## 10. 全原 law恢复、有限编码与真正矛盾

每 A只存 ordered finite tests、各whole-block fit和 priority/merge table。轨迹上 x、F皆quadratic，逐测试消去单一time quantifier为 fixed-format semialgebraic；不对一个 N-dependent giant formula误用 fixed-complexity QE。图分支、cap masks、residual search、posteriorselector均不编码。coeff≤N^δ，旧 native/坐标/逆q_A及A系统tempered，测试数≤N^δa^{-d}；全部 original complexity有预先固定 polynomial bound。

用 Lemma4.12 的输入为 **原 unnormalized μ_ref**、任意analytical submeasure μ_c≤μ_prep≤μ_ref、上段geommap和原 observation p₁。O=(p₁,A)只用于证明列表；最终 unknown A不直接可见，而通过 old actual A-list at p₁取union。original path/internal indices也只作joint tags，不交给selector。保 raw success≥cκp_path，不把 μ_c 或各 posterior换成质量1后遗失分母。

原 joint law（无analyticalmask）在 (t,y(t),剩余coefficients)中Jacobian1。finite polynomial sign boundaries、density heights/ranges及 fixed-format测试给 quantitative TV；取 original mesh足细使 e=O(N₀⁻¹)，cellwise最大非failure labels保 m−2e，列表数不增加。hidden bin作为原 discrete tag，无需与新basecells对齐。仅表内容来自可测搜索，其复杂度由finite表大小控制。

因此 actual输出覆盖≥cκp_path−O(N₀⁻¹)>p_path/log N₀，条件为 p_path≥K_path⁻¹及 N₀⁻¹K_path log N₀→0。这与 fixed-i excluded range中的预定guard矛盾。关键是一个 fixed fraction，而不是在最后仍只拥有 N^{-o(1)}、可能小于1/log的 coverage。

## 11. 最后 completion 不需要新 parent true floor

新 atlas 的 label c=(A,b) 有自己的 full assigned prior ν_c；它一般不等于 ν_γ(A)，也不具 new true floor。将其 depth c′ known atlas送入 Lemma2.13，须用 ν_c，不能沿用 projected λ_A 的 ν_A。设 Z=Σ_cω_γq_Aν_c；原成功 M≤Z≤1 且 M≥p_path/log N₀，所以新 weighted selected mass M/Z 和 Z⁻¹均有 actual subpower控制。

新 worlds conditional priors、version2 native P_new/a_c′、B′=B/a_c′、time/spatial affine maps皆符合原 exact model。terminal label knowledge给 n′(1−c′)∼_log n(1)J_A/ν_c；在更早 relative s只需 n′(s)≤N₀^{o(1)}n(c′+s)J_A/ν_c。置 t_c=log_{N₀}(J_A/ν_c)，则

\[
f'(1-c')-f'(s)\le f(1)-f(c'+s)
\le d_i(1-c'-s).
\]

任意巨大 absolute t_c完全抵消，不需求新 n′(0)∼1，也不用假 intermediate density equality。新 velocity bins经 D_A/q_A映至 old balls、terminal p₁-known label给相同因子，故原 angular参数在新较短 length范围仍适用。删 reciprocal-polynomial light charts及homogenize属于原2.13，并保上述 actual质量。因此新问题属 C(d_i)，即使新 parent非true。

取新问题 terminal true child，m′_d/q_d≥n′(1−c′)J_d/K。原量为 m_cd=q_Aν_cm′_d、q_cd=q_Aq_d、J_cd=J_AJ_d，故

\[
m_{cd}/q_{cd}=\nu_c m'_d/q_d
\ge n(1)J_AJ_d/K.
\]

这里使用的正是 **terminal equality**，完全不依新 parent floor。whole assignments及native tests按2.13复合，于是 H(E_i)≤h_A,i+H(E_new)≤h_A,i+k(d_i)(1−c′)。对 fixed large i 用 h_A,i<kc′/2，令 i→∞便是(10.19)的严格矛盾。无需额外宣称 E_new 本身 maximizing，亦不先给其 absolute density下界。

在原前半输入及 8.2 已完整支付的条件下，后半证明闭合；未发现保全部原假设的反例。本人的 root全稿/A前半正式全文独审已归档 `research/reviews/R0036_graphs_and_actual_atlas_review.md`，包括修后 d≥0 依据；本主稿后半本身不代替该独审。正有限ℓ分支、完整2.17/readout、具名高级输入与KT及高维目标均未因本稿消失；不认证fullsource、无条件六维17/4或新颖性。
