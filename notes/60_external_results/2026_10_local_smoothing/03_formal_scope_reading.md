# 全维局部光滑发布：Lean 题面、解答与核验范围

2026-10-27，local_smoothing_formal_scope。按用户新指令解读外部成果，停止原 Kakeya 续研。本文是公开材料的范围核对，不是本机完整 Lean 重放、整篇证明独审或外部同行评审。所有 openai/math 链接固定在 commit `7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a`。

## 1. 确认不是只有低维或 sticky 版本

已实际读取官方 [范围说明 lean/docs/079.md](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/docs/079.md)、独立题面、解答模块、Comparator 配置，以及主定理和 Hausdorff 桥的源码。

- 局部光滑题面量化所有整数 n≥2、有限实数 p≥2。对 Schwartz 初值，控制半波在 R^n×[1,2] 的 L^p 范数，Sobolev 阶为 max{0,(n−1)/2−n/p}+ε，ε>0；p=2 还允许 ε=0。因此它不是只陈述 n=3，也没有把所有临界端点都宣为 ε=0。
- Kakeya 极大函数题面控制单位线段的开 δ 邻域平均，先对所有中心取 supremum，再在单位球面方向上取 L^n。对每个 ε>0，存在常数 C，使全部 0<δ≤1 和全部 L^n 初值满足 Cδ^(−ε) 的界；常数可依 n、ε。
- 集合维数题面是：对每个 n≥2、任意集合 F⊂R^n，若每个单位方向都有一条真正单位线段包含于 F，则 dim_H F=n。没有 measurable、compact、sticky、方向子族或正密度附加假设。这正覆盖原项目所研究的通常 Euclidean Kakeya 集合问题。

这些定义及量词可直接在 [参照题面 LocalSmoothing.lean](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/ComparatorChallenges/LocalSmoothing.lean) 的对应六个目标中核对。范围说明还列出 Bochner–Riesz、球面 restriction、Stein square function 的严格范围及三维对数管体积改进；本稿不将这些额外结论逐项当作独立完成证明。

## 2. 题面中的 sorry 不能当成解答漏洞

`lean/ComparatorChallenges/LocalSmoothing.lean` 是 Mathlib-only 的独立参照题面；六个目标以 `sorry` 留给解答，这是 Comparator 的正常设计。它不是作者声称已经补完的证明文件。

对应 [LocalSmoothing.json 配置](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/ComparatorChallenges/LocalSmoothing.json) 明确指定另一个 solution module：`OAI.Analysis.Fourier.LocalSmoothing.Comparator`。本次已实际完整读取这个 [真正的解答模块](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean)：六个证明都转接到现有 development 的定理，未在本文件使用 `sorry`；文件也不 import 独立 Challenge。

配置没有 `definition_names` 形式的定义空洞，只列六个 theorem targets。允许的公理恰为 `propext`、`Quot.sound`、`Classical.choice`，即通常的 Lean 经典数学基础；没有许可 `sorryAx` 或把局部光滑/Kakeya 结论本身列为新公理。这是明确的核验目标设置，不能仅凭配置文本就断言本次已经成功重放。

## 3. 实际源码中可见的证明依赖

[LocalSmoothing/Main.lean](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/OAI/Analysis/Fourier/LocalSmoothing/Main.lean) 的主链为：已经构造的 positive packet solvability → logarithmic refinement → Euclidean local smoothing。另实际读取 `WavePackets/PositivePacketSolvability.lean`，其声明从 constructed Dirichlet family 取得物理 packet 解及局部光滑性，不在主定理中外加“假设某 PDE 有解”的 premise。本次没有逐一审查其全部传递依赖，所以不据此代替 PDE 全证明审查。

[Kakeya/Main.lean](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/OAI/MeasureTheory/Kakeya/Main.lean) 明确从 local smoothing 调用 restriction-to-maximal，再以 maximal 推集合维数。这个 implication 在 [Kakeya/Hausdorff.lean](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/OAI/MeasureTheory/Kakeya/Hausdorff.lean) 中不是仅一句“Minkowski 所以 Hausdorff”：它利用任意 Hausdorff 小代价球覆盖、方向上的线段占用 lower 和 maximal 给出的 cover-sum upper，排除每个 0<s<n 的 Hausdorff measure 为零，再推出 dim_H=n。源码特别允许覆盖集不具备可测、有界或闭假设。

## 4. 本次实见证据与未做的核验

可确认的层级是：官方范围文字确实声称全维结论；独立参照题面明确写出通常定义；真正解答模块存在并转接到对应数学定理；配置限定通常公理；主链和任意集合 Hausdorff 桥源码可公开阅读。

官方 [Comparator README](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/lean/ComparatorChallenges/README.md) 给出安装 Comparator、landrun、lean4export 后运行验证的指引。Comparator 工具自身的说明区分“核对题面、允许公理、Lean kernel 接受”和“只编译到一个含未证公理的目标”。本次没有安装/重建整个 Lean 库、运行该配置或独立 replay 每个依赖，也没有将一个 GitHub 文件 hash 当作形式正确性证据。

`lean/formalization.yaml` 将上述六个 LocalSmoothing 目标列入 formalized-main-results，其全库 review 状态仍标 `unchecked`；这是所读元数据的字面状态，不等于已经外部同行评审，也不能反过来推断作者报告的 Lean 检查失败。当前措辞宜为“OpenAI 已公开自然语言稿和全维 Lean 形式化，并报告完成形式化；本项目已核范围和主要公开接口，尚未在本机独立重放”。

## 5. 适合固定归档的小文件

下列均已通过 GitHub connector 在上述 commit 实读；blob SHA 用于定位版本，不替代证明。

| 仓库路径 | Git blob SHA |
| --- | --- |
| lean/docs/079.md | e6ea535832d6dfef60c539a2e0537b560c1b7108 |
| lean/ComparatorChallenges/LocalSmoothing.lean | 9e712197a604ecb440b9dade7469ef44ba5f716a |
| lean/ComparatorChallenges/LocalSmoothing.json | 88c1e1c3368f66f9d64206a2b166a89bc87b4f9b |
| lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean | 6def181857b8148d9dbaed288876a225ca9ddbfb |
| lean/OAI/Analysis/Fourier/LocalSmoothing/Main.lean | 3b95ea013123b96932afb88cc11e6aa1579c59ed |
| lean/OAI/Analysis/Fourier/WavePackets/PositivePacketSolvability.lean | ce4d5eea7655bbb4beb5a45c36124bd5a231d4e6 |
| lean/OAI/MeasureTheory/Kakeya/Main.lean | 14441e0b9ef840955ca38ba802441b26ac73c179 |
| lean/OAI/MeasureTheory/Kakeya/Hausdorff.lean | 05fa717c044ea326081acab039c2f2cf652a8f2c |

本稿只解释外部成果的范围与证据，不登记本项目新定理、优先权或重大结果，不恢复原研究 Goal。
