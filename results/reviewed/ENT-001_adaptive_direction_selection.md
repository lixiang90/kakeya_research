# ENT-001：适应方向事件的熵与列表成本

日期：2026-10-16，R0004。状态：内部独立复核通过，见research/reviews/R0004_boundary_entropy_review.md。未经外部同行评审，不声称新颖性。

完整证明见notes/60_entropy/R0004_full_slope_selection.md。固定同一概率律及有限原始方向网格S，父/多项式label A，point/history Z，各label方向事件Ea。令p=P(S∈EA)、q=Σa PA(a)PS(Ea)，则

p log(1/q)≤I(S;A)+h(p)≤I(S;Z)+H(A|Z)+log2。

同一law上almost-sure大小L列表给H(A|Z)≤logL。列表仅在后续submeasure上成功时，须先支付选择成本并保持原palette，不可免费沿用原prior信息界。

若另有同一joint domination P(S,Z)≤Kπ(S)PZ(Z)，且所有π(Ea)≤ε，则不论全局A数多少，都有p≤KLε。原始完整方向密度可估事件参考质量；仅有已选parent的可见球cap不能替代该输入。

这些是可检验接口，尚未从真实临界路径获得所缺的完整斜率似然控制或小信息成本。完整W方向熵必须与V在同一原始分辨率上记账，并保留已有祖先label成本。没有新的Kakeya维数结论。
