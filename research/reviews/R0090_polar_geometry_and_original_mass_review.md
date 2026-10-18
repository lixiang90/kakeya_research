# R0090：polar几何与原质量的独立终审

2026-10-18，A。恰六个编号二级节。以下只在实际全文与明列的有限范围内内部审查，未经外部同行评审；不认证未来元数据、Git或同步。

## 1. 实际全文、源读域与独审分工

已fresh实际全文读取最终root《R0090_polar_hyperplane_completion_and_endpoint_closure》十节、A/B两个gate各八节、reselection_spec五节、working_spec五节、终macro六节、next六节和source scope六节。发现root§8有限轴并／连续族的字面问题后，已再次实际全文读回修后的root十节及macro六节；并非只据旧版审查记录写通过。

本轮本人实际读WZ本地Def3.1–3.9、Def17.1–17.4/Remark17.1、19.4相关完整计算与19.5证明，并全文核R76/R78原归约和R80旧质量责任。Csörnyei–Stull2609.38742v1本人实际打开Th1.1/1.3及§2.1声明／定义；root/B的§3–4.1证明、PDF视觉和字节记录不冒记为本人完成。没有新审其全33页算法／距离集或外部高级wholeproof。

A自身polar施工不算自身独审，已由root/B独核。本formal重点独审root完整有限归约、B的原质量／端点闭包与root新增校准；接受完整Def17为来源输入，不将该应用写成源wholeproof新认证。

## 2. 原E、原N/I与删选闭包

root§3的relative4-Frostman上界可直接逐slice核：固定t时physical r-ball令x在Cr-ball、native y=z−F_tx在某Cr-ball；其中心可随t变，但原Y_t的AD upper对任意中心统一。因此每slice至多K^C(r/δ)^3点，再乘δ-separated Z在r-interval内至多Cr/δ个times，得#E∩B_r≤K^C(r/δ)^4。总数下界由完整Y_t和filled X及Z给#E≥K^-Cδ^-4。A/B若用allowed上邻处理F漂移并付K^C也成立，但该更保守步骤不是root简证的隐藏缺口。

原Φ1-AD给每point约K^±Cδ^-1个细角；每角取一根真实witness，dyadic管的同point／同角δ-bin重复只付固定或K^C重数。由此原selected tube-point访问I_*≈K^±Cδ^-1#E，与原N≈K^±Cδ^-4保在各自分母。取固定比例points及同一normal chart仍保K^-C原访问，不把新增PH边数当原I_*。

这一点集是实际source的有限E，不是ordinary反设的Lebesgue并；不能由普通小体积免费得到。删point、角或normal边没有生成新完整source，未改Z/F/newallowed。Whole-label restriction保已有逐管marks，但会改normalized CW及ADlower；本轮normal trim不授每原T逐管保相同比例。平均nearfull、重管子族和逐pair／逐H密度分别处理，未赠条件角独立。

## 3. 双band、真实全局H及统一M

固定p的φ映到归一真实方向(φ,ξ_p+F_tφ,1)，bounded chart与末坐标1使之定量双Lipschitz，Oδ误差只改常数；原角law因此为relative1-Frostman。其方向在同一固定hemisphere，projective角与差距比较有统一常数。

独核root§4：单band面积≈δ，双band面积≤Cδ²/(|v∧v′|+δ)。乘δ^-2并以1-Frostman作dyadic annuli求和，含最细对角，得∫f_p²≤K^C log(2/δ)，而∫f_p≈1。令A=C K^C log，删f_p>A只损一个小常数的f_p-mass，所以剩support面积≥c/A，覆盖至少cδ^-4/A个不同normal cells。这是criticalκ1的真原角计算，不把filled X添成point正常量维数，也未声κ<1的多尺度推广。

root§5的H来自同一根原axis的全部正交法向，保持同一全局完成族。band normal可投到真实v_T⊥只动Oδ；bounded intercept使offset亦只动Oδ。p距axis Oδ时用固定相邻参数cells H^+，给source的真实cube incidence。去重、有限charts和padding仅固定成本，没有把weights复制成不同hyperplanes。

对每point保不同normal bins，offset由normal和该point确定至Oδ；参数r-ball内至多C(r/δ)^4个候选。故任取统一M=floor(cδ^-4/A)个，确得relative4-Frostman常数≤CA。先按最富chart分point保固定比例，再确定选M，得到同一bounded chart、同一个M及仍合法的点law。先定source输出损失、再把原η取小，K/log可落入新定理要求；不需另假ADlower或随机独立sampling。

## 4. 新primary端点、二点CS和未付四维出口

实际Th1.1要求s严格大于d−2、point relative t-Frostman、每point同M个relative s-Frostman超平面，计的是去重后的几何参数cells。这里d5、s=t4由上一节合法供应；标准line dual为3-flat或法向直接取v且随clock换offset的旧编码失败，不被拿来否定这个polar编码。

但新定理只给δ^-1+ε M的端点。独核root§6／B的替代证明：两个point cubes距离r，共同δ-hyperplane cells至多Cδ^-3/(r+δ)，由normal薄band和每normal固定个offset cells得出。原点4-Frostman使Σ_(p,q)(|p−q|+δ)^-1≤K^C|P|²，p=q项由#P≥K^-Cδ^-4亦可吸收。真实PH图有|P|M条边，故

    Σ_H d_H²≤K^Cδ^-3|P|²，
    #H^+≥cM²δ³/K^C≥cδ^-5/(K^C log²(2/δ))。

所以在本输入的正幂端点，原二点/Fubini和CS已经足够；没有新增高维growth，也不否新定理其它指数区间的内容。

root§7仍以原全N计每根T的S3 polar族，Σ_H#T_H≤CNδ^-3，与ambient #H≤Cδ^-5一致。H近满五参数只使自然均度预算约K^Cδ^-2，不授R4方向cap、全三参数方向网、原marks／unit clock、归一CW或体积回传；稀疏DIR也必须保真实条数和密度，不能从很多H免费取得满四维阴影。此账本不证明不存在少量异常富H，只说明本链未提取到可调用的原质量。

## 5. 新a(v)=v²校准的独立核算及已修必修项

令v在固定有界四维盒中，a(v)=(v1²,…,v4²)，轴为(a(v)+tv,t)。v的Cδ网（或固定着色）给真实δ方向分离和N≈δ^-4，joint参数为光滑bi-Lipschitz四维graph。超平面x1+b2x2+b3x3+b4x4+ct=h包含轴当且仅当

    c=−v1−b2v2−b3v3−b4v4，
    h=v1²+b2v2²+b3v3²+b4v4²。

在指定b2≈1、b3/b4≈0且v1/v2处于两个固定分离interval的子patch，Jac_(v1,v2)(c,h)=2b2(v1−v2)有固定lower。连同三个b自由参数得到真实五维submersion，故该子chart polar参数有≈δ^-5个cells。固定其中一个H及(v3,v4)网点，先由c消一个变量，再用导数离0的二次式／有限inverse chart，Oδ残差仅容O1个(v1,v2)网点，所以其tube数≤Cδ^-2。此upper严格限所选子chart，不声全部polar H均如此；其它退化normal可能富得多。

正式审查指出的唯一字面必修已修并读回：有限δ网的axes并本身是零测，不能写它有正五维体积。底层连续v盒的axis map有Jacobian∏j(2vj+t)，在非零处含open5。对有限δ网的roundδtubes，另取固定内部t区间及缩小v盒，使各2vj+t离0；每slice map统一双Lipschitz，δ-balls重叠O1，Nδ4≈1给slice四维体积≥c，再沿t积分，确得δ无关的五维体积lower。root§8和macro§4现在明确区分两者。

该族未构造完整pointΦ1-AD或critical E，也未给full方向低维集合。它只校准H参数满5并不单凭计数迫所选H有三维管纤维，不能作完整Def17或Kakeya反例。

## 6. 最终有限判定、宏观与冻结

上述终稿全文在明列的有限范围内通过；唯一字面必修已修复，无未解决强制项。通过的是完整sourceκ1的polar原质量转换、去重／同M／relative4-law、二点端点闭包、原TH预算及限定子chart校准，不是完整κ1排除或ordinary/general新结论；完整κ1仍未证未否。

已实际全文核终macro六节、next六节及source六节，并重读macro的体积修订：四完整路径和ordinary初始化责任保持；本次polar→超平面端点→R4直接桥停止，不续κ、normal厚度、M、richH假设或旧跨块／更多锚点。阶段gate中的streak12是开轮历史，最终保守ordinary/fullbranch-saving时钟为13；实际输入资格信息不当branch-saving。当前无qualified下一gain主命题。

无newID、major、ordinary新界、完整branch-saving或full方向反例，Goal active，未经外部同行评审。A自己的正证由root/B独审，本稿对root/B的核算不替代该分工。新来源全33页高级wholeproof、未亲自核的PDF/metadata身份及未来提交／同步均不在本人认证范围；完成本formal后按授权冻结，不再编辑检索。
