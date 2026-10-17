# R0052 唯一后继：新三维任意密度输入的真实四维 quadric 检验

> **R0053当前范围更新：** exact regular quadric Q3已完整转移且与具名3D M3任意小幂等价，不另立新ID，停止该exact模型迭代。同轮真实near-contained抛物柱面已另用空间packet/原cap/Hölder闭合；并非Oδ snap。当前唯一后继为 notes/40_multiscale/R0053_next_actual_five_dimensional_coupled_quadrics.md，下文是R52历史计划。

2026-10-17，Goal active。目标仍是 n≥5/general；本 spec 不把模型成立当作最终完成。R46 加权算术候选已否定，不调 q/权重/更多 slopes。下轮先 context/GOAL/STATE/ROADMAP/registry/最近轮次及回执恢复。

## 1. 为什么是新机制，先核是否重复

新具名输入为官方 3D full maximal Theorem1.1：每 ε>0 有 L³→L³ 的 δ^(−ε) 估计；其任意平均密度的加权角 cap 推论为 |E|≳δε λ³δ²W/α，见 R51 root/A 实证推导。97 页全 proof 未独证，调用须保此外部责任。

旧 DIR/FSD 的 nearfull λ≥δ^η(ε) 与两个 λ 的种子不能直接给任意 λ。下轮首先完整检查：restriction/shading/rescaling 的合法闭包、平均/逐管分别；是否旧全称 CP/PM 或 R50 lift 在统一量词下可再次调用并推出本候选；双向若只有已知正幂等价则不新开方向。一般四维族没有已知保原方向与质量的 quadric 嵌入，不预先假定非等价或强转移。

## 2. 明确模型命题与全部量词

固定 c>0、固定允许的管厚常数。P 为 R4 中次数≤2、系数绝对值≤1 的非零实多项式；考虑位于 B(0,10) 的单位线段 ℓ_T⊂{P=0}，并在这些线段固定邻域内满足 |∇P|≥c。T 为对应半径 δ 的真正四维管，所有线段长度固定为1，不把曲线弧称直线。常数可依赖 c、ε 和固定 chart，但不依赖 δ、P、族数或 λ。

对每个有限这样的族取原非负权 w_T。原 physical directions 每个半径 Cδ 的 S³ angular bin 的总权≤α，W=∑w_T>0。可测 shading Y(T)⊂T，E=∪Y(T)，加权平均相对体积 λ=(∑w_T |Y(T)|)/(∑w_T |T|)∈(0,1]。候选为每 ε>0，在小 δ 时

    |E| ≥ c_(ε,c) δ^ε λ³ δ³ W/α.                    (Q3)

归一化 tube 常数必须支付；若用时间 marks 代体积，要证明其 δ-cell 对应。平均密度是本命题输入，不先换逐管相等密度。仅 regular quadric patch，不含梯度可趋零的奇点；此排除是模型假设，不能在全高维应用中免费删除奇点。

## 3. 首轮必须实际施工的几何

先完成超平面子例，把空间层的 Fubini、端点、原权 bin cap 和平均 λ 的 Jensen 全部写出，确认 exponent/δ³ 正确。随后处理至少一种真正非平面二次模型，而不只写“局部近似平面”。首选 P=x4−x1x2 以及 rank-one cone P=x1x4−x2x3 的 regular patch；必要时用其 rescaled 版本满足系数假设。

精确列出整段直线包含于 P=0 的条件 P(a)=0、∇P(a)·v=0、vᵀ Hess(P)v=0，并分类实际 line family。每一个投影/坐标变换均计算真实方向变化、同 bin 重数、Jacobian、tube 形状与原 shading 的对应；不能把 body/参数方向当 physical direction。只有在已核 phase/curvature 条件下调用 3D companion §11，不能只凭 smooth 就套用。

一个明确可反攻的尝试：记 Q 为二次齐次部分，非奇 direction cone 的 normal 为 Hess(P)v。选投影 kernel 同时横截物理 normal 与该 direction normal，尝试有限 chart/固定分段。物理横截若给 E 沿 kernel 的总纤维长度 O_c(δ)，令 f=δ^−1∫_kernel 1_E，则 f≤C_c，投影 tube 对 f 的平均保原 λ；若方向 chart 还保 bin cap，3D L³ 可转回 (Q3)。这只是拟证明机制：两 normal 的同时横截、全部方向 chart 的统一常数、Qv=0 奇 direction、原 shading 和分段损失都未付，不能把它写成已证模型。

## 4. 独立反例、误差与高维桥

独立攻击：单平面 bush 的共同短 clock、极不均匀权与 shadings、不同平面/叶片重叠、cone approaching singular set（明确是否离开固定 c 假设）、basepoint 依赖投影导致方向纤维爆炸。有限计算只核明确的代数分类或证书，不替 union 估计。

即使 (Q3) 成立，R5/R4 实际 polynomial tangency 只是在 variety 邻域的近切管，未必 exact contained lines；其 degree、regularity、shortclock、局部 anisotropic rescaling 和原质量都要另付。因此本轮只能把可调用的严格模型输入或具体反例存档，不宣 full HRZ、4D maximal 或 n5>4 已由它推出。若有真正进一步桥，须写完整量词再独审。

## 5. 停止和验收

一主轮停止。验收可为：(i) 完整证明 (Q3) 在明确非平面类的成立，并指出全命题未付部分；(ii) 对 (Q3) 本身的合法严格反例；(iii) 经过精确 line classification 和原质量/角 cap 计算定位的新硬障碍。只有超平面现成推论或改名旧闭包没有新信息，不允许再续 degree/regularity/λ 阈值小改。

不得因模型容易而缩小长期 Goal。新 ID 仅在非等价且完整独审的命题需要时登记，重大性先一手文献比对；所有未审来源输入和模型假设均保留。若旧冻结适用就停止，不另命名重启。

## 6. 分工、归档和同步

root 主几何/平均密度及整合；至多两个互补代理，一个核一手 3D 输入与闭包/等价，一个独立 quadric 反例与方向计数。代理只改分配文件，root 统一 metadata/registry/Git。结果进入 notes/40_multiscale 相应多级目录，原来源进入 literature。每轮写 working_spec、round/macro/next、更新 STATE/路线，相关验证后安全同步现有 main，禁止 force；长期 Goal 保持 active，未经外部同行评审。
