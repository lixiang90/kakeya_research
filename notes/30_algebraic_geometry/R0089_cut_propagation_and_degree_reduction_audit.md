# R0089：全维cut传播、原访问质量与五维降次数尝试

2026-10-18，A；按R89 working_spec五节锁题施工，恰十个编号节。目标是完整原H5的真实低degree/coarse用途，不附tube-star横截、全局multiplicity、ADlower或四hop mixing成功假设。以下支付可证部分并实际回放降次数门；最终目标未证未否，未经外部同行评审。

## 1. 原任务、实际primary与符号

固定R、原R5单位round δ管Ti⊂BR，M≈δ^-4个原projective δ分离方向，Yi⊂Ti可测，E=∪Yi，I=Σ|Yi|，逐管density≥λ≥δ^η。反设|E|≤δ^(1−γ)。令L=δ^-1表示inverse physical scale，不与原管数M或source每管访问数混淆。锁题问：对任意小ε，能否取γ,η足小，得到degree≤δ^-ε的非零cut模型，承载固定正比例真实incidence，并付后继coarse4D调用？

实际全文读working_spec五节、R56 root十节/A十三节的本门范围；本轮新源[Guth1402.0518v1](https://arxiv.org/html/1402.0518v1)实际读intro Hyp0.2/Prop0.3/Th0.4/0.5、完整§1及§2.2（Th2.2、Lem2.3–2.5全部证明），并读§3 Th3.1/3.2和相关投影面积段。已对照root归档的local extracted PDF8–17等对应文本；没有重新渲染PDF或独立bytes验证，没有全文重证§4高级曲率graininess。

原source §1 fixed n工具确可取n5；主Th0.4/Th2.2字面R3，不能换维引用。Stone–Tukey ham-sandwich、标准relative isoperimetric／面积公式仍明确具名；下文具体根计数和原质量账自行给出，不以作者或论文标题替代。

## 2. 真Lebesgue阴影到同一格／原incidence的归约

取共同随机b∈[0,δ)^5，格Gb=b+δZ5。令Kb=#(E∩Gb)，Jb=Σi#(Yi∩Gb)。因Ti固定长、半径δ，逐管格点数≤C0L，所以Jb≤C0ML，而

    E_b Kb=δ^-5|E|， Jbar:=E_b Jb=δ^-5 I≈λML。

在这里λ也可定义为原平均密度I/(M|Ti|)，逐管输入只是其特例。用阈值

    Kb≤4(C0ML/Jbar) E_b Kb≤Cλ^-1 δ^-5|E|               (1)

定义good phase。Markov给bad概率≤Jbar/(4C0ML)，于是E[Jb1good]≥3Jbar/4。可选同一个good b使Jb≥Jbar/2。再剔逐管格访问< Jbar/(8M)者，只损≤Jbar/8。剩余真实H保

    JH≥3Jbar/8≈λML， |H|≥cλM，
    cλL≤ji:=#(Yi∩Gb)≤C0L，
    Kb≤Cλ^-1δ^-5|E|≤C L^(4+γ+η)。                    (2)

所有grid marks均是原Yi实际点；不拿NδE作E，不由measurable小体积直接推cover小。以每个E格点为中心取sideδ cubes，再放大δ^-1得K=Kb个unit cubes X⊂B_(CRL)。每原selected incidence(i,Q)只计该中心属于Yi，cube确交相应radius1、长L round tube。固定fat tube包整个cube的费用只是维度常数，原正向/端帽点均可用，未删真端帽。

(2)保的是原有subpower比例和同一格上的真实质量，不声仍有完整方向网，也不把单一格结构自动当原全部Lebesgue marks的逐点结构。若最终有合格finite contradiction可另沿原期待桥返回；当前只把这些实际计数作为数学输入。平均版已用总I支付，不假每原label都为重管；后续restriction均重记M′=|H|、ji及JH。

## 3. 全ambient scale-cut的存在：没有leading conditioning

以下r_c∈(0,r_5)是固定几何cut精度，与原δ/coarse半径不同。source Def1.1要求每个cube附近dist≤r_c^-1内、半径r_c..1的所有球B满足P>0体积为(1/2±r_c)|B|，强于只bisect一个cube。

为实际实现，用side c_n r_c²的更细lattice cubes近似这些球，覆盖X的C/r_c邻域。其数量≤C_n r_c^-a_n K。对它们施Stone–Tukey：若该数<dim Poly_D(R5)，有非零P同时二等分全部小cube。球内未被完整小cube覆盖的边界层相对体积≤C_n r_c，调整常数得所需scale-r_c cut。由dim Poly_D≈D5，可取

    D≤C r_c^-A K^(1/5)。                                (3)

这就是source Lem1.3/Cor1.5的全n内容；fixed r_c时常数固定，若让r_c随δ变小，r_c^-A及后面r_c^-20必须另付，不能藏为固定常数。P的cut不依赖系数大小或原近点jets的condition number，确避R56抽topform的具体指数费，但(3)本身仍不是目标δ^-ε。

## 4. Lemma1.6的完整全n传播与坏gap量词

把radius1 tube写为T={|y|≤1,z∈[a,b]}，n=5，π(y,z)=y。取相隔≥2n的unit cubes Qj∩T≠∅，其轴向中心hj有固定正gap，定义相邻segments Tj。假P cuts每Qj at r_c。对a.e. y，纵线π^-1(y)不整含Z(P)，故至多D个zero；整含Z的y集合是非零系数polynomials的共同zero，measure0。

令R_c=n+r_c^-1。由于相邻hj分离，扩大segments N_(R_c)Tj的pointwise overlap≤C(R_c+1)；横投影落radiusO(R_c+1) ball。根计数和Fubini给

    Σj |π(Z(P)∩N_(R_c)Tj)|≤C_n D(R_c+1)^n。             (4)

把投影measure>c_n r_c^(2n)的segments列bad，得#bad≤C_n r_c^-4n D（实际粗估已足）。对good Tj及其接触cube Q，取测试球B半径2r_c..1、中心距Q≤(2r_c)^-1；沿轴平移到hj得B′。B′在Qj的r_c^-1邻域，已近二等分。在不碰Z(P)的纵线上符号沿连接区间不变，B与B′截面长度相同；余下纵线投影measure≤c_n r_c^(2n)，其体积远小于r_c|B|。所以B也近二等分，得P cuts Q at2r_c。

这只覆盖所选first/last Qj之间的good gaps，不覆盖更外clock。最关键的是#bad=O_(r_c)(D)，不是bad轴长或bad原访问质量O(D)。若一个bad gap承载大量原marks，不能直接删去不计；下一节source正为此另作random spacing和global平均。

## 5. R3两跳source究竟如何付原质量

Th2.2在R3要求每管Nvis..E0Nvis个cube、每cubeρ..E0ρ根管、每cube对每比较方向有E0^-1比例的E0^-1横截管。它不要求Hyp0.2的全空间最高multiplicity或三方向条件；后二者属更后graininess，不能混写成同一输入。

源取D=K0|X|/Nvis²，K0是E0与目标ε的足大固定幂；约K0^-1/2 D²根随机种子管，每根选约K0^1/2D个按原访问次序等量分段的cube。HS约束总数≈D³。Lemma1.6让每seed tube仅O(K0^+D)坏segments；每segment按原访问quantile含≈Nvis/(K0^1/2D)个cube，因此seed坏cube总质量真小，而非仅gap数小。

第二跳不是无条件独立：近乎平行tube可能连续命中许多cube。源先只留E0^-1横截事件、在原访问序列取间距≥C E0的cube（固定着色可消字面常数）；同一横截tube不能影响两个这些事件，Bernoulli选择才独立。这个真hypothesis支撑长空档的exponential tail，继而保证任意O(D) gaps只带很少原cube访问。seed bad对其它tube的误差另按全部T′平均、用每cube的ρ upper付；不声每固定T′都已保留。

最后source cube-degree可比才把多数tube的保留转为多数X；要保原incidence亦须把错误fraction乘其实际E0。不能把定理的1−ε cube比例免费读成1−ε原weight。源E0若为δ的固定逆幂，Poly(E0,ε^-1)就可能吃掉degree优势；不同层的原M/Nvis/I及实际几何/selected边必须明写。上述全proof已实际读，不重新证明所有Guth论文高级内容。

## 6. 从原H5到source输入的实际匹配与失败测试

(2)已经给原访问行下界与总JH；一行上界C0L使行比最多C/λ。它没有给cube列degree可比、逐cube的常量横截fraction，也没有给全空间tube multiplicity upper。按列degree的dyadic层挑可保一部分J，但可能让许多行失去其原访问；再tube-heavy、再column-layer必须真付迭代并以原J作分母，不能把结果预先称满足Th2.2。

原方向δ分离只在全局angular cap给至多C(θ/δ)^4根管；一个局部star即使有很多原labels，也可集中在θ趋零帽内。此量词本身不授对每比较方向E0^-1角分散。不能以几个方向张成、poly足够大或局部补重复管代替；若经角尺度分解、横向rescaling改善，必须保original marks／footprint与所有尺度倍率，不能引用一个未付multiscale初始化。

还要区别原marks边与全部几何intersections：填Ti∩E不增并集，可作某些体积论证，但新边的多重计数不能冒原JiQ或Φ/CW prior。本文HS/下一节能直接对原selected edges工作；源两跳及最终coarse回传的均匀性不能因此免费继承。

## 7. 可证的原质量hyperplaniness，及其准确层级

有(2)的同一finite原incidence图，不加上述技术假设，也能证一个标准正向应用。取(3) fixed-r_c P。可取其odd sign-boundary的regular4维部分Σ；squarefree化/去不影响符号的因子不增degree，singular residual无H4质量。每Q中心小球被cut，relative isoperim给H4(Σ∩Q内球)≥c。记此不交部分ΣQ、单位法向n(z)。

对原selected edges i∼Q，设c_Q(n)=Σ_(i∼Q)|n·vi|。取一个regular point的法向nQ，使

    c_Q(nQ)≤C∫_(ΣQ)c_Q(n(z))dH4(z)。

每Q只有有限选择，不需可测selector。Q接触Ti时ΣQ位于同轴fixed-fat tube T_i^fat内。纵向面积公式与根数≤D给

    ∫_(Σ∩T_i^fat)|n·vi|dH4≤C D。

奇异纵线仍measure0，fat tube transverse4-volume固定；lengthL及round caps不增加该上界。求和得到真正原图账本

    Σ_Q Σ_(i∼Q)|nQ·vi|≤C D M′，M′=|H|≤M。             (5)

令πQ=nQ⊥（通过Q中心）。对任意θ>0，坏角原edge数≤C D M′/θ。由JH≥cλML，取θ≈sqrt(D/(λL))得坏原edge比例O(θ)。以(3)/(1)估算，可取

    θ≤C λ^-3/5 δ^((1−γ)/10)。                           (6)

η最后足小可令其为固定δ正幂。它只对实际选定grid的原edges给mass-averaged 4-plane，不授每cube uniform或每管所有old Lebesgue点。此为ham-sandwich/Crofton已知工具的实际应用，不能把standard hyperplaniness当完整本门成功；尤其πQ沿同管可变，尚无graininess／coarse4D出口。

## 8. 真正尝试降degree：两跳预算与四hop未闭环节

若形式上把上述seed方案推至n5，degree-D参数空间≈D5，seed预算是约D4根管×D cut constraints。即使先给最有利的均匀横截与spacing，原Nvis访问图的第二跳期望尺度只约

    Nvis² D4/|X|。

要远多于D个独立可用cut cube，仍需D³≳|X|/Nvis²，另有实际技术常数；不是R3字面D≲|X|/Nvis²，更不是D≲|X|/Nvis4。这个只是该算法的必要账本，不在本稿宣n5主定理已经证明。

在有利均匀模型|X|≈L^(4+γ)、Nvis≈L时，候选degree尺度L^((2+γ)/3)仍不是任意小ε。相较切大部分X的Crofton最低可期degree |X|/L4=L^γ，两跳离最优仍有固定幂。此对照不声任何合法输出一定需此degree，原题γ可在ε后小，也未把upper |X|当lower。

实际也尝试四hop：将原有限incidence图的point→tube→point核按degree正规化，以原edge marginal νQ为reference，得到reversible Markov核P。它确有∫P^k f dν=∫f dν；更多walks的raw数目不自动给更多distinct、原time分开的cut witnesses。非线性的cut激活仍需每tube远多于D个好cube及任意O(D) gaps的原mass控制。直接CS或总walk数没有付这一threshold，也未付同一seed反复影响的相关性；不能把此stationarity观察本身当新结果或给mixing公设后声闭合。

这个缺口还可作一个严格但仅限算法的有限证书。为避免与原M混淆，局部记二部图有J_c个tube rows、K_c个cube columns，row degree在[M_c,2M_c]，column degree在[ρ_c,2ρ_c]，所以J_c M_c≈K_c ρ_c。不同两row共有columns至多B_c≥1。独立以概率p≤min(1,cD⁴/J_c)选seed，甚至先赠每个seed整row全部columns都已certified，比真实P传播更有利。

固定未seed的row i。它接触的其它rows至多(2M_c)(2ρ_c)≤4M_cρ_c；条件i未seed后，其它seed indicators仍独立。因此邻seed数X_i被Binomial(⌊4M_cρ_c⌋,p)支配，已certified的hit columns至多B_c X_i。令a=ceil(D/B_c)、μ=4M_cρ_c p。在b:=e B_c μ/D<1的范围，Chernoff和union bound给

    Pr(存在非seed row至少D个hit columns)
      ≤J_c (e B_c μ/D)^(D/B_c)
      ≤J_c (C B_c M_c² D³/K_c)^(D/B_c)。                (7)

第二式使用p预算及J_c M_c≈K_cρ_c；常数必须保，邻row数不能由上述端点界字面写成2M_cρ_c。实际充分条件是log J_c+(D/B_c)log b→−∞；例如b≤δ^c0且D/B_c≫log J_c足够。这时高概率没有第一个非seed激活；任何只以“已certified graph intersections达到D”触发、之后再传播整row的有限／无限代闭包都停在初始seeds。若还要实际seed数≤C D⁴，E #seeds≤cD⁴，Markov与(7)合用可同时选出这样的seed realizations，HS的O(D⁵)约束预算不变。

(7)仅说明这个独立随机seed、graph-certified阈值算法没有自动多跳改进；不排其它seed分布、P偶然cut未命中columns、真实非均匀几何或其它传播见证。原δ-separated近角rows的B_c可达O(δ^-1)，D/B_c≫log J_c并非原H5已知输入；所以不能把该证书当本题反例，更不能由它宣所有四hop不可能。它只精确阻止把“增加代数”本身算作免费的K_c/M_c⁴收益。

近角pair可用几何共享cube≤C/angle估，但全方向网仍不授后续每层条件图的常角量。当前没有把这个四hop尝试推进成保原J的uniform低degree theorem；明确未证，不用弱graph模型否H5，也不以加更多hop／anchor续下轮。

## 9. 最终coarse4D用途仍缺的是真几何，不是常数

(5)–(6)给πQ的逐点原mass，未控制πQ在同一tube/coarse packet的变化。R5 tangent4-space的Sym²有10维；非零形式u1²−u2²的null directions也能张成R4。故仅局部多方向／span大不迫第二基本形式小，不能把源R3三方向曲率步骤照搬。本文不把这个有限代数校准升级fullsource反例，也不添加good十元组或quadric-spread条件。

即使某段有coarse4-plane，要调DIR4仍需该共同投影保原direction帽、完整actual shadow/clock及原N/I；逐cube的变化平面不够。高degreeD随δ增长时fixed-format几何工具的常数也不自动uniform；不能把P的Z当旧R59/60固定degree G3或R85regular-leading输入。切割cube意味着零集有真实面积，不意味着整轴contained或每label穿过同一个良态graph，旧G4／projectedCW4门没有因此完成。

因此本轮主目标degree≤δ^-ε并有原coarse调用质量仍未证、未否。只得到generic HS cut、真实mass hyperplaniness和已知source的准确条件范围，不把它们作普通n5新界或“已提取所需graininess”的替代。

## 10. 依赖、实际尝试结论与待交叉核

已付§§2–4的原sampling/cut传播及§7原图directed-area应用，§5按实际source完整proof核其row/column/横截/坏gap返回；§8实际回放二／四hop并指出没有获得新原mass及最终degree的具体位置。R56的leadingfee已被新cut工具绕开，但这并不提供本题所需的高维graininess。完整H5不是由旧bush反例否定，当前新门也不能靠proper技术假设宣完成。

按preset停止无原四hop/coarse质量的本次直接接法，不续degree/λ/ε参数或以wanted输入开方向。现已actual全文逐式读root十节《R0089_original_shadow_cuts_degree_budget_and_graininess_boundary》与B十节《R0089_original_incidence_and_graininess_counteraudit》。独核root共享格/原边分母、§5近biregular peeling、physical directed-area和两跳／有限graph账本；B的固定degree真实长bad-gap例、splitquadric实体II反攻与binomial(3)均通过其明列范围，未发现强制修改。A自身施工已由B/root独立核，自己不把本稿自证计作独审。正式review及终macro/next尚待授权和actual全文读，不预记外部wholeproof认证、metadata或Git/sync。仅授权本稿，无新代理／下载／元数据或Git操作，无newID/major/ordinary增益；Goal active。
