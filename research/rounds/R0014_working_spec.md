# R0014：共享时间双块投影的真实满方向增益

2026-10-17。起点R0013 commit b20939b36287b9973dbac9dad9eb8e58f4ff80af，208文件回执、local=origin/main及clean tree已核。上一Goal turn分类progress：实际管构造、条件包校准、独审、macro和精确同步改变了下一行动。最终Goal仍active，未达数学完成标准。

## 唯一主任务 N5-COUPLED-PROJ-01

采用R0013_next_coupled_target.md全部量词。固定r足够小、R,C₀≥1；δ dyadic，Ωδ⊂[−r,r]⁴，κ(v)=(1,v)/√(1+|v|²)方向δ-separated，#Ωδ≈δ⁻⁴。bounded anchors f(v),g(v)任意耦合。Euclidean单位轴L_v(t)=(t,bt−d,ct−e,f+dt,g+et)，clock域[0,1/|(1,v)|]；I=[1/4,3/4)由全部axes覆盖，所计原whole-cube marks的dense mass已在I内，不免费丢endpoint tails。

P={(b,d,f(v),c,e,g(v))}固定；A_t=[[t,−1,0],[0,t,1]]，Π_t=A_t⊕A_t。I内δ-slabs的midpoint t_j共享于两块。任意P_j⊂同一P，Σ_j#P_j≥δ^η #P δ⁻¹。是否有固定σ∈(0,1)，对每ε>0可选η>0、δ₀>0，使

    Σ_j Nδ(Π_(t_j)P_j) ≥ c_(ε,r,R,C₀) δ^(−4−σ+ε)？ (CP)

Nδ是四维δ-cube covering number；固定倍尺度等价只损常数。上一轮已独审CP与本子类原cubical volume δ⁵ΣN、incidence count Σ#P_j的比较，不能把finite P的dim_H=0偷改为4。

## 与总目标的关系及分工

该真实光滑三平面场子类保完整四参数方向与原dense shading；它是一般NG的必要检验，任何成功仍不自动抽取一般V_Q，更不自动解决Hausdorff多尺度覆盖。FO单块a.e.-t不能免费tensorize，参数fiber与输出fiber不同。

root尝试shared-time joint energy/多时刻关联或直接结构估计；互补审查1检索并核一手restricted-projection/Grassmann-family定理的准确可调用范围及finite quantitative版本，保存用到的新文献；互补审查2在全部原量词下做真实反例和energy攻击，或给非同义新瓶颈。每人只编辑分配文件，root整合。

## 本轮验收、攻击与停止

优先尝试CP证明或真实满足方向/marks的反例；其次只能接受严格的新联合估计、可调用现有joint定理或带具体损失的新障碍。独立t1,t2、product sanity、smooth selector内点、只改写single-block条件fiber、任意统计irreducibility都不计进展。检验时间集中marks、块间强耦合、参数投影退化及对η/ε的顺序。只给一主轮；没有joint信息增益即macro冻结本子类并另选真实主机制，不能继续等价改写。结果独审、更新恢复入口、同步并核同一local/remote commit。Goal不因局部结果或本轮结束而完成。
