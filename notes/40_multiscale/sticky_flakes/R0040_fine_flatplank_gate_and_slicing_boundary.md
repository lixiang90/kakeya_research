# R0040：真实来源的细尺度平直薄片门槛与切片边界

2026-10-17，root 整合证明。长期目标仍是 n≥5/一般维度的欧氏 Kakeya；本轮主候选为完整 WZ d=5,k=ell=3 配置的 κ≤ζ，**未证**。本文证明的只是一个条件于已具名来源引理的提取限制，另核两个几何转移反例。不宣称新的维数界、重大成果或新颖性；未经外部同行评审。

## 1. 来源、量词与对象

采用 literature/primary/wang_zakharov_2026_sticky.pdf 的 Definitions17.2–17.4。固定 ζ,γ,c0>0，d=5,k=ell=3，κ≥ζ；η 足小。所有原始条件均保留：原 T 的 (4,δ^{-η})-AD 与 C_CW(T)≤δ^{-η}，δ-separated Z 及密度，bounded dyadic-Lipschitz f(z)∈Mat(2,2)，完整 Y_z 的 AD 和 tube-Katz–Tao(1−γ)，dense horizontal X_{y,z}，ξ/Φ/slab/coherence 与真实原整管 witnesses。写

    E_z={(x,y+f(z)x,z):y∈Y_z,x∈X_{y,z}},   Eδ=N_{C0δ}(E).

C0 是固定常数。本文只用 fine δ blur；不把 E_e,e≫δ 偷换进来。

bounded f 是原来源的字面约定：PDF65、提取文本行3361在 Definition17.2 前定义 Mat(k,ell) 为 entries∈[−1,1] 的矩阵。root与两代理再次核原文字及页面；不从 dyadic-Lip 的差分条件推绝对 bound，也未额外添加 chart 假设。

**平片结论。** 存在 c=c(ζ,γ,c0)>0、η0>0，使每个 η≤η0 及充分小 δ 都满足：对每个位于固定有界球内、边长 a×b×1×1×1 的 affine rectangular plank F，若 δ≤a≤b≤1，且其 long3-plane P 满足 |proj_P e_t|≥c0，则

    |Eδ∩F|≤δ^c |F|.                                      (FG)

常数倍轴长、固定倍 δ 下界、有限个 unit-long boxes 只改固定常数。量词是对每个原配置及所有 F 同时成立，不需为 F 做无限并集估计。输入明确包括原 Lemma19.2；本文不重证该高级引理整个证明。

## 2. 原 Lemma19.2 的准确调用

原 PDF78/提取文本行4124–4131：对一个完整 ell-linear k-planar (δ,η,κ,γ) 配置，η<γ，若有 ρ∈[δ^{1/3},1]、σ_L∈[ρ²,ρ]，使每个 z0∈Z 及其 dyadic ρ-time window 都有至少 δ^{ε19} 比例的 z 满足 |f(z)−f(z0)|≤σ_L，则

    C_CW(T) ≳ δ^{C(η/γ+ε19)}(ρ/σ_L)^κ.                  (19.2)

只找到一个好 window 不够。下面通过整层 restriction 得到所有新 times 的 whole-matrix 近常，故每个新 window 的比例实为1。使用完整原 T 的 CW，不是某个 shortened tube 或 slice 的 CW。

## 3. Plank 参数与 normal 时间分量

V=P∩e_t^⊥ 是固定二维 horizontal plane。取其正交基 v1,v2，取 P 中垂直 V 的单位 v3 且 v3·e_t=h=|proj_P e_t|≥c0，再取 F 的实际两根短轴为 n1,n2（不能任意旋转 anisotropic P^⊥ 的轴）。用

    q=c+s1 v1+s2 v2+s3 v3+r1 n1+r2 n2,
    |s_i|≤C, |r1|≤Ca, |r2|≤Cb

覆盖 F 的固定倍 enlargement。把 s3 换成实际时间 t，Jacobian 为 1/h。短轴 n_i 可有时间分量；该换元已经支付它们，不需假短轴水平。固定 t,r1,r2 后，水平截面方向始终为同一个 V，offset 可以任意。

每个 exact z 的 O(δ)-time band 在此参数域中的总体积≤C(c0)abδ。每 t 只有 O(C0) 个原 z 可能贡献 Eδ，因为 Z δ-separated；fine blur 不混合 e/δ 个来源层。以下在每个 exact z 用 L_z(x,y)=y−f(z)x，不对跨 dyadic 边界的 f 偷用 Euclidean Lipschitz。

## 4. 逐层 Tube-KT 给出不依赖短轴的积分上界

令 λ_z=||L_z|_V||_op。若 λ_z≥σ≫δ，对 V 的参数作 SVD 旋转，固定较小奇异方向参数。沿最大奇异方向，L_z 的像是速度 λ_z、长度 O(λ_z) 的直线段。属于 Eδ 的点必须满足 dist(L_z(q),Y_z)≤Cδ。原逐层 Tube-KT(1−γ) 给该线段的 Cδ-neighborhood 内至多

    Cδ^{-Cη}(λ_z/δ)^{1−γ}

个 δ-cells，每 cell 在原一维参数中占长≤Cδ/λ_z。故截面面积≤Cδ^{-Cη}(δ/σ)^γ。线段长大于1、固定倍 blur 和边界覆盖都只需 O(1) 个分段；沿另一个参数积分范围有统一常数。

记 Zσ={z:λ_z<σ}，其截面仅用 bounded area。积分 r1,r2,t 并保留 ab 得

    |Eδ∩F|≤C(c0)ab[δ#Zσ+δ^{-Cη}(δ/σ)^γ].             (1)

这里没有 a^{-1}/b^{-1} 损失，也没有用 AD 自动代替 Tube-KT。原 X 的全局稠密性没有被误用为每个 local square filled。

## 5. 较大密度迫使固定 whole matrix 近常

反设 |Eδ∩F|≥δ^c|F|，取 σ=δ^{1/4}。选 c 小、再取 η 小，使 bad-time 项 δ^{3γ/4−Cη}≪δ^c，则 (1) 给

    #Zσ≥c1 δ^{c−1}.                                   (2)

固定因子以下可吸收为 Cc+Cη。对任意 z∈Zσ、v=(x,y)∈V，有 |y−f(z)x|≤σ|v|。f bounded 强迫 |x|≥c2|v|，否则 |y|≤C|x|+σ|v| 与 |v|²=|x|²+|y|² 矛盾。因此 π_x:V→R² 是 uniformly invertible；存在由同一 V 决定的 bounded G，使

    V=graph G,   ||f(z)−G||≤Cσ   (z∈Zσ).               (3)

这是完整2×2矩阵近常，G 不随 z 或 normal offset 变化；不是只控一个条目。

## 6. 合法整层 restriction 与 allowed scales

取 Z'=Zσ，保留其每个完整 E_z,Y_z,X、原 ξ/Φ/coherence/witness；保留全部原 T。**不把 F∩E 的点子集当新配置。** 取 η'=Mη，其中 M 是整数，且

    C1(c+η)≤η'≤C1(c+η)+η.

新 allowed δ^{η'j} 是旧 allowed δ^{ηj} 子格；(2) 给 #Z'≥δ^{η'−1}。原逐点/逐层 AD、Tube-KT、slab、X 下界及 coherence 以较弱 η' 成立。

跨时间 Y-union 的 lower 不能只说 restriction 自动继承。完整证明参见 R0022_time_restriction_closure.md，并在此复核：对新 allowed ρ 和 occupied time interval J，U'=∪_{z∈J∩Z'}Y_z⊂U=∪_{z∈J∩Z}Y_z，upper 从原 union 继承。任取 occupied ρ-center，选附近某个完整 Y_z 的点。该 Y_z 在 R-ball 的 fine AD lower 至少 δ^η(R/δ)^s 个 cells，s=2−κ；每个 ρ-cell 用这个 Y_z 的 fine AD upper 至多 Cδ^{-η}(ρ/δ)^s 个。故 U' 在固定倍 R-ball 的 ρ-cover 数≥cδ^{2η}(R/ρ)^s。R≈ρ 由至少一个 occupied cell 补齐。固定倍 ball/grid 只损常数，η' 吸收。没有赋予任意 selected Y-subset AD lower，也没有把 union AD 升格成 Tube-KT。

因此删整层后仍是具名19.2所需的完整同 κ,γ 配置。未改 T，其 AD/CW/整路径均保留。

## 7. 平均与逐管 marks 的区别

为核原 law 的费用，每个 p∈E' 的各 fine Φ_p-bin 选原 witness T。原数据给

    #E'≥δ^{-5+κ+Cc+Cη},   deg_witness(p)≥δ^{-κ+Cη}.

每个 (T,z) 只承载 O(1) 个 δ-separated p；原 #T≤Cδ^{-4−Cη}。故在**原 uniform-T×unit-time law** 中，retained raw marked mass 至少

    δ (#retained original incidences)/#T ≥ δ^{Cc+Cη}.    (4)

这里只是平均 duration，不能断言每根 T 都有这么多 marks。调用19.2本身使用完整配置；(4) 另行证明没有成功后验归一化或原质量消失。若后续需要逐管 dense marks，必须另外 heavy filter 并付 loss，本文不作该断言。

## 8. 每个新 window 满足19.2并反原 CW

由 (3)，全部 z,z0∈Z' 有 |f(z)−f(z0)|≤Cδ^{1/4}。取新 allowed ρ 为从 C^{1/2}δ^{1/8} 向上 rounding 的最近尺度，令 σ_L=ρ²。于是

    c3δ^{1/8}≤ρ≤C3δ^{1/8−C3η'},   ρ≥δ^{1/3},
    ρ²≤σ_L≤ρ,   |f(z)−f(z0)|≤σ_L.

所有新 times 均好，故每个新 window 的条件成立，ε19=0；若要求正 ε19，任选足小正数吸收。19.2 给

    C_CW(T) ≳ δ^{Cη'/γ−(1/8−O(η'))κ}.                  (5)

κ 原有 bounded range。先取 c≪ζγ/C，后取 η≪c，使 η'≤C'(c+η)≪ζγ/C 且 η'<γ，(5) 严格大于 δ^{-η}，反原 CW。固定常数由充分小 δ 吸收，得到 (FG)。不需整个 source 的 κ≤ζ 作为输入，也不把内部参数 ρ 当一次免费空间 rescaling。

## 9. FG 对新定理排除的精确范围

任意有限 family 的上述 F，任意非负 weights，若 Y(F)⊂Eδ∩F，则其按原 Σw_F|F| 计算的平均密度≤δ^c。因而不可能在 η_src→0 时保留 δ^{Cη_src} 或 δ^{o(1)} 平均密度，直接套新 LPSW 的 whole-clock fine-flat input。

这**没有排除所有 fixed-loss LPSW 调用**：若 a=δ^u，0<u≤1，定理门槛 λ≥a^{η_L}=δ^{uη_L}，FG 只给必要条件 uη_L≥c（固定因子留余量）。若 uη_L≥c，仍须计算输入 η_L(ε_L)、volume/mass 与输出 saving；不能因为可以选较小 η_L 就断言所有较大可用 η_L 无效。

也未覆盖：clock transversality 随 δ 消失；E_e,e≫δ 的 coarse shading；额外空间/curved sheets 的合法方案；支付 fixed loss 后仍有真实 gain 的方案。对 coarse blur 同时可混合 O(e/δ) 层，逐层 Tube-KT 不直接控制其 union。以上未覆盖项是范围声明，不是自动授权下一轮逐一阈值改名再试。

## 10. Ambient all-convex cap 不能免费赋给每个 slice

B 独稿 §3 给一个完整 flatflake family，root 逐步复核。坐标 (x1,y1,x2,y2,t)，r-grid a,b∈[−c0,c0]，#indices≈r^{-2}。F_ab 为 orthonormal (1,a,0,0,0)、(0,0,1,b,0)、e_t 三方向的 unit3-cube 的 r-neighborhood，体积≈r²，full shading。

对任意 convex K，设 contained indices 为 S，A=osc_S a,B=osc_S b。K−K 含三个独立 unit-order tangent vectors、r-ball，以及比较共同 x1=c 或 x2=c 的 axis points 所得 cA e_y1、cB e_y2。其 convex hull 含体积≥c(A+r)(B+r) 的5维 crosspolytope（取每个 normal 方向的 A 或 r 中较大者；三个 tangent 的 x1,x2,t minor 有固定下界）。经典固定维凸体差体积界 |K−K|≤C5|K|，加 grid packing #S≤C(1+A/r)(1+B/r)，给

    Σ_{F_ab⊂K}|F_ab|≤C|K|.

但 central thick slice |x1|,|x2|≤cr 中，各 cut 投影到 (y1,y2,t) 都含同一 c'r-tube、contained 于同一 Cr-tube，故 indexed slice tube density≈r^{-2}。取 essentially distinct representatives 会损 r² 比例 indexed slice mass。central slice 仅承载 O(r²) 原总质量，所以它不反 LPSW9.2 的 global paid refinement；只反“每 slice 免费继承 cap/distinctness”。固定维差体积界在此作为标准凸几何输入，不冒称新结果。

## 11. 移动 grains 的真实 slice 是曲线

原 line p(t) 加满 horizontal2-patch 形成

    S_p={(p_x(t)+u,p_y(t)+f(t)u,t)}.

若 u 在开集、t 在非退化区间且整个 patch 在一个 affine3-plane 中，则其固定 horizontal kernel 必等于每时刻 graph f(t)，强迫 f 恒定。这不意味着离散 dense X 有开内点；仅否定免费将整 ruled patch 叫 flatflake。

slice x=(a,b)，取 f(t)=diag(t,t²)、p(t) 为 clock axis，得 γ_ab(t)=(at,bt²,t)。该例不是完整 κ>0 source。对任意 affine line L、|a|≤1、0<|b|≤1，

    Leb{t∈[−1,1]:dist(γ_ab(t),L)≤e}≤C sqrt(e/|b|).      (6)

投影到曲线的二维平面，坐标为 (sqrt(1+a²)t,bt²)。line-normal 若第二分量≥1/8，用二次 sublevel；否则导数绝对值≥1/2。事件至多两个 intervals。若原 time law 在长度 h 的 J 上满足 ν(I)≤K_t(|I|+d)/h，任意相关 retained event 被 N 条 e-tubes 覆盖且原质量≥β，则 union bound 给

    N≥cβh/[K_t(sqrt(e/|b|)+d)].                         (7)

不用独立性、整段 marks 或换成 Lebesgue 先验。b 固定、e≈ρ²、d≪ρ 时，若 h≥ρ^{1−c1}、固定 c1>0 且 β/K_t≥ρ^{o(1)}，则迫 N≥ρ^{−c1+o(1)}，排 subpower-size line 表。仅 h/ρ→∞ 不够，log 比率只迫 log 大小。但 local horizontal radius R≈ρ、|b|≈ρ 时门槛只是 h≈sqrt(e/ρ)=ρ^{1/2}。不能把 unit transverse 示例套给所有 local freeze。

## 12. 本轮实际得失与停止

未得主 κ≤ζ、实际 Kakeya 反例或 strict source saving。新增信息是实际完整来源的 FG 条件推论，以及全片 indexed slice 转移和曲线 line-table 的严格边界；不是 R39 平行 Cantor normal 的同义费用校准。来源19.2未在本轮全篇重证，外部 peer review 未完成，novelty/major 均不认证。

按 R40 退出条件冻结“细 δ、whole-clock、subpower-dense flat3-flake 直接提取”及免费 ambient→each-slice cap。其它 fixed-loss/coarse/auxiliary 可能性没有被全部反证，但无新机制不继续局部 blur/clock/threshold 改名。提前 macro 见 research/reviews/R0040_macro.md，下一任务转真实 all-directions 构造的 power-saving 检验。旧 matrix/action/carry/CP⇔PM 冻结保持。

两代理已实际读本文12节、macro8节、nextspec及对方全文，并正式写 R0040_source_and_mass_review.md、R0040_slicing_and_quantifier_review.md；root实读两稿与两份正式review，修正实际短轴及固定幂时间比率后，限定范围通过。详见 R0040_root_integration_review.md。本文不增独立结果 ID，未经外部同行评审。
