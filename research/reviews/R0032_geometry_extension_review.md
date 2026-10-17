# R0032：基础与 terminal extension 几何链独立审查

2026-10-17，A / audit_four_dimensional。审查对象为 root 的 `R0032_terminal_extension_full_proof.md`（本次读取152行）与 B 的 `R0032_anchor_assignment_audit.md`（184行含末空行）。对照原 OAI4 PDF8–14、36–46，抽取文本358–495、592–750、1908–2475行；相关引用按 `split('\n')` 编号。具名输入为已内部重证的 TCM001 / ASM001，不重证其全部内容。只编辑本 review，不操作 Git。

**结论：通过本次独立审查。** root 基础 §§2–4 与 root/B 的 anchor、代表方程、whole assignment、曲率归一化和 tempered 实现未发现必须修正的数学缺口。A 自己的 part1 稿不计作本次独立证明；root §§5–7 在这里检查与前后实际 law/常数接口，part1 的独立验收须并用 root/B 的另行审查。通过范围限于原 j=1/2、degree2 的 Lemma3.5；不认证其余章节、完整 OAI4 或无条件高维结论。

## 1. 量词及原 prior

固定 d₀<1、angular S/η、维数和 degrees，然后固定 e>0，再沿原 N=N₀ 序列趋于无穷。允许充分大 N 的阈值依具体 exact problem/e；不能让 N^{Ce} 的 C 依其 polynomial complexity exponent。root §1/§13、B §1/§11 均如此区分，没有宣称 e=e_N→0 的统一估计。

原 assigned prior 为 νγ，time 独立 uniform；selected incidences 是未归一化 restriction。w_new=B w_old 后 hidden grid 宽度变为 δ，derivative scale 为1；还原时一阶/二阶 w 导数分别乘 B/B²。world/block 外权始终为 ωγ q₁。

## 2. Lemma2.3/2.4：TV 与列表表实现

root §2 的 restriction/refinement estimate 是逐 state 的 g′≤εg 后积分与至多 D 个 entries 求和；不含条件概率下界假设。将原 tempered joint law 转为 (t,y,V,其余系数) 后 Jacobian1。固定其它变量，一条 base-coordinate fiber 上所有原 polynomial predicates、density pieces 及 discrete-label bin predicates只有 polynomial 多次跳变。高度、其它变量体积和 copies 数均 polynomial，因此沿一个 base 轴的 L¹ translation 代价≤N^A|h|；多轴 telescope 后仍如此。

在同一网格 cell 内积分 pairwise density differences，再令 h 为两点之差，得到 cell averaging 的 L¹ 误差≤C N^Aρ；取 D>A+T+1、ρ≈N^{-D} 即得 TV≤O(N^{-T})。A/D 可以依原复杂度，未进入后续 N^{Ce}。

flattened joint law 在固定 cell/conditioning bins 内 posterior 恒定，故有限候选 label lists 中可选一个最大成功质量的固定列表。表的 cell/entry 数为 polynomial，实际查询几何谓词仍 tempered。TV 对任何 selector 一致，所以先从 capped measure 证明某可测 short-list 有高 success，再在**原 tempered joint law**做 flattening、最大表、转回，确实可去掉分析 density mask。这里未把 masked measure 冒充 piecewise-constant tempered prior。

## 3. Lemma2.9/2.10：真 floor 与 crossing lists

degree2 Q 的 |Q′|≥b 分至多两个 monotone 区间；每段 |Q|≤ε 的长度≤2ε/b，故总长≤4ε/b、grid-bin 数≤C(1+ε/(bδ_bin))。root §3 与原2.9一致。

先用 Σωqν_c≤1 删除 qν_c>H m_c，损失≤H^{-1}。对移除 observation upper-cap 例外的部分，在每 chart base 上以 test 小值及**该 chart 的 selected-derivative 兼容条件**限制 hidden bins，给 good m_c≤K n(r)qJ_c。full chart mass超过此上界两倍的 whole-chart 删除量≤2 omitted mass。合 true floor 得 m_c/q∼logν_c∼logn(r)J_c。

crossing count 积分针对 capped **原 incidence law**，而非只已 assigned 的 incidences，故 ∫T dμ_cap≤KΣω n(r)qJ_c≤KΣωm_c；Markov 给 subpower lists。§2 的原 joint-law table 实现后，再删失去超过半 mass 的 charts，true floor 只扩大 subpower slack。未以任意后来 pair restriction 的 current mass 代替旧 floor。

## 4. 原2.12的实际调用

root §4 已补工作入口未显列的真实依赖。若 ∥D_c∥/q≤N^{-α} 在 inverse-subpower mass 上，whole-interval 空间拟合迫 V 落中心速度附近 K N^{-α} ball。取 fixed 0<u<α/2、u≤ηL，每个候选 chart 仅给 K 个 angular bins；pL-known label lists 于是也仅给 K 个 bins。

先删 pure pL lower 与 joint-angular upper 的例外，再对每个实际候选 bin 用 numerator≤n(L)N^{-Su+τ}、pure denominator≥n(L)N^{-τ}。其候选质量积分≤K N^{-Su+2τ}，τ<Su/4 时为 power-small，矛盾。这里只利用原 good measure，未对所有未删 bins 取免费 maximum。whole-label homogenization 后最大轴∼logq；保留整 labels 不改变各旧 used chart 的 floor。

## 5. part1 接口核验，非 A 自审认证

root §§5–7 用双时间 restriction 的 one-time domination、旧 true floors 计 oldlabels、同 source-base cap (5)、pre-deletion entry masses 及 group π；这些与 A 主稿接口一致。尤其 C_entry 先给 discriminant coefficients/C_U，之后另选 C_index，未把后者回灌前者。group mG 可以很小：raw index weights nQ/mG′ 的总和≤2N^{C_index e}，确实支付 normalize 分母。

二维 strip intersection→小 velocity ball 只用于原 j=2。没有将该论证视作 j=3 的 AFF 前端。M>1 的 group mass 依 native test/derivative 提供 subpower unit bins，未按 O(M) 计费。

## 6. 随机 anchor 与 bounded-root/far-root 区分

root §8 / B §2 的每个 retained pair 点值 lower 给 discriminant 在固定 anchor box 的 norm lower。polynomial sublevel 控 anchor value 失败；限制到 complex line 后 degree fixed、endpoint values lower、derivative upper，迫 bounded roots 距0/1至少 N^{-Ce}。

从任一 endpoint 到随机 σ 的 segment 碰半径 N^{-Be} root disk，其 shadow probability≤C N^{-Be}/dist(root,endpoint)。两 endpoint、boundedly many roots 求和仍 power-small。沿避盘路径使用 p(s)/p(0)=Π(s-r)/(-r)：bounded roots 的 numerator 有 lower、denominator 有 fixed upper；far roots 的 ratio 有 fixed lower。因此不需要 leading coefficient lower，也不需要 bound 所有 roots。再以 full-base derivative upper 缩小 tube 即得真正 complex-base zero-free tube。

异常先对随机表、再对原 weighted pair law 平均。共享同 D 的随机点只用 Fubini；未 union polynomial 多 trajectories，也未要求所有 pairs 同时好。

## 7. Anchor bins、tiny curvature 与代表表

ASM001 将 local difference 传至 anchor/固定 jets；common bin spacing δN^{C_b e} 取在 close loss 之后，故 paired jet bins 只有 bounded neighbors。给 witness A′，每 compatible D 的 converted equation在 anchor 仅≤2 simple root/jet tuples；monodromy 只能互换这两 tuple，不能增计。因此 oldpL→A′→D→neighbor bins 的列表为 subpower。

tiny c 的 unused root 可以逃至超 polynomial，root §13 / B §3 没有储存它或显式 c^{-1}。实际表只量化 polynomial stored range 内的 root/jet，使用原 polynomial equation 与已付 lower 的 P_w=±√discriminant 作 implicit jets；root 在范围外不产生输出记录。chosen source branch 的 range 由 source 近实际 w、implicit jets 与 ASM001 continuation 给 polynomial bound，足以覆盖全部 successes。

P_b 是 anchors/D/bin 与固定有限 old-equation list 的函数，先建表，再选 source time；代表为 real equation，即使其 anchor branch非实。同 bin 的 source/代表 germs 由 finite-jet comparison 接近。Taylor 的二次误差是 δ^{-1}(δN^{Ce})²，故 root (8)、B (3) 的 δN^{O(e)} / N^{O(e)} 估计正确。

## 8. 返回 source evaluations 与整段外推

回传函数为 P_b(z,f(z)) 与 P_{b,w}(z,f(z))，它们是 **source** germ 的 fixed-degree polynomial evaluations。ASM001 沿 source-safe path 适用；不要求 representative discriminant 在 return path nonzero，也不要求代表在实 source 附近有根。

source own selected incidence 的原 |P_A,w|≥K^{-1}，结合其 affine-time upper，给相对 new-block 长度≥N^{-Ce} 的一侧 segment 保持 derivative lower。缩入 source ball 后 early curvature cutoff 使 completing-square estimate 连续跟同一个近根；临 block 边界使用 one-sided segment。于是 returned evaluations 可换实际 w，再按固定 degree 外推整 I，得到 (9)/(B4)。version1 虽 w quadratic，但 test 仍 w−F，沿 trajectory degree2；未误用一般含 w² 的 test。

## 9. 代表 discriminant source lower 与 source-time freeze

先固定 anchors/table。每 source A 的 D 固定，anchor 最多两 source root/jet tuples，故最多 bounded 个代表，不按全部 bins union。每代表 anchor lower 经 polynomial norm comparison 与 sublevel 给坏 source-base volume≤C N^{-θ(C₃-b_anc)e}。以 (5) 的原 source-base density 和 oldlabel count 相乘，bad mass≤K N^{[C_base+1−θ(C₃-b_anc)]e}。C₃ 在 later T 之前固定，table 的 functional independence of t₀ 是此求和的必要输入，已满足。

每 world/block 选择 anchors/detour/source time 使 success 至少其参数平均，只保证 Σωq₁ success≥N^{-o(1)}。individual blocks 无 lower 也无妨；未按 block 数收费或把 frozen measure 条件化成新 trajectory prior。

## 10. 唯一 whole assignment、真正 oldpL knowledge

fixed source time 的旧 selected membership 唯一决定 A；A 决定 D/nearest branch/path/bin。显式要求 stored range/table entry、whole-block spatial/test bounds及 source representative discriminant lower 后，将满足条件的 trajectories 赋 c₀=(D,b)，merge 所有同 c₀ 的旧 source identities。assignment 与 later t 无关且 disjoint。

later selection 仅要求原旧 selected incidence 及 actual witness 的 compatibility list 含 D/b。它含所有冻结 successes，故有 inverse-subpower mass；输出不保 analytical density/group masks。原 pL 的 A′ shortlist 再组合有限 roots/neighbor bins，真正命中新 c₀。old source A 只在 assignment 的内部计算使用，未作为 output label 的不可观测附加项。

## 11. 曲率分支及全部 Def2.8 条件

低曲率先有 C₂/C₃，再选 C₄>C₃/2+2、C_s>C₂+C₄+1，最后 T>max(C₂+C₃+1,C_s+C₄+1)。|2cP_b|≪N^{-C₃e} 与 source |D_b|≥N^{-C₃e}、P_{b,w}²=D_b+2cP_b，迫 D_b>0 和 source derivative≥N^{-C₄e}。dyadic v 给 block max normalized∈[1,2)、value fit δ_s、curvature≤K/δ_s，label 只多 O(logN) choices。

normalized derivative affine 且 block max≥1，其绝对值<κ 的 timefraction≤Cκ：小 slope 时区间为空，大 slope 时直接 inverse derivative。以 Σωq₁ν_assigned≤1 计 global loss≤Cκ，选 inverse-subpower κ=o(M_fr)，所以无需 conditioned success time 有 density upper。version1 derivative恒1，v=1。

高曲率直接 |w−F_ctr|=|P_{b,w}|/|c|≤δN^{(T+C₂)e}，得到 real affine test、derivative1/curvature0，不需实代表根。选有至少半 mass 的 case，C 超过最终两厚度指数，再限制 e<cL，给0<L′<L、L−L′≤Ce；q₁ exponent 为 h−e。undo B/base map 后正好恢复 derivative B、curvature B²/aL′、空间最大轴≤q₁K。未额外要求或声称 new true floor。

## 12. Temperedness 与最终边界

finite tables 的 polynomial 个数、原 bounded-degree predicates、fixed-format branch continuation/jet relations、whole-block 对单 time variable 的测试均允许固定维 QE/显式极值实现。source times/anchors 可作为无 height 限制的 real constants。分析搜索和 density masks 不进入 predicates。inverse curvature 仅用于已指定 cutoffs 以上；1/v 有显式 polynomial upper；tiny unused c^{-1} 不存储。因此最终 coefficients/width inverses/ranges 仍 polynomial。

N^{Ce} 的常数仅依固定 degrees/model/angular：discriminant由 heavy-entry体积给相对界；oldlabel count 的 nQ 恰取消；每 A 仅 bounded 代表；continuation 为 fixed format；删时按 whole-prior budget。具体 problem 的大 range exponent 只付 O(logN) choices，可在每 fixed e 下吸入 N^e；它只影响阈值，不影响 C。root/B 均未作对所有复杂度的共同 N₀ 阈值声明。

综上，两份被审稿在上述范围可归档，未发现真实原 prior/量词反例。完整 Lemma3.5 的内部验收应联合根与 B 对 part1 的独审；本 review 不把 A 自己的前半重证算第二份证明。未经外部同行评审，不释放后续 critical-path/高级输入及完整四维证明的未审条件，不作新维数界或重大性声明。到此停止本轮编辑。
