# R0057正式独审：带费joint包络、sharp校准与范围

2026-10-17，B。修后root主稿与A主稿在本审明确范围通过；未经外部同行评审。结论是指定scalar-K／完整slab汇总证书不能给H5，不是H5或Th2.2的反例，不认证未来metadata／registry／Git。

## 1. 实际全文与原输入范围

已实际全文读root `notes/40_multiscale/R0057_charged_joint_capacity_envelope_and_stop.md` 10节、A `notes/40_multiscale/R0057_conditional_capacity_source_and_closure.md` 10节、最终macro6／next6／working_spec6；自身B8仅作一致性回读，不计独审。重核本地elliptic Def2.1／Th2.2／§2.2量词，而非重证103页wholeproof。当前是一次新all-s输入的实际charged组合，超出R56仅free-cap交换校准；ordinary H5原目标及所有既有冻结未被改名解除。

## 2. source调用与可付闭包

原Th2.2是fixed s、κ、finite D，base决定二维U,V，逐base逐dyadic depth的time support和maxweight双条件；初始ellipse floor δ^D，末端floor δ^(D−1)，源给q*≥1+2s−10κ，不给其上限。末端必须用X_v、v=T1左端点。A完整保留这些条件、subpower dominated结论及D／time-error／base阈值顺序；没有让可数多个packet同时保留自动成立。

root§2的两次无条件顺序调用可付：有界4D slope density使两block边际有界，Pr(Uj∈E,Vj∈E)≤C|E|≤CWκ(E)。对ν≤μ质量r，删原base保留率g<r/2损≤r/2；其余conditional time密度≤2/r倍，归一后capacity upper≤2C/r。r=M⁻ᵒ⁽¹⁾时均subpower，原第一块upper又由domination保留。它只给两个边际，不能相乘；逐包／s<1 profile仍未免费继承。反攻即使乐观授予所有逐包调用成功，下面费用仍存在。

## 3. 共同clock、实际K与原质量分母

已独算root(1)–(2)：共同physical短clock改τ=t/ℓ+1/2后，U1′=ℓa、V1′=b−ℓa/2、U2′=ℓb、V2′=a−ℓb/2，故U1′=ℓV2′+ℓU2′/2、V1′=(1/ℓ−ℓ/4)U2′−ℓV2′/2。都是固定scalar mix，未混空间方向或偷换physical unitlength。因此同形第二块双ellipse确把第一块放入固定倍同形tests，K_j≥c/Wκ(E_j)。fixed D≥2容纳固定缩小后的cδ轴，最大轴用有限cover，无aspect／δ幂损失；没有假Γ_j为product。

任意time-dependent ν≤μ给每j的time marginal density≤p0_j，故p_j≤p0_j a_j^time；离散a_j^time明确是δ乘active bin个数。Fubini处理可测版本，零prior项不带保留质量，countable sums用Tonelli。原Cauchy给Σp_j a_j^time≥Σp_j²/p0_j≥m²；不能把p0_j改成最终p_j或漏掉重复packet次数。

## 4. 全分区下界、sharpness及finite区别

root(7)按δΣ_v∫dx2积分完整slabs，截面面积≈L_jw_j，而area/Wκ=(w_j/L_j)^κ≥cδ^κ。全部slabs在同一个固定bounded盒内，所以sup及固定Lp下界均≥cδ^κm²，包含全部orientation／axes／partition／ν。它用的是虚拟完整slab的面积，未冒原shading体积。

已另核root§6 continuous strip sharpness：p0≈δ²，固定scalar clock mix保long-pair边际有界、joint4D密度≤Cδ⁻²，且不混long／normal坐标。任意rot F给概率≤CL² min{1,(w/δ)²}；除Wκ分w≥δ和w<δ均≤Cδ^(−1+κ)，故真实continuous K≈δ^(−1+κ)对all fixed D成立。固定time每l仅O(1)个k命中slab，sup C≤Cδ^κ，与下界匹配。finite atomic网未jitter时细于δ有atom费，稿中只沿floorδ或另付Oδ jitter，不误称all-fine同K。

finite方向网经bounded slope→unitdirection映射双Lipschitz可取N≈δ⁻⁴、physical δ分离；原unitaxis内部有共同固定比例clock和逐管≈δ⁻¹ marks。Oδ几何误差只在w_j≥δ的secondblock slabs／unit输出邻格中吸收，thin terminal δw转换未免费获得。任意旧shadings不保证该crop保质量；本校准原Y=T且保留ν任意，稿中未作该偷换。

## 5. θ／p方向、指数与真正被否的对象

root(9)的实际upper RHS必须保调用前原权θ_j≥p_j。δ^qΣp_jK_j1Sj只是该RHS的数值lower，不是已证明的真实atom upper，更不是实际atom lower。只采用具名保证的q_j<1+2s_j−10κ≤3−10κ，各项数值包络≥δ^(3−10κ)p_jK_j1Sj，故sup至少cδ^(3−9κ)m²；ν/m归一则除m。m≥δ^η且η小，不能把这种uniform证书降到δ^(4+σ−ε)。额外慷慨数值rate3仍给δ^(3+κ)m²，不依赖误把10κ当最优q上限。

真实swap输出在原小clock内的Jacobian=(1−t²)²远离0，continuous joint(T,X1,X2)密度O(1)、δ-cells质量O(δ⁵)。因此大的是所用upper expression，不是实际joint集中；其并集常量级，不满足小并集反设。两包络的min、真实joint support、不同split、perpacket anisotropic坐标回传等仍可能用额外信息；主稿明确未排除，不能将两个各自sup大推成min的sup大。

## 6. 宏观、停止和下一入口

最终macro正确区分本轮新增全partition／保留质量预算与旧free-cap例，停止同base scalar-K／完整slab uniform策略，不续κ／s／strip／包数。A对平均m与逐管dense、wholelabel restriction与进一步time shading删选分开核；没有用CP／PM全称闭包改名新增方向。本文不认证更强joint规律，更没有新增ordinary维数界、Euclidean反例、重大或新颖声明。

next6回完整ordinary高维目标重选并同轮实际数学，当前未选R58命题，未借本例可逆Jacobian给general gain。它要求新机制从原straight-line incidences付联合信息、先restriction／双向排重，禁止添加“支持上费用小”“conditional cap好”等未证公设冒完成；既有KT算术和四维assembly不冒新进展。该停止和交接范围通过；Goal active。正式文件终稿后停止编辑，统一归档／验证／同步由root执行。
