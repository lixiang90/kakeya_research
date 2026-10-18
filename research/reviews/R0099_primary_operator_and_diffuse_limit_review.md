# R0099：原算子、整线段与弥散弱极限的独立终审

2026-10-19，A。本审稿只认可下列实际读取和逐式核查的有限来源应用；未经外部同行评审。

## 1. 实际全文对象及独立审查分工

已 fresh 实际全文读 root 主稿 notes/40_multiscale/R0099_concentration_wholeclock_and_known_determinant_gate.md（12节）、A 主稿 notes/00_map/R0099_concentration_primary_and_operator_gate.md（12节）、B 主稿 notes/00_map/R0099_concentration_geometry_and_counteraudit.md（12节）、reselection／working spec 各5节，以及终 macro、next、source-scope、round 各6节。root §9 的内部 BV／零延拓修订和 §11 新增同 ambient PSD barrier 比较已读回；A §11 的实际 FT 读域与 §12 cross 已收尾，仍12节。

本人 A 主证不是自身独审，正证另由 root／B 实际全文核查；本审稿的独立对象是 root 的整合证明和 B 的另一条 CV、equator、ribbon 链。采用来源的实际读域为 GR v2 完整 §1 定义／主声明、相关 §2／§3／§4 证明接口和 Appendix A；FT v2 Th1.1、§2.1、完整 Prop3.4／Cor3.5 及缩放证明、Th4.1 与主定理应用证明；库存 CV v1 intro、完整 Theorem1 和 affine-form footnote。新 GR 热流／Young-measure 表征、旧 CV 端点高级证明及全部外部 wholeproof 仍具名，不冒已逐页独立重证。source-scope §1／3 的最后日期修订亦已实际读回：GR history／HTML／侧栏为 Sep11、PDF 正文为 Sep14；FT 前者为 Sep9、PDF 正文为 Sep10，两日期不冒一致。root 的 PDF 字节／图页记录不当作本人的新视觉或档案校验。

## 2. 原 wholeclock、算子条件及真正浓集资格

独核 root §§1–4、B §3：对 Sym_n 上 row-Div，符号为 A(ξ)M=Mξ。单位 ξ 和任意 b 对应 symmetric 矩阵 b⊗ξ+ξ⊗b−(b·ξ)ξ⊗ξ，确送 ξ 到 b，故 rank 恒 n；wave cone 为 singular symmetric matrices，rank-one vvᵀ 张成 Sym_n，实际满足 GR1.7 的 constant-rank／spanning。PSD 是取值 cone，不是另一个线性值空间；它包含 wave cone 中的非零 rank-one PSD 矩阵，故与 wave cone 非零相交，不能免费使用 GR1.9 的避锥假设。

真实单位段 stress 的 row-Div 是向量端点 Σw_i v_i(δ_a−δ_(a+v))，TV≤2W。PSD 给 tr/√n≤Frobenius≤tr，W=1 时 cδ∈[1/√n,1]。全 Cδ 轴邻域体积趋零使场趋零于 measure；端点另由 Nδδ^n→0 付 RHS 的趋零，N≤Kδ^(1−n) 时须实际有 Kδ→0。共同大 Lipschitz cube 内部紧支撑付极限边界零。Rem1.5 真实容许一致 L¹ 且趋零于 measure 的非零 RHS，未把原序列伪称 exact A-free；仅负 Sobolev precompact 不能替代这两项。

root §9 已明确 h∈BV(0,1) 时 D_t 只指内部导数，端点取单侧 trace；若用零延拓 D_t(h1_[0,1])，端点已计入。一般可测 mask 无端点 trace／BV 保证。一轴 m 个区间给 TV 2m，长度 λ 的单区间归一后给 2/λ；平均或逐管 density 都不控制这一项。root 的修订消除了重复端点和对任意可测 h 取端值的歧义，无未解决强制项。

## 3. GR 的新旧边界及固定 null 排重

独核 root §§2、5–6 与 B §§2、4–5。GR1.6 约束 Choquet 组件的 barycenter 属于 wave cone，不是一般 μ 的每个值或其总 barycenter 属于 wave cone。GR1.7 的新 generators 也不是原 tube restriction。PSD 场的额外结论须用正性：μ 由 PSD 单位矩阵承载，故几乎所有组件 ν 亦然；其 singular PSD barycenter B 有 kernel vector e，0=∫eᵀAe dν 迫 Ae=0 ν-a.e.，于是 μ 支持 singular PSD。e 可逐组件变化，不能据此恢复同一物理 plane 或同一 wholeclock 子族。

固定 null stress 的正核卷积和端点卷积由 Lebesgue differentiation 趋零，strict variation 收敛及 Reshetnyak 给实际 law 等于原 polar 的推前。旧 finite-Div DPR 已给该 polar 在 wave cone。Dirac δ_A 的 exact generator 也确可付：Ae=0，沿 e 的正集中条纹或穿域内部的窄 slab，Div(Af)=0、L¹归一、趋零于 measure，弱极限无边界质量，值方向恒 A。穿域超平面在边界的交集低一维，不产生边界质量。

因此只对这个固定 null 应用，新存在分解已属旧闭包；不能将整篇新 GR 归约成旧 DPR。varying 序列可有 ac 弱极限正是其真实新 scope，下节给原整线段实现。组件的值空间共同 kernel 及任意新生成场，不赠原位置—角度—时钟联合 restriction。

## 4. 有限平移的真整线段序列与满秩弱极限

root §10 和 A §§8–10 的来源／量词已逐步核对。采用已有经典 compact planar null Kakeya P，K₀=P×cube³：每 v∈S⁴ 的平面速度长度≤1，可用 P 内单位段的相应初始子段，其余 cube 坐标在同一个 t∈[0,1] 线性移动，确有原方向整单位段。P 的 Hausdorff 维数2与 cube product 给 dim_H K₀=5；它不是 strict 低维反例。可测 selector 只用于定义 occupation，不要求连续。

S₀ 的 trace mass1、总矩 I/5、端点 TV≤2。大 cube C 上有限等权平移网格 law τ_j 趋向 1_C/|C|；S_j=S₀*τ_j 仍由 copy×v×t 的真实段积分组成，每个 j 的 carrier 是有限 null compact 平移并，物理方向边际仍为 σ。其弱极限为 F dx，F(x)=|C|⁻¹∫1_C(x−y)dS₀(y)。common core 中所有 x−y∈C，故 F=I/(5|C|)，真正 full rank，core 散度0。

逐 j 选 ε_j 使 carrier 的 3ε_j 邻域体积<1/j，原场与端点卷积都在其中；c_j∈[1/√5,1] 取收敛子列，u_j 和 Divu_j 均趋零于 measure，RHS L¹≤2√5。统一测试的 modulus of continuity 给 mollify 不改弱极限，u_j⇀F dx/c；共同大 cube 付边界零。Θ 的 barycenter 为 I/(5c) 满秩，而其 PSD 值分布仍 singular，和 GR 不矛盾。

B §8 的精确校准亦正确：先均匀选 e，再在 e⊥ 的单位球均匀选 v，混合后 v 边际恰为 σ，每组件矩为 (I−eeᵀ)/4，总矩 I/5。equator 在 σ 中零测，不能称原保正质量删选。上述平移模型保 weighted copies／真实全角／整段，未保 unweighted one-per-direction 同 δ 参数或 power footprint 亏损；每 carrier 本来满 Hausdorff 维数，不能冒原 Kakeya 反例。

## 5. 旧 CV 的更强有限输出与 FT 的精确范围

独立核 root §§7–8、11 与 B §§6–10。Cauchy–Binet 的 ordered tuple 系数 1/n! 正确，det(v_tuple)²≤|det(v_tuple)|；CV 任意方向、非负权的 n 个 family 可全取同一族，重复 label 项为零。k_i≤Cδ^(1−n)1_(无限Cδ管)，取 1/(n−1) 后外部 δ⁻ⁿ 与 CV 缩放 δⁿ 恰消，给 ∫det(M)^(1/(n−1))≤C W^(n/(n−1))。从而自身 ε-broad trace 的 L^{n/(n−1)} 范数≤Cε⁻¹W，E 上质量≤Cε⁻¹W|E|^(1/n)。

任意真实 Lebesgue marks 取 M^Y=Σw_i1_Yi k_i vvᵀ，PSD 序给 det M^Y≤det M；marked-broad 不必包含于 whole-broad，正文保留了自身 broad。核支持 B₃δ、在 B₂δ 下界保证整个圆帽管上 k_i≥cδ^(1−n)，故 ∫trM^Y≍δ^(1−n)Σw_i|Y_i|，平均／逐管 λ 都按原真实质量支付，无删帽或 shaded BV 假设。restriction 保上界 W，却不自动保归一后的 λ／全角 law，正文未偷渡这些闭包。

FT Prop3.4／Cor3.5 是一般 matrix-measure 出口，不能以 rectifiability 粗拒；其正 Φ 下界和真实 carrier 仍须付。对同 ambient PSD 场，源 barrier 有限、连续、concave、一次齐次，双向 superadditivity 给 global Lipschitz；M−λ_min(M)I 奇异，故 φ₊(M)≤L√n λ_min(M)≤L√n det(M)^(1/n)。CV 随即给相同 p=n/(n−1) 的 Lp 和 E 上 |E|^(1/n) 上界，M^Y 亦然。只排重此实际 PSD 应用，不否任意 matrix measure 或投影后的其他工具。

B 的 rectifiable ribbon 面积 (2δ)^(m−1)、boundary variation 2(2δ)^(m−1)+2(m−1)(2δ)^(m−2) 正确，ratio 为 2+(m−1)/δ；不能从原两个 clock 端点免费取得 m-sheet first variation。FT Th4.1 的 spectral positivity、rectifiability 和低维投影 carrier 仍为真实输入，未冒已付。

## 6. 终判、宏观范围和停止

限定范围内全文通过，无未解决 mandatory。实际核过的修改包括 root §9 的内部 BV／零延拓端点约定、root §11 同 ambient barrier 旧覆盖，以及 A 的实际 FT 读域和真实 cross 记录。本审 §2 曾误写 PSD 包含整个 wave cone，已按 root 指出修为仅与其非零相交（rank-one PSD 在其中）；Λ 另含 signed／indefinite singular 矩阵，未改变原数学主链。自己 A 的施工不计自独审，root／B 的实际全文独核分工保留。

终 macro／next／source／round 各6节已全文读：新 GR 序列定理和真实满秩 ac 弱极限的 scope 被承认；固定 null 的旧闭包、finite determinant 更强覆盖和未付原同管／跨fiber／ambient 出口明确区分。ordinary／HRZ、完整 rough sticky 及 ordinary 桥、真 full-direction 严格低维四路仍 open；没有 qualified next gain，不以 cone、moment、operator 或 ribbon 参数延长该直接桥。streak22 仅计未获 ordinary／完整 branch-saving，不否认本轮来源和反攻信息。

本审仅认可有限来源应用、已知估计比较和明确校准，不是新 result ID、major、ordinary 增益或全部 PDE 方法 no-go。未新认证外部高级 wholeproof，未经外部同行评审；不预认证未来 metadata、Git、同步或最终档案计数。Goal 保持 active。
