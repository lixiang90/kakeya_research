# NAR-001：真实满量级方向下沿富集轴的旋转三平面

2026-10-17，R0013。内部交叉审查，未经外部同行评审；不声称新颖性或重大结果。完整构造见notes/40_multiscale/narrow_five_dimensional/R0013_geometric_attack.md；独审research/reviews/R0013_geometric_packet_review.md，root复核R0013_root_integration_review.md。

对所有充分小dyadic δ，存在同一固定有界盒内R5的Euclidean单位线段族、δ-separated方向、#T≈δ⁻⁴，取全部相交whole δ-cubes为T且full marks Y(T)=T。每个参与cube Q的全部方向都距某3-plane V_Q为Oδ。一根central tube在正比例δ-cubes中有≈δ⁻²参与方向，但任意固定3-plane只能以Oδ误差包含O1个这些rich cubes的全部方向。

具体使用D_x={(a,b,c,tb−x₂a,tc−x₃a)}及L_(b,c,d,e)(t)=(t,bt−d,ct−e,f+dt,g+et)。hot directions为(b,c,τb,τc)，anchors f=−τ²b,g=−τ²c，经过Pτ=(τ,0,0,0,0)。固定τ的δ⁻²方向迫plane靠近Eτ=span(e1,e2+τe4,e3+τe5)。gap(Eτ,Eσ)=|τ−σ|/√((1+τ²)(1+σ²))。hot directions扩成满四维direction cap的maximal δ-separated集，所有实际新增incidences继续满足D窄条件。轴clock取[0,1/|(1,u)|]保证实际单位长度。

这严格排除“full source加一根持续rich轴就强制plane沿轴近常”的捷径，即使允许Lipschitz plane field。它**不反驳N5-NARROW-GAIN-01**：补全方向取f=g0给|U|≈1；hot tube mass仅Oδ，central hot incidence mass仅Oδ²。因此允许从全局删除小质量的averaged兼容性估计仍开放。

依赖只有显式直线、方向packing及有限维线性代数，无OAI4输入。没有新的Hausdorff或Minkowski界；不是Kakeya集合反例。
