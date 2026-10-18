# R0080：pivot 几何、真实 lift 和 retained shading 回拉证书

2026-10-18，A。按本轮正式 phaseII 施工；这是 KT 既有递推核心的依赖核验，不是新维数定理、新 ID 或原 KT 错误声明。以下完整给出 normalized critical inputs 下的 soft-loss certificate；critical preprocessing 另列具名，不冒整篇 Theorem6.2 已重新独证。未经外部同行评审。

## 1. 实际读域、原文字面与证明对象

实际全文读本轮最终 spec5/macro6、KT math/0102135v1 §6 的原 text，并实际查看 parent 已渲染的 PDF22/23 图像。原式(45)–(48)、Lemmas6.4–6.7是本稿对象。原 PDF22 的 lift 过 (x,0)、(x+z−i,1)，其空间方向平行 T2；原文随后把 mark 第一坐标写作 y1，与这条实际 lift 不符。下文不用指标名称猜测，而从真实二维坐标导出应使用**第二原端点 y2**。PDF23 对 L² 两式的文字 upper/lower 与不等号方向也以实际推导为准。

更实质的责任是：lift shading 在 Lemma6.7 后已删去高重数 marks，不能仍把所有旧 collinear pairs 算入新 shading。我们定义真实 retained relation，再由其总质量取 CS；不要求每一个 pivot 删后仍保 N 个 pairs。原 Lemma6.6 的 displayed d−1 不由 E 的 d 维 ball upper 推出；正确 d-collection 需要的正是指数 d，见§8。

## 2. normalized finite 输入及 soft-loss 约定

固定 ambient M、空间界 R、实参数 n,d,d′，0<d<n。设 δ=N^-1，L≥2且 log N≤L，最终 L=N^ε、ε可在所有固定损失之后任意小选。C 是仅依固定 M/R/参数的有限常数，可逐式扩大；L^±C 不表示固定正比例。原点集 E 是 bounded box 内 δ-lattice cells 的代表，|E|≤L N^d，且对全部 δ≤r≤O(1)，

    # (E∩B(a,r)) ≤ L (Nr)^d。                         (1)

原 tube labels 来自一个物理方向 cδ-separated 的有限族，各原 shading 是自己 tube 的 δ-cells，≤C_R N 个。A 为实际 ordered angles α=(x,T1,T2)，x 是两原 shadings 的共同格点，angle(T1,T2)≥c0>0，且 |A|≥L^-1 N^(2n−d)。对实际使用的两条管，各 shading cardinal≥N/L；这些是经源 bilinear/critical normalization 后的**输入**，不是从只给平均密度就免费推出。

近 incidence 用 Cδ 容差。把两原轴在距 x 为 O(δ) 处平移到过 x，原 marks 仍在 O(δ) 邻域；所有几何计算先对这些代表轴做，最后由§7支付格误差。方向 labels 不因此变成新自由方向；相同原两方向只容 O(1) 个 transverse intersection cells x。若角下界仅 L^-C，下列证明增加 L^C 也成立，但本稿不重证把原小角 θ 归一到此输入的 bilinear step。

## 3. 从近满 shading 真取 N³/L^C 个非退化 triples

对固定 α，用轴坐标写 T1=x+R v1、T2=x+R v2，v1/v2 单位且横截。先删去距 x≤L^-C 的 marks，仅损 O(N L^-C)；取 C 足大，该损失小于 N/(10L)。对 T1 按关于 x 的正/负半轴和 dyadic distance annuli 分组，可取同号、半径 r∈[L^-C,C_R] 的一个 annulus，含≥N/L^C 个 marks。令 i、y1 都从此组取，删去 |i−y1|≤L^-C 的 pairs；每个 i 被删 y1 至多 C N L^-C，余 pair 数仍≥N²/L^C。y2 取 T2 上距 x≥L^-C 的原 marks，≥N/L^C 个。

于是有 X_α，|X_α|≥N³/L^C，每 triple (i,y1,y2) 都有

    |i−x|, |y1−x|, |y2−x|, |i−y1| ≥ L^-C，

且 i、y1 同侧、其至 x 距离之比在固定 [1/2,2] 内。最后这个 annulus 选择避免把 pivot 的空间范围免费扩大到 N^c；所有 z 留在固定 bounded box。这里 density N/L 可远小于 cN；所有删选预算都按 L^C 计。

## 4. pivot 的精确公式、Ω 质量和 good-pair 关系

写 i=x+a v1、y1=x+c v1、y2=x+d0 v2，令

    b=d0(1−a/c)，  z_exact=x+a v1+b v2。              (2)

则 z_exact−i=b v2，且 y1,z_exact,y2 共线。§3保证 |a|,|c|,|d0|,|a−c|≥L^-C，a/c∈[1/2,2]，故 |b|≥L^-C，z_exact 在固定 bounded box，且距两条轴至少 L^-C。将 z_exact 取最近 δ-grid 代表 z；误差 O(δ)，角坐标公式受扰只增 L^Cδ。

给定 z，可恢复 i 的格点至 O(1)（平行 v2 向 T1 的投影）；给定 y1 后，直线 y1z 与 T2 的交点 y2 至多 L^C 个格候选，因所有交角/距离分母≥L^-C。因此每 z 的 triple fibre≤L^C N。又 z 在固定二维平面的 O(L^Cδ) 邻域内，总 z≤L^C N²。删去 fibre<N/L^C 的轻 z，仍保≥N³/L^C 个 triples，故有≥N²/L^C 个重 z。每 z 仅有 L^C 个可能 i，选其最富 i=i_(α,z)，仍有≥N/L^C 个实际 pairs。

令 Ω 为这些 (α,z)，并为每 w=(α,z) 固定上述由 X_α 生成的 pair 集 P_w；它不是任意旧 collinear pairs 的全集。于是

    |Ω| ≥ N²|A|/L^C， |P_w|≥N/L^C。                 (3)

P_w 预先保 |y1−y2|≥L^-C、|z−y1|≥L^-C，以及下面的 time 分母下界；删 lift marks 后不再另删这些几何条件。每个 w 的 |P_w|≤L^C N，因为每 y1 决定 y2 至多 L^C 个。

## 5. Córdoba f-map：方向恢复、能量与真 injective 子族

置 f(w)=(z,i_w)。由 z−i_w 的长度≥L^-C且其方向距 T2 至多 L^Cδ，物理方向分离只给 L^C 个 T2 候选；先按每 f 的最富候选删选，保 Ω/L^C，并使 T2 由 f 确定。注意只恢复方向已足够：原族每 δ-direction bin 只有 O(1) labels，不另赠 arbitrary many parallel labels。

按 θ=angle(T1,T1′) 的 dyadic 层估计 f-collision。固定 α 后，候选 T1′ 同 T2 和 T1 在其 O(L^Cδ) 二维平面内，方向在 θ 范围；δ-packing给≤L^C Nθ 个候选。对每一个，公共 i 在两 tube 交中有≤L^C/θ 个格点；每 i 的 z 沿 T2 方向有≤L^C N 个格点。T1′ 与 T2 的交点 x′ 只增 L^C 候选，因为 i 距 T2≥L^-C、所有轴长度 bounded，故 T1′ 对 T2 仍有 L^-C 角。每层总≤L^C N²|A|。θ≲δ 的对角层由单 α 的≤L^C N² pivots直接付；log N 被 L 吸收。

所以 Σ_f #f^-1(f)^2≤L^C N²|A|。CS 和(3)给 |f(Ω)|≥|Ω|/L^C。每 f 取一个实际 w，得 Ω0，f在其上真 injective 且

    |Ω0| ≥ N^(2n−d+2)/L^C。                        (4)

没有把全部 Ω 自动当 injective，也没有用一般原 incidence 的无证明 bounded multiplicity。

## 6. 正确 lift、时间公式与第二端点

对 w=(α,z)，定义支持线

    Tbar_w(t)=(x(α)+t(z−i_w), t)。                    (5)

忽略已支付的 O(L^Cδ) 误差，(2)中 y2=x+d0 v2 处的 lift time 是 t=d0/b。由 a/c+b/d0=1，有

    z=(1−1/t)y1+(1/t)y2，
    y1=(t z−y2)/(t−1)。                              (6)

因此 lift spatial mark 是 y2；(y1,t)一般不在(5)。由 good triples，|t|,|t−1|≥L^-C且 |t|≤L^C。这里不能只写 |t−1|≈1 后忽略其 soft 下界；反解(6)的误差放大恰是 L^C。

对每一共同原 triple (z,y1,y2)，取

    t*= ((y2−y1)·(z−y1))/|z−y1|²，                  (7)

再取最近 time grid。由于 z−y1≈(y2−y1)/t，这是共同 triple 决定的 t，**不依赖 α**。近共线误差和近轴误差使 (y2,t*) 距(5)≤L^Cδ。t*、t*−1 的同一下界保持（δ足小于 L^-C）；每 pair 的 marker由(7)唯一规定，不能为不同 α 分别挑不相同 t。

## 7. 真实单位窗、格误差和有限重数规范化

|t*|可达 L^C，不是固定 bounded clock。先对每 w 按整数单位 t 窗分 P_w，选最富窗，仍≥N/L^C pairs；再按其单位窗编号作一次 pigeonhole，保 Ω0/L^C 个 w共享同一窗。所有 lift 空间 marks=y2∈E 留在固定 box。共同平移 t→t−j 后，支持线在该单位窗内的部分处于固定 bounded graph chart；端点可保闭/邻窗有限复制，不删端帽质量。把此后子族记 Ω′，仍满足(4)但 C扩大；P_w也同步限制为该共同单位窗中的实际goodpairs，以下不再使用窗外pairs。

取一次 δbar=L^C0δ，C0大于前述全部格误差指数。原每 pair映到 δbar-liftcell时，其 fibre≤L^C：固定 y2/time格反解(6)只容 L^C 个 y1格点；因此各 w 实际生成的 distinct lift marks≥N/L^C。方向 w_spatial=z−i 在 fixed bounded range，原 i-grid δ分离；在 δbar尺度每方向bin只有 L^C 候选。每 z 固定有限/L^C coloring后取一色，损 Ω′/L^C，可使 lifted directions cδbar-separated。所有 marks仍为原 pairs所生成，不添加人工尾段。Nbar=δbar^-1=N/L^C，故改用 Nbar只改有限 L 幂。

以下用 N写回同尺度幂，所有格损失并入 L^C；这是明确的 scale-change，不是假 O(1) lattice multiplicity。因每个 w在同一真单位窗有 N/L^C marks，按原支持线 unit extension调用 finite seed时保原marks，不要求所延尾部有shading或承原PW。新时间坐标只是共同平移，回拉(7)仍使用原 t=j+t_new。

## 8. 正确 d-collection 及与 B 密度证书的接口

固定 z，Ω′ 的 f-injectivity给 i_w互异；方向由 bounded affine slope z−i_w决定。故任意 θ≥δbar 的 lifted angular cap，其 i落在半径 Cθ 的球内，由(1)

    # {w: lift direction∈cap(θ)} ≤ L^C(Nbar θ)^d。    (8)

每 z 总数≤L^C N^d，所需是 d-collection（即 K(d+1,d′) 的方向参数 d），不是 displayed (Nθ)^(d−1)。即使原 E 的 ballcap恰饱和，也没有额外一维改进；不把它当新几何定理。

我们所需 seed 是实际 unsaturated 版本：任意上述族的原平均 shading≥Nbar^-o(1)，有

    #union marks ≥ Nbar^(d′−d−o(1))·#lines。          (9)

它在本任务一般符号中具名 K(d+1,d′)+(40)；用于DIM的 d′=4−ζ时，R29 FSD001已有任意条数的实际有限版，可直接支付。ambient为固定 M+1；所有 C0/损失指数固定后再选择原 ε到 seed输入门槛内。没有要求 ambient随N增长或借字母d当整数。

## 9. retained lift marks 与原 triples 的精确定义

令 raw lift shading Ybar(w)为§7由 P_w生成的 lift cells。给定任意实际删选 Ybar_ret(w)⊂Ybar(w)，定义

    R(w,y1,y2)=1_{P_w}(y1,y2)
              ·1_{Ybar_ret(w)}(cell(y2,t*(z,y1,y2)))。 (10)

这是原 Ω′、原 pair以及已删后 liftcell 的联合指标；不能删去第二项。每个 retained liftcell至少由一个 P_w pair生成，故

    Σ_w,y1,y2 R ≥ Σ_w #Ybar_ret(w)。                 (11)

反向每 cell 的原 pair fibre≤L^C；所以 retained pair mass与真实 retained lift L¹仅差 L^C。即使全部某个 pivot 的 marks被删，只要总 L¹仍近满，(11)依然成立。没有宣 retained graph对原每条 T1/T2仍逐管近满，也没有把其平均密度改成逐pair条件。

## 10. 共同 triple、共同 liftcell 与 L² 下界

令 Σ 是 P_w所可能出现的共同(z,y1,y2)集合，保§4的距离下界及 L^Cδ近共线。固定 y1,y2，其距离≥L^-C，z 在固定 box内靠这条线：至多 L^C N个δ格点，所以

    #Σ ≤ L^C N |E|² ≤ L^C N^(2d+1)。                (12)

置 r(z,y1,y2)=Σ_{w=(α,z)}R(w,y1,y2)，μ_z(liftcell)=Σ_w1_{Ybar_ret(w)}(liftcell)。由(7)，每共同triple的所有 α都贡献**同一个** liftcell，故 r≤μ_z。反过来固定(z,liftcell)，y2在δbarcell内有≤L^C个原δ格候选，由(6)及 |t−1|≥L^-C，y1也只有 L^C个格候选。于是

    Σ_Σ r² ≤ L^C Σ_z ||μ_z||₂²。                   (13)

若密度证书给真实 Σ_w#Ybar_ret(w)≥N|Ω′|/L^C，则(11)–(13)及CS给

    Σ_z||μ_z||₂² ≥ N^(1−2d)|Ω′|²/L^C。             (14)

这是要求的 L² **lower**。它只使用 retained totalmass；原文删后直接使用每pivot旧(46)的近满pairs，可由(10)–(14)替代，不能把那一步原字面当已经证成。

## 11. 独立核密度截断逻辑及指数合并

独立给B所需接口核算。每 z记 m_z=#Tbar(z)、W_z=Σ_w#Ybar(w)≥Nm_z/L^C；raw multiplicity μraw仅计生成marks。令 H_z={μraw>Λ}，Λ=N^(d+1−d′+ω)，ω>0先固定。若 H_z占 W_z至少一半，则用单line≤CN的上界，取≥m_z/L^C条 heavy lines，每条 H_z marks≥N/L^C。对这一**坏 shading**用(9)，得 #H_z≥N^(d′−d−ε_seed)m_z/L^C。另一方面全 raw L¹≤CNm_z，却至少Λ#H_z；若 ε_seed<ω/4且原 log_N L充分小，即矛盾。因此保留 H_z外的 marks，可使 retainedL¹≥W_z/2，且 retained μ≤Λ。

严格顺序是先ω、再seed目标损失与输入η、最后原 ε≪η/C；不是为每N任选违反seed门槛的L。对无line的 z无操作，其他 z同一常数，不因z数目损失。实际用途 d′≤d+1；若抽象种子给 d′>d+1，(9)对任何非空近满族已经超过其≤CNm_z的总可见格点上界，normalized输入本身矛盾，无需用负幂threshold。于是

    Σ_z||μ_z||₂² ≤ N^(d+2−d′+ω)L^C|Ω′|。            (15)

这里高重数测试必须定义自 raw μ；定义自待构造 Yret会循环。结合(14)、(4)得

    N^(1−2d)|Ω′| ≤ N^(d+2−d′+ω)L^C，
    4d ≥ 2n+1+d′−ω−C log_N L。                       (16)

令源soft losses、ω依次趋0，得到normalized critical certificate。此处是 L¹×L∞ 的 **upper** 与 retained-CS 的 **lower** 比较；不跟随原文相反的 upper/lower 文字。随后已实际全文独读B终稿12节；其(3)–(11)以raw μ定义坏集、保same Ω′总mass、使用真实unsaturated seed和一致的retained indicator，与本独算相合。该实际读取不使A自身几何证明自动成为独立审查。

## 12. 反攻、停止边界与待交叉审查状态

独立反攻均保原分母：saturated仅N/L时仍有N³/L^C triples；goodpairs先排nearvertex/nearcoincident端点；pivot可能t≈1或t很大时分母/单位窗和δbar付费；f只恢复T2候选而非任意平行labels；先injective再取perz d-cap；删后仅用实际(10)；共同triple定共同time，单liftcell回拉只多L^C；seed坏shading的heavy成本和原Ω′分母均保。若去掉retained indicator，某pivot的旧pairs可以全删，原计数式即不再有理由成立；这反的是未标记的回拉，不是KT定理的反例。

已付是所列normalized有限模型的完整pivot/lift/retained证书和密度逻辑独算。未在本轮独证的是：提高极值d的全small-loss实现、heavy-ball regularization及其blurring/cap重建、bilinear θ归一化、源 K(d+1,d′) 的wholeproof；这些仍具名。没有因为该局部核心闭合就删去DIM001的原四维finite/高级输入条件，也没有新报六维17/4或wholeKT6.2已无条件逐式验证。已实际全文独审B的 notes/20_dimension_lifting/finite_seed_transfer/R0080_lifted_multiplicity_and_seed_scope_audit.md 12节：其d-cap/seed的共同格规范、逐z高重数反证、same Ω′分母、两侧L²指数及raising-d用途均无强制修正。特别确认seed只为lower拆boxes/颜色，不把每条line的不同归一化坐标混入共同energy。A自身pivot正证仍待root/B实际独审；root整合稿尚未在此声称读过。未经外部同行评审。
