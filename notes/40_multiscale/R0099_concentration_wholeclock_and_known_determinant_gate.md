# R0099：浓集序列的整线段输入与旧行列式估计强度门

2026-10-19。固定n≥5（校准取n=5）；外部高级定理具名输入，以下应用与反攻已通过两独立限定全文审查及root整合，登记内部reviewed，未经外部同行评审。没有新高维维数界。

## 1. 命题、量词和三种浓集

给有限族(a_i,v_i,w_i)，|v_i|=1、w_i≥0、W=Σw_i>0，原轴a_i+[0,1]v_i位于共同有界区域。ρδ为非负光滑紧支撑径向近似恒等，定义k_i(x)=∫₀¹ρδ(x−a_i−tv_i)dt及Mδ=Σw_i k_i v_i⊗v_i。先取W=1。严格区分固定null Kakeya载体测度的mollification、随δ变化的全轴邻域体积趋零、以及只有原marks Y_i小而全轴不小。第三类不能仅凭小footprint调用浓集定理。本轮检验新GR序列定理的真实输入与输出，并先比较旧CV加权端点估计；不把新paper标题当新Kakeya增益。

## 2. 新定理的确切内容

Gennaioli–Rindler2608.20899v2 Def1.3用Frobenius范数：u_j光滑、Au_j=0、L¹norm1、→0inmeasure、在Q闭包上weak*收敛且极限无边界质量、Θu_j=(u_j/|u_j|)#(|u_j|dx)→μ。Rem1.5允许Au_j=z_j、sup||z_j||₁<∞且z_j→0inmeasure。Th1.6给μ=∫νdπ，组件barycenter[ν]∈Λ_A；Th1.7在constant rank且spanΛ_A=V时组件还能取Y_A内。新定理实质覆盖有绝对连续弱极限的浓集序列，不能整体称旧DPR等价。它不说总barycenter属于Λ，也不在一般有符号空间说μ每原子在Λ；不保原(a,v,t)标签的可测restriction。

## 3. 对称散度算子真正合格

V=Sym_n，A=行散度，符号A(ξ)B=Bξ。|ξ|=1时，对任意y取B=y⊗ξ+ξ⊗y−(y·ξ)ξ⊗ξ，即Bξ=y，故rank恒n。Λ={detB=0}。秩一v⊗v在Λ（取ξ⊥v），这类矩阵张成Sym_n，因此Th1.7的两附加输入成立。对PSD M有|M|F≤trM≤√n|M|F；∫trMδ=1，cδ=∫|Mδ|F∈[1/√n,1]。归一uδ=Mδ/cδ不使任何误差无界。

## 4. 原wholeclock和真正浓集的端点

分布积分得DivMδ=Σw_i v_i[ρδ(x−a_i)−ρδ(x−a_i−v_i)]，L¹≤2。若N条轴且Nδ^n→0，端点邻域体积≤C Nδ^n→0，故归一误差→0inmeasure。一条每δ方向N≲δ^{−(n−1)}足够；若N≤Kδ^{−(n−1)}须另付Kδ→0。若全管邻域体积也→0，uδ→0inmeasure；共同紧支撑放在固定大Lipschitz cube内部，则weak*子列边界质量零，Θ子列存在，Rem1.4–1.5可用，不必缩短物理unitclock迁入unitcube。只有端点稀疏或只有marks小均不足替代wholefield浓集。

## 5. PSD专属后果及其限度

μ支撑PSD单位球。由正Choquet分解，对π几乎所有ν仍支撑此闭集（对其补集用μ=∫νdπ）。B=[ν]为PSD奇异矩阵。选e∈kerB、|e|=1，有0=eᵀBe=∫eᵀAe dν，且被积非负；故Ae=0于ν几乎处处。每组件有共同kernel，因而μ支撑奇异PSD。这里只需逐ν选一个e作论证，不需可测kernel选择。秩亏矩阵的混合可满秩，故不能把总矩阵变奇异；Th1.7的任意生成场也不能自动当作原轴分组。此后果本身没有跨空间点/跨fiber/同clock的联合质量。

## 6. 固定null源的旧DPR闭包排重

设PSD有限矩阵测度S由固定null compact Kakeya载体K的真实线段occupation构成，trS总质量1、DivS为有限端点测度且也载K。则S*ρε和DivS*ρε都→0inmeasure，归一输入合格。近似恒等严格收敛：上界由Jensen，下界由weak*半连续；故cε→|S|，Reshetnyak给实际Θ极限为polar(S)#(|S|/|S|(全域))。旧DPR finite-Div singular-polar定理已给此law支撑Λ。任一单位A∈Λ，取Ae=0，Q内穿中心而非边界面的超平面，u_j(x)=c_j A jψ(j(x·e−s₀))，ψ≥0紧支撑，c_j归一，则Divu_j=0、Θ=δ_A、→0inmeasure，极限为超平面概率测度，无∂Q质量（边界交集低一维）。因此δ_A∈Y_Div；对实际polar law混合这些Dirac组件已给Th1.7式存在分解。只排重这一固定源应用，不否认新定理更广范围。

## 7. 已知加权端点估计直接更强

实际primary CV1205.6371v1 Theorem1允许任意方向、非负权重、d≤n个无限直管族和外积权。取d=n、n份同一原管族，半径Cδ缩放，右侧C_n δ^n W^{n/(n−1)}。Mδ中k_i≤Cδ^{1−n}1_{T_i}，T_i为相应无限Cδ管；端点帽也被包含。Cauchy–Binet精确给detMδ=(1/n!)Σ有序(i₁,…,i_n)∏w_i k_i |det(v_i₁,…,v_i_n)|²。单位方向使det²≤|det|，重复label项为零。因此

∫(detMδ)^{1/(n−1)}dx≤C_n W^{n/(n−1)}。

δ^{−n}与CV右侧δ^n恰消；无限管的单管积分无穷并不妨碍该外积和估计。无方向分离、Wolff、density、Div、浓集或全union小假设。这个具名已知定理的直接应用不是新数学ID。

## 8. 原marks自身的broad质量与两种density

任意可测0≤h_i≤1（例如1_{Y_i}），Mδ^h=Σw_i k_i h_i v_i⊗v_i。它PSD且0≤Mδ^h≤Mδ，故det单调；也可直接在上式逐项以k_i h_i≤k_i估计。对其自身broad集Bε^h={λmin(Mδ^h)≥εtrMδ^h}，ε∈(0,1/n]，得||1_B trMδ^h||_{n/(n−1)}≤C_n ε^{-1}W，任意原E上质量≤C_n ε^{-1}W |E|^{1/n}。不能将marked-broad偷换为whole-broad。

选ρ支撑B(0,3)、在B(0,2)上有正下界。对整个原圆帽δ管，距离某t₀∈[0,1]≤δ，长≳δ的单侧clock区间使距离≤2δ，故k_i≥cδ^{1−n}。因此Y_i⊂原δ管时∫trMδ^{1_Y}≥cδ^{1−n}Σw_i|Y_i|。加权平均density Σw_i|Y_i|≥λΣw_i|T_i^unit|给≥cλW；逐管density则逐项给同式，二者分别成立。合法删管或删marks保不等式的absolute W upper，却未必保原λ；重归一须付所留权重。若|E|≤δ^κ、λ≥δ^{Cη}且Cη<κ/n，broad不能承载全部原质量；只得已知局部hyperplaniness，不补剩余rough分支或ambient出口。

## 9. 为什么shading仍不能免费调用GR

上一节绕过BV而非证明它。wholefield端点仅两个；当时钟mask h∈BV(0,1)时，乘occupation的导数为v[h(0)δ_a−h(1)δ_{a+v}]+沿轴推送v D_t h，此处D_t仅指(0,1)内BV导数且h(0),h(1)取内部trace，内跳项不能省。若用零延拓全轴导数D_t(h1_[0,1])则端点已包含，不再重复列；对一般仅可测h只能按此distribution定义，不能假设BV或端点trace存在。一条轴上m个不交clock区间，occupation的DivTV=2m；平均或逐管密度不控制m。单interval长度λ_j→0，归一总质量1后DivTV=2/λ_j，仍不满足Rem1.5统一L¹。subpower费用也不等统一常数，换A_j=λ_jDiv违反固定算子。小markedfootprint不能让未删wholefield→0inmeasure；合法可测restriction的几何与PDE闭包必须分开。

## 10. 真实wholeclock可有满秩绝对连续弱极限

取已有R91/R94的compact planar null Besicovitch P，K₀=P×[-1,1]³。每v∈S⁴以P内单位段的长度|v_P|子段及cube中的−v_Q/2+tv_Q取得真实五维单位轴；v_P=0另选P点，可测selector按既有闭关系选择论证。P的dimH=2、乘cube后dimH K₀=5；它为Leb-null full-direction集而非strict低维反例。按球面均匀方向测度σ积分构S₀：tr mass1、全局矩阵I/5、DivTV≤2，S₀及端点载K₀。

取大cube C=[−L,L]⁵，K₀⊂[−R,R]⁵、L>R。有限均匀网格平移概率τ_j→1_C dx/|C|，S_j=S₀*τ_j仍由整单位轴组成，每方向总权重σ，有限个null载体平移并、DivTV≤2。逐j后选ε_j<1/j，使载体的3ε_j邻域体积<1/j。故u_j=(S_j*ρε_j)/c_j及Divu_j都→0inmeasure，c_j∈[1/√5,1]、DivL¹≤2√5。共同紧支撑消边界质量；子列c_j→c>0且Θ收敛。weak*极限为S∞/c，S∞=S₀*(1_C/|C|)dx；在commoncore[−L+R,L−R]⁵密度I/(5|C|)，满秩且core散度0。μ的value-polar law依旧由§5约束，空间弱极限却可满秩，两者不矛盾。

此例保真实unitclock、fullangular，不保一个原δ尺度one-per-direction族，也不保证power尺度footprint亏损；ε_j依j对角可任意快。它只否决“GR+wholeclock+全角必迫弱极限奇异/低维”的桥，不证伪Kakeya，不称重大新结果。

## 11. FT一般barrier与varifold输入分开

Firester–Tsiamis2608.31164v2 Prop3.4适用于一般matrix measures，不以varifold粗拒：mass bounded、DivTV→0、carrier m-Leb→0推出limsupΦ≤0。原wholeclock的Div≤2是统一有界，不自动→0；但不能就此粗拒Cor3.5，它已用普通pushforward缩放得到|E|^{1/m}DivTV≥c，只需mass≤L且Φ≥η>0。真正未付是正barrier质量：concave barrier在奇异matrix≤0，秩一/秩亏PSD本来落此域；global isotropic matrix不推出局部Φ正，§10校准也不违反。

Th1.1/4.1另外要求rectifiable m-varifold、finite firstvariation和正投影barrier输入，2≤m<N；线occupation不能免费给它。尝试m-ribbon [0,1]×[-δ,δ]^{m−1}，mass=(2δ)^{m−1}、boundary=2(2δ)^{m−1}+2(m−1)(2δ)^{m−2}，归一后variation/mass~δ^{-1}；MS右侧归一为δ^{(m−1)/m}δ^{-1}=δ^{-1/m}，没有增益。只否该转换，不声所有varifold路径不可能。

同一ambient PSD场的barrier正部还可更强排重。任意源定义的有限concave一次齐次φ在全部matrix空间全局Lipschitz：concave+homogeneous给superadditive，配|φ(Z)|≤L|Z|从两向差商得|φ(X)−φ(Y)|≤L|X−Y|。对PSD M，B=M−λmin(M)I奇异PSD，故φ(B)≤0，φ₊(M)≤L√n λmin(M)≤L√n(detM)^{1/n}。由§7旧CV，||φ₊(Mδ)||_{n/(n−1)}≤C_φ W，任意E上∫φ₊≤C_φ W|E|^{1/n}；Mδ^h亦同。故这一原ambient PSD载体的正barrier有限输出已由旧工具更强覆盖，不需Div。不把此结论扩到任意matrix measures/投影后的未付carrier或声全部FT工具失效。

## 12. 闭包、双向排重与停止

有限原tube PSD后果由更强旧CV直接推出；反向定性GR不含该尺度Lp率，不能等价夸称同一完整外部定理。fixednull实际law的分解由旧DPR+Dirac闭包完全重获；varyingsequence的新scope承认，原geometry有限输出仍已旧覆盖。average/per-tube density与合法restriction各自核过，没有换名新方向或newID。缺原samepoint/跨fiber耦合与完整ordinary/HRZ/stickyrough或strict低维full-direction出口。本直接PSD浓集桥的operator系数、moment阶数、端点/厚度参数续轮停止；新主任务必须带尚未付的新原质量输入。两独立formal及root整合后仅本应用账内部reviewed；Goal active。
