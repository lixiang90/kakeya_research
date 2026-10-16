# R0025：scalar curvature engine 的原文审计及同先验径向修补

2026-10-17。唯一任务 N5-MIXED43-NQ01 的子任务 A。本文只处理 scalar finite engine 的 separated-time 层；原 fine weighted time 到该层的选择由 root 另证。它不调用整个 Lemma 22.5，不构造新的四维 Kakeya configuration，也不声称已解决 mixed43、五维或一般维 Kakeya。高级输入 scalar BSG 13.7、radial 22.2 的完整证明本轮未重跑，均作为具名条件输入。

## 1. 已读范围与精确输入

主文献为 `literature/primary/wang_zakharov_2026_sticky.pdf`，Wang–Zakharov arXiv:2609.22035v1。行号统一指 `literature/extracted/wang_zakharov_2026_sticky.txt` 按 `split('\n')` 编号；页码指 PDF/印刷页，两者此处一致。本轮逐行读下表范围，另核 §3 定义及 §5 uniform refinement。未宣称完整核验全篇 117 页。

| 原位置 | 本轮核出的准确责任 |
|---|---|
| Def.3.1，PDF15，765–767 | `(w,s,K)-set` 是归一化 counting cap `#(A∩B_r)≤Kr^s#A`，不是 Katz–Tao cardinal cap。 |
| PDF20，1017–1025 | metric `(w,K)-uniform` 定义；任意 bounded separated set 可取大小至少 `w^u` 倍、uniform constant `w^-u` 的子集，任意固定 `u>0`、足够小 w。该标准 refinement 本文具名使用。 |
| Lemma13.7，PDF54，2826–2831 | scalar asymmetric BSG；另须 `#Y≤#X^C`。给定 `C,ε_B` 才得到常数 `K_B`；输入 energy loss 的幂须最后选小。 |
| Theorem22.2，PDF96，5078–5084 | 三维 **separated、uniform、2-Frostman** 点集，且所有宽 `w^σ` slabs 质量≤`w^b_s`；`σ≤ζ/100`。其 `η_0` 依赖 `(σ,b_s,ζ)`，不能忽略 slab 指数依赖。输出坏对质量≤`w^(η_R/10)`，好对所有 `r≥w` 的 tube cap≤`w^-ζ r²`。 |
| Lemma22.3，PDF96，5086–5091 | separated parameter set 和 target set；文字结论是 **image set** `π_λ(P_λ)` 的 counting Frostman。它本身未明确给原 target 标签的 pushforward multiplicity cap；下面直接证明所需的 weighted law 版本。 |
| §22.5 Step2–4，PDF100–102，5307–5421 | 原 L 图、scalar Y 的工作尺度、F/G 定义与 quadratic nonfit。fine-time 分离及 A 的重权化不是由符号 `|B|_w` 自动完成。 |
| Step5–7，PDF103–105，5424–5554 | 原 S、Q、U、V 恒等式；balanced S cells、BSG；P 的 multiset/均匀化、(208) 原 B⁴ almost-all、投影乘数及最后 multiplicity 的接口。本文补证其中几个有限步骤。 |

原式为（把原 `F̃` 记为 G）：

\[
 S(t,s)=(s-t)[F(t)-F(s)-G(s)(t-s)],\quad
 V(t)=(t,t^2,F(t)),\quad U(s)=(F(s)-2sG(s),G(s),s).
\]

直接展开得原 (202)–(204)：

\[
 Q(t_1,t_2,s_1,s_2)=S(t_1,s_1)-S(t_1,s_2)-S(t_2,s_1)+S(t_2,s_2)
 =[V(t_1)-V(t_2)]\cdot[U(s_1)-U(s_2)]. \tag{1}
\]

G 完全任意，以下不假定它是 F 的导数、连续函数或分片低振荡函数。

## 2. 本文证明的有限 separated-time 命题

固定 `0<κ<1`、bound M。对足够小的 `α>0`（只需依赖 κ、M）及任意固定 `b>0`，有 `η_*>0,w_*>0`，使下列输入在 `η<η_*`、`w<w_*` 时不相容，**条件于上述具名 BSG/radial 输入和 uniform refinement**：

1. B⊂[-1,1] 是 w-separated finite set，ν 是其均匀概率，`ν(I)≤w^-η |I|` 对所有长度≥w 的 intervals 成立。
2. `|F|,|G|≤M`，且对所有 real quadratic p，`ν{|F-p|≤w^α}≤w^b`。
3. scalar A₋、A₊ 在固定 bounded box 内 w-separated，`#A₋≤w^(-1+κ)`，`#A₊≤w^-η #A₋`。
4. `0≤g≤1`，`E_(Uniform A₋×ν²) g≥w^η`；若 g(x,t,s)>0，则 `dist(x+S(t,s),A₊)≤C_M w`。

原 coefficient-weighted nonfit 强于第 2 条，故够用。结论允许固定倍 base-resolution、box 与误差常数；可用固定 scalar grid colouring 或 common homothety 处理，严格正幂余量吸收这些常数。本文不把一般 fine-time ν 称作这样的 B。

### 参数顺序

下面给一个可实现顺序，防止 `η` 循环：先取 `β=q_n=κ/20`，`ζ,c_ch≪β`（例如各 κ/10000）；再取 `8α≤ζ/100`，令 `σ=8α`、`b_s=min(b,α)/4`。由 22.2 取固定

\[
0<a_R<\min\{\eta_0(\sigma,b_s,\zeta),b_s/100,c_{ch}/100,\beta/100\}.
\]

随后取 `q_g,u≪a_R`，使下文 P 的损失小于 `a_R`；再取统一 BSG/图密度损失 `ℓ≪q_g,u,a_R,c_ch,β`。先固定 BSG 的 `ε_B` 使其固定 n,m≤4 的损失小于 ℓ，再取得其 `K_B`，最后才选原 η 足够小（也依赖 `K_B`）。可使所有 `p≥w^ℓ`、BSG cover `≤w^-ℓ #A′` 同时成立；把固定倍 ℓ 吸收进同一记号。最后缩小 w。`q_n` 是删小向量的指数，`q_g` 是删近对角时间对的指数，二者不同。

## 3. 原 balanced S 层的基数下界：任意 G 也成立

令 `m=E g`，`k(t,s)=E_x g(x,t,s)`。边集 `H₀={k≥m/2}` 的 ν² 质量≥m/2，且每个边有至少 `(m/2)#A₋` 个可用 x。按 S(t,s) 的 w-cells 和每 cell 的 H₀ 边数作 dyadic pigeonhole；得到 w-grid set T 及 `H_j⊂H₀`，每 T-cell 含 `D≤#edges<2D`，且

\[
 \nu^2(H_j)\ge m/(C\log(1/w)). \tag{2}
\]

这里只有 O(log(1/w)) 层，因为 `#B≤C/w`；保留的是原边，不是换一个 S 的均匀先验。

对任意 real z，由 (1) 固定 `(t₂,s₁,s₂)`。若 `|s₁-s₂|≥r₀=C_M w^(1-α)`，则 `|Q-z|≤C_M w` 把 F(t₁) 限制在某个 quadratic 的 `w^α`-neighborhood 中。因此

\[
 \nu^4\{|Q-z|\le C_Mw\}\le w^b+C_Mw^{-\eta}w^{1-\alpha}=:A_w. \tag{3}
\]

小时间差的质量由 interval cap 给出；这里不需要 F/G 正则性。H_j 的 C₄ 质量≥`ν²(H_j)^4`。其 Q 落 `T-T-T+T+O(w)`，最多 `C#T⁴` 个 w-intervals。故

\[
 \#T\ge c\big[\nu^2(H_j)^4/A_w\big]^{1/4}\ge w^{-c_0}, \tag{4}
\]

可取某个固定 `c₀>0` 依赖 α,b，再让 η 小。此为原 5458–5460 “similar to Claim13.8” 的完整有限补证。特别它先于 BSG，不以径向结论循环证明 small-S。

## 4. asymmetric BSG：energy、原边及小输出集

每 T-cell 任取一个真实 H_j 边。它有至少 `(m/2)#A₋` 个 x 使 `x+Tcell` 落 A₊ 的 O(w)-邻域。因此有关系 `R⊂A₋×T`，`#R≥(m/2)#A₋#T`，其 sums 至多占 `C#A₊` 个 w-cells。按 sum-cell Cauchy–Schwarz 得 full additive energy

\[
 E_w(A_-,T)\ge c\,m^2\,\#A_-\#T^2\,w^{\eta}. \tag{5}
\]

若 cell 误差取固定倍 w，先分成固定数小 cells 或对 convolution cell-count 用有限相邻项 Cauchy–Schwarz，可得同尺度 (5)。加法 energy 与 13.7 所写 difference energy 由交换两个 A 标签相等。

由 (4) 及 `#A₋≤w^-1`，可取固定 `C_B=2/c₀` 使 `#A₋≤#T^(C_B)`。用 Lemma13.7，得到 A′⊂A₋、T′⊂T，各保 `w^ℓ` 比例，并且（n,m≤4）

\[
 N_w(A'+nT'-mT')\le w^{-\ell}\#A'. \tag{6}
\]

原 13.7 右侧为 `#A₋`，用 A′ 的下界换成 (6)，这一额外幂已计入 ℓ。

定义 H 为 **H_j 中** S-cell 属于 T′ 的原边。balanced counts 给

\[
 p:=\nu^2(H)\ge w^\ell. \tag{7}
\]

若只保 T′ 的 cardinal fraction、而未先平衡原 cell weights，(7) 不能推出。H 的所有 cycles 的 Q 属于 `2T′-2T′+O(w)`；两个这样的 Q 之差属于 `4T′-4T′+O(w)`。固定任意 a₀∈A′，`a₀+4T′-4T′` 包含于 (6) 的 n=m=4 sumset，所以

\[
N_w(\{Q(c)-Q(c'):c,c'\text{ are H-cycles}\})
 \le Cw^{-\ell}\#A'\le Cw^{-1+\kappa-\ell}. \tag{8}
\]

本有限修补直接使用 13.7 的 n=m=4 结论，无须另把 Plünnecke–Ruzsa 当作未展开步骤。

## 5. 真实左时间对→uniform P，并在新先验再生 cycles

对左对 `l=(t₁,t₂)`，设 `N_l={s:H(t₁,s)H(t₂,s)=1}`。Cauchy–Schwarz 给

\[
 E_{l\sim\nu^2}\nu(N_l)\ge p^2.
\]

因此 `L={l:ν(N_l)≥p²/2}` 的 ν² 质量≥p²/2。删 `|t₁-t₂|<g₀=w^(q_g)` 只损 `Cw^-η g₀≪p²`，剩余至少 p²/4。每一保留对仍有 **原右时间** 共同邻居质量至少 `d₀=p²/2`。

映射 `l↦P_l=V(t₁)-V(t₂)`。前两坐标 `(d,e)=(t₁-t₂,t₁²-t₂²)` 在 `|d|≥g₀` 上反解

\[
t_1=(e/d+d)/2,\qquad t_2=(e/d-d)/2.
\]

两对的 (d,e) 距离≤r 则原 times 距离≤`C r/g₀`。故任意 P-space r-ball（r≥w）的原 product probability≤

\[
C w^{-2\eta}g_0^{-2}r^2. \tag{9}
\]

在 r=w 时，w-separated B 还给 ball 内原 pair 个数≤`C g₀^-2`。从这些真实像中取 maximal w-separated net，再用原 1017–1025 的 uniform refinement，得到真实点集 P，每个点保一个实际 l witness，且

\[
\Delta_P:=\#P/(\#B)^2\ge c w^u p^2g_0^2,\quad
\sigma_P(B_r)\le Cw^{-2\eta-u}p^{-2}g_0^{-4}r^2, \tag{10}
\]

P 为 `(w,w^-u)-uniform`。所有点都是实际 P_l，**没有将 V 或 F/G 舍入到代表函数**。每点的 min degree d₀ 由其原 l witness 保持。P 的均匀先验等于选中真实左对的原 ν² 条件先验，选中事件质量恰 Δ_P；这是付损失的 prior restriction，不是假定所有原对等权地保留。

在 `σ_P×ν` 上令 `h_P(P_l,s)=1_(s∈N_l)`。每点 degree≥d₀。定义

\[
\mathcal W=\{(P,P',s_1,s_2):h_P(P,s_i)h_P(P',s_i)=1,\ i=1,2\}.
\]

先 `E_(P,P′,s)h_P(P,s)h_P(P′,s)≥d₀²`，再平方作 Cauchy–Schwarz，得到

\[
(\sigma_P^2\times\nu^2)(\mathcal W)\ge d_0^4=p^8/16. \tag{11}
\]

这是 d₀⁴，不是 d₀²；后者只有一个 shared-right 标签。每个 W 元素对应原 B⁶ 的八条 H 边，即原 K₄,₂。其原 ν⁶ 质量下界为 `Δ_P² d₀⁴`。对 W，输出恰为

\[
(P-P')\cdot[U(s_1)-U(s_2)], \tag{12}
\]

且仍满足 (8)。下面 radial/Kaufman 的 almost-all 只用于 **新 σ_P² 先验**；不声称原式 (208) 对原 B⁴ 的量词免费成立。

## 6. 新 P 的 slab cap 与具名 radial 输入

先估原 ν² 下 P_l 的任意宽 `w^σ` slab。固定 t₂ 后：

- 若单位 normal 的 `|n₃|≥w^(σ/2)`，则 F(t₁) 被限制在某 quadratic 的 `C_Mw^(σ/2)`-邻域。σ=8α 使该宽≤w^α，所以质量≤w^b。
- 若 `|n₃|<w^(σ/2)`，则 `(n₁,n₂)` 有固定下界；`n₁t+n₂t²` 的相应 sublevel 是 O(1) 个总长≤`C_Mw^(σ/4)` 的 intervals。由 time cap 得质量≤`C_Mw^-η(w^(σ/4)+w)`。

因此原 slab probability≤`w^b+C_Mw^-η w^(σ/4)`。选中真实 pairs 的 normalized probability 最多乘 Δ_P⁻¹；(10) 中损失由既定次序选小，遂得到所有 slabs

\[
\sigma_P(\text{width }w^\sigma\text{ slab})\le w^{b_s}. \tag{13}
\]

同时 (10) 的 2-Frostman constant、uniform constant 均≤`w^-a_R`。P 的固定 bounded box 用 isotropic homothety/translation 化为 [0,1]³；base scale 只改固定倍，(10)、(13) 的严格幂余量保留。用具名 Theorem22.2（参数 a_R）得到 D⊂P²，

\[
\sigma_P^2(D^c)\le w^{a_R/10},\qquad
\sigma_P(T_{P,P'}(r))\le Cw^{-\zeta}r^2\quad((P,P')\in D,r\ge w). \tag{14}
\]

小 P-pair 距离另用 (10) 估计，不把 radial good 自动解释成第一坐标差非零。特别，不能只因 V 前两坐标可反解，就称未经 uniform refinement 的 multiset P 满足 22.2。

## 7. weighted Kaufman **law** 引理及完整证明

以下自包含小引理替代 Lemma22.3 的 multiplicity 接口。固定 bounded box。设 µ 为 R³ 的任意 probability，Λ 为 R² 的任意 probability（均可带原标签），对 `w≤r≤1` 有

\[
\mu(B_r)\le K_Ur,\qquad \Lambda(B_r)\le K_\Lambda r^2.
\]

令 `π_λ(z)=z₃+λ₁z₁+λ₂z₂`。给定 β>0，若 `K_U K_Λ≤w^(-β/8)`，足够小 w 时，除 Λ 质量≤`w^(β/8)` 的参数外，每个 λ 有原 target 标签事件 E_λ，`µ(E_λ)≥1-w^(β/8)`，并且

\[
 (\pi_\lambda)_*(\mu|_{E_\lambda})(I)\le w^{-\beta}|I|
 \quad(|I|\ge w). \tag{15}
\]

把 restriction 再归一化至 probability 至多额外乘 2。结论控制原标签的质量，而非只数 distinct projected cells。

证明。对 dyadic `q∈[w,C_M]` 考察

\[
I_q=E_{\lambda\sim\Lambda}\iint 1_{|\pi_\lambda(z)-\pi_\lambda(z')|\le q}\,d\mu(z)d\mu(z').
\]

距离≤Cq 的 target pairs 质量≤`C K_U q`。若距离∼r≫q 且 projection difference≤q，由 λ bounded 可知 horizontal difference `|(z₁-z′₁,z₂-z′₂)|≥c r`。允许的 λ 落宽 `Cq/r` 的 strip，有限 box 内可用 `O(r/q)` 个半径 `Cq/r` 的 balls 覆盖；即使该半径与 w 差固定倍，也可用半径 w 扩大。故该参数事件质量≤`C K_Λ q/r`。target pairs 此 shell 质量≤`C K_U r`。求和得

\[
 I_q\le C K_U K_\Lambda q\log(2/w). \tag{16}
\]

令 `T=w^(-β/2)`。在每尺度 q，把原 target 标签 z 判坏当

\[
\mu\{z':|\pi_\lambda(z)-\pi_\lambda(z')|\le q\}>Tq.
\]

由 (16)、Markov 及 O(log(1/w)) 个尺度，(λ,z) joint bad probability≤

\[
R=C K_U K_\Lambda w^{\beta/2}\log^2(2/w).
\]

再对 λ Markov：除质量≤√R 的 λ 外，每个 λ 的 bad-target union 质量≤√R。假设使 `√R≤w^(β/8)`。取其补集 E_λ。任意长度 r≥w 的 I 若碰到 `π_λ(E_λ)`，选其中一个 good 标签 z，再取 dyadic q∼r，使整个 I 包含于以其 projection 为心的 q-interval；good-centre bound 给质量≤`CTr`，足够小 w 时≤`w^-β r`。若不碰则为零。证明完毕。此论证允许 target/parameter 重合像、原加权 atoms，并未使用它们的独立 sampling 或 separation。

## 8. 从 radial 到原 right-time law：所有 charts 与 norm 费用

`µ_U=U_*ν` 自动满足 1-Frostman constant `C_Mw^-η`，因为 U 第三坐标就是原 s；不需要 U 的 Euclidean Lipschitz 性。下面只对 `v=P-P′≠0` 定义 charts；v=0 及小 norm 事件统一由本节末的 (10) 估计删除。对每个 pin P，把 D 中 P′ 按 `i=argmax_j|(P-P′)_j|` 分成 3 个 charts（ties 固定规则）。若该 chart 在 σ_P 下质量小于 `w^(c_ch)`，全部删去；对所有 pins 总损≤`3w^(c_ch)`。

其余 chart 归一化为 probability，记 `v=P-P′`，取 projective coordinates `λ=(v_j/v_i)_(j≠i)∈[-1,1]²`。任意半径 r≥w 的非空参数 ball，任取其中 actual good P′₀；对应 cone 在 bounded P-box 内落 `T_(P,P′₀)(C_Mr)`，故由 (14) 得归一化参数 law

\[
\Lambda_{P,i}(B_r)\le C_Mw^{-\zeta-c_{ch}}r^2. \tag{17}
\]

这给真实 angular law，不要求 slopes 构成另一个 uniform set，也不需要免费固定第一坐标。对 U 坐标同样置换，使 `v·U=v_i π_λ(U)`。有限个 charts 上用 §7，`ζ+c_ch+η<β/8` 保证合法。平均回原 `σ_P²`，只额外删≤`w^(β/8)` 的左 pairs；每个剩余 v 的原右时间可删≤`w^(β/8)`，其余 right-time pushforward law 满足 (15)。

另删 `|v|<w^(q_n)`，由 (10) 总损≤`K_P w^(2q_n)`，其中 `K_P=Cw^(-2η-u)p^-2g₀^-4`。在余下 chart 中

\[
|v_i|\ge |v|/\sqrt3\ge c w^{q_n}.
\]

所以 **原输出** 的一个 O(w)-interval，对归一 π_λ 的宽为 `O(w/|v_i|)≤Cw^(1-q_n)`。由 (15)，若两个 right-time 标签均 good，则对任意该 interval I，

\[
\nu^2\{v\cdot[U(s_1)-U(s_2)]\in I,\ s_1,s_2\text{ good}\}
 \le Cw^{1-q_n-\beta}. \tag{18}
\]

这里固定 s₂ 后用 (15) 再积分；(18) 是 original right multiplicity 的估计。norm 因子 `w^(-q_n)` 已支付。直接把原文 5517 的分母 `t₁-t₂-t₃+t₄` 当作有下界，不足以推出此式。

## 9. 同一新先验内结束 separated engine

(11) 的 W mass≥p⁸/16。radial bad pairs、light charts、Kaufman bad pairs/right times、small norm 的总质量至多

\[
C\big[w^{a_R/10}+w^{c_{ch}}+w^{\beta/8}+K_Pw^{2q_n}\big]\ll p^8.
\]

这里每项都是对 **σ_P²×ν²** 的绝对质量界，故对 W 的任意相关 restriction 也适用。剩余 W 至少保一半。输出 (12) 仍由 (8) 的 `Cw^(-1+κ-ℓ)` 个 O(w)-intervals 覆盖；(18) 给整个 good W 的质量上界

\[
Cw^{-1+\kappa-\ell}w^{1-q_n-\beta}
=Cw^{\kappa-\ell-q_n-\beta}\ll p^8/32,
\]

最后一不等式由 `q_n=β=κ/20` 及 `ℓ≪κ`、`p≥w^ℓ` 得到。矛盾。这证明 §2 的 separated finite 命题，保留了原 g→balanced H→selected actual pairs→new cycles 的全部质量损失。

## 10. 回到原 scalar Y 与 fine-time：已付和未付分开

原 Step2 的 5315–5335 把 scalar physical Y_j（区间尺度 τ）用 affine ψ 化为 bounded A，以 `w=Cδ^-η′(ρ+ρ^(3+ε₀)/τ)` 覆盖。其原 fine mesh 是 δ/τ，**要先核 `τw≥δ`**；R23 已记录早期 5315 的 `δ≤δ^-η′τρ` 并非一般成立，最终 τw 的另一误差项才可能覆盖 δ。本文不因原文的该局部算式而反驳整主定理。

若**全原Y**在所用 [δ,τ] 尺度保原 `(1-κ,K)` AD 上下界，Y_j 的 fine cardinal lower `K^-C(τ/δ)^(1-κ)` 已付，且 `e=τw≥δ`，则 Y_j 的原均匀 fine-label law 在任一 working w-bin 的质量≤`K^C w^(1-κ)`，occupied bins≤`K^Cw^(-1+κ)`。后一个 cover upper 不能仅凭 fine-point upper 得到：在每个 occupied cell 的实际原Y点旁放半径 cτw 的 balls，分常数颜色使之不交，用**全原Y**的 AD lower 逐球计数，再用常数扩大 τ-patch 的 AD upper 求和；不要求裁切patch自己有新的lower。不能仅凭此 upper capacity 换成均匀 A：还须删质量小于 `K^-B w^(1-κ)` 的 light bins。总删量≤`K^(C-B)`；B 依原 graph density 选足够大。余每 bin 权重在 `K^-B w^(1-κ)` 与 `K^Cw^(1-κ)` 之间，换均匀 bins 只付 `K^C`。对各 bin 保留原 g 的 conditional average；positive average 仍有实际 fine witness，舍入 x 只增 O(w) output 误差。把目标 A₊ 取全部 enlarged target bins，则

\[
\#A_-\le K^C w^{-1+\kappa},\qquad \#A_+\le K^C\#A_-.
\]

这些 K 幂要在原 δ→w 参数中转换，并可把 κ 缩为 κ/2 后应用 §2；不得抹去。边界 bins 可用常数 overlap/扩大区间并选择中心 ball 支付。本文没有为任意 intersection Y_j 免费断言新的 AD lower。

原 `B={ρ^-1z:z∈Z(q)}` 的实际 fine spacing 可为 δ/ρ≪w；`|B|_w≳K^-1w^-1`（5333–5334）只给 covering 下界。F/G 可以在同一 w-timecell 内有大振荡，所以不能用“每 cell 任取一个代表”保存全部 nonfit 与原 g。root 本轮另证的 fine weighted sampling/selection 若同时保留这些输入，才接上本文。选出的新时间先验须重新生成 cycles；不能称每个 sampled atom 还保持原 ν 的质量。

## 11. 审计结论与停止边界

本轮可归档的数学内容是：任意 G 的 small-S 下界；balanced energy 与原边 recovery；带真实 common-neighbor witnesses 的 uniform P 提取；在该新先验内再生 K₄,₂，质量 d₀⁴；weighted Kaufman law、多 charts 与 norm 费用；并由此得到条件于具名高级输入的 separated scalar curvature engine。原 (208) 从 multiset P 直接回原 B⁴ 的 almost-all 写法未在原 Step6–7 中完整付费，本文采用不同但有实际质量记录的修补。

这仍不是整篇 WZ 证明审查结论。本文未重证 13.7 或 AppendixA 的22.2，未免费继承原 fine-time separated-uniform 性，未支付 mixed43 的 whole-matrix AFF₃、large-τ projected stability 或其他原几何分支。下一只核 root 的 weighted fine-time reduction 和整体 engine 合成；不重开旧 frozen 路线，不把本有限门槛称作新的 Kakeya 维数界或重大结果。
