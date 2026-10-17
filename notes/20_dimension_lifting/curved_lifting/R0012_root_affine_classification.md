# R0012：codimension-one空间仿射lift的完整局部判别

> **R0050范围更正（2026-10-17）：** 下文保留开轮/历史论述。对目标 `w+F(t)y`，在同一个参数点沿同一条lift直线取第一变分，可构造同codimension和方向rank的真正全时affine lift。因此一般smooth与affine的**存在性等价**，旧文“空间affine为实质限制/一般nonlinear未排除/需逼原π affine”的判断不再成立；原π本身仍可真正非线性。完整更正见 [R50主证明](R0050_variational_equivalence_and_full_smooth_lift_classification.md)，当前登记为 `results/reviewed/LIFT-005_full_smooth_variational_classification.md`。不新增ID或重大性声明，换clock/selector/Θ依赖w等边界保留。

2026-10-17。作者root；在独立阅读source与working_spec后推导，主rank障碍与两位代理独立推导一致。最终稿已由lifting_obstructions逐步独审通过，见research/reviews/R0012_affine_classification_review.md；不以本稿自证代替独审。不声称新颖性或重大结果。

## 定理及精确边界

令m≥2，B∈Mat_m(R)，F(t)=tI_m+t²B。在具有内点的y,w∈R^m、ρ∈R以及非退化时间区间I上，考虑任意光滑

    π_t(z)=T(t)z+c(t),  T(t)∈Mat_(m×(m+1)), rank T(t)=m,
    a(y,w,ρ), Θ(y,ρ)∈R^(m+1),

满足全部t和参数的coherence恒等式

    T(t)[a(y,w,ρ)+tΘ(y,ρ)]+c(t)=w+F(t)y.       (1)

这里Θ独立w，D_(y,ρ)Θ在某内点rank m+1。则若B≠0，必有

    rank B=rank B²=1.                         (2)

反之，B=0或(2)成立时，存在全参数的上述lift，且方向rank处处为m+1。因此对Definition2.1的保留原时钟、空间仿射(1,0)-lift，存在性等价于

    B=0 或 rank B=rank B²=1.                  (3)

原任务m=2、B=diag(1,2)不满足(3)，所以不可能。这覆盖任意光滑T,c,a,Θ，不先假定它们对参数线性，也不先假定π=x+tUz。结论只关于空间仿射、保留原时钟的类。非线性π、时间重参数及仅针对一个不规则selector w(y)的较弱lifting问题均未被排除。

## 1. 完整平移参数强制共同右逆

固定一个方向fullrank的内部参数点(y*,w*,ρ*)。对(1)关于w微分，因Θ独立w，得到

    T(t)A₀=I_m,   A₀=(∂_w a)(y*,w*,ρ*),       (4)

对全部t成立。A₀是固定的(m+1)×m矩阵，rank m。取一个固定向量k，使L=[A₀,k]∈GL_(m+1)。进行同一个常数空间坐标变换z=Lz'，a'=L⁻¹a，Θ'=L⁻¹Θ。于是

    T(t)L=[I_m,h(t)], h(t)∈R^m.                (5)

常数GL变换保coherence、slope独立w和完整方向rank。以下全部导数都在该参数点取值；省略撇号。没有作依赖t的lift坐标变换，故线仍是a+tΘ。

## 2. 两个参数导数消去任意光滑h(t)

写固定导数为

    ∂_y a = [C; r],    ∂_y Θ = [D; ℓ],
    ∂_ρ a = [p; u],    ∂_ρ Θ = [q; v],

其中C,D∈Mat_m，r,ℓ为1×m行向量，p,q∈R^m，u,v∈R。对(1)分别关于y、ρ微分，c(t)直接消失，得

    F(t)=C+tD+h(t)(r+tℓ),                     (6)
    0=p+tq+h(t)(u+tv).                        (7)

u+tv不可能为零多项式。否则u=v=0，由(7)可知p=q=0，于是完整方向Jacobian的ρ列∂_ρΘ=0，违反rank m+1。

将(6)乘u+tv，并用(7)消去h，得到全部t成立的矩阵多项式恒等式

    (u+tv)(tI_m+t²B)
      =(u+tv)(C+tD) − (p+tq)(r+tℓ).           (8)

此步骤从未除以u+tv，故无分母零点或ruling在某时刻退化的遗漏。右边次数至多2；比较t³项得到vB=0。若B≠0，则v=0，进而u≠0。再比较t²项得

    uB=−qℓ.                                  (9)

所以rank B≤1；B≠0时恰为1。这已完成B=diag(1,2)的全指定类不可能证明。任意非线性的a,Θ在这里仅通过一点的导数进入，不能逃过此必要条件。

## 3. 完整方向rank排除nilpotent秩一

继续比较(8)的t项：

    uI_m=uD−pℓ−qr,
    D=I_m+(p/u)ℓ+(q/u)r.                     (10)

该点的方向Jacobian是

    J_Θ = [[D,q],[ℓ,0]].                      (11)

将上面m行减去(p/u)倍最后一行，再将前m列分别减去最后一列乘r/u，都是可逆、行列式为1的操作，得到

    [[I_m,q],[ℓ,0]].

故

    det J_Θ=−ℓq=u trace B.                    (12)

fullrank迫trace B≠0。对秩一B=xℓ₀，B²=(ℓ₀x)B=(trace B)B，所以这等价于rank B²=1。特别B≠0且B²=0时虽有标准(1,1)-lift，却没有本类的(1,0)-lift。没有把方向loss悄然丢掉。

## 4. 两个充分性构造

若B=0，令π_t(x,z)=x，a=(w,0)，Θ=(y,ρ)。每条line投影为w+ty；D_(y,ρ)Θ=I_(m+1)，是合法(1,0)-lift。多出的坐标被π忽略，但Θ仍有全部独立方向；source定义允许此情况。

若rank B=rank B²=1，取B=xℓ₀且ℓ₀x=trace B≠0，定义

    π_t(x',z)=x'+t x z,
    a=(w,ρ),  Θ=(y−xρ,ℓ₀y).                 (13)

直接展开π_t(a+tΘ)=w+ty+t²By；T=[I_m,t x]始终rank m。

    D_(y,ρ)Θ=[[I_m,−x],[ℓ₀,0]],
    det D_(y,ρ)Θ=ℓ₀x≠0.                      (14)

所有域可取小compact balls并在其邻域延拓，线段支撑包含于合适open Ω，source的coherence/domain要求均满足。此充分性是source Proposition2.5(i)的秩一特例；新增必要性证明覆盖了任意光滑空间仿射投影。

## 5. 与总目标的距离及停止规则

对n=3、B=diag(1,2)，本类codimension-one降低不成立。标准codimension-two lift仍存在且用到R5直线输入；此处没有证明所有类型的lift都需要R5，也没有得到三维曲线新维数界或五维Kakeya新界。

B=λI_m≠0、m≥2也不能在本类拥有(1,0)-lift，但可经τ=t+λt²换元直接化直线。这不是矛盾：本定理保留原t，严格排除时间换元。必要性使用了全部w的平移族及Θ独立w；若只研究一张w(y)选线图，(4)未必存在，不能援引本定理免费否定。

本轮已从标准rank公式推进到整个指定类的必要充分性，信息增益明确；但它仍是一项局部提升障碍，不是最终目标。归档独审后停止该窄类，不继续围绕其系数或等价normal form做琐碎优化。下一项必须由宏观审视选择实际Kakeya几何任务。
