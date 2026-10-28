# 一般维度 Kakeya 研究

2026-10-29 R120：完成[经典解析数论应用审查](notes/90_analytic_number_theory/2026_10_transfer/00_assessment.md)。已严格周期化二次和估计，并量化其与数论l²系数预算的差别；优先研究锥分布/Dirichlet大值的新正能量，未声新的经典数论指数。114PDF/129sources，旧Goal保持停止。

2026-10-27 R119：已完成 [p-adic 类比与方法移植研究](notes/80_nonarchimedean/2026_10_transfer/00_assessment.md)。普通 p-adic Kakeya/maximal 已有解答；精确波包与条件 extension→maximal 桥可保留，临界正能量/PDE 输入尚未取得。两项模型计算已独立内部逐式审查，未声新 restriction 解或重大结果。文献108PDF/116sources。原欧氏 Goal 保持停止，本轮未创建长期 Goal。

2026-10-27：用户停止原独立续研，转读OpenAI最新全维局部光滑发布。[阅读指南](notes/60_external_results/2026_10_local_smoothing/01_reading_guide.md)说明59页新稿的主定理、辅助PDE、Kakeya全维推论与Lean核查边界。原件已存literature；本项目没有重放整套形式化，也不据外部署名自行认证证明。当前不恢复旧Goal。

以下为发现新发布前的历史研究记录，不作为当前前沿状态。

2026-10-26 R112：已完成[不同输入及原质量宏观](notes/00_map/R0112_macro_and_charged_geometric_return.md)和两独审，严格排除一个好chart直接搬原方向帽的接法；一般猜想仍open，无新维数改善。文献现93PDF/97sources。

2026-10-26：用户授权在六维17/4之后继续研究，[新Goal](GOAL.md)已启动（active）。[R0111](research/rounds/R0111.md)完成宏观重选和旧路线排重，尚无新维数改善；不能用旧17/4再次完成新Goal。[下一输入资格门](notes/00_map/R0111_next_new_input_gate.md)与[独立审查整合](research/reviews/R0111_macro_and_root_integration.md)保存当前边界。

目标：以OpenAI四维Hausdorff Kakeya预印本为起点，研究欧氏空间n≥5或一般维度。R109已按原Goal第3出口审定重大中间结果：**通常引用列明具名定理时，任意六维Kakeya集合的Hausdorff维数至少17/4**。两份独立内部终审及root接受，未经外部同行评审；一般维度满维猜想仍未解决。

[成果报告](results/reviewed/DIM-001_six_dimensional_Hausdorff_research_report.md)保存精确依赖、有限/任意集合桥及一手比较。相对已核普通六维7−2√2基线的固定改善约0.078427；不认证绝对首次、绝对最优或新递推。已归档109轮，88PDF/92sources；最终交付与Goal状态以R109实际同步回执及工具为准，提交快照不预认证未来同步。

每次恢复研究，依次读 [GOAL.md](GOAL.md)、[STATE.md](STATE.md)、[ROADMAP.md](ROADMAP.md)、[最近轮次](research/rounds/)；执行 `python scripts/context.py` 可生成精简交接摘要（识别编辑轮）；`--full`读取完整历史。摘要只作导航，研究前还须读当前spec与原proof。

## 目录

| 位置 | 用途 |
| --- | --- |
| `literature/primary/` | 原始论文，不修改原文 |
| `literature/extracted/` | 可全文检索的提取文本 |
| `literature/metadata/` | 来源、版本、校验值与下载状态 |
| `notes/00_map/` | 问题定义、已知界、文献前沿 |
| `notes/10_source_audit/` | 四维证明依赖与逐引理审查 |
| `notes/20_dimension_lifting/` | 投影、切片、纤维及归纳 |
| `notes/30_algebraic_geometry/` | 方向簇、张量测试与退化结构 |
| `notes/40_multiscale/` | 多尺度、管丛、熵与质量预算 |
| `notes/50_counterexamples/` | 候选引理的反例、失败机制 |
| `notes/60_entropy/` | 同一先验的系数熵率与信息成本 |
| `notes/70_flags/` | 多轴几何、外积目标、列表匹配与审查边界 |
| `notes/80_nonarchimedean/` | p-adic/非阿基米德模型、已知定理和方法移植 |
| `notes/90_analytic_number_theory/` | 数论应用、离散均值、格点与大值能量接口 |
| `results/` | 分状态存档的可审查结论 |
| `experiments/` | 可重复计算及原始输出 |
| `research/rounds/` | 每轮问题、证据、结论、交接 |
| `research/reviews/` | 独立审查和每三轮宏观审视 |
| `research/sync/` | 同步规程；本地同步回执放 `tmp/sync/` |

`literature` 中的论文由各自作者享有版权；复存不改变其许可。来源及核验边界见文献元数据。原Theorem1.1的完整内部argument在列明输入下已审；未独证全部外部高级文献，也不以来源署名保证正确性。依赖与核验层次见RED001及文献元数据。

## 检索与复现

```powershell
python scripts/context.py
rg -n 'Lemma 6.6|11.2' literature/extracted
rg -n '状态|阻碍|下一步' notes results research/rounds
python experiments/algebra/tensor_kernel_probe.py
```

GitHub: https://github.com/lixiang90/kakeya_research 。每轮结束必须提交并验证远端；同步未验证时如实保留待同步状态。


## 论文源码（2026-10-26）

[中文版](papers/six_dimensional_17_over_4/main.tex) · [English version](papers/six_dimensional_17_over_4_en/main.tex) · [双语完整源码包](papers/six_dimensional_17_over_4_bilingual_sources.zip)。两版均由内置LaTeX编译器核验成功；保留完整项目目录。编译说明与范围见[papers/README.md](papers/README.md)，源文件哈希见[papers/manuscripts.json](papers/manuscripts.json)。此为既有DIM-001的编辑整理，R110当时无新数学Goal、作者署名或对外投稿；R111依用户新请求另开研究Goal。
