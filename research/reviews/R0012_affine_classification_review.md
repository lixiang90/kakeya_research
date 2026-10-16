# R0012 独立审查：codimension-one 空间仿射 lift 分类

2026-10-17。审查人：`lifting_obstructions`。主对象为 `notes/20_dimension_lifting/curved_lifting/R0012_root_affine_classification.md`；另逐步交叉核查 `R0012_affine_lift_obstruction.md` 的主不可能证明。已读本地 Nadjimzadah v1 Definition 2.1、Proposition 2.5(i) 及本轮 spec。结论：两份证明通过，无需数学修正；root 的自然必要充分分类也通过。内部独审，不等于外部同行评审，不声称文献新颖性或重大结果。

## 1. 从 arbitrary smooth data 得到同一常数右逆

对完整 w 平移族求导，Θ 独立 w 确实给 T(t)A₀=I_m，其中 A₀ 只取同一个固定内部参数点的 ∂_w a。因此它与 t 无关，并且 rank A₀=m。选 k∉im A₀，L=[A₀,k] 是常数 GL_(m+1)；T(t)L=[I_m,h(t)] 对全部时间成立。

这个变换同时把 a、Θ 左乘 L⁻¹，保留 a+tΘ 的直线形式、原 t、Θ 的 w-独立性及 direction rank。没有使用逐时间改变的 lifted coordinates，也没有先假定 T 的特殊形式。任选这样的 k 即可，不必要求 k∈ker T(0)；后者只是我独立推导采用的额外方便正规化。

只在一个方向满秩点取 y、ρ 导数合法。原数据可对参数任意非线性，所有参数导数在该点为固定数值；T(t) 必须对它们的所有时间恒等式同时成立，足以施加必要条件。c(t) 在这些导数中完全消失，不需要设为0。

## 2. 无除法消元式 (8)：次数、外积及退化情形

记 a_y=[C;r]、Θ_y=[D;ℓ]、aρ=[p;u]、Θρ=[q;v]。维数逐项正确：h、p、q 为 m×1，r、ℓ 为1×m，u、v 为 scalars。因 coherent ruling 的 RHS 不依赖ρ，得到

\[
 F=C+tD+h(r+t\ell),\qquad
 0=p+tq+h(u+tv).
\]

以 scalar u+tv 乘第一式、用第二式消元，root (8) 精确为

\[
 (u+tv)(tI_m+t^2B)
 =(u+tv)(C+tD)-(p+tq)(r+t\ell).
\]

右边次数至多2，左边 t³ 项为 vB。整个消元从未除 u+tv，对个别时刻为零完全有效。若 u+tv 恒零，则 u=v=0，第二式再给 p=q=0，Θρ=(q,v)=0 违反 full direction rank。因此在 B≠0 时，vB=0 迫 v=0，而 u 必非零。

t² 系数是 uB=−qℓ，符号与 scalar/matrix 乘法顺序均正确；所以 B≠0 时 rank B=1。这个结论已足以排除本轮 diag(1,2)。对任一非退化时间区间的 polynomial identity 都可比较系数，不要求该区间包含0；root 稍强的时间表述并没有偷用原点。

## 3. 行列式 (12) 的独立核对

t 项给 uI_m=uD−pℓ−qr，即 D=I_m+(p/u)ℓ+(q/u)r。full direction Jacobian 为

\[
 J_\Theta=\begin{pmatrix}D&q\\\ell&0\end{pmatrix}.
\]

先对上面 m 行减去 (p/u) 倍最后一行，得到上左 I_m+(q/u)r；再将前 m 列各减最后一列乘对应的 r_j/u，得到

\[
 \begin{pmatrix}I_m&q\\\ell&0\end{pmatrix}.
\]

两步都是 determinant1 的 elementary operations。Schur complement 为 −ℓq，故 det JΘ=−ℓq。由 B=−qℓ/u，u tr B=−ℓq，root (12) 的系数和符号均正确，对任意 m 成立，没有遗漏奇偶符号。

fullrank 迫 trace B≠0。rank-one B 满足 B²=(trace B)B，所以必要条件恰为 rank B=rank B²=1。非零 rank-one nilpotent 时 trace B=0，方向 Jacobian 必奇异；不能把标准 lift 的 direction loss1 删去。

我另从 T=[I,g(t)]、g(0)=0 的独立正规化得到 g=t k/(1+βt)，继而 B≠0 迫 β=0、B=kℓ，方向 determinant 为 a₃ρ·tr B；与 root 无除法计算一致。该复核不依赖仅测试标准构造。

## 4. B=0 与 rank-one 的充分构造

B=0 时，T=[I_m,0]、a=(w,0)、Θ=(y,ρ) 直接满足 coherence，DΘ=I_(m+1)。π 忽略最后一坐标不妨碍 slope fullrank，Definition 2.1 允许这种自由 ruling；不能错误排除此分支。

若 B=xℓ₀ 且 ℓ₀x≠0，root (13) 给

\[
 T=[I_m,t x],\quad a=(w,\rho),\quad
 \Theta=(y-x\rho,\ell_0y).
\]

展开恰为 w+ty+t²By，rank T=m。其 direction determinant 为 ℓ₀x=tr B，非零，(14) 正确。取紧参数小球及合适 open Ω 即满足 source 的 line containment/coherence；若同时以 source 的 Hörmander-type X_B 为背景，取含0的足够小时间区间，使 I_m+2tB 可逆即可。上述代数 lift identity 本身对任意时间成立。

所以 B=0 或 rank B=rank B²=1 的必要充分分类已完整覆盖；并非仅必要条件加尚未核验的候选构造。

## 5. 对方主证明及范围交叉检查

`R0012_affine_lift_obstruction.md` 的 (2.2)–(2.10) 是同一主障碍的独立无除法证明，使用更弱前提 Θρ≠0：其 d(t)=r_v+t s_v 消元、t³ 系数 s_vB、先得 s_v=0 再证明 r_v≠0 的顺序均正确。仅在已得非零常数 r_v 后除法，不遗漏分母退化。随后 β(t) affine，二次系数 B=β₁V_v 为外积，确实排除 rank B≥2。该稿未声称 rank-one 完整分类，与 root 的额外自然分类不冲突。

两稿都正确保留全部实质条件：Θ 独立 w、整个ρ域投到同一曲线、空间仿射、原时钟。若 Θ 依赖 w，则共同右逆不再推出；若只对一张 selector w(y) 或单个ρ拟合，则相关参数微分不再合法；一般 nonlinear π 也不由同一 T(t) 描述。没有越界否定这些类。

标量 B=bI_m、b≠0、m≥2 的原时钟 codimension-one 情形被 rank≥2 排除，但 τ=t+bt² 可以在适当小区间把原曲线改为直线。它改变 clock，正是未覆盖的例外，不与分类冲突。source Proposition 2.2 的方向仍是线性 Kakeya 输入推出 curved 下界；本分类未给逆向 R⁵ Kakeya 推理或任何新维数界。

主任务及自然补充均已内部独审通过。按本轮停止规则，归档后停止该窄类的等价正规形与系数优化。
