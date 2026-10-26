# R0115 working：完整 source 的标量上界资格与原质量量词

2026-10-26，root。已运行恢复脚本，实读 GOAL、STATE、ROADMAP、registry 最近项、R0114 本轮/后继稿及 WZ Def17.2–17.4、Lemma19.2/19.4 原文。本轮不续整格筛法、三角参数或旧 vector cap；先决定 R0114 强标尺是否具有独立的局部数学内容。

## 原对象与当前缺口

固定 d=5、k=ℓ=3、κ=1、γ>0，δ 足够小，K=δ^{-O(η)}。T 为原 joint 4-AD δ 管族且 whole-axis C_CW≤δ^{-η}。采用原文(19)/Def3.9 的 usual 管规范：bounded slope、clock u∈[−1,1] 的同一段直线厚管；该源规范没有要求每段 arclength 恰为 1，不为资格审查附加此要求。Z 为原 δ-separated clock，#Z≥δ^{η-1}；共享 F_t∈Mat(2,2) 满足原 allowed-scale dyadic Lipschitz。每个 t 的 Y_t 为 native 1-AD/tube-KT(1−γ)，且每个 allowed clock interval 的 Y-union 在其尺度仍 1-AD。每 y∈Y_t 有 filled X_{y,t}⊂R²、#X≥δ^{η-2}；p=(x,y+F_tx,t) 配 Φ_p 的 1-AD/slab-γ 和 ξ_p∈R²，原同 T 的斜率为 (φ,ξ_p+F_tφ)+O(δ)，满足原所有 allowed coarse Φ/ξ coherence。slice 的 #E_t≈_Kδ^{-3}，跨约 δ^{-1} clocks 的整 E≈_Kδ^{-4}，二者不得混淆。

原 visits 图 Γ={(p,T):T 是 p 的一个原 witness}，总质量 I=#Γ（体积版乘 δ⁵）。原定义只推出全局平均 I/(N#Z)≥δ^{O(η)}；不得赠每 T 在许多 clocks 的下界，或赠任意删选后 filled X 和 Φ 下界。

## 待资格审查的精确强标尺

给定 γ，是否存在 a,τ>0、C<∞、η₀>0，使所有 η<η₀、足够小 δ 的上述完整原对象，对所有原 (t,y)、所有固定 ν∈S¹、b∈R 和 allowed ρ∈[δ^a,ρ₀] 满足

    #{x∈X_{y,t}: |ν·ξ_{x,y,t}−b|≤ρ} ≤ K^C ρ^τ #X_{y,t} ?

ν 在同 grain 内必须固定，不能按 x、φ 优选。此式尚未证明、未锁为正确或足以给高维 gain。若已付原 vector cap β≤K^Cρ 或旧全称命题合法重调用即给，拒改名。若它本身按存在小 η 的量词排除所有完整 source，也不得声成独立的便宜局部输入。

## 本轮两出口与独立反攻

出口 A：从任意假想完整 source，严格构造保持共享 F、合法原 clock restriction、所有 Y-union AD、filled X、Φ/ξ coherence、T 4-AD/CW 的有限常数 graft，仅在一个 clock 加入 R0114 的真实 scalar-atomic dust。逐项给实际坐标、tube 规范、allowed scales、宏观分离和常数账；若可避免仿射 rescale，应优先保持 δ 及原 T。若成功，只得条件地说明强∀grain cap 已承担相应 source 不存在的排除责任；不声无条件 full source 存在、Kakeya 反例或加权 good-grain 版本被否。

出口 B：若 A 的某一原条件实质阻断，写首个无法支付的条件和实际计算；不以“联合输入仍缺”结束。针对该条件推导实际原 Γ 质量约束，或给精确的原质量加权替代表述和双向强度；纯 endpoint phase 的双向代数只计排重，不当新机制。

独立测试：ξ coarse 是 O(ρ) 的几何一致性，不能以 K 大吞 fixed jump；Φ_p coarse 容器须真的存在；graft 若只证各 t 的 Y-AD 而未证所有 clock intervals 的 union-AD，不成立。凸 U 包含整管的 CW 与点访问占用分开。固定量的 affine rescale 必须核 δ、box、allowed-scale 常数是否仍合法。heavy tube pruning 只保原平均质量时，不得免费保 source 下界。

## 闭包及停止条件

显式核 restriction 的两向：保 q 原标签和 p 原 I 时 λ'=(p/q)λ，归一化 cap 除 q；point/visits、全局/grain 分母分别写。单层污染只占约 (#Z)^{-1} 原 clock，因而不能由全局平均简单排每 grain，也不能推出承载原 I 的 good grains 无 cap。

完成上述 source-exact 资格证明或反攻、独立逐步审查、原量词恢复后结束本轮；没有 ordinary/full-source 正 gain 不完成 Goal。每三轮的下一宏观不晚 R0117，连续两轮无信息提前。本轮成果不新登记正下界 ID；更新状态、归档并通过 10808 代理非 force 同步及 full-tree 校验。
