# R0027：observed matrix 有限反攻与联合增量二维平面门槛

2026-10-17，`lifting_obstructions`。已读本轮 macro/spec、R26 next target、STATE 与 R18 原 W 边界。唯一 main 是 actual ell3 的 whole-matrix AFF₃；本稿只检验所展示的有限 observed 接口，不把它预设为全部原配置，也不将有限模型自动升级成 source/Kakeya 反例。

**结论：没有构造出满足 fixed matrix nonfit、原 slab prior、任意小图密度损失的完整反模型。独立核得一项严格的联合增量估计：原 matrix-time 增量在所有 affine 2-planes 的薄邻域上有统一 upper，并能在同一个任意相关 g 下支付密度费用。** 此估计保留二维 visible block，严格不同于只看 Y 或抹 g 独立化；但它本身不证明 `#A>r⁻²`，不能宣布 AFF₃ 已得。

## 1. 全部有限量词及原参考先验

令 t,s∈[-1,1]，ν 为有限原 time 概率。给定 base d>0，假设对长度 ℓ≥d 的 interval I，

    ν(I)≤K_t ℓ。

令 `M(t)∈Mat(2,2)`，operator norm≤1，不要求连续、Lip、C²、不可约或任意 secant 满秩。固定 `0<h<1/100`、`0≤a≤1`，假设所有 real matrices R,U 都满足

    ν{t: ||M(t)−tR−U||≤h}≤a。                         (1)

令 Λ 为有限原角标签空间、π₀ 为其概率，ψ:Λ→R²、|ψ|≤1。允许重复 ψ，始终保原标签质量。设 π=ψ_*π₀，且对所有 affine lines L 和 `q_base≤q≤1`，

    π(N_q L)≤K_ψ q^γ， 0<γ≤1， K_ψ≥1。              (2)

可把原 φ₁,φ₂ 标签的差映射作为 ψ；不得将 distinct differences 改成 uniform。定义真正保留 visible block 的增量

    D(t,s,ψ)=((t−s)ψ, −[M(t)−M(s)]ψ)∈R⁴。           (3)

令 λ_D 为 `ν²×π` 经 D 的 pushforward。为统一处理合法查询，把

    C_π(q)=min{1, K_ψ max(q_base,q)^γ}

用于 q≥0；当 max>1 时取概率上界1。查询 raw width 小于 q_base 时只能查 q_base，不能免费沿用更小的幂。

本稿用 operator norm；源中的任意固定矩阵 norm 可用固定常数换 h 并预留精度余量。固定振幅 upper 大于1时先同步归一，或在后式保其常数，不能把原小幂振幅当绝对常数。

## 2. 主命题：任意 affine 2-plane 的统一增量 upper

取 `0<ε,λ<1/10`、`d≤g≤1/10`。对任意 affine 2-plane P⊂R⁴，下列两种 upper 之一成立：

    λ_D(N_ε P)≤a+C_π(Cε/(λh))，                    (4a)

或

    λ_D(N_ε P)≤C K_t g+C_π(C(ε+λ)/g)。             (4b)

常数 C 为固定维常数，与 P、其平移、拟合 slope、原原子数和重数无关。因此取

    ε=h⁴， λ=h²， g=h， h≥d，

便有同时对所有 affine 2-planes 的统一界

    sup_P λ_D(N_(h⁴)P)
        ≤a+C K_t h+C K_ψ max(q_base,C h)^γ。         (5)

当 q_base≤c h 且 h 后小，简化为 `a+C K_t h+C K_ψ h^γ`。这里每个 P 单独满足同一个数值上界，不是对不可数个事件作 union bound。

### 证明：垂直 block 非退化

把 P 写成 `P={z:Qz=c}`，其中 `Q=(A,B):R²×R²→R²` 的两行正交单位，故 `QQ*=I₂`。`dist(D,P)≤ε` 等价于 `|QD−c|≤ε`。先设 `σ_min(B)≥λ`。记

    R_ts=M(t)−M(s)−(t−s)B⁻¹A。

由 (3) 得 `QD=−B R_ts ψ`。所以近 P 迫

    |R_ts ψ+B⁻¹c|≤ε/λ。                            (6)

固定 s，事件 `||R_ts||≤h` 是 (1) 中的一个真实 matrix affine fit，其 slope 为 B⁻¹A、intercept 为 `M(s)−sB⁻¹A`，虽可很大仍属 (1) 的 all-real 量词。因此该事件的 ν² 质量≤a。

其余 pairs 有 `||R_ts||>h`。选择最大奇异值的左单位向量 w，使 `|wR_ts|>h`。把 (6) 左乘 w 并除以 |wR_ts|，ψ 必须位于宽 `ε/(λh)` 的某条 affine line 的邻域。其中心包含 B⁻¹c，但 (2) 已对所有 affine lines 一致，所以原 π 质量≤`C_π(Cε/(λh))`。按原 ν² 积分，即 (4a)。没有假设 R_ts 可逆或 rank2。

### 证明：垂直 block 近退化

若 `σ_min(B)<λ`，取左单位向量 w 满足 `|wB|<λ`。由 `AA*+BB*=I₂`，有

    |wA|²=1−|wB|²≥1−λ²。

近 P 给

    |(t−s)(wA)ψ−wc|≤ε+|wB| ||M(t)−M(s)|| |ψ|
                           ≤ε+2λ。                  (7)

原 time cap 直接给 `ν²{|t−s|<g}≤C K_t g`，因为 g≥d。其余 pairs 除以 `(t−s)|wA|` 后，ψ 落在宽 `C(ε+λ)/g` 的某条 affine slab 中。再次调用原 π、按原 time prior 积分，得 (4b)。任意 affine offset wc 均被保留，不需要 P 经过0。

将三个尺度代入，两个 slab raw width 都≤C h。固定上界常数和大宽度的 trivial probability1可统一进 (5)。证明完。

## 3. 保同一个任意相关 g，不能虚构其边际独立

令 µ_A 是任意 finite observed labels 的概率；A 可以是原 `R²_x×R²_ξ` coarse graph，带原重数。设

    0≤g(a,t,s,ℓ)≤1，
    m=∫g dµ_A dν² dπ₀>0。

不要求 g 是乘积，不要求其 conditional angle marginal 仍满足 (2)。按同一个 g/m 定义真实 increment law λ_g。因为平面事件只依赖 t,s,ψ，且 g≤1，严格有

    λ_g(N_(h⁴)P)≤m⁻¹ λ_D(N_(h⁴)P)
       ≤[a+C K_t h+C K_ψ max(q_base,C h)^γ]/m。       (8)

这是原参考先验上的 domination，不是把实际图独立化。如果 terminal observed difference 与 D 仅相差 E₀，則其 N_εP 质量由右边对 `N_(ε+E₀)P` 的版本控制。特别当 `E₀≤c h⁴`，用固定倍 h⁴ 邻域的同一证明即可；不免费忽略原 O(Kr) relation error。

一项明确的 fine-scale实现：令 h=r^α、a≤r^β、K_t,K_ψ≤r⁻η、m≥r^η，d,q_base≤C r，`0<α<1/4`，β>0固定。若 η 充分小依 α,β,γ，且原 error≤r^(1−Cη)≪h⁴，则 (8) 为

    sup_P λ_g(N_(c h⁴)P)
      ≤C[r^(β−η)+r^(α−2η)+r^(αγ−2η)]。             (9)

各指数严格正；常数亦由最后 r 小吸收。这里没有缩小 fixed β 或 γ 来迎合 η。若当前 source 的 base、loss 或 error 不符合这些关系，(9) 不能直接调用，须保 (4a)–(4b) 的实际尺度。

## 4. 对所指 rank/kernel 与 world 模型的严格攻击边界

**共同核捷径不能免费给 dense g。** 若图正权只用 `|R₀ψ|≤ε`，某固定矩阵 `||R₀||≥c₀>0`，则取其最大奇异方向，(2) 给 `m≤C_π(Cε/c₀)`。精度 ε=K r、固定 γ 和任意小 η 时，该固定正幂代价一般远小于所需 `r^η`。把 g 与 a,t,s 相关也不能突破此上界，因为事件依旧由原标签概率控制。单写 ψ 属于 common kernel 因而平移闭合，不是满足原 prior 的有限反例。

**按 affine worlds 匹配也有真实质量代价。** 若 B 分成 pieces B_i，每 piece 上 M 恰为某条 affine matrix function，则由 (1)，`ν(B_i)≤a`。若 g 只用 t,s 来自同 piece 的 tuples，原 mean 至多 `Σ_i ν(B_i)²≤a`。当 a=r^β、β固定而 η≪β，不能达到 `m≥r^η`。这只排除此种匹配机制，不是把任意 correlated g 都归成 worlds。

本轮未找到在原 matrix nonfit/slab prior/小损 graph density 全部保留时的 strict countermodel。上述两点是对具体攻击的费用核验，主新增估计是 (4)–(9)，不把旧 rank-one 分类重复登记为成果。

## 5. 为什么新门槛尚不产生 >2 observed 基数增益

原 finite candidate 另有 bounded `A⊂R²_x×R²_ξ`、每个 visible r-cell 至多 K 个 joint labels、`#A≤K r⁻²`，并要求原 g 支持 `a+D∈N_(Kr)A`。这些 A 信息未用于 (4)–(9)；所以证明仅提供必要的 **joint increment nonconcentration**，没有从 near-closure 推出足够多输出点。

特别，λ_g 不集中在固定 2-plane，并不自动使 A 的每个局部 component 饱和于同一 plane，也不证明 A 与 D 的独立卷积有小增长或大增长。R18 的 global marginal 独立化捷径仍冻结。若要接 inverse theorem，必须先保原 g 获得其真正适用的 additive/entropy输入，再把组件结构与 observed visible-fibre cap 对接；当前稿没有付这些步骤。

固定一个 ψ 后，horizontal increment沿 ψ，确可按 x⊥ψ 的 strips 分解 A；每个 r-strip遇 O(r⁻¹) visible cells，粗化和 output error还需 K 的固定幂。但这样也固定掉了原角维数。仅对该纤维调用没有正维参数的标量 ABC，不会免费给超过一维的 lower，更不能由此声称全 A 超过二维。这一维数预算说明，新增 visible block 必须在联合 prior 下实际使用。

与旧 R18 球 cap `(1+γ)` 不同，(5) 利用 QQ*=I 的 visible/vertical block 二择，直接控制所有 **affine 2-planes**，即使 M 的全部增量有共同像或含 singular matrices 也成立。但从此到 AFF₃ 的原图基数增长仍是一项真实缺口。源 observed A、原 W 重数和 used-angle law 是否具备本文 finite 输入，由本轮 A/source稿独立核；本文不预设全部source已付。

## 6. 严格数字模型：二维平面 cap 加 observed 粗图仍不足增长

以下是对**删去 matrix-time 实现要求后的推论**的严格反例。它保 bounded observed graph/coherence、near-2-Frostman、小基数、小损 bounded graph、以及非集中的真实增量 law；但不提供 (3) 的 M/time/原角实现，故不是 main finite candidate 或 source 的反例。

固定足够大的 `B=2^L`，N 为任意偶数，`r=B^(−N)`。对全部 N 位 base-B 小数

    x=Σ_(i=1)^N d_i B^(−i)， 0≤d_i≤B−1，
    f(x)=Σ_(i odd) d_i B^(−i)，

定义

    A₀={(x₁,x₂,f(x₁),f(x₂))}⊂[0,1)⁴， #A₀=r⁻²。

所有原子 uniform。D₀ law 取 Uniform(A₀)，并用实际实数向量作为增量；令 `A=A₀+A₀`。因为 0∈A₀，A₀⊂A。所有 support 位于固定 bounded box，fine 坐标在 r-grid，不需对有限计算求助。

### 6.1 A₀ 的全 dyadic coherence 和 2-Frostman

B 为2的幂，所以 f 是 binary digits 上保留奇数 block、清零偶数 block 的 map。若 x 处于任意 aligned dyadic R-cell、`r≤R≤1`，全部共享其 binary prefix；f(x) 的同长度 prefix 也固定，故恰在一个 dyadic R-cell 中。二维分别应用，A₀ 在任意 visible dyadic R-square 上至多占一个 joint R-cube。这不是仅在 base-B 尺度成立。

对任意 R-ball，visible 投影含 O((R/r)²) 原 x-grid点，因此 Uniform(A₀) 的质量≤C R²。此常数与 B,N 无关。

### 6.2 D₀ law 的所有 affine hyperplane cap

取任意 unit normal `n=(n₁,n₂,n₃,n₄)`，则

    n·D₀=Σ_i B^(−i)[(n₁+1_odd(i)n₃)d_i¹
                              +(n₂+1_odd(i)n₄)d_i²]。

四个系数 `n₁,n₁+n₃,n₂,n₂+n₄` 中至少一个绝对值≥1/4。选择其 coordinate/parity，条件化其它全部 independent digits；剩下的是一个系数 bounded below 的单 parity Cantor sum。其每两位取一个完整 B 字母，uniform 维数为1/2。直接 cylinder packing 给任意 `r≤u≤1` interval 的质量≤C_B u^(1/2)：选 cylinder 尺度 B^(−2k) 与 u 相邻，最多 O(B²) 个 cylinders，每个质量 B⁻ᵏ；odd parity 只是固定 B 倍缩放，末层 u≈r 的原子质量 r^(1/2) 同样满足界。C_B 是只依固定 B 的常数。

因此对每条 affine hyperplane H（从而每个 affine 2-plane P），

    Pr(D₀∈N_u H)≤C_B u^(1/2)，
    Pr(D₀∈N_u P)≤C_B u^(1/2)。                      (10)

这是对所有位置和 normal 的统一 cap，不只检验坐标平面。B 先固定、N 后任意大，C_B 可以由最后 r 小吸收至任意指定的小幂。

### 6.3 真实实数 sumset 的 cardinal upper：不省略进位

一个 scalar pair 的和可精确写为

    (x+x', f(x)+f(x'))=(Σ_i e_i B^(−i), Σ_(i odd)e_i B^(−i))，
    e_i=d_i+d'_i∈{0,...,2B−2}。

两个 coordinates 独立，于是无论这些 raw words 是否碰撞，都有

    #A≤(2B−1)^(2N)=r^(−2−ε_sum)，
    ε_sum=2 log_B(2−1/B)→0  (B→∞)。                 (11)

这只是按真实实数和的 raw digit word 作 upper，完全不需要把有进位的整数误当 digitwise group，也没有使用 Leibniz 法则。

### 6.4 A 的全 dyadic coarse-fibre cap：显式 carry 证明

固定一个 scalar visible sum X。把其 canonical base-B digits 写为 `X=k₁+Σ_i a_i B^(−i)`，`a_i∈{0,...,B−1}`。加法 carries 满足

    e_i+k_(i+1)=a_i+B k_i，
    k_i∈{0,1}， k_(N+1)=0。

给定 visible X 和一条 carry pattern，它确定全部 raw e_i。相应 vertical sum 为

    Σ_(i odd)e_i B^(−i)
       =f(X mod1)+Σ_(i odd)(B k_i−k_(i+1)) B^(−i)。   (12)

固定 carry pattern 后，第二项是常数。在任意 aligned visible dyadic R-cell 中，X mod1 的 binary prefix 固定（R≤1的 cell 不跨整数内部），所以 f(X mod1) 处于一个 R-cell，平移常数后只遇 O(1) 个 R-cells。每 coordinate 至多2^N条 carry patterns，两 coordinate 至多2^(2N)条。因此对任意 visible dyadic R-square，A 在其上占据的 joint R-cubes 至多

    C 2^(2N)=C r^(−ε_coh)， ε_coh=2 log_B2。          (13)

取 R=r 即得每 fine visible cell 的 joint fibre cap。由 `#A≥#A₀=r⁻²`，再以 visible r-grid packing求和，Uniform(A) 对任意 R-ball 的质量≤`C r^(−ε_coh)R²`。故它保全部尺度的近二维 Frostman upper，不是假定 sumset 自有无损 AD lower。

如改成三份 A₀ 相加或 `A₀+2·A₀`，carry 可取0,1,2，稳健同类上界为 C3^(2N)，不能沿用未经证明的2^(2N)。本模型只需要真实 A=A₀+A₀，故 (13) 已够。

### 6.5 同一个真实 bounded graph 与任意小幂损失

在 Uniform(A)×Uniform(A₀) 上取

    g(a,d)=1_{a∈A₀}。

g≤1，且所有正权 tuples 满足精确实数关系 `a+d∈A`。其 mean 为

    m=#A₀/#A≥r^ε_sum。                              (14)

对任意预给 η>0，先选固定 B 使 `ε_coh<η/10`，再取任意深偶数 N。则 `(11)–(14)` 的 card、coarse-fibre/Frostman 常数及 graph density 都有任意小于 η 的幂损失，同时增量保 (10) 的固定指数1/2。若有人只用这些量便声称固定正 gain χ>0，取 B 使 ε_sum<χ 即与 (11) 冲突。

这个 countermodel 排除的是“2-plane nonconcentration 加 observed coarse graph 自动增长”的无条件桥接，**没有**否定保完整 matrix-time action 的主目标。D₀ 是独立指定的真实有限 law；本稿未把它伪写为同一 M(t)、共同 time 和原角 prior 的 (3)。恰恰必须继续使用这一额外结构，才能绕开 (10)–(14) 的严格边界。固定 B 后所有深度均有效，非仅某个 loss 以外的单尺度例子。

## 7. 停止范围

已给严格原 time/原角先验及同 g 的联合二维平面 cap，并给真实 digit sumset 反模型排除只靠该 cap/coarse-fibre 的增长推论；未给 `#A≥r⁻²⁻χ`，未构造完整 source/Kakeya 反例，未证明 actual ell3 AFF₃。后续若只有改名、Y-only 投影或独立化，按本轮 macro 停止；本稿不追加 C²、irreducibility 或新的统计假设来伪造完成。

长期五维/一般 Kakeya Goal 仍 active。无新维数界、重大性或新颖性认证。
