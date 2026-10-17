# R0041：实际构造、原质量及有限耦合熵的正式审查

2026-10-17，A。**修后全文在所述范围内通过，可归档。** 主 fixed-power 构造未得；没有 Kakeya 反例或新的高维 Hausdorff 下界。结论为实际可分离构造的体积障碍与有限概率必要条件，未认证新颖性/重大性，未经外部同行评审。

## 1. 实际读取与独立性

全文读取 root `R0041_actual_volume_and_coupling_entropy_boundary.md` 全10节、B `R0041_recursive_power_counterattack.md` 全7节、`research/reviews/R0041_macro.md` 全8节及 `notes/00_map/R0041_next_macro_and_nonseparable_route_gate.md` 全文。原 primary 实读 §2–5 相关完整 construction/continuous directions/Prop5.4，详见 A assigned source 稿的 PDF/文本范围。

A 是自己 source 稿作者，不把对自身论证的重复阅读计为另一份独立审查；本报告对 root 的扩展熵估计、完整整合/宏观，以及 B 的独立反攻作逐式核验。B 的共同 clock/方向限制不是由一般 all-directions 假设免费得到的，root §8 已另外支付。

## 2. 原 source 与参数尝试

原 Prop4.1/式(5)确实将 protruding branches 加到 core 之外。t_i 固定时 P_n 可指数小，但它不是整个 union 的体积。root §2 最大 t_i=1/2 的精确例给 w_k=−kr，h∈[1/4,1/2] 的 intervals 相接，|A(h)|≥1/4，故 raw actual volume≥4^{-d}。完整单位 clock、连续 base directions 和 bounded centers 均仍保留；这是合法改造的真实失败。

可变 c_i 的 weighted Holder 计算正确：令 Δ_{n+1}=P_n、ΣΔ=1，权 a_i=(1−c_i)^{-d}，得证书≥[1+Σ(1−c_i)^{d/(d−1)}]^{−m}。每真分支至少2，r_nat=(∏|I_i|)^{-1/m}，所以 n≤C_m log(1/r_nat)。该结论只限原证书；root/B 都没有从 upper 右侧的 lower 倒推所有实际 nonproduct unions 的 lower。

A 的任意 t_i cube coefficient q_j=1+P_{n-j}−2P_{n-j+1} 与原优化显式式子一致；最大压缩及标准 G_r 的 plus placement 已逐项重算。嵌入 N_{2r}T_i⊂CT_i−(C−1)q_i 后应取 v_i=Cw_i+(C−1)q_i，root §9 用的是正确符号。

## 3. B 的 actual product lower

B 的有限 slope 网取 M≈1/r，strip halfwidth ε≈r，任意 intercepts 下 pair overlap 的时间积分≤Cε²/|Δq|。diag O(1)，按 slope index 差求 harmonic sum，得到平面 L² integral≤C log(2/r)。每 t 的 strip 总质量固定，因此 ∫_J1/L_i(t)≤C log。

对全部 coordinates 的坏时刻以 Markov+有限并集控制，保留同一个至少半长的 J-good set。仅在这个共同 set 上乘 slice lengths，得到实际 N_r(K) lower≈log^{-m}。有限 Cartesian combinations 的真实线段点就在 K 中，产品小盒距离它们≤r；不需要 u_i 可测、不同坐标概率独立或先将各自好时刻相乘。

该证明 uniform 于深度与目标 r，故排 n(r)重新标定；但假设是每个完整 Cartesian direction 组合都具有 separable intercept、同一 clock。任意 joint direction placement、原5.4后的不同 frame/clock 均不能免费套它。不同 n_i 的 finite product pyramids，可对 e_i/(n_i+1) 同时 Markov，得 raw volume≥c∏(n_i+1)^{-1}，也与 root §4 相符。

## 4. Root (EG) 的 L² 与原有限边际

root §5 的实际输入为有限 joint law(A,B)，各 Ai 在固定区间的 r-grid 上，每 atom≤K0/M，M≈r^{-1}；K 包含每个 positive-support (a,b) 的共同 J 全段。它没有将一般 δ-shading 的均值或分离方向自动变为这一 law。

卷积 uniform[-r,r] 后，same-slope pair 的时间 kernel≤C_ℓ/r，概率 Σ_a p_a²≤K0/M，贡献 O(K0)。对异斜率，积分 kernel≤C/|a−a'|；另一 atom cap K0/M 和 r-grid harmonic sum给 O(K0 log M)。条件于 a 的 B 任意相关也只改变平移，不能增大这一 uniform pair bound。因此 (5)成立，不需要 B|A 独立。

对 Σ_i e_i(t) 作 Markov得到同一长≥ℓ/2 的 G，各边际满足 e_i(t)≤C_{m,ℓ}K0 log(2/r)。这里 K0 不是隐藏的 uniform probability 假设。

对实际 unsmoothed X_i=floor((B_i+tAi)/r)，第k-bin质量卷积后落在长度3r的 enlarged bin。局部 Cauchy 给 p_k²≤3r∫_{I_k^+}μ²，sum 时 enlarged bins仅 O(1) overlap，故 Σp_k²≤Cr e_i。Shannon≥collision entropy，得 root (7)。没有把 smoothing 后的 law 偷换成原 source 的条件 law。

## 5. 条件 entropy、TC 与返回真正体积

root §7 的不等式方向正确：

    ΣI(Ai;Xi)≤ΣI(Ai;X)≤TC(A)+I(A;X)≤TC(A)+H(X)。

中间一步用 H(A|X)≤ΣH(Ai|X)，所以无需独立 Ai。给定精确 Ai 与 floor(B_i/r)，X_i 只有一个确定整数平移加一个 carry bit，因此 H(X_i|Ai)≤H(floor(B_i/r)|Ai)+log2。两项分别收费 S_r 与 TC(A)，没有把所有 marginal high entropy 当 joint high entropy。

每个 positive X-bin 确有 support point 属于 K_t。相应整个 r-cube 距这个点≤√m r；distinct cubes互不重叠，因而 |(N_{C_mr}K)_t|≥r^m #supp X≥r^m exp H(X)。这一步返回的是**实际邻域 Lebesgue volume**，不是 entropy 形式量。对共同 G 积分得到 EG：

    |N_{C_mr}K|≥c exp(−S_r−TC(A))[K0 log(2/r)]^{-m}。

该式同时保留 S、TC、atom cap 和 clock长度常数。大 S 情形没有矛盾；也未推出一般非均匀 Hausdorff covers 的下界。

## 6. 任意 bounded compact K 的共同 clock crop

固定小 slope box及其中有限 r-grid，每方向只选择一根实际单位段。unit方向的 clock 分量有固定正下界，故 clock intervals 长度≥ℓ0；bounded K给共同有界 time 范围。预先有限组长度ℓ0/4 的 lattice clock intervals可让每原段包含至少一个；pigeonhole保 p≥p0(K,m) 的方向。

此 S 不必是 Cartesian。uniform on S 时，每 Ai atom≤1/(pM)，而

    log(1/p)=TC(A)+ΣD(P_Ai||UniformGrid)，

所以 K0=1/p、exp(−TC)≥p，得 p^{m+1} 的真实费用，root (9)正确。finite witnesses 不要求 measurable selector；clock crop确在每根原完整段内，没有把 partial marks 填成长直线。

稀疏半径列也未漏 fixed-radius 责任：若仅已知 |N_{r_j}K|≤Cr_j^κ，root明确在 r=r_j/C_m 的 workmesh 使用 (9)，而不是擅自把 upper 扩成 N_{C_mr_j}K。于是 S_r≥κlog(1/r)−m loglog(2/r)−O(1) 的符号、p因子及尺度量词均正确。换 clock 原点 given Ai 后最多一个 carry bit，bin entropy只差 O(1)。

## 7. Continuous directions 与同一个 compact K

原5.3的 full pyramid 保每个 base point→apex 段，长度≥1；其固定球面开 patch 不随 r 缩小，有限 rotations覆盖所有方向并只乘固定体积常数。A 给 q_i 的 uniform inball，故 canonical G_r 的 N_{2r} upper 有明确合法 embedding，同时仍 separable；没有把有限 axis net 当完整方向。

原5.5的 anisotropic map 只在 transverse coordinates缩 ε；unit length 来自两 clock faces相距1，而非假定 minsingular不缩短任意段。恢复 full sphere要 O(ε^{-m}) 个 caps，抵消 det ε^m。原5.4的 stage估计因此是最近 f(δ/ε)，不是过去体积乘新的 f。

δ_n=2^{-2^n}、ε_n=(δ_{n-1}−δ_n)/√m 的有限早期非法步可跳过；后续 nested N_{δ_n}F_n 保 same compact E。对固定方向，其 nonempty starting-point compact sets随层递减，保完整 unit segment；没有可测选择漏洞。intermediate radii以 monotonic f 得 f(C_d r^{1/4})，真 power seed会保正幂 c/4，log seed仍是log。product lower不自动给任意 final patched E 的lower，root §9已明示。

## 8. Macro/下一入口及最终状态

一主轮没有实现 power 构造，已用 actual lower排除明确类的可变参数，提前macro符合退出规则。冻结 t_i/coordinate-depth/product-patching循环；未排跨坐标 coupling不能以名称自动继续下一轮。

R42入口要求先作有界primary证据及等价/闭包排重，再选唯一实际新 main；不自动把 EG 所需低 S 设为公理，也不由两个 marginals高熵假推 shared-time joint。它明确比较既有6D finite链的文献地位、未解决source mixed branches、真 nonseparable构造，未将三者同时开轮。没有与旧冻结项冲突或把未证目标标成已有实现。

本报告无 outstanding 必修问题。A source稿198行与本review为唯二编辑文件；UTF8/control检查另记录。所有已审结论保持范围/引用层次，未经外部同行评审；Goal active，主猜想、反例及major均未达成。现在停止编辑，无Git。
