# R0102：原多块质量、rich fibres与闭包独立终审

2026-10-19，B／lifting_obstructions。本文件是root／A证明的独立逐步审查；本人B稿的自证不计独审。实际全文范围如下，结论仅覆盖working锁定的有限δ原配置归约及明确条件投影应用。未经外部同行评审，完整Goal保持active。

## 1. 实际全文对象、版本与审查职责

实际全文读root主稿 `notes/40_multiscale/sticky_matrix/R0102_global_codes_and_rich_fibre_restricted_projections.md` 十二节、A最终 `notes/00_map/R0102_complete_goal_outlets_reselection.md` 十节、本人B最终十节，以及R0102 reselection／working两份各五节spec。A原八节阶段I与锁后第9–10节分开核：前者ordinary／HRZ／DIM资格重选不是新主定理；后者才是本轮原多块码及literal源调用的有限证明。本人B的公式只作为对照，不以自审替独立核root／A。

终 `research/reviews/R0102_macro.md`、`notes/00_map/R0102_next_full_goal_reselection.md`、`literature/notes/R0102_CSWZ_global_code_projection_and_scope.md` 及 `research/rounds/R0102.md` 各六节均已实际全文读。本文不认证这些文件中的未来归档／Git／回执或库存字节检查，只核数学与停止范围。

一手采用库存CSWZ2610.13682v1：本人实际读Def1.4–1.5、Th1.6–1.7完整statement，本次另全文读§3.16的Th1.7推导。已核其bad cell是“存在cell内代表及一个大子集使像小”，并非要求整cell所有参数都坏。WZ原Def17及R76同T原访问／两端码接口沿本轮已记录的实际读域核；mixed原contact的相关段亦读回。没有宣称重证CSWZ45页、WZ或其余高级具名输入的全部wholeproof，没有新PDF或官方整库字节认证。

## 2. 多块原分母、实际code概率及同权层

root§2–4与A§9的计数通过。开始于真实det-large原分支：两锚差h及A的最小奇异值至少σ，实际同T双访问数至少τδ⁻⁴。finite code offset只损固定倍；双侧weighted peeling用原两端点总数≤K^Cδ⁻³选阈值D₀≥L⁻Cδ⁻¹，删边预算相对原τδ⁻⁴收费，而非先把每code块当一份新完整源。固定原两端点时，clock gap给T重数≤Cσ⁻⁴；每个非空配对code块因此至少消耗D₀/(Cσ⁻⁴)个左端点。左codecell归属唯一，各块端点不重复计，故全局非空codecell数≤L^Cδ⁻²。这里保留H₀≥L⁻Cδ⁻⁴原管及其全部旧S_T，没有取最大单块，也没有支付R76最终δ²比例。

对code C(T)=(U,V)=(y+Ax,y+hξ)作ρ球查询，只取U约束即可。每个原native y把x限于半径Cρ/σ的二维球；ρ≥δ时ambient δ-packing给Cσ⁻²(ρ/δ)²。再乘原|Y_t|≤K^Cδ⁻¹及每个used p_t的实际point-pencil degree≤K^Cδ⁻¹，得

\[
\#\{T\in H_0:C(T)\in B_\rho\}\le L^C\rho^2\delta^{-4},
\qquad \mu_0(B_\rho)\le L^C\rho^2.
\]

ρ/σ>1时显示upper只是更宽，fine code中心误差用固定倍球吸收；没有把ξ当正则函数或授q-offset二维lower。除数始终为实际H₀，条件化原T的损失列入L。

按每个codecell中的实际管数w(Q)作O(log1/δ)二幂层，保至少其倒数的原管数，且层内管数在[w,2w)。H保全该层原管、P为不同code中心，uniform P与H的pushforward权在固定倍内可比。因此同一个P满足|P|≤L^Cδ⁻²和2-Frostman upper；取ρ≈δ的原atom upper再给|P|≥L⁻Cδ⁻²。每T的全部S_T仍保留。此处没有从重归一CW免费取得新的Def17 lower，也没有合并重复码后丢失管权。

## 3. 真正第三点恒等式、逐管与平均及rich fibre碰撞

root§5–7／A§9逐项通过。将同一实际T在第三p=(x,y+F_u x,u)的selected ξ_p和原horizontal slope φ代回两端码，确得

\[
C(T)=\Gamma_p+G_u\phi+O(\delta),\quad
G_u=\binom{(t-u)(F_u-F_s)}{(s-u)(F_u-F_t)},
\]

其中Γ两分量分别为y+(F_u−F_s)x+(t−u)ξ_p、y+(F_u−F_t)x+(s−u)ξ_p。两block直接相减恢复A，没有A⁻¹放大fine误差，亦未用独立第三label替换原w。若距两锚至少r，则G₁/(t−u)−G₂/(s−u)=A给smin G_u≥rσ/2。

far删选先逐T做：δ-separated Z在两个r窗共至多C(r/δ+1)点，除原|S_T|≥K⁻C m、m≥K⁻Cδ⁻¹，η≪c时每T保一半。其后才用全原|E|≤K^Cδ⁻⁴取point-heavy阈值D=I_f/(2|E|)≥L⁻Cδ⁻¹，删light p只损I_f/2。此后root／A正确只宣平均，不声每T仍半保。I_u≤|H|和ΣI_u≥I_f/2给|U_rich|≥L⁻C m、各rich u的I_u≥L⁻C|H|。

在heavy p，同codecell迫φ在半径Cδ/(rσ)球；原Φ_p的AD1 upper及每δ角bin的有限T重数给每codecell至多CK^C/(rσ)根实际管。因此该p至少访问R₀≥L⁻Cδ⁻¹个不同P-cells。这里D是真实保留degree，AD只用upper，不向裁切角族赠lower。

固定u时这些affine planes全平行。按q_p=Π_(imG_u)⊥Γ_p的δ-outputcells分组，每组挑一个heavy p即可取得R₀个码点；每P码点仅能邻接固定个q-cells。这是有重叠的双计数，仍得active q-cell数≤C|P|/R₀≤L^Cδ⁻¹。令P_u为该time全部实际heavy visits的码点，w层还给

\[
|P_u|\ge I_u/(2w)\ge L^{-C}|P|,
\qquad |\Pi_{(\operatorname{im}G_u)^\perp}P_u|_\delta\le L^C\delta^{-1}.
\]

这同时保一个共同P和每u的大P_u；P_u、p、native w均可变化，不要求q-law、公共sheet、所有端点pairs或每管同一末clock。该原point-pencil用途确比单块g能量多了完整联合数据。

## 4. Chart、代表、参数重复及literal robust结论

root§8–9／A§10通过。真正projection参数是normal plane(imG_u)⊥，literal π_θ的kernel才是imG_u。固定有限小Grassmann atlas取rich times最多的一chart，费用固定；统一正交变换／平移缩放作用整个P，再按可比δ mesh重格化，每cell仅合并O(1)码点。Frostman、P_u比例和output cover只变固定倍。小chart留θ∈[−1/2,1/2]⁴的margin，不把越界cell当literal参数；π_θ与正交projection的target-isomorphism有统一条件数。cellcorner改变θ时，P有界保证output只移Oδ。

取d=4、output=2、point exponent=2、outputloss=1/4、固定s>0，Th1.7给ε_*。先固定此ε_*，再选本轮a,b,c、η，使全部L^C≤δ⁻ℓ，ℓ<min(ε_*/10,1/10)。则P满足源Frostman，实际P_u≥δ^ε_*|P|，而像cover至多\(\delta^{-1-\ell}<\delta^{-7/4}\)。δ取原dyadic fine mesh，固定缩放／重格化只改常数；没有依赖随δ失控的坐标变换。

Θ_rich只由rich u实际实现的不同参数cells组成，每cell任选一rich代表及其P_u。所有这些cells均为bad。任何非空Θ⊂Θ_rich若有源要求的(δ,s,δ⁻ε_*)_(4,2)-SPREAD，Th1.7便给至少一个good cell，并对同P的所有大子集给像至少\(\delta^{-7/4}\)，与其实际P_u矛盾。完整§3.16正以存在这样的代表／子集定义bad，故此处无未付uniform例外到time的转移。

重复u不计为不同参数，|U_rich|大亦不授|Θ_rich|大。若改用全部原time pushforward的加权SPREAD假设，再限制到rich u或转uniform cells，仍须另付质量、重复cell和restriction常数；本应用没有作该升级。本人阶段I“必须先有time-weighted SPREAD”措辞已在B§6纠正：它是另一条转移路线的warning，不阻本每格皆bad的合法路线。实际证明的是必要nonspread／条件SPREAD排除，未取得源自身SPREAD。

## 5. 原反攻、旧冻结与删选闭包边界

root§10–11和A的对应scope通过。固定far u，graph Z=q(F_u−F_t)(F_u−F_s)⁻¹的逆式为F_u=(Z−qI)⁻¹(ZF_s−qF_t)，左乘次序正确。合适可逆basepoint处它映到Gr(4,2)开chart，故旧R76中R⁶共同point-law的结构零项不能直接移植。这里Z是kernel的下block-over上block graph，交换codeblocks后literal projection参数是−Z；不能混normal／kernel。开chart只检验系数map，不构造原完整T或证明实际time曲线SPREAD。标量仿射F使G两blocks相等、方向恒定，只反自动SPREAD，不是fullsource反例；它未保原SM／全部native／CW／Φ数据。R97特定Segre局部障碍也不能未经map计算套到本新family。

整管code层保全部旧marks；far逐管保量，point-heavy后只保平均；原N/I/m分母始终可追踪。绝对CW upper继承，若重归一为概率要付N/|H|，ADlower不会自动继承。任意g边restriction亦非重新生成完整Def17源。没有将抽象P及可变P_u反向构造成原filledX／ξcoherence／pointΦ／CW，故不声与完整源双向等价。

R44原共同tests、R45接受selected tuples的KBL、R76最终单δ²块及R78–80共同action，都未自动给本轮全局2Fst码集和实际point-rich fibres。旧CP/PM/PW全称gain等价不解冻；本轮不是以新名字要求同一个统一gain，而是对真实新构造family核具名定理的明确分支输入。mixed42／43仍须消费原contact、不同native维数和原τ范围；没有借matrix33结论覆盖它们。

A阶段I完整四路及DIM层级核过：在明列具名输入及已审proof-level finite接口下，17/4六维推论已完成，不应复活旧assembly缺口。外部source核验等级、当前priority／major与数学应用是否完成分开；本审未fresh复查A全部网页或认证其前沿穷尽。

## 6. 必修项、实际范围通过与停止

当前root12／A最终10的上述有限证明、原分母、量词和限定反攻未见未解决的强制修复项，**在本文件明列实际全文范围内通过**。本人B的阶段I加权参数warning已改成本次all-representatives-bad证明兼容的准确范围；graph参数与projection参数的swap／sign、旧拟锁／待交叉历史句已在本人授权稿收尾。这些修订不把必要退化升为全源增益。root／A对B自证的独立实际审查应以其各自文件／记录为准，本文不自计。

终macro／next／source／round实际全文范围亦通过：新信息是全局原多块质量→同一2Fst P→实际rich受限小投影→rich Θ不能含合格small-loss-SPREAD子族。next没有预锁合格gain；若研究nonspread必须另给实际Def1.5失败的子族／尺度及原I量词，不把失败公设化为公共kernel、全局有理F或旧uniform projection gain。停止r／σ／ε调参，旧R101完整witnessbox、BSG/action与R96–97模板冻结不变。

完整rough κ1及其余source分支、SPREAD失败后的恢复、ordinary／HRZ全部费用与一般Hausdorff返回仍未付。本审不宣newID／major／novelty、完整κ1／ordinary saving或Goal完成；CSWZ高级wholeproof继续具名，**未经外部同行评审**。不认证未来metadata、提交、同步或回执；完成指定文件后停止编辑与检索。
