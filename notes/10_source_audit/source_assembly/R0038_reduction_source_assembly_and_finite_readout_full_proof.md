# R0038：任意集合归约、原证明拼接与有限/Hausdorff出口

2026-10-17。root整合稿，修后两实际全文独审通过；未经外部同行评审。主要新增审查是原Theorem2.17全部归约及各原证书的精确拼接，不宣称新颖/重大或一般维度已解。原PDF20–25/text1066–1332及proof closing PDF168，官方02-framework.tex exact65440bytes/Gitblob2cb57ede…；有限读出另核R7/R9/R29原稿，不从Hausdorff statement倒推有限定理。独审为research/reviews/R0038_outer_measure_and_horizon_review.md、R0038_assembly_finite_seed_and_input_review.md，root实读两份完整独稿及两正式reviews后整合。

## 1. 量词、固定对象与输出边界

原四维归约：若任意K⊂R4含每方向单位线段且dim_H K<4−σ，0<σ<1，不假可测/紧/可测选线，则有固定0<d<1、Sη>0和tempered homogeneous version2 exact E∈C(d)，每subsequence/后续合法inverse-subpower selection上的terminaltrue horizons均≥σ/6。由已审工具/优化/三几何分支在列明具名输入下反bad E，即得原Theorem1.1的内部argument assembly。

同时证明sourceproof的direction-rich finite读出SRC：每fixedbounded R4graphchart、每σ>0，存在η>0与δ0，使δ-separated方向M≥δ^{-3+η}且逐line time marks≥δ^{-1+η}的family，其visitedδcells不能≤δ^{-4+σ}。这比仅引用dim_H结论多用原归约的finite初始化。后续DIR/FSD/KT是已有明确命题的合法重用，不新立方向。所有新高维/新颖性flag在审查/一手比对前保留条件。

## 2. 具名输入与不循环的依赖次序

G为GWZ arXiv2601.14411v2 Theorem1.1：每β>0存在η_G>0，finite distinct unit δ-tubes在R3满足convex-clustering Δmax<=δ^{-η_G}、平均shadingdensity>=δ^{η_G}时，|unionY|>=δ^βΣ|T|。本轮核其primaryversion/history/本地PDF2 exactstatement；whole49页高级proof与作者报告Lean未本地重跑，显式具名。companion05-inputs.tex只用G→weightedconvexclustering→linechart/fulltimeplank，即原2.15；不是调用companion整个新maximal theorem。

其它高级输入为WZ2210.09581v2 Def4.2/Th5.2 restricted planar dot product、CV1205.6371v1 Th1 determinant multilinear Kakeya、OSS2309.03068v2 Th1.5 single-scale multiplicative Fourier decay，均已核确切statement/application，fulladvancedproof具名。经典固定-iterate Ruzsa/Plünnecke、固定格式QE/semialgebraicchoice/C1decomposition/面积公式等标准基础明列。KT math/0102135v1 Th6.2只在高维出口具名调用，未混入四维源排bad问题的前提。

顺序必须是 G→2.15/2.16、TCM/ASM/TEX→CRP/AIM；先用ISO排version1并给Cor6.9 scalarH0，再供8.2有限接口（UNB）使用；version2在此基础分ell0/positivefinite/infinity，∞用其直接actualatlas论证。不能以v2/8.2预先证明v1，也不以4.11有限ell假设直接排∞。

## 3. 非可测/非紧K的有限选择

固定bounded open graph-slope patch，单位段在time方向有positive projection。每witness含某个rational-endpoint timeinterval、其intercept落某integerbox。countablymany pair的eligible slopes并覆盖整个patch，故outermeasure subadditivity给一个pair的S0正有限outermeasurea。只作fixedaffineclock/spatialchange使共同time=[0,1]、b,s在fixedboundedboxes；不选所有方向的witnessmap。

取dim_H K<4−σ的ballcovers，maxradius→0且Σr_i^{4−σ}<=1。只留meetingbounded graphregion的balls；U_k收2^{-k-1}<r_i<=2^{-k}，ballcount<=C2^{k(4−σ)}。对每eligibleline，Σ_k |{t:line(t)∈U_k}|>=1，故某k的timefraction>=c k^{-2}（cΣk^{-2}<1）。定义S_k为存在这样的boundedwitness的slopes，不要求S_k可测，S0⊂∪S_k。

再由outermeasure同一k有|S_k|*>=c'a k^{-2}，否则sum<c'aΣk^-2<a。该k同时有directionoutermass与逐line成功时长，maxcoverradius→0迫k→∞。令δ=2^{-k}，boundedS_k的maximalδ-separated finite subset覆盖S_k，故c k^{-2}δ^{-3}<=M<=Cδ^{-3}。现在才为这M个slopes逐个选一个成功witness，是有限选择，不需measurableselection。

## 4. smoothing与uniformtempered预算

N0=δ^{-1}、initialL1、nativeP*=w、B1。uniformfinitewitnessmixture，对全部3 intercept/3 slope coordinates独立加cδ-boxnoise。各原coveredtime在所有noise下仍进U_k固定enlargement，rawselectedmass>=c k^{-2}=N0^{-o1}。全time prior独立ν⊗dt，selectedµ=1_Eνdt不归一成功event。

M<=Cδ^-3，piecewiseconstantdensityheights<=Cδ^-6、indexcopies polynomial；unionenlargedballs<=Cδ^{-4+σ}个degree2 predicates，originalbounded ranges，uniformpolynomial exponent。原nonmeasurableK不作predicate，只用finite openballunion；故确为tempered version2。

δ-separated slopecenters有bounded overlap，full3-slope marginaldensity<=C/(Mδ³)<=Ck²<=K0。条件fullslope后的2D y-interceptdensity<=Cδ^-2：每mixturecomponent来自独立interceptnoise，条件componentweights总和1，不假slope/intercept全局独立。

## 5. joint homogenization与三个g界

用原2.3–2.5的jointbaseflattening/finitecelltable及slowgrid homogenize p_r和V_{a_u}，0<=r<=1,0<=u<=4。得到f(r,u)对r单调1-Lipschitz、对u单调2-Lipschitz，n=N0^{-f},m=N0^r n,g=r−f。所有限制保raw upper；inverse-subpower总mass和typicaldensity下界通过2.3再付异常，不能对每稀疏currentworld免费保floor。

(i) 细widthδ时每coverball仅O1 hiddenw bins、base(t,y)volumeOδ³，总observationmeasure<=Cδ^{-4+σ}δ³=Cδ^{σ−1}。selectedmass inverse-subpower及homogeneity迫n(1,0)>=δ^{1−σ}/K0，故g(1,0)>=σ。

(ii) fullvisibleV-density<=K0，故Vbinwidtha_u mass<=K0N0^{-2u}。给fullslope的y(t)-density<=Cδ^-2=N0²，ignorehiddenbin得jointdensity<=K0N0^{2−2u}，因此g(r,u)<=r+2−2u。

(iii) g(0,0)<=0不是单纯density packing结论，需原weightedplank 2.15，下一节支付。fullslopecap既用于此处，又在末尾slopevolume→prior时再次使用，不能删掉后者。

## 6. g(0,0)的raw marks有限化

对任意fineρ=D_m^{-1}，完整projected y-traces全time contained在movingplank的spatialradii aρ,bρ，则endpoint差把V限在同axes宽2aρ,2bρ rectangle，原Vdensity给其priorweight<=K0abρ²。2.15的prefactor A=K0ρ²（不是K0），无方向/各indexlongmarks允许估计Σω_i#J_i<=CεK0ρ^{2−ε}#Evis。

若g00>0，选fixedα>0低于其增益，ρ~N0^{-D}fixedpower足细以2.4jointflattening把typical unit-hiddenbin observationdensitylower转成wholebasecell witnessmass>=N0^αρ³。hiddenw range只有K0个unitbins，visitedbasecells<=K0N0^{-α}ρ^-3。先冻结这些wholecell见证，再作currentduration删选；不能声称residual仍有该floor。

原νdt domination按Σprior1删short integratedduration lines，仅损small inverse-subpower，保mret>=1/K0、每usedline labeled ordinarytime>=1/K0。把其所有positive-durationtimebins标记，Σω_i#J_i>=mret/ρ；移至bincenter只固定enlargebasecells。continuousprior在远细于ρ的coefficientmesh按roundedtrace+finite markset分finiteindices，保原weights/plankcap至fixedconstants，不用counterfamily数量统一有界，2.15constants独立indexcount。

故raw multiplicity >=K0^{-1}N0^αρ²，而2.15upper<=CεK0N0^{Dε}ρ²。先fixD再选ε使Dε<α/2，lateN0矛盾。g00<=0成立；此步仅依具名G导出的原2.15，不依未证高维WP4。

## 7. 正endpoint及角尺度

选fixedR,S>0，R+4S<σ/2且R,S<1/10，max Φ(r,u)=g(r,u)−Rr+Su于[0,1]×[0,4]，continuity由homogenization。Φ(1,0)>=σ−R；r0=0时Φ<=4S，u0=4时g<=r−6令Φ<0，所以maximizer r0>0,u0<4。maximality另给g(r0,u0)>=σ−R−4S>σ/2。

沿r/s比较及沿u比较，分别得

f(r0,u0)−f(s,u0)<=(1−R)(r0−s)，0<=s<=r0；
f(r0,u0+u)−f(r0,u0)>=Su，0<=u<=4−u0。

第二式的正角gain不能由第一式或fulltimeplank口头替代；需要同一个二维jointprofile上的endpoint。

## 8. fulltimecrop的精确density及C(d)

以sidea_u0把(y0,V)分成fulltimeboxes B，newworldprior ν(.|B)，worldweights∝ν(B)。丢extremelylightprior boxes只损power-small（polynomialboxcount）；homogenizepriorweightexponents和successfractions，保globalinverse-subpowermass。减central y_B(t)再除a_u0，w/nativeP*=w/B1不变，time不变，new y,V boundedK0，coordinateJacobian及逆仍polynomial。

在exact(t,y)给oldV_{a_u0}，y0=y−tV限制interceptbin只有boundedchoices，故加B是old(p_s,Vbin)的bounded-list refinement。old未归一raw densityρ_B(s)运输后严格为 ρ_new,B(s)=a_u0²ρ_B(s)/ν(B)。roundedgrid boundedoverlap与2.3给 n_new(s)~n(s,u0)a_u0²/ν(B)，newangularu对应old u0+u，同一within-worldfactor取消。worldweightnormalizer Z只在总mixture，不在这个densityformula。

L=r0、d=1−R∈(0,1)，firstendpointinequality给C(d)terminalhiddencap；second给terminaljointangularcap n_new(L)N0^{-Su+o1}，取η=(4−u0)/(2r0)>0，u<=ηL有room。没有将当前成功probability换成trajectoryprior，也不假每newworld和原world同mass。

## 9. 每terminaltrue system的原priorfloor

任意后续合法selection/subsequence再出的true terminalchart c，lengthq、newspatialJacobianJ_new，wholeassignedprior可只部分lines成功但selectedm_c/q>=n_new(r0)J_new/K0。由于2.3典型exponent在inverse-subpower限制下保持，n_new公式仍可用于该system（重新丢power-small异常）。设J_phys=a_u0²J_new，原未归一selectedmass m_old=ν(B)m_new。于是

m_old/q >= n(r0,u0)J_phys/K0 = m(r0,u0)a_r0 J_phys/K0。

tinyν(B)精确抵消。原priorof贡献正selectedtime的trajectories>=m_old/q（每line总time<=q）；这些line在全block满足spatial/value/upperderivative，且至少某时|P_w|>=1/K0。原B1未改，P变回original(t,y,w)仍degree2。这里下界来自真正truechartfloor，knownatlas无该floor，不能直接代用。

## 10. Σ的固定格式geometry、choice及regularmultiplicity

固定此chart，用bounded原3D slope s定义Σ：存在boundedinterceptb使全I上 |D_phys^{-1}(y−y_c)|<=K0、|P(t,b+ts)|<=K0 a_r0、sup|P_w|<=K0且sup|P_w|>=1/K0。Σ只放这些固定数目的degree-bounded geometricconditions；不加cropmembership、finitewitnessindex、densityselection或原K成员测试。因此Σ包含所有贡献轨迹slopes且是fixed-format semialgebraic set，虽然原K可非可测。

parameter-uniform QE/semialgebraicchoice/C1decomposition给eligibleb(s)，graph与finite C1pieces格式统一有界，不依q^{-1}或P数值系数大小；full-dimensionalopenpieces覆盖Σ除nullset。F_t(s)=b(s)+ts在每piece局部C1，Jacobian det(Db(s)+tI_3)为moniccubic。

fixedt/targetpoint的fiber有uniformboundedsemialgebraicconnectedcomponents；nonzeroJacobianpreimage在其openpiece内localinverse故isolated，是该piecefiber单独component。finitepieces总数uniform，因此regularmultiplicity<=C_uniform，不是N0^C。无需Db幅度界。面积公式可先在各C1piece上compact exhaustion的locallyLipschitzpatch应用，再monotone limit，避免假全局Lipschitz。

## 11. 共同goodtimes与slopevolume

对fixeds，在I去掉moniccubic三个complexroots之realparts周围radiuscq区间，lostlength<=6cq；其余|det|>=c³q³。g_s(t)=P_w(t,b(s)+ts)为real affine、M=sup_I|g_s|>=1/K0。若variation<M/2则|g_s|>=M/2；否则slope>=M/(2q)，故{|g_s|<ε/K0} length<=4εq。取fixedc,ε使各badlength<=q/4，不假independence，jointgoodtime每s至少q/2。

设Σ_t为passingboth的slopes，∫_I|Σ_t|dt>=q|Σ|/2。uniformregularmultiplicity与areaformula给

q⁴|Σ| ≲ q³∫|Σ_t|dt ≲ ∫|F_t(Σ_t)|dt。

image空间中allowed y-area<=K0J_phys，fixed(t,y)的quadraticP在|P|<=K0 a_r0、|P_w|>=ε/K0处总w-length<=K0 a_r0（原2.9：有限monotonepieces及导数lower，至多degree常数）。所以右侧<=K0 q J_phys a_r0。除q⁴得 |Σ|<=K0 a_r0 J_phys/q³。goodJacobianq³再timeq产生q⁴，不能漏其中一项。

## 12. H>=σ/6对所有合法selection

原full3-slopedensity<=K0将eligibleprior upper压成K0|Σ|，无需对intercept重新选prior。与§9 originalfloor比较，cancel a_r0 J_phys>0，得 m(r0,u0)<=K0q^-3。g(r0,u0)>=σ/2，q=N0^{-h+o1}故3h>=σ/2，h>=σ/6。

每合法terminaltrue system都满足同geometry/originalν上界与transportedfloor；后续analytic selection只减旧rawnumerator，homogeneousexponents通过2.3/实际tempered表在其inverse-subpowermass上仍有效。故该bound含所有subsequences/allowed selections的horizon competitors，取inf仍H(E)>=σ/6>0。没有只证明某一个chosenatlas的time短，也没把有限样本当continuous areaformula。

## 13. 原工具/critical/actual接口的完整拼接

TCM001给原3.3一般fixedorder、arbitraryπ/相关events的two-colormatching；ASM001给3.1noheightlower norm/jet、独立3.2continuation、完整Cor3.4原π/Fubini/R0uniformepsilon，Cor3.4不循环调用3.2。TEX001给原3.5两model terminalextension、oldpL-known/wholeassignments/tempered及列明2.x基础，无额外newfloor/j3。

CRP001从G经2.15/2.16得H/L<=1，再TEX+composition于任何badclass给positivecritical k>0；故不存在被遗漏的k0 badalternative。允许d*=0，已按monotonicity另处理；k=1仍在工具范围。relativeprofile只f(r)−f(0)compact，所有normalizationsdensity为J/ν（无ω/Z）；terminalknownparent只付terminaltrue lifting，中间floor需preparedknownpr。fixedfinitegrid的actualnestedtrue systems保每层ownwholewitness，不假finalpath仍saturate祖先floor。

criticalsupinf无需attained，fixedi先innerexactN0极限再outeri，finite/∞ℓ亦同顺序。AIM001在finiteell setup把every-subsequence/every-substantialresidual propercandidates转成原actualknownatlas，success>p_path/logN0、lists/geometry (Kpath logN0)^C、预声明complexityguard2^((Mpath+n)^2)。先wholepriorityassignment再删derivativebadtime，µprep乘回p_prep、finalselected-testfailure不进posteriorlist、TV表用原observations，原guard晚N0在scenario固定后核。analysisK不冒actualslack，不能只因tangentgain正就忽略此接口。

## 14. version1先闭合、scalarH0再供投影

若version1某C(d)有badproblem，CRP给0<k<=1 maximizingtangent，v1 formalell0。ISO001完整6.1在每substantialresidual构造properdegree2candidate、mass hν_Q(a2/a)^d/K、gain e2ks正有限；AIM转换反criticalpath，故原Cor6.9对所有version1 C(d<1)有H0。这里用的matchedquadratic scalar model允许w沿line二次，符合version1，不错当原R4 affinew。

UNB001原8.2的scalar mesh projection使用这一Cor6.9、arbitraryrawactiveµ<=Kνdt和extra correlatedcoords、完整meshcaps/terminalsupport；其wholejitter/crop/floor重付的finite接口已审。没有从v2全source正确性推出8.2后再循环用8.2证明v2。

## 15. version2所有narrowness与actual出口

badversion2经CRP优化globalell∈[0,∞]。ell0由ISO001同一原模型给candidate、AIM反优化。0<ell<∞由FIN001完整7–9：retained原edges/OSSflatcoeff/collision/row、threewideimprovement或horizontal k=ell，2k=1 critical同law三switch、2k<1 G(u)每denseinput及真实endpoint、2k>1直接offcritical，各自properwholeblockcandidate和原qνmass全付，再AIMactualcontradiction。k=1可进supercritical，k=1/2有专门分支，未漏边界。

ell∞不满足4.11finiteell前提，故用UNB001原Prop10.1直接nestedQ1/Q2/fullcenter-motion/relativeν_A/J_A cancellation→每residualscalarprojection/greedy固定fractioncoverage→originalp1-known positive-depthactualatlas，timeexponent→0。原4.12recovery/actualguards引用只是通用编码，不以4.11finiteell假设偷排∞。newlabel c=(A,b)的完整ν_c不是ν_A，terminalcompletion密度ratio因子抵消恢复truechild，反positivek。全三类都被排除，原2.17bad E矛盾。

这给原Theorem1.1 argument在所列named高级输入/标准基础下的完整内部assembly；不是重证每一份外部高级proof，也不认证原§11所有曲线/方向推论。原任意K集合结论dim_H=4依此链，不借compactness。

## 16. SRC finite读出：η→0反证而非dim_H→finite口号

假某fixedσ>0的finite命题对所有η和所有小尺度threshold都失败。选η_j↓0、δ_j↓0 counterfamilies，M_j>=δ_j^{-3+η_j}、每line marks>=δ_j^{-1+η_j}、#visitedcells<=δ_j^{-4+σ}。固定graphchart有M_j<=Cδ_j^-3。取N0=δ_j^-1，uniformlines，六coefficient cδ_j-independentnoise；在原markedcellunion的fixedenlargement选incidences。

每marktimecenter可取cδ_j neighborhood（端点clip只fixedfactor），原lineboundedvelocity、noiseOδ_j使这些timepoints仍进enlargement，同line这些intervals可选disjoint或boundedoverlap。故selectedmass>=cδ_j^{η_j}=N0^{-o1}；不要求marks均匀于time。fullslopedensity<=C/(M_jδ_j³)<=Cδ_j^{-η_j}=N0^{o1}，conditionaly-interceptdensity<=Cδ_j^-2，temperedindexcount<=Cδ_j^-3、incidencecellpredicates<=Cδ_j^-4，统一polynomialformat，不让complexityexponent随j发散。

support观测measure<=C#E δ_j³<=Cδ_j^{σ−1}，故同g10>=σ。§§5–12其余步骤从这些finite/data bounds开始，与固定跨scale K无关；产生C(1−R)badproblem，§§13–15反它。于是存在真正η_src(σ,R)>0和δ0。没有声称线性η(σ)、explicit modulus、uniformtangent绝对高度或任意convex-clusteredWP4。固定constants/δ-grids用σ余量吸收；σ>=1时先证更小的正σ即可。

## 17. 稀疏放大与任意权重DIR出口（复用R9）

任意M separatedslopes在boundedR3 chart，U=∪B(v_i,cδ)有volume~Mδ³。以Kcopy<=C/(Mδ³)独立boundedshift directions，对fixedtargetbox每点被U+shift覆盖概率p~Mδ³；Kcopy使expectedcoveredvolume正，故有确定shifts覆盖正方向体积。maximalCδ-separated实际centers子集有≥cδ^-3，取对应真实shearedlines S_a(t,y)=(t,y+ta)。clock不变、逐line原marks保留，重分Cδ-timegrid只fixedmerging，unioncell数<=CKcopy#E。

调用SRCnear-full给任意稀疏M的#E>=cMδ^{-1+ε_D}，取η_D小于source阈值并留fixedmesh余量。weightedcase每directionδbin总权<=α，fixedfinitecoloring使不同同色bins任意代表均separated。每非空bin选一个原index及自己的marks，unweightedbound控制occupiedbins数；Σω_i#J_i<=δ^-1Σbinweight<=Cαδ^{-ε_D}#E。α任意小、权重跨度/repeatedindices任意，不假weightedprior正则；代表的marks只用于满足lowerthreshold，没被冒充原全部marks。

若实际只给平均marks λ，就必须先heavy筛，不能将平均λ直接视作逐管条件。以上DIR不是无方向WP4，也不使genericj3 horizon自动闭合。

## 18. arbitraryambient、realangulars及λ²成本（复用R29）

固定ambientA>=4、实s>=3，m方向δ-separated，#angleballθ<=K(θ/δ)^s；totalmarks>=λmδ^-1。heavy#Y>=λδ^-1/2的lines数>=cλm。R29 Gaussian4×A投影的paircollisionprob<=Cmin(1,(δ/θ)^3)；dyadicannuli给每line expecteddegree<=C_s Kδ^{3−s}(1+log1/δ)。短projection/大operatornorm事件以fixedconstants排后，independent-set bound给nonshort/separatedprojected族 >=cλm/[Kδ^{3−s}(1+log)]。

每条保自己的>=cλδ^-1 marks；fixed有限directionpatch/commonclock窗与lineextension只删fixedfraction且不添加marks，boundedP使newvisitedcover<=C#E。DIR对projected separated族给

#E >= c λ² m K^{-1} δ^{s−4+ε_D}/(1+log1/δ)。

两个λ分别来自heavyline数量与逐outputline marks，不能漏一个。νmass不在归一化后免费替K消除。给任意targetε，先ε_D小再η<min(η_D/2,ε/16)，K<=δ^-η,λ>=δ^η时3η+ε_D+log成本可吸收，得unsaturated #E>=c mδ^{s−4+ε}。m无需饱和；右边小于1时合法但弱。

## 19. KT实际输入与严格次临界参数

KT Def6.1的K(n,d)容realn,d、fixed arbitraryambient，saturated(n−1)-collection具有全部angularball upper与m≈N^{n−1}，shading是总mass saturated；非逐管unitdensity。§18先heavy再投影正好付平均→逐管闭包，且unsaturated形式为#E>=m N^{4−s−ε}，匹配其(40)因子m/N^{n−1}。

固定0<ζ<1：每realn>=4、s=n−1>=3，target亏损先<ζ/2，之后选择所需inputloss小于sourceη，再以ζ余量吸收有限调用费用，给K(n,4−ζ)。不从∀ε∃η推得η线性或literalendpointK(n,4)的uniformmodulus。ambient若不容此saturated方向family则命题空真，不提供虚假新几何。

具名KT Th6.2：0<d<n，K(n,d)+K(d+1,d')⇒K(n,(2n+1+d')/4)。其第二family在高一ambient，§18的fixed arbitraryambient/realn与unsaturatedweight恰为需要的范围，不能只给R4内满方向集合。取n6,d=d'=4−ζ得到K(6,17/4−ζ/4)，未调用不已付的方向维monotonicity。KT完整6.2proof未在本轮自包含重证；原6.6proof的d−1印刷疑点与statement d-collection/实际使用分开，不以此声称反named6.2。

## 20. finite K到任意集合Hausdorff的直接outermeasure读出

为明确compactness范围，给独立有限cover论证。设integern>=2的KT式finiteK(n,d)成立，且任意K⊂R^n含每方向单位段。若dim_H K<t<d，按§3的rationalclock/interceptbox选positiveoutermeasure slope S0⊂R^{n−1}，先取固定窄directionpatch并用固定affineclock/spatial normalization满足KT的近竖直约定，保fixedboundedchart/linebounds。取Σr_i^t<=1、maxr_i→0的ballcover；U_k的δ=2^-k balls数<=Cδ^-t。

同两次k^-2 pigeonhole（以outermeasure）给某k的directionoutermeasure>=c k^-2且每successfulfinitewitness在U_k ordinarytime>=c k^-2。maximal Cδ-separatedfinite slopes数>=cδ^{-(n−1)}/k²，C取fixedchart逆Lipschitz常数使实际unitdirections δ-separated，angularcap由boundedchart packing<=C(θ/δ)^{n−1}；不靠可测方向选线。timebins见证转换成actualcenterline marks每line>=cδ^-1/k²，移center最多Cδ所以visitedcells<=Cδ^-t。KT离散line是固定ambientball中supportingline的Cδ-neighborhood，共同boundedgraphinterval长~1及marks在该witness内，fixedchart/固定enlarge即可。若采用unit Euclideansegment约定，另可将boundedlength graphsegment分fixednumber单位arclengthwindows并每line保最富窗，逐line只损fixedconstant；两约定均不添加marks到footprint。

此为saturated(n−1)-collection/saturatedshading（polylogloss在任意小幂内）。更明确地，先固定输出loss ε<(d−t)/3，再取finite K对应的输入门槛，最后k足大；方向数、角cap与总shading的polylog亏损都在门槛内，故finite lower至少cδ^{-d+ε}，与#E<=Cδ^-t矛盾。这个读出可付任意非可测/非紧K，不由Minkowski直接推Hausdorff，也没假一个跨尺度measurablewitnessfamily。两实际全文独审另核KT Def5.1/5.2/6.1及39/40，修后Cδ separation、fixedambientball与supportingline约定通过，因此DIM条件scope可由compact扩为任意Euclidean六维Kakeya集合。

## 21. 验收、真实增益与剩余责任

root proof的原2.17是来源归约重证；allcertificate assembly及SRC/DIR/FSD/KT应用是明确具名输入下的依赖拼接，非新方向。§20通过两独审，是同outermeasure机制的标准finite读出，不登记重大引理。六维17/4仍须分别披露高级输入核验状态与2026一手优先权/前沿比对，不能因内部source拼接就称一般猜想已解。

反攻保原source：非measurablewitnessmap、同scale方向/time双选择、mixtureconditionaldensity、g00不付2.15、tinycropworld漏νB、Σ夹原event/index致format随N、Db未界/regularfiber误计、q³/q⁴漏time、仅选一个shortatlas、后selection冒旧floor、scalarH0循环、∞误用finiteAIM、SRC由集合声明倒推、平均marks免费逐管、λ丢一次、fixedambient/realn/unsaturated遗漏、literalKendpointmodulus、Hausdorff从Minkowski冒推。以上各责任明确付或具名保留，两实际全文独审通过；R39先执行宏观审视，正面核实前沿、具名输入状态及下一直接高维机制，不继续细化已付的cubic/crop/ε常数。
