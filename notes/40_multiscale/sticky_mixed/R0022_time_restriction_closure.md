# R0022：原配置对时间删选的闭包和全速度准备

2026-10-17，root。主任务LOCAL-AFF的实际前提。本文核原Definitions17.2–17.4的时间restriction；不删除每个保留层的点、Y、X或Φ，不改变原T。被任意空间/管/标签子族删选后的AD lower并不在本结论范围内。

## 1. 固定计数AD约定

原Def3.3的AD不是一个抽象概率声明：A为(δ,s,K)-AD时，对a∈A和δ≤R≤1，N_δ(A∩B_R(a))在K^{±1}(R/δ)^s内。所有dyadic cubes与球只差固定维常数。

若A在fine δ上AD，则对任意r≥δ，A的r-cover在r到1尺度为K^C-AD。下界：fine球内至少K⁻¹(R/δ)^s个δ-cells；一个r-ball内至多K(r/δ)^s个，故N_r≥K⁻²(R/r)^s。上界：取相互r/4-separated的centres，周围fine r/8-ball各有K⁻¹(r/δ)^s个cells、固定重叠；用原AD upper求和，得N_r≤K²(R/r)^s。R≈r或r≈δ的有限边界由至少一个cell和固定维packing处理。中心从真实点移到其coarse cube只改固定倍球半径。

## 2. 跨时间Y-union的lower不因删整层而丢失

固定原allowed r和dyadic time interval J。原U_J=∪_{z∈Z∩J}Y_z是(r,s,K)-AD。任取Z'⊂Z，非空S_J=∪_{z∈Z'∩J}Y_z。

upper直接由S_J⊂U_J继承。对任意S_J的coarse centre，选其所属的某层Y_z和一个相距O(r)的真实点。单层Y_z本身fine δ-AD；第1节给它的r-AD lower。因此S_J在每个自身centre也有K⁻C(R/r)^s个coarse cells。R为O(r)时单cell即可。所得S_J为(r,s,K^C)-AD。

这不要求Z'在每个原interval中dense，也不要求不同层独立；关键是删**整时间层**、每层Y_z不变。与任意子集Y或选Φ unused cells的错误AD继承不同。原Def17.2(3)的s=d−ell−κ在这里不改变。

## 3. 其余原数据及参数格

若#Z'≥δ^a#Z，则原#Z≥δ^{η−1}给#Z'≥δ^{η+a−1}。T完全不改，joint(d−1)-AD与CW原bound保留。每个保留层E_z、X、Y、tildeY、Φ_p与witness均不改；f/tildef只restriction。原ξ_q和coarseΦ_q仍覆盖subset的全部原点，Φ_q本身不删，故其AD和coherence保持。每层tildeY tube-KT upper原样保持。只要所有量的常数统一放大到δ^{-η'}，得到合法配置。

为避免allowed scales换格的漏洞，可选η'=Mη，其中整数M使η'≥Cη+a，且η'≤C'(η+a)（η>0）。新allowed格{δ^{η'j}}是旧格的子格，所需coherence与第2节union AD都已有。若调用某固定r或ρ并非新格点，用相邻新格点，尺度比至多δ^{-η'}；packing/AD/fibre的有限维损失计入δ^{-Cη'}。这不是把固定ρ幂藏进K；η'含实际时间density损失，后取足够小。若要保持更多旧格点的property，它们其实也仍成立，但不把它们冒充新格定义。

所以任意δ^a-dense的整时间层删选，都是同κ、γ、T和原marks的配置，代价η→C(η+a)及allowed-scale取整。原remark的平均shading可重新由原witness总数计，不宣称每条管的shading独立保持。

## 4. 从全局dense affine fits中合法删低速windows

本节条件于LOCAL-AFF给出Z_*，#Z_*≥δ^a#Z，每个ρ-window J有同一whole-f速度R_J∈R³和pairwise error≤Cρ^{1+ε₀}。若拟合最初是单点误差，pairwise只增固定倍，预留相应容差。先删局部point数太少的windows，仍留全局固定比例，且各window的time span≥δ^{C(η+a)}ρ。原f本尺度Lip upper于是给|R_J|≤δ^{-C(η+a)}；这也可直接从分离times的affine式重算。

欲取得whole velocity lower，设低速windows满足|R_J|≤δ^b，其中b=C₀(η+a)/(γζ)，C₀取足够大。取a、η小到b≪µε₀且b<µ。若这些windows在Z_*中占比≥δ^a，则它们的整层原times在原Z中仍有≥δ^{2a}比例；依第3节是合法配置，参数η''≤C(η+a)。

任意同window两点满足

    |f(z)−f(z')|≤Cδ^bρ+Cρ^{1+ε₀}
                    ≤ρδ^{b/2}=:σ,

因为ρ≤δ^µ、b/2<µε₀，且δ小。又ρ≥δ^{1/4}≥δ^{1/3}，σ∈[ρ²,ρ]，后一个下界由b/2<µ及ρ≤δ^µ保证。

原named Lemma19.2可用于该低速配置，所有window中的(154)甚至取全times，因此

    C_CW(T)≥δ^{C(η+a)/γ}(ρ/σ)^κ
             =δ^{C(η+a)/γ−bκ/2}.

取C₀大且κ>ζ，与原C_CW(T)≤δ⁻η冲突。故低速windows所占Z_*比例<δ^a，可删而保住全局≥(1−δ^a)δ^a原times。保留速度满足

    δ^{C₀(η+a)/(γζ)}≤|R_J|≤δ^{-C(η+a)}.

它是同一small-loss预算的K^{±C}，不是事先增加的固定正速度假设；首坐标r仍可能为零，要等R21的τ-collapse再推r下界。本节依赖named19.2的结论，未重证其全部高级证明。

## 5. 对R21的实际意义与范围

上述闭包使有限次stable原time细化可合法使用原配置和原graph计数，不需每次给选中管族新AD。若LOCAL-AFF本轮通过，其globally dense affine和whole-velocity准备就可送入R21条件链。仍须原quadratic residual approximation这个alternative本身，以及namedABC/19.2/19.4等输入；非二次、其他mixed和一般Kakeya未解决。
