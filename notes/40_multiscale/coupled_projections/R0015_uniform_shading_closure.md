# R0015：原着色删选闭包使 CP 与 PM 的正幂增益等价

2026-10-17，root。两代理独立检查同一量词后确认。这里修正上一轮把PM视为不同质量机制的判断；这是初等的量词闭包观察，不是新的Kakeya估计、文献新颖性或重大结果。CP、PM均未证明或证伪。

## 1. CP 的全称选择不能丢掉

固定原四参数δ-separated full graph P，N=#P≈δ⁻⁴，bounded anchors、Euclidean单位轴及共同I。每个原时刻允许任意P_j⊂同一个P。S=Σ#P_j，δ^ηNδ⁻¹≤S≤C Nδ⁻¹。m(j,Q)为原fixed output cells的重数。

CP(σ)表示：对每ξ>0可选η_CP(ξ)>0，使**所有**满足这些条件的原选择都给M=Σ_jNδ(Π_tjP_j)≥cξδ^(−4−σ+ξ)。不是只有当前一次配置的union数值。原方向图P即使某些参数在删选后无marks，也不必删除，故满方向来源仍原样存在。

这里用的是本轮原平均质量门槛，不是每管长marks条件。whole-cell删选未必保持逐管密度；若以后换成逐管版本，必须重新验证闭包，不能把本论证无条件移用到DIR003之类的输入。

## 2. CP 推出常数比例质量，牺牲任意小gain余量

假设CP(σ)。固定0<τ<σ，取ξ=(σ−τ)/2及η₀=η_CP(ξ)。要求原η≤η₀/2，δ足够小以吸收1/2常数。则至少S/2原mass满足更严格阈值

    m(j,Q)≤δ^(−1+τ).                                 (U1)

否则保留所有m>δ^(−1+τ)的完整原cells。对应P_j^H⊂P_j是CP允许的新选择，anchors、P、N、时钟和单位轴全部未变，原质量

    S_H≥S/2≥(1/2)δ^ηNδ⁻¹≥δ^η₀Nδ⁻¹.

故可再次调用CP。另一方面，每个保留cell承载超过δ^(−1+τ)个原labels，所以

    M_H≤S_H δ^(1−τ)≤C Nδ^(−τ)≤C'δ^(−4−τ).

CP在这个新选择上要求M_H≥cξδ^(−4−σ+ξ)，两式因σ−ξ−τ>0矛盾。若Nδ为minimum covering number而非fixed grid，minimum cover≤fixed occupied cells，所需lower方向仍成立；固定倍尺度只影响常数。

(U1)直接包含PM(τ)的要求：δ^(−1+τ)≤δ^(−1+τ−ε)，S/2≥δ^ε S/2。其实得到的是常数比例原incidence质量，不仅δ^ε比例；无需正规化subset或免费保常数比例管数。

## 3. 反向及端点边界

PM(τ)本身以阈值δ^(−1+τ−ε)保cεδ^ε S，除质量即给M≥cδ^(−4−τ+η+2ε)。内部ε和η按CP最终误差变小，就得CP(τ)。

若M采用minimum cube covering而不是fixed网格occupied数，每个covering cube只遇常数个fixed cells，故上述occupied数lower仍给M的同阶lower；没有把两者的比较方向混用。于是

    ∃σ>0 CP(σ)  ⇔  ∃τ>0 PM(τ).                      (U2)

精确端点未混同：已证CP(σ)⇒PM(τ)对每τ<σ；不据此宣称CP(σ)⇒PM(σ)无损。

单次union计数确实不能形式上推出mass，但原问题有对全部shadings的量词，删选后再次应用足以弥补。这就是上一轮漏用的信息。修正R0014交接中“未证等价”的当前状态；保留旧轮文本为历史，在其末尾注明本轮纠正。

## 4. 研究决策

没有证明PM，也没有新质量修剪估计。把CP改写成PM、inverse concentration、restricted weak-type或相近entropy目标，不能算独立新路线。按开轮停止条件冻结本光滑D场子类的CP/PM局部迭代，除非获得不同且已验证的实质输入。CP本身仍open，而非refuted。

本轮two-path恢复/原cone cap也没有提供路径终点law对原prior的权重比较；不借此再开一个等价mass目标。下一步回到一手真实多尺度配置中尚未被处理的五维矩阵分支，保留其完整AD、convex Wolff、slab Frostman、tube Katz–Tao和原长路径来源，不向任意管族免费添加这些假设。最终一般Kakeya目标不变。
