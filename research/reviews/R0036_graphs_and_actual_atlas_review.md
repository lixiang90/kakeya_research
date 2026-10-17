# R0036：scalar projection、原 priors 与实际 atlas 全文独审

2026-10-17，审查者 `/root/lifting_obstructions`。已独立实读 root `R0036_unbounded_narrowness_full_proof.md` 全部 §§1–17、A `R0036_scalar_projection_and_nested_normalization_audit.md` 全部 §§1–10，并对照原 8.2、10.1–10.7、2.13、3.4、4.12。本人的后半主审稿不作为自己的独立认证依据。

**结论：完整 Theorem8.2 的有限实现及 Proposition10.1 的 ℓ=∞ 排除，通过本次内部逐步独审。** 具名高级输入、正有限窄度和完整源读出责任保持原范围；未经外部同行评审，不认证新颖性、无条件高维界或最终 Goal。下述 §1 明确 d≥0 的真正依据，以避免把相消的两个终端幂当证明。

## 1. 原 active law、有限平滑及 d≥0

8.2 输入是任意 probability trajectory prior ν 与 μ_act≤Kνdt，允许任意额外相关坐标。root/A 先以五个实际 scalar coefficients 分 finite tags，质量 ω_j；mark threshold针对整个 tag×σ-time-bin，不假逐原轨迹有同一 marks。未mark总费用≤1/K₁；μ_act domination给新 marked product-noise law 的 inverse-subpower质量。

五坐标 independent common-distribution jitter给 full-dimensional piecewise-constant coefficient prior，内部 tag weights不需 lower bound；额外原坐标暂不伪造成 Lebesgue density，最后按 tag原conditional prior恢复。固定(t,y)时 y-intercept noise给1/σ密度；先以原整tag×I cap bound total tag weight≤Kσcp^d，再乘，得到真正 exact-base ceiling。给定y后无需声称slope仍独立：先对intercept密度取upper，再对独立slope noise积分，正确得 min(1,ρ/σ) 因子。

terminal noisy support只在原active terminalcells的 K邻格内，因 Kσ≪a；是实际支持上界，不是由cap反推cover。相同marked law的terminal density与support夹逼给 n(s)∼ca^d，再得所有endpoint slope caps。

**d≥0须用 unit-width(p=1) cap。** x的 bounded range只占K个unit bins，故每occupied basecell的总质量≤Kσ²c；basecells数不超过 terminal triple cells数≤Kσ⁻²c⁻¹a⁻d。因此总质量≤Ka⁻d，d<0违inverse-subpower总质量。单独 terminal x_a cap乘terminal support的a幂会相消，不能证明此项。root§3 已按反馈明确该完整链及相消警示，已实读修后段落；A§1的完整证明也与此一致。

## 2. 无角输入的 crop、原 world 权重及 profile

noise使joint profile有(u−M)_+增量。固定小 ε 后最大化 (1−R)r−f(r,u)+εu，R=(1−d)/2；比较(s,0)得到 r₀接近s、u₀≤M/(1−ε)、f(r₀,u₀)≤f(s,0)+εU，U=4(M+s+1)保证u₀+r₀≤U。各坐标的最大性分别给 pure endpoint cap1−R和terminal angular ε。

按 slope/intercept widthG作whole-trajectory crop。给exact base和旧slope bin，intercept crop仅bounded choices；new within-world factor G/p_C，而真实worldweight含p_C。其抵消给 f′(r)=f(r,u₀)+u₀−α，不能以cross-world平均代替这条公式。cropped问题属C(1−R)，可调用已有scalar Cor6.9；不要求新f′(0)为零或bounded。

true packet lift回原noisy law后 mass/q≥βN^{-f(r₀,u₀)}/K≥βca^dN^{-εU}/K，p_C与G精确消去。先对每fixed tolerance取successful exact subsequence，再让ε/horizon容差慢趋0，给q≥1/K、errorKa、原mass floor qca^dβ/K。没有以单个有限样本中infimum自动attain的误用。

## 3. interval尺度、whole-time外推与共同jitter

packet position把slope限制到Kβ/q；exact-base graph只容K个x_a bins。以area Kqβ积分cap和noise factor，与**当时的true active floor**比较，得到β≥σ/K。optional angular case若β有fixed-power deficiency，选fixed正小u，增强cap与同floor矛盾，故β∼log1。

mass floor除base ceiling给normalized真实正measure set，polynomial Remez控制adapted quadratic norm。q≥1/K所以从block至unit time只费subpower；沿每条trajectory的difference确为quadratic，position difference为affine，可以分别外推。不存在fixed-power短见证的免费unit-time推广。

fix共同u**之前**，disjoint labels与floors给Σ ca^dβ≤K。先保一个block、再Fubini选同一个noise vector，不能逐label各选u。标签在固定(j,u)唯一，因此所有原tag trajectories可以同label恢复，额外坐标任意相关不影响disjointness。反向 predictor F(t,y+Δy)−Δx及center y_c−Δy正确；σ′≪σa²和β≥σ/K使unrounding误差≪a。

整marked原tag-bin可恢复其全部原active part，包括旧block边缘，因为输出已whole-unit-time fit。fixu不保原每label floor，作者已显式以先前固定Σca^dβ预算重新删light restored labels，最后才dyadic选择commonβ。这项必要收费已支付。8.2 对每substantial residual的uniform-use通过fixed-power失败model sequence反证，未假显式uniform modulus或fixed正幂输入K。

## 4. nested true priors、两时间角预算与 C 标签

实读root§§6–8和A§§6–9。初始n_i(0)∼1来自先经own-depth true normalization；随后relative profiles才成为f_i(r)→dr。native monotonicity与zero-depth cap给old base-density upper；不可直接条件于tiny A后重用。

ℓ=∞是对所有maximizing sequences的global-inf意义，CRP第四项可对新segment maximizing问题取large narrowness；乘fixed正深度差保持发散，得到α₂−α₁→∞。原ν(Q_j)来自full-layer saturation，不受后path incidence restriction追改。

在原world/trajectory prior上独立抽两times，仅要求两处path event，Jensen保p_path²。异常 entries先删后数first labels，故不乘其巨大数量。固定first Q₂的whole-unit extrapolated strip面积K₀g₂，hidden求和仅在good p₀ ancestors内；与firstlabel数相乘后g₂取消，失败mass为N₀^{-Su/2+(d+2k)s₂+o(1)}，在固定参数选择下power-small。

C标签同时记录normal、center normal-intercept、center normal-velocity，不记录early Q₂身份。later label和early label贴同一bounded affine trajectory，normal近parallel给这两个center coefficients同样近；故later actual Q₂-list恢复C的bounded neighboring bins。这一点排除了只恢复normal却遗漏center motion的假known atlas。whole assignments与fixedt₀切片均tempered。

## 5. C→A的绝对 shift、实际 knowledge与两极限

C空间normalization的world weight为ων(C)/W，raw prior只整体除W。terminal equality为 n′(1)∼n(1)g_C/ν_C；earlier只有upper，已足够保持endpointcap与angularclass。任意absolute shift在density差中取消。terminal true systems lift保证H(E_i)≤H(E′_i)≤k(d_i)，所以新问题仍maximizing，才可用其relative profile。

b_i→0的coarsening只需universal H≤L，不要求coarsened问题仍C(d_i)。饱和A′后

    ν(A)/J_A ∼ n_i(1) n′_i(b_i)/n′_i(1)=N₀^{-db_i+o_i(1)+o_N(1)}.

因此该比值只在two-limit diagonal为subpower，fixed i不冒actual K₀。原p₁先列C、恢复primed exactbase与coarser hiddenbin，再复合A′ own-depth list；无absolute-shift费用。largest tangent width lower由old terminal angularcap和actual A-list另证，没有凭det上界推出。global预算Σωq_Aν_A≤1保持至所有后续restrictions。

## 6. root全稿后半的独立核验

已逐式对照root§§9–13，而非只引用本人主稿。graph前第一次 light label floor给Q₁ whole-domain old witnesses，第二次core-entry floor给norm数据；两个用途分开，后删不追认新conditional floor。D=P_z²−2P_zzP independentz，positive projection在curvature split之前得到，故Remez/complex core radius有依据。signed largecurvature用affine center；small/tiny curvature只追used simple branch，unused escaping root不入output。

固定λ_A分母q_Aν_A，ΣR_A≤1与∥μ_prep∥=ΣR_A∥λ_A∥支付dense A选择。projected cap的J_A/ν_A仅在diagonal用；support则独立以compatible旧Q₁的whole witnesses收费。其normal center速度误差O(g₁)使 Δy−y₁′Δt 的normal分量为O(g₁q_Aσ+g_C)，除q₁g₁前time项先抵消g₁；不需绝对g₁ lower。Δ_i→∞与fixedM使native coords变化≪a，graph derivative upper确给Ka⁻d支持数。

每residual使用fixed prior ν(.|A)而非current success renormalization，8.2输出只作候选。greedy每次移除prior≥ν_Aa^dN⁻δ，所以finite；every-residual量词反终止才给fixed fractionκ₀p_path覆盖，不能把一次subpower floor当constantcoverage。

Π=∫π_o⊗π_o dm_c(o)保原raw质量和两marginals μ_c。badpairs若占固定比例，先global预算找b_A≥q_Aν_A/K，再normalize；两色marginals的q_Aν_A/b_A已付。每index的X_a-bin cap配finite list数给uniform reference weights，未假posterior最小原子。Cor3.4 用R=a⁻¹、M_norm=1、quadraticdegree及fixedmargin；δ先小、K后diagonal，list/value/density/norm的全部loss均进入ε，normgap a^{2θ}/K>R⁻ε。pair colors可任意相关。

## 7. actual map、原law恢复与最后2.13出口

root§§14–16已显式保持wholeblock assignment；final incidence只有所选真实tests、尤其derivative lower也成立才报label，否则non-listable failure。P_new=P_*−F̃不改w-derivatives，positive depth buffer吸收analysisK/N^δ，frame/time原A不变，故finalslacks与lists是actual path幂。

原law恢复只flatten μ_ref的finite geometric joint law，不flatten analytical μ_c/masks。未知A经actual p₁-list并入，不直接给selector；hidden/path tags仅joint保留。4.12 用 μ_c≤μ_ref 的raw success，经Jacobian1及finite sign-boundary TV得到原cell table，误差O(N₀⁻¹)。每测试fixed-format time quantifier单独消去，priority/merge不引入无界degree；预先 C_i罩住输出数量/坐标与逆长度，样本不事后改guard。

最终newparent c=(A,b)的fullpriorν_c通常小于ν_A，作者已明确两者不同。normalization的terminal equality n′(1−c′)∼n(1)J_A/ν_c及earlier upper给C(d_i)，即使absolute J_A/ν_c exponent很大也在差中抵消。remaining terminalchild lift时 ν_c n′(1−c′)J_child=n(1)J_AJ_child，故old truefloor恢复，**不需newparenttruefloor**。因此H(E_i)≤h_A,i+k(d_i)(1−c′)严格违maximizinglimit；没有免费n′(0)界或intermediate equality。

fixed i先定 finite complexity/actualslack bounds、再选late excluded N₀、最后outer diagonal的顺序合法。raw coverage cκ₀p_path−O(N₀⁻¹)>p_path/logN₀使用actual p_path≥K_path⁻¹，不仅是笼统N^{o(1)}。这完成actual atlas矛盾，而非只完成一个candidate。

## 8. 认证边界与阶段退出

本次全文核验覆盖共享8.2及完整∞分支；未把它登记为新的scalarization方向。没有保全部原假设的counter，也没有需要缩小原命题才能通过的缺口。d≥0依据的root最新修复以及 common-jitter预算、failure与ν_c修复均已实读通过。无pending数学修正。

保留原高级输入与正有限ℓ/§7–9、2.17/finite-Hausdorff读出、KT等未付责任；不因UNB通过清空SRC/DIR/FSD/DIM条件。后续须按阶段退出重新选择完整责任，不能以继续拆小lemma替代目标推进。Goal仍active，本轮不构成最终或重大新结果。
