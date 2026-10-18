# R0086：Du 显式压缩、真实直线方向与补齐成本的独立审计

2026-10-18，B。仅编辑本分配稿。本文核源构造和资格接口，不声明新的数学 ID、重大结果或 ordinary Kakeya 反例；具名高级输入与本文独立代数计算分开，未经外部同行评审。

## 1. 实际阅读、原目标与停止量词

实际读 R86 working_spec5（含最后资格补锁）、GOAL、STATE 顶部、ROADMAP 当前冻结、registry 全78状态、R85 next。全文读 [Du2610.05404v1](https://arxiv.org/html/2610.05404v1) §§1–3和参考文献，以及库存 `literature/extracted/du_2026_fraction_dimensional_compression_2610_05404_v1.txt` 的 physical pages1–5。未冒 PDF render/view、源字节认证或首次全文发现：R81 已有全文 HTML 记录，当前 spec 已纠正此历史。

又实际读 Nadjimzadah2609.06299v1 的 Def2.1、Prop2.2 及 §3证明；在线读 [2503.15760v3](https://arxiv.org/html/2503.15760v3) 的 Def2.1–2.2、Condition2/4、Remark2.6、Cor2.10 和相邻说明。后一个高级 projection theorem 的 wholeproof 未独立重证。Du 的初等构造以下逐式核，matching Hausdorff lower 保留该具名依赖。

资格任务是同一紧集合能否在某 n≥5 包含每个真实方向的单位直段并保 dim_H<n。原相位方向 (p,q)、拉直后已展示的线族方向、以及集合里所有可能额外线段的方向是三个不同对象。仅分类源所展示的线族，不声已经分类 K′ 内全部线段。若以下实际补齐或合法 lift 不给完整资格，就停止本入口，不续 rotation/codimension/clock 模板。

## 2. 原相位、Hörmander 与 worst compression 的直接核算

源族和相位为

\[
X(w,t;p,q)=\bigl(w_1-tp-t^2(q+p^2/2)-t^3p,\ w_2-tq-t^2p\bigr),
\]
\[
\phi=x_1p+x_2q+\tfrac t2(p^2+q^2)+t^2(pq+p^3/6)+\tfrac{t^3}2p^2.
\]

解 \(\nabla_{p,q}\phi=w\) 恰得 X。混合 x/y 导数为 I₂。因 G 的第三坐标为1，H2 的矩阵是

\[
\begin{pmatrix}1+2tp+3t^2&2t\\2t&1\end{pmatrix},
\qquad \det=1+2tp-t^2>0
\]

于原小域。正常形中 R=0，\(S=(-q-p^2/2-tp,-p)\)，故 \(|S|\le C|(p,q)|\)。这是实解析 Hörmander 族，不能据此推拉直后的角度满性。

若 C² 的 W(p,q) 在非空开参数域使所有 t 的 union 落二维 surface，令 \(DW=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\)。rank 必迫

\[
0=AD-BC-(A+D)t+(1+B+C-pD)t^2+(p-D)t^3.
\tag{1}
\]

故 A=−p、D=p、B+C=p²−1、BC=−p²；两个可能的 (B,C) 是 (−1,p²)、(p²,−1)。两 branch 由 p²+1≥1 隔开，连续 DW 在小连通邻域固定其中一个。于是 \(\partial_pD=1\) 而 \(\partial_qC=0\)，违反 W₂ 的混合偏导相等。源 worst-compression 定义的 direction Jacobian 满秩允许局部将其两个时间参数换成 (p,q)，得到这样的 W，故该否定成立。这不否定任意粗糙 selector 的分数维压缩。

## 3. 二进制 Heisenberg Q 的紧性与精确 cylinder

对两列 \(e_i,f_i\in\{0,1\}\)，设

\[
x=\sum_{j\ge1}2^{-j}e_j,\quad y=\sum_{j\ge1}2^{-j}f_j,\quad
z=\sum_{i<j}2^{-i-j}e_if_j.
\]

统一绝对收敛使这是 compact sequence space 的连续像 Q。\(\operatorname{proj}_{x,y}Q=[0,1]^2\)，且 \(0\le z\le1/3\)。固定前 n 位，写 r=2⁻ⁿ 和相应 (x₀,y₀,z₀)，则该 piece 精确为

\[
(x,y,z)=(x_0+rx',\ y_0+ry',\ z_0+r x_0y'+r^2z'),\qquad (x',y',z')\in Q.
\tag{2}
\]

跨 prefix/tail 的和是 \(r x_0y'\)，双 tail 项是 r²z′，故 (2) 不是近似。二进制端点双表示只使 pieces 重叠，不影响覆盖或满投影。4ⁿ 个 pieces 各直径 O(r)，所有 dyadic scales 给 upper-box≤2；满平方的 Lipschitz 投影给 Hausdorff≥2。因此 Q 的 Hausdorff、packing、upper-box 均等于2。

## 4. Q_s、原 E 与全相位方向的真实覆盖

取 \(\varepsilon=1/100\)、\(s_0=4\varepsilon\)，定义固定可逆仿射像

\[
(p,a,b)=\bigl(s_0(x-1/2),\ s_0(y-1/2),\ s_0^2(z-y/2)\bigr)\in Q_{s_0}.
\]

于是 \(\operatorname{proj}_{p,a}Q_{s_0}=[-s_0/2,s_0/2]^2\)，\(|b|\le s_0^2/2\)。再设

\[
E=\{(-a,b,p,a-p^2/2):(p,a,b)\in Q_{s_0}\}.
\]

该嵌入在 bounded 区域 bi-Lipschitz，逆直接取 p、−w₁、w₂，所以 E 的三种维数均为2。给定 \((p,q)\in\overline B_\varepsilon^2\)，令 a=q+p²/2；则 \(|p|\le\varepsilon\)、\(|a|\le\varepsilon+\varepsilon^2/2<s_0/2\)。满 (p,a) 投影给 b。取 w=(−a,b)，由 \(|b|\le8\varepsilon^2\) 可核 \(|w|<2\varepsilon\)，故源的完整相位方向球覆盖是真的。

原集合 \(K=\{(X(w,t;p,q),t):(w,p,q)\in E,\ |t|\le\varepsilon\}\) 是紧集，包含同一 E 的全部固定 clock。它的上界不是粗加 dim E+1=3，而要使用下一节的实际各向异性。

## 5. 全 clock 的真直线化与 upper-box 上界 5/2

固定 diffeomorphism

\[
\Psi(x_1,x_2,t)=\left(-\frac{x_1}{1+t^2},\ x_2-\frac{tx_1}{1+t^2},\ t\right),
\quad
\Psi^{-1}(U,V,t)=(-(1+t^2)U,V-tU,t)
\]

在有关紧邻域 bi-Lipschitz。代入原 E 得

\[
\Psi(X((-a,b),t;p,a-p^2/2),t)
=\ell_{p,a,b}(t)=(a+tp,\ b+t p^2/2,\ t).
\tag{3}
\]

从 (2) 令 R=s₀r，每 piece 有 \(|\Delta p|+|\Delta a|+|\Delta b|\le CR\)、\(|\Delta b-p_0\Delta a|\le CR^2\)。对 (3) 令 U=Δa+tΔp、V=Δb+t(p²−p₀²)/2，则

\[
|U|\le CR,\qquad
|V-p_0U|=|\Delta b-p_0\Delta a+\tfrac t2(\Delta p)^2|\le CR^2.
\tag{4}
\]

每 piece 的整个 clock union 因而落在一个 O(1)×O(R)×O(R²) parallelepiped。其 frame 三列是 \((p_0,p_0^2/2,1),(1,p_0,0),(0,1,0)\)，det=1 且 condition 固定，故可以固定倍 rectangular box 包络。共 O(R⁻²) 片；每盒在 R² 半径需 O(R⁻³) 球，总 O(R⁻⁵)。相邻 R² 比4，给所有充分小尺度的 upper-box≤5/2，从而 dim_H K≤5/2。

## 6. matching Hausdorff lower 的准确 named 输入

写 \(F_t(p,a,b)=(a+tp,b+t p^2/2)\)。固定同一物理点解 position 为 (a′,b′) 后，spread velocity 为 \(\omega(p')=(p',p'^2/2)\)。于是 \(\det(\omega',\omega'')=1\)、\(\gamma=(1,p)\ne0\)，position Jacobian 对 (a,b) 为 I₂；bounded 区域的其余相关导数均有固定界。参数次序应是 source 的 position=(a,b)、angle=p，不把三个字母的名字混同。故其 basic conditions 与 coney 假设已在本例核实；固定 clock 平移缩放仅改变常数。

引用 [Nadjimzadah2503.15760v3 Cor2.10](https://arxiv.org/html/2503.15760v3#S2.SS1)：对 Borel、Hausdorff 维2的 Q_s，coney restricted projection 分支给几乎每 t 的 \(\dim_H F_t(Q_s)\ge3/2\)。这里只调用 coney 分支，不赠 twisty 的更强数值。再用标准 Hausdorff slicing lower 得 \(\dim_H K'\ge1+3/2\)。结合 (4) 以及 Ψ 的 bi-Lipschitz 性，源的 dim_H=upper-box=5/2 在所列 named 输入下成立。高级 projection theorem 的 wholeproof 和一般 slicing theorem没有在本文重新完整证明。

## 7. displayed 直线方向、restriction 与两种 shading 密度

源展示的真实单位方向是

\[
d(p)=\frac{(p,p^2/2,1)}{\sqrt{1+p^2+p^4/4}}.
\tag{5}
\]

其对 p 导数非零、对 q 导数为0：相位的二维方向球没有被 Ψ 送成二维角域。固定 p 变化 q 是改变 a/intercept。若原参数取 δ 分离网，约 δ⁻² 个相位方向可在仅 O(δ⁻¹) 个 displayed 直线方向帽中出现，不能继承原角度分离。

(5) 不分类 K′ 中所有可能额外线段；例如后文矩形有其它斜率。资格门拒绝的是当前展示并验证的构造未提供全方向，而非从一个 Jacobian 宣告原集合绝无任何额外方向。

whole-label restriction 只减小已验证方向覆盖；shading restriction 不论平均或逐管 λ>0，都不能还原完整 unit segment。对有限加权 tube 族，Ψ 的体积 Jacobian 和正反 Lipschitz 界使同一 measurable mark 的 density 可比：逐管 lower 逐条继承，平均 lower 也按同一权总和继承。仅平均 λ 要取 density≥λ/2 的 labels，可保至少 λW/2 权及 λ/2 逐管 lower，未归一角帽 upper 可保；这并不保全部方向。本文没有从 Du wholecurve 构造推出任意 marks 的统一估计。源 cited coney theorem自身另有有限 shading 结论，也不能补方向或将每个 label 不同的 marks 当共同全参数 slice。

## 8. 真产品和自由 fibers 的方向秩核算

在 n=3+k 取 \(K'\times[-C,C]^k\)，其 upper-box≤5/2+k=n−1/2，且继承的直线可配额外 bounded slope β：

\[
(a+tp,\ b+t p^2/2,\ t,\ z+t\beta),\qquad |t|\le\varepsilon.
\]

同一大盒可容全部 z+tβ；它们方向参数 (p,β) 共 k+1=n−2，低于所需 n−1。这是已构造方向的不足，不声产品中所有未知线段都已分类。固定 dilation 可把原 clock 长2ε的直段统一变成至少单位长，不能提升方向秩。

若取 m 个独立 K′ 的 Cartesian product 并可独立 reparametrize 各时钟 \(t_i=c_i+\alpha_i t\)，每块非零方向为 \(\alpha_i(p_i,p_i^2/2,1)\)。所有非零块共2m个参数，去整体尺度后≤2m−1；在 R^{3m} 的方向维数需3m−1，仍缺 m。加 k 个自由坐标只两边同加 k。这里没有把产品中未展示的线段自动补全，也不续更多产品模型。

## 9. 独立旋转或 missing-slope 自由化的实体满维反攻

Q 中取 e₁=1、其后 e=0；取 f₁=0、其后任意。则 x=1/2、0≤y≤1/2、z=y/2，故

\[
p=b=0,\quad a\in[-s_0/2,0],\qquad
\{(a,0,t):-s_0/2\le a\le0,\ |t|\le\varepsilon\}\subset K'.
\tag{6}
\]

将同一个 K′ 绕 t 轴作所有 θ∈任意开角区间的独立旋转并，(6) 扫出径向、角向、时间向均有正宽度的扇柱，故实际3维 Lebesgue 体积>0；不是由粗 upper≥3 推出满维。乘有内点的 k 盒后实际 n 维体积>0。全圆旋转时，原 (5) 的 horizontal magnitude \(\sqrt{p^2+p^4/4}\) 从0连续扫到正数，的确补出一个开 slope disk；再配 β 和有限 ambient rotations 可覆盖全方向，但已无严格低维。

仅有限或可数 rotations 的 displayed 方向是可数个低维光滑像，角测度0；若取 dense rotation 后 closure，(6) 的柱体也进入 closure，不能免费用闭包修紧性。另一种真实 missing-slope completion 是把原 y 坐标加 qt：

\[
\ell^q(t)=(a+tp,b+t p^2/2+qt,t),\quad q\in[-c,c].
\]

方向 (p,p²/2+q,1) 有开二维像；但 (6) 已使 union 包含 \(\{(a,qt,t):a\in(-s_0/2,0),\ t\in(\varepsilon/2,\varepsilon),\ |q|<c\}\)，这是 open wedge，实际正3体积。上述反攻只针对这些独立 completion，不否所有依赖原 label 的选择、任意其它映射或未知构造。

## 10. 全 open 参数、原 clock 下所有有限零损失 lift 的反证

按实际 Def2.1，设 \(m=2+s\)，有 \(\pi_t:\mathbb R^m\to\mathbb R^2\)、a(y,w,ρ)、Θ(y,ρ)，在全部 open 内参数及非退化 I 满足 \(\pi_t(a+t\Theta)=X(w,t;y)\)，且 \(J=D_{(y,\rho)}\Theta\) 可逆。固定同一 P=(p₀,q₀,w₀,ρ₀)，令

\[
T(t)=D_z\pi_t(a(P)+t\Theta(P)),\quad W=a_w(P),\quad
C=a_{(y,\rho)}(P)J^{-1},\quad P_1=[I_2\ 0]J^{-1}.
\]

同点链式法则精确给

\[
TW=I_2,\qquad T(C+tI_m)=F_{p_0}(t)P_1,
\quad F_{p_0}(t)=-t\begin{pmatrix}1+p_0t+t^2&t\\t&1\end{pmatrix}.
\tag{7}
\]

Θ 独立 w 才有第一式。删 det(C+tI)、detF 的有限零点后，原 I 中仍有开子区间，得到

\[
F_{p_0}(t)^{-1}=P_1(C+tI_m)^{-1}W.
\tag{8}
\]

两侧有理，开区间恒等允许清分母成多项式恒等。右侧在形式无穷远 O(1/t)，但左侧 (2,2) 项是 \(-(1+p_0t+t^2)/(t(1+p_0t))\)：p₀≠0 时趋 −1/p₀，p₀=0 时为 −t−1/t。矛盾覆盖所有有限 s 和每个方向内点。这里 π 自身不必 affine、analytic 或在原 clock 外有定义；比较的是由原区间导出的有理恒等式。只是 R50 必要变分法的应用，未调用原 parameter-linear 分类的充分方向。

只在 rough E 上、Θ 依 w、允许 time change、非零 direction loss 的 lift 均未被 (8) 排除。全 open w 正是可微右逆责任，不能用源位置 selector 代替后还冒全族定理。

## 11. 可行有损 lift、投影方向与实际正五维体积

A 给出且本文独立代入核过的合法 (s,ν)=(3,1) 例：ρ=(r₁,r₂,r₃)、z∈R⁵，

\[
\pi_t(z)=(z_1+tz_3+t^2z_5,z_2+tz_4),
\]
\[
a=(w_1,w_2,-p-r_1,-q-r_2,-q-p^2/2-r_3),
\quad \Theta=(r_1,r_2,r_3,-p,-p).
\tag{9}
\]

π 前两列为 I₂，rank DΘ=4，全部参数/all clock 代入就是原 X。Nadjimzadah Prop2.2 用 full inverse image 的一般 upper 是 dim_H K+s≤5.5；ν=1 后投影的 effective ambient 是5，预算无严格余量。一般 upper=s+2.5=(3+s−ν)+ν−0.5，而 (8) 迫 ν≥1；不能由该预算自动得严格反例。这不证明所有特殊 inverse subsets 实际达到该 upper。

具体 (9) 丢 z₅ 后，真实 slope=(r₁,r₂,r₃,−p,1) 覆盖开4维方向域。对同一个原 E 的 (6)，即 p=b=0、q=a，所得实体点为

\[
(-a+tr_1,\ tr_2,\ -r_1+tr_3,\ -a-r_2,\ t).
\tag{10}
\]

固定 t≠0，(a,r₁,r₂,r₃) 到前四坐标 determinant=t³。取 a 的内部、ρ 的内部、一个非零时间开区间，(10) 是局部 diffeomorphism，因此该具体投影后 full-direction-patch 构造实际含 R⁵ open subset。这里只反该正 ν 构造，不泛称所有正 ν lift、所有更小 fiber 或所有其它 completion 均不可能。

## 12. 实际交叉审查、通过范围与停止

已实际全文读 A12 `R0086_actual_Du_lift_qualification.md`，以及 root8 `R0086_full_clock_resolvent_and_actual_direction_certificate.md`。独核 A/root 的 Def2.1 全量词、同点 (7) 到 (8)、开 clock 的有理恒等、p₀两情形、(9) 的全参数/rank/投影及 (10) 的 determinant；均未发现必须修正的数学问题。root 的 Q_s 实矩形、任意非空旋转区间正体积和原 whole-label/shading 量词亦逐式通过。B 自己的 Q/upper 和 completion 计算不以本节自审冒第二次独审；已交 A/root 实际独核。

需保持的字面边界是 (5) 只为原 displayed family，不能误读成集合中全部线段已分类；本稿已显式收紧。matching lower 的基本条件本例已核，但外部 advanced wholeproof 仍 named；无 PDF 视觉/字节新认证声明。后续 formal 只有实际授权后另写，不预认证未来 meta/Git/sync。

结论是源的 compact2.5维曲线构造与其 proper-direction 真直线族成立；全部 Def2.1 原 clock/full-w 零损失 lift 已否；若干实际独立 direction completion 或具体正 ν lift 真有正 ambient 体积。本 source 未产生 ordinary n≥5 满方向严格低维反例。按 spec 冻结本入口，不续更多 fixed times、clock、rotation、产品或 codimension 参数；不新增 ID/major，不把资格证书叫 Goal 完成，未经外部同行评审。
