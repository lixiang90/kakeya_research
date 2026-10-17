# R0050：全光滑 lift 的构造、秩与范围独立审查

2026-10-17，B独立逐步审查。结论：下列明确范围内通过；这是既有LIFT-005的存在性等价与适用范围更正，不是高维Kakeya新界，也不认证新颖性或重大性。未经外部同行评审。

## 1. 实际阅读范围与审查责任

实际全文读root的R0050_variational_equivalence_and_full_smooth_lift_classification.md（8节）、A的R0050_nonlinear_lift_source_and_rigidity_audit.md（10节）、当前结果页LIFT-005_full_smooth_variational_classification.md（4节）、R0050_macro.md（7节）及R0050_next_global_frontier_and_critical_path_gate.md（5节）。另复核自己的6节施工稿与原Nadjimzadah2609.06299v1 Def2.1、Prop2.2证明、Prop2.5(i)；自己的施工不计作对自身的独立审查。

已核R12三稿、旧LIFT-005结果页、R49 next/macro及R50 working_spec共7处更正banner；历史数学证明保留，关于一般非线性类尚未被旧必要性论证覆盖的范围判断由本轮更正。本review不认证尚待root完成的元数据、registry、提交或同步。

## 2. 同一参数点的全时第一变分与真实 realization

固定同一个内点P，令z_P(t)=a(P)+tΘ(P)、T(t)=D_zπ_t(z_P(t))。对原全参数恒等式一次求导，确实共同得到

    T a_w=I，T(a_y+tΘ_y)=F(t)，T(a_ρ+tΘ_ρ)=0。

所有a/Θ导数均在P取值，是常矩阵；π的非线性完整包含于沿同一条线读取的T(t)。这里只作一次参数微分，没有遗漏Hessian，也没有把不同基线的Jacobian拼在一起。Θ独立w与全开w、ρ域是实际必需条件。

以Da(P)u、D_(y,ρ)Θ(P)(u_y,u_ρ)为新截距和方向，以T(t)z为新投影，线性组合上式就对全部新参数及全部原t精确实现u_w+F(t)u_y。新轨迹仍为原空间中的直线，不是非线性坐标拉直后的曲线，也不是有限时间jet近似。T a_w=I保证submersion，方向rank保留且成为常rank。原compact时间区间的端点可由原smooth开域及紧性取共同邻域；必要时只取小compact参数balls，全部线段包含条件合法。

因此对该参数线性目标，一般smooth lift与空间仿射、参数线性lift的存在性双向等价。反向只是子类包含。它不等价于原π本体仿射，也不涵盖任意非参数线性目标。

## 3. 常右逆、leading minors与codimension

a_w是与t无关的满列秩矩阵，可扩成一个常GL基；在该基中T=[I,H(t)]。据此

    t²B+t(I−D)−C=H(t)(R+tL)

每个t的rank至多s。s<m时，每个(s+1)-minor左边是一个在非退化区间恒零的标量多项式，其最高次系数恰为对应B-minor，故rankB≤s；s≥m时平凡。没有假设H解析或延拓至无穷，也没有使用ρ列满秩来获得这个下界。

源Prop2.5(i)的满秩分解B=UV以s=rankB给出标准lift，方向loss为s−rankB²。因此“允许方向loss时最小codimension为rankB”在这一精确类中成立；不能替换成曲线Kakeya集的最小Hausdorff维数，或替换成固定ν=0时所有s的分类。B=diag(1,2)须s≥2，标准(2,0)达到，故整个smooth (1,0)类确实被排除。

## 4. codimension-one方向秩、退化边界与校准

root保一般C、p的消元和A在t=0取核补基的化简均合法。u+tv若恒零，则p=q=0且Θ_ρ=0，违反方向满秩；不先除该可能有零点的多项式是必要的。乘法恒等式的t³项为vB，B非零迫v=0、u≠0；t²项给uB=−qℓ。常数行列操作给

    det DΘ=−ℓq=u trB。

于是非零B必须秩一且trB非零，等价于rankB=rankB²=1。B=0的充分例和非nilpotent秩一的标准充分例均通过；非零nilpotent秩一仅有相应方向loss，不能冒充(1,0)。这给整个smooth类的完整codimension-one判别。

两个真非线性可行例已独立展开：B=0时z₃=(1+t)ρ的平方项恰好抵消；B=diag(1,0)时k+k²=y₁使全部交叉项抵消。两例Dzπ的前两列均为I，方向det均为1，空间Hessian非零，且在共同开参数域、全时间成立。施工稿的nilpotent校准方向rank为2，不是3。这些例子严格否定“原π必须仿射”的过强说法，而不反驳分类或diag(1,2)的排除。

## 5. source与forward应用边界

真实lifting来源是2609.06299v1；2511.10918/GAFA00750-4不是其修订。Def2.1确实允许一般smooth保t submersion、Θ独立w，并要求全部ρ的coherence，故第一变分没有削弱原量词。

A对Prop2.2的有限submersion坐标图、正buffer、方向image的开patch及有限旋转的解释与原证明匹配。Hausdorff上界来自局部与坐标投影双Lipschitz等价及有界纤维网，不依赖错误的任意纤维维数相加。maximal应用的coarea与方向像重复需保有限图费用，不能假Θ全局单射。本轮分类本身不使用Kakeya猜想输入；该来源只提供从高维直线到曲线族的forward结果，不能逆读成R5证明。

## 6. 更正、停止与下一轮scope

当前结果页及7处banner正确区分了映射class更大和存在性完全等价，更新既有ID而不新登记同一代数。局部开放域restriction保rank/coherence；这里没有获得任意shading或平均、逐管密度的免费闭包。selector、Θ依赖w、换clock及非参数线性目标均保留为不同定义的未处理范围，不能借此自动续相邻细节轮。

macro与next明确停止本类Taylor/Hessian/normal-form迭代，R51只先做全局前沿和关键路径比较，再选择一个有量词、原质量、合法删选、等价检查及独立反攻标准的唯一后继。其ordinary Hausdorff/finite/maximal区分、具名高级输入、旧冻结责任及不预设重大结果的范围均通过。Goal仍active；本review仅核本文列出的数学与范围，不预认证root后续归档和Git状态。
