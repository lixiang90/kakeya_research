# R0087：全 G4 的奇异近轴转移尝试与真实停止接口

2026-10-18，A。唯一主任务为全部 fixed-degree、δ-dependent metric-near hypersurfaces；目前未证、未反全 G4。以下区分全类可付的几何、旧统一输入的再调用、具体免费桥反例与真正未付的 joint 接口，不以 proper 子类结案，不新增数学 ID／重大性声明，未经外部同行评审。

## 1. 完整原命题、删选与本轮反攻

已实际读 R87 working_spec5、GOAL、STATE、R86 next6 和 R85 root10；复用同会话 ROADMAP 全部冻结与 registry78 的恢复，未重跑过去通过的计算。本命题固定 D,R,C,C0，对每 ε>0 须存在 η,c,δ0，使每个非零实 Pδ、degree≤D、系数ℓ1归一为1，以及原 R5 unit round δ-tubes T_i=Nδℓ_i、whole ℓ_i⊂B_R∩N_(Cδ)Z(Pδ)，在原非负权和 W>0、每物理无向 C0δ帽原权≤α、原 measurable Y_i⊂T_i 且 |Y_i|≥δ^η|T_i| 时满足

    |E|=|∪Y_i|≥c δ^(4+ε) W/α。                           (G4)

所有常数必须独立于 Pδ 的条件数、δ、W、权跨度及原族。无 leading/physical 梯度 lower、exact containment、无奇点、ADlower 或额外 PW4 输入。非零 constant P 没有合法非空 near-axis 族；其它情形不先删成 regular。

whole-label restriction 保原 P、whole-axis metric 条件及未归一 α，但只保实际剩余 W/I。任意裁 marks 须重算 density。若逐管 G4 在 ε/2 下真成立，平均 λ≥δ^η_av 时 heavy 到 density≥λ/2 可保 W′≥λW/2；先 η_av≪η_per、η_av<ε/2，再吸此真实 λ 损，才能得平均版。逐管和平均不直接互换。flat P=x5 以原4D marks乘 normal δ区间反推 DIR4，所以成功 G4 也只是既有输入的几何应用，不会独立证明 ordinary 新界。

预设反攻涵盖 repeated/irreducible 因子、空 singular locus 却任小绝对梯度、δ依赖近平面、exact Fano 空集、bad-clock 集中的原 marks、端帽、近多个因子的 clock 切换、投影角帽和 partial query。一个具体桥失败不等于 G4 refuted；若最终只能复述 regular／resolution 公设，按 spec 停止，不把困难记 external block。

## 2. 实际 source 范围与可复用输入

本轮实际重读 R60 root §§5–9、11–12 的 majority／same-π图形／whole-volume和原权接口，R59 root §§3–5 的全局 Lipschitz 图、RCF uniform格式与 normal-fiber 测试；R85 root10已全文读。又实际读 FSD001 reviewed页和 R29 A 全文 §§1–8，确认其是任意 fixed ambient、全部中心和δ≤r≤1的 angular cap K(r/δ)^s、任意原条数／原marks输入，不是仅总 N≤δ^-s。已实际全文读本轮 B《R0087_full_G4_original_mass_counteraudit》10节，并逐式核其 factor 尺度和两桥反攻。

以下半代数 smooth stratification、CAD/QE、Pawłucki regular-cell／全局 Lip 分解、固定格式 uniform界、KR polynomial counting 和 DIR003 继续列为实际具名输入；未新独证其完整高级 proof。R60 对 dim≤3 的 M3 出口已经付，不能改个维数就称四维 full indexed 定理也有。R38 assembly、R80 retained core、R61/62 PW4 闭包、R84 factoring 和旧 parabolic 模板均不重报新结果。

## 3. 对全部近轴类确可付的 same-π 图形与实际阴影

令 S=Z(P)∩B_(R+2)，real dimension≤4、格式只依 D。R60 的有限大多数投影构造可原样用于 R5→R4：Haar 投影在每个≤4维 tangent plane 上几乎处处 injective，紧性和有限采样给固定有限 π_j、τ>0，对每个此类平面至少1−e比例的 j 有 smin≥τ。它不依 P 的系数条件数或δ。

对每 j，仅取其 good tangent strata；在同一个 π_j 下，CAD／目标minor／Paw regularcells和 lower-dimensional 递降给固定数 global Lip graphs闭包，Lip常数及格式统一。H_j 为这些闭包的固定 Cδ-neighborhood并。每条 π_j-normal fiber 的长度≤C_Dδ。点wise每个 near-S 点属于≥1−e比例 H_j，无须可测 nearest-point selector。

分别在每个真实 T_i 和 Y_i 上积分该点wise计数，Markov 可选同一 j(i) 使

    |T_i∩H_j(i)|≥|T_i|/2， |Y_i∩H_j(i)|≥|Y_i|/2。        (1)

这里是同π有限图的 union，不假整管在一张图上。由 normal fiber upper，

    |T_i∩H_j|≤Cδ |π_jT_i|≤Cδ⁴(|π_jv_i|+δ)，

故 (1) 迫非短 |π_jv_i|≥c>0，端帽已包含于 δ 项。原 labels 按有限 j／方向 charts 分组，全部实际权和按组重计；不动原点，不填 marks。

在每组设 E_j=E∩H_j，f_j=δ^-1∫_(kerπ_j)1_Ej，则0≤f_j≤C、每个固定长 projected envelope P_i 的平均 f_j≥cλ。阈值 F_j={f_j≥c′λ} 给真实 |F_j∩P_i|≥cλδ³。若令 A_j 为这组实际 projected δ角帽权的 supremum，则 R85 的真实共同随机格／DIR 桥确给

    |E_j|≥c δ^(4+ε′) λ³ W_j/A_j。                        (2)

(2) 只是带实际 A_j 的结论，尚不是 G4；没有在符号里把 A_j 换成原 α。全局的粗 bound 只有 A_j≤Cαδ^-1，因为非短区间上一个 projected δ帽的原方向逆像可含一维 O(1) 长 fiber。δ^-1 是固定幂损失，不能并进 ε。near-axis 多项式兼容性是否能去掉这个真实重数，是当前没有支付的一步。

## 4. 原 PW 真能给的查询与递归正模块的限度

固定一个 projected envelope P_i⊂凸 U。由 (1)，H_j∩π_j^-1(U) 含原 T_i 的常数体积比例。用 John 外接 box Q_U，测试集

    H=H_j∩π_j^-1(Q_U)， |H|≤Cδ|U|

具有固定格式。KR 对原 direction-separated samples 的固定比例查询，及按原方向bins以 w_i/(Cα)概率抽原 labels 的线性期望，严格给

    Σ_(P_i⊂U) w_i≤C_σ α δ^(−3−σ)|U|。                  (3)

这保了 projected 位置和重复 indices，没有 λ^-5，因为查询的是原 whole T 的常数证据。但 (3) 是 whole-containment convex 查询，不是 projected angular cap，也不是一项已证的四维 indexed full-CW/全体积定理。一般 partial U 只截 P_i 的一段 clock，T_i∩H_j 的好体积可能在该段之外，不能由 (1) 给同样比例。若改用实际 marks 的该段作证，则必须保其真实 fraction；原 n5 PW 的 a^-5 费用和新 clock/marks 门槛均不能省。

可另实际核一个递归模块，但不足收全 G4。对同π的一个 global L-Lip graph f:D→R，McShane函数 ftilde(x)=inf_(y∈D)(f(y)+L|x−y|) 是同值 L-Lip extension，QE给固定格式。若原 projected axes 整段近 fixed-format Z⊂R4、dim≤3，则 graph(ftilde|Z) 也固定格式、dim≤3。原在该图邻域的 marks，因 projected 距 Z 为 Oδ，真近这个3fold。有限同π图并同理；R59 marked-only nearfull或真正 whole-axis 情形的R60可处理这批原 marks，保原α和固定次数格式。

然而当前没有完整 polynomial-partition 分解保证足够原 W/I 落于这些**原单位clock**子族。局部 r段需真实缩放，coarse帽原权可增 r^-4；partial intersection 未必保好图；把“所有 tangential pieces 可接G3”直接当全管结论正是旧尺度费用。故此模块不赠 all-scale algebraic nonconcentration，更不能以一般 CW4 的目标公设填 (2) 的 A_j。

## 5. Exact 与 factor reductions：已知正面范围，非主目标完成

若 axes exact-contained于 Z(P)，则 P_d(v)=0。非零齐次 P_d 的 S4零集是固定格式、dim≤3，奇点和δ系数均不改变这一维数陈述。uniform global Lip pieces使其与任意 r角帽相交部分可由 C_D(r/δ)^3 个 δ帽覆盖，故原角权有真正所有中心／所有尺度的3-KT upper C_Dα(r/δ)^3。原 FSD001 s3、任意 ambient／条数及共同随机格真Leb桥可得 nearfull G4 exact版；固定 λ幂和log由η最后小吸收。这是旧 FSD 的直接统一再调用，不另搭 majority proof或登记新结果。metric-near 不能自动换成该 exact directioncone。

对一般 P 的 factor reduction，B 的全时原质量证明通过。写 P=c∏Q_j^m_j，忽略无实零点因子；每轴的 B_ij={t:dist(a_i+tv_i,Z(Q_j))≤Cδ} 有统一有限一维分量，覆盖原clock。不能按 label 免费选 whole factor。先去球端帽 Oδ体积，用所有边界分配 clock 后，从每 label 取一条 assigned interval保≥cλδ⁴ marks，其长度≥cλ。长度 ℓ∈[r,2r) 可由原 interval 内两条完整长 r子段覆盖，择一保常数 marks。

r≥cλ，只有 O(log(2/λ)) 层。取一层保 W/log；再按片中点的 r格和因子分组，所有真实 E_g 位于有固定 overlap 的 C′r球，故 Σ|E_g|≤C|E|，没有格数 r^-5。r归一后 h=δ/r，原方向不变但新帽

    α_h≤Cαr^-4， density≥cλ/r≥cλ。

若不可约全类真在 ε′成立，回传为 δ^(4+ε′)r^(5−ε′)W_g/α，r≥δ^η和log可由η最后小吸收；h≤Cδ^(1−η)也允许选η小于被调用门槛。这严格把全部 P 缩到实不可约；real dimension≤3的因子由旧 G3处理，degree1由flat DIR处理。余下实不可约 dim4、任意δ退化近轴并未被这些旧正面闭包证明。

## 6. 两个完整量词的桥反例及其实际原质量

B 的两例已独算，均不是 G4反例。第一，e=δ^A、A>2，Pδ=(x5²−e x1)/(1+e) 实不可约且 ∂1P恒非零，Sing为空。取 x1∈[1,2] 的原 unit轴，其距零集≤√(2e)≪δ；最近零点的梯度 O(√e)，轴上梯度 O(e)。对任意预设 c，选 A>2c 可使其小于δ^c；所以 norm1／远离Sing不授绝对梯度下界。这不反 normalized normal／真实图形的方法。P=x5^D 也提醒 polynomial-small |P|≤δ只给 δ^(1/D) 厚度，不能代 metric δ假设。

第二，e=δ^A、A>1，Pδ=(x5−eΣ_(j≤4)xj²)/(1+4e) 是不可约严格凸图、physical ∂5P≥1/2。任何 exact affine line的t²系数迫 v_h=0，再t系数迫v5=0，故原 Pδ 中根本无非平凡 exactline。然而所有 horizontal unitaxes tv_h 的距曲面≤e/4≪δ；取 S3 的δ-net有 N≈δ^-3、原capO(1)、fullmarks。tube union真≈δ：上界在固定B4×[−δ,δ]，下界由方向稠密性得到 B4_c×[−cδ,cδ]。这严格否“nearaxes→原同一P的exact Fano线”的桥，任何δ^c精度也无对象可选；不排允许更换低degree近似面、并支付其实际质量／尺度的正确方法。

同一族把marks限制在中心clock λ长时，λ≫δ下实际union≈δλ⁴，而逐管density≈λ。这说明 η 必须在 ε 后小；若误称 η任意给定，取4η>ε就失败，但 G4 的∃η量词允许更小η。此反攻不能升级G4 refuted。跨两因子的轴、indefinite中间slope与端帽也均须按 §5真clock收费，不给固定坐标 Oδ捷径。

## 7. 主机制实际卡点与未付量词

全类 majority／图形部分统一处理 physical singular strata 和δ系数，却没有把原 whole-axis 信息变成 projected全局 angularcap。单次非短投影、pointwise tangent／normal条件、全部N≤Cαδ^-3，均不等于所有r帽的3-KT。旧parabolic近轴族在r≥√δ的某些帽内约r²δ^-3，足以排把全N记成r³上界的shortcut；这只是旧校准的真实用途，不另计数学反例。

同样，(3) 的 convex wholecontainment只能得到已经付的强度；不能调用不存在的一般4D full indexed-CW bound。若期望由 polynomial graph 的额外兼容性改进，则必须在同一原 family 上实际证明如下类型的联合预算：保每组实际 marks、原α、非短clock、normalfiber和 projected角重数，且多组实体体积可控相加。此处只是指出缺的估计，不把它作为新增原假设、resolution theorem或已提取的分解。

若 fiber 只≤L≥δ、帽只≤αδ^-b，则 θ≈λδ/L；就算另外支付 DIR门槛，R85桥也仅给 δ^(4+ε′)λ³(δ/L)²δ^b W/α。固定幂的fiber／帽损失会留下固定维数损失，不是δ^o(1)。特别是 θ 本身可能已小于 source nearfull门槛。允许空间packet后求和也必须真实支付 bounded overlap／原label质量；本稿没有证明这种全类分解，也不以一个global失败反全部packet方法。

因此本轮完整 G4 仍未证未反；严格剩余接口是 δ-near、实不可约 realdim4 情形的 position–direction联合恢复与可相加原质量，而非又一个 regular分支、given cap 或 exact FSD应用。没有把阶数／κ／δ阈值优化、旧PW4改名或‘假设resolution有原mass’当主结果。

## 8. 当前交叉范围与停止

已实际全文读 B10，逐式独核其 factor时间分配、长度r／空间包、α_h与r^(5−ε′)、h门槛、低real-dim调用，以及两桥例和真实 marks 校准；无必须修正的数学问题。B自证不以其自审计为独审。root 的完整 downstream／整合稿尚待实际落盘后全文读回；本稿不预填其通过，正式审另待明确授权。

按 preset 停止 G4 这一 generic projection／所需joint预算门，不把未解决记refuted、blocked或Goal完成；也不沿 irreducible、D/λ/κ、小模型继续一轮。whole-class目标没有被成功公设或proper子类替换。完整 ordinary、高维一般、sticky余case和真实full-direction构造继续开放。本轮不新增 ID／ordinary gain／major，具名高级proof和本文自证接口分开，未经外部同行评审；不认证未来metadata、Git或同步。
