# R0074：原标签质量、完整源提取与 CW 出口正式复核

2026-10-18，A。只编辑本授权 review；不操作 Git、元数据或新代理。本次为内部逐步复核，未经外部同行评审。

## 1. 实际全文对象、独立性和待审量词

本次 fresh 实际全文读 root `notes/40_multiscale/sticky_mixed/R0074_AD0_native_labels_to_CW_exclusion.md`12节（含第6节新增 IKQS经典比对）、A `R0074_AD0_label_source_and_mass_audit.md`13节、B `R0074_singular_pencil_CW_counteraudit.md`10节、working_spec5、macro6及next6 `notes/00_map/R0074_next_full_goal_and_critical_source_gate.md`。另全文读 `literature/notes/coste_2002_semialgebraic_power_scope.md`和 `tmp/R0074_new_sources.json`；独立读取本地 IKQS提取文本§6.2具体statement，并只读计算其PDF及Coste范围笔记的bytes／SHA256／Git-blob哈希，不执行Git。

我参与的是 A 的 common-right tube-anchor 独立提取，故不把它当自己的独审。本 review 的独立数学对象是 root 的不同 row-greedy 提取和 B 的 Schur／定量稳定／CW 出口；A13由 B 已实际全文逐式互审，不能以双方类似公式代独立检查。root12与B10在此重新逐式复核。

通过命题的完整量词为：固定原γ>0、κ=1，沿 R43及本轮spec的**全部原T bounded joint-parameter chart**规范，η最后足小、δ最后足小，不存在所列 WZ2609.22035v1 Def17.2–17.4 的 d5/k4/ell2完整配置且原 CW≤δ^-η。本次不把该规范改成仅used T bounded，也不宣无界unused-padding泛命题已证。

## 2. 原质量、同 label 关联及 row-greedy 提取独核

native三水平 filled 与AD0标签给每time约_K δ^-3点，原scalar Φ的AD1给每点约_Kδ^-1不同管供应。一个固定原管／time的点和fine角cell碰撞只有固定倍，故canonical实际visit图满足 |G|≥K^-C N m、每管time度≤m。这里 N是**原全T**，N≈_Kδ^-4由bounded原chart与joint4-AD给出；不能从bounded used T数直接推出此原分母。root§1/2已保该范围。

先tube-heavy使每条H0管有至少K^-Cm个**原全部**visits，原质量≥K^-C。以后仅选whole tube labels，故每个Hj仍逐管保此访问下界，不能在此误把平均density无证升逐管。若 outside-row times承载至少半当前原visits，对原time平均后取一个实际time，再按至多K个**该time原label**取同label，确保真实Hj+1占Hj的K固定次幂比例；此前anchor约束同时保留。若不然，W对原Uniform(Z)质量≥K^-C，而非对重新归一的邻接time免费称满。

j个rows逐次离旧span>τ，其Gram体积≥τ^j、其余singular values固定upper，故原参数距同一affine S_j≤Cδτ^-j。reference可由实际管投影取bounded点。第5个独立row会使足原概率H5落在3plane的w=Cδτ^-5邻域；bounded cover为O(w^-3)个joint balls，原4-AD upper给 μ(H5)≤CKw，与K^-C冲突。先固定a<1/20、τ=δ^a，再η足小可付。于是 j≤4停止，确返回真实原H、p≥K^-C、dimS≥4、ε_par≤Cδτ^-4及足原time W；不是只得到一组好anchors。

finite witness不被称新完整Def17配置：没有把条件化 pointΦ授新ADlower，没有把跨anchor删选当whole-time restriction，也没有新增allowed-grid闭包。若原shading逐管有下界，whole-label留存保原shading；若再取共同访问则需重计。本证明最终用whole参数及CW，完全没有要求该共同访问继承旧逐管密度。

## 3. 全 minors、精确 compression 和统一幂稳定独核

对S的原正交joint基Q=[A;B]，W上 V_t距rowspan≤τ给 ||n_t(A+tB)||≤τ、||n_t||≥1，故全部4×4 minors≤Cτ。minor的次数≤4；原ν interval upper及ν(W)≥K^-C允许选5个两两gap≥K^-C的实际times，δ≪gap由η后小保证。Lagrange分母的四个gap使全部系数 D≤K^Cτ。未假tildef smooth／rational，也没有从一个坏det点推出全pencil亏秩。

B的精确分类经完整复核：取达到maxrank r≤3的evaluation，Schur恒等给G=0及FC^jD=0；Cayley–Hamilton使U=span C^j imD为C-invariant且FU=0。K0=U×R^(m-r)、E0=U×0给compression，再取dimK=m-3+e、dimE=e。所有m≥4及多right／left／regular退化已计，r=0亦平凡。GL仅用于存在证明，随后用原Euclidean orthogonal projectors，因此没有未付canonical-basis条件数。

Grassmann最小泄漏Ψ在固定bounded矩阵域连续且半代数，D=0⇒Ψ=0。H(s)=max_{D≤s}Ψ²的compactness只给趋零；root/B另用固定QE令graph落有限polynomial零集，除公共s因子后，以P(0,y)最低非零y次和 |P(s,y)-P(0,y)|≤Cs 实付H(s)≤Cs^c。该步骤完整保固定正指数，不能用pointwise compactness替代。基础QE为具名标准输入，不声新独证全部QE或将格式随δ增长的域纳入。

## 4. Whole-tube box、参数顺序及固定维推广

近compression选原orthogonal K/E后，h≥C(δ+ε_par+D^c)包住全部泄漏。补参数维数恰3-e，故一个h格原概率≥cp h^(3-e)；其**whole original tubes**包含于体积≤Ch^(4-e)的真实R5凸box。reference-axis剪切bounded且Jacobian1，原δ半径和roundcaps由h付，因此原CW≥cp/h。没有给H新ADlower，没有将CW分母改成H，也没有把短clock片段延长成新管。

先固定维数、QE指数与a，再固定s<min{1-4a,ac}/2，取h=δ^s；所有有限K幂在η最后小后均比这一固定saving弱，δ最后吸常数。第5row排除及最终p/h>δ^-η可同步满足，无参数循环。A common-right版不同的ε_par=θ、D≤K^Cδθ^-8也在其明确参数顺序下通过；它不是root proof中的免费替代步骤。

root§10的固定n=d-1读出范围成立：n+1独立rows把原n-AD law困于(n-1)plane；停止S维≥n，n-minors次数≤n，用n+1真实times插值；compression补维n-1-e、物理短轴n-e仍差一幂。用于k=d-1、κ1的native AD0时，filled n-1水平与原Φ AD1确给每time δ^-n管供应。每个n固定后选择常数；不声dimension-uniform、正维label或κ<1、普通方向初始化已付。

## 5. 一手范围、具名依赖和 κ1 表边界

本次直接使用的是原Def3／17输入、其已明示bounded规范、有限CS／插值／Schur／Cayley–Hamilton及标准real QE；没有为本源应用另调GWZ或OAI3 wholeproof。macro的κ1 case表中(2,2)/(4,4)仍依原**Propositions17.4／17.3**具名声明，非本次重新独证它们全部proof；mixed32／mixed43分别沿R73／R70已审参数范围。这些命名依赖在表中保留，matrix33等未付责任没有被删掉。

IKQS1307.6429v2本地§6.2明确允许rectangular矩阵，并说two-dimensional matrix spaces over sufficiently large fields为compression spaces，追溯Atkinson–Stephens。R域适用；故本轮精确pencil结构确属经典重证。该来源JSON记录root实际text读PDF1/3–5/20、视核1/20；我本次只独立读本地§6.2文字，未冒称自己新视觉核25页或全算法。只读哈希复算给PDF314137bytes、SHA256 `dd8a396b1f38552c8da205dc3e141ccc778f3647bba92829afbaf4f30f2db7ea`，与snapshot一致；不能由此认证其wholeproof。

Coste范围笔记与snapshot一致：作者2002讲义Theorem2.12及proof仅网页索引／缓存读域，作者直连403、镜像404，无local PDF和视觉页31；笔记900bytes及哈希吻合。未把该记录当讲义全文已读或联网重试的新事实。当前特殊power步骤已另从具名QE实证，Coste仅作经典范围比对。last actual官方三核心bytes核仍R72，本次没有新的官方版本检查。上述只读snapshot核不预认证未来catalog、metadata或Git结果。

## 6. 必修结论、停止线与最终通过范围

**没有未解决的强制数学修订项。** root12的原row-greedy、B10的全维精确／定量compression和保原CW出口，在明确bounded原全T规范下通过本次独立逐步复核；A13自己的上游链不计自审，已由B独立全文核。通过的是完整mixed42 κ1的限定源应用及固定维同型有限关联读出，不只是一个孤立finite rank lemma，亦不把经典工具应用包装新rank theorem／重大结果。

macro6／next6正确保持：不由κ1 case表推出Kd17.1极值κ≤1，不由ordinary4D下界授任意joint4AD／CW输入，不证明κ<1或uniform邻域，不推出ordinary n5严格超过4／n6界。长期Goal active，所有旧packet／basicness／BSG等冻结继续；下一轮先全目标比较并同轮锁真正不同的数学，不能续AD0 anchors、阈值或proper类换名。

本review仅完成内部审查，**未经外部同行评审**；原文及外部高级wholeproof未被本次一并独证，无新数学ID／major／优先权声明。不预认证随后归档、元数据、验证或Git同步。已完成授权六节后停止编辑和检索。
