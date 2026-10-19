# R0103：一手投影输入与原质量多项式 profile 独立审查

2026-10-19，A 正式终审。以下“通过”仅指实际全文读取的本轮有限原配置应用、集中 profile、限定反攻及停止范围；具名高级定理未从零独证，未经外部同行评审。

## 1. 实际全文对象和审查分工

本次 fresh 实际全文读 root 主稿 `notes/40_multiscale/sticky_matrix/R0103_original_incidence_Schubert_concentration_and_polynomial_layers.md` **10 节**、B 终稿 `notes/00_map/R0103_rich_direction_nonconcentration_counteraudit.md` **10 节**、A 分配稿 `notes/00_map/R0103_complete_goal_and_global_projection_reselection.md` **10 节**，以及 reselection、working 两份规格各 **5 节**。B 第2节最终 q<1/4 和第6节 product-sine 分窗补充已读回。本审查逐步独核 root/B 的链；A 本人分配稿的自证不计为它自己的独立审查。

原输入沿已实际全文审的 R102 root12 §§1–7，而非重新假定其全局 P2Fst 或 rich fibres；本轮复核了该主稿全文及 R78 root14 的真实质量范围。He 一手实际读域为官方 1710.00795 current v2 history、固定 v2 HTML/本地提取的 §1.1、§1.2、§1.4 的所用 statements，§2.2 wedge/对偶公式及 §3.1 Prop25 完整段。未据此声全文审过其 §4 高级证明。官方版本为 2018-05-09，PDF 提取正文 Date May10，HTML 再生成 Date August24,2026；33页 arXiv 稿与47页2020 JFG正式版不冒逐字认证。没有作本人未执行的 PDF 视觉或新字节核验。

## 2. He Th1、同一个 P 与任意原权概率的适用性

Th1 的真实输出是对 good V 的 **所有**大子集 A′ 成立，不只是存在一个好 A′。取 n4/m2/α2/κ=q 后给 δ^-1-ε_H 增长；R102 每个 rich u 的 P_u 虽可不同，仍都在同一个 P 中、具有 ≥L^-C 比例且投影 cover≤L^Cδ^-1，因而这个量词足够。P 的二维 point upper 蕴含 q<1/4 的 weaker upper；其有界共同 scalar 缩放到单位球、固定维 grid/ball cover 与 cardinality 的比较只付固定倍。未作非正交 Grassmann 坐标变换来假定 cap 不变。

减小 ε_H 到 e 的单调使用正确：输入 upper 更严、P 的 size lower 更强，待测 P′ 门槛更大，原结论强于 δ^-1-e。先定 q 和 e，再取全部源损失指数 ℓ≪e，故固定常数、P_u 比例和小像 upper 均满足此门。源 ρ≥δ 的完整范围保留，没有 sub-δ 非集中要求。

对任意剩余原时钟支持 R，用 I_u 归一后 pushforward 到 **normal** W_u=(imG_u)⊥。它可原子化、不同 u 可重复 W_u。若该概率满足所有全局 Schubert cap upper，He 给一个正权 good 方向，而同一方向至少有一个实际坏 P_u，矛盾。这里每个方向都坏，故不需把源坏方向小比例回传 uniform times，也不需无偿参数多重数 upper。结论是 cap 必失败，不是从完整 Def17 证明 cap 成立。

## 3. Half 剥取、原 I 分母及平均到逐管返回

root §4/B §5 的剥取正确。每个非空剩余 R 都可重复 §2，选 ρ_j∈[δ,δ^(e/q)) 及 cap 内剩余 clocks U_j；条件 mass>δ^-eρ_j^q。仅在剩余原权至少1/2时选下一簇，所以每簇在初始 μ_U=I_u/I_U 下有

    μ_U(U_j)>(1/2)δ^-eρ_j^q≥(1/2)δ^(q−e).

各簇是 clock 标签不交，而非 cap 的几何不交。至多 ceil(2δ^-(q−e))≤Cδ^-q 步覆盖 ≥I_U/2；最后一步仍满足同一 lower。没有漏掉 log，也没有把原 I_U 换为 distinct directions 计数。原全部分母返回只保 L^-C N m，不是固定比例的无损原全部访问。

root §8 再以 J_tot/(2N) 对原管 heavy：低管总量≤J_tot/2，留下 ≥J_tot/(2m) 条原管，每条 ≥J_tot/(2N) 个真实旧 marks，故取得 L^-C N 管和 L^-C m 逐管访问。B 用 J/(4N) 的等价保守阈值亦正确。此逐管 lower 只对所有 U_j 的并成立；单簇仍只有平均 lower。whole-index restriction 继承原 absolute CW upper，重新归一付 N/N′；filled-X、point-Φ/native lower 和完整新 Def17 配置没有免费继承。另对原平均 shading 做初始 heavy 也必须付 λ 质量及 normalized CW 费用，稿件未将平均等同逐管。

## 4. Normal 对偶、quartic 非零性和归一化费用

对正交 B∈R^(4×2)，P_B(v,F)=det(G(v,F)^T B) 的总 degree≤4、v-degree≤2、F-degree≤2。正交化 G 给

    |P_B(u,F_u)|=sqrt(det(G_u^TG_u))·d_angle(G_u⊥,W).

det-angle 是两个 principal sines 的乘积，不是 Grassmann metric 距离。bounded G 支付 cap 上的 Cρ upper，未除小 singular value。B 的 chart 展开式及其消分母式(2)符号另独算一致；不能只测特殊 affine rank-one functional 来代替全部 He Schubert cycles。

formal 中点 v0=(t+s)/2 代入后，S(a,b)=(-A^-1(a+b),b) 将 G 送到 (h/2)(I;F−F_t)。||S||≤Cσ^-1、||S^-1||≤C，故 S^-T B 的两列 wedge≥cσ²。六个 minors 配对独立的 1、四个 F−F_t entries、det(F−F_t)；bounded translation、formal v0 评价只付固定系数范数费用。因此 ||coef P_B||≥ch²σ²≥cσ⁴，upper C 也统一成立。这个检验不要求 v0 在原 Z，不延拓 rough F，也没有在其实际曲线上插值。

归一 Q_B 后厚度 a_j=Cσ^-4ρ_j。先取 4bq≪e 再取 δ 小，可得 μ_U(U_j)≥δ^(−e/2)a_j^q 及 δ≤a_j≤δ^(e/(2q))。稿件正确保留了归一损失，未声仍有同一 δ^-e 因子。所获只是多项式**值**的 sublevel；没有梯度或稳定输入时，不等于 Euclidean 距离 a_j 的零集管状邻域。

## 5. 平凡 profile 测试、弱反攻及旧闭包边界

root §7/B §6 保留了每簇的尺度—质量 lower，而不只报“少量非零 quartic 层”。由原 I_u≤|H|、I_U≥L^-C|H|m、δ-separated Z 及 m≥K^-Cδ^-1，原访问概率满足 interval upper L^C(|J|+δ)。长度 a 的普通分窗无法支付 δ^(−e/2)a^q；取中心 normal 的 Lip product-sine 通用二阶构造给厚度约 l²、所选窗质量至多 L^C sqrt(a)，working q<1/4 同样排除它。稿件没有由一个 upper 反推真实 cap 最多持续 sqrt(a) 长；曲线可以沿 cycle 走，故这不是所有 Lip 集中都不可能的证明。

root §7 最后追加的 degree6 plane-law 校准已实际读回：六个 Plücker functions 的线性独立给所有正交 B 的统一 coefficient lower，七个相隔 c·l 的小值点经 Lagrange 给 sublevel 长度 Cρ^(1/6)；degree≤6 保固定 interval 数，uniform δ-net 仅加 Cδ。它在 q<1/6 时严格否自动 profile，但没有同一个全坏 P_u 输入，不能作 source 反例。该校准由 A 提出、B 已独核；本人不把自己原校准的再计算列作独审，审的是 root 新增的插值说明和范围。

上三角 weak 模型的检验通过：G 两个 blocks 上三角，取 W=span(e2,e4)，B^TG 的第一列为零，实际 profile 落一张 Schubert cycle。所用 R79 对象缺完整全 T AD4/CW、filled-X、point-Φ 与 selected-ξ 等输入，故它只否自动 cap，不是完整 source/Kakeya 反例。formal P_B 非零与 P_B(u,F_u) 可恒零没有矛盾。对角系数例也不授所有差矩阵共同 image/kernel。

R78 的单 δ² 原管块、共同 X 与矩阵 sum-product cone 不含本轮保 L^-C 原全 I 的多块 profile；反向由此 profile 恢复那些输入亦未证。R76 ambient6 固定零项、R97 scalar local Segre 与当前 global Gr(4,2) 对象不同。稿件没有因此解冻旧 CP/PM/PW 全称正幂，也未将 Q_j 当 F 本身是 bounded-degree 函数去重开 R96。

## 6. 最终判定和仍未支付的完整出口

**限定全文通过；无未解决强制项。** 实际通过的是：在既有完整源的 det-large 分支、R102 原全局码链及具名 He Th1 下，任意支持概率 cap 失败，进而得到带每簇异常质量的有限 clock 集中、多项式值薄层及其并集上的原管逐管 marks 返回。root10/B10 的证明、两规格和 A10 的结论范围相容；A 自证未计本人独审。宏观/next 文件若随后更新，须另实际读取后才增记其 scope，不预认证。

没有证明所有原 source 都有该 det-large 分支，没有消费此集中 profile 得到完整 rough κ1 排除、ordinary 初始化或 Hausdorff 新界，也没有构造真实全方向 strict 反例。单簇 source 重建及其 allowed 尺度、δ^-q 个簇的费用与未知 e(q) 强弱、native 几何返回均仍有实质责任。后继不能以 q/e/ρ 优化、固定公共 kernel/有理 F 公设或少簇 cover 表象代替它们。完整 Goal active；无 newID/major/novelty 或完整 branchsaving 声明。He 高级 wholeproof 仍具名，内部独立审查不是外部同行评审；不预认证未来 metadata、Git 或同步。
