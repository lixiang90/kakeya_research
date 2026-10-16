# R0014：联合闭环的方向秩层级与精确边界

2026-10-17，root。由lifting_obstructions独立发现的四cycle约束出发，root继续检验五、六cycle。对象仍为同一真实水平线族，不把有限代数闭环当CP证明。所有times在固定I内；γ(t)=(1,t,−t²)。把参数看成R³⊗R²，输出Π_t=A_t⊗I₂，原方向投影D(p)=(B,D)∈R²⊕R²；原先(b,d,f,c,e,g)与此仅坐标重排。

## 1. 同一实际交点的闭环方程

k条参数线p₁,…,p_k以t₁,…,t_k依次相交，p_(k+1)=p₁，精确条件是Π_(t_i)(p_(i+1)−p_i)=0。故存在u_i∈R²使

    p_(i+1)−p_i=γ(t_i)⊗u_i,
    Σ_i γ(t_i)⊗u_i=0.                                (L1)

其中u_i正是两块第一参数坐标B的差，不新增latent标签。δ近交时，若每块两个outputs的绝对误差≤ε，直接取u_i=ΔB_i，有ΔD_i=t_i u_i+Oε、ΔF_i=−t_i²u_i+Oε。因此每个参数边距γ(t_i)⊗u_i至多Cε，闭环的三组moment残差为O_k ε。

## 2. 定量稳定：只需三个分离times，不除方向角

假设各t_i两两间隔≥ρ，且k≤6。任何三个γ列的3×3矩阵G满足||G⁻¹||≤Cρ⁻²：用三个点的Lagrange基，各分母(t_i−t_j)(t_i−t_l)绝对值≥ρ²，分子系数有统一界，得到此范数界。等价σ_min(G)≥cρ²。

保留前k−3个u_i，调整其余三个u_i的每个分量以消去总moment残差，调整量≤C_k ερ⁻²。得到精确向量u_i*，Σγ_i⊗u_i*=0。相应精确参数边γ_i⊗u_i*之和为零；由p₁累加形成闭环p_i*，有|p_i−p_i*|≤C_k ερ⁻²，方向投影亦然。这个修正不要求首边或任意方向差有角度下界。ρ可依δ，但当δρ⁻²不小时结论没有细尺度内容，不应忽略该损失。

## 3. 三、四、五cycle

三个distinct times时Vandermonde可逆，(L1)迫全部u_i=0，因而精确三cycle只能为同一参数线；近似三cycle的全部方向距同一点≤Cερ⁻²。

四个distinct times时Γ=(γ(t₁),…,γ(t₄))的kernel为一维。两块的kernel系数只能相差一个固定u∈R²，故所有参数差位于R³⊗u，所有方向位于仿射2-plane D(p₁)+(R²⊗u)。更强的固定首边定量版本见R0014_joint_attack.md：直接取u=u₁，解剩余三列，无需除首边大小，可把所有相同首边的四cycles限制到同一方向2-plane的Cερ⁻²邻域。

五个distinct times也有一个真正联合约束。定义非零barycentric weights

    w_i=1/∏_(j≠i)(t_i−t_j).

Lagrange插值的最高次系数给Σ_i w_i t_i^m=0（m=0,1,2,3）。所以ker Γ恰为span((w_i),(t_iw_i))：两者独立且都满足三个moment，kernel维数2。对两块同时使用同一组times，存在a,b∈R²使

    u_i=w_i(a+t_i b).

于是方向边

    ΔD_i=(u_i,t_i u_i)
         =w_i[(a,0)+t_i(b,a)+t_i²(0,b)].              (L2)

整个cycle的方向均落在D(p₁)+span((a,0),(b,a),(0,b))，维数至多3。近交经§2修正后得到同一仿射3-plane的Cερ⁻²邻域。这不是两marginal定理相加，而是shared times的联合闭环约束。

a,b独立时这三个向量独立：a s+b t=0迫s=t0，继而第三系数亦0；方向边的三组系数以非零weights乘二次Vandermonde，rank3。因此3不能统一降为2。五cycle的plane通常依整个cycle，不能沿用四cycle的“固定首边即固定plane”而不证明。

## 4. 六cycle已经允许全部四维方向秩

给一个完全实际的例子，排除把前面的退化无限迭代。取t_i=a+hi，i=0,…,5，a=1/4、h=1/12，都在共同I内；令

    q=(-1,5,-10,10,-5,1),
    u_i=s q_i(1,t_i²),
    Δp_i=γ(t_i)⊗u_i.

有限差分恒等式Σ_i q_i t_i^m=0对m=0,…,4成立，故全部三组二维moment为零。取p₀=0、p_(i+1)=p_i+Δp_i便闭合。方向边为

    ΔD_i=s q_i(1,t_i²,t_i,t_i³).

非零q_i乘三次Vandermonde的六行rank4，所以整个cycle的方向仿射span恰4。六个顶点确实不同：第一方向坐标的prefix是s(0,−1,4,−6,4,−1)；仅重复的两对在第三方向坐标分别相差5sh、10sh，均非零。首尾仅闭环时重合。

取固定s>0足够小，全部p_i的directions在[−r,r]⁴、anchors在[−R,R]²；对应Euclidean单位轴含I。Π_ti Δp_i=0保证邻轴在真实t_i相交。六个方向有固定正最小间隔，充分小δ时分离；可用同一D场加入其余方向补成δ⁻⁴满族而不破窄条件。这里只证明一个非退化六cycle能在真实满来源系统出现，补全不提供小union，绝不声称CP反例。

## 5. 可调用packing与不能跳过的质量问题

若ε=Cδ，δ-separated原方向在一个给定仿射l-plane的Cδρ⁻²邻域内，固定有界方向chart的packing给至多Cδ⁻ˡ max(1,ρ⁻²)^(4−l)个。故固定首边的四cycle只能涉及Cρ⁻⁴δ⁻²个候选方向；一个指定五cycle的proper3-plane邻域则容量≤Cρ⁻²δ⁻³。后者不是预先统一plane，不能据此直接对所有五cycles求和。

存在闭环约束不意味着原dense incidence系统必有足量的time-separated四/五cycles。重数m、每管D≈λ/δ的简单局部展开，在四cycle层只给N≈δ⁻⁴与D²m²≤N形式的四维阈值m≈δ⁻¹；这个启发性tree数不在此升级成一般定理。需要实际的cycle下界、角/时间退化删剪与重叠计数才能获得σ。六cyclefullrank例也说明不能靠声称所有长度闭环均退化来绕过这个缺口。

本稿给出新的严格joint代数约束及近似损失，未证明CP、NG或新Kakeya下界；意义/新颖性尚未认证，不能据此完成长期Goal。下一步是否值得继续须以真实cycle质量信息决定，不能沉迷增加polygon边数。
