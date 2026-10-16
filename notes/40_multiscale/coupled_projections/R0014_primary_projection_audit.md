# R0014：共享时间双块投影的一手定理适用审计

2026-10-17。任务 N5-COUPLED-PROJ-01。目标是同一固定参数图
\[
 P=\{(b,d,f(v),c,e,g(v)):v=(b,c,d,e)\in\Omega_\delta\},
\]
其中方向分离且 \(\#\Omega_\delta\asymp\delta^{-4}\)，对同一时间的
\[
 \Pi_t=A_t\oplus A_t,\qquad
 A_t=\begin{pmatrix}t&-1&0\\0&t&1\end{pmatrix}
\]
与任意原选择 \(P_j\subset P\)，由
\(\sum_j\#P_j\ge\delta^\eta\#P\,\delta^{-1}\)
推出严格超过 \(\delta^{-4}\) 的总 covering 下界。两块不能改为独立时间；本稿不再以单块 FO 的结论作为联合输入。

## 1. 本次结论

本次读到的三个直接相关一手来源中，**两篇确实提供足以处理有限尺度质量/零散 dense selections 的定量工具**，所以不能笼统以“只有 Hausdorff a.e. 结论”排除它们。直接调用失败的位置是实际的几何假设：

1. Gan–Guo–Wang（GGW）Theorem 2.1 有有限尺度 Frostman incidence 结论；本轮参数质量可满足其 Frostman 和参与密度输入，但该定理只针对单条非退化曲线的 osculating 子空间。我们的四平面族 Grassmann 一阶导数秩为 **2**，该 osculating 族的秩为 **1**，即使固定线性换坐标或正则重参数也不能识别。
2. Cohen–Shmerkin–Wang–Zakharov（CSWZ，2026-10-09）Theorems 1.6/1.7 有 general Grassmann、原参与 shading 和 robust subset 的有限尺度结论。但我们的整个联合族位于固定 Schubert cycle；在 big-cell 坐标中，它更是恒处于一个 rank-one model hyperplane。所有原时间子选择都保留这个退化，不能满足该文所需 spread-outness。
3. Du 的 general-family 论文 Theorem 1.7 的已证范围是 \(\mathbb R^4\to\mathbb R^2\)，且要求对每个固定线性子空间无 generic 维数塌缩。我们的 \(\mathbb R^6\to\mathbb R^4\) 块族确有固定四维子空间被压到三维，连其一般猜想的无塌缩假设也不满足。

因此尚未定位可直接解决本轮 CP 的已证联合定理。这个结论只覆盖下列具体来源及有限检索，不认证“任何文献都不存在”，也不证明 CP 为假。

## 2. 新增文献、版本与准确阅读范围

全部保存官方 PDF、pdftotext -layout 全文和同名前缀 metadata；关键定理 PDF 页图已核。页码从 1 计，本次三个 PDF 的印页与 PDF 页一致。

| 一手来源 | 本地前缀（literature/primary、extracted、metadata） | 实际核读 |
| --- | --- | --- |
| [Gan–Guo–Wang, arXiv:2211.09508v2](https://arxiv.org/pdf/2211.09508v2)，2024-01-21 修订 | R0014_gan_guo_wang_2211_09508_v2 | pp.1–4，Thm1.2/Thm2.1、式(1.5)–(1.6)、(2.2)–(2.7)；浏览 decoupling 输入说明，未重证全文 |
| [Cohen–Shmerkin–Wang–Zakharov, arXiv:2610.13682v1](https://arxiv.org/pdf/2610.13682v1)，2026-10-09 | R0014_cohen_shmerkin_wang_zakharov_2610_13682_v1 | pp.2–6，Schubert/Def1.4–1.5、Thm1.2/1.6/1.7；pp.37–39 的 osculating 引用和一般族范围；未重证全文 |
| [Jiahan Du, arXiv:2510.16671v2](https://arxiv.org/pdf/2510.16671v2)，2025-10-23 修订 | R0014_du_2510_16671_v2 | pp.1–4，Conj1.5/1.6、Thm1.7 和 polynomial/no-subspace-collapse 条件；后文不作为输入 |

校验：

- GGW：16 页，283891 bytes；SHA256 709fdd2a2e5665f84e76b565c2c07fff925707c024f9ae224ea5dbb72d68c2f5。
- CSWZ：45 页，652284 bytes；SHA256 3605d5a2655ef25f7021282e91e88e1d946c7b1189aed2fb14cd974efd92f8e8。
- Du：22 页，609577 bytes；SHA256 9416fe67c0a4e95dd36f1860ea2cd05a3eacc3e34dfc22885ffd046d98f5859e。

准确全文定位：

- GGW Thm1.2 本地 txt 行 73 起（p.2），Thm2.1 行 147–160（p.3），其有限尺度推论式(2.7)在 p.4。
- CSWZ Def1.5 行 251 起（p.5），Thm1.6/1.7 行 270–289（p.6），引用 GGW 的 Thm4.10 行 1994 起（p.37）。
- Du Conj1.5/1.6 行 85/90 起（p.2），Thm1.7 行 103 起（p.3）。

另读 [Hong Wang ICM 2026 survey §1](https://epubs.siam.org/doi/full/10.1137/25M1806156) 的 pencil 定义、Questions1.5/1.6 和后文局部方向来源警示，仅用于检索入口与范围比较；没有下载 PDF，也不把它当新证明输入。FO 一手论文已在上轮入库，本轮没有重复下载。

检索词包括 restricted projections / Grassmannian curves / higher dimensions / direct sum / tensor product / polynomial curves / nondegenerate planes；部分结果不相关，未作为数学证据。特别不能从未命中的检索推断定理不存在。

## 3. 本轮的质量输入确实强于“任意四维集合”

以下先说明哪些前提没有问题，避免把真正的几何缺口误归为点集不正则。

由方向 chart 的双 Lipschitz 性，\(\Omega_\delta\) 的四参数 \(v\) 为 \(c\delta\)-分离。方向投影
\[
 D(b,d,f,c,e,g)=(b,d,c,e)
\]
是坐标投影，故 \(P\) 本身分离；任意六维半径 \(\rho\ge\delta\) 的球只容纳
\[
 O_{r,R,C_0}((\rho/\delta)^4)
 \tag{F1}
\]
个参数点。其计数概率 \(\mu_\delta\) 在 \(\rho\ge\delta\) 时满足四维 Frostman upper \(C\rho^4\)。

为调用连续测度版本，可把每个点替换为半径 \(c\delta\) 的六维小球上均匀质量，总权仍为 1；称为 \(\widetilde\mu_\delta\)。在 \(\rho<\delta\) 时，密度至多 \(C\delta^{-2}\)，故
\[
 \widetilde\mu_\delta(B(x,\rho))
 \le C\delta^{-2}\rho^6\le C\rho^4.
 \tag{F2}
\]
合并 F1–F2 得全部尺度的 \(c_4(\widetilde\mu_\delta)\le C\)，从而对每个固定 \(\alpha<4\) 也有统一 \(c_\alpha\)（统一有界 support）。这个平滑仅用于分析性定理适用审计；没有把原离散参数图换成新的 CP 数据。

平均参与质量也可变成逐点长参与。令 \(m(p)=\#\{j:p\in P_j\}\)，其 upper 为 \(C\delta^{-1}\)。保留
\[
 P_*=\{p:m(p)\ge \tfrac12\delta^{-1+\eta}\}
\]
可保证 \(\#P_*\ge c\delta^\eta\#P\)。不正规化 restriction 时，Frostman upper 不恶化，保留总质量至少 \(c\delta^\eta\)；若正规化，则相应 Frostman 常数要付 \(\delta^{-\eta}\)。两者在“总质量/Frostman 常数”的比例中给同一成本。

对保留点的每个原 marked time，逆投影 covering cells 的固定倍扩大同时包含其 \(c\delta\)-平滑小球，因为 \(\Pi_t\) 的算子范数统一有界。这可把原 participation 转为有限 plate incidence，而不新增别的参数时间 labels。固定尺度常数须吸收于密度指数的余量中。

**边界。** 这只给 uniform four-Frostman upper 与原参与下界，既不给任意 conditional fiber 的正则，也不证明输出 covering 多。第 6 节的线性例子会说明 four-Frostman alone 本身不足。

## 4. GGW：有限尺度定理输入合适，osculating 几何不合适

GGW 的几何是非退化曲线 \(\Gamma:I\to\mathbb R^n\)，满足
\[
 \det(\Gamma'(t),\ldots,\Gamma^{(n)}(t))\ne0,
 \qquad
 V_t=\operatorname{span}(\Gamma'(t),\ldots,\Gamma^{(m)}(t)).
 \tag{G1}
\]
Thm1.2 对固定 Borel 集给 a.e.-\(t\) 的 Hausdorff 投影维数；然而其 Thm2.1 更强且定量。若 \(\mu\) 有 \(c_\alpha(\mu)<\infty\)、\(\alpha<m\)，在 \(\delta\)-时间网格选择法向厚度为 \(\delta\) 的 plates \(\mathbb W_t\)，并满足所有 support 点参与至少 \(c\delta^{-1+\zeta}\) 次，则
\[
 \#\mathbb W\ge
 C_{\zeta,n,\alpha}\,
 \frac{\mu(\mathbb R^n)}{c_\alpha(\mu)}
 \delta^{-1-\alpha+O_n(\sqrt\zeta)}.
 \tag{G2}
\]
常数不依赖 \(\delta\)，论文给了显式但极大的 \(O_n(\sqrt\zeta)\) 系数。

假如 G1 对本族成立，取 \(n=6,m=4\)、任意固定 \(\alpha\in(3,4)\)，结合第 3 节的保留质量，G2 就有
\[
 \sum_j N_\delta(\Pi_{t_j}P_j)
 \gtrsim \delta^{-1-\alpha+O(\sqrt\eta)+O(\eta)}.
 \tag{G3}
\]
选择 \(\eta\) 足够小，便超过 \(\delta^{-4-\sigma}\) 的某个固定阈值。因此本轮不缺“如何从该 finite theorem 处理平均 shading”的基本量词；缺的是 G1。

### 4.1 一个覆盖任意固定换坐标的 rank 障碍

令 \(H_t=\operatorname{row}(\Pi_t)=\ker(\Pi_t)^\perp\in\mathrm{Gr}(6,4)\)。对光滑子空间曲线 \(V_t\)，其一阶导数是线性映射
\[
 \dot V_t:V_t\longrightarrow\mathbb R^6/V_t,\qquad
 v(t)\longmapsto v'(t)\bmod V_t.
 \tag{G4}
\]
对 G1 的 \(m=4\) osculating 族，基向量 \(\Gamma',\Gamma'',\Gamma'''\) 的导数都仍在 \(V_t\)；只有 \(\Gamma^{(4)}\) 的导数可以逸出。非退化保证它真的逸出，所以 \(\operatorname{rank}\dot V_t=1\)。

本族则分为两个独立三维块。单块 \(H_t^{(1)}=\gamma(t)^\perp\)、\(\gamma=(1,t,-t^2)\)，取 row basis
\[
 u_1=(t,-1,0),\qquad u_2=(0,t,1).
\]
它们导数在 quotient by \(H_t^{(1)}\) 的分量由与 \(\gamma\) 的内积 \(1,t\) 给出；因此单块导数秩恰为 1。两个块的 quotient 方向独立，得到
\[
 \operatorname{rank}\dot H_t=2\quad\text{对所有 }t\in I.
 \tag{G5}
\]
固定 \(GL(6)\) 变换只在 G4 的左右乘可逆映射；正则时间重参数乘非零标量；正交取补使导数取负转置。这些都保持秩。因此不能通过固定线性换坐标、取对偶或正则重参数把本四平面族变成 GGW 的 osculating 族。

这不排除设计新的适合本族的 decoupling 方法。它只严格排除直接调用该最相关 general-\(n\) 定理，以及把两块分别“非退化”当作联合 osculating 非退化的做法。

## 5. CSWZ：真正 joint/finite/shading 定理，但本族恒处于模型超平面

CSWZ Thm1.7 在 ambient \(d\)、kernel dimension \(k\) 下研究
\(\pi_\theta:\mathbb R^{d-k}\times\mathbb R^k\to\mathbb R^{d-k}\)，\(\pi_\theta(x,y)=x+\theta y\)。它要求参数族 \(\Theta\) 在 matrix big cell 中 spread-out，点集有 Frostman upper，并给除 \(\delta^\varepsilon\) 比例参数外、对每一个保留比例至少 \(\delta^\varepsilon\) 的 subset \(P'\) 都成立的 covering 下界。Thm1.6 还允许各点拥有不同的原方向 shadings。

这类 robust quantifier 本来可以处理本轮任意 \(P_j\)：先删除小于 \(\delta^\varepsilon\#P\) 的轻时间片和异常参数；若原 \(\eta\ll\varepsilon\)，删去总 incidence 至多 \(O(\delta^{\varepsilon-1}\#P)\)，严格小于原 \(\delta^{\eta-1}\#P\)。剩下至少 \(c\delta^{\eta-1}\) 个 heavy times，每个可使用定理的 robust subset 结论。不能因其某个连续推论写成 a.e. 便忽略这项有限能力。

但本族的 parameter hypothesis 不成立。重排输入为
\[
 x=(d,f,e,g)\in\mathbb R^4,\qquad y=(b,c)\in\mathbb R^2.
\]
对每个固定 \(t\)，对原输出施加 uniformly invertible 的块变换
\((X,Z)\mapsto(-X,Z+tX)\)，获得
\[
 \widehat\Pi_t(x,y)=x+\theta(t)y,\qquad
 \theta(t)=
 \begin{pmatrix}
 -t&0\\t^2&0\\0&-t\\0&t^2
 \end{pmatrix}.
 \tag{S1}
\]
这个有界输出变换只用于每时刻 covering 比较，不将两个时钟分开，也不改变同一个固定输入 \(P\)。

CSWZ 的 model hyperplanes 是
\[
 \mathcal H_{a,b,u}=\{\theta:a^\mathsf T\theta b=u\},
 \quad a\in\mathbb R^4\setminus0,\ b\in\mathbb R^2\setminus0.
\]
取 \(a=e_1,b=e_2,u=0\)，S1 给
\[
 \theta(t)\in\mathcal H_{e_1,e_2,0}\quad\text{对全部 }t.
 \tag{S2}
\]
这是精确的 rank-one model hyperplane，不是只说 Plücker 坐标落在某个任意线性超平面。

### 5.1 连续和有限尺度条件都失败

连续层面，令 \(B_1,B_2\) 为两个三维参数块；\(H_t=\gamma^\perp\oplus\gamma^\perp\)。取第一块中的固定二维 \(W\)，则两二维子空间 \(W,H_t\cap B_1\subset B_1\cong\mathbb R^3\) 总有非零交。因此
\[
 H_t\in\mathcal S_W=\{H\in\mathrm{Gr}(6,4):H\cap W\ne0\}
 \quad\text{对全部 }t.
 \tag{S3}
\]
Thm1.2 的 local Schubert non-concentration 明确失败。

有限层面，覆盖 \(\theta(I)\) 的 \(\delta\)-matrix cells 全部处于 S2 的 \(C\delta\)-邻域。取 Def1.5 的任何非空子选择 \(\mathcal J'\)，所有 \(r\ge C_\beta\delta\) 的 dyadic scales 都为 \(\beta\)-singular。因此每个参数有
\[
 \mathfrak s\ge\log_2(\delta^{-1})-O_\beta(1)
\]
个 singular scales。把 \(\mathcal J'=\mathcal J\) 代入 spread-out 定义，会要求
\[
 1\le C\,2^{-\beta\mathfrak s},
 \qquad\text{即 }C\gtrsim_\beta\delta^{-\beta}.
 \tag{S4}
\]
因此对于允许常数 \(C=\delta^{-\varepsilon}\) 的 **small-loss 范围 \(\varepsilon<\beta\)**，条件明确不成立。这个计算不单独排除所有更大 \(\varepsilon\) 的数值选择；不能通过“把 theorem 的 \(\varepsilon\) 再减小”就否定其全部可选参数。任意原时间 shading 子选择仍在 S2 内，也保留这一 small-loss 障碍。

对于声称某个其余参数选择能通过 Thm1.7 给本族 **输出维数严格大于 3** 的直接调用，第 6 节另有独立校准：定理要求对所有相应 four-Frostman 点集成立，因而也必须适用于该节 \(Z\) 的四维网格，而它在每个时间只有 \(O(\delta^{-3})\) 个输出 cubes。若定理输出 exponent \(4-\text{loss}>3\)，就与此网格的实际 upper 矛盾。因此不存在能给本轮所需 \(>3\) 输出、同时满足该 universal theorem 全部假设的这种直接调用。这里没有把 \(Z\) 误作 CP 的方向图反例。

以上否定的是该文定理的直接适用性，不是 CP。一个仍保完整方向图的 CP 结果，必须利用点集相对于这些 pencil 的额外结构；CSWZ 的“对任意 Frostman 点集”定理不能免费提供它。

## 6. 一个说明 universal four-Frostman 输入不足的联合线性校准

取固定四维子空间
\[
 Z=B_1\oplus\operatorname{span}(e_c),
\]
即第一块 \((b,d,f)\) 任意、第二块只有 \(c\) 自由。对所有 \(t\in I\subset(0,1)\)，
\[
 \dim\Pi_t(Z)=2+1=3.
 \tag{L1}
\]
因此 uniform four-Frostman probability supported on a bounded part of \(Z\) 的联合投影只有三维。其 \(\delta\)-离散化有 \(\asymp\delta^{-4}\) 个参数点，而每个输出只需 \(O(\delta^{-3})\) 个 cubes，沿 \(\asymp\delta^{-1}\) 个时间求和只有 \(O(\delta^{-4})\)。这严格阻止把 G3/CP 直接推广为“任何四维 Frostman 参数集合”的结论。

它不是 CP 的反例：\(D(Z)\) 只有 \((b,d,c)\) 三维，许多点共享同一原方向，违反满四参数分离方向图的输入。它的作用是说明 full-direction graph 条件在联合问题中具有实质内容，不能只把它压成无条件的 \(c_4(\mu)\le C\) 后遗忘。

## 7. Du general-family 定理的已证边界

Du Conj1.5 要求每个线性子空间 \(Z\) 都满足 generic rank
\[
 \dim\Pi_t(Z)=\min\{\dim Z,m\}.
 \tag{D1}
\]
已证 Thm1.7 仅对 polynomial \(\mathbb R^4\to\mathbb R^2\) 族，在 D1 下给二维参数集合投影维数严格大于 \(1\) 的结果；它不是任意 ambient/output 维数的已证 Marstrand 定理。更一般按子空间最坏 rank 制定的 Conj1.6 明确是猜想。

本族的 L1 已直接违反 D1。即使不管维数范围，也不能把本族套进该 theorem/conjecture 的无塌缩假设。原 \(P\) 是四参数图，并不使 \(\Pi_t\) 变成对四参数 \(v\) 的线性族：输出中的 \(f(v),g(v)\) 是任意 bounded selectors，没有统一导数或模连续性。故不能先把 graph 参数化为 \(\mathbb R^4\) 就直接调用其线性族定理。

## 8. 可保留的精确信息及停止边界

本轮没有发现直接覆盖 CP 的一手 theorem，也没有证明/证伪 CP。可保留的非同义源结论为：

- 原 full-direction graph 能给统一四维 Frostman upper 和有限长参与，平均 shading 的保留成本可明确付掉；这并非关键缺口。
- GGW finite theorem 若有相应联合几何便足够产生所需增益；Grassmann 导数秩 \(2\) 与其 osculating 秩 \(1\) 的不匹配严格排除直接应用。
- CSWZ 具备所需类型的 robust finite/shading 量词；本族精确 model-hyperplane 退化使其 spread-out 条件在几乎全部尺度失效。
- universal four-Frostman 联合投影有真实线性反例，但它不满足 full-direction graph。这迫使任何正向新估计继续保留方向图相对于 block pencils 的信息。

这些是明确工具边界，不是新的维数下界或重大中间结果。不把固定 \(P\) 的 a.e.-时间结论直接当作对全部 \(\delta\)、任意 \(P_j\) 的共同异常集界；也不使用独立 \(t_1,t_2\)、product 例或光滑 selector 内点替换原任务。是否继续该子类由本轮 macro 决定，不以额外任意 irreducibility 条件自动缩小主目标。

## 9. 追加审查：是否已有相对于点集的 pencil/BL 版本

root 随后要求检验：family 虽处在固定 pencils 中，是否有定理可以保留 \(D\mu\) 的满四维来源，而不要求 family 对所有子空间统一 spread-out。现有三项结果的适用失败本身没有回答这个更精细的问题。

已补读 [Shengwen Gan, Exceptional set estimate through Brascamp–Lieb inequality, arXiv:2308.07675v2](https://arxiv.org/pdf/2308.07675v2)，2024-02-09；存档前缀 R0014_gan_2308_07675_v2，650385 bytes，SHA256 5b3ba237487b8a474c70dbb17f6c54fbbe5e859291903f2910986e8cfadff62e。实际读 Introduction、Theorem5 的 dimension-profile 声明、§5.2 Theorems25/26 及式(70)；没有重证全文。

其 Theorem5 的 bound 由 ambient \(n,k\)、\(\dim_H A=a\)、exceptional set 的维数参数 \(t\) 及最坏子空间投影维数 profile 决定，不含 \(D\mu\) 或对某个固定 graph 选择的适应条件。式(70) 使用的 BL 亏损是
\[
 \operatorname{BL}(\{H_{t_i}\},p)=
 \sup_{Z\le\mathbb R^6}
 \left(\dim Z-\frac pJ\sum_{i=1}^J\dim\pi_{H_{t_i}}Z\right).
 \tag{R1}
\]
第 6 节的同一个 \(Z=B_1\oplus\mathbb Re_c\) 对任意选出的 \(t_i\in I\) 都给
\[
 \operatorname{BL}(\{H_{t_i}\},p)\ge4-3p.
 \tag{R2}
\]
因此该直接的全空间 BL 工具仍对坏子空间付费；它没有因本轮点集的 full \(D\)-graph 来源而自动去掉这个代价。不能把 universal dimension-profile 估计改写为尚未证明的 relative-to-\(P\) 估计。

Wang ICM 2026 的 Question1.5 精确提出了这种相对问题：当投影族落在 pencils 中时，点集相对于这些子空间应满足何种条件才能保留 Marstrand 型结论。Du Conj1.6 则是按最坏子空间 rank 制定的一般猜想，不是已证的 adapted-to-\(P\) 版本。本次有限核读尚未找到可以把原 \(D\mu\) cap 直接代入、处理任意同时间 selections 的相对定理。未宣称这类定理在全部文献中不存在；本轮新的 joint cycle 机制另由 root 审查，不由这里的工具不适用推断其成败。
