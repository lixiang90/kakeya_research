# R0021：mixed32 的原路径质量、向量 cubic 与条件回传

2026-10-17，`audit_four_dimensional`。已读 AGENTS/GOAL/STATE/ROADMAP/registry、R21 macro/spec、R20 handoff，以及本库 WZ arXiv:2609.22035v1 Definitions17.2–17.4、§19.2–19.5、§21.1、§22.1、§22.4 的相关原文。

**结论范围：** 若本轮修订有限 PCT 成立，并保留第1节明确列出的 named 固定尺度 affine/nondegeneracy 与 Lemma19.4 输入，则实际 d5/k3/ℓ2 的向量 quadratic alternative 可按本文链条条件排除 κ>ζ。没有由原 all-scale 声明免费获得该 affine 输入，没有独立重证全部 source，也没有解决完整五维 Kakeya或声称重大结果。

## 1. 原数据、量词与高级依赖

源仍是完整原配置：T 的 joint 参数 AD4、whole-tube CW≤δ⁻η；共同 δ-separated Z；原点/管 witnesses；Φ/ξ coherence；两套 grain；κ、γ 固定，κ>ζ>0 的反证范围。mixed32 中

    f=(u,v), u:Z→R, v:Z→R²;
    tilde f=(a,b), a,b:Z→R²;
    v=a+bu,
    α=2−κ, horizontal dimension=2.

每个原 tildeY_z⊂R² 为 (δ,2−κ,δ⁻η)-AD，且 Def17.4(4) 另给 **tube-KT 指数 1−γ**。该项是实际新增几何，不能由 AD 维数2−κ替代。原 global ℓ-grain 的 Y⊂R³与 tildeY 不是同一对象；本文用后者作 PCT 载体。

高级输入须分别列出：

1. **固定尺度 affine alternative：** 在原 allowed `ρ∈[δ^(1/4),δ^µ]`，有全局原 density≥δ^(θ_aff) 的 retained times，每个 retained ρ-window 上有 `(r,s)∈R×R²`，使整个 f 的 affine error≤ρ^(1+ε₀)。
2. **whole affine velocity 非退化：** 可保 `K⁻¹≤|(r,s)|≤K`；下界的 source 责任是原19.2/CW及合法删除 low-speed windows。它不预设 |r| 下界。
3. **原 tilde f 的本尺度 Lipschitz upper：** 保留原19.5支付后的 `osc_J tilde f≤Kρ`，f 的 dyadic upper 来自 Def17.2。
4. **Lemma19.4 的一般维数结论：** 整个 tilde f 在一个原ρ-window中有足够 dense 的 σ-cluster，`ρ∈[δ^(1/3),1]、σ∈[ρ²,ρ]` 时，`C_CW≥δ^(C(η+ε_den)/γ)(ρ/σ)^κ`。

原 Lemma21.1(pp.90–93，文本4751–4916行) 的印刷非集中声明量化所有 allowed scales。其形式否定只给某窗口的 fit，不能自动给第1项。原 proof 固定任意尺度所需的窗口 averaging/localization 仍须单列审查或条件化。本文不以该印刷声明的逻辑否定代替第1项。Lemma19.2/19.4 与 scalar ABC 的完整证明未在本项目独立重证；source 的 scalar multiplier输入在 ℓ=2 的任意 d 声明，不是 vector-Φ 定理。

以下 K、K_γ 均为 δ 的明确小幂：K=δ⁻Cϑ，ϑ含 η、θ_aff、题设 quadratic retained density、19.5删选和当前稳定化 η_j。固定 κ,γ,ζ,µ,ε₀ 后选 `0<ε≤ε₀/2`；所有 ϑ 再足够小，最后 δ 小。PCT 的 `2/γ` 幂与 fixed `(C_D,m)^(2/γ)` 不隐去：γ先固定，令 K_γ=δ^(−C_γϑ)，C_γ 可依 γ,κ；δ阈值亦可依 γ与全部 fixed constants。

## 2. 原 V/J/L 质量：horizontal2 与 vectorY 的实际计数

精确原文入口：§22.1，pp.93–96，4923–5072行；V 为(175)，J为(178)，L为Lemma22.1，向量关系为(176)/(180)。这些定义和矩阵恒等式已在任意 d,k,ℓ 声明，但原省略计数不能靠逐管独立 dense marks补齐。

对当前 retained times 作 R16/R19 的原 incidence、cross-time covering 选择合法 good-q，记 `m=#Z(q),e=#E(q)`：

    m≥K⁻¹ρ/δ,
    e≈K^(±1)m(ρ/δ)^(4−κ),
    #T(q)≤Kρ⁻κ(ρ/δ)^4,
    deg(p)≈K^(±1)δ⁻κ.                       (1)

不能对任意 q 作此 lower。每个 fine Φ_p-bin 选一个实际原 witness，O(1) 碰撞；选后 ambient AD upper 保留，不给所选 T 新 AD lower。

设 d_T 为 q 内原 marked degree，I=Σd_T≈K^(±1)eδ⁻κ；于是 `R_arm=Σd_T²≥I²/#T(q)≥K⁻¹eδ⁻κm`。令 `B_p=Σ_(T∈T_p)d_T`，其总和为 R_arm。按 `(p,z')` 对 one-arm 作 CS 得原 V lower `K⁻¹eδ⁻²κm`。

中间 k-grain 总数≤`Km(ρ/δ)^α`；J 的原权精确为 `Σ_grain(Σ_(p∈grain)B_p)²`。所以

    J≥K⁻¹eδ⁻²κm²(ρ/δ)^2.                   (2)

这里使用平均，未要求每个被 q 截出的二维 X 都 locally dense。

记向量

    E(z,z')=v(z)−v(z')−b(z')(u(z)−u(z')).

若 `|E(z,z')|≤cτ/ρ`，(176) 使同一原起点两 arm 的 vector y 标签相距 O(τ)。按 `(p,z',z'',x̃_τ,terminal θ_τ)` 编码，签名数≤`K e m²(ρ/τ)^2τ⁻κ`：两中间点因 x̃、y 均近而 physically τ-close，故可用原 ξ/Φ coherence。若 τ 非允许尺度，取相邻 allowed scale并细分 coarse bins，损失只是 δ^(-Oη)，显式计入 K。再次 CS 得

    L≥K⁻¹eF_Lm²,
    F_L=δ⁻⁴κτ^κ(ρ/δ)^2(τ/δ)^2.              (3)

此填入Lemma22.1的省略质量证明，不逐管假设其余终层恰有 m 选择。

## 3. vector-Y graph 的 code 恢复与真实误差

固定末层 z''，code 为 `(y,z,z',φ₁_ρ,φ₂_ρ)`，y 是实际二维 tildeY 的 fine δ-cell。给定 code：第一终端 horizontal x 有至多 `(ρ/δ)^2` 选择；原末管 T₁' 至多 `Kδ⁻κ`；其 z'交点确定；第一被平移点的原同-grain 中间点 x 有 `(ρ/δ)^2` 选择；两 initial管各在相应 coarse φ-bin 中有 `K(ρ/δ)^κ` 选择；第二平移中间点 horizontal x 限于 τ-bin有 `(τ/δ)^2` 选择；末管T₂'的 τ-close 选择≤`K(τ/δ)^κ`。故

    M_code≤K F_Lρ^(2κ)(ρ/δ)^2.               (4)

使用 (1)、(3)、每层 `#tildeY_z''(q)≤K(ρ/δ)^α` 与 `#Φ_q≈K^(±1)ρ⁻κ`，对 z''平均可得 `0≤g≤1`、在同一个 `tildeY_z''(q)×Z(q)²×Φ_q²` frame 中 density≥K⁻¹。这是原路径 fibre 除以(4)，没有把原输出 endpoints 或时间改成独立 samples。标量 Φ_q 的 κ-AD 直接给整个coarse carrier的interval cap；不需要 vector-Φ 分支的另一次 slab-heavy选择。

每条正权原路径满足

    y_out=y+(z'−z)E(z,z')(φ₁−φ₂)+O(Kτρ+δ).   (5)

fine φ 换ρ-bin额外误差也≤Cτρ。所有输出可以多值，但逐条均在该邻域。同 code fibre 重数已由(4)支付。取相反顺序的角差 `ψ=φ₂−φ₁` 后，下节 polynomial 使用正 `(z−z')²`；这是标签互换，不改原质量，也避免原(180)/(182)不同书写符号被混用。

原 Φ 的κ-AD与原time packing、(1)，允许从同 g 中删除 `|ψ|<K⁻C` 或 `|z−z'|<K⁻Cρ` 的小reference质量，仍留K⁻C原质量。对正比例的 z'，再固定实际 y和angle pair，可保 `≥K⁻C m` 个 z。因 g≤1，此 averaging 是原 fine-time cardinal，不是任意 coarse distinct image 的密度。

## 4. 向量 quadratic 的初始系数控制

轴调整 `h=v−b(z₀)u`，令 `c(z)=b(z)−b(z₀)`。题设在原 retained times 上有

    h(z)=A₀+A₁(z−z₀)+A₂(z−z₀)²+O(Δ),
    A_i∈R²,
    Δ=ρ^ε(ρ²+ρ|A₁|+ρ²|A₂|).                  (6)

原 h 的振荡≤Kρ；去常值后，ρ-window 上 vector quadratic 在 K⁻C-density times 上范数≤Kρ+Δ。可选三个相互间隔≥K⁻Cρ的原 times，逐坐标 quadratic interpolation gives

    ρ|A₁|+ρ²|A₂|≤K(ρ+Δ).

这里样本数 m≥K⁻Cρ/δ→∞，不是忽略有限 sample 边界。把该式代入 Δ，因 `Kρ^ε≪1` 可吸收得

    Δ≤Kρ^(1+ε),
    ρ|A₁|+ρ²|A₂|≤Kρ.                        (7)

affine fit、`osc c≤Kρ` 给 `|c(z')r|≤Kρ`，且原 E Lipschitz upper 给 `τ≈max(δ,Cρ max|E|)≤Kρ²`。这一步无需先假设 τ 已很小。

## 5. PCT 的 physical tube-KT 尺度可直接使用

将 f 的 affine approximation 和(6)代入(5)，得到 fixed y,z',ψ 的 actual vector cubic

    P(z)=(z−z')²[A₁+A₂(z+z'−2z₀)−c(z')r]ψ,
    y+P(z)∈N_e tildeY_z''(q),
    e=C K(τρ+δ+ρΔ).                          (8)

`Kρ^(3+ε₀)` 这项拟合误差由 `ρΔ≥ρ^(3+ε)` 吸收（ε≤ε₀/2，ϑ后取）。z-window归一到[0,1]，fine spacing `d₀=δ/ρ`，原 fiber B 有 `#B≥θ/d₀, θ≥K⁻C`。原 polynomial 的全window振幅 R 由(7)满足 `R≤Kρ²≤1`；于是

    d₀R≤Kδρ≤δ≤e.                            (9)

这是实际验证PCT的离散尺度条件，不靠重新定义误差。δ小后 e≤1；若某粗情形e≥1，则R≤1已给平凡R≤e，不影响后文。

**不需要将 tildeY 空间除以ρ。** 它是原 R² 载体的子集；平移减y只改fixed support box。Def17.3、17.4原tube-KT对全部 `δ≤e'≤L≤1` 方向tubes成立，e≥δ使PCT要求的全部查询直接可用，K_TKT≤δ⁻η。q子集继承 upper，不给它 AD lower；固定support变换和tube邻域只付 fixed/K 常数。不能只用 α=2−κ 的 AD 去声称曲线不可能。

按本轮修订PCT，正确常数结构是

    R/e≤(C_(D,m) K_TKT θ⁻C_(D,m))^(2/γ),

其中 fixed constant 在 `2/γ` 幂内；原幂外 constant 若要求uniformγ并不等价。此处 D=3,m=2，γ先固定后令ϑ小，故

    R≤K_γ(τρ+δ+ρΔ).                          (10)

本稿此式条件于root的PCT有限证明及独审通过，不把尚待审的有限引理暗中算成source既有结果。

## 6. vector 系数恢复与原 τ 稳定化

因 P(z')=0，`sup_J|P|≤R`。归一z-coordinate后，cubic最高次系数为 `ρ³A₂ψ`；二次项再恢复 `ρ²(A₁−c(z')r)ψ`，逆系数norm一致有界，z'在unitwindow中。用 |ψ|≥K⁻C 和(10)得

    |A₂|≤K_γ(τ/ρ²+δ/ρ³+Δ/ρ²),
    |A₁−c(z')r|≤K_γ(τ/ρ+δ/ρ²+Δ/ρ).           (11)

向量各坐标使用同一个 z'、y、ψ、B；没有分别选坐标世界。对 K⁻C比例的 z' 有此结论。由(11)代回其余 retained z的E表达式，即

    ρ|E(z,z')|≤K_γ(ρτ+δ+ρΔ).                 (12)

不需先由 r 除法恢复 b。

以原 global retained Z 为母集，按 source22.4运行有限 η_j 稳定化，起点包含全部既有density预算。各ρ-window分别选择第3节的合法good-q和这些good z'，再取原times的并；每window只损K_γ固定幂，全局仍如此。选一个窗口后不能冒充全局retained density。对τ_j作最小化和dyadic层选择，若全部τ_j>ρ^(3+ε/2)，可取相邻j满足 `τ_(j+1)≥ρ^(ε/10)τ_j`，且good z'并足为下一集候选。由(12)得

    τ≤K_γρ^(−ε/10)(δ+ρΔ).

由(11)及 `|c r|≤Kρ` 又有 `Δ≤K_γρ^ε(ρ²+τ+δ/ρ)`。按ϑ≪µε/C_γ和ρ≥δ^(1/4)吸收，得

    τ≤ρ^(3+ε/2).                             (13)

若某τ_j本已满足就直接选它。有限 j 的个数先依ε固定，初始η_j小到所有j的K_γ均可支付。此与R19 scalar-Y稳定化不同之处仅在(10)的真实tube-KT输入与其γ费用，不能省略该新费用。

## 7. scalar r 的合法非退化、整列 b 慢变和19.4

在(13)后的原times中取 |z−z'|≥K⁻Cρ。由原 affine fit，

    E(z,z')=(s−b(z')r)(z−z')+O(Kρ^(1+ε₀)),
    |s|≤C|r|+K[τ/ρ²+ρ^ε₀].                  (14)

其中s∈R²。结合 named `|(r,s)|≥K⁻¹`，误差在ϑ后取时更小，故 `|r|≥K⁻C`。没有由whole velocity非零直接推r非零。

精确 E+swap 为

    E(z,z')+E(z',z)=(b(z)−b(z'))(u(z)−u(z')).

以 `u(z)−u(z')=r(z−z')+O(ρ^(1+ε₀))` 及 `osc b≤Kρ`，对分离 pair 得

    |(b(z)−b(z'))r|≤K_γ[τ/ρ²+ρ^(1+ε₀)].

对近 pair用一个共同远anchor（原time packing与m lower保证存在），以两次此式连接。因r是**标量**且已有下界，整列而非仅一个投影满足

    osc_J b≤K_γρ^(1+ε/2).                    (15)

不再作新轴变换；在原有界坐标中，consistency 精确给

    a(z)−a(z')=E(z,z')+[b(z')−b(z)]u(z).

原 u 有界、`|E|≤τ/ρ` 与(13)、(15)直接推出 `osc a≤K_γρ^(1+ε/2)`。它和 b 使用同一原retained簇。终步只需这个保守指数，不需另声称 a 的ρ²强化，也不引入新坐标系下CW/图表的费用。

取 `σ=ρ^(1+ε/4)`，ϑ足够小吸收K_γ，得整个 tilde f 的osc≤σ。`ρ≥δ^(1/4)≥δ^(1/3)`且`ρ²≤σ≤ρ`。某原窗口有 `≥K_γ⁻Cρ/δ` 个goodtimes，而原Z在该窗口至多Cρ/δ，因此原Lemma19.4的cluster density≥δ^(C_γϑ)。可直接对原配置及这个local cluster调用，无需将选中family重新声明AD。结果为

    C_CW(T)≥δ^(C_γϑ/γ)ρ^(−κε/4).

ϑ≪µζεγ/C_γ、η同时小后，与C_CW≤δ⁻η矛盾，故条件排除κ>ζ。

## 8. 条件结论与尚未解决的部分

链条完整保留原V/J/L权重、同一vector cubic、physical tube-KT尺度、有限PCTγ费用、非零scalar r证明、保守(15)和19.4参数。没有调用原PDF99未获支持的ρ^(2+ε/2)强化，也没有把vectorΦ的矩阵问题变回scalar multiplier。

**本稿的branch结论明确条件于：** 本轮修订PCT通过；named fixed-scale全局affine alternative及whole-velocity非退化确实取得；原19.4一般维度结论及其原配置适用合法。它不是这些高级输入的完整独立证明，不是整个mixed32（非二次仍未处理），不覆盖其他五维分支/general-to-sticky/Hausdorff，亦无重大性或新颖性认证。若任一named localization未支付，只登记本条件应用，不能将完整主分支写成无条件已解。
