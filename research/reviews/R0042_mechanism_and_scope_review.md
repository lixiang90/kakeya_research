# R0042：新输入机制、原 law 与下一闭包任务独立审查

2026-10-17，B。实际全文读取 root `R0042_sharp_polynomial_Wolff_original_law_transfer.md` §§1–8、`R0042_macro.md` §§1–8、`R0042_next_actual_section18_PW_class_gate.md` 全文，以及 A `R0042_primary_frontier_and_six_dimensional_status.md` §§1–7。独立打开 BS2609.24135v1 官方 HTML 的 Theorem1、相关完整证明/Props3.1–3.2及 Claim6.1；读取原 WZ §18 到最终(145)，并回核17.1–17.4。自己的宏观稿不计独审。无 Git 操作。

**结论：修后稿在明确范围内通过。** 本轮完成的是具名新定理的有限加权/共同仿射推论、来源量词纠错与真实未付闭包的定位。没有证明五维 κ≤ζ、一般到sticky、Kakeya反例或新的普通高维维数界；不认证新颖性/重大性，未经外部同行评审。

## 1. BS 原输入与微小 λ

官方 Theorem1 允许所有0<λ,δ≤1，确实不保旧 Conjecture1.1.1 中 λ≥δ 的限制。有效 polynomial complexity 常数需要 semialgebraic/#o-minimal 的固定 format；一般 o-minimal 的 C(S)不能改称统一 poly(E)。原 presentation 的系数大小不计 E，仿射 pullback 不因系数1/r大就增加次数。

root采用的 unit-clock graph cylinders 与原§6 Claim6.1 后的实际证明对象一致，方向在固定 bounded chart 仅有固定比较常数。微小 λ 时不能简单删掉 O(δ)端部而说 relative intersection 不变；root明确直接保留 graph-cylinder statement，未用该不合法捷径。相关深层 #o-minimal 工具仍作为具名文献输入，不在本证书重新证明。

## 2. 任意权重、平均 density 与等价排重

root(1) 的代表选择可依赖同一 S 和 threshold s；每个同色 occupied direction bin 只选一个原管，BS仍适用。该 bin 中的全部高threshold权≤α，故 W_s≤min(W,Bs^{-n})。重复 indices、极小权重及任意权跨度均不需 dyadic 分层。

在 a=(B/W)^{1/n}处分裂积分，n>1给 M≤[n/(n−1)]W^{1−1/n}B^{1/n}，确得 root(2) 的 M^n/[αW^{n−1}]，无需额外 log 或 M^{n+1}。B≥W、B=0边界已分别处理。反向用单位权方向分离族，取足够细的固定倍方向bins使每bin至多一个index，即恢复 BS；固定比较只改常数。因此这是 all-subfamily BS 的等价加权扩展，不能登记成新的正幂机制。

restriction 后 α可以保原上界，但 W、M必须取实际保留值；归一化时三者同时除 parent mass。root已明确齐次性。平均 hypothesis经完整 tail积分处理，未被误称逐管 hypothesis。

## 3. 共同 affine/crop 的准确原质量公式

root F 把原共同clock J长度q、横向半径δ变成unit clock、宽δ/r的graph cylinders。共同 shearing 后新 slope=q(a_i−a0)/r；其 boundedness和δ/r≤1是显式输入。对同一个 S' 作一个共同 pullback，原体积为 r^{n−1}q|S'|，新 relative fraction≥λ只保证原 whole-tube fraction≥qλ。

原 ν|I 的未归一化质量p以及概率化的1/p都在式(3)保留，故

    C'=C0 r^{n−1}/(p q^{n−1})，n=5为C0 r⁴/(p q⁴)。

直接平均法用 W=p、M≥p qλ也给同一式，未偷用W=1。whole-clock/p≈r⁴的抵消只在实际验证该质量时成立；AD/truefloor/成功后验均未被直接代成p。短clock的q^{-4}未消失。

测试包含全部新管的 bounded ball，确有新常数不得趋零的必要校准；它限制可同时成立的p/geometry，而非额外免费gain。不同 F_i 对应不同 S_i，不能一份旧PW免合并费用；root也未将 projective/coarse/replacement 包括进式(3)。

## 4. PW与方向 law 的双向排重边界

如果已有all-scale角Frostman4，共同 affine/crop 的新角cap就是 K(r/q)^4 h'^4/p。对新分辨率 h'≥δ/r，旧查询尺度至少δ/q≥δ；大于1时用总质量上界即可。所以同一费用也能从旧角law再调BS，单独这项 inheritance 不构成新机制。原权 Dρ pushforward 的方向bins也只需固定倍扩大；无权coarse计数则还要双边权重比较。

另一方面，PW严格不强迫满维方向law。root平行transverse满网族有 bounded-overlap，均匀whole-tube visit density≤C；任意可测S的平均 intersection≤C|S|，于是 Markov 给 tail≤C|S|/λ≤C|S|/λ^n。方向却集中单点。该校准通过，且明确没有positiveκ，不是高维反例，也不证明任意AD/CW族都满足PW。

因此下一任务不能只给角law换名；必须证明原实际操作或真实增长复杂度处新增了原来没有的信息。

## 5. 实际来源与重要初始范围修正

WZ17.1的 κ 极值类为joint tube-parameter AD/CW及平均shading，不是direction-separated祖先类。18.2起点及其 coarse/parent 两尺度调用确实使用这个类的 K_d；不能给任意Def17.4输出补一个未证祖先。root§6准确保留这一缺口。

本次独审另发现 nextspec 原句可能误将“BS给PW”扩大为“任意满方向网进入jointAD/CW加强类”，已由root实修并读回确认。显式校准：δ=ε²，v=εA+δB、b=εB，A,B逐坐标遍历0,…,ε^{-1}−1。v为完整δ方向网，joint(b,v)却ε-separated，r=ε/10的occupied parameter ball只有一个index，不能满足small-loss的4-AD lower≈δ^{-2}/K。角距离的固定倍可用网格/coloring支付。

修后 nextspec 明确：BS只补PW条件；已有jointAD/CW的方向网才可直接进入加强类；一般Kakeya到此类的归约另欠。root主稿也加入该校准。该例只否一个输入推断，不是Kakeya反例。原全部五维剩余责任未被这一修正掩盖。

## 6. 真实 coarse gate 尚未被假证

原§18的 X' uniformization、无权DρT和(106)–(113)极值递归是必须单列的操作。coarse Tρ与S相交并不保证对应fine tubes与S相交；一般只到N_{Cρ}S，而其体积不必与|S|可比。因此共同fine affine公式不证明完整§18闭包。

nextspec现在明确先测fine-PW加强类，失败不能悄加所有coarse-PW进定义后标通过。它也明确新κPW不能借旧κ替换；原mass、coarse reweight双边比较、clock、复杂度指数与g/h层级都需实际核。闭包即使通过，仍要一个真实半代数S的intersection/volume/complexity预算，而不是将 χ+Aθ+5u<κ设为公设。这是一项具体有界门槛；本review没有把其待证结论预先认证。

## 7. 宏观与前沿范围

A将KT、HRZ、Zahl、GLX表及新四维后果正面对照，且将本轮有限检索与first/best/major认证明确分开。现有 DIM001/R38内部有限—Hausdorff链已付的责任不应重新列未证；外部具名输入、内部逐步审查和外部评价仍分别披露。本文没有重新穷举A全部queries，也不以读到的有限范围认证最新最优。

root macro没有从四维 smooth cap推出五维jointgain，也没有把R41低S设成新输入。full mixed、general-to-sticky/Hausdorff及其它冻结路线保留。下一唯一任务不是自动重开CP/PM、carry、flake或构造常数；若实际闭包失败或只复述角law且无复杂度作用，一轮即停。长期Goal和完成标准不变。

正式全文审查完成。BS本身是文献定理，本轮有限推论已审，实际§18加强类及任何κ gain仍待研究；三种状态不得合并为已解普通高维Kakeya。
