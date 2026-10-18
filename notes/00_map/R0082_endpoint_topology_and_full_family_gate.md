# R0082：完整紧致多纤维直线族的端点与拓扑选择门

2026-10-18，phase I，Goal active。本稿只筛完整 compact 全方向不交族；不启动未锁的 phase II，不以连续单选子类替代原对象。下列计算没有证明该族存在或不存在，也没有产生 Kakeya 维数界、新数学 ID 或重大性声明。

## 1. 实际恢复、原对象与停止量词

已实际全文读 R0082 working_spec 五节、R0081 next 六节、当前 GOAL、STATE、ROADMAP 及 registry 的全部 78 个 ID/status；当前 registry.latest_round 为 R0081。R0081 root 十二节本轮再次全文读回。其 SHA256 为 fe81c7fbff92ca018518f33cdda250564e9aebfab10e804222638e5022f5c4a9；R0081 next 的 SHA256 为 bc38aaa63388a13d7b9dd55c56f8f0503b2e33c4af60915b8829580c74c7d7d9。前轮实际全文阅读的讲义、KM 具名输入及两份正式审查保留原边界，不作本轮新的官方字节检查。

固定 n≥3，首要 n=6。无向 affine line 的 canonical code 是 (a,P)，其中 P 为 rank-one 正交投影且 Pa=0；对应线为 a+range(P)。C 为这种 line space 的非空紧致子集，方向映射 π:C→RP^(n−1) 满射，任意两条不同线在整个 R^n 中不交。原输入不授每方向唯一、有限纤维、连续 selector、流形、Lipschitz、代数性或任何测度下界。

本门须对这个完整 C 找到超出端点重写的真实可执行障碍。若只得到唯一方向图的矛盾、失去全方向的 residual restriction 或无模量的坐标化，则拒绝 phase II，并由 root 作完整四路径 macro。此处没有原 δ 族或 shading，不能把定性 Baire/有限覆盖费用称作次幂质量或有限正增益。

## 2. 无向方向的 double cover 与真实端点嵌入

令 A=max_C|a|，固定 R>A，并定义

    C̃={(a,v):(a,vvᵀ)∈C，v∈S^(n−1)}，
    ι(a,v)=(a,−v)， r_R(a)=√(R²−|a|²)，
    E_R(a,v)=a+r_R(a)v。

C̃ 紧致，ι 是无固定点的 deck involution，C̃/ι=C。方向满射确给 C̃→S^(n−1) 满射：每个无向方向的任一实际线都有两个 oriented lifts；不需要先选 orientation section。a⊥v 保证 |E_R|=R，且它是沿 v 的正球面交点；另一个交点是 E_R∘ι。

若 E_R(a,v)=E_R(b,w)，该点位于两条实际整线上。原不交性迫两条 canonical lines 相同；同一条线只有两个不同球面交点，r_R>0 又排除正负 orientation 混淆。因此 (a,v)=(b,w)，E_R 单射。紧致空间到 Hausdorff 空间的连续单射给

    E_R:C̃→F_R:=E_R(C̃)⊂S_R^(n−1)

为到闭像的 homeomorphism。这里的结论恰是闭像，不是 F_R 等于球面、有内点或为流形。R>A 的严格性不可删；相切时两个端点会合，orientation 单射失效。

## 3. 配对 involution、chord 关系与无穷远近反极几何

在 F_R 上定义 J_R=E_R∘ι∘E_R^−1 以及 V_R(E_R(a,v))=v。于是 J_R 连续、无固定点、J_R²=id，V_R 连续满射，并且

    J_R x=2a−x， V_R(J_R x)=−V_R(x)，
    V_R(x)=(x−J_R x)/|x−J_R x|，
    a=(x+J_R x)/2， x·J_R x=2|a|²−R²。

配对的两个端点决定原整线，所以 C≅F_R/J_R。除同一 orbit 外的两个 pair 所确定的无限延长线必须不交；只检查球内 chords 不交不足以恢复原假设。尤其任意抽象 free involution 加任意 equivariant 满射不必满足上面的 chord-direction 恒等式，不能当完整几何反例。

当 R≥2A 时有一致估计

    |x/R−V_R(x)|≤A/R+1−√(1−A²/R²)≤2A/R，
    |J_R x/R+x/R|≤2A/R。

因 V_R 满射，每个球面方向距 F_R/R 至多 2A/R；故归一化闭像在 Hausdorff 意义趋近整球面。但随 R 改变的是 F_R，本结论不使任何一个固定 R 的 F_R 变成整球面。不同 R 的 F_R 由同一个 C̃ 连续识别，只有一般一致连续性，没有统一幂模量。这里也没有可对照固定 fundamental class 的满射 degree。

## 4. 维数、degree 和端点逆模量的严格边界

连续满射不能反推 domain 的拓扑维数不小于 target；Cantor 集可连续满射一个区间或球面。虽然 F_R 是球面闭子集，尚不能给它球面流形结构、顶维 fundamental class、invariance-of-domain 的同维 manifold domain 或 nonzero degree。方向图 V_R 还是受到真实 chord 关系约束的特殊满射，但把该额外约束转成全类障碍正是未付处。

原 endpoint inverse 也不能仅由 compactness/disjointness 升为 Hölder。以下 genuine 几何校准适用于 n≥3，但只有部分方向。固定 R，从足够大的 j 开始取

    θ_j=1/j， c_j=exp(−j²)， s_j=√(R²−c_j²)，
    x_j=s_j e1+c_j e3， v_j=cosθ_j e1+sinθ_j e2，
    ℓ_j=x_j+ℝv_j， a_j=x_j−(x_j·v_j)v_j；另 ℓ_∞=ℝe1。

第三坐标恒为各不相同的 c_j 或 0，故所有不同整线确不交。canonical codes (a_j,v_jv_jᵀ)→(0,e1e1ᵀ)，族紧致，且从大 j 开始可使 sup|a_j|<R/2。因 x_j·v_j=s_j cosθ_j>0，恰有 E_R(a_j,v_j)=x_j。可是

    |x_j−Re1|≈exp(−j²)， |v_j−e1|≈1/j。

所以在这一个紧致不交族上 E_R^−1 不满足任何正 Hölder 指数。此例不含全部 RP 方向，因而不反驳“full directions 另能给某种模量”的新命题；它严格排除由 compact/disjoint 两项直接免费取得该模量。Hausdorff 维数、正测度和 finite power gain 也不能靠这个未付模量反向搬运。

## 5. 最小紧致子族：合法 residual 唯一性仍不是全方向 selector

在所有满足 π(C0)=RP^(n−1) 的闭子族 C0⊂C 中，递减链的交仍满方向：每个方向上的非空紧致纤维有有限交性质。故可取 inclusion-minimal 的紧致满方向 Cmin。它仍保全部原不交关系；这是合法闭删选，但并未产生新几何定理。

记 D=RP^(n−1)，f=π|Cmin。给 D 中任意非空 open W 及 ε>0，在 f^−1(W) 内取非空相对 open U，diam U<ε。极小性迫 f(Cmin\U)≠D；该像紧致，所以

    V=D\f(Cmin\U)

是非空 open，且 V⊂W、f^−1(V)⊂U。由闭映射的 upper semicontinuity，G_ε={d:diam f^−1(d)<ε} 是 open；上述论证给它 dense。于是 G=∩_kG_(1/k) 为 dense Gδ，其方向纤维为 singleton，唯一逆在 G 上连续。

这没有取得 G=D。删成 f^−1(G) 可失紧致及全部方向；再取闭包恰回到 Cmin，因为每个非空 open U 都含某个 G 上的唯一纤维。不能以 residual 大替代原全部方向。

一个保真实整线不交的 cut 校准说明缺口不是字面措辞。R4 中令 θ∈[0,π/2]，

    a_θ=(0,0,cosθ,sinθ)， v_θ=(cos2θ,sin2θ,0,0)，
    ℓ_θ=a_θ+ℝv_θ。

末两坐标唯一保证不同 lines 不交，族紧致；方向恰覆盖固定 2-plane 内的 RP1。除一个拼接方向外方向纤维唯一，拼接方向有两个不同的 parallel lines；没有连续 full-RP1 section，否则 S1 连续单射嵌入区间。此族是这个 RP1 满射的极小闭子族。它不是 ambient RP3 满方向，更不是原 full-C 反例；它恰好反 residual 唯一性自动延拓的步骤。

## 6. 连续全方向 section 确实不可能，但不能从原 C 抽取

若额外给连续 section s:D→C，则其 image C0 紧致、每方向恰一条线、仍不交。π|C0 为 homeomorphism；其 incidence space 是 RP^(n−1) 上 tautological real line bundle γ 的 total space。评价映射

    Φ:Tot(γ)→R^n， Φ(d,w)=a(s(d))+w， w∈range(P_d)

连续且单射：不同 d 对应的整线不交，同一条线的参数 w 也唯一。它是 proper，因为 a 有界且 |w|≤|Φ|+A，故 compact physical set 的逆像是 closed bounded bundle subset。Tot(γ) 是无边界 n-manifold；invariance of domain 使 Φ 的像 open，properness 使它 closed。R^n 连通，像只能是全部 R^n，故 Φ 为 homeomorphism。然而 Tot(γ) retract 到 RP^(n−1)，后者在 n≥2 非 contractible，与 R^n 矛盾。

因此任何假想完整 C 都不容连续满方向 section。此 conditional obstruction 是初等标准拓扑用途；把“每个原 C 都能抽连续 section”当下一候选，会立即与 no-family 形成同一目标，而没有给出抽取机制。最小化、方向 closed caps、任意选择后取闭包均未补上这个机制。本稿不将这段 unique/continuous 子类证明登记为新结果或 phase II 主任务。

B 独立给的更直接 selector 校准为上一节 θ∈R/(2πZ) 的整个圆周族：direction RP1 上的映射 θ↦exp(4iθ) degree 4。若有 continuous section，degrees 之积须为 1，矛盾。它同样保真实 compact/disjoint，但只有部分 ambient directions，不能偷偷提升成完整假想 C 的存在证据。

## 7. 闭包、旧指纹与可执行机制筛查

closed direction restriction 保 compact 与不交，但通常只保一个 closed cap 的方向；有限 cap 族只有在跨 pieces 的整线也实际不交时才能拼回原问题。对同一 C 的 closed restriction 不会新增交线，但任意 selector 的非闭图既不保紧致，其闭包又可恢复多纤维。新构造独立 pieces 时不能用 R81 在假低维 residual 输入下成立的 Baire avoidance 循环取得本轮不存在的选择定理。

R81 的 dim≤s<n−1⇒可数 compact full-direction disjoint families 是既有 source 归约；本轮端点模型不反过来排这些族。真 closed 非紧致 odd-dimensional line constructions 的 offsets 可无界，不能由选一个有限球面或 truncation 变成 compact 且仍满方向。不从“closed”误读“compact”，亦不从 endpoint 近 antipodal 推 sphere image 满、局部 direction chart 或 degree。

当前尚未有能从真实 chord relation、满 RP 与 compact 多纤维同时推出 nonzero topological index、全域 selector 或另一矛盾的定量/定性步骤。把这一待证结论仅改称“端点拓扑障碍”仍没有增加信息。partial-direction 反攻只否免费中间蕴含，并不证明 fullcompact 族可能。四路径的完整 Goal 不因本门失败而收缩，亦不回旧 CP/PM、PW4、更多 fixed anchors 或 KT 数值闭包。

## 8. phase I 结论、真实读域与下一责任

本稿独立付清 oriented endpoints、闭像/involution/chord 的精确关系、R→∞ 近反极估计及合法最小紧致子族的 residual singleton 边界；给 genuine partial-direction non-Hölder 和 selector 校准。这些是筛查证书，未形成超出 elementary 坐标/连续单选子类且能作用完整 C 的新可执行机制。

结论：本端点/degree/selector 门未通过 phase II 锁题条件，应按 working_spec 停止并由 root 完整 macro 重比 ordinary 初始化、direct ordinary 多尺度、全部 matrix/mixed/extremal κ 与真构造。不能再把该 unique/smooth toy 续一轮，不能以本稿证明 n−1 下界或宣布任何 n≥5 ordinary gain、Kakeya 反例、major 或 Goal complete。

实际 source 读域为 R0081 root/next 与既有 Keleti 讲义的 compact/closed 和全方向问题陈述；本轮不采用新高级 proof 输入。root 负责的新 Harrison primary screening 不在本稿伪记为自己 actual 全文读，亦不以其 skew/no-parallel 或 manifold-base theorem 调到原多纤维 C。B 的 notes/00_map/R0082_multifiber_selection_and_countergate.md 七节落盘后，已实际全文逐式读并独核其 endpoints、degree-4 真实圆周族、Cantor-height 局部无 selector、极小族残余唯一性、proper bundle 子类矛盾及抽象弱模型边界，未发现必须修正项。Cantor-height 例中任何非退化 connected subarc 的 section 都会经 height 连续映入 totally disconnected Cantor set 而为常值，故不能 right-invert 原方向；仍不含 ambient 全方向。B 的抽象一致极限例不满足整套真实 chord/incidence，正文亦已明确，不能误作原反例。自己的端点计算不计为自身独立审查；由 root/B 实际互读另核。相关内部核算不等于外部同行评审；无官方版本新核、无元数据或 Git 认证。
