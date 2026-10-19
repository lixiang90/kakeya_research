# R0103：原rich方向、全局Schubert集中与质量反攻

2026-10-19，B／lifting_obstructions。先实际读reselection5、R102原全局码与原WZ假设作资格筛查；随后root锁working5，本文全文读后在第4–6节独立核其有限正面施工。本人文件不是独立formal，当前不预授reviewed、newID／major或完整κ1／ordinary saving。Goal active，未经外部同行评审。

## 1. 恢复、原数据与本轮实际读取

实际读GOAL、当前STATE、ROADMAP当前完整路径表与历史停止记录、registry全部78项ID/status、R102 root十二节及next六节，另全文读R103 reselection／working两份各五节。较早已经实际全文审的R102两formal及旧轮source范围沿同会话保留，不重跑context、旧计算或Git。root父快照／clean／receipt由其恢复记录负责，本稿不自行认证。

本轮读回WZ2609.22035v1 Def17.1–17.4完整定义与Remark、19.2／19.4的原statement和相应CW证明、20.2原statement及affine情形实际输出(162)。源matrix33 κ1包括bounded F、δ-separated原time、dyadic Lip、native Y的AD1及tube-KT、filled horizontal X、每point的Φ AD1／slabγ与ξcoherence、原T joint4AD及whole-CW。SM是另有实际准备及原质量条件的结论，不能误写成Def17直接赠任意代数非集中。

R102已经付清并沿用：原H保L⁻C全T且保旧S_T；同一个P⊂R4为2-Frostman、|P|≈Lδ⁻²。原rich U上各u有大子集P_u≥L⁻C P，沿V_u=(imG_u)⊥投影cover≤L^Cδ⁻¹；I_u是真实原第三访问，I_u≤|H|，J=Σ_U I_u≥L⁻C N m。先逐管far，后point-heavy只平均，这个先后不改。本轮不再将这些已付对象作为欲证公设。

## 2. He实际primary：较弱的全局门和真实可用强度

实际打开[He官方history](https://arxiv.org/abs/1710.00795)及[固定v2原PDF](https://arxiv.org/pdf/1710.00795v2)，读PDF1–5的§1.1–1.4 statement／说明，未下载新PDF或认证其33页wholeproof。current v2为2018-05-09；所需是《Orthogonal projections of discretized sets》Th1，不是旧1611.09639矩阵sum-product定理。

其方向假设对所有互补维W、所有ρ≥δ控制det-angle事件：ν{V:d∠(V,W)≤ρ}≤δ⁻ερ^q。这里d∠是两组正交列基拼接的绝对行列式，亦为principal angles的sin乘积；不是到Schubert cycle的普通metric距离。Th1同时要求点集cover下界及弱Frostman，给near-full ν-good，且对每个大子集P′ robust投影增长。取n4、m2、α2，lower为δ⁻¹⁻ε，虽弱于CSWZ的接近二维，已足超过R102的一维像。

固定q∈(0,1/4)后先取得ε_H，再降为e≤min(ε_H,q/4,1/100)。He本身允许更大q；working收窄是为了第6节排除普通Lip二阶接触的平凡profile。减小e使源输入更强、输出更弱，故可合法统一用e。令全部L损失指数ℓ≪e：|P|≥δ⁻²⁺e，2-Frostman蕴含源所需q-Frostman，P_u≥δ^e P，而small image≤δ⁻¹⁻ℓ<δ⁻¹⁻e。P固定有界，homothety至unit ball及cover常数只付固定倍。因每个rich u已有坏P_u，任意支持这些方向的atomic概率都不能满足上述cap；不需uniform distinct parametercells或time→parameter有界重数。

He的global假设确比CSWZ local SPREAD弱，但没有从原Def17证明该假设。本轮锁后取反使用它，不将失败解释成固定公共kernel或全局有理F。

## 3. Schubert接近的精确native约束

记α=t−u、β=s−u、A=F_t−F_s，G_u=(α(F_u−F_s);β(F_u−F_t))。far u保证sminG_u≥rσ/2。对任意W∈Gr(4,2)，取正交列基B=(L;M)∈R4×2，上下blocks各2×2。normal V_u=(imG_u)⊥的det-angle恰为

\[
d_\angle(V_u,W)=
\frac{|P_B(u,F_u)|}{\sqrt{\det(G_u^TG_u)}},\qquad
P_B(u,F)=\det\!\left[(t-u)L^T(F-F_s)+(s-u)M^T(F-F_t)\right].
\tag{1}
\]

理由是把G_u乘Gram逆平方根取正交kernel基，W到该kernel的投影行列式与normal／W的拼接行列式相等。分母在c(rσ)²与C之间；不能用普通距离无费替换此product-sine。每G entry在(u,F四entries)中总degree≤2，所以P_B总degree≤4、系数upper固定。它是原F的det-cone约束，不是SM中的F≈Ru+U。

在F−F_s可逆、kernel graph Z=q(F−F_t)(F−F_s)⁻¹的chart，q=β/α，固定swap后literal projection参数θ=−Z。若只考虑model affine Schubert切超平面ℓᵀθv=c，消分母给

\[
\bigl[(t-u)c+(s-u)\ell^Tv\bigr]\det(F-F_s)
 -(s-u)\ell^TA\operatorname{adj}(F-F_s)v=0.
\tag{2}
\]

这里用(F−F_t)adj(F−F_s)=det(F−F_s)I−A adj(F−F_s)。一般He的全部Schubert cycles须用(1)，不能只测(2)的rank-one线性functional，亦不能倒说全部cycles在chart都是affine hyperplanes。近似形式还须保分母的conditioning。

## 4. 锁后：degree4关系的统一非真空性

working要求Q不能只是归一化零多项式；这一点独核如下。形式取u₀=(t+s)/2，不要求u₀属于原Z，令h=s−t、Z_F=F−F_t。此时

\[
G(u_0,F)=\tfrac h2\binom{-A-Z_F}{Z_F},\qquad
S(a,b)=(-A^{-1}(a+b),b),\quad
SG(u_0,F)=\tfrac h2\binom I{Z_F}.
\]

S⁻¹(c,d)=(-Ac−d,d)有固定norm upper，||S||≤Cσ⁻¹。令C_B=S⁻T B，则其两列的wedge norm≥cσ²，因为B两列正交而smin(S⁻T)≥cσ。于是

\[
P_B(u_0,F)=\tfrac{h^2}{4}\det\left[\binom I{Z_F}^{T}C_B\right].
\]

右端六个Plücker系数恰进入六个独立多项式1、四个Z_F entries、detZ_F。展开即可看出constant系数为C_B上两行minor、detZ_F系数为下两行minor，四个一次系数为cross minors，只有固定sign。该系数map有固定逆norm。因此P_B(u₀,·)的某系数≥c h²σ²≥cσ⁴。由u₀有界，代入u₀的系数norm至多是全变量系数norm固定倍；由F_t有界，Z_F↔F的translation同样固定有界。故

\[
c\sigma^4\le k_B:=\|\operatorname{coeff}P_B\|_\infty\le C.
\tag{3}
\]

这是所有正交B统一的finite-dimensional证明，不需要W固定、非zero-minor额外下界或Schur近解。设Q_B=P_B/k_B，则degree≤4、max coefficient=1、非零。由(1)，cap d∠≤ρ推出

\[
|Q_B(u,F_u)|\le C\sigma^{-4}\rho.
\tag{4}
\]

反向若仅知|Q_B|≤a，也只能由分母lower得d∠≤C(rσ)⁻²a，未消去conditioning。本文不把任意形式非零Q自动解释为一个Schubert cap，也不把多项式值的sublevel自动称为到其zero set的Euclidean距离a邻域；后者尚需梯度或独立稳定费用。

## 5. 任意剩余原访问概率的失败与disjoint剥取

在原rich U定义μ(S)=J⁻¹Σ_(u∈S)I_u，J=Σ_U I_u；同normal重复u的权直接pushforward，不删除重复time。对任意剩余R⊂U、μ(R)>0，其条件概率仍每个support方向都拥有实际坏P_u。若它满足He cap即与第2节矛盾。因此存在W及ρ≥δ使

\[
\mu\{u\in R:d_\angle(V_u,W)\le\rho\}/\mu(R)
 >\delta^{-e}\rho^q.
\tag{5}
\]

左端≤1，故δ≤ρ<δ^(e/q)，且所取条件mass>δ^(q−e)。从R₀=U开始，取cap的全部剩余clock为U_j后删除；每一步删除的是原time标签，不是另配几何像。当剩余μ至少1/2时，(5)给

\[
\mu(U_j)>\tfrac12\delta^{-e}\rho_j^q
 \ge\tfrac12\delta^{q-e}.
\tag{6}
\]

故至多2δ^−(q−e)+1≤Cδ⁻q个clock不交簇就使其union的原μ至少1/2。若假始终剩余至少1/2，每步的绝对lower累计超过1即矛盾，因而有限停止严格。相应B_j可各不相同，ρ_j也可各异；不能从全局cap失败选一个W并声它承载全部质量。每簇保的是原I_u权的绝对lower (6)，不是仅其自身重新归一的比例。

结合(3)–(4)，每簇实际(u,F_u)处于非零Q_j的厚层，厚度a_j=Cσ⁻⁴ρ_j。取4bq≤e/4并使固定常数由δ吸收，有

\[
\mu(U_j)\ge\delta^{-e/2}a_j^q,
\qquad a_j\le\delta^{e/(2q)}.
\tag{7}
\]

最细ρ_j≥δ确保没有免费sub-δ cap。所有a_j为真实δ-dependent normalized thickness，且随j的原mass不能省略。这是working锁定的正面集中profile；它不先假源方向具有非集中。

## 6. 非trivial cover的责任与原管marks返回

单独“少数非零低degree sublevel层cover一部分曲线”可能是平凡的dyadic Lip分窗，不能据此自认新结构。本文在资格时已向root提出这个警告；working补保(6)–(7)并收窄q是实质区别。实际原rich μ满足interval upper

\[
\mu(J_0)\le L^C(|J_0|+\delta),
\tag{8}
\]

因为I_u≤|H|、J≥L⁻C|H|m、Z δ-separated且m≥K⁻Cδ⁻¹。若用一个长度a_j≥δ的普通time窗口当簇，则mass≤2L^Ca_j，和(7)矛盾：q<1、a_j≤1、L^C≤δ⁻ℓ且ℓ≪e，所需δ⁻e/2a_j^q远大于该upper。

更强的平凡施工须考虑product-sine：取W等于窗心normal，在长度l的Lip窗中两个principal sines均≤L^Cl，故d∠≤L^Cl²。只用该通用upper保证cap时，可选窗长为带L费用的sqrt(a_j)量级；原质量upper至多L^Csqrt(a_j)。working q<1/4仍使(7)远大于这个数，因为q<1/2、a_j≤1且ℓ≪e。若取q>1/2则此profile可能已由二阶接触平凡产生，本文不使用该范围。这里不声真实cap只能持续sqrt(a_j)长：曲线沿某cycle运行时可更长。故本比较只排除这些通用分窗证书，不反任意Lip族出现集中，也不强迫单个公共kernel、共同image、全局有理F或曲率。

令U_*为这些disjoint簇的union，保Σ_(U_*)I_u≥J/2≥L⁻C N m。以原N／m作阈值：删除|S_T∩U_*|<J/(4N)的管最多损J/4，余管数至少J/(4m)≥L⁻C N，每根保≥L⁻C m个实际旧marks。实际U_*访问是point-heavy后仍存的边；若按所有原S_T∩U_*计只更多，不逆补新管。

这里只union有平均lower，随后heavy才有许多原T的逐管lower。单簇(6)可能仅固定幂小质量，不授每根T或每native pair都访问该簇，更不保证删后Φ／filledX ADlower或完整Def17。若对每簇重生源配置调用19.2／19.4，需另付其clock／参数／density和原允许尺度，本文没有这样调用。

## 7. 独立反攻：哪些输入仍不能给global cap

标量仿射F使G方向恒定，只否自动非集中，且原local affine准备会排它，不可当SM反例。更强的现成弱接口是R79已审rough上三角族：bulk F_u=uI−u(1−u)b(u)E12、anchors F₀=I、F₁=0，真实δ-grid time、global／dyadic Lip、每allowed窗口all-real local NF及native AD1/tube-KT、same X small actions、真实g和wholeclock直线同时成立。该原稿本轮全文读回，不继续其digit参数。

对该族任意锚，G上下2×2 blocks均上三角。取W=span(e₂,e₄)，其B^TG两行均为(0,*)，故P_B≡0于实际profile，全部normal law落同一Schubert cycle，任何正指数cap失败。这个例子确兼顾det-large两锚及上述time/NF/native接口，不是只global非affine的光滑二次曲线。但它缺全T joint4AD/CW、filled horizontal X2、pointΦ AD1/slab及selectedξ coherence，故不是完整matrix33或Kakeya反例，也不否本次从完整源取得的集中profile。

单个Schubert条件本来也不授固定kernel：例如仅令F全为对角矩阵、两对角各自变化时，det(F_u−F_v)可非零，而G仍在上述cycle；两方向quotient线随u各自改变。光滑版本不保local SM，只作代数范围检验。类似地near-cycle不能只由距离给出一条公共核线，必须区分两principal angles、u-dependent交线和完整源质量。

## 8. 原restriction、平均密度与双向排重

本轮用μ_R任意原访问条件化是He的概率输入，不宣该R是新完整配置。其输入点P始终同一个；R102的大P_u仍存在，因此任意条件化支持全坏。原T whole-index restriction保全部旧marks和绝对CW upper，归一constant要付N/N′；point／clock restriction则只保实际incidence，不能免费继承Φ ADlower、native lower或每管density。

若原开始只有平均λ=I/(Nm)，heavy |S_T|≥λm/2保至少I/2且N′≥λN/2，然后才有逐管门槛；CW概率费N/N′≤2/λ必须保。R102／103用的是已准备的heavy与det-large原分支，没有倒推任意ordinary族都有该分支。剥cap只平均保，§6的再次heavy重新付每管lower；平均、逐管、逐pair及逐cluster始终不同。

新global-profile并非旧CP⇔PM全称正gain改写：只有明确原多块码及原point-pencil的family可调用，未从任意CP对象重建完整source，反向亦未证。若只把“方向非集中”当欲证成功假设则仍不准开方向；working实际采用其失败，保每簇质量异常。R78的单块fractional稳定line／二次cone只有原δ²块及不同算子共同X输入，不提供这里全局原I覆盖和(6)尺度下界，不能混分母；但都不因此自动产生新的fullsource saving。

## 9. 四完整路线与未获准的升级

ordinary初始化仍缺在同一small-footprint族保方向、原ADlower／CW及marks的真实接口；R103不提供该入口。HRZ仍须全部父子、narrow及原norm主幂，不能以多项式厚层标签代actual physical carrier。sticky方面，本轮仅matrix33 det-large分支的必要global集中；其余rough、mixed42／43的实际contact与ordinary返回保留。真反例必须同一K含全方向单位段且strict Hausdorff低维，本稿没有这种集合。

R102的P2Fst／rich fibres已付，不重复命名；R74 AD0、R75 κ>1、R77双rank1、R78–80 action／跨块、R95平面饱和、R96 uniform polynomial及R97局部Segre停止均保持。尤其本轮Q_j degree≤4是原native profile的近关系，不是把F假为bounded-degree函数，不能借其名字重开R96。R97 local SPREAD的ε边界亦不被He global入口抹除。DIM001具名输入下17/4推论已付及priority层次沿R102保持，不以旧数表作本轮新增益。

## 10. 当前结论、实际交叉审查及停止线

第2–3节完成真实primary准入和native约束反攻；在实际全文working5锁后，第4–6节独核了He反用的disjoint集中profile、统一非零Q_j、每簇原mass异常及unionmarks重取manyT。已实际全文读root主稿十节及working最终q∈(0,1/4)修订，源单调、原分母、normal对偶、Plücker系数lower／absolute剥取、product-sine二阶平凡证书和union平均返回均未见必修。A终稿尚待其落盘后实际全文读，不提前记完整cross或formal通过；本人自证不计独审。

目前有限正面结论不是global cap，也不是固定kernel／有理F，而是许多可变Schubert厚层上的定量原访问集中。其后完整point／grain几何尚未付，故不续q／e／ρ常数或用新desired逆分类收轮。严格反攻只否上列免费桥，不反完整source。高级He33页wholeproof仍具名，本稿未新独证；无newID／major／novelty、完整κ1／ordinary saving或Goal完成。只分配文件编辑，无Git／metadata／下载／新代理，正式review另授权。
