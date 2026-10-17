# R0037：horizontal 临界率、参数 bootstrap 与宽区间回传

2026-10-17，独立审查 B。实读原 §9 全文（PDF137–153/提取7333–8254），以及实际调用的 5.2/5.4、7.7、8.4–8.9、4.10/4.11 statements 和相应 proof 接口。官方 `08-critical-rates.tex` 用于校正公式。本文完整审 §9，前置 §7/8 几何定理由另稿/root逐步支付；不以本人后半审查自认证完整正有限分支。未经外部同行评审，不称新高维定理。

## 1. 唯一命题、同一原输入与闭包

假原 version2 tangent parent 已合法进入 Prop8.5 的 horizontal alternative，k=ℓ∈(0,1]，原 critical dimension 0≤d<1，固定角 palette π 有正指数 interval upper。relative a_s=N^{-s}、h_s=N^{-ks}，全轨迹满足

\[
Z=p+tv,\quad Y=q_0-tp+O(N^{-e_0}),\quad P=(p,q_0),
\quad |x|+|x'|\le K,
\]

x=(w−L)/a_r 沿轨迹 affine；prime 始终指完整 Q_r-time，不是 child unit time。固定 full prior ν♭=ν(.|Q_r)，current raw law μ≤Kν♭dt。true descendants 的 full assignment weights、block length H_s∼h_s 与 reference budgets为

\[
\nu^\flat(Q_s)\asymp_{\log}h_s^3a_s^d,
\quad m_{Q_s}=H_s\nu^\flat(Q_s)\asymp_{\log}h_s^4a_s^d,
\quad\sum m_{Q_s}\le1.
\]

引用的(8.3)是在同raw law上、所有预备fixed-power网的pure/joint caps；(8.5)和旧whole-domain pair witnesses也固定。目标：每subsequence及每substantial residual都在further subsequence产生proper Def4.10 time candidate，再由已审AIM转actualcontradiction。任何新selection仅保cap/support upper；current floors需重新收费，ν♭及早witness不因selection重置。

本文停止于完整9.2/9.5/9.6链及原质量回传通过，或保上述实际hypotheses的gap；不以generic increment、抹掉g/clock或重命名G(u)代替该任务。G(u)是同一bootstrap的中间性质，不登记新方向。

## 2. 真实依赖与同时floor

§9使用：8.5的horizontal equation/whole tilted domains，8.6–8.8 affine fits/fine states/nested slopes，8.9 every-dense-input full-time coefficient counts；7.7 affine–skew row fit；ISO已审5.4 scalar-normal first jet及其named WZ输入；UNB已审8.2；ASM/Cor3.4；8.4 three wide intervals；AIM actual conversion。9.1本身是2.11固定threshold peeling，不是主要新增增益。

对当前质量M≥1/K与finite label families，先固定threshold numerators总和≤K。删任何不足T_j/K₁的整entry并重复，每entry永远empty最多收费一次，故总费用≤ΣT_j/K₁≪M。finite grids慢增时先各fixed family完成再对角。这个lemma可同时保old当前floors、new predictors和history-state floors；旧referencewitness仍可独立保存，不要求其成为最后law的submeasure。

## 3. 临界2k=1：从evaluation lists到affine primitive

选small固定s，100s<e₀并预备s+c、3s等深度，a=a_s=h_s²，0<c<ks/2。8.9取D=a，given Q_s、精细centered z与v，p由Z−tv恢复，q₀由Y+tp恢复至K H_s²=Ka；故group(d₀,P_a)、time subbin及x_a只有K项。8.9遂给x′_a的K-list，仍为完整Q_r-time导数。

较深fit L_{3s} 给 x′=G_*·(1,v)+O(Ka)，G_*=∇_zL_{3s}+(∂_Y L_{3s})Jz，|G_*|≤K；微分误差a_{3s}/h_{3s}=a^{3/2}≪a。深history附(Q_s,z_ξ,[G_*]_a)只K ambiguity，按原referenceweights删light，得到conditionalvelocity≤Kπ。每row state有separated velocity pairs、palette product mass≥1/K；每pair的两evaluation lists以线性插值只许K row bins。对palette product求和给每position K个G_*_a选项，不能仅以“有两个方向”免费断言row有限。

在Q_s，fine z-cell的physical area为(H_sξ)²，transverse范围K H_s²，x只K个a-bins；(8.3)给raw joint≤K H_s⁴ξ²a^dπ。除m_Qs∼H_s⁴a^d得Kξ²π，且该law受K times conditional true prior×centeredtime支配。7.7可用，得G_*=B+λJ((z−z_c)/H_s)+O(Ka)。令

\[
F_*(z,Y)=(B-\lambda Jz_c/H_s)\cdot z+\lambda Y/H_s.
\]

由Y′=Jz·(1,v)+O(N^{-e₀})，|x′−dF_*/dt|≤Ka；N^{-e₀}/H_s≪a。F_*普通斜率可K/H_s，不假initial tangent中的全局系数K。

## 4. 临界intercept：原current law三次切换

a′=aN^{-c}，trajectory intercept c_l=(x−F_*)(t_mid)，C=[c_l]_{a′}。整块 x−F_*=c_l+O(Ka h_s)，而a h_s≪a′。因此足够精细真实base/x-state恢复K项C，8.7允许这些state精度超过horizontal error；不把近似(9.1)硬用至任意精度。

旧nested true descendants Q_{s+c} 的总数≤K(a/a′)^d(h_s/h_{s+c})⁴；每whole domain在centered Q_s的volume≤K(h_{s+c}/h_s)⁴，affine entries每finebasecell只给K intercept bins。因此(baseω-cell,C)占用总数≤Kω⁻³(a/a′)^d，ω例如N^{-5s}并留全部evaluation buffers。

以同一law的reference-weight pruning准备 switching state=(C,精细base,x)，保 μ_last质量≥m_Qs/K及conditionalvelocity≤Kπ；其probability μ̃=μ_last/m_last在centeredtime上≤K times frozen true trajectory prior×dt。丢 trajectory marginal density<1/K₁ 的lines只损≤1/K₁；good lines的conditional time density≤K。

每次先按当前state resample完整event，再按其整个indexed trajectory resampleevent，三次均为同μ̃的heatbath，保持μ̃和C。路径上的good/regular限制只乘indicator，**不重归一transition kernels**。fresh roundedcontrol c_i/time τ_i 在全past给定下的good subkernel≤Kπ⊗dτ_i，所以joint control/time law≤Kπ³dτ₁dτ₂dτ₃。stationarity、π intervalcap及goodline time upper使 |c₂−c₁|、|c₃−c₂|、|τ₂−τ₁|≥1/K′ 的失败概率o(1)。

忽略o(ω) simulationerror，signed traversals满足 dZ/dτ=c_i、dY/dτ=−Z+τc_i。令D₁=c₂−c₁、D₂=c₃−c₂，固定start与controls：

\[
Z_f=Z_0+c_1(\tau_3-\tau_0)+\sum_{j=1}^2D_j(\tau_3-\tau_j),
\quad
Y_f=Y_0+(-Z_0+\tau_0c_1)(\tau_3-\tau_0)+\sum_{j=1}^2D_j\tau_j(\tau_3-\tau_j),
\]

\[
\det\frac{\partial(\tau_3,Z_f,Y_f)}{\partial(\tau_1,\tau_2,\tau_3)}
=2D_1D_2(\tau_2-\tau_1).
\]

regular set上det有inverse-subpower lower。固定τ₃,Z_f后内部times在非平凡line上，Y_f是degree≤2；若该restriction恒定则无regular solutions。因此regularfiber≤2，即使c₃=c₁使二次项退化也不失效。change-of-variables加上述原subkernelupper给endpointcell probability≤Kω³，uniform in start/control；signed timeincrements合法，不必ordered times。

各C的conditional路径失败率e_C只有全weighted平均o(1)，不假uniform。保e_C≤1/2的bins占质量1−o(1)，每个占用≥(2Kω³)⁻¹ basecells。与upper count比较，#C_good≤K(a/a′)^d；故一个C有原raw质量≥m_Qs(a′/a)^d/K。其wholeblocktest恢复为 w−L−a_r(F_*+c_C)，hiddenderivative1、curvature0、widthKa_ra′。乘q_rν(Q_r)回initialtangent，得到原9.2 mass；除actual childblock q_desc=q_rH_s后即Def4.10的ν_desc N^{-dc}/K。每步可对任意substantial residual重做。

## 5. G(u)真实量词与9.4比较

2k<1时，固定共同s_max、directiongrid χ≤N^{-e₀}。G(u)对**每个**固定0<s<s_max及每个dense input/其subsequence，在further dense restriction给whole-unit-time predictors H(t,P)，参数group D=a_s^u、full disjoint assignments、每label active floorπ(d₀)D²a_s^d/K；H affine in P，coefficients affine in t，scaledgroup normK。它不是只对某一个先选输入成立。u=1由8.9的heavy ordinary affine coefficient bins给出，predictor可无P dependence。

9.4先准备true depths与old pair witnesses，再对该dense input取G(u) labels。对G=(d₀,P_D₀)、timeblock I，两色individual reference numerator T_GI=|I|π(d₀)D₀²a₀^d。full-time色的thresholds以Σ|I|=1及旧floors求和；true色每Qs₀,d₀只需K h_s₀³/D₀²个P bins，D₀≤h_s₀²保证meetingbins也在enlargement内，故ΣT_GI≤K。保individual marginal witnesses，不以稀疏pair-law质量替其floor。

P→(p+tv_d₀,q₀−tp) determinant1；reconstructionerrorK(χ+N^{-e₀})远小所有实际查询网。用共同tiny-cell jitter实现index-base≤K T_GI的精确density。若normdifference M₀/a₀有positivepower，则按邻jet bins分groups，storedfloors与near-representative x_{M₀} cap给每色≤K(M₀/a₀)^d indices。references总和K，选badmass≥(W₁+W₂)/K的group；normalize时分别用color weights T/W_c，成本W_c/B≤K。Cor3.4排除，得whole product norm≤Ka₀。

givenH₀,I，所有true entries的stored witnesses落在其Ka₀ graph band，individual floors相加给K-list。deeper L_s−L_s₀ norm≤Ka₀用的是提前冻结的full-child pair witnesses及affine Remez，后条件化到H₀不需新floor。

## 6. 一步bootstrap：固定ν_H与integrated→instantaneous

目标s₁，取s₀=s₁/(1+θ)，D₀=a₀^u，W_G=π(d₀)D₀²。用9.4选每H₀/timeblock一个paired L_s₀。restorefloors及删poor successfraction后，full assigned prior ν♭(H₀)∼W_G a₀^d。始终固定ν_H=ν♭(.|H₀)，λ_H为当前incidence除这个prior，而非换新trajectoryprior。

设 y=(P−P_c)/D₀静态二维，x̄=(x−H₀)/a₀沿line affine、range/slopeK，F(t)=∇_y(L_s₀−H₀)/a₀为time-only boundedrow，S=x̄−Fy。取E=(u−2k)s₀/10>0、ζ=N^{-E}。先积分jointcap得到 λ_H(I,yr,x̄_w)≤K|I|r²w^d，r,w≥ζ。

λ_H=f_Hν_Hdt，δ_H=λ_H(all)≥1/K。先留f_H≥δ_H/2，得indicatorρ_H⁰及 (δ_H/2)ρ_H⁰≤λ_H|E⁰≤K_preρ_H⁰；这提供双向比较，不从单向domination倒推prior cap。再删line/timebins中labelduration<|I|/K_dur的对，费用≤1/K_dur及K_pre/K_dur。time partition足细使K|I|≪ζ，则某时刻constraints对该line的整retained portion仍在enlargement内，durationfloor除积分cap给

    ν_H{active at t, yr, x̄_w in bins}≤Kr²w^d.

此后只restrictlabels，ν_H保持，所以instantaneousupper可用。任何返回weighted λ_H的保留indicator质量只再损subpower。

## 7. S支持、F比较与coefficient-bin conditional cap

对s=s₀+s′、w=N^{-s′}、0≤s′≤E，原full-domain witnesses在H₀条件化之前冻结。compatible childboxes在同referencehorizontalbox，pairedLs₀-band总ceilingKh_s⁴a₀^d；每child witness floorh_s⁴a_s^d/K，所以≤Kw^{-d} children。L_s−L_s₀的parameter variation acrossD₀≤KD₀/h_s²，其中

    D₀/h_{s₀+E}²=N^{-(10−2k)E}≪ζ≤w.

故 S(t)只需Kw^{-d} bins。按support数删instantaneouslight S-bins、mixedcap求任意S_r interval的mass≤Kr^d，得hereditarycount K(r/w)^d；后restrict仍保uppercounts。

若|t−t′|≤r而M=|F(t)−F(t′)|≫r，shared-line prior weight≤K(r/M)^{1−d}：source S_r bins Kr^{-d}、nearby target bins K(M/r)^d、差方向projectionwidthKr/M只需K/(Mr)个y_r squares，每square/sourcebin成本Kr^{2+d}，乘积恰该幂。另一方面在r-intervals抽timepairs、Jensen给shared weight≥1/K。挑anchor并保|F−F_anchor|≤Kr、再取separated residueclass，finite-grid迭代给 F的K(|Δt|+ζ)比较。没有免费假源F Euclidean Lipschitz。

对slope比较，durationfloor先给每yr-group的(t,x̄) spacetime support≤Kr^{-1-d}。在固定ν_H下，以longlabelled lines的auxiliary prior除r²，mass≤K、coefficientballcap K w^d（w≥r），可在每dense putative light-bin residual上新用5.1，得heavy B_r=(y_r,affine x̄coeff_r)，currentfloor r^{2+d}/K。再准备(B_r,I_r) floor |I_r|r^{2+d}/K，Σthresholds有限；其整个旧subentry落于任一相遇spacetime cube的Kr enlargement，integratedcap给每cube K个slope options。

逐cube选一slope、取separated residueclasses并慢迭代，得Def5.2的residual-slope comparison；因y′=0，所比就是x̄′。ν_H(B_r)≥r^{2+d}/K作为prior floor在后restrict下保持，instantaneous q^{2+d} numerator除该floor给 (q/r)^{2+d}，即真正(5.8)。nestedgrids与subpower邻scale比处理插值，不把current incidence floor误作新的conditional probability。

## 8. first jet读尺度、单time选择与新wholetimepredictor

以上为原Def5.2的全部输入，j=2。对H_*=N^{-E/4}，ζ≪H_*³/K；θ=(1−d)(u−2k)/10000给

    θs₀=(1−d)E/1000 < (1−d)E/256.

因此w=N^{-θs₀}满足5.4的first-jet readout范围。A(t)与single-time restriction先固定，entropy H((x̄′−A(t)y)_w |t,S_w)=o(logN)在原ν_H×dt presampling后取labels。小conditional information只给subpower列表，需删tinyconditionalprobability events；S support再给每active time至多Kw^{-d} binpairs。丢短总labelduration lines后以averaging取一个t_*，保dense trajectory及labelled incidence质量。

按两bins b=[S(t_*)]_w、b′=[x̄′−A(t_*)y]_w作固定wholetrajectorylabels。exact affine evolution给

    x̄(t)=b+F(t_*)y+(t−t_*)[b′+A(t_*)y]+O(Kw).

此为affine-in-P且affine-time coefficients，scaledgroup normK，restoring H₀后thicknessa₀w=a_s₁，参数D₀=a_s₁^{u/(1+θ)}。每旧H₀仅Kw^{-d}新labels，旧denominator∼W_Ga₀^d，按sumthresholds删lightnewlabels，重得π(d₀)D₀²a_s₁^d/K activefloor。不是fix t_*后免费继承旧逐label floor。

重建误差只在积分/旧spatial evaluation处使用。最大基本amplification K/(D₀a₀)≤KN^{2s_max}，floor指数E≤s_max/10；first-jet fitting/powers全固定阶。可先取统一固定C₀、再取s_max使C₀s_max<e₀/2。u−2k趋零时相关floor变粗，常数/有限步数可增大但没有必须1/E增长的mesh exponent；更细真实base integration不再调用horizontal reconstruction。

## 9. 到达端点G(2k)，不是只取参数极限

α=(1−d)/10000，u₀=1、u_{j+1}=u_j/[1+α(u_j−2k)]。逐式有u_j>2k、strictly下降，且u_{j+1}−2k=(u_j−2k)(1−2kα)/[1+α(u_j−2k)]，故limit2k。

对给定dense input及target s，每个finite j先完成有限次bootstrap和subsequence，收全部loss于K_j(N)。后取N够晚使log_NK_j<1/j、retained mass≥N^{-1/j}并满足所有buffers，再令j(N)慢趋∞。这是针对**该input**的diagonal；不主张一个diagonal同时适用于所有possible dense inputs。

设D_j=a_s^{u_j}、D_*=a_s^{2k}、R_j=D_*/D_j=N^{s(u_j−2k)}=N^{o(1)}。保old predictor labels独立，即使同new D_*cell也不合并；按newgrid拆assignments，每oldcell只遇boundednewcells。affine predictor在newcell的norm≤CK_j(1+R_j)。old floor numeratorsT_j=πD_j²a_s^d的总和≤K_j；每split所需endpointnumerator=R_j²T_j，总和≤CK_jR_j²=subpower。重新删light splits，才得到真endpointfloorπD_*²a_s^d/K。

多fixeddepths要successively作用currentdenseinput，保旧assignments/witnesses；最后9.1同时恢复所有predictorfloors和currentfulltimechart mass≥ν♭(H)/K。后者numeratorsΣν♭(H)≤1，故conditionalprior denominator不靠免费继承。这证明可fresh调用、可同时使用的G(2k)，不只是u_j数值趋端点。

## 10. 9.6源公式校准及shared time polynomial

**提取文本的 s_b=32s₀ 是分数串行误读。** 官方08-critical-rates.tex明确 s_b=\tfrac32s₀。按32会使D₀/h_s_b=N^{30ks₀}发散；按真实3/2，两项savings正确。已向root反馈，不能把提取误读当源数学gap。

统一D₀=h_s₀²、P̃=(P−P_c)/D₀。2k>1以(d₀,P_D₀)group作chart，H₀=0、A₀=1；2k<1用G(2k) at s₀,s_b=3s₀/2，并比较trueentries。typicalchart的active及fullprior都∼W_G A₀^d，W_G=πD₀²；先删poor successfraction，保固定ν_H。设R=P̃₂−2tP̃₁、W(t)=(1,2t)，R-fiber方向正是W。

subcritical shared signal G₀(t)=(D₀/A₀)∇_P(L_s₀−H₀)·W，与某H_b对应quadratic time polynomial的误差为

    K[D₀/h_s_b+(D₀/A₀)a_s_b/h_s_b²]
      =K[N^{-ks₀/2}+N^{-(1−2k)s₀/2}]≤N^{-κ},

κ=s₀ min(k,1−2k)/4。L_s₀每chart/timeblock选定，使G₀对该chart所有pairedlines共享。不能只选一条line并保其tiny mass：若paired time densitym_H(t)、totalM_H≥1/K，先留m_H≥M_H/2，再由λ≤Kν_Hdt选一line的time setT_b长≥M_H/(2K)。该line的whole H_b label固定，其quadratic在T_b逼近G₀，Remez给coeffK；恢复**所有pairedlines**在相同T_b，质量≥M_H²/(4K)。

若该poly为b₀+b₁t+b₂t²，取H_corr=(b₀+b₁t)P̃₁+(b₂t/2)P̃₂，则∇H_corr·W恰该poly。supercritical取H_corr=0。不需要globalF时间正则性或一条line承担全部输出质量。

## 11. 三个深度的正margin与新scalar projection

C_d=10/(1−d)、C=C_d+3。取B_*=min(s₀/2,κ,ks₀/(1+k))（subcritical），或min(s₀/2,(2k−1)s₀)（supercritical）。令δ=B_*/4、s=s₀+δ、u=min(δ/4,kδ/(4C))、c₂=(1−d)u/8；s_i∈{s,s+u,s+c₂}，Δ_i=s_i−s₀≤5B_*/16。

subcritical directional errors除w_i=a_si/A₀后为 N^{-[ks₀−(k+1)Δ_i]}及N^{-(κ−Δ_i)}，均power-small；supercritical为D₀/a_si=N^{-[(2k−1)s₀−Δ_i]}。从而(9.5)精确为

    |∇_{P̃}[(L_si−H₀)/A₀−H_corr]·W(t)|≤Kw_i.

对R和x°=(x−H₀)/A₀−H_corr，两者沿line affine、coeffK。P̃→(R,R′) determinant magnitude2，truejointcap经originalspatial determinant1 map积分，在(t,R) σ_R=N^{-20s₀}格、x° widthϱ≥w_i的rawbound为KπD₀²σ_R²(A₀ϱ)^d；adjoinR′宽N^{-v}多N^{-v}，0<v≤s₀。除固定chartprior∼πD₀²A₀^d后，8.2输入prefactor1及positive angular gain真实成立。

支持另证：取R-cell代表R_*，reference Z_ref=p_c+tv_d、Y_ref=q_c+D₀R_*−tp_c恰horizontal。contact displacement为D₀P̃₁(1,t)+smallerror，D₀≪h_si；alignedtruebox整domain在同volumeKh_si⁴的box。supercriticalwholewitness仅需boundedx的unitcap；subcriticaloldpairedwitness near sharedLs₀，ceiling为KA₀^dh_si⁴。除childfloorh_si⁴a_si^d给≤Kw_i^{-d} entries。

仿射parameter预测沿W误差Kw_i，所以可改在P̃=(0,R)评价。true ordinary slopes≤KN^{(2k−1)_+s_i}，除A₀后time/R derivatives保守≤KN^{5s₀/2}；cellvariation≤KN^{-35s₀/2}≪w_i（w_i≥N^{-3s₀/2}）。D₀σ_R≪h_si²，且(N^{-e₀}+χ)/D₀≪σ_R；全部重建/offset误差在100s₀<e₀及预声明buffer内。故每basecell≤Kw_i^{-d} scalarbins，非仅mass ceiling。

8.2 optionalangular输出unit-timequad F_i(t,R)、每label conditionalmass≥w_i^d/K。三depthsuccessively对currentdense residual应用同一fixedν_H、同caps/support，保ensemble的dense总质量而非只保一个tiny chart；必要时fresh删poor conditional success，费用仍由chartprior预算支付。

## 12. 回真实坐标、α-slices与8.4输入

把p分χ-bin α，p_α为代表，用P#=(p_α,Y+tp_α)代替P。误差≤K(N^{-e₀}+χ)；H₀+A₀H_corr+A₀F_i经此代入为真正quadratic(t,Y)，在movingY interval宽KD₀、center q_c−tp_α 的scalednormK，wholeassignedlines误差Ka_si。没有把quadratic-in-parameter直接误认成原physical quadratic。

unsliced原floor numerator T_i=π(d₀)D₀²a_si^d；每p-slice需t_i=π(d₀)χD₀a_si^d=w_αD₀a_si^d，w_α=πχ。每oldlabel最多KD₀/χ slices，故Σslice t_i≤KT_i。以oldfloor/disjointness给ΣT_i≤K，再9.1重删light slices，三层floors真实保留，不按各slice免费分摊旧质量。

另外准备true Q_s+fine truebase/x conditioningstates，**不append projected predictor**。8.7给每deependhistory K choices，原references insideQ_s sum≤Km_Qs；与三projected layers一起9.1，恢复conditionalvelocityKπ。选择heavyQ_s不再改已含Q_s的conditional law。

三层β_i=D₀ upsubpower，β_max≤Kg_s（g_s=h_s），b_s/D₀=N^{-2k(s−s₀)}，h_sβmax/βmin=N^{-ks}。参数给(C_d+3)u≤kδ/4，两wide inequalities各有fixedpower余量，0<c₂<(1−d)u/4亦满足。true L_s lists的norm在centeredboxes K，jointcaps/palette/原time H_s、tiltedgeometry及fineprojectionmesh全部匹配8.4。subcritical在endpointG(2k)获得这些实际输入；supercritical不调用bootstrap。

## 13. 原质量、proper test及every-residual实际出口

8.4输出horizontal mass≥H_sν♭(Q_s)N^{-dc₂}/K与wholeblockquadfiterrorKa_s+c₂。提升时q_desc=q_rH_s、ν_desc=ν(Q_r)ν♭(Q_s)，counted原mass乘q_rν(Q_r)，得到q_descν_descN^{-dc₂}/K。再w=L+a_rx，test为w减一个proper quadraticbasepredictor，hiddenderivative1、curvature0，wholeblockhiddenupper/fit均合法。除q_desc后恰Def4.10 mass，gainc₂固定正有限，depth r+s保持bounded。

每次从给定subsequence/任意substantial原residual重新准备；uppercaps、旧fullprior/witness保留，current floors/poor-success/indicator-duration在该residual重新支付。G endpointdiagonal针对该input、finite三depth simultaneous-use及uniformsubpower chart调用均按此前量词，不偷偷取跨所有inputs共同diagonal。因而9.2或9.6 supplies AIM所需真正 every-residual propercandidate；AIM另在原observations/guard中完成actualconversion，本文不以tangentK冒actualslack。

本后半在所列前置几何/高级输入下闭合，目前未找到保全部原hypotheses的反例。本人的root整合 §§1–23及A前端正式全文独审已归档 `research/reviews/R0037_horizontal_bootstrap_and_quantifiers_review.md`；后半主稿本身不代替该独审。fullsource、finite-Hausdorff、GWZ/KT及无条件高维责任仍保留。
