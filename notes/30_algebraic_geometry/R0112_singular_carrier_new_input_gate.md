# R0112：奇异载体的 resolution / 高阶参数化资格门

2026-10-26，独立分工 algebraic_gate。只编辑本文件，主代理统一整合和 Git。已运行恢复脚本，实读 GOAL、STATE、ROADMAP、registry 开头及 R111 next，定向实读 R85 regular-leading、R87 全 G4/factor/投影余口、R89 cut/degree/graininess、R44 多项式 presentation 与 R56 连续抽最高项责任。以下不是新数学 ID、普通维数改善或重大性声明；本稿的独立复核待主代理实际整合后记录，未经外部同行评审。

## 1. 当前命题、量词、失败条件先锁定

要接近总目标，须取得能处理真实 R5 近超曲面的 position–direction 联合质量的输入；单独修好载体的奇点不够。候选检查仍面对 R87 的完整 G4：固定 D,R,C,C0，对每 ε>0，存在 η,c,δ0>0，使每个可依 δ 变化、非零、degree≤D、系数 l1 范数为 1 的实 Pδ，以及原 whole unit axes

    ℓ_i ⊂ B_R ∩ N_(Cδ) Z(Pδ),   T_i=Nδ(ℓ_i),

原非负权 w_i、总 W>0、每个原物理无向 C0δ 帽的权≤α，和可测逐管 marks Y_i⊂T_i、|Y_i|≥δ^η|T_i|，须有

    |E|=|∪_iY_i| ≥ c δ^(4+ε) W/α.                    (G4)

不加 physical/leading gradient floor，不先假 exact 轴、共同 chart 或原来没有的 PW4/方向帽。常数不能依最小非零系数、判别式、奇点距离或归一化条件数；D 固定也不限制 Pδ 的系数接近退化的速度。

本轮只检一个具体新桥：由 uniform resolution / C^r 参数化或分层各向异性坐标得到可调用的旧四维输入，并在原对象上付清 marks、方向帽、尺度、Jacobian 与求和。预设停止：若实际定理只控制 forward derivatives，或真实图变换不能保原方向帽且没有新的位置—方向求和证据，拒选；不通过增加 desired cap、Jacobian lower、richness 或 generic-normal 假设结案。一个坐标桥反例不等于 G4 或 Kakeya 反例。

## 2. 实际一手输入与读域

本轮实际 browse [Binyamini–Novikov, arXiv:2009.02082v1](https://arxiv.org/html/2009.02082v1)，唯一 v1 日期为 2020-09-04。实读 Th1、Def2–3、Th2、§2.1–2.2 的解析参数化障碍全证明、§3.1 Lemma9 及证明、§3.4–3.5；未称本轮逐步独证全部十页的高维归纳。

具名输入的实际内容是：固定 ambient、维数、半代数格式与有限 r，可以用统一有限个 C^r maps 覆盖，forward r-norm≤1；其 cellular 版本可对系数参数族统一。它不声明 ambient 可逆延拓、inverse derivative/Jacobian lower、仿射轴保持或方向帽保持。Lemma9 的幂代换正会改变 clock。§2 的 xy=e 例另外排除了同样统一的固定复邻域解析范数版本，所需图数至少按 log|log e| 增长。这些是文献陈述/具名证明输入，与下文自证的 tube 接口测试分开。

主代理已存 `literature/primary/R0112_binyamini_novikov_2009_02082_v1.pdf`，10 页，182648 bytes，SHA256 `6b612bec3feee5b42cbd6612d37340b40f92f80e3bf72f65dbf581c4dbb88949`，及 extracted 同名前缀 txt。本分工实读其 extracted 开头再核 Th1/版本。最初同时 browse Burguet math/0509277 的 abs，实际只读 abs，不以它为额外已读 proof；1802.07577v3 HTML 返回 404，不据此声该论文没有相关定理。Bierstone–Milman alg-geom/9709028 只取得一手 abs/书章首页摘要，未用它的完整 resolution theorem 推任何 tube 结论。

## 3. 固定有限 r 真能提供什么

半代数 carrier 的统一 C^r 图和 R87 的有限 global-Lip 分解可以处理 physical singular strata；这不自动提供高维 incidence 的新输入。若取固定大 r 并用参数网 s≈δ^(1/r) 做 r−1 阶 Taylor 近似，每个四参数图需 O(δ^(-4/r)) 小盒；r 在 ε 后取大可以使这个**参数盒数**成为小幂费用。这只是参数域近似计数，不是已经把原单位轴分配到相同数量的合法四维线族。

需要分别证明：一个原轴的 δ-neighborhood 是否有单值 lift；lifted 轴是否仍是 line，或是否有原 marks 密集的可线性化子段；回到实体时 multiplicity/Jacobian 是否受控；lifted cap 是否由原 α 控；空间包求和是否 bounded overlap。forward C^r upper 对这五件事均没有给 lower。若让 r=r(δ) 增长，则 Th1 的 C(r,D) 不能凭“统一”二字写成 δ^o(1)；须实际引入另一个定量定理。即使另有 polynomial-in-r 图数，也不修复 line/cap 的接口。

这里没有沿 R44 的 degree 近似公式或 R56 的 Chebyshev/最高项范数再调阈值。用 r 很大的 Taylor 图替换 P 也不会把 polynomial-near 自动升级为 metric δ-near，且每个测试 presentation 的 degree、盒数和原 mass 仍须另付。

## 4. 新的具体压力测试：甚至 biLip 且保直轴的 blow-up 也不保原方向帽

此处自证一个准确的桥失败，不是换另一个 quadric-spread 公设。取固定不可约二次超曲面

    P(x)=(x1 x3 − x2²)/2,     x∈R5,

系数 l1 范数为 1。其 singular locus 为 {x1=x2=x3=0}×R²。标准 ambient blow-up 的一个实 chart 为

    β(u,v,w,z1,z2)=(u, u v, u w, z1,z2),
    P∘β=(u²/2)(w−v²),    det Dβ=u².                 (1)

只在固定紧区域 u∈[1,3]、|v|≤1/10、|w|≤1/50、|z|≤1 内工作。β 及 β^(-1) 都有统一有界导数；这里没有任何 δ 条件数退化。因此以下方向帽崩塌不能归咎于靠近 exceptional divisor 的 Jacobian。

采用主代理建议的三参数强化，固定 r0=2，让 q,b1,b2∈[-1/20,1/20]。令

    L_(q,b)=√(1+q²+q⁴+b1²+b2²),
    A_q=(r0,r0q,r0q²,0,0),
    V_(q,b)=(1,q,q²,b1,b2)/L_(q,b),
    ℓ_(q,b)={A_q+t V_(q,b): |t|≤1/2}.               (2)

每根原轴是真实单位段，且 x2=q x1、x3=q²x1，故 ℓ_(q,b) exact-contained 于 Z(P)，全部落在固定 B_R 内及 (1) 的好区域。取 q,b1,b2 的 Mδ product grid，M 是足大固定常数。由 v2/v1=q、v4/v1=b1、v5/v1=b2 及 v1≥c>0，(q,b1,b2)→V_(q,b) 有统一 Lipschitz inverse。因此原方向确为 C0δ separated，N≈δ^-3；对所有 δ≤θ≤1，任意 θ 帽至多 C(θ/δ)^3 个原 labels。这正是 s=3 的全尺度 cap 域，不是只保总 N 的 toy。取单位权和 full marks Y_(q,b)=T_(q,b)，原 λ=1、W=N、α=O(1)。这里原 N、物理轴、whole clock 和 marks 全部明确。

直接代入 inverse，得到

    β^(-1)(A_q+tV_(q,b))
       =(r0+t/L_(q,b), q,q², b1t/L_(q,b),b2t/L_(q,b)). (3)

所有 lifted axes 仍为仿射线段，长度在固定上下界之间。对每一个固定 b=(b1,b2)，全部 q 的单位方向却**完全相同**，都平行 (1,0,0,b1,b2)。所以一个固定倍 δ lifted-direction 帽承载至少 cδ^-1 原权；要用原 α 作帽权，必损 δ^-1。全部 lifted directions 本身只有二维，q 被完全送到 offset。tube 厚度在此仅固定倍变化，marks 及体积 Jacobian 也仅固定倍变化，长短轴可以固定延长但不填 marks。因此这个测试没有偷用曲线变直、端帽忽略或原质量归一化。

准确被否的桥是：

    “在统一 biLip resolution chart 上，若所用原轴的 lift 仍直，
     就可把原物理方向 cap α 直接送给 lifted line family。”

β 在 (1) 中去掉 exceptional factor 后的载体是 w=v²；再做 w'=w−v² 的固定 shear，可把载体变成平面，同时 (3) 的轴仍直、每个固定 b 的方向仍完全相同。故 regular carrier / plane carrier 也不恢复所丢的方向信息。原 q 方向参数已经变为 lifted **位置**参数，正是需要额外联合求和的内容。

原实体质量也可直接校准为 |E|≈δ。上界：全部管在 u∈[1,3] 上 smooth graph x3=x2²/x1 的固定倍 δ 邻域，图的导数固定有界，故体积≤Cδ。下界：固定原 x1=r0+s，s∈[1/5,3/10]，每轴在该切片上有真实点

    ((r0+s)q, (r0+s)q², s b1,s b2)

且都在轴内部离端点固定距离。不同 (q,b1,b2) 的这些 R4 点以≥cMδ 分离，故取 M 足大，其周围 cδ 四维球两两不交并含于原 round tubes 的切片；切片体积≥cNδ⁴≈cδ。沿 s 积分给下界。由此 I=Σ|Y_i|≈Nδ⁴≈δ、λ=1，没有小密度隐藏；G4 所求仅 δ^(1+ε)，本例与它相容。

本例不反“存在更好 chart 或 packet 分配”的全称定理。事实上 q 在此成为空间分离的 offset：inverse tube 的 v 坐标落在 q±Cδ 内，按 Mδ 的 q 包分组时只有固定 overlap。每包有≈δ^-2 个 b labels，逐包调用再求和能恢复本例的预算；只用全局方向帽则看不见它。它也不是 G4 反例：全族 exact-contained，R87 已核的 FSD001 s=3 统一闭包可直接处理，毋须本次 resolution。曲面是 cone 并不把 R89 的 II 非零/方向 span 旧反攻冒成新结果；此处测试的是方向→位置在精确 blow-up 里的迁移。

## 5. 真正靠近 exceptional divisor 时还须额外支付形状与密度

在同一 β 的 u∈[r,2r]、|v|,|w|≤c、δ≪r，Dβ 的三个横向/纵向特征尺度可比 1,r,r,1,1，det≈r²。inverse 会把物理 δ 厚度放大至 δ/r。对沿自由 z1 的物理单位 round tube，inverse 实体横截面在 (u,v,w,z2) 上分别可比

    δ, δ/r, δ/r, δ.

其体积≈δ⁴/r²；若硬放入 round h=δ/r、单位长的 envelope，后者体积≈δ⁴/r⁴，故实际 full marks 的新 density 仅≈r²。原 full density=1 也不能写成新 full density。若原 marks 任意，只能按真实 Jacobian/分片计，不能先把 5D 体积除以 r² 当处处恒等；在该 annulus 可比较而非全域相等。

取 r=δ^a、0<a<1 固定（这样才同时满足此前δ≪r），这已是固定幂 density 损失 δ^(2a)，不能对任意小 ε 自动当 δ^o(1)。放回原 E 要乘回相应 Jacobian，新的 round 尺度 h 也改变其方向帽和 source nearfull 门槛。这个单管例只是 shape/density 的 sharp 局部测试；它没有声称 r 一定由完整 source 强迫，更没有把分层后所有 r 的损失都判不可付。§4 已在 r 固定时独立显示，光修好这项条件数仍不够。

## 6. 第二个压力测试：固定 degree 不付 exact analytic chart 数

为免把 finite-r 参数化误读成统一解析 resolution，取

    eδ=exp[−exp(δ^(−a))], a>0 固定,
    Qδ(x)=(x1x2−eδ)/(1+eδ).

这仍是实不可约 degree 2、系数 l1 范数 1 的合法 Pδ，且 real singular locus 为空。考虑其 positive branch ×(0,1)^3。要求每张四参数 chart 在参数 cube 的固定复 1-neighborhood 上 holomorphic、各坐标模≤2、且 image **精确**落在 Qδ=0，则图数至少 c log|log eδ|≈cδ^-a。

说明高维 product 不绕开文献的一维障碍：恒等式 x1x2=eδ 经解析延拓仍成立，所以 x1 的复值落在 annulus A(eδ/2,2)。固定其它三个实参数，沿任一参数坐标的复线段运用 §2 的 Schwarz–Pick；该坐标从 0 到 1 的 image hyperbolic diameter≤常数。改变四个坐标至多给四倍该常数，故一张图的 x1-image 的 annulus hyperbolic diameter 统一有界。实参数域连通，其 positive x1-image 是区间，而要覆盖的 x1∈(eδ,1) 的相同 hyperbolic 长度≈log|log eδ|。区间覆盖长度比较给所述图数下界。这一步是文献 §2 论证的明确四参数 product 应用，不是声称任意 resolution 的 chart 数都有此 lower。

因此对 ε<a，把这套**固定复半径、固定解析范数、exact**图强写成≤δ^-ε，不可能从 fixed D / coefficient norm 归一化得到。允许图的复半径退化、解析范数增大或 nonlinear ambient maps 时，须实记那些费用。

尤其不能由此推出 δ-metric approximate resolution 失败：当 eδ 极小时，许多区域确可由坐标平面在 δ 精度逼近；准许换 carrier 的 packet 方法可能避开 exact analytic 下界。但它须证明保原 marks / whole-axis 的合法替换和原质量求和，不能把 exact resolution 的存在性当作该结论。此例的 exact 轴也可沿自由三维取，属于旧 exact/FSD 可调用范围；不以新 coefficient 取法重新登记数学结果。

## 7. restriction / shading 闭包与排重

whole-label restriction 保 Pδ、原 whole-axis 条件与未归一 cap α；只保实际剩余 W 和 incidence I。若保管权比例 q、原 weighted-incidence 比例 p，则

    W'=qW,   I'=pI,   λ'=(p/q)λ,

归一概率 cap 至多要除以 q。将 marks 分到 resolution charts 是删 marks，不自动使每根余管保 λ；须依原 I 先 heavy，再记 p,q。平均 density≥λ 时，取逐管≥λ/2 的 labels 只保证 W'≥(λ/2)W 和保常数原 I；不能直接说原全部 labels 获逐管输入。反过来逐管全称 G4 真成立，才可在 ε/2、η 足小条件下吸这次权损得到平均版本。

§4 full marks 反攻 λ=1、p=q=1，所以 cap 失败不依赖任何平均/逐管转换。§5 的 r² 则是实体进 round envelope 后的真实 density，重新命名 λ 不能消去。

旧 full exact containment 由 FSD001 s=3 一次统一重调用覆盖；regular-leading 是 DIR4 的正幂双向改写；dim≤3 marked carrier、finite global-Lip pieces、fixed-format whole-containment 查询已在 R60/R87 覆盖。均不将本轮新 source 名称作为另一个数学方向。全 G4 本身的成功也不能自动成为 ordinary n5>4；R87 已核 HRZ 窄转线性、全 λ 与 coarse 重复等额外责任。

## 8. 决策、未付接口与本轮停止

本轮没有从 quantitative resolution / stratified rescaling 获得新的、可直接调用的全 physical R5 near-axis 输入。具体新信息是两项可证伪压力门：保直且 uniform biLip 的实际 blow-up 仍会把方向编码成 offset，和 coefficient-uniform exact analytic charts 的超指数退化计数障碍。第一项保原 unit axes/N/full marks；第二项仅反指定 analytic chart 升级，不冒充 δ-approximate carrier 反例。fixed-r C^r 的真正正面范围承认保留。

仍未付的是：允许非线性 charts 后，在同一原 family 上把变为位置的信息与剩余方向联合控制，并用实际 marks、真实 packet 尺度和 bounded overlap 返回原 W/α。这不是本轮从 source 提取的新定理，不能把它加成假设而称通过。仅给 resolution 加 Jacobian floor 或再调 r/D/leading 梯度不能越过 §4；下一轮也不沿这些参数续做。完整 G4 未证未反，ordinary n≥5/全 rough-mixed/真实同集全方向反例目标保持，Goal 不能由此完成。
