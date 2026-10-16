# PLK-001：四维无方向加权plank输入为假

R0007，2026-10-16至17。全文notes/50_counterexamples/R0007_weighted_plank_obstructions.md；独审research/reviews/R0007_quadric_plank_review.md与R0007_root_quadric_review.md。内部审查，不声称新颖性，非外部同行评审。

三参数完整线族M(t)=(s+pt,−sq−p/s−pqt,1/s+qt)位于ty+xz=1。对所有正交框、所有仿射中心、全部0<w1≤w2≤w3≤C0，连续参数质量有

μ(P)≤C w1 min(w2,w3²)。

证明用最薄轴的一阶Fubini界、最大轴局部化，以及两短轴固定后沿最长轴解二次关系的至多两根团；包括二次项近零的全部方向。没有从某个坏框反推全框上界。

δ格点离散后，所有δ≤wj≤1的完整plank计数≤Ccap δ^-1/2(w1w2w3/δ³)。固定权ω=δ^1/2/Ccap给所有cell-width测试Σω≤a1a2a3，即A=1。完整D=δ^-1个时间标记给Σω#J≥cD^{7/2}，而四维visited cells≤CD³。因此WP4对任意ε<1/2及任意允许η均失败。

这是Zahl综述已知signature(2,2) quadric障碍的自包含加权核算。方向u=(p,−pq,q)缺少一个自由度，不是挂谷反例。它否定三维输入的直接加维及对应greedy证明，不直接否定j3模型H≤L本身。完整未加权族的δ^-1/2坏框下界另由root精确算式及有限有理网格验证。
