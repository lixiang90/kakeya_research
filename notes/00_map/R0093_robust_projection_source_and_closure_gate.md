# R0093：稳健投影的原来源、真实BP与删选门槛

2026-10-18，A。恰八个编号二级节，只作已锁资格审查。全目标不变；没有锁定新维数gain、newID或重大性。未经外部同行评审。

## 1. 实际恢复、版本及正确编号

实际读GOAL、当前STATE、R92 next六节和R93 reselection_spec五节；全部路线、78项registry及R92原数学／两formal沿同会话的实际读记录使用，不冒一次新Git或远端检查。ordinary多尺度初始化、directHRZ完整费用、sticky临界κ1／余mixed与ordinary桥、同集full方向严格低维构造四完整路径均仍open。R92算术精度、R91标准rank／C1、旧cut／cone／polar／跨块及CP/PM/PW冻结不因新题名解冻。

本次fresh打开[Orponen官方history](https://arxiv.org/abs/2008.08843)：v1=2020-08-20、v2=2020-09-01、currentv3=2021-06-21。实际读[v3原PDF](https://arxiv.org/pdf/2008.08843v3) physical1–5完整引言、定义、statement、Question1及notation，并对照HTML和root新存的同stem提取文本；另核§4 Prop4.2的常数声明和§7.3收尾对应接口，未独证全部40页高级proof。PDF正文June22,2021与arXiv标签日期分开；HTML重编2026日期不是新版本。本人未下载或核PDF整字节。

实际v3的BP/PBP为Def1.2，投影不等式编号为(1.3)，主定理是**Th1.6**，不是Th1.3。已消息parent纠正定位。David–Semmes、Besicovitch–Federer、rectifiable tangent、面积公式等按各自标准具名范围使用，未因引用而认证其全部外部证明。

## 2. 原定理量词、尺度与定量范围

源中的n-regular是closed E⊂R^d且H^n⌞E对每个x∈E、0<r<diamE有同一个C_0的上下r^n界。BP只要求每个(x,r)存在一个V_{x,r}，使H^n(π_V(E∩B(x,r)))≥δr^n；PBP要求同一V_{x,r}的整个Grassmann球B(V_{x,r},δ)中的所有V都满足该lower。δ固定，不是工作网格δ→0时可任意退化的小数。Grassmann metric是两个正交投影之差的operator norm。

BPLG意味着每个原ball中有H^n质量≥θr^n的E∩Γ，Γ是某个n-plane V上的L-Lipschitz graph，V可随ball改变。Th1.6给PBP⇒BPLG，配源原有的反向即相应regular类的表征；不是BP⇒BPLG。源Theorem1.5把BP与另一个WGL输入一起使用，WGL不能免费赠送。引言明确以four-corner Cantor的BP非BPLG说明已知障碍，不能将本轮数字版本当新发现。

notation及Prop4.2的依赖是ambient d、regularity C_0和PBP常数δ（另有局部证明的ε等参数）；没有本轮可直接调用的显式θ≥δ^C或L≤δ^{-C}统一幂式。只在有限mesh以上joint AD、或PBP常数随mesh退化，不等于已验证连续定理的固定量词。源§1.3 Question1还明确区分一个固定大ball里的投影信息与全ball／更小尺度PBP；不能把该问题当单scale版本定理。

## 3. 一个固定方向真的大：F^4给原joint4-AD及完整角度

令A={Σ a_j4^{-j}:a_j∈{0,1}}、B={Σ b_j4^{-j}:b_j∈{0,2}}，F=A×B。每个digit和a_j+b_j唯一取0、1、2、3，因此A+B=[0,1]。取x∈A^4、y∈B^4，并作固定可逆线性变换

Z={(a,v)=(x−y,x+y)}⊂R^4×R^4。

原product是256个ratio1/4同向homothetic copies的强分离自相似集；level-k copy的Bernoulli质量4^{-4k}、直径≈4^{-k}，不同copy有固定比例分离。球r≈4^{-k}至多遇固定个该层copy，而包含中心的更细copy整体落球内，故原概率上下≈r^4。这给真实4-AD，且与H^4⌞Z双边可比；不是只声明Hausdorff维数为4。

π_v Z=[0,1]^4，原Bernoulli law的π_v pushforward恰Lebesgue概率：四个坐标的和digit均独立uniform于0、1、2、3。对任意z∈Z与r，球中还包含一个尺度s≈r的完整level cylinder；它的π_v像为边长s的cube。因此**同一个固定方向平面**V_dir={0}×R^4就满足局部投影lower≥cr^4。global full角度、其自然law的全尺度下界和local BP都真有，不是仅有一处大投影。

这比只反global angular→local BP更精确：本例已经有local BP，真正不能免费升级的是其附近一整个Grassmann开球。其余physical line／CW和有限族规范须另核，不能由joint AD这一段独自声全部原source。

## 4. F^4确为纯4不可整流，故不是隐藏PBP输入

可用经典自相似整流性及Besicovitch–Federer作为具名结论；此处另给具体几何核验，避免只把“乘积”当pure证明。原A^4×B^4包含0及八条坐标轴上的非零点，affine span为R^8；固定线性变换后的九个点仍张满R^8。因Grassmann紧性及可限制有界offset，存在c>0，使任意affine4-plane至少距这九点之一≥c。由AD lower，该点附近的一小块Z质量≥c′并远离该plane。

在任意z、任意小r的完整level cylinder里缩放这九点；整个copy位于B(z,r)，尺度与r可比。所以对任意affine4-plane L，有固定c_1,c_2>0使

H^4((Z∩B(z,r))\N_{c_1r}L)≥c_2r^4。

这排除近似4切平面。若Z与某countably4-rectifiable集有正H^4交，取交集相对于AD测度的density点及rectifiable近似切点，上式的固定远离质量将同时须为o(r^4)，矛盾。这里density theorem及rectifiable tangent characterization是标准具名输入，具体非平坦质量已经支付。故Z为purely4-unrectifiable，0<H^4(Z)<∞。

因此没有任何positive-H^4 Lipschitz graph piece，不能有BPLG；接受正确Th1.6即知不能有PBP。也可由标准Besicovitch–Federer得到几乎每个G(8,4)投影的H^4为零，任何非空Grassmann开球含这样的plane，直接排任意中心的PBP。固定V_dir投影满立方体与此不矛盾，单个例外方向不代表邻域。此为经典BP／rectifiability障碍的项目量词应用，不新立定理或ID。

## 5. Convex Wolff、全clock与完整source不能混用

本例的graph lines是(a+t v,t)，t在固定单位graph-clock I中；每个v∈[0,1]^4有实际标签，真实Euclidean长度统一可比。完整S4需要另作有限方向chart／旋转与单位长度规范，不能只称一个proper slope patch已经是全方向Kakeya。B负责其实际构造、并集体积／Hausdorff与finite δ-family；A不预认证尚未读到的B稿。

仅为了比较本门的whole-containment凸CW，方向概率本来有bounded angular density。固定有界单位axis／round tube若整体包含于convex U，用John box宽度r_0≥…≥r_4；r_0≳1，方向在四个横向坐标上的angular范围至多固定倍r_1,…,r_4。故连续whole-axis事件概率≤C∏_{j=1}^4min(r_j,1)≤C|U|；原δ-direction-separated tubes的版本在U可含整δ管时由同一angular packing得#≤Cδ^{-4}|U|。这不需要位置selector正则。该意义的凸CW并不升级为R^8上所有π_V投影的稳定lower，亦不默认更一般partial-intersection/full polynomial-Wolff测试。

反例当前核的是joint4-AD＋full angular/local BP不能免费给PBP。它不自动满足Def17全部filledX、pointΦ、selectedξ、tubeKT与原小阴影／跨尺度关系。若后文用更强CW或full PW，必须保其query及原N/I另付；不能拿这个generic模型反完整source。也不将Lebesgue零并集误称Hausdorff小于5，原Goal的两个结论不能互换。

## 6. BPLG并非关于原方向的graph，真正条件出口是什么

Th1.6中的graph base是任意V∈G(8,4)，不保证是V_dir或π_v在该graph上injective。甚至一个纯position4-plane本身BPLG，而π_v为零。故选出一个大joint-H^4 graph piece，不能立刻把它写成a=a(v)或认其保原角度质量。global full π_vZ也不说明某个预先指定piece有positive π_v-image。

一个可具名且应单独证明的条件出口是：若整个Z有限H^4、countably4-rectifiable，且|π_vZ|>0，那么原common-clock union有正5体积。理由是countable Lipschitz charts中必有一片π_v-image正4测度；面积公式和nonsingular Lipschitz分解给positive-measure方向域上a=a(v)的Lipschitz graph。延拓后Da(v)几乎处处存在，映射(v,t)→(a(v)+tv,t)的Jacobian为|det(Da(v)+tI_4)|；其关于t是monic degree4多项式，故几乎处处非零，面积公式给正5体积。

这是整个countably rectifiable对象加方向投影质量的条件推论，不是把一个BPLG piece的方向质量免费补上；所用graph分解／面积公式仍具名。它也未给任意finite δ及λ的uniform正幂估计。原输入不能推出PBP，所以不能借该条件出口解ordinary或完整source。root将独立写这一出口，本稿仅定位量词，待实际主文再审。

## 7. Restriction、平均／逐管shading及旧等价停线

任意label子集只自动保AD upper，AD lower与uniform PBP不能一般继承。简单闭集校准已足：在原平面单位cube内保一块固定正体积，再加向0聚集的极小不交balls及0，令每个tail的质量远小于相应半径的四次方。所留总质量可固定为正，但0仍在support，AD lower失败。平均heavy删选保λ比例原权／incidence，不会修这一几何条件；不能归一子族后照抄C_0与PBPδ。

只删clock而保全部labels时，joint参数Z的PBP若原来成立可保持，因为Z未变；但所得big piece是否带原marks另是一问。逐管density≥λ使一个真正原label piece至少保相应λ-incidence，平均density只控全族，marks可避开某个预选piece。无论哪种情形，有限shading都不能无额外说明变成连续H^4全尺度regular set，或让source的固定constants保为δ^{-o(1)}。要应用源必须支付实际选中labels、方向投影、时钟及原权分母。

已实际重读R15 uniform_shading_closure全四节与R62主稿§§14–18：CP/PM的全称合法shading量词使存在正gain等价；完整PW4的unshaded/shaded/projective门在其具名有限输入下亦同一正幂责任。不能把“从所有原子选择抽PBP／rectifiable pieces并返回gain”直接写作成功假设，再当不同正机制登记。此处不宣PBP本身与CP/PM双向等价；实际结论是上游免费PBP推论已经被更强的local BP模型否定，条件BPLG后果不替代未付原输入。

## 8. 当前判定、审查范围与停止

来源正确入口为closed全尺度n-regular＋PBP，当前v3 Th1.6确给BPLG；BP、global full角度、局部一个方向投影和凸whole-containment CW各不是该输入。F^4的joint4-AD、完整方向law及fixed-plane local BP已逐步核，纯4不可整流也已给具体量词依据，故不能把它当偷偷满足PBP的模型。经典four-corner障碍与本轮复用的地位明确，无新发现认证。

建议拒“原joint AD/fullangular/CW免费推PBP”作为新gain门，不续单方向大小或有限尺度常数优化；不以假WGL、graph base=原方向或desiredPBP重名开方向。完整Kakeya/source仍未证未否。B全稿与root整合主文尚待其落盘后实际全文互审，本文不预记通过；后续formal仍需单独授权。未经外部同行评审，无newID、ordinary新增益或major，仅本A8与实际消息范围，无Git/meta/download/spawn。
