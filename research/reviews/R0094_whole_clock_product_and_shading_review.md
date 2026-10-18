# R0094 正式审查：真实时钟、全方向乘积与谱边界

2026-10-19，B 独立逐步终审（本轮于 2026-10-18 开始）。结论仅限本轮实际资格、已知谱证书及精确接口反攻，未经外部同行评审。

## 1. 实际全文对象、独审分工与来源读域

已 fresh actual 全文读 root 主文 R0094_sharp_Fourier_boundary_and_algorithmic_input_scope 十节，A 的 R0094_primary_frontier_and_original_input_gate 八节，B 的 R0094_complete_routes_and_new_mechanism_countergate 八节，reselection/working 两 spec 各五节，以及终 macro、next、source_scope 各六节。逐式核对 root/A 的证明与适用域，不以本人 B8 自证代替独立审查；本人两端谱证明已有 root/A 另行独核。

采用源的实际读域：FHK 2105.11414v2 官方定义、§2（含 Cor2.4）和 §3 clock 证明；Fraser 2505.09464v1 intro/规范/§2 及 §3.1 对应计算。此轮终审另直接从库存原 PDF 提取并读 PZ 2603.25611v1 物理 6–8 页，Lutz–Lutz 1511.00442v4 物理 6 页的 point-to-set 声明和 10–12 页的平面算法及高维限制。未虚报已独证四稿全部高级 wholeproof、已执行 root 的 PDF 视觉检查，或已重核下载字节/官方核心 wholebytes。

## 2. 单个真实 supported measure 与 endpoint 衰减

root §2 的 witness 关系闭于 compact 球面×K，且每 fiber 非空 compact。对任意开 anchor 集，关系的相应交可作 compact 层的可数并，投影为 F_sigma；因此原 compact-valued 可测选择合法。也可沿 R91 的 universal 选择再取球面完成概率下的 a.e. Borel 版本。坏方向的任意合法补选只影响零测；pushforward 为 Borel 概率，μ(K)=1 加上 K 闭严格给 sptμ⊂K。未把 hull 上概率误说成非 Borel 原 K 上支持。

固定非负内部 smooth φ、积分 1 后，先作完整原单位段的 clock 积分，得到 anchor 相位乘 φ̂(ξ⋅θ)；取模只需原方向的球面概率，不需 anchor 正则性。对 R=|ξ|≥1、M>1，中央带的坐标密度有统一上界，积分 (1+R|u|)^(-M) 为 O(R^-1)；两端部分直接用 O(R^-M)。n=2 的极点密度只在两端发散，后一处理避免了错误的全域有界断言。

故同一个实际原测度满足 |μ̂(ξ)|≤C_n(1+|ξ|)^(-1)，不是仅每个次临界指数另取一个概率。常数依固定 φ/n，不依原 anchor。Riesz 能量在 0<s<2 的无穷远径向积分为 ∫R^(s-3)dR；这给 dim_H≥2 及 dim_F≥2。二维 s=2 的 L2 上界积分仍为对数临界，不能推出正面积。以上正链通过，属于已知 Oberlin/FHK 型方法，不是高维新下界。

## 3. 同一全方向产品、Hausdorff 满维与任意测度上限

令 P 为 compact planar 零面积 Kakeya 集，E=P×[0,1]^(n-2)。root §5 对每单位 θ=(u,w) 的逐方向构造合法：u≠0 时从 P 的 u/|u| 原单位段截取长度 |u| 的子段，按 t∈[0,1] 参数得到 a+tu；u=0 时固定平面点。额外坐标按 w_i 符号选起点，使 b_i+t w_i 全程留在盒内。最终 R^n 段的方向正是 θ、长度正是 1，包含竖直/混合方向，而非只给乘积中明显显示的一小族方向。

该 E compact 且零 n 维 Lebesgue 测度。对 P 上 s<2 能量概率与盒上 q<n-2 能量概率，

\[
|(x,y)|^{-(s+q)}\le |x|^{-s}|y|^{-q}
\]

给乘积 (s+q)-能量有限。令 s↑2、q↑n-2，得 dim_HE=n；B8 的 Frostman×Lebesgue 球质量证法给同一结论。无需假设一般两个粗糙集的 Hausdorff 维数总可直接相加。

对 E 上任意 Borel 概率 ρ，若有某 s>2 衰减，将其投影到前两坐标 P。投影 Fourier 为 ρ̂(ζ,0)，在 R^2 平方可积；有限测度版 Plancherel/分布唯一性给一个 L2 密度。投影既为概率又载于零面积 P，矛盾。因此上限排除的是所有支持概率的 s>2，不只是指定 occupation measure。结合正链，dim_FE=2、dim_HE=n。它是全方向谱 sharpness 校准，不是严格低维 Kakeya 反例，也未构造完整 Def17 临界源。

## 4. 原阴影质量、band 上限与闭包边界

root §8 将原 fat-clock 反攻落在真实圆帽管上，已付正 n 维 Lebesgue 质量：取 closed F⊂[0,1]、|F|≥1/2、空内点，在圆柱主体保 t∈F 的整横截 disk。其体积为 |F|ω_(n-1)δ^(n-1)，除以 roundtube 的 ω_(n-1)δ^(n-1)+ω_nδ^n，充分小 δ 得统一正逐管密度。任何非零连续纵向函数都有一个非空开区间上的非零值，故其 support 不可能包含于 F。这真实反驳逐管正密度免费抽取本证明所需 smooth clock；平均密度更不能恢复逐标签的 clock。未将此扩大为这些阴影不支持任何别的 Fourier 概率。

正球面质量 a 的标签 restriction 可用归一化 σ|Omega/a，但衰减常数相应付 a^-1；一般权重需实际 band 非集中。B8 中 average-to-heavy 的 I/W 账本保留 W' 损失及 log(1/λ)，不将其免费化为所有 original-family uniform 结论。好谱 measure 的存在反向也不控制原 indexed I/所有 shadings 或 finite small shadow。

root §9 的全方向 uniform band 指数上限独核通过：任意方向概率 ν 对 Haar ω 积分，Tonelli 和旋转对称性给

\[
\int\nu\{\theta:|\theta\cdot\omega|\le r\}\,d\sigma(\omega)
=\sigma\{\omega:|\theta_0\cdot\omega|\le r\}\asymp r.
\]

若所有 ω/r 有统一 C r^β 且 β>1，则 r↓0 矛盾。这只限制取 anchor 相位绝对值后的 strip 预算；不否所有相位抵消方法。FHK 的 k-plane 后果需要真正统一尺度 k-ball/规定全部 orientations，原 filledgrain 不自动提供。

## 5. 算法来源的独立检查与精确 proof-step 反攻

Lutz 原 PDF 物理 6 页确为对任意 E 的 min_oracle sup_point 恒等式；不能只固定有利 oracle。物理 10–12 页的 decoder、Claims 与作者高维说明均支持 A/root 的限定判断：一维 clock 控制候选 index 的平面步骤不能无费推广到四维 slope。本文未把这个明确列表成本扩大成所有算法信息方法不可能，也未新独证其全部算法维数基础。

PZ 原 PDF 6–8 页实际列明 compact Z/U/X、joint 有效双 Lipschitz、injective 及 computable with effective modulus；物理 7 页的下界搜索字面枚举

\[
G_s=(Z\cap 2^{-s}\mathbb Z^{n-1})\times(U\cap 2^{-s}\mathbb Z),
\]

随后选其中最近格点并宣称搜索停机。root 的 α=√2/2、Z={(α,0,...,0)}、U=[0,1]、X=Z×U、ψ(z,u)=(z,u) 满足其全部列明假设：L1=L2=1，有效常数；α 为可计算实数，identity/常向量模量有效；injective 且真满像。a(z)=(z,0)、ϕ=e_n 也是要求的 affine-fiber 形式。但 Z 的首坐标不是任意 finite dyadic，故 G_s 对所有 s 为空；nearest point 与停机声称失效。

该反例严格针对字面交集网格步骤。若重写为合法有效 net/近似域搜索，需另证它们的可枚举性与误差恢复；此例不反 Proposition1 的结论，不反整体 Kakeya 猜想，也不以修一个 proper 输入证明替代原 rough geometry。完整 joint-biLip 本身已在其 full-dimensional 参数域保持几何维数，未从 ordinary 或 source 原条件自动产生。

## 6. 必修清单、实际范围和最终判定

**未发现未解决的强制修正项；限定范围全文通过。** 审查对象与节数如第 1 节，包含终 main10/A8/B8、两 spec5、macro6/next6/source6。B8 自证未计作本人的独审次数；其结论与 root/A 独立链相符。本 formal 主核 root/A 的 compact 原支持、单测度 endpoint、product 全方向/全维数/任意测度上限、物理正体积 marks、band Tonelli 和 algorithmic 字面反攻。

真实通过范围是已知谱边界在原 whole-unit-segment 对象上的证明与严格适用域审计。两源谱结论已先文献比对，无 new ID、major、ordinary Hausdorff 改善、fullbranch saving 或低维反例；完整四条主路径和 Goal 保持 active。终 macro/next 没有把谱维数 2 当成 n 维 Hausdorff 输入，也没有据有限搜索认证不存在更强定理；其停止普遍 Salem/band>1/desired joint-biLip 续改的决定与实际证书一致。

标准选择、Plancherel/Riesz/Frostman、经典 planar compact Besicovitch 存在性及来源高级定理仍按具名层次使用，未声称重新独证所有外部 wholeproof。**未经外部同行评审。** 不认证尚未执行的 metadata、Git、验证或 same-SHA 同步；本审完成后停止编辑和检索。
