# R0018：原 W 质量接口与 entropy gate 的独立审查

2026-10-17，lifting_obstructions。已完整审查 `R0018_W_mass_extraction.md` 与 `R0018_entropy_inverse_gate.md`，并对照 Hochman arXiv1503.09043v2 Theorem2.8、Definitions2.1/2.3及 WZ原(148)–(152)。限定结论通过：原 W提取的有界图与边缘费用正确，entropy输入的前提及反例边界正确；没有证明 small independent convolution、公共二维plane或原矩阵affine结论。

## 1. 原 W计数与边际

R=Σd_T²及Σ_pB_p=R给两边路径的平均lower；再按(p,z′,z″,terminalρ-direction)签名平方，得到 #W≈K^(±1)eF_Wm²，其中F_W=δ⁻⁴κρ^κ。原q coherence控制所需terminal direction数，既不需每管都有m个marks，也不需局部每grain填满。

固定原第一终端点恢复路径时，三个自由fine管各付δ⁻κ，最后ρ-close管付(ρ/δ)^κ，两时间付m²，合并正是KF_Wm²。固定初始(p,T₁)则少一个δ⁻κ，得到Kδ^κF_Wm²。这些upper足以支付辅助H轻方向删除及后续endpoint修剪，方向与终端law的支配没有从无权support大小猜出。

厚y-bucket每桶原点数 upper为K(ρ/δ)²(σ/δ)^α，占用桶数upper为Km(ρ/σ)^α。删除light buckets时，两量相乘与good-q的e可比；再用固定endpoint的W upper，所删路径质量确实可由K大幂门槛压小。按剩余桶原e_Q加权平均得到局部density，而非免费保全局路径比例。

稿中明确保留的全局成本

    W_Q/#W≥K⁻¹/[m(ρ/σ)^α]

正确。这个比例一般是固定幂，不能称单桶保全局K⁻¹质量。κ<2时再选精确grain通常还要付(δ/σ)^α；σ=ρ²≥δ^(1/2)给固定正幂成本。该段是现有计数能保证什么的界限，不是完整source反例。

## 2. joint supports、恢复表与原product frame

σ=ρ²属于精确allowed grid时，固定x-σcell、同一y-bucket与同一z*只遇O(1)个物理σ-cubes；每个cube内ξ coherence给一个O(σ)盒。因此每x-cell的joint cell数有固定upper，max fine fibre为K(σ/δ)^(4−κ)。结合桶总质量lower，确得输入coarse数≥K⁻¹(ρ/σ)²，输出upper≤K(ρ/σ)²与K次cardinal比。

这里得到的是coarse joint support及每x-cell的有限多重性；不应额外解释为所有实际点已经落一个全局唯一值的光滑χ图。稿中没有作这种声明，也没有赋予任意clipped patch ADlower。

固定joint code恢复W的管选择乘积为

    δ⁻κ(ρ/δ)^(3κ)=δ⁻⁴κρ^(3κ)=F_Wρ^(2κ).

乘第一终端fine fibre即得M_code。用原W_Q除以这个真正max fibre后，0≤g≤1及Σg≥K⁻¹#A_c⁻m²#H²均成立。原correlations保留在g内；uniform A_c⁻×Z_q²×H²是已证明的dominating参考计数，而非声称实际路径端点和方向独立。

raw同p方向pair law与uniform H²的区别也正确。固定(p,T₁,T₂)后扩展upper为Kδ^(2κ)F_Wm²，给全W的raw pair domination；条件于具体桶后，现有保证另付Km(ρ/σ)^α，不能写成无损同prior。使用H² frame则由逐codeupper另行证明，逻辑不依赖该raw条件化捷径。

## 3. 原关系、support R与直接fine-time非集中

原(151)/(152)加coarse direction误差，归一化后给(12)的实际4×2矩阵作用式及O(r)误差，r=ρ。横坐标除ρ，ξ减共同ξ_q再除ρ，M也除ρ；完整allowed J上的f variation≤Cρ，所以这些support与coefficients都被一个固定盒控制。此frame已支付 Hochman Theorem2.8 的固定R前提，不应重复虚构一个δ⁻O(η)的未付support gate。

source scale未精确匹配时，稿中要求保O(Kr)或另补分辨率，边界正确。fine times的normalized spacing是δ/ρ，不能仅由cardinal把它们说成r-separated。

不过本代理(1+γ)增量lemma只需时间概率对长度≥r的interval upper，不需r-separation。m≥K⁻¹ρ/δ及原δ-separation直接给normalized fine interval质量≤Kw，因为ρw≥ρ²≫δ。与H²差law、bounded quotient g结合，令η足够小使全部K次损失≤r⁻ʰ（尤其η≪μh），即可直接得到所选局部桶的非集中结论。所保一半是W_Q，不是全原W。

## 4. Hochman输入的范围正确

Hochman v2 Theorem2.8确实要求固定R、ε、m，先得δ_ent(ε,R,m)，再取足够大n；small growth前提是两个独立概率的卷积entropy。其结论在共同随机level i上，对独立抽样的两个components，分别有μ的V_i-saturation与ν的V_i-concentration。V_i不依该level的component locations，但可随i变。

Definition2.1的concentration允许V的affine translate；Definition2.3的saturation是normalized H_m(θ)≥H_m(π_(V⊥)θ)+dimV−ε。它不是θ自身集中在V上，也不决定dimV_i=2或global平面。根稿准确区分了这几项。

查看§4.6证明接口不等于本项目独立重证Theorem4.12；根稿保留这一阅读范围。Theorem2.14的C¹映射和product输入不能无检查套到scale-dependent source f与受限路径图，范围判断正确。

## 5. 两平面捷径反例及entropy数值

根稿模型输入与输出是两个水平域分离的二维Lipschitz图，increment law水平为二维uniform square。匹配plane标签的g有constant density，所有相关sum落在两个二维output graphs内。

独立卷积的两个same-plane分支各有2n+O(1) entropy；cross分支由(x,u)到(x+u,u)或(x+u,x)的固定可逆映射给4n+O(1)。四个component平均为3n+O(1)，mixture entropy与此平均只差[0,log₂4]；相对输入的normalized增量为1+O(1/n)，不能成为O(h)的小增长。标签在零点的重合只涉及可删的零尺度质量，不改变这些估计。

本代理主稿又把相同现象实现为实际matrix-time作用：F在两个time intervals上分别取−bL_i，g只匹配同一world的端点与时间对。κ=2的full prior给相同精确系数3；固定κ=1/2的Cantor H×H prior给至少5/8 log(1/r)的entropy缺陷。两种模型都因固定大affine pieces而违反SM，所以只否定自动global marginal独立化，不否定joint主命题或完整source。

正确付代价的BSG或matching-world提取仍可能在这些模型上选择一个plane；反例没有排除它。真正缺项是这种提取后如何保原time/direction law，并恢复足够同一B上的all-real matrix fit。

## 6. 终稿结论与停止

实际W的joint quotient、endpoint domination、H frame及本轮(1+γ)增量upper是已明确的新接口/有限估计；它们没有建立small independent convolution，也没有推出共同平面、affine f或κ改善。根稿据此冻结无新输入的局部W/BSG/common-plane循环，未把这一冻结说成主命题已证伪，范围正确。

该审查不开展下一mixed分支，不改变最终一般Kakeya Goal。主Mat(2,2)任务、其他mixed cases、一般到sticky和Hausdorff步骤继续open；无新Kakeya维数界或已确认重大中间结果。
