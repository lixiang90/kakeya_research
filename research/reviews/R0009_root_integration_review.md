# R0009整合复核：方向质量输入的稀疏与加权量词

2026-10-17。root独立复核amplification稿与weighted稿。证明链仍以SRC-001及完整四维proof正确为条件；未把主定理的Hausdorff statement直接升级为finite shading/maximal theorem。

## 独核的关键步骤

方向δ/10球互不相交，体积u=cMδ³。固定大shift盒Q和目标盒Z使z−U⊂Q，故单次命中概率严格为u/|Q|。K=ceil(|Q|/u)次平移后的expected覆盖≥(1−e^-1)|Z|；只须near-full数量，不须覆盖每格，无coupon-collector对数。有限center集的maximal H_Rρ-separated子集用其ρ球覆盖已得方向体积，从而数≥cρ^-3。bounded chart使slope与unit方向距离双向可比。

Shear保持t、b及原time marks；新增速度v+a仍固定有界。每个原δ-cell的shear像与移动到新bin center的O_R(ρ)邻域仅遇固定个ρ-cells。union upper为CK#E，未误乘M。ρ=Cδ固定倍数时每新time-bin合并固定个原marks；η≤ηsrc/2保证门槛余量，任何marks集中方式均不影响。

SRC-001在放大后chart应用，得到#E≥cK^-1δ^-4+σ≥cMδ^-1+σ。M=1与M≈δ^-3均保持同一常数形式，未假设原族方向丰富。此处唯一深输入为SRC-001。

权重部分固定coloring的任意代表法更直接：同色非空格数由unweighted bound控制；实际marks≤δ^-1且每格质量≤α给目标。每条代表保有逐线marks下界、其footprint属于E；没有用代表marks代替该格原indices的实际marks。无需概率集中、最小权或权重级数。原子方向质量单位与物理密度Aδ³已区分。

root补核连续版本：有限正质量方向格可从full-measure长marked轨道中取实际代表，积分访问数≤δ^-1ν(all)。这是分析性估计，无需输出不可观察轨道标签，也不要求有限化mark patterns具统一多项式数量。

## 适用范围与宏观边界

源zero-depth的相反raw multiplicity lower含N0^gainρ³，本方向输入upper含Aρ^(3−ε)。A subpower、ρ=N0^-D时选Dε<gain/2得矛盾；A=N0^κ时仅能排除gain>κ。一般parent的visible Jacobian J/q³与full slope Jacobian J/q⁴已逐坐标核对，均须除完整parent prior质量。

Prop2.16仍是不同任务。用direction upper控制某group的访问重数，只比较其真实A_group与n(L)J0；不因此得到比greedy stopping更大的plank concentration。一般cap-class未记方向来源，HOR-001也未被本条件工具消除。未证明受限极值类闭合，无Kakeya维数改善。

两份互补稿另交叉独审；本文件不替代其作者外的审查。工具自身初等、未声称新颖性或重大中间结果。原草案的δ³单位错误已在R0008收尾修复，本轮全部主陈述使用α单位。
