# R0019：实际 mixed (4,2) 二次分支的源与原质量审计

2026-10-17，`audit_four_dimensional`。读了 AGENTS、GOAL、STATE、ROADMAP、registry、本轮 spec 和 R18 handoff。对象为 WZ arXiv:2609.22035v1 的实际 `d=5,k=4,ℓ=2` 配置；不是任意 slope 数据的形式推广。**没有解决整个 mixed 二次分支或 Kakeya。** 本稿给原 V/J/L 权重恢复、可保留的标量二次压缩、r 非退化的合法推导，以及原 PDF99 一个可保守修复的算式断点。named source 的完整高级输入仍列依赖。

## 1. 读到的准确源范围

本库 `literature/extracted/wang_zakharov_2026_sticky.txt` 行号按 `split('\n')`，不按会额外拆 form-feed 的 `splitlines()`。

| 源位置 | 页码、行号 | 实际范围 |
| --- | --- | --- |
| Definitions17.2–17.4 | pp.65–66，3362–3434 | 原管联合参数 AD；两套 grains；原 ξ、Φ 的 dyadic coherence；consistency |
| Lemma19.2 | pp.78–80，4124–4241 | 任意 d,k,ℓ；整个 f 的慢变给 CW 下界；不是任意一个分量慢变 |
| Lemma19.4 | pp.81–82，4244–4330 | 任意 d,k,ℓ；整个 tilde f 在一个原窗口浓集给 CW 下界 |
| Lemma19.5 | pp.82–83，4331–4370 及后文 | retained times 上两 slope 的 Lipschitz upper；没有次 Lipschitz 收缩 |
| Lemma21.1、Theorem21.2 | pp.90–93，4751–4916 | ℓ=2、任意 d；scalar multiplier Φ；A/B 可高维，未变 vector multiplier |
| §22.1 | pp.93–96，4923–5072 | 任意 d,k,ℓ 的 V/J/L 定义、(174)–(183)；有省略的质量/重数步骤 |
| §22.3–22.4 | pp.96–99，5093–5268 | 二次排除本身只声明 d4/k3/ℓ2；(184)–(195) |

已把 PDF98、99 原页渲染到 ignored `tmp/pdfs/R0019/WZ-098.png`、`WZ-099.png` 并目视核版，特别核了 (189)、(190)、(192)、(195) 和其后两行；第7节的问题不是文本提取错误。没有下载新文献，没有重证整篇或 Lemma19.2/19.4 的全部 neighborhood-to-CW 证明。

## 2. 全部原假设与不免费的操作

写

    f=(u,v), u∈R², v∈R;
    tilde f=(a,b), a∈R, b∈Mat(1,2);
    v=a+bu, α=1−κ, D=4−κ=3+α.

原 k-grain 是三维水平 x，标量 Y 的 AD 维数 α；原 Φ 为标量，维数 κ。原 global ℓ-grain 则是一维水平 grain、三维 Y，不能混同这两套 Y。Def17.4 给每个完整三维 grain 的全局 dense X，但不保证任意空间 ρ-cube 内每个被截 grain 都 dense。Def17.2 的跨时间 Y-union 正则性直接给的是原 ℓ-grain 的 Y；不能擅自把它也赋给 tilde Y。

每个 fine Φ_p-bin 只取一个原管 witness，O(1) 碰撞；所有管仍来自原 T，故其联合参数 AD upper 可用，不把选出的管族重新声明 AD lower。删时间保持原 X 与 Y；删局部点/管不产生新完整配置。K 表示 `δ^(−Cϑ)`，ϑ 必须包含 η、原 affine alternative 的 retained density、题设 tildeη、当前稳定化 η_j 等**所有**损失预算；不同固定次幂允许改变 C。取 η_j 序列可从这些预算的最大值开始，而不能把 `δ^tildeη` 免费藏进独立的 `δ^(Oη_j)`。

固定 allowed `ρ∈[δ^(1/4),δ^µ]`，固定 κ>0；常数可依 κ。先固定 ε、ε₀、µ 等，再把全部 ϑ 取小，最后 δ 小。下文所有 K 费用均须实际支付。

## 3. 原 V/J/L 质量：水平三维没有消失，也不需逐管独立密度

在 retained times 的原窗口，沿 R16 的原 incidence/cross-time covering 选择合法 good-q，记 `m=#Z(q), e=#E(q)`。这里只用原 ℓ-grain 的跨时间 covering 作 spatial averaging，得到

    m≥K⁻¹ρ/δ,  e≥K⁻¹m(ρ/δ)^D,
    #T(q)≤Kρ⁻κ(ρ/δ)^4,  deg(p)≈K^(±1)δ⁻κ.       (1)

不是对任意 q 作此断言。给每个原 witness 管 T 记 `d_T=#(E(q)∩Y(T))`，每管每个 time 有 O(1) 个点。原 incidence `I=Σd_T≈K^(±1)eδ⁻κ`。Cauchy–Schwarz 给

    R=Σ_Td_T²≥I²/#T(q)≥K⁻¹eδ⁻κm.

再记 `B_p=Σ_(T∈T_p)d_T`。原 V 数为 `Σ_(p,z')` 同一终层的两 arm 数平方；按 `(p,z')` 作 CS，得 `V≥K⁻¹eδ⁻²κm`，与 (175) 同阶。这里没有说每条管恰好有 m 个 marks。

原 J 的中间两点必须在同一实际 k-grain，故精确计数为

    J=Σ_(中间grain g) (Σ_(p∈g)B_p)².

局部每层 tilde Y 的 AD upper 给 grain 数 `≤Km(ρ/δ)^α`。因此

    J≥R²/[Km(ρ/δ)^α]
     ≥K⁻¹eδ⁻²κm²(ρ/δ)^3.                       (2)

这正是 (178) 的 horizontal-three 因子；由原平均得到，不要求每个局部 grain 的 X lower。

令

    E(z,z')=v(z)−v(z')−b(z')(u(z)−u(z')).

若所有所用 times 满足 `|E(z,z')|≤cτ/ρ`，原 (176) 使同起点、同中层的两 arm 的 y 标签相距 O(τ)。将 J 按

    (原起点 p, z', z'', 中间 x̃ 的 τ-bin, 末管方向的 τ-bin)

编码。给定前三项与 x̃-bin，所有相关中间点在 O(τ) physical cube，原 ξ/Φ coherence 给末方向只需 `Kτ⁻κ` 个 bins；横向 x̃-bin 数 `(ρ/τ)^3`。签名总数至多

    K e m²(ρ/τ)^3τ⁻κ.

签名 CS 及 (2) 得

    L≥K⁻¹eF_Lm²,
    F_L=δ⁻⁴κτ^κ(ρ/δ)^3(τ/δ)^3.                 (3)

这填入源 Lemma22.1 的省略 CS；source line5025 的“选剩余点约 m 种”不能逐管直接使用，原平均/signature 论证避免了该额外假设。对应 upper 可逐个选原对象，仍同阶 K。

## 4. 从原 L 到 scalar-Y graph 的重数表

固定终层 z''，code 为 `(y,z,z',φ₁_ρ,φ₂_ρ)`，其中 y 是第一终端原 grain 的 fine 标量标签。保留全部原 y，并不免费固定一个精确 grain。给定 code 的恢复 upper 为：第一终端 x 至多 `(ρ/δ)^3`；T₁' 至多 `Kδ⁻κ`；其 z' 交点确定到 O(1)；第一原中间点在相同 k-grain，至多 `K(ρ/δ)^3`；两条初始管各至多 `K(ρ/δ)^κ`；第二平移中间点的 x 限在 τ-bin，至多 `K(τ/δ)^3`；末管 T₂' 的 τ-close 选择至多 `K(τ/δ)^κ`，其终点 O(1)。故每个 code fibre 至多

    M_code=K F_L ρ^(2κ)(ρ/δ)^3.                 (4)

对所有终层计数，再用 (1)、(3)、`#Y_z''(q)≤K(ρ/δ)^α` 和合法的 coarse H 大小 `≈K^(±1)ρ⁻κ`，可选一个终层得到 `0≤g≤1`，其在 `Y_z''(q)×Z(q)²×H²` 原参考 frame 的密度 `≥K⁻¹`。同 code 可有多个输出，但每个原路径均满足同一个误差关系。这里可直接取原 coarse `H=Φ_q`：在本分支 Φ 标量，Def17.2 给整个 Φ_q 的 κ-AD，已支付 normalized interval cap `K t^κ`。不需要像 vector-Φ 分支那样另外从原 incidence 作 slab-heavy 选择；不能只凭包含关系推出此 cap，但本分支确有独立的 scalar AD 输入。

原 (180) 给

    y_out=y+(z'−z)E(z,z')(φ₁−φ₂)+O(Kτρ+δ).      (5)

将 fine φ 换成 ρ-bin 的额外误差也只有 `O(τρ)`，因为 `|E|≤τ/ρ`。所以 (181)–(183) 在 matrix-row mixed42 仍为真正 scalar Y graph；没有把 b 的剩余分量从这个 code 中恢复出来。times 仍是原 fine times，未把 δ/ρ-spacing 误写成 ρ-spacing。

## 5. 二次压缩到 τ≤ρ^(3+cε) 不需要整 row 恢复

本节条件是 handoff 中明确保留的固定尺度 affine alternative，以及上述实际原 graph；并保留源中 elementary bounded-degree polynomial/Remez 输入。写 `u(z)−u(z')=r(z−z')+O(ρ^(1+ε₀))`、`v(z)−v(z')=s(z−z')+O(ρ^(1+ε₀))`。轴调整 `h=v−b(z₀)u`、`c(z)=b(z)−b(z₀)` 后

    E(z,z')=(z−z')[A₁+A₂(z+z'−2z₀)−c(z')r]+O(Δ),
    Δ=ρ^ε(ρ²+ρ|A₁|+ρ²|A₂|).                  (6)

原 Lipschitz 与 affine upper 给 `|c(z')r|≤Kρ`。对 (5) 用原 g averaging 固定 y,z',φ₁,φ₂，可保 `≥K⁻¹m` 个 z，且时间 gap≥K⁻¹ρ、`|φ₁−φ₂|≥K⁻¹`。其 polynomial

    P(z)=(z−z')²[A₁+A₂(z+z'−2z₀)−c(z')r](φ₁−φ₂)

落在 scalar α-AD Y 的 `e_tol=K(τρ+δ+ρΔ)` 邻域。对次数≤3的 polynomial，dense-time image 与 AD upper 给 `osc_JP≤K e_tol`；这里只需 AD upper，未给所选 Y patch 新 AD lower。一个直接理由是：Remez 控制 derivative 小值区，从原 θ-dense time 邻域中保 θ/2 测度且 derivative≥θ^C osc(P)/ρ 的部分；其像测度≥θ^C osc(P)。反过来，AD upper 把该像压在 ≤K osc(P)^α e_tol^(1−α) 的测度内，故得所述界。δ-time 变为小区间的误差用 Markov/Remez 和 `|P|≤Kτ` 控制为 Kδ，已包含于 e_tol。

固定次数的系数范数等价遂给源 (189)、(190) 的**收缩版本**

    |A₂|≤K(τ/ρ²+δ/ρ³+Δ/ρ²),
    |A₁−c(z')r|≤K(τ/ρ+δ/ρ²+Δ/ρ).             (7)

对至少 K⁻¹m 个原 z' 有此结论。并不需要由第二式恢复 c 整行；由 (7) 可直接把其余任意 retained z 代回 (6)，得

    ρ|E(z,z')|≤K(ρτ+δ+ρΔ).                   (8)

对每个窗口分别做原质量 averaging，取这些 good z' 的并，所得仍为全局 K-density 的候选下一时间集；不能只取单个窗口后称全局 subpower density。τ 的最小化/稳定化以有限 η_j 预算运行，若所有 τ_j>ρ^(3+ε/2)，可取 `τ_(j+1)≥ρ^(ε/10)τ_j`。用 (8) 及下一时间集的合法原质量得

    τ≤Kρ^(−ε/10)(δ+ρΔ).

又由 (7)、`|c r|≤Kρ` 得 `Δ≤Kρ^ε(ρ²+τ+δ/ρ)`。吸收后 `τ≤ρ^(3+ε/2)`，因为 `ρ≥δ^(1/4)`、ε 小且 K 预算后取。若某 τ_j 本来已低于该界则直接选择该 j。τ 可取 `max(Cρ max|E|,δ)`，δ 项同样被该 upper 包含。

**实际进展边界：** 这部分 scalar-Y polynomial 压缩不依赖 c 是标量，在 mixed42 可保留；它把原数据归约到 E 很小，尚没有压缩 b 的正交分量。外部 Lemma21.1/高级 scalar ABC 和完整 Lemma19.2/19.4 仍为 named source 依赖，未全文独立重证。

## 6. r=0 和幂小 r 可排除；剩余恰一个标量 row 分量

保留源非退化 affine alternative `|(r,s)|≥K⁻¹`，而非擅自先假设 |r| 下界。压缩后的原 times 有 span≥K⁻¹ρ。对一对分离 times，由 affine approximation 与 `|E|≤τ/ρ` 得

    E(z,z')=(s−b(z')r)(z−z')+O(Kρ^(1+ε₀)),
    |s|≤C|r|+K[τ/ρ²+ρ^ε₀].                  (9)

η预算足够小使右侧误差比 K⁻¹ 小；结合 `|(r,s)|≥K⁻¹` 严格推出 `|r|≥K⁻C`。所以 r=0 及 fixed-power 小 r 已不可能；不从 |(r,s)|≠0 直接偷推 |r|≠0。

利用精确恒等式

    E(z,z')+E(z',z)=(b(z)−b(z'))(u(z)−u(z'))

以及 `osc b≤Kρ`、u 的 affine approximation，任意 gap≥K⁻¹ρ 的 pair 满足

    |(b(z)−b(z'))r|
      ≤K[τ/ρ²+ρ^(1+ε₀)]≤Kρ^(1+ε/2).          (10)

近 pair 可借同一个远 anchor：原 m≥K⁻¹ρ/δ 和 δ-packing 确保两个长 cK⁻¹ρ 的短区间外还有原 time，故以两次 (10) 得全 pair bound，原权不重置。

轴对齐 `u(z₀)=b(z₀)=0` 后，由 `h(z)−h(z')=E(z,z')+c(z')(u(z)−u(z'))` 得 `osc h≤τ/ρ+Kρ²≤Kρ²`。consistency `a=v−bu` 再给 `osc a≤Kρ²`。故实际保守归约为

    osc a≤Kρ²,
    osc(proj_r b)≤Kρ^(1+ε/2),
    |r|≥K⁻C,
    osc(proj_(r⊥)b)≤Kρ.                      (11)

最后一个只是原 Lipschitz，剩一个标量函数 β(z)。本节排除零/小 r 并定量隔离 residual，未把它换名为已证完整目标。

## 7. 原 PDF99 的强度跳步与保守修复

原 (192) 印为 `osc tilde f_(z₀)≤K(τ/ρ+δ/ρ²+Δ/ρ)`；(195) 后立刻写它成为 `Kρ^(2+ε/2)`。但已显示的估计只有 `Δ≤Kρ^(2+ε)`，从而 `Δ/ρ≤Kρ^(1+ε)`。对 ε<1，这大于 ρ²；直接代入并不支持原书面强化。PDF98/99 的原版式已核实，非 OCR 遗失的幂。

此外 scalar (192) 隐含了对 r₁ 的除法；可按 (9) 先严格给 scalar r₁ 下界。然后用 (10) 取代那次过强代入，在原 d4/k3/ℓ2 中因没有正交 row，得到

    osc tilde f₂≤Kρ^(1+ε/2),
    osc tilde f₁≤Kρ².

选 `σ=ρ^(1+ε/4)`，η预算后取可吸收 K，且 σ∈[ρ²,ρ]。Lemma19.4 得 `C_CW≥δ^(Oϑ/γ)ρ^(−κε/4)`，与 `C_CW≤δ⁻η` 矛盾（κ>ζ、ϑ≪µκεγ）。所以这是**原局部算式强度的可保守修复**，不反驳四维结论；但本项目不应继续未经补证引用其更强 `ρ⁻κ` 下界。mixed42 仍因 (11) 的 β 未控而不能作同一调用。

## 8. full 水平 grain 重用原 (155) 的精度不足

原19.5 lines4344–4370 通过一个共同 coarse θ 得 (155)，随后推出

    y+(tilde f(z)−tilde f(z'))x+constant∈N_(Kρ²)Y_z'.

共同方向只有 ρ 精度，跨 ρ 时间自动产生 ρ² 误差。full 三维 x 的像宽为 `ρ||tilde f(z)−tilde f(z')||`；Y 的 tube-KT/AD upper 在此误差下恰给 row oscillation≤Kρ，即原19.5，并没有第二次收缩。

严格的 query 校准：令 Y 是含 0 的标量 α-AD Cantor，`x∈[-cρ,cρ]³`，取 `Δtilde f=(0,ρ,0)`、constant=0。则对全部 x，`Δtilde f·x∈[-cρ²,cρ²]⊂N_(ρ²)Y`。full horizontal mass 完全保留，而 row 大小仍为 ρ。该有限 observable 并不满足完整 source/SM；它只严格排除由上面这一个含误差关系及 full x/AD upper 免费推出 ρ²-row variation。

若要从同一 fullgrain 机制独立控制 β，至少还需真实地把共同方向误差支付到 ρ²（跨时后 ρ³），或提供另外独立 contraction/原质量约束。不能重复平均 (155) 并把误差自行降低。

## 9. 形式声明与实际可调用输入的量词

Lemma21.1 (167) 原声明量化全部 allowed ρ、全部窗口、全部 R,U；形式否定只给某窗口的 affine concentration，可能损失一个 ρ 固定幂。source §22.3 所用“固定ρ后全局 retained Z'”还需要固定尺度版本的 proof 与窗口 averaging。§21.1 的实际证明确实先固定任意 ρ 再做 W/ABC，因此该强化是其意图；但不能说它由印刷声明的逻辑否定直接得到。本稿以 handoff 明列的固定尺度 affine alternative 为输入，不掩盖这项 named-source localization 责任。

Lemma19.2 控整个 f，不能因 u 慢变就调用；Lemma19.4 控整个 tilde f，不能因 a 和 br 慢变就调用。source (185) 的 `|(r,s)|≥K⁻¹` 可在原 times 上删除少量低速窗口后由19.2/CW得到；若保留这种结论，须把该删除也放进 K。19.4 本身是任意维声明，可对 (11) 若再获得 β 的正幂收缩时使用，不要求把 mixed42 免费投影成 d4。

## 10. 全局原管 marks 可提取，单 q 的 CW law 不免费

完整尺度上 `#E≈K^(±1)δ^(−5+κ)`、`deg(p)≈K^(±1)δ⁻κ`、`#T≈K^(±1)δ⁻4`，所以原 incidence `I≥K⁻¹δ⁻5`。每条原 graph 管至多 Cδ⁻1 marks。删除 marks 少于 K⁻Bδ⁻1 的管后，仍有 ≥K⁻Cδ⁻4 条原管，各有 ≥K⁻Cδ⁻1 marks；用这些原管的均匀 law 或保留原 law restriction，domination 只付 K。不要改成均匀 distinct projected coefficients 再忽略 fibre 重数。

因此 root 所检验的**全局 canonical residual 子例**可尝试直接用原 CCW law 加有权 projection/shading 定理。可是若先选单一 ρ-window/q，单纯从 global probability cap 再归一化会除以局部管质量（自然可能为 `ρ^(4−κ)` 级），这是 fixed power。必须另核实际 sticky rescaling 或保 whole-source mass；不能把全局子例的论证直接当任意局部 β 的证明。

## 11. 本子任务实际改变的下一步

可保留的实际归约是：原三维水平 V/J/L 质量仍付得起；scalar-Y 二次部分先压 τ；再合法排 r=0/幂小 r，控制 a 与 br，并严格隔离一个 residual β。原 (192) 的强化须按第7节保守修复；重用 (155) 的原误差不能补 residual。

尚未证明 β 的独立收缩或完整 mixed 二次排除。root 的全局线性 residual 几何/投影检验若成立只解决其明确子例，不关闭一般 local normalized β。源高级 inputs、实际 restriction 成本、CW 回传仍须独立审查。该记录不作为重大新结果或长期 Goal 完成。
