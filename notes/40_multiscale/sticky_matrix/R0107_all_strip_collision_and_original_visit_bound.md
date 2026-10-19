# R0107：全部横条的collision计数与原访问条件上界

2026-10-19，root。先锁reselection5与working5。本稿证明明确附加输入下的有限计数lemma，并核原source的匹配责任；不证明fullsource moving-row cap，不登记新ID、新颖或major。使用标准初等energy/Cauchy–Schwarz，未经外部同行评审。

## 1. 为什么改变单strip计数

完整目标仍是ordinary n≥5/general Hausdorff Kakeya、真正同集全方向strict反例或重大中间结果。四出口已重新比较，DIM001已付具名链不重做，A10未获新seed；R106两锚nativeY tubeKT失败永久保留。本轮不换网救该构造。

R106§3在一个x2宽h的strip内只保h原质量，后续单片设想把横向projection要求推向接近一维。本轮同时计全部O(h^-1) strips：第二输出相隔h²，使它们在终端只能有限重叠。任意正横向斜率幂可通过一个全图energy，控制所有依clock变化的保留子集。下文须把图、原访问重数和终端Y放在同一root上；不能由这个机制名自动宣布fullsource具其输入。

## 2. 有限lemma的完整输入

固定0<τ<1、0<h<1/10及A,B,K,D≥1。Q为[-1,1]²中同一坐标h格的任意子集，写q=(a,b)，g:Q→[-B,B]在选clock前固定。σ是clock概率；每v有H_v∈[h,2h]、|k1(v)|,|k2(v)|,|c|≤B和中心y_v∈R²。对所有q0∈R、h≤r≤1要求

    σ{v:|k1(v)−q0|≤r}≤A r^τ.                    (1)

每个实际访问保留原标签(v,q,T)，每(v,q)重数至多D，其实际终端输出z属于Y_v并满足

    z=y_v+H_v(g(a,b)−k1(v)a−k2(v)b,2b−c)
          +e,   |e|≤Bh².                         (2)

只要求该公式所涉及的CB²h球中，Y_v的h²-grid cover至多K B^C h^-1，常数C为固定绝对数。原Y_v的全尺度AD1在δ≤h²≤CB²h≤1时供应此种upper；若球过大，可按有界域的完整cover作相同宽松估计。lemma直接明列cover输入，不引用未展示的源lower。

令J_v为该root在v的实际访问数。目标是

    ∫J_v dσ(v) ≤ C_τ D (AK)^1/2 B^C
                         h^(-2+τ/2).             (3)

无每strip非空、无每q共同clock、无v与图独立采样假设；Q_v={q:有访问}可以任意依v变化。σ和k1本身须满足(1)，不可从实际Q_v重归一后偷保同A。

## 3. 先固定全图的collision energy

写Q_b={a:(a,b)∈Q}，令

    E_v=∑_b ∑_(a,a'∈Q_b)
       1{|g(a,b)−g(a',b)−k1(v)(a−a')|≤C0 B h}.

C0取固定足大以包含(2)误差及同一h²输出格的直径；k2b在同strip精确消去。E_v计整个原Q，而非已选Q_v。因此一个E_v同时支配所有clock依赖子集和其全部更小删选。

当a≠a'，设d=|a−a'|≥h，事件把k1限制在以[g(a,b)−g(a',b)]/(a−a')为中心、半径C0Bh/d的区间。该半径≥h；若大于1用概率≤1，否则用(1)，统一得事件概率≤C_τ A B^τ(h/d)^τ。每个a在距离jh的格位置至多两个a'。因τ<1，

    ∑_(j=1)^(C/h) j^-τ≤C_τ h^(τ−1).

每strip至多C/h个a、至多C/h个b。加对角#Q≤Ch^-2，得到

    ∫E_v dσ(v)≤C_τ A B^τ h^(τ−3).              (4)

对角可吸收，因为h^-2≤h^(τ−3)。未采用Φ的Frostman、独立pencil或一般投影定理；这里的h格packing已经足够。τ=1会有log，故规格明确排该端点，不用它优化固定幂。

## 4. 全部strips共享终端容量

对每个v及每个q∈Q_v，仅选一个实际输出，仍保所有其他原访问用于§5乘D。记n_b为该strip已占原q数，m_b为所选输出占据的不同h²格数。同一输出格的两个原q属于上节collision事件，故Cauchy–Schwarz给

    n_b²≤m_b E_(v,b).

strip b的第二输出距(y_v)_2+H_v(2b−c)至多Bh²。相邻b中心相隔2H_v h≥2h²，故任一终端h²格仅可能来自O(B)个b。即使b间第一输出位置不同，第二坐标仍给这个重叠upper。因此

    ∑_b m_b≤C K B^C h^-1.

再对全部b作一次Cauchy–Schwarz，得到

    n_v²=(∑_b n_b)²≤C K B^C h^-1 E_v.           (5)

这里没有先选单strip，也没有丢h原质量。输出允许任意依q、v、T的误差；选一个实际输出后即可用其grid格进行CS，不把近似公式冒成唯一精确输出。

## 5. 原标签重数、平均与restriction

每(v,q)访问数≤D，故J_v≤D n_v。对(5)在同一σ上积分，使用概率CS及(4)，即得(3)。这给的是原访问绝对upper，不只occupied cells的cover。任意删marks或whole-T子族仍满足upper，因为沿用同一图、D、σ与原分母；它不授删后完整pointΦ/filledX或逐管lower。

若roots r的原访问标签互不重记，可逐root相加，允许D_r、A_r、K_r不同。要读相对密度，必须有原reference量I_ref与∑_r D_r h^-2的实际比较；只知每root占格很多不够。若另有I_ref≥c∑_r D_r h^-2、统一A,K,B，则(3)给平均比例≤C c^-1(AK)^1/2B^C h^(τ/2)。这项比较是条件读出，不自动属于fullsource。

clock限制到σ质量p的集合后，未归一的原upper仍成立；若改概率σ/p，(1)的A至多变A/p，且左侧也除p。不能免费用原A。若一个tube平均visits很少，(3)不创造每管duration；双time lower必须另由原tube degree给出。

## 6. Same-T公式与粗图的实际单位

在固定normal chart t=0,s=1、F0=I,F1=0，写

    F_u=[[f1(u),f2(u)],[0,1−u]],
    C(T)=(U,V)=(b,b−a+ψ−φ).

若所考察原T还真实满足U2−V2=c，则ξ2(p_u)=x2(u)−c。此关系同时用了code hyperplane和第二row，不能只由nᵀG_u=0推出。令H=v−u，ki=(fi(v)−fi(u))/H，则同一实际T有

    Y1(v)=Y1(u)+H[ξ1(p_u)−k1x1(u)−k2x2(u)]
                         −H²[k1φ1+k2φ2],
    Y2(v)=Y2(u)+H[2x2(u)−c]+H²φ2.              (6)

固定root(u,原Y(u))；若ξ1在每个x的h-cell内有O(Bh)统一振荡，先取实际代表g(a,b)。替换x为h-cell中心和ξ1为g，使(6)只增O(B^C h²)误差，实际轴/point误差δ须δ≤h²并连同source常数计B。|ki|受所用窗的真实dyadicLip控制，不能公设连续可微。此时(6)匹配(2)，对所有原访问共用同一图；不同v可有完全不同Q_v。

本段只在明列exact normal form/code条件和coarse coherence实际成立时匹配。一般small row误差、moving normal、arbitrary code slab、不同root的normalization尚未付；不能通过“normal form”三字删掉它们。

## 7. 横向斜率law与一般NF的差别

若额外已有固定root u的横向secant law (1)，lemma立即生效。精确对角子情形f2=0时，一个h-window中k1落半径h^ε0的ball，会使f1(v)落某affine函数的h^(1+ε0)邻域，第二row本身affine；可尝试使用R77 whole-matrix local nonfit得到该尺度cap，再转换为弱正幂law。此尝试还须付good windows、root条件概率、all尺度及allowed floor；本文没有把这些量词未经核实就宣为source推论。

一般第一row为(f1,f2)，wholeF nonfit可能完全由f2驱动。在所检bulk时窗上取f1恒定而f2粗糙，该窗的k1是atom，即使wholeF不fit，(1)仍完全可能失败；窗外可另接anchors，不能误称f1在F0=I/F1=0的全部Z上恒定。向kernel横向x1的projection看不到f2；不能以全矩阵NF直接给横向NF。它与旧R72 common-kernel不可见变量问题相连，但不是通过重调R72已付γ>1/2子范围即可覆盖一般smallγ。

因此本文未证明fullsource nᵀG cap，亦未证明exact diagonal子类在所有参数下已排除。真正可用的新内容是(3)–(5)的全部strips原计数机制；source横向law和完整code/row归约是未付输入，不得改写成定义赠品。

## 8. 条件分支的原source分母与同shell比较

下面使用κ1源的明确计数输入：m=#Z满足K^-Cδ^-1≤m≤Cδ^-1，N=#T满足K^-Cδ^-4≤N≤K^Cδ^-4，native roots(u,y)总数≤K^Cδ^-2。先对每fine p、每原Φ_p的δ方向bin固定一根实际witness T，去重复(p,T)，再每(T,u)保一个visit；截面δ-packing及同(point,方向)物理碰撞仅损固定K幂。每point的**所用图**degree≤K^Cδ^-1，其总访问I≥K^-Cδ^-5≥K^-C Nm由原E/Φ下界给出。没有对未筛全T_p赠degree upper，也没有把自由角bins当真管；witness是原定义实际存在的相容管，保留同T双time标签。

一个固定root的水平H-cell至多C(H/δ)²个原fine points，因而每(v,cell)实际原pair重数

    D≤K^C H²δ^-3.                                (7)

ξ的粗图需H在可用coherence范围：若非allowed格，取上邻ρ∈[H,K^C H]。每水平H-cell的physical affine grain片只交有限个ρ-point cubes（固定bounded F）；按这些有限cube tag分为有限个图，ξ代表先于v固定，误差O(K^C H)。所有piece及rounding费用进入B=K^C；不可跨coherence边界直接声一个代表。δ≤H²保证轴误差可吸收。

还需一个**额外、非原定义赠予的横向输入**：对所有原u、所用shell H、q0∈R及H≤r≤1，原clock counting满足

    #{v∈Z:H≤v−u≤2H, |k1(u,v)−q0|≤r}
           ≤A(H/δ) r^τ.                          (8)

不用已按tube偏置的clock概率。取σ=δ/(C H)乘shell上的counting measure，它是subprobability；§3–5只使用总质量≤1，故照样成立。每root再乘C H/δ恢复原计数，合计roots及(7)给同shell真实pair upper

    #Pairs_H≤K^C √A B^C δ^-6 H^(1+τ/2).          (9)

下面不能为任意预选shell赠pair lower。取δ^(1/8)的上邻source allowed h0，满足δ^(1/8)≤h0≤K^Cδ^(1/8)，把time轴分为O(h0^-1)个该格的区间。对每T按区间计n_Tj，CS给∑_j n_Tj²≥c h0 n_T²；再对T用原I得总pairs≥K^-C N h0 m²。对角≤Nm，可由δ≪K^-C h0吸收。每root距u小于q h0的terminal clocks≤C(q h0/δ+1)，所以全部short pairs≤K^C q N h0 m²+Nm。先取q=K^-C足小，保留正比例；取u<v仅损固定倍。始终保留同一个h0-window的标签，不把任意跨边界pair赠dyadicLip。

按dyadic gap选一个H∈[q h0/2,2h0]，壳数O(1+log K)可入K固定幂，得到

    #Pairs_H≥K^-C N H m²≥K^-C δ^-6 H.            (10)

在η足小时H≥δ^(1/4)、H≤K^Cδ^(1/8)，所以coherence与δ≤H²均有余量。同h0-window的实际Lip给|F_v−F_u|≤K^C h0，且h0/H≤K^C，故|ki|≤K^C；选H的allowed上邻仅用于固定u下的空间coherence，不替代这一时间Lip责任。σ还限制在该原window内，其(8)只减不增。若额外(8)对这些shell统一成立、A≤K^C、B≤K^C，则(9)(10)迫1≤K^C H^(τ/2)≤K^C δ^(τ/16)，η最后小即矛盾。只用原平均I和CS，未从平均赠每管duration，也未赠每root/strip density lower。

这支付的是**明列exact normal form/code条件与横向law(8)之下**的原source条件分支，非全rowcap。一般source是否给(8)、一般code slab/row是否可归到§6，仍未付。此真实原分母比较不是假设“flatness”后的读出；有限lemma§5的一般条件读出仍适用于其他系统。

## 9. 独立反攻、旧命题关系及有限范围

若去掉(1)，取g(a,b)=q0 a、k1≡q0、k2≡0、全Q格及全部Q_v。输出沿第二坐标直线，h²-cover≈h^-1、每root n_v≈h^-2，没有h^positive saving；这严格检验横向law必要性。此例仅满足本lemma其余有限输入，直线Y违反原tubeKT，故不是完整source反例。

若让每q有M个原T重复标签而保持同一输出，原访问数乘M；D真实不可删。若图随v改变成g_v=k1(v)a，energy强度同样消失；因此粗ξ给一个预先固定图是实质输入。恶意Q_v、稀疏strips和相邻strip重叠已经分别被全图energy、无lower的CS及O(B)重叠覆盖。未声称τ/2为sharp，也不做数值实验替代证明。

这是标准projection energy的一个显式计数用途，不以新名称登记新理论。旧CP/PM全称gain在完整source上当然可能蕴含本条件应用的某些相对结论；反向由此有限lemma推全source缺(1)、code/row及原质量lower，故不构成新的等价完整gain方向。R106单strip缺口部分被改正，而R72/R75/R77已付source结论均不被重命名为本轮新结果。

## 10. 结论与停止

已写出条件有限估计(3)，其核心是全部strips输出容量只用一次、一个全图energy控制任意clock-dependent删选、D保原访问。它消除了“每strip必须接近一维projection”的错误要求；任意固定τ>0即足以给此条件分支正平均幂。独立formal审查尚待实际全文后完成，本文不自封reviewed。

原same-shell预算已在§8按明确源upper/原平均I付出；完整source仍缺横向law(8)与一般code/row归约，不将其藏入K或source定义。无ordinary/fullrough/新维数下界、无新ID/major；高级具名输入与外peer层级不变。停止重复energy、单strip和更多fixedtime模板，下一必须面对一般非横向分量及全source责任或完整宏观重选。Goal active；根目录状态、验证和保历史同步由root另行完成。
