# R0113：三角截距原质量证明的独立逐式审查

2026-10-26，algebraic_gate。审查对象为 `research/rounds/R0113_working_spec.md` 和 root 的 `notes/50_counterexamples/R0113_triangular_Borel_original_shading_proof.md`。本分工未参与该机制的提出或原证明，只编辑本审查文件，不 Git。实际全文读两稿，并从 scalar energy、原 marks 筛选、逆序消元和 Frostman 返回分别反攻。

结论：有限体积式 (F) 和连续 Borel 式 (H) 的核心证明正确，量词覆盖的是完整 product direction grid/cube 上的**三角 prefix 截距类**，没有推出普通高维 Kakeya。发现 bush 校准的一处时间区间笔误及需显写的固定小尺度范围，已先消息 root；见 §7。没有新的 major/ordinary 维数结果或外部同行评审认证。

## 1. 精确对象与可攻击入口

固定 m≥1、0<s<1、非退化 bounded J、R>0、c0≤Lδ≤C0。原表 a_i 只依 k_≤i；每个 label 的 Y_k 是原 indexed cylinder 内任意 Lebesgue 可测子集，允许 empty，允许依全部标签/输出/time，绝无 Cartesian marks 假设。λ=I/[N(2Rδ)^m]∈(0,|J|]，不是预先逐管 dense 的下界。

本审查优先尝试以下反攻：diagonal 噪声能量是否漏 δ^-s；不同 prefix 是否偷偷各选时间；marks 能否专门集中于 bad；good 密度控制是否遗漏 interval 质量；逆序求和是否保留未来依赖；Borel image 是否只对 closure 有测度；只给某些尺度球界能否冒 full Hausdorff。逐项检查结果如下。

## 2. 标量能量：常数和有限 diagonal 均付清

长度 ℓ=|J|，B≠0 时，对 t 作 y=A+tB 代换。长度 |B|ℓ 的区间上 |y|^-s 的最大积分在以0居中的区间，故

    ∫_J|A+tB|^-s dt
      ≤2^s ℓ^(1−s)|B|^-s/(1−s).

源式 (1) 常数和 |B| 幂正确，对 A 任大、B 任小都成立；s<1 必不可少。这里不要求 a_i 有界。

令 d=2Rδ。uniform probability on an interval of length d 的 self-energy 独立计算为

    d^-2 ∫_0^d∫_0^d |z−w|^-s dzdw
      =2d^-s/[(1−s)(2−s)].

所以 L 个 diagonal 乘 L^-2、再积 J 后是 C|J| L^-1δ^-s≤Cδ^(1−s)，依 Lδ≥c0 统一有界。L=1 也由 δ≥c0 保界，无漏掉原子自身：这里每个方向有真实 interval noise，非点原子。

off-diagonal 时固定两噪声，B=(k−l)/L≠0；上述 t 积分不依差截距及噪声。因此总额

    C L^(s−2) Σ_(d=1)^(L−1)2(L−d)d^-s≤C_s

正确，L 个 prefix 也不增加此常数：每个 prefix 各自有同一 J 上同一统一上界，再按 prefix probability 平均。并未为不同 prefix 选择不同 good time。非负 kernel 可直接 Tonelli，之后有限 upper 自行证明能量有限，不循环假设。

## 3. 任意原 Y 的 bad 预算与 good 密度

源先验为 uniform k、Lebesgue t、m 个独立 uniform intervals。对每个实际 Y_k 积噪声恰给 |Y_k|/(2Rδ)^m，再乘 N^-1 后总质量 precisely λ。有限个 Lebesgue 可测 Y_k 可取 Borel 代表并交回 cylinder，只改零集，I/|E| 不变。

固定 i 和 prefix 后，当前 k_i,z_i 的输出分布 exactly μ_(prefix,t)。故先验 bad 质量为

    P(U_s μ_(prefix,t)(x_i)>T)
      ≤T^-1 E[U_s μ_(prefix,t)(x_i)]≤C_s/T.

过去噪声和未来 labels/noise 积分成1是合法的：a_i/potential 不依未来，且此处先对全先验作 upper，未条件于相关 marks。所有 bad 的 union 质量≤mC_s/T，取 T=2mC_s/λ 后，即使**全部原 Y 专门压在最坏位置**，Y∩all-good 仍保至少 λ/2。没有先删管后重设 λ，没有要求每根管各保一半。

good 密度式也核过。若 M 个 interval 包含 x，则它们的总 μ 质量为 M/L，且各点距 x≤2Rδ。因此

    U_s μ(x)≥(M/L)(2Rδ)^-s
             =(2Rδ)^(1−s)ρ(x).

所以 good 上 ρ≤T(2Rδ)^(s−1)，源式 (5) 没有漏乘 interval 长度或概率 L^-1。endpoint 的密度代表仅影响零集。

## 4. 逆序求和：未来依赖真的被消掉

marked-good 推送密度 q 的源公式成立，因为每个固定 k,t 下 z↦x 是平移，Jacobian=1。反攻关键是 Y_k 可依所有变量；原证先把它用 cylinder 的 product interval indicators 上界，然后只保结构化 good 因子。因此随后不再需要 Y_k 分解。

按 k_m 先求和，i<m 的 interval/good 均不含 k_m，第 m 个 good 自身只含 k_<m、t、x_m，确不含当前 k_m。归一化最后一层为

    1_good_m · (1/L)Σ_(k_m)uδ(x_m−a_m(k_≤m)−tv_(k_m))
      =1_good_m ρ_(prefix,t)(x_m)
      ≤T(2Rδ)^(s−1).

这个上界已不依 prefix，于是整层删掉，才可处理 k_(m−1)。逐层反向直到 k1，得到 q≤[T(2Rδ)^(s−1)]^m，正确；若按正序，或 a1 依未来变量，这个步骤确会失效，源稿没有混用。

q 的真实 support 仍在原 E，且总质量≥λ/2，所以

    |E|≥(λ/2)T^-m(2Rδ)^(m(1−s))
        =c λ^(m+1)δ^(m(1−s)).

这直接是 Lebesgue |E|，没有先扩张 E 或只数 occupied cells。对任意 ε>0，先固定 s<1 使 m(1−s)≤ε 后，δ≤1 给 δ^(m(1−s))≥δ^ε；常数可依 ε，不能据 s↑1 宣 endpoint density 或 positive Lebesgue volume。有限主式 (F) 通过。

## 5. Round tubes、共同 J 与 normalization

斜率 v∈[0,1]^m 的 unit direction 是 (v,1)/√(1+|v|²)，chart 有统一双 Lipschitz 界；h≈δ 给固定倍方向分离和 m-KT upper，源稿只称“约δ”分离，未冒字面 unit separation 常数。

对 round δ tube 的一点，先取最近轴点，其 clock 差≤δ，各横坐标差≤δ；用 |v_i|≤1 改到该点自身 t，横向误差≤2δ。因此原 round tube 落在固定 R 的 rectangle-cylinder，clock 只需把原共同 bounded J 固定增大以容纳 endcaps。单位轴的原 intercept/prefix 结构不变，原 marks 未被填满或移动。每根轴的 clock 长可不同，只需都落在同一个固定 J；证明本来允许每管任意 time shading。

λ 的定义除以横截体积但未除 |J|，故 λ≤|J| 而非强称≤1。固定 J/R/envelope 常数全部进入 c。单位段只能从原有线段取，后来的 envelope 延长不新增 marks，源稿保持了这点。

## 6. 连续 Borel 全 r Frostman 与 analytic image

连续版固定 prefix 后，w≠w' 的 affine-time 斜率差 B=w−w'，由同一 scalar inequality 和 ∫∫|w−w'|^-s=2/[(1−s)(2−s)] 得统一 ∫_J I_s μ_t≤C_s。w=w' 的无穷 kernel 位于 Lebesgue 零 diagonal；Tonelli 下不影响有限 upper。任意 Borel f_i 的振荡/幅度不进入该界。

共同函数 (prefix,t,x)↦U_s μ_(prefix,t)(x) 是非负 extended Borel kernel 的参数积分，故 Borel；good source set 为 Borel，X 也是 Borel。于是 ν_s=X_*(Leb|_(Z∩allgood)) 是合法有限 Borel measure，总质量≥λ/2，不必有物理 Lebesgue density。

对任意长≤r 的 Q，如果 μ 在 Q 的 good 输出有正质量，可只为**证明这个数值不等式**取一个 good z0∈Q：∀w∈Q 有 |z0−w|≤r，故 μ(Q)≤r^s U_s μ(z0)≤Tr^s。无需给 z0 作可测选择；当 good 质量为0时更平凡。

对物理 box Q1×...×Qm×Qt，先丢原 Z，再逆序积分 v_m...v1，每一层只用当前 prefix 的上述 upper，最终 t 长≤r，严格得到 ν_s(box)≤T^m r^(ms+1)。good_(i<m) 不依 v_m，未来依赖没有留下。包 ball 的 box 边长2r 只改维数固定常数，所以该 bound 对**所有中心、所有 r>0**成立，非 dyadic/单尺度陈述。

X(Z) 是 Borel image，故 analytic、对 ν_s 完备化 universally measurable。更直接地，对 X(Z) 的任意 countable ball cover，其 union 的 X-preimage 包含全部 Z∩allgood，故 cover 总 ν_s 质量≥λ/2；不必以 closure 代原 image。由球界得 H∞^(ms+1)(X(Z))≥cλ/T^m>0，再逐个固定 s↑1，dim_H X(Z)=m+1。不同 s 可用不同测度，不要求一个 endpoint Frostman measure。连续主式 (H) 通过。

## 7. Restriction、bush 反攻与小修正

zero-shading 扩回完整原 L^m 网格是正确闭包：保管比例 q、保原 I 比例 p 后，仍用原 N 调 (F)，density 是 pλ；若用 N'=qN 归一才是 λ'=(p/q)λ。任意不成 product 的子族不能假成新的 saturated product 网并保原常数。原逐管 lower 可给平均 lower，但 good 筛选只保总 I；例如后续欲再 heavy 到每管≥(λ/4)(2Rδ)^m，可保至少 I/4、管数至少 λN/(4|J|)，一般不是固定比例全部原管。源稿未免费声逐管闭包。

fractional marks 0≤w≤1 只需把源 indicator 改 w，bad budget 和推送密度 upper 都仍真。未授权非均匀方向分布/无界权的无损扩张；原稿限制准确。

bush 可用真实单位轴 ℓ_v={σ(v,1)/√(1+|v|²):0≤σ≤1}，取共同 clock marks t∈[0,r]，δ≪r≤r0(m,R,c0,C0)。各管密度≈r。横截 upper 为 C(t+δ)^m，积分给 |E|≤Cr^(m+1)。取 t∈[r/2,r]，若 r0 固定足小，则方向网的坐标间隔 th≤2Rδ（真实 round tube 可换固定可比横截常数），横截覆盖边长 ct 的盒，给 lower cr^(m+1)。所以 |E|≈r^(m+1)、λ≈r，检验主式对稀疏 clock 的真实收费。

首次稿 §7 写成 t∈[Cr,r]，按通常 C 为大常数时区间为空，应改 `[r/2,r]` 或 `[cr,r]`；“覆盖整盒”的措辞亦宜显写 r≤r0 固定小范围，使 th≤横截宽。已先消息 root。这是校准笔误/范围的小修，(F)/(H) 的证明不依该段。该 bush 也不在所有 δ/λ 组合中证明一个绝对最佳指数，源稿没有作此过强声明。

## 8. 完成范围与最终意见

该证明不使用原 full family 的四维种子/KT 数表，也不把两个边际直接相乘。核心是 scalar 能量对每个 prefix 统一、在原任意 marks 上一次总量筛选、然后合法逆序积分。它允许真正 prefix 耦合和 Borel 粗糙性，超出纯 Cartesian 例；一旦有未来/循环依赖，证明不给结论。

三角性没有从普通方向到截距的 full Kakeya family 提取；声称任意族都可低损转成此类需一个新结构定理，本轮未给。初等 scalar projection/triangular iteration 的文献新颖性亦未由本审查认证。故此处仅是严格 proper 类有限体积与 Hausdorff 结果，不是 ordinary n≥5 改善、完整原 source gain、Kakeya 反例或重大中间结果；未经外部同行评审。

修正 §7 的小校准后，working spec 所锁 (F)/(H) 可作内部独立通过记录。未见主证明中其它强制数学修正；本审查不预认证未来公开状态、Git、同步或长期 Goal 完成。

## 9. 实际读回修正与新增的精确三角化反攻

随后实际读回 root 主稿当前 §7：bush 已改为 cylinder marks `C_k∩{0≤t≤r}`、`t∈[r/2,r]`，并明确 `r0<min(1/4,Rc0)`，由 h=1/L≤δ/c0 给 th≤Rδ，横截覆盖有据；λ=r 是这个 cylinder 版本的精确归一。另单列若要求 marks 在 round 单位管，取固定小 R 并令 r0 小于共同 unit-axis clock 下界。§7 的笔误及固定范围问题均已修，不留未决强制项。

同次读回的新反攻 `a(v)=Av, A=diag(J0,J0), J0=[[0,−1],[1,0]]` 也独立核验。任意固定实可逆空间 S 后 B=SAS^-1 只有复特征值 ±i；若 B 第一行仅 B11 可能非零，e1^T B=B11e1^T 就产生实左特征向量，矛盾。所以至少一项 B1j≠0、j≥2。若在正 Lebesgue 质量可测 D 上有 `(Bv')_1=g(v1')`，则每个固定 v1' 的 fibre 在 R3 中受一个非零线性 functional 的 level 超平面约束，故 fibre Lebesgue 测度为0；Fubini 给 |D|=0，与假设冲突。这真实排掉了所写的“固定空间线性坐标变换+正角质量删选”精确三角化规则。

原构造可取 bounded open direction cube 及共同短 clock interval，保证各线段可装入真实单位轴。每个固定 clock 的 map `v↦(A+tI)v` 可逆，因为 det(A+tI)=(1+t²)^2>0；联合输出因此含一个开集，确为 full-dimensional union。该例既不低维，也没有冒成 Kakeya 反例。root 只否精确三角化，明确不否有限 δ 近似、其它时间/射影/非线性变换，这个范围限定正确。

最终判定：本审查覆盖的 (F)/(H)、原 marks 质量证明、bush 修正及新增精确提取规则反攻均通过内部独立逐式核验；仍限 proper 三角类及具体拒桥，不给普通 n≥5 新界、major、新颖性或外部 peer 认证。
