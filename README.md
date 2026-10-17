# 一般维度 Kakeya 研究

目标：以OpenAI四维Hausdorff Kakeya预印本为起点，研究欧氏空间n≥5或一般维度的证明、证伪或重大中间结果。已完成四十二轮归档研究与内部审查，**尚未解决高维猜想或取得经确认的重大中间结果**。

R30–38在具名输入下完成四维内部论证及finite/Hausdorff接口审查。R42全局复核后新增锐polynomial-Wolff文献，核算原权与共同仿射/短clock费用，明确实际sticky极值类没有免费方向分离祖先；尚未建立新五维增益。下一唯一任务测试原§18粗化、重新赋权和递归在加强类中的闭包，一轮失败即停。文献31篇PDF/34条来源；六维17/4的已审条件推论链仍未获新颖性或重大性认证。

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

`literature` 中的论文由各自作者享有版权；复存不改变其许可。来源及核验边界见文献元数据。原Theorem1.1的完整内部argument在列明输入下已审；未独证全部外部高级文献，也不以来源署名保证正确性。依赖与核验层次见RED001及文献元数据。

## 检索与复现

```powershell
python scripts/context.py
rg -n 'Lemma 6.6|11.2' literature/extracted
rg -n '状态|阻碍|下一步' notes results research/rounds
python experiments/algebra/tensor_kernel_probe.py
```

GitHub: https://github.com/lixiang90/kakeya_research 。每轮结束必须提交并验证远端；同步未验证时如实保留待同步状态。
