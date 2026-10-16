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

这是候选引理反例库，不是Kakeya集合反例库。尚无满足全方向单位线段且维数低于环境维数的构造。
