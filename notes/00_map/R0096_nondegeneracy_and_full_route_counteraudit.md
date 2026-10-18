# R0096：原观测商、非退化量词与完整四路反攻

2026-10-19，B。依 R0096 reselection/working 及施工前另锁 uniform-polynomial 三份五节规格，仅编辑本分配稿。具名 GGW 高级 wholeproof 不新认证；以下初等原 CW 商和 proper 用途需独立全文审查，未经外部同行评审。

## 1. 恢复、四完整路及旧接口边界

已实际读本轮两 spec、GOAL、当前 STATE、R95 next/source、ROADMAP 更新段与四路表；未改中段沿此前实际完整读取复用。原 registry78 的 ID/status 沿 R95 逐项读取及本轮主代理恢复记录，不自行声称 fresh Git/远端核验。R95 实际资格/两审/归档是 progress，未给 ordinary/fullbranch saving。

四完整任务分别是 ordinary allscale 初始化与强 Hausdorff 读出、HRZ 全 parent/terminal/coarse/narrow 费用、sticky 临界 κ=1/余 mixed 和 ordinary 桥、同一 full-direction 欧氏集合的严格低维构造。本轮只从完整 bounded mixed42 的 scalar native 观测出发；若仅排 fixed-polynomial proper 类，不能视为解决任一完整任务。已有 DIM/KT、CP/PM/PW、R74 标签阈值、R95 直接平面小改冻结保持。

实际重读 R14 的 GGW osculating 审计和 R19 global residual 的 finite GGW 接口。R14 的 R6 到 R4 双块一阶 Grassmann rank2 障碍不能抄到这里：当前 V_t 是一行，形式上总能令 Γ'=V。真正待付的是原曲线的 smoothness、点点 jet 非退化和统一条件数，不是再次否认 scalar 切线表示。

## 2. GGW 原定理的真实尺度和量词

实际读库存 GGW2211.09508v2 物理1–4对应 text 的 (1.4)–(1.6)、Th1.2、(2.1)–(2.6)，以及固定 moment/perturbation 说明。原非退化是 fixed smooth Γ:I→R^n 且每个 t 都有 det[Γ',...,Γ^(n)]≠0；不是全区间 row-span 满秩。m=1 时需 0<α<1。

采用的有限输入是 Th2.1：支持于固定单位球的非零测度 μ、全尺度 c_α(μ)<∞；每个时间 mesh 的法向 plates 为 δ×1^(n-1)，每个 support 点参与至少 δ^(ε-1) 次，输出

\[
\#\mathcal W\ge c\,
\frac{\mu(\mathbb R^n)}{c_\alpha(\mu)}
\delta^{-1-\alpha+L_n\sqrt\epsilon},
\qquad L_n=10^{10n}\text{ 可用}.
\tag{1}
\]

source 先在 literal moment Γ=(t,t²/2!,...,t^n/n!) 下写定理/证明，再说明 fixed 非退化曲线的稳定用途；不能将固定曲线的常数和 cutoff 读成所有随 δ 变化曲线的 uniform 定理。归一化 scalar V_t 只改变有界 covector 长度，不免费改善小 jet；定性 a.e. Th1.2 也不替 (1) 的逐点参与/有限 δ 结论。

## 3. 至少五个观测的 uniform 正交 CW 商

设 bounded 原轴 x_λ(u)=a+ub，λ=(a,b)∈R^8，原概率 μ=Uniform(T)，原 normalized whole-CW 常数 K。任取至少五个不同 times J 与任意 bounded β_t∈R³，令

\[
n_t=(-\beta_t,1),\quad V_t=(n_t,t n_t),\quad
S=\operatorname{span}\{V_t:t\in J\},\quad H=S^\perp.
\tag{2}
\]

对 H 取正交基 Q=[A;B]，m=dimH。每 t∈J 有 n_t^T(A+tB)=0，所以 rank(A+tB)≤3。若 m≤3 此结论已在所有 u 自动成立；若 m≥4，其每个4-minor 是次数≤4多项式，五个不同 t 的精确零使它全实 u 恒零。此处没有 time-gap 倒数、Remez 或近零插值费用。记 r_0=max_u rank(A+uB)≤3。

精确压缩给某 e∈{0,...,r_0} 和子空间 H_1⊂R^m、E⊂R^4，

\[
\dim H_1=m-r_0+e,\quad \dim E=e,\quad
A H_1+B H_1\subset E.
\tag{3}
\]

为完整核此步，取达到 r_0 的 u_0，把 A+u_0B 以可逆基写成 diag(I_(r0),0)，B 分块为 (C,D;F,G)。小参数 Schur complement 恒零给 G=0 和 FC^jD=0。U=span{C^j imD:0≤j<r_0} 满足 CU⊂U、FU=0；取 H_1=U×R^(m-r_0)、E=U×0，恢复原基并由 A=(A+u_0B)-u_0B 得 (3)。r_0=0 时 A=B=0 直接成立。GL 化只证明 subspace 存在，不用其可能病态的基覆盖原管。

若 P_Sλ 落一个半径 r≥δ 的 ball，选一条命中的原管 λ_0，写 λ=λ_0+Qz+e_S，|e_S|≤2r、|z|≤C。用原 Euclidean 正交坐标按 R^m/H_1 的 r-grid 覆盖，至多 Cr^(-(r_0-e)) 个补参数格。每格的 whole 原轴在某个 (e+1)-affine plane 的 Cr 邻域，round 半径由 r 支付；bounded chart 给真实 convex box 体积 ≤Cr^(4-e)。原 CW 对各箱求和，保原 N，得

\[
(P_S)_\#\mu(B_r)\le C K r^{4-r_0}\le C K r.
\tag{4}
\]

常数只依 fixed dimension/chart。m=0 可取 H_1=E=0、r_0=0，系数球直接对应 whole-line 的 r^4 箱；大 r 用概率≤1 调固定常数。一般 m 小、left/right/regular pencil 退化均含在 (3)，不需抽取新的原管 carrier、AD lower 或小标签。

## 4. 固定多项式的系数 law：满八阶不是必要输入

固定 D 及一个固定 β(t)∈R³ polynomial，degree≤D。令 C_β:R^8→R^(D+2) 为

\[
F_t\lambda=n_t\cdot(a+tb)
=\sum_{j=0}^{D+1}(C_\beta\lambda)_j t^j
\tag{5}
\]

的 monomial 系数图。S=(kerC_β)^⊥ 等于全观测 span；在有限 Z 含至少 D+2 不同 times 后也等于其 V_t span。kernel 中全部轴满足 F_t=0，故第3节的 exact rank/compression 可直接用。

C_β|S 的最小非零 singular value 倒数 L_β 是固定常数。一个 coefficient r-bin 的原像只在某 affine kerC_β 的 C L_βr 邻域；故由同一补参数 cover/CW 求和，

\[
(C_\beta)_\#\mu(B_r)
\le C_\beta K r^{4-r_0}\le C_\beta K r,
\quad\delta\le r\le1.
\tag{6}
\]

若 L_βr 大于 fixed chart 尺度，用 trivial probability bound，常数仍只进 C_β。ker=0、r_0=0、低 rank image 都已包含；GGW 可作用于低维支持的测度，不要求 coefficient image 满 R^(D+2)。只有正交商 (4) 不付 conditioning；从正交 S 到特定 monomial 坐标的 (6) 才付 L_β，不混淆两者。

因此即便 V 在 R^8 没有 full8 jet，仍可在 literal R^(D+2) moment family 中使用 (5)。这比只测 β=(t²,t⁴,t⁶) 更宽，但结论仍是已有 GGW/R74 工具的 fixed-polynomial 源应用，不是完整 rough 分支的新解决。

## 5. 原质量、mollification 与 proper 完整用途

完整 mixed42 给原访问平均 ≥K^-1δ^-1 和每 time native labels #Y_t≤Kδ^(-1+κ)。先 tube-heavy 保原管质量 K^-C，并让每管保其全部原 visits；CW/商 upper 的归一化常数相应乘 K^C，原全 T/N 仍不改。不能先把任意 time 限制说成逐管近满。

对 coefficient pushforward 在 Cδ 小球上 mollify，support 归一到 fixed 单位球。(6) 的 δ 以上一维 ball bound 给 δ 以下密度 upper C_βK^Cδ^(1-n)，n=D+2；于是任意固定 0<α<1 的全尺度 c_α≤C_βK^C。每个 mollified support 点可继承某条原 heavy 管的全部旧 visits；系数扰动和 fixed bounded monomial covector 仅将目标 label 加厚 O_β(δ)。有限参与不是只在原离散 atoms 上成立。

原 times 以可比 fixed δ mesh 聚合，fixed polynomial 的有界导数使误差 O_β(δ)；每 mesh 格只合 O(1) 原 times，选有限颜色保实际每管 fixed 比例 clock。空 time 格给空 targets，长向覆盖 fixed coefficient ball 只需每 label O_β(1) 个 plates。故诚实 upper

\[
\#\mathcal W\le C_\beta K^C\delta^{-2+\kappa}.
\tag{7}
\]

取 (1) 的 n=D+2、m=1、α=1-κ/4，先选 theorem ε 使 L_n√ε<κ/8，再选 source η 足小支付原 heavy/participation/权成本。δ 最后小可依固定 β 吸收 C_β，lower ≥C_β^-1K^-Cδ^(-2+κ/4+L_n√ε) 与 (7) 矛盾。没有额外 angular physical separation、independent clock 或 conditional ADlower。

这付的是每个 fixed-polynomial β 的完整源 proper subclass；δ_0 可依 β 的非零 singular values，不能交换为所有随 δ 变化 β 的 uniform 结论。R19 旧 fixed scalar residual/moment 用途保留，R95 β affine 的 native 曲线仍非直线不妨碍这里把它视为线性 moment 投影。

## 6. Full moment 透明校准及条件数所在

取 β=(t²,t⁴,t⁶)，则 V 的八个坐标按顺序为

\[
(-t^2,-t^4,-t^6,1,-t^3,-t^5,-t^7,t),
\]

即 monomials 0,...,7 的 fixed permutation/符号。故 |det(V,V',...,V^(7))|=∏_(j=0)^7 j!，Γ' =V 为 fixed smooth 非退化曲线。这只是透明 proper 校准，不是 source 必须出现此模型的证明。

若改为 β_ε=(εt²,t⁴,t⁶)，上式两个坐标被乘 ε，因此 Wronskian 正比 ε²；所有 fixed 阶 C^k norms 在 ε↓0 时仍有统一 upper。仅说每次 determinant 非零，不给其 lower。将系数作 inverse diagonal normalization 会把对应参数方向的长度/measure Frostman 常数或 plate 精度改变 ε 的负幂，这不是无损坐标选择。

正交商 (4) 对这些观测依然 uniform；第4–5节 fixed-polynomial 结论也依然成立。此校准不否定两者，只提醒 β_δ 的 conditioning 和 δ_0(β_δ) 未被 fixed-curve 定理自动支付。

## 7. Smooth、单调分量且全 row span8，仍可处处零八阶 jet

取三个内部不交 closed supports 的非零 C_c^∞ bumps ψ_i，support 间和外部都留 open gaps。令

\[
\beta_i(t)=t^i+\psi_i(t),\quad i=1,2,3,
\tag{8}
\]

幅度足小，使 β 有统一 bounded/Lipschitz norm 且 β_1'≥1/2。故连“某 open 区间完全常值”都不是下述失败的原因。

若 1,t,β_i,tβ_i 有一个全局线性关系，则它是 degree≤4 的 polynomial P(t) 加 Σ_i(A_i+tB_i)ψ_i(t)。在外部 open gap 得 P 恒零，再在各 bump 的非零 open 核逐一得 A_i=B_i=0，最后常数/t 系数亦零。因此八个函数全局独立，原 V_t 的全 interval row span 为 8。

但每个 t 的足小邻域至多有一个 active bump；在该邻域，所有八函数落在

\[
\operatorname{span}\{1,t,t^2,t^3,t^4,\psi_i,t\psi_i\}
\]

的至多七维空间内。support 边界的 jets 全平同样成立。因此 det(V,V',...,V^(7)) 在每个 t 都等于 0。这严格否定 global nonconstant、uniform smooth/Lip 或全 row span8 免费推出 GGW fullambient8 非退化；不否第3节商 law，不排 lower ambient/factorization/proper polynomial 的别种用途。

这个是 β 数据的弱接口反攻，不是完整 source。可给它附原 R95 的真实单位 bush，保 joint4AD/wholeCW 和显示法向，但并未证明它的原 visits 落在 small native labels、具有正 κ point-Φ、两套 filled grains、selected ξ/coherence 与全部 source 限制；不能由此宣布 mixed42 或 Kakeya 为假。

## 8. 随 δ 非零 torsion 不给无条件数的 finite theorem

令 ε=δ^A，A>1，并用第6节 β_ε。取 R^8 参数空间一条 fixed 短 e_(a1) 线段上的归一 Lebesgue μ_0。对任意固定 0<α<1，c_α(μ_0)≤C_α；其每点满足

\[
|F_t\lambda|=|\epsilon t^2 s|\le C\epsilon\ll\delta
\quad(t\in[-1,1]).
\tag{9}
\]

对每个 δ-net time 选择一个以 0 为中心、短轴沿 V_t、尺寸 δ×1^7 的真实 rectangular plate；线段取足短后整个 μ_0 support 都在该 plate 内。每 time 的其余 plates 可平移排成 disjoint tiling，故选中 plate 合法。不同 t 的短轴不同（V_t 含固定坐标1和t），于是 #W≈δ^-1，每个 support 点有完整 δ^-1 参与。

如果将一般 fixed-curve GGW 的常数及 cutoff 无费 uniform 化到这一 δ-dependent 曲线族，选 theorem ε_th 使 L_8√ε_th<α/2，则 (1) 会迫 #W≥cδ^(-1-α/2)，矛盾。因此即使每 δ 都是 smooth/full nondegenerate 且全 derivative **upper** 有界，也不能忽略 torsion lower/conditioning。若 ε 是一个 fixed 正数，再令 δ↓0，(9) 不再落于一块 δ-plate，完全不反原 fixed-curve 定理。

μ_0 不是原 joint4AD/CW 管概率。此例只反上述 **不带条件数的泛化定理接口**，不反第3节的原 CW 商、加强的 coefficient law 或完整 source；也不证明实际 source 不可能另行支付统一几何。

## 9. 新锁题的统一 bounded-degree 分支：谱gap与近压缩独核

本节新增施工严格在另行五节 `R0096_uniform_polynomial_spec.md` 锁题后进行。仍固定 D、系数 upper B，允许 β=β_δ 任意依赖 δ；不是从 arbitrary dyadicLip 原源提取 polynomial。以下不再把第6/8节的弱测度反攻误用于具有原 whole-CW 的系数 law。

取固定 0<ε_*≪κ，并取 M 足大。令 a_j=a_0(ε_*/(4M))^j，j=0,...,8，a_0<1/4 固定。先将 source η 取小于全部 a_j 的固定小倍数，逐一取原 allowed ρ_j，其实际 exponent e_j=logρ_j/logδ 在 [a_j,2a_j]。相邻候选的 singular-value exponent 区间 (ε_*e_j,M e_j) 不交，因为

\[
M e_{j+1}\le2M a_{j+1}=\tfrac12\epsilon_*a_j
<\epsilon_*e_j.
\tag{10}
\]

C_δ:R^8→R^(D+2) 最多八个非零 singular values，故九个开 band (ρ_j^M,ρ_j^{ε_*}) 中至少一个无 singular value。选该 ρ；以 SVD 正交截断定义 C_s、C_w，边界分别分入 strong/weak，则

\[
s_{\min}^{+}(C_s)\ge\rho^{\epsilon_*},\qquad
\|C_w\|\le\rho^M,\qquad C_\delta=C_s+C_w.
\tag{11}
\]

零 singular values 一律进 weak，不除它们。范数上界只依固定 D/B。allowed 取整是在固定九个目标 exponent 后选 η，因而不根据 δ 的奇异值再无限细分尺度。

令 H=ker C_s，取其原正交基 Q=[A;B]。对所有 bounded 实 clock u，原 polynomial 相位满足

\[
n_u^T(A+uB)=p_D(u)C_wQ,\qquad
\|n_u^T(A+uB)\|\le C_{D,B}\rho^M,
\tag{12}
\]

其中 p_D=(1,u,...,u^(D+1))、|n_u|≥1。若 m=dimH≥4，每个4-minor 的绝对值在一个固定实 interval 上≤Cρ^M；在固定五点插值即使全部 degree≤4 系数≤Cρ^M。这五点不是源 visits，不需源钟质量，也不付 β 的非零 singular 值。m≤3 则直接走全 H 网格，不调用 minors。

R74 的定维稳定可在这里完整适用：在 bounded (A,B) 的固定 compact 域，定义 Ψ 为 e=0,...,3、dimH_1=m−3+e 和 dimE=e 的正交 Grassmann 上的最小泄漏。其平方为 compact 多项式约束下连续半代数最小值；精确全部4-minors为零时，第3节 Schur 压缩（必要时缩小 H_1）给 Ψ=0。最大函数 sup{Ψ²:D_min≤s} 趋零且一元半代数，固定 QE/一元多项式最低非零项给 Ψ≤C D_min^{c_*}。故存在真实正交 H_1/E，

\[
\dim H_1=m-3+e,\quad\dim E=e,\quad
\|(I-P_E)A P_{H_1}\|+\|(I-P_E)B P_{H_1}\|
\le C\rho^{Mc_*}.
\tag{13}
\]

这个 c_* 与 C 只依固定维数/范数 upper，不依 SVD gap 或某个 Kronecker 基。若 m≥7 且 Q 是 joint isometry，精确奇异零集为空，compactness 给 minors 固定正下界；因此足小 ρ 不会出现此支，不以不存在的压缩子空间强行处理。也可直接使用 R74 不要求 joint 单射的 compact 域版本，再在原 isometry 子集读取 (13)。

固定非空 C_s 输出 r-ball，r≥ρ，选实际原 λ_0。每个 query 参数距同一个 affine H 的距离至多2rρ^(−ε_*)。设置

\[
h=C_{D,B,R}\bigl(r\rho^{-\epsilon_*}
                 +\rho^{Mc_*}+\delta\bigr).
\tag{14}
\]

M 先大使 Mc_*>2，则 h≤C rρ^(−ε_*)。若 h≥一个 fixed 正数，概率≤1已经给同一上界；否则按 H/H_1 的原正交补 h 网格，数量≤Ch^(−(3−e))。每格全部 whole 原轴到一个 (e+1)-affine plane 的误差≤Ch；其中 H_1 自由参数 bounded，其 leakage 由 (13) 支付，原圆帽厚度 δ≤h。真实 convex box 体积≤Ch^(4−e)。原 N/CW 逐格求和给

\[
\bigl((C_s)_\#\mu\bigr)(B_r)
\le CK h\le CK\rho^{-\epsilon_*}r,
\qquad r\ge\rho.
\tag{15}
\]

特别不是把 box 的四个短向误差各自收费而误得 ρ^(−4ε_*)；补参数数量必须同时计。m≤3 时全 H 的 h 网数≤Ch^(−m)，各盒近 whole 直线体积≤Ch⁴，乘积≤Ch^(4−m)≤Ch；m=0 同样合法。没有先选稀 tube 子族再重置 N，也没有把 mark 比例代 wholeaxis 质量。

将 (C_s)#μ 在半径 cρ 球上 mollify，ρ 以上用 (15)，ρ 以下密度≤CKρ^(1−ε_*−n)，n=D+2。故任意固定 α<1 的全尺度 c_α≤CKρ^(−ε_*)（固定 support 归一/monomial-factorial 换坐标只改 D/B 常数）。先 tube-heavy 时 K 换固定幂；weak 相位≤Cρ^M≤Cρ，原 polynomial C1 bound 统一。

原 coarse 输入已按 A16 的独立完整证明逐步核验，并重新读取 Def17.2(2)(3)、17.4(2)。固定原 allowed ρ 窗 J，第一套 global Y_union 的原 coarse AD 和 f 的 dyadic Lip 使实际 spatial union E_J 的 ρ-cover≤K^Cρ^(−4+κ)。在同一 E_J 用固定 L_J(X_H,X_N)=(X_H,X_N−β(t_J)X_H)。每个 native label 只择它自己的一个原 time/grain；fine filled 数≥K^-1δ^-3 与每 horizontal ρ-cell 容量≤C(ρ/δ)^3，使每grain真实占≥K^-1ρ^-3个格。poly uniform C1 使其 L_J-normal 坐标在 label 的 Cρ 内。取 Cρ-separated 实际labels后，这些normal slabs的ρ格两两不交，故

\[
N_\rho\Bigl(\bigcup_{t\in J\cap Z}\widetilde Y_t\Bigr)
\le C_{D,B}K^C\rho^{-1+\kappa}.
\tag{16}
\]

这不是单time cardinal 简单相加，也不声 native union 本来带 coarse ADlower。不同labels所择time可以不同；利用的是同一 fixed L_J(E_J) 的真实空间cover。coarseclock槽相交固定个dyadic J 时加和只改常数。

每个原heavy管至少K^-Cδ^-1旧visits，而一个ρ-time槽至多Cρ/δ个原δ-separatedtimes，因此保≥K^-Cρ^-1个不同coarse times。同一 mollified strong系数support点择一个原heavy系数点继承其全部旧visits；原phase与strongphase差≤Cρ^M、roundtime误差≤Cρ、supportmollification误差≤Cρ，都由(16)的固定倍目标增厚支付。共同plates只取所有原targets，不要求不同管的visits取交。

因此 literal moment finite 定理可在 ρ 调用：lower≥K^(−C)ρ^(ε_*−1−α+L_n√ε_th)，对比 upper K^Cρ^(−2+κ)。取 α=1−κ/4、ε_*和 theorem ε_th 足小，九尺度所选 ρ=δ^b 满足 b≥a_min；K^C=δ^(−Cη)≤ρ^(−Cη/a_min)，最后 η≪a_min·min{κ,ε_th}，参与数足够且两个幂严格相反，得到统一于全部 degree≤D、coeff≤B 的 δ-dependent β 的 proper-source 排除。

原 source 的任意 dyadicLip β 仍不授 degree D；随 #Z 插值的 D 可达 δ^(−1)，定维 QE/ambient n/L_n 不再统一。本节强化只消除了固定 bounded degree 内的 singular-value 条件数，未提供一般曲线的 representation 或从 rough 源的正质量提取。restriction 的原分母、平均先 heavy 与后续 coarseclock 重计仍分别收费。

原 time restriction/label restriction 只继承 upper；归一化概率付保留质量 p 的倒数，selected Φ/Y 的 AD lower 不能凭重命名恢复。平均访问先 tube-heavy才给逐管长参与；后续 time 删选仍须实际重新 heavy。相反，第3节只用原 whole-CW 作固定凸查询，不删 source、不固定五个 times 的各 native label，也不声已经抽到次幂质量 tube carrier。

欲将本轮 proper 出口用于原全类，须从完整原数据实际付一个可调用的 coefficient/curve representation，其复杂度、条件数、fine δ 误差和原质量总损失能被统一参数预算吸收。本文没有这样的提取；不给 desired polynomial、good-jet 或 good-rank 作为附加公设。不因 R14 旧双块失败否掉当前 m1，也不因 R19 已有三个例子就虚称全 arbitrary native row 已解决。

## 10. 当前结论、独审与停止合同

本稿独立核了 uniform 正交观测商 (4)、fixed-polynomial coefficient law/原 full-clock finite 用途、两种精确弱非退化反攻，以及新锁题 bounded-degree 的空谱band/近压缩/CW统一系数 law (10)–(15)。第7–8节只反错误自动输入，不反整个 GGW 策略，更不反完整 source；full8 moment 只是校准，固定多项式不需 full8 jet。

已实际全文独核 A16 `R0096_scalar_restricted_projection_source_audit.md`：原第3–10节 fixed 链及新增第13–15节 actual coarse 标签、全部 coarseclock/support/plates和统一参数链均无强制修订。其实际点数 proof 进一步在本稿 (16) 单列，不以自证冒独审。另已 fresh actual 全文逐式审 root12 `R0096_uniform_polynomial_native_exclusion.md`，九尺度/near-kernel/原whole-CW分母、coarse标签/全部support参与、η/a_min与GGW指数均无必修项。A/root已分别实际全文核本B主链；正式review仍须等终macro/next/source实际全文读取，不预认证未来对象。

完整四路未获 general saving。统一 bounded-degree 即使连同原 coarse 输入闭合，也只排明示 proper 完整source subclass；一般 rough β 的复杂度/原质量提取仍未付，不能宣整个 mixed42 已排。按 spec 停止 degree/κ/window/导数阈值续轮，无新数学 ID、ordinary 维数改善或重大性声明，Goal active。

本 B10 的自证不计作独立审查；root/A 实际全文互审范围如上。正式 review 已获指定路径授权，须待最终宏观与后继/source 文件实际全文读取后单独完成。具名高级输入、项目直接推导、内部独审与外部同行评审分别记录，不预认证元数据、Git、验证或同步。
