# R0101：原 native 图的 witness、完整 box 和真实质量费用

2026-10-19，B／lifting_obstructions。先实际读 reselection5和原来源，再全文读另锁 working5后施工。以下保留半代数正用途，同时独立核 witness 边际与原质量；不是完整 source 反例、κ1排除或高维新界。未经外部同行评审。

## 1. 实际恢复、原命题和读域

已实际读 GOAL、当前 STATE、完整 ROADMAP（分段读）、registry全部78项 ID／status、R100 next6和 R101 reselection／working各5节。root 已运行一次 context，本人不重复运行。完整普通初始化／HRZ全预算、sticky全 rough及普通桥、同集全方向严格低维构造四路仍保留。此次只核固定格式超图能否给实际 R76 图一个保原质量的大完整几何乘积，不预授 selected support 可定义或共同 X。

实际全文读 R76 root12，另读 R44 root8／B8及R45 root10／B9原文件；原 WZ Def17.1–17.4、20.3(164)–(165)、21.1(172)–(173)、21.2及其应用段读回。新 primary 实际读本地 FPS1502.01730v3半代数定义／Th1.1／1.3，Rubin2407.15518v2定义／Th1.3／1.6及§5.2 Th5.1和完整该节 proof sketch。未独证其余高级 wholeproof，未下载或修改来源。只编辑本分配稿，不操作元数据／Git／新代理。

## 2. 实际 sameT 图及原分母

采用 R76 明列的 bounded matrix33、κ=1、det-large 分支。固定原锚 t,s，A=F_t−F_s、h=s−t均有 R76 的 σ条件；令 n_1=|Y_t|、n_2=|Y_s|、m=|Z|，有 K^{-1}δ^{-1}≤n_i≤Kδ^{-1}。其共同 fine residual bucket 内 H*保每根原 T 的全部原 S_T，且同 fine native endpoint pair 的 T 重数≤M_0=O(1)。记

\[
g(y,y',u)=M_0^{-1}\#\{T\in H^*: (y_T,y'_T)=(y,y'),\ u\in S_T\},\quad
0\le g\le1,\quad \sum g=\theta n_1n_2m,
\tag{1}
\]

其中 θ≥L^{-1}，各 T 的 |S_T|≥K^{-C}m，m≥K^{-1}δ^{-1}。L包含锚距、逆矩阵和八维 residual 桶的真实费用，不与 K混称。单个 H* 相对全部原 N≈_Kδ^{-4}只有 L^{±1}δ²级质量；本轮不将它当新的完整 Def17配置或保归一 CW常数。

原同管访问给 B_u+C(u)y+D(u)y'∈N_{Cδ}Y_u，其中 λ=(u−t)/(s−t)，

\[
C(u)=(1-\lambda)(F_u-F_s)A^{-1},\qquad
D(u)=\lambda(F_t-F_u)A^{-1}.
\tag{2}
\]

这些是同一个原图的实际系数，不要求 F_u可微或 g独立。源 upper／相关 priors 本来允许选边，不能仅因关联拒定理；真正需要核的是精确几何关系和原产品分母。

## 3. 任意 mask 的真实正面用途

设有限域 P_1,P_2,P_3的几何关系 R有固定格式，0≤f≤1支撑于 R，V=|P_1||P_2||P_3|、Σf=ϑV。Rubin Th5.1在各侧至多 P≤Cε^{-(d+ζ)}个部分上，使所有非齐次部分乘积的总 cardinal volume≤εV。空齐次 box 上 f=0，因此完整 edge boxes合计保留

\[
\sum_{\text{complete boxes }Q} f(Q)\ge(\vartheta-\varepsilon)V.
\tag{3}
\]

这是原 f质量而非仅新几何 edges；不要求 f本身半代数。ε=ϑ/2时至少一完整几何 box 满足 f(Q)≥cϑ^{1+3(d+ζ)}V，原 f质量比例≥cϑ^{3(d+ζ)}。又因 f≤1，每侧相对大小至少 f(Q)/V。源 parts不必等大，(3)只用总非齐次乘积体积，不能误用“不规则 box 的个数比例”。

此正用途确修补“selected mask不半代数所以一律不能用”的过强说法。它只补全 R，不补全 f。FPS Th1.1也给固定(d,t,D)下 density 的正幂完整几何子族；其 block-degree量词与 Rubin的 total-degree量词需分别保留，高级常数按源具名。一般 vertex概率权重若无产品密度上界，不在此无权 cardinal 证明中免费覆盖；当前 R76实际产品域无此问题，f的分数权已完全允许。

## 4. 合法增广编码与 witness 密度

取第三域

\[
P_3=\{z=(u,C(u),D(u),B_u,w):u\in Z,\ w\in Y_u\}.
\]

其13个坐标可另加 tag区分三part，统一放入 R^{14}。关系 R由 |B+Cy+Dy'−w|_∞≤Cδ的四个不等式决定，total degree2、每个 vertex block degree1，格式固定。任意 rough F及任意离散 Y只是顶点集合，不进入公式复杂度；没有附加 smooth／bounded-degree F假设。

每个原 T,u选定一个原 native witness w_T(u)∈Y_u；多个可选时先确定选择，不在不同用途换 witness。令 f(y,y',z)为分配到该 w的实际 T权除 M_0，则 f支持 R且

\[
\sum_{w\in Y_u}f(y,y',u,w)=g(y,y',u)\le1.
\tag{4}
\]

原 q_u=|Y_u|∈[K^{-1}δ^{-1},Kδ^{-1}]，故新第三域大小 Q=Σ_uq_u∈[K^{-1}mδ^{-1},Kmδ^{-1}]。同一原总质量没有多算，但其新 density ϑ=Σf/(n_1n_2Q)满足

\[
K^{-1}\theta\delta\le\vartheta\le K\theta\delta.
\tag{5}
\]

不能仍以 θ调用 density结论。反之也不能由(5)断言丢了 δ比例的原质量：只是产品参考分母改变，Σf=Σg严格相同。应用(3)时，ϑ≈_Kθδ带来 polynomial δ费用；它与 fixed-format 定理完全相容，不是对源的反例。

## 5. 两个精确的免费桥反攻

第一，complete geometric relation 不使其任意 dense selected mask也有大 complete selected box。取 n×n独立 Bernoulli(1/2)矩阵 M，置 f(i,j,u)=M_{ij}并保全部 clocks。Chernoff使密度和每个 row／column degree均≥n/3的概率趋1；存在 s×s全1矩形的概率至多 n^{2s}2^{-s²}。取 s=⌈4log_2n⌉后该 upper趋0。因此存在正密度、每条选中 pair保全部 clock的 mask，但任意非空 selected complete box至少一侧大小<s。底层 R可取恒真、格式0。它只否 selected 补全，不否(3)的 geometric补全和原 f质量结论；该有限图未实现 full T AD4／CW／filled X／Φ，非 source反例。

第二，消去 arbitrary Y witness不免费保固定格式。固定其他变量使 nearoutput等于一维 x；取2q个递增等距测试点，Y只含其中偶数点，半径小于间隔的1/4。消去 w后的 membership在这些点交替真假至少2q−1次。任意由 s个 degree≤D一元多项式及 Boolean组合给出的关系，去掉恒零多项式后在至多 sD个实根之间真值恒定；测试点若恰在根上，一个根可以触发两次相邻变化，故安全必要条件为 sD≥(2q−1)/2。连续版本是 q个分离小 intervals，也须随q增长的根数。该例不是说任意原 Y均难定义，而是 fixed QE只适用于原 membership已有固定格式；不能把 q个任意离散点当免费固定格式输入消去。此有限点根计数的初稿因忽略根上测试点多算一倍，actual互读root§9时已修，不影响格式不统一的结论。

## 6. 远 clock 删选和单 box 的第三边际

取 r=δ^c、0<c<1，删 |u−t|<r或|u−s|<r的原 visits。Z是 δ-separated，每根 T至多删 C(r/δ+1)个 time。由§2，删掉比例≤CK^C(r+δ)，η先小于 c的固定倍、δ足小则各 T均保至少原 |S_T|/2。令 g_f、f_f为这同一原删选，M_f=Σf_f≥θn_1n_2m/2，且仍有Σ_w f_f=g_f≤1。这个步骤真是逐 T支付，故也保平均；不是以全局平均代逐管 lower。

对 R任意非空 complete box Q_1×Q_2×Q_3，固定 y_0∈Q_1、y'_0∈Q_2。每个固定 u的所有第三顶点 w都在同一个 Cδ-ball内，由原 Y_u δ-separated至多 C个。因此

\[
|Q_3|\le Cm,\qquad |Q_3|/|P_3|\le CK\delta.
\tag{6}
\]

这是完整几何 witness box的第三 PRIOR 上界，尚不是它承载 f_f的质量上界；原任意图的质量可集中在很小 prior部分。为区分二者，下一节使用原端点 Tube-KT真正估计质量，不从(6)偷推。

## 7. 原 Tube-KT 对完整 witness box 的实际质量限制

设该 complete box承载正 f_f质量，选其中一个 far顶点 (u_0,C,D,B,w)。λ和1−λ均非零，(2)精确给

\[
\frac{C}{1-\lambda}+\frac{D}{\lambda}=I_2.
\tag{7}
\]

因为 |u_0−t|、|u_0−s|≥r且 |s−t|≤2，min(|λ|,|1−λ|)≥r/2，故 max(||C||,||D||)≥r/4。若 ||C||≥r/4，固定任一 y'_0∈Q_2，完整性使所有 y∈Q_1满足 Cy位于同一个 Cδ-ball。取 C最大奇异值对应的单位左向量，得到 Q_1包含于宽 Cδ/r、长 O(1)的 strip。另一情形同理约束 Q_2。这用的是 operator norm最大奇异值，不假另一奇异值非零，不授 goodrank。

令 a=C_1δ/r。δ≤a≤1时，原 Def17.3–17.4的 Y⊂R² Tube-KT exponent为1−γ，在宽a、长O(1) strip上给 a-cover数≤CKa^{-(1−γ)}；每个 a-ball的原 AD1 upper≤CK(a/δ)。原 |Y|≥K^{-1}δ^{-1}，所以

\[
\frac{|Y\cap\mathrm{strip}|}{|Y|}\le CK^3a^\gamma.
\tag{8}
\]

长O(1)用固定个单位 tubes，若 a>1用 trivial1。此处 a≥δ，未将 Tube-KT用到未定义的 sub-δ尺度；κ=1原 native AD1和 exponent1−γ均为实际源输入，不用 rescaled裁切集的新 ADlower。

结合Σ_w f_f≤1而非仅 f_f≤1，任意该 box满足

\[
\begin{split}
f_f(Q)&\le |Q_1||Q_2|m
 \le CK^3(\delta/r)^\gamma n_1n_2m,\\
\frac{f_f(Q)}{M_f}&\le CK^3\theta^{-1}(\delta/r)^\gamma.
\end{split}
\tag{9}
\]

若一族 B个完整 witness boxes覆盖至少 qM_f质量，哪怕 boxes相互重叠，求和上界给

\[
B\ge c q\theta K^{-3}(r/\delta)^\gamma.
\tag{10}
\]

选择 R76有限损失 L≤δ^{-β}、K≤δ^{-C_0η}，再使 β+3C_0η<γ(1−c)/2及η≪c，则(9)有固定正幂质量费用，(10)要求 polynomial数量而非 subpower数量的 boxes。Rubin在ϑ≈_Kθδ的输入下本来也只保 polynomial δ成本，故没有矛盾。这里是在完整源若存在时推出的上界，不是构造了完整源反例，也不能仅由此宣其为空或 κ1已排除。

## 8. 原权重、平均和逐管闭包

Rubin正引理允许 f的任意[0,1]权。当前 f是实际原 tube incidence除固定 M_0；若给各原 T额外 subordinate权0≤ω_T≤1，仍有(4)及相同的 upper，但总质量和 θ必须按这些原权重重算。没有将无限权跨度或任意 vertex概率无费纳入原无权 theorem。

whole-index restriction H'⊂H*保各自全部旧 S_T及原的逐管 lower；原 CW的绝对计数 upper也继承，但若改成新 probability，常数要乘 N/|H'|。端点／第三 witness box restriction仅保选中的 visits，不自动保每根 T的旧 clock密度。若其实际 incidence总数为 I'、候选原 tube数 N'，以 I'/(2N')截 heavy保≥I'/2，heavy各管至少该阈值、heavy数≥I'/(2m)。这是真平均→逐管转换，必须同时保新 N'和 I'分母；不是仍宣旧 λ、旧全 T比例或全部原 ADlower。

几何 supgraph替换只保 upper合法性，不把新 edges当原同T lower。保原 f的(3)正是可用修复，但不能反向补回 source全部数据。尤其去掉 w只允许输出落Y_u且 w随端点对改变，与固定第三顶点 w下的完整 box不同；(9)没有排除这种 variable-output图或全部几何编码策略。

## 9. R44／R45排重与双向责任

R44对每个共同半代数测试逐项应用 PW时已保原 index权和 A_tot访问重数；natural／fine affine包络精确回 CW。把每条管另选一个 witness测试而不计域／重数，并未避开那个账本。本轮新引理可对已经合法的几何 relation补 box，却没有压缩原 joint endpoint／normal palette或减少原N/I费用，故不能按新工具名解冻 R44 degree／piece参数。

R45的 Zorin-Kranich Th1.5本就允许任意选中 tuple hypergraph，不需 Cartesian全族、也不要求虚拟 planes有filled shading。原time／angle分离和near-plane incidence已付；实际 good-BL质量与 endpoint字母表门仍未付。因此若这里只为套旧 KBL upper取得 complete box，新的 Cartesian化并非必要输入；也不能因为有几何 box就赠 transverse rank或更强指数。

本轮未证明“有 geometric box”等价于原 full gain；反向从任意 bounded-format几何 relation及 mask重建全 T／CW／filled X／Φ／selected ξ同样未付，不能将本稿 toy或(9)上界改成 fullsource反例。旧全称 positive估计在所有合法restriction下再调用的输出仍须先核双向正幂排重；本轮没有新的无条件 positive gain可登记。新做的是保原 mask的合法几何分解，以及对实际 witness编码的严格费用，而非旧失败指纹的简单复述。

## 10. 当前结论、独审和停止

已正面付出固定格式 supgraph对 arbitrary supported mask的真实质量保留；rough coefficients可放入第三域；原 sameT witness分配与产品密度δ费用；远 clock逐管删选；原 AD1＋Tube-KT经(7)给单完整 witness box真实质量上界及覆盖数 lower。两个反攻只否 selected免费补全和 arbitrary membership免费消元，均不冒完整源或 Kakeya反例。

目标中的各边际／原质量仅损 subpower的大完整 witness乘积未从这两 primary取得，实际原 Tube-KT反而要求固定幂端点与单box费用。停止直接 witness-box的d／D／ζ／θ参数续轮，不将 selected bounded-format／大 complete box／common X增列成功假设。保留任意 mask的正引理和 variable-output等未被排除范围，无新ID／major／ordinary增益。

现已 actual全文独读 root主12、A10及两spec各5，读回A§8/10新增far／strip原mass链；终macro／next／source／round各6也实际全文读。root／A的原mask保量、fixed-format编码、weighted clone的额外维数、逐管远clock、真实单box质量／cover数、prior与mass区别和旧R44–45接口均逐式核过，未见未解mandatory。本人§5 sampled交替的根计数漏1/2已实际修正并记录；自己正证不算自独审。正式有限范围审查另存获授权review6，不预认证高级wholeproof、元数据或同步；本稿停止扩数学。
