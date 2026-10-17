# R0032：原 terminal extension 前半段的 frame/graph/matching 审计

2026-10-17，子任务 A。已读恢复入口、R32 spec，逐式核原 OAI4 Lemma3.5 part1（PDF36–40，文本约 1945–2196 行）及其实际 Def2.1/2.6/2.8、Lemma2.9/2.10/2.12 接口。唯一 main 是完整 terminal extension；本稿只支付原 paired prior 至 local graph comparison，不把它单独登记为完整 Lemma3.5。

**结论：此 part1 的原质量、二维 frame、heavy-entry、stable graph 与 Cor3.4 group 链可严格闭合；未发现保全部原输入的反例。** 必须区分两个 pre-deletion mass 层和两套删轻常数，不能用同一个后增 C′ 反过来改变已固定 CU。后续 anchor、freeze time、whole assignment/old-pL knowledge 仍由 root/B 另核。

## 1. 原 prior、尺度及已付基础的调用范围

记 N=N₀、δ=N^-L，先在各 world 取 w_new=Bw_old，使 derivative unit 为1、native/terminal hidden bins 宽 ar。B 和 B^-1 tempered，逆变换留到输出。本稿始终在原 trajectory probability ν_γ、原 world weights ω_γ、独立时间 priors 上工作，不把 packet prior 条件化到后来的 pair success。

old true terminal system 用 Lemma2.10 准备，使 labels known by pL 且每个 original used label 的 true floor 仍在。Lemma2.12 的 largest-axis fullness 是真实额外调用：known labels 加原 joint angular cap 排除轴长比 q₀ 固定幂小的 substantial portion。root 另完整支付此基础；本稿不把它当 Def2.8 自动给出的等式。

whole-label homogenization 后，version2 的两 singular radii 为 `q₀,q₀g` up to K₀，g=N^-β、β≥0；version1 的 single radius 为 q₀，记 g=1。定义

\[
n_Q=n(L)q_0^j g. \tag{1}
\]

在各 old q₀-block，每个保留 label 的**原 selected mass**除以 q₀ 至少 nQ/K₀。select whole labels 不改变该 label 自己原 floor；以后的 incidence/pair masks 则不再宣称有 floor。

## 2. 真 paired experiment 与两个 one-time marginals

取 nested dyadic q₁-block I，q₁/q₀≈N^e、e<h。world/block 内定义未归一化 measure

\[
d\lambda_{\gamma,I}=1_{E_{old}}(\ell,t_0)
1_{E_{old}}(\ell,t)
d\nu_\gamma(\ell)\,\frac{dt_0}{q_1}\frac{dt}{q_1}.
\tag{2}
\]

global weight 是 ω_γq₁，且 `Σ_{γ,I}ω_γq₁=1`。置 s_I(ℓ)=q₁^-1∫_I1_Eold dt。global pair mass 为 `Σωq₁∫s_I²dν`，Jensen 对这一个总 probability reference 给其至少 old total selected mass 的平方，故 inverse-subpower。

将另一时刻积分掉，source marginal 为 `1_Eold(ℓ,t₀)s_I(ℓ)dν dt₀/q₁`。global 乘回 ωq₁ 后≤原 old selected incidence law；witness 同理。block 内只可写 ≤old law/q₁。此 q₁ 在后来变 τ=t/q₁ 时取消，不能在 physical t-density 中漏掉。

相关成功条件只作未归一化 restriction，以上 domination 永久保留。不需要 t/t₀ 在 retained pair 条件下独立；独立仅用于最初 (2) 的 raw experiment。

## 3. old-label count、外推和 opposite-time derivative

在一个 old subblock，assignments 在 ν_γ 下 disjoint，且每 label 原 normalized-time floor≥nQ/K₀，故 labels 数≤K₀/nQ。new I 含 O(N^e) 个 old subblocks，因此

\[
\#\{old\ labels\ in\ \gamma,I\}\le K_0N^e/n_Q. \tag{3}
\]

此计数只借准备时的 old floors。所有后来 masks/prunings 不重设一个 label floor，再用 (3) 计算成本即可。

沿原 assigned trajectory，test 是 degree≤2 的 time polynomial（version1 w quadratic、version2 w affine），Pw 是 degree≤1。old block bounds 向 new I 外推，给

    sup_I|P|≤δ N^{C₀e}，    sup_I|Pw|≤N^{C₀e}。

其中 C₀ fixed，degree interpolation 只花 `(q₁/q₀)^2`/`q₁/q₀`，不花 tempered complexity exponent。spatial affine error 同样只放大 N^e。

对某 test，先固定 trajectory 及它自己的 selected time/label，其 affine Pw 在 I 上 maximum≥K₀^-1。affine scalar sublevel 的相对长度 `|{|Pw|<N^-e}|/q₁≤C K₀N^-e`。另一个 sampled time 仍是 raw uniform dt/q₁；加其 selection 只减 bad mass。两 colors 分别这样计费，总 opposite-time derivative failure 为 power-small **absolute pair mass**。这不是条件在 pair success 后重新假 uniform time。

在两个 vertices 同时删去原 p_r 密度>N^e n(r) 的 entries（fixed grid spacing≤e、含0/L），及 joint `(pL,[V]_{N^{-R_ang e}})` 密度>`n(L)N^{(1−SR_ang)e}` 的 entries。one-time domination 使所删 pair mass 受原典型异常控制；`R_ang e≤ηL` 必须留作最终 e/L 限制。后面的每次 cap 积分均对这个已剔除 exceptions 的原 good submeasure。

## 4. 二维 normal exception (3.29)

仅 version2 有此步。old spatial bounds 在各 old interval 上给 V 位于 normal n_A/n_A′ 的两 strips，normal widths K₀g。若

    sin angle(n_A,n_A′)>g N^{R_ang e}<1，

则两个 strips 的交直径≤K₀N^-R_ang e，所以只需 K₀ 个 angular grid bins（width N^-R_ang e）。若阈值≥1，exception 为空。

固定 source A。witness spatial point 在 A 的 extrapolated rectangle内，面积≤`q₀²g N^{C₀e}`。source test 在该 witness point有 small value 和 opposite derivative floor，Lemma2.9 以 ε=δN^{C₀e}、b=N^-e、bin widthδ，给至多 N^{C₀e} 个 hidden bins，已增大 C₀ 吸收额外1。old A′ knowledge 在每个 pL 只给 K₀ 个 A′，对每个再枚举 K₀ angular bins。

应用同一个 capped original witness marginal，再用 (3) 求和，exception total bound为

\[
\frac{K_0N^e}{n_Q}\cdot
q_0^2gN^{C_0e}\cdot N^{C_0e}\cdot
n(L)N^{(1-SR_{ang})e}
=K_0N^{(2+2C_0-SR_{ang})e}. \tag{4}
\]

normalized time integral 是1，没有额外 q₁ 或 q₀。cap 对每个 retained angular entry pointwise 有效，枚举的 bins 可依 A/A′/observation 变化；不把原“sampled typical upper”未经删异常就当全 bins 的 upper。先 fixed C₀，再选 R_ang 大使 (4) power-small，最后才限制 e/L。

## 5. common D：rotation 只作用于相对误差

记 `g#=min(1,gN^{R_ang e})`。source A 确定 D：orientation 以 g# grid rounded，normal velocity 以 g# grid，new-block midpoint 的 tangent/normal positions 分别以 q₁/q₁g# grid；tangent center velocity设0。g#=1 时取固定 axes/static midpoint。

对真实共同 line，old centers 在 new midpoint 的 errors 为 tangent≤K₀q₁、old normal≤K₀q₁g；velocity errors 为 tangent≤K₀、normal≤K₀g。retained normals相距 O(g#)。在 source rounded frame 中，将 A/A′ 各自 center 与 **共同 line** 比较，rotation error因此至多 `K₀q₁g#`/`K₀g#`。它不乘一个可能远大于 q₁ 的 absolute midpoint。

故 A′ 可先枚举 constant 个候选 source orientations，再在每个相同 rounded frame 中预测 A 的 position/velocity，仅有 subpower grid neighbours。A→D 为 deterministic，A′→D 为 K₀-list。这种 relative-frame 兼容不能换成“两个各自 rounded frames 的绝对位置近”，后者没有所需精度。

common subpower dilation后，在 z=(τ,ξ) 的 fixed box 内 traces 和 normalized speeds bounded。spatial Jacobian 满足

\[
J_D\le K_0q_1^j g^\#\le N^{C_{frame}e}q_0^jg, \tag{5}
\]

因为 g#/g≤N^{R_ang e}。C_frame 可依已固定 R_ang，不依 β、L/h/e 或 complexity exponent；每个 fixed e 下 subpowers 最终吸收。

## 6. source-base density (3.31)：witness 条目也不条件化

对 fixed entry (A,D) 或 (A′,D)，推 (2) 的 current restriction 到 source z₀，积分另一 time。它仍被原 source selected marginal 支配（block normalization除以q₁）。无论这是 source 还是 witness entry，其 equation 在 source point 有 value≤δN^{C₀e} 和 own/opposite derivative floor。Lemma2.9 给 N^{C₀e} terminal hidden bins。

用 source vertex 上已经 capped 的 pL density，且

    (dt₀/q₁)dy=J_D dτ₀dξ₀，

得到该**未归一化** entry 的 z₀-density

\[
\rho_{entry}(z_0)\le n_Q N^{C_{base}e}. \tag{6}
\]

这里 (A′,D) 不由 source observation known 也无妨：它只是原 source marginal 的 restriction；extrapolated witness test 负责限制可用 hidden bins。没有 conditioning on A′、entry mass 或 pair success，故没有遗漏分母。不能把此 upper 误写成 normalized entry law 的同一 upper。

## 7. 第一轮 heavy entries 与 stable simple graphs

先 fixed C_entry，删除 (A,D)/(A′,D) raw entry mass小于 `nQ N^{-C_entry e}` 的 entries。每 old label 至多 N^{C_D e} 个 D options，(3) 给总成本≤`K₀N^{(1+C_D−C_entry)e}`；加两 colors 后仍 power-small。所存 lower 是**联合删选之前的 frozen mass**。之后不需要每个 entry current mass继续大。

写原 test 为 `(c/2)w²+b(z)w+a(z)`，c=Pww。选 early C_A>C₀+4。若 `|c|≥δ^-1N^{-C_Ae}`，用 `w−Fctr(z)` 比较，`Fctr=−b/c` affine，且沿 assigned line whole I 的 value≤`δN^{(C₀+C_A)e}`。此转换仅依 old label/D，不依后来的 t₀/trajectory。

否则保原 test。在 source point，`|2cP|≤2N^{(C₀−C_A)e}≪|Pw|²`，因此

\[
\tfrac12N^{-2e}\le\mathcal D(z_0)=P_w^2-2cP
 \le N^{C_{disc,0}e}. \tag{7}
\]

替换测试的 discriminant 为1。conversion的 value loss C_graph 要包括 C_A+C₀；不要后增 C_A 再回用旧的 Cor value constant。

由 frozen heavy mass及 (6)，该 entry 的 source-base positive-density carrier 有 Lebesgue measure≥`N^{-(C_entry+C_base)e}`，(7) upper 在其 a.e.点成立。这个 measurable carrier 足够，不需对任意非可测“投影支持”作体积断言。固定 degree polynomial Remez/系数范数等价给 converted discriminant 的 coefficients、fixed derivatives 在 fixed complex enlargement 上≤`N^{C_disc e}`。该 argument 用原 heavy entry，不拿后来的 joint/group mass补 lower。

现在 fixed `C_U>C_disc+4`，以 radius `N^{-C_Ue}` 的 finite net覆盖 real source box。每 pair 取离 z₀半径一半内的首个 admissible ball U，则8U上两个 discriminants都离零，源点 (7) lower 与 uniform derivative bound支付这一点。所选 equations各在8U有 simple holomorphic branch、real on real；nearest root或affine branch给

    |w(t₀)−f(z₀)|≤δN^{C_graph e}。

只需 U 对当前 pair admissible，不要求躲开所有 labels 的 discriminant zeros。每label/ball最多2 branches，unused far root不参与 near-w bound。version1本来 Pw=1、c=0，图是原 quadratic F，以上处理不引入额外根。

## 8. M/D/U/jet groups：option count 不依 C_*

对 pair sheets 的 `||f−f′||_{2U}` 在 dyadic [M,2M]、`M≥δN^{C_*e}` 的大差异 events，group by world/I、M、D、U及两个 center-jet cubes（在 U-scaled coordinates、spacing M、fixed sufficient jet order）。Lemma3.1 upper使配对 cubes 为 constant neighbours；finite-jet norm control使每group所有 functions距一个实际 common reference的norm≤CM。

每oldlabel的 D options≤K₀；U net≤N^{(j+1)C_Ue}；branches≤2；固定 M 后自己的 jet cube deterministic，另一cube仅 fixed个 neighbour choices。M range虽然可能有大 tempered exponent，但 occurring branch在 source point近 polynomially bounded w，discriminant floor和implicit differentiation给 fixed jets polynomial bounds，再由3.1 finite-jet控制whole norm。故 dyadic M choices仅 `C_problem logN`，对 fixed e 大 N 时可吸收 N^e；exponent C_opt 不依该 problem complexity。

因此总 group options per old label≤N^{C_opt e}，C_opt 在 C_U 之后确定、独立于 C_*；C_*增加只减少低端 M 范围，不增加 options。

## 9. (3.35) 的真实 group-mass upper

在 group 的每个 source base z₀∈U，实际 w(t₀)距共同reference的值≤CM，因为两 branches 的 approximation error `δN^{C_graph e}` 可由后选 `C_*>C_graph` 吸收到M内。

若 M≤1，选 capped fixed-grid depth r 使 `M≤a_r≤MN^e`。band只遇 fixed 个宽a_r bins，原 capped source marginal和 (5)给

\[
m_G\le N^{C e}q_0^jg\,n(r)
 \le N^{C_{mass}e}n_Q(M/\delta)^d. \tag{8}
\]

其中 cap-class `n(r)≤n(L)(a_r/δ)^d`；fixed depth mesh费用N^{de}可吸收，d≥0且≤d₀<1。所有 densities是原 source vertex law，而非归一化 group。

若 M>1，不能简单按 band 长度 O(M) 数 unit bins，那会多出有害的 M。version1 w 原本 subpower bounded；version2 在原 selected source incidences满足 native `|P*|≤K₀, |P*_w|≥1/K₀`，Lemma2.9 只允许 subpower个unit w-bins。故 depth0 cap同样给 (8)，因为 `n(0)≤n(L)δ^-d≤n(L)(M/δ)^d`。d≥0来自 profile非减与cap-class inequality，负d的非空class不可能。

## 10. 第二轮 group-index floors、原 π 构造与 Cor3.4

现在才选另一个 C_index，删除每group每color `(oldlabel,branch)` 的 pre-joint-deletion marginal小于 `nQ N^{-C_index e}` 的 indices。以 (3)×N^{C_opt e} 计数，若 C_index>C_opt+常数，总 global weighted损失可小于 N^-2e。

若大差异 events 总 mass≥N^-e，则有某 group保 `m'_G≥m_G/2>0`。无需 mG 本身≥N^-Ce；world/group可很小。每color保留index数由原 marginal floors与 (8)得

\[
\#I_{G,\kappa}\le N^{C_{list}e}(M/\delta)^d. \tag{9}
\]

将该 surviving group 除以 mG′ 为 probability。每color先给每index raw weight `a_i=nQ/mG′`，其总和

\[
W_\kappa=\sum_i a_i
\le (m_G/m'_G)N^{C_{index}e}
\le2N^{C_{index}e}. \tag{10}
\]

设 `πκ,i=a_i/Wκ`。group index-base density≤`nQ N^{C_base e}/mG′≤N^{C_pi e}πκ,i`，加 U rescale Jacob只付 N^{O(e)}（实际缩小 U 的 Jacob≤1）。这就是 Cor3.4 所用的两color probability weights；不要求原indices uniform，不要求 mG′ inverse-small-power，也没有把 entry-normalization 分母省略。small π 不额外收费。

norm gap≥M、common-reference norm≤CM、value gap≤δN^{C_graph e}，lists满足 (9)，law为 probability。置 `R_match=M/δ≥N^{C_*e}`。此前全部loss与options constants已固定，取 C_*大使每个 `N^{C_loss e}≤R_match^{ε_Cor}`，其中 ε_Cor低于已认证 Cor3.4 的 fixed tolerance。fixed constants也可吸收于严格余量，R_match→∞。

于是该group不可能存在，得 local norm comparison (3.34) 除 power-small absolute pair mass外成立。Cor3.4 使用真实 common source base z₀与各自 real branches；不借一个重新独立的 pair law，也不把当前floor假设成旧truefloor。

## 11. 必须显式分开的常数顺序

可行前半顺序是：C₀（外推/hiddenbins）→R_ang→C_frame/C_base→early C_A→C_entry→C_disc→C_U→C_opt→C_index→C_list/C_pi/C_loss→C_*。C_A 可更早在 C₀ 后选；关键是 C_entry 在 discriminant/C_U 前，C_index 在 C_opt 后，二者不再同名回增。

最后才限制 e/L，使 `R_ang e≤ηL`，并让本段和后续 anchor/normalization 的总 thickness loss<L。Lemma3.5 的最终 c 需等后续所有 constants固定后再取；本稿不提前认证全proof的 c。e<h保证 nested longer time blocks仍合法。

## 12. 反攻结论与未核责任

没有找到保原 j=1/2、full old trajectory assignments、true floors、pL knowledge、native bounds及cap-class的严格反例。以下偷换均已排除：对 pair-success condition 后再假 uniform time；对 witness entry在source端免费重设prior；用current pair mass给每oldlabel新floor；把normal rotation误差乘absolute midpoint；把 M>1 band按O(M) bins收费；以C_index后增回灌已定C_U；以tiny mG 断言Cor law无控制或反过来免费取消其分母。

本稿只核 part1 至 (3.34)/(3.35) 的实际先验和小幂预算。后续 common complex anchor、representatives、source-time freezing、whole assignments/newselected tests、old-pL subpower lists和tempered编码还需独立核验。原Lemma3.2/Cor3.4已内部重证为具名输入；本稿通过不等于Lemma3.5全文或完整OAI4认证，不解除DIM001条件，未经外部同行评审或重大性声明。到此交叉审查。
