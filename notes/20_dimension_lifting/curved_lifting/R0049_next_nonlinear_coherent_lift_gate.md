# R0049唯一下一任务：一般非线性空间的coherent codimension-one lift

> **R0050范围更正（2026-10-17）：** 下文保留开轮/历史论述。对目标 `w+F(t)y`，在同一个参数点沿同一条lift直线取第一变分，可构造同codimension和方向rank的真正全时affine lift。因此一般smooth与affine的**存在性等价**，旧文“空间affine为实质限制/一般nonlinear未排除/需逼原π affine”的判断不再成立；原π本身仍可真正非线性。完整更正见 [R50主证明](R0050_variational_equivalence_and_full_smooth_lift_classification.md)，当前登记为 `results/reviewed/LIFT-005_full_smooth_variational_classification.md`。不新增ID或重大性声明，换clock/selector/Θ依赖w等边界保留。

2026-10-17，R50唯一主任务；待证，不重开已完成的空间仿射分类细节，也不预认证高维新界。general→sticky初始化按R49停止；coarseentropy不能改名续轮。

## 1. 与总目标的关系及旧结论

Nadjimzadah的真实lifting从较高维直线Kakeya输入推出曲线结论，方向不可逆。现有LIFT005完整处理保原clock、空间仿射π_t(z)=T(t)z+c(t)的(1,0)-lift：对X_B(w,t;y)=w+(tI+t²B)y，必要充分是B=0或rankB=rankB²=1。B=diag(1,2)在这整个旧类不可能。

原结果明确没有排一般空间非线性submersion。本轮新增class去掉π的affine限制，保其它原coherence/方向满秩量词。旧定理不统一蕴含新命题；若全coherence会逼π affine，需要新的rigidity证明，不能先假结论再称推广。不是继续LIFT005的clock/normal-form/系数优化。

## 2. 精确命题与量词

固定B=diag(1,2)。问是否存在非退化含0的时间区间I、有内点的y,w∈R2和ρ∈R的共同参数域，及smooth函数

    π(z,t)=(π_t(z),t),   rank D_zπ_t=2,
    a=a(y,w,ρ)∈R3,     Θ=Θ(y,ρ)∈R3,
    rank D_(y,ρ)Θ=3,

使所有原参数及所有t∈I同时满足

    π_t(a(y,w,ρ)+tΘ(y,ρ)) = w+(tI₂+t²B)y.

π_t允许一般空间非线性；Θ必须独立w。同一原曲线的全部ρ都投回同一曲线。定义域必须容纳整段所选线，不将一条线的局部t-jet一致误作全时coherence。先判本local full-parameter class构造或不可能；若真构造，再按source实际全局/有界chart量词核能调用的曲线结论。

## 3. 先读源、合法归一化和反攻

先读已存Nadjimzadah **arXiv2609.06299v1** 的Definition2.1/Proposition2.2/2.5及旧LIFT005三稿；A本轮核官方history仍v1（2026-09-05，15页）。这个lifting读本允许一般smooth time-preserving submersion。**arXiv2511.10918v2/GAFA10.1007/s00039-026-00750-4是另一篇Bourgain-condition文章**，本轮读取其§1.3/1.5只用于general→sticky范围，AppendixA不能作为lifting定义的修订版。正式来源与元数据逐项对应，不因作者/曲线关键词混同。新版本若实际出现再由root统一保存bytes/hash。

Θ满秩可局部用v=Θ作方向坐标，y成为Y(v)；对w求导给 `D_zπ_t(a+tv) D_w a=I₂`，故D_w a rank2。这些是合法必要式，但D_zπ一般依赖z,w,v，不能照搬旧共同常数右逆。空间Hessian/高阶t-jet必须在同一原a、Θ上相容，不能给每条线单独重选frame/π或只逐点匹配。

反攻quadratic/nonlinearπ、可逆source重参数、局部kernel foliation、混合w/y/t导数；区分同一t处所有directions与每点只经过的方向子流形。通用projective变换若改原clock不在此类。标量B可经t↦t+bt²变直线的旧例不应误排，但也不是本固定diag(1,2)保clock构造。

## 4. 验收、蕴含和不允许的捷径

验收为一个核完整rank/submersion/全coherence的真nonlinear lift，或对整个上述smooth class的逐步no-go。只重复旧affine t³系数、先假π affine、只保给定selector w(y)、少一个ρ、降低方向rank或换clock，都不回答此命题。若得到新rigiditylemma，先独审是否真正用full class，不能把改写旧定理当新方向。

合法开放域restriction可保这些rank与全coherence，但不是对任意shading的uniform正幂估计；平均/逐管密度和完整高维反向归约没有在本任务自动成立。若存在可用lift，直接潜在收益只是以4D输入推出某三维曲线结论，source应用量词和新颖性另审。若不存在，只排除该coherent降低维度机制，不能当高维Kakeya证伪/证明或重大结果。

## 5. 一主轮停止与恢复

只开一主轮。若仅旧rank障碍改名、需先加affine/selector/未证foliation假设、或没有超出旧类的新必要约束/构造，则停止并macro，不追加Taylor阶数/阈值/clock参数轮。真新证明先逐步独审、一手比对及scope修正，未经外部同行评审；不预宣major。

恢复先context.py、GOAL/STATE/ROADMAP/registry/latest及R49reviews/receipt；不要重跑R46/R47计算。root统一Git和文献，至多两互补代理只assigned文件。长期目标不变，Goal active；下次常规macroR51，失败提前。
