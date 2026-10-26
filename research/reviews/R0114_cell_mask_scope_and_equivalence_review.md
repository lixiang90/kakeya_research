# R0114：整格mask、原质量与条件carrier强度的独立逐步审查

2026-10-26，new_projection_gate。实际全文读root主稿 `notes/40_multiscale/R0114_whole_cell_discrepancy_and_original_carrier_gate.md` 八节、working `research/rounds/R0114_cell_selection_working_spec.md` 及macro spec。另定向读R101主证明§1–11和R10随机标签证明§1–5/其独审，用于排重。未参与root的此随机机制；本人rough-source grain稿不计独审。不修改被审主稿，不核Git。

**结论：按主稿当前固定格式、任意原平均Lebesgue shading的量词，证明及§7条件规则审查通过，未发现必修数学缺口。** 其结论是合法整格删选后的carrier压力及条件命题强度，未证明ordinary新下界、完整source gain、开放smallfootprint域的反例或major。未经外部同行评审。

## 1. 格式计数包含等号，且与系数大小无关

固定ambient n、s、D。一个degree≤D多项式的b=binom(n+D,n)个系数构成参数R^b；在任意K个输入点上的取值为系数的K个线性函数。包括退化和零号在内，hyperplane arrangement的全部faces数≤Σ_(j≤b)2^j binom(K,j)，因加一个hyperplane最多新增两倍其上restricted arrangement的faces。重合或低秩不会增加计数；可降到实际span。

故一个多项式在该点云上的三值sign patterns≤C_b(2K)^b，s个至多其s次幂。任意Boolean组合只多一个固定因子≤2^(3^s)，得到|P|≤C_s(2K)^(sb)。零多项式、实系数任意大、等号和事后选H均在此计数内。H=R^n也包含，后续总量控制确能使用。

对每个membership pattern，Z=Σ(ξ_j−p)w_j1_A(j)独立、零均值，单项区间长度w_j，故Hoeffding moment≤exp[t²Σw_j²/8]。对±Z及所有有限patterns取log-sum-exp并优化t，得到主稿(2)。没有按p方差声更强结论；0<p<1任意成立。Σw_j²=0时两边皆零。

## 2. 连续cell积分的Jensen与sup可测性

对每个w_j>0用概率g(x)dx/w_j在cell j采独立U_j；这些点仅为证明工具。固定**同一**ξ后，对每H有

    ∫g1_H(1_M−p)=E_U Σ_j(ξ_j−p)w_j1_H(U_j).

于是sup_H|E_U·|≤E_U sup_H|·|。交换有限ξ平均与U积分，点云上统一成立的第1节界直接给主稿(1)。它控制的是absolute discrepancy，既未假∫_Hg有lower，也未将cell内g/H换成中心值，所以不产生cell-boundary误差。U_j不写入输出mask，更非subδ打孔。

可测性已实际检查。H由有限维实系数及有限个Boolean choices参数化，(H,x)→1_H(x) Borel；g取Borel代表后，积分test是Borel参数函数。U上sup的strict上水平集是Borel集的参数投影，故analytic、对有限Radon产品概率的completion可测。sup被Σw_j支配，积分存在。外层ξ仅2^K个状态，逐状态sup为实数，可测性没有遗漏。一般Lebesgue g换Borel代表不改变任意H的积分，且统一误差受全局零L¹差控制。主稿允许outer expectation亦足以推出存在mask。

这比“固定一个H应用Hoeffding”多了必要的统一步骤；没有偷将对每H分别存在的mask换成一份共同mask。

## 3. 同一mask同时保体积和原incidence

在A={a≤f<2a}上，V=|A|、J_A=∫_A f，确有aV≤J_A≤2aV。cell质量平方和分别满足

    Σ(∫_Q1_A)²≤δ^nV,
    Σ(∫_Qf1_A)²≤2aδ^nJ_A≤4a²δ^nV.

将两种sup分别除V和aV后**相加**，期望≤C sqrt(δ^n log(2K)/V)。有限ξ空间上有某一状态使该和不超过上界；因此两sup由同一mask控制。若要联合概率趋1的逐管事件，阈值增4倍使此和的good event概率≥3/4，做法正确。

取H=R^n和r≤p/4，

    V'≤(p+r)V≤5pV/4,
    I'≥pJ_A−raV≥3pJ_A/4.

第二步用aV≤J_A，未误用反向不等式。I'>0，且f>0在A上，所以E'=A∩M与union of retained marks一致（至多null差）。

## 4. Carrier估计为absolute-error的合法用途

若|H|≤C V'，则

    I'(H)≤2ap|H|+raV≤(5/2)aCp²V+raV.

以I'≥3paV/4相除，得(10/3)Cp+(4/3)r/p≤4Cp+2r/p。先固定C,θ，再取p≤θ/(16C)、δ小至r≤θp/8，使upper≤θ/2<θ。这个顺序正确；C不是随机mask选后再调的常数。小体积H的误差虽未按|H|缩小，但r由整个原层的V控制，已足够本结论。

主稿没有声任意H的相对均匀，也没有声全supporting axes不存在代数carrier；其积分test只是被删后实际Lebesgue marks。低维零体积H对该积分的质量自动为零，不产生奇异测度例外。

## 5. 原dyadic层、N/I/log与nearfull指数

f是有限原indicators之和，1≤f≤N在E上；至多L₀=1+ceil(log₂N)层覆盖其正部分。选J_A≥I/L₀，由a≤N有

    V≥J_A/(2N)≥I/(2NL₀).

以主稿声明的规范I=λNδ^(n−1)，得到V/δ^n≥λ/(2δL₀)。N≤C₀δ^{−(n−1)}给L₀=O(log(1/δ))，K≤C_Bδ^{-n}给log(2K)=O(log(1/δ))，所以

    r²≤Cδ L₀ log(2K)/λ
       ≤Cδ^(1−η)log²(1/δ)→0,   0<η<1.

无须对V额外给smallfootprint lower。δ^η密度下每层含足够多整δ格，这是whole-cell筛选可用的关键floor。

实际输出Y_i'=Y_i∩A∩M⊂原Y_i⊂原T_i；原N、方向、角帽、axes和clock不改。因此

    I'≥3pI/(4L₀),
    λ_new≥cpλ/L₀.

cp/L₀不能逐字保λ_new≥δ^η；对任意η'>η才可在δ充分小时保证δ^η'。主稿已正确写明。用条件carrier规则时从λ≥δ^(η/2)起步，才可在同规则的η门槛上再次调用。这两个量词方向一致。

I一直是Σ|Y_i|而非|E|；N始终是原N。此处体积规范与通常管体积只差固定ambient常数，没有把点访问count当I。若额外删管比例q、保原I比例p_I，平均密度=(p_I/q)λ；不能把保层量的p误当每管保量。

## 6. 逐管mask和格式边界均未越权

只做M时，单管cell权w_ij≤δ^n、平方和≤δ^n|Y_i|，Hoeffding以偏差p|Y_i|/4给

    P(bad_i)≤2exp[−cp²|Y_i|/δ^n].

若每原管|Y_i|≥δ^ηδ^(n−1)、η<1，且N为多项式量级，union bound确使同一mask逐管保3p/4的事件概率→1，可与第3节的3/4事件相交。但layer A可能先删光若干管，因此主layer+mask结论仍只有平均保证。主稿明确区别，不把这个可选tail偷用于fullsource的point-pencil/filled-X lower。

M为完整δ格并；原cell-shading的f在格内常数，A也是格并，故输出仍同类。一般round管marks的A未必是格并，此时输出仅取真实子集，不填格、越出原管。whole-axis CW/PW upper只因原轴未改而保留，source AD lower/selectedξ/Φ等没有因此自动保留。

C,s,D须先固定。若C随λ_new恶化、例如达到1/p量级，carrier允许体积可能已经足够，本证明不否它；若格式随δ增长，pattern entropy也须重新收费。主稿没有外推这些版本，也没有据此否nested partition、whole-axis near-variety或付费多个carrier之和。

## 7. 条件smallfootprint规则的双向强度

固定β>0和一个在合法平均shading删选下封闭的原几何类（例如原饱和方向族，保所有原labels、可允许空marks）。定义R_β(η)：存在固定s,D,C,θ,δ₀，对所有δ<δ₀及该类λ≥δ^η、|E|≤δ^β的实例，存在fixed-format H，|H|≤C|E|且I(H)≥θI。

若R_β(η)成立，并在任意小δ有同类λ≥δ^(η/2)、|E|≤δ^β实例，则第5节产出同类新实例：λ_new≥cpδ^(η/2)/L₀≥δ^η，E'⊂E仍small。规则给H，新mask估计却排全部这种H，矛盾。因此

    R_β(η) ⇒ 不存在足够小δ的
       [λ≥δ^(η/2), |E|≤δ^β] 实例.                  (7.1)

反向，若某η已有相应finite排除，同η域中任何carrier规则真空成立。于是固定β下的“存在足够小η”的规则与finite正幂排除具有相同**逻辑强度**，正向有明确η→η/2余量。不是说同一固定η下逐字双向，也不是一种已证的finite增益；若原类要求每管lower或完整point-structure，删选closure本身须另核，本结论不免费扩展。

这是本轮最关键的范围检查：无条件的任意平均marks fixedC规则确被实际筛后族反攻；只在尚未构造出的power-small族上声称的规则，未由本稿证明为假。其条件性不能靠“把假想小族mask一下”升级成真实Kakeya反例。主稿§7的最终表述保留了这一逻辑区分，审查通过。

## 8. 与旧记录的闭包核及最后判断

R101的原命题使用native finite见证图、AD/tubeKT和完整witness box；其随机选边反攻仅保一个离散图/第三prior，并无任意physical L¹积分、wholeδ-cell mask及原真实marks输出的统一命题。因此不能把本结论简单视为其原全称statement再次调用。R10已有固定格式pattern＋随机标签的一般工具，并以quadrature/ghost-swap处理其专用level模型；当前证明使用同一经典工具族，新增的用途是cell内Jensen、同一mask控制两种原权及原密度floor。它不是新的概率理论，也不证明前沿新颖性。

未发现需阻断的数学项。working目标均由主稿(1)–(6)付清，§7的可选逐管和条件carrier逻辑亦通过；主稿对HRZ/rough source及ordinary未越权。完成本有限closure审查不完成长期Goal，不登记newID/major，不预认证归档或Git同步。
