# R0037 原正有限窄度完整分支：逐步证明与量词审计

2026-10-17。状态：修后两份实际全文独审通过，root整合完成；未经外部同行评审。范围是原稿§7–9已有分支，不声明新定理/新Kakeya界。原PDF物理页108–153、text5803–8254；官方06a-retained-edge.tex、07-finite-narrowness.tex、08-critical-rates.tex精确源码。8.2复用UNB001。下文所有K为当前tangent序列的subpower，可因固定准备增大；原尺度actual输出另由AIM001支付，不将K当actual输出预算。

## 1. 命题与固定对象

在原4.7 version2、0<=d<1（原capclass边界，未加pointwise lower regularity）、0<k<=1、0<ell<infinity及CRP/TCM/ASM/TEX/AIM/ISO/UNB具名输入下，对每子列和每substantial raw active residual，进一步子列给原Def4.10 strip或time candidate，depth固定正且有界，gain固定正有限。time输出在全assigned block满足proper degree2 test，hidden derivative上/计数下界和curvature条件，质量为q_Q nu_Q N^{-dc}/K；strip输出质量q_Q nu_Q/K且velocity改善固定幂。nu_Q是完整trajectory assignment，不是成功样本的后验。

原几何尺度 a_s=N^{-s},h_s=N^{-ks},g_s=N^{-ell s},b_s=h_sg_s，true Q_s长q_s~h_s、tilted spatial axes h_s,b_s，nu_Q~a_s^d h_sb_s。所有删选保固定轨迹prior、原palette pi和原clock。Σ_Q q_snu_Q<=1；归一为Q-time要除q_s，条件prior再除nu_Q，两个分母分开。未审的新GWZ set输入仍具名，WZ/CV/下述OSS为既有一手文献具名定理，未查证OSS期刊发表状态；不冒称完整高级证明都重证。

## 2. 删选闭包与非新方向检查

raw上界对restriction自动保留，当前entry floor和conditional pi domination不自动保留。每次附加datum只有K options/history时，先冻结reference R_e且ΣR_e<=KM，删除current mass<R_e/K1者；损失<=KΣR_e/K1，选K1晚于当前inverse dense mass和options。留下entry除新floor后才有conditional velocity<=Kpi。旧full-domain witness可单独保留，不能将它称current floor。

有限多family同时floor可反复删任一不达阈值的label：每label删后永久空，至多charge一次，总损失由阈值和控制。平均incidence mass、完整assignedprior和逐轨迹duration分别处理，不能相互替代。8.2、ISO/scalar firstjet对所有合法原选择的统一结论只重用；G(u)是本分支迭代性质而非新研究方向。旧OBS002不满足本分支原endpoint/factorization，不能直接反源。

## 3. 7.1–7.3：保原edges的同endpoint scalar closure

有限图G⊂A×B、density theta，C={x+y:(x,y)∈G}。先删degree<theta|B|/2的A；令bad pair common-neighborhood<theta^3|B|/512。随机邻域U用E|U|²及E Bad(U)选大U、低bad比例，删bad伙伴太多者成A'，B'取与A'有theta|A'|/4邻点。原edges≥c theta²|A||B|，两端≥c theta各原大小。每(u,v)∈A'×B'有≥c theta^5|A||B|条原三步walk，三sum交替给u+v且对固定端点注入；每distinct sum选一端点，triples不相交，故 |A'+B'|<=C theta^{-5}|C|³/(|A||B|)。不能只留下抽象小doubling vertices。

7.2 mesh h=N^{-a},L=h^{-1}：|A|,|B|~_K L，represented index law κ有K^{-1}<=|κ|<=K及interval cap K r^S，原Gκ有≥L²/K edges、restricted x+κy sumcover<=KL，uniform edge first-coordinate rectangle cap Kh²。round A,κB到h格，vertex/edge multiplicity<=K/K²，应用7.1后pullback全部selected vertices和原edges，得Aκ,Bκ小crosssum且保≥L²/K原edges。

对rectangles Aκ×Bκ在同A×B universe作二次平均，选represented κ0，使positive-subpower index mass与其交集≥L²/(2K^6)；各端交集≥L/(2K^7)。固定 A*=Aκ0,B*=Bκ0，E=A*,F=-κ0B*，R={κ/κ0}。原Gκ0在E×F仍≥L²/K edges，ratio law的intervalcap保正指数。

以 d_h(U,V)=log[N_h(U-V)/(N_h(U)N_h(V))^{1/2}]，mesh Ruzsa triangle及fixed-iterate Plünnecke–Ruzsa给d_h(E,F),d_h(E,tF),d_h(E,tE)=O(logK)。通过large intersections连接各κ与κ0。固定长度product p=t1…tj逐次triangle，d_h(E,pE),d_h(E,pF)=O_j(logK)；selfdifference再给signedproducts。覆盖lemma把每signedproduct U包在K_H个E-E translates，固定和仍K_{m,H}L cells。coefficient c是signedproducts的和时只用 cX⊂Σ ε_jp_jX；不除会抵消的c，故c=0无问题。所有common subpower dilation单独支付mesh成本。固定迭代set calculus具名经典输入，未将长度随N自由增长。

## 4. 7.4：OSS输入与真正flat coefficients

使用Orponen–de Saxcé–Shmerkin arXiv2309.03068v2 Th1.5：固定n>=2、s_j∈(0,1]、Σs_j>1，[-1,1] Borel probability各single-scale smoothed energy I_sj^r<=r^{-epsilon0}，则乘法卷积在r^{-1}<=|ξ|<=2r^{-1}有|ξ|^{-tau}衰减。精确单尺度版本/无避零要求核于PDF2；其whole advanced proof保具名，不以作者保证正确。

令λ=law(T/R)支撑[-1,1]，R及R^{-1}subpower；选0<s<min(S,1)，n s>1。ratio interval cap经r-ball与dyadic annuli使I_s^r(λ)<=C_s K'，h<=r<=1。固定e0<e/2后，在h<=r<=h^{e0}上K'<=r^{-epsilon0}对晚N一致。ω=λ^{⊠n}在h^{-e0}<=|ξ|<=h^{-1}衰减；取固定j tau>2，η=ω^{*j}。bandlimited positive majorant积分给 sup_x η([x-h,x+h])<=C h[h^{-e0}+∫_{h^{-e0}}^{h^{-1}} t^{-j tau}dt]<=C_e h^{1-e}。

每系数C=Σ_{i=1}^j∏_{l=1}^n T_il/R属于§3准许scalar expression，同common R^{-n}；不同coeff独立，但同一collision的两endpoint sum必须用同一coeff tuple。n,j只依固定e，之后才h→0，最终slow diagonal不在任一fixed tolerance使用无界表达式长度。

## 5. 7.5–7.6：collision强迫同slope strips

µ是≥L²/K retained原edges的uniform law（变y→-κ0y）。设 p(w)=sup µ(S_E×S_F)，两strip平行、宽w。若固定ε,c>0序列上p(h^{1-ε})<=h^c，取m对独立edge-pairs，v_i=a_i-a_i',u_i=b_i-b_i',q=h^{ε/2},Delta=q h^{1-ε}/10。rectanglecap先给P(|v_i|<q)<=CKD(q+h)。若某|v_i|>=q而所有wedges<=Delta，则其余unprimed edges各落在一对宽w平行strip。固定anchor/primed后仍独立，故degenerate概率<=[CKD(q+h)]^m+m p(w)^{m-1}<=h³，m固定够大。

两sum Z=Σ(C_i a_i+D_i b_i)、Z'=Σ(C_i a_i'+D_i b_i')：条件同coeff tuple为同分布独立samples，support<=K_m h^{-1}，collision>=h/K_m。另一方面endpoint先固定，非degenerate时选r,s wedge>Delta，选法不看coeff；条件其它coeff后剩二独立flat law。allowed parallelogram面积O(h²/Delta)、perimeterO(Dh/Delta)，只遇K/Delta个h-squares，每个prob<=C_e²h^{2-2e}，故collision<=h³+K_m h^{1+ε/2-2e}，e<ε/8矛盾。因而每fixedε,c后有p(w)>h^c，slow diagonal给宽h^{1-o1}、mass h^{o1}。

矩形first-coordinate cap还给m0<=CK(D|q_direction,1|+w+h)²，故strip direction第一分量逆subpower下界，slope subpower有界。undo -κ0 dilation保同slope和原edge身份，得到7.6。仅vertex集中不足以恢复原incidence，这里始终保original graph edges。

## 6. 7.7：affine–skew row，两个不同冻结law

z=(t,Z)，velocity(1,v)，raw µ<=Kνdt、mass>=1/K，jointcell<=Kξ² pi(vξ)，row T每zξ有K个E-bins且T·(1,v)逐trajectory近常数，ξ<=E。设V0=(ξ/E)T，occupied(z,V0)ξ只有Kξ^{-2}cells；投影P_u(z,V0)=(z·Ju,V0·u)沿direction u近常数。

先freeze µ_cov：删过短line witnesses后每used trajectory有duration>=1/K、≥1/(Kξ) witness cells；相距>Kξ的projection values用disjoint witness sets，故每direction projectedcover<=Kξ^{-1}。此旧cover在后续删选仍可用。另删π weight<ξ² bins、homogenize palette weights成M bins，uniform law仍有fixed positive interval exponent。normalize当前law freeze µ_pt，每point–directioncell<=Kξ²/M，删lightpoints/edges并低degreepoints，保≥ξ^{-2}/K high-degree cells，每cell有旧µ_pt marginalfloor ξ²/K。不能用µ_cov的longline见证冒充这组pointfloors。

以uniform palette选三separated incident slopes，pigeonhole前二v1,v2并保many third directions；A=P_u1(pointcells),B=P_u2(pointcells)，invertiblebasis给K preimages/endpointpair，原thirdgraph≥ξ^{-2}/K edges。u_d=c1u1+c2u2，κ=c2/c1=(vd-v1)/(v2-vd)，a+κb=c1^{-1}P_ud(point)。fractional map有subpower inverse Lipschitz，保ratio intervalcap；指定first endpoint rectangle束z到Kcells、row Koptions，uniform graph rectanglecap成立。

7.6选原edges→≥ξ^{-2}/K distinct survivingpointcells。strip slope若记λ_strip，投影关系为V0·u=b+λ_strip z·Ju=b−λ_strip Jz·u；解basis并重命名λ=−(E/ξ)λ_strip，还原T=B+λJz+O(KE)。restore这些cells的全部µ_pt incidences，无需direction仍是所选三方向。若|λ|固定幂大，由|T|<=K迫z落半径K/|λ|球，jointcapsum给mass<=K(K/|λ|+ξ)²，反densemass；故λ,B都subpower。结论可重新用于每合法dense residual。

## 7. §8.2–8.3：finite parent投影及双向comparison

固定parent residual，α=(vχ,Z(0)χ)，wα=π(vχ)χ；另crop(Y(0),Y')于g_s，group prior p_αγ。条件prior固定，rawactive除p；Y减representative affine motion再除g_s。8.2 prefactor c=wαg_s/p。σ=N^{-M}且χ更细：jointcell积分Z motion给Kσ² wα g_s p_hidden^d，除p即8.2 density。

support另算：每trueQ_s、velocitybin有K h_s/χ个Zintercepts，每个K个γ，normalized(t,Y) area<=K q_sb_s/g_s，stablegraphs每cell K terminal X_a bins。乘wαg_s再sumπ→每Q成本Kq_s h_sb_s~Kq_snu_Q a_s^{-d}；总<=Ka_s^{-d}。删除weighted support过大/poor success groups有budget；unitcap+densemass确保c,c^{-1}固定幂。8.2给disjointwholetrajectory Φ_s，原activefloor wα a_s^d β_s/K，g_sσ/K<=β_s<=Kg_s，全unit quadratic X-fit Ka_s。原prior不因删active重设。

比较domain D取length q~min(h_s,β_s/g_s)、Y'bin g_s、midpointwidth m~qg_s。两色entry reference T_D=q wα a_s^d m：true色sum<=KΣ q_snu_Q，projected色sum<=KΣ wα a_s^dβ_s，均<=K。删light marginalentries和stablebranch/core subentries，先选共同comparison ball再配pair，避免pairwise-ballintersection损失。

每index–base density<=KT_D，discrepancy M0/a_s固定幂大时按nearbyjets分组，每色storedfloor在common graph KM0 band下计数<=K(M0/a_s)^d。densebadmass group B>=(W1+W2)/K，分色referenceprior p_i=T_i/W_c，rawceiling/B<=K p_i，B<=KW_c，付tinygroup分母。TCM/ASM的Cor3.4否定power discrepancy；slow tolerance给normgap<=Ka_s。每fixed(α,D,Q_s)及reverse的partnerfloor再在Ka_s-band下sum，双向list<=K。无每surviving pair的独立floor，也不用neighbor paletteweights可比。

## 8. 8.4：three wide intervals的参数与two-domain比较

三depth s,s+u,s+c2，a1=aN^{-u},a2=aN^{-c2},0<c2<(1-d)u/4。βmax<=Kg_s且 b_s/βmin+h_s βmax/βmin<=N^{-(C_d+3)u}, C_d=10/(1-d)。shortdomains是Q_s全block/widthb_s；longdomains length ρ~βmin/βmax、widthβmin。各色reference A wα a_i^d，分别保floor与prior。

longnorm discrepancy若M0>=aN^{C_du}，每色list<=K(M0/a_i)^d<=K(M0/a)^{(1+d)/2}，因d+d/C_d<(1+d)/2<1，套matching可排除。whole shortdomain diameter在longunits<=K(h_s/ρ+b_s/βmin)，故F_Φi-F_Φ在全shortdomain变化≪a_i；写 X=F_Φ+D_i+O(Ka_i)，constant D_i<=Ka。floor+cap给每coarse entry fineroffsets<=K(a/a_i)^d，reversecoarseoptions<=K。保source(α,D,Φ1,Φ,Q)的unnormalized density ceiling q_s wα a1^d b_s×K area，不除其survivingtiny mass。

## 9. 8.4：非constant transverse coefficients必须共同

Qunits z=(t-t*,Z-Z*)/q_s,U=(Y-Y_Q)/b_s，F_Φ=f0^Φ(z)+f1^Φ(z)U+f2^Φ U²，f1 affine/f2constant。令 e=aN^{-(1-d)u/2},τ=(1-d)u/8。在fine(Q,z,U,X)state配独立targetconditionaldraw；targetvelocitykernel<=Kπ，source保持Φ1 ceiling/reference总和<=K，不假Φ独立于v。

fixedsource与targetvelocity在tinytimebin只K targetα/coarsepolynomials，细Φ1只增加≤KN^{du} offsets、不增derivativepolynomial数。若nonconstant coefficientpair gap>=Ke，二次polynomial的U-derivative gap>eN^{-τ}除U-length KN^{-τ}；在其外每offset值能匹配Ka1的length<=Ka1N^τ/e。sumoffset给KN^{du}a1N^τ/e=KN^{-3(1-d)u/8}。sourceceiling积分timebin长度而不乘bin数，再sumreference与π，badpairs power-small。所有冻结/transporterrors以χ和更细state统一压入Ka1。

stateconditional averaging给确定coeffpair。选heavyQ，以palettepairs选两separated basisdirections，并用ω≪χ productgrid；同fiber全程K个α/coarseΦ，其coeffpair各affine+constant。按fiber平均选一fit，保dense matchingvertices。3×3 complete bipartitegrid的双Jensen保dense量，固定四anchors给≥ω^{-2}/K targetvertices；row/columnaffine interpolation给bilinearfirstentry和constantsecondentry，coeffK。

还须消mixedbilinearterm：保选择fiber/anchors之前的rawdirectionbound µ_Q(axisballs r)<=K m_Q r^{S'}，后续restriction仍成立。选r逆subpower小于retainedmass/K，保nonaxisdense law；prior–time domination得一条duration>=q_s/K的nonaxisline，其中一coarseΦ仍长。其bilinearrestriction二次项等于mixedcoeff×两个basiscomponents，二component逆subpower下界，Remez给mixedcoeff<=Ke。因此有共同 P_nc=C1(z)U+C2 U²。

subtract后每zcell、固定velocity只有K(a/a2)^d residualbins；outputstate不append projectedlabel，只有K options/deephistory，重新删lightentry取conditionalπ。compatiblevelocitypalette mass>=1/K，积分pervelocitylist得到无velocity的同supportbound。归一byq_snu_Q，projected(t,Z) density<=K(p/a)^d、angularcap仍有；terminalsupport σ²#<=K(a/a2)^d。8.2以c=a^{-d}、terminala2给β~1 label、mass≥(a2/a)^d/K，全time quadratic。restoreP_nc，得Q_s mass q_snu_Q(a2/a)^d/K的fullbasequadratic timecandidate。nativeP*减basequadratic不改hidden derivative/curvature；AIM支付actual恢复。

## 10. 8.5：窄projectedinterval→horizontal equation及k=ell

若s=1附近三β_s'~g_s'则§8立即给candidate；否则某β_s=N^{-B0+o1}、ell s<B0<=ell s+M。选r>s使(k+ell)r>B0>ell r，Q_r与Q_s history/finehorizontalposition/velocity给K比较domains，继而Y'在K个β_s bins。normalizeQ_r：horizontal (t,Z)除q_r，transverse (Y-Y_Q)/(q_rg_r)，normalizedvelocity=(Y'-A_QV1)/g_r。

deep rowT=(A_deep-A_Q)/g_r的evaluation近trajectoryconstant，accuracy E=N^{-(B0-ell r)}。fine(location,deeprow)state conditionalπ给两separated velocities，解row boundK；每fixedvelocitypair的K evaluationlists给K rowbins，再按paletteproductweight计数，row每cell只有K options。horizontaljointcap before /q_rnu_Q是K ξ²q_rnu_Qπ(vξ)。7.7给T=B+λJz+O(KE)。λ固定幂小时原row是stripcandidate；否则λ~1，subtractB·z、divideλ，得 |Y'-(-Z+tv)|<=N^{-e0}，逐line误差恒定。

child relative s' time H~N^{-ks'}，deepfixedrow与Jz按两velocity比较误差<=K(N^{-ell s'}+N^{-e0})。currentchildfloor Hnu_child/(Knu_Q)和prior–time domination迫active duration>=H/K；row的第二分量预测t到KN^{-ell s'}，故k>=ell。若k>ell，Jz替activechildcenter误差KH固定幂小于g_s'，给stripcandidate及正确fullprior质量。余下k=ell。childwholebox以occupiedcenter写 zhat=(z-zc)/H,Yhat=(Y-Yc-Jzc·(z-zc))/H²；row差KH×horizontalH只KH²，故整个box（非仅active points）有H/H² geometry。

## 11. 8.6：contact方向消除hidden sheet的非affine部分

hiddenw保原derivativeunit，fittedwidth Delta=a_r a_s'。高curvaturecutoff用affinecenter，低curvature用stable simplebranch，K cores/branches/label。删短ballbranchwitness和lightentry，reference blocklength×fullprior求和支付；basecap得inverse-subpower填充，存longwitness，后续currentfilling需再删轻entry。

设M_f为realcomparisonball上bestaffineerror。ASM fixeddegree norm+margin使所有二阶以上固定阶derivative<=KM_f；沿longsamebranchchord的f−affinelinesignal小KDelta，一维algebraicRemez给Hessian(actualW,actualW)<=KDelta。三separatedvelocityactualwitnesses在同finestate，transfer到samebase及horizontalW=(1,v,-Z+tv)误差KM_fN^{-e}。这里先减任意affinepart再估，未对f/w或affinepart假设固定幂幅度。

Xcal=∂t−Z∂Y,Zcal=∂Z+t∂Y；(Xcal+vZcal)(−Z+tv)=0，故平方正是frozen-direction Hessian。interpolate三个v得Xcal²f,Zcal²f,(XcalZcal+ZcalXcal)f全O(K(Delta+M_fN^{-e}))。algebraicRemez将well-filledbase estimate及所需固定阶derivative传comparisonball。Tcal=[Xcal,Zcal]=2∂Y central；

Xcal(XcalZcal+ZcalXcal)−2ZcalXcal²=3TcalXcal，
Zcal(XcalZcal+ZcalXcal)−2XcalZcal²=−3TcalZcal，
Tcal²=Xcal TcalZcal−Zcal TcalXcal。

由此得fYY,f_tY,f_ZY及f_tt,f_ZZ,f_tZ同bound；Taylor affineerror M_f<=KDelta+KM_fN^{-e}，晚N吸收第二项，无需M_f预先powerbound。拟合在storedlongtimes成立，f的affinefit与真实w在line上差affine，外推全assignedblock仍KDelta。

## 12. 8.7–8.8：bounded residual、任意fine state与nested slopes

选parentaffineL后x=(w-L)/a_r，fullblockfit给x,x'<=K。固定fullprior ν^flat=ν(.|Q_r)，rawµ由q_rnu_Qr归一、不再除retainedmass。恢复fine residualstates必须先在更deeptrueR删lightbranchentries，referenceΣ<=Kq_rnu_Qr；bounded实际x和filledbase使g_R=(f_R-L)/a_r的norm/derivativesK，即使Lcoeff巨大。先使R grapherror小于targetmesh，再用更deep位置精度，得K residual/baseoptions/history，**不依horizontal equation在该mesh有效**。之后append state并重付currentfloor来转velocitynumerator。纯cap积分oldw宽pa_r围绕exactL，得µ(C,x_p)<=K|C|p^d，联合<=K|C|p^dπ(vχ)，restriction保upper。

fullchildprior ν^flat(Q_s)~a_s^dh_s³，m_Qs=H_sν^flat(Q_s)~a_s^dh_s⁴，Σm_Qs<=1；prior不condition Lsuccess。相邻depthaffinepairs只有K options/child，删小于εm_child/K_pair，损失Σ<=ε。storedpairwhole-domainfilling给norm(L_si−L_si-1)<=Ka_si-1 onchildbox，水平slope增量<=Ka_si-1/h_si、transverse<=Ka_si-1/h_si²。depthgrid慢增并gaps→0，telescoping得

|∇zL_s+(∂YL_s)Jz|<=K(1+a_s/h_s)， |∂YL_s|<=K(1+a_s/h_s²)。

原horizontal equation逐line恒误差给Z=p+tv,Y=q0−tp+O(N^{-e0})。仅在coarser-than-error、含所有coefficientamplification的fixed buffer内用此reconstruction；更finecaps积分使用真base，不把approximation无限延长。

## 13. 8.9：spacetime support→fulltime heavy coefficients

k<=1/2时上述ordinaryslopes全K。固定s、D=a_s^u(u>=1 bounded)≤a_s≤h_s²，group G=(d0,P_D),P=(p,q0)，W_G=π(d0)D²。movingcenter (Zc,Yc)=(p_c+tv_d,q_c−tp_c)，jointcap在其KD² spatialarea积分给每timeI/widthρ≥a_s band mass<=K|I|W_Gρ^d。Σ_GW_G<=K，丢poor mass/W_G或success/prior groups后active/prior~W_G，prior仍完整assignment。

support不由cap推：先在boundedresiduallaw freeze每usedQ_s的full-domainwitness mass>=m_Qs/K。group在a_s-timebin遇其box，D≤h_s²使wholebox都在reference motion的共同horizontalenlargement volumeKh_s⁴；disjointstoredwitness+纯unitcap给labelcount<=Ka_s^{-d}。boundedslopes、D≤a_s和timebinlengtha_s让每affineentry仅K xbins；全(t,x)support<=Ka_s^{-1-d}。

任意dense residual先删短integratedduration trajectories，固定prior的coefficientballcap Kρ^d由bandcap除duration所得。已审scalarclustering(原5.1)对zeroquadraticcoefficient给一ordinary a_s coefficientbin的prior≥a_s^d/K，duration再给activefloor。若lightbins携nonvanishing总mass，先aggregate选densegroup、再对此badbin residual调用同过程，contradiction；slowδ→0得所有retainedbins有activefloorW_Ga_s^d/K，count<=Ka_s^{-d}，fullunitpredictions。

time再分η≪a_s，删entrymass<ηW_Ga_s^d/K'，counts与Ση预算支付。一个coefficiententry若任一点进某x_a bin，其整个storedsubbinmass因coeffdiam O(a_s)、time motionKη全在同K a_s band；bandcap KηW_Ga_s^d除storedfloor给K coefficientoptions。旧floor只在其指定stage使用。

## 14. 9.2 critical 2k=1：derivative primitive与upper count

取smallfixeds，a=a_s=h_s²、100s<e0，prepare s,s+c,3s，0<c<ks/2。Q_s+finehorizontalpoint+v确定P_a、x_a、d0/timeη到K options，8.9给K x' bins(widtha，仍全Q_r time)。G*=∇zL_3s+(∂YL_3s)Jz，slopeboundK且affinefit derivativeerror a_3s/h_3s≪a，故x'=G*·V1+O(Ka)。用sameappendfloor+separatedtwovelo interpolation给每horizontalcell K G*_a options；horizontalcap积分transverse H²与x_a，再除m_Qs~H⁴a^d，得Kξ²π。

7.7作用T=G*,z=zhat,E=a得B+λJzhat。primitive F*(z,Y)=(B−λJzc/H)·z+λY/H，有slopeK/H、|x'−dF*/dt|<=Ka，仍fullQ_r time。每trajectory midpointintercept c_l，x−F*=c_l+O(KaH)全block；a'=aN^{-c}且aH≪a'，故C=[c_l]_a'为trajectorydata，也由足够finebase/x确定K options。

upper(baseωcell,C)count<=Kω^{-3}(a/a')^d：true Q_s+c over allsubblocks count<=(a/a')^d(H/h_s+c)^4 K，eachwholebox在Q_sunitsvolume K(h_s+c/H)^4；meshω finerthanwidths，scale^4相消，affineL_s+c和F*每cell K interceptoptions。这里count的子块含timefactor四次，不能只用spatial三次。

## 15. critical：三次same-law切换给lower count

switchstate=(C,tinycenteredbase,tinyx)，由§12 truefineresidualstates给K choices/deephistory，即便fine beyondhorizontalequationprecision。referenceΣ<=Km_Qs，重删lightentry/aggregatestate后µ_last mass>=m_Qs/K且conditionalv<=Kπ。设tildeµ=µ_last/m_last；goodtrajectory指相对trueblockprior marginaldensity≥1/K1，坏轨迹stationarymass negligible；goodline的conditionaltimedensity<=K。

从tildeµ起，每步先conditional同switchstate刷新event/trajectory，再conditional整个indexedtrajectory刷新time，共三次；两个heatbath都保同tildeµ且C不变。只取三freshtrajectories good、|c2−c1|,|c3−c2|,|τ2−τ1|>=1/K'的subkernel，failureo1，**不renormalize kernel**。由conditionalπ与goodline时间密度，完整past条件下controls/times jointlaw<=Kπ^⊗3 dt1dt2dt3。stationarity只给总failure小，不将其错当uniform每C failure小。

signed traversals在centeredbase满足Z'=c_i,Y'=−Z+tc_i，模拟erroro(ω)。固定start和controls，D_j=c_j+1−c_j，

Zf=Z0+c1(τ3−τ0)+Σ D_j(τ3−τ_j)，
Yf=Y0+(−Z0+τ0c1)(τ3−τ0)+Σ D_j τ_j(τ3−τ_j)。

Jacobian det∂(τ3,Zf,Yf)/∂(τ1,τ2,τ3)=2D1D2(τ2−τ1)，regular下逆subpower；fixedτ3,Zf的internal times在线上，Yf二次，regularpreimages≤2。changevariables给endpoint每ωbasecell条件start概率<=Kω³。badC averagedfailure e_C，总Σq_Ce_C=o1，因此e_C<=1/2的C携1-o1 mass，每个至少1/(2Kω³)occupiedcells。与upperpaircount比得这些C数<=K(a/a')^d，故某C有rawµ_last(C)>=m_QsN^{-dc}/K。

restore原mass q_rnu_Qr，test w−L−a_r(F*+offset) hidden derivative1/curvature0、widthKa_ra_s+c，全assignedblockfit；候选depth r+s/gainc固定，fullnu_desc与timefactor保留。不是每C mixing常数统一，也没postconditioned independenttime。

## 16. 9.3–9.4：G(u)量词与full-time comparison

2k<1时G(u),2k<=u<=1：每fixeds<smax、每denseinput及每subsequence，经furtherrestriction/subsequence在groups(d0,P_D),D=a_s^u有disjointfulltime labels，activefloor π(d0)D²a_s^d/K，predictor H(t,P) affineP/timeaffine且normK于scaledparameterbox×unit-time，全assignedtrajectoryerrorKa_s。只说一个input某predictor不够再次调用。G(1)由§13。

在s0/nearbydeeper先preparetrueaffinepairwhole-domainwitness，再对该denseinput调用G(u)。slice H0/trueQ_s0 bygroup/timeblockI，reference T_GI=|I|π(d0)D0²a0^d。每Q,d0的parametercells<=K h_s0³/D0²（det-one map P→(Z,Y)且D0≤h_s0²），故两list referencebudget<=K，重新删lightentries。calligraphic L_s0(t,P)=L_s0(t,p+tv_d,q0−tp)与H0在pairedpointsclose，精度只用reconstructionbuffer内meshes；jointcap+jitter给indexbasedensity<=KT_GI。

按discrepancy M0附近jets分组，两colorstoredfloors在KM0 band下给listcount<=K(M0/a0)^d，选badgroup付B/W分母，Cor3.4排powergap，得whole I×parameterdomain norm<=Ka0。fixedH0,I的truepartnercount<=K。nestedtruepair另外有massm_Qs/K旧witness、wholechildbox||L_s−L_s0||<=Ka0，后续conditionH0不重设此见证law。

## 17. 9.5一个合法bootstrap step：fixed chartprior及instantaneous caps

假G(u)，2k<u<=1，target s1<smax，θ=(1-d)(u−2k)/10000，s0=s1/(1+θ)，D0=a0^u。每H0/I选K truepartners之一，summablefloors/poor-success deletion后fullpriorν^flat(H0)~W_G a0^d。固定ν_H=ν^flat(.|H0)，raw λ_H=f_Hν_Hdt，0<=f_H<=K_pre，δ_H=mass>=1/K；不能用λ_H的trajectorymarginal替ν_H。

设y=(P−Pc)/D0 static2D，barx=(x−H0)/a0 affinebounded，F(t)=∇y(calligraphic L_s0−H0)/a0 time-only K，S=barx−F(t)y。E=(u−2k)s0/10，ζ=N^{-E}，D0/h_{s0+E}^2=N^{-(10−2k)E}≪ζ。rawjointcap积分movingdomain给timeI/mixed y_r、barx_w mass<=K|I|r²w^d。

先取f_H≥δ_H/2，指标ρ^0=1_Eν_Hdt与retainedweightedλ双向subpowercomparison。timebins选K|I|≪ζ；删每line–bin duration<|I|/Kdur，其indicatorloss<=1/Kdur、weightedloss<=Kpre/Kdur。对active固定t∈I的lineconstraints，whole retainedportion I落同enlargedconstraints，所以 |I|ν_H(A_t)/Kdur<=ρ^0(I,constraints)<=2λ_H(I,constraints)/δ_H<=K|I|r²w^d。得instantaneous固定priorcap，之后只删E_l，upper保留；积分到time不能免费改成pointwisecap。

S_w support<=Kw^{-d}，w=N^{-s'},s'<=E：currentH0 events定位true Q_s0+s'，但计数用condition前原horizontal-law的pairedfull-domainwitness。commonbox体积Kh_s⁴、nearL_s0 bandceiling K h_s⁴ a0^d除每childfloor h_s⁴a_s^d/K给K(a0/a_s)^d；差affinefit的参数variation<=KD0/h_s²≪w，故每entry仅K S_w bins。删instantaneousbinweight<w^d/K预算可积；mixedcap在scalarwidthr并分y_r squares给S_r mass<=Kr^d，除binfloor得localcover K(r/w)^d。

## 18. scalar-normal全部准备、loss闭包与step输出

要调ISO已审scalar-normal firstjet，仍须先付regularization。fixedr下uniformtimepairs/commonrinterval的sharedlineweight Jensen有inverse-subpowerlower；若M=|F(t)−F(t')|≫r，源S_r bins、targetlocalcount K(M/r)^d及staticy projectionstrip由mixedcap给sharedweight<=K(r/M)^{1-d}。anchor每interval并保separatedresidueclass，finitewidths迭代、slowgrid后F Lipschitz K(|t−t'|+ζ)，每步损失纳K而非无限many固定损失。

每y_r group先删短line–timebin、短总duration，spacetime support<=Kr^{-1-d}；auxiliary ν_H restrictedgroup/longlines除r²只为clustering，不替fixedν_H。integratedmixedcap给coefficientballmass Kw^d。对任意dense lightbin residual重用clustering，得current B_r=(y_r,barxcoeff_r) floor r^{2+d}/K；再timeI_r entry floor |I_r|r^{2+d}/K，wholeentry碰一个cube则全storedsubentry在Kr-enlargement，cap/floor→K slopeoptions/cube。选一option+separatedcolor，finitegrid迭代给sloperegularity。fullparameterbin的fixedν_H floor>=r^{2+d}/K survives laterlabelrestrictions；instantaneousqcap除它给K(q/r)^{2+d}，补足scalar-normal的conditionalcap。所有widths先finitegrid、再slowdiagonal，保densemass和fixedprior。

firstjet使用H*=N^{-E/4}，ζ≪H*³，θs0=(1-d)E/1000<(1-d)E/256，reading/floor条件有room。结论 H((barx'−A(t)y)_w|t,S_w)=o(logN)，w=N^{-θs0}，A boundedK。entropy删除conditionaltinyprobabilities给subpowerlists；S support Kw^{-d}，选charttime t*及long-durationlines，≤Kw^{-d} value/slope binpairs。exactaffineevolution给全unit预测

barx(t)=b+F(t*)y+(t−t*)[b'+A(t*)y]+O(Kw)。

新labels disjointwholeassignments，丢lightlabels按旧chartprior denominator W_Ga0^d及countKw^{-d}得floor W_G(a0w)^d/K。a0w=a_s1，sameD0=a_s1^{u/(1+θ)}，故G(u)⇒G(u/(1+θ))。每次先对任意denseinput准备再调用假设，非单existential对象迭代；rawweightedλ和indicatorρ双向comparison最后乘回。

## 19. endpoint的真正labels，不仅指数极限

统一reconstructionbuffer：largestcoefficientamplification<=K/(D0a0)<=KN^{2smax}，firstjet所有test固定order，E减小只令必要widths变粗，不引入1/E深度；先固定大C0，再选smax使C0smax<e0/2。真base更fine积分不使用approxreconstruction。

α0=(1-d)/10000，u_j+1=u_j/[1+α0(u_j−2k)]从u0=1严格降、始终>2k，差公式 (u_j−2k)(1−2kα0)/(1+α0(u_j−2k))>0，limit=2k。对给定denseinput、每finitej先做完finiteiterations，晚N使log K_j/logN<1/j、mass≥N^{-1/j}、buffers全过，再j(N)慢增。无所有inputs共用的uniformdiagonal承诺。

D_j=a_s^{u_j},D*=a_s^{2k},R_j=D*/D_j=N^{o1}可发散。保oldpredictorlabels分开、wholeassignments按newD*grid split，oldcell遇boundednewcells；affineP predictor延伸newbox norm<=C K_j(1+R_j)。oldfloornumerator T_j=π(d0)D_j²a_s^d、ΣT_j<=K_j；newsplitnumerator R_j²T_j总<=CK_jR_j² subpower，重新删lightentries即有真正endpointfloorπ(d0)D*²a_s^d/K。不能把R_j当bounded或仅以u_j→2k就宣布G(2k)。

任意finite depths逐次对currentdenseinput重做，保earlierobjects；最后所有familyfloor加fullchartν^flat(H)floors同时删除，Σprior<=1/family。获得currentchartmass≥ν^flat(H)/K，故随后conditionaldenominator仍有效。G(2k)可对每subsequence/denseinput重新调用。

## 20. 9.6：offcritical的共同correction与三depth

固定s0 small，D0=h_s0²，group(d0,P_D0)。2k>1取H0=0,A0=1；2k<1取simultaneousG(2k)在s0,sb=3s0/2的fulltimeH0,Hb，A0=a_s0，配trueaffineL_s0/L_sb及whole-domainpairwitness。typicalchart fullprior与active质量都~W_G A0^d，ν_H固定。设R(t)=tildeP2−2t tildeP1，fiberW(t)=(1,2t)。

subcritical sharedtime G0=(D0/A0)∇P(calligraphic L_s0−H0)·W，被(D0/A0)∇P(Hb−H0)·W近似，误差<=K[D0/h_sb+(D0/A0)a_sb/h_sb²]<=N^{-κ}，κ=s0 min(k,1−2k)/4。第一项由wholechildboxnorm差KA0在centralhorizontal方向、第二项由Hb全parameterdomainnorm，saving分别ks0/2与(1−2k)s0/2。

须保alllinesmass：chartpairedlaw λ<=Kν_Hdt，time densitym(t)，M=∫m>=1/K。T0={m>=M/2}保≥M/2mass，某trajectory的pairedtime T_b⊂T0有|T_b|>=M/(2K)且Hb wholelabel固定。其quadratic time polynomial在T_b拟G0，Remez给coeffK。**restore同T_b全部pairedlines**，mass>=∫_Tb m>=M²/(4K)，非只保单trajectory。选Hcorr=(b0+b1t)tildeP1+(b2t/2)tildeP2，使∇Ptilde Hcorr·W=b0+b1t+b2t²。supercritical令Hcorr0。

取C=C_d+3，B*=min(s0/2,κ,ks0/(1+k))于subcritical，min(s0/2,(2k−1)s0)于supercritical；δ=B*/4，s=s0+δ，u=min(δ/4,kδ/(4C))，c2=(1-d)u/8，s_i=s,s+u,s+c2。Δ_i<=5B*/16给 subcritical D0/h_si≪a_si/A0、N^{-κ}≪a_si/A0；supercriticalD0≪a_si。因此 ∇tildeP[(calligraphic L_si−H0)/A0−Hcorr]·W<=Ka_si/A0。

## 21. offcritical scalar projection的cap与support分开

x°=(x−H0)/A0−Hcorr与R均affinealonglines、coeffK，terminalw_i=a_si/A0。maptildeP→(R,R') 的|det|=2（按(R,R')顺序det=+2）。σ_R=N^{-20s0}，原jointcap在fixedd0积分、xwidthA0ρ绕offset，beforedenominator ceiling Kπ(d0)σ_R²D0²(A0ρ)^d；若R'限制宽N^{-v0}再乘该width。dividechartprior~πD0²A0^d给8.2 c=1及positive angulargain。reconstructionerror(N^{-e0}+χ)/D0≪σ_R、所有offsetevaluationerror≪a_si，100s0<e0先留buffer。

support另用condition前storedwhole-domainwitness：在(t,R)cell取reference Z=p_c+tv_d,Y=q_c+D0R*−tp_c。contactdisplacement D0tildeP1(1,t)水平、D0≪h_si；真boxplane与referenceplane相差Kh_si，故整个truebox在commonvolumeKh_si⁴。supercriticalunitbasecap除m_Qsi给Ka_si^{-d}=Kw_i^{-d} labels；subcriticalpairedwitness近L_s0，bandceiling KA0^dh_si⁴除m_Qsi给K(A0/a_si)^d。这里绝不在conditionν_H下沿用原witnessfloor。

directionalcollapse让每affineentry可在tildeP=(0,R)评价到Kw_i；entrytime/R derivative<=KN^{5s0/2}，cellvariation≤KN^{-35s0/2}≪w_i，故每cell Kbins/entry，总σ_R²#<=Kw_i^{-d}。8.2 angular版给fulltimequadraticF_i(t,R)、β~1、conditionalactivefloor w_i^d/K。三depth在同chartensemble的dense restrictions上依次调用、共同renewfloors，不能选单tinyvelocitychart替globalmass。

## 22. 回到原Y、wideinterval和actual contradiction

按p=Z(0)宽χ split回α，P#=(pα,Y+tpα)。表达H0+A0Hcorr+A0F_i(t,R)在(t,Y)为quadratic（firstparameterconstant），wholelineerrorKa_si，movingintervalwidthβ_i=D0、normK。unslicednumerator T_i=πD0²a_si^d，per-slicenumerator t_i=πχD0a_si^d；每label≤KD0/χ slices，Σt_i<=KT_i，旧floors+disjointassignments支付新slice/currentfloors。

wide需要的conditioningstate=(Q_s,fine truebase,x)，不appendprojectedlabel；Koptions/history、referenceΣ<=KΣm_Qs，simultaneousfloors覆盖三slicedlayers和stateentries，除currentfloors后恢复finalconditionalπ。earlierwhole-domainwitness继续原law。β_i=D0<=g_s，且 b_s/D0=N^{-2k(s−s0)+o1}, h_sβmax/βmin=N^{-ks+o1}；Cu<=kδ/4<min(2k(s−s0),ks)，故§8wide全部strictmargins满足。

trueaffine L_s在centeredbox normK由active x bound及水平slope×h_s、transverse×h_s²所得。§9wide输出relativeQ_s mass>=H_sν^flat(Q_s)N^{-dc2}/K。restore q_desc=q_rH_s，ν_desc=ν_Qrν^flat(Q_s)，乘q_rν_Qr得原q_descν_descN^{-dc2}/K；w=L+a_rx给fullblockquadratic、widthKa_ra_s+c2、hidden derivative1。所有truepriors未以activeposterior替换。

由§8wide/strip-horizontal归约、critical§15、offcritical§22，原0<ell<infinity每subsequence每substantialresidual都有properpositivefinitegain candidate。AIM001是已审原4.11接口：wholetrajectorypriorityassignment先于derivativebadtime删除，原preparedprobability乘回p_prep，sameoriginalobservations/selected-test failure map，实际(K_path logN0)^C列表/geometry、预声明2^((M_path+n)^2)complexityguard、lateN0恢复，使actualsuccess>p_path/logN0，反原CRP extremality。此处引用其完整接口，不把analysisK当actualslack，也不另假parenttruefloor。

## 23. 审查边界与反攻结果（两实际全文独审通过）

重点攻击：abstract vertex替原edges、ratio0/coeffcancellation、独立化原g、旧witness冒currentfloor、tinygroup不付denominator、nonconstantcoefficientpairwrongoffsetcount、bilinear保axis后非法用旧conditionalcap、巨大affineL的fine-state循环、criticalC后验归一、signedJac/multiplicity、G(u)单existential迭代、endpoint只取指数极限、singleline代globalmass、ν_H下偷用旧wholeboxfloor。上面分别给原law/预算/量词解决；若独审发现仍有未付责任，停止整个分支认证并提前macro。

这份稿件只验证来源已有链及明确具名输入的应用，不解除2.17/finite-Hausdorff读出、新GWZ与KT未审责任，不证明fullsource、无条件DIM001或一般维度Kakeya，不声明新颖/重大。

正式全稿reviews：research/reviews/R0037_retained_edges_and_projection_review.md、research/reviews/R0037_horizontal_bootstrap_and_quantifiers_review.md；rootintegration为research/reviews/R0037_root_integration_review.md。三处记号/显示校准已核，未发现pending数学修正。
