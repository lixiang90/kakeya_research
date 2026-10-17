# R0033：原 prior 归一化、加权 plank 与初始 horizon 独立审查

2026-10-17。审查对象为 supplied OAI4 原 Lemmas 2.7、2.13、2.15 和 Proposition 2.16，及已入库 companion `05-inputs.tex` 中 weighted convex/full-time plank 的直接推导。**结论：以下有限推导和归一化公式通过本次独立逐步核查；GWZ2026 Theorem 1.1 的三维 Kakeya set estimate 保留为具名高级输入。** 这不认证 companion 整篇 maximal 定理，也不认证 OAI4 整篇或高维 Kakeya。

本文件是作者独立工作稿；须另有代理交叉审查方可登记 reviewed。root 的 4.3 整合稿另在指定 review 文件审查，不将自审本文件计入独审。

## 1. 固定数据和逻辑边界

固定一条 exact N0-sequence、原 j=1/v1 或 j=2/v2、长度 L、cap 参数 S,η。K=N0^{o(1)} 可逐次增大，所涉 polynomial complexity 指数固定；先固定任意正幂 tolerance，再取 sufficiently large N0，最后缓慢对角化。每个 world 的 prior νγ 为概率，独立于 uniform time；所选 measure 为 1_E dνγ dt，不重新按成功概率归一化。world 权重 ωγ 最后求和。

使用 R32 已审的原 2.3/2.4/2.10：restriction 的典型密度稳定、joint flattening、true chart 饱和/label 知识。原 2.11 的多层 current-floor 修复不在这里追认为 R32 已审输入；本轮只需保 frozen whole layers/witnesses，不调用该额外结论。特别不把任意 analytic cap-mask 作为新的 tempered prior；需要输出选择时，使用原 tempered labels 的联合有限表实施。下文 lower/upper typical 都按原 selected law 的加权坏质量解释。

## 2. Lemma 2.7：先加 good numerator，再处理分母

固定 b<L、u>0 与 tolerance τ。记旧 terminal pure density 为 d_k(x)，旧 joint angular density 为 d_{k,v}(x)，其中 x=(γ,t,y)，k 为 terminal hidden bin；粗 hidden bin B 内含若干 k。删掉 joint upper 或 pure lower 失败的**所采 fine entries**，所得 good numerator 满足逐 entry

\[
 d^{g}_{k,v}(x)\le N_0^{-Su+O(\tau)}d_k(x).
\]

这是使用 d_{k,v}≤N0^{τ}n(L)N0^{-Su} 和 d_k≥N0^{-τ}n(L)，不是所有 v 的未删 law pointwise cap。于是固定 B,v 可先求和：

\[
 d^{g}_{B,v}=\sum_{k\subset B}d^{g}_{k,v}
 \le N_0^{-Su+O(\tau)}\sum_{k\subset B}d_k
 =N_0^{-Su+O(\tau)}d_B.
\tag{1}
\]

分母是旧 pure 总密度 d_B。若 full joint 的 bad 部分大于 good 部分，其采样质量至多两倍已删质量；其余 sampled states 上 full joint≤2 good joint，故 (1) 给所需 typical conditional cap。再作一项保 inverse-subpower 总质量的 restriction，原 2.3 保证新 pure denominator 除 power-small exceptions 外不小于 N0^{-τ}d_B；联合 numerator 只下降，故 cap 仍成立，只多付 τ。

这也说明不能先对每一旧 bin 的未删 conditional maximum 取上界，再声称 summation 合法。若换用 good-measure 的分母，也必须先通过 restriction 估计恢复它与旧 denominator 的典型比较。

对固定有限 (b,u,τ) 表，坏质量可直接求和；随后让测试数、tolerance 和 list slack 足够慢地变化，使异常质量小于当前指定 inverse-subpower selection。归一总 selected mass 对条件分布没有影响。若要真实输出 cap 选择，则联合 flatten 原 labels/observations，付 TV error 后用 tempered cell table；这不要求 good analytic mask 自身先是 tempered。

## 3. Lemma 2.13：概率结构和密度公式

### 3.1 新 world prior 与总 mass

parent atlas 在 depth r<L，每 interval 长 q。c=(γ,I,A_c)，ν_c=νγ(A_c)，J_c=|det D_c|。assignment 在同一 interval 内互斥。令

\[
 Z=\sum_c\omega_{\gamma(c)}q\nu_c,
 \qquad\omega'_c=\omega_{\gamma(c)}q\nu_c/Z.
\]

若旧 atlas selected mass 为 M≥K⁻¹，则 M≤Z≤1。新 world prior 是 νγ(·|A_c)，新 time τ uniform independent，t=t_c+qτ。旧已指派 selected measure 在该 chart 上除 qν_c 后，恰为新 product prior 的一项 event restriction；总 weighted selected mass为 M/Z。**不能以 m_c 而非 ν_c 条件化 trajectory prior。** 否则 prior 依赖 time-success，原独立模型和 lift 公式均会改变。

极轻 conditional-prior chart 可删：chart 数 polynomial，旧 selected mass≤qν_c，故取足够小 reciprocal-polynomial 阈值后全局损失 power-small。其余 chart 条件密度高度仍 polynomial；无系数 height 下界要求。

### 3.2 模型和 coefficient-space Jacobian

作 t=t_c+qτ、y=y_c(t)+D_c z。endpoint containment 给 |z|+|V'|≤K，其中 V'=qD_c^{-1}(V−y'_c)。

- v1：若 parent test=w−F(t,y)，设 w'=(w−F)/a_r。沿每条 parent whole trajectory 为有界二次式；w'−G 的模型闭合。
- v2：保留 hidden 值 w，用 parent test P/a_r 作新 native test，B'=B/a_r。parent whole-block 小值、upper derivative 与 selected lower derivative 正好给新 native bounds；curvature 为 |P_{ww}|/a_r≤K B²/a_r²=K(B')²。

因此 v2 新 native 一般是 **P_parent/a_r**，并非旧 P*/a_r。只有 r=0 且旧 native 已满足新 spatial chart 的全套 bounds，才可选择原文允许的保留旧 native 例外。

系数变换有常 Jacobian。base coefficients (y0,V)→(z0,V') 的 determinant 绝对值为 q^j J_c⁻²。v1 的 hidden coefficient map 在 fixed base coefficients 下 triangular，det 为 q³/a_r³；v2 time-reparametrized affine hidden coefficients 的 det 为 q。故全 coefficient map 可逆且常 Jacobian、双方 polynomial control；piecewise-constant semialgebraic prior 保持原格式。这里 determinant 是 coefficient-space 的，不可与 observation-base 的 qJ_c 混用。

### 3.3 Terminal equality 和 intermediate upper

固定 chart 与旧 exact base，new depth s hidden bins对应旧 width a_{r+s}/B；v1 有确定的 base-dependent translation，v2 无 hidden-coordinate 缩放。两种 half-open grids 彼此至多固定重叠。把旧已指派 selected measure 按 chart label refine，密度记 ρ_c。对 transported bins，base 变换给 dt dy=qJ_c dτ dz，而 product prior 归一为 1/(qν_c)，所以

\[
 \rho'_c=(qJ_c)/(q\nu_c)\,\rho_c
        =(J_c/\nu_c)\rho_c.\tag{2}
\]

world weight 与 Z 都不在 (2) 的 within-world factor 内。将 (2) 按新 world 权重求和时，旧加权坏质量仅乘 Z⁻¹≤K，因此仍 power-small。

原 parent label 已知于 p_L，label refinement 只有 K 个 sampled 值；经 restriction/refinement 引理和 bounded grid overlap，terminal refined pure density仍 ∼log n(L)。因此

\[
 n'(L-r)\sim_{\log}n(L)J_c/\nu_c.\tag{3}
\]

在早期 depth r+s，chart label 未必已知，refinement 只给 upper，故

\[
 n'(s)\le N_0^{o(1)}n(r+s)J_c/\nu_c.\tag{4}
\]

若 label 已知于 p_r，则也已知于所有更细 p_{r+s}，同一 list argument 给 (4) 的反向 typical 比较。prepared true parent 由 2.10 有 ν_c∼log n(r)J_c，从而 n'(s)∼log n(r+s)/n(r)、n'(0)∼log1。

不同 c 的 J_c/ν_c 先按 logarithmic type homogenize，才记一个新 common profile；选择 type 只付 inverse-subpower mass。这里没有要求世界权重或 f(0) 绝对值一致有界。

### 3.4 Cap class

由 (3)(4)

\[
 f'(L-r)-f'(s)=\log_{N_0}\frac{n'(s)}{n'(L-r)}
 \le f(L)-f(r+s)+o(1)\le d(L-r-s)+o(1).
\]

注意 upper 的方向正好足够保持 endpoint cap；同一 upper 不足够 lift intermediate true floor。

new velocity bin width a_u 在旧 V-space 的像含于半径 K a_u 的 ball，因为 ∥D_c∥/q≤K。它可盖 K 个旧 angular bins；depth u≤η(L-r) 仍在旧允许范围。先对已经剔除异常的旧 joint numerators 求和，再乘 (2)，以 (3) 的 terminal pure density 比较，可得同一 S,η 的 new angular cap。异常需按原 law 移除后才求和，不能在许多 chart 中重复消费未删坏质量。

## 4. Full assignment、true lift 和 tempered composition

child chart 在 parent new world 中的相对时间、Jacobian、selected mass为 q_d,J_d,m'_d。拉回旧世界：

\[
 q_{cd}=qq_d,\quad J_{cd}=J_cJ_d,\quad
 m_{cd}=q\nu_c m'_d,\quad
 m_{cd}/q_{cd}=\nu_c m'_d/q_d.\tag{5}
\]

child terminal floor配 (3) 得旧 floor K⁻¹ n(L)J_cJ_d。若 child 为 intermediate depth s，只有 intermediate equality 才给 n(r+s)J_cJ_d；(4) 的 upper 不能反向使用。故 terminal-known atlas 足够 terminal lift，但不能免费得到其全部 intermediate true layers。

tests 拉回为 v1 的 w−F−a_rG(τ,z)，或 v2 的 a_rQ(τ,z,w)。后者 first derivative 尺度 B；curvature≤K a_r(B/a_r)²/a_s=K B²/a_{r+s}；小值≤K a_{r+s}。affine base changes 保持 total degree≤2。

空间矩阵相乘、time interval 嵌套，∥D_cD_d∥≤Kqq_d；disjoint assignment 是在每一 whole trajectory 上取 child assignment 的 pullback，保留整条 parent path，而非为不同 incidences 另选 parent。dyadic common partitions可相乘得到统一 finer partition。旧 parent label 与新 child label 的 K×K lists 在 transported terminal observation 下合并，保持 known。

有限层 paths 可作为内部 trajectory index/有限 predicates 编码；不以 selected mass 重置 ν_c。日后缩小 incidences 时，旧 true floor只可作同一 frozen law 的 witness；若要求所有层在最后 current measure 上仍 true，则还须独立支付原 2.11 的 simultaneous pruning 和原 assignment budgets。这不是本轮路径结论所需输入，也不由 (5) 自动免除。

v2 narrowness 完全按 determinant相加：q_{cd}²/J_{cd}=(q²/J_c)(q_d²/J_d)，不要求轴平行。最大的轴 ∼log q 是额外的 2.12 结论，不是 determinant 恒等式本身。

## 5. Weighted convex clustering：任意正权和 repeats

本节唯一深层输入为 saved companion 所陈述的 GWZ2026 Theorem 1.1：三维 δ-tube set 满足 Δmax≤δ⁻η、average shading density≥δ^η，则 union volume≥δ^εΣ|T|。下面不调用 companion 其它 maximal 部分。

固定 bounded ambient chart，T_i 为 common volume vδ∼δ² 的 convex tubes，repeat indices允许。假所有 convex K 有 Σ_{T_i⊂K}ω_i|T_i|≤A|K|，且每 index |Y_i|≥δ^η|T_i|。令 v_i=ω_i/A；取 K=T_i 给 v_i≤1，取固定 enclosing ball给 S=Σv_i≤Cδ⁻²。

独立以概率 v_i 采每个 **index**。对任意含 tube 的 K，先截 enclosing ball，再用 John ellipsoid 取包含它的 box Q，volume≤C|K|，shortest width≥cδ、largest width≤C。以 cδ² 网量化 center、axes、frame 后扩大 sides，得到 polynomial 大小的 universal box net，仍 containment且 volume比较不变；含 tube 的 Q 必有 |Q|/vδ≥c。

每个 net Q 的 sampled count Z_Q 是独立 Bernoulli 和，EZ_Q≤|Q|/vδ。Chernoff/指数矩界及 polynomial union bound 给，概率≥3/4 时同时 Z_Q≤C(1+log(1/δ))|Q|/vδ。若 S≥C log(1/δ)，另有概率≥3/4 的 sampled total≥S/2。两事可同时发生，取一 realization。John comparison 将 net cap转为所有 convex 的 O(log) cap。

对同一重复 tube，取 K=T 说明 sampled multiplicity≤C log。每 distinct tube保一个 sampled index，仍至少 cS/log 个 tubes；保该 index 自己的 Y_i，故逐 index shading density 保留，不必合并不同 shadings。丢弃其它 index 在这里不需要保它们的 shading mass：原 weighted numerator另由 Σω_i|Y_i|≤ASvδ 控制。

选择 GWZ target ε/2，η 小于其 density tolerance；小 δ 时 log cap≤δ⁻η。于是原总 union至少 cSvδ δ^{ε/2}/log，推出 Σω_i|Y_i|≤CAδ⁻ε|∪Y_i|。S<C log 时直接逐点 Σω_i1_{Y_i}≤AS 即可；剩余 bounded δ 区间由 Σω_i≤CAδ⁻²吸入常数。结论独立于 index 数和权跨度，未作 min-weight 截断。

## 6. Full-time plank、连续 law 与 long marks

对 bounded affine traces (t,b_i+tu_i)，每条用 common fixed Euclidean length的 Cδ-tube T_i 包住，并向两端延长固定余量，使 chart trace 上所有小 balls 均在 tube内。

若 convex K 含若干 T_i，John enclosing ellipsoid 的 time diameter≥1；horizontal slices 的 center affine、空间主轴固定，slice semiaxes为固定两轴乘共同 scalar。最大 slice area≤C|K|。以其 circumscribed rectangle 按 affine slice center平移，得含全部 counted **whole traces** 的 full-time plank，area uv≤C|K|、各轴≥cδ。bounded chart保证 upper widths≤C。原允许 δ≤u≤v≤1：固定倍数的上下 cutoff可通过 enlargement及按 t=0,1 endpoint 分有限个 intervals延伸；area成本仅固定常数。故 plank cap Σω≤Auv/δ² 蕴含 Σ_{T_i⊂K}ω_i|T_i|≤CA|K|。

对每 index 的每 marked bin center，在 trace上放 radius cδ ball；同一 index 的 balls 因 time separation δ 而互不相交。所以 |Y_i|∼#J_i δ³，每 index density≥cδ^η；union≤Cδ³#Evis。对 common length作固定 rescaling，取 long-mark η 小于 weighted convex 输入 tolerance的一半，固定常数都可吸收。约去 δ³ 即原 Lemma 2.15。这里只在 GWZ 应用时使用 per-index long marks，不能以总平均 mark count代替。

连续 law 的使用也是合法的有限逼近：以远细于 δ 的 coefficient mesh 取 representative，按 rounded coefficients 和整套 finite mark set分组，每组权为原 prior mass。mark subsets可能很多，但总数有限；此估计与 index 总数无关，且这些 mark-set labels不作为最终 atlas的输出。rounding全时间误差≪δ；扩大 cells、planks固定倍数即可同时控制原 family 的 cap和访问数。判定 full-time containment 时须扩大 whole plank，不能只恢复 marked points。

子幂 chart bound可先 common spatial rescale到固定 chart，counts/marks/caps只付 subpower；工作网是 N0 的固定幂，long duration≥K⁻¹对每一固定 ε 的 long-mark threshold最终足够。ε↓0只能在 fixed-ε 定理生效后慢选。

## 7. Proposition 2.16：旧 witness 与当前残余严格分开

### 7.1 初始 blocks、group知识与 native test

选 dyadic q∼a_L。在每 world、每 q-block I，以 midpoint y 的 q-bin 和 native X 的 a_L-bin分组 G。X(t)为 globally bounded quadratic，因此其 coefficients和导数≤K，whole I 内 y、X 均变≤Kq。观察 p_L 的 exact t,y与 hidden bin将 X(t)定位到 K a_L：v2 以 native first derivative及 curvature Taylor，误差≤K a_L+K a_L²。故 G 在 p_L 下只有 K 个可能值。

以 X-bin center b_G 作 test，v1用 w−b_G，v2用 P*−b_G。whole block小值≤K a_L；upper derivative 和 selected lower derivative沿用 native；native curvature K B²也满足 terminal允许 K B²/a_L。这里不需要另拟合 w。

以 y-midpoint-bin center平移，空间除 Rq、block time除 q，R足够大且 subpower；全部 traces进入固定 bounded chart。记 J0=(Rq)^j。**group内仍用旧 νγ|G，不除 νγ(G)**，只有 time变为 normalized unit。original normalized selected mass记 m_G≤νγ(G)。在 retained典型 entries，按 known G refine p_L，再合 compatible hidden bins，得到 group exact-base density至少 N0^{-ξ/4}n(L)J0。

### 7.2 工作网、greedy 与 complexity

先固定 ρ=D_m⁻¹∼N0^{-D}，D足够支付 tempered complexity、group/block coordinate changes和所需 TV；随后才选 ξ∈(0,1)。joint flattening作用于原所有 groups/worlds 的联合 law，不是把任意 analytic mask当输入。由典型 lower及 TV，除全局 power-small mass外，所在旧 group cell的**旧 whole-cell mass**至少

\[
 N_0^{-\xi/4}n(L)J_0\rho^{j+1}.\tag{6}
\]

在各 group 贪心找 full-time spatial planks，orthonormal axes任意、center affine、ρ≤r_i≤C。当 remaining incidences 上 whole contained trajectories 的 normalized mass≥N0^{-ξ}n(L)J0∏r_i 时，assign **所有**这类 available trajectories并从 group删除。assignment按 entire endpoint containment；test一直是该 G 的固定 native test。

每步删除至少 reciprocal-polynomial mass，因为 ξ<1、r_i≥ρ，且 n(L),J0为固定幂。总 within-world group mass≤1，故步数有 ξ-uniform polynomial上界。center/speed可改用一条 contained bounded trace并固定扩大 widths控制；frames为有限 real constants，无 height约束。whole endpoint tests、此前 exclusions及 group labels均为 polynomial count、bounded-degree predicates，因此输出 tempered，不要求 measurable搜索过程具有低复杂度。

### 7.3 若覆盖不足，则找真实可接受新 plank

假 global initial selected mass M≥K⁻¹，但 greedy覆盖不足 M/2。残余先删未满足 (6) 的 cells，再删 normalized surviving duration<M/C 的 trajectory–block entries。前者 power-small；后者加权损失≤M/C，因为 Σ_{worlds,blocks,groups}ωγ qνγ(G)≤1。保≥cM，每条 used trace的 surviving duration≥K⁻¹。

由 weighted averaging，有 group 的 surviving mass m'_G≥m_G/K。该 group所有 surviving visited good cells的数量至多

\[
 \#\mathcal C_G\le
 \frac{m_G}{N_0^{-\xi/4}n(L)J_0\rho^{j+1}}.\tag{7}
\]

分子是旧 group mass，分母是 (6) 的旧 witness floor，二者为同一 law。当前 residual cell可以只剩任意小质量；证明从未给它 (6)。

每 used trace 标出有 positive surviving duration的全部 time bins。duration≥K⁻¹意味着 marks≥D_m/K，weighted marks总和≥D_m m'_G≥D_m m_G/K。移动到 bin center只须固定 cell enlargement。

若 j=1，独立加入 static dummy z∈[0,1] uniform；marks不变、总权不变，visited cells增加≤Cρ⁻¹。此 dummy仅为应用 analytic plank estimate，不输出为新 exact problem，也不假定它在 full coefficient space 有 Lebesgue density。两种 j 都因此给

\[
 \frac{\int\#J_l\,d\nu(l)}{\#E_{vis}}
 \ge K^{-1}N_0^{-\xi/4}n(L)J_0\rho^2.\tag{8}
\]

以 A*=sup_P ρ²ν(used whole traces in P)/(uv) 应用 2.15，由 (8) 得一个 full-time plank

\[
 \frac{\nu(used\cap P)}{uv}
 \ge C_\varepsilon^{-1}K^{-1}N_0^{-\xi/4}D_m^{-\varepsilon}n(L)J_0.\tag{9}
\]

若 sup未 attain，取固定近似最大值即可。连续 rounding恢复 whole traces时的固定扩大已在 cutoffs中预留。

### 7.4 j=1 投影回去不损 area比

padded rectangle 的投影半宽 W=u|cosθ|+v|sinθ|，每条 vertical chord≤2min(u/|sinθ|,v/|cosθ|)，其乘 W≤Cuv（轴向极限亦成立）。对每原 trace，可被 P 接受的 static dummy比例≤Cuv/W，因为只取任一时间的 chord已给 upper。因此

\[
 \nu_{pad}(P)/(uv)\le C\nu_{orig}(P_{proj})/W.
\]

projection center仍 affine、ρ≤W≤C，故得到原 j=1 greedy允许的 whole-time interval plank。dummy label不需从 p_L恢复，也没有进入最终 chart assignment。

### 7.5 矛盾与 ξ 慢对角化

每一 counted 原 used trace还有 duration≥K⁻¹，故 (9) 给 remaining incidence mass/面积至少其右侧再除 K。选固定 ε使 Dε<ξ/4，则 ξ/4+Dε<ξ/2；subpower和固定常数可吸收到剩余 ξ/2。于是 remaining mass严格超过 greedy阈值 N0^{-ξ}n(L)J0乘相应面积，矛盾。

所以至少覆盖 M/2。每输出 chart旧 spatial Jacobian为 J0∏r_i，满足 true floor N0^{-ξ}n(L)J。先各固定 ξ 的证明在足够大 N0生效，再让 ξ↓0；polynomial step count、工作 D和predicate degrees独立于 ξ∈(0,1)，故输出仍 tempered。原 time q∼a_L，h=L+o(1)，得到 H(E)≤L。

这个结论不要求 E∈C(d)，也不付任何 j=3 extension；使用 j=1/2 与具名三维 set input十分实质。

## 8. 对 critical path 主稿的接口结论

1. 原 2.7 可用，但其 cap是 sampled typical cap；必须准备 good law，保原 denominator。
2. 原 2.13 可用且保持同一 S,η；terminal lift与 intermediate lift的条件不相同。
3. 原 2.15 和 2.16 的有限推导可在 GWZ set estimate具名条件下使用；无需 companion 整体 maximal证明。
4. 所有 nested true layers若要求最终 current floor，需明确 simultaneous pruning；只记 frozen witness也合法，但其 cap必须针对同一冻结 law。不能将两者在后续计数混用。
5. 本次未发现需要削弱原 statements的 counter；也未通过本文件提前认证 4.3 的极值、finite/infinite narrowness和双极限量词。

来源：`literature/extracted/openai_2026_four_dimensional_kakeya.txt` 原2.7/2.13/2.15/2.16；`literature/primary/openai_3d_maximal_source/05-inputs.tex` 的 `weighted-convex-set`、`weighted-set`（part-source边界见同目录README）。
