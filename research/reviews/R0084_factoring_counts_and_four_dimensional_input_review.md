# R0084：真实 factoring 计数、原质量与四维输入正式审查

2026-10-18，A。内部逐步审查，未经外部同行评审；不认证新数学 ID、重大性、普通高维新界或未来 metadata/Git/sync。

## 1. 实际全文对象与独审分工

本次 fresh 实际全文读 root《R0084_actual_convex_factoring_input_gate》九节、A《R0084_convex_factoring_polynomial_count_audit》八节、B《R0084_factoring_shading_and_full_PW_counteraudit》八节、working_spec 五节、最终 macro 六节、next《R0084_next_full_goal_reselection》六节，以及 literature/notes/R0084_convex_factoring_sources 六节。已读回 root §1 的 K_N/logN 范围、A §2/7 的修订及 macro §2 最后修复。

原文实际读域是 Hong Wang [ICM2026 官方 HTML](https://epubs.siam.org/doi/full/10.1137/25M1806156) §6 的定义、Lemma6.10、后续形状讨论及 Conjecture6.14；库存 GWZ streamlined v2 §2 相关定义、§3 heredity、§4 Lemma4.1 完整 proof/Remarks4.2–4.3/Definition4.4、§5 Proposition5.1 statement、Lemma5.9 完整 proof、Remarks5.2/5.10，以及末次补读 Lemma5.11 完整 statement/proof；另核 LPSW v1 Lemma4.5、Proposition5.1/Lemma5.3 的实际量词与尺寸。没有将本人的读取范围扩大成 GWZ 49 页全 proof、LPSW 全文或 OAI4 全部高级证明。

A 参与 bounded-parent／containment 推导，不将自己的稿件视为自身独审。该正算已由 root/B 实际全文核；本 formal 独立重点是 root 整合和 B 的质量、partial-PW、投影及校准链。这里的内部限定通过和源高级 theorem 的具名责任、外部同行评审是三件不同的事。

## 2. 原分母、平均密度与 assigned partition

root/B 正确保留原 N、I=λNv_δ 及 E=∪Y(T)。平均 λ 先删 density<λ/2，再选一个 dyadic density层；保 incidence I0≥I/polylog，不能同时无条件保同一比例的 cardinal。层上各管密度可比后，count-factoring 才保 I′≥I/polylog 和 N′≥λN/polylog。逐管已有 lower 的输入则整 label restriction 直接保该 lower；两类闭包没有混写。原 shading 始终完整保留且新 union⊂E，直到另行定义 induced parent shading。

GWZ proof 输出的关键是 assigned partition T′=⊔C_P、C_P⊂T′[P]。计算 mM≈N′ 用 partition；没有将其升级为几何上每个 child contained 于 O(1) parents。B/root 的归属求和相同，均允许实际几何包含更多 parents。

原 direction-separated N 根 fine tubes 只有 absolute 系数 C_Dδ^(1−n)，normalized K_N=C_Dδ^(1−n)/N；N 不满时不能写成 O(1)。若无 N 上界而允许 arbitrary indexed 输入，factoring 的 logN 费用须保留，不能一概称 polylog(1/δ)。这些限定在 root §1、A §2、B §2 均已写明。任意跨度原权的无损 factoring 未被本轮偷偷加入。

## 3. Bounded parents 与上下 containment 计数逐式核

独核 root/B 的 boundedness：relative convexFW 在 P∩B_R 处给 |P∩B_R|≥|P|/L。任意轴的最大截面积 A 与 width w 满足 |P|≥wA/n、|P∩B_R|≤2RA，所以所有 width≤2nRL；因 P 与 B_R 相交，全部 parents 落共同 O(RL) 球。absolute convexKT 再给 Mv≤L^{O_n(1)}。closure/极限处理不取到截面最大值即可，parent 含正体积 child 排除了退化零体积。GWZ greedy 可选择 convex hull 容器的交叉验证也成立；未免费剪 parents 后继承其 KT。

对半代数 W，m#P[W]≤Σ_{P⊂W}#C_P≤#T′[W]≤K_NN|W|，配 mM≈N′ 得 normalized parent 系数 L^C K_N(N/N′)。absolute parent 系数再乘 Mv。固定 P 共用一个 affine frame，其逆像体积≈v|W′|，child 系数同样只多 Nv/m≤L^C N/N′。仿射代入保固定格式且不要求 P 自身半代数；不能给不同 child 各选 frame 后继续称同一测试。

上列是 finite containment 的真实应用，不是新的 Kakeya 增益。原全称输入经合法 restriction 再调用已经给出此类继承；generic maximal-density factoring 也早在库存 GWZ 中，未以新综述名称另注册。

## 4. Partial PW、原 shading 与 B 反攻

若原本有 all-λ partial-PW，则固定 C_P 的 restriction 与共同 affine image 可按同一 volume/mass 因子继承；这是 R42/R43 已付闭包。B §6 同形 parent 的共同核 μ_P≤C μ_T*k_CQ 成立：x∈P、z∈T⊂P 时 x−z 落共同扩大盒，卷积在 P 上有所需 lower；平均 assigned children 后仍是同一核，可用旧 restricted-mean 证明。该正输入未被误判为旧失败。

但一般 variable-shape/orientation kernels 不是共同核；parent 的 partial event 也不直接授 children 对同一 S 的事件。B 的 parent 空半部测试严格展示这种“同 S 收回 child 事件”步骤无凭，不是对某个充分 λ-loss 的普遍定理的反例。B 中心全方向 bush 的未增厚 shading union≈λ^n，也只否 parent density 免费等于 λ；它不反 near-full/subpower lower，更不反 GWZ 的 induced thickening。

真实 GWZ5.9 给的是 P∩N_{w1}(∪Y) 的密度与 compatible multiplicity，不是原小 footprint 的免费父影。其 planar Córdoba overlap argument 在 R3 已付；Remark5.2 明确高维所需 R^(n−1) 输入，LPSW 已推广的 v1×v2×v3^(n−2) 类也不含 n5 初始 δ^4×1 ordinary tubes。当前证明没有抹去这项维度与形状责任。

已 fresh 读回 root §7 最后新增的正面特殊范围，并独核 GWZ5.11：fine round tube T⊂round coarse T_ρ 时，直接体积比较给 |T_ρ∩N_ρY(T)|≳(|Y(T)|/|T|)|T_ρ|；不需另授 children relativeFW。uniform／同层密度及既有 refinement 后 parent density 可保 ≳λ。这是旧 round coarse-tube 的真实正接口（甚至不必要求 fine/coarse 轴严格相同），与 R43 相容；既不被本轮否定，也不能推广为 arbitrary anisotropic factoring parents。

## 5. 四维调用、参数费用及已修强制项

一般 convex children 增厚最短 parent 宽后，其 R4 投影仍可能为 planks；relative convexFW，甚至额外 fixed-format polynomial containment，都没有直接给 DIR003 的实际四维 slope-bin cap、round graph-tube、near-full marks 与端点条件。对初始圆管，在非短投影情形 projected w1-cap 的原 count 至多 C(w1/δ)^4；正确归一是先除实际 m_P，再以 L^C N′v 作 lower。A §7 已改为

    α_P ≤ L^C(N/N′) w1^4/(Nδ^4v)。

原版本把 m_P 与 Nv 误写为可直接比较，已按全类保守账本修正；slab 语句也保 N/N′。即便原 Nδ^4≈1，shape v 与新尺度密度仍须支付，不能将 slab 特例扩成全部 parents。R53–55 已审投影、纤维、原帽及 incidence 求和的费用并未在本轮消失。R4 CW-alone quadric 障碍不反 ordinary，也不把 polynomialFW 自动升级成已知 OAI4 输入；Conjecture6.14 不能当 theorem。

第二处实际修复为 macro §2：旧“保 N/polylog”已改“先 densitylayer，N′≥λN/polylog、I′≥I/polylog”。已 fresh 读回，root 主稿 §3 原先就保有此损失。A §2 无 N 上界时保 logN 的澄清也已核。修后无未解决强制项；不能把修正后的 subpower 费用又在摘要抹掉。

## 6. 最终限定结论与停止

限定通过：root9/B8 的原质量、bounded parent、assigned-partition containment、旧共同核 partial 正闭包及当前 4D 输入不匹配判断，均在上述实际量词下可成立。A 正算已由 root/B 独核，本 formal 不以本人重读代替其独立性。没有完整 parent-shading／variable-kernel 新定理、ordinary gain、full PW4 解决或新反例；拒 phaseII 与本轮输入证据相符。

最终 macro6/next6 全文 scope 通过：ordinary 初始化、directHRZ、matrix/mixed 与 full-direction 真构造四路保留；下一主命题诚实未选定，不以 desired father-density／PW4 公设改名，不续旧常数或形状模板。主 gain/branchsaving streak7 是保守记录，不能因新网页来源归零；Goal active。

ICM 正式 PDF 本机下载失败、web screenshot cache miss 仅记录 root 的真实工具结果；本人没有获得或视觉核验该 PDF，也没有复核它的本地 hash。本文只依 actual HTML 与已存 GWZ/LPSW 对应正文，不认证未来 metadata、PDF 计数、Git 或同步。具名高级 wholeproof 未新独证，未经外部同行评审，无新 ID／重大性／优先权声明。
