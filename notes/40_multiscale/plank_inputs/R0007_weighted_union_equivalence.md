# R0007：WP4与加权阴影并集的条件互推

日期：2026-10-16。任务：N4-PLANK-01的互补审查。开轮已读working spec、STATE、原始三维companion `05-inputs.tex` 的Theorem2.1及Lemmas2.2–2.3，并读取已入库GWZ2026 v2 Theorem1.1和Zahl2025 survey §4.1。未新搜索或下载。本笔记中的互推是工具，不声称新颖性或重大中间结果。

核查范围：权重和重复index、所有凸体测试、full-time plank、每index时间密度，以及$\varepsilon/\eta$顺序。以下几何和抽样在任意**固定维度**成立，常数依赖维度及有界图；不能称为常数对维数一致的dimension-free定理。真正依赖维度的输入是最后的并集定理。

## 1. 三种待区分的陈述

先按一般固定时空维数$n=m+1$写；WP4对应$m=3,n=4$。固定$|b_i|+|u_i|\le R$的有界线图，

$$M_i(t)=b_i+tu_i\in\mathbb R^m,\quad0\le t\le1,
\quad\delta=D^{-1}.$$

使用凸的chart tube

$$T_i=\{(t,x):0\le t\le1,\ |x-M_i(t)|\le\delta\},
\quad |T_i|=v_m\delta^m.$$

它与有界斜率的普通Euclidean tube在固定半径、长度变化下相容。所有这些固定变化须并入图常数和输入密度容差。索引有限、$\omega_i>0$任意，允许相同$T_i$有不同$Y_i$或不同$J_i$。

**P$_n$（WP型）。** 所有full-time正交空间框、$1\le a_1\le\cdots\le a_m\le D$满足

$$\sum_{M_i\subset P}\omega_i\le A\prod_{j=1}^m a_j.$$

每个index的标记时间bin集满足$\#J_i\ge D^{1-\eta}$，$E$为其中心访问的时空mesh cells并。要求对每$\varepsilon>0$存在$\eta>0,C$，

$$\sum_i\omega_i\#J_i\le CA\delta^{-\varepsilon}\#E.\tag{P}$$

**W$_n$（加权凸聚类阴影并集）。** 对每凸体$K$有

$$\sum_{i:T_i\subset K}\omega_i|T_i|\le A|K|,$$

并对**每个index**有$|Y_i|\ge\delta^\eta|T_i|$。要求

$$\sum_i\omega_i|Y_i|\le CA\delta^{-\varepsilon}|U|,
\qquad U=\bigcup_iY_i.\tag{W}$$

先可将$Y_i$限为时间bin中心的小球并；这时与(P)的计数直接匹配。若$Y_i$是任意可测cross-section子集，另需§4的重mesh筛选，不能直接说$\#E\delta^n\lesssim|U|$。

**U$_n$（非加权near-convex-Frostman输入）。** 对有限不同tube集合，若

$$\Delta_{\max}\le\delta^{-\eta},\qquad
\frac{\sum_i|Y_i|}{\sum_i|T_i|}\ge\delta^\eta,$$

则要求$|U|\ge\delta^\varepsilon\sum_i|T_i|$。这是GWZ2026 v2 Theorem1.1在$n=3$实际陈述的形式：只有平均密度门槛，并且保留$\eta$依赖$\varepsilon$。**本文不把U$_4$当成已有定理。**

## 2. Full-time框与凸聚类的几何互换

### 2.1 凸聚类给full-time框cap

物理半宽为$r_j=a_j\delta\ge\delta$。若整条$M_i$包含在该框，$T_i$包含于空间半宽$r_j+\delta\le2r_j$的相同仿射移动凸框$K$。其体积至多$C_m\prod_jr_j$。用凸聚类并除以$|T_i|=v_m\delta^m$，得到

$$\sum_{M_i\subset P}\omega_i\le C_m A\prod_ja_j.$$

必须测试完整trace；只有shade落在框内不足以推出这个式子。

### 2.2 Full-time框cap给凸聚类

取含有若干$T_i$的凸体$K$，先与固定有界环境球相交，再取体积$O_{m,R}(|K|)$的外John椭球$\mathcal E$。椭球的水平$m$维切片中心随$t$仿射变化，主轴固定，所有切片形状是最大切片的公共标量倍。其时间跨度至少为1，因此最大切片体积至多$C_m|\mathcal E|\lesssim|K|$。

用最大切片的外接正交矩形沿其仿射中心移动，得到包含所有被计完整traces的full-time框。每根空间半宽至少$c\delta$，因为一个$T_i$在每个chart时刻含半径$\delta$的空间球。若这些半宽为$r_j$，则$\prod_jr_j\lesssim|K|$。应用框cap得到

$$\sum_{i:T_i\subset K}\omega_i\lesssim A\delta^{-m}|K|,$$

乘回tube体积即得(W)所需凸聚类cap，常数为$C_{m,R}A$。

宽度落在固定倍$[\delta,1]$外时：下端以固定倍放大；上端按两个endpoint的相应空间坐标作有限分组，再逐组插值。组数只依赖固定图界，最终乘积因子只增固定倍。这里没有使用任何三维特殊线几何或shading密度。

## 3. W$_n$推出P$_n$：时间中心球的直接转换

每个标记时间bin中心取半径$c_R\delta$的球，$c_R>0$固定足够小，使其包含在$T_i$内、远离time endcaps。不同时间bin的球在同一index内不交。记其并为$Y_i$，则

$$|Y_i|\asymp\#J_i\delta^n,\qquad
|Y_i|/|T_i|\ge c_R\delta^{\eta_P},$$

$$|\bigcup_iY_i|\le C_R\delta^n\#E.$$

先对目标损失$\varepsilon/2$调用W$_n$，得到其密度容差$\eta_W$；取$\eta_P\le\eta_W/2$，则固定常数$c_R$在小$\delta$时被吸收。用§2.2得到凸聚类$C_RA$，再约掉$\delta^n$即得(P)，损失至多目标$\delta^{-\varepsilon}$。有界$D$用有限个最宽框控制总权重，再扩大常数。

**时间密度仍是每index的$\#J_i\ge D^{1-\eta_P}$。** 任意时刻的高重数、平均总occupation或后期稀疏selection不能无损替代它；需要先删轻/分层才能调用输入。

## 4. P$_n$反推任意可测W$_n$：必须支付一次重cell损失

这是对任意cross-section的额外步骤。假设(W)中的凸聚类cap及逐index密度$|Y_i|\ge\delta^{\eta_W}|T_i|$。由§2.1得到(P)的框cap。给定目标$\varepsilon>0$，取

$$\varepsilon_P=\varepsilon/3,\qquad
\kappa=\min(\varepsilon/3,1/4),$$

并令$\eta_P$为P$_n$对$\varepsilon_P$给出的时间容差。选择

$$0<\eta_W\le\min(\eta_P/2,\kappa/2).$$

将时空划分成$\delta$-cubes，称cube $Q$为heavy若

$$|U\cap Q|\ge\delta^{n+\kappa}.$$

每个有界斜率tube只遇到$O_R(\delta^{-1})$个cubes，所以其落在light cubes中的shade体积至多

$$C_R\delta^{-1}\delta^{n+\kappa}
\le C_R\delta^\kappa|T_i|.$$

因$\kappa>\eta_W$，小$\delta$时保留的$Y_i^H$满足$|Y_i^H|\ge|Y_i|/2$。每index标记所有与$Y_i^H$相交的时间bins。一个时间bin内tube体积至多$C_R\delta^n$，故

$$\#J_i\ge c_R\delta^{-1+\eta_W}
\ge\delta^{-1+\eta_P}$$

于小$\delta$成立。相应中心访问cell距某个heavy cube只有$O_R(\delta)$，所以

$$\delta^n\#E\le C_R\delta^n\#\{Q\text{ heavy}\}
\le C_R\delta^{-\kappa}|U|.$$

另一方面$|Y_i|\le2|Y_i^H|\le C_R\#J_i\delta^n$。因此(P)给

$$\sum_i\omega_i|Y_i|
\le C_RA\delta^{-(\varepsilon_P+\kappa)}|U|
\le C_RA\delta^{-\varepsilon}|U|.$$

这严格处理了任意可测shade；没有把其$\delta$邻域体积免费等同于自身体积。上述互推仅针对固定bounded chart及固定倍tube/cell变化。若转换普通Euclidean tube集合或改变chart时间长度，还须固定半径/长度比较并重新吸收密度常数。

故在所写bounded-chart类中，**P$_n$与W$_n$在“每$\varepsilon$存在$\eta$”的量词意义下等价**，而非相同$\eta$、相同损失的逐式等价。

## 5. U$_n$到任意权重：抽样没有四维新障碍

以下为companion Lemma2.2证明的固定$n$版本。令$v_i=\omega_i/A$。以$K=T_i$测试得到$v_i\le1$，用环境球测试得到

$$S:=\sum_i v_i\le C_{n,R}\delta^{-(n-1)}.$$

若U$_n$只对标准Euclidean tubes陈述，可先把每个chart tube扩成共同固定长度、半径$C_R\delta$的Euclidean tube$\widetilde T_i$。有$T_i\subset\widetilde T_i$、体积相差固定倍；含$\widetilde T_i$的凸体亦含$T_i$，故其weighted convex cap只变固定倍。原shade仍在内，密度只损失固定倍。最后将共同长度缩成1并缩小输入$\eta$以吸收这些常数。此处不能只引用“形状可比”而忽略cap的方向。

独立以概率$v_i$抽取每个index。John椭球及$O(\delta^2)$精度的center、frame、axis量化，把所有相关凸体cap压到至多$\delta^{-C_{n,R}}$个盒测试；每个测试盒体积至少常数倍tube体积。指数矩界加union bound使样本的全部凸聚类至多$C_{n,R}\log(1/\delta)$，概率至少$3/4$。当$S\gtrsim\log(1/\delta)$，另一个下尾界给样本数至少$S/2$，亦有概率至少$3/4$。

每条完全重复tube的样本重数至多$C\log(1/\delta)$；只留其中一个**原index连同其自己的shading**，仍有$\gtrsim S/\log(1/\delta)$条不同tube。不能把不同index的shadings合并后声称每index密度不变。

对保留样本调用U$_n$，目标损失取$\varepsilon/2$，逐index密度容差取其输入容差的一半以吸收固定常数。对数聚类满足$\Delta_{\max}\le\delta^{-\eta_U}$。因此

$$|U|\gtrsim\delta^{\varepsilon/2}
\frac{S\delta^{n-1}}{\log(1/\delta)}.$$

而$\sum_i\omega_i|Y_i|\le C A S\delta^{n-1}$。吸收对数即得(W)。若$S\lesssim\log(1/\delta)$，直接逐点用$\sum_i\omega_i1_{Y_i}\le AS$，无需依赖样本下尾。常数均独立于index数、重复次数和权重极差。

这只说明：**若有U$_4$，加权化本身可以执行。** 它不证明U$_4$；已归档GWZ输入是U$_3$。

### 5.1 从W$_n$返回平均密度的U$_n$

若$\Delta_{\max}\le\delta^{-\eta_U}$且平均shade密度至少$\delta^{\eta_U}$，删去密度低于$\delta^{\eta_U}/2$的tubes，则剩余shade总量至少原总shade的一半。对剩余集合以权1、$A=\delta^{-\eta_U}$调用(W)。若W的目标损失为$\varepsilon/4$，且$\eta_U\le\min(\eta_W/4,\varepsilon/8)$，则

$$|U|\gtrsim\delta^{\varepsilon/4+2\eta_U}\sum_i|T_i|
\ge\delta^\varepsilon\sum_i|T_i|$$

于足够小$\delta$成立。两个$\eta_U$分别来自原平均密度和凸聚类常数，不能漏掉其中一个。这样在调整容差之后，U$_n$、W$_n$和P$_n$属于相同强度的bounded-chart输入。

## 6. Quadric族为什么直接检验并否定无方向WP4

已读Zahl survey §4.1的原文：$Z=\{(a,b,c,d):ad-bc=1\}$含三维line family；$N_\delta Z$中有约$\delta^{-3}$条essentially distinct tubes，其全族存在$\delta^{-1/2}$凸聚类过量。作者给出随机稀疏化及copies的convex-Wolff反例。**survey展示过量下界不等于本文独立证明全族的matching upper bound**；全族所有凸体/框的精确上界由本轮反例主稿另核。

可直接检查的转移命题是：若有固定bounded chart中$\asymp\delta^{-3}$条完整traces，全部位于一个四维mesh覆盖数$O(\delta^{-3})$的quadric邻域，且其未加权凸聚类满足

$$\Delta_{\max}\le C\delta^{-1/2}\Lambda(\delta),$$

其中$\Lambda=\delta^{-o(1)}$（例如常数或对数），取统一权

$$\omega_i=c\delta^{1/2}/\Lambda(\delta).$$

则加权凸聚类为常数，由§2.1得到WP4的$A=O(1)$。所有time bins都标记，故任意固定$\eta>0$的门槛自动满足。计数为

$$\sum_i\omega_i\#J_i\asymp
\frac{\delta^{-7/2}}{\Lambda(\delta)},\qquad
\#E\lesssim\delta^{-3}.$$

所以

$$\frac{\sum_i\omega_i\#J_i}{A\#E}
\gtrsim\delta^{-1/2}/\Lambda(\delta),$$

直接违背任意固定$\varepsilon<1/2$的WP4。等价地，weighted tube总量$\asymp\delta^{1/2}/\Lambda$而union体积$O(\delta)$，违背(W)。**一旦全凸体cap已认证，无需随机copies，也无需削弱时间密度来制造失败。**

这些quadric直线的方向满足其二次型的null条件：把$\det(x_0+tu)\equiv1$展开，其$t^2$系数为$\det u=0$。因此方向本来位于真代数薄层，未包含所有四维方向，也不提供方向分离/完整方向分布。Full-time框cap没有排除这种二次曲面聚集；权重和重复index不是障碍的来源。

### 6.1 本轮已完成的实例化

`notes/50_counterexamples/R0007_weighted_plank_obstructions.md` 已给出显式$\mathcal Q=ty+xz-1$参数族，直接证明所有full-time空间框的连续cap

$$\mu(P)\le Cw_1\min(w_2,w_3^2)$$

及离散cap$N(P)\le C\delta^{-1/2}\prod a_j$。本文作者已独立逐项审查，报告为 `research/reviews/R0007_quadric_plank_review.md`；不是从survey某个坏框的下界反推upper。因此上面的转移现可取$\Lambda=1$，本轮WP4反例的全部框假设已获得直接证明。

具体统一权重为$C_{\rm cap}^{-1}\delta^{1/2}$，$A=1$、满时间标记、访问cell数$O(\delta^{-3})$、加权访问总量$\gtrsim\delta^{-7/2}$。WP4对任意$\varepsilon<1/2$均不成立。主稿的全部上界证明与本笔记的plank/union互推保持独立记录。

## 7. 收束与不应误报的结论

本轮互推把缺口具体定位在无方向四维凸聚类并集估计，而非weighted sampling、mesh量纲或时间密度转换。上述证明各步均保留$A$、$\varepsilon/\eta$及逐index长mark条件；任意cross-section另付过重cell损失后才取得相同量词强度。

四维满Hausdorff维数并不自动给U$_4$/W$_4$/WP4，而quadric反例正针对后者的无方向量词。本轮主稿已对**所有**full-time框完成cap证明，见§6.1；反例依据是该全上界及满时间计数，不能只凭曲面或最坏框下界。否定此加强输入没有否定五维Kakeya；下一次正向输入必须明确排除这里实际出现的二次曲面/方向退化，且重新核查是否能从真实Kakeya来源保留到调用层。
