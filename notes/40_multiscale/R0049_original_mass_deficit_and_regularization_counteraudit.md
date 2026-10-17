# R0049：原计数质量、归一化亏损与AD正规化的真实预算

2026-10-17，`lifting_obstructions`。本稿只编辑指定接口；未经外部同行评审。不证明或否定一般E5*、H5或Kakeya。下面给出可独立核的预算和一个合法特殊类，明确不将附加coarse-cover假设说成由小并集推出。

## 1. 任务和源范围

E5*原输入是bounded R5图线、满四参数δ方向网，每原label权1、每管至少δ⁻¹⁺η原time-bin marks，原全部whole δ-cells并E体积≤δ^κ₀。欲保至少δ^ε**原计数访问**，经原labels/marks删选、共同合法affine/clockwindow，得到uniform h管族的joint4-AD/CW、near-full原shading，且仍保固定正幂output deficit。κ₀是体积指数，不能与H5中的维数增益σ混用。

恢复已读context.py、固定入口/registry78/latestR48、R49 working spec和R48 next。实际读Wang–Zahl2210.09581v2 §1.2、Def2.1/3.1/3.2、完整Prop3.2及Lemma3.3；对照已审R43实际§18操作稿与Wang–Zakharov2609.22035v1 Def17.1/§18起点。后者从joint(d−1)-AD/CW极值类开始；前者Def2.1(b)已假设所有尺度的近sticky covers。二者不是general小并集→joint4-AD的来源。

本轮不重报R42无小并集的digit-permutation反例，也不把不同一般性regularization称新五维结果。停止条件是：不能从真实小并集输入付coarse joint entropy/lower，且只能在额外nearsticky假设下闭合，就停止该gate，不续parent或AD阈值。

## 2. 一个共同parent/window的精确原计数模型

令m=#T≈δ⁻⁴，I₀为原总访问数，则 `I₀≥cδ^η m/δ`。选原label子集A与共同clock区间I，长度q≤1。共同轴c(t)是仿射函数，假设所选轴在整个I上位于其Cr邻域，δ≤r≤1。定义

\[
 \Phi(t,x)=\left((t-t_0)/q,\,[x-c(t)]/r\right),
 \qquad h=\delta/r,\quad J=q r^4.
 \tag{1}
\]

Cr containment保证变换后的轴是bounded unit-clock直线；`|det DΦ|=J⁻¹`。此处“合法”还包括固定chart、实际管外包误差和端点只付固定常数，并非把任意曲线直化。令I_A只数所选原labels在I内的原访问，设

\[
 I_A\ge\delta^\ell I_0,\qquad a=\ell+\eta<1/10.
 \tag{2}
\]

每label在I至多C(q/δ+1)次，故先由m而不是N_A计数，得

\[
 q+\delta\ge c\delta^a,
 \quad\text{从而对小δ，}\quad q\ge c\delta^a.
 \tag{3}
\]

这一步不能遗漏。原mass保留本身排除了固定幂过短clock；不能仅看到q⁻⁴就宣布E5*无法闭合。

若r≤q，原slopes在宽Cr/q的四维box内。原δ方向分离给

\[
 N_A\le C m(r/q)^4,
 \quad I_A\le C N_Aq/\delta,
 \quad r^4\ge c\delta^a q^3.
 \tag{4}
\]

若r≥q，则直接有r⁴q≥q⁵。结合两种情况与(3)，

\[
 \boxed{J=q r^4\ge c\delta^{5a}},
 \qquad r\ge c\delta^{5a/4},
 \qquad \delta\le h\le C\delta^{1-5a/4}.
 \tag{5}
\]

whole-clock q=1时更强：r⁴≥cδ^a。以上均是必要预算，不是存在好parent的结构定理。取r=q=1当然可保质量，但不因此得到AD lower。

## 3. 纯Jacobian不足以控制h网格外包

Wang–Zahl Def3.2把clock保持不变、横向放大r⁻¹，再把image shading外包为h=δ/r cubes。原δ-cell经此图变成横四轴h、clock轴δ的薄块；用h-cube外包可能再膨胀r⁻¹。原(3.5)字面的双边常数比较不能只从(3.4)的Jacobian推出。

这是严格有限校准而非Kakeya反例。取r=δ^s、λ≈δ^b，0<b<s<1；whole-parent里取过原点、slopes为r-box中固定倍δ网的管，N≈(r/δ)^4。把每管marks放在t∈[1/2,3/4]的共同细clock comb上：每⌈δ⁻ᵇ⌉个原timebins取一个，故逐管密度≈λ。此远clock段管重数有固定上界（将slope网格取足够大的固定倍δ，还可使相应pieces互不重叠），于是

\[
 |E|\asymp\lambda r^4,
 \qquad |\Phi E|\asymp\lambda.
\]

但comb间距≈δ/λ≪δ/r=h；外包h-grid在该固定clock段沿每条新轴都填满固定比例。新slopes为h尺度满网，故rounded union体积≈1。因此膨胀比≈λ⁻¹=δ⁻ᵇ，不能以固定常数或polylog隐藏。该父族满足源Lemma3.3所用的方向/近sticky covers及总pair-mass≈λr⁴；不保E5*原满R5全方向小并集输入，不用来否主定理。它也不否Lemma3.3最终结论，因为结论允许refinement，且有下述小幂修复。

## 4. 显式local-heavy修复：保原mass后再控制rounded union

先给实际whole-clock版本。原parent横尺度r，h=δ/r，N条原labels；将clock分成长h区间。对每个(T,block)，删去其中原marks数小于β h/δ的部分；剩余block称heavy。总删除访问≤CβN/δ。

若原pair-volume `δ⁵ I≥δ^u r⁴`，且 `N≤δ⁻ᵛ h⁻⁴`，取

\[
 \beta=\delta^{u+v+w}\quad(w>0),
 \qquad\frac{I_{\rm deleted}}I\le C\delta^w.
 \tag{6}
\]

令E′是保留原marks的whole δ-cell并，Ŷ是其变换后的固定倍h-grid外包，并只赋给保留block的原labels。则

\[
 \boxed{|\widehat Y|\le C\beta^{-1}r^{-4}|E'|.}
 \tag{7}
\]

证明：任一产生的output h-cube取一个原label/block见证。该heavy block至少βh/δ个不同时标原δ-cells；它们都位于此output cube的固定邻接preimage中，因为新轴斜率有界、block长度h。原cells互不同时标，故其原union体积≥cβhδ⁴；经Φ后为≥cβh⁵。对output cubes作固定颜色划分，使其固定邻接立方体互不重叠，求和得(7)。这里只需一个原见证，不把不同labels的marks合并，不要求原μ独立或恰恒定。

原“cell仅与轴相交”的网格约定可先取固定δ-neighbor enlargement；whole δ-cell并的这种增厚体积≤C|E|，并保证每原mark含固定长度δ的轴段，不新增幂费用。边界clock blocks和仿射shear同样只需固定邻接与常数。常数依赖固定chart和维数。

对(1)一般q，若q≥r则按**原clock长度qh**分block，同样证明

\[
 I_{\rm deleted}\le C\beta N_Aq/\delta,
 \qquad |\widehat Y|\le C\beta^{-1}J^{-1}|E'|.
 \tag{8}
\]

此时原block里有βqh/δ个时标；原体积≥cβqhδ⁴，除J恰为cβh⁵。若q<r，image原cell所有轴均≥h，固定h增厚可直接用packing比较，(8)的体积式可取β=1，无须此time-heavy删选。

必须保持先后顺序：若之后再任意细删shading，block-heavy可能失效，不能免费沿用(7)。保留whole labels或保留整个已选block不破坏它；其它refinement须重做其预算。本修复不是追认原source已写，也不等于完成原Prop3.2每步认证。

## 5. 标签去重、CW、密度和deficit可以一并付小损

仍在(1)–(5)下。一个output h-joint parameter bin原像，对原slopes的宽度是O(δ/q)；所以它含原labels至多

\[
 L_{\rm dup}\le Cq^{-4}\le C\delta^{-4a}.
 \tag{9}
\]

对每bin选保留原访问数最多的**一个原label**，不把其它label的marks转给它；固定着色可使所选h-tubes分离，或付已计的固定h外包把参数取整。这至多损C L_dup，所选访问量仍≥c q⁴ I_A。若先local-heavy、后只删whole labels，(8)仍保持。

以原full方向counting law，设最后保留N′=p′m条原labels。共同crop/affine后真正可用的convex Wolff upper是

\[
 C_{\rm CW,new}\le C\frac{r^4}{p' q^4}.
 \tag{10}
\]

可直接由原方向分离证明：新slopes fine spacing≈(q/r)δ=qh；任意含新unit h-tube的convex body具有最小John轴≥ch。将body固定倍h增厚，含相应原新轴；方向packing给其中原labels≤C(qh)⁻⁴|W|。除N′=p′m得到(10)。bounded graph chart外取原共同有界区域的交即可；r、q或p′都不能删除。原labels取整误差在此增厚中已计。

由保留访问量与每label最多Cq/δ次，`p′≥cδᵃq³≥cδ⁴ᵃ`。故(10)至多Cδ⁻⁸ᵃ。新joint ball的原upper同理由slopes给 `Cq⁻⁴(s/h)^4`，但没有AD lower。每原mark代表长度≈δ的真实轴段，coarsening后的新平均duration至少cδ⁴ᵃ；q<r时image轴段跨多个h-timebins，不能仅把一个原mark算成一个新bin而漏掉这个长度。

例如在(8)取β=δ^(a+w)，则删除访问≤Cδʷ I_A；结合(5)，最终rounded union满足

\[
 |E_{\rm out}|\le C\delta^{\kappa_0-6a-w}.
 \tag{11}
\]

取a,w为target ε及κ₀的充分小固定倍，可同时付：原访问保留≥δ^εI₀（去重后损至多约δ⁵ᵃ）；CW/joint upper≤h⁻ε；平均shading≥h^ε；以及 `|Eout|≤h^(κ₀/2)`。这些均只在**已有合法parent/window且保(2)原质量**后成立，不生成joint4-AD lower或near-minimal joint covers。短clock的q⁴虽真实出现，(3)说明它在本强原质量目标下也可付小幂；本稿不把它误报成固定幂不可能性。

## 6. 一个完整合法特殊类：coarse joint entropy upper足以提AD core

假设原输入另有下列真实上界：在固定bounded八维joint参数box里，对每个dyadic s∈[δ,1]，occupied s-cells数

\[
 N_s(T)\le K s^{-4},\qquad K\le\delta^{-\eta}.
 \tag{12}
\]

它比直接假AD lower弱，但已是所有尺度的near-minimal joint coarse entropy；**没有从E的小并集得到(12)**。原方向δ分离另给每个joint s-cell内的count≤C(s/δ)⁴。

固定target ε>0，令η≪ε并取θ=cδ^(ε/2)。在dyadic参数树由细到粗操作：当某cell的当前剩余label数<θ(s/δ)⁴，删除整个cell的剩余labels。每cell至多删除一次，每尺度至多K s⁻⁴个cells，故总删除labels

\[
 D\le C\theta K\log(1/\delta)\,\delta^{-4}.
 \tag{13}
\]

删除的原访问≤CD/δ；用I₀≥cδ^ηm/δ，m≈δ⁻⁴，得删除比例≤C log(1/δ)δ^(ε/2−2η)=o(1)。这里不能只按label比例宣称保原incidence；已单独付其δ⁻η分母。

每个最终occupied dyadic cell在其处理时已过threshold，后续祖先要么整体删除它、要么不改它，因此最终count≥θ(s/δ)⁴。原upper仍保。对中心为保留label的任意ball B(a,s)，取包含于B(a,s)的更细dyadic cell、尺度与s可比，得

\[
 c\theta(s/\delta)^4
 \le\#(T'\cap B(a,s))
 \le C(s/\delta)^4.
 \tag{14}
\]

s=O(δ)用该label本身处理；固定维度因子可由θ的ε/2余量吸收。采用源AD定义的support-centered balls，不对任意擦边非空ball虚加lower。

N′≈m，原方向分离给原uniform CW≤C（John ellipsoid的方向packing，或既有R43所用标准方向-CW输入）；whole-label删选后仍≤C。每条保留label的全部原marks保留，逐管density仍≥δ^η；如仅有平均初始density，(13)保总incidence后须另heavy，不能自动宣逐管。取h=δ、无clock裁切/affine，`Eout⊂E`，故κ₀亏损原样保留。于是附加(12)的真实特殊类满足E5*要求。

这只是已近sticky输入的初等正规化；不是新一般Kakeya估计或新ID。Wang–Zahl Def2.1(b)的nearsticky covers在bounded chart中确实供给类似(12)，而一般满方向只给upper Frostman，并不供给(12)。

## 7. 真正未付的初始化与source边界

以上预算反而缩小了缺口：若确能保global δ^o原incidence来选parent/window，Jacobian、clock、coarse labels和grid-shadow可一起付δ^o损失；不能把某个显眼费用单独升级为不可能结论。但r,q由(3)–(5)被迫只改变小幂尺度，不能指望一次任意深的重缩自动修复原固定幂joint entropy surplus。

目前没有证明：从E小并集及原full方向，能得到(12)、它在所选parent的新版本，或其它足以推出joint4-AD lower的同强度原质量结构。一般dyadic uniformization能使若干block branching可比，却不把所有branching exponent强制成4；用s>4 regular族不能进入Def17.1。原CW、方向Frostman和原总count也不单独给cover上界。

Wang–Zahl Prop3.2的粗/细extremality传递依赖其**原sticky class**的all-scale covers，以及该class的极值下界M(s,t,δ)；不能对general小并集直接调它的Lemma3.3。(7)修复一个rounding接口也不会补出这个初始化。Wang–Zakharov§18从jointAD/CW的Kd极值开始，原AD lower负责whole-parent质量和coarse无权law；去掉lower后不能沿旧证明保same priors。

## 8. 收尾与停止

已得：原global计数保留迫q和J不能太小；local-heavy修复outer-grid体积；labels去重/CW/density/deficit的共同小损账本；附加全尺度near-minimal joint covers时的完整AD4 core提取。没有得到一般E5*，也没有保其全部小并集/满方向条件的反例。

具体未付项是小并集到joint coarse entropy/lower的几何输入，不是待调的AD/parent阈值。若主代理整合后无新的真实来源，按一轮规则停止此general-to-sticky提取gate并macro；不将(12)加到原input后宣布一般归约通过，也不把source猜想或小幂rounding修复当重大结果。长期Goal保持active。
