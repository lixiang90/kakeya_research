# R0017：向量攻击与原 W 数据的交叉审查

2026-10-17。审查对象为 R0017_vector_counterattack.md 与 R0017_original_W_reset.md。本文不独审本审者所著 R0017_joint_expansion_attempt.md；该稿另由 root / B 核查。

**最终结论：两稿按其“攻击边界＋源审计／路线决定”的范围通过，可归档；没有必须修改项。** 没有因此验证或否定完整 finite strengthening、Mat(2,2) source 非线性结论或 Kakeya 猜想。Y-only BSG/cycle 局部迭代冻结，下一实际 W 机制须取得新增长，不能只重复已知恒等式。

## 1. 原 W 恒等式与真实额外数据

回查 WZ arXiv:2609.22035v1 §19.1、PDF pp77–78、抽取文件 4049–4118 行。原 W-tuples 两条两边路径共有起点、三个时间层及最终 ρ-close 的两根实际管方向。对其实际终端点，(148)–(152) 的符号和 block 维数均与 root 稿一致：

    Δx''=(z'−z)(φ₂−φ₁)+O(ρ²+δ),
    Δξ''=(f(z)−f(z'))(φ₂−φ₁)
                  +O(ρ||f(z'')−f(z')||+δ).

因此 d5/ℓ3 的系数为竖直堆叠的 4×2 矩阵，而非一个标量 multiplier。ρ-allowed Lipschitz 给误差 O(ρ²+δ)；root 使用 δ^(−O(η))ρ² 的更宽记法也合法。两终端 y 标签由 (152) 仅知 O(ρ²) 接近，不能免费改成同一个精确 grain。

实际同一点 p 上的 ξ 标签及其沿原管的 cocycle 在 Y-only finite graph 中已被积分掉；root 因此返回更完整的来源数据，判断正确。这里没有证明两个尚未解决的目标严格逻辑不等价，也没有从这些恒等式本身推出增长。W-path 总数下界不等于选中一个固定 endpoint grain 后的无权 dense graph；稿件把后者留作新接口，未偷换。

## 2. 固定完整 grain 的 R4 图 cover / Frostman

对固定原 (y,z)，x↦p=(x,y+f(z)x,z) 是有固定 bi-Lipschitz 常数的线性图参数化。E 的 δ-separation 因而给原 x 的 O(1) δ-cell multiplicity；没有由 arbitrary source clipping 取得新 lower density。

对于 source-allowed σ，x-domain 至多 Cσ⁻² 个 dyadic σ-cells；每个 cell 的 p 图只遇 O(1) 个物理 σ-cubes。Definition17.2(4) 在每个物理 cube 控制其中所有实际 ξ 到一个 O(σ) box，故 R4 中 (x,ξ) 图的 cover upper 为 Cσ⁻²。这个证明逐 cube 操作，不需要穿过 dyadic 边界的全局 Lipschitz extension。

反向，一个 R4 σ-ball 的 preimage 的 x 都在一个平面 O(σ)-ball 内，最多 C(σ/δ)² 个原 x。用 #X≥δ^ηδ⁻² 得

    cδ^ησ⁻²≤N_σ(A_yz)≤Cσ⁻²,
    μ_yz(B_σ)≤Cδ⁻ησ².

这验证 root 的 full-grain cover 与 uniform original x-counting 概率的 2-Frostman upper。它不是每个 graph patch 的 lower AD，不控制整个 z-slice 的联合图权，更没有把 W multiplicity 先验换成 μ_yz。root 对这些边界全部写明，故通过。

若要把该断言用于非 admissible σ，须另付相邻 source scale 的 δ^(−O(η)) 误差；当前稿只声明 source-allowed σ，所以没有缺漏这一量词。

## 3. Theorem21.2 的标量 multiplier 门槛

回查 source PDF pp91–92，抽取文件 4780–4786、4840–4842 行。Theorem21.2 允许向量输出 a,b∈R²，但其 C⊂R 仍为**标量**集合，平移是 a+cb；Remark21.3 只提高 A,B 的 ambient 输出维数，仍不改变 C 的标量性质。

d5/ℓ3 的原 W 表达式是 4×2 矩阵作用在二维 φ 差上。一般投影 π:R4→R2 得 πM_(z,z')ψ；它不会把所有 times/ψ 同时变成一个固定向量 b 乘标量 c。固定 grain 的二维图之泛型二维投影也可以已经二维，不能套用维数一 B 的 source 输入。root 没有借 ambient-dimension 符号误调用 Theorem21.2，此项通过。

新源-W 任务仍须有真实 joint graph 的 bounded weights、方向先验和 endpoint 质量，不只重复恒等式与 cover 上界。当前宏观决定冻结 Y-only BSG/cycle 局部迭代，并未把 main N5 目标改成这个 elementary cover fact，范围正确。

## 4. B 稿：量词与三种固定损失策略

已读 R0017_vector_counterattack.md 全稿。其明确结论是既没有完整 finite countermodel，也没有完整 vector strengthening 证明；全文未将 mechanism test 冒充真实 source 反例。

固定 γ_T、γ_Φ、a、b₀ 后，反例须应对定理可能选取的任意小 h；一个固定 r^c density 的构造不能反驳 h<c 的结论。作者据此检查三种廉价删选，均正确：近时间 width r^θ 的 pair 比例至多 Cr^(θ−h)，同一个 affine piece 的 pair 比例至多 r^b₀，逐时间对的单一方向 strip width r^θ 质量至多 Cr^(θγ_Φ−h)。与 r^h 门槛比较分别需要 θ≤2h+o(1)、h≥b₀、θγ_Φ≤2h+o(1)。这些上界保留 g≤1 和原 prior，没有免费将近核方向条件化成新的 uniform 先验。

这些只是对应策略的上界，未说明所有非退化原 tuples 占多少质量。稿件保留该界限。

## 5. Derivation 模板与实际直线恒等式

令 D 加法且满足 Leibniz，F(b) 的两行是 (b,0)、(2D(b),b)。对 d=b−b'、ψ=(x,Dx)，原乘积精确为

    d(F(b)−F(b'))ψ=(d²x,2dD(d)x+d²D(x))
                 =(d²x,D(d²x)).

符号和因子 2 正确，确为原 time-matrix 乘法形式的一个 formal 实现。

对实际形式直线，取水平 x=(u,v)、φ=(c,Dc)、ξ=(−u,v−2Du)。其时刻 t 的 grain 截距第一坐标为 y₁−2tu−t²c；第二坐标展开为

    Dy₁−2tDu−2uDt−2tcDt−t²Dc,

正好等于第一坐标的 D 值。这里使用的是直线 (x+tφ,y+tξ,t)，再减去 f(t)(x+tφ)，没有遗漏 t f(t)φ 项。

有界 additive D 在一个完整实区间连续，Leibniz 迫 D1=0，所以 D=0；稿件没有将完整区间假设赋给有限 dense grains。形式恒等式不提供有限 covers、AD、原管密度、bounded ξ 或 coherence，边界声明准确。

## 6. 数字进位的三个精确失败值

对作者 D_N(b)=N⁻¹Σ j c_jQ⁻ʲ，逐项代入得：

1. x=(Q−1)Q⁻²、y=Q⁻² 时，D_N(x)+D_N(y)=2/(NQ)，D_N(x+y)=1/(NQ)，差为 1/(NQ)。
2. u=(Q−1)/Q 时，u² 的前两位为 Q−2、1；D_N(u²)−2uD_N(u)=−(Q−2)/(NQ)。
3. E_N=D_N−b/N 给 E_N(u)=0、E_N(u²)=1/(NQ²)，所以线性主项相减也不修复乘法缺陷。

Q 固定、N→∞，第三误差与 r^a（r=Q⁻N）的比值为 Q^(aN−2)/N→∞，更不为 O(r)。这些算式通过，但只验证具体合法 tuples 的失败，未提供成功 tuples 总质量的 upper。作者明确指出 dense graph 仍可能删除坏 tuple 或加入 carry fibres，故没有越界否定所有数字模型。

## 7. 完整网上近加法图的 2θ 稳定性

减去端点线性插值，令 g(0)=g(N)=0。普通 j+k≤N 的 additive defect 不变；若 j+k>N，置 l=j+k−N，用 j=l+(N−k)、N=k+(N−k) 两条原假设，得到 cyclic defect≤2θ。固定 j 对全部 k∈Z/NZ 平均，cyclic shift 的两项平均相消，留下 ||g(j)||≤2θ。这也适用于 R^m 的任意范数。

因此全部合法加法 tuples 的 O(r) defect 确会使 single-valued D 图 O(r)-affine，进而模板 F 在 O(r) 内 affine，与固定 a<1 的 r^a-SM 矛盾。该引理没有用于仅 r^h-dense 的 restricted graph；稿件对此界限清楚，未把它提升为主向量定理。

## 8. 最终范围

B 稿给出若干策略门槛与 real carry 风险，root 稿给出固定完整 grain 的真实 joint cover 信息；两者均未制造完整反例或完成 Mat2 expansion。fixed-grain probability upper 与 whole-slice W 路径先验的区别被明确保留。下一轮如使用实际 joint W 数据，仍需新的 bounded-weight/marginal 或增长估计，不由本 review 免费供应。两稿可以据当前范围归档。
