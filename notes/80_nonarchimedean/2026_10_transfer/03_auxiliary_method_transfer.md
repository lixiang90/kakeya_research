# R0119：辅助 PDE 方法的 p-adic 可移植性

2026-10-27，padic_method_transfer。只答用户新提出的可行性问题，不恢复旧欧氏Kakeya Goal，不声证明新的p-adic restriction或一切移植不可能。依据研究规格R0119_padic_transfer_spec、OpenAI固定版本原稿§1.4、§2.1–2.3、§3、§4.2–4.4、§5的比较框架和§6；这是结构阅读与下列有限接口的代数核算，不是整篇独立重证。p表示素数，r表示Lebesgue指数。

## 1. 结论须分两层

原生p-adic Fourier分析、频率小球、加性character、Haar积分、复值Gram矩阵正性及随机符号可以保留。它们足够建立很多wave-packet和restriction-to-tube接口。

但原稿最重要的新增步骤不是这些接口，而是一个与欧氏波符号**同时兼容**的正守恒张量、四元数Dirichlet势和精确能量抵消。目前没有从本次读取的文献中取得这组三件套的p-adic对应物。故不能把新欧氏定理自动改写成p-adic限制/局部光滑定理；也不能据此断言所有重构均无望。

普通p-adic Kakeya/maximal是否早已有解由本目录01的原文核查负责；已有定理不再作为待解决目标。实时间径向norm演化与p-adic时间曲率多项式extension是不同模型，本目录02另检前者的单壳压力。

## 2. 原证明的依赖表

| 原稿步骤 | 可以保留的内容 | 不能免费移植的内容 |
| --- | --- | --- |
| Fourier与局部化，§2.1/§9 | Q_p上的复值character、Haar正交、Plancherel、频率小球/不确定性；多项式相位可产生真正细管 | metric norm壳不能当欧氏曲率球面；相位、时间域、Hessian非退化条件须另定 |
| 虚光线Gaussian，式2.4 | 可以另定义正实值热乘子或频率ball cutoff | X−iq的实到复解析延拓及指数衰减不在Q_p坐标中有同一含义 |
| 正守恒tensor，Lemma2.1 | 若χ是复/四元数值，χχ*≥0仍是有意义的值域正性 | 原构造依赖holomorphic G、D_laG=0、局部一阶系统和普通Leibniz；不能从Gram正性单独推出逐列divergence为零 |
| Hessian/cofactor，式3.1–3.14 | 某些形式多项式恒等式可在其他特征零代数上讨论 | 物理复值Bruhat–Schwartz波、Haar能量与实/四元数梯度、顺序正锥、Green边界式之间的联结未给出 |
| fiber Dirichlet，式4.8 | 非阿基米德Monge–Ampère理论确实存在，见下节 | 不等于本稿光滑、随参数变动、具有特定边界normal核的四元数Dirichlet问题 |
| 修正能量，Prop4.2 | 变分能量和非局部Dirichlet form可作为候选工具 | A:H(|Φ|²)=0、rank-one背景、cofactor边界系数为零和精确full-determinant相消须重新证明 |
| 两个圆环，Lemma6.1 | 若能先造出同一实变量非负能量与微分不等式，这个实分析引理仍可调用 | 不能把p-adic时间直接代入实T的Δ_(T,τ)；改成tree平均也须另证所需传播/势项预算 |

这里不是“p-adic没有正性”：函数和矩阵可取复值，其平方模与Hermitian正性完全存在。p-adic解析微分也存在。问题是原证明同时使用的值域、底空间、局部微分和正性不能仅靠同名对象拼接。普通p-adic球是开闭集，也不能在它的经典拓扑边界上照抄Euclidean外法向与侧面通量公式。

## 3. 一个可原生保留的 cap-to-tube 恒等式

取奇素数p、d≥1、Haar(Z_p^d)=1，标准characterψ在Z_p上平凡。定义p-adic时间的抛物面extension

    Eg(x,t)=∫_(Z_p^d) g(ξ) ψ(x·ξ+tφ(ξ))dξ，
    φ(ξ)=Σ ξ_j²，   x∈Q_p^d，t∈Q_p。

给ξ_0∈Z_p^d、整数k≥0和cap C=ξ_0+p^k Z_p^d。若|t|_p≤p^(2k)，则精确有

    E1_C(x,t)=p^(−kd) ψ(x·ξ_0+tφ(ξ_0))
                 ·1_(x+2tξ_0∈p^(−k)Z_p^d)。

证明：写ξ=ξ_0+η。因η∈p^k Z_p^d，tΣη_j²∈Z_p，二次余项的character恒为1；剩余线性character在cap上积分，恰给其湮灭子p^(−k)Z_p^d的指标。这是p-adic时间尺度p^(2k)、横宽p^k的真实管，不是借用欧氏方向的比喻。奇p确保标准二次Hessian 2I为unit非退化；这里没有借此证明全范围restriction。

所以“频率cap产生细管”这层不仅可类比，甚至有比欧氏stationary-phase近似更干净的精确版本。真正未付的是控制大量此类波包叠加的临界能量。

## 4. 虚位移与微分核心的准确障碍

原稿式2.4的Gaussian来自把复解析波取在X−iq上；Lemma2.1令G=f_sys(X−iq)，由辅助向量场D_laG=0与原系统PG=0推出逐列守恒。随后式3.2用普通乘积法则，式3.12用Hessian cofactor的散度零，式3.13用带外法向的Euclidean Green公式；式4.12两部分能量的full determinant才会相消。

以下只排除字面坐标平移方式。任何连续实参数映射I→Q_p^m（I为连通区间）都是常映射，因为像连通而Q_p^m全不连通；有限p-adic扩域的norm拓扑亦然。故不能将实辅助虚位移解释成原Q_p坐标内同样的连续平移流。即使扩到Q_p(i)，标准复值加性character仍取单位圆值，平移只给模1因子，不会自动给原稿所需实指数Gaussian衰减。

这不排除实参数热半群：函数空间L^r(Q_p^m)是复/实Banach空间，存在非平凡连续演化。可另引入exp(−s||ξ||_p^α)或频率ball滤波，但必须证明它与相位、守恒流及rank-one背景相容，不能只替换一个权函数。Berkovich空间也并非Q_p经典点的全不连通拓扑；利用其骨架是另一种可能重构，不被上面的区间论证排除。

## 5. 非局部守恒确实存在，但不是原局部张量

下面给一个正面可保留接口及其真实费用。对标准径向正算子写

    Df(x)=c_(p,n,α)∫(f(x)−f(y))K(x,y)dy，
    K(x,y)=||x−y||_p^(−n−α)，α>0，c_(p,n,α)>0。

在Bruhat–Schwartz函数上直接展开可得

    D(fg)−fDg−gDf
       =−c∫(f(x)−f(y))(g(x)−g(y))K(x,y)dy。

该额外项不能在移植普通Leibniz时删掉；取共轭配对正是非局部Dirichlet form的平方差结构。它可能是新能量的材料，不应简单称为致命障碍。

对于实时间i∂_t u=Du，若初值为Bruhat–Schwartz且其Fourier支持紧并避开0，可逐时保持Bruhat–Schwartz类，以下积分/微分可逐点计算。令

    J_t(x,y)=2c Im(conj(u(t,x))u(t,y))K(x,y)。

由∂_t|u|²=2Im(conj(u)Du)以及积分表达式，得

    ∂_t|u(t,x)|²+∫J_t(x,y)dy=0，
    J_t(y,x)=−J_t(x,y)。

因此质量守恒本身并不缺失。这个J是两点之间的antisymmetric edge流，既非原稿局部一阶flux，也没有自动给出逐列散度零的正半定物理tensor或μ^(n/(n−1))势能下界。其符号与Leibniz展开在此自含核算；不冒已独立同行审定的新定理。

## 6. 现有非阿基米德 Monge–Ampère 为什么不能直接补洞

已实读[BFJ arXiv1201.0188v1](https://arxiv.org/abs/1201.0188v1)的Introduction、TheoremA/A′和能量概述。该版本要求残余特征0、smooth projective/algebraizable Berkovich对象及支持在SNC dual complex上的测度，产出连续半正线丛度量。第5页明确其MA由交叉理论定义，不是局部微分算子。Q_p的残余特征是p，所以该定理不能直接用于本问题。这里是已读版本的假设，不能据此泛称后来所有非阿基米德MA定理都没有混合特征形式。

确已有[Fang–Gubler–Künnemann混合特征结果](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/on-the-nonarchimedean-mongeampere-equation-in-mixed-characteristic/EA7FA05D9CA2855EC077647C1F48BAE6)，Nagoya Math. J.259(2025),548–561，DOI10.1017/nmj.2025.8；本次实读出版方摘要与Introduction。其结论仍在smooth projective Berkovich几何中，并假设相应resolution/embedded resolution。本文未独证该高级理论，也不将它写成可直接用于频率fiber的Dirichlet解。

要补原稿式4.8，至少还需：把经典Q_p波的Haar密度送入可解的几何域并保持临界L^r质量；构造与守恒流相容的rank-one背景；取得随真实参数的规则性、对边界的控制，以及对应cofactor/能量变分抵消。单有“MA方程有解”不支付这些附加接口。

## 7. 可行性判定与最小下一步

结论是**Fourier/波包/正复值能量部分可移植，新增PDE核心目前不能照抄；同一策略的重新设计仍有研究价值，但尚未由已读结果闭合**。不能从这个结论宣称已解决新的p-adic restriction，也不能说未来任何p-adic辅助能量方法都不可能。

若进一步探索，较有内容的第一步是：在一个指定曲率多项式phase或有限商模型上，把上面的非局部edge守恒/Dirichlet form升级成可检测临界幂的正能量，并实际证明其传播不等式。只有这个与原符号相容的identity出现后，保留实辅助圆环或使用tree平均才有可调用的输入。当前它是准确未付门，不是已证hyp或新Goal。不得拿已解Kakeya重新包装为目标。
