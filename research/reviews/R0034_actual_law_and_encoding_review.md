# R0034：完整 actual-improvement 转换的原 law 与编码独立审查

2026-10-17，B。已实际通读 root `notes/10_source_audit/actual_improvements/R0034_actual_improvement_full_proof.md` §§1–12及 A `R0034_guarded_diagonal_and_preparation_audit.md` §§1–12，对照 OAI4 原 4.4–4.12（PDF50–70）。B 自己的 candidate audit不是本次独审对象，不能以自审代替读 root全文。

**结论：修后 root 全稿及 A 的 guard/preparation 部分通过本次逐步独审。** 通过范围包括原 4.11完整 residual-to-actual-output 转换及其实际 4.4–4.10/4.12依赖，原模型和全部输入保留。下述 failure-map实现修正已核，不留 pending修复。不认证后续候选存在、源整篇、无条件六维17/4或高维 Kakeya；未经外部同行评审。

## 1. Closure、量词和 guard

旧统一工具在合法 restriction上可复用，但没有独自支付 fixed scenario coverage、实际 original slack和后验 geometric labels的有限编码。root明确 4.12的 flatten部分是原2.4定量复用，不将它单独当作本轮主成果。

root §2/A §§1–5 保 fixed stage→outer exact problem/path→M_path/M#→late N0顺序。4.4 的 depth-zero normalization用实际 terminal lift；vanishing nodes先 fixed positive depth、再 outer convergence、最后慢减 depth。4.5 thickness gain用 H composition给正间隙，width gain用同 depth/time的真正 known atlas、后续 maximizing和 base terminal窄度上界，未索取不存在的新 true floor。

4.6反证假设 infinitely late outputs在一个固定 original complexity exponent内：它们可成为 actual exact subsequence，success/list/slack均为原 N0-subpower，homogenize后严格 gain不消失，因此得到 fixed-M# cutoff。没有对所有 M# 同时的 cutoff。

预声明指数 guard **2^{(M_path+n)^2}** 可对每 fixed scenario吸收任意 fixed polynomial P_S(M_path)，uniform于 M_path≥1。root保留此正确上标；不是二次多项式 2(M_path+n)^2。scenario只在后面 fixed，最后丢有限早期 stages，不改 guard、不重抽原样本。K=N^{o(1)}与 actual (K_path log N0)^{r_S}始终区分。

## 2. 所有 potential parents与同一 probability

root §3/A §§6–8 的 density factor为 J_A/ν_old(A)，配 saturation和 relative profile给 Kp^d；不混 world weights，不按 current success重置 trajectory prior。原 angular numerator先删异常/小 denominator；positive ℓ时 parent minor velocity的原尺度固定幂窄度，确实小于 ε_nU_n范围内所有 tested precisions，才可降至 scalar major v。ℓ=0不作这一降维。

actual major-row fullness由累计 child fullness和 parent minor固定幂缺口推出；row orthogonalization给 transverse width/time∼J_s/q_s²和 actual row bounds，不是从原chart的 operator upper自动推出。

entropy窗口使用同一 surviving μ_prep和记录 whole histories的 nested labels，chain rule使各 window conditional information和≤H(V*)。给 A后 requested v-bin从 V*只有 K choices，故其 mutual information差≤log K。选 window后 p_A、λ_A^0、π_A冻结；后续 analytic/likelihood/sparse masks只减 numerator。小 s_A parents按原 qν预算删除，不要求逐 parent同等成功。

新 native X有 bounded motion，但 w值/速度可在 tangent units很大。root/A stable-graph和 fixed-time推导都未虚增 w motion bound。

## 3. Current budget、stable graphs和条件化

root §3/A §8 本轮完整支付原2.11的 finite peeling：threshold固定，删任一不足 current floor的整 entry后重查各层，每 entry永久 empty最多收费一次，Σlayer charges≤Σε_i。finite entries保证终止；若原输入 analytic只作为 analytic预算，不冒称由此自动 tempered。未追认为 R32/33已支付。

root §4 的 true Q-entry projection由实际 current mass floor和 same-law base cap建立；D=P_w²−2P_wwP独立 w，固定次数 Remez控制 complex derivatives。high-curvature center/low-curvature stable branch的截断与 margin均有余量。先证明每 deep history仅 K个 (t,y,X) point states，再把这个数量送入4.8；没有以 palette floor循环证明 ambiguity。

full-layer witness经过原 pure cap masks，丢失半质量的 labels由 saturation qν预算收费；所保 floor属于该 witness，不属于最后 path。固定 graph bounds形成后可供日后 restriction使用，不需要每次重建旧 witness质量。

root §5/A §§9–10 的 log-ratio负部期望≤1/e，故 mixture MI=o(log N)足以截取 joint cap；small loss只全 mixture，未声称每 parent小损。append-entry floor用 preomit marginal，coarsen C前先求 good numerator之和；进一步 sparse conditional cap必须再付 current denominator pruning。没有多时刻独立性结论。

4.9 先保 integrated duration≥|I|/K2的 line–interval pairs，再利用 C_t⇒C_τ^+积分，得到原 active-prior upper；这不是无费用的 pointwise time slicing。controlled (t,y,X)/affine quantities给 implication，原 ν不重新归一化，亦不要求 w regularity。

## 4. Fixed scenario 与 counted coverage

root §6的 coverage先取整个 assigned pieces上的 path incidences。每 scenario独立 maximal greedy，assignment是纯 whole-block几何测试加 finite priority；residual只用于 eligibility证明。full ν_Q budgets给 per-Q finite tests数，raw prior与 λ_A^0只差 fixed s_A，成本在预留 σ内。

若每 fixed finite menu覆盖趋0，slow J_n删除其所有 whole pieces上的 incidence后仍 substantial；原全 residual/subsequence假设给 further-subsequence候选。gain与 slack同时匹配 value/curvature和 N^{-dc} floor，得到一个最终在 menu内的 fixed scenario，其 witness仍 free，反 maximality。这不是 countably infinite pigeonhole。node选择只再损 G_n。

先固定 scenario，再删 affine P_w的小 derivative时段；λ_A^0≤Kν_A dt及 disjointness给 fixed-power损失 o(β_n)。root未在 fixed scenario之前对所有 σ统一收费。β_n^{-1}=N^{o(1)}仅用于 analytic comparison；β_n log N0→∞另用于 final success，两者都已支付。

## 5. Strip 是真实空间 gain

root §7使用 original predeletion history marginal配 palette joint cap收费；misaligned rows将 v限于 N^{-c/3} interval，row count和 S>0使损失 fixed-power。raw huge rows亦由同 cap与 eligibility floor排除，故 priority predicates中原 rows有 fixed-power coefficient bound。

τ使用 **actual J_s/q_s²**乘 N^{-c/4}。deep row给 binned row在原 pL下的 actual list，midpoint transverse-position bin由 exact base恢复。whole assignments合并后空间 columns q_s(1,R_1^b)、q_s(0,τ)的 determinant正是 J_sN^{-c/4}，旧 depth/time/test保持。这是可提升的 moving spatial chart，未把 velocity graph当已完成的空间输出。

## 6. Time matching 的真实 margins与概率分母

root §8的逐 index cap m_QN^{-dc+Cσ}du配最初 threshold witness，给 inverse-power base projection；m_Q=p_Aq_sν_Q在相除时消去。原 witness先于 whole-assignment enlargement，不是每 later subbox的免费新 floor。discriminant upper/derivatives据此建立，tiny/unused far roots不存入 label。

root §9按 covered law condition O后才采两 posterior；pair两 marginals仍是 μ_cov，unnormalized mass保留。light-entry费用由 list/subbox counts和 Σm_Q≤1控制。若 bad pairs非消失，找到 B≥m_QN^{-Cσ}的 group，然后两色 marginal都明确除 B，并用 raw weight和 W_color归一。该 m_QW_color/B成本没有遗漏，π_i未改成 conditional-on-base权重。

Cor3.4 的 R=N^c、M=a、Δ=a'、d0=(1+d)/2，ε=ε*/2、θ=ε*/8，σ在全部固定常数后选择。bad norm gap MR^{-ε*/4}>MR^{-ε}；list/norm/value/base-rescaling/β_n^{-1} losses均在容许 ε内。group仅用于反证 bad fraction，最终输出仍保 aggregate coverage，不被锁到 tiny group。

## 7. Representatives、actual slacks与 whole pieces

root §10 的 posterior neighbor-list success至少 pair-neighbor average，故积分保覆盖质量。给原 observation的 Q/history/subbox/true sign只有 actual path ambiguity；没有把所有 N^{Oσ} subboxes当 actual list成本。finite jet norm rule在共同 fixed-margin比较域控制同 bin全 piece，representative由 geometric label固定；original candidate identity不进入最终 label。

low-curvature代表先按 stable branch derivative归一，得到 actual order-one derivative；member偏离分支的误差有严格正幂 saving。thickness a_QN^{-2θc/3}足够容 value与 curvature两向约束。high-curvature代表改 affine center、thickness a_QN^{-θc/3}；只在 cutoff以上求逆，不存 huge unused root。两类型选一保固定质量，给 common output depth。

short-block geometry用 actual D_sρ与 midpoint position bin，actual slacks只为 path幂。N^{Oσ} fitting losses靠 depth buffers消去；C'σ<kθc/12支付 extra time，未遗留成原尺度 N^{σ} slack。parent lift保持原 v1/v2模型及 derivative单位。

## 8. 原 map的 failure修复已核

root §11最新版本明确：A(l,t)只有在已固定 whole trajectory assignment、whole-block upper/value几何测试，以及当前 incidence的 **最终 derivative lower等 selected tests**均成立时才取 geometric label，否则赋 failure。trajectory assignment仍 block-invariant；failure依 t只反映最终实际 selected tests，不含 analytic mask。failure从 maximizing list中排除。

这项修复必要：若无效 incidence仍报一个普通 label，原 posterior最大列表可能偏选它，事后再删无效 incidence会破坏 claimed success。root附有限例子正确；它只反错误实现，不反原4.12。B自己的 audit已同步相同明确条件。

## 9. 全原 law、复杂度与质量兑现

μ_prep为概率，不能直接视作原 μ的 submeasure。root已明确 p_prep=(1−o(1))p_path及 ν=p_prep T≤μ；raw/conditional parent factors在此正确乘回。original-law recovery只 flatten μ的原 geometric joint law，不 flatten analytic masks。

list rule只观察 original x,o；unknown history/path/output tags仅 joint保留后求和，不给 selector。flatten后按 (cell,o)取最高质量的非failure labels，两次 TV给 m−2e。原 hidden bins当 discrete tags，无须对齐 base mesh；最后用原 bin值评价。

candidate coefficients以原 w范围 W≤N0^{P0(M_path)}及 threshold witness上的 derivative/value控制 B,C，再 fixed-degree Remez；未将 SCL警示的原 N0^M幅度冒充 uniform tangent N^C。whole-block测试逐个 fixed-format QE，finite priority/merge只增计数，nonempty jets重编号，不编码 analytic search或 far roots。

原 joint law改到 (t,y(t),rest coefficients)为 Jacobian1；一轴平移只跨原 finite polynomial sign boundaries，joint tag-vector L1变化同被其数量控制。marginalization收缩 L1，故 flatten depth及表计数的 exponent仍为 fixed polynomial P_S(M_path)。maximal posterior表在此之后才建立，无复杂度循环。

最后 m_out≥c0η0p_path/(JG_n)−O(N0⁻¹)>p_path/log N0使用 G_n/log N0→0与 N0⁻¹K_path log N0→0两项原预算。fixed r_S和 P_S最终进入原预声明 guard，不重抽样。positive tangent gain超过 γ_n后符合4.6，time或strip各自 actual改善完成，得4.11矛盾。

## 10. 终稿范围

没有 pending数学修正。正式通过以 root修后全稿为准，包括 incidence-dependent failure、prepared probability原质量回传、指数 guard和本轮2.11有限预算证明。A preparation稿与其独立分析的责任范围一致。

未支付的仍包括后续几何分支对每 substantial residual的真实候选存在、完整源 bad-problem排除、完整 finite readout及其外部高级 inputs/KT。不得把本次 actual conversion通过改写成完整 OAI4正确或六维无条件新界；下一门槛须按阶段退出重新选择，Goal active。
