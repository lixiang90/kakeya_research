# R0116 独立审查：uniform 全clock仿射 codec

2026-10-26，algebraic_gate。未参与本轮codec机制提出、有限certificate或Monna施工；本代理另作Spread-out I宏观准入稿，不属于本审对象。仅编辑本审查文件，root统一整合Git。内部独立审查，未经外部同行评审。

## 1. 实际读取、待核版本与判定

实际读 `research/rounds/R0116_uniform_clock_codec_working_spec.md`、当前GOAL/STATE/路线及R115 next；读R92算术transfer/precision两原稿的有限域、primitive方向、uniform格与marks范围。随后全文读作者 `notes/50_counterexamples/R0116_actual_direction_construction_gate.md` 九节，初读raw SHA256为

    33a257aa73e1c334cd89f4a0911902514bae51d19ab7497479b7ff7b1c59037e

独立重算全部tuple、scalar估计、非coordinatewise目标空间三误差、exact分类及Monna校准；作者修订后已再次实际全文读回。**最终通过，无未解决必修项。** 最终锁定末节实际读回hash，不认证之后未读改动。

唯一提出的边界精确化是§8的dense像：若“ζ-dense”按到像的inf距离定义，c无连续性，inf未必取到。作者已补先取任意 `ζ'>ζ` 的midclock近似见证，再令 `ζ'↓ζ`；证明的lower不变，包含 `ζ=0` 而像不闭的情形。这不改定理或机制。

## 2. 全原量词与tuple合法性

主对象是同一个任意函数 `c:Z_p→[0,1]`，仅端点 `c(0)=0,c(1)=1`，对**所有**a,b,t的一个uniform误差。不给连续、可测、injective或homomorphism。所有输入关系先在Z_p中计算，实输出仅作凸权加法；不能把实数系数与p-adic系数默认为同一域。

独算tuple表，按(a,b,t)次序：

| tuple | 原Z_p中结果 | 真实RHS |
| --- | --- | --- |
| `(0,-1,-1)` | 1 | `c(-1)^2` |
| `(1,0,-1)` | 2 | `1-c(-1)` |
| `(0,1/2,2)` | 1 | `c(2)c(1/2)` |
| `(0,b,2)` | 2b | `c(2)c(b)` |
| `(-1,b,2)` | 1+2b | `(1-c(2))c(-1)+c(2)c(b)` |

第三行只在odd p用；2在这些Z_p中为unit，所以1/2合法。p2分支从未使用1/2；任意even z的z/2及任意odd z的(z-1)/2都在Z₂。负号、2及所有所需b均未离开单位球。域内点不必是实区间中的正数，这不会妨碍输入合法性。

odd下三个tuple固定即可给统一lower；p2给定midclock见证z后只需前两tuple及与该z对应的一个tuple。exact parity的**全函数**分类则是对所有b逐点应用此关系，不把一个有限样本检验说成已经检查了全部Z₂点。

## 3. Scalar不等式、sup和端点

令每个tuple误差≤ε，写q=c(-1)、r=c(2)。range保证q,r∈[0,1]，前两行给

\[
 1-q^2\le\varepsilon,
 \quad q\ge1-\varepsilon,
 \quad r\le1-q+\varepsilon\le2\varepsilon.
\]

这里只需ε<1；ε≥1的情况已经满足所求lower。odd p第三行给 `1≤r c(1/2)+ε≤3ε`，所以 `ε≥1/3`。端点与range全部实际使用；若去掉它们，本审不授同一下界。

p2 even行给 `c(2b)≤r+ε≤3ε`。odd行的实表达为q(1-r)+r c(b)，其lower至少q-r，因此

\[
 c(1+2b)\ge q-r-\varepsilon\ge1-4\varepsilon.
\]

若c(z)在半径ζ的midclock窗口，even情形迫 `ε≥(1/2-ζ)/3`，odd情形迫 `ε≥(1/2-ζ)/4`。统一保守取四分母正确；本审不为优化这一常数另开证明。

误差函数的两个值均在[0,1]，所以D(c)有限且≤1。每tuple误差当然≤其sup，即使sup不达到；作者采用任意 `ε>D(c)` 后下降取极限也合法。没有借紧性、极值取到、可测选择或极限函数。c可逐δ完全改变，三个固定tuple的估计仍逐δ成立。

## 4. Exact p2必须保留的例外

ε=0时，even与odd估计分别迫c=0、c=1，所以parity是唯一候选。核其对**任意**a,b,t都成立：t even时原仿射组合模2等于a，t odd时模2等于b；实RHS对应权重c(t)=0或1，确实只选择c(a)或c(b)，不是把任意mod2相等提升为实相等。

parity满足端点但不供中间clock；尤其 `c(2)=0≠c(1)+c(1)=2`，它不是到R的unital ring map。故不能用“无field embedding”一句替代作者的实际分类。odd p无exact解和p2的例外均已付。

## 5. 非coordinatewise H：三误差逐项审查

H任意从Z_p^d到Rⁿ，固定pair输出距离D₀>0。令L(a)=P₀+a(Q₀-P₀)，用输出单位向量v作同一个实线性投影h(a)。域内L(a)对所有a合法；Q₀-P₀不必primitive，证明也未除其p-adic范数。

对原pair(P₀,Q₀)用t=a，确得 `|h(a)-c(a)|≤e`，且h端点0、1。h本身可在[0,1]外；作者没有错误地把scalar range lemma直接套h，而是继续恢复c的defect。

对原hyp再用pair(L(a),L(b))与原t，输入严格为L((1-t)a+tb)，投影残差≤e。替换左侧h为c花e；原关系残差花e；右侧两项替换的总费用是

\[
 (1-c(t))e+c(t)e=e,
\]

因为c(t)∈[0,1]。故D(c)≤3e正确，没有把两个右端误差误计成无权2e，也没有用一对anchors就免费补全所有新pair。

由此odd得e≥1/9；p2在midclock条件下得 `e≥(1/2-ζ)/12`，实际含midpoint时为1/24。若只知道像在inf距离意义下dense，用近似见证后极限也得对应lower。D₀始终固定为同一pair的输出距离，不能在tuple间调分母；D₀=0的塌陷与非塌陷pair的相对误差没有混淆。

去掉wholeclock条件后，p2的parity与只依模2 residue-vector的finite-image H确为exact例：t的parity只选择P或Q的residue，real权重也只选择同一个输出。这准确显示midclock条件不能删。constant H同样不能被当作非塌陷例。

## 6. Monna校准：compact满clock与大defect同时真

M_p读p-adic digits为实base-p digits，c_p(t)=M_p(-t)。共同前k位相同后的实tail差≤p^{-k}，所以M_p连续；负号是Z_p自同胚。每个实y∈[0,1]选择一个base-p展开，y=1取全(p-1)，按同一digits读成p-adic -t，确得满射。Z_p本身compact，故不存在用不闭像或端点缺失解释失败的漏洞。

独算 `c_p(0)=0`、`c_p(1)=M_p(-1)=1`、`c_p(-1)=M_p(1)=1/p`。tuple(0,-1,-1)的误差正是 `1-p^{-2}≥3/4`。这给一个同时连续、紧域、满实clock而uniform仿射关系失败的实际校准。它没有生成全部Euclidean方向的unit segments，也没有低维upper；本审不把满射clock当Kakeya构造。

## 7. 旧R92、restriction和主Goal范围

R92审的是实际Euclidean同格算术轨道、短primitive方向代表、field/ring计数及真实marks费用；本轮审的是任意单一codec对所有p-adic affine tuples的uniform intertwining。当前有限certificate不重跑或否定R92已付的有限转移与弱Hausdorff返回。

最关键的反攻范围通过：实际source/构造所用的稀疏相关tuple族不一定包含这三个证书；合法restriction可能正好删掉它们，Haar平均误差也不由sup lower控制。按line/tuple分别选codec更已改变hyp。因此本稿只排uniform-all-pairs接口，未排actual sparse source、全部p-adic路线或所有非coordinatewise构造。

这里没有一族原Euclidean T、原N/I及shading正gain。无新ordinary维数界、完整source排除或重大结果；内部通过不完成长期Goal。固定误差门及显式校准是本审唯一确认的数学范围。

## 8. 最终读回凭据

作者在§8补入dense像的inf未取到说明后，本代理已再次实际全文读回九节、重核修订段，并真实运行Get-FileHash。最终主稿raw SHA256为

    b044a044e23e32bcb32c2b383964cfd40dff1fd3d0a4118b857a0f5cbc31f331

修订给出任意 `ζ'>ζ_δ` 的见证后下降极限，确实覆盖dense但非闭/非满射的像，未改其余证明。以此版本通过本文件所列内部独立逐步审查，无未决必修。主稿若再有实质改动须重审；换行规范化导致raw bytes变化应另记。通过范围仅uniform-all-pairs固定误差门，不含actual sparse source或一般Kakeya。
