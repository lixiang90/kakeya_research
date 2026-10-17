# R0049正式独审：原质量、尺度与输出亏损

2026-10-17，`lifting_obstructions`。本review通过下列明确局部预算、附加类和scope；未经外部同行评审。一般E5*与H5均未证未否，无新高维下界或重大性认证。

## 1. 实际全文和独立范围

已实际全文读root `R0049_general_input_regularization_and_deficit_ledger.md`八节、A `R0049_general_to_sticky_source_implication_audit.md`十一节、macro八节、next nonlinear lift五节、working specification及B施工八节。B稿用于检查整合一致性，不将自身施工算作独立认证；其独立审查另由A/root完成。

源端实际读Wang–Zahl2210.09581v2 §1.2、Def2.1/3.1/3.2、Lemma3.3及Prop3.2全部证明；对照Wang–Zakharov2609.22035v1 Def17.1与§18真实起点及R43已审操作。A的官方版本/有限外查按明确scope读取，不伪称本人重复了其全部网络操作，也不预认证尚未写出的元数据、PDF校验或Git同步。

## 2. 原source不是一般小并集初始化

root§2与A§§3–4、7–8通过。WZ2025 Def2.1(b)已要求所有尺度近sticky covers；M、σ_n和η-extremal均在此类中定义。Prop3.2先由(b)控制coarse父管数/父质量，再用同一类的极值下界与原并集上界迫coarse/fine饱和。任意原κ₀小并集既不提供(b)，也不保证接近同一σ_n。Conj1.2仍是general近极值→近sticky猜想，不能用Prop3.2标题将它升为定理。

WZ2026 Kd、Prop17.2/18.2已假joint(d−1)-AD/CW；其极值见证存在量词不是给定ordinary family的restriction结论。源中新配置生成/厚化也不能未经回传等同于原任意marks。A将这些责任与R43局部PW审计分开，正确。

## 3. parent、clock与labels的共同预算

root§3最关键的新必要式是正确的：原m≈δ⁻⁴、I₀≥cδ^ηm/δ且I_A≥δ^ℓI₀时，先用每个原label最多C(q/δ+1)次，得到q≥cδᵃ，a=ℓ+η。不能只用选后N_A或漏掉这个全局上界。

r≤q时方向band Cr/q给r⁴≥cδᵃq³，r≥q时J=qr⁴≥q⁵，合得J≥cδ⁵ᵃ及h=δ/r∈[δ,Cδ^(1−5a/4)]。wholeclock r⁴≥cδᵃ更强。故本强原质量目标下q⁻⁴也只能是小幂费用；将它单独称不可逾越fixed-power障碍会错。此预算只对文中明确的共同横向r/crop q map、合法原轴containment成立，不认证任意各向异性affine或parent存在。

output h-bin含原slopes宽O(δ/q)，原label数≤Cq⁻⁴。先block-heavy，再每bin取原访问最多的一个原label并固定着色，保cq⁴I_A，不合并他人marks，且whole-label删选保heavy。每label最多q/δ次，故p′≥cδᵃq³≥cδ⁴ᵃ。以新fine方向间距qh的packing及John ellipsoid（已计h取整误差）得到CW≤Cr⁴/(p′q⁴)≤Cδ⁻⁸ᵃ；joint球upper≤Cq⁻⁴(s/h)⁴。真实原δ轴段在新clock上的长度δ/q须保留，尤其q<r时跨多个新bins，由此平均duration≥cδ⁴ᵃ。上述都没有产生joint AD lower。

## 4. 外网格校准、单次修复和亏损

root§4与A§§5–6通过。Def3.2的横向放大r⁻¹但clock不放大，将原cell变为h⁴×δ薄块；Jacobian本身不足以支持字面(3.5)的outer h-grid常数比较。远clock方向bush配共同comb保source局部质量阶/nearsticky covers，原union≈λr⁴、rounded新union≈1，膨胀λ⁻¹。该校准不满足本原满方向小并集全部假设，不被误报为E5*或原最终定理的反例。

local-heavy修复的见证计数正确：wholeclock每good tube/block有≥βh/δ个原时标，经Φ后在一个Ch邻域贡献≥cβh⁵；output cubes固定颜色求和给outer≤Cβ⁻¹r⁻⁴E′。一般q≥r用原block qh，除J后同样贡献βh⁵；q<r时原cell像所有主尺度≥h，固定网格packing足够。whole δ-cell固定邻接约定、边界和共同shear只付常数。

β=δ^(a+w)时总删除≤CδʷI_A，J界给新union≤Cδ^(κ₀−6a−w)。取ℓ、η、w为target ε与κ₀的充分小份额，可同时付原访问、CW、平均density和κ_out≥κ₀/2；这是条件于已有保质量parent的预算，不是提取存在定理。

A保initial常重数μ₀而不把heavy后的新measure误当恒μ₀，推μ₀ upper的顺序正确。arbitrary后续shading refinement可破heavy，两个稿件均明确只通过一次local repair，没有追认原source已写或整Prop3.2已完整修复。

## 5. 树正规化的原incidence与special-class边界

root§6与A§9通过。额外全尺度N_s≤K s⁻⁴，K≤δ⁻η，配原方向upper；从细至粗删当前小于θ(s/δ)⁴的节点，θ=cδ^(ε/2)。每节点至多收费一次，每尺度总数≤Ks⁻⁴，故删label数≤CθKlog(1/δ)δ⁻⁴。删原访问还必须除原δ^η密度，比例≤C log(1/δ)δ^(ε/2−2η)=o(1)，主稿已真实支付。

存活节点处理后只可能被祖先整体删除，未被祖先删除的细节点不再局部变化；因此所有最终lower同时成立。support-centered ball内取更细可比dyadic cell，s=Oδ用该label处理，原方向packing给upper。不是仅有处理当时lower，也不对擦边任意非空球乱加下界。

whole labels保原全部marks、总数仍≈δ⁻⁴，CW仍O1；h=δ、Eout⊂E，体积亏损κ₀原样保留。若只有平均初始density，原总量保留不自动给逐管，须另heavy。此项完整证明的是附加near-minimal joint-cover类；小并集→该全尺度cover尚未证明。source已有sticky输入可以供类似上界，不是general初始化。

## 6. 停止与下一任务的scope

当前main/macro按spec停止general→sticky gate，不续coarseentropy/AD/parent/η阈值；没有将附加cover上界移进input宣称E5*完成。真实欠缺是从原小并集提取恰四维coarse结构，未有全部假设下的反例，Goal保持active。

next已纠正来源：真正lifting读本是Nadjimzadah **2609.06299v1**；2511.10918v2/GAFA00750-4是另一篇Bourgain-condition文章，不是lifting修订本。该纠正避免了误借source。Fu–Gan topology仅作本轮未选有限scope比较，不冒充rough原管族已有连续/边界正则selector。

下一smooth空间非线性submersion类严格超出旧LIFT005空间仿射分类；将π₀以非线性坐标拉直会弯曲原straightlines，不能据此自动套旧rankB≤1。next保同一原clock、full open(y,w,ρ)、Θ独立w及rank3、整段coherence；禁止selector/降rank/只配有限jets，范围清楚。它不与原uniform shading正gain命题等价，不解冻旧AFF3/CP/PW等路线；构造或rigidity须下一轮真证。直接潜在收益为forward曲线lifting，不能逆向当一般R5结果。若仅旧affine障碍改写则一轮停止，scope与长期目标一致。

正式审查完成。未见当前主稿必须修正的数学跳步；metadata/remote receipt留主代理另核。停止编辑及检索，不Git。
