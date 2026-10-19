# R0107：全横条能量、原访问与条件分支独立审查

2026-10-19，A。正式独立审查只编辑本文件，六个编号节。下列“通过”限于明列条件的有限估计、实际原分母比较及未完成范围；未经外部同行评审。

## 1. 实际全文读域与审查对象

实际全文读取root《R0107_all_strip_collision_and_original_visit_bound》十节、B《R0107_bulk_source_mass_and_general_goal_counteraudit》最终十节、本人的《R0107_complete_goal_and_seed_strength_reselection》十节，以及reselection、working各五节。终macro、《next_complete_goal_reset》、source scope和round各六节亦已实际全文读取。root最终§8的canonical point/Φ witness图、原平均I、同一h0-window标签、上邻空间coherence及shell/floor修订均已读回；B§6–7从先逐管heavy改为同一usedgraph平均CS的终版亦已再次全文读取。

本审查逐步独核root和B的有限证明，不把本人资格稿作为自己的独立审查。源方面，本轮实际回读WZ Def3.1–3.6及Def17.1–17.4的计数、native AD与coherence输入；既有R77等高级准备的wholeproof仍为具名输入，本轮没有新认证其全部证明。没有把root的恢复、Git、未来状态或同步记为本人验证；source note所报文献总量也不是本人本轮重新执行的字节审计。

## 2. 固定全图的同条能量

root§2–3及B§3–4的量词正确：图g在clock前固定，Q是同一坐标h格的任意子集，实际Q_v可以依v恶意变化；只要求0<τ<1及横向k1的全部区间概率upper。对同一b的两个点，k2b精确抵消。距离d=jh的碰撞将k1限制在半径C0Bh/d的区间，C0足大使该半径至少h；半径超过1时用总质量≤1，其余用所给law。得到概率upper Cτ A B^τ j^-τ，没有将k1与k2或Q_v独立化。

每a在距离jh至多两个a′，每条及条数均O(h^-1)，因此

    ∫E_v dσ ≤ Cτ A B^τ h^(τ−3).

对角O(h^-2)在τ<1时可吸收；τ=1的log未被抹去，也没有被纳入锁题。该全图energy同时支配所有Q_v及其更小删选，不需要对clock依赖的子集额外union bound。它也适用于总质量≤1的clock subprobability，因证明只用其总质量upper。

## 3. 全部条的共享容量与原标签

对每个已访问q只挑一个实际输出用于占格CS，不丢其他原访问；同一b内有n_b²≤m_b E_(v,b)。第二输出中心的相邻间距至少2h²，而误差至多Bh²，故任一终端h²格只与O(B)个b相容。由所用CB²h球内的native cover得Σ_b m_b≤K B^C h^-1，再对全部b一次CS，确有

    n_v² ≤ K B^C h^-1 E_v,
    ∫J_v dσ ≤ Cτ D(AK)^1/2 B^C h^(-2+τ/2).

此处跨b只使用第二坐标的有限重叠，未对可能被k2抵消的跨条碰撞强套横向law。终端容量只用一次，没有先选单strip损h，也未赠每strip、每root或每cell的density lower。乘D是原(v,q,T)重数的必要费用，不能以occupied cells替代原访问。

沿用同一g、D及未归一σ时，whole-T或marks删选保该绝对upper；删后point Φ、filled X和逐管duration的lower不自动保留。clock限制质量p后如归一为概率，law常数须付A/p，左侧亦除p。平均upper不能逐管读出。以上闭包与root§5、B§9一致。

## 4. 原same-T公式、canonical图与空间精度

独算root§6及B§2的两行native公式正确，包括第一行−H²(k1φ1+k2φ2)、第二行H(2x2−c)+H²φ2。其前提同时包括精确第二row及原T的code关系U2−V2=c；nᵀG_u小或零本身不提供这些条件。一般code slab、moving normal或误差归约没有被本轮支付。

root最终§8的degree上界明确只用于预先固定的canonical point/Φ witness图。每fine p、每原Φ_p δ方向bin选一根实际相容原T，合并重复(p,T)，每(T,u)留一个访问；实际物理碰撞及截面packing仅损固定K幂。于是所用point degree≤K^Cδ^-1，原E/Φ下界给I≥K^-Cδ^-5≥K^-C Nm。这不是对全部过p管族赠degree upper，也不是把自由角bins视作原管。

固定root(u,y)，水平H-cell有O((H/δ)²)个fine points，故每(v,cell)原重数D≤K^C H²δ^-3；roots总数≤K^Cδ^-2。native AD1的上下界在δ≤H²时给所需局部H²-cover≤K^C B^C H^-1。对非allowed H，使用上邻ρ∈[H,K^C H]，将physical affine grain片按有限个相交ρ-point cube标签拆图；每图的ξ代表在v前固定，振荡K^C H转为输出误差K^C H²。不能跨coherence边界免费用一个代表。

这些source计数在同一原N/I上成立。条件分支还须要求这一个保所述I的usedgraph确满足精确row/code前提；任意截取code slice不自动继承该原lower。root§6、§8末已把此项与一般归约缺口分开，没有将它当已提取成功的完整source分支。

## 5. 原shell lower、counting law与幂预算

root最终§8与B终§6采用平均I而非赠逐管heavy。取δ^(1/8)的上邻allowed h0，将各原S_T分到O(h0^-1)窗，先按窗再按T的CS给

    Σ_(T,J) n_TJ² ≥ c h0 I²/N ≥ K^-C N h0 m².

对角≤Nm；每u的q h0近终时数≤C(qh0/δ+1)。利用n_T≤m及m≈K^±Cδ^-1，选q=K^-C足小后可删近对角并保正比例。正向pairs再分O(1+logK)个gap壳，某H∈[q h0/2,2h0]有

    #Pairs_H ≥ K^-C N Hm² ≥ K^-C δ^-6 H.

始终保同一h0-window标签，才有原dyadicLip的|ΔF|≤K^C h0及|k_i|≤K^C；H的上邻allowed尺度只用于空间coherence，不能替代该时间责任。η最后小使H≥δ^(1/4)、H≤K^Cδ^(1/8)，故δ≤H²及rounding均可支付。

原clock counting cap(8)仍是额外输入，要求对可能选中的所有所用壳统一成立。取σ=δ/(CH)乘原shell counting为subprobability，而非tube偏置的clock law；再限制到原h0窗只减其质量。将有限lemma乘CH/δ、D及root数，确得

    #Pairs_H ≤ K^C sqrt(A) B^C δ^-6 H^(1+τ/2).

若A,B≤K^C，与lower相比为1≤K^C H^(τ/2)≤K^Cδ^(τ/16)，固定τ后让源η足小即矛盾。原N、m、D及H/δ均在同一计数单位；无density-flat公设、无每strip共同时间或每管same-shell lower。反之，A若带未吸收的尺度负幂，该矛盾不能照搬。

## 6. 限定结论、残余与停止

**全文通过，限于上述有限lemma及明列条件分支；无未解决强制项。** root与B已把usedgraph而非allT_p、平均I而非逐管duration、时间h0窗而非仅H上邻、subprobability及原counting law各项实际收紧。我的独立复核认可这些修订后的证明，不把本人资格稿算作自己的独审。

额外(8)没有从原定义或whole-matrix nonfit推出。所检bulk窗上f1常量而f2粗糙时，wholeF非拟合仍不提供k1非集中；窗外另接anchors，不把f1说成在F0=I、F1=0的全部Z上恒定。root§7对此的最终收紧和§1对“后续单片设想”的历史措辞已实际读回。精确对角分支借R77的尝试也尚未付全部原pair质量、root条件、全尺度和floor。一般code/row归约仍缺。因此不认证fullsource moving-row cap、fullrough、ordinary增益或新维数下界。

去掉横向law的全格线性图、随v变化的图及原标签复制分别检验law、固定图及D的必要性；前一例的直线native Y不满足原tubeKT，不能当完整source反例。全条求和是标准能量/CS的明确用途，不登记新ID、新颖理论或major；旧CP/PM全称gain不因这项条件应用被重新命名。终macro/next/source/round一致保留四完整出口、已付DIM链及原未付责任，没有将有限lemma当成无附加source输入。保守actual no-information2、legacy30及下一先完整重置的范围通过，不以自选条件估计重置主目标停滞。

完整Goal仍active。审查未经外部同行评审，具名高级wholeproof层级不变；未预认证未来metadata、Git或同步。
