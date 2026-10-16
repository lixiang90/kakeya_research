# R0027：matrix D-plane gate 与 digital observed boundary 独立审查

2026-10-17，`audit_four_dimensional`。逐式审查：

- root `R0027_matrix_translation_plane_gate.md`；
- root `R0027_digital_observed_boundary.md`；
- B `R0027_matrix_observed_counterattack.md`（当前 §1–7，含真实数字加法模型）。

**结论：通过，可在下列 scope 内归档。** 本 review 独立核这三稿的有限数学。本人原 source 稿不是自身的独立认证；其 W/counting 接口由 B 交叉审查。根据 B 指出的真实责任，本人只收紧 source §8 的泛称：heavy lower 不能免费传任意斜率 matrix affine nonfit；现限定为有完整 fine-preimage 和已支付增厚误差的事件，plane 应用仍按 fine-law→D-event 的既有正确路线。

## 1. 任意 affine 2-plane 的 normal block 分解：通过

任意 affine 2-plane 都能写作 `P={z:Qz=c}`，Q 有正交单位行，故 `dist(z,P)=|Qz-c|`。分块 Q=(A,B) 后，`AA*+BB*=I₂`。该表示包含所有 offset、vertical、horizontal、近退化 P，不要求它是 bounded-slope graph。

### B 非退化

当 `σ_min(B)≥λ`，原

`D=((t-s)ψ,-[M(t)-M(s)]ψ)`

满足 `QD=-B N_ts ψ`，其中 `N_ts=ΔM-(t-s)B^-1A`，顺序 B⁻¹A 正确。因此 D近P 推出 `|N_ts ψ+B^-1c|≤ε/λ`，符号和矩阵乘序均无误。

固定 s 时，`||N_ts||≤h` 正是 all-real matrix affine fit，slope为 B⁻¹A、intercept为 M(s)−sB⁻¹A；该 slope/intercept 可很大，但原假设覆盖它们。故此 pair事件质量≤a。

若 `||N_ts||>h`，最大奇异方向给一个长度>h的 row，左乘并归一将 ψ 限制在宽 `Cε/(λh)` 的 affine slab。中心含 B⁻¹c，可任意大；原 slab 假设对**全部中心**成立，所以不需要把 P 设为过原点。没有使用 N_ts 满秩。

### B 近退化

当 `σ_min(B)<λ`，取单位 w 使 `|B*w|<λ`，由正交块恒等式有 `|A*w|²=1-|B*w|²≥1-λ²`。所以

`|(t-s)(A*w)·ψ-w·c|≤ε+2λ`

确实成立。删 `|t-s|<g` 的原 ν² 质量≤C K_t g，前提 g≥d 已列。余下除以 time gap 和 |A*w|，得到宽 `C(ε+λ)/g` 的原 affine slab；offset wc依旧保留。

因此 B稿 (4a)/(4b) 与 root稿 (3) 均成立。代入 ε=h⁴、λ=h²、g=h，两个 raw widths都是O(h)。q_base以下向上clip、超过1用trivial1是必要且正确的；没有在非法base下直接套更小幂。

## 2. all P、同 g 及 fine→coarse 的量词：通过

估计对每个 P 都由同一确定性代数和 uniform slab 假设推出，所以可同时取 sup_P；无需对不可数 planes 作概率 union。dim≤2的 affine subspace可嵌入2-plane，其邻域事件更小，推广正确。

原 graph `0≤g≤1`，reference为 `σ_A×ν²×μ²`，ψ是原 μ² 的差映射。因此未归一事件积分≤同 ν²×π 的 D事件，conditioned graph law只多 mean(g)⁻¹。没有假设 g的角/time 边际仍有原cap，也没有将 g独立化。若 eventupper比mean(g)小，才可排 graph全部落一固定plane。

coarse proxy与每个原fine preimage相距≤r_err 时，coarse宽 h⁴/2 的事件包含于fine宽 h⁴事件（r_err≤h⁴/2）。uniform coarse prior的比较另需真实 heavy occupancy两侧界及angle有界碰撞，root已明确乘K固定幂。这个 transfer控制的是 **D-plane事件**，不等于原 all-real M-affine nonfit可经未知 `|R|r` 的clock error直接继承。

actual source的尺度校准正确：fine M在 `h₀=ρ^ε₀/L_f` 有fitcap后，取 h=ρ^(2ε₀)、ε₀<1/32；source loss后小，则 h<h₀、`Kρ≪h⁴=ρ^(8ε₀)`、`d=δ/ρ≤ρ³≪h`、`q_base=Cρ≪h`。所有 time/slab查询及 relationerror均处合法范围。固定幅度归一须同步 observed ξ和M，原稿有该要求。

## 3. 共同核和 affine-world 攻击的费用：通过，限其陈述

B §4 的两项具体排除正确：固定非零 R₀ 下 `|R₀ψ|≤ε` 由最大奇异 row及原slabcap付 `C_π(Cε/||R₀||)`；任意相关 g≤1不能扩大该 reference事件。若g只用某个 affine world 的两 times，而每 world质量≤a，则总mass≤Σν(B_i)²≤a（这里以 disjoint pieces为前提）。它们排除这两个具体攻击，不把任意 g归类为worlds，也不证明主finite candidate无反例。

## 4. 数字模型的真实定义与所有 dyadic 尺度：通过

B=2^L，N偶，r=B^-N，取终止 N位 B-adic/长度LN位 binary展开。mask f只保奇数blocks中的bits，不发生函数定义内的carry。对任意 aligned dyadic `R=2^-j∈[r,1]`，visible x的共同 j-bit prefix决定 f(x)的同长prefix；即使j在一个block内部也成立。因此 A₀在每visible R-square只落一个 joint R-cube，不只在B-adic层。

两维visible full r-grid给 `#A₀=r^-2` 和 r-separation。任意R-ball的visible投影含≤C(R/r)²个该grid点，所以 UniformA₀的 2-Frostman upper为CR²，不需要给f跨dyadic边界的Euclidean Lip。

任意平移的visible R-square可由常数个标准dyadic R-squares覆盖；非dyadic半径也可与相邻dyadic尺度比较。故所需任意位置coarse-fibre cover不会因仅陈述aligned格而留下漏洞。

## 5. λ=UniformA₀ 的全 normal、全 offset hyperplane cap：通过

unitnormal n下，投影系数是 `α₁,α₂,α₁+β₁,α₂+β₂`；至少一个绝对值≥1/4，否则单位长度不可能。选择该 coordinate/parity后，其余三组digits与该组独立，可以全部条件化。所留变量为每两位取一个完整B字母的有限Cantor sum；偶组每级scale B^-2、质量B^-1，奇组只是固定B倍缩放。

cylinder尺度相邻比B²是固定常数，因此对所有 `r≤q≤1` 有 `Pr{Z∈I}≤C_B q^(1/2)`。N偶时两parity的原子质量均为r^(1/2)；最细odd spacing为Br、even为r，q=r端点仍合法。选中系数有统一正下界，只改变C_B，interval centre可任意。因此结论对全部normal和affine offsets同时成立，不作无限normal union。

affine2-plane包含于某hyperplane，故同upper也控制它。特别在固定 q=r^ε、0<ε<1处，N后大使 `C_B r^(ε/2)≤r^(ε/3)`，是独立小loss η的固定正幂。

## 6. 实数和、carry patterns 及 all-dyadic A：通过

本模型的 `2A₀` 明确是 A₀+A₀（两份相加）。因0∈A₀，root的 A=A₀∪(A₀+A₀)等于 B稿的 A=A₀+A₀。没有三份相加；无需carry取0,1,2。

对每scalar coordinate pair，真实和严格为 `(Σe_iB^-i,Σ_odd e_iB^-i)`，raw e_i∈[0,2B-2]。按raw words计数给 upper `(2B-1)^(2N)`；即便不同words碰撞也只使card变小，不假定digitwise group加法。

已核 B稿显式normalization：

`e_i+k_(i+1)=a_i+B k_i, k_i∈{0,1}, k_(N+1)=0`。

可由最低位向上递归得到；给定visible X的canonical N digits及carry pattern，e_i唯一。vertical sum等于 `f(X mod1)+Σ_odd(Bk_i-k_(i+1))B^-i`。root的carry公式采用边界索引平移，含义相同；首位integer carry单列，不改变2^N upper。

每fixedcarry pattern的第二项是常数。visible dyadic R-cell（R≤1）不跨整数内部，故X mod1的binary prefix固定，mask后落单个R-interval；加常数最多遇固定数相邻vertical R-cells。每coordinate至多2^N patterns，两coordinate至多4^N，得到全dyadic coarse-fibre `C4^N`，包括非B尺度及R=r。无需给sumset免费graph性质。

## 7. UniformA 的 fine mass cap：通过，未偷用 coarse cover

这里不能只说每joint R-cube中有O((R/r)²)原labels。正确的终稿证明用 **R=r的真实纤维**：每visible r-cell至多C4^N个joint points（support在r-grid、固定X的vertical值由carry pattern界定）。一个R-ball的visible投影只遇C(R/r)²个fine visible cells，所以

`#(A∩B_R)≤C4^N(R/r)²`。

再除 `#A≥#A₀=r^-2`，得到 UniformA(B_R)≤C4^N R²。故(r,2,K)Frostman确由fine counting推出，不是把cover upper误当weighted mass upper。它也不宣称裁切A有AD lower。

card、coherence和graph费用的精确指数为

`θ_sum=2log_B(2-1/B)`, `θ_coh=log_B4=2log_B2`，二者随B→∞趋0，且θ_sum<θ_coh。

任意η>0先取固定B使两者≪η，再取任意足够大偶N吸收C/C_B。则 `K≤r^-η`、card≈K^±1r^-2、全部coarse fibres与UniformA cap成立。取 g(a,d)=1_(a∈A₀)，同 UniformA×UniformA₀ 下 mean≥r^θ_sum（root的1/2版本更保守），且真实 a+d∈A，无输出增长。图条件化后的increment law仍正是λ，因为g只依a。

这与第5节fixed hyperplane非fit兼容：B可依η取大，但1/2指数不变；C_B只需N再大。若声称仅由这些弱接口能给独立η的正gainχ，另选B使θ_sum<χ也可同时完成。因此counterexample量词强度足够，不只是固定η之外的一次校准。

## 8. 范围与最终 verdict

三稿均可按当前边界归档：真实 matrix-time law由wholematrix非fit和原角slab给统一 affine2plane cap；数字模型严格否定**删掉matrix-time分解后**仅凭多尺度visible fibres、2-Frostman、非平面law和小损near-closure自动取得fixed增长的桥。

数字λ没有实现同一个 `D=((t-s)ψ,-ΔMψ)`、原ν/Φ、真实W witnesses或完整jointtube AD/CW/两grain配置。它不否定主finite matrix目标、原source、AFF₃或Kakeya。plane gate亦不证明A的>2增长。当前main AFF₃未解，无新高维维数界、真实Kakeya反例或重大性认证。按指派完成后停止编辑，不新增理论任务。
