# R0013 root独立整合审查

2026-10-17。审查对象：primary_narrow_audit、geometric_attack及root的packet/coupled两稿。内部审查，未经外部同行评审。主命题(NG)仍未解决。

## 一手文献与指数

逐核HRZ Thm4.1的n5/k4为p>21/16、对偶21/5；Prop4.2另需p>3/2，吸收指数2p−3在21/16为−3/8。两者不能合成一般线性21/5界。平均密度删轻仅保留至少barλ/2的tube mass，不是常数比例管数；额外密度成本已明确。

Kulkarni Prop18的声明代入n5/k4为δ^((7−d4)/3+ε)，即使d4=4也只δ¹。其参数是maximal维数，不可把OAI4 Hausdorff声明当maximal。原PDF40、41页已由root另行渲染查看：删除预算中的δ^(k−1)、末尾幂和比较都不能仅由所列方向分离推出。自行重算角度环：方向数≤θ^(n−k+1)δ^(1−n)，相交长度≤min(1,ρ/θ)，乘δ^(n−1)并求和只得Oρ（n>k）。这说明打印证明仍需补证，不证明最终Prop18为假。KZ v3修正旧Lemma7.1后的maximal与Hausdorff数值须分开，不能沿用thesis旧版本数字。

## 真实方向旋转构造

独立代入L(t)=(t,bt−d,ct−e,f+dt,g+et)，得方向(1,b,c,d,e)确在D_L(t)中。D在固定盒Lipschitz，所以每个轴线实际相交cube的全部方向都距cube中心D为Oδ；补全方向不破坏窄条件。用0≤t≤1/|(1,u)|保证Euclidean单位长度，小slopes共同包含[1/4,3/4]。

hot参数H(τ,b,c)的逆用b≥β恢复τ，故三参数网确为分离方向而非只有参数分离。固定τ有δ⁻²个方向，三支conditioned frame迫任何可行plane靠近Eτ。投影gap公式由两组互相正交的二维旋转直接得到；固定plane最多匹配O1个hot cubes。方向maximal补全给δ⁻⁴总数，full marks保原质量。

关键限制亦正确：hot tube mass仅Oδ，中央rich incidence mass仅Oδ²；completion的f=g=0切片映射det=t⁴且公共t区间双Lipschitz，故整个union体积≈1。它只反驳不带全局贡献条件的沿线plane一致性捷径，不反驳(NG)或允许删小质量的averaged抽取。

## 包输入及三轴闭合

固定H4的整根单位tube迫法向方向Oδ，故投影方向每bin原管O1；原长marks经有限graph charts和常数重分箱保持。调用DIR003必须保同一索引marks、每管subpower长度及完整四维proof条件。投影访问点移至time中心仅扩大Oδ；投影whole cubes各含半径cδ的4-ball，故其固定倍δ邻域体积与原投影并体积可比。这补明DIR003的expanded cell count如何转回|π_H E|。

每原cube有投影4-volume≤Cδ⁴，求和给|π_HE|≤Cδ⁻¹|E|，不假设满fibres。于是ambient packet lower为δ^(4+ε)λN。若另假定合法brush count、保密度和可求和重叠，则立方估计δ^(3+ε)λ⁴ρ无固定幂gain。H4内满三参数bush的union≤Cδ，严格阻止packet因子统一改成δ^(4−σ)。这不是满四参数主命题反例。

三独立轴与P相交所得三点必仿射不共线，否则从y看的方向至多二维。故P∩(y+W)恰2维；两轴例中的第三方向e4确永不碰P。精确span事实无δ稳定成本，也无质量下界，不能当下一条定量定理。

## 共享时间投影接口

Π_t=diag(A_t,A_t)、ker A_t=span(1,t,−t²)直接核对正确；D的括号生成两个缺失方向，但只给不可积分性。单块线性变换的−1/2系数与FO标准horizontal line一致。root已读FO Theorem1.5/Remark1.7及§3；其底层restricted-projection定理没有在此独立重证。

完整D(P)不保证固定第一参数block后的dim2 fibres，线性例f=c,g0确仅剩e一维；其输出仍通常full4，所以只是错误前提反例。对投影输出条件化产生time-dependent集合，单块固定集合的a.e.-t定理不可直接再次调用。独立product检查无新一般结论。CP仅为这个真实光滑场子类的finite-scale目标，须固定共同clock、单位length与任意dense marks；不声称一般V_Q可转此形。

本轮可以归档明确的捷径反例、条件包接口与模板障碍。没有新Kakeya维数界、真实Kakeya反例或已确认重大结果。关键失败和文献输入疑点触发macro：停止沿线固定plane及只增强同种packet的路线；下一轮只试新的coupled shared-time估计，不继续completion/normal-form细节。
