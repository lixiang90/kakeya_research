# R0030：Lemma3.3 的原先验、预选质量与 fresh refresh 审计

2026-10-17，子任务 B。已读 GOAL、STATE、ROADMAP、registry、AGENTS、R30 macro/spec、R29 next，并执行 context.py。原件为库内 `openai_2026_four_dimensional_kakeya.txt` §3.2，PDF29–35，重点 (3.3)、(3.13)–(3.18) 及 endpoint 体积调用。

**本稿结论：双 index–time marginal、subpower restriction、预选 atom masses、交替 fresh resampling 和原成功 law 的 product upper 链成立。未发现把条件 law 免费独立化或从 dense relation 假大矩形的错步。** 以下给出完整概率/质量证明，并核它如何与原 Jacobian/target 体积接合；jet 尺度和精确控制逼近另由 root/A 独审。本稿不因此认证整篇四维证明、无条件六维新界或长期 Goal 完成。

## 1. 本轮命题、量词与检验边界

固定 D≥1、整数 J>D、d₀<1。原 Lemma3.3 断言不存在 N→∞ 序列：两 C^{J+1} lists 各至多 N^{d+o(1)} 项，d≤d₀，函数至 J+1 阶导数均≤K=N^{o(1)}，有 event probability P₀(i₁,i₂,t)，两色分别满足

\[
P_{0,\kappa}(i,dt)\le K\pi_{\kappa,i}\,dt,
\qquad \sum_i\pi_{\kappa,i}=1, \tag{1}
\]

且每 event 的 value gap≤K/N，而某 1≤j≤D 的 derivative gap≥1/K。π 可极不均匀、可有零权；两色和 t 不独立。若 D 非整数，导数索引取 j≤⌊D⌋，以下概率证明不变。

本审计目标是：所有实际 restriction、conditional atom、refresh、adaptive arm 和完整 history 下，原 (1) 仍以已付 subpower 常数使用，并能推出 (3.18) 的共同 domination。停止条件是发现真实分母、边缘分布或隐藏依赖错误；只给每对函数 sublevel upper 不能完成该审计。

## 2. 限制与归一化：π 保留，但分母不消失

若 0≤χ≤1、q=∫χdP₀>0，定义 P=χP₀/q，则

\[
P_\kappa(i,dt)\le(K/q)\pi_{\kappa,i}\,dt. \tag{2}
\]

所以 q=N^{-o(1)} 的有限次 restriction 只扩大 K。无需改变 π，也不能声称 restriction 后仍以原 K 成立。若 q 是固定正幂小量，不能在此阶段免费称 subpower。原 proof 在 bounded-length experiment 前只作 subpower selections，符合 (2)。

后面的 successful kernels 全部保**未归一化**质量；若事后把 survival law 除以其可能很小的 mass，(2) 的分母会重新出现，原 proof 没有这样做。π_i=0 的 index 在所有保留事件中为零质量，可忽略。

event 空间为有限 index product 与实 interval 的标准 Borel 空间，原 marginal upper 也保证各 index–time law 对 dt 绝对连续。因此所用正质量 atom 条件 law、regular conditional kernels 均有合法版本。

## 3. 预选 atom 计数与 (3.13)–(3.15)

固定全部有限 grid 后，记 refinement 前的 event law 为 p_pre。F_a 是嵌套有限 states。一个 color index 加 finest time interval I₁ 决定该 arm 全部历史；另一 arm 在每个已记录 level 的 bins 只在 subpower 邻域中。固定 grid 的 coordinates 数有限，故

\[
|\operatorname{supp}F_1|\le N^{d+r(1)+o(1)}. \tag{3}
\]

这一步是实际 jet/bin 邻接计数，不是对 event 条件概率的主张。

可先删 p_pre 极轻的 finest atoms，使删除 mass→0：若 finest support≤N^{U+o(1)}，选一个趋零但比该 o(1) 大的 ε_N，并删 mass<N^{-U-ε_N} 的 atoms。之后在固定有限各 levels 的 logarithmic atom-mass bins 上共同 pigeonhole，保 subpower event mass。抽 subsequence 后，所有保留 atoms 的 **p_pre 原质量**均为 N^{-u_a+o(1)}，其中

\[
0\le u_a\le u_c\quad(a<c),\qquad u_1\le d+r(1). \tag{4}
\]

父 atom 原质量不小于任何 child；finest 剩余 mass 下界给 (4) 的上界。选出的 event subset 未必由 whole atoms 构成，这不影响下一步。

固定保留父 atom A、level c>a。其保留 children 都是 p_pre 中 disjoint atoms，且原 mass≥N^{-u_c-o(1)}；父原 mass≤N^{-u_a+o(1)}。因此

\[
\#\{\text{retained children of }A\}
 \le N^{u_c-u_a+o(1)}. \tag{5}
\]

原 (3.15) 正确使用 p_pre，没有声称最终 P 的各 atoms 仍同质量，也没有以未来 survival 条件概率代替它。最终 P 正规化后的条件 law 可以高度不均匀；(5) 完全不需要它均匀。

## 4. Palette entropy 的坏事件在原 P 下计费

以下 P 为所有前置 selections 后的 normalized event law，并按 (2) 增大 K。固定一条 active m-piece 和其 A₀。palette Z 是两 arms 在 A₀ 的 m-th derivative finer bins。因为 F_{A₀} 已记宽 N^{-β_m} 的 bins，进一步缩 N^{-D₁b} 后

\[
H(Z\mid F_{A_0})\le2D_1b\log N+O(1). \tag{6}
\]

定义 L_a=log[P(Z|F_{a+Cb})/P(Z|F_a)]，在 sampled Z 处求值。由嵌套 conditional entropy chain，overlap 最多 C 次，

\[
\sum_a\mathbb E L_a\le C H(Z\mid F_{A_0}).
\]

负部对任意概率向量 p、q 有

\[
\sum_{p(z)<q(z)}p(z)\log\frac{q(z)}{p(z)}\le1/e.
\]

条件于 finer state，p 是 fine palette law、q 是 coarse law，故每 step 的负部 expectation 有统一常数。总 steps O(b⁻¹)；平均正部 expectation 为 O(b²log N+1)。在 threshold b^{5/4}log N 上两次 Markov，得到除 O(b^{1/2})+o_N(1) 比例外的 steps，其原 P-bad probability≤b^{1/4}，并有

\[
P(Z=z\mid F_{a+Cb})
 \le N^{b^{5/4}}P(Z=z\mid F_a) \tag{7}
\]

在非 bad 的 sampled event/palette 上成立。这里没有宣称 (7) 对所有 finer atoms、所有 palettes 点态成立；后续在 refresh 抽到 bad 值时直接 kill。

## 5. 两种 heat-bath kernels 及原 law 的不变性

对任何有限 state partition F 定义 refresh kernel

\[
R_F(x,dy)=P(dy\mid F(y)=F(x)).
\]

若某未归一化 current law ν≤cP，则对任意 measurable A，

\[
(\nu R_F)(A)
 =\sum_C\nu(C)\frac{P(A\cap C)}{P(C)}
 \le cP(A). \tag{8}
\]

零 P-mass cells 对 current law 也为零，故无除零。P R_F=P。这是依 finer atom 的实际相关 refresh，绝不是独立抽整个 P。

固定 color κ 与 coarse time interval partition I_a，定义 arm kernel

\[
T_\kappa(x,dy)
 =P(dy\mid i_\kappa(y)=i_\kappa(x),\ I_a(y)=I_a(x)).
\]

同一计算给 PT_κ=P。若 arm 的选择依赖完整 history、完整 refreshed event，甚至是随机选择，只用选择权重≤1，就有

\[
\nu(\text{adaptive arm traversal})(A)
 \le\sum_{\kappa=1}^2(\nu T_\kappa)(A)
 \le2cP(A). \tag{9}
\]

此 upper 不要求 given-history current law≤cP；先对 hidden histories 积分，再用 current event marginal ν≤cP 即够。因此从 E⁰∼P 开始，bounded m+1 traversals 中 raw E^p 和 refreshed event marginals 均≤2^pP（按 leg 编号可相差固定一次 2，皆无关紧要）。restriction/kill 后不归一化，domination 继续成立。

原 proof 的“each color kernel preserves P after averaging over index/interval”正是 (8)–(9)。若把 adaptive κ 当独立，或先 condition 全程 survival 后声称仍≤2^pP，才会错误；现稿没有这些操作。

## 6. Bad pair、条件 time density 与 separation

记 arm atom C_{κ,i,I}={iκ=i,I_a=I}，p_{κ,i,I}=P(C_{κ,i,I})。kill 被选 arm 满足

\[
p_{\kappa,i,I}<\pi_{\kappa,i}|I|/\log N. \tag{10}
\]

对每个 color，所有 bad arm atoms 的原 P-mass 总和≤∑_{i,I}π_{κ,i}|I|/log N=1/log N。原 π 无需条件化；I_a 是整 unit interval 的 partition。由 refreshed marginal≤2^pP，即使 κ adaptively 选，bad pair 失败 mass≤2^{p+1}/log N。palette bad 失败也只再付同样固定 2^p 因子。

在 retained pair 上，给定完整 refreshed event 及实际 chosen κ，下一 event 从 **P 的该 arm atom 条件 law**重新抽取，所以其 time marginal 满足

\[
\frac{P_\kappa(i,dt)1_I}{p_{\kappa,i,I}}
 \le\frac{K\pi_{\kappa,i}}{\pi_{\kappa,i}|I|/\log N}\,dt
 =\frac{K\log N}{|I|}\,dt. \tag{11}
\]

这是全部 conditional denominator 的支付处。π 再小也抵消，常数不依赖其最小正权。将时间归一为 s=(t−t_a)N^{r(a)}、|I_a|≈N^{-r(a)} 后，密度≤K′ds，K′ subpower。

internal times 两两 separation 可显式取 1/K_sep，其中 K_sep=K′log N 乘固定 J² 常数。在 normalized bounded interval 内，每次 hit 之前 O(J) 个长度 O(1/K_sep) 禁区的 mass≤O(JK′/K_sep)=o(1)。最后把 K_sep 的固定幂和其它 subpower factors 合并为新 K；这样没有先说“1/K separation”再用同一个 K 作 density 的循环。

故先固定足够小 b、再取 N 大，bounded-length experiment 的 averaged successful mass≥c_J>0。没有要求对每个 exact start 有 uniform survival lower。

## 7. 共同 coarse 邻域和同一个控制 measure Λ

每一步 refresh 保 F_a，因为 finer state 包含它。traversal 保 chosen index 与 I_a，因而保 chosen arm 在 a 及所有更早 levels 的历史；另一 arm 在两端的各级 bins 均距 chosen arm 仅 K 邻居。bounded m+1 次、固定 grid 下，所有 possible coarse states 都在由 exact start 决定的 N^{o(1)} 个邻居中。不是“稠密关系包含大矩形”的论断。

原 Taylor construction 给每个 coarse state C 和 palette z 两个 deterministic control codes U_κ(C,z;start)，只需保留未出现 C 为零质量。它们只用 coarse earlier data、palette 和固定 frame，不依隐藏 line identity；actual traversal 误差由原 (3.17) 单独控制。

对固定 exact start，定义有限正 measure

\[
\Lambda=\sum_{C\in\mathcal N(start)}\sum_{\kappa=1}^2
 (U_\kappa(C,\cdot;start))_\# P(Z\in\cdot\mid F_a=C).
 \tag{12}
\]

因此 Λ(R)≤2#N(start)≤K，且同一个 Λ 对该 start 的所有 admissible hidden histories 有效。Λ 可原子化，不是 Lebesgue 控制 law。

给定完整过去 H_p，它确定 current finer atom F、其 parent coarse C。fresh event 的 law **恰为** P(.|F)，与剩余过去条件独立。在 (7) 的 good palette 值上，palette law≤N^{b^{5/4}}P(Z|C)。adaptive chosen arm 的推前 upper 由两个 candidate controls 之和控制，再用 (11) 的新 time upper，得到未归一化成功 step kernel

\[
Q_{H_p}(dU\,ds)\le K N^{b^{5/4}}\Lambda(dU)\,ds. \tag{13}
\]

新 event 仍可含隐藏另一 index 和 witness 依赖；(13) 只支配下一对 displayed (U,s)，没有声称 full event conditional law 成 product。

## 8. Backward iteration：为什么隐藏依赖不破坏 product upper

若 Ψ≥0 只依 exact start 及 displayed controls/times U₁,s₁,…,U_{m+1},s_{m+1}，从最后一步开始，固定其完整过去 H_m，用 (13) upper integrate 最后 displayed pair。结果只依先前 displayed pairs 与 start，不再依 hidden history。如此倒推，可得

\[
\int \Psi\,d(\text{successful path law}\mid start)
 \le (KN^{b^{5/4}})^{m+1}
 \int\Psi\prod_{p=1}^{m+1}\Lambda(dU_p)\,ds_p. \tag{14}
\]

这里使用的是所有 future success 条件的**必要** displayed test，可丢弃其余 hidden success 条件增大 upper；从未 condition future survival。若不同 histories 用不同 Λ、或 test 仍依 hidden final index，则 (14) 不会如此推出；原 proof 已分别用邻居求和和 target union 排除这两个问题。

此为真正原 successful law 的上界，不是假设 g 因子化后的新 product law。averaged lower 来自 §6，对 exact start 的 (14) upper 最后再按 P(start) 积分即可。

## 9. Jacobian/target 如何与原 mass 接合

给定原几何已建立的 control approximation/jump estimates，endpoint 使用 exact-start jets 与 constant controls 积分。对 fixed controls，其从 m internal times 和 final time到 low jets/final time的 polynomial map degree 仅依 J，Jacobian 为

\[
\frac{\prod_{p=1}^m|U_{p+1}-U_p|
 \prod_{1\le p<q\le m}|s_p-s_q|}
 {\prod_{k=0}^{m-1}k!}. \tag{15}
\]

retained consecutive controls 和 §6 internal times 的 separation 给其下界 K⁻¹。非零 Jacobian 的 fibers 是 isolated regular roots，固定 degree/dimension 的 polynomial system 有统一有限 multiplicity；这可以用 complexified Bézout 或固定格式 semialgebraic fiber bound 支付，不需 coefficients 非退化下界。

每个 final child c=a+b 的 low-jet fiber widths 为 KN^{−(1−j/m)b}，j=0,…,m−1，final-time width 为 O(N^{−b/m})。故单 target volume≤

\[
K N^{-bL_m},\qquad L_m=1/m+(m+1)/2. \tag{16}
\]

中心可随 final time 快动，Fubini 只积分这些 fiber widths。两色与所有 start coarse 邻居的 retained children，依 (5) 总数≤N^{u_{a+b}−u_a+o(1)}。这使 target union 只依 start 与 displayed endpoint，不依 hidden final index。

对每 fixed separated control tuple，area/change-of-variables 加 (15) 得 time preimage measure≤K×target volume。再对 Λ^{m+1} 积分，原子 Λ 也合法，结合 (14)，conditional success upper 为

\[
N^{u_{a+b}-u_a-bL_m+(m+1)b^{5/4}+o(1)}. \tag{17}
\]

所有 K 为固定 grid 下 subpower，统一于 start；与 averaged success≥c_J 接合，得

\[
u_{a+b}-u_a\ge bL_m-(m+1)b^{5/4}-o_N(1)
 \ge b(1+1/m-o_b(1)). \tag{18}
\]

最后不需要 success image 的概率 law 等于 Lebesgue；使用的是其 time-domain 上的 bounded density upper 与 Jacobian。若只说“Jacobian 非零所以原 event law 有 image lower”而未经过 §6–8，则不成立。原 proof 用的是本节的正确链。

## 10. 极限、uniform fixed-power 与验收范围

所有 grid/trim/b 先固定，再选 atom masses、subsequences 并让 N→∞。因此 K^{O_J(1)} 与 fixed grid 的邻居数仍是 N^{o(1)}。随后 b→0，good steps 缺失比例 O(b^{1/2}) 消失，再撤 trim。(18) 的 b 項总和→1，b/m 項→∫r′=r(1)，和 (4) 给 d+r(1)≥1+r(1)，即 d≥1。此时只使用各次 grid 的统一 u₁ upper，不要求不同 grids 的 exponent selections 相同。

若无任何足够小 fixed-power tolerance，可取 losses ε_k→0、N_k→∞ 的反例，在固定 D,J,d₀ 下组成 subpower countersequence，违前述结论。这一步是量词对角化；不提供可计算 ε_* 或对 D/J 的 uniform 模数。

本子任务认证的实质为：原 π 无需条件化、preselection mass 与 final conditional law 不混用、adaptive fresh refresh 的原 marginal 控制、同一个 Λ 的逐 history upper、未归一化 backward product test，以及 endpoint volume 对原成功质量的合法调用。一般 D/J 的 jet/Taylor 前提仍需与 root 的独立几何证明逐式合并，不能用本稿概率部分单独宣称 Lemma3.3 全证。

没有构造完整 source/Kakeya 反例，没有采用 AD lower、uniform π、Cartesian dense subrelation 或任何额外独立性。R29 六维链的完整源条件只会在所有必要 gateways 逐项核过后才可能缩减；本轮通过这一概率链不等于完整四维或高维认证。
