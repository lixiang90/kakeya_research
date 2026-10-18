# R0075阶段II：global近kernel粗商、原权CW与四维三维基线

2026-10-18，B。仅编辑本授权稿，不Git、spawn或元数据。实际全文读已锁R75spec§2；本稿负责近kernel最终出口及weighted normalized CW转经典基线，并独立反攻fine／sameT rawclock。没有先假商AD lower、physical方向分离或完整κ1结论；内部逐步审查不等于外部同行评审。

## 1. 完整对象、依赖和本稿目标

固定ζ>0、κ∈[1+ζ,2]、原γ>0，η最后小、δ最后。保完整bounded WZ Def17.2–17.4 d5／k=ell3的原T joint4AD/CW、原N≈_Kδ^-4、Z、Y_t AD(2−κ)、filled X、pointΦ ADκ／slab、selected ξ及coherence。K记δ^-Cη固定幂，不把正δ幂塞入K。

设上游已在whole-time集W保 `#W≥K^-C#Z`，原层数据和原全T不换。raw分类给同一固定近kernel形式

    ||F_t−F0−u(t)e^T||≤ε_F≤Cδ^c0， t∈W，           (1)

其中e为固定unit、F0/u有固定上界、c0>0先于η固定；近常可并入u=0。源是否真给此形式由root/A付。本稿证明在这些**global原clock**条件下，κ≥1+ζ与原CW矛盾。不是长度ρ局窗，无额外ρ固定幂密度成本。

具名经典输入为Zahl survey2512.09397v1 §2 Definition2.1、Theorem2.2所述Wolff估计：R4半径r的unit tubes满足绝对Katz–Tao convex Wolff axioms、常数为固定L时，对任意ε>0，

    ||Σ_P 1_P||_(3/2)≤C_(ε,L) r^(−1/3−ε)。          (2)

原文明确不需方向分离；本稿实际读本地提取前190行相应statement及上下文，whole Wolff深层证明仍具名。下面通过undersampling使L固定，避免假定(2)对δ-dependent CW常数有未核polynomial dependence。

## 2. 原whole-time限制后重计marks，不借单管旧密度

原每t∈W的全空间层有 `#E_t≈_Kδ^(−4+κ)`，每point原Φ供应 `D0≈_Kδ^-κ` 个fine witnesses。因此全层重计 `I_W≥K^-C#W δ^-4≥K^-Cδ^-5`。fixed tube/time只有O(1)实际点／fine角碰撞，取canonical visit仍保固定比例。原N≈_Kδ^-4，故原平均visits每管至少K^-Cδ^-1。

先tube-heavy：删访问少于固定倍该平均的原管，保总I固定比例；余H的原概率p≥K^-C，每根原管保全部W-visits且至少K^-Cδ^-1个。以下ν=Uniform(H)，其原whole-tube CW常数最多K/p≤K^C；原分母损失已经支付，不将ν偷称原全T概率。

没有假whole-time restriction自动保每根原管旧density，更没有在raw分类后继续使用旧q图。重计只需原层和原witness供应；H的pointΦ不被授新的AD lower，最终仅用真实原marks。

## 3. 固定线性商与global coarse footprint

用固定orthogonal horizontal变换将e变e1，再共同物理shear减F0；它们有固定norm／Jacobian费用。写x=(x1,x2)，则原marked点在新坐标为

    (x1,x2, y+u(t)x1+R_t x,t)， |R_t|≤ε_F， y∈Y_t。 (3)

左侧normal坐标若旋转，Y_t一并旋转，其各尺度球cover只改固定常数。令π删x2、保(x1,normal2,t)，是R5→R4的固定线性商，不依point／time。选r=δ^s，s>0固定且s<c0/2，并取原allowed上邻尺度；可令

    δ^s≤r≤Cδ^(s−Cη)， δ+ε_F≪r。                  (4)

上邻若采用newallowed子格，其尺度步长为δ^Oη，同样只付K。若坚持某非allowed r，取R∈[r,K r]为原allowed上邻，先算N_R再乘(R/r)^4；额外至多K^κ，仍只K固定幂。

在长r的原dyadic clock窗J里，Definition17.2的原跨time条件给 `N_r(∪_(t∈Z∩J)Y_t)≤K r^(−2+κ)`；W的子并只继承此upper，不假AD lower。取实际t_J∈W∩J，u取F_t−F0的第一column，故原dyadicLip给 `|u(t)−u(t_J)|≤Cr`。于是该窗内(3)投影点以至多

    K r^-1 r^(−2+κ)=K r^(−3+κ)

个Cr-cells覆盖：x1贡献r^-1、normal Y贡献r^(−2+κ)，clock只一个格。共至多C/r个窗，因此

    N_r(π E_W)≤K^C r^(−4+κ)，
    |N_(Cr)(π E_W)|≤K^C r^κ。                       (5)

误差R_t x已由ε_F≪r支付；使用global各尺度Y并与F的dyadicLip，而非把fine Y数直接乘clock／horizontal数。未在局窗赋新global配置。

## 4. 原whole管投影、proxy及真实coarse shadings

每根H原管的π-image保原clock，轴长介于两个固定常数，斜率bounded。取bounded六参数r-net并以固定倍radius外罩，赋给一个proxy，包含完整projected原管及原marked点周围cr-balls；net规模O(r^-6)。共同fixed homothety后，旧完整轴段长度≤1/2且≥c>0，沿同一轴延成unit segment，用共同半径≈r的standard tube P_i外罩。保固定端部margin，故原端帽附近的coarse markballs仍在P_i内，无需删端点。

若P_i⊂凸U，则完整原projected T_i⊂固定inverse-image U。原H管在被删kernel coordinate上有固定bounded范围，故原完整T_i包含于相应bounded convex prism，体积≤C|U|。因此原indexed probability pushforward满足

    ν{i:P_i⊂U}≤K^C|U|。                            (6)

proxy若只按近轴外罩而未包整个fine projection，改用U+B_(Cr)；所有short axes≥r的box测试体积仍只变固定倍。这里不要求projection去重后uniform，重复仍按原ν权重。

每个H管至少K^-Cδ^-1个原δ-time visits，每r-time bin最多Cr/δ个，所以有至少K^-Cr^-1个distinct coarse levels；有限颜色取相隔Cr的一组仍保固定比例。对其实际π-marked points取cr-balls作为Y_i^r⊂P_i，则

    |Y_i^r|≥K^-C r³，
    ∪_i Y_i^r⊂N_(Cr)(π E_W)。                       (7)

所有balls来自真实selected visits，只为合法粗管shading增厚；(5)已支付此增厚footprint。它们不被称作原fine新points或新完整Def17配置。由(6)(7)已得weighted normalized-CW及nearfull coarse marks；无商3AD lower、无physical方向分离。

## 5. 可重复原weights的有限convex测试net

以下helper固定bounded R4 tube chart：有限indexed unit r-tubes P_i、概率ν_i任意，允许完全重复或极小权；假对所有convex U有 `ν{P_i⊂U}≤K0|U|`，平均density `Σν_i |Y_i|/|P_i|≥λ`，Y_i⊂P_i任意可测。所有P_i位于固定ball，无须参数分离。

任意包含某P_i的convex U可先与固定ball相交，再用John外box B覆盖，体积≤C|U|、轴长bounded、各short axis≥cr。空／零体积查询不含tube。orientation与center以cr精度离散，side lengths取dyadic并加固定margin，可由至多r^-D个固定D的boxes Q外罩全部这种B，且 `B⊂Q、|Q|≤C|B|`。故同时控制所有Q就控制任意convex U。

若Q确含unit r-tube，则 `u_Q=|Q|r^-3≥c>0`；不含任何tube的Q之count恒0，不在小体积端错误加一。ν(Q)≤C K0|Q|，rounding邻域若需要也只固定倍，因short axes≥cr。该net不由原#index或最小权决定，故没有weight跨度／support-size费用。

## 6. Undersampling得到固定KT常数并保平均marks

固定小a>0，令 `M=floor(r^(−3+a))`，独立按原ν有放回抽样M个indices。假 `K0≤r^(−a/2)`，可把固定前因子并入更小r阈值。对每个上述Q，binomial变量X_Q的均值满足

    EX_Q≤C r^(a/2) u_Q。

对固定L充分大、Lu_Q≥2，Chernoff给

    Pr{X_Q>L u_Q}≤(C r^(a/2)/L)^(L u_Q)
                    ≤r^(c a L)。

选择L≫D/a及所需固定失败幂，union bound使全部r^-D个测试以1−o(1)概率满足 `X_Q≤L|Q|r^-3`。L依固定a／维数，不依r或原K0。因此sample indexed family满足**固定常数**KT convex Wolff，不是带r^-η常数直接冒用(2)。

令Z_i=|Y_i|/|P_i|∈[0,1]，实际平均λ0≥λ。独立sample的Z和有方差≤Mλ0，Chebyshev给 `Pr{ΣZ_i<Mλ0/2}≤4/(Mλ0)`。只要 `Mλ→∞`，和KT同时成功的sample存在。应用中λ≥K^-C≥r^v、v先足小，故此条件成立。这一步保的是任意原weights和平均marks，不需要每根原管等密；本源的(7)另已给逐管下界。

同一个proxy重复出现的次数≤CL：取其containing constant-radius box，体积≈r³，KT查询即给该上界。合并重复P并将其shadings取并，每个几何tube至多CL份，所以合并后总shading mass至少sample总量的1/(CL)。所得真实set仍满足固定KT上界，且

    Σ_(distinct P)|Y(P)|≥c_(a) λ M r³≥c_(a)λ r^a。 (8)

不要求去重family uniform概率等于原pushforward；这里只把实际(8)交给绝对KT定理。源总footprint不增，近重合而非完全相同的tubes也由相同小box控制，不偷用方向分离。

## 7. Wolff基线的实际weighted／average读出

对上述sample set用(2)，写f=Σ_P1_P、U=∪_P Y(P)。由(8)和Hölder，

    c λ r^a≤Σ|Y(P)|≤∫_U f≤|U|^(1/3)||f||_(3/2)
                         ≤C_(ε,a)|U|^(1/3)r^(−1/3−ε)。

所以原整个indexed shading union（包含此sample union）满足

    |∪_i Y_i|≥c_(ε,a) λ³ r^(1+3a+3ε)。              (9)

这是normalized-CW probability到R4三维基线的完整有限转移，适用任意原weights／重复／平均λ，但明确需 `K0≤r^(−a/2)`、`Mλ→∞`。没有声任意tinyλ或维数4 fullunion。需要的常数L已经固定，故没有未核robust-K dependence；Wolffwholeproof依然具名。

给任意固定目标lossξ>0，先取a、ε、v很小且3a+3ε+3v<ξ，源η最后使K0≤r^-v及λ≥r^v，并令v<a/2；(9)给 `|∪Y_i|≥r^(1+ξ)`（r最后小吸固定常数）。这正是本global source所需的nearfull平均版，绝不等于强Wolff猜想的R4维数4。

## 8. 近kernel完整源出口与参数不循环

将第4节的indexed family交第5–7节，r由(4)是δ的固定正幂；原K=δ^-Cη可转成r^-C'η，因为logr/logδ≥s/2。先固定ζ及上游分类误差指数c0，取s<c0/2，再固定例如满足

    3a+3ε+4v<ζ， v<a/2

的小a／ε／v。最后η使全部finite原权／coarse／sampling费用K≤r^-v、λ≥r^v，δ最后小。lower(9)至少 `c r^(1+3a+3ε+3v)`，而(5)给upper≤`C r^(κ−v)`；κ≥1+ζ使指数严格分离，矛盾。

近常支归u=0同证。global W可以仅有δ^Cη的原clock比例，仍只是上述λ小幂；若换成固定ρ局窗，ρ密度成本会破此参数选择，不能照搬。本证从未赋原商AD3 lower、把R4 PW／CW fullunion4当输入、或在projection去重时重设原N。也未用κ=1；该点upper r^1与基线r^(1+o)没有矛盾。

因此**若上游在完整源、原质量及fine精度下付(1)，nearconstant／nearkernel的κ≥1+ζ分支已由本稿给出真实最终CW／volume矛盾**，不再止于准备报告。一般Mat2到该分类及common-image另一出口是root／A的不同责任；当前实际全文互审结论列在第9–10节，不把本节条件出口自身冒为穷尽。

## 9. 独立反攻fine bad-pair到原rawclock

已锁上游对象为实际sameT selected-visit图。对fixed(p,t,s)，真实native响应有完整baseline `y+(s−t)ξ_p+(F_t−F_s)x`，角系数D=(s−t)(F_t−F_s)。若sminD≥h，normal δ-output cell的φ原像为O(δ/h)-ball。原ADκ给≤K h^-κ个fine angles；native Y_s totalδ-cover≤Kδ^(−2+κ)，故per-root实际管数≤K h^-κδ^(−2+κ)，相对D0为 `K h^-κδ^(2κ−2)`。这使用完整Y cardinal，不是原slabγ被免费升κ，也未假det-large原g质量。

在全部root／times求和，预期bad sameT pair upper为 `K^C h^-κδ^(2κ−2)N m²`。重管平方供应≥K^-CNm²后，必须按真实n_T²加权选一重T*，而非把任意edge law称raw。其整Z_T*有≥K^-Cm个原times；坏det对在Uniform(Z_T*)²下的概率才可交R64。shortclock按该真实clock的intervalupper另付，并用bounded F将det(F_t−F_s)>ε、|t−s|>q推到sminD≥c qε；选择q／ε固定小δ幂时κ>1的saving可支付。

此检查指出R64cross-only g不等于真实clique-mixture；但PSD名称本身不保证选管，也不送mixing。现已实际全文独读root12／A12：root用原N上界作tube-heavy分母、按n_T²返回一根原T*的完整S²，短clock按该管真实δ-separated visits付K(δ^b+δ)，均与上述独算一致。whole-time保整层、跨time Y-union lower／upper和newallowed子格分别有来源；分类后的固定power误差进入(4)，未直用fineδ quotient。未见此上游fine计数或原质量返回的未解决必修。

## 10. 当前verdict、具名责任与停止线

本稿已给global近kernel的原粗footprint、真实coarse marks、convexprism保原权CW、finite convex net、undersampling／去重／平均marks、经典Wolff L3/2调用及最终κ>1矛盾。并非靠未付商AD lower，也不只是标准定理名字。有限sampling是存在性连续数学论证，不以有限数值试验代一般δ证明。

已fresh实际全文读root主稿12节、A阶段II12节（含all-real扩展的终版第8节）、本稿10节、working_spec5节、macro6节及next6节。非自推部分逐式独核包括原fine逆像、同管平方质量到GLOBAL rawclock、R64删除及whole-time闭包、近image的SM准备和R16真实working误差。A的第8节没有直接把原20.2的bounded Mat改称全real：fitspan先给||R||≤Cρ^-ε_SM，high branch给||R||≥ρ^ε0/3；原fit并内重取good-q／V／own-H，保留质量只在反设K_fit中收费。二次native输出的Δ≈ρ^(2+ε0/2)||R||、L≈ρ²||R||满足L<1和Δ≫δ（亦超过δ/ρ floor），R在KT比值中抵消。坏整窗删除不把ε_SM／a_B灌回最终K。此非自推接口在所列具名输入下通过，未见未解决必修。

依赖是原Def17各尺度结构／bounded规范、R64有限raw分类、R22闭包、R16 linewise／13.5、19.2／19.4／20.2实际tuple几何及经典Wolff Theorem2.2；本轮没有重新独证这些高级wholeproof。B的kernel主证由A／root独核，不能以本稿自审计独审。未经外部同行评审，不宣新ID、major、新颖性、ordinary n5或Goal完成。

若上游只有局部clock、κ1、无固定指数的近似或平均marksmass不足(7)，本出口仍不能使用；当前原证明给的是GLOBAL clock和固定δ^c误差，故在显式bounded原wholeT／N／CW规范的完整matrix33、κ≥1+ζ范围，两出口及原前提均已实际核到限定源矛盾。literal所有配置的Kd5(1)读出另需极值提取保该bounded规范，不能由localAD或bounded usedT自动推出。正式独审文件待授权后另写；不预认证未来元数据／Git／sync。κ1、ordinary初始化及Hausdorff仍open；停止更多κ／sampling阈值或额外smooth条件续轮。
