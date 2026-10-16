# 下一唯一主任务：支付固定尺度 affine alternative 的实际来源

2026-10-17，R21交接，仍服务 N5-MIXED32-Q01。PCT 已有修正版有限证明，实际 quadratic→全 tildef慢变→19.4已有明确条件链。下一轮不再改多项式常数或重复 E+swap；只攻尚未支付的固定尺度全局 affine/nondegeneracy 准备。所有旧冻结仍有效。

## 1. 精确待证目标 LOCAL-AFF

在原 Definitions17.2–17.4 的 d5/k3/ell2 配置中，κ>ζ，C_CW≤δ⁻η；固定 allowed ρ∈[δ^{1/4},δ^µ] 与ε₀小。对每个原ρ-window J 定义

    M_J=max_{R,U∈R³} #{z∈Z∩J: |f(z)−Rz−U|≤ρ^{1+ε₀}}.

欲从实际原数据证明：对于足够小的 θ_aff（并按原参数次序取η），要么κ≤ζ，要么

    Σ_J M_J≥δ^{θ_aff}|Z|.

这才能选全局 dense 原times、每window一个全 f affine fit；不能从印刷 Lemma21.1 的 all-scale nonconcentration 的形式否定得到它。随后按原19.2/CW支付删除全速度过小的 windows，保全局dense且 |R_J|≥δ^{Cθ_aff}。这一步仍不预设首坐标r非零；r下界由R21后段推出。

## 2. 实际 source 的新可检验机制

源 proof21.1（PDF92–93，文本4844–4916）看上去固定一个ρ运行 W图、(170)–(173)、scalar ABC Theorem21.2，但印刷声明的量词更强。应逐行提取其真正尺度依赖，补好原time删选/coarse权重和通用二维投影的费用，不只宣称“同一证明”。

可优先测试**保留时间坐标的 scalarization**：B={(t,F(t))}⊂R×R³，A={(x,ξ)}⊂R×R³（源observed graph），用同一个固定线性映射

    Π_λ(x,ξ)=(x,λ·ξ).

这样 B 的time坐标和 A 的observable x不丢失。若原 ξ coherence 真给每个 coarse x只有K个A-cells，Π_λ 的A-cover就可直接控制，不需未经支付的任意集合 generic projection。须从原 A 的定义证明此 fibre cap，不能只凭“graph”词语重置。

B 的 vector affine nonconcentration 是否推出某 λ 的 scalar tube nonconcentration，是新的有限可证伪门槛。候选方法是三时刻残差：固定分离 t₁,t₂，第三个 t₃的 vector residual 若小就接近原 affine fit；若 residual 大，随机 λ 使其scalar值小的概率受 anti-concentration 控制。scalar投影有rich tube时同tube内有大量原 triples；以此控制所有可能rich tubes，而不对无限条拟合线粗作无费用union bound。所有gap删除、ρ-net合并、原coupled graph mass、projection条件数和两端指数必须保留。

这只是待证机制，不是R21结果。它不要求 B 是任意 projection family的全维联合图，也不重开冻结的CP/PM、generic免费加维或W独立化。这里的对象、source观察量和scalar ABC输入不同。

## 3. 合法 restriction 的先决核验

删原times时 T不改，各 E_z/Φ_p不改，但 Def17.2(3)要求coarse跨时间Y-union AD，不能仅查逐层cardinality。应核：原whole-window union upper支配子并；非空子并含某个原AD的Y_z是否足以给其每个coarse点的lower及总量，常数多付几次K；原allowed-scale格变更是否要相邻scale取整。保 tildeY tube-KT upper、ξ/Φ coherence和原witness，不生成独立shading。若某项不闭合，应给严格interface反例或新提取估计，不假定完整新配置。

## 4. 分工和停止条件

Root核 LOCAL-AFF 的固定尺度 proof与time restriction；A独审原A/B观察图、权重和ABC量词；B反例攻击time-preserving scalarization/triple机制。最多两个互补代理。一轮必须产出真实source准备定理、严格反例或实质新缺口；仅重写R21条件或重复印刷all-scale否定不算进展。

若这个门槛成功，才能更新mixed32 quadratic conditional结果的责任清单；还需非二次和其他分支，不可直接声称五维/general Kakeya。若失败，立即macro决定去向，不连续在相同projection阈值中改名。长期Goal完成标准不变。
