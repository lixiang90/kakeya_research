# R0092：共同网格算术转移的精度、阴影与原质量资格门

2026-10-18，B。恰八个编号二级节，作已锁资格定理及停止门审查。结论为：明列的one-orbit/isotropic-grid转移可合法完成，付真实平均Lebesgue及弱Hausdorff返回，但指数不足；拒据此锁新gain。不声称有限域结果证明Euclidean Hausdorff猜想，也不排所有算术方法。未经外部同行评审。

## 1. 恢复、实际源阅读与待核量词

实际读GOAL、STATE、全部ROADMAP（分段读完）、R91 next六节和R92 reselection_spec五节；读取registry全部78项ID/status及相应FSD-001、DIR-003条目，另全文读这两个结果和R56主稿十节。R91任意K同维hull/current资格沿上轮真实审查记录，不重做或解冻normal3/C1出口。

实际全文读项目已存作者版`dvir_2009_finite_field_kakeya_author.txt`：Definition1.3、Theorems1.1/1.4/1.5和完整§§2–3证明。Theorem1.5为有限域F_p中每个方向含一条**全部p点**的affine line则`#S≥c_n p^n`；§3用degree<p的一元多项式的全部p个exact zeros。另实际打开[Ellenberg–Oberlin–Tao0903.1879v2 HTML](https://arxiv.org/html/0903.1879v2)，读Th1.3(1.1)、其counting ℓ^p定义及line-sum约定：页头v2为2009-05-12，正文重编日期不是新版本。仅采用此具名weighted maximal输入，不新认证其整个高级证明。本文没有下载、核原PDF字节或新认证有限环高级定理，来源版本与元数据由parent管理。

候选原对象先取有界K⊂R^n，每个实方向含一条unit segment，或对应真实单位round管及marks。测试同一各向同性格、每个有限域方向一个整数步长b、同一轨道`A+j b, 0≤j<p`能否返回超过现有ordinary界的输入。bounded/full-direction版本与任意集Hausdorff版本并非无条件互换；下文所得结论已经弱到不具锁题价值。

## 2. 四完整路径、删选与旧等价排重

ordinary初始化仍需同一原集合的多尺度质量和Hausdorff返回；directHRZ仍需全部parent/terminal/coarse费用；sticky完整κ1、余mixed及ordinary桥仍open；真反例必须同一集合供应全部方向真实unit段及严格维数upper。DIM/FSD/KT已付内容不重排，R91标准rank、R90 polar、R89cut及旧CP/PM/PW/action冻结。

未归一化whole-label restriction只减原权和并集，不保证保全部有限域方向。逐管density删clock保其原方向，却不保whole finite line。平均density先heavy只能保原incidence和至少相应权质量，不能无费给全mod方向、原cap下界或新AD lower。任何最终候选若只是对所有合法原选择统一成立的旧FSD/DIR正幂结论，应先按既有放大与restriction闭包排重；这里的有限域源本身既不等价也不蕴含旧四维有限源，不能以“有限域Kakeya已证”代替Euclidean输入。

R56已有actual small-footprint exact interpolation，不是只欠本轮小阴影假设；其主障碍是实数近轴误差与leading-form外推/conditioning。当前格点模转移用的是另一项真实精度费用，不重开R56的degree、Taylor或Remez参数。

## 3. 共同格的合法精确算术线：短整数代表

固定prime p。对每条射影方向`d∈P^(n−1)(F_p)`，取非零v∈d。将p个不同点`λv mod p`写在`[0,p)^n`；取`q=floor((p/2)^(1/n))`，对大p有`q^n<p`且q≈p^(1/n)。分成q^n个盒，两点同盒，其整数差b满足

    b mod p∈d\{0},   |b|≤C_n p^(1−1/n)=:M。

这是非零有限域差，故不是零方向。取共同物理格宽`h=c_n/(pM)`，使`p h|b|≤1/4`。K中方向`b/|b|`的一条unit segment可容纳p点`a+j h b`。对任意共同格shift ξ，选`A∈Z^n`使`|h(A+ξ)−a|≤C_n h`。则全部格点

    h(A+ξ+j b),  0≤j<p

都在`N_(C_n h)K`。因此`S={z mod p: h(z+ξ)∈N_(C_n h)K}`确含每个d的一条完整finite-field line。对有界K，这些格点数至多`C_n N_h(K)`，所以Dvir给

    N_h(K)≥c_n p^n≈h^(−n²/(2n−1))。

anchor的自由相位在此没有造成损失：各段独立选A，格本身和ξ始终共同。代价是**到原K的Ch邻域/cover**，不是格点精确落K，也不是保原|K|。无须把各anchor的亚格相位强行变成同一个真实clock。

## 4. 精度损耗的范围、方向舍入和模lift重数

若直接取|b|≈p，p步容纳于unit段要求h≈p^−2，得到的只是n/2覆盖指数。短代表改善为上一节的`n²/(2n−1)`；五维为25/9，仍低于经典7/2，更不能超过目标4。不能把p²称为所有算术策略的普遍下界。

在本节限定的“一个共同h、每方向一个b、全部连续j=0,…,p−1的真实lift”类中，所有`|b|≤M_0`整数向量至多`C_n M_0^n`个，覆盖约p^(n−1)个有限域方向迫`M_0≥c_n p^(1−1/n)`。又必须`p h max|b|≤C`，故以上最坏精度指数在这个类内有真实计数责任。未排多块、各向异性、非连续clock、有限环或多尺度新机制。

方向rounding不能忽略p步累计：在格单位误差为ε的步长，j步可积累pε。特别h=1/p时，沿实unit方向以clock j/p采样，首坐标可为`floor(A+j/3−ξ)`（取unit方向首坐标1/3）；p足大时相邻增量同时出现0和1，任何共同shift均不能使这一**指定rounded轨道**成为mod p固定步长线。此只反自动rounding断言，不否其并集中另有算术线。

有界物理盒中同一mod residue可以有约`(hp)^−n`个不同lift。Dvir只数image，给`#image≤#原格点`，不能反过来把image lower再乘这个最大重数。同样不因不同方向的real slopes接近而授予原angular权的独立下界。

## 5. 逐管shading：可保部分clock，不可补whole line

先在单条真实轴的unit clock I上取可测B、|B|≥λ。令`Δ=h|b|`、`L=pΔ≤1/4`。用位于I内的长度L区间覆盖I，总长度至多2；某个区间J=[a,a+L]有`|B∩J|≥λL/2`。对相位`ε∈[0,Δ)`，

    ∫ Σ_(j=0)^(p−1) 1_B(a+ε+jΔ) dε = |B∩J|。

故可选相位，使至少λp/2个**原marked clocks**落同一p点算术轨道。anchor随此改变，上一节共同空间格仍有效。但一般只有这些j，绝不能补齐其余finite-field points。甚至密度1的clock mask也能删掉某个预指定的有限采样集；这只否固定采样保全，不否自适应phase或其它line。

对半径δ_0的真实round tube，逐管`|Y_i|≥λ|T_i|`时，先处理O(δ_0^n)端帽；在λ≫δ_0的near-full范围只损常数incidence。用正横截面体积的clock集合，其长度≳λ，每个clock的轴点距真实Y_i≤δ_0。若目标格h≥δ_0，上述采样只给`N_(C h)(∪Y_i)`的cover，保真实marks附近而非实际体积。λ≤Cδ_0时不得沿用这一步而假装没有帽费用。

若每个有限域方向确有γp个保留点且γp≫1，Dvir§3的同一有限代数论证还能直接给`#S≥c_n(γp)^n`：取degree小于γp，沿各选线的zeros迫限制恒零，top form在全部方向为零，degree<p再迫其恒零。这里只把原输入改为**实际部分线**并付γ^n；没有声称原Theorem1.5可无改动用于缺点线。

## 6. 平均density：固定采样失败与加权算术线的真实修复

若平均`Σω_i|Y_i|≥λΣω_i|T_i|`，heavy删选可保至少一半原incidence及权质量≳λW，并给余label逐管密度≳λ。它并不确保上一节预选的每个d有一个heavy label。

具体固定采样反攻：在h满方向网中保有每个short代表方向的label，另补成满网。不同有限域方向的整数代表不实平行，其integer wedge非零，角距至少c/M²≫h；故这种网可取。预选label数≈p^(n−1)，原满网N≈h^(1−n)，所占比例≈`(ph)^(n−1)≈M^(1−n)→0`。只将这些label的Y置空，其余Y=T，原平均density仍趋1，却这一个预选mod方向方案没有marks。可用原点bush实现全部真实单位段；其体积宏观，此例不是small-footprint或Kakeya反例，也不排自适应重新选择。

上述反攻严格只针对**固定方向选择**。parent提出的自适应旋转可在原full h-separated h-net、无权平均density模型中真实修复。令每label的density为d_i∈[0,1]，平均≥λ；各原方向Voronoi cell的球面质量≥c h^(n−1)。对有限域短代表方向集施Haar随机旋转R，每个代表的边际uniform，故存在R使至少cλ比例代表读到`d_i≥cλ`。短代表间角距≥c/M²≫h，所读原labels不同。无需赠独立clock或free angular AD。

在这个R坐标系中用共同h格，称格Q heavy当`|E∩Q|≥c_0λ h^n`。每条原unit round h管只交`C_n/h`格，所以其nonheavy部分Y质量至多`C_n c_0λ h^(n−1)`；c_0先小，所有上述好label仍保`cλ h^(n−1)`的真实heavy marks。将该管换成θ平行的固定加宽cylinder，长度O(1)，包住其全部roundcaps，横截面积O(h^(n−1))。Fubini给好clock集合长度≥cλ，不需另外删帽。

设`τ=h|b|`。在一个step相位区间积分所有落入bounded clock范围的j，存在相位给至少`cλ/τ`个实际好clock；同一j mod p的重复至多`1+C/(pτ)`。因`pτ≤c`，故至少cλp个不同residues。相应grid nodes只在heavy格的固定邻格中，故总node数不超过`C#heavy≤C|E|/(λh^n)`。有限域good方向fraction和line richness均≥cλ；取degree`<cλp`，一元限制及Schwartz–Zippel给`#nodes≥c(λp)^n`。因此已独立核成

    |E|≥c_n λ^(n+1) p^n h^n。

λp小于固定常数时，原平均保证某条Y密度≥λ，单管`|E|≥cλh^(n−1)`已覆盖该更弱右端。此为原平均I的实际Lebesgue返回，不再只是邻域cover；两次筛选没有把λ损失藏进常数。

parent随后提出EOT weighted maximal替代，可去掉heavy阈值的额外λ；此更强版本也已独核。设`w_A=|E∩Q_A|/h^n≤1`，w为其piecewise constant函数。不能直接声`∫_T w≥|Y_T|`，但包含所有与T相交整格的固定加宽θ-cylinder确有此lower，长度O(1)、横截面积O(h^(n−1))，包括roundcaps。Fubini在其中选一条θ-parallel fiber，使其line integral≥c d_i。phase采全部bounded clock j，round anchor后，用固定邻格和w_A^+支配actual sample所在格的w；因此该轨道的加权和≥`c d_i/τ`。

令`F(z)=max_(A mod p=z) w_A^+`。同一j residue出现次数至多`1+C/(pτ)`，故对应finite-field line的**平均F值**≥c d_i，未把shading补成全1线。又`0≤F≤C`及

    Σ_z F(z)^n≤C Σ_A w_A^+≤C h^(−n)|E|。

这里max≤sum已付，不能再乘lift数。Haar旋转只需保平均d_i，不需heavy goodlabels；Jensen给全部模方向的maximal line-average n次方之和≥`cλ^n p^(n−1)`。实际EOT Th1.3的counting line-sum范数，除以p后恰给此和≤`C p^−1ΣF^n`。因此最终真实平均式加强为

    |E|≥c_n λ^n p^n h^n。                         (1)

该weighted推导对所有λ>0直接成立，不要求λp大，逐管版是其特例；上面的heavy版本是另一个已付但较弱的验证链。原full方向h-net和无权平均分母仍不可省：Voronoi下界不把任意ω质量自动变成球面质量。没有据此取得旧FSD任意非饱和N/任意权跨度/给定α的统一强输入，也没有将partial finite lines改称whole lines。

## 7. Hausdorff、多尺度和有限环不免费闭合

仅§3–4的整段cover lower本身，是有界full-direction K在一列h尺度的覆盖结论。prime尺度稠密性即使将它补成所有小h，也至多给相应lower-box结论；一般Hausdorff不能由此推出。非均匀Hausdorff cover的各尺度片未必各含每条线的足够clock，按方向/clock切片再mod化必须重计原质量，不能对每片免费调用whole-line定理。任意非可测/无界K亦不得从R91同维hull选择直接赠一个有界全方向原子族；若采用全clock概率及平均式而绕开此要求，应把该独立返回写全。

对一般可测E，`N_h(E)` lower本身不推出`|E|` lower；第6节的heavy密度或weighted cell函数才分别付出实际Lebesgue返回，不能省掉这些输入。共同格和独立clock phase不授whole finite line，也没有独自证明Hausdorff；若再进行标准cover分层，必须保原direction平均、所选scale及真实λ账本。即使付成相应弱Hausdorff界，指数也不会优于本门25/9的上限，不具五维新界价值。

root主稿§9随后已把这一步完整付成，已实际全文独核：若`dim_H K<t<s_n`，取同维Gδ carrier及Borel a.e.方向选择；对`H^t(G)=0`的球cover按半径`2^(−k−1)..2^−k`分层为U_k/M_k。全unit clock给`Σ_k m_k≥1`，其中m_k为方向平均的U_k时长，故某大k有`m_k≥c/(k+1)^2`。Bertrand取prime使h≈2^−k；Haar旋转有限h-net可同时避选择异常null方向并保实际平均时长≥m_k/2。真实Y=T∩(U_k)_(+h)含每个marked axis-clock的完整h横盘，因而λ≥m_k/2。式(1)与`|∪Y|≤C M_kh^n`给

    M_k 2^(−kt)≥c(k+1)^(−2n) 2^(k(s_n−t))。

对起始k足大，和原cover总费用上界矛盾。没有选有界全方向子族，常数不依有限family位置；也没有由boxcount直接冒Hausdorff。由此接受弱结论`dim_H K≥s_n`的实际返回，但它不改进既有界。

有限环也不能只把p换成模数：例如在Z/4中非零多项式`2X(X−1)`于全部四点为零，degree小于4，故Dvir的field restriction恒等性论证不能原样搬；primitive方向、单位与valuation层、period及lift次数须按实际ring定理核。本文没有否已知有限环Kakeya定理，只拒把未读/未匹配的ring量词作Euclidean新输入。

## 8. 本门判定、实际信息与停止

当前合法正向部分为共同格anchor处理、真实short整数代表及one-orbit精度费用、逐管clock-phase部分线闭包、full h-net模型中Haar+weighted maximal的平均Lebesgue式(1)，以及上节已逐步核完的弱Hausdorff读出。输出始终是弱指数25/9；不可冒有限域full维数无损返回实数full维数。任意权/稀疏N的强输出未获，换源名字不授本项目ordinary增益。

已实际全文读A稿`R0092_arithmetic_transfer_and_full_goal_gate.md`八节（包括新§6 weighted式）、working_spec五节及root主稿`R0092_finite_field_weighted_transfer_and_precision_ceiling.md`十节。A的短代表/角分离、fullclock、weighted平均链、heavy备份与primitive-ring校准均独核无mandatory；root§§3–6与§9的原质量和任意K返回已逐式核。A所读Dhar声明只按其实际域与阅读层级引用，不冒本人独读其高级证明。working_spec已锁资格完成而拒phaseII新gain，与本稿一致。终macro/source/next尚待落盘后按实际版本审，不预认证未来内容。

据R92预设停止条件，建议**拒锁此直接mod转移的phaseII新gain**，不继续p、环数、shading阈值或代表长度的小调，不注册数学ID/major。仅限所列桥，无完整Euclidean/source反例，也不宣所有算术策略无效。四完整路线仍open，Goal active；phaseI筛查不能代替最终数学目标。不预认证metadata、Git、文献计数或同步。
