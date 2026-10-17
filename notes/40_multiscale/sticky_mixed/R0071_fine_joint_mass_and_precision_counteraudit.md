# R0071：条件κ packets的细联合质量与精度反攻

2026-10-18，B。实际读R71 spec5／macro3、STATE、78项状态、R70 next6，完整R67 root14及R69 B§5旧候选。只编辑本assigned稿，无Git／spawn／元数据。以下保完整mixed43，目标到实际W/native共同图及用途，不把单arm cover当完成。没有构造fullsource反例，也不宣任何更精确联合方法均不可能。

## 1. 原量词、尺度与需要比较的证书

完整Def17.2–17.4 d5/k4/ell3、whole T joint4-AD／CW、两grain／ξ／Φκ／slab及native scalar AD维数`α=1−κ`均保留；当前剩余`0<γ≤1−κ`。指定原allowedρ，原同S有R68的`T≤ρ^(3−ζ)`、R69 d-cap及R70 raw zeroD估计。不同ρ的S不交。原三类incidence core／good-q供应按R67具名接口，记

    m=#Z_q， E0=#E_q， D0=δ^(−κ)， L=ρ/δ， N=L³，
    E0≈_K m L^(4−κ)， #I≈_K E0D0， m≥K^(−1)ρ/δ。

原point、tube、nativegrain min-degree用同core，不重新授AD lower。τ为原选角前native上界所选尺度；R70可在重构后的同time law给`τ≳_Kρ^(3+B)`，且`τ≲_Kρ^(3−ζ)`，但不能因此声δ≤τρ。

为给本机制最有利的预算，§2–6先研究`δ≤τρ`、native最终error `ε_L≈_Kτρ`。末W角close尺度记a、细W observable记σ。若要同一native归一mesh O_K(ρ)，两端matching误差要求`ρσ≲_Kτρ`，即σ≲_Kτ；W末角误差要求ρa≲_Kσ，故最有利边界为

    a≈_Kτ/ρ， σ≈_Kτ， λ=a/ρ≈_Kτ/ρ²≪1。                  (1)

λ是固定ρ幂，不是源η产生的可任意小损失。δ-floor与最终working observable另在§7核，不能把有利区结论冒全部范围。

## 2. 真point条件packet上界与index的选择

固定原p@t和middle s。每个初arm的实际p_s满足

    p_s=p+(s−t)(φ,ξ_p+f(t)φ)+O(δ)， φ∈原Φ_p。

φ↦p_s的Lip常数≤Cρ；完整Φ_p的κ-AD在角尺度a/(Cρ)上给physical a-cover至多`K(ρ/a)^κ`。a为原allowed尺度，边界邻格只固定费；不把跨不同p的集合称同一κ集。

在每个occupied physical a-packet，用原point-specific a-coherence，实际续接管的a-direction proxy至多Ka^(−κ)。因此对固定(p,s)，所有W续接末角的**union**大小至多`Kρ^κa^(−2κ)`；连terminal time u一起，

    R_X(a)≤K mρ^κa^(−2κ)。                                (2)

这里X-index只记实际末time和全局末角bin，不把physical packet也作为必须相同的index。若强迫两arm的p_s落同a-packet，远clock下会有

    |ψ|≤C[a/(qρ)+δ/(qρ)]， |t−s|≥qρ。

原同point Φ_p的ball upper即使在core下也只能保证该近对角角pair的质量≤`K(a/(qρ))^κ`；这不能免费保原宽角或slab质量。加入packet标签作为共同index会改变所抽对象，不能偷作更强横截结论。使用(2)的union则没有这个错误。

## 3. 同trunk Tensor Gram的实际fine计数

保持R67同初arm的X_α与native Y_α张量，只把W末角close由ρ改成a。每α的续接ℓ¹总量仍为`≳_K D0m`和`≳_K ND0m`；native index上界仍

    R_Y≤K m(ρ/τ)³τ^(−κ)。

由(2)及同一个Gram CS，实际fine hybrid数量给

    H_a≥K^(−C)E0 D0^6 m³
                a^(2κ)ρ^(−κ) τ^κ L³(τ/δ)³。              (3)

相对于R67天然W-close ρ计数，该下界乘`λ^(2κ)`。这是使用原条件κ信息后比环境4维packing更强的下界，但它本身仍含固定损失；所有objects是真原points／tubes／jump，u、v可不同。两初arm、原ψ与共同p、t、s仍共享，没有把两个独立dense图求交。

对一个固定原初incidence(p,T1)逐项恢复，第二W末管处只能改善为`K(a/δ)^κ`，其余自由项沿R67，给

    H_a(p,T1)≤K D0^5 m³ a^κτ^κ N(τ/δ)³。                  (4)

与(3)相除，当前证明仅给初incidence边际相对原Uniform(I)的domination常数`Kλ^(−κ)`，不是K。固定t,s同样逐项计数，利用原每slice point upper，得其time边际至多

    Kλ^(−κ) Uniform(Z_q)²。                               (5)

因此原fine角／slab与R70 zeroD上界不能自动按旧K传递。式(4)(5)是现有certificate的upper，不是实际law必须饱和的lower；若要更好domination须新原质量估计。

## 4. 同一fine frame的完整恢复，先给予最有利patch

先**额外给予**一个最有利、尚待证明的公共native长度τ patch，以检验仅packet改进能否闭合。取σ=ρa≤τ，精细两端matching需把TW1／TL1末φ的恢复proxy也取a。固定u,v、原W normal Q的σ-bin、W联合observable A的σ-bin及native ε_L-bin，按R67两端公式恢复：

    #fine w1≤K(σ/δ)³(ε_L/δ)^α。

其后两个末a-proxy数a^(−2κ)，TW1／T1／T2／TW2／TL1五项fine角数合为`(a/δ)^(5κ)`；native第一jump的fine水平cell数N，第二jump和TL2仍为`(τ/δ)^(3+κ)`。故在真正细initial a-proxy也进入code的方案中，统一fibre upper为

    M_a≤K^C(σ/δ)³(ε_L/δ)^α
              a^(−2κ)(a/δ)^(5κ)L³(τ/δ)^(3+κ)。            (6)

这个恢复使用固定observable physical σ-cube内的原ξ-coherence和σ-cube枚举，不假Euclidean全局Lip或整grain ξ恒定。原W Q桶数≤`K m²(ρ/σ)^(2−κ)`，observable A upper≤`K(ρ/σ)²`，B upper≤`K(τ/ε_L)^α`，原t,s reference共m²。

令N_a为最终公共初角a-carrier的card。将(3)、桶数、(6)和上述frame逐项相除，得到此certificate保证的mean量级

    K^(−C)(σ/τ)^α (ρa)^(−κ)/N_a²。                        (7)

δ、m、ε_L的幂完全相消；σ=ρ²、a=ρ、N_a≈ρ^(−κ)时退回R67的`(σ/τ)^α`，是独立校验。

原incidence-mixture的fine a-ball upper≤Ka^κ。若希望目标fine角reference保K-domination原law、且保K^(−C)质量，其公共carrier至少需`N_a≥K^(−C)a^(−κ)`。即使给予最乐观`N_a≈_K a^(−κ)`及公共τ-patch，在σ=τ、a=τ/ρ时，(7)仍只保证

    K^(−C)(τ/ρ²)^κ=K^(−C)λ^κ，                            (8)

不是K^(−C)。若只用原coarse Φ_q的ρ-cover及二维环境，则`N_a≤Kρ^(−κ)(ρ/a)²`，直接代入同一证书的保证更弱，为λ^(4−κ)。不能把(8)叫actual density upper或全source不可能：实际H可比(3)大、实际fibre可比(6)小。正确结论是仅这些已付upper／lower不能给所需subpower密图。

actual fine hybrid若利用(4)把角边际集中到更少a-cells，N_a未必仍≥a^(−κ)；但此时已失K原law domination，只得λ^(−κ)收费，不能一面缩carrier救density、一面仍免费保原angle slab。这是两个不同责任。

## 5. 公共native patch、U分桶与bundle不能冒乘积reference

R67的相容式仅给，固定u,v及W Q后，native L label落已知bulk平移附近的长度

    R_B≈_Kρ²

区间。σ=τ≪ρ²时，完整scalar Y上τ-patch的数目可达证书upper`K(R_B/τ)^α`。对这些patch平均固定一个，只减少H和B-card相同因子，不能因此消除density费用。保粗初ρ reference的形式账本为

    K^(−C)λ^κ(σ/R_B)^α；

在σ=τ、R_B=ρ²时是`K^(−C)λ^(κ+α)=K^(−C)λ`。该粗初角账本不能直接声W support误差Oσ，下一节另区分其最终working精度。

可以尝试按第一jump的native水平a-cell分桶，使C_L的bulk在τ误差内固定；但cell数`(ρ/a)³`与相应jump fibre由N减至`(a/δ)³`恰相消，不白送新gain。另C_W、jump点所在physical cube及其ξ代表仍可依W-input A改变；在旧全q只知Oρ²的不确定。原coherence按实际point cube使用，不能把这些不同cube的ξ换成同常量。

若由此仅得到每A自己的native interval B(A)，它是bundle reference，不是Uniform(A)×Uniform(B)的公共乘积。要转成一个共同scalar carrier，须证明原tuple的可保分桶／translated patch质量和output/input ratio，或支付其union cover；不能把B(A)中心平移后默认旧scalar输出核不变。这样的gauge还会在W action改变A时加入中心差，是实际新核，未有可用inverse。

即使这些公共patch问题全部被理想地解决，§4仍剩λ^κ的保证损失。因此当前未给一项足以越过旧R67账本的新mass／precision估计，不能只用bundle口号声已补两端matching。

## 6. 细code与最终working observable必须分开

若声称W关系以physical误差Oσ成立，初ρ-proxy误差Oρ²大于σ，必须把初角也细到O(σ/ρ)，或者保exact fine角及其真正reference／fibre。上述(6)(7)处理前一种最有利a≈σ/ρ的方案；不能用粗ρ角名义省掉细reference费用。

但目标若只是最终归一meshρ，W physical observable可以在ρ²上重聚合，初ρ-proxy误差合法。这不意味着所有common-ρ方案都必须fine初角。此时细σ-cells原先只用于恢复，随后到ρ²-cells的actual aggregation容量与两端joint碰撞必须计入；visible二维容量至少只能由证书给`K(ρ²/σ)²`上界，不能既保细frame的fibre改善又按粗frame免费合并。

重聚合也不会令fine native匹配误差自动变小。原两端误差ρσ要不超过ε_L≈τρ，仍需σ≲_Kτ；若把σ恢复为ρ²，native blur重新成为ρ³/τ，回到R67天然mesh不能读contact的界限。反过来若继续保σ≤τ，§4–5的已付计数保证仍有固定λ损失。这里是两种具体certificate的完整账本，不是任何可能联合observable的下界定理。

## 7. δ-floor和R70 smallD不能随便转移

一般范围必须用

    ε_L=max(Kτρ,Cδ)， w_native≥max(Kρ,Cδ/τ)。

R70的τ≳ρ^(3+B)和δ≤ρ⁴**不保证**δ≤τρ；在δ≈ρ⁴、τ≈ρ^(3+B)时δ/τ≈ρ^(1−B)>ρ。只有有利区δ≤τρ才有前述共同workingρ，floor主导区还需更粗native mesh，不能把这些ρ幂放进K。即使先给予有利区，(8)的固定损失已经存在。

此外(5)将R70原ν² zeroD cap传到fine hybrid，至多先给`Kλ^(−κ)δ^v`的bad-mass upper。当前细图保证mean只有λ^κ（甚至实际公共patch证书λ），v又先取远小于µκ等正阈值；这个upper未必小于整张fine图质量。不能只说原bad set是δ^v便删除，更不能授新角nonconcentration。若有人另给更强time domination或actual hybrid mass，须独立重算；当前没有这项证明。

## 8. 反攻、闭包和“固定损失”的正确含义

本轮没有构造保完整T／CW的负例。条件point Φκ→packets是真source上界；同trunk Gram也真，但CS保证的λ^(2κ)成本与fibre改善并未抵消。只把两次CS分别作rich再求交、把相同physical packet作为无代价共同index、给跨root的fine末角授globalκAD，都是不同的无证升级。

原CW／jointAD4、原tuple min-degrees和平均shading在这些counting中未重归一。逐active tube lower来自旧同core；细pair限制不是新Def17配置，不保每原管逐管density或所有原times。whole-time／conditional-angle／bundle分桶的原质量各自计算，不用一个K隐藏固定ρ幂。

目标positive-gain若已对全部合法选择统一成立，当然可排原positiveκ类；由该空类得到packet结论不能算独立机制。本轮没有证明packet候选与完整gain双向等价，也未以更大／更细class名称登记结果。若要声新正结论，仍须在相同原reference上实际给K^(−C)共同图及最终AFF或κ矛盾；当前这一步未付。

## 9. 条件packet乘积的严格local sharpness

以下只校准(2)的局部上界，不构造fullsource。取小固定缩放的middle-third Cantor集合F⊂[0,1/20]，其Ahlfors维数`κ=log_3 2`；令`γ=κ/2`，则`κ+γ=3κ/2<1`，确位于本轮剩余参数范围。写

    C_F={(v,v²):v∈F}，
    Φ_z=C_F ∪ [C_F+(0,x1(z))]。

每个Φ_z是至多两条固定biLip Cantor曲线的union，故uniform κ-AD。单位normal的linear／quadratic sublevel在v轴上至多两段，总长度O(√w)，Cantor interval upper给原slab exponent γ=κ/2。两component的union只固定常数。若z在同physical a-cube，x1(z)相差O(a)，所以可用cube中心的同一union作coarse κ-carrier，满足原式point-coherence到O(a)。这不是授所有点的fine global κ-cover。

取root p0的x1=0、原f=0／ξ=0的局部方向表，初管φ(u)=(u,u²)、clock差s−t=ρ，实际

    p_s(u)=p0+ρ(u,u²,0,0,1)， u∈F。

unshifted component确保该初管在p_s处仍是允许方向；不能只定义shifted component而漏掉初arm incidence。每p_s处shifted末角族的union为

    Γ_ρ={(v,v²+ρu):u,v∈F}。

因0∈F，它已包含unshifted C_F。映射`(v,w)↦(v,v²+w)`在此固定小盒双Lipschitz，所以对`δ≤a≤ρ`，

    N_a Γ_ρ≈N_a F · N_a(ρF)
           ≈ρ^κ a^(−2κ)。

这比免费a^(−κ)末角κ-cover多`(ρ/a)^κ`，正好饱和条件packet乘积。有限实现时middle u取F的δ/ρ-net，使p_s(u)物理δ-separated，terminal v取F的δ-net；root Φ仍可保完整δ-net，落在同δ/ρ-cell的初角在middle只差O(δ)，按原O(δ) incidence convention／固定邻格合并。所有a≥δ的cover与AD／slab／coherence上界只改固定常数；不声这些选择有原core的每tube长marks／全部point最低度。它保局部单arm直线几何和原式point方向相容，但没有filled2／3-grains、whole-time continuation graph、T joint4-AD／CW或全source平均质量，绝非完整source／Kakeya反例。

因此单靠point κ-AD／slab和coherence，不能把(2)的两个κ因子压成一个。是否完整wholeT／长访问能另给补偿仍是额外source责任；本例不否它。

## 10. 本轮数学终点和停止

已实际核到条件cover、同trunk lower、初incidence／time上界、两端fine fibre、公共frame、native patch／bundle、最终observable精度和δ-floor，而非只重复R67一句normal误差。最好公共patch且保原fine角law的证书仍有λ^κ，真实旧公共patch给λ；条件packet信息尚未产生新的可用joint mass／precision或whole-row用途。

这不否所有更精细source方法；它是当前已付数据下的保证不足，不是actual density upper或全source反例。按本轮spec，若root／A没有另给新的补偿估计，应判该packet机制未达到主目标、冻结局部迭代，R72先完整Goal宏观，不续a、σ、τ阈值或增添conditional AD公设。普通初始化、其余matrix／mixed／general-to-sticky及wholeAFF仍open；无ordinary新界、新ID／major／新颖或外部同行认证。正式全文review待授权，未来Git／meta／safe sync不预认证。
