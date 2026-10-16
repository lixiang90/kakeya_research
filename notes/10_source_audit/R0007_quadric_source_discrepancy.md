# R0007：四维quadric例的文献强弱差异与显式坏框

日期2026-10-16。此处审计既有例子的准确版本，不声称新颖性，不以权威署名替代计算。

## 1. 核对的原始版本

1. Larry Guth, *Introduction to the proof of the Kakeya conjecture*, arXiv:2505.07695v1，2025-05-12，21页。新增原PDF与提取文本存literature。p.20 §9叙述一个signature(2,2) quadric的完整δ^-3管族，声称其凸聚集常数有常数上界，重数为δ^-1。
2. Joshua Zahl, *A Survey of the Kakeya conjecture, 2000–2025*, arXiv:2512.09397v1，§4.1 pp.11–12，说明完整SL2 quadric族不满足常数凸Wolff界，具体坏框损δ^-1/2；其后用稀疏及多个复制族给常数凸Wolff界、并集体积O(δ^1/2)的例子。
3. Wang–Zakharov, arXiv:2609.22035v1 pp.3–4记录后一种规模的既有反例。它另需AD-regular/sticky假设才有自己的正向定理。

上述PDF页码及数学式已通过渲染查看，非仅HTML或抽取文本误读。两份综述的更强/更弱数字不能混合使用。本项目不采用Guth p.20未经完整凸体检验的更强断言；下面给自然完整网格族的直接坏框。WP4否定的all-plank上界另见R0007_weighted_plank_obstructions.md，不从某个坏框下界反推上界。

原始链接：[Guth v1](https://arxiv.org/abs/2505.07695v1)，[Zahl v1](https://arxiv.org/abs/2512.09397v1)，[Wang–Zakharov v1](https://arxiv.org/abs/2609.22035v1)。

## 2. 显式参数与两综述quadric的关系

取(t,x,y,z)∈R4和

Q(t,x,y,z)=ty+xz−1。

参数s∈[1,2]、p,q∈[−1/4,1/4]给完整0≤t≤1轨道

x=s+pt，y=−sq−p/s−pqt，z=1/s+qt。

逐项相乘有ty+xz≡1。初始系数和速度在固定有界盒内；反向直接读s=b_x、p=u_x、q=u_z，故δ-parameter网格是系数空间中本质不同的δ线。

矩阵[[t,x],[−z,y]]的det为ty+xz。再作固定可逆线性变换

U=(t+y)/2，V=(x+z)/2，C=(t−y)/2，D=(x−z)/2，

得到ty+xz=U²+V²−C²−D²。故这里不是通过换成不同signature的quadric绕开文献差异。

## 3. 完整网格族确有δ^-1/2的凸聚集损失

令δ=m^-2，m为充分大的整数。完整δ-网格中选子族

s=1+σ，σ=iδ，p=jδ，q=−p，0≤i,j<m。

恰有m²=δ^-1条。它们满足全时间精确式

x+z−2=σ²/(1+σ)，
y=p[(1+σ)−(1+σ)^-1]+p²t，
x−z=(1+σ)−(1+σ)^-1+2pt。

所以|x+z−2|≤δ、|y|≤4δ、|x−z|≤4√δ。令空间正交轴为(1,0,1)/√2、(0,1,0)、(1,0,−1)/√2，所有这些完整轨道都在固定中心、空间半宽(Cδ,Cδ,C√δ)的全时plank内。

其四维体积O(δ^{5/2})；固定倍扩大后也包含每条轨道的半径cδ管。管总量至少cδ^-1·δ³=cδ²，故该凸体的管密度至少cδ^-1/2。这直接否定自然完整δ网格quadric族的常数凸聚集界。

证明同时解释为什么‘曲面中有三维linefamily’本身不是满足Wolff条件的反例。必须稀疏或加权并重新核验所有planks；坏框只证明必要损失，不能证明该损失已足够。

## 4. 本轮使用边界

文献反例已知，本轮用途是修正拟推广的输入强度与可调用形式。即使WP4一般形式被严格否定，也只否定原三维输入的直接维数替换，不能推出五维Kakeya为假，不能直接推出j=3 universal H≤L本身为假。

本轮独立构造/审查记录会分别标记bad-frame下界、all-plank上界与source有限尺度推论，避免把不同验证范围拼成不存在的完整证明。
