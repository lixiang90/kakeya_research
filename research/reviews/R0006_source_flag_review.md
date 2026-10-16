# R0006：原始列表与全时flag候选的独立复核

日期：2026-10-16。审查人：`literature_frontier`。被审文本：`notes/70_flags/R0006_source_fulltime_atlas.md`。重点核验§3.1的旧真实框与own-depth列表、§3.3的任意全时known flag覆盖界；另检查§2的条件性交框与列表假设。没有复核整个原稿Proposition10.2、五维cap类或极值闭合。

结论：被审有限模型与覆盖不等式在明示条件下通过内部独立复核，未经外部同行评审。该模型为真实$d=1$边界，未认证正horizon或critical路径；本次审查没有证明其horizon为0。

## 1. 旧框的质量、测试及列表

从$(Y_0,V,\zeta_0,\zeta_1)$到$(Y_0,V,w_0,W)$是常Jacobian1的可逆线性映射。固定块中心$t_i$，$n_i\cdot Y(t_i)$分箱宽$qg$、两根tangent anchor分箱宽$q$、$n_i\cdot V$分箱宽$g$。在所选固定interior中，位置—速度密度有上下常数，因而

$$\nu(Q)\asymp (q^3g)g=q^3g^2.$$

沿整个块，normal位移误差为$O(qg)$，两个tangent误差为$O(q)$。测试$w-\sqrt{1+t_i^2}c_i$的小值为$O(g+q+\eta)=O(g)$，隐藏一阶导1、二阶导0。$J_Q\asymp q^3g$且实际观测$n(g)\asymp g$，故$m_Q/q\asymp n(g)J_Q$。这是完整prior assignment的真实floor；不是后验小分支重命名。

当前观测给$w(t)$到$\delta\le g$，而$|t-t_i|\le q=g$，所以$n_i\cdot V$误差为$O(g)$，对应$O(1)$个velocity bins。再恢复normal anchor时该误差乘$q$，得到$O(qg)$；tangent anchors由exact当前$Y$及有界速度恢复到$O(q)$。因此真实单时刻own-depth列表成立，未调用另一时刻exact base。

取足够小的固定interior参数盒即可保证所有块保持固定正覆盖，且每块assignments互不相交。上述证明未赋予该例$d<1$、unbounded narrowness gap或critical资格。

## 2. 任意全时known flag的覆盖上界

全时frame的endpoint测试把该label的全部assigned velocities限制在一个固定velocity parallelepiped内，其一个边长至多$K^C$，另两个至多$K^C\varepsilon$。任意plane的截面积不超过该盒在该plane上的投影面积；后者由三对相邻边的面积和控制，为$CK^C\varepsilon$。该界对plane方向和chart中心速度统一成立。

固定$t,Y,\zeta$后作$s=w=V_1+tV_2+\zeta_0+t\zeta_1$，从$V$到$(s,V_2,V_3)$的Jacobian恰为1。固定$s$的积分是一个plane截面积，Euclidean面积与$dV_2dV_3$只差$\sqrt{1+t^2}$常数。真实原始列表取决于$(t,Y,[s]_\delta)$，所以即使为积分而把$s$精确固定，列表仍至多$L$项且不依赖噪声或隐藏速度。并集界给截面上界$CK^CL\varepsilon$。

对固定有界的$Y,s,t$范围积分，再对归一化噪声密度积分，得到

$$\|\lambda_{\rm atlas}\|\le CK^CL\varepsilon.$$

这里既不损失$\eta^{-2}$，也不损失$\delta^{-1}$：按bin积分时每bin有额外$\delta$因子，再对$O(\delta^{-1})$个bin求和恰好消去。无需$\eta\ll\varepsilon$或$\delta\ll\varepsilon$。输出family的不同几何、测试或assignment不会破坏证明，只要每个实际计数label在原观测的真实列表内，且全时几何及$\lambda_{\rm atlas}\le\nu dt$成立。

## 3. 正向条件引理与限制

§2的双normal对偶列构造给$J_C\asymp g_0g_1/|n_0\times n_1|$，同reference times下完整assignment交集仍不交；这些几何和prior预算通过检查。但成为原始known atlas还须**当前同一个$p_L$**恢复两套完整affine signatures。两个参考时刻各有自己的短列表不等价于这一条件。原有单框true floor也不自动成为每个交集的floor。

边界模型的raw full-slope密度约为$\eta^{-1}$，真实$d=1$，且没有源稿$\alpha_2-\alpha_1\to\infty$条件。它严格否定去掉这些额外条件后的通用自动匹配推论，不反驳原二维命题或高维$d<1$临界版本。**Horizon未在此次审查中计算；不得从$d=1$自动推出$H=0$。**
