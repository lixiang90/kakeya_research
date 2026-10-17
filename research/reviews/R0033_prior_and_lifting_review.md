# R0033：完整 critical paths 的 prior、lifting 与有限初始界独立审查

2026-10-17，B 独审。已实际通读 root `notes/10_source_audit/critical_paths/R0033_critical_paths_full_proof.md` 全部 §§1–11，及 A `R0033_extremal_and_narrowness_audit.md` 全部 §§1–11；对照原 OAI4 2.7、2.13、2.15–2.16、4.1–4.3 和 saved companion `05-inputs.tex`。不是仅审我自己的 normalization audit；我自己的主稿不计作独立认证。

**结论：root 整合稿和 A 的极值/窄度论证在所列原模型、假设及具名输入下通过本次独立逐步审查。未发现尚待修复的数学缺口。** GWZ2026 Theorem 1.1 的三维 set estimate 保留为高级输入；原 TCM/ASM/TEX 的已核范围及标准基础不扩大。该结论不认证后续 OAI4 排除所有 bad problems，不解除 DIM-001/FSD-001 的完整源条件，未经外部同行评审。

## 1. 典型 cap 与原 law

root §2 的顺序正确：先删 joint upper/pure lower 失败 fine entries，固定 angular bin 对 good numerators 求和，再除对应旧 pure denominator。omitted-mass comparison 在新 sampled states 转移 cap；任意后续 inverse-subpower restriction 的 denominator 损失另用 2.3。它没有声称未删 law 的 angular maximum 对全部 bins pointwise 成立。

slow finite-grid 实施只在每一 fixed exact problem 内进行，坏质量预算相对实际 selected mass选择。需要 tempered 输出时使用原 joint law 的 2.4 lookup table，不把任意 analytic good mask 追认为 tempered prior。A §3 同样先由 coarse conditional cap 乘 coarse pure typical density，未将 n(L)误用作 coarse endpoint density。

root §1 对 2.5 的使用保 fixed compact depth ranges和固定 polynomial mesh：density-type 数量缓慢增长为 subpower、上下密度先截 polynomial 范围，再 restriction/refinement 形成 Lipschitz profile。它没有对外层 i 的不同 exact problems 要求统一 polynomial complexity 或 density height。

## 2. Normalization 中的两个不同 Jacobian

root §3 的新 world 权为 ωγ qν_c/Z，Z∈[M,1]；trajectory prior 是 νγ(·|A_c)，independent uniform new time，而非按 selected success 条件化。Observation base 的 Jacobian 是 qJ_c；product-prior normalization 为 qν_c，故 within-world 因子为 J_c/ν_c。world weight、Z、或额外 q 都没有混入该公式。

系数坐标的 Jacobian 是另一个对象。v1 对 hidden coefficients triangular，base change affine，v2 只需 affine coefficient reparametrization；两者均可逆、constant Jacobian、polynomial inverse。极轻 assigned-prior charts由 polynomial count和 selected≤qν_c预算先删，故保 piecewise-constant full-coefficient prior 的 tempered 格式。root/A 未假设 arbitrary success-conditioned law仍有此性质。

v2 的 native test为 P_parent/a_r，B'=B/a_r；不是无条件沿用旧 native。parent curvature除 a_r 后为 K B²/a_r²，正好是 K(B')²。v1 沿完整 assigned trajectory 仍为二次函数。hidden grids在固定 chart/exact base时只有 bounded overlap，v1 的 offset不需要全局固定。

## 3. Terminal、intermediate 和 cap 的方向

parent terminal-known 给 terminal equality n'(L−r)∼log n(L)J_c/ν_c；arbitrary earlier refinement只给 n'(s)≤N^{o(1)}n(r+s)J_c/ν_c。root (N2)/(N3) 和 A (1) 的方向一致：这足够控制 new endpoint profile，**不足以提升 intermediate true floor**。

prepared true parent在 p_r 已知，由更 fine observation亦可列它，才恢复 intermediate equality。root 的 intermediate lifting 全部穿这种 prepared parent；general terminal-known atlas仅用于 terminal lift。二者没有混用。

velocity map的旧像半径≤K N^{-u}由 ∥D_c∥≤Kq 保证；只需 K 个旧 angular bins。good old joint numerators先求和，再乘 J_c/ν_c，与 terminal pure equality比较，故同 S,η 保留。新 u≤η(L−r)在旧允许范围内。

## 4. Whole assignments 与真实 mass 回传

root §4/A §2 的 q_cd=qq_d、J_cd=J_cJ_d、m_cd=qν_c m'_d 正确；child true terminal floor转成旧 n(L)J_cJ_d。v1 拉回 test为 w−F−a_rG，v2 为 a_rQ；后者 curvature恰为 K B²/a_{r+s}。tests仍 total degree≤2。

可把 root 关于 global success 的文字写成一个精确核算：若 parent normalization 常数为 Z，新 child system 的 weighted selected mass为 M'，拉回旧问题的 weighted mass就是 **ZM'**，因为新 world 权是 ωγ qν_c/Z。Z与 M'均 inverse-subpower，故有限次回传仍有 inverse-subpower成功；无需逐 world 的 success 下界。这也解释为何只能保 full assigned prior，不能用 current success重置 ν_c。

finite history labels、dyadic nested time partitions、whole-trajectory pullback和 determinant乘法给实际层。parent old label与child transported observation的有界 overlap保证 short lists相乘。root 没有只构造 final incidence path后声称它自动携带 earlier floor。

原 4.3 的 conclusion允许保每层 frozen full assignment、原 prior和自己的 incidence witnesses。root/A明确 final path不必饱和 earlier floor。若未来要 final current measure上每层同时有 floor，还需独立支付原 2.11；它不在这里追认为 R32 已审输入，也不是本次路径结论所需假设。B 主稿首段原曾误列 R32 已审 2.11，已按 root 指出删改；最终稿不存在该虚增依赖。

## 5. G 到 weighted plank 的有限链

root §5 的 Bernoulli 证明适用于任意正权和任意多个 repeated indices：取 v_i=ω_i/A≤1，total expectation S≤Cδ⁻²；universal John-box net的个数 polynomial且各 relevant box volume≥c|T|。exponential moment给全 net logarithmic cap，lower-tail给 sample size≥S/2，两事各概率≥3/4即可同取。无任何 min-weight 或 index-count 损失。

同一 tube 的 sampled multiplicity≤C log；每 distinct tube保一个实际 index的 shading，逐 index long density仍成立。原 weighted shading numerator另以 AS|T|控制，因此不要求被保 index捕获全部原 shading质量。small S由逐点总权直接控制，bounded δ段用总权上界。GWZ输入使用 distinct tubes，恰在去重后调用。

whole-time plank到 convex clustering的转换合法：共同延长 tube留 endcap余量，John ellipsoid time diameter≥1；maximal horizontal slice area≤C|K|，固定空间轴及 affine centers给包含所有 counted whole traces的 plank。lower widths≥cδ，upper widths bounded；固定倍 cutoff由 endpoint partition/enlargement支付。marked balls在同一 index内因 time separation而 disjoint，union由 visited cells控制。只有此处需要 per-index long marks，root没有用平均 marks代替。

连续 law按 fine rounded coefficients和 finite mark sets分组，权仍为旧 prior质量。即使 mark sets数量很大，有限估计常数独立于 index数；这些 labels不输出。whole traces而非仅 marked pieces通过扩大planks恢复。故原 2.15的有限部分通过，残余高级责任准确限于具名 G；未借用 companion完整 maximal结论。

## 6. Proposition 2.16 的 greedy、witness 与 padding

root §6 的 G在 p_L 下 short-list已知：whole block native X变化≤Kq，hidden-bin Taylor误差≤Ka_L；v2 curvature项≤Ka_L²。P*−b_G/v1 w−b_G给全 block test，native derivative及 terminal curvature条件合法。

空间除 Rq后，原 group prior未重新归一化；group base density lower为 n(L)J0，J0=(Rq)^j。工作 mesh指数 D先选到足够支付 tempered/TV，再定 ξ、ε。greedy每步 mass至少 reciprocal-polynomial，uniform于 ξ<1，endpoint whole-containment和 successive exclusions保持 finite encoding；不要求 intermediate measurable搜索可计算。

覆盖不足时，用原 assignment budgets删短 duration entries，剩余每 trace有 K⁻¹ normalized duration；weighted averaging保某 group的 surviving mass≥m_G/K。visited cell数以 **原** m_G和 **原 whole-cell witness floor**计，没有给 current残余cell偷加同一 floor。moving to bin centers只付固定 enlargement。

j=1加入 independent static dummy仅用于 analytic estimate，未将其冒充 full-dimensional tempered new exact prior。projection的 chord bound≤Cuv/W由 rectangle几何成立；accepted dummy fraction至多此界，故恢复 original trace weight/W。projected whole-time interval仍属原 greedy允许族，marks duration也保留。

所得 incidence mass比 greedy threshold强固定正幂，只要 Dε<ξ/4；其余 slack subpower可吸收。ξ↓0在每 fixed ξ/ε有效以后慢选，而 polynomial step count、工作D和 degree bounds均统一于 ξ<1。故 H(E)≤L通过，范围仍仅原 j=1/2和具名 G。

## 7. Horizon composition、正 k 与 relative profile

root §7/A §§3–4 未假 near-infimum attained：任意 tolerance实际选 terminal true child，terminal equality lift后取inf。coarsening的 angular cap和它自己的 terminal slope cap分开；(H1)本身无需 coarsening属于原 C(d)，但以 k(d')上界它时确实另查 cap。

length-one normalization以 N'=N^L实行，L是该 fixed exact problem的实际常数；S,η保持。k≤1来自已付 2.16。正 k使用统一 fixed d0<1 的 TEX常数C，选 e小于各自 H及允许尺度；remaining长度≤Ce和 composition给 ratio≥3/(4C)。没有要求 e或problem-dependent阈值在 outer i统一。

root §8/A §5 的 secant minimizer逻辑通过：strict lower secant使 r_i−a≥c；在[a,r_i]得 d'' cap，x<a另得全局<1 cap。固定 i使用自己的 TEX constants，令剩余段完全落局部 d'' cap区，再由 terminal equality/intermediate upper推出新 C(d'') bad problem，矛盾。随后 H_out=0与正 k破坏 maximization。compactness仅作用 f_i−f_i(0)，不作用绝对 f_i(0)。

## 8. 实际节点、嵌套层与双极限

root §9/A §§6–7 用慢 α_i高于 profile error，在[0,r]最小化 f_i−(d*+α_i)x，得 actual r_i→r和该 actual endpoint的 cap；不是把 limiting target r直接当已证 cap的 endpoint。

coarsened horizon夹在 H(E_i)−k(d_i)(1−r_i)与 k(d*+α_i)r_i之间，所以除实际 r_i后 maximizing。选 actual near-inf true systems，经 2.10 prepared；remaining horizon再由 composition/class upper夹住。任何合法进一步 restrictions的 H只能上升，但 class upper仍在；A明确不声称 H在restriction下恒定。

finite grid逐段使用 limiting fraction确定目标，实际选择节点趋它；归一除实际 segment length，回传乘实际 length。最后fraction1直接取terminal系统，结尾严格为深度1。有限次 exact subsequences/outer subsequences及 prepared true parents使每层 actual whole assignment和 floor可保，而非仅指数形式路径。

每 fixed i先取自己的 exact N0→∞形成 exponents和H competitors，然后 outer i→∞。未以单个(i,N0)diagonal替代内层 infimum，亦未把固定有限 grid结论扩大为一个同时实现全部无限 grids的系统。

## 9. Finite/infinite ℓ

root §10/A §§8–10 对 ω、ℓ 的 sup/inf不要求 attained。finite ℓ先选 base whole sequence ω_base≤ℓ+ζ；每新 maximizing sequence的 ω≥ℓ，选 attainable limsup再取 subsequence给 relative segment lower。新选择始终能拉回 base竞争者，故最终 **实际 composed terminal system**才受 ω_base upper限制；没有给每段免费加同一 upper。

现稿已采用任意 segment collection/complement的精确计算：实际总length为 a_i时

\[
 (\ell-\zeta)a_i-o_i(1)\le\sum b_{i,j}
 \le\ell a_i+2\zeta+o_i(1).
\]

这同时控制 cumulative和相邻 increments，O(ζ)常数无需随 fixed grid点数增长。determinant/time乘法给窄度精确相加，不需 axes平行。

ℓ=∞时，ω=∞只是 attainable limsup的sup无界；root先固定整数threshold取实际竞争者，再选足够大的 outer index，随后让threshold增加。每 chosen index内部仍是完成原exact极限的系统。finite positive-length段的实际长度有统一正下界，故 relative divergence可转成旧单位 divergence；不对 vanishing-length段作此推论。

## 10. 最终状态与退出范围

正式审查通过范围：原 2.7/2.13、G条件下的 2.15/2.16，以及据此配合已核 TEX 的 4.1/4.2/4.3四项完整结论。root/A对上述范围未留 pending数学修复。B 主稿的 2.11追认措辞已修；root finite ℓ估计已按 collection/complement形式收紧，本 review核的是修后现稿。

后续 excluded improvements、tangent/original-resolution guard、local branch构造、完整 bad-problem排除及有限 readout尚不由此得到。不能因本轮通过便给完整 OAI4、无条件六维17/4、五维或一般 Kakeya加“已证”状态。按 R33 macro，下一阶段须重新盘点实际责任/可证伪收益，不自动沿论文续审。
