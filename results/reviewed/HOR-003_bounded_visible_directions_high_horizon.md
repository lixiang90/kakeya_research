# HOR-003：实际可见方向密度有界仍无uniform horizon上界

2026-10-17，R0011。内部交叉独审；未经外部同行评审，不声称新颖性、重大中间结果或Kakeya维数改善。结论仅涉及literal j3 version2拟推广的模型类。

## 否定的精确命题

固定L>0、d₀=1/2、S=1及angular范围。对每个任意大的固定M>6L，存在单world完整8维tempered概率prior，actual f(r)≡0，native P*=w、B=1，selected mass1/4，原visible-slope law的实际Lebesgue density ceiling为O(1)，且

    M/6 ≤ H(E) ≤ M.

因而N5-DIR-COST-01所拟H≤C_(d₀,S,angular)(L+κ)不成立，甚至κ=0；常数不能独立于任意tempered complexity exponents。固定L=1使M任意大，排除了所有有限C。即便同时限制f0=0和实际可见density有界，形式all-model horizon/length supremum仍无限。

## 构造与证明入口

λ,s∈[1,2]、p,q∈[−.1,.1]的δ格点均匀混合，δ≈N₀⁻ᴹ；固定α=.1，取

    b=(s,−sq−λp/s,λ/s), u=(p,αλ−pq,q),
    B=b+ξ, V=u+ζ,  ξ,ζ独立均匀于[−δ,δ]³。

每层配一次性固定的随机存在性tag cλ，再取w₀=cλ+η盒噪声、W∈[η,2η]均匀独立，η≈N₀⁻ᵁ、U>M+L+10。无噪声恒等式

    tY₂+Y₁Y₃=λ(1+αt²)

使exact base只接收O(1)层，故f≡0/S1全部保留。同时，实际V₁,V₃先定位O(1)个p,q，V₂再定位O(1)个λ；三格点权δ³与三速度noise densityδ⁻³抵消，得到实际density ceiling O(1)。

每层只是HOR-002轨道沿e₂增加αλt；任意whole/short-block空间fit拉回时只平移affine center，D与J不变。R0010统一随机标签引理对新的固定层law重新选一张好表，给全部二次charts、任意assignments同时成立的

    m/q ≤ K^C[a_L+(log N₀)²δ^(1/2)q⁻³]J + N₀^(-ω(1)).

与原floor比较得H≥M/6；q=δ的good midpoint cube×原w₀-bin真实atlas给H≤M，覆盖常量、own-list O(1)，不输出内部λ。

完整主证：notes/50_counterexamples/R0011_direction_smoothing_attack.md §§1–8。独立接口稿：notes/40_multiscale/plank_inputs/R0011_direction_cost_positive_audit.md。交叉审查：research/reviews/R0011_direction_smoothing_review.md、R0011_visible_cost_interface_review.md；root整合独核：R0011_root_integration_review.md。R0010随机引理及其独审仍是明确依赖。

## 边界与路线处置

完整(V,W)的density ceiling仍≈η⁻¹=N₀ᵁ。本例缺少真实五维完整方向来源，不是Kakeya集合反例、不反驳原j2四维稿。也不能据此否定专用source条件下的DIR-003。

按既定停止规则冻结整个visible-direction-cost completion策略；不继续添加同义统计条件或优化这些模型的H指数。下一轮转向新曲线lifting的具体几何检验N5-CURVE-LIFT-01，见R0011_macro。长期Goal仍active。
