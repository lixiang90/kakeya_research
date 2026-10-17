# R0031 独审：Cor3.4 的真实 norm/π 接口及 fixed-format 延拓

2026-10-17，审查者 `audit_four_dimensional`。审 root `R0031_scalar_sheet_matching_full_proof.md` 与 B `R0031_continuation_and_slice_audit.md`。本审查者是 Lemma3.1 norm 主稿作者，故对自己的 norm 证明不计第二独立证明；该稿由 root/B 另核。本 review 独立核 root 的 Cor3.4 合成、resultant/量词/反攻及 B 的 Lemma3.2 延拓。

**结论：数学链通过内部审查，可按本稿所列源基础与 scope 归档。** 初稿两处范围措辞已修：root Ω 保持同一 connected ball/polydisc；margin 删除测试改为保圆盘形状的单极点模型。两修正均不改变 Cor3.4 主证明。未认证整篇 OAI4、无条件高维界或重大性/新颖性，未经外部同行评审。

## 1. difference resultant 的非零性和 total degree

对在 chosen sheets 上恒零的 irreducible P/Q，各 total degree≤D，且均含 W。root 取

    Res_W(P(z,W),Q(z,W−T))。

在 generic z（两 leading coefficients 非零）处，roots α/β 的 product 表达给其 T-roots 为 α−β。因此它确实是 u−v 的 relation，并非 u+v 或反号；作为 T polynomial 非零。Sylvester matrix size≤deg_WP+deg_WQ≤2D。

Q(z,W−T) 的每个 W-coefficient 是 z/T polynomial，total degree≤D；P 的 entries 亦≤D。所以 determinant total degree≤2D²，清楚包含 base z 与 T，不只是 W-degree。generic 开集上的 relation 由 holomorphic identity 延至 Ω。tiny leading coefficients、unused factors、乘 M 改变量 T→MT 均不增加这个 degree，也不引入 height lower。

减 f_* 后 h_i 和 pair difference g_ij 分别直接是两个**原** sheets 的差；g_ij 无需从 h_i 再作一次 degree 膨胀。root 统一取 D'=max(1,2D²) 合法。

## 2. 固定 domain、norm-to-each-point jet 和有限方向

root 最新 §1 明定 B/Q 在同一 connected Ω（ball/polydisc）中，有限 product boxes 只是 Ω 内的覆盖，未引入独立分量。若允许 disconnected union，B 上 normalization 无法约束另一个分量选出的 branch，因此这项收紧是必要的范围澄清。

以实际 list member f_* 作 reference 保同一 degree/domain；三角不等式给 `||h_i||_B≤2R^ε`，不假额外 common reference 有未列的较低 degree。Lemma3.1 齐次 upper 给所有所需 fixed derivatives；每个 incident pair 的 norm≥R^-ε 则在每个 incident point 给≤D' jet lower。root 没有把“某处大 jet”误当“每点大 jet”。

对 ε≤1/4，`R^-1+ε` 与 `cR^-ε` 的 ratio≤c^-1R^-1/2；固定 R₀ 可在所有这些 ε 同时排除 zeroth order。real-on-real 保 diagonal real derivatives 为实；有限维 homogeneous polynomial evaluation 给 fixed finite real directions 与 orders。按第一满足的候选作 measurable partition，再作 finite pigeonhole，质量只损固定 factor，不依 indices、π 或 R。

Cor3.4 这里仅需 Lemma3.1 的 norm/jet 与 difference closure。Remez、affine-line relation specialization 及 Lemma3.2 continuation 不是额外隐含输入；特别没有为了切到一条实直线而先调用一个未付的复杂 path comparison。

## 3. boundary cover 和原 π 的 Fubini

Q compactly 位于 Ω，故对每个 fixed direction 可用有限 fixed-size product boxes 覆盖 Q，并使其 complex enlargements 仍在 Ω。盒可伸出 B/Q，μ 在原 Q 外延为零。若只取紧含于 real ball 内的有限盒，会漏随 R 集中的 boundary collar；root 已采用正确外伸 cover。

每个 pair component measure≤其某个 index marginal，故对 dz 绝对连续。finite indices 下可取所有 a_ij densities，并同时令两色 row/column sums 的 upper 在 a.e. z 成立。先取 finite null-set union，再 Fubini，保证 a.e. transverse fiber 上全部 marginals 及 event conditions 同时成立。

restricted mass≥cR^-ε，transverse X 的 volume fixed，因此存在处于 full-measure good set 的 fiber，未经归一化 mass `m(x)≥c'R^-ε`。使用 factor 2 的 threshold 可使候选 good fibers 为正测度，不能只在可能 exceptional 的最大点取值。n=1 的横向空间按单点处理。

只有此时才除以 m(x)，得到两色 `≤CR^{2ε}π_i ds`。π 是同一个原 probability vector；没有改成条件 π，也不需要 minimum positive π lower。pair/time 相关性没有被拆成 product。slice mass 可以大于 1，但它 finite 且有正 lower，正规化仍为 probability，故不影响这一步。

## 4. ε→0 时 R₀ 的统一性与 TCM001

固定 fiber length ℓ 与 boxes/margins，使 rescaled H_i 在整个 unit interval 上各 fixed derivatives≤C_*R^ε；positive-order gap≥cℓ^pR^-ε；两边缘≤C_*R^{2ε}π_i dt。统一 `K_R=C'R^{2ε}` 支付 value、gap、derivatives 与 marginals。

root 先取 `d₁=(1+d₀)/2` 和 TCM001 对 fixed D'/J/d₁ 的 tolerance η，再取

    ε_*≤min(1/4,(d₁−d₀)/2,η/4)。

最后选固定 R₀ 使 `C'≤R₀^{η/2}`，可对所有 `0<ε≤ε_*` 同时得 K_R≤R^η。常数是吸进**预选 η/2**，不是吸进趋零的 ε。card≤R^{d₀+ε}≤R^{d₁}，因此 TCM001 的 fixed-power 量词完全对准；R₀ 不会在 ε↓0 时隐含发散。

R=M/Δ 可为任意大 real；TCM001 本身的 N→∞ 不要求整数。即使另取相邻整数，也只是固定 ratio 预算。此合成一般 fixed dimension/degree，不是单个 fiber 或只 uniform indices 的特例。

## 5. root 两项假设删除测试的终稿

degree 删除例 `f₂=z^k`、k=ceil(2log₂R)，在 B=[0,1] norm1、fixed Ω 全纯；event [0,1/2] 的 normalized density2 保全部双 marginals和 small values，惟 total algebraic degree 无 fixed bound。各条件均实际核算。

margin 删除例终稿取 B=[0,1]、a=R^-2、`f₂=a/(1+a−z)`、`Ω_a={|z|<1+a/2}`、event [0,1/2] density2。relation total degree2，pole 1+a 在 Ω_a 外，norm_B=1，event values≤2a；B 到 complex boundary 的 margin 为 a/2→0。它保 spherical domain 形状、fixed B/degree、real-on-real 与其余原 law，仅失 uniform margin。

旧对称 poles±ia 模型虽能在 shrinking tube 邻域全纯，却没有单独保一个包含 B 的 disk/polydisc；本次替换消除了这个额外范围差异。终稿是严格假设删除测试，不是原 Cor3.4 counter。

## 6. B Lemma3.2：fixed A 的比较与实际 branch parity

固定 A 时，bounded path region/固定 piece 数给总长度 fixed upper；用 O(A) 个半径 c/A balls 串接。linear denominators 与 quadratic discriminants 在 tube 不零，故每个 enlarged ball 的 chosen germ 全纯。Lemma3.1 在 rescaled fixed geometry 上的 norm comparison independent of coefficients，连续 overlaps 上确为同一 germ，得 C₀^{C₁A} 双向 bound。start norm=0 则 analytic continuation 恒零，ratio 只对正 start norm 取。

对 `cW²+bW+d=0`、constant c≠0，S=2cW+b 满足 S²=disc。straight segment 上 p(u)=disc(z(u)) 是 fixed-degree nonzero complex polynomial。argument derivative numerator `Im(p'conj p)` 是 fixed-degree real polynomial；若不恒零只有固定多个 critical parameters，若恒零则 argument constant。generic ray 可避 vertices、critical values 和 constant directions。

正 ray crossing 由 `Im(conjζ p)=0, Re(conjζ p)>0` 记录；generic choice 保 transversal，每 piece 至多 deg p 次。取 η²=ζ，端点 `Im(S/η)` 非零；经过 cut ray时该 sign 恰翻一次，故 crossing parity 精确选择 endpoint branch。ray 的反向 intersections 不算 crossing，η 的两选择只同时翻两端 labels。loops/monodromy 未被忽略。

finite crossing list、ordered parameters、universal “无其它 crossings” 以及 parity finite flags 全是 fixed-dimensional real formulas。tube nonvanishing 也只需 quantifier 在 piece parameter 与 displacement 上；没有把 O(A) 个 balls 编入 format。因此系数很小、root values 很大都只是实参数值，不能造成 format 的增长。

## 7. norm supremum 的固定格式及 polynomial A-growth

在 endpoint ball 的 variable point求值，可从已选 center germ append 一条 straight segment；其 complex enlargement 在 tube 中，piece 数仅加1。正确 branches 仍由上一节的 parity relation 选择。于是 norm upper 用“对 ball 内全部点”及正确 root relation 描述；real balls、complex balls、parallel real slice balls 都有 polynomial inequalities。若原 bounded path region 非 semialgebraic，可先扩大为一个 fixed Euclidean ball，再对这个更大的 admissible class 取 upper supremum；B 终稿已补这一点，避免虚加 region 形状假设。

正 start norm、两 endpoint norms、其 ratio 和 least upper bound 均可用 fixed real first-order formulas 描述。real quantifier elimination 后，R(A) 是一元 semialgebraic function；sup 不必 attained。fixed-A comparison 给其 finite/local bounded，而非直接给 A^C。

最后的 polynomial growth 也可具体看作：对足够大 A，semialgebraic graph 的有限 cells 受某非零 polynomial Q(A,T)=0 约束（否则只有 strict inequalities 会给二维 interior，不能是 function graph）。最高非零 T-coefficient 是非零 A-polynomial，在大 A 处有 polynomial lower，其余 coefficients 有 polynomial upper；基本 root bound 给 |R(A)|≤CA^C。有限 A 区间由前述 local bound 补齐，再因 A≥2 吸固定前因子。这里仍以标准 fixed-format QE/cell facts 为基础，不声称重证全部实代数几何基础理论。

反向 path 给 inverse ratio；endpoint radius≈A^-1 下的 Cauchy/finite jets 用对应 scaled derivatives，恢复 physical derivatives只付 fixed A powers。tiny quadratic coefficient 不引入额外 c^-1 height 条件。B 的3.2证明因此通过；它独立于本轮 Cor3.4 的实际依赖链。

## 8. 最终范围

root 主 Cor3.4 的 degree/reference、每点 norm→jet、finite real direction/边界 cover、真实两π slice、全部 fixed losses 与 ε/R₀ 次序均已核。B 的 fixed-format continuation 也经逐式审查，但其标准 QE 基础仍作为明确 foundational input，不以一次 norm lemma 当整篇认证。

可归档为原 source gateways 的内部重证；来源已有结果，未经外部同行评审。Lemma3.5 的真正 terminal atlas/knowledge 回传、critical paths 和所有后续高级排除仍未认证，SRC/DIR/FSD/DIM 的完整 OAI4 条件未清空。无无条件高维新界或重大性/新颖性声明。到此停止本子任务编辑。
