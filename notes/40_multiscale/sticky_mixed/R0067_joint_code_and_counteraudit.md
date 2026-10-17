# R0067：共同原 trunk、联合码恢复及两端 normal 匹配独审

2026-10-18。B 的独立施工；只处理原 Def17.2–17.4 的 d=5,k=4,ell=3。已实际读本轮 spec、opening macro、R66 next，以及原 §19.1 的 (146)–(153)、§22.1 的 (174)–(183) 和原 tuple 审计。下文不是完整 AFF₃、ordinary 五维增益或新的方向登记；未经外部同行评审。

## 1. 原变量、先付输入与本轮修订范围

写空间坐标为 `(x,z,y)∈R²×R×R`，时间另记 t。ell slope 为 `f_t=(a_t;b_t)`，native slope 为 `F_t=(c_t,d_t)`，且 `b_t=c_t+d_t a_t`。原 ell label 为 `(z−a_t x,y−b_t x)`，native label 为

    η_t=y−c_t x−d_t z。

原 ξ=(ξ₁,ξ₂)，native velocity intercept 为 `ζ_t=ξ₂−d_t ξ₁`。这里 ξ 只在原允许尺度的物理 cube 内有代表；不假它是 η、水平位置或时间的全局 Euclidean Lipschitz 函数。

固定已合法取得的 good ρ-cube q。记 `m=#Z(q), e=#E(q), D=δ^(−κ), L=ρ/δ, N=L³, K=δ^(−O(η))`。所有 K 允许扩大固定次幂，且需 η 相对固定 µ,κ,γ 足够小。原估计为

    e≈_K m L^(4−κ),    #T(q)≤K ρ^(−κ)L⁴≈_K eD/m。

点的原管数至多 KD，每原管在每个原 time 至多 O(1) 个 δ-point labels。native grain 的 q 内容量至多 CN，所有 time 合计 grain 数至多 `K m L^(1−κ)`。后两者仅用 native scalar Y 的 AD upper 和 δ-packing。

先用原 §19.5 取得 f,F 在所用原 time window 内的 `O(Kρ)` 振荡，再重新选 q、执行下面的 core，不能把旧 core 原样当作 time 裁切后的 core。本轮联合恢复最终使用天然尺度

    σ≈_K ρ²,    τ≈_K σ,    e_L≈_K(ρσ+δ)≈_K(τρ+δ)，                 (1)

取常数使 `δ≤e_L≤τ≤ρ`。因 ρ≥δ^(1/4)，在天然尺度 `ρ³≥δ^(3/4)≫δ`，所以 e_L 的 δ-floor 不另损固定幂。对 spec 最初允许的任意 τ∈[δ,ρ]，不能无条件在 τρ<δ 时用 native AD covering；第 7 节明确这一点。

## 2. 三类有限 peeling 的真实原质量

在原 point–tube incidence 上反复删除：当前 tube degree 小于 θD 的点、当前 point visits 小于 θm 的管，以及当前点数小于 θN 的 native grain。grain 删除时删其剩余点及关联 incidences。θ=K^(−C₀)，C₀ 预先固定足够大。

每个原 vertex 至多被计费一次。三类损失分别至多

    θDe，    θm #T(q)≤Kθ eD，
    θN · K m L^(1−κ) · KD≤K^C θ eD。

故可保原总 incidence 的固定比例。终 core 有 `e_core≥K^(−C)e`，每点 ≥K^(−C)D 管，每管 ≥K^(−C)m visits，每 native grain ≥K^(−C)N 点；所有 upper 仍用原未条件化分母。

若原格点/近 grain 的记号允许多 label，把原 label copies 留在 incidence 集中；由 bounded slope 与 δ-packing，其局部重数最多 K^C。计费和最后恢复均付该固定幂。不能为了唯一归属先随意分配点而同时保每个原 grain 的 lower。

这不是重新证明 core 满足全部 Def17。特别不赋给 core 新 AD lower、完整 Φ lower 或新的 CW normalization。后面使用的 lower 都来自此次有限 peeling，使用的 upper 都来自原对象。

## 3. 同一 trunk 的 tensor Gram 计数

固定 core 起点 p@t 和 middle time s。初 arm α=(T,p_s) 必须是同一原 T 从 p 到其原 p_s 的实际访问，令其数为 n_(p,s)。core 的 tube lower 给

    Σ_(p,s)n_(p,s)≥K^(−C)eDm，
    Σ_(p,s)n_(p,s)²≥K^(−C)eD²m。                              (2)

第二式只对至多 `e_core m` 个 (p,s) 作 Cauchy–Schwarz。

给每 α 两个非负整数向量。X_α 的坐标是 `(u,W末管的ρ-direction bin)`，值为真实 p_s→T^W→w@u 的条数；Y_α 的坐标是 `(v,native jump水平τ-bin,L末管τ-direction bin)`，值为 p_s↔p̃_s→T^L→l@v 的条数。二者的原 lower 为

    ||X_α||₁≥K^(−C)Dm，    ||Y_α||₁≥K^(−C)NDm。

共同 X signature carrier 大小至多 `K m ρ^(−κ)`。对 Y，原 (176) 与 `ρ||E(t,s)||≤cτ` 保证同一 (p,s) 的所有 p_s native labels 彼此 O(τ)-close。固定 jump 水平 τ-bin 后，所有 p̃_s 在共同 O(τ) 物理 cube 中；原 coarse-angle coherence 因此给至多 Kτ^(−κ) 个末管 direction bins。故共同 Y carrier 大小至多

    K m (ρ/τ)³ τ^(−κ)。

只在原 allowed grid 有 coherence 时，取上邻 allowed cube，尺度比至多 K，付 K^C，不假所有实尺度的免费输入。细 bin 常数取足够小，所造 pair 满足所需的 ρ/τ closeness。

真实 hybrid pair 数恰是

    Σ_(α,β)<X_α,X_β><Y_α,Y_β>
      = ||Σ_α X_α⊗Y_α||₂²。

在两个共同 signature carrier 的乘积上作一次 CS，继而用 (2)，得到

    #H≥K^(−C)e D⁶ m³ ρ^κ τ^κ L³(τ/δ)³。                    (3)

这次 CS 的两个 tensor factors 各自来自同一个 α，故真正保同 p,t,s,T₁,T₂ 和原 exact ψ=φ₂−φ₁。不是把分别选好的 W/L dense graphs 取交，也未使用任意两原 grains 必有大交。

## 4. Hybrid 自己的初角边际与实际 used H

不能借旧 W 或 L 的边际直接给 hybrid。固定原初 incidence (p,T₁)，逐项上数：middle s 至多 m，T₂ 至多 KD；W第一末管 KD、time u 至多 m、第二末管在其ρ包内至多 KL^κ；第一 native jump 至多 KN、L第一末管 KD、time v 至多 m、第二 jump 至多 K(τ/δ)³、第二 L 末管在其τ包内至多 K(τ/δ)^κ。因此

    #H_(p,T₁)≤K D³m³ L^κ N(τ/δ)^(3+κ)
                =K D⁵m³ρ^κτ^κ N(τ/δ)³。                  (4)

这与 (3)/(eD) 只差 K^C。两臂对称，故 normalized hybrid 的两初角边际各被原 point–tube incidence mixture 的 K^C 倍支配。原逐点 Φ 的 slab upper、ρ-bin AD upper 于是给

    μ_H(slab width w)≤K^Cw^γ  (w≥Cρ)，
    μ_H(ρ-bin)≤K^Cρ^κ，    #used bins≤Kρ^(−κ)。

删除 μ_H 质量小于 K^(−B)ρ^κ 的 light bins，B 足够大，仅损小比例 hybrid mass；两边都处理后，以保留 used bins 的并作为同一个 H，uniform H 有 `#H≈_Kρ^(−κ)` 及原 slabγ upper。这里不声称包含无用 bins 的 Φ_q 自身有同样 normalized slab bound。

以下把 (3) 理解为已完成这种原质量删除后的同阶 lower。之后固定 terminal buckets 也不能重新免费赋新的角 lower；保留这个原 H 作 reference，图的平均密度承担后续删选。

## 5. 两个实际输出恒等式与联合图用途

令 h=s−t、ψ=φ₂−φ₁。原 W 计算给

    (x_w₂−x_w₁, ξ_w₂−ξ_w₁)
      =(hψ,(f_t−f_s)ψ)+O_K(ρ²+δ)。                         (5)

native L 的实际 scalar 输出为

    η_l₂−η_l₁=hE(t,s)ψ+O_K(τρ+δ)，
    E(t,s)=b_t−b_s−d_s(a_t−a_s)。                          (6)

取同一对 coarse 初角的中心差代替 raw ψ，对 (5) 另增 O_K(ρ²)，对 (6) 另增 O(τρ)。因此是先用 raw ψ 计数、最后才对图统一粗化；没有给每个 coarse code 伪造一对固定 exact fine angles。

若写 W 的后两行增量为 V_a=(a_t−a_s)ψ、V_b=(b_t−b_s)ψ，则 scalar 增量是

    S_L=h(V_b−d_sV_a)。                                    (7)

它不是一个独立随机第三输出。实际新增资料是 native scalar carrier 的亏损与同 trunk 的联合 output restriction；(7) 本身不供独立化、三维 Frostman 或 AFF₃。

## 6. Generic 联合码：原 fixed-power 责任确实存在

先不使用两端匹配。把 w₁@u 的 ell label 放 σ-bucket Q；每 u 至多 `K(ρ/σ)^(2−κ)` 个 Q。固定 Q 后，以 mesh σ 记录 A_W=(x_w₁,ξ_w₁)，至多 `K(ρ/σ)²` 个 cell；因为固定 x-cell 与 Q 决定一个 O(σ) 物理 cube，原 ξ coherence 只需 K 个代表。每 A_W-cell 内 w₁ 点数至多

    R_W≤K(σ/δ)^(4−κ)。

若还独立记 l₁@v 的 fine native label η，完整 frame 上数为

    F_fine≤K m⁴(ρ/σ)^(4−κ)L^(1−κ)ρ^(−2κ)。

给定 code，可依次反向选 w₁,T₁^W,p₁,T₁,p,T₂,p₂,T₂^W,w₂，再正向选第一 jump、T₁^L,l₁、第二 jump、T₂^L,l₂。忽略 η_l₁ 约束的安全 fibre upper 为

    M_old≤K(σ/δ)^(4−κ)D²L^(3κ+3)(τ/δ)^(3+κ)。

代入 (3) 给 `#H/(F_fine M_old)≥_K(δ/ρ)^(1−κ)` 这个较弱证书。把 η 粗到 `e=max{δ,τρ}`，frame 中的 native factor 可换成 `(ρ/e)^(1−κ)`，证书才变为 `max{δ/ρ,τ}^(1−κ)`。两者在 κ<1 时通常有固定幂损失，不能记作 K。

以上只是此 generic recovery 的保证较弱，不是实际 graph density 的 upper，也不证明更精确 recovery 不可能。下一节利用两个 terminal labels 的相关性修复天然尺度。

## 7. 天然尺度两端匹配：不需要单边输出扩散

先固定 u,v,Q 和 A_W-cell。由所有点在 q、F 在该 time window 的 O(Kρ) 振荡及原 q-level ξ representative，任意一臂的两个 terminal labels 满足

    η_v−η_u=(v−u)ζ_q+[F_u−F_v]U_q+O_K(ρ²)。               (8)

其中 U=(x,z) 是 native 水平三坐标，q 的 U_q 与 ζ_q 固定。Q 把 η_u=q₂−d_uq₁ 限在 O(σ) 区间。因 τ≈_Kσ≈_Kρ²，(8) 说明 η_v 只落 K^C 个 native τ-patches，不能仍独立收取全体 `(ρ/τ)^(1−κ)` 桶。patch 用固定格及邻接扩大即可；不需从标量分布推出填满。

再先选择 T₁^W 和 T₁^L 的两个 ρ-angle 包，之后才选 w₁ 细点。令 `v_h^W=(φ_W,ξ₁,w+a_uφ_W)`，即该管的前三个方向分量。精确反向恒等式是

    η_s=η_u+(s−u)ζ_w+[F_u−F_s](U_w+(s−u)v_h^W)+O(δ)。     (9)

固定 Q/A_W 后 U_w,ξ_w 各有 O_K(σ) 不确定性；ρ-angle proxy 的不确定性 O_K(ρ) 被 `F_u−F_s=O_K(ρ)` 与 time gap O(ρ) 相乘，故

    η_s=η_u+C_W+O_K(ρσ+δ)。

同时 p₁ 本身落在 K^C 个 σ-physical cubes 中。固定第一 jump 的 fine native 水平坐标 Ũ₁ 后，η_s 的总变化 O_K(σ)，所以 p̃₁ 也在 K^C 个原允许 σ 级 cubes 内。逐 cube 选择实际 ξ representative，误差 O_K(σ)。这是有限分包，不是假 ξ 对 η_u 的连续依赖。

在一个这样的分包及固定 L ρ-angle 包内，用同样正向恒等式

    η_v=η_s+(v−s)ζ_p̃₁+[F_s−F_v](Ũ₁+(v−s)v_h^L)+O(δ)
        =η_s+C_L+O_K(ρσ+δ)。                              (10)

因此一个 e_L-output bin 要求 η_u 位于 K^C 个 O_K(e_L) 区间，前提正是 `e_L≥C_K(ρσ+δ)`。native Y_u 的原 AD upper 给改进 fibre

    R_new≤K(σ/δ)³(e_L/δ)^(1−κ)。                          (11)

第一因子是三个水平坐标的 δ-packing；第二因子才是 scalar Y 的 AD。这里没有假 native label 总和 ξ 独立。

两 ρ-angle 包先选的费用是 `Kρ^(−2κ)`，包内每点各至多 `KL^κ` 个细管，因此合计 `ρ^(−2κ)L^(2κ)=D²`，和旧恢复的两个 D 完全相同。初 T₁,T₂、W第二末管另各 L^κ，第一 jump L³、第二 jump `(τ/δ)³`、L第二末管 `(τ/δ)^κ`。故总码纤维为

    M_new≤K(σ/δ)³(e_L/δ)^(1−κ)
             ·ρ^(−2κ)L^(5κ+3)(τ/δ)^(3+κ)。                (12)

δ 与 allowed-grid rounding 均在 e_L 的定义和 K 中；天然尺度可同时满足 e_L≤τ。不能把这个证明直接移到任意 τ≪σ：误差 ρσ 不再小于 τρ。

## 8. 原分母下的实际 product-reference graph

新 full frame 的上数为

    F_new≤K m⁴(ρ/σ)^(4−κ)(τ/e_L)^(1−κ)ρ^(−2κ)。

u,v 的 m²、Q 的 `(ρ/σ)^(2−κ)` 都在这里，未藏入 K；另外 m² 是原 t,s，ρ^(−2κ) 是已用 H²。直接代入 (3),(12) 得

    #H/(F_new M_new)≥K^(−C)(σ/τ)^(1−κ)≥K^(−C)             (13)

于天然 τ≈_Kσ。故某原 u,v,Q 及其 K^C 个 compatible native patches 之一承载足够多 codes。固定这些桶后，令 A 是其中 W cells，B 是 native e_L-bins，保原 times Z(q)² 与原 used H² 作 product reference；tuple-count 除以统一 (12) 就是一个 `0≤g≤1`、平均 ≥K^(−C) 的真实图。

这不要求每个 product pair 都实际出现。A,B 的实际大小至多上述 upper，而 (13) 也反过来保证实际 product 不是过小。将 terminal 二点的相邻桶固定扩大，A_+,B_+ 同样有这些 upper，故 output/input cardinal ratio 至多 K^C。按 (5),(6) 图支持在实际输出的 O_K(σ),O_K(e_L) 邻域。

除以 W 空间/ξ 的 ρ 尺度、native 的 τ 尺度，两个 mesh 都约为 Kρ，联合 carrier 的上界约为 `Kρ^(−3+κ)`。图的 t,s 和 ψ 仍原共同参数，但 g 可相关；未产生独立 time-angle law、conditional AD lower 或全 raw-pair 结论。

## 9. 单边 normal-cap 反攻与不能过称的校准

令 f=F=ξ=0，三个 native 水平坐标取完整 δ-grid，native η 取维 1−κ 的规则 Cantor，Φ 取 κ 维 product Cantor。可取 κ=2/3、base8 两端 digits，native Cantor 维 1/3，Φ 为两个 1/3 维 Cantor 的乘积，slabγ 可取 1/3。管的前三个 intercept 自由、normal intercept 在 native Cantor，斜率为 `(φ₁,φ₂,0,0)`。在固定 bounded 内框与 interior visits 上，原参数乘积是 joint4-AD；水平两/三 grains、angle upper、coherence、core度数和 straight wholeclock 都可实现，格点 rounding 仅常数费。

native η 在水平 jump 和后续管上守恒。因此对固定 p₁ 的第一 native continuation，输出某一个 scalar bin 可容纳全部 ND 选择；不可能仅由 filled grain/core 赋其一个比例 `(e/ρ)^(1−κ)` 的单边 diffuse cap。

但该族 CW 在固定 normal label 的 δ-plate 上损 δ^(−κ)：family mass δ^(1−κ)，plate volume≈δ。因此它不是完整正 κ source counter。更重要，它也不反第 7 节 joint matching：这里 η_l₁=η_w₁，联合 output 条件正好切掉 w₁ 的细 normal 自由。故此校准只否单边 cap 的不当证明，不否两端恢复、AFF₃ 或 Kakeya。

## 10. 与旧 box 的区别、AFF 尝试与剩余责任

本轮 (3) 和 (13) 比并列 W/L 的旧 box 强之处是同一原两管 trunk 和同一 exact ψ 已经通过实际 tensor Gram 与码恢复保留，两个 terminal time/桶的原分母亦已计费。它没有依靠 independently selected dense graphs 交有质量。

然而 (7) 说明新 scalar displacement 是 W 两行增量的 time-dependent combination。把它叫“第三独立输出”、用 standalone displacement 的 Jacobian/Frostman，或以 joint carrier 的 `3−κ` cover deficit 自动推出 whole-f affine，都仍不合法。必须有保此 g 的联合非扩张逆定理或另一实际输出增长证明；本稿未提供它。

因而当前严格 verdict 为：原 core、shared-trunk hybrid lower、hybrid used-angle 边际以及天然尺度两端联合码的 bounded product graph 可在上述原输入下施工；generic 任意 τ 的 fixed-loss 诊断不再冒作天然尺度障碍；完整 AFF₃、raw 全 ordered-pair 准备和 ordinary 高维增益仍未证明。不能用本图重开 R18 increment cap、R28 action/box 或把准备登记为新 major。
