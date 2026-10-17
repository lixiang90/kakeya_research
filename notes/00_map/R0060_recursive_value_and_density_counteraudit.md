# R0060：真实递推价值与全密度联合图形机制反审

2026-10-17开轮，2026-10-18施工补全，B。已实际读固定入口／registry78状态、R59 round／macro／next、R60先写spec／macro及正式转题§7，重读HRZ §4、§5、§8与OAI3 §§2.1–2.3、10.1–10.2。只编辑assigned文件，不Git／spawn。以下具名高级wholeproof未由本轮重证，未经外部同行评审；不宣普通高维维数改善、重大或新颖。

## 1. HRZ真实价值：停止责任不是所有k都被m4封死

HRZ Th4.1与Prop4.2给n5的完整broad／narrow门槛如下；其中q为tube-overlap Lq指数，所对应集合维数为q′。

| k | 原broad q下界 | 原narrow q下界 | 两者最大值 |
|---|---|---|---|
|2|16/11|5/4|16/11|
|3|18/13|4/3|18/13|
|4|21/16|3/2|3/2|
|5|5/4|2|2|

dim>4需要q<4/3。因此k≥3即使任意改进broad，也被原narrow封住严格>4；k4的m3 tangential broad本已vanish。k2仍须处理raw m2／m3分支：R59只是near-full union，不保HRZ raw tiny-broad质量或Lp，因此没有提供对源(53)的合法替换。

不能声称m4对所有k本身封死：若无依据地完全抹去k2的m≤3分支，源m4数值21/16与窄5/4反可给q′=21/5。真正未付的是低维终端的原norm／marks调用，而不是这个反事实numerology。R48的whole-broad与原shadings分离、短clock方向重数及真实leaf费用仍有效，不把重算记新数学。按spec停止当前接法，正式转题为全密度三维颗粒，不续k／degree／radius参数。

## 2. 正式选题、强输入及未偷换范围

spec§7：fixed n≥4、bounded semialgebraic格式、R,C、ε>0；Sδ⊂B_R realdim≤3，系数可依δ。原unitδ-tubes整轴在N_(Cδ)S，原物理方向δ-separated，Yi⊂Ti任意Lebesgue可测，平均密度λ∈(0,1]。目标

    |∪Yi|≥cδ^(n−1+ε) λ³N。                           (1)

这次保**整轴**近S；不是把R59仅Yi近S的结论免费扩大到任意λ。新机制是同时保whole-T与Yi的多数投影，以及OAI3实际weighted indexed plank临界结论；后者强于只引用Theorem1.1的方向分离statement。该结论须作为明确具名输入，不把全部论文由本审计认证。

## 3. OAI3 h=0到任意原权有限图：统一常数完整证明

固定p>2且Prop10.1所给h(p,0)=0，N为dyadic resolution。bounded矩阵族Mi、正权ωi、非空time-bin集合Si允许重复矩阵及任意权跨度。写

    W=Σωi，I=Σωi|Si|，k=I/W，λ=k/N，
    Δ0=sup_(full-time B) nB/(ab)，m=I/|E|。

对任意ξ>0，存在C_(p,ξ,chart)，统一于全部有限族，使

    m≤C N^ξ λ^(−p) Δ0，
    |E|≥cN^(−ξ) λ^(p+1) N W/Δ0。                   (2)

证明不假原counts已uniform。先删|Si|<k/2的indices，只损≤I/2；将余下|Si|按dyadic区间[K,2K)分组，某组保≥I/O(logN)原event mass，且K≥k/4。每根只保恰K个原bins，损至多因子2，原权保留，Δ0不增。

若(2)不uniform，取固定ξ的违反序列。bounded N不可能使ratio无界：widest bounded-chart plank给Δ0≥cW/N²，且m≤NW，所以mλ^p/Δ0≤CN³，不需#index或权重比上界。故N→∞。对上述exact-K序列用原Lemma2.6的extensive regularization，保I N^−o(1)events；原active weight不增，root count≤K，统一root count至少K N^−o(1)。因此新λreg≥λ N^−o(1)，新raw mreg≥m N^−o(1)，Δreg≤Δ0。抽取profileF后，q=0恰有ΠF(1)=pF(1)，而λreg=N^(−F(1)+o(1))。Definition2.3与h=0给mreg≤λreg^−p Δreg N^o(1)，和固定N^ξ违反量矛盾。所有量均为原weighted graph，未独立化。

允许event中心距指定grid cell≤C/N：把该cell集合固定邻接扩大，仅乘常数，或直接以真实Mi(tJ)所在cell为E。于是(2)同样给指定邻近cell count下界。此是原Prop10.2离散uniformity论证保留Δ0的版本；原文10.20利用方向分离置Δ0≤C，这里未作该置换。

## 4. 共同random-grid：从有限图到任意可测CW阴影

设R3 bounded族的原unitδ-tubes带任意正权、总权W，允许相同参数；原可测Yi的平均密度为λ。令

    Δ=sup_(convex U) Σ_(Ti⊂U) ωi|Ti|/|U|。

证明具名h=0输入给

    |∪Yi|≥cδ^(2+ξ) λ^(p+1)W/Δ。                    (3)

先分固定有限方向charts，使时间分量有统一lower；共同bounded clock留固定padding，原round端帽仍在其中。旋转／固定重缩只改常数。用同一个随机平移格δZ³+z0，z0在一个δ-cube中均匀；这里只为计数可取与dyadic N^−1可比的间距，以下仍记δ。

令E=∪Yi，E_z=E∩(δZ³+z0)，I_z=Σωi#(Yi∩grid)。每根tube在一个该时间层的空间截面直径O(δ)，故至多C个gridpoints。按固定字典序分成C个slots，每slot每time最多一个point，复制原index及原权；空slots删掉。其active total weight≤CW，事件总质量恰I_z。样本point离支持线O(δ)，采用**未clamp**时间坐标，共同time-grid shift吸收进intercept；实际事件cell count≤C#E_z。没有只因端点time measure0而删掉端帽实体质量。

slot的full-time plank参数≤CΔ：若extended trace在cell widths a,b的plank内，原实心tube在其固定厚化的凸平行棱柱内；a,b≥1且δ≈N⁻¹，体积≤Cabδ²。原CW及C次slot复制给nB/(ab)≤CΔ。矩阵范围和共同clock都是固定chart，不把原短阴影补成full marks。

逐z0调用(2)，用active W_z≤CW、Δslot≤CΔ，得

    #E_z≥cδ^(p+ξ) I_z^(p+1)/(Δ W^p)。

空事件时两侧为0。对任意Lebesgue可测sets，共同格计数可测，Tonelli给

    E #E_z=δ⁻³|E|， E I_z=δ⁻³Σωi|Yi|≈λδ⁻¹W。

Jensen直接推出(3)。这里随机的是全空间同一格；没有把不同Yi独立抽样，也没有以δ-grid厚化E的体积反推原|E|。bounded support使每次格点数有限；任意有限#index、原权极小或重复均不增加费用。有限方向charts可按weighted incidence选一类，或相加后用Jensen，均仅固定常数。

还可去掉p+1>3的极小λ损失。bounded chart给Δ≥cδ²W；某原index的密度≥λ，故|E|≥cλδ²。若λ≤δ，则此粗界已强于cδ^(2+ε)λ³W/Δ；若λ≥δ，令p−2=ζ<ε/2，(3)中的λ^ζ≥δ^ζ，再取ξ<ε−ζ。由Prop10.1可选这样的p，所以统一于**全部**λ有

    |∪Yi|≥cε δ^(2+ε) λ³W/Δ。                       (4)

这是bounded weighted indexed absolute-CW版本；不只方向分离，也不是GWZ near-full门槛的字面推论。

## 5. 多数投影如何同时保存whole T与任意Yi

固定e0<1/8。有限等权正交投影πj:R^n→R³可选得：任意m≤3平面V上至少(1−e0)比例j的最小singular value≥τ>0。有限Grassmann net加Haar投影的小singular-value概率及有限采样给存在性；τ、族大小只依n,e0。m<3可先补至3-plane。此几何选取和同π图形分解由A完整独立处理，未据generic transversality替实际原law。

对每j，仅取原各strata中πj-good tangent点，再按R59 regular-cell法在**同一个πj**下分有限global-Lip图，令Hj为它们Cδ邻域之并。finite union仍有normal fiber≤Cδ^(n−3)，格式统一。每个q∈N_CδS至少属于(1−e0)比例Hj：取任意邻近stratum点p，在其good projections上q属于Hj；不需要可测footpoint选择。

整原Ti⊂N_(C+1)δS，于是平均j的|Ti\Hj|≤e0|Ti|，对Yi亦同。Markov分别使坏j数≤2e0J，所以存在同一个j(i)同时满足

    |Ti∩Hj(i)|≥|Ti|/2， |Yi∩Hj(i)|≥|Yi|/2。          (5)

Yi为空时第二项平凡。将原labels唯一分给这样的j，保全部原权，不重置平均密度。无需假整Ti在单个graph。

由normal fiberupper，|Ti∩Hj|≤Cδ^(n−3)|πjTi|，而|πjTi|≤Cδ²(|πjvi|+δ)；(5)迫|πjvi|≥c。故在有限投影方向chart中，以支持线在固定坐标平面处的精确截距pin中心，把原整投影包入固定长L0、半径Aδ的精确包络Pi；不round四线参数，也不去重。端帽及调用固定长度版CW时的共同固定homothety只改常数，不另作新unit延长。

## 6. 常数PW查询与indexed重复：不再支付λ⁻n

固定assigned group j。对任意convex U取John矩形Q_U，test Hj∩πj⁻¹Q_U格式有界、volume≤Cδ^(n−3)|U|。若Pi⊂U，原Ti与test至少有**whole tube一半**体积，由(5)，与Yi密度无关。原方向分离PW因此给

    # {assigned原i:Pi⊂U}≤Cσ δ^(−2−σ)|U|。            (6)

把每个原i的Pi保作indexed tube，即使投影包络相同也不合并；其absolute Δ≤Cδ⁻σ，正是(4)允许的重复weighted范围。因此没有R59重数去重的N损失，也没有λ⁻n。若要证明任意原权的PW版须另付，以下主证明先原unweighted方向分离。

## 7. 全levels积分和原group Jensen：无额外λ

令Ej=E∩Hj，f_j(z)=δ^(−(n−3))正常∫1_Ej，0≤f_j≤C。每个assigned Pi有∫Pi f_j≥δ^(−(n−3))|Yi∩Hj|。设该group总数Nj、原总shading体积Ij=Σ_(i in j)|Yi|，写λj=Ij/(Nj |Ti|)。则Pi的f平均再对indices平均至少cλj。

对每个u∈[0,C]，在同一indexed Pi族取真实shadingPi∩{f_j>u}。用(4)及(6)，再对u积分，layer-cake和Jensen给

    ∫f_j ≥ cδ^(2+ε0+σ) Nj∫_0^C λj(u)^3du
           ≥cδ^(2+ε0+σ) Nj λj³。

这里∫λj(u)du为真实平均f值，≥cλj；没有先选一个u再倒付λ。把normal因子回传，|Ej|=δ^(n−3)∫f_j。有限个Hj可能重叠，但Σ|Ej|≤J|E|；原labels唯一分组且ΣNj=N、ΣNjλj=λN。因此

    |E|≥cδ^(n−1+ε0+σ)ΣNjλj³
         ≥cδ^(n−1+ε0+σ) λ³N。

先取ε0、σ使和<ε，得(1)。调用固定长度L0版CW时，共同fixed homothety同步推forward Pi与Pi∩{f_j>u}；u积分在原正交frame完成，不混不同frame的fiber测度。各λ始终按实际tube体积定义，写cδ^(n−1)仅作固定倍比较。

## 8. 原weights／方向bin α及全称删选闭包

若(1)对全部unweighted子族、全部原可测shadings统一，则任意有限原非负权、每δ方向bin总权≤α，也给同λ³W/α版本。固定有限着色使同色bins内方向δ-separated。每bin以概率ωi/α选择原i，否则留空；保留原Yi和whole axis，不造新时钟。随机N_s、I_s=Σ所选density满足E N_s=W/α、E I_s=λW/α。

对每次sample应用(1)，其union⊂原E；N_s=0时定义I_s³/N_s²=0。联合凸性／Hölder给

    E[I_s³/N_s²]≥(E I_s)³/(E N_s)²=λ³W/α。

故得到weighted结论，不要求W/α≥1或权跨度有界。多颜色再按原W_j、I_j作Jensen，仅固定常数。非负零权直接删去。此随机抽样严格依赖全λ统一子族结论；R59 near-full定理不足以先免费使用这一闭包。

本轮scope仍是whole-axis近fixed-format realdim≤3载体；不含R59仅Yi近S的全λ升级、不认证任意HRZ叶，也不解决ordinary H5。高级OAI3 Prop10.1、PW、regular-cell输入保具名wholeproof责任。已实际完整读root14／A10／B8／macro6／next6／spec7，正式审查见research/reviews/R0060_density_and_mass_review.md；本人finitecritical／randomgrid证明由A另行独核，不将自审冒独审。终稿后停止，不另续HRZ参数或把同模板另立major。
