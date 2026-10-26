# R0115：完整bulk对fixed-row候选的原质量资格

2026-10-26，new_projection_gate。只编辑本分配稿。恢复context、GOAL/STATE/ROADMAP/registry摘要及R114 next，实际重读原WZ2609.22035v1 Def17.1–17.4全部statement；回读R72、R107、R108相关完整推导和R114原质量测试。当前Goal active，六维17/4不变，无ordinary/完整source新gain、newID或major，未经外部同行评审。

## 1. 当前候选的完整量词与停止条件

本轮资格问题是如下**强版**，不是已付假设：对每个固定γ>0，是否存在a,τ>0、有限C和η₀(γ)>0，使0<η≤η₀、δ充分小后，任意完整d5、matrix33、κ=1原source，对全部

    t∈Z, y∈Y_t, ν∈S¹, b∈R,
    ρ∈R_η∩[δ^a,ρ₀],  R_η={δ^{jη}:j∈Z},  ρ₀<1固定，

都有

    B_(t,y)(ν,b;ρ):=
    #{x∈X_(y,t): |ν·ξ_(x,y,t)−b|≤ρ}/#X_(y,t)
            ≤K^Cρ^τ,       K=δ^{-C₀η}?             (1.1)

ν在本grain的所有x、φ上固定；b亦固定。η最后小到C C₀η≪aτ，因此右侧在ρ≈δ^a确为非平凡正幂。不能靠让η或C依δ任意恶化使其失去内容。

完整输入逐项保留：原T的bounded joint4AD、原N≈_Kδ^{-4}、whole-containment CW≤K；δ-separated Z且m=#Z≥K^{-1}δ^{-1}；原same-T全部selected visits；F_t dyadic-Lipschitz；nativeY_t AD1、tube-KT(1−γ)及全部allowed time intervals上的Y-union AD1；每grain filled X₂≥K^{-1}δ^{-2}；每point Φ_p AD1/slabγ及真实witness；selected ξ及Φ的每allowed physical cube粗coherence。Def17.4在k=ell=3与同一F相容，不另送额外斜率。

停止门：若只是原vector cap/CP/PM重调用，或强版自身已承担完整source排除，则拒“新局部输入”资格。若bulk统计不能控制所指单grain，须写出实际原质量不等式及最先缺失的推导，不把正cap设成成功hyp后读出。

## 2. 原selected graph、质量和旧闭包

按每point/Φ fine-bin固定实际原witness，保bounded(point,方向)及(T,t)重数，得到原used graph G。设d(p)为所用point degree、n_T为原全clock访问数。固定K有限幂费用后

    K^{-C}δ^{-1}≤d(p)≤K^Cδ^{-1},
    #E_t≤K^Cδ^{-3},
    I_cnt=Σ_p d(p)=Σ_T n_T≈_K Nm≈_Kδ^{-5},
    n_T≤Cm.                                         (2.1)

这里I_cnt是实际访问count，非物理shading体积；canonical选取若只保一个(T,t)须先付bounded multiplicity，不能删光某point后还声其degree lower。下文即保此固定图，不在每个用途重新选witness。

R114已证整vector球cap≤K^Cρ：一grain的水平/角packing经原4AD lower膨胀回原N，再以codim2的whole prism测试CW。固定scalar row仅把整管放近codim1的4-plane；packing和CW同有一幂ρ，不能旋转normal坐标后免费变成vector cap。原19.2/19.4仍须整矩阵slow前提，(1.1)的反设没有它。

R107的k₁(t,s)是F横向secant的clock law，(1.1)是grain内ξ的point law，两者不同。R108终端相容ξ_s−ξ_t=(F_t−F_s)φ正是原W式(148)，且全局终点collision不送同初fibre collision。不能由新增名称、更多clock或same-T恒等式本身宣布(1.1)。本轮不再证明其all-strip energy或two-terminal恢复。

## 3. 完整原source给出的ranked-multiplicity容量

这是将R114实际bulk失败用于**任意当前原source**的一条确切估计，不另换toy。取任意原管子族H⊂T，所有clock仍为原Z。以固定δ-grid表示物理R⁴截面。令

    M_H(t,Q)=#{T∈H:其实际轴在clock t距Q≤Cδ},

只为处理端帽，将原轴沿其同一直线作Oδ的clock延长；t在此扩大的单位段clock外时不计。这不换轴或添加原visits，端帽Oδ和原point误差只增固定倍。每管/clock只影响O(1)个格，因此Σ_Q M_H(t,Q)≤C#H。记同一H在原G中的实际访问I_H。每层原points占≤L_t≤K^Cδ^{-3}个格；按M_H(t,Q)递减排列为M_(t,1)≥M_(t,2)≥…，则

    I_H≤C Σ_(t∈Z) Σ_(j≤C L_t) M_(t,j).              (3.1)

因为每条实际selected edge的终点在相应轴的Cδ格内，原pointδ分离使格内point数有固定上界。该式不假角分离或独立clock，也不把原axes换成每time新族。

更直接，对任意L≥1，落于M_H(t,Q)<L的原H-visits数满足

    I_H,low(L)≤K^C m δ^{-3} L.                       (3.2)

令q=#H/N，若H的实际平均duration满足I_H≥α #H m=αqNm，α>0，则由N≥K^{-C}δ^{-4}可选

    L=c αq K^{-C}δ^{-1}                              (3.3)

（C和c作固定调整），使至少I_H/2在M_H≥L的高重数格上。若(3.3)<1，只给平凡门，不能声高重数。q是**原**N的比例，α为该H的实际duration，不得将它们省略后仍用δ^{-1}阈值。

这条结论是classical bookkeeping/校准，**没有独立的原source新信息**。对全T而言，Def17每point Φ degree早已直接给M_T(t,Q)≥K^{-C}δ^{-1}，high-multiplicity要求并非新增约束。对子族H的版本只在额外实际保有α average duration时成立，而R114坏grain的pencils没有这项future lower；不能把有条件subset校准作本轮positive主成果。这里的作用仅是保精确原分母，定位R114正幂容量失败及拟议推理的收费位置。

## 4. R114未来密度模式的一般原质量版本

固定真实clock t₀及任意H。若在所有|t−t₀|≥r的原clock上有一个**已经独立证明**的physical cap

    max_Q M_H(t,Q)≤A r^{-s},  s>0，                 (4.1)

则近clock每管最多C(r/δ+1)个visits，远clock用(3.1)，严格得

    I_H/(Nm)≤K^C [ q(r+δ)+Aδ r^{-s} ].              (4.2)

其中near项使用m≥K^{-C}δ^{-1}，far项用N≈_Kδ^{-4}；全部是原图访问。若同时I_H≥αqNm，且r≤cαK^{-C}、δ≪r，(4.2)迫

    A≥c αq K^{-C}δ^{-1} r^s.                        (4.3)

这不是附(4.1)后的“新fullsource结论”，而是由(3.1)可立即检验的**必要容量条件**。在R114数字族，q≈1、s=2、A=O(1)，取r=δ^{1/3}返回其I_H/(Nm)≤K^Cδ^{1/3}；该失败仍不被误称fullsource反例。

当前没有从row集中推出(4.1)。数字族的L∞≤C|t|^{-2}来自y₁、φ₂的精确独立均匀投影及特定线性det=−t²；完整原source不供这些联合priors。不能以Y和Φ各自AD/KT替换该joint density，也不能把一个nativeY的投影维数lower当实际卷积L∞upper。

所以(4.2)提供一条完全原质量的否定测试：任何未来的regularization主张须先保H的αq，再让其A与右式矛盾。它没有证明完整source普遍regularization，亦未靠另一toy规避联合责任。

## 5. 单grain与全bulk的真实比例差

固定(t₀,y₀)及该grain内任意A⊂X，#A=β#X。保这些point的全部原pencils，起点事件C的原访问数由(2.1)满足

    I_C≈_K βδ^{-3},
    p_C:=I_C/I_cnt≈_K βδ².                          (5.1)

对应真实witness管数至多I_C，故其原管比例q_C≤K^Cβδ。全局平均I_cnt的heavy删选可以删去整批C而几乎不影响bulk。即使β=1，这个grain也只有δ²级全局访问质量，不能将其witness自动当有nearfull duration的H。

用4AD lower在ρ尺度膨胀可得到更多原管（例如row集中所对应的4-plane附近有ρ级原族），但这些近邻原管没有因膨胀而取得任何原selected future visits。AD lower是原tube parameter计数，不是原G上的degree lower。将其代入(3.3)/(4.3)时α仍未付。

因此“原fullsource bulk近满＋一个grain的row集中⇒该grain原witness向未来输送固定比例原I”这一中间句不成立于现有平均账。若想只控制代表性grains，须把量词改成全原I加权，不能悄悄将它说回(1.1)的所有grain。

## 6. 实际origin质量能保证什么：duration筛选

本节给一条正向的原计数，避免只列缺什么。令C为原G上的**任意**origin事件，I_C=p I_cnt>0；C可横跨许多真实grain，但不重新定义原clock。令

    h=pI_cnt/(2N),  H={T:n_T≥h}.

低degree管承载的C-visits总数≤Σ_(T∉H)n_T≤Nh=pI_cnt/2。所以H中至少保I_C/2个C起点，每个该起点沿同一原T有至少h个实际terminal visits。全同管有序pairs数至少

    P_C≥(I_C/2)h=p²I_cnt²/(4N).                    (6.1)

若要求|s−t|≥r，每个origin最多损C(r/δ+1)个terminal choices。只要

    C(r/δ+1)≤h/2,

便有P_C,far≥p²I_cnt²/(8N)。由I_cnt≈_K Nm及m≥K^{-C}δ^{-1}，例如r≤c pK^{-C}且pK^{-C}≫δ即可。逐管筛选阈值依**事件质量p**，不是对原全管都赠同样density。

当p为K^{-C}级时，这提供subpower费用的同T far传播；当C只在一个grain时，(5.1)给p≈βδ²，所需r≤K^{-C}βδ²甚至低于δ，不能送一个非平凡far shell。这里的floor明确拒绝从单grain直接借全bulk duration。也不从(6.1)获得同初fibre collision；这是same-T pair lower。

## 7. 正确的加权替代量词与双向闭包

定义每grain的实际weight

    J_(t,y)=Σ_(x∈X_(y,t))d(p_x),
    ω_(t,y)=J_(t,y)/I_cnt,  Σω=1.

若每grain另固定row ν_(t,y)、center b_(t,y)，则其band的原incidence占比

    P_ρ=(1/I_cnt)Σ_(t,y)Σ_x d(p_x)
             1{|ν_(t,y)·ξ_p−b_(t,y)|≤ρ}.             (7.1)

由d(p)上下界，P_ρ与Σω B_(t,y)在K固定幂内可比。(1.1)统一成立会给P_ρ≤K^Cρ^τ；反向加权cap至多给单grain B≤K^Cρ^τ/ω，ω_(t,y)≈_Kδ²，丢δ^{-2}，不回到(1.1)。合法whole-time restriction可沿旧R22保层，但只保一个grain/clock会丢filled source的m下界，并非subpower重调用。

保管q、保原I比例p时λ'=(p/q)λ；归一事件cap除p，方向概率cap除q；若重取H的point-pencil lower或native AD lower，须另付。平均I cap也不自动对每条T成立。本轮未证明(7.1)有正ρ幂，更没有把它加到输入后宣新进展。它只是明确区分两个不同命题及(6.1)所能实际消费的质量。

此类incidence/phase-band到same-T far-pair的精确闭包由本轮另一分配稿专门核，不在本稿重复；R107所需F-clock secant law仍不是(7.1)的ξ-origin事件。若未来想证明加权版，须独立审它是否已由旧全称CP/PM/source gain推出，以及反向能否重建完整gain，不能因原source可能为空就真空登记新lemma。

## 8. 候选可行性、完整Goal与交接

截至本稿：没有从完整source取得(1.1)或(7.1)的新正幂。已实际付清的是任意原H的ranked容量(3.1)–(3.3)、near/far容量(4.2)及任意真实origin事件的mass-sensitive同管传播(6.1)，全保原N、原G和实际clock。这些是初等源计数的审计用途，不是新理论/维数界。

更强的资格攻击是：能否在任意假想完整source旁合法并入一个稀时钟、scalar原子的真实组件，仍保Def17全部下界及原T4AD/CW？若能，(1.1)已承担“无完整critical source”的排除强度；反向无source时其真空成立。这须核共享F、严格Oρ的ξ粗coherence、全部allowed Y-union、原N/I和unit axes，不能只以平均容忍小组件即预认证。本轮algebraic分工独立主核这个grafting，本文不抢写未验证的结论，也不与其重复proof。

即使得到完整κ1源排除，其与ordinary五维/Hausdorff的原提取/归约责任仍须分别核；不得直接把一个局部cap叫ordinary改善。当前停在root统一资格审定，不另开研究轮、不回到旧F-statement/更多times/重跑KT数表，不作Git或文献新颖性声明。Goal保持active。
