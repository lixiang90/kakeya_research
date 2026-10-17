# R0028 独审：原共同作用盒、闭包边界与下一种子任务

2026-10-17，`lifting_obstructions`。独立审查 A 的 `notes/40_multiscale/sticky_mixed/R0028_original_action_extraction_audit.md`、root 的 `R0028_actual_action_boundary.md`，并核 `notes/20_dimension_lifting/finite_seed_transfer/R0028_next_finite_seed_target.md` 的范围与条件算术。对照本库 He1611 v2 Theorem3、He–de Saxcé1806 v3 Theorem1.1/Def2.1，以及 Katz–Tao0102135 v1 Definitions5.1–5.2、6.1和Theorem6.2。本文不新增下一轮证明或重新搜索前沿。

**结论：上述稿件在明确范围内通过。** 共同base、原四time/四角参考先验上的有限16边box有真实质量；恢复matrix-time frame的误差及参数费用已付。有限box不等于可迭代作用闭包，现有He自然lift有具体不变子空间或平凡quotient障碍。四维结果到任意ambient、单尺度任意saturated shading的KT种子尚未证明，17/4只是条件算术，五维递推ceiling为4。本轮未证明AFF₃、固定>2增长、完整factorized反例或新高维维数界。

## 1. 原参考先验与共同base：通过

原图为 `0≤g(a,t,s,α,β)≤1`，参考为同一个 `σ_A×ν²×µ_H²`，mean为m。positive tuple只要求某个真实输出cell满足

    b=a+L_ts(β−α)+O(E₀)，
    L_ts=((t−s)I₂; −[M(t)−M(s)])。

这里 a 是共同coarse observed code，不是未经证明的共同exact fine point。原code内细点差、proxy误差已经进入 E₀=Kr。全部g相关性保留；不将原endpoint或time/角边际重新假定独立。

原used-H有κ-cover、Frostman upper及slab upper，不能由heavy subset自动取得逐点κAD lower。A/root及B主稿当前均明确修正；下面提取只需slab，未使用未付的lower。

## 2. 四变量CS给16边质量：通过

固定a，把g视为t,s,α,β四变量非负函数。对每个变量取两copy、所有16个corner乘积的box积分，逐变量Cauchy–Schwarz给

    Box₄(g_a)≥(∫g_a)¹⁶。

再在a上用Jensen，得到总质量至少m¹⁶。对常数函数取等，指数正确。它不是density自动给一个大Cartesian子集，而是同原产品参考中的有限copy质量；原atom重数不影响证明，也不要求变量分离。

每个正权box的16条边均为原positive codes，故分别有真实输出cells。没有声称这些不同codes的细路径可以在同一exact点或同一原管上拼接；所需结论仅在共同coarse a和误差E₀下成立。

## 3. 横截角、四clock分离及合法base：通过

令 `v=α₁−α₀`、`w=β₁−β₀`，在原µ_H⁴参考下它们独立、各有原差law的slab upper。`|v|<λ`包含于一个宽Cλ的固定slab。其余|v|≥λ时，`|det(v,w)|≤λ²`迫w距span(v)至多λ，固定v后再次用原slab。故坏角概率≤`C_γK_πλ^γ`，要求λ≥q_base。

四times有六个可能的近碰撞；对每对time条件化其中一个，interval cap给坏概率≤CK_tg_t，要求g_t≥d。因box权≤1，按原reference删除坏事件即可，各自费用不能改成未经证明的条件边际。取

    λ=[m¹⁶/(C_γK_π)]^(1/γ)，
    g_t=m¹⁶/(CK_t)，

并将常数取大，保留box质量≥m¹⁶/2。存在满足base的λ/g_t是显式条件，不对任意有限图免费成立；实际small-loss与更细source base的相容性已在稿件说明。固定单一frame以后也不能继续把它当正维角population。

## 4. frame恢复、符号及一致性：通过

对同一time-edge，A稿用两输出差得到 `L_ts(-v,w)`；root用反号的第一列得到 `L_ts(v,w)`。两种约定均正确。det下界λ²、原角有固定bound，故逆frame norm≤Cλ⁻²，而非免费λ⁻¹。因此恢复L_ts的误差为

    O(E₀λ⁻²)。

其top block是`(t−s)I₂`，bottom是`−[M(t)−M(s)]`；没有假设矩阵差满秩。若除time-gap恢复secant，须再付g_t⁻¹，误差为`O(E₀λ⁻²g_t⁻¹)`。root现稿明确保E₀=Kr与两项费用，不把它写成无损O(r)。

同time-edge的angle四角因原差结构构成O(E₀) parallelogram；固定angle-edge的time四角因同一M的coboundary结构也构成O(E₀) C4。后者确是共同matrix-time数据，不是任意非平面增量law自动给的关系。原误差在有限次相减中只增固定倍。

## 5. 有限box与可迭代闭包：边界证明通过

有限star只给从同一a出发的16个输出，不保证某个输出还能作为下一原作用的input。因此不能从`a+d₁,a+d₂∈A`推`a+d₁+d₂∈A`，也不能把固定box质量当成所有bounded operator words的小image。

A稿M=0的有限star校准足以否定该逻辑跳步：取有限不同times和横截角，令A只含0与该star的有限输出，最大正水平分量的增量d存在而2d不在A。此例不满足whole-M非fit或完整source分布，稿件未将其用作主反例。

F₂ⁿ正交关系的另一个边界也正确：density≥1/2；若U′×V′为complete rectangle，则两span正交，故`#U′#V′≤2ⁿ`。所以一般dense relation不自动包含两边均近满指数的Cartesian作用域。固定大小CS盒与大rectangle的区别被准确保留。

固定times及base再向角应用energy时，单凭image≤#A只给`E(H)≥p²#H⁴/#A`，按#H³归一为约`r^(2−κ+O(η))`。该已有计数不产生small-loss BSG参数。它不是实际energy的upper，A稿明确区分；若有更强energy必须另用时间/作用结构证明。

## 6. He自然lift的适用条件：通过

对照He Theorem3，operator family必须逃离所有proper nonzero invariant subspaces。将4×2的L_ts补零列为End(R⁴)时，vertical W={0}×R²被全部operators映到0；自然shears亦共同保持W。该escape条件直接失败，不能由whole-M非affine或D-plane cap补出。

对照He–de Saxcé Theorem1.1，V须属于P(G)，即Jordan–Hölder中无trivial constituent。自然shear群逐点固定vertical W，并在horizontal quotient R⁴/W上作用恒等，因此该representation具有平凡constituents，不满足所需条件。即使secants遍历全部Mat2，这个表示障碍仍在。

直接以secants作用R²也不由nonfit保证irreducibility：M(t)=diag(t²,t³)的whole affinefit质量在均匀fine time上≤C(√h+d)，但全部secants都保持两坐标轴。该例只检验定理假设，未提供原A/g闭包，未被称作主反例。加入dilation或换lift可另研究，但原g尚未给这些新增operators的共同input域与迭代small-image，不能免费扩代数。

## 7. 平均carry结论与main边界：通过整合范围

B主稿的平均carry门槛在原ν²×π上证明；root摘要保持了time-prefix domination、angle-prefix slab upper、harmonic digit weight及同g仅付1/m的责任。该结论不是单tuple失败，也不把原digits当独立。

positive比例raw overflow只迫真实非负乘法的向上carry数量，不迫不同修正值的熵、observed fibre数量或输出增长。root现稿明确允许修正相关/相消，并不排除其他signed-digit算法。其余独立carry细审由本轮另一review承担，不将本人的自查重复登记为该核心的独立审查。

## 8. 下一KT种子：定义范围、条件算术与baseline

对照[Katz–Tao原文](https://arxiv.org/abs/math/0102135v1) Definitions5.1–5.2、6.1：K(n,d)是任意固定ambient R^M中，实参数n的saturated(n−1)-direction collection及finite saturated shading的union计数陈述；shading饱和首先是总质量约N#T，不是逐管完整单位线段。原`≈`记号容许N^(Cε)费用，后续需按ε任意小的量词展开，不能只当log损失。

四维Hausdorff结论、任意ambient集合的dimension≥4或方向集推论，尚未在本项目推出这个单尺度任意shading种子。nextspec已明确把OAI4量化输入、任意ambient投影、separation/重数、线段长度、shading平均到逐管及uniform损失顺序全部列为待证；没有把它们写成现有定理。OAI4完整证明亦保留未全面独审条件。

Theorem6.2准确为

    K(n,d), K(d+1,d′) ⇒ K(n,(2n+1+d′)/4)， 0<d<n。

若强种子K(4,4−ε)及保shading的随机thinning转移都取得，取n=6、经典起点`d≈7−2√2`使d+1>4，并取d′≈4，则得到`17/4−O(ε)`。17/4=4.25大于经典KT六维值`7−2√2≈4.171573`；这一比较和算术正确。该经典值来自原Theorem1.1的Hausdorff公式，不把Minkowski或maximal指数混入。当前未做最新六维全部一手前沿与新颖性认证，有限搜索无结果不能承担此责任。

nextspec还把K(4,4−ε)到更大实方向维的随机thinning、并保finite shading列为未证步骤，当前审查没有将其当已付monotonicity。在n=5、该迭代第二输入至多d+1且起点≤4时，`d_new≤(12+d)/4`的固定点为4，故所述路线ceiling=4，不是五维full机制。

因此下一spec仅确定一个值得检验的有限种子桥，未启动或完成R29证明，亦未登记17/4为新界。上述量词与未证责任列明后通过。

## 9. 最终审查范围

本轮已付共同base的有限原作用盒与平均进位门槛；没有付可迭代operator action、actual AFF₃或固定>2增益。停止observed/BSG/自然shear/仅carry数量的无新输入细修，符合当前macro要求。长期高维/一般Kakeya目标保持active，最终标准不降低。无真实Kakeya反例、维数改进或重大/新颖性认证。
