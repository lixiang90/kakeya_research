# R0017：有限向量强化的反例攻击与数字进位边界

2026-10-17，lifting_obstructions。读过 GOAL、STATE、ROADMAP、registry、AGENTS及本轮 working_spec。本轮唯一攻击对象是 MNL-001 删除最后“逐差落直线”条件后的 finite strengthening；不是给实际 source 删除 AD、coherence或原管关系。

结论先行：**未构造满足全部量词的 finite countermodel，也未证明完整 vector strengthening。** 以下得到固定损失构造的精确门槛，以及形式 derivation 模型的实数进位障碍。它们不等于新的联合扩张或原配置反例，不能据此完成 N5-STICKY-MATRIX-01。

## 1. 攻击的量词不能放宽

固定 γ_T、γ_Φ>0、足够小的精度指数 a>0和质量指数 b₀>0。然后必须对任意小 h>0，在足够小 r上给模型。保留：同一个 exponent-one Frostman时间 B；有 line-cap的同一个差标签先验 ν；bounded F:B→Mat(2,2)及 all-real SM；A₋的 tube Katz–Tao指数1−γ_T；#A₊≤r⁻ʰ#A₋；原0≤g≤1密度≥r^h，且每个正权tuple的

    a+(b−b′)(F(b)−F(b′))ψ_s

距 A₊至多 O(r)。不能把 O(r)改为r^a，也不能把原 joint g换成独立时间或独立方向。只有最后的 linewise条件被删除。

因此 density=r^c、其中c为某个固定正数的例子，不能通过令 h<c 来反驳该强化。代数恒等式或某个小子族的点数也不能代替这个 density要求。

## 2. 三种便宜删选的固定损失门槛

下面均直接对原 g≤1和原先验作 upper，不附加正则性；尺度指数先取0<θ≤1，以保证 Frostman/cap查询不小于 r。

**近时间。** 若所有正权 edges要求 |b−b′|≤r^θ，B的 exponent-one Frostman给可用时间对比例≤C r^(θ−h)。故 density≥r^h至少要求 θ≤2h+o(1)。固定 θ>0的近时间模型不能覆盖任意小 h。

**同一个 affine piece。** 若把 B分成不交 pieces B_i，每个piece上 F以≤r^a误差拟合某个实矩阵仿射函数，则 SM迫 #B_i≤r^(b₀)#B。若正权edges只用同一piece内的时间对，其比例≤Σ_i(#B_i/#B)²≤r^(b₀)。这不能达到 h<b₀时的 density门槛。允许每piece使用不同affine coefficients并不能消除此损失。

**逐时间对选窄方向带。** 即使条带方向可任意依赖 b,b′，ν的 line-cap仍给每个宽r^θ条带质量≤C r^(θγ_Φ−h)。若图完全限制于此类带，density≥r^h要求 θγ_Φ≤2h+o(1)。因此“为每个矩阵差挑其近核方向”不是免费操作；当要把固定量级作用压到 O(r)时，该成本一般是固定正幂。

这些门槛只排相应构造策略，没有覆盖粗糙 F的全部可能性，也没有证明普通非退化方向对上有足够原质量。

## 3. 一个确实保原平移式的形式 derivation 恒等式

设 D为实数上的一个形式加法映射并满足 Leibniz：D(xy)=xD(y)+yD(x)。定义

    F(b) = [[b,0],[2D(b),b]],
    ψ = (x,D(x)).

令 d=b−b′，利用加法性与 Leibniz可精确算出

    d(F(b)−F(b′))ψ
       = (d²x, 2dD(d)x+d²D(x))
       = (z,D(z)),  z=d²x.                       (3.1)

graph(D)还对加法封闭。因此若能把这些 formal graphs实现为合适有界有限载体，(3.1)会是需要认真检验的 vector机制；它不是单一像线或一个 matrix pencil。没有在这里从形式恒等式推得 finite countermodel。

它甚至给出一个形式直线核验。令 f(t)同上、原grain点(x,y,0)中x=(u,v)、y∈graph(D)，选 φ=(c,Dc)、ξ=(-u,v−2Du)。直线

    (x+tφ, y+tξ, t)

在时刻t的grain截距为 y+tξ−f(t)x−t f(t)φ，其第一坐标为 y₁−2tu−t²c，第二坐标恰为该数的 D值。此计算保了原 full水平坐标的代数位置，仍没有证明 bounded ξ、finite covers、Φ AD、tube joint AD或跨尺度原关联。

若 D在整个有界实区间上有界，则加法性迫它连续：当|x|≤1/n，|D(x)|=|D(nx)|/n≤M/n。连续加法映射为 D(x)=xD(1)，而 Leibniz给D(1)=0，故D=0。所以上述理想模型在“完整实区间且统一bounded”的版本直接退化，F变为affine并违反 SM。有限 densegrain没有被当作完整实区间；不能把这一连续论证直接套给本轮原数据。

## 4. 基数数字 derivative 不保实数乘法

这是有限实现中已严格核到的错误点。固定整数Q≥3、N≥2、r=Q⁻ᴺ，对 b=k/Qᴺ∈[0,1)写唯一N位展开 b=Σ_(j=1)^N c_jQ⁻ʲ，0≤c_j<Q。定义

    D_N(b) = N⁻¹ Σ_j j c_j Q⁻ʲ.

它有界，且是数字 coefficients的线性函数；这并不使它成为实数加法/乘法上的 derivation。

取合法网格点 x=(Q−1)Q⁻²、y=Q⁻²，其和为Q⁻¹。直接代入有

    D_N(x)+D_N(y)−D_N(x+y)=1/(NQ).              (4.1)

再取 u=(Q−1)/Q。u²的数字是 c₁=Q−2、c₂=1，所以

    D_N(u²)−2uD_N(u)=−(Q−2)/(NQ).              (4.2)

减去线性主项也不能修复。令 E_N(b)=D_N(b)−b/N，则 E_N(u)=0，但

    E_N(u²)−2uE_N(u)=1/(NQ²).                  (4.3)

对每个固定 a>0，(4.3)与 r^a之比为Q^(aN−2)/N，随N趋∞发散；与r之比更大。因此即使只希望 O(r) graph误差，也不能把这些真实carry当作低阶项。以有限域、无进位 formal polynomial或单独digits的乘法替代原实数乘法，会改变攻击对象。

这些是合法 tuples上的精确失败值，**不是整张 restricted g的质量upper**。一个或常数比例的坏tuple可以被删去，而目标只需 r^h比例；本稿没有因(4.1)–(4.3)就宣布所有数字反模型失败。要形成真正反例，必须实际构造多值/进位输出载体 A₊，验证其与 A₋的 cardinal比及全尺度tube Katz–Tao，或证明能保住足量成功tuple。目前未完成这一项。

## 5. 完整时间网上的近加法 graph还有一致稳定性障碍

下述有限lemma说明不能把上节carry忽略为一个统一 O(r)的single-valued误差。

设 d:{0,…,N}→R^m，d(0)=0，且对所有 j+k≤N，

    ||d(j+k)−d(j)−d(k)||≤θ.

则对所有j都有

    ||d(j)−(j/N)d(N)||≤2θ.                    (5.1)

证明：减去(j/N)d(N)，记所得函数g，故g(0)=g(N)=0。对j,k∈{0,…,N−1}，若j+k≤N，其 cyclic加法缺陷≤θ；若j+k>N，令l=j+k−N，分别使用j=l+(N−k)及N=k+(N−k)，得缺陷≤2θ。固定j对全部k取平均，cyclic平移使两侧平均g相消，留下||g(j)||≤2θ。

因此在 complete r-grid上，一个对全部合法加法tuple均具有 O(r) defect的single-valued图，已经在 O(r)精度内仿射。把它放入(3.1)的矩阵模板时，矩阵 F也在 O(r)内仿射；固定 a<1、小r时不可能满足 r^a精度的 SM。

(5.1)需要全部加法tuples，不是 source条件。它不排除仅在 r^h dense joint graph上的近加法、多值输出或新增carry fibers。故不能把这个稳定性lemma当作本轮vector命题的证明。

## 6. 本轮边界与停止

以上没有产生满足全部 finite strengthening的反例。它提供了三种固定损失策略的原质量upper，及形式derivation实际具有的代数风险与有限实数carry障碍。没有使用C²、定量曲率或额外irreducibility替代原量词。

很高的加法能量/很小doubling本身也不能成为同一个原 translation graph的替代：向量承载结构的各尺度方向可以变化，普通 additive inverse不自动给 F或原b,b′的作用闭包。本轮另一互补审查负责其具体能量/BSG门槛；本稿不以单因素 highenergy模型冒充已接回(1.1)的反例。

当前真正未处理的仍是含实数乘法、同一个 bounded g和同一prior的二维 joint机制。如果 root没有得到新的实际质量估计，应按 working_spec执行宏观停止，不再围绕carry阈值、scalar投影或同义inverse目标开下一轮。原source保留的x、ξ、fullgrain与路径信息可以作为不同机制的来源，但本稿没有将其假定为已经完成的新证明。长期Goal仍active。
