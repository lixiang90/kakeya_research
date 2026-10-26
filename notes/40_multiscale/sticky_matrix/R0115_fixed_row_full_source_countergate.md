# R0115：完整 usual-source 的单 clock graft 与 fixed-row 全称门

2026-10-26，algebraic_gate。本稿只编辑分配文件。结论是一个**条件构造闭包**：从一个已经存在的完整 matrix33、κ=1、usual-tube source，可造另一个完整 source，使某个新增 clock 的每个 grain 都有固定 scalar ξ 原子。没有构造任何无条件完整 source，没有证明普通 Kakeya 或来源主定理的反例，没有新 ordinary 界或 major，未经外部同行评审。正式独审另存；本代理参与机制，不自计独审。

## 1. 恢复、原缺口与精确停止门

运行 `python scripts/context.py`，读 GOAL、STATE、ROADMAP、registry 摘要、R114 next 及 rough 稿 §§2–9；实读 WZ 原 Def3.3、Eq(19)、Def3.9、Def17.1–17.4、Remark17.1、Lemma19.2 statement 和 Lemma19.4 statement/proof 的 concentration→CW 段。回读 R22 整 time restriction、R106 native-Y KT 失败及 bulk 预算、R79 缺 whole-T 范围。主缺口仍是完整原 bulk/source 的联合质量。

本轮独立攻击 R114 rough §9 的强标尺：固定 γ>0 时，是否存在 `0<a<1`、τ>0 和有限 C，使 η 足小、δ 足小时，对**每个**完整 d5、k=ℓ=3、κ=1 source、所有原 t,y、固定 ν∈S¹、b∈R 和 allowed ρ∈[δ^a,ρ_0]，均有

\[
 \frac{\#\{x\in X_{y,t}:|\nu\cdot\xi_{x,y,t}-b|\le\rho\}}
 {\#X_{y,t}}
 \le K^C\rho^\tau. \tag{1.1}
\]

ν在本 grain 所有 x/φ 上固定。`a<1` 不失一般性：若标尺原先给任何 a>0，可仅保留 `a_0=min(a,1/2)` 对应的尺度子区间，再重命名为 a，保证下文所用尺度也在原 `[δ,1]` 内。没有把此式加作成功假设。本稿若只得到 R114 dust 本身而未付 bulk，或污染后破坏 strict O(ρ) coherence，就停止并记未达；不把 R106/R79 的缺项模型改名成 full counter。

实际结果：以下 graft 在原 usual Eq(19) 管规范中逐项可付；代价仅 η→η'=Mη、γ 可降级，δ 与全部物理坐标不缩放。因此它对 strong **∀grain** 标尺给真实的 closure 压力，但不攻击“原 I 意义下正质量 good grains”版本。full source 存在仍是开放前提。

## 2. 原输入账及条件命题

使用 WZ2609.22035v1 固定原件。实际重新打开[官方版本页](https://arxiv.org/abs/2609.22035v1)，提交日期2026-09-18、当前版本记录仅v1；HTML整页因内容大小工具读取失败，数学依本地 `literature/extracted/wang_zakharov_2026_sticky.txt` 原文。原物理65–66页的定义及78–81页 lemma 目标段已实读，不认证 wholeproof 或全前沿。

明确使用 Def3.9 允许的 **usual Eq(19)** 规范：每条管是 bounded-slope 直线在共同 clock `[-1,1]` 上的 δ-厚 graph，

\[
 T=\{(b+u\theta+w,u):u\in[-1,1],\ w\in B_\delta^{4}\}.
 \tag{2.1}
\]

这是固定有界长度的真实整段，不是精确 arclength=1。原 source 本来采用此规范；本稿不另声真 unit-arclength 版本或 dyadic 每 parent 的 AD lower 已免费得到。没有短 clock 后重置 N、原管体积或密度。输入另保本项目 R43/R75 使用的 bounded joint chart。

条件给定完整 source `S_0`，fine δ 是任意足小 dyadic 数，参数 η>0、γ_0>0，`K_0=δ^{-η}`，原 `T_0` 使用(2.1)。其输入如下。

| 原责任 | 完整给定输入 |
| --- | --- |
| Whole T | joint4AD、`C_CW(T_0)≤K_0`，bounded chart 中 `N_0≈_{K_0}δ^{-4}`；无 physical 方向分离假设 |
| Clock | δ-separated `Z_0⊂[-1,1]`，`m_0≥δ^{η-1}` |
| Matrix | `F_t∈Mat(2,2)`，全部原 allowed `ρ=δ^{jη}` 上的 strict dyadic `O(ρ)` variation |
| Point层 | `E_t={(x,y+F_t x,t):y∈Y_t,x∈X_{y,t}}`；native `Y_t` AD1、`#X≥δ^{η-2}`，boundedness 给 `#E_t≈_{K_0}δ^{-3}` |
| Native KT | 每个 `Y_t` 对全部 `δ≤r≤s≤1` 的 tube-KT exponent `1-γ_0`；每个 allowed time 窗的 Y-union coarse AD1 |
| Point star | 每 p 有 selected ξ_p、AD1 且 slab-γ_0 的 Φ_p；每 φ 有同一原 `T_0` 中真实 witness，斜率 `(φ,ξ_p+F_tφ)+O(δ)` |
| Coherence | 全部原 allowed physical ρ-cube 内有真正 AD1 coarse Φ_q carrier 覆盖所有 fine Φ_p，且 `|ξ_p-ξ_q|≲ρ`，不是 `Kρ` |
| 原质量 | canonical selected marks 的 `I_0≈_{K_0}N_0m_0`，真实 volume density 至少 `δ^{Cη}`；平均与逐管另分 |

最后一行可由 Remark17.1 和逐层 witness count 推出，下面仍以原 N、m 显式计算。k=ℓ=3 时两矩阵一致，Def17.4 consistency 是空块恒等式。

记

\[
 \gamma_d=1-\log3/\log4>0,
 \qquad 0<\bar\gamma\le\min(\gamma_0,\gamma_d). \tag{2.2}
\]

本稿证明：存在固定整数 M 和 δ 阈值，使由 `S_0` 可造完整 `S_+`，参数 `(δ,η'=Mη,κ=1,γ=barγ)`；其某个 clock 上 `ξ_1≡0`，而全部表内责任仍真。若原 γ_0≤γ_d，可取 barγ=γ_0，因而这是**同 γ** 闭包。若原 γ_0>γ_d，须明确降级，不能声原较强 γ 原样保持。

## 3. 不改变 δ 的 time restriction 与新增 clock

以八个长度1/4的闭区间覆盖 `[-1,1]`，取含原 Z 点最多的一个 I，于是

\[
 Z_I=Z_0\cap I,\qquad m_I\ge m_0/8.
\]

这些区间各自位于 `[0,1]` 或 `[-1,0]`。若 I 位于正半轴，取 `t_*=-1/2`；否则取 `t_*=1/2`。因此

\[
 \operatorname{dist}(t_*,I)\ge1/2. \tag{3.1}
\]

只删**整时间层**，原 `T_0` 和每个保留层所有点、X、Y、Φ、ξ、witness 完全不动。单层 AD 与 KT、filled X、point star 当然保持；coarse ξ/Φ 原 carrier 覆盖子集，也保持。

coarse Y-union 的 lower 不作任意子集继承：对某 allowed ρ 窗 J，留下的 Y-union 是原 union 子集，故 coarse upper 继承。任意留存 coarse centre 所属的一个完整 fine-AD1 层 `Y_t`，在 fine R 球中有至少 `K_0^{-1}(R/δ)` 个 fine cells，而一个 ρ 球至多含 `K_0(ρ/δ)` 个，因此其 ρ-cover 在 R 球至少 `K_0^{-2}(R/ρ)`；`R≈ρ` 用一个 cell。这付 lower，正是 R22 §1–2 的计数证明，不要求 `Z_I∩J` dense。

后取整数 M 足大，使 `K_0^{C_0}` 与固定常数都由 `K_+=δ^{-Mη}` 支付。重要的是新 allowed 格

\[
 \mathcal R_{\eta'}=\{\delta^{jM\eta}\}\subset
 \{\delta^{j\eta}\}=\mathcal R_\eta \tag{3.2}
\]

**精确**包含，没有 nearest-scale 或 isotropic rescale。常数 `1/8` 的 clock 损失由 δ 足小后 `m_I≥δ^{Mη-1}` 吸收。新 clock `t_*` 与旧点距≥1/2，自动 δ-separated。δ 从始至终不改变。

## 4. 对每个足小 dyadic δ 都成立的数字 dust

完整重用 R114 已付的数字几何，但这里只用于 graft 的一个 clock，不再声 dust 自身支付 bulk。定义

\[
 A=\{\textstyle\sum a_j4^{-j}:a_j\in\{0,1\}\},\quad
 B=\{\textstyle\sum b_j4^{-j}:b_j\in\{0,2\}\},
\]
\[
 Y_d=c\{(r+s,r-s):(r,s)\in A\times B\},\quad
 \Phi_d=c\{(v-w,v+w):(v,w)\in A\times B\}, \tag{4.1}
\]

固定 `c=4^{-h}` 足小。自然 product 概率下，两者均1AD；`y_1` 与 `φ_2` 各自是 `[0,c]` 上的 Lebesgue 概率，且除零测歧义外 `y_2=h(y_1)`、`φ_1=g(φ_2)` 为 Borel 函数。原因是每位和唯一遍历 `{0,1,2,3}`，不需要 h/g 连续。

全尺度 KT/slab 的实际几何：把 `A×B` 作一个固定双边仿射归一化，其四个第一代 child rectangle 在四角，各边比1/4。足窄于 parent 的任意 strip 不可能同时交四个 child：最远两个 child 的投影间隙至少是固定 parent 尺度。故统一至多三支。宽 r、长 s 的 tube 先在尺度 s 只遇 O(1) 个 parent，再到 r 逐层最多三支，得到

\[
 N_r(Y_d\cap\operatorname{tube}(r,s))
 \le C(s/r)^{\log3/\log4}. \tag{4.2}
\]

固定仿射变化只改常数。相同分支计数给 Φ_d 任意宽 r 的 slab 中概率 ≤`Cr^{γ_d}`。这是 native tube-KT，不是只核全局 slab；没有 R106 的 smooth tangent 漏洞。

**任意 dyadic δ 的有限化：**不限制 δ 为4-adic。取 Y_d、Φ_d 各自 maximal `Lδ`-separated nets，L为一个固定大常数；a在 `[0,c]^2` 取同尺度网格，端点作固定常数的均匀分格。1AD 给各 net 的大小 `≈δ^{-1}`，a-grid 大小 `≈δ^{-2}`。从连续量到 finite net，每个 net point 的 Voronoi cell 自然质量 `≈δ`，support 在 `O(δ)` 内；a-cell 质量 `≈δ²`。这些结论直接由 maximal net 的 covering 和 AD upper/lower 给出，适用于全部足小 δ。也可取4-adic level ε 满足 `ε≤δ<4ε` 后有界去重，结论相同，但本证不用 subsequence 代全 δ。

finite AD1 与(4.2)的全部 r≥δ cover 由连续 upper、净分离和 cell 质量比较继承，finite Φ 的 slab bound亦然。固定 L/c 仅改常数；当 r 在 O(δ) 的端点用 bounded packing。下文仍用 Y_d、Φ_d 表示这些 finite sets。

## 5. Dust 的同一真实 whole-T、4AD 及全部凸体 CW

对每个 a-grid、y∈Y_d、φ∈Φ_d，取同一条真实 straight graph

\[
 x(u)=a+(u-t_*)\phi,\quad
 z_1(u)=y_1,\quad
 z_2(u)=y_2+(u-t_*)a_2,
 \qquad u\in[-1,1]. \tag{5.1}
\]

其 δ 厚化按(2.1)，斜率为 `(φ_1,φ_2,0,a_2)`，所有参数 bounded；fine labels 选择 L 足大时 distinct tubes 且 `N_d≈δ^{-4}`。joint 几何参数与 `(a,y,φ)` 双 Lip：由 θ 恢复 φ,a₂，再由 intercept 恢复 a,y。Def3.9 usual `N_r T` 计数与此固定 joint metric 可比，故 T_d 在所有 δ≤r≤1 是4AD，未授任意 dyadic parent 的 lower。

实际 whole-CW 不能由4AD单独推出。给自然 continuous labels 概率 μ，写 `v=u-t_*`。对固定 v≠0，physical R4 点分布满足

\[
 \|d\mu_v/d\operatorname{Leb}_4\|_\infty\le C|v|^{-2}. \tag{5.2}
\]

确实，条件在均匀 y₁ 后 `y₂=h(y₁)`；φ₂独立均匀、`φ₁=g(φ₂)`。从 `(a₂,φ₂)` 到 `(x₂,z₂-h(y₁))` 的矩阵是 `[[1,v],[v,0]]`，det=`-v²`；a₁只平移 x₁，Fubini 给上式。没有对 rough h/g 误用 smooth Jacobian。

相对 clock `v∈[1/8,1/4]` 总在(5.1)的原 `u∈[-1,1]` 内，因为 `t_*=±1/2`。若整个 graph 轴在凸 U 中，它的这些点也在 U 中。因此按真实 u-slice 积分，

\[
 \mu\{\text{whole graph axis}\subset U\}\le C|U|. \tag{5.3}
\]

finite product cells 各有质量 `≈δ⁴`，实际几何 labels 在每 cell 只动 O(δ)，故 whole graph 也只动 O(δ)。若某 finite δ 管含于凸 U，对应 cell 所有 continuous 轴含于 `U+B_{Cδ}`。U 若含一条这种管即含一个固定 `c_1δ`-ball，其中 `c_1>0` 只依 bounded slope；凸性给 `|U+B_{Cδ}|≤C'|U|`（以该 ball 中心作固定倍膨胀）。所以

\[
 \#\{T\in T_d:T\subset U\}\le C\delta^{-4}|U|
 \le C N_d|U|. \tag{5.4}
\]

空或无限体积测试平凡。此为**全部凸 U** 的整管包含上界，不是 box 测试或单 mark upper。自然参数质量只作计数证明，最终分母仍是 finite N_d。

## 6. Graft 后全部 source 假设的实际核验

定义

\[
 T_+=T_0\cup T_d,\quad Z_+=Z_I\cup\{t_*\},\quad
 F_+(t)=F_0(t)\ (t\in Z_I),\quad F_+(t_*)=0.
\]

旧层所有数据不变。新层取

\[
 E_{t_*}=\{(a,y,t_*):a\in[0,c]^2_{L\delta},\ y\in Y_d\},\quad
 X_{y,t_*}=[0,c]^2_{L\delta},\quad
 \xi_{a,y,t_*}=(0,a_2),\quad \Phi_{a,y,t_*}=\Phi_d. \tag{6.1}
\]

每 φ 由(5.1)同一原 T_+ 中的管见证。新 E 是 δ-separated；其新层与旧层的 time gap≥1/2，因而没有细点合并或选后补 marks。全部 coordinates、F、ξ、Φ 在定义要求的 bounded 范围，c固定足小。

**Whole T 与 N：**保持实际 union 并对 exact duplicates 只计一次，故

\[
 \max(N_0,N_d)\le N_+\le N_0+N_d\le K_0^{C_0}N_0.
 \tag{6.2}
\]

usual joint metric 中有限并的4AD lower由含中心的原 component 给；upper 对另一 component 若相交 r 球，选一个相交 centre 后用其 Cr 球 upper。因此为 `K_0^{C_0}`-4AD。whole-CW由分别计数及 `N_0+N_d≤2N_+` 给 `C_CW(T_+)≤CK_0`。如 old/dust tubes 在 fine metric 相近，数量上界仍由两个 component 的 AD upper 支付；本稿不对 union 再取 maximal net，因此不丢任何 selected witness，也不借 O(δ) 容忍来赠源闭包。usual 管不要求 physical 方向分离。

**逐层 point-size / native KT：**旧层未动，新层 Y_d 是 AD1/tube-KT(1-barγ)，X 是实满二维 grid，`#E_{t_*}≈δ^{-3}`，Φ_d 是 AD1/slab-barγ。每个 retained old layer 同样降级至 barγ，全部 fine upper 和 lower 仍真。

**F 的 strict variation：**纯旧 time 窗继承原 O(ρ)，纯新窗只有一个 clock。一个混合窗必须有 `ρ≥1/2`，此时 `|F_0(t)-0|≤1≤2ρ`。没有用 `Kρ` 吞跳跃。

**所有 coarse Y-union：**纯旧窗由§3的整层 restriction证明，纯新窗由单层 fine AD 给 coarse AD。混合窗必有 `ρ≥1/2`；在这个宏观尺度，任何非空 bounded Y 集的 ρ-cover 都是 `(ρ,1,C)`-AD：r∈[ρ,1] 时最多固定个 cells，而至少有自身一个，且 `1≤r/ρ≤2`。故 mixed lower/upper 都由 fixed C 支付。没有假定不同 clock 的 native 标签连续或同形。

**strict ξ 和 coarse Φ：**只含旧点的 physical ρ-cube 继续用其原 ξ_q、Φ_q；只含 dust points 的 cube，`ξ=(0,a₂)` 对 physical a 真 Lip，Φ_d 恒定。此时在每个与 Φ_d 相交的 dyadic ρ-cell 内选一个原 Φ_d 点作为 Φ_q；由 fine AD→coarse AD 的计数证明，此 carrier 是 AD1，且其 dyadic ρ-neighborhood **严格包含**整个 Φ_d，未把一个通常 Euclidean net 的固定倍覆盖冒作原精确包含。若 cube 同时碰旧/新 E，则由 time gap 必有 `ρ≥1/2`。取 `ξ_q=0`，所有 `|ξ_p-ξ_q|_∞≤1≤2ρ`。明确取 `Φ_q=[-1,1]^2`：Def3.3 的 AD 用 covering number，未要求此 coarse carrier 分离；对所有 `R∈[ρ,1]`，box 的局部 ρ-cover 介于1和固定常数，而 `1≤R/ρ≤2`，所以它是 `(ρ,1,C)`-AD，且其 dyadic ρ-neighborhood 包含每个 fine Φ_p。这里**不是**将 fine 2D box 冒作 AD1。混合 coarse Φ 只在宏观尺度使用。coarse carrier 不需要由某个实际单 p 的 star 取得；定义只要求覆盖与 AD，这些已实付。

**参数与 allowed grid：**以上共有限幂 `K_0^{C_0}` 和 fixed constants，取一个固定整数 `M>C_0+2`，δ 足小后均 ≤`K_+=δ^{-Mη}`，clock lower也满足。所需全部新allowed scales正是(3.2)的子格；strict F/ξ 常数是 fixed C，独立 η,δ。故 `S_+` 满足完整 Def17.2–17.4 usual variant，而非只有某个 initial layer。

## 7. Bulk 与原 N/I：谁承担哪些访问

把 selected count incidence 记为 `I_cnt`，每个真实 tube/time pair 只计 bounded 次。完整旧层有 `#E_t≥K_0^{-C}δ^{-3}`、每个点有 `≥K_0^{-C}δ^{-1}` 个不同真实 witness。不同 φ 不能免费重复当同一根管，因为第一斜率坐标 δ-separated；一个 T 在固定 time 只碰 O(1) 个 δ-separated points。因此每个旧 t

\[
 I_t\ge K_0^{-C}\delta^{-4}\ge K_0^{-C}N_0.
\]

保留 m_I≥m_0/8 层，给

\[
 I_{I}\ge K_0^{-C}N_0m_0/8,
 \qquad I_0\le C N_0m_0,
 \qquad I_I\ge K_0^{-C} I_0. \tag{7.1}
\]

增管后 `N_+≤K_0^C N_0`、`m_+=m_I+1≈m_I`，故

\[
 I_+\ge I_I\ge K_0^{-C}N_+m_+,
 \qquad I_+\le C N_+m_+. \tag{7.2}
\]

所有访问始终用同一 T_+ 的实际 straight graphs；各旧层原 bulk3、filledX、stars 全保。dust whole tubes 在旧 clocks 可完全没有 selected visits；它们不被冒作逐管稠密。原 Def17/Remark17.1 只要求推出**平均** shading density，这一点允许。

按 canonical δ-cube marks，有限重叠的 slice thickening给每visit体积 `≈δ⁵`，每条(2.1)真实 whole 管体积 `≈δ⁴`。故 `I_vol/(N_+δ⁴)≥K_0^{-C}m_+δ≥δ^{C'η}`。若继续把同一符号 η 用于某 lower，可再一次固定整数倍放大并取旧格子格；不能把 count 与 volume 当同一 I，也不能声原同一个 density exponent 数值未变。

增管比例和保量责任可写为 `q=N_0/N_+≥K_0^{-C}`、`p=I_I/I_0≥K_0^{-C}`，沿用原 count/volume 单位时新平均密度至少 `pq` 倍旧平均密度；这是**增管**，不是误用删管公式 `p/q`。没有删管重置分母。一般保管比例 q、保 I 比例 p 的另一个 restriction 仍是 `λ'=(p/q)λ`。

新增 clock 的 selected visits至多 `CN_+`；相对(7.2)至多

\[
 \frac{I_{t_*}}{I_+}\le K_0^C/m_+
 \le K_0^C\delta. \tag{7.3}
\]

η 足小是固定正幂的小比例。因此它正是原平均质量意义可忽略的污染；此处 bulk 由给定 `S_0` 支付，未声 R114 dust 自身的 bulk 失败已神奇修好。

## 8. Fixed row 原子与强全称 statement 的准确逻辑

新 clock 每个完整 grain上取**固定** `ν=e₁`、`b=0`。由(6.1)

\[
 \#\{a\in X_{y,t_*}:|\nu\cdot\xi_{a,y,t_*}|\le\rho\}
 =\#X_{y,t_*}\qquad(\rho>0). \tag{8.1}
\]

令强标尺给定 a,τ,C，令其 K 费用统一为 `δ^{-C_1η'}`。先取 η' 足小于 a 和 `aτ/C_1`，并取整数

\[
 j=\lfloor a/\eta'\rfloor,
 \qquad \rho=\delta^{j\eta'}\in
 [\delta^a,\delta^{a/2}]. \tag{8.2}
\]

δ 足小后 ρ≤ρ_0，而且

\[
 K^C\rho^\tau\le
 \delta^{-C_1\eta'+a\tau/2}<1. \tag{8.3}
\]

与(8.1)矛盾。γ≤γ_d 时 graft 保持同 γ；若旧 γ 更强，先降至 barγ≤γ_d，再用该 γ 的标尺。不能将后一步声为所有更强指定 γ 的同参数反例。

因此准确命题为：在这个 **完整 usual-source 类**及固定 `0<γ≤γ_d` 上，若全称(1.1)在其足小 η、δ 域成立，则该域不能存在可按上述有限参数余量输入的完整 source。反向，若完整 source 本来不存在，(1.1)真空成立。因 graft 只损固定 η 倍数，按“先固定 cap 的 a,τ,C，再令输入 η 足小、δ 足小”的常规正幂量词，strong ∀grain cap 承担了排除整个 κ1 source 的强度。

**这没有证明 cap 或 source 排除任一者成立。** 它也不等价整个 ordinary 五维满维、更高维猜想或本 Goal。实际提供的是一个全输入自洽的 conditional graft，不是无条件 full-source 反例。

## 9. 旧闭包、合法添加与不得越界的版本

R114 原全 vector ξ-ball cap是19.4 concentration→CW已付，graft 并未反它：dust 的 ξ=(0,a₂) 仍是1维球分布，球质量≤Cr。fixed row 集中只给近4-plane，原CW幂抵消，与该旧结论相容。19.2/19.4的整矩阵 slow 前提也未从原子 row 得到。

这不是“任何 padding 都合法”：本稿添加的 whole family 单独已有全部凸 U 的 CW与4AD，单层 Y/Φ已经有实际KT/slab，time gap逐项支付 strict coarse coherence，allowed子格精确对齐，全部旧bulk层由实际给定 source保留。缺其中任何一项都不能借本稿补齐 R79/R106。任意删点、选角、删管或将新增 clock 塞进小ρ旧窗，不在此闭包证明内。

若把完整输入额外加强为**每条** T 在原 m 上至少 `K^{-C}m` 次访问，dust tubes未付该要求；本构造不反这种加强类。若问题只要在原 I 意义正比例 good grains 成立，(7.3)允许直接删去新增 clock并仅损固定正幂小质量，故本稿也不反该版本，更不能把这一版本判为已证。存在一个 bad grain与必须处理的主要原质量是两件事。

本轮止点：原强标尺确有 conditional contamination 闭包，不应作为比完整 κ1排除更弱的免费预处理；真正可用的 good-grain 原质量命题仍须新数学。无新正 source gain、ordinary维数界或 major，不登记新ID，不续数字参数优化，不自行开下一轮。root统一安排正式独审、状态和Git同步。
