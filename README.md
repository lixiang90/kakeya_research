# 一般维度 Kakeya 研究

目标：以 OpenAI 四维 Hausdorff Kakeya 预印本为研究起点，寻求欧氏空间 n >= 5 或一般维度猜想的证明、证伪或重大中间结果。已完成三十二轮研究与内部审查，**尚未解决高维猜想或取得经确认的重大中间结果**。

R0032完成原Lemma3.5两版本的真正terminal extension内部重证及交叉独审（TEX-001），包括旧观察的短标签列表、整段轨迹分配和原序列复杂度控制；原3.1–3.4工具已由TCM/ASM认证。这些均为来源已有结果的核验。完整四维证明及其它输入尚未全面独审，compact六维17/4仍是条件结论；未认证无条件新界或重大性。文献20篇PDF。下一轮先宏观审视当前前沿和路线，再决定critical-path候选。

每次恢复研究，依次读 [GOAL.md](GOAL.md)、[STATE.md](STATE.md)、[ROADMAP.md](ROADMAP.md)、[最近轮次](research/rounds/)；执行 `python scripts/context.py` 可生成精简交接摘要。

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
| `results/` | 分状态存档的可审查结论 |
| `experiments/` | 可重复计算及原始输出 |
| `research/rounds/` | 每轮问题、证据、结论、交接 |
| `research/reviews/` | 独立审查和每三轮宏观审视 |
| `research/sync/` | 同步规程；本地同步回执放 `tmp/sync/` |

`literature` 中的论文由各自作者享有版权；复存不改变其许可。来源及核验边界见文献元数据。对 OpenAI 原文的全面正确性尚未完成独立审查；依赖它的结论须注明条件。

## 检索与复现

```powershell
python scripts/context.py
rg -n 'Lemma 6.6|11.2' literature/extracted
rg -n '状态|阻碍|下一步' notes results research/rounds
python experiments/algebra/tensor_kernel_probe.py
```

GitHub: https://github.com/lixiang90/kakeya_research 。每轮结束必须提交并验证远端；同步未验证时如实保留待同步状态。
