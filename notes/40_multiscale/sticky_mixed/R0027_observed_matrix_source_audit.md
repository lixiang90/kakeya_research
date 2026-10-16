# R0027：actual ell3 observed matrix 图的源推导与质量审计

2026-10-17，子任务 A。已读 R27 macro/spec、R26 next target、恢复入口和 WZ §19.1、§21.1 的原公式。主任务是未付的实际 d5/k4/ell3 AFF₃，不能把 R24–26 条件分支的完成当作这个前端已证。本稿只编辑被分配文件，不提交，不重开冻结 Y-only 或抹 g 独立化路线。

**结论先记：** 原 W 可给实际 `A⊂R²_x×R²_ξ`、`N_r(A)≈K^±1r^-2`、保留全部原相关性的 bounded dense graph，以及正确矩阵平移。原 used-angle/slab 先验可支付；raw unused Φ_q 不能直接叫 slab。额外保留 normalized A 的 2-Frostman upper 和多尺度可见 x-fibre cover。本文没有由这些推出 >2 的增长或 AFF₃，也没有认证某个弱 finite 模型是原 source/Kakeya 反例。

## 1. 原文与对象

文献 `literature/primary/wang_zakharov_2026_sticky.pdf`，arXiv:2609.22035v1；行号为 extracted txt 按 `split('\n')` 编号。已逐行核：

| 原位置 | 本稿用法 |
|---|---|
| Def17.2，PDF65，3362–3381 | 原 Z、δ-separated points、f 的 dyadic Lip、Y_z AD、ξ/Φ coherence、fine witness。 |
| Def17.4，PDF66，3408–3433 | 实际 `f∈Mat(2,2)`；f=(u;v)，u,v row2；水平3-grain另有 scalar tildeY、`v=a+bu`。 |
| §19.1，PDF76–78，4033–4122 | 原 W 定义、19.1 计数、(148)–(153) 的实际路径恒等式。 |
| §21.1，PDF92–93，4844–4916 | 原 ell2 observed A、(170)–(173)、scalar ABC 的调用边界。本稿不把该 scalar proof直接视为 ell3 proof。 |
| Lemma19.5 与 R16/R22 已审接口 | 本尺度 Lip、合法 good-q 及原 weighted path averaging；不假任意 q 的局部 lower。 |

固定原合法 good-q，q 为 ρ-cube，原 times `Z_q`，`m=#Z_q`、`e=#E_q`。所有 T_p 每个 fine Φ_p-bin只取一个实际原 witness（O(1) 碰撞），保原 tube upper，不把 arbitrary extras计入度数。令 K 为有限固定小幂、最后相对目标指数选小。具名原 incidence/good-q 接口给

\[
m\ge K^{-1}\rho/\delta,\quad
e\approx K^{\pm1}m(\rho/\delta)^{4-\kappa},\quad
\#T_q\le K\rho^{-\kappa}(\rho/\delta)^4. \tag{1}
\]

每个保留 p 的 witness degree≈K^±1δ^-κ。原 R16 通过 weighted incidence Cauchy–Schwarz修补逐管 degree 不均匀的问题；不是每条管在 q 中都有 m 个 marks。原 W total lower 为

\[
W_{tot}\ge K^{-1}e\delta^{-4\kappa}\rho^\kappa m^2. \tag{2}
\]

E 的单时层 fine点上界维数为 4−κ：visible x维2，加原 ell-grain Y_z 维2−κ；水平3-grain没有被误写成新的2维Y。

## 2. 从两条原路径逐项得到 matrix translation

原 W 的起点 p 在 z₁，中点 p_i 在 z₂，两个终点 p_i′ 在 z₃。写

\[
p=(x,y+f(z_1)x,z_1),\quad
p_i=(x_i,y_i+f(z_2)x_i,z_2),\quad
p_i'=(x_i',y_i'+f(z_3)x_i',z_3).
\]

此处 x、φ、ξ、y 均为 R² 列，f 为 2×2。先由两段方向的共同点一致性：

\[
\xi_i=\xi_p+[f(z_1)-f(z_2)]\phi_i+O(\delta),\quad
\xi_i'=\xi_i+[f(z_2)-f(z_3)]\phi_i'+O(\delta).
\]

原 W 要求末管方向 ρ-close，故 `|φ₂′-φ₁′|≤Cρ`。相减得

\[
\xi_2'-\xi_1'=[f(z_1)-f(z_2)](\phi_2-\phi_1)
 +O(\rho\|f(z_2)-f(z_3)\|+\delta). \tag{3}
\]

再相减两条位置路径，末段差由 ρ-close 乘时间跨度ρ控制：

\[
x_2'-x_1'=(z_2-z_1)(\phi_2-\phi_1)+O(\rho^2+\delta). \tag{4}
\]

在终层 z₃ 用其 grain 表示减去 `f(z₃)Δx′`，得到原 (152)：

\[
y_2'-y_1'=(z_2-z_1)[f(z_1)-f(z_3)](\phi_2-\phi_1)+O(\rho^2+\delta)
=O(K\rho^2). \tag{5}
\]

因此两个终点位于同一终层、ell-grain label相差O(Kρ²)的厚桶；不是必须同一 exact grain。

令 raw `ψ=φ₂-φ₁`。本尺度 Lip 与 δ≪ρ²使 (3)–(4) 的两块误差均 O(Kρ²)：

\[
(\Delta x',\Delta\xi')=((z_2-z_1)\psi,-[f(z_2)-f(z_1)]\psi)+O(K\rho^2). \tag{6}
\]

这正是从 source 而非预设得到的矩阵作用。原印刷 (170) 的 ξ-block 与 (151) 相反；本稿不反射 ξ，直接保留 (6) 的负号。若取反射 observable，可改为正号，但须同步改 f，不能同时沿用两种约定。

## 3. 终层厚桶的 A-support：真 upper/lower 和 fibre

记 `σ=ρ²`（allowed 向上取整只多 K）。按第一终点的 z₃ 及 ell-grain y′∈R² 的 σ-cell Q分桶。每层至多 `K(ρ/σ)^(2-κ)` 个桶；这个 cover 来自全原 Y 的 AD lower/upper packing，不给 q 裁切后的 Y 重设 lower。每桶原点容量为

\[
P_Q=K(\rho/\delta)^2(\sigma/\delta)^{2-\kappa}. \tag{7}
\]

固定一原第一终点 p₁′ 的 W 恢复上界为

\[
K\delta^{-4\kappa}\rho^\kappa m^2. \tag{8}
\]

理由：反向选 T₁′、z₂、T₁、z₁、T₂、ρ-close T₂′，度数依次 δ^-κ、m、δ^-κ、m、δ^-κ、(ρ/δ)^κ；其各固定time交点只有O(1)。总所有桶的 P_Q upper≤Ke，由 (2)、(8)，可删 `e_Q<K^-B P_Q` 的轻桶只损原 W 小量。按 W_Q/e_Q 平均后，有一真实桶满足

\[
e_Q\ge K^{-C}(\rho/\delta)^2(\sigma/\delta)^{2-\kappa},\quad
W_Q\ge K^{-C}e_Q\delta^{-4\kappa}\rho^\kappa m^2. \tag{9}
\]

固定该 z₃、厚 y 桶，定义实际 observed support

\[
A_{phys}=\{(x',\xi_{p'}):p'=(x',y'+f(z_3)x',z_3)\in E_q,\ y'\in Q\}.
\]

固定一个 visible x 的 σ-cell，其实际终点全在 O(1)/K 个物理 σ-cubes内（y厚σ、f bounded）。ξ-coherence遂给 joint `(x,ξ)` 的 σ-cover≤K。x在 q中占 side Oρ 的二维box，所以

\[
N_\sigma(A_{phys})\le K(\rho/\sigma)^2. \tag{10}
\]

每个 jointσ-cell含原终点最多 `K(σ/δ)^(4-κ)`；由 (9) 又得 lower

\[
N_\sigma(A_{phys})\ge K^{-C}(\rho/\sigma)^2. \tag{11}
\]

这没有把 exact x 免费视作唯一 ξ。不同厚 y、不同物理dyadic cube均可能给多值；只证明付费 coarse fibre cap。也没有推出跨所有dyadic边界的 Euclidean Lipschitz 延拓。

取常数倍扩大的厚桶作为 output A_out，(5) 保第二终点在内；其 upper 只多 K。input (11) 给 output/input ratio≤K^C。可合并 input/out为同一个 A，graph density再付K。

## 4. 原 used-angle law：先删除 light cells，再允许 product reference

raw Φ_q 包含 unused coarse cells，单凭它的 κ-AD不能推 slabγ。用原实际 initial incidences定义

\[
\beta={1\over e}\sum_{p\in E_q}{\rm Uniform}(\Phi_p),
\]

再推至 ρ-cells c。原点的 Φ_p slabγ给 `β(slab_r)≤K r^γ`，r≥Cρ；κ-AD upper给 `β_c≤Kρ^κ`。coherence给 used carrier cell数≤Kρ^-κ。

固定原初点 p 和一条原初管 T₁，W恢复 upper为

\[
K m^2\delta^{-3\kappa}\rho^\kappa. \tag{12}
\]

选 z₂、T₁′、z₃、T₂、ρ-close T₂′即可；除总 (2) 得 W 的每个初角边际被 Kβ支配。对第二初角同理。因此删 `β_c<K^-Bρ^κ` 的 light used cells，总 W 损≤K^(C-B)；可以在第3节选厚桶之前做，后续 upper均不增加。

剩余 used set H满足

\[
K^{-C}\rho^{-\kappa}\le\#H\le K^C\rho^{-\kappa},\qquad
{\#(H\cap slab_r)\over\#H}\le K^C r^\gamma\quad(r\ge C\rho). \tag{13}
\]

证明 upper：每cell β_c≥K^-Bρ^κ，故 slab内cell数≤β(扩大slab)/(K^-Bρ^κ)，再用 H card lower归一。base以下只能 clip，不宣称同公式一直到0。其差 law

\[
\pi=(\phi_2-\phi_1)_*\big({\rm Uniform}(H)^2\big)
\]

也有同类 slab upper，因固定 φ₁ 后是 H 的一个平移 slab。

这里不是声称原 W 的角 pair独立，或 g 的角边际是 π；product law只是bounded graph的 dominating reference。真实所有相关性都继续由 g携带。

## 5. W-code 的完整恢复表：ell3 没有多损一个ρ幂

厚桶固定后，code为 `(a_σ,z₁,z₂,c₁,c₂)`，a_σ为第一终点 actual jointcell、c_i∈H为两初角的ρ-cell。给定code，原W重数upper：

| 原恢复选择 | upper |
|---|---|
| p₁′ 在其 x-cell、厚 y 桶 | `K(σ/δ)^(4-κ)` |
| T₁′及其 z₂交点 | `Kδ^-κ`，交点O(1) |
| T₁在已给 c₁内及其 z₁交点 | `K(ρ/δ)^κ` |
| T₂在已给 c₂内及其 z₂交点 | `K(ρ/δ)^κ` |
| ρ-close T₂′及其 z₃交点 | `K(ρ/δ)^κ` |

故

\[
P_{code}\le K(\sigma/\delta)^{4-\kappa}\delta^{-4\kappa}\rho^{3\kappa}. \tag{14}
\]

与 (9) 相除，得到 positive codes 至少

\[
K^{-C}(\rho/\sigma)^2\rho^{-2\kappa}m^2.
\]

这恰匹配 reference frame `A_σ×Z_q²×H²` 的大小：`#A_σ≈K^±C(ρ/σ)²`、`#H≈K^±Cρ^-κ`。按每 code 的原数除 P_code，得到同一frame上的 `0≤g≤1, mean g≥K^-C`。这逐项支付了 dense observed graph；不能仅由 source一句 “using19.1” 免费换产品先验。

初角从原fine φ换到 c_i-centre的误差Oρ，乘 Oρ time或f差即 O(Kρ²)，所以每 positive code仍满足 (6) 的同级误差。没有为 exact fine角 pair声称 dense slice。

## 6. 同步 L_f 与正确的矩阵 observed 公式

取 `1≤L_f≤K^C` 同时控制 M及q中ξ振幅。选实际中心 `(x₀,ξ₀,z₀)`，定义

\[
a=\left({x-x_0\over\rho},{\xi-\xi_0\over L_f\rho}\right),\quad
t={z-z_0\over\rho},\quad
M(t)={f(z_0+\rho t)-f(z_0)\over L_f\rho}. \tag{15}
\]

没有反射ξ，所以由 (6)，以 t=z₂、s=z₁ 的normalizedtime记号，真实平移为

\[
a'=a+\big((t-s)\psi,-[M(t)-M(s)]\psi\big)+O(K\rho). \tag{16}
\]

M为2×2矩阵。两块都在固定bounded box；不能只把 M除 L_f、却仍把 observable ξ只除ρ后声称 (16)。这就是原印刷(172)的 L_f mismatch在矩阵情形所需同步修复。原 (170) 的反号问题与缩放问题独立。

取 working `r=C K₀ρ` 吸收明确的误差。A、H的ρ-cells在r重新分箱，每个r-bin至多K个旧cells（固定 ambient维数、K₀固定小幂）；graph 聚合只多付K。写 `N_r(A)≈K^±C r^-2` 与 `≈K^±Cρ^-2` 等价，不能把 r/ρ 的费用叫固定常数。

## 7. 原 observable 真正保留的额外约束

除 base cover 外，对每个 R≥r 及 visible x 的 R-cell Q_R，都有

\[
N_R\big(A\cap\{x\in Q_R\}\big)\le K^C. \tag{17}
\]

原物理x-cell宽Rρ，terminal厚y宽Kρ²≲Rρ；其图只需O(1)/K个物理Rρ-cubes，ξ-coherence逐cube控制，allowed向上取整付K。这是多尺度 **cover fibre** 约束，不是全局单值或 Euclidean Lip。

特别由base纤维上界及 `#A_r≥K^-Cr^-2`，Uniform(A_r) 的 ball cap为

\[
\mu_A(B_R)\le K^C R^2\quad(R\ge r). \tag{18}
\]

即真实normalized 2-Frostman upper。它并非任意裁切后 A 的AD lower。root的新matrix增益候选至少可以保 (17)–(18)，弱finite反例若不满足这些不能称已覆盖实际接口。

水平3-grain还给终层label关系：若 `f=(u;v)`、`tildef=(a,b)`、`v=a+bu`，则两维ell-label `(y₁,y₂)` 的scalar横向label是 `η=y₂-b(z)y₁`。但这不推出固定厚桶中 `ξ₂-b(z)ξ₁` 与x无关。原定义允许该offset依原point变化；“同grain所以offset常数”不是可用新关系。

原(152)的两终端label接近已经用于厚桶；原(153)还保 terminal-close方向与 `Δf ψ` 的关系，但其方向都被原W约束，不能把它另当一个独立 slab样本。本文未从这些事实导出更强的 rank2、共同kernel排除、保质量的矩阵逆定理或 >2 增长。

## 8. fine time到coarse matrix graph：需要真实 heavy lower

normalized fine times spacing为 d=δ/ρ。把 `(t,M(t))∈R×Mat(2,2)` 按r-cells聚合。一个time-r interval在原物理rρ尺度只遇O(1)相邻 allowed cells；每个内部使用dyadic Lip，向上取整及4个matrix坐标只多付K。于是

\[
n_b\le P=K r\rho/\delta,\quad
\#\{b\text{ cells over one time-r cell}\}\le K,\quad
\#B_c\le K/r,\quad m/P\ge K^{-C}/r. \tag{19}
\]

fine g两time fibres求和除P²，并除 A/H合并的有界K重数，给 coarse boundedgraph，mean≥K^-C。单有 upper capacity不能把原nonfit传到uniform B_c。删 `n_b<P K^-B` 的light matrix-graph cells，所删原fine质量≤`#B_c P K^-B≤K^(C-B)m`；用 fine g≤1先支付loss。余每cell occupancy两侧K可比，所以 coarse事件的质量可由其完整fine-preimage质量以K固定幂控制；只对已支付增厚误差的interval/Euclidean事件或第9节D事件使用。这里不免费继承任意斜率matrix vertical-affine nonfit。

每保留 coarsecell取一个真实原 `(t,M(t))`代表；差 M及time都只改O(r)，故 (16)只增O(r)，不需global Euclidean Lip。若round clock另换值，必须说明误差/是否继续all-real非fit；本步只用实际graphcell代表。B_h有normalized1-Frostman upper与每timecell≤K个matrixcells，未称它是单值Lipschitz延拓。

## 9. whole matrix nonfit到新的 affine-2plane translation cap：source接口

设同window原whole f对所有Mat(2,2) affine `Rz+U` 在precision `ρ^(1+ε₀)` 下最多占 a_phys 原times。good-q的**原 fine-label law**中，M在

`h₀=ρ^ε₀/L_f`

精度有fit upper `a=K^C a_phys`。这里不声称 uniform coarse B的任意斜率 vertical-band nonfit已免费继承：time舍入可产生未知 `|R|r` 误差。以下plane结论应先在fine label law应用，再传实际 D的O(r)误差。不能从scalar projection nonfit反推whole matrix nonfit。

root本轮另证的finite plane lemma输入是 ν interval cap、M bounded且wholematrix h-affine nonfit≤a、原差角π slabγ；输出对

\[
D(t,s,\psi)=((t-s)\psi,-[M(t)-M(s)]\psi)\in R^4
\]

任意affine2-plane的宽h⁴ neighborhood有产品reference质量 upper `a+C K_t h+C K_πh^γ`，查询不足base时需clip。其两分支代数初核：orthonormal normal `Q=(A,B)`，若σ_min(B)≥h²，乘B⁻¹后余矩阵≤h只占a，其余用widthh的角slab；若σ_min(B)<h²，取小left singular向量使wA有常数下界，删timegap<h付K_t h，其余再用角slab。这个finite结论的独立证明/审查由root/B完成，本稿不把它直接写成加法增长定理。

实际source可选 `h=ρ^(2ε₀)`，令L_f loss≪ε₀，则h<h₀；先取ε₀<1/16，再取loss小，有

\[
r=K\rho\ll h^4=\rho^{8\epsilon_0},\quad
q_{base}=C\rho\ll h,\quad d=\delta/\rho\le\rho^3\ll h. \tag{20}
\]

所以该plane cap不含非法sub-base查询。coarse D相对fine D改O(Kr)，远小h⁴，可先在fine law证cap再以常数厚化传给coarseframe。具体地，某个coarse D落plane neighborhood时，它的全部fine preimages也落固定倍增厚neighborhood；每time cell的真实occupancy在P K^-B与P之间，故uniform coarse product law可由原fine product law以K^C支配。angle进一步聚合的碰撞数≤K、非空cell至少一个原H点，也只多K。这样继承的是D事件，不是未经证明的arbitrary-slope M-band。若要把任意coarse affine-fit nonfit直接当fine nonfit，仍须处理未知slope times舍入误差，不能仅写O(r)。

在原 bounded g的normalization下，任意事件最多再付 mean(g)⁻¹≤K^C；有固定positive指数时可吸收。这不使 g独立，也不自动证明 `N_r(A)>r^-2`。

## 10. 结论与停止边界

逐项已付：actual ell3 W的两块位移与grain label厚化；原endpoint/angle/tuple恢复；used角slab而非rawunusedΦ；dense boundedg的真实frame；A≈r^-2及2-Frostman/多尺度fibre；正确负号和同步 L_f；heavy time lower与新增plane-cap的合法source尺度。

scalar Theorem21.2仍只给scalar multiplier的约 `r^-1-κ`，κ≤1时不足越过A的2维upper。原Remark21.3也不把R²角作用变成一个scalar multiplier。新的 affine2plane非集中仅是更精确的实际可用输入，本文没有从它得到 wholematrix AFF₃；若所需matrix增长必须用新定理，应保持未付，不靠重新命名冻结Y-only或抹g独立化。

whole time限制闭包仍用R22并保原T/每层数据，不给管子子族或空间patch重设ADlower。高级原source计数与完整WZ/四维证明的未审范围仍保留。无完整五维/一般Kakeya结论、真实反例、维数改进或重大性认证。
