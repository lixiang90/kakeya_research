# R0089：几何 cut、原访问质量及五维 graininess 反攻

2026-10-18，B；恰十个编号二级节。全文读取锁定的R89 working_spec五节后施工。只审原H5小阴影的几何cut/降次数及其coarse用途；不附成功假设，不以局部例否定H5，不声新ID、major或Goal完成。高级来源与本次独证范围分别记录，未经外部同行评审。

## 1. 实际来源、量词与不同于R56的输入

实际读 [Guth1402.0518v1](https://arxiv.org/html/1402.0518v1) intro/Hypotheses0.2、Th0.4/0.5，完整§1和§2.2证明；对照新存提取文本的PDF8–16，并读§2.1的相邻概率模型。没有把整40页后半曲率wholeproof称为已独审。本轮固定采用v1；source中的大尺度 \(N\) 下文改记 \(L\)，避免与原管数混淆。

cut是原Def1.1的signed-volume条件：对尺度参数 \(r\) 与给定单位格Q附近全部适当中心、全部半径介于 \(r\) 和1的球，正号部分体积与一半只差 \(r\) 比例。它强于仅 \(Z(P)\) 与Q相交或二分Q。全ambient Lem1.3/Cor1.5可用ham sandwich构造cut；Lem1.6按degree控制传播失败的gap数。这个几何机制不抽top coefficient，确不同于R56已经停止的scalar Taylor/Remez外推。

原H5仍是R5中满 \(\delta\)-方向网的单位round管、原可测marks、\(\lambda\ge\delta^\eta\) 及真实 \(|E|\le\delta^{1-\gamma}\) 反设。不能预给每格多方向、全空间multiplicity上界、quadratic-spread或free mixing。对该完整输入，本稿最终没有证明所需 \(\deg P\le\delta^{-\varepsilon}\) 与足够coarse用途，也没有构造其反例。

## 2. 共同随机格：可同时保的是真实K、I和未饱和N′

取一个共同平移 \(\xi\in[0,\delta)^5\)，格点 \(G_\xi=\xi+\delta\mathbb Z^5\)。记

\[
K_\xi=\#(E\cap G_\xi),\qquad
I_\xi=\sum_i\#(Y_i\cap G_\xi).
\]

对任意Lebesgue可测原阴影，Fubini给 \(\mathbb EK_\xi=\delta^{-5}|E|\)、\(\mathbb EI_\xi=\delta^{-5}I\)。单位round管中每个 \(\delta\)-clock slab只有固定个 \(\delta\)-分离格点，包括端帽，故 \(I_\xi\le C N\delta^{-1}\)。若 \(I\ge\lambda NV_\delta\)，\(V_\delta\asymp\delta^4\)，则用Markov先删

\[
K_\xi>C_0\lambda^{-1}\delta^{-5}|E|
\]

的shift，选 \(C_0\) 足大，使这些shift承载的期望 \(I_\xi\) 至多原期望的四分之一。因此存在同一个shift满足

\[
K\le C\lambda^{-1}\delta^{-5}|E|,
\qquad I_{\rm grid}\ge c\lambda N\delta^{-1}. \tag{1}
\]

这不是把 \(N_\delta E\) 当成 \(\delta^{-5}|E|\)，也不声同时选择时没有 \(\lambda^{-1}\) 成本。随后删访问少于 \(c\lambda/\delta\) 的labels，可保常数比例 \(I_{\rm grid}\)，原剩余管数 \(N'\ge c\lambda N\)，逐管访问密度 \(\lambda'\ge c\lambda\)。原方向仍分离，但不自动仍满S4。平均版用总I先作同一证明；逐管假设给同样下界，不能反向无费互换。

每个保留格点配一个同平移的半开 \(\delta\)-cube，固定着色后可满足Lem1.6的 \(2n\) 分离，沿每管每clock slab的slot重复度亦只常数。缩放后这些cube与原管常数倍厚化相交；几何半径常数可统一改到1。其并集体积由 \(\delta^5K\) 控制，但cube未必全在E中。cut该cube只保证原格点距 \(Z(P)\) 为 \(O(\delta)\)，没有自动切到全部原可测Yi；从单shift证书返回Lebesgue质量还须另证。

## 3. 全n cut传播工具独核：degree控制的到底是什么

Lem1.3/Cor1.5在每个固定n的合法输入是任意有限单位cube，固定 \(r>0\) 时可取 \(D\lesssim_{n,r}S^{1/n}\)。证明用半径 \(O(r^2)\) 的更细cube网对每个相关球作体积近似，再以ham sandwich同步二分，故不需要kernel conditioning或原cube可测密度。这个工具可在R5使用。

独核Lem1.6：将管竖直化、以 \(\pi:\mathbb R^n\to\mathbb R^{n-1}\) 投影。几乎每条竖直线与非零P零集相交至多D次；异常整线的横向参数集零测。对有界重叠的扩张gap邻域，Bézout/Fubini给

\[
\sum_j|\pi(Z(P)\cap N_R T_j)|\le C_nD(R+1)^n.
\]

固定 \(R\asymp r^{-1}\)，将投影量大于固定 \(c_nr^{2n}\) 的gap判坏，可得至多 \(C_nr^{-4n}D\) 个坏gap。好gap中，把待测球沿轴平移到一个已cut的anchor高度；除横向投影极小的竖直线外，P的符号不变，两个球在每条竖直线上截长相同，近二分传递成立。

这是实际全n证明，不把R3结论换维套用。它只传播两个anchor之间的区域，不处理最外anchor以外的尾段；所控是gap数量，不是这些gap的物理长度、所含原访问数、tube-label权或Lebesgue阴影质量。

## 4. 坏gap数量不能免费换成坏clock／阴影质量

先给最基本的量词压力测试：可有很多cut anchors挤在两端，而唯一大gap占几乎全部clock。此时 \(\#\mathrm{bad}\lesssim_rD\) 不能推出坏长度小；把所有marks放在该gap也不违反一个单独的gap数量声明。

这还可由真实固定degree多项式实现，而不是仅抽象序列。固定小cut参数r。在相关有界横向盒内取高频 \(\sin(ky_1)\)：对所有半径≥r的球，signed-volume偏差 \(\lesssim(kr)^{-1}\)，因为球的横切面积权有总变差 \(O(\rho^{n-1})\)。先令k足大，再以多项式 \(P_0(y_1)\) 一致近似，使近零带的额外体积也小；于是P0对这些球有严格cut margin。所有选择仅依n,r，\(d_0=\deg P_0\) 固定。

令管clock为 \([0,H]\)，设

\[
P_H(y,t)=P_0(y_1)+A\,t(H-t)/H^2,
\]

其中A大于所需横向盒上 \(8\|P_0\|_\infty\)。在两端各取 \(S\gg d_0\) 个相互 \(2n\) 分离的anchor cubes。\(H\) 足大于 \(S\) 后，相关球上新增项任意小，所以保原cut margin；但在 \(H/4\le t\le3H/4\) 的整个管截面，P_H同为正，不cut。degree至多 \(\max(d_0,2)\)，且可令中间唯一大gap占clock比例趋1。

此例只反“少数坏gap自动是小质量”的推论。它没有原满S4方向、小footprint的完整H5条件；不称H5/Kakeya反例。原文§2.2并未作这个免费推论：它先按**访问cube rank**均衡选择anchors，随后又用独立横截抽样控制任意D个gap所含的原cube数。对于加权或局部删选后的marks，必须按实际被用的质量重付这种均衡。

## 5. 原R3 theorem的假设与真实全局分母

实际源Hyp0.2为R3：每管访问约L个格、每格约 \(\mu\) 条管、全空间点multiplicity至多 \(E\mu\)，以及每格方向在定量意义下不能集中于任意两条方向。Th0.4的graininess与这些输入绑定，不能只保 \(\#X\) 和逐管访问就声全n版本。

更一般的Th2.2是R3 degree reduction，它只要求逐管/逐格访问近均匀和每格避开任一方向的定量两向横截，**不要求**Hyp0.2的全空间multiplicity upper，也不要求其三向条件。须把两个层级分开。方向分离本身不推出局部star的固定角transversality；原许多方向可挤在一个小cap内，若令其角参数E增长为固定δ负幂，source的 \(\operatorname{Poly}(E)\) 会产生真实费用。

源§2.2的关键独立性也实际核过：对目标管T′只看与其夹角≥\(E^{-1}\) 的随机选中管，并取沿T′相隔足够远的访问格，使一条选中管最多命中其中一个格。坏事件再对**全部原T′**平均，利用每个X格的原上次数；不是只在选中子族内换一个有利分母。最终从好管返回大多数X格，仍用原逐格次数比较。原H5未预给这些uniform/transverse性质，不能把它们加作成功假设。

## 6. 五维两跳最乐观预算：改善参数计数不等于小次数幂

只为检验这一机制的能力，暂在最有利的访问近均匀、横截独立和坏gap质量均已可付的情形算账，不把它们授给完整原H5。记K为格数、\(M_{\rm vis}\) 为每管实际访问数、原管数为N，于是 \(K\mu\asymp NM_{\rm vis}\)。

在R5中，degreeD的ham-sandwich自由度为 \(\asymp D^5\)。每条seed管要 \(\gg D\) 个cut anchors才能抵坏gap，故seed管数至多 \(\lesssim D^4\)，忽略固定cut常数。目标管的预期横截seed访问最多在理想均匀模型下达到量级

\[
M_{\rm vis}\cdot D^4\mu/N
\asymp D^4M_{\rm vis}^2/K.
\]

要据此供应 \(\gg D\) 个anchors作第二次传播，该方案需

\[
D^3\gtrsim K/M_{\rm vis}^2. \tag{2}
\]

在R3，同一推导是seed数 \(D^2\)、约束 \(D\gtrsim K/M_{\rm vis}^2\)，吻合原Th2.2。不能把这个三维输出凭ambient维数改写成 \(D\lesssim K/M_{\rm vis}^4\)。式(2)是**该sampling proof的预算要求**，不是全部可行多项式的普遍次数lower。

以(1)的诚实上界作最坏预算，\(K\lesssim\delta^{-(4+\gamma+\eta)}\)、\(M_{\rm vis}\gtrsim\delta^{-1+\eta}\)，选定该最坏规模时(2)要求次数约 \(\delta^{-(2+\gamma+3\eta)/3}\)，不是任意小的 \(\delta^{-\varepsilon}\)。若K实际更小或存在不同原结构，不能用上界倒推同样lower；这里只判当前两跳uniform预算不足以证明所锁全称门。

## 7. Directed area／Crofton只给已知一阶几何

固定cut尺度使每个被cut的单位cube内零集有固定正的 \((n-1)\)-面积，来自球内两侧正体积与relative isoperimetry。R5的Crofton/Bézout给

\[
\mathcal H^4(Z(P)\cap B_L)\lesssim D L^4.
\]

因此若切到K个分离格，必有 \(D\gtrsim K/L^4\)。这是必要lower，不是constructive upper；当 \(K\asymp L^{4+\gamma}\) 时只表明最理想次数至少 \(L^\gamma\)，并不否定先取小γ后寻求 \(L^\varepsilon\) 的完整方案。

沿一条radius1管的directed area \(\int|n_Z\cdot v_T|\) 又由几乎所有平行线的至多D次交点控制。结合cut面积能作标准planiness类估计，但它只读法向的一阶角信息；原biased axes可能是异常含线，须保横向Fubini而非把Crofton的almost-every-line直接逐label用。

上述量不自动让tangent hyperplane沿长clock近常，不给原coarse管的方向cap或partial-mark PW，不供应一份四维DIR可合法调用的共同carrier/clock。若后续步骤仍需要这些实际原质量，不能将directed-area恒等式或Crofton计数本身叫作已付五维graininess。

## 8. 三个quadratic null方向不迫四维tangent的II为零

R3光滑surface的tangent为二维，非零齐次二次型在RP1最多有两条零方向；所以三个定量不同的straight/null方向能迫该二次型为零。这个线性代数输入在R5不成立，甚至给四条线性独立null方向也不够。

实体模型为

\[
Z=\{x_5=x_1x_2+x_3x_4\}\subset\mathbb R^5.
\]

其梯度末项恒为1，故全局光滑。设 \(q(x')=x_1x_2+x_3x_4\)。在任意小有界graph点 \(a=(a',q(a'))\)，每个满足 \(q(w)=0\) 的横向方向给真实整直线

\[
a+t(w,\nabla q(a')\cdot w)\subset Z.
\]

特别是四个coordinate w=e_j给四条定量分离、张满tangent的整线。与此同时第二基本型是 \(\operatorname{Hess}q/\sqrt{1+|\nabla q|^2}\)，signature \((2,2)\)，在固定小盒内norm有固定正下界。没有 \(\mathrm{II}=0\) 或任意长clock的小曲率结论。其quadratic-null项目方向可有正维，故只要求“更多若干不同方向”仍不等于二次张成。

这是真实光滑quadric和whole straight-line小star，严格反所述R3→R5的曲率推论；不是完整H5反例。它的继承方向受 \(q(v')=0\) 的leading cone约束，未供应原满S4方向、完整小shadow/任意nearfull族，也未声一切不同的曲率或grain分解都不可能。

## 9. 多hop、实际collision与coarse四维调用的未付责任

把两跳改四跳，需证明新一层访问在原label、原clock、原quality下真是新的端点，而非同一小bundle内的大量walk重计。二部图的最小degree只控制walk数；从walk数变不同cells/tubes/横截witness数，要付最大返回multiplicity和共用首尾条件。没有已付的原conditional domination，不能把每一hop都乘一个独立 \(M_{\rm vis}\)，更不能以trace或Gram较大代原几何spread。

这一点有真实局部line校准：原方向虽δ分离，但可取一个角半径θ的cap内全部网点，其轴都过0；长度 \(\rho\asymp\delta/\theta\) 的共同细cylinder确能作为这些管的同一shading。局部访问图高度接近complete bipartite，更多walk反复回到同一cells，不生新方向或空间质量。它缺原满S4/full H5条件，只反“degree/dirsep alone授独立hop”，不用于否完整H5。

要接具名四维输入，仍须从同一个原访问图实际得到可调用的coarse族：支付短clock/unit rescale、原N′与λ′、重复projection labels、四维方向caps、真实shading density及union的Lebesgue回传。切格/planiness/高阶walk计数都没有单独付齐这些量；禁止附全局multiplicity、三方向或quadratic-spread作为成功前提。本稿未找到从完整原小shadow强制这些性质的证明，故没有可用coarse gain。

还可对**独立均匀seed＋图证书阈值传播**给有限且严格的非启动界。设二部图有J个tube rows、K个cube columns，每row次数在 \([M,2M]\)、每column次数在 \([\mu,2\mu]\)，所以 \(JM\asymp K\mu\)；任两rows共column数≤B。每row独立以概率 \(p\le cD^4/J\) 作seed，与R5中每seed花 \(O(D)\) anchors的 \(O(D^5)\) 自由度预算一致。

固定非seed row，其可能相邻的其他rows至多 \(4M\mu\) 个；条件该row未被选后，这些邻row的seed数 \(X\) 仍是相应独立Bernoulli和。被seed触及的不同columns最多 \(BX\)。因此要出现≥D个触及columns，必须 \(X\ge k=\lceil D/B\rceil\)。在下面括号小于1的范围，标准binomial tail和union bound给

\[
\Pr\{\exists\text{ 非seed row有}\ge D\text{ hits}\}
\le J\left(\frac{e\,4M\mu p}{k}\right)^k
\le J\left(C\frac{BM^2D^3}{K}\right)^{D/B}. \tag{3}
\]

故若 \(CBM^2D^3/K\le c_0<1\)、\(D/B\gg\log J\)，首代几乎不产生任何新active row；可同时用Chernoff保seed数≤\(CD^4\)，额外失败概率≤\(e^{-cD^4}\)。即使乐观地把seed rows上的全部columns都判为good，首代不能启动，单靠同一“已有good cells达到D才激活下一row”的规则增加hop数也无从启动。

(3)是给定有限图和该seeding/认证规则的证明，不是实际 \(P\) 的degree lower，也不是完整原H5反例。它不排 \(P\) 偶然cut别处、相关或非均匀seed、不同几何认证。原几何若只在angle-transverse pairs有B上界，亦只能对这些实际允许邻居应用相同tail。它表明缺口不宜泛写成“独立mixing即可”：低于此预算时，独立抽样恰好可能不能启动。

## 10. 本轮有限结论、交叉审查与停止

已独立付清的范围是：全n cut工具的实际传播量、共享格筛选的(1)及平均/逐管费用、source技术假设层级、真实坏gap质量反攻、两跳的(2)预算、Crofton必要lower以及四维tangent的实体II反攻。cut机制确不同于R56 scalar coefficient方法，但这些步骤还没有证明完整所锁H5降次数及coarse用途。

因此保持**全H5门未证未否**；不以弱例否主命题，也不以技术条件下proper模型或known planiness登记新结果。按spec，如果没有真实多hop/返回mass或新的原几何，则停止，不续次数、cut尺度、λ或quadric方向数量参数，不立newID/major，Goal active。

已实际全文交叉读A十节 `R0089_cut_propagation_and_degree_reduction_audit.md` 和root十节 `R0089_original_shadow_cuts_degree_budget_and_graininess_boundary.md`。独立核A/root的正向原质量hyperplaniness：每个cut的 \(\Sigma_Q\) 面积≥常数，在其中选法向 \(n_Q\) 使原edge角和不大于面积积分的固定倍；对每根fat tube沿原方向用area formula给积分≤\(CD\)，故坏角原edge比例≤\(CD/(\theta\lambda L)\)。取 \(\theta\asymp\sqrt{D/(\lambda L)}\)，结合诚实K得到 \(\theta\lesssim\lambda^{-3/5}\delta^{(1-\gamma)/10}\)。这一点确无额外star横截假设，但只给每格各自的4-plane，不给coarse一致性。root的两次degree分桶/剥离、原I分母、§7有限图认证范围及§8两反攻亦逐式核，无强制修正项。

这份cross记录不把自己的施工计作独审，也不预认证尚未写成的formal、元数据或Git/sync。源高级graininess wholeproof与通常具名基础输入的核验层级继续保留，未经外部同行评审；后续仅在明确授权后写正式终审。
