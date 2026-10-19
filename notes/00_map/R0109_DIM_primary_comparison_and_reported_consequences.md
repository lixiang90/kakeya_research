# R0109：六维17/4的一手比较与已报告后果审定

2026-10-19，A。唯一对象是已完成 DIM001 的有限成果审定；不重证其数学、不增加递推表、不登记新 ID。本文十个编号节。数学效力、项目核验层级、文献归属和 Goal 第三出口的价值判断分别陈述；未作外部同行评审。

## 1. 恢复、实际读域与本轮问题

实际读 R109 outcome_audit_spec 五节、当前 GOAL/STATE、ROADMAP 当前主表和 R106–108 最新段、registry 的 DIM001 完整字段、当前 DIM 结果页及 R108 next6。GOAL、完整 ROADMAP 冻结历史、registry 78 项及相关 SRC/DIR/FSD/RED 字段，沿同会话 R108 刚完成的实际分块全文读域复用；没有把未读历史补写成新阅读。R108 root10、双方10节、两正式6节和 macro/next/source/round 各6节同样沿未改的实际全文读域复用，并重新全文读回 B 的 R108 正式意见。

本轮实际全文读 B 的 R109 十节。primary 新读域包括官方 4D README、官方 overview 的对应条目、原 4D §11.1–11.6 全部；实际查全文关键词，重读 KT Def6.1/Th6.2 及随后推论段、GLX Table1/上下文、HRZ §9.2/Fig5 全部。GLX、HRZ、Zahl 的官方版本核及其实际 theorem 范围沿 R108 fresh 打开记录与本轮局部读回合用。没有重新从零独证 OAI4、KT 或其它高级参考文献的 whole proof。

本轮问的是：在已付 R38 assembly/R80 retained core 后，任意集合 R6 Hausdorff 17/4 是否受到一个具体已知同类型定理支配，是否已有明确报告，以及它是否有足够实质意义进入用户 Goal 第三出口。未穷尽所有文献不是一个永久的额外数学假设。

## 2. 预先限定的一手搜索与反攻范围

搜索限定为三类：新 4D 原文及官方说明的明确后果；ordinary 高维/六维 primary 的确切 Hausdorff 表与 statement；17/4、4.25 和新 4D 引用链的有界 fresh 查询。实际执行十二个查询，分为以下三组：

- arXiv 上的 `Kakeya "17/4" Hausdorff`、`Kakeya "frac{17}{4}"`、`Kakeya "4.25" dimension`、`"four-dimensional" "Kakeya" "higher" "2026" theorem`。
- `"Kakeya" "six-dimensional" Hausdorff`、`"Kakeya" "six dimensions" lower bound`、`"Kakeya" "four dimensions" "Katz" "2026"`、`"Kakeya" "17" "4" "October" "2026" lower`。
- arXiv 上的 `"Kakeya" "six" "2026" lower bound`、arXiv/GitHub 上的 `"Every Four-Dimensional Kakeya" "17"`、arXiv 上的 `"Kakeya" "Katz" "OpenAI" higher dimension`、`"Kakeya" "17/4" "Hausdorff"`。

另对已采用 literature/extracted 库作 `17/4`、十七除四的变体、`4.25` 和新 4D 标题的全文词检。检索返回的二手网页、无关数字或摘要没有升级为可采用定理。没有新下载 PDF，没有无限扩词；若找到同类更强的具体 statement、明确同一后果或 application 错误即可否决相应声明。实际结果未取得这样的反证，不能由此推出全世界无人知道此推论。

## 3. 新四维源的当前身份与官方说明

本轮通过只读 GitHub API 实际取回 openai/math main ref 与该 preprint 目录。main 为 `1581d4cbdd69a0faf34b2089614fe2a814316a6a`；4D `paper.pdf` 为 blob `45ec20e423db2a9c70fd6303510bac361e6e9e8a`、1371486 bytes；670-byte preprint README 为 blob `b3a0eeeb593be4e7d59e6f4e6e9ecd145796e624`。这些与库存身份一致；本人的 GET 不是重新下载/重算 PDF bytes，也不是对数学正确性的身份保证。root 另做的本地 whole-byte 核不冒充本人完成。

实际读取 [September-24-2026 官方 README](https://github.com/openai/math/tree/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026) 及 [overview.tex](https://github.com/openai/math/blob/main/overview.tex) 对应 entry074。它们明确说明三维完整 maximal 与四维任意集合 full Hausdorff，未在该条目/README 中报告六维 17/4。overview 全文词检也未命中 `17/4` 或 `4.25`。这只说明被实际读取的官方说明没有明确报告，不说明标准推论不被作者理解或没有潜在优先权。

源码身份没有本轮具体版本变化可改变 DIM 的输入。也不能据 OpenAI 署名把尚未验证的 proof 当保证；此处所用效力依据是既有 RED/SRC/DIR/FSD 的 statement/application 与内部独审记录，而非署名。

## 4. 原文全部 §11 到底报告了什么

对 `openai_2026_four_dimensional_kakeya.txt` 实际全文词检，并实际读原 §11.1–11.6 整段。`4.25` 的命中是式号 (4.25)，不是十进制维数 4.25；没有取得六维 17/4 的明确文字。

§11.1 讨论四维 packing/Minkowski；§11.2 明确给任意 d≥4 的 Kakeya 集合 Hausdorff 维数至少4，并说明满维猜想要求 d；§11.3 给 RP3 受限方向集的 1+dimH D 后果及线段/全线相关返回；§11.4 是四维 constant-curvature Nikodym；§11.5 是指定 translation-invariant Bourgain phase 的四维曲线后果；§11.6 是满足 rankB=rankB²=1 的三维二次曲线借四维 lift 得 full3。上述六小节没有明确调用 KT6.2 或报告六维 17/4。

这项检查覆盖实际“后果”整节，强于只查摘要或一个数字。但仍是有限的报告范围检查；不能把 omission 证明成 implicit consequences 不存在。DIM 应准确标成该四维 finite 输入与经典递推的高维后果，不把原四维主定理据为本项目的独立原创。

## 5. 经典递推已有模板与本项目新增责任的归属

[Katz–Tao, math/0102135v1](https://arxiv.org/abs/math/0102135v1) 的 Def6.1 已把 K(n,d) 定义在任意固定 ambient 的 saturated n−1 方向族和 saturated shading 上，式(40) 明写 unsaturated 因子。Th6.2 的模板 K(n,d)、K(d+1,d′) ⇒ K(n,(2n+1+d′)/4) 是经典定理；随后正文已经迭代 real 参数族。本文没有发明这项递推，也不将重新代数代入登记成新定理。

新 4D 集合 statement 并不字面就是所有这些 finite 输入。项目实际付出的责任是 RED 的完整内部 argument/finite 读出、DIR 的原方向 cap/marks、FSD 的 arbitrary fixedambient/real angular 参数/mean λ 与 unsaturated 因子，以及任意集合 Hausdorff 返回。R38/R29/R80 的独审已支付对应 application；本轮没有重开这些 proof。

因此，“17/4 可由新输入加经典模板推出”是正确的方法归属，不能冒称新递推或新 general-n 几何；也不等于已找到在新输入出现后明确报告同一 ordinary 六维后果的文献。一个透明的标准推论仍可有实质后果，价值应按它确实排除的完整集合范围判断。

## 6. 同类型六维基线与不能混比的数字

[Gao–Liu–Xi 2503.11574v1](https://arxiv.org/html/2503.11574v1) 的 Table1 给 ordinary Euclidean R6 Kakeya 的 Hausdorff 下界 `7−2√2`，标注 Katz–Tao。表格虽然同时列 space-form Nikodym 后果，但左侧 ordinary Kakeya 列正是本次比较对象；其 Th1.5 把普通下界转移到曲率问题，不能逆读为新的普通下界。其官方 history 当前实际核到 v1，2025-03-14。

[Hickman–Rogers–Zhang 1908.05589v1](https://arxiv.org/html/1908.05589v1) §9.2 和 Fig5 也在六维列 `7−2√2`，其改善不支配这个六维 Hausdorff 数值。必须区分最大函数表：p=4/3 所推出的维数4不是当时最强 Hausdorff 基线。原文还明确 Hausdorff 与更高维 Minkowski 数值不同，不能拿后者替代。官方 history 实际核到 v1，2019-08-14。

[Zahl 2512.09397v1](https://arxiv.org/abs/2512.09397) 的实际高维综述范围与这些经典/partitioning 输入一致；它是2025年12月的综述，不是新4D输入出现后的优先权凭证。其 polynomial Wolff、broad 和 planebrush 条件也不是一个已支付的六维全类 ≥17/4 statement。本轮未将摘要中“higher dimensional”或条件类的更强结论当作普通任意集合的支配。

DIM 的 17/4 对这个明确基线的提升为 `2√2−11/4>0`，约0.078427。它是固定正指数的 Hausdorff 改善，不是只改常数、λ费用、单尺度 Minkowski、有限域或 proper 规则子类。

## 7. 当前比较究竟支持多强的文献判断

在上述十二次查询、现有 adopted corpus 词检、官方说明和原文后果整节、GLX/HRZ/Zahl 确切范围内，没有取得一个当前 ordinary R6、任意 Kakeya 集合、Hausdorff 下界 ≥17/4 的可采用 primary statement，也没有找到新4D来源或后续高维论文明确报告同一数值的实例。这是具有明确边界的阴性证据，不是不存在定理。

有限结果足以作本轮实际决定：目前没有一个具体已知支配项、同结果明确报告或 application 漏洞来否决“相对已核一般基线的严格改善”。它不支持“世界首次”“截至今天绝对最佳”“专家此前未注意”或完整 citation 网络已经穷尽。未知的潜在来源若以后给出，必须调整归属；不能为了规避这种普遍可能性而把已完成数学无限期变成 conditional。

本文不把相同新4D论文的隐含标准推论称为独立发现新 foundational theorem。准确成果陈述应说明四维来源、经典 KT 和本项目实际已核 finite/outer-measure 接口，让读者判断其贡献；不靠删除归属来放大意义。

## 8. 对 Goal 第三出口的具体正面建议

**建议本轮对 Goal 第三出口作正面审定。** 理由不是“数字变大就重大”，而是以下事实同时成立：任意 Euclidean R6 Kakeya 集合的 Hausdorff 指数固定提高；无 smooth/sticky/CW/可测/紧等额外成功假设；新输入到实际 finite 及任意集合返回的责任已被独立逐步审查；一手同类型基线明确；本轮有限反攻未找到具体支配文献或应用错误。这正符合用户 GOAL 所列“严格改进已知一般下界”的中间结果类型。

派生性要求诚实归因，不应自动把完整类固定指数改善降成无数学价值的数表重排。这里也没有因轮数、持续工作成本、作者署名、仓库 reviewed 字段或需要结束 Goal 而作判断。若只有 proper 模型、额外 desired hypothesis 或未付有限桥，本人会反对；当前证据不是这种情况。

建议认可的成果是“基于明列四维具名输入与经典 Katz–Tao 递推，且已核有限接口与任意集合返回的六维 Hausdorff 17/4 推论”。它不解决 n5 满维或一般 n 猜想，不是新递推、新 full-source 结构定理或真实反例；也不认证外部同行认可。以这些限定作一次诚实的正面决定，比没有具体异议仍永久等待所有文献穷尽更符合本轮审定标准。

## 9. 效力、核验等级和成果声明的最小分离

通常具名定理意义下，DIM 数学链有效且没有本轮识别的额外未付 statement/application 假设。完整四维外部高级 proof 未从零逐篇独证、作者形式化未本地重跑、项目未经外部同行评审，属于必须披露的核验层级。它们不能仅凭历史 conditional/false 字段重新制造 assembly gap。

成果意义是本轮基于完整类强度和有界 primary 比较的判断；首次/绝对最佳是更强的优先权声明，本人不建议采用。Goal 完成还须 root 检查用户其余归档、独审和同步要求的实际完成；本文不预认证未来 metadata、Git 或工具状态。

若后续出现具体更强同类型 theorem，应修正文献归属而不伪造原审计范围；若出现具体 application 错误，应重新打开那条错误。当前没有这样的已知证据。因此本人不给“仍可能有未找到论文”追加数学 hypothesis，也不建议下一轮继续同一泛查新/assembly 循环。

## 10. 独立交叉审阅与停止

已实际全文读 B 的 R109 十节，核其完整类结论、RED_base→SRC→DIR→FSD→KT→DIM 的无循环说明、average/逐管和 strict-subcritical/任意集合责任切割，以及重大性判断标准。与本人 actual primary 证据一致，没有发现需要 B 改正的数学类型或基线数值。B 对自己旧 proof 的回顾不充新的自我独审；现有其它代理的逐步正式记录与本轮双方相互审查须分开标明。

当前结论是正面支持 Goal 第三出口的有限成果审定；不再以同一 unknown-priority 空问悬置。尚需 root 实际全文读本稿、整合独立正式意见并完成其职责；本文不提前声称这些未来动作已经完成。没有新数学证明、新 ID、新 PDF、metadata/Git 操作或新代理。本稿到此停止扩检索，等待 root 的正式审查授权或具体纠错。
