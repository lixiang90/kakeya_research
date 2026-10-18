# R0087：原质量、精确类闭包与全 G4 停止范围终审

2026-10-18，B。内部独立逐步审查，未经外部同行评审。全 near-contained G4 未证、未否；不新增数学 ID、major 或 ordinary 高维增益。

## 1. 实际全文对象、来源与独审层级

已 fresh 实际全文读 root8 `notes/40_multiscale/R0087_full_G4_factor_scope_and_projection_boundary.md`（含§7最后固定格式半代数U的whole-containment查询）、A8 `notes/40_multiscale/R0087_full_G4_singular_transfer_attempt.md`、B10 `notes/40_multiscale/R0087_full_G4_original_mass_counteraudit.md`、working_spec5、macro6及next6；又实际全文读 root 新保存的 source scope6 `literature/notes/R0087_full_G4_and_downstream_source_scope.md`，其使用层级与本审查一致。本文主独审root/A；自己施工的B10不计为自己的独立审查，A/root已另实际核过该稿。

为核root新增接口，实际读FSD001 reviewed页、R29 A稿完整8节；读库存Wongkew1993 Main Theorem及相邻局部球/厚度语境和开头证明；读HRZ v1 Theorem4.1、Proposition4.2完整证明（含(27)和窄指数）及§8(51)–(53)相关上下文。复用已审R59/60与R85范围，未冒Wongkew或HRZ高级wholeproof本轮全部新独证、PDF视觉核或源字节新认证。DIR003/FSD001/G3及各半代数分解的高级依赖仍保具名条件。

## 2. 因子、原 clock、真实 marks 与尺度回传

root/A的factor归约逐步通过。Z(P)是各实不可约因子零集的有限并，重数无影响；每轴对每factor的距离≤Cδ时间集合有固定复杂度的存在公式，QE给统一有限一维分量。按全部端点细分后可给每开区间指定factor，未把逐点近零集并冒某factor的whole-axis containment。

两原球帽只占OδVδ，η<1可在每label先删而保≥λVδ/2。body的正交clock截面≤Cδ⁴，有限端点没有5D质量；故每label能保一段上≥cλδ⁴原marks，其clock长度≥cλ。首尾两条完整r子段覆盖长度在[r,2r)的区间，选其一不会把markcomponent质量免费当单位轴。每label只选一个原子段，权/标签无重复扩增。

原权选共同dyadic r层只损O(log(2/λ))；再按中点r格和factor分组，实体支持在有界重叠的C′r球内，Σ|E_g|≤C_D|E|，没有另付r⁻⁵格数。x=c_g+rx′后轴长恰1、round半径h=δ/r，实际marks体积缩放r⁻⁵；新density≥cλ/r，位置范围固定。新方向仍是原方向，而h帽需C r⁻⁴个原δ帽，故α_h≤Cαr⁻⁴，不能沿用原α。

真实Lebesgue回传因此为

\[
r^5 h^{4+\sigma}W_g/\alpha_h
\ge c\delta^{4+\sigma}r^{5-\sigma}W_g/\alpha.
\]

r≥cδ^η给h≤Cδ^(1−η)；η相对被调用η₀严格小后，cδ^η≥h^η₀且h在其小尺度范围，固定常数由δ₀余量支付。σ先小、η再小可吸r幂及log。低实维factor调用真实G3时亦保这些费用。因而“所有P”与“实不可约real-dim4 P”的正幂范围等价归约成立，条件是该余类本身有uniform结论；后者没有被证明。

平均版也单独过：heavy density≥λ_av/2保权至少λ_avW/2，α不归一且继承；用ε/2逐管结论、先η_av≪η_per再η_av<ε/4，才能吸λ_av的真权损。没有免费保原W/I、逐管门槛或全λ强型。

## 3. 精确轴、Wongkew local entropy 与旧 FSD 返回

exact containment才给P_d(v)=0。P_d非零齐次，在任何固定紧stereographic chart上的有理式清分母后是非零degree≤2D多项式；否则P_d在球面开集为零，齐次性迫其在R5开锥上为零，违反非零。图正反导数固定，不依系数条件数。

Wongkew在R4、球半径Cr和厚度Cδ的上界，δ≤r时高阶δ^jr^(4−j)项均≤Cδr³。以分离小4球packing得到每个r角帽里的方向零集可用C_D(r/δ)³个δ帽覆盖；所有中心及δ≤r≤1都覆盖，不把总N≤δ⁻³当3-KT。奇点、重复因子和δ系数不改变该uniform degree-only bound。

root的weighted连续接口亦通过。有限着色方向bins后，每bin按w_i/(Cα)抽一个原label，总概率≤1；所得actual directions分离且全尺度3-KT常数固定。共享δ随机格每管总点≤Cδ⁻¹，真marks点数期望≥cλδ⁻¹，因此rich概率≥cλ、rich时有≥cλδ⁻¹个原marks。有限slots/clock处理仅常数，原端帽至多相邻有限bins，不偷填E。

FSD001的任意原条数版本给rich族有限λ²下界，实际markedcell数受真实E格点数固定倍控制；再对抽label及共同格取期望，rich原权的λ因子另计，得到保守

\[
|E|\ge c\delta^{4+\sigma}\lambda^3W/
\bigl(\alpha\log(2/\delta)\bigr).
\]

格点期望恰δ⁻⁵|E|，未用occupiedcell体积代理。η在σ后小即可得exact nearfull版本；权跨度及重复labels均没有额外未付费用。它是旧FSD001的统一再调用，不是本轮新方向，且不推出near轴方向接近原leadingzero。

## 4. A 的全类图形步骤和 whole-containment 边界

独核A的R5→R4多数投影/same-π finite global-Lip graphs链：对任意≤4维tangent strata可选固定有限多数good投影，低维递降保同π；所有near-S点pointwise属于大多数H_j。分别在真实T_i及Y_i上积分，确可为每label选同j保两者各至少常数质量，不假整轴在一张graph。normalfiber≤Cδ结合whole-volume强迫投影非短，端帽包含于Oδ项。

f_j=δ⁻¹fiber(E∩H_j)真实有界，投影管平均≥cλ；threshold和DIR格桥给带实际projected帽权A_j的结论。一般非短projection的逆帽可长一维，只有A_j≤Cαδ⁻¹的粗界，不能换成原α。该missing factor是固定幂，非任意小损。

root§7新增固定格式半代数U的whole-shadow containment计数也合法：P_i⊂U使原T_i∩H_j常数质量落入H_j∩π⁻¹U；后者格式固定、体积≤Cδ|U|，原PW/KR固定fraction查询经weighted sampling给Σw_i≤C_σ αδ^(−3−σ)|U|。凸U可用John外接box作固定格式包络。只允许固定格式测试，不许用复杂度随管数增加的并集。

但任意partial U截取P_i的clock片，不保证H_j好体积仍在那里；不能省原fraction费用。因此whole-containment不授partial/fullPW4、global angularcap或一般4D full-volume CW定理。McShane将已给的低dim projected载体提升成低dim原carrier是合法模块，却没有实际提取所需全族质量/递归分解。A/root明确保留这些欠项，没有用desired公设强制通过G4。

## 5. 实体反攻与 HRZ downstream 的实际强度

两桥例均逐式复核通过而不反G4。P=(x₅²−δ^Ax₁)/(1+δ^A)不可约且Sing空，合法unit近轴及其最近零点的梯度仍可任意小，故norm1/远Sing不授uniformδ^c梯度。P=(x₅−δ^A|x′|²)/(1+4δ^A)的exactline t²系数迫v′=0再v₅=0，Fano空；但S3水平δ-net供N≈δ⁻³合法近轴、cap O1及fullmarks，真实union≈δ。原leadingzero仅±e₅，原方向离它固定远。后者可由低degree平面近似修，故只否snap到原P/原leadingzero，不否所有正确近似机制。中心clock λ marks实际union≈δλ⁴，只迫η在ε后小，不否∃η版本。

HRZ源的窄吸收指数为e(p,n,k)=(n−k+1)p−(n−k+2)，原Prop4.2需要正值；n5、k≥3时门槛至少4/3。经原Lp读出dim>4需p<4/3，不能只换一个terminal就穿过这个既有窄阈值。k2没有这一同样阈值，但其它真实terminal/parent尚未支付。G4 nearfull结论亦不自动给全λ sharp L^(4/3)。局部r段、原coarse帽、parent重复和算法的actual wholebroad对象均须另收费。root没有据此宣所有HRZ方法不可能或本轮有globalgain。

## 6. 必修状态、限定通过与最终停止

当前没有未解决的强制修正项。root8/A8的全部整合和具体查询边界已实际逐式通过；B10末尾的“待稿落盘”是施工时的历史状态，终审实际读取在本formal补全，不作为当前数学缺口。本文自己的factor/校准施工不计自独审，已由A/root独核。

在上述具名依赖及有限归约/旧输入应用/specific反攻范围内，root8/A8/B10、spec5、macro6、next6全文通过。准确结论是fullG4仍未证未否，不可约只是等价范围，exact类是旧源闭包；停止generic图形/CW4接法，不续不可约换名、D/κ/λ/低degree或新quadric小改。macro/next的四主路余责、streak10及未锁合格后继均未冒Goal完成/blocked。

本轮无newID、major、ordinary高维增益或完整source反例；未经外部同行评审，具名高级wholeproof未新完整认证。不预认证未来metadata、Git、远端同步或状态归档。完成本formal后停止编辑和检索。
