# R0065先写规格：有理曲率与实际输出图

2026-10-18。父364a374d419bb29c90ec157ebcdfdba644645a20/tree285ec5ff27844a82bee5cc9b93163a7d705fcdf0、977tracked clean，R64 receipt全部通过且fresh remote相同。context.py已重定向tmp/R0065_context.txt；GOAL/STATE/ROADMAP/78状态/最近round/macro/next已读。上一轮归progress，Goal active，普通高维/major未达。未经外部同行评审。

## 1. 当前缺口和不同输入

R64 raw分类不适用于只控制g边；其双曲线反例未保原A-output。本轮唯一主任务是给固定复杂度的真实双时间平移证明有费用的output-incidence上界，检查R64双曲线是否因此不能完成低维输出图。不能把该额外regularity假设授给原source，也不重开raw分类常数、fixed arms、stationarity或standalone arbitrary-Lip D2Fst。

## 2. 正式有限命题

固定D>=1、M>=2、gamma∈(0,1]、kappa∈(0,2]、输出误差常数C0。F(t)=P(t)/Q(t)，t∈[-1,1]；P为2×2实多项式矩阵，Q为标量多项式，degree<=D，coefficients绝对值<=M，|Q(t)|>=1/M。可允许delta/r-dependent coefficients；但D、M固定。原时间概率nu满足每interval I的nu(I)<=K(|I|+r)，K>=1。原向量标签概率pi不去重，|psi|<=M，所有宽w>=r的slab质量<=K w^gamma。sigma为任意原输入y概率；g(y,t,s,omega)∈[0,1]可任意相关。

令Tpsi(t,s)=(t-s)(F(t)-F(s))psi，Jpsi=det(∂tTpsi,∂sTpsi)。采用固定多项式表达Jpsi=N(t,s;psi)/[Q(t)^3Q(s)^3]，N关于psi为homogeneous quadratic，time degree以d=6D+4作统一上限。假设N的某个t,s monomial系数作为psi二次型有coefficient maxnorm>=lambda，lambda>=r^theta，0<theta<min(1/6,kappa/6)。

设Aplus在R²中可由最多K r^(-2+kappa)个r-balls覆盖；每个g>0 tuple满足dist(y+Tpsi(t,s),Aplus)<=C0 r。检验能否统一证明

    integral g <= C[D,M,C0] (K r^(theta gamma/2)
                    +K² r^(theta/(2d))+K³ r^(kappa-3theta)).

若K<=r^-h、g质量>=r^h且h足够小，则不得共存。任何指数或分母有误须明修，不能先登记通过。

## 3. 证明责任、source和反同义检查

须实际证明angular homogeneous quadratic sublevel被最多两条width O(sqrt(tau)) slab覆盖、二维polynomial sublevel上界、原nu在尺度r的合法smearing、good-J推前小球上界及regular fiber multiplicity。不能用连续Lebesgue密度替原离散nu或把J积分当union体积；角law只slab非2D体积。所有g相关性保持，丢坏参数从原product reference收费，输出card用于每个原y。

R16只已付linewise；R58 arbitrary-Lip plateau使普遍D2Fst失败。本轮额外有理格式和量化N系数是可反攻的新输入，不声source可提取。restriction到任意bounded shading仅改g，时间/角归一删选分别收费，不授AD lower；也写反向为何不能从本界推出普通完整Kakeya正幂gain。实际原L图如能被O(r)有理模型近似则只追加O(r)输出误差；F的normal/time单位必须与R16一致。

## 4. 独立测试和停止

具体检验R64 rational two-branch hyperbola（cross rectangle分别有有理式、非单一全域曲线），核J系数是否为固定正量；near-zero翻译/critical curves必须收费，不可声整个raw law有2-Frostman。也测试F=pencil/common-image使N恒0、direction concentrated onzero line和time原子/低维输入破坏假设，以免把nondegenerate前提忘掉。

A只编辑notes/00_map/R0065_rational_curvature_source_audit.md，负责源接口/旧闭包/独立证明检查；B只编辑notes/00_map/R0065_rational_curvature_counteraudit.md，负责有限离散反攻、J/critical集合和具体双曲线。最多两代理不Git。root主稿/整合/最终formal及同步。完成定理或严格反攻及source限界后即停；不续D/M/theta/h阈值，不认证major/首创，不以subclass代总Goal。周期macroR66，关键失败提前。

## 5. 双分支chart的先写补充

为了严格检验R64，不将其piecewise F误称一个全域P/Q。同步检验固定intervals I1,I2⊂[-1,1]、长度>=1/M上分别F1=P1/Q1与F2=P2/Q2的矩形版本；两原time概率nu1,nu2各有同样interval cap，T=(t-s)(F1(t)-F2(s))psi，Jac分母Q1(t)^3Q2(s)^3，numerator同degree上限d。系数与denominator控制仅需在对应interval及固定小扩展。theta/J下界及结论同§2，常数可依D/M。需实际支付restriction mass与chart rescaling，不声任意δ-dependent tiny chart免费固定长度。原同F版本仍为special case；此补充在证明前锁定，用于R64两个固定半单位interval。
