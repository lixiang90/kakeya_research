# R0007：四维源输入量词的独立复核

日期：2026-10-17（本轮于10月16日开始）。审查人：`literature_frontier`。被审文本：`notes/10_source_audit/R0007_four_dimensional_input_audit.md`。本次重点核验proof-level finite readout、j3专用zero-depth修补与generic调用的区分、原始完整斜率成本；对照已归档四维稿pp.20–25的实际计算。没有独立验证175页主证明、其全部外部输入或新的j3极值类。

结论：以下明确的条件性推导与调用区分通过内部独立复核，未经外部同行评审。

## 1. Direction-rich有限尺度读出的强度与条件

§4并未将Hausdorff主定理的statement直接替代有限估计，而是假设整条四维proof及其输入成立，再反证读出有限尺度结果。该条件不可删除。

若某固定$\sigma>0$对任意$\eta>0$均有任意小尺度的反例，选$\eta_n\downarrow0,\delta_n\downarrow0$。$\delta_n$-separation及$M\ge\delta_n^{-3+\eta_n}$使均匀混合后平滑的完整three-slope密度至多$C/(M\delta_n^3)\le C\delta_n^{-\eta_n}$，即该exact sequence中的subpower。每条至少$\delta_n^{-1+\eta_n}$个marked bins，固定倍扩大访问cells后给selected mass至少常数倍$\delta_n^{\eta_n}$。同时cell亏损给$g(1,0)\ge\sigma$，如需可先收紧固定亏损以吸收常数。

在固定bounded chart内，indices至多$C\delta_n^{-3}$、访问cells至多$C\delta_n^{-4}$；独立intercept/slope平滑的密度高度及所有盒谓词仍有统一固定多项式界。Mark中心到整time-bin的替换只用bounded speed与固定倍cell enlargement。因此Theorem2.17在finite witness选取后的后续归约可以接受这条exact sequence，而不再需要一个预先固定、跨尺度的原始集合。

所以“每固定亏损存在小density tolerance”的受限finite结论是该完整proof的合法条件读出。它仍要求near-full数量的separated完整方向及逐index长marks；没有得到任意weighted convex-clustered family估计，也没有独立证明一个新定理。

## 2. j3专用g(0,0)步骤确有更强方向来源

对源初始prior的未归一化restriction，若完整visible $V\in\mathbb R^3$密度$\le K$，保留长duration后总trajectory质量仍为inverse-subpower。每个$\rho$-velocity cell质量至多$K\rho^3$，所以占据cells至少$\rho^{-3}/K^C$。以固定有限coloring隔开cells，每cell选一个已经长shaded的实际trace，可得同阶方向丰富、$\rho$-separated family；其marks均访问原有限visited union的固定扩大。

当$g(0,0)>0$导致visited count$\le K N_0^{-\alpha}\rho^{-4}$、$\rho=N_0^{-D}$且$D$固定时，这给相对于$\rho$的固定亏损。$K=N_0^{o(1)}$可以满足上一节的固定方向数量与时间密度门槛，故条件性finite readout可排除它。原Theorem2.17初始chart本就固定有界；若另扩到subpower chart范围，仍须实际执行有界chart化/慢对角，不能宣称常数任意一致。

这只处理具有该初始full-visible-density记录的zero-depth调用。Proposition2.16的一般conditional group、greedy residual只携带未归一化prior及density witnesses，不附有这样的full-$V$边缘上界。不能把上述代表抽取免费套在generic调用，也不能从无方向WP4失败直接推出这一专用初始化失败。

## 3. S1和S2中的原始斜率损失

原稿p.23的原始mass floor和p.24–25的eligible slope volume分别为

$$m_{\rm old}/q\gtrsim m(r_0,u_0)a_{r_0}J_{\rm phys},\qquad
|\Sigma|\lesssim a_{r_0}J_{\rm phys}/q^3.$$

若完整原始slope密度只有$K N_0^\kappa$，将volume转成prior mass时确实多出$N_0^\kappa$，相除得到$ m(r_0,u_0)\le K N_0^\kappa q^{-3}$。必须有观测gain指数超过$\kappa$才迫使正horizon；旧crop质量的消去不会消掉这项。角落上界也相应多$\kappa$，用同一plank路线的zero-depth上界至多shift到$g(0,0)\le\kappa$。

对一般可见维数$j$，固定parent坐标变换给

$$V_{\rm old}=y'_c+(D/q)V_{\rm new},\qquad
W_{\rm old}=W_{\rm new}/q.$$

旧full slope对新full slope的Jacobian是$J/q^{j+1}$；再除完整parent prior质量$\nu(A)$，得到

$$C_{\rm new}\le C J/[q^{j+1}\nu(A)].$$

这里不能只用visible的$q^{-j}$，也不能混入observation density换元中抵消的时间$q$。同一固定prior的unnormalized restriction保留旧upper；normalized当前world则要支付该质量/坐标成本。

## 4. 全来源与一般优化类

已核对的$\mathcal C(d)$优化对所有cap-class problems进行，假设只有profile与terminal conditional angular cap等源明示结构；并未附原始完整斜率密度、polynomial nonconcentration或Kakeya祖先记录。Theorem2.17证明至少存在一个有来源的bad problem，不等价于所有近极值序列都保留来源。增加这种受限类可以是另一个方案，但必须重新证明其normalization、coarsening、completion和同步有限网格选择闭合。

本轮加权完整quadric族的all-plank证明与WP4反例另已复核，见 `R0007_quadric_plank_review.md`；无需再将未加权完整族误称常数convex-Wolff。该反例不改变本review对direction-rich专用输入与generic输入的区分，也没有否定五维Kakeya。
