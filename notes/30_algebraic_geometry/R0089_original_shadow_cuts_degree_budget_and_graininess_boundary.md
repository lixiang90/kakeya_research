# R0089：原小阴影的几何cut、降次数预算与graininess边界

2026-10-18，root。完整spec门仍未证、未否。以下是实际原marks归约、具名全n几何cut工具的应用，以及两处具体桥反攻；不是普通新界、完整H5反例或重大结果，未经外部同行评审。

## 1. 原目标、排重与来源层级

原R5单位roundδ管T_i⊂B_R，原projective δ分离满角网J≈δ^-4，可测Y_i⊂T_i，逐管density≥λ=δ^η或平均I=Σ|Y_i|≥cλJδ⁴另记。E=∪Y_i。working_spec锁的主门问：在|E|≤δ^(1−γ)反设下，能否对每小ε选择γ,η，构造degree≤δ^-ε且保原incidence的几何cut模型，并付真实coarse四维调用，取得ordinary五维strict>4的结构输入。下面没有完成这条全门。

R56本来已假actual小footprint；其通用Taylor/Remez抽top系数路线已停止，不以补smallunion重做。新采用Guth1402.0518v1的cut方法：Definition1.1、Cor1.5、Lemma1.6实际全ambient，其几何正负体积条件不需控制outer/top coefficient。原Th0.4/Th2.2是R3且带技术假设，不把标题或全n单引理变成已证R5graininess。高级source责任按实际读域列明。

## 2. 共同shift保真实格点、footprint与原质量

取ξ均匀于[0,δ)^5，G_ξ=ξ+δZ5。令K_ξ=#(E∩G_ξ)、J_ξ=Σ_i#(Y_i∩G_ξ)。Fubini给EK_ξ=δ^-5|E|、EJ_ξ=δ^-5I≥cλJ/δ。单位roundtube含任意此格至多C/δ个点，故J_ξ≤CJ/δ。

以K_ξ>C_0λ^-1δ^-5|E|为bad phase，Markov给其概率≤λ/C_0。取C_0足大，E[J_ξ1_bad]≤(1/4)EJ_ξ。因此存在同一个good ξ使

    K_ξ≤Cλ^-1δ^-5|E|， J_ξ≥cλJ/δ。                 (1)

删除该phase上点数<cλ/δ的rows，只损固定比例总incidence；余J′≥cλJ，每row仍有≥cλ/δ真实原marks点，方向未改但不再literal满网。点集取固定格颜色使相应δ-cubes彼此距离≥Cδ，保常数incidence，再按同样重管筛选。最终selected graph A⊂{原labels}×{原δ-cubes}有

    K≤Cλ^-1δ^-5|E|， |A|≥cλJ/δ， J′≤J，
    每余row cλ/δ≤deg_A(i)≤C/δ。                    (2)

这里cube中心是实际格点x∈Y_i，cube可超出E，只用于几何建模；没有声这些cube并的体积仍是|E|，没有用NδE作代理。原physical cube侧δ；应用unit cube source前仅统一按δ缩放并保固定几何常数。

平均版(1)只用总I，同样可用，但不授原全部rows逐管门槛；重管比例λ和筛后N始终计。任意后续删labels或marks都按实际剩余图重算，不免费保ADlower/满方向/每point-star角度。

## 3. 全n cut工具及其准确作用

固定足小cut参数r0>0，只依维度。P在一个unitcube Q上cut at r0是：每个半径r0..1、中心在Q的r0^-1邻域内的球，P>0体积介于(1/2±r0)球体积。它比只在Q二分强，且不等于P在Q逐点为零。

具名Cor1.5给对任意K cubes的非零P，degree D≤C_{r0}K^(1/5)，同时cut全部cubes。其证明是细格多项式ham-sandwich；不靠approximate-zero或Remez系数外推。cut含一个cube内固定球的正负体积下界，relative isoperimetry给该球中符号边界H4面积≥cδ⁴。

具名Lemma1.6则对任意ambient：沿一根radius1 tube，若相距≥2n的anchors都cut at r，则除≤C_n r^(-4n)D个between-anchor gaps外，所有其余gap所碰unitcubes都cut at 2r。它不管最外anchors之外，且只计坏gap个数。原roundtube可放入固定倍柱体，所用cube/半径/分离的固定变更均由同一证明吸入常数，不产生δ幂。

原文该引理的证明直接以纵向rootcount控制各gap附近零面投影体积，比较纵移球的正号体积；系数大小、gradient floor均不在输入。本轮实际读完整证明，非把R3graininess换n。

## 4. 对原selected incidences可付的标准hyperplaniness

用§3的P切(2)全部K cubes。只取其符号边界的regular部分Σ；删除even factors及重数不增加degree且不改符号（零集measure0），故H4Σ∩Q≥cδ⁴，奇异集不承载H4。对每Q在Σ∩Q选unit normal n_Q，使

    Σ_(i,Q)∈A |n_Q·v_i|
       ≤Cδ^-4 ∫_(Σ∩Q) Σ_(i,Q)∈A |n(x)·v_i|dH4(x)。

可由有限被积函数的平均值选取；这里只控制原selected edges，不用whole-tube unmarked degree。对固定i，所有其访问Q均落在固定fat T_i。沿v_i平行线rootcount≤D、例外整线的横向参数为零测，coarea/Crofton给

    Σ_(Q:(i,Q)∈A) ∫_(Σ∩Q)|n(x)·v_i|dH4≤CDδ⁴。

因此

    Σ_(i,Q)∈A |n_Q·v_i|≤CJ′D，
    # {bad edges:|n_Q·v_i|>θ}/|A|≤CDδ/(λθ)。        (3)

在反设|E|≤δ^(1−γ)及λ=δ^η下，Dδ/λ≤Cδ^((1−γ−6η)/5)。η足小、取θ为该正幂的平方根，(3)保1−O(θ)原selected-incidence质量，其方向近某Q自己的4plane。没有每Q同一方向数/ADlower或相邻Q超平面一致性。

这是已知ham-sandwich/directed-volume机制的实际加权原图应用，不新登记工具或称major。它比重述‘小体积蕴含应有结构’具体，但远未付coarse graininess或δ^-ε次数门。

## 5. 原图均匀化可付什么，不能付什么

可对selected cube degrees dyadic分桶保≥|A|/O(logJ)边，再对row degrees分桶保另一个log。若该bucket upper row2M、upper col2ρ，初始col桶总边≈K1ρ，所选row桶总边A2≥K1ρ/L（L=O(log(1/δ))）。迭代删row degree<M/4和col degree<ρ/(CL)，每个节点只删一次，损失总数≤A2/4+A2/4，故留至少A2/2边。剩余row上下常比、col上下polylog比；原incidence及J′损失都要保在账上。

这只是近biregular selected graph。whole tubes碰同一cube的未标记次数可能更大；更不授source的局部非平行fraction、R3三方向、全局physical overlap上界或四次路径独立。原δ方向分离只给一个θ角帽至多C(θ/δ)^4个labels，在一个ρ-star中只能强迫θ≈δρ^(1/4)的粗角散开；不能当固定角或subpower角。任何删选后这些量仍须重核。

## 6. R3两跳的真实R5预算，未完成的新定理不伪报

源Th2.2在R3需每tube M..EM visits、每cube ρ..Eρ以及每cube相对任一方向有E^-1比例E^-1横截tubes。其proof以独立seed约D²根tube、每seed约D anchors，D³个cut约束，经过横截independence和另一个bad-rank质量估计，把cut传回多数cube。公式D≈K/M²的幂来自此R3维数。

若尝试相同几何算法在R5，degreeD的系数维数≈D⁵，至多约D⁴ seeds×D anchors。近均匀图的第一代给固定row的预期命中数约

    M ρ · D⁴/J′ ≈ M²D⁴/K。

要有远多于D个anchors以触发同一Lemma1.6，需要该预算满足

    D³≳K/M²。                                      (4)

这是特定两跳预算，不是任意P次数下界，也不冒成已独证完整R5技术定理。即使暂给最有利的subpower technical常数、K处在δ^(-4−γ)规模、M≈δ^-1，(4)对应D约δ^(-(2+γ)/3)，而非Crofton体积最优Kδ⁴≈δ^-γ或spec的任意小ε。真实λ、角度及均匀化费用只会增添责任，不得把R3字面公式直接搬来。

## 7. 更多代不自动降低门槛：明确有限图证书

为检验‘再传播几跳即可’这一步，单独考虑近均匀J0×K0 incidence graph：row degree≤2M0、col degree≤2ρ0、J0M0≈K0ρ0，任两row共有cube≤B。独立seed每row概率p≤cD⁴/J0。此是一个有限算法模型，不声原H5自动给固定B、均匀性或其全部几何。

固定未seed row i，能通过它的cube接触的其它rows≤4M0ρ0。令X_i为其中seed的个数，X_i是相应binomial，总hit cubes H_i≤B X_i。若t=ceil(D/B)≥E X_i，Chernoff给

    P(存在非seed row有H_i≥D)
      ≤J0 (e·4M0ρ0p/t)^t。

控制比率是C B M0²D³/K0。当它是δ的正幂、t≫logJ0时，此概率趋0。若所用算法只凭已certified graph intersections、每新row需≥D hits才能触发下一代，则没有首个新row，后来代也无法开始。它说明独立均匀的更多跳本身不赠K/M⁴；在低于(4)门槛时，independence甚至使首代启动稀少。

不排P偶然cut别处、利用未标记几何、相关seeding或新的原结构；不宣所有多代polynomial法不可能。此有限概率证书只证明其明列模型，不替代连续H5、Hausdorff或原source counterexample，也不登记新ID。

## 8. 坏gap数量与四维tangent二次型的具体边界

坏gap个数不能独自控制坏physical clock。固定r下可取P0(y1)一致近似高频sin(ky1)在所需固定横向盒上，使它在所有半径≥r的相关球中带余量地近二分：sign-sin的有界primitive给相对误差O((kr)^-1)，小一致误差仅改变近零薄条。取A>8||P0||∞，设

    P_L(y,t)=P0(y1)+A t(L−t)/L²。

L足大时，两端长S≪L的anchor clusters及其r^-1邻域内扰动微小，故多于C_r degP_L个分离anchors仍cut；中间t∈[L/4,3L/4]则同正号。一个长bad gap可承载绝大多数clock乃至原full marks。degree固定，S可远多于degree；但anchors并不按原full marks的rank均衡。此单管例只反‘数量⇒质量’，不满足原full方向小footprint。源Lemma2.4/2.5实际另用了rank-balanced sampling、横截独立与总visit账，不能删掉。

R3的三条不同null方向迫II=0也不可换成R5的线性方向展开。取光滑quadric Z={x5=x1x2+x3x4}。每点四个坐标切向都是整真实直线方向，线性span全部4维tangent；其第二基本型却是非零h1h2+h3h4。Sym²(T)维10，线性spread不授二次测试spread。在R3 tangent dim2，非零齐次二次在RP1最多两个零点，原三方向逻辑才有效。这个quadric的全局方向仅3维leading cone，不是fullS4/H5反例，也不排所有正确高维graininess方法。

## 9. 原coarse用途与完整目标准确剩余

§4的H_Q只对各cube独立给近切方向。没有证明H_Q沿原tube在ρ≫δ尺度慢转、没有extract保足够原W/I的grain包，也没有能恢复四维投影全局cap的质量分解；不能套R87未证G4或把高degreeδ依赖carrier当fixed-format G3。坏gap的rank/clock和II的Sym²责任均真实存在。

完整spec降次数/coarse门未证未否。新primary工具确避了R56的topcoef norm conditioning，但不解决其余次数/原质量责任；不回通用Remez、degree/λ/r小调。ordinary、directHRZ、sticky完整余分支及ordinary桥、同一full方向低维构造四主路保留。旧DIM001/R38/R80已付部分不伪列gap。

## 10. 审查、来源归档与停止

新Guth原PDF40页/478336bytes，SHA256 a0ce228a06daf32f46897c6ace390dc34fae2a5ce378d918ef2cc245e2b0159b，blob87cf245447b99d4a2a382279f1c77eac88abf2bd。root实际intro/Hyp0.2、Th0.4/0.5、完整§1及§2.1–2.2原证明、view物理8/13；文献全40页高级curvature/graininess proof未本轮新独证。原page13比较Crofton处有不等号排印方向：由area≥K与≤DN²应读D≳K/N²，不以该处文字误字否整定理。原字节不改。

A/B主稿及两份实际全文正式独审后才内部有限reviewed，非外部peer。65PDF/69sources/78IDs，无新实验/ID/ordinary改善/full方向反例/major。保守ordinary/fullbranch-saving streak12不由工具应用清零。停止这次cut-degree-graininess直接接法，不以更多跳/二次spread公设或另quadric模板续轮；当前无qualified新gain，Goal active，不complete/blocked。
