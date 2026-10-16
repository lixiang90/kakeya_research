# R0015：PM 的原选择量词审查；与 CP 的正幂增益等价

2026-10-17。作者：`lifting_obstructions`。任务 N5-PRUNED-MULTIPLICITY-01。root 在本轮发现 universal shading 量词可以再次调用 CP；以下独立核验该关键事实。结论：存在正 gain 的层面，原 PM 与 uniform CP 等价。把 PM 另当一个较小的新质量目标不能降低当前难度，应按宏观规则停止该局部改名。没有证明 PM、CP 或五维 Kakeya。

## 1. 原数据与必须保留的量词

P 始终是同一个 full four-direction graph，#P=N≈δ⁻⁴，anchors 每方向一对、bounded，单位 axes 共同覆盖 I。P_j⊂P 是任意原时间选择，

\[
 S=\sum_j\#P_j\ge\delta^\eta N\delta^{-1},
 \qquad S\le C N\delta^{-1}.
\]

在固定 output δ网格令 m(j,Q) 为原重数。删选只改变 P_j，不改变 P、N、directions、anchors、单位 axes、clock 或 grid。所有比较使用未正规化的原 incidence 数；不会删除无 marks 的参数后把剩下的稀疏方向族假称为 full family。

uniform CP 的含义至关重要：给出一个正 σ，对每个最终误差 ε₀>0，有 η₀>0，使其 covering lower 对**全部**上述原 P_j 同时成立。它不只是针对当前这一次选择的数值 union 下界。

## 2. Uniform CP 推出常数比例低重数质量

假设 CP 具有 gain σ>0。任取 0<τ<σ，取

\[
 \varepsilon_0=(\sigma-\tau)/2,
\]

并取得 CP 允许的 density exponent η₀。以下输入要求 η≤η₀/2；小 δ 时常数1/2可由这个指数余量吸收。

事实上可证明比 PM 更强的结论：至少 S/2 的原 incidence mass 在

\[
 m(j,Q)\le T_0:=\delta^{-1+\tau}
                                                        \tag{2.1}
\]

的 cells 中。反设该 low mass 小于 S/2，定义合法的新选择

\[
 P_j^H=\{p\in P_j:m(j,Q_j(p))>T_0\}.
\]

它保留整个 high cell 的原参与 labels，所以该 cell 的重数没有被人工稀释；其原质量

\[
 S_H\ge S/2\ge\tfrac12\delta^\eta N\delta^{-1}
       \ge\delta^{\eta_0}N\delta^{-1}
\]

在充分小 δ 时满足同一个 CP 的 density 门槛。全部其他输入原封不动。

high occupied cells 的数量满足

\[
 M_H\le S_H/T_0\le C N\delta^{-1}/T_0
       \le C'\delta^{-4-\tau}.             \tag{2.2}
\]

另一方面，在新选择 P_j^H 上再次应用 **uniform CP**，得到

\[
 M_H\ge\sum_jN_\delta(\Pi_{t_j}P_j^H)
       \ge c\delta^{-4-\sigma+\varepsilon_0}.
                                                        \tag{2.3}
\]

若 Nδ 定义就是 fixed dyadic occupied cells，则第一不等式为等式；若允许其他相同边长的 covering，仍有该方向的不等式，故无覆盖常数漏洞。

因 σ−ε₀−τ=(σ−τ)/2>0，(2.3) 的 lower 与 (2.2) 的 upper 对小 δ 矛盾。故 (2.1) 的常数比例结论成立。

PM 的阈值 Cε δ^{−1+τ−ε} 比 T₀ 更大，可取 Cε=1；S/2≥(1/2)δ^ε S。因此已得到 PM 对任意 ε∈(0,τ/4) 的要求，甚至不需要仅保留 subpower 比例。η 选择可由上述固定 CP 调用给出，当然也允许依 PM 的 ε 再减小。

这一证明保持 marks 在共同 I 内，未移动接触点、改 direction source 或把新几何近交添加成 shading。删掉的只是原来合法的 incidences，恰属于 CP 已经量化允许的全部选择。

## 3. PM 推 CP 的反向核对与正确结论

若 PM 具有 gain τ，保留低重数 mass≥cε δ^ε S，除以阈值 Cε δ^{−1+τ−ε}，得到

\[
 \sum_jN_\delta(\Pi_{t_j}P_j)
 \gtrsim\delta^{-4-\tau+\eta+2\varepsilon}.
\]

对 CP 给定最终误差 ε₀，取内部 ε<min(τ/4,ε₀/4)，并把 PM 的 η 缩至≤ε₀/4，即给 σ=τ 的 CP。缩小 η 只加强原 density hypothesis，没有无偿放大原质量。

因此

\[
 \boxed{\text{存在某个正 gain 的 uniform CP}
 \iff\text{存在某个正 gain 的 PM}.}
                                                        \tag{3.1}
\]

精确端点不应混同：PM(τ) 给 CP(τ)，CP(σ) 已证明 PM(τ) 对每个 τ<σ；这里没有另证 CP(σ) 的 endpoint PM(σ)。

此前“单次 union 数值 lower 不自动给大比例原质量”的判断仍然正确，但不能据此把 uniform CP 与 PM 分开为难度不同的任务。新证明实际用的是对**删选后的原数据再应用** CP，先前的单次数值比较没有利用这个量词。现有恢复入口应记录此纠正，不能继续称二者是否等价未知，或借重命名 PM 继续同一局部迭代。

## 4. 本轮另见的端点代数，尚无新质量结论

反例/计数攻击中曾检查以下真实 two-path 端点事实。它只供归档，不作为重新开启本子类的理由，也未解决任何 mass 输入。

若 p₁→p₂ 在 time a、p₂→p₃ 在 time b（a≠b）精确相交，按 R²-valued blocks 写端点差 Δp=(B,D,F)，则

\[
 \Delta p=\gamma(a)\otimes u+\gamma(b)\otimes v,
 \qquad F+(a+b)D-abB=0.                  \tag{4.1}
\]

若 det(B,D)≠0，两个 blocks 的 (4.1) 唯一确定 a+b、ab，故有序 (a,b) 至多两种；给定顺序后 u=(D−bB)/(a−b)，中间参数 p₂ 也唯一。这是联合恢复，单个 block 只有一个方程不足以定两个 symmetric time parameters。

原 full-direction source 对坏端点 cone 有直接 upper：对任意固定 p₁，bounded box 内

\[
 \#\{p\in P:|\det(B(p)-B(p_1),D(p)-D(p_1))|\le\theta\}
       \le C\delta^{-4}(\theta+\delta),
 \qquad0<\theta\le1.                    \tag{4.2}
\]

证明不含额外正则性：在 R⁴ 的方向差坐标中，固定 B 的 norm=s，D 被限在宽≤Cθ/s 的 strip，面积≤Cmin(1,θ/s)；以 B 的二维 polar measure s ds 积分，sublevel volume≤Cθ。disjoint cδ-balls 的方向 packing 只把 θ 加大 Cδ，因为 determinant 在 bounded box 中 uniformly Lipschitz，得到 (4.2)。这仍是原方向图 derived cap，而非 PM 的新统计假设。

但上界 (4.2) 没有说明原 two-path mass 有多少送到这些 endpoints、每个退化 endpoint 承载多少 paths。路径的终点 law 以“有多少中间参数与原时间 labels 通向该终点”为权，不是 P 的原 uniform counting prior。它可以在原 prior 很小的 cone 中被大幅重权；没有一个已证的权上界或 domination，不能把原 cap 直接用于这项 endpoint mass。单纯对 rare set 赋大权这一逻辑可能性不是实际几何反例，但足以指出所缺输入。

没有这项原质量比较，(4.1)–(4.2) 不是新的质量修剪估计，也不应把它们再改成下一目标继续局部尝试。这里停止近似条件数、路径数与阈值细化，服从本轮宏观换路要求。

## 5. 本轮攻击结论

未找到满足原完整方向来源和任意小 η 的 PM 反例，也未证明 PM/CP。已独立核验的关键发现是 uniform shading 量词使两种 positive-gain formulation 等价，纠正了将 PM 当作单独较小质量任务的思路。普通 caustic、分拆成许多焦点、只改变 low threshold，都不能以此认定为新主路线进展。

应由 root 执行宏观停止并转向不同的一般五维几何机制；本稿不提出新的统计条件、不继续 polygon 分类，也不把初等等价视作重大中间结果。root 最终稿的交叉审查见下一节。

## 6. root 最终量词纠错稿的独立审查

已逐步读 `R0015_uniform_shading_closure.md`，并交叉核另一代理的 `R0015_mass_pruning_attempt.md` §2–4。两稿通过，无需数学修正。root 的 ξ=(σ−τ)/2、η≤η_CP(ξ)/2 足以吸收删选后的1/2质量常数；完整 high cells 保留其全部原 labels，原 P 与 N 不删除，所以满方向图没有在第二次调用前被换成稀疏图。

high footprint upper≤CNδ⁻τ 与 CP lower 的指数矛盾方向正确。minimum covering 的 upper 不超过 fixed occupied cells，故不依赖把两种计数强说成逐项相等。PM⇒CP 的误差重命名、较小 gain 的反向与未声称 endpoint 无损也全部正确。

关键闭包使用的是本轮**总质量** dense 条件。若另一个问题要求每根管均有长参与，删 high cells 未必保持该条件，不能无检查照搬；当前稿没有越界到该版本。原场子类 CP/PM 应冻结为同一未解问题，而非认定其中某个已被反例否定。two-path endpoint cap 不控制重新加权的终点 law，这项研究边界也已正确保留。

此独审只确认量词纠正与停止决定所依据的数学推理，不把它登记为新的质量 gain、Kakeya 结果或重大中间结果。
