# R0014：固定首边四环与 caustic 能量的交叉审查

2026-10-17。审查者 audit_four_dimensional。审查文件为 notes/40_multiscale/coupled_projections/R0014_joint_attack.md。

**结论：通过，可按当前限定范围归档。** 固定首边的四环二维方向平面约束和 caustic 的未截断 \(L^2\) 障碍均成立。没有发现必须修正的数学问题。它们没有证明或证伪 CP；未给足量 separated-time cycles，亦未排除允许保留原质量后修剪的能量路线。

## 1. Vandermonde 条件数与四环常数

对 \(G=[\gamma(s_1),\gamma(s_2),\gamma(s_3)]\)，\(\gamma(s)=(1,s,-s^2)\)，逆矩阵各行确为 Lagrange polynomial 的 coefficient vector，只在第三项改符号。nodes 间距至少 \(\rho\) 时 denominator 至少 \(\rho^2\)，numerator coefficients 被 \(1,2,1\) 控制，所以
\[
 \|G^{-1}\|_{2\to2}\le\|G^{-1}\|_F
 \le\sqrt{18}\rho^{-2}<5\rho^{-2}.
\]
这里 \(s_i\in[1/4,3/4]\)，常数有充分余量；没有把 determinant 下界 \(\rho^3\) 粗暴反演，也不要求时间的 cycle 次序与数值顺序相同。

单边 residual 的分解精确成立：
\[
 (\Delta b,\Delta d,\Delta f)=
 \gamma(t)\Delta b+(0,-r_1,r_2+tr_1).
\]
在 \(|r_1|,|r_2|\le\varepsilon\)、\(t\le3/4\) 时，单块 error 不超过 \(\sqrt5\varepsilon\)，双块不超过 \(\sqrt{10}\varepsilon<4\varepsilon\)。四边闭环给 combined residual 至多 \(16\varepsilon\)，故利用后三个时间的 \(G^{-1}\) 可得
\[
 \left(\sum_{i=2}^4|\eta_i|^2\right)^{1/2}
 \le80\varepsilon\rho^{-2}.
\]
Lagrange coefficients 在两个 blocks 中完全相同，因而
\[
 u_i=-L_i(t_1)u_1+\eta_i
\]
是一个真正联合的向量关系。它没有除以 \(|u_1|\)，因此首边很短不会引入未记录的逆角度成本。

若 \(u_1\ne0\)，每条 edge 的主要部分均在 \(S_e\) 中；加上最多三个 edges，把任一 vertex 移回 \(p_1+S_e\)，误差小于 \(500\varepsilon\rho^{-2}\)。\(q\) 是坐标删除和置换，不增范数，所以方向到 \(q(p_1)+W_e\) 的同一误差界成立。若 \(u_1=0\)，全部主系数都被 error 控制，确实得到半径 \(500\varepsilon\rho^{-2}\) 的球。未遗漏该退化情形。

## 2. 固定首边的方向 packing

原单位方向的分离经 bounded graph chart 给 raw slope \(q(p)\) 的固定倍 \(\delta\)-分离。一个有界四维盒内宽度 \(w\) 的 affine 2-plane neighborhood，常数倍 \(\delta\)-packing 的体积比较给
\[
 C_r\min\{\delta^{-4},\delta^{-2}(1+w/\delta)^2\}.
\]
取 \(w=500C\delta\rho^{-2}\) 得原稿式(4.2)。对于同一首边，\(u_1\) 固定，故 \(W_e\) 不随后两个 vertices 或其余时间变化；把所有 eligible cycles 的第三、第四 vertices 合并后仍能用同一 bound，而不是只能逐 cycle 使用。

\(u_1=0\) 的球也包含在任意经过 \(q(p_1)\) 的该宽度 plane-neighborhood 内，因此统一上界仍成立；球 packing 可以给额外改善。每方向只有一个 anchor 是从方向 packing 控制参数数量所必需，原稿已准确保留这个 graph 条件。

原 joint cell 的实际两点差满足式(3.1)，但该必要条件不会反向新增 shading participation。把 slab 内实际时刻移到 midpoint 只损固定倍 \(\delta\)，因为原 slopes 在固定有界盒。四个时间的 separation 仍是额外需证明的事件条件，原稿没有从 dense marks 免费获得它。

## 3. Caustic 数据满足原单位方向图输入

固定小四维 \(A\delta\)-grid 的方向数 \(\asymp\delta^{-4}\)，取 \(A\) 大固定可确保归一化方向 \(\delta\)-分离。anchors \(f=-\tau d,g=-\tau e\)、\(\tau=1/2\) 有界，且沿用原实际单位长度轴和共同时间 \(I\)。按坐标置换得到
\[
 \Pi_t p=(tX-Y,hY),\quad h=t-\tau,
\]
是精确等式，两块仍共享同一 \(t\)。

可以 full marks，也可保留 \(|h|\le\lambda\) 的全部原 indices。后者约有 \(2\lambda/\delta\) 个时间 slabs，因而密度 \(\asymp\lambda\)；固定常数可通过给门槛留指数余量或加固定窗口因子处理，原稿没有把未着色的新增几何交当原参与。

## 4. 未截断能量的上下界

最近 midpoint 满足 \(|h|\le\delta/2\)。此时 \(hY\) 占常数个二维 cells，\(tX-Y\) 占 \(O(\delta^{-2})\) 个 cells；由 Cauchy，该时刻的 energy 已至少
\[
 cN^2\delta^2\asymp\delta^{-6}.
\]

反向固定 index 的 close partners 满足每个坐标
\[
 |t\Delta X-\Delta Y|\le C\delta,\qquad
 |h\Delta Y|\le C\delta.
\]
每个 \(\Delta Y\) 坐标有
\(O(1+\min(\delta^{-1},|h|^{-1}))\) 个 grid choices；固定后因 \(t\ge1/4\)，\(\Delta X\) 坐标只有常数个 choices。两块相乘给每 index 的 partner bound
\(C(|h|+\delta)^{-2}\)。时间求和为 \(O(\delta^{-2})\)，故
\[
 E_2\le CN\delta^{-2}\asymp\delta^{-6}.
\]
同 cell collision 是上述 close partner 的子事件，upper 有效；lower 使用实际 cells，因此两边不混用尺度。

窗口内 \(S\asymp\lambda\delta^{-5}\)，所以对真实未截断 \(E_2\) 直接用 Cauchy 的数值是
\[
 S^2/E_2\asymp\lambda^2\delta^{-4}.
\]
它不支持一个统一固定幂改善的未截断 energy upper。这里的 \(\asymp\) 指该 Cauchy 表达式，而非把实际 union 声称为这个量。

## 5. 实际 covering 更大，修剪也保留原质量

每个单 coordinate block 的二维矩阵
\[
 (X_i,Y_i)\mapsto(tX_i-Y_i,hY_i)
\]
把 grid 映到有界 parallelogram。其 \(\delta\)-neighborhood 面积 \(\asymp|h|+\delta\)，给 covering upper；上述 partner bound 给 matching lower。两个 input grids 独立，输出是这两个集合的笛卡尔积，故
\[
 N_\delta(\Pi_tP)\asymp\delta^{-4}(|h|+\delta)^2.
\]
对窗口求和确得 \(\asymp\delta^{-5}\lambda^3\)，所以该构型不是 CP 反例。

删除 \(|h|<s\)、\(\delta\ll s\ll\lambda\)，只损 \(O(s/\lambda)\) 比例原 incidence；保留 energy 满足
\[
 E_{2,\mathrm{keep}}\le
 CN\delta^{-1}s^{-1}\asymp\delta^{-5}s^{-1}.
\]
从而 Cauchy 得
\(\gtrsim\lambda^2\delta^{-5}s\) 个 cells。取满足 \(\eta<a<1\) 的固定 \(a\)、\(s=\delta^a\)，与前述尺度条件一致；当 \(a+2\eta<1\) 时确有严格超过 \(\delta^{-4}\) 的增益。原稿只用它说明修剪路线未被排除，没有声称任意数据都允许同样修剪。

因此可归档的两项结果是固定首边的 separated-time 四环秩限制，以及原数据中 caustic 集中的未截断能量障碍。仍缺从任意原 dense selections 获得足量有效 cycles 或可保留低重数质量的估计，不能将该缺口改作新假设后宣布 CP 成立。
