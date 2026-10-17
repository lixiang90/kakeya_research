# R0047唯一候选：五维真实cyclic selector的全时体积

2026-10-17，R46 macro选择，尚未开展该主任务。Goal仍一般/高维Kakeya解决或重大中间结果；以下是受限真实构造类，不预称新定理或反例。

## 1. 对象、量词、目标

固定d=5。每个dyadic整数N≥2令δ=1/N、D_N={0,...,N−1}/N，A=(a1,a2,a3,a4)遍历完整D_N⁴。任意四个maps b_i:D_N→[−1,1]，定义B_i(A)=b_i(a_(i+1))（a5=a1），以及实际有限segments

    K_N(b)=union_(A in D_N^4) {(t,B(A)+tA):0≤t≤1} ⊂ R^5.

必须估计Euclidean C0δ-neighborhood的真实Lebesgue volume。C0≥10固定，不随N或maps改变；round intercept到δ网只改变固定C0，若用该简化须双向付厚度。每根wholeclock段长度至少1、direction chart满4网、centers统一有界；不是四时间截面或填出来的shade。

首个明确待检验命题：存在绝对c>0、A0<∞（允许依固定d,C0）使所有N和所有maps都有

    |N_(C0/N)(K_N(b))| ≥ c [log(2N)]^(−A0).             (CYCL)

也允许反攻寻真实asymptotic power family：存在固定κ>0、C及dyadic N_j→∞上的maps，使同一volume≤C N_j^(−κ)。每个足够大dyadicN的构造是更强目标；稀疏无穷序列也有§4支付的Hausdorff桥。仅否定某个A0或有限N不自动给power，更不自动证伪Hausdorff Kakeya。无论候选lower还是构造，常数与完整量词必须明示。

## 2. 为何不是R41或旧正幂等价改名

R41 EG lower付exp(−S_r−TC)，本类directions独立所以TC=0，但B_i依赖另一独立A坐标。当b_i在δ-bins上注入时，H(floor(B_i/δ)|Ai)=logN，故S_r=4logN可达。其EG只给N^-4 log^-4，不能推出CYCL；coordinate-separable b_i(ai)的S=0假设确已改变。

本类不包括任意B(A)。任意删direction会破坏fullproduct；任意删时间会破坏wholeclock，不能免费把restricted/shaded实例重造成原类。任何保positive mass选择都须付density，平均/逐管分别核。CYCL没有这些统一闭包，故不能直接反推全称CP/PM；旧未知全称positivegain也不自动推出log下界。下一轮先复核这个双向判断，若真实完整等价出现则不得以新名开方向/登记结果。

## 3. 独立反例测试与实际计数责任

先检查b_i常数/affine、四cycle可逆/退化、独立随机、digit reversal及单t高碰撞。affine族应使用真实slice线性map而非只计最小det；一个singular time不等于全clock压缩。有限计算须明确direction网、intercept取值、δ、每个time slab厚度及union voxel的upper/lower属性，不能以time采样点数作连续volume上界。

解析方向可从真实pair碰撞和四cycle闭合关系出发；不得把四个边际projection sizes相乘充当joint occupied cubes。若发现高entropy只是旧EG责任重写而无新估计，应停止。不得拿Fourier、polynomial或sum-product theorem名称代替原hypotheses、scale、bad-set和完整质量预算。

## 4. 有限全网到compact反例的已知桥与scope

每个δ方向cell中令a′复用代表a的intercept，真实segment(t,B(a)+ta′)距原segment≤Cδ，得到同固定openpatch的连续方向集合，其δ-neighborhood被N_(C0δ)(K_N)包含（固定厚度常数重分配）。必要时先以δ/C的网工作；不能在一个固定C0的upper里无费再扩大半径。有限旋转覆盖sphere，unitclock段内取unitsegment，得到full Gδ。

若每个足够小dyadicδ都有统一κ/C的真实power upper，monotonicity用相邻尺度补全后才满足FD–deLaSalle2607.14824v3 Proposition5.4的(1)_f。该已审primary桥给同一compactE，|N_r(E)|≤C′r^(κ/4)（固定常数/足够小r），因此upper Minkowski和Hausdorff≤5−κ/4。这里四分之一次幂已付，不再次声称缺未知跨尺度coherence。单个/有限样本不够；稀疏无穷尺度须用下一段的step-f处理。

若只有无穷稀疏δ_j=1/N_j↓0且同κ/C，也可定义非减函数f(r)=C min{δ_j^κ:δ_j≥r}（较大r补常数），在每r选择达到min的G_(δ_j)，由N_(2r)⊂N_(2δ_j)支付原(1)_f。Prop5.4输出在r_j=(δ_j/C_d)^4满足|N_(r_j)(E)|≤C′r_j^(κ/4)。以r_j-grid cover即给下Minkowski及Hausdorff≤5−κ/4：对每s>5−κ/4，cover的s-cost≤C r_j^(s−5+κ/4)→0。该序列bound不自动约束上Minkowski。有限N没有这个极限。

这是条件蕴含，不是已经构造这样的maps；新颖性和重大性须另查一手文献。CYCL若证明，首先只是该受限placement类的neighborhood lower，未经进一步Frostman/cover论证不能宣其全部集合Hausdorff满维。

## 5. 一主轮停止和固定协议

只开一轮：得到完整uniform lower、真实power构造及对应scope，或明确没有越过旧EG/4D projection/N^-1/单时碰撞门槛。最后一种即macro停止本cycle施工，不续循环长度、alphabet、熵阈值/时间crop调参，不转成旧CP/PM或下一q任务。任意新reviewed命题须两代理实际独审及primary比对；有限样本只证明其有限整数/volume证书。

恢复先context.py/GOAL/STATE/ROADMAP/registry/latest及R46完整receipt；写本轮量词/反攻/停止条件，最多两个互补代理只编辑assigned文件，root统一提交/同步。Goal保持active；一般五维、全部mixed及Hausdorff主问题不因这个受限test消失。
