# R0013：一个真实三平面窄子类与共享时间的双块投影

2026-10-17，root。由lifting_obstructions的真实平面场攻击引出。以下是精确几何/代数接口和未闭合量词，不是(NG)证明，不声称新维数界或重大结果。不得把任意pointwise V_Q直接正规化成本节的一个全局场。

## 1. 保留原始四维方向来源的子类

对v=(b,c,d,e)在固定有界小盒内，取任意bounded anchors f(v),g(v)，考虑

    L_v(t)=(t, bt−d, ct−e, f(v)+dt, g(v)+et).          (C1)

不同v给完整四维方向(1,b,c,d,e)。该方向图在小盒上与v双Lipschitz；δ-grid因此可取δ-separated满量级δ⁻⁴方向。所有这些直线都沿着

    D_x={(a,b,c,tb−x₂a,tc−x₃a)}

运动。D_x为光滑Lipschitz三平面场，故原cubical tube的所有实际参与方向都距同cube中心D_x为Oδ。这是主(NG)的一种真实full-direction子类；任意anchors不会破坏窄条件。

但D不是常平面或可直接取积分叶的场。令X₀=∂_t−x₂∂_(z₁)−x₃∂_(z₂)，X₁=∂_(x₂)+t∂_(z₁)，X₂=∂_(x₃)+t∂_(z₂)。直接计算

    [X₀,X₁]=2∂_(z₁), [X₀,X₂]=2∂_(z₂),

与D一起张满R5。这只说明不能无依据把D当作三维叶的切空间，不提供量化体积增益。

## 2. 全部耦合都保存在一个固定参数集合中

把参数按两个块重排，定义

    P={(b,d,f(v), c,e,g(v)):v∈Ω}⊂R³⊕R³,
    D(P)={(b,d,c,e):p∈P}=Ω.

Ω有正4维测度时，P的**原方向投影**为full4；不能仅要求dim P≥4而丢掉这一来源。固定t定义

    A_t=[[t,−1,0],[0,t,1]],
    Π_t=A_t⊕A_t,
    ker A_t=span(1,t,−t²).                              (C2)

则(C1)在clock t的四维空间切片，除固定坐标重排外，恰为Π_t(P)：

    Π_t p=(tb−d, f+td, tc−e, g+te).                    (C3)

两个块严格共享同一个t，P可完全耦合；并非两个独立Kakeya问题。若P为Borel，则E_I(P)={(t,Π_t p):t∈I,p∈P}是analytic，适用标准Hausdorff切片lower。若能证明在某正测度t集合上dim_H Π_tP≥3+σ，则dim_H E_I(P)≥4+σ。这里的投影增益未证。

## 3. 一块的已知定理与不能直接tensor的原因

Fässler–Orponen, arXiv2210.09955v1，Theorem1.5/Remark1.7及§3证明，研究一块horizontal lines的union及正长度segments。我们的单块(t,X,Z)=(t,bt−d,f+dt)经固定线性变换(t,X,Z)↦(X,t,−Z/2)，恰成其参数(a,b₀,c₀)=(b,−d,−f/2)的horizontal line。原文将切片化为满足曲率条件的一参数平面投影，结论对固定Borel参数集给几乎处处的t维数。

这尚不足以对两个块直接相加：

- D(P)正4measure不保证固定第一参数块后，第二块fiber仍有dim2。实际线性例f(v)=c、g(v)=0给P={(b,d,c,c,e,0)}，D(P) full4，但固定(b,d,f)后只有e一维自由。此例本身的Π_t通常仍full4，不是投影gain反例；它严格否定所需错误fiber前提。
- 真正条件化的是同一个t下的第一**输出**A_t p₁。由此得到的第二块参数fiber随t变化；不能对它再调用“固定集合对几乎处处t”的单块定理。
- 两个marginal union分别dim3，不提供joint union维数相加。共享t与参数耦合的信息不能丢掉。
- Hausdorff/正长度segment结论没有自动给任意δ^η-dense cubical shadings所需的统一有限尺度损失。source依赖的restricted-projection theorem也未在本项目独立重证。

若P=P₁×P₂确实独立，且每P_i的方向(b,d)投影为正2measure，则单块定理的两个full-measure good-time集合可以取交，Π_tP为两个dim2切片的积，从而得到dim E=5。这个简单检查只验证独立极端；不是允许免费施加在一般anchors上的新假设，也不算主问题增益。

## 4. 可检验的下一候选；原NG仍开放

下一主候选N5-COUPLED-PROJ-01必须保留完整耦合的P，而非先假定product或条件独立。有限尺度版本可这样固定：v取满量级δ-separated四维方向网，每v仅一个bounded pair(f,g)；在固定共同clock interval内取δ时间网t_j，每j可从同一P中选subset P_j，且

    Σ_j #P_j ≥ δ^η (#P) δ⁻¹.

令N_δ为四维cube covering number。目标是某固定σ>0的

    Σ_j N_δ(Π_(t_j) P_j) ≥ cε δ^(−4−σ+ε).            (CP)

对共同clock interval内的原cubical shading，每条线在一个δ-clock slab经过O(1)个cubes，选定incidences与P_j对应到固定常数。相应|U|与δ⁵Σ_jN_(Cδ)(Π_(t_j)P_j)可比，半径常数改变只付维度常数，故(CP)正对应此子类的(NG)幂gain。δ网/方向归一化、各轴clock长度与实际单位length的常数变化须在开轮spec中固定；此处不借它们覆盖所有任意V_Q。

具体比较时，P_j由该slab中至少有一个原marked cube的indices组成。每line在slab只有O1 cubes；任一原marked cube的transverse坐标与Π_(t_j)p相差Oδ，反过来每个p∈P_j也有这样的原cube。因此原transverse cell集与投影点集双向Hausdorff Oδ，covering number只差固定因子。必须假设所计dense mass已经处在所有相关单位segments共同覆盖的固定interval内；不能从任意原dense shading免费丢掉可变endpoint tails。下一精确目标见R0013_next_coupled_target.md。

这是从真实窄几何得到的新projection机制，不是恢复formal j3统计completion。主(NG)仍未证明或证伪；即使(CP)成立也还缺从任意V_Q提取这种全局子类的定理。只给一轮尝试真正的shared-time joint估计或有效反例/明确新障碍，不反复弱化成product sanity check。
