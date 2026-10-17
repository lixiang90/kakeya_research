# R0049：一般输入、sticky正规化与保亏损账本

2026-10-17，root整合。Goal active，未经外部同行评审。本轮有具体可证的重缩/删选与附加类正规化，但未证一般E5*、H5或新高维维数界。working specification在施工前保存；不把已sticky的输入写成一般Kakeya的归约。

## 1. 原目标、量词与闭包

原R5单位图管有满四参数δ-separated方向网，m≈δ⁻⁴，每原label权1、每管至少δ⁻¹⁺η个原time-bin marks。记I₀为原总计数访问，E为原marked δ-cells并，故 `I₀≥cδ^η m/δ`。E5*固定原体积亏损κ₀∈(0,1)，假设|E|≤δ^κ₀；对每小target ε≪κ₀，试图保≥δ^ε原访问，经合法共同affine/clockwindow，生成h与δ成固定幂关系的unit h直管族，joint(4,h⁻ε)-AD、CW≤h⁻ε、平均原shading≥h^ε，且输出仍有κ_out≥cκ₀的体积亏损。AD的lower按源定义作用于**support-centered balls**，不是任意仅擦边非空球。

候选未证。H5若成立可使某些κ₀输入最终为空；反向提取还需未证完整R5sticky结论及deficit回传。shading删选/原label限制会改变平均、逐管密度和方向饱和，须分别付账；不能因名称不同登记新的正幂机制。本轮不新立数学ID。

## 2. 实际来源已假定什么

实际全文读Wang–Zahl2210.09581v2 §1.2、§2、Def3.1–3.2、Lemma3.3及Prop3.2证明。Def2.1(b)已经要求：每个δ≤ρ≤1，存在ρ-tube cover，任一ρ方向上至多δ⁻ᵗ根coarse父管。M(s,t,δ)和σ_n在这个类上定义；Def3.1的extremal同时要求该覆盖、原总shading质量及接近σ_n的并集上界。

Prop3.2由已有(b)给父管总数≲δ⁻ηρ⁻⁴，再给每parent原质量≥δ^{O(η)}ρ⁴；Lemma3.3用同一类的M下界控制fine multiplicity。coarse/fine上界与原extremal小并集共同迫两层近饱和，才得每parent/cover重新extremal。一般|E|≤δ^κ₀既不提供(b)，也不说明κ₀接近该类σ_n。Conj1.2明确是general近极值到近sticky的猜想，不是Prop3.2已完成的步骤。

Wang–Zakharov2609.22035v1 Def17.1的Kd(κ)同样从joint(d−1)-AD、CW和平均near-full shading开始；Prop17.2/18.2取这个Kd类的极值，§18起点已写AD/CW。它们没有提供本E5*初始化。A的有界primary核未读到适用ordinaryR5的一般归约；未命中不认证不存在或优先权。R42digit-permutation不满足(b)的coarse multiplicity，但未付小并集，不能当E5*反例。

## 3. 保原global质量本身限制共同window和Jacobian

取共同clock长度q，所选原轴在该区间位于一条共同仿射轴的Cr邻域，δ≤r≤1。合法map为

    Φ(t,x)=((t−t₀)/q,(x−c(t))/r),  h=δ/r,
    J=q r⁴,  |det DΦ|=J⁻¹.

假设保留的原访问I_A≥δ^ℓ I₀，a=ℓ+η充分小。每个原label至多C(q/δ+1)次，先用原m计数就得 `q≥cδ^a`。若r≤q，端点相减给原slopes在宽Cr/q的box内，原δ-separation给N_A≤Cδ⁻⁴(r/q)⁴，故 `r⁴≥cδ^a q³`。若r≥q，直接qr⁴≥q⁵。因此

    J≥cδ^(5a),  r≥cδ^(5a/4),  δ≤h≤Cδ^(1−5a/4).

wholeclock q=1有更强r⁴≥cδ^a。这些是**已有保质量parent/window**的必要预算，不证明其存在或AD lower。q⁻⁴虽会出现，但q本身不能是固定幂过短；不能仅据q⁴因子宣称整个E5*不可能。

## 4. 网格外包有额外费用，local-heavy可以支付

源Def3.2在wholeclock横向放大r⁻¹，h=δ/r。原δ-cell变为横向h、clock δ的薄块；outer h-cube并体积不由Jacobian自动常数比较。root/A实际视觉读已存v2 PDF13，原(3.5)确写常数~，并非OCR。A/B独立的clock-comb校准表明该字面推断缺条件：slopes取r-box内δ网，远离原点的每h-clock块仅保λ比例原δmarks，λ=δ^b且b<log r/log δ，则原union≈λr⁴、image≈λ，而outer h-grid union≈1。该族满足Lemma3.3的局部质量阶和近sticky cover，却使比例≈λ⁻¹。它不满足本E5*原全方向输入，也不否源最终定理，因为允许refinement和小幂费用。

正确local修复如下。wholeclock里若pair-volumeδ⁵I≥δ^u r⁴、N≤δ⁻ᵛh⁻⁴，按原clock长度h分每条管的blocks，删mark数<βh/δ的blocks，取β=δ^(u+v+w)。删除比例≤Cδ^w，余下原cells E′满足

    |outer_h(Φ E′)|≤C β⁻¹ r⁻⁴ |E′|.

证明每个output cube由一个heavy原tube/block见证；其中至少βh/δ个不同time-bin原cells，在固定邻接像中贡献≥cβh⁵体积。固定颜色/邻接有界重叠求和即可。只删原marks，不把别人的marks转给代表，不densify原shading。

一般q≥r时用原clock长度qh，原重块质量≥β qhδ⁴，除J恰为βh⁵；总删除≤CβN_A q/δ。若q<r，原cell像的各主尺度已≥h，可直接固定网格packing，外包常数付。原cell/轴交点的端点、旋转和固定加厚只付常数，B稿给完整约定。

设本节应用于§3已有parent，取β=δ^(a+w)，则删除≤Cδ^w I_A；若|E|≤δ^κ₀，得到

    |E_out|≤Cδ^(κ₀−6a−w).

选a,w≪κ₀可保固定正幂亏损。任意后续细删shading可能破block-heavy；它只自动闭于whole-label/whole-selected-block限制。不得声称源已写此修复或Prop3.2全proof已认证。先取constant multiplicity再做heavy也不能把新outer的multiplicity当原µ；原µ上界可另用初始E与上述outer upper比较，完整后续归纳责任另列。

## 5. 方向代表、CW及密度不应另虚报成固定幂障碍

§3map后一个h-direction bin的原slopes落在O(δ/q)内，故原labels≤Cq⁻⁴≤Cδ⁻⁴ᵃ。每个joint bin选原访问数最多的一个原label，固定着色实现分离，至少保cq⁴ I_A；不合并其它labels的marks。先block-heavy再只删whole labels保本节shadow upper。

最后N′=p′m、每label原window长度≤q，给 `p′≥cδ^a q³≥cδ^(4a)`。方向packing与John ellipsoid给输出CW≤C r⁴/(p′q⁴)≤Cδ⁻⁸ᵃ；joint ball upper≤Cq⁻⁴(s/h)⁴。原mark的真实轴段变换后，平均duration≥cδ⁴ᵃ；q<r时一个原δ段跨多个h-bins，不能只数一次新bin。按小ε预算选择ℓ,η,w可同时付这些小幂，保target δ^ε原质量、h^-ε上界和固定κ_out。

这些计算**仍没有joint AD lower**，也没有产生合格parent。它们缩小真实缺口，不把一个显眼Jacobian/clock费用误称不可逾越。全部步骤的细节与独立攻击见B稿§§2–5；E5*并未因此通过。

## 6. 一个完整合法特殊类：全尺度近最小joint-cover上界

额外假设原八维joint参数box内每dyadic s∈[δ,1]的occupied cells数 `N_s≤K s⁻⁴`，K≤δ⁻η。这是nearsticky的实际全尺度coarse-entropy输入，尚未由小并集推出。原方向分离另给每joint s-cell标签数≤C(s/δ)⁴。

固定target ε，选η≪ε、θ=cδ^(ε/2)。在参数树由细到粗，若节点当前后代数<θ(s/δ)⁴，删该节点全部剩余labels。每尺度最多Ks⁻⁴个原节点，因此总删除

    D≤C θK log(1/δ) δ⁻⁴.

原访问损失≤CD/δ，除以I₀≥cδ^ηδ⁻⁵为 `C log(1/δ) δ^(ε/2−2η)=o(1)`。不能只以label比例宣布访问保留，已付原密度分母。

每个最终存活节点在处理时达到threshold，后续祖先要么整删它、要么不改变它。因此所有最终occupied节点同时有lower；用中心为存活label的球内一个更细可比尺度cell得到任意support-centered ball lower。r=O(δ)用该label处理，固定维度费用由ε/2余量吸收。原upper仍保，故得到joint(4,δ⁻ε)-AD族。

N′≈m，wholeclock原δ方向分离的CW≤C，保near-all子族后仍≤C。每条余下管的**全部原marks**保留，原逐管密度仍≥δ^η；若最初只有平均密度，访问保留后需另heavy。取h=δ、无clock/affine变化，输出union⊂E，κ₀原样保留。这完整证明附加coarse-cover类的E5*，不是一般E5*或新的高维维数界。

## 7. 精确剩余责任和本轮停止

一般direction net只给joint球内upper，不给§6所有尺度coarse-cover数量上界。普通uniformization可平衡某些branching，不能强制指数恰为4；s>4不进入Kd类。源(b)恰在提供这个小coarse数及每parent质量，不能先去掉后在极值证明里再使用它。

目前没有从原|E|≤δ^κ₀证出§6上界、其合格parent版本或同强度原质量结构，也没有全部原假设下的反例。E5*未证未否。对已有保subpower globalmass的parent，Jacobian/rounding/代表/CW/密度可付；实质仍是合法结构提取，不是待调的r/q/AD阈值。不能把附加上界移进input便宣布一般归约完成。

按working spec停止这个general-to-sticky初始化gate，提前macro，不续parent/entropy/η阈值，也不把coarse-entropy条件改名立新方向。general/higherdim、所有未付mixed与原Hausdorff仍open；旧冻结保持。

## 8. 审查和归档范围

A独立读源/正式版本范围并核树和重格，B独立重建parent/window、blockheavy、去重和ADcore证明；正式reviews须全文读完main/macro/next才写。本轮没有新有限实验，不重跑R46/R47。已存PDF/元数据按实际读取更新，未取得的AMS正式PDF不伪报已核。无新数学ID/major/novelty认证；内部证明与具名外部proof责任分开。最终root统一state/route/registry/round/验证并沿R48父safe sync，Goal active。
