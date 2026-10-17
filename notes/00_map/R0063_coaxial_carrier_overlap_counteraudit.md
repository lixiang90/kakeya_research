# R0063：共同二维脊的载体重叠、平均质量与严格校准

2026-10-18，B。已恢复context、GOAL／STATE／ROADMAP、78项状态及R62入口，实际读本轮先写macro／spec及R44／45／48／61冻结边界。仅编辑assigned文件，不Git／spawn。三维全密度absolute-CW沿R60具名临界输入，不把其wholeproof作本轮独证；全部新模型结果待独立审查，未经外部同行评审。

## 1. 完整模型与待检结论

固定n≥4、bounded ambient、常数C，Pi为affine 2-plane。Sigma_j为包含Pi的affine 3-planes，其商方向在RP^(n−3)中h-separated，δ≤h≤1。每原index唯一归入一组j；允许重复支持线及非负权w_i。真实physical unitδ管Ti的整轴在N_(Cδ)Sigma_j中，Yi⊂Ti任意Lebesgue可测。置

    E=∪Yi，W=Σw_i>0，I=Σw_i|Yi|，
    Vδ=|unitδ-tube|≈δ^(n−1)，λ=I/(VδW)。

Vδ含roundcaps。假原S^(n−1)每固定C0δ方向帽的**全族**权≤α；无向线可先用有限antipodal charts，常数不变。不能把仅组内cap称全局cap，亦不由PW自动获得它。

若所有原unit directions满足|proj_(Pi⊥)v_i|≥a>0，则下文证明对每ε>0

    |E|≥c δ^(n−1+ε) λ³ W/α
                  ·min{1,h aλ/δ}^(n−3)。            (1)

常数依n,C、bounded chart及具名三维输入，独立于组数、权跨度、a,h,λ。这里平均输入直接可用，不额外假每根有相同密度。

## 2. 离脊处实际overlap

平移使Pi线性，写Rn=Pi⊕Pi⊥，Sigma_j=Pi⊕ℓ_j。对x的商坐标q≠0，d=|q|=dist(x,Pi)，准确有

    dist(x,Sigma_j)=d·sin angle([q],ℓ_j)。

所以x落在N_(C′δ)Sigma_j中时，ℓ_j位于RP^(n−3)内半径O(min{1,δ/d})的角帽。h-separated packing给

    #{j:x∈N_(C′δ)Sigma_j}
       ≤C[1+δ/(h d)]^(n−3)。                     (2)

当d≲δ时可用总数O(h^(−n+3))，仍被(2)覆盖；不需要d≥δ。在dist(x,Pi)≥r>0的区域，以d换r即可。真实Ti在N_(C′δ)Sigma_j内，因其轴有原Cδ误差而自身半径δ；这项只改固定C′。

## 3. 平均λ可直接保原incidence，无δ下限

固定Ti方向v，记b=|proj_(Pi⊥)v|≥a；取Pi法向unit l使l·v=b。以自身轴坐标s及z∈v⊥参数化真实管。round tube包含在

    {x_i+s v+z: |s|≤1/2+δ， |z|≤δ}

中。固定z时，dist(x_i+s v+z,Pi)<r迫使|l·(x_i+z)+bs|<r，其s长度至多2r/b。对z积分得

    |Ti∩N_rPi|≤C (r/a)Vδ。                      (3)

这是实体tube slicing，不是先把轴加粗后得到(r+δ)/a。因而(3)对r<δ也成立；roundcaps没有被当参数端点零测删掉。

取r=c aλ，c依固定常数足小。置Yi′=Yi\N_rPi，则

    Σw_i|Yi\Yi′|≤C(r/a)VδW≤I/2。               (4)

无需heavy过滤、逐管密度或aλ≥δ。单根可能失去全部阴影，但后面的局部定理允许全部λ，故只需保全族I′≥I/2。若后来再按labels／shading删选，必须重算I、W、λ，不能照抄(4)后的平均值。

## 4. 每载体的三维absolute-CW与原物理体积

对固定j正交投影π_j到Sigma_j。轴在Cδ邻域且单位长，故|proj_(Sigma_j⊥)v_i|≤Cδ，|π_jv_i|≥1/2。若两个投影unit directions落同Cδ帽，则原directions也落原空间一个C′δ帽；有限cover给投影帽原权≤Cα。重复indices全部保留。

取共同fixed physical length L0及半径Aδ的三维包络P_i，覆盖π_jTi；仅延模型支持线、不移动Yi′。对任意凸U，P_i⊂U的directions可由John box计数：两短轴宽l2,l3及长轴l1≥c给O(l2l3/δ²)个δ方向帽。因此

    Σ_(P_i⊂U)w_i≤Cαδ⁻²|U|，
    D_j=sup_U Σ_(P_i⊂U)w_i|P_i|/|U|≤Cα。       (5)

若U不含任何tube则平凡；有tube时短轴≥cδ。大／细长box用min{1,l_k}只会改善方向帽数，l1≥c足够。这不是假定投影directions分离，而是原cap的indexed绝对浓集。

令Ej=∪_(i∈j)Yi′，Wj=Σ_(i∈j)w_i，Ij=Σ_(i∈j)w_i|Yi′|。每个π_j-fiber与Ej相交的(n−3)-volume≤Cδ^(n−3)，因为Ej⊂N_(C′δ)Sigma_j。定义f_j=δ^(−n+3)∫fiber 1_Ej，则0≤f_j≤C，且

    Σ_(i∈j)w_i∫_(P_i)f_j≥δ^(−n+3)Ij。

对真实f_j全部levels用R60三维全密度absolute-CW估计，再积分并用Jensen，得到

    |Ej|≥c δ^(n−1+ε) Ij³/(αVδ³Wj²)。            (6)

Wj=0组记0。没有只选一个level后再损λ；没有把fiber upper误作fake fiber lower。normal维数δ^(n−3)及三维δ²合为原δ^(n−1)，所有体积均回到同一原Rn frame。

## 5. 全局求和与定量结论

由(2)，所有Ej在dist≥r部分的overlap≤M(r)=C[1+δ/(hr)]^(n−3)。因此

    M(r)|E|≥Σj|Ej|
       ≥c δ^(n−1+ε)/(αVδ³) Σj Ij³/Wj²
       ≥c δ^(n−1+ε) (I′)³/(αVδ³W²)。

最后一步是weighted Holder，未假各组密度或权相同。将I′≥I/2、r=c aλ代入，即得(1)。n=4特别为

    |E|≥c δ^(3+ε)λ³ W/α·min{1,h aλ/δ}。         (7)

若没有原方向cap但独立给各投影族D_j≤D统一，则同证明把α换D。还有R60§12的实际absolute-PW版本：若原Rn族对相关固定格式H满足Σ_(|Ti∩H|≥|Ti|/2)w_i≤Kpδ^(1−n)|H|，则对P_i⊂U用H=N_(C′δ)Sigma_j∩π_j⁻¹(Q_U)∩B_R查询；其体积≤Cδ^(n−3)|U|，每根原Ti全在H内，故D_j≤CKp。因此固定angle结论(1)可直接以Kp替α，不先授方向cap。原测试格式统一，C依fixed n／containment／bounded ambient；absolute计数无需重设子族Kp。

这个替代不自动授权下一节的small-angle帽cover；§6仍用真实全局方向cap。全族／逐组cap、absolute-PW、物理containment和原label质量各有不同责任，不能把PW4字面偷换成方向cap。

## 6. 不预设angle：全局cap支付小角度删除

记Q=δ^(n−1)W/α≤C，最后不等式由S^(n−1)的δ帽cover。与Pi角<a的directions可盖

    Cδ^(1−n)(a+δ)^(n−2)

个原δ帽，故这部分最大原incidence≤CαVδδ^(1−n)(a+δ)^(n−2)。若λQ≥C1δ^(n−2)，选a=c1(λQ)^(1/(n−2))、c1足小及C1足大，删小角仅损I/4。余族仍用原λ取r=c2 aλ，(3)再删至多I/4；没有另损一次λ。

h=δ时，由(1)得到

    |E|≥c δ^ε λ^[3+(n−3)(n−1)/(n−2)]
                       Q^[1+(n−3)/(n−2)]。       (8)

小区λQ≤C1δ^(n−2)也由trivial |E|≥I/W=λVδ支付(8)：若p、q为(8)两指数，则p−q=n−1，(n−2)q=2n−5，故

    λ^pQ^q≤Cλ^(n−1)δ^(2n−5)
             ≤Cλδ^(n−1)       (n≥4)。

因此无需留下小角漏区。n4为δ^ελ^(9/2)Q^(3/2)；n5为δ^ελ^(17/3)Q^(5/3)。这是该结构类内的模型结论，不是ordinary满方向族自动满足的初始化。

## 7. δ-net归类与重复、density闭包

若每根whole轴只已知近某个包含同Pi的3-plane，先在RP^(n−3)取δ-net，每index选择一个合法carrier witness再唯一归入最近net点。bounded ambient使换carrier只增加C_Rδ误差；W、I、全局α原样保留，无额外labels或网格重数。所得h=δ族适用(8)。选择只需有限indices的有限选择，不假全参数可测selector。

如果同一原label被人为复制进多组，W／I／α必须按这些复制后的原index权同时计入，不能只在求和中计copies而在α中忘记。平均与逐管也分开：本证明保平均I′即可，完整whole-label唯一分组时原逐管Y未变，但去脊这个shading restriction不保证逐管lower。

## 8. 合法相近carriers点刷：求和损失真必要

令d=n−3，取δ≪λ≪1、h≥Cδ且hλ≲δ。在quotient的一个角半径cδ/λ小sector内取h-separated carriers，数J≈(δ/(hλ))^d。每carrier取一个避开Pi固定角的三维unit方向patch，放Cδ-separated网，≈δ⁻²个方向；其全部单位轴过Pi中的同一点。

各carrier方向patch可用共同水平二坐标及quotient line参数描述，跨carrier角距≳h、组内网距≳δ，所以全原帽权α≈1（取unit weights并适当固定着色／加大网距）。W≈Jδ⁻²。Yi为Ti在中心Cλ球内的真实部分，逐管密度≈λ，roundcaps不参与裁零。

所有Yi都在同一参考Sigma0的Cδ邻域及Cλ球内，因为carrier sector宽δ/λ。因此

    |E|≤Cδ^dλ³。

而(1)去掉δ^ε后的右侧恰为δ^(d+2)λ³(Jδ⁻²)(hλ/δ)^d≈δ^dλ³。故overlap因子及其λ依赖不能在本全模型中免费消去。单点dist=r的角帽packing也直接使(2)饱和。

另取单管在Pi交点附近长≈λ的中央阴影、δ≪aλ，可使全部阴影落在N_(C aλ)Pi中；故不能以r≫aλ的截断仍普遍保质量。两校准均非Kakeya／完整source反例，也不证明(8)的每个Q指数最优。

## 9. Source与旧冻结的责任比较

实际读Katz–Zahl v3 Lemma30与(48)、(55)–(70)。W(T)是S3中的direction box，不能单凭其字面授physical containment；但固定Q0后有独立合法构造：取其中心及Pi(Q0)为affine Π。T过Q0且v(T)距Pi(Q0)≤Cθ，故整T及Q′距Π≤Cθ。T′轴有点z距Q′≤Cθ，取p∈Π距z≤Cθ，则Σ=Π+span(v(T′))使完整T′在N_(Cθ)Σ中。非平行情形Σ为3-plane；平行情形可任意补第三维。因此whole-axis containment无须(48)辅助线的θ／dist费用，A的这项正面接口已独立核实。

源Definition5还须字面付实体接口：Y2(T)为完整θ-cubes、各cube仅intersects原T，不一定在原physical θ-tube内。保持这些原cubes不动，取同支持轴fixed Cθ-radius实体包络（含端帽）即可包含全部Y2；密度及方向cap CA只变固定常数，空间disjoint仍保。carrier网可改成相应fixed Cθ-net，各label仍唯一归类；不付δ幂。这里用方向cap版，不免费声加粗包络继承原absolute-PW K。

(63)–(64)和其前序原shading分区仍是另一责任：从平方multiplicity比较到空间union求和不对任意抽象矩阵仅凭Cauchy–Schwarz成立。沿具名原R4／disjoint preprocessing作Y2-light labels删选，保实际tuples后重选rich Q0再调用模型，而不是把完整Y1阴影免费附给每条入选二臂。A13／root12现已完成这项原质量证明、诚实N1／A0计数及W／rho／p预算；B已实际独核其完整条件桥。它不认证(63)整段预处理wholeproof或所有source分支的统一改良。

与R44单包络piece预算不同，(2)处理同空间多carrier实际重叠；与R45固定arms endpoint/BL不同，本稿不抽generic横截tuple；与R48／61不同，没有短clock重缩或声称删除原ρ费用。但若source仅给更厚近载体、direction-cap按θ非所用物理厚度，或每label被多tuple计数，则不能凭(1)抹掉这些费用。也未证明一般全PW4族可化为本共同脊结构，所以不把模型式另命名为一般PW4增益。

## 10. 当前结论与停止

模型已完整支付原平均质量、全局cap、同组投影及重复、真实normal fiber和跨组overlap；一般fixed n扩展是同一证明，不另开机制。它给(1)／(7)，以及任意合法共同脊carrier归类后的(8)。相近carrier点刷严格说明主要overlap费用必要。

本轮真实KZ映射与完整参数桥已在named R4／disjoint／angle／方向盒输入下施工并独核：完整Y2-heavy保原tuples，whole-axis共同脊、实体包络及specific原PW查询均已支付。新旧倍率rho p lambda0³/(C_loc theta)没有统一固定幂余量，所以本轮停止该插入及a／h／λ／p／rho参数轮；不把桥梁升级为普通高维结论。最终范围见research/reviews/R0063_geometry_and_mass_review.md。Goal active，具名三维source conditional，未经外部同行评审，不认证major／novelty。
