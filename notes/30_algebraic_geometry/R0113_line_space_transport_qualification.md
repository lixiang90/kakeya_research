# R0113：直线空间 transport、方向别名与位置偿付的资格审查

2026-10-26，algebraic_gate。只编辑本文件，主代理统一 Git。已运行 context，实读当前 GOAL/STATE、R112 next、R112 原 chart 反例及其限制；定向实读 R59 joint-PW graph、R61 fixed-format line-parameter/projective 证书、R87 fullG4 范围和 R83 line-union 输入审计。不重跑旧计算。本轮没有新 ID/major/ordinary 界，未经外部同行评审。

## 1. 当前问题和先验停止条件

目标是检验 R112 方向别名的真正后继，而非再次声好 chart 免费保方向帽。精确问：一个统一 C² biLipschitz ambient map 若把真实原 R5 单位段送到非短直线段，是否可证明原方向的别名必由 target transverse position 分离偿付，并据此付一个保原 W/I 的四维估计？本稿分别核“别名内的位置偿付”和“跨不同方向包的体积求和”；前者成立不代表后者成立。

候选先分两种原输入：

* 只有物理 δ 方向帽权≤α，则 all-scale upper 仅可自动取 s=4。
* 若另已给所有 δ≤r≤1 的 s=3 方向 KT upper，则原 full family 已可直接调用全 ambient FSD001。任何仅重新包装其同强度 positive-power lower 的 chart 结论，先按旧全称闭包拒作新机制。

本轮停止条件：得到的位置偿付若只有 joint line-parameter KT，而相应四维结论对真实 tube 反例失败，或完整 s=3 用途已由旧 FSD 直接支付，就不把所缺跨包定理添成成功假设；不再调 R112 的 degree/chart/Jacobian/r 参数。

## 2. 一个完整可证的 transport 事实：两端点已足够

固定 R,L≥2。设 F:U→V 是 R5 开集间的 L-biLipschitz homeomorphism（C² 是更强条件），U 含原单位轴 ℓ_i 和固定倍 δ 邻域。每条 F(ℓ_i) 是直线段，落在 B_R，长度在 [L^(-1),L]；为真实四维调用，另要求它们落在同一个 affine H4，刚性坐标取 H4={x5=0}。原轴可带重复 indices/非负权 w_i，总 W。

设原无向方向 v_i 对所有 δ≤r≤1 有

    Σ_(angle(v_i,v0)≤r) w_i ≤ A (r/δ)^s.          (1)

仅 fine cap≤α 时，可令 s=4、A=Cα；s=3 不由 fine cap 免费获得。

对 target segments 作固定有限次 whole-label 分组：先用某个 H4 坐标满足方向分量绝对值≥1/2 的 bounded-slope chart；取此坐标为 target clock t 并统一正向。其 clock 长度至少 c_L，位置有界，故有限个固定 clock intervals 中有一个闭 J_k⊂proj_t F(ℓ_i)，长度 c'_L。按这个 k 分组。分组不裁任何 marks，也不选其中一个组假称保全部 W；所有组的 W/I 仍可精确相加。

每组取共同 τ0,τ1∈J_k，τ1−τ0=c''_L>0。target supporting lines 写为

    γ_(b,u)(t)=(b+t u,t,0),     b,u∈R3,

参数均有固定界。记 ψ=F^(-1)。在该组，原有向单位方向恰为

    V(b,u)=[ψ(γ_(b,u)(τ1))−ψ(γ_(b,u)(τ0))]
           /|ψ(γ_(b,u)(τ1))−ψ(γ_(b,u)(τ0))|.      (2)

原因是两点确在同一原轴中，并非只在其 δ 邻域；按 target clock 定向后，差向量与原单位方向同向。分母≥L^(-1)(τ1−τ0)，分子差随 (b,u) 的变化由 inverse Lipschitz 常数控制，故

    |V(b,u)−V(b',u')|≤C_(L,R)|(b,u)−(b',u')|.     (3)

这里在仅由实际 labels 构成的参数域上比较即可，根本不需把 ψ 延到所有缺失线或假设最近点 selector。有限分组也处理了同一 target supporting line 上 longitudinally 错开的非短段；没有共同两端点时，不能无条件用 (2) 比它们。

由 (1)–(3)，每个 group 的 target **joint** line-parameter 球满足

    Σ_((b_i,u_i)∈B(p,r))w_i ≤ C A (r/δ)^s,
    δ≤r≤1.                                      (4)

因此固定 target δ 方向帽内，每个 transverse δ-offset cell 的原权至多 C A；固定方向帽与半径 r 的 offset 球联合也有 C A(r/δ)^s upper。原 directions 严格 δ 分离时，每个 joint δ cell 只有固定个 labels，可有限着色成 joint δ-separated families。它不表示任意两根 target 近方向轴的 offset 都必须 δ 分离；target δ 方向帽自身还有固定倍 angular 余量，正确陈述是上述 cell 的**有界原权/重数**。

C² 条件另允许局部 jet 公式 V=normalize[Dψ(γ(t))(u,1,0)]，因为该曲线就是原直线；Dψ 的 Lipschitz 常数也给 (3)。但两端点证明更弱且完整，不能把这个初等事实冒称新的 C² 结构定理。

## 3. 原 marks/clock/体积在这一步没有消失

原 measurable Y_i⊂Nδℓ_i 的像是实际 F(Y_i)，不是 target envelope 的 full shading。biLip 给实体体积上下固定倍、image 支持在 target C_Lδ-round tube、轴长上下固定倍；共同延长为固定长度包络只改 density 固定倍。C² 情形沿轴的 target clock 是单调 reparameterization，速度上下有固定界；它不等于原 clock，但没有 δ 的幂次损失。

finite whole-label 分组只重新分配各自原 marks。若后来另作 label/mark restriction，仍是

    W'=qW,  I'=pI,  λ'=(p/q)λ,

此处 I 为 weighted Lebesgue incidence Σw_i|Y_i|；若用离散访问数，须实际网格/clock 转换再计，不与 I_vol 混用。归一概率 cap 要除 q。平均 density 不能自动送逐管，heavy 到 ≥λ/2 时只保证 W'≥λW/2 和保固定比例原 I。transport 的 (4) 对所有合法 label restrictions 继承未归一 A；它不为后来的 marks restriction 恢复 density。

## 4. 严格压力测试：joint 3-KT 和别名内 offset 分离不够四维体积

下面是真实 R4 管族的完整反例，准确攻击一个**中间 proxy**，不冒充满足原合格 lift 的反例。R4 坐标为 (t,x1,x2,x3)。令 a,u,v 在一个固定小 box 的 Mδ-grid 上变化，M 固定大，取单位轴

    ℓ_(a,u,v)={(0,a,0,0)+τ(1,u,v,0)/√(1+u²+v²):
                |τ|≤1/2}.

给 full marks Y=T=Nδℓ。N≈δ^-3、|T|≈δ³、逐管和平均 λ=1。canonical line parameters 是

    offset=(a,0,0),   slope=(u,v,0),

所以对所有 δ≤r≤1，每个 joint r-ball 含至多 C(r/δ)^3 labels，fine joint cap A_joint=O(1)。每个 fixed (u,v) 的方向 bin 内，不同 a 的 offsets 确为 Mδ 分离，其 round tubes 有固定 overlap；别名内位置偿付已做到。

但全部管均在 H3={x3=0} 的固定倍 δ 邻域，故 |E|≤Cδ。反向只用 u=0 子族，在 t∈[1/8,1/4] 的固定 clock slice，(a,tv,0) 是二维 δ-separated 网；相应三维 cδ balls 不交且属于原 tubes 的 slice，slice 体积≥cδ。沿 t 积分给

    |E|≈δ,   Σ|Y_i|≈1.                           (5)

故声称一般 4D full-density joint-3-KT family 都有

    |E|≥c_ε δ^(3+ε) N/A_joint                     (6)

在任何固定 0<ε<1 都严格失败：右边≈δ^ε，大于 (5)。full marks 下没有平均/逐管或端帽损失可补。重复方向内的 tubes 基本分开，跨**不同**方向包却有平均≈δ^-1 的 overlap；(4) 本身没有付这个求和。

此反例不反 (2)–(4)，也不反真正“来自同一 F 的原方向 law”类。尤其若它能经 uniform biLip inverse 变为原 R5 的 s=3/A=O(1) 合格直线族，则 target 4D δ-tube union 乘 normal δ 的体积≈δ²，inverse 像可覆盖原单位 δ-tube union。旧 full-ambient FSD001 却会给 ≥cδ^(1+σ)（任取 σ<1 并用 full marks），矛盾。因此这个 proxy 虽有 (4)，并未保住所有实际 lift 信息；不据它宣布 complete transport-to-source 被反。

## 5. 旧统一闭包先行：s=3 下的体积回传不新

在原 R5 已有 (1) 的 s=3 情形，FSD001 对全部原 centers/真实 marks/条数统一适用，nearfull 给

    |∪Y_i|≥c δ^(4+ε) W/A,                         (7)

或其已有显式 density/log 版本，η 在 ε 后取小。F 的固定 Jacobian 比较立即给同强度的实体 image lower。若要对 target H4 中、支持在**实际 image segments**的固定倍 δ envelopes 内的任意真实 4D shadings 得相应估计，先取其 normal cδ extrusion，再经 ψ 返回原固定倍 δ tubes：体积、density 和 union 仅固定倍变化，原角 law 仍是 (1)，故 (7) 除以 δ 就得 target 4D 的 δ^(3+ε)W/A lower。不能把任意新延长段上的 marks 说成这些原 segments 的像。这是旧全称输入的一次真正合法重调用，不依赖新 packet 分解。

所以“给定合格 original s3 lift 的四维估计”虽比一般 joint-3-KT 类强，当前所需体积强度仍在旧 FSD 闭包内，不能另起结果/方向或称超出 DIM001。反方向也不能从体积 lower 构造 (2) 的同一 inverse chart；不声两种结构命题全等价，只按所需 positive-power 输出排重。

如果 original 仅有 fine angular cap，则 s=4 才自动给出，(4) 也仅是 joint-4-KT；不能把 target H4 的三维 direction space 当作原 s3。这个 s4 类的有用增益并未由本稿取得，不能先假一个带位置权的四维定理就称新 bridge 完成。

## 6. 与 projective / G3 / fullG4 的真实边界

R61 的正面 projective 恢复另要**固定格式 dim≤3 的 line-parameter carrier**和原 absolute PW；其 bad-sweep 小体积/CAD/有限 clockprojective 机制能实际付原 incidence。一个 joint s-KT 的有限集合不自动有这个 fixed-format carrier。任意 C² F 本身也可能任意高复杂度；不能对 F^(-1)(target convex/semialgebraic test) 免费调用原 polynomial-Wolff，因为该 inverse image 未必半代数或统一格式。R112 的 β 特例是多项式并不能替一般 F 支付这件事。

R59/R60 的 physical dim≤3 carrier 已有 joint-PW graph/GWZ 出口；dim4 同样的 graph/normal-fiber/whole-containment 查询在 R87 已核，但一般 4D full indexed-CW 不是已付 DIR4。当前 (4) 不把 whole-containment CW 变成 partial-fraction PW4，更不控制所有方向包在实体中的 overlap。§4 的 H3 proxy 也不能因在低维平面内，就声它违反旧 G3：旧 G3 消费的是原高维方向或原 PW，而不是本例的 joint-3-KT 这一项。

fullG4 原 axes 只是 metric δ-near P=0，一般没有一个 uniform C² ambient chart 把**全部这些近轴**精确送成直线。R87 已有 near-axis≠exact-Fano 的真实反攻；本轮的 exact image-lines 假设不能免费授予它。若 map 只近似送曲线到 δ 线，还须重新证明两端点、marks、clock 与原帽误差，不能以本稿精确情形代替。

R83 一般 line-union theorem 的实际参数强度和 Fubini/whole-clock 责任也已读；把 (4) 叫“line-space Frostman”不会提升已知输出，亦不保全部 finite marks。这里没有新增泛 line-union 搜索路线。

## 7. 一手检索范围与结论

为核 projective/path 名称是否已有匹配，本轮有限 browse 了库中已有 [Guo–Guth–Nadjimzadah–Shen–Zhang 2607.27629v1](https://arxiv.org/html/2607.27629v1) 的 abstract/intro、非退化完整 path family 的说明及 Informal Th1.3/1.4；未重证90页高级 proof，未新下载/新入库。该源的固定解析/非退化族、方向标签与 path 几何的区分，以及主要 R3 结构范围不能当作本轮任意选定 C² R5 line subfamily 的无损 transport 定理。R12/R51/R82 已有该来源指纹，本轮不报新发现。

本轮明确可付的是 (2)–(4) 的共同两端点 transport：原 direction law 能送成 joint law，方向别名在 transverse δ-cells 内只有受控原权。它是实际几何事实，但初等且不是新的主幂增益。真实4D full-mark 族 (5) 严格否“仅凭这种 joint cap 和别名内 offset 分离即可调用 (6)”的中间桥。对完整 s3 lift，所需 lower 已由旧 FSD 统一重调用；对 ordinary s4/fullG4，尚没有新的实际位置—方向 cross-packet 输入。

最小未付内容因此很具体：同一个 nonlinear inverse 与全 straight-line incidence 所保留的额外跨方向相容性，不能丢成一个 joint KT 常数后再用一般4D估计；但本稿没有将该相容性写成一个欲证公设来结案。按预设停止这一接法，不续 chart/r/D/CW 常数，不新增 ID/major，不反完整 G4 或真实全方向 Kakeya。长期 Goal 保持原完成门槛。
