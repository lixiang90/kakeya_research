# 当前研究交接

更新2026-10-16，最近轮次R0006。长期Goal active；尚无高维Kakeya解决、新维数下界或经文献确认的重大中间结果。

## 宏观状态与恢复入口

R0005已同步352bd6d3d031dedbbf1c191ccefc35805842d9f6；R0006开轮工作树干净，先作固定宏观审视。六轮的局部工具和路线排除均不计作重大中间结果。R0006收尾审视已改选不同主输入审计，见research/reviews/R0006_macro.md。不得仅从上轮最后一个代数式继续。

文献库6篇PDF、提取文本与关键源码保持；本轮无新下载。核心四维PDF与06-isotropic.tex核对过官方blob，但175页证明与外部输入未全面独立验证。原稿version2为j=2；j=3五维拟推广的初始化、cap类、极值闭合均未建立。

## R0006实质结果

- FLAG-001：原10.2的near-parallel同时匹配法向、法向位置及中心速度。给定双完整signature及同一当前p_L的小列表，可条件性构造全时交框J≈g0g1/σ，保留完整prior和有限次采样质量。两个参考时刻各有小列表不够。
- full8的d=1边界例实现真实own-depth列表、νQ≈q³g²、n(g)≈g、J≈q³g及常量覆盖；任意一长两短全时known atlas覆盖≤CK^C Lε。即使长轴全局固定仍有中心运动残余。此例horizon未计算；不具critical认证。
- FLAG-002：外积负log超可加而非可加；固定网格的段下界/terminal上界可夹逼全部节点及拼接缺陷。谱隙r=σ(k+1)/σk和近乘积比ρ给实际复合top-k左奇异plane的sin最大principal angle≤r/ρ。
- 真实j=3同步det/外积二级极值、coarsening闭合、共同原始列表和谱隙准备仍缺。条件矩阵工具不是已建critical path。
- FLAG-003：d=1/2有限Cantor full8模型P*=w−StY3实现同prior native箱lower、全时双薄轴、真实列表/floor、常量覆盖及原H=0。丢敏感短轴Y3、仅免费提供几何cell后，得到Z=u+tv、w̄=c+tD。
- 即使免费给完整投影可见仿射线，任意whole-block二次测试known atlas也有M≤C_d L K^{2d}(a/q)^d。沿线Markov+Frostman积分无额外q^-1。显式终端q=a true系统给投影H=L_depth，隐藏profile为1。不能免费携带旧c-bin。
- 原FLAG-003有H=0且raw full-slope来源未保留，不是positive-horizon/critical/Kakeya反例。三份独立审查与root整合复核位于research/reviews/R0006_*review.md；未改变的旧实验不重跑。

## 保留工具与冻结版本

ENT-002同prior mixed-scale系数熵率、DIR-002真实floor加权预算及FLAG-002条件外积工具保留。NAT-001仍区分native箱与raw W精度，exact current point的信息不可漏。原始N0幂界不自动成为统一切线幂界。

冻结：朴素投影加一、无条件局部次数恢复、guard-only旧窗口修补、小全局palette、无损native-to-W桥接，以及本轮“仅两个短轴即可无损投影/自动当前signature matching”的版本。重开flag须有针对完整signature或sensitivity×discarded-width的新可检验输入；不得只换轴名、外积名或反复完善H0 toy。

## 下一轮唯一优先任务：N4-PLANK-01

问题转到五维初始化前的必要几何输入。源四维论文Lemma2.15调用的是三维加权fulltime plank估计，而四维Hausdorff结论不自动给四维加权凸聚集/阴影并集估计。

先逐项核查现有四维论文是否真能提供下述更强输入，或需要何项新增结构：M_i(t)=b_i+t u_i∈R³，δ=D^-1；对所有全时空间框，cell宽1≤a1≤a2≤a3≤D，有Σ_{M_i⊂P}ω_i≤A a1a2a3。每条index保留至少D^{1−η}个time bins；E是所访四维mesh cells。目标为对每ε>0存在η>0及C，使Σ_iω_i#J_i≤CA D^ε #E，常数独立于indices、重复轨道及权重。

验收：明确它是否由已归档四维结果严格推出；给量词完整的推导或满足全部plank/shading假设的反例，或定位唯一缺失而非同义的原始几何条件。先查原文方向Frostman/cap、极值和阴影密度来源，禁止以Hausdorff满维直接替代上述统一有限尺度估计。一个审计主轮后根据证据重新选择，不以重述目标为结果。

## 操作

恢复依次读GOAL、STATE、ROADMAP、results/registry.json与最近正式轮次；python scripts/context.py已排除working_spec误选。每轮先写工作命题，三轮或关键反例触发宏观审视。系统Python中文用-X utf8。

R0006以R0005为父增量同步；核对完整远端tree、同一local/remote commit与干净树，回执tmp/sync/R0006.json。Git CLI网络不可用时沿用已连接GitHub API及精确commit导入，不force push。长期Goal仅达到GOAL.md数学标准才可complete。
