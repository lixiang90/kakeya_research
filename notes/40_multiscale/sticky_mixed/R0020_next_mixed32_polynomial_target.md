# 下一唯一主任务：N5-MIXED32-Q01 的多项式曲线 tube-KT 机制

2026-10-17，R20 宏观交接。**以下为待证候选，尚无结论。** 先完成 R21 定期宏观审视，再开始这一主任务；不继续 local mixed42/GWZ 的端点 budget。

## 1. 如何接近长期目标

实际 d5 有多个 mixed 配置。选原 Definitions17.2–17.4 的 d=5、k=3、ell=2：horizontal grain 维2，原方向参数 Φ 标量，隐藏薄集 tildeY 在 R²；其维数为 2−κ，且另有 tube Katz–Tao 指数 1−γ。两斜率写成

    f=(u,v), u∈R, v∈R²;
    tildef=(a,b), a∈R², b∈Mat(2,1), v=a+b u.

同样研究 quadratic alternative。与 mixed42 不同，u 和仿射速度 r 都是标量：一旦合法推出 r 非零，收缩 b r 就控制整个 b，不留下正交 row。新增障碍是原22.4的 scalar-Y interval argument 不再适用于二维 tildeY。不能只从维数2−κ声称曲线不可能；改用原 tube-KT 这个真正额外的几何输入。

完整 tube AD/CW、Φ/ξ coherence、原 marks、所有 source 参数次序保留。只证明这一分支也不等于五维 Kakeya；非二次分支、其他 mixed 和 general-to-sticky/Hausdorff 仍开放。

## 2. 首个可证伪的有限命题 PCT

固定 m,D≥1 和 γ∈(0,1)。设 P:[0,1]→R^m 为次数≤D的多项式，振幅 R=diam P([0,1])≤1。B⊂[0,1] 为 d₀-separated 集，#B≥θ/d₀，0<θ≤1；取 e≥d₀R，0<e≤1。Y 在 bounded box 中满足：对任意 e'≥e、长度 L∈[e',1] 的任意方向 tube，

    N_e'(Y∩tube) ≤ K (L/e')^{1−γ}.

假设 P(B)⊂N_eY。待证存在只依赖 D,m 的有限 C，使

    R/e ≤ C (K θ^{-C})^{2/γ}.

固定倍 thickening、L 常数倍大于1、R≈e 或 d₀不够小时的平凡项必须明确处理。不能在 polynomial sublevel 的 bad intervals 中藏入多于 O_D(1) 个离散边界点而不计 θ/d₀。若该精确形式错误，先给严格反例；只允许有实质来源理由的修正，不以自动附加的同义条件救命。

候选证明机制（尚未经逐步审查）：选一个 oscillation≈R 的分量，其导数有宏观 sup；有限次数 sublevel/Remez 给 |P'| 太小的时间集 measure≤C α^{1/(D−1)}，取 α≈θ^{D−1}。在长度 u≈sqrt(e/R) 的时间 bin 内 Taylor 余项 O(e)，曲线落在长度≈sqrt(Re) 的直 tube 中。good derivative 给该 tube 内 N_e(P(B))≥θ^{C}sqrt(R/e)；tube-KT upper 则为 K(R/e)^{(1−γ)/2}。必须严查离散密度、符号区间、同一 bin 的 good mass 和 preimage multiplicity。D=1 单列。该机制利用**实际有限次多项式**，没有将任意 dyadic-Lipschitz source 曲线假设成 C²。

## 3. 实际 source 回传，而非证明一个脱离来源的引理

命名输入：原固定尺度 affine alternative

    u(z)−u(z')=r(z−z')+O(ρ^{1+ε₀})

必须从正确 source 量词取得或明确条件化，不能将 all-scale Lemma21.1 的形式否定当免费输入。对 residual v_{z₀} 的向量 quadratic approximation，误差范式沿原22.4：

    Δ=ρ^ε(ρ²+ρ|A₁|+ρ²|A₂|).

复核实际 V/J/L 计数在 horizontal2、vectorY 中仍保同一个原 graph，固定原 y,z',φ₁,φ₂ 后在密集 z 上有

    y+P(z)∈N_e tildeY_{z''}(q),
    P(z)=(z−z')²[A₁+A₂(z+z'−2z₀)−b(z')r](φ₁−φ₂),
    e=K^Cτρ+δ+ρΔ.

P 是 R² 值 cubic。将 z-window 归一化到[0,1]，d₀=δ/ρ；通过 τ 定义需验证 e≥d₀·osc(P)，不能口头省去。tube-KT 用同一 q 的 tildeY；检查原文 Y/tildeY 命名混用、空间 rescaling 和该层实际 γ。此后才可用 PCT 推向量版 (189)/(190)、稳定细化后的 τ-collapse。每个挑选 z' 的概率及 K 的幂必须保留。

即便 τ-collapse 成功，还要从原 Lemma19.2 全斜率预算与分离 times 推 r 非退化；不能预设 r≠0。r 为标量时再用 E+swap 控制整列 b、consistency 控制 a，按 R19 保守 row 指数而非原PDF99未补证的强化。最后按 Lemma19.4 的真实参数与 retained-time 常数给正 CW gain。任何一个接口未支付，都只归档条件引理，不能声称完整 quadratic 分支。

## 4. 分工、失败条件和宏观约束

Root 负责 PCT 的完整有限证明及与原 polynomial 尺度匹配；审查 A 核实际 mixed32 的 V/J/L、normalization、r 非退化与19.4；反例攻击 B 检验 PCT 在离散稀疏时间、曲率、系数抵消、原 tube-KT 小幂常数下是否错误。最多两个互补代理。

本轮必须得到严格有限证明/反例或一项实际 source 的新明确缺口。单独把 scalar interval 换成 vector norm，复述已知 b r 线性代数，或调整 R20 的 λ/D 端点，均不算结果。若 PCT 只给错误尺度或参数无法支付，立即 macro，不连续两轮在同一个等价修补中迭代。候选的重大性、新颖性与全部 Kakeya 完成标准保持未认证。
