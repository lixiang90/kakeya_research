# R0098：primary、原wholeclock与定量current用途终审

2026-10-19，A。本文是内部逐步审查，未经外部同行评审。仅认可实际读取及以下限定数学范围，不预认证元数据、版本存档、Git 或未来同步。

## 1. 实际全文对象、原文读域与审查分工

本次 fresh 实际全文读：root《R0098_planar_measure_wholeclock_and_ambient_gate》12节、A《R0098_ordinary_HRZ_primary_reselection》12节、B《R0098_full_rough_source_joint_input_gate》12节；reselection／working 两份各5节；终 macro、next、source-scope、round 各6节。root§4 strong-L² 整合、§5 analytic carrier／support closure，B§9 determinant prior 作者修订均实际读回。

primary 实际读域：官方 De Philippis–Pigati 2601.10647 history（current v3，2026-09-01），HTML §§1.1–1.3、Th1.6–1.7／Th3.1、Rem3.2／Cor3.3–3.4、相关 §3 开头及 §4 应用输入；本地提取的对应 Th1.6／1.7／Rem3.2／Addendum 另实际读回。BDH 2404.04754 官方 history 仅 v1，HTML §§1.1–1.3／2.2–2.4 原定理、BL 量词和固定参数化常数已读。不是两篇高级 wholeproof 的新独证，也未新独审 prior [13] 全文。parent 的 PDF 视觉／字节记录与本人阅读分开。

A 参与 primary 筛选、dilation 和 strong-L² 校准，自身 A12 不算自身独审。相应正证由 root／B 实际逐式重算；本 review 的独立重点是 root／B 的原 current 构造、真实 functional、closedness／shading／slicing 及 native 出口。有限计算、具名来源、内部 reviewed 与外部同行评审分别标记。

## 2. 原measure定义、wholeclock端点和真实量词

λ=|S|+|T| 下按一次齐次公式定义 SP／SN／TP／TN，再取 measure infimum ν=min(SP,TP)，不依共同支配测度的选择。原 theorem 的 χ 范数是 Leb² 的 L²；两个 cone 各自总质量正，并不提供 ν 的共同质量。root／B 没有偷偷加 determinant≥0 到新 Th1.7，或将其 measure 版本误拒为仅光滑场。

原 whole-unit-segment γ_v(t)=a(v)+tv 经 rank2 正交 P 后，按真实速度 Pv 的正向两 cones 分组，S=∫w(v)∫Pv δ_(Pγ_v(t))dt dσ。对测试函数沿 t 积分，DivS=∫w(δ_(Pa)−δ_(P(a+v)))dσ，符号、无额外速度因子及 TV≤2∫w 正确；M_S≤∫w|Pv|。T 同理，实际 B≤6，bad parts 为零。direction restriction 保 absolute upper，归一化时必须保其原质量；未授独立角／共同位置 lower。

若原 K 非闭，只能说由 analytic P(K) 承载（在完成测度中解释），support⊂closure(PK)。原主文将 support⊂PK 的字面误用改正后已读回；非测原 K 用 R91 已付的同维 Borel hull／a.e. selector，不能把 hull 段当仍逐点位于原任意 K。没有新增 anchor 正则性、连续 selector 或完整原 directions 的新认证。

## 3. 完整缩放强度，以及zero-bad旧强L²覆盖

S_L=L(D_L)#S 是 physical current dilation，DivS_L=(D_L)#DivS；mass 和正／负部乘 L，Div TV 不变，||χ(·/L)||_2=L||χ||_2。root／B 除 L 后的式子和 A=Leb²(E)≤1 取 L=A^(−1/4) 正确，给

    ν(E)≤CB A^(1/4)+N，

其中 N=(SN+TN)(R²)。A=0 用 L→∞；A>1 用总质量即可。N=0 的 level-set 先 bounded 截断再极限，确给 weak-L^(4/3)，一般只可保含 N 的不等式。固定 unit box 的 flux lower 不能否定这个合法缩放输出。

强度校准也逐步成立：N=0⇒Sx≥|Sy|、Ty≥|Tx| 作 measure。对正概率 mollifier，Sε,Tε 及一阶导数属 L²，Div 卷积的 L¹ norm≤原 D；ν*ρε≤min(SεP,TεP)。写 Sεx=a+p、Tεy=b+q，其中 a=|Sεy|、b=|Tεx|，则 det≥(a+p)(b+q)−ab≥pq≥(ν*ρε)²，且两个指定坐标非负。具名 Th1.6／3.5 因而给 ∫(ν*ρε)²≤D_SD_T/4。L² weak compactness／分布极限给

    ν=f dx，||f||_2≤√(D_SD_T)/2；
    ν(E)>0 ⇒ Leb²(E)≥4ν(E)²/(D_SD_T)。

D_SD_T=0 时 ν=0，不作除零。原 statement 明列该 determinant 估计已见 Guerra–Raiţă–Schrecker [13]，Ars Inven.Anal.2024；B 的 Firester–Tsiamis 误归属已改并读回。故实际 zero-bad bridge 已被更强旧 planar multilinear 覆盖，不能把弱型当新 ordinary 输入。新 Th1.7 一般 bad-N 版本没有被此推翻，也不免费截正部后授 finite Div。

## 4. 独立反攻：flux、functional值、marks与conditional边界

bounded 正 cone current 用坐标乘 cutoff 测试，∫Sx=−∫x dDivS≤R D_S；SP≥(1−a)Sx 且 SP≤Sx。其意义是固定 chart 不能凭 δ 令 endpoint 费用消失，不是所有 dilation 后不等式均无效。

真实 full-angular 原点单位 bush 在每个 rank2 P 下，非零 projected position 与速度同向。横、竖正 cones 的空间 sectors 不交，原点无 clock atom，故 SP、TP 总量各正、bad0，却 ν=0。该计算在同一个 positive-volume 原集合进行，不反 Kakeya，也不反完整 small-label／point-Φ source；它精确否定从 global cone 质量赠 local overlap 的一步。

等密度 m 个 clock intervals 的零延拓导数为左端正、右端负，单线 TV=2m；A 原负号已按 B 独审实修为正 D_t。有限 generic P 的端点可避碰撞，但没有冒 continuum 投影后也有同样 TV lower。真实 round-tube marks 的内部 cylinder／端帽常数与平均、逐管密度区分正确；两种密度均不自动控 BV。

root§9 的斜线 conditional 校准亦成立：例如 v=(1,0,1,0,0)/√2，P=(x1,x2)、Q=(x3,x4,x5)。相对 Q#dt 这个一维 law 的 planar conditional 是非零向量乘一个 Dirac；其 Div 对 bounded oscillatory 测试可无界，非 finite measure。不能把它当 Leb³ fiber law，也不能从完整 Div finite 把横向抵消赠到每个 planar slice。此例只否一般 slicing 闭包，不是全方向反例。

## 5. 原native几何、HRZ比较与二维出口边界

实际重读 WZ Def17.4 的 (103) 及上下文：mixed42 中 f1∈R²、f2 scalar，β1 scalar、β2 为二元 row；f2=β1+β2f1，故 (1,f1,f2) 位于 native horizontal W_t。若 time-preserving 光滑 π=(q,t) 真在 native plane 的相对 open patch 恒定，D_xq annihilate W_t，同一个 p 两角的速度差 (φ−φ′)(1,f1,f2,0) 被消去。root／B 没有把有限 filled X 自动升为这项光滑假设；也没有从同 p collapse 宣整个 pushforward ν=0。跨 fiber 不同 ξ 的混合质量仍未付。

即使有 ν lower，平面 positive area 只直接返回维数≥2；不提供 R5 footprint 的 fiber lower、R4 直管模型、方向 cap 或完整 Hausdorff 全尺度返回。π=(filled-coordinate,time) 的完整二维 packing 属 R95 已付饱和门，不因换工具题名产生新 gain。

BDH 固定 smooth nested frequency flags／deepest regularized-BL 的新局部化定理，未从原 HRZ narrow 给出这些 flags、原 marks／parent clock 预算及统一条件数；其几何 KBL 原 statement 具名旧来源。R48／61／63 的具体质量和尺度指纹保留，不仅以“缺完整 Lp”粗拒，也不续旧参数优化。

## 6. 修正、终macro／next与最终判定

已解决的实际修正为：root 非闭 Borel carrier／support 混用，A clock-mask 导数符号，以及 B determinant prior 作者；皆已实际读回。另独审补出 zero-bad strong-L²，终 root12／macro6／next6／source6／round6 已实际完整读其整合范围。当前**无未解决强制项，全文在上述有限范围通过**。

终 macro 保四条完整路线、ordinary／fullbranch-saving 时钟21、实际数学信息与 gain 分开。next 只要求下一轮先读 addendum 指向的 concentration-sequence／任意维 MS 原定理，比较旧 R91 singular-polar 与原算子／分母／clock／ambient 责任；它明说目前只核 abs/history，不预授新定理适用或新增成功假设。本人未打开这三篇新文献的 theorem／wholeproof，故不认证后继结论。Prop1.9 的等价范围不被误写成“当前任意维 MS 未证”。

本轮只认可来源适用、定量 current 后果、既有更强输入覆盖及所列桥反攻。完整 ordinary／HRZ／rough sticky 及 ordinary 初始化、真实 full-direction strict低维四路均未解决；未否一般 Kakeya、所有 PDE／projection 方法或新 Th1.7。无 new ID／major／ordinary 增益或 novelty 认证，Goal active，未经外部同行评审。档案字节／库计数依 root 的独立记录，不预认证未来 metadata、Git、验证或同步；round 的完成态须在实际审稿后据实收尾。
