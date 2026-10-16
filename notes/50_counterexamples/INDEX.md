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

这是候选引理反例库，不是Kakeya集合反例库。尚无满足全方向单位线段且维数低于环境维数的构造。
