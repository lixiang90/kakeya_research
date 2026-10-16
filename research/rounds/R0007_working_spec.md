# R0007：四维加权fulltime plank输入审计

日期2026-10-16。上轮分类progress：R0006形成独立复核的障碍及工具，已同步61e983535f25dbf70d8e78a988fd2b36c5d749bd；本轮开树干净。已读GOAL、STATE、ROADMAP、registry及上轮，沿用R0006收尾宏观决定。

主任务N4-PLANK-01。它接近总目标的方式：五维拟推广先需要在四维时空中把密集阴影的高重叠转成可用全时空间框；若此输入尚缺，后续j=3 critical推广不能免费初始化。

候选WP4：有界affine traces M_i(t)=b_i+t u_i∈R³，δ=D^-1；允许重复indices和正权重。所有全时正交空间框、cell宽1≤a1≤a2≤a3≤D满足Σ_{M_i⊂P}ω_i≤A a1a2a3。每条保留至少D^{1−η}个time bins，E是所访四维mesh cells。目标：每ε>0存在η>0,C，使Σω_i#J_i≤CA D^ε #E，常数不依赖family、重复与权重。

并行检查：(1) 原四维论文实际有限尺度定理与reduction量词，方向/隐藏条件是否由plank cap推出；(2) WP4与四维convex-clustering shaded-union估计的精确互推，尝试全部假设的反例；主代理查文献与原3D输入，并独审关键新推导。

先写清验证范围。正向必须完整付权重、shading密度、bounded chart、统一ε/η与有限尺度常数。负向必须对所有空间框核验cap，不能仅给曲面上多直线或低维方向集。若只确认‘Hausdorff不自动蕴含’而无更具体输入，则不再将其等价重写延长下一轮；按实际证据重新选题。无论结果如何不降低长期完成标准。
