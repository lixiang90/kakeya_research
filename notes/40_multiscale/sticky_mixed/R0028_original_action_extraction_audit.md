# R0028：共同 time/多角作用提取及闭包门槛

2026-10-17，子任务 A。已读 R28 spec、R27 next target、STATE 和 R18 原 W 提取。R18 已保原 joint observed frame，本稿**不**把重写该 frame算新信息。唯一 main 仍为实际 ell3 AFF₃；以下取得一个同原 g 的有限作用 box，并给后续几项具体提取跳步的严格边界。未得 >2 gain、AFF₃ 或完整 factorized/source 反例。

## 1. 固定的原对象与本稿未重复之处

沿 actual d5/k4/ell3原管、两grain、Φ/ξ及 R18/R27 quotient。A⊂R²_x×R²_ξ在working r下约有r^-2个cells，并有真实多尺度visible fibre upper及UniformA的2-Frostman upper。原 fine time lawν有interval cap K_tℓ（ℓ≥d）。同一 M(t)∈Mat(2,2)满足全矩阵 all-affine nonfit。原 used角 H的概率记µ，差lawπ有slabγ，合法base q₀。

保原 bounded graph

\[
0\le g(a,t,s,\alpha,\beta)\le1,\quad
m=\int g\,d\sigma_A d\nu^2d\mu^2>0,
\]

其中 σ_A 是原 coarse observed reference；不是重新假定原 W endpoints独立。若g>0，有某真实output cell b∈A满足

\[
\|b-a-L_{ts}(\beta-\alpha)\|\le E_0,\quad
L_{ts}=\begin{pmatrix}(t-s)I_2\\-[M(t)-M(s)]\end{pmatrix}. \tag{1}
\]

在 source中 m≥r^O(η)、E₀≤r^(1-O(η))、K_t/K_π≤r^-O(η)。本稿下面所有 copies仍用这些原 ν、µ，不把 distinct differences改成uniform，也不固定一个ψ后暗称κ仍在。

H的 κ-AD lower须另核：R27 light-used构造明确给card、κ-cover upper与slab，不自动给任意heavy subset每点的κ-AD lower。以下提取仅需原slab。若某后续作用定理确需完整AD lower，可另以保g的分块uniform refinement计费；不可先把该lower写成既有事实。该regularization本身不是本轮main成果。

## 2. 同一原 g 的十六边 box：完整质量证明

取同一个a，两原time copies t₀,t₁和s₀,s₁，各两原角 copies α₀,α₁和β₀,β₁。定义

\[
\mathcal B(a,\mathbf t,\mathbf s,\boldsymbol\alpha,\boldsymbol\beta)
=\prod_{i,j,k,l\in\{0,1\}}g(a,t_i,s_j,\alpha_k,\beta_l).
\]

则在 **同一** σ_A×ν⁴×µ⁴ product reference中

\[
\int\mathcal B\ge m^{16}. \tag{2}
\]

证明并非density推出大矩形。对固定a的四变量函数f，令Box_d为每个变量取两copy、所有2^d个corner乘积的积分。`Box_d(f)≥(∫f)^(2^d)`由Cauchy–Schwarz归纳：先对前d−1变量用Jensen把平均平方送入，再引入最后变量z₀,z₁，对非负函数 `f(·,z₀)f(·,z₁)`用d−1步。base d=1为恒等式。取d=4，最后对a用Jensen，即(2)。原g内部全部相关性保留。

这是带共同a、四共同times和四共同原角的有限box。每条边仍为原positive code，故有16个实际output cells `b_{ij,kl}∈A`满足(1)。source中的a是同一coarse observed code，未声称16条路径共享同一个exact fine point或同一条管；误差E₀已记录这一差别。相应原路径配置是按各code原恢复权相乘计数，不是把它宣称为原单个W的m^16比例子集。

### 横截角与真实时间间隔

令 `v=α₁-α₀`、`w=β₁-β₀`。它们是独立原差lawπ的两copy。若 λ≥q₀，原slab upper给

\[
\Pr\{\|v\|<\lambda\ \text{或}\ |\det(v,w)|\le\lambda^2\}
\le C_\gamma K_\pi\lambda^\gamma. \tag{3}
\]

第二项先限定|v|≥λ，条件化v后w距span(v)≤λ，才用原affine slab。取

\[
\lambda=\big(m^{16}/(C_\gamma K_\pi)\big)^{1/\gamma},\quad
g_t=m^{16}/(C K_t), \tag{4}
\]

常数选大并要求 λ≥q₀、g_t≥d。因为𝔅≤1，删(3)坏角只损≤m^16/4。四个time变量任意两相距<g_t的六事件总概率≤C K_tg_t，故也可删≤m^16/4。于是

\[
\int\mathcal B\,1_{|\det(v,w)|>\lambda^2}
 1_{\text{四times两两距}\ge g_t}\ge m^{16}/2. \tag{5}
\]

在原small-loss regime，λ=r^O(η/γ)、g_t=r^O(η)，原d/q₀为固定更细底层，故(4)的合法性由η最后小支付；不是在sub-base沿用slab幂。

此提取不固定v或w，原四角population及其κ参数仍在reference中。若以后只选一个横截frame，则不能继续把它叫positive-dimensional角集。

## 3. 在同一 box 内恢复 matrix-time 作用

记 `ψ_kl=β_l-α_k`。令

\[
X_{ij}=\big(b_{ij,10}-b_{ij,00},\ b_{ij,01}-b_{ij,00}\big),\quad
B_{ang}=(-v,w).
\]

由(1)，

\[
X_{ij}=L_{t_i s_j}B_{ang}+O(E_0),\quad
\|B_{ang}^{-1}\|\le C\lambda^{-2}.
\]

因此同一组三个真实A-output的差恢复

\[
L_{t_i s_j}=X_{ij}B_{ang}^{-1}+O(E_0\lambda^{-2}). \tag{6}
\]

top block是 `(t_i-s_j)I₂`、bottom block是 `-[M(t_i)-M(s_j)]`；不假任何矩阵差满秩。若再恢复secant `S_ts=(M(t)-M(s))/(t-s)`，须另付 `g_t^-1`，error为 `O(E₀λ^-2g_t^-1)`。在η小于固定source精度时仍可控制，但不是免费O(r)。

同一box真实保留两类一致性：

\[
b_{ij,00}-b_{ij,01}-b_{ij,10}+b_{ij,11}=O(E_0), \tag{7}
\]

以及对每固定k,l，

\[
b_{00,kl}-b_{01,kl}-b_{10,kl}+b_{11,kl}=O(E_0). \tag{8}
\]

(8)使用同一M和同一四times的coboundary关系；不是任意非平面D-law自动具备的标签。genericD替换会丢掉这些数据。有限多copy可同样用box CS支付m的固定次幂，但本稿只用(2)–(8)，不将其登记为>2增长。

## 4. 提取后仍缺什么：不能把star/box称为作用闭包

(5)给共同base的有限star及两个方向的作用，但不保证任一output b还能作为下一条同time/角作用的input。尤其不能从 `a+d₁,a+d₂∈A` 推出 `a+d₁+d₂∈A`，或从(7)–(8)得到所有bounded words仍在同一个small observed carrier中。

这个推断有严格有限反例，即使保原线性形式：取M=0、四个不同bounded times、角集合含0,e₁/2,e₂/2；固定base0，令A是该16-edge box的全部 `L_ts(β-α)` 及0。所有star边与(7)–(8)精确成立，但取其中最大正e₁方向增量d，2d不在A。该模型未保whole-M nonfit/source维数，只否定“有限star已是可继续作用的闭包”这一逻辑跳步。

若在此后用globalBSG，balanced D-image subset可以拉回原 `(t,s,α,β)` 的dense relation；但BSG不会自动把它变成一个大Cartesian operator×vector域，或使所有后续words同时在原g正支撑内。以下exact density反例明确这个量词差别。

### density alone不产生大共同作用域

取 U=V=F₂ⁿ，`N=2ⁿ`，关系 `E={(u,v):u·v=0}`。其density为 `(N²+N)/(2N²)≥1/2`。若 `U′×V′⊂E`，则 `span(U′)⊥span(V′)`，所以

\[
\#U'\,\#V'\le2^{\dim span(U')+\dim span(V')}\le N. \tag{9}
\]

故对任意固定ε<1/2，不存在两边都≥N^(1-ε)的complete rectangle。另一方面，每个固定大小的finite box仍有density CS下界，二者不冲突。

(9)不是本轮finite matrix目标的反例：它未提供A、M、ν、H及near-closure。它严格排除仅从原boundedg密度、或一次BSG拉回dense relation，就声称已经得到几乎满维的共同operator×angle action域。若新的几何信息真能迫这种域，必须用(1)的具体matrix-time结构另证。

## 5. 固定times再向角BSG的实际指数障碍

另一看似较小的操作也不是small-loss。固定(t,s)及一个base a后，允许角relation⊂H²的image落A-a，最多N_r(A)≈r^-2。设 `n=#H≈r^-κ`，其conditional图密度为p。即便忽略投影误差、并使用 B_ts的horizontal block注入性，单凭image upper的Cauchy–Schwarz最多给

\[
E(H)\gtrsim p^2n^4/\#A.
\]

按scalar/abelianBSG所需 `\nu_{BSG}n^3` 归一，得到的系数只有

\[
\nu_{BSG}\gtrsim p^2n/\#A
\approx r^{2-\kappa+O(\eta)}. \tag{10}
\]

这是固定正幂，而不是r^O(η)。κ≤1时甚至n²≤r^-2，角pair image近一一完全不违A预算。这里不是对实际energy的上界或说它一定小，而是指出**这项现有计数**无法证明所需small-doubling；额外energy若存在必须来自未冻结的时间结构。固定单ψ则更直接丢掉κ。不能用(10)的小量BSG参数冒充一个small-loss action set。

## 6. He工具的精确接口：哪些不是原作用

本轮重新读已有原文（没有新增下载）：

- `literature/extracted/R0015_he_1611_09639_v2.txt`，PDF3–4，Theorem2/3。Theorem3作用于End(Rⁿ)和X⊂Rⁿ，要求escape所有proper nonzero invariant subspaces，结论是X+X或X+aX增长。
- `literature/extracted/R0015_he_de_saxce_1806_06375_v3.txt`，PDF1–4，Theorem1.1及Def2.1。要求V∈P(G)（Jordan–Hölder无trivial quotient）、所有normal quotient的operator投影cover、escape connected subgroups及X escape submodules；结论是bounded mixed words产生小ball。

原 L_ts 是4×2 map，不直接是End(R²)或End(R⁴)。两种字面补法有真实结构障碍：

1. 把 L_ts补零列为 `P_ts=[[Δt I,0],[-ΔM,0]]∈End(R⁴)`，则对W={0}×R²恒P_tsW=0。因此 He1611 Theorem3的irreducibility条件对每个M都失败。
2. 对Δt≠0取natural shears `U_ts=[[I,0],[-S_ts,I]]`。它们逐点固定vertical W，horizontal quotient R⁴/W也trivial；整个unipotent shear group的该representation有trivial Jordan–Hölder factors，故不在P(G)。He–deSaxcé1.1不能直接套这个lift。

这不是说任何lift或商方法都不可能。可另引同尺度dilations，使两个quotients非trivial；但原g仅控制这些operators作用于 `(ψ,0)` 的相关images，并未给operator×X的Cartesian作用闭包或混合words的small-image upper。改变lift须逐项重新证明这些输入，不能由M nonaffine一句话补齐。

即便直接以secants S_ts∈Mat2作用R²，whole-matrix nonfit也不推出irreducibility：`M(t)=diag(t²,t³)` 在均匀fine time上有all-affine fitcap `C(√h+d)`（看(1,1)的monic quadratic sublevel即够），但全部M及secants都在diagonal proper algebra，保两个coordinate axes。它未给原A/g闭包，不是main反例；只是严格说明这个外部定理条件不能由whole-M非affine/slab角alone推出。

## 7. 本轮 source-law回传与真实缺口

(2)–(8)完全使用原g和共同ν/µ，保四time及四角标签，而不是R18 frame换名、固定ψ或genericD-plane gate。这是一项带实际小幂权重的有限作用提取。原fine标签可能多重，box证明不假r-separated；如果源关系误差是E₀=Kr，逆frame及secant的全部λ/g_t费用都明确。它只在coarse同base上成立，不给exact grain、原tube子族或输出carrier重设ADlower。

尚未支付的可检验下一项是：从这些same-base/time/angle boxes及原(1)的作用，产生足够多**输出可再次作input**的匹配，且bounded words的small-image/quotient控制仍与同一M和原角population相连。当前BSG只保dense relation、(9)排除自动大矩形、(10)排除冻结times后的免费small-doubling、He自然lift还面临精确的invariant/trivial-quotient障碍。

未得>2gain，未构造保全部factorized finite条件的countermodel。若root/B本轮没有另得真正增长或完整反例，应依开轮macro停止本局部action迭代并重选实际输入，不把本稿有限提取或外部工具条件重述称作AFF₃。完整d5/k4/ell3原T/grains及长期Kakeya目标均不丢；无新维数界、真实Kakeya反例或重大性认证。
