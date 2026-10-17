# R0033：critical paths 整合稿独立量词审查

2026-10-17，A / audit_four_dimensional。实际逐式读取 root `notes/10_source_audit/critical_paths/R0033_critical_paths_full_proof.md` §§1–11（148行含末空行），并对照原OAI4 2.7/2.13、2.15/2.16、4.1–4.3（PDF11–20、47–50），原 GWZ2026 v2 Theorem1.1 的声明及 companion `05-inputs.tex` 接口。A 的独立极值证明另存 `R0033_extremal_and_narrowness_audit.md`，不以审自己稿代替root全稿独审。

**审查结论：通过。** 未发现必须修改的数学缺口。通过以具名 GWZ2026 Theorem1.1 的三维 convex-clustering 集合估计为高级输入；本轮未独立重证该输入，也不调用或认证 companion 整个三维 maximal theorem。以下审查同时覆盖root §§5–6的有限构造，非只复核A自己负责的极值段。范围仅原version1/j1、version2/j2的原4.3，不是高维新结果或全文OAI4认证。

## 1. 原law、coarsening与normalization

root §2的angular coarsening正确保旧pure denominator：fine good numerators先求和，再除coarse pure。bad density支配good的states用2∫bad计质量，其余以2good控制；后续inverse-subpower restriction用2.3付分母降低。只承诺实际sampled entries的typical cap，不取未删所有bins的免费maximum。原joint-law table实现与先前TEX审查一致。

§3中Z=Σωqν_c与newworldweight ωqν_c/Z各有正确用途。newworld selected law除qν_c，而base Jacobian为qJ_c，因此within-world factor恰J_c/ν_c；ω/Z或额外q均没有混进(N1)。newweighted异常成本乘Z^{-1}≤K，仍power-small。轻chart删除有polynomial count和prior upper；conditioning保持piecewise-constant density/semialgebraic pieces，v1 nonlinear triangular subtraction的Jacobian常数，v2保w/native P_parent/a_r及正确B′。

terminal equality依旧pL-known label；earlier只有upper，除非label已知pr。profile inequality的方向正确：earlier density upper给earlier exponent lower，故remaining terminal-minus-earlier profile cap不增。newangularbin经D_c/q送入旧radiusK N^{-u}球，∥D_c∥≤Kq足以支付，不需额外inverse norm bound。

## 2. True floors、parent history与实际质量

(L1) `m_cd=qν_c m′_d, q_cd=q q_d, J_cd=J_cJ_d` 无漏因子。terminal true child经terminal-known atlas可lift；intermediate floor必须用(N3) equality，这由prepared true parent的knownpr性质供应。root未把upper误作floor lower。

whole assignment/prior/own selected witnesses逐层保留，child在parent full conditionalprior中定义；final selected path可仅占earlier witness一小部分，earlier floor不被重定义。每次新selected mass在newworld mixture中为inverse-subpower，乘parent归一预算Z后仍inverse-subpower；固定有限层迭代不需逐world质量相等。label histories通过known-parent及transported hidden-grid bounded overlap恢复，finite list乘积仍subpower。

## 3. 具名G→任意positive weights的convex估计

原GWZ Theorem1.1声明：在R3的有限tube set、Δ_max≤δ^{-η_G}、平均shading density≥δ^{η_G}下，union≥δ^{ε_G}Σ|T|。root保此为named input，未从direction-separated-only输入免费推任意convex配置。

root §5先以weighted cap测试K=T_i得v_i=ω_i/A≤1，测试bounded ambient得S=Σv_i≤Cδ^{-2}。S≤Clog时逐点multiplicity≤AS已经给weighted estimate。否则Bernoulli(v_i)抽样：每个含unitδtube的convex K截boundedball后，John ellipsoid给comparable-volume enclosing box，各axis≥cδ；cδ²的center/frame/axis finite net加微放大可统一包住它，数目δ^{-C}。

各net box的期望count≤C|Q|/δ²，指数矩法取Clog倍阈值同时控所有boxes；因含unitδtube的box体积≥cδ²，union bound有效。large S时Chernoff同时保sampletotal≥S/2。固定这一样本，exact重复tube的count≤Clog，由cap测试其自身得到；保一actualindex的原shading后distinct数≥cS/log。每index原density lower仍在，故可调用G。这里没有把不同重复indices的shadings任意合并后声称原density。

取G目标ε/2并令输入mark-density exponent小于其η_G，logarithmic clustering/count损失被余下ε/2吸收，得到 `Σω_i|Y_i|≤Cε Aδ^{-ε}|∪Y_i|`。此有限推导不依index总数上界；它使用逐indexdensity，不能直接换成任意average density前提。

## 4. Fulltime plank的convex转换与marks

每个bounded graph trace放入共同fixed-length/radiusCδ tube并留endcap余量，之后共同constant rescale归unit。若convexK含这些tubes，其John enlargement的time diameter≥1。ellipsoid水平slice centers随time affine，section axes固定，maximal section area≤C|K|，所以存在包含这些fulltime traces的moving spatial rectangle，area≤C|K|、widths≥cδ。输入plank cap因此给weightedconvex cap≤CAδ^{-2}|K|。

fixed enlargement只改变constants：可将endpoint坐标分fixedmanyparts，再线性插值，避免偷改原permitted plank convention。每marked timebin center放radiuscδ ball，同index time间隔δ保证disjoint；shadingvolume∼#J_iδ³，union≤C#E_visδ³。因此weightedconvex估计约去δ³，恰得原2.15。没有direction separation或逐管AD lower的附加假设。

continuousprior先细round coefficients，再按roundedtrace及finite markset分组，各组weight原prior总量；family虽可很大但finite且引理常数不依其基数。固定enlargement覆盖回原trace，未免费改变marks或prior。

## 5. 2.16的真实greedy构造

q∼aL分组由midpoint y/X确定，原native X quadratic系数subpower，故wholeqblock小值；pL当前X的Taylor误差O(KaL)，加X沿q变化给group subpower list。所用test v1 w−b_G / v2 P_*−b_G保持原model与derivative/curvature。空间normalize J0=(Rq)^j后，raw group law不除m_G；density factor为J0，非额外q或group-normalization。

greedy门槛 `N^{-ξ}n(L)J0 Πr_i` 恰是oldJacobian的true floor；每positive step有reciprocal-polynomial mass，故polynomial steps。wholecontained available trajectories删除使assignments互斥；center选一containedtrace与fixed enlargement，系数/control保持tempered。

若未cover一半globalmass，先用原joint flattening/known-group lower去低whole-cell witness异常，再按原Σωqν预算删marked duration太小的trajectory-block entries。剩余仍inverse-subpower，每usedtrace的normalizedmarkduration≥1/K；weighted averaging选一个residual mass≥m_G/K的group，m_G是原group selectedmass，非currentcell floor。

被residual访问的每goodcell，其**原whole-cell witnessmass**≥N^{-ξ/4}n(L)J0ρ^{j+1}。cells disjoint，因此count≤m_G除该量。与rawweightedmarkcount≥m_Gρ^{-1}/K相比，2.15给某fulltimeplank的weight/area≥K^{-1}N^{-ξ/4}ρ^ε n(L)J0。再用逐usedtrace duration≥1/K，转成currentincidencemass/area；m_G取消，未假currentresidualcell仍饱和。

## 6. j1 padding、尺度选择与subpower diagonal

给j1 trace独立static z∈[0,1]，prior仍product、marks相同，visitedcells最多乘Cρ^{-1}；于是同二维质量比适用。rotatedrectangle的horizontal projection width W、area∼uv，其任意verticalsection≤Cuv/W：写W=u|cosθ|+v|sinθ|，最大chord≤min(u/|sinθ|,v/|cosθ|)，分主导项即可证。每原trace接受dummyfraction至多此值，故project回来的originalweight/W至少paddedweight/(Cuv)。projected interval仍fulltime，duration lower没改变。

ρ=N^{-D}中D可依原tempered complexity但对fixedξ<1可固定足够大。先fixξ，再取ε使Dε<ξ/4；used duration inverse-subpower对每fixedε最终满足2.15长marks阈值。所得质量密度严格超过greedy stopping threshold，矛盾。ξ↓0只在各fixedξ估计成立后慢增加要求；stepcount/degree/reciprocalwidth的polynomial bounds可uniform取ξ<1，所以输出仍原exact sequence tempered，而不是只固定正幂floor。由此H(E)≤L在具名G下已付。

## 7. Composition与positive k的非循环使用

root §7第一式只lift terminal child，因此terminal-known parent足够。第二式的outercoarsening若需要C(dbar)，另核其terminalcap；本身可用original E∈C(d)保remaining class，不要求outer同属C(d)。H的infimum允许subsequences/restrictions，故逐tolerance取competitor无需attainment。

TEX的e在每fixedbad E内选，h<H(E)+e/4、e<H(E)保证h>e。remaininglength≤Ce且H(F)>3e/4，uniform C在固定d0<1内给k≥3/(4C)>0；upper k≤1来自刚核2.16。没有为了证明k>0先假4.3，亦未要求e对全部outer problems统一。

## 8. Relative profiles：minimizer与coarsened global cap

root §8只compactify g_i=f_i−f_i(0)，1-Lipschitz、[0,1] bounded。若limit有interior低secant，minimizer r_i使r_i−a≥c。对x≥a有terminalcapd″；对x<a的Lipschitz加局部cap使global ratio≤1−(1−d″)c<1。因此Gi真实满足某d_G<1，可在**固定i**调用TEX。

选e<(r_i−a)/C_i保证extended atlas后的remaininginterval全在局部cap有效区。2.13 terminal equality+earlier upper恰能得F∈C(d″)；此处不需earlier equality。其H>0反d*。所以H(Gi)=0，再composition回原E_i反k>0/maximization。d*=0由monotonicity处理。endpointcap与continuity迫唯一linear limit，未假bounded f_i(0)。

## 9. Actual finitegrid、inner/outer顺序

root §9取α_i比profileerror慢趋零，ε_i/α_i→0，故minimizer actual r_i→r。两向H bounds证明coarsened H/r_i→k和remaining H/(1−r_i)→k，均按individual actual length归一。对任意进一步合法restriction，H只会增加，但C(di)的upper仍在，所以squeeze保持maximizing；不必假H严格不变。

有限grid逐段用limitingremainingfraction确定target，但实际normalize/返回cost均用actual length；最后fraction1取whole remaining true terminal，endpoint严格1。prepared true parents供应所有intermediate floor equality，full layers/priors/witnesses与final path分别留存。每fixedi的N-exponents先形成，只作finite次actual subsequences；未把(i,N) diagonal当这些对象的证明。

## 10. Finite/infinite ℓ与最终system upper

root §10的ω允许base序列所有outer子列及各i内部合法competitors，因而finiteℓ先选ω_base≤ℓ+ζ后，后续composed terminal系统仍落其范围。每newmaximizingsequence的ω≥ℓ，从sup取attainable limsup>ℓ−ζ/2并抽子列，得relative段width≥ℓ−ζ；不需sup/inf attained。

time/determinant乘法使narrowness exact add，实际length因子不可省。**最终composed terminal true system**的horizon→k，故其总width limsup≤ω_base；不是将各段自己的ω upper拼接。以该总upper减future段lower得node width≤ℓ actualdepth+2ζ+oi(1)，lower同样成立；increments随之线性。root允许Oζ常数依fixedgrid，合法；也可用complement求和使常数不依grid数。

ℓ=∞只保证sup无界，root已显式对每threshold M选attainable competitor，再取large outer index、保每fixedi内部exact系统，得到width→∞。有限positive-lengthsegments的actual长度最终有正lower，故oldunit增量可任意大。没有假一个fixed exact problem自身实现无限width，也未向vanishing-lengthsegments扩大结论。

## 11. 最终审查边界

本次未提出必须修正项。原4.3完整四项及所需2.7/2.13/4.1/4.2、有限2.15/2.16链在已列高级具名G下可以内部归档。各主稿作者自审不计独审；A已对root完整有限/极值稿实读，自己的audit另由root/B交叉检查。

仍未认证：G全部proof、原后续excluded improvements/finite guards/prepared tangent laws/三个几何排除、完整finite readout及具名KT全部证明。新三篇前沿文献的scope筛选不证明本项目新颖性。六维17/4保持完整OAI4/SRC/DIR/KT条件；无一般或五维满维数结论，未经外部同行评审，不称重大新结果。到此停止本轮编辑。
