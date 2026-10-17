# R0043：fine-PW 到真实粗管的共同平移平均

2026-10-17，独立反攻／证明，lifting_obstructions。本文只证明本轮 §18 加强类闭包的粗化接口及其原质量费用；完整实际操作由 root/A 另审。这里得到正向有限命题，没有构造 Kakeya 反例，也没有证明正 κ 极值类不存在。内部独立审查仍不等于外部同行评审，不宣新颖或重大。

## 1. 原量词、当前缺口与停止边界

固定 n≥2、同一 clock I（长度1或2）、固定复杂度指数 A。原有限管可重复，带非负权 ν_i，原总质量不超过1。首先使用精确 graph cylinders

    T_i(δ)={(b_i+t a_i+x,t): t∈I, |x|≤δ}.

记 q_i^δ(S)=|T_i(δ)∩S|/|T_i(δ)|。假设原 law 满足所有半代数 S、其 presentation 复杂度 E≥1、所有 0<λ≤1 的

    ν{q_i^δ(S)≥λ} ≤ C0 P(E)|S| λ^(−n),
    P(E)=(1+E)^A.                                      (1)

有限体积 S 即可；无限体积时结论平凡。所有测试都在同一 physical space 中，不准让每个 index 使用不同测试集合。目标是将每个 fine index 归到唯一粗管后，证明原权 pushforward 仍满足(1)，只损失依 n 和固定管形比较的常数，复杂度指数 A 不增长。它不是 direction-Frostman 的重新调用。

独立攻击包括：极小 λ、任意权跨度、粗化事件与原 index 的相关、微小 S、parent 边缘、dyadic tube 非圆截面、无权 coarse law 与 weighted pushforward 不一致。若共同平移平均只能得到 N_ρS，就不能据此判失败或添加 all-coarse 公设。本节以下给出真正避开 N_ρS 的证明。剩余实际 §18 量词、相对新尺度损失及 strict saving 不能由这个有限命题自动获得。

## 2. 未归一化子族的准确平均估计

取任意原 index 子集 H，保留原权，质量 a=ν(H)。对固定 S 置 B=C0P(E)|S|。由原(1)而非新的独立性假设，

    ν(H∩{q_i^δ(S)≥s}) ≤ min(a,Bs^(−n)).

若 0<B<a，在 s0=(B/a)^(1/n) 处分积分；若 B≥a，直接用 q≤1；B=0 时平均为0。统一得到

    ∫_H q_i^δ(S)dν(i)
      ≤ c_n B^(1/n) a^(1−1/n),   c_n=n/(n−1).          (2)

这一步的 a^(1−1/n) 必须保留。将 H 除以 a 归一化会把 PW 常数变为 C0/a；本文粗化证明直接用原 law 的(2)，避免丢失该分母。H 可由粗管、测试 S 和 λ 自适应决定，不要求 H 与 tube parameters 独立。

## 3. 共同横向平移的核支配

令 k_r 为 R^(n−1) 中 B(0,r) 的归一化指标函数。若 δ≤R，对所有 |z|≤R，B(z,δ)⊂B(0,R+δ)，故

    (k_(R+δ)*k_δ)(z)=1/|B(0,R+δ)|
      ≥2^(−(n−1)) k_R(z).

因此在整个横向空间均有

    k_R ≤ 2^(n−1) k_(R+δ)*k_δ.                       (3)

对任意 i，沿同一 clock 积分，Tonelli 给

    q_i^R(S)
      ≤2^(n−1) average_{u∈B(0,R+δ)}
             q_i^δ(S−(u,0)).                         (4)

u 的分布不依赖 i；它是整族共同的横向平移。时间没有移动，没有裁去端部，也没有将 S 换成 N_RS。每个 S−(u,0) 与 S 体积相同，presentation 的次数、个数和复杂度相同；系数大小变化不属于 E。故同一(2)可对每个 u 应用。

固定 R≥δ，令 H={i:q_i^R(S)≥λ}、a=ν(H)。先固定 H，再对 u 积分(2)，得

    λa ≤∫_H q_i^R(S)dν
       ≤2^(n−1)c_n [C0P(E)|S|]^(1/n)a^(1−1/n).

a>0 时约去 a^(1−1/n) 并取 n 次幂；a=0 时平凡。因此

    ν{q_i^R(S)≥λ}
      ≤ C_n C0 P(E)|S| λ^(−n).                       (5)

常数不依赖 R/δ、λ、权跨度或 index 数。原 PW 是 weak-L^n 的估计；(2)以任意原子族测试后，足以控制共同平移平均，不能仅将 Markov 不等式用于整族平均并丢掉 a 因子。

## 4. 真实 coarse representatives、dyadic 管形与重复 indices

设 coarse map i↦c(i) 为确定的有限映射，粗管宽 ρ≥δ；粗轴与每个原细轴在整个 I 内距离≤Cρ。设粗管自身宽为 cρ，c>0 固定。则它逐点包含于以该细轴为中心、宽 R=(c+C)ρ 的 inflated cylinder，且两管体积之比仅为固定常数。因此

    q^coarse_c(i)(S) ≤C' q_i^R(S).

若 C' 将阈值降到 λ/C'，(5)仍适用，所有 0<λ≤1 均保留。令 ν_coarse(c)=Σ_{i:c(i)=c}ν_i，便有

    ν_coarse{c:q^coarse_c(S)≥λ}
       ≤C_n,c,C C0 P(E)|S| λ^(−n).                  (6)

每个 coarse 事件的原 preimage 正是 §2 的 H，所以很多细管合到一根粗管不会被当成很多独立样本。不同 fine ancestors 的轴偏差可以不同；上面的固定倍 containment 先处理偏差，随后对原细轴统一使用同一个平移分布，并没有对 i 选择不同 u 后调用 PW。

WZ PDF16式(19)的普通管正是 clock t∈[−1,1] 的 graph cylinders。Def3.6 的 dyadic parameter cube p 在 |t|≤1 上截面，是 intercept cube 与 t 倍 slope cube 的 Minkowski sum；以中心参数给出的直线为轴，截面内含 c_nδ 球、外含于 C_nδ 球，体积也与 δ^(n−1)|I| 双边可比。parent 参数中心相差 O_n(ρ)，故整个共同 clock 上轴距 O_n(ρ)。这正是上段条件。

更严格地，从 dyadic fine tube 的 PW 转到内接 c_nδ graph cylinder，有 q_inner≤C_n q_dyadic；从 coarse dyadic tube 转到外接 C_nρ cylinder，同样有 q_coarse≤C_n q_outer。中间应用(3)–(5)，得到(6)，只是固定常数变大。管靠近 dyadic parent 边缘不影响这个论证：不要求 N_ρT 落在 parent 内，也不做指数依赖的 safety 删除。半开参数边界与截面边界均是 Lebesgue 零测集。

此处只要求原、粗管都使用共同 bounded clock 和双边可比的截面。若改为每个 index 不同 clock、只保一段 shading 后把新 tube 延长，必须另付 time-crop 费用；不能引用(6)免除它。

## 5. 无权粗管先验：AD 下确有原质量比较

weighted pushforward 不是 uniform coarse family。设原 fine family 是有限集合，原 law 为 uniform probability，每个 occupied coarse parent c 的原 fine count 为 n_c。若

    K^(−1)L≤n_c≤KL  （所有 occupied c），               (7)

则对 coarse 管数量 N、总 fine count N_f=Σ_c n_c，有

    (1/N)/(n_c/N_f)=N_f/(N n_c)
       ≤(max_c n_c)/(min_c n_c)≤K².

故 uniform coarse law 被 K² 倍原 pushforward 支配，(6)给其 PW 常数≤C_n K² C0。没有以 #coarse 代替 fine preimage count，也没有原权跨度的 dyadic log。

WZ Def3.9 joint t-AD 的 dyadic 版本，对每个 occupied coarse parent 正给 n_c∈[K^(−1)(ρ/δ)^t,K(ρ/δ)^t]。实际 d5 的 t=4，取 L=(ρ/δ)^4 即(7)。若已删到 T′，须使用 T′ 自己已证明的 AD 常数 K′；不能沿用删前的 lower。若原 ν 本来非 uniform，则 cardinal AD 并不自动控制 parent mass，须另证原权双边比较。更一般，若仅知每 parent 原质量在 K 倍同一平均值内，uniformization 花 K 的对应比较费用。

因此实际加强极值类的 PW 必须属于同一个 uniform counting tube law，或已明付其与该 law 的双边 domination。仅说“存在一个 whole-tube probability ν 满足 PW”，允许把大部分实际 tubes 置极小权甚至0，不能推出原无权 T 的粗化闭包。有限 §2–4 对任意原权成立，不补这个独立的 class-definition 责任；本轮源应用按 uniform law 的精确版本认证。

先将原 fine uniform family 限制到 T′，其原质量 p，归一化为 uniform T′：PW 常数先变 C0/p；之后 coarse/unweighted 花 (K′)²。若只重选 shading 而 whole-tube index law 不变，则 PW 本身不花 shading density；但 subsequent 删除整条 tube 仍须记实际 p。原平均 shading 如何保留和 subsequent 极值调用是否合法，由实际 §18 操作另审。

## 6. Parent、相对新尺度与固定 complexity exponent

共同 parent 的 affine/crop 费用沿用 R42 已独审公式。n=5，原 selected index 质量 p、横向尺度 r、共同 clock 长 q，将它同时归一化到 unit clock 后

    C_new = C_old r^4/(p q^4).                        (8)

式(6)没有新增小尺度比，式(7)只有 AD 常数的固定幂。如果实际选择的整个 parent 原质量 p≥K^(−1)r^4，whole clock q=1，则(8)的 r^4 被 p 抵消；若 q<1，q^(−4)照付。不能把(6)误读为短时间线段可以免费延成长 whole tube。

这里的 parent-mass lower 是另须支付的条件：source 在固定 bounded joint-parameter chart 内，用总 finecount≤C Kδ^(−4)及 occupied parent lower 得到 p≥c K^(−2)r^4。仅局部 AD 而无总计数上界，不能推出这种 probability lower。远隔平行满网的任意多份复制就是校准；准确的 r^4/p 公式始终成立，不能在无界 chart 中直接消掉 p。

若新尺度 δ_new=ρ/r，写 c=log δ_new/log δ>0，任何剩余 δ^(−Cη) 的费用换成 δ_new^(−Cη/c)。只有实际尺度选择给定 c 的正下界、再令 η 充分小时，才能称相对 δ_new 任意小幂；本命题不假定这个下界自动成立。对后续有限多次操作，须实际计算其 c 与保留质量，不以“都是 subpower”略过。

所有测试集合只经共同 translation 或共同 affine substitution。它们不增长 presentation complexity E；对测试求平均不把无穷多 translates 的 union 当一个新测试。故同一指数 A 保持，常数仅乘管形/维数常数和原质量/AD 比较。若未来出现 nonlinear projection、不同 frames 的集合并或正厚化，则不在这个固定指数结论内。

## 7. 本轮独立结论与尚未支付责任

fine PW 确实推出实际共同-clock D_ρ coarse 原权 pushforward PW；有 joint-AD 双边计数后，也推出 uniform coarse PW。仅指出 fine 管访问 N_ρS 而非 S 的逻辑缺口，不构成这一转移的不可能性；共同平移平均补齐了它。没有必要向类定义添加 all-coarse PW。

本有限结论不使用 positive κ、joint-AD/CW 或 shading；后两者只在实际 class 和 §5 uniformization/parent 费用中进入，因此不存在将缺 κ 的 calibration 冒充 full-source counter 的问题。它也不提供一般 Kakeya 到 joint-AD/CW 的初始归约。PW 比满维 direction-Frostman 更弱的 R42 平行管例仍成立，故这里不是重新假定同一 angle law。

完整 §18 recurrence 是否真的保持加强极值类，仍需实际读每次 restriction 的 mass、wholeclock、δ_new、反复 extremality 调用和参数顺序。即使全部闭包通过，也还须找到有真实复杂度和原 shading 的 strict saving 测试；没有该 saving 就不宣五维 κ≤ζ、一般 Kakeya 或重大结果。本稿交 root/A 独立逐式审查，正式全文审查另写指定 review。
