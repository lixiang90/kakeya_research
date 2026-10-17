# R0040：原来源、质量及下一任务的正式审查

2026-10-17，A。**结论：修后稿在下列明确范围内通过，可归档；完整 d5/k3/ell3 的 κ≤ζ 未证。** FG 条件于具名 WZ Lemma19.2；没有独立重证该高级引理全部证明，没有新的 Kakeya 维数界、真实反例或重大/新颖性认证。未经外部同行评审。

## 1. 实读范围与独立性

本次实际全文读取：

- root `notes/40_multiscale/sticky_flakes/R0040_fine_flatplank_gate_and_slicing_boundary.md` 全12节，并重读短轴、Mat bounded 及 fixed-power time 比率的最后修订；
- B `notes/40_multiscale/sticky_flakes/R0040_slicing_convex_caps_and_counterattack.md` 全7节；
- `research/reviews/R0040_macro.md` 全8节及 `notes/50_counterexamples/constructive/R0040_next_coherent_power_construction_target.md` 全文。

另实读 WZ 原PDF65、78及提取文本 Definitions3.3、17.2–17.4、Lemma19.2；LPSW §9 Steps(i)/(ii)、Props9.1/9.2及投影 fibre 构造（提取2927–2974、3074–3138），Theorems17.3/17.4；FD–deLaSalle v3 Definitions5.2、Lemma5.3、Prop5.4 statement 与其 nested-limit 结尾、Th1.3。

本人是 A 的原 source/FG 独稿作者，故不把对自己同一证明的重读算一份独立审查。这里对 root 整合、B 的独立反攻及 macro/next 作实际逐步核对；FG 另外由 B/root 独立推导审查。三份稿件没有被压成“已证主分支”。

## 2. 原 bounded f 与几何 Jacobian

原PDF65在 Definition17.2 前明定 Mat(k,ell) 的 entries∈[−1,1]，随后给 f:Z→Mat；本次用 Poppler 单抽原页再次核清。故绝对 bounded f 是原假设，并非由 dyadic-Lipschitz 的差值条件推出，也不是额外 chart 假设。无需另增 H=δ^{-Oη} 的修补或误差预算。

long 三维方向空间 P 与 clock 的 projection 长 h≥c0，给固定二维 V=P∩e_t^⊥。V 内任意正交旋转只改变 unit-long cube 的固定倍 enclosure。两 normal 方向必须是 F 的实际 short axes，才能保留 r1∈O(a)、r2∈O(b)；修后 root 已明确，不能任意旋转 anisotropic normal plane。

将 s3 改为实际 t 的 Jacobian 确为 1/h，normal 含 clock 分量亦在换元中。固定 t,r1,r2 时，水平截面仍为同一个 V。由此 ab 同时出现在 numerator 与 |F|，没有漏 a^{-1} 或 b^{-1} 的固定幂代价。

## 3. 逐层 Tube-KT、good times 与 whole matrix

对 exact 原 z 用 L_z(x,y)=y−f(z)x；fine δ blur 只遇 O(1) 原 z。若 λ=||L_z|V||≥σ，在其最大奇异方向上，Tube-KT 给 O(δ^{-Cη}(λ/δ)^{1−γ}) 个 δ-cells。每个 cell 的参数原像长度 O(δ/λ)，乘得 δ^{-Cη}(δ/λ)^γ，再积分另一方向即可。

所得 root (1)

    |Eδ∩F|≤C(c0)ab[δ#Zσ+δ^{-Cη}(δ/σ)^γ]

正确。没有跨 dyadic 边界调用 f 的 Euclidean Lipschitz，也没有给跨时间 Y-union 偷加 Tube-KT。取 σ=δ^{1/4}，假密度≥δ^c，先 c 小后 η 小，使第二项更小，确得 #Zσ≥c1δ^{c−1}。

由 |y−f(z)x|≤σ|v| 与 f bounded，可得 |x|≥c|v|。所以 V 是同一个 bounded G 的 graph；所有 retained times 均有 ||f(z)−G||≤Cσ。这控制完整 2×2 矩阵，不是单一方向或条目的近常。

## 4. 时间删选、原质量及每个 window 的责任

root §6 保留每个 good z 的完整 Y_z/X/Φ/ξ 与原全部 T，而非保 F∩E；η'=Mη 为整数倍，且 η'=O(c+η)。新 allowed scales 是旧尺度子格。

cross-time Y-union upper 由原 union 继承；lower 从任一 occupied center 所属的完整 Y_z 出发，以 fine AD lower δ^η(R/δ)^{2−κ} 除以单个 ρ-cell 的 fine upper δ^{-η}(ρ/δ)^{2−κ}，得到 δ^{2η}(R/ρ)^{2−κ}。固定倍球/边界可将 R 换 R/C，R≈ρ 以一个 occupied cell 补足。该证明不要求任意 selected subset 继承 AD lower。

原 fine Φ-bin→witness 的 O(1) collision、每 (T,z) 承载 O(1) 原 δ-points 与 #T≤δ^{-4−Cη}，确给原 uniform-T×time 的 retained raw marked mass≥δ^{Cc+Cη}。这是平均 duration，root 明确未升级为逐管 density。没有把 selected T 的 posterior 当新 AD 管族。

对所有 retained times，f pairwise 距离≤Cδ^{1/4}。向上取新 allowed ρ≈δ^{1/8−Oη'} 并令 σ_L=ρ²，满足 ρ≥δ^{1/3} 及 σ_L∈[ρ²,ρ]。**每个**新 z0/window 的全部 times 均好，故 ε19=0 合法；若 statement 要严格正值，任取充分小正值即可。因此 named19.2 给

    C_CW(T)≳δ^{Cη'/γ−(1/8−Oη')κ}。

c 先依 ζ,γ 固定小，η 后取小，可使它严格超原 δ^{-η}。没有循环使用待证 κ≤ζ，亦没有把仅一个好 window 送入原全称引理。FG 的所有 F 量词及 δ0 对 η 的依赖正确。

## 5. B 的两个独立转移障碍

all-convex pencil：对任意 contained indices S，取 oscillations A,B。K−K 包含三个 unit-order tangent、r-ball及两根差向量；其 convex hull 的5维 crosspolytope 体积≥c(A+r)(B+r)。标准固定维差体积界与 #S≤C(1+A/r)(1+B/r) 正好给 Σ|F_ab|≤C|K|，不假 S 是 rectangle。central thick slice 的 projected tubes 却都重叠，indexed density≈r^{-2}。每原 cut 只占原 flake 质量 O(r²)，故不反 LPSW 的 global refinement。此范围限制必要且已写清。

曲线表：投影到 γ_ab 所在二维平面，以 normal 的第二分量分大/小两种情形，分别用 quadratic sublevel 与单调 derivative，事件至多两个 intervals，长度≤C√(e/|b|)。原 time-Frostman law 给 N≥cβh/[K_t(√(e/|b|)+d)]，适用于任意相关 marks。local |b|≈R 时的近直线时间尺度 √(e/R) 亦正确。

曾建议修 root 的“h≫ρ 排 subpower 表”措辞：仅 h/ρ→∞ 可只是 log。现已明确 fixed c1>0、h≥ρ^{1−c1}、β/K_t subpower 才迫 N≥ρ^{-c1+o(1)}；精确不等式保留。修后通过。

## 6. LPSW 范围与固定损失没有被误排

LPSW Props9.1/9.2 明确先利用 flat long planes 做直管切片，再投影成 R^{n−1} 的 (n−3)-flakes、uniformize fibres、引用低一 ambient 的 codim2 induction 并付 refinement。n=5 时后者为 R4 的二维 flakes，不能用 ordinary line Kakeya 替代。原论文还明确警告 Tω 未必 essentially distinct；B 的逐 slice 反例针对的正是更强的免费转移。

FG 对任意非负 weights 的平均同样成立，所以否掉 η_src→0 的 fine/whole-clock/flat 平均密度 δ^{Cη_src} 提取。若 a=δ^u，LPSW 门槛仅给必要 uη_L≥c，不能推出所有 fixed-loss 调用都无效。root §9、macro §4 与 next choice 均保留了该区别，也未把 coarse E_e、clock-tangent 或 auxiliary geometry 宣告全部反证。

## 7. 提前 macro 与下一构造任务

主 κ≤ζ 未闭合触发 spec 的停止条件，冻结直接 subpower fine-flat/global-clock 提取及免费 each-slice cap，合理。未覆盖部分不能仅改 blur/clock 参数再续同机制；旧 CP⇔PM、matrix/action/carry 冻结不因此解除。

下一任务直接检验 FD 实际 all-directions 构造的 power saving，与旧全称 source growth 不是已知双向等价改名。它明确只是待研究目标，不称原 paper 已有 power 或反例。固定同一个 compact K 是核心：若 |N_{r_j}(K)|≤Cr_j^c，选 side≤r_j/√5 的 occupied cubes，则这些 cubes 全在 N_{r_j}(K)，数量≤Cr_j^{c−5}，s=5−c/2 时总 s-cost→0，故确反 Hausdorff full-dimension；不需要全尺度 upper Minkowski。

有限 K_j 随 j 改变且仅各自小体积不够。nextspec 要求实际覆盖同一 K，含 fixed-multiple radius 的 upper、方向全集、单位长度、bounded centers 与相容链，未以 compactness 自动给指定 r_j 的 Hausdorff 距离。

FD Definition5.2 确为 compact/unit segments，Prop5.4 的输入是对每个 δ 有合格 compact Gδ、同一 nondecreasing f 的 volume upper；输出为同一 compact E，损失 f(C_dδ^{1/4}) 及固定常数。若将来真有 f(r)≤Cr^c，该桥仍保正幂；本次只核 statement/scope，未声称新构造已满足。macro 将新增义务放在实际 log→power 改造而非重命名原5.4，正确。

## 8. 最终状态

修后 root/B/宏观/下一任务均可按上述范围归档。A 自己源稿仅补 Mat 的字面 bound 与实际短轴说明，未改变主命题。没有 outstanding 必修问题。完整五维 sticky 分支、一般 Kakeya、major/novelty 均保持未解决/未认证；外部 advanced proof 责任按具名输入保留。本次停止编辑，无 Git 操作。
