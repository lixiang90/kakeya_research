# R0004主代理独立复核：边界模型与熵选择成本

日期：2026-10-16。审查者：root。对象由两个不同子代理撰写，root逐项核查全文及关键公式；未经外部同行评审。不声称新颖性或重大结果。

## 1. Actual list/floor边界模型：通过

已读notes/50_counterexamples/R0004_list_floor_palette.md全文。独立核验如下。

- 八参数到全部轨道系数的Jacobian绝对值为1，完整斜率边缘密度1；大密度只发生于截距方向。原始系数prior是固定次数半代数区域的常密度。
- t≤1/2时(θ,z)到(Y1,Y2)的Jacobian=t²−1，稳定反演误差O(σ)。因此θ、z真实bins来自exact base的常数列表，不是假设有不可见速度tag。
- 固定框架A=(2θc+t0,1+2θct0)、B=(1,t0)的行列式=t0²−1。将θ=θc+s、z=zc+r、t=t0+τ展开，额外法向量为O(q²+η+σ)。q²≤η≤q使完整时间块containment成立；不能省去q²下界。
- 固定v,W后块起点Y3,w的q-bin概率各q/4，故完整assignment质量精确q³η/16。整块均参与，m=qν。J=q²η(1−t0²)，且典型hidden-bin密度n(a)≈a、a=q，确有ν≈n(a)J。所有blocks合计selected质量1/32。
- Y3(t0)由当前Y3定位至长度q的区间；w(t0)由当前宽q的隐藏bin定位至长度2q的区间。不知道v,W也有常数列表。四项乘积仍固定常数。
- Qj(V)=V2−V1²−zj的系数范数均1，在精度η/4下至少需η^-1个中心；pointwise列表不控制此全局数目。

精确符号验证见experiments/algebra/known_floor_probe.py及json。运行通过：full8 Jacobian、固定时base Jacobian、逆投影误差、框架行列式、完整法向余项与true-floor方向比率消去。

此模型确为d=1边界。d<1、native Hessian来源及criticality没有验证；H未计算。观察密度满维不蕴含H=0，已在讨论中主动排除此错误推断。它只能否定不含这些新增条件的list/floor⇒小palette命题。

## 2. ENT-001选择成本：通过

已读notes/60_entropy/R0004_full_slope_selection.md全文。以下证明的量词与分母核对通过。

- 固定有限方向网格、同一概率律，以PS⊗PA为参考，二元KL数据处理给p log(1/q)≤I(S;A)+h(p)。链式法则给I(S;A)≤I(S;Z)+H(A|Z)。只有列表在该同一law上几乎处处成功时，才能用H(A|Z)≤logL。
- 选择质量α后相对原palette的额外KL≤log(1/α)；λ≤Kνdt则方向密度比成本为log(K/α)。原律小互信息在稀疏选择后可能被α^-1放大。
- 同一joint domination P(S,Z)≤Kπ(S)PZ(Z)配合pointwise列表与π(Ea)≤ε，逐Z取事件并集，给bad≤KLε。全局label数可以很多，但共同palette和方向事件必须在同一网格；连续薄层需扩大方向cells并计边界。
- 完整方向网格的H(Wδ|Vδ)下界与链式展开正确。已有parent选择和I(Wδ;Z|Vδ,parent)不会被可见方向的小窗口增量自动控制。

这些是条件信息接口。尚未从真实d<1临界路径导出所缺的完整方向似然或剩余隐藏熵，不能把接口本身登记为Kakeya进展。
