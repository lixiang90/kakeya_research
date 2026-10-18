# R0089：几何cut与原质量的独立终审

2026-10-18，A。仅对下列实际全文及明列的有限数学范围作内部逐步审查；本稿恰六个编号二级节。未经外部同行评审，不认证未来元数据、Git或同步。

## 1. 实际全文范围、来源与独审分工

本次正式审查前已fresh实际全文读取root《R0089_original_shadow_cuts_degree_budget_and_graininess_boundary》十节、A《R0089_cut_propagation_and_degree_reduction_audit》十节、B《R0089_original_incidence_and_graininess_counteraudit》十节，working_spec五节、终macro六节、next六节、source scope六节，以及阶段I的A/B两篇各八节。未用旧版阅读记录代替本次终稿全文；阶段I尚未锁题的历史措辞与后来的spec锁题分开。

A自己的主证不计自身独立审核；该主证已由root/B实际全文逐步独核。本formal的独审对象主要是root整合与B的真实坏gap、有限图及II反攻，另核它们与原质量、源量词和最终范围是否一致。

Guth1402.0518v1本轮本人实际读intro/Hyp0.2、Prop0.3、Th0.4/0.5、完整§1及§2.2的Th2.2/Lem2.3–2.5证明，并读§3 Th3.1/3.2相关投影面积段；已对照本地提取文本。本人没有重新view PDF、验证源字节或全文重证后半§4曲率graininess。Stone–Tukey、relative isoperimetry和标准面积公式仍是具名基础输入；root的文件身份/渲染与B另读的Yomdin等来源不冒记为本人独立完成。

## 2. 同一shift、原I与删选分母

root§2的共同格桥成立。对任意Lebesgue可测原Yi，Fubini给EKξ=δ^-5|E|及EJξ=δ^-5I；单位roundδ管每个δ-clock slab只容固定个格点，所以Jξ≤CJ/δ，端帽亦计。删Kξ>C0λ^-1δ^-5|E|的phase，坏概率≤λ/C0；用Jξ的统一upper控制其承载的期望质量，取C0足大后，同一个good phase保Jξ≥cλJ/δ。这不是分别选两个有利shift。

再按实际row访问数筛重、取固定空间颜色并重新筛重，确保原selected edges总数≥cλJ/δ、余管数J′≥cλJ且每row访问在[cλ/δ,C/δ]。所有格点仍是原Yi点；相应cube可超出E，故没有偷用NδE或把cube并当原E。label restriction保方向分离upper，但不保字面满角网，后续仍须支付原J/I与剩余J′。

平均版直接从总I运行该证明，不先假每个原label满足逐管密度；逐管版当然供应总I，但两者不被无费反向混同。root§5的两次degree分桶与peeling也成立：row桶的原A2边数控制低row阈值总损≤A2/4；K1个原column及A2≥K1ρ/L控制低column阈值总损≤A2/4。余图只是上下常数／polylog可比的selected incidence图，不授whole geometric degree、局部横截或全空间multiplicity。

## 3. 全n cut与原edge法向面积核算

源Def1.1的cut要求附近全部合法球的signed-volume近二分，强于仅交零集或只二分Q。细格ham-sandwich以固定cut尺度r0可给D≤C_r0 K^(1/5)；r0若随δ变小，不能藏其负幂。Lemma1.6的纵线rootcount／投影体积证明确对固定任意ambient有效，但仅控制两个外anchor之间O_r0(D)个坏gap，未给坏clock或原质量。

独核root§4：去偶重数并取符号边界regular部分不增加degree；cut与relative isoperimetry给每个相互分离Q中的H4面积≥cδ4。有限原edge角和在该面积上的平均，允许选一个实际法向nQ使角和≤Cδ^-4乘相应面积积分。对每根原fixed-fat tube，纵向面积公式加a.e.平行线至多D个根，给积分≤CDδ4；异常整含零面的纵线只有零测横向参数，不能把a.e.交点数直接逐原axis使用，但这里实际以整个横截面Fubini，合法。

因此Σ_(i,Q)∈A |nQ·vi|≤CJ′D，坏角原edge比例≤CDδ/(λθ)。由K≤Cλ^-1δ^(-4-γ)，Dδ/λ≤Cλ^-6/5 δ^((1-γ)/5)，可取θ≤Cλ^-3/5 δ^((1-γ)/10)。η最后足小使其为δ正幂。这是同一原图的标准mass-averaged hyperplaniness，不是每Q uniform或每管完整Lebesgue结构，也没有付沿原tube的法向coherence。

## 4. 两跳预算与有限非启动证书

R3 Th2.2的实际输入是逐管／逐格访问近均匀及每格相对任一方向的定量两向横截。Hyp0.2/主graininess另有全空间multiplicity upper及三方向条件；root/B没有混写。源§2.2的rank-balanced anchors、相隔足够远的横截Bernoulli事件及对全部原T′的错误平均，均是真实质量步骤，不能删掉后引用原结论。

R5系数维数≈D5、每seed约D个anchor时，独立seed预算只有≈D4；在最有利均匀模型中目标row的期望命中尺度为Mvis²D4/K。由此试图触发远多于D个anchors，需要D³≳K/Mvis²。这仅是显示算法的预算要求，不是全部多项式的次数lower；K的upper也不能倒作每一原输入的lower。现有读出不能推出spec要求的任意小ε次数。

root§7／B(3)有限证书亦成立：固定非seed row至多接触4Mρ个其它rows，条件该row未seed后其邻row仍独立；若两row共享column≤B，hit≤BX，触发需X≥ceil(D/B)。Chernoff与union bound给J(CBM²D³/K)^(D/B)，其适用需相应base<1并使该上界趋零，例如base为δ正幂且D/B≫logJ。甚至赠seed整row都certified，若没有首个新row，单靠相同阈值认证的后来代不能开始。seed数预算亦可与该事件同时保留。

该证明只限制独立seed及graph-certified触发规则，不排P偶然cut、相关seed或其它几何。原近角pair的B可很大，所需充分条件并非H5已知输入；不能用它宣所有更多hop或原H5不可能。

## 5. 两个实体桥反攻、coarse出口与来源边界

独算B§4／root§8的强cut长gap例：固定r，先使sign-sin在所有相关半径≥r球中的偏差小，再在所需固定横向盒上以P0一致近似，保严格cut余量。对P_H=P0+A t(H-t)/H²，取A>8||P0||∞，H远大于两端anchor-cluster长度及r^-1，端部扰动可任小；中间[t=H/4,3H/4]却全正。degree固定、端anchors可远多于degree，一个坏gap仍可承载几乎全部clock。这严格反数量自动变质量，但不满足原满方向小footprint，不否H5，也不指称源§2.2犯了该错误。

对Z={x5=x1x2+x3x4}，每个graph点及每个q(w)=0的方向给真实整直线；四个坐标w张满tangent，而II在小固定盒内仍非零、signature(2,2)。故R3 tangent二维的三条不同null方向逻辑不能按线性span照搬tangent四维；其leading cone又缺原full S4，仍非H5反例。

这些核算没有得到共同coarse4-plane、原clock/密度、方向caps或原N/I返回。δ依赖高degree零面也不能免费当fixed-format G3/G4输入。source scope把全n工具与R3主定理、实际局部proof与未新独证的高级wholeproof分开；Crofton比较的局部排印方向不以讹传讹，也不借此否源主定理。

## 6. 最终有限判定、宏观与停止

上述终稿全文在明列的有限范围内通过；无未解决强制修改项。通过的是原Lebesgue-to-grid质量桥、已知全n cut应用、原edge局部hyperplaniness、有限认证算法证书与两个实体桥反攻及它们的范围。不是通过完整H5的任意小degree/coarse主门；该主门仍未证未否，未得到ordinary新界、完整branch-saving或full方向低维反例。

已实际全文核终macro六节、next六节及source scope六节：四完整路径继续开放，DIM001/R38/R80已付部分不伪列新gap；本轮直接cut-degree-graininess门停止，不续更多hop、D/λ/ε/r或赠quadratic-spread/全局multiplicity公设。保守ordinary/fullbranch-saving streak12与有实际费用信息并不矛盾。当前无qualified下一gain主命题，不冒记已锁新题，也不把困难作external blocker。

不新增数学ID或major声明；Goal active，未经外部同行评审。A正证由root/B独核与本稿对root/B的独审分工保留。本文不认证源全40页wholeproof、未亲自读取的辅助论文、未来元数据计数、提交或同步；按授权写完本formal即停止编辑检索。
