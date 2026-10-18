# R0098：平面向量测度新不等式的wholeclock用途与ambient门

2026-10-19，root。量词与停止见research/rounds/R0098_working_spec.md。以下具名采用De Philippis–Pigati2601.10647v3 Th1.7/Th3.1，实际支付其原wholeclock用途和缩放强度；没有取得一般五维/高维Kakeya增益，未经外部同行评审。

## 1. 全目标与新primary的实际范围

任意欧氏n≥5 full-direction unitsegment Kakeya集合仍是目标。R97输入门已冻结，不续ε/b或polynomial模板。本轮采用此前未入库的DP–P v3（2026-09-01）：其Th1.7容许平面向量Radon measures及finite-TV div，不要求光滑场，也不要求det≥0。不能因为其Michael–Simon主应用只处理R³ rectifiable2-varifold而拒绝独立平面定理。

root实际读官方§1.1–1.3、§3 Th3.1/Remark3.2/Cor3.3与原PDF4图。全高级functional proof仍具名，未重独证。另BDH2404.04754v1实际smooth flags/regularizedBL范围由A核，定位为比较源，不当新的HRZ输入。两PDF原件/提取/metadata归literature。

## 2. 共同支配测度的非线性量

S,T为R²上的finite-TV vector measures，divS、divT也finite-TV。取λ=|S|+|T|，S=sλ、T=tλ，定义SP=(s_x−|s_y|)^+λ、SN=(s_x−|s_y|)^−λ、TP=(t_y−|t_x|)^+λ、TN=(t_y−|t_x|)^−λ。这些是一阶正齐次，换支配测度不改定义。ν=min(SP,TP)为measure infimum，等于(SP+TP−|SP−TP|)/2，不是原tube数量的min或全局角质量的乘积。

记M_S=|S|(R²)、D_S=|divS|(R²)，T类似，N=SN(R²)+TN(R²)，B=M_S+M_T+D_S+D_T。DP–P给任意bounded support Borel 0≤χ≤1：Iχ=∫χdν≤C||χ||₂√((M_S+D_S)(M_T+D_T))+C(D_S+D_T)+N。χ范数按二维Lebesgue，不是按λ。

## 3. 真正的dilation账与定量面积输出

对L>0设D_L(x)=Lx，物理current dilation S_L=L(D_L)#S（T同），χ_L(x)=χ(x/L)。于是M→LM，D保持，SP/SN/ν总质量及I→L倍，||χ_L||₂=L||χ||₂。divS_L=(D_L)#divS可用任意测试函数链式法则直接验证。将原不等式除L得到

Iχ≤C||χ||₂√((L M_S+D_S)(L M_T+D_T))+C(D_S+D_T)/L+N。

取χ=1_E，E bounded Borel、A=Leb²E。0<A≤1时取L=A^-1/4≥1，根号≤(L+1)B，故ν(E)≤CB A^1/4+N。A=0令L→∞得ν(E)≤N；A≥1由ν(E)≤√2M_S≤√2B≤√2B A^1/4。故对所有bounded E，统一

ν(E)≤CB (Leb²E)^1/4+N。                    (98.1)

这是原定理的实际缩放后果，不能因unitbox内D不小就宣称该工具强度无效。标准缩放不认证新颖性或独立新主定理。

## 4. 零坏cone时更强的已知L²校准与条件出口

若N=0，null集合代(98.1)给ν≪Leb²；写ν=f dx。对E={f>τ}∩B_R，τ|E|≤CB|E|^1/4，故τ|E|^{3/4}≤CB；R→∞得到||f||_{L^{4/3,∞}}≤CB。反过来这是标准Lorentz积分弱型的同阶形式，不把它当新Kakeya维数界。

若ν载于有界E且I=ν(E)>N，(98.1)给Leb²E≥c((I−N)/B)^4。因而实际原配置若真能提供I≥δ^o(1)、B≤δ^-o(1)、N=o(I)以及二维target面积的正幂upper，就可得到矛盾。四项必须同时支付，尤其I是同一空间点的cone-overlap质量，不是两个cone各自总质量下界。

独审进一步发现本轮实际N=0构造已有更强旧平面机制覆盖。此时S_x≥|S_y|、T_y≥|T_x|作为measure。对非负smooth mollifierρ_e，令S_e=S*ρ_e、T_e同；三角不等式给S_e^P≥SP*ρ_e、T_e^P≥TP*ρ_e，故ν*ρ_e≤min(S_e^P,T_e^P)。写a≥|b|、d≥|c|，则det=ad−bc≥(a−|b|)(d−|c|)≥(ν*ρ_e)²。卷积场属于W^{1,2}、div的L¹norm≤D_S,D_T，可用DP–P Th1.6/3.5的sharp1/4版本。其机制已有Guerra–Raiţă–Schrecker [13]（Ars Inven.Anal.2024），旧常数非sharp；这里不把本paper的sharp常数追认给旧文：

∫(ν*ρ_e)²≤D_S D_T/4。

uniform L² weakcompactness并令e→0给ν=f dx、||f||₂≤√(D_S D_T)/2。若ν载于E且I>0，Leb²E≥4I²/(D_S D_T)；某D=0则ν=0。这比weakL4/3更强，不需要新Th1.7的一般badcone量化。本轮actual zero-bad桥被旧平面双线性包含，不能登记为新ordinary输入。N>0新定理未由本校准排除，也不据此重开badcone模板。

## 5. 任意原单位线段到S/T的真实构造

先在有界Borel K或保同Hausdorff维数的Borel hull上取可测原unitsegment选择γ_v(t)=a(v)+tv，0≤t≤1，v服从固定full-angular概率σ。可用完备化measurable selection；原R91已付该构造，不另认证新选择定理。固定orthogonal rank2 P:Rⁿ→R²，u=Pv。令C_x={u_x≥2|u_y|,u_x>0}、C_y={u_y≥2|u_x|,u_y>0}，并取任意原方向权0≤w≤1。

定义S=∫_{C_x}w(v)∫₀¹u δ_{Pa(v)+tu}dt dσ(v)，T由C_y同式。确为finite vector measures，由analytic P(K)承载（按完成测度解释），topological support只保证包含于closure(P(K))；若K compact则可去closure。M_S≤∫_{Cx}w|u|dσ≤1、D_S≤2∫_{Cx}w dσ≤2；divS=∫_{Cx}w(δ_{Pa(v)}−δ_{Pa(v)+u})dσ。此符号来自−∫d/dt测试函数。T同，故B≤6。两个正向cones凸，任意同point向量叠加仍在同cone，所以SN=TN=0。

这是对任意原wholeclock的合法用途，实际N=0时第4节已知strongL²适用；没有把scalar occupation law当vector measure，也没有向K加入连接曲线/端点回路。方向restriction只减少上述absolute upper，不赠conditional angular independence或I下界。对非Borel原K，结论先在明确hull/原选择的测度支持范围用，不反推K自身Lebesgue可测。

## 6. 有界正向current的flux与端点收费

若S支持在|x|≤R的有界集合且S_x为正measure，用等于x的紧支撑cutoff测试函数得到∫dS_x=−∫x ddivS≤R D_S。若|S_y|≤a S_x、a<1，则SP≥(1−a)S_x且SP≤S_x，所以D_S≥SP(R²)/R。固定unitbox中不准由方向数多、λ密度高或δ细就假D_S=o(cone mass)。

该下界只拒这种unitbox免费端点假设，不反第3节正确dilation或全部DP–P用途；放大几何时R同步放大、D不变、mass变L，恰与(98.1)一致。没有利用未知universal常数C去宣称RHS必压倒所有I。

## 7. 真实full-angular unitbush的精确校准

取γ_v(t)=tv、v∈S^{n−1}，全方向unitclock，原union为闭unitball，正n体积。对任意rank2 P，投影原轨迹z=tu，u=Pv；z≠0时当前速度u与z平行。故S仅在C_x对应的空间sector、T仅在C_y空间sector有质量。这两sector不交，0点在各current中无atom（单t集合Lebesgue零，u=0贡献也零）。于是ν=min(SP,TP)=0，而fullangular law下SP、TP总质量分别正，坏部零，端点TV finite。

这个例精确计算本轮新functional的输入与LHS，不是Kakeya反例、不是否(98.1)。global angular richness不授local相交已R91证明，不换名作新重大数学结果。它也不满足原mixed smalllabel/Φ/grain全套，不能否完整sticky源。

## 8. 原shading不会免费保finite边界成本

单一真实unitline上选m个互不相交、均在(0,1)内的等长intervals，总长固定λ∈(0,1)。令h为其indicator，S_h=∫h(t)v δ_{a+tv}dt。分布divS_h是2m个不同内部端点的signedatoms，TV=2m；因此即使每管都有同一λ的逐管密度，也不能只从λ得到统一的TVdiv upper。任意Borel shading更可能没有BV，不能以wholeclock端点≤2替代。

在δtube有限模型选长度≫δ且间隔≫δ的intervals，λ按端点舍入只付O(mδ)，m可至cδ^-1，密度可固定而TV发散。该例否定所需闭包，不反原finite theorem或完整源配置。选择tube族仍保持wholeclock与截去时钟，是不同操作。

## 9. 为什么平面投影不能免费返回五维

即便实际ν(PK)>0推出投影正二维面积，也只立即给dim_H K≥2；不能把它当五维增益。若企图在Q:R⁵→R³的fibers逐个用平面定理，再Fubini返回5，必须先证conditional planar currents有finite-TV二维div与共同质量。

这个闭包一般失败，甚至一条斜unitline已足校准：取v有Pv≠0、Qv≠0，wholeclock current∫vδ_{a+tv}dt有两个端点边界。按Qx对其P分量disintegrate，在几乎每个内部Q位置，planar conditional为c Pv δ_{x0}（沿Qv的1维推前law；不能冒Leb³ fiber law）。其二维div是δ点的方向导数，不是finite measure：取supnorm≤1、梯度在x0沿Pv增至m的测试函数，div作用无界。total n维div中Q方向导数的抵消不能在conditional P部分免费留下。

此反例只检验analytic slicing闭包，不是full-direction源反例。原完整K若另有fiber-tangent representations可能适用，但本轮未获得；不能以全方向law中Qv=0方向集的零σ质量建立正质量fiber流。

## 10. 原mixed42的小target与角横截的冲突

检验合法光滑压平模型π(x,t)=(q(x,t),t)。假设q在每个原native horizontal3plane上真正恒定，记其切space W_t={h4=β_t h_H}。则D_xq annihilates W_t。原同p方向star的差为(φ−φ′)(1,f1,f2,0)，由原(103) f2=β1+β2 f1可知水平部分属于W_t，time分量零。故Dπ在同p的全部原φ上给同一projected velocity。

因此这个真正保小native标签的压平选择不会自动将原Φκ变成两横截cone流；同point angle variation被消掉。不同p/fibers仍可能投影到同point而速度不同，不能从该恒等式宣布全部projected ν=0。需要原跨fiber混合质量才能应用第4节条件出口，这正尚未支付。实际只有有限filled X，不自动授q上述光滑恒定hyp；此节是合法压平时的必要检查，不把roughβ可微当原结论。

另一方面π=(filled x1,time)可保角变化，但其target已有完整二维packing，没有原κ面积亏损；R95已付其RW饱和范围，不能换DP–P题名重开同一平面gain。

## 11. 四路线、文献与独立审查责任

新primary采用的是允许measures的独立functional定理和真实缩放用途；Michael–Simon/Prop1.9仍要求rectifiable varifold、正k-density及atomiccondition，不给一般R⁵ Kakeya直接定理。BDH固定smooth nested flags和regularizedBL核条件不支付旧HRZ原marks/parent缺项，A实际比较不把标题当输入。

ordinary初始化、HRZ全部预算、sticky完整rough及ordinary桥、同集full方向strict低维四路均open。以上是具体适用信息，但actual N=0用途已由更强旧Th1.6覆盖，不是新ordinary输入或独立主gain。不认证新颖/重大性，不增registry ID、不改变78旧ID状态。R91已知rankgap和R95旧平面门不登记为新结果；仍须实际独立逐式审后才内部reviewed。

版本范围补记：该v3 addendum及refs[10–12]报告后续Firester–Tsiamis的任意维/余维MS工作和Gennaioli–Rindler的vanishingmass输入。root本轮只fresh核2608.31164v2、2608.20899v2官方abs/history，未读其主定理/wholeproof、未采用或下载这些新paper。不能因本paper Prop1.9只是等价就泛称‘目前任意维MS未证’；原Kakeya到rectifiable-varifold/variation的输入仍须实际支付。

## 12. 本轮判定与停止

本轮付清finite-TV原wholeclock入口、dilation后weakL4/3/面积条件输出，并由独审补出更强已知strongL²校准，发现actual zero-bad桥没有新增工具强度。原shading内部BV、fiber conditionaldiv和native角横截费用已明确；未取得原local-overlap下界及二维到ambient返回，无一般Kakeya增益或strict低维反例。

停止这组直接投影/端点/clockdilation及cone aperture参数续轮，不宣称所有向量测度/PDE或其他高维机制无用。下一必须先重新筛全路线或确实新的原跨fiber输入，不能将本轮条件出口当已经解决的主gain。两PDF来源/读域、独审与archive/sameSHA同步另记录，完整Goal active。
