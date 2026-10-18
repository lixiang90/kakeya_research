# R0084：真实 factoring 的原阴影、完整 PW 与各向异性边界

2026-10-18，B 阶段 I 独立审计。未锁新 gain 定理，未作正式终审；不认证普通高维 Kakeya、重大性或外部同行评审。

## 1. 实际读域与原量词

已读 GOAL、STATE 顶部、ROADMAP、registry 当前入口、R83 next6、R84 working_spec5；实际全文读 R43 B7/root10 与 R49 B8。一手读域为 Hong Wang ICM2026 官方 HTML §6 的 Lemma6.10、相关定义与 Conjecture6.14；没有冒称下载或视觉核验正式 PDF。另实际读既存 GWZ streamlined v2 的 §2 定义、§3 heredity、Lemma4.1 完整 greedy proof/Remark4.2–4.3/Definition4.4，以及 §5 Proposition5.1、Remark5.2–5.4、Lemma5.9 完整证明和 shading 机制。实际读 LPSW2610.10603v1 Lemma4.5、Proposition5.1、Lemma5.3 statement及证明所需开头；没有把高级全证明全部新独证。

任意固定 \(n\) 的 factoring 已在旧库 GWZ Lemma4.1 给出实际证明；LPSW Lemma4.5 明确引它，且记录更早 Wang–Zahl 来源。ICM 是综述入口。本轮至多核原 PW、measurable shadings及其分母接口，不另立数学 ID。

设 \(\mathbb T\) 有 \(N\) 个等体积单位 \(\delta\)-管，均在固定 \(B_R\)，\(v_\delta\asymp\delta^{n-1}\)，
\[
 I=\sum_T|Y(T)|=\lambda Nv_\delta,\qquad
 E=\bigcup_TY(T),\qquad \lambda\ge\delta^\eta.
\]
首先只讨论原 labels 的 counting law，不暗扩成任意权跨度无费用版。normalized polynomial containment 记为
\[
 \#\mathbb T[W]\le K_N C_D\,N|W|.                         \tag{1}
\]
原方向 \(\delta\)-分离直接授 sharp-PW absolute 系数 \(A_\delta\lesssim C_D\delta^{1-n}\)；写成 (1) 必须取 \(K_N=A_\delta/N\)。只有原 \(N\asymp\delta^{1-n}\) 等量级时才可称归一化系数为常数。restriction 后不能偷换原 \(N\)。

## 2. assigned partition、均匀 child 数与 polylog 范围

GWZ 实际输出为
\[
 \mathbb T'=\bigsqcup_{P\in\mathbb P}\mathcal C_P,\qquad
 T\in\mathcal C_P\Longrightarrow T\subset P.              \tag{2}
\]
这不是断言每个 child 在几何上只被 \(O(1)\) 个 parents 包含；求和使用 assigned partition。

以 \(L\) 汇总固定维数 polylog 因子，\(M=\#\mathbb P\)，父体积 \(\asymp v\)，各 assigned child 数 \(\asymp m\)。则
\[
 mM\asymp_L N',\qquad
 \#\mathcal C_P[U]\le Lm|U|/v\quad(U\subset P\text{ convex}),            \tag{3}
\]
且
\[
 \#\mathbb P[U]\le L|U|/v\quad(U\text{ convex}).             \tag{4}
\]
greedy proof 依次取最大体积密度容器、删除其 children，再 pigeonhole 密度和尺寸。共同密度与同尺寸产生均匀 \(m\)，不能由任意 thickening 替代。

当前原方向分离保证 \(N\lesssim\delta^{1-n}\)，故 Remark4.2 的 \(\log N\) 确为 \(\log(1/\delta)\) 费用。若改为仅给 (1) 的任意 indexed family而无 \(N\) 上界，不能把原文全部 \(\log N\) 无说明地改叫 polylog\((1/\delta)\)。

## 3. 平均阴影先分层，才保原 markedmass

任意 count-refinement 不自动保 markedmass。先删 \(d_T=|Y(T)|/v_\delta<\lambda/2\) 的 labels，损失至多 \(I/2\)。其余有 \(J\lesssim1+\log(1/\lambda)\) 个 dyadic density层，选 \(d\le d_T<2d\) 且 \(I_1\ge I/(2J)\) 的一层，管数 \(N_1\)。再 factoring 保 \(N'\ge N_1/L\)，每个原 \(Y(T)\) 不扩大，故
\[
 I'\ge dN'v_\delta\ge I/(4JL),\qquad E'\subset E.           \tag{5}
\]
逐管及平均 density均有 \(d\ge\lambda/2\)。由 \(I_1\le2dN_1v_\delta\) 得
\[
             N/N'\le 4JLd/\lambda\le4JL/\lambda.           \tag{6}
\]
这就是 normalized upper 改原分母的费用；\(\lambda\ge\delta^\eta\) 使其可作小幂预算，不使其等于常数。

若一开始已有逐管共同 lower，直接在该层 factoring 即可；一般平均版本必须先做以上步骤。进一步删 shading或另选父组时，(5) 要重算，不能继续引用所有旧管的 lower。

## 4. bounded parents 不必另加假设

因每个 assigned child都在 \(B_R\)，对 \(P\cap B_R\) 用 (3)，得
\[
                    |P\cap B_R|\ge v/L.                  \tag{7}
\]
令 \(D_P=\operatorname{diam}P\)，沿直径方向取截面，其最大面积为 \(A\)。凸性把该截面与两端点连接为两锥，积分给 \(|P|\ge AD_P/n\)。用闭包及极限处理不取到最大值的情况；父集含正体积 child，故无零维体积问题。于是
\[
 |P\cap B_R|\le2RA\le2nR|P|/D_P,\qquad D_P\le C_nRL.
\]
又 \(P\cap B_R\ne\varnothing\)，所有 parents 都在 \(B_{C_nRL}\)。由 (4)
\[
                    Mv\le C_{n,R}L^{n+1}.                \tag{8}
\]

实际 GWZ greedy maximizer还可取其 children 的 convex hull而直接在 \(B_R\)；boxes 版只需固定倍球。上述自证说明即便只接 ICM 黑箱，boundedness 也能支付，不免费添加假设。

## 5. polynomial containment 的真实父/子闭包

若半代数 \(W\) 包含 parent \(P\)，则其全部 assigned children 都在 \(W\)，故
\[
 m\#\mathbb P[W]\lesssim_L\#\mathbb T'[W]\le K_N C_DN|W|.
\]
由 (8) 和 \(mM\asymp_LN'\)，
\[
 \#\mathbb P[W]\le L^{O_n(1)}K_N C_D(N/N')M|W|,            \tag{9}
\]
\[
 \#\mathbb P[W]\le L^{O_n(1)}K_N C_D(N/N')|W|/v.          \tag{10}
\]
若原输入是 absolute \(A_\delta|W|\)，原式就是
\(\#\mathbb P[W]\lesssim_L A_\delta|W|/m\)，normalized系数为 \(A_\delta/N'\)，不能少写分母。

固定 \(P\)，John 仿射归一化 \(A_P\) 有 \(|\det A_P|\asymp1/v\)。normalized fixed-format 测试 \(W'\) 的原像体积 \(\asymp v|W'|\)，可逆 affine变换不增加代数格式。于是
\[
 \frac1m\#\{T\in\mathcal C_P:A_PT\subset W'\}
 \le L^{O_n(1)}K_N C_D(N/N')|W'|.                         \tag{11}
\]
这里 \(W\) 不必 convex；convex只用于 factoring、(7)–(8)。若后续测试需要把 \(P\) 放进半代数交集，应取 GWZ boxes输出或固定格式 John外包盒，不能把任意凸体直接算固定格式。

这是实际 containment 应用，关键是 uniform \(m\)、assigned partition、global KT。其计数本质也是旧 GWZ Remark3.3 upward heredity用于 polynomial 测试，不是新 Kakeya 增益。

## 6. partial PW 的共同核旧闭包与变核缺口

若原 fine law另给全部 partial-intersection PW
\[
 \Pr\{|T\cap W|\ge a|T|\}\le C_DK_N|W|a^{-n}\quad(0<a\le1),           \tag{12}
\]
其 restricted-mean形式为
\[
 \int_H |T\cap W|/|T|\,d\nu
 \lesssim_n(K_NC_D|W|)^{1/n}\nu(H)^{1-1/n}.               \tag{13}
\]
固定 parent 的 child restriction及 affine image直接继承，系数同 (11) 的 \(Nv/m\)。这用完整原 PW，不是从 containment 自动推出所有 partial事件。

parent事件 \(|P\cap W|\ge a|P|\) 不表示 assigned child访问同一 \(W\)。固定 \(P=B_4\)，把全方向 centered单位细管置于 \(B(2e_1,1)\)，取 \(W=P\cap\{x_1<0\}\)：child relative convex FW及单个parent KT均只损固定常数；parent与 \(W\) 有固定比例交，而所有 children不访问 \(W\)。这只反“同 \(W\) 直接收 child事件”的证明步骤，不反 parent partial PW 定理。

同时保留一个正面旧闭包：若所有 parents 是同一中心对称 John盒/椭球 \(Q\) 的平移，归一体积测度满足
\[
                    \mu_P\le C_n\mu_T*k_{C_nQ}\quad(T\subset P).     \tag{14}
\]
因为 \(P-T\subset C_nQ\)。平均 assigned \(m\) children后，以同一个核对 (13) 积分，即得父 full partial PW，损失 \(L^{O(1)}N/N'\)。这就是 R43 common-kernel proof 的共同 affine版。

未付的是不同 \(P\) 各用不同方向/长短轴的核后，把 label-dependent平移免费换成全族共同平移。R43 已实证 isotropic、common-clock coarse kernel无 \(R/\delta\) 损失，不能误写成旧失败；它也没有自动支付 arbitrary anisotropic varying-kernel family。此处只列未证明接口，不声其不可能。

## 7. 父阴影和四维输入不能免费提升

自然未加厚父阴影 \(Z(P)=\bigcup_{T\in\mathcal C_P}Y(T)\subset E'\) 的总 incidence \(\asymp dmv_\delta\) 不是它的体积。具体取全方向 \(\delta\)-网 through origin、一个固定球 parent、每管只取中心 \(\lambda\) 长片，\(\delta\ll\lambda\)。原 fine family有常数 convex FW：远离原点的管段重数由角分离控制，故任意 convex \(U\) 中 contained管数乘 \(v_\delta\) 至多 \(C|U|\)。然而
\[
                       |Z(P)|\asymp\lambda^n.
\]
上界是中心球包含；下界因方向网覆盖 \(B_{c\lambda}\)。因此不能令父 density免费等于同一个 \(\lambda\)。它不否定 \(\lambda^n\) 的 subpower lower，更不反原文 induced shading。

GWZ 用的是 \(Y_{\mathbb P}(P)=P\cap N_{w_1}Z(P)\)，会扩大 footprint。Proposition5.1/Lemma5.9 在 \(\mathbb R^3\) 另用 planar Córdoba 给 \(\lambda_{\mathbb P}\gtrapprox C^{-1}\lambda^2\)，并用 multiplicity product管理扩大。Remark5.2 明说高维需合适 \(\mathbb R^{n-1}\) Kakeya估计。LPSW推广输入为 \(v_1\times v_2\times v_3^{\,n-2}\) flakes；ordinary \(n=5\) 的 \(\delta^4\times1\) 管不是这个尺寸类。

不能直接以已存 OAI4 finite DIR替换 \(n=5\) 所需输入。drop最短轴会删一个方向分量：原方向在 \(|v_1|\lesssim w_1\) 带内仍可 \(\delta\)-分离，同一投影 \(\delta\)-帽能含 \(\asymp w_1/\delta\) 个原 labels。厚化到 \(w_1\) 后必须重计真实多重数；factoring没给新管族方向分离。\(w_1\asymp\delta\) 的 flat特殊情况不覆盖一般 \(w_1\gg\delta\)。

relative convex FW只直接传对应投影 CW，而四维 CW-alone 有原文所述 quadric障碍。即便借 full fine PW、同parent共同核及 fixed-format cylinder测试传某种 polynomial上界，无物理方向分离的 PW4仍不能当 OAI4 all-directions/finite DIR；R62已冻结此正幂等价难题。R53–55/R59–60 的区别是 M3 有 arbitrary-CW/full-density 输入，不能免费升成 M4。John各向异性归一化还将横截面短轴变成 \(\delta/s_i(P)\) 的椭球；缺比例及真实 clock时，不是共同参数的 isotropic \(\delta'\)-tubes。

## 8. 阶段 I 判定与停止线

自证的正接口是 (5) 原 measurable markedmass及小 footprint保留、(7)–(8) bounded parents、(9)–(11) polynomial containment，及共同 affine核条件下 R43 的 full partial PW。平均density和逐管lower分别付费；每个归一化保留 \(N/N'\) 或原 absolute系数。没有赠 parent AD lower、projection方向分离、父阴影同density或 arbitrary varying-kernel PW。

完整四路尚未合拢：ordinary初始化不能仅凭 factoring将小 union送给父阴影并调用4D seed；direct HRZ仍需 leaf/parent形状、原density和局部倍率；matrix/mixed完整原jointmass不由此 counting closure生成；真反例仍需同一个全方向集合及严格 Hausdorff upper。本稿没有这些路线的 branchsaving、新维数界或重大结果。

以上 whole-label restriction保留原 \(Y(T)\) 是合法闭包；诱导加厚父阴影是另一对象，必须接新的 multiplicity输入。若再对所有原合法删选统一假设正gain，不能仅以 factoring gain名称解冻旧 CP/PM/PW4。本稿没有提出这种公设。

当前判断：实际 factoring给可用但经典的 containment应用；任意维 generic lemma本身没有付 ordinary \(n=5\) shaded/full-PW/anisotropic leaf的关键输入。不建议包装为 gain phaseII。若继续，须先锁真正有新输入的变核或实际父阴影定理并付原质量及最后用途；否则按spec回完整宏观，不续常数/更多形状或 PW4改名。校准只反明确列出的免费步骤，非完整source/Kakeya反例。

实际交叉记录：已全文逐式读 root9、A8、spec5、终 macro6/next6/source6。A§7把一般 \(m\asymp Nv\) 收紧为 \(m\gtrsim L^{-C}N'v\)，其投影帽上界显式保 \(N/N'\)；macro§2已把平均起点 cardinal保证修为 \(N'\ge\lambda N/\mathrm{polylog}\)，两处均 fresh读回。其余原质量/计数/形状边界无遗留强制项。本稿自身正证由 root/A实际全文独核，不拿自证当独审。另补读 GWZ Proposition5.1 最后 density证明及 Lemma5.11：round coarse-tube形状的诱导 density可直接保 \(\lambda\)，正是 R43 已付特殊闭包，不将 generic缺口扩大成所有形状都失败。正式限定结论见授权 review；未经外部同行评审。
