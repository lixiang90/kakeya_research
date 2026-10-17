# R0054 正式独审：平面重叠、真实原密度及宏观范围

2026-10-17，A。**修后当前结论通过，无 pending 数学项。** 这是一项自含低维闭包应用的内部独立审查，未经外部同行评审；不宣普通五维新界、novelty 或 major，不预认证 metadata／registry／Git。

## 1. 实际阅读全文及结论层次

已实际全文读 root `notes/40_multiscale/R0054_two_branch_planar_closure_and_template_stop.md` **10 节**、B `notes/40_multiscale/R0054_common_factor_ruling_and_counteraudit.md` **8 节**、A 独立审计 **10 节**、`research/reviews/R0054_macro.md` **6 节**、`notes/40_multiscale/R0054_next_general_threefold_nearcontainment_gate.md` **6 节**、working_spec **5 节**；B 最终补入较大 $\delta$、affine 投影和边长 $\delta$ 方格的文字已读回。A 自己的证明不计作独立验证，本 review 另行重算 root／B 的推导。本轮无计算代码或数学实验代 proof。

通过的是原 $Z=(x_1,x_2,x_3,x_1x_2,x_1x_3)$ 的 truly near-contained 整单位轴、可测任意原 shadings、非负原权与 physical $S^4$ cap 输入下的

$$|E|\ge c\lambda^2\delta^4W/[\alpha\log(2/\delta)].$$

所有解析和几何输入在三稿中自含证明，**不需要 M3**，更不依赖未审的 97 页。该结论包含先前 $\delta^{4+\varepsilon}\lambda^3$ 模型目标，但不具有一般五维 Kakeya 强度。

## 2. 原 whole-clock 代数及两支分类

root §2／B §2 的近图→残差合法：在固定有界域内 $P_4=x_4-x_1x_2$、$P_5=x_5-x_1x_3$ 梯度有界，原整轴距 $Z$ 为 $C\delta$ 给全部 $|t|\le1/2$ 的 $|P_j(a+tv)|\le K\delta$。在 $0,\pm1/2$ 比较完整二次式，得 $|v_1v_2|,|v_1v_3|\le K\delta$ 及两个 linear residual 的 $K\delta$ 界，常数不受原族／权／密度影响。

由 bounded midpoint 和两线性残差，$|(v_4,v_5)|\le K|(v_1,v_2,v_3)|+K\delta$；unit norm 迫 projected 三维速度有固定正下界。按 $|v_1|\ge\eta/2$ 唯一归 B，其余归 A，分别推出 $v_2,v_3=O(\delta)$ 或 $v_1=O(\delta)$；没有漏掉需要 dyadic $h$ 的中间层。A 审计用等价的 $|(v_2,v_3)|$ 阈值也完整，常数不同不改变结论。较大 $\delta\ge\delta_0$ 用固定帽覆盖和 $|E|\ge I/W$ 已付清。

A 包按原 $a_1$ 的 $\delta$ 格；B 包按原 $(a_2,a_3)$ 的边长 $\delta$ 方格。全 tube（包括端帽）分别近同一二维 affine plane／一维 affine line，相关坐标只漂移 $O(\delta)$，所以包的 actual $E_b$ 有固定空间重叠。不是把不同几何包数当常数；每个原 label 恰进一包，$\sum I_b$ 和 $\sum W_b$ 为原分支的精确量。

## 3. 真方向帽、antipodal 及自含平面 $L^2$

root §3／B §3 在 $V_b$ 正交投影的 unit 方向 $u_i$ 满足 $|v_i-u_i|=O(\delta)$；A 的纯 $(x_2,x_3)$ 投影及显式归一化也独立给同 cap。每个 projected $C\delta$ 帽的原方向预像在一个固定倍 $\delta$ 的 physical 帽内，可用固定个原帽覆盖，故总原权 $\le C\alpha$。无向 projective 角必须同时计 $u_i$、$-u_i$ 两帽；root／B 均已付该常数，重复方向没有被非法去重。

投影整管及端帽被长≤2、宽 $C\delta$ 的 rectangle／capsule 包围。交集面积由单包面积 $C\delta$ 和无限 strips 的 $C\delta^2/\sin\theta$ 两界给 $C\delta^2/(\delta+\theta)$。在 $\theta\asymp2^k\delta$ 的一维角环，原权最多 $C\alpha2^k$，故每层 row contribution 至多 $C\alpha\delta$，低角层和 diagonal 项同样成立。求和确为

$$\|F_b\|_2^2\le C\alpha\delta W_b\log(2/\delta).$$

这个式子对任意非负原权、重合位置／方向都成立，没有隐藏最大权或等权假设；其 log 来自实际角环数而非原族大小。

## 4. normal 纤维、Cauchy–Schwarz 和平均／逐管闭包

root §5／B §4 使用 affine plane 的正交 splitting，Jacobian 一；A 使用纯坐标纤维也恰为一，未混淆这两个参数化。每个 $E_b$ 的三维 normal fiber 在 $C\delta$ 球内，所以 $f_b=\delta^{-3}\int1_{E_b}$ 有 $\|f_b\|_2^2\le C\delta^{-3}|E_b|$。真实 $\pi Y_i\subset D_i$ 和 $E_b\supset Y_i$ 给 $\int f_bF_b\ge\delta^{-3}I_b$。CS 后的维数因子重算为

$$|E_b|\ge c I_b^2/[\alpha\delta^4W_b\log(2/\delta)],$$

不是 $\delta^3$ 或漏一份密度。A 包有界空间重叠，$\sum I_b^2/W_b\ge I_A^2/W_A$，而 $W_A\le W$。B 包所有方向在 $\pm d_b$ 的固定倍 $\delta$ 帽中，故 $W_b\le C\alpha$；点态 $\sum_iw_i1_{Y_i}\le W_b1_{E_b}$ 及空间重叠给 $|E_B|\ge cI_B/\alpha$。选 $I_A$ 或 $I_B\ge I/2$，代原 $I\asymp\lambda\delta^4W$ 即得目标，无需任何分支保固定比例 $W$，亦不额外 heavy 到逐管密度。

一处范围文字已由 root／B 独立指出、A §8 实修后读回：本轮只是整 label 唯一分区且完整保留 $Y_i$，所以若原逐管密度至少 $\lambda_*$，分支／包中的每条余管仍保原逐管下界。只有另作 shading 缩小时才不自动保该条件。对任意重新删选的平均版本须用新的 $I',W',\lambda'$；若 $I'\ge\theta I$，$I'^2/W'\ge\theta^2I^2/W$ 是精确回传。全 proof 对 $\lambda\ll\delta$、碎 shading、仅端帽有质量或极不等权均不要求额外正则性。

## 5. 平面反向闭包、密度反攻和模型停止

root §8 的反向平面 embedding 已核：在 $x_1=x_4=x_5=0$ 取任意有界二维管／shadings，乘三维 $c\delta$ normal ball，放进固定放大半径的真实五维管；union 和 tube volume 都多 $\asymp\delta^3$，平均密度、原帽权和原时钟仅差常数。因此当前对象实质含平面 $\lambda^2/\log$ 估计，正向证明又只用了这些低维事实，不称新的五维 maximal 机制。

$p<2$ 校准全条件合法：在该 exact 平面叶片取 $\delta$ separated 方向，$W/\alpha\asymp\delta^{-1}$，原单位轴相交，取共同长 $\tau\ge\delta$ 的真实 tube 子集。round tube 体积 $\omega_4\delta^4+\omega_5\delta^5$ 给原平均 $\lambda\asymp\tau$，且 actual union $\le C\tau^2\delta^3$。以 $\tau=\delta^a$、$\varepsilon<a(2-p)$，即使允许 $\delta^\varepsilon$ 和 log 损失也与 $\lambda^p$ 改进矛盾。此只校准密度指数；未证明 log 必需，也不是满 $S^4$ Kakeya 反例。

因此本轮不新立数学 ID／priority／major，整个 common-factor 输出模板按 macro 冻结，不以更多输出／ambient／rank 变体续轮。M3、原四维全 source 与其他高级 wholeproof 的旧状态并未被错误升级。

## 6. 宏观、下一 G3 全类门槛及最终 scope

macro 的三路线比较与 next 的量词已全文核：G3 是固定 format／degree≤D、real dimension≤3 的任意 $\mathbb R^5$ 代数集，允许奇点和 $\delta$ 依赖系数，保 whole-unit-axis 距离、physical $S^4$ 原帽、任意权与平均密度，目标 $\delta^{4+\varepsilon}\lambda^3W/\alpha$。它在文稿中是**尚未证也未否**的全类任务；没有用当前特殊图、R53 exact regular quadric 或近抛物柱面结果替代全部原选择。

现有台账中没有已付的全称 G3 闭包：finite seed／DIR 保 near-full 量词，PW 计数与有复杂度费用的集合估计不能免费给任意可测原 $Y_i$ 的 cubic 密度，CP／mixed／sticky 特定来源也没有此一般嵌入。这不证明现有一手文献无此定理；next 正确要求开轮先有界 primary 排重，若只是已知一般转移则实际调用后停止，不声明新颖性。flat 三维平面反向包含 M3 不等于一般 near-singular-variety 的正向转移已付。

本轮另实际重读库内 HRZ v1 extracted 1016–1056：Def5.2 的原对象是 transverse complete intersection，切向条件给 (29) $T\cap B(x_0,2r)\subset N_{4\delta}Z$，Lemma5.3 另有尺度条件且 dim≤$k-1$ 时 broad vanishes。next 留出的真实轴片／球边端点、$h=\delta/r$ 下原 $\alpha_h$、entry 和 marks 责任没有被免费删掉；macro 明写 $k=4,m=3$ vanishing，因此没有声称局部 G3 可直接带来全 HRZ／H5 gain。此 review 不预证 G3，不在本轮开展它。

综上，root10／B8 的当前自含闭包定理与修后 A10、macro6／next6 的范围通过。当前原高维 Goal 仍 active，未达到最终完成标准；元数据、验证器、registry 和安全 Git 同步由 root 后续独立整合。本人两 assigned 文件至此终稿，停止编辑／检索，无 Git。未经外部同行评审。
