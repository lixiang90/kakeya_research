# 唯一下一main：四维输入到Katz–Tao定量种子的合法转移

2026-10-17，R28提前macro后选定。长期目标仍高维/一般Euclidean Kakeya完整解决或认证重大中间结果。这里优先核可望产生六维中间界的具体有限输入，不再局部改写mixed43 observed/BSG。

## 1. 精确定义，避免把Hausdorff结论当成有限种子

原始文献KT《New bounds on Kakeya problems》§5 Definition5.1/5.2、§6 Definition6.1与Theorem6.2，本地literature/extracted/katz_tao_2001_v1_new_bounds.txt；官方https://arxiv.org/abs/math/0102135v1。原文N≫1，在任意固定ambient R^M（常数允许依M），lines方向N^-1分离；实参数n允许非整数。saturated (n−1)-collection有约N^(n−1)条线，且任意角capθ≥N^-1内条数≤N^o(1)(Nθ)^(n−1)。saturated shading是总质量约N#T，允许N^o(1)损失，**不是**每条整线或固定正比例可见。

K(n,d)断言所有这些配置的shaded union cardinal≥N^(d−o(1))，原文用ε及N^(Cε)记号。R29开轮须重新展开全部量词，包含ε到常数、ambient、bounded box、querybase及near-full-average shading到逐管的合法删选。不要把原文o(1)理解为只有log损失。

OAI4 Theorem1.1给四维集合Hausdorff结论；§11.2已给ambient≥4集合dim_H≥4；§11.3方向集推论也仍是集合结论。它们尚未在本项目推出上述**任意ambient、实方向维、单尺度任意saturated shading**的uniform K(4,4−ε)种子。Theorem2.17及全部weighted输入需逐项核；不能把投影、紧致性或‘dim_H=4’一句当作这个桥已付。OAI4本身仍为未全面独审条件输入。

## 2. 为什么该定量桥值得核：明确的条件算术

KT6.2：当0<d<n，K(n,d)及K(d+1,d')蕴含

    K(n,(2n+1+d')/4)。

以下均为条件路线算术，未取得任何新界。若先有uniform arbitrary-ambient K(4,4−ε)，随机thinning一个n−1≥3的angular-cap集合应给K(n,4−O(ε))，n为实参数；这一步也必须证明并保shading，不作为已付输入。于是n=6取仓库已核KT经典起点d≈7−2sqrt(2)，d+1>4，若上述转移全付，则d'≈4代入得17/4−O(ε)。17/4=4.25，严格高于仓库既有六维KT基线7−2sqrt(2)≈4.171573。最新全前沿与新颖性必须另做完整一手比对，有限搜索没有结果不能作优先权认证。

这个递推单靠四维种子在n=5的固定点上限为4：若迭代第二输入至多d+1，则d_new≤(2n+2+d)/4，固定点(2n+2)/3，n5恰4。因此不把本路线说成五维full证明机制，也不承诺种子桥成立。n6的条件收益是检验方向，而非已登记结果。

## 3. 可证伪主命题与分工

下一唯一main：从OAI4实际已声明/可核的量化命题，证明所需K(4,4−ε)或实际足够的K(d+1,4−ε)种子；若无法推出，给出精确量词缺失、严格有限边界模型或可核不适用判据。主证明必须保原angular cap、线段长度、ambient、separation、shading质量、输出覆盖及损失极限顺序。任意ambient随机投影到R4需给small-image方向/短线/多重数的真实质量预算，不能免费假preserve Frostman。

Root审OAI4定量陈述与实际推导；A审arbitraryambient/方向及合法restriction、independent反攻；B核KT递推使用位置、shading/真实参数及最新六维一手基线。最多两个互补代理，先写working spec再开始。此R28文件仅确定目标，未启动R29证明或把前端缺口登记为新定理。

## 4. 停止与重开规则

一轮必须得到真实finite种子、严格边界/量词障碍，或找到有具体出处且实质不同的定量输入。不允许连续只换ε、投影维数或thinning叫法。若核心只剩Hausdorff⇒uniform finite这一未证跳步，则freeze并重选；不得把冻结projection+kernel免费加维复活。

R30常规macro保留，关键失败提前。mixed43/其余五维cases及general-to-sticky/Hausdorff所有旧缺口仍存档；本路线目标直接针对维数提升，不更改最终标准。每轮独审归档、安全同步GitHub，Goal active。
