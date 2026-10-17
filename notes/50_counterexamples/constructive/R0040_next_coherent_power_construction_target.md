# R41 唯一下一任务：真实 all-directions 构造的相容幂次检验

2026-10-17，R40提前macro选择。待研究目标，不是已知可实现的参数选择，不登记新命题ID。来源为已入库 Fernandez-Delgado–deLaSalle2607.14824v3 的实际 Kakeya construction；原定理只给 logarithmic neighborhood-volume upper，不是维数反例。下一轮读其完整相关 construction 与 estimates 后再尝试修改，不自动重新审无关高级输入。

## 命题与量词

优先 n=5。是否能在该真实构造的多尺度参数/复制规则中，给出 c>0、有界 compact K⊂R5、r_j↓0、固定 C，使每 v∈S4 存在 a_v，且

    {a_v+t v:0≤t≤1}⊂K,
    |N_{r_j}(K)|≤C r_j^c  对所有 j？

没有方向可测选择假设；每方向存在完整单位段必须逐一证明。可令 0<c<1 以兼容已知至少四维的必要底线；这不是假设它存在。若构造需要别的固定 n≥5，需说明为何该维度本质必要，不悄悄改目标。

同一个 K 的子序列 neighborhood upper 足够反 Hausdorff conjecture：grid cubes 给 N_{r_j}(K)≤C r_j^{c−5} 个 O(r_j) cubes，s=5−c/2 时总 s-cost≤C r_j^{c/2}→0，故 dim_H K≤5−c/2<5。若更直接给同一 K 的合法 s-covers 也可，不强加全尺度 Minkowski upper。

## 有限 stage 到最终集合的桥

若首先定义 K_j/tube unions，必须给同一最终 K、全部方向、bounded centers 和 unit lengths。必须证明 K⊂N_{C r_j}(K_j) 且 stage upper 在该固定倍 radius 有效；或给另一个真正覆盖 K 的 estimate。仅 compactness 抽子列不自动保证 d_H(K,K_j)≤r_j，不能把随 j 的不同集合体积当同一 K 的 cover。

若用嵌套紧集，每层允许的 direction/center fibers 应有非空相容链；网方向近似须在极限保持每个给定方向及单位长度。若有 anisotropic scaling/translation/复制，逐项记录体积、半径、directions、长度、复制数及误差的乘加预算。不可将每层成功后验重归一后宣称方向全集仍满。

A 的本轮 scope 核查指出：原 Definition5.2 采用 compact/unit segments，Lemma5.3 是 Gδ 的单尺度输入；Proposition5.4（PDF18–19）本来就有相容紧集桥，Theorem1.3 使用 f(C_d δ^{1/4})。所以不能预称“没有现成 compact bridge”：下一轮先逐项核5.4的实际假设；若新的全小尺度构造确实满足它且有 f(r)≤Cr^c，原桥的1/4损失仍保正幂。真正新增义务是严谨的新 power-saving 构造及其适用性，不是重命名原5.4。该处目前仅 scope 识别，未认证新构造存在或已适用。

## 合法删选与排重

任意 tube restriction 不保所有方向，任意 set restriction 不保单位段。可按有限方向图分块，但其并必须覆盖 S4 并付 overlap/union 费用。正密度 directions 不等于全部 directions；小 neighborhoods 正体积不等于小 Hausdorff dim。原FD log upper与候选power upper不可混为同一结论。

本目标直接修改真实 Kakeya 构造，不调用旧 CP/PM、matrix-time增长或LPSWsource-to-flake全称正增益作为假定，因此不是它们的同义命题。若实际修改退化为上述旧全称难题或仅循环固定 log 压缩，则立即说明并冻结，不新增结果ID。

## 独立反攻与停止条件

反攻须同时检查：每个方向是否缺失；nested fiber 是否真的非空；累计长度/方向误差是否有界；最终集合是否 compact/bounded；所算小体积是否实际覆盖同一 K；fixed c 是否被 ε_j→0 或复制数抵消。有限算例仅覆盖有限代数模型，不认证连续极限。

只作一主轮。验收为完整候选与真实极限/cover桥，或此前未支付必要步骤的严格失效机制。若结果仍只是原 log upper，或不能保同一 K，或 fixed power 只在丢方向/长度后出现，则记录失败并macro重选，不继续 ε、网格、常数小改动。任何疑似反例先独立全文审查及一手文献比对；未经这些步骤不称重大/新颖/猜想已解。
