# R0049 正式独审：source、原质量和下一机制范围

2026-10-17，A。结论：**通过下述局部预算、附加类正规化与宏观范围；不通过一般 E5* 归约，也不认证整个 WZ2025 Proposition 3.2 已修复或 WZ2026 §18 全部证明。** 未经外部同行评审，无新普通高维 Kakeya 界或重大性/新颖性认证。

## 1. 实际全文读取及独立性

本次实际全文读完：

* root `notes/40_multiscale/R0049_general_input_regularization_and_deficit_ledger.md` 八节；
* B `notes/40_multiscale/R0049_original_mass_deficit_and_regularization_counteraudit.md` 八节、186 行；
* `research/reviews/R0049_macro.md` 八节；
* `notes/20_dimension_lifting/curved_lifting/R0049_next_nonlinear_coherent_lift_gate.md` 五节；
* 本轮 working_spec 与 A source 审计十一节终稿。

读源范围另见 A 审计 §2：WZ2025 原 Def2.1/3.1/3.2、Lemma3.3 与完整 Prop3.2 三步，WZ2026 Def17.1–4 和 §18 至(145)；本地 v2 PDF13 已实际渲染查看。A 自己的 source 稿不算独立认证；以下逐项针对 root 与 B 的实际证明。单次 regrid 的 initial-μ 补证由本人提出并经 root/B 独立重算，不能将此作者身份隐藏成另一个全然独立证书。

## 2. 原来源及极值量词：通过

WZ2025 Def2.1(b) 确实要求每个 coarse scale 的近 sticky cover，σn 只对此类定义。Prop3.2 的三步依赖链准确：原(b)给 parent 数，原 incidence 给各 parent 质量，M 下界给 coarse/fine multiplicity upper，原同一 σn 的小并集再迫二者近饱和。任意给定 κ0 的小并集输入不自动具备这些相同极值类的上下界。

WZ2026 Kd 起点明确是 joint(d−1)-AD/CW 及平均 dense 原 shading；Prop17.2/18.2 选择这个类的 extremal witnesses，未对 arbitrary ordinary full-direction input 给输出。原 direction separation 不送 joint AD lower 或 every-scale near-minimal joint covers。R42 digit-permutation 的(b)失败可校准这一点，但未付 small union，三稿没有将它当 E5* 反例。

原 v2 的(3.5)确有 outer h-grid 的时间厚化责任。已读正式 arXiv 当前 history 仍 v2(2025-10-07)，AMS 正式 PDF 未成功取得/读取，故不能声称刊本修没修或 wholebytes 同。此次 source 局部问题没有被升级成原最终定理反例；也没有用局部修复追认整个 Proposition 的认证。

## 3. 保原计数质量后的 q、J 和相对尺度：通过

设 I0≥cδ^η m/δ，IA≥δ^ℓ I0，a=ℓ+η。每管在 q-clock 内最多 C(q/δ+1) 访问，先以原 m 上界计数得到 q+δ≥cδ^a；a<1/10 时 δ 项可吸收，所以 q≥cδ^a。该推导不需要事先知道 NA 的 lower。

r≤q 时，whole-window containment 对每条轴在两个端点相减，给 slopes 落在半径 Cr/q 的 ball；原 δ-separated packing 送 NA≤Cm(r/q)^4。代回 IA≤CNAq/δ 得 r⁴≥cδ^a q³，故 J=qr⁴≥cδ^a q⁴≥cδ^(5a)。r≥q 时直接 J≥q⁵，同一结论成立。于是 r≥cδ^(5a/4)，h=δ/r 满足 δ≤h≤Cδ^(1−5a/4)。

这些都是已有合法保质量 parent/window 的必要预算，既不构造 parent，也不送 AD lower。root/B 明确保留这一边界，因而没有只据 q^(-4) 因子错判 E5* 不可能。

## 4. shadow 修复、原代表及密度/CW：通过

wholeclock 的 β-heavy blocks 删除访问上界 CβN/δ；配 δ⁵I≥δ^u r⁴、N≤δ^(-v)h^(-4)，取 β=δ^(u+v+w) 给相对删除 ≤Cδ^w。每 output h-cell 选一个原 heavy block 见证，它在固定邻接像中贡献至少 cβh⁵ 的**原细 cell 体积**；固定邻接 bounded overlap 求和，得 outer≤Cβ^(-1)r^(-4)|E′|。只需一个 witness，不合并不同管的 marks，不假事件或 μ 独立。

一般 q≥r 时，原 block 长 qh，重块体积 βqhδ⁴ 除以 J=qr⁴ 正好是 βh⁵；删除 CβNAq/δ 与上述原质量 lower 相容。q<r 时也已核常数 packing：whole-window containment 与 bounded 原 slopes 给 `|q c′/r|≤C`，所以共同 affine map 的最小奇异值 ≳1/r，原 cell 像的最小主尺度 ≳h。其固定 h 增厚可由原共同 δ-grid 的固定邻接实现，只付维数/chart 常数。不能在这一分支偷加入 q 的幂。

之后只删 whole labels，故 heavy 性及 shadow upper 保持。新 joint h-bin 的原 slope width O(δ/q)，最多 Cq^(-4) 原 labels。每 bin 取原访问最多的一个代表，固定着色仍至少保 cq⁴IA；每个代表携带自己的 marks，原别人的 marks 不转移。原轴仅与 cell 相交的约定，可用 whole δ-cell 并的固定邻接缓冲，相应体积只乘常数，原访问仍按原 label/time 记。

独立重算：Iret≥cq⁴mδ^(a−1)，而每代表访问≤Cq/δ，故 p′=N′/m≥cδ^a q³≥cδ^(4a)。新总 duration 至少 (δ/q)Iret，除 N′≤m 给平均 ≥cδ^a q³≥cδ^(4a)。q<r 时 image 原 δ 段跨多个新 h-bins，不能丢掉这项长度；三稿已正确处理。

CW 计算对 whole unit-clock 新管使用 John ellipsoid/direction packing。新 slope separation 是 qh，任一含新 h-tube 的凸体各短轴至少 ch，故其中原标签数 ≤C(qh)^(-4)|W|；除 N′=p′m 得 `C_CW,new≤Cr⁴/(p′q⁴)≤Cδ^(−8a)`。取代表/固定 h-rounding 的角误差在凸体固定 h 加厚中支付，不需方向满网重新生成。

最后 β=δ^(a+w)、J≥cδ^(5a) 给 output union≤Cδ^(κ0−6a−w)。先固定 target ε,κ0，再选 ℓ,η,w 充分小，能同时付原访问约 δ^(5a) 的损失、h-relative CW/density 常数及固定正 κout。此结论仍以已经有合法 parent/window 为条件，没有证明主 E5*。

local-heavy 不闭于任意后续细 shading refinement，原常重数 μ 更不能等于 rounded 后的新 μ。A 的单次修复用 initial E、I 的常重数，再取 heavy 子族，得到 `μinitial≤Cδ^(−b)θ^(−1)h^(−σn−ε′)`，相对 h 的损失可由 η≪ε² 吸收；它未补齐 Prop3.2 最后任意 refinements。三稿已显式限制此 scope。

## 5. 额外 all-scale cover 上界的 AD core：通过

该命题的附加输入 `Ns(P)≤K s^(−4), K≤δ^(−η)` 明写，未从 small union 得到。由细至粗用**当前**后代数测试：某节点不足 θ(s/δ)⁴ 时整删。每尺度最多 Ks^(-4) 原 occupied cells，所以总删 ≤CKθlog(1/δ)δ^(-4)。除原 incidence lower，而不是只除 m，损失比例 ≤CθKlog(1/δ)δ^(-η)=o(1)，θ=cδ^(ε/2)、η≪ε 即可。

后续 ancestor 删除不破存活节点的 lower：若最后仍有一点，该点的祖先都没有被整删；处理较粗层时也不会仅删除该点所在的更细节点的一部分。故所有最终 occupied cells 同时过 threshold。support-centered ball 内取包含该点的尺度 cr 子 cell，送任意球 lower；s=Oδ 用该点本身，upper 仍由方向 packing。没有把擦边非空 ball 强行赋 lower。

全体标签删得很少，N′≈m，原 whole unit tubes 的 direction-separated CW 及全部原 marks 都保持；h=δ、无 clock/affine，output union⊂E。附加类的 deficit 因而确实原样保留。只保平均初始密度时还需另 heavy，不能借此宣逐管；三稿已分开。此证明是额外近 sticky 子类的合法正规化，不是一般 E5* 或新的 ordinary bound。

## 6. macro 与下一任务：修正后范围通过

macro 真实执行停止：未证一般小 union→near-minimal joint coarse entropy/lower，故停止初始化 gate，不换 coarse-entropy/AD threshold 名称再开轮。FG 的 topology 只作已读 primary 的备用输入；其边界 Hölder/W^(1,p) 假设与 Lusin、rough 插值原 footprint 回传尚未付，macro 没有据它宣新机制或无限重证已有工具。R41/R47 冻结边界保留。

下一命题已正确换成 arXiv2609.06299v1 的 lift Definition2.1，不再与 GAFA00750-4/2511.10918 的 Bourgain-condition/AppendixA 混淆。官方 history 此次实际打开只有 2026-09-05 v1；本地 PDF6 定义确允许一般 smooth time-preserving submersion，a 可依 y,w,ρ，而 Θ 不依 w，整段全参数 coherence 与方向 rank 都必须保持。

R12/LIFT005 只对空间 affine πt=T(t)z+c(t) 完整分类，下一稿的非线性 πt 严格扩大容许 class。旧分类不能不经新的 rigidity 直接排它。下一稿也准确警告：对 w 微分时 Dzπ 依赖当前点，不能再视为旧共同常数右逆；更换 clock、只保 w(y) selector 或少一个 ρ 不回答新命题。存在 lift 的应用直接只是从 4D 直线输入到某 3D 曲线族，不能倒推普通 R5；不存在只排该机制。没有预认证新不等式、主问题解决或重大性。

## 7. 终判和未认证项

本轮 root/B 的已写数学预算与 special-class 证明可按上述 scope 归档。一般 E5*、完整 R5 sticky、H5 与一般/高维 Goal 均未完成；没有符合全部 E5* 输入的反例。未将新 metadata、PDF hash、最后 Git/sync 或外部同行评审当作本次数学 review 已核对象，仍由 root 统一验证。

本文完成后停止编辑/检索，不扩下一轮数学施工。
