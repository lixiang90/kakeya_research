# R0103：原访问集中profile、native条件与闭包终审

2026-10-19，B／lifting_obstructions。独立主审root／A，本文自身B稿不计独审。仅对实际读取的有限原配置归约、具名定理应用及限定反攻作结论；高级He wholeproof仍具名，未经外部同行评审。

## 1. 实际全文范围及所限原命题

实际全文读root `notes/40_multiscale/sticky_matrix/R0103_original_incidence_Schubert_concentration_and_polynomial_layers.md` 十节，A `notes/00_map/R0103_complete_goal_and_global_projection_reselection.md` 最终十节，本人B最终十节，R0103 reselection／working两份各五节。主稿§7随后新增degree6 plane-law校准及七点Lagrange简证，已实际全文读回；working最终q∈(0,1/4)亦读回。本人B§10当时“A待落”历史状态不作为当前审查状态，现A已实际全文核，按仅formal授权不再改原稿。

当前磁盘macro、next、source、round各六节亦实际全文读：`research/reviews/R0103_macro.md`、`notes/00_map/R0103_next_full_goal_reselection.md`、`literature/notes/R0103_He_global_projection_and_original_mass_scope.md`、`research/rounds/R0103.md`。只核实际数学与停止范围，不认证未来档案计数、Git／sync／receipt。

继承的是完整WZ matrix33 κ1中R102已实际提取的det-large分支，不是任意rough F或全部ordinary族。R102全局多code的同一个P、实际大P_u、small image及原I_u不再当未证假设重做；其原数据身份、同T／point／clock和平均／逐管差别已沿本会话实际全文审查。当前所限结论是带原质量与每簇尺度下界的必要Schubert集中，未得完整κ1排除。

## 2. He输入、任意剩余权与减e单调性

采用[He1710.00795v2](https://arxiv.org/abs/1710.00795v2) Th1；本人实际官方history／PDF1–5的§1.1–1.4声明与说明，未新独证其33页高级主证明。此为投影论文，不是1611矩阵sum-product。原版本日期2018-05-09与正文May10分开，未认证正式47页版字节相同。

root§2–3／A§2–3调用通过。取(n,m,α,q)=(4,2,2,q)，固定q<1/4先取源ε_H，再令e≤min(ε_H,q/4,1/100)。较小e使点数、概率upper和方向cap三项假设更强，所测试P′更大；原输出和good质量也强于降e后的版本，故没有符号倒置。选全部原L费用指数ℓ≪e后，R102的2-Frostman上界给所需q-Frostman，点数≥δ⁻²⁺e；实际P_u比例≥δ^e，而像upper≤δ⁻¹⁻ℓ严格小于源half-plus lowerδ⁻¹⁻e。共同缩放进unit ball、同δ cover／card常数付固定倍，未另加point ADlower。

对任意非空剩余R⊂U，以原I_u归一pushforward到normal G_u⊥。它允许原子及多个u重合同一normal；每个正权支持方向都已有某个实际坏P_u。若对所有W、ρ≥δ满足cap≤δ⁻eρ^q，He会给正质量good方向，对它的所有大P′增长，特别对该方向的实际P_u增长，矛盾。这一步不依uniform不同cells，不把参数例外比例返回time，也不要求不同u的P_u相同。本文没有从原SM／slab／time AD直接证明cap；真正采用的是cap必失败。

## 3. Half剥取、每簇绝对分母与非平凡量

root§4／7及A§5／8通过。令I_U=Σ_U I_u，μ₀(S)=Σ_S I_u/I_U。每个剩余条件概率失败给某cap，且

\[
\delta\le\rho_j<\delta^{e/q},\qquad
\mu_{R_j}(U_j)>\delta^{-e}\rho_j^q\ge\delta^{q-e}.
\]

每次删除的是剩余time labels中该cap的全部元素；clock簇不交而几何caps可重叠。只在剩余原μ₀至少1/2时继续，于是每簇都满足

\[
\mu_0(U_j)>\tfrac12\delta^{-e}\rho_j^q
 \ge\tfrac12\delta^{q-e}.
\tag{1}
\]

累计至多ceil(2δ⁻(q−e))≤3δ⁻q步即保至少I_U/2。最后一簇也是移除前剩余≥half时选出，仍有(1)。有限U无可测选择／极限漏洞；原normal重复权与原point／tube重数并未在剥取中被改成uniform参数。I_U≥L⁻C N m只是原总量的次幂比例，不是固定比例全部原I。

保留逐簇(1)不可省。归一厚度a_j=Cσ⁻⁴ρ_j后，4bq≪e及δ最后小给

\[
\mu_0(U_j)\ge\delta^{-e/2}a_j^q,
\qquad \delta\le a_j\le\delta^{e/(2q)}.
\tag{2}
\]

原rich权有interval upper L^C(l+δ)，故一个a_j-sized普通time窗不付(2)。更强的通用Lip证书可把W取为窗心normal，以product-sine二阶接触得到cap尺度O(L^Cl²)，从而选sqrt(a_j)量级窗；q<1/4仍使其L^Csqrt(a_j)质量远小于(2)。该比较只拒这种通用分窗，不把sqrt(a_j)误当真实cap最长时窗：沿Schubert cycle运行可持续更久。工作范围不使用可被该施工平凡化的q>1/2，也不从层数／厚度本身声新gain。

## 4. Normal公式、formal中点与统一系数lower

root§5–6／A§6–7通过。对W的正交列基B，令P_B(v,F)=det(G(v,F)ᵀB)，v、F是独立formal变量。G的每entry总degree≤2，故P_B总degree≤4、v-degree≤2、F-degree≤2、系数upper固定。实际far u上有准确恒等式

\[
|P_B(u,F_u)|=\sqrt{\det(G_u^TG_u)}
 d_\angle(G_u^\perp,W).
\tag{3}
\]

这里normal为G_u⊥；d∠是principal sines乘积，不是普通Schubert metric距离。bounded G给cap上的|P_B|≤Cρ，不需要额外倒置smin。若反向从多项式sublevel推cap，才有原r／σ条件数；更不能无梯度lower就把sublevel值叫到零集的同量级Euclidean距离。

统一非零性没有从实际time插值。取formal v₀=(t+s)/2，A=F_t−F_s、h=s−t，S(a,b)=(-A⁻¹(a+b),b)，则SG(v₀,F)=(h/2)(I;F−F_t)。||S||≤Cσ⁻¹、||S⁻¹||≤C，故B′=S⁻ᵀB两列的wedge norm≥cσ²。det((I;X)ᵀB′)的六个Plücker minors逐一配对独立基{1,X₁₁,X₁₂,X₂₁,X₂₂,detX}；普通monomial系数norm与这六维系数norm只差固定倍。因此固定v₀后的系数lower为c h²σ²。F_t有界的平移有bounded逆，formal v代入有bounded operator norm，遂得

\[
c\sigma^4\le\|\operatorname{coef}_{v,F}P_B\|_\infty\le C.
\tag{4}
\]

v₀无需在Z，B可随簇／δ变化，所有constants仍统一。归一Q_B真正非零、norm1，并由(3)(4)得a_j；本证明没有将rough F延拓为多项式。Q_B形式非零不排其在实际(u,F_u)上恒零，后者恰是允许的集中。

## 5. 反攻、degree6校准和两密度闭包

A§9及root§7新增段独核通过。取kernel graph T(z)=((z,z²);(z³,z⁵))，其六Plücker functions为1,z,z²,z³,z⁵,z⁶−z⁵，线性独立。任意W的正交B wedge norm1，故det((I;T(z))ᵀB)是degree≤6且系数统一lower的非零polynomial。有界Gram因子只改变sublevel阈值常数。若其小值集长l，从中选七个相隔≥cl的点，degree6 Lagrange插值给sup≤Cρl⁻⁶；系数lower给sup≥c，故l≤Cρ^(1/6)。小值集为固定数intervals，uniform δ-net只多Cδ，ρ≥δ时得到uniform cap≤Cρ^(1/6)。固定q<1/6时这不可能达(1)的异常lower。此反攻只说明任意Lip plane-law不会自动给profile；它不携带R102全部坏P_u或完整Def17，不是source反例。

R79已审rough上三角联合模型则可在同一Schubert cycle内运行：W=span(e₂,e₄)使BᵀG两行的首列为零。它兼顾所列time/NF/nativeg等弱接口，但缺fullT joint4AD/CW、filled-X、pointΦ及ξcoherence，不反完整源。常值／标量仿射F亦只反自动cap。原SM排的是有实际量词的affine fit，不等于任意det-cone非集中；near-Schubert不授公共kernel或全局有理F。

root§8／A§8的真实mass返回通过。U_*为簇union，仅先有总访问J_tot≥I_U/2。每T至多m访问，用阈值J_tot/(2N)或对|H|的相应阈值删light tubes，至多损半总量；保≥L⁻C N根原T且每根≥L⁻C m个旧marks。逐管lower只属于union，不属于每一簇。单簇源restriction要另付固定幂mass、新η／allowed尺度和完整X/Y/Φ资料，不能直接调19.2／19.4。

从平均λ开始的heavy必须同时保I/2与N′≥λN/2，再有逐管λ/2；absolute CW继承而normalized费N/N′。本稿继承R102已经heavy／det-large的原分支，不倒推任何ordinary原族都有它，也不向marks限制授ADlower。与R78单δ²块的共同X/cone相比，本证书的原I分母及逐簇massscale确不同；反向恢复原source／共同X未证，不宣CP/PM双向gain新名称。

## 6. 必修项、有限范围结论与停止

当前root十节、A最终十节及两spec的所限有限链**未见未解决强制修复项，实际全文范围通过**。本审主核root／A，B自身相同推导不自计；A对B独审以其报告为准。q收窄、product-sine与metric区分、sublevel非距离、normal／kernel对偶、绝对μ₀分母及单簇／union逐管边界均已在当前文本保留。

当前macro／next／source／round实际全文scope亦一致：较弱He输入经实际全坏支持得到带尺度mass的必要集中，而非额外假设cap后才推出条件结论；归一多项式非真空，仍未消费完整point-pencil／filled-X／CW以返回ambient saving。next没有预锁成功逆分类，停止q／e／ρ及degree小改，不把集中失败换名为旧uniform gain或补公共kernel／有理F公设。ordinary／HRZ全预算、其余rough及真正full方向strict反例目标仍open；DIM已付推论不重报assembly gap。

高级He33页wholeproof继续具名，本文不认证正式版同一性、全前沿穷尽或future metadata／Git／sync。没有新数学ID、major／novelty、ordinary／完整κ1结果或Goal完成声明，**未经外部同行评审**。指定formal完成后停止编辑与检索。
