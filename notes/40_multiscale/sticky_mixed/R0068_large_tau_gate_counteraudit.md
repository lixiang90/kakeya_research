# R0068：无 AFF/NQ 的大残差门槛独立反攻与证明

2026-10-18，B。已实际读本轮 spec5/opening macro3、R67 next6、R26 两个原 gate/large 稿、R21 finite polynomial-KT、R25 同代表抽样，以及 WZ2609.22035v1 原 V/L 恒等式和 Theorem13.5 的精确陈述。本稿只编辑本 assigned 路径，不 Git/spawn。目标是完整 d5/k4/ell3 的原时间 large-T upper，不证明 whole-matrix AFF₃、contact 联合图、完整 mixed 或 ordinary 新界；未经外部同行评审。

## 1. 原命题、全部前提与直接删去旧前提的责任

保完整 Def17.2–17.4：T joint4-AD/CW、两水平 grains、原 ξ/Φκ/slabγ、ell Y 的 2−κ AD、native scalar Y 的 1−κ AD/tube-KT(1−γ) 及原 straightline 访问。写 `f=(a;b), F_native=(c,d), b=c+da`，原 rows/scalar bounded，0<κ≤1、0<γ≤1。先具名19.5作整 time 准备并付 R22 闭包；其后所有删选只删整时间层，重新 good-q/core。

固定任意原 allowed `δ^(1/4)≤ρ≤δ^µ`、0<ζ<1/10、任意目标 a_*>0。在固定半开 dyadic ρ-partition 上定义

    E(t,s)=b_t−b_s−d_s(a_t−a_s)，
    T(S)=max{δ, ρ max_J max_(t,s∈S∩J)||E(t,s)||}。             (1)

欲得某真实 S，`#S≥δ^(a_*)#Z_original`、`T(S)≤ρ^(3−ζ)`。这是每个指定 ρ 各有自己的 S，不声称同一 S 同时适用于所有尺度。

R26 的 nonquad 只用于迫 rich affine fit 的 slope 小，以及以 AFF/NQ 取得链的 tiny lower。下面分别用原 V/native KT 和“反设所有 minima 大”的逻辑替换。L 图的 coupled 误差则直接以 Lip 上界支付，不以 a 的 affine 展开代替。因而不是把旧条件文字删除后再调用原结论。

## 2. 有限最小值链：无需 NQ 提供低端

在 19.5 准备后的同一原 Z 上取 `0<η₀≪⋯≪η_M≪a_*`，令 T_j 是所有 `#S≥δ^(η_j)#Z` 的 S 上 (1) 的真实 minimum，S_j 为 minimizer。finite time labels 保证取得；候选族只查同一固定 J 中的 pairs。

若某 T_j≤ρ^(3−ζ)，已得目标。否则全部大于该值。原 f 的本窗 Lip 与 d bounded 给 `T₀≤K_srcρ²`。取 M>100/A；若每相邻比小于 ρ^(A/8)，则

    T_M<K_srcρ^(2+MA/8)<ρ^(3−ζ)，

矛盾。因此存在稳定 j：

    T_(j+1)≥ρ^(A/8)T_j，    T_j>ρ^(3−ζ)。                    (2)

这里没有沿用 R26 的 AFF/NQ tiny lower，δ-floor 也不能伪造反设中的 large lower。因为 δ≤ρ⁴ 而 A,ζ 小，后面的降低候选仍能支付 δ。

## 3. Global fast-fit 见证并，不能以单窗伪造 source

对每个保留窗 J 选旧 actual anchor c_J∈S_j∩J，令 `d₀=d(c_J), h_J=b−d₀a`。设 normalized clock u=(z−c_J)/ρ，

    H_J(u)=(ρ/T_j)[h_J(z)−h_J(c_J)]
           =(ρ/T_j)E(z,c_J)，  |H_J|≤1。                    (3)

先删 relative-light 与 absolute-light windows，费用相对原 #Z；阈值可取 `#S_jJ<δ^(2η_j)#Z_J` 及 `#S_jJ<cδ^(Bη_j)ρ/δ`。总损为 o(δ^(η_j)#Z)，并保证剩余窗绝对 clock density。任何 rich fit 的 mass 都以其真实 S_jJ 计，不以某个后来 q 的 normalized prior 代替。

令 β_j=ρ^(b_j)、b_j=η_(j+1)/100。bad J 有某 row affine `Ru+C` 在 precision ρ^A 命中至少 β_j|S_jJ| 个 times，取一真实 witness W_J。若 |R|≥ρ^(A/2) 称 fast。所有 fast witness 并若有至少 `δ^(η_(j+1))#Z` 原 mass，就可合法整层 restriction 到该并，再去其绝对 light windows、重新 good-q/core。

这一步 K_fast 允许依 η_(j+1)，而不是假孤立一个小窗本身是新的 global Def17 配置。fit 的旧 anchor 不必留在见证并中，其值仍来自原同窗并受原 Lip 控制。若 global fast 反证成功，就只推出见证并质量小于该阈值，再以 β_j lower 给 fastbad 整窗总质量上界；没有赋任意单窗新的 source。

## 4. V 的完整 endpoint 码与同图初角先验

在上述 global fast 并上重构 local good-q/core。记 m=#Z_q、e=#E_q、D=δ^(−κ)、L=ρ/δ；已有供应给 `e≈_K mL^(4−κ)`、`m≥K_fast^(−C)ρ/δ`、point 管数 ≥D/K、每管实际 visits ≥m/K。有限 point/tube peeling 的每个 vertex 只计费一次；原 T、CW 与 full Y 不重归一。

两原 arms 从 p@t 到 p₁,p₂@s 给

    #V≥K_fast^(−C)eD²m。                                    (4)

固定初 incidence (p,T₁) 的原 V 数至多 K_fast Dm；除 (4) 后的边际由原 incidence mixture 的 K_fast 幂支配。重新按这个 V law 的 used ρ-bins heavy 剪选，得到同一个 H，`#H≈_Kρ^(−κ)`，Uniform(H) 有宽≥Cρ的 slabγ upper。不能借 unused Φ_q 的 normalized slab，更不能借 R67 hybrid 的边际不经复算。

给 V 的 code 只记 `(p₁完整原label,t,h₁,h₂)`。p₁ 已决定 s。给定 code，T₁ 在其 ρ-angle bin 内至多 KL^κ 个并决定 p@t，T₂ 同样至多 KL^κ 并决定 p₂@s。因此 fibre≤K_fast^C L^(2κ)。reference 大小至多 `e·m·ρ^(−2κ)`，且 `D²/L^(2κ)=ρ^(−2κ)`，故真实码给

    0≤g_V≤1， E_(Uniform(P_core)×Uniform(Z_q)×Uniform(H)²)g_V
                    ≥K_fast^(−C)。                          (5)

完整 endpoint 而不是标量 η_s 避免了额外 normal-fibre 公设。对 fast 斜率 r，slab 上界删 `|r·ψ|<K_fast^(−C)|r|` 的坏 proxy pairs，可令其 reference 概率小于 (5) 一半；再固定真正 good pair 和 p₁，保至少 K_fast^(−C) 比例的原 fine t。ψ 在本码内是 proxy，fine pairs 仍可各不相同，误差下一节计入。

## 5. Fast affine fit 产生真实 native 二次轨迹

physical row slope 为 `r=(T_j/ρ²)R`，fit error 为 `(T_j/ρ)ρ^A`。同一窗原 Lip 给

    (s−t)E(t,s)=−(t−s)²r+O_K(T_jρ^A+ρ³)。                  (6)

native V 恒等式把左侧乘原 fine ψ 送入 `η_s(p₂)−η_s(p₁)`，误差 O(δ)。在本应用 W_J⊂S_jJ，(1) 还给 `||E||≤T_j/ρ`；故**先在原 V 式**把 fine ψ 换固定 ρ-proxy，成本≤T_jρ。A<1 时它被 T_jρ^A 吸收，再代 (6)。若只陈述不含这个 residual upper 的 standalone fast-fit lemma，则可保较粗的 `Kρ³|r|` proxy 项；不能在未列 upper 的引理里无条件改成 T_jρ。

固定 (5) 中选出的 p₁@ s 与 good ψ，得到至少 K_fast^(−C) 原 fine t 满足

    P(t)=η_s(p₁)−(t−s)²(r·ψ)∈N_Δ Y_native,s，
    Δ=C K_fast^C(T_jρ^A+ρ³+δ)。                             (7)

所有 witnesses 都是真原 p₂；使用完整 native Y_s 的 KT upper，不给裁切 Y 加 lower，亦不误用 ell Y 的 line-KT。

记 `B=ρ²|r·ψ|`。fast 与 good-angle 给 `B≥K_fast^(−C)T_jρ^(A/2)`。fit-rich 原 times 的 span≥K_fast^(−C)ρ（由 absolute local clock），原 h 的 Lip/振荡与小 fit error 遂给 `|r|≤K_fast^C`，不需预设有界 fit coefficients。于是 `B≤K_fast^Cρ²≤1`。在 u=(t−c_J)/ρ 的整单位窗上，P 的振幅≈B，与 vertex s 的位置只差固定常数。

large lower `T_j>ρ^(3−ζ)`、δ≤ρ⁴、A<ζ/10 及全部 fast losses最后小，给

    Δ/B≤K_fast^C[ρ^(A/2)+ρ^(ζ−A/2)+ρ^(1+ζ−A/2)]
        ≤ρ^(A/3)。                                         (8)

两种等价验收方式均可：

- 对原 time cap 删除 vertex 附近 K_fast^(−C)ρ 短区间、留一侧。此处导数≥K_fast^(−C)B/ρ，每个 Δ-image interval 只能装 K_fast^C·Δ/B 原 ν mass；δ/ρ atom 项由 B≤K_fast^Cρ²、Δ≥δ 吸收。故 image Δ-cover≥K_fast^(−C)B/Δ，而 native KT 给 ≤K_fast^C(B/Δ)^(1−γ)，与 (8) 矛盾。
- 或直接用 R21 scalar finite PCT，domain fine base δ/ρ、保留 time 密度 K_fast^(−C)、degree2。其必要条件 `Δ≥(δ/ρ)B` 由上述 B upper 与 Δ≥δ 支付；固定常数在 2/γ 次幂内部，γ 先固定。

因此 global fast witness 并不可能达到 δ^(η_(j+1))#Z。该证明保原 grid、原近管访问、点态 ξ/Φ 和任意相关 g，不需要 whole a affine、NQ、全 time-angle 独立或微分正则性。

## 6. Slow witness 并与原稳定量

对 |R|<ρ^(A/2) 的 witness W_J，(3) 的 fit 给同窗 t,s∈W_J 上

    ρ||E(t,s)||≤C T_jρ^(A/2)+K_src^Cρ³
                    ≤T_jρ^(A/3)。                          (9)

δ/T_j≤ρ^(1+ζ) 也小于 ρ^(A/3)，故 δ-floor不破坏降低。若所有 slow witness 的并达 δ^(η_(j+1))#Z，它就是下一个原 minimum 的合法候选；(9) 与 (2) 矛盾。不同窗的 fit 常数与 anchor 不必一致，因为 T 不查跨窗 pairs。

fast/slow 两种 witness 并各小于该阈值，而每 bad J 的见证≥β_j|S_jJ|，所以 bad 全窗总质量至多

    2δ^(η_(j+1))β_j^(−1)#Z。                               (10)

取 η_j≪η_(j+1)，结合 light-window 预算可保 S_j 常比例原时间。每余窗对所有 row affine precision ρ^A 的 fit mass 均 <β_j，以 S_jJ 原分母计。随后只删整窗，不把旧 g 的 surviving mass 当已有；在余合法 whole-time 配置重新 good-q、重构 L 图。

## 7. 无 AFF 的 L 图与诚实 working mesh

在新的 good-q，固定 same-global `τ≈_K T_j`，只用 `ρ sup||E||≤T_j` 构造原 native L。局部 actual sup 不必达到 T_j。原细时间 ν=Uniform(Z_q) 仍有 base δ/ρ，used 角的同图 incidence/heavy 证明重新执行。

不作 a 的 affine 展开，而用精确式

    E(t,s)=h_J(t)−h_J(s)−(d_s−d₀)(a_t−a_s)，
    |(d_s−d₀)(a_t−a_s)|≤K_src^Cρ²。                         (11)

native scalar空间先除 exact T_j、clock除ρ后，L 自身误差为 `O_K((τ/T_j)ρ+δ/T_j)=O_K(ρ+δ/T_j)`，丢弃 (11) 的误差为 O_K(ρ³/T_j)。native patch 的长度 τ/T_j 至多 K。若改除 τ，主项会多系数 T_j/τ，不能无声删掉；本稿采用前一单位。故同 g 支持

    x+(s−t)[H_J(t)−H_J(s)]·ψ∈N_(Cw)A_plus，
    w≈K_graph^C(ρ+ρ³/T_j)，   ρ²≤w≤ρ^(ζ/2)。                (12)

必要时空间、H_J 与该表达式同时除一个 L₀≤K_graph^C 至 unit norm，mesh同步除；不把 F 的 norm 费抹掉。空间 fine base 为 δ/(T_jL₀)，且 δ/T_j≤ρ^(1+ζ)、δ/ρ≤ρ³，均小于诚实 mesh。K_graph 只含 η_j 与原 source loss，**不含限制到 fast witness 并时的 η_(j+1) 或 β_j**。

全 native Y 的 AD packing及原 L fine 质量给粗空间 `#A_minus≈_K w^(−1+κ)`、`#A_plus/#A_minus≤K_graph^C`，mean g≥K_graph^(−C)。其 lower 由原 fine mass/cell capacity及 light-cell 删除所得，而非给任意裁切 patch 重授 AD lower。此处复用 R26 的计数操作，输入只有 (11)(12)、原 AD/coherence 与 time cap，没有调用其 AFF/NQ 原结论。

## 8. 原 slab prior、adaptive fits 与同一次 time 抽样

good-q time 是 S_jJ 的 K_graph 次幂份额，因此 row nonfit 在 precision `h=K_graph^(−C)ρ^A`、原 ν 下为 `a≤K_graphβ_j`，不仍写 β_j。归一化三个 distinct times 的 annihilator，使最大系数为1，其他比值≤1；小 residual 的 Fubini 质量≤3a，大 residual 按原 π 的 slab 上界收费。因此 scalar affine σ-fit 的 mass≥b 时，坏角概率≤

    C b^(−3)[a+K_graph^C max(Cρ,3σ/h)^γ]。                  (13)

distinct-time atom 费用要求 b≥C K_tδ/ρ，以下自动满足。取 `σ=ρ^(2A), b=ρ^v, v≪min(b_j,γA)`；合法查询取 ≥max(Cρ,3σ/h) 的较宽 slab。K_graph 最后小，使坏角概率小于原 graph mean/4。以 g≤1 删坏角后，可固定同一 good proxy pair，保 g 的 conditional mean，同时对所有 scalar affine p 有 `ν{|H_J·ψ−p|≤σ}<ρ^v`。不是说每个 projection 都 nonfit，也不是固定某对 exact fine 原角仍 dense。

空间粗化后以 w-time cells 抽独立代表，并保同一原 F 值。先删 light time cells，prepared mixture 相对原 ν 的 density在 `[c/K_t,CK_t/m_g]` 内，故 graph mean 至少 c m_g/K_t²。sampled diagonal最多1/N；一个 bounded graph mean 事件已有多项式正概率，不需假 g 独立。

若 coarse clock 上有 q=w^(v/10) 比例的 w^e affine fit，interval cap 给两点 gap≥cq/K_t，bounded F 给系数 ≤CK_t/q。原 time 与 cell center 差 O(w)，故原标签在误差 `w^e+CK_tw/q≤2w^e` 内命中同一 fit。统一 bounded 系数 net 配合 independent-cell Hoeffding，坏概率≤poly(w^(−1))exp(−cNq²)，远小于保 graph 的概率，遂有一次选择兼保 graph 与全部 adaptive affine nonfit。没有原子数或权跨度费用，也没给 F 免费 Euclidean Lip。

## 9. Named13.5 与无循环顺序

取 `α=1−min(κ/2,1/2), β_time=1, C={1}`。先由 named13.5 固定允许小的 e<1/4，再取 `A=ζe/1000`、M>100/A。因 w≤ρ^(ζ/2)，同步 norm 费 L₀ 可由 η_j 最后小支付，满足 `4L₀w^e≤σ=ρ^(2A)`。刚证明的 sampled affine nonfit 就是13.5(78)，regularity threshold不依 nonfit mass指数、graph threshold可依 v，二者分开支付。

给 g 取固定小幂 threshold 后得真实 finite G，支持的 O(w) 输出用有限邻格覆盖，ratio≤K_graph^C。若符号反向取 −F，不用不合法的负 C。13.5 推 `#A_minus≥w^(−α)`，与 `#A_minus≤K_graph w^(−1+κ)` 的 κ/2 固定余量矛盾。

参数从后向前选：先固定 κ,γ,µ,ζ,a_*,e,A,M；terminal η_M 小于 a_* 与 fast-V/KT 所需 µAγ 的全部固定常数余量。每 j 在已知 η_(j+1) 后定 b_j、v_j、13.5 两阈值及 sampler 容差，再取 η_j 足够小，最后才取原 η_src 和 δ。fast branch 可含 η_(j+1)，但 nonfit graph 只含 η_j，故不是用 graphloss 定 β 再把 β 损失送回同一个 graphloss。

## 10. 原尺度、闭包、反攻与最终范围

指定原 ρ 始终保留。whole-time restriction 后未必属于重新命名参数的 newallowed grid；这里 finite q/core/V/L 只查询原 ρ 及原允许尺度上的继承 upper/coherence、原 full 层的 AD packing，再以实际重留质量付 K。需要 τ 的格点取整时按原可用 coherence 取邻格，损 K；不能为此改 T 的原 partition 或把不同窗拟合常数合并。

快速 fit 藏在短 time 区间、critical vertex、ξ 随点变化、原角相关、单 endpoint normal 质量不足等反攻均由 absolute-window 修剪、完整 endpoint 码、原 slab 删除、真实 time cap 与 δ-floor 处理。用单 isolated 窗声称新的 global source、或从两个 separately rich graphs取交，仍不合法且本证不用。全 T/CW 没有对子族重归一；core的逐 active tube density 来自新付最低度，原 family 只保平均质量。

结论：在上述 source good-q／整层闭包与 named19.5、13.5 高级输入的既有范围内，反设全部 T_j large 导致矛盾，故任意指定原 allowed ρ 有某原 S 满足 (1) 目标，并在把准备损失加上 η_M 后保 ≥δ^(a_*) 原 #Z。该推导实际取消旧 whole-AFF/NQ 条件，未由 R26 原定理直接推出；但只定位 residual 的 upper，不能免费和不同 S/ρ 上的 lower 求交、不能推出 whole f affine或完整 mixed。

本稿尚待 root/A 当前终稿全文互审。无完整 source 反例、ordinary 增益、major 或新ID认证；具名高级 wholeproof 未在本轮新独证，Goal active。
