# R0017：同一联合图的四边形质量与加法终点障碍

2026-10-17，独立正向尝试。已读本轮 spec、STATE、AGENTS、GOAL、ROADMAP、registry 和 MNL-001 的有限输入。本稿检验去掉 linewise 后的 finite vector strengthening；不增加光滑性、不可约性或 Y+aY 闭包。没有证明完整 strengthening，也没有给满足其 F/time 结构的反例。完整 sticky / 一般 Kakeya 仍未解决。

实质输出是同一原 g、同一差 prior 下可证明的 energy 与四边形质量，以及一个严格的加法终点校准：tube Katz–Tao 与任意小幂 small doubling 可以共存，所以 BSG 若只给加法近似结构就不够。该校准缺少规定的 F/time 结构，不能升级为有限 strengthening 或真实 source 的反例。

## 1. 原有限输入与记号

沿用 R0016_vector_attack.md §2 的前五项，去掉最后 linewise 条件。n=#A₋，m=#B；ν 是原差标签概率，ψ_s 有固定上界，原图权 0≤g(a,b,c,s)≤1。所有输出

    a+T_s(b,c),
    T_s(b,c)=(b−c)(F(b)−F(c))ψ_s

距 A₊ 至多 Cr，且 #A₊≤r⁻ʰn。总原质量

    W=∫Σ_(a,b,c)g(a,b,c,s)dν(s) ≥r^h n m².   (1)

B 是 r-separated 的 (r,1,r⁻ʰ)-set，故对 t≥r，每个长度 O(t) 区间至多 Cr⁻ʰtm 个原时间点。这里的 a 表示原输入点，nonaffinity 精度另记 a₀ 或原规范中的 a，不混淆。下述估计甚至不需要先用 SM；因此不能把这些估计本身当成 SM 所需的完整扩张矛盾。

## 2. 可保原质量的向量 additive energy

固定 s。对每个正权 tuple，确定性选一个原 y∈A₊，使其距 a+T_s(b,c)≤Cr（若多选取固定次序第一项）。令 w_s(y) 为分配到 y 的原 g 权之和，W_s=Σ_yw_s(y)。

定义原 weighted energy E_s 为两份 g 权的乘积，在

    ||a₁+T_s(b₁,c₁)−a₂−T_s(b₂,c₂)||≤2Cr

的所有原 tuples 上求和。分配到同一个 y 的两份 tuples 全被计入，所以

    E_s≥Σ_yw_s(y)²≥W_s²/#A₊.

对同一 ν 积分并用 Cauchy–Schwarz，得到

    ∫E_s dν(s) ≥r^h n⁻¹(∫W_s dν(s))²
                ≥r^(3h)n m⁴.                (2)

这是真实的二维、同图同 prior mass estimate。没有把 T_s(b,c) 的 distinct 值改成均匀 prior，也没有给其最大原像上界。若进一步调用 BSG，需要保这种原 time-pair 重数，不能直接把 m² 换成 distinct translation 数。

(2) 只约束 A₋ 与翻译多重集的加法能量；它没有推出矩阵作用在 A₋ 上的 Y+aY small growth。He Theorem3 的作用对象/闭包门槛仍未提供。

## 3. 四个分离原时刻上的 weighted C4 下界

固定 (a,s)，令 u_(a,s)=Σ_(b,c)g(a,b,c,s)。非负 weighted bipartite C4 的两次 Cauchy–Schwarz 给

    Σ_(b,d,c,e)g(a,b,c,s)g(a,d,c,s)
                g(a,b,e,s)g(a,d,e,s)
        =Σ_(b,d)[Σ_c g(a,b,c,s)g(a,d,c,s)]²
        ≥u_(a,s)⁴/m⁴.

再对原 a 计数与原 ν 概率 Jensen，由 (1) 得

    C4_mass≥r^(4h)n m⁴.                     (3)

此处四条边使用同一个输入 a 和同一个差标签 s，故没有额外独立 times / independent original Φ 假设。

坏四元组若任意一对时间的距离小于 t≥r，其总质量由 g≤1 与 B 的区间 upper 至多

    Cr⁻ʰt n m⁴.

对全部六对求和仍同阶。取 t=r^(6h)、h<1/6，且 r 足够小，可保留至少

    (1/2)r^(4h)n m⁴                         (4)

的 C4 原权，使 b,c,d,e 两两距离均≥t。这不是假设足量四环，而是从原 dense graph 直接导出的 weighted 四环下界。

## 4. 四边形矩阵恒等式及真实 sink

对 (4) 中每个 tuple，取四个原输出 y_(bc)、y_(de)、y_(be)、y_(dc)∈A₊。同一个 a 消去，严格得到

    y_(bc)+y_(de)−y_(be)−y_(dc)
      =R₄(b,d;c,e)ψ_s+O(r),

其中

    R₄=(e−c)(F(b)−F(d))
                 +(d−b)(F(c)−F(e)).         (5)

因此有质量 (4) 的矩阵增量落在 2A₊−2A₊ 的 O(r) 邻域。该 sink 是实际四输出的加法组合，**不是原 A₋ 或 A₊**。现有 cardinal 比较 #A₊≤r⁻ʰ#A₋ 不给 2A₊−2A₊ 的 small cover，更不给它原 tube KT。

在分离时间上若要除以 (b−d)(e−c)，(5) 成为两条矩阵 secant slope 的**和**：

    R₄/[(b−d)(e−c)]
       =[F(b)−F(d)]/(b−d)
                      +[F(e)−F(c)]/(e−c).  (6)

它不是 free cancellation of the affine part；F(b)=bR+U 时 (6) 恰为 2R。除法把 O(r) error 放大到 O(r/t²)=O(r^(1−12h))，若用在下一尺度必须付出此损失。这里没有把它继续称为 O(r)。

四环的条件分布也不是 ν 的无损替身；原权乘积≤1，归一化其质量至少 (4) 后，prior domination 最坏付 r^(−4h) 和固定常数。这一小幂可登记，但不能默认为 ν 本身不变。

## 5. 严格的 BSG 加法终点校准

下面校准直接排除一项捷径：“tube KT 有固定正亏损，所以任意小幂 doubling 已经矛盾”。它不填入原 F/time 关系。

固定 γ_T=1/8、γ_Φ=1/4，固定任意整数 M≥3、小 h>0，以及任意所需的 source-like 常数损失指数 η>0。先选很大的 dyadic 整数 L₀，令

    N=L₀⁴, D=L₀³, r=N^(−n),
    C_n={Σ_(j=1)^n d_jN^(−j):0≤d_j<D},
    A_n=C_n×C_n.

L₀ 只需先依 M,h 选足够大，保证 2log_N M<h 以及 log_N(MD)<7/8；其后 n→∞，n₀ 可依 N,h,η。这里 r 为 dyadic，#C_n=D^n=r^(−3/4)，#A_n=r^(−3/2)。实际 A_n 的 AD 维数恒为 3/2，即 source-like κ=1/2，**不随 h 缩到端点**。其 AD 常数 C_N 只依已固定 N，不依 n，因此对每个 η>0，n 足够大都有 C_N≤r⁻η。

### 5.1 全宽 tube Katz–Tao

对所有 r≤w≤t≤1，单坐标 Cantor 的 elementary cylinder packing 给

    N_w(C_n∩I)≤C_N(t/w)^(3/4)               (7)

（I 长 O(t)）。证明：取 N-adic 邻近尺度 N^(−k)≈t、N^(−j)≈w；I 只遇 O(1) 个 level-k cylinders，每个只有 D^(j−k+O(1)) 个相关 level-j descendants。跨两端尺度的 N 固定因子吸收入 C_N，独立于 n。反向从包含任意原点的合适 cylinder 取其全部后代，给各中心 ball 的 lower；故 C_n、A_n 的 AD 维数分别固定为 3/4、3/2，常数 C_N 与 n 无关。

对任意平面 width-w、length-t 的 tube，选其轴方向分量至少 1/√2 的坐标。该坐标的投影区间长 O(t)，由 (7) 只需 C_N(t/w)^(3/4) 个 w-intervals；在每个 interval 内，tube 的另一坐标跨度 O(w)，故只需 O(1) 个 w-balls。因此

    N_w(A_n∩tube)≤C_N(t/w)^(3/4)
                ≤r⁻η(t/w)^(1−γ_T).        (8)

对每个 η>0、n 足够大成立。这核的是全部 w,t，不是仅最细宽 r。为了连方向 AD 维数也校准到同一个 κ=1/2，可另取每坐标 digit alphabet 为 {0,…,L₀−1} 的 Cantor 积 H_n。H_n⊂A_n，AD 维数为 1/2，各坐标概率 Frostman exponent 为 1/4。取 s=(x,x')∈H_n² 的 uniform ordered-pair prior、ψ_s=x−x'，对每个 slab 固定 x' 并选法向分量大的坐标，得

    ν{ψ_s∈slab_t}≤C_Nt^(1/4)≤r⁻ηt^(γ_Φ).  (9)

所以本加法校准还能保真正的差 prior 与 fixed complementary AD dimensions；未改成 distinct difference 上的均匀计数。输入 tube/slab 常数满足任意 η 的 r⁻η，而非固定粗 porosity 替代品。

### 5.2 任意小幂加法膨胀与满质量平移

对任意固定非负整数 p,q 且 1≤p+q≤M，每个坐标的 digits 至多有 (p+q)(D−1)+1≤MD 种；有无进位冲突均不增加 distinct 输出数。因此

    #(pA_n−qA_n)≤[(p+q)(D−1)+1]^(2n)
                  ≤M^(2n)#A_n
                  =r^(−2log_N M)#A_n
                  ≤r⁻ʰ#A_n.               (10)

这是先给任意固定 M,h，再选 base，最后任意深度 n 的完整量词；所以任意预定有限次数的加法闭包都可能只有所需的小幂膨胀。所有点仍在固定有界盒（M 固定），且为 r-grid 点。令 A₊=A_n+H_n−H_n⊂2A_n−A_n，则对每个原 a∈A_n 和每个标签 ψ=x−x' 都有

    a+ψ∈A₊.

所以这个**未指定 F/time 形式**的平移图可取 g≡1，保留全部原 mass，且由 (10) 有 #A₊≤r⁻ʰ#A_n。若希望输出也有同一个 γ_T=1/8 的 tube-KT upper，用 2A_n−A_n 包含它并以更大 digit alphabet 重复 (7)：log_N(3D−2)<7/8，给常数 C_N、独立于 n 的 upper。没有声称 A₊ 仍有恰好 3/2 的 AD 维数；小的 dimension excess 不是免费消掉的。如果另要求相同 exponent 下 r⁻η upper，base 还须依 η 选得更大。

这不违反 MNL-001：这里没有构造满足 SM 的 F:B→Mat(2,2)，也没有使平移等于 (b−c)(F(b)−F(c))ψ。恰恰是该时间形式与 nonaffinity 承担了标量分支真正的信息。该模型只证明：从 (2)/(3) 获得 BSG 加法近似结构后，不能只凭 tube KT 结束；必须再次使用原时间结构、共同 prior 和真实矩阵作用。

## 6. 当前正向缺口与本轮范围

目前可保原质量的步骤到 (2)、(4)、(5) 为止，未把它们转成 He 的 Y+aY 闭包或一个受 tube KT 控制的共同 sink。多次 sum/difference 的大小不能从一次 A₊/A₋ cardinal 比较直接推；即使 BSG 给小加法增长，§5 表明那种结论本身也不足以矛盾。

因此不把 energy、C4 的重新命名当成一般 matrix theorem，也不加 C²/曲率假设来代替任务。本稿没有完整 finite strengthening 反例；另一代理独立攻击其实际 F/B 量词，root 继续检查 source 的真实额外输入。没有新 primary 下载或未经核验的向量和积定理调用。一般二维曲线分支与完整 N5-STICKY-MATRIX-01仍 open；后续行动按本轮 macro 与实际新信息决定。
