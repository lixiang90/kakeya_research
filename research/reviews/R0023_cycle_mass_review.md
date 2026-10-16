# R0023 独审：原 weighted cycle 集中估计

2026-10-17，`lifting_obstructions`。独立审查 `notes/40_multiscale/sticky_mixed/R0023_weighted_cycle_concentration.md` 最终正文 §§1–5；对照本轮 actual source audit 的 §§4–9、原 WZ §22.5 及本人的独立有限证明。只审该文件，不把 vector BSG、粗时间选择或完整非二次增长当作已验证输入。

**结论：通过其有限结论；§5 对直接从实际 L bounded graph 取得的 heavy-edge H 的 small-τ 点球排除也通过。** 原 c 的总质量、实际 base/gap、误差与 retained loss 均须保留。近线结论只产生有原质量的部分 scalar nonquad 模型，不是 linewise translation 定理或二维增长。

## 1. S/Q 的符号和 vector 系数

将 `S(t,s)=(s−t)(F(t)−F(s))+(s−t)²G(s)` 展开，mixed terms 正好为

    t[F(s)−2sG(s)]+t²G(s)+sF(t).

故四差给正文式(1)，特别是 F(t₁) 的系数为 `(s₁−s₂)I₂`，G 项的 sign 为正。写成 U(s) 的 2×4 矩阵作用和 V(t) 的四维列也一致。此处没有从形式 rank 推出任何非集中。

实际 L relation 的总正负号应由原路径核；本轮 source audit 已记录固定角差次序得到这一 S。若整体反号，反射 image/改变 q₀ 可保持本有限结论；不能仅改 F 的一块而漏改 G。

## 2. 点球 cap 和 conditional D⁻¹

正文式(2)正确：固定 s₂，close s₁ pairs 的原质量≤2K_tg₀，前提 `g₀≥d` 使查询 interval 长度合法。其余固定 s₁,s₂,t₂ 时，除以 Δs 得同一个向量 quadratic。所有 coefficients 可以依赖已固定参数和 ball centre，甚至很大；uniform all-real (NQ) 正好覆盖，原 t₁-fibre 质量≤a。

对任何 `0≤c≤1`，直接积分得到未归一质量 upper；除以 `D=∫c dν⁴` 后确须乘 D⁻¹。正文没有忘记这个费用，也未把 cycle law 改成 Q-image 的均匀 law。N 个 e-balls 的 covering lower `N≥D/(a+2K_tg₀)` 因此成立。

若 c 是大重数路径 law 而尚无 c≤1 的 domination，以上结论不能直接应用；这一责任仍在 actual L/code 恢复和归一。正文所用实际 frame 来自已付 bounded graph，不声明原路径天然等权独立。

## 3. dense-cycle 近 affine line 的选择和常数

令 `k(t)=ν(H_t)`。固定低 row k(t)<r 时，c 支撑于 H 的四环，故两个右时间都在 H_t 中；对其余左时间仅用 upper1，整条 row 的 cycle 质量≤k(t)²。两条 left rows 删除损失≤2r²。取 `r=√D/4` 后为 D/8，正确。

再删 `|s₁−s₂|≤g₀`，损失≤2K_tg₀≤D/8，剩余 c_* 质量≥3D/4。原三个其它变量均带概率 prior，连续两次有限 Fubini/平均可选固定的 `(s₁,s₂,t₀)`，使

    ∫c_*(t,t₀,s₁,s₂)dν(t)≥3D/4.

所以其正支集 T 的原 ν 质量 m≥3D/4，且每个 T row 都保 degree≥r。t₀ 不必属于 T，本证明不需要它属于 T。

这里 L 可为 affine `q₀+L`：在 normal component 的式(1)中，`n·q₀/Δs` 只进入 quadratic 的 constant coefficient。无需让 affine line 通过0，也无需假设原选择 c 在交换两个左时间后仍保持。正文没有错误使用支撑对称性。

由 `e/g₀≤h/4` 和 scalar h/4-fit 组成的 vector polynomial，误差至多 `√2h/4<h`。因此 scalar nonfit 条件质量≤a/m，(9)的 `4a/(3D)` 正确；这只给沿 L 的一个经过付费的方向，不是全部 scalar projections。

## 4. 原 g 质量以及重新生成的 cycles

若 `H={E_σg≥λ}`，T 的每一行 degree≥r，便有 `E_{σ×ν}g(t,·)≥λr`。因此 conditional graph mean≥λr，原 absolute mean≥λrm≥`3λD^{3/2}/16`。这一步不删除 A，故其 input AD/tube-KT 保持原样。

H|T×B 的 conditional edge density≥r；两次 CS 给完整四环相对质量≥r⁴=`D²/256`。乘 m² 后，原 ν⁴ 质量≥`9D⁴/4096`。这些常数均核对正确。

正文准确说明这是**重新生成**的 H-cycles。原 c 在 T²×B² 上不必仍 dense，这些新 cycles 也不必仍在 `N_e(q₀+L)` 中。固定一个 Fubini fibre 不能提供这个量词闭包。该限制正是剩余 branch extraction 的实际缺口，不能删去后宣称已付 common-line translations。

此外 Q 是 mixed difference，不能由 Q 沿线便在原 `x+S(t,s)` 关系中删除 left/right coboundaries。A 的 scalar projection 也不继承二维 A 的 deficit。MNL001 还要求其自身的 affine-SM、同 B 与二维差 law 的 slab line-cap；当前 mixed32 的 Φ 是 scalar，不能直接嵌成全压一条线的二维差 law。正文保持未接入状态正确。

## 5. small-τ 的 actual 点球预算

对实际归一化 F，原 source coefficient-weighted quadratic nonfit 可缩弱为 uniform

    h≈K⁻Cρ^{2ε₁+ζ₁},
    a≤K^Cρ^{ε₂}/θ,

其中 θ 是相对被引用原 window 的真实保留质量，angle lower 及 normalization 的固定小幂已计 K。只要 normalized uniform h 被选得不超过该实际容差，就不必假定所有 scalar projections 非二次。反向从 uniform 推回 coefficient-weighted 不是本文结论。

保留原 fine indices，base `d=δ/ρ`。ρ≥δ^{1/4} 给 d≤ρ³。对

    ρ^{3+2ε₁}<τ≤ρ^{3−ζ₁},
    w=K[ρ+ρ^{3+ε₀}/τ],

有

    w/h≤K^C[ρ^{1−2ε₁−ζ₁}
                    +ρ^{ε₀−4ε₁−ζ₁}].

因此先选 `ζ₁+4ε₁<ε₀`、`2ε₁+ζ₁<1`，再把 AFF/retention/stability 和原 η 的损失选小，两项确实有正幂余量。这里使用的是允许的 sufficiently-small ε₁ 子范围，未认证原打印允许的每个 ε₁<ε₀/2 都自动满足此估计。

正文最终选取 H 为原 L bounded graph 的 a-average heavy-edge set，因此 edge density≥K⁻C、原 complete-cycle 质量 D≥K⁻C，直接由 CS 得到；**不必先支付尚未验证的 vector BSG。** 以 K_t≤K 和 θ 的真实 lower 计费后，可令

    a+2K_t max(d,w/h)<D.

所以全部这些直接原 H-cycles 的 Q 不能落在一个 w-ball 中。这是实际原质量的点球退化排除。后来的任意 c 删选须重新检查 D；不能无条件沿用原 complete-cycle lower。

若还要应用正文§3的近线提取，取 `g₀≥max(d,4w/h)`，并检查 `2K_tg₀≤D/8`；固定倍常数由同一正幂余量支付。点球§2只需 `max(d,w/h)`，两种容差没有实质冲突但须区分。

本 actualization 不需要把 fine B 免费改成 w-separated，也不借 large-τ 删除 G 的尚未覆盖误差。它只覆盖上述 small/middle-τ 区间；large-τ、vector BSG 的输出控制、后续 matrix projection-growth 均未因此通过。

## 6. 认证范围

已核：保原 weighted ν/c 的 point cap、dense-cycle affine-line Fubini、row degree 的平方损失、原 g 的两种质量、重新生成 cycle 的准确范围及 small-τ 正幂预算。没有得到足够的二维 covering exponent、translation gain 或 κ>ζ 矛盾；N5-MIXED32-NQ01 仍 open。有限 CS/Fubini 接口不列为已认证新颖或重大结果，不是完整五维/Kakeya 反例或维数结果。
