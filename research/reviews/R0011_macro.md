# R0011：可见方向成本也不足后的路线冻结

2026-10-17。触发：关键候选N5-DIR-COST-01被严格否定。Goal active；仍无n≥5的维数改进、真实Kakeya反例或重大中间结果认证。不能用继续积累模型障碍替代最终数学标准。

## 新结果与停止决定

HOR-003同时保留actual f≡0、S1、full8原prior、native bounds、原floor、全部二次charts量词、实际visible-slope density≤C，仍有任意大M/6≤H≤M。和HOR-002不同，它真正去掉了visible方向的δ⁻¹密度成本。关键是λ-dependent shear使同一个λ既能从base恢复，也填满缺失的速度维数；独立shear copies通常使profile变d1的失败并不排除此机制。

所以继续在这个泛类上追求有限critical k或用projected DIR-003接回completion，已不具备可行基础。现在冻结整个无source/n0-only/visible-direction-cost completion策略。完整(V,W)方向信息确实更强，但本轮不把“再加一个full-slope条件”指定为下一主任务，也不继续改善toy的H下界、误差指数或颜色算法。重开必须有不同的实际前端几何定理及验证过的闭合操作，不能只更换统计条件名称。

保留已审查的概率引理、方向质量工具和source-specific四维输入；其适用边界不变。原稿j2、四维证明的正确性审查及更高维猜想均未由这些模型解决。175页四维proof尚未全面独立重证。

## 转向新的可证伪几何任务

本轮下载并归档Nadjimzadah 2026v1《Lifting curved Kakeya sets to linear Kakeya sets》。Definition 2.1与Proposition 2.2将coherent曲线rulings提升为直线方向，给d_Kak(X)≥d_lin(n+s−ν)−s。此方向不能倒置。标准quadratic lift对n=3、B可逆需要5维直线输入；但标量B可以直接时间换元化直线，故“标准维数高”尚不足以说明无法降低。

下一唯一主任务N5-CURVE-LIFT-01：固定B=diag(1,2)，检验三维曲线族w+(tI+t²B)y是否存在保留时间、空间仿射submersion π_t:R³→R²的(1,0)-lift。允许任意光滑T(t),c(t),a(y,w,ρ),Θ(y,ρ)，要求slope独立w且D_(y,ρ)Θ rank3，全部Definition 2.1 coherence保留。目标是显式构造，或对整个指定类严格排除；不只检验π=x+tUz。

若存在，只能以四维输入推出一项三维曲线满维结果；没有自动五维逆向结论。若排除，只排除指定lift类，不排除非线性submersion或时间重参数。无论哪种，都不自动成为重大中间结果。意义在于检验新的几何降维机制，明确哪部分五维输入可以被四维替代，而不是继续修补旧exact-model模板。

只给一主轮，若无超过标准rank计算的信息增益则冻结此窄类。再下一步须按结果重新宏观选择，禁止顺着细小系数优化无限延长。执行时先读GOAL/STATE/registry，写新working_spec，独立构造与反例攻击并行，归档后同步同一local/remote commit。
