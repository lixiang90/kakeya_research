# R0069：官方核心版本、完整Goal与原native双锚点审计

2026-10-18，A。只编辑本assigned稿，无Git／spawn／元数据改动。已实际恢复GOAL、STATE／ROADMAP顶部、registry全部78项状态、R68交接和R69 spec5／opening macro3。§§1–7保留阶段I来源／候选筛查；§§8–13在root随后锁定spec后追加阶段II数学，不先施工未选任务，也不把宏观报告算本轮数学完成。

## 1. 完整目标和本轮边界

Goal仍是ordinary Euclidean n≥5／general的完整证明、真实全方向反例或有文献比对支持的重大中间结果。现有DIM001是具名输入下的六维17/4链；R29 finite seed／KT、R38内部assembly以及后来shading模块的实际范围保留，不能把它们换名作本轮新结果。没有普通五维新界或major认证。

R68已付的具体新准备是：每个指定原allowedρ各有自己的足量整time S，使raw T(S)≤ρ^(3−ζ)，不预AFF／NQ。它不提供一个共同多尺度S，也不读出whole矩阵a,b的affine结构；原mixed43的contact耦合及其他五维分支、ordinary初始化仍须逐项处理。19.5／13.5等高级wholeproof仍具名，不把OpenAI署名或内部复核当外部正确性保证。

## 2. Fresh官方GitAPI及README／history实际读取

本轮通过Git connector只读公开API，实际读取[root main tree](https://api.github.com/repos/openai/math/git/trees/main)、[preprints tree](https://api.github.com/repos/openai/math/git/trees/df0564b2deaab87e07854b6344d8c2f037682e77)、三个子目录tree，以及总README／history和三篇manuscript README的全文。当前root tree仍为`1581d4cbdd69a0faf34b2089614fe2a814316a6a`，preprints为`df0564b2deaab87e07854b6344d8c2f037682e77`。

| 稿件 | 目录tree | PDF blob／bytes | README blob |
|---|---|---|---|
| OAI4，2026-09-24 | `807c97661f95850b7c324356febc3774e7c51c86` | `45ec20e423db2a9c70fd6303510bac361e6e9e8a`／1371486 | `b3a0eeeb593be4e7d59e6f4e6e9ecd145796e624` |
| M3，2026-09-23 | `b3ef56e6408c303f96e3f3d8f9771cbea2ec703b` | `fa215607c58ade54fc6d60dec81530b33f15ab0c`／925416 | `81a1e551c93a964576cc77eab7fb760b385d29a9` |
| elliptic，2026-09-24 | `b2736db3ad1d72483f2eff2c852f4484cf3915b6` | `5b13ea550428fb8701da1f40c1fb7e5820838211`／945868 | `0ff38e654a636dde651971d4bf6865018b35603a` |

三者均与R66的actual核对相同。三manuscript README只给题名／作者／原发布日期／citation，本次未见新版本、修复或撤回通知。总README blob为`50feb63d396138f30dc1ff1e0af121d0263bf5a3`，history blob为`693874f398905b1bc59e01b898b223ae9956bfc2`；history的Oct7条目涉及其他稿件，不构成这三篇已被新修复或已形式化的证据。总README本身仍区分不同验证阶段，并提醒未形式化结果可能有问题。[官方README](https://github.com/openai/math/blob/main/README.md)、[history](https://github.com/openai/math/blob/main/history.md)。

这次读的是API JSON中的tree/blob身份与README文本；未让工具按UTF8解析PDF二进制。PDF身份通过下节本地字节重新计算交叉验证，没有重下相同PDF。

## 3. 本地bytes与真正statement范围

对当前本地PDF重新读取全部bytes并计算SHA256及Git blob（`SHA1("blob "+length+NUL+bytes)`）：

| 本地PDF stem | SHA256 | 本地Git blob |
|---|---|---|
| openai_2026_four_dimensional_kakeya | `30d0c186aa9c697d02ab9bf736968028f1ce8a2f164f1d7291398d530035ccde` | `45ec20e423db2a9c70fd6303510bac361e6e9e8a` |
| openai_2026_three_dimensional_kakeya_maximal | `49cc52aa3de89f0e91d181b00ee8050fb29635ee0da9f29145d52318e7168204` | `fa215607c58ade54fc6d60dec81530b33f15ab0c` |
| openai_2026_elliptic_capacity_sphere_restriction | `669efdbef915014402795e07bfbcb958ae534b6910f05a8737a6fce0c216d394` | `5b13ea550428fb8701da1f40c1fb7e5820838211` |

本轮实际重读OAI4 Th1.1和§11相关声明：其结论是任意R4 Kakeya集合的Hausdorff维数4，允许非可测K／非可测segment选择。direction-set／line-extension及曲线后果有各自具名transfer，不能单凭dim_H=4改成任意single-scale四维maximal。现有SRC001／DIR003是本项目另外核过的有限读出，仍带完整源输入边界。[官方OAI4目录](https://github.com/openai/math/tree/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026)。

实际重读M3 Th1.1、§1.1、Cor11.1／11.2：Th1.1对每ε给R3的L3→L3 Kakeya maximal δ^-ε，具有任意密度λ³而非只近full。局部Nikodym／曲线后果仍是R3及固定geometry；Cor11.2采用固定translation-invariant phase、Hörmander与Bourgain条件，比较常数可依phase／chart，未提供R5 arbitrary moving-grain直线化。R53／R60已付的exact／near-variety fullλ应用和R61 tiny-terminal饱和仍有效，不能重登记为新高维工具。[官方M3目录](https://github.com/openai/math/tree/main/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026)。

实际重读elliptic Th1.1、Cor1.3及§2 Th2.2完整假设：前二者是S²→R3的p>3 extension及R3 maximal，非一般S^(n−1)结果。Th2.2允许所有固定0<s≤1，但按确定(U,V)的base label要求每depth的conditional time upper与support两界；初joint test为同shape、独立中心的两ellipse，带实际K及M^-D floor。输出保left-bin `X_v=V+vU`，terminal floor升至M^-(D−1)，只保证一个dominated大质量sublaw。R57已经付过scalar-block charged aggregation不能免费成为原joint gain；all-s标题没有取消joint K、原mass或条件time责任。[官方elliptic目录](https://github.com/openai/math/tree/main/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026)。

上述是新版本核和statement／接口范围重读，不声97／103／175页全部高级证明在本轮重新认证，也不以官方无变推断证明无误。

## 4. 有界一手机制比较：未发现立即可付full5D新输入

本轮只打开下列已定位primary页面／声明，不再穷举广搜；无新PDF或source入库建议。有限未命中不能证明无新定理或认证优先权。

1. [Wang–Zakharov 2609.22035](https://arxiv.org/abs/2609.22035)：官方history仍仅v1，2026-09-18；其sticky R3 Furstenberg／sticky R4 Kakeya结论仍不能跳过ordinary到sticky和高维matrix／mixed的原前提。HTML本次一次Internal Error不等于版本未核；abs history已实际读，本地原statement／Def17和后续输入已有实际阅读。
2. [Cohen–Shmerkin–Wang–Zakharov 2610.13682v1](https://arxiv.org/html/2610.13682v1)：history仍v1 Oct9。本轮实际读Th1.2／1.3及离散定义。高维Grassmannian结论要求每尺度局部Schubert非集中／spread-out，给典型投影或dual plane-family维数；这不是原g边际的global slab upper。原模型若要用，必须支付这个局部非集中及与原输出共用的质量，不能由AD上界、一个generic rank或删掉g直接调用。
3. [Nadjimzadah 2511.10918v4](https://arxiv.org/html/2511.10918v4)：当前页注明2026-08-18。本轮实际读Th1.17／1.23及§1.4范围：同维classical sticky输入推出Bourgain-condition curved sticky，不是普通R5到sticky归约；其局部直线化不能当跨所有管／尺度的统一坐标。[真正lifting稿2609.06299](https://arxiv.org/abs/2609.06299)与此文不同，不能混用书目；R50完整保clock的smooth lift分类仍冻结。
4. [2610.05404v1](https://arxiv.org/html/2610.05404v1)：只实际读family定义和Th2.2，未审全proof或下载。该文报告特定曲线族的分数维压缩，非ordinary直线Kakeya反例，也不送本项目原rough mixed族的全mass比较。它可作曲线transfer反攻，不能作为当前full5D正向输入。

这一比较没有发现可直接替换完整原五维coupling的新定理。它不是exhaustive frontier或best／first认证；WZ higherdim／普通维数前沿的既有HRZ／KT／GLX等仍按已审精确scope使用，不重新算旧gain表冒新数学。

## 5. 完整Goal各路线仍须支付什么

| 原路线 | 可实际调用 | 仍未付／本轮不能重开成新方向 |
|---|---|---|
| ordinary R5初始化 | 原direction-separated输入与sharp PW | small union不自动给joint4-AD／allscale jointcover；R49附加nearsticky类不是一般归约 |
| 四维seed／高维递推 | SRC001／DIR003／FSD001及具名KT；DIM001条件17/4 | 不认证无条件／新颖界；更高n继续同KT数值闭包已冻结 |
| arbitrary fullλ到低维carrier | M3、R59／R60一般三维代数marked／wholeaxis transfer | R61 actualHRZ m3 tiny终端同主幂饱和，m4／narrow未被替换；R63条件R4 planebrush桥非ordinary改进 |
| PW4／projective／Nikodym | R62有限原marks、same-radius continuation与三向闭包 | 全称正gain为同一难题，不能把adaptive projective改名独立路线或免费query随N长格式的union |
| d5 matrix及mixed32／42 | 原source工具、已付proper二次和scalar准备 | matrix非线性joint output／mixed32向量非二次；mixed42 localCF端点无strictgap；旧W独立化／rank-only／localGWZ均冻结 |
| mixed43完整原数据 | R66 tiny lower、R67 natural joint图、R68无AFF/NQ large upper | contact尺度必须保(d_s−d0)Δa及第二row，不能h单row代wholeAFF，也不能不同S或两个dense图免费取交 |
| 构造／反例 | FD–deLaSalle原全方向构造和已审coherence桥 | cyclic一般粗selector仍未得power；有限碰撞lower、低conditional entropy门槛非真实全方向counter |

具名文献可作为输入使用，不要求为了结束一项完整应用而递归重证所有已发表高级定理；但新OpenAI／其他预印本wholeproof未独立认证的边界仍须明列。不能把fullsource=false本身当本轮新缺口。

## 6. 候选比较与阶段II前的建议

当前证据没有支持从新标题转向一个已能处理ordinary full5D的外部机制。若保留mixed43，真正尚未被大τgate读取的是原contact的第二row／coupled信息。单锚点h=b−d0a的任何proper后果仍不足；两个不同native锚点或原nested jumps若要有作用，须先给同一原共同tuple、原time／角reference、joint恢复fibre及global mass，再证明这些数据能读出独立于h的约束。原d(t)不得被重新参数化冒straightline clock。

这只是锁题前的责任比较，不把“需要第二row信息”包装成已找到机制，也未先施工新计数。R67 finer contact matching仍有其真正normal-label精度费用；R68的T upper只缩短τ范围，不自动支付它。若root提出两锚点机制，首先应攻击：同一rich slice能否同时保两锚点、二次clock项是否因耦合而改变、conditional time下界与原slab是否仍同prior、其原质量能否在完整global minimum／CW量词中回传。若只能添加AFF／rank／smooth／rational假设，立即视为旧proper子类回圈。

阶段II仍由root先追加spec后唯一选择；A此时不预选新命题／新名称、不称ordinary或wholeAFF进展。阶段I已完成的实质是fresh权威版本／本地bytes核和当前输入边界比较，而非数学主任务结案。

## 7. 限制、反攻和停止

restriction检查始终分平均与逐管：whole-time restriction只按原T分母重计平均，core逐active tube下界来自实际peeling；定性segment-extension不替代single-scale nearfull/shading。source slab、projection law及maximal输入每个都保原质量和方向分辨率，不由两个各自dense图取交。proper低维／特殊光滑类的可证后果不完成一般目标。

当前没有新full-input或严格countercert；不以此断言不存在。停止官方同blob重复下载、KT算术、HRZ终端norm与scalarK／strip、旧contact有理／smooth toy和大τ阈值续轮。待root锁唯一phaseII后再按原量词施工；本稿可依该授权追加本轮数学，当前不提前认证。无新ID／major／新颖性／外部同行认证，Goal active。

## 8. 已锁阶段II：原d的局部不聚集

以下依root随后锁定的spec§2施工，不是阶段I预先选题。固定完整mixed43、原allowed `δ^(1/4)≤ρ≤δ^µ`、`0<β<1/4`，取`0<ζ<min(1/10,1−2β)`。由R68先在同一原ρ取得原整time S，`#S≥δ^{a_*}#Z_original`、`ρ sup_sameJ ||E||≤ρ^{3−ζ}`；a_*可在以下阈值后任意小。原f、tildef与原whole T完全未改，tildef=(c,d)、c=b−da。

令`h=ρ^{1+β}`。断言：存在足够小、仅依固定参数的u>0，源η最后小，则任意原ρ窗J及任意长度h的区间I都有

    #{z∈S∩J:d(z)∈I}<δ^u ρ/δ。                              (2)

证明不需要重选q，也不把该局部簇当新的global time配置。若D为反例集合，取实际z0∈D。对t,s∈D，精确关系为

    c_t−c_s=E(t,s)+(d_s−d_t)a_t。

原a bounded，故`diam tildef(D)≤C[ρ^{2−ζ}+h]≤C h`，最后一步用β<1−ζ。取σ=C h；δ小后`ρ²≤σ≤ρ`，且ρ≥δ^(1/4)≥δ^(1/3)。原Z是δ-separated，`#(Z_original∩J)≤Cρ/δ`，所以D在**原分母**中的相对质量≥cδ^u。对删选前完整原配置和实际anchor z0直接调named19.4（常数可由把density指数改为2u支付），得到

    CW(T)≥δ^{C(η+u)/γ}(ρ/σ)^κ
          ≥C^{-κ}δ^{C(η+u)/γ}ρ^{-βκ}。                      (3)

因ρ≤δ^µ，先取`C u/γ<µβκ/4`，再取η小，使(3)违原CW≤δ^-η。19.4只在此调用其原完整源量词／高级wholeproof，未在本轮重新证明它。其证明实际使用局部绝对clock量，现`#D≥δ^uρ/δ`已经直接提供，不能只有一个极稀窗中的相对比例。

最简办法因此无需把S重命名参数或换allowed格。若坚持在重命名S配置上调用，可取共同嵌套的上邻allowed R∈[ρ,δ^-ηSρ]；D在R窗比例≥cδ^{u+ηS}，σ=C h仍满足R²≤σ≤R（`2ηS<µ(1−β)`），得到相同gain至δ小幂。这只是保守备选，不是合窗后声整个R窗tildef慢。

## 9. 同一原L图和不聚集的normalized代价

在此S上重新good-q／native L；不沿用R68删前的图。按原绝对heavy窗和good-q供应，某q在一个原J中有`m_q=#Z_q≥K^{-C}ρ/δ`。K=δ^-C(η+a_*)/γ只计本source质量，原T／CW分母不重归一。原22.1只需选角前upper，取`τ≈_K max(δ,T(S))≤Kρ^{3−ζ}`，不要求q内达到global sup。原native L给fine scalar carrier A_in／A_out、原ν=Uniform(Z_q)及ordered proxy pair referenceΩ=H²上的

    0≤g(x,t,s,ω)≤1， Eg≥m0≥K^{-C}，
    y=x+(s−t)E(t,s)ψ(ω)+O(e)∈N_(Ce) A_out，
    e=K^C(τρ+δ)， ψ(ω)=φ1−φ2。                              (4)

x、y均保physical native单位，所在patch长O_K(τ)；ν仍是原fine times。Ω是本L自己的used-angle prior，ψ推前law π有合法base Cρ以上的slabγ；不将g条件边际当独立π。full scalar Y用于AD packing和tube-KT，不借ell二维Y的line-KT。

(2)转到q后，对任意长度O(h)区间I，

    ν{d(s)∈I}≤K^C δ^u。                                    (5)

常数长度扩张用固定数原h区间覆盖。这里不是给d重新参数化后的clock授1-Frostman；真正time cap仍是原δ-separated ν，对physical长度ℓ的区间有`ν(I)≤K^C(ℓ/ρ+δ/ρ)`。先u固定，再a_*与η小于u及m0所有固定次数需要的阈值，故(5)可小于m0的任意指定有限幂。

## 10. Two-fan：保同一输入、原clock和共同proxy

以 `z=(x,t,ω)` 表示共同reference，其余变量仍是原s law。Jensen给

    ∫ [∫g(z,s)dν(s)]² dz
       =∫g(x,t,s1,ω)g(x,t,s2,ω) d(x,t,ω,s1,s2)≥m0²。          (6)

`|d(s1)−d(s2)|<h`部分因g≤1至多K^Cδ^u，与(5)一致，不需对任何已条件化的角law赋slab。再删`|t−s_i|<q0ρ`：原time cap给总reference质量≤`C K^C(q0+δ/ρ)`。可选q0=K^-C并使δ/ρ项也远小于m0²；u／source loss在固定有限次数后选，余(6)仍≥m0²/2。

先Fubini选一对实际s1,s2，满足`|d1−d2|≥h`，并令

    H(x,t,ω)=g(x,t,s1,ω)g(x,t,s2,ω)
              1_{|t−s1|,|t−s2|≥q0ρ}。

则0≤H≤1、`E_(x,t,ω)H≥m0²/2`。再固定一个真正proxy pair即可保共同(x,t)质量，或继续下一节的两角处理。它不是从两个独立证明的dense图取交：两份g同一原reference、同一x/t/ω，平方矩先计费。fine exact角可随各L见证变化，(4)已支付proxy误差。

两L见证共享的是native scalar observable x（至原fine O(δ)），不自动共享完整physical endpoint或原管。若后续需要那个更强共同trunk，必须另付恢复重数；本证明不作该升级。所有删去的坏set由原reference及g≤1支付。

## 11. 两个原角和whole row2的真实恢复

为避免一个scalar projection冒whole row，再在同一H作一次angle平方矩：

    ∫_(x,t) [∫_Ω H(x,t,ω)dΩ]²≥(m0²/2)²。                    (7)

π slab upper使`|ψ|<r0`的reference概率≤K r0^γ；在`|ψ1|≥r0`时，`|ψ1∧ψ2|<r1`是ψ2的一条宽≤r1/r0的slab。先后取r0、r1/r0为足小K固定幂、均≥Cρ，使两坏角贡献小于(7)的固定比例。故可固定两个实际proxy pairs，令`Ψ=[ψ^(1) ψ^(2)]`满足`||Ψ^-1||≤K^C`，并保共同(x,t)的K^-C质量。再Fubini固定一个真实x，留K^-C原fine ν-times。此时每个t有四个实际native输出`y_i^ℓ(t)∈A_out`（i,ℓ=1,2），它们可以随t变化。

记`A_ℓ(t)=a(t)ψ^(ℓ), B_ℓ(t)=b(t)ψ^(ℓ)`、`C_iℓ=B_ℓ(s_i)−d_i A_ℓ(s_i)`。原输出(4)给

    B_ℓ(t)−d_i A_ℓ(t)
       =C_iℓ+(y_i^ℓ(t)−x)/(s_i−t)+O(e/(q0ρ))。

设右侧无误差项为Z_iℓ(t)，则

    A_ℓ(t)=(Z_1ℓ−Z_2ℓ)/(d2−d1)+O(K^C e/(ρ h))，
    B_ℓ(t)=(d2 Z_1ℓ−d1 Z_2ℓ)/(d2−d1)+O(K^C e/(ρ h))。       (8)

其二乘二物理det为`(s1−t)(s2−t)(d2−d1)`，下界q0²ρ²h；inverse的正确upper可用entries的O(ρ)把误差化成e/(q0ρh)，不额外浪费一个ρ。再乘Ψ^-1得到完整a,b两row，全部K有限幂明计。

由τ≤Kρ^(3−ζ)、δ≤ρ⁴，必须保原e中的τρ，恢复误差为

    K^C[τ/ρ^(1+β)+δ/ρ^(2+β)]
        ≤K^C[ρ^(2−ζ−β)+ρ^(2−β)]。                         (9)

因此首项是τ/ρ^(1+β)，不能在展开时漏掉e中的一个ρ。任取`0<ε0<1−ζ−β`，source loss后小可把(9)压到ρ^(1+ε0)。所以恢复**数值误差**确实足够精细；这仍不等于输出主项是affine。

## 12. Adaptive native labels的实际cover与AFF责任

设目标精度r_aff=ρ^(1+ε0)。为使每个输出label粗化后的(8)误差≤r_aff，取native physical mesh

    ℓ=K^{-C} ρ h r_aff=K^{-C}ρ^(3+β+ε0)≥δ。                  (10)

最后不等式由ε0<1−ζ−β及δ≤ρ⁴支付。原Y的完整AD packing（非给裁切patch授lower）给每个O_K(τ)输出patch的ℓ-cover upper

    N_ℓ≤K^C max{1,τ/ℓ}^{1−κ}。

四个输出组合因此给一个诚实的whole-(a,b)参数化cover，大小至多

    K^C max{1,τ/ℓ}^{4(1−κ)}。

在允许的最坏τ≈ρ^(3−ζ)时，此证书可收费

    K^C ρ^{-4(ζ+β+ε0)(1−κ)}。                              (11)

x已经由Fubini固定，不能再多算或反过来免费去掉四个随t改变的y。若不固定x，则还多一个native cover因子；本稿使用较强的固定x版本。(11)是当前cover方法的upper，不是所有策略必须支付的lower，更不反完整source。仅按它pigeonhole不能保证任意小原time loss的冻结；actual四输出可能有额外相关性，但尚无已付估计读取它。

即使固定某组coarse y常数，(8)仍含`(s_i−t)^-1`，给带两锚点分母的rational clock曲线，而非affine函数。在有原time密度的O(ρ)区间上仅知原Lip，并不让其Taylor误差自动为ρ^(1+ε0)。不能把原clock换成d，也不将该rational family再作为额外low-degree假设重开R65 proper类。

因此本轮已真实尝试whole-matrix恢复：两个不同角读取完整rows、native误差足够，但当前label参数化并未给AFF₃。仍缺的是同一原graph中四个adaptive输出的结构／增长或与原W联合数据的非平凡约束，不是再作一个除det或time重参数化。它须有完整原质量来源；未制造一个新公设当新方向。

## 13. 原质量闭包、反攻与当前结论

(2)是完整原source上逐每窗／每d区间的结论，19.4使用原T/CW并付绝对clock，未把局部set作新global配置。重构L使用R68留下的同S，其平均incidence按原whole T重计；若使用core，逐active tube访问下界仍是有限peeling所得，不声所有原tube保旧逐管density。two-fan／two-angle只在一个真实fine图内迭代有界核的平方矩，没有把单独rich图求交。

本次输出是在一个真实q内保K^-C原time的d-separated双锚点和共同四输出，不自动成为全原Z上每个window的wholeAFF准备。若未来有uniform矛盾或正结构定理，仍须在global bad-window见证并上回传；当前无该后段，不能把一个q的保留量误记成δ^a_*#Z_original。

已排的错误推理包括：从每个固定s各有dense slice便断有共同time、为条件角law免费赋slab、一个ψ恢复whole row2、把y_i(t)当固定系数、忽略e中的clockρ、以及把rational主项叫affine。把任意A(t),B(t)代入(8)再定义y_i(t)，可见该线性恒等式本身不会迫AFF；这只是代数反攻，不声这样的labels形成正κ／CW的完整原配置。

阶段II实质完成了原d-noncluster、同g两次fan／angle提取及完整精度／cover账，wholeAFF／完整mixed／ordinary目标仍未解。此不是R45固定臂泛位置或R58全Q二维Frostman的换名，也不是一个已经闭合的全source正gain。后段若只余上述未付coupling，不以覆盖upper当不可行lower，停止本轮在β／ζ／det常数的调参。待root完整稿后作实际全文独审；只改本assigned稿，未经外部同行评审，无新ID／major认证。
