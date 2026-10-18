# R0097：原scalar投影的真实质量与局部Segre输入门

2026-10-19，A。按本轮reselection/working两份五节规格，仅编辑本稿。主结论是精确finite输入障碍及正面质量转移的范围，不是完整mixed42反例或ordinary增益；未经外部同行评审。

## 1. 实际来源、原量词及定理强度

实际全文读R97两spec、当前STATE及R96 next；GOAL/ROADMAP/registry78与R96已审主链按本会话未改范围复用。实际读CSWZ2610.13682v1的引言、Def1.4–1.5、Th1.2/1.6/1.7及所需big-cell说明；已读R14 primary audit及R76 B10的固定Schubert证明作排重。原WZ Def3.6–3.9及普通/标准dyadic管替换说明本轮实际读回，Def17两grain/Φ范围沿R96实际读取复用。fresh[官方abs/history](https://arxiv.org/abs/2610.13682)仍仅v1，2026-10-09；使用库存原件，没有下载或重证其45页高级wholeproof。

保持完整bounded WZ mixed42 d5/k4/ell2，0<κ<1及γ固定，η最后小、δ最后小；原T/N/joint4AD/whole-CW、原Z/两grains/Φ/ξ/coherence均不改。记K=Cδ^-Cη。λ=(a,b)∈R4×R4，native F_tλ=a4−β_t·a_H−tβ_t·b_H+t b4，scalar native Ỹ_t的δ-cover≤Kδ^(-1+κ)。

重排λ为x=a4、y=(a_H,b_H,b4)∈R7，即F_tλ=x+θ_t·y，

    θ_t=(-β_t,-tβ_t,t)∈[-1,1]^7。

CSWZ Th1.7取ambient d=8、kernel k=7、output d−k=1；参数spread-out的下标是(8,1)，不是(8,7)。对point exponent t_P≤1，它给除δε比例参数外、所有≥δε比例point子集的输出≥δ^(τ−t_P)，τ>0任取。Th1.6也有逐point原shading的near-full lower。故源输出不是只half-plus，强度本身足够；真正必须核的是Def1.5的local模型条件。

## 2. 每个原time的actual point–angle供给与管碰撞

固定t∈Z。第一套global ℓ2 grain有global Y_t^g维3−κ，每个scalar horizontal X_(y,t)有≥K^-1δ^-1个细格；bounded shear和原E的δ分离给

    #E_t≥K^-Cδ^(-4+κ)。

每p∈E_t的原scalar Φ_p为κ-AD，故有≥K^-1δ^-κ个细角。对各(p,φ)取原Def17.2(4)的真实witness tube，记所有这些原管为T_t。映射(p,φ)到T的碰撞固定有界：bounded graph-direction chart使一根δ管在固定time截面直径Oδ，只遇O(1)个原δ-separated points；给定p/T，其第一graph slope固定，φ只可在Oδ区间内，遇O(1)个原分离角。角误差和边界用固定着色处理，不损δ幂。因此

    #T_t≥K^-Cδ^-4≥K^-C N； t∈Z。                 (1)

最后一步用bounded全T的原N≤Kδ^-4，不以used族重置N。所有T_t都是真在t有原p/Φ见证的管，F_tλ_T∈N_CδỸ_t；没有将任意通过某个native plane的ambient参数当原管。式(1)比只平均访问强，但只在每层分别保证原管质量，不能取各T_t的大交集。积分确给平均访问≥K^-Cδ^-1；若走逐管路径，仍须heavy化，之后保各管全部旧visits，不能免费改为独立clock。

## 3. 原joint参数到finite point格及Th1.7的条件用途

在bounded原joint chart把λ按可比δ网格round，得到P；取P_t为有至少一根T_t命中的参数cells。原joint4AD和N≈_Kδ^-4使每δ-cell的管重数至多K^C，因此#P≥K^-C N、#P_t≥K^-C N≥K^-C#P。即使一个cell在不同时刻由不同原管见证，也只用了这些参数间Oδ近似；每个t的scalar输出仍在原N_CδỸ_t。这里不将格点视为新完整source或授其same-T访问下界。

对δ≤r≤1，原joint upper和原分母给UniformP(B_r)≤K^Cr⁴，因而也≤K^Cr^(t_P)，取

    t_P=1−κ/4∈(0,1)。

用固定平移/共同homothety将P置[0,1]^8只改变δ常数和各θ的target baseline；native标签card upper不变。θ_t的最后坐标为t，原δ-separated Z使一个参数δ-cell至多接O(1)个times，故#Θ≈#Z。无需β Lip便可对θ参数及p分别round：两者bounded，πθ(p)只损Oδ。

现在仅作合法的条件检验：若Θ满足Th1.7所需(δ,b,δ^-ε)_(8,1) spread-out，ε由固定b,t_P,τ给定，取原η足小使P是(δ,t_P,δ^-ε)-Frostman，且每P_t比例≥δε。定理删去δε比例参数后，仍有实际t的参数cell保留；每个参数cell只合固定个原times。对该t的实际P_t用robust结论，得到

    N_δ(π_(θ_t)P_t)≥δ^(-1+κ/4+τ)。

另一方面原见证与bounded误差给≤K^Cδ^(-1+κ)。τ<κ/4、原η最后小便矛盾。若定理写lower-left参数，actual θ_t在同一格的误差由固定邻格cover吸收。此正转移完整保原point质量/标签upper，没有给条件角独立性；下文证明其small-loss参数hyp不能成立，不把上述条件结论登记为新的源gain。

## 4. Th1.6的逐point shading入口也不免费

Th1.6取hyperplane dimension7和ambient8，point exponentt_P≤d−k=1。kernel plane kerπθ在坐标(y,x)下为Graph(−θ^T)，故参数是R^(7×1)，与Th1.7的R^(1×7)经固定transpose/符号对应。两边的model hyperplanes都恰是参数R7中的所有affine hyperplanes；不能交换kernel/output维数后误称几何假设不同。

原二部图{(p,t):p∈P_t}由(1)有总边≥K^-C#P·δ^-1，每点degree≤Cδ^-1。先point-heavy可保≥K^-C#P点，各带≥K^-Cδ^-1个原time cells；将每点选到同M、M≈K^-Cδ^-1，原Frostman upper只损K固定幂。对每点的这些actual parameters取其通过该格点的kernel hyperplanes，offset在N_CδỸ_t。真实affine-plane总cover至多

    #Z·max_t N_δ(Ỹ_t)≤K^Cδ^(-2+κ)。

如果每点shading另满足Def1.5，Th1.6会给≥δ^(τ−t_P)M，与上式同样有κ gap。这里有限plane总upper计的是(θ,offset)，两者都保原δ误差，不是只数方向。每point time子选不自动spread-out；第5–7节对任一非空子选证明相同local障碍，因此Th1.6不是绕过它的另一入口。平均访问、逐point长参与和逐tube长参与是三种不同分母，本文未混用。

## 5. 精确Segre关系与局部model超平面

写参数z=(u,v,w)∈R3×R3×R，Σ={v=wu}。原θ_t=(-β_t,-tβ_t,t)全部在Σ，无需任何β regularity。对i=1,2,3设Q_i(z)=v_i−wu_i。在任意z_0∈Σ，

    g_i=∇Q_i(z_0)=(-w_0 e_i,e_i,-u_(0,i))， ||g_i||≥1，
    H_i(z_0)={z:g_i·(z−z_0)=0}。

对z,z_0∈Σ，直接展开而非只引用Taylor得

    g_i·(z−z_0)=(w−w_0)(u_i−u_(0,i))。

故dist(z,H_i(z_0))≤|z−z_0|²/2。H_i在m1参数big cell中确为model hyperplane：source H[x,y,c]={θ:xθy=c}中x为非零scalar、y可为任意R7非零normal，所以每个affine H都合法。法向norm下界来自v_i系数1，不含β导数、时间gap或小singular值。

这些H_i随basepoint改变；Σ一般不在某个固定全局affine H中。该局部关系因而不同于R14/R76的全参数固定H精确包含，也不依赖原参数曲线平滑。

## 6. 实际δ-cells的误差及strict singular范围

令𝒥⊂D_δ(Σ)非空，𝒥′⊂𝒥非空，source把家族视作其cubes的union。任取θ∈∪𝒥′，在其cube选z_0∈Σ，|θ−z_0|≤√7δ。若ω∈(∪𝒥′)∩B(θ,r)，在其cube选z∈Σ，则|ω−z|≤√7δ且|z−z_0|≤r+2√7δ。第5节与distance的1-Lipschitz性给

    dist(ω,H_i(z_0))≤C(r²+δ)； δ≤r≤1。            (2)

取固定spread参数b∈(0,1]。可选仅依dimension的A≫1、c≪1，使

    Aδ/b≤r≤cb  ⇒  C(r²+δ)<b r。                      (3)

例如分别令Cr²≤br/4、Cδ≤br/4，余常数给strict裕量。source允许H依θ/r选择；本证实际对固定θ用同一H已够。无需Θ′有任何正质量、分离维数、Lip图或稠密性。空家族不在Def1.5非空输入中，不作无意义除法。

原δ rounding/可比dyadic尺度只把C和A改固定倍；若参数精度扩大K^Cδ则须把δ换实际精度重新数尺度，不能假细网误差仍为Oδ。原source本次θ与point都bounded，固定倍邻格已经足够，不需此K级放大。

## 7. 奇异尺度总数与ε的真实边界

对固定b和足小δ，(3)中dyadic尺度至少

    s_δ≥log_2(1/δ)−2log_2(1/b)−C_0。                 (4)

因此每个θ∈∪𝒥′都有至少s_δ个b-singular scales。若𝒥满足(δ,b,C_spread)_(8,1) spread-out，取𝒥′=𝒥，Def1.5直接迫

    1≤C_spread 2^(-b s_δ)，qquad
    C_spread≥c_b δ^-b。                              (5)

任一非空subselection当作自己的新家族时，取其自身全子族，仍有同一lower；因此删坏times、删每point shading或权层均不能除去这段local singular性。这个结论只需参数支撑，不依原图质量，也不凭原Φ/Y ADlower。

严格限定：(5)排固定b与C_spread=δ^-ε、ε<b的small-loss输入。ε=b或ε>b不能单由该不等式排除。不能以‘定理的ε还可缩小’代替对较大ε调用的反证；本文未证明所有数值参数版本或所有projection结论无效。若另允许b随δ趋零，也不在此固定b结论中，不能免费沿用Th1.7的ε/δ_0。本轮不优化这些边界。

## 8. 强global hyperplane cap仍不救local条件

用β=(t²,t⁴,t⁶)、t为[-1,1]等距δ网作参数law校准。θ的七坐标是monomials t,…,t⁷的fixed signed permutation；原V再含常数1，所以full span8且8-jet determinant非零。任意affine H的单位normal ℓ给P_H(t)=ℓ·θ_t+c，一个degree≤7多项式，其非constant系数norm为1，故某系数≥1/√7。

若E={|P_H|≤r}有Lebesgue长度m>0，可在E取8点，两两gap≥c m。degree7 Lagrange插值给所有系数≤C r m^-7，故m≤C r^(1/7)。该sublevel是固定数intervals的union，δ网点数相对比例≤C(m+δ)。因此对δ≤r≤1，统一于H有

    ν_δ{dist(θ_t,H)<r}≤C(r^(1/7)+δ)≤C' r^(1/7)。     (6)

常数不依c；若sublevel空则平凡。此为global affine-H nonconcentration，严格不存在固定H包含整族，但第5–7节的local奇异尺度仍全在。它说明global cap/full span/full moment不能自动供CSWZ的local hypothesis。该β模型本身被R96的原source proper-class定理排除，不能附会它具有本轮全部small native标签/Φ/两grain；不把它当fullsource反例。

## 9. 原观测商、适应性责任与旧冻结

R96给原管参数概率对任意≥5times的exact观测span之orthogonal商≥1Fst。它约束的是point law μ，不是当前Θ在每parameter ball中离model H的比例；第5节的H会随parameter基点变。因而不能把该原μ结论填成Def1.5，更不能从exactspan upper自动得到approximate span/条件纤维lower。Th1.6/1.7要求的spread-out是与point law独立的一项实际hypothesis，没有提供由μ修补参数几何的版本。

R14为R6→R4双块、R76为R6→R4 code，均有固定model hyperplane或Schubert divisor；当前R8→R1在global上可逃出所有H，却因局部Segre关系失败small-loss。这是不同的具体有限输入证书，不把旧rank2证明复制成m1结论。它不排非invertible有效商、另一保质量原坐标表示或新point-adapted定理；那些步骤须实际支付，不能添欲证的spread-out公设结束。

对固定有界可逆affine参数坐标变化，(2)仍只改常数；若采用一般Grassmann chart变化须核model H和输出关系，δ病态condition不在免费范围。任意非线性‘压平’Σ并不保πθ的线性作用/模型H定义。这里不证明与旧CP/PM双向等价，也不以新adaptive名字注册完整正幂gain；若新全称估计统一涵盖合法原选择，仍须先做反向正幂检查。R95/R96及全部旧冻结保持。

## 10. 当前判定、独审与停止范围

已支付真实原E_t/Φ到T_t、原参数δ-grid及near-full Th1.7的条件质量转移；Th1.6的selected point shadings和总affine-plane upper亦可诚实列账。无效处是参数族在Def1.5中的local small-loss假设，而非输出强度或所有shading都不能处理。已给精确δ-cell误差、strict尺度范围、所有非空subselections、(5)指数边界和global-cap强校准。

现已fresh实际全文读root主稿`R0097_scalar_Segre_local_spreadout_gate.md`12节和B最终8节，并读回root§7新增原E_t/Φ三行、K^C参数cell重数及跨time可不同witness的澄清。独核nearfull强度、原参数/Frostman/每time质量、local δ厚化/strict尺度、ε边界、global power cap及unit bush范围，无未解决强制项。终macro/next/source各6节亦已实际全文读，均保fixedb且ε<b、未覆盖非可逆商/完整rough的边界。自己的质量证明由root/B独立全文核，不计本人独审；正式结论另在授权formal记录。

按spec停止此直接small-loss CSWZ接法，不续b/ε/window或变换条件数阈值。完整rough mixed42未证未否，四条完整路线仍open；没有ordinary新界、新ID/major或Goal完成。高级CSWZ wholeproof仍具名，未经外部同行评审，不预认证元数据/Git/sync。
