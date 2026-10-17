# R0067：共初始管的W/native L联合图及AFF尝试

2026-10-18，root，数学前已写spec5/macro3，随后spec§3先明确天然τ的两端matching候选。完整Goal为ordinary n≥5/general；本稿不宣该目标或AFF₃已解。主要新施工是实际原labels共同主干的联合质量与自然尺度同frame，不是把两图总数直接取交。高级source good-q／19.5及原Def输入仍具名，未经外部同行评审。

## 1. 原数据、两种尺度范围与具名准备

完整WZ2609.22035v1 Def17.2–17.4，d5/k4/ell3。f=(a;b)、tildef=(c,d)，a,b,c row2、d scalar、b=c+da。原T joint4-AD/CW，ell Y为2−κ维AD、native scalar tildeY为1−κ维AD及tube-KT，Φκ-AD/slabγ和ξ各allowed cube相干。0<κ≤1、γ>0固定（必要时降至min(γ,1)），η在固定目标参数后小，δ最后小。所有原weights为实际有限labels/路径计数。

指定原allowedρ∈[δ^(1/4),δ^µ]。对最终native scalar误差，先使用named Lemma19.5作**整time**细化，按R22闭包付δ^O(η/γ)原质量，再在这些数据上重新选择good-q，绝非沿用删前q图。固定原ρ窗内f和tildef的variation≤Kρ，K=δ^−O(η/γ)，次数可变但有限；原额外ρ/σ等coherence仍保留，allowed向邻格取整一律计入K。源global到good-q的既有计数接口不在本轮全量重证。

在这个q中记m=#Zq、e=#Eq、D=δ^−κ、L=ρ/δ、N=L³。保真实incidences I={(p,T):T为原Φ witness且p是原mark}，有

    K^−1 eD≤#I≤KeD,  #Tq≤K eD/m,
    #native grains G≤Ke/N,
    deg(p)≤KD,  #points_per_grain≤KN,
    #marks_per_T≤Km,  e≈K^±1 m L^(4−κ),
    m≥K^−1ρ/δ.                                  (1)

G的upper由完整native tildeY的AD packing及原good-q点数计，不给每个裁切grain重设filled lower。点/tube与slice的交点O(K)碰撞计入K。环境T、原CW和AD不因取witness子族而重新归一。

## 2. 三类最低度的有限core

用原incidence edges作有限peeling。point、tube、nativegrain三类的原vertex数分别≤e、T₀、G₀；每个edge同时记其point和该point的唯一原nativegrain assignment。阈值取#I/(6e)、#I/(6T₀)、#I/(6G₀)。某类active vertex低于其阈值即删除其全部active edges并继续，直到没有这种vertex。

一个原vertex只被充电一次，三类所删edge总数≤#I/2。因此core I_*≥#I/2。其每个active point的degree≥K^−C D，每个active tube的marks≥K^−C m；每个active grain含edge≥K^−C ND，除以原point degree upper KD，得至少K^−C N个active points。active points数≥#I_*/KD≥K^−C e。下面将这些同一core数据记P_*,T_*及原grain关系↔。

core不是新的Def17配置：不授T_* AD lower，不授任意删选Φ lower或新CW归一化。point方向upper/slab、每粗角包fine数、point-coherence都沿用原superset upper。所声称每条active T的local mark lower是这次peeling的已付结论；不保证原所有T逐管density或所有原ρ窗都一样。全局shading平均分母仍用原T。

## 3. 同一初arm上的两个续接向量

计数先允许任意τ∈[δ,ρ]，假设选角前全q ordered residual满足

    ρ||E(t,s)||≤cτ,  E(t,s)=Δb−d(s)Δa.          (2)

固定root p∈P_*，其time t；固定middle time s∈Zq。初arm α=(T,p_s)，T∈T_p^*且p_s∈P_*∩T在s。令n(p,s)为此类arm数。由core tube/point lower，

    Σ_s n(p,s)≥K^−C Dm,
    Σ_(p,s) n(p,s)²≥K^−C eD²m.                (3)

第二式对每p在至多m个times用CS再求和，实际p数量≥K^−C e。没有假每条tube访问每个time。

对每个α定义非负整数向量X_α：从p_s走一条原core管T^W至W-terminal w∈P_*，index记(u, T^W的ρ-direction packet)。其ℓ¹总量≥K^−C Dm，所有α共享的index数

    R_X≤K mρ^−κ.                               (4)

定义Y_α：在p_s的同一原native3grain内跳至p̃∈P_*，再走原T^L至l∈P_*，index记(v,p̃ native水平τ-cell,T^L的τ-direction packet)。其ℓ¹总量≥K^−C NDm。对固定(p,s)，(2)与原V恒等式使所有p_s的native labels在O(τ)内；jump保持这些labels，所以固定native水平τ-cell只遇K个物理τ-cubes。原τ-coherence给共同packet数≤Kτ^−κ，故

    R_Y≤K m(ρ/τ)³τ^−κ.                         (5)

计数簇合仅需固定s处bounded tildef和原相干性；跨time tildef-Lip在输出误差中另用，不偷混。

## 4. Tensor Gram保同一个主干

令Z_α=X_α⊗Y_α。则

    Σ_(α,β) <X_α,X_β><Y_α,Y_β>
     = ||Σ_α Z_α||²_2
     ≥ [Σ_α ||X_α||₁||Y_α||₁]²/(R_X R_Y).       (6)

每一项确实是共享同初root、middle time和两初arms的hybrid：W两续接同time u且末角ρ-close；L两续接同time v，native水平τ-close且末角τ-close。u,v可不同，但原T1/T2及exact ψ相同。不需要两类延伸在每一对arm上均rich，也不是两次独立CS后取交。

代(3)–(5)并对(p,s)求和得到

    #H≥K^−C e D^6 m³ ρ^κ τ^κ
                  (ρ/δ)³(τ/δ)³.                (7)

所有objects均实际原管/点/跳跃。阈值core及tensor CS是有限完整证明，(1)的source供应和原V公式按其具名范围保留。

## 5. 同hybrid law的初角先验

固定一个实际初incidence(p,T1)，逐项选s/T2、W第一末管/u/ρ-close第二末管，再native第一jump/L第一末管/v、τ-close第二jump/L第二末管，得

    #H_(p,T1)≤K D^5 m³ρ^κτ^κ N(τ/δ)³.         (8)

除(7)，其初incidence边际由K^C Uniform(I_*)支配；另一臂对称。core incidence mixture β因point degree lower和原slab/κ-ball upper仍有β(slab_w)≤K^C w^γ、β(ρ-cell)≤K^Cρ^κ。全部usedρ-cells被原coarseΦq覆盖，个数≤Kρ^−κ。

删β-cell质量低于K^−Bρ^κ的light used cells，按(8)付tuple loss。先取B大于全部有限loss次数，再取原η小。余共同H方向carrier满足#H≈K^±Cρ^−κ、Uniform(H) slab upper K^Cw^γ（w≥Cρ）；差lawπ=(差)_*Uniform(H)²保原有序pairs重数。真实fine角在各code可不同，proxy差误差Oρ。原unusedΦq仅用于cover/card，不赋slab。

## 6. 两端的原位移与source误差

固定hybrid，W终点w_i@u，L终点l_i@v，初times t,s。ψ=φ2−φ1。原(151)/(176)/(180)逐项给

    Δx_W=(s−t)ψ+O(Kρ²+δ),
    Δξ_W=[f(t)−f(s)]ψ+O(Kρ²+δ),
    Δη_L=(s−t)E(t,s)ψ
             +O(τρ+τ||tildef(s)−tildef(v)||+δ). (9)

Δ按第二端减第一端；此处native L scalarη为原k4 label。第1节已付tildef variation Kρ后，最后误差≤Kτρ+Cδ。所有times/ψ共享，不把g条件law假成独立。计数(7)即使没有tilde-Lip仍真，但不能因此把最后误差写细。

以下joint graph只取天然τ=C₀K₀ρ²，K₀足以覆盖(2)及tilde-Lip费，τ≤ρ由η≪µ付。σ=ρ²，ε_L=C₁K₁τρ（含δ；δ≤ρ⁴使δ≤Kτρ），选有限K_i满足所有常数；ε_L≤σ≤τ，因K_iρ→0。一般τ近δ时必须保δ-error，不在这个同mesh图结论内。

## 7. 两终桶的相容性：不独立付native patch数

取q的native水平中心Uq∈R³及ζq=ξq,2−d(tq)ξq,1。对所有原p∈q有native offsetζp=ξp,2−d(time p)ξp,1=ζq+O(Kρ)。从同p_s分别沿W及nativejump-L走到w@u、l@v，直接用原直线方程和两grain相容式得

    η_l−η_w=(v−u)ζq+[tildef(u)−tildef(v)]Uq
                         +O(Kρ²+δ).             (10)

jump只改native水平，保中点η_s；所有水平位置距Uq为Oρ，所有direction bounded，故tildef差O(Kρ)乘位置差Oρ只给Kρ²。式(10)的首项bulk可达Oρ，但固定u,v后是已知平移。

按u,v及w1的原ell normal标签Q（σ-cell）分桶。Q和u固定使η_w1=y2−d(u)y1落长度Kσ区间。由(10)，η_l1只落一个已知中心、长度Cτ的interval I_Q,u,v；覆盖该interval只需K个τ-patches。不能另付(ρ/τ)^(1−κ)个任意native输出patch。输出l2则再扩大I常数倍，因为(2)/(9)给两L末点native差Oτ。

## 8. 两端法向匹配的有限纤维引理

固定u,v,t,s、W标签Q、w1的joint(x,ξ)σ-cell A，以及TW1、TL1各自的first-two-coordinateρ-angle packet χ_W、χ_L，再固定nativejump点p̃1在s的水平三坐标δ-cell U。将w1的native水平坐标记U_w，native label记η_w。native方向vh^W=(φ_W,ξ1,w+a(u)φ_W)，ζ_w=ξ2,w−d(u)ξ1,w。

沿TW1反向至p1给精确近似式

    η_s=η_w+(s−u)ζ_w
          +[tildef(u)−tildef(s)](U_w+(s−u)vh^W)
          +O(δ).                               (11)

A/Q使U_w及ξ_w只变Kσ；χ_W使φ_W只变Cρ。φ_W误差前的系数是(s−u)[tildef(u)−tildef(s)]，大小Kρ²，故总误差Kρσ，不能把它错估成ρ²。取这些coarse cells代表，得

    η_s=η_w+C_W+O(Kρσ+δ).                      (12)

η_w原来只在Kσ区间，因此固定jump U后p̃1只遇K^C个原物理σ-cubes。逐cube使用原ξ_(cube)代表，ζ_p̃1误差Kσ；不假跨相邻dyadic边界的全局Euclidean Lip，也不假整grain offset恒定。

再沿TL1正向，使用χ_L的ρ-proxy，

    η_l1=η_s+(v−s)ζ_p̃1
       +[tildef(s)−tildef(v)](U+(v−s)vh^L)+O(δ)
         =η_w+C_W+C_L+O(Kρσ+δ).                (13)

对每个已付σ-cube选择，C_L不依赖w1未观测的fineη_w。指定η_l1的ε_L-cell因此迫η_w在长度Kε_L的区间。native tildeY_u的原AD upper及w1三水平坐标的σ³容量，给

    #possible fine w1 ≤K^C(σ/δ)³
                                      (ε_L/δ)^(1−κ). (14)

这里确使用两端合起来的matching；“固定p1后L本身normal-output必须均匀”并不成立，也不需要。parallel-native校准只否那个单边断言，不反(14)。

## 9. Joint code完整恢复与自然尺度抵消

固定bucket(u,v,Q)，code为

    (A_Wσ-cell, η_l1 ε_L-cell, t,s,h1,h2),

h_i∈H是初管的ρ-proxy。恢复顺序：先选χ_W、χ_L（各≤Kρ^−κ）、jump U（≤K N）及(12)允许的σ-cube（K^C）；由(14)选w1；TW1在χ_W内≤K L^κ并决定p1；T1在h1内≤KL^κ决定p；T2在h2内≤KL^κ决定p2；W末T2^W受ρ-close限制≤KL^κ。jump1点由U和p1 native label决定到K个原点；TL1在χ_L内≤KL^κ。第二jump水平τ-close给≤K(τ/δ)³，TL2受τ-close给≤K(τ/δ)^κ。各固定time交点K次。

所以joint fibre upper为

    M_H≤K^C (σ/δ)³(ε_L/δ)^(1−κ)
                ρ^−2κ L^(5κ+3)(τ/δ)^(3+κ).    (15)

两个末ρ包的card与其fine数恰分解原D²：ρ^−2κ L^(2κ)=D²，不额外损κ幂。粗恢复若忽略指定η_l1对η_w的限制，会多(σ/ε_L)^(1−κ)固定损失；若又独立选两终patch，还多(ρ/τ)^(1−κ)。两错误不应作为原joint图不可能的证明。

W Q数每u≤K(ρ/σ)^(2−κ)，u,v共m²。因此(7)平均至少一个bucket满足其原总H除K m²(ρ/σ)^(2−κ)的lower。对该bucket，A_W的σ-cover upper A₀=K(ρ/σ)²，native input B⊂tildeY_v∩I的ε_L-cover upper B₀=K(τ/ε_L)^(1−κ)。把(15)、m²、#H²≈K^±Cρ^−2κ及A₀B₀相乘，和所选H lower相除，剩下

    K^−C(σ/τ)^(1−κ)=K^−C                       (16)

因为τ≈_Kσ。给每code其实际hybrid fibre数除统一M_H，即0≤g≤1，在**同一个**Uniform(A_W)×Uniform(B)×ν²×Uniform(H)² reference上mean≥K^−C。若实际A/B少于其upper，density只更大；g≤1反过来给A、B各自card≥K^−C相应upper。没有先假两端points独立，原相关性在同g中。

## 10. 共同原图、cover与工作单位

input A_W使用所选W bucket内全部实际joint cells，output A_W^+扩大ell Q常数/K倍；ξ-coherence使每visible x σ-cell只有K个joint cells，所以card upper K(ρ/σ)²。input B及output B^+都由完整native tildeY_v在长度Kτ的interval上取cover，AD packing给K(τ/ε_L)^(1−κ)；(16)的input lower使output/input ratios均为K^C，不把裁切sets重授AD lower。

time ν=Uniform(Zq)为原fine labels，floorδ/ρ，合法interval upper K(w+δ/ρ)。原proxy difference π保slab γ和重数；不会把fixed exact fine-angle slice冒成dense。把x和ξ同步除ρ（ξ若需另除L_f≤K，与M同步），nativeη除τ，time除ρ；取共同working r=K^Cρ吸收所有K和ε_L/τ误差，再聚合真实cells，fixed ambient碰撞只K^C。得到

    #A_W≈K^±C r^−2,  #B≈K^±C r^(−1+κ),
    output/input ratios≤K^C, mean g≥K^−C.       (17)

H及time原labels可暂不coarsen；空间重分箱的每bin容量只K^C，g用这些上界聚合，原support关系只增O(r)。所有bounds中的K次数有限，η最后小。此是天然尺度完整source的新联合接口，不是四维Kakeya配置，不自动可调入旧scalar engine。

## 11. AFF用途实际测试：两个increment并不独立

在原physical单位记W increment为(U,V_a,V_b)=((s−t)ψ,Δaψ,Δbψ)，则native L主位移正好是

    S_L=(s−t)[V_b−d(s)V_a].                    (18)

若反射ξ convention，两V和右侧同步反号。故联合图保留新的native input/deficit和共同clock，但不是添加一个独立随机增量；不能把两个增长下界相乘，或给combined displacement虚构三维Frostman。σ_A×σ_B是已证dominating reference，g仍可依赖所有变量。

尝试把L位移直接交Theorem13.5时，用窗口anchor d0并记h=b−d0a，

    E(t,s)=h(t)−h(s)−[d(s)−d0][a(t)−a(s)].      (19)

两套slopes variation≤Kρ，末项原scalar位移≤Kρ³。天然τ≈Kρ²归一后为Kρ，恰是(17)工作误差。因此此图在当前mesh只分辨h-row，d变化与a变化的乘积已经处于误差内。即便付三点slab scalarization及named13.5得到h的某个rich affine fit，也不能从它解出两个row a,b的whole-matrix AFF：一个row关系只给b≈d0a+affine，a仍自由；mixed ell Y未带line-KT，不能误用R16 k=ell3的linewise排除。

这是实际AFF尝试的停止点，不将h-fit预证（其同原time/global窗口mass仍需支付）；也不把所需second row估计写成已得新定理。

## 12. 分辨率账本：为什么不能免费下探contact尺度

若把native信号patch缩成τ_f≪ρ²，但仍沿W的σ=ρ² observable，(11)–(13)的现有证书只保证两端matching误差O(Kρσ+δ)=O(Kρ³)。把η除τ_f，这份证书需预留Kρ³/τ_f blur，而native自身L误差是Kτ_fρ/τ_f=Kρ。两份预算之比ρ²/τ_f是固定power，不能藏进K。因此现有证明不支持把(17)原样声成τ_f≈ρ³处的共同mesh r≈ρ联合图；这不是实际误差的普遍下界。

若仅减W末角close阈值α<ρ来令observable误差O(Kρα+δ)更细，原q只保证ρ方向cover≤Kρ^−κ；对α<ρ没有免费κ维方向packet数。粗环境packing给Kρ^−κ(ρ/α)^4，依该upper直接CS得到的计数证书多付(α/ρ)^4，尚无subpower-loss版本。另一个独立责任是原ell normal-label差仍含(s−t)[f(t)−f(u)]ψ这一O(Kρ²)主项，并不随末角α缩小；不能把Q_W及其output Q+也免费改宽ρα。这个过粗计数证书并不是实际必损的下界；若要改善须给新原几何并支付跨normal桶费用，不能只改记号或用scalar normal AD替代。

本段是当前恢复/误差证书的界限，不是证明所有更精确联合方案不可能；全source CW也未被任何有限校准否定。要取得AFF或完整mixed，仍须新估计处理被天然mesh掩掉的coupled项，而不是续参数常数。

## 13. 反攻、旧闭包与本轮停止

分别rich的W/L可无common trunk，故原(6)不可省；有限core不等于新source。parallel-native模型可保fullgrains/AD4/slab/clock与normal守恒，但CW plate坏δ^−κ，不能当完整反例；它也只否单边output cap，不否两端matching联合图。粗恢复的固定loss是错误/过粗证书，已由(10)–(15)修复，不把历史失败当最终不可能。

本稿只证共同主干hybrid及天然尺度joint frame，未给AFF₃、contact-scale或中/大τ排除、ordinary维数增益、新ID/major/novelty。R28仅W同basebox没有native continuation/第二端carrier；本次确多原数据，但(18)显示不能以新名声已有全称gain。停止core/ρ包/τ常数微调，下一直接面对第11–12节实际未付的mixed项与共同质量。

## 14. 审查状态

A/B已独立施工core/tensor与两端matching，分别fresh实际全文审本稿14节、对方18/10节、spec5/macro6/next6，formal各6节通过，无剩余强制数学修复项。root已实际读两formal并集成，§12补ell normal主项警示。源19.5和原good-q接口的高级wholeproof不新独证，有限数学/源应用/最终目标分开标注；未经外部同行评审，Goal active。元数据与safe sync另按实际结果。
