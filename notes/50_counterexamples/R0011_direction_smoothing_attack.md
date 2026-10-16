# R0011：level-dependent shear 保留高 horizon，并将实际可见方向密度降为常数

2026-10-17。作者：`lifting_obstructions`。对象为 N5-DIR-COST-01 的 literal j=3 version2；四维源论文实际 j=2。本稿逐项独核 `audit_four_dimensional` 提出的 foliation shear，并使用 R0010 已独审的统一随机标签引理。本文待本轮独立整合审查；不声称 Kakeya 反例、维数改善、新颖性或重大中间结果。

## 0. 量词、主结果与实际新增输入

固定 L>0、M>6L、α=1/10，令 δ≈N₀⁻ᴹ 为 dyadic，η≈N₀⁻ᵁ，U>M+L+10。M、U 在每个 exact sequence 内固定；最后在不同 sequences 之间任取大的固定 M，不令 M 随 N₀ 发散。

本稿核验：存在单 world、完整八系数 finite-piece tempered 概率 prior，native 为 w、原 selected mass 为1/4，满足

\[
 f(r)=0\quad(0\le r\le L),\qquad S=1,\qquad
 \left\|\frac{d\nu_V}{dV}\right\|_\infty\le C_\alpha,
 \qquad \frac M6\le H\le M.                 \tag{0.1}
\]

因而可固定 d₀=1/2、angular 参数、L=1、κ=0，而 H/(L+κ) 随固定 M 无界。只要求**实际可见三维 slope marginal** 的 N₀^{κ+o(1)} ceiling，仍不足以得到常数独立于 tempered complexity exponents 的 H≤C(L+κ)。这不使用 f 的常数平移、world 权重平均或小质量 prior 的免费正规化。

与 HOR-002 的实质差别是：每个 level 沿 Y₂ 加 αλt，使 level 参数进入第三个独立可见速度方向，同时 exact base 继续定位 level。其作用不能归结为全族共同的一个 affine 坐标变换。每层各自的 shear 却恰好只改变 plank 的 affine center，故单层 cap 保持原 J。随机标签的统一引理必须对**新的层 priors** 重新应用，不能无证明沿用 R0010 旧表中的具体好 tags。

## 1. 同一个原概率 prior 与精确 foliation

独立均匀选择四个格点参数

\[
 \lambda,s\in[1,2]\cap\delta\mathbb Z,
 \qquad p,q\in[-1/10,1/10]\cap\delta\mathbb Z.
\]

indices 共 Nδ≈δ⁻⁴ 个，每个质量≈δ⁴；λ 的边缘质量 πλ≈δ。设

\[
 b=(s,-sq-\lambda p/s,\lambda/s),\qquad
 u=(p,\alpha\lambda-pq,q).                 \tag{1.1}
\]

对全部 t∈[0,1]，直接展开得

\[
 t(b_2+t u_2)+(b_1+t u_1)(b_3+t u_3)
       =\lambda(1+\alpha t^2).             \tag{1.2}
\]

取 ξ、ζ 为互独立的 U[-δ,δ]³，记 B=b+ξ、V=u+ζ、Y(t)=B+tV。固定一张稍后选择的 color table (cλ)，其中 cλ∈[0,1]。再独立取 e∼U[-η,η]、W∼U[η,2η]，令

\[
 w_0=c_\lambda+e,\qquad w(t)=w_0+tW.       \tag{1.3}
\]

条件在 λ 后，visible block、e、W 独立；完整 hidden 与 visible blocks 经 λ 耦合。λ 是单 world 的内部 index，不能观察到。tags 一次性固定以后，prior 中没有额外随机 color 变量。

以 ν 表示上述原概率，取 dμ=1_{I₀}(t)dνdt，I₀=[1/2,3/4]，故 μ 总质量1/4。native P*=w，B_derivative=1；原 native bound、Pw=1、Pww=0 以及 visible 原始系数界均为固定常数。

## 2. 完整八维 tempered prior：通过

固定一个 index 后，(B,V,w₀,W) 是完整八维矩形盒上的常密度。每个 index 的 density 贡献不超过

\[
 C\delta^4\delta^{-6}\eta^{-2}
       =C\delta^{-2}\eta^{-2}.             \tag{2.1}
\]

重叠数为固定常数：B₁、V₁、V₃ 依次把 s、p、q 限在 O(δ) 区间；固定 s 后，B₃=λ/s+O(δ) 又把 λ 限在 O(δ) 区间。新的 V₂ 条件只会进一步减少重叠。因此 (2.1) 是实际 full8 density ceiling，不只逐 index ceiling。

保留内部 indexed copies 时有 O(δ⁻⁴) 个盒；若合并为普通 density，把全部 coordinate facets 共同 refinement，固定维数下仍只有 N₀ 固定幂个线性 semialgebraic pieces。全部逆噪声尺度、密度和 pieces 数均为 N₀ 的固定幂。源 Definition 2.2 没有限制固定实 tags 的代数高度，选定随机方法产生的有限表合法。

## 3. 实际可见 slope density：κ=0，且常数独立于 M、U

连续参数映射 (λ,p,q)↦u 的 Jacobian 矩阵为

\[
 \begin{pmatrix}0&1&0\\ \alpha&-q&-p\\0&0&1\end{pmatrix},
 \qquad |\det|=\alpha.                    \tag{3.1}
\]

但单算 Jacobian 尚不足以证明 noisy grid prior 的实际密度界，以下直接计数。

对任意固定 velocity point v，|v−u|∞≤δ 先由 v₁、v₃ 将 p、q 各限在 O(δ) 区间，即各 O(1) 格点。固定 p,q 后，v₂=αλ−pq+O(δ) 将 λ 限在长 O(δ/α) 区间，所以只有 O(1+α⁻¹) 个 λ 格点。s 不影响 u；将所有 s 的原概率求和后，每个 (λ,p,q) 的权为 O(δ³)。ζ 的 density≤Cδ⁻³，于是

\[
 \boxed{\displaystyle
 \frac{d\nu_V}{dV}(v)\le C(1+\alpha^{-1})=C_\alpha.}
                                                        \tag{3.2}
\]

该式对任意颜色表、δ、η 成立，常数不依赖 M、U。这里使用原概率的实际三维 velocity marginal；没有先按 level 正规化后再错误删除 πλ。α 固定后 Cα=N₀^{o(1)}，所以命题 N5-DIR-COST-01 的 κ 可以真正取0。

## 4. 原 observation profile 与全部 angular 尺度

记 Q(t,Y)=tY₂+Y₁Y₃，F_t=1+αt²∈[1,1+α]。全部系数有固定界，(1.2) 给

\[
 |Q(t,Y(t))-F_t\lambda|\le C\delta.       \tag{4.1}
\]

因此任意 fixed exact (t,Y) 只可能有 O(1) 个 contributing λ。特别地，这个 level 定位在原 observable base 内发生，不需要把内部 λ 作为 world 或 output label。

### 4.1 可见 g_t≤C 与实际 f(r)=0

固定 t∈I₀、λ、s，near-Y₁ 和 near-Y₃ 分别给

\[
 s+tp=Y_1+O(\delta),\qquad
 \lambda/s+tq=Y_3+O(\delta).
\]

t≥1/2，故 p、q 各 O(1) 候选，s 共 O(δ⁻¹) 个。结合 contributing λ 只有 O(1) 个、单 index 的 Y-density≤Cδ⁻³ 及原质量≈δ⁴，得 g_t(Y)≤C。可见 support 体积也有固定界。

设 a_r=N₀⁻ʳ，0≤r≤L。每个 contributing λ 的 w(t) 都落在 cλ+[-η,3η]，η≪a_L≤a_r，故至多碰 O(1) 个 hidden a_r-bins。于是实际 `(t,Y,[w]_{a_r})` density G_r 与其 reference support 满足

\[
 G_r\le C,\qquad
 |\operatorname{supp}G_r|_{dt\,dY\times\#\text{bins}}\le C.
\]

直接积分给 μ{G_r<K⁻¹}≤C/K。取 K=N₀^τ 就得到源定义的双侧 typical density exponent

\[
 \boxed{f(r)=0\quad(0\le r\le L).}         \tag{4.2}
\]

这里没有宣称支撑中每一点有固定 lower；只证明按实际原 μ 抽样时低密度点的质量小。对有限 prepared depths 可 union bound。cap-class 的 density 条件对任意固定 0≤d≤d₀<1 成立，如需严格 d>0，固定 d=d₀=1/2 即可。

### 4.2 Joint-angular cap：S=1

令 ρ∈(0,1]，Jρ 是一个三维 velocity bin。对 ρ≥δ，contributing λ 仍 O(1)；V₁ bin 与 near-Y₁ 把 s 限在长 O(ρ) 区间，共 O(ρ/δ) 格点，固定 λ,s 后 p、q 仍各 O(1)。所以

\[
 g_{t,\rho}(Y,J_\rho)
 \le C\delta^4(\rho/\delta)\delta^{-3}=C\rho.
\]

对 ρ<δ，V₁、V₃ 与 near-Y₁ 使 p,q,s 各 O(1)；λ 仍 O(1)。单 index 的 (Y,V) density≤Cδ⁻⁶，积分 velocity bin 再乘 δ⁴，得

\[
 g_{t,\rho}(Y,J_\rho)
 \le C\delta^{-2}\rho^3\le C\rho.        \tag{4.3}
\]

加入任何一个 hidden observation bin 时，逐 index 的 hidden conditional probability≤1，故相同 upper 仍成立。n(L)≈log1，所以 terminal joint-angular 条件可固定 S=1；该证明涵盖全部正 ρ，因而 angular depth 参数也可固定，完全不依赖 M、U。不能把 hidden 与 visible 无条件独立作为理由；正确理由是条件后 bin 概率≤1。

## 5. 原 J 的单层全宽度 cap 保持不变

固定 λ，新 layer 与 R0010 old layer 有精确关系

\[
 Y_{\rm new}(t)=Y_{\rm old}(t)+\alpha\lambda t e_2.
                                                        \tag{5.1}
\]

使用同一个 s,p,q,ξ,ζ 作 coupling 即得 (5.1)，没有近似误差。对任意 block I、矩阵 D、affine center y_c(t) 与 slack K，新 layer 的 whole-block fit 事件恰等于 old layer 对 center y_c(t)−αλt e₂ 的 fit 事件。D、q、K 与 J=|detD| 全部不变。

R0010 §5 已对 λ∈[1,2] 的旧 layer 证明统一全正宽度 cap；其基础是 R7–R8 的自包含 quadric plank estimate 与 full6 smoothing。故本模型直接得到

\[
 \pi_\lambda\nu_{\lambda,\rm new}(G)
 \le CK^3\delta^{1/2}q^{-3}J.             \tag{5.2}
\]

这里 πλ≈δ 已乘回原 prior；若使用 conditional-on-λ 的概率，右边应是 δ⁻¹/²，不可混用。由于 pullback 只改 affine center，任意旋转框、任意中心、任意 positive axes widths，以及短块 q 的 q⁻³ 成本，都正好由原 lemma 覆盖。不是从 visible slope density (3.2) 推出的各向异性估计。

## 6. 对新层 priors 重选统一好标签，给 H≥M/6

调用 `R0010_uniform_random_level_labels.md` 的 RL4。该引理的证明对层分布是 distribution-free：条件只有独立随机 tags cλ、每层的其余概率 Πλ 与自身 cλ 无关，以及 fixed-dimensional bounded-degree chart predicates。G 是 whole-block visible fit，H 是 G 加当前 selected time、二次 small-value 与 hidden derivative 下界。

新的 Πλ 只把 visible coefficients 的中心按 (5.1) 改变；各层的 e、W 仍独立于 tags，G 仍由两 endpoints 的 convex norm fit 表示，current predicates 仍为同样固定次数。先于 tags 的 quadrature、fixed-dimensional polynomial patterns、ghost/swap 及一元 quadratic sublevel 证明均适用。特别是允许任意事后选择的 P、D、center、block、K，不是只对预备 predictor 成立。

**在这些新 Πλ 上重新选择一张好 color table。** 并不要求 R0010 具体旧好表继续有效。对新固定表及所有 chart 参数，RL4 给

\[
 \frac mq\le C K^2a\,\nu_{\rm vis}(G)
 +C_M(\log N_0)^2\max_\lambda
       \{\pi_\lambda\nu_\lambda(G)\}+r_N,
                                                        \tag{6.1}
\]

r_N 比 N₀ 的任意固定负幂小。quadrature 仅作分析工具，不增加实际 prior 或 labels 的 tempered complexity。

若实际 chart 有非零 selected mass，其 block 与 I₀ 相交；取 t*∈I∩I₀，whole-fit 将 Y(t*) 限在体积≤CK³J 的椭球中。由第4节 g_t≤C 与 (5.2)，(6.1) 化为

\[
 \frac mq\le CK^C
 [a+(\log N_0)^2\delta^{1/2}q^{-3}]J+r_N.  \tag{6.2}
\]

对 true terminal chart，实际 n(L)≈log1，其 floor 为 m/q≥K⁻¹J，K=N₀^{o(1)}。tempered 条件给 J≥N₀⁻ᴮ，其中 B 沿 exact sequence 为固定有限数，故 r_N/J 仍 superpolynomial small；K^Ca→0。两式比较迫使

\[
 q^3\le N_0^{o(1)}\delta^{1/2},\qquad
 \boxed{H\ge M/6.}                       \tag{6.3}
\]

任意复杂 assignments/selection 已扩大为 H 事件，所以没有遗漏任意定义的实际 packet。原坐标 further incidence submeasure 仍被原 νdt 支配；inverse-subpower selection 不改 typical exponent，任意 subsequence 不改固定幂，故与源 horizon 的 inf 量词兼容。该步骤只重用已独审的一致随机标签 lemma，并已重新核验它在新 prior 上所需的两个数值输入 g_t≤C 与 (5.2)。

旧模型的特殊二次消色式不能直接套用：若 h(cλ)=λ，旧式 Q−h(w) 在此多出 αλt²；写成 Q−(1+αt²)h(w) 则一般超过 total degree2。但这只是检查一个旧 shortcut，绝不据此宣称排除了全部二次式；真正的统一排除由 (6.1) 完成。恒定 tags 当然仍给 P=w−c 的 H=0，所以好表的存在步骤不可省略。

## 7. 同一模型的有限 true atlas：H≤M，且实际 own-list 为常数

这一节不调用 generic completion。将 I₀ 划为 q=δ 的完整 dyadic blocks，忽略 O(δ) 端块。固定 block I、midpoint t_I，按 midpoint Y(t_I) 所在 δ-cube Q 与原 w₀ 的 terminal a-bin C 作完整轨道 assignment

\[
 A_{I,Q,C}=\{Y(t_I)\in Q,\ w_0\in C\}.    \tag{7.1}
\]

由 (4.1) 以及 F_{t_I}≥1，固定 Q 只可能有 O(1) 个 λ，各层 w₀ 支撑只碰 O(1) 个 C。因此每个 block 参与 pairs 至多 Cδ⁻³；又由 g_{t_I}≤C，每个 pair 原质量≤Cδ³。

删除质量<τδ³ 的 pairs，原 prior 坏质量每 block≤Cτ。固定充分小的 τ 后，所有留下的 pairs 有

\[
 \tau\delta^3\le\nu(A_{I,Q,C})\le C\delta^3,
                                                        \tag{7.2}
\]

并保留固定正质量。这里不声称每个 occupied bin 自动有 lower；lower 是明确删轻后得到的。

取 center 为 Q 中点、D=C₁δI₃。V 统一有界，故所有 assigned trajectories 在整个 I 都满足 spatial fit，且 ||D||≤Kq，J=C₁³δ³。取 P=w−c_C，其中 c_C 为原 w₀-bin 中点，则整个 I 上 |P|≤a/2+2η，Pw=1、Pww=0。selected incidences 为全部 good assignments 在 I 内的时间，故 m/q=ν(A)≥τδ³≥K⁻¹n(L)J。扩大固定 K 后得到每个实际 packet 的完整 floor，总覆盖可取≥1/8。

当前 exact t,Y(t) 与统一 V 界将 midpoint cube Q 限在 O(1) 选项；当前 [w(t)]_a 与 |w₀−w(t)|≤2η 将原 C 限在 O(1) 选项。因此真实 terminal/own-depth observation 给 label (I,Q,C) 的 O(1) 列表，不输出 λ、noise 或内部轨道 index。

所有 assignments 为线性 bin 条件，good-pair 删除为有限常数表；blocks、pairs、labels 总数至多 Cδ⁻⁴，frame inverse 与全部尺度为 N₀ 固定幂。故这是合法 tempered true terminal atlas，

\[
 \boxed{H\le M.}                         \tag{7.3}
\]

本证明保留原概率，没有 good-cell 内正规化；与第6节同一张已固定好表及同一 selected event 配套。上界用来排除无 true system 的 vacuity，不声称任意进一步删选后自动保留各原 pair 的 floor。

## 8. 对 N5-DIR-COST-01 的严格否定范围

固定 L=1、d₀=1/2、S=1 与 angular depth 参数。对任意固定 M>6，先固定 U>M+L+10，再沿 N₀→∞ 构造上述 exact sequence，逐 N₀ 选一张第6节的好表。由 (3.2)，同一个实际可见 slope ceiling 为 Cα=N₀^{o(1)}，即 κ=0；而

\[
 \frac{H}{L+\kappa}\ge M/6.
\]

任意假定只依赖 d₀、S、angular 参数的有限 C，都被足够大的固定 M 否定。没有在单个 sequence 内使用无界 complexity exponent，也没有把 M 的依赖藏入 κ。

完整 raw 四维 slope (V,W) 的 density 则仍含 η⁻¹：W 与 V 独立且均匀于宽 η 区间，故 f_{V,W}=f_V/η，其 ceiling 至少 cη⁻¹、至多 Cαη⁻¹。可见三个方向分量的常密度不等于全部四个原始 slope 分量的常密度。因此本模型不保留五维 Kakeya 所需的原始 full-direction 来源，不反驳四维 j=2 源定理，也不解决 n≥5 Kakeya。

本轮数学验收是排除仅 visible-direction-cost 的 uniform completion 命题；其复杂度独立版本不能作为高维研究后端输入。本稿不据此建议继续给同一 completion 模板追加同义条件；宏观路线处置由 root 统一归档。

## 9. 次要边界：为什么独立 copies 的方向平滑通常失败

这是新 foliation 机制之前独立尝试的可复核排除，不作为主反例的输入。仍取旧 HOR-002，限制 q∈[1/20,1/10]，沿 x-direction slope 加 a_j e₁。令 spacing Δ≈δN₀^κ，K_c≈Δ⁻¹ 个 copies 均匀混合。每个 copy 继续使用同一套 cλ，或对每 copy/level 独立取 colors。

原 visible velocity density≤C/(K_cδ)≈N₀^κ：V₃ 定 q，V₂=−pq 因 q 远离0而定 p，V₁=p+a_j 再定 copy。但 fixed base 满足

\[
 |Q(t,Y)-t a_jY_3-\lambda|\le C\delta.
\]

在 I₀ 与 Y₃≥c 的实际支撑中，每个 fixed λ 只能由 O(1) 个 copies 贡献，因为 Δ≥δ。因此若 bλ(t,Y) 表示共享该 color 的 base density，则

\[
 \sum_\lambda b_\lambda=g_t\le C,
 \qquad \max_\lambda b_\lambda\le C/K_c.  \tag{9.1}
\]

独立均匀 cλ∈[0,1] 时，令 G_a(t,Y,B) 为实际 hidden a-bin density。条件在 base 后不同 colors 仍独立；不同 colors 落同 bin 的概率至多 Ca，而同一 color 的 diagonal term 由 (9.1) 控制。逐 bin 平方、积分给

\[
 \mathbb E_{\rm tags}\int\sum_B G_a^2\,dt\,dY
       \le C(a+K_c^{-1}).                \tag{9.2}
\]

噪声厚度 η≪a 只改变常数：每个 color 的 conditional bin probabilities 和为1，单 bin 上其 tag 平均≤Ca。于是对任何 τ>0，按原 incidence 质量计

\[
 \mathbb E_{\rm tags}\mu\{G_a>N_0^\tau a\}
 \le C N_0^{-\tau}(1+(K_ca)^{-1}).       \tag{9.3}
\]

若 M−κ>L，则 K_ca_L→∞。Markov 与有限容差/尺度对角选择给典型颜色表的 n(r)≈log a_r；另一侧只用 bounded base、hidden support 和至多 C/a_r 个 bins，积分得到 μ{G_{a_r}<N₀^{-τ}a_r}≤CN₀^{-τ}。特别 endpoint 为 f(0)=0、f(L)=L，违反任何固定 d≤d₀<1 的 C(d) 条件。对每 copy/level 独立 colors 也有更细 component 的 max≤C/K_c，同一计算仍成立。

所以这种独立 copies 不能把旧 κ=M 的高 horizon 模型免费变成 κ=0、d<1 模型。第1节的 level-dependent shear 解决的是不同问题：它使 level 本身成为缺失的速度参数，同时仍由 exact base 定位该 level，并不混入 K_c 个无法从 base 消除的独立颜色。这正是第4节 profile 保持 f≡0 的原因。
