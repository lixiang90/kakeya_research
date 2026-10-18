# R0087：分因子原质量、精确类与几何转移边界的独立终审

2026-10-18，A。所列有限范围归约、旧输入应用及具体桥反例限定通过；无未解决强制项。完整 near-contained G4 仍未证、未否，未经外部同行评审。

## 1. 实际全文范围、独审分工与具名输入

已 fresh 实际全文读 root《R0087_full_G4_factor_scope_and_projection_boundary》8节、A《R0087_full_G4_singular_transfer_attempt》8节、B《R0087_full_G4_original_mass_counteraudit》10节、working_spec5、终 macro6、next6。root §7 最新的固定格式半代数 U whole-containment 扩展亦已读回。A/B 中记录 root 未落盘的句子属于先前写作阶段；本正式审查以当前实际全文为准，不把历史 pending 当作已经做过的审查。

本轮实际重读 R60 §§5–9、11–12、R59 §§3–5、R85 root10，FSD001 reviewed页及 R29 A §§1–8；为核 root §5，实际读 Wongkew1993 本地 text 的印刷177–183页中 Main Theorem 与相邻证明段。另实际读 HRZ2019v1 Th4.1、Prop4.2完整证明及(27)/e(p,n,k)，和 §8 开头 tiny bound、(51)–(53)及 nested计数的对应段。没有新 PDF 视觉或字节检查，不冒全文重证 HRZ、KR、Pawłucki、DIR003、Wongkew 或全部高级来源。

A 的 same-π尝试是本人施工，不能算自己的独立审查；其内容已交 root/B 核。本文独立检查重点是 root/B 的原 factor 质量和尺度、root 的 exact local entropy／weighted FSD 链、两桥反攻以及最终整合的边界。QE／固定格式有限分量、Paw globalLip、KR计数、DIR/FSD/G3 等仍按已有明确依赖使用，不将内部互审冒外部同行评审。

## 2. 原 factor clock、真实 marks 与空间求和

实因式分解 P=c∏Q_j^m_j 后，重数不改零集，但原轴近其并不等于某因子含整个轴。root/B 使用 B_ij={t:dist(a_i+tv_i,Z(Q_j))≤Cδ} 的存在量词公式合法；固定 degree／维度的 QE 给统一有限个一维分量，不依系数条件数。距离函数连续、各零集闭，故 assigned 开区间的闭包端点也可供新闭子段使用。所有 clock 分界有限，body 中对应截面的5维 measure为0；这与正体积 round端帽不同。

原每管 density≥λ=δ^η，η<1，端帽总体积 O(δVδ) 可在δ最后小后删，保 λVδ/2。body 用唯一正交 clock 和截面积 upper Cδ⁴，从有限 assigned intervals 中选择一条保≥c_Dλδ⁴真实 marks，故区间长度至少 c_Dλ。若其长度ℓ∈[r,2r)，首尾两条完整 r长子段均含于该区间，且并覆盖它；择一保常数质量，得到长度恰r、whole近对应因子的真实新轴。没有移动点、填满 marks、免费延 clock 或忽略原端帽。

r∈[cλ,1] 只有 O(log(2/λ)) 层。按原非负权选一层保 W/log 后，每剩余 label 仍各自保 cλδ⁴ marks；不是只保一项未绑定 labels 的总平均。以片中点所在半开 r格和 factor 分组，每组 support 落该格的固定倍放大，所有这些 support 的 overlap 固定（再乘≤D因子数），所以 Σ_g|E_g|≤C_D|E|。没有 r^-5 的空间格数量罚；不同 groups 的重叠以真实支持支付，而非假 E_g 互不相交。

## 3. h帽、r⁵回传、η次序与平均 heavy

以组格中心平移、按 r isotropic 缩放后，轴长度恰1、round半径恰 h=δ/r，原 marks 确在这个真实 roundtube内。变换后 Q_j(c+rx) 非零、不可约性保留；重新归一系数不改 metric零集，位置／次数／格式仍固定。新 density≥cλ/r≥cλ。由 r≥cδ^η 得 h≤Cδ^(1−η)，取原 η<η0/4，随后δ小，保证 cδ^η≥h^η0，且 h 进入输入的小尺度区间。不能把 subpower长片或 anisotropic tube 直接当原标准单位管。

方向虽不变，新 h帽仍须由原δ帽覆盖；S4维数4给 α_h≤Cαr^-4，全部原重复 indices／权都按此计。条件于不可约4维 G4在σ成立，实体回尺度为

    r⁵ h^(4+σ) W_g/α_h ≥ cδ^(4+σ) r^(5−σ) W_g/α。

r⁵ Jacobian、h的四次幂与 r^-4 帽罚缺一不可。选 σ=min(ε/4,1/4)，η≪ε和η0，r≥cδ^η及一层 log费确可吸入最终ε。低实维因子由已存G3的 λ³输入取足小 nearfull门槛得到同形结论；degree1由flat DIR覆盖。因而“完整全P类”与“实不可约 real-dim4类”是条件于所列既有输入的正幂范围等价，不是剩余类已证或新的方向。

平均版本另核：密度σ_i≤1，Σw_iσ_i≥λ_avW；heavy到σ_i≥λ_av/2可保 W′≥λ_avW/2，未归一α继承。用ε/2逐管结论，取η_av≤η_per/2并小于ε/4，吸真实λ_av权损才得平均ε版。整label restriction与再次裁 marks 的闭包分开；没有偷保原W/I或 all-λ强型。

## 4. Exact方向 local entropy 与旧 weighted FSD 应用

exact轴给 P_d(v)=0。P_d非零齐次，有限固定 stereographic紧charts中所得 numerator为非零 degree≤2D多项式：若它在某开chart恒零，P_d在球面开集恒零，再由齐次性／多项式恒等性推出P_d=0，矛盾。charts正反 Lipschitz常数统一。

Wongkew Main Theorem 对 R4中 degree有界零集、半径Cr球及厚Cδ给 Σ_(j≥1) C_Dδ^j r^(4−j)≤C_Dδr³（δ≤r）；奇点或更高codimension只使该 upper更强。对一个原 r角帽，其在某固定chart中的δ分离 centers 落Cr球，互不交的小4球含于该代数零集的 Cδ-neighborhood。体积比较给≤C_D(r/δ)^3 centers，故角帽 cover数亦如此。这个是每中心、每δ≤r≤1的local entropy，不是总N≤δ^-3，也不需 leading系数或梯度 floor。原权于是有 C_Dα(r/δ)^3 的3-KT upper。

独立核 root 的保守λ³ Lebesgue回传：先细角bins有限着色，按 w_i/(Cα)抽每bin至多一个原label；所有样本的方向都仍在上述Σ且δ分离，所以确定满足 uniform K_D的s3 cap，而不只期望cap。共同δ随机格使每label有≥cλ/δ真实点的概率≥cλ，rich原样本用已有 FSD的λ²有限计数下界。期望 rich数≥cλW/α，E#(E∩grid)=δ^-5|E|，遂得保守 δ^(4+σ)λ³W/[αlog(2/δ)]。finite slots／clock/cells只固定常数，未以 NδE 代真实体积；η在 source门槛后足小便得 exact版G4。

这条链准确属于旧 FSD001统一输入再调用，无新增ID或新主机制。它不能用于 metric-near输入，因为原方向未必在该Σ的任何小邻域；下一节的近平面例甚至使距离固定非零。

## 5. 几何查询边界、两桥反例与HRZ实际范围

same-π图形的有限majority、whole T和Y同时保常数、normalfiber≤Cδ、非短投影可依R60的同一证明用于物理dim4，uniform于δ系数。root正确保留实际 projected角帽 A_j；带它的 δ^(4+ε′)λ³W_j/A_j 不是原α版本。原KR可对 H_j∩π^-1U 使用原管常数体积证据，故对固定格式半代数U的 whole S_i⊂U 得 Σw_i≤Cασδ^-3-σ|U|；凸U用John盒付格式。这既不允许 U 的复杂度随管数增长，也不是 projected global angularcap。partial U可能只见不同clock段，好图质量可全在其外，不能据 whole证据授 full fraction-PW4；若用实际短段marks须重付原fraction／a^-5等费用。

McShane延拓模块在真已给投影whole近3fold时可调用旧G3／marked-only nearfull，但当前没有完整递归证明足够原W/I落入这些原单位clock子族。没有把 conditional低维集中变成已提取质量；也没有以任意4D CW/PW4定理填最后缺口。

两例独核通过且不反G4。x5²−δ^A x1 归一后实不可约、Sing空，水平原轴距零集 O(δ^(A/2))，最近零点梯度同阶；任意固定δ^c梯度floor可被A大否定。x5−δ^A|x′|² 归一后physical梯度良好，却t²系数迫任何exactline为常点；S3水平δ-net的原N≈δ^-3、capO1、full marks、真实union≈δ均合法。其 leadingzero只有±e5，horizontal原方向距之固定远；因此原exact-Fano／原leadingzero snap桥失败。允许换低degree近似未被排除，而相应原质量／尺度未付。原marks集中到λclock时实际δλ⁴只要求η在ε后小，不推∃η的G4失败。

HRZ再读范围支持 root的限定：Prop4.2的缩放(27)和 e(p,n,k)=(n−k+1)p−(n−k+2)在n5、k≥3保留至少4/3的旧窄阈值，不能由换一个terminal自动授p<4/3。§8使用tiny raw norm和(51)–(53)/nested maxcount，nearfull G4不是全λ sharp强L4/3，也不消ρ归一、原cap/PW和parent重复费用。没有据此宣称一切HRZ变体皆不可能或新的ordinary上限。

## 6. 最终限定通过、全G4未解与停止

当前root8/B10的原质量归约、exact旧输入闭包、specific桥反例及停止结论经独立逐步审查通过，无未解决强制项。A自己的主文不算自身独审，其实际主链由root/B承担交叉核；本文未用自身结论替代独立检查。高级具名wholeproof未在本轮新完整独证，未经外部同行评审；未认证未来meta、Git、字节或同步。

终macro6/next6已实际全文核：full near-contained G4仍未证、未否，余责是退化不可约4维类中真实位置—方向联合恢复／可相加原质量，而不是把不可约重新命名再续一轮。停止这次generic physical graph/CW4接法，不续低degree／κ／λ／D或又一quadric模板，也不拿resolution/desired cap公设结案。exact、factor及反例均没有变成 ordinary新界或major，streak10保守计时不清零。

完整ordinary/general、direct HRZ、sticky全κ及ordinary桥、同一full-direction低维构造四路仍开放；当前没有qualified新gain。困难不使Goal完成、降格或blocked。flat反向只表明G4若完成至少包含已有DIR强度，不能反过来假G4已是旧DIR自动后果。终审只认可上述有限范围事实，不预定下轮命题或成果。
