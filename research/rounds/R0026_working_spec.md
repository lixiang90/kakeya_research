# R0026 working spec：large-τ的全局质量门槛

2026-10-17。先读GOAL/STATE/ROADMAP/registry/最近round和R25下一spec，context.py已运行。起点R25 bd475daa2d00f3cc7fab4c47b0dcdca6c89d5214，tree b2f49d26b5b04557cda99f2d58f728d2c3e3409a，386文件receipt、HEAD/origin一致及clean已核。R25分类progress，未达到长期Goal。原Goal active，不重建。

唯一main仍N5-MIXED43-NQ01：支付large-τ分支在选原角ψ之前的vector/global稳定性。与最终目标的关系是关闭带whole-matrix AFF₃准备的mixed43非二次分支尚缺的large-τ alternative；AFF₃存在及完整五维仍另缺。

可证伪命题：若每ρ-window有一条rich vector affine fit，则physical coefficient-weighted nonquad迫其slope小、所保留fiber的原vector E收缩。将各window所选fiber的原时间质量相加；达到下一合法δ^{ηj+1}|Z|则其并集违τ稳定，否则bad-fit windows总质量有可计算upper，删后每remaining窗口有vector affine nonfit。检验是否可在此删选后合法重建good-q/L/g，不能假设旧g自动存活。

量词：原Z、当前Z_j、下一candidate及每window质量均明确；每window可选不同fit。F/G来自同一原row函数及window anchor，不能依赖尚未选ψ。诚实workingmesh w_L=K[ρ+ρ³/τ]，不得沿用原ε₀-controlled mesh。参数需有非循环顺序，13.5两η阈值分别支付。

独审A：源22.5 Step1/3及窗口、anchor、globaltime闭包和q重建。独审B：严格反例攻击global/local、g集中、候选密度和参数；只编辑分配文件。最多两个互补代理，不新增支线。

停止条件：若无法支付真实globaltime质量/重新生成原g，归档严格缺口并立即macro；三点scalarization、投影τ改名或sampling常数不算main进展。若global gate成立，再将带准备large-τ排除写成明确条件定理并独审。不夸大source反例或新颖性。R27常规macro保留，关键失败提前。

收尾：更新台账/状态/next unique task，验证相关数学文档与仓库结构，沿R25父commit安全同步GitHub，完整tree与本地精确commit及全部blob bytes/SHA256回核。最终数学标准不降低。
