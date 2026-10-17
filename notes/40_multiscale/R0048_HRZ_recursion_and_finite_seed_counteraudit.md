# R0048：HRZ真实递归、有限四维入口和短包方向重数

2026-10-17，`lifting_obstructions`。本稿只处理本轮指定接口；未经外部同行评审。不声称证明或否定五维Kakeya，也不把HRZ文献中的高级定理全部重证。Goal保持active。

## 1. 本轮命题、原输入和排重

唯一主目标H5：存在固定σ>0，对任意ε>0存在η>0、δ₀、c，使bounded R5中的满四维δ方向网、每管至少δ⁻¹⁺η个原time-bin marks，满足 `#E≥cδ⁻⁴⁻σ⁺ε`。所有限制均作用于原tube/marks，不能先把原shading换成整管。

实际可调用的四维输入是DIR003及其R29任意ambient后果FSD001；它们条件于完整四维argument及具名输入正确，量词是∀ε∃η。它们不直接提供full maximal Lp或任意λ的尖锐幂。

先实读R0012/R0013 source-check、R13 `R0013_primary_narrow_audit.md` 和 `R0013_packet_input_limit.md`。HRZTh4.1/Prop4.2的n5k4 `p>21/16`、narrow `2p−3`，以及理想unit-H4包只能给维数4，均是旧审计，不登记本轮新结果。R29新增任意ambient/unsaturated有限入口也已是现有输入。本轮新增核查范围是alg1/2的真实停止、短clock原密度和局部方向bin的费用。

反攻包括：原marks远离whole-tube broad集中点；即使代数层完全flat仍在缩放后发生方向重数；cellular/代数分支的重复tube账本。若没有可付的原质量接点，或只能恢复既有4维下界，本轮停止，不追加k、degree、radius、η参数轮。

## 2. 逐式读到的HRZ源范围

主源 `literature/extracted/hickman_rogers_zhang_2019_v1.txt`，原arXiv1908.05589v1，题名 *Improved bounds for the Kakeya maximal conjecture in higher dimensions*。已实际阅读§4–8，包括Def5.1/5.2、Lemma5.3–5.6、Th6.1、完整alg1/2和§8终止/numerology；主要定位为PDF16–36、extracted832–2299。固定复杂度polynomial partition、Guth transverse-ball counting、多尺度polynomial Wolff等高级证明仍保文献输入，不把本接口审计称其全部独立认证。正式accepted版本与v1的相同范围由本轮另一代理/主代理另核。

alg1输入始终是ambient Rn中的原δ管，在半径r₀球内切于m维TCI；Def5.2的角度是 `c_tang δ/r`，不是只知某一次切点。输出历史由cellular/algebraic字母组成。cellular半径变为 **r/2**，并非提取文本视觉上的r²；原(32) `r_j≤2^(-#c)δ^ε°`也直接核实这一点。algebraic半径变为r^(1+ε°)。

原Properties I–III分别控制whole-tube broad质量、tube-entry总数和单cell管数：

\[
 \|\sum_T\chi_T\|_{BL^p(B_{r_0})}^p
 \le C_j\sum_O\|\sum_{T\in T[O]}\chi_T\|_{BL^p(O)}^p,
\]
\[
 \sum_O\#T[O]\le C_jd^{\#c}\#T,
 \qquad \#T[O]\le C_jd^{-\#c(m-1)}\#T.
 \tag{1}
\]

其中 `C_j=d^(#c ε°) d^(#a(n+ε°))`；#a有admissible上界，#c可O(logδ⁻¹)，故后续D参数不是免费常数。cellular由每条直线最多进入O(d)个shrunken cells给entry费用；algebraic/transverse由原Guth球计数控制重复。两者均不是原Y(T)的density下界。

## 3. tiny-dom不是“四维直管终点”

alg1在 `r_j≤δ^(1−ε°)` 或低一维tangential贡献支配时停止。alg2把后者递归到更低维TCI，保每一级原δ管，并在前者支配时触发tiny-dom。其(45)含broad-Lp与L1插值，不是原marks访问量的守恒。由于切于维数≤k−1的TCI时k-broad为零，递归最终停在某个 **m≥k**；它可能是m=5，也可能小于4，不保证m=4。

§8对最终tiny cell O使用的实际终点是

\[
 \|\sum_{T\in T[O]}\chi_T\|_{BL^{p_m}(O)}^{p_m}
 \lesssim_{\delta^{-O(\varepsilon^\circ)}}
 \delta^n\#T[O]^{p_m}.
 \tag{2}
\]

它来自cell直径约δ^(1−ε°)的体积及粗重数，不是n降为m。再结合(51)/(52)、alg2 Properties2/3和Th1.4，原(53)得到max-cell-count形式，原(54)–(57)选择指数使尺度和D因子可求和。特别终点 `p_m=m/(m−1)` 是该账本的选择，不能直接以“dim_H R4-Kakeya=4”替换成某个更好的p_m。

源§8使用原direction separation的准确位置是

\[
 \#T[S_\ell]\lesssim
 \delta^{-(n-1)}
 \prod_{i=\ell}^{n-1}(\delta_i/\delta)^{-1},
 \tag{3}
\]

每管在各TCI邻域里停留长度≈δᵢ，才可调用多尺度polynomial Wolff。不能把这个原尺度方向计数，自动解释为局部归一后一个方向bin只有O(1)根。

## 4. 四维near-full输入确有弱重数入口

以下只重用DIR003，不要求full Lp。固定四维原finite incidence graph，每个index i每time-bin至多O(1)次访问、总访问≤D=δ⁻¹；先以固定次数着色消去这个O(1)。权ωᵢ>0任意，原方向δ-bin总权≤α，W=Σωᵢ。令Yᵢ为任意原marks子集，

\[
 f(e)=\sum_i\omega_i1_{e\in Y_i}.
\]

给ε>0，让η_D是DIR003对该ε的允许密度指数。存在Cε，使对所有 `L≥2Cε αδ⁻ε`，

\[
 \sum_{e:f(e)\ge L}f(e)
 \le 2\delta^{-1+\eta_D}W.
 \tag{4}
\]

证明：在高重数cells集合E_L上，称i为heavy若它在E_L的原访问数≥δ⁻¹⁺η_D。其余indices总贡献≤δ⁻¹⁺η_D W。对heavy原indices及其E_L内原marks，DIR003给heavy贡献≤Cεαδ⁻ε#E_L；而左侧总贡献≥L#E_L，故heavy贡献≤左侧一半。移项即(4)。任意小权、重复index、极小W都不变；未作概率归一或独立化。

若原每管marks≥δ⁻¹⁺η_in，η_in<η_D，则删除所有高重数cells损失原weighted incidence比例≤2δ^(η_D−η_in)。因此near-full原shading能留下几乎全部原质量且重数≤L。这是真可用的restricted weak入口，不可只因“没有full Lp”就排除所有finite改写。

但(4)不控制删除部分的Lp：极少原质量仍可支配高次矩。反过来，若对所有原shadings有这种删选及上界，取η_in<η_D，剩余原访问量除以L即恢复DIR式的finite union下界。因此其正幂信息只是现有DIR的闭包形式，不是新的H5机制/ID。

## 5. 同原shading进入递归的缺失责任

原(1)、(45)–(47)和tiny-dom为whole-tube broad law；它们本身不保证每个被保留T[O]仍在O内拥有相对短clock的near-full原marks。尤其alg1的entry重复总数可带非admissible `d^#c`；若逐entry调用(4)，删选预算须乘其**实际加权full-clock长度**，不能因(1)的Lp比较就把总删选量改成原唯一一次的DW。

一个已知类型的严格校准是原满δ方向bush：所有线经过原点，原marks只放在固定远离原点、长度λ=2δ^η的共同clock段。它保满方向与逐管原密度；但whole-tube k-broad可能集中于原点附近，远处相交的方向集中于小角cap。于是whole-tube tiny/broad选出的局部区域可以没有任何原marks。此现象不反H5，也不排除重新按原shading构造算法；它只说明“原整管decomposition已有，所以原shading自动落入终点”不是证明。R13已审过相同责任，本轮不登记新结果。

若真改写为shaded broad，仍需支付：原broad质量与原总访问量的分裂；narrow剩余的实际空间和时钟；每次cell/ball重复的原长度；在每个要调用DIR的局部包内逐管或heavy平均密度。现有(4)能在这些费用已付后使用，不自动供给费用。

## 6. 即使完全flat，短clock方向重数也有锐费用

这是可独立核的真实有限管校准，不是假定曲率造成失败。取δ≪r≪1，令δ′=δ/r，H={x₄=0}⊂R⁵，坐标为 `(t,x₁,x₂,x₃,x₄)`。取过原点的whole-unit graphlines，slopes为

\[
 v_{1,2,3}\in[-c,c]\cap\delta\mathbb Z,
 \qquad v_4\in[-c_{\rm tang}\delta',c_{\rm tang}\delta']
                    \cap\delta\mathbb Z,
 \tag{5}
\]

常数取得足够小。用原δ尺度固定着色，可使实际unitdirections δ-separated；不改下面各数值量级。在长≈r的原clock段中，每根原δ管piece位于H的Cδ邻域，法向角≤c_tang δ/r；它们切于平坦TCI H，满足Def5.2并有**该短段的全部原marks**。不声称其整条轴线精确包含在H中。原index数

\[
 m\asymp \delta^{-3}r^{-1}.
 \tag{6}
\]

把空间和时间同时除以r，工作厚度是δ′。在一个投影到H的δ′方向bin内：三个切向坐标各有≈δ′/δ=r⁻¹个细值，法向带也有≈r⁻¹个值，故原label重数

\[
 \alpha\asymp r^{-4}.
 \tag{7}
\]

投影后的不同粗方向数≈δ′⁻³，乘以α恰为m。投影原短marks的relative density为1，没有靠稀疏shading制造此费用。

实际短piece全在有界r-ball与H的Cδ邻域内，因而

\[
 |\bigcup T_{\rm piece}|\le C r^4\delta,
 \qquad \sum_T|T_{\rm piece}|\asymp mr\delta^4\asymp\delta.
 \tag{8}
\]

所以若声称原δ-separation和flat tangency足以在δ′尺度免费保原全部labels，并得到与total piece volume成常数比例的四维包结论，它将与(8)相矛盾。该比例至少要付r⁴，恰为1/α。直接以DIR003的原weighted input、方向bin权α调用，归一后的四维visited-cell数最多只能期望 `mδ′⁻¹/α` 的量级；回原R5体积为 `mr⁵δ⁴=r⁴δ`，与(8)吻合。

特别tiny尺度r≈δ^(1−ε°)时，δ′≈δ^ε°而α≈δ⁻⁴⁺⁴ε°，不是相对δ′的subpower。此例仅否“局部缩放后自动方向分离/免费4Dterminal”桥；它不是满δ⁻⁴方向的H5反例，也不说明HRZ的全部D/尺度账本无法联合抵消这项费用。要抵消必须实际证明，不能删掉α。

另可校准(2)的raw broad终点：固定有限A、2≤k≤4，先取β>0相对A足够小，再取δ/r≪β。H内方向patch有3维角测度；任意A个(k−1)-planes的Cβ邻域在此patch不能全部覆盖（最坏k=4时，覆盖比例≤C Aβ）。留下的方向中有一个β-cap含≥c_(A,β)m根原管且与所有选定planes夹角>β。在共同原点的cδ-ball中这些管同时出现，故

\[
 \|\sum_T\chi_T\|_{BL^p_{k,A}(B_{Cr})}^{p}
 \ge c_{A,\beta,p}\delta^5m^p.
 \tag{9}
\]

该合法local terminal class满足原(44)的非退化，因而不能对所有此类输入把(2)统一再乘δ^σ。k=5时方向接近H4，不能使用这个broad下界。这里没有证明该包必是任一给定global运行实际选中的输出。

而在此bush中，原时刻t≫δ/β的每个δ-ball里，所有相交管方向都落入一个O(δ/t)cap，故k-broad为零。删掉clock长度O(δ/β)的原点区域，仅损相对短clock质量O(δ/(βr))，却可抹去全部whole-tube broad质量。它直接说明：用(4)保几乎全部原访问量，不会自动保原Lp/broad量；仍不能据此否定重新组织原shading的不同算法。

## 7. 直接保原尺度和曲面flatten的替代也未免费闭合

不缩clock而把短piece当原δ厚unitlines的shading，只给相对密度λ≈r。tiny情形r≈δ^(1−ε°)不在DIR对任意目标ε所保证的near-full `λ≥δ^η_D`范围。把短线延长、复制或重置方向来补满clock，要同时控制新footprint和原labels；(5)–(8)已经给出最有利flat情形的预算测试，不能免费完成。

一般TCI还需合法flatten：直线在曲面附近不等于曲面坐标下仍是直线；次数固定不自动给予任意系数下的uniform curvature bound。即便某个可付chart把所有局部管放入共同四平面的Cδ邻域，§6的方向费用仍在。因此“曲面4D可投影”不能替代原clock/方向/entry账本。这里不宣称所有flatten策略不可能，只是没有从已核源不等式得到免成本接口。

最后可直接用FSD001于原R5满方向family，s=4、m≈δ⁻⁴、原λ≥δ^η，得到 `#E≥cδ⁻⁴⁺o(1)`；这是真实原law上的基线4，不含固定σ>0。不能把每个terminal再调用同一4维种子的写法登记为已得到额外一维或新的正幂估计。

## 8. 结论、具体未付项和停止

本轮有用信息是：完整定位了alg1/2真正终止形式；给出DIR可用的原weighted weak-pruning闭包；并用flat短包证明局部方向bin费用r⁻⁴确实可发生，且在tiny尺度不是subpower。后二者是接口证明/校准，不是新的Kakeya下界。

没有得到H5，也没有其反例。没有证明一项可同时满足下列条件的新估计：保原shading的大部分质量；把真实tiny/tangent输出组织成合法四维长见证；保可求和的entry/clock预算；支付δ→δ/r方向重数后仍有固定σ余量。不能以补上这些假设的方式宣称接口通过。

依本轮spec，停止当前HRZ有限四维替换路线，不继续k、degree、radius、η或同义pruning阈值调整。若以后重开，需新的已证明输入，具体补上上述某个质量/尺度机制并产生严格增益；仅将(4)重命名、或重新计算旧narrow指数，不足以解除冻结。具名HRZ/完整四维/KT等外部责任继续分别保留，有限source审计不等于长期Goal完成。
