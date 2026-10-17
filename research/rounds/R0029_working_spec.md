# R0029 working spec：OAI4到KT finite seed的真实量词桥

2026-10-17。R28 commit3dc500e74d1ff803a29c7b72cfc1052160def3a0、tree8c510c3e6efe2ca9b68a4dec2a1454f84680acb0；427文件receipt、local HEAD/origin/clean已核。上一Goal turn为progress（完成独审/安全同步），非最终或重大结果。固定入口/registry/最近轮次/AGENTS已读并运行context.py。R28已提前macro，R30常规macro保留。

本轮唯一main：审OAI4实际量化结果能否产生KT§6的arbitraryambient K(4,4−ε)或足够的K(d+1,4−ε)。这直接检验四维成果是否通过不同高维机制改善维数；六维17/4仍仅未证桥下的条件算术，不作新界。

检验的显式uniform seed形式：任意固定ambient M≥4及ε>0，是否存在η>0、C、N₀，使所有N≥N₀、bounded box内方向N^-1分离的line族T，满足#T≥N^(3−η)、每角capθ≥N^-1内条数≤N^η(Nθ)^3、总shading mass≥N^(1−η)#T，均有shaded union的N^-1-cover数≥C^-1 N^(4−ε)？原KT lines/shading的grid版本与cover版本转换须付固定常数及小幂，不能当逐管整线；是否正好等价于原K也须核。

Root核OAI4 Theorem2.17/关键finite reduction及原weighted输入，尝试完整种子或给精确缺失责任。A核arbitraryambient→R4方向投影、separation/重数/短线及restriction/shading闭包，并反攻种子；B核KT§6真实参数/shading/递推输入与已有高维一手基线。两个互补代理只写分配文件，不提交。必须先检验候选是否只是冻结projection+kernel加维/集合到finite换名；若是，则停止该跳步，不注册新结果。

验收：真实finite seed，严格边界模型/量词不适用判据，或有精确出处且实质不同的定量输入。角thinning/随机projection若仅付独立接口不算main完成；尤其不得用dim_H=4直接升级uniform finite/maximal。所有源高级证明仍未全面独审，OAI4作为条件输入列明。

停止：本轮若只剩Hausdorff⇒uniform finite的未证跳步，立即macro冻结这一无输入调用，不连续换ε/ambient或thinning称新方向。若有源量化输入未审，则说明具体命题及全部新假设，避免无input循环。完成后交叉独审、更新registry/state/next/文献记录并沿R28父安全同步；不force，不降低高维最终目标，Goal active。
