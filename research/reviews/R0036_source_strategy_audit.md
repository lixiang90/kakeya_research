# R0036：source 路线的收益、余责与有界继续条件

2026-10-17。强制 macro 的独立意见，不是新数学结果。已读 GOAL/STATE、R0036 working_spec、R35退出文件、R29 finite seed 主稿；实际读原 OAI4 §7–11 的结构、主要 statement 与依赖接口，以及原2.17的输出/positive horizon终步。只编辑本文件，不Git，不自动开始下一条 lemma 的证明。

## 1. 当前收益与不能跳过的总缺口

TCM/ASM/TEX/CRP/AIM/ISO 形成了一条可复核的真实源前端：原坏问题的优化、actual candidate conversion与完整 isotropic候选已经有内部双审，且 ISO 同时支付 scalar zero horizon Cor6.9。R35的主要信息不是另调一个网格常数，而是清掉一个完整分支，并为后续 scalar projection提供独立输入。它的价值是减少共同 source 条件、暴露真实 prior/precision接口；它仍是已有来源的复现，不能冒称用户要求的重大中间结果。

长期目标仍缺 n≥5/一般维数真实 gain。当前有两条不同未闭合链：

- 高维 finite seed/KT 出口：R29投影与稀疏加权桥已支付，但要使用 SRC001/DIR003，仍要排掉原 j2 **全部** optimized narrowness，并核完整2.17/finite readout。ISO只有ℓ=0，不是四维 finite theorem本身。
- 直接五维源模型：AFF3、真实 vector growth/actual matrix-time action的closure仍未支付。ISO 的二维/三维基底 conic与planar dot-product机制没有自动增加维数；R1–R28的冻结账没有因新源证书失效。

连续六轮 source 审计有真实累计信息，但尚未产出无条件新高维界。继续的正当性必须来自一项**可完成的整分支责任**和明确高维出口，不能把“下一节还没审”本身当研究理由。

## 2. ISO 不能单独把 R5/R6 的条件删除

原2.17（PDF20–25，文本1066–1328）输出的是 version2、j2、C(d)、H>0。full three-slope density用于 initial horizon及归一化，但 statement没有断言其 maximizing sequence的optimized ℓ=0。原 positive horizon终步用 `m(r0,u0)≤K0 q^{-3}` 与 `m≥N0^{σ/2}`，只迫 H≥σ/6；没有把所有narrow情况压回isotropic。

原结尾（PDF168，9031–9053）明确分三类：ℓ=0用6.1；0<ℓ<∞用8.4/8.5及9.2/9.5/9.6；ℓ=∞用10.1。故不能只把6.9插进2.17就声称 finite四维种子已证。若试把 j2投影为 j1再免费补一个kernel维度，就重开已冻结的投影/乘积跳步；标量投影保持full-time labels和质量的责任恰是8.2以后要做的工作。

即使额外宽松地假设scalar H=0已经给任意ambient的finite3D种子，单用 d′≈3 的KT递推，在n=6的输出也只有 `(2·6+1+3)/4=4`，不是17/4；不能把不存在的finite4D输入放进第二参数。j2 ℓ0本身又不是所有四维direction-rich输入的统一finite定理。因此没有从ISO直接得到R5>4或R6=17/4的合法快捷链。

## 3. 原 §7–11 的真实依赖图

下表是实际读过的statement/interface图，不代表本轮已重新证明这些结果。

| 责任 | 原页/文本 | 真实用途与尚需验收的量词 |
|---|---|---|
| §7 retained-edge planar tools | 页109–117；5803–6280 | 7.1三路径保原edges；7.3共同endpoint sets与scalar-generated closure；7.4 flat coefficient law；7.5 weighted collision→parallel strips；7.7把真实line-incidence row拟为affine–skew。不能只得小sumset顶点而丢原g/edges。其可证性有额外planar first-coordinate cap与scalar参数law，不被旧generic vector BSG数字边界直接否定。 |
| Theorem8.2 scalar mesh projection | 页118–120；6309–6479 | 直接使用6.9，输入是fixed ν、raw active mass、所有depth的 mesh caps和terminal occupied count，输出disjoint whole-trajectory labels/full-unit-time quadratic fits、每label质量 `c a^d β/K`。无角输入时先crop制造角增益；有角时β∼1。noise/tag common prior、crop weights、full-time extrapolation及回原µ_act mass必须完整付。 |
| 有限ℓ的几何比较 | 页121–137；6481–7332 | 在原α、γ groups中保c及support预算；8.4三wideinterval→actual candidate，8.5否则变horizontal k=ℓ；8.6/8.7/8.8付hidden-sheet affine approximation、bounded residual/fine states与nested slopes；8.9给full-time coefficient counts。只读statement不能追认这些为已认证。 |
| horizontal critical/subcritical链 | 页137–154；7333–8252 | **9.1是Lemma，不是Theorem9.1**，只是simultaneous floors；真正完整分支为Prop9.2（2k=1）、9.5（2k<1参数尺度bootstrap至endpoint G(2k)）、9.6（2k≠1返回wideinterval）。G(u)要求每dense input/子列、同prior、fulltime assignments/predictors及原marginal floors，不能把一次existential predictor迭代成全称endpoint。 |
| 无限ℓ整分支 | 页154–168；8255–9029 | Prop10.1以两nested true systems构造fulltime thin charts，balance原质量/面积，投影8.2，再做原p1-known actual atlas、coverage与finite-sample exclusion。**它不调用§7或§9**；新共享输入只有8.2。 |
| 完整reduction/读出 | 页20–25、168；1066–1328、9031–9053 | 原2.17要连同outer slope measure/finite witnesses、六系数平滑、cap-class crop、positiveH全部核；R29只对finite读出接口作了条件性审查。最后尚需把所有源certificates的量词与原任意集合/finite-sequence输入统一，而非假“集合dim=4⇒任意finite估计”。 |

§10的依赖位置已逐项查过：2.13/4.3在8276–8323，10.2在8347起，10.3在8434起，3.4与4.6 finite-sample接口在8557–8599，10.4/10.5在8626/8756起，唯一scalar theorem调用8.2在8867与8895，最终3.4/4.12在8956–9028。没有发现暗用7.7、8.4/8.5或9.x的引用。它因此可作为一个相对独立的完整余责，而不是必须先顺序审第7节。

## 4. §11 没有藏着已完成的高维 KT 推论

实际读§11.1–11.6（9056–9295）。其中：

- §11.1只是从四维Hausdorff满维推出同维packing/Minkowski满维，不是uniform maximal estimate。
- §11.2（9073–9080）明确仅 `dim_H E≥4` 对所有ambient d≥4，证明是固定四维orthogonal projection保每V内单位方向。原文也写full conjecture仍要求d。
- §11.3的任意方向集界为R4内部 `dim_H E≥1+dim_H D`，具名Keleti–Máthé；它不使ambient五维direction family的投影fibres免费贡献维数。
- §11.4–11.6是固定曲率Nikodym、固定phase curved与rank-one三维quadratic curved transfer。Nadjimzadah lifting在此用于**较低维曲线**，不是ordinary Euclidean R5/R6 full-direction unit lines。

未见原§11调用KT6.2或声称>4的一般ambient下界。R29的17/4链是本项目另行拼的conditional后果，仍须其明列的arbitraryambient/unsaturated seed与KT量词。上述本地结构检查不认证2026文献新颖性；R33有限primary前沿调查的保守范围保持不变，本轮不以搜索无命中替代新颖性证据。

## 5. Source 路线的可支付收益与真实成本

若直接继续有限ℓ，需一起支付约页109–154的45页：retained original edges、scalar closure/flatness、fulltime scalar projection、三interval比较、horizontal normalization与critical/subcritical bootstrap。它是一个完整的几何branch，但不是一两条现成lemma的拼接；其中保留同一prior与bootstrap endpoint是实质反攻点。只完成7.1或9.1不能称此分支有新gain。

一个更小且完整的source cut是：**8.2（约3页）+完整10.1（约14页）**。这可独立消掉ℓ=∞并支付finite分支也要用的共同scalar gate。其核心不是重新做5.6，而是把6.9从exact问题转为当前finite weighted/shaded trajectories的fulltime、same-prior、可实际回收标签，并在unbounded outer sequence中区分tangent K与每fixed-i实际K0。

已发表的WZ5.2/CV1可以作为具名已知定理；statement与application已核，不应为“所有依赖都检查”而无限递归重证其高级proof。**GWZ2026的新原input与OpenAI完整source则仍严格列未验证**：本项目已核其statement/application、没有因此认证全proof，不能借与已发表WZ/CV并列而清除条件。KT具名递推仍保R29的确切hypotheses/量词和源排印接口责任。当前必要未验证路径因此是OAI4其余branches、原2.17/finite读出，以及新原GWZ等所列条件；不是机械要求所有标准文献的全部proof都重新写过才能结束。

直接五维路线目前没有本次新引入的不可替代primary theorem。R28实际action/g、R27 plane cap、R24–26 scalarization gates、R21 polynomial tubeKT都已到明确边界；新选“共同time/更多angles/更好density”若只是再次调用旧全称结论即为旧正gain等价改名。没有新原假设或可调用joint theorem时，它们不应仅因source进度缓慢而解冻。

因此本审计的优先建议是有界继续source整分支，先选择8.2+10.1；不是从7.1自动续页。root若选择直接五维，须先指出一项冻结后真正新增的source信息及不等价目标，不能只重述未付AFF3。

## 6. 推荐下一唯一main：完整无穷窄度排除

候选命题可写为：固定原version2 C(d0),d0<1与S,η，取CRP maximizing sequence，H→k>0，若其global optimized narrowness ℓ=∞，则每必要subsequence上的substantial original-path residual，经合法whole-layer/known-atlas normalization，在further exact subsequence产生一个固定正深度 c′>0、time exponent→0的**原p1-known** atlas，覆盖≥ppath/logN0，列表/slacks是实际(Kpath logN0)固定幂，复杂度落预声明guard，矛盾k>0。输入8.2必须在本main完整重证其所有上述finite hypotheses/output，不能只写“scalar H=0所以可用”。最终命题是Prop10.1完整结论；8.2是共享中间责任。

合法closure核查：

1. µ_res≤µ_prep只保caps/support upper；每次投影始终除固定 `q_Aν_γ(A)`，不按当前残余归一后假新AD lower。global residual质量需经原 `Σω_γq_Aν_γ(A)≤1` 平均找到某dense A。
2. time-pair采样的Jensen只给原paired law；fulltime chart label必须包括normal、**center intercept与velocity**，在每当前p1由actual later Q2恢复。仅近parallel normals/几何交线不等于source label knowledge；R6中心运动toy只反少这项的弱化版，不能代原10.2审查。
3. C→A normalization的absolute primed f′(0)可能很大。10.3实际用terminal equality与intermediate one-sided formula抵消到ν(A)/J_A，而非假归一后仍n′(0)∼1。不能解冻R10的restricted-optimizer n0闭包猜测来代证。
4. greedy candidates需保whole trajectory assignment，finite插入数来自每条最多q_A duration的原prior预算；eventualcoverage来自every-substantial-residual矛盾，不能从一次N^{-o(1)}成功直接声称固定比例覆盖。
5. actualcoeff bin/PDF3.4 matching与4.12回收必须按原unnormalized µ_c/rawπ收费，先声明guard再取N0晚样本。analytic K、outer-i常数及N^δ不能直接当actualpathslack；SCL绝对幅度障碍仍禁止事后调网格。

排重：此命题不是已证ISO或AIM的逻辑等价改名。ISO不处理ℓ∞；AIM有限ℓcandidate conversion未给fulltime localization、mass/area cancellation或原标签回收。10.1也不蕴含尚余finiteℓ：若通过，仍需独立7–9链。故其通过会减少真实source责任，而不会因把剩余内容重命名就冒充解决全部高维问题。

独立反例测试应集中：tiny A/current-mass conditioning、large absolute density shift、two-time known-label center motion、prior-preserving common jitter undo、从short-block到unit-time的合法Remez、posterior较大无效label替换、posthocguard与boundedcomplexity顺序。必须保原全部hypotheses才算source反例。

停止条件：完整8.2+10.1通过双独审，或找到一处保原法则/权重的严格gap/counter；任何单个localization小lemma通过不登记整branch。若连续两轮只能重复同一未付转换且无新数学信息，立即停止这条source局部迭代并macro，不再改阈值命名。即便通过，也先重评剩余finiteℓ成本与6D出口/novelty，再决定是否付最后约45页，不自动承诺逐节走完。

## 7. 本轮意见的边界

本macro没有证明8.2或10.1，也没有新高维数学结果；它给出了一个比自动§7续审更短的完整source候选、明确的依赖cut和停止线。若root选择另一完整任务，本文件只保策略审查记录。最终Goal不改变，R29 conditional flags及全部冻结账保持。
