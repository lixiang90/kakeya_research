# R0050 working specification：一般smooth nonlinear coherent lift

> **R0050范围更正（2026-10-17）：** 下文保留开轮/历史论述。对目标 `w+F(t)y`，在同一个参数点沿同一条lift直线取第一变分，可构造同codimension和方向rank的真正全时affine lift。因此一般smooth与affine的**存在性等价**，旧文“空间affine为实质限制/一般nonlinear未排除/需逼原π affine”的判断不再成立；原π本身仍可真正非线性。完整更正见 [R50主证明](../../notes/20_dimension_lifting/curved_lifting/R0050_variational_equivalence_and_full_smooth_lift_classification.md)，当前登记为 `results/reviewed/LIFT-005_full_smooth_variational_classification.md`。不新增ID或重大性声明，换clock/selector/Θ依赖w等边界保留。

2026-10-17，Goal active。已运行context.py→tmp/R0050_context.txt，读GOAL/STATE/ROADMAP/registry78全部状态/latestR49/AGENTS/R49round/next；R49 HEAD=origin=remote59d261395f39a5d4302c9bb243c1829c64034c22/tree2d77f3ead106d144962cceaa75d805c8c6acf6e9/732files/clean及receipt全项核。上一turnprogress：真正原质量/亏损账本与附加类core改变后继并同步。R49已提前macro，本轮关键失败后macro，常规R51。

## 1. 当前唯一命题

固定B=diag(1,2)。在非退化含0的I和有内点的y,w∈R2、ρ∈R共同参数域，问是否存在smooth π_t:R3→R2、a(y,w,ρ)、Θ(y,ρ)使rankD_zπ_t=2、rankD_(y,ρ)Θ=3且

    π_t(a(y,w,ρ)+tΘ(y,ρ))=w+(tI₂+t²B)y

对所有原参数和整段t成立。Θ独立w；同一曲线的全部ρ须一致；定义域容纳整线段。π_t允许一般空间非线性而保原clock。验收完整构造及全部rank/coherence，或整个smooth类no-go。局部finitejet相配不够。

## 2. 排重、合法闭包与总目标

旧LIFT005只π_t=T(t)z+c(t)，已完整且冻结；新class严格更大，旧rankB条件不能不经新rigidity推出。以非线性坐标拉直π会弯原straightlines，不能偷用仿射结论。局部开放域restriction保rank/coherence；不假selector w(y)、不换clock/少ρ/降rank。它不是旧uniformshading正幂命题的改名；平均/逐管density及高维逆向归约均不自动产生。

真lift可按具名source从4D直线输入给某3D曲线结论，应用须另付原global/boundedchart量词；no-go只排降低维度机制，不解一般R5。全过程不预认证major/novelty/Goal完成。旧general→sticky/coarseentropy、HRZ/cyclic/CP/BSG/action/carry/AFF3等冻结保持。

## 3. 源和独立反攻

实际源为已存Nadjimzadah2609.06299v1 Def2.1/Prop2.2/2.5及R12三稿；2511.10918/GAFA00750-4是另一文。R49官方v1核过，不重做完整globalfrontier。必要有界primary比对新rigidity/构造的已有性，不把未命中当无已知。

可用Θ满秩方向坐标v、D_w a rank2，但D_zπ(a+tv)依赖w/v，不能旧共同右逆。反攻quadratic/nonlinearπ、kernel/foliation、混合w/y/t导数、through-point direction子流形、三阶t必要条件与实际全时解析，所有identity须同一a、Θ、π。测试B0/非nilpotent rank1旧可行例、标量B时间改换例和diag1,2，不能误排旧合法例。

## 4. 分工

root主稿/meta/state/route/registry/统一Git。A仅notes/20_dimension_lifting/curved_lifting/R0050_nonlinear_lift_source_and_rigidity_audit.md及research/reviews/R0050_geometry_and_source_review.md，原source/全class必要约束及独审。B仅notes/20_dimension_lifting/curved_lifting/R0050_nonlinear_lift_construction_counteraudit.md及research/reviews/R0050_construction_and_rank_review.md，独立构造/反例/完整rank与coherence攻击。最多两互补代理、不Git不spawn不编辑他人文件；formal需root/main/macro/next齐后实际全文审。

## 5. 一轮停止和保存

若仅旧affine障碍改写、先加未证affine/foliation假设、或没有超旧类的真实新约束/构造，停止并macro，不续Taylor阶数/阈值/clock参数。若有真新结构证明但未解本class，仍明确剩余并依一主轮规则决定，不把所需新引理塞假设。新结果reviewed须独立逐步审，一手比对后再判意义；未经外部同行评审。每轮完整归档/验证并沿R49父safe sync，Goalactive，目标不缩小。
