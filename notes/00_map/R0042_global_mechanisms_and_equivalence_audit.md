# R0042：高维机制、四维输入的信息量与等价排重

2026-10-17，B 宏观独审。已运行 context.py、读固定入口/registry78状态/R42 spec/R41 nextgate，实际回读 R13 coupled interface、R9 weighted direction proof及 R38 出口范围。只编辑分配文件，不 Git，不开新代理。本文是路线及输入审计，不登记新结果ID，不以建议替代高维证明。

## 1. 总缺口：三类不能混作一个已解问题

长期目标仍为 n≥5 的 Hausdorff Kakeya、真反例或经文献认证的重大中间结果。当前四维内部 argument under named inputs、有限读出及任意 ambient 种子已付，六维17/4是接原 KT 递推的明确条件/引用链；是否已有相同直接 statement、能否称新界/重大，仍需独立 primary 证据，不能因有限检索无命中就认证。

五维 actual WZ 各 mixed case 不是一般 Kakeya 的全部：即便逐一证明 κ≤ζ，还须保持原 general-to-sticky、极值配置、重缩和 Hausdorff 归约责任。已完成 ell2 affine/部分 proper alternative 不给 ell3 矩阵增长；Q-cycle line 也不是原 translation S-line。原 joint tube AD4/CW 不等于 direction-separated family。

构造支路同样没有真 power seed。R41 实际 lower 只排共同 clock/可分离 placements；一般 coupled intercepts 的 S_r 并未被证小。不能把“需低 S”当新公设，或把高 S 本身当反例。R40 global fine flatflake gate不能泛反所有 fixed-loss/coarse 策略，但没有新原质量机制时也不重开它们。

## 2. 四维有限输入真正可给的原 law 信息

取 bounded R4 graph lines L_i(t)、原概率权 ω_i、uniform δ-time mesh D=δ^{-1}，每方向 δ-bin 总权≤α。引用已付 DIR-003：对任意逐线 marks≥δ^{η_0}D 的子族，

    Σ_i ω_i #J_i ≤ C_ε α δ^{-ε} #E。               (1)

这是任意数量/重复 indices/任意正权的有限结论，η_0 随 ε 而选；不是仅一个固定集合的 a.e.-t 维数结论。定义原 incidence visit cell 的概率 law μ。对任意 cells 集 A，q=μ(A)，删 #J_i<qD/2 的 rows 只损 q/2。若 q≥2δ^{η_0}，(1)给

    μ(A)≤C_ε α δ^{1−ε} #A。

所以对所有 A 都有

    μ(A)≤L #A+2δ^{η_0}，  L=C_ε αδ^{1−ε}。          (2)

取 A={cells c:μ(c)>L}，可得 Σ_c(μ(c)−L)_+≤2δ^{η_0}。于是 μ_good(c)=min(μ(c),L) 是删去至多 2δ^{η_0} 原质量的真实 subprobability，且

    ||μ_good||_∞≤L，   Σ_c μ_good(c)^2≤L。           (3)

这是 smooth cap/energy 信息，不只一个 support lower。若 α≤Kδ³，得到四维基准 L≤C Kδ^{4−ε}。它同时适用于原未归一化 incidence restrictions；若 actual law≤G(ω⊗uniform time)，cap和删质量分别乘 G。若再把质量 m 的 selected law 归一化，必须将 cap与error均除 m。没有假定 conditioning 后仍为独立时间。

该推导完整支付了 R13 单块固定集合 a.e.-t 工具没有提供的有限 prior/shading 量词，但它实质已在 R9/R38 的专用 zero-depth 信息范围内；不能在 R42 把重述(2)登记新方向。尤其 fixed-power 小 conditional fibers 的 m 分母会花掉同阶信息。

## 3. 为什么仍不能免费得 shared-time joint gain

R13 的实际双块 Π_t=A_t⊕A_t 保同一个 t 和固定耦合 P。固定第一输出后的 parameter fibers 随 t 变；原 finite(1)并未把这种条件族变为一个独立于 t 的真 line family。可以用 domination 做未归一化删选，但不能抹其归一化质量或重建 time law。

即使两个或若干 R4 projections 均有(3)的近满维 entropy，也只给 joint≥4维基准。固定一个与有限所选投影均横截的4-plane，在其上取平滑概率就能有每个投影的四维 cap，但 joint 仍4维。此例只校准信息不足，缺 full五维方向，不是 Kakeya/CP反例。

要推出4+σ，仍须利用实际 straightline/direction graph 的新兼容信息。若所谓新 entropy/energy 命题对所有原 dense P_j 统一成立并给正增益，必须检查是否由旧 universal CP再次删选就推出，反向亦然。R15的 CP⇔存在正gain PM 已付；不能以不同 multiplicity 阈值或 conditional entropy 名称重复开同一主命题。

因此“把(3)对两个 marginal 各用一次”不是当前可推荐的完整 main。新四维工具足以作为真正 uniform finite input，但下一步需要的 joint 兼容估计尚无独立证据。

## 4. 新 primary 的准确新增范围

本轮在线实读 [Binyamini–Salant2609.24135v1](https://arxiv.org/html/2609.24135v1)（2026-09-21）Theorem1/Corollary2及相关 Props3.1–3.2。其 semialgebraic 特例为：direction-δ-separated tubes，S 的复杂度 E，逐管 relative intersection≥λ，则

    |S|≥c_n #T λ^n δ^{n−1}/P_n(E)，                (4)

P_n为固定 ambient n 的多项式；不再有旧额外 δ^ε。真正新增的是对复杂度的定量控制与任意 λ 预算，不是对任意小集合的 Kakeya 结论。一般 o-minimal 的未定常数不能自动当 poly(E)；需要 #o-minimal/semialgebraic 的有效格式假设。全文高级证明仍由 root另定必要范围，不在本宏观稿认证。

方向分离是必需的原 hypothesis。WZ T 的 AD4 在 joint tube-parameter space，不能免费换成方向 α≈δ⁴ 的 family。甚至 jointAD4/CW 校准族可以由满4维 transverse translations 的平行管组成，只有一个方向；该例不保正κ/slab的全部来源，只说明这两项本身不送所需方向结论。

## 5. 可保任意原权的 BS 平均形式

这是(4)的直接应用计算，不作新颖性声明。设有限 tubes 可重复、原总权 W，方向bin权≤α；S仍是同一个真实复杂度 E 的集合。记 θ_i=|T_i∩S|/|T_i|，M=Σω_iθ_i。固定有限 coloring 后，同色各bin任选 θ_i≥s 的一条原 tube；其 directions分离，故

    W_s:=Σ_{θ_i≥s}ω_i
      ≤min(W,C_n α P_n(E)|S|δ^{1−n}s^{−n})。

对 0<s≤1 积分，n>1 时

    M≤C_n W^{1−1/n}
       [αP_n(E)|S|δ^{1−n}]^{1/n}，

即

    |S|≥c_n δ^{n−1} M^n/[α W^{n−1}P_n(E)]。        (5)

W=0平凡；否则所有数量有限，权重跨度无损。(4)的当前 main statement允许任意正 λ，故无需低s截断；若调用另一仅λ≥δ的版本，须另保 Wδ error。这里保 M 的 n次幂，简单 heavy-filter 会给较差的 n+1次幂，不必把那种损失冒充必需。

原 law 可未归一化，α/W比例和 M/W平均 density均真实出现；conditioning mass分母并没有被“多项式常数”消掉。S 的复杂度也必须是 actual presentation 或已付外包络的复杂度，不能把原 visited cells 的巨大并自动视为低度对象。

## 6. 当前最有希望的可证伪接口及硬停止边界

新BS给出了区别旧CW/AFF3的实际格式预算，但尚未看到完整source到(5)的低成本桥。比在最终 T 上免费恢复方向分离更值得优先检验的是：从最初真正 direction-separated 的 finite Kakeya family 携带 polynomial-Wolff bound，沿**原 general-to-sticky 的实际抽取流程**回传，作为未归一化 law 的额外 invariant。projective/affine 变换可使最后方向坍缩，却不必破坏已从原 separated family 付出的几何估计；这必须逐项证明，不能由新名字当作假设。

该候选须固定原 finite family、原 shading、真实每次 parent restriction/重缩/normalization及输出来源，量化所有 semialgebraic S、复杂度 E、intersection λ 的新常数。目标只在已付 loss 为 subpower 时声称 poly(E)×subpower 控制；若原抽取只有任意 AD4/CW family、并无真实 separated ancestor，不能套用。也不能仅证明抽象变换引理后就宣实际输出满足它。

一个可证伪的费用校准：原总权1、direction-bin α≈δ⁴，保留 whole-parent 原质量 m，4个横轴除 r、clock piece长度 q 再除 q。若新平均 intersection 为 λ，则原 M≈m qλ，原体积 Jacobian 为 q r⁴。(5)给新体积 lower 的因子

    (m/r⁴) q⁴ λ⁵/P_5(E)。

wholeclock q=1、m≈r⁴ 时 parentmass/Jac 可取消；短clock却仍有 q⁴。因此不准把 arbitrary short-piece 的 PW 常数说成与原一样。真实 source 的 affine/projective Jacobians、piece lengths、mass 与 complexity 都要算，若只剩 q^{-4} 固定幂成本且无saving支付，即应判该转移未闭合。这与R20费用警告兼容，不是再做同一toy。

即使此 inherited-input gate 通过，后续还须付**真实原 law 的 direction/format 共同预算**，而非添加 low-complexity envelope 公设：

- 必须实际构造 finite T'、原权、S，证明原 marks落于S且有已量化 M；
- 证明方向bin α的真实尺度，以及 S 的 E，不只 tube jointAD或native单个低次 test；
- 比较(5)和原 |S| upper。若方向损失记 χ、复杂度 E≈δ^{−θ}、density损失记 u，则必须实际得到 χ+C_nθ+nu<κ 的严格余量；W及 group mass不得遗漏。

这可对真实 all-directions construction 的 finite seed、或一个实际 source family做；两者不得互换。单个低次 native polynomial 不给整个 E 的低复杂度，global AD/CW也不给方向分离。若这两项只被当作新假设，则本次桥没有建立，应立即停，而非继续 palette/threshold/blur改名。

仅作为校准：若一个完整direction-separated δ-net 的整管均在semialgebraic S中，|S|≤δ^κ，则(4)迫 E至少有一个固定幂增长。原FD叶族 presentation本来可以很大，不矛盾；这个初等复杂度必要条件自身不达成Goal。它也不证明所有 power构造的实际 lower。

### 6.1 追加排重：PW不等于方向上界，但共同affine回传可能完全重复它

严格区别的校准族是 T_a={(a,t):0≤t≤1} 的δ-tubes，a取[0,1]^4的δ-grid。它们 bounded-overlap，所以对任意可测S，Σ|T_a∩S|≤C|S|；若每管intersection≥λ，则 |S|≥c #T λδ⁴≥c #T λ⁵δ⁴。它满足比半代数PW更强的测试，常数O1，但全部方向相同，方向Frostman4常数至少δ^{-4}。这个例子只判定输入类严格不同，不保positiveκ的全source。

另一方面，若真正ancestor有所有尺度的dir-Frostman4，后续只有共同affine/crop、未归一化restriction和加权Dρ pushforward，则new方向bin可由old角cap直接得到同一费用，重新调用BS便已给PW。仅把同一计算叫“PW inheritance”没有新增高维机制。

为核实际流程，已另读原§18 Proposition18.2 Steps1–6及18.1升级到(145)。所读流程用whole-tube transverse affine normalization、coarse DρT、uniform X'重新计无权coarse tubes及两尺度Kd再调用，而非免费保原conditional prior。若每个coarse parent的fine原权双边可比共同值，则无权coarse law与原pushforward可比，all-scale角cap也能继承；须先检查是否仍是同一原方向信息。

可能有独立内容的是 **PW extremal class** 的实际闭包；先测试当前 fine PW 能否经原coarse操作保持，而不是先加入全部coarse PW。上述平行族说明PW严格弱于dir-Frostman。然而 T_ρ∩S较大不迫对应fine tubes也与S相交，只能粗推它们与N_{Cρ}S相交，后者体积不必与|S|可比。厚度、λ与格式费用必须真实核。若fine闭包失败后把所有coarse PW直接加入定义，部分closure成为tautology；即使仍需支付祖先、uniformization、parentmass及Kd recurrence，也不能用这个定义扩写把原测试标成通过。

另一个不能隐藏的初始责任是 jointAD lower。显式取 ε=M^{-1}、δ=ε²；逐坐标 A,B∈{0,…,M−1}，令 v=εA+δB、b=εB。方向遍历完整δ-grid，#T=δ^{-4}（单位角分离只需固定倍网格/coloring），但 joint(b,v) 为 ε-separated。r=ε/10 的 occupied parameter ball 只有1点，4-AD lower 却要求 K^{-1}(r/δ)^4≈K^{-1}δ^{-2}，对小 loss K=δ^{-η}不成立。因此BS只把该满方向family送入PW测试性质，不能同时送入原jointAD/CW加强极值类；真正 Kakeya 输入到该类仍要付归约，不能追认为已证。本例不是高维Kakeya反例。

## 7. 宏观建议与停止结论

目前没有证据让旧 shared-time positivegain、低S、genericcompletion、AFF3 或 fineflatflake以新名复活。R38的all-prior finite信息可严格写出，但仍只付四维基准。新BS的无ε/poly(E)输入只在真正不同的actual-source闭包/format预算处值得一次反攻；共同affine下已能由all-scale角cap重做的inheritance不单列main。是否有可执行main，取决于 root能否指定并真正支付上述原流程和对象，不能仅有形式 χ+Cθ<κ。即使独立的PW闭包通过，也不是完整五维 κ≤ζ，必须保留这一范围。

root最终选择一主轮测试实际§18的fine-PW加强类闭包；已实读其main8节/macro8节/nextspec及A7节，正式review见 `research/reviews/R0042_mechanism_and_scope_review.md`。这只是一项原流程可证伪门槛，未保证五维正增益。若预算没有原来源或fine闭包失败，不能改定义救回；继续寻不同 primary/实际结构，不造新ID、不以路线分类当数学成果。一般维度目标和完成标准保持不变。
