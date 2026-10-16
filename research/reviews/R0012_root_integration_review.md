# R0012整合复核：共同右逆、核消元及分类边界

2026-10-17。root独立推导与audit_four_dimensional的必要条件证明一致；lifting_obstructions另给原点核正规形证明，并独审root最终分类稿及audit稿。root本文件只作为整合，不将其自写分类的复述充作独审。

## 两种独立必要性证明的交叉核对

audit稿仅用一个内点Θρ≠0，比完整方向rank更弱。T(t)A=I来自该点∂_w a，A是固定矩阵；[A,k]的常数GL变化保线性时间轨道。其d(t)=r_v+t s_v消元从不除潜在零点，t³项s_vB=0，先得s_v=0再证明r_v≠0，之后才以非零常数除法得到β(t)仿射。这一步确实覆盖整个smooth T，不是先假定T标准。

lifting稿选择k₀∈kerT(0)得到g(0)=0，再由原t0恒等式得到a₁₂=w−c0。ρ方向的(h+tb)g+trρ=0先在零点取导数；h0分支由fullrank迫b非零，进而g≡0与B非零矛盾。h非零后只在小邻域除1+βt；主rank矛盾局部已足够。补充分类又得β0，故远处潜在分母零不留缺口。c(t)始终以参数微分消去，没有偷设c0。

root通用m稿的无除法恒等式(8)将上述机制压为矩阵多项式系数。两个代理对主结论都独立得到rankB≤1；trace条件及充分构造也由lifting稿独立核出。一般m的det计算由lifting逐项独审，见R0012_affine_classification_review.md。

## 满方向秩与两个充分性分支

uB=−qℓ及t项D=I+(p/u)ℓ+(q/u)r正确。方向Jacobian[[D,q],[ℓ,0]]的两步det1操作给[[I,q],[ℓ,0]]，det=−ℓq=u trB。非零rank-one B满足B²=(trB)B，故nilpotent秩一确实丢一个方向，不能只登记rankB≤1为充分条件。

B0时π忽略最后坐标、Θ=(y,ρ)，方向rank仍完整，source允许这种自由ruling。B=xℓ₀且ℓ₀x非零时标准π=x′+t x z、a=(w,ρ)、Θ=(y−xρ,ℓ₀y)的投影及det均直接成立。小时间区间I+2tB可逆时同时是Hörmander-type family；代数coherence本身不需要额外猜想。

## 研究边界与宏观决定

本轮解决的是任意smooth空间仿射、保留时钟类，超出了只计算标准rank，因此确有信息增益。但它仍只是局部几何障碍，不是五维Kakeya结果。共同右逆需要完整w域及Θ独立w；一般非线性π的导数随base point变化，不属于同一T(t)。时间换元也不保原clock；标量矩阵例外保留。对单个不规则selector w(y)不能免费使用w微分。

独审通过后冻结这项窄类，不继续扩时钟、normal form、系数或模型统计。下一轮直接研究真实R5方向分离管族的点态三平面窄情形之体积增益；宏观选择与量词见R0012_macro及新任务入口。未声称已具有一般Hausdorff改进，Goal active。
