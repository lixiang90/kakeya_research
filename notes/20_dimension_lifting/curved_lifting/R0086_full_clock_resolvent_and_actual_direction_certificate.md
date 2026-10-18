# R0086：Du压缩的全时提升资格与真实方向证书

2026-10-18，root。自包含的有限维代数与原构造检验；独立审查见本轮正式稿。未经外部同行评审。不是一般Kakeya证明、反例或重大结果；沿用R50变分方法，不新立数学ID。

## 1. 全部量词和源对象

Du arXiv2610.05404v1的原曲线族为

    X(w,t;p,q)=(w1−tp−t²(q+p²/2)−t³p, w2−tq−t²p).

本证书排除：任意有限s≥0，在有内点的w∈R²、y=(p,q)∈R²、ρ∈R^s及任意非退化时间区间I上，存在smooth π_t:R^(2+s)→R²、a(y,w,ρ)、Θ(y,ρ)，π为空间submersion，满足所有参数和全部t的

    π_t(a(y,w,ρ)+tΘ(y,ρ))=X(w,t;y),
    rank D_(y,ρ)Θ=2+s.                                  (1)

这是Nadjimzadah2609.06299 Def2.1的原clock、零方向损失(s,0)类。Θ独立w不可省。允许a非线性、π任意smooth，不假设affineπ。否定不覆盖换clock、只有一个rough selector w(y)、少ρ或不同目标family。

## 2. 同一固定点的全时变分

假定(1)，固定同一个内参数点P=(p0,q0,w0,ρ0)，m=2+s，令

    T(t)=D_zπ_t(a(P)+tΘ(P)), W=a_w(P),
    J=D_(y,ρ)Θ(P), C=a_(y,ρ)(P)J^−1,
    B=[I2 0]J^−1.

矩阵尺寸为T:2×m，W:m×2，J,C:m×m，B:2×m。由方向rank，J可逆。关于w、y、ρ分别微分，且所有常矩阵均取同一个P，得

    T(t)W=I2,
    T(t)[a_(y,ρ)(P)+tJ]=[F(t) 0],
    T(t)(C+tIm)=F(t)B,                                (2)

其中

    F(t)=D_yX(P,t)=−t [[1+p0t+t²,t],[t,1]].

这只是R50同参数点变分的应用，不要求目标X对y全局线性：此处仅把实际D_yX取在固定P。π的T(t)本身不需有理或解析。

## 3. 有理必要性与矛盾

det(C+tIm)是首一m次多项式，非零；detF=t²(1+p0t)，亦非零多项式。在I内去掉有限个零点后仍有非空开区间。由(2)，在那里

    F(t)^−1 = B(C+tIm)^−1W.                            (3)

右边的每个entry是有理函数，而且在实t→∞时为O(1/t)，因为(C+tI)^−1=t^−1(I+t^−1C)^−1。左边也是明确的有理函数；两边在开区间相等，清分母所得多项式恒零，故可比较这两个有理函数的无穷远行为。这不把原π、原曲线参数域或原几何线段延拓到无穷远。

直接求逆得

    F(t)^−1=−1/[t(1+p0t)] [[1,−t],[−t,1+p0t+t²]].       (4)

若p0≠0，entry22趋−1/p0≠0；若p0=0，entry22=−t−1/t。二者均非O(1/t)，与(3)矛盾。于是全部有限s的(1)不可能。不依赖高维Kakeya猜想或Du维数下界，也不是仅某个低余维ansatz失败。

## 4. 原紧集合、真实直线和低维上界

源中Q由二进制e_j,f_j的x=Σ2^−je_j、y=Σ2^−jf_j、z=Σ_(i<j)2^−i−je_if_j组成，Qs=(p,a,b)=(s(x−1/2),s(y−1/2),s²(z−y/2))，固定s=4ε、ε=1/100。E={(−a,b,p,a−p²/2):(p,a,b)∈Qs}，其(p,q)投影覆盖小球，但E不是full open(w,p,q)。

源Ψ(x1,x2,t)=(−x1/(1+t²),x2−tx1/(1+t²),t)把这个所选E的曲线精确映为

    l_(p,a,b)(t)=(a+tp,b+t p²/2,t), |t|≤ε.

在有关紧集Ψ及逆均Lipschitz。上述显式标签线段的实际方向为normalize(p,p²/2,1)，只有一参数；q和a并未增加这些线段的斜率。这不分类K′中所有偶然附加直线段，§5的矩形本身就有额外线段。固定prefix n后，r=2^−n，Q的piece为(x0+rx′,y0+ry′,z0+rx0y′+r²z′)，4^n片，diam≤Cr，故Q、Qs、E的Hausdorff/packing/upper-box均为2。原直线并K′每片处于1×R×R²盒，R=s2^−n；每盒在R²精度需O(R^−3)球，共O(R^−5)。相邻精度比4有界，故这是所有小尺度upper-box≤5/2，并给Hausdorff≤5/2，而非只有一列覆盖。

源的等号Hausdorff=5/2还调用其[3]的coney restricted projection定理。该高级wholeproof本轮不独立重证；本证书否定lift及方向资格不使用这个下界，不能用metadata核验充作它的证明。

## 5. 原矩形使独立旋转completion有正体积

取Q里e1=1、e_(j>1)=0，f1=0、其余f任意，则x=1/2、0≤y≤1/2、z=y/2。于是p=0、b=0、a∈[−s/2,0]，所以K′真实包含矩形

    {(a,0,t): −s/2≤a≤0, |t|≤ε}.                       (5)

若把同一个K′绕t轴作所有φ∈任意非空开角区间的独立旋转并，(5)产生有非零径向宽度、非零角宽度、非零t长度的扇柱，三维Lebesgue体积严格正。乘任意有内点的(n−3)维固定盒，其n维体积也严格正。因此这种独立旋转并不能保留原strict低维上界；不是只因一个粗上界超过n就宣称不可能。

原K′直接乘(n−3)维盒确有upper-box≤n−1/2，但得到的明显直线方向只有normalize(p,p²/2,1,u)，u∈R^(n−3)，像维数≤n−2。需要至少另付方向参数，不能把这个proper族叫普通Kakeya反例。上述旋转反攻只排独立旋转并，不排所有依赖参数选择、不同构造或其它映射。

## 6. restriction、shading及原输入强度

删选原E标签只能缩小真实方向像，不能增加满方向；(1)的局部open restriction仍受§2–3排除，但只剩rough selector时已经不满足其fullw输入。保留每条完整曲线包含全部clock；删shading后，不论逐管或平均密度为正，都不能据此恢复每个方向的完整单位段。

逐管density≥λ能推出原平均≥λ，反向不成立；本轮源的集合维数构造不是对任意λ、任意权、任意marks的uniform有限估计，也没有新的平均shading闭包。时间区间长度2ε固定，若真有满方向直段，整体固定缩放可给unit长度，但固定缩放不能增加方向维数。§2–3否定不需要任何shading密度，不能升级成所有多尺度管族的体积下界。

## 7. 与已有输入的双向关系

2609 Proposition2.2的方向是：合格(s,ν)-lift加相应高维直线下界，推出曲线下界d_Kak(X)≥d_lin(3+s−ν)−s。它不保证每个曲线族存在零损失lift；若确有ν0，低维曲线压缩才能通过inverse image给高维反例，这个充分性入口在§3对当前原clock/full族已被排除。

‘无零损失lift’不等于无lift。A给出的合法(3,1)校准为ρ=(r1,r2,r3)，

    π_t(z)=(z1+t z3+t²z5,z2+t z4),
    a=(w1,w2,−p−r1,−q−r2,−q−p²/2−r3),
    Θ=(r1,r2,r3,−p,−p).

直接代入a+tΘ给原X，π前两列是I2，方向Jacobian rank4，故s3、ν1。将原R6直线丢z5，R5方向(r1,r2,r3,−p,1)满一个open角域，但原维数上界2.5+s=5.5超过effective ambient5。更强地，对同一原E的§5矩形p=b=0、q=a，这个投影的实体点为

    (−a+t r1, t r2, −r1+t r3, −a−r2, t).

固定t≠0时，(a,r1,r2,r3)到前四坐标的线性Jacobian determinant绝对值为|t|³；也可依次由第2、4、1、3坐标恢复r2、a、r1、r3。取原a区间内部、ρ内点和I内非零t，inverse function theorem给真实open subset，故这一个具体R5 full方向patch构造实际有正五维体积。这不是否定所有有损lift或所有更小fiber子集。

普通三维diffeomorphismΨ只直线化同一个受限E，完全不等于Def2.1要求的fullw与fullρ共同ruling。R50原parameter-linear存在性分类不自动覆盖当前全非线性y目标；但其一次变分法实际足够得到§3的必要条件。因此只登记旧方法的实际应用，不新开‘任意codimension’方向，不据此宣对一切lift不可能。

## 8. 来源、独审与停止

root本轮实际读Du官方abs/history、全文HTML和原PDF1–5 text，render/view physical2–3。原PDF有Date October6字样、arXiv v1提交October4；分别记录而不改原始字节。R81已完整读过HTML，R86是原PDF首次归档和逐步独审，不能称新版本或首次阅读全文。

源完整显式构造、§3提升否定、§5独立旋转校准各有明确范围；formal实际审查后才可标内部reviewed，非外部同行。本轮没有新gain Phase II、普通n≥5界或full-direction反例。此source作为ordinary反例入口停止，不续clock/rotation/ambient模板；全目标下一需不同实际输入，状态可保留无合格候选，Goal active。
