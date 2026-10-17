# R0032：共同 anchor、代表表与整段轨迹分配审计

2026-10-17，子任务 B。已读恢复入口、R32 spec、原 Lemma3.5 PDF36–46及 Def2.1/2.2/2.8、Lemma2.9/2.10 的接口，执行 context.py。仅编辑本分配文件，不操作 Git。Part1 的 paired mass/normal-frame/heavy-group comparison由 root/A独审；本稿逐式核其后如何真正产生两原版本的 known atlas。

**结论：以原 Part1 的 (3.27)、(3.28)、(3.31)–(3.34) 为已付输入，Part2/3 的共同随机 anchors、代表表、source-evaluation 回传、先验质量冻结、唯一 whole-block assignment、旧 p_L subpower lists和曲率归一化链成立。** 没有发现 source identity 被偷偷加入 output label、把代表 branch强续回 source、或 condition on pair success改原 assigned prior 的错步。本稿不是只验证局部 graph，也不单凭后半段认证完整 Lemma3.5/整篇四维证明。

## 1. 固定量词、原两版本与需交接的 Part1 输入

固定 d₀<1、angular S/η、原 model version/test degrees。原 N=N₀→∞，length L fixed，δ=N⁻ᴸ，old true terminal length q₀=N^{-h+o(1)}，q₁/q₀≈Nᵉ，0<e<h。先按 world 作 w→Bw，使 derivative unit为1，末尾逆变换；version1本来B=1、hidden w(t)可二次，tests限 w−F(t,y)；version2 y/w trajectories全affine、tests total degree≤2。

所有 subpower K在原 exact sequence 中取值；任意 fixed e>0，N充分大时可吸入任意预留 N^{ce}。**N^{O(e)} 的 exponent constants**只许依 fixed model/angular/degree，不能依 L、h、old polynomial complexity exponent。后者可以影响 tempered ranges与充分大 N 的阈值。

本稿使用的 Part1 成果为：old label数≤KNᵉ/n_Q；source frame D由old source A确定；(A′,D) compatibility每A′仅subpower个；normalized source base z₀-density≤n_QN^{C₁e}，其中 n_Q=n(L)q₀ʲg；转换后 discriminant coefficients/derivatives在fixed complex boxes上≤N^{C_de}，tested z₀处值介于N^{-C_de}与N^{C_de}；stable simple branches f、f′在local fixed-relative-margin balls上 close≤δN^{C_*e}。这些均针对未归一化原 pair restrictions，不额外要求每个later entry保floor。

## 2. 随机共同 anchor 的低异常概率

每 D 带 world/new block context，独立选择 α_D 于固定有 interior 的 bounded complex box，σ_D 于固定 bounded complex disk。对 retained pair用 base line z(s)=z₀+s(α_D−z₀)，参数路径0→σ_D→1。每 pair只访问其一个 D，不对全部 pairs或D作 polynomial-size union bound。

固定 pair的任一 converted discriminant Δ(z)为固定 degree polynomial，coefficients≤N^{Ce}，且 |Δ(z₀)|≥N^{-Ce}。有限维 polynomial norm equivalence给 anchor box上 norm≥N^{-C′e}；polynomial sublevel estimate遂给

\[
\Pr_{\alpha_D}\{|\Delta(\alpha_D)|<N^{-Be}\}
 \le C N^{-\theta(B-C')e}. \tag{1}
\]

取 fixed B大，可使两 equations一起的失败 probability为 N^{-Ω(e)}。这里不需要 Δ 的 numerical coefficient lower，point value已供 norm lower。

条件于好的 α_D，p(s)=Δ(z(s)) coefficients≤N^{Ce}、p(0)、p(1)≥N^{-Ce}。固定 bounded path region上 derivative upper使 endpoints距其内 roots至少 N^{-Ce}。对 boundedly many roots去半径 ρ=N^{-Be} 的 disks，B再放大；从0或1出发的 segment打中一 disk，其 σ_D shadow angle至多 Cρ/dist(root,endpoint)，故 probability N^{-Ω(e)}。

路径避开 disks后用**比值 factorization**

\[
\frac{p(s)}{p(0)}=\prod_r\frac{s-r}{-r}.
\]

bounded roots的 numerator≥ρ、denominator≤固定常数；far roots对 bounded path的比值有 fixed positive lower。故 path上 |p|≥N^{-C″e}，无需 lower-bound leading coefficient或所有root sizes。constant/nonzero p时直接用其point lower。

full z-variable gradient≤N^{Ce}，再将tube半径缩成 N^{-C_path e}，便使两discriminants在真正 complex base tube上 nonzero并有inverse-power lower。source/anchor comparison balls半径可取这个tube半径与stable source radius的fixed小倍，保 common fixed relative margins。所有 constants在后续C₂/C₃/T之前确定。

将 (1) 和 detour failures对原 weighted pair law平均，异常总 mass为 power-small；同 D共享随机点不会损坏 Fubini，因为每pair的 pointwise bad-probability upper统一。没有声称一个随机表对所有pairs同时无失败。

## 3. Anchor jet bins：为什么知识表不是 N^{O(e)} 大小

先用3.1把local real norm comparison扩到interior complex source ball，再用3.2沿上述two-sheet-safe path延拓。anchor上的差及所需 fixed jets≤δN^{C_close e}。选 fixed bin exponent C_b>C_close，spacing为

\[
s_b=\delta N^{C_be}. \tag{2}
\]

complex jets分实虚部，tuple length固定。两tuple差/s_b为 bounded（事实上趋小），所以相邻 bins数是固定常数或subpower，**不是**N^{C e}。

已选 source branch在source点距实际w≤δN^{Ce}，实际 trajectory coefficients polynomial，implicit differentiation分母在point有inverse-power lower；以finite jet控制source norm，再用3.2传播branch自身，得到其reached jets的polynomial ranges。其指数可依 exact problem，但 fixed finite degree/jet order使总 bins数仍 polynomial。unused escaping root不必存入该range。

给定 witness A′，先枚举subpower个兼容D。每个D的 converted witness equation在anchor至多两个simple roots；fixed jets由root与equation确定，任意continuation只能互换这两个tuple。每tuple的bounded neighboring bins再交stored range，给source b的subpower list。旧p_L先给subpower A′list，组合后仍subpower。

实现此枚举不必储存unused far root。若constant quadratic coefficient极tiny，公式中1/c可能superpolynomial；正确有限编码是用原quadratic relation及root/jet属于stored polynomial bins的有界量词检查，只存range内bin。implicit differentiation可用已付lower的P_w=±√Δ作分母，不把tiny c⁻¹写入output。故“至多两根”是计数，不是要求把两根数值都作为polynomial-bounded输出数据。

world与new block可从p_L中的γ、exact t读出，anchor/detour/table是事先固定的数据，不是额外未观测变量。若在 output label保old source A或允许N^{Ce}个邻bins，则上述knowledge不成立；原构造明确没有如此做。

## 4. 代表表必须是 anchor 参数的函数，不能依 source t₀

对每(D,b)，从所有old source subblocks的converted **real equations**中按固定顺序选第一个eligible P_b：固定discriminant coefficient bounds、anchor inverse-power lower，以及某simple branch jet属于b。原success source本身eligible，故success bin有entry。

eligibility和代表表只依 anchors/D/b/finite old equations，**不依采样 t₀或trajectory**。虽然末尾可以联合选择优化(a,t₀)，其functional construction仍为P_b=P_b(a,D,b)；这种最终参数相关不把它改成先看t₀后重选representative。

在common anchor ball上，source f与representative branch f̂同bin，bounded-degree difference的finite-jet norm comparison给 ∥f−f̂∥≤δN^{Ce}。代表branch可在complex点取非实值；真正output equation P_b仍real，因为选自real converted equations，不把complex root写成新test。

early conversion后 |P_b,ww|≤δ⁻¹，且在f̂上 P_b,w²=Δ_b 的anchor norm≤N^{Ce}。Taylor in w得

\[
\|P_b(z,f(z))\|\le\delta N^{Ce},\qquad
\|P_{b,w}(z,f(z))\|\le N^{Ce}. \tag{3}
\]

二次误差为 δ⁻¹(δN^{Ce})²=δN^{Ce}，不含 old coefficient-height exponent。

## 5. 回传的是 source polynomial evaluations，不是代表根

(3)中的函数是source branch f的fixed-degree polynomial evaluations。沿**source-safe** path反向用3.2即可回到source ball；不需要代表 discriminant在该return path nonzero，也不需要代表在real source附近有root。尤其不能把f̂强行延拓回source来证明fit。

在source own incidence有 |P_A,w|≥K⁻¹，而沿assigned line的P_A,w affine、whole-block upper≤N^{Ce}。取normalized length≥N^{-Ce}的一侧segment使derivative lower保constant fraction，再缩入source ball。early curvature cutoff确保 |P_A,ww P_A|≪|P_A,w|²，可连续使用(3.24)追**同一个**source root；converted affine source则直接用critical-center estimate。t₀靠block边界时取one-sided segment，长度仍同阶。

于是实际w与f(z)差≤δN^{Ce}；再次用 |P_b,ww|≤δ⁻¹把returned evaluations转成实际trajectory上bounds，最后用fixed-degree polynomial interpolation外推whole new block：

\[
\sup_I|P_b(z,w)|\le\delta N^{C_2e},\qquad
\sup_I|P_{b,w}(z,w)|\le N^{C_2e}. \tag{4}
\]

version2全部coordinates affine，degrees为2/1；version1因为test保持w−F，虽w quadratic，沿line仍degree2且P_w=1。不能把version1放宽到含w²的一般quadratic而仍用此degree理由。

## 6. 代表 discriminant 的 source lower：C₃在T之前

固定所有anchors及相应代表表。每个Δ_b有anchor lower≥N^{-b_anc e}，fixed polynomial norm comparison给real z-box的norm至少同一形式。fixed θ>0的sublevel estimate给

\[
|\{z:|\Delta_b(z)|<N^{-C_3e}\}|
 \le C N^{-\theta(C_3-b_{anc})e}. \tag{5}
\]

固定 source label A，其D唯一，converted source equation在fixed anchor最多两个root/jet tuples，因而至多两个source bins及bounded个representatives。变化的 paths/homotopy classes不会增加此数。不能按全table的polynomial bin数去union，否则会引入problem complexity。

对source A用原source-base density upper n_QN^{C₁e} charge (5)，再乘 old source count≤KNᵉ/n_Q，得到

\[
\text{bad mass}\le K N^{[C_1+1-\theta(C_3-b_{anc})]e}. \tag{6}
\]

选 C₃>b_anc+(C₁+2)/θ，异常为power-small。此计费在t₀仍平均时进行，且table对t₀不变；anchors固定后restrict pair law也不增原density。**C₃只依已固定table/continuation constants，不依后选curvature T。**

## 7. 冻结只能保 weighted 总 mass，不给各block虚构下界

令a为全anchor/detour表，S为通过(4)及 |Δ_b(z₀)|≥N^{-C₃e}等全部restrictions的事件。每world/block定义

\[
s_{\gamma,I}(a,t_0)=\int\int_I1_S(\ell,t_0,t;a)
 \,d\nu_\gamma(\ell)\,dt/q_1.
\]

有限个world/blocks分别选(a,t₀)使s至少其参数平均，可在其good measurable set中取值。则

\[
M_{fr}=\sum_{\gamma,I}\omega_\gamma q_1
 s_{\gamma,I}(a_{\gamma,I},t_{src}^{\gamma,I})
 \ge N^{-o(1)}. \tag{7}
\]

各block s可能极小甚至0；(7)只保证weighted总量。参数选择不付#blocks或#worlds，因为一直以原ω_γq₁求和。冻结后的measure仍为1_S dν_γ dt/q₁，不condition ν_γ于pair success。

## 8. 唯一 whole-block assignment与去解析 masks 的新selection

在fixed t_src要求old selected source membership。old time partition和disjoint trajectory assignments给唯一A；它确定D及nearest simple source branch。要求source-safe continuation/endpoints、stored jet ranges及representative table entry；定义b。再显式要求whole-block spatial containment、(4)、以及source代表Δ_b lower。

每个满足这些geometric predicates的trajectory赋唯一c₀=(D,b)，**合并所有给同c₀的旧source identities**。该assignment只用fixed source time和trajectory，完全不依later t。它不必只含原成功pair投影的trajectories；新增的trajectory也显式通过whole-block fit checks，故不害atlas有效性。

在这些assignments上，new selection只留原later selected incidences，其old A′ compatibility lists包含D和b。它包含全部frozen successes，所以weighted mass≥M_fr；同时去掉供估计用的one-time/joint density masks、group success和随机search记录。最终selection是旧predicate、固定table和geometric checks的restriction，**不等于**把1_S直接当tempered incidence predicate。

old p_L给A′短list；A′给D短list；每D给至多2 anchor-jet tuples及bounded neighboring bins。因此新c₀确被subpower list命中，不是只有N^{O(e)}个可能。内部trajectory index可用于assignment的原predicates，但不作为observed feature或output标签恢复。

## 9. 低曲率分支：正 discriminant、整段归一化和原prior删时

先固定C₂/C₃，选 C₄>C₃/2+2、C_s>C₂+C₄+1，再取

\[
T>\max(C_2+C_3+1,C_s+C_4+1).
\]

当 |P_b,ww|≤δ⁻¹N^{-Te}，(4)给 |2P_b,wwP_b|≪N^{-C₃e}。source上 P_b,w²=Δ_b+2P_b,wwP_b，连同Δ_b absolute lower迫Δ_b>0并有 |P_b,w|≥N^{-C₄e}。所以M_∂=sup_I|P_b,w|在[N^{-C₄e},N^{C₂e}]。

按M_∂的dyadic lower endpoint v分裂trajectory assignment，label c=(D,b,v)、test P_b/v。v≥(1/2)N^{-C₄e}，full range仅O(log N)个，故knowledge仍subpower。其whole-block derivative max∈[1,2]，value≤CδN^{(C₂+C₄)e}、curvature≤Cδ⁻¹N^{(-T+C₄)e}，均符合thickness δ_s=δN^{C_s e}。version1恒P_w=1，取v=1且仍为w−F。

selected derivative lower另删 |P_b,w/v|<κ 的times。version2该derivative affine、block max≥1；其bad相对长度≤Cκ（斜率太小则small κ下为空，斜率大则inverse derivative直接给此界）。由原disjoint assigned-prior budget，weighted损失≤Cκ；不是对conditioned success time law求density。取κ=N^{-o(1)}且κ=o(M_fr)，例如κ=M_fr²/log N的dyadic小倍，则final mass仍inverse-subpower、incidence lower≥κ。

## 10. 高曲率分支及原坐标恢复

当 |P_b,ww|>δ⁻¹N^{-Te}，F_ctr=−(P_b,w−P_b,ww w)/P_b,ww为real affine base function。沿整个I，

\[
|w-F_{ctr}(z)|=|P_{b,w}|/|P_{b,ww}|
 \le\delta N^{(T+C_2)e}.
\]

test w−F_ctr配thickness δ_h=δN^{(T+C₂+1)e}，derivative1、curvature0，不用representative real root。保持c=c₀与原assignments。version1无此分支。

低/高选有至少半mass的一类，subsequence固定其thickness exponent。令C超过两final exponents和前面smallness constants，再取e<cL，c≤min(1/(2C),η/R及其它fixed小常数)，则0<L′<L、L−L′≤Ce，且 q₁=N^{-(h−e)+o(1)}。这里R是已固定angular depth常数，不是新的尺度。

最后compose实affine base map并undo w→Bw：version1仍w−F quadratic-base；version2仍totaldegree≤2，derivative/curvature分别乘B/B²，恰恢复Def2.8。空间largest radius≤q₁K，因为g#≤1；不要求newtruefloor。

## 11. Temperedness及C与problem complexity的分离

old labels、world/blocks、D、stored jet bins和representative entries皆polynomial多。anchor coordinates/detours/source times只是固定有限表中的real constants；joint优化search本身不编码。source branch的nearest root、path nonvanishing/continuation sign/parity、endpoint fixed jets均有fixed-format semialgebraic描述；3.2的bounded pieces实际用到，root/jet变量数不随N增长。

whole-block test与spatialbounds对每个trajectory只quantify一个time variable；version1/2的along-trajectory degree如§5所核。低curv affine derivative block max可用endpoints，v bins为geometric tests。合并old predicates与这些fixed-degree tests，允许polynomial多的Boolean conditions，满足Def2.2；密度analytical masks不进入最终selection。

old coefficients/trajectory/root ranges的poly exponent可以大，并影响tempered complexity；它只通过O(log N) range choices被吸入subpower，不乘到N^{Ce}损失常数。涉及inverse curvature的两次affine-center转换均有specified cutoffs，1/v也有N^{C₄e} bound；其余coordinate inverses由old tempered widths/B保证polynomial。所有output coefficients/inverses因此polynomial可控。

C/C₂/C₃等独立L、h和complexity的关键不是所有data绝对≤N^{Ce}，而是：heavy-entry discriminant bounds、以n_Q取消oldcount、每A最多2代表、fixed-degree continuation和whole-prior删时损失。这些避免按全poly tables计power-small exceptions。阈值N充分大可依原exactproblem与fixed e，不违反C独立性。

## 12. 验收边界

后半段未发现合法counter。tiny curvature归入lowcase并付v，large curvature用affine center；escaping unused roots不储存；block-light只保global weightedmass；hidden oldsource identity被merge；representative table先于t₀ functional freeze；C₃不依T；selection去解析masks且重建wholeblock assignments。两原model class、oldp_L list和tempered原sequence均已逐项对接。

这仍须与root/A的Part1及原2.9/2.10/Def2.8完整核验合并，才认证一般Lemma3.5。它不扩展到j=3、不恢复旧冻结genericcompletion，也不认证critical paths/后续排除或无条件六维新界，长期Goal active。
