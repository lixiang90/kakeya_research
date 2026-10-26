# R0115 独立复审：full usual-source 单clock graft

2026-10-26，constructive_gate。审查对象为 notes/40_multiscale/sticky_matrix/R0115_fixed_row_full_source_countergate.md 全部九节。本代理未参与graft机制提出、dust嫁接施工或主稿撰写；本人另作的phase闭包稿不是本审查对象，不算被本人独审的正成果。未读其他graft reviewer的审查稿后复制结论。

已实际全文读取初落盘主稿，提出两处精确化；作者修改后又实际全文读回，并在作者补入a<1端点后再次全文读回终版。此复审锁定主稿raw bytes SHA256：

    3031421946416e39e8f00299192e9e48f5f1645f13a86859b675519598997314

hash以实际文件Get-FileHash SHA256读取，不是对渲染文本或规范化换行求hash。本稿不认证后续未读修改。另实际读本轮working spec、R114 rough数字dust与whole-CW段，以及本地源Def3.3、Eq19、Def3.9、Def17.1–17.4和19.4目标段；没有重证具名源高级wholeproof或认证外部优先权。

## 1. 精确scope与判定

**结论：修后通过本稿所列条件闭包与量词范围，未见未解决必修gap。** 通过的是：在主稿§2明确的bounded joint chart、usual Eq19、平均source类中，从给定完整matrix33 κ1 source构造另一个完整source。新source在一个新增clock的各grain具有固定scalar ξ原子。代价为η的固定整数倍及必要γ降级，δ和旧管/旧保留层坐标不缩放。

这不是无条件存在性构造，更不是全方向unit段低维Kakeya集合；usual Eq19 clock=[−1,1]也没有要求arclength恰为1。本审查不把它推广为每个dyadic parent保lower的规范、不把bounded-chart输入悄悄删掉、不把平均source加强成逐管duration。strong ∀grain cap与κ1排除的∃小η等强只在下面固定γ范围成立；没有证明等强的两命题任一者成立。

## 2. Time restriction、coarse Y lower与新allowed子格

八个长度1/4区间覆盖[−1,1]，择m_I≥m₀/8的一段，并在相反半轴取t*=±1/2，确有dist(t*,I)≥1/2。旧管T₀全部保留，保留时间层的每个X/Y/Φ/ξ及实际witness均不动；不存在选角或选point后免费补lower。

主稿对coarse Y-union的lower给了实际计数，避免任意子集继承的漏洞。核算如下：对一个留存union中的centre y，选含y的完整旧Y_t；在B_R(y)内有≥K₀^{-1}R/δ个fine cells，而任何ρ-cell/ball最多容C K₀ρ/δ个。故所留union在该球内的ρ-cover≥cK₀^{-2}R/ρ；R≈ρ时自身一个cell足够。原union的coarse upper则对subset单调。因此不需要Z_I在每个小窗稠密，也不需要I边界与每个allowed窗精确对齐。

取固定整数M，η'=Mη，得到

    R_(η')={δ^(jMη)}⊂{δ^(jη)}=R_η.

这是原allowed尺度的**精确子格**，不是nearest-scale恢复。所有纯旧窗和纯旧physical cubes的coherence均可在原同尺度调用。K₀有限幂及固定常数、m₀/8损失，在δ充分小时可由δ^{-Mη}与δ^{Mη−1}支付；M取在这些有限责任之后。若密度标记另放大一次η，也只需再乘固定整数，子格仍精确包含。未见δ被改成邻近4-adic数或引入affine rescale。

## 3. 任意dyadic δ的dust、whole 4AD/CW与有限化

主稿的A/B每位分别{0,1}/{0,2}；和每位遍历0,1,2,3，故自然概率下y₁、φ₂均匀，h/g作为digit函数仅需Borel。固定仿射归一化后四角child比例1/4。足窄strip不能同时交最远两个投影child，统一最多三支；宽r长s tube在尺度s只遇O(1)个parent，至r逐层计数给(s/r)^{log₄3}。slab概率计数则给r^{γ_d}，γ_d=1−log₄3>0。固定仿射变化和端点有限层只改常数。此法核native tube-KT，不是仅核全局slab，也没有smooth切线漏洞。

maximal Lδ nets不限制δ为4-adic。每个Voronoi cell含本centre附近半分离球，并由maximal覆盖控制在O(δ)球内；自然1AD给质量≈δ。a-grid cell质量≈δ²，product cell≈δ⁴。有限net的AD lower由连续局部质量/每cell upper给出，upper由分离及cell lower给出；r≈δ的端点只用固定L费用。tube cover upper对continuous set子集可直接继承，finite slab计数则用cell在Oδ增厚slab内及每cell质量下界。因此这项有限化覆盖全部足小dyadic δ，不是只取某子序列。

由joint参数的固定双Lip，labels维数2+1+1=4，T_d为usual joint4AD；N_rT计数与joint参数球可比。r接近δ时用单管lower吸收固定常数，r≈1时用bounded chart。whole-CW另有独立证明：条件y₁后，从(a₂,φ₂)到(x₂,z₂−h(y₁))的det=−v²，a₁再作Fubini，所以固定v≠0时R⁴点密度≤C|v|^{-2}。t*=±1/2使相对v∈[1/8,1/4]总在原clock段内。whole轴包含U则整段这些点在U中，slice积分给概率≤C|U|；没有把单个mark包含冒作whole包含。

finite cells到whole axes的误差为Oδ。此处提出过的小修已修：usual横向δ截面tube含一个**c₁δ** Euclidean球，半径常数依bounded slope；未必含恰δ球。若凸U含该球，U+B_Cδ包含于以球心为中心的固定倍U，故体积≤C'|U|。这足以将连续概率上界转成全部凸U的finite count upper≤C N_d|U|。4AD本身没有被当成CW证明。

## 4. 混合coherence、严格Φ包含及全部source责任

T_+=T₀∪T_d不再次取maximal net，exact duplicates只计一次，因此旧witness没有丢失。union joint4AD lower由centre所属component给出；另一component相交r球时，以其相交centre的Cr球计upper，端尺度用bounded global count。CW由两个component各自whole upper及N₀+N_d≤2N_+给出。没有方向分离输入，也不需要dust在旧clocks有marks。

新clock的X是实二维grid、Y是实际native-KT dust、Φ是实际AD1/slab dust、ξ=(0,a₂)，每个φ确由主稿(5.1)原whole graph见证。旧层全保；Y的KT exponent随γ降级变弱，Φ slab exponent同样变弱，均合法。k=ℓ使两矩阵consistency不再另有非空块。

strict Oρ检查通过：任一time窗或physical cube若混合旧层与dust，time gap迫ρ≥1/2。故bounded F或ξ跳跃≤1≤2ρ，常数固定，独立K、η、δ。纯旧继承同尺度原upper，纯dust的ξ对physical a真Lip。没有用Kρ遮盖fixed jump。

Φ部分也已按反馈实读修复：纯dust cube中，每个occupied dyadicρ-cell选一个原Φ_d点作为Φ_q，故Φ_d⊂Φ_q^(ρ)是严格dyadic包含；coarse AD1由fine AD的计数比较给出，而不是只证明某固定倍Euclidean覆盖。混合cube直接取Φ_q=[−1,1]²：原Def3.3的AD用ρ-covering number，未要求coarse carrier本身ρ-separated。仅在ρ≥1/2时，box局部ρ-cover介于1和固定常数，R/ρ≤2，确为(ρ,1,C)-AD；它也严格覆盖全部fine Φ_p。接受此宏观continuous box没有添加新公设，亦不表示该box在fine尺度是AD1。

所有coarse Y-union的混合窗同理：ρ≥1/2下任一非空bounded union都有coarse AD1的固定常数；纯旧用§2实算，纯dust用单层AD。因此共享F、all-scale Y-union、coarse Φ/ξ均已核，不能再以R114 dust缺bulk的失败直接否定这次**给定完整S₀后**的嫁接。

## 5. 原N/I、平均与逐管的核算

保留旧时间层给I_I≥K₀^{-C}N₀m₀，而I₀≤C N₀m₀。新增Nd≈δ^{-4}与N₀≈_{K₀}δ^{-4}同量级至K费用，N_+≤K₀^C N₀；m_+=m_I+1≈m_I。因此

    I_+≥I_I≥K₀^{-C}N_+m_+.

上述图每(T,t)只计有界次；canonical化若丢某point degree，在这里也只承担总I核算，不被用于重调用逐point lower。source本身的全部Φ和witness没有从数据中删除。δ-cube volume需另乘δ⁵，whole tube体积≈δ⁴，给平均density≥δ^{Cη}；没有混淆count I与volume I。

这里是**增管**：q=N₀/N_+、p=I_I/I₀，新平均密度至少pq倍旧密度；不是删管公式p/q。主稿已区分。新增clock访问至多C N_+，所以所占全局原I比例≤K₀^C/m_+≤K₀^Cδ，η先足小时是小正幂。dust管可以在其余时间完全无selected marks，完整Def17只有派生的全局平均density，未要求每管长duration。因此该事实不是遗漏hyp；若额外加强为逐管K^{-C}m visits，本构造不适用。

反向边界也通过：本graft只给一个可忽略clock上的坏grain，不能反“原I意义正质量good grains”cap。主稿§9对此明确，未把强∀grain失败资格当成平均版本已证或已否。

## 6. ∃小η的双向强度与最后范围

为避免“同一数值η”误读，正式化主稿§8。固定0<γ≤γ_d，在其§2 bounded-chart usual-source类上定义：

    C_γ：存在a,τ,C,η_cap>0，使对每0<η'<η_cap，
         δ充分小时所有source满足strong ∀grain cap；
    B_γ：存在η_ex>0，使对每0<η<η_ex，
         δ充分小时不存在该完整κ1 source。

若C_γ真，可先将a替为min(a,1/2)，只限制到原cap的尺度子区间，因此不失一般性有0<a<1。取输入η足小，使η'=Mη<η_cap、η'≤a/2且C₁η'<aτ/4；若完整source存在，graft得到同γ的新source。令j=floor(a/η')，则jη'∈[a/2,a]，故ρ=δ^{jη'}∈[δ^a,δ^{a/2}]，在新allowed格内；因a<1还有ρ≥δ，δ充分小时也≤ρ₀。新grain的固定ν=e₁,b=0带比例为1，而cap upper

    δ^{-C₁η'}ρ^τ≤δ^{aτ/2−C₁η'}<1

矛盾。δ阈值可取graft阈值与cap在参数Mη处阈值的最小者，均是“η固定后δ足小”允许的阈值。于是C_γ⇒B_γ；反向B_γ⇒C_γ是真空成立，可任取a,τ,C并缩η域。故两者按∃小η的正幂量词等强，**并非同一η和同一δ阈值逐字等价**。

γ₀>γ_d时graft只保证barγ≤min(γ₀,γ_d)；它不证明仅给定较强γ₀的cap也同γ₀等强。较弱γ_d的cap若成立，会通过降级排除更强γ₀ source，但这与较强γ₀ cap本身是两个命题。主稿已限定此范围。

本轮条件闭包因此确实比phase换名多一项实际qualification信息：强∀grain标尺在准确范围内已经承担完整κ1排除责任。它仍不等价ordinary满维或长期Goal，也未证明C_γ/B_γ任何一者。不将本审查通过升级为正source gain、新维数界、无条件反例、新颖性认证或外部同行评审。

已修两点在raw SHA所锁版本中实际读回；本稿无未解决必修项。root可据此整合状态，若主稿数学内容再改需另读新版本再确认。
