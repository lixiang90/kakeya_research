# R0003：原始 guards、切线窗口与分支幅度

日期：2026-10-16（Asia/Shanghai）。任务：N5-SCALE-02。审读对象为已入库四维稿的 Definition 2.1–2.2、Theorem 2.17、§4.2–4.3、Proposition 4.11 的系数段，以及 (6.30)–(6.40)。本轮没有下载新文献。

## 0. 任务、量词与本轮结论

长期目标仍是高维 Kakeya；本轮只审计一个可以明确核查的接口：原始分辨率控制是否能把共同方向网格细化到 \(a_2/S_0\)，而不改变已经选好的熵窗口。

待检验的统一结论是存在固定 \(C<\infty\)，使真实临界路径的相关分支满足

\[
S_0/a\le N^C,\qquad N=N_0^{\epsilon_n},\quad\epsilon_n\to0,
\]

其中 \(C\) 不随 \(n,i,N_0,\epsilon_n\) 或选中场景变化。

**本轮可严格得出的结论：**

1. 已读定义和 guard 的显式系数/范围控制给出的是原始尺度 \(N_0^{P(M_{\rm path})}\)，没有写出或推出统一的切线固定幂界。这里的推导是具体的分支范数控制，见 §2。
2. 有一个比“换底后指数变大”更强的预算障碍：原熵窗口只控制不细于 \(N^{-U_n}\) 的速度网格，且要求 \(U_nD_n\epsilon_n\to0\)。若 \(S_0/a\) 为固定原始幂 \(N_0^m\)，要求网格细到 \(a_2/S_0\) 就迫使 \(U_n\epsilon_n\gtrsim m\)，直接破坏上述熵预算，见 §3。
3. 本轮补验了此前没有验证的完整原始条件：**超大 \(S\) 能与原文 version 2 的 piecewise-constant、全系数空间 Lebesgue prior 及 native bounds 同时相容。** §5 给出原文 \(j=2\) 版本的显式半代数厚化，不再使用奇异 Cantor prior 或零体积参数化。
4. 上述检查没有构造满足 \(\mathcal C(d)\)、positive horizon、所有 true floors 和临界极值性的完整模型。因此不能据此断言“真实临界路径不可能另有统一界”。对真实临界路径的完整蕴含仍未解决；本轮排除的是仅凭这些已读范围、系数 guards、分支稳定与原生导数界就得到该界的推理。

独立反例测试是让 \(S=N_0^m\)，同时令切线深度单位 \(\epsilon_n\to0\)。停止条件：若文中另有 \(M_{\rm path}=O(\epsilon_n)\)、原始 \(w\) 范围为切线固定幂、或直接的相对幅度界，则必须使用并重新核验；不能仅以 guards 很大或输出已 tempered 代替这个缺失条件。本轮没有发现这样的附加界。

## 1. 原文实际限制了哪些量

| 位置 | 确切内容 | 不包含的结论 |
|---|---|---|
| Definition 2.1，p.8 | version 2 中 \(w=w_0+tW\) 仿射；\(y,V\) 为 \(K_0\) 有界；\(X=P_*\) 与其隐藏导数满足 (2.1) | 没有要求 \(w_0,W\) 为 \(K_0\) 有界 |
| p.8，Definition 2.2 前 | polynomial 是 \(N_0^M\)，\(M\) 在一个 exact sequence 内固定；换 exact problem 可任意增大 | 没有要求 \(M\) 是切线窗口长度的 \(O(\epsilon_n)\) |
| Definition 2.2，p.8 | 参数范围、系数、\(B,B^{-1}\)、密度高度/片数等原始多项式有界；full coefficient coordinates 上 piecewise-constant Lebesgue prior；条件实常数不设 height 限制 | 不等于所有输入系数或 \(w\) 为 \(N^{O(1)}\) |
| Theorem 2.17，pp.20–21 | 初始见证线的斜率和截距处于固定有界盒；初始化 \(P_*=w,B=1\)，按 \(\delta=N_0^{-1}\) 做独立盒扰动 | 初始有界性不自动成为所有后继归一化世界的切线有界性 |
| Lemma 2.13，pp.15–17 | version 2 保留 \(w\)，将 native test 换成 \(P/a_r\)，导数尺度变为 \(B/a_r\)；坐标变化及逆仅要求原始 polynomial control | 归一化可以引入固定原始深度的放大 |
| §4.2，pp.52–53 | \(M_{\rm path}\) 在抽样 \(N_0\) 前固定；\(M^\#=2^{(M_{\rm path}+n)^2}\)；原始输出复杂度限于 \(N_0^{M^\#}\) | 此 guard 不是 \(S_0/a\le N^C\) 的输入幅度结论 |
| §4.3，p.54 | 归一化隐藏导数单位为 \(B=1\) 后，隐藏值不必在 tangent units 中有界；native signal 有其 native bounds | 不能把 \(X\) 有界误读为 \(w\) 有界 |
| Proposition 4.7(4)，p.54；证明 p.57 | graph 与 native test 复合后的固定阶导数为 \(K\) 有界 | 不是 graph \(f\) 本身的导数有统一绝对界 |
| Proposition 4.11 系数段，p.69，(4.43) | 明确用 \(W\le N_0^{P_0(M_{\rm path})}\) 控制候选系数，并说明不要求其仿射部分在 tangent units 有界 | 原文在该处明确使用原始指数，而非固定切线指数 |
| p.107，(6.39)–(6.40) 后 | 不使用 \(w,L',S_0\) 的绝对大小上界，只用归一化 \(H'\) 和 \(S_0\) 的下界 | 不能在迁移这段时默加 \(S_0\le K\) |

注意 p.17 的 **式 (2.17)** 是窄度定义；本轮使用的反例归约是 p.20 的 **Theorem 2.17**，不是一个叫“Definition 2.17”的条件。

### 1.1 Kpath 与 Mpath 不是同一种控制

§4.2 把原始几何 slack、list 大小、累计准备损失和路径质量倒数收进 \(K_{\rm path}\)。条件 (4.16) 使这些量在切线对角线上为 \(N^{o(1)}\)。但系数范围、坐标变换和 law complexity 的原始指数收进的是 \(M_{\rm path}\)。

原文没有由 (4.16) 得到 \(N_0^{M_{\rm path}}=N^{o(1)}\)。把 \(M_{\rm path}\) 控制的幅度当成 \(K_{\rm path}\) 控制的 slack，会丢掉本任务真正的尺度差异。

## 2. 当前可以推出的分支幅度上界

固定阶段 \((n,i)\) 和它的 exact sequence。由 tempered 参数范围、原始路径坐标变化及隐藏导数单位归一化，计数见证上的 tangent 隐藏值至多

\[
|w|\le W\le N_0^{P_0(M_{\rm path})}.
\]

这正是 p.69 系数证明使用的范围形式；不需要猜测源稿是否暗中把 \(w\) 设为切线有界。

在 §6.9 的稳定分支内，\(|f(u)-w|\le Ka_2\)，且 heavy-group mass 除以 base ceiling 给出 inverse-subpower 的实投影体积。因 \(f\) 是固定关系次数的 holomorphic algebraic sheet，可对 \(f\) 本身应用 Lemma 3.1，pp.26–27 的齐次 norm comparison。稳定球半径、复杂延拓余量及投影体积只损失 \(K\) 因子，于是

\[
\|f\|_{C^0(U)}\le K(W+Ka_2),\qquad
S_0\le\|f\|_{C^0(U)}\le N_0^{P_1(M_{\rm path})}
\]

（如有固定场景常数，可一并写入 \(P_1\)；不宣称一个与所有场景无关的最优指数）。若 \(a=N^{-s}=N_0^{-\epsilon_ns}\)，则得到

\[
\frac{S_0}{a}
\le N_0^{P_1(M_{\rm path})+\epsilon_ns}
=N^{P_1(M_{\rm path})/\epsilon_n+s}.
\tag{A}
\]

这是一个有效的原始多项式界。它不是待证的统一 \(N^C\) 界，即使 \(M_{\rm path}\) 恰好不随 \(n\) 变化也如此。

此推导只给上界，不证明该上界在真实临界路径上达到。本轮没有发现能把 \(P_1(M_{\rm path})\) 替换成 \(O(\epsilon_n)\) 的现有条件。

### 2.1 复合 native bounds 不控制 f 自身

一个直接的机制检查是

\[
P_*(u,w)=w-Sq(u),\qquad f(u)=Sq(u).
\]

此时 \(P_*(u,f(u))=0\)，其所有导数都为零；但 \(\nabla^2f\) 的大小为 \(S\)。因此 Proposition 4.7 的“先复合 native test 再求导有界”与 \(f\) 可以巨大并不冲突。§5 会把这个例子扩展为符合原文 full coefficient Lebesgue prior 要求的版本。

## 3. 从原熵窗口预算推出的分辨率限制

§4.2，p.52 规定

\[
D_n,U_n\to\infty,\qquad U_nD_n\epsilon_n\to0,
\]

并使用原始深度 \(\epsilon_nU_n\) 的 coarse velocity label \(V_*\)。§4.3，pp.55–56 的窗口平均为

\[
H(V_*)\le O(U_n\log N)+o(\log N),
\]

窗口数为 \(\gtrsim(D_n\epsilon_n)^{-1}\)，故选到的窗口具有

\[
I(V_*;\text{end history}\mid\text{start history})
\le O(U_nD_n\epsilon_n\log N)+o(\log N)
=o(\log N).
\tag{B}
\]

p.56 随后明确说明要求的速度网格不细于 \(N^{-U_n}\)。这不是任意 fine velocity labels 的无条件信息结论。

设某分支 \(S_0/a\asymp N_0^m\)，其中 \(m>0\) 固定，而 \(a_2/a=h^e=N^{-kes}\)。为了把 \(f\) 的方向传递误差 \(S_0\rho\) 降到 \(a_2\)，需要

\[
\rho\lesssim\frac{a_2}{S_0}
\asymp N_0^{-m-\epsilon_nkes}.
\]

把该网格纳入原来的 coarse velocity label，至少要求

\[
\epsilon_nU_n\ge m+\epsilon_nkes+o(1).
\]

于是 \(U_nD_n\epsilon_n\ge(m+o(1))D_n\to\infty\)，与预算要求矛盾。这表明：**若只使用原来同一套窗口平均机制，固定原始深度的速度细化无法被它免费容纳。**

这不是证明不能采用别的熵论证，也不是证明旧窗口之外的全方向信息不存在。它准确说明“先任意细化到 \(a_2/S_0\)，再沿用 (B)”是循环或缺失预算的步骤。

### 3.1 原始恢复网格不能替代速度熵网格

Lemma 4.12，pp.62–63，(4.31)–(4.32) 允许为 original-law list recovery 取很细的 **base averaging mesh** \(\rho=N_0^{-D_{\rm mesh}}\)，以取得 \(O(N_0^{-1})\) total-variation error。该网格控制已固定几何标签的 posterior table 实施，不给出对同样精细的 \(V\) 标签的 \(o(\log N)\) mutual-information bound。

所以，原始输出算法能处理 \(N_0^{-D}\) 的 base cells，并不修复上述 coarse velocity entropy 的缺口。

## 4. 显式数值序列：固定原始幂击败每个固定切线幂

为展示范围/guard 数值本身没有隐藏约束，取

\[
\epsilon_n=n^{-3},\quad U_n=D_n=n,\quad
N_{0,n}=2^{n^8},\quad N_n=N_{0,n}^{\epsilon_n}=2^{n^5},
\]

\[
a_n=N_n^{-s},\qquad h_n=N_n^{-ks},\qquad S_n=N_{0,n}^{m}
\]

其中固定 \(s>0\)、\(0<k\le1/2\)、\(m>0\)。则

\[
U_nD_n\epsilon_n=1/n\to0,
\qquad \frac{S_n}{a_n}=N_n^{mn^3+s}.
\]

因此对每一个固定 \(C\)，有 \(S_n/a_n>N_n^C\) 对所有充分大的 \(n\) 成立。

同时，若 native 测试含系数 \(S_n/h_n^2\)，其原始指数为

\[
\log_{N_{0,n}}(S_n/h_n^2)=m+2\epsilon_nks\le m+1
\]

对充分大的 \(n\) 成立。\(S_n/h_n\)、\(h_n^{-1}\)、\(a_n^{-1}\) 及下一节 prior 的密度高度也有固定原始多项式界。

若只检验 §4.2 的数值余量，可取 \(K_{\rm path}=1\)、\(G_n\le n^4\)，于是 (4.15)–(4.16) 的三种比值均趋于 0：

\[
\frac{G_n}{\log N_{0,n}}=O(n^{-4}),\quad
N_{0,n}^{-1}\log N_{0,n}\to0,
\quad
\frac{\log((\log N_{0,n})^n)}{\epsilon_n\log N_{0,n}}
=O(\log n/n^4).
\]

取一个足够大的固定 \(M_{\rm path}\) 即可覆盖下节的全部输入幂；\(M^\#=2^{(M_{\rm path}+n)^2}\) 当然容纳这些有限系数。**这只验证 guard 的数值范围和窗口参数预算，不验证 Lemma 4.6 的无改进排除命题。** 后者以实际临界路径及 Lemma 4.5 为前提，本序列尚未提供它们。

## 5. 新核验：原文 version 2 的 full-coefficient 半代数 prior

本节专门处理 R0002 尚未核验的一项完整原始条件。它使用原稿真实的 \(j=2\)，不是把五维模型误称为原文定义中的 exact problem；其目的仅是核验大幅度是否被 Definition 2.1–2.2 的范围、Lebesgue prior 和 native bounds 直接禁止。

### 5.1 六维轨道系数空间中的支撑

轨道系数为

\[
(Y_1,Y_2,V_1,V_2,w_0,W)\in\mathbb R^6,
\qquad y(t)=Y+tV,\quad w(t)=w_0+tW.
\]

取 \(0<h\le1\)、\(S\ge1\)、\(\delta=N_0^{-D}\)，其中固定 \(D>0\)。在系数空间中定义下列支撑：

\[
|Y_i|\le h,\quad 1\le V_1\le2,
\]

\[
|V_2-V_1^2|\le\delta h^2/S,
\]

\[
\left|w_0+\frac S{h^2}Y_1^2\right|\le\delta,
\qquad
\left|W-\frac S{h^2}(Y_2-2V_1Y_1)\right|\le\delta.
\tag{C}
\]

给这个支撑上**常数**概率密度，支撑外密度为 0。这是 full trajectory coefficient coordinates 上的 piecewise-constant Lebesgue density，不是低维图面的奇异推前测度。

为了算其体积，令

\[
\theta=V_1,\quad e_V=V_2-\theta^2,\quad
e_0=w_0+SY_1^2/h^2,
\]

\[
e_1=W-S(Y_2-2\theta Y_1)/h^2.
\]

这是从 \((Y_1,Y_2,\theta,e_V,e_0,e_1)\) 到全部六个原系数的三角变化，Jacobian 恒为 1。支撑体积恰为

\[
32\delta^3h^4/S,
\]

故概率密度高度为 \(S/(32\delta^3h^4)\)。对 §4 的序列，这是

\[
N_0^{m+3D+4\epsilon_nks}/32\le N_0^{m+3D+1}
\]

（充分大 \(n\)）。支撑只用固定数量、次数至多 2 的多项式条件。所有系数、参数范围及宽度倒数都为固定原始多项式；无需 height 限制、Cantor 极限或指数多个小片。因此 Definition 2.2 的这项 prior 条件得到完整核验。

### 5.2 Native bounds 在整个 unit time 上成立

取一个世界、\(B=1\)，定义

\[
P_*(t,y,w)=w-\frac S{h^2}(ty_2-y_1^2).
\]

把 (C) 中的系数代入，直接展开得到

\[
X(t)=P_*(t,y(t),w(t))
=e_0+t e_1-\frac S{h^2}t^2e_V.
\tag{D}
\]

因此在整个 \([0,1]\) 上 \(|X(t)|\le3\delta\)，并有

\[
\partial_wP_*=1,\qquad\partial_{ww}P_*=0.
\]

\(y,V\) 有固定常数上界。\(w_0\) 至多为 \(O(S)\)，\(W\) 至多为 \(O(S/h)\)，它们可能不是 \(K_0\) 有界，但仍受 Definition 2.2 允许的原始多项式控制。令全部 incidence 都被选中，独立 uniform time 的总成功质量为 1，满足 Definition 2.1 的选择质量要求；不必把一个短 \(h\)-block 的质量误当成全 parent 的 dense mass。

在 \(t=hu_0,y_i=hu_i\) 的局部坐标，原生零分支为

\[
f(u)=S(u_0u_2-u_1^2).
\]

它是整多项式，稳定判别量为 1；\(S_0\asymp S\) 于任一固定非退化比较球上。native 复合恒为零，真实轨道与分支的误差由 (D) 控制到 \(3\delta\)。取固定 \(D\) 足够大，可以使这误差小于当前 \(a_2\)，同时所有原始多项式指数仍然固定。

所以，大 \(S\) 既不违反 native hidden derivative 下界，也不违反隐藏曲率上界；大底座二次项的抵消确实能在一个合法的全系数 Lebesgue prior 内发生。这个核验比 R0002 的奇异精确线族多了一项原文的真实有限性条件。

### 5.3 没有核验的条件

本节没有证明该 exact problem 在目标深度族上具有 \(\mathcal C(d)\) 的相对密度与 angular 条件、(6.6) 的参与系数箱下界、嵌套 true packets、原始 \(p_L\) list knowledge、positive horizon 或临界极值性。

特别地，“native 测试在整个 unit time 都很小”并不单独证明 minimum horizon 为 0，因为 Definition 2.14，p.17 还要求构造满足终端 true floor 的系统。此处既不登记 \(H=0\)，也不登记 \(H>0\)。

该局部分支的 primary quadric 在三维 base 中，原四维定理可以利用其单生成元结构；因此这个检验完全不反驳原稿四维次数恢复。它只排除一个会错误禁止巨大 \(S\) 的输入读取方式。

## 6. 对 R0002 五维模型的准确影响

R0002 的耦合剪切参数是 \(\varepsilon_{\rm shear}=a/S_0\)，本节的切线深度单位是 \(\epsilon_n\)。两者不是同一个 \(\epsilon\)。当 \(S_0/a\) 为固定原始幂时，\(\varepsilon_{\rm shear}\) 可以位于所有 bounded tangent exponents 之下；甚至 \(U_n\to\infty\) 也不够，因为原窗口还要求 \(\epsilon_nU_n\to0\)。

本轮尚未证明 R0002 的完整五维模型能同时满足 critical-path 输入。已经严格查明的接口是：

- Def2.1–2.2 的 native/tempered 上界本身容许这种幅度。
- 现有熵窗口不能在同一预算下把速度标签细到固定正原始深度。
- 原始 output guards 与 base-list recovery 不提供缺失的 fine-velocity 信息。
- 若想排除该模型，必须使用未在这些上界中体现的条件，例如 participating coefficient-bin lower bounds、原始全方向斜率质量、真系统极值性，或新的多项式方向非集中输入。

后续任务不应再只写“取更细网格”。它应指明从哪一条真实条件推出 \(S_0/a\le N^C\)，或者在不需要这条幅度界的情况下直接检测并排除剪切相关性。

## 7. 验收与边界

本轮形成三项可审查的新内容：由原窗口参数推出的分辨率预算不相容性、原始/切线双尺度的显式数值序列，以及符合原文 full-coefficient piecewise-constant prior 的大幅度 native 模型。

没有形成真实临界路径上的统一幅度定理，也没有完整 critical exact 反例。没有解决一般维度 Kakeya 或改进维数下界，不声称新颖性或重大中间结果。本轮只编辑本文件，未改控制文件或 Git。
