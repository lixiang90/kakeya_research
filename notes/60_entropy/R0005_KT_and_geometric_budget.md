# R0005：KT有限集方法与原生系数熵的几何接口

日期：2026-10-16。互补任务：N5-ENT-01。只读取已入库文献与源码，没有新搜索或下载。本文的初等熵与线性恢复命题不声称新颖性；没有推出新的Kakeya维数下界。主线有限熵率候选的独立核验已完成，见§5。

## 1. 本轮确实读取的KT输入

一手来源：Katz–Tao, *New bounds for Kakeya problems*, arXiv:math/0102135v1，2001-02-16。已入库 `literature/primary/katz_tao_2001_v1_new_bounds.pdf` 与对应抽取文本。这里只评估该版本中读到的论证，不把它标作全部后续文献的最终最强表述。[作者原稿](https://arxiv.org/abs/math/0102135)。

| 原稿位置 | 可核验机制 | 与当前方案的区别 |
|---|---|---|
| §2，pp.2–3；§3，p.3，(2)–(3) | $\pi_r(a,b)=a+rb$；任意两个不同投影共同确定$(a,b)$；另要求差投影$\pi_{-1}$在$G$上单射 | 两时刻恢复只对应第一条线性参数化；差单射是额外的方向唯一性输入 |
| Theorems 3.2–3.3，pp.3–4 | 比较同投影的成对元素集合$\mathcal V$，构造可由两套双投影恢复的$\nu$，迭代popularity后得$\#G\lesssim N^{7/4}$ | 增益来自不同轨道之间的重叠计数，不是单条轨道的可恢复性 |
| Lemma 3.4、Corollary 3.5，pp.4–6 | 在$\nu$纤维内再次应用sum-difference估计；$\beta\mapsto(4\beta-1)/(2\beta)$，固定点$1+\sqrt2/2$ | 必须构造有大量成对重合且仍满足方向单射的子问题 |
| §4，pp.6–12 | 使用三元素corner及另一层纤维，处理不同切片的非均匀性，极限指数满足$\alpha^3-4\alpha+2=0$ | 不能略掉严格证明中的popularity与切片切换，把启发式均匀性直接当成熵独立 |
| §6，pp.18–24；Theorem 6.2 | 取消固定切片，使用angle-pivot构造、近共面性及hairbrush/Córdoba计数；$K(n,d)$与$K(d+1,d')$推出$K(n,(2n+1+d')/4)$ | Hausdorff增益含真正的跨轨道几何；并非只由投影的熵链式法则给出 |

该PDF的抽取文本没有出现`entropy`一词；原稿在此用基数、纤维数、popularity和几何重叠表达论证。可以对某些参数化步骤作Shannon熵解释，但不能据此说“KT已经证明本文每条加权条件熵命题”，更不能把“熵”称作当前方案相对于KT的新输入。

最基本的区别可直接量化：对$G$上均匀分布的$(A,B)$，两个投影的可恢复性仅给

$$\log\#G=H(A,B)\le H(\pi_r(A,B))+H(\pi_s(A,B))\le2\log N.$$

这就是基本的两投影指数2。KT的$7/4$及以后指数需要上述重叠结构。一般非均匀prior还需处理权重与选择，不能把$H$无损等同为整个支撑的对数基数。

## 2. 两时刻可见base不会创造新的隐藏信息预算

**命题KT-COMP-01（恢复恒等式）。** 固定先验上的可见仿射轨道为$Y_t=y_0+tV$，令$W$为任意隐藏斜率，$s,t\in[0,1]$为两个固定且不同的时刻。在精确随机变量层面，

$$\sigma(Y_s,Y_t)=\sigma(y_0,V),$$

且在已经条件于$V$之后，

$$I(W;Y_s,Y_t\mid V)=I(W;y_0\mid V).\tag{K5.1}$$

这里若连续互信息无穷，可改用有限量化变量或理解为信息生成的$\sigma$代数等价。证明只有

$$V=(Y_t-Y_s)/(t-s),\qquad y_0=(tY_s-sY_t)/(t-s),$$

以及给定$V$时任一$Y_s$都与$y_0$相互确定。

在共同原始网格$p$上，若$|t-s|\ge c>0$且所有可见系数在固定盒内，量化恢复误差为固定倍$p$，每个cell的反向选项数有固定上界。因此相应有限熵与互信息恒等式有$O_{c,j}(1)$误差。若时间间隔变小，必须改用$p/|t-s|$精度或支付$O_j(\log(1/|t-s|))$的bin损失，不能仍写$O(1)$。条件于$V_p$后，$(Y_s,Y_t)$和$y_0$也只在这些网格误差内等价。

所以把同一原始网格的$y_0,V$换成两个可见时刻，不能使已得到的$I(W;y_0\mid V)$下界成为更强的几何结论。新约束必须还连接不同方向/不同轨道，例如某个真实共享点纤维中的重叠、共同小支撑或条件独立性。

在特殊线性隐藏测试$P_*=w-Q(t,y)$中，给定$y_0,V$后，$x_2$已由$V$决定，而两个相隔固定距离的$X_s,X_t$可恢复$x_0,x_1$。这也只把native coefficient信息换了坐标。一般源稿测试允许$w^2$，不能无条件宣称$x_2$仅由$V$决定；从原生信号回到$W$须另外处理隐藏二次反解、分支与原始分辨率。

## 3. 同prior双边系数界和完整斜率密度仍不足：明确反例

以下模型否定一种**仅使用部分输入**的推论：即“native coefficient箱双边界、完整斜率密度上界、两时刻代数以及point/velocity确定系数的短列表，自动给出超过方向—截距相关性的隐藏熵约束”。它不是满足全部source物理支撑/临界路径输入的反例。

### 3.1 同一长线先验与完整系数厚化

取$j\ge2$。$y_0$均匀于$[0,1]^j$，$V_1$均匀于$[1,2]$，其余$V_i$均匀于$[0,1]$，彼此独立。取$d=1/2$。令$c$服从base4 digits为$\{1,2\}$的等权Cantor测度的有限层平滑版：截断到长度$\ell=4^{-L}$后，在每个末级cylinder的中间三分之一区间均匀分布。

事先给定有限组dyadic网格$p\ge p_{\min}\gg\ell$。对每个占据的$c$-bin，有

$$\mu(c_p)\asymp p^{1/2},\qquad
\operatorname{dist}(\operatorname{supp}\mu,\partial c_p)\ge p/6.$$

偶数dyadic层的bin质量为$2^{-k}$，奇数层为$2^{-(k+1)}$，故第一式可直接逐层核验。边界距离来自每个base4 cylinder尾部位于其$[1/3,2/3]$相对区间；奇数层的最小距离为其dyadic宽度的$1/6$。

独立取$\zeta$均匀于$[-\eta,\eta]$，$\eta<p_{\min}/12$，定义真正的完整仿射线

$$y(t)=y_0+tV,\qquad w_0=c,\qquad
W=y_{01}+c+\zeta,\qquad w(t)=w_0+tW,$$

以及固定native test

$$P_*(t,y,w)=w-ty_1.$$

从$(y_0,V,c,\zeta)$到完整$(y_0,V,w_0,W)$的Jacobian恰为1。只要$\ell^{-1},\eta^{-1}$是固定原始$N_0$幂，先验就是多项式高度、在多项式个固定次数半代数pieces上分段常Lebesgue密度。它并非仅存在于低维参数图上的奇异prior。

所有$t\in[0,1]$上，

$$X(t)=P_*(t,y(t),w(t))=(1+t)c+t\zeta-t^2V_1,$$

$$\boxed{(x_0,x_1,x_2)=(c,c+\zeta,-V_1).}\tag{K5.2}$$

原生系数一致有界，$\partial_wP_*=1$，$\partial_{ww}P_*=0$。完整斜率$(V,W)$的密度有一致常数上界：给定$V$，$W$是均匀$y_{01}$与独立$c+\zeta$的卷积，密度不超过1。这个上界不随$\ell,\eta$退化。

### 3.2 系数双边界、矩形upper cap和短列表均成立

记$\pi$为$V$边缘。在每个prepared $p$上，$c+\zeta$与$c$属于同一个dyadic bin，而$[-V_1]_p$由$[V]_p$唯一决定（忽略零质量边界）。因此对**同一归一化先验**$\nu$的每个参与完整native coefficient箱

$$B_p=[y_0,V,x_0,x_1,x_2]_p,$$

有

$$\boxed{\nu(B_p)\asymp p^{j+d}\pi([V]_p).}\tag{K5.3}$$

这里没有逐箱改变prior，也不需要事后重新归一化来恢复lower floor。

给定$t$和$V$-bin，$Y_t$的$p$-box限制$y_0$到体积$O(p^j)$；$X_t$的$p$-interval再限制$c$到长度$O(p)$，因为$1+t\in[1,2]$。Cantor cap给

$$\nu\{Y_t\in B_p^y,X_t\in J_p,[V]_p=J\}
\le Cp^{j+d}\pi(J).\tag{K5.4}$$

同理，给定$(t,[Y_t,X_t]_p,[V]_p)$，先恢复$y_0$到$O(p)$，再由(K5.2)恢复$c$到$O(p)$；$x_0,x_1,x_2$及整个$B_p$只有$O(1)$个选项。这正包含“point+velocity的native coefficient短列表”形式，但不声称是source的全部observation/parent知识。

### 3.3 任意两个固定时刻只重复同一个Cantor信息

令$C_p=[c]_p$，$S_p=[y_0,V]_p$。由(K5.2)–(K5.3)，

$$H([x_0,x_1,x_2]_p\mid S_p)
=H(C_p)=d\log(1/p)+O(1).\tag{K5.5}$$

任意固定$s,t\in[0,1]$，给定$S_p$后，$(X_s,X_t)$的$p$-bin由$C_p$确定到固定选项数；反向由任一个$X_s$便可恢复$c$到$O(p)$。故

$$H([X_s,X_t]_p\mid S_p)=d\log(1/p)+O(1).\tag{K5.6}$$

两时刻没有产生第二份独立$d$维信息。另一方面，$W$边缘在固定盒内有有界密度，且给定$y_0$后，$W=y_{01}+c+\zeta$与$c$在$p$分辨率相互确定到固定歧义。因此

$$H(W_p\mid V_p)=\log(1/p)+O(1),$$
$$H(W_p\mid (y_0)_p,V_p)=d\log(1/p)+O(1),$$
$$\boxed{I(W_p;(y_0)_p\mid V_p)=(1-d)\log(1/p)+O(1).}\tag{K5.7}$$

所以完整方向的1维隐藏熵与native条件$d$维熵相容，缺额恰由已有截距信息支付。此处没有无限条件数或奇异的完整系数prior；参数floor指数明确取$d=1/2$。但这个参数指数不等于真实观测profile，不能据此声称已越过原稿的$d=1$边界，见下一节。

它也满足主线进一步调用的mixed-scale cap：固定$A_p$后，$C_r$的$x_0$限制$c$到宽$r$的区间，因此$\nu(A_p,C_r)\le Cp^jr^d\pi([V]_p)$。对所有prepared $r\ge p$，$x_0,x_1$的粗bin相同、$x_2$的粗bin已由$V_r$决定，故$C_r$向$A_p$在给定$A_r$后的额外transfer为0。正确的固定native熵率也不能单独排除此部分输入模型。

### 3.4 明确失败的真实几何输入

该模型**不满足source (6.2)的物理支撑数**$\#W_p\le Kp^{-(j+1+d)}$。在$t\in[1/2,1]$，$X=(1+t)c+t\zeta-t^2V_1$随$V_1$扫过固定长度区间。对任意固定$c,\zeta$，从$(y_0,V_1)$到$(Y,X)$、固定其余$V_i$时，其Jacobian绝对值为$t^2$。限制到小固定参数盒，可得其物理推前有正$(j+1)$维Lebesgue体积。再对$t$积分，$(t,Y,X)$具有正$(j+2)$维体积，故实际占据箱数至少为$cp^{-(j+2)}$。

因此它不能作为Kakeya/critical反例，也没有满足全部bad-path输入；其作用是严格定位：仅从系数双边界、同prior upper cap和两时刻恢复出发，尚未使用把可见方向变化压进共同小物理支撑的关键几何条件。加入这个条件后能否产生新结果，仍需额外论证。

尤其，本文参数箱中的$d=1/2$**不是这个世界的真实hidden profile指数**。在$t\ge1/2$的固定内部区域，给定可见base后$X$（等价地$w=X+ty_1$）具有通常的一维连续变化，宽$a$的隐藏bin质量为$\asymp a$；对应典型观测密度是$n(a)\asymp a$，即$d=1$。因此该模型不属于原稿的$\mathcal C(d<1)$。这正是物理支撑计数失败的同一现象，不能把参数floor的形式指数冒充真实观测profile。

## 4. 可逐项检查的下一条几何接口

如果后续候选声称超过(K5.7)，应明确指出新使用的跨轨道条件，并在下面三项中至少给出一项真正增益：

1. 在同一个真实物理point纤维内，以完整原始方向为变量得到有效的双时刻/多时刻重叠上界；它必须强于逐方向已给的$B_p$短列表。
2. 在条件于固定祖先及同一原始网格后，证明某两个相关观测保留有正量级条件熵，从而不能由同一个$c$或已知$y_0$共同解释；不能把不同时间重新归一化的law直接相乘。
3. 把strict physical support计数与这些重叠同时结合，建立一个明确的增益量；只以“单点熵上界”替代“系数熵上界”，然后再用基本两投影参数化，不足以复现KT的$7/4$机制。

这些是候选结果的验收接口，尚不是新的几何定理。若本轮主候选仅推出$H(W_p\mid y_0,V)$小及其等价的方向—截距相关性，则本版本N5-ENT-01应按停止规则冻结，不能把它登记为超过既有投影/斜率方法的进展。

## 5. 主线候选的独立审查

已独立审查 `notes/60_entropy/R0005_coefficient_entropy_source.md` §2–3，报告为 `research/reviews/R0005_entropy_rate_review.md`。在明确的有限离散(F)、(A)、(M)、同一law及participation条件下，以下候选均通过：

$$H(C_p\mid C_r,A_p)\le d\log(r/p)+2\log K,$$

$$I(C_r;A_p\mid A_r)\le\log D+5\log K+c_y.$$

总熵下界中的velocity-reference KL项符号为正，不需affine marginal lower。两端floors/upper成立而mixed cap失败的有限-bin反例也经逐项核验。这里没有重新审查上游scalar clustering或完整几何准备。

这个rate控制了固定parent-native变量向fine affine坐标的额外transfer，确实比总熵单独饱和强；但尚未给出原始全斜率的几何增益，也未自动复现KT跨轨道重叠机制。跨native重置、隐藏反解和同原始分辨率的桥接仍是另一个命题。本文自己的反例不计作独立核验，且其真实profile为$d=1$的限制继续有效。

另独立审查了 `notes/50_counterexamples/R0005_native_coefficient_inverse.md` §7–8，报告为 `research/reviews/R0005_native_mass_review.md`。对固定式$P_*=\alpha w-\beta(tY_3-Y_1Y_2)$，同prior affine cap与$|W|\le M_W,|x_1|\le M_x$给出真正使用位置—方向联合分布的质量界

$$\nu(\mathrm{target})\le C_RA_{\rm aff}\left[p+\frac{|\alpha|M_W+M_x}{|\beta|}\right].$$

它比“$W$与截距相关”多使用了一个带横向导数1的几何薄带计数，但适用的二次形状、同一tuple和坐标范围均须单独验证。隐藏坐标缩放使$\alpha$减小时会同比放大$M_W$；该乘积不能免费消失。此部分条件命题通过复核，不代表一般native测试或真实临界路径已被排除。
