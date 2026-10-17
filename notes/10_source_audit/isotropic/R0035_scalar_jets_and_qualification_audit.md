# R0035：标量 jets、qualification 与 Cartesian 状态提取

2026-10-17。独立源审计；本稿只处理原 j=1，或 j=2 且 ℓ=0 的接口。不是整篇四维证明的认证，也不是五维新界。固定入口为 GOAL/STATE、R0035 working_spec；当前目标是为完整 Theorem 6.1 审查支付其前半部，不能以工具通过替代候选存在。

## 1. 已读范围、依赖与停止条件

原 PDF 页70–98，提取文本3735–5283行逐式读过：Cor4.13、§5.1–5.6、§6.1–6.5；Theorem6.1 的整条后半部须另读 root 整合及另一代理的 potential/conic 稿后再出正式 review。页码为正文页码，与本 PDF 物理页一致。提取位置按 `split('\n')` 计，不能以 `splitlines()` 吞掉 form feed 后的行号代替。

外部确切输入：Wang–Zahl, *Sticky Kakeya sets and the sticky Kakeya conjecture*, [arXiv:2210.09581v2](https://arxiv.org/abs/2210.09581v2)，v2 为2025-10-07，JAMS39(2026)515–585；本库 `literature/primary/wang_zahl_2025_sticky_kakeya_2210_09581_v2.pdf`，已读 Def4.2（页17，文本901–908）、Thm5.2（页31，1655–1666）及 §8 开头重述（页49，2682–2698）。这里只核 statement/application，不认证其 radial projection/Bourgain 等完整高级证明。Lemma5.1 调用已具名审查的原2.15；§6 的 determinant multilinear estimate 调用 Carbery–Valdimarsson Theorem1（root 核确切 statement），仍保 named input 状态。

反攻对象：不均匀/相关事件的分母、预采 tuple 是否仍独立于原轨迹、发现一些好点能否推出 relative o(1)、稀疏选择后非法重用 breadth、同一 ν° 与 palette、物理/参数 zoom 错配、fiber polynomial 列表爆炸、缺失 Cartesian 顶点。停止条件为完整支付或明确合法缺口；不以数值秩样本或高维 toy 反原假设。

## 2. Cor4.13：breadth 必须先于稀疏选择

源页70–71/3735–3801。状态须含原 parent，在原 pL 有实际 path 因子与 log 的固定幂列表知识，且给 used deep history 只有 K=N^{o(1)} 个选项。结论量词是：每固定 κ,u>0，条件速度法则将至少 κ 质量放进 N^{-u} 线条带的状态总质量趋零。它不声称任意速度依赖的 K^{-1} 子族都 broad。

独立核重条带计数如下。先用 joint(history,velocity) upper 与状态 ambiguity，把被预测条带 palette 太小的事件删掉，剩余每条带 π 质量≥κ_N=1/K。参数以同时变号取商，取 r1=N^{-u/2} 分离极大族。若两个条带在 |v|≤T 相交且参数相差≥r1，则法向角≥c r1/(1+T)，交集直径≤C(1+T)N^{-u}/r1≤N^{-u/3}。角球 cap 与 Cauchy–Schwarz 给

`(M κ_N)^2 ≤ M + K N^{-Su/3} M²`，故 M≤K。

再以 r2=N^{-u/4} 分开参数；宽 C(1+T)r1 的扩大条带之间交集仍是固定幂小角球，K² 次并集可付。于是按 parent/velocity 的第一个包含代表分配整轨迹；参数及横向位置用 r2 bins。此为 whole-block assignment，横轴宽 r2，行列式获得固定正幂 narrowness。原状态只负责输出列表成功，有限几何 map 的实际化交给4.12/4.6，不能把分析状态预测表当 tempered 输出。v1 用角 interval cap，不用二维重条带引理。

因此可在任何 substantial residual **重新**准备 breadth；其后选 whole states 不改条件法则，只删状态内小固定比例则 spanning 概率只损受控常数。选走 K^{-1} 个速度后不得追认仍 broad。§6 的 strip filling 前最后一次使用 breadth，随后只继承已证 upper support lists，是合法的分界。

## 3. Lemma5.1：标量二次系数聚类

页72–73/3831–3882。输入是 raw νdt 的 dense 标记、≤K p^{-1-d} 个(t,x)格、ν 的系数球 cap K r^d（r≥p），不是逐点 AD lower。删短标记后加入独立 D∈[0,1]，把 `x0+t x1+t²x2` 写成 `(1,t)·(x0+t(x1−D), D+t x2)`。其 lifted support ≤Kp^{-2-d}。

原2.15给时间满的平面 plank，宽 p/K≤u≤v≤K，lifted 质量≥p^{d−1}uv/K。来自同 plank 的标量二次多项式全时差≤Kv；三时刻插值把系数放入 Kv 球。固定标量轨迹时，D 的方向为 (−t,1)，任意单位短法向在 t=0 或1的投影绝对值≥c，故 D 接受长度≤Cu。于是 lifted 质量≤K u v^d。比较得 `v^{1−d}≤K p^{1−d}`，即 v≤Kp；再除 D 长度 u，标量系数质量≥p^{d−1}v/K≥p^d/K。半径 Kp 球只需 K 个 p-bins。这一结论对新 dense 标记残余重新成立，因为所有输入为 raw upper 或重新验证的总密度。

## 4. Lemma5.3：必须在每个 tested event 重新计算

页74–75/3935–4011。令 T 为 world 与**整个预采时间 tuple**，预采在 world 内独立于轨迹；时间边缘 AC 足以避同一 null set，无须 tuple 密度 ceiling。A 是任意依赖全 tuple/轨迹的 dense event，且所有 tested labels 成立；Q=P|A，p_A=P(A)，s(T)=P(A|T)。直接积分得到

`E_Q(1/s(T))≤1/p_A`，`E_Q log(1/s(T))≤log(1/p_A)=o(log N)`。

固定 T 的轨迹先验仍是原 world prior，因此剪切 (x,y)→(S=x−Fy,y) 的 joint r-bin raw 质量≤Kr^{j+d}。Q 条件质量只多 1/s(T)，熵≥(j+d)log(1/r)−o(logN)。支持数 S_r≤Kr^{-d}、y_r≤Kr^{-j} 给 (5.9)/(5.10) 的匹配上下界。

再令 B=l_r。tuple 独立性使 restriction 前给 B 的轨迹法则正是原 (5.8) within-bin prior。固定 S_q 时相关 y_q bins≤K(r/q)^j，故 `P(A,S_q=z|T,B)≤K(q/r)^d`。同一个分母计算适用于 s(T,B)，不含 #B 或 minν(B) 的费用。于是 `H_Q(S_q|T,B)≥d log(r/q)−o(logN)`；B 内 S_r 只有 K 选项，而 local support 给 `H_Q(S_q|T,S_r)≤d log(r/q)+o(logN)`，相减得 (5.11)。

单位行 e=e(T) 的 r-slab 在有界 y 范围只交≤Kr q^{-j} 个 q-cubes。因此从 `H(y_q|T,S_q)` 减去此覆盖熵，得到 `H((ey)_r|T,S_q)≥log(1/r)−o(logN)`，即 (5.12)。

这里没有把旧事件上的 entropy 偷渡到小 discrepancy event：每个后续 dense event 使用其自己的 p_A、s(T)、s(T,B) 重算。若事件只有固定幂小概率，则 log(1/p_A) 是主阶，以上 o(logN) 就失败。这是明确边界。

另核 (5.14) 确为一般离散恒等式推论：`H(Z|T,C)≤H(Z|T,B)+H(Z|T,A)+I(A;B|T,C)`，由 chain rule 与 `I(Z;B|T,C)≤I(A;B|T,C)+H(Z|T,A,C)` 得到，不需变量独立。

## 5. Proposition5.4：完整 first jet 与确切 dot-product 输入

页76–81/4018–4321。局部 search 前先付当前 m(t) floor 与每 H-block 质量 floor；不能先找到少量时间再声称全局 dense。 surviving blocks 数≥δ/(2H)，其 prepared active times 的原 m(t)≥τ，δ、τ 均 inverse-subpower。固定标量起始 H-bin C 后除 H^d，再固定 j−1 个切向 p-bins 后除 p^{j−1}；每次 light group 删除先按原权重求和，不按组数免费均匀化。

以 p=H^{1/4}，方程为 `L=z+uG(v)−φ1(u)v+O(Kp)`。固定第一轨迹在 u0 的标量 p-bin，剩余 collision 质量≥p^{2d}/K；每 (u,v,v′) p-cell 质量≤Kp^{3+2d}，故 represented triples 的 p-cover≥p^{-3}/K。每时刻总 pair 质量≤Kp^{2d}，先删活动时间长度<p/K1 的时间 bins，才选 quadrant；保存的是 **pre-quadrant 的真实活动集 T_J**，不是把整个 p-bin 当标记时间。

WZ Thm5.2 的输入正好是：F,G⊂[0,1]²，所有 p≤s≤w 的 upper cover≤p^{-η}(w/s)，以及**任意受限** H⊂F×G×G 的 E_p(H)≥p^{η−3}。其 ADset 定义只有 upper，没有 lower；原稿5.5因此未缺一项 AD lower。WZ alternative(A) 甚至要求第二条正交线经过原点，原稿只需第一条线更弱。alternative(B) 在某 s≥p、|J|≥p^{-η}s 上产生 exponent1−ε 的输出覆盖。此为 named 高级输入，未重证。

应用归一化要同一坐标反射以保 dot product、两个正比例缩放≥K^{-1}、**只平移第二个图集**，因 b−b′ 消去该平移；不能任意平移第一个集。图比较给所有尺度上 K w/s upper。dot products 由(5.23)位于一个固定起始 scalar 支持的平移 Kp 邻域，因此输出 cover≤K(|J|/s)^d。取固定 ε<1−d，与 `(|J|/s)^{1−ε−d}≤K`、`|J|/s≥p^{-η}` 矛盾。subpower dilation/error 被固定 η 吸收。

第一集近线 alternative 给≥p^{ε−1}/K 个时间 bins，线斜率≤K，因为水平跨度≥p^ε/K≫Kp。graph comparison 把每个 represented point 的 fit 扩到保存的整个 T_J；实际 fit 时间总长≥Hp^ε/K。令 ε 慢趋零才是 H/K。此时恢复这些时间上的**所有** prepared labels，原 m(t) floor 与 surviving-block 数给全局质量≥δτ/(2K)。没有从临时切片组的少量成功直接推全局密度。

对 j=2 两分量、有限 scale hierarchy 顺次重复，重算每次 δ,m,τ。邻尺度 H′≥H^{33/32}/2；在预删除共同 µ_fit 上删低质量 child，再以其先前≥H′/K 的时间集比较两 affine fits，斜率差≤K H^{5/4}/H′≤K H^{7/32}。有限链相加给(5.15)的 H^{11/10}，不要求后续 surviving 时间仍满。

残余斜率 k 在 p0=H_*^{1/8} 的 Y-cell 内变动≤Kp0。若每宽 p0^γ（γ=(1−d)/4）区间质量≤N^{-c}，删短轨迹及 light Y-cells 后，close-slope collision≤Kp0^d N^{-c/2}，far-slope collision≤Kp0^{1−γ}=o(p0^d/K)，反 collision lower。故每 good group 有 inverse-subpower 重斜率区间。给 (t,S_H) 和给 (T,l_r) 两种条件都得到 J1 的确定短列表，再在每个 tested event 用§4的 mutual information 与(5.14)回到 (T,S_r)。

## 6. Proposition5.6：预采树、精度顺序与 fiber 投影

页81–85/4324–4573。先定 M,d,h，再定有限固定幂尺度：r_min=.009·4^{−(M−2)}、α0=(1−d)/64，H1^{r_min}≤h^{M+11}，H_i^{r_min}≤H_{i−1}^{1.02}，H_*^{α0}≤H_{M−1}^{1.02}；floor ζ≤K^{-1}min(H_*³,h^{M+1/2})，可再取固定幂 buffer。所有行均在 tuple/trajectory restriction 前成为仅 world 与 tree 时间的函数。

u 均匀，树在逐层 H_i-block 内独立补时间；t′ 独立均匀于 u 的 h-block。原轨迹独立于整个实验。反复条件平方与 Jensen 给所有叶及 t′ 标记事件概率≥原单时密度的固定次幂；小 pair gaps 的原概率≤C/K1，先选其预算低于整个成功概率。没有在已条件化的全成功事件上再次假称 child 独立。

在 H pair，q=H^{1.01}。已知 child jets 后可在给(T,S(t)_q)下以 o(logN) 熵读 S(w)_q 及有限 jets。精确 divided difference 为

`∇J_i=x^(i+1)(t)−(∇F_i)y(t)−(F_i(w)+i∇F_{i−1})y′`。

前级兼容使最后系数 bounded K。若 ∇F_i 在某固定幂阈值以上的事件 dense，则除其 T-known 大小，读出单位行 y 投影的固定幂精度；选择读宽比 pair scale 和 nuisance 都粗、仍固定幂小，与(5.12)矛盾。故所有固定幂大 tails 为 relative o(1)，可慢选 K。相同方法把 `∇F_i−F_{i+1}` 限在 H^{r_i/2}，并由(5.14)把新 jet 从(S_q,l_r)两种读法转回S_r。根/子读宽的严格余量正由上述 schedule 提供，不能先给 floor 再事后要求更细。

令 P_F 为根处 degree-M Taylor polynomial；E=F(t′)−P_F(t′) 为 T-known。精确代数式

`S(t′)=Σ_{i=0}^M J_i(u)(t′−u)^i/i!−E y(t′)+O(Kh^{M+1})`。

在 |E|≥h^{M+1/4} 的 dense event 上，condition(T,S(u)_p)，p=h^{M+10}，根 jets 仅耗 o(logN)。宽 |E|r、r=h^{1/4} 的 scalar 支持≤Kr^{-d}；其合法 floor 为 |E|r≥h^{M+1/2}。除 E 后 nuisance 为 Kh^{3/4}，用 y(t′)=y(u)+O(Kh)，推出单位行 y(u) 的 r-bin entropy≤d log(1/r)+o(logN)，与事件上重新证明的(5.12)矛盾。

最后冻结 (world,l,tree) 而保 t′ 的先前 h-block 均匀条件法则。对实际成功 fiber fraction 做 light-fiber 删除，得到长度≥h/K 的真实 labeled witness，且包含 counted t′。restriction 前(l,t′)边缘正是 νdt（按 h-block 长度采 u）；投影成功 tuple 不会凭空产生更多 incidence mass。输出只是在每个 dense 输入中有 dense 发现，尚非全部参考点 qualification。

## 7. 同一 physical prior 到 scalar-normal world

源页86–91/4610–4881 为本应用必要前置。所有 incidence 以 `λ=σν°dt≤Kν°dt` 表示，ν° 是 preceding long occupation 轨迹 prior 的**一次冻结、未归一化**子先验。以后删 labels 不重置 ν°，也不把旧 coefficient-bin lower 追认为新 incidence floor。

这里必须显式支付双向 density 比较；另一代理独审指出，仅 `λ≤Kν°dt` 不能把 λ 的 upper caps反传到 product-prior labels。若原路径是归一化 indicator density，其 support 上 σ≥1，则直接可用。若只假 §6.1 的任意 0≤σ≤K，先在有限准备预算中删 σ<K_cut^{-1} 的 events；按 `Σp_γν_γ°≤1`，其总 λ质量≤K_cut^{-1}，取 K_cut为比全部 entering inverse-density更大的 subpower即 negligible。其后所有 boolean restrictions保留同一 σ，因此在 label support 上 `K_cut^{-1}ν°dt≤λ≤Kν°dt`。若过程另改 raw density，须重新付此阈值，不能追认旧 lower。以下 upper传递使用 lower比较，dense label质量使用 upper比较；两者用途相反。

physical count `#W_p≤Kp^{−(m+d)}` 先由 actual packet 质量下界 p^d H^j、每 H-block disjoint assignment、gradient K、m=j+1 得到；再删全局 light cells，给 hereditary local support。gradient 若固定幂大，会在深历史可知的 packet/ball/sign/base 状态预测 V 薄条带，Cor4.13排除；这一步须在 arbitrary sparse selection 前。系数块 (6.6) 的 lower 由 Lemma5.1 反全体 light coefficient-bin 残余：先按 affine (y0,V)_p 以原 palette 归一化再聚类，不能由 floor 单独推出 affine marginal upper。

(6.9) 块/cell 列表也先按 `pν°(B_p)/K1` 删除 entry，并以同一个 joint cell×velocity upper 支付。物理图构造后先恢复 W_b 状态内 breadth 与 palette domination，冻结 G 和 Λ_ref；L_ref 有常数下界。G 的 coarse row lists 是由有 palette-product 质量≥1/K 的 actual spanning witness tuples 及(6.9)计数得出的 support statement；后删 witness 不破坏此 support list。这里不假定不同时刻速度独立。

Prop6.3 在失败残余上 renew 后用 Lemma6.4 选 G；其每 world 损失仅 `Π_i(4^D K_i)^{-1}`，与 cell/world 总数无关。取固定有限 grids 后再慢加密，令 ΣlogK_i+DLlog4=o(logN)、相邻比A=N^{o(1)}，得到 G 的 K-Lipschitz **带 floor ρ** 比较，不声称真正全局 Lipschitz。

在 C=W_ρ 中以常行 G_C 分 width-p normal strips，p=ρs′、s′≥ζ≫ρ。沿 active 轨迹 normal derivative≤Kρ，且该 derivative affine；其在任意两 active times 间仍有此界。因此 normal range≤Kρ²+Kb≪p，每线仅 K 个 strips/C，全部 C/strip 数≤K/ρ。删 duration<ρ/K1 的部分，再删过损状态/strips，原总损失可在有限 grids 上求和；surviving strip 质量 M 的 contributing prior≤KM/ρ。最后一次用 breadth 与 multilinear estimate 得≥K^{-1}(ρ/p)^m 个 base cells。除 hereditary physical support count，得 (6.15) `#normal p-strips in r-interval≤K(r/p)^d`。此后只用冻结 upper lists，容许逐边删选。

真正 scalar-normal world 为 q=(γ,B_ρ)，**不是 physical cube C 的当前条件法则**。减 central coefficient curves、位置除ρ，时间不改；归一 prior 是 ν_γ°(.|B_ρ)。对细 subbin B_{ρr′}，固定时刻 numerator≤K(ρq′)^{j+d}π(V_{ρr′})，denominator≥(ρr′)^{j+d}π(V_{ρr′})/K，得到原(5.8)的 K(q′/r′)^{j+d}，r′=1给(5.5)。这是 prior conditioning，labels 以后只限制 raw numerator。

残余 R=x′−F ỹ′ 的精确式是 `ρR=G0+Gy v_c−X_c′+(Gy−F)(V−v_c)+O(b^κ)`。同(W_b,B_ρ)内 G 固定、|V−v_c|≤Kρ、F 的 floor ρ 比较，故 R range≤K(ρ+b/ρ+b^κ/ρ)≪ζ。对 β=ρs′ block，删 zoomed cell entry 质量<s′ν°(B_β)/K1；同一 cell 时间宽s′，moving physical cross-section宽β，所以 numerator与floor都含s′，不丢 β/s′ 因子。每 fine velocity bin 只支持 K 个 residual bins。

去 velocity 条件必须另付分母：旧 fine-state weights m0(W)，`λ(W,J)≤K_pre m0(W)π(J)`、Σm0≤K_pre。给 W 和 coarse I=V_ρ，只有 K_pre² 个 (W,B_ρ,zoomcell) entries；删质量<m0(W)π(I)/K_cut 者总损≤K_pre³/K_cut。于是每 survivor 条件速度≤Kπ(J)/π(I)，每 residual bin 的 supporting velocity palette≥π(I)/K。双计数得同 zoomcell 仅 K 个 residual bins。

再以 Lemma6.4 选同 world 的 residual comparison，允许删 individual edges；breadth 已不再使用。权重 a_q=p_γν_γ°(B_ρ) 总和≤1，所以 global selected mass δ≥1/K 给某 q 的相对 mass≥δ。除 a_q 后，以 `λ≤Kν°dt` 得原 fixed probability prior 的 dense labels；以已付的反向 lower比较将 scalar-normal caps转成该 product-prior labels 的 upper，损失 K_cut可吸收K。不是免费把极小 world 当均匀世界。

## 8. Proposition6.3：为何可升级为 relative o(1)

页91–96/4887–5162。固定 ε>0，把 U_{N,ε} 定义为**不存在** coeff≤N^ε、error≤h^M、duration≥hN^{-ε} 的 degree-M whole-row polynomial witnesses 的 reference incidences。若其相对质量不趋零，L_ref≥c 给 substantial 失败残余，保持原 parent mixture 权重、G 及其 mesh 不变，在此 residual 从头进行§7准备。发现 inverse-subpower 正质量已足够矛盾，不需发现相对常数质量。

上节 scalar-normal 输入允许 Prop5.6 在某原 coefficient world 输出 Gy 的 error Kh^{M+1/4}、duration h/K witness；(6.11)给 G0=X′−GyV+O(b^κ)，故 G0 也有同 degree-M fit。whole Q_s assignment 保同 h-block。固定 ε 后 N 足够大，K<N^ε、h/K≥hN^{-ε}、Kh^{M+1/4}<h^M/4；先声明的 coefficient grid 再舍入误差≤h^M/4，发现点属于资格集，反 U_{N,ε} 定义。

所以每固定 ε 的 relative failure→0。再对 ε_r=1/r 选 cutoffs，使失败≤1/r，并同时延迟有限 grids/preparation，取 K_qual=N^{1/r(N)}。这是合法慢对角，不给 finite-N nullness，不给显式 rate，也不能传到任意后来稀疏子族。恰恰因为反证对象是每次新的 substantial failure residual，此处不是“存在一些好点”推出“几乎处处”的跳步。

## 9. Cartesian interpolation：状态、palette 与一个坐标修正

页96–98/5164–5283。先取 α∈(0,1/2)，ε_T=h^{1/k−1+α}，a1=a h^{α/2}；a2 与 e2 均预声明。把 physical mesh b、qualification scales、descendant depths a1,a2 与足够细 base grid ξ 全部放在 G 构造前。须明确取 `Kξ≪ε_T`，并满足文本列出的 `Khξ≪a1`、b/h≪ξ；“all later evaluations accurate”包含前一个更细要求，单独后一个不推出前一个。

状态 D=(parent,Q_s,W_b) 具实际 old-pL 知识与 deep-history ambiguity。重新准备 palette/breadth得到 Λ_prep≤Λ_ref 且总质量≥c。若 q_D 为该状态中不 qualified 的比例，则

`Σ_{q_D>η}m_D≤Λ_prep(U_N)/η≤e_N L_ref/η=o(1)`。

取固定 η≤p0/(2m)，一组 m 个条件独立 draw 同时 spanning 且 qualified 的概率≥p0−mη≥p0/2。因此只删少量坏状态后有常数总质量；不先把 Λ_prep 限到 qualified edges 再假称 breadth 保留。插值完成的结论只依赖 state 时，才能恢复该 state 的其他 prepared edges。

选择 parent/Q 时用 `Σ p_γ hν_Q≤1`，得到 good-state mass≥hν_Q/K。u=(z−z_c)/h 无速度 shear，原 normalized base ceiling给每 u-cell质量≤K hν_Q ξ^m。每 fine base cell 上 G 的 ε_T-bin 列表≤K：packet graph X=f(z)+O(Ka)、|∇f|≤K，而 ε_T≫Ka；该 cell 用至多 K 个 physical ε_T cells，适用 frozen coarse field lists。

对每状态，conditional product tuple 的 qualified spanning 事件概率常数，palette domination给其 product-palette measure≥1/K。先固定 parent 后 π 不再随状态改变；对状态质量积分并交换积分，存在**一个共同速度 tuple**，其各 bin 都有见证的状态质量≥hν_Q/K。不是给每状态另选坐标系。令 A0 的列为 v_i=(1,V_i)，则 ∥A0∥+∥A0^{-1}∥≤K。

**原5220行有上标串行提取歧义，不是源笔误**：PDF页97在 A0 旁明确有上标 −1，应读在 `r=A0^{-1}u` 中取 product grid。另一代理先独核原页 bbox，随后本稿用原 PDF text spans 交叉确认；不能按纯文本残缺顺序误读为 A0u。因为 u 沿 v_i 变化时，r 才只变第i坐标。以下一律用 PDF 的正确坐标；线性变换、体积、grid count 与系数 bounds 均只付 K，不改变 exponent 或先验。

每 direction/fiber 的 represented polynomial ε_T-bin 数≤K：为每 bin选一个原 qualified fit与见证线；该线在整个 block 内距 fiber≤Kξ。取 M+1 个独立均匀 block times，每个 witness-set长度≥h/K，因此成功且两两 gaps≥h/K1 的概率≥1/K。成功 tuple 上每时刻 row field 列表≤K，normalized-time Lagrange weights≤K；h^M≪ε_T、Kξ≪ε_T，故固定 tuple 最多 K 个 polynomial bins。对所有 represented bins 求期望，列表大小≤K。此计算使用原 reference field lists，不要求临时发现族仍有新 support lower。

每状态固定各方向一个 qualified witness；独立给每 fiber选一个 polynomial bin、每 cell选一个 field bin。每状态通过 m+1 个 size≤K 测试的概率≥1/K，故有选择保质量≥hν_Q/K。只要求 retained vertices 上 field center 与相应 fiber polynomial 差≤Kε_T；不声称整个 fiber已被填满。

删低于 hν_Q ξ^m/K1 的 cell，总成本≤K hν_Q/K1；原 base ceiling使 retained cell集合占整个 product grid 比例η0≥1/K。每轴独立取 M+1 anchors与一 target，反复 conditional Jensen 给全 (M+2)^m vertices 出现概率≥η0^{(M+2)^m}。anchor gaps<K1^{-1} 的概率可先取 K1大到低于此 fixed-power-of-η0 预算；fine mesh ξ 是固定幂，离散碰撞也低于预算。固定 separated anchors后仍有 inverse-subpower 比例 successful targets。

在 pure anchors 上作 tensor Lagrange interpolation得每 coordinate degree≤M 的 row T。成功 target 的所有中间 vertices 均已出现，逐轴用该 fiber polynomial比较，inverse-subpower anchor gaps使每步权重≤K，故误差≤Kε_T。cell floors把 target count转回 hν_Q/K 的真实质量。`|G(W_b)−T(u)|≤Kε_T`是 state statement，恢复所选 good states 的全部 prepared edges因此保 breadth/palette。

对 weighted duration≥h/K 的轨迹，原 density≤Kν°dt 给 ordinary duration≥h/K。X′−T(u(t))·v 为固定度 polynomial，Remez外推至**同一个 h-block**；不外推整个父时钟，得到(6.23)。

最后(6.24) descendant计数使用真实 a_i-packets：每 h_i-block轨迹质量≥a_i^d h_i^j/K、在 Q内disjoint、bounded-gradient joint cells≤K(h_i/(hξ))^m。乘 h/h_i 个blocks后为 `K ξ^{-m}ν_Q/(a_i^d h^j)≤K ξ^{-m}(a/a_i)^d`；m=j+1 恰使 h_i powers消掉。须 ξ先细到 hξ≪h_i，不能漏稀疏 fiber或descendant原质量。

## 10. 边界测试与待整合责任

1. 若只知在每 residual 找到正质量好点，但 residual 可有固定幂小概率，§8不能推出 reference relative o(1)。原命题以失败占 L_ref 的固定正比例反证，且 L_ref≥c，避免了此漏洞。
2. 若先取 qualified edges 的 inverse-subpower速度子族再调用 Cor4.13，非法；正确次序是先准备状态 breadth，删失败比例大的状态，再用固定tuple union bound。原§6.5确按后者。
3. same ν° 的 coefficient lower 是原长占用先验质量，不是当前λ floor。zoom/residual list的每个新分母都另作 entry 删除，当前代码不能省掉(6.18)。
4. 原 j2 cone/conic 与 planar dot product 均有维度内容。R1–R3 twisted-cubic/ruled-cubic 模型只反未付的高维迁移；不能当 j1/j2 isotropic 原假设反例。SCL 所记 N0 polynomial amplitude不自动给固定 tangent N幂；本节 scale需预声明、relative failure用慢对角，不能事后追随巨大隐藏幅度改 palette。candidate 的 actual-scale/guard仍须 AIM，而非从本稿强行推出。

目前前半部通过独立逐式检查，附上述 `A0^{-1}u` 提取校正、明确 ξ 精度要求，以及经另一代理提示补齐的 raw-density 双比较。未把此判定登记为完整 Theorem6.1。后半 signed paths、potential、heavy intercept、原七方向/conic、degree-two恢复及 actual candidate各项，须在正式 review 实读 root/B 全稿；外部5.5/6.10与既有2.15仍具名输入，不认证其完整高级 proofs。
