# R0006：两个全时间短轴并不支付投影标签；任意二次 atlas 的覆盖下界

日期：2026-10-16。作者：`lifting_obstructions`。状态：精确有限模型与自包含证明；主覆盖命题和完整 prior 双边界已通过内部独立复核，未经外部同行评审。

## 0. 本轮得到的结论与量词

本笔记不再停留于“三维两个 slab 的交还留一条线”。构造一个 **d=1/2、全八系数分段常密度**的三维可见模型，在同一份概率 prior 上同时具有：

1. 原生二次界和完整单位长仿射轨道；
2. 两个相互正交的薄空间轴；两个单薄轴系统及其联合 flag 系统都是全时间 true systems，有常数总覆盖，标签由实际 own-depth 及 terminal observations 确定到 O(1) 列表；
3. 有限预备 dyadic 表上的同-prior native 系数箱双边界；
4. 原模型的 H=0，由上述 true systems 直接得到。

然而，丢掉其中一个薄轴后，即使额外免费告知**几何 flag cell**、完整投影可见仿射线及微小噪声，任何任意二次测试组成的 known atlas，若共同时间长度为 q、深度厚度为 a、列表长度至多 L、拟合及导数 slack 为 K，都满足

\[
 M_{\rm selected}\le C_d L K^{2d}(a/q)^d,\qquad d=1/2.
 \tag{0.1}
\]

这个界不预先限制新测试的表达式、个数、空间轴、中心或系数幅度，甚至不需要新 true floor。因此它排除以 q≫a、subpower L,K 获得 inverse-subpower 覆盖的**任何新投影二次 known atlas**。该投影确实变成完整六系数、隐藏轮廓为 1 的二维可见模型，其 H=L_depth 可独立核实；与原模型 H=0 形成严格区别。

“免费几何 cell”只指两个短轴的粗位置索引，**不包含旧 c-bin 或旧完整 chart label**。若把旧 c-bin 一并交给投影观察者，便已免费提供正是本笔记计算的丢失信息，(0.1) 的条件不再成立。

这不是正 horizon 临界路径反例，不反驳四维定理，也不是 Kakeya 猜想反例。它表明：两个全时间短轴及真实原列表、floor 本身，仍不能保证投影保留原 d、长时间 atlas 或标签成本。

## 1. 一个不需要删核的有限 Cantor prior

取 d=1/2。第 m 层 base-4 Cantor 近似由 digits {0,3} 的 2^m 个长度 ℓ=4^{-m} 闭区间组成，每段均匀质量 2^{-m}。端点用半开约定处理。记其概率测度为 λ。

它有两项初等性质：

\[
 \lambda(J)\le C |J|^d\quad\hbox{对所有区间 }J;
 \tag{1.1}
\]

对每个 dyadic p≥ℓ，所有参与的对齐 p-bin C 均有

\[
 c p^d\le\lambda(C)\le C p^d.
 \tag{1.2}
\]

证明：(1.1) 在 |J|≥ℓ 时由标准两支分离计数得到；在 |J|<ℓ 时，常密度给 `λ(J)≤C |J| ℓ^{d−1}≤C |J|^d`。(1.2) 在 p=4^{-k} 时每个参与箱是一个 Cantor parent，质量恰 p^d；在 p=2^{-1}4^{-k} 时，两个占据的半箱各有 parent 质量的一半，故比值为固定常数。有限末层不改变 p≥ℓ 的结论。

固定有限 dyadic 预备表，最细宽度 a_*。选 dyadic S≥16，及 η、ℓ，使

\[
 \delta=4/S\ll1,\quad a_*\ll S^{-1},\quad
 0<\eta\ll a_*,\quad \ell\ll a_*,\quad \eta<10^{-3}.
 \tag{1.3}
\]

所有参数及其倒数均为原始 N₀ 的固定幂；m=O(log N₀)。无需在任何箱内归一化或删除轻箱。

## 2. 完整八系数模型与同一 prior

取内部离散索引 i₃=0,…,δ^{-1}−1，等概率 δ，令 b₃=i₃δ。该索引可视为 Definition 2.2 允许的 coefficient-space copies，**不是 world，也不是额外观察量**。取独立参数

\[
 y_{01},y_{02},V_1\sim U[0,1],\quad V_2\sim U[0,\delta],
\]
\[
 D\sim U[1+2\eta,3],\quad e_1,e_2\sim U[\eta,2\eta],\quad c\sim\lambda.
\]

定义

\[
 y_{03}=b_3+(D-e_1)/S,\quad V_3=-e_2/S,\quad
 w_0=c,\quad W=Sb_3+D.
 \tag{2.1}
\]

在 0≤t≤1 上取完整长线

\[
 Y(t)=y_0+tV,\qquad w(t)=c+t(Sb_3+D),
\]

及 native test

\[
 P_*(t,Y,w)=w-StY_3.
\]

直接计算得

\[
 X(t)=c+e_1t+e_2t^2,\qquad P_{*,w}=1,\quad P_{*,ww}=0.
 \tag{2.2}
\]

因此 native X 全时间有固定常数界；可见位置、速度有固定常数界；真实隐藏 W 的范围虽可达 S，仍为允许的原始多项式范围。事件为完整单位时间、全部轨道，概率质量为 1。

### 2.1 完整系数与半代数性

在每个 i₃ copy 内，八个连续独立参数可取

`(y01,y02,V1,V2,c,D,e1,e2)`。

到完整八系数 `(y0,V,w0,W)` 的变换为可逆仿射映射。其非平凡三变量部分是

\[
 (D,e_1,e_2)\mapsto
 (y_{03},W,V_3)=
 (b_3+(D-e_1)/S,\ Sb_3+D,\ -e_2/S),
\]

Jacobian 为 −S^{-2}。故完整八系数 prior 在有限个半代数 pieces 上确为分段常 Lebesgue 密度，非奇异参数图；其高度、pieces 数及逆映射都是固定多项式界。

### 2.2 原隐藏轮廓与 native 系数箱

固定 exact base 时有

\[
 w=StY_3+c+te_1+t^2e_2.
 \tag{2.3}
\]

c 与其它参数独立；η≪a_*，所以在所有预备厚度 a≥a_* 上，隐藏 bin 律为 Cantor 平移加 O(η) 噪声。其区间上界为 Ca^d，占据数为 Ca^{-d}；(1.2) 加通常的有限表典型化给原隐藏轮廓 `n(r)=N₀^{-dr+o(1)}`。可见 base 密度为常数阶，除去固定幂小边界层不改变指数。这里 n(0) 也为常数阶：i₃ 的质量 δ 正好抵消每个占据片的 Y₃ 密度 S 阶。

更具体地，对每个预备 dyadic `a_*≤p≤1`，y₀₃ 的每个参与 p-bin 质量在 cp 与 Cp 之间。这里必须使用精确端点，不能仅说边层质量小：

- `D−e₁∈[1,3−η]`，所以占据片完全处在对齐的 `[b₃+1/S,b₃+3/S)` 内，绝无向外伸出的 tiny positive bin。其密度在 `[b₃+(1+η)/S,b₃+(3−2η)/S]` 为常数 `4/|J_D|`；只有首尾各 O(η/S) 宽度的边层。
- 若 p≤1/S，因两端均为 dyadic 网格点，每个参与箱均是上述对齐区间的完整 p-bin；首尾箱也只从一个完整宽 p 的箱中损失 O(η/S)。故其质量至少 `c(p−Cη/S)≥c'p`，这一步使用 `η/S≪a_*≤p`。
- 若 p=2/S，每个 period 的两个半箱分别含约 1/S 的占据长度，质量均为常数倍 p。若 p≥δ=4/S，每个箱由完整 periods 构成，质量恰 p。

这穷尽所有 dyadic p。V₃、e₁、e₂ 各落在一个固定 p-bin。

因此，令 π 为实际 V-bin palette，同一个、未条件化的 prior ν 满足每个参与完整 native 箱

\[
 c p^{3+d}\pi(J)\le
 \nu\{(y_0,V,x_0,x_1,x_2)\in B_p\}
 \le C p^{3+d}\pi(J),
 \quad (x_0,x_1,x_2)=(c,e_1,e_2).
 \tag{2.4}
\]

给定 physical cell 与 V-bin，y₀ 可恢复到 O(p)，x₁、x₂ 已各为一个 bin，x₀由当前 X 恢复，因此源 (6.9) 型列表也为 O(1)。本轮主结论不以 (2.4) 为前提，但这个核验说明反例并非靠换 prior 或删掉系数箱 lower 构造。

## 3. 两个薄轴、实际列表和 true floors

把 y₀₂ 按宽 δ 分箱，索引 i₂，左端点 b₂=i₂δ。对任意预备深度厚度 a≥a_*，以

\[
 A_{i_2,i_3,C}=\{y_{02}\in[b_2,b_2+\delta),\ i_3\hbox{固定},\ c\in C\}
 \tag{3.1}
\]

为全时间、互不相交的 assignments，其中 C 为参与的 c 的 a-bin。其完整 prior 质量为

\[
 \nu(A_{i_2,i_3,C})=\delta^2\lambda(C)\asymp\delta^2 a^d.
 \tag{3.2}
\]

取空间中心

\[
 y_C(t)=
 (1/2+t/2,\ b_2+\delta/2+t\delta/2,\ b_3+2/S-3\eta t/(2S)),
\]

空间矩阵 `diag(4,4δ,4δ)`，时间长度 q=1。所有 assignment 轨道 whole-time 落在该盒的固定扩大内；两薄轴分别是 e₂、e₃，宽度均为常数倍 δ，最大轴为常数阶 1。空间 Jacobian `J=64δ²`。

取二次 test

\[
 P_C=P_*-c_C,
\]

c_C 为 c-bin 中点。全时间 `|P_C|≤a/2+4η≤Ca`，隐藏导数为 1、曲率为 0。选中全部 assignment incidences，故 `m_C/q=ν(A_C)≈a^d J`；这是同一 prior 下的**真实 floor**，不是仅 assignment 质量的命名。全部 chart 覆盖总质量 1。

实际 own-depth 观察为 `(t,Y(t),[w(t)]_a)`，B=1：

- Y₂(t) 给出 y₀₂ 至 δ 精度，因 V₂∈[0,δ]，所以 i₂ 只有 O(1) 个选项；
- Y₃(t) 与 y₀₃ 之差只有 O(η/S)，而相邻 i₃ 的占据片相隔约 δ/2，所以 i₃ 也只有 O(1) 个选项；
- (2.3) 给 c 的误差为 O(a+η)，所以 c-bin C 只有 O(1) 个选项。

终端观察宽度 a_*≤a 仍给同样列表。这些列表均是有限半代数测试，并非熵平均意义上的恢复。故每个预备深度都有 full-time true atlas；特别是 **原模型 H=0**。

若希望分别看到两个法向：只保留 `(i₂,C)` 得到宽度 `(1,δ,1)` 的 true 全时间系统，质量 `δλ(C)`、J≈δ；只保留 `(i₃,C)` 得到 `(1,1,δ)` 的 true 系统，同样质量和 floor。二者的真实联合 refinement 正是 (3.1)。因此这里不是空洞地画出两个正交 slab，而是把两个单法向系统及联合 flag 的实际质量与列表全部实现。

## 4. 丢掉一个薄轴后的精确 prior

现在额外提供纯几何 cell `(i₂,i₃)`，在该 cell 内正规化第二可见坐标并丢掉第三坐标：

\[
 Z_1(t)=Y_1(t),\qquad
 Z_2(t)=(Y_2(t)-b_2)/\delta,\qquad
 \bar w(t)=w(t)-Sb_3t.
 \tag{4.1}
\]

得到二维可见模型

\[
 Z_1=u_1+t v_1,\quad Z_2=u_2+t v_2,
 \qquad \bar w=c+tD,
 \tag{4.2}
\]

其中 u₁,u₂,v₁,v₂ 独立均匀于 [0,1]，D 独立均匀于 `[1+2η,3]`，c∼λ。e₁、e₂ 完全不影响 (4.2)。

这次投影后的完整六系数 prior 是**严格分段常密度**，并非把 e₁ 的卷积后验错说成分段常量。native 可取 `\bar P_*=\bar w`，全时间有界、隐藏导数 1。世界 `(i₂,i₃)` 的权重为 δ²；正规化后各世界的律完全相同，所有加权质量仍相加为 1。

隐藏轮廓变成 d_proj=1。事实上固定 t>0 时

\[
 g_t(w)=\frac{1}{t\,|J_D|}
 \lambda([w-tD_{\max},w-tD_{\min}]),\qquad
 J_D=[1+2\eta,3].
 \tag{4.3}
\]

这是有界区间上绝对连续的密度；对 typical entries 而言有限隐藏 bins 的幂指数为 1。一个可直接量化的证明是：去掉 t<N₀^{-ε} 以及 D 距端点小于 N₀^{-ε} 的轨道，损失 O(N₀^{-ε})；在剩余点，(4.3) 的 Cantor 窗口包含以真实 c 为中心、半径 ≥N₀^{-2ε} 的区间。有限 Cantor 的 AD lower 及 ℓ 的足够小选择给 `N₀^{-O(ε)}≤g_t(w)≤N₀^{O(ε)}`。再令 ε 随典型容差取小即可。固定可见 base 的密度也只贡献相同的典型 subpower 因子。

所以此投影无法继续当作原来的 C(d=1/2)。这个变化本身必须计入任何降维调用。

## 5. 任意二次 projected known atlas 的覆盖界

### 命题 FLAG-INV

对 (4.2) 的 prior，固定厚度 a>0 和共同时间分割长度 q。允许任意有限的 chart family，测试为 total-degree≤2 的任意

\[
 Q(t,Z_1,Z_2,\bar w).
\]

每个被分配轨道要求在其整个 time block I 上有 `sup_I |Q|≤K a`，在该 chart 的 selected incidences 上要求 `|Q_{\bar w}|≥K^{-1}`。空间条件、曲率条件和 true floor 可任意再加；本命题不用它们。

假定在每个 current observation 上，可供实际 assigned label 使用的确定性列表至多 L 个。为加强观察者，甚至允许该列表依赖完整投影可见仿射线

\[
 \alpha=(u_1,u_2,v_1,v_2),
\]

精确当前值 `(t,\bar w(t))`、几何 cell 和任意独立噪声；**不给 c、D 或旧 c-bin**。则

\[
 \boxed{M_{\rm selected}\le
 C_d L K^{2d}(a/q)^d.}
 \tag{5.1}
\]

常数与 charts 数、系数范围、空间框架及 q 无关。若右侧大于 1，仅取平凡上界 1。

### 证明

固定 α，沿任一 assigned 轨道，

\[
 R(s)=Q(s,Z(s),c+sD)
\]

是次数至多二的单变量多项式。由 `sup_I|R|≤Ka` 和区间缩放的二次 Markov 不等式得

\[
 |R'(t)|\le CKa/q\qquad(t\in I).
 \tag{5.2}
\]

此处可完全不用外部不等式：把 I 缩放到 [0,1]，在 0,1/2,1 三点的 Lagrange 基分别是 `2x²−3x+1,4x−4x²,2x²−x`，导数绝对值分别不超过 3、4、3，所以 C=10 足够。

在固定 current exact point `(t,Z(t),w)`、固定 α 及一个候选测试 Q 下，链式法则给

\[
 R'(t)=Q_t+v_1Q_{Z_1}+v_2Q_{Z_2}+D Q_{\bar w}.
\]

右侧所有偏导在固定 point 取值，均不再依赖未知 c、D。若该 point 是该 chart 的 selected incidence，`|Q_{\bar w}|≥K^{-1}`；结合 (5.2)，允许 D 位于一个长至多

\[
 C K^2 a/q
 \tag{5.3}
\]

的区间。由于 `c=w-tD`，允许 c 位于长 `C t K²a/q` 的区间。

对每个 t>0，将 `(c,D)` 换成 `(c,w=c+tD)`，精确得到未归一化积分元

\[
 \frac{1}{t|J_D|}
 1_{\{(w-c)/t\in J_D\}}\,\lambda(dc)\,dw.
 \tag{5.4}
\]

故固定 `(t,w,α)` 的一个候选 Q 的 selected numerator 至多

\[
 \frac{C}{t}(tK^2a/q)^d
 =C t^{d-1}K^{2d}(a/q)^d
 \tag{5.5}
\]

（用 (1.1)，其对任意短区间均成立）。当前列表至多 L 个，先逐点求和；w 的总范围处在固定 [0,4] 内，再积分 t∈(0,1]。因为 d>0，

\[
 \int_0^1 t^{d-1}dt=1/d<\infty.
\]

最后积分 α 与世界权重即得 (5.1)。

**没有 q^{-1} 个 time blocks 的额外损失**：在固定 current t，仅有一个 time block 与该点相容，列表也已包含实际 time label；(5.5) 是逐点界，随后只积分一次全单位时间。t=0 的单点没有 incidence 质量。证毕。

### 此命题确实排除了任意新测试

Q 可随 label 及世界变化，可含 w²、mixed terms、很大的原始多项式系数。证明只用 whole-block 小值、次数≤2、当前导数下界与实际列表；没有假设 `Q=w−某个旧表达式`，也没有只数旧 c-label。因此换一套 projected quadratic atlas 不能避开 (5.1)。

## 6. 原 H=0，投影 H=L_depth：不从 d 猜 horizon

令 terminal 厚度 `a=N₀^{-L_depth}`。若共同 time length `q=N₀^{-h+o(1)}` 且 h<L_depth 为固定差距，subpower K,L 使 (5.1) 为固定幂小质量，所以无法有已知 atlas 的 inverse-subpower 覆盖。任意 true system 经源 Lemma 2.10 的 saturation/list pruning 产生这种已知 atlas，仍保 inverse-subpower 质量。因此

\[
 H(\text{projected model})\ge L_{\rm depth}.
 \tag{6.1}
\]

上界可以显式构造，不必从 d_proj=1 推断。取 q=a，在 `t∈[2/3,3/4]` 的 dyadic blocks；在每个 block 起点 t₀，按 Z(t₀) 的 a-cubes 与 `\bar w(t₀)` 的 a-bins 分配轨道，只使用

\[
 Z(t_0)\in[.81,.89]^2,\qquad
 \bar w(t_0)\in[1.82,1.88].
\]

在稍大的固定内层中，Z(t₀) 的密度有常数上下界。对所列 t₀,w，所有 c∈[0,1] 都对应 J_D 内的 D，所以 (4.3) 的密度也有固定常数上下界。每个 assignment 的 prior 质量因而为常数倍 `a²·a=a³`。

用空间矩阵 `Ca I₂`、相应 affine center，以及测试 `Q=\bar w-s_C`，其中 s_C 是起点 hidden bin 中点。因 |D|≤3，whole-block `|Q|≤Ca`，导数 1、曲率 0。选择整个 block；于是 `m/q≈a³≈n(a)J`，其中 `n(a)≈a,J≈a²`。标签由当前 Z 和 hidden a-bin 确定到 O(1) 选项，所用内层给常数总覆盖。这是真实 q=a 系统，因此

\[
 \boxed{H(\text{projected model})=L_{\rm depth}.}
 \tag{6.2}
\]

原模型的 H=0 已在第 3 节由 whole-time true atlas 证明。这个对比表明，隐藏敏感方向的投影可以把一个已有的 fulltime trueatlas 变成只能在 terminal 时间尺度拟合的模型；不能只按空间几何的短轴宽度决定投影成本。

## 7. 丢轴精度与原 c-label 的新定量下界

原 native test 对丢轴 Y₃ 的敏感度为 `|(P_*)_{Y₃}|=St`。几何 cell 内 Y₃ 宽度约 S^{-1}，故 t≈1 时丢掉它造成的 native 误差为常数阶，远大于 a。把该短轴代入中心并非无损。

在固定几何 cell 内，取 `t∈[2/3,3/4]`、`w∈[1.82,1.88]`，(5.4) 对所有 c∈[0,1] 均不截断，故 c 的 conditional law 正是 λ。该区域承载固定正质量。任意仅依赖 projected observation 的 L 元旧 c-bin 列表，其条件成功率至多

\[
 C L a^d.
 \tag{7.1}
\]

因此单纯恢复旧 c-label 就需要约 a^{-d} 个选项；完整几何 cell 已免费提供，仍然如此。第 5 节则进一步排除了替换成任意新 quadratic label 的规避。

若另外给 Y₃ 至精度 Δ，则直接恢复公式 (2.3) 的误差为 `O(a+SΔ+η)`。因此 `Δ≲a/S` 是直接恢复 c 的 a-bin 到 O(1) 列表的**充分精度**；它比几何短轴 δ≈S^{-1} 细 a 倍。这里不声称一般 L 元列表的最优必要精度：这种更细的量化还须处理 η 噪声、端点截断及 conditioning 后的窗口分母，未在本轮验证。主覆盖界 (5.1) 与 (7.1) 不依赖任何此类窗口 lower。

## 8. 对源接口的意义与未验证项

源 §10.2 在二维可见空间中，把两条明显不平行的速度 strip 交成小球，再用实际终端角 cap 排除。三维版本若想保留两条 independent normal，得到的是一长两短 flag；本模型已实现比“两时刻交线”更强的 fulltime 正交 flag、同-prior true floors、actual own/terminal 列表与常数覆盖。

在原 point 中，两个原系统的完整标签组合仍是 O(1) 列表。本笔记**没有**证明这一步在原 observation 下必然失败。失败发生在下一步：把一个几何短轴丢掉后，仅提供几何 flag label 不能传递旧 c-bin，也不能由任意新 fulltime quadratic atlas 补回。

若某条正向路线提供额外条件，例如 `sensitivity×discarded width≲a`、可由保留点以 subpower 选项恢复的旧 c-label、或者新的 d<1 projection theorem，这个模型就可能被该条件排除；必须明确核验此项，不能从“两轴薄”自动推出。

还须保留以下边界：

- 原三维可见模型有 H=0，所以不满足正临界 horizon；
- 原始 full-slope 来源没有保留，V₃ 极薄，raw W 范围大；
- 没有声称实现 §10.1 的 maximizing sequence、两重 narrowness divergence、nested true critical history 或全部 angular-cap 输入；
- 投影模型的 d_proj=1，是源 d<1 论证明确排除的边界，不反驳四维理论；
- (5.1) 依赖 total quadratic、whole-block 小值及实际 list；若放宽模型类或免费携带旧 c-bin，应重新计算。

本轮新增可复用结论是 (5.1) 的**任意二次测试覆盖界**及其真实 flag/prior 实现。它把投影丢标签的代价从定性担忧提升为 `L K^{2d}(a/q)^d`，下一步正向几何引理必须支付这个接口。
