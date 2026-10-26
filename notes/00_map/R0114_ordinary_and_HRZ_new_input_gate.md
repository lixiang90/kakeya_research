# R0114：ordinary / HRZ 宏观与真实 shading 的有限复杂度压力门

2026-10-26，algebraic_gate。只编辑本文件，主代理统一 Git。已读 GOAL、当前 STATE、ROADMAP 主表及 R113 更新、registry/latest=R0113、R113 next；执行本轮先周期宏观，不续三角/DAG/block、resolution、jointcap 或 KT 数表。下文没有 ordinary 新下界、完整 source gain、major 或一般反例，未经外部同行评审。

## 1. 先固定完整 ordinary 输入及 HRZ 的实际出口

原 R5 中固定 bounded 区域 B，真实单位 round δ tubes T_i，方向严格 δ-separated，N≈δ^-4。每管有自己的 measurable Y_i⊂T_i，E=∪Y_i，I=Σ|Y_i|，共同管体积 uδ≈δ⁴，平均 λ=I/(Nuδ)。方向/clock/位置/原 marks 都不换成独立模型。small-footprint 反设是

    |E|≤δ^(1−γ),     λ≥δ^η0,

γ>0 固定、η0 在 γ 后足小。若另要求逐管 lower，则须与平均版区分；本稿的 pressure 只直接消费平均输入。真实全方向满足该 power-small 反设的 nearfull 族本身涉及开放问题，不能拿 full-volume bush 冒作它的反例。

实际读回库内 HRZ `hickman_rogers_zhang_2019_v1.txt` 的 Th1.3–1.4、Th4.1/Prop4.2 和 narrow contraction 的 e(p,n,k) 段。原 multiscale Wolff 计数对同一原 T 在 nested balls 与各维 varieties 的 rich 事件**同时交集**计数，不是分别存在每层 rich 子族即可相乘；公式中的 ρ/λ_j、原条数和 degree 常数不能抹去。其 broad→linear 要

    p>(n−k+2)/(n−k+1),
    e(p,n,k)=(n−k+1)p−(n−k+2)>0.

n=5 欲由此得 dimension>4 须 p<4/3，而 k≥3 的原 narrow 入口已不覆盖该区间。k=2 不能被这句话一并排除，但仍欠其实际 raw terminal / parent norm 输入，R60/R61 已核的 G3 替换不自动给 fixed saving。本轮没有再优化这张旧参数表，也没有重开它。

完整出口宏观判定：ordinary 初始化仍须从原 small E 得真实共同几何；HRZ 需它能进入原 narrow/terminal/parent 数量；full rough/mixed 另缺同一 same-T/filled-X/Phi/xi/native-Y/CW 联合实现；counter 仍须同集全方向且 strict Hausdorff upper。R113 的 proper 类证明和 R112/R113 拒桥没有交付这些输入。当前不锁 qualified positive mechanism。

## 2. 本次可证伪候选：同体积 fixed-format carrier 能否自动出现

一项自然但具体的初始化候选是：仅据原 arbitrary-shading small-footprint，得到某个 fixed-format 半代数 H，使

    |H|≤C|E|,       I(H):=Σ_i|Y_i∩H|≥θ I,          (C)

其中 C≥1、θ∈(0,1) 与格式界 A 固定，系数可随 δ 任意变化。它若真能被廉价取得，才可能对原 direction-separated family 调 polynomial-Wolff/形状计数。本轮先攻击 (C)，不先假 E 是 fixed-format，更不把期望中的 joint structure 当作新输入。

root 提醒并提出的关键修正是：不用只在 sub-δ 周期条纹上作反攻，而对**原 δ-grid whole cells**作 Bernoulli mask；不能声所有 H 有 uniform relative discrepancy，只能证统一 absolute error。以下已独立核该有限推导，并给可直接作用于任意真实 measurable marks 的版本。

## 3. 有限复杂度类的绝对随机筛选：不靠 boundary cells

令 Q_1,...,Q_K 是 B 内 side δ 的 grid cells，K≤C_Bδ^-5。边界取半开，只影响零集。固定 nonnegative integrable g，记

    w_j=∫_(Q_j)g,     W=Σw_j.

独立 ξ_j∈{0,1}，P(ξ_j=1)=p∈(0,1)；令 M_ξ 为所保 whole cells 的 union。格式≤A 的半代数类记 H_A。对每个 w_j>0，在 Q_j 内按概率 g/w_j 独立取 U_j，并令它独立于 ξ；w_j=0 的 cell 可跳过。则对固定 ξ，Jensen/sup 给

    sup_H |Σ_j(ξ_j−p)∫_(Q_j)g1_H|
      ≤E_U sup_H |Σ_j(ξ_j−p)w_j1_H(U_j)|.           (1)

这没有把跨 boundary 的 cell 整个计错；积分是在真实 H∩Q_j 上精确取的。

固定 U 后，格式≤A 的 H 在 K 个点上所能实现的不同 indicator patterns 至多 C_A(2+K)^d_A。可直接用 polynomial coefficient lifting 解释：degree≤D 的多项式系数维数 binom(5+D,D)，点上的 sign vectors 是该系数空间中 K 个超平面的 arrangement faces；固定数个多项式/Boolean 组合只把多项式增长的指数与常数改成依 A 的数。允许零符号和任意 real coefficients，不假系数高度下界。

对任一固定 pattern，Σ(ξ_j−p)w_j1_H(U_j) 为 centered independent bounded sum，Hoeffding 的 mgf 参数≤CΣw_j²。对全部 patterns 和正负号作 log-sum-exp/union bound，得到

    E_(ξ,U) sup_H |Σ_j(ξ_j−p)w_j1_H(U_j)|
       ≤C_A sqrt[log(2+K) Σ_j w_j²].               (2)

由 (1) 再取 ξ 期望，统一 absolute discrepancy 即有相同上界。有限点的 patterns 存在性是有限实多项式量词命题，故相关 supremum 可测；也可用其 universally measurable 版本。这里不是对任意极小 H 的相对 p 误差；H 当然能钻进某个选中 cell 的很小子集。

若 g 在 E0 上满足 a≤g<2a、其余为0，V0=|E0|，则 w_j≤2a|E0∩Q_j|，从而

    Σw_j²≤2aδ⁵∫g≤4a²δ⁵V0.

另对 g=1_E0 同用 (1)–(2)。同一 ξ 的两个非负误差的期望相加，因此存在一个确定 whole-cell mask，使同时

    sup_H |∫g1_H(1_M−p)|≤ε aV0,
    sup_H |∫1_E0 1_H(1_M−p)|≤ε V0,
    ε=C_A sqrt[δ⁵log(2+K)/V0].                    (3)

常数吸收了同时筛选费用；可把全 B 加入查询类，所以 (3) 也控制所保 total mass/volume。若原 marks 已是 cells 的 union，g 在 multiplicity layer 内 piecewise constant，(1) 可简化成每 cell uniform sampling；故本证明也封住“先 δ-cell 化便自动得到 (C)”的直接逃门。

## 4. 真正应用于原 tube incidence，而非 abstract mask

对当前原 Y_i 定义整数 multiplicity f=Σ_i1_Yi。分 dyadic 层

    E_j={2^j≤f<2^(j+1)},      0≤j≤ceil(log2 N).

令 J0=1+ceil(log2 N)。某层 E0 有 I0=∫_(E0)f≥I/J0。设该层 2^j=a，则 a≤f<2a；把各原 marks 改成 Y_i^0=Y_i∩E0，原 tubes/axes/directions/N/共同 clock 完全不动，允许一些 labels 的 marks 为空。V0≥I0/(2N)，所以

    V0≥c λ δ⁴/J0,
    ε²≤C_A δ J0 log(2+K)/λ.                       (4)

N≈δ^-4、λ≥δ^η0、η0<1 时，(4) 使 ε→0。没有依靠 E0 为 semialgebraic，也没有用 |Nδ E0| 代 V0。

取 (3) 的同一 whole-cell mask，并设 Y_i'=Y_i^0∩M、E'=E0∩M、I'=Σ|Y_i'|。于是

    V'=|E'|∈[(p−ε)V0,(p+ε)V0],
    I'≥p I0−ε aV0≥(p−ε)I0.                       (5)

对任意格式≤A 的 H，有

    I'(H)≤p∫_H f1_E0+ε aV0≤2ap|H|+ε I0.

因此在 |H|≤C V' 时，

    I'(H)/I'
      ≤[2Cp(p+ε)+ε]/(p−ε)
      =O(Cp+ε/p).                                 (6)

先取固定 p≤min(1/4,θ/(20C))，再令 δ 足小到 ε≤min(p/10,θp/10)，便使 (6)<θ。原新的总 incidence 同时仍满足

    I'≥c_p I/log(2N),     λ'=I'/(Nuδ)≥c_pλ/log(2N). (7)

这是一项实际原 measurable shading 的合法限制。不是只有抽象 g 或 label law；mask 不改任何原管支持，所有点仍是原 Y_i 的点，整段方向和物理尺度仍是 δ。E'⊂E，若原 small-footprint 反设成立，新的 upper 仍成立。

## 5. 正确量词：它反哪一条桥，不反哪一条数学主张

(3)–(7) 是无条件的筛选事实；它能从**任何**给定原族的任意 marks 造出此 incidence-flat layer+mask。对 (C) 的准确结论是：在任意平均 nearfull shading、允许合法限制并带小 η 余量的 uniform 初始化中，不能免费声每个新 E 都有该同体积、固定格式、保固定原 I 的 carrier。若原 λ≥δ^η0 而待调用门槛取 η>η0，(7) 的 log 与固定 p 可由 δ0 吸收，真实 density 余量已写明。

若某 theorem 只声某个**原 full per-tube nearfull 族**存在 carrier，且不要求对上述平均限制闭包成立，不能拿层化后的数据直接反它。层化只保 I/log，可能让一些管全空；(3) 本身也没有承诺每管都保 p。后续若再 heavy，可保 I'/2 并写 q≥cλ'，但方向族不再是 literal 饱和 full net，不能重设原 N 或逐管 lower。统一账是 q=1（保全部原 labels、允许 zero shading）、保 incidence 比例 p_eff≈p/logN；若删管重归一，则 λ_new=(p_I/q)λ，概率 cap 除 q。

更重要的是：本稿**没有构造**满足完整 ordinary power-small 假设的 Kakeya 反例；这类 nearfull small E 的存在正是待排对象。它只证明：若用“small E 自动造 literal comparable-volume fixed-format carrier”作为一个对所有合法平均 shading 的廉价桥，则该桥在进一步合法 layer/mask 上必须面对 (6) 的冲突，因而已在承担排除原 small E 的实质强度。不能把它当作无需新几何的简单预处理，也不由此认证一般 small-footprint implication 在空前提下为 false。

## 6. R101 排重和 HRZ 不被这项筛选反驳的原因

已实际读回 R101 `semialgebraic_density_primary_gate` §§4–10 与 `native_graph_witness_and_complexity_gate` 后部。那里有两种不同内容：fixed-format geometric relation 上任意 bounded mask 的保原 mass 正面 box 工具，及 random selected triples 不自动 complete；更强的实际 native 同-witness boxes 则用原 Tube-KT/far-clock/strip 付固定幂的 h-mass upper。本稿不重报这些。

当前 (1)–(7) 的对象是**原物理空间 whole δ cells**、真实 tube Lebesgue incidence f、所有 real-coefficient fixed-format 查询 H 的 uniform absolute discrepancy，以及 |H|≈|E'| 与 I' 同时收费。它不是 R101 的 selected product 完整性问题；也不反 R101 对 geometric supergraph 的正面质量结论。两个失败指纹相关，但查询类型、原质量和证明都不同，本轮不据此登记新数学 ID/重大性。

此筛选没有否定 polynomial-Wolff：PW 对已给定的合法测试 H 给计数 upper，并不保证存在 (C)。也不否定 HRZ 的合法流程：HRZ 并未要求 literal E 有一个同体积固定复杂度 semialgebraic envelope，partition cells/variety neighborhoods 的体积和原 marked fraction本来各自收费；whole-axis tangency 信息不会被保/删一些原 cells 改变。许多 pieces、复杂度增长、或 |H|远大于|E'| 的结构不在 (C) 的否定范围。

因此本次不能靠 cell mask 宣称 HRZ/整个 polynomial 方法失败；真正收缩的是一种非常具体的 ordinary 初始化捷径。parent/nested 计数仍需从原 geometry 提取，不由 (6) 给反向增益。

## 7. 一手范围、候选可行性与宏观停止

本轮有限 web 检索 ordinary 高维/新 polynomial 及 Lipschitz multilinear 入口，实际可直接对照的是库中 [HRZ1908.05589v1](https://arxiv.org/abs/1908.05589v1) 的上述原 statement/proof 段。作者讲义 `jnwt.eu/talks/lisbon_2025-11-06.pdf` 只作 scope screen：其中 Lipschitz multilinear 的低于 endpoint 正面与 endpoint 障碍不是已付的新 R5 terminal；未据此调用高级 theorem，未新下载/新入库。没有把搜索不到当作全球无新工具/新颖性认证。

候选可行性：当前没有合格新的 ordinary/HRZ 正面输入。实际数学缩窄是 root 提出并在此独立核过的 whole-cell absolute screening：small footprint 即使保真实原 N/I、原尺度与平均 nearfull，也不能无费获得 (C) 这种 literal E 的共同方向/shape 输入。主代理如采用它，须另锁 working、逐步独审和准确归档；本分工不预认证未来 proof/review。

不以它自开下一轮、不续 p/ε/format 或 density 阈值优化，不把所缺 cross-direction/whole-axis 几何另命名为成功假设。四完整目标继续开放，旧三角/resolution/jointcap/seed 冻结保持；本轮为周期宏观中的具体拒桥证据，未取得普通维数改善、完整 source 正 gain、真反例或 major。
