# R0111：2026-10-26 一手前沿、来源身份与重启资格核验

日期：2026-10-26（Asia/Shanghai）。执行者：独立 frontier_audit 代理。只更新本文件和对应 baseline review；不修改公共状态、registry、文献 catalog 或原 PDF，不提交 Git。本文是有界来源审查，不是文献中所有高级证明的重新证明，也不认证世界首次或绝对最优。

## 1. 恢复范围与先锁问题

实际读取 GOAL、STATE；ROADMAP 当前主表与冻结记录的本次工具可见范围；registry 顶层当前状态及 R0109 成果字段；DIM-001 成果报告；R0109 一手来源审计与完整 primary comparison；frontier_sources 的身份/核验政策和相关 metadata；R0081/R0085 macro 及 R0108 primary reselection。没有把一次截断的全 registry/ROADMAP 输出冒作全部历史的新阅读。

本轮只问：相对于 R0109 已付的六维 17/4，当前一手来源是否产生一个真正新增、可适用到 ordinary Euclidean 高维 Hausdorff 的输入？若没有，就不能把旧全 real 参数递推、改题名、有限域/曲线结果或搜索阴性算作新数学机制。

独立否决条件预先为：发现具体更强同类型 theorem；发现已明确报告相同六维后果的 primary；发现来源版本变化；或者拟议任务由旧统一命题经合法 restriction/shading 重调用直接推出。停止条件：完成以下有界实际检索和精确域核验后不无限扩词；无合格输入即报告 no qualified input。

## 2. OpenAI 四维原件的 fresh 身份

实际浏览 [官方 repository README](https://raw.githubusercontent.com/openai/math/main/README.md) 和 [四维 preprint README](https://raw.githubusercontent.com/openai/math/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/README.md)。后者仍列作者 OpenAI、稿件日期 2026-09-24。官方 root 说明这些是内部模型产物，核验阶段不一，未形式化稿件可能有问题；作者和文件身份均不保证证明正确。

另用 GitHub connector 的只读 GET 实际读 [main ref](https://api.github.com/repos/openai/math/git/ref/heads/main)，再读固定 commit 的 [preprint directory metadata](https://api.github.com/repos/openai/math/contents/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026?ref=1581d4cbdd69a0faf34b2089614fe2a814316a6a)。结果：

| 项 | 本轮实际返回 |
| --- | --- |
| 官方 main | `1581d4cbdd69a0faf34b2089614fe2a814316a6a` |
| paper.pdf Git blob / bytes | `45ec20e423db2a9c70fd6303510bac361e6e9e8a` / 1371486 |
| 稿件 README blob / bytes | `b3a0eeeb593be4e7d59e6f4e6e9ecd145796e624` / 670 |
| 本地 paper.pdf bytes / SHA256 | 1371486 / `30d0c186aa9c697d02ab9bf736968028f1ce8a2f164f1d7291398d530035ccde` |

本地大小和 SHA256 用 Get-Item/Get-FileHash 重新计算，均与 R0109 完整字节证据一致。此次没有下载远端 PDF，也没有重新对远端 PDF bytes 计算 SHA256；fresh directory blob 未变支持沿用既有 whole-byte 身份记录。起初 PowerShell HTTP 因套接字权限失败，随后 purpose-built GitHub 只读 connector 成功；失败结果没有当作身份确认。

实际重读本地 extracted abstract、原 §11.1–11.3（原 PDF 标页 168–169 的文字），并核四维主结论的既有结果报告。原 §11.2 已明确任意 d≥4 的 Kakeya 集合 Hausdorff≥4，特别包括五维。它没有支付 4D maximal，更不直接免费支付所有 KT finite seed。本轮不重做 RED/SRC/DIR/FSD 的已审内部接口。

## 3. 同类型普通六维基线

fresh 打开 [GLX arXiv history](https://arxiv.org/abs/2503.11574)（仅 v1，2025-03-14）、[HRZ history](https://arxiv.org/abs/1908.05589)（仅 v1，2019-08-14），并实际读 GLX HTML Table 1 及其转移语境、HRZ HTML §9.2/Corollary 9.1/Figure 5。两份表在六维均明确列 ordinary Euclidean Hausdorff≥7−2√2，归 Katz–Tao；该数字不是本轮新界。[GLX Table 1](https://arxiv.org/html/2503.11574v1)、[HRZ §9.2](https://arxiv.org/html/1908.05589v1#S9.SS2)

因此，已完成 DIM-001 的 17/4 相对这个明确同类型基线确有严格差值 `2√2−11/4≈0.078427125`。该比较保留任意 ordinary 集合、Hausdorff 和具名 theorem 使用的范围。curved/Nikodym、maximal 指数、Minkowski 和规则子类强结论不能与它混比。

表格确切行也给五维 18/5、七维 34/7、八维 11−4√2；新四维输入已使五维至少4。不能把一份2025表的历史4D数字当2026当前最佳，也不能由这里的有限审查认证所有高维当前最佳。HRZ Corollary 9.1 是无穷多个维数上的 `(2−√2)n+3/2−1/√2−ε`，并非每个 n 同一强化公式。

## 4. KT 是既有递推，不是重启后的新机制

fresh 读 [KT 官方 history](https://arxiv.org/abs/math/0102135)（仅 v1，2001-02-16）及 [原 HTML Def6.1、(40)、Theorem6.2 和随后的迭代段](https://arxiv.org/html/math/0102135v1)。原定理为 `0<d<n` 时 `K(n,d)` 与 `K(d+1,d′)` 推出 `K(n,(2n+1+d′)/4)`；定义和 (40) 包含 fixed ambient、方向 cap、saturated shading 与 unsaturated 数量因子，不能仅凭集合 Hausdorff statement 免费取得。

项目 R29/R38 已付这些 finite/任意集合接口。R0081 macro 又已明确全 real affine envelope 的迭代及 n8/n10 数值均在旧输入闭包内；R0085 再冻结其改名。新用户要求继续研究不抹去这些失败/重复指纹。本轮不登记新递推、新 n 表、新数学 ID 或新重大成果。

R0109 检查过原 §11.1–11.6 全部及官方说明，未找到明确写出六维 17/4 的文字；本轮没有把它冒作重新逐页全读。此次 fresh 搜索也没有取得同果的可引用 primary，但仍不排除作者或其他人已知该标准推论。KT 自身已有相同函数递推模板这一事实必须正面归属，不能以“没有搜索结果”改变它。

## 5. 本轮实际搜索、读域与阴性证据边界

实际执行12个有界 web 查询，分3批、每批4条（搜索结果用于定位，所采用判断仅依 primary）：

1. `Kakeya Hausdorff dimension higher dimensions 2026 four OpenAI six 17/4`
2. `Kakeya higher dimensional Hausdorff 2026 arxiv new lower bound`
3. `site:github.com/openai/math "four-dimensional" Kakeya`
4. `site:arxiv.org Kakeya "4.25" OR "17/4"`
5. `site:arxiv.org Kakeya "Hausdorff" "2026" "higher"`
6. `site:arxiv.org Kakeya "2026" "dimensions" lower bounds`
7. `site:arxiv.org "Kakeya" "five" "2026"`
8. `"Kakeya" "17/4" "Hausdorff"`
9. `site:arxiv.org "Kakeya" "Submitted on" "Oct 2026"`
10. `site:arxiv.org "Kakeya" "Hausdorff" "Sep 2026"`
11. `site:arxiv.org "Kakeya" "higher dimensions" "2026" -Heisenberg -curved -P-adic`
12. `"Kakeya" "multiscale" "2026" "Hausdorff"`

除 §2–4 的精确来源外，fresh 打开 [Zahl survey 2512.09397](https://arxiv.org/abs/2512.09397)、[Guth Bourbaki 2604.03416](https://arxiv.org/abs/2604.03416)、[Zhang mixed-norm BL 2608.17952](https://arxiv.org/abs/2608.17952)、[Choudhuri 2610.12480](https://arxiv.org/abs/2610.12480)。实际读 history/abstract/声明的当前返回域，未重新全文独证。Zhang仍 v2=2026-08-19；Choudhuri页面只有 v1，并显示日期2026-08-30（标识号与日期看似不一致，本轮如实记录，不擅自改正）。这些均已在库存对应 metadata，不能再以检索命中日期冒新采用。

搜索还命中已筛曲线 lift 2609.06299、p-adic 2609.22485、Du 曲线压缩2610.05404、CC-geodesic 2607.26906和二手全维 claim。它们没有此次可采用的 ordinary Euclidean Hausdorff 新 theorem。p-adic 全维结论不能跨度量直接使用；曲线压缩不能当直线 full-direction 反例；升维 implication 不能倒用。对这些命中本轮只定位/对照库存，不声另一次全文证明审查，不需要新下载 PDF。

检索覆盖不穷尽 arXiv、作者网页或所有隐含推论；未命中不是无结果，更不是创新性证明。本文不宣2026-10-26绝对 frontier 已认证，也不改变 DIM 原文献归属。

## 6. 重启选择：本次没有合格新机制

本轮未取得足以重开旧110轮路线的新增 primary 输入。尤其：全 real KT envelope、4D projected seed 的再调用、regular-leading G4片的 DIR4应用、p-adic/有限域借名转移、曲线 lift 和新方向题名都不能当新机制。

一个未来真能改变主幂的任务须具体支付此前未有的量：例如 actual full-source 上、在任意合法 restriction/shading 后仍保原质量的联合非集中或原共同轨道恢复。此句只是准入标准，不是本轮推出的结构定理，也没有给它另起名称、数学ID或宣布已锁 working candidate。其 average density、逐管 density、逐点与逐 clock 责任必须分开。

建议本轮如实采用 **no qualified new primary/mechanism** 的有限审查结果，保留已有六维成果、更新用户新 Goal 的完整目标和下一可证伪资格门。若 root 从独立数学审查获得真正不同且未在闭包内的命题，再单独锁定；不能仅因为用户要求继续便重开旧数表或给原难点换名。

## 7. 本轮未核项目

没有重新阅读四维175页全部证明、全部高级外部源、全部92项catalog，未本地重跑作者形式化，也未外部同行评审；来源声称、已有项目内部审查与本轮网页身份/声明审查分开。未做新数值实验、未注册新结果、未下载新PDF、未操作同步。对应 review 只审本轮来源证据与基线资格，不是对 DIM wholeproof 的重新独审。
