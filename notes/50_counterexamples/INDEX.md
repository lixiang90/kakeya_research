# 已排除的步骤与恢复条件

| 指纹 | 已否定的说法 | 严格证据 | 重新开启条件 |
| --- | --- | --- | --- |
| projection-full-plus-kernel | 所有四维投影满维即可给原集加一 | LIFT-001：S4投影为球、纤维有限 | 新的纤维下界或真实选线耦合 |
| direction-slope-equals-fiber | 同一商方向的一维斜率族必形成一维纤维 | LIFT-002：直纹图面，斜率编码于截距 | 证明共同投影支撑线或可控替代条件 |
| linear-gp-implies-unique-quadric | R4中任意四方向独立推出唯一非奇异二次式 | ALG-001A：twisted cubic的三个二次生成元 | 对低次多项式的额外非集中/秩假设 |
| arbitrary-d-two-copy-injective | 任意d方向一般位置足以使cubic2copy单射 | ALG-001C：d>=5 Hankel三次式 | 使用超出线性广度的输入；d=4另行证明 |
| arbitrary-d-rank5-zero | 同上可保证rank5 three-copy零核 | ALG-001C：DQ五次式 | 分类奇异方向簇或增加真实几何约束 |
| two-slabs-ball-in-R3 | 两个非平行速度slab的交落小球 | 线性代数：一般仍有一维自由方向；四维审计§7 | 第三独立法向或沿子空间的额外cap |
| native-coupling-finite-caps-restores-quadric | native耦合、真实长线、非退化q及有限upper cap即可恢复二次 | ALG-004直纹三次模型：任意二次小值迫使隐藏导数退化 | 统一S0/a精度界、额外完整先验或多项式非集中 |
| original-guard-free-tangent-refinement | 原始N0幂界可免费支撑旧切线熵窗口的任意速度细化 | SCL-001：εU>=m与UDε→0不兼容 | 新统一切线幅度界或另付标签熵的窗口 |
| full-directions-survive-parent-for-free | 原始全斜率密度可无代价变成各parent多项式非集中 | DIR-001：薄层分为η^-1个parent，质量合计仍1 | 真实加权预算或原始多项式palette控制 |
| pointwise-true-floor-global-palette | 不加d<1/native来源，仅真实list/floor就保证小全局多项式palette | BND-001：d=1边界、完整斜率密度1、真实floor与常数覆盖仍需η^-1个 | 真正使用d<1、native Hessian或criticality的新输入 |
| branch-inherits-full-parent-floor | 质量仅f比例的native分支可免费使用原父floor | DIR-002：固定分支比例界须付f^-1，多个事件另付并集预算 | 更强分支质量或同一prior的新预算 |
| visible-window-controls-hidden-total | 可见方向的小窗口增量自动控制W或祖先总信息 | ENT-001同网格链式展开保留隐藏项与祖先成本 | 真实full-slope/原生系数的新增熵率及几何约束 |
| native-bins-preserve-raw-W-resolution | d<1原生系数箱及mixed熵率自动给同精度W列表 | NAT-001：H(Wp\|Bp)≥logS，L-list成功≤L/S；H0且非raw来源 | 使用正horizon/source结构，或明确支付p/S与point信息 |
| two-time-recovery-is-overlap-gain | 同一轨道两时刻恢复就提供KT式几何增益 | R0005 KT对照：给定V后两时刻等同y0；改进需跨轨道重合 | 新的共享point纤维、重叠计数或真正独立信息 |
| two-time-lists-give-current-signature | 两参考时刻各自小列表自动使当前point知道全时双signature | FLAG-001：d1 full8真实floor/list，任意全时双短轴atlas覆盖≤CK^C Lε；horizon未算 | 新的同观测完整center-motion匹配或真实critical输入 |
| two-short-axes-project-without-native-cost | true双短轴与完整原列表/floor自动给无损投影 | FLAG-003：d1/2原H0，任意新二次projected atlas覆盖≤CL K^{2d}(a/q)^d，投影H=L | 敏感度×丢轴宽度控制、原c-label恢复或新投影定理 |
| determinant-determines-each-short-axis | 总det窄度决定每根短轴的累计窄度 | FLAG-002：diag交叉缩放反例；外积只能条件性补充 | 同步合法外积极值和实际谱隙闭合 |
| arbitrary_4d_plank_cap_gives_dense_union | 所有全时框加权cap即可给四维D^ε阴影估计 | PLK-001全框QCAP及固定权δ^.5，满marks访问D^(7/2)但cells≤CD³ | 真正排除quadric/方向退化的source条件；加权与mesh等价改写无效 |
| source_free_j3_has_terminal_horizon | literal j3完整tempered、d<1及S1角cap保证H≤L | HOR-001：full8平滑quadric×有限1/2-Cantor，任意二次chart真实floor迫H≥M/6，显式atlas给H≤M；M>6L | 保留真实full-slope/多项式来源并验证操作闭合；不得仅重写greedy输入或改善toy指数 |
| zero_depth_density_one_restores_j3_horizon | 上述formal j3类另有实际n0~1就保证H≤L或有限统一k | HOR-002：内部quadric-level mixture加一次性随机hidden标签，actual f≡0、S1，全部二次tests统一界迫M/6≤H≤M；M任意大 | 冻结n0-only修补；改研究实际祖先方向成本，不能靠density平移或另加同义统计条件 |
| bounded_visible_directions_give_uniform_horizon | actual visible-slope density≤N₀^(κ+o1)加f≡0/S1就有H≤C(L+κ)，C独立任意tempered复杂度 | HOR-003：level-dependent shear u₂=αλ−pq，Q=λ(1+αt²)；真实visible density≤C、κ0且M/6≤H≤M，M任意大，full(V,W)仍η⁻¹ | 整个visible-cost completion策略冻结；需不同的实际前端几何及已验证闭合操作，不继续追加同义统计条件或改善toy指数 |
| quadratic_rank2_affine_codim1_lift | B=diag(1,2)的曲线族可由任意smooth空间仿射/原clock的(1,0)-lift降到R4 | LIFT-005：完整w域强制共同右逆，ρ/y无除法消元给rankB≤1，完整方向rank进一步迫rankB²1；全类必要充分为B0或rankB=rankB²1 | 本窄类完成并冻结；非线性π/时间换元/单selector不在排除范围，重开须不同的真实管几何机制，勿继续等价normal form |
| rich_central_axis_forces_constant_three_plane | 真实δ⁻⁴方向/full marks/central正比例δ⁻²rich cubes迫沿轴同一plane | NAR001：光滑D场、hot三参数刷加full方向补全，plane Eτ gap≈|τ−σ|，固定plane仅O1 cubes | 需使用小union和全局贡献mass的derived averaged信息；本例union≈1且hot总mass小，不反驳NG |
| four_plane_packet_negative_power_improvement | 仅增强同种H4包下界即可获五维固定幂gain | NAR002：H4点发δ⁻³方向unit bush的ambient union≤Cδ，排除统一δ^(4−σ)#T；两步刷模板仅δ¹ | 真正跨包/高阶incidence gain；勿把局部包当满四参数NG反例 |
| single_block_ae_time_free_tensorization | full四参数方向加两个单块a.e.-t定理就自动joint满维 | R0013 coupled接口：f=c,g0的参数条件fiber仅1维；输出条件fiber随t改变，不能交换固定集合量词 | 保同一P和shared t的新joint投影/能量估计；product或独立t平均不能替代 |
| unpruned_joint_L2_has_power_gain | 对全部原dense marks统一E₂≤δ^(−6+σ) | CPJ002真实full4网、f=−τd/g=−τe使E₂≈δ⁻⁶；actualcover≈δ⁻⁵λ³ | 需从原marks证明质量可保的修剪；该例坏时间可删，不是CP或truncated反例 |
| every_long_cycle_forces_further_direction_drop | 从三四五环退化可无限推全部闭环低于full4 | CPJ001六cycle有限差分构造真实full4方向rank且可满来源补全；五环仅3、四环固定首边2 | 不继续逐边polygon；必须从原incidences推出有效cycle质量或新的可检验机制 |
| uniform_shading_lower_and_low_mass_are_different_tasks | 对全部原P_j统一CP只给union，不能反推出PM，故PM是独立更小新路线 | R0015删high whole cells后再次应用CP，任意τ<σ获≥S/2更严格低重数mass；与反向合成正gain等价 | 冻结CP/PM局部改名；此是量词纠错而非Kakeya反例，逐管门槛须另核闭包 |
| unused_coarse_direction_cells_inherit_slab | Phi_p包含在粗Phi_q邻域就使全部Phi_q uniform slab-Frostman | R0016源审查：包含关系不控制unused cells；已用原incidence混合heavy辅助H及L边际upper合法修补 | 必须保原质量证明辅助方向/差prior的cap，不可直接重置原Phi_q |
| tube_KT_subpower_constant_gives_fixed_porosity | 原delta^-eta tube-KT常数直接给独立delta的line-porosity从而套一般卷积corollary | R0016_matrix_span_boundary的短连续δ网格满足相应Y假设而无固定尺度porosity；仅Y接口测试非完整source反例 | 需从完整原time/coherence证明额外跨尺度输入，不能仅引用inverse theorem题名 |
| small_additive_growth_and_tube_KT_force_contradiction | 只有BSG小加法增长、AD与tube-KT固定亏损就足以结束matrix证明 | R17 fixedκ1/2的Cantor积保Y维数1.5/Phi维数.5及真实差prior，全部预定有限加法iterates可任意小幂增长；缺time/F/SM故非主反例 | 必须重新使用真实time-matrix关系或原W点/方向数据，冻结Y-only闭包迭代 |
| rectangle_secant_cancels_affine_matrix | 四边形R4除两个time gaps后自动消去affine斜率 | R17精确代入F=bR+U得到2R；真实sink是2Aplus-2Aplus，error还付gap逆平方 | 需要不同已核恒等式及原mass/sink控制，不能仅改写secant |
| digit_derivative_automatically_preserves_real_Leibniz | 数字coefficient导数可忽略进位并当成真实乘法derivation | R17合法网格tuple有1/(NQ²)残差，远大r^a；只排此跳步不排dense restricted模型 | 需实际carry载体与整张原g质量/cover估计，不能拿formal algebra当finite source |
| dense_restricted_W_gives_independent_marginal_convolution | 原dense bounded graph的2D小输出直接让两边际独立卷积小熵增量 | R18双平面matching worlds：restricted输出2D、independent卷积熵3；timeaction/固定κ版仍有固定growth，SM失败故非完整source反例 | 必须支付BSG提取及同原time/direction回传，不能抹掉g或只引用common-subspace定理 |
| vector_contraction_controls_entire_mixed_slope_row | source22.4的scalar r1恢复可直接换成vector r并恢复全部tildef2 row | r=(1,0)、rows(0,t) contraction恒零却row变化；只排线代跳步，非实际mixed配置反例 | 用完整actual geometry/mass控制正交row或合法降grain，不能dot替换/免费投影 |

这是候选引理反例库，不是Kakeya集合反例库。尚无满足全方向单位线段且维数低于环境维数的构造。
