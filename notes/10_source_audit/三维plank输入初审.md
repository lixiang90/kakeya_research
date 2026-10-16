# 三维 plank 输入初审

日期：2026-10-16。状态：**已核验原始陈述和直接证明依赖，未完成整篇 companion 或四维证明的审计**。

原文：[OpenAI companion 的 05-inputs.tex](https://github.com/openai/math/blob/main/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/sections/05-inputs.tex)，Gitblob `ed56986ab92f34a3e134d59cfef5269f26a21b45`。本地 `literature/primary/openai_3d_maximal_source/05-inputs.tex`；只有这一个章节，并非完整可编译项目。

## 1. 实际陈述及与四维稿的对应

四维稿引用的 [24, Lemma 2.3] 对应源码 `lem:weighted-set`（行199开始），标题 *Weighted set estimate in a line chart*。取固定有界的二维空间仿射线图

$$M_i(t)=b_i+tu_i\in\mathbb R^2,\quad 0\le t\le1,\quad\delta=D^{-1}.$$

这是三维时空中的线族。索引有限、正权 $\omega_i$ 任意，允许同一条迹线有多个索引和不同标记集。对所有空间正交轴、仿射移动中心、宽度参数 $1\le a\le b\le D$ 的 **full-time plank**，假设

$$\sum_{i:M_i\subset P}\omega_i\le Aab.$$

这里 $M_i\subset P$ 指整个 $t\in[0,1]$ 迹线被包含，绝不是仅标记部分落入。标记长度为 $D^{-1}$ 的时间格 $J_i$，要求每个索引 $\#J_i\ge D^{1-\eta_{\rm in}}$。$E$ 是标记格中心访问到的**时空网格单元**的并（或固定倍扩大）。结论为

$$\sum_i\omega_i\#J_i\le C A D^\varepsilon\#E.$$

量词次序：先固定图与允许的网格扩大倍数；每个固定 $\varepsilon>0$ 才获得某个 $\eta_{\rm in}>0$ 和 $C$，二者与索引数、权重无关。不能预先让 $\eta$ 任意大或让 $\varepsilon$ 随 $D$ 变而不作对角线控制。

本轮逐项对照本地四维稿 pp.17–18 Lemma 2.15，正权、重复迹线、长标记条件、全时包含、格点访问量和损失均一致。四维稿随后加上的连续加权法则舍入、subpower 图界及慢对角线属于**调用扩展**，不是源码 Lemma 2.3 本身的原始假设，需要在每个实际调用处另审。

## 2. 原证明依赖链

依赖是 `GWZ Theorem 1.1 → companion Theorem 2.1 → companion Lemma 2.2 → companion Lemma 2.3`。此链没有用 companion 后文声称解决的完整三维 maximal 定理，所以这一输入可以被独立审查。

1. 源码行53的 `thm:set-input` 保留 GWZ 的密度阈值：对每个目标损失 $\varepsilon$ 有容许的 $\eta$；若 $\Delta_{\max}(\mathbb T)\le\delta^{-\eta}$、平均 shading 密度 $\lambda\ge\delta^\eta$，则并集体积至少为 $\delta^\varepsilon\sum|T|$。此形式与已入库 GWZ v2 Theorem 1.1 一致；尚未读取 companion 参考文献文件以确认 `GWZ2026` 具体锁定哪一版本。
2. 源码行74–178的 `lem:weighted-convex-set` 将它推广到正权和重复索引。若所有凸体满足 $\sum_{i:T_i\subset K}\omega_i|T_i|\le A|K|$，且每个 shading 密度至少为 $\delta^\eta$，则 $\sum_i\omega_i|Y_i|\le C A\delta^{-\varepsilon}|\bigcup Y_i|$。
3. 源码行225–289的 Lemma 2.3 证明，先将迹线加粗成长度固定、半径 $C\delta$ 的管；以 John 椭球的水平切片构造全时 plank，从 plank cap 推出加权凸聚类常数 $O(A)$。再于各标记时间格中心放不相交小球，得到 $|Y_i|\asymp\#J_i\delta^3$、$|\bigcup_iY_i|\lesssim\delta^3\#E$。应用前一步并约去 $\delta^3$ 即得结论。

## 3. 直接证明的局部检查

加权凸聚类部分采用独立 Bernoulli 抽样。令 $v_i=\omega_i/A$，用凸体 $T_i$ 测试给出 $v_i\le1$，用固定环境球测试给出 $S=\sum_i v_i\lesssim_R\delta^{-2}$。John 椭球与有限精度量化把所有凸体测试压缩成多项式多个盒测试；大偏差和并集界给出 $O(\log(1/\delta))$ 聚类。重复管的抽样重数也被该对数界控制，故保留每条不同管的一条原始索引即可调用 GWZ，同时保留那条索引自己的 shading。$S$ 较小时直接用逐点重数界，避免抽样下尾不足。

plank 到凸体的关键几何是：三维椭球的水平截面中心随时间仿射移动，主轴固定，截面形状仅乘公共标量；包含完整迹线使时间跨度至少为1，故最大截面积 $\lesssim |K|$，并能用面积 $O(|K|)$ 的全时 plank 包围所有计入迹线。加粗管提供每个时间截面半径 $\gtrsim\delta$ 的圆盘，保证宽度下限。固定图界下超出 $D$ 固定倍的宽度，通过两个端点有限分组处理。

这些步骤在尺度与权重上相互匹配，初读未发现直接的维度量纲错误。这个判断不是逐行形式化验证；盒量化对任意凸体的统一控制、常数吸收到密度容差的量词、以及四维稿实际调用中舍入后 cap 的保留仍值得分别复核。

## 4. 对研究路线的直接含义

令 $\mu=(\sum_i\omega_i\#J_i)/\#E$，则原引理的逆否使用给出：全时 plank 集中参数的上确界至少为 $\mu/(C D^\varepsilon)$（取接近上确界的 plank 即可）。物理半宽 $r_1=a\delta,r_2=b\delta$ 时，该参数是 $\delta^2\sum_{M_i\subset P}\omega_i/(r_1r_2)$。这是“高访问重数迫使一个全时 plank 集中”的定量依据；不是凭少数时刻或单尺度图像作出的推断。

五维四维稿式推广会把可见空间从 $\mathbb R^2$ 改成 $\mathbb R^3$，从而要求四维时空的对应加权估计。现有三维 Lemma 2.3 不直接给出它；四维满 Hausdorff 维数声明也不自动给出这种有限尺度、带密度阈值、带任意权重的并集估计。Wang–Zakharov 的一般 convex-Wolff 反例障碍进一步说明，简单把维数符号改成4不足以成立。此处是推广必须解决的明确接口。
