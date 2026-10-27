# p-adic 类比可行性：可以移植哪一层，真正缺什么

2026-10-27，R0119，root 整合。当前用户问的是能否借鉴新欧氏局部光滑证明；本轮是有限范围研究，旧欧氏 Kakeya Goal 继续保持用户停止状态，没有新建长期 Goal。

判断：**Fourier 小帽、原生细管、随机符号与对偶这层可以精确移植；产生临界估计的辅助 PDE 核心尚未移植。普通 p-adic Kakeya 本身已有全维解答，不应重新包装成目标。** 这不是所有 p-adic 能量方法都不可能的结论。

## 1. 先排除已经有解的目标

[Arsovski](https://arxiv.org/abs/2108.03750v3) 已证明每个有界 Q_p^n Kakeya 集的 Hausdorff 和 Minkowski 维数均为 n。这里 |p|_p=p^(-1)，线段指 a+Z_p v，||v||_p=1；不是实参数区间。发表版 JAMS 37(2024),69–80 还证明 maximal；作者主页明确提醒 arXiv 与发表版有显著差别。本次实读的是 7 页 arXiv v3，没有下载或逐读 12 页刊本的 maximal 证明。

为避免混版本，我们另从已存 [Dhar 2209.11443v1, Thm 1.6](https://arxiv.org/abs/2209.11443v1) 的整数函数不等式，完整处理其高度常数和计数/概率归一化，得到尺度 δ=p^(-k)、k≥1 时

    ||M_k f||_(L^n(directions))
      ≤4(3k+ceil(log_p(2n))) ||f||_(L^n(Q_p^n))。

M_k 对单位长度、半径 δ 管作归一化平均再取中心上确界。方向采用有限射影类的均匀概率及其逆极限。该 O_(p,n)(k+1) 界包含通常任意 δ^(-ε) 损失的猜想形式，不主张最优 log 幂。推导见[01 §4](01_known_results_and_models.md)，是文献的直接推论，不是本项目新的 Kakeya 结果。有限扩域的满维数字依绝对值归一化改变，不能把所有环境都不加说明写成 n。

正特征 F_q((t)) 也有 Salvatore 的对应结果；其 v3 的 PDF5/8 norm 漏印 n 次幂，按齐次性及实际 layer-cake 论证辨认，不能照抄错误式。有限域 F_q 和有限环 Z/p^kZ 具有不同尺度结构，亦不能互换。

## 2. 一个确实保留的机制

固定奇素数 p，O=Z_p，Haar(O)=1，ψ 为 conductor O 的复值加性 character。对 d≥1、n=d+1 取真正的 Q_p 值曲率多项式 Q(ξ)=Σξ_i²：

    Eg(x,t)=∫_(O^d) g(ξ)ψ(x·ξ+tQ(ξ))dξ， t∈Q_p。

频率小帽 C=ξ0+p^kO^d 在 |t|_p≤p^(2k) 时满足精确式

    E1_C(x,t)=p^(-kd)ψ(x·ξ0+tQ(ξ0))
      ·1_{x+2tξ0∈p^(-k)O^d}。

这由 Haar character 正交性直接得到：二次余项 t p^(2k)Q(z)∈O，character 恒为1。因而小帽恰产生常模细管，不只是欧氏 stationary phase 的比喻。

[04](04_exact_packet_and_conditional_bridge.md) 还证明条件桥：若临界 s=2n/(n−1) 时，对所有 g 有

    ||Eg||_(L^s(p^(-2k)O^n))≤A_k||g||_(L^s(O^d))，

则其指定的单位管方向 chart 满足

    ||M_k f||_(L^n(O^d))≤A_k²||f||_(L^n(O^n))。

所有原管、中心和任意非负权重保留；独立随机的是人工符号。缩放 Jacobian 为 p^(2kn)，与临界 ds=2n 恰好抵消。02/04 已经未参与施工者全文逐式独立复核，见[审查记录](../../../research/reviews/R0119_padic_model_and_packet_review.md)。严格通过的是 04 明定的奇 p、单 chart 版本，不认证 p=2 的调整、一般曲面或全方向最佳常数。

**A_k 的 subpower/poly(k) 界仍是未付输入。** 已有 Kakeya maximal 不能逆推这个 restriction 输入；条件桥不是新的 restriction 证明，也不成为新的重大结果登记。

## 3. 一个不应误选的模型

若直接把欧氏 |ξ| 换成 p-adic max norm，取实时间演化

    U_α(t)=exp(−it||D||_p^α)， α>0， t∈R，

则高频测试族 f_m(x)=ψ(p^(-m)x_1)1_(O^n)(x) 有 Fourier 支持 p^(-m)e1+O^n。整个频率球处于同一 norm 壳，所以

    U_α(t)f_m=exp(−itp^(αm))f_m， |U_α(t)f_m|=1_(O^n)。

对任何固定 1≤r<∞、实时间集合 0<|I|<∞ 及 σ>0，这排除统一估计

    ||U_α(·)f||_(L^r(I×O^n))≤C||J^(-σ)f||_r。

完整量词及计算见[02](02_radial_wave_probe.md)。它只否定该模型在零阶以下的输入节省，不否定欧氏公式本来的非负 Sobolev 阶、所有 p-adic 局部光滑或本页的多项式相位 extension。Kozyrev 的 Vladimirov 特征函数理论早已显示这类谱现象；这里不声称新发现非色散现象。metric 单位“球面” O^n\pO^n 是正 Haar 测度开闭壳，也不是余维一曲率曲面。

## 4. 新辅助 PDE 方法实际缺的接口

对固定 OpenAI 原稿 §§2–6 的结构审查见[03](03_auxiliary_method_transfer.md)，此前欧氏读解见[原稿指南](../../60_external_results/2026_10_local_smoothing/01_reading_guide.md)。困难不是一句“p-adic 没有正性/微分”：复值 Hermitian 正性、Haar 能量和 p-adic 解析微分都存在。

原稿需要同一套对象同时具备：虚平移产生的正 Gaussian；与波系统兼容、逐列散度为零的正张量；具有 rank-one 背景的四元数 Hessian Dirichlet 解；cofactor/边界通量的精确能量抵消；供两个实辅助圆环使用的传播不等式。不能只换名称就得到这些联动身份。

以真实 p-adic 非局部算子 D 的径向积分核为例，普通 Leibniz 法则多一个平方差项；实时间 Schrödinger 演化却仍有质量流：

    ∂_t|u(x)|²+∫J(x,y)dy=0，
    J(x,y)=2c Im(conj(u(x))u(y))||x−y||_p^(-n−α)，
    J(y,x)=−J(x,y)。

在文中明列的 Bruhat–Schwartz、Fourier 支持紧且避开0条件下，积分/微分合法，root 已另核符号和乘积展开。这个两点间的反对称流是可用材料，但尚不提供原证明的局部正半定张量及临界 μ^(n/(n−1)) 能量。这里没有审定由该流推出新的 restriction 定理。

非阿基米德 Monge–Ampère 亦确实有理论：BFJ v1 处理残余特征0的 projective Berkovich 几何；Fang–Gubler–Künnemann 已有假设 resolution/embedded resolution 的混合特征结果。它们不是原稿的 fiber 四元数 Dirichlet 问题；尚需 Haar 密度、边界、参数正则性、rank-one 背景和守恒流之间的相容性。不能声称“有同名方程”就补完方法，也不能声称混合特征理论不存在。

## 5. 真正有依据的后续方向

[Johnsrude 2409.09163v2](https://arxiv.org/abs/2409.09163v2) 已将抛物线 high-low/wave-envelope small-cap decoupling 推广到 char K≠2 的非阿基米德局部域，尺度损失为 polylog，残余特征/扩域次数依赖明确。这是 Fourier 曲率机制可以移植的现成正面先例，方法与本次新增的辅助 PDE 不同。Hickman–Wright 则给多项式图形 restriction 与全部有限商的 uniform restriction 之间的严格对应；只证明一个有限商或允许任意尺度大幂损失不能冒充该统一结论。

若用户继续这一方向，值得先固定一个曲面、维数、指数和素数依赖，比较其已有 restriction/decoupling 界，再尝试构造与 character 相位兼容、能真实产出 A_k 的正能量。第一道门是证明能量 identity/传播估计；不是重复已成立的 cap→tube→maximal 公式，也不是重解已知 p-adic Kakeya。可以考虑实辅助变量或树/有限商 Dirichlet form，但目前只是有明确验收条件的候选，没有被本轮证明可行或不可行。

## 阅读索引与认证范围

1. [01 已知结果、尺度与源公式](01_known_results_and_models.md)。
2. [02 实时间径向单壳压力测试](02_radial_wave_probe.md)。
3. [03 原辅助 PDE 的逐步骤移植审查](03_auxiliary_method_transfer.md)。
4. [04 精确波包与条件桥](04_exact_packet_and_conditional_bridge.md)。

8 篇新 PDF、提取文本及9条新来源元数据均归档于 literature；旧 Dhar 论文沿用不重复下载。源定理、根代理直接归一化推论、两份内部审查通过的自含计算及未付 PDE 输入分别标明。未全篇独证这些高级文献，未重放整套 Lean，也未认证新颖性或外部同行评审。文献详情与实际失败下载见 literature/metadata/R0119_source_check.json；每轮保存和同步不改变这些数学证据边界。
