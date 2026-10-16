# LIFT-005：保留原时钟的空间仿射codimension-one提升分类

2026-10-17，R0012。内部独立审查通过；未经外部同行评审，不声称新颖性、重大结果或Kakeya维数改善。

令m=n−1≥2，X_B(w,t;y)=w+(tI_m+t²B)y。允许任意光滑T(t),c(t),a(y,w,ρ),Θ(y,ρ)，ρ为一维，要求

    π_t(z)=T(t)z+c(t), rank T(t)=m,
    T(t)(a+tΘ)+c(t)=X_B(w,t;y),
    Θ独立w，rank D_(y,ρ)Θ=m+1.

时间区间非退化，参数域有内点，coherence对整个参数域成立。这是Definition2.1的保留原时钟、空间仿射(1,0)-lift。则存在此lift的必要充分条件为

    B=0，或 rank B=rank B²=1.

特别n=3、B=diag(1,2)不可能在这个整个任意光滑类别中由四维直线lift实现；不是仅排除标准π=x+tUz的公式。

证明核心：对w求导产生固定共同右逆，常数ambient GL变换后T=[I,h(t)]。在一个方向满秩点对y及ρ求导，写成

    tI+t²B=C+tD+h(t)(r+tℓ),
    0=p+tq+h(t)(u+tv).

乘u+tv消去h而不作除法，右侧次数≤2，t³项给vB=0。B≠0时v=0且u≠0，t²项给uB=−qℓ，故rank B=1。方向Jacobian经行列消去的det为−ℓq=u trace B；fullrank又迫trace B≠0，即rank B²=1。B0及非nilpotent秩一的充分构造直接给出。

完整证明：notes/20_dimension_lifting/curved_lifting/R0012_root_affine_classification.md。另有独立的全类障碍稿R0012_affine_lift_obstruction.md及局部核正规形攻击稿R0012_construction_attack.md。独审：research/reviews/R0012_affine_classification_review.md、R0012_construction_attack_review.md；root整合复核见R0012_root_integration_review.md。

本结果不排除一般非线性空间submersion、时间重参数或仅针对一张selector w(y)的lifting。标量B经τ=t+bt²化直线的例外与本定理不矛盾。标准B=diag(1,2)的(2,0)-lift仍有效，其五维输入并未被本分类证明。归档后冻结该窄类细节，不继续等价normal form或系数优化。Goal active。
