# R0089：原质量、降次数预算与停止范围正式独审

2026-10-18，B。本文恰六个编号二级节；仅审明列的有限归约、工具应用、算法证书和接口反攻。完整H5门未证未否，未经外部同行评审，不认证未来元数据、Git或同步。

## 1. 实际全文对象与独审层级

已fresh实际全文读 root 主稿 `notes/30_algebraic_geometry/R0089_original_shadow_cuts_degree_budget_and_graininess_boundary.md` 十节，A 主稿 `R0089_cut_propagation_and_degree_reduction_audit.md` 十节，B 主稿 `R0089_original_incidence_and_graininess_counteraudit.md` 十节，working_spec 五节、终macro六节、next六节、source_scope六节及两个阶段I gate各八节。A新增有限no-first段与最终cross记录均已读回；本 formal 正证主核root/A，B自证不算本人的独立审查。root/A已实际全文独核B的两实体反攻和有限概率式，无未解决数学必修项。

本轮primary实际读Guth1402.0518v1 intro/Hyp0.2、Th0.4/0.5、完整§1及§2.2证明，并对照本地extracted PDF8–16，另读§2.1相邻随机模型。没有重新独证整40页后半高级曲率/graininess wholeproof，没有本人的渲染、下载或源bytes核验。Stone–Tukey、relative isoperimetry及标准面积公式保持其通常具名层级，具体原质量、根计数与概率应用则已逐步复算。

阶段I辅助source的实际读域也保留：Yomdin0911.1937v1的相关定义、Th1.3/2.1证明和采样声明；Brudnyi–Yomdin1312.6050v1的norming与§4倒数稳定性；2511.10918 currentv4/GAFA的相关statement和§1.5比较。后者未完整审Appendix A高级证明；不能从出现其标题或statement冒记完整wholeproof。R69早已记录v4，fresh确认不算新发现。

## 2. 共同shift、原N/I及root peeling的独立核算

对一个共同平移格 \(G_\xi\)，\(K_\xi=\#(E\cap G_\xi)\)、\(J_\xi=\sum_i\#(Y_i\cap G_\xi)\)。Fubini给期望 \(\delta^{-5}|E|\)、\(\delta^{-5}I\)；原unit round管连端帽均有格点数 \(\le C/\delta\)。以 \(C_0\lambda^{-1}\delta^{-5}|E|\) 截大K phase，利用 \(J_\xi\le CJ/\delta\) 真正控制坏phase的incidence期望，故可在同一个phase同时保

\[
K\le C\lambda^{-1}\delta^{-5}|E|,
\qquad J_{\rm grid}\ge c\lambda J/\delta.
\]

这两条件不是各自独立选shift。heavy和固定颜色仅损固定比例总incidence，保 \(J'\ge c\lambda J\) 原labels及逐row \(\ge c\lambda/\delta\) 的实际marks；方向分离保留，满方向和原管数不免费恢复。cube中心是原Yi的点，cube本身可出E，文中没有把cube并或 \(N_\delta E\) 代替真实Lebesgue E。平均版从总I起步，与逐管版的逻辑层级分开。

root§5的两次degree分桶及peeling亦成立。设column桶有 \(K_1\) 个columns、度数 \([\rho,2\rho]\)，row桶保 \(A_2\ge cK_1\rho/L\) 边、row度数 \([M,2M]\)，\(L=O(\log\delta^{-1})\)。删除当前degree小于 \(M/4\) 的rows，累计最多丢 \(A_2/4\)；删除degree小于 \(\rho/(CL)\) 的columns，累计最多 \(K_1\rho/(CL)\le A_2/4\)，取C足大。每节点仅删一次，故最终仍保 \(A_2/2\) 边。

保留的row上下常比、column上下只polylog比，原N/I与层损失都仍在账上。这不是whole geometric intersections的全局均匀化，也没有提取固定角star或全空间multiplicity upper；root/A明确保留这些限制，未以selected graph换掉原source分母。

## 3. 全n cut及原质量hyperplaniness的正向范围

Guth Def1.1/Lem1.3/Cor1.5和Lem1.6确为固定任意n工具。细网ham-sandwich可在R5以 \(D\lesssim_{r_0}K^{1/5}\) 同步cut所有给定格；它不抽最高次项，确避开R56的特定conditioning费。Lem1.6中纵向根计数、扩张gap有界重叠及Fubini给投影总量 \(O_n(D(R+1)^n)\)，从而坏gap数 \(O_n(r^{-4n}D)\)；好gap通过纵移球保符号体积。它没有控制最外anchors之外或坏gap的clock质量。

root/A的标准原图正算逐步通过。cut在每Q内给符号边界regular部分的面积 \(\ge c\delta^4\)；去掉偶因子与无关重数不增degree，singular residual不承载四维面积。面积平均可选一个实际法向 \(n_Q\)，而对每原tube在固定fat tube中用纵向面积公式和几乎所有平行线的至多D个根，得

\[
\sum_{(i,Q)\in A}|n_Q\cdot v_i|\le CJ'D,
\quad
\frac{\#\{(i,Q)\in A:|n_Q\cdot v_i|>\theta\}}{|A|}
\le\frac{CD\delta}{\lambda\theta}.
\]

取 \(\theta\asymp\sqrt{D\delta/\lambda}\)，结合诚实K上界即

\[
\theta\lesssim\lambda^{-3/5}\delta^{(1-\gamma)/10}.
\]

这确实保原selected-incidence分母，且η可在γ后足小以得到正幂角误差；不需先假每格多方向。它只给每格独立的4-plane，未给沿原tube慢转或coarse graininess。

源Hyp0.2/Th0.4与Th2.2没有混用：主graininess的global upper/三方向条件不能漏，较一般的R3 Th2.2只用row/column近均匀和相对任一方向的定量横截。后者proof额外用访问rank均衡、横截Bernoulli独立和对全部原T′的bad-event平均保质量。这些不是原δ方向分离自动赠予的输入，也不被本文正向hyperplaniness补齐。

## 4. 两跳次数、Crofton方向及有限graph Chernoff证书

独立重算该seed算法：R5 degreeD自由度 \(\asymp D^5\)，每seed需要 \(O(D)\) cut anchors，故预算seed数 \(O(D^4)\)。在理想近均匀图 \(JM\asymp K\rho\) 上，目标row的预期seed触及数为量级 \(M^2D^4/K\)。要供应 \(\gg D\) 个可传播anchors，只有

\[
D^3\gtrsim K/M^2
\]

这一特定两跳预算；不能叫所有可行P的universal lower，更不能改写成 \(D\lesssim K/M^4\)。当K只给upper时，也不能反向推相同次数lower。Crofton则由切K个格的面积lower与 \(\mathcal H^4(Z(P)\cap B_L)\lesssim DL^4\) 给 \(D\gtrsim K/L^4\)，方向是lower，不能冒constructive upper。原文physical13局部比较的排印方向不改变这个独立计算，也不足以否整篇定理。

有限graph证书的常数与量词均过。row degree≤2M、column degree≤2ρ，使固定row的不同邻rows≤4Mρ；条件该row非seed后，邻seed indicators仍独立。若任两row共columns≤B，hits≤BX。取 \(k=\lceil D/B\rceil\)、\(p\le\min(1,cD^4/J)\)，在尾界非平凡的范围

\[
\Pr\{\exists\text{非seed row有}\ge D\text{ hits}\}
\le J\left(\frac{e\,4M\rho p}{k}\right)^k.
\]

以 \(JM\asymp K\rho\) 消去原J，控制比率确为 \(CBM^2D^3/K\)。取其小于固定常数1且 \(D/B\gg\log J\)，或更一般满足相应log-tail条件，才有高概率无第一条新active row。seed-count预算可与此事件同时保留；独立指标的Chernoff或更弱的Markov均可作实际存在性选择。

由“无首个新row”推出任意代**同一graph-certified阈值规则**不能启动是正确的。原H5不自动有固定B，P也可能偶然cut未认证格；相关/非均匀seed和新几何没有被排除。故本证书不是H5反例、连续Kakeya否证或对所有多hop算法的普遍界，root/A未越过这个范围。

## 5. 两实体反攻、coarse未付及辅助来源排重

坏gap反攻是真多项式例而非仅一句警告：固定cut参数r，先对固定横向盒内高频sin作多项式一致近似，sign-sin的有界primitive和小近零带给全部相关球严格cut margin。\(P_H=P_0(y_1)+At(H-t)/H^2\) 在两端长S的anchor clusters及其相关球上只加小扰动，而中部同正；\(H\gg S\)、\(S\gg C_r\deg P_0\) 可同时选。degree固定、少数大gap承载几乎全部clock或marks，严格否“坏数量小⇒坏质量小”。它是单管/非rank均衡例，不满足完整full-direction小footprint H5；原文自己的Lem2.4/2.5已另付所需的rank与随机分布，文中没有把反攻升级为原定理反例。

\(Z=\{x_5=x_1x_2+x_3x_4\}\) 的梯度末项1，光滑；每点四个coordinate tangent directions都给真实整直线、定量张满tangent，而 \(\mathrm{II}\) 是非零signature(2,2)二次型。在二维tangent的RP1上三个不同零方向迫二次型零，在四维tangent却不能如此；Sym²的责任不能由线性span代替。该族方向受leading cone约束，没有原满S4方向，也不是H5反例。

coarse四维调用未付范围明确：逐Q的4-plane未沿管coherent，未保共同grain包中的原N/I、短clock、投影重复和方向cap；高degreeδ依赖carrier也不能免费当fixed-format旧G3/G4输入。cut工具确绕开R56 scalar费，但没有完成锁定的小degree加coarse门。停止决定没有把desired spread/mixing/ADlower附成成功假设。

阶段I的Yomdin、Brudnyi–Yomdin采样前提和次数指数没有被隐藏，特别倒数norming稳定性不授uniform upper。2511.10918v4在R69已记，现有全维fixed-format局部containment计数与只R3/allscale Frostman PW应用不授普通R5初始化；相关版本、定理statement和高级wholeproof层级分别保留。没有借这些排重重新包装DIM/KT或旧正幂等价方向。

## 6. 必修项、最终限定verdict与冻结

数学逐步核算后，**无未解决的强制修正项**。曾向root指出来源读域文字须明确2511.10918部分仅相关statement/比较读域，未完整审Appendix A高级proof；root已收紧source_scope§4，本人已fresh全文读回最终六节确认修复。该项是阅读声明的字面修正，不改变数学结论；本 formal 不据source记录扩张本人的阅读声明。

在共享格原质量、全n cut工具应用、标准hyperplaniness、所列两跳及有限graph算法预算、具体坏gap/II接口反攻和停止范围内，结论为 **全文通过**。完整H5降次数/coarse门仍未证未否；没有普通维数提升、完整branch saving、full-direction反例、新数学ID或major。两独审分工与具名高级wholeproof分开，本人的施工不冒本人独立审查，**未经外部同行评审**。

终macro/next六节实际读过，保持四完整路径、Goal active和保守streak12；仅停止本次直接接法，不否一切polynomial/cut/多尺度策略，也不以更多hop、degree/λ/r参数或quadratic-spread公设续名。未认证未来metadata、Git、哈希或同步，formal完成后冻结本轮编辑和检索。
