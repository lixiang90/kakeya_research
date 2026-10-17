# R0053 独立全文审查：二次方向几何、近抛物柱面与范围

2026-10-17，审查者 B（`/root/lifting_obstructions`）。结论：下列明确范围内通过内部逐步审查，无尚待修补的数学步骤；条件仍包括具名三维完整 maximal 输入 M3，未经外部同行评审。本审查不将自身分配稿计作独立认证，不认证尚未生成的 metadata、registry、Git 或同步回执。

## 1. 实际全文与命题范围

已实际全文读取 root《R0053_uniform_quadric_transfer_and_maximal_equivalence》最终11节、A《R0053_primary_density_and_closure_audit》最终11节、B独立稿9节、`R0053_macro.md`6节、唯一 next《R0053_next_actual_five_dimensional_coupled_quadrics》6节及 working_spec6节。正式核的是原 R4 unit axes、原非负权及 physical angular cap α、任意可测原 shadings 和平均 λ 的 Q3；并核同轮追加的整轴近 contained 固定柱面 x₄=x₁² 子类。没有把平均变逐管、near-full 换成任意密度，也没有以短 clock 重置题目。

root的 exact 命题只需原轴上 |∇P|≥c，原 spec 的固定邻域 regular 更强；系数和有界域给 tube 内 |P|≤Cδ、|∇P|≥c/2，所用 δ₀ 只依固定 c/geometry。P 可随 δ 退化，最小非零 Hessian 奇异值不进入常数。具名 M3 的原单位圆柱定义、任意 f∈L³/任意小幂损失由 A实际 source 范围承担；本轮未重证来源97页全 proof。

## 2. Exact quadric 的统一方向与物理纤维

逐式核 root §§3–6。精确线条件 P(a)=0、(Aa+b)·v=0、vᵀAv=0正确。h=Av≠0时，有限固定 S³ kernel 网可同时与实际物理 normal 和 h 作相对横截；h⊥v还保证投影方向不短。将 v 正缩放成 w=u+te 后，二次 secant恒等式和同号分母 ≥κ(|Aw|+|Aw′|)给全局 |t−t′|≤κ⁻¹|u−u′|，因而每 projected δ帽的原方向直径 O(δ)、原帽权≤Cα。此论证对任意两点成立，不需要域连通、根分支延拓或除以 |Av| 的绝对下界。

Av=0的全部方向另属于 V=kerA∩b⊥，物理 normal 恒在 V⊥；在 V⊥ 选有限 kernel 网，投影在 V 上等距，处理线性、半定和一般退化核方向。V proper 的理由使用 regular zero axis，未漏奇方向质量。物理事件按同号 ∂eP 分开，任一纤维上两个实际近零点用二次割线给距离 O_c(δ)，所以 f_j=δ⁻¹∫fiber1_Ej 的 L∞ 上界成立。root用实际 tube 点、B用零点 footpoint，两种证明均已支付各自的 O(δ) 厚化，未将不同 chart 的全部 E 免费代入同一纤维界。

## 3. 原 law、任意密度及完整反向闭包

逐式核 root §§6–9/A §§5–8。固定数事件覆盖只要求 ΣI_j≥I，选一组后用 W_j≤W，未把重复 whole-tube 权相加冒作 W。投影单位轴的直管区域及其邻角扰动由固定数单位圆柱覆盖，保全部端帽；并非仅用一个同长旋转圆柱而漏 tiny λ 可集中的端点。原帽积分给 δ²Σw_iβ_i³≤Cα‖K_(Cδ)f_j‖₃³，M3取 loss ε/3，纤维给 ‖f_j‖₃³≤Cδ⁻¹|E_j|。Jensen的精确分母 W_j² 因而得到 δ^(3+ε)λ³W/α，无第二次 heavy 密度损失。

完整双向亦通过：超平面中的三维原 tube/shading 乘 [-δ,δ] 确包含于半径2δ的真4D管；有限 separated level 方向及 packing 将 Q3 变成任意 λ 的 restricted weak L³。对局部 ‖f‖₃=1，低于δ²的部分和高于δ⁻²的 L¹ tail 对 maximal 均为 O(δ²)；中间 J=O(logδ⁻¹)层的 Σ2^(3k)|F_k|≤1，level只损 J³。Hölder cutoff δ^(-2/3)及 layer cake 再损一个 log，任意小幂可吸收。全空间按单位 cubes分输入，一根单位圆柱交 O(1)个 cubes，Kf≤Csup Kf_j 后立方范数求和闭合。故不是仅 restricted 的口头等价：exact Q3⇔M3在任意小幂层面已完整支付，不应新立同义结果ID。

## 4. 新增近 contained 抛物柱面的真实 packet 证明

实际全文核 root §11/A §11/B §9，三份计算一致。整条单位轴距 Z={x₄=x₁²}≤Cδ先给 |P(a+tv)|≤Kδ；t=0,±1/2严格推出 |v₁|²≤8Kδ、|v₄−2a₁v₁|≤2Kδ，继而 drop-x₄投影长度≥1/2。仅有稀疏 marks 近 Z 不足作此前提，三稿均保留整轴假设。

按 midpoint a₁ 以 r=√δ格唯一分原标签，原 W 和 I 都精确分区；整轴x₁漂移O(r)，端帽只多δ≤r，所以各包实际 E_j在原空间重叠 O_C(1)。同包写 u=πv/|πv|、s=v₄/|πv|，有 s=2b_j u₁+O_C(δ)，因为 midpoint误差 r 乘 |u₁|=O(r)。于是 projected δ帽的原方向仍在一个 Cδ帽内，无包数或 δ^(-1/2) 重数费。每包竖直纤维长 O(δ)，单位圆柱覆盖保任意 λ/端点；逐包 M3 后以 ΣI_j³/W_j²≥I³/W²及 Σ|E_j|≤C|E|合并，恰给同 Q3。这里没有把近轴 snap 到原 Z内的 exact line；此前 √δ 方向反校准依然成立。新支付的是空间 packet、原角帽与 actual overlap 的联合费用。

## 5. Macro、后继量词与停止边界

macro准确关闭 exact 等价模型；near-P子类是明确几何应用，不宣一般 R4 nearquadric。下一 spec 的 R5图 Z={(x₁,x₂,x₃,x₁x₂,x₁x₃)}、真实整轴 O(δ)近图、原 S⁴方向帽权、任意平均 λ及目标 δ^(4+ε)λ³W/α具有一致的 tube/fiber维数；两个方程同时生效，不以第二方程 linear 的 flat 子例验收。它没有预认 anisotropic packet、投影 cap、重叠或 original mass 已付，恰将这些列为下一待检步骤；本审查未研究或通过该下一命题。

该共同因子模板不同于已关闭的 exact-quadric 字面重述，但若最终仍只是 M3应用，继续不立新数学ID/major。spec明确模型方向不占满 S⁴，真实 HRZ终点也不强制此图，故不能推出普通 n5>4；成功也冻结模板，不追加更多输出维数，一主轮失败则停止，未复活 CP/PM、BSG、PW或一般→sticky旧冻结路线。当前未见需修改的量纲、闭包或假承诺。

## 6. 正式结论与保留责任

通过 root11/A11 的 exact uniform Q3应用、完整 M3双向闭包以及固定近抛物柱面 Q3证明；通过 macro/next 的范围和一轮停止约束。权重跨度、重复方向/管、δ依赖退化 P、极小 λ、碎 shading和 round endcaps已在实际计算覆盖，无 pending 数学修补。结论条件于具名 M3，不是对其整篇 proof 的外部认证。一般近quadric、growing degree、一般高维原族模型提取及普通 n≥5/full HRZ增益仍未解决，长期 Goal active。完成本文件后停止编辑与检索，由 root统一归档和安全同步。
