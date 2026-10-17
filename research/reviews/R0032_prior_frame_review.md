# R0032 独审：基础、原 prior 与前半 frame/group 链

2026-10-17，审查者 `/root/lifting_obstructions`。独立逐式实读 root `R0032_terminal_extension_full_proof.md` 最新版和 A `R0032_frame_graph_matching_audit.md` 全稿，并对照原 Def2.1/2.2/2.6/2.8、Lemmas2.3/2.4/2.9/2.10/2.12及3.5。本人的 anchor/assignment 主稿不计作自我独审；此处另核 root 最终整合及 A 的独立前半输入。

**结论：root 完整两原版本 terminal extension 链及 A 的前半证明通过本次内部独审。** 没有发现漏掉 conditional denominator、把 old floor 当 current floor、normal rotation误乘absolute midpoint、或 tiny group mass造成Cor3.4归一化失控的错步。已核作者补充：2.4只作用原tempered joint law，analytic cap仅用来证明存在高success selector；far roots仅计数，不储存巨大的1/c。未经外部同行评审，不认证完整OAI4或无条件高维界。

## 1. 2.3/2.4 的基础和实际可调用版本

restriction的g′≤g与∫_{g′<εg}g′≤ε∫g直接；refined label至多D个时逐旧state求和才付D。不能把未删bad部分拿去乘小conditional probabilities，现稿所有小域积分均先使用good capped submeasure。

2.4的坐标(t,y,V,rest)由y₀=y−tV给constant Jacobian1。固定rest/其余base轴后，每个原polynomial condition在单base轴至多fixed degree个 roots，identically zero则无changes。piecewise constant prior heights、piece counts、finite bin predicates、internal copies及其余变量ranges皆polynomial。任意Boolean组合的changes数由全部roots总数控制，因此向量值joint density（把全部discrete entries一起保留）有

\[
\|G(\cdot+h)-G\|_1\le C N^A|h|.
\]

不是只对已积分的一个marginal假设smoothness；它先在full coefficient fibers上证step-function bound再积分。extend-by-zero的support boundaries也在这些conditions中。

同cell pairwise difference可送入|h|∞≤Cρ的translation积分，给cell averaging误差≤CN^Aρ；固定D>A+T+1时TV≤N⁻ᵀ。D可依原problem complexity，这只细化有限编码，不进入后面N^{Ce}的C。

原只可测short-list selector在flattened law上的success由uniform TV比较；flat cell内posterior恒定，可取constant最优list，转回原law再损同量TV。cells/entries数polynomial、list长subpower，输出table本身tempered，search无需被编码。

**已核必要范围修补：** root最新版§3明确该TV输入为原tempered joint law(actual chart label,p_r)。分析density cap只证明存在高success可测selector；不把density-masked、可能非tempered的goodmeasure本身套入2.4。最终用actual label∈storedtable重建真实tempered restriction，去掉分析mask。该解释闭合了基础调用，没有循环。

## 2. 2.9/2.10：真floor和原观察知识同时保留

quadratic sublevel有至多两monotone components，|Q′|≥b时各value-window preimage长≤2ε/b；total≤4ε/b，gridbin数只多固定end bins。此界与bin所在位置无关，适用于很远的roots。

删qν_c>Hm_c的whole charts成本≤H⁻¹Σωqν_c≤H⁻¹。原pr密度cap的goodmeasure上，每chart空间basevolume≤KqJ_c、hiddenbins≤K，故good m_c≤Kn(r)qJ_c。若full m_c超该upper两倍，其至少半mass在原globalbad部分；按实际disjoint assignments求和删除whole charts成本≤2bad mass。配合original truefloor得到m_c/q、ν_c、n(r)J_c的subpower可比，未重设assigned prior。

crossing count T在capped**原**incidence law上积分，每chart再用同一basevolume/bin bound，故∫T≤KΣωn(r)qJ_c≤KΣωm_c。Markov的threshold可取subpower且使loss为系统mass的o(1)。随后用§1的原jointlaw表替换selector，再删失去超过半selected mass的charts；survivors的new m_c≥old m_c/2，truefloor仍在。没有对每个幸存incidence额外condition label或trajectory probability。

## 3. 真正额外的2.12及whole-label几何

Def2.8只给最大轴upper，不能自行写成q。root显式调用并重证largest-axis fullness是必要的。若||D_c||/q≤N⁻α在inverse-subpower质量上，wholeinterval端点bounds给|V−y′_c|≤KN⁻α。选fixed0<u<α/2且u≤ηL，每候选chart只需subpower个angular bins；oldp_L给subpower候选charts，故每pure observation只需subpower候选velocity bins。

先删joint cap和pure typical lower例外。在good numerator上，每bin≤n(L)N^{-Su+τ}，old pure denominator≥n(L)N⁻τ。候选bins可依observation，但pointwise求和后≤KN^{-Su+2τ}倍原pure density；再积分原pure law。τ<Su/4使deficient mass power-small，不能承inverse-subpower质量。未用未剪原law的max-angular bound。

由此排每fixedα，可缓慢对角化/whole-label homogenization成largest axis q up to subpower。保whole labels不改变该label原floor；n_Q=n(L)q₀ʲg的使用合法。version1 g=1，version2仅两个空间轴q₀/q₀g；这里没有j3推广。

## 4. 原双时间实验及old floor与current mass的区别

weighted reference Σω_γq₁ν_γdt₀/q₁dt/q₁为probability；both-old-selected event质量是Σωq₁∫s_I²≥(Σωq₁∫s_I)²，故inverse-subpower。积分任一time得到1_E s_I times原one-time law；在block内≤原law/q₁，乘globalωq₁后≤原selected law。后续全部pair restrictions未归一化，这个domination一直有效。

每old subblock内由prepared **original** floor和ν assignment disjointness给labels≤K/n_Q；new block有O(Nᵉ)个subblocks，故≤KNᵉ/n_Q。未来pair/group masks不必给这些labels保currentfloor，计数只借frozen oldfloor。

degree2/1 interpolation从q₀外推q₁只付N^{O(e)}，不付coefficient heights。固定某test自己的selected vertex后，另一raw time仍uniform；affine derivative有ownmax≥K⁻¹，小于N⁻ᵉ的time比例≤KN⁻ᵉ。加对方selection只减质量，未在retained pair条件下再假uniform。

## 5. Angular exception与relative frame

v2两widthKg velocity strips、normals正弦角>gN^{Re}时交集diameter≤KN^{-Re}，仅需K angular bins。这是二维geometry，不适用于更多visible维数。source A的extrapolated rectangle面积≤q₀²gN^{C₀e}，terminal hiddenbins≤N^{C₀e}，oldlabelcount KNᵉ/n_Q，jointcap n(L)N^{(1−SR)e}相乘正给KN^{(2+2C₀−SR)e}；normalized time积分是1，n_Q恰取消q₀²g n(L)。R在e/L限制前固定足大即可。

g#=min(1,gN^{Re})，source D为deterministic rounded frame。A′列候选source orientations后，必须把它的center/velocity投到**同一个candidate rounded frame**再比较；actual common line使center差≤Kq₁/Kq₁g、velocity差≤K/Kg。rotation只乘这些差，故normal error≤Kq₁g#/Kg#，与grids匹配。不把绝对midpoint旋转误差g#·|y|错误地当q₁g#。

g#=1时static midpoint/固定axes利用原V subpower即可覆盖wholetrace。J_D≤Kq₁ʲg#≤N^{C_frame e}q₀ʲg，因为g#/g≤N^{Re}；constant不依g、h或L。A′→D options为subpower perlabel，非仅perpoint的不可统一list。

## 6. (A′,D) 在source的density没有隐去分母

fixed (A,D) 或 (A′,D) entry只是pair law的restriction。即使A′在source observation不可知，其source marginal仍≤原source selected law/q₁；无需condition A′，所以无entry-mass denominator。

witness equation沿其assigned line从自己的old subblock外推，在source有smallvalue；opposite-derivative剪选给source derivative floor。于是对fixed source base，其可兼容hidden terminal bins数≤N^{Ce}。用source vertex已capped pr density和(dt₀/q₁)dy=J_Ddτdξ，可得每entry z₀-density≤n_QN^{C_base e}。不是把normalized entry law错误地赋此同一upper。

## 7. 两套删轻常数、carrier体积与stable graphs

先选C_entry，用oldlabelcount×Doptions支付删light(A,D)/(A′,D)成本。保存的是该轮**joint删除前**的entry mass≥n_QN^{-C_entrye}，与densityupper给carrier Lebesgue volume≥N^{-(C_entry+C_base)e}。不需要用可能不可测的support projection，只用positive-density carrier。

early C_A curvature转换只依old equation/D；highcurv用realaffine center，未替换部分source满足|2PwwP|≪|Pw|²、discriminant下上界N^{-O(e)}…N^{O(e)}。Remez用heavy carrier原mass而非latercurrentmass，给coefficients/derivativesN^{Ce}。随后fixed C_U保证两当前discriminants在8U nonzero；不要求一球对所有labels安全。nearest root对actual w近，farunused root不参与。

后面的C_index在C_U/C_opt之后选择，与C_entry不同；currentgroup删除不反改carrier/Remez/C_U。root与A均已拆开这两常数，未用同名C′后增造成循环。

## 8. Group options与M≤1/M>1真实mass upper

group按M/D/U和两center jet cubes分。norm差≤2M给center jets相差CM，故配对cubes为bounded neighbours；same-group functions的finite jets彼此CM-close，再由norm-to-finitejet比较得共同actual reference norm≤CM。每label每M自己的cube确定；另一cube只有fixed choices。U网格N^{C_U(j+1)e}、M的polynomial range只给C_problem log N choices，可对fixed e吸入Nᵉ，因此C_opt独立C_*及problem polynomial exponent。

M≥δN^{C_*e}且C_*>C_graph使near-w error吸入band O(M)。M≤1时，选M≤a_r≤MNᵉ，band仅碰O(1)个a_r bins，source capped density和Jacobian给m_G≤n_QN^{C_mass e}(M/δ)^d。cap-class不等号方向n(r)≤n(L)(a_r/δ)^d正确；d≥0、d<1使mesh费用受固定Nᵉ控制。

M>1时若直接数O(M)个unit bins会错。现稿正确用v1的subpower w-range，或v2在**source自己的selected incidence**的native |P*|≤K、|P*_w|≥K⁻¹，2.9只容subpower个unit w-bins，不依它们的绝对位置。n(0)≤n(L)δ^{-d}≤n(L)(M/δ)^d给同一bound，未把w假成subpower bounded。

## 9. Tiny m_G的Cor3.4原π预算

第二轮每group/color删pre-joint-deletion index mass<n_QN^{-C_indexe}。options总count结合oldfloor付global loss<N^{-2e}；若badpairs总mass≥N⁻ᵉ，必有group m_G′≥m_G/2>0。该group可以绝对极轻，无需m_G′≥N^{-Ce}。

每色保留index数≤N^{C_indexe}m_G/n_Q。raw weights a_i=n_Q/m_G′总和W_κ≤2N^{C_indexe}，π_i=a_i/W_κ。normalized perindex base density≤(n_Q/m_G′)N^{C_basee}=a_iN^{C_basee}≤N^{Ce}π_i。tiny m_G′分母确被同一个rawweight支付，未免费取消；两色可有不同W但各自仍probability weights。

scaled U使holomorphic geometry固定，Jacobian只付N^{O(e)}（实际体积因子≤1）。R_match=M/δ≥N^{C_*e}，其后选C_*使此前C_list/C_pi/C_graph/常数均为Cor3.4允许的小fixedpower。normgap≥M、reference≤CM、lawmass1及真实相关source basepoint完全匹配。C_*不倒流影响C_entry/C_U/C_opt，故没有闭环。

## 10. Root后半及Def2.8最终接口的复核

anchor异常按每pair概率对原weightedlaw积分，未对全部poly tables union；source-safe路径回传仅为P_b(z,f_source)、P_b,w(z,f_source)，不把representativebranch强续回source。fixedsource A在anchor≤2root/jet bins使代表source-discriminant异常charge只乘oldlabelcount；C₃在laterT之前固定。

table作为anchors/D/b的函数先建，后联合freeze参数与t_src；weighted总success保inverse-subpower，不许逐block下界。最终trajectory assignment在fixedsource时间由唯一oldA/branch得到c₀=(D,b)，merge oldsourceidentity，并显式检验wholeblock fits；later incidence selection用旧A′compatibilitylist，去除analytic masks仍含frozen successes。旧pL提供subpower而非N^{Ce}个c₀，lowcase另乘O(logN)个v仍subpower。

lowcurv source上P_b,w²=Δ_b+2P_b,wwP_b与absolute discriminant lower迫Δ_b>0并给M_∂下界；P_b/v满足wholeblockvalue/derivativeupper/curvature，selected lower以原disjointassigned-prior预算删O(κ)时间支付，无pair-success density假设。highcurv用w−F_ctr，值由derivativeupper/curvaturelower直接给，不要求representative实根。

version1保持w−F，hidden quadratic仍使along-line degree2；v2 totaldegree2、y/w affine。undo w_new=Bw_old使derivative和curvature分别乘B、B²，精确恢复Def2.8。newlargest spatialaxis≤q₁K、assignments disjoint、totalmassinverse-subpower、oldpL knowledge和temperedness齐备；known atlas不要求新truefloor，当前文本没有增此结论。

## 11. C不依L/complexity与有限编码

固定model/angular/degree决定extrapolation、Remez、continuation、jetdimension和最终C₂/C₃/C₄/C_s/T。n_Q取消oldcount、每source至多2representatives、按原prior删时，避免C乘上全poly table指数。problem的巨大range只影响O(logN) choices、finiteencoding和充分大N阈值。e先fixed，再N→∞，没有声称e_N→0的uniform版本。

root§13明确farroot仅用于count，输出只存stored polynomial bins；可用原quadratic relation加bounded root/jet变量检查，不储存可能superpolynomial的1/c。实际affine-center inversions只在specified curvature cutoff之上，1/v有subpower upper，coordinateinverse与B/B⁻¹原本polynomial。whole-block条件仅一time quantifier，fixed-piece continuation、nearest-root和fixed-order jets为fixed-format predicates。analytic density/search过程不编码，fixed source times/anchors/table常数可编码，符合Def2.2。

最后所有constants先定，才取c使e<cL并保证Re≤ηL和L−Ce>0；选择有半mass的curvaturecase及subsequence给共同L′，0<L′<L、L−L′≤Ce，q₁ horizon exponenth−e。通过范围严格为原j1/j2及原tests，不能据此升j3或恢复旧frozen genericcompletion。

本次内部独审通过，尚未经外部同行评审。critical paths、后续排除与其余完整source责任没有被Lemma3.5认证自动消去，SRC/DIR/FSD/DIM的完整OAI4条件仍保留，Goal active。
