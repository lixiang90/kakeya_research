# R0036：完整 scalar mesh projection 与无界优化窄度排除

2026-10-17。UNB-001 主证明，修后完整主稿已通过两次实际全文独审，见research/reviews/R0036_scalar_projection_and_normalization_review.md及R0036_graphs_and_actual_atlas_review.md。对象为原Theorem8.2（PDF118–121/文本6309–6479）及Prop10.1全部§10.1–10.7（PDF154–168/8255–9029）。原TeX 07-finite-narrowness.tex与09-unbounded-narrowness.tex已入library且本地Git blob/字节与官方一致；这里只认证前者的8.2，未认证其余finite分支。未经外部同行评审，不声明新颖/重大结果。

## 1. 总命题及输入

固定原version2 cap class C(d_initial)、d_initial<1、角参数S,η>0，按CRP的原极值设置，critical cap d<1、maximizing horizon H(E_i)→k>0。结论：global optimized narrowness ℓ（对maximizing sequences取inf、对terminal narrowness取sup）必有限，即原Prop10.1。反证假ℓ=∞；要产生固定正深度c′、time exponent→0的原p₁-known actual atlas，以实际列表/几何slacks、预定复杂度及原质量覆盖反极值。

输入为已独审TCM/ASM/TEX/CRP/AIM/ISO与其列明基础。实际新共享输入8.2在§3–5完整支付，不把scalar zero horizon一句直接当finite输出。已发表WZ5.2/CV1按已知具名定理调用；CRP所列新GWZ2026集合估计仍是明确保留的高级输入。本证明不认证正finiteℓ/§7–9整链、2.17/finite/Hausdorff读出或KT全proof，不删除高维条件。

8.2是ISO的finite weighted实现，不另立新数学方向；完整∞排除则不是ISO或finite-ℓ AIM的一步改名。后者没有fulltime localization、质量/面积相对抵消及∞情形的original atlas recovery。

## 2. 固定测度与restriction规则

原世界权重ω_γ固定，ν_γ为轨迹prior，原time单位[0,1]。µ_ref=Σω_γ µ_ref,γ为原tempered path，mass p_path≥K₀^{-1}；K₀=N₀^{o(1)}是每个固定exact E_i的实际subpower。earlier true full-layer assignments与其ν_γ(Q)不随µ_ref的后来删选改变。分析对角N=N₀、i→∞上可有K=N^{o(1)}，但不得把它直接当实际output slack。

任意submeasure只保raw numerator caps/support上界，不保新的conditional palette或floor。本轮投影一律用固定q_Aν_γ(A)作分母；最后新chart world则用**该新whole-assignment prior** ν_c，c=(A,b)，不能误用整ν_A。global Σω_γq_Aν_γ(A)≤1支付选取dense A的平均论证，逐line普通duration另付。

8.2的input本来是任意active µ_act≤Kνdt，不需将其support标签反推product-prior upper；mark构造直接以原µ_act(tag×time-bin)收费。它不同于R35 scalar-normal调用时要先付双density比较。后续原law recovery的几何label map先检查whole-block fit及该incidence最终selected tests，失败一律non-listable failure；whole-trajectory assignment仍固定。

## 3. Theorem8.2：从raw active law到共同平滑exact问题

固定probability ν上的indexed trajectories，y scalar affine、x scalar quadratic，五系数≤K，允许其它轨迹坐标。µ_act≤Kνdt，mass≥K^{-1}。固定a=N^{-s}、σ∼N^{-M}，M>s；c,c^{-1}≤N^C。假每(σ,σ) basecell及宽p=N^{-r}的x-bin（0≤r≤s）有active mass≤Kσ² c p^d，terminal occupied (σ,σ,a)-cells数×σ²≤Kc^{-1}a^{-d}，d<1。由unit-width(p=1) cap及terminal support得d≥0：每occupied basecell的全部x质量≤Kσ²c（x范围仅K个unit bins），basecell数≤terminal triple-cell数≤Kσ^{-2}c^{-1}a^{-d}，故totalmass≤Ka^{-d}；若d<0便反dense mass。不能只将terminal-width cap乘terminal support，因为那会把a幂相消。

把五系数round到σ′≪σa²的固定更细幂。有限tags j的ν-weight为ω_j，使用原tag×timeσ-bin的完整质量，若µ_act(j×I)≥ω_j σ/K₁则mark I。unmarked总质量≤1/K₁，选K₁远大于进入inverse-density后可忽略。记M_j为marked bins之并。对五系数加**同一分布**ρ_σ（五坐标独立uniform noise），prior ν_jit=Σω_jδ_j⊗ρ_σ，marked law 1_{M_j}(t)ν_jit dt。由µ_act≤Kνdt，marked law总质量dense。

新prior在五连续系数坐标上piecewise constant、密度≤σ^{-5}，tags/marks数polynomial，故为tempered版本1 exact问题，hidden w=x。ω_j没有inverse下界的需要（j为内部index）；其它原坐标只在回收时按原tag条件prior带回，不伪作新observed features。

固定(t,y)与x_p-bin，能贡献的marked tags的总ω_j≤Kσ c p^d：对应原tag在其整time-bin内的active incidences落在K个邻basecells和x_p邻bins，原cap给总mass≤Kσ²cp^d，mark threshold除σ。noise的y-intercept密度≤1/σ，得exact-base x_p ceiling Kcp^d。独立y-slope noise若再限制宽ρ slope-bin，多因子Kmin(1,ρ/σ)。若原terminal cap有额外N^{-S₁u} y′-gain，则对固定0<u≤u₁且u<M，noise enlargement远小于bin，marked law同样有Kc a^d N^{-S₁u} ceiling。所有是raw ceilings，后删选可保。

noisy terminal support只在原active terminalcells的K邻格中，故base Lebesgue measure×x_a计数≤Kc^{-1}a^{-d}。按原homogenization/有限grid准备profiles，C₀=lim log_N c：

    n(s)∼c a^d,  f(r)≥dr−C₀,  f(s)−f(r)≤d(s−r).

这些来自同一marked law的support upper与density upper夹逼，不假原prior下界。

## 4. Theorem8.2：无角输入时crop，所有world权重抵消

若已有terminal angular gain，则新问题属于C(d)，直接ISO/Cor6.9取任意小horizon。否则homogenize joint profiles f(r,u)，0≤u≤U=4(M+s+1)。令R=(1−d)/2>0、固定小ε>0，最大化

    (1−R)r−f(r,u)+εu,   (r,u)∈[0,s]×[0,U].

在(s,0)值C₀+Rs；slope noise ceiling给其上界C₀+Rr+εu−(u−M)_+。故maximizer(r₀,u₀)满足

    s−r₀≤εU/R, u₀≤M/(1−ε), f(r₀,u₀)≤f(s,0)+εU.

对r的optimality给终端slope cap1−R；对u的optimality给f(r₀,u₀+b)−f(r₀,u₀)≥εb（0≤b≤r₀）。ε足够小使r₀>0且u₀+r₀≤U。

以G∼N^{-u₀} crop y-intercept及velocity，每crop C取conditional prior及真实world weight p_C。crop总数polynomial，删极轻crop再normalise仅付subpower，总质量仍dense。减central affine motion并除y以G；若used p_C∼N^{-α}，within-world density乘G/p_C，故

    f′(r)=f(r,u₀)+u₀−α.

这不是跨world平均density：给exact base与old slope bin，intercept crop因y₀=y(t)−ty′只有bounded options；old/new joint grids在固定crop中bounded overlap。于是new problem在C(1−R)，角指数ε。ISO给其任意小horizon，不要求f′(0)有界。

lift回原noisy single world，packet time q、physical interval widthβ（含G）与原mass floor：

    mass/q ≥ p_C N^{-f′(r₀)}(β/G)/K
            = β N^{-f(r₀,u₀)}/K
            ≥ β c a^d N^{-εU}/K.

p_C和G真实抵消。crop trajectories disjoint，true assignments在每block disjoint，原world weights保成功总质量。送ε与horizon tolerances慢趋0后，先每fixed tolerance取late successful exact samples，再对角，得q≥K^{-1}、thickness≤Ka、mass≥q c a^dβ/K，所有是本finite theorem允许的tangent subpower。额外坐标从未进入crop信息或改变原prior。

## 5. Theorem8.2：fulltime、interval尺度及共同jitter回原law

block position bounds把y′限制到moving center slope±Kβ/q，q≥K^{-1}。在exact base，quadratic graph只用K个x_a bins。积分base area Kqβ的density ceiling，并用额外slope-noise factor Kmin(1,β/σ)与packet mass lower比较，迫β≥σ/K。若有原angular gain，而β有任意fixed-power缺损，则取足够小fixed u>0的slope-bin把全packet velocities包含，积分同augmented ceiling多N^{-S₁u}，与mass floor矛盾。因此optional case β∼1（up subpower）。

用block时间和(y−y_c(t))/β归一化，x coefficients/ranges≤K；mass floor与base ceiling使|F|≤K的真实base set体积≥K^{-1}。polynomial Remez给F在adapted coordinates norm≤K；q≥K^{-1}允许从q-block外推至unit time仅付K。affine position与沿trajectory的quadratic fit errors同理。moving center亦≤K，因为一条bounded assigned trajectory在chart中。此处q不是fixed positive power小时间；这正是合法unit-time外推的原因。

选一个block（共K个）保dense marked mass。**在固定jitter之前**，disjoint label floors给Σ_labels c a^dβ≤K（每floor含q且q≥K^{-1}）。对共同noise vector u求平均，固定一个u保dense assigned marked-time mass，不能逐label各选jitter。对一个获选tag，把其全部原轨迹assigned到同label，unrounding误差O(σ′)≪aβ的所有adapted误差余量。

若公共jitter的affine/quadratic噪声为∆y、∆x，改center为y_c−∆y、predictor为F(t,y+∆y(t))−∆x(t)，保fulltime fit/norm。每贡献的marked tag-bin原active mass≥ω_jσ/K₁；因fit已fulltime，恢复此tag在该bin的**整个原active part**，含edge bins，保globaldense。最后以固定总阈值预算Σc a^dβ≤K删恢复mass不足c a^dβ/K′的labels，仍dense。旧label floor不会自动穿过固定jitter，必须用此最后重删。再dyadic pigeonhole使βcommon，输出disjoint whole-trajectory labels、moving affine interval宽Kβ、fullunit quadratic fitKa、每label原active mass≥c a^dβ/K。

∀eligible finite models只要exponent ranges共同固定，可统一取subpower：若存在fixed-power failure sequence，逐N选择该model便由上述subsequence论证矛盾。故8.2可fresh用于每个dense residual，需其fixed prior/rawcap/support及mass全部重新核；不把一次成功自动传给任意subprobability归一law。

## 6. ℓ=∞的nested true systems与原zero-depth cap

CRP允许先在一true intermediate system normalize、rescale剩depth为1，得到仍maximizing E_i，own-depth saturation/knowledge给n_i(0)∼1，故relative profiles成为f_i(r)→dr均匀（0≤r≤1），d_i→d<1，H(E_i)→k>0。原trajectory |y|+|V|≤K₀，native X=P_*(t,y,w)，hidden derivative scale B。

在exact base，|P_*|≤K₀、|P_*w|≥B/K₀的tested part只用K₀个宽1/B的hidden bins：quadratic只有bounded monotone pieces，每段inverse interval长度≤CK₀²/B。与n_i(0)∼1的good entries给zero-depth base density≤K₀。此为原法则cap，不能在稍后的tiny A条件化后免费重用。

先选0<u<η、0<s₁<s₂<1且(d+2k)s₂<Su/4。CRP segment construction在ℓ=∞假设下给nested true Q₁,Q₂，r_{j,i}→s_j，q_j=N₀^{-h_{j,i}+o(1)}、h_{j,i}→ks_j，g_j=N₀^{-α_{j,i}}，α₂,i−α₁,i→∞。后段normalize后仍maximizing，global∞使其narrowness发散，乘fixed positive depth差仍发散；不是只任意选一大narrow chart。

full-layer assignments固定且同block disjoint：ν_γ(Q_j)∼n_i(r_{j,i})q_j²g_j。both labels实际known by p₁，angular fullness给majorwidth q_j（up K₀）。令D_j spatial matrix、n_j left minor normal，center y_j(t)，则全Q_j-block

    |n_j·(y−y_j(t))|≤K₀q_jg_j,  |n_j·(V−y′_j)|≤K₀g_j.

nested D₂=D₁R，||R||≤K₀q₂/q₁及Q₂majorwidth≥q₂/K₀给|sin∠(n₁,n₂)|≤K₀g₁。

## 7. Prop10.2：两次原time采样与fulltime C标签

对同原trajectory以原ν和world weights独立抽t₀,t，要求两次path incidence。Jensen给pair mass≥p_path²≥K₀^{-1}。先删t-incidences的bad terminal joint angular(u/2)、terminal pure lower、zero-depth upper entries；extra time长度1，cost不乘任何label数。

固定t₀,γ，fullQ₂ saturation/disjointness给至多K₀/[n_i(r₂)q₂²g₂]个first labels。固定一个。若later n₂(t)与first normal角大于g₂N₀^u，则两velocity strips交在radiusK₀N₀^{-u}球；每p₁(t)只有K₀个later Q₂ lists，故只K₀个old N₀^{-u/2} velocity bins。good joint cap给numerator≤K₀N₀^{-Su/2} times pure p₁ density。

先只积分permitted good zero-depth ancestors（每base K₀ hiddenbins、total densityK₀）。first label的whole-unit extrapolated transverse strip宽K₀g₂、tangentbounded，time t可用area≤K₀g₂。因此sum first labels后的bad pair mass≤

    K₀ N₀^{-Su/2}/[q₂² n_i(r₂)]
      =N₀^{-Su/2+(d+2k)s₂+o_i(1)+o_{N₀}(1)},

为fixed power小，低于pair mass。exceptional masks在计数前删，不放大。

按平均选fixed realt₀保subpower paired successes。对trajectory在t₀的Q₂只记录unit normal、normal-center intercept及normal-center velocity，全部bin到g_C=g₂N₀^{2u}，sign以有限orientation charts处理；不存first Q₂ identity。representatives给fulltime C：tangentwidth1、normalwidthg_C，native test仍P_*。position/velocity原affine tests外推误差≤K₀g₂，round误差≤K₀g_C。

later Q₂ normal距first≤K₀g₂N₀^u=o(g_C)。两个标签都控制同一bounded affine trajectory，故normal intercept/velocity也各差≤K₀g₂N₀^u；given later actual Q₂-list，只K₀ neighboring bins恢复整个C，故actual p₁-known。仅近parallel normals不足，center motion是必需标签。因g_C/g₁=N₀^{−(α₂−α₁)+2u}，它远小g₁；结合nested比较，在retained Q₁-incidences

    |n₁−n_C|≤K₀g₁,  |n_C·(y′₁−y′_C)|≤K₀g₁.

这些是label常参数，整块可用。选择输出只用原path/geometric角tests/finitebins，analysis masks不用编码；每fixed i tempered bounds可大但固定。

## 8. Lemma10.3：C→A后绝对density shift真实抵消

normalize C的空间、不改time/hidden/native P_*。newworld (γ,C) prior为ν_γ(.|C)，weight=ω_γν_γ(C)/W，W=Σω_γν_γ(C)≥K₀^{-1}。raw law只整体除W；terminal density equality

    n′_i(1)∼n_i(1) g_C/ν_γ(C),

intermediate仅n′_i(r)≤n_i(r)g_C/ν_γ(C)。若g_C/ν_C=N₀^{t_i+o(1)}，则f′(1)=f(1)−t_i、f′(r)≥f(r)−t_i，所以f′(1)−f′(r)≤d_i(1−r)。prime velocitybin映入old K₀倍ball，terminal angular同因子，故E′_i仍C(d_i)。没有f′(0)绝对界。每prime terminal true system可lift，故H(E_i)≤H(E′_i)≤k(d_i)，仍maximizing。

取b_i→0足够慢：每fixed b先i晚以得relative profile、初始H≤L给b-coarsening small horizon，再选true packets A′并saturate。compose C得original A，time q_A=N₀^{-h_A,i+o(1)}、h_A,i→0、actual p₁-known。terminal equality和A′ true floor给

    ν_γ(A)/J_A ∼ n_i(1) n′_i(b_i)/n′_i(1)
                 =N₀^{-d b_i+ε_i+o_{N₀}(1)}, ε_i→0.

所有absolute primed shifts取消；它是两limit o_i(1)+o_N(1)，固定i不宣称actual subpower。全original budgetΣ_{γ,I,A}ω_γ q_Aν_γ(A)≤1始终保留。

若e_Z tangent C，则||D_A^T n_C||≤K₀g_Cq_A。还可保||D_A^T e_Z||≥q_A/K₀：否则两physical widths都比q_A fixedpower小，endpoint tests迫每A的原velocity进radiusK₀(N₀^{-ε}+g_C)球；actual A-list于p₁只K₀个选择，good terminal angularcap及rawdenominator积分给power-small mass，反原subpower成功。先删bad entries后求和。这个first-width lower不是从矩阵det上界免费推出。

## 9. 正深度、finite-sample guard与对角次序

取d<d_aux<1，ASM/Cor3.4在两base变量quadraticgraphs的容差ε_*。固定0<θ<min(1,ε_*/4)、2θ<ε<ε_*；C_match≥1涵盖稍后固定degree/list/fit/marginal所有loss指数。选

    0<δ<min(θs₁/4, εs₁/(2C_match)),  c′=θs₁/2>0.

这些在样本前固定。i足够晚h_A,i<kc′/2。若有actual p₁-known atlas于depth c′/time q_A，其合法normalization与remaining true system给

    H(E_i)≤h_A,i+k(d_i)(1−c′)≤kc′/2+k(d_i)(1−c′),

极限<k；§16详细核newparent无需truefloor。故每fixed i可预选一个够大的polynomial output complexity bound C_i（依old problem/path/fixed constants），允许outputlists/slacks≤(K_path logN₀)^{r_i}、success≥p_path/logN₀。若无限样本有这种output，tempered subsequence形成exact knownatlas，矛盾。因此N₀可任意晚采在excluded range。

先fix i/old path/allfixedexponents/复杂度bound，后late N₀，再outer i→∞。在N=N₀ diagonal吸收K₀、两limit errors和有限grid阈值为analysisK。output参数族/count由§13–15给polynomial bounds，事先选C_i涵盖它们；没有看见成功candidate后再提高guard。这里不要求C_i uniform-in-i，也不把N^δ/analysisK当actual path slack。

## 10. Lemma10.4：冻结earlier witness与native stable graph

先准备throughs₁的goodpureceilings（含0,r₁）和p₁ purelower/jointupper；固定i/tolerance坏mass power-small，late采样使它o(p_path)。由Σω_γq₁ν_γ(Q₁)≤1，删Q₁-entry mass<q₁ν_γ(Q₁)/K后成本o(p_path)。冻结这些whole-block earlier witnesses W_{γ,I,Q₁}，mass≥q₁ν_γ(Q₁)/K，disjoint并有old zero-depth cap；它们不必是最终µ_prep子测度。

在Q₁ normalized base û=((t−t₁)/q₁,D₁^{-1}(y−y₁(t)))，令z=Bw、a_fit=N^{-r₁,i}∼a=N^{-s₁}。true quadratic P满足|P|≤K₀a_fit、|P_z|∈[K₀^{-1},K₀]、|P_zz|≤K₀/a_fit。r₁ cap+chartJacobian给base density≤Kq₁ν(Q₁)，因此witness projection体积≥K^{-1}。

D(û)=P_z²−2P_zzP与z无关，fixeddegree；real projection上K界→polynomial Remez给complex norm/derivativeK。若|P_zz|≥(a_fit K′)^{-1}，affine center z_c=−(linear coefficient)/P_zz距actual z≤Ka_fit。否则选K′≫K₀³使2|P_zzP|≪|P_z|²，D正且≥K^{-1}。在invsubpower core boxes及fixed-factor complex margins，D variation小于其lower，roots holomorphic；linear case保持linearcoef非零。每label仅K core/branch entries。

再次按q₁ν(Q₁)预算删light core entries，real projection仍≥K^{-1}。center/root compose nativeP_*（w=z/B），nativehiddenderivative/curvature给X errorKa_fit；因X≤K₀，ASM无heightlower normlemma给每usedcore上的algebraic graph G及∇G≤K，且|X−G(û)|≤Ka。边界用overlapping interiors，不同entry分开比较。冻结最终µ_prep（mass(1−o1)p_path）；以后只restrict它。原W在二次删除前已冻结，仅用于whole-domain计数，不把其floor追认为条件于A的current floor。

## 11. Lemma10.5：fixed-budget projection的cap和support分别证明

对original A-block令τ=(t−t_A)/q_A，Z=e_Z·y，ζ=(Z−Z_*)/q_A，Z_*是midpoint center的tangent值。ζ affine、dζ/dτ=e_Z·V，Xquadratic，scalar系数≤K。令

    λ_A=(T_A)_*(µ_prep,γ|I,A)/(q_Aν_γ(A)),  R_A=ω_γq_Aν_γ(A).

λ_A由fixed probability ν_γ(.|A)dτ支配，不按currentmass归一；ΣR_A≤1，||µ_prep||=ΣR_A||λ_A||。

**density。** ζ宽b切A-domain的原spatial area≤K₀J_A b，因||D_A^Te_Z||/q_A≥K₀^{-1}。每exact oldbase的X_p-bin用K₀个p/B-hidden bins。积分prepared purecap、dt=q_Adτ，再除q_Aν_A，得projecteddensity≤Kp^d J_A/ν_A≤Kp^d，最后仅在选定diagonal用§8的两limit抵消。terminal adjoinedζ′ widthN^{-v}（fixed0<v≤u₁<u）与C-normalvelocity精度K₀g_C一起只需K₀个oldvelocitybins，goodterminal jointcap多N^{-Sv}。坏entries先删、只在permitted good ancestors中sum，不将tinyangularfactor乘未删exception。

**support。** 取fixedM>1+s₁+ks₁、σ∼N^{-M}。每projectedcell至多碰两个Q₁ timeblocks（q_Aσ≪q₁）。compatible Q₁-center在其整block内都位于同moving box：tangent宽K₀q₁、normal宽K₀q₁g₁。compatibility给一时刻位置，§7的n₁≈n_C和center-normal velocity差O(K₀g₁)把它延全block，majoraxis投影到n_C只付q₁g₁。故**whole originalQ₁ domains**及其W witnesses都在该box。zero-depth cap与disjoint W给

    L₁ q₁[n_i(r₁)q₁²g₁]/K ≤Kq₁³g₁,
    L₁≤K/n_i(r₁)≤Ka^{-d}.

不用条件于A的witnessfloor，也不sum所有C labels。

在同projectedcell、同Q₁/core，两个occurrences可属不同trajectory。|∆t|+|∆Z|≤K₀q_Aσ；C-domain给n_C·∆y=n_C·y′_C∆t+O(K₀g_C)。分解n₁=c₁n_C+c₂e_Z，|c₂|≤K₀g₁，先减同Q₁-center，利用n_C·(y′_C−y′₁)=O(K₀g₁)，得

    |n₁·(∆y−y′₁∆t)|≤K₀(g₁q_Aσ+g_C),
    |∆û|≤K₀[q_Aσ/q₁+g_C/(q₁g₁)].

**先取消time项的g₁，再除小轴width**。两项分别N^{-M+ks₁+o1}、N^{−(α₂−α₁)+2u+ks₁+o1}，均≪a，无需g₁任何fixed-power lower。graph derivativeK及fitKa使每graph只用K个X_a bins。Kgraphs×L₁给每basecell≤Ka^{-d} Xbins，总support≤Kσ^{-2}a^{-d}。同λ_A上的两个估计保任意后续restriction。

## 12. 每substantial residual的candidate与greedy全局覆盖

任意子列上µ_res≤µ_prep、mass≥κp_path。globalbudget给某A的λ_A,res=(T_A)_*(µ_res,γ|I,A)/(q_Aν_A) mass≥K^{-1}。其fixed prior仍ν_γ(.|A)，§11cap/support保留，8.2取c=1且terminalangulargain，得β∼1、quadratic F(τ,ζ) norm≤K、wholeunitblock |X−F|≤Ka，原incidence mass≥q_Aν_A a^d/K。这里β~1且centermotionK才把adapted norm转成ordinary coefficientK。

在每A依次插入coef≤N^δ、whole-blockfit≤aN^δ、residual masked mass≥q_Aν_A a^dN^{-δ}的quadratic。每次对所有still-unassigned A-trajectories满足该whole-blockfit者作wholeassignment，再计其原µ_prep incidences。单轨迹incidence duration≤q_A，故每insert移走prior≥ν_A a^dN^{-δ}，每A最多N^δa^{-d}项。finite stopping只用prior预算，不将一次subpower发现当constantcoverage。

设µ_c为所有coveredincidences，保原worldweights与analysismasks。若||µ_c||/p_path→0，终止residual仍substantial，上一段在further子列给另一eligible候选（K≤N^δ），反终止。故some subsequence有||µ_c||≥κ₀p_path，κ₀>0 fixed。fixed orderedgeometrictests与wholefit assignment实现上述greedy映射，analytic residual search只用于找常数，不输出其mask。

## 13. 同原observation的posterior比较，分母与Cor3.4

O=(p₁,A)含world/block，m_c=O_*µ_c。conditionalprobability π_o来自**未归一**µ_c pushforward，Π=∫π_o⊗π_o dm_c(o)，故||Π||=||µ_c||、两incidence marginals皆µ_c。sameO给sameτ,ζ，terminalhiddenbin与nativebounds给|X₁−X₂|≤K₀N₀^{-1}；加fits得|F−G|≤aN^{Cδ}。

若coeffmax差>a^{2θ}的badpairs占fixedpositive比例，global ΣR_A≤1给某world/A的within-worldbadmass b_A≥q_Aν_A/K。只有此时normalizebadpairs成probability，marginals≤(q_Aν_A/b_A)λ_A≤Kλ_A。不把每个tiny A都当probabilitydense。

一assignedindex在base的fit只容N^{Cδ}个X_a bins，故marginalbase density≤KN^{Cδ}a^d。每color list≤N^δa^{-d}项，令ρ_{j,f} uniform其list，a^d≤N^δρ_{j,f}，得到ASM/Cor3.4所需index-base domination KN^{Cδ}ρ_{j,f}dτdζ。两colors可相关，Cor3.4允许这原pair law。

把K-boundedζrange affine resize进fixed comparisonbox只付K。quadratic graph norms≤KN^δ，commonreference0、normscale1、matching∆=a、R=a^{-1}。Cδ/s₁<ε/2支付list/norm/value/marginal所有fixed losses，K=R^{o1}。coeffgap>a^{2θ}给normgap≥R^{-2θ}/K>R^{-ε}，因2θ<ε。badpairprobability1且d<d_aux<1，矛盾Cor3.4。故badpairs=o(total)。此用raw b_A分母与uniformreferenceρ，不偷用posterior最小概率。

bin六个ordinary(τ,ζ)coefficients至a^θ。goodpairs系数差≤a^{2θ}≪a^θ，故落bounded neighboring bin list。对每o，若β_o为coeff-bin posterior，E_{b∼β_o}β_o(neighbors(b))等于good-matchprob；选maximizingcenter并积分m_c，给deterministic bounded lists保fixedpositive coveredmass。compose actualA-lists于p₁只乘actualK_path固定幂。

## 14. 合并tests、nativequadratic与实际全块bounds

在每A合并相同coeffbin，取binnedquadratic F~_{A,b}。原native测试

    P_new(t,y,w)=P_*(t,y,w)
       −F~_{A,b}((t−t_A)/q_A,(e_Z·y−Z_*)/q_A).

总degree≤2。wholeassignedblock误差≤aN^δ+Ka^θ；δ<θs₁/4、θ<1、c′=θs₁/2，两个幂均严格优于c′，所以late diagonal上≤N₀^{-c′}，analysisK被positivebuffer吃掉。第二项不含w，P_new,w=P_*w、P_new,ww=P_*ww；原actualnativeupper、countedlower及K₀B²curvature保留，后者强于depthc′所需K₀B²N₀^{c′}。frame/time仍原A，geometryslacks只actualpath固定幂、time exponent仍h_A,i→0。

特别是合并label的fullassigned priorν_c可能远小于ν_A；后续actualcompletion用ν_c，candidate发现/投影仍用ν_A固定budget，两者不混。输出atlas不需新truefloor。

## 15. 原law可实现的assignments、lists与预声明complexity

每A储存orderedtests，trajectory按第一个whole-block geometricfit assigned，再mergecoeffbins。timequanitifier只有单变量、fixeddegree可用fixed-format elimination；每A tests≤N^δa^{-d}，A总数、inverseq_A、coordinatechanges/nativecoeffs各在fixedi有polynomialbounds。realconstant无需bitheightrestriction，旧tempered定义允许它。由oldbounds与fixedexponents预先选择C_i覆盖全部操作，不依analysismask描述或具体搜索。

把geomlabelmap(A,b)附于原µ_ref。**wholeassignment不变，但每incidence只有finaltest/derivative条件也合格才报label；否则failure且不进任何列表**。在µ_c上nativeconditions/wholefits都成立，故map与posterior一致。此显式沿用R34已审的failure校准，避免rawposterior把有效success替换成无效points。

µ_c≤µ_prep≤µ_ref未归一；boundedcoeff-bin lists保其fixedfraction质量。4.12以原µ_ref的jointlaw与该finitegeometricmap回收，选择maximal rawsuccesslists至少保analyticalsubmeasure所供质量；不比较normalizedposteriors。lookup只看原p₁，A仅通过旧actualshortlist并入；hidden/pathtags不当observedfeature。2.4 jointTV flattening在fixedC_i bounds后选fixedmesh，误差O(N₀^{-1})，列表仍(K_path logN₀)固定幂。analysiscaps/masks与residualsearch不编码。

原成功≥constant·κ₀p_path，因p_path≥N₀^{-o1}，flatteningerror可忽略且最终≥p_path/logN₀。所有derivative/geometryslacks实际，coefvalue的analysisK只靠positivebuffer进入原thickness，不冒actualslack。得到§9预排除的depthc′/timeq_A actual p₁-known atlas。

## 16. 最后normalization与truechild：无需parent新floor

newparent c=(A,b)使用其wholetrajectorypriorν_c、spatial determinantJ_A；输出success M≥p_path/logN₀，Z=Σω_γ q_Aν_c≤1且Z≥M，newnormalizedmass M/Z仍actualsubpower。由terminalp₁-knowledge，2.13给

    n′(1−c′)∼n(1)J_A/ν_c,
    n′(r)≤n(c′+r)J_A/ν_c.

任意absolute log(J_A/ν_c)在f′(1−c′)−f′(r)中取消，purecap≤d_i(1−c′−r)；terminalangular同因子，所以remainingproblem属于C(d_i)。这不要求ν_c/J_A等于n(c′)，亦不要求n′(0)∼1。

只在remaining terminal取truechild。oldchild incidence/time floor按2.13 lift为

    m_old/(q_A q_child)≥ν_c n′(1−c′)J_child/K₀
                         =n(1)J_AJ_child/K₀,

所以原terminaltruefloor恢复；ν_c恰相消，无需parenttruefloor。CRP composition/known-atlas normalization给H(E_i)≤h_A,i+k(d_i)(1−c′)，与§9 gap矛盾。由每fixedi有限样本排除，actualatlas不可能；故globalℓ≠∞，原Prop10.1通过这一完整链。

## 17. 独立反攻、范围及阶段退出

反攻已逐步支付：µ_act的tagmark不要求逐原trajectorymark；common jitter固定后旧labelfloors不自动继承；center normal/截距/velocity均入C标签；C-worldabsoluteprofiles可巨大而终端比值真抵消；Q₁ witnesses在A条件化前冻结；cap与occupiedsupport独立，timeerror先抵消g₁才除tinywidth；badposterior pairs只在globalbudget选denseA后归一；greedyfullcoverage由every-residual而非单次成功；originalfailure先检验finalselectedtests；最后ν_c不同于ν_A且无parentfloor。全部保持原trajectory/marks与可测性/tempered上下文，不把toy反例冒原反证。

当前未发现保原全部假设的counter。经两正式全稿独审通过后登记UNB-001为来源已有Prop10.1及shared8.2内部复现；未经外部同行评审。它不直接给R5>4/R6无条件17/4；SRC/DIR/FSD/DIM仅可增加partialgateway，仍余正finiteℓ约§7–9、原2.17/finite读出、新原GWZ/具名KT等明确责任。完成此阶段后必须重列这些余责与高维价值，不能自动逐节续页；常规下一macroR39，gap/两轮无信息提前。
