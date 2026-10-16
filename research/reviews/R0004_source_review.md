# R0004：DIR-002 源应用与 branch 阈值复核

日期：2026-10-16。审查范围：`results/reviewed/DIR-002_true_floor_direction_budget.md` §3–4 与 `literature/primary/openai_4d_source/06-isotropic.tex` 的真实输入。本代理参与了 DIR-002 所用 Jacobian 消去公式的初稿，因此本文件**不重复登记该核心公式的独立审查**；其独立审查见 `R0004_direction_entropy_review.md`。这里核对源稿应用、分支量词与尺度。未复核完整四维证明、五维几何归约或 full critical path。

## 1. Branch 质量损失：通过

源 TeX 行 1656–1659（PDF p.105）仅在一次固定 potential/packet 后选出一个 group/core/sign choice，质量为至少 \(h\nu_Q(a_2/a)^d/K\)。故 DIR-002 §3 必须保留

\[
f=(a_2/a)^d,
\qquad
\lambda(B)\ge h\nu_Qf/K_{\rm br}.
\]

若同一支方向事件在完整 assigned prior 中的比例至多 \(\beta\)，且 \(\lambda\le G\nu dt\)，其 branch 比例上界是 \(\min\{1,GK_{\rm br}\beta/f\}\)。现版只支付一次 \(G\)，并明确每父先固定一支和一个事件，正确。源文的一次选择数 \(K/f\) 不控制其他 residual、插值或 potential 所产生的所有二次式；现版已保留此限制。

这里 \(n(b)\) 是 observation 的 base density；\(\nu_Q\) 是完整 assignment 的 prior mass。不能把 \(n(b)\) 解释为 prior mass，也不能为此支直接登记 \(\nu(B)\asymp n(b)J_Q\)。

## 2. \(Kh\) 薄层可覆盖此固定支的 contributing lines

源行 1780 只显式写七个被抽样方向，但可严格补足以下推导：

- 行 1661–1668、1699–1708（PDF pp.105–106）给每条同支 contributing line 的长见证，并在其计数 incidence \(u\) 有 \(|D_{\mathbf v}^2f(u)|\le Ka_2\)。
- 行 1740–1754（PDF p.106）的张量反演给整个凸内球 \(U\) 上 \(\|\nabla^3f\|\le K(a_2+S_0h)\)。对任一这样的线，\(\mathbf v=(1,v)\) 固定、大小受 \(K\) 控制，移 Hessian 到 \(u_c\) 因而至多损失 \(K(a_2+S_0h)\)。
- 行 1763–1779 定义 \(q_{\rm Hess}=\nabla^2f(u_c)/(2S_0)\)，在 conic case 有 \(S_0>a_2/h\) 及系数范数 \([K^{-1},K]\)。于是全体仍计入该支的轨道满足

  \[
  |q_{\rm Hess}(1,v)|\le K(a_2/S_0+h)\le Kh.
  \]

源行 942–945 同时缩放全部 base-time 坐标，无 velocity shear，因此这里不再丢一个独立时间长度因子。结论只关于此固定支的当前贡献轨道，不关于完整 assignment 内没有该 branch 见证的其他轨道。但这已足以对该支 incidence 用固定方向事件上界。

五维中同样推导以对应的统一三阶导数界为条件；五方向 cubic-two-copy 代数引理并不自动建立整个几何准备。DIR-002 现版注明拟五维结构仍须验证，正确。

## 3. 通用 sublevel 与最终尺度：通过

Hessian 在 affine 方向 chart 中成为任意系数归一化的次数不超过 2 多项式。固定有界盒上的统一体积只保证 \(C\sqrt\eta\)；\(v_2-v_1^2\) 的线性 \(C\eta\) 依赖额外的一阶横向非退化。DIR-002 已正确区别两者，不能把特殊式的估计免费用于 native Hessian。

在 \(n\asymp a^d\)、\(q\asymp h\)、\(a_2/a=h^e\)、\(\eta=Kh\) 下，含分支损失的一般二次式预算为

\[
K\frac{h^{1/2-ed}}{a^dh^j};
\]

即使额外有线性薄层，也只是 \(K h^{1-ed}/(a^dh^j)\)。对 \(j\ge2\)、\(d\ge0\) 均不提供趋零的上界。现版先列乐观线性式再注明通用更弱，逻辑正确；这个上界不小不能反推真实 bad mass 大。

## 4. Corollary 4.4 与来源闭合：有限条件通过

Corollary 4.4（PDF pp.50–51）只控制相对 profile 并构造 vanishing-depth 节点，显式允许绝对密度指数无界。DIR-002 §4 的固定原始精度排除计算以额外 \(n(0)\)、visible density 的 actual-subpower 上界为条件，没有声称 Corollary 已给出它们，正确。

更精确的充分条件是同一 prior/坐标下 \(L/n(0)\) 为 actual subpower；分别要求两者各为 subpower 是较强但合法的条件。父归一化保持

\[
L_{\rm new}\le L J/(q^j\nu_A)
\le K_{\rm sat}L/[n(b)q^j],
\]

所以不能因新 \(n(0)\asymp1\) 而删除方向密度成本。Theorem 2.17 最初 full-slope 密度有界只保证存在有此来源的正 horizon problem；§4.1 对全部 \(\mathcal C(d)\) 优化不自动让所有 maximizing sequences 保留它。增强来源类是否闭合仍是开放接口，不能据当前公式直接排除所有增强方案。

结论：DIR-002 当前 §3–4 在明确假设范围内与源稿一致；本次补清了全 branch 方向事件的来源。没有新增 Kakeya 维数结论或完整反例。
