# HOR-001：形式j3模型中通用H≤L上界为假

2026-10-17，R0008。证明分三份：notes/50_counterexamples/R0008_smoothed_quadric_prior.md、notes/40_multiscale/plank_inputs/R0008_smoothed_all_width_cap.md、notes/50_counterexamples/R0008_horizon_floor_audit.md。独审见research/reviews/R0008_prior_profile_review.md、R0008_spatial_cap_review.md及R0008_root_horizon_review.md。内部复核，未外部同行评审，不声称新颖性或重大中间结果。

把原exact/charts定义的visible j从2形式改成3，保留其余原始坐标、native derivative scale及真实floor。存在完整8维分段常密度tempered概率先验，选中质量1/4，nativeP*=w、B1，lengthL1，且

n(r)≈log N^(M−r/2)，f(r)=r/2−M；joint角cap满足S1。

取任意固定M>6，visible先验为PLK-001 quadric格点加六系数δ噪声，δ=N^-M；隐藏c为末层充分细的有限1/2-Cantor、W为更细的独立均匀噪声。全部正宽度空间框在原概率下有νvis(P)≤Cδ^-1/2J；短块长度q付q^-3。任意quadratic test、任何assignment/selection的selected质量满足m/q≤K^C a^(1/2)νvis(P_I)。真实floor迫q³≤K^Cδ^(1/2)，所以H≥M/6。

独立构造q=δ真实终端atlas，给H≤M。因此H/L可任意大，具体M12为2≤H≤12。进一步选择与subsequences不能逃过lower。这里不借用已被质疑的generic completion定理。

这否定无source j3模板的上界本身，强于仅否定其greedy证明输入。它不反驳原j2四维论文或高维挂谷猜想；该数据没有原始full-slope subpower密度来源，不含全部方向。应转向保留真实方向来源的模型，不继续优化此toy的精确H。
