# R0085：方向恢复、实体阴影与既有有限输入的独立审查

2026-10-18，A。本文只审实际写出的 regular-leading 转移 certificate 及本轮输入资格结论。结论为所列条件下内部审查通过，无未解决强制项；没有 ordinary 新界、全 G4、新数学 ID 或重大性声明，未经外部同行评审。

## 1. 实际全文范围、分工和依赖等级

已实际全文读当前 root《R0085_regular_leading_hypersurface_transfer_certificate》10节、A《R0085_dimensional_recurrence_and_source_qualification》8节、B《R0085_midpoint_support_and_actual_construction_input_gate》8节、working_spec5及其末尾精确 certificate 补锁、终 macro6 和 next6。最后又读回 root §7 的 θ² 格桥、§9 的 N≈δ^-3 实体校准，以及 A/B 追加候选的全部段落。A/B 中“尚未锁候选”的句子保留阶段 I 的写作历史；本审查以随后实际补锁的 root10/spec 作为当前准确命题，不把旧资格文字当成已证明全 G4。

A 参与了同坐标 Euler／Remez／纤维接口的独立施工；自己的 A8 不能替代自身独立审查。root、B 已实际全文逐步核过 A8。本文独立复核 root 的完整整合、其更精确的 θ² 格桥和抛物校准，以及 B 的 FY 原输入／平均密度资格判断。不能将这些内部互审称为外部同行评审。

具名 DIR003 是实际使用的四维 finite near-full 方向／marks 输入，完整高级来源 proof 未在本轮重新独证。DIM001 的已付 RED/SRC/DIR/FSD 内部 assembly、具名 KT6.2 及任意集合 Hausdorff 桥沿用其真实审查等级；M3 全函数定理也仍为具名输入。本轮实际 source 读域以 A8/B8 明列的 KT §5–6、M3 的定理／应用段、OAI4 §11、FY v2 相关陈述与证明段及有限 primary 比对为限，不冒全文独证所有高级论文，也不认证尚未结束的 FY 下载或未来文献字节记录。

## 2. Whole clock、五组投影和近零方向恢复

root 的原对象是固定 D,R,C,κ>0、真实 degree d≤D、系数和≤1 的 P，可随 δ 变化；整 unit 轴在 B_R∩N_(Cδ)Z(P)，每个原 label 额外满足 |∇P_d(v)|≥κ。原非负权、重复 indices、物理无向 C0δ 角帽权 α 和原真实 Y 均被明确保留。这项 leading 梯度下界不是 physical regularity 的推论。

whole-axis 假设及固定导数上界先给 |P(a+tv)|≤Aδ；固定 d+1 节点的插值确给 |P_d(v)|≤A_Dδ。选 |∂jP_d(v)|≥κ/√5 后，Euler 恒等式及梯度 upper 迫 |π_jv|≥cκ：若 v 近 ±e_j，内积的该主坐标不能被其它坐标抵消到 O(δ)。因此只有五个 whole-label 组，同一 j 同时承担非短方向和后续物理导数，未另行选择互不兼容的 kernels。

写 v=r(u+s e_j)，r=|π_jv|，则 s 有固定界，齐次性给 P_d(u+s e_j)=O_κ(δ)，其 s 导数有固定 κ 下界。在同一 projected δ 帽内，换成固定 u0 的误差是 O_κ(δ)。将一元多项式按 p′=±cκ、p=±A_κδ 分成固定多个单调区间后，每个好区间宽 O_κ(δ)。这是对近零集合而非 exact roots 的恢复，故只需要固定多个原 O_κδ 角帽，付固定覆盖常数后其原权为 C_D,κ α。无向方向的有限定向 charts 只改常数，没有免费 projected δ 分离或去重。原 κ 固定是必要量词；不能证明后再令其任意依 δ 衰减。

## 3. 同坐标 sublevel、实体端帽与实际纤维

对实际选定 j，h(t)=∂jP(a+tv) 的 t^(d−1) 系数恰为 ∂jP_d(v)。d≥2 时，从 |h|≤2τ 的集合选择 d 个按其长度分离的分位点，最高系数插值给 bad clock 长度≤C(τ/κ)^(1/(d−1))。取 τ=c_D,R,κ λ^(d−1) 可使其少于固定小倍 λ；d=1 是非零常导数，须且已单列。这里不需要原 shading 在 clock 上逐点均匀。

两个 round 端帽共只有 O(δu_δ) 真实体积，因 λ≥δ^η、η<1 才可先删；不能用端点 measure0 解释。body 用未 clamp 的正交轴 clock 和截面体积 upper 积分，删除 bad clock 至多 Cb u_δ。固定 C2 upper 使轴到实体点的导数误差 O(δ)，由 δ≪τ 吸收。故每条实际 Y′ 仍有 cλu_δ，并满足 |P|≤Aδ、|∂jP|≥τ。η(d−1)<1 和 δ 最后足小同时付这些要求，没有隐含独立角度或额外 regularity。

沿同一 kernel，一元 P(z+t e_j) 在 |P|≤Aδ、|P′|≥τ 的真实点集只有固定多个单调分支，总纤维长度≤C_Dδ/τ。于是 f=(τ/δ)∫1_Ej 的上界是固定常数。非短投影允许以固定长、固定倍宽的 S_i 包住原投影；只延长 supports，不添加 marks。Fubini 给 ∫_(S_i)f≳τλδ³，取 F={f≥cτλ} 后每 S_i 内实际 F 的 Lebesgue 质量≥cτλδ³。令 θ≈τλ≈λ^d，不能把这个真实 F 改成占格的 δ-neighborhood。

## 4. θ² 共同随机格桥、回拉和两种密度闭包

独立核过 root §7 的较强桥。令 h=C_κδ，使用所有 labels 共同的随机格 G_ζ。对每 i，X_i=#(F∩S_i∩G_ζ)≤C/h，且 EX_i=h^-4|F∩S_i|≥cθ/h。因此事件 X_i≥c′θ/h 的概率≥c″θ。这个单变量截断足以给 E W_rich≥cθW_j，不需要不同 i 的独立性，也不引入 weight-span 损失。

在每个 rich index 的有限 graph/clock charts 内，每个 clock 层点数 O(1)；固定 slot 选择只损常数。真实格点到支持线 marks 的移动为 O(h)，其 occupied source cells 至多是原格点的固定邻格数。η 先依 DIR 门槛足小，保证 θ≥h^(η_src/2)，所以 rich lines 的 θ/h marks 满足该 near-full 输入。应用 DIR 的线性边数形式得到

    #(F∩G_ζ) ≥ c θ h^(σ−1) W_rich(ζ)/α。

再用准确恒等式 E#(F∩G_ζ)=h^-4|F|，即得 |F|≥cδ^(3+σ)θ²W_j/α。两次 θ 分别来自 rich line 的实际 marks 和 rich 原权的期望；没有第三次 θ。B 阶段 I 经 FSD 写的更保守固定次幂损失不否这个较强版本。可测零集的代表不影响共同随机格的期望恒等式，有限 charts、固定 homothety 和 clock padding 不依 δ 变大。

回原物理体积为 |E_j|=(δ/τ)∫f≥cδλ|F|，故得 δ^(4+σ)λ(τλ)²W_j/α≥cδ^(4+σ)λ^(2D+1)W_j/α。五组满足 ΣW_j=W、Σ|E_j|≤5|E|。平均 λ 的版本先整 label 删除 density<λ/2 者，保 W1≥λW/2，帽的未归一原 α 继承，再多付一次 λ；不能仍写原 W 全保。整 label restriction 保 P/κ/α，进一步裁 shading 必须重算 density。σ→η_src→η→δ 的选择次序明确；显式 λ 幂不等于已经取得全 λ 同常数的四维 maximal。

## 5. 原实体校准、其它输入与反攻结果

独立核 root §9：固定倍归一 P=x5−x1² 后 physical 梯度有固定 lower。a 的 L√δ 格、r 的 Lδ 格于 [τ0√δ,2τ0√δ]、b,c′ 的 Lδ 格给 N≈δ^-3；所写 v 的范数恰为1且 v4 有固定 lower，P(A+tv)=−t²r²，故是整单位轴的真实 N_Cδ 例。不同 r/b/c′ 由其自身坐标分离；只变 a 时 v5 差≥2τ0Lδ，选 L 大给固定原角帽 O(1) labels。所有 leading 梯度仅≈√δ，不能提取任何 fixed-κ 子族。

union 上界来自固定图的 O(δ) 邻域。下界不是仅 count axes：固定 x4=s∈[1/8,1/4]，同 a 的 (r,b,c′)/v4 有所写 uniform Lipschitz 逆；异 a 组的 x1 间隔 L√δ，运动仅 O(τ0√δ)。故切片中心 δ 分离，仍在实际轴的固定内段；每个真实 tube 的该截面含 cδ 四维球。积分给 |E|≳Nδ4≈δ。此例只拒“physical regular 免费给 leading regular”，是 R53/R55 旧 parabolic 模板的 ambient 扩充，既非 ordinary 全方向族，也不反 G4 目标 δ^(4+ε)N。

B 的 FY 审计另核通过：同一 midpoint/hitting 集合需 packing 控制，坐标格超平面确给命中每条原单位段的 P，但只有 s≤n−1，原公式仅给2。固定 A 的 weak-Lq 子集积分确给平均 λ 的 λ^p Q^(p/q)，没有免费换成四维强 maximal；每 δ 另选有限 A_δ 的 packing0 不能填原 fixed-A 常数。A 的 KT/M3 资格范围也与 root/B 一致：R38 assembly 与 R80 core 已付，M3 全 λ 在 saturated 入口不自动提高 d′，旧数表或递归重证全部参考文献不构成本轮新主机制。有限 primary 搜索未取得新输入不等于 absence、best 或 priority 认证。

## 6. 最终限定通过、停止与完整目标边界

反向 flat P=x5 必须将四维真实 Y 乘 normal δ 厚度，放进固定倍宽的五维管；固定尺度比较、帽 covering 和近满密度常数吸收都只改固定参数。除去 normal δ 后返回同正幂强度 DIR4。正向又只用既有 DIR，故本 certificate 是真实几何 transfer 的闭包，不是新的 gain 方向、full maximal 或新的 ID。没有因 source 应用正确就把完整 G4 的 singular／δ-degenerate leading forms 付掉；物理维≤3 的 R60 和参数 Σ 维≤3 的 R61 均未被冒用来覆盖它。

终 macro6/next6 已实际全文核：保守主维数／branchsaving streak8 不因旧输入应用而清零；DIM 条件后果保留真实具名依赖；完整 ordinary 初始化、direct HRZ、多 matrix/mixed κ 和同一 full-direction 低维构造仍分别未解。下一题尚无 qualified 新 gain，若重开 G4 必须有实际 singular/退化原对象与质量／尺度输入，不能继续调 D/κ 或添加欲证公设。停止本 regular 分支迭代，长期 Goal 继续 active。

结论：当前 root10/B8 的上述数学与量词范围限定通过，未发现未解决强制项。A 自证部分已经 root/B 实际独审，本审查不冒自身独立复核。高级具名 wholeproof 未在本轮全新独证，未经外部同行评审；未作 ordinary 新界、重大性或优先权声明，也不预认证未来 metadata、文件计数、Git commit 或同步。
