# R0009 稀疏方向放大独立审查

日期：2026-10-17。审查者：`lifting_obstructions`。对象：`notes/40_multiscale/plank_inputs/R0009_sparse_direction_amplification.md`。结论：**有界 shear 放大及其到任意 M 无权输入的条件桥接通过内部独审**；最后的几何下界始终依赖 SRC-001，进而条件于完整四维证明及其外部输入正确。

## 1. 量词与几何类别

输入是固定 bounded 四维 graph chart 内的 M 条 δ-slope-separated lines，各自有至少 δ⁻¹⁺η 个 marks，footprint 为同一 E。输出使用 shear `S_a(t,y)=(t,y+ta)`，不是正交旋转；现稿首段明确限定这一点。

这种替换合法：SRC-001 的条件输入只要求输出仍是固定 bounded graph family，没有要求它必须是原 family 的正交像，也没有要求所有 copies 属于同一原始 Kakeya set。后一点正是 SRC-001 的 proof-level finite 读出与仅引用 Hausdorff 定理陈述的区别。若不接受 SRC-001，则不能靠本初等 lemma 单独补上其几何下界。

所有 shifts、输出截距、斜率、位置与 shear operator norm 都只依赖原固定 R；没有 δ-dependent chart 范围。

## 2. 任意稀疏 M 的方向体积放大：通过

δ-separated slopes 周围 radius δ/10 的球不相交，故其并 U 的体积为 cMδ³。对固定目标盒 Z 及足够大但固定的 shift 盒 Q_R，所有 z−U 均落在 Q_R，因此均匀 shift a 有精确概率

`Pr(z∈U+a)=|U|/|Q_R|=:p`。

取 K=ceil(1/p)，即 K≤C_R δ⁻³/M。独立 shifts 的命中概率至少 1−e⁻¹；Fubini 直接给一个确定选择，使 Z 内覆盖正的固定体积。这里只需正体积，不需覆盖每个方向 bin，因此没有 coupon-collector 的 log δ⁻¹ 成本。

M=1 和 M≈δ⁻³ 两端均包含在这个同一估计中；没有使用总方向质量有固定 lower 的假设。

## 3. 提取实际 separated lines：通过

复制后所有 slopes 的集合仍有限且有界。在其中选 maximal H_Rρ-separated centers，ρ=C_*δ；bounded-chart bi-Lipschitz 常数保证其单位方向至少 ρ-separated。

每个原 center 都被一个 H_Rρ 球覆盖，因此前述正体积给输出数量至少 c_Rρ⁻³。每个被选 center 都对应一个实际 pair (i,k)，不是仅选一个球中心后臆造线或 marks。若相同 slope 有多个 indices，保留一个实际 index 即可；其完整 marks 均继承。

copy 数乘原 M 至多 C_Rδ⁻³，故输出有限复杂性也不依赖额外的巨大 index 数。

## 4. Marks 与全部 union 成本：通过

shear 保留 t，故不会将长 shading 压成坏的时间投影。ρ-time bin 最多合并 C_*+1 个原 time centers，因此每条输出保留至少 c_Rδ⁻¹⁺η 个 marks，不要求这些 marks 均匀分散。

将每个保留 mark 移到新 ρ-bin center，空间位移至多 C_Rρ。一个原四维 δ-cell 的 shear image 再扩大 C_Rρ，只碰到固定 C_R 个 ρ-cells。因此全部 K copies 的 footprint 满足

`#E'_ρ≤C_R K #E`。

这是按原 E 的 cells 计一次每个 copy；没有按每条 line 再乘 M。最后取 separated 子族只减少 union。该论证也兼容把完整 marked trace segments 相交 cells 纳入 E 的更宽约定。

## 5. SRC-001 与任意 M 输入的指数预算：通过

对给定 σ>0，先以本 lemma 的固定输出 chart 调用 SRC-001，得到 η_src>0；再取原 η≤η_src/2。输出数量 c_Rρ⁻³ 大于 ρ⁻³⁺η_src，输出 marks c_Rδ⁻¹⁺η 大于 ρ⁻¹⁺η_src，均对足够小 δ 成立。常数吸收使用了明确的幂余量，而不是在 η=η_src 时直接删掉常数。

SRC-001 给 `#E'_ρ≥ρ⁻⁴⁺σ`；结合 K≤C_Rδ⁻³/M，得到

`#E≥c_{R,σ} M δ⁻¹⁺σ`。

该下界对所有 1≤M≤C_Rδ⁻³ 一致，正好给本轮 weighted 化约所需的任意 M 输入 U(σ)。需要更保守的单线边界预算时，可再把 η 取为不超过 σ/2；这是自由缩小容差，不影响上述证明。

本步骤没有把 direction-rich 假设偷偷应用到原稀疏 family，而是先对实际放大后的 near-full separated family 调用它。所有 ε/η 常数、阈值只依赖目标 σ、固定 chart 与 SRC-001。

## 6. 审查结论及保留边界

现稿主数学不需修订。它已经严格区分无条件的初等 shear 放大与依赖 SRC-001 的四维几何下界。与同轮 `R0009_weighted_direction_reduction.md` 的确定性 bin-representative 化约接合后，可获得任意正权与重复 indices 的方向-bin 版本，物理 slope-density ceiling A 必须代入 α=C Aδ³。

本 review 不证明受限 source 类的 normalization、coarsening、selection 或 completion 闭合，不修复 generic j=3 horizon 模板，也不认证新的 Kakeya 维数下界。对原 source zero-depth 调用的可用范围及原 (2.20)–(2.23) 的 group 成本，应继续按 weighted 笔记第 5 节的实际 A 与原 prior 核算。
