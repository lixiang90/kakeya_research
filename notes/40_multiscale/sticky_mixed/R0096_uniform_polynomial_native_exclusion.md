# R0096：原观测商、coarse标签闭包与统一多项式native分支

2026-10-19，root。三份spec在各阶段施工前落盘。下面是完整原source的一个有额外bounded-degree输入的分支排除；不是全部mixed42、ordinary Kakeya或重大结果认证。高级GGW/QE仍按具名输入使用，未经外部同行评审，当前交独立逐步审查。

## 1. 精确结论和全部输入

固定D≥0、B≥1、0<κ<1、γ>0及bounded chart。存在η0>0、δ0>0，常数可依这些固定量，使完整WZ2609.22035v1 Def17.2–17.4 d5/k4/ell2、0<η≤η0、δ≤δ0、normalized C_CW(T)≤δ^-η的配置不可能同时满足：native βδ(t)=tildef(t)是degree≤D、各monomial系数绝对值≤B的R3多项式row。

允许βδ依赖δ、秩改变、非零singular values任意小；不加统一torsion、固定系数map inverse、goodrank或原T physical方向分离。原T joint4AD、N≈K^±1δ^-4、Z、两套filled grains、ξ/Φ/全coherence全部保留。K=Cδ^-C0η只计原有限损失。证明调用GGW2211.09508v2 moment Th2.1及R74经典compression/QE幂稳定；这些外部高级基础不声本轮全独证。

结论只排这个额外degree/系数范数受控的全局native分支。一般原β仅在Z dyadic-Lip，尚未提取此hypothesis；本稿不将其补为原定理输入。D随δ增长、任意分段拟合或局部proper模型也不在结论中。

## 2. 原whole管与逐管真实clock

原轴写X_T(t)=a_T+t b_T∈R4，λ=(a,b)∈R8 bounded，physical单位长度的clock区间在一个固定bounded区间内。原每条selected visit给

    F_tλ=n_t·(a+t b)∈N_Cδ Ytilde_t， n_t=(-βδ(t),1)。

Remark17.1及原incidence计数给平均每管≥K^-1δ^-1个不同原times，m(T)≤Cδ^-1。去轻管后得H，#H≥K^-C N，每T∈H仍带其全部原visits S_T且#S_T≥K^-Cδ^-1。μ_H归一后原whole-CW仅乘K固定幂；后文记作K^C，原分母收费不消失。不声这些witness删选组成新Def17配置，也不保删后Φ ADlower。

## 3. 精确观测商的原CW上界

先取任意至少五个不同times J及任意bounded β_t，V_t=(n_t,t n_t)，S=span{V_t:t∈J}，K0=S⊥，m=dimK0。用原Euclidean正交基Q=[A;B]参数化K0。每t∈J有n_t(A+tB)=0。m≥4时全部4minors是次数≤4的多项式，五个精确零点使它们恒零；m≤3时自动rank≤3。故r0=max_t rank(A+tB)≤3对全部实clock成立，无J gap分母。

经典compression的所需证明如下。取最大rank处作clock平移及临时可逆基，将A化[I_r0 0;0 0]，B写[C D;F G]。Schur恒等式给G=0、FC^jD=0。U=span{imD,…,im C^(r0−1)D}在C下不变且FU=0；令e=dimU，得到K1⊂K0、dimK1=m−r0+e和物理E⊂R4、dimE=e，使AK1+BK1⊂E。还原后立即用原正交投影；临时基的条件数不参与覆盖。ker0取r0=e=0。

一个P_S参数r-ball，δ≤r≤1，使原参数距同一affineK0≤Cr。只网格化K0/K1的r0−e个bounded坐标，需要≤Cr^-(r0−e)个bins。每bin的whole原管在一个affine(e+1)-plane的Cr邻域，含round caps的凸box体积≤Cr^(4−e)。原N/CW求和给

    (P_S)#μ(B_r)≤C K r^(4−r0)≤C K r。                (1)

大r用概率粗界，ker0用nearline r4体积；常数仅固定维数/chart，不依S/J/β conditioning。五times只定义商，未声原管共同访问或共享label。此命题是既有compression的原law应用，不将其新命名为独立重大方向。

## 4. 系数map与uniform性真正困难

令N_D=D+2、p_D(t)=(1,t,…,t^(D+1))，定义线性map

    Cδ:R8→R^N_D， F_tλ=p_D(t)Cδλ。

||Cδ||≤C_D,B，rank≤8。若β固定，则在S=(kerCδ)⊥，非零smin倒数L固定，(1)转换后给系数law至少1Fst，literal fullmoment R^N_D/m1 finiteGGW可直接排该fixed-polynomial分支。低rank系数support合法，不需V在R8有full8jet；R19只处理更窄固定单残差/一方向β，不能把其GWZ3应用当这个全R3 row已免费解决。

但当βδ随δ变时，L可为δ的任意大负幂；固定证明不能冒uniform结论。下列原coarse闭包与spectral gap正是支付这项责任，不能从printed GGW常数省略。

## 5. 从两套原grains支付coarse native标签upper

取原allowed尺度ρ≫δ及dyadic ρ-time窗J。第一套global grains为(x,y+f(t)x)，x∈R、y∈R3。原f在窗内变化Oρ，Def17.2的coarse Y_union为(ρ,3−κ,K)-AD。固定窗内原t_J，用有界shear (x,y)↦(x,y+f(t_J)x) 得空间union

    Nρ(E_J)≤C K^C ρ^(-4+κ)。                         (2)

其中time已在一个ρ窗内，(2)数空间四维格；x最多Cρ^-1格。

native表示为(u,η+βδ(t)u)，u∈R3。polynomial范数给uniform Lip C_D,B。取A_J=∪_(t∈J∩Z)Ytilde_t的一个L_D,Bρ-separated极大子集，每η_i选择其实际t_i及完整native filled Xtilde_(η_i,t_i)。后者有≥K^-1δ^-3个细horizontal格，ambient packing给≥K^-1ρ^-3个coarse horizontal格。用共同shear (u,y)↦(u,y−βδ(t_J)u)，其normal坐标处于η_i+O_D,Bρ；L_D,B足大使不同i的这些normal slabs格不交。于是(2)迫

    Nρ(A_J)≤C_D,B K^C ρ^(-1+κ)。                    (3)

这里借的是原filled三轴和原第一套coarse union，未假Def17.4额外native unionAD、也未授任意active子集ADlower。固定常数着色/邻格与体积范数全在C_D,B内。

## 6. 九个allowed尺度和空singular band

先固定ε*>0很小于κ，及下节需要的大M；a0=1/100，a_j=a0(ε*/(4M))^j，j=0,…,8，a_min=a8>0。源η最后小于a_min/10。对每j向上取原allowed exponent a'_j∈[a_j,a_j+η]⊂[a_j,2a_j]，ρ_j=δ^(a'_j)。必要的dyadic格常数按可比尺度处理。

各open singular bands (ρ_j^M,ρ_j^ε*)互不相交，因为M a'_(j+1)≤ε*a_j/2<ε*a'_j。Cδ至多8个singular values，故九band中某一个不含它们。固定这一原allowed ρ，按SVD写

    Cδ=C_s+C_w， smin^+(C_s)≥ρ^ε*， ||C_w||≤ρ^M。    (4)

零singular values进weak；边界值按strong/weak约定，不需相邻间隙strict下界。C_s norm/support界≤C_D,B。ρ在δ^(2a0)与δ^a_min之间，δ≪ρ，所有K损失换成ρ^-Cη/a_min。此步不改变原配置或要求C_s对应另一原β。

## 7. 近kernel的统一半代数compression

令K_s=kerC_s，以正交Q=[A;B]参数化，m=dimK_s。在K_s上

    n_t(A+tB)=p_D(t)C_w Q， ||·||≤C_Dρ^M， |t|≤1。

因||n_t||≥1、||A+tB||≤C，m≥4时全部4minors在固定五个times为O_Dρ^M；固定degree4插值使其全部系数≤C_Dρ^M。R74已证明的固定维compact半代数幂稳定给：某e∈{0,1,2,3}、K1⊂K_s维数m−3+e、E⊂R4维数e，满足

    ||(I−P_E)A P_K1||+||(I−P_E)B P_K1||≤Cρ^(M c*)。 (5)

c*>0与C仅依固定维数及norm bound，m有限取最小共同c*。它来自Grassmann正交projector的compact最小化、精确zero compression及具名real QE幂比较，非基底condition number。先取M c*>3；若m≤3直接全K_s网格，无需(5)。此处不使用δ-dependent曲线的非退化定理。

## 8. 强系数law的Frostman账

令ν=(C_s)#μ_H。对r≥ρ，一个系数r-ball的原参数在同一affineK_s的Crρ^-ε*邻域，因为(4)强非零smin已付。置

    h=C[rρ^-ε*+ρ^(M c*)+δ]≤C' rρ^-ε*。

m≥4时按K_s/K1的3−e个坐标作h网；whole原管均落相应affine(e+1)-plane的Ch邻域。原whole-CW给

    ν(B_r)≤C K^C h≤C K^Cρ^-ε* r， r≥ρ。            (6)

每bin体积h^(4−e)、bins数h^-(3−e)，所以只付一幂ρ^-ε*。m≤3用全K_s的h网与nearline h4体积，得到h^(4−m)≤h；ker0同式。h≥固定常数用概率≤1粗付，无大r漏洞。

将ν在半径cρ的R^N_D球上mollify，记νρ。r<ρ时(6)给density bound C K^Cρ^-ε*ρ^(1−N_D)，所以每固定α<1有

    c_α(νρ)≤C_D,B K^Cρ^-ε*。                       (7)

重叠小球也满足该上界；共同同系数的原管可以有不同visits，随后用全部witness并集保每个support点参与。固定homothety把support放unit ball只改C_D,B。

## 9. 实际coarse clock、目标与全部support参与

将原fine t round到一个完整ρ-regular网u。每槽长Oρ，最多Cρ/δ个δ-separated原times，故每heavy T的原S_T仍给≥K^-Cρ^-1个不同coarse u。每槽被O(1)原dyadicρ窗覆盖，(3)给coarse目标Y_u的ρ-cover≤C_D,B K^Cρ^-1+κ。

原F_t和p_D(t)C_sλ在bounded λ上有uniform derivative bound C_D,B；weak phase≤C_Dρ^M，原fine标记误差Oδ。因此每个所保coarse visit确有

    p_D(u)C_sλ∈N_(C_D,Bρ) Y_u。

ρ-smear只添O_Dρ误差。对每个coarse u，从该固定moment normal的disjoint ρ×1×…×1 tiling选所有与这些扩大target strips及固定support盒相交的plates；每target interval只有O_D,B(1)个长轴盒，得到

    #W≤C_D,B K^Cρ^-2+κ。                            (8)

整个νρ support每一点至少参与K^-Cρ^-1个实际time plates。没有将a.e. Hausdorff投影当finite定理，没有把原time law改成独立产品，也未丢multiple tube witnesses；完整regular网未用的times取空plates即可。

## 10. literal GGW与统一指数矛盾

具名GGW v2 Th2.1原PDF3，§2先固定factorial moment曲线。通过固定D的diagonal归一化，p_D正是其m1 tangent normal；该转换成本只依D，不依C_s/βδ condition。对0<α<1，全部support若参与≥ρ^(ε_th−1)，则

    #W≥c_(ε_th,N_D,α) νρ(total)c_α(νρ)^-1
         ·ρ^(-1−α+L_N sqrt(ε_th))， L_N可取10^(10N_D)。

先α=1−κ/4，取ε*<κ/64；ε_th足小使L_N sqrt(ε_th)<κ/16。再取M满足§7和九target exponents，最后η足小，使Cη/a_min<min{ε_th/2,κ/64}（包括全部有限原成本）。原参与遂超过theorem阈值，(7)给lower至少cρ^-2+κ/2，(8)至多Cρ^-2+7κ/8；δ最后小即矛盾。所有fixed constants通过ρ→0吸收，ρ的a_min固定正，δ0不依Cδ的最小非零singular value。

这完成§1 uniform bounded-degree/coeffnorm分支的候选证明，待独立全文验收。不因一般smooth nondegenerate定理的曲线依赖常数跳步，也不以fixed-profile proof误报uniform。

## 11. 独立反攻与实际范围

B的强反攻：β_i=t^i+ψ_i，三个小C∞ bumps有不交内部supports并留gap、||ψ1'||<1/2。全函数1,t,β_i,tβ_i线性独立（gap先消base polynomial，再逐support消Ai+tBi），故global row span8；但每局部仅degree0…4加单个ψ_i/tψ_i，至多7维，8-Wronskian处处0，β1'仍≥1/2。它否globalspan/Lip/smooth免费授full8jet，不否lowerambient或本poly分支；未构成完整source。

另一校准βδ=(δ^A t²,t⁴,t⁶)、A>1，每δ八维torsion非零却趋零。若仅用小e_(a1)线段概率，它有uniform α<1 Fst且原标量输出全在δ，但每time一plate已覆盖，故GGW不可对这种δ-dependent曲线无条件宣uniform cutoff/constants。该概率没有原wholeCW/joint4AD，不反(1)、(6)或本source排除。

真unit bush/parallel族可配前一β说明弱原law不授曲线hyp，却union正体积、缺source小label/Φ，不是Kakeya反例。R95的native非直线和R14双块rank2障碍保持原scope；当前是不同一维moment系数工具，仍未证明rough source可作全局bounded-degree近似。

## 12. 闭包、原目标与审查停止

平均访问到逐heavy管、原CW重归一、mollify/粗clock比例及全部coarse标签都已分别列账；没有授删选后ADlower。coarse native闭包来自两套原E表示，不是把allcoarse当公设；固定S商及近compression是经典工具应用，不新立同义ID。初步primary比较只到GGW/R74/R19与原WZ范围，有限搜索未认证新颖或优先权。

即使全文通过，结论也只排额外统一D/B的global polynomial native case；ordinary初始化、HRZ全费用、sticky完整κ1/余mixed/ordinary桥、同集full方向严格低维四路仍open。一般dyadicLip的degree可能随δ增长，分段拟合的time/质量和coarse误差不能免费送入本定理。完成本门后停止D/κ/window/导数或谱gap常数续轮，不降低完整Goal。两代理实际全文审和root整合后才内部reviewed，仍未经外部同行评审；状态/验证/git/sameSHA同步另按实际执行记录。Goal active。

当前两份actual全文formal与root实际整合已限定通过：research/reviews/R0096_original_coarse_labels_and_GGW_review.md、research/reviews/R0096_spectral_gap_compression_and_scope_review.md及research/reviews/R0096_root_integration_review.md。上述uniform polynomial-native结论现记内部已审，仍未经外部同行评审，未升级为完整rough分支或重大结果。
