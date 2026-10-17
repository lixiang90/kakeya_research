# R0063 工作规格：真实同轴三维载体及 planebrush 责任

2026-10-18。先有周期 macro 再施工；主命题是以下带费用估计及其 source 可用性，不预断它改善 Kakeya。

## 1. 总目标关系

检验新三维全密度 absolute-CW 输入能否改善旧 planebrush 中跨三维 carrier 的重叠责任；若合法可望成为四维 PW/更高维 narrow 部分输入。不能以已解 direction-separated 四维结果或条件局部 union 作为最终成果。

## 2. 原量词与模型

固定 bounded ambient R4、共同 affine 2-plane Pi，delta>0。Sigma_j 为包含 Pi 的 affine 3-planes，法向商 RP1 的角分离 h>=delta（允许 sector 子集）。每个 j 有原 unit delta tubes indexed family T_j，整轴近 Sigma_j，保原 labels、权 w_i、实际 Lebesgue Y_i。原方向每 Cdelta-cap 的权<=alpha，或另列足够 projected absolute-CW 的输入；不由 PW4 自动授予 alpha。各原管与 Pi 的夹角 a_i 可分 dyadic a 档。平均 lambda 与逐管 lambda 明列，不把零阴影 labels 强迫保留。原 incidence I=sum w_i |Y_i|。

## 3. 待证和传递责任

对同轴 carriers，在 dist(x,Pi)>=r 的实际点上证明 overlap<=C(1+delta/(hr))。对 angle>=a 的 tubes，删 dist<c a lambda 的脊邻域后是否可保固定比例 I，并用同一 3D projection 的 indexed absolute-CW 把各载体 lower 相加，给完整 delta,h,a,lambda,alpha 费用。若平均密度不能直接保逐管，先作明确 heavy 筛选并记录损失。所有 volume 回到 R4 原物理 measure。

## 4. 实际 source 映射

Katz–Zahl v3 Lemma30 的 Sigma(T)、W(T)、rho/p/q 及 (63)-(74) 是唯一优先 source 检查。须明确哪组原 tubes 整轴落哪个共同 affine Sigma_j、carrier 间法向分离、同轴脊是否固定、与原 quintuples 的质量关系。方向 boxes 不等于物理 carriers，选中的 paths 不等于整管 containment。若无法映射，记清具体失败而不添加未付假设。

## 5. 反例与双向闭包

独立检验靠脊薄阴影、相近 carriers、多重 labels、法向 angle 小、平均密度集中及 3D projection 重数。比较 R44/R45 固定 endpoint 和 R48/R61 rho 账本；新命题如果可直接由旧 universal gain 反复调用推出，先标 closure 而不新起方向。模型校准不冒充完整 source 或 Kakeya 反例。

## 6. 停止条件

本轮支付全部费用并完成一次 source 映射判定。若仅方向盒/近似载体而无可付整轴和质量、或所需额外结论即原 PW4 gain，立即冻结这次插入。不能续常数/阈值；本轮实际证明和校准仍需完成与独审。

## 7. 独立任务

A 只写 notes/00_map/R0063_actual_planebrush_carrier_source_audit.md，实际原文标签、全部费用、可能可行的非等价接口。B 只写 notes/00_map/R0063_coaxial_carrier_overlap_counteraudit.md，独立证明/反攻模型，保全假设。两者不 Git，不改 root 文件。root 统一整合及 formal review 再分配。

## 8. 完成与持续

本规格不是结果；具名三维输入 wholeproof 不自动认证。新 theorem reviewed 必须独立逐步审查，外部同行评审 false。每轮固定入口/登记/轮次/相关验证/提交/同步，Goal 保持 active 直到原目标真正完成。
