# R0038：来源证书拼接、有限读出与具名输入的独立审计

2026-10-17，B。读固定恢复入口、registry、R38 spec，运行 context.py；逐段复读原 2.17、4.3、4.11、6.1/6.9、§§8–10 的结尾，SRC001/DIR003 的实际证明与独审，以及 R29 投影、KT 接口的证明与独审。本文不是新的研究方向或新高维定理；以下来源拼接仍显式保留具名高级输入，未经外部同行评审。

## 1. 本轮可证伪的责任

唯一问题是已审工具和三种窄度分支能否接受**同一原模型、同一原先验、同一 actual guard**，并真正给出四维有限着色输入。不能只用“所有集合 Hausdorff 维数为 4”的句子替代有限结论。

检查项是：j=1/2、d 的端点 0、k 的端点 0/1、ℓ=0/正有限/∞；每 subsequence、每 substantial 原 residual 的存在量词；prepared probability 返回原质量；known atlas 与 true floor 的差别；有限长 marks 与平均 shading；KT 的任意固定 ambient、实角参数和严格次临界种子。若其中任一处要新增未付几何定理，则停止相应出口，不能用削弱假设补洞。

下文的 G 专指 GWZ arXiv:2601.14411v2（2026-10-11）Theorem1.1 的三维 convex-clustering **集合估计**。本项目核其确切 statement 和应用，不在本轮重证整篇高级证明。KT6.2 同样保持具名完整输入。WZ/CV/OSS、固定次组合论及固定格式实代数基础分别依原证书保留。

## 2. 同一模型的证书接口

| 已审证书 | 原输入与输出 | 本轮拼接必须保留的限制 |
|---|---|---|
| TCM001 / ASM001，R30–31 | 原3.3及3.1/3.4，两色任意原 π、相关事件、范数/jet与切片 | 不是把相关 law 改成两个独立 lists；容差先固定，规范化的两色分母都付 |
| TEX001，R32 | 原3.5，v1/j1与v2/j2 terminal extension | C 只依固定模型、d0<1、Sη，不依 L/复杂度；old pL-known，不要求新 true floor |
| CRP001，R33 | 2.7/2.13、G条件下2.15/2.16、4.1–4.3 | within-world factor Jc/νc，world factor ωqνc/Z；terminal equality/intermediate upper 分开 |
| AIM001，R34 | 原4.4–4.12完整 candidate→actual conversion | every-residual 假设、countable menu→fixed scenario、whole assignment、原 law posterior、预声明实际 guard |
| ISO001，R35 | 原6.1，v1/j1，或v2/j2且ℓ=0 | 同 h-block 的 degree2 proper test、qνQ(a2/a)^d/K质量；不是任意 scalar observable |
| UNB001，R36 | 完整8.2及10.1 | 8.2先由scalar H=0取得；∞分支原µprep固定，parent仅known、terminal child才付true floor |
| FIN001，R37 | 完整§§7–9，v2/j2且0<ℓ<∞ | 两份 frozen laws、原 edges、所有 residual；critical/bootstrap/endpoint和offcritical实际恢复全部保留 |

这是输入输出核对，不追改旧证书当时的完成 flags。特别是原2.11的同时 current floors 是 R34 支付，不追认为 R32；原 frozen witnesses 的 floor 不能免费转给最后 residual。

实际过程均为：固定 exact problem 的内层 N0→∞，再取优化问题的外层 i→∞，最后作预声明的慢对角。有限次子列、重设问题的 polynomial complexity 可以依固定问题；不能将任意 analytic K=N^{o(1)}直接当 original actual output 的 Kpath 幂。

## 3. 先排 scalar，后排二可见坐标；不存在循环

固定任意 admissible S,η>0。若 v1/j1 有 C(d<1) 的 bad problem，CRP 给 d*∈[0,1)、正临界率 0<k≤1 和 formal ℓ=0 的路径。ISO 的 **v1部分**给每 substantial 原 residual 的 proper candidate；AIM 得被预声明 actual guard 排除的已知 atlas。因此 scalar Cor6.9 的 H=0 先成立。

只有这一步以后才调用8.2的 scalar reductions；它们为每个需要的固定角参数重用 Cor6.9，未先用 v2有限/∞分支反过来证明 scalar。8.2和 UNB001 的组合没有逻辑上依赖正有限窄度分支。

再假 v2/j2 有 bad problem。原4.3选 d* 和 k 后，优化的窄度只有三种：

- ℓ=0：ISO 的 v2部分→AIM。
- 0<ℓ<∞：FIN001，先原投影/比较；直接候选或 horizontal k=ℓ。2k=1 用原9.2；2k<1 用每 dense input 的 G(u)、有限 bootstrap 后的真正 endpoint；2k>1直接用9.6所需 wide intervals。三支最终都返回 proper candidate→AIM。
- ℓ=∞：UNB001/10.1 用 nested true systems、8.2、原 posterior/list recovery 构造实际 known atlas，再用2.13及终端 completion破坏正临界率。

d*=0 时 critical relative-profile 证明用单调性排除更低 secant；不要求 d*>0。k=0 由 TEX 的统一 C及 horizon composition排除，不能作为第四几何分支；k=1被ISO及FIN的above-critical支包含。ℓ是跨 maximizing sequences 的 inf/sup优化值，不要求由一个单一系统 attained；ℓ∞按有限 threshold和外层子列实现。所有 fixed finite target grids 最后才慢增，未把无穷 grid当同时免费存在。

## 4. 原 law、candidate 和 actual guard 的共同接口

每个 true chart c保 whole-trajectory assignment Ac、νc=ν(Ac)、time q及自己的 frozen selected witnesses。一个节点作新 world时，其 probability prior是ν(.|Ac)，其世界权重是ωqνc/Z。2.13给 terminal density equality与 earlier upper，只有 parent已知pr时才有 earlier equality。terminal true child 可通过仅terminal-known parent lift；intermediate child需该额外 equality。这正覆盖∞分支的已知parent，不额外要求新parent true floor。

各候选分支对进一步合法原 residual仍可调用：先保已有 upper/cap 的原 fixed reference，再删轻或按预算恢复所需 current floors。whole witnesses在进一步删选后仍作为原 frozen submeasure计数。两份不同 references（如 long-line cover和point density）始终分开；没有把成功事件条件化后的 law冒充原 trajectory prior。

AIM要求 every subsequence携带 substantial residual时有 further-subsequence候选，不只存在一次 inverse-subpower discovery。其 finite greedy对每 fixed scenario取 whole trajectories，若所有 finite menus覆盖趋零，删除全部这些 whole pieces后的 substantial residual仍可给候选，反 maximality。于是固定scenario保原reference的 inverse-subpower覆盖；随后才删其小 derivative时段。

prepared measure是 probability，其回原质量是 pprep=(1−o(1))ppath。实际 submeasure写ν=pprep T≤µ，不能写 T≤µ。最终 geometric map在整个原 tempered joint law上定义；不通过最终 derivative lower等 selected tests时赋 failure，failure不进最大列表。unknown path/output labels仅在 joint law里保留，不能给 observation selector。

最后输出的 list/slack为实际 (Kpath logN0)^rS；complexity为固定 P_S(Mpath)，由预声明 2^{(Mpath+n)^2} guard吸收。candidate的固定正厚度/窄度 gain支付 analytic fitting losses；原覆盖比较还使用 G_n/logN0→0，而非只用 inverse-subpower字样。故各分支的结论恰为原4.11所需对象，不是仅一个 tangent statement。

## 5. G 的最小直接输入：不需要 companion整个 maximal theorem

G的确切范围是有限 **distinct** 三维 unit δ-tubes，Δmax≤δ^{-ηG}、平均 shading density≥δ^{ηG}，结论 union≥δ^ε Σ|T|。见本地GWZ v2 PDF2。它既非四维无方向 WP4，也非只对 separated directions 的输入。

重新核 companion `05-inputs.tex` 前两小节及 CRP001的完整有限证明：

1. 若任意正权/重复 indices有Σ_{Ti⊂K}ωi|Ti|≤A|K|，置vi=ωi/A。测试tube本身与ambient ball给 vi≤1、S=Σvi≤Cδ^{-2}。每个index的原 shading需逐个满足长密度，不能只假原平均长。
2. S≲log时 pointwise总权已给结论。否则独立Bernoulli(vi)抽样。John ellipsoid及 center/frame/axes精度 cδ²的固定维 box网，将全部convex tests压到δ^{-C}项。指数矩给同时 O(log)聚类，lower-tail给sample数≥S/2，两个事件可同取。
3. 相同tube重复数亦≤C log。每 distinct tube保一个实际index及它自己的原 shading，仍逐管长；distinct数≥cS/log。原weighted numerator另以 AS|T|控制，无需这个代表保留重复tube全部shading质量。G于ε/2给weighted bound，log由余ε/2吸收。原index数、最小权和跨度全不进常数。
4. line chart中whole trace先放共同fixed-length、radiusCδ tubes并留endcap余量。任意convex K的John ellipsoid含这些whole traces，time diameter≥1，最大水平slice area≤C|K|。各slice有固定空间轴及affine centers，最大slice外接矩形给一个**full-time** spatial plank，面积≤C|K|、轴≥cδ。
5. 因而全时plank cap Σω≤Aab给 weightedconvex cap CA。每marked time-bin中心放 disjoint cδ-balls，同index shading体积≈#Jiδ³、总union≤C#Eδ³。逐线marks≥δ^{-1+η}使G密度条件成立，约去δ³正得原2.15。

截断宽度的固定倍、bounded remaining δ、任意rotated frame和变换后的cell enlargement均已在CRP中支付。continuous prior只为这项估计按更细coefficient rounding/finite mark patterns分组；即使分析性indices极多，有限引理常数独立其数量。mark pattern不是输出 atlas label。接2.16时原 group先验未归一化、whole-cell witness与current residual分开、j1 dummy-padding有独立 chord bound；故不借额外高维输入。

**最小责任链是 G集合估计→weightedconvex→linechart2.15→2.16/其余原调用。** 不能将 companion maximal的其它深层证明额外列为这条链所必需，也不能因为这条有限链已核就称 G整篇新高级证明已在本项目独证。

## 6. SRC001的完整有限反证读出

固定bounded四维graph chart及0<σ<1。所需 statement为：存在η>0及δ0，使δ<δ0、δ-separated full三维slopes的实际indexed lines满足

    M≥δ^{-3+η},  每条#Ji≥δ^{-1+η}

时，visited δ-cell union不能有#E≤δ^{-4+σ}。取固定enlargement/cell convention只改变常数，先用更小固定σ留余量即可。

若该statement失败，对ηi↓0取δi↓0反例。line indices≤Cδi^{-3}，全部visited cells≤Cδi^{-4}。把每个marked center扩为沿原line长cδi的time interval；bounded速度使整段落在E固定扩大内，每条总时长≥cδi^{ηi}。这是正Lebesgue时间，不能用孤立mark点的零时间质量冒充。

用原line的uniform mixture，各三intercept与三slope独立O(δi)-box noise，取 native P*=w、B=1、L=1。所有上述times对全部允许noise仍在再固定扩大的 E中。separation给

    ||dν_s/ds||∞≤C/(Mδi³)≤Cδi^{-ηi}=N0^{o(1)}；

给定完整slope时，二维visible intercept density≤Cδi^{-2}，因为每component的intercept noises独立且conditional mixture weights求和1。mixture indexed copies、density heights、box/predicate数全有一个统一固定polynomial bound；ηi变化不增复杂度指数。故是合法tempered exact sequence，selected mass inverse-subpower。

这正是原2.17 **有限见证选取之后**的输入，不需要固定跨尺度K。joint homogenization时：每cover δ-cell在(t,y,[w]δ) observation只用O(1)hiddenbins，basevolume O(δ³)，所以总support measure≤C#E δ³≤Cδ^{-1+σ}。典型density有 n(1,0)≥δ^{1−σ}/K，故g(1,0)≥σ。其它两界g(0,0)≤0及g(r,u)≤r+2−2u用原2.15和上述slope/intercept ceilings，完全不再用K。

选择g(r,u)−Rr+Su的endpoint后得C(1−R)、fixedSη>0、g(r0,u0)≥σ/2。A的本轮2.17全审负责其crop、semialgebraic slope choice、regular fiber/monic cubic/Pw good-times和q³界；这些步骤仅用同一smoothed原prior及true chart定义。最终所有subsequence/合法selection的true terminal q满足m(r0,u0)≤Kq^{-3}，从而H≥σ/6。

§§2–4的完整模型分支排除遂给矛盾。这里不能把“任意K的Hausdorff满维”当已足够；所用的是**它背后的有限后半归约和bad problems排除**。本轮若A/root对应证明有缺口，SRC001出口也相应停止；不能由旧证书statement掩盖。

## 7. 稀疏、权重与合法shading删选的不同闭包

先从SRC001得任意M的separated family估计。R9的实际proof用 bounded shear S_a(t,y)=(t,y+ta)，保持旧clock与marks。M个δ/10方向小球并U有体积≈Mδ³；O_R((Mδ³)^{-1})个随机bounded shifts在固定目标方向盒覆盖常数体积，故某确定choice可取≈δ^{-3}个separated实际copy-lines。时间重分ρ=Cδ每bin只合并O_R(1)marks；#E'≤C_R copies·#E。SRC001于是给

    #E≥c_{R,ε}Mδ^{-1+ε}                         (F1)

对所有1≤M≤C_Rδ^{-3}统一。复制后仍是固定bounded graph chart，不需这些copies属于某一个K；正是有限proof-level输入允许此操作。

任意positive weights/repeated indices，若每δ-slope bin总权≤α且**各原index**均长marked，则将bins固定有限coloring，每bin任取一个真实index。F1给occupied-bin数≤Cδ^{1−ε}#E；用每index最多δ^{-1}marks得

    Σωi#Ji≤Cαδ^{-ε}#E。                         (F2)

代表只保它自己的marks，不拼接同bin别条线的marks。极小总质量/最小权、任意权重跨度和indices总数均无条件。continuous law的正质量bins内取实际长marked代表也一样。若有actual slope density≤A，则α≤Aδ³；不能将α=A或将atomic-bin cap反称Lebesgue density。

restriction减少原positive upper cap，footprint也只是子集；但 arbitrary shading删选会破坏逐线长marks，不能免费对删后全部indices用F2。仅有平均mass≥λmδ^{-1}时，先取heavy lines各≥λδ^{-1}/2，数≥cλm，再调用；由此产生真实密度费用。原2.16任意parent/residual没有full方向密度，不能以F2替其无方向plank输入。

## 8. R29任意ambient种子与两个λ

复读A投影全稿及两独审：fixedambient M、reals≥3、原方向cap K(θ/δ)^s对所有centers和δ≤θ≤1成立。boundedGaussian P到R4的pair collision probability≤Cmin(1,(δ/θ)³)。dyadic求和及θ≥1的固定sphere cover给每line expected degree≤CKδ^{3−s}(1+logδ^{-1})。同一个P可同时bounded、保常数比例nonshort、总edges有界；independent set给任意m个原indices的输出数

    m'≥c m/[Kδ^{3−s}(1+logδ^{-1})]。             (F3)

output separated以后cap3才由packing得，不是将projection Frostman当免费继承。nonshort、共同fixed graph chart/clock、endpoint marks及boundedP的每原cell cover都只损固定常数；延长supporting line不增加新marks。

原平均mass λ先heavy，(F3)再给m'≥cλm/[Kδ^{3−s}log]；每输出line自己的marks仍≥cλδ^{-1}。F2于α=O(1)给

    #E≥c λ²m K^{-1}δ^{s−4+εD}/(1+logδ^{-1})。   (F4)

一个λ来自heavy数量，一个来自单line marks，均不可删除。K≤δ^{-η}、λ≥δ^η时，额外成本是δ^{3η}，不是δ^{-3η}。先εD，再η<ηDIR/2并小于最终ε余量，最后δ小吸log及常数，得

    #E≥c m δ^{s−4+ε}。                          (F5)

这是任意条数unsaturated形式，正好支付KT(40)的m/N^{n−1}；无需额外无费用direction-monotonicity或factorization假设。饱和m≥δ^{-s+η}给#E≥δ^{-4+εtarget}。F3–5本身没有把four-dimensional Hausdorff集合statement升级为finite input；其真正几何前提仍是§6的SRC001。

## 9. 严格次临界KT接口与条件六维结论

KT math/0102135v1 Definitions5.1/5.2/6.1允许fixed任意ambient R^M、real n,d、separated lines、all-angle (n−1)-collection；saturated shading只要求**总**mass≈N#T。其proof的第二family在R^{M+1}、角指数d，未必方向数饱和，所以(F5)的任意条数形式有实际用途。

本有限输入的准确顺序是∀outputε>0∃inputη>0，不给η(ε)线性模数。固定ζ>0后，先选source输出loss≪ζ，再把KT有限次所用soft input losses选到该η内，才得全real n≥4的 **K(n,4−ζ)**。不能额外登记literal K(n,4)统一定量端点。fixedambient常数可依M；M不随N增长。

具名KT Theorem6.2：K(n,d)与K(d+1,d')、0<d<n，推出K(n,(2n+1+d')/4)。取n=6、d=d'=4−ζ，有两项seed K(6,4−ζ)、K(5−ζ,4−ζ)，第二项real angular s=4−ζ≥3，均由(F5)支付。于是

    K(6,17/4−ζ/4)。                              (F6)

完整KT高级proof仍具名，尤其不能以R29核定义/第二输入代替每个pivot/Córdoba步骤的独立重证。其原Lemma6.6 proof中exponent d−1与statement d-collection的局部排印责任仍在旧audit明列，不在本轮凭无关有限检验将整篇认证为已逐式重证。

## 10. 有限K(n,d)到任意集合的outermeasure读出

此节是对R29仅写compact convention的**额外显式桥接核验**，不从“standard”二字免费扩大scope。设整数n、d>0，已经有上述完整small-loss有限K(n,d)；假任意K⊂R^n含所有方向unit segments且dimH K<t<d。

先在一个固定窄graph-slope chart工作。所有unit segments中可取rational公共time interval和integer bounded interceptbox；这些countably choices覆盖chart directions。outer subadditivity给其中一个选择的eligible slopes S0有positiveoutermeasure a>0。固定affine坐标把clock化[0,1]、slopes化KT的近竖直bounded chart；这只改变固定常数和Hausdorff covers，不需可测选线。

取最大半径趋0的ballcover，Σr_i^t≤1。对δ=2^{-k}层Uk，ball数≤Cδ^{-t}。每eligible segment至少有一个k使其在Uk的time≥c/k²；再以outer subadditivity找同一k的successful slope set Sk满足|Sk|*≥c'a/k²。随着最大cover radius趋0，该k趋∞。

在Sk取maximal Cδ-separated有限真实slopes，选择各自成功witness，得

    c δ^{-(n−1)}/k²≤#T≤Cδ^{-(n−1)}。

取C为固定chart常数，使KT方向separation满足。sphere packing对任意center和δ≤θ≤1给cap C(θ/δ)^{n−1}。每条成功线Uk时间至少c/k²，故至少cδ^{-1}/k²个非空δ-timebins；在这些bin中心取该原line点，再换ambient lattice。位移O(δ)，每timebin仅O(1)合并，marks仍≥cδ^{-1}/k²。所有points位于Uk固定扩大，故#E≤Cδ^{-t}。

于是这是KT的saturated direction collection与saturated shading，所有缺损仅polylog。这里saturated允许softloss，非要求每条全线；平均shading由更强的逐条polylog时长给出。给最终ε<(d−t)/3，固定相应finite input门槛，k^{-C}最终大于δ^η，全部hypotheses满足。有限K(n,d)给#E≥cδ^{-d+ε}，与#E≤Cδ^{-t}矛盾。

因此该有限K(n,d)已足以对**任意**K给dimH K≥d；没有把非可测K作Fubini，也没有使用可测direction-to-line选择。原cover是openballs，单条已选line的time集合可测；全程只选有限个witness。上述桥可接(F6)再ζ↓0，得到任意六维K的条件17/4下界。它是2.17外测度有限选择的重用，非新数学方向/新颖性声明。

## 11. 停止边界与剩余条件

本稿未发现必须新增的有限几何估计：全证书按正确模型可接，SRC001的finite反证有实际输入，DIR/FSD的删选和权重费用完整，strictsubcritical KT及outermeasure读出闭合。随后已实际通读root整合§§1–21及A完整2.17§§1–14，正式审查归档于 research/reviews/R0038_assembly_finite_seed_and_input_review.md；本稿自审不计独立审查，本稿本身的独审由A/root负责。

未消除的责任是 G新高级完整proof、具名KT完整递推proof，以及各证书明确保留的WZ/CV/OSS/基础标准inputs；没有在本轮独立重证它们。条件链若被接受才有完整来源排除及高维推论。没有认证2026全前沿/优先权、新颖性、重大性，也没有证明五维或一般满维数；长期Goal仍active。授权全文交审已完成，随后停止编辑；不继续以合法重用、ε改名或compactness补注登记新方向。
