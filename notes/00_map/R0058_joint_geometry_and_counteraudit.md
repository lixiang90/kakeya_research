# R0058：原矩阵割线的二维预处理门槛及严格有限反攻

2026-10-17，B。实际恢复固定入口／registry78状态、R57停止记录及R58先写macro／working_spec6，选定后又读spec§7再施工。只编辑assigned文件，不Git／spawn。主结果是保真实matrix–time–angle分解的有限反攻：真1AD时间、uniform Lipschitz、all-real矩阵非仿射及coarse空间直线逃逸，不自动给二维Frostman割线law。未构造原A／完整translation graph，不反actual source或Kakeya。未经外部同行评审。

## 1. phase I排重、所选门槛与实际缺口

普通n5 H5仍是原满物理方向／原位置／wholeunitclock／near-full marks的固定正幂增益。R57完整slab的scalar-K费用已经停止，不能把“使用真实joint support”加为公设重开。初判common-kernel F(t)=F0+u(t)r0ᵀ确未被R16的共同像线／pencil全覆盖：固定ψ后F(t)ψ=u(t)(r0·ψ)仍可为二维曲线。标量投影Y不继承deficit；quotient掉kernel坐标只从原CW给projected tube-bin的3-Frostman upper，未给joint3-AD lower。ξ可依被删坐标，不能免费数成R4配置。

因此本轮选择了更明确的割线门槛，而非声称整个common-kernel分支已解决。记

    Q(t,s)=(t−s)(u(t)−u(s))，
    D(t,s,φ,φ′)=(t−s)(F(t)−F(s))(φ−φ′)=θQ(t,s)，
    F(t)=u(t)e1ᵀ， θ=e1·(φ−φ′)。                          (1)

独立检验的是：原1Frostman时间、原角prior、all-real SM及没有subpowermass的coarse直线片时，Q或D是否必能保subpowermass并取得2−ζ维Frostman。以下给严格cover反例。它针对standalone law预处理；并不声称真实原A与g的相互作用也可被删掉。

## 2. 有界uniform-Lipschitz平台曲线，保原fine times

选固定参数0<a<d<1，0<b0<a/2。令δ=2⁻ᴺ，ρ=2⁻⌊dN⌋，N→∞；于是ρ≈δ^d，ρ／δ为整数且趋∞。在[0,1]上定义连续hδ：对j=0,…,ρ⁻¹−1，

    hδ(t)=(jρ)²，               jρ≤t≤jρ+ρ/2；
    hδ在右半cell线性连接(jρ)²与((j+1)ρ)²。

令uδ(t)=(t,hδ(t))，Fδ=uδ e1ᵀ。函数有界，右半cell斜率4jρ+2ρ≤4，左半斜率0，故uniform Lipschitz，不依δ；并且

    ||hδ(t)−t²||∞≤Cρ。                                   (2)

取B为每个ρ-cell左半内的全部原δ-grid points，统一左闭右开，最后端点可不计；#B=1/(2δ)。原ν_B为uniform counting，任意长度q≥δ区间的质量≤Cq。下界也成立：中心在B的q-ball中，q≤ρ时至少固定比例一侧仍在同一左半，q≥ρ时每coarse cell占一半；故B是真(δ,1,C)-AD，而不只是一个稀疏子网。没有把原fine times改成coarse centers。

## 3. 全实仿射SM及coarse空间直线逃逸

若||Fδ(t)−tR−U||∞≤δ^a，则由(2)、d>a及δ足小，必有

    |t²−R21 t−U21|≤Cδ^a。

二次首项固定为1的sublevel集合是至多两个interval、总长度≤Cδ^(a/2)，常数独立所有实R21、U21。B的interval cap连同至多两个端点grid误差给

    ν_B{||Fδ(t)−tR−U||∞≤δ^a}≤Cδ^(a/2)≤δ^b0。             (3)

因此矩阵SM允许所有实coefficients，未暗设bounded slope，也不需要C²或δ-independent曲线。

对任意空间affine line ℓ，取单位normal(n1,n2)及offset c。对每个固定0<e<d，dist(uδ(t),ℓ)≤C0δ^e迫

    |n1t+n2t²−c|≤C(δ^e+ρ)≤C′δ^e。

若|n2|≥1/4，二次首项有固定lower，sublevel长度≤Cδ^(e/2)；否则|n1|大且|n1+2n2t|有固定lower，单调反函数给更强O(δ^e)。再用B的interval cap，得到uniform于全部ℓ的

    ν_B{dist(uδ(t),ℓ)≤C0δ^e}≤Cδ^(e/2)。                  (4)

这排除在这些fixed coarse widths上保subpowermass的空间直线片。每个单独平台确在水平线上，但其time质量≈ρ=δ^d，不能把δ^h原图（h≪d）免费限制到它。故这里不是旧linewise分支或不加非仿射假设的rank toy。

## 4. 割线support的精确有限cover

在B的第j、k个平台上，hδ(t)−hδ(s)=c_jk=(jρ)²−(kρ)²为常数。令v=t−s，则

    Q(t,s)=(v²,c_jk v)。                                  (5)

每一固定(j,k)的全部原pairs都映入这条单参数parabolic arc，而非一个二维面。参数v在固定bounded interval，|c_jk|≤1，arc长度／Lipschitz常数均O(1)，故N_δ≤Cδ⁻¹。平台对数≤ρ⁻²，直接求并得

    N_δ Q(B×B)≤Cδ⁻¹ρ⁻²≤C′δ^(−1−2d)。                   (6)

这是全finite pairs的确定性cover，不是单个tuple或数值采样；区间更短或重复arcs只会减小cover。不从Jacobian几乎处处rank2推Frostman，也没有把左半平台从原B之外延长。即使把time edge权取g≡1，(6)也成立。

## 5. 原角集合κ-AD／slabγ及exact factorization

为避免任意D替代原matrix–time–angle，固定整数m≥2，M=2^m，并取N=mL，即δ=M⁻ᴸ。设

    C_L={Σ_(i=1)^L ε_i(M−1)M⁻ⁱ: ε_i∈{0,1}}，
    H=C_L×C_L， κ=2/m， γ=1/m。

H用原uniform labels，#H=4^L=δ⁻κ，minseparation≥δ。base-M cylinder在任意radius q≥δ给每点ball质量≈_M q^κ：把q夹在相邻M-powers，upper只需固定数prefix cylinders，lower取更深固定两级包含点的cylinder。单坐标C_L同理为γ-AD。对任意方向宽q slab，至少一个normal坐标有abs≥1/√2，固定另一坐标后仅留长度O(q)的interval，所以H的slab质量≤C_M q^γ。常数依固定M，不依L或δ；可被源小幂constant吸收。

原先验仍为ν_B×ν_B×unif(H)×unif(H)，保ordered angle pairs及其重数，不改成distinct differences的uniform law。θ=e1·(φ−φ′)只取C_L−C_L；每个difference可由L个digits −(M−1)、0、M−1表示，故其distinct support数≤3^L。这个upper不需要signed-base表示唯一，也没有省略进位或另作数值猜测。|θ|≤1，(1)是真矩阵乘法，因此

    N_δ supp D ≤ 3^L Cδ⁻¹ρ⁻²
                ≤C′δ^−sD， sD=1+2d+log_M3。              (7)

乘θ是Lipschitz常数≤1，不放大δ-cover；θ=0也只加一个点。选m、d、a满足a<d及2d+log_M3<1，即得固定sD<2。原γ、κ都是fixed正数，原B仍near-full1、F仍uniform Lip／SM／coarseline escape，未通过角集中来伪造低维D。

## 6. 任意保留／重加权也不能免费成为二维Frostman

记Δ=2−sD>0。任何非零子measure的pushforward support仍在(7)的全support内，故甚至不需要domination：若一个normalized probability τ在该support上声称

    τ(B(x,q))≤δ^−h q^(2−ζ)， q≥δ，

取(7)的δ-cover求和，得1≤Cδ^(Δ−ζ−h)。对fixed 0≤ζ<Δ、h<Δ−ζ及δ充分小矛盾。特别不能保任意subpowermass后以subpower常数取得2−ζ Frostman；选择哪个time/angle labels或重新赋权都不能新增support。

若用未归一化measure τ、质量≥δ^h，并要求同一个absolute upper δ^−h q^(2−ζ)，则覆盖给δ^h≤Cδ^(Δ−ζ−h)，在2h<Δ−ζ时同样矛盾。原0≤g≤1、任意密图删选是这个结论的子类。这里的g只指parameter law上的选择；本稿没有另构造承载集A使a+D落同一个A⁺，不能把g≡1冒称完整translation incidence图。

## 7. 对正面slab门槛的核对责任

低二维cover不反“每个nonzero offset slab有fixed-power upper”。事实上(4)使单time片不能直接给subpower空间line；Q的global support可以是许多arcs，所有单slab仍轻。这正区分line非集中与二维Frostman，后者不能由前者／Jacobian rank升级。

nearzero门槛还必须保原g。一个可用charged结构是：原edge massD0，并假D0≥C Kt r，使g0=D0/(C Kt)≥r（固定常数留足余量）；按time interval cap删|t−s|<g0只损固定比例。若D0不足这个floor，不声称同一删选结论。|ℓQ|≤ε则H=ℓu满足|H(t)−H(s)|≤ε/g0。按H值宽w=Cε/g0分bins，三邻bin clusters Bk覆盖所有剩余edge。令e_k为原g在Bk²的absolute mass，有Σe_k≥cD0及Σ√e_k≤Σν(Bk)≤3，于是某e_k≥cD0²。两端time都在同一coarse line片且保原图质量，而不是只有一个anchor的neighbors被重新称dense。line宽为O(ε/g0)，若远大working r，R16已证O(r)稳定版本不自动适用，需另付coarsening及原A/outputratio；本文不作这个跃迁。root/A正面主稿另独审，不把本段当全部source排除。

## 8. 真实收益、scope与停止

本反攻比R27的任意数字D模型严格多保真实F(t)−F(s)、同一原times及原angle-difference先验；也保fixed all-real SM、真1AD和所有指定coarse spatial line逃逸。它给standalone secant law→二维Frostman预处理的严格否定，不是common-kernel source反例。原T的joint4-AD／CW、horizontal grains、ξ coherence、原A tubeKT及relative output/input比都未由此构造，不能登记为Kakeya反例或高维维数界。

主目标仍是实际原A-D耦合或另一条完整高维关键路径。两维Frostman并非ellipse容量的必要条件，不能以(7)关闭所有capacity或common-kernel策略；也不能再添加“D有2Fst”公设冒推进。按本轮spec在完成slab门槛与此有限counter后停止，不续平台数／d／m阈值。已实际全文读root10／A11／B8／macro6／next6／spec7，正式独审另存research/reviews/R0058_geometry_and_quantifiers_review.md；本B稿不把自审计为独审。Goal active。
