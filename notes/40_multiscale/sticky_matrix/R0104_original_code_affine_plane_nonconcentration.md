# R0104：原全局码对affine2plane的质量上界

2026-10-19，root，working5锁后施工。消费完整原point-Φ的slab条件与既有全source统一非拟合输入；不把平坦P另作假设。拟得的是R102实际码集及其所有二维投影的弱非集中，不是完整Schubert分支、κ1/ordinary或Hausdorff新界。具名源高级wholeproof保原责任，终版独审另记，未经外部同行评审。

## 1. 原量词、目标与固定损失

保完整WZ Def17.2–17.4 bounded d5/k=ell3/κ1、固定γ>0、原N≈Kδ^-4及CW/AD、nearfull原clock Z（m=|Z|）、native Y/filled X、Φ AD1/slabγ/ξ-coherence。沿R102 det-large分支的两锚t,s，h=s−t、A=F_t−F_s满足|h|、sminA≥σ=δ^b；原H为选单codeblock以前的同权code层，|H|≥L^-C N，每T保全部原S_T且|S_T|≥K^-C m，P为其codecell中心。

L≥2只包含有限次K=δ^-C0η、τ^-1、σ^-1、r^-1与log费用，r=δ^c是farclock阈值。所有C可依固定γ及已经具名的source/NF输入，不能将新正幂塞进原K。目标存在β=β(γ)>0和M=M(γ)>0，使

    |P∩N_aΛ|/|P|≤L^M a^β
    (所有affine2plane Λ⊂R4，δ≤a≤1).              (1)

这不是常数与δ无关的AD断言。先固定NF的ε0、θ、c_N，再固定d0≤1/100、B足大、M最后足大，之后选择原a_anchor,b,c、η足小，δ最后小。L中有限费用的总次数在选这些小参数之前固定。

## 2. 重用的完整源统一非拟合及闭包

实际读取R77主稿§§3–4、R78§§9–10及原19.2/19.4与相关proof：固定ε0>0、θ>0足小依γ，存在c_N>0，使完整source参数ξ≤c_N µ_w、allowed w=δ^µ_w、δ^(1/4)≤w≤w0时，所有允许all-real affine fit F≈R_J u+U_J、精度w^(1+ε0)、命中>w^θ w/δ的bad w-windows承载原time总质量<w^θ。小slope以19.4、快fit以20.2原几何的all-real扩展及真实tube-KT矛盾支付；不是从SM口号免费假任意代数非集中。θ/c_N不随µ_w重新选择。

R22 whole-time闭包已付：限制完整原time层到S⊂Z且|S|/m≥p_S，仍用原T全族/原N/CW和各余time全部X/Y/Φ/ξ，完整源参数ξ≤C(η+log(1/p_S)/log(1/δ))，新allowed为原格整数子格。平均marks重新计；这与仅选H的管/marks完全不同。本稿实际S有p_S≥K^-C，故ξ=Oη，不将p_code损失写入该源参数。

## 3. Code薄层管选择及真正的p取消

固定Λ=q+V、V∈Gr(4,2)、a≥δ，令p=|P∩N_aΛ|/|P|。p=0或L^M a^(γ/2)≥1时粗结论平凡。否则选这些codecells的全部原T为H_a、N_a=|H_a|；同权层给N_a≈p|H|。每条仍保全部旧S_T。删距两锚小于r的times，每管删≤C(r/δ+1)；η≪c保证各管至少半保。

因此far访问I_f≥K^-C N_a m。按原全部E（|E|≤K^Cδ^-4）重做point-heavy，阈值D=I_f/(2|E|)，删light point访问至多I_f/2，且

    D≥p L^-Cδ^-1.                                (2)

再以time访问I_u和I_u≤N_a选rich clocks S：

    |S|≥K^-C m,
    I_u≥K^-C N_a (u∈S).                           (3)

证明取门槛I_f/(4m)，低time总量≤I_f/4；剩余访问至少I_f/4且每u≤N_a，故time数≥I_f/(4N_a)≥K^-C m。Np在分子分母取消；point degree仍损p。这是保每管全部旧S_T才成立的关键，不适用于先删成任意稀薄mark子图。每u∈S至少有一个实际heavy point。

## 4. 原slab强迫整个G-plane贴近平面

R102实际同管恒等式对每旧访问成立：

    C(T)=Γ_p+G_u φ+Oδ,
    G_u=((t−u)(F_u−F_s);(s−u)(F_u−F_t)),
    smin G_u≥rσ/2  (u far).                        (4)

Λ上codecell中心与C(T)误差Oδ，故对每unit n∈V⊥及一个heavy p，所有其保留φ满足

    |n^T G_u φ−c_p|≤C(a+δ).

若z=|n^TG_u|≤C(a+δ)已可用；否则实际φ落宽C(a+δ)/z的slab，宽至少常倍δ（G bounded、a≥δ，扩大常数）。原Φ_p slabγ上界及usedδ-bin tube重数O1给

    D≤K^C ((a+δ)/z)^γ δ^-1.

结合(2)得z≤L^(C/γ)(a+δ)p^(-1/γ)。对V⊥两条正交基逐一测，a≥δ吸收误差，遂有

    ||Π_(V⊥)G_u||≤E:=L^(C/γ)a p^(-1/γ)
       (u∈S).                                    (5)

这里p仅一次线性进入D，因而恰是p^(-1/γ)，不能无说明换成p^(-C/γ)还沿用后面的γ/2。只用原Φ的upper和实际degree，不声删后的Φ保持ADlower或slab lower。平面位移q在c_p中消去，常数对所有affineΛ统一。

## 5. 任意平面方向的whole F恢复，包含奇异blocks

取V任意正交列基B=(B1;B2)，X_u=B^TG_u，R_u=G_u−BX_u。令α=t−u、β_u=s−u，

    D_V(u)=β_u B1−α B2.

有||X_u||≤C、||R_u||≤E及原恒等式

    D_V(u)X_u=αβ_u A+O(E).                         (6)

若E≪r²σ，右端smin≥cr²σ，故D_V(u)与X_u均可逆，||D_V(u)^-1||≤Cr^-2σ^-1。它由乘积加X有界推出，不需B1或B2可逆，也不需det M_u/det(I−M_u)非零。代入top block并除α（|α|≥r）得到

    F_u=R_V(u)+O(L^C E),
    R_V(v)=F_s+(s−v)B1 D_V(v)^-1 A.                (7)

D_V是affine v。对每实际u∈S，D_V(u)的smin lower使其在|v−u|≤c r²σ的整实区间无pole；那里R_V的C² norm≤L^C。各occupied小窗口可以用其中实际u作anchor，不要求原F在窗口外插值，不把R_V称新source。平面基改变只改X、D的坐标，R_V及统一norm估计不依可逆block chart。

## 6. 粗尺度反设、newallowed和非循环预算

先证(1)的a≥δ^d0粗版，指数γ/2。反设

    p>L^M a^(γ/2).                                (8)

由(5)，E≤L^((C−M)/γ)a^(1/2)。M一次足大，使(7)总误差≤L^-C a^(1/2)并确保E≪r²σ。更关键的是p≤1迫

    log L/log(1/a)<γ/(2M).                         (9)

这把所有conditioning费用相对工作尺度都变小，不能仅凭‘a足小’遗漏粗端。

按(3)限制完整原time层到S，得ξ=Oη的完整源。取一个新allowed w近a^(1/B)，并写µ_w=log w/logδ。格取整仅损δ^O(ξ)；M相对B/NF费用足大，由(9)可保证

    (log(1/a)/log(1/δ))/(2B)≤µ_w
                  ≤2(log(1/a)/log(1/δ))/B,
    ξ≤c_N µ_w， ξ≪θ µ_w， w≪r²σ,
    L^C(a^(1/2)+w²)≪w^(1+ε0),
    w≥δ^(1/4).                                   (10)

先选B>8(1+ε0)，再M大吞(9)中的有限C、B、γ、c_N^-1和θ^-1；原小参数随后选，故无µ_w→0时重取NF阈值的循环。a≥δ^d0与d0≤1/100确保w≥δ^(2d0/B)≫δ^(1/4)；a的粗端若不满足(9)则反设本已不可能。新格及C²/Taylor/pole费用在(10)中明列。

## 7. 密窗与完整非拟合矛盾；细尺度仅用单调性

每个有S的w-window取一个实际u0∈S。由(7)(10)，在其中每个原S-time，F_u距R_V在u0的一阶Taylor affine fit≤w^(1+ε0)。该fit的矩阵可all-real，正由§2输入覆盖。完整S-clock有|S|≥δ^Cξδ^-1。低于2w^θ w/δ点的所有窗口合计≤Cw^θδ^-1，即其time比例≤Cw^θδ^-Cξ=o(1)，由ξ≪θµ_w支付。

所以至少half S质量处于命中>w^θ w/δ的bad-fit windows。但§2统一NF说这类窗总质量<w^θ<1/2，矛盾。(8)不成立，故所有a≥δ^d0有

    |P∩N_aΛ|/|P|≤L^M a^(γ/2).                    (11)

对δ≤a<δ^d0，只用集合单调性在a0=δ^d0应用(11)：p(a)≤L^Mδ^(d0γ/2)≤L^M a^(d0γ/2)。coarse a同样服从这个更弱指数；因此(1)成立，β=d0γ/2>0。没有将NF外推到w<δ^(1/4)，也没有假固定a下的无限尺度极限或Hausdorff结论。

## 8. 所有二维投影的实际弱Frostman后果

对任意orthogonal π_W:R4→W∈Gr(4,2)，ball B_W(z,a)的逆像为某affine kerπ_W的a邻域。由(1)，实际均匀code概率µ_P满足

    (π_W)_*µ_P(B_W(z,a))≤L^M a^β (δ≤a≤1).        (12)

这支付了每个二维投影的正指数nonconcentration；不是2-Frostman/ADlower，也不是只知道P2Fst便免费投影。若在P中取质量v的大子集，同一upper只损v^-1；若将投影合并δ-cells再换uniform distinct点，仍须dyadic权层收费。

特别R103每个Schubert W_j上的实际投影不再可任意集中为一个点，但近Schubert fibres变lines仍有rank0/1、厚度SVD、方向law和offset重数责任。新OS2603.19171平面定理不因此已可调用：其nice tube-pencil s-Frostman和真实平面incidences仍未付。Héra高维Furstenberg输入在α1/k2边界也不自动增长。不能把(12)写成R103所缺全部几何已解决。

## 9. 独立测试、hyperplane界限与旧闭包

若只P近一个hyperplane n=(l,m)，§4只给n^TG_u小；展开为[(t−u)l+(s−u)m]^T F_u≈(t−u)l^TF_s+(s−u)m^TF_t。单row不恢复wholeF，也非物理prism。用原管axis参数(x0,z0,φ,ψ)，C的两个blocks是z0−F_s x0+t(ψ−F_sφ)、z0−F_t x0+s(ψ−F_tφ)，单hyperplane只是phase一线性约束，不能免费套CW。若将其1-form/contact结构换名，不计新gain。

抽象flat P和富2plane fibres可饱和R102派生计数；它缺完整sourceslab/NF，不能反本定理。R79弱rough三角模型亦缺fullΦ/filledX/joint4AD-CW，不能拿它否(1)或Kakeya。R103的det Schubert小值只给rank交线，远弱于(5)的plane接近；反向从(1)推出R103 profile或fullsource未证。

R78在both-fullrank坐标得某算子ball cap，本稿的全V恢复不假两个blocks可逆；使用的是已经实际付费的R77全source NF。新增桥是code比例p→逐管ST/pointslab→richclock中p取消→(1)及(12)的原P输入，不是对任意旧CP/PM对象声正gain。没有独立的双向全称restriction重调用把它直接变成旧主命题，因此只作原source用途登记，不新立数学ID或宣新颖性。

## 10. 已付范围、终审要求与停止

本稿给完整matrix33 κ1既定det-large分支的原global code对所有affine2plane质量upper，并给任意二维投影的弱Frostman。使用原fullΦ slabγ、原管全部旧marks、完整time restriction与统一NF；其中原source高级引理仍具名，非全部wholeproof新独证。

终审须实际核p一次指数与取消、point/clock阈值、δ/slab查询、任意V的D invertibility/pole、ξ/newallowed/粗端(9)、Taylor密窗矛盾与fine单调、(12)的概率/权重、hyperplane和Schubert边界。通过也不解完整nonspread、κ1/ordinary/general或major；不得继续β/M/a/degree小修作新轮。后继须消费(12)的实际原联合几何或返回完整四路线重选，Goal active，未经外部同行评审。
