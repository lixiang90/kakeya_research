# R0005主代理独立复核：原生逆映射、KT对照与条件范围

日期：2026-10-16。审查者root。已完整读取两个不同子代理的R0005_native_coefficient_inverse.md与R0005_KT_and_geometric_budget.md，逐项核验下述构造。未经外部同行评审，不声称新颖性或重大结果。

## 1. d<1逆模型：通过

P_*=w−StY3、V3=−e2/S、W=Sy03+e1、w0=c给X=c+e1t+e2t²。8参数到full coefficient map的Jacobian=-1/S，逆可直接解出e1,e2,c；有限Cantor平滑与盒噪声给完整半代数分段常密度。

有限预备网格上，仅在c变量删轻，独立的y0、V1,V2保持不变。因e1/e2在单个正p-bin、V3在单个负p-bin，ν°(Bp)=p³π(Vp)λ°(cp)准确。fixed exact base上，w=StY3+c+O(η)，大平移不改变Cantor区间上界及占据箱数，实际典型隐藏密度为p^d。边界层和低三角形base密度可作power-small例外；不得把此有限表结论升级为一个固定模型任意细尺度的统一估计。

在最细参与Bp内，y03仍均匀于完整p-cell，与e1独立，故W_p每原子≤1/S；L-list成功≤L/S，H(Wp|Bp)≥logS。反向用y03精度p/S足够。这个熵损失是实际条件律的损失，不只是系数幅度换底。

exact current Y3则能恢复W至O(η)：W=SY3+e1+t e2。故不能将这个反例说成加入exact point/history后仍无W列表；遗漏的point互信息恰可达logS。

H=0由直接unit-time trueatlas证明：original prior保持概率，c-core是trajectory-level assignment/selection；每保留c-bin质量≥τp^d、q=1、J固定、test=P_*−c_center全时拟合O(p)，标签由exact base及hidden p-bin恢复至常数列表。它并非从d<1推测H值。full-slope密度约η^-1，未保留最初全部方向来源，也不是positive-horizon或critical模型。

## 2. bounded-W质量界：通过，另有独立代理复核

沿线展开双线性剪切，x1=αW−β(y3−y1V2−y2V1)。固定速度p-bin和前两位置cells，允许y3长度≤C_R[p+(|α|Mw+Mx)/|β|]。按同prior affine cap逐箱求和，给目标质量≤C_R A_aff[p+(|α|Mw+Mx)/|β|]，0<p≤1。

这是几何质量约束，但只覆盖所列特殊原生式。隐藏缩放和父test更换后，必须重新计算整个tuple；不能沿用初始raw W范围。另审见R0005_native_mass_review.md。

## 3. KT对照与partial-input模型：通过，范围保留

KT2001 §3–4、§6的原稿确实使用额外跨轨道纤维重合、方向差单射与hairbrush几何；两个时刻恢复(y0,V)本身只给基本两投影指数，不能据此宣称复现其改进。

互补模型P_*=w−ty1、w0=c、W=y01+c+ζ给原生C=(c,c+ζ,−V1)。同一个有限Cantor+噪声prior可有完整斜率密度≤1、参数箱形式指数d=1/2、mixed cap及constant point/velocity coefficient lists。两时刻给定(y0,V)只重复同一Cantor c信息。

关键边界已核：t有固定正下界时，连续V1在给定visible base后使X扫过固定区间，physical support有正满维体积，真实观测profile为d=1。参数箱中的d=1/2不能冒充source C(d<1)指数。因此它只说明参数熵/两时刻代数输入不足，不能反驳完整物理小支撑约束。

## 4. 精确计算证据及完成边界

native_entropy_probe.py已通过：full coefficient Jacobian、原生多项式、exact-point逆关系、双线性一次项公式，以及缺少mixed cap时的finite-bin counterexample质量与transfer计数。脚本只覆盖这些恒等式与有限计数，连续概率、profile及Hausdorff结论由上面的证明范围决定。

ENT-002的有限离散熵率另由R0005_entropy_rate_review.md独审通过。没有新的Kakeya维数下界，没有真实反例，没有达到长期Goal完成标准。
