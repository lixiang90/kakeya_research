# R0088：实际锥面波包、原阴影与源范数预算

2026-10-18，A。按本轮working_spec五节的phaseII锁题独立施工；本文恰十个编号节，只检验指定R5→R6 cone packet/random-sign直接桥。不是新的Kakeya定理、反例或重大性声明，高级来源wholeproof仍具名，未经外部同行评审。

## 1. 实际primary、规范及被调用的量词

实际读Xiangyu Wang [arXiv2411.02961v8](https://arxiv.org/html/2411.02961v8) §1.1全部定量声明、§1.2开头和完整§2.1，并读root新存local extracted PDF1–6相同范围；history为v8=2026-09-30。未阅读／重证其全部29页递归proof，未作PDF渲染或独立文件bytes检查。原稿中的小参数δ另属其epsilon层级，不与下文原管尺度δ混同。

记cone extension为

    Ef(X,S)=∫ exp(i(X·ξ+S|ξ|)) f(ξ)dξ，1≤|ξ|≤2，ξ∈R5。

Th1.5/Prop1.7以n=6、2≤q≤p、2≤k≤4及源显式p,q分支条件为输入。本文仅具名调用Prop1.7：每εs>0，对所有此annulus内Schwartz f与A≥1，

    ||Ef||Lp(B_A)≤C A^εs ||f||2^(2/q)||f||∞^(1−2/q)。      (1)

n6的所有k限制保留，不把渐近Cor1.6当固定n6的主定理。Th1.5严格可用区间另给全空间Lq→Lp；对本文disjoint bump求和，它给相同幂预算。§2.1的long/mini directions是(−ω,1)、(ω,1)，本来就是plank而非round tube。以下直接构造正相位bump，故不需假标准分解的essential support就是精确support，也不调用RapDec消掉实际marks。

## 2. 原R5数据、真实clock与全端帽

固定R,C，0<δ≪1。原N条单位round δ管为

    Ti={x:dist(x,ai+[−1/2,1/2]vi)≤δ}⊂B_R，|vi|=1，

unoriented directions彼此Cδ分离，因而N≤C_Rδ^-4。任取可测Yi⊂Ti，E=∪Yi，I=Σ|Yi|，定义原平均密度λ̄=I/(N Vδ)，Vδ是同一unit round tube体积，cδ4≤Vδ≤Cδ4。逐管density≥λ只意味着λ̄≥λ，不替代后面的实际质量分母。

保未clamp的正交坐标

    ti(x)=(x−ai)·vi，zi(x)=x−ai−ti(x)vi。

对所有x∈Ti，|zi|≤δ且|ti|≤1/2+δ；这包括两个round端帽。即使Yi集中在端帽也不删去或当零测。方向vi任取一个orientation即可，原unoriented separation保证下面中心−vi的窄sector仍分离；无需原图为Cartesian、ADlower、PW或sticky。

## 3. 全径向带宽与三种物理尺度

令Rpacket=δ^-2，δ≤τ≤1，ρ0=3/2，ωi=−vi。取固定极小c1>0，在正交分解ξ=ρωi+η、η⊥ωi上定义非负smooth bump

    bi(ξ)=χ((ρ−ρ0)/(c1τ)) ψ(η/(c1δ))，0≤bi≤1，

其中χ、ψ固定、非零、紧支于单位球／区间。c1小使支持在1<|ξ|<2，并由原方向分离使各support不交（或固定着色后不交，常数无幂费用）。它们的频率体积

    Aδτ:=∫bi≈∫bi²≈δ4 τ。                             (2)

将物理Rpacket尺度缩回单位尺度，angular δ产生四个中轴δ，quadratic angular phase产生长轴1，radial τ产生mini轴

    r=Rpacket^-1 τ^-1=δ²/τ，δ²≤r≤δ。                   (3)

不是六维round δ管；τ=1时mini轴δ²最窄，τ=δ时才与中轴δ同级。这里的radial cutoff允许随δ变化，因为(1)对全部Schwartz输入统一，常数不依其导数大小或τ。

## 4. 模ulation与整根原管上的相位下界

设置fi(ξ)=exp(−iRpacket ai·ξ)bi(ξ)。对x=ai+tvi+z∈Ti，令S=t+h。扩展相位为

    Rpacket[(x−ai)·ξ+S|ξ|]
      =Rpacket ρ0h +Rpacket[h(ρ−ρ0)+z·η+S(|ξ|−ρ)]。

ρ≥1且|ξ|−ρ=|η|²/(|ξ|+ρ)，所以当|h|≤c2r时，后一方括号乘Rpacket的绝对值至多

    C(c2c1+c1+c1²)，

均匀于所有标签、τ和x（包括端帽）。先取c1、c2固定足小可使其<π/6。扣掉公共carrier phase exp(iRpacketρ0h)后积分实部≥c∫bi，因此

    |Efi(Rpacket x,Rpacket(ti(x)+h))|≥c Aδτ。            (4)

carrier phase本身可能很大，不能直接声整个积分的相位接近0；(4)用的是去掉同一packet公共相位后的正实部。不同packet间的相位不要求相同，后面由随机符号处理。原midpoints仅在modulation中出现，source常数不依它们。

## 5. 保原Lebesgue marks的label-specific提升

定义真实集合

    Si={(x,ti(x)+h):x∈Yi，|h|≤c2r}，Z=∪Si，M=Σ1Si。

映射(x,h)↦(x,ti(x)+h)是Jacobian为1的线性剪切，因此不论Yi多不规则，

    |Si|=2c2r|Yi|，∫M=2c2r I≈r λ̄ Nδ4。                (5)

原x坐标未改，且|ti(x)|≤1/2+δ、r≤δ，故

    Z⊂E×[−1,1]，|Z|≤2|E|。                              (6)

并集不是来自一个共同lift：不同标签ti(x)一般不同。在固定x处，Z的vertical fibre是多个不同中心的r区间之并；不能免费把(6)加强为|Z|≤Cr|E|。下文既不把NδE当E，也不对Yi进行未知平滑／填充，所有集合都是实际Lebesgue阴影。

## 6. Random signs、L²/L∞与六维缩放

取独立Rademacher signs εi，fε=Σεi fi。频率支持不交给精确预算

    ||fε||∞≤1，||fε||2²≈N Aδτ。                         (7)

固定着色版本的常数亦可吸收；不能在L∞中错误留下N，也不能因原管相交而否定频率不交。p>2时Khintchine及(4)给

    Eε|Efε(Rpacket X)|p≥c_p Aδτ^p M(X)^(p/2)。

Z在固定bounded六维盒内，在(1)取A=C_RRpacket。缩放的体积因子为Rpacket^-6=δ12。积分、用(7)并对sign平均，得到

    Aδτ^p ∫M^(p/2)
       ≤C δ^(12−2pεs)(N Aδτ)^(p/q)。                    (8)

源L²的2/q次幂在p次方后正是(N Aδτ)^(p/q)，不是p/2或2p/q。Th1.5严格区间若直接用全空间Lq范数，也有||fε||q^p≈(N Aδτ)^(p/q)，只去掉εs亏损，不能改善以下主幂。

## 7. 独立解出非饱和N与饱和公式

由Hölder、(5)、(6)，

    ∫M^(p/2)≥(∫M)^(p/2)|Z|^(1−p/2)
             ≥c(r λ̄ Nδ4)^(p/2)|E|^(1−p/2)。             (9)

将Aδτ≈δ4τ、r=δ²/τ代入(8)–(9)，先在升幂前得到

    |E|^((p−2)/2)
      ≥c λ̄^(p/2) N^(p/2−p/q)
           δ^(7p−12−4p/q+2pεs) τ^(p/2−p/q)。

定义

    s_p=p/(p−2)，a_pq=p(1−2/q)/(p−2)，
    βp=(10p−24)/(p−2)=10−4/(p−2)。

由于2≤q≤p，0≤a_pq≤1。对每ν>0选εs=ν(p−2)/(4p)，得到完整非饱和式

    |E|≥c_ν λ̄^s_p N^a_pq
        δ^[(14p−24−8p/q)/(p−2)+ν] τ^a_pq
       =c_ν λ̄^s_p δ^(βp+ν)(Nδ4τ)^a_pq。               (10)

N≈δ^-4时即

    |E|≥c_ν λ^s_p δ^(βp+ν) τ^a_pq。                    (11)

所有I、N、τ都在代数中保留，没有先按饱和N取消后冒称任意N。原λ可在逐管假设下代入λ̄≥λ；一般平均版直接用λ̄。

## 8. 必要p≥5/2及这条桥的强度上限

这里独立核标准常函数驻相必要条件，不能用conjecture本身当定理。取固定非零annular radial bump、固定角度patch内正smooth函数f，令X=ρω、S≈ρ，ω在一个更小patch。角度维数4的非退化驻相给|Ef(X,S)|≥cρ^-2，在|S−ρ|≤c且ρ足大的这块区域成立：radial积分在足小固定区间内不抵消，驻相主系数非零，余项更小。每个ρ壳的六维体积≈ρ4dρ，故p<5/2时

    ||Ef||Lp(B_A)≥c A^(5/p−2)。

固定f的右边范数为常数，(1)若对任意εs>0成立，取εs<5/p−2即矛盾。因此此种源局部估计必要p≥5/2；全空间强估计在endpoint还受log发散，不能免费取p=5/2。

βp对p>2严格递增，故p≥5/2⇒βp≥2。τ≤1且a_pq≥0，(11)中τ=1最强；N非饱和亦不会给新的有利因子。目标|E|≳δ^(1−σ)需主幂βp<1，即p<22/9，已经违反上述必要条件。λ≥δ^η只再付s_pη的正亏损，不能反向补它。因此即便给这条桥最有利的hypothetical p↓5/2、τ=1，也只到δ^(2+o(1))层级，弱于所需δ^(1−σ)；并非说实际集合必须只有此体积或所有cone方法不可能。

## 9. 平均／逐管、restriction与反攻核

本桥的完整证明只用I=Σ|Yi|，所以(10)对原平均密度λ̄本身成立，不需先heavy删选，也不赠平均⇒逐管。若另一步确需逐管≥λ̄/2，则heavy族N_h≥cλ̄N、保其actual marks；把N_h放入(10)还会产生相应a_pq费用，不能悄悄保原N。整label restriction保方向分离和全部旧Yi，但N/I/λ均按真实子族重记；任意shading删选则只在新I下可用。

独立压力测试：τ=δ给round级mini宽r=δ而非δ²，带宽因子τ^a不会优于τ=1；τ=1的||f||2²≈Nδ4在饱和N下为常量，而每packet的δ4幅度不能删。p=2不在(10)除数范围内，当前source合法区间亦不因此允许取极限获增益。pointwise复相位用Khintchine，不假独立几何g或共同纤维；端帽通过未clamp的ti全保，无density阈值删端点。重复方向不属当前δ分离假设，若增加同sector packet不能继续用(7)的L∞≤1而无费套公式。

本稿未把cone源的“n”或频率sector数当原ordinary维数，也未引用sphere restriction；局部wave packet的mini方向始终保留。没有从所得较弱lower反推真实反例、上界或完整finite→Hausdorff新后果。

## 10. 限定结论、依赖与待实际互审

本轮实际完成的是指定cone packet/random-sign桥的完整原量词预算，主式(10)与必要条件的独立计算不给普通R5>4所需强度。它是一次来源转移试验，非新ID／major，不复活旧KT数值、G4／proper模型或通过调τ/q/k续轮。高级cone Prop1.7仍为具名输入，其全部外部proof未新独证；Khintchine、Hölder和标准角驻相的作用已明确，未借OpenAI署名或作者AI披露作为正确性保证。

当前尚待B/root最终稿actual全文交叉核，本文不预记自己已独立reviewed或未来metadata/Git/sync；source正算本身不代替独立审查。主目标保持active，停止结论只针对这条明确直接桥，不排除其它真正不同的cone几何或高维方法。
