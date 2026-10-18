# R0081：从低维挂谷失败到紧致不交全方向直线族

2026-10-18，root阶段II整合。先锁spec§2后施工。重构Keleti（joint Gáspár/Máthé）2026-04-20 BME讲义PDF15–18报告的已有归约；未预判紧致不交族不存在，无新维数界/ID/major。root/A/B与两formal已实际全文独审，所列相对归约限定通过，未经外部同行评审。

## 1. 精确命题、来源与独立输入

固定整数n≥2。令D=RP^(n−1)，Q=[0,1]^n，X=Q×D，采用其固定有界product metric。记Kspace为全部非空compact K⊂X且π_D K=D的code sets，Hausdorff metric。对code(p,e)令ℓ(p,e)为过p、无向direction e的**无限直线**，S(K)=⋃_(p,e)∈Kℓ(p,e)。

本稿的自包含相对命题是：若存在s<n−1及一个residual集合G⊂Kspace，使dim_H S(K)≤s对所有K∈G成立，则存在可数compact straight-line families C_1,C_2,…，每个direction map像为全部D，且∪_i C_i中任意两条**不同**直线互不相交。每个C_i还可取其union dim_H≤s。

唯一高级具名输入为Keleti–Máthé arXiv2203.15731v3 Th1.1、Lem2.1/2.2的typical-minimality：若存在任一Besicovitch变体B、dim_H B=h<n−1，则上面可取s=d_n≤h，G为typical最小维全线union的residual。原文全参数code space在text261–295真实给出，不从四维dim_H statement倒推，也不本轮递归重证其wholeproof。Baire category定理及compact Hausdorff hyperspace基础为标准输入。

这是原报告的证明核验，不是本项目新归约。fullcompact不交问题仍open；其不存在才由逆否命题给普通dim_H≥n−1，不给满维n。n6的目标≥5才超当前4维种子后果；本稿未获得此no-family结论。

## 2. 完备空间、canonical line quotient与closed unions

X为compact metric，非空compact subsets的Hausdorff hyperspace完备（亦compact）。π_D对Hausdorff metric连续，故π_D K=D是closed条件；Kspace非空、closed、完备，是Baire space。任意nonempty relatively open U⊂Kspace与任一residual集合相交。

为避免同一line被不同p重复编码，写e对应orthogonal rank-one projector P_e=v v^T。令

    a(p,e)=(I−P_e)p， q(p,e)=(a(p,e),P_e)。

q为canonical line map，在X上Lipschitz；ℓ由(a,P)唯一决定，Pa=0。取line metric d_L((a,P),(b,R))=|a−b|+||P−R||。C(K)=q(K)compact且K→C(K)对Hausdorff metric连续，π_D C(K)=D。raw codes不同但同一line时d_L=0，不可把它们当自交的不同lines。

S(K) closed：若x_j→x、x_j∈ℓ(p_j,e_j)，由K compact取(p_j,e_j)→(p,e)∈K；incidence方程(I−P_e)(x−p)=0在极限仍成立。S(K)∩bar B(0,R) compact，因此S(K)是σcompact。这同时处理intersection可能远在原Q外的wholeline责任。

## 3. 固定compact障碍的avoidance是open

固定compact B⊂R^n，定义A_B={K:S(K)∩B=∅}。若K_j∉A_B、K_j→K，取w_j∈K_j及x_j∈B与incidence。X、B compact及Hausdorff收敛给子列w_j→w∈K、x_j→x∈B；incidence闭，故K∉A_B。于是A_B在Kspace中open。

等价地，code good set V_B={(p,e):ℓ(p,e)∩B=∅}为X中的relatively open，K∈A_B正指K⊂V_B。这里使用B compact，不把不交wholeline误写成只在unitsegment上不交。B为空时全部Kspace。

## 4. fixed-B密度：真实有限code网与全部方向

再假对每个e∈D，π_(e⊥) B在e⊥内empty interior。因B compact，这些projection均closed nowhere dense。给原K∈Kspace、目标ε>0。

对任一(p,e)∈K，先在Q内选距p任意小的interior p0；其小open ball U⊂int Q的projection π_(e⊥)U是open。可选p′∈U使π_(e⊥)p′∉π_(e⊥)B，故ℓ(p′,e)避B，且p′任意近p。由§3 good-code openness，固定p′并缩direction neighbourhood V_e，可使{p′}×V_e全部good且距原(p,e)小于ε/3。

为保Hausdorff的两侧：先对K的一个finite ε/3-net分别选这样的good code (p_i′,e_i)，把这些isolated codes保留。另一方面，为每个e∈D选原K中的一个(p_e,e)，作上述construction；V_e覆盖D。由compactness取finite subcover，再取finite closed direction caps D_j⊂V_(e_j)且⋃D_j=D（例如Lebesgue number/有限更小球）。令

    K′={这些finite good net codes} ∪ ⋃_j({p_j′}×D_j)。

K′ compact、π_D K′=D、所有codes good，且d_H(K,K′)<ε。每个新增code在旧K附近，旧K又由net近似；未将finite direction net当full directions。这证明A_B dense。

若dim_H B<n−1，则所有π_(e⊥)B的Hausdorff维数<n−1，故确empty interior。因此所有这种fixed compact B都有open dense A_B。

## 5. σcompact障碍、局部position盒与合法独立选择

若F=⋃_m B_m、各B_m compact且dim_H B_m<n−1，则A_F=∩_m A_(B_m) residual（Gδ dense），不宣open。特别若L∈G，S(L)∩bar B_m compact、dim≤s<n−1，因此A_(S(L)) residual。

给任意small open ball U⊂int Q，集合V_U={K∈Kspace:K⊂U×D}是nonempty relatively open：{p}×D见证非空，compact subset在open U内有正margin见证开放。故可在任意这样的位置盒中同时选

    L∈G∩V_U∩⋂_(j<k) A_(S(L_j))，

只要前面有限个L_j∈G已实际选定。其所有S(L_j)是此时**固定**的σcompact障碍，Baire合法；L自身dim≤s。不可把fixed-B泛性直接套成B=S(L)并称无自交。该自依赖将在§8用finite pieces消除。

## 6. far-linepair的badset闭性及有界intersection

固定正整数j,R。令Bad_(j,R)为那些K，使存在ℓ,ℓ′∈C(K)，满足

    d_L(ℓ,ℓ′)≥1/j，且某x∈bar B(0,R)同时属于ℓ,ℓ′。

在K_m→K的bad sequence上，canonical line参数有统一bound（|a|≤√n），交点x_m在compact ball；取子列并用q与incidence闭性，得到极限bad witness，line距离仍≥1/j。因此Bad_(j,R) closed，O_(j,R)=Kspace∖Bad_(j,R) open。

intersection可随m逃∞，所以不能仅靠‘无限两线最短距离连续’跳过R；本证明在每个R先compact化，末尾交全部R。parallel不同lines自不交；coincident raw codes被d_L≥1/j排除。

## 7. density所用的小pieces与closed direction caps

给任意K、Hausdorff精度ε及j，取τ>0使C_q τ≪1/j且τ≪ε，其中C_q为§2的固定Lipschitz常数。取finite τ-net{(p_i,e_i)}_(i=1)^m⊂K。direction e_i的τ-balls覆盖D；取closed caps D_i（半径2τ即可），每个含e_i且⋃D_i=D。

把p_i移动至距离<τ的interior p_i*，选nonempty open ball U_i⊂int Q、半径≤τ、且所有p∈U_i距p_i<2τ。对任意L_i∈V_(U_i)，限制

    L_i^*=L_i∩(Q×D_i)。

该限制compact、direction像正为D_i；每个code距(p_i,e_i)≤Cτ，故q(L_i*)的line-metric直径≤C_q′τ<1/j。它可以有内部相交lines，但它们的参数距离全小于本次badpair阈值。这里只取closed direction restriction，任意非closed selection不免费保compactness。

## 8. 真正消除内部自依赖的finite拼块

依§5逐个选择L_i∈G∩V_(U_i)，并使S(L_i)避开所有先前S(L_k)，k<i。每次非空open position盒与finite/countable residual相交，所以可选；没有把互不相容的泛性声明当自动独立。令K′=⋃_i L_i*，这是finite compact union，π_D K′=⋃D_i=D。

任何K′ code距一个旧netpoint≤Cτ，反之旧netpoint(p_i,e_i)由L_i在direction e_i的真实code近似，故d_H(K,K′)≤Cτ<ε。若K′有distance≥1/j的两个canonical lines，它们不能同属一个piece；若来自不同pieces，则其whole unions已实际不交。因此K′∈O_(j,R)，甚至对所有R均成立。

于是每O_(j,R) dense。finite pieces的数m可依ε,j而变；这是Baire存在证明，不是无损finite mass界、也不将其叫δ^o(1)费用。位置在cube边界的旧codes已由§7内移付Hausdorff误差，未假position盒必须中心正好原p_i。

## 9. 同一residual里的内部不交全方向族

令R_disj=∩_(j,R≥1)O_(j,R)。由完备性及§6–8，这是dense Gδ。对K∈R_disj，任何两条distinct ℓ,ℓ′∈C(K)有d_L>0；若相交于x，则选j足大使1/j≤d_L、R足大使|x|≤R，反O_(j,R)。所以其全部distinct lines两两不交。

G∩R_disj仍residual且非空；任选K得到compact全方向C(K)、whole union dim≤s和内部不交。没有先为每direction单独选择一个line再取closure；所有方向始终在同一个compactcode中，closure不会新加未核的交线。

## 10. 可数多个族及全体cross-disjoint

递归选K^(1),K^(2),…，使

    K^(r) ∈ G ∩ R_disj ∩ ⋂_(i<r) A_(S(K^(i)))。

每个先前S(K^(i))是dim≤s的固定σcompact set，其avoidance residual；与G、R_disj相交仍非空。令C_r=C(K^(r))。每个compact且direction像全D，内部distinctlines不交，且新whole union避前面全部wholeunions。所以∪_r C_r中所有distinctlines两两不交；相同line若出现在两族会相交，亦已被排。

这些族不由简单translations获得：任一全方向wholeline union S与S+v必沿direction v的某条line重合（v=0时更平凡），所以无论v多小都不能用平移制造cross-disjoint。本证明每次在完整code space中重选真实minimal族，不依赖错误的平移泛性。

## 11. 反攻、量词与不合法推广

严格阈值必须保：B是一个(n−1)-plane中的closed disk，中心在int Q，dim_H B=n−1；近中心且近法向的lines都会穿B。code K0={中心}×D附近有必须穿B的codes，所以A_B不dense。不能把s<n−1放宽到s≤n−1。

fixed B非compact时§3的compactwitness证据失效；例如single-line空间中B={(k,1/k):k≥1}闭而无界，x-axis避B，但y=1/k的parallel lines趋x-axis却碰B。这一小例只校准全线hit关系的非compact风险，不冒full-direction Kspace反例；本证书对σcompact F仅用countable residual，已足。

source允许arbitrarycompact多fiber，不给continuous selector、每direction唯一、code manifold、Lipschitz inverse或semialgebraic性。restriction仅finite closedcaps拼全方向，保compact和directioncover，非任意shading闭包；没有mean/逐管/逐pair密度概念可偷移。CP/PM/PW4全称positivegain不与此qualitative还原双向等价，亦不能由本稿导finitegain。finite计算/图示不替代Hausdorff或Baire证明。

## 12. 文献状态、终点与完整目标

本归约来自Keleti 2026 BME讲义15–18已有主张；本稿实际补fixed-B density、self-dependent internal避交的finite拼块、canonical distinctline事件及所有j/R同一选择。Keleti–Máthé2203.15731v3最小维/typicalitywholeproof具名，不因本稿而声其已全文新重证。新Slides21页另存版本/字节，报告与内部证书分层，未经外部同行评审。

这不排任何维度的fullcompact disjoint family，不证明dim≥n−1、n5满维或一般满维；若将来某n排这些族，才由具名最小维输入及本归约得该维度dim_H≥n−1。原Slides19–20 closed构造仅明确R3及相似odd维，不能当compact反例或全n theorem。

两独审须实际全文核§4与§8密度构造、typicality输入、line quotient、事件闭性及可数递归；发现任何gap则保精确未付项，不改成continuous/unique较弱问题结案。实际两formal及root整合已限定通过，仅此具名输入下核心内部reviewed；无新ID/major/priority。旧onefull/KT闭包拒题保留，完整Goal active。
