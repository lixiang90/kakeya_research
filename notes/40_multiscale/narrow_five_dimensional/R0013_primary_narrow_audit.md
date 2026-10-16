# R0013：五维三平面窄端点的一手文献审计

2026-10-17。任务 N5-NARROW-GAIN-01。只审计 working spec 中原有的真实单位管、原 cubical shading 和点态三平面窄条件，不赋予 sticky、AD 正则、two-ends 或平面场正则性。

## 1. 结论与读过的范围

在下列已核来源中，尚没有可直接给出目标
\[
 |U|\gtrsim_{\epsilon,C,C_0}\delta^{1-\sigma+\epsilon},\qquad \sigma>0
 \tag{NG}
\]
的定理。这是对明确来源及明确输入接口的审计结论，不是对全部文献的不存在声明。

最直接的高维来源是 Kulkarni 2024 学位论文第三章。其 Definition 16 与本轮点态窄条件匹配；Proposition 18 声称的指数为
\[
 |U|\gtrsim_\epsilon
 \delta^{(n-2+k-d_k)/3+\epsilon}
 \lambda^{d_k/3+1}\sum_T|T|,
 \tag{K18}
\]
其中 \(d_k\) 是 **\(k\) 维极大函数估计**的维数参数。代入 \(n=5,k=4\)，即使假想 \(d_4=4\)，也只有 \(\delta^{1+\epsilon}\) 基线，不能给严格的 \(\sigma>0\)。此外，第三章打印证明存在下文第 7 节列出的未闭合计算；本项目没有独立验证整项 K18。

Katz–Zahl 的原 planebrush 定理在 \(\mathbb R^4\) 使用点态 **二平面**。HRZ 的 \(n=5,k=4\) broad 阈值确实对应 \(21/5\)，但其 broad-to-linear 命题需要 \(p>3/2\)，没有把本轮三平面 narrow 输入转为 \(>4\) 的结论。

已读范围：

- Zahl survey §4.3–4.4、Theorem 4.4/Corollary 4.5/Theorem 4.6 及文献 [42]、[43]。
- Katz–Zahl arXiv:1902.00989 **v3** 的 Definitions 5、9、21，Propositions 11、32、37；浏览相关 proof 接口。未重证整篇。
- Kulkarni thesis Chapter 3 的 Definition 16、Propositions 17/18/20/22、Lemmas 21/23/28/29 和 §3.4 删除算法；关键公式已查看 PDF 页图。未重证整篇。
- HRZ arXiv:1908.05589v1 的 Theorem 4.1、Proposition 4.2 及其缩放证明。该 arXiv 当前只有 v1；刊物版本为 2022。

## 2. 版本、存档与准确定位

新增官方原件：

1. [Kulkarni 官方论文](https://thesis.caltech.edu/16515/1/Kulkarni_Neeraja_2024.pdf)，作者 **Neeraja Raghavendra Kulkarni**，Caltech 2024 thesis，66 PDF 页。存于 literature/primary/kulkarni_2024_sticky_planebrush_thesis.pdf；SHA256 4644b8b051d32ef0d0cce000b2694ef5ea120fef8748810ac75690b1e68416dc。
2. [Katz–Zahl v3](https://arxiv.org/pdf/1902.00989v3)，2025-10-07 修订，40 页。存于 literature/primary/katz_zahl_2019_planebrush_v3.pdf；SHA256 0b5d54018077353172a0c2db3382c271b3e40ce8a6ba43a3d4477d864bbbe671。

均已建立同名 literature/extracted/*.txt 与 literature/metadata/*.json。页码以下用“印页/PDF 页”（PDF 页从 1 计），行号是本地 pdftotext -layout 文件的一基行号；页图用于排除上下标抽取错误。临时核图位于 tmp/pdfs/R0013/。

| 来源 | 位置 | 本地抽取行 |
| --- | --- | --- |
| Kulkarni Def16 | 20/PDF25 | 982–988 |
| Kulkarni Prop18、式(3.1) | 21/PDF26 | 1003–1018 |
| Kulkarni Prop20/Lemma21 | 22–24/PDF27–29 | 1030–1136 |
| Kulkarni Prop22 | 24/PDF29 | 1149–1176 |
| Kulkarni Lemma28 | 30–31/PDF35–36 | 1446–1510 |
| Kulkarni Lemma29、式(3.14)–(3.18) | 31–34/PDF36–39 | 1512–1636 |
| Kulkarni §3.4 算法/求和 | 34–36/PDF39–41 | 1639–1766 |
| KZ Def21 | 13/PDF13 | 733–736 |
| KZ Prop32、式(75) | 26–27/PDF26–27 | 1456 起 |
| KZ Prop37、式(89) | 32/PDF32 | 1787–1804 |
| HRZ Thm4.1/Prop4.2 | 16/PDF16 | 863–899 |
| HRZ narrow 缩放指数 | 17–18/PDF17–18 | 903–1009 |

**版本纠正。** [KZ 当前官方摘要](https://arxiv.org/abs/1902.00989v3) 明确说 v3 修正旧 Lemma 7.1；当前 maximal 数值约 **3.049**，而 Hausdorff 数值仍约 **3.059**。不能沿用旧版本/2024 thesis 中的 maximal 3.059。该区别不影响 K18 在假想 \(d_4=4\) 时仍无严格增益的算术结论。

## 3. 本轮假设与已有命题的逐项匹配

本轮 \(T\) 是所有相交轴线段的 whole \(\delta\)-cubes 的并；只以 \(Q\subset Y(T)\) 定义参与。不同来源的圆管可作常数半径扩大；必须继续保留原 \(Y(T)\) 标签，不能把新增几何相交当作新的 shading incidence。

Kulkarni Def16 对每个 shaded cube 允许任意 \(V(Q)\)，只要求所有参与管与 \(V(Q)\) 夹角 \(O(\delta)\)，没有要求它连续或沿线固定。因此其 \(n=5,k=4\) 的三平面条件没有隐藏的“平面场正则”缺口。Chapter 4 才引入 sticky；Chapter 3 命题声明没有 sticky 假设。

K18 声明逐管 \(|Y(T)|\ge\lambda|T|\)，而本轮只给平均密度 \(\bar\lambda\ge\delta^\eta\)。这个差异可付明确的微小幂成本消除：取
\[
 \mathbb T_*=\{T:|Y(T)|\ge(\bar\lambda/2)|T|\}.
\]
低密度部分的 shading 质量至多总 tube 质量乘 \(\bar\lambda/2\)，故
\[
 \sum_{T\in\mathbb T_*}|T|\ge
 \frac{\bar\lambda}{2}\sum_{T\in\mathbb T}|T|.
 \tag{A}
\]
在 \(\mathbb T_*\) 上应用任一对稀疏管族也线性含 \(\sum|T|\) 的逐管密度估计，取 \(\lambda=\bar\lambda/2\) 即可。若密度代价为 \(\lambda^b\)，得到总成本 \(c\bar\lambda^{b+1}\)。这里不声称保留常数比例的管数；其额外 \(\delta^{O(\eta)}\) 可在“先给 \(\epsilon\)、再选 \(\eta\)”的量词中付掉。

若拟调用的定理另要求 \(\#\mathbb T_*\sim\delta^{-4}\)，则 (A) 不足，必须另审。K18 声明没有这个满管数要求，故其**声明接口**允许上述操作。

**密度不自动蕴含 two-ends。** 沿每根单位管只保留连续长度 \(\lambda\) 的一段，在半径 \(O(\lambda)\) 的球内已包含全部 shading。它不能以与 \(\delta\) 无关的常数满足
\[
 |Y(T)\cap B(x,r)|\lesssim r^{\epsilon_1}|Y(T)|
\]
的固定 \(\epsilon_1>0\) 条件。即使 \(\lambda=\delta^\eta\)，仍需真实的 two-ends 缩短、重标度及方向再分离，不能直接把原 shading 称为 two-ends。

Kulkarni Prop20/22 在证明阶段要求 two-ends；Lemma21 声称消去它，Lemma23 又把二方向 robust transversality 化归掉。因此 K18 的**最终声明**不另要求 two-ends，但是否已有可无条件调用的完整证明，须连同第 7 节问题处理。

## 4. 原四维 planebrush 不能直接升为五维三平面估计

KZ Def21 的 plane 是二维；Prop37 在 \(\mathbb R^4\)、\(\Omega\subset S^3\)、逐方向管数可比、原 cubical shading 及 \((\epsilon_1,C_1)\)-two-ends 下，给式(89)
\[
 |U|\gtrsim
 C_1^{-C/\epsilon_1}\,
 \theta^\epsilon\lambda_Y^{4/3}\theta^{2/3}
 (\theta^3|\Omega|)^{1/3}(\theta^3|\mathbb T|)^{2/3}.
 \tag{KZ}
\]
Prop32 另有 robust transversality；Prop37 的作用是消去该附加要求。满量级方向和满管数时，\(\theta^{2/3}\) 对应四维 plany 下界 \(10/3\)。survey Theorem4.6 是这一四维几何的简述，不是已经写出的 \(n=5\)、三平面一般定理。

将五维三平面投影到四维，通常仍是三平面，不能调用二维 plany 条件。选择投影核落在每个 \(V_Q\) 中会降到二平面，但本轮 \(V_Q\) 可任意随 \(Q\) 变化，没有一个共同投影核；逐 cube 改投影又破坏同一条真实直线的关联。故不能由 KZ 加一个坐标的形式类比得到 (NG)。

## 5. HRZ broad 与 narrow 的精确数值断点

HRZ Thm4.1：
\[
 p>1+\frac{2n}{n(n-1)+k(k-1)}.
 \tag{H1}
\]
当 \(n=5,k=4\)，右端是 \(21/16\)，对偶维数阈值为 \(p'=21/5\)。这是 **4-broad** 估计。对满足本轮条件的 shaded 函数 \(\sum_T1_{Y(T)}\)，每个 \(\delta\)-ball 只遇到常数个原 cubes；把这些 cubes 的 \(V_Q\) 都放入 broad 定义的有限排除表（取足够大的常数 \(A\)），当 \(\delta\ll\beta\) 时，其 shaded 4-broad 量可以完全消失。不能利用原管的未着色交点，把 broad 质量强加回原 \(U\)。

Prop4.2 则要求
\[
 p>\frac{n-k+2}{n-k+1}.
 \tag{H2}
\]
在 \(n=5,k=4\) 是 \(p>3/2\)，其对偶参数小于 \(3\)，远不能把 H1 的 \(21/5\) 保留为线性维数结论。证明末尾准确的 narrow 缩放因子是
\[
 \beta^{e(p,n,k)+p\epsilon},\qquad
 e(p,n,k)=(n-k+1)p-(n-k+2).
 \tag{H3}
\]
在希望保留 \(p\) 接近 \(21/16\) 时，\(e=2p-3\) 接近 \(-3/8\)，不能按原吸收法闭合。这里是直接计算出的瓶颈，不是“broad 定理较弱”的泛述。

因此 H1 无附加 two-ends/shading 密度要求，但不是所需 narrow 定理；H2 也不因本轮角宽已经是 \(C\delta\) 就自动改善数值。

## 6. K18 的 maximal 输入在哪里；有限密度输入能替换到哪一步

Kulkarni Lemma29 将一个以 \(P=V(p)\) 为根的 \(k\)-planebrush，按法向角分入 \(k\)-平面 \(V_j\supset P\) 的 \(O(\delta)\)-邻域，令 \(E_j\) 为远离根平面的剩余原 shading。式(3.14) 有
\[
 \int_{E_j}\sum_{T\in\mathbb T_j}1_{Y(T)}
 \gtrsim \lambda\delta^{n-1}\#\mathbb T_j.
 \tag{B}
\]
式(3.15) 用 \(L^{d_k'}\) 的 Hölder；随后把该 norm 投影到 \(V_j\)，调用 \(k\) 维 Kakeya maximal，得到式(3.16)
\[
 |E_j|\gtrsim_\epsilon
 \delta^{n-1+k-d_k+\epsilon}\lambda^{d_k}\#\mathbb T_j.
 \tag{C}
\]
其输入是任意稀疏方向族及任意 \(\lambda\) 的 norm/密度界。OAI4 的 Hausdorff 结论和 SRC-001 不能直接当作这一 maximal 估计。

但若只审 **这个包内接口**，可给条件性的有限密度替代。固定 \(n=5,k=4\)，假设：

1. 包 \(\mathbb T_j\) 在同一个固定四平面 \(H\) 的 \(C\delta\)-邻域内；
2. 保留的 \(Y_j(T)\subset Y(T)\) 是原 whole-cube shading，每管密度至少 \(\lambda\ge\delta^\theta\)；
3. 允许调用条件于完整四维证明的 DIR-003 稀疏方向 dense-mark 版本，\(\theta\) 先选得足够小。

正交投影到 \(H\) 后，单位轴长度保持常数下界；其方向在常数着色后仍 \(\delta\)-分离：因为原方向的法向部分为 \(O(\delta)\)，每个投影 \(\delta\)-方向球中至多常数个原分离方向。再按有限个时间 charts 分组，并把投影 cube 集按固定常数尺度重分箱。对每根管，原 cubes 的投影只有常数重数，故每管保留 \(\gtrsim\lambda/\delta\) 个原访问时标；标签不新增。

DIR-003 因而在 \(H\) 内给
\[
 |\pi_H E_j|\gtrsim_\epsilon
 \delta^{3+\epsilon}\lambda\,\#\mathbb T_j.
 \tag{D}
\]
原 \(E_j\) 为 whole-cube 并且位于 \(O(\delta)\) 厚的单一 \(H\)-邻域内，投影有
\[
 |\pi_H E_j|\le C\delta^{-1}|E_j|.
 \tag{E}
\]
这是离散盒体积比较：每个原 cube 的投影体积 \(O(\delta^4)\)，而其原体积是 \(\delta^5\)，对原 cubes 求和即可；不要求投影 fibre 每处连续填满。由 D–E：
\[
 |E_j|\gtrsim_\epsilon
 \delta^{4+\epsilon}\lambda\,\#\mathbb T_j.
 \tag{F}
\]
此时只要求保留 subpower 密度，可以不用完整任意 \(\lambda\) 的 maximal norm，且 \(\lambda\) 代价优于假想端点 C 的 \(\lambda^4\)。

**它仍不给幂增益。** 若另有一只根刷满足文献式 Lemma28 的计数
\[
 N_{\rm brush}\gtrsim
 \lambda^3\rho\,\delta^{-1}|U|^{-2},
 \tag{G}
\]
且远离根平面后各四平面包有常数重叠，F 仅给
\[
 |U|^3\gtrsim_\epsilon
 \delta^{3+\epsilon}\lambda^4\rho.
 \tag{H}
\]
在 \(\rho\ge\delta^{o(1)}\)、\(\lambda\ge\delta^{o(1)}\) 时仍只有 \(\delta^{1+o(1)}\)。当 \(\rho\) 更小时反而更弱。这里没有重新证明整个刷提取/删除算法，也没有声称所有其间产生的包都保持上述密度；每次应用 F 必须检查这一点。

这个局部替代说明：本轮障碍不只是四维 maximal 还没有证明。即使在密度良好的四平面包上用最佳的四维有限输入，原两步刷计数的 \(|U|^{-2}\) 与环境体积因子仍停在维数四。

## 7. Kulkarni 第三章打印证明中待补证的具体位置

以下问题均查看了原 PDF 页图，不是文本抽取造成。它们不构成“Prop18 为假”的证明，但阻止本项目将其整稿标为已验证。

**(i) 删除质量的额外 \(\delta^{k-1}\)。** 印页35/PDF40、§3.4 Step2，在对与 \(V(p_i)\) 夹角为 \(\theta\) 的管求和后，写出 \(2\rho_i\delta^{k-1}\) 的删除质量上界，two-ends 一行也保留该因子。仅由 \(\delta\)-分离方向可推出的标准方向计数是
\[
 \#\{T:\angle(v_T,P^{k-1})\lesssim\theta\}
 \lesssim \theta^{n-k+1}\delta^{1-n},\quad \delta\le\theta\le1.
\]
每管处于 \(N_\rho(P)\) 的长度至多 \(C\min(1,\rho/\theta)\)。相乘后（\(n>k\) 时）只给
\[
 \sum_T|T\cap N_\rho(P)|\lesssim \rho,
 \tag{I}
\]
而不是 \(\rho\delta^{k-1}\)。打印中方向计数的 \(\theta\) 指数符号也与此不同。若还使用了额外的管数正规化或几何排除，必须显式补出；本节未找到对应假设。

**(ii) 角度求和指数变动。** Lemma29 结论、式(3.18) 的立方根给 \(\rho^{1/3}\)，印页36/PDF41 援引它时却写成 \(\sum_i\rho_i^{d(k)/3}\)。在五维本轮 \(d_4>1\) 时，后者较小，故这一方向可以作为主动削弱，但必须说明；它不能当作与原引理完全相同的公式。

**(iii) 终止条件到 \(\sum\rho_i^k\) 的比较。** 同页又写
\[
 \sum_i\rho_i^k\ge
 \sum_i\rho_i^{(1+\epsilon)/2}\lambda^{1/2}\delta^{k-1}\ge1/2.
\]
该第一比较不是对任意 \(\rho_i\in[\delta,1]\) 都成立。即使可以另用 \(\sum\rho_i^{d(k)/3}\) 与最小尺度 \(\delta\) 修复，仍要与 (i) 修正后的真实删除预算一起重算，不能只改排版后保留结论。

另一个需付费的接口：Lemma28 由“通过 \(p\) 与 \(Q_1\)”把 \((T_1,Q_1,T_2)\) 转为 \((Q_1,T_2)\) 时，打印说 \(Q_1\) 唯一确定 \(T_1\)。一般只能在 \(p,Q_1\) 有定量分离后给有限/微小幂的上界；应结合 two-ends 对近根部分的修剪记录损失。此处没有用它否定最终命题。

## 8. 对本轮真实瓶颈的可调用结论

可直接保留：

- KZ 四维二维 plany 声明与适用条件；不能把它变成五维三平面声明。
- HRZ 的 H1–H3 数值及 narrow 缩放断点；不是新的 Kakeya 估计。
- 第 6 节 D–F 的**局部有限输入替代**，明确条件于完整四维证明和包内实际 subpower 密度；有明确体积、投影及方向着色成本。
- 即使接受 K18，或者只把其 maximal 包输入理想化到 \(d_4=4\)，原指数仍不产生 (NG) 所需严格增益。

Kulkarni Prop22 的“broad”只保留定量分离的**两方向对**，Lemma28 的刷计数也基于两步路径 \((T_1,Q_1,T_2)\)。已读 Chapter3 没有给出“在同一远点的三条独立刷轴，使整个三平面方向场闭合”的三方向质量下界。root 本轮检查的三轴闭合几何若要用于 (NG)，真正新增输入必须是：从原参与 cubes、原 shading 和方向分离推出足量的这种三轴配置，并付清 two-ends/角度/退化秩损失。几何上的 span 等式本身不提供该质量。

待交叉审查重点为第 6 节局部替代的方向分离、时间标记保留和式(E)，以及第 7 节打印问题的定位。未给出 (NG) 的证明或反例，未认证文献新颖性；本轮不重开 completion 或提升形式分类。
