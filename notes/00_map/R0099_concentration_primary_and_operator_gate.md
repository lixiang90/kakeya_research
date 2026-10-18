# R0099：concentration primary、原wholeclock与算子资格

2026-10-19，A。先实际读 reselection5／当前 STATE／R98 next6 和 root-review6；随后实际读研究前已锁的 working5，再施工以下十二节。只编辑本分配文件，不操作元数据、PDF下载、Git 或新代理。Goal active，未经外部同行评审。

## 1. 原目标、三种场景与实际primary读域

完整 ordinary／HRZ、sticky 全 rough 及 ordinary 桥、真实同集 full-direction 严格低维四条路线不变。当前检验的新输入是浓集**序列**的值分布结构，不把 R91 单测度 singular-polar 换名；也不以新来源题名预认能解决 Kakeya。

实际 fresh 打开 [Gennaioli–Rindler 官方 history](https://arxiv.org/abs/2608.20899)：v1 为2026-08-21，current v2 为2026-09-11。实际读 [v2 HTML](https://arxiv.org/html/2608.20899v2) 的完整 §1 主声明／定义、§2 相关 convexity/barrier 声明及组装接口、§3 Lem3.6 与 Prop3.1 收尾、§4 Th1.6／1.7／1.12 的组装证明和 Lem4.1，以及 Appendix A 的三个例子。热流核心估计、广义 Young-measure 表征等高级 wholeproof 仍具名，未新独证整篇。

始终分开：固定 null whole-K stress 的 mollification；随 δ 变化且 whole-tube union 小的 stress；仅 marks union 小而 whole axes 未必小的原配置。前者可由旧结果重获，第二种才涉及新 sequence 约束，第三种不能凭平均或逐管 density 冒第二种。

## 2. 原定义：真正需要浓集的是哪些量

源取一阶常系数齐次算子 A=Σ A_k∂_k，值空间 V,W 有限维；不含零阶项。Def1.3 对 Lipschitz 域（原记 Q）中的 smooth u_j 要求：A u_j=0、||u_j||_1=1、u_j→0 in measure、u_j 弱星收敛到有限 measure u 且 |u|(∂Q)=0，以及

    Θ_(u_j)=(u_j/|u_j|)#(|u_j| dx) → μ

在单位值球面 S_V 上弱星收敛。矩阵用 Frobenius norm；Θ 是**矩阵值方向**的分布，不是原物理 v 的分布，也不保留 x、tube label 或 clock。

Rem1.5 明确允许 A u_j=w_j，其中 ||w_j||_1 一致有界且 w_j→0 in measure。这是非零 RHS 的真实资格，不能把 finite endpoints 粗拒为“不是 A-free”。但也不能把仅 finite measure、仅弱星有界或仅负 Sobolev precompact 擅自改写成该假设。本文在使用此扩展时明称 Rem1.5 generator；原 u_j 本身不被伪称 homogeneous A-free。

## 3. 主定理比R91真正多给什么、又没有给什么

Th1.6 对上述 concentration law μ 给 Choquet 型分解 μ=∫ν dπ(ν)，各 probability ν 的 barycenter [ν] 落 wave cone Λ_A=∪_(|ξ|=1)ker A(ξ)。不要求 constant rank。Th1.7 另需 rank A(ξ) 对 ξ≠0 恒定及 spanΛ_A=V，才可令各成分 ν 自身也有 concentrating A-free generators；并有 concentration laws 等于上述 barycenter-wavecone laws 的弱星闭 convex hull。Rem1.5 的 law 先经 Th1.6 落入该闭包，再由 Th1.7 获得其他 exact generators，不能说原含端点序列已经变 A-free。

区别实在：即使原 u_j 的 weak limit 是 Lebesgue-ac，值分布 μ 仍受此约束；旧 R91 只约束一个极限 measure 的 singular polar。源 Th1.9 的 equi-integrability 另需闭凸 cone K∩Λ_A={0}、K∩(−K)={0}，不可直接给含 rank-one 的 PSD cone。Th1.10 的 recession／Λ-convex 条件也须保留，Th1.12 的 extremal support≤rank A(ξ)+1 只约束值分布成分，非原管数量。

不能从分解推出 μ 所有原子在 Λ_A，更不能推出总 barycenter [μ]∈Λ_A：wave cone 非凸。源 Appendix A Example3 的带符号矩阵浓集正是其强限制的反攻。后文 PSD 情形有额外正性，须另证明，不能当一般主定理的原话。

## 4. Sym_n上的row-Div、constant rank及有限RHS

取 V=Sym_n、W=R^n、A=Div，符号 A(ξ)M=Mξ（省略无关 Fourier 常数）。对 |ξ|=1 及任意 b，

    M=b⊗ξ+ξ⊗b−(b·ξ)ξ⊗ξ

是 symmetric 且 Mξ=b，故 rank A(ξ)=n 恒定。Λ_A={symmetric singular matrices}；每个 rank-one vvᵀ 都在 Λ_A，且这些矩阵张成 Sym_n，故 Th1.7 的两项附加条件实际成立。PSD 是取值 cone，不是另一个线性值空间，不能在计算 symbol 时把它当向量空间。

原 wholeclock positive stress

    S=∫∫_0^1 v⊗v δ_(a(v)+tv) dt dσ(v)

满足 tr S 为 occupation probability，S(total)=∫v⊗v dσ。row-Div 的端点是**向量** measure

    DivS=∫v[δ_(a(v))−δ_(a(v)+v)] dσ(v)，TV≤2。

对 PSD measure，Frobenius variation c=|S|(R^n) 满足 1/√n≤c≤1。原 trace 归一与源 Frobenius 归一相差至多 √n，而不是同一规范。

补充真实 negative-Sobolev 边界：固定有界域上，一致 finite-TV measures 沿子列在 W^(−1,p)（1<p<n/(n−1)）precompact，可由 W_0^(1,p′) 的 Morrey／Arzelà–Ascoli compact embedding 到 C_0 再对偶得到。但只保证差到某个 RHS limit 收敛，不是 A u_j→0。若另作右逆校正，必须证明校正 L1 小且不改变浓集 law／PSD；本稿没有赠这一步。以下直接验证更合适的 Rem1.5 条件。

## 5. 固定null whole-K：资格可付，但新分解是旧闭包

若原 bounded Kakeya/hull G 为 Leb-null，原 S 和端点 DivS 都由 G 承载，虽 topological support 可能更大。取正 compactly supported mollifier ρε→0，Mε=S*ρε、cε=||Mε||_1、uε=Mε/cε。在共同较大 Lipschitz cube 内，support 远离边界，1/√n≤cε≤1，且 finite singular measure 的 Lebesgue differentiation 给 Mε→0 a.e.，端点卷积也趋零 a.e.；Divuε 的 L1≤2√n。故 Rem1.5 的输入实际成立，没有因端点非零失效。

另一方面 Mε dx 弱星趋 S，Young 的 variation upper 和弱星 lower 给 cε→c=|S|。标准 strict-convergence polar continuity（或先 Lusin 近似 dS/d|S| 再用一次齐次连续测试）给

    Θ_(uε) → (dS/d|S|)#(|S|/c)。

旧 DPR finite-measure-RHS 定理已给 dS/d|S|∈Λ_Div，|S|-a.e.。所以这个实际 law 已在 Λ 上，不需要新 GR 才知道；它的 Dirac 分解 μ=∫δ_A dμ(A) 已满足 barycenter-wavecone 要求。

额外“成分也可生成”在这里亦直接：|A|=1、Ae=0 时，取沿 e 的非负细周期 concentrating stripes f_j(x·e)，平均1、support比例趋0，设 u_j=A f_j／其 L1规范。则 Divu_j=Ae f′_j=0，值方向恒 A；条纹周期趋零给 weak limit A dx、边界无 mass，Θ≡δ_A。可先在 e-coordinate rotated cube 写出，再用 Rem1.4／细周期 averaging 在原 cube 上归一化。故固定 null 源的新“存在分解”不多给原 straight clocks 或管子族；高级来源责任不无限递归重开。

## 6. 随δ的whole-tube浓集与PSD的真正sequence后果

原 bounded unit axes i=1,...,Nδ，权 w_i≥0、Σw_i=1，取 smooth 正 kernel，Mδ=Σw_i∫vvᵀ ρδ(x−a_i−tv_i)dt。若整个 Cδ-tube union Uδ 有体积趋零，则 Mδ→0 in measure；若 Nδ δ^n→0，端点 RHS 支持在至多2Nδ个 Cδ-balls，故 DivMδ→0 in measure，L1≤2。两项是不同条件。Frobenius 归一、共同 interior 域与子列 Θ limit 付齐后可实际调用 Rem1.5／Th1.6–1.7。

μ 由 unit PSD matrices 承载，正 Choquet 分解迫 π-a.e. ν 同样由 PSD 承载。其 barycenter Bν≥0 且 singular，选 e∈kerBν 非零，则

    0=eᵀBνe=∫eᵀAe dν(A)。

正性给 Ae=0 ν-a.e.，所以这些 ν、以及 μ 本身均由 singular PSD matrices 承载。此结论用的是 PSD，不是一般 signed matrix law；总 barycenter仍可 full rank。

这给任何固定 ε>0 的全场 broad mass 消失：在 λ_min(Mδ)≥ε trMδ 的集合上，归一值 A=Mδ/|Mδ| 位于离 Λ 有正距离的闭集；由 Θ weak limit及 trace≤√n Frobenius，

    ∫_(broadε) trMδ →0。

没有从 qualitative limit 获得一个可比较 δ^η 的统一速率，更没有固定原4-plane、同一管的整 clock 分组或原跨fiber tuple lower。旧 endpoint multilinear 甚至给下面更强有限估计。

## 7. 既有endpoint multilinear的有限δ比较及真实marks

实际重新读库存 Carbery–Valdimarsson1205.6371v1 的完整 Th1（含任意方向、非负系数和 wedge 权）；其高级证明仍具名。令 k_i(x)=∫_0^1ρδ(x−a_i−tv_i)dt≤Cδ^(1−n)1_(T_i^C)(x)。Cauchy–Binet 的 ordered tuple 形式为

    detMδ=(1/n!)Σ_(i1,...,in) ∏(w_ij k_ij) |det(v_i1,...,v_in)|²。

单位方向的 wedge≤1，故以 wedge 一次方控制平方。Th1 缩放到 Cδ-tubes 给 δ^n，而上述系数提出后取 1/(n−1) 恰为 δ^(−n)，因此

    ∫ det(Mδ)^[1/(n−1)]≤C_n W^[n/(n−1)]，W=Σw_i。       (1)

同一原 family 作 n 份合法；重复 label 的 determinant 为零，不需独立方向 law 或先抽 transverse 子族。在 λ_min(Mδ)≥ε trMδ 上，(1) 给

    ||1_(broadε) trMδ||_(n/(n−1))≤C_n ε^(−1)W，
    ∫_(E∩broadε)trMδ≤C_n ε^(−1)W |E|^(1/n)。             (2)

对任意原可测 Y_i⊂T_i，直接取 Mδ^Y=Σw_i k_i1_(Y_i) v_iv_iᵀ≥0。其 determinant≤whole-field determinant，故 (1)／(2) 对其**自身** broad 集同样成立；不把 marked-broad 误作 whole-broad 子集。无需证明 shaded field 的 Div 有界。

若 kernel 支持 B_(3δ)、在 B_(2δ) 有统一正 lower，则 k_i≥cδ^(1−n) 于整个原 roundδtube，包括 endcaps：离最近轴点≤δ，沿原段至少 cδ 长仍在 B_(2δ)。因而

    ∫trMδ^Y≥cδ^(1−n)Σw_i|Y_i|≈cλW。

平均 density 可直接保真实 I；逐管 density 当然亦给此式。若 |E| 小，则 (2) 只把大部分原 mass送到局部 narrow/hyperplanar 区，尚无相同 plane／全 clock 组织。这个更强已知有限输出是本轮必须排重的责任，不是 ordinary 新界。

## 8. 真full-direction且满Hausdorff的compact null初始集

采用 R94 已审的经典 compact planar Leb-null Kakeya P⊂R²，含每个平面方向的单位段且 dim_H P=2。令

    K0=P×[0,1]^(n−2)⊂R^n。

对单位 v=(v′,v″)，|v′|≤1：若 v′≠0，在 P 的单位 v′/|v′| 段上取长 |v′| 的初始子段；额外各坐标选0或1为起点，使其速度 v″_j 在整个 t∈[0,1] 留在 [0,1]。若 v′=0，取任一 P 点。所得是原方向 v 的**整单位**段，不将每方向单独 rescale clock。可按 R91 完成可测选择得到 a0(v)，没有连续性假设。

K0 compact且 Leb-null；Fubini 给零体积。其 Hausdorff 维数恰 n：对任意 s<2，P 上 Frostman s-law 与 cube Lebesgue 的 product 给 dim_H K0≥s+n−2，令 s→2。故它绝不是 strict低维 Kakeya 反例。

取均匀 σ_(S^(n−1))，定义 S0=∫v⊗v dt dσ 沿这些真实段推前。其 trace mass1、S0(total)=I/n，端点 E0=DivS0=∫v(δ_(a0)−δ_(a0+v))dσ，TV≤2。S0／E0 均由 compact K0 承载；选 R0≥1 使 K0⊂[−R0,R0]^n。以下平移均值保持这些原段，而非造 PDE 假轨迹。

## 9. 平移均值与实际full-rank common core

固定 L>2R0+1，令 C=[−L,L]^n、V=Leb^n C。取 C 的越来越细 Cartesian midpoint grids A_j，各赋权1/J_j，概率 η_j弱趋 η=1_C dx/V。令

    S_j=J_j^(−1)Σ_(a∈A_j)(T_a)#S0=S0*η_j。

它的实际 labels 是 (a,v)，copy index 均匀、v-law 仍严格为 σ，原 clock仍为 dt／[0,1]，每条曲线 a+a0(v)+tv 是真实整 unit line。各 j 的 carrier K_j=∪_(a∈A_j)(a+K0) 是有限 compact null union，且包含全部方向单位段；dim_H K_j=n。方向重复按真实 copy 权1/J_j计，不声这是 unweighted one-per-direction δ-separated族。

S_j≥0，trace mass1、总矩 I/n，DivS_j=E0*η_j、TV≤2。对连续紧支撑矩阵测试，平移平均的 integrand 连续，故

    S_j ⇀ S∞=S0*η=F(x)dx，
    F(x)=V^(−1)∫1_C(x−y)dS0(y)。

F 是有界 PSD density（上界≤|S0|/V），support在固定 bounded box。在 open common core C_*=(−L+R0,L−R0)^n，所有 y∈K0 都满足 x−y∈C，故

    F(x)=I/(nV)，x∈C_*。                                (3)

这是实际 full-rank ac weak limit，不是仅总矩 full rank。core 中 DivF=0；全局 DivS∞ 是有限 L1 field，但一般不为零。取一个共同较大 cube Ω，使所有 K_j 的 1-neighborhood compactly contained于 Ω，源 Rem1.4 允许该固定 Lipschitz 域，boundary mass为零。

## 10. 正则化对角、Frobenius规范与真正concentration law

对每个 compact null K_j，令 ε_j<1/j 足小，使 Leb^n(N_(ε_j)K_j)<1/j；取非负 C_c^∞ 概率 kernel ρεj 支持 Bεj。端点 carrier亦在K_j，因此

    M_j=S_j*ρεj，DivM_j=E0*η_j*ρεj

的 support 都在该小 neighborhood。令 c_j=||M_j||_1，PSD点态 tr/√n≤Frobenius≤tr 和 ∫trM_j=1 给 1/√n≤c_j≤1。取子列 c_j→c∈[1/√n,1]，定义 u_j=M_j/c_j、w_j=Divu_j。

||u_j||_1=1，||w_j||_1≤2√n；u_j,w_j 的非零集体积≤1/j，故均→0 in measure。对连续测试，|S_j|≤1 和其统一 modulus of continuity 给 M_j−S_j⇀0，因 ε_j→0；所以

    u_j ⇀ F(x)dx/c，|u|(∂Ω)=0。

这实际付完 Rem1.5 的非齐次输入，没有把 w_j=0 伪造出来。球面 probability Θ_(u_j) 取弱星子列极限 μ，μ由 unit PSD 承载；GR给第6节 singular PSD 支持及可生成 Choquet 分解。

但总 barycenter 是

    [μ]=lim∫u_j dx=I/(nc)，                            (4)

严格 full rank；在 common core 的实际位置 weak limit亦为 I/(ncV)。分解的每个成分 barycenter singular，与 (4) 不矛盾。原 copy×direction×clock trace-law 仍为 η_j⊗σ⊗dt；Frobenius规范只乘同一个介于1与√n的 scalar，不冒物理方向边际已经等于矩阵值球面 μ。

## 11. 新sequence校准的边界与原时空耦合

第8–10节保持 genuine full-direction／wholeunit／bounded geometry，并生成 ac full-rank weak limit，故不能以“弱极限ac所以旧singularpolar不给信息”把新 GR 内容说成没有作用。另一方面它的 K_j 本来 dim_H=n、仅 Leb-null，正好说明这种值分布结构与完整 Kakeya 满维结论相容，不给新维数反例或矛盾。

成分 ν 的 barycenter kernel 可固定某 e，并迫该 ν 的矩阵值 annihilate e；这不是原一组 (a,v) labels 在整段上都 annihilate e。Θ 本身已先把各位置的 second moment 记成一个矩阵值，Choquet／Th1.7 的新 generators 可以重新安排全部位置和振荡；不是原 Sj 的 restriction，也不是原 tubes 的 clock-weight g≤1。即便把分布分解重新 lift 为原 value-dependent 权，沿同一 tube 权重也可随 t 变化，内部边界和原 mass须另付。

同样只知原 Y_i footprint 小，不能断言 whole Mδ浓集。直接乘 marks 再调用 GR 则要一致 L1 Div 和 RHS→0 in measure；R98 的固定 density mask TV2m 已否这种免费预算，δ^(−o(1))的发散也不等uniform有界。(2) 对 marked-field的有限估计无需这项假设且更强，但仍只给旧局部 narrow。

施工前尚未读取的 FT 部分随后已实际补读：本地 v2 的 Th1.1、§2.1 barrier 定义、完整 Prop3.4 证明、Cor3.5 及其缩放证明、Th4.1 和回到 Th1.1 的应用证明。没有声17页整篇高级 wholeproof 被新独证。Prop3.4 对一般 matrix measures 仅需 mass bounded、DivTV→0、carrier Lebesgue量→0便给 limsupΦ≤0；Cor3.5 由真实 pushforward 缩放给正 Φ 的面积×Div 下界，不能按 rectifiable 主应用粗拒这些一般接口。Th4.1 的 rectifiability、spectral positivity 和投影 carrier 则仍是额外真实输入。

其 barrier 在全部 singular matrices 上非正；对同一 ambient PSD 场，还可直接和旧 (1) 排重。有限连续 concave 一次齐次 φ 满足 superadditivity，|φ(Z)|≤L|Z| 配合双向差商给 global Lipschitz 常数 L。令 B=M−λ_min(M)I，则 B 是 singular PSD，故

    φ₊(M)≤L√n λ_min(M)≤L√n(detM)^(1/n)。

以 p=n/(n−1) 和 (1) 得 ||φ₊(Mδ)||_p≤C_φ W，任意 E 上积分≤C_φ W|E|^(1/n)；Mδ^Y 同样成立。不需 shaded Div，也不把此同 ambient PSD 比较扩张到任意 matrix measures、未付的低维 projection carrier 或全部 FT 工具。原 PSD cone含 wave cone rank-one，不能冒 GR1.9 的避波锥 cone；若另授 uniform ellipticity，已在 (2) 的 broad 责任中，不是新原假设。

## 12. 当前结论、审查与停止

实际新 primary 确强于旧单测度定性结论，算子 constant-rank／spanning、Rem1.5 endpoints、浓集规范及 boundary／Young law 均可在明列场景付清。固定 null stress 的用途完全落旧 DPR＋strict-polar／DiracΛ闭包；varying whole-tube 的 broad-mass消失又被既有 endpoint multilinear 的更强有限式 (1)–(2)覆盖。真正的新 sequence 校准 (3)–(4) 不违反主定理，且不赠 original tube/time 分组。

所以尚无 ordinary／完整 branch-saving：缺将局部 proper-plane 结构组织为保原全 clock／跨fiber质量的实际4D输入，或一个其他已付 ambient 出口。按 working 停止本直接 sequence／moment／cone／endpoint 参数续轮，不宣 GR、FT、所有 PDE 或全部多尺度方法无用。平均和逐管删选、whole field 与 marked field 的区别保持；四完整路线仍open。

以上是 A12 独立施工，自己推导不算自身独审。现已 fresh 实际全文读 root12《浓集序列的整线段输入与旧行列式估计强度门》、B12《浓集值分布、原直线耦合与既有有限broad估计》、两 spec 各5节及终 macro／next／source-scope／round 各6节。独核 B 的 weighted CV δ 幂取消、marked 自身 broad、equator 精确概率混合和 ribbon long-side variation；独核 root 原 wholeclock／RHS、strict-polar Dirac 生成、有限平移对角与 common-core full-rank limit、§9 内部 BV／零延拓不重复端点，以及 §11 全 ambient PSD barrier 旧覆盖，未见未解决 mandatory。A 的正证已由 root／B 实际全文独核，不能用本人的复算代替该独审。

本稿不预认证后续 formal、metadata、下载字节、Git 或同步。高级来源 wholeproof 仍具名，未声明新 ID、major 或新颖性，未经外部同行评审，Goal active。
