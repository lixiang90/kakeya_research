# R0051唯一后继：R52严格复现有限有理算术反例证书

2026-10-17，Goal active。来源新证据与R46候选冲突，下一轮先解决这项真伪责任；不修改q/权重、不重跑旧16点网格、不把有限算术反例当欧氏Kakeya反例。

## 1. 固定入口与意义

先context.py、GOAL/STATE/ROADMAP/registry全部状态、R51root/A/B/macro/twoformal/receipt及R46原候选/熵必要性/旧有限计算范围。高维最终目标不变；该任务删除可能不成立的中间候选，不能以复现来源完成Goal。

原R46全称(R)为每个无挠群有限Z⊂G²存在统一C，N≤C M^(1/3)(S1S2S3)^(10/21)S4^(5/21)，Sj为x+y、−x+y、y、x+3y投影基数，M最大x纤维。文献Tao2511.15135v1及GGSWT2511.02864v3 Problem6.30报告SD({0,1,2,∞};−1)≥1.668>5/3。报告已actual核，产生它的finite rational certificate尚未项目独立验证。

## 2. 精确证书目标和允许输入

找有限整数支持(A,B)及正整数权n_ab，总和Q，给p_ab=n_ab/Q。定义D=A−B和四个随机变量A、B、A+B、A+2B。优选验证

    H(D)−(5/3)max{H(A),H(B),H(A+B),H(A+2B)}>0，

或直接较弱且足够的weighted gap

    21H(D)−10[H(A)+H(B)+H(A+B)]−5H(A+2B)>0。

若D的合并权为d_v、某controlled marginal合并权为c_z，则`3H(D)>5H(C)`精确等价于`∏ c_z^(5c_z)>Q^(2Q)∏ d_v^(3d_v)`；四个marginal分别核，可完全用整数乘幂证strict SD>5/3。数值过大时可给可靠log区间，不强求物化巨整数。

可靠有向区间/可核的有理log上下界必须给严格正gap；只报告float ratio不是验收。所有marginal由同一个jointlaw重算。允许从官方google-deepmind/alphaevolve_results的mathematical_results.ipynb/问题数据取表或对明确支持独立优化后有理化；保原URL/版本/hash/搜索范围，不执行未审远程代码。新概率表必须可重生成且无负数/漏归一化。

## 3. 从证书到完整全称否定

对长度kQ联合type class，目标D的image恰覆盖全部目标type words；逐difference分配joint计数证明surjectivity。保每个Dword的一个原pairword，置x=B−A、y=A+B，得到M=1，N=(kQ)!/∏(kn_d)!，四projection基数不超过对应marginal multinomials K0,K∞,K1,K2。

必须验证某有效k使N^21>(K0K∞K1)^10 K2^5，或给带明确误差的严格存在性证明。清分母/有限高维整数编码保全部五projection等值关系，再压回Z²。用张量放大消掉任意统一C，不能只反sharp C1后忘记原C。可给生成规则而无需枚举天文规模的type words，但所有基数上/下界、M1和整数编码须完整证明。

## 4. 独立反攻及闭包

独立程序/代理从保存的有理joint表重算全部marginals、目标熵gap及(C)所需整数或误差，不复用主程序的聚合逻辑；检查目标不是jointentropy偷换，π2确为A+2B，linear transform的四forms确切对应。只删shading或均匀化可能丢原entropygap，不免费使用。

原算术restriction保projection/M上界不保N；本one-difference代表正好保目标N，typeclass计数支付一切。平均/逐管density在这里没有几何转移，不能声称full angular unit tubes。全部finite证书仅否定(R)，不否定四维源、Zhang旧q7/4、其它slopes的算术猜想或欧氏Kakeya。

## 5. 一轮停止与状态分层

仅做一主轮复现，不求source小数最优、不再换q/权重续轮。成功则把R46候选改为独立证书已否，保原有限无反例历史正确范围，执行macro另选真正高维机制。若原数据不可得且独立有理化未成，如实记录已读primary lower与内部certificate待复现，不把它当新的open improvement；不因网络失效伪造或反复运行无新信息搜索。

正式reviewed需要独立逐步审；未经外部同行评审，不预认证novelty/major。只取得数值law未严格核时保持candidate/exploratory，不以它改Goal完成。

## 6. 分工、存档与同步

root具体证书/完整type与整数转换及整合；至多两互补代理，一个独立exact核算/误差，一个全部量词/来源和反攻，只assigned文件。代码、原表、输出和hash存experiments/arithmetic，source保存literature；状态、失败/路线/registry和唯一next同步更新。每轮沿现有main安全同步并fulltree/canonical/逐blob核验，Goal active。
