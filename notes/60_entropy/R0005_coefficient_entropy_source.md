# R0005：共同先验的 native 系数熵与混合尺度熵率

日期：2026-10-16（Asia/Shanghai）。任务：N5-ENT-01 的源文审计。已读 GOAL、STATE、AGENTS、ENT-001 及原稿 Definition 2.1、Proposition 4.7 与 §6.1–6.2。本轮只处理固定 parent-native 坐标内的有限网格，不把它当作一般 Kakeya 证明或新的维数估计。

接近长期目标的具体问题：native 三系数的熵是否只给一个总量上界，还是还控制粗 native 系数向细 affine 坐标传递的信息？下面的答案使用原稿明确写出的**混合尺度先验上界**，超出只引用 (6.6) 的上下界。其几何有效性仍以原稿相应准备与聚类输入成立为条件。

## 1. 精读位置与正确的概率对象

源码均为 `literature/primary/openai_4d_source/06-isotropic.tex` 的当前入库版本；页码为 175 页原 PDF 的页码。

| 源位置 | 本轮实际使用的输入 |
|---|---|
| Definition 2.1，PDF p.8 | \(y(t)=y_0+tV\)，\(y,V\) subpower 有界；\(X=x_0+tx_1+t^2x_2\) 的三系数由单位时间插值而 subpower 有界。version 2 是 \(j=2\)，不是 \(j=3\) |
| TeX 54–66，PDF p.86 | parent/world 包含在 state 内；incidence 一般不归一化，\(\lambda\le K\nu dt\)；later restriction 不继承早期 incidence saturation |
| TeX 68–89，PDF pp.86–87 | 在 sparse selection 前准备共同有限网格与 joint caps；无多时刻速度独立性声明 |
| TeX 195–210，PDF p.88，(6.6) | \(B_p\) 是全部 \((y_0,V,x_0,x_1,x_2)\) 的 aligned dyadic cube；额外 tags 不属于 bin；同一未归一化 \(\nu^\circ\) 对每个 participating block 给上下界 |
| TeX 212–240，PDF pp.88–89，(6.7)–(6.8) | rectangular joint cap；active line–time marks；共同时间 partition；保留 weighted occupation 至少 \(K^{-1}\) 的完整轨道，定义并冻结 \(\nu^\circ\) |
| TeX 242–253，PDF p.89 | 明写 \(\nu^\circ(A_p)\le Kp^j\pi(V_p)\) 及混合尺度 \(\nu^\circ(A_p,C_r)\le Kr^dp^j\pi(V_p)\)，\(r\ge p\) |
| TeX 255–270，PDF p.89 | (6.6) 下界用 physical support、scalar clustering 和删轻得到；不是从概率归一化自动得到 |
| TeX 272–281，PDF p.89，(6.9) | 再删轻 physical-cell entries 后，给定同一 physical cell 与 velocity bin，只有 \(K\) 个参与 coefficient blocks，因而有导数列表 |
| TeX 283–292，PDF p.89 | 邻近网格插值还要删 palette-light children；所有上下界仍关于同一 \(\nu^\circ\)，later labels 不建立新 saturation |

固定一个 parent-native world，只用 \(0<p\le r\le1\) 的已准备尺度。写

\[
C=(x_0,x_1,x_2),\qquad A=(y_0,V),\qquad
C_p=[C]_p,\quad A_p=([y_0]_p,[V]_p).
\]

所有网格取同一个 aligned dyadic 系统，所以 \(p<r\) 时 \(A_r,C_r\) 是 \(A_p,C_p\) 的确定函数。设 \(\pi\) 是此 parent 冻结的概率 velocity palette，\(\Pi_p(v)=\pi([V]_p=v)\)；若仅用总质量为 subpower 的参考 palette，先归一化并将其总质量并入以下常数。

用 \(K\ge2\) 同时控制本轮有限网格的固定幂损失。源码中的每次 \(K\) 可以增大；以下为看清依赖，把需要的三项明确列出：

\[
\begin{aligned}
\nu^\circ(B_p)&\ge K^{-1}p^{j+d}\Pi_p(v)
&&\text{对参与的 }B_p=(a,c),\tag{F}\cr
\nu^\circ(A_p=a)&\le Kp^j\Pi_p(v),\tag{A}\cr
\nu^\circ\{A_p=a,C_r=c\}&\le Kp^jr^d\Pi_p(v)
&&\text{对准备过的 }r\ge p.\tag{M}
\end{aligned}
\]

在 \(r=p\) 时，(M) 就给 (6.6) 的 upper half。零 palette bins 在这些测度下均为空，可忽略。

熵必须相对于概率律定义。以下取**一个固定的概率轨道律** \(P\)，满足：

1. 在所讨论各尺度，\(P\) 支持于对应 participating coefficient bins；
2. 若需要熵下界，再要求 \(P\le D\nu^\circ\)，\(1\le D<\infty\)；
3. \(|y_0|_\infty\le R_y\)，\(R_y\) 为 subpower。

常见来源是一个后续 incidence submeasure \(\lambda'\le G\nu^\circ dt\)，总质量 \(\alpha>0\)。将 \(\lambda'/\alpha\) 投影到轨道便得 \(D=G/\alpha\)，因为 parent 时间为 \([0,1]\)。不需要后续 \(\lambda'\) 仍有每线长 occupation；长 occupation 已经用于建立共同先验的 (A)、(M)。若把 \(\nu^\circ\) 本身归一化，其 \(D\) 为 \(1/\nu^\circ(\mathrm{all})\)，但还必须检查其全体轨道是否都落在 participating bins，不能由原文的 “every participating block” 反推这个覆盖。

所有熵用自然对数。额外 trajectory tags 可以完全任意；以下只控制可观察的系数 bins，不控制 tag 熵。

## 2. 总条件熵：不偷用 affine 边缘上界

### 2.1 上界必须同时使用 (F) 与 (A)

固定 \(A_p=a\)。不同 \(C_p\) 所对应的 coefficient bins 两两不交，每个 participating bin 由 (F) 至少有 \(p^{j+d}\Pi_p(v)/K\) 的 \(\nu^\circ\)-质量。因此由 (A)，参与个数至多

\[
\#\{C_p\text{ participating}\mid A_p=a\}
\le K^2p^{-d}.
\]

于是对**任何**支持于这些 bins 的 \(P\)，不论它是否 sparse，

\[
E_P(p):=H_P(C_p\mid A_p)
\le d\log(1/p)+2\log K.
\tag{E-upper}
\]

这个支持数上界无需 \(P\) 与 \(\nu^\circ\) 的 domination；因而在进一步 restriction 后不支付成功率分母。但是 floor 单独不够：它还需要 (A)，而 (A) 的来源是 joint caps 加 preceding long occupation。

例如只在一个 \(A_p\) 上均匀放置 \(\asymp p^{-(j+d)}\) 个 coefficient bins，就满足 (F) 的量级，但条件熵为 \((j+d)\log(1/p)+O(1)\)，不是 \(d\log(1/p)\)。原稿实际 \(j=2,d<1\) 时，这些 bins 可以放进固定有界的三系数盒。这只是说明 (F) 在逻辑上不足的有限-bin 例子，不是满足全部源 joint caps 的模型。

### 2.2 下界不要求每个 affine bin 都饱和

现在用同一概率律 \(P\le D\nu^\circ\)。由 (M) 的 \(r=p\) 情形，

\[
P(A_p=a,C_p=c)\le DKp^{j+d}\Pi_p(v).
\]

所以

\[
H_P(A_p,C_p)
\ge (j+d)\log(1/p)
 +\mathbb E_P\log\frac1{\Pi_p(V_p)}-\log(DK).
\]

给定 \(V_p\)，可取的 \([y_0]_p\) 至多 \(C_j(1+R_y)^jp^{-j}\) 个。记

\[
c_y=\log\bigl(C_j(1+R_y)^j\bigr).
\]

于是

\[
\begin{aligned}
E_P(p)
&\ge d\log(1/p)-\log(DK)-c_y\\
&\qquad+D_{\rm KL}(P_{V_p}\Vert\pi_p)
\ge d\log(1/p)-\log(DK)-c_y.
\tag{E-lower}
\end{aligned}
\]

这里没有把 \(\nu^\circ(A_p)\) 设成 \(p^j\Pi_p\)，也没有假设 \(P\) 的 velocity marginal 等于 \(\pi\)。非负的 KL 项准确支付两者的差别。若 \(\log D,\log K,\log(1+R_y)=o(\log N)\)，便有

\[
H_P(C_p\mid A_p)=d\log(1/p)+o(\log N)
\tag{E}
\]

于所有已准备、并保持同律与 participation 的固定幂尺度。若后续选择成功率为固定幂而非 inverse-subpower，\(\log D\) 可能为 \(\Theta(\log N)\)，下界不能再以 \(o(\log N)\) 表述。

### 2.3 若直接问完整归一化 \(\nu^\circ\)，须记录未参与质量

令 \(M=\nu^\circ(\mathrm{all})>0\)、\(P_0=\nu^\circ/M\)，\(\varepsilon_p\) 为 \(P_0\) 落在 nonparticipating coefficient bins 的概率。设 native 三系数范围在 \([-R_C,R_C]^3\) 内，记 \(c_C=3\log(C(1+R_C))\)。通过先揭示 good/bad 指示量，得到

\[
\begin{aligned}
H_{P_0}(C_p\mid A_p)
\le{}&h(\varepsilon_p)
+(1-\varepsilon_p)\bigl(d\log(1/p)+2\log K\bigr)\\
&+\varepsilon_p\bigl(3\log(1/p)+c_C\bigr).
\tag{Full-prior-upper}
\end{aligned}
\]

同样，细尺度不参与的质量最多需付完整三系数 children，故

\[
\begin{aligned}
H_{P_0}(C_p\mid C_r,A_p)
\le{}&h(\varepsilon_p)
+(1-\varepsilon_p)\bigl(d\log(r/p)+2\log K\bigr)\\
&+3\varepsilon_p\log(r/p).
\tag{Full-prior-rate}
\end{aligned}
\]

这里每个 dyadic \(r\)-cube 恰有 \((r/p)^3\) 个细三系数 children，故第二式不需另付系数范围。相反，(E-lower) 使用 \(D=1/M\) 仍然成立，因为 (M) 的 numerator upper 不限于 participating bins。

若 \(\varepsilon_p=o(1)\)，\(M^{-1},K,R_y,R_C\) 为 tangent subpower，则完整 \(P_0\) 也得到同样 \(o(\log N)\) 精度。但只能在有证据时使用该 \(\varepsilon_p\)：若对定义 \(\nu^\circ\) 的**同一 preceding occupation law**，所有 bad-bin trajectories 的 incidence 质量至多 \(\delta_p\)，长 occupation 才给 \(\varepsilon_p\le K\delta_p/M\)。后期稀疏 \(\lambda\) 上的小删除量不自动给这个全先验界。实际应用可以直接取所有 prepared participation 删除之后的 incidence 概率律，使用前两节的 \(P\) 与其明确 \(D=G/\alpha\)，避免偷换全先验覆盖。

## 3. 真正的熵率来自混合尺度上界 (M)

### 3.1 直接数细系数 children

固定准备过的 dyadic \(p<r\)，以及 \((A_p=a,C_r=c)\)。其中参与的细 coefficient bins 各有至少 \(p^{j+d}\Pi_p(v)/K\) 的先验质量。由 (M)，其总质量至多 \(Kp^jr^d\Pi_p(v)\)。故

\[
\#\{C_p\text{ participating}\mid A_p=a,C_r=c\}
\le K^2(r/p)^d.
\]

对同一律 \(P\) 得到

\[
\boxed{
H_P(C_p\mid C_r,A_p)
\le d\log(r/p)+2\log K.}
\tag{Rate-upper}
\]

它无需 \(D\)，且是窗口宽度 \(\log(r/p)\) 的界。不能只从两个总量上界相减得到它；真正的新输入是源码 247–248 行的 mixed-scale numerator cap。

### 3.2 精确 transfer 恒等式及其控制

因为网格嵌套，恒等式为

\[
H_P(C_p\mid C_r,A_p)
=E_P(p)-E_P(r)+I_P(C_r;A_p\mid A_r).
\tag{Transfer}
\]

故即便 (E) 在两个尺度成立，也不能直接删掉最后一项。现在 (Rate-upper) 才补上这一步。若两尺度均有 participation，且同一 \(P\le D\nu^\circ\)，用 (E-upper)、(E-lower) 与 (Rate-upper) 得

\[
\boxed{
0\le I_P(C_r;A_p\mid A_r)
\le \log D+5\log K+c_y.}
\tag{Transfer-bound}
\]

同时令 \(\Delta=\log D+3\log K+c_y\)，则

\[
\left|E_P(p)-E_P(r)-d\log(r/p)\right|\le\Delta,
\tag{Rate-total}
\]

\[
d\log(r/p)-\Delta
\le H_P(C_p\mid C_r,A_p)
\le d\log(r/p)+2\log K.
\tag{Rate-two-sided}
\]

因此在固定幂窗口、所有损失及选择分母都为 subpower 时，系数新增熵的 rate 为 \(d+o(1)\)，而 coarse native 系数向 fine affine 坐标的额外 transfer 是 \(o(\log N)\)。若窗口比 \(\log K\) 还窄，不能把误差除以窗口而仍声称 rate 接近 \(d\)。不必逐层累加 \(O(\log K)\)：只要两端 mixed cap 已准备，可直接用两端公式。

### 3.3 没有 (M)，总量饱和与两端 floors 仍不足

以下有限-bin 例子准确隔离 (M) 的作用。取 \(j=2,d=1/2\)，\(p=2^{-4m}\)、\(r=2^{-2m}\)，\(V\) 固定于一个 bin，palette 质量为 1。令 \([y_0]_p\) 在单位方形的全部 \(p\)-bins 上均匀。每个 \(r\)-bin 有 \(2^{4m}\) 个细 affine children；从 child label 的前 \(m\) 个 bits 读取均匀 \(S\in\{0,\ldots,2^m-1\}\)。独立取均匀 \(U\in\{0,\ldots,2^{2m}-1\}\)，设置

\[
x_0=Sr+Up,\qquad x_1=x_2=0.
\]

用半开区间或 bins 内固定内点消除边界歧义。则 \(C_r=S\) 由 \(A_p\) 决定，在给定 \(A_r\) 时仍均匀；给定 \(A_p\) 的细 \(C_p\) 有 \(2^{2m}\) 个等概率选项。

两个尺度均有精确的 \(\nu(A_s)=s^j\)、\(\nu(B_s)=s^{j+d}\)，系数保持有界。因此两端 (6.6) floors/upper 和 (A) 全部成立，且

\[
E(p)=2m\log2=d\log(1/p),\qquad
E(r)=m\log2=d\log(1/r).
\]

但

\[
I(C_r;A_p\mid A_r)=m\log2,
\quad H(C_p\mid C_r,A_p)=2m\log2,
\]

比 \(d\log(r/p)=m\log2\) 大一倍。它恰好违反源 (M)：固定 \(A_p\) 后相应 \(C_r\) 的质量为 \(p^j\)，不是 \(O(p^jr^d)\)。此例不满足全部 joint caps/long-line physical support；其用途只是说明 transfer 不能被 (6.6) 的两端熵饱和自动删除。

## 4. (M) 的 long-duration 与 mesh 证明链

源码 247–252 行本身已经陈述并解释 (M)。为审查归一化，展开其逻辑如下：

1. 对固定 \(A_p=a\)，在时刻 \(t\) 可见位置 \(y_0+tV\) 在一个随 \(t\) 移动的 \(O(p)\) 盒内。对固定 \(C_r=c\)，\(X(t)\) 在一个移动的 \(O(r)\) 区间内，因为 \(0\le t\le1\)。velocity 仍在同一 bin \(V_p\)。
2. 所有相关 native 系数与速度有界，故共同时间 partition 细到 \(o(p/K)\) 后，在每个时间块中可用固定扩大盒包住这些 moving constraints。这里必须是预先准备的有限 meshes 及其所需 rectangular caps；不能选择一个更细的后验尺度而继续免费使用原常数。
3. (6.7) 给每个时间块的 incidence numerator 上界 \(K|I|p^jr^d\Pi_p(v)\)。对整个单位时间求和，仍为 \(Kp^jr^d\Pi_p(v)\)。
4. 定义 \(\nu^\circ\) 时，每个保留完整轨道的**preceding weighted occupation** 至少 \(1/K\)。对这个 line-invariant coefficient event 积分并除以该下界，才得到 (M)。这是 \(\nu^\circ\) 的上界，不是把某一时刻的 success 条件概率当作 prior。
5. 然后冻结 \(\nu^\circ\)。后来的删标签/删 incidence 仍使用这个 numerator 及相同 palette。若最后将一个质量 \(\alpha\) 的 submeasure 归一化，只有下界与 transfer 的误差中引入 \(\log(G/\alpha)\)；支持数版本的 (Rate-upper) 不引入它。

下界 (F) 另依赖 §6.2 physical support 与 Lemma 5.1 scalar clustering。这条证明没有重新验证这些上游定理。其 finite-grid 结论只在原文共同准备、删轻与慢对角顺序内使用；不能宣称一个固定 \(\nu^\circ\) 在所有无穷细尺度同时满足 uniform \(K\)。

## 5. (6.9) 补什么，不补什么

令 \(O_p=[t,y(t),X(t)]_p\) 为物理 observation；避免与原始隐藏斜率 \(W\) 混名。源码 208–209、272–277 行在删去 light entries 后给出：每个 \((O_p,V_p)\) 至多兼容 \(K\) 个 participating full coefficient bins。取**同一后续 incidence 概率律**，其轨道边缘就是前述 \(P\)，便有

\[
H(C_p\mid O_p,V_p)\le\log K.
\tag{Point-list}
\]

(6.9) 显式陈述的是 \(X'\) 的 \(p\)-列表，是这个更完整 coefficient-block 列表的推论。该结论需要 entry floor 的额外删轻，不能只由 (F) 推出。进一步条件于 \(A_p\) 后右边仍成立，结合 (E-lower) 可得

\[
I(C_p;O_p\mid A_p)
\ge d\log(1/p)-\log(DK)-c_y-\log K.
\]

所以真实物理点可携带 native 系数的 \(d\log(1/p)\) 信息；不能把“小 pointwise 列表”解释成物理点与 native 系数近乎独立。它也不控制原始隐藏斜率的 \(I(W_\delta;O\mid V_\delta,\text{ancestors})\)。

## 6. 可用于后续研究的结论与边界

本轮得到的严格 conditional entropy 接口是 (Rate-upper)、(Transfer-bound) 与 (Rate-two-sided)，关键输入为同一 \(\nu^\circ\) 的 mixed-scale cap (M)，不是 floor alone。原稿实际 \(j=2\)；若五维拟推广 \(j=3\) 已能建立同样 caps、长期 prior 与 scalar-clustering floors，完全相同的有限离散证明才适用。这里不补齐该几何归约。

仍未得到原始全斜率的几何增益，原因已具体收缩为以下接口：

- 结论固定一个 parent-native world；跨 world 混合须把 parent/world label 放入 conditioning。删掉该 label 可能增加其全部祖先信息成本。
- \(C_p\) 始终是同一个 native polynomial 的三系数。在 parent normalization 更换 native test、减去不同多项式、除以新尺度时，原变量不再是同一个 \(C\)；新 \(C_p\) 的恢复可能需要更细旧 bins 或原始 hidden 变量。以上 rate 不能免费跨此转换传递。
- 原始完整斜率的 \(W_\delta\) 尚未由 native 三系数在同一 \(\delta\) 下恢复。其坐标条件数、分支、导数尺度、已有祖先成本和 selection denominator 必须另证；\(d<1\) 的 native 熵率本身没有消除它们。

未声称数学新颖性、一般 Kakeya 改进或 full critical 模型反例。若原始 \(W\) 桥接仍只能付固定幂的旧精度/祖先成本，应按本轮停止条件冻结这个版本，不能把上述正确熵率反复改写成进展。
