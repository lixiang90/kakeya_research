# R0026：全局τ稳定性下的rich vector-affine窗口删选

2026-10-17，`lifting_obstructions`。本轮唯一main是large-τ的**vector/global质量**gate。已读R25 next large-τ target、actual middle-τ稿、STATE及root指派；不将三点标量化本身登记为main进展，不使用projected τ替代原vector τ。本文证明有限weighted窗口lemma，并明确它接actual配置所需的候选族/窗口/非二次量词。

**结论：框架可证，但必须先删locally-light窗口，且全局候选族必须容许所选纤维的整时间并。** 原g不需要在删除后存活；应在剩余合法时间配置中重新选good-q和构造原图。本文未构造完整source/Kakeya反例，也不宣称whole-matrix AFF来源已付。

## 1. 固定partition、原质量和τ候选族

令Z为有限原时间集，带概率ν。固定ρ∈(0,1)，按**固定半开dyadicρ-windows**分成J；每个time仅属一个J。令u,v:Z→R²为rows，b:Z→R为scalar。定义anchor-free row residual

    E(z,s)=v(z)−v(s)−b(s)[u(z)−u(s)]。

对任意T⊂Z，定义

    Tcal(T)=max{δ, C₀ρ max_(J,z,s∈T∩J)|E(z,s)|}。          (1)

空/单点window的pair max取0。**不包含跨不同J的pairs。** C₀≥1固定。当前允许母集M⊂Z，可为此前实际whole-layer restriction；所有下面的candidate均为M的time subsets，不额外强制保每个window、指定q、angle或local密度。

对两个absolute thresholds `0<s_+<s≤ν(M)`，令

    τ=min_{T⊂M,ν(T)≥s} Tcal(T),
    τ_+=min_{T⊂M,ν(T)≥s_+} Tcal(T)。                       (2)

finite Z保证最小值由某S⊂M取得。设ν(S)≥s，Tcal(S)=τ，且

    τ_+≥ρ^d_st τ,    d_st>0。                              (3)

s/s_+为相对同一个原ν的absolute质量，不能中途把一个局部q归一成新全局先验。若源记法threshold相对某旧Z_base计数，应先乘其真实ν质量再代入(2)。

## 2. 原window nonquad与每个actual anchor

假设在每个J内u、b的oscillation均≤Kρ，K≥1。对a∈S∩J，设

    h_a(z)=v(z)−b(a)u(z),   c_a(s)=b(s)−b(a)。

则精确地

    E(z,s)=h_a(z)−h_a(s)−c_a(s)[u(z)−u(s)]，              (4)

所以E不依赖选择哪个anchor。设每个这样的actual a、每个vector affine P₀+P₁(z−a)，都有原质量cap

    ν{z∈J: |h_a(z)−P₀−P₁(z−a)|
          ≤ρ^ε₁(ρ²+ρ|P₁|)}≤a_NQ ν(J)。                 (5)

原coefficient-weighted quadratic nonfit蕴含此linear特例。此处右侧是**原ν(J)**，不是当前ν(S∩J)。若输入只给一个预选anchor，需另证anchor变换；本命题直接要求原(196)本来具有的actual-anchor量词。

对于每个anchor a，用全局同一个τ定义

    t=(z−a)/ρ,
    F_(J,a)(t)=(ρ/τ)[h_a(z)−h_a(a)]。                     (6)

这是whole-window时间上的向量函数，不能先只定义在某q或按q重新选τ。允许bad事件在任意actual anchor中取存在式，见下节；因此之后good-q的anchor依赖不会漏掉。

## 3. 局部轻窗和bad-window质量的精确定理

固定0<λ,β<1、ξ>0。先删locally-light窗口，即

    ν(S∩J)<λ ν(J)。

这些窗口所含当前time总质量≤λ。其余称heavy windows。heavy J称bad，当存在a∈S∩J、R,C∈R²，以及T_J⊂S∩J，使

    ν(T_J)≥β ν(S∩J),
    |F_(J,a)((z−a)/ρ)−R(z−a)/ρ−C|≤ξ, z∈T_J。            (7)

假设

    βλ>a_NQ。                                             (8)

则big slope `|R|≥2ξρ^{-ε₁}` 不可能：将(7)乘τ/ρ，得到h_a的原linear fit，P₁=(τ/ρ²)R，error≤(τ/ρ)ξ；其允许容差的ρ|P₁|项至少2倍该error。T_J的原质量由(7)、heavy及(8)严格大于a_NQν(J)，违(5)。因此每个bad fit的slope满足

    |R|<2ξρ^{-ε₁}。                                       (9)

对同一个fit fibre内z,s，(7)/(9)与|z−s|≤ρ给

    |h_a(z)−h_a(s)|≤C(τ/ρ)ξρ^{-ε₁}。

原u、b oscillation upper代入(4)，得

    |E(z,s)|≤C(τ/ρ)ξρ^{-ε₁}+K²ρ²。

故所有bad窗口各选一个这样的fibre，作全局并T=∪_badJ T_J，具有

    Tcal(T)≤max{δ, C₁τξρ^{-ε₁}+C₁K²ρ³}=:τ_shrink。        (10)

每个window只选一个anchor/fit即可，constants与anchors可以不同；因(1)只比较同窗pairs，不产生跨窗误差。

**命题。** 若另有

    τ_shrink<ρ^d_st τ，                                   (11)

则heavy bad windows的当前总质量B_bad严格小于

    B_bad<s_+/β。                                         (12)

证明：反设βB_bad≥s_+。按(7)，全局并T⊂S⊂M且ν(T)≥s_+，是(2)中合法next candidate。由(10)/(11)，`τ_+≤Tcal(T)<ρ^d_stτ`，违(3)。

因此删light和bad全部windows后，保留S_good满足

    ν(S_good)≥ν(S)−λ−s_+/β。                              (13)

每个保留window的全部actual anchors、所有real R,C都没有质量≥βν(S∩J)的ξ-fit。保留窗内S_good∩J=S∩J，所以同样是该窗当前概率下的all-real affine nonfit。不能将(10)用于任意tiny fit：只有达到(7)且通过(8)的fibre，才已由原nonquad迫slope小。若用M_J最大fit mass，则sum只对这些heavy bad windows求。

## 4. large-τ的收缩预算

设原当前τ满足 `τ>ρ^{3−ζ₁}`，0<ζ₁<1，取诚实mesh

    w_L=K₁[ρ+ρ³/τ],
    ξ=w_L^a,    0<a<1。

K₁是已付K的固定幂。large-τ给`w_L≤C K₁ρ^{ζ₁}`，因此(10)的非floor部分除τ至多

    C K₁^a ρ^{aζ₁−ε₁}+C K²ρ^{ζ₁}。                     (14)

先固定a、ζ₁，再选physical ε₁<aζ₁。令d_st小于min(aζ₁−ε₁,ζ₁)的一个固定份额，最后选K/K₁的loss足够小，(14)严格小于ρ^d_st。固定常数以额外幂余量吸收。若d_st=1/m，选固定m足够大即可；不得反过来把source小幂K当绝对常数。

floor也必须核：δ≤ρ⁴与τ>ρ^{3−ζ₁}给

    δ/(ρ^d_stτ)<ρ^{1+ζ₁−d_st}→0，

只要d_st<1+ζ₁。因而(11)可与严格常数余量同时成立。这里没有任何scalar projection τ_ψ。

## 5. source层η参数的一个可付实现

原ν为base Z的uniform counting时，设source thresholds为

    s=δ^{η_j},   s_+=δ^{η_(j+1)},
    λ=δ^{2η_j},  β=ρ^{b_j},
    a_NQ=ρ^{ε₂},  ρ∈[δ^{1/4},δ^µ]。

若threshold相对较早保留母集计数，其质量须同时乘入s/s_+并计loss。一个充分的具体条件组是

    b_j+2η_j/µ<ε₂,
    η_(j+1)−b_j/4>η_j,
    η_j/µ≪b_j≪η_(j+1)，                                  (15)

另有第4节K-loss预算和stable relation。第一式给βλ>ρ^{ε₂}，第二式给s_+/β≪s；λ≪s显然。因此(13)保当前原质量的固定比例，至少δ^{η_j}/2。

η_j/µ≪b_j在本有限窗口lemma之外，还给之后原角gate/graph loss留余量，明确支付δ小幂换ρ小幂的费用。源高级阈值可对b_j有任意依赖，故不能只随手用η_j的平方根定义b_j后声称所有阈值自动成立。合法次序是先给tiny但固定的η_(j+1)，取b_j为其足够小固定份额，再选η_j小于全部所需函数阈值；有限链可倒推或用source的h函数实现，δ最后小。所有η层仍须低于physical ε₂等固定量。

## 6. 对q、旧g、候选族与边界的独立攻击结论

1. **q依赖：** bad事件必须在window的完整当前time fibre上定义，而非只在某个q的稀薄time子集上。上文允许对所有actual anchors取存在式，因此后选good-q的anchor已覆盖。若q所用time fibre具有K⁻¹的window质量lower，局部fit cap至多放大K；这个good-q责任仍由原incidence平均支付。若q另用τ_q，必须重算，不能由本lemma免费继承。
2. **旧g集中：** 删除bad窗口可能删除几乎全部旧g，本文没有保旧g的结论。剩余S_good携带完整原时间层，R22的一般维数restriction闭包保原配置；在它上面重新平均选good-q、重建used角law/原L图，才得到合法的新g。不能用(13)的time质量假称任意旧g质量也保住。
3. **全局候选族：** (2)必须允许所选fibre并T。若暗加“每个原窗都保一点”“原q固定”“同一个anchor/fit全局通用”等约束，T未必是合法candidate；稳定性便不能用于此步。反过来，本lemma不需要这些额外约束。
4. **窗口边缘：** fixed half-open partition确保不同fit constants不产生跨窗pair。若将τ定义成所有|z−s|≤ρ的sliding pairs或相邻窗pairs，(10)并不由local fits推出；原source的`z'∈z^ρ`应按固定dyadic cell理解。本文不把两个定义混用。
5. **非quad参考：** 原(5)若相对旧window，而当前只保tiny fraction，必须先light-window过滤。只有全局density而没有每个保留window的质量比较，不足以逐窗迫R小。若原NQ仅在另一个anchor给定，还需先证anchor转移，不能省略其AFF误差。

这些是量词和quality条件，不是完整source反例。未找到在(1)–(11)全部成立时破坏(12)的finite模型；上述证明保原ν的真正质量，并非重做toy rank分类。

## 7. 当前停止范围

已付主gate：从rich vector-affine fits，经physical coefficient-weighted nonquad迫slope小，再在全局原候选族中并纤维缩vector E，由stable τ排出过多bad窗口。它可以产生后续所需的windowwise vector-affine nonfit，但不直接证明原slab三点选择、weighted scalar13.5或whole-matrix AFF₃。

actual应用必须保所列全局candidate/within-window约定、原physical NQ参考、合法time闭包及重新构造原g。长期五维/一般Kakeya目标未完成；没有新维数界、真实Kakeya反例或重大/新颖认证。
