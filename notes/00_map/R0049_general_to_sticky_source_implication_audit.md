# R0049：general→sticky 的原文蕴含、原质量与外网格责任

2026-10-17，A。对应唯一任务 E5*，不操作 Git。本文不是一般五维归约的证明或反例，不认证整个 WZ2025 Proposition 3.2 或 WZ2026 §18 的全部证明。局部修复和额外近 sticky 子类的结论不登记为新维数结果；须另经独立审查，且未经外部同行评审。

## 1. 入口、当前命题与停止条件

已读 GOAL/STATE/ROADMAP、registry/latest、AGENTS、本轮 working_spec 与 R48 next。E5* 的输入是有界 R5 中原 full δ-direction net、每 label 权 1、逐管至少 δ^(-1+η) 个原访问及真实并集 ≤δ^κ0；目标是在保 ≥δ^ε 原计数访问、共同合法 affine/clock 变换后，得到 h 尺度 uniform-count joint 4-AD/CW/平均近满 shading，并保正的归一化亏损 κout≥cκ0。这里 κ0∈(0,1) 固定，ε≪κout；不能只得到某个规则管族便宣布完成。

本轮检查两类不同命题：

1. 文献是否从上述 ordinary 输入出发，给恰为 4 的 joint AD 和保亏损输出。
2. 已经假设 sticky 或 joint AD 的极值化究竟能推出什么，以及其重缩中原 marks 和外网格体积的真实费用。

若只得 sticky 类内的自相似、额外近 sticky 假设下的提取或需吞掉 κ0 的 fixed-power 费用，即停止 general→sticky gate；不把 entropy/cover/AD 阈值换名续轮。

## 2. 实际读本、定位与版本边界

主要读本是已存 `wang_zahl_2025_sticky_kakeya_2210_09581_v2`（69 页）及 `wang_zakharov_2026_sticky`。下列行号按各 extracted 文件的 `split('\n')` 一基编号；formfeed 不另切行。

| 原读本 | 实读范围 | 本文使用 |
|---|---|---|
| WZ2025 PDF2、5–8 | lines79–105、240–386 | sticky/ε-close 定义、Conj1.2、finite M/σn 的输入类 |
| WZ2025 PDF11–16 | lines572–858 全部 | Def3.1/3.2、Lemma3.3、Prop3.2 完整三步及质量/重数公式 |
| WZ2026 PDF65–76 | lines3351–4020 全部 | Def17.1–4、Prop17.2、Prop18.1/18.2、直到(145) 的极值配置构造 |

2026-10-17 打开 [arXiv 官方页](https://arxiv.org/abs/2210.09581)：当前仍 v2，修订 2025-10-07；期刊信息 JAMS39(2026),515–585，DOI [10.1090/jams/1067](https://doi.org/10.1090/jams/1067)。页面声明 v2 结果不变。尝试 AMS 正式 PDF 的 web 入口未返回可读全文，故本文不声称刊本与 v2 逐字相同，也不声称刊本已修或未修下述(3.5)。没有新刊本 bytes/hash。

已用 `pdftoppm` 渲染并实际查看本地 v2 PDF13，临时图 `tmp/R0049_wz2025_p13.png`；确认(3.5)的常数可比和其前后文字是 PDF 字面，不是 OCR 丢失上标。本文没有据此反驳原最终定理。

## 3. WZ2025 起点本来含 sticky：不是 ordinary 极值化

Def1.1 的 sticky K 要求可选择的原线族 packing dimension 为 n−1，并含全部方向的单位线段；Def1.2 将其放宽至 n−1+ε。Conj1.2（PDF6）才讨论 ordinary Kakeya 反例的最小 Hausdorff 维数是否迫近 sticky；它在此处是猜想，不是 Proposition 3.2 的结论。

finite 类更明确。Def2.1（PDF7–8，lines350–378）定义 M(s,t,δ)，其所有输入须：

* (a) joint line-parameter metric 中 essentially distinct；
* (b) **每个 δ≤r≤1** 有 r-tube cover，任一 r-direction 周围至多 δ^(-t) 个 cover 元素；
* (c) 原总 incidence volume Σ|Y(T)|≥δ^s。

σn 是这一类的 infimum/limsup 指数，不是任意 ordinary 小并集族的维数亏损。Def3.1 的 η-extremal 在小并集 ≤δ^(σn−η) 之外，仍原封保留(a)(b)(c)。Lemma3.1 仅保证在此类内有任意小尺度的极值见证。

方向 δ-separated 只控制每个方向角球内的细管数，不能送入(b)的每尺度 joint cover；原截距可散布。R42 的 digit-permutation 可作精确读本校准：δ=ε²，A,B 各取四维 ε 网，v=εA+δB，b=εB。v 是 full δ 网；在一个 ε-direction bin（A 固定）里，截距 b 占 ε^(-4) 个 ε-separated cells，覆盖至少需要 cε^(-4)=cδ^(-2) 个同方向粗管。因此 η<2 时不能满足(b)的 δ^(-η) 门槛。

这个例子没有证明小并集 ≤δ^κ0，故不是 E5* 反例。它明确指出 source 的额外假设位置，不能把满方向输入自动当 sticky。

## 4. Proposition 3.2 的完整质量依赖

Prop3.2（PDF12，lines604–615）量词为 ∀ε∃η,δ0∀δ小，对**η-extremal 输入**及 ρ∈[δ^(1−ε),δ^ε]，输出原 refinement 和 balanced ρ-cover；粗族及各 parent 的 unit rescaling 都 ε-extremal，并有 coarse/fine 点重数上界。Refinement 的原定义（lines326–338）只允许删原管/原 δ-cubes，保 log^(-C) 原总 incidence，而非重新创造 uniform 权或 marks。

完整 proof 的依赖如下。

1. Step1（lines702–729）直接用 Def2.1(b) 选 cover；constant-fraction 颜色删选使每细管有唯一 parent、parent 与某原管同轴并有空间 buffer。δ^(-η) coarse-direction 重数再用 ρ≤δ^ε 转成 ρ^(-η/ε)。这一段已是 sticky 假设的使用，不是从少体积推 sticky。
2. Step2（730–748）将 parent 的原 incidence equalize，得到(3.9)。#parents≲δ^(-η)ρ^(1−n)，故每 parent 有 δ^(Oη)ρ^(n−1) 的原 incidence；然后调用单 parent Lemma3.3。原(a)(b)对子族保持，(c)需重付；unit-rescaling 的外网格体积见下一节。
3. Step3（754–853）在原 ρ-cubes 上做 heavy/pigeonhole。原每 parent 细管数(3.12)、每粗 cube incidence upper(3.13)，配原总 incidence lower，给粗 incidence(3.17)。再造 μfine、均匀每 cube 原 union w 和 μcoarse。
4. 极值类 M 的 lower 给 μcoarse upper(3.18)，单 parent lemma 给 μfine upper；**原极值并集 upper δ^(σn−η)** 与总 incidence lower(3.19)才反推二者 lower(3.20)。由这些同一 σn 的饱和关系得粗/细亏损，最后删低 parent 原 incidence 以恢复(c)。

因此此 proof 并不将任意 κ0 替入 σn 就成立。一般输入没有给与 σn 同一类的 lower bound，也没有证明必须同时饱和 coarse/fine 重数。裸 Jacobian 更不可能自动保 normalized union deficit。

## 5. 外 h-grid 的(3.5)有一项实际责任

Def3.2（PDF11，lines586–596）取 φ 为刚体变换加 transverse ρ^(-1)、clock 常数倍的 dilation；h=δ/ρ。它将 Yhat 定义成所有**与 φY 相交的 h-cubes 的并**。原(3.4)的确给 |φE|≍ρ^(1−n)|E|；但 φ(δ-cube) 的轴长为 h^(n−1)×δ，outer h-grid 可沿 clock 多付 h/δ=ρ^(-1)。

PDF13 的(3.5)直接写 |E|≍ρ^(n−1)|Ehat|，仅以(3.4)为由，尚未加入 clock-block 密度条件。故这里的常数比较不能只由定义与 Jacobian 推出。一个 δ-cube 已显示几何原因；以下例子还符合原(a)(b)与单 parent 所需的质量阶。

取 n=5、ρ=δ^(1/2)、h=δ/ρ，所有轴截距 b=0，方向在大小 cρ 的四维 box 内取 δ 网，#T≍h^(-4)。每个尺度用方向网覆盖只需每 coarse-direction O(1) 个 parent，故满足(b)。在 t∈[1/2,1] 的每个 h-clock block 内，仅保前 θh 长的原 δ-cube marks，θ=δ^η，η<1/2（取 dyadic 参数使 δ|θh）。则

\[
 I\asymp\theta\rho^4,\qquad |E|\asymp\theta\rho^4,
 \qquad |\widehat E|\asymp1.
 \tag{1}
\]

前两式来自远离共同原点后各细管仅有 O(1) 重叠且填充横向 ρ-box；最后一式来自每 h-clock block 都有 marks，并在每层占固定比例的横向 rescaled box。于是 ρ⁴|Ehat|/|E|≍θ^(-1)→∞，不为常数。此例不声称经过 source 所有后续 refinement 仍保每 block；它仅否定未经额外论证的常数(3.5)。θ^(-1)=δ^(-Oη) 很可能可支付，并不否定 lemma 的最终小幂结论。

## 6. 可支付的单次 local regrid 修复：原 marks，不加密

下面是本轮独立证明、并与 root/B 讨论核对的局部修复，不宣 source 已写过，也不认证完整 Prop3.2 的所有后续步骤。

**局部引理。** n=5。所有原 δ-tubes 在一 ρ-parent 中，h=δ/ρ。先做 essentially-distinct/constant-multiplicity 的合法 refinement，记所得原集为 initial，原 union E0，原 incidence I0，原点重数 μ0。假设

\[
 I_0\ge\delta^a\rho^4,\qquad N=\#\mathcal T_0\le\delta^{-b}h^{-4}.
 \tag{2}
\]

这里 constant factors/polylog 已吸入 a,b=Oη；单管 |Y(T)|≤Cδ⁴，故另有 I0≤Cδ^(-b)ρ⁴。对任意 u>0，置 θ=δ^(a+b+u)。可以仅删原 marks，损失 ≤Cδ^u I0，并得到

\[
 |\widehat E'|\le C\theta^{-1}\rho^{-4}|E_0|.
 \tag{3}
\]

**证明。** 用 parent 轴为 clock，将每管原 δ-cubes 按 cube 中心的 clock 分到长度 h 的 blocks J；每管只有 O(h^(-1)) 个 blocks。细轴与 parent 夹角 Oρ，所以一个 block 的原横向漂移 O(ρh)=Oδ，原 δ-cubes 经 φ 后全部在一个 Ch-box 内。删掉 marked volume <θhδ⁴ 的整个(T,J) block。总损失

\[
 \le C(N/h)\theta h\delta^4
 \le C\theta\delta^{-b}\rho^4
 =C\delta^{a+u}\rho^4\le C\delta^u I_0.
 \tag{4}
\]

每个剩余 outer h-cube Qhat 的原 witness 属于一个 heavy block，其 φ-image 有体积 ≥cθh⁵，且位于 C Qhat。对 h-grid 的固定放大有 bounded overlap，故
`#Qhat·cθh⁵ ≤ C|φE0|`，这就是(3)。边界 δ-cube 整块保留，不制造新时间 marks；clock 交界只造成常数放大。

**点重数的正确使用。** Heavy 删除会破坏“当前处处 μ0”，所以不能把 μ0 改写为新 hat 总 incidence/新 hat union。应一直保 initial 常重数等式 |E0|=I0/μ0。若剩余 hat 家族经原(a)(b)(c)与 σn 定义给
`|Ehat′|≥h^(σn+ε′)`，则(3)及 I0 upper 给

\[
 \mu_0\le C\delta^{-b}\theta^{-1}h^{-\sigma_n-\varepsilon'}.
 \tag{5}
\]

当 ρ≥δ^(1−ε)，h≤δ^ε，于是 δ^(-c)≤h^(-c/ε)；选择 a,b,u=Oη、η≪ε²，可将附加指数吸入目标 ε。原(a)(b)对子族继承，hat(c)由 |φY′| lower 和 I′≥(1−o1)I0 得到；从 N(s,t) 的 limsup 得所有足够小 h 的 M lower，不需挑新的不同尺度。

**严格边界。** (3)只对本次 heavy-block 输出保证。Prop3.2 Step3 后续按点、按粗 cube、按重数作 arbitrary refinement，可以把每个 block 又删薄；不能无证继续沿用(3)。若要完整修复其最后每 parent 的 normalized union upper，必须将 compatible block 密度与后续 balanced/μfine 操作一起维护，或逐次补付合法修复并重算预算。本文没有完成该整合，故不把 source 定理标为已证或已否。

## 7. WZ2026 Def17.1/Prop17.2 的量词不是任意 E5* 输入

Def17.1（PDF65，lines3356–3360）中 Kd(κ) 的假设已经是 joint `(d−1,δ^(-η))-AD` 原管族、CW≤δ^(-η)、平均 δ^η-dense shading。它允许方向重复，也不假 ordinary full-direction net；joint AD 的 lower 是明写的输入，不是方向 separation 的结果。

Prop17.2（lines3439–3443）令 κ=inf{κ′:Kd(κ′)}，在 κ>0 时，对任意指定函数 g,h 及阈值 δ0,η0 **存在**一套 δ,η,γ,k,ℓ 与全局/混合配置。它选择 extremizing witnesses，不是“对任意 κ0 小并集 ordinary family”输出。Kd(κ) 若在 inf 处需使用，可由 ε-budget 取 Kd(κ+ε/2) 再减半 loss 支付；不应无证假定 inf attainment，也不必因此否定该接口。

Prop18.2（PDF68 左右，lines3486–3495）从 Kd(κ−ν) 的失败出发，选择**已经 joint AD/CW** 的新 T 与原 shading，其 union(104)≈δ^(-d+κ)；不是对 E5* 某个给定输入删选。正式否定 Kd 给任意小 δ 的反例见证即够；无需把文中“all sufficiently small δ”读成对每 δ 都有同一坏 family 的额外结论。

## 8. §18 到(145)：哪里保原 law，哪里重新生成配置

逐段实际读到 PDF76/lines4020；这里只认证此处对 E5* 的蕴含范围，不重认证所有已具名的中间几何引理。

| 步骤/公式 | 原质量或几何输入 | 对 E5* 的限制 |
|---|---|---|
| (105)，选择 η≪ε1≪ηd≪… | 极值原 incidence/union 迫大重数 | 输入已是 joint AD/CW 极值类 |
| ℓ-linear stars、uniform point-line X′，(106) | Lem4.2 原关联删选、原 coarse shading DρY′ | 不是自动重设新的均匀原 law |
| (107)/(109)，到(111)–(113) | 原 Tρ,Y 及原 T[parent],Y 的 Kd lower 与极值重数饱和 | 必须用相同 κ；任意 κ0 小并集不保证这些饱和 |
| (114)–(126)，ξ/coarse Φ | 原 tuple/wedge/coherence 及 dense grids | 已在合法源配置内；不能由普通 direction net 免费生成 |
| ρ-parent 再缩，原细 index→DδellT | coarse 去重后再 anisotropic dilation，δtilde=√δell | 不是每原 label 一一 affine 变换；原计数和 union 不能只写 determinant |
| (127)–(140) | X′/extremal multiplicity 得 slice AD，filled X 因子析出 Yz，Obs3.4 给 CW | AD 与 deficit 同来自极值类，非一般 smoothing |
| Prop18.1，到(145)/(103) | 对 AD Yz 用结构 lemma、共同 parent/scale 迭代，最后 thickening 吸收误差 | 输出是新配置；厚化和 scale/loss 须按 source 参数付出 |

R43 已核 fine-PW 的原权 coarsening/同 clock 接口，不等于已认证 §18 全部 point-density 几何；本轮没有把旧未付项抹掉。Remark17.1 从新 E 与 T 定义 shading，平均 δ^(Cη)-dense 仍不保证它就是 E5* 最初给定的任意 marks restriction；这个 association 也要证明。

因此 source 给的是“若 joint AD/CW 类的最优维数仍不足，则有高度结构化 extremizers”，不是 ordinary→joint4AD 的入口定理。两种 κ 及两种存在/全称量词不能混用。

## 9. 一个真正可付的额外近 sticky 子类：独立核 B 的树方案

本节是给 E5* 的**额外输入测试**，不是从小并集推该输入。设原 full δ-separated directions 的 joint 参数集 P⊂boundedR8，#P≍δ^(-4)，并假设对所有 dyadic δ≤r≤1，`N_r(P)≤K r^(-4)`，K≤δ^(-η)。每原 label duration≥δ^η，保留 whole 原 marks。

在有界 R8 的 dyadic tree 从细向粗处理：若某 r-cell 当前存活 descendants 少于 θ(r/δ)⁴，就删其全部 descendants，θ=δ^(ε/2)。原 occupied r-cells 至多 CKr^(-4)，因此

\[
 \#P_{\rm deleted}\le CK\theta\log(1/\delta)\delta^{-4}.
 \tag{6}
\]

关键不是仅在处理当时有 lower。若一点最后存活，其任一较细 cell 后续不会被局部改动：后续删的是较粗 ancestors，要么整 cell 连该点一并删，要么不删。故所有最后 occupied dyadic cells 的 lower 同时成立。一个以存活点为心、半径 r 的球包含该点所在尺度 cr 的 cell，于是 ball lower≥cθ(r/δ)⁴；upper来自原方向 δ-separation 的 `(r/δ)⁴` packing。得到真正 joint4-AD，loss 仅 θ^(-1) 常数幂。

原 incidence 下界 ≥cδ^η#P（用 duration units），每删 label 最多 C duration，故 incidence 相对损失
`≤CKθlog(1/δ)δ^(-η)=o(1)`，η≪ε。保留的每管仍带**全部原 marks**，union 不增，未缩 clock、h=δ，原亏损 κ0 不变。

CW 也需说明：对整个 unit graph tubes，若凸集 U 容纳一根管，则其 John axes 中至少一轴为常数长度，其余各轴≥cδ。可容纳的 directions 的 δ-neighborhood 体积≤C|U|；δ-separated directions 因此 #T[U]≤C|U|δ^(-4)。存活总管数≈δ^(-4)，故 C_CW=O(1)。这里使用 whole unitclock/whole tubes；短 piece 不能不付 clock 费用照搬。

这项证明严格填了一个近 sticky 上界→同 exponent 双边 AD 的有限子类接口，同时保原 labels/marks/deficit。其额外 all-scale cover 上界尚未从 E5* 的小并集假设推出，所以不解决主候选，也不能下一轮将这个未证上界换名为 entropy 初始化而继续同一路线。

## 10. 有界 primary 外查与本轮后的不同机制

实际打开 Nadjimzadah 正式 [GAFA 页面](https://link.springer.com/article/10.1007/s00039-026-00750-4)，读 §1.3/§1.5 与 AppendixA 目录/相关 theorem statements：ordinary general→sticky 成功范围在 R3；高维只是可望，新增 curved 步骤也没有给本轮 R5 入口。正式版多出 Appendix，不能把它与已打开 arXiv2511.10918v2 字节/命题完全等同。本次有限读段没有发现可直接调用的 E5* 定理；不据无命中认证不存在。没有下载新 bytes。

下一机制的有限候选可与本轮 AD 入口分开：Fu–Gan [arXiv2009.09108v2](https://arxiv.org/pdf/2009.09108)，实际读 PDF1–5 的 graph Kakeya map 定义、Theorem1/2 及 winding 接口。其 positive-measure 定理要求连续方向截距，且边界 Hölder α>n(n−2)/(n−1)²，或边界 W^(1,p),p>n−2；n5 的 Hölder 门槛为15/16。本文未用它证明任何原族结论，也没有重证高级 winding 估计。

旧记录排重：R47 已指出 rough direction-table 的任意插值可能离开原 Cδ-neighborhood，determinant 积分还需 multiplicity；R41 的低条件熵已冻结。Lusin 只能在大测度紧集给 continuity，不能送 open direction ball、统一模数或上述边界正则性。若下轮选此路线，应只测一个真实有限→边界 winding 的原体积回传 gate，先独立反例攻击，不把 generic smooth 插值/Lusin 改名作新证明。

## 11. 归档结论与未付责任

主 E5* 未证未否。WZ2025/2026 已读 source 未给 ordinary 满方向小并集→joint4AD/CW 且保 κ0 的完整入口；其 sticky/AD 假设、极值 σ/κ 饱和及新配置存在量词已定位。外网格恒比有具体责任，单次 block-heavy 修复可保原质量并付 δ^(-Oη)，但尚未完成它与 Prop3.2 后续全部 refinements 的联合维护。额外 all-scale cover 上界子类确实可树删选，未从原小并集导出。

按本轮停止条件冻结 general→sticky 初始化 gate；新的 cover/entropy 阈值若只是同一未证入口，不另开轮。高级文献具名使用与本项目已逐步验证内容继续分开；没有 ordinary R5/一般维数或重大中间结果声明。长期 Goal active。
