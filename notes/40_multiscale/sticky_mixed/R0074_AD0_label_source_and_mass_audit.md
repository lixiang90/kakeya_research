# R0074：原 AD0 标签的共同右邻居提取与完整 CW 出口

2026-10-18，A。仅编辑本分配稿，不操作 Git、元数据或新代理。这里独立使用“实际管锚点／共同右邻居”的提取，和 root 的 time-row greedy 分开；后段已实际全文读取 B9 并独立核其 Schur、正交压缩及统一幂稳定。本稿尚须交叉独审，未经外部同行评审。

## 1. 完整输入、实际阅读及本轮不同责任

对象是 WZ2609.22035v1 Def17.2–17.4 的 d5／k4／ell2、κ=1 完整配置，固定原 γ>0，η最后小，δ最后。保原 joint4-AD 管族 T、原 normalized CW 上界 δ^-η、原 Z、两套 grains、ξ／Φ／coherence；不增物理方向分离、smooth、rational、goodrank 或各时刻访问独立。此处沿本轮 spec 及 R43 既有的**原 bounded joint-parameter chart 规范**：全部原 T 的物理 intercept／slope 在固定有界域中。它不是先删成 used T 再改 CW 分母。

具体已读本轮 spec5、R73next6、STATE，以及 R19原source／mass全稿、R20projection／clock全稿、R45后段 fixed-arm／原 alphabet 成本、R64 raw-vs-edge 后段和 R72 common-kernel 全稿。实际重新读取原 Def3.6／3.9、Obs3.4(22)、Def17.1–17.4。原 literal dyadic tube 的 intercept 允许在 R4；若移除上述 bounded source 规范而容许无限远 unused padding，local AD upper 不自动界定原总管数。本稿不声称用 E bounded 即已修复那一不同范围；本次返回原概率时明确保留规范和原分母。

κ=1 使 native scalar label 集 tildeY_t 为 AD0，故每 time 只有 K 个标签；K 统一表示 Cδ^-Cη 的固定次幂，常数依固定维数／规范，不依 δ。旧 R45 的正维 alphabet 无此代价。R19–20 的固定 tuple、R64 的 raw edge、R72 的更多固定终时不提供下面的实际管族提取。本轮需付从原 incidence 到共同参数 carrier，再到 whole-tube 凸 CW 的全部责任；不以有限 rank 引理结案，不注册新 ID／major／ordinary 界。

## 2. 原坐标、单次真实 visit 和原分母

将原 tube 的物理参数写为 λ(T)=(A,B)∈R4×R4，轴为 (A+tB,t)。native split 是三个 horizontal 坐标及一个 normal 坐标；令 n(t)=(-tildef(t),1)，其中 tildef=(c,d) 为原 bounded 三维 row。于是

    V(t)=(n(t),t n(t))， F_t(λ)=V(t)λ。                 (1)

V bounded，且含一个恒为 1 的坐标。原实际 marked point p@t、其 native 原标签 y∈tildeY_t 给 F_t(λ(T))=y+O(δ)。误差是原 fine tube／point／dyadic label 的固定常倍 δ；无需 Lip 的导数，也没有 coarse ρ³ 误差。不同 time 的 y 值可以完全不同。

native filled 三水平与 AD0 给 #E_t≈_K δ^-3；原 scalar Φ_p 的 AD1 方向供应给每点约_K δ^-1 个不同原 tube labels。因此原 incidence I≈_K mδ^-4，m=#Z≥δ^{η-1}。反向 upper 由细点 δ-separation、原方向 δ-bins 及有界参数查询支付。一个 T 在一个固定 t 只有 O(1) 个所选实际点／角标签可发生碰撞，均可用有限着色或 canonical 选择除去，损固定常数。

在原 bounded chart 下 joint4-AD upper 给 N_orig=#T≤Kδ^-4，AD lower 给 N_orig≥K^-1δ^-4（等同原 Obs3.4(22)的规范用法）。所有后文 probability 一直除 N_orig。used T 的 bound 也成立，但绝不以它代替原 CW 分母。

## 3. Tube-heavy 与同 time、同原 label 二部图

以 I/(4#used T) 为访问阈值删轻管，至少保原 I 的固定比例。每条余管保它**全部原 visits**，形成 H0，N=#H0≈_K δ^-4，且 N≥K^-C N_orig；每条 T∈H0 至少有 h m 个原访问，h≥K^-C。

每个余 T／time 取一个实际 canonical visit。右顶点为

    R={(t,y):t∈Z， y∈tildeY_t}， #R≤K m。

左顶点是 H0 原 tube labels，边 T~(t,y) 表示选中的真实点属于该**原 time 的该原 grain label**。每左顶点／time 至多一边；总边数 I0≥hNm。若若干管共享同一个右顶点，由(1)其参数差满足 |V(t)(λ_i-λ_j)|≤Cδ。

此构造不把 pruned point-Φ 族说成新完整配置，不要求其 AD lower。图只是 finite witness，原 upper、原 CW 与原全部 tube parameters 仍在原 T 上查询。原平均 incidence、逐 H0 管访问 lower 已分别支付；若原输入另有逐管 shading 下界，整 label 留存保它，后来只取共同右边不能无证保同一逐管密度。

## 4. 独立 common-right 锚管算法与真实管子族返回

固定小 a>0，θ=δ^a。先选一个实际锚管 T0。对右度 deg(z)，

    Σ_(T0∈H0) Σ_(T∈H0) # [N(T)∩N(T0)]
      =Σ_(z∈R)deg(z)² ≥ I0²/(Km)。

故可选 T0 使 R0=N(T0) 上的全部左边数 I_0'≥(h²/K)Nm。记其 density p0≥h²/K。此后维持实际锚管 T0,...,Tr、其 affine span S_r=λ0+W_r（dim r）、共同右集 R_r=∩_(i≤r)N(T_i)，以及

    I_r=Σ_(T∈H0) # [N(T)∩R_r]=p_r Nm。              (2)

每新锚管距旧 S_r 大于 θ，故 affine 独立。所有原 T 的 visits 不重定义；只是在计数中取其共同右边。R_r⊂N(T0)，实际上每 time 至多一原 label，特别 #R_r≤Km。

若距 S_r≤θ 的左顶点承担至少 I_r/2 边，停止。令 H 为这些实际原管，则

    #H≥I_r/(2m)≥(p_r/2)N， dist(λ(T),S_r)≤θ (T∈H)。 (3)

这就是返回的真实 original tube subfamily，非只一个好 anchor tuple。由 I_r≤N#R_r，共同右 time 集 G_r 的 cardinal≥p_r m；即使未用“一 time 一 label”强化，除一次 K 也只有次幂代价。

否则 outside 左边 I_out≥I_r/2。对候选 outside 锚管 a，令 I_next(a) 为再交 N(a) 后的全部左边数。精确地

    Σ_(a outside)I_next(a)
      =Σ_(z∈R_r)deg_out(z)deg_all(z)
      ≥Σ deg_out(z)²≥I_r²/(4#R_r)。

除候选数≤N，选到一条实际 outside 锚管使

    p_(r+1)≥p_r²/(4K)。                              (4)

这里用的是 deg_out deg_all≥deg_out²，未把 outside 边与所有边误写恒等，也未假 tube visits 独立。至多八步，故所有 p_r≥K^-C，C虽然可大但固定；源 η最后小足以支付有限次 squaring。

## 5. 不能早停于 r<4，也不能到 r=8

对任意 bounded affine r-plane S、r≤3，用 O(θ^-r) 个 θ-balls 覆盖其与固定原参数 box 的交。joint4-AD upper（off-support ball 可移到相交原点并扩大固定倍）给

    # {T∈T:dist(λ(T),S)≤θ}≤C K θ^(4-r)δ^-4。       (5)

每管每 time 至多一边，故若 r<4，(5)承担的边≤K^Cθ^(4-r)Nm。因 p_r≥K^-C、η≪a，此值小于 I_r/2，不能满足停止条件。没有给高维 S 新 AD lower。

再设 r 个参数差为 B_r=[λ1-λ0,...,λr-λ0]。每个 sequential pivot>θ，全部 columns bounded，故其 r-volume≥θ^r、least nonzero singular value≥cθ^r。对每个共同右顶点，(1)给 |V(t)B_r|≤Cδ。因此若 Q_r 是 W_r 的原 Euclidean orthonormal basis，

    |V(t)Q_r|≤Cδ θ^-r。                              (6)

r=8 时 Q_r 张成 R8，故 |V(t)|≤Cδθ^-8，与恒 1 坐标矛盾。只须先固定 8a<1，再 δ小。算法(4)保证若真进行到该步 I_r>0，故不能用共同右集空来逃避矛盾。最终必在 4≤r≤7 停止，(3)给原概率 p=#H/N_orig≥K^-C、whole 参数误差 θ、共同原 time 数≥K^-C m。

## 6. 同 label 的多时约束给同一 evaluation pencil

在停止 affine S 上取原正交基 Q=[A;B]，A/B 为4×r，QᵀQ=I。reference λ0 是实际锚管，因此 bounded；距 S≤θ 的原参数可写 λ=λ0+Qz+O(θ)，|z|≤C。

对共同 time t∈G_r，式(6)成为

    |n(t)(A+tB)|≤Cδθ^-8， |n(t)|≥1。                (7)

故 4×r 的 A+tB 最小 row-singular value≤Cδθ^-8，而其余 singular values fixed bounded；**全部** 4×4 minors 在这些同一 time 上≤Cδθ^-8。这里 n(t)本身任意变化，无需它 affine；多项式对象仅是物理 evaluation pencil。

G_r 中至少 K^-C m≥K^-Cδ^-1 个实际 δ-separated times，位于[-1,1]。由 δ-packing 可贪心选5个，两两 gap≥K^-C（先 source η小，使 gap≫δ）。每个 minor 是次数≤4 的 t-polynomial。Lagrange 的四个 gap 分母给所有系数的统一 bound

    D(A,B):=max_(all 4-minors,all t-coefficients)|coefficient|
          ≤K^C δ θ^-8。                              (8)

这包含共同 time mass、原 δ-clock floor 和插值条件数。没有在新 allowed time grid 上重构完整配置，故无 allowed-grid 闭包缺口；也不把单个好时刻的 rank 亏当全 polynomial rank 亏。

## 7. 全 r singular pencil 的精确正交 compression

本节与 B9 已 actual 全文互读，以下是独立复核。若所有 4-minor 恒零，r0=max_t rank(A+tB)≤3。取实际 t0 达最大秩，把 A换 A+t0B；仅为精确存在证明作固定可逆 row／column 变换，令

    A=[I_r0 0;0 0]， B=[C D;F G]。

在0邻域 Schur complement 为 tG-t²F(I+tC)^-1D≡0，故 G=0、FC^jD=0 全部 j≥0。置 U=span{imD,...,im C^(r0-1)D}，e=dimU。Cayley–Hamilton给 CU⊂U、FU=0，因而

    K0=U×R^(r-r0)， E0=U×{0}， AK0+BK0⊂E0。

返回原 Euclidean 子空间后，取 K⊂K0 维 r-3+e、E=E0 维 e≤3；可行因 r0≤3。于是 AK+BK⊂E。r0=0平凡。全部 regular／left／right blocks 同时包括，不以一个 minimal block 代全部参数。

**关键**：GL 只证明子空间存在，几何一律用还原后的原 orthogonal projectors。完全不用可能随 δ 爆炸的 canonical-basis condition number。joint[A;B]单射另给 r≤2r0≤6；因此 r=7 的 exact singular 不存在，但无需预设其 gap，下面统一近似论证同样适用。

## 8. 统一幂稳定不是 pointwise compactness 口号

在固定 bounded A/B 域定义

    Ψ(A,B)²=min_(e,K,E)
       ||(I-P_E)A P_K||_F²+||(I-P_E)B P_K||_F²，     (9)

其中 dimK=r-3+e、dimE=e，e=0,...,3，P 为原 orthogonal projectors。约束 P=Pᵀ=P²、trP=dim 是固定多项式，Grassmann compact；Ψ连续且固定半代数。第7节证明 D=0⇒Ψ=0。

令 H(s)=max{Ψ²:bounded A/B,D≤s}，域 compact 且含零 pair，max 存在。若 H(s)不趋0，取收敛子列即违 D=0⇒Ψ=0。基础具名输入 real quantifier elimination 给 H 的图为固定半代数集。其图无二维内部，故有限 sign decomposition 中每一点有非零 polynomial 取零，有限乘积 P(s,H(s))=0。除去公共 s 幂后 P(0,y)非零。若 H 在0附近非恒零，P(0,0)=0，设最低非零 y 次 j≥1；小 y 时 |P(0,y)|≥c y^j，而 |P(s,y)-P(0,y)|≤Cs。故 H(s)≤Cs^(1/j)，即

    Ψ(A,B)≤C D(A,B)^c， c>0 fixed。                  (10)

若 H 恒零则更易。这里实际证明了所需一元 power growth，没有用未量化的 compactness 代幂指数。QE 本身为与 R31 同样的标准具名基础；不宣新证其全部理论。变量数／格式固定 r≤7，故 C/c 不依 δ、各时刻 tildef 的复杂度或最小非零 minor。

## 9. 返回原 T、whole axes 与真实 convex box

由(8)(10)取 e≤3、K⊂R^r 维 r-3+e、E⊂R4维e，A/B 的 K方向对 E⊥泄漏≤C D^c。选 thickness h_* 满足

    h_*≥C(δ+θ+D^c)， h_*≤c。                         (11)

对 bounded P_(K⊥)z 用 h_*-grid，补维数正好3-e，只有 O(h_*^-(3-e)) 格；某格保原 T 概率至少 c p h_*^(3-e)。以其 reference 轴剪切平移后，这些原轴全 clock [-1,1] 的 K部分在 E 内、偏离 E 的量≤Ch_*，补坐标变化亦≤Ch_*。θ 参数误差和原 δ-radius／roundcaps由(11)支付。

因此存在一个真实 physical R5 convex box，e个空间长方向和 clock 长方向 O(1)，其余4-e个方向 Ch_*，体积≤C h_*^(4-e)，包含所选**整条原管**。有界 reference slope 的 shear determinant1、norm fixed bounded，不改变这些成本。用原 normalized CW 分母得到

    C_CW(T)≥c [p h_*^(3-e)]/[h_*^(4-e)]=c p/h_*。   (12)

没有用短 time shading 补成长管，也没有对 fat／延长 tube 免费继承 PW。实际用到的是整参数靠 S，足以包住原轴全部 clock；模型要的是 CW whole containment，故原 marks再怎么集中也不影响(12)。

## 10. 参数顺序、最终 source 矛盾和平均／逐管闭包

先固定足小 a，例如 a<1/100，使 conditioning 的8a小于1/4。式(8)在源 η足小后给 D≤δ^b，b可取某个 fixed 正数。再固定 0<s<min(a,bc,1)/4，置 h_*=Cδ^s。θ≤h_*、D^c≤h_*、δ≤h_*，故(11)成立。所有有限 squaring／AD／插值损失均只有 p≥δ^Cη。最后使 η≪s/C，式(12)≥cδ^(Cη-s)>δ^-η，违完整原 CW 上界。

η最后小是有限深度算法和 fixed QE exponent 之后选取，不循环；δ最后吸固定常数。无需原 γ的新阈值，此 κ1 argument 对每个 fixed 原 γ>0成立，实际上到图提取后不再调用 native tube-KT。它使用 κ1 所特有 AD0 标签及 filled native 三维；不是借 R73 mixed32 的 γ／κ 范围。

图删选只作 finite witnesses。平均 I 明确保常数／K幂，每 active H0 管原访问 lower 明确保 h m；共同右边不被声称有各 tube 原逐管密度，也不被当新 Def17 配置。最终 H保的是实际原管概率，且其 whole original tubes 用于 CW；无须对子族重新授 AD lower、point-Φ lower 或 dense shading。若输入另是完整原逐管 shading，整 label 留存本身保它；另缩共同右访问时必须重新核。本证已绕开该额外需要。

## 11. 独立反攻与旧冻结逐项排除

一 time AD0 不送多个 time 标签同值，本稿右顶点为(t,y)而非 y；common-right CS实际付每一有限次质量。一个好 anchor tuple不送原 H，本稿在停止式(3)返回 H，低维 early stop由原 ADupper禁止。更多 fixed times自身也不够，本稿多时只在实际 common-right 上插值同一个 pencil。

高维参数 carrier不等于物理低维 plane；本稿保全 r=4..7，经 Schur可达子空间和 orthogonal K/E 再给凸 box。常值 tildef、parallel／common-ridge、直纹退化分别都归 exact compression；有 joint kernel 的重复参数若冒原 δ-separated labels则须先纠正，不能反本证。近 singular 不是 exact，而由(9)(10)付统一 power，最后 h_*非免费 δ。

若放掉 whole 参数 closeness，仅若干短片靠 plane，则(12)不可用；本提取确给 λ距离。若原 #T分母无 bounded规范或另有独立dense-original-shading控制，本证明不会自动返回原 p；本轮已明确保 bounded 规范而不消掉此范围。若 carrier 格式／变量数随δ增长，固定QE指数不能照搬；本轮 r≤8是源固定维数。R45 fixed-arm costs、R64 edge-only rank、R72 basicness等停止线均未重命名复活。

## 12. 已完成内容、依赖与供互审接口

已给出独立完整 source-to-CW 链：原 tube-heavy；同 time／同原 AD0 label 图；finite common-right tube-anchor CS；真实原 H 返回且 r≥4；conditioned fineδ法向约束；原time五点插值；全 r pencil compression及统一幂稳定；保原 T 分母的 whole-tube p/h_* CW矛盾。按本轮 bounded source 规范，这排完整 d5/k4/ell2、κ1配置，不只容易的有限秩部分。

具名输入为 WZ原 Def3／17 的源结构及其实际 bounded normalization、标准 real quantifier elimination；没有本轮重新独证全 WZ论文、全部高级外部输入或 ordinary初始化。B9的精确压缩／QE power／box已 actual全文独核，A上游提取须由 root/B独立逐式审查；不能把自己证明当自己的独审。尚未宣 outer formal-reviewed 状态。

本结论不推出 sticky K5(inf)≤1，不从普通4D Hausdorff下界反推该极值类范围，不解决其它 κ或 general→sticky、ordinary n5严格超过4／n6界。无新数学 ID、优先权／major 或独立新高维增益声明。未经外部同行评审。

## 13. 根稿互审的实际终点

本稿完成后已实际全文读取 root `R0074_AD0_native_labels_to_CW_exclusion.md`12节及 B终稿10节（前9节已先实际读，新增第10节现补读）。以下独核不是把A自己的上游证明当独审。

root的row-greedy首先令每条 H0 管有原 m时间分母下 K^-C m visits。以后每次只删 whole tube labels，故所有 Hj仍有此逐管原下界。若 outside-row times占至少半原访问，time平均再付该time至多K labels即可选真实 Hj+1；否则 W在**原 Uniform(Z)**下质量≥K^-C。j行 sequential pivots>τ给 row smin≥cτ^j，故真实 Hj距同一个8-j维 affine solution plane≤Cδτ^-j；reference可由一条实际管正交投影，仍 bounded。第5行会使足原管概率困于3plane厚 Cδτ^-5，AD4 upper与 η后小确排；j≤4停止后不是仅有一个tuple。

对原正交 Q，V_t距rowspan≤τ直接给 n_t(A+tB)≤τ，因此全4minors≤Cτ；原 W质量与 clock interval upper可选5个分隔原times，故系数≤K^Cτ。该误差和参数距S的 Cδτ^-4均在root最终 h=δ^s预算内。B第2–7节的exact Schur／原orthogonal子空间／QE power／whole管box逐式通过；最坏补维3-e与短轴4-e确给一幂，而非在m>4漏费。root/B原N范围均已显式保bounded全原T，不以used族归一。

root第10节的固定n=d-1同型推广也核过：n+1独立rows将n-AD管law困于(n-1)plane；停止时参数维≥n，n-minors次数≤n，n+1原times插值；compression补维n-1-e、物理短轴n-e仍差一幂。用于 k=d-1、κ1 native AD0时每time filled n-1水平加原Φ AD1供应确给δ^-n真实不同管。只对每个固定n及同一bounded源规范成立，不能读作dimension-uniform、κ<1或ordinary初始化。此推广是同有限关联证明的已查读出，不另开研究或ID。

截至这次实际互审，root12及B10没有未解决的强制数学修订项。A13上游独立提取仍须root/B审查；最终macro／next及正式review未授权前，不预认证未来范围／元数据／Git。当前结论为在明确bounded完整源规范下的κ1 source应用通过本次内部逐步核查，未经外部同行评审，无ordinary或major声明。
