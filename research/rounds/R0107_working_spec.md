# R0107：全窄片collision与原访问条件上界

2026-10-19，reselection后锁定；以下是有限条件lemma，不是fullsource rowcap。未宣新ID或重大结果。

## 1. 精确量词与假设

固定0<τ<1，0<h<1/10，A,B,K,D≥1。每个root有h-separated坐标格Q⊂[-1,1]²（每个坐标取同一h格，可缺格），图值g:Q→[-B,B]。clock概率σ的每v给k1(v),k2(v)、H_v∈[h,2h]、中心y_v及有界c，|k_i|,|c|≤B，且对全部q∈R、h≤r≤1有σ{|k1−q|≤r}≤A r^τ。每个实际访问(celldata q=(a,b),v,T)输出在Y_v内，距 y_v+H_v(g(q)−k1a−k2b,2b−c)≤Bh²。每(v,q)原访问重数≤D。

每个Y_v在所用CB²h-ball内的h²-cover≤K B^C h^-1；可由完整native AD1在h²≥δ时给，但本lemma直接明列其cover假设。clock可有限，图与root必须先于v固定；允许任意依v选择Q_v、任意重数，不授每cell共同clock或每strip下界。

## 2. 唯一目标

证明有C_τ及固定B幂，使该root的原访问clock平均≤C_τ D(AK)^1/2 B^C h^(-2+τ/2)。证明必须在所有b窄片合计，不以先选一个strip损h原质量。可对互不重记的roots相加；只有另付原分母与∑D h^-2可比时才能读出正相对密度gain。此比较不在假设中赠予原source。

## 3. Source匹配和禁止补充

完整code hyperplane及F=[[f1,f2],[0,1−u]]可导同T两time输出形式；H_v=v−u∼h、粗ξ-coherence提供g代表与O(h²)误差。一般wholeF nonfit不授k1 cap；f1常量/f2rough残余保留。不能将nᵀG≈0单独换成ξ2=x2−c，不能把coarsecell occupied数自动换成原incidence数，不能公设新增transverse nonfit或flatness后声已解原问题。

## 4. 独立测试与闭包

测试原Q_v随clock恶意变化、全图能否一次支配全部large subsets、相邻strip输出重叠、对角和τ=1端点、k1 atom、原multiplicity D和不满h^-2输入。average与逐管分开：删除whole-T或marks后upper只对同一原分母成立，不自动重源；clock restriction概率cap归一须除保留质量。与R72/R75/R77/R80/旧CP⇔PM全称重调核范围；本lemma若可归入标准energy就明确为初等估计，不登记新颖理论。

## 5. 停止、审查与结果范围

若计数proof有未闭费用则修正或记录失败，不延伸参数模型。root主10后A/B各独立formal6，只认证实际已读证明及source边界。若有限lemma成立但source导出未付，记录局部信息与实质残余，不宣fullrowcap、fullrough、ordinary、critical seed或major；下一必须处理不同的未付结构或完整重选，不再重证此energy。Goal active，照协议归档验证与同步。

施工澄清：有限proof也适用于总质量≤1的clock subprobability；这不改目标强度，只避免按稀疏shell重新归一。源应用明确附加原clock counting cap≤A(H/δ)r^τ，绝非声原source已给。原degree upper及同shell pair lower可从原cardinality/平均I/CS独立审计，不再将flatness公设当成果；所有一般row归约和横向law缺口保留。
