# R0081：紧致族归约、全方向量词与内部避交独立终审

2026-10-18，B。内部逐步审查；未经外部同行评审。仅审本轮锁定的条件归约，不认证未来元数据、Git、同步或新维数结论。

## 1. 实际全文范围及独审分工

已实际全文读取 root 主稿 notes/20_dimension_lifting/disjoint_lines/R0081_baire_reduction_to_compact_disjoint_families.md 的 12 节、A 独立稿 notes/20_dimension_lifting/disjoint_lines/R0081_code_space_and_baire_avoidance_audit.md 的 12 节、B 稿 12 节、锁题 working_spec 5 节、终 macro 6 节、next R0081_next_fullcompact_multifiber_gate.md 的 6 节。两份 phase I 拒题稿 A8/B7 的已有实读记录仍适用；本次没有把旧 onefull 或 KT 数表重新认作数学进展。

另实际完整读取新 Keleti BME 讲义 21 页提取文本，并核 KM2203.15731v3 Theorem 1.1 及 §2.1 Lemmas 2.1–2.2 的 statement/相应证明读域。B 未声称本次重新视觉审查原 PDF 或新做官方整文件字节验证。以下独审重点是 root/A 的完整证明；B 自身重构由 root/A 已独立实读，不拿自审替代独审。

## 2. 原空间、具名输入与固定障碍密度

原空间是 \(K\subset[0,1]^n\times\mathbb {RP}^{n-1}\) 的非空紧致 code，方向投影满射，取 Hausdorff metric。full projection 条件闭，故 hyperspace 子空间完备；没有向 arbitrary measurable selectors 缩题。canonical 参数 \(((I-P_e)p,P_e)\) 对 bounded codes 连续/Lipschitz，同像恰为同一 whole line，且线族像紧致。incidence 闭性给 whole union 闭、从而 σ 紧致，不只给单位线段的性质。

KM 的共同最小维/typical-minimality 是明确具名输入：低维 Besicovitch 集存在时，完整 code 空间有 residual \(G\)，其 whole unions 维数不大于某 \(s<n-1\)。本轮没有新独证该高级 whole proof，也未免费从原不可测集合取 compact 子族。

固定 compact \(B\) 的 hit 事件在 code 与交点共同紧致化后闭，避交集开。密度逐式通过：原位置先内移，正交投影的 compact nowhere-density 保一个近位置的原方向线避 \(B\)；连续性保真实 open direction neighbourhood。root/A 分别保 finite good-code net 及 finite closed direction cover，前者保旧到新，后者保满方向，新到旧亦受控。closed caps 可用 finite subordinate refinement 取，不能只依赖 finite direction net。cube 边界与同方向多 position fibres 均保留。B 的单乘积开覆盖版本为等价的独立校核。

## 3. 内部自依赖、同一 residual 与可数 whole families

root/A 的局部化不是把 dense \(G\) 随意截到 closed position 子空间：\(V_U=\{K:K\subset U\times D\}\) 为非空相对开集，故可与 \(G\) 及先前 fixed σ-compact whole-union 的 residual avoidance 条件相交。B 稿以 cube homothety 转送真实最小维 residual 的另一证法也合法，未误用 arbitrary residual 的 closed-subspace restriction。

对 canonical line 距离至少 \(1/j\)、交点在 \(\overline B_R\) 的坏对，codes、交点都可共同取极限，故坏集闭。构造 density 时 finite 小 code pieces 内部 canonical 直径小于 \(1/j\)；不同 pieces 选取时实际避先前 **whole** unions。这样解决 \(B=S(K)\) 的自依赖，而非直接引用 fixed-\(B\) lemma。pieces 的 closed direction caps 仍覆盖全部方向，Hausdorff 两侧近似均有真实 witnesses。

所有 \(j,R\) 取同一 countable intersection，再与 \(G\) 相交，给同一族内部全部 distinct lines 不交。随后归纳逐避先前每个 whole union 的 compact truncations，得到可数个紧致全方向族，跨族同一直线亦被排。参数重复只按 canonical quotient 去重；平行多线不被误判。不存在先逐方向选择、再 closure 偷增交线的步骤。

## 4. 独立反攻、严格性及下一门量词

严格 \(s<n-1\) 真实必要于本证法：法向方向在 full-direction code 中必须出现，若位置接近超平面 disk 的内点，附近法向 lines 必穿 disk，故维数 \(n-1\) 障碍不授 density。闭无界点集的 parallel-line 例只校准非 compact hit 关系的开性失败，不被夸为 full-direction 空间反定理。交点逃无穷的两线例说明 \(R\) 截断不可漏。

σ 紧致障碍的 avoidance 仅为 residual，一般不称开；任意非 closed restriction 亦不授 compact。全文没有唯一方向、连续 selector、流形、Lipschitz inverse 或 semialgebraic 假设。原讲义非紧致 closed 构造仅在 \(\mathbb R^3\) 与类似奇数高维明确，未误用于 compact 或所有偶数维。

终 next6 仍只授权完整 compact 多 fibre 问题的阶段 I。其大球端点模型在 \(R>\sup|a|\) 时经 orientation double cover 连续、由原线不交给端点单射，compact 到 Hausdorff 闭像的 homeomorphism 合法；但 next 明确不据此声称闭像是整球面/流形、方向可单选或 degree 已定义。尚未选定新的无条件障碍，不提前认证下一数学。

## 5. 依赖、修复项与未付结论

当前没有遗留强制数学修复项。B12 初次落盘的若干 inline math delimiter 缺失属于实际字面问题，已在其授权文件中修正，并检查 display/inline delimiter 配对；未改变数学。root/A 的两步 finite cover 证明与 B 单乘积盖不是漏洞分歧。

具名高级输入保留 KM typical-minimality/最小维变体定理；其余核心使用 compactness、Hausdorff hyperspace、正交投影与 Baire category。新 Keleti 讲义是已报告归约的来源；本轮补齐省略证明，不声项目首创、优先权或外部 peer review。未把 full source 身份、作者署名或一次检索未命中当正确性/新颖性担保。

此处没有有限 \(\delta\) shading、平均/逐管/逐 pair 密度的数值闭包；方向覆盖只在具体 closed-cap 拼接中保持。定性还原不授 CP/PM/PW4 正幂增益或新 maximal estimate。no-compact-family 若将来在某 \(n\) 成立，才由逆否与具名输入得该 \(n\) 的 \(d_n\ge n-1\)；本轮未证明 no-family，也没有证明反向 existence 推低维。因此不是 full Kakeya 等价声明。

## 6. 限定 verdict 与实际终版 scope

在明确的具名输入和严格 \(s<n-1\) 假设下，root12/A12 的所锁归约逐步通过：存在可数 compact full-direction straight-line families，全部 distinct whole lines 两两不交，每族 whole union 保低维。内部自依赖、同一 residual、可数 whole-union 避交和 selector 范围均已实际核算，无遗留 mandatory。

终 macro6/next6 已实际全文核对：本轮有新的具体 source 及完整 Baire 重构信息，保守主 gain 无新维数/branch saving streak4，四完整路径与旧冻结责任仍保留；不以归约证明冒普通高维/general 目标完成。n6 的未来 no-family 才可能给至少 5，当前没有这一结论。结果为内部 reviewed 的条件证明核验，未经外部同行评审，高级 wholeproof 未新独证；不预认证后续归档、Git 或同步状态。
