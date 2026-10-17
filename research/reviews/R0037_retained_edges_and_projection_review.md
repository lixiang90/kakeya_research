# R0037 正有限窄度分支：原边、投影与整链独立审查

2026-10-17，审查者 A。结论：**所列具名输入下，root 整合稿与 B 后半稿通过本次逐步独立审查**。这是原稿已有 §7–9 分支的来源审查；未经外部同行评审，不声明新定理、完整四维源认证或新高维界。

实际全文读取：`notes/10_source_audit/finite_narrowness/R0037_positive_finite_narrowness_full_proof.md` §§1–23，以及 `R0037_horizontal_critical_and_bootstrap_audit.md` §§1–13。核对原 PDF 物理页108–153、提取文本5803–8254，及官方 `06a-retained-edge.tex`、`07-finite-narrowness.tex`、`08-critical-rates.tex`。本人前端独稿为独立重算记录，不作为一份额外独立审查；以下对 root 全稿和 B 后半实际逐式核查。

## 1. 命题、删选闭包及证书边界

root §1 的命题保留原 version2、j=2、d<1、固定正角指数和 0<ℓ<∞；结论是每子列、每 substantial 原 active residual 上的 further 子列 proper candidate。证明没有将其降成“某一个输入上存在好拟合”。所有 raw upper 对限制保留，但 current marginal floor、conditional π domination 和逐轨迹 duration 分别重新支付；full assigned trajectory prior 与早期 whole-domain witnesses 不因当前删选而改换。

§2 与原9.1的有限 family peeling 合法：每 entry 永久删除最多收费一次；分母阈值在 finite 总预算与当前 inverse mass 之后选。缓慢增大的 family 先作每个 fixed finite 构造再对角，未将无限多次固定损失免费相乘。AIM001只是引用其已审完整实际转换接口，不以 tangent K 冒充原 N₀ 尺度输出常数。

## 2. 原 §7 retained-edge 工具

root §3 的三步 walk 计数保留的是原 G 的边。对固定终端 (u,v)，中间两顶点可从三个原 restricted sums 恢复；不同 u+v 的三元组互不相交，故全 cross-sum 的上界正确。rounding 后的 vertex/edge multiplicity 分别付 K/K²，再 pull back 原边，不能只依靠抽象小 doubling 顶点。

共同 κ₀ 来自同一个 A×B universe 的交集二次平均。原 ratio 索引不被无代价合并；fixed-length Ruzsa/Plünnecke 运算统一于一个 E/F endpoint frame。signed products 的证明用 cX 包在各项 Minkowski sum 中，既不除相消系数 c，也不假乘积系数远离零。迭代长度先固定，随后才允许 tolerance 的慢对角。

§4 的外部具名输入核为 Orponen–de Saxcé–Shmerkin，*On the Fourier decay of multiplicative convolutions*，arXiv2309.03068v2，Theorem1.5。所用的是 smoothed single-scale energy 版本，无避零要求；本次只核定义、statement 和应用，不重证其 whole proof。原 ratio interval cap 对任何固定 s<S 给 I_s^r≤C_sK′；在 h≤r≤h^{e₀} 上晚 N 可满足定理的 r^{-ε₀} 门槛。乘法卷积的 Fourier decay 再作固定次数加法卷积，频率分段积分确给区间 h 上 C_e h^{1-e}。

§5 collision 的两份 endpoint sums 使用**同一** coefficient tuple，条件于该 tuple 才是同分布独立样本，故 support 下界 h/K_m 成立。反向先固定 endpoint samples，再选与系数独立的非退化 wedge，两个剩余 flat coefficients 的 parallelogram 计数是 K/Δ 个 h-squares；总上界 h³+K_mh^{1+ε/2-2e} 与下界冲突。这里完全没有把原 source edge law 或 κ 条件化后假设成 product law。

§6/原7.7确需两个不同冻结 law。旧长轨迹 witness 给投影 cover；较晚 point marginal floors 给最终恢复的原 incidence mass。两者在稿中分开，三方向 graph 的 endpoint-pair multiplicity、first-coordinate rectangle cap 和 ratio law均有原计数支持。选中点 cells 后恢复其整个 μ_pt incidence 子集合法，并非只剩三条方向。

投影符号已明确：z·Ju=−Jz·u，因此 λ=−(E/ξ)λ_strip。该重命名不改变命题。最终 λ 的 K bound 由原 base cap 排除大 λ，而非从较大尺度投影直接免费继承。保原 clock，未作不合法时间重参数。

## 3. §8.2–8.4 的 full prior、三宽区间与 native candidate

root §7 的 projected group 密度分母是完整 prior p_{αγ}，不是成功样本质量；c=w_αg_s/p_{αγ}。support 的加权计算另由 true Q_s、K h_s/χ intercept choices、normalized area 与 Σq_sν_Q≤1 给出，未从 density cap 倒推出 support。8.2 的 floors 及 optional angular width 重用已审 UNB001。

8.3/§7 的 matching 使用预选 common stable comparison ball、各色 individual reference weights和 stored marginal floors；neighbor jets 只引入有限重复。选 dense bad group 后 B/W_c 的逆分母明确付 K，故 Cor3.4 使用原非均匀 π，而非将每个 tiny pair 单独均匀化。reverse list 也由 individual floors 在同 graph band 下相加获得。

§8 的 long→short 变化估计依赖真实 wide inequality。C_d=10/(1-d) 保证 d+d/C_d<(1+d)/2<1；a₂ 的 c₂<(1-d)u/4 为后续 offset 精度留正余量。

§9 的随机匹配保 source Φ₁ ceiling 和 target 的 conditional π kernel。每固定 source/target direction只有 K 个 coarse derivative polynomials，细 Φ₁ 只增加 N^{du} 常数 offsets。计入 exceptional U-length 与每 offset 的 value length 后，坏质量为 K N^{-3(1-d)u/8}；积分按 time-bin 长度求和，未额外乘 bin 总数。

Cartesian interpolation 只先给 bilinear 第一系数；稿中又在选择前冻结 angular upper，以 non-axis 长见证消掉 mixed term。这个额外步骤必要且已付。减去共同 base quadratic 后，输出 residual list 去掉 velocity 的过程重新 floor true-base/x states；8.2 的 reference prior 保 full assignment，最后 P_new 的 hidden derivative/curvature 沿用 native test，符合 proper candidate 接口。

## 4. horizontal 归约、减 affine 与任意 fine states

§10/8.5 的 small interval 给 trajectory-constant **evaluation** lists；并未要求 row T 本身沿线常数。两方向插值与 palette-product multiplicity 给每位置 K row bins。7.7 后 non-small skew 情形逐 true child 的 time extent 与 row recovery 比较才得到 k≥ℓ；k>ℓ 的 strip gain保原质量。剩余 k=ℓ 的 H/H² box 描述适用于整个 true domain。

§11/8.6 的巨大 affine part 处理正确。先减任意 affine part，ASM 控制二阶以上 jet 为 KM_f，再把实际方向换成水平理想方向，所以误差是 KM_fN^{-e}。不能把该项写成一个与 affine height 无关、未经证明的绝对 K N^{-e}；root没有这样做。

独立核算 X=∂t−Z∂Y、Zop=∂Z+t∂Y、T=[X,Zop]=2∂Y，T central：

\[
X(XZop+ZopX)-2ZopX^2=3TX,
\quad Zop(XZop+ZopX)-2XZop^2=-3TZop,
\quad T^2=X(TZop)-Zop(TX).
\]

由三方向平方与其固定阶导数推出所有 Hessian 分量，Taylor 后 M_f≤KΔ+KM_fN^{-e} 可吸收；无需先给 M_f 固定幂上界。全块外推仅用同 assigned block 上的 affine trajectory signal。

§12/8.7 使用 ν♭=ν(.|Q_r)，未改成 L-success posterior。精细 residual state 的可读性来自更深 true stable graph 及 bounded g_R=(f_R−L)/a_r 的 jet，**不是**把 horizontal equation 延长到任意细精度。pure cap在 exact L 周围对原 hidden 宽 pa_r 积分；conditional velocity 再由同 entry 的 numerator/floor 获得，故联合 cap没有乘两个无关 marginals。

8.8 相邻 affine fits 的 whole-child witnesses、差函数 norm 与 slope increments均保原 law；缓慢 depth grid 的相邻比与 telescoping只耗 K。§13/8.9 全盒计数先存 full-domain witnesses，再把所有 meeting true boxes 放入共同 H⁴ enlargement。由 unit cap除各 label floor才得 a_s^{-d} label count；既没有只数成功 L 条件 prior，也没有从 point count 反推 whole support。

full-time coefficient clustering 对每个假定稠密 light-bin residual重做。普通 coefficients 有 K bound，D≤a_s≤h_s²，故同 coefficient entry在小 time bin 的整 stored mass落于同标量 band；用原 band cap除该 entry floor得到 current point 的 K-list，这一责任已付。

## 5. 原9.2：同 law 三次切换与 intercept 质量

已独立逐式核 B §§3–4、root §§14–15。x′始终是完整 Q_r-time 导数；深 L_{3s} 的 error a_{3s}/h_{3s}≪a，三方向 row-list可用7.7。primitive F_* 的 slope 可为 K/H，且 N^{-e₀}/H≪a；没有偷用初始坐标的绝对 K bound。

intercept C 是完整 indexed trajectory datum，switchstate也含 C。两个 conditional heat baths均保持同 μ̃，所以每次 trajectory/time refresh保 C。good-line condition是相对固定 block prior 的 marginal lower；它和 μ̃≤K prior×dt才推出该 line 的 conditional time density≤K。good/regular限制只乘 indicator，不重新归一 transition kernel；完整过去给定下仍有 Kπ³dt₁dt₂dt₃ 的 domination。

独算 signed endpoint map 的 determinant为 2(c₂−c₁)(c₃−c₂)(τ₂−τ₁)。固定终时与 Z_f 后，其余两 time 位于非平凡线，Y_f 是二次；regular solutions≤2，允许 c₃=c₁ 与未排序 times。cell probability Kω³ 成立。每 C 的失败率只知 weighted average o(1)，稿中正确取 e_C≤1/2 的 bins，并未虚构逐 C uniform mixing。

upper (base cell,C) count 的四次尺度比包括 time subblocks；与 endpoint lower count消去后，重 intercept raw mass为 m_QsN^{-dc}/K。最后乘 q_rν_Qr、保持 q_desc/ν_desc 两因素，proper test hidden derivative1、curvature0，均符合 Def4.10。

## 6. 原9.4–9.5：fixed ν_H、迭代及真端点

root §§16–19/B §§5–9的 G(u) 是每 dense input、每子列的命题。预先冻结 child pair witnesses，再应用 G(u)；比较个体 reference floor在 group/time domain 总和有限。原 joint cap经 determinant-one P→(Z,Y) 与共同 jitter给 matching 原边缘；没有由 postconditioning H₀ 的 law冒充旧 witness floor。

在每 H₀ chart 固定 ν_H。λ_H=f_Hν_Hdt 的 low-f trim提供双比较；line/time-bin duration trim后才能把 integrated cap变成固定时刻 ν_H cap。后续限制 E_l 保其 upper。仅 λ_H≤Kν_Hdt 本身不能做这一步，整合稿显式补足了该责任。

S_w support 使用 H₀ 条件化以前的 whole-child pair witness计数，且 D₀/h_{s₀+E}²≪ζ。F 的时间比较没有先假 Euclidean Lipschitz：同 line weight 的 Jensen lower与 K(r/M)^{1-d} upper、interval anchor/residueclasses给出合法限制。slope regularization 使用真实 heavy coefficient/time-bin entries，其整 stored mass在 cube enlargement内；fixed ν_H(B_r) lower在之后 label restrictions下保持，因而 (q/r)^{2+d} conditional cap可用。

first-jet 指数核为 ζ=N^{-E}≪(N^{-E/4})³/K，读数 θs₀=(1-d)E/1000<(1-d)E/256。entropy 小只提供 subpower lists；稿中另删除 tiny conditional probabilities、选一个 chart time、用 long durations恢复质量，再由 exact affine evolution产生 wholetime predictor。

端点没有只以 u_j→2k 结束。实际 D_j→D_* 的比例 R_j=N^{o(1)}可能发散；保旧 labels，按新格 split，norm付 K_j(1+R_j)，新 floor 总阈值付 K_jR_j²，再删除轻 splits。对每给定输入进行 finite-stage diagonal，不声称一个 diagonal对所有输入同时有效。固定 reconstruction exponent buffer先于 s_max，随后更细积分不再调用近似 horizontal reconstruction。这些步骤使 G(2k) 的 actual objects、simultaneous-use floors 和 full chart denominator 都成立。

## 7. 原9.6：shared time、原角 cap及回传

官方 TeX 中 s_b=\tfrac32s₀，即 3s₀/2；提取文本的“32s₀”是串行分数误读，不是 source 数学反例。采用真实值后两误差为 N^{-ks₀/2} 与 N^{-(1-2k)s₀/2}，κ取其固定小余量正确。

subcritical 的 G₀ 是 chart/timeblock共享信号。选一 line仅用于找到 quadratic time polynomial，在其 T_b 上再恢复所有 paired lines，保留质量≥M_H²/(4K)，不是只保一条可能零 prior mass的轨迹。H_corr 的 W-derivative逐式等于 b₀+b₁t+b₂t²，且仍 affine-in-P、affine-in-time；whole signal x°沿原 trajectory affine。

三个深度的 Δ_i≤5B_*/16 同时满足 directional collapse 和 wide margins。P̃→(R,R′) 的 |det|=2：按 (R,R′) 顺序，矩阵 [[−2t,1],[−2,0]] 的 determinant为+2。此前写−2是 minor 符号误记，不改变质量或 cap结论；optional angular factor由同一原 joint cap积分获得。support另由 condition前 witnesses与共同 horizontal H⁴ box证明；subcritical额外 A₀^d band factor不能省，整合稿保留了它。所有 reconstruction只在较粗固定 buffer内使用，σ_R=N^{-20s₀}的评价误差有显式余量。

回 α-slice 后，P#的第一坐标是常数，第二是 Y+tp_α，所以 predictor确为原 (t,Y) 上 degree≤2；不是将任意 parameter quadratic免费当 physical quadratic。每 label ≤KD₀/χ slices且每 slice numerator πχD₀a_si^d，总费用≤KπD₀²a_si^d，three layers的 current floors有真实预算。最后 fine conditioningstate不含 projected predictor标签，避免 palette 相关性；trueQ已在 state内，选 heavyQ不再改 conditional velocity law。

最终 mass乘回 q_rν_Qr，q_desc=q_rH_s、ν_desc=ν_Qrν♭(Q_s)相消正确。所有 time/strip alternatives都可从任意原 substantial residual重新准备，足以接已审 AIM，而非仅某个概率归一后模型的存在结论。

## 8. 最终判定与未解除的责任

没有发现必须修改的实质数学缺口。此次核对明确了三类易误用接口：7.7 的不同冻结 law及 λ 符号；8.6/8.7 的 affine-height相对误差和超细 state；9.5 真端点与9.6 all-lines 质量恢复。root/B当前稿均已显式处理，不需将 toy countermodel或 generic OBS002 当原 factorized source反例。

本次结论限于原正有限窄度 candidate branch及所列应用。TCM/ASM/TEX/CRP/AIM/ISO/UNB按已有证书范围重用；OSS、经典 fixed-iterate additive combinatorics和已发表 WZ/CV按具名输入使用，未在此重新认证全高级证明；CRP所依新GWZ输入、完整2.17/finite-Hausdorff读出、KT高维 transfer的各自责任仍独立保留。未据本审查清除 fullsource 或宣称无条件六维17/4、一般Kakeya解决/重大新成果。
