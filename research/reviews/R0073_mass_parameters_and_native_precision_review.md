# R0073 正式独审：原质量、参数与 native 精度

2026-10-18，B（lifting_obstructions）。结论为下述具名输入和完整源假设下的内部逐步审查；未经外部同行评审。

## 1. 实际全文范围与独审分工

已实际全文读取当前 root 主稿 `R0073_mixed32_native_incidence_application.md`（12节）、A 阶段II稿 `R0073_mixed32_raw_zero_and_native_source_audit.md`（12节）、B 阶段II稿 `R0073_mixed32_zero_mass_and_fine_counteraudit.md`（9节），以及阶段I A稿（8节）、B稿（7节）、working_spec（5节）、macro（6节）和 next `R0073_next_mixed42_zero_label_source_gate.md`（6节）。本审查独立核 A/root 的正证；B自己的 C4 证明不自算独审，其独立审查由 A/root承担。

本轮未新核官方 PDF/README 字节或版本，不将 R72 的实际官方核验追认作 R73 新核验。本文只审当前证明及下一题边界，不预认证未来元数据、Git、归档或同步。

## 2. light/bad 原质量、fan 与参数顺序

absolute-light 整窗门槛 `m_J<δ^a1 ρ/δ`，配合至多 `C/ρ` 个窗和原 `#Z≥δ^(η−1)`，所删比例至多 `Cδ^(a1−η)`。余窗不改变内部层或时间权。近对角先按原 `ν_J²` 删除，费用 `Cδ^(−a1)(δ^(4v)+δ/ρ)=o(δ^v)`；`ρ≥δ^(1/4)` 付离散 floor。

root/A 同一个 left 的 two-right fan 质量至少 `p²/4`。near-d 部分只有在这个原 fan 中才推出 whole `(c,d)` 簇：两条原 E 方程给 `Δc=−Δd·a_t+O(e)`。若其质量至少 `p²/8`，固定实际 t、s1 后原 rights 比例为 `cp²`；local19.4 的分母仍是原 `m_J`，而非重新归一的邻域。否则得到 d-separated anchors 和共同 left 集 `#S_J≥cp²m_J`。非零向量 `d2−d1` 乘标量 a 的恢复给整个 `(a;b)` 簇，不需要新增矩阵 rank 假设。

B 的独立 C4 路径使用 p⁴ 总量，剔除近 d 后再由平方平均提取至少 cp² 的共同 left；不是把四边质量直接记成 p²。其 local whole-tildef cap和参数余量与 root/A p² 路径相容。两种证明均未把仅 d 或仅 a 集中冒充 whole-matrix 集中。

参数顺序可实现：固定源参数及 Δ=κ+γ−1>0，先定小 β、B=3β、b*=β，再定充分小 v，随后 η 足小、a1=C0η，最后 δ。`4v≪μ(B−β−b*)`、`v≪μβκγ` 及离散 floor 条件可同时支付。最后 K 仅含原 η 的固定幂；不把坏窗反设见证 v 灌入 K。

## 3. global19.2 的合法 restriction 与新 R 分母

若坏窗总质量至少 `δ^v#Z`，各 `S_J` 原质量至少 `cp²m_J`，其 whole-time 并 W 满足 `#W≥cδ^(3v)#Z≥δ^(4v)#Z`。R22 闭包保各保留层完整的 Y/X/Φ/ξ，原 T 与 CW 分母不换；反设配置参数 `η_W=O(η+v)` 只用于产生矛盾。

取 newallowed 上邻 `ρ≤R≤Cδ^(−η_W)ρ` 后，每一个 `z0∈S_J` 只用自己的旧 `S_J` 作 whole-f 簇见证。其数量至少 `cδ^(a1+2v)ρ/δ`，而新局部分母最多 `CR/δ`，故比例至少 `cδ^(a1+2v+η_W)`。不同旧窗中心不合并，既不声整个 R 窗近常，也不把一个好窗当作 every-anchor 条件。

`η_W≪μ(1−b*)` 给 `R²≤σ_f=ρ^(1+b*)≤R`，且原 ρ 下界满足具名19.2/19.4的允许尺度。原逐层限制和每 anchor 分母均已收费，因此19.2的 CW 下界与原上界矛盾合法。最终只删整 bad/light 窗，保 Z′ 常数比例；最终重建图的参数仍为 O(η)。不同指定 ρ 可以有不同 Z′，证明未求交这些限制。

## 4. same-T pairs、完整基线与 fine δ saving

余 heavy J 上完整空间层给 `P≈_K mδ^(−4+κ)`、原 scalar Φ 供应 `D0=δ^(−κ)`，故 `I≈_K mδ^(−4)`。原 joint4AD 在 bounded joint-parameter chart 给 `#used T≤Kδ^(−4)`；没有增加物理方向 δ 分离假设。选择原 fine witness和 tube-heavy 只损固定比例 I，得到真实同一 T 的 ordered pair lower `K^(−C)δ^(−4)m²`。

fixed(t,s) upper为 `Kδ^(−4)`：先数原 root incidence，再用同管同 time 的有界点碰撞。因而原 raw tiny-pair cap可先删，费用 `Kδ^vδ^(−4)m²`，不乘 native Y cover数。这是实际 pair law 对原 time reference 的 upper domination，不是任意固定 p 的条件时间正则性。terminal是同一选中 incidence图的真实 visit。

独立展开 native 输出，基线为

    ytilde +(c_t−c_s)x +(d_t−d_s)w
      +(s−t)(ξ2,p−d_s ξ1,p)，

其角系数正是 `D=(s−t)E`。基线保留 d_s 与 p,t,s 依赖；fixed(p,t,s) 时才是可用的平移。使用实际 fine φ，故误差 O(δ)，不产生 coarse native L 的 ρ³ 项，也未调用 AFF/NQ 或 R68 大 τ 准备。

令 `ℓ=|D|≥r0`。原兼容和 dyadic-Lipschitz 给 `ℓ≤Cρ²<1`。native tubeKT给 `K(ℓ/δ)^(1−γ)` 个 fine 输出格；每格的 φ 原像长度 `O(δ/ℓ)`，scalar Φ 的 κ-upper给 `KD0(δ/ℓ)^κ` 个角。原 fine 碰撞固定倍，故 upper 为 `K^C D0(δ/ℓ)^Δ`。所有查询在原 δ base以上；用的是 κ角cap，不是较弱 γ-cap。求和得到 upper `K^Cδ^(−4)m²(δ/r0)^Δ`，而 `δ/r0≤δ^((1−B)/4)`。Δ固定后 η 最后小，确实违 pair lower。

## 5. 源责任、排重及下一题边界

本证明条件于完整 WZ Def17.2–17.4、具名19.2/19.4和 R22 whole-time闭包；这两项高级源引理的 whole proof 未在本轮重新独证。平均 incidence与逐 active tube密度分开核；whole-time删选不自动保每根原管的旧密度，故后段重计原 fine incidence并重新 tube-heavy。Φ删后只用原 upper，不授新 AD lower。

有限恢复是旧 R70 代数的转置同型，不是 ambient source 对偶或新方向。源 local/global 引理、Φ/native Y维数和 fine 计数仍需本轮已完成的独立支付。当前 spec 已明确 fine Φ/Z/点 δ 分离，未增加原 T 的物理方向分离；此范围修正已读回。

next mixed42 κ=1 只锁待证的原 AD0 label机制：native label数量次幂小不等于时间值固定，更不保证多管共享同一 label。原访问质量、共同时间集、参数仿射独立、条件数及 fine 精度，均须由完整源推出后才能抵达 CW 矛盾。若产生有理结构也须先付其源来源和分母，不能免费调用 R65 proper 类。next 未把 formal rank、更多固定时间或新增 good-tuple 公设作已证结果；未将 ordinary 四维结论偷换成任意 R5 joint4AD/CW 类的 κ≤1 归约。

本次终审未发现尚未解决的强制数学修订项。下一题的原质量/共同 label及最终 CW 出口仍是未证责任，不在本次通过范围内。

## 6. 正式结论与停止范围

在上述完整源假设与具名输入下，root/A 的 mixed32 `κ+γ>1` 排除及其 `κ=1、任意固定 γ>0` 用途，通过本次内部独立逐步审查，可按该限定范围登记 reviewed；仍未经外部同行评审。

本轮不证明 `κ+γ≤1`、一般 mixed/matrix、ordinary初始化、general-to-sticky或 ordinary R5>4/Hausdorff 增益；不声新数学ID、重大或新颖。零球阈值及 κ+γ 子范围应用按本轮停止条件归档，不以调阈值再开同义方向。当前正式稿完成后停止编辑；未来元数据/Git/sync状态不由本文认证。
