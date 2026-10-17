# R0034：原 Proposition 4.11 的候选转换、原 law 与有限编码审查

2026-10-17，B 独立审查稿。实际读取 OAI4 原 4.10–4.12 全部 statement/proof（PDF61–70），并追读 4.7–4.9 中使用的 priors、budgets、point-state lists 与 fixed-time caps。root 整合稿的独审另在指定 review 完成。本稿不把作者自己的核对计为独立评审。

**本稿结论：原候选转换在以下完整准备与 guard 假设下可逐步实现，未发现保全部原条件的反例。** 这只是源接口认证，不认证之后几何分支必能提供候选，不解除完整四维源/六维条件链的剩余条件。

## 1. Closure 检查和实际假设

TCM/ASM/TEX/CRP 的合法 restriction closure 可再次使用；它们本身不推出下面三项：一个固定 scenario在整个 residual menu 上有足够覆盖、后验 graph labels可换为 whole-block assignments、最终输出有 original-resolution 的统一复杂度。因此 4.11 不是已核 Corollary3.4 的一次等价改名。

固定原 v1/j1 或 v2/j2、有限优化窄度 ℓ、guarded tangent diagonal。N=N0^{ε_n}，K=N^{o(1)}仅作分析；实际可输出的 slack/list必须是 (K_path log N0)^{r_S}。parent weights p_A、probability λ_A^0、其 palette π_A在准备后冻结。parent prior ν_A条件于完整 parent trajectory assignment，λ_A^0≤Kν_A dt；raw prepared-prior restriction等于 s_Aλ_A^0，s_A⁻¹≤K。任何后续 omission只减 numerator，不重置上述 reference laws。

node Q_s 的 a=N⁻s、actual a_Q∼log,N a、time q_s、spatial determinant J_s、full assigned mass ν_Q满足 ν_Q∼log,N a^d J_s，d=d_*<1。候选的 mass始终相对 ν_Q，按 residual parent-time incidence mass除 q_s计，不以当前 selected packet mass代换。

prepared caps、history joint ceiling、point-state ambiguity及实际 spatial fullness是实质输入。原假设是：**每个带 substantial residual的子列，都有进一步子列及 bounded depth、正有限 limiting gain候选。** 只知道某一初始 residual有一个候选不足以作本证明。

## 2. 一个有限 current-floor 辅助事实（本轮新支付）

如准备步骤实际需要多个层/entries同时有 current floor，可使用如下有限预算证明，而不追认为 R32/33 已审过它。每层 i保固定完整 assignments、预算 Σ_cω_c q_cν_c≤1；每 chart最多 D_i entries。固定正 ε_i，threshold为 ε_i q_cν_c/D_i。

反复删当前质量为正但低于 threshold的**整个 entry**，删除后重查所有层。每 entry被删后永久 empty，所以最多收费一次；第 i层总收费≤ε_i，所有层≤Σε_i。有限 polynomial entries使过程 polynomial终止，最后所有非空 entries都满足阈值。删选结果是 finite removed-entry table，不需把“质量小”作为新的 analytic predicate存入输出；不改变 ν_c。再分时间时预算用子区间长度，长度之和仍为 q_c。

这支付原 2.11 的有限重复删除机制。若只需固定 graph/witness bounds以供日后 restriction，则不必在以后每一步恢复 current floors；fixed graph bounds一旦从 retained witness建立便保持。无论哪种用法，不能把最后 path质量当作所有 earlier frozen floors。

## 3. Finite greedy 的 whole assignment 与 countable menu

对一个固定 scenario S，固定 type、bounded depth range、gain c>0、足够小 σ>0，允许 N^σ级分析余量。每个 Q中，测试 eligibility mass只在当前 residual计算；但选中 test后，assign所有尚未分配且满足整个 block上几何/value/upper-derivative条件的 Q-trajectories。time case另要求 derivative lower在 block中至少一处成立，且只有满足 lower的 incidences计入阈值。strip case用整条 trajectory的 affine velocity inequality。

这种 enlargement包含原 threshold witnesses，assignment不编码 analytical residual mask。每 Q的 full prior budget使 time tests数≤N^{dc+O(σ)}，strip rows数≤N^{O(σ)}；可预留若干分之一 σ使原显示的 N^{dc+σ}/N^σ 上界成立。每次删除整条已分配 trajectory piece，有限 priority predicates固定 throughout block。

countable menu取 rational gains/slacks和整数 depth bounds，含任意细 choices。若 c_n→c_*>0，选 fixed menu gain足够近，使所有因 c改变的 exponent误差小于预留 σ/4；这同时支付 value、curvature和 **N^{-dc} mass floor**，不能只比较 fitting widths。subpower K及 node rounding消耗剩余 slack。

若每 fixed finite menu的 union coverage都趋0，slow选择 J_n→∞使前 J_n个仍覆盖 o(1)。删其所分配 whole pieces上的全部 path incidences，剩余 substantial。候选假设给某进一步子列上的正 limiting-gain候选；与一个 fixed scenario最终相容。其 mass witnesses仍在该 scenario的 free trajectories上，违 maximal greedy。这个反证允许 residual可依 menu而变；正是全 residual量词的用途。

因此有 fixed finite menu覆盖 η0>0，finite pigeonhole选一个固定 scenario；每 sample再选一个 node，coverage

\[
 \beta_n\ge \eta_0/(JG_n).
\tag{1}
\]

节点可以随 sample变，仍在 fixed bounded range。β_n log N0→∞来自 G_n/log N0→0；β_n⁻¹=N^{o(1)}另由 diagonal小幂条件取得。前者支付最终 original mass，后者支付 graph matching，不能混为一句“subpower”。

## 4. Counted duration、source marginals 与 strip 真空间输出

在 v2中 P_w沿 affine trajectory为 affine time函数；v1 P_w=1。whole assigned line的 max|P_w|≥N^{-σ}时，|P_w|<N^{-2σ}的 relative time总长≤CN^{-σ}（constant derivative情形平凡）。λ_A^0≤Kν_A dt及 disjoint assignments使总损失为 fixed negative power，故 o(β_n)。未把 selected event假设为 uniform time。

strip case取足够深且同 parent的 true end history E，其 row A_deep预测误差远小于 gN⁻c。若 ||R−A_deep||>gN^{-c/2}，bounded v使非空事件必有足够大的 slope差；于是 v落宽≤N^{-c/3}的 interval。每 preceding Q有≤N^σ rows，用已准备的 **same original history marginal** λ_{A,pre}(E)和 palette joint ceiling求和，总代价≤KN^{σ−Sc/3}=o(β_n)。没有假设 v和 history独立，也不以 sparse conditional history law替换该分母。

raw rows的 coefficient亦须有固定幂 bound：过大 row若还能拟合 bounded velocities，会把 v限制到任意细 fixed-power interval；按同 joint cap、Q history mass≤Kq_sν_Q和 row count收费，违 greedy mass threshold。这一步保证即使先前 priority predicates中保留的未输出 raw rows也有 polynomial coefficient bound。

aligned events满足 R距 actual deep row≤gN^{-c/2}，后者 coefficients是实际 K_path^O(1) bounds。取

\[
 \tau=(J_s/q_s^2)N^{-c/4},
\]

row coefficients bin到 τ。deep label给 R-bin的 actual short list；v的 actual bound使 binning误差仍≤K_path^O(1)τ。再以 q_sτ网记录 midpoint的 Y−R_1^bZ，given exact observed base及 row-bin，有 actual short ambiguity。

旧 Z-center不变；新的 transverse center令 Y−R_1^bZ的 derivative为 R_0^b。空间 columns可取 q_s(1,R_1^b)、q_s(0,τ)，whole-block fit从 midpoint bin和 velocity error积分得到，det=q_s²τ=J_sN^{-c/4}。旧 test、depth、time保持。这是实际 moving spatial chart的 width gain，不是仅一张 time-velocity graph。

保留 earlier priority assignment，合并相同 (Q,row-bin,position-bin)的 trajectories。predictor原身份不在输出label中。输出 raw R coeff超出实际 row bound的部分可删；aligned coverage仍保 fixed fraction。

## 5. Time graph比较的 base marginal 和原 witness

记 m_Q=p_Aq_sν_Q，Σ_Qm_Q≤1。一个 time candidate index在 counted occurrences上的 unit-Q-base marginal满足

\[
 d\mu_i(u)\le m_QN^{-dc+O(\sigma)}du.
\tag{2}
\]

理由：value/lower-derivative测试至多需要 N^{Oσ}个 a'-hidden bins；pure cap为 K(a')^d，base Jacobian为 q_sJ_s，且 a^dJ_s∼ν_Q。raw parent-prior eligibility law受同 cap支配，或与 λ_A^0相差固定 s_A factor≤K，故亦合法。

每 test最初达到 greedy threshold的 **原 matched witness** 质量≥m_QN^{-dc-Oσ}；除 (2)得其 base projection volume≥N^{-Oσ}。后续 whole-line assignment enlargement不会销毁这份冻结 witness。不能对每个 later selected subbox免费加同一 mass floor。

高 curvature |P_ww|≥N^{-Cσ}/a_fit时，用 affine center，whole line error≤a_fitN^{Oσ}。其余测试的 D=P_w²−2P_wwP与 w无关；在 retained counted points上 D≥cN^{-4σ}，其值及导数由原 matched projection和固定次数 Remez控制为 N^{Oσ}，允许 complex K_path-sized box。

subdivide time及 midpoint spatial bins到 ρ∼N^{-C'σ}。comparison domains为固定倍 K_path^O(1)ρ的 complex balls/polydiscs并留 margin；C'足够大，使 D变化远小于 N^{-4σ}。保 certified test–subbox choices后有 stable simple real branches，或 nonzero linear coefficient。member whole short piece上的 identity保证 P_w不穿0；midpoint sign固定一支，w距它≤a_fitN^{Oσ}。far/unused root不需编码。

## 6. 不独立的 posterior pair law与 Corollary 3.4

covered law μ_cov尚未归一化，total≥β_n。按 O=(原 pL,Q,subbox,true branch) disintegrate，取 μ_pair=∫κ_O⊗κ_O d(O_*μ_cov)。它的两 marginals严格都是 μ_cov，total仍为 μ_cov(all)；不把 original labels/time关系变成独立 law。

common O给相同 exact base和足够细的原 terminal hidden bin，故两 candidate values相差≤a'N^{Oσ}。original parent在内层 depth window，固定 scenario的 s+c有界，原 terminal精度远细于 tangent a'；v1 parent subtraction在 fixed base/chart已知。

删 entry mass<m_QN^{-dc-C''σ}的轻 (index,subbox,branch signs)；index数与 subbox数给 fixed-power总损失。每 retained entry用 (2)得到 inverse-power real base projection，在该投影 candidate−true graph≤aN^{Oσ}，再用固定-margin norm estimate扩为 comparison norm bound。

若 bad posterior pairs占非消失 relative fraction，以 Σ_Qm_Q≤1及 subbox count找到一个 group的 bad mass B≥m_QN^{-Oσ}。只有这个 contradiction group被临时归一化，原总输出不局限于该 tiny group。第 κ色令 W_κ=Σ_iN^{-dc}，概率权 π_{κ,i}=N^{-dc}/W_κ；由 (2)

\[
 d\mu_{\kappa,i}/B\le
 N^{O\sigma}\frac{m_QW_\kappa}{B}\pi_{\kappa,i}du
 \le N^{O\sigma}\pi_{\kappa,i}du.
\tag{3}
\]

W_κ≤N^{Oσ}由 greedy count。没有把 π改为条件于 basepoint或另一颜色的 law。

置 M=a、Δ=a'=aN⁻c、R=N^c、d0=(1+d)/2<1。Cor3.4给 ε_*，取 ε=ε_*/2、θ=ε_*/8，再选 σ，使所有 O(σ)/c losses<ε_*/8；β_n⁻¹的 o(1)另吸收。bad norm gap aN^{-2θc}大于 MR^{-ε}，而 value precision、norm upper、list counts及 (3)满足其余条件，归一化 mass=1。故 bad pair relative fraction→0。

## 7. Aggregate jets、representatives 与 genuine tests

在 comparison-scaled中心将固定有限阶 jets bin到 aN^{-θc}。good pair norm closeness给 bounded neighboring bins。对每 O的 actual posterior π_O，∑_bπ_O(b)π_O(N(b))为 good-neighbor pair probability；故一个 maximizing neighbor-list的 success至少此平均值。积分保 (1−o(1))覆盖质量，而非仅挑一条可能极轻的 candidate。

Q/history在原 pL已有 actual short list；short time block由 exact t确定，midpoint spatial bin的可见 ambiguity≤K_path^O(1)，true branch只有2项。因此并合这些条件得到原 pL下 c_geom=(Q,short block,spatial subbox,true sign,candidate jet-bin)的 actual short list。不能用 N^{Oσ}总 subboxes数量代替 sampled observation的实际 ambiguity。

保持 initial priority和 invariant signs，merge同 c_geom，trajectory assignment固定 throughout short block。每 bin选一个实际代表 equation及 branch；固定有限 jets控制同 bin全 comparison norm，所以所有 member whole pieces距代表 branch≤CaN^{-θc}。

若代表 |P_b,ww|≤a⁻¹N^{θc/2}，以其 branch center的 |P_b,w|归一；discriminant stability使它和整个 branch上的 derivative可比，且 reciprocal≤N^{Oσ}。member w偏离 branch引起的 derivative误差≤N^{-θc/2+Oσ}。由此输出 value≤CaN^{-θc}、实际 order-one derivative、curvature≤a⁻¹N^{θc/2+Oσ}，可在厚度 a_QN^{-2θc/3}拟合。

若 curvature更大，branch距 affine center≤aN^{-θc/2+Oσ}；用 w−center，在厚度 a_QN^{-θc/3}拟合。中心的 1/P_ww只在上述 cutoff之上取逆。选两类型之一保固定质量，输出common depth。actual a_Q/a的 tangent-subpower差及全部 N^{Oσ}由严格正幂 buffers吸收，不能保留成 original输出的 N^{Oσ} slack。

短块时间长 ρq_s，空间取 old true frame乘ρ并调整 midpoint center，其 whole-block geometry只用 actual path factors。选择 C'σ<kθc/12，depth gain≥(θc/3)ε_n，额外time cost<其 k/2。恢复旧坐标用原 2.13：v1 special quadratic形式保持，v2恢复 parent B。old candidate identity不进入输出label。

## 8. 全 original law上的 geometric map与 4.12

先在原 path law μ上定义 **完整** finite geometric label map A：旧 Q assignment、stored ordered tests/rows、whole-block predicates、priority、branch midpoint signs、subbox/merge IDs、代表 test及最终 admissibility检查。特别是，固定 whole-trajectory assignment中若当前 incidence未满足最终 derivative lower等 selected tests，也必须令 A(l,t)=failure；这不改变 trajectory assignment，failure可依 t但不含 analytic mask。failure不入 list，posterior回收才不会引入违反图表条件的 incidence。masked analytic successes均满足这些几何测试，故 A与分析标签一致；未用 analytic eligibility mask定义原 A。

μ_prep是归一化 probability，不能直接声称 μ_cov≤μ。应将 covered submeasure乘其 original prepared mass M_prep∼p_path，得到 ν≤μ、list success≥cβ_np_path。所有 parent s_A和 p_A factors已经由这一次正确回传付清。

对于任意 measurable L(O)，ν-success≥m先给 μ-success≥m。joint law λ保原 observation、path tags及 A，但 list只观察 exact base x和原 discrete o；unknown tags在 posterior maximization前求和，不交给 selector。对 flatten law Fρλ，在每 (cell,o)选最高总质量的 D_list个 **非failure** labels，得到 same-size cell-constant list。两次 TV转移给 μ-success≥m−2e。

原 hidden-bin边界无须对齐 base cells：bin当 discrete tag保留，回原 law时仍用它的实际值。该证明没有 conditional-probability reciprocal，也不要求 analytical ν或后验规则本身 tempered。

## 9. 原复杂度、实际 slack与质量预算

candidate P=Aw²+B(u)w+C(u)，|A|≤N^{s+c+Oσ}。原 threshold witness projection有 volume≥N^{-C_Sσ}，且原 w范围 W≤N0^{P0(M_path)}。在其上 derivative/value给 |B|≤N^σ+2|A|W及 |C|≤a'N^σ+|A|W²+|B|W；固定次数 Remez遂给 B,C全部 coefficients≤N0^{P_S(M_path)}。这不假设 w在 tangent units有界。代表 reciprocal仅在已给 lower cutoff处取，未存巨大 unused root。

new choices数 per old path chart为固定 tangent幂，回原 N0仍为 polynomial exponent P_S(M_path)。whole-line/block tests逐个 fixed-dimensional quantifier elimination保持 fixed degree，finite priority/merge只增加 predicate数；nonempty jet bins可 reindex为 IDs，不把 analytic jets计算写进 predicates。

4.12的 quantitative flattening在原 (x,ξ) coefficient坐标，x=(t,y(t))；Jacobian1。固定其它变量，一轴平移 h只跨过至多 Σdegrees个原 polynomial boundaries，Boolean组合不生新 boundary，joint tag向量变化总 L1亦由同 boundary数计。故 ∥τ_hf−f∥₁≤C H(TD+1)J(1+R)^q|h|；marginalization收缩 L1。取 mesh exponent D_mesh≥B_S(M_path)+2得到 e=O(N0⁻¹)，table cell/entry count的指数仍为 polynomial in M_path。输出 posterior table在这之后才建立，故无自指。

预先 guard必须是原指数形式 **M#=2^{(M_path+n)^2}**；它可对所有 M_path≥1最终吸收任意 fixed polynomial P_S。若误读为 2(M_path+n)^2则此结论不成立。scenario确定后只删有限早期 stages，不重选 N0或改 guard。actual list/slack的固定幂 r_S最终<n；N^{σ}仅用于分析并由 gain buffers消去。

aggregate posterior成功保固定 c0β_n，不选一个 tiny candidate作为最终 output。恢复 original law后

\[
 m_{out}\ge c_0\eta_0p_{path}/(JG_n)-O(N_0^{-1})
            >p_{path}/\log N_0.
\]

第一项靠 β_n log N0→∞，误差靠 N0⁻¹K_path log N0→0及 p_path≥K_path⁻¹。fixed positive tangent gain最终超过 γ_n；original depth/time/width gain和 guard全满足原 4.6，产生矛盾。

## 10. 审查边界

原 4.11 的完整 residual量词、prepared caps/原 history marginal、actual path列知识、predeclared guard及 polynomial output bounds均为实质条件。删除其中任一项的 toy可示边界，但不反驳原命题。结论不提供某 geometric branch中的候选存在，更不提供 full source bad-problem排除。

本稿未把单独 TV恢复引理或 Cor3.4重调用登记为主成果。正式 root全文独审待整合稿ready后在分配 review文件完成；本稿只编辑所分配文件，无 Git操作。
