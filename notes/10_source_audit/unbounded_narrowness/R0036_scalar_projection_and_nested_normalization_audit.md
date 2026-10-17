# R0036：完整 scalar mesh projection 与 nested normalization

2026-10-17，A独立审计。任务为原Theorem8.2及Prop10.1前端10.1–10.3/10.19；不自动进入§7。已读R36新spec、R35退出/ISO主证明、R29 finite出口；原PDF页118–120、154–160及相关2.8/2.10/2.13/4.3/4.6，文本6309–6479、8255–8615。官方TeX已由root归档为 `literature/primary/openai_4d_source/07-finite-narrowness.tex` 与 `09-unbounded-narrowness.tex`。本稿先独立支付前端，完整Prop10.1须实读root/B后半及正式review才验收。

所有K=N^{o(1)}可增大；fixed powers先声明后慢对角。已发表WZ/CV作为已知具名输入；ISO/GWZ等沿用其明确证书范围，不认证整篇OAI4或无条件高维界。

## 1. Theorem8.2的确切输入与输出

ν为任意概率轨迹law，y=y0+tV标量affine、x=x0+x1t+x2t²标量quadratic，五个coeff有界K；额外坐标/indices可任意相关。原active measure `µ_act≤Kνdt`、总质量≥1/K，不要求逐轨迹AD lower。a=N^{-s}、σ∼N^{-M}，fixed M>s>0；c,c^{-1}有固定多项式界。每(t,y) σ-cell及每宽p=N^{-r}的x-bin，0≤r≤s，raw质量≤Kσ² c p^d，d<1；terminal occupied (σ,σ,a)-cells数≤Kσ^{-2}c^{-1}a^{-d}。相邻网格及null边界按原约定处理。

目标：further subsequence上保dense原µ_act质量，赋disjoint **whole trajectory** labels，有共同scale σ/K≤β≤K，各label有whole-unit-time moving affine interval宽Kβ、whole-unit-time quadratic fit `|x−F(t,y)|≤Ka`、在moving β坐标中normK，以及原active质量≥c a^d β/K。若terminal cap附原V-bin N^{-u}因子KN^{-S1u}（fixed S1,u1>0），则β∼log,N1。没有声明所有逐轨迹marks都保留，也没有把current成功质量当原prior。

terminal support与unit-width cap相乘还说明d≥0：若d<0，p=1 upper与terminal support给总质量≤K a^{-d}，与inverse-subpower质量矛盾。因此后用0≤d<1合法。

## 2. 任意原law到一个合法scalar exact problem

先选五系数tag mesh σ′≪σa²（固定幂buffer），每个原trajectory按五系数rounded vector分tag j，质量ω_j=ν(tag j)。额外坐标保留在原条件prior中，不要求其密度或独立性。tag数量≤N^C；即使ω_j极小，噪声density≤σ^{-5}已是多项式upper，tempered定义不要求每个ω_j inverse-polynomial。若后面形成条件world，则极轻world再按总预算删除。

把time分σ-bins I，令I对j被marked iff `µ_act(j×I)≥ω_jσ/K1`。所有未marked原active质量≤Σ_jΣ_Iω_jσ/K1≤C/K1，故保原dense mass。对每j加**同一产品分布**的五坐标independent uniform jitter u，宽σ，令

`ν_jit=Σ_jω_j δ_j⊗ρ_σ(du)`，`µ_mark=1_{M_j}(t)ν_jit dt`。

这里j是internal trajectory index，不是world；µ_mark为indicator exact law。`µ_act(t∈M_j)≤KΣ_jω_j|M_j|`，故µ_mark总质量dense。noisy trajectories的coeff仍K；piecewise constant五维density≤σ^{-5}，tag/time表polynomial，给合法tempered version1 exact problem，hidden w=x。原额外坐标只在最终回收时恢复，不用伪造其Lebesgue density。

### 2.1 exact-base caps的真实计算

固定(t,y)、宽p≥a的x-bin。任何可贡献jittered tag的原coeff位置在time所在σ-bin I内始终落入一个K倍扩大的原(σ,σ,p)窗口；运动与noise误差均Kσ≪p。因此该tag的整个`µ_act(j×I)`可计入同一扩大窗口。mark threshold给

`Σ_{eligible j}ω_j≤(K1/σ)Σ_jµ_act(j×I)≤Kσ c p^d`。

noisy y-intercept的conditional density≤C/σ，乘起来就是exact-base cap Kc p^d。此证明用整tag×I质量，不假每条原轨迹各自达到mark threshold。

因y-slope noise独立，在给定其他noise后V落入宽ρ interval的概率≤Cmin(1,ρ/σ)；先对y-interceptdensity取upper再对slopenoise积分，得到额外该因子，且没有把fixed-y条件后的slope错误称独立。若原附加terminal角cap，原slope只扩大O(Kσ)≪N^{-u}，相同计算给Kc a^d N^{-S1u}（测试u<M的合法范围）。

任一marked noisy terminal cell距某原active cell至多K个baseσ格/有界个x_a格；噪声x偏移Kσ≪a。因此weighted terminal support measure仍≤Kc^{-1}a^{-d}。这是support上界，不是从cap推cover。

## 3. Profiles、可选角输入与没有角输入时的crop

用已审2.3/2.4的有限counting/tempered实现同质化；取subsequence使C0=lim log_N c。terminal density upper为Kca^d，support upper为K/(ca^d)，dense total mass迫terminal typical density `n(s)∼ca^d`：若density低于ca^d N^{-τ}，该部分总质量≤KN^{-τ}。故

`f(s)=ds−C0`，`f(r)≥dr−C0`，`f(s)−f(r)≤d(s−r)`。

有optional角时已经是C(d) scalar exact problem；角depth取在原u1与M之内，Cor6.9给horizon0。无角时先同质化joint f(r,u)，u≤U=4(M+s+1)。noise gain给

`f(r,u)≥dr−C0+(u−M)_+`。

令R=(1−d)/2，取fixed ε∈(0,1/2)小，最大化 `(1−R)r−f(r,u)+εu` 于[0,s]×[0,U]。在(s,0)值C0+Rs，与upper C0+Rr+εu−(u−M)_+比较，得

`s−r0≤εU/R`，`u0≤M/(1−ε)`，`f(r0,u0)≤f(s,0)+εU`。

取ε使r0>0。U足够大，使u0+r0≤U。最大性分别给

`f(r0,u0)−f(r,u0)≤(1−R)(r0−r)`，
`f(r0,u0+b)−f(r0,u0)≥εb`（0≤b≤r0）。

按(y0,V)的G=N^{-u0} bins作whole-trajectory crops C，prior质量p_C。删除极轻crops、同质化p_C=N^{-α+o(1)}；选出的world prior仍ν_jit(.|C)，world weight为p_C/W，W=Σ_used p_C≥inverse-subpower。全局乘回worldweight后条件prior的p_C分母取消，仅有W^{-1}。不把每个tiny C都单独当常数质量。

减central affine motion并除y坐标G，hidden x不变。给exact(t,y)和旧V_G bin，intercept crop只有O(1)选项，因为y0=y−tV。因此terminal/crop refinement只付K；within-world density乘G/p_C，得到

`f′(r)=f(r,u0)+u0−α`。

在r0 terminal，前述pure差商与joint角增益使cropped exact problem属于C(1−R)，角exponentε；其长度r0>0。额外time/world selections引起的exception总质量按原weights求和，再用2.3重同质化，不从cross-world平均推出逐world density。Cor6.9遂可用于每fixed ε的这份exact sequence。

## 4. 真packets lift的质量、宽度与误差

scalar H=0意味着对每fixed tolerance有exact true systems的time exponents任意小；先取对应successful subsequence，再慢降tolerance/ε。不是在单个有限N凭infimum直接取attaining atlas。设lift到原noisy coordinates后spatial widthβ=Gβ′（optional情形G=1），block q。真floor/2.10提供current active mass，不仅priorfloor；未裁切的full assignments在各block disjoint。

无角crop时每label原单world质量除q至少

`p_C n′(r0) β′/K = β N^{-f(r0,u0)}/K ≥ β c a^d N^{-εU}/K`。

这里p_C与G精确取消，不遗留p_C^{-1}。fit error为N^{-r0}≤a N^{εU/R}。令ε慢趋零、horizon exponents慢趋零并取足够晚样本，可同时得q≥1/K、β≤K、每label质量≥q c a^d β/K与errorKa。optional情形r0=s，无crop直接同结论。full-time assignments可有新complexity，在此finite定理尚不要求以这个慢对角系统直接作原尺度输出；后来回收为有限tag/几何表，实际output另付guard。

### 4.1 β≥σ/K，以及optional β∼1

每packet whole-block y位置约束使V限宽Kβ/q≤Kβ。其graph在exact base只需K个x_a bins；积分area≤Kqβ，pure density与noise factor给active mass upper

`Kqβ c a^d min(1,Kβ/σ)`。

比较true active floor `qβ c a^d/K`，迫β≥σ/K。若optional角存在而β=N^{-b+o(1)}、b>0，取fixed0<u<min(b/2,u1,M)，该V域只需K个N^{-u} bins，upper多N^{-S1u}，与同floor矛盾。因此所有fixed-power β缺陷均排除，慢阈值后β∼log,N1。这里用的是全true packet floor，不能拿后来稀疏的noise slice假新floor。

### 4.2 F norm与whole unit time

packet active质量lower除exact-base densityKca^d，给投影base area≥qβ/K。在(t−t_I)/q、(y−y_c(t))/β单位坐标中为inverse-subpower面积；原x有界K，F与x差Ka，所以|F|≤K在该集合。degree2 polynomial Remez给adapted normK。q≥1/K，故把time伸到[0,1]只付K；每条trajectory的affine位置误差与quadratic scalar-fit误差也可从q-block Remez外推至[0,1]。centermotion由一条实际有界trajectory及q≥1/K得coeffK。没有从fixed-power短block免费外推。

## 5. 固定共同jitter后回原law：per-label floor须重付

先保一个q-block系统，其global marked success仍dense，因为block数≤K。其全部noisy labels的floors与disjoint assignments给

`Σ_labels c a^d β_label≤K`，

包括原crop世界weights与q≥1/K费用。这个是**固定的全label numerator预算**，不是固定noise后仍保每label旧floor的断言。

产品noise分布对所有tag相同，Fubini固定一个共同jitter u，使所选label中`Σ_jω_j dt`的marked success仍dense。同一(j,u)在所选block只有一个label，所以给每个selected原tag赋该label，可保持原trajectory assignments disjoint；对tag内所有原额外坐标保留原ν条件law。不同tag无需独立。

共同jitter的affine/quadratic差为∆y(t)、∆x(t)。给原label换成center y_c−∆y、predictor `F(t,y+∆y(t))−∆x(t)`。β≥σ/K保证原tag rounding的误差 `Kσ′/β≪a`，因为σ′≪σa²；因此full-unit-time interval/fit与adapted norm仍K。此步骤不把原µ_act做卷积，也不需anchor选择正规性。

若某tag-time bin贡献成功，它原来就满足`µ_act(j×I)≥ω_jσ/K1`。现在几何fit已经whole unit time，故可恢复该bin的**全部原active part**，即使bin跨旧block端点也合法；总恢复质量≥先前marked success/K1。这与逐原轨迹各自marked是不同命题，后者未被假设。

fix jitter后各label旧floor可全失效，故最后按`c a^dβ_label/K_cut`删light restored labels；由固定Σ numerator≤K，总损≤K/K_cut，选K_cut更大subpower即可。然后对dyadicβ pigeonhole，宽度范围[σ/K,K]只有O(logN)个尺度，保dense原µ_act且各label新floor成立。得到Theorem8.2全部输出。

Uniform-use量词：若在共同fixed exponent bounds下无uniform subpower选择，则存在fixed-power失败model sequence；取它们各自输入组成exact sequence，按上面homogenization/subsequence又产生subpower输出，矛盾。无需给每model相同显式modulus；也不能先让输入K变成fixed positive power再套此结论。

## 6. 无穷窄度初始normalization与两层真priors

原页154–155/8255–8339。假CRP global ℓ=∞，先经own-depth true intermediate normalization使原Ei length1、n_i(0)∼1。由CRP relative profiles，`f_i(r)→dr` uniformly、d_i→d<1、H(E_i)→k>0。这一步用真实初始node；不声称任意known atlas都令新n′(0)∼1。

native P*沿fulltrajectory boundedX、selected hidden derivative≥B/K0。Lemma2.9使每exact base只有K0个width1/B hidden bins，配zero-depth typical upper得原base density≤K0。先选fixed0<u<η，再选0<s1<s2<1满足 `(d+2k)s2<Su/4`。

在s1与s2的nested maximizing segments用CRP第四项：global inf窄度为∞意味着每个相应maximizing sequence的terminal窄度sup为∞，可选差值α2,i−α1,i→∞。乘正深度长度s2−s1不消散divergence。两层原actual time qj=N0^{-h_j+o(1)}、h_j→ksj，minor ratio gj=N0^{-αj}；保原whole assignments及saturatedpriors

`ν_γ(Qj)∼n_i(rj) qj² gj`。

路径后删不追认这些为current floors。nested composition与largest-axis fullness给D2=D1R、∥R∥≤K0 q2/q1，故同incidence处`|sin angle(n1,n2)|≤K0g1`。normal位置误差≤K0qjgj，endpoint求导误差≤K0gj；center velocity本身K0（|V|≤K0且∥Dj∥≤qjK0）。这些full affine consequences用于下一节。

## 7. Proposition10.2：paired sampling、角预算与full center motion

原页155–156/8347–8427。原world/trajectory prior下t0,t独立uniform，只要求两处当前path event。若path质量p≥K0^{-1}，Jensen给paired质量≥p²；不先按两处成功normalize成独立law。

在t-incidences上先删terminal joint angular坏entries、pure terminal lower坏entries与zero-depth upper坏entries。这些原µ例外乘额外t0的长度≤1，因此总paired成本仍negligible；**在数first labels前删**，不能事后乘其巨大数量。

固定t0、γ。由原full Q2 prior lower及该时block disjointness，first labels数≤`K0/[n_i(r2)q2²g2]`。若两个Q2 normals角大于g2N0^u，它们velocity strips宽K0g2相交在radiusK0N0^{-u}的ball（或为空）。每当前p1(t)实际Q2(t)列表只有K0项，故只需K0个widthN0^{-u/2}旧velocity bins；joint cap给KN0^{-Su/2}乘原pure p1 density。

积分hidden时只在permitted good p0 ancestors内求和：每base有K0个width1/B bins，其totaldensity≤K0；不能把N0^{1}个terminalbins免费逐一乘。固定first Q2的fulltrajectory在整个unit time位于normal widthK0g2、tangent boundedK0的extrapolatedstrip，area≤K0g2。乘first label数，g2取消，故总失败paired质量≤

`K0 N0^{-Su/2}/[n_i(r2)q2²] = N0^{-Su/2+(d+2k)s2+o_i(1)+o_{N0|i}(1)}`。

先i大后N0晚，至多N0^{-Su/4+o(1)}，相对p²为零。平均固定一个t0保inverse-subpower pair success。

给每原轨迹以其Q2(t0)的data分C：unit normal（mod sign）、normal-center intercept、normal-center velocity，三类都分width `g_C=g2N0^{2u}` bins；**不存first Q2身份**。初始t0唯一assignment使C是wholetrajectory标签，合并同bins保持disjoint。其normal position在全unit time误差≤K0g2，加rounding≤K0g_C；tangent宽1upK0，所以给fulltime C geometry，native P*不变。

原p1知识必须恢复center motion：在paired成功点，late normal与early normal差≤K0g2N0^u。两label都贴同一原affine trajectory；分别比较normal intercept与V，再计normal误差乘|y0|+|V|≤K0，得到两套center intercept/velocity差≤K0g2N0^u=o(g_C)。因此lateQ2(t)只容O(1)个C bins，复合其actualK0列表即为原p1的actualC列表。仅normal近parallel而无此center比较不够，原R6 toy不能越过这项假设。

因为g_C/g1=N0^{-(α2−α1)+2u}→很小，n1与n_C误差≤K0g1。用V比较两个中心速度，得`|n_C·(y1′−yC′)|≤K0g1`，即10.8。t0切片、有限bin/angle/geometric tests与原path是tempered；分析density masks只定位成功，不要求作最终谓词。

## 8. Lemma10.3：C-normalized prior与absolute shift取消

原页157–158/8434–8543。空间除C矩阵D_C（det g_C upK0）、时间和hidden w/B/P*都不改。每新world (γ,C) 的prior为ν_γ(.|C)，world weight为`ω_γν_γ(C)/W`，`W=Σω_γν_γ(C)∈[K0^{-1},1]`。乘回worldweight精确恢复原restrictedν/W；不把tiny C条件law误当原probability。

C在原p1已知，故terminal density equality由2.13为

`n′_i(1)∼n_i(1) g_C/ν_γ(C)`。

intermediate只用upper：homogenize g_C/ν(C)=N0^{t_i+o(1)}，则`f′_i(1)=f_i(1)−t_i`，`f′_i(r)≥f_i(r)−t_i`，从而`f′_i(1)−f′_i(r)≤d_i(1−r)`。newvelocity球经D_C映成oldradius≤K0倍的ball，terminal joint cap在同density因子下继承。于是新E′_i∈C(d_i)，但其f′_i(0)可能很大，**未假n′_i(0)∼1**。

任何E′ true terminal system lift回原Ei仍true：仅terminal equality正好取消ν(C)与g_C。故`H(E_i)≤H(E′_i)≤k(d_i)`；两端都→k，E′_i也是maximizing。其**relative** profiles线性，无需控制absolute f′(0)。

对b=1/m先令i足够大使relativeprofile在b,1误差≤1/m；再用coarsening的universal H≤L给depth-b true systems，horizon≤b+1/m。不要求length-b coarsened问题还在C(d_i)。慢取m(i)→∞，bi→0、q_A的timeexponent h_A,i→0。饱和A′后原priors/行列式满足

`ν_γ(A)/ν_γ(C)∼n′_i(b_i)·J_A/g_C`。

代terminal equality得到

`ν_γ(A)/J_A∼ n_i(1)·n′_i(b_i)/n′_i(1)`。

log_N0指数为`−f_i(1)+f′_i(1)−f′_i(b_i)=−d b_i+o_i(1)`。absolute t_i彻底消掉；这就是10.12。它是two-limit结论，不是每fixed-i实际subpower比值。分析diagonal可把该比值并入K=N^{o(1)}；输出不能直接把它当K0。

同一original预算`Σ_{γ,I,A}ω_γq_Aν_γ(A)≤1`来自每block assignments disjoint；之后conditional success低者只能按此global预算删，不要求每tiny A中的exception都小。C-stage的W^{-1}为actualsubpower，A-stage的fullν(A)保持为frozenprior，不随µ_res更新。

## 9. 原p1知识、largest-axis与10.19

给原p1，先actual列表C；存储的invertible affine map恢复primed exactbase，old hidden widthN0^{-1}/B bin决定coarserN0^{-bi}/B bin至≤2项，再复合A′ own-depth列表。A-label list≤2L_C L_A′=N0^{o(1)}，独立于巨大absolute density shift。

composition给`∥D_A^T n_C∥≤K0g_Cq_A`及∥D_A∥≤K0q_A。若tangent分量`∥D_A^T e_Z∥/q_A≤N0^{-ε}`占subpower mass，则每A的endpoint约束将原V放入radiusK0(N0^{-ε}+g_C)球。取fixed angulardepth v<ε,η且小于g_C的fixed小幂，原p1 actualA-list只需K0对应bins；先删angular/pure异常再积分，得到K0N0^{-Sv}总mass，反retained subpower质量。故homogenize可得`∥D_A^T e_Z∥≥q_A/K0`。仍不把currentselectedµ_A当新truefloor。

下一实际output是depth c′的known atlas c=(A,b)，**不需要新truefloor**。其完整assigned prior记ν_c，通常不等于ν(A)；不得把先前JA/ν(A)的balance追认给ν_c。2.13的new-world权重是原`ω_γ q_Aν_c`再除其global总和，within-world density因子为`J_A/ν_c`（time Jacobian q_A与active-law归一化中的q_A抵消）。terminal p1已知给 `n_c^{new}(1−c′)∼n_i(1)J_A/ν_c`，intermediate只给 `n_c^{new}(r)≤K0 n_i(c′+r)J_A/ν_c`；即使该比值有巨大absolute exponent，terminal–intermediate差仍继承C(d_i)。若其timeexponent h_A,i<kc′/2，则4.1的composition给

`H(E_i)≤kc′/2+k(d_i)(1−c′)→k−kc′/2<k`。

这就是10.19；没有从n′(0)密度或everyintermediate true saturation推它。fixed c′的选择先于outer diagonal：d<d0<1、ASM tolerance ε*、θ、ε、matching指数C_match先定，再取δ<min(θs1/4,εs1/(2C_match))、c′=θs1/2。i晚到h_A,i<kc′/2、density-ratioerrors足够小；再在fixed-i exact subsequence取N0晚样本。

finite-sample exclusion的合法版本是：固定i和任何事先声明的finite complexity bound，以及actual `(Kpath logN0)^R` 列表/几何slacks、mass≥ppath/logN0，若无限多N0有此output，便给一个uniformly tempered exact known atlas反10.19。因此可在chosenbound的排除区任意晚采样。bound必须罩住本轮后半全部有限几何操作，且先于N0；不能在看见拟合曲线或S0后再抬bound，不能把tangentK直接当actualKpath幂。4.6的证明依据已审，后半是否实际给这样的统一bounds还要root/B全文审查。

## 10. 本稿结论及待完整分支验收

Theorem8.2的finite arbitrary-prior/extra-coordinate/commonjitter/角可选/全时间/per-label原active质量输出，和10.2/10.3的fulltime中心知识、原nestedpriors与absolute-shift cancellation，以上给出完整推导；未找到保其原hypotheses的counter。重点修复说明是：fix jitter不保旧逐label floor，必须用原全label预算最后重付；只有normal共线不够，必须恢复center的两affine coefficients；ν_A/J_A只在two-limit中subpower。

这还未独自认证Prop10.1全branch。剩余本轮责任是10.4/10.5 stable native graphs与投影caps/support、固定µ_prep下每residual candidate、greedycoverage、Cor3.4原posterior/rawπ/representatives、selectedtests-failure与4.12实际表/guard。收到root/B完成稿后须实读全稿正式独审，不能以本前端通过代替完整目标；n≥5/general Goal与fullsource flags均保持。
