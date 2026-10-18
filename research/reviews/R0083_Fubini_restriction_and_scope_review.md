# R0083：Fubini 删选、原角度质量与输入强度终审

2026-10-18，B，内部限定审查，未经外部同行评审。本文件恰六节；不认证未来 metadata/Git/sync，不把具名来源的应用审查冒成高级 wholeproof 新独证。

## 1. 实际全文范围和独审层级

已实际全文读取最终 root9《R0083_direct_line_union_input_gate》、A8《R0083_Zahl_line_union_input_audit》、B8《R0083_HKM_Fubini_and_restricted_projection_input_audit》、working_spec5、source scope6《R0083_direct_line_union_sources》，以及终 macro6、next6《R0083_next_full_goal_reselection》。同会话先前完整读的数学正文与后来 cross/scope 收尾均已分别核对，没有以合并截断输出充全文读取。

HKM2106.09661v3 的原 HTML 与本地 text，§2 及完整 §3（实际为3.1/3.2）均逐式读过，包括应用证明；§4 反例另读，§5–7/Appendix wholeproof 未新独证。Zahl2208.02913v1 本人仅另实际读本地 PDF1–2 的原主结论/Th1.2 statement，未读其全部八页，不能把 A/root 的完整阅读冒成本人阅读。其具名输入及 A/root 实际应用链在下文按真实层级审查。

正式独审主核 root/A 的可测 lift、有限平均密度与参数阈值、整合范围；B8 自证的删集校准和推导不计本人独立审查，已由 root/A 实际另核。来源身份、版本或字节一致性本身不认证数学；未重新冒报官方 core bytes 或 PDF 视觉核查。

## 2. Compact fibre 的 Borel lift 与真实 Frostman upper

root/A 的 nested compact-witness 选择合法：对连续满射 \(\pi:C\to D\)，逐层用有限 closed balls 覆盖当前 compact 前缀；判断某方向 fibre 与某个固定 compact witness 相交，等价落在其 compact projection。取首个可行 index 的分支事件 Borel，嵌套非空 fibres 的直径趋零，极限给 Borel section。这里没有强行取连续/Hölder selector，亦没有把 arbitrary nonclosed restriction 当紧致子族。

把标准角度概率 \(\sigma\) 推到该 section，得到 \(\pi_*\nu=\sigma\)。canonical metric 中的方向投影 Lipschitz，所以对六维 line space 的任意小球，
\[
\nu(B_{\mathcal L}(\ell,r))\le C\,\sigma(B_D(\pi\ell,Cr))\le C' r^5.
\]
这给真实 5-Frostman upper 及 \(\dim_H C\ge5\)，未给 ADlower、有限 \(\mathcal H^5\)、更高 exponent、全部 support 或 position/direction 独立。正角度 restriction 的 normalized upper 须除原角度质量；closed restriction 保 compact/不交却未必保 full directions。root/A 的这些分母和闭包均未遗漏。

## 3. Zahl 的合法应用、平均 \(\lambda\) 与 matching entropy

原集合维数结论的 \(d\le n\) 与 finite Th1.2 的 \(d<n\) 范围已分别核对；不以两者不同制造 source 错误。finite upper 是 line-space ball 的计数条件，在有意义的 \(r\ge\delta\) 尺度解释；不是 arbitrary indexed-weight maximal estimate。本审查不替源 §3 的随机 thinning、小尺度 rounding 或 CV 高级 theorem 提供未做的完整新认证。

在已满足原 finite 输入的 unweighted family 上，记 \(V=\sum_T|T|\)、\(q=p'=d+\beta>1\)，原 bound 为
\[
\|f\|_p\le C\delta^{(1-d)/q-\varepsilon}V^{1/p},
\qquad f=\sum_T1_T.
\]
若 \(Y_T\subset T\)、\(E=\bigcup_TY_T\)、\(\sum_T|Y_T|=\lambda V\)，则 \(\lambda V\le\int_Ef\le |E|^{1/q}\|f\|_p\)，故
\[
|E|\ge c\lambda^q\delta^{d-1+q\varepsilon}V.
\]
这一平均密度推导完整，不偷升为任意权；逐管 lower 仅在整 label restriction 时继承，进一步删 shading 或平均重新取样须重算。

六维现有原输入只有 \(s=\dim_HC\ge5\)，匹配 \(s=2(d-1)+\beta\) 的 \(d=3,\beta=1\)，合法但只得 union lower 4。超过既有条件 \(17/4\) 需实际 \(s>25/4\)，达5需 \(s\ge7\)，都未付。有限球上较大 \(s\) 使 upper 更宽松，不能同时赠 \(\#T\asymp\delta^{-s}\)；保原 \(\#T\asymp\delta^{-5}\) 后 norm/Hölder 物理量并不改善。packing10、raw longitudinal anchors、可数重复族或 analytic enlargement 都不补这份 Hausdorff 参数 entropy。

## 4. HKM 逐线和平均 clock 闭包及未删等式

root 对 HKM 的应用输入确有匹配：bounded nonvertical compact chart 的整线 union Borel，clock 基底是 AD1 的 \(\mathbb R\)，无需 line labels ADlower。删一个共同 Borel \(\Gamma_1\)-null 集，可对每条原 affine graph 保 Lebesgue-a.e. clock；同一原 \(\nu\times dt\) product 下 Tonelli 也给平均零损。逐线与平均两项都真，但只针对该 Lebesgue clock。

自含校准 \(G_0=B\cap(\mathbb Q\times\mathbb R^5)\) 说明仅由 \(\Gamma_1\)-null 性质不授 whole line、nondegenerate segment 或原 finite marks：所有 rational clock 可同时被删，原 dyadic time law 甚至全损。这不反原定理对特别 \(G\) 的存在主张。取 closure 可恢复原 \(B\)，却不保删后的 Hausdorff 维数；不能回写成 R81 的同维 compact full-direction label restriction。

Cor3.4 的 proof 在正 clock-measure 坏集里取 compact base 后，逐 graph 的正长度和删后正长度都保留，\(r(E)\) 的矛盾链合法。但 Cor3.10 的等式限于 line-family 维数不大于1（或 union<2），不能用于原正角度质量维数至少5的族。一般 Cor3.16 只得 bounded graph code \(s\) 的 a.e. section lower \(s/2\)，在六维仅保证 union 至少 \(7/2\)。未删 Fubini 在所核 source 中是 Conj3.11；Th3.12 是固定 \(m\) 推 Hausdorff \(m-1\)、所有 \(m\) 才推 full upper-Minkowski 的条件结论。不能删掉 conjecture、把 generic clock 换成特殊 clock，或把 source 应用 proof 误作已证一般下界。

## 5. 必修检查、完整 C 和终版宏观范围

当前无遗留 mandatory 数学修正。root/A/B 对核心量词一致：两项 primary 不是因完全不适用而被拒；Zahl 给真实4，HKM 给真实删后/投影信息，但尚无超旧四维 seed/KT 且匹配原 full compact disjoint \(C\) 的新增输入。涉及高级 wholeproof 的短写和标准离散实现保具名层级，未被本审查错误认证或据此宣主定理失败。

终 macro6 与 next6 已实际全文核过，原 \(C\) 的 compact/full \(\mathbb {RP}^5\)/wholeline 输入及 R81 低维条件没有变成 R82 partial chart 反例。C10 只有普通 cycle 数与“五点 affine span 至多4”仍缺 clock-separated 原质量、wholeaxis \(\delta/\mathrm{gap}\) 精度和大量圈共享 carrier；未被锁成新 gain。四条完整路线的未付责任与全部旧冻结保持，没有把其缺失部分改名成已获公设。

下一只是完整目标重新选题协议，明确尚无合格主命题，不继续本次两 primary 的 abstract 检索；不是预领新的 source theorem 或 phase II。本轮未获得新 ordinary 高维界、fullcompact no-family、Kakeya 反例、major 或新数学 ID；搜索未命中及出处身份不作 priority/正确性保证。

## 6. 限定 verdict、独立分工与停止

在具名 primary 输入、实际读域及上述范围下，root9/A8 的应用与强度审计通过，无必修项：Borel lift/Frostman upper、平均 \(\lambda^q\)、finite upper 与 entropy 区别、HKM 逐线和平均 Lebesgue clock 闭包、未删 Fubini 的条件性均已独立核算。B8 自身内容不计本人的独审；root/A 的实际另审记录保留，未宣其 source 高级 wholeproof 获第二次完整新独证。

本结果为内部 reviewed 的有界输入选择审查，未经外部同行评审。真实新证据与主 gain 无新维数/branch saving streak6 分开；完整 Goal active，未因当前未选定题目置 complete 或 blocked。当前审查完成，停止编辑与检索，不预认证 root 后续 metadata、归档、Git 或 exact-byte sync。
