# R0004：完整斜率、点态label恢复与熵型选择成本

日期：2026-10-16。互补任务：检验能否把DIR-001中父数量/父质量成本换成条件信息成本，并准确对应真实的pointwise knowledge机制。总目标仍是一般/五维Kakeya，不将下述初等信息论接口声称为新颖或重大中间结果。

已读STATE、DIR-001、已有原始 `06-isotropic.tex` 的测度与条件palette机制，并对照本地PDF的Lemma 4.8、4.9。没有搜索新文献或下载源码。所有离散熵均使用自然对数；方向变量在**同一原始分辨率**上离散化。

可证伪命题：少量pointwise label选项是否自动限制适应父label选择的二次方向薄层总质量？本轮停止条件：若成本不可避免地转入 $I(\text{direction};\text{point/history})$ 或祖先parent信息，便不把低条件label熵重新命名为全局非集中。

## 1. ENT-001a：适应label的事件所需互信息

固定一个概率律 $P$，令 $S$ 是有限方向label，$A$ 是有限父/多项式label，$Z$ 是有限point/history状态。对每个 $a$ 给定一个在**相同 $S$ 网格上可测**的集合 $E_a$。令

$$B=\{S\in E_A\},\quad p=P(B),\quad
q=\sum_aP_A(a)P_S(E_a).$$

则

$$d_{\rm bin}(p\Vert q)\le I_P(S;A),\tag{ENT-1}$$

$$p\log(1/q)\le I_P(S;A)+h(p)
\le I_P(S;Z)+H_P(A\mid Z)+\log2.\tag{ENT-2}$$

这里 $h$ 为二元熵。若 $q=0$，则 $p=0$；其余边界按连续约定处理。若每个 $Z$ 有一个至多 $L$ 项的列表，且 $A$ 在**同一律 $P$ 下几乎处处**属于该列表，则

$$p\log(1/q)\le I_P(S;Z)+\log L+\log2.\tag{ENT-list}$$

**证明。** 取独立参考律 $Q=P_S\otimes P_A$。$D(P_{S,A}\Vert Q)=I_P(S;A)$，而把 $(S,A)$ 推到事件指示量 $1_B$ 的KL数据处理给出(ENT-1)。展开二元KL：

$$d_{\rm bin}(p\Vert q)
=p\log(1/q)-h(p)+(1-p)\log(1/(1-q))
\ge p\log(1/q)-h(p).$$

又由链式法则与非负性，

$$I(S;A)\le I(S;A,Z)
=I(S;Z)+I(S;A\mid Z)
\le I(S;Z)+H(A\mid Z).$$

有限列表给 $H(A\mid Z)\le\log L$，即得结论。这个证明没有假定 $A$ 与方向独立。

还可保留逐label的信息成本。令 $p_a=P(S\in E_a\mid A=a)$、$e_a=P_S(E_a)$，则

$$\sum_aP_A(a)d_{\rm bin}(p_a\Vert e_a)\le I_P(S;A).\tag{ENT-per-label}$$

这是对每个条件律 $P_{S\mid A=a}$ 分别应用KL数据处理，再求和。若每父全部质量都在其事件中，便有 $I(S;A)\ge\sum_aP_A(a)\log(1/e_a)$。小薄层可以被许多适应性label覆盖，但这些label必须携带相应方向信息。

## 2. 选择和失败列表必须支付成本

不能在原始prior上有一个熵界，却把列表成功率仅在后来的submeasure上成立当作(ENT-list)的无损输入。

若 $A$ 在列表外的概率为 $r$，全局label数量至多 $R$，则只能直接保证

$$H(A\mid Z)\le h(r)+(1-r)\log L+r\log R.$$

原始 $R$ 允许是 $N_0$ 的多项式，$r\to0$ 本身未必使最后一项成为 $o(\log N)$；需要相容的衰减率。

对选中事件 $G$、$\alpha=P(G)>0$，令 $\widetilde P=P(\cdot\mid G)$。保留原始方向参考 $\pi=P_S$ 时，链式KL变为

$$D(\widetilde P_{S,A}\Vert\pi\otimes\widetilde P_A)
=I_{\widetilde P}(S;A)+D(\widetilde P_S\Vert\pi).$$

由于 $\widetilde P_S\le\pi/\alpha$，第二项至多 $\log(1/\alpha)$。因此用原始 $\pi$ 估计自适应事件时，可用的选择成本界为

$$p\log(1/q_\pi)
\le I_{\widetilde P}(S;Z)+\log L+\log(1/\alpha)+\log2,$$

其中 $q_\pi=\sum_a\widetilde P_A(a)\pi(E_a)$，且列表必须在 $\widetilde P$ 下几乎处处成功。若只知unnormalized incidence密度 $\lambda\le K\nu dt$、质量 $\alpha$，则相应参考方向密度成本最多写为 $\log(K/\alpha)$，不能漏掉 $K$。

此外，原律的小互信息不自动在稀疏选择后仍小。对选择指示量可由链式法则得到

$$\alpha I_{\widetilde P}(S;Z)
\le I_P(S;Z)+h(\alpha).$$

所以 $I_P=o(\log N)$ 除以一个inverse-subpower成功率之后，未必仍为 $o(\log N)$。这与原稿反复保留固定law和前置分母的做法一致。

## 3. ENT-001b：似然domination与pointwise列表的幂级版本

仅平均互信息 $I=o(\log N)$、$q\le N^{-c}$，由(ENT-2)只得到 $p=o(1)$。它排除固定正比例的substantial事件，但不必排除任意 $N^{-o(1)}$ 质量的discovery family。

更接近source实际机制的条件命题如下。设同一律上的方向/状态边缘满足

$$P_{S,Z}(s,z)\le K\pi(s)P_Z(z),$$

$A$ 在每个 $z$ 的列表 $\mathcal L(z)$ 内，$\#\mathcal L(z)\le L$，且**同一个参考palette**满足 $\pi(E_a)\le\varepsilon$。则

$$P(S\in E_A)\le KL\varepsilon.\tag{ENT-dom}$$

证明：真实事件蕴含 $S\in\bigcup_{a\in\mathcal L(Z)}E_a$；先删去 $A$，在每个固定 $z$ 用上述joint domination，再对至多 $L$ 个方向事件取并集，最后对 $z$ 积分。全局label数量可以任意多。

unnormalized版本也成立：若 $\lambda(S,Z)\le K\pi(S)w(Z)$、$\sum_Zw(Z)\le M_0$，则bad原始质量至多 $KLM_0\varepsilon$。比较其在当前保留质量 $\alpha$ 中的比例时，仍须除以 $\alpha$。

从小互信息可以先作source Lemma 4.8类型的likelihood截断：$D(P_{S,A}\Vert P_S\otimes P_A)=o(\log N)$，允许删 $o(1)$ 总质量后有joint submeasure $P_{\rm good}(S,A)\le N^{o(1)}P_S\otimes P_A$，故bad的good部分至多 $N^{o(1)}q$。但被删的 $o(1)$ 仍可能吞掉一个更小的指定discovery family；截断law与后续成功率需要事先兼容。

若 $E_a$ 来自真实连续方向二次式，必须先把它扩大为同一 $S$ 网格上的方向cell并集，且在 $\varepsilon$ 中计入覆盖边界误差。对固定原始盒中系数归一化的二次式，cell宽 $\delta$ 使值误差增加 $C\delta$；不能把连续零集的零测度直接拿给离散cell事件。

## 4. 与DIR-001相比：什么时候真的更强

DIR-001给出无额外独立性假设的

$$\sum_a\nu(A_a\cap E_a)\le\sum_a\min\{m_a,\text{原始方向体积上界}_a\}.$$

熵型界可以不用全局父数，而按实际 $I(S;A)$ 支付适应性成本。但若只是把 $I(S;A)$ 粗略换成 $H(A)\le\log\#A$，这仍是对父选择成本的重述，不能产生新的源数据约束。

新信息只有在另有真正较小的 $I(S;Z)$ 或joint likelihood bound时出现。一个纯概率例子说明差别：令 $S$ 均匀于 $R$ 个方向cell，$E_a$ 为第 $a$ 个cell；父label $A$ 独立均匀，取 $Z=A$。每父 $m_a=1/R$，DIR-001的min求和可等于1，完全不给衰减；而 $I(S;Z)=0$、列表大小1，(ENT-dom)给真实bad概率 $1/R$。因此新条件下的幂级熵/palette方法确实更强。

相反，若 $A$ 就是方向所在cell，则真实bad概率为1、独立参考概率 $q=1/R$、$I(S;A)=\log R$，正好支付全部成本。pointwise知道 $A$ 不意味着这个互信息小。

## 5. 实际可见时空点也能支付大量label信息：明确长线例子

这个反例只否定“实际pointwise恢复本身使全局palette很小”的推理，**不声称满足 $d<1$、true parent floors或临界路径**。

取原始四维斜率 $(V_1,V_2,V_3,W)$ 独立均匀于固定有界盒，令 $V_1\in[1,2]$，其余范围也固定。独立取 $\zeta_1,\zeta_2$ 均匀于 $[-\epsilon,\epsilon]$，另取 $Y_{03}$ 与隐藏截距 $w_0$ 在固定盒独立均匀。定义完整仿射轨道

$$Y_{01}=V_1+\zeta_1,\quad Y_{02}=V_2+\zeta_2,\quad
Y(t)=Y_0+tV,\quad w(t)=w_0+tW,\quad 0\le t\le1.$$

从这些独立参数到full8 trajectory coefficients的Jacobian为1。故当 $\epsilon$ 为固定原始幂时，这是全系数空间中有限半代数、分段常Lebesgue prior，密度高度为原始多项式；完整斜率边缘仍为有界密度。取 $P_*=w$ 时native bounds也成立。

给定真实可见点 $(t,Y_1,Y_2)$，计算

$$\widehat V_j=Y_j/(1+t),\qquad |\widehat V_j-V_j|\le\epsilon.$$

由于 $V_1$ 有固定上界，

$$|\widehat V_2-\widehat V_1^2-(V_2-V_1^2)|\le C\epsilon.$$

令 $A=\lfloor(V_2-V_1^2)/\tau\rfloor$，取 $C\epsilon<\tau/10$，则在**每条线的全部单位时间**，实际点把这个轨道不变label定位到至多3个整数选项。若使用有限point mesh，令它的宽度也 $\ll\tau$，同一计算只增加固定倍误差，仍有固定列表。它不是只在一个时刻或一个抽象tag上的恢复。

可是全局不同 $A$ 有 $\asymp1/\tau$ 个；每个parent band的原始质量为 $O(\tau)$。对应visible affine平移 $V'_2=V_2-A\tau$ 后，所有条件质量落在 $0\le V'_2-(V'_1)^2<\tau$ 中。这正是DIR-001的父选择代价，实际pointwise列表并没有使它消失。

在原始斜率cell宽 $\delta\ll\tau$ 上，$H(A)=\log(1/\tau)+O(1)$，且 $H(A\mid S_\delta)=O(1)$；故 $I(S_\delta;A)\ge\log(1/\tau)-O(1)$。实际点也必须携带这部分方向信息，因此 $H(A\mid Z)=O(1)$ 与 $I(S_\delta;Z)$ 很大完全相容。

这个例子中隐藏截距和 $W$ 的独立有界盒使隐藏观测保持通常的一维连续变化；它没有建立 $d<1$ 的压缩profile。将 $A$ 称作可由真实点恢复的轨道assignment label是准确的，将它直接称作满足真chart floor的临界parent则不准确。此处未计算其horizon，更不以缺少 $d<1$ 自动推断horizon值。

## 6. 同一原始分辨率上的完整斜率链式界

以原始完整斜率 $S_\delta=(V_\delta,W_\delta)$，均使用同一原始网格 $\delta$。若原始四维斜率密度 $\le C_0$、支撑盒固定，则每个完整cell概率 $\le C_0\delta^4$，而可见cell数 $\le C\delta^{-3}$，所以

$$H(S_\delta)\ge4\log(1/\delta)-\log C_0,$$

$$H(W_\delta\mid V_\delta)\ge\log(1/\delta)-\log C_0-C.$$

这确实是未被可见球cap概括的原始额外信息。加入label和point后的精确记账是

$$\begin{aligned}
H(W_\delta\mid V_\delta,A,Z)
={}&H(W_\delta\mid V_\delta)
-I(W_\delta;Z\mid V_\delta)\\
&-I(W_\delta;A\mid V_\delta,Z).
\end{aligned}$$

最后一项至多 $H(A\mid Z)\le\log L$，但 $I(W_\delta;Z\mid V_\delta)$ 未因此变小。只知pointwise列表小，无法保证保留任何隐藏方向剩余熵。

同样，在已经选定的祖先parent $A_0$ 内，

$$I(S_\delta;Z\mid A_0)
=I(V_\delta;Z\mid A_0)
+I(W_\delta;Z\mid V_\delta,A_0).$$

source对第一个可见项的窗口控制，并不控制第二个隐藏项。即便另证全斜率的窗口增量小，已有祖先成本 $I(S_\delta;A_0)$ 仍在：

$$I(S_\delta;A_0,A_1)
=I(S_\delta;A_0)+I(S_\delta;A_1\mid A_0).$$

例如祖先已记录 $[W]_\delta$，其后的新label恒定，则所有后续增量为零，但隐藏方向熵早已被祖先支付。用全斜率替代可见斜率重做窗口时，还必须保持同一原始网格；不能把原始 $W$ 的粗bin未经仿射畸变成本就当作新parent隐藏方向的同精度bin。

## 7. 与真实source机制对应后的结论

原Lemma 4.8不是凭pointwise knowledge声称全局多项式数量少，而是：在固定parent混合律中，先把**可见velocity bin与end history**的小互信息变成joint numerator domination，再对每个history只有 $K$ 个选项的point states设置entry floors；更晚的稀疏限制需重新剪除分母过小的state。原文没有声称多个时间的方向独立。

`06-isotropic.tex` 中的 $\lambda(W,J)\le K_{\rm pre}m_0(W)\pi(J)$、$\sum_Wm_0(W)\le K_{\rm pre}$，以及用共同palette支付各state列表的步骤，与(ENT-dom)的unnormalized形式一致。这里的 $\pi$ 是**已选parent的visible palette**，并只在事先准备的有限网格上使用。原始完整斜率密度并未在该处升级为每个 $\pi$ 的多项式非集中。

因此本轮有两个可审查接口，但没有完成主线新增估计：

1. 若能在原始坐标的同一方向网格获得共同palette似然界，并使方向薄层有小参考质量，pointwise列表就可把全局父数成本替换为 $KL\varepsilon$。
2. 若只保留源文已有的parent-visible似然界，参考薄层质量仍可能为1，祖先选择成本并未减少。这个版本只是准确重写R0003的成本，不构成新的排除。

一个值得独立检验的后续任务是：从真实全斜率law出发，寻找能同时控制 $I(W_\delta;Z\mid V_\delta,A_0)$ 与祖先信息成本的原始坐标预算；成功时还需证明这部分剩余熵能产生几何增益。若只重复“小增量不等于小总量”，或把 $H(A\mid Z)$ 当作 $I(S;A)$，应立即停止而非延长路线。
