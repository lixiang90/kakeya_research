# R0033：原 critical paths、真实归一化与所需有限初始界

2026-10-17，root主稿。来源OAI4（175页、blob45ec20e…）原2.7、2.13、2.15–2.16、4.1–4.3，PDF11–20/47–50；companion `05-inputs.tex` 前两小节。**CRP-001内部交叉独审通过，未经外部同行评审；完整边界见两份R33正式reviews及rootintegration。** 这是原结果的内部重证，不声明新Kakeya定理、源全文正确或六维无条件新界。GWZ2026 Theorem1.1的三维convex-clustering集合估计保为具名高级输入；没有调用companion整个3D maximal主定理。

## 1. 固定对象、量词与输入

只用原v1/j=1或v2/j=2、固定S,η和原tempered exact problems。选中incidence measure μγ≤νγ⊗dt，world weights ωγ总和1，成功质量inverse-subpower；n(r)=N^{-f(r)+o(1)}为within-world典型密度，f单调1-Lipschitz，绝对f(0)不受统一界。C(d)要求f(L)−f(s)≤d(L−s)，以及(pL,[V]_{N^{-u}}) joint ceiling n(L)N^{-Su+o(1)}，0<u≤ηL；d<1。

原chart c=(γ,I,A_c)有time lengthq、spatial Jacobian J_c=|det D_c|、whole-trajectory assigned prior ν_c=νγ(A_c)，selected mass m_c≤qν_c；每个world/time block的whole assignments互斥。true floor为m_c/q≥K^{-1}n(r)J_c；K=N^{o(1)}，known atlas没有该floor。拟合/测试适用于整段assigned trajectories；selectedincidences才要求原lower derivative。原H为terminal true systems horizon exponent的infimum，含所有合法inverse-subpower restrictions及exact subsequences。

调用已核TCM001/ASM001/TEX001，以及其明确基础2.3/2.4/2.9/2.10/2.12和2.5 homogenization。2.5此处只用原slow finitegrid实施：共同固定polynomial base mesh，density-type lists数量subpower，选有质量list；refinement density比较给Lipschitz，countablegrid慢增加。后续所有finitegrid/slack对每个fixed exact problem内单独选。没有由数值实验替代此步骤。

具名三维输入G：∀ε>0∃η_G,δ_G>0，有限distinct unit δ-tubes若convex clustering Δ_max≤δ^{-η_G}、平均shading density≥δ^{η_G}，则union≥δ^εΣ|T|。这是库中GWZ2026 Theorem1.1的声明；本稿不重证G。下面把它转为原weighted plank并核实际使用，不额外要求3D maximal。

## 2. Angular coarsening：先求和后除旧pure分母

固定b,u和容差τ，剔除fine observation的joint ceiling或pure lower失败的power-small质量。对每个剩余fine bin a、angular bin v，good numerator g_{a,v}≤N^{-Su+O(τ)}g_a，其中右侧是旧pure density，非good density。固定coarse bin B，把其中a求和，得Σ_a g_{a,v}≤N^{-Su+Oτ}Σ_a g_a。连续exactbase可先用共同mesh解释，随后TV回传。这证明相对于旧coarse denominator的good bound。

若新pushforward省略bad density b，good densityg，在b>g的新states中总质量≤2∫b；其它states总density≤2g。删去该power-small集给typical conditional cap。后续inverse-subpower restriction的分母低于旧分母固定幂因子的质量亦power-small（2.3），重新付τ。故cap在所需slow finitegrid上成立，且只在实际sampled angular entry评价；不是unpruned所有bins的pointwise最大值。需要输出时2.4以原jointlaw实现tempered celltable，不能把analytic mask自行当tempered law。

## 3. Chart normalization的精确质量与密度

设terminal-known atlas在r<L。令Z=Σ_cωγ qν_c，则selectedmass M≤Z≤1。新world是c，weight ω'_c=ωγ qν_c/Z，prior νγ(.|A_c)，time τ∈[0,1]，t=t_c+qτ，y=y_c(t)+D_c z。新selected measure是旧assigned selected measure除以qν_c后的pushforward，因此仍≤conditioned prior⊗dτ，其weightedmass=M/Z为inverse-subpower。Z只改变worldweights，不属于within-world density。

丢弃ν_c极小于reciprocalpolynomial的charts：其总质量以原qν_c预算及polynomial chartcount控制为power-small；余下conditional laws保持固定polynomial heights。homogenize J_c、ν_c等exponents。v1设w'=(w−F_parent)/a_r，v2保留w并用P'_* =P_parent/a_r、B'=B/a_r。v1沿trajectory仍quadratic，coefficientmap triangular constantJacobian；v2不把新的native test误认成旧P_*。空间/时间变换及逆的polynomial bounds、tests degree、label count均有原tempered控制。

在固定chart及exactbase，new p'_s的hiddenwidth等于旧a_{r+s}/B，v1 offset依chart/base但网格boundedoverlap。base Jacobian为qJ_c，新productprior分母qν_c，故refined within-world density严格变为

    ρ'_c = (J_c/ν_c) ρ_c.                                      (N1)

不能出现额外ωγ、Z或q。terminal label由pL的subpower list已知，refinement双向density比较给

    n'(L−r) ~log n(L) J_c/ν_c.                                  (N2)
    n'(s) ≤ N^{o(1)} n(r+s) J_c/ν_c, s<L−r.                     (N3)

若parent label已知pr，则也已知更fine p_{r+s}，(N3)是equality up to subpower。否则只可upper：任意labelrefinement能使其raw numerator远小于旧总numerator。2.3/2.4控制异常与knownlist；worldweighted异常另乘Z^{-1}≤K，仍power-small。因而

    f'(L−r)−f'(s) ≤ f(L)−f(r+s) ≤ d(L−r−s).

velocitynewball经V=y'_c+D_cV'/q映为旧radiusK N^{-u}ball；原chart axes≤Kq，只需subpower angular/terminal bins覆盖。对good旧joint numerators先sum，再用(N1)和(N2)，得到同S的n'(L−r)N^{-Su+o(1)} cap，u≤η(L−r)。typical异常同前。故C(d)保持，且固定S,η没被偷偷改成零。

## 4. True lifting、whole layers与narrowness

child chart的相对time q_d、Jacobian J_d、newworld selectedmass m'_d转回旧量：

    q_cd=q q_d, J_cd=J_c J_d, m_cd=qν_c m'_d;
    m_cd/q_cd=ν_c m'_d/q_d.                                    (L1)

terminalchildfloor用(N2)得≥K^{-1}n(L)J_cJ_d，故terminal true child可经仅terminal-known parent提升。intermediatechild要得到n(r+s)J_cJ_d则必须用(N3)的反向；preparedtrueparent由2.10 knownpr使其成立。只引用upper无法支付lowerfloor。

v1 childtest w'−G变回w−F_parent−a_rG，仍原specialquadratic；v2 a_rQ仍degree2、旧derivativescaleB，curvature bound为K B²/a_{r+s}。wholeblocktime/linearspatial transforms compose，childwholeassignment是parentwholeassignment子集；recordlabelhistory，有限层list大小相乘仍subpower。actualpriors在每层保持为parent的完整assignedprior的conditional，**不会在进一步selectedpath上重新归一化prior**。

保留每层自己的fullchart assignments、prior及selected witnesses以证明该层truefloor，同时标记最终各层共同的pathincidences。最终path可以只覆盖earlierchart的一小部分；不声称它自身saturates每层。每次子系统在parentconditionedprior下有inverse-subpower成功，则原worldweighted总成功仍inverse-subpower：之前有总质量/预算支持，finite次pruning/2.3/tempered实施，不能要求每world等质量。父层frozen witnesses并不因这次pruning被重定义。

v2窄度记χ=log_N(q²/J_c)。det乘法而非axesparallel给

    χ_cd=χ_c+χ_d.

relative length-one child的窄度乘实际L_child后才加到旧units。最大轴fullness给nonnegative exponents；没有统一outer上界。j3或通用horizon不在本命题范围。

## 5. 从具名G到weighted full-time plank（原2.15）

先证明weightedconvex形式。令任意positiveweights/repeatedtube indices满足Σ_{T_i⊂K}ω_i|T_i|≤A|K|，每个shading|Y_i|≥δ^{η_in}|T_i|。设vδ~δ²、v_i=ω_i/A。测试K=T_i得v_i≤1，测试ambientball得S=Σv_i≤Cδ^{-2}。若S≲log(1/δ)，pointwise Σω_i1_{Y_i}≤AS已给所需Aδ^{-ε}unionbound。

否则独立Bernoulli(v_i)抽样。任意含tube的convexK截boundedball后，由Johnellipsoid放大得包围boxQ，axes≥cδ且≤C、|Q|≤C|K|。center/frame/axes以cδ²网离散并微放大，全部tests只有δ^{-C}个，仍含K且volume comparable。每Q期望samplecount≤|Q|/vδ；exponentialmoment与unionbound给同时count≤C log(1/δ)|Q|/vδ，概率≥3/4。S≥Clog时sampletotal≥S/2概率≥3/4。两者共同有正概率，固定一次。此样本convexclusteringO(log)；重复同一tube数也O(log)，每tube保任一实际index的原shading，distinct数≥cS/log且逐tube density仍≥δ^{η_in}。

给G目标ε/2，取η_in比其densitytolerance小；logcluster≤δ^{-η_G}最终成立。故union≥cS vδ δ^{ε/2}/log，而Σω_i|Y_i|≤ASvδ，得到Σω_i|Y_i|≤C Aδ^{-ε}union。boundedremainingδ用总权≤CAδ^{-2}吸收。这里原G只需平均density，但抽样后用的是更强的逐indexdensity；任意average shading不能直接冒用这个strongerhypothesis。

现在fulltime traces M_i(t)=b_i+tu_i∈R²，0≤t≤1，weightsω_i，δ=D^{-1}，假每fulltime spatialplank of widths aδ,bδ有Σcontainedω_i≤Aab。允许固定倍宽度：partition端点坐标进fixedphysical bins，linearinterpolation使每part在原permitted plank，只有fixedmanyparts，总area成本comparable。

每trace放入radiusCδ、共同fixedEuclideanlengthtube，留远离endcaps余量。任意convexK含若干这些tubes，截ambientball并John放大成ellipsoid。其time diameter≥1；水平截面有affinecenters、固定主axes、共同scale，最大slice area≤C|K|。沿affinecenters放最大slice外接rectangle是fulltimeplank，spatialwidths≥cδ（tube含每个charttime的水平disk）。所以Σcontainedω_i≤CAδ^{-2}|K|，其weightedconvexclustering≤CA。

在每markedbincenter的tracepoint放radiuscδ球。同index的balls因time间隔δ而disjoint，shadingvolume~#J_i δ³、density≥cδ^{η_in}（逐index longmark #J_i≥D^{1−η_in}），总unionvolume≤C#E_vis δ³。共同lengthrescale后套上一段，约去δ³，得Σω_i#J_i≤Cε A D^ε #E_vis。arbitrary repeatedindices/不同marks均保留；没有directionseparation假设。

continuousprior应用：coefficients以远细于δ网格round，按roundedtrace和finite markset分组，weight为原prior总质量；组数可能巨大但finite，引理常数独立indexcount。固定cell/plankenlargement包回原trace。marklabels仅为证明estimate，无需输出chartlabels。因此原2.15在G条件下已给，未引用companion其它主定理。

## 6. 原2.16的实际初始true构造

取q~a_L。每world每q-interval按midpoint y到q-bin、X到a_L-bin分组G。系数bounds给全block |y−ymid|、|X−Xmid|≤Kq；pL确定当前X up to Ka_L（v2 Taylor曲率项O(Ka_L²)），故groupG由pL以subpowerlist已知。test为v1 w−b_G，或v2 P_*−b_G；derivative/curvature和wholeblocksmallvalue符合terminalchart要求。剩余只需spatialplank的truefloor。

移到y-bincenter并除Rq（R大subpower），time归一[0,1]，traces在固定boundedchart，J0=(Rq)^j。此group仍用旧trajectorylaw的restriction，**不除该group质量**。knownG和coordinatechange给typical原groupbase density≥K^{-1}n(L)J0。选ρ=D_m^{-1}~N^{-D}，D固定足够大，以jointflattening把density lower转到cellaverages，globalweightedbadmasspower-small。以下ξ∈(0,1)固定后再选ε。

greedy在remainingwholetrajectoryfamily中选arbitraryorthonormal spatialplanks、affinecenters、ρ≤r_i≲1，若该plank中remainingselectedincidencemass（blocktime已归一）≥N^{-ξ} n(L)J0 Πr_i，则全containedavailabletrajectories归该chart并删去。每步mass下界reciprocalpolynomial（n(L)、J0、ρ有temperedbounds且ξ<1），故uniformpolynomialsteps。endpointlinearinequalities测wholecontainment，successiveexclusions保持tempered。任选containedtrace为center、fixedenlargement使center/speed polynomialcontrolled；oldJacobian=J0Πr_i，floor就是greedythreshold。group内assignments互斥。

若未覆盖一半globalmass：先删原groupcellfloor低于N^{-ξ/4}n(L)J0的power-small旧witness异常；再删remainingmarked duration小于globalinitialmass足够小固定倍的trajectory–block entries。后者的global损失用Σωγqνγ(assigned)≤1控制，故还留inverse-subpowermass，每usedtrace有≥1/K的normalizedmarkedlength。weightedaveraging可固定一个group，其survivingmass≥m_G/K，m_G为**原groupselectedmass**。

每residualvisitedgoodcell都有原whole-cellwitnessmass≥N^{-ξ/4}n(L)J0ρ^{j+1}，因此#cells≤m_G/[N^{-ξ/4}n(L)J0ρ^{j+1}]。不声称currentresidualcell仍有这个floor。将所有positive survivingduration的timebins标记，#marks≥D_m/K，每原trace保旧priorweight。bincentermoving仅fixedcell enlargement；rawweightedmarkcount≥m_GD_m/K。

j2时直接应用2.15，除cellcount得rawmultiplicity≥K^{-1}N^{-ξ/4}n(L)J0ρ²；故某fulltimeplank physicalarea uv承载oldusedtrajectoryweight/(uv)≥cεK^{-1}N^{-ξ/4}D_m^{-ε}n(L)J0。每usedtrace duration≥1/K，遂incidencemass/(uv)也有此界。

j1时给每trace添加independent static z∈[0,1]（原prior×dz），visitedcellcount最多乘Cρ^{-1}，markcount不变，得到同二维估计。若返回rotatedrectangle的横向projectionwidth为W、area~uv，其任意verticalsectionlength≤Cuv/W（可由sidehalfwidths u,v及angle的projection/chord公式直接验证）。每originaltrace接受的dummyfraction≤该界（在任一time已够），故originalusedtraceweight/W至少是paddedweight/(Cuv)。projectedintervaltube仍fulltime，原duration也≥1/K，转回j1的incidencemass/W。

选ε使Dε<ξ/4，以上lower严格大于N^{-ξ}n(L)J0的greedythreshold，反stoppingrule。固定enlargements/原trace rounding只改constants，plankminimumwidth可clip/放大与ρ比较。故halfglobalmass必覆盖。ξ↓0只在每fixedξ/ε估计完成后慢diagonal；polynomialcomplexityuniformξ<1，得到truefloor withsubpowerloss、h=L。命题2.16在具名G下通过；不是无条件移除三维高级输入。

## 7. Horizon composition与正临界率

knownatlas在depthr有horizonh，remainingproblemF。任意τ>0，按H(F)定义选terminaltruechild cost≤H(F)+τ，允许所需exactsubsequence/restriction；用terminaldensity(N2)经knownparent提升，timecostsadd，得H(E)≤h+H(F)+τ。τ↓0给4.1第一式。allinputswithinonefixedexactproblem，无需uniformthreshold。

coarsening到r保原trajectory/incidences/profile[0,r]，2.7给对应angularcap；若声称coarsenedC(dbar)，必须另核f(r)−f(s)≤dbar(r−s)。它不由原terminalC(d)自动推出。外problem的任意near-minimaltrue system经2.10 prepared knownpr，成为原E的trueintermediateparent；normalizing剩余由(N2/N3)保原C(d)、长度L−r，H(F)≤k(d)(L−r)。故

    H(E)≤H_out+k(d)(L−r).                                     (H1)

relativeprofileexponents在inverse-subpower restrictions下不改；新的subsequences和systems本来就在H的competitors中，infima可逐τ取，不假attainment。

定义d*=inf{d<1:存在C(d)bad H>0}，k(d)=sup_E H(E)/L，k=lim_{d↓d*}k(d)。lengthrescale N'=N^L同时把depth/horizon/logdensity除以L，angularu也除以L，S,η保持；故可归一L1。由§6 k≤1。对d靠近d*取固定d0<1，badE、e>0小于H(E)/2及TEX尺度，选h<H(E)+e/4。TEX给knownatlas horizonh−e、remaininglength0<L'≤Ce，uniformC只依fixedd0/model/Sη。composition得H(F)>3e/4，故k(d)≥3/(4C)，d↓d*得k>0。e对该fixedE选择，不声称e_N统一或outeruniform阈值。

maximizingsequence指length1 exactE_i∈C(d_i)、d_i→d*、H(E_i)→k。每fixedi先完成自己的exactN-sequence指数/infima，再i→∞。monotonicity给limsup k(d_i)≤k（亦允许d_i=d*）；不能用一个(i,N)diagonal替代。

## 8. 四项critical paths：relativeprofile

令g_i(r)=f_i(r)−f_i(0)。0≤increments≤length给uniformcompactness。任意subsequential uniformlimitg若有interiorsecant[a,b] slope<d*，当d*>0选secantslope<d''<d*且d''>0；大i取f_i(x)−d''x在[a,b]的minimizer r_i。strictsecant差和1-Lipschitz使r_i−a≥c>0。minimizer给[a,r_i]全部terminalcapd''。

x<a时，f_i(r_i)−f_i(x)≤d''(r_i−a)+(a−x)=(r_i−x)−(1−d'')(r_i−a)。除r_i−x≤1，coarsenedG_i的globalterminalcap≤1−(1−d'')c<1；angular由§2。若H(G_i)>0，**先固定i**，取其TEX constants C_i,c_i，e<min(H(G_i),c_i r_i,(r_i−a)/C_i)，trueh<H(G_i)+e/4。TEX使remaininginterval[t_i,r_i]完全落(a,r_i]，且positive length；normalizationprofileupper+terminalequality给remainingF∈C(d'')。composition使H(F)>3e/4>0，违d*。故每大i有H(G_i)=0。

(H1)回到原E_i，H(E_i)≤k(d_i)(1−r_i)；r_i≥c而k>0，违maximizing。若d*=0，monotonicity已排lowersecant。故limitg每interiorsecantslope≥d*；原endpointcap给g(1)−g(s)≤d*(1−s)。令s→0并用continuity，强迫g(r)=d*r。任意subsequence的所有uniformlimits同一，故全部g_i uniform趋d*r。完全没有对f_i(0)取compactlimit。

## 9. Fixed finitegrid的嵌套真系统

固定0<r<1。记uniformprofileerrorε_i→0，取α_i↓0且ε_i/α_i→0，令r_i在[0,r]最小化f_i(x)−(d*+α_i)x。与x=r比较得α_i(r−r_i)≤2ε_i，故r_i→r；实际endpoint的terminalcap为d*+α_i。coarsenedG_i归一除**r_i**后属于C(d*+α_i)。

其outerH_i≤k(d*+α_i)r_i，且H(E_i)≤H_i+k(d_i)(1−r_i)。上下夹得H_i/r_i→k。因此G_i/r_i maximizing。选择actualoutertrue costs h_i/r_i→k，preparedknownpr_i；originalfinerremainingF_i由§3归一保C(d_i)，长度1−r_i，其H满足

    H(E_i)−h_i ≤H(F_i)≤k(d_i)(1−r_i).

所以F_i/(1−r_i)也maximizing。所有进一步outer/inner subsequences保这些bounds。

对固定有限orderedtargetgrid 0<r^(1)<…<r^(m)=1，迭代该程序，每步用由limitingremaininglength确定的fixedfraction，实际分段length a_{i,j}>0趋a_j=r^(j)−r^(j−1)>0。归一时除actuala_{i,j}，回传时乘actuala_{i,j}；finitej的errors仍oi(1)。最后fraction1直接选remainingterminaltrue，故最后depth严格1。各段relativehorizon→k，cumulativehorizon→kr^(j)，相关coarsened/remaining序列都maximizing。

§4确保各次childintermediatetrue经preparedtrueparents可lift；记录整条labelhistory和wholelayers/frozenwitnesses。nestedtimepartitions、spatialJacobian乘法与有限subpowerlist确保actualobjects，不是纯exponentformalpath。仅finalpath无需再证明它saturatesearlierfloors。固定grid只finite次subsequences，不能直接宣称同一系统同时实现所有无限grid。

## 10. Finite/infinite narrowness优化

v2对一个maximizingsequenceE定义ω(E)：所有terminaltruesystems（允许outer子列、每i各自exact子列和合法selections）且relativehorizon→k时，attainable narrownessexponents之limsup的sup。设ℓ=inf_E ω(E)∈[0,∞]。sup/inf都无需attained；v1只记formalℓ0。

若ℓ<∞，固定ζ>0选wholebasesequenceω(E)≤ℓ+ζ。每新coarsenedmaximizingsequenceE'都有ω(E')≥ℓ，故存在terminalchoices horizon→k、limsupnarrowness≥ℓ−ζ/2；取outer子列得到liminf≥ℓ−ζ（若ℓ<ζ可用nonnegative）。每fixedi再选所需actualnear-infimumtrue，不能只取formal极值。如此迭代有限段，包括最后，剩余仍maximizing。设relative段窄度β_{i,j}≥ℓ−ζ−oi(1)，旧units增量b_{i,j}=a_{i,j}β_{i,j}。

finite段compose得base的terminaltrue horizon→k，故总χ_i=Σb_{i,j}的limsup≤ω(E)≤ℓ+ζ。对任意段集合，其实际总length为a_i，逐段lower给Σb≥(ℓ−ζ)a_i−oi(1)；从总upper减complement段lower又得Σb≤ℓa_i+2ζ+oi(1)。所以累计窄度和任一increment都是ℓ乘其实际length加O(ζ)+oi(1)，O(ζ)可取统一常数，fixedfinitegrid只影响oi(1)。horizons仍kr。totalupper针对**最终composedactualsystem**，不能拿每段各自ωupper拼接。

若ℓ=∞，每一个newmaximizingseq必ω=∞。这可能只是sup无界，不是单一choice已经limsup∞：对thresholdM先选attainablelimsup≥2M，再outer子列使narrowness≥M、horizonerrors小。M逐整数慢增加、每阶段fixedi的innerexactsystems先存在，再outer选i，给narrowness→∞且horizon→k。对fixedfinitepositivelengthsegments迭代，actuala_{i,j}最终≥a_j/2，threshold可除该下界保证oldunitincrements也任意大。有限次嵌套子列保此前阈值。无需ℓ∞在某singleexactproblem由一个unbounded系统实现。

## 11. 反攻、边界与剩余责任

已逐步测试：ω/Z混within-world (N1)；仅terminalknownparent非法intermediatelift；oldfullwitnessfloor与currentresidual不同；不核coarsenedterminalcap；强行outeruniformTEXconstants/e；absolutef0compactness；actual/limitinglength互换；双极限抹去；ω/ℓ未attain；finalpath替代wholelayers；weightedplank重复indices、逐管marks与平均density混用。上述错误均会使证明失效，但本稿没有按这些错误推理，未找到保原全部假设的反例。

简单两label密度模型可见(N3)upper不足lower：旧coarse densityg，某labelrestricted numerator仅εg，任意小ε；给其childfloor只能回传ε倍旧floor。这个模型解释为什么knownpr是实际假设，不是声称反驳原2.13。相似地任意subselection可让一个earlierchart的pathmass任意小，故保earlierwholewitness是必要接口。

通过本阶段仍未核后续excluded improvements、linear relation/higher branches、所有badproblems排除、完整2.17和finite readout，以及G与具名KT全证明。R29 finite种子和六维17/4仍依完整OAI4及其全部输入、具名KT与Hausdorfftransfer。下一候选须重新盘点这些责任和路线收益，不能自动从本文末尾逐节续审；Goal active。
