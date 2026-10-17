# R0040：真实五维(3,3)来源与细尺度整时段平直薄片提取

2026-10-17，A 独立源审计。仅处理本轮真实 WZ 配置，不把任意 AD 集或平行 Cantor 校准替代原配置。下文的主要结论是一个**来源条件下的提取障碍**，不是 κ≤ζ 的完整证明，不是 Kakeya 反例，也未作新颖性或重大性声明。高级输入 WZ Lemma 19.2 保留具名；其整篇证明未在本文重新认证。

## 1. 任务、量词及已读来源

固定 0<ζ,γ<1，取 d=5、k=ell=3。原数据满足 WZ2609.22035v1 Definitions 17.2–17.4，T 为原 (4,δ^{-η})-AD 管族，C_CW(T)≤δ^{-η}，κ≥ζ。原几何写成

\[
 E_z=\{(x,y+f(z)x,z):y\in Y_z,\ x\in X_{y,z}\},
 \qquad f(z)\in\operatorname{Mat}(2,2).
\]

保留全部原 Y_z 的 AD/Tube-KT、Φ_p 的 AD/slab、ξ/Φ 的跨尺度 coherence、原管的完整路径及原关联。本文不重开 R18 的 W 提取，也不把新命题改写为旧 CP/PM 或一般 observed-set 增长。

绝对 bounded f 是原文字面输入：PDF65、提取行3361 在 Definition17.2 前定义 Mat(k,ell) 为 entries∈[−1,1] 的矩阵，随后 (2) 给 f:Z→Mat。本轮另以 Poppler 单抽 PDF65 核过该行；不是从 dyadic-Lipschitz 的差值 bound 推出绝对 bound，也无需额外加 chart 假设。

已逐项读取本地 primary 的下列范围，行号按 `literature/extracted/wang_zakharov_2026_sticky.txt` 的 `split('\n')`：

- PDF15–16，Definitions 3.1–3.6，行765–813：AD 采用覆盖数的双侧定义，tube 是完整 bounded graph tube。
- PDF65–66，Definitions 17.2–17.4、Remark 17.1，行3362–3434：整层、coherence、原平均 shading 与逐层 Tube-KT。
- PDF78，Lemma 19.2 statement，行4124–4131；并读其证明中原 full-tube convex sets 的定义，PDF78–80，行4132–4215。本稿只调用该引理的明确 statement。
- LPSW2610.10603v1 PDF148，Theorems 17.3/17.4：共同 a×b×1³ 平直 planks、平均 shading、raw Δ_max 或归一化 C_F；没有从原线族到这些对象的免费桥。

本轮停止条件：若未得到 κ≤ζ，则必须给此前未付几何步骤的严格限制及精确未覆盖部分；不能用局部 C_F≈r^{-κ} 再次抵消来假称新推进。

## 2. 先区分真实水平 grains 与整时段平直候选

每个原 E_z 的水平二维方向为

\[
 H_z=\{(u,f(z)u,0):u\in\mathbb R^2\}.
\]

对一条原直管的轴 p(t)=(p_x(t),p_y(t),t)，把其每时刻的水平 grain 扩大为满二维平面，得到 ruled sheet

\[
 S_T=\{(p_x(t)+u,p_y(t)+f(t)u,t):u\in\mathbb R^2\}.
\]

这只是包含型几何候选：原 X_{y,z} 全局稠密，不表示其在每个局部 patch 中完全填满。若一个固定仿射三平面 P 包含某时间区间内每个 H_t 方向上的非空开 patch，则其方向空间的 clock kernel V=dir(P)\cap\{dt=0\} 固定且为二维，H_t⊂V 因维数相等而 H_t=V，故 f(t) 必为常矩阵。原 source 没有给 f 恒定。

固定三维切片 x=a 所得轨迹为

\[
 \Gamma_{T,a}(t)=\bigl(p_y(t)+f(t)(a-p_x(t)),t\bigr),
\]

一般不是直线。例 f(t)=diag(t,t²)、p(t)=(0,0,t) 给 (a₁t,a₂t²,t)；当 a₂≠0，在长度 h 的时间区间上任意仿射函数逼近第二坐标的 uniform error≥c|a₂|h²（三个等距点的二阶差分即可证明）。该例只校准几何误差，不宣称满足全部 source 数据。局部 ρ 窗口的 O(ρ²) freeze 不因此能粘成单位时间的平直 flake。

## 3. 细 δ 尺度、clock 横截的单薄片密度 gate

令 E_δ=N_{C₀δ}(E)，C₀ 为固定常数。固定 c₀>0。存在 c=c(ζ,γ,c₀)>0 与 η₀>0，使 η≤η₀、δ 充分小时，对每个边长为 a,b,1,1,1 的仿射直角 plank F，若

\[
 c_1\delta\le a\le b\le1,\qquad
 h:=|\operatorname{proj}_{P}e_t|\ge c_0,
\]

其中 P 为 F 的 long 三维方向空间，则

\[
             |E_\delta\cap F|<\delta^c |F|. \tag{FG}
\]

固定倍边长/有限个 unit-long box 的版本只改常数。所有 F 同时满足此界：证明不对 F 作随机选择或付无限并集。假设 κ≥ζ 是必要的使用范围。此结论条件于原 Lemma 19.2，不声称本文已证明 κ≤ζ。

## 4. 正确处理 normal 的时间分量与逐层 Tube-KT

V=P\cap e_t^\perp 为二维水平线性空间。取 V 的正交基 v₁,v₂，取 P 中垂直 V 的单位 v₃，使 v₃·e_t=h；n₁,n₂ 取 F 的两根实际短轴单位方向（而非任意旋转的 P^⊥ 基）。F 及固定倍 enlargement 可由

\[
 c+s_1v_1+s_2v_2+s_3v_3+r_1n_1+r_2n_2,
 \quad |s_i|\le C,\ |r_1|\le Ca,\ |r_2|\le Cb
\]

参数化。将 s₃ 换成实际时间 t，Jacobian 为 1/h。n_i 可以有时间分量，已包含在该换元中；不能先假设两根短轴水平。固定 t,r₁,r₂ 后的水平二维截面方向恒为 V，offset 任意。

记 L_z(x,y)=y−f(z)x，λ_z=||L_z|_V||_op。若某点距原 E≤C₀δ，则它的时间 t 距某原 z≤C₀δ，其空间坐标满足 dist(L_z(x,y),Y_z)≤Cδ。每个 t 只对应 O(1) 个原 z，因为 Z 为 δ-separated；无须控制跨时间 unionY 的 Tube-KT。

若 λ_z≥σ≫δ，在 V 的参数域作二维 SVD 旋转。固定小奇异方向坐标，沿最大奇异方向变化时，L_z 的像为速度 λ_z、长度 O(λ_z) 的直线段。原 Y_z 的 (δ,1−γ,δ^{-η})-tube-KT 给该线段的 Cδ 邻域内至多

\[
 C\delta^{-C\eta}(\lambda_z/\delta)^{1-\gamma}
\]

个 δ-cells。每个 cell 对该一维参数贡献长度≤Cδ/λ_z。积分另一参数得到截面面积

\[
 C\delta^{-C\eta}(\delta/\lambda_z)^\gamma
 \le C\delta^{-C\eta}(\delta/\sigma)^\gamma. \tag{1}
\]

线长大于1、边界 enlargement 或 Cδ 代 δ，只需 O(1) 分段/覆盖。这里确实应用逐层 Tube-KT，而非由 AD 自动推出线状 nonconcentration。

令 Z_σ={z∈Z:λ_z<σ}。对其截面仅用 bounded area。由 normal 范围和 t-带宽积分，(1) 给

\[
 |E_\delta\cap F|
 \le {Cab\over h}\left[\delta\#Z_\sigma+
          \delta^{-C\eta}(\delta/\sigma)^\gamma\right]. \tag{2}
\]

短轴宽 a,b 被精确保留在同一 ab 因子中，不损 a^{-1} 或 b^{-1}。这就是相对体积估计所需的预算。

## 5. 较大密度迫使完整二维水平方向近常

固定 b₀=1/4，取 σ=δ^{b₀}。反设某 F 有相对密度≥δ^c。先取 c>0 足够小，后取 η 足够小，使 Cη+c<γ(1−b₀)/2。由 h≥c₀、(2)、|F|≈ab 得

\[
                    \#Z_\sigma\ge c_2\delta^{c-1}. \tag{3}
\]

固定常数可吸收到略大于 c 的损失指数，以下用 Cc 统一记此损失。若 z∈Z_σ，则对 v=(x,y)∈V 有 |y−f(z)x|≤σ|v|，且 ||f(z)||≤C。因此

\[
 |y|\le C|x|+\sigma|v|,\qquad |x|\ge c_3|v|.
\]

所以 V→R²_x 是双射且逆范数有统一常数；存在固定 bounded 矩阵 G，使 V=graph(G)。对所有 z∈Z_σ，

\[
                         ||f(z)-G||\le C\sigma. \tag{4}
\]

G 由固定 V 决定，不随 z 另选。没有用只控一个矩阵条目或一个标量投影来冒充 whole-f 近常。

## 6. 合法整时间删选：不重设选中点的 AD lower

取 Z'=Z_σ，保留每个原完整 E_z，保留原全部 T、原 Y_z、X_{y,z}、ξ_p、Φ_p 和所有 witness；不把 F∩E 当新配置。取 η'=Mη，其中 M 为整数，使

\[
 C_1(c+\eta)\le\eta'\le C_1(c+\eta)+\eta.
\]

原 allowed 尺度 δ^{η'Z} 是旧 allowed 尺度的子格。(3) 给新 time cardinality≥δ^{η'−1}。原 AD、Tube-KT、slab 及 X 下界均以较弱参数 η' 成立，原 T 的 AD/CW 完全未改。

唯一需补证的是跨时间 Y-union 的 AD lower。对新 allowed ρ 及其 dyadic time interval J，记 U'=∪_{z∈J∩Z'}Y_z，U=∪_{z∈J∩Z}Y_z。新 union 的 upper 直接由 U'⊂U 与原 (ρ,s,δ^{-η})-AD 得到，s=2−κ。对任意 occupied coarse center 选 y∈Y_z⊂U' 与其相距 O(ρ)。当 R≥Cρ 时，原这个**完整** Y_z 的 δ-AD lower 提供≥δ^η(R/δ)^s 个 fine cells，而每个 ρ-cell 至多容纳 Cδ^{-η}(ρ/δ)^s 个该 Y_z 的 fine cells。因此

\[
 |U'\cap B_{CR}(y)|_\rho\ge c\delta^{2\eta}(R/\rho)^s. \tag{5}
\]

R≈ρ 时 lower 由至少一个 occupied cell 补齐；有限倍 ball 与 dyadic grid 切换只损固定常数。于是 U' 是 (ρ,s,δ^{-Cη})-AD，η' 吸收这些费用。这里没有给一个任意 selected Y-subset 设 lower，也没有将 union 的 AD 升为 Tube-KT。保留 Φ_q 的原容器即可满足 coarse coherence；不用声称所有 unused Φ_q cells 有额外 slab upper。

## 7. 原始关联/平均 marks 仍有真实质量

时间删选不产生一份新 uniform 源。为显示原始质量，给每个 p∈E' 的每个 fine Φ_p-bin 选一个原 witness T；固定 point 上每根 T 至多对应 O(1) 个这样的 bin。由原 AD/X 下界和 (3)，

\[
 |E'|_\delta\ge\delta^{-5+\kappa+Cc+C\eta},\qquad
 \deg_{\rm witness}(p)\ge\delta^{-\kappa+C\eta}.
\]

故原 marked incidences≥δ^{-5+Cc+Cη}。每个 (T,z) 至多承载 O(1) 个 δ-separated p，原 #T≤Cδ^{-4−Cη}。在原 uniform-T×unit-time law 下，完整保留层的 raw marked mass 至少

\[
        {\delta\over\#T}\#\{(p,T)\text{ original retained witnesses}\}
        \ge\delta^{Cc+C\eta}. \tag{6}
\]

该式只给平均 duration，不声称每根原管都保留逐管 dense marks。T 的完整路径、原 AD lower、all-convex CW 上界均未改；(6) 没有把成功后验重新宣布为 AD 管族。此处也与原 Remark 17.1 的平均 shading 结论一致。

## 8. 在每个新 window 调用原 Lemma 19.2，得到矛盾

原 Lemma 19.2 的完整量词是：对某 ρ∈[δ^{1/3},1]、σ_L∈[ρ²,ρ]，**每个**新 z₀ 及其 ρ-time window 满足

\[
 \#\{z\in Z'\cap z_0^\rho:|f(z)-f(z_0)|\le\sigma_L\}
       \ge\delta^{\epsilon_{19}}\#(Z'\cap z_0^\rho),
\]

则 C_CW(T)≳δ^{C(η'/γ+ε₁₉)}(ρ/σ_L)^κ。只找到一个好 window 不足以调用它。

由 (4)，所有新 times 的 pairwise f 差≤Cδ^{b₀}。取新 allowed ρ 为略大于 C^{1/2}δ^{b₀/2} 的最近尺度，令 σ_L=ρ²。于是

\[
 c_4\delta^{b_0/2}\le\rho\le C_4\delta^{b_0/2-C_4\eta'},\qquad
 \rho\ge\delta^{1/3},
 \qquad |f(z)-f(z_0)|\le\sigma_L
\]

对所有 z,z₀∈Z' 同时成立。因此每个新 window 的全部 times 均好，可取 ε₁₉=0（若 statement 要正参数，取任意小正值再吸收）。原引理给

\[
 C_{CW}(T)\gtrsim
  \delta^{C\eta'/\gamma}\rho^{-\kappa}
 \ge c\delta^{C\eta'/\gamma-(b_0/2-O(\eta'))\kappa}. \tag{7}
\]

先选 c=c(ζ,γ,c₀) 充分小，再选 η≪c，使 η'≤C₂(c+η)≪b₀ζγ/C，且 η'<γ。κ 有原 bounded range，故 (7) 严格大于 δ^{-η}，与原 CW 上界矛盾。这证明 (FG)。ρ 不是把整配置空间重缩到 σ 后免费继承 CW；它只是原引理允许的内部参数。

## 9. 对新 LPSW 输入真正排除的量词

若一家共同尺度的 flat planks 均满足本稿 clock 条件，且 shading 是 E_δ∩F 的子集，则即使按任意非负原 weights 取平均，也有平均密度<δ^c。因此当 η_src→0 时，不能从完整 κ≥ζ source 提取平均密度≥δ^{Cη_src} 的这种**细 δ、whole-clock、平直** family。

这不是说 (FG) 单独否定所有 Theorem 17.3/17.4 调用。若 a=δ^u，0<u≤1，LPSW 要求 λ̄≥a^{η_L}=δ^{uη_L}；本稿上界只迫必要条件 uη_L≥c（忽略固定倍）。当 η_L<c/2 时它不可能成立；但若 fixed-loss 策略选择 η_L 或输出 ε_L 较大，必须另计其全部预算，不能据此直接否定。单 flake 的 raw-density 校准或定理的 η_L(ε_L) 未知模数，也不准擅自填成线性关系。

下列仍未被反证：clock 分量趋于0的 family；以 e≫δ 的 E_e 作 shading 的方案；额外几何空间/非平直 ruled sheet 的合法 slicing；支付固定密度损失后仍有严格 saving 的其它调用。对 E_e，时间误差可混合约 e/δ 个 Y_z，原逐层 Tube-KT 不自动控制其 union，本稿 (1) 不能无费用重用。

## 10. 本轮结论与停止边界

本稿得到一个有原配置、原整管 CW 与完整时间删选支撑的严格门槛，超出 R39 仅局部 C_F 端点校准：**直接从细尺度原 E 提取任意小 loss、整时段且 clock 横截的平直三薄片不可行**。它也定量解释了为何原随时间转动的水平 grains 不能免费粘成新 LPSW 的整时段平直对象。

完整 d5/(3,3) 的 κ≤ζ 仍未证明；本文不清除 AFF₃/矩阵增长或其它 mixed branch，也不输出新高维维数。下一步若无新输入，不应把 E_e blur、clock 缩短或局部 freeze 改名再续同一提取；是否有真正全局 slicing/auxiliary 几何及其原 E 回传，由本轮其余主稿实际证明后再审。
