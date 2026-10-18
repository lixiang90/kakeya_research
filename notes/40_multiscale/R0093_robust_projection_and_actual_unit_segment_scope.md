# R0093：稳健投影接口与真实单位线段校准

2026-10-18，Goal active。经典Cantor阻碍在真实五维单位线段接口上的逐步校准；非新维数界、非重大结果，未经外部同行评审。

## 1. 精确问题与一手输入

本轮问：单位线段联合参数Z⊂R4_a×R4_v的4-AD正则、完整方向及各球单方向大投影，甚至whole-tube convex Wolff计数，是否足以免费调用整流性定理？答案是否。原Def17完整κ1配置另有small footprint、marks、filledX与跨尺度信息；这里没有构造该全部输入的反例，也不否有这些额外输入的结构定理。

具名外部输入为Orponen arXiv:2008.08843v3，官方currentv3=2021-06-21，原PDF40页；body Date June22不是新版本。Def1.2的BP是每z,r至少有一个4-plane使投影H4≥ηr4；PBP要求同一球内所有距某中心plane小于η的planes均满足此界，η统一。主结论为Th1.6 PBP⇒BPLG，不是Th1.3。原文physical2–5明确给经典four-corners BP非PBP及单ball问题；不能把该旧例或本文改写说成新发现。本项目只核实际应用与下列构造，不新认证全部40页高级证明。

经典切平面/BF及areaformula按Lang作者讲义Notes on Rectifiability（Version December15,2023）Th10.6、10.8和8.3具名采用。root实际读physical31–33及21–22的相关statement，BF高级证明未重证；Examples10.9–10.10已明确给Cantor参数构造零体积Besicovitch集。讲义原35页已入库，非新research paper或新发现。

## 2. 数字对象、真正方向和联合AD

令A={Σ_{j≥1}α_j4^{-j}:α_j∈{0,1}}，B={Σβ_j4^{-j}:β_j∈{0,2}}，F=A×B。每位α+β恰遍历0,1,2,3，故A+B=[0,1]，均匀Bernoulli概率的和像为Lebesgue概率；终止/双展开只影响零测集，不影响集合满区间。F由4个ratio1/4且strongly separated的同形copies组成。F^4有256个ratio1/4的copies，level k质量256^{-k}=4^{-4k}，直径≈4^{-k}、不同cylinders间距≳4^{-k}。包含cylinder给球下界，球只交O(1)同尺度cylinders给上界，因此自然μ为4-AD；覆盖比较亦给μ≈H4|F^4，0<H4(F^4)<∞。

线性映射L(x,y)=(a,v)=(x−y,x+y)为√2倍正交映射（每一坐标对），故Z=L(F^4)为compact4-AD，π_vZ=[0,1]^4，π_vL_#μ=Leb4|[0,1]^4。对任一z∈Z和r，在含z的地址中取深度k使整copy直径≤r且4^{-k}≈r。该copy包含于B(z,r)，v像是边长4^{-k}的4-cube，故|π_v(Z∩B(z,r))|≥cr4。这是每球**同一个固定π_v**的真实BP；π_v与沿v坐标平面的orthogonal projection相同。不是PBP。

## 3. 纯不可整流的具体证明

F^4在R8中包含0和8个正坐标轴端点（x轴端点1/3，y轴端点2/3）。对任意affine4-plane P，这9点至少一点距P≥c>0：否则取逼近序列，平面法向/offset紧性给含9点的4-plane，与其affine span R8矛盾。由此取各点附近固定小半径的相对球，其μ质量有统一正下界；对每P至少一球整体距P≥c/2。任意cylinder内按相似缩放得到同一结论。

固定z及其level k cylinder，令R_k=C4^{-k}使该copy在B(z,R_k)内。对过z的任意4-plane P，每k都有≥cR_k^4的μ质量距P≥cR_k，且该质量处于B(z,R_k)内；故没有approximate tangent4-plane。若Z与某countably4-rectifiable集有正H4交，取交集的μ密度1点及其rectifiable approximate tangent，外部相对质量o(R^4)与上述统一远离质量矛盾。这里采用标准rectifiable tangent/differentiation定理，非仅“自相似所以不可整流”的断言。因此Z纯4不可整流。相同3点/2轴论证给F纯1不可整流、finiteH1。

若Z有PBP，具名Orponen1.6与标准BPLG⇒rectifiable将产生正H4 rectifiable交，矛盾。亦可用具名Besicovitch–Federer（finiteH4 pure4集的a.e.4-plane投影零）直接排除任一PBP邻域。只存在一个好的π_v完全合法。

## 4. 真实单位clock及有限δ管族

对(a,v)∈Z取S_{a,v}={(a+tv,t):0≤t≤L_v}⊂R5，L_v=(1+|v|²)^{-1/2}∈[1/√5,1]。其physical长度恰1，方向θ(v)=(v,1)/√(1+|v|²)，并有公共clock[0,1/√5]。a,v有界，(a,v)是这些单位线段的真实斜率/anchor参数，而不是自由矩阵模型。并集K紧：compact参数域上的连续像（以s∈[0,1]写t=sL_v）。方向含4维open patch。

δ=4^{-m}，截断前m位且尾取0，v逐坐标为{jδ:0≤j<δ^{-1}}，每个v有唯一α/β分解；N=δ^{-4}。θ在cube上双Lipschitz，故方向≳δ分离，角网格常数尺度等价，原无权方向law有四维上界及interior局部下界。联合截断族在δ≤r≤diam的自然计数归一化下4-AD：same cylinder质量与packing论证仍成立；不对r<δ声称连续AD。取这些段的round δ-neighborhood为管。全管shading Y_T=T，λ_T=λ=1，故失败不源于删去clock或平均质量损失。

## 5. Whole-tube convex Wolff计数的范围

以下只证标准containment形式 # {T⊂W}≤C|W|N，W任意convex body；不是所有coarse/marks/shading版本。管都在固定B_C。以W∩B_C替换W（无损包含且体积不增），John给ellipsoid E⊂W∩B_C⊂5E，半轴ρ1≥…≥ρ5。若没有contained tube，计数0；否则单位长度迫ρ1≥c，roundδ横截/端帽迫所有ρj≥cδ，且ρ1≤C。

contained tube方向θ满足各主轴坐标|θ_j|≤Cρj。δ-separated方向的δ帽不交；帽均落在增厚后的sphere box |θ_j|≤C(ρj+δ)。因ρj≳δ，在球面按|θ_i|≥1/√5分成5 charts，用其余4坐标参数化。每个实际非空chart还迫ρ_i≥c，结合ρ1≤C给ρ1/ρ_i≤C；于是每chart面积≤C∏_{j≠i}min(1,ρj)≤C∏_{j=2}^5ρj。帽增厚后chart可用较小固定阈值，结论相同。故数目≤Cδ^{-4}∏_{j=2}^5ρj≤Cδ^{-4}|W|，最后用ρ1≥c、|E|≈∏ρj≤|W|。N=δ^{-4}给所需计数。finite旋转补全方向若使用有限多个patch，只改变固定常数；patch证明已足以否该局部免费桥。

## 6. Lebesgue零并集：明确具名输入

对固定t，K_t⊂C_t^4，C_t=(1+t)A+(t−1)B；可变L_v只删slice点。C_t是F的线性一维projection再非零缩放。具名Besicovitch–Federer定理用于compact、finiteH1且pure1的F，给a.e.投影方向的Leb1(C_t)=0。t∈[0,1]映到方向向量(1+t,t−1)的angle为非退化光滑参数（导数非零且有界），故坏angle零集的t逆像为零集。Fubini用于compact K，得|K|_5=0。本步没有重证BF全部高级证明；与Orponen原文physical3–4所列经典输入分层，不是数值推断。

取方向patch的一个内部小cap，有限个orthogonal旋转可覆盖S4（compactness），令K_full为对应有限旋转K的并。它仍compact、Leb5零，且每方向含真实单位段。这是经典Besicovitch型对象的本接口校准；零Lebesgue测度不是低Hausdorff维数。

## 7. 满Hausdorff维的实际energy与覆盖证明

不给裸boxcount或仅调用未核Marstrand。令μ_F为F的自然1-AD概率。固定0<s<1，有I_s(μ_F)<∞，由layer-cake球上界Cr积分即可。对任意差向量h=(dx,dy)≠0及固定有界interval I⊂[0,1/√5]，

∫_I |(1+t)dx+(t−1)dy|^{-s}dt≤C_{s,I}|h|^{-s}。

证明：记a=dx−dy,b=dx+dy。若|b|≤c_I|a|，则|a+tb|≥|a|/2且|h|≈|a|；否则|b|≳|h|（若a较大且b不小亦可比），换u=t+a/b，I上|u|^{-s}积分统一有界，因s<1。对h积分及Tonelli得ν_t=(p_t)_#μ_F的I_s有限，对a.e.t成立。取countable有理s↑1，其共同full-measure t集上dimH C_t=1。

这些t上ν_t^{⊗4}承载C_t^4，且|w|^{-4s}≤∏_{i=1}^4|w_i|^{-s}，故I_{4s}(ν_t^{⊗4})≤I_s(ν_t)^4<∞，dimH C_t^4≥4s。公共clock内部t上K_t=C_t^4，取s↑1给dimH K_t=4 a.e.

最后付slicing：若H^q(K)=0、q>1，以radius→0且Σr_i^q→0的球覆盖K。球与t-slice的交只在长度≤2r_i的t区间存在、slice直径≤2r_i，故其(q−1)-cost对t积分≤CΣr_i^q。选可求和小的cover序列、Tonelli，得到a.e.t的H^{q−1}(K_t)=0。若dimH K<5，可选max(1,dimH K)<q<5，与a.e.slice dim4矛盾。因此dimH K=5，有限旋转K_full亦dimH5。energy、product和cover链为本项目实际核算，仍非新维数界。

令K_m为截断参数的整unit段并。连续unit段参数化对(a,v,s)在有界域Lipschitz，故K_m⊂K且Hausdorff距≤Cδ。固定倍邻域体积比较（δ网packing）给|N_δ K|≤C'|N_δ K_m|。因此这些whole-tube并虽因K紧且零测而体积趋零，却不能沿δ→0序列有任何固定幂upper Cδ^c、c>0：同尺度球cover将迫dimH K≤5−c。该有限footprint限制从实际逼近与cover付过，不只凭包含关系倒推下界；不声称任意partial shading都无small footprint。

## 8. 正向条件出口：整流参数确实给原并正体积

一个足够条件可精确写出。设Z'⊂R4×R4为有界Borel集、H4有限、countably4-rectifiable，π_v(Z')正Leb4，每个参数的原线段都包含公共clock[0,c]、c>0。则原段并有正Leb5。证明：取countable Lipschitz参数化q↦(a(q),v(q))覆盖H4-a.e.Z'；零H4遗漏的v像零。若所有charts在实际映入Z'的可测参数域上的Dv determinant都a.e.零，4维areaformula将使其v像均零，矛盾。因此一chart在参数集Q上有正测度且detDv≠0。可再限制到有界Q，保持正测度。对其Lipschitz延拓，Φ(q,t)=(a(q)+tv(q),t)的5-Jacobian是|det(Da+tDv)|，在Q×(0,c)内对a.e.q为非零最高项的4次多项式，至多4个根。故Jacobian积分正，5维areaformula迫Φ(Q×(0,c))正Leb5，且像在原并内。需在chart实际落Z'的可测子集上用公式；不能把延拓后整像计入原集合。

PBP+AD可通过具名Orponen与标准rectifiability给以上资格，但单个BPLG块的v像可能为零，不能直接假定它是a(v)图。本证明用全countable覆盖与真实方向像支付该点。定性正体积不提供finiteδ统一常数或δ正幂gain；若常数随δ恶化，不能套本定性出口结束ordinary Hausdorff任务。

## 9. Restriction、平均密度及等价排重

本轮反例有全clock和λ=1，亦有真实联合AD及whole-tube CW；所以为免费PBP桥增添平均或逐管正density不能修复。任意label删选虽保CW上界，不保联合AD下界、完整方向、BP/PBP；任意阴影删选更不保wholeclock或连续参数集。原N分母保留，不能把小子族重新归一化说原质量无损。即使逐管λ>0也不自动把整流参数出口的原段区间送入阴影；仅平均λ更弱，另需真实clock/Jacobian支持的返回证明。

本候选没有从旧CP/PM/PW全称正幂结论合法再调用得到新正幂估计，也没有证明反向推出旧结论；它是原结构是否足够调用具名整流性输入的资格测试，且在该范围为否。不可把PBP当“新的更强方向定理”登记，也不可凭本失败声称所有整流性方法无效。原smallfootprint等额外source输入的可能贡献仍open。

## 10. 本轮判定、停止与完整Goal

可保留的实际信息是：经典数字对象同时落在真实5维unit-clock、联合4-AD、局部固定方向BP、δ方向网格和whole-tube CW接口，却纯4不可整流；该免费PBP入口失败。其并集零Leb但满Hausdorff5，不能证伪Kakeya。条件rectifiable参数正体积出口已具体付Jacobian，不把未付PBP藏作成功前提。

不增加78项registry的数学ID，不宣ordinary维数改善、完整branch saving或major，不清零保守streak16。停止此固定projection→PBP的邻域/数字/密度参数续改。下一须完整四路macro重选：ordinary真实多尺度初始化、directHRZ全费用、sticky完整κ1/余mixed和ordinary桥、同一full方向严格低维构造；R92算术单轨道与R91PDE/free-normal3仍冻结。Goal active；完成两独立actual全文有限审查和档案/精确同步后才记录本轮结束。
