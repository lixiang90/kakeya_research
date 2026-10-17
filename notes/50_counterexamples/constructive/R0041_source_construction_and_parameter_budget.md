# R0041：真实 Perron 构造、可变参数与实际体积门槛

2026-10-17，A。唯一任务为 FD–deLaSalle2607.14824v3 的实际 all-directions 构造能否由 log 改为 fixed power。本稿完整支付所用 finite/continuous/compact 接口，另测试真实参数改造。**没有构造 Kakeya 反例，没有证明整个框架不可改进，也不认证新颖性或重大性。**

## 1. 恢复、命题与阅读范围

已读 GOAL/STATE/ROADMAP、registry 最新状态、R41 working spec 与 R40 nextspec。主目标仍是同一 bounded compact K⊂R5，所有方向完整单位段，并有固定 c>0、r_j↓0 使 |N_{r_j}K|≤Cr_j^c。每次不同的 K_j 各有小体积不够。

本次完整读取 primary PDF6–19 的相关 construction：Definitions2.1/2.2、Lemmas2.4/2.5、§3 全部、§4 全部、§5.1/5.2 至 Th1.3 证明。提取文本 `fernandez_delgado_de_la_salle_2026_construction_2607_14824_v3.txt` 的 `split('\n')` 行305–1142；尤其 (3) 行398–414、Prop4.1 行578–714、(5)/(6) 行748–799、Remark4.4/4.5 行831–875、Lemma5.3/Prop5.4 行970–1142。

下文把三种不同结论分开：原 upper-bound certificate 的最优值；某个实际参数选择的真实 set lower；整个 coordinate-separable 类的真实 neighborhood lower。第一种不能被冒充后两种。

## 2. 一步压缩保留了什么

令 m=d−1，Σ 为 m-polytope，T=conv(Σ,v)。partition Σ=∪Σ_i，且存在 c∈(0,1)、x_i∈Σ，使 Σ_i⊂cΣ+(1−c)x_i。取 o∈AffΣ、u_i=o−x_i、0<t≤1−c。原 Lemmas3.5/3.6 给

\[
 \Sigma_i+t u_i\subset H_o^{1-t}\Sigma,
 \quad (T_i+t u_i)\setminus H_o^{1-t}T
      \subset H_v^{t/(1-c)}T_i+t u_i.
\]

所以 core 缩了，但完整 T_i 被**平移**，没有在其 clock 方向缩短。漏出 core 的 branches 不能丢；它们携带原方向的完整线段。总漏出体积的 upper 为 (t/(1−c))^d|T|。这是一项求和上界，不是漏出集合体积的精确值。

反射 cones 的 containment/disjointness（原3.7/3.8）另外服务 Theorem1.4 的 translated-tubes disjointness，不是证明每个实际 K 小体积的额外乘法因子。对 §5.2 连续方向集合，核心是完整 base partition 与每叶整 pyramid，没有只选一根 leaf-axis 代替全部方向。

## 3. 原有限迭代的精确预算

同一个公平 partition 的第 n 代有 B^n 个 leaves，B=|I|；每个 leaf 的水平线性尺度 r=B^{-n/m}。令 P_0=1、P_j=∏_{k≤j}(1−t_k)。Prop4.1 的真实 translations 通过

\[
 w_{(i',i_n)}=w_{i'}^{(i_n)}+P_{n-1}w'_{i_n}
\]

递归拼成；内层整个 branch 随其 parent 平移，而非重新复制且另付一次完整单位长度。其 union U_n 满足

\[
 {|U_n|\over|T|}\le
 B_n:=P_n^d+(1-c)^{-d}\sum_{j=1}^n(P_{j-1}-P_j)^d. \tag{1}
\]

所有 leaves 仍是原 unit-height pyramids 的 translates。Σ 的每个点都属于某个 leaf，因此每个 base-to-apex 方向仍有完整原长度的线段；没有按平均方向概率删选。

原优化取 t_j=[n−j+(1−c)^{-1}]^{-1}。立方体二分 c=1/2 时，t_j=1/(n−j+2)、P_j=(n−j+1)/(n+1)，得到 |U_n|≤C_d(n+1)^{-m}。同时 r=2^{-n}、leaf 数 2^{mn}；不能在维持分辨率 r 时独立令 n=r^{-a}。

Holder 直接核原 Remark4.5：设 x_j=P_{j-1}−P_j≥0、x_{n+1}=P_n，则 Σx_j=1，所以 B_n≥Σx_j^d≥(n+1)^{-m}。这只说明 (1) 这份 upper certificate 没有 fixed-power 小值，不是由 |U_n|≤B_n 倒推 |U_n|≥B_n。

## 4. 非齐次公平分支/压缩参数的证书测试

允许第 j 级使用同一 reference Σ 的不同公平 partition，B_j≥2，合法 c_j∈(0,1)；同一级所有 nodes 用相同这份选择。逐项重复原 induction，可得原式的 level-dependent 版本

\[
 B_n=P_n^d+\sum_{j=1}^n (1-c_j)^{-d}x_j^d,
 \quad x_j=P_{j-1}-P_j,\quad \sum_{j=1}^{n+1}x_j=1. \tag{2}
\]

weighted Holder 给完整下界

\[
 B_n\ge\left[1+\sum_{j=1}^n(1-c_j)^{d/(d-1)}\right]^{-m}
       \ge(n+1)^{-m}. \tag{3}
\]

证明是 1=Σx_j≤(Σa_jx_j^d)^{1/d}(Σa_j^{-1/(d-1)})^{m/d}，a_j=(1−c_j)^{-d}、a_{n+1}=1。约束 x_j≤(1−c_j)P_{j-1} 只会增大最小值，不破坏 (3)。

公平尺度 r=(∏B_j)^{-1/m}，故 n≤m log(1/r)/log2。B_j=1 的 identity 分支不能有 c_j<1：一个正体积 Σ 不可能包含在其 c_j-homothetic copy 中，体积立刻矛盾。因此插入无方向细分的“额外压缩层”不是原合法一步。改变 q_j 或 t_j 的 level-dependent 调度仍不能让 (2) 的 certificate 在 r 尺度达到 fixed power。

这是对实际可变参数证书的扩展核查，不排跨 node 的非一致选择、跨坐标耦合或利用 branches 大幅额外重叠的新估计。那些选择须另证共同 core/完整方向/尺度，不能自动沿用 (2)。

## 5. 一个真实改造严格失败：每层最大压缩

对 Σ=[0,1]^m、o=0，设 leaf 左端点 α=Σ_{j=1}^nβ_j2^{-j}，β_j∈{0,1}^m，r=2^{-n}。原 algorithm 对任意 t_1,…,t_n∈(0,1/2] 都给 coordinate-separable translations

\[
 w_\beta=-\sum_{j=1}^n2^{-j}q_j\beta_j,
 \qquad q_j=1+P_{n-j}-2P_{n-j+1}. \tag{4}
\]

可逐级验证：最外 bit 的 coefficient 为 (1−P_{n-1})/2+P_{n-1}t_n；其它 bits 是前 n−1 级 coefficients 除2。n=1 给 w=−t_1β_1，即得 (4) 的 induction。原最优参数化简 q_j=1−(j−1)/(n+1)，恢复 Remark4.4 的显式式子。

现试图每层取最大 t_j=1/2，使 core P_n=2^{-n} 指数小。(4) 却给所有 q_j=1、w_β=−α。高度 h∈[0,1] 的每个 coordinate slice 是

\[
 A(h)=\bigcup_{k=0}^{2^n-1}[-hkr,-hkr+(1-h)r].
\]

当 h∈[1/4,1/2]，相邻 intervals 重叠，故 |A(h)|=h+r(1−2h)≥1/4。整个 slice 为 A(h)^m，因此

\[
                         |U_n|\ge4^{-d}. \tag{5}
\]

这是**实际集合体积**的下界，非 certificate 倒置。此选择仍保所有连续 base directions、整 clock 长度、bounded centers；失败原因正是漏出 core 的 branches，并非先丢了目标假设。常比例重复压缩不把总 union 体积乘成指数小。

## 6. 更广的实际下界：同 clock 的 coordinate-separable line array

下面是初等平面重数方法的完整有限版本；不是文献新颖性声明。

设 J 为固定正长度 interval。每 coordinate i=1,…,m 有 N≈r^{-1} 个 slopes a_{i,k}，位于固定 bounded interval 且 |a_{i,k}−a_{i,l}|≥c r|k−l|，每个有任意 intercept b_{i,k}。假 K 包含**全部 Cartesian combinations** 的完整 clock lines

\[
 \{(b_{1,k_1}+ta_{1,k_1},\ldots,b_{m,k_m}+ta_{m,k_m},t):t\in J\}
 \quad\text{for every }(k_1,\ldots,k_m).
\]

则

\[
                    |N_rK|\ge c_{d,J}\,[\log(2/r)]^{-m}. \tag{6}
\]

不假 intercepts 均匀，不要求同 coordinate 的 b 对 a 连续；但不能把每个 joint direction 任意依赖其它 coordinates 的 b_i 免费改为本假设。

证明：取 strip halfwidth s=r/(10\sqrt m)，设

\[
 M_i(t,x)=\sum_{k=1}^N1_{|x-b_{i,k}-ta_{i,k}|\le s},
 \quad e_i(t)=\int M_i(t,x)^2dx.
\]

每 t 的 ∫M_i=2sN≥c。对 k≠l，两 strips 的交面积≤Cs min(|J|,s/|a_{i,k}−a_{i,l}|)。按 |k−l| 求和及 N s≈1，得

\[
 \int_J e_i(t)dt\le C\log(2/r), \tag{7}
\]

diagonal 只贡献 O(1)。Markov 对 Σ_i e_i 同时选出长度≥|J|/2 的同一个 good-time set，使各 e_i≤C_{d,J}log(2/r)。对 strip union D_i(t)，Cauchy–Schwarz 给

\[
 |D_i(t)|\ge{(\int M_i)^2\over e_i(t)}\ge {c\over\log(2/r)}.
\]

在每个 t，∏D_i(t) 距某条真实 Cartesian-combination line 的对应点≤√m s<r，所以其积包含在 N_rK 的该时刻截面中。对公共 good times 积分，得 (6)。没有把分别有大 time-set 的结论相乘；共同 good times 是由同时控制全部 energies 明确选出的。

若 K 含同 clock、intercept map 为 (b_1(a_1),…,b_m(a_m)) 的完整 continuous slope box，则对每个 r 抽上述 grids 即得 (6)。所以该类 **真实 neighborhood** 不可能在任意 r_j↓0 有 fixed-power upper。只得到 lower Minkowski 的限制，不免费推出其 Hausdorff dimension full。

## 7. 应用于原 cubical tree 与 variable-parameter 改造

原 (4) coordinate-separable，U_n 的每个高度截面恰为 m 个一维 unions 的 Cartesian product。对每 coordinate 选 α_k=(k+1/2)r 的中心线；在 h∈[0,1/2] 时原 pyramid 的横向 halfwidth≥r/4。因此上节 strip argument 甚至直接给

\[
                       |U_n|\ge c_d(n+1)^{-m} \tag{8}
\]

对全部合法 t_j 成立，不仅对最优 t_j。允许各 coordinate 分别选择不同参数、不同 intercept maps、不同一维分支排列，只要所有 combinations 仍存在、common clock interval 固定，(6) 同样适用。故仅作这类可变参数修改不能突破 log。这比 Remark4.5 的 upper-method 最优性更强，但没有排除 genuine cross-coordinate coupling。

## 8. 连续方向 G_r 的 neighborhood/平移符号逐项支付

Lemma5.3 使用 full pyramids 而非只一个 direction per leaf。可显式实现 Lemma2.5 的 shifts，保持上节 product：对 T_α=conv(α+r[0,1]^m,(0,1))，取

\[
 q_\alpha=((\alpha+(r/2){\bf1})/2,1/2).
\]

距 base face≥1/2，距每个 side face≥c_d r，故 B(q_α,c_d r)⊂T_α。凸性给

\[
 N_{2r}T_\alpha\subset C T_\alpha-(C-1)q_\alpha
\]

对固定 C≥1+2/c_d 成立。定义

\[
 v_\alpha=Cw_\alpha+(C-1)q_\alpha,\qquad
 G_r=\bigcup_\alpha(T_\alpha+v_\alpha).
\]

**符号为 plus**：这样 N_{2r}(T_α+v_α)⊂CT_α+Cw_α。因此 |N_{2r}G_r|≤C^d|U_n|。各 v_α 的竖坐标共同为 (C−1)/2，水平坐标按 α 的各 coordinate 分离，所有 centers 一致有界，故这个明确合法的 G_r 仍满足 (6) 的 log lower。

每个 base x∈[0,1]^m 属于某个 leaf，原 segment [(x,0),(0,1)] 长度≥1；纯平移后完整保留。方向 patch S={(-x,1)/√(1+|x|²)} 与 r 无关，含球面开集；固定有限个 rotations 覆盖全 S^{d−1}。并成 compact all-directions G_r 只乘固定体积常数，且包含其中一个 product patch，故保该 lower。

这里排除的是这份显式标准 cubical G_r 及 product-preserving 修改。没有声称 Lemma2.5 的所有任意选择都保持 product，更没有由 U_n 的 lower 倒推其任意 subset 的 lower。

## 9. Proposition5.4 的完整适用接口

输入为同一 nondecreasing f，对每个 δ∈(0,1) 存在 compact all-directions Gδ，|N_{2δ}Gδ|≤f(δ)。不是只一串 unrelated finite direction nets。

原5.5先把 Gδ 通过冗余 unit-cube 切割/平移装进 fixed cube，保每个小 slope cone 的 crossing segment；再用 (x₁,x')↦(x₁,2εx')。det=(2ε)^m，minsingular=2ε，所以 |N_{2δ}F^{I,ε,δ}|≤Cε^m f(δ/ε)。其 unit length 来自**穿过两个相距1的 clock faces**，不是把 anisotropic map 当等距。方向覆盖半径 ε/2，且 F^{I,ε,δ}⊂N_{√mε}I。

设 δ_n=2^{-2^n}、ε_n=(δ_{n-1}−δ_n)/√m；有限多个早期 n 若 ε_n<δ_n，则按原证明跳过该步并放大固定常数。从满足 ε_n≥δ_n 的后续步起，以 O(ε_n^{-m}) direction net 给上一 compact F_{n-1} 选各一完整单位段 I_u，并置 F_n=∪_uF^{I_u,ε_n,δ_n}。则

\[
 N_{\delta_n}F_n\subset N_{\delta_{n-1}}F_{n-1},\qquad
 |N_{2\delta_n}F_n|\le C f(C\sqrt{\delta_n}). \tag{9}
\]

direction net 的 ε_n^{-m} 与 determinant ε_n^m 精确抵消；没有额外 ε_n^m 可偷偷留作反复乘法压缩。E=∩N_{δ_n}F_n 非空紧且含每方向完整单位段：对固定方向，starting-point 的非空闭集随 nested compact sets 递减，故有相容极限；无需 measurable direction selection。δ_{n+1}<δ≤δ_n 时 E⊂N_{δ_n}F_n 给 |N_δE|≤|N_{2δ_n}F_n|≤Cf(Cδ^{1/4})。

因此 f(r)≤Cr^a 的合格新输入会给正幂 a/4；f(r)=C log(2/r)^{-m} 仍只给 log。原5.4没有凭空制造 power，也没有证明其所得 final E 必保持 product；上节 finite/product lower 不自动变成任意 final patched E 的 lower。

## 10. 本轮实际新增限制与未完成项

已严格排除三种实际尝试：常比例最大压缩的指数 core 不能代表实际 union（(5) 给常数 lower）；所有同 clock、coordinate-separable 自由参数改造都有实际 log lower（(6)–(8)）；level-dependent 公平细分和 scalar t 调度在原证书中最多 log，branch number 与 effective δ 不可独立。

跨坐标/跨 node 的 genuinely coupled translations 不满足 (6)，不能据本稿说它们不可能。若将其作为新构造，必须重新支付原 common-core induction/branches 交叠、continuous directions、neighborhood upper 和最终 compact bridge；不能只把未估计的交叠叫乘法 saving。完整同 K fixed-power 构造仍未找到。本文的来源重证部分不作新结果；实际 barrier 为有界路线信息，不升格 Goal/major/novelty。

正式 review 待实际读 root 与 B 的全文后另归档；本稿仅编辑本文件，无 Git。
