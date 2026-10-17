# R0040：切片、来源门槛与下一任务量词独立审查

2026-10-17，B 独立审查。实际全文读取 root 的 `R0040_fine_flatplank_gate_and_slicing_boundary.md` §§1–12、`R0040_macro.md` §§1–8、`R0040_next_coherent_power_construction_target.md` 全文，以及 A 的 `R0040_actual_source_and_flake_extraction_audit.md` §§1–10。收到修正后又逐项读回当前文本。自己的几何稿不计独立审查；无 Git 操作。

**结论：修后文本在下列明确范围内通过。** FG 是条件于具名 WZ Lemma19.2 的真实来源推论；两个切片障碍的几何证明成立。完整 d5/k3/ell3 的 κ≤ζ 仍未解决，没有满足全来源条件的 Kakeya 反例，也没有新高维维数结论。新颖性、重大性及外部同行评审均未认证。

## 1. 原输入与 FG 的量词

独立重读 WZ2609.22035v1 Definitions17.2–17.4、Tube-KT 定义和 Lemma19.2 的完整 statement。原 PDF65、提取文本行3361 明确约定 Mat(k,ell) 的 entries 属于 [−1,1]，随后 f:Z→Mat；故绝对 bounded f 是原输入，不是从 dyadic-Lip 差分推得的新假设。root 与 A 已在修后文本写明出处。

FG 仅针对 fine N_{Cδ}(E)、固定有界区域、三根单位长轴、δ≤a≤b≤1，且 long-plane 的 clock projection 至少固定 c0。对所有 plank 同时成立来自逐个确定性的统一估计，不需无限并集。它没有覆盖 clock 分量趋零、局部时间重缩或 e≫δ 的 blur。

## 2. FG 的积分与来源回传

修后 n1,n2 明确是 F 的两根实际短轴。a≪b 时不能任意旋转 normals 后仍免费给 a×b 参数盒；该处已修复。三根长轴均为单位量级，V 内的 SVD/正交换基只放大固定倍。

令 V 为 long-plane 的二维 horizontal kernel，以真实时间替换第三个长参数的 Jacobian 为 1/h，h≥c0；短轴可以有时间分量。每原 z 的 O(δ) 时间带体积上界为 C abδ，保留同一 ab 因子。E 的 fine blur 在每时刻仅涉及 O(1) 个原 z，使用 exact z 的 L_z，未跨 dyadic 边界调用 f 的 Euclidean Lipschitz。

若 ||L_z|V||≥σ，沿最大奇异方向固定另一参数：原逐层 Tube-KT(1−γ) 给 O(δ^{-Cη}(λ_z/δ)^{1−γ}) 个 cells，每 cell 参数长度 O(δ/λ_z)。因此相对截面面积上界是 Cδ^{-Cη}(δ/σ)^γ。normal offsets 只平移这条 image line，Tube-KT 对其统一适用。积分得 root(1)，没有 a^{-1}、b^{-1} 或换先验费用遗漏。

σ=δ^{1/4} 且 c,η 足小，则假定相对 shading≥δ^c 迫至少 c1δ^{c−1} 个小算子 times。bounded f 保证 π_x:V→R² 统一可逆，由同一个固定 V 得到同一个 bounded G，全部这些 times 的完整矩阵 f(z) 与 G 相距 O(σ)。没有将单条目近常冒充 whole-matrix 近常。

取这些完整原时间层，保全部 T、每层完整 Y_z/X、ξ/Φ 及 witnesses。新 allowed grid 选 η'=Mη，只放宽原条件。跨时间 Y-union upper 由包含继承；lower 用一个完整保留 Y_z 的 fine lower，除以该 Y_z 在每 coarse cell 的 fine upper，给 δ^{2η}(R/ρ)^{2−κ}。没有给 selected point subset 重设 lower，也没有把 union AD 升为 Tube-KT。

原 incidence 计数亦核过：Φ-bin 到 witnesses 有固定重数，每个 (T,z) 承载 O(1) 个 δ-separated p，因而保留层在原 uniform-T×unit-time law 下平均 marks 至少 δ^{Cc+Cη}。这不是逐管 density；修后主稿及 A 均保留了区别。

最后取新 allowed ρ≈δ^{1/8−O(η')}、σ_L=ρ²。所有新 times 的 f 值彼此近常，故 **每个** 新 window 的19.2条件均成立，而非只一个窗口。其 CW 下界指数为 Cη'/γ−(1/8−O(η'))κ；先 c≪ζγ、后 η≪c，利用 κ 的原 bounded range，确实反原 δ^{-η} 上界。调用的是未改整管族 T 的 CW，无短片自动继承。19.2 的整篇高级证明未在本轮重证，仍是明确具名责任。

## 3. All-convex pencil 与曲线表边界

root§10 的全片 pencil 对任意 contained index 集 S 都成立：K−K 含三个 unit tangent、r-ball 与两参数振幅给的 normal 向量；选择各 normal 的振幅或 r 中较大者，determinant 给 volume≥c(A+r)(B+r)。固定维差体积界及 grid packing 于是给所有 convex K 的 ambient cap，无须 S 是 product。central slice 的 indexed raw density 可达 r^{-2}，取 distinct reps 付 r²；但它只占总原质量 O(r²)。所以只反免费逐 slice 继承，不反 LPSW9.2 的付费 global refinement。

root§11 的曲线 sublevel proof 对任意 affine line、任意相关 marks 与原 interval-capped time law 都成立；至多两个 interval 的覆盖将 Lebesgue sublevel 正确转成原 ν 上界。修后固定幂量词已补：b 固定、e≈ρ²、d≪ρ、h≥ρ^{1−c1} 且 β/Kt≥ρ^{o(1)} 才迫固定幂大小 line 表。仅 h/ρ→∞ 可以只是 log 比率，不能排 subpower 表。若 transverse b≈ρ，则正确门槛为 √(e/ρ)，不能套 unit-b 例子给所有 h≫ρ。该曲线例明确不满足完整正 κ 来源，不被当主命题反例。

LPSW§9 的 flatflake→straight slice→低一维 codim2 plane induction，与实际 moving grains 不是同一个几何类别。n=5 时投影对象是 R4 的2-plane flakes，不能直接换成 OAI4 普通直管定理。

## 4. 被排除的桥与仍开放的预算

FG 对任意非负 weights 的原体积平均逐项相加，排除 source η→0 下 fine/whole-clock/固定横截性的 inverse-subpower dense 平直片直接提取。

修后 fixed-loss 范围准确：a=δ^u、λ≤δ^c，与 LPSW 门槛 λ≥a^{η_L} 兼容的必要条件是 uη_L≥c；不能从可选更小 η_L 推断一切较大可用 η_L 都失效。fixed-loss、coarse blur 或辅助几何策略未全部反证。冻结的是上述特定直接桥和免费逐 slice cap；不把其余阈值改名继续作为新进展。

## 5. 提前 macro 与下一构造目标

macro 如实保留完整 κ≤ζ 未证，并按 R40 既定退出规则冻结局部连接；没有把 FG 偷换成整个 sticky 分支。下一任务直接攻击真实 all-directions 构造，与旧 matrix/carry/CP⇔PM 的全称 shading 改写不同，因而作为有界试验合法；这不是成功概率或新定理判断。

nextspec 的目标是 **同一个** bounded compact K⊂R5，包含每方向完整单位段，并在一列 r_j↓0 上有固定 c>0 的 neighborhood upper。取 mesh 为固定倍更小的 r_j，cube 数≤C r_j^{c−5}，s=5−c/2 时 cover cost→0；所以该子序列足够给 Hausdorff 反例，不误加全尺度 upper Minkowski 要求。反过来，不相容的不同单尺度集合与仅 compactness 子列并不自动给所需 radius 的最终 cover。

有限 stage 的方向、中心、长度、复制数、极限 fibers 和最终覆盖责任均明确。FD 原5.4已有合格单尺度输入到 compact 集的桥这一点在 nextspec 仅作 scope 识别；其实际适用及 power 输入留下一轮核，未假称本轮已重证。若 f(r)≤Cr^c 真满足该桥，参数 r^{1/4} 仍保正幂，但原 logarithmic bound 不因此变成 power。

一主轮停止条件具体：只剩原 log、fixed power 以丢方向/长度为代价、不能给同一个 K 的合法 covers，或退回旧冻结全称难题时，记录严格失败并 macro 换路。仅改 ε(r)、网格或常数不验收；疑似反例须独立全文审查与一手比对后才可声明。

以上修后范围审查完成。长期 Goal 保持 active；不提前标猜想、完整五维分支或重大结果已完成。
