# R0117 辅助范围核：普通逐管 phase 删选与完整 source

2026-10-27，algebraic_gate。只核输入范围，不参与 ordinary AP-free 构造、phase 保量或其条件双向证明，不替作者认证。没有新 source 排除、ordinary 维数 gain、major 或数学 ID；未经外部同行评审。

## 1. 恢复与原文读域

运行 `python scripts/context.py`，读 GOAL/STATE/ROADMAP/registry 当前摘要、R0117 working、R0116 next、R114 whole-cell 主证及 R115 full-source graft。实读固定原件 WZ2609.22035v1 的 Def3.3、(19)、Def3.8–3.9、Def17.1–17.4、Remark17.1，另读 Lemma19.2/19.4 statements 以防误调用。数学依本地 `literature/extracted/wang_zakharov_2026_sticky.txt`，主要物理页15–17、65–66、78、81；没有新文献下载或 fresh-version/wholeproof 认证。

本轮主问题是 ordinary 全方向真实单位 δ 管、任意 marks 的长间隔近似 3AP 前端；本稿只问：其逐管删选能否被直接当作**完整 configured source 的 canonical 访问删选**。停止条件是锁出一项准确未付门，不另造 graft 或调 η/γ。

## 2. 先区分两个对象

Def17.1 的 K_d(κ) 对给定 AD/CW 整管族上的任意平均 δ^η-dense shading 声有限 lower。Def17.2–17.4 的配置则另给共同 Z、矩阵 f/tilde-f、点层 E、水平 filled X、native Y、逐点 Φ/ξ 及全部 coarse 一致性。两者不能由“管族相同”混为一个输入类。

尤其源定义的 E/Φ/ξ 不以任意外给 shading 为定义参数。Remark17.1 是从这些配置数据和 selected tube visits **生成** canonical shading，并从完整下界推出平均 δ^(Cη) 密度；不是从每条管的任意大 marks 反推该配置。

因此对一个假想完整 source 的普通 marks 做删选有两种解释：

- 保留全部原 E/Φ/ξ：原 source 仍真，但其 canonical shading 不随外给 marks 自动改变。不能把另一个 AP-free shading 的性质赋给原 canonical 访问。
- 要求新 canonical selected visits 真落在筛后原 marks 内：须给 E'、Φ'_p 及其实际原 witness，重新满足全部定义。仅有 Y'(T)⊂Y(T) 和逐管保量没有完成这一步。

若某 AP 命题的量词本来就覆盖同一整管族上的**任意** marks，可按它的 literal ordinary/Def17.1 型输入检查删选；本稿没有否定这种重调用。不能因此声 full configured class 对同一删选闭包，更不能预认证其与完整 source 排除等价。

## 3. 不同 arclength phases 没有给共同整层筛法

usual(19) 是 T={(b+zθ+w,z):z∈[-1,1], |w|≤δ}，长度固定有界，不是 arclength 恰等于1。对其轴，任意固定 arclength 起点给

    τ_T(z)=α_T z+β_T，   α_T=sqrt(1+|θ|²)。

ordinary 每管 phase s_T 的保留条件形如 α_T z+β_T∈M+s_T。它是明确定义的管内条件；**不表示物理共同 clock 消失**，同轴 AP 在仿射换 clock 后亦有对应关系。但不同 T 的 α_T、β_T、s_T 可不同，在一个源 point p 上，一些 selected tubes 可保留、另一些可被删；它不是单一的 z∈Z' 整层事件。对 δ-cubes/离轴 marks 还需 O(δ) clock 误差与实际包含账，本稿不替主作者支付。

R115 调用的 R22 整层 restriction 之所以能保 native coarse-Y lower，是每个保留 clock 的**整个 fine Y_z 和所有 filled X、stars**未动。逐管 phase 不具有这个前提，不能引用该结论冒充证明。

## 4. 哪些确实继承，哪个首先未付

下表只讨论不动 whole T、保原坐标/labels，并尝试从 surviving visits 取子数据的情形；重建坐标或矩阵不在其内。

| 项目 | 准确的继承或缺口 |
| --- | --- |
| 原 T/N、整管4AD及 whole-CW | 若原来给定则精确保留，因为整管没有改。ordinary 方向 net 本身不自动提供所需 joint-AD lower；本稿不泛称 ordinary CW 失败。 |
| 共同物理 z、原 f/tilde-f | 可继续使用原坐标和函数，其 strict dyadic variation 继承；但每管各自的大 clock 集并不直接给满足全部点层条件的共同 Z'。重新选 Z' 须按真正 surviving configured visits 计账。 |
| coarse ξ/Φ 的覆盖上半段 | 对 E'⊂E、Φ'_p⊂Φ_p 可沿用原 ξ 和原 coarse Φ_q，原 O(ρ) 及包含继续真；不能泛称 coherence 必坏。这不补 fine Φ'_p 的 AD lower。 |
| 逐点 Φ 与实际 witnesses | 首个未付门。令 Φ'_p 只保在 p 有 surviving 原 witness 的 φ；逐管积分保量不推出每个保留 p 上 Φ'_p 为 κ-AD，更不推出其每尺度 lower。若仍用原 Φ_p，删去的 tube visit 未必在新 marks 内。slab upper 按归一质量计，还须另付每个 p 的保留比例。 |
| filled X_{y,z} / tilde-X | 所需是每个保留 native y 的水平纤维 lower，不是总 I 或某管的访问 lower。各管 phase 可能在同一纤维删去不同访问，未给 #X'≥δ^(η−ℓ+1) 等条件。 |
| native Y_z、coarse time-window 的 Y-union | 固定坐标下其 AD upper/tube-KT absolute upper 可对子集继承；AD lower 不单调。重新只保有足够 X'/Φ' 的 y 后，fine lower 及全部 allowed 窗的 union lower 都须再证。 |

在 d5、k=ell3、κ1 的常用分支，每层 Y 为1AD、X 有约 δ^-2 个点、每点 Φ 为1AD并给约 δ^-1 个 witnesses，约 δ^-1 个共同 clocks 产生约 δ^-5 个 selected visits（均带允许的 δ^(Oη) 费用）。逐管或全局保住这一访问总数的一小幂比例，仍不是这些**每层、每 grain、每 point、每尺度**下界。

严格的 AD 非单调警告：A={jδ:0≤j≤δ^-1} 是1AD，B=(A∩[0,1/2])∪{1} 保至少固定比例点数。但在1的固定半径 R=1/8 球里，B 只有一个点；对任意固定 η<1，原 lower δ^η(R/δ)→∞，所以 B 不是 (δ,1,δ^-η)-AD。这个 toy 只证“保总量不能推出 AD lower”，没有声 B 支付正 γ slab 条件、由 AP phase 实现，或已经造出一个完整 source 反例；删掉孤立点等修复亦未被它排除。

## 5. 本稿止点与后继资格

准确未付门是：**把逐管 phase 后的 surviving 原访问重新组成同时满足 Def17.2(3)/(4)、Def17.4 的 E'/X'/Y'/Φ'，且让其 canonical shading 仍在原删选 marks 内。** 没有证明这个重组不可能；也没有从 ordinary 合法删选推出它总是可能。R114 已明确 mask 不保这些 fibre lower，R115 只对特殊整层保留加已逐项验证的单 clock graft 付闭包，都不补当前门。

因此 ordinary AP-free 反攻和其条件 finite 量词，须由主稿及真正独审按各自定义裁定；本稿不将它升级为 complete-source 反例、完整 source 排除等价或全部 source 的失败。Lemma19.2/19.4 另消费真实配置及整矩阵慢变化，不能凭普通 mask 或 scalar AP 缺失直接调用。

本次未发现一项已付、不同于旧闭包的原方向—空间重叠联合输入。将上述未付重组改称“joint regularization”仍只是所求的新定理，不能加作成功 hyp 或新主机制。完成范围核后停止，不续 AP 常数、graft、更多 fixed clocks 或旧 cap 形式。
