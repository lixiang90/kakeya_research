# CPJ-002：真实满方向数据的未修剪平方能量障碍

2026-10-17，R0014。内部交叉审查通过，未经外部同行评审；不声称新颖或重大。完整计数在notes/40_multiscale/coupled_projections/R0014_joint_attack.md §§5–6；独审research/reviews/R0014_joint_attack_review.md，root复核R0014_root_integration_review.md。

Ωδ取四参数固定小盒内的常数倍δ-grid，#P=N≈δ⁻⁴且实际单位方向δ-separated。anchors f=−τd,g=−τe，τ=1/2。原Euclidean单位轴共同覆盖I。令X=(b,c)、Y=(d,e)、h=t−τ，则共享时间输出为(tX−Y,hY)。取全P_j=P，或只在|h|≤λ=δ^η保原全部indices，0<η<1。

原output cell重数n_j(Q)给S=Σn≈λδ⁻⁵；未修剪E₂=Σn²满足

    cδ⁻⁶ ≤ E₂ ≤ Cδ⁻⁶.

lower来自距τ最近的midpoint时间：输出只Oδ⁻²cells；upper来自每index joint-close partners≤C(|h|+δ)⁻²，时间求和Oδ⁻²。因此统一E₂≤Cδ^(−6+σ)、固定σ>0，**对原全部marks不成立**。普通Cauchy的数值仅S²/E₂≈λ²δ⁻⁴。

这不是CP反例：每时刻实际cover≈δ⁻⁴(|h|+δ)²，窗口总cover≈δ⁻⁵λ³。若删除|h|<s，δ≪s≪λ，原incidence仅损O(s/λ)，余下E₂≤Cδ⁻⁵s⁻¹；取s=δ^a、a+2η<1可在此例获得gain。所以它不排除保留原质量后的truncated方法。

没有改变anchors、没有独立两时间、没有丢方向来源；反驳的是未经修剪的能量捷径，非主CP/NG。新的任务须证明任意原数据中的可保留低重数质量，不能把该尚未证结论加作假设后宣布成功。
