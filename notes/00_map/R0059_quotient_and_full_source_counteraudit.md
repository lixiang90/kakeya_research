# R0059：共同核商族的原质量与全源反攻审计

2026-10-17，B。已读GOAL／STATE／ROADMAP／registry78状态、R58 round／next及R59先写spec6／macro6，重读WZ原Definitions3.3、17.2–17.4与19.2。本稿先记录phase I实际核验，不预称商族提取、完整common-kernel或普通高维结论。只编辑assigned文件，不Git／spawn。未经外部同行评审。

## 1. 当前候选与原几何

原d=5、k=ell=3完整配置，κ≥ζ>0、γ>0先固定，η足够小、δ后足够小；f(t)=F0+u(t)eᵀ。作一个共同bounded可逆线性变换后可取e=e1、F0=0，物理坐标为(x1,x2,y1,y2,t)，grain方向是(1,0,u(t),0)与固定kernel方向(0,1,0,0)。原管方向是

    (φ1,φ2, ξ_p+u(t)φ1, 1)。                         (1)

删除x2保原clock，所有原管仍投为R4整直管。候选要求保subpower原访问／原labels质量并提取joint3-AD商族，且密度、union亏损及mesh没有失效；这不是只需一个CW upper的命题。X_(y,t)只保δ^η-full二维占据，不是自动完整kernel直积；ξ_p可依x2，原coherence只给物理邻点的O(r)振幅上界，没有字面kernel常性。

## 2. 已付上界的正确方向：不作为本轮新成果

本节在一个共同bounded joint-parameter chart内讨论原uniform管概率；若用有界双边权，明确另付domination费用。一个商参数r-ball中的整管，其R4投影都在同一Cr-tube中。恢复bounded x2范围得到R5凸棱柱，三条短空间轴宽O(r)，另两轴长O(1)，体积O(r³)。原whole-CW因此给

    μ{T:quotient(T)∈B_r} ≤ K^C r³。                  (2)

这是3-Frostman upper，不是joint3-AD。结合原joint4-AD lower、packing和原总card≈K^(±C)δ⁻⁴，落在该商r-bin中的occupied lifted r-bins数至多K^C/r。故“证明invisible fibre最多一维”已经由原CW付出；只再证明这个不接近缺失lower。本人phase I首次消息曾漏用凸棱柱约束，把一般线性投影的2-upper当作当前唯一上界，已在施工前纠正，不把它写入成果。

真正尚缺的是商占用格的lower≈K⁻C r³，或全support upper N_r≤K^C r⁻³；按原AD4比较，这要求典型invisible fibre至少有K⁻C/r个r-bins。原CW只给相反不等式。(2)仅迫N_r≥K⁻C r⁻³，不能把这个方向倒过来。平均质量／逐管marks和各scale同时lower还须分别核验。

## 3. κ=γ=0边界校准：全源形状仍可投成joint4维

以下只是被spec排除的边界校准，不能反κ≥ζ、η≪γ的主候选。取固定小c>0，f=0；Z为[-c,c]的δ网，Y_t为[-c,c]²的δ网，X_(y,t)为[-c,c]²的δ网。对b=(b1,b2,b3,b4)取固定bounded四维满δ网（前两坐标范围[-c,c]、后两取更宽固定范围），令整管轴为

    T_b(t)=(b1,b2,b3+t b1,b4+t b2,t)，t∈[-1,1]。

在E的每个原点p取ξ_p=(x1,x2)、Φ_p={(0,0)}，即可由相应b的原管见证。整T的joint参数是b的uniform bi-Lipschitz像，故4-AD；ξ Lipschitz、全grain、Y的2-AD与exponent1的tube-KT、所有粗尺度coherence均成立。κ=0、γ=0处singleton Φ的要求是合法边界。原shading有固定正密度。

CW也有直接证明：对每个固定t，b到空间点(b1,b2,b3+t b1,b4+t b2)的Jacobian为1。先对每个原δ-grid intercept cell作小常数δ-jitter，再积分whole-clock；若原实心δ管含于凸U，足够小jitter的所有中心点都留在U，故所含管的原概率≤C|U|。不只检查轴或单一时刻。

删除x2后，商轴为(b1,b3+t b1,b4+t b2,t)，其截距／斜率参数仍是b的四维线性单射像。因此商support有≈δ⁻⁴个jointδ-bins。任何保原uniform质量≥δ^ε的label子族至少占δ⁻⁴⁺ε个商δ-bins，而bounded-chart joint3-AD常数δ⁻ε容许的总数至多Cδ⁻³⁻ε；ε<1/2时不可能。此例严格排“full grain+coherent ξ在无正κ／γ条件下自动给商3AD”，不反当前正κ／γ目标。

## 4. unused-label并入只排whole-family自动lower，不排原质量提取

还有一个源级条件责任：Def17没有要求整T的每根管都由所选E／Φ_p使用。假定给定一个满足主候选全部正κ／γ条件的配置，在同一bounded chart中并入上一节的4-AD／CW族（必要时先作共同逆shear／rotation）。两个4-AD族之并仍4-AD，常数只固定倍变化；normalized whole-CW同样保留。原E、Y、X、f、Φ、ξ及所有见证完全不变，η可增为固定倍以吸收常数，原允许粗尺度取相应子网。

新增族的商support为四维。因此若声称**全部**T投影不经选择就有小常数3-AD lower，该说法对任何给定的正κ输入也不稳定。此论证没有自行构造未知的正κ全源，故不是一个非空正κ反模型；更不能反保subpower原质量的提取，因为后者可以删去unused族、保留原见证族。原Remark17.1给平均dense shading，不把所有unused tubes免费升级为逐管dense。不能以这个padding论证完成本轮主任务。

## 5. 实际尚未付的coupling及阶段停止

R18原W联合图比删除kernel后的Y图保更多实际信息。记原角差ψ=(θ,ζ)，其精确joint增量是

    ((t−s)θ,(t−s)ζ,−[u(t)−u(s)]θ)                  (3)

（前两项是x-block，后项是二维ξ-block；原误差按既有W尺度付）。kernel的x2仍受ζ作用，ξ增量不含ζ。这一实际关联可能约束kernel方向上的ξ变化，但尚未有保原g质量的估计。不能固定θ后假ζ仍有正维条件law：原Φ可以是斜Cantor graph，满足多方向slab upper而该条件law为原子。也不能只从(3)形式上独立化g、调用R58单D/slab，或补一个未证的fibre-lower公设。

截至phase I没有证明主商族提取，也未给符合κ≥ζ、η≪γ及全straight-line／CW／AD／Φ／ξ条件的反例。root已据spec要求及时宏观重选有实际输入的任务；本稿这些上界／边界／padding只作真实范围审计，不当本轮完整主数学成果。选定后的唯一任务及实际证明将按root追加spec再审，不主动续κ0、kernel toy或旧Y-only／BSG。

## 6. spec§7正式转题：图形–PW联合接口及精确输入

已实际读root追加spec§7与此前已入库Choudhuri arXiv2610.12480v1 §4 Proposition17／Lemma19（本轮不是新PDF）。原文只述R4余维一、whole-tube union；以下独立支付本轮所选n≥5、realdim≤3、任意near-full可测shadings的原质量接口，不把原命题字面扩大。其机制使用原PW的joint空间测试，和R55只要求projected angular cap的失败门槛不同。

固定n、semialgebraic格式A、C、ε>0。S=Sδ⊂B_R⊂R^n为realdim≤3、格式≤A的半代数集，系数可依δ。原N根unit δ-tubes物理方向δ-separated，Y_i⊂T_i任意可测，令E=∪Y_i，Σ|Y_i|≥δ^ηΣ|T_i|。spec原选的是整轴在N_(Cδ)S，以下证明实际只需Y_i⊂N_(Cδ)S；wholeaxis情形自动满足稍大C的这个条件。root终稿已采用此合法加强。不先增加任意weights或全λ³结论。

所需明确图形输入是：S由J≤C_A个半代数pieces Γ_j的闭包覆盖；每piece为某个正交投影π_j:R^n→R³上的**全局**L-Lipschitz图，J、L、图格式均≤C_(A,n)，不依系数／δ。低维pieces的domain可以是R³的低维子集，不要求填满。该全类图形分解不是原R4 Lemma19的字面内容。已实际独读A§§3–5及Pawłucki primary PDF1–3：用切空间coordinate minor／有限图关系、open域regular-cell分解及lower-dimensional递归，补足全n覆盖；对任意RCF成立的定理经compactness统一fixedformat界，不要求系数height。此输入已在本轮付清statement／应用链，Pawłucki wholeproof仍具名，不以它作新增公设冒完整证明。

令H_j=N_(C′δ)Γ_j，C′固定足够大则E⊂∪H_j；wholeaxis选题下整T_i也被覆盖，但下文不需要这一步。全局Lip立即给每个正常纤维的(n−3)-体积

    |H_j∩π_j^−1(z)|_(n−3)≤Cδ^(n−3)。                 (4)

证明：若该fiber非空，任取对应图点(x0,F(x0))；其他图点的x距z为O(δ)，故F(x)距F(x0)为O_L(δ)。正常fiber被一个半径O_L(δ)球覆盖。domain的boundary、非闭性、低维domain均不破这个upper；不把它误称fiber lower。

## 7. 原平均shadings、选chart与非短整轴投影

先保density_i≥δ^η/2的原labels。每管密度≤1，故保留数至少cδ^ηN；逐管Y_i完整保留。对每根保留管，从有限个chart选j(i)使

    |Y_i∩H_(j(i))|≥c_A δ^η δ^(n−1)。                (5)

再固定一个j，使其assigned原labels数N_j≥c_Aδ^ηN。以下Y_i^j=Y_i∩H_j，实际原质量(5)逐管成立；不会先假一个共同短clock内保所有质量。

各管轴的π_j速度有统一lower。对原axis midpoint a与unit方向v_i，用**未clamp**的正交坐标t=v_i·(q−a)，允许范围[-1/2−δ,1/2+δ]；其cross-section面积≤Cδ^(n−1)，所以Y_i^j的t-support直径≥cδ^η。不是把端帽正体积clamp到单个unit轴端点后再用截面积。选两个实际shaded points，其t差ℓ≥cδ^η；对应支持直线点相距ℓv_i、距Γ_j均O(δ)（即使越unit端点O(δ)也一样）。由图形全局Lip，

    |(I−π_j)v_i|ℓ ≤ L|π_jv_i|ℓ+Cδ。

η<1且δ后足够小时，δ/ℓ=o(1)，故|π_jv_i|≥c_L>0。此证明只使用两个原shaded points和全局Lip，没有假shading含interval、没有将非线性图拉直后冒原直线。投影后原整轴长度在[c_L,1]。在一个固定方向chart选主坐标k，使投影方向第k分量≥c；支持线以x_k=0处的两个截距和两个方向参数表示，从这个四维δ网选带余量、固定长度L0的C_Lδ-tube P_i，保π_jT_i⊂P_i且|P_i|≈δ²。L0仅依共同bounded chart。不给纵向center另加δ网；调用GWZ时才共同固定缩放并延长为unit包络。最多固定数方向charts／邻格／端帽包络，费用仅常数；没有改变原straight axis或unitclock，也不需付δ^−a的短clock重缩。

## 8. 原PW传绝对凸浓集并支付重复投影

取任意包含若干P_i的凸U⊂R³。对finite-volume U取包含它的John外接矩形Q，|Q|≤C|U|；无限体积时所求upper平凡。测试

    H_j∩π_j^−1(Q)

具有统一半代数格式（Q任意转向／尺度的系数不改变格式），由(4)体积≤Cδ^(n−3)|U|。若P_i⊂U，则原Y_i^j全部落此test中，故原T_i与test的intersection比例至少c_Aδ^η。对原direction-separated δ-tubes应用具名PW定理，任取小σ>0，有

    # {原assigned i:P_i⊂U}
       ≤C_(A,n,σ) δ^(−2−σ−nη)|U|。                 (6)

PW查询λ=c_Aδ^η≥δ由η<1及δ足小支付。我们使用原Y_i^j作为test中体积的证据；不要求整T_i在单一chart，也不把原半代数S的global体积上界代替这个局部test。

对同一个包络网格label P，其原multiplicity以U=P查询(6)，得到≤Cδ^(−σ−nη)。每个包络选一个assigned原label代表；因(5)逐管成立，任意代表均保原实际shading下界。所得distinct projected族数

    N′≥cδ^(σ+nη)N_j≥cδ^(σ+(n+1)η)N。                (7)

由(6)，该distinct族的绝对Δ_max= sup_U Σ_(P⊂U)|P|/|U|≤Cδ^(−σ−nη)，其中|P|≈δ²。没有将它错认normalized CW≤Cδ^(−σ−nη)／N′，没有假N′≈δ⁻²，也没有为distinct投影重新创造原权。若需essentially distinct，可对固定δ-net的O(1)邻接关系着色后再取一色，仍只常数loss。

## 9. 任意可测shading的真实fiber积分回传

设E_j=E∩H_j，定义R³上的实际函数

    f(z)=δ^(−(n−3))∫_(π_j^−1(z))1_(E_j)。

由(4)，0≤f≤C。Fubini及π_jY_i^j⊂P_i给

    ∫_(P_i) f ≥δ^(−(n−3))|Y_i^j|≥cδ^η δ²。

取统一τ=c_0δ^η，c0足够小。因为f≤C、|P_i|≈δ²，

    |P_i∩{f≥τ}|≥cδ^η|P_i|。                       (8)

故Y′(P_i)=P_i∩{f≥τ}是**真实**δ^η-dense可测shading，union包含于同一level setF={f≥τ}。没有从fiberupper推fiberlower；相反，原Yi质量先推出∫P_i f下界，再用f上界转为level shading。物理回传是

    |E|≥|E_j|=δ^(n−3)∫ f≥δ^(n−3)τ|F|。             (9)

GWZ的B1／unit-axis规范可付：先把共同bounded chart作固定homothety缩入B_(1/4)，此时axes长度为固定ℓ0；再以同center／direction延长包络为unit axes，全部仍在B1。任何新包络含于U仍使旧投影短管含于U，故(6)的原计数upper保持，只变固定chart常数；原shading仍保在新包络，density只付固定ℓ0。没有说homothety本身保unitlength。

以具名GWZ2601.14411v2 Th1.1取目标β>0。选σ、η使σ+nη小于其容许浓集指数，并使cδ^η≥所需dense threshold，则由(7)(8)及绝对Δ_max upper得

    |F|≥cδ^β δ²N′，
    |E|≥cδ^(n−1+β+σ+(n+2)η)N。                     (10)

先取β<ε/3，再取σ同时小于ε/3与GWZ容许参数，最后取η足够小，得本轮目标|E|≥cδ^(n−1+ε)N。PW、GWZ与Pawłucki的wholeproof仍具名；全类图形分解statement／应用已按A／root完整衔接独核。没有把平均δ^η密度升级成全λ统一λ³式。

## 10. 原R55反攻、闭包与最终审查范围

R55 product-parabola近轴族的projected directional bin确可有δ⁻¹重数，所以只调用M3方向分离会失败。本机制不声这种projected angular cap成立；(6)约束的是whole projected tubes的**joint**凸浓集。大量同方向但不同截距的P_i不必在同一个unit δ-tube内，故与(6)不冲突。若实际投影包络重合，则(6)已量化扣掉multiplicity，不把不同原labels悄去重。

初次heavy删选付δ^η原label数，chart选择付常数，包络去重付δ^(σ+nη)，level回传付δ^η；这些均在(10)显式出现。全原clock、任意可测Y、端帽和原物理方向分离都保留。这里未推广任意positiveweights或原direction-bin α；也未认证HRZ某递归叶自动满足全部新输入、或由此得到ordinary H5的固定正幂。phase I的common-kernel提取仍未解，不因这次转题抹去。

本稿主数学链已完成，已实际全文读root12／A10／macro6／next6／spec7，正式独审存research/reviews/R0059_geometry_and_mass_review.md；本稿自审不算独立review。完整图形输入的statement／应用已付，PW／GWZ／Paw wholeproof仍具名。结论不缩成exact、regular或单一canonical例；不续失败的quotient上下界、旧G3方向cap或R58参数。未认证后继递归叶自动满足输入，Goal active。
