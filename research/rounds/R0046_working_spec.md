# R0046 working specification：固定有理R5/3候选及四维finite编码

2026-10-17，Goal active。开轮context.py已运行至tmp/R0046_context.txt，GOAL/STATE/ROADMAP/registry78全部状态/latestR45/AGENTS/R45轮次next已读。HEAD=origin=remote a9cc3af8d7d279d31a066e32b60db63f00882955/tree cef98b860515e18e7ea35cc1e249fa91b781c143/679files/clean，receipt全项通过。上一Goalturn progress：实际四臂/条件BL桥与计数停止明确改变下一动作，精确新primary及同步完成。R45周期macro已先执行，通常下一R48；候选失败则本轮提前macro。

## 1. 目标、命题和量词

总目标仍n≥5/一般Euclidean Kakeya完整解决或重大中间结果。本轮唯一主任务按R45 next：能否用已付DIR003/FSD001的四维finite新种子，真正改善固定有理projection restricted弱型。先测试明确候选，对所有torsion-free abelian G、有限Z⊂G²，xfiber至多M，S1=x+y,S2=−x+y,S3=y,S4=x+3y：

    |Z|≤C M^(1/3)(|S1||S2||S3|)^(10/21)|S4|^(5/21)。

C须独立G/rank/tensor。q5/3,r5/2,p=(2/7,2/7,2/7,1/7)量纲已核但估计未证。若候选严格失败，立即停止该式及本轮seed→fixed-pattern路线，不把finite反例写成Kakeya反例；保存最小失败点而不续调权重/q。

## 2. 排重、闭包及张量必要性

原q7/4 Lemma4.2及§3 weak→strong/tensor只去log，不自动改善q。查primary必要条件和是否已有同等式，旧KT/CP⇔PM全称shading等价改写不得记新结果。restriction保projection upper/M upper但原质量需付；avg/逐管density分别核。

对每个固定有限Z取G^n、Z^n，所有cardinalities和M取n次幂，统一C强制sharp常数≤1。因此整数严格不等式 |Z|^21>M^7(|S1||S2||S3|)^10|S4|^5 足够作为finite反例证书，推广为全称失败另用张量证明。若枚举未找到反例，不是全称证明。

## 3. 实际几何入口

若候选过有限测试，实际构造四维直管/sharedclock/原shading，付DIR003/FSD001方向分离或bin cap、总prior、M与各Sj、δ尺度、λ≥δ^η和常数quantifiers。Freiman编码只保等式不保angular丰富；几何Cartesian积/多个clock不自动仍为原fixed4D模型。任意近似rational frame受新paperTh5.8边界限制。allG/tensor统一不能以fixedrank计算或ambient依赖Cε替代。

## 4. 反攻及分工

独立检验小整数grid、graphs M1、projection核集中、低加法rank、nonuniformfibers、unequalSj、tensor扩增、近似整数编码、clock/方向质量亏损。精确有限验证只证明覆盖的有限代数；只有明确tensor论证才能推广全称否定。

root负责主稿/实验代码和outputs/元数据/Git。A只notes/20_dimension_lifting/R0046_primary_and_geometric_seed_audit.md及research/reviews/R0046_source_and_encoding_review.md，核primary/真实四维编码。B只notes/20_dimension_lifting/R0046_arithmetic_counterattack_and_tensor_scope.md及research/reviews/R0046_arithmetic_and_tensor_review.md，独立算术/张量反攻。最多两互补代理，no agent Git/no额外代理。

## 5. 一主轮停止

候选被严格反例否定、无合法angular/原mass编码、或完整费用只旧q7/4/KT，则本轮停并提前macro，不追加同义权重/q/阈值轮。真新不等式须独立实际全文审查及primary比对后才登记；无自动major。每轮固定入口/多级笔记/文献/验证/安全同步，Goal完整active。
