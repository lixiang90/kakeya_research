# R0081：完整code空间、固定障碍避让与内部far-linepair的Baire证书

2026-10-18，A。先锁spec§2后施工。重构Keleti（joint Gáspár/Máthé）2026-04-20 BME公开讲义15–18报告的归约，不宣本项目新定理/ID/major或Kakeya下界。未经外部同行评审。

## 1. 精确相对命题和实际来源读域

固定整数n≥2，Q=[0,1]^n，D=RP^(n−1)。令X=Q×D，Kspace为非空compact K⊂X且π_DK=D，采用Hausdorff metric。S(K)为codes对应的全部**无限支持直线**之并。假存在s<n−1及residual G⊂Kspace，使每K∈G有dim_H S(K)≤s。目标是在同一原完整空间中构造K_1,K_2,…，每个全方向，canonical line images紧致，全部distinct lines两两不交，且dim_H S(K_i)≤s。

实际全文读锁题后的R81 spec5/macro6、新Keleti slides提取21页（15–18为主张/略述）、KM2203.15731v3的Th1.1及§2.1 Lem2.1/2.2完整原文。本相对证明仅具名使用：KM所给d_n是所有Besicovitch变体的共同最小维，且典型S(K)维数d_n。因此若任意普通Kakeya集合dim<n−1，可取s=d_n<n−1并获得G。未重证KM完整高级proof；slides公开报告不是外部peer-reviewed证明。

## 2. 完备性、全方向closed条件和residual的使用

X为compact metric，非空compact subsets的Hausdorff hyperspace是compact、完备。若K_m→K且π_DK_m=D，任取e∈D、从K_m取(p_m,e)，compactness给p_m子列趋p，Hausdorff极限含(p,e)，故π_DK=D。Kspace因此是非空closed完备子空间，Baire定理合法。

残余G不必自身是完备子空间，也不先假closed；按residual定义取dense Gδ集G0⊂G，以下用G0仍记G。对任意非空相对open V⊂Kspace，G与任意countable open dense条件的交在V内非空。这是我们使用的唯一泛性逻辑；不能由G dense便推出它与任意closed position子空间相交。

方向投影满D是每个code集的**原定义**，不是finite方向网近似后取极限的未证结论。hyperspace只包含非空compact objects，未把空族当极限选项。

## 3. canonical line quotient与whole-union σcompact性

用rank-one orthogonal projector P_e=vv^T表示无向e（不选全局连续unit向量）。定义

    q(p,e)=((I−P_e)p,P_e)=(a,P)， Pa=0，
    d_L((a,P),(b,R))=|a−b|+||P−R||。              (1)

这是affine unoriented line的canonical参数，两个codes有相同q当且仅当是同一无限直线。q在bounded X上Lipschitz，故C(K)=q(K)compact、其方向像仍为D。raw(p,e)可沿同一line重复；内部badpairs必须按d_L≥1/j，不能按raw-code距离。

若x_m∈S(K)、x_m→x，取其codes(p_m,e_m)∈K，子列收敛于(p,e)∈K；incidence (I−P_e)(x−p)=0在极限保留，所以S(K)closed。各S(K)∩bar B_m compact，S(K)是σcompact。此处不是只讨论code中点附近的unit pieces；所有相交点的可能位置都在后面按m穷尽。

## 4. fixed compact B的avoidance开放性

固定compact B⊂R^n，置A_B={K:S(K)∩B=∅}。若B非空，函数

    d_B(p,e)=min_(x∈B)|(I−P_e)(x−p)|

连续；若K∈A_B，compact K上的最小值正，故足小Hausdorff扰动仍避B，A_B相对open。等价地，bad序列的codes与交点分别在X和B中取极限给closed hit事件。B空时平凡。

这里compact B必要：单条x-axis避开闭无界点集{(k,1/k):k≥1}，但y=1/k的parallel lines趋它且碰点集，说明不能从无界不交直接得统一正margin。该例只校准局部hit关系，不冒全方向Kspace反例；σcompact障碍后面改用countable residual，绝不免费继承open。

## 5. fixed-B密度：位置内移、投影避让与closed全方向盖

再假每e∈D的π_(e⊥)B为空内点。B compact使此projection为closed nowhere dense。对任一旧code(p,e)和任意小ε，先在int Q选p0近p，再在其足小open ball U⊂int Q选p′，使π_(e⊥)p′不在π_(e⊥)B。因为π_(e⊥)U open，此选择确存在。于是ℓ(p′,e)避B；由§4的good-code openness，固定p′后有e的一个open direction cap V_e，使所有{p′}×V_e都避B且仍近旧code。

给任意K0∈Kspace，做两个独立有限步骤。第一，取K0的finite ε/10-code网，对每个netcode作上述扰动，保这些finite good codes以保证旧K0到新族的Hausdorff距离。第二，对每个e∈D选一个旧(p_e,e)∈K0并扰动；所得V_e覆盖D。compact D给finite subcover，Lebesgue number/缩球给有限closed caps F_i⊂V_(e_i)，⋃F_i=D。可让各cap在原V内且直径很小。定义

    K′={第一步有限good codes} ∪ ⋃_i {p′_i}×F_i。    (2)

K′ compact、全方向、避B。每个新code近某旧code，而每个旧code近第一步的net witness，故d_H(K′,K0)<ε。不能只以finite direction net代替第二步，也不能只cover directions而丢K0上同方向其他position fibres。位置内移处理cube边界，不假K0原来在int Q。至此A_B open dense。若dim_H B<n−1，则任意orthogonal projection维数≤dim_H B，故其内点必空，适用本lemma。

## 6. σcompact障碍与小position盒中的真实低维全族

若F=⋃_m B_m，各B_m compact且dim_H B_m<n−1，则A_F=∩_m A_(B_m)是dense Gδ（不宣open）。对每个已选L∈G，S(L)的compact truncations有dim≤s<n−1，因此A_(S(L)) residual。

若U⊂int Q为任意非空open小球，令

    V_U={K∈Kspace:K⊂U×D}。

它非空（{p}×D见证）、相对open（compact K到Q∖U有正margin）。故可在G∩V_U∩∩_(h<i)A_(S(L_h))选择新的L_i，只要前面有限个L_h已实际固定。每L_i本身**仍是全D方向族**，且whole S(L_i)维数≤s并避开先前whole unions。

这一步不把global residual G任意限制到一个closed子空间K(Q_i,E_i)。若采用KM的局部cube/compact-direction版也可从Lem2.2另推，但本证明不需要该额外topological论断。所有低维position localization直接来自非空open V_U，避免“dense集与任意closed盒都相交”的错误。

## 7. 有界far-linepair事件的closed性

固定正整数j,R，Bad_(j,R)由存在codesw,w′∈K及x∈bar B_R满足

    d_L(q(w),q(w′))≥1/j， x∈ℓ(w)∩ℓ(w′)            (3)

定义。K_m→K时，w_m/w′_m在compact X、x_m在compact ball可取共同子列；Hausdorff极限保w,w′∈K，(1)和incidence连续，所以极限仍bad。于是O_(j,R)=Kspace∖Bad_(j,R) open。

R不能略掉：交点可能随line参数趋近而逃∞，我们只在bounded intersection box中取compact witness。d_L阈值也不能换成两条线的最小物理距离，因为相交lines的该距离为0；(3)排的是canonical意义不同且分离的line参数。coincident raw codes永不被当两个different lines。

## 8. density拼块的有限code网和真实Hausdorff双向近似

给K0、ε>0及j，选τ>0使Cτ<ε且C_q Cτ<1/j，其中C_q是q在X上的固定Lipschitz常数。取finite τ-net {(p_i,e_i)}⊂K0。因为π_DK0=D，其direction τ-balls覆盖D；令D_i为以e_i为中心半径2τ的closed projective caps（包含e_i），则⋃D_i=D。

对每p_i选int Q内的非空open小球U_i，使其每个p距p_i<2τ、diam U_i≤τ。此选择在p_i位于边界/角时仍可内移完成。若L_i∈V_(U_i)，置L_i*=L_i∩(Q×D_i)。该restriction为compact，方向投影恰D_i；每code距旧(p_i,e_i)≤Cτ，所以canonical piece直径<1/j。

任何新piece code都近某旧netpoint；反之，对每个旧netpoint，L_i在原direction e_i中有一个真实code，其position在U_i，故旧netpoint近新piece。结合旧finite net即d_H(⋃L_i*,K0)<ε。这里并不要求common/unique selector；各D_i允许多line fibres、caps重叠亦无妨。

## 9. 内部self-dependence的完整消除

按§6逐次选择L_i∈G∩V_(U_i)，并要求S(L_i)避开全部先前S(L_h)。这是每一步对**已固定**σcompact障碍的Baire选择，而不是把fixed-B lemma套B=S(L_i)本身。令K′=⋃_(i=1)^m L_i*。

K′有限compact union，全方向，且按§8近K0。若其两条canonical lines的distance≥1/j，它们不能来自同一个piece（piece直径小于阈值）；若属于不同pieces，其原whole unions已由选择时严格不交。所以K′∈O_(j,R)，事实上同一次构造对全部R都有效。每O_(j,R)因而dense。

选择的piece数、避让margin及Hausdorff精度可以极坏地依赖ε/j/此前族；本证书不提供finite δ数量或subpower原质量，不能称它为uniform-shading gain。构造可另得dim_H S(K′)≤s（有限个低维whole unions的子集），但density只需O_(j,R)，没有拿这一点冒无条件open低维集。

## 10. 同一residual及可数个cross-disjoint全方向族

令R_disj=∩_(j,R≥1)O_(j,R)，由§7–9和Kspace完备，它dense Gδ。任取K∈G∩R_disj，若两distinct canonical lines相交于x，则其d_L>0，选j足大且R>|x|使(3)成立，矛盾。因此C(K)内部两两不交、compact、方向全D。

递归选

    K_i ∈ G∩R_disj∩⋂_(h<i) A_(S(K_h))。              (4)

每步先前K_h已实际固定，S(K_h)为dim≤s的σcompact障碍，故右侧residual非空。令C_i=q(K_i)。各C_i紧致/full directions/内部不交，新whole union避前面所有whole unions，所以全部i中的distinct lines两两不交；同一line重复跨族也被排。这里没有先为每direction任择一条再取closure，因而closure不会偷偷增加相交lines。

简单平移不能代替(4)：任一全方向wholeline union S与S+v，若v≠0，取S中direction v的一条lineℓ，ℓ+v=ℓ，故两union相交。v=0更平凡。实际Baire重选整个族是必要的不同操作，不能误说generic translation已给cross-disjoint。

## 11. 严格阈值、primary层次和独立反攻

s<n−1是实用门槛。取垂直e_n的(n−1)-disk B，其投影包含Q的horizontal footprint，则每个direction e_n、position在Q的line都碰B，A_B甚至为空；dim B=n−1不能保原avoidance结论。非compact障碍仅σcompact residual处理，非无限步自动open；任意非closed direction restriction不保compact，故我们只用closedcaps。

KM输入允许arbitrarycompact多fibres，不给continuous/Lipschitz selector、方向唯一、有限维manifold或semialgebraic line family；本证明没有加这些条件。最小维的arbitrary-Besicovitch→compactcode接口来自具名Th1.1/Lem2.1/2.2，不能从任意非可测原集合直接取compact witness selector。新slides 15–18只报告归约，我们独立补其‘extra work’及internal自依赖；不把报告当已peer-reviewed proof。

Slides19–20的closed（未必compact）构造只明确R3和类似odd维，不能充当本compact族的反例，也不能扩成全部even n结论。本轮反攻覆盖cube boundary、多codes同line、全方向finite闭盖、交点逃∞、重复跨族、σcompact和countable simultaneous选择；不靠数值样本替代这些拓扑证明。

## 12. 当前结论、互审对象与总目标

以上从第1节完整相对输入得到了所锁结论，无需unique/continuous较弱子类；归约本身不是n−1下界证明。若未来某固定n排除这样的compact全方向族，才由contrapositive及KM输入给ordinary dim_H≥n−1。n5仅≥4不强于现有4D输入后果；n6的≥5才有更强潜力。未获得no-family或满维数、finite/maximal/shading量化、newID/major/优先权。

本稿已实际全文读root12 notes/20_dimension_lifting/disjoint_lines/R0081_baire_reduction_to_compact_disjoint_families.md；其fixed-B有限net加closed direction盖、G∩非空open位置盒全D选择、canonical farbad闭性及countable crosswhole递归逐步独核一致，当前无强制修改。随后已actual全文独审B12 notes/20_dimension_lifting/disjoint_lines/R0081_compact_family_reduction_and_counteraudit.md：其fixed-B乘积开覆盖/closedcaps、cube同胚传递R_dim、whole previous-obstacle选择和同一residual/countable recursion均正确，无强制项。root及B均已回报实际全文独核A12通过，B终稿§12cross记录也已实际读回；A自身施工不计自己的独审。终macro6及next6 notes/00_map/R0081_next_fullcompact_multifiber_gate.md已实际全文读取：只授权完整多fiber compact问题的下一phaseI，orientation double cover端点模型不冒满球面/selector/degree，未预证no-family，范围无强制修正。具名KM wholeproof不新独证，未经外部同行评审；正式六节独审另存授权review，不认证未来metadata/Git/sync。无Git/meta/download/spawn。
