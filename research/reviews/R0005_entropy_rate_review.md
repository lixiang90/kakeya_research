# R0005：共同先验系数熵率的内部独立复核

日期：2026-10-16。审查人：`literature_frontier`。被审文本：`notes/60_entropy/R0005_coefficient_entropy_source.md` 的§2–3；对照本地已归档 `06-isotropic.tex` 242–253行确认其明写的混合尺度上界。本次只审核明确列出的有限离散假设(F)、(A)、(M)、participation、同一概率律及domination后的推论；**不声称重新验证scalar clustering、physical support或整条几何准备**。

结论：所列总条件熵、混合尺度rate、transfer界与有限-bin反例均通过内部独立复核。其数学新颖性及高维Kakeya应用尚未建立。

## 1. 总条件熵的两边

固定$A_p=a$后，各参与$C_p$箱互不相交，每箱(F)质量至少$p^{j+d}\Pi_p(v)/K$，总质量由(A)至多$Kp^j\Pi_p(v)$。所以参与数至多$K^2p^{-d}$，得到

$$H_P(C_p\mid A_p)\le d\log(1/p)+2\log K.$$

此步对任意支持于这些箱的同一概率律$P$成立，不需要$P\le D\nu^\circ$。

用domination及(M)的$r=p$情形，有$P(a,c)\le DKp^{j+d}\Pi_p(v)$，因此

$$H_P(A_p,C_p)\ge(j+d)\log(1/p)+\mathbb E_P\log(1/\Pi_p(V_p))-\log(DK).$$

扣除$H_P(A_p)\le H_P(V_p)+j\log(1/p)+c_y$后，剩余cross-entropy减$H_P(V_p)$正是

$$D_{\rm KL}(P_{V_p}\Vert\pi_p)\ge0.$$

故E-lower正确；它没有偷用affine marginal lower、没有令$P_V=\pi$，也没有把unnormalized先验直接代入Shannon熵。损失$\log D$必须保留。

## 2. 混合尺度rate及transfer常数

固定$(A_p=a,C_r=c)$后，每个参与fine coefficient箱由(F)支付$p^{j+d}\Pi_p(v)/K$，其并集由(M)支付$Kp^jr^d\Pi_p(v)$，故fine children数至多$K^2(r/p)^d$。这直接证明

$$H_P(C_p\mid C_r,A_p)\le d\log(r/p)+2\log K.$$

关键是对相同$A_p$使用粗$C_r$的(M)，而不是相减两个总熵上界。此支持数版本也无需domination。

因为共同dyadic网格嵌套，$C_r$是$C_p$、$A_r$是$A_p$的确定函数，准确恒等式为

$$H_P(C_p\mid C_r,A_p)=E_P(p)-E_P(r)+I_P(C_r;A_p\mid A_r).$$

代入fine总熵下界、coarse总熵上界及上面的rate上界，误差依次为$\log D+\log K+c_y$、$2\log K$、$2\log K$，合计

$$I_P(C_r;A_p\mid A_r)\le\log D+5\log K+c_y.$$

两端总熵之差的误差为$\Delta=\log D+3\log K+c_y$；结合互信息非负即得Rate-total、Rate-two-sided。以上常数与符号均正确。参与support、网格、native变量和概率律必须在两尺度相同；窗口窄于这些误差时不能把误差除以窗口而宣称rate接近$d$。

## 3. 有限-bin反例的逐项核算

§3.3取$j=2,d=1/2,p=2^{-4m},r=2^{-2m}$。每个fine affine箱概率$p^j=2^{-8m}$；给定该箱，$U$有$2^{2m}$个等概率选项，所以fine完整箱质量为$2^{-10m}=p^{j+d}$。

每个coarse affine箱概率$r^j=2^{-4m}$；该箱内$S$均匀于$2^m$个选项，所以coarse完整箱质量为$2^{-5m}=r^{j+d}$。由$x_0=Sr+Up$且$0\le Up<r$，可得$C_r=S$、$C_p$在给定$A_p$后仍有$2^{2m}$个选项。因此总熵两端饱和、transfer为$m\log2$、真实rate为$2m\log2$，而$d\log(r/p)=m\log2$。

固定$A_p$后的对应$C_r$事件质量为$p^j$，(M)右边在常数$K$下为$Kp^jr^d=Kp^j2^{-m}$，恰差因子$2^m/K$。所以该有限-bin例子准确说明(M)不可从两端floors/upper自动推出；它不是满足全部源输入的轨道模型。

## 4. 审查范围与几何含义

这组界在固定parent-native变量内，比总条件熵的单独饱和多控制了粗系数向细affine坐标的transfer；该信息确实来自额外的mixed-scale cap。审查通过不意味着它已控制原始完整斜率$W$，也没有支付native重置、反解分支、原始分辨率或全部祖先信息成本。

KT2001的跨轨道pair/corner/angle-pivot增益没有由这些有限熵恒等式自动得到。比较详见 `notes/60_entropy/R0005_KT_and_geometric_budget.md`。该比较笔记由本审查人撰写，本文不将其自查登记为独立核验。

## 5. 完整先验覆盖补充的追加核验

源稿随后补入的§2.3也通过检查。以是否落入参与fine bins的指示量$G_p$先分解条件熵，指示量最多付$h(\varepsilon_p)$；good部分可用支持数界，bad部分在有界三系数盒内至多付$3\log(1/p)+c_C$。条件于$C_r$时，每个dyadic粗三系数cube恰有$(r/p)^3$个细children，所以bad rate只付$3\log(r/p)$，不需全局系数范围。由此得到的Full-prior-upper与Full-prior-rate正确。

这项补充没有把“每个参与bin满足floor”偷换为“完整$\nu^\circ$覆盖于参与bins”。只有同一preceding occupation law中的bad轨道incidence质量得到控制时，才能借occupation下界转成完整先验中的$\varepsilon_p$上界；后期稀疏律的小删除量不够。使用最终已删轻incidence的概率轨道边缘并明确$D=G/\alpha$，可避开这个覆盖量词问题。
