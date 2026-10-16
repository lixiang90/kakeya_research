# R0004：真实父质量方向预算与熵接口的内部复核

日期：2026-10-16。审查人：`literature_frontier`；被审文本：`results/reviewed/DIR-002_true_floor_direction_budget.md`，并核对 `notes/40_multiscale/parent_mass/R0004_source_assignments.md` 的§2、§3与§6。本次只审查明确条件下的不等式及应用尺度，不把审查扩大为原稿全部 chart/floor 来源、五维结构约化或临界路径的验证。

结论：**DIR-002 的核心条件命题通过内部独立复核。** 它是初等换元、先验质量下界与同层加权预算的组合，不声称数学新颖性或 Kakeya 维数下界改进；未获外部同行评审。

## 1. 逐父界与归一化

固定同一 world 的概率 prior、父 assignment $A$、时间块长 $q_A$、固定可见仿射变换 $V=v_A+F_Av'$，其中 $F_A=D_A/q_A$。事件与矩阵不随当前 trajectory 或时空点改变。令 $J_A=|\det D_A|$，方向事件体积为 $\Phi_A$，incoming visible 密度至多 $C_\gamma$。则

$$\nu_\gamma(A\cap\{v'\in E'_A\})
\le\min\{\nu_A,C_\gamma J_A\Phi_A/q_A^j\}.$$

用**同一 prior 的完整 assignment**下界 $\nu_A\ge n_\gamma(b)J_A/K_{\rm sat}$，得到(D2.1)。$J_A$ 确实消去；条件化到该父后的密度换元同样给出

$$C_{\rm new}\le C_\gamma J_A/(q_A^j\nu_A)
\le K_{\rm sat}C_\gamma/[n_\gamma(b)q_A^j],$$

即(D2.3)。这些式子无需假定 assignment 仅由方向决定。后来的 incidence restriction 不可替换其先验分母或自动继承该下界。

## 2. world/time 权重与真实分支

若 $\lambda_\gamma\le G\nu_\gamma dt$，固定父事件在其整个块上的 incidence 至多 $Gq_A\nu_A\beta_A$，其中 $\beta_A$ 是(D2.1)的比例上界。用明示的同层预算 $\sum_A\omega_{\gamma(A)}q_A\nu_A\le1$ 求和即得(D2.2)；不同长度的块亦可直接使用这个已给预算，不能未经证明从任意重叠块推出它。比较保留质量 $M$ 的比例仍须除以 $M$。

先固定每父一支 $B$ 及其固定方向事件。若 $\lambda(B\times I)\ge q_A\nu_A f/K_{\rm br}$，则精确的分支比例界为

$$\frac{\lambda((B\cap\mathrm{bad})\times I)}{\lambda(B\times I)}
\le\min\{1,GK_{\rm br}\beta_A/f\}.$$

这里仅有一个 $G$；$GK_{\rm br}/f$ 是乘在 prior 比例 $\beta_A$ 上，不能再对已含 $G$ 的 incidence 上界重复乘 $G$。多个不同方向事件须另给并集体积预算。每父 $R$ 个事件、各体积 $\Phi$ 时可付 $R\Phi$；未受控的不同 potentials 不可免费重复使用同一 $\nu_A$。

## 3. 薄层体积与最后指数

特殊式 $v'_2-(v'_1)^2$ 对 $v'_2$ 的导数为1，Fubini 直接给 $2\eta(2T)^{j-1}$。一般系数归一化的次数不超过2多项式在固定有界盒上只有统一 $C\sqrt\eta$ 界；例如平方线性式达到平方根量级。可变盒、系数规范与仿射条件数的损失必须保留。$R$ 个一般二次事件的并集界是 $RC\sqrt\eta$，不能误写成 $C\sqrt{R\eta}$。

忽略只会增加成本的常数，代入 $n\asymp a^d$、$q\asymp h$、$f=(a_2/a)^d=h^{ed}$、特殊事件精度 $\eta\asymp h$，所得预算恰为

$$a^{-d}h^{1-j-ed}.$$

在 $0<a\le1$、$h\to0$、$j\ge2$、$d\ge0$、$e>0$ 下，此表达式不趋零。通用平方根体积给 $a^{-d}h^{1/2-j-ed}$，更弱。这说明此上界和现有精度不能提供所需 smallness，**不证明真实 bad 质量大，也不反证整个路线**。

原始固定精度 $\eta=N_0^{-c}$、$n(b)=N_0^{-db+o(1)}$、$q=N_0^{-kb+o(1)}$ 及其余输入为 actual subpower 时，特殊事件指数为 $-c+(d+jk)b+o(1)$，一般二次式把 $-c$ 换成 $-c/2$；该条件算术正确。本次不复核 Corollary 4.4 是否提供这些额外绝对输入。原稿真实 $j=2$；$j=3$ 的几何 reduction 尚未建立。

## 4. ENT-001 的审查来源

`notes/60_entropy/R0004_full_slope_selection.md` 由本审查人撰写，因此本文件**不把自查登记为独立审查**。Root 已独立逐项检查并在本轮消息中确认：固定 law 的二元 KL 界、$I(S;A)\le I(S;Z)+H(A\mid Z)$、同 law 几乎处处列表、selection 成本、同方向网格与边界扩大、joint domination 下的 $KL\varepsilon$ 界，以及小互信息的标准 likelihood 截断均通过。此处只记录该内部审查的来源。

ENT-001 对原稿的应用仍受 parent-visible palette、有限 prepared 网格与选择分母限制；它未补上原始完整斜率共同 palette 的似然界，也未计算其实际长线反例的 horizon。DIR-002 与 ENT-001 均未提供新的全局 Kakeya 维数结论。
