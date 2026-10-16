# HOR-002：实际零深度密度为1仍不保证j3的H≤L

2026-10-17，R0010。内部独立审查通过，未经外部同行评审；不声称新颖性、重大中间结果或Kakeya维数改善。本结果是对原exact/chart定义的literal j3拟推广的反例，不反驳原j2四维稿。

## 严格存在性结论

对任意固定L>0及M>6L，存在单world、完整8维分段常密度tempered概率prior，native P*=w、B=1，selected mass1/4，所有深度实际典型密度n(r)~log1（f≡0），terminal joint-angular cap可取S=1，且

M/6 ≤ H(E) ≤ M。

因此额外n(0)~log1也不能恢复H≤L。具体L=1、M=12给2≤H≤12。该profile属于任意固定C(d)（0≤d<1，需d>0时可取1/2）；S及angular depth range可固定。M可任意大，所以即使限制f0=0，该formal j3类的all-model horizon/length supremum也无有限上界。

## 构造和证据

可见轨道混合Q=tY2+Y1Y3=λ的δ-grid levels，δ=N0^-M，每层三参数grid并加六系数δ噪声。层λ赋一个一次性固定的hidden tag cλ∈[0,1]，w0=cλ+η盒噪声，W为更细均匀区间。exactY定位O1 λ，故实际observation support与density在所有深度均有常数upper，积分给typical lower，n(r)=1；并非observable world权重平均。

uniform tag存在性用固定维多项式tests的hyperplane pattern bound、forall参数quadrature及完整ghost/swap估计给出。对任意二次chart、任意完整assignment及selection，其质量统一有

m/q ≤ K^C[a_L+(log N0)²δ^(1/2)q^-3]J+r_N，

r_N比任意固定负幂小。原真实floor为m/q≥K^-1J，tempered J有固定幂倒界，故q³≤N0^o(1)δ^(1/2)，H≥M/6。upper由q=δ的good midpoint cube×原w0-bin真实atlas直接构造，覆盖常数且own-list O1，不输出内部λ。

证明：notes/50_counterexamples/R0010_zero_depth_counterexample_attack.md（模型、profile、cap、§8真实upper），R0010_uniform_random_level_labels.md（uniform lower）。独审：research/reviews/R0010_random_label_review.md、模型稿§9及research/reviews/R0010_root_model_review.md。正向cube shortcut的独立失败证据另见notes/40_multiscale/plank_inputs/R0010_zero_depth_positive_attempt.md；该stripe例自身H0，不与主反例混同。

## 范围与下一步

本例的实际visible-slope density ceiling≈δ^-1，full(V,W)成本更大；它缺少原始完整方向来源。不是欧氏Kakeya集合反例。冻结n0-only completion修补；下一步须研究真实祖先方向预算及其坐标/条件化成本，不能再给同一generic模板追加一个等价统计条件。
