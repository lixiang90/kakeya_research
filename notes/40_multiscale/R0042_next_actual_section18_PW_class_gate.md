# 下一唯一main：实际§18的加强PW极值类是否闭合

2026-10-17。R42已完成macro和新BS输入可用性测试。该任务是达到高维目标的一个有界必要接口测试，不把长期Goal降格为closure引理。不是已经选择的新颖方法；若下述差异不能成立，一轮即停。

## 1. 当前命题与全部量词

固定d=5及BS给出的固定复杂度指数A_5。以WZ Def17.1原joint4-AD/CW和平均δ^η shading为基础，考虑另外带真实whole-tube probability law的类，要求所有半代数S（presentation复杂度E≥1）、所有0<λ≤1满足

    ν{T: |T∩S|≥λ|T|} ≤ C δ^(−η)(1+E)^{A_5}|S|λ^(−5).

BS只保证原finite direction-separated满δ方向网的PW条件，**不保证任意anchors的joint4-AD**；其能否同时满足或经合法提取进入原joint4-AD/CW加强类，是另须支付的输入责任。已有joint4-AD/CW的满方向网可由BS补PW，但不能据此覆盖一般Kakeya。某个 arbitrary Def17.4输出也不能被追认为这种祖先的后代。定义K_{5,PW}(κ)时，κ取这个**加强类**的极值，必须说明初始真正Kakeya family如何进入，以及对原平均shading的量词，不借旧K_5的极值偷换。闭包目标：在任意ε/最终η0、δ0/g/h层级下，实际原§18操作均能选择保足够原质量的输出，使所有后续极值调用留在同一PW类，代价相对新尺度为可任意小次幂，复杂度指数受固定d与初始A_5控制，不随迭代深度无界增长。

这是待证命题而非新假设。先测试fine-scale PW的加强类；若coarsening失败，不准悄加all-coarse PW进定义后把原闭包命题标通过。若另提all-scale类，初始输入、共同parent、迭代与strictgain均须真实重新支付，本轮不另开第二主任务。若原κPW不能保持所需量词，需给精确失败，不可仍调用原κ。即使闭包成立，full(3,3) κ≤ζ、其它mixed、一般到sticky和Hausdorff仍各欠证明。

## 2. 先做合法闭包与双向排重

先逐项表：原ν质量、wholeclock length、共同frame、coarse representatives、从pushforward到unweighted count的双边比较、shading refinement、每次调用K_d的新δ/η/κ。root R42式(3)给共同affine/crop C'=C r4/(p q4)，不能把coarsen/reweight/pertube frames也宣布付清。

若所有输出仍保满4维多尺度angleFst，PW只是再次调用BS，不把inheritance登记新机制。平行translations校准证明PW不强迫angleFst，但不证明原§18需要更宽类。只有实际操作在anglelaw失效而PW仍可合法保留，或真实随尺度增长complexity使新BS起实质作用，才说明有不同于旧anglelaw的输入。平均density与逐管tail分别核，归一化mass分母不可消失。

## 3. 实际必须读和计算的操作

versioned WZ PDF65–80的Def17.1、Prop17.2/18.1/18.2全文：起点、Step1至后续步骤、(106)–(113) coarse/unweighted与parent multiplicities、排除multilinear和最终k-planar/ell-linear升级。记录每次common affine/可能projective与tube replacement；真实polynomial presentation在pullback/union/thickening后的复杂度。不得只读相似toy操作便声称actual输出闭合。

可独立攻击：同一原tube给多个coarse输出；均匀化只控制incidences不控制whole-tube prior；shortclock产生q^(−4)；细管只能转移到N_ρS而非S；coarsecardinal与原mass不成比例；迭代complexity exponent增长；不同parent使用不同pullback S。每个例子必须标明是否保完整实际来源，toy不升级为主命题反例。

## 4. 主尝试、结果出口与一轮停止

若闭包通过，须再定位一个实际半代数测试S，写出原逐管/平均intersection、|S| upper、E与其fixedκ预算；仅写“χ+Aθ+5u<κ则矛盾”不构成新增定理。若没有实际S，结论只能是可用输入未产生新gain，不自动追加第二轮参数优化。

若某个实际操作不能闭合，保存该操作的精确量词/费用或保source的反例，立即冻结当前inheritance路线。不得用lowcomplexity envelope、paidseparatedancestor、conditional-smallSr作为附加公设救回相同命题。无信息的等价改写不新增ID；按全局任务重新选择真正不同输入。两互补审查、相关验证、安全同步照常，Goal保持active。
