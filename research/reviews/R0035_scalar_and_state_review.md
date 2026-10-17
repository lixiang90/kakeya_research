# R0035：完整 isotropic 引擎的独立 scalar/state 审查

2026-10-17。审查者为负责 scalar/qualification 的独立代理。已实际读 root 完整 `notes/10_source_audit/isotropic/R0035_isotropic_candidate_full_proof.md` §§1–18、另一代理 `R0035_conservativity_potential_and_degree_audit.md` 全稿，以及原 PDF 页70–108/提取3735–5799行的相关算式。自己的前半部稿只作交叉接口，不把自审计为独立审查；本 review 对 root 全稿和 B 的后半部逐项独立检查。

**最终判定：修补后通过，可作为原 Theorem6.1/Cor6.9 在列出的具名高级输入下的内部复现归档。** 未发现保原全部假设的反例或剩余未付前后半接口。这里的“通过”不认证外部高级输入的完整证明、不认证整篇四维论文，不产生无条件五维/一般维数结论，也不认证新颖性/重大性。未经外部同行评审。

## 1. 两项已修补责任与一个提取误读

1. **raw density 与 product-prior labels。** B 独立指出，`λ≤Kν°dt` 只给 label 质量下界，不能把 λ 的 spatial upper 直接传成 ν° 标签 upper。root §2 已补：原 indicator-normalized path 在 support 上 density≥1可直接用；若只假 0≤σ≤K，删 σ<σ_N 的 events，其原 parent mixture 总损失≤σ_N，因为Σp_γν_γ°≤1。选 σ_N^{-1} subpower 大于所有 entering inverse-densities，并在有限步骤预算后慢对角。boolean restrictions 保同 σ；若另产生更小 fractional density，使用前重新 trim。于是 `σ_Nν°1_Edt≤λ_E≤Kν°1_Edt`。root §9 用 lower 比较转 caps、用 upper 比较得 dense labels，方向正确。此补证由 B 首先提出、root/本代理各自核过，不是原 counter。
2. **全 row qualification。** 本 review 指出5.6直接只拟合 F_q≈G_y。root §9末已显式补同 indexed line 上 `G0=X′−GyV+O(b^κ)`，V 常值、X′ degree1、coeff≤K，因 M≥2，整个 `(G0,Gy)` 仍 degree≤M、coeff≤K、error Kh^{M+1/4}。whole Q_s assignment 保持同 h-block。不能省略这步后把 Gy 资格称全 row 资格。
3. **Cartesian inverse。** 纯文本5220行曾被本代理误读成 A0u；B 核原 PDF 页97后，本代理用 `pdftotext -bbox` 交叉核上标“−1”位于 x400.465/y466.715，下标0另在 y474.763，原式确是 A0^{-1}u。root/两子稿均已明确这只是提取排版，不是源错误。root §10还按本代理建议显式取 `Kξ≪ε_T`；仅 `Khξ≪a1` 不蕴含前者，预声明 all-evaluations mesh 可同时满足。

## 2. 命题、量词与高级输入

root §1 的范围准确：原4.7 tangent、j1/v1 或 j2/v2且ℓ=0、0<k≤1、d<1；任意 substantial residual 可在 further subsequence 找固定正 bounded s、a=N^{-s}、h∼a^k、a2=a h^{e2}，e2>0固定，计数 incidence≥hν_Q(a2/a)^d/K。ν_Q 是完整 assigned prior，非当前发现族质量。proper quadratic 的 whole 同 h-block upper、counted derivative lower、constant curvature上界分开，gain=e2ks正有限才接 AIM。

独立核两项新增 primary 的 statement：

- Wang–Zahl [2210.09581v2](https://arxiv.org/abs/2210.09581v2) Def4.2（页17）只有每球/每中间尺度的 covering upper。Thm5.2（页31）及§8重述（页49）允许**任意 restricted triple set** H⊂F×G×G 满足 E_δ(H)≥δ^{η−3}。无 AD lower 被遗漏；其 expansion 是某 interval/scale 上的 covering exponent1−ε，恰是原5.5所需。A alternative 的第二线过原点比本应用更强，但这里只用第一线集中。v2日期/刊物由 root 归档核对；此 review 没有重证其§8 radial/Bourgain高级证明。
- Carbery–Valdimarsson [1205.6371v1](https://arxiv.org/abs/1205.6371v1) Thm1（页2）含正权重、双向无限1-tubes及 wedge determinant 因子。本应用取 multilinearity=ambient n，缩放得 r^n；n=2,3,4。bounded region 的有限测度直线族可先圆整参数、扩大半径、对有限 sums 用 theorem，再取极限；passing determinant bounds以常数 buffer稳定。未把 quadratic curves直接当直线套定理。高级 theorem 本身仍 named。

GWZ2026 set input及由其支付的2.15仍沿用 CRP 的原条件证书，不偷换成已全审 maximal theorem。

## 3. Cor4.13、5.1–5.4：原状态与原权重

root §3 的 unit normal/offset≤K 归一化、重 palette strips 计数及 original label-map realization 均符合原70–71页。κ,u先固定，breadth只在 substantial 残余上准备；whole-state或状态内小固定比例删选可保留，任意 inverse-subpower 速度子族不可。后续多次 renewal 均发生在可重新准备的 substantial reference/failure law 上；strip filling之后不再追认新 breadth。

§4 scalar coefficient clustering 的 D-lift 确实把二次 X变成二维 affine base projection。plank质量 lower `p^{d−1}uv/K` 与 upper `Kuv^d` 比较得v≤Kp，再除独立 D接受长度u而得到原 scalar p-bin floor。没有要求 coefficient prior 的 AD lower。

§5 entropy 已独立重算：对任意新 dense tested event A，T为独立预采的 whole tuple，`E_Q log1/P(A|T,B)≤log1/P(A)`，不支付 #B或minν(B)。参数块条件 cap和 scalar local cover给 MI=o(logN)；T-known unit row薄片计数给投影 entropy exponent1。所有 discrepancy events 上须重新调用这套计算，root 已逐次注明，没有 conditioning-MI错误。

§6 first jet 局部点积只得到少量 fit times时，root确实先付 instantaneous m(t) floor/好 H-block数；保留的是 pre-quadrant T_J的真实活动集，然后恢复这些时间的所有 prepared labels，故 global density lower不是临时 slice 的成功概率。normalization只平移 B不平移 A，保 dot product；upper-AD graphs与 restricted triples count对准5.5。相邻 fits用预删除共同 µ_fit 的 child mass选择两个 separated见证，后删不需再饱和旧floor。close/far residual-slope collision两项分别为 `Kp0^dN^{-c/2}` 与 `Kp0^{1−γ}`，γ=(1−d)/4使后者确为o(p0^d)。

## 4. Higher jets 与 fixed reference qualification

root §7 finite tree 在labels前独立于trajectory，单时密度的固定次幂保全部 tested labels；近时间差删除按原 experiment probability收费。rows只依world/tree、不依trajectory/t′，所以投影 entropy的 unit row确为T-known。H_i schedule保证所有 divided-difference读取在 floor以上，并留出strict powers；final t′ discrepancy 用 |E|r≥h^{M+1/2}、r=h^{1/4}，正好合法。

最终 witness回收先冻结(l,tree)再用t′原h-block均匀法则，不在成功条件下重称均匀；light-fiber删除后输出包含 counted t′的 h/K-long actual labels。该结论只是每dense输入中能发现dense合格族。

root §8–9补足升级：ν°一次冻结、原(6.6)先验 bin floors不追认为当前incidence floor；coefficient-world q=(parent,B_ρ)的分子/分母使用同一个 π、同一个ν°。moving zoomcell 的时间宽s′在 numerator和entry floor两边都出现，没有多丢β/s′。残余列表去velocity条件另删 light E，费用 K_pre³/K_cut；conditional palette π(J)/π(I)来自真实新分母，E不变成新增world。Lemma6.4一scale一world费用，与cells/world总数无关。

Prop6.3固定 ε失败若占reference正比例，即为 substantial residual；在那里重新做准备，但保持G与meshes冻结。得到任何正质量的真正资格点便反其“全失败”定义；不需发现族与原失败族有常数相对质量。最后ε=1/r慢对角才给relative o(1)，不传给任意稀疏子族。经§1双density比较及全row recovery补丁，该逻辑闭合。

## 5. Cartesian 状态恢复与真实 descendant计数

root §10 先从relative qualification误差删除 failure proportion>η的**整个状态**，成本≤e_NL_ref/η；η固定小于spanning probability/(2m)，所以 simultaneous qualified basis事件仍常数概率。原prepared edges都在，不把稀疏qualified subfamily冒充broad。

palette averaging先固定parent，其π共同；每state eligible tuple palette质量≥1/K，于是存在同一tuple支撑 hν_Q/K状态质量。正确坐标 r=A0^{-1}u，共同 velocities变成各坐标 fibers。fiber fits的coeff-bin上界通过对每represented bin选一个long witness、用同一 M+1 uniform separated-times实验求和概率证明，不假各 witness 独立。

每fiber/每cell的随机列表选择只固定数量 m+1 个tests；用 cell floors+base ceiling把 mass转Cartesian计数。逐轴Jensen给完整(M+2)^m顶点，不是只拥有各轴线段；anchors过近先作原probability预算，再固定anchors与dense targets。tensor插值误差 Kε_T是state property，故可恢复整个所选state的prepared边。长线 polynomial Remez只延至当前 h-block。

(I2)另用真实 descendants a_i的 full prior lower与disjoint whole assignments计数。`(h/h_i)·ν_Q/(a_i^d h_i^j)·(h_i/(hξ))^{j+1}=ξ^{-m}ν_Q/(a_i^d h^j)`，h_i恰抵消；不是当前稀疏子族自带的新floor。ξ预细到hξ≪h_i，各图支撑来自之前完整准备。此接口与B后半完全一致。

## 6. B 后半与 root §§11–16 的独立核验

**换线/换时。** 两个 heat-bath分别保持同一P；先以总ν_Q预算删除短线choices，再保未归一good kernel。其上界为 `Kπ(J)dt/h`，backward integration合法支配product reference。good path中不声称条件独立。signed increments变换三角、Jacobian1；同W_b换线的physical误差Kb无需native w绝对有界。

**conservativity。** 两个m方向bases的cross Hessian确为 DT(u0)[v_i]·v_j；若所有 maximal minors小，则对首半变量求导、反演两basis，使skew DT小。只对passing nonzero-Jacobian fibers用固定次数regular isolated multiplicity，不声称整个algebraic fiber有限。面积公式保完整 `ξ^m(a1/h)` cell体积；乘(I2)后正是 `K h^{e1(1−d)−c0}=Kh^{c0}→0`，与正成功概率矛盾。start height仅平移endpoint cell，不影响数目。

**势函数/组质量。** P径向积分误差只含skew，∇P−hT≤Ka h^{c0}，X−P沿同block变化小于a2。组base cap≤Khν_Q(a2/a)^d，不能从任意C限制继承breadth。root/B的两次short-line/state删除、只保fixed-fraction C、最后group损失控制，使每组原prior≤KM/h来自最近long witnesses。CV填满base cells再用(I2)控制组数，得到目标 heavy floor；不是单用当前组mass假新AD lower。

**tensor/conic。** 七个R³ projective points每三独立给唯一非奇异conic；二拷贝cubic injectivity与三拷贝rank3/4/5核 q·Lin、Rq²、0的Euler/整除证明独立核过。rank4只在exact-conic constant-rank family取逆；approximate real conic先付det lower、再由Euler得spatial gradient lower，真实IVT修到首坐标1的实零，未偷换复零。

**native branch/degree。** discriminant与w无关，positive lower和real-volume floor付zero-free complex margin。tiny native curvature不以farroot或1/curvature作无界输出。R=P_s(z,f)/a的绝对导数K界先于conic shift，使用原long witness exact quadratic Taylor及无coefficient-height-lower的ASM。f只作relative S0 derivative界，mesh误差按KS0收费，预选δ≤h²/K独立S0；所以SCL所指出的绝对幅度缺口未被偷渡。

大S0时q lower来自distance-to-affine定义，real-conic修复位移Kh对R的误差Kh≪a2/a。exact kernels恢复 `R2+qL1+λq²`，把q替成H′=(w−L′)/S0，括号内**全部乘a**，得到总degree2。derivative扰动≤Ka/S0<Kh^{1−e2}，curvature≤K/a+Ka/S0²≤K/a2；不需w、L′、S0绝对上界。小S0与v1分支均由cubic derivative控制取二次Taylor。

最后每条实际trajectory上的value为time二次、hidden derivative为time一次，已有ordinary h/K witnesses。仅同一h-block的Remez给whole-block upper；counted lower及constant curvature另证，质量不再丢固定幂。此为完整候选，不是只有jet工具通过。

## 7. 归档边界

root §17的 residual全称闭合与AIM量词一致，Cor6.9仅原scalar模型的H=0。原正有限/无限窄分支、完整2.17 finite读出、KT advanced proof以及全部高维目标未由本轮完成。新登记应保 `full_source=false`、`high_dimensional_unconditional=false`、`major_or_novel=false`，具名 inputs逐项列出。R36按约先macro，不因本轮完整一个源分支便自动逐节续审。

本 review 对修补提出者身份如实注明：Gwt lower比较来自B，full-row/ξ接口由本代理指出，root整合；这些补证不冒称对自己稿的独立审查。原PDF inverse误读已撤销，无合法原反例。审查完成后停止编辑，交root统一验证/同步。
