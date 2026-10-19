# DIM-001：任意六维Kakeya集合的Hausdorff下界17/4

2026-10-19，R0109成果说明，沿用DIM-001，不新增命题ID。数学链已在R29/R38/R80独审；本报告与重大性判断已获本轮两份独立正式审查及root接受，最终同步是另一个交付gate。未经外部同行评审。

## 1. 精确结果与来源归属

**定理（通常使用下列具名定理）。** 若K⊂R6包含每个Euclidean方向上的一条单位线段，则

    dim_H K ≥ 17/4 = 4.25。

K可以不可测、非紧或无界，不要求可测选线、sticky/CW规则性、光滑性或代数结构。本结果是已审四维finite输入、保原marks的有限投影桥和经典Katz–Tao递推的高维后果。方法来源按此归属，未声创造新的KT递推。五维满维数及一般维度猜想仍未解决。

当前四维稿是OpenAI于2026-09-24发布的175页原件；官方当前commit1581d4cb、PDF blob45ec20e4与本地完整bytes/SHA256相同。身份不证明数学正确。项目的RED001已经在明列高级定理下逐步拼接原四维全部internal argument和finite读出；所有外部高级proof未从零重证、作者报告的形式化未本地重跑，均如实保留核验层级。

## 2. 明列输入与已审依赖图

四维内部argument使用[GWZ2601.14411v2 Th1.1](https://arxiv.org/abs/2601.14411v2)的精确distinct-tube/平均shading/convex-clustering集合估计，并使用[WZ2210.09581v2 Def4.2/Th5.2](https://arxiv.org/abs/2210.09581v2)、[CV1205.6371v1 Th1](https://arxiv.org/abs/1205.6371v1)、[OSS2309.03068v2 Th1.5](https://arxiv.org/abs/2309.03068v2)及列明的标准固定格式实代数、组合和测度基础。statement/application范围已核，wholeproof按通常具名定理引用。高维步骤使用[Katz–Tao math/0102135v1 Th6.2](https://arxiv.org/abs/math/0102135v1)。

实际依赖为

    RED_base → SRC001 → DIR003 → FSD001 → KT6.2 → DIM001，
    RED001 §20 → 最后的任意集合Hausdorff返回。

RED结果页摘要下游出口，不表示KT被用于证明四维输入。原四维细证与任意集合桥见notes/10_source_audit/source_assembly/R0038_reduction_source_assembly_and_finite_readout_full_proof.md；高维有限桥见R0029_projection_and_prior_audit.md与R0029_conditional_seed_and_six_dimensional_bound.md。历史R29 compact/未assembly措辞已被R38扩展与R108效力澄清覆盖，不作为今日额外hyp。

## 3. 所用四维finite输入

DIR003的精确形式是：每个固定bounded四维graph chart、每ε>0，存在η>0及δ0，使原indexed straight lines若每条各有至少δ^(-1+η)个自己的marks、每方向δ格的总权≤α，则其visited cell union E满足

    Σ_i ω_i #J_i ≤ C α δ^-ε #E。

正权、重复indices与任意权重跨度允许，常数不依最小权重。该结论由SRC的proof-level finite反证及bounded shear/方向bin选择得出；它不是仅从四维Hausdorff statement免费升级的maximal估计。

RED完整审查已经支付finite反证中noise smoothing、subpower slope density、真实selected duration、tempered复杂度、positive horizon和全部模型排除。对任意新family只作已审引理调用，不再要求它属于同一个跨尺度原K。∀输出ε∃输入η保留，未授线性η(ε)模量或全λ尖锐maximal。

## 4. 固定ambient与任意条数的投影桥

在任意固定R^M，设m条原δ-separated方向的unit tubes满足全部角球cap

    #{T:angle(v_T,u)≤θ}≤K(θ/δ)^s， δ≤θ≤1， s≥3。

原总marks≥λmδ^-1。先heavy，保至少cλm条、各有cλδ^-1旧marks。bounded Gaussian P:R^M→R4的投影角collision概率≤C min(1,(δ/angle)^3)；按原cap作角环求和，平均collision degree≤C Kδ^(3−s)log(1/δ)。同时保固定比例nonshort投影，independent-set选择给至少

    c λm/[Kδ^(3−s)log(1/δ)]

条输出分离方向。共同chart/clock和mesh coloring仅损固定常数，每条保自己的旧marks，输出union cover≤C#E。没有拼接不同原线marks或免费继承投影Frostman。源DIR003于是给已审FSD001：

    #E ≥ c λ² m K^-1 δ^(s−4+ε)/log(1/δ)。

两个λ分别来自heavy条数和每条marks。任意m的unsaturated因子真实保留，ambient固定但可为KT实际lift所需M+1。完整证明和独审已归档R29，本报告不把它再次登记新几何引理。

## 5. 递推的真实输入与六维输出

FSD以K≤δ^-η、λ≥δ^η及饱和条数，在每个固定实n≥4给严格次临界K(n,4−ζ)，ζ>0；实际调用先固定ζ、输出loss，再取足小输入η。unsaturated版本同样符合KT(40)。没有调用未证literal临界K(n,4)的uniform loss modulus。

KT6.2把K(n,d)与K(d+1,d′)送到K(n,(2n+1+d′)/4)。对任意0<ζ<1，所需两项正是

    K(6,4−ζ)， K(5−ζ,4−ζ)，

后者角指数4−ζ≥3，落入FSD真实范围。取d=d′=4−ζ得到

    K(6,17/4−ζ/4)。

KT的real参数、total saturated shading和任意条数第二输入均已核；normalized retained/pivot核心在R80另经独审，完整critical preprocessing仍按具名定理引用。上述是有限次调用，不让ambient随δ无界，也不以一个固定loss替o(1)。

## 6. 任意集合的Hausdorff返回

若某普通六维Kakeya K的dim_H<t<17/4，取ζ使d=17/4−ζ/4>t，再选足小finite输出loss。任意细Hausdorff球覆盖按半径δ=2^-k分层。可数bounded graph boxes及外测度pigeonhole，在同一k取positive outer方向质量与每条见证线至少cδ^-1/k²个marks；maximal Cδ-separated有限方向集有至少cδ^-5/k²个方向。只选有限见证，不用可测direction选择或对K积分。

该层球的δ-cover至多Cδ^-t；packing给所用角cap，polylog条数与duration亏损小于任意固定δ^η。nearest-lattice、bounded supporting lines/固定clock windows只付固定常数并保原marks。故KT有限K(6,d)在足大k给δ^(-d+ε)下界，取ε<d−t与原upper冲突。覆盖最大半径趋零保证可选k趋∞。对ζ↓0得到dim_H K≥17/4。

完整外测度/同尺度/finite choice证明是RED001 §20及R38两独审；本段指出返回依赖及量词，不把单尺度Minkowski自动当Hausdorff。K无需有界，先按可数bounded轨迹区域取得正外方向质量即可。

## 7. 同类型一手比较与可主张的改善

[GLX2503.11574v1 Th1.5/Table1](https://arxiv.org/html/2503.11574v1)与[HRZ1908.05589v1 Fig5](https://arxiv.org/html/1908.05589v1)明确普通六维Hausdorff基线为KT的7−2√2。当前版本history仍相同，未把其curved/Nikodym或maximal参数冒作更强ordinary下界。严格差为

    17/4−(7−2√2)=2√2−11/4≈0.078427125>0。

这是对任意普通六维集合的固定维数指数改善。它改变可排除的候选Hausdorff维数范围，具有实质数学内容，既非λ常数也非仅规则子类结论。

本轮A对官方四维README/overview及原§11全部后果、相关引文和有界查询作比对，未识别已明确报告同一17/4或可具体引用的同类型≥17/4来源。原§11.2明确投影给任意d≥4的≥4。完整读域及有限阴性证据见A的R0109_primary_comparison稿；这支持有限成果评估，不是绝对首次/最新最优认证，也不否认别人可能从同样输入得同一推论。

## 8. 独立审查与反攻范围

已有R29两formal核投影、原clock/marks、两个λ、real/ambient/unsaturated及KT第二输入；R38两formal核完整源assembly、finite初始化与任意集合返回；R80两formal核same Ω′ retained indicator的真实回拉/二阶矩。它们各自的自推部分不算独审，root整合记录保留实际全文交审。

本次A/B另对数学强度、原文是否已报告后果、同类型primary比较及重大性作独立审定。攻击的问题包括：仅集合statement换finite、mean换逐管、compact冒任意集合、临界loss模量、依赖循环、把不同类型数字当支配。未以所有证明未从零重证为虚构新hyp；有具体statement/application问题才需重开。全部仍未经外部同行评审，作者署名、Git身份和档案脚本均不充正确性证明。

## 9. Goal第三出口的成果意义审定

用户Goal以“严格改进已知一般下界”为重大中间结果例子。本结果覆盖完整ordinary六维类、真正Hausdorff、固定正指数改善，且新增桥和返回有实际独审，两份正式意见均明确认可，root实际全文接受，故按该第三出口审定为重大中间结果。证明的派生性要求准确归因给四维finite输入和经典KT，不自动抵消所得高维数学后果的价值。

该判断不靠轮数、作者身份、搜索无命中或metadata布尔值。它建立在具体完成推论、明确一手基线、有限已报告后果比对及两份独立价值意见上。首次、绝对最优及外部专家认可均未主张；数学效力、合理有界的新后果评估与这些更强priority声明分开。本轮两formal与逐要求completion audit已实际全文审定通过；最终工具完成仍须本轮同步实证。

## 10. 可复核档案与最终交付gate

本报告沿用DIM-001，历史proof页与失败记录均保留。bibliography与原件在literature，78ID依赖台账、多级notes、固定恢复/宏观机制均可追溯。R109官方OAI4身份记录、R1–R108同步证据检查及逐用户要求审定另存；脚本检查档案和字节，不验证数学。

两formal已确认本报告及第三出口判断、root已全文接受；root仍须完成本轮档案验证、保历史同步、完整tree/逐blob/本地远端同SHA和clean核验，之后才调用Goal complete。一般高维满维数猜想与真反例出口未达成；完成范围只允许用户原目标中的重大中间结果这一分支，不将它改称完整猜想解决。
