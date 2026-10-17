# R0043：原质量、复杂度与实际闭包的独立全文审查

2026-10-17，lifting_obstructions。实际全文阅读并逐式审查：root《R0043_actual_PW_coarsening_and_extremal_class_closure.md》10节、A《R0043_actual_section18_operations_audit.md》10节及修后全文、root《R0043_macro.md》8节、下一《R0043_next_actual_polynomial_grain_test.md》4节。对照原WZ(19)/(20)、Def3.6/3.9、Obs3.2–3.4及§18(104)–(145)对应操作；本审查不是本人kernel稿的自审。BS及原结构推导仍保具名输入责任；未经外部同行评审。

结论：**以下有限转移与修正后的有条件PW携带范围通过。** 不能据此认证原无界local-AD类的免费局部化、原§18全部grain几何proof、五维κ≤ζ或普通高维Kakeya；本轮没有strict gain。

## 1. 原law与此次必须保留的范围实修

finite kernel允许任意非负原权、重复indices、subprobability和无界位置。但actual无权递归必须用同一T的uniform counting probability，或真实支付counting law对所给ν的domination；仅“存在一个whole-tube probability”不够。root已将R42该表述明确修正，没有认证字面任意law的加强类。

parent概率质量的取消还需固定bounded joint chart或显式总count N≤CKδ^(−m)。原Def17.1字面R^d及local AD不自动给这一点；原Obs3.4(22)确实使用了总count量级。root现在将有界规范列为新κ_PW类的条件，并保留无界限制未证。若仅所有原marks已在固定box，active tube参数有界，平均density λ0给N_active≥cλ0N，故N≤CKλ0^(−1)δ^(−m)；parent费用多λ0^(−1)，实际λ0为小幂时可如实支付。这里没有反过来声称global marks可免费移进一个box。

## 2. 任意原子族、共同平移与所有微小λ

root(1)从tail≤min(a,Bs^(−n))积分，完整处理B≥a、B=0及a=0，所得 B^(1/n)a^(1−1/n)正确。高访问粗事件的原preimage H先固定，H允许与S、管参数和以后选择相关；没有独立化、换prior或漏掉归一化分母。

核式 k_R≤2^(n−1)k_(R+δ)*k_δ 对R≥δ点态成立：|y|≤R时整个B(y,δ)处于B(R+δ)。同一横向u用于整族，clock不移动。对每个S−u使用上述restricted mean，再积分u并约去a，正给λ^(−n) tail；没有ρ/δ、λ、权跨度或index数损失。所有translates体积与presentation复杂度不变，没有把其无穷并作为一个新测试，因此固定指数A不增长。

dyadic tube截面内外球比较、coarse轴O(ρ)偏差和normalized volume比较均只花维数常数。用内接fine graph及外接coarse graph两次比较的方向正确；不需要N_ρT在parent内部，不删clock端部，故不能以tinyλ反驳该证明。N_ρS直接论证的缺口在此确实补齐，而非通过添加all-coarse公设回避。

## 3. 无权coarse与whole-parent的准确费用

occupied parent finecount n_j∈[K^(−1)L,KL]给

    (uniform coarse mass)/(pushforward mass)
      =N/(J n_j)≤K²。

无需先知道N的全局量级；这一步不把incidence权误当tube计数。T′若经删选，必须使用T′自己已证明的AD lower。原law不是uniform时，cardinal AD不能替代weight比较。

在§1有界/总count条件下，p_τ≥cK^(−2)τ^m，clock-preserving ψ_τ的volume factor τ^m与真实parent mass抵消，得到C_parent≤CC0K²；parent后按同一参数树粗化再付K²，合为root(6)的CC0K⁴。ψ参数取原dyadic cube的lowercorner，原树精确送到新树，中心只作kernel截面比较；两者已分清。共同描述basis若旋转，仍携带原树或其共同image，不偷换任意新网格后沿用occupied-bin lower。短clock的q^(−m)费用没有被消除。

## 4. 实际§18、relative mesh与新极值的条件范围

Steps1–3的shading/incidence refinement不自动重设whole prior；删整条tube则如实付p^(−1)，p≥c fλ0只用原平均density，不要求每管或每parent都dense。原uniformization另证T′的AD，这是无权化实际所需输入。

此次指出并已实修的关键层级点是：(107)/(109)调用原T_ρ,Y与原T[T_ρ],Y；其PW/AD费用为δ^(−O(η))。不能把T′较大的δ_ell^(−O(η_ell))塞进ε1≪η_ell的早期调用。(110)通过Y′≤Y及原multiplicity uniformity回传。该修后说明保留两种不同frozen laws，没有免费给所有parent逐管density。

relative mesh预算 δ′≤δ^χ ⇒ δ^(−Bη)≤(δ′)^(−Bη/χ)正确。χ先定再选η；原18.1有真实τ/ρ power gap，18.2的a_j backward power schedule可按有限维数预留。极近endpoint的scale不机械调用新极值估计，trivial AD数量付入原δ^(−ε1)误差；固定绝对mesh端点常数也由δ充分小吸收。内部多层point剪枝不等于每层whole-law条件化，真正tube替换次数受维数控制。

κ_PW必须从同一有界uniform-PW加强类的failure sequence出发；infimum端点通过先取一个有效κ′<κ_PW+ε/2再留ε/2合法，不借旧κ或任意现成Def17.4配置。以上足以支付所列操作的新增PW责任；其余结构推导、Lemma4.2/5.3等仍为明确条件输入。原PDF70/72的Δ_J文字不一致没有被伪修成一条完整grain证明；本轮只使用明确的最终D_{δ_ell}[T_{√δ_ell}]管操作。

## 5. 真实Sδ测试及不能夸大的复杂度结论

原marked cube仅intersect T，不能直接以cube体积作tube intersection。root修后Sδ取固定邻接扩张；有限着色后，接点附近的互不交小球在bounded-slope管内各占≥cδ^n，即使在clock/截面边界也有固定体积分数。因此真实平均M≥δ^(Oη)，体积和presentation计数只增固定倍。不同管可选不同heavy color，因为同一Sδ已含全部扩张；没有私设每管测试。

PW给体积lower除以P(Eδ)，但已构造cell/grain presentation的复杂度上界仍很大，未得strict κ余量。所选presentation的大上界不是所有可能envelopes的复杂度下界；root没有以它宣布所有曲面策略不可能。本轮通过closure，不通过高维gain，也没有新维数界、反例、新颖性或重大性认证。

## 6. Macro、下一任务与停止边界

macro准确停止kernel常数、网格和先验命名的局部循环；不重新开启冻结的CP⇔PM、BSG/action/carry或fineflatflake。PW较满维angle law更弱的校准只说明适用类较宽，不能当五维增益。

下一spec是一次actual growing-degree ruled-grain测试，不把低复杂度包络作为假设：P须来自真实保留times上的f近似，h_j须来自原offset分片；piece数、degree、same-S/分别测试方式、p_j/λ_j和shortclock费用都要支付。dyadicLip不等于C²，ρ²的coarse一致性不能免费用到e≪ρ²；原point/tuple prior也不能直接换whole-tube prior。已有Lemma20.2的matrix-affine/Taylor及Lemma19.2小variation分支须先排重。

这些是待施工量词，没有被本review证明。若一次实际尝试只回baseline4、缺原mass关联或degree费用吃尽saving，就停止该envelope路线，不续参数小改。formal审查至此完成，无待作者修复项；只按上述有限及有条件范围通过，Goal保持active。
