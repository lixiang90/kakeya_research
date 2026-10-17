# R0058：完整路径筛选与 common-kernel 原 finite 接口审计

2026-10-17，A。按固定入口恢复 GOAL、STATE、ROADMAP、registry78状态、R57 next、R58 working_spec/macro；原目标仍 ordinary n≥5/general 或经审查重大结果。本稿 phase I 不重查未变化官方版本，不重证四维 assembly、KT 算术或 R57 包络。新输入仍仅已存 elliptic Th2.2；其103页 wholeproof 未独证。候选先报 root 再选择，本稿不把尚未选择/证明的命题列为成果。

## 1. 两个候选及实际选择门槛

优先候选是 actual WZ d=5,k=ell=3 的 **common-kernel** 非线性矩阵分支：

    f(z)=F0+u(z)rᵀ，r为固定非零row，u(z)∈R²任意。

它是所有 pairwise matrix differences 都秩≤1时、与 common-image 不同的自然分支。r 可规范化为单位长度并把幅度并入 u；F0 的常数项在 secant increments 中抵消。不假 u 光滑、低次数、曲率下界或条件独立。目标仍是在完整原 Def17.2–4、原SM和合法输出图下排除固定 κ>ζ，而非只证明一个 canonical u 的 union 很大。

第二候选曾为 HR restriction 递归的 actual m=3 tangential terminal 能否使用新 R3 elliptic 全振幅输入；它不同于 R48 Kakeya finite4D 替换，但 actual terminal 仍是原 Rn 中的 tangent varieties/wave packets，不能先假可 flatten。root 倾向第一项后，本稿不施工第二项，不为 terminal flatten/G3 的旧未付接口换名。没有新的几何转移就不把它作为下一主任务。

## 2. 已实际重读的 primary 与旧证明范围

重读 WZ2609.22035v1 原 PDF88–89、抽取 `split('\n')` 4603–4695行的 (163)–(166)：原 Lemma20.3 只述 f∈Mat(1,d−2)，输出 A 为标量，才可按固定 Φ 差调用13.5。五维 Mat2 分支并不是原标量定理的字面结论。

已实际读 R0016_matrix_span_boundary、R0016_source_linewise_application、R0016_vector_attack §§1–5、R0016_weighted_coarsening。R16 全部 fixed-ψ images linewise 的分类只有 PENCIL 与 IMAGE：

    F=F0+h(b)M，或 F=F0+v r(b)ᵀ。

common-kernel F=F0+u(b)rᵀ、非共线 u 不属于这两个全局 linewise 类。若 u 又共线，则回到已付旧类，应直接调用已有结论排重。此处不是重新发现 linewise 分类，也没有证明 approximate rank-one classification。

elliptic 原 PDF9–12 Def2.1/Th2.2/§2.2/Lemma2.3 已在 R57实际复核：时间须条件于一个确定 U/V 的 base label 满足 all-depth 双 profile，初始同形双椭圆 joint cap，finite D 及 X_v 左端点全部保留。本轮若改变量角色，必须重新核这些完整假设，不能继承 R57 的 K 或 uniform 原时间。

## 3. common-kernel 的真实原图及质量

R16 已付 actual source counts 的接口可原样作为已审工具引用，不能重记为本轮新提取：在 source-allowed ρ 上取 actual good q 和 endpoint z*，保原 witness/used-angle mixture，选实际 τ-window，再以 τ 缩 y、ρ 缩 time。得到同一个 coarse resolution r0=ρ（以下不与row r混淆）的数据：

- 非空 A_-、A_+⊂R²，输入来自原 Y_(z*) 的真实 heavy local cells，输出在其固定扩大，#A_+≤K^C#A_-；输入有原 (2−κ) AD上界与1−γ的tube Katz–Tao，不给裁切子集免费AD lower。
- 同一个 B⊂[−1,1] 的 r0-separated time set，exponent-one Frostman 常数 K^C；两个时间坐标保同 B 与原 heavy preimage 权，不重新 uniform 原 fine points。
- 原 used H⊂R²，保 κ-cover upper 与 γ-slab cap（原 Φ_p mixture 而非 unused Φ_q cells）。差标签可有重数，先验为原 H×H 的有序差 law。
- 0≤g(y,b,s,φ,φ′)≤1，平均≥K^−C，支持

      y+(b−s)[F(b)−F(s)](φ−φ′) ∈ N_(C r0) A_+。

K=δ^−Cη，source η 后取小，使它在 r0 单位为任意小 power。原完整配置不是被声明成一个新的 AD regular restricted tube family。

这里 τ≈δ^−ηρ²，F=(f−f(z*))/(τ/ρ)，其 small amplitude 抵消 coarse time error δ^−ηρ，所以输出误差仍 O(ρ)，不是自动膨胀到ρ^(1−Cη)。原 all-real affine nonfit 由 heavy-time lower 与 bounded recovered slope 回传，已有明确精度/质量余量。上述正常化不改变 exact common-kernel 关系。

在本分支令 θ=rᵀ(φ−φ′)，则唯一变化是

    y+θ(b−s)(u(b)−u(s)) ∈ N_(C r0)A_+。               (1)

图仍可把全部 y,b,s,φ,φ′ 相关；不能把 g 换成独立 product 或把 θ 改成 uniform。固定 φ 后由原 slab cap 积分，有真实 raw θ interval cap≤K^C max(w,r0)^γ。删除 |θ|<r0^a 的 raw 质量至多K^C r0^(aγ)，故在先定 a、η足小后可保非零 θ 的原图质量。这个删选只排零乘数，不把 planar curve 变成 line。

## 4. 为什么标量13.5不是现成二维结论

固定 θ≠0，b↦u(b)θ 可以是真二维曲线，(1) 的平移方向随 b,s 变化。R16 的 fiber 分解依赖对每个固定差标签，全部 translations 平行于一条固定直线；本分支未供给这一点。

若先投影到标量 ℓy，13.5至多推出 N_(r0)(ℓA_+)≥r0^(−1+ζ)。当 0<κ<1 时，原二维 Y 允许维数2−κ>1，标量投影满一维完全兼容。没有维数加回、共同正交fiber transport或两投影joint cap的已知结论。vector u 非affine也不保证任意固定 ℓu 非affine，例如一个坐标可线性而另一个非线性。

因此下一可检验的实际 finite 命题应直接保上述原 g、原time与angle，检验是否能逼 #A_+≥r0^(−2+ζ)（或排除 κ>ζ），并将所有 K/误差转回 original source。若只能得到一维投影满维、假设新的 K=O(1)、irreducibility、curvature 或增补共同fibers，就是未完成而非二维推广。它不是 R16 字面可再调用一次便得到的同一结论。

## 5. 新 all-s 输入的合法 affine phase 尝试

展开式是

    θ(b−s)(u(b)−u(s))
      =θ[bu(b)+su(s)−b u(s)−s u(b)]。

这四项的 cross dependence 不能通过重置原 prior 消失。一个确实 affine 的写法是以角差为时间：

    T=θ，U=(b−s)(u(b)−u(s))，V=y，X_T=V+TU。          (2)

固定平移/缩放 θ 到 [0,1] 时须同步改 U、V；base label可取(y,b,s)，仍保原 φ/φ′ 辅助标签与 g。若把 φ/φ′ 也加进决定 time 的 base，则 T 条件成为原子，不能再声 s_time>0。raw θ 只有 interval upper；是否可取大质量 all-depth双profile、对应何种 s_time 以及这次 (U,V) 的真实 jointellipse K 都待证明。dominated g 本身不补这些输入。

尤其 used H 的 κ-cover upper 给其 r0 粗 support≤K^C r0^−κ，故 θ 的粗 support≤K^C r0^−2κ。κ<1/2、η很小时，(2) 不可能免费具有 s_time=1 的条件 profile；因为这种profile在末层至少需要 r0^(−1+o(1))个time bins。不能以原 b、s 各自1-Frostman替代 θ 的条件时间。

另一形式 T=b−s、U=θ(u(b)−u(s))、V=y 也须 base 确定 U。以 u(b)=(b,b²)、|θ|和|b−s|均远离0的 raw几何作接口诊断，给 U 和 θ 即有

    b+s=U2/U1，b−s=U1/θ。

所以 fixed U-bin 与 fixed θ-bin只容 O(1) 个 T-bins（同精度，逆映射常数有界）。T 条件于 U 的粗支持仍至多 C times θ-bin 数，不能从两独立原 uniform time 偷得 condition time1。这个诊断未构造满足 dense 输出 g 的全 source 反例，只排该直接 phase 改写中的免费时间假设；不反整个 common-kernel finite 命题，也不分类所有可能 affine embeddings。

## 6. phase I 决策与下一责任

root 已先追加 working_spec§7，选择同一 common-kernel 原割线 law 的 slab 门槛与二维上限测试，再施工。以下§§7–11完整证明本轮正向门槛；不预称完整 common-kernel 排除。真正需付的是 (1) 的原图二维 expansion 或与之相配的合法 conditional-capacity bridge，包括实际 time 双profile、jointellipse K、retained原质量及物理尺度回传；不能以 (2) 的形式相似即套 Th2.2。R57固定split/slab证明不直接排此变量角色的新尝试，但其 source费用纪律仍适用。

本稿不先证明未选多个任务，不将自然 proper source 分支夸为 ordinary 五维界；完成全 common-kernel 也不解决全部 Mat2/mixed/general-to-sticky。若只回到已冻 Y-only/BSG、linewise/标量投影或增加输入公设，则按开轮门槛立即排重，不能把这些改名计新结果。正式最终 review 等 root/B/main/macro/next 全文完成后另写，Goal active。

## 7. 非零 offset 的统一 slab 上界：完整有限证明

以下独立命题不要求 u 光滑、Lipschitz 或非仿射。固定 R≥1，B⊂[−R,R]，ν 为其概率，|u|≤R。假对长度 q≥r 的任意区间 J 有 ν(J)≤K_B q，0<r≤1，K_B≥1。记

    Q(b,s)=(b−s)(u(b)−u(s))，|ℓ|=1，v(b)=ℓ·u(b)。

对 e∈(0,1]、c≠0，有

    p=Pr_(ν×ν)( |ℓ·Q−c|≤e )
      ≤ C_R K_B^(1/2)[(e/|c|)^(1/6)+r^(1/2)]。       (S1)

右侧大于1时取平凡 upper1；|c|超出 Q 的固定范围则事件为空。故只需 e/|c| 足够小。令 E(b,s) 为该对称关系，d(t)=ν{b:E(b,t)}。Cauchy–Schwarz 给

    p²≤∫d(t)²dν(t)
      =∫ ν{t:E(b1,t),E(b2,t)}dν(b1)dν(b2)。          (S2)

选择 ξ=max{r,(e/|c|)^(1/3)}，固定倍边界常数可吸入 C_R。|b1−b2|<ξ 的 anchor 对质量≤C K_B(ξ+r)。其余对若有共同 neighbor，写 w=v(t)、A=v(b1)−v(b2)，两个原式为

    (b_i−t)(v(b_i)−w)=c+ε_i，|ε_i|≤e。

相乘消 w，得到**无分母**恒等式

    A(b1−t)(b2−t)−c(b2−b1)
      =ε_1(b2−t)−ε_2(b1−t)=O_R(e)。                (S3)

若 |A|<c_R|c|ξ，则第一项在 t∈[−R,R] 的绝对值至多 |c|ξ/2，不能抵消 |c(b2−b1)|≥|c|ξ。因 e/(|c|ξ) 很小而矛盾；非小情形已由 p≤1 吸收。因此任何能有共同 neighbor 的 far anchor 对均有

    |A|≥c_R|c|ξ。

(S3) 是 leading coefficient 为 A 的二次多项式 sublevel。完成平方后，任意 monic quadratic 的 |P(t)|≤h 集合为至多两个区间，总长≤C√h：若中心值在 [−h,h] 则 |t−t0|≤√(2h)，若小于−h则两根两侧区间宽由平方根差≤C√h，若大于 h 则为空。故这里共同 neighbor 位于至多两个总长

    L≤C_R sqrt(e/(|c|ξ))

的区间，ν 质量≤C_RK_B(L+r)。代回 (S2)，

    p²≤C_R K_B[ξ+sqrt(e/(|c|ξ))+r]。

当 ξ=(e/|c|)^(1/3) 时两项同阶；当 ξ=r 时 e/|c|≤r³，第二项≤r。开平方即得 (S1)。没有假 v 单射、导数、曲率、点集二维 AD 或普通 Jacobian rank。有限 ν 的原 atom 重数全保，probability 定义直接适用。

允许任意 auxiliary 标签空间 Ω，原先验 μ=ν×ν×π，任意 0≤g≤1。非零 slab 中的原 g 质量不超过上述 raw upper。g 可以把所有变量相关；这里只用 domination，没有按 g 再假 B 独立。

## 8. 直接 θQ 版本与 near-zero 的保原 g 提取

进一步令 θ=θ(ω) 有界，原 π 与原 B² 独立；这是 actual angle 先验与原 time 两坐标的关系，g 仍可任意相关。置 D=θQ。对 θ≠0，D 的 (e,c) 测试是 Q 的 (e/|θ|,c/θ) 测试，比值仍为 e/|c|。θ=0 对 |c|>e 无贡献。因此 (S1) 原样适用于

    ∫g 1_{|ℓ·D−c|≤e}dμ，c≠0，                    (S4)

不额外付 θ 下界，也没有在保留 g 后重新假 θ 独立。若原 θ 本已依赖 b,s，这个 raw-product 推导则须另证；本文不扩张该量词。

近零 offset 需要真正保图。固定 0<a<1、r≤e≤1，|c|≤e^a。设 π{|θ|≤q}≤K_θ q^γ 对 q≥r，γ>0。假原 slab graph 质量

    σ=∫g 1_{|ℓ·D−c|≤e}dμ
      ≥ C_R[K_θ e^(aγ/4)+K_B e^(a/4)]。              (S5)

先删 |θ|<e^(a/4) 的原事件，再删 |b−s|<e^(a/4)；两次损失至多右侧两个收费项的小固定比例，保至少 σ/2。两查询宽度≥r，不问 source floor 以下的 cap。余 tuple 有

    |v(b)−v(s)|≤2e^(a/2)。                           (S6)

令 h=4e^(a/2)，将 v 的 bounded range 分为半开 h-intervals I_k，取双邻格 J_k=I_k∪I_(k+1)，B_k={b:v(b)∈J_k}。每个满足 (S6) 的时间对被至少一个 B_k×B_k 包住，每个 b 属于至多两个 B_k。令

    P_k=ν(B_k)，
    H_k=∫g 1_(retained slab) 1_(b,s∈B_k)dμ。

于是 ΣP_k≤2，ΣH_k≥σ/2，且 H_k≤P_k²（原 auxiliary 概率≤1，g≤1）。故存在 k 满足 H_k≥cσP_k，继而

    P_k≥cσ， H_k≥cσ²， H_k/P_k²≥cσ。               (S7)

最后一项是只将两个原 time 坐标条件到同一个 B_k 后的真实 graph density；不是重新造 independent g。保留原 auxiliary 标签、权重、输出 A_+ 和 (1) 中全部事件。同时

    u(B_k) ⊂ {x:|ℓ·x−d_k|≤C e^(a/2)}，
    ν_(B_k)(J)≤C K_B σ^−1|J|（|J|≥r）。             (S8)

两个 time 坐标在同一原时间片；没有挑两个不相干的子集。对 Q 本身，可不删 θ，只删 |b−s|<e^(a/2)，所需损失≤C K_B e^(a/2)，余下 (S6)–(S8) 一样成立。

对 normalized g law 若总质量 m，测试概率 p 对应 σ=mp；结论保的是**原绝对**质量≥c(mp)²，不能误写成 cp² 或免费保 m。所有原 angular/point 的 multiplicities 都在 π 中积分。若还要保持每管或每 label 的原 marks 下界，需另作原 heavy-fiber 重收；(S7) 自身只给 incidence 平均质量。

## 9. source 参数及 near-line 回传的真实责任

取 e=r^d，fixed 0<d<1、0<a<1，K_B,K_θ≤r^−h。若目标 σ≥r^h，则 (S5) 在

    d a min(γ,1)/4 > 2h

并留固定余量后对 r 小成立。非零 |c|≥e^a 时 (S1) ≤C r^(−h/2)[r^(d(1−a)/6)+r^(1/2)]；先定 d,a,γ，再让 h 足小，使它比原 graph mass 的所需小 power 更小。这明确使用原 K 与 σ 的分母，不把 subpower 当 O(1)。估计对所有单位 ℓ、所有 offset c 一致。

这只能给一个带 near-line alternative 的 slab 不集中门槛，**没有给二维 Frostman**。若 weighted D-law 某 nearzero slab 承载原质量 σ，则 (S7) 提供保同 g 的时间片；若要禁止这 alternative，必须真实排除那个原片，不能先假 u 的全 time range 不共线即可。

尤其 (S8) 的像离直线误差为 e^(a/2)。当 e=r^d、d<1 时，该误差远大于原 O(r)。把 u 投影到直线后，对 D 的误差为 O_R(e^(a/2))；不能仍以原 r 调用 R16 的 exact-linewise theorem。需 coarsen 到 r′至少此量级，重付 F/time oscillation、Y 的原 AD packing+KT、g heavy quotient、all-real SM 的精度与质量。R16 已有 coarsening 技术并不自动认证这次参数。本文明确停在 (S7)–(S8)，不宣称该 near-line case 已被实际原管配置排除。

## 10. ellipse 输入与 θ-clock 强度：不同于二维 Frostman 的责任

二维 Frostman 不是 ellipse capacity 的必要条件，不能因 root 的二维预处理反攻就声所有新 source 接口失败。例如，若原独立 Y 与 Q 的概率确有 all-scale estimates

    Pr(Y∈E)≤K L^(1−γ_T)w^(1−κ+γ_T)，
    Pr(Q∈E)≤K w^β，β≥κ，

则乘积律的 joint ellipse mass 除 W_(κcap)(E) 至多

    K² L^(−γ_T−κcap)w^(γ_T+β−κ+κcap)
      ≤K² L^(β−κ)≤K²。

第一式可由原 α=2−κ AD fine-ball upper、full-Y packing 与 tube KT 推出；对 arbitrary clipped 支持必须保其真实归一分母。第二式是 all-scale，而本轮 (S1)/(S8) 只给特定粗精度的 alternative，不自动供给它。原 g 下条件化也可能将该 product 输入多付 m^−1；不能忽略。

即便这些 initial ellipse 费用理想，(2) 的 θ-clock 仍有独立强度门槛。记原整体 θ 支持的 r-bin 数为 r^(−t_θ)，有 t_θ≤min(1,2κ)+O(h)。任何实际 conditional time 双profile 的指数 s_θ≤t_θ+O(h)，但两者不能免费视为相等。source本次保证任意严格 q<1+2s_θ−10κcap，不是最优 q upper。原输出落于整体 time-support×N_r A_+，其 covering upper 至多 r^(−t_θ−2+κ−O(h))。仅用这个 covering upper 与 guaranteed q 作矛盾，需

    1+2s_θ−10κcap > t_θ+2−κ+O(h)，

因 t_θ≥s_θ−O(h)，必要条件是

    s_θ+κ > 1+10κcap+O(h)。

故 κ<1/3 时，即使 s_θ达到最乐观2κ、K理想，此直接 θ-clock 调用也不足以排到任意小 κ。这只审查所写 phase 与所保证指数；不排更强 source、其它 variables 或真正 joint g 方法。它也不以二维 Frostman 的假必要性结论代替这项时间账本。

## 11. 当前完成范围与等待独审

本轮新增、已完整证明的是 (S1) 非零 offset uniform upper、(S4) 对原 θQ 的 extension，以及 (S5)–(S8) nearzero 保原 g 的同 time 片提取。它们对全部 bounded u、原 interval-Frostman time law和任意 dominated g 成立，不是一次 Jacobian 检查或只求 canonical union。

更强二维 Frostman 预处理的 strict counter 由 root/B 独立开发，须实际全文读其 final 后正式审。本文未预认证该 counter、完整 common-kernel、source四维/五维定理或新颖重大；不新增数学ID。选定主任务之后不继续第二候选、G3、R57 包络或旧 BSG/action 微调。最终 root/B/macro/next 全文实际读后在 assigned formal6另记，通过范围保留未经外部同行评审，Goal active。
