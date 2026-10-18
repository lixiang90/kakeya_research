# R0084：原阴影 restriction、凸 factoring 与投影输入终审

2026-10-18，B 独立终审。限定结论为 phase I 的经典输入应用及停止判定；未经外部同行评审。

## 1. 实际全文对象与独审分工

已实际全文读当前 root 主稿 R0084_actual_convex_factoring_input_gate.md 的9节、A稿 R0084_convex_factoring_polynomial_count_audit.md 的8节、B稿8节、working_spec5、终 macro6、next6和 source6。另复用并核本轮实际读过的 GOAL/STATE/ROADMAP/registry入口、R83next6、R43 root10/B7、R49 B8。

一手范围：ICM官方HTML §6 Lemma6.10及相关 definitions/conjecture；旧 GWZ v2 §3所需定义/heredity、完整§4 Lemma4.1 greedy proof及remarks、§5 Proposition5.1完整证明、Lemma5.9完整证明和Lemma5.11；LPSW Lemma4.5及Proposition5.1/Lemma5.3所需statement/尺寸。没有将 ICM本机下载失败或web截图失败写成已保存PDF/已visual核。没有新独证这些论文所有高级 wholeproof、Lean或全部四维来源。

本 formal 主核非自己推出的 root/A 原质量与投影账本；B自己的截面、共同核及几何校准已由 root/A实际全文独核，不把自证充作独立审查。

## 2. assigned partition、平均删选与真实原分母

GWZ输出是 assigned partition \(\mathbb T'=\bigsqcup_P\mathcal C_P\)，不是每个几何containment的重数1。root/A各次
\(\sum_{P\subset W}\#\mathcal C_P\le\#\mathbb T'[W]\)
都合法；没有把 \(\mathcal C_P\) 偷换成全部 \(\mathbb T'[P]\)。共同密度和父/子尺寸 pigeonhole给 \(mM\asymp_LN'\)，原文已在旧库，不是新定理。

平均 \(\lambda\) 的处理逐步通过：删 density<\(\lambda/2\) 至多损 \(I/2\)，选一个 dyadic逐管density层保 \(I/\mathrm{polylog}\)，再factor保该层count，即保
\[
 I'\gtrsim I/\mathrm{polylog},\qquad
 N'\gtrsim\lambda N/\mathrm{polylog},\qquad E'\subset E.
\]
原 \(Y(T)\) whole-label保留，逐管lower独立成立。一般不能同时保证原 \(N/\mathrm{polylog}\)；终macro§2已修成以上实际式并fresh读回。任意权跨度版本没有被免费加入。

原δ方向分离提供absolute \(\delta^{1-n}\) 系数；normalized系数必须保 \((N\delta^{n-1})^{-1}\)。root/A已显式区分，restriction产生 \(N/N'\) 至多polylog/\(\lambda\)。只有原N接近满方向量级时可把最初normalized系数当常数。

## 3. bounded parents 与上下计数闭包

独立核 root/A 的 boundedness：relative convex FW可查 \(P\cap B_R\)，因包含全部assigned children，得 \(|P\cap B_R|\ge|P|/L\)。沿直径方向，最大截面A及两端锥给 \(|P|\ge A\operatorname{diam}(P)/n\)，交球的轴长度至多2R，遂
\(\operatorname{diam}P\le2nRL\)。共同球查询parent absoluteKT给 \(Mv\le L^{O_n(1)}\)。这一步查询任意convex允许，不要求该交集为固定格式半代数；没有循环增加ambient假设。greedy可选children convex hull是另一独立检验。

对同一 fixed-format semialgebraic W，
\[
 m\#\mathbb P[W]\lesssim_L K_N C_DN|W|
\]
配 \(mM\asymp_LN'\) 得parent normalized polynomial containment；absolute版本再用 \(Mv\) 得系数 \(L^{O_n(1)}K_NC_DN/N'\) 乘 \(|W|/v\)。固定P的共同affine归一化将测试pullback体积变为 \(v|W'|\)，除m所得child normalized系数相同。可逆affine保持格式；无需免费把任意P视为低复杂度半代数体。这些推导逐式通过，只是全包含上界，没产生新positive power。

若原有完整partial PW，child restriction及同一affine fraction不变，可保all-\(a\) tail。parents共同对称形状的平移可由 \(\mu_P\lesssim\mu_T*k_{CQ}\) 和R43 restricted-mean支付；这已经是旧common-kernel机制。不同parents的dependent anisotropic核没有被证明可免费统一；本轮亦未反证其任何充分形式。

## 4. 原遮蔽、投影帽及四维适用范围

GWZ Proposition5.1的诱导parent shading是 \(P\cap N_{w_1}\bigcup Y(T)\)，会扩大原footprint；其相容multiplicity管理是独立于generic factoring的真实内容。Lemma5.9的密度lower用二维Córdoba，Remark5.2将一般n版本的责任指向适当 \(\mathbb R^{n-1}\) 输入。LPSW的 \(v_1\times v_2\times v_3^{n-2}\) flakes不包含n5 ordinary \(\delta^4\times1\)管。不能把它们的λ²直接移植。

正面特殊情形没有被误否：GWZ Lemma5.11的round coarse-tube几何可直接保诱导parent density \(\gtrapprox\lambda\)，不需generic convex-FW假设，和R43已付coarsening一致。root§7最后加入此正面范围的句子已fresh读回。一般parent缺口不表示每种shape都失败。

A§7投影cap修订已逐式核。原S4方向w1帽含至多 \(C(w_1/\delta)^4\) labels；除实际m，并用 \(m\gtrsim L^{-C}N'v\)，所得通用保守界为
\[
 \alpha_P\lesssim L^C\frac{N}{N'}\,
                    \frac{w_1^4}{N\delta^4v}.
\]
原稿一般 \(m\asymp Nv\) 的假等号已删；slab句也保 \(N/N'\)，没有将λ损失藏入polylog。此upper不声称任何更特殊geometry都必须达到这损失。

最短轴投影可有重复方向；parent归一化又可产生不同横截面椭球。relative CW或polynomial containment均未自动给DIR003所需真实round graph-tubes/slope-bin原权及newscale shading门槛。OAI4 Hausdorff结论、arbitrary-PW4/fullλ maximal和原方向分离有限种子不是同一输入。R53–55的cap恢复/反攻及R62的PW4冻结没有被绕过。

## 5. 反攻、依赖与已修必修项

B的中心bush校准保实际方向分离及逐管density，未加厚自然parent shading体积约λ^n，只否免费同λ；它不反induced shading的源结论，也不构造Kakeya反例。另一空半parent测试只否把父partial事件逐个收费给同W的child事件；不反任何有充分a-loss的parent PW定理。两项边界在root/A互审中均明确。

本轮两项必须修正均已实际修复并fresh读回：

- A§7一般m与原Nv的比较改为保留N′的合法lower，cap及slab上界含 \(N/N'\)。
- macro§2平均起点的cardinality保留改为 \(\lambda N/\mathrm{polylog}\)，incidence仍保 \(I/\mathrm{polylog}\)。

root主稿相应账本原已正确；修后无遗留强制数学或scope修改。ICM HTML符号转换不作为证明依据；采用既存GWZ实际proof。论文身份、版本及第三方formalization声明不当作本项目已完成全部证明的担保。完整ordinary/HRZ/matrix和Hausdorff桥仍各保其具名未付条件。

## 6. 最终范围与停止判定

在显式bounded原单位δ管、原N/counting law及平均λ的范围，root9/A8关于原shading分层、真实assigned factoring、bounded parents、normalized/absolute polynomial containment、同parent affine child输入的推导限定通过。修后的macro6和next6已实际全文核：拒phaseII，不把源应用或初等ratio当新维数界/branchsaving；保守streak7、完整Goal仍active；下一尚无已锁gain命题，必须完整四路径重选。

本轮没有证明generic anisotropic parent的相容高维密度/full-PW gain，也没证明这种机制普遍不可能。没有fullsource/Kakeya反例、新ID、major、priority或普通n≥5结论；不允许以新名称续冻结CP/PM/PW4。高级wholeproof仍按实际具名范围调用，内部独审不是外部同行评审。

结论：上述证据门和停止范围通过，当前无未解决必修项。本文不预认证未来元数据、Git、同步或尚未写出的研究结果；完成后停止本任务编辑和检索。
