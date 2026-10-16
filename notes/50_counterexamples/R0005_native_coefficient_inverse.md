# R0005：原生系数不保留同精度的隐藏斜率；一个可量化逆映射障碍

日期：2026-10-16。独立互补反例：`lifting_obstructions`。状态：以下精确模型与质量不等式有完整证明，待交叉审查；未经外部同行评审。

## 0. 本轮任务与结论范围

任务是检验：已知同一 prior 的原生系数 `(y₀,V,x₀,x₁,x₂)` 的 p-bin，能否将原始隐藏斜率 W 的 p-bin 恢复到 subpower 个选项？不能把原生 X 的小系数熵免费当作原始 W 的小熵。

本轮给出 d<1 的模型，具有完整系数有限半代数先验、真实长仿射轨道、原生界、有限预备表上同一 ν° 的 (6.6) 和 (6.9)。在其每个参与 native p-bin 内，W_p 的剩余熵至少为 `log S−O(1)`；任意 L 元列表的成功概率至多 L/S。额外精度 p/S 是实质需要。

同时证明一项新的正向几何限制：若在**同一坐标和同一 prior**下，W 范围有界，并有源稿的 affine-bin joint cap，则某些大原生二次幅度模型只有幂小总质量。这不能未经坐标核算升级为真实临界路径的排除。

## 1. 精确 full-coefficient 原生模型

固定 `0<d<1`。给定有限个嵌套 dyadic meshes，最细宽度 p_*，选

\[
S\ge2,\qquad p_*\ll S^{-1},\qquad 0<\eta\ll p_*.
\tag{1.1}
\]

S、所有 mesh 倒宽和 η⁻¹ 都要求是原始 N₀ 的固定幂；例如可取 `S=N₀^A,p_*=N₀^{-P},η=N₀^{-M}`，P>A、M>P。dyadic 取整仅改固定因子。

取相互独立的参数

\[
y_0=(y_1,y_2,y_3)\in[0,1]^3,\quad
V_1,V_2\in[0,1],\quad e_1,e_2\in[\eta,2\eta],
\]

以及 c∈[0,1] 的有限层 d-Cantor 常密度近似。定义

\[
V_3=-e_2/S,\qquad w_0=c,\qquad W=Sy_3+e_1,
\]
\[
Y(t)=y_0+tV,\qquad w(t)=c+tW,\qquad 0\le t\le1.
\]

取真正的原生二次式

\[
P_*(t,Y,w)=w-StY_3.
\]

则精确有

\[
X(t)=P_*(t,Y(t),w(t))=c+e_1t+e_2t^2,
\qquad (x_0,x_1,x_2)=(c,e_1,e_2).
\tag{1.2}
\]

因此整个单位时间上 |X|≤2、`P_{*,w}=1`、`P_{*,ww}=0`；base 与可见速度有固定常数界。W 可以有长度约 S 的范围，但 Definition 2.1 的 version 2 并未要求 W 本身 subpower 有界，它要求的是 X 和隐藏导数界。W 及所有系数仍为原始固定幂范围。

从八个独立参数 `(y₁,y₂,y₃,V₁,V₂,c,e₁,e₂)` 到完整八系数 `(y₀,V,w₀,W)` 的映射可逆，Jacobian 绝对值为 1/S。逆映射为 `c=w₀,e₁=W−Sy₃,e₂=−SV₃`。故有限层 Cantor 与其余常密度盒推前后，是全八维系数上的分段常 Lebesgue 密度；高度、pieces 数、所有支持谓词及逆映射均满足原始多项式有限性。这里没有以奇异参数图冒充完整系数 prior。

## 2. d<1 隐藏轮廓与同一个 ν° 的系数箱双边界

### 2.1 有限 Cantor 和同一未归一化删除

取第 L 层 Cantor 近似，层长 ℓ≪p_*，层数 `L=O(log N₀)`。对所有预备 p≥p_*，其区间上界为 Cp^d，占据的对齐 p-bin 数至多 Cp⁻ᵈ。

仅在 c 变量上，跨所有预备 p 迭代删除当前质量小于 `τp^d` 的 c-bin。每个箱最多删除一次，总删失至多 CGτ。所得同一测度 λ° 不归一化，质量可保留至少 9/10，并在每个仍参与的预备 c-bin C_p 上满足

\[
\tau p^d\le\lambda^\circ(C_p)\le Cp^d.
\tag{2.1}
\]

G 是预备表大小；若需要 K 为切线 subpower，必须按 PRI-001 保留 G 与 τ 的相容选择。λ° 仍是有限区间上的分段常密度。

令 ν° 是把原始 prior 的 c 测度替换为 λ° 的**未归一化**长线 prior；其余参数完全不变且独立。所有保留轨道都有完整单位时间占据。

### 2.2 (6.6) 在这个模型中几乎是乘积恒等式

对任意预备 p≥p_*，e₁、e₂ 全落在同一个正 p-bin 内，V₃ 全落在同一个负 p-bin 内。V₁、V₂ 是 unit-square 均匀参数，所以其 palette bin 质量为 `π(J)=p²`，边界用半开 dyadic bins。

每个参与的完整 native 系数箱 B_p 因而满足

\[
\nu^\circ(B_p)=p^3\pi(J)\lambda^\circ(C_p).
\]

结合 (2.1)，得到同一个 ν° 上

\[
\tau p^{3+d}\pi(J)\le\nu^\circ(B_p)
\le Cp^{3+d}\pi(J).
\tag{2.2}
\]

并未在箱内重新归一化。删除只依 c，所以它不会破坏下节 y₃ 在其 p-cell 内的均匀性。给定当前 physical cell 和 V-bin，y₀ 可由 `Y−tV` 确定到 O(p)，x₁、x₂ 已在固定 p-bin，x₀再由当前 X 重建，故 (6.9) 的完整 B_p 与 X′ 列表也只有 O(1) 个选项。

### 2.3 真正的隐藏密度轮廓

在固定 exact base `(t,Y)`，隐藏变量满足

\[
w=StY_3+c+te_1+t^2e_2.
\tag{2.3}
\]

当前 y₃ 对 e₂ 的依赖只在宽 O(η/S) 的边界层发生；离该层后，e₂ 的条件律保持均匀。前两个 base 坐标是独立的 `U+tV`，其密度有固定上界。对任意 u>0，其密度低于 u 的点所承载质量至多 Cu²：直接积分左右两个线性斜坡即可。故这些固定几何密度只产生 subpower 的典型因子，不改变幂指数。

在任意预备隐藏宽度 p≥p_* 上，c 加 O(η) 噪声后的区间质量至多 Cp^d，占据的 p-bin 数至多 Cp⁻ᵈ。于是固定 base 上，质量低于 `p^d N₀^{-δ}` 的参与 hidden bins 总质量至多 `CN₀^{-δ}`；上界与有限表联合处理同样成立。式 (2.3) 的大平移 `StY₃` 不改变这些计数。

所以同一 finite exact sequence 经通常的轻 entry 准备/同质化后，隐藏典型轮廓为

\[
n(r)=N_0^{-dr+o(1)},\qquad d<1.
\]

这不是上一轮 d=1 的边界例子。它满足被调用的原生/有限表条件，但没有声称来自初始全部斜率归约。

## 3. 同 native p-bin 内 W 的精确剩余熵

固定任意最细预备 native 系数箱 B_p，p=p_*。其 y₃ 坐标是一个完整的宽 p 区间；给定 B_p，y₃ 仍均匀于该区间，且和 e₁ 独立。因为 (2.2) 的删除仅涉及 c，所有其它粗网格约束也不切割最细 y₃ cell。

对每个固定 e₁，`W=Sy₃+e₁` 均匀于长度 Sp 的区间。因此任意一个宽 p 的 W-bin D 都有

\[
\mathbb P\{W_p=D\mid B_p\}\le S^{-1}.
\tag{3.1}
\]

对 e₁ 取混合仍保留这个上界。于是，对任何只依赖 B_p 的 L 元列表，

\[
\mathbb P\{W_p\text{ 命中该列表}\mid B_p\}
\le\min(1,L/S),
\tag{3.2}
\]
\[
H(W_p\mid B_p)\ge\log S.
\tag{3.3}
\]

整数取整、网格边界或固定扩大只改 O(1) 常数。p≪1/S 时，单个纤维区间 Sp 甚至可小于固定 1，但仍穿过约 S 个 W 的 p-bins；这不是由于目标 W-bin 本身无界。

**所需额外精度。** 若把 y₃ 旧网格细到 δ，而 x₁ 仍知道到 p，则 W 的误差为 `O(Sδ+p)`。要恢复到固定数 p-bins，δ≲p/S 足够；均匀纤维也表明同量级是必要的。要用 L 元列表，应付 `δ≲Lp/S`，不能免费保持同一 p。

因此原生系数的窗口熵即使很小，也不能在同一网格上自动转成原始 W 的窗口熵。这里损失是一个可测量的条件熵 `log S`，不是仅把幅度换成另一个底数。

## 4. 精确 point/history 会取回这份信息：不得删去的互信息项

这个反例**没有**否定加入 exact current base 后的恢复。事实上由 (2.3) 和轨道公式，

\[
W=SY_3+e_1+te_2.
\]

exact Y₃ 一旦给定，W 只剩 O(η) 误差，远小于 p。故在本模型中

\[
I(W_p;\text{exact current base}\mid B_p)
\ge\log S-O(1).
\]

这精确说明 ENT-001/N5-ENT-01 不能删除的点态/历史信息项：W 信息藏在 base 的 sub-p 精度中。不能把 native coefficient bins 的小熵直接当成“原始隐藏方向信息仍未被观测使用”。

## 5. 全时间 true atlas 与 horizon 的明确边界

本模型的 H=0 可以**直接构造**，不从 d<1 或光滑性推断。

在 terminal 宽度 p_*，以 c-bin C 为轨道 assignment，使用整个单位时间、一个固定大空间盒 D（覆盖全部有界 Y 轨迹），测试

\[
P_C=P_*-c_C.
\]

由 |c−c_C|≤p_*/2、|e₁t+e₂t²|≤4η≪p_*，whole-time 小值为 O(p_*)，隐藏导数为 1、曲率为 0。每个 chart 的原始 assignment 质量是 `λ°(C)≥τp_*^d`，selected duration为 1；空间 Jacobian固定，所以它满足 `n(L)J` 的 true floor，损失只为 reciprocal-subpower τ。c-bin 可由 `(t,Y,[w]_{p_*})` 经 (2.3) 恢复到 O(1) 列表。全部 chart 的质量至少 9/10。

故有真正的 unit-time terminal true atlas，H=0。它不是 positive-horizon 或 critical-path 反例。

## 6. 原始 full-slope 来源没有保留

本模型虽然是完整八维先验，却不是初始原始四维斜率的 subpower 密度模型。V₃ 的宽度是 η/S，W 的宽度约 S，两者乘积约 η。更精确地，V₃ 密度为 S/η，而 W 的内部密度为 1/S，所以完整 `(V,W)` 的密度在内部约为 η⁻¹，是原始固定正幂，而非 subpower。

若再要求原始 |W|≤M，模型仅能保留 O(M/S) 的质量，不能把这一步条件化后重新归一化而免费使用原始方向密度。这个损失是祖先/父选择应支付的成本。

因此本反例证明：原生界、d<1、有限半代数 full-coefficient prior、(6.6)/(6.9) 以及 full-time true charts 本身仍不足以从 native p-bin 恢复 W_p。它没有同时保留初始全部方向的有界斜率来源，也没有正 horizon。

## 7. 一个真正的新排除条件：bounded W 与同-prior affine caps

先给出对 PRI-001 型双线性原生式的精确结论。所有符号必须在**同一坐标、同一未归一化 prior ν**中使用。

设

\[
P_* =\alpha w-\beta(tY_3-Y_1Y_2),\qquad \beta\ne0,
\]

初始位置和可见速度在固定盒 `[-R,R]³` 内。假设 |W|≤M_W、原生线性系数 |x₁|≤M_x，并对一个可用的 0<p≤1 网格有 affine-bin cap

\[
\nu\{y_0\in C_p,V\in J\}
\le A_{\rm aff}\,p^3\pi(J),\qquad \sum_J\pi(J)\le1.
\tag{7.1}
\]

沿线比较一次项，精确有

\[
x_1=\alpha W-\beta(y_3-y_1V_2-y_2V_1).
\]

故全部目标轨道位于

\[
|y_3-y_1V_2-y_2V_1|\le t_*,\qquad
t_*=(|\alpha|M_W+M_x)/|\beta|.
\]

对固定速度 p-bin J 和固定 y₁、y₂ 的 p-cells，右侧所允许的 y₃ 区间宽度至多 `C_R(p+t_*)`，因此只需 `C_R(1+t_*/p)` 个 y₃ cells。前两个位置坐标共有至多 C_Rp⁻² 对 cells。用 (7.1) 求和，再对 J 求和，得到

\[
\boxed{\nu(\text{目标轨道})
\le C_R A_{\rm aff}(p+t_*).}
\tag{7.2}
\]

若 p≥t_*，右侧至多 `C_R A_aff p`。这**不要求把网格细到 β⁻¹ 以下**；相反，任意预备的固定幂小 p，只要大于关系厚度 t_*，就已看见一条位置-方向薄带。若 A_aff 为 subpower 而目标 prior 质量为 inverse-subpower，该界会排除 t_*≪p 的大幅度配置。

对本文件的简化式 `P_*=αw−StY₃`，同理 `x₁=αW−Sy₃`，把上式的双线性表达式换成 y₃ 即得完全相同的质量界。它解释了为何 bounded-W 修补不能既保大量质量，又免费保留原始 affine cap。

这里比仅给 native inverse 条件数多了真实几何输入：(7.1) 同时控制位置与方向，且用的是未归一化 prior。若 cap 只对另一份后验、另一坐标、或另有父条件化因子成立，必须把该损失重新乘入 A_aff。

## 8. 为什么不能立刻套用初始 raw W 范围

源稿 Lemma 2.13 version 2 在父正规化中保留 w，但改时间 `t=t_c+qτ`，因此新 affine hidden slope 是 `W_new=qW_old`。新 native test 是所选父 test P 除以父厚度 a_b，隐藏导数尺度从该父使用的 B 变为 `B_new=B/a_b`；这个 P 不必是旧 native P_*。

若熵变量改用导数归一化的隐藏坐标 `\widetilde w=B_new w`，则

\[
\widetilde W=B_{\rm new}qW_{\rm old}.
\]

它未必在固定 O(1) 范围。即使仍保留原始 w，上节一般式中的线性系数 α 也可能等于大的 B_new，故厚度 t_* 的分子是 `|α|M_W+M_x`，不能只保留 M_W。

可见基底变换还会改变 β 及其二次形状。仅当新 native 恰是旧 native 除以 a_b 时，才能直接用旧 x₁、旧 x₂与时间中心的混合公式；一般情形须从所选 P 重新计算新系数。要应用 (7.2)，应先写出当前坐标中的实际 `(α,β,M_W,M_x,A_aff,p)`；初始 raw |W|≤O(1) 本身不是该 tuple 的验证。

因此 (7.2) 是可进入真实路径审计的新质量不等式，不是已经排除所有临界数据的结论。本轮没有完整 Kakeya 或高维 critical-path 反例。
