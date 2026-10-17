# R0041：共同时间的可分离构造及递归幂次反攻

2026-10-17，B。已运行 context.py、读固定入口、R41 spec/R40 nextspec；实际读取 FD–deLaSalle2607.14824v3 的 Definitions2.1–2.2、Lemmas2.4–2.5、完整§3–5，及相关 Appendices A/B。只处理真实构造的方向、clock、半径与极限预算，不重开旧 matrix/flake 路线。无 Git；只编辑分配文件。

唯一主目标仍是同一个 bounded compact K⊂R5，含每方向单位段，且某趋零半径列有固定正幂 neighborhood upper，或同 K 的合法低维 Hausdorff covers。本文没有构造这样的 K。主要新增证据是一个实际邻域体积下界：保完整 Cartesian 方向参数、共同 clock、逐坐标可分离平移时，任意尺度均不能给 fixed power。它比仅说原 upper certificate 不够更强，但范围也更窄，不能排所有非可分离构造。

## 1. 可检验命题与反攻边界

令 m=d−1。对每 i∈[m] 取任意函数 u_i:[0,1]→R，不要求可测。假一个集合 K 包含全部真线段

    ((1−t)q_1+u_1(q_1), …, (1−t)q_m+u_m(q_m), t),
    q∈[0,1]^m，0≤t≤1。                              (1)

这是实欧氏线段，不是形式 digit 运算；每段长度至少1。全部方向参数的 Cartesian 组合均有同一个 clock 区间，intercept 的第 i 坐标只依赖 q_i。目标是在任意 0<r<1/10 证明

    |N_r(K)|_* ≥ c_d [log(2/r)]^{−m}，                (2)

其中左侧可取 inner measure；若 K compact 则为普通体积。本证明只构造 N_r(K) 内的有限可测子集，所以不需要对任意 u_i 做可测选择。

不能把一般的每方向存在某个独立 a_q 降为(1)。特别是 u_i 依赖完整 q、clock 区间按方向变化、分支旋转耦合坐标，均未被假设自动排除。本轮独立反攻须保这一边界。

## 2. 一个平面 strips 的原参数估计

取 M=floor(1/r)，q_k=(k+1/2)/M，k=0,…,M−1；ε=r/(20 sqrt(m))，共同 J=[1/4,1/2]。对任意实数 c_k，在平面(x,t)定义

    I_k(t)=[c_k+(1−t)q_k−ε, c_k+(1−t)q_k+ε]，
    F_t(x)=Σ_k 1_{I_k(t)}(x)，
    L(t)=|∪_k I_k(t)|。

有 Σ_k|I_k(t)|=2Mε≈_d1。对 k≠l，中心差是仿射函数，t-导数大小 |q_k−q_l|=|k−l|/M。因此无论 c_k 如何选，

    ∫_J |I_k(t)∩I_l(t)|dt
      ≤ C ε²/|q_k−q_l|。

这只是两条真实 strips 的交叠估计：可相交的时间长度≤Cε/|Δq|，每层交长≤2ε。对角项总和≤C_d。于是

    ∫_J∫ F_t(x)² dxdt
      ≤ C_d[1+ε² M² Σ_{h=1}^{M−1}1/h]
      ≤ C_d log(2/r)。                              (3)

每个 t 的 Cauchy–Schwarz 给

    (2Mε)² ≤ L(t)∫ F_t²，
    ∫_J L(t)^{−1}dt ≤ C_d log(2/r)。                (4)

L(t)>0，无零分母；常数不依赖平移 c_k、递归深度或任何形状优化。该估计保原全部 k，不做成功后验删选，也不需不同 t 独立。

## 3. 任意各坐标参数、同 clock 的实际体积下界

对每个 i 以 c_{i,k}=u_i(q_k) 应用(4)，记其 union 长度 L_i(t)。Markov 给固定 c'_d>0，使

    |{t∈J:L_i(t)<c'_d/log(2/r)}| ≤ |J|/(2m)。

因此至少 |J|/2 的同一批 times 同时有全部 m 个 L_i(t)≥c'_d/log(2/r)。这一步使用同一个 clock；不是把 m 个分别正测度的时间集合免费相交。

对每 t，Cartesian product ∏_i(∪_k I_{i,k}(t)) 中任一点，距(1)中某个真实 q=(q_{k1},…,q_{km}) 线段点不超过 sqrt(m)ε<r。全部组合都在原(1)中，这正是不能省掉的方向参数假设。故有限可测集合

    {(x,t):t∈J，x_i∈∪_k I_{i,k}(t) 对所有 i}

contained于 N_r(K)。Fubini 和同批 good times 给

    |N_r(K)|_* ≥ ∫_J ∏_i L_i(t)dt
      ≥ (|J|/2)[c'_d/log(2/r)]^m，

即(2)。对任意固定 c>0，log(2/r)^{−m}/r^c→∞，所以(1)类不能在趋零子序列上有 Cr^c neighborhood upper。结论 uniform 于各 u_i：把递归深度取得远大于 log(1/r) 也不绕过它。

这是对**实际体积**的下界，不是“某个原 upper bound 的右侧不够小”。它仍只排 fixed-power neighborhood 目标；本文没有以此免费断言任意非均匀 Hausdorff covers 的下界。

## 4. 对 FD cube 路线实际覆盖的部分

原§4 Remark4.4 的 canonical cube 分解保持坐标轴，叶子为 Q_j=∏_i[j_i2^{-N},(j_i+1)2^{-N}]，apex=(0,…,0,1)。标准共同逐层 t_l、同固定 o 和 canonical dyadic maps 下，每叶的平移第 i 坐标只依赖第 i 个二进制 word：base-step w=t(o−x_j) 逐坐标，归纳 w=w_inner+P w_outer 只作同一 scalar P 的加法，故该性质逐层保留。

原优化公式也直接显示它：

    w_j=−Σ_{l=1}^N β_l2^{−l}[1−(l−1)/(N+1)]。

各坐标可用不同深度或不同 scalar 参数，只要最终仍是完整 Cartesian 叶族及逐坐标可分离平移，便仍落入(1)。每个 q 在某叶 base 中，连接 q 到 apex 的整段加该叶平移均在真实 pyramid 内。因此整个 finite tree 在**任意**目标半径 r 下受(2)约束，不只 natural r≈2^{-N}。

在原共同参数版本，也可用原 Th(t)=(Th^{2D}(t))^m 与二维 strips 估计/Jensen 得 natural-scale 的 c_d(N+1)^{−m} actual-volume lower；(2)避免了这一较弱形式对参数相同或 natural scale 的依赖。

各坐标深度 N_i 不同时，还有 actual |U|≥c_d∏_i(N_i+1)^{−1}：取第 i 坐标 M_i=2^{N_i} 个 leaf-center slopes，并以 halfwidth ε_i=c_d/M_i 的 strips 在同一个 J 内直接放进真实 pyramids，无须取 neighborhood。§2 的同一计算逐坐标给 ∫_J L_i^{−1}≤C_d(1+log M_i)≤C_d(N_i+1)；各用 threshold c'_d/(N_i+1) 作 Markov，仍保至少半个 J 的公共 good times。对这些 times 积分 ∏L_i 即得所述式。若某 N_i=0，取唯一 coarse cell 的固定宽 inner strip，同样给常数 factor。

适用范围不能扩大：任意每叶独立旋转、根据完整多坐标地址选 child map、完整地址依赖的参数或平移，都可能破坏(1)。Lemma2.5 只保证某个 pyramid-neighborhood embedding，若其新 translations 未证明可分离，也不能仅凭它来自 cube 树就套(2)。原5.4的反复 chart patching 更不自动保持一个全局 Cartesian intercept。本文没有排这些真正耦合的改造。

## 5. 原递归 upper certificate 为何不相乘

此处仅复核已知来源，不冒充新结果。原 Proposition4.1 在每层留下 core，同时把 protruding branches 作为外部 error 累加。式(5)是

    U_N=(1−c_0)^{−d}Σ_{l=1}^N(P_{l−1}−P_l)^d+P_N^d，
    P_l=∏_{j≤l}(1−t_j)。

令 x_l=P_{l−1}−P_l≥0、x_{N+1}=P_N，则 Σ_l x_l=1。Hölder 给 U_N≥(N+1)^{1−d}。所以共同参数的最优估计本来就是 N^{−m}，不是每层固定压缩率连乘；只跟踪 P_N 而丢外部分支不是合法 upper。源 Remark4.5 已有此观察。

公平 fixed q 分解的叶尺度是 q^{−N}，故 N≈log(1/r) 时只得 log。若 N≫log(1/r)，不能把非常薄叶的体积当较粗 r-neighborhood upper；Lemma2.4/2.5 的 natural thickness 与 actual r 必须分开。对可分离 cube 类，§3 的 actual bound 已彻底排掉这一重新选 N 的捷径；对其它类，仅有 U_N 的 lower 并不证明其实际 union 有同样 lower。

把一批已压缩的不同叶各自再压缩，不自动得到上一 union 体积乘同一比率：原 bound 参照的是被分割的 pyramid volumes 之和，重叠 union 不是一份已 partition 的 parent。除非重新证明形状/方向/误差预算，否则只能合法地累加下一轮证书，不能抹掉旧分支。

## 6. 异速、anisotropic 与复制的两种费用

一般可逆线性 A 的奇异值为 σ_min≤…≤σ_max。对任意 E，

    N_r(AE)⊂A N_{r/σ_min}(E)，
    |N_r(AE)|≤|det A| |N_{r/σ_min}(E)|。             (5)

若只知道原每方向一根单位段，A 后长度为 |Av|；要无条件恢复全部单位长度，统一再放大至少 σ_min^{-1}，有效 determinant 为 |det A|/σ_min^d≥1。不能保原半径和单位长度，却只领取 transverse determinant 小因子。

这不否原 Lemma5.5：它先取完整 crossing segments，再只保 narrow cone，clock 长度未缩短，transverse determinant ε^m 合法。但覆盖整个单位球面需要约 ε^{−m} 个 ε-caps；在原 union-upper 证书中复制数与 ε^m 相消。原5.4正是这一预算，不是每个尺度再额外乘一份 f。若想用各复制对象更大实际重叠改善 union，需要新的真实几何证明；本计数只否免费证书，不给任意复制模型的 actual lower。

## 7. 同一个 compact K 的源桥与本轮未证部分

完整读回原 Definition5.2、Lemma5.3、Lemma5.5、Prop5.4：有限 chart 的旋转并保全部方向；选每方向真实单位段；后续 stage 的 ε-net caps 覆盖 sphere；δ_n=2^{−2^n}、ε_n=(δ_{n−1}−δ_n)/sqrt(d−1) 保 nested neighborhoods；最终交集才是同一个 compact Kakeya set。

其体积 estimate 是最近 working scale 的 f，而非跨 n 的乘积；用 monotone f 后为 C_d f(C_d r^{1/4})。若新 seed 真有 f(r)≤Cr^c，这个已存在桥保正幂 c/4；原 log f 则仍是 log。这里没有把 patching 不足当作新的研究缺口，也没有从原 certificate 不够推出最终 compact E 的 actual lower。

没有 measurability 的方向选择也不自动破坏此桥：各 stage 只取有限 net 的真实单位段，最后针对每个固定方向在嵌套 compact sets 中取 segment 参数极限。反过来，任意不相容 G_{δ_j} 的小体积或仅抽 Hausdorff-convergent 子列，不自动给 d_H-error≤δ_j 的最终 covers；须使用已付的5.4或另一个合法桥。

本轮没有 fixed-power candidate。新增严格障碍为(2)，它排掉真实共同 clock、完整 Cartesian directions 与可分离平移模型的全部迭代参数、深度及目标半径，包含 canonical cube 的直接改参。一般 coordinate-coupled seed、non-fair 分支、旋转/局部 patching后的 source 仍未被(2)排除，但无新的耦合机制不以这些名称再开一轮常数优化。

按一主轮停止规则：root亦未给真实改造及合法 power seed/limit，故记录这项实际 lower 与原 certificate 边界并提前 macro；不能把原 log 结果、上述排除或同 K scope 审查登记为 Kakeya反例/重大成果。已实际读 root主稿/macro/nextgate及A全文，正式review见 `research/reviews/R0041_direction_and_limit_review.md`；未经外部同行评审。
