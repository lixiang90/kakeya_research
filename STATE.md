# 当前研究交接

更新2026-10-17（Asia/Shanghai），最近轮次R0015。长期Goal active；未解决n≥5/general Kakeya，无新维数界、真实Kakeya反例或已确认重大中间结果。

## 恢复与宏观状态

R0015起点R0014 commit 565016ef8fc9ecf9c36a09b6e57dd5387b6f235d，233文件回执、local=origin/main及clean tree已核。本轮沿此父同步；完成回执tmp/sync/R0015.json在完整远端核验和精确本地导入后生成。下一轮核回执/git，再读GOAL、STATE、ROADMAP、registry与R0015正式轮次，运行python scripts/context.py；不从局部末段恢复。

上一Goal turn分类progress。本轮是第三轮macro节点并实际执行停止规则：没有新质量估计或Kakeya界；通过证据纠正PM新路线的误判、冻结等价迭代，转真实多尺度矩阵分支。初等等价不新增result ID，也不作为数学突破。AGENTS新增开轮合法restriction闭包与双向蕴含检查。

## R0015量词纠正及冻结

原CP对同一full方向图P的全部合法P_j统一量化。保留high重数whole cells后，原平均密度仍可用η余量吸收常数1/2，得到新的合法选择，P/anchors/单位轴/clock均不变。因此CP(σ)推出任意τ<σ下至少S/2原mass满足m≤δ^(−1+τ)；PM(τ)反推CP(τ)已核。存在正gain层面CP⇔PM；精确endpoint不等同。完整证明notes/40_multiscale/coupled_projections/R0015_uniform_shading_closure.md，两代理独立核验及research/reviews/R0015_*。

R0014“单次union计数不直接给mass”仍正确，但原问题可删选后再次调用，所以不能把PM当不同新机制。历史候选已加更正。CP/PM本身仍open，没有反例；其光滑D场子类局部迭代冻结，不以inverse、entropy、relative或重数阈值改名重开。论证依平均密度闭包，逐管long-marks的输入未必闭包，不能移用DIR003。

两步path端点恢复F+(a+b)D−abB=0及原方向rank-one cone cap≤C(θ+δ)只是边界。路径终点law按路径数重权，缺对原prior的domination，不能把cap当mass删剪；不继续局部条件数/阈值推演。

## 唯一下一主任务：N5-STICKY-MATRIX-01

返回Wang–Zakharov arXiv2609.22035v1 Definitions17.2–17.4的真实d5/k=ℓ3配置，f:Z→Mat(2,2)。完整tube(4,δ⁻η)-AD、CCW≤δ⁻η、cross-scale原管/Φ_p/ξ_p相容、dense2D grains、Y_z的(2−κ)-AD及(1−γ)-tube Katz–Tao、Φ_p的κ-AD及γ-slab Frostman全部保留。一般方向分离管不自动sticky，source约化也未在本项目全面重证。

下一候选是原Lemma20.3的完整Mat(2,2)非线性版本：固定source参数ζ,κ,γ,ε₀,μ，适当ε、η及依η的δ₀；某source允许ρ∈[δ^(1/4),δ^μ]上，对所有z₀及dyadicρ-interval J、所有实矩阵R,U，满足

    #{z∈Z∩J:||f(z)−zR−U||∞≤ρ^(1+ε₀)}≤ρ^ε(ρ/δ)

是否推出κ≤ζ？R,U不限entries；κ在source允许0<κ≤2范围，不能途中缩原亏损。精确目标notes/40_multiscale/sticky_matrix/R0015_next_matrix_target.md，输入审计R0015_source_matrix_reset.md。下一轮先working_spec，再从真实L-tuples/原质量推进联合二维扩张或可约分支。

已有正向输入不为空：source Lemma20.2 pp86–87明确适用所有矩阵尺寸，已处理dense local-affine branch；其V-tuple/19.2依赖仍须核，非线性分支另用L-tuples。Lemma20.3 pp88–89的scalar方法靠Y维数1−κ矛盾；本分支Y维数2−κ，尤其κ<1时单个标量projection满1不够，两投影也不能免费相加。原V/L-tuples给Y平移由(z−z')(f(z)−f(z'))(Φ−Φ)控制，这是实际来源，不是CP的替代假设。

He矩阵和积、He–de Saxcé Lie表示定理可作参考，但不可约/商非集中/远离stabilizers与submodules及多次作用闭包都须从原数据证明。后者允许某些可约表示，不可一概排除；也不许添加irreducibility丢掉合法分支。原更新作用Φ差，不能直接当Y+aY。下一主轮至多两互补审查，一项真实L-tuples及affine输入，一项向量扩张/可约反例；需实际joint估计或严格分支收缩，无新信息再macro，不回formal j3。

这只是五维sticky一个关键分支；(3,2),(4,2),(4,3) mixed cases、一般到sticky及Hausdorff多尺度覆盖仍未解决，不替代最终一般Kakeya目标。成功后仍需独立完整审查与一手新颖性比对才能评估重大性。

文献库现17篇PDF；新增He1611.09639v2（29页）及He–de Saxcé1806.06375v3（23页），均原PDF/全文/SHA256/精确read_scope。metadata/R0015_source_check.json区分声明阅读和全文独立重证；两篇均未直接用作无条件新证明输入。核心175页proof仍未全面独立重证，SRC001/DIR003继续conditional。

## 保留与冻结

CPJ001四/五cycle约束与六cyclefull4例保留；CPJ002未修剪E₂≈δ⁻⁶障碍保留。两者均无原mass下界，不是CP反例。CP↔PM的原平均shading等价已核，因此冻结该子类局部改名，重开须不同实质输入。

NAR001：full4实际unit tubes/full marks可沿central rich轴旋转plane；union≈1，hot mass Oδ，central hot incidences Oδ²，只排直接沿轴固定plane，不排averaged删剪。NAR002：固定H4整管包、原subpower逐管marks在DIR003条件下给δ^(4+ε)λ#T，假设两步brush/密度/重叠也只δ¹；H4 δ⁻³方向bush排包级统一负幂增强，不是主NG反例。

保留DIR002 truefloor、ENT002同prior entropy、FLAG002条件外积、PLK001全框QCAP、PLK002固定维转换、SRC001和DIR003实际方向质量输入。SRC001/DIR003条件于完整四维proof及全部输入正确，α=C Aδ³，不能替generic completion或maximal theorem。

HOR003：literal j3 full8、actual f≡0/S1、visible density O1(κ0)仍M/6≤H≤M任意M；完整(V,W)成本η⁻¹、缺真实full来源。原paper可见j2，不能把formal j3反例当原论文反例。HOR001/002/003范围不同。

LIFT005已完整分类任意smooth空间仿射/原clock codim1 coherent lift：X_B=w+(tI+t²B)y在完整w、Θ独立w、全ρ及满方向rank下可lift iff B0或rankB=rankB²1；不排一般非线性π/时钟换元/单selector。该窄类冻结。

继续冻结免费投影加一、无条件次数恢复、guard-only、小palette、native-to-W无损、双轴自动matching/投影、generic WP4、无source/n0-only/visible-cost completion及finite critical k修补。新冻结未修剪L2 gain和无限polygon降秩。重开须不同真实信息；失败指纹见notes/50_counterexamples/INDEX.md。

## 同步执行

每轮working_spec→数学/攻击→独审→必要macro→状态更新→安全同步。Git CLI网络不可用可用GitHub connector，以已核base tree只上传变化blob、lease且不force push。回读完整tree/path/mode/blob，核全部本地SHA256，导入精确远端commit并核同一HEAD/clean后写ignored回执。Python中文用-X utf8。
