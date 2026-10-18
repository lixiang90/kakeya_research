# R0083：Zahl 直线并集定理的原输入、离散质量与六维价值

2026-10-18，A，phase I。只在 R0083 先锁的有界 primary 输入选择门内核原量词；不施工未锁 phase II，不按预期强拒该定理，也不把参数维数或定性满射放大成新输入。全文恰八节，未经外部同行评审。

## 1. 实际读取、版本与具名证明层级

已实际全文读当前 STATE、R0082 next 六节及 R0083 working_spec 五节；沿用同会话已实际读的 GOAL/ROADMAP、78状态、R82完整稿/两formal和全部冻结范围。本轮未重核无变化的官方三核心，也未重跑旧有限计算。

一手对象为 Joshua Zahl，[arXiv:2208.02913v1 官方 HTML](https://arxiv.org/html/2208.02913v1)及[官方 abs/history](https://arxiv.org/abs/2208.02913)。实际查看 history 仅列 2022-08-04 的 v1；abs 记 8 pages、Mathematika 69(2)(2023), 473–481。root 保存 PDF 后，本人实际全文读其本地八页提取正文，包括 Th1.2、§2 的 Lem2.2–Cor2.6/induction 及 §3 全段应用；前次合批尾部截断后另读回 reference 尾和所需局部，未以 abstract 代整段应用。

本人只读核本地 bytes：147536；SHA256 30d05387fd542928264af829ac8276d980e5f6bb76d372004443133f51f50660；按 Git blob 定义计算 SHA1 为 807e744af6609ed6b2f379b9c85f295ba7ae2fed，与 root 给定一致。没有下载、改 metadata 或运行 Git。主定理按已发表的一手输入使用；§2所引 Carbery–Valdimarsson endpoint multilinear Kakeya Th2.1、HKM analyticity/Frostman 及其它高级 wholeproof 未由本轮新独证。

## 2. 两种原定理、参数和 metric 的完整区别

令 s=2(d−1)+β，其中 d 为整数，1≤d<n、0≤β≤1。Zahl 的 line metric 是最近点 offset 距离加无向方向 wedge 的长度。对 rank-one projectors，方向的 operator-norm 距离正等于该 wedge 值，故它与本项目 canonical (a,P) metric 可比，不需要任意 selector 正则性。

有限 Th1.2 的对象是 B(0,1) 内 unit δ-tubes 的集合，假设每个 line-space ball 的 tube-axis 计数≤(r/δ)^s，结论

    ||Σ_T1_T||_p≤C_(n,ε) δ^((1−d)/q−ε) V^(1/p)，
    q=p′=d+β， V=Σ_T|T|。                           (1)

q>1 是以下 Hölder 应用的非平凡范围。该条件没有原方向分离、PW/CW、同方向唯一、AD lower 或 algebraic format 假设；是 joint axis 参数球 upper。它也不是任意 indexed weights 的 literal 定理，不能将概率权直接塞进计数后省掉离散化。

原文 Th1.2/(3.7) 把 radius 写作 all r；非空 δ 离散族须按有意义的 r≥δ 范围读，literal r<δ 的 RHS<1 不可能容一个 axis。§3 自己使用 dyadic δ≤r≤1。本稿仅使用该标准离散规范，不以这个字面范围推 source 主定理错误，也未宣其全部抽样细节已新独证。

最终 line-union 结论是 Hausdorff 类型：若原 line family L 有 dim_H L≥s，则 dim_H S(L)≥d+β；不是把 finite bound 或 packing dimension 直接当这个假设。对原 n6，只知道方向满 RP5 时，s=5 对应 d=3、β=1、q=4；这些数不是物理 ambient n=6 或原点集维数的重命名。

## 3. 实际读完整 §3：从任意 family 到 Hausdorff 的质量路径

§3 先用与 X=S(L) 同 Hausdorff 维数的 Gδ superset，并在某个 bounded ball 中保足够参数维数及正长度；HKM 的 positive line-content analyticity 给 analytic 的 L2。以小 ε 损失取 exponent s−ε 的 Frostman 概率。这里 analytic enlargement 只授 dim L2≥原门槛，没有保证 strict 参数维数增益；不能把增加了一批可能的 lines 当已经达新阈值。

随后按点集 Hausdorff cover 的尺度 k 对每条 line 选一个有足够长度的层：line-mark 长度和该 common 层的概率质量都只损 polylog。再将 δ-ball 原概率质量按 dyadic level A 均匀化，取 line-space separated representatives，并 independent thinning，将球上计数 upper 规范至 (1.2)，仍留 δ^(−s+O(ε)) 条。每条保留 line 仍有相同下界的实际 cover-length；不是只保总平均长度。最后选其 unit pieces，转 tube-cover incidence，再用 (1) 和 Hölder 对比较 (3.8)/(3.9)，得到 dim X≥d+β−O_n(ε)，让 ε→0。

上述是实际阅读与质量用途核对，不是宣布源 §3 的每个实现常数都已独立认证。其所谓 every ball failure exponentially small 在 r≈δ 并非可无说明统一套用；小尺度 packing/pruning、finite ball net 等标准细节仍属具名定理的 proof 层。本轮不把修补这些细节另立主数学。有限 unit-piece 位置和从 line-length 转到 tube-volume 可通过固定 homothety、固定倍 cover-ball enlargement 规范，不能从任意 measurable E 的 line-intersection 长度免费推原同半径 tube 体积。对本轮 compact whole C，更可先选固定大 physical ball，使每条整线都有统一内段，再作标准 cover 读出，不涉及 line segment extension 猜想。

## 4. 原 fullcompact C 的真实 angular lift 与 line-space 上界

n6 的 π:C→D=RP5 连续满射，C compact；direction projection 对 canonical metric Lipschitz，故 dim_H C≥5。还可实际构造 angular-uniform Borel lift，不必假连续单选：在 C 内取逐级 finite closed-ball covers，半径趋零。对每个方向，递归取按固定次序首个与其 fibre 及此前 compact intersection 相交的 cover-ball。每条有限 index path 的可行域是 compact image 的有限 Boolean 组合，因而 Borel；嵌套非空 compact 交的直径趋零，唯一极限给 Borel s(d)∈π^−1(d)。这只是可测选择，不 contradict R82 排除的连续 section。

令 σ 为 normalized angular measure，ν=s_*σ。对任意 line-space ball B_L(ℓ,r)，

    ν(B_L(ℓ,r))≤σ(B_D(πℓ,Cr))≤C_n r^5。           (2)

所以真实概率确有 exponent 5 的 upper，也给 H^5(C)>0 的下界；没有得到有限 H^5(C)、AD lower、uniform fibre lower 或 exponent 5+ε 的 upper。ν 的 support 可以只占原 C 的一部分，且方向/offset仍强相关；权重也不是独立 time/shading law。

对原 C，本来 compact/analytic，故使用 Zahl 的 Hausdorff 结论无需为 measurable selector 找 Hölder 子集，也不用先做 HKM 任意非analytic family 的 enlargement。(2) 合法匹配 threshold 5，因而得 bound 4 是一个真实可用应用，不能因它未改善旧值就说源假设不适用。不同问题是：原 C 的不交性尚没有在此定理中带来额外收益。

## 5. Closedrestriction、原角度质量与 finite tube spacing

任意 closed C′⊂C 保 compact/不交，方向却可能变小；若其 direction image 仍满 D，重做 §4 即仍有 (2)。若仅保正 angular measure，normalized restricted angular law 也有 upper C r^5/σ(D′)，常数须付；这个 restriction 不再叫 full-direction C。若只知 dim_H D′=5 而 angular measure 为零，可用严格次临界 Frostman exponent 后取极限，不能声有 angular-uniform概率。任意可测子族上的概率 restriction亦须 measurability和其原质量分母，不自动保 fullD 或 compact。

Finite spacing可以由真实方向抽取，而不是赠原 C physical δ-direction separation。取一个 sufficiently large fixed multiple of δ 的 angular-separated net，每个 direction 选原 C 中一条 line；其 line-space ball r≥δ 中计数≤C_n(r/δ)^5，且总数≈δ^−5。固定 spacing/有限着色支付常数；若应用 §3 的 common cover-level，只在该 positive angular-mass 层中选 representatives，总数仍有该层实际 polylog 质量因子。不能让原任意全族自动变成方向分离，也不能由 tubeδ-neighborhood 的 overlap 推一个未知 inverse 模量。

C 的 offsets 有界，故先做一次依该界的固定 physical homothety，把最近点放在 B(0,1/4)，每条**整线**可取长 1 的内段及 δ-tube 于 B(0,1)。该固定变换不改 Hausdorff 维数或 angular directions；单位管来自实际无限线，不需未知 segment-extension。原 pairwise line disjoint不授 δ-neighborhoods不交，(1)仍须真实处理全部 overlap。

对于已满足 (1.2) 的某个 unweighted finite family，任意 measurable Y_T⊂T，令 E=∪Y_T、λ=Σ|Y_T|/V。单纯 Hölder 由 (1) 实际给

    |E|≥c λ^q δ^(d−1+qε)V
         ≈c λ^(d+β) δ^(n+d−2+qε) #T。             (3)

因此可处理其**平均**密度；若原逐管有下界，则整 label restriction 保该逐管下界。任意删 labels 后平均要重算，shading进一步删选也不自动保原逐管下界。此处不偷升 source 为任意权 maximal 定理。§3 恰以每条 line 的 polylog density 和 common-level mass 来取得 Hausdorff 读出，不能只凭 (3) 写邻域维数就忽略 cover层质量。

## 6. 六维阈值、真实比较和不能放大的参数

令 t=一个实际已证明的 dim_H C lower。Zahl 只许可选择 2(d−1)+β≤t 的 d/β；n6 的几个关键值是

| 原 Hausdorff 参数门槛 | 可给并集下界 | 与本项目责任 |
| --- | --- | --- |
| t≥5，d=3,β=1 | 4 | fullD 的实际直接结论 |
| t≥6，d=4,β=0 | 4 | 仍无 strict 增益 |
| t≥6+β，0<β≤1 | 4+β | 需额外 Hausdorff 参数维数 |
| t>25/4 | 可选 β>1/4 得 >17/4 | 该 strict t 下界未从原 C 付出 |
| t≥7，d=4,β=1 | 5 | 可反 dim S(C)<5，但 t≥7 未付 |

没有把 t=5 代进 d=4 的 threshold6，更没有把 packing 或 topological dimension 当 Hausdorff。source 的一般最优例含许多平行 d-planes 内的线，通常大量相交且 directions非全；这些例只能校准一般定理，不否认在原 compact/disjoint/fullD 上可能存在更强、但尚未找到的几何定理。

有限条件的指数 s 也不能人为选大来制造结论。因为 r/δ≥1，较大的 s 会使球 count upper 更宽松；但缺少 #T≈δ^−s 的 matching entropy。n6 实际 #T≈δ^−5 时，d=3,β=1 的 (3) 仅给 |E|≳λ^4δ^(2+4ε)，近满 density 是维数4；改用 d=4 并不会变成4+β，而会得到含同一 #T 的较弱 physical δ^3 主幂。不能复制同一 axis 的 unit pieces或index来填满 δ^−s：最小 line-space ball计数随之破坏。

已实际读回当前 DIM001：在RED/FSD的明列高级输入、KT6.2及已付任意集合桥下，ordinary R6 的既有条件结论为17/4；四维输入本身在本项目框架给高维baseline4。Zahl在当前原信息下给4，比17/4少1/4，亦未超过先前明确KT基线7−2√2。比较的是同 Hausdorff/ordinary 对象的值，不认证最新最优、优先权或旧高级proof无条件正确，更不重做R29/R38/KT算术主任务。

## 7. 典型 Hausdorff/packing 与维数放大的失败指纹

已 actual 读 KM2203.15731v3 PDF2 的原文：典型 Besicovitch line collection可有 Hausdorff 参数维数 n−1、packing参数维数2n−2。这个 statement 不是本轮新独证；但它明确阻止把 R81 的 generic/typical 词解释成 Hausdorff 参数维数接近 line-space ambient。n6 的两数是5与10，Zahl用前者。

若沿 KM具名的原 residual typical范围与R81低维/不交 residual同时选择，其 canonical quotient q 是 Lipschitz，故参数维数上界5；full direction的 Lipschitz投影又给下界5，恰为5。此一致性核验不是无条件构造完整 C，而是说明已有归约并未免费产出 t>25/4。不能把 packing10转Frostman exponent10，也不能通过countably多族把Hausdorff维数从5抬高（可数并取sup）。

沿同一条 line 移动 raw anchor 并不改变 canonical line，不能把 raw code 的额外纵向参数拿来填 Zahl 的 Ln 维数。§3的 analytic enlargement 可真含更多 lines，但源只承诺不减参数维数；dim S<5 条件下是否强迫这个新 family 达7，本轮没有证明，也不把 desired entropy amplification 另命名为已选机制。原 no-Hölder、无ADlower、Schubert集中和旧CP/PM/PW4量词冻结仍完整保持。

## 8. 结论、真实可用范围与停止建议

Zahl是一项与原compact line metric真正兼容、无smooth/ADlower假设的正面输入；本轮已按原文定理与完整§3应用核它的用途，而非预先强拒。对当前 fullcompact n6原C，它合法给dim_H S(C)≥4；若另有实际 Hausdorff 参数维数超过25/4或达到7，其 stronger输出也真实有效，但原full directions、不交性、compactness或R81典型性均未付这个新增门槛。

因此**该单一输入目前未提供合格的非旧闭包 phase II 主命题**：只再调用它得到4，不超现有四维/KT后果，按R83 spec须停止本 line-union abstract筛查门并交root完整macro；不能为给出主数学而把 t≥7、ADlower或更强δseparated熵写成原假设。本稿未拒未来与新真实结构输入的组合，也未认证“没有任何其它primary工具”。

root完成整合后，本人已再次 actual 全文读 notes/00_map/R0083_direct_line_union_input_gate.md 九节、B《R0083_HKM_Fubini_and_restricted_projection_input_audit》八节及 literature/notes/R0083_direct_line_union_sources.md 六节。root 的 Borel lift/真实 r^5 upper、Zahl finite/集合量词、5→4与25/4/7阈值和named抽样边界均与本人实际原文核算一致，无必须修正项。对B/root的HKM部分，独核其自含 rational-clock Γ1-null 校准、逐line零损与Tonelli平均零损、删后无整段/closure不保维数、s≥5经1+s/2只得7/2及Conj3.11不能当已证输入的逻辑范围，无阻断；本人尚未新全文读HKM §§2–3原primary，故此cross不冒HKM高级声明的第二次来源独证。source6所记root视觉/PDF读域与本人Zahl实际全文及原bytes读域分列，没有把其HKM读取虚记为我的读取。自己的source正算不计自审独立，root/B另有实际cross记录。

若有真正匹配且超旧baseline的输入，应先报告、先补锁spec再施工，不在本phaseI偷偷开新定理。主定理按具名已发表输入，CV等wholeproof未新独证；sampling小尺度/全部常数未在本轮冒独证。未经外部同行评审，无新数学ID、ordinary维数界、major/priority、metadata或未来Git同步认证。只编辑本分配文件，未spawn/Git/meta/download，完整Goal active。
