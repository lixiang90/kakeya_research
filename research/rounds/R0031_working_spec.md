# R0031 working spec：原Cor3.4实际代数标量图匹配

2026-10-17。R30 commit a964d9e7f95efc30d7003d9441e5d1cfcd3615c1、tree96385a660c9df71dc157402c52978124d177b142，455文件receipt/HEAD/origin/clean已核。GOAL/STATE/ROADMAP/registry/latest round/AGENTS已读，context.py恢复执行。上一Goal turn分类progress：原Lemma3.3一般固定阶逐步重证/两独审/安全同步，非最终或重大成果。R30定期macro已执行，下一常规R33，失败提前。

唯一main按R30 next spec：固定base维度、代数degree、real comparison balls及共同固定holomorphic margins、d0<1；存在ε*>0排除充分大R=M/Δ、0<ε≤ε*的两lists（card≤R^(d+ε)、d≤d0），每member距同一代数reference norm≤M R^ε；pair/common-basepoint subprobability质量≥R^-ε、每色index-base marginal≤R^ε π_i dz，Σπ_i=1；events值差≤ΔR^ε但pair difference norm≥M R^-ε。完整原Cor3.4（PDF35–36）需保这些量词、任意π及相关events，非只单fiber或uniform indices。

Root核degree closure、减真实reference/除M、每incident point norm-to-jet、有限direction/box选择及Fubini/原π/全部loss与TCM001对接。A只写notes/10_source_audit/scalar_sheet_matching/R0031_algebraic_norm_audit.md，逐式重证Lemma3.1必要norm/finitejet/sublevel输入并反攻coefficient degeneracy；B只写同目录R0031_continuation_and_slice_audit.md，核Lemma3.2 fixed-format polynomial continuation及Cor3.4切片边缘、哪些输入真正被调用。最多两个互补代理；后续独审另指定各自文件，不操作Git。

该main向后续Lemma3.5 terminal/knowledge输入推进，不等整篇OAI4或无条件DIM001。TCM001普遍matching只有已具jet假设的函数，不能凭等价restriction自动推出本轮norm-to-jet，故有不同可证伪输入。若3.2并非Cor3.4所需，作为独立continuation责任明确区分，不虚加依赖或为同义推论新立方向。全部旧高维冻结保留。

closure：restriction质量q使原π marginal ceiling乘q^-1；Fubini须先对finite indices同时保a.e. fiber density，选正mass fiber后才归一化，不能用conditional basepoint概率免费保π。平均pair mass、每index-base密度和sliced mass分别核。函数字段real-on-real、complex margins固定；所有Taylor/jet degree常数须独立于系数height、N/R及π最小正权。

countertests：tiny leading coefficient、unused escaping roots、branch points近邻/monodromy、小π、相关events、支持靠comparison边界的mass；反例需满足共同holomorphic域及fixed margins，shrinking域/pole入域不算。目标完整证明或合法counter/精确未付步骤。关键假设失败立即macro；不能以数值roots、只单方向结论或调整常数验收。完成后两独审/root整合、更新状态和台账、验证归档并沿R30父安全同步，不force，Goal active。
