# R0012：非标准空间仿射 lift 的构造攻击与核约束

> **R0050范围更正（2026-10-17）：** 下文保留开轮/历史论述。对目标 `w+F(t)y`，在同一个参数点沿同一条lift直线取第一变分，可构造同codimension和方向rank的真正全时affine lift。因此一般smooth与affine的**存在性等价**，旧文“空间affine为实质限制/一般nonlinear未排除/需逼原π affine”的判断不再成立；原π本身仍可真正非线性。完整更正见 [R50主证明](R0050_variational_equivalence_and_full_smooth_lift_classification.md)，当前登记为 `results/reviewed/LIFT-005_full_smooth_variational_classification.md`。不新增ID或重大性声明，换clock/selector/Θ依赖w等边界保留。

2026-10-17。作者：`lifting_obstructions`。对象：N5-CURVE-LIFT-01，B=diag(1,2)，保留原时钟、空间仿射的 (1,0)-lift。独立核查结论：非标准光滑 T(t) 与非线性参数化不能绕过障碍；下文证明全部指定类均不可能。另核 root 提出的自然 rank-one 补充分类。已由audit_four_dimensional交叉独审通过，见research/reviews/R0012_construction_attack_review.md；不声称新颖性、Kakeya 维数改善或重大中间结果。

## 1. 一手定义及本轮量词

核对本地 `literature/extracted/nadjimzadah_2026_curved_to_linear_lifting_v1.txt` 的 Definition 2.1、Proposition 2.2 与 Proposition 2.5(i)：

- 方向 Θ(y,ρ) 不能依赖 intercept w；intercept a(y,w,ρ) 可以任意光滑依赖全部参数，未要求线性。
- 每个固定 (y,w) 的**整个 ruling 参数域** ρ 都必须投影到同一条曲线；不是每个方向只挑一个有利 ρ。
- 对 n=3、s=1、ν=0，D_(y,ρ)Θ 是3×3满秩矩阵。不能仅要求 Θ_y 秩2，也不能把截距参数误算作方向参数。
- 一般定义允许任意光滑 submersion；本轮额外限定 π_t(z)=T(t)z+c(t)、rank T(t)=2、原时钟不变。故这里的否定不覆盖一般空间非线性 π。

标准 quadratic construction 使用 rank factorization B=UV，得到 s=rank B、direction loss ν=rank B−rank B²。对 diag(1,2)，它给 (2,0)-lift 到 R⁵。源文没有仅凭该构造宣称任意其他 lift 的最小 s 必为2；本轮必须处理整个指定的任意光滑空间仿射类，不能把标准 rank 公式当作排除证明。

设时间 I 含0，参数在有内点的 product domains 中变化，并假设

\[
 T(t)\{a(y,w,\rho)+t\Theta(y,\rho)\}+c(t)
   =w+(tI_2+t^2B)y.                       \tag{1.1}
\]

下面只在一个内点取参数导数，故不依赖边界或全局参数单射。需要的 T、a、Θ 光滑性远少于题设；没有假设它们关于参数线性。

## 2. 任意 T 都被共同右逆正规化，而非预设标准形

在任一固定参数内点 P，令 M=∂_w a(P)，是3×2矩阵。对 (1.1) 求 w 导数，因 Θ 与 w 无关，得到

\[
 T(t)M=I_2\qquad(t\in I).                 \tag{2.1}
\]

因此 M 是全部时间共用的右逆，秩2。这是从 exact/coherent identity 推出的必要条件，不能以每个 t 自选不同右逆替代。

选非零 k₀∈ker T(0)，则 S=[M,k₀] 为可逆3×3常矩阵：若 Mv+rk₀=0，左乘 T(0) 得 v=0，再有 r=0。用 z=S z̃ 作**常数**空间线性坐标变换，a、Θ 同时左乘 S⁻¹，方向满秩与 Θ 独立 w 都保留。于是可合法写成

\[
 T(t)=[I_2,g(t)],\qquad g(0)=0,            \tag{2.2}
\]

而不是一开始假定 T=[I,tU]。非标准性仍完整保留在任意光滑向量函数 g(t) 中。

把 a=(a_{12},a_3)、Θ=(Θ_{12},Θ_3) 代入 t=0 的 (1.1)，得

\[
 a_{12}(y,w,\rho)=w-c(0).                 \tag{2.3}
\]

所以 a₁、a₂ 的参数依赖已被真正的原时钟恒等式固定；第三分量 a₃ 仍可任意非线性。c(t) 没有被假定为零，以下参数导数会消去它。

## 3. 攻击非标准 g(t)：ρ 核向量强制所有 g 共线

仍在固定内点 P 取导数，记

\[
 h=\partial_\rho a_3(P),\quad
 b=\partial_\rho\Theta_3(P),\quad
 r_\rho=\partial_\rho\Theta_{12}(P),\quad
 k=g'(0).
\]

ρ 不改变右边的曲线。对 (1.1) 求 ρ 导数、使用 (2.3)，得到对全部 t 的精确向量恒等式

\[
 (h+t b)g(t)+t r_\rho=0.                 \tag{3.1}
\]

在 t=0 求一次 t 导数，得 rρ=−hk，因此

\[
 (h+t b)g(t)=t h k.                      \tag{3.2}
\]

先检验不能除的情形 h=0。此时 rρ=0；满秩 D_(y,ρ)Θ 迫使 Θρ≠0，故 b≠0。(3.1) 因而给 g(t)=0 对所有非零 t 成立，连续性再给 g≡0。将 (1.1) 求 y 导数，便有

\[
 t\,\partial_y\Theta_{12}=tI_2+t^2B,
\]

其在一个开时间区间内成立只能 B=0。因此针对本轮 B≠0 的情形，必有 h≠0。

令 β=b/h。缩小含0的时间邻域，使 1+βt≠0，(3.2) 给

\[
 \boxed{g(t)=\frac{t}{1+\beta t}\,k.}     \tag{3.3}
\]

若 k=0，则局部 g≡0 又迫 B=0；故 k≠0。由此任意光滑 T 的剩余变化在局部只能沿一个固定空间向量 k；旋转 kernel、非线性 ρ 重参数或第三分量的非线性变化都没有提供第二个弯曲方向。

取非零 row n∈(R²)* 满足 nk=0，(3.3) 给 ng(t)=0。对原 (1.1) 求 y 导数再左乘 n；c 已消掉，a₁₂ 的 y 导数由 (2.3) 为零，于是

\[
 t\,n\partial_y\Theta_{12}=t n+t^2 nB.
\]

对小的非零 t 除 t，再比较任意两个 t，得到 nB=0，故

\[
 \boxed{\operatorname{rank} B\le1.}       \tag{3.4}
\]

diag(1,2) 的秩为2，矛盾。这已经解决主任务；没有依赖标准 x+tUz 构造，也没有只排除某个候选表达式。

## 4. 自然补充的独立检查：rank-one nilpotent 也不满足满方向秩

root 提出同一计算的自然完整分类：B=0，或 rank B=rank B²=1，恰为存在该类 (1,0)-lift 的2×2矩阵。下面独立核验这一补充，并不另开更广分类主任务。

继续假设 B≠0。令在 P 的 y 导数为 rows R=∂_y a₃、L=∂_yΘ₃，矩阵 D=∂_yΘ₁₂。对原恒等式求 y 导数，并使用 (3.3)，除 t 后在 t→0 时得到

\[
 D=I_2-kR.
\]

对所有足够小的非零 t，代回同一式得

\[
 B=\frac{k(L-\beta R)}{1+\beta t}.        \tag{4.1}
\]

B 是非零常矩阵，故 (4.1) 迫 β=0。因此 b=0，而且 (3.2) 现在对全部 I 给 g(t)=tk；没有遗留远离0的分母零点。记 ℓ=L，则

\[
 B=k\ell,\qquad
 D_{(y,\rho)}\Theta(P)
 =\begin{pmatrix}I_2-kR&-kh\\\ell&0\end{pmatrix}.
                                                        \tag{4.2}
\]

该矩阵分解为

\[
 \begin{pmatrix}I_2&-k\\\ell&0\end{pmatrix}
 \begin{pmatrix}I_2&0\\R&h\end{pmatrix},
\]

所以其 determinant 恰为 h(ℓk)=h tr B。满秩又有 h≠0，因而 tr B≠0。对 rank-one B，恒等式 B²=(tr B)B 说明这等价于 rank B²=1。

充分性也完整可验：

- B=0 时，取 T=[I₂,0]、c=0、a=(w,0)、Θ=(y,ρ)，则 DΘ=I₃。
- B=kℓ、ℓk≠0 时，取 T(t)=[I₂,tk]、c=0、a=(w,ρ)、Θ=(y−kρ,ℓy)。投影恰为 w+ty+t²kℓy，且 det DΘ=ℓk≠0。

因此，在本轮保留时间/空间仿射/Θ独立 w 的类中，严格分类为

\[
 \boxed{B=0\quad\text{或}\quad
        \operatorname{rank}B=\operatorname{rank}B^2=1.}
                                                        \tag{4.3}
\]

这与 Proposition 2.5(i) 的 rank-one 充分构造一致；新增必要性来自共同右逆及 coherent ρ 核约束。特别地，仅 rank B≤1 尚不够，非零 nilpotent rank-one B 的方向秩只能欠一维。

## 5. 对潜在漏洞的逐项检查

**每时刻不同右逆。** (2.1) 的 M 来自一个固定参数点的 w 导数，天然与 t 无关。没有以任意 rank T=2 单独推出共同右逆；真正使用的是 Θ 不依赖 w 的原量词。

**非线性 a、Θ。** 正规化只做一个常数空间基变换，随后只在同一参数内点取导数。h、b、R、L 是该点的数值，不要求对其他点相同。由于同一个 T(t) 必须对该点的全部 t 成立，一个点已经足够施加 (3.2) 和 (4.1)。没有先把所有参数化线性化再错误地忽略高阶项。

**ρ 对曲线可有影响。** 本轮禁止这种改变，因为源 Definition 2.1 要求 π(L_{y,w,ρ})=γ_{y,w} 对整个 ρ 域成立。若允许不同 ρ 对应不同 y 或 w，则 (3.1) 的右边不再为0，已换了问题。只取一个 ρ-selector 也不能保证升维后的方向满秩。

**c(t) 任意光滑。** 它在 w、y、ρ 导数中都消失；t=0 时仅用 a₁₂=w−c(0)，没有把 c(t) 任意时间变化当作额外曲率信息编码 y。

**t=0 与除 t。** 原恒等式对含0开区间成立，先取导数/极限确定系数，再只对非零 t 除 t。(3.3) 只需局部小区间；主矛盾是局部的，远处 1+βt=0 不会逃避。自然补充又证明 β=0，彻底消掉该分母问题。

**换时间 origin。** 本题已指定 I 含0，F(0)=0、F′(0)=I₂，因此原点正规化直接合法。若仅技术上将一个 regular 时间 t* 平移为 s=t−t*，先作 intercept 参数 w′=w+F(t*)y，线性项变成 A=I₂+2t*B；当 A 可逆时，再置 y′=Ay，新的 quadratic matrix 为 BA⁻¹，秩仍为 rank B，方向满秩亦保留。不能只平移 t 却遗漏 F(t*)y 或 A。对本题不需要这项扩展，也没有以非线性时间换元改变主类。

**标量 B 的时间换元。** B=bI₂、b≠0 时本类仍被 rank2 排除；但 τ=t+bt² 在小区间可将曲线写成 w+τy。这改变了原时钟，不与本结论冲突。不能将这种标准例外误说成一般空间非线性 π 或任意重参数的否定。

## 6. 研究边界及下一步审查

结论严格排除 n=3、B=diag(1,2) 的任意光滑、原时钟、空间仿射 (1,0)-lift，包括任意非线性 a、Θ。对于一般空间非线性 submersion，以上共同矩阵右逆及 kernel 论证不再适用；本轮没有排除它。对于时间重参数也没有否定。

Proposition 2.2 的方向始终是 d_Kak(X)≥d_lin(n+s−ν)−s。标准本例的 (2,0)-lift 需要五维线性输入；若存在四维 (1,0)-lift，它也只会以四维输入导出一个三维曲线结果，而不会逆向解决五维 Kakeya。本轮的指定类排除使这一边界更清楚，不提供新欧氏 Kakeya 维数界。

root 的无除法系数证明已交叉审查通过；本稿保留独立的 kernel/局部正规形推导以检查假设和分母边界。该窄类按本轮停止规则归档后即停止细节扩展。
