# R0006：丢短轴后的任意二次atlas覆盖界复核

日期：2026-10-16。审查人：`literature_frontier`。被审定稿：`notes/50_counterexamples/R0006_flag_label_obstructions.md`。独立检查§2.2参与native箱下界、§5任意quadratic known-atlas质量界，并核对§3及§6显式horizon比较所需的模型算术。没有审查一般$j=3$临界路径、全部角cap或极值闭合。

结论：主模型中同prior参与箱双边界及任意二次atlas覆盖界通过内部独立复核，未经外部同行评审。删去的精度窗口扩展不在认证范围内。

## 1. 同prior参与箱的下界确实成立

在每个copy中，$D-e_1$支撑为$[1,3-\eta]$，除宽$O(\eta)$端点ramp外具有上下常数密度。故$y_{03}$占据片位于

$$[b_3+1/S,\ b_3+(3-\eta)/S].$$

$S$、$\delta=4/S$及prepared $p$均为dyadic。对$p\le1/S$，$b_3+1/S$、$b_3+3/S$是$p$边界；首尾占据箱仅损失$O(\eta/S)\ll p$，不会产生独立的tiny端点箱。乘copy权$\delta$后，内部密度$\asymp S$正好抵消该权，故每个参与$y_{03}$的$p$-bin质量为$\asymp p$。

对$p=1/S,2/S,4/S$直接按每个$\delta$周期的两个占据子箱求和，结论仍为$\asymp p$；更粗dyadic bins由完整周期求和。其余初始位置独立均匀，$V$的实际palette独立于这些位置；$e_1,e_2,V_3$在所有prepared $p$上各只占一个固定bin，$c$-bins具有$\asymp p^d$质量。因此整个相同未条件化prior上

$$\nu(B_p)\asymp p^{3+d}\pi(V_p)$$

对每个参与箱成立。这里未偷用任意非空bin自动AD lower；成立依赖本模型的dyadic端点排列、$\eta\ll a_*$以及copy权重。

## 2. 任意二次测试的Markov—Frostman证明

固定完整投影可见系数$\alpha$及一个候选$Q$。沿真正affine轨道，$R(s)=Q(s,Z(s),c+sD)$为次数至多2的多项式。长度$q$的whole-block小值界$|R|\le Ka$给

$$|R'(t)|\le CKa/q$$

于整个块，包括端点。此处常数与$Q$系数幅度无关。在固定当前exact $(t,Z(t),w)$时，链式式中的$Q_t+v\cdot Q_Z$及$Q_w$均不再随未知$c,D$变化。若该label实际选中该point且$|Q_w|\ge1/K$，$D$只能位于长$CK^2a/q$的区间，$c=w-tD$只能位于长$CtK^2a/q$的区间。

由于$D$是与$c$独立的固定长度uniform变量，换元给

$$d\mathbb P(c,w\mid t)=\frac1{t|J_D|}1_{\{(w-c)/t\in J_D\}}\lambda(dc)\,dw.$$

有限Cantor的全尺度upper $\lambda(J)\le C|J|^d$于是把每候选label的numerator限制为$Ct^{d-1}K^{2d}(a/q)^d$。真实列表至多$L$，在同一个固定exact point逐项求和后再积分；$w$范围固定、$\alpha$为概率律，且$\int_0^1t^{d-1}dt=1/d$，得到

$$\boxed{M_{\rm selected}\le C_dLK^{2d}(a/q)^d.}$$

这个证明适用于任意total-degree不超过2的$Q$，包括$w^2$、mixed terms和大系数。它不依赖新空间frame、true floor、chart总数或预先保留某个旧$c$-label。额外告知的独立噪声可先固定再按概率密度积分，不增加成本。

固定当前$t$只有一个相容time block，所以没有额外$q^{-1}$。列表可以依赖精确$w$及完整$\alpha$，比原实际投影观测更强；证明仍不给$c,D$或旧$c$-bin，量词没有免费送回丢失信息。

## 3. horizon比较及其边界

原三维模型在§3对每个prepared厚度$a$明确构造whole-time true atlas：assignment质量$\delta^2\lambda(C)\asymp\delta^2a^d$，空间Jacobian$64\delta^2$，test为$P_*-c_C$，实际point恢复$i_2,i_3,C$只有$O(1)$选项。其$H=0$由这项构造给出，而非从$d<1$推断。

投影模型的$H\ge L_{\rm depth}$以以上覆盖界和原Lemma2.10的true-to-known准备为条件；本次未重新证明该源lemma，但覆盖界对其产出的任意列表和测试统一成立。$q=a$的反向构造也可直接核对：在$t_0\in[2/3,3/4]$、$w\in[1.82,1.88]$及指定visible内层，所有$c\in[0,1]$对应的$D$均处于其uniform区间，assignment质量为$\asymp a^3$；$J\asymp a^2$、$n(a)\asymp a$，whole-block小值、真实floor及当前$O(1)$列表均成立。因此该明确模型的投影horizon比较有直接依据。

定稿§7保留的旧$c$-bin列表界只在上述固定内层使用，条件$c$律恰为$\lambda$，故成功率至多$CLa^d$。先前窗口端点删失与必要精度扩展已删除；本review不认证那些已删除说法。$\Delta\lesssim a/S$仅作为由直接误差公式得到的充分恢复精度。

原模型无正horizon，未保留初始raw完整斜率subpower来源；投影真实profile为$d_{\rm proj}=1$。该结果反驳“几何两轴薄可免费投影并保留原列表/时间成本”的通用推论，不能作为高维critical/Kakeya反例。
