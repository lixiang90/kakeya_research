# CPJ-001：共享时间闭环的联合方向秩约束

2026-10-17，R0014。内部交叉审查通过，未经外部同行评审；不声称新颖、重大或新的Kakeya维数界。完整证明在notes/40_multiscale/coupled_projections/R0014_joint_attack.md §§2–4和R0014_cycle_rank_hierarchy.md。独审research/reviews/R0014_joint_attack_review.md、R0014_cycle_hierarchy_review.md；root复核R0014_root_integration_review.md。

令Π_t=A_t⊕A_t，ker A_t=spanγ(t)，γ=(1,t,−t²)，t∈I=[1/4,3/4]。原参数图每个δ-separated四维方向只有一个bounded anchor pair。k个参数vertices以互距至少ρ的times依次joint-close，误差≤ε，首尾闭合。

三个γ列的逆范数≤5ρ⁻²。每条参数边=γ(t_i)⊗u_i+Oε，u_i为两块第一系数的原差。因而：

- 三环全部vertices距同一点O(ερ⁻²)，精确三环不能有不同参数线。
- 四环全部方向距同一affine2-plane≤500ερ⁻²；该plane由原固定首边u₁决定，不随后续times变化，也无需除首边大小。u₁0时全部vertices在同样小球。
- ε=Cδ时，固定首边所有eligible四环的其他vertices，只能来自≤C min(δ⁻⁴,ρ⁻⁴δ⁻²)个原方向。
- 五环方向距某affine3-plane为O(ερ⁻²)，plane可依整个环。精确kernel由barycentric weights w,tw张成，方向边在span((a,0),(b,a),(0,b))中；a,b独立时rank3。
- 六环已允许full4方向仿射rank。取t_i=1/4+i/12、q=(-1,5,−10,10,−5,1)、u_i=sq_i(1,t_i²)，第五有限差分使全部moments闭合，方向边为sq_i(1,t_i²,t_i,t_i³)，rank4。取s小得到真实单位轴及不同方向，可加入同一D场满方向补全；不是小union构造。

近环稳定先修正最后三条边的moment残差，再回到原vertices，损失仅O(ερ⁻²)，不会因barycentric weights再乘ρ⁻⁴。修正点不被加入原P或原shading。

依赖只有显式线性代数、Vandermonde/Lagrange及原方向packing，无OAI4条件。尚未给出足量time-separated有效cycles的原质量下界；同time大bush及重复times不在禁例中。不得把这些上界当CP/NG证明，亦不继续逐边增加polygon作为主要研究。
