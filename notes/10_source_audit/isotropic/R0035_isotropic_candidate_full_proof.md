# R0035：原 Theorem 6.1 完整 isotropic 候选引擎

2026-10-17。ISO-001 主证明。修后完整稿已通过A/B两次实际全文独审；见research/reviews/R0035_scalar_and_state_review.md及R0035_geometry_and_prior_review.md。原文为 literature/primary/openai_2026_four_dimensional_kakeya.pdf，第70–108页，文本3735–5799；原§6 TeX同时存档。这里只重证已有来源中的分支及其实际调用的§5输入，不提出新的 Kakeya 定理。外部高级输入在§2具名保留；未经外部同行评审。

## 1. 命题、范围及量词

固定原4.7的 prepared tangent data、角参数 S,η、0<k≤1、0≤d<1，版本1/j=1，或版本2/j=2且优化窄度ℓ=0。设 N→∞，K=N^{o(1)}；所有 fixed positive powers、固定次数/维数先于慢对角选择，K可增大但不是原尺度可编码 slack。所有 priors、packet assignments、path layers和已认证帽/短列表按原定义。给定任意子列及其中任意 substantial residual incidence family，本轮证明可再取子列，得到固定正且有界深度 s、packet Q、a=N^{-s}、h∼a^k，以及

    a₂=a h^{e₂},  e₂>0 fixed,
    counted incidence mass ≥ h ν_Q (a₂/a)^d / K.

测试在原版本中 proper 且总次数≤2；版本1形如 w−F(z)。在同一 h-block 上值≤Ka₂、隐藏一阶导数上界K，计数点一阶导数下界K^{-1}，隐藏二阶导数≤K/a₂。这里 ν_Q 是完整原 assigned prior，不是当前被选轨迹的质量。除以时间h正是原4.10候选质量；gain=e₂ks是正有限数。于是AIM-001适用，排除这一完整 isotropic 分支，并由CRP给原Cor6.9：版本1任意固定可容角参数、d<1时 H(E)=0。

这不证明版本2的正有限窄度/无限窄度分支、完整原2.17与finite读出、所有外部输入的证明，或n≥5/一般Kakeya。源定理认证不算新颖/重大结果。原R1–R3高维 moment-curve、同q核及SCL幅度问题保持冻结，它们不是原三维基底 conic 步骤的反例。

## 2. 真实输入与 restriction 闭包

已独审TCM/ASM/TEX/CRP/AIM及其明确的标准测度/固定格式实代数基础。在本轮还需以下具名高级输入，核其原始定理与使用范围，不宣称重证整个外部论文。

1. Wang–Zahl, *Sticky Kakeya sets and the sticky Kakeya conjecture*, arXiv2210.09581v2，Def4.2、Thm5.2及§8证明。Def4.2的AD条件是每球每中间尺度的 covering **上界**，没有下界。F,G为平面(δ,1,δ^{-η}) upper-AD sets。Thm5.2或者给正交直线上的各δ^{ε−1}个δ格，或者对**每个**覆盖数≥δ^{η−3}的 restricted triple set H⊂F×G×G，点积 a·(b₁−b₂) 在某区间I/尺度ρ有指数1−ε的输出覆盖下界，|I|/ρ≥δ^{-η}。本轮取后者与局部d<1上界相冲突。原文5.5只需第一集合线集中，因此这里的原输入较强。原论文全§8保留为具名定理，不把核 statement 当其全证明复现。
2. Carbery–Valdimarsson, *The endpoint multilinear Kakeya theorem via the Borsuk–Ulam theorem*, arXiv1205.6371v1，Thm1。令其 d=n，正权重、半径1的双向无限直线管：包含方向行列式绝对值的n重和之1/(n−1)次方积分≤C(各族总权重之积)^{1/(n−1)}。缩放半径r带来r^n。固定有界区域内，对有限测度直线族作离散近似，固定倍增管半径，先加强常数阈值再取极限，得到原6.10所需任意正权重/重指标版。仅在n=2,3,4使用；原曲线先在w₀块线性化，不直接把曲线当直线输入。
3. CRP-001已保留GWZ2026 arXiv2601.14411v2 Thm1.1 convex-clustering set estimate；其导出的原2.15加权全时间 plank 估计用于5.1。高级GWZ全证明仍未复现。

加权标签预处理：若实际path law在support上的G_wt≥1，indicator-label upper caps直接成立；对于原6.1允许的一般0≤G_wt≤K，在进入的原parent mixture（总prior×time≤1）先删G_wt<σ_N，取σ_N小于本次进入dense mass的固定小比例，损失≤σ_N。σ_N^{-1}=N^{o(1)}。冻结ν°是删whole lines，未改留下线的prior density，故所有后来indicator restrictions上都有σ_N ν°1_E dt≤λ_E≤Kν°1_E dt。若一次合法fractional restriction产生更小density，有限步骤中在使用label caps前按其当前dense mass再作同样trim并计入总删除预算。于是λ的physical/spatial upper caps除σ_N才可传给product-prior labels，支持性质不受影响；用λ≤Kν°dt只负责dense labels的质量下界。这是明确付费的双向比较，不是由单向domination倒推上界。所有有限步骤先定预算、后慢对角，累计仍K。

任意删选只保未归一的 numerator ceilings。条件 palette、逐管长见证、coefficient-bin floor 都需另付分母。全过程 distinguishes global average density、各Q完整prior和各轨迹duration；不假 upper-AD 的子集有AD下界。候选在每substantial residual重新构造，故不是把一次小成功条件化成全称闭包。AIM是candidate→actual接口，并不倒推本轮的存在性，因而本轮不是其正幂增益层面的等价重命名。

## 3. 先取得原4.13 breadth，再允许稀疏选边

版本2 ℓ=0时，对任意固定κ,u>0，若正质量的可知states在N^{-u}仿射速度线条带内具有条件质量≥κ，则得到原宽度改善矛盾。state须按原p_L与给定已用deep end histories具有≤K种歧义；实际使用的Q/球/符号/细位置格满足它。版本1相应结论是角分离，排除短速度区间。该结论不是任意后续速度依赖删选后的自动 breadth。

反证：把state预测细条带在原共同palette下作heavy化，阈值κ_N=1/K，低palette者由原joint cap删去。把strip法向unit-normalize；每条有eligible |V|≤K的线必有offset≤K，所以参数范围为subpower而不是任意原尺度幂界。以参数距r₁=N^{-u/2}取极大分离代表；交叠条带的交集为空或在半径N^{-u/3}速度球中，palette质量≤KN^{-Su/3}。若代表数M，Cauchy–Schwarz给

    (Mκ_N)^2 ≤ M + K N^{-Su/3} M²,

故M≤K。再以r₂=N^{-u/4}选代表并稍扩条带，交叠可忽略，按速度首个所属代表固定整轨迹 assignment。条带参数、normal midpoint以r₂分格，保原time/depth；法向宽r₂、切向宽单位，满足原改善。列表是给定state的实际短列表，不是把所有M代表直接当每个state的列表。调用AIM/4.12时 map先检验最终selected derivative tests，失败者归non-listable failure。该步骤保存真实编码/复杂度，矛盾ℓ=0。

以后凡需basis，先在还 substantial 的state family上renew此结论，再仅作whole-state或每state固定比例删选。任意稀疏速度选边后不得直接再次声称basis。

## 4. 原5.1 coefficient saturation

x_l(t)=x₀+x₁t+x₂t²，系数有界K，prior≤K，label incidence稠密。假其(t,x)支撑只占≤Kp^{-1-d}个p格，并有每r≥p系数球质量≤Kr^d。先移除过短labeled fibers；引入独立D∼Unif[0,1]，作二维仿射lift

    z_l,D(t)=(x₀+t(x₁−D), D+t x₂),   (1,t)·z=x_l(t).

lift支撑≤Kp^{-2-d}格，每保留索引有≥p^{-1}/K个marks。原2.15给某全时间plank，尺度p/K≤u≤v≤K，lifted mass≥p^{d−1}uv/K。沿plank长时间的三个t值恢复二次系数，所有x系数落在Kv球。对每固定x系数，plank窄法向在t=0或1接受D长度≤Cu，因为 max(|n₂|,|n₂−n₁|)≥c。因此lift mass≤Kuv^d。比较得v≤Kp；除去D接受长度后原系数质量≥p^{d−1}v/K≥p^d/K，再Kp球分成K个p格，某格质量≥p^d/K。

这是任意合规稠密 residual 上的有限标量饱和结论；不假删选后priors已重新normalise或自动有lower floor。

## 5. Scalar-normal系统与每次 tested event 的entropy

x二次，y∈R^j仿射，ν为冻结概率，Glabels≤K。F(t)只依时间/外部world，|F|≤K，S=x−F(t)y，R=x'−F(t)y'。精度ζ以下不读。原Def5.2五项：S在任意q≤r局部区间的q-cover≤K(r/q)^d；每时刻(x,y)q格质量≤Kq^{j+d}；F Lipschitz up ζ；R在标记spacetime Lipschitz up ζ；给定系数r-bin B，q格条件质量≤K(q/r)^{j+d}（q≤r）。各自分母都是当前固定prior或固定ν(B)，不是成功事件的质量。

先独立于轨迹采样有限时间tuple，T包含world与全tuple；在其上任意 dense tested event A（每个指定时刻均有label），Q=P(.|A)。记s(T)=P(A|T)，则

    E_Q(1/s(T))≤1/P(A),   E_Q log(1/s(T))≤log(1/P(A))=o(log N).

同理对(T,B)。这些分母损失只在期望entropy中记o*。sheared joint (S_r,y_r) cap与S-cover上下夹出

    H(S_r|T)=d log(1/r)+o*,
    H(y_r|T,S_r)=j log(1/r)+o*.

给定系数B=l_r，在一个S_q格上对y求和≤K(r/q)^j项，故H(S_q|T,B)≥d log(r/q)−o*。Sr由B确定至K种歧义，再局部d-cover给

    I(l_r;S_q|T,S_r)=o*.

对任意T-known unit row e，薄片计数给联合(y_q,(e y)_r)的fiber上界，减去H(y_q|Sq,T)得

    H((e y)_r|T,S_q) ≥ log(1/r)−o*.

每次后来出现dense discrepancy/tail event，**在该event上重新从以上caps证明**，不沿用一次已经条件化前的平均mutual information。反复使用的合法不等式是

    H(Z|T,C)≤H(Z|T,B)+H(Z|T,A)+I(A;B|T,C).

可由chain rule先加入A再交换A,B得到；没有免费“conditioning decreases conditional mutual information”。continuous时间只用有限mesh entropy，auxiliary tuple/rows须trajectory-independent before labels。

## 6. First jets：5.4，含实际5.5点积接口

给固定有限time hierarchy，最细H*且ζ≤H*³/K，构造time-only有界A(t)，保dense单时刻labels。若u,v在同一长度H块，

    |F(v)−F(u)−(v−u)A(u)|≤KH^{1.1}.

并令J₁=x'−Fy'−Ay，在r≥H*^{(1−d)/64}时对每个后来dense tuple test有H(J₁,r|T,Sr)=o*。

固定组件/尺度前，先计算当前m(t)、总质量δ；删m(t)<τ及total mass<τH的H-block（τ≪δ，成本≤2τ）。各剩active time m≥τ，至少δ/(2H)个好块。在块I令t=t_I+Hu。以Cauchy–Schwarz选anchor t*保共同labels，冻F*=F(t*)；B_l=x(t_I)−F*y(t_I)的H-bin至多KH^{-d}个，每个prior≤KH^d。以H^d作分母，保好C-groups。令

    Y=y(t_I), z=(B−b_C)/H, q=x'(t_I)−F*y', φ=(F(t_I+Hu)−F*)/H,
    L=z+u q−φ Y.

S/H与L误差≤KH。q在anchor处按原R Lipschitz是Y的Lipschitz graph up KH。取p=H^{1/4}；j=2时把其余j−1个Y坐标切p格，prior除H^d p^{j−1}。在slice里q≈G(v)，得到L≈z+uG(v)−φ₁(u)v，联合(v,L)p格质量≤Kp^{1+d}。

对共同label时间u₀，输出碰撞给pair-times质量≥p^d/K；再固定一个起始scalar bin，得到≥p^{2d}/K。关系是

    (u−u₀)(G(v)−G(v'))−(φ₁(u)−φ₁(u₀))(v−v')
      = L'(u₀)−L(u₀)+O(Kp).

每(u,v,v')p格质量≤Kp^{3+2d}，每固定u的总pair质量≤Kp^{2d}。先保有pre-quadrant active time length≥p/K₁的time bins，其损失≤Kp^{2d}/K₁，故restricted triples的cover≥p^{-3}/K。a=(u−u₀,−φ₁(u)+φ₁(u₀))，b=(G(v),v)，b'同形，均为upper-1-AD graph up K。取同象限、同时反射两集合、正比例dilate、只平移第二集合（b−b'消平移）使其入单位盒；所有AD损失是K。WZ的η固定先选、后用K≤p^{-η}。其expansion alternative与scalar局部d-cover冲突，取ε<1−d，输出区间scale ratio≥p^{-η}给指数矛盾。故a-line含≥p^{ε−1}/K个time bins。time-Lipschitz graph迫使该线非vertical、斜率≤K。恢复每个命中bin的整个预先存好的active time set，φ₁在这些times上拟合直线至Kp；总时间≥H p^ε/K。

ε慢降为o(1)，得到H/K长时间、误差KH^{5/4}的fit。**恢复这些times上所有prepared labels**，不只保参与碰撞的pair；m≥τ与好块数保全局subpower质量。对j个组件、有限尺度依次付费。中间hierarchy使H'≥H^{33/32}/2；两见证时间分离≥H'/K比较相邻fit slopes，差≤KH^{5/4}/H'≤KH^{7/32}。最细slope定义A(t)，累积得上述1.1 Taylor误差。

J₁小entropy还需斜率集中。p₀=H*^{1/8}、γ=(1−d)/4。若所有p₀^γ slope intervals只带N^{-c}质量，删duration<τ=N^{-c/4}、小Y-cell后，近斜率输出碰撞≤Kp₀^dN^{-c/2}，远斜率≤Kp₀^{1−γ}=o(p₀^d)，反Cauchy–Schwarz下界。因此每好group有一heavy slope interval；同时间同S_H只有K个groups，J₁的cover≤K个宽KH^{(1−d)/32} intervals。系数r-bin也确定J₁,r至K种歧义，与§5互信息不等式合并得coarser r的结论，必须每新test event重做。

## 7. Higher jets：5.6与独立的最终时间

固定M≥2和h。置c₀=.1，r_i=min(.009,c_{i−1}/2)，c_i=r_i/2，r_min=.009·4^{−(M−2)}，α₀=(1−d)/64。先选

    h≫H₁≫…≫H_{M−1}≫H*,
    H₁^{r_min}≤h^{M+11}, H_i^{r_min}≤H_{i−1}^{1.02},
    H*^{α₀}≤H_{M−1}^{1.02}, ζ≤K^{-1}min(H*³,h^{M+1/2}).

独立于trajectory采二叉时间树（level H_i），另采h-block内uniform t'，其独立于树条件block。Jensen给所有树叶和t'均labeled的概率≥δ^{2^{M−1}+1}；排过近时间差<H_i/K成本小。归纳time-tree rows F_i（不依trajectory或t'）及

    J_i=x^{(i)}−F_i y−iF_{i−1}y'.

一阶Taylor以q=H^{1.01}读给低entropy endpoint jets。差商恒等式

    ∇J_i=x^{(i+1)}(t)−(∇F_i)y(t)−[F_i(w)+i∇F_{i−1}]y'.

若∇F_i在任何fixed positive power高度的tail上有dense质量，除其幅度后会把一个T-known unit projection of y编码到fixed power精度，与§5投影entropy下界矛盾；对该tail重新用§5，慢截取得K界。已知compatibility ∇F_{i−1}=F_i(t)+O(KH^{c_{i−1}})后，编码

    U_{i+1}=x^{(i+1)}−(∇F_i)y−(i+1)F_i(t)y'

至H^{r_i}。与已构造J_{i+1}比较，若rows差≥H^{r_i/2}则又在该bad event上编码unit y-projection至H^{r_i/3}，矛盾。以F_{m+1}=∇F_m完成归纳；系数bin信息和§5互信息不等式负责coarsen conditioning，不能把上一次平均MI直接附加新条件。各H_i schedule保证root jet误差≪p=h^{M+10}，所有leaf reading合法。

令P_F(v)=Σ_{i=0}^M F_i(u)(v−u)^i/i!，不含t'，E=F(t')−P_F(t')。精确scalar evolution是

    S(t')=ΣJ_i(u)(t'−u)^i/i! − E y(t')+O(Kh^{M+1}).

若|E|≥h^{M+1/4}的dense事件存在，给定T、S_u,p及low-entropy root jets，局部scalar d-cover把(E/|E|)y(u)在r=h^{1/4}上限制在Kr^{-d}个bins。|E|r≥h^{M+1/2}≥Kζ且remainder≪|E|r，与投影entropy指数1>d冲突。E的unit row只依T。

回收single-trajectory polynomial witness时冻z=(world,l,tree without t')；t'原先仍uniform于h-block。令good fraction g(z)，∫g=p_g dense；删g<p_gδ仅损≤p_gδ，成功fiber长度≥h/K，且包含计数incidence。投影好tuples回(l,t')的原prior×dt仍dense。固定系数grid舍入保证“存在拟合多项式”的事件可测。这给degreeM、coeff≤K、errorKh^{M+1/4}的同block长时间见证，适用于每个dense residual。

## 8. Physical caps、梯度与唯一冻结prior的bin floors

m=j+1，z=(t,y)，v=(1,V)，W=(z,X)，λ=Gwt νdt≤Kνdt。用实际packets a=p、H∼p^k、ν_Q∼p^dH^j及whole assignments。原joint cap、duration4.9、已准备全时间witness给

    #W_p≤Kp^{−(m+d)}, λ(W_p)≤Kp^{m+d}, λ(z_p)≤Kp^m.

分packet/球/符号，移除mass相对于Hν_Q过小的graph entries，得projection≥K^{-1}，ASM在H尺度上先给derivatives K。每个长line/packet/ball/sign有H/K见证；沿其二次轨迹，原test及complex margin推出|D_v f−X'|≤Kp/H≤K。若physical gradient有positive-power大值，其y-component大，∂_t f+∇_y f·V=O(K)预测power-thin velocity strip。state已知、在足够细位置格以Hessian≤K/H²冻梯度，§3矛盾。慢截断得physical梯度K及used interiors的derivative bounds。细cell轻质量prune同时给hereditary (m+d)支撑上界、每base cell上≤Kp^{-d}个X格。

为系数floor先取细于所有mesh的公共time partition，删每line/time interval内duration<|I|/K₁；joint cap

    λ(I,y-box J_y,X-interval w₀,velocity J)≤K|I|J_y w₀^d π(J)

转为active prior fixed-time cap。再删总体occupation短的线，**一次性冻结未归一ν°**，之后只保λ≤Kν°dt。系数B_p包含X全部二次系数与y全部仿射系数。令α=[y₀,V]_p，Πα=π([V]_p)，则

    ν°(α)≤Kp^jΠα,
    ν°{α,X-coefficient r-ball}≤Kr^d p^jΠα.

若在substantial residual中参与的B_p没有lower floor，某α坏incidences≥p^jΠα/K（Σp^jΠα≤K）。把ν°的这些坏线除p^jΠα，得到§4的scalar问题：r-ball cap Kr^d、支撑≤Kp^{-1-d}、dense labels。5.1给质量≥p^d/K的p-bin，反其bad定义。慢阈值、有限mesh并行后，所有参与bins在**同ν°**下满足

    ν°(B_p)∼_K p^{j+d}π([V]_p).

每B_p使用≤K/p个W_p entries；删entry mass<pν°(B_p)/K₁后，给定W_p,V_p至多K个B_p。因此X'在给定W_p,V_p下有≤K个p-bin，即原6.9。以后删选不把ν°换成当前小残余再声称同floor。

## 9. 固定field G、renewal与相对qualification

先固定a,h,M且h^M≪a₂（可选M更大；a₂由§10固定正指数预声明），再选ζ满足§7，ρ≪ζ,h^{M+1/4}，b/ρ、b^κ/ρ远小于所有比较误差；有限grids/degree/positive exponents全部先定。最后慢增grid数，不能在每个N上无限次付固定比例成本。

**Prop6.2。** 若多数W_b细cells的lifted directions (v,X')没有.9质量靠近某m-plane至b^τ，则§3 breadth逐次抽n'=m+1个方向，det≥b^θ，取θ<(1−d)/3、τ<θ/(n'−1)。在w₀=b^{2/3}物理块内，把二次轨迹线性化（位置误差Kw₀²≪b，角误差Kw₀≪b^θ）。每线最多K/w₀个blocks；先删duration<w₀/K₁再用最近witness，contributing prior≤KM/w₀。CV给占格≥K^{-1}b^θ(w₀/b)^{n'}，支撑upper≤K(w₀/b)^{m+d}；比值≥K^{-1}b^{θ−(1−d)/3}→∞矛盾。

所以平面存在。捕获固定比例的base directions仍有basis，平面是normK的graph，得到W_b常值G，|X'−G·v|≤b^κ，κ=τ/2。renew W_b breadth/palette，在此冻结prepared reference mixture Λ_ref，L_ref≥constant>0。给定粗W_s cell，s≥b^κ，每个G_s-bin选一个fine witness；其well-conditioned base tuple在共同product palette下有≥1/K质量，每固定tuple由6.9仅能见K个rows。总palette质量1，故G_s支持≤K。该已认证support-list upper可遗传任意后来删选。

**Lemma6.4 common choice。** 有限worlds、Z∈R^D、boundedY，测试scales1=s₁>…>s_L=r*，每Z-cell Y支持≤K_i bins。每scale/world先选heaviest coordinate color mod4（4^D种），每保留Zcell再选heaviest Ybin。总质量≥∏(4^DK_i)^{-1}；两个距≤s_i的保留点若不同格则至少隔3s_i，故

    |Y−Y'|≤C(A+B)(|Z−Z'|+r*), A=max s_i/s_{i+1}.

先有限grid，后慢加密使ΣlogK_i+DLlog4=o(logN)且A=N^{o(1)}。成本按world/scale，不按cell重复；若state-only输入则输出whole-state selection。

**Prop6.3 fixed tolerance failure。** 对每固定ε>0，令U_N^ε是没有degreeM、coeff≤N^ε、error≤h^M且同Q/h-block内含该incidence的witness length≥hN^{-ε}的incidences。有限coeff grid及h^M/4余量保证可测。若其Λ_ref-relative质量不→0，因为L_ref≥constant，这就是substantial residual；不更换G/meshes，在failure里renew breadth。

先以G的粗lists作6.4，wholeW_b选择，得|G(W)−G(W')|≤K(|W−W'|+ρ)。在C=W_ρ，冻G_C，以p=ρs'≥ρζ把whole W_b分到X−G_C·z的p-strips，normal derivative O(Kρ)，每line/C只有K strips、总K/ρ pairs。先删duration<ρ/K₁及bad state fractions，最近见证prior≤KM/ρ。最后一次用breadth和CV R^m，每strip有≥(ρ/p)^m/K个basecells。比较normal interval r内的physical upper K(ρ/r)^m(r/p)^{m+d}，得到strip local d-cover K(r/p)^d。之后才许逐edge删选。

world q=(parentγ,完整B_ρ)；subtract中央曲线并除位置ρ，时间不缩放，prior固定ν°(.|B_ρ)。取time-only F_q(t)代表G_y，fine times≤ρ使|F−G_y|≤Kρ且F Lipschitz upρ。scalar S与normal strip up K(ρ²+b)≪ρζ；给定系数B_{ρr'}，spatial q'-cap的分子≤K(ρq')^{j+d}π(V_{ρr'})，除**同ν° floor** ≥(ρr')^{j+d}π/K，得K(q'/r')^{j+d}。这明确支付Def5.2的两种密度。

R=x'−Fy'在固定(W_b,B_ρ)内几乎常值：

    ρR=G₀+G_y v_c−X_c'(t)+(G_y−F)(V−v_c)+O(b^κ).

每β=ρs'参数block用≤K/s' zoom cells。删entry<s'ν°(B_β)/K₁后，在fixed velocity J_β的移动截面time window s'上，raw mass≤Ks'β^{j+d}π(J)，每block支付≥s'β^{j+d}π(J)/K，故R_s'有K种。要消掉velocity条件，再用早先state weights m₀(W) joint cap≤K_pre m₀(W)π(J)，Σm₀≤K_pre；给定W,I=V_ρ至多K_pre² entries E。删entry<m₀(W)π(I)/K_cut，成本≤K_pre³/K_cut，survivors满足conditional palette≤Kπ(J)/π(I)。每Rbin有几乎常值R的entry见证，其palette≥π(I)/K；每细J只能支付K个Rbins，所以给定zoom cell最终≤K个Rbins。注意E只作分析，不成为下一world。

冻结这些有限scale lists，再以world=q、Z=(t,ytilde,x)、Y=R用6.4，得R Lipschitz upζ。令a_q=p_γν°_γ(B_ρ)，Σa_q≤1，总label质量dense故某q有mass/a_q dense。除该**固定**分母，§2低权重trim后的下比较把λ caps传给ν° indicator labels（额外σ_N^{-1}已计入K），上比较给labels dense mass；所以在ν°(.|B_ρ)×dt下全Def5.2成立。§7先拟合time-only F_q，且F_q≈G_y至Kρ，得到G_y的degree≤M fit。再在同一indexed line用G₀=X'−G_y V+O(b^κ)：V常值、X'为coeff≤K的一次多项式，故得到整个row(G₀,G_y)的degree≤M fit，coeffK、误差Kh^{M+1/4}。原sameQ assignment在整h-block固定，故所有witness times仍属该Q。这才是actual全row qualification；K'<N^ε、witness h/K'≥hN^{-ε}、errorKh^{M+1/4}<h^M/4，舍入后矛盾failure定义。只需发现正质量好点即矛盾“该集合全部失败”，不需其质量与整个reference可比。

所以每固定ε的relative failure→0。ε=1/r慢对角得K_qual=N^{1/r(N)}与Λ_ref-relative error e_N→0；这不是所有后来inverse-subpower残余都统一o(1)失败率。

## 10. Cartesian插值：从qualification回到整个state family

记p*=1/k，a∼h^{p*}。选0<α<1/2，ε_T=h^{p*−1+α}，e₁=α/2，a₁=a h^{e₁}，c₀=e₁(1−d)/2，e₂=c₀/3，a₂=a h^{e₂}；e₂<1/24。先选细ξ同时满足Khξ≪a₁及Kξ≪ε_T（后者支付poly沿fiber平移的误差，前者不蕴含后者），并取hξ≪h_i（i=1,2）使descendant格计数有效；速度mesh更细，其余deep meshes先定，不依隐藏w幅度。

回到substantial Λ_ref，renew states D=(parent,Q,W_b)的pencil smallness。用qualification的relative o(1)，仅删conditional failure proportion>η的states，成本≤e_N L_ref/η=o(1)。η取小于basis概率/(2m)，每好state可抽m个qualified、well-conditioned basis witnesses，**这些好state的全部prepared edges仍留着**。以Σp_γ hν_Q≤1选parent/Q好质量≥hν_Q/K。令u=(z−z_c)/h，不作速度shear，base density除hν_Q后≤K。

每ξ-basecell的G在ε_T上仅K个bins：原Q图physical gradient K且ε_T≫Ka，配合Prop6.2粗lists。共同product palette平均固定一组basis bin centers v₁,…,v_m，使其支持states仍≥hν_Q/K；A₀列是(1,v_i)，A₀,A₀^{-1}≤K。正确Cartesian坐标是r=A₀^{-1}u，因沿r_i fiber的物理方向正是v_i。**原PDF97页有inverse上标，提取txt将其串到上一行；不是source坐标笔误。**

每basis fiber上，qualifying degreeM多项式的ε_T coefficient bins至多K：随机取M+1个分离times，落在其h/K见证的概率≥1/K；固定这些times用base-only G-lists及Vandermonde插值只有K种coeff-bins；所有见证共同采样，求和概率得K界。每state先固定一种witness；每fiber随机选一种polybin、每cell随机选一种fieldbin，m+1 tests共同保states mass≥hν_Q/K。

删cell质量<hν_Q ξ^m/K₁，保留grid cells的计数比例≥1/K（因为basecap）。随机选每轴M+1 anchors与一个target，Jensen给所有(M+2)^m vertices retained的概率≥K^{-1}；删anchors过近后固定separated anchors且dense successful targets。逐轴Lagrange tensor interpolation得poly row T，固定总次数、coeffK，在保留cells |T−G|≤Kε_T。cell质量floor把计数回成≥hν_Q/K质量。因T近G是state-property，恢复所选states的全部prepared reference edges。长见证Remez给同Q全block

    |X'_l−T(u_l)·v_l|≤Kε_T.                         (I1)

以早先真实descendants a_i,h_i∼a_i^k、assigned priors≥a_i^d h_i^j/K、每h_i block disjoint assignments计数，有

    # joint (ξ-base, a_i-height) cells ≤K ξ^{-m}(a/a_i)^d,  i=1,2.   (I2)

计算是：每descendant用≤K(h_i/(hξ))^m basecells，每h_i block数量≤ν_Q/(a_i^d h_i^j)，block数h/h_i，乘得Kξ^{-m}ν_Q/(a_i^d h^j)。这里使用完整assigned prior与此前实际饱和witness，不要求最终selected path饱和全部旧floors。

## 11. Switched signed paths与conservativity

以selected incidence probability P起步，总分母≥hν_Q/K，base density≤K。要证

    ||skew DT||≤K h^{p*−1+c₀}.                       (I3)

否则polynomial sublevel保证多数start的skew大。交替2m次：从P(.|当前同D)抽新occurrence，再在其line上按P(.|line)抽time。**删选前两种heat-bath都保同P**；由全部ν_Q与原分母，union bound删各步duration<h/K₁的line成本≤K/K₁。在good restriction后保持kernel未归一，不声称仍保P。每步上界

    dP{V-bin J,t_i∈dt_i,long | past} ≤K π(J)dt_i/h.

backward integration给product palette×Lebesgue times upper；不假成功条件化后的增量独立。选择前、后m个方向均成basis的概率固定正。δ_i=(t_i−t_{i−1})/h可正可负，times→δ是三角Jacobian1。模型base u₀+Σv_iδ_i，height R(δ)为沿T的signed integrals。sameW_b换线、velocity bin、I1误差按先选mesh都≪ξ及a₁/h。固定start的X_start/h平移不改变I2的endpoint格数。

endpoint map是2m→m+1多项式。以首m列A_I成basis，I∪{j} minor除detA_I等于 ∂_jR−(∇_IR)^T A_I^{-1}A_j。若所有这些polynomial minors系数≤η，对δ=0求导得到cross-Hessian≈A_I^T H_sym A_J，其中H_sym来自I-I symmetric Hessian。但直接D²R(0)_{ij}=DT(u₀)[v_i]·v_j，i首半、j后半；两basis反演得skewDT≤Kη。因此至少一minor norm≥h^{p*−1+c₀}/K。

每start/control tuple只有限选一minor；删其低于h^{p*−1+c₀}/K₁的sublevel，backward product upper和固定次数Remez保证path损失小。冻其余m−1 increments，剩m+1维polynomial map在passing Jac≠0 fibers只有固定次数有界的孤立regular preimages（Bézout/semialgebraic cell bound；无需所有fiber都有限）。change of variables给每endpoint cell的preimage量≤K ξ^m(a₁/h)h^{−(p*−1+c₀)}。与I2相乘，成功概率≤

    K (a/a₁)^d (a₁/h) h^{−(p*−1+c₀)}
      =K h^{e₁(1−d)−c₀}=K h^{e₁(1−d)/2}→0,

反先前正概率，得I3。负increments、未归一kernel及regular fiber multiplicity均在此实际使用。

## 12. Potential与heavy intercepts的最近duration预算

定义P(u)=h∫₀¹T(tu)·u dt；正阶derivatives≤Kh，I3给||∇P−hT||≤Ka h^{c₀}。结合I1，沿长line X−P变化≤Ka h^{c₀}≪a₂。按midpoint X−P分a₂ bins，每line一个C；每state只有有界相邻C（state知道足够细X,u及∇P）。对应group的base density（除hν_Q）≤K(a₂/a)^d。

此时不能用早先已失效长见证的prior。先删globally short lines/states中过大loss，再在每state只保C fraction≥固定小阈值（C选项有界），再删long-line failure、各(D,C)中过大loss和whole groups中过大后续loss。总保≥hν_Q/K；每surviving(D,C)占原good state固定比例，故renewed breadth/palette还成立。每group contributing prior≤KM/h，M为其**最近前置**incidence mass。

CV R^m给每group≥ξ^{-m}/K个basecells。联合I2且P在细cell波动≪a₂，groups数≤K(a/a₂)^d。再删mass<hν_Q(a₂/a)^d/K的groups仅固定小成本。heavy group长见证及固定次数Remez给whole同block

    |X−P(u)−C|≤Ka₂.                               (I4)

不是把h/K见证延伸到单位parent时间；全部延伸仅该h-block。

## 13. 原R³七方向的exact tensor核与近conic修复

取p_i=(1,v_i)∈R³七点，每三点独立，范数/逆det≤A。二次齐次q若过七点，其空间≤1维且非零者nonsingular：五个无三共线点决定唯一conic；singular quadratic为两条复线或重线，至多覆盖四个此种点（实点情形同样）。

rank3两拷贝 T(p_i,p_i,.)=0 ⇒三次F的一阶partials全是q的倍数；Euler F=qL，∇F(p_i)=L(p_i)∇q(p_i)=0，故L=0。因此两拷贝map injective。若七点确在同一nonsingular conic q=0，参数化后binary degree6在七点为零，得到rank3三拷贝kernel=q×linear；rank4三拷贝kernel=R q²（对partials用前者，再Euler及q与∂q互素）；rank5三拷贝kernel=0（对二阶partials应用rank3，再积分得到F=q²L，三拷贝迫L=0）。这些也可逐项齐次多项式除法验证。

固定A-compact point family与fixed format semialgebraic singular-value lower bound给逆矩阵cost≤CA^C。rank4结论只在**exact conic family**上有uniform meaning，不把离conic时jump rank的逆硬当连续。

若q norm∈[A^{-1},A]且|q(p_i)|≤ε，compactness函数 |det Q|+Σ|q(p_i)|在coefficient-normalized family上有正下界≥cA^{-C}，否则极限是过七点的singular q。ε足够小给det Q≥cA^{-C}，full gradient亦下界；Euler ∂₀q+v·∇_v q=2q使spatial gradient≥cA^{-C}。沿spatial gradient方向走O(A^C ε)，单变量二次式换符号，有exact real zero p_i'=(1,v_i')。位移≤CA^Cε，triple determinants仍≥(2A)^{-1}。这是原6.7，不假复零点等于实零点。

## 14. 版本1 degree restoration

I4沿line把P与二次X−C比较，Remez给|D_v³P|≤Ka₂。product sampling/palette averaging固定四个分离fine velocity bins，共同states仍inverse-subpower；位置误差Kb/h、velocity mesh errors由P正阶derivatives≤Kh控制，先选b/mesh足够小使transfer≪a₂。组的base mass/cap给inverse-subpower体积，polynomial Remez扩到box。binary cubic由四个分离(1,V_i)方向决定，Vandermonde inverse≤K，故||∇³P||≤Ka₂。P+C的quadratic Taylor polynomial F拟合Ka₂。测试w−F，hidden derivative1、curvature0；heavy mass即§1要求，wholeblock已由I4付。

## 15. 版本2：native test、无绝对隐藏高度的branch控制

对heavy group考察native quadratic equation

    P_*(z,w)=P(u)+C, z=z_c+hu.

观察点residual≤Ka₂，native hidden derivative∈[K^{-1},K]，curvature≤K。discriminant与w无关；它在观察点上下受K控制。heavy group质量/对应basecap使real projection体积≥K^{-1}，polynomial Remez给discriminant及固定derivatives K；在inverse-subpower core balls里有K^{-1}的complex margin。按rootsign选real analytic root f(u)，|w−f|≤Ka₂。

core choice由state center决定；rootsign fractions只固定比例删选，再删line某core/sign内duration<h/K₁以及state过大损失。仅K(a/a₂)^d个group/core/sign choices，故某一选择质量≥hν_Q(a₂/a)^d/K并有samechoice h/K witness。设

    R(u)=P_s(z_c+hu,f(u))/a.

旧长见证P_s(z,w)≤Ka及|w−f|≤Ka₂，隐藏derivative≤K、curvature≤K/a给R≤K；base体积与ASM norm先给R所有fixed derivatives K。此时**先有R绝对导数界，才移动/反演方向**。

令S₀=inf_affine L ||f−L||_U。ASM closure给f的二阶及以上derivatives≤KS₀；不假S₀有任何绝对上界。沿long line，f−w≤Ka₂，w affine，得D_v²f≤Ka₂；R沿line接近degree2至Ka₂/a，得D_v³R≤Ka₂/a。以准备好的state breadth/product palette固定七个每三独立fine velocities，transfer到centers。R误差用先有K导数界；f误差用KS₀，mesh≤h²/K（**不依S₀大小**）。basevolume/Remez后

    D_{v_i}² f ≤K(a₂+S₀h),   D_{v_i}³ R≤Ka₂/a.

固定次微分后，§13两拷贝injectivity给||∇³f||≤K(a₂+S₀h)。若S₀≤a₂/h，quadratic Taylor f₂拟合Ka₂，w−f₂即proper候选。

## 16. 大S₀分支的conic quotient与degree2恢复

若S₀>a₂/h，取affine Taylor L'，q=(Hess f at center)/(2S₀)对应齐次二次项，则

    (f−L')/S₀=q+O(Kh),  K^{-1}≤||q||≤K,  |q(v_i)|≤Kh.

§13近conic修复给exact real conic与shifted directions v_i'，位移≤Kh，triple det仍K^{-1}。R独立导数界使三/四/五阶tests的shift error≤Kh≪a₂/a（e₂<1）。exact conic上的rank5/4/3 kernels先后给

    R=R₂+q L₁+λq²+O(Ka₂/a),

R₂ degree≤2，L₁ linear，λ scalar，所有coeff≤K（fixed-degree乘法无零因子及compactness给product norm lower）。令H'=(w−L')/S₀。计数点H'=q+O(Kh)，|H'|≤K，因为a₂/S₀<h。构造

    P_new=P_s−a(R₂+H'L₁+λH'^2).

u、H'、L₁均对native variables affine，所以总次数≤2。值≤Ka₂：用w≈f及q→H'替换，误差Kah≪a₂。隐藏一阶导数改变量≤K a/S₀≤K h^{1−e₂}，小于native旧lower；隐藏曲率≤K/a+Ka/S₀²≤K/a₂，后项用S₀>a h^{e₂−1}。这里仅归一化H'有界，绝不要求w、L'或S₀绝对有界，也不在看见S₀以后选velocity grid。

沿实际trajectory P_new是time二次，hidden derivative是time至多一次。计数long witness h/K上lower成立、value upper成立，以same h-block的fixed-degree Remez扩展value/upper derivative到全block；lower只在counted points，二阶derivative对w常值。没有从h/K见证外推到unit parent。此选择保持质量hν_Q(a₂/a)^d/K，无额外discard，正gain e₂ks不减少。

## 17. 每个residual的闭合、Cor6.9及失败测试

任意substantial residual→physical estimates/Prop6.2仍substantial→固定Λ_ref的qualification relative o(1)→fixed-threshold whole good states→Cartesian选Q并恢复其prepared edges→signed-path conservativity→heavy intercepts→两个版本degree2 restoration。所有参数来自fixed powers和固定深度；subsequence后ks正有限。AIM/4.11接收的是实际proper candidate，并负责回原尺度输出与guard，analytic K不被直接当原slack。因每个hypothetical residual都能重新执行，满足AIM的全称量词。CRP对bad scalar问题给k>0 tangent，故矛盾，得到原Cor6.9。

独立反攻边界：任意删选不保ν° floors；qualification的单个dense good subset不自动给relative o(1)，必须fixedε failure argument；后验tuple entropy必须fresh tested-event；signed good kernel不能归一；heavy group prior只用最近duration；conic rank4不能离exact family直接取极限；S₀不能事后决定mesh；wholeblock Remez不能延长到parent。每一项均已在对应§明付。没有找到保原全部假设的counter；未拿toy/finite algebra证据替代连续证明。

## 18. 认证边界与下一阶段

ISO-001已通过两次正式全稿交叉审查，登记为原Theorem6.1/Cor6.9在§2具名输入下的内部复现，所有full-source/high-dimensional flags仍false。TCM/ASM/TEX/CRP/AIM既有独审证书本身范围不追改。本轮只增加这一完整branch gateway。

R36必须macro：重新估算余下finite/infinite窄度、§7 retained-edge工具、scalar projection读出、原finite statement以及外部输入/KT责任与conditional6D出口的代价；比较直接五维实际模型的新输入，不能因上一节刚完成而自动逐节续审。不将原4D论文署名当证明保证，不因长Goal未完成而降低‘重大’标准。
