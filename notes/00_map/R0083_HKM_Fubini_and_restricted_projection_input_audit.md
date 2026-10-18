# R0083：HKM Fubini 删集、原直线 clock 与受限投影输入审计

2026-10-18，B，phase I 一手输入匹配。恰八节；未获授权主定理施工或 formal。本文不把 conjecture 当输入，不把 \(\Gamma_1\)-null 删集变成紧致全方向子族，也不以题名认证高维改进。

## 1. 实际版本、全文读域及本轮对象

已实际读当前 STATE、R82 next6、R83 working_spec5；R81 归约及 R82 root/A/B 与正式审查沿用同会话真实全文记录。原首要对象为 \(m=6\)（亦可一般 \(m\ge5\)）的 compact canonical line family \(C\)，方向满 \(\mathbb {RP}^{m-1}\)，distinct whole lines 不交，可能另反设 \(\dim_H S(C)<m-1\)。不授 line-parameter ADlower、PW/CW 或 Hölder selector。

本次实际一手读 [Héra–Keleti–Máthé, A Fubini-type theorem for Hausdorff dimension, arXiv2106.09661v3](https://arxiv.org/html/2106.09661v3)：HTML 明写 2022-09-15；先完整读 §2，再完整读 §3 全部 statements、应用与证明，继而对照 root 保存的 literature/extracted/hera_keleti_mathe_2022_Fubini_2106_09661_v3.txt 相同读域。原 §3 只有 §3.1、§3.2，另有 Definition 3.3，并无第三个 §3.3 小节，故准确记为“完整 §3”。§4 反例及其证明另实际读到；§5–7 与附录的高级 wholeproof 未新独证，仍具名保留。

未自行下载、未宣本人的 PDF 视觉或原 bytes 核；root 的版本/26页/404219bytes 等 metadata 与本人的数学阅读分层。没有以公开作者身份或原论文已发表身份代独立应用审核。

## 2. 标准设置与主定理：AD 是 clock 基底，不是管参数

在 \(B\subset T\times\mathbb R^n\)、\(T\subset\mathbb R^k\) 的设置中，\(\Gamma_\alpha\)-null 逐个测试所有 Lipschitz graphs 的 base-\(\mathcal H^\alpha\) 零集；不是说 \(G\) 自身 Hausdorff 维数低。Theorem 2.12 的实际数据是：Borel \(B\)、AD \(\alpha\)-regular \(T\)、\(\dim\operatorname {proj}B=\alpha\)。其等式涉及 \(B\setminus G\) 和**原** sections 的 essential supremum；Theorem 2.14 用所有 sections 的共同维数 upper 得删后 upper。这些输入均在 [原文 §2.3](https://arxiv.org/html/2106.09661v3#S2.SS3) 明列。

对非 vertical 整线 union 可选 clock \(\mathbb R\) 作 \(T\)，所以这里 AD 基底免费由真实整线全时钟提供；它并没有把 \(C\) 的 angular-uniform lift 或 line-space support 变成 ADregular。若换成原 discrete/fractal time law，不能仅因其有 Frostman upper 或正有限 Hausdorff measure 便沿用 AD 版本；§4.4 本来就在校准这个差别。

对 \(\mathcal H^\alpha(\operatorname {proj}B)=0\) 时 essential supremum 的 \(\alpha-\varepsilon\) 极限约定也实际核过，不能不经检查把它写成某个任意 weighted prior 的 ess-sup。当前整线 clock \(\mathbb R\) 情形没有该退化。Proposition 2.6 的 almost-every-Grassmann-clock Fubini 性质属于 generic 结论，不能指定为下一构造所需的特殊 clock。

## 3. 合法 whole-line 应用及 \(\Gamma_1\) 删选的实际质量

在 bounded nonvertical direction chart 中，线写 \((t,b+tv)\)。原 compact \(C\) 的 chart restriction 仍 compact，whole union \(B\) 闭、故 Borel；每条线是一个全球 Lipschitz graph。Corollary 3.2 的证明确实可直接调用 2.13，使各原线仅删一维测度零集，并得到删后 Fubini 维数。这是合法的 genuine input，未发现主定理输入不匹配；关键是它的**输出对象不同**。

以下自含反攻说明不能免费升级：在此 clock 下
\[
G_0=B\cap(\mathbb Q\times\mathbb R^{m-1})
\]
是 Borel \(\Gamma_1\)-null。\(B\setminus G_0\) 在每条原线保 Lebesgue-a.e. clock，却不包含任何整条 nonvertical line，甚至不含任何 nondegenerate nonvertical segment。对这些线的任何 clock interval 都有 rational clock 被删。该例只否“\(\Gamma_1\)-null 所以 wholeline/segment 保留”的推论，不反原定理可选某个特殊 \(G\) 的存在主张。

若原 clock 真是 Lebesgue、label 为任意有限 Borel 概率 \(\nu\)，共同 Borel \(G\) 的 graph preimage 可测，Tonelli 给每条线、每个 bounded interval 的零损，也给 \(\nu\times dt\) 的平均零损。逐线和平均这两种闭包都真，无需独立抽选 null sets。反之，对于 deterministic dyadic finite clocks，\(G_0\) 可删**全部**原 marks；不是 \(o(1)\) 损失。此 qualitative theorem 未给有限 \(\delta\) cover、允许尺度或 uniform loss，不能直接接旧 FSD/DIR 的 finite seed。

删后集合通常不 closed/compact，也不是原 \(C\) 的 whole-label restriction。沿各原线剩余点 dense，故 closure 可回到原 whole union，但 Hausdorff 维数不对 closure 连续；恢复 closure 就失删后 upper，不能借 R81 typical-minimality 把它“补成”同维紧致全方向族。

## 4. Corollary 3.4、低参数范围及完整证明用途

原 Definition 3.3 的 \(r(E)\) 是“每个原 affine plane 上保正 \(\mathcal H^k\) 质量”的最小 union 维数减 \(k\)，不是方向数或已付 uniform positive gain。Corollary 3.4 在 Borel nonvertical whole union 上给 Lebesgue-a.e. base section 的 \(r(E)\) lower。其 [完整反证](https://arxiv.org/html/2106.09661v3#S3.SS1) 已逐步核：假一正 base-measure 集 sections 低于 \(r-\varepsilon\)，从其取正测度 compact base \(A'\)，每个 graph 因满投影而在 \(A'\) 上有正 \(k\)-measure；2.14 的 \(\Gamma_k\)-null 删集保持这份正质量，最终与 \(r(E)\) 定义矛盾。没有把只对部分 planes 的质量赠给全部原 \(E\)。

Theorems 3.6、3.8 提供的是具名旧 line-family bounds。Corollary 3.10 的全 Fubini 等式只在 \(\dim_HE\le1\)；其“union \(<k+1\)”推论先由 3.6 迫参数维数 \(<1\) 后才调用。对 R81 的 \(m=6,k=1\) 全角 family，方向 Lipschitz image 已有维数5，这个低参数范围明显不匹配。不能把“\(s\le1\)”误读成当前 line dimension \(k=1\)，两者是不同变量。

若想通过先取某个参数维数 \(\le1\) 子族再反复使用，必须保原 full angular image/质量；原方向维数5已禁止这样保 full directions。只保一个低维子族所得等式，不反当前 \(S(C)<5\)，也不是新的完整归约。

## 5. Conjecture 3.11 与 Theorem 3.12 的条件方向

一般 Borel nonvertical whole-plane union 的未删 Fubini 等式，在原文是 **Conjecture 3.11**。Theorem 3.12(i) 假它在固定 \(m,k=1\) 成立，才推每个 Besicovitch 集维数至少 \(m-1\)；(ii) 需要它对**每个** \(m\ge2\) 成立，才导出所有维度 full upper-Minkowski。不能从固定六维或某 chart 情形直接称所有 Hausdorff/full Minkowski 结论。来源和条件关系见 [原文 3.11–3.14](https://arxiv.org/html/2106.09661v3#S3.SS1)。

本次实际逐步核完整 proof：具名 KM 先换为同维 closed full-line set；projective map 把方向无穷远面送到 \(H_1\)，得到 punctured lines；再在 \(H_1\) 选一高维 continuous graph \(C_0\)，它对另一组平行 sections 每片至多贡献一点。以两个 transverse clock 方向及可数角度下界分组，Lemma 3.13 的 compact anchor/direction witnesses 保每组 whole union 闭；countable dimension 选一组维数至少 \(m-1-\varepsilon\)。若猜想可用，就会迫整组维数不超过去掉 \(H_1\) 后的低维部分，矛盾。

高维“隐形”graph 的贡献正是被当前删集 theorem 允许丢弃的类型；不能把 2.12 的 \(B\setminus G\) 等式替换为该 proof 需要的 \(B\) 等式。因此 Theorem 3.12 没有把 main Fubini theorem 自动变成 \(m-1\) 下界。原 Remark 3.14 只把所需猜想缩到 closed unions，不把它升级为已证，也不说明已对 pairwise-disjoint/full-angular 子类证明。

## 6. Corollaries 3.15–3.16 的对偶码与可用强度

这里的原受限 family 是
\[
\pi_t(x_0,\ldots,x_k)=x_0+\sum_{i=1}^kt_ix_i.
\]
Corollary 3.15 保参数维数只在 \(\dim_HX\le1\)；3.16 对一般 Borel \(X\) 给 almost-every \(t\) 的 \(\dim_HX/(k+1)\) lower，不给任意 singular time prior 的坏集质量。其 [应用 proof](https://arxiv.org/html/2106.09661v3#S3.SS2) 全文已核：先 compact approximation，再令 \(P_x=\{(t,\pi_t x)\}\)；bounded code 与 natural plane metric 双 Lipschitz，whole union 是 \(\sigma\)-compact/Borel，section 精确等于 \(\pi_tX\)，最后用 3.4 加相应 \(r(E)\) bound。没有依赖未证 Conj3.11。

对原六维 \(C\)，取一个 bounded transverse chart；其 graph parameters 为 \(X=\{(b,v)\}\subset\mathbb R^{10}\)，\(s=\dim_HX\ge5\)，因为 slope image 含一个五维开角度 chart，且参数与 canonical metric 在此 bounded chart 双 Lipschitz。应用 \(k=1\) 的 3.16 给 a.e. clock section 维数至少 \(s/2\)，再用基础 section lower 给
\[
\dim_H S(C)\ge1+s/2\ge7/2 .
\]
这只有旧一般 bound 强度，弱于现有四维种子/KT 所给六维后果，不关闭 \(\dim S(C)<5\)。若另反设该低维，就只约束 \(5\le s<8\)，这个非空区间不构成矛盾。没有从 compact disjointness 得 \(s\ge8\) 的原输入，不能假它来锁题。

## 7. Angular law、原删选与旧 gain 排重

满方向 continuous projection 的 compact fibres 可给 Borel measurable lift，而非连续/Hölder lift：用有限 closed balls 的 nested fibre witnesses 逐层选择，判断“某 fixed compact witness 与 fibre 相交”是其 compact projection，故 Borel；直径趋零给 Borel section \(s\)。把标准 angular probability 推到 \(s(D)\) 即有原 angular-uniform \(\nu\)。这是可自含核验的选择接口，不授 \(\nu\) 在 line space 的 ADlower、全部 support 或 fixed-format PW/CW。

原 \(\nu\) 在角度 caps 中的质量保持，但定理 exceptional clocks 用 Lebesgue null，不是 \(\nu\) 或某原离散 time prior 的 uniform estimate。closed direction restriction 保 compact/inherited disjointness，通常失 full directions；正角度 measurable restriction 保一个 angular mass 但未必 compact。第3节共同 \(\Gamma_1\) 删集的逐线/平均 Leb-clock 闭包不能混成这些 whole-label restrictions。

若欲把未知 \(r(E)\) lower、未删 Fubini 等式或“删后可恢复同维 full compact 族”当新假设，它们正是新的实质 Furstenberg/extension 责任；本次没有证明。若只统一调用旧四维 finite seed、KT 或既有 CP/PM/PW4 positive-gain 读出来支付同一责任，则是旧全称闭包，不新增方向/结果。原完整对象不因局部 graph 双射或本次 Borel lift 就获得 R76 缺失的 Schubert spreadout。

## 8. 有界输入选择 verdict、独审与停止

当前一手结论有真实可用匹配：全 clock 的 Borel 整线 chart 满足 2.12/3.2/3.4，且 graph-code family 满足 3.16；上述应用不是因输入不满足而全盘拒绝。但输出只为 per-line a.e. clock 删集和一般投影 lower，未找到超旧四维种子/KT、又能处理原 compact full-direction disjoint \(C\) 的新输入。最强目标等式在此次核过的 source 中仍列为 conjecture，不能作为已证输入；这不是未检索其后全部文献却认证全球当前 open 状态。低参数 corollaries 不覆盖维数至少5的原 line family。

建议依 R83 spec 停止这一轮 HKM 输入门，不锁未删 Fubini/同维紧致恢复作 target-strength phase II，也不续第二轮同 family abstract 检索。由 root 完整宏观重比 ordinary 初始化、direct 多尺度、全部 matrix/mixed \(\kappa\) 与真 compact 构造；完整 Goal active，没有 n−1 下界、Kakeya 反例、new ID/major 或优先权结论。

已实际全文读 A8《R0083_Zahl_line_union_input_audit》：从其明确具名定理所得有限平均 shading 的 Hölder 代数、原参数 entropy 与大指数 upper 的差别、六维 \(s=5\to4\)、严格超过 \(17/4\) 需 \(s>25/4\)、得到5需 \(s\ge7\) 的门槛均独核一致。其 Borel angular lift 只授 upper、KM typical Hausdorff 与 packing 分开、raw anchor 重复不增 canonical dimension 的范围也正确。本人没有把仅实际读 A8 当成自己实际全文读 Zahl 新原 primary 或独证其高级 wholeproof。A 已实际全文读本 B8，自含删集/clock 与六维代数无阻断，但其本人未新读 HKM §2–3，故也没有把它虚记为 HKM wholeproof 的第二次独证。

又已实际全文读 root9《R0083_direct_line_union_input_gate》、source scope6《R0083_direct_line_union_sources》，并 fresh 全文读 A8。root 的 nested compact-fibre Borel lift、原 \(\nu(B_{\mathcal L})\lesssim r^5\) upper、Zahl matching entropy 与六维阈值、HKM 删集类型及 generic/fixed-clock 分离均一致，无必需数学修正。另实际读 Zahl 本地提取 PDF1–2 的 Conjecture1.1/已证结论与 Th1.2 statement：集合版 \(d\le n\)、finite norm 版 \(d<n\) 的范围差别正确，不能混成 source 错误；本人仍未冒完整八页或其抽样 proof 新独证。root 已实际全文核本 B8，无 mandatory。当前 line-union 门依锁题停止，拒未付 phase II。

本稿是 primary scope/应用审计，不是 source §§5–7/附录 wholeproof 的新独证；标准 section lower 与具名 3.6/3.8 亦不冒本轮新发明。未写 formal；无新数值实验、下载、Git/meta/spawn 或未来同步认证。
