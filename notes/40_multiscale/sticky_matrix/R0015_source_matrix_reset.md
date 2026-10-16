# R0015：从等价局部目标返回真实五维矩阵配置

2026-10-17，root，宏观选题的一手接口审计。不是新Kakeya结果。CP/PM子类已因等价量词关闭局部迭代；本稿选择不同的实际多尺度输入，而非把其inverse或entropy重命名。

## 1. 真实五维分支，保全部source假设

Wang–Zakharov, arXiv2609.22035v1（已存117页PDF），§2.3、Definitions17.2–17.4和Proposition17.2表明：其sticky问题的临界亏损若正，可构造若干(k,ℓ)-配置。本项目没有全面重证该约化，调用继续标明source条件；一般δ方向分离族不自动满足AD/sticky。

五维d=5的一个未由其已写特殊分支处理的情形是k=ℓ=3。它有实际δ-tubes的(4,δ⁻η)-AD正则、convex Wolff常数≤δ⁻η，以及：

- f:Z→Mat(2,2)，Z为δ分离且#Z≥δ^(η−1)，f在source指定离散尺度dyadic Lipschitz。
- E_z={(x,y+f(z)x,z)}，x∈R²的grain充分填满，Y_z⊂R²为(δ,2−κ,δ⁻η)-AD正则；source还要求跨时间尺度的Y联合正则。
- 每个原点p有ξ_p∈R²和κ-AD的Φ_p⊂R²，原管方向为(φ,ξ_p+f(z)φ)+Oδ；这些原管/Φ_p/ξ_p保Definition17.2(4)的跨尺度相容，不能只留点态场。
- Φ_p为γ-slab Frostman，Y_z为(1−γ)-tube Katz–Tao。这些是原配置数据，不能换成任意小体积集合，也不能从CP的full方向图自动赋给它们。

完整正式定义仍以原PDF65–66页为准；上列不是删除细节后的替代定义。

## 2. 已有矩阵线性分支；真正未写出的非线性替换

原§20.1从原V/L-tuples给

    y₁−y₂=(z'−z)(f(z)−f(z'))(φ₁−φ₂)+Oδ.             (M1)

Lemma20.2（PDF86–87）已对任意d,k的Mat(d−k,k−1)陈述和证明局部affine情形：若ρ∈[δ^(1/4),δ^μ]，在dense时间子集上f(z)可被rz+u以ρ^(1+ε₀)|r|精度拟合，则C_CW(T)≥δ^O(η+ε)ρ^(-κ)。这包含Mat(2,2)，不应再把整个矩阵分支称作无现有输入。线性lemma依赖Lemma19.2、V-tuples及tube Katz–Tao，后续非线性分支另用L-tuple计数；这些接口仍须在最终定理使用前核清。

Lemma20.3（PDF88–89）却只处理Mat(1,d−2)。它用标量Theorem13.5把Y_z的标量slice推到维数接近1，和其1−κ维AD正则矛盾。d5/k3时Y_z维数2−κ，特别κ<1时，任何单个标量投影的满1维都不足以构成矛盾。两个不同投影各满1维也不自动令同一Y_z满2维，必须保原联合图及其多尺度质量。

因此下一检验是**完整真实配置下的Mat(2,2)非线性Lemma20.3**，而不是再要求某种没有来源的matrix irreducibility，也不是此前光滑D场CP的改写。即使成功，也只处理五维sticky的一个关键分支；(3,2),(4,2),(4,3)等mixed配置、一般管到sticky的步骤及Hausdorff覆盖仍未解决。

## 3. 新存矩阵和积文献：可参考的工具与真实门槛

新增原件：

1. Weikun He, [Discretized sum-product estimates in matrix algebras](https://arxiv.org/abs/1611.09639v2)，v2日期2017-10-17，29页。读§1.2 Theorems2/3及其条件说明，查看PDF3页原图；未重证全文。
2. Weikun He–Nicolas de Saxcé, [Sum-product for real Lie groups](https://arxiv.org/abs/1806.06375v3)，v3日期2021-01-27，23页。读Definition2.1、Theorems1.1/2.3/2.4与Proposition2.5的声明，查看PDF6页原图；未重证全文。

He Theorem2在简单实代数中要求系数集远离所有proper subalgebras；Theorem3的作用版本要求定量不可约。结论分别是A+A及A+AA的增长，或X+X及X+aX的增长。不能只看题名就把(M1)当其输入。

He–de Saxcé Theorem2.3允许可约表示，但要求各Jordan–Hölder商上的系数不集中、远离proper stabilizers的identity components，且X远离proper submodules；Theorem2.4/Prop2.5是不可约特例。因此也不能笼统说“有不变子空间就完全不可用”。

然而(M1)里的矩阵系数可能奇异，作用对象是Φ的差，而平移承载集合是Y；原式没有直接给Y+Y或Y+aY对每个同一a的small doubling。密图、缩放、BSG与多次乘加闭包的成本必须从原L-tuples重新导出。若改写为near-identity群元素，还必须验证群与商的非集中条件，不能假装已得到它们。

仅f的非affine性不蕴含作用不可约：例如f(z)=z²I₂，其差矩阵仍全为标量。这不是满足完整critical配置的反例，也不排除可约表示工具；它只表明后续必须处理可约/稳定子情形，不能增加任意不可约假设丢掉合法分支。

这个例子只校准定性的nonaffine与irreducible不同；在小尺度上它通常有Taylor affine拟合，未被证明满足下一候选的(SM)。不能把它升级成(SM)或原配置反例。

## 4. 与总目标、验收和停止

下一主轮以真实Mat(2,2)配置的非线性命题为目标，先核source线性输入与实际L-tuples，再试向量和积/可约分支。候选需从所有原source数据推结论，或给满足全部配置/正亏损/CCW的反模型。仅抽象矩阵函数、单点图或scalar projections不算完成。

这仍是重大中间结果候选，尚未获得或认证新颖性；不把sticky子问题代替最终一般欧氏Kakeya完成标准。CP/PM当前open但其局部迭代冻结，不从本文再重命名回去。
