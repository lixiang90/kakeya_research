# R0065：有理曲率、原输出质量与物理尺度正式审查

2026-10-18，A。仅assigned A稿及本review，不操作Git、不修改root／B或元数据。修后有限命题与条件source接口通过；未经外部同行评审，不认证首创、重大性或普通高维Kakeya结论。

## 1. 实际全文阅读与审查对象

已fresh实际全文读root《R0065_rational_two_time_curvature_and_output_incidence》14节、A《R0065_rational_curvature_source_audit》10节、B《R0065_rational_curvature_counteraudit》9节、working_spec5节、最终macro6节与next《R0065_next_periodic_full_goal_review》6节。另实读Tao网页scope3节，核实际原作者网页Theorem1／Corollary2；source接口对照R16 original_tuple §§2–6、source_linewise_application §§1–3与finite vector命题，以及R58量词边界。

A参与finite推导和fine-source接口，不能将本稿对A的重读计作独立自审；B已独立逐式核这些部分。本人独立核root／B的ν-smearing、二维sublevel、regular复fiber及双曲线因式／critical参数校准，并实际核最终拼接和宏观范围。没有以“3D／4D已证明”代任何此处finite输入。

## 2. 定理、代数格式和三项指数

固定degree／coefficients／denominator lower的两个有理chart、原概率σ×ν1×ν2×π及任意相关0≤g≤1均保留。单F为两chart相同的special case，R64不同branch没有被错误拼成一个全域P/Q。T的两个导数分母分别Q1²Q2、Q1Q2²，N time degree≤6D，故d=6D+4安全；ψ只homogeneous quadratic，所有相关导数bound由固定D、M控制。

角小值集经实对称对角化：半定用最大eigenvalue，异号用两个linear factors，至多两条宽C√u的slab，不要求二次型满秩。取指定time coefficient阈值后，角删除≤CKr^(θγ/2)，其width≥r恰在原floor范围。原ψ重复labels和原差权未丢。

一元Lagrange节点可从measure-e的小值集中以互距ce选出，给coefficient≤Cεe^(−d)。root的两次Fubini／插值给二维coefficient≤Cεe^(−2d)，B的系数切片法同样给sublevel指数1/(2d)。角good时N-coefficient≥r^(2θ)，时间threshold r^(3θ)，故第二项确为CK²r^(θ/(2d))。这不只依“Jac非零”或定性rank。

## 3. 原离散质量、smearing与good-J换元

νi与Uniform[−r,r]卷积后的density≤3K/2，是原interval cap连r-floor的直接结果；允许atoms及重复time labels。原坏事件的全部jitter落入增厚小值集，故原事件概率由新product-density上界比较，原g未被假设独立。bounded rational模型只在其固定小扩展计算；原source f没有被授smooth延拓。θ<1/6保证Cr≪r^(3θ)，可同时支付bad-N增厚与good-N保持threshold一半；r不小时固定常数吸收trivial界。

清分母后target方程degree≤2D+1。每个J≠0的real解，其complex Jacobian亦非零，故确是复零维解；即使另有共同curve，regular preimages仍≤(2D+1)²。inverse-function局部charts／面积公式因此给good部分小球原概率≤CK²r^(2−3θ)。没有声全fiber有限、全局单射，或直接以Jac积分推union体积。

对每个原y平移Aplus的有限r-cover，面积只由绝对N_r(Aplus)≤Kr^(−2+κ)控制，求和得第三项CK³r^(κ−3θ)。再积分任意σ、π即原m上界；不需σ的density或Aminus的cardinality。h先选小、η后选的次序可使三项均o(r^h)。三项指数、K幂和floor均无遗漏。

## 4. R16真实fine图、绝对cover与尺度

原R16已有good q、used H、good τ-window及原L-tuples最大fiber upper所给bounded graph；本轮没有把原tuple重数免费抹掉。直接用fine σ=Uniform(A_f^−)、ν=Uniform(Z_q)、π=原H×H有序差标签即可。#Z_q≥K⁻¹ρ/δ与δ-grid给K(|I|+δ/ρ)，r=ρ且ρ≥δ^(1/4)保证δ/ρ≤r；H的slab floor为ρ。因本定理不需r-separated ν或输入AD，确实无需再制造coarse代表times。

输出绝对cover不能只由Aplus／Aminus比推出。full Y在τρ-separated中心的小balls给AD lower，所有balls在C′Q内再以full Y于τ的AD upper控制，得N_(τρ)(A_f^+)≤K^Cρ^(−2+κ)。τρ≥δ、κ=2也合法。使用完整Y周围点，未给裁切集合重新赋AD lower；近重复grain标签的K费用保留。

规范F=(ρ/τ)(f−f_ref)、time=(z−z0)/ρ、y单位τ；原误差(τρ+δ)/τ=O(ρ)=O(r)。有理模型的值误差O(r)可保原输出关系，只增固定C0；物理误差须ρe_phys/τ≤Cr，即r=ρ时e_phys≤Cτ。没有把粗r^a误差当r。模型的fixed D／M／denominator及N-coefficient lower均仍是额外未提取输入；值近似也不自动传任何导数／Jacobian下界。

## 5. 独立反攻、旧闭包与primary范围

独立微分B的cross模型T=X(1,−1/(uv))，所得J与N因式恒等式正确。N中p²项的最高u次幂为2c²u⁵v，代u=2t+3、v=2s给[t⁵s]N=128c²p²=2p²；另在ψ=e2、t=−3/4、s=3/4核得J=−1/8。两branch各质量1/2，restriction／归一只固定费，所以R64 cross g的低维A-output补全确被本定理排除，而非靠raw det差的分类。

B的真H−H三角density在所选角盒有正lower，q近up/v的宽r带给raw零点ball质量≳r；commonkernel抛物线则J=4(t−s)^3(e·ψ)²、raw零点ball质量≳√r。二者都严格禁止whole raw law的uniform 2-Frostman升级，却不反已收费good-J估计。pencil／common-image的J恒零，属于R16而不满足本轮曲率前提；R58 plateau复杂度随r增长，也不被fixed-format命题覆盖。angle零线及time大atom必须付原K，不能作为违规反例。

实际读取作者一手说明[Terence Tao, Bezout’s inequality, 2011-03-23](https://terrytao.wordpress.com/2011/03/23/bezouts-inequality/)的Theorem1／Corollary2及共同因子处理，匹配复平面零维部分的degree乘积界；未依赖其高维推广，也未将任意real isolated component冒成complex零维。其具名经典结论与标准局部换元是数学输入；WZ高级wholeproof和标量Th13.5未在本轮新独证，本曲率finite证明本身亦不调用Th13.5。

## 6. 必修项、最终范围与停止

fresh最终全文未见强制数学修改。任意dominated g／shading删选保原未归一上界；另条件化time／angle必须按原保留质量重付K，不能声AD lower或逐管density自动闭包。该条件proper-subclass结论不反向赋予所有source有理化／定量曲率，不是普通Kakeya正幂gain的已付全类机制。

最终macro／next忠实记录本轮已付及未付，R66先周期宏观复核完整目标后再锁真正完整责任；不续D／M／θ／h、critical阈值、fixed-degree推广或旧pencil误差微调。53PDF／54sources中的新增项是Tao作者网页、未新PDF，此处只核范围不预认证后续metadata／Git。无新数学ID、major／首创或ordinary高维界声明，未经外部同行评审；Goal active。正式审查完成后停止编辑／检索，由root统一归档。
