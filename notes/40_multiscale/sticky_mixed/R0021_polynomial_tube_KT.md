# R0021：有界次数向量多项式的离散 tube-KT 振幅估计

2026-10-17，root。主任务 N5-MIXED32-Q01 的有限几何输入。本稿自包含证明；source 应用另列，不能仅由本引理宣称整个 mixed 或 Kakeya。待独立交叉审查后登记。常数放置相对 R20 待证草案作明确修正：固定常数放在 2/γ 次幂**内部**；不声称可将其移到幂外且仍独立于 γ。

## 1. 精确定理 PCT

固定整数 D,m≥1。存在 C=C(D,m)≥2，使以下成立。设 0<d≤1、0<θ≤1、0<γ<1、K≥1；P:[0,1]→R^m 为次数至多 D 的向量多项式，R=diam P([0,1])≤1。设 B⊂[0,1] 是有限 d-separated 集，#B≥θ/d。设 0<e≤1 且 e≥dR，P(B)⊂N_eY，Y 在一个固定 bounded box。

对所有 e'∈[e,1]、L∈[e',1] 的任意方向 e'×⋯×e'×L tube，假设

    N_e'(Y∩tube) ≤ K (L/e')^{1−γ}.             (PCT-input)

N_r 用半径 r 的欧氏球覆盖；改成边长 r 的 cubes 或固定倍宽 tube 只会改变 C。结论是

    R/e ≤ [C K θ^{-C}]^{2/γ}.                 (PCT)

常数 C 与 γ 无关，但整个右侧会依赖 γ。R=0、e≥R/C 时平凡。tube 容许的 bounded 长度改成固定数可由固定坐标缩放得到同一式。source 使用 K=δ^{-O(η)}、固定 γ，因此这种常数位置修正不改变其小幂预算。

## 2. 两个有限次数事实及其证明

首先，有限维多项式插值给

    ||P'||∞+||P''||∞ ≤ C_D,m R.               (1)

理由：减去 P(0)，各分量绝对值≤R；在 D+1 个固定等距结点用 Lagrange 公式表示，再对固定基多项式求一、二阶导数。D=1 时二阶导数为0。另一方面，某一分量 p 的 oscillation≥R/sqrt(m)；由积分中值 bound，q=p' 满足 ||q||∞≥R/sqrt(m)。

其次，对非零实次数≤n多项式 q、n≥1，及 a>0，有

    |{t∈[0,1]: |q(t)|≤a}|
       ≤ C_n [a/||q||∞]^{1/n}.                (2)

自包含理由：若 sublevel 集测度 b>0，按其测度分位点选择 n+1 个点，相邻点相距≥c_n b；在这些点上 |q|≤a（可取闭集的分位点，或极限）。Lagrange 公式的分母≥c_n b^n，分子在[0,1]有固定 upper，于是 ||q||∞≤C_n a b^{-n}。移项即(2)。该 sublevel 集至多有 2n+1 个区间/孤立点分支，因为边界包含于 q=±a 的有限根；q 为常数时单列。故 d-separated 集在其中的个数≤b/d+C_n。measure upper本身不够，后一个离散边界项必须保留。

## 3. 从原离散样本保留下导数

若 D≥2，取 α=c_D,m θ^{D−1}，常数 c 足够小。用(2)及 ||p'||∞≥R/sqrt(m)，令

    S={t: |p'(t)|≤αR}.

则 |S|≤θ/8，分支数≤C_D。即使 p' 的实际次数较低，也可用 n=D−1 的 weaker upper（α≤1）。若 d≤c_Dθ，则

    #(B∩S)≤θ/(8d)+C_D≤θ/(4d),
    #B_good≥3θ/(4d).                          (3)

否则 d≥c_Dθ，而 e≥dR 已给 R/e≤1/d≤C_Dθ⁻¹，包含在(PCT)内。D=1 时 p' 是常数且 |p'|≥R/sqrt(m)，直接取 α=c_m，不删除样本；下文照用。统一可写 α≥c_D,m θ^{D−1}，#B_good≥cθ/d。

good set 的 connected components 数≤C_D，每个分支上 p' 符号固定且绝对值≥αR。因此对任意长度 O(e) 的实区间 I，

    #{t∈B_good: p(t)∈I}
       ≤ C_D [1+e/(αRd)]
       ≤ C_D,m e/(αRd).                       (4)

最后一步用 e≥dR、α≤1；这正是离散尺度假设的实际作用。跨分支的 fold 只付 C_D，不假设向量曲线全局单射。

## 4. 一个真实短直管内的 cover 下界

只需考虑 Q=R/e 大于某个 C_D,m²。取 u=c_D,m Q^{-1/2}，将[0,1]分成至多 C/u 个长度≤u 的 intervals。由(3)，某 interval J 内

    #B_good∩J ≥ c θu/d.                       (5)

以 J 的一个端点 t₀ 作 Taylor 展开。由(1)，对 t∈J，

    P(t)=P(t₀)+(t−t₀)P'(t₀)+O_D,m(Ru²).

余项≤Ce，而切线段长度≤CRu。故 P(B_good∩J) 及其距离≤2e 的原 Y-witness，都在某个宽 e'=C₀e、长 L=C₁sqrt(Re) 的直 tube 中。这里取2e容许 Y 非闭、距离下确界未达到的情形。常数选到足以容纳端帽、margin与所有横向坐标；选 Q 的平凡阈值足够大后 e'≤L≤1，e'≥e。若 P'(t₀)=0，只是切线段缩为点，仍可用任意方向、同样长度的 tube 外罩；不影响 upper。

用 N_{e'}(Y∩tube) 个半径 e' 球覆盖其中所有 witnesses。每个球经 N_{2e} 扩张后，只能装下 (4) 所计的 ≤C e/(αRd) 个样本像。由(5)得

    N_e'(Y∩tube)
       ≥ c (θu/d)(αRd/e)
       ≥ c_D,m θ^D sqrt(Q).                  (6)

这里每个样本选择任意一个真正 Y-witness 即够；不要求 witnesses 等权、独立或不同。有限cover若无最小值，取近最小cover，常数不变。

## 5. 与 tube-KT 比较

PCT-input 在同一个 e'、L 上给

    N_e'(Y∩tube) ≤ K(L/e')^{1−γ}
                   ≤ C_D,m K Q^{(1−γ)/2}.

和(6)合成

    Q^{γ/2}≤C_D,m K θ^{-D}.

加大只依赖 D,m 的 C，同时覆盖 Q 小、d≥cθ 与 R=0 的情况，得到(PCT)。没有假设 Y 具有 AD lower，也没用任意 source 曲线的二阶光滑性；光滑和二阶导数 bound仅来自此处实际 polynomial 的固定次数。

## 6. Source 使用前必须支付的接口

本结论适用于向量 cubic，直接在原 physical Y 尺度应用可以保原 tube-KT 常数。实际 z-window 先只归一化 domain：d=δ/ρ；需要先验证完整 polynomial window 的 R≤1 与 e≥dR，而非只在离散 B 上有小值。不同于 source22.4 scalar interval，(6)使用原 tube-KT 的真正新几何输入，适用于二维乃至固定维数向量值。

PCT给 R≤δ^{-O(θ_loss/γ)}e 时，1/γ 的费用必须包括在稳定化 η_j、φ/time-gap删选、Δ吸收和19.4参数中。若只拿到 vector cubic lemma 而未核实际 graph/精确 Y/非零 r/全 tildef 慢变，就仍未证明 quadratic alternative。准确 source 审计与 conditional theorem 另存本轮文件。
