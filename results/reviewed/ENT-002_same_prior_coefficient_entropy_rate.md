# ENT-002：共同先验的原生系数熵率

日期：2026-10-16，R0005。状态：内部独立复核通过，见research/reviews/R0005_entropy_rate_review.md。未经外部同行评审，不声称新颖性；不是Kakeya维数改进。

完整证明与源定位：notes/60_entropy/R0005_coefficient_entropy_source.md。令A_p=(y0,V)_p、C_p=(x0,x1,x2)_p，网格嵌套，所有测度均在同一parent-native world。关键输入为同一未归一化ν°的参与箱floor与混合尺度cap：

ν°(A_p,C_p)≥p^(j+d)π(V_p)/K，
ν°(A_p,C_r)≤K p^j r^d π(V_p)，r≥p，
ν°(A_p)≤K p^j π(V_p)。

第二式来自原稿TeX247–248行及preceding long occupation；不是两个尺度的(6.6)直接相减。零palette bins忽略，fixed finite grids与同prior不可省略。

对任何支持于参与fine bins的同一概率律P，计数直接给

H_P(C_p | C_r,A_p)≤d log(r/p)+2logK。

若两尺度均参与，且同一P≤Dν°、|y0|∞≤R_y，令c_y=log[C_j(1+R_y)^j]，还有

dlog(1/p)−log(DK)−c_y≤H_P(C_p|A_p)≤dlog(1/p)+2logK，

I_P(C_r;A_p|A_r)≤logD+5logK+c_y。

下界利用velocity参考palette的非负KL项，不需要假定affine边缘逐箱饱和。稀疏后验的D=G/α；若D为固定幂，误差不能称作subpower。完整ν°未必全部参与，不能把参与箱结论自动套给全prior；笔记另给显式bad质量误差。

在固定幂窗口、K,D,R_y均subpower时，这是实际d+o(1)的条件熵率，并压住coarse native向fine affine的额外信息。NAT-001说明它仍不能免费恢复原始W的同精度bins；跨native重置和exact-point信息属于另一个输入。
