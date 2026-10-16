# R0022：付原权重和定量投影的 fixed-scale affine 准备

2026-10-17，root。主任务LOCAL-AFF，服务实际N5-MIXED32-Q01。本文使用原WZ Theorem21.2作为**命名标量ABC输入**，不独立重证其radial/BSG全部高级证明。原路径/删选/投影接口在本轮具体支付；不是对all-scale21.1作形式否定。

## 1. 固定尺度结论和参数次序

设原数据满足WZ Definitions17.2–17.4，d=5、ell=2（应用取k=3）；T joint4-AD、C_CW(T)≤δ⁻η，κ>ζ>0。固定µ∈(0,1/4]，取ε₀依ζ充分小，使9ε₀处于named Theorem21.2对ζ₀=ζ/4的真实允许区间，并额外要求0<ε₀<ζ/10000。不以后一数值代替原文未知的“充分小”函数。固定任意充分小a=θ_aff>0，再取η足够小依赖κ,ζ,µ,ε₀,a,γ，最后δ小。ρ∈[δ^{1/4},δ^µ]为指定尺度。对每个原dyadicρ-window J，定义

    M_J=max_{R,U∈R³} #{z∈Z∩J: |f(z)−Rz−U|≤ρ^{1+ε₀}}.

则

    Σ_J M_J ≥ δ^a |Z|.                       (LA)

若ρ不在原allowed格，向上取整和固定容差只改变δ^{Oη}费用；也可先将本定理陈述在allowedρ上并按相邻尺度完成固定幂容差版本。R21只需带K固定倍的affine error；不能从向上取整直接声称每个任意ρ具有**完全相同的常数1容差**。下文先证明原allowedρ上的(LA)，应用版明确容许K倍和略小ε₀。

进一步可选全局≥δ^{Ca}|Z|的原times，每个保留window中有完整whole-f affine速度R_J、pairwise error≤K_prepρ^{1+ε₀}，且K_prep⁻C≤|R_J|≤K_prep^C。这里K_prep=δ^{-C(η+a)/(gamma ζ)}可以包含真实affine密度loss；首坐标r非零另由R21推出。后一结论使用原named Lemma19.2和本轮时间闭包。

**预算区别：** 第2–7节反证只删去≤1/2原times，其中K始终是K_src=δ^{-C_aη}，常数次数可依a等固定参数，但不含a作为指数loss。a先固定、η后取小使K_src相对ρ^β任意小。仅第8节positive fits/low-speed准备才用含a的K_prep；不能把K_prep回灌第6节概率或第7节ABC，否则β≈a/100会被耗尽。

## 2. 从全局反证得到真正同尺度nonfit，而非逻辑倒置

反设Σ M_J<δ^a N，N=#Z。删掉M_J>δ^{a/2}#(Z∩J)的windows，所删times数<δ^{a/2}N。再删原time数小于δ^{Cη}ρ/δ的windows，总损失至多Cδ^{Cη}/δ，可选C>2使其小于N/4。最终保留≥N/2的整层原times，在每个保留window J中

    M_J≤δ^{a/2}#(Z∩J),
    #(Z∩J)≥δ^{Cη}ρ/δ.                       (1)

本轮R0022_time_restriction_closure.md证明这仍为原配置，参数只变为Cη；所有跨时间Y-union/coherence/tildeY tube-KT都核过。删窗不删除保留层的点、Φ或T。可以在一个保留window内用原cross-time covering和incidence平均选合法good-q；m=#Z(q)≥K⁻¹ρ/δ且m≥K⁻¹#(Z∩J)，因此(1)给任意whole-f fit在这些原times中的比例≤Kδ^{a/2}。没有声称任意q都有lower。

## 3. 原W、observed A与同一个bounded graph

令D=4−κ。原good-q点数e≈K^{±1}m(ρ/δ)^D、degree≈K^{±1}δ⁻κ，且#T(q)≤Kρ⁻κ(ρ/δ)^4。每条原tube的marked degree d_T可不均匀。Σd_T²≥(Σd_T)²/#T(q)，再按原中点作CS，给原两边path数≥K⁻¹eδ⁻²κm²。按共同原起点、两原times和terminal direction的ρ-bin再作CS，给

    #W≥K⁻¹eδ⁻⁴κρ^κm².                      (2)

W的每条边都属于两端Tp的交，因此恢复时可使用原pointwise Φ计数；不是将所有穿过某点的任意环境管都当κ-dimensional。

按末层和末grain厚度σ=ρ²分桶，选一个原W足够重的桶。原观察集A_phys={(x,ξ_p): z固定，|y_p−y₀|≤Kσ}。给定x的σ-cell，原p只遇K个σ-cubes；ξ-coherence给每个x-cell至多K个jointσ-cells，故N_σ A_phys≤Kρ⁻¹。

code=(a_σ,z₁,z₂,φ₁,ρ,φ₂,ρ)的原W fibre至多

    K(σ/δ)^{4−κ}δ⁻⁴κρ^{3κ}.                (3)

实际恢复表见A的R0022_observed_graph_source_audit.md：第一endpoint局部点数、T₁'原Φ、两initial粗Φ和ρ-close末T₂'均逐项计入。用(2)/(3)及末层/厚桶/Φ大小平均，得同一个原reference frame上的0≤g≤1、mean≥K⁻C。输出A允许厚桶固定K倍扩张，input/output并到同A只损K，不把桶自身的小全局质量称作K⁻¹。

## 4. 从原(151)直接修复符号与缩放

原真实路径(151)的increment是

    (x₂'−x₁', ξ₂'−ξ₁')
      =(z₂−z₁, f(z₁)−f(z₂))(φ₂−φ₁)+O(Kρ²).

PDF92的(170)把后一block符号反过来；且F除以δ⁻ηρ而A的ξ仅除ρ，后续(172)漏了相应factor。PDF78/92原图已核，不是提取误差。可保守局部修复：选1≤L_f≤K控制窗口f和q内ξ的振幅，同步定义

    a=((x−x₀)/ρ, −(ξ−ξ₀)/(L_fρ)),
    b=((z−z₀)/ρ, +(f(z)−f(z₀))/(L_fρ)).

同一固定线性缩放加vertical反射后，正确关系为

    a'=a+(b₂−b₁)(φ₂−φ₁)+O(Kρ).              (4)

A,B有界；first observable坐标不变。反射和同步缩放不产生新独立law，也不改变whole-f affine nonconcentration。只需原A的coarse-x fibre cap，不需A全局Lip。该修补不反驳原主定理。

## 5. 实际粗化、必须删除的轻time cells

取工作mesh s=C K₀ρ吸收(4)误差，K₀是已固定小幂；η≪µ使s→0。按s-cells将原fine times聚合，δ/ρ-spacing经原time packing给每个B-cell的occupancy n_b≤P=K sρ/δ；dyadic Lip与allowed取整给每个time-s-cell至多K个B-cells，故N_B≤K/s。原m/P≥K⁻¹/s。

g的两个fine time fibre求和后除P²，仍≤1且coarse mean≥K⁻C。这一步只付upper capacity；还**不能**继承coarse uniform nonfit。删除n_b<P K^{-B₀}的cells，所删原fine mass≤K^{C−B₀}m；由g≤1，两个time坐标上的graph损失也小。B₀先取大于graphloss的固定常数，保graph mean≥K⁻C。剩余carrierB_h满足

    K⁻C/s≤N_B≤K/s,
    P K^{-B₀}≤n_b≤P.                        (5)

故original fine nonfit upper可除以真实lower capacity传到uniform B_h，只多付K^C。每个保留B-cell选一个真正原fine time及其F值作代表；不同cells的fine原indices不交，所以这些time可以取不同。它们相距未必≥s，但对所有长度≥s的interval，uniform time质量≤K^C|I|；这才是有限rich-triple引理所需的base d≈s，不是未经支付的s-separated graph。相邻代表离原coarse中心O(s)，关系(4)仅再付O(s)。稍后投影/rounding到工作s-grid，first time坐标与每time cell的K-cap给(s,1,K^C)-set，碰撞重数≤K。源g的相关性仍保在bounded graph中，未将原W当product law。

对F=(f−f₀)/(L_fρ)，原fine vector vertical fit容差可取h₀=ρ^{ε₀}/(100L_f)。但不能直接说coarse任意斜率band的误差只有O(s)：若其斜率R很大，time rounding另有|R|s。因此先传**Euclidean tube cap**，不免费传band。

取h=ρ^{4ε₀}。一个单位h-tube若轴的time分量≥sqrt(h)，其中graph点落在某个vector affine band，垂直误差≤C sqrt(h)≪h₀；否则其time投影长度≤C sqrt(h)，由原time packing控制。故fine tube mass≤K[δ^{a/2}+ρ^{2ε₀}+δ/ρ]。Euclidean距离在coarsening时只增O(s)而不乘未知斜率，且s≪h；(5)付heavy lower后uniform B_h继承同一cap，只多付K。

所有B_h坐标在固定bounded box。任意vertical h-band中的点都在某一向量直线的Ch邻域内，该直线与扩大bounded box的交段长度O_m(1)，可由O_m(1)根unit Euclidean Ch-tubes覆盖。因此任意该vertical band的uniform质量≤ρ^χ，χ=min(a,ε₀)，固定倍与K均由η后取小吸收。这里的h是ρ^{4ε₀}，**不是**未支付粗化的h₀。原F只需bounded，不把dyadic Lip偷换成全局Euclidean Lip。

## 6. 真正定量scalarization，所有adaptive tubes一次控制

调用本轮独立证明的bounded-range rich-triple lemma。对uniform B_h，time packing常数K_t≤K^C，base d≈s，diam F≤C。上节h=ρ^{4ε₀}，任意vector h-fit质量≤a₀=ρ^χ，χ=min(a,ε₀)。对λ∈[1,2]³，Π_λ(t,F)=(t,λ·F)，若某Euclidean w-tube有质量≥b，其三时刻有序中点残差迫一个统一triple统计量大。vector residual≤h的triple总质量≤a₀；大residual时λ小球概率受w/h控制。垂直化只用bounded range和time gap，因此

    Pr_λ[存在b-rich w-tube]
      ≤C[a₀/b³+K_t w/(h b⁴)].              (6)

注意b⁻⁴而非免费用Euclidean Lip版的b⁻³；有序中点convexweights本身没有gap逆损失，额外gap仅来自tube垂直化。

取

    β=χ/100=min(a,ε₀)/100,
    b=ρ^β,  w=ρ^{8ε₀}.

则b≫K_t(s+w)，且(6)≤C[ρ^{χ−3β}+K^Cρ^{4ε₀−4β}]<1/2，η按µ、a、ε₀后取小。存在一个有界λ，使所有该宽度tubes的mass≤ρ^β。没有对无限条r,u作无费用union bound，也没有对每个source世界另选λ。

同一个Π_λ作用于A和(4)。A每个coarse observable-x的fibre≤K，所以N_s(Π_λ A)≥K⁻C N_s(A)，pushforward聚合重数≤K。B也因first time坐标每cell≤K而有bounded聚合重数；scalar Φ在s重分箱κ-AD，原ρ-cells碰撞≤K。coarse graph与uniform frame的density、regularity及small image各只损K^C。把上述tube cap保守降为ρ^{β/2}以吸收这些K与rounding。原同一个W graph仍存在。

## 7. 原标量ABC接入，不用generic projection

在coarse graph中平均固定b₁,φ₁。剩余为A₂×(B₂−Πb₁)×(Φ_s−φ₁)上的dense subgraph。由(4)其像a+(b−Πb₁)(φ−φ₁)在A₂的Cs邻域，故N_s(image)≤K^C#A₂。input/output的support固定bounded，固定改单位不变幂预算。

原Theorem21.2使用两个不同小参数：η_reg控制B,C的Frostman upper；barη_graph控制graph density和small image。此处二者均≤C_aη/µ，分别选低于其真实阈值。取ABC ζ₀=ζ/4、ε₁=9ε₀、ε₂=β/4，ε₁的真实“充分小”条件已在第1节支付；额外数值ε₁≤ζ₀/100本身不替代它。s^{ε₁}≤w且K_src^Cρ^{β/2}≤s^{ε₂}，η后取足够小。B₂为(s,1,K_src^C)-set，C为scalar(s,κ,K_src^C)-set，#C≥K_src⁻C s⁻κ；A₂仅需s-separated、#A₂≤K_src/s。

named scalarABC给

    #A₂≥s^{ζ₀−1}#C≥K⁻C s^{-1−κ+ζ₀}.

与#A₂≤K/s矛盾，因为κ>ζ且K转换为s的小幂可任意小。整个证明只查询当前ρ-window的whole-f nonfit；原AD/coherence仍在ρ²及其他regularity尺度被使用，不能误称配置只需单尺度数据。矛盾证(LA)。

## 8. low whole velocity、stable closure及mixed32回传

选择每个window最大fit的原times，并去掉过稀windows，得全局δ^a密度及每window原time span。R0022_time_restriction_closure.md第4节以真实time子配置和named19.2排除携带δ^a比例mass的低whole-velocitywindows，给|R_J|≥K⁻C；原本尺度upper给|R_J|≤K^C。这没有预设首坐标非零。

任意后续δ^{a_j}-dense整时间删选仍为原配置，只付C(η+a_j)；所以R21有限stable graph所需的每一轮global候选并和good-q路径计数可继续合法调用。本轮支付的是这项操作闭包，不是每次声明选中T重新AD。

因此R21 MIX-003的固定尺度globally dense affine、whole-velocity和time-stable原graph准备现有明确来源。若起点就是实际globally dense vector quadratic alternative，先合法保留其整层，再应用本准备，quadratic property在后续time子集上保留；送入PCT/τ-collapse/非零scalar r/全tildef慢变/19.4正gain，条件排除κ>ζ。

仍依赖named Theorem21.2、19.2、19.4等高级source结论，其全部证明未独立重跑；本轮不把它们的引用说成全source审计。实际mixed32的**二次alternative**在这些明确输入下闭合，不处理非二次、其他mixed、一般归约或Hausdorff。没有新维数界、Kakeya反例或重大性认证。
