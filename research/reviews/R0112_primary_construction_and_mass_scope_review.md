# R0112：新 primary 构造与投影原质量的独立逐步审查

2026-10-26，algebraic_gate。审查对象仅为他人稿 `notes/50_counterexamples/R0112_actual_construction_new_gate.md` 与 `notes/00_map/R0112_projection_geometry_input_gate.md`；本审查不把自己的 resolution 稿当作独立审查对象。只新增本文件，不改原稿、公共状态或 Git。结论限定于源资格和实际压力测试，未经外部同行评审；不认证一般 Kakeya、完整 mixed source 或新 major/ID。

## 1. 独立读域及总判定

已全文读上述两稿，回读本地 Lai–Wong v2 extracted 的 intro/Def1.1 与 §4.1–4.2（对应 PDF 约11–14页），本地 Wang–Wu v3 extracted 的 Def1.1–1.4、Th1.5/Cor1.6、Def2.3–2.5；另实际 browse 两固定版本 HTML，并用 Wang–Wu PDF 的第二页文字层独立核 (1.3)–(1.5)。本轮 web 的 Lai–Wong PDF cache miss，不冒称视觉核验本地 PDF。数学公式在现有 extracted/HTML 中可读。

Ren 另实际 browse [2309.04097v1](https://arxiv.org/html/2309.04097v1)，核 Def1.6–1.7、Th1.8、Prop3.1、Th3.3/Rem3.4 的完整 statement 与该节 proof strategy；未逐步重证整篇高级定理。R105 两份原 weighted planar/sphere 稿的相关章节实际读回，确认其仅是 derived 接口反攻。

两稿的主要拒门结论均成立：LW 指定生成 labels 与全部含单位段直线不可免费等同；WW 的必要 Γ 和 geometric-line 去重不能抹原 J；Ren 列出的直接映射没有可用的临界主幂。本审查列出两项须精确化的小修正，见 §6；它们不改变主结论，但归档为严格版本前应修。

## 2. Lai–Wong：同一个真实集合和 t=1/2 截面

独立设 D 为 base-4 数字 {0,3} 紧集，m=n−1。生成族的真实闭段为

    K0={((1−t)a+t b,t): a∈(D/2)^m,b∈D^m,0≤t≤1}.

紧性来自紧参数域连续像；每条段的物理长度为 √(1+|b−a|²)≥1，可截出同方向单位段。D−D/2=[−1/2,1]，因此生成 slope patch 有内点；有限个固定旋转覆盖方向球面后，得到同一个紧全方向单位段集合。这些操作既不按方向换集合，也不把 clock 长度直接当物理弧长。

独立核加法集：D+D/2 的四个数字为 0,3/2,3,9/2，四个比例 1/4 的相似像将 [0,3/2] 首尾相接地覆盖。由紧不动集唯一性，D+D/2=[0,3/2]，故

    (K0)_(t=1/2)=(D/4+D/2)^m=[0,3/4]^m.          (A)

这是一条 exact infinite-digit 等式，不是 finite approximation。它只占一个 clock 截面，和 n 维 Lebesgue 零不冲突。n≥3 时 m≥2，盒对角弦长 3√m/4>1，严格不等式有余量；n=2 不能用该单位弦论证，原稿已限定 n≥3。

源 §4.1 的 slice 相对系数确须为 (1−t)/(2t)，并非 (1−t)/t。这个固定倍不改变 t∈(0,1) 到相对投影参数的非退化性；所以它不反源中 a.e. slice 的零测度和满维几何后果。原稿对此限定正确。

## 3. LW 全部含段线的维数与 rotation/chart 量词

设 L1(K) 为全部在 K 中含一个实际单位段的 affine supporting lines。生成 labels 的维数 m 计算本身正确：端点对到 (slope,offset) 是固定可逆线性变换，D^(2m) 的 Hausdorff/packing 维数均为 m。

但 (A) 内还有 horizontal supporting lines。先取盒中心的对角线，其弦长严格大于1；方向和垂直 offset 在 m 维超平面内作足小扰动后，仍有大于1的盒内弦。因此其中有一个局部 line-space 开集，自由度为 (m−1)+(m−1)=2m−2。canonical compact chart 上度量局部双 Lipschitz，得到

    dim_H L1(K0), dim_P L1(K0) ≥ 2m−2=2n−4.       (B)

原始 source graph chart 不包含 horizontal 方向，原稿没有直接把 (B) 当作该 chart 内的计数。对把此 m 维超平面真正倾斜的固定 R，vertical coordinate 在 R 的超平面方向空间上是非零线性泛函；它的零集无内点。因此上述开族含一个 |u_n|≥c>0 的小方向帽。在此帽上

    slope=u_h/u_n,
    intercept=x_h−x_n slope

与 canonical affine-line 坐标局部双 Lipschitz，(B) 确进入该 source chart。只保竖轴的有限旋转无法用原 bounded-slope 生成 patch 覆盖 horizontal 方向，所以按生成 patch 作标准全方向 completion 必有倾斜 copy。另加一份倾斜 RK0 的安全版本更直接，保紧性/零测度/满维与全方向。

这不证明任意只凭未知 accidental lines 完成的有限旋转族都具有同样 chart 证书，原稿已明确不声此强量词。若 source 的 AK 被解释为全部含单位段 lines，则 n≥4 时 (B)>n−1，确不能用生成参数维数代替它；若 AK 被解释为选择的生成 family，则其单位圆盘的 all-offset 例也需消歧。原稿没有替作者任择定义，也没有把这个限制升级为整个满维构造定理被否，处理正确。

§4.2 的生成参数仍是共同 clock 的 F^m，slices 为 π_t(F)^m。各坐标的满维 a.e. clock 取有限交仍 conull，再 product/slicing 得满 n 维。它是本次 source 的范围核验，不给严格 Hausdorff 上界；R41/R93 旧指纹归类合理。acyclic 另加假设未从完整 compact family 提取，原稿按 R83 拒绝重开，也未把 partial 拓扑类作为本轮成果。

## 4. Wang–Wu：必要 Γ、R105 去重与 ordinary bush

固定 [2509.21869v3](https://arxiv.org/html/2509.21869v3) 的绝对 shading 常数为

    Γ_(Y,b)=sup_(ℓ,r,x)(h/r)^b h^(-2)|Y(ℓ)∩B(x,r)|.

原稿所抄 Th1.5 的 h、λ、a、a* 主幂及 Γ^(-1/2) 符号均与 PDF 第2页相符。对固定长度 dense segments，|Y∩B_r|≈hr（固定范围内），sup 在 r≈1 给 Γ≈h^(b−1)，0≤b≤1。于是

    h^((a−1)/2) Γ_(Y,a*)^(-1/2)
        ≈h^((a−a*)/2)
        =1 (a≤1),   h^(a−1) (a≥1).

所以 a<1 的表观负幂确被必要 Γ 抵消。概率 γ-upper 给 Γ≲M h^min(b,γ) 的计算也正确；它仍带每线绝对 mark 数 M，不能写成 free Γ≈1。此处未独立重证 WW 的整篇定理。

R105 已付的是同一个 π_W、h≈ρ^(1−χ) 的有权原访问，允许 line/point/u 重复。sphere/native-G 模型中所有 geometric lines 可相同，而且 point/slab/time-plane cap 仍成立；它缺完整 same-T、physical p↔Γ、filled X/Y/CW 的同时实现，原稿都明确保留。singleton 几何 L 仍满足任意 exponent 的 KT upper；拒门理由必须是原 J 经 distinct-line/ball union 丢失大重数，而不是 singleton “没有正维故不能用定理”。原稿对此区分正确。不能把 WW 既有真实分离 line set 的 random thinning 证明当成任意原 labels 的 weighted 无损去重定理。

ordinary bush 原分母可独立复算。用严格分离的 slope product grid v∈(MδZ)^4∩[0,c]^4（M 固定大、c 固定小），原 unit axes 是 (tv,t) 的单位子段，取共同 [a,b] 位于全部段的内部，给该 interval 的 full tube marks。则原 N≈δ^-4，每管 discrete clock mark 数 m≈δ^-1，原 discrete incidence I≈δ^-5；这与连续 Σ|Y_i|≈Nδ⁴ 是不同单位的账，两者都可明确换算。

π(x,t)=(x1,t) 只记 v1，distinct planar lines≈δ^-1，每条原重数≈δ^-3。每条保一个原 label 时 N'≈δ^-1、I'≈δ^-2，所以 p=q≈δ³、λ'=(p/q)λ≈1。保全部 labels 却用 projected union 同样只剩 δ^-2 个几何 line/clock 访问；WW a=1/Γ≈1 能合法给二维投影下界，却没有偿付原三维 fibre。该 bush 满维，不能当 Kakeya 反例或所有投影法的不可能性定理。

## 5. Ren：实际输入和直接主幂

核 [Ren v1](https://arxiv.org/html/2309.04097v1) 的 Def1.6–1.7/Th1.8/Prop3.1/Th3.3 后，原稿所分的两种直接用法范围正确。Th1.8 需真实每点的 tube pencil 同时有 ball 与 plate 衰减；Prop3.1 虽移除了 pencil 非集中，仍需真实 quasi-product points 及每点 tube 数。κ1 原 Φ_p 对应约 δ^-1 个不同物理管，只付 s≈1，δ^(-2s−ε) 的 total-tube lower 远不足以超过原约 δ^-4；重标 angles 或把二维 code fibre 当 tube 不合法。

有用主幂的准确阈值是 2s+ε>4+O(η)，见下节文字修正，不应把 s>2 当作必要条件。此修正不接近修复 degree 从约1到约2的缺口。

Th3.3 要 scalar clock、真实 tube plate upper、clock measure upper 和角度下界，且同一个 good-clock 集对所有 sufficiently-large tube subsets 有效；粗糙矩阵 F(u) 不能直接换成 uI。其 ε 可向下缩小：输入门槛更强，good mass、subset 门槛及 lower 均同时变弱，原稿这项单调性解释正确。N≈δ^-4+O(η) 时可输入的 s 至多 2+ε/2+O(η)，slice lower exponent s+ε 至多 2+3ε/2+O(η)。即便宽授 Lebesgue clock 并把 slice 转回实体，直接只给约3维，不到既有4入口。

对 shading 必须在每 clock 用 active 原 T_u，而不是原 full T 的整 slice。若平均 λ≫δ^ε，以原 I 提取 rich clocks且排 good-clock 例外可收费；若不满足，则无此免费转换。原稿没有把 whole-tube slice 当 shaded slice，限制正确。以上拒门只针对写明的原映射，不宣称 Ren 所有可能用途无效。

## 6. 两项小修正与最终限定

1. 投影稿 §6 的 slope grid 当前写为 `(cδZ)^4∩[0,c]^4` 且 c 小，字面只给 fixed-comparable c'δ 分离。为与声称的严格 δ-direction-separation 一致，改成 `(MδZ)^4∩[0,c]^4`、M 固定大，或把结论准确写成固定倍 δ 分离后统一改尺度。N/I/p/q 主幂完全不变。
2. 投影稿 §7 的 “s>2 的有用尝试”须精确化为 “若欲使该 lower 超过原 N，需 2s+ε>4+O(η)，故 s 须接近2；例如 s>2 是充分但非必要范围”。s=2−ε/4 已可使形式主幂超过4，因此不能字面声只有 s>2 才有用。原 source 每点仅 δ^-1 的拒门保持。

除此未见会推翻两稿限定结论的强制修正。上述两项由主代理统一处理后，两稿可作为内部源资格/压力测试记录归档；此“通过”不覆盖源全部高级 proof，不构成新维数结果/完整 source 反例/重大中间结果，也不把未达成长期 Goal 变成完成。所有同步和未来公共状态由实际权威回执另验。

## 7. 最终读回：两处已修与 root 的 OWY/文献范围整合

随后实际读回投影稿 §6–7 的当前文本：slope grid 已改成 `(MδZ)^4∩[0,c]^4`，附 bounded-slope 双 Lipschitz 与 M 足大的严格分离说明；Ren 已改成准确的 `2s+ε>4+O(η)` 门，并明确 source 没有供应可使 s≈1 时 ε>2 的定量下界，不宣最优 ε 或所有可能用途不成立。§6 所列两项现均已修，保留原审查发现的历史而不删改。

又实际全文读 root `notes/00_map/R0112_macro_and_charged_geometric_return.md`。本次只复核其中 WW/Ren/LW/OWY、宏观范围与声明边界；root §2 的 resolution 来自我自己的原稿，不在此充当它的独立审查。

root §3 对 WW 的 Γ cancellation、singleton 适用与原 J 去重的区分，和 Ren 的 degree/plate/scalar-clock/active-subset 用途，与上述独立复算一致。约3维直接出口是当前已匹配调用的保证；不把存在一个可任意向下弱化的小 ε 理解成对最优改善量的上界。root §4 的 LW 同一集合/t=1/2/单位弦/2n−4 与倾斜 chart 证书，及生成标签量词限制，都保持上述正确范围。

对 root 新增的 OWY 资格例另作独立核验。实际读本地 `literature/extracted/R0112_oregan_wu_yi_2607_08461_v1.txt` 开头的 Def1.1 及 Th1.5；再 browse [同固定 URL 的 HTML](https://arxiv.org/html/2607.08461v1) 的 Def1.1/Th1.6。两种呈现的 transversality 都要求

    inf_(θ∈I)(|f(θ)−g(θ)|+|f'(θ)−g'(θ)|)
        ≥ T^(-1)||f−g||_(C²(I)).                  (C)

独立取 I=[−2,2]、t0=0、f=0、g(t)=a t²，0<a≤1/10。两函数均在 C² 单位球内，且属于一个小三参数系数盒 `c0+c1 t+c2 t²`。在 θ=0 左边为0，而右边至少 2a/T>0；所以任何有限 T 都不能使含这两函数的 family 满足 (C)。对任意固定 t0，同样可用 a(t−t0)² 并把 a 固定取小。更一般，一个真正三维 C² 线性空间的 evaluation map `h↦(h(t0),h'(t0))∈R²` 有非零核，取小倍的核向量就给同样反攻。这是 elementary rank-nullity 加一个真实 double-zero pair，未把高阶光滑误当 transversality。

此例准确否定“有界次数/光滑即可自动送入 OWY 定义”的接口；它没有从完整 rough source 提取这个三参数盒，也不排系数相关后的合法 transversal 子族。root 已明确写此量词，不存在把它升成 source/Kakeya 反例的问题。

本地 PDF 提取文本显示 Date July10/2026、Th1.5/(1.6)，网页显示 Date August24/2026、Th1.6/(1.7)，与 root 的差异记录一致。Def1.1 及式 (C) 在两处一致；只消费这个定义不依赖更改数值定理编号。两处 t* 的 brace 文本均未被 root 默补为新的已核 min 公式，root 未以 OWY 主定理数值推出新 bound，处理合适。

root §5 将新限定压力证据、实际 primary 资格匹配与“无 ordinary/source 正 gain”分开；保四完整出口、旧冻结、不用 joint-law 附加假设充新 working，也不以宏观或来源入库完成长期 Goal，范围无夸大。当前未见新的强制修正。两份被审稿及 root 上述**非 resolution**整合可按内部有限资格审查归档；不预认证 Git/sync、源全 proof、外部同行评审或未来完成状态。
