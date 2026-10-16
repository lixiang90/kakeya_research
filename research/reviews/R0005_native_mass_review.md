# R0005：native逆映射的质量界与坐标缩放复核

日期：2026-10-16。审查人：`literature_frontier`。被审文本：`notes/50_counterexamples/R0005_native_coefficient_inverse.md` 的§7–8。本次独立审查只覆盖其中的固定模型质量界及坐标算术；不将root对其§1–6构造的独立检查冒称为本人的全文复核。

结论：在明确的同prior、同坐标、固定模型及$0<p\le1$网格条件下，§7的质量界通过；§8的隐藏斜率缩放也通过。它们没有给出所有临界数据的排除，也没有改进Kakeya维数下界。

## 1. 质量界的独立推导

固定

$$P_*=\alpha w-\beta(tY_3-Y_1Y_2),\qquad\beta\ne0.$$

沿$Y=y_0+tV$、$w=w_0+tW$逐项取一次系数，得到

$$x_1=\alpha W-\beta(y_3-y_1V_2-y_2V_1).$$

所以目标事件$|W|\le M_W,\ |x_1|\le M_x$包含于厚度

$$t_*=(|\alpha|M_W+M_x)/|\beta|$$

的带$|y_3-y_1V_2-y_2V_1|\le t_*$。固定一个宽$p$的速度cube及$y_1,y_2$的两个$p$-cells后，因全部位置与速度位于固定$[-R,R]$盒，$y_1V_2+y_2V_1$的摆动至多$C_Rp$。所需$y_3$-cells数因此至多$C_R(1+t_*/p)$；前两个位置坐标的cells数至多$C_Rp^{-2}$。

每个完整affine bin由**同一个未归一化prior**的cap支付$A_{\rm aff}p^3\pi(J)$。相乘后再对速度bins求和，利用$\sum_J\pi(J)\le1$，即得

$$\boxed{\nu(\mathrm{target})\le C_RA_{\rm aff}(p+t_*).}$$

此推导不要求隐藏斜率与可见系数独立，也不要求知道目标分支条件律；但cap必须针对完整prior，不能只在另一后验中有相同名称的常数。若$R$是subpower而非固定常数，$C_R$可取$C(1+R)^C$，须计入实际损失。

若$p\ge t_*$，上界为$C_RA_{\rm aff}p$。因此无需把网格细到关系厚度$t_*$之下；一个事先可用的固定幂小$p$已足以与inverse-subpower目标质量比较。这个结论依赖$A_{\rm aff}$与目标原始质量之间的量级，不能在条件化后删除分母。

## 2. 时间与隐藏坐标的缩放

对固定parent时间变换$t=t_c+q\tau$，若仍保留旧隐藏坐标$w$，则

$$w=(w_0+t_cW)+\tau(qW),\qquad W_{\rm new}=qW_{\rm old}.$$

源Lemma2.13 version2的新native test实际是**所选parent test**$P/a_b$，导数尺度$B_{\rm new}=B/a_b$；它未必等于旧$P_*/a_b$。若进一步定义导数归一化隐藏坐标$\widetilde w=B_{\rm new}w$，则

$$\widetilde W=B_{\rm new}qW_{\rm old}.$$

所以原始$W$的有界范围不能直接作为$\widetilde W$的同一范围。即使通过隐藏坐标缩放把线性系数$\alpha$变成1，质量界中的乘积也不会消失：$\widehat w=\lambda w$时$\widehat\alpha=\alpha/\lambda$、$\widehat M_W=|\lambda|M_W$，故$|\widehat\alpha|\widehat M_W=|\alpha|M_W$。

若恰好继续使用同一个旧native polynomial，则其系数在仅时间变化与除$a_b$后满足

$$x'_0=(x_0+t_cx_1+t_c^2x_2)/a_b,\quad
x'_1=q(x_1+2t_cx_2)/a_b,\quad
x'_2=q^2x_2/a_b.$$

若parent换用了不同test，这个旧系数公式不能代替对新test的计算。可见仿射空间变化还可能改变二次式形状，未必仍是单一$\beta(tY_3-Y_1Y_2)$；应用质量界须重新验证该形式或相应的横向非退化体积估计。

## 3. 可得结论的边界

该质量界提供了一个具体的新使用接口：有界原始$W$、native系数界和位置—方向joint affine cap同时成立时，大$\beta$的指定模型不能免费承载大量原始质量。它没有证明一般native多项式都具有这个横向形状，也没有证明同一tuple $(\alpha,\beta,M_W,M_x,A_{\rm aff},p)$跨全部祖先正规化均受统一控制。

对反例主体的full-coefficient Jacobian、真实$d<1$观测profile、同$B_p$的$W_p$最大原子、单位时间atlas及horizon判定，本次不作全文认证；它们由root另行检查。本文独审结果仅覆盖上述质量与坐标命题，未经外部同行评审。
