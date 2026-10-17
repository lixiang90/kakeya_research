# R0031：固定格式延拓与原 π 切片审计

2026-10-17，子任务 B。已读固定恢复入口、registry、R31 spec/上一轮次并执行 context.py。逐式读取 OAI4 §3.1 Lemma3.1–3.2（PDF26–29）、Cor3.4（PDF35–36），不重做 R30 已认证的 matching kernels。本稿只编辑被分配文件，未操作 Git。

**结论。** Lemma3.2 的 fixed-A 比较加固定格式 semialgebraic continuation 确可给 coefficient-independent A^C 损失；以下补足实际 endpoint branch/parity 与 norm supremum 的量词。Cor3.4 的 Fubini slice 保两色原 π，条件质量的分母必须支付。**Cor3.4 本身只调用 Lemma3.1、degree closure 和 Lemma3.3，不调用 Lemma3.2。** 后者是后续把比较传到共同 complex point 的独立责任，不能虚加到本轮主推论的依赖中。

## 1. 精确对象、输入和停止条件

固定 base dimension n、所有多项式 degrees、sheets 数 k、polynomial evaluations 的 degree、broken straight path 的 pieces 上界 S，以及 path 所在 bounded complex region。允许 affine functions、linear roots 和 constant-leading simple quadratic roots；每个 quadratic 的 constant c 可任意小但非零，c=0 时另归 linear case。沿 path 的 A⁻¹ tube 内，所有 linear denominators 和 quadratic discriminants 均不为零。A≥2。

取 endpoint comparison balls 半径 c₀/A，且其固定倍 enlargement 留在 tube 内。欲证每个允许 continued function H 的两 endpoint norms 双向比≤A^C，并有 fixed derivative 与 sufficiently-long finite jet 版本。C 仅依固定格式和 margins，不依 coefficients 的 height、最小非零 coefficient 或 unused roots。

标准基础输入为固定格式实 quantifier elimination、semialgebraic fiber/component bounds、one-variable semialgebraic functions 的 polynomial growth；以及 Lemma3.1 的 fixed-geometry coefficient-independent norm/jet comparison。本轮 A 负责独立核后者，本稿不以延拓反向证明它。若编码实际 branch 需不定长离散信息、或 fixed-A supremum 不有限，则原 3.2 此证明失败。下面逐项消除这两风险。

## 2. 固定 A 的有限 bound：只用局部简单性与 Lemma3.1

bounded region 加 S fixed 给 path 长度≤C_S。沿每 piece 用 O(A) 个 balls 覆盖，半径为固定 c/A，选择相邻 balls 有固定相对重叠、enlargements 留于 A⁻¹ tube。linear root 为 rational holomorphic branch；quadratic 的 nonzero constant leading coefficient 与 nonvanishing discriminant 使选定 root germ 在这些 simply-connected enlarged balls 上唯一 holomorphic continuation。

对 H 的 differences/polynomial evaluations，degree closure 给 bounded-degree polynomial relation。将每个局部配置 translate/rescale 至固定几何，Lemma3.1 比较邻 ball norms 的常数只依格式和相对 margins，**不依 coefficients 或 c⁻¹**。相邻 germs 在 overlap 上确实相同，因此连续 O(A) 次比较给

\[
\|H_{\rm end}\|\le C_0^{C_1A}\|H_{\rm start}\|. \tag{1}
\]

反向 path 给逆比较。若 start norm=0，H 在 start ball 恒零，identity theorem 沿该 analytic germ 链保持零；无需把零 denominator 纳入 ratio。即使 end ball 与 start ball 物理重合但发生 monodromy，逐段 continuation 的同一 germ 链仍是所比较对象。

(1) 只证明固定 A 的 supremum 有限、并在 A 的任意 compact interval 上有统一 finite bound；它**尚不是** polynomial A^C。下面利用的是该 supremum 的固定 semialgebraic format，不能把 O(A) 个 comparison balls 装入 format 后声称维数固定。

## 3. 真正的 endpoint continuation 编码

### 3.1 线性 root

线性 equation a(z)W+b(z)=0 在 tube 上 a≠0，其 root W=−b/a 单值。endpoint equation已确定实际 branch；无独立 sign 或 path history。affine functions 是更简单子类。

### 3.2 二次 root 的平方根变量

对 cW²+b(z)W+d(z)=0、c≠0，令

\[
\Delta(z)=b(z)^2-4cd(z),\qquad S(z)=2cW(z)+b(z).
\]

则 S²=Δ。记录起点 W 等价于记录起点非零 S，之后 W 由 2cW=S−b 确定。使用这个 polynomial identity 无需假 c 有下界，也不需要在 format 中显式引入巨大系数 c⁻¹。

沿一条 straight segment z(u)=(1−u)v₀+uv₁，u∈[0,1]，Δ(z(u)) 是 degree bounded 的复多项式 p(u)，且不为零。其连续 argument 导数为

\[
\frac{d}{du}\arg p(u)
 =\frac{\operatorname{Im}(p'(u)\overline{p(u)})}{|p(u)|^2}. \tag{2}
\]

numerator 为固定 degree 的实多项式。若不恒零，其 critical parameters 有固定个数；若恒零，则在 nonvanishing segment 上 argument 恒定。故可选一条从0出发的 generic ray，避开所有 vertices 的 Δ 值方向、所有 finitely many critical directions，并避开 constant-argument pieces 的方向及其反方向。

对 ray direction ζ、|ζ|=1，crossing 条件是

\[
\operatorname{Im}(\overline\zeta p(u))=0,
\qquad \operatorname{Re}(\overline\zeta p(u))>0.
\]

generic 选择使 crossing transverse。每 piece 的 crossing 数≤deg p；constant p 或 constant-argument piece 可取无 crossing。总数只依 fixed S/degrees。

取 η²=ζ、|η|=1。在不位于 cut ray 的 endpoint，Im(S/η)≠0，故给 root 贴 ± sign。continued S 经过 cut ray 一次，该 imaginary sign 恰翻转一次；没有 crossing 时保持。于是

\[
\operatorname{sgn}\operatorname{Im}(S_{\rm end}/\eta)
 =(-1)^{N_{\rm cross}}
   \operatorname{sgn}\operatorname{Im}(S_{\rm start}/\eta). \tag{3}
\]

这编码的是实际 continuation，不是独立挑 endpoint root。两种 η 只会把两端 signs 同时翻转，不改变 (3)。反平行、loop winding 和可能的 root swap 均已由 crossing parity 支付。

### 3.3 为什么 format 真正固定

把 complex variables 拆实虚部。可先将给定 bounded base region 放入一个固定 Euclidean ball，并对这个较大 ball 中的 paths 取 upper supremum；这样不必额外假设原 region 自身 semialgebraic，§2 的 path 长度/固定-A bound 对扩大类仍成立。coefficients、≤S+1 vertices、start/end root values、generic ray ζ 和其 η，均为固定个数 real parameters。crossings 可用固定最大个数的 ordered u₁,…,u_B 加 finite flags 编码；用 universal real quantifier 声明所有合法 ray intersections 均在这个列表中，并要求 transversality。parity 只有固定有限种情况，可写 finite union。

tube nonvanishing 写成：对每 piece 的 u∈[0,1] 与所有 displacement h，若 A²|h|²<1，则 linear coefficient/discriminant 在 z(u)+h 不为零。度数和变量数固定，只有 A 进入 coefficients。实际简单 root 由 start value 与 (3) 选择；未对每个 step 引入 O(A) 个 branch variables。

若有 finitely many quadratic sheets，可对它们分别选 ray，或统一选避开有限坏方向的 ray，均为固定格式。不同 sheets 的 coefficient degenerations 也只在有限 case splits 中处理。

## 4. Endpoint norm supremum 与 polynomial growth

要在 endpoint ball 的 variable point z 求 H，append 一条从 endpoint center 到 z 的 straight segment。其长度≤c₀/A，位于原 endpoint tube 内；新增 piece 数仅1。用 §3 相同编码从 chosen center germ 取正确 root values，再作允许 polynomial evaluation。start norm 也可用 start center到variable point 的一段编码。

norm inequality “对 ball 上全部点，|H|≤T”因此是固定格式 real first-order formula；closed real ball、parallel real slice ball 或 complex ball 均可用多项式 inequalities 表达。固定 c₀/margins 使函数在所用 ball 的 neighborhood holomorphic，norm 有限，球内 branch 唯一。对另一方向的 ratio 同理。

令 R(A) 为所有 admissible coefficient/path/root data 中、start norm>0 时的 endpoint/start norm ratio supremum。用上述 universal inequalities 表达 upper bound，再以 least-upper-bound quantifiers 表达 supremum，real quantifier elimination 给 R(A) 为一元 semialgebraic function。supremum 不必 attained，定义性不依赖 attainment。

§2 给 R(A) finite 且 locally bounded。one-variable semialgebraic polynomial-growth theorem于是给 R(A)≤C A^{C'}；A≥2 可把固定前因子 C 吸入 A 的更高固定幂。反向 path 给双向

\[
A^{-C}\|H_{\rm start}\|
 \le\|H_{\rm end}\|\le A^C\|H_{\rm start}\|. \tag{4}
\]

因此原 Lemma3.2 的 coefficient-independent A^C 结论成立。半代数步骤仅用于 norm ratio 的 uniform A growth；没有让 (1) 的指数 O(A) 直接变成固定格式。

## 5. Derivatives、finite jets 与退化测试

endpoint balls 的 radius≈A⁻¹。translate/scale 后用 Lemma3.1，在固定较小/较大 comparison balls 的 margins 下，fixed q 阶 derivatives 费用至多 A^q；足够长 scaled finite jet 控 norm，jet order只依 bounded algebraic degree。恢复 physical derivatives并结合 (4) 仍是 A^{C_q}。不需将 derivative 自身误说成原列表独立 branch。

退化测试：cW²+zW+1、c→0 时未选 roots可趋无穷，但 §2 比较的是已选择且连续的 holomorphic germ，不以所有 roots 的最大值控制它。以 c>0 为例，两个 branch points ±2√c 距离若小于2/A，则其 forbidden A⁻¹ neighborhoods 连通；closed admissible path 不能分开它们的 winding numbers，所以不会仅绕一个而偷偷换到 escaping branch。一般情形由固定-A bound和实际 parity 编码共同处理，不要求这一示例覆盖所有 equations。

反例若把 pole/branch point移入 prescribed tube、令 endpoint ball无固定相对 margin、或允许格式/degree随 A 增长，均不满足本 lemma。norm zero 情形由 identity theorem单独处理，不能用 ratio除零。这些是本审查保留的真条件。

## 6. Cor3.4 的真实依赖：不用3.2

原 Cor3.4 proof 依次做：取 actual list member f_* 作 reference；减 f_* 并除 M；用 degree closure 和 Lemma3.1 给 fixed derivative upper/每点 norm-to-finite-jet lower；有限 order/direction/box selection；Fubini slice；套 Lemma3.3。

所有 sheets 已在同一 fixed holomorphic domain/margins上，比较都在其中进行，没有沿复杂 path 改变 germ。因此 Lemma3.2 **不是此 proof 的必要输入**。它服务后续 Lemma3.5 将已得 local comparisons 继续到 common complex point，并以 endpoint jets作 labels。本轮认证3.2应独立登记 source tool，不能虚称 Cor3.4 因而需要新增路径假设。

取 actual f_* 也避免外部 common reference 的 degree 或 holomorphic domain 被默许；triangle inequality保每 member normalized norm≤2R^ε，reference 自身有已固定 degree。此部分的完整 norm-to-jet 由 root/A 主稿给出。

## 7. 原 pair law 的 density 及固定 product boxes

设原 subprobability measure μ(i,j,dz) 的 total mass≥R⁻ε，两色分别满足 marginal≤R^ε π_{κ,i}dz。finite indices 下可写非负 joint densities p_{ij}(z)，因为每个 pair law由相应 index marginal支配而对 Lebesgue 绝对连续。对几乎处处 z，同时有

\[
\sum_jp_{ij}(z)\le R^\varepsilon\pi_{1,i},\qquad
\sum_ip_{ij}(z)\le R^\varepsilon\pi_{2,j}. \tag{5}
\]

每个 R 的 lists 都有限，所以所有 indices/colors 的 exceptional null sets可同时取并集。先按 positive-order directional derivative gap和有限 fixed product boxes作 measurable restriction，只会降低这些 densities，不需归一化。

为覆盖 comparison ball 中可能集中于 boundary collar 的 event mass，product boxes允许略伸出该 real ball，只须连同固定 complex enlargement 位于原 holomorphic margin内。不能要求有限个 boxes 全紧含于 real ball 后声称覆盖了靠边界的全部 mass。real boundary本身虽为零 measure，随 R 变薄的 collar可承载全部 R⁻ε mass，故这一点不是靠忽略 null boundary解决的。

选中的 order/direction/box 只有固定个数，保 mass≥cR⁻ε（或把此前固定数 losses统写为 R^{-Cε}）。取正交坐标 z=y+tv，t∈I、y∈U⊂v^⊥，I、U和holomorphic fiber margins皆 fixed。正交 Jacobian=1；其他 fixed affine coordinates也只付固定常数。事件仍可在 (i,j,y,t) 上高度相关。

## 8. Fubini slice 保两色原 π，先取 mass 后归一化

写 restricted densities p'_{ij}(y,t)。对几乎每个 y，(5) 同时对所有 indices 和几乎每个 t 成立。定义未经归一化的 slice measure

\[
\mu_y(i,j,dt)=p'_{ij}(y,t)\,dt,\qquad
m(y)=\sum_{i,j}\int_Ip'_{ij}(y,t)\,dt.
\]

Fubini 给 ∫_U m(y)dy≥cR⁻ε。存在同处上述 full-measure good set 的 y，使 m(y)≥cR⁻ε/(2|U|)>0；取 factor2可确保 high-mass fibers 为正测度，而非试图在一个 exceptional maximizing fiber 上取值。n=1 时没有 transverse variable，直接用原 interval law。

在这个实际 y 上，slice 的两 index–time marginals仍为

\[
\mu_{y,\kappa}(i,dt)\le R^\varepsilon\pi_{\kappa,i}\,dt. \tag{6}
\]

归一化 P_y=μ_y/m(y) 后，才支付分母：

\[
P_{y,\kappa}(i,dt)
 \le \frac{R^\varepsilon}{m(y)}\pi_{\kappa,i}\,dt
 \le C R^{2\varepsilon}\pi_{\kappa,i}\,dt. \tag{7}
\]

若先前统写 Cε losses，只把 2ε换成固定 C′ε。π 仍是两色各自原 probability weights，允许绝小权或零权；不对仍出现的 indices 免费重归一化 π。slice mass 不必≤1，只有其 lower用于 (7)，upper 由 (6) 自动有限。

将 fixed I affine rescale到[0,1]，time density及各 fixed directional derivatives只变固定 factors。pair仍来自同一 common basepoint的同一 y，不引入独立 i、j、t。selected positive derivative lower仍在每个保留 event上有效，函数在整个 fiber interval的高阶 upper由 fixed holomorphic margins保证。故 TCM001 的两 marginal 假设与相关events量词完全对准。

## 9. 不能免费使用的替代说法与验收

- “条件于 basepoint 后 π 仍是先验”并非证明；正确步骤是 joint densities、有限 indices同时 a.e.、选正 mass fiber，再除该 mass。
- 仅有 t 的 total marginal upper不够推出每个 index–time upper；本稿逐色使用 (5)。原 law可有任意 pair/time 相关，不假 product。
- tiny π不产生额外分母，归一化费用是整 fiber mass；若另筛 indices并重设 π，需另证明，不在本稿实施。
- Cor3.4 不需要3.2；3.2 的 A^C也不认证3.5 labels/knowledge/temperedness的其余步骤。

在 Lemma3.1 本轮独审及标准 fixed-format semialgebraic 基础下，原3.2与Cor3.4的slicing接口已逐式完成，无合法 counter。最终 Cor3.4全loss/degree/TCM对接仍由root主稿与独审合并；整篇OAI4、无条件DIM001、新颖性与长期高维Goal尚未认证。
