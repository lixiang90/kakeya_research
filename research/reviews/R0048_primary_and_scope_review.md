# R0048：现行primary、真实终点与原质量接口的独立审查

2026-10-17，A。已实际全文读 root《R0048_actual_HRZ_terminal_and_original_shading_boundary》8节、B《R0048_HRZ_recursion_and_finite_seed_counteraudit》8节、macro8节、next5节和working spec；自己的primary稿不计独立数学审查。另读本地HRZv1 §4、alg1/alg2及§8对应段，并实际打开JHU官方PDF核声明及PDF33–35接口。**通过本文所列的source/接口校准与停止范围；没有通过H5、完整HRZ重证或general-to-sticky新归约。** 无必须修改的数学问题。未经外部同行评审。

## 1. Primary当前状态及版本scope

官方arXiv1908.05589当前history只有2019-08-14的v1；但作者机构primary明确AJM144(6)(2022)1511–1560、DOI10.1353/ajm.2022.0037。root/A均实际打开JHU官方43页PDF，Thm1.2、Thm4.1、tiny式(51)–(53)/PW接口与库v1所用段对应。v1四维表1.4794...与官方PDF1.4854...确不同，稿件没有冒称整份bytes相同或把2019表当2026最优。

CLI下载Win10013/403与web读取成功是两件事；root没有accepted新PDF bytes，故没有伪造离线归档/hash。A不认证尚未写出的metadata。OpenAI当前官方tree/blob核验明确归因root本轮authoritative逐级JSON：paper.pdf为45ec20e423db2a9c70fd6303510bac361e6e9e8a、1371486 bytes，与库同；不能将先前两个失败入口误记为最终未核。

有限前沿只提供实际打开的声明范围：GLX2025 Table1的n5=18/5、n6=7−2√2；已付条件4D finite链下项目n5基线4、n6条件17/4。BS exact-PW、LPSW codim2、WZ sticky3/4D、Moreira四维maximal参数均未直接覆盖本轮H5。无命中不认证不存在/first/best；RED已付内部assembly不被重新列为欠账，具名外部定理与内部审查/外部同行评审仍分开。

## 2. 真实HRZ递归终点

root §3/B §§2–3与本地source一致：cellular为r/2，algebraic为r^(1+ε°)，不是将文本分式误读成r²。alg1/2保原ambient δ管、TCI切向及whole-tube broad/计数账本。Properties I–III、(45)–(47)、(51)/(52)不自动保原shading在每entry中的密度。

tiny-dom最终某m≥k，未必m=4；即便m=4，管仍在Rn，曲面坐标未必保straightline。§8终点为δ^(−O(ε°))δ^n(#T[O])^(p_m)，之后是PW最大leaf计数及插值。公式里的n没有降成m，p_m=m/(m−1)亦不是一个可由集合dim4直接替换的黑箱。上述不是提前认证HRZ所有高级proof，但精确核出了本轮要替换的实际接口。

R12/R13旧k4 broad/narrow/planebrush数值已在三稿中明确排重；不把重算p>4/3或21/5当本轮新成果。

## 3. DIR原权weak-pruning：正确但非新的正幂输入

root §4/B §4的证明逐步成立。高重数集E_L上，light indices贡献≤δ^(−1+η_D)W；heavy以其原marks/原权调用DIR得≤Cεαδ^−ε#E_L。L≥2Cεαδ^−ε时，后项≤总高重数质量一半，移项得总高重数质量≤2δ^(−1+η_D)W。任意小权、极小W、重复index不破证明，未重置先验。

原逐管密度指数η_in<η_D时，删除比例≤2δ^(η_D−η_in)正确。它只保总weighted incidence；若要每管density须另heavy，不把平均当逐管。反向以保留下来的访问量除以L返回同级DIR union下界，故这是已有uniform shading定理的合法闭包，不新增数学ID。

父包r缩放后h=δ/r，每个原index最多O(r/δ)个短clock访问，light预算遂为C h^(η_D)W_P r/δ。跨父包要原ΣW_P r_P重复预算；whole broad/tube-entry的Lp比较不能替这个账本。高次矩能集中于少量原质量，因此weak-pruning不自动保whole Lp/broad。

## 4. 原shading和整管broad的错开校准

root §5的满方向bush原marks放在[1/2,1/2+2δ^η]，δ小后合法，逐管bin数至少δ^(−1+η)。原点附近整管强重叠与原marks可完全分离。时刻t远离0时，同一δ-ball内相交原管的方向都在O(δ/t)cap中，一根(k−1)-plane便可排除这些caps的broad贡献；固定β后whole broad只可能在O(δ/β)原点区域。

所以“整管算法已经选出tiny/tangent部分，故原marks在那里仍dense”确是无效蕴含。该例原shading并集很大，不是H5反例。两稿均保留重新设计shaded算法的可能性，只列出其尚未付的原访问分裂/clock重复/逐管密度责任，没有宣称所有HRZ组织都不可能。

## 5. Flat短包的方向费用与raw-broad校准

逐项核root §6/B §6：δ≪r≪1，h=δ/r，三个切向slopes用δ-grid、法向带宽c h；实际方向经固定着色仍δ-separated。短clock≈r的pieces都位于H4的Cδ邻域，法向角≤cδ/r，满足flat切向条件，并保短段的全部marks。原m≈δ^−3/r，非满δ^−4族。

重缩后一个投影h-direction bin中，三切向各有r^−1细值，法向另r^−1，故α≈r^−4；不同粗方向≈h^−3，相乘恰为m。并集≤Cδr⁴、总piece体积≈m rδ⁴≈δ，比例r⁴不能删。DIR带α的回传量m r⁵δ⁴=δr⁴与实际尺度相符。tiny r=δ^(1−ε°)时α=h^(−4/ε°+4)，并非相对h的任意小幂损失。

对2≤k≤4，H内3维方向patch不被A个(k−1)-planes的Cβ-neighborhood覆盖，最坏覆盖比例O(Aβ)；先取β相对A小，再取h≪β，留下某β-cap含c_(A,β)m根原管。在共同cδ-ball内同时出现，给broad p次方≥cδ⁵m^p。k5时H自身为允许4-plane，不能使用该lower，稿件已明示。它排除对所有此local类统一增加固定δ^σ的raw终点改善（ε°先小于其常数余量），没有证明此族必由任意global运行选中。

删除O(δ/β)原点clock仅损短段访问比例O(δ/(βr))，却能抹去raw broad支持，进一步核实§3的质量/范数区别。以上是有原几何/原labels的合法local校准，不是H5或完整HRZ反例。

## 6. 一轮停止的范围

不重缩时短片作为unitline shading只λ≈r，tiny尺度不能保证DIR对任意目标ε所需的near-full门槛；延长/复制会改变footprint/labels，稿件没有免费补齐。一般曲面flatten可能弯线，固定degree也不送任意系数下的uniform curvature。即使完全flat，上一节方向费仍在。

直接FSD作用于原R5满方向只回δ^(−4+o(1))。本轮没有同时支付原shading、大多数父子clock、合法R4长见证及方向重数后仍留固定σ的估计；因此停止当前替换接口合working spec。它是明确免费蕴含的排除，不是对所有shaded新递归的否定，也没有新增高维界/ID/major或Goal完成。

## 7. 下一general-to-sticky gate的独立scope

已全文核next五节。它先实际读WZ2025猜想/极值类/Prop3.2、WZ2026Def17.1/Prop17.2/§18，判定输入是否早已sticky，而没有先假设已有ordinary R5归约。固定原体积deficitκ₀∈(0,1)与H5的小σ（κ₀=1−σ）区分正确。

E5*明确要求原labels/marks下的至少δ^ε原incidence、共同合法affine/window、h与δ的范围、uniform计数与去重费用、所有尺度joint4-AD/CW、dense shading以及输出固定正幂小并集/Jacobian公式。尤其κ_out≥cκ₀与ε≪κ_out是实际任务，未以普通AD子族代替。进一步coherence/slab须从已证操作产生，没有加到input作公设。

R42 digit-permutation只否无小并集假设的自动jointAD，未被冒用为E5*全反例；tiny/crop及权重去重测试适当。旧H5在部分κ₀范围会令假设为空，提取反向还需未证完整sticky theorem及deficit回传；next明确记录这些蕴含，因此不预认证新非等价定理。仍须R49实际检查全参数范围的双向关系，当前只选一个待证来源/质量gate。没有复开已冻结matrix增长/PW/η调参，亦未保证其一定可行。

本文完成后不新增检索或数学任务，等待root核终版后停止编辑。通过仅限上述原量词、已证校准、primary/current范围和宏观安排；未预认证未写出的metadata、Git receipt、下一轮命题或外部同行评审。
