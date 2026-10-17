# R0031 独审：代数 norm/jet 与原 π 的 Cor3.4 对接

2026-10-17，审查者 `/root/lifting_obstructions`。独立实读 root `R0031_scalar_sheet_matching_full_proof.md` 最新版（含保圆盘域的单 pole margin test）、A `R0031_algebraic_norm_audit.md` 全稿，并对照原 Lemma3.1/Cor3.4。本人 continuation/slice 主稿不是此独审的自我认证依据。

**结论：A 的固定几何、无 coefficient-height 下界 Lemma3.1 证明及 root 的完整 Cor3.4 对接通过本次内部独审。** tiny/escaping branches、bounded-degree closure、每 incident point 的 finite jet、有限方向/边界 boxes、双边缘 Fubini、slice mass 分母与 R₀ 对 ε 的统一性均已支付。原双 pole margin test 的圆盘域责任已由作者按建议修为单 pole，最新版通过。未经外部同行评审，不认证整篇 OAI4、无条件 DIM001 或新颖性。

## 1. A 的 normal-family 证明不循环

normalized relations 的 coefficient unit vectors 有 subsequential nonzero limit P。若 P 不含 W，B 上 chosen functions 的 |fν|≤1 足以直接推出 P(x)=0；real ball 的实开 interior 使 polynomial 恒零，矛盾。这一步并未预先假 complex local boundedness。

令 a_m 为 P 的最高非零 W coefficient。Ω\{a_m=0} 的 compact 上，可选足够大 root-free circle |W|=R，Pν 在该 circle 上也最终 root-free，即使其额外高次 roots 逃向无穷。取 p∈int(B) 且 a_m(p)≠0，chosen fν(p) 在 circle 内。沿 complement 中 compact path 和小 neighbourhood 连续传播，只追 chosen root，未以所有 Pν roots 的 uniform bound 作错误推论。

Ω 为 ball/polydisc 时 complement path-connected 的直线/有限零点 detour 证明合法：p 处 a_m≠0 使 complex-line restriction 不为零 polynomial，compact real segment距 Ω boundary 正，small detours仍留在 Ω。目标 neighbourhood可放入同一 connected compact tube。

跨 a_m=0 时，选一条 a_m restriction 非零的 complex direction 和 boundary避零的小 disk，再作**全维** small translates。全部 translated boundary circles 的并为 compact subset Ω\Z；已得 uniform bound后，每个平移 disk 的 maximum principle 控其 center。因此得到整个 neighbourhood 的 bound，而非只在一根 complex line 上有界。

若原 family 在 fixed K 上无 uniform bound，选一条发散 sequence，以上 coefficient subsequence推导给其 compact upper，矛盾。中间 circles/paths 可以依 limit P，最终反证仍给全 family uniform 常数，不需要显式 height lower。

## 2. Cauchy、finite jet 和每点下界

先在 K 的 fixed compact neighbourhood取 norm upper，再 Cauchy，得到任意 fixed q 的 derivative upper。compact exhaustion/Arzelà–Ascoli 加 Cauchy integrals 给 holomorphic compact limit和 fixed derivatives convergence。

limit 保 ∥f∥_B=1，故非零。对 P约去最大 W 整体因子，Q(z,f)=0 先在 f≠0 开集成立，再由 connected-domain identity 延至全域。Q 的 constant coefficient b₀(z) 非零；若 f 在某点有 order h，b₀=−Σ_{k≥1}b_kf^k有 order≥h，所以 h≤deg b₀≤D。对 violating points zν∈K 同时取 subsequence，可得 uniform ≤D finite-jet lower。包括 zeroth order，正是 Cor3.4 排去小 value 后所需的每点 positive-order lower。

这不是“全局 norm 在某处产生大 jet”而已；compactness 对任意 varying points给每个 incident point uniform 下界。使用任意关系的 removable factors 不破坏该论证。

## 3. 有限方向、sublevel 和 closure

A 的 finite real-direction construction 可由 degree-q homogeneous polynomial 在 {0,…,q}^n 网格的插值证明 injectivity；非零向量归一化不改变其是否为零。q=0 另以 value处理。complex f 取 Re/Im 中一项，q+1 derivative upper使 lower在固定 radius保持，因此有限 cover与 divided differences确给 sublevel exponent 1/D；无须有限实零点数或 algebraicity 的额外 regularity。

Remez由相对 norm sublevel直接反解；zero function、positive-measure E 上 norm0、ratio≥1 均已单列，未错误套非零归一化。affine translation/rescaling只对相应 scaled derivatives 宣称 uniform；没有免费消去 shrinking geometry 的成本。

product over root combinations 的 evaluation relation在 C(z) 中为 monic W-polynomial，故非零；分 roots 对称使 coefficients 可由 elementary symmetric polynomials表达，清 leading denominators 的 fixed power后 total degree bounded。numerical denominator再小不改变次数。

fixed derivatives 的 resultant 中，选 genuine irreducible factor P₀；char0 下 P₀与 P₀,W coprime，最高 Y coefficient是 nonzero resultant乘 leading factors，所以新 relation不是零。generic处的 differentiated identity再 holomorphically延至 singular points，无需在那里除 P₀,W。

affine-line restriction若 direct relation为零，A 用平行 lines扰动、coefficient归一后取非零 limit；chosen f composition在 fixed disk上uniform convergence使 identity保留。limit若 W-independent就为一个在整 disk为零的非零 polynomial，矛盾。因此 specialization没有丢掉 degree control。

## 4. Root preliminary degree 与 actual reference

两原 sheets 的 irreducible relations必含 W。Res_W(P(z,W),Q(z,W−T)) 对 T 为非零 polynomial：generic root pair有 T=u−v，符号正确；Sylvester matrix size≤2D、entries total degree≤D，故 relation total degree≤2D²。cleared identity先在 nonzero leading coefficients开集成立，再延至 whole holomorphic domain。

取 actual list member f_* 再减并除 M，既保 common domain又无需假外部 common reference 的 degree。hκ,i norm≤2R^ε，degree bounded；incident g_pair直接是两个**原** sheets之差，因此同一 D′=max(1,2D²) 足够，未重复扩大造成隐性参数循环。M任意大小只替 relation的变量缩放，不增 degree，不要求 height lower。

若使用 finite fixed balls作原 domain的局部 cover，应理解为同一 connected holomorphic domain中的固定 overlap chains；norm propagation只付固定次数比较。root 的主 ball/polydisc scope本身已满足，不把分离 components 的任意函数拿来比较。

## 5. 每事件 norm-to-jet、boundary boxes 与原 law

incident pair的 normalized norm≥R⁻ε，Lemma3.1给每 event z 的 jet≥cR⁻ε。value≤R^{-1+ε}，ε≤1/4时其与 lower的比至多 R^{-1/2}/c，故固定 R₀即可统一排去 zeroth order，不依 ε趋零。

finite p/direction检测只依 n/D′，再按第一个满足 lower 的条件分 measurable classes，保 fixed fraction。fixed boxes可略伸出原 real ball，但 enlargement仍在原 holomorphic margin内；μ外延0。因而没有把所有 mass可能落入的 R-dependent boundary collar删掉。boxes/directions/interval lengths均不随 R或所选 event变化。

finite pair components对 Lebesgue绝对连续。先为全部 indices/colors取 finite null-set union，再 Fubini，故几乎每个 transverse x 上两组 index–time ceilings同时成立。event value/positive-jet lower也在 sliced law下几乎处处成立。高 slice mass m(x)≥cR⁻ε 的 fibers 为正测度，可和 good full-measure fibers取交。

只有选完该 x 后才 normalize；每色 upper变为 R^επ_i/m(x)≤CR^{2ε}π_i。π 保原 probability weights，零权及极小正权都合法；未按 active indices免费重设 π。相关 i/j/time从未被独立化。n=1 的 transverse R⁰按 volume1单点处理一致。

## 6. 全部 loss 与 R₀ 独立 ε

fixed interval affine rescale后，各 positive directional derivatives乘 ℓ^p，概率 density乘 ℓ；所有 finite choices的 ℓ 有 fixed positive lower。high-order upper通过 fixed holomorphic margins得到，因此统一 K_R=C′R^{2ε}可同时控制 derivative upper、两色 marginals、value gap和positive jet lower。

root 取 d₁=(1+d₀)/2<1，再用 TCM001 对固定 matching orders D_m=D′、J=D′+1、d₁的 tolerance η。令 ε_*≤min(1/4,(d₁−d₀)/2,η/4)，则列表card≤R^{d₁}，2ε≤η/2。预先取 R₀使 C′≤R₀^{η/2}，于是对**全部**0<ε≤ε_*、R≥R₀有 K_R≤R^η。

这正确保留 R₀ 的 uniform量词。把 C′吸入 R^ε 会在 ε→0时失败，现稿未这样做。TCM001的 N可实数R；若坚持 floorR，card buffer和fixed constants也足以支付。所有 orders、η先固定，再选 ε_*与 R₀，未循环依赖所选 slice。

## 7. 两个假设删除测试的完整核验及已修事项

degree 删除例：f₁=0、f₂=z^k，k=ceil(2log₂R)，B=[0,1]、fixed complex disk有 fixed margin。pair norm_B=1、reference0、mass1、single indexπ=1；t∼Uniform[0,1/2] density2，values≤R⁻²≤R^{-1+ε}。对任意固定 ε>0，R大使2≤R^ε，所有其它条件保留；唯一 degree随 R增长。该模型不否定原 fixed-degree命题。

原 margin test 的 a²/(z²+a²) 若仍要求 Ω为 disk，任何包含 [−1,1] 的 disk都会含至少一个 ±ia pole，不能仅归咎于 margin。该处已通知并由 root换为最新版：

\[
B=[0,1],\quad a=R^{-2},\quad
f_2(z)=\frac{a}{1+a-z},\quad
\Omega_a=\{|z|<1+a/2\}.
\]

现在 Ω_a仍为 complex ball，pole1+a在其外，故 f₂ whole-domain holomorphic且 real-on-real；relation degree2固定，norm_B=1。event t∈[0,1/2] density2给 value≤2a≤R^{-1+ε}，其余 card/π/mass/reference/normgap全同上一例。B距 Ω_a boundary为 a/2→0，确实只缺 uniform holomorphic margin，修复通过。

A 的 tiny-coefficient example只追 bounded chosen quadratic branch，large unused root归一化后也不违 homogeneous bounds；variable Bε逼近 fixed Ω boundary 的模型在 K={0}令所有 fixed jets→0，明确违反 fixed normalization geometry；shrinking normalization ball的 linear model令 fixed-point norm发散，亦非原反例。三类测试的违法项均明确，未把一个假设删除例升级原 Cor3.4 counter。

## 8. 真依赖与验收界限

Cor3.4 当前证明使用 Lemma3.1、bounded-degree closure及TCM001；**没有使用Lemma3.2的path continuation**，因此不应虚加其branch/tube假设。后续 Lemma3.5 才有该独立责任。本人的3.2主稿由其他代理审查，不在此计作自审通过。

在上述固定几何、degree、common domain/margins和原 π/mass假设下，Cor3.4已完成一般维度、任意相关events的内部逐步认证。后续 atlas/knowledge/temperedness及critical alternatives尚未因此核完；SRC/DIR/FSD/DIM的完整OAI4条件仍保留，六维17/4仍条件，长期Goal active。
