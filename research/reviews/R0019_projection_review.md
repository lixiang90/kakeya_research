# R0019 独审：全局残余 shear 的有限投影输入

2026-10-17，`lifting_obstructions`。审查对象：`notes/40_multiscale/sticky_mixed/R0019_global_residual_projection.md`（包括新增第6节）。一手输入核读了本库 `R0014_gan_guo_wang_2211_09508_v2.txt` 的 Theorem 2.1、(2.1)–(2.6) 及曲线定义；另核 `guth_wang_zahl_2026_streamlined_v2.txt` 的 Theorem 1.1、Definitions 3.4–3.5、Lemma 3.7（PDF2、6–7）。没有重证前者的 Fourier/decoupling 证明或后者的完整三维 Kakeya 证明。

**结论：该全局 proper-branch 排除的数学接口通过。** 第1–4节的固定 profile 校准显式条件于 GGW Theorem 2.1；更强第6节对任意有界 global residual beta 的排除显式条件于 GWZ Theorem 1.1、Lemma 3.7。原时间集转成标准 net 的常数界舍入已在 root 第4节落实。本结论不把局部 q 的原质量费用消去，也不以调整函数 h 的二次近似推断 residual beta 为二次函数。

## 1. 原质量与 whole-tube 凸原像

令原管数 N，参与时间数 m(T)。由平均下界、m(T)≤Cδ⁻¹，删除 m(T)<c′δ⁻¹⁺η 的管之后：

    #S≥cδ^ηN；每个 T∈S 保留 ≥c′δ⁻¹⁺η 个原时间。

正规化 Uniform(S) 的凸 Wolff 常数至多从 Cδ⁻η 增为 Cδ⁻²η。这是真实原 restriction 成本，正确。

参数 p=(a3,a4,v3,v4) 的半径 w 球描述整条投影轴与某参考轴在固定完整时钟内相差 O(w)。其五维原像可以取为

    |x3−a3*−tv3*|≤Cw，|x4−a4*−tv4*|≤Cw，
    |x1|,|x2|,|t|≤C。

这是包含完整 δ 管的凸集合，体积 O(w²)；使用 w≥δ 付管半径即可。故原 pushforward ω 满足 ω(B(p,w))≤Cδ⁻²ηw²。该结论不依赖投影线去重，也不需要投影先验独立或 AD。

## 2. 三种 profile 的系数与 Frostman 指数

逐项展开核验如下。

| beta | 系数 C | 相位 | 系数球原像 |
| --- | --- | --- | --- |
| t | (a4,v4−a3,−v3) | C0+tC1+t²C2 | 有界一维 fibre；O(w⁻¹) 个 w 参数球 |
| t² | (a4,v4,−a3,−v3) | C0+tC1+t²C2+t³C3 | 可逆常数界线性变换 |
| t/(1+t) | (a4,a4+v4−a3,v4−v3) | (1+t)[x4(t)−beta(t)x3(t)] | 有界一维 fibre；同一 cover |

所以三维系数概率有原权的一维 Frostman upper Cδ⁻²ηw；四维系数概率甚至有二维 upper Cδ⁻²ηw²。分式线性 profile 在 [0,1] 上乘 1+t，目标 cover 数和 O(δ) 误差都只改变固定常数。三种恒等式无符号问题。

半径 cδ 的平滑在小于 δ 的尺度分别给

    μ̃(B(x,w))≤Cδ⁻²ηδ⁻²w³  (R³)，
    μ̃(B(x,w))≤Cδ⁻²ηδ⁻²w⁴  (R⁴，原 exponent 2)。

与大于 δ 的 upper 合并，对任意固定 0<α<1，全部尺度的 cα(μ̃)≤Cδ⁻Aη。固定对角变换及固定 homothety 只改常数。原文没有把 δ⁻Aη 偷换成统一常数，这一点正确。

## 3. 平滑后的逐点 marks

保留后的每个原管有长参与。一个原系数值的 mollifier 小球内，每点在该原管的所有原 marks 上仍满足固定倍 O(δ) 目标区间，因为相位的系数范数在固定时钟上有界。

相同系数值的不同管可有不同时间集合，但其并集至少包含某一原管的长参与；无需交集或独立性。有限个原系数小球的并为闭集，support 点确实属于至少一个这样的小球。故 GGW 所需每个 support 点的参与下界成立；不是只证明平均或 almost-everywhere 版本。

## 4. GGW 的实际有限输入与指数

GGW Theorem 2.1 使用 α∈(0,m)，这里 m=1，故选 α<1 是正确范围。其 printed normalization 是 Γ=(t,t²/2!,…,tⁿ/n!)，短边平行 span Γ′。相位 (1,t,…,tⁿ⁻¹) 通过固定对角线性变换等价于这个切向族；将测度作逆向配套变换即可调用 printed 定理，不必假定一般 Grassmann family。

在固定有界 support，每个一维目标区间只与 O(1) 个长边为1、短边为δ的标准切向法框相交。选择所有相邻框吸收固定误差，所以

    #W≤Cδ⁻¹ max_t Nδ(Y_t)≤Cδ⁻²⁺κ⁻η。

外部定理给

    #W≥c cα(μ̃)⁻¹ δ⁻¹⁻α⁺L_n√ε。

取 α=1−κ/4，先令 L_n√ε<κ/8，再取 η 小到 Aη<κ/8 且 η<ε/2，可得 lower≥cδ⁻²⁺κ/2。与 upper 的指数差为 κ/2−η>0。固定常数由最后取 δ 小吸收。κ>1 时可先减弱为 κ=1；若目标 cover 上界已经小于1则无 marks，更是直接矛盾。

## 5. 原离散时间到 printed net 的精确处理

GGW (2.4) 对 net 使用特定距离约定，任意 δ-separated 原时间不宜未经说明就称可原样嵌入该字面 net。以下修正只付固定常数，不是新假设。

选覆盖 [-1,1] 的固定规则 δ-net，把每个原时间 t 舍入到距离 O(δ) 的网点 j。原时间 δ-separated，故每个 j 只收到 O(1) 个原时间。对 j 的目标，使用这 O(1) 个原 Y_t 的 cover 的并；分式线性分支使用原 (1+t)Y_t 的并。

对有界系数，q_j(C)−q_t(C)=O(δ)，所以只需固定倍扩大目标区间。每个 support 点的原参与数在舍入后至多除以一个固定常数；每时目标 cover 数至多乘固定常数，故第3、4节的两边指数完全保留。网的其他时刻使用空框族即可。若使用不同固定步长或将全时钟先放到 [-1,1] 的内部，所有尺度也只差固定常数。

这同时避免对原 Y_t 作任何连续时间插值；实际目标集可以任意变化。

## 6. 适用范围与尚未关闭的主接口

这里的凸原像覆盖完整原管，是全局假设直接推出的原概率 cap。若先条件化到质量 p 的局部 q/窗口/normal-form 族，最多保留 Cδ⁻Aη/p 的同类 upper；p≈ρ⁴⁻κ 属固定幂损失，不能作为 δ⁻O(η) 重置。root 稿明确承认这一点。

实际 scalar quadratic 控制的是 h_{z0}=v−b(z0)u；残余 beta 可以仅 dyadic-Lipschitz，并依 δ 变化。当前没有将其全局且以次幂质量成本归入前三个固定 profile 的合法步骤。下节更强的 GWZ 输入消去了 profile 限制，却仍要求一个共同固定核在原工作分辨率消去全部其他水平坐标，且保留原整体概率。它不关闭 N5-MIXED42-Q01，也未提供一般五维/一般维度 Kakeya 结果。

## 7. 新增任意 bounded beta 分支的独审

### 7.1 完整投影管、convex prism 和原权

每条原管先整体投影，再由一条代表管 P_j 包含，保留其 assigned 原权 w_j。可统一取代表轴在 t=0 平面的四个 joint 参数作 δ 网，选择一个固定足够长的线段使它覆盖有界时钟内所有实际投影；最后作一次固定 homothety，变成普通单位长、半径可比 δ 的三维管。这个安排保持 whole-projection containment，而不是把一个原管拆成若干未知比例的 pieces。图参数网格代表至多 Cδ⁻⁴ 个。

若 P_j⊂U，所有 assigned 原管都位于 U 在五维的凸 prism（再与原固定自由坐标盒相交）。其体积≤C|U|。因此即使 U 很薄，也直接有

    Σ_{P_j⊂U} w_j≤Cδ⁻²η|U|。

没有先把 U 膨胀 δ 再错误比较体积；所需 margin 在选 P_j 时已付清。

root 终稿已使用极小权重删剪：先删除 w_j<δ⁵ 的代表，总原质量≤Cδ⁻⁴δ⁵=Cδ；其余权重落在 [δ⁵,1]，仅 O(log(1/δ)) 个 dyadic bins，某 bin 原质量 p≥c/log(1/δ)。bin 内权重在 factor2 内，所以 uniform bin 的 normalized convex Frostman 常数至多 Cδ⁻²η/p，正确。这已消去原管数上界，也允许任意有限正原权及重复索引；不是把任意罕见投影像重新均匀化。

若已有 #T≤δ⁻M，利用非零 w_j≥δ^M 作 dyadic binning 只是一个可选简法，不再是现稿的额外假设。终稿也明确所有原 marks 来自同一个 δ-separated 时间集 Z；下节的时间分层上界按这个共同 Z 计算。

### 7.2 同一原 marks 的 projected shading

每个保留代表只选其 assigned 的一条 good 原管，并使用该管原 marks。不同 δ-separated time 对应的 cδ 小球在三维时空有有界重叠；由于 P_j 的 margin，小球可放在 P_j 内。所以每条代表 shade volume≥cδ⁻¹⁺ηδ³=cδ²⁺η，进而 λ≥cδ^η。

这些小球只触及 O(1) 个邻近时间 cell。固定原时间 t 上，x3 在有界区间，x4=y+beta(t)x3+O(δ)；bounded beta 保证其空间 δ-cover 数≤Cδ⁻¹Nδ(Y_t)。因此所有小球并集体积≤Cδ^{κ−η}。这仅数原离散时间层的邻近 cells，不使用 beta 的时间连续性，也不把任意 Y_t 连续插值。

### 7.3 命名三维定理和 Np 的消去

GWZ Theorem 1.1 给 β_KKT=0 的 KKT 结论（从 volume 表述到 multiplicity 表述用 λ≤1；反向可吸收小密度指数）。Lemma 3.7 在该参数取0时恰给

    multiplicity(P,Y)≤δ⁻ε Δmax(P)。

它不要求 Δmax 已经小。uniform bin 的 normalized convex upper 给

    Δmax(P)≤Cδ⁻Aη Np δ²。

总 shading volume≥cNpδ²⁺η，故 Np 确实消去：

    |U(P,Y)|≥cδ^{ε+(A+1)η}。

取 ε=κ/4，再取 η 小，使 shading density 达到该 lemma 阈值且 (A+1)η<κ/4，lower≥cδ^{κ/2}，与 upper≤Cδ^{κ−η} 冲突。这里既没有假设 Np≈δ⁻²，也没有把 full direction separation 赋给 projected family。命名定理明确允许所用普通有限管集合和 shading。

因此第6节的更强 global proper-branch 结论通过。主 source-local 接口仍是保住原 law、尺度及全部其他分量的误差：osc a≈Kρ²、osc(proj_r b)≈Kρ^{1+cε} 远大于 δ，不能由本全局投影结论自动忽略。该边界在 root 第6.3节已明确列出。
