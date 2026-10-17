# R0035：conservativity、势函数、heavy intercept 与 degree restoration

2026-10-17，B 独立审查稿。对象为原 §6.5–6.9（Cartesian interpolation、Prop6.5、Lemmas6.6/6.7、Prop6.8），并追读 §6.1–6.4 的 physical caps、long witnesses、state/palette输入。root完整6.1及A负责的scalar/qualification另待正式全文独审。以下不独自认证整个6.1，不称新高维结果。

**本稿后半链结论：在原前置 physical/qualification/插值条件全部已付时，switched signed paths至 proper quadratic candidate的推导可成立，未找到保原假设的反例。** 原高维 moment-curve/common-q失败不反原 R3七方向定理。determinant multilinear估计为 Carbery–Valdimarsson Theorem1具名高级输入，本稿只核所需 statement/使用接口，不重证其深层证明。

## 1. 固定 law、scales 与输入责任

固定一个 substantial residual和同一 frozen parent law。m=j+1为2或3；λ(l,t)=G_wt(l,t)ν(dl)dt，0≤G_wt≤K=N^{o(1)}，ν始终条件于完整 parent assignment。line/packet选择只 restriction，不按 time-success重置 ν。fixed exponent ranges、physical b、direction bins、qualification meshes先声明，再在失败集内应用；S0的值不参与这些网的选择。

取 fixed s>0，a=N⁻s，实际 Q-block长度 h∼log,N a^k，p*=1/k。选0<α<1/2，e1=α/2，c0=e1(1−d)/2，e2=c0/3；ε_T=h^{p*−1+α}，a1=a h^{e1}，a2=a h^{e2}。各为固定幂精度且0<e2<1。physical/velocity/base meshes可预先细于所有以下固定幂比较；显式要求 Kξ≪ε_T（fiber-field比较）及 Khξ≪a1（endpoint joint cells），前一项不由后一项单独推出，原“all later evaluations accurate”允许同时预声明。b和 direction-bin误差尤其能满足 h²/K与 a2/a精度，无需预知 hidden幅度。

关键前置接口：ν_Q∼a^d h^j；pure X-cap与 joint π-cap；same ν° 的 coefficient-box上下界/finite lists；state conditional palette domination及 breadth在稀疏选择前准备；qualification是 frozen post-renewal law下的 relative o(1) failure，不是某失败集中偶有好点。它们未由本稿后半证明自动获得。

## 2. Cartesian 插值所需的真实质量

state D=(parent,Q,W_b)有实际原 observation list及 deep-history ambiguity。返回 substantial reference law，先按原 fixed state law准备 palette/breadth。若 U_N为 qualification失败集合，q_D=Λ_prep(U_N∩D)/Λ_prep(D)，则对 fixed η有 Σ_{q_D>η}m_D≤Λ_prep(U_N)/η=o(1)。因此好 state中的 fixed-size spanning tuple可同时 qualified；不是把 o(1)错误率直接传给任意 sparse subset。

以 conditional-product sampling和 palette domination固定一组方向 p_i=(1,V_i)及共同 witnesses，所选 states保质量≥hν_Q/K。令 A0以 p_i为列，应使用 **r=A0^{-1}u** 的 product grid，沿 r_i纤维即沿 p_i。PDF p97 的 bbox glyph中确有 A0上标−1；txt把它并到邻行，不是源坐标错误。

每 fiber的 polynomial fit coefficient bins至 ε_T只有 K种：对每 represented bin固定一个真实 long witness；M+1独立 uniform block times同时落 witness且 separated的概率≥K⁻¹。每成功time tuple的 coarse field lists与 interpolation只容K coefficient bins。对 bins求概率和即得数量上界，不需 witnesses彼此独立。

选择每 fiber一项 polynomial-bin、每 cell一项 field-bin，独立有限抽样保共同 states质量≥hν_Q/K。删 low cell mass，以 base cap得 occupied Cartesian fraction≥K⁻¹。product anchors/target的全部 vertices retained概率≥η0^{(M+2)^m}（逐轴 conditional Jensen），再删太近 anchors，固定 separated anchors及 inverse-subpower successful targets。tensor Lagrange weights仅K，得到 bounded-degree row T、coefficient/derivatives≤K，且所保 states上 |G−T|≤Kε_T。

该结论仅依 state。此后恢复这些 states的全部 prepared reference edges，保持原 conditional breadth与 palette；不用声称恢复的边全部 qualified。对 current line duration≥h/K，X'−T(u)·p是固定次数 time polynomial，原误差在 long set上成立，Remez延至整条 Q-block，即6.23。

joint support计数6.24需要另付 descendants：true thickness a_i的 whole assignments与 full ν质量下界、disjointness和 physical-gradient graph lists。每个 descendant占≤K(h_i/(hξ))^m joint cells，h/h_i blocks，总数≤Kξ⁻m(a/a_i)^d。ξ预先使 Khξ≪a1（故亦≪a2）。它不是只从 current incidence mass lower计 descendant数，也不要求 current path保持每层旧 floor。

## 3. Prop6.5：同一个 P 的两个 refresh

归一化 restored state-selected Q-incidence为 probability P，分母≥hν_Q/K，因此 u-base density≤K。若 ||skew DT||≥H:=h^{p*−1+c0}，固定次数 polynomial sublevel和 base cap可删任意小 fraction starts，使 sampled start的 skew≥H/K。

从 e_{i−1}先按 **P(·|D(e_{i−1}))** fresh取一 incidence，再保它的 line、按 **P(·|line)** fresh取 endpoint time；两次操作各保 marginal P。当前 restored-state law的 weighted line duration<h/K1的 P质量≤K/K1，由 ν_Q预算和该同一 normalization denominator证明。finite 2m步可 union bound删短 choices，但不把随后 good transitions重新归一化。

在 longness筛选之前，给任意 past，next velocity来自 prepared state law，其 thin-pencil概率任意小。sequential avoidance使前m和后m controls分别为 well-conditioned bases，正概率不依N消失；与 high-skew、long choices相交仍有正下界。

good next-step的**未归一化** measure满足

\[
 dP\{[V_i]=J,t_i\in dt_i,\text{long}\mid\text{past}\}
 \le K\pi(J)\,dt_i/h.
\tag{1}
\]

palette factor来自 state refresh，time factor来自 G_wt≤K除该 current line的 long weighted duration。逆向逐步条件积分，将任意 nonnegative path functional支配于 start P × palettes × normalized endpoint Lebesgue measure；不要求成功事件条件下独立。

δ_i=(t_i−t_{i−1})/h可正可负。由 endpoint times到 signed increments的变换 triangular、Jacobian1，范围在[-1,1]^{2m}。同 W_b refresh引起 physical(z,X)误差Kb；native X与 z都有 bounded motion，所以回到 previous time仍Kb，无需 w有 tangent motion上界。有限步模拟误差为 K(b/h+p_v)于 u、K(b/h+p_v+ε_T)于 X/h，分别远小ξ、a1/h。

## 4. Jacobian minor和实际 endpoint支持

模拟 endpoint map为 Φ(δ)=(u0+Aδ,R(δ))，R为依次沿 signed segments积分 T·p_i的 fixed-degree polynomial。固定 start还需加实际初始 X0/h；它只是 endpoint height的平移，不改变 cell数或 Jacobian。

取前m列 I、后m列 J各为basis。固定 base endpoint的第j方向是 ∂_j−Σ_i(A_I^{-1}A_j)_i∂_i，相应 height derivative乘 detA_I即一个 maximal minor。若全部 minors的 polynomial norms≤η，其对 I坐标的导数在0也≤Kη，故

\[
 (D^2R(0))_{I,J}\approx (D^2R(0))_{I,I}A_I^{-1}A_J.
\]

左侧直接积分计算为 entries DT(u0)[p_i]·p_j；右侧对应同一 symmetric matrix在两 bases间传送。两 basis可逆，迫 skew DT(u0)≤Kη。因此 high-skew starts至少一 maximal minor norm≥H/K。

polynomial sublevel结合 (1)删 minor绝对值<H/K1的 increments，损失可任意小。对 passing region固定其余 m−1 controls，剩余 m+1变量的 polynomial map有 Jacobian≥H/K1。只需 **regular preimages** 的 fixed-degree multiplicity bound：它们是 isolated solutions，可用固定次数代数/半代数孤立纤维界；不声称整个 fiber处处 finite。

area formula于是给单 endpoint cell preimage volume≤Kξ^m(a1/h)/H。每条真实成功路径的 simulated endpoint在 actual support6.24的固定扩大内；不是把任意模拟路径自动放入 support。#cells≤Kξ⁻m(a/a1)^d，start height平移不改它。总 path概率因此≤

\[
 K(a/a_1)^d(a_1/h)h^{-(p*-1+c_0)}
 =K h^{e_1(1-d)-c_0}=K h^{c_0}\to0,
\]

反正下界。故 conservativity得证。其关键是 full (m+1)-维 cell volume；只估 base volume或只用一个小 endpoint球都不足够。

## 5. 势函数与拦截 groups的同 prior收费

P(u)=h∫_0^1 T(tu)·u dt。直接求导并用 d[tT_j(tu)]/dt比较，∇P−hT只含 DT−DT^T项，故≤K a h^{c0}；所有 fixed positive derivatives≤Kh。沿 long line whole Q-block由6.23积分得 X−P variation≤K a h^{c0}≪a2。

C为 midpoint (X−P)的 a2-bin，每条 whole trajectory只有一个 C；state知道 u,X足够准且 P梯度Kh，所以每 state仅 boundedly many neighboring C。对 arbitrary moving center P(u)+C，good X-bin cap可用少数 fixed-grid bins覆盖，得到 group u-base density/(hν_Q)≤K(a2/a)^d。

不能从 arbitrary C-restriction继承 breadth。原流程先删短 lines、损失过多 states，再只保 state中占 fixed fraction的 C；此时原 pencil概率除该 fraction，选择初始 pencil阈值更小即可保一般位置。再删该 family的短 lines、损失过多(D,C)-states，以及相比**最后短线删除前**总质量损失过大的 groups。所剩 group current mass M配最近 long witnesses给 contributing prior weight≤KM/h；不可拿较早 group floor替换这份 witness。

对一个 group，以 ξ-cells记 masses m_E。每 line在 cell的 weighted physical duration≤Khξ；breadth保证 conditional independent velocity tuples的 determinant成功率下界。具名 determinant multilinear estimate在 m维 base、m个families、radius ξ，结合该 prior bound给

\[
 \sum_E\bigl((m_E/(h\xi))^m/K\bigr)^{1/(m-1)}
 \le K(M/h)^{m/(m-1)}.
\]

power mean消去 M，得每 group至少K⁻¹ξ⁻m occupied base cells。任一 joint (u ξ-bin,X a2-bin)只容K个 C，因为P在cell中变化≪a2。因此6.24迫 total groups≤K(a/a2)^d；删小 groups遂保每组≥hν_Q(a2/a)^d/K而总质量仍≥hν_Q/K。6.29 whole-block P+C fit对所有保留 long lines成立。

## 6. 原 R3 七方向核与 real-conic conditioning

以下只针对 p_i=(1,V_i)∈R³、七点且每triple独立。

- singular complex conic是两条直线并，每线最多含两点，不能含五点。任五点的 conic space恰一维：前三点作projective basis，余两点给独立条件，故全七点 quadratic kernel维≤1且非零者 nonsingular。
- cubic two-copy tests等于所有 first derivatives在p_i为0。若quadratic kernel为Rq，Euler使F=qL；∇F(p_i)=L(p_i)∇q(p_i)，故L在三个独立点为0，F=0。
- cubic three-copy kernel为q·Lin：限制到 nonsingular conic parametrization给 binary sextic，七 distinct zeros迫恒零，再由monomial remainder证 q整除。
- quartic的每一 first partial是上述 cubic，Euler得F=qH；选非零linear ∂q并用gcd(q,∂q)=1迫q|H，故F∈Rq²。
- quintic的每一 first partial先由quartic结论为λ_jq²，Euler得F=q²L；再微分/mod q²迫q|(∂q)L，故L=0。

compact fixed-format point family加 real quantifier elimination给 polynomial conditioning。rank4 estimate只在 exact-conic family的constant-rank集合使用，不能从 off-conic附近 smallest positive singular value免费取得。

approximate real q的 norm上下、point conditioning和小 evaluations，使 |detQ|+Σ|q(p_i)|的 compact semialgebraic正下界给 |detQ|≥A^{-C}。空间 gradient亦下界：Euler ∂0q+V·∇_Vq=2q，full gradient下界和小q值排 spatial gradient过小。在 spatial gradient方向作 real one-variable IVT，修到实零 p_i'，距离≤A^Cε，first coordinate保1且 triple determinants保原一半。故没有假设 conic先已实不定或远离singular；这些性质由实际条件推出。

## 7. Degree restoration：先 analytic bounds，再移方向

v1用 heavy group long witnesses，P与 quadratic X−C在各线相差Ka2；one-variable polynomial Remez得 D_p³P≤Ka2。state四 separated directions、common-state质量配 group base ceiling给 inverse-subpower base volume；binary cubic Vandermonde与 fixed-degree Remez迫∇³P≤Ka2。二次 Taylor test w−F符合原special model。

v2在同组解 native equation P*(z,f(u))=P(u)+C。native derivative/curvature和残差Ka2给 positive discriminant、stable simple real branches及w−f≤Ka2，不需 w在tangent units bounded。以 real core/sign固定选择并删 short line/group/core/sign portions；每 line一个C、仅K core/sign choices，损失以 hν_Q预算付。重删 excessive state/group fractions保 breadth/palette。有≤K(a/a2)^d choices，因此选一 choice质量≥hν_Q(a2/a)^d/K且每line有同一choice内最近 ordinary long witness。

**先定义** R= P_s(z_c+hu,f(u))/a。原 true test于 witness的 exact quadratic Taylor给 |R|≤K；same group cap与 mass floor给 real projection volume≥K⁻¹，algebraic norm lemma给 R所有必要 fixed derivatives≤K。这个 independent R-bound先于任何 conic shift，不能省略。

沿每 contributing line比较 f与 affine w_l、R与 quadratic P_s(z_l,w_l)/a，使用同 controlled core/chord内 ordinary length≥h/K的 witness，得 |D_p²f|≤Ka2、|D_p³R|≤Ka2/a。S0=dist(f,affine)在 U上；S0>0时选误差≤2S0的affine L，所有order≥2 derivatives≤KS0；S0=0平凡。

七 velocities在state sequential避所有连接线，breadth给 fixed positive成功率；palette domination、averaging固定一个 tuple有 common witness states质量inverse-subpower。位置/velocity mesh误差对 f按 KS0乘δ收费，预先令δ≤h²/K即可，**不依S0大小**；对 R用刚建立的独立K-bound。common-state mass和 base cap后再对 directional derivative functions作 norm extension，得6.34及其必要 fixed derivatives。

## 8. S0两种情况与 native quadratic编码

differentiate D_{p_i}²f再用 cubic two-copy injectivity，得∇³f≤K(a2+S0h)。若S0≤a2/h，二次 Taylor f2误差Ka2，w−f2直接合格。

否则 S0>a2/h。以中心 Hessian/S0定义 homogeneous q，third-derivative余项给 (f−L')/S0=q+O(Kh)；distance-to-affine定義与 relative derivative upper给K⁻¹≤||q||≤K。tests给 |q(p_i)|≤Kh。由于 h是 fixed negative power、所有conditioning为 subpower，real-conic lemma可用，移到exact real p_i'距离≤Kh。

R derivatives已先有K-bound，故rank3/4/5 contractions的shift error≤Kh≪a2/a=h^{e2}。exact-conic tensor kernels给

\[
 R=R_2+qL_1+\lambda q^2+O(Ka_2/a),
\]

其中所有coeff≤K：∇⁵R由零kernel控制，Taylor到4阶；固定次数 product norm下界和 ||q||≥K⁻¹支付因子除法。这里不能把高维 common-q猜测代替原R3核。

设 H'=(w−L')/S0。在前置 long witnesses，H'=q+O(Kh)、|H'|≤K，定义

\[
 P_{new}=P_s-a\bigl(R_2+H'L_1+\lambda(H')^2\bigr).
\]

括号内全乘 a，PDF107该括号已在旧源审视觉核，不能按txt排版误读。所有项total degree≤2。以H'代q成本Kah≪a2，以实际w代f成本Ka2+Ka2²/a，故value≤Ka2。

derivative perturbation≤Ka/S0<Kh^{1-e2}，保原counted lower；curvature≤K/a+Ka/S0²≤K/a2+(K/a2)h^{2-e2}≤K/a2。无绝对 S0/L'/w tangent幅度界被加入。

最终 equation为全空间 proper quadratic。沿每version2 trajectory value是time quadratic、hidden derivative是time affine；ordinary witness length≥h/K位于同一h-block，polynomial Remez仅在该h-block外推，给whole-block value/upper derivative。version1同样fixed-degree。不能将这份witness外推到单位parent time。lower只需 counted incidences。

最后质量仍≥hν_Q(a2/a)^d/K，除h即原候选mass；gain e2 log_N(1/h)→e2ks为positivefinite，可接 AIM。实际原尺度编码/slack通过 AIM 的完整constructor处理，不从 S0巨大时的tangent图表直接推原guard。

## 9. 当前责任与停止

后半链没有发现未付的原prior、regular multiplicity、real conic或same-block extrapolation缺口。正式 Theorem6.1验收还须 root/A完整支付 §§5–6.4：尤其 same frozen ν°的 parameter lower/upper、relative o(1)qualification、renewal mass/entropy及 named planar input。不能用本稿后半通过提前认证它们。

本稿未改高维frozen账、未新增primary文件、未Git操作。正式全文review待root ready；一般/五维满维和六维无条件界仍未达成。
