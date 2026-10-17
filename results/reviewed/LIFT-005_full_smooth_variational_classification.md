# LIFT-005：参数线性曲线族的全光滑提升分类

2026-10-17，R0050更新既有LIFT-005，不新增ID。R12仿射分类已内部独审；本次第一变分及范围纠正的实际逐步审查见下列R50两份review。未经外部同行评审，不声称新颖性、重大结果或Kakeya维数改善。

## 1. 精确量词与变分等价

令m≥2，F(t)为固定smooth矩阵函数。时间为非退化共同区间I，y,w∈R^m、ρ∈R^s各域有内点；光滑π_t定义在容纳全部线段的共同开域，空间rank m。要求Θ=Θ(y,ρ)独立w，且

    π_t(a(y,w,ρ)+tΘ(y,ρ))=w+F(t)y

对全部参数和全部t成立；方向rank为m+s−ν。则这种一般smooth lift存在，当且仅当存在同s、ν的空间仿射且参数线性的lift。

证明：固定同一个内点P，取T(t)=D_zπ_t(a(P)+tΘ(P))。对w、y、ρ一次微分得到

    T a_w=I， T(a_y+tΘ_y)=F(t)， T(a_ρ+tΘ_ρ)=0.

这些是整段t的精确恒等式，所有a/Θ导数均取同一P，故是常矩阵。以Da(P)u、D_(y,ρ)Θ(P)(u_y,u_ρ)为新的截距、方向，以T(t)z为新投影，即给出真正全时lift。T满秩，方向rank不变；小compact参数balls的线段位于适当共同开域。反向affine是smooth子类。

结论是**存在性等价**，不是原π被迫affine；对一般非参数线性目标不作此断言。

## 2. 二次族的codimension下界和可达性

对F(t)=tI_m+t²B，固定右逆a_w后作常数空间基变换，T=[I,H(t)]。写a_y=[C;R]、Θ_y=[D;L]，得到

    P(t)=t²B+t(I−D)−C=H(t)(R+tL)，rankP(t)≤s.

当s<m，每个(s+1)-minor在I上恒零，所以作为多项式恒零；最高次系数就是相应B-minor。因此s≥rankB。s≥m时平凡。这里不要求H解析，不作无穷时间延拓，也不使用ρ的满秩条件。

源Prop2.5(i)以B=UV、s=rankB给π_t(x,z)=x+tUz、a=(w,ρ)、Θ=(y−Uρ,Vy)，方向loss ν=s−rankB²。故在**允许方向loss、保原clock、全w且Θw=0**的上述类中，最小codimension恰为rankB。不是曲线Kakeya集的最小Hausdorff维数。

## 3. codimension-one完整方向分类

对s=1、ν=0，存在上述一般smooth lift的必要充分条件仍为

    B=0，或 rankB=rankB²=1.

必要性在同一P将导数写成a_y=[C;r]、Θ_y=[D;ℓ]、a_ρ=[p;u]、Θ_ρ=[q;v]。消去T=[I,h(t)]给

    (u+tv)(tI+t²B)=(u+tv)(C+tD)−(p+tq)(r+tℓ).

u+tv不为零多项式，否则Θρ=0。B≠0时t³系数给v=0、u≠0，t²给uB=−qℓ。方向Jacobian行列式经常数行列操作为−ℓq=u trB≠0，所以rankB=rankB²=1。B0及非nilpotent秩一的旧充分构造有效。

特别m=2、B=diag(1,2)的所有此类smooth lift都要s≥2；(1,0)不存在，标准(2,0)仍存在。

## 4. 校准、来源和停止

原π确可非线性。例如B0时π_t(z)=(z1+z3²/(1+t),z2)、a=(w1−ρ²,w2,ρ)、Θ=(y1−ρ²,y2,ρ)；在|t|<1/2全参数coherence成立且方向det1。B=diag(1,0)亦有真非线性例，完整展开见主稿。不能将本结果解释为π本体的线性刚性。

主证明：notes/20_dimension_lifting/curved_lifting/R0050_variational_equivalence_and_full_smooth_lift_classification.md。独立施工：同目录R0050_nonlinear_lift_source_and_rigidity_audit.md、R0050_nonlinear_lift_construction_counteraudit.md。本次实际全文独审：research/reviews/R0050_geometry_and_source_review.md、research/reviews/R0050_construction_and_rank_review.md；root整合见R0050_root_integration_review.md。

真正source为Nadjimzadah arXiv2609.06299v1 Def2.1/Prop2.2/2.5。2511.10918/GAFA00750-4是另一篇文章。source的forward应用不是逆向R5证明。仅selector、Θ依赖w、换clock、非参数线性目标均不由本结论排除。旧LIFT-005仿射页及R12三稿保留历史并加更正说明。

本轮是已有证明的范围和存在性等价纠正，不新立结果或重大性声明。此窄类停止，不续Taylor/Hessian/normal-form或相邻clock参数轮。Goal active。
