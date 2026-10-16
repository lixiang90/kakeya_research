# R0008：完整八系数平滑 quadric 先验与典型 profile

日期：2026-10-17。任务 N5-HOR-01 的 prior/profile 子任务。作者：audit_four_dimensional。状态：下列估计为自包含初等证明，待本轮独立审查；它们本身不计算 horizon，不是 Kakeya 反例。

本文只构造拟推广的 visible dimension \(j=3\)、affine hidden coordinate 的单 world 数据。原论文 Definition 2.1 的 version 2 实际为 \(j=2\)；此处“形式满足 cap class 输入”专指把该定义中的 visible dimension 改成3后的数值条件，不声称原稿已经定义或处理此类问题。

## 1. 参数与同一个完整先验

固定 \(L>0\)、\(M>6L\)，令 \(N_0\to\infty\)，并取

\[
 \delta\asymp N_0^{-M},\qquad
 \ell=4^{-m}\asymp N_0^{-T},\qquad
 \eta\asymp N_0^{-U},\qquad U>T>L.
 \tag{1.1}
\]

所有指数固定；可取一个 dyadic 子序列，或将 \(\delta\) 向上舍入到 dyadic 宽度。因而 \(\eta\ll\ell\ll a_L=N_0^{-L}\)。\(\eta\) 在本文仅为 hidden slope noise 宽度，不是原 cap class 的 depth-range 参数。本轮统一的具体实例为 \(N_0=2^n,L=1,M=12,T=40,U=80\)，即 \(\delta=N_0^{-12},\ell=N_0^{-40}=4^{-20n},\eta=N_0^{-80}\)。

在固定参数盒

\[
 \Omega=[1,2]\times[-1/10,1/10]^2
\]

取间距 \(\delta\) 的笛卡尔格点 \(\lambda=(s,p,q)\in\Lambda_\delta\)，记 \(N_\delta=\#\Lambda_\delta\asymp\delta^{-3}\)。每点等概率。原可见线为

\[
 b_\lambda=(s,-sq-p/s,1/s),\qquad
 u_\lambda=(p,-pq,q),\qquad M_\lambda(t)=b_\lambda+t u_\lambda.
 \tag{1.2}
\]

它满足

\[
 t(M_\lambda)_2+(M_\lambda)_1(M_\lambda)_3=1.
 \tag{1.3}
\]

独立取 \(\xi,\zeta\sim U([-\delta,\delta]^3)\)，定义完整可见 coefficients

\[
 B=b_\lambda+\xi,\quad V=u_\lambda+\zeta,\qquad Y(t)=B+tV.
 \tag{1.4}
\]

因此六个可见 affine coefficients 都有独立的绝对连续盒噪声。没有把参数平滑的三维测度误当成六维 Lebesgue density。

隐藏初值 \(C\) 采用有限的 base-4 Cantor law：令

\[
 C=\sum_{k=1}^{m}3\varepsilon_k4^{-k}+\ell Z,
 \qquad \varepsilon_k\in\{0,1\}\text{ 独立均匀},\quad Z\sim U([0,1]).
 \tag{1.5}
\]

即在 \(2^m\) 个末层长度 \(\ell\) 的区间上赋相同质量 \(2^{-m}=\ell^d\)，其中 \(d=1/2\)。其 Lebesgue density 在这些区间上恒为 \(\ell^{d-1}\)，在其余位置为零。另独立取 \(W\sim U([\eta,2\eta])\)，并令

\[
 w(t)=C+tW,\qquad P_*(t,Y,w)=w,\qquad B_{\rm derivative}=1.
 \tag{1.6}
\]

这里整个 visible block \((B,V)\)、\(C\)、\(W\) 三组独立；噪声 \(\xi,\zeta\) 也互独立且独立于 \(\lambda\)。\(B,V\) 内部仍经同一个 \(\lambda\) 耦合，并不声称六个最终 coefficients 相互独立。令 \(\nu\) 为以上同一个概率先验；单 world 权重为1，selected incidence event **仅**为

\[
 I=[1/2,3/4],\qquad d\mu=1_I(t)\,d\nu\,dt.
 \tag{1.7}
\]

所以 \(\mu(\mathrm{all})=1/4\)，没有把 incidence measure 再归一化，也没有按时刻更换 prior。

### 1.1 完整八维 tempered 性

在坐标 \((B,V,C,W)\in\mathbb R^8\) 中，每个 \(\lambda\) 和每个末层 Cantor interval 给一个矩形 box。visible boxes 可以重叠，但每个 coefficient point 只属于固定多个 boxes：\((B_1,V_1,V_3)\) 的中心恰是格点 \((s,p,q)\)，noise 半宽为 \(\delta\)。因此直接求和的 Lebesgue density 有统一有界的重叠因子。将全部有限 box 的坐标 facets 作共同矩形 refinement，可得到至多 \(C N_\delta^6\) 个 visible pieces；也可使用原 Definition 2.2 明确允许的内部 trajectory index copies，此时只需 \(N_\delta\) 个 visible pieces。两种实现给同一个不观察该 index 的 coefficient law。

每个 index box 对 \(\nu\) 的常 density 贡献为

\[
 N_\delta^{-1}(2\delta)^{-6}\ell^{d-1}\eta^{-1}
 \le C\delta^{-3}\ell^{d-1}\eta^{-1}.
 \tag{1.8}
\]

由有界重叠，这也给无 index 密度的同阶 ceiling。上述任一实现的 piece 数及 density ceiling 都是固定的 \(N_0\) 幂；所有 pieces 由固定数量的线性不等式定义。系数、参数范围、原生导数尺度及其倒数都多项式有界，\(Y,V,w\) 实际有绝对常数界。selection (1.7) 也是两个线性 time 条件。原生条件有 \(\partial_wP_*=1\)、\(\partial_{ww}P_*=0\)、\(\sup|P_*|\le2\)，所以完整数据满足拟版 Definition 2.1–2.2 的 finiteness/native 输入。

末层 Cantor 本来就有 full Lebesgue density；**没有再给 \(C\) 卷积噪声**。\(W\) 是另一个 coefficient 的独立区间变量。

## 2. 可见 exact-base density 的 upper 与 support

固定 \(t\in I\)。用 \(g_t(Y)\) 表示 \(Y(t)\) 的三维 Lebesgue density。我们证明统一的

\[
 0\le g_t\le C\delta^{-1},\qquad
 |\operatorname{supp}g_t|\le C\delta.
 \tag{2.1}
\]

这里 support 可取实际有限个 noise supports 的并；不要求它填满 quadric 邻域。

### 2.1 固定时刻的格点计数

无噪声时第一、第三位置为

\[
 x=s+tp,\qquad z=s^{-1}+tq.
 \tag{2.2}
\]

给定 \(s\)，\((p,q)\mapsto(x,z)\) 的 Jacobian 为 \(t^2\ge1/4\)。更直接地，若 \(M_\lambda(t)\) 落在任意边长 \(C_1\delta\) 的空间盒内，固定一个 \(s\) 格点后，(2.2) 分别把 \(p,q\) 限制到长 \(O_{C_1}(\delta)\) 的区间，每个只有 \(O_{C_1}(1)\) 个格点。\(s\) 总共 \(O(\delta^{-1})\) 个，因此

\[
 \#\{\lambda:M_\lambda(t)\in Q\}\le C_{C_1}\delta^{-1}.
 \tag{2.3}
\]

固定 \(\lambda\) 时，\(\xi+t\zeta\) 的 density 至多 \(C\delta^{-3}\)，support 在 \(C\delta\)-box。将 (2.3) 除以 \(N_\delta\asymp\delta^{-3}\) 后相加，给出

\[
 g_t(Y)\le C\delta^{-3}\frac{\delta^{-1}}{N_\delta}
 \le C\delta^{-1}.
 \tag{2.4}
\]

这没有假设有限 \(\delta\)-grid 在像中均匀铺满。

### 2.2 支撑体积

由 (1.3)、noise 大小及有界坐标，所有 noisy positions 都满足

\[
 |tY_2+Y_1Y_3-1|\le C\delta.
 \tag{2.5}
\]

在 \(t\in I\) 有 \(t\ge1/2\)，故给定有界 \((Y_1,Y_3)\) 后，(2.5) 将 \(Y_2\) 限在总长 \(O(\delta)\) 的区间中。因此 support volume \(\le C\delta\)。同理整个 \((t,Y)\) support 的四维 volume 也是 \(O(\delta)\)。

## 3. 隐藏 bin 的 upper 和 occupied count

令 \(\lambda_m\) 为 (1.5) 的概率律。对于任意实区间 \(J\)，任意 \(m\) 都有

\[
 \lambda_m(J)\le C|J|^d,
 \qquad d=1/2,
 \tag{3.1}
\]

区间长度大于1时以常数放宽。证明分两段：

- 若 \(\ell\le |J|\le1\)，选一级长度 \(4^{-k}\asymp |J|\)。每个 level-\(k\) interval 的质量为 \(2^{-k}\asymp |J|^d\)，而 \(J\) 只碰到固定多个这种彼此分离的区间。
- 若 \(|J|<\ell\)，末层 density ceiling 给 \(\lambda_m(J)\le \ell^{d-1}|J|\le |J|^d\)。

所以给定任意 \(t\in I\)，甚至给定 \(W\)，平移后的 \(C+tW\) 仍有同一 Frostman upper。令 \(\mathcal B_a\) 是任意半开 nested dyadic grid，\(a_L\le a\le1\)，并记

\[
 h_{t,a}(B)=\Pr\{C+tW\in B\},\qquad B\in\mathcal B_a.
\]

则

\[
 h_{t,a}(B)\le Ca^d,
 \qquad
 \#\{B:h_{t,a}(B)>0\}\le Ca^{-d}.
 \tag{3.2}
\]

第二式是独立于第一式的 support covering：取长度 \(4^{-k}\asymp a\) 的 Cantor level，至多 \(Ca^{-d}\) 个 interval；每个长 \(O(a)\)，经 \(tW\in[0,2\eta]\) 扩大后仍长 \(O(a)\)，故每个只碰到固定多个 width-\(a\) grid bins。这里确实用了 \(\eta\ll\ell\ll a_L\le a\)。并未从 Frostman upper 反推 occupied count。

## 4. 不填孔也成立的双侧典型 profile

depth \(r\in[0,L]\) 的 observation 是

\[
 p_r=(t,Y(t),[w(t)]_{a_r}),\qquad a_r=N_0^{-r},
 \tag{4.1}
\]

忽略固定 world index。对 \(\mu\) 的 observation density，用 \(dt\,dY\) 与 hidden-bin counting measure 作 reference，独立性给精确乘积

\[
 G_r(t,Y,B)=1_I(t)g_t(Y)h_{t,a_r}(B).
 \tag{4.2}
\]

因此 everywhere upper 与 support 的 reference 体积分别为

\[
 G_r\le C\delta^{-1}a_r^d,
 \qquad
 |\operatorname{supp}G_r|_{dt\,dY\times\#B}
 \le C\delta a_r^{-d}.
 \tag{4.3}
\]

对任意 \(K\ge1\)，直接在小密度集合积分，得到

\[
 \mu\{G_r<K^{-1}\delta^{-1}a_r^d\}
 \le K^{-1}\delta^{-1}a_r^d\,
      |\operatorname{supp}G_r|
 \le C/K.
 \tag{4.4}
\]

这是随机 observation 在**同一个** density 下的质量估计。它不声称整个 quadric 邻域内有 pointwise lower，也不声称每个 occupied hidden bin 都有统一 lower。

取 \(K=N_0^\tau\)，\(\tau>0\) 固定，(4.3)–(4.4) 正好给原 Definition 2.1 意义下的 typical density

\[
 \boxed{n(r)\sim_{\log}\delta^{-1}a_r^d,
 \qquad f(r)=dr-M.}
 \tag{4.5}
\]

lower 例外质量 \(\le C N_0^{-\tau}\)；upper 中的绝对常数最终小于 \(N_0^\tau\)。舍入只改变常数。特别地 \(f(L)-f(r)=d(L-r)\)。负的 \(f(0)=-M\) 只表示 exact-base density 很大，原定义允许它。

这些常数对所有 \(r\in[0,L]\) 一致。若需同时处理一个 \(N_0^{o(1)}\) 大小的 prepared finite depth grid，union bound 仍给 fixed-power 小的例外；再用 nested-grid 比较处理固定中间 depths。不需要为了得到 profile 先做不透明的 density-type 选择。进一步 inverse-subpower selection 仍可调用原 Lemma 2.3 保留相同 logarithmic profile；本节没有把 selection 后的 law 重新归一化后还说它等于原 law。

## 5. 可选加强：同 prior 的全宽度 visible-angular cap

令 \(\mathcal V_\rho\) 为三维速度盒 grid，side \(0<\rho\le1\)。记固定 \(t\) 时 joint observation \((Y,[V]_\rho)\) 的 density 为 \(g_{t,\rho}(Y,J)\)。则

\[
 \boxed{g_{t,\rho}(Y,J)\le C\delta^{-1}\rho}
 \qquad(t\in I,\ 0<\rho\le1).
 \tag{5.1}
\]

### 5.1 \(\rho\ge\delta\)

若某个 noisy index 能同时贡献给 \(Y\) 和 velocity bin \(J\)，则 \(p\) 落在 \(J\) 第一坐标的 \(O(\delta)\) 扩大内，且

\[
 |s+tp-Y_1|\le C\delta.
\]

于是 \(s\) 只在总长 \(O(\rho)\) 的区间内，有 \(O(\rho/\delta)\) 个格点。对每个 \(s\)，由 (2.2) 和 near-\(Y\) 条件，\(p,q\) 各只有 \(O(1)\) 个格点。单 index joint density 不超过它的纯 \(Y\) density \(C\delta^{-3}\)，所以

\[
 g_{t,\rho}(Y,J)
 \le C\delta^{-3}\frac{\rho/\delta}{N_\delta}
 \le C\delta^{-1}\rho.
 \tag{5.2}
\]

### 5.2 \(\rho<\delta\)

改用完整 coefficient noise：变换

\[
 (\xi,\zeta)\mapsto(\xi+t\zeta,\zeta)
\]

Jacobian 为1，故单 index 的 \((Y,V)\) joint density 至多 \(C\delta^{-6}\)。给定 \((Y,J)\)，noise support 要求 \(p,q\) 各在长 \(O(\delta)\) 的区间内，再由 \(s+tp\approx Y_1\) 得 \(s\) 在长 \(O(\delta)\) 的区间内。因此仅 \(O(1)\) 个 indices 能贡献。对 width-\(\rho\) 三维 velocity bin 积分后，

\[
 g_{t,\rho}(Y,J)
 \le C N_\delta^{-1}\delta^{-6}\rho^3
 \le C\delta^{-3}\rho^3
 \le C\delta^{-1}\rho.
 \tag{5.3}
\]

最后一步使用 \(\rho\le\delta\)。所以不是仅在高于 smoothing scale 的 bins 上得到 angular cap。

hidden variables 独立，故同一个 selected prior 的 joint density 进一步满足

\[
 \frac{d\mu_{(p_r,[V]_\rho)}}{dt\,dY\times\#B\times\#J}
 \le C\delta^{-1}a_r^d\rho.
 \tag{5.4}
\]

在 terminal \(r=L\)、\(\rho=N_0^{-u}\) 时，(4.5) 与 (5.4) 给原 (2.6) 的形式 upper

\[
 G_{L,u}\le C n(L)N_0^{-u},
 \tag{5.5}
\]

可取固定 angular exponent \(S=1\) 与任意固定紧的 \(u\)-range。这里相对纯 terminal density 的 cap 是一个 joint-density upper；不宣称每个 individual \((t,Y,B)\) 上都没有例外地具有相同 conditional probability ceiling。纯 density 的 typical lower 给 corresponding typical conditional statement。

## 6. 与本轮其余任务的接口和边界

已提供：归一概率的 full8 piecewise constant tempered prior、\(1/4\) selected mass、原生 \(P_*=w,B=1\)、同 prior 的 \(n(r)\sim_{\log}\delta^{-1}a_r^{1/2}\)、以及可选的正 angular cap。每个 upper、support count 和 lower 质量估计均与原坐标及原先验一致。

尚未由本文证明：任意二次测试 \(P\) 的短块质量界、所有宽度平滑 plank cap、true-chart floor 的可调用形式、已知 assignment/list 的完备性，以及任意 chart system 的 horizon lower。它们由本轮其他子任务独立处理；不能只凭本文 profile 就登记 \(H>L\)。尤其 \(M>6L\) 在本文件只用于和待核验 horizon 目标配参，未用于上述 prior/profile 证明。

这组数据没有 full original slope density 的 subpower ceiling，亦未给出五维 Kakeya 来源。即使最终证明它反驳 generic \(j=3\) horizon 上界，也只否定无来源的模型推广，不能反驳四维论文的 \(j=2\) 主结论或任何 Kakeya 猜想。
