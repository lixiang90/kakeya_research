# R0055：全类近threefold的全局投影障碍与真实r-piece账本

2026-10-17，B。已恢复 GOAL/STATE/ROADMAP、registry78状态、R54macro/next与R55spec，实际重读HRZ Def5.2/(29)。本稿未证明或否定全G3；给出保全部本轮模型输入的一个严格**转移步骤反例**，以及合法HRZ局部piece归一证明。只编辑分配文件，不Git/spawn。未经外部同行评审，不作新高维/重大/新颖声明。

## 1. G3原量词、闭包和停止

固定D,C,C₀，Z⊂R⁵是至多D个次数≤D实多项式共同零集，实维数≤3，允许奇点和δ依赖系数。有限整单位轴ℓ_i=a_i+t v_i，|v_i|=1、|t|≤1/2，位于B10∩N_(Cδ)Z。T_i=N_δℓ_i，w_i≥0、W>0，physical S⁴每C₀δ帽原权≤α；可测Y_i⊂T_i、E=∪Y_i、I=Σw_i|Y_i|、λ=I/Σw_i|T_i|>0。G3问∀ε>0有

    |E|≥c_(ε,D,C,C₀) δ^(4+ε) λ³ W/α。            (G3)

具名M3可调用，但原97页wholeproof不在本稿认证。删label/任意缩shading后仍在几何类内；平均λ须按实际I/W重算，整label而不缩Yi才保原逐管下界。一个projection失败不等于(G3)假。若只得一个exact/regular toy的正结果，不算本轮全类成功；本轮止于全类证明、合法反例或明确实质门槛，不续模板参数。

## 2. 光滑degree2三维簇与真实近轴族

A提出product-parabola障碍后，本人独立给出完整有限族与原volume校准。固定小c>0，先取相对源c_tang足够小的固定τ>0，再取L≫(1+C₀)/τ且满足下述帽分离/截面分离的固定下界，最后取足够小δ。令r=√δ、

    Z={(a,b,s,a²,b²):a,b,s∈R}。

它由x₄−x₁²、x₅−x₂²定义，实维数3，两normal独立且uniform regular；D=2已足。令a,b遍[-c,c]中间隔Lr的格，p,q遍[τr,2τr]中间隔Lδ的格。忽略端余格，不影响下述常数量级。设

    A_(a,b)=(a,b,0,a²,b²)，
    v=(p,q,v₃,2ap,2bq)，
    v₃=√[1−(1+4a²)p²−(1+4b²)q²]。

δ充分小时v₃≥3/4、|v|=1；所有ℓ=A+tv在B1内。与图中拥有相同前三坐标的点比较，两个输出残差恰为−t²p²、−t²q²，故整unit轴距Z≤Kτ²δ。取原Y_i=T_i、w_i=1，则λ=1，所有端帽保留，真T_i⊂N_((1+Kτ²)δ)Z。

原方向数为

    N≈(r⁻¹)²(r/δ)²≈δ⁻²。                       (1)

若p或q不同，v的相应坐标差至少Lδ。若p,q相同而a或b不同，则输出坐标差至少2τLδ。明确再要求min{L,2τL}>4C₀，则原方向两两Euclidean距离>2C₀δ，每个半径C₀δ的physical帽至多一条，故α=1可取。所有v却在e₃的Kτr帽中。τ、L固定后这些计数/系数常数都不依δ。

这不是近图缺少regularity的病态例子：允许固定降低τ，使HRZ固定macroscale r₀=3/4的切向角也成立。对z∈Z距T_i中某点≤8δ，normal与v的内积分别为2ap−2z₁p、2bq−2z₂q，绝对值≤K(τ²δ+τδ^(3/2))。两个normal正交且长度≥1，故相应角≤Kτ²δ+o(δ)。先选τ相对c_tang固定足够小即≤c_tangδ/r₀。中点恰在Z∩B_r₀，且全T在B_r₀内。故它也可属于源Def5.2的合法宏观局部切向类；不声称它必是某个全局HRZ运行的selected leaf。

## 3. 原union并未反G3：体积恰为δ²量级

上界：bounded域内T_i点均满足|x₄−x₁²|、|x₅−x₂²|≤Kδ。固定前三坐标的二维输出纤维面积≤Kδ²，故|E|≤Kδ²。

下界亦可直接核，不依赖(G3)。取x₃=s∈[1/8,1/4]，每轴与该hyperplane交于

    (a+s p/v₃, b+s q/v₃, s,
     a²+2as p/v₃, b²+2bs q/v₃)。                  (2)

原axis参数t=s/v₃在原段内部。固定a,b时，映射(p,q)↦(p/v₃,q/v₃)有uniform Lipschitz逆：若(X,Y)=(p/v₃,q/v₃)，则

    (p,q)=(X,Y)/√[1+(1+4a²)X²+(1+4b²)Y²]。

在当前小box其Lip常数固定，所以不同(p,q)在(2)的前两坐标相隔≥cLδ。不同(a,b)的格距Lr，而同包位移至多Kτr；取L大后不同包的这些坐标也相隔≫δ。因此在每个上述s-slice，N个中心周围的固定cδ四维球两两不交，且都在各自真实tube内（中心处于unit轴内部）。截面体积≥cNδ⁴≈δ²，积分固定s区间给

    cδ²≤|E|≤Cδ²。                               (3)

G3右边在本族为δ^(4+ε)N≈δ^(2+ε)，所以(3)与其相容。这是新bridge反例，不是G3反例，更不是满S⁴方向的Kakeya反例。

## 4. 严格否global有限投影保原角权

令π:R⁵→R³为任意正交投影，并假设所保方向的投影长度≥c₀>0，c₀固定。由于所有v距e₃≤Kr，若有一个保留方向则|πe₃|≥c₀/2（小δ）；归一后的所有投影方向都在S²一个K_c₀r帽内。该帽只需

    K_c₀(r/δ)²≤K_c₀δ⁻¹                          (4)

个δ帽覆盖。因此若某global group用此π，并要求每projected δ帽的原权≤Aα，该group的总原权≤K_c₀Aαδ⁻¹。

即使π可依δ或group变化，给J个global groups、任意原shading限制/重复分配，只要各group仍以原label权计帽、投影轴不短，则总可承载incidence至多

    K_c₀ J A α δ⁻¹·|T_i|≤K_c₀JAδ³。

原I=N|T_i|≈δ²，所以可保的原incidence比例至多

    K_c₀JAδ。                                   (5)

J,A固定不能保常数质量；即便J,A≤δ⁻η，也不能对任意小η保≥δ^η质量（η<1/3时(5)为更小量）。这是满足原D、真实whole-unit axes、α、W、λ和union全部输入的反例，严格排除了“先取固定有限global线性投影组，每组uniform原cap，再直接M3”的具体证明路径。

它不否允许许多**空间packets**且有实际overlap预算的方案。该族在(a,b)的r格已有≈δ⁻¹个分离空间包；包内的2D方向可投影，空间体积同时支付数量。也不否允许短投影轴但显式付平均/纤维费用的另一方案。不能由(5)升级成所有联合space-direction transfer不可能，或由exact方向的低维信息恢复被否的global gate。事实上本Z的exact contained方向只有±e₃，而真实near方向数却为δ⁻²。

## 5. HRZ原r-piece：轴端点、球边和实际shading可完整处理

本节独立给出几何接口，条件只有源Def5.2导出的(29)：T∩B(x₀,2r)⊂N_(4δ)Z，0<δ≤r/16≤1/16。Z为原TCI；若维数≤3且format≤D，经下述affine仍属G3类。这里不把未证G3加入结论。

原axis参数I₀=[−1/2,1/2]。对y∈Y_i∩B(x₀,r)，取到原segment的最近点a_i+t(y)v_i；t(y)连续，距离≤δ，故参数在

    S_i={t∈I₀:|a_i+t v_i−x₀|≤r+δ}。

S_i是区间、长度≤2(r+δ)。用长度r/8的参数格划I₀（端部允许更短格）：各格左闭右开，唯最后一格还包含原参数右端点+1/2，构成整个闭I₀的真正不交分区。原round右端帽有正体积可映到+1/2，不能把这一参数单点当可忽略零测。对每个与S_i相交的格C取原I₀内长ℓ=r/4、包含C的区间J_C。这总能向原端点内侧clamp实现，段数≤20。J_C内任一点距C∩S_i的某点至多ℓ，故全轴段在B_(r+δ+ℓ)(x₀)⊂B(x₀,2r)，由(29)距Z≤4δ。**没有向原单位轴外延长。**

令Y_(i,C)为Y_i∩B_r中t(y)落在该半开格的部分。它们可测、无损分区原localshading；每点距所assign的真实子axis≤δ，所以Y_(i,C)⊂N_δ(axis J_C)。新piece端帽可以超出原T，但没有新增shading：所有实际Y_(i,C)仍是原点。每label至多20次；全局跨许多HRZ父球的重复不在这一个球的常数内，仍须另计。

取F(x)=(x−x₀)/ℓ，子axis变unit、h=δ/ℓ=4δ/r，空间在B8，变换Z的方程数、degree和实维数不变，系数可变正合G3格式。原localincidence I_B变为I′=ℓ⁻⁵I_B。令W_B是原local族总权（允许含零localshading标签），则W′≤20W_B；令α_h为原族physical h帽的**实际**总权上界，新piece帽权≤20α_h。isotropic缩放不改physical方向，没有设α_h=1。

## 6. 条件G3的局部账本及未付原质量

若G3未来成立，把它用于§5的真实新输入并乘回ℓ⁵，可得等价局部形式

    |E_B|≥c_ε δ^(4+ε) r^(1−ε)
               λ_loc³ W_B/α_h，
    λ_loc:=I_B/(r δ⁴ W_B)，                       (6)

固定形状常数可并入λ_loc，且λ_loc≤K。证明可直接用incidence形式：G3给h^(ε−8)I′³/(α′W′²)，再用W′≤20W_B、α′≤20α_h、I′=ℓ⁻⁵I_B及ℓ≈r，即cδ^(ε−8)r^(−2−ε)I_B³/(α_hW_B²)。这只是未证G3的合法尺度推论，不宣(6)无条件成立。

仅原δ帽界会允许α_h≤Kα_δ(h/δ)⁴≈Kα_δr⁻⁴，不能免费当subpower。原whole-broad/计数支配不提供I_B的大下界；原shadings可能完全避开所选球。跨父球/层的entry与clock重复也未支付。特别k=4、m=3的broad由源Lemma5.3已vanish，(6)不是k4 tiny终点的自动改良。R48的原marks/方向反校准及R49的general→sticky提取缺口保持。

## 7. 对全类转移门槛的精确结论

本轮可确证的新增负信息是(5)：有限global投影/小原cap损失并不足，甚至对fixed degree2、uniform regular的合法near-三维族也必损固定正幂质量。Z的正常二维纤维体积本身良好，所以不能只修normal graph；必须将方向变化与实际空间packets/重叠、原I/W共同支付。把Z换成exact含线或假方向2D图，是删掉了本族真实输入。

但当前没有反G3的合法数据，也没有全类space-direction packet定理。§§2–4不是再证明一个canonical正例充当主目标，§§5–6也不将条件尺度账本当G3证明。不能附加所缺packet公设然后记全类成功。不新增数学ID/高维界/major，G3保持未证未否；一轮已定位实质门槛后，应按spec宏观转出，不续normal/degree/selector阈值或冻结的共同因子模板。

## 8. 全文独审与归档责任

root/A须独立核族数/真实方向cap、cross-section下界、(5)的原incidence及§5原端点cover；本稿自审不算独审。B正式review须实际读最终root/A/macro/next后再写。具名M3及其它wholeproof层次保持；本轮源(29)只用于明列局部几何，不认证HRZ全部递归。长期Goal仍active，普通一般n≥5和重大中间结果完成标准均未达到。
