# R0048：HRZ真实终点与四维原染色输入的接口边界

2026-10-17，root整合。Goal active。本文核一个具体接法，未经外部同行评审；没有证明或否定H5，也没有新的高维维数下界。施工前的working specification及周期macro均已保存。A/B稿分别独立处理primary版本和实际递归/反攻，正式审查另存。

## 1. 目标、原量词与历史排重

H5要求：存在固定σ>0，对任意ε>0存在η>0、δ₀、cε及固定bounded graph chart，使R5单位图线

    L_i(t)=(t,b_i+t v_i),  0≤t≤1,

的slopes构成一个固定四维box内满δ-net且δ-separated，每个原index有至少δ^(−1+η)个原time-bin marks时，全部原marked δ-cells E满足 `#E≥cε δ^(−4−σ+ε)`。所有b_i、v_i一致有界，几何网格和固定倍厚度只付常数。H5尚未成立，任意集合Hausdorff读出须另付。

现有DIR003/FSD001提供near-full-density原straightline finite输入，量词∀target ε∃source η。它们不提供完整四维maximal Lp或任意λ的尖锐函数。另一方面，“没有full Lp”本身也不排除直接finite方法，所以本轮实际检验弱输入。

开轮排重后发现：R12/R13已经审过HRZ Th4.1/Prop4.2的n5 k4 broad 21/5、narrow `2p−3`及unit-H4 brush只给维数4。重算这些指数不是本轮成果。本轮新增核查是alg1/2真正tiny终点、原shading质量能否进入该终点、以及短clock缩放下真实方向重数。

## 2. 一手版本与依赖层次

主施工源为库内 `hickman_rogers_zhang_2019_v1.pdf`，570874 bytes、43页、SHA256 `ca20b3366b4e01717d741a6df94eb633a56c6f96b4a86eba5463362231eca93d`。root实际读§4/alg1/alg2/§8，并通过本地PDF34图像核tiny式(53)。A独立对照[JHU/AJM官方43页PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-hickman-rogers-zhang.pdf)的Th1.2、Th4.1和PDF34–35；root也实际读取该官方文本接口。关键递归接口对应，但v1四维历史表1.4794...在JHU变为1.4854...，不宣整篇字节相同。

[作者机构页](https://www.research.ed.ac.uk/en/publications/improved-bounds-for-the-kakeya-maximal-conjecture-in-higher-dimen-2/)确认AJM144(6)(2022)1511–1560和DOI10.1353/ajm.2022.0037，并提供accepted manuscript。CLI下载受Win10013/HTTP403阻碍；web读取成功不等于已保存新PDF bytes。本轮不伪造accepted版本hash，文献库保持33PDF/36sources，URL与实际scope入元数据。

当前OpenAI官方逐级Git tree独立核到paper.pdf blob `45ec20e423db2a9c70fd6303510bac361e6e9e8a`、1371486 bytes，与已存原稿一致。本轮有界primary检索没有发现已读声明覆盖H5，不认证不存在或first/best。RED001已经完成具名高级输入下的内部四维argument及finite/Hausdorff链；不复活已付assembly缺口，也不把作者署名当正确性保证。HRZ多尺度PW、完整四维及KT等高级输入仍分别列明。

## 3. 实际算法没有规范的四维直管末端

alg1的输入始终是原ambient Rn的δ管，切于m维TCI并在半径r球中工作。cellular半径r→r/2，algebraic半径r→r^(1+ε°)。原Properties I–III控制whole-tube broad范数、Σ_O #T[O]及max_O #T[O]，cell-entry/横截球重复费用由d的历史幂支付；它们不保持每个entry的原Y(T)密度。

alg1停于tiny `r≤δ^(1−ε°)`或较低维tangential支配；alg2沿后者下降，在tiny-dom支配时结束。k-broad对切于(k−1)维的家族消失，因此最终某个m≥k，但m未必等于4。所有管仍在原ambient Rn，m=4也不等于曲面坐标已把轴线变成R4直线。

§8对tiny O实际使用

    ||Σ_(T∈T[O]) χ_T||_(BL_k^(p_m)(O))^(p_m)
        ≲ δ^(−O(ε°)) δ^n (#T[O])^(p_m).

再以(51)/(52)、alg2的L1/计数属性及多尺度polynomial Wolff控制最大leaf管数，得到(53)的max-count形式。终点n没有变成m；`p_m=m/(m−1)`是这套计数插值的选择。用四维Hausdorff statement直接换p_m没有依据。原(44)只是broad非零，不额外保证原shading质量落在broad支持处。

## 4. DIR确实给弱删选，但这是已知正幂闭包

在四维原有限访问图上，原权ω_i>0，方向δ-bin总权≤α，W=Σω_i；每index/time-bin只访问O(1)个cells，固定着色后总访问≤δ⁻¹。任取原marks子集Y_i，令 `f(e)=Σ_i ω_i 1_(e∈Y_i)`。DIR对ε给η_D、Cε，则

    L≥2Cε αδ^(−ε)
       ⇒ Σ_(e:f(e)≥L) f(e) ≤2 δ^(−1+η_D) W.       (W)

证明按高重数cells上的原访问数将indices分heavy/light。light贡献≤δ^(−1+η_D)W。对heavy及这些原marks调用DIR，heavy贡献≤Cεαδ^(−ε)#E_L≤总高重数贡献的一半，移项得(W)。无需归一化权重或新独立化。

若原逐管有δ^(−1+η_in) marks且η_in<η_D，则删高重数cells损失原weighted incidence比例≤2δ^(η_D−η_in)。这是可调用的真实restricted-weak入口。然而反向用剩余访问量除以L即恢复DIR同级正幂union lower；heavy可从平均密度恢复逐管调用。因此它属于原uniform shading定理的合法闭包，不能另起新方向/新ID。只保总原访问不保每一原index；重新要求逐管须再heavy，不能混用。

高次矩可由很少原质量支配，所以(W)不保whole-tube Lp/broad范数。若在父包P内缩放到h_P=δ/r_P，其light预算是 `C h_P^(η_D) W_P r_P/δ`。把各父包相加需要真实Σ_P W_P r_P的原clock重复预算。alg1/2已有whole-broad/tube-count不等式没有自动提供该原染色预算。

## 5. whole-broad选择与原marks可以彻底错开

取满四维δ方向bush，所有原线过原点，原marks放在 `[1/2,1/2+2δ^η]`，δ足够小。它保H5的原满方向和逐管near-full密度。远离原点t处，一个δ-ball内相交管的方向落在O(δ/t)角cap；固定β时whole k-broad质量仅可能位于原点O(δ/β)邻域，与原marks分离。

因此直接在整管上运行现有HRZ后称选中tiny/切包承载原marks，是无效蕴含。本例的真实shading体积很大，不是H5反例。可以试图重新设计shaded算法，但需自己证明broad/narrow的原访问分裂、剩余原时间、父子重数及每个合格四维见证的密度。上述(W)不替代这些证明。

## 6. flat短包的方向费用与raw终点校准

取δ≪r≪1、h=δ/r、H={x₄=0}⊂R5，仍用过原点的原unit graphlines：三个切向slopes遍历固定小box中的δ-grid，法向v₄遍历宽c h的δ-grid。在原clock长度≈r内，pieces均在N_Cδ(H)，法向角≤cδ/r，保短段的全部原marks。轴线并非全程精确包含于H。

原index数 `m≈δ^(−3)/r`。空间与时间除以r后，厚度h，投影到H的每个h-direction bin有三个切向细/粗因子r⁻¹和一个被忘法向因子r⁻¹，故

    α≈r^(−4),    #coarse directions≈h^(−3),    m≈α h^(−3).

短piece并集≤Cδ r⁴，总piece体积≈m rδ⁴≈δ，故原labels与总piece体积相比的r⁴损失确实可发生。DIR带α调用给四维cells下界约 `m h⁻¹/α`（另付h^ε），回R5体积约 `m r⁵δ⁴=δr⁴`，与该几何尺度一致。tiny r=δ^(1−ε°)时α=r⁻⁴不是h的subpower；不能从原δ-separation推局部h-bin质量O(1)。此局部族只有m≈δ⁻³/r，不是原满δ⁻⁴方向H5反例。

固定有限A、2≤k≤4，先取β相对A足够小再令h≪β。H内3维方向patch不能被A个(k−1)-plane的Cβ邻域覆盖，至少一β-cap含c_(A,β)m根管并避开这些planes。在共同cδ-ball中它们同时出现，因而raw broad的p次方≥c δ⁵m^p。它达到tiny粗上界的主幂；当ε°可取得足够小时，没有对所有这类局部输入免费额外乘δ^σ的终点改良。k=5不适用，因为整个patch接近一个4-plane。

删掉原点O(δ/β) clock只损相对原短段O(δ/(βr))访问，却可抹去全部whole-broad支持。这再次校准(W)的适用范围。此证明只针对合法local terminal class，没有证明该族必是某个给定global HRZ运行选中的leaf，也不排除各层D/尺度的联合新估计。

## 7. 其它直接接法仍需的输入

保原δ厚度、不缩clock时，短段作为unitline shading只有λ≈r。tiny r≈δ^(1−ε°)不能保证满足DIR对任意target ε所需的λ≥δ^η_D。延长/复制pieces来补clock会改变原footprint或index计数，须另证明预算。

一般TCI的flatten还可能把直线变成曲线；固定degree不提供任意系数下一致curvature bound。即便已有可付chart把pieces送到共同H4邻域，§6的方向费用仍在。不能把这些未证接口加入假设后宣布获得H5。

可直接对原R5满方向family用FSD001，s=4、m≈δ⁻⁴、原λ≥δ^η，得到原#E≥δ^(−4+o(1))基线。它没有σ>0。旧HRZ broad/narrow的Lp障碍仅作历史对照，不算新数学结论。

## 8. 审计结论和停止条件已触发

本轮定位了真实tiny终点，保留了DIR确有的弱原质量入口，并严格支付flat短包α≈r⁻⁴及raw broad校准。没有得到同时保原shading、付重复clock、形成合法R4长直线见证、又在方向重数之后留固定正幂的估计。

故停止当前HRZ有限四维替换接口，不继续k/degree/radius/η阈值。此结论只否定本文所列免费蕴含，不宣称所有HRZ或shaded多尺度新算法不可能。H5未证未否，一般Kakeya、重大中间结果和优先权均未完成；registry不新增数学结果ID。后继必须先选不同的已定位责任，不能把(W)换名称继续循环。
