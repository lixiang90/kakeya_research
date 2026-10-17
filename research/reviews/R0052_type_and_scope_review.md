# R0052：type整数反例、统一常数与后继范围的独立审查

2026-10-17，B。结论：本review所列完整反例链通过，R46固定全称候选被严格否定；不是欧氏Kakeya反例或新维数界。该独立Q12 weighted证书不复现文献的SDfour≥1.668强报告。未经外部同行评审，不认证重大性或新颖性。

## 1. 实际读取范围

实际全文读root的R0052_six_point_exact_refutation_of_R46.md（8节）、A的R0052_source_and_independent_certificate_audit.md（7节）、R0052_macro.md（6节）和R0052_next_arbitrary_density_narrow_transfer.md（6节）；并读实际integer输入、root程序/完整JSON、A独立程序/完整JSON。自己的9节type稿仅作交叉核对，不计对自身独审。本review不认证root后续metadata、registry或Git。

具体文件为experiments/arithmetic/inputs/R0052_rational_counterlaw.json、R0052_exact_countercertificate.py、R0052_independent_certificate_verify.py及outputs下两个相应JSON。没有导入或修改两程序，也未执行远程notebook。B另用独立sequential-binomial product直接重算n240的multinomial，不复用两程序的factorial实现。

## 2. 同一jointlaw、整数熵与来源层次

六点权总Q=12，D支持单射。逐行重算得D权(1,2,3,3,2,1)、A权(1,5,5,1)、B权(3,6,3)、A+B权(6,6)、A+2B权(2,4,4,2)。完整值与权在输入及两输出一致，四个controlled marginals确来自同一joint表。

H(C)=lnQ−Σc ln c/Q给出Δ=21HD−10(HA+HB+Hplus)−5Hplus2，准确指数比为5¹⁰⁰/(2¹⁴⁰3⁵⁴)>1。root的Counter/乘幂与A的排序groupby/素因数指数是分别聚合，未把一方输出当另一方输入。A的自然log区间用z∈[0,1/3]的atanh展开；48项后power为z⁹⁷，正尾上界2z⁹⁷/[97(1−z²)]正确，range reduction、Fraction运算及正负系数的向外端点组合都合法。所报严格区间下端为正，不靠float作数学判断。

尤其本law的3HD−5H(A+2B)<0，精确整数比为2⁴⁰/3⁴²<1；所以不可以说“1.668表已复现”。root/A/macro正确说明采用了允许的较弱weighted目标，来源是旧六点支持上的独立自然权构造。A所读两个官方notebook没有可直接验收的强表是明确版本/片段的读取结论，不扩大成来源报告被否。root保存来源/hash/许可的归档责任与本数学证书分开。

## 3. 有限type图的真实基数、M=1与四个forms

取k=20、n=240，六行字counts为20、40、60、60、40、20。D在单坐标支持上单射，故每个D-type word唯一决定行字；jointtype与目标type一一对应。N=n!/(20!40!60!60!40!20!)为真实图基数，不只是某个entropy upper。一般非单射的条件计数填充不是本实例的额外假设。

变元x=B−A、y=A+B使x唯一决定行字，严格M=1。四forms准确为2B、2A、A+B、2(A+2B)。相应actual projection只需包含于边际type类；root和A均将各multinomial记为安全upper，没有免费把上界当实际image相等。

两个输出的准确N、K_A、K_B、K_plus、K_plus2完全一致。B用逐步二项式乘积另算同一N与四upper，确认N²¹>(K_A K_B K_plus)¹⁰K_plus2⁵，甚至比值>2³⁹；两侧bit lengths分别12011、11971。因此本例已直接支付有限误差，不只声称n趋于无穷时会成立。代码的正整数/总权/重复支持/整除检查、目标injectivity检查及强SD失败标记均与所证明的范围相符。

## 4. 同时整数编码与排除任意C

逐坐标x、y、四forms的abs最大值为6。base14同态ℓ(v)=Σv_j14^j对其有限值域的并单射：最高非零差项至少14^h，低位总差至多12(14^h−1)/13，严格较小。负digits不构成例外。于是N、M=1及四projection的全部等值关系精确保留；不是仅一两投影的近似保真。

一次strict C1图不单独反任意大C。root另取t次Cartesian product，实际N和四个S_j都准确取t次幂，M仍为1，再在长度240t用同一个base14压回Z²。原比率r>1因而变成r^t，无有限常数能统一控制。甚至固定G=Z也得到反例族，符合原命题不许C依坐标大小的量词。

这条闭合不需要uniform高维Euclidean常数，不保角方向/单位clock/密shading，也没有把巨type类当Hausdorff集合。旧有限uniform枚举与新非均匀type图不同，保留其有限正确范围和关闭全称候选并不冲突。

## 5. 后继Q3的强度、闭包与待证门槛

已实际读修后next§3。其输入明确为R⁴有界、regular degree≤2 hypersurface中的exact单位直线、真实physical angular-bin权上界、任意可测shading的原加权平均λ；目标是δ^ε λ³δ³W/α，常数可依c而不能依P/δ/λ。超平面子例可由新3D full maximal经normal方向Fubini和平均Jensen校准，δ³而非δ²符合多一个normal厚度；短clock bush、极小λ、uneven weights仍须原样支付。

该任意λ³强度不由DIR/FSD的near-full λ门槛直接给出，也不等于将旧PW的复杂度/λ费用重命名；一般原四维族没有已付的保方向保质量quadric嵌入。它不同于R50的全参数coherent lift存在性分类。以上是必要范围判断，不认证该候选已新颖或与所有旧命题绝无其它逻辑联系；next先核restriction和双向蕴含是正确要求。

next提出的同时横截、短固定分段和fiber integral是可证伪的实际施工计划，未被当作证明。两个normal均垂直v时选有限kernel在点上有希望，但仍必须证明direction-cone在δ-bins的uniform有限重数、Qv=0奇方向、physical纤维总长度、分段后原λ/W/α和tube端点。仅generic投影或某一normal横截不够；已保这些为待付项。

## 6. 归档结论与停止

root/macro正确关闭固定R46候选，不继续q/权重/更多slopes/小数优化，不新增同义ID或声称重大结果。成功验收的是strict weighted law、一个真实有限图及tensor反例族；没有完成强SD来源复现，更未完成高维长期Goal。

R53最多一主轮的regular quadric模型检验、至少一个非平面类的实质几何、失败即宏观停止的边界合理。即便Q3成立，也不自动处理高维variety邻域的near-tangent pipes、任意degree、奇点、anisotropic短clock、原质量或HRZ完整终点，next明确保留这些责任。审查到此终稿，停止额外数学与检索；root另做元数据和安全同步。
