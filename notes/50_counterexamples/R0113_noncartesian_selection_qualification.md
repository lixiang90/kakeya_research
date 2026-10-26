# R0113：任意 Borel 三角截距耦合的共同 clock 反攻

2026-10-26。constructive_gate 分工，仅编辑本文件，不提交 Git。新候选是共同 clock 上真正非 Cartesian 的**前缀截距耦合**。下面支付原平均 marks 的势能删选与逆序积分，并给不经邻域倒推的有限管版本。它严格排除该指定构造类的固定正幂降维；不证明普通高维 Kakeya，不声新颖或重大，不立新 ID，未经外部同行评审。root 提供的定量势能机制在本稿被逐式核验；本稿不以此自认该机制的独立审查。

## 1. 恢复、精确候选与停止条件

实际读 GOAL、STATE、R112 next；定向回读 R41 的 Cartesian 全组合/共同 clock、R47 的 rough cycle 停止门、R83 的 acyclic proper 类冻结，以及首轮 `projection_slicing/首轮障碍与严格命题.md` 中 LIFT-003、LIFT-004、LIFT-NEXT-01。没有重跑 context、旧有限算例或下载。

固定 (m=n-1\ge1\)。对每个 (i=1,\ldots,m\)，给任意有界 jointly Borel 函数
\[
 f_i:[0,1]^i\longrightarrow[-M,M],\qquad
 F_t(v)_i=f_i(v_1,\ldots,v_i)+t v_i. \tag{1}
\]
定义真实评价 (X(v,t)=(F_t(v),t)\)，(0\le t\le1\)。不假设连续、单调、BV、可微、可逆或几乎处处 Jacobian。各 (f_i\) 可以真实依赖全部前缀；例如 (f_2(v_1,v_2)=v_1v_2\) 不满足 R41 截距逐坐标分离。

可证伪候选为：这种任意 rough 前缀耦合，是否能在同一个全方向单位段集合中产生严格 Hausdorff 上界，或者在完整方向网及任意原 marks 下产生固定幂体积压缩？本稿给出否定该构造机制的精确证书；不是先假欲证 joint-law。若证明须交换未付的好基点维数、把不同 clock 拼接或免费丢原 marks，立即停止；以下证明不使用这些步骤。

## 2. 旧闭包与真正新增的责任

R41 假设所有 Cartesian combinations 的第 (i\) 个截距只依赖第 (i\) 个 slope，故每个 clock 的 slice 本身是坐标乘积。本稿的 (1) 一般不具有这种 slice 乘积结构。R47 是闭环互相依赖；本稿的依赖有确定前缀次序，**不**把其未解 rough cycle 估计重新命名。R112 的 LW 参数 Cartesian 例亦不用于本证明。

首轮 LIFT-NEXT-01 曾提出 Borel 平面 graph 的好 clock 纤维，但未支付好投影基点的四维质量。本稿先考虑的条件测度/维数混合方式确会遇到这个责任；最终改用下文的**同一原参数先验、统一坏路径预算及逆序积分**，直接给物理 Frostman 质量。因此不以“每个前缀 a.e. 好”免费改成每个物理基点好，也不引用未证的维数相加公式。

本稿没有证明任意 ordinary 截距 selector 能用保原集合、保原质量的变换变成 (1)。这是其与完整目标之间的真实限制，不能把本类的完整解误报成一般维数 gain。旧 CP/PM/PW4 全称正幂闭包不赋予这个三角结构；反向，本类结论也未推出那些全称目标。

## 3. 标量势能的统一估计与可测性

固定 (0<s<1\)，定义一维概率
\[
 \mu_{i,u,t}=(w\mapsto f_i(u,w)+tw)_\#(1_{[0,1]}dw),
 \quad u\in[0,1]^{i-1},
\]
\[
 U_s\mu(x)=\int |x-y|^{-s}\,d\mu(y),\quad
 I_s(\mu)=\int U_s\mu\,d\mu. \tag{2}
\]
势能可取 (+\infty\)。因为 (f_i\) jointly Borel，(2) 的所有被积函数为非负 Borel，Tonelli 适用；((u,t,x)\mapsto U_s\mu_{i,u,t}(x)\) 为 extended Borel。无需可测反函数或连续 selector。

对 (w\ne w'\) 及任意实 (A\)，
\[
 \int_0^1 |A+t(w-w')|^{-s}dt
 \le C_s|w-w'|^{-s}. \tag{3}
\]
证明是提出 (|w-w'|^{-s}\)，平移长度 1 的区间后，(|t|^{-s}\) 的积分由穿过 0 的区间控制。对角 (w=w'\) 的二维 Lebesgue 测度为 0。故对每个固定 (u\)，
\[
 \int_0^1 I_s(\mu_{i,u,t})dt
 \le C_s\int_0^1\!\int_0^1|w-w'|^{-s}dw\,dw'
 \le C'_s. \tag{4}
\]
常数统一于全部 (i,u,f_i\)；有界性只供物理集合有界，不是 (3) 的输入。

## 4. 任意原 marks 的全球删选：只花原 \(\lambda\)

令 (Z\subset[0,1]^m\times[0,1]\) 为任意 Borel 原 marks，
\[
 |Z|=\lambda>0. \tag{5}
\]
对原路径 ((v,t)\)，第 (i\) 项好条件为
\[
 U_s\mu_{i,v_{<i},t}(F_t(v)_i)\le T.
\]
沿原完整参数先验 (dv\,dt\)，其左边积分恰为 (4) 对 (u\) 的平均；未来坐标和其余前缀概率均积分成 1。取
\[
 T=2m C'_s/\lambda,
\]
Markov 加 union bound 给所有坏路径之并的质量至多 \(\lambda/2\)。因此
\[
 Z_*:=Z\cap\bigcap_{i=1}^m\{\text{第 }i\text{ 项好}\}
 \quad\text{有}\quad |Z_*|\ge\lambda/2. \tag{6}
\]
这是原完整先验上的坏集预算；没有给每个前缀另归一化，更没有把每前缀的坏概率再乘成不存在的独立事件。(Z\) 只需平均质量，原每条参数线可以有不同、甚至零 marks。

## 5. 同一物理测度的逆序积分与全维结论

令 \(\sigma=X_\#(1_{Z_*}dv\,dt)\)。其总质量至少 \(\lambda/2\)，且真来自原 marks。若一维区间 (J\) 长 (r\) 并有一个好输出点 (x_0\in J\)，则
\[
 U_s\mu(x_0)\ge r^{-s}\mu(J),\qquad \mu(J)\le T r^s. \tag{7}
\]
若 (J\) 没有好点，其 good pushforward 质量为 0。由存在一个好点得到 (7) 只作数值不等式，不需要选择该点的可测函数。

对物理坐标盒 (Q=J_1\times\cdots\times J_m\times J_t\)，各区间长不超过 (r\)，先在 (\sigma(Q)\) 的积分中丢掉 (1_Z\)，再从 (v_m\) 逆序到 (v_1\) 积分。固定 (v_{<m},t\) 后，第 (m\) 项给 (Tr^s\)，其他行的函数与好条件均不依赖 (v_m\)；于是可提出该常数并继续。这正是前缀结构的实际用途，不要求输出 prefix 单射。最后对原 clock (J_t\) 积分，得
\[
 \sigma(Q)\le T^m r^{1+ms}. \tag{8}
\]
所以任何覆盖原物理 marks (X(Z)\) 的球族均有
\[
 \sum_j r_j^{1+ms}\gtrsim_{m,s}\lambda/T^m
 \gtrsim_{m,s}\lambda^{m+1}. \tag{9}
\]
这是正的 Hausdorff content 下界，不是 upper、单值 graph 的参数维数或仅一个 clock 的碰撞。令 (s\uparrow1\)，得到
\[
 |Z|>0\quad\Longrightarrow\quad \dim_H X(Z)=m+1=n. \tag{10}
\]

不必另外调用有潜在量词问题的 disintegration 维数加法引理。(7)–(8) 直接支付旧计划所缺的物理质量；也是对 root 势能机制的逐式核验。(X(Z)\) 为 analytic，故所用完成测度合法；(9) 本身也能直接对任意球覆盖积分，不需要把 analytic 像冒称 Borel。

每个原生成段 (t\in[0,1]\) 长度至少 1。若只取准确单位段，令 (T(v)=(1+|v|^2)^{-1/2}\)，保 (0\le t\le T(v)\)。这些单位段仍共同包含 (0\le t\le(1+m)^{-1/2}\)，参数 marks 质量为正，故其**同一个**并集也满维。slope cube 对应固定开角度 patch，固定有限旋转补齐全部方向仍满维。任意取紧闭包亦满维，不产生严格低维反例。

## 6. 有限方向表与实际横截 marks：精确模型

仅由 step extension 得 \(|N_\delta E|\) lower 不能回推任意可测 \(|E|\) lower。以下给出直接支持于原 (E\) 的有限版本，消除这个桥的风险。

取整数 (K\ge2\)，\(\delta=K^{-1}\)，原 (N=K^m\) 个方向标签 (k\in\{0,\ldots,K-1\}^m\)，slopes (v_i=k_i\delta\)。每个前缀给任意实表 (a_i(k_1,\ldots,k_i)\)，无连续插值假设。固定 (h>0\) 和固定长度 clock 区间 (J\)（如 ([-1,2]\)），真实物理圆柱为
\[
 T_k=\{(a(k)+tv(k)+b,t):t\in J,\ b\in[-h\delta,h\delta]^m\}. \tag{11}
\]
这是有水平横截面的实际直轴圆柱，体积 \(V=|J|(2h\delta)^m\)。令任意可测 (Y_k\subset T_k\)，\(E=\bigcup_kY_k\)，原 incidence 与平均密度为
\[
 I=\sum_k|Y_k|,\qquad \lambda=I/(NV). \tag{12}
\]
原先验为独立 uniform (k\)、uniform (t\in J\)、uniform (b\in[-h\delta,h\delta]^m\)；每个标签的评价 Jacobian 对 ((b,t)\) 恰为 1，所以 marks 的原先验质量就是 \(\lambda\)。标签间物理重叠不去重、不丢 incidence。

固定 (i,k_{<i},t\)，把标量概率改为
\[
 \mu_{i,k_{<i},t}=
 K^{-1}\sum_{j=0}^{K-1}\operatorname{Unif}
 [a_i(k_{<i},j)+tj\delta-h\delta,
   a_i(k_{<i},j)+tj\delta+h\delta]. \tag{13}
\]
其时间平均 (s\)-energy 统一有界：同一 (j\) 的 diagonal 总贡献为
\(O(K^{-1}\delta^{-s})=O(\delta^{1-s})\)；不同 (j,j'\) 先对 (t\) 使用 (3)，再求和
\[
 K^{-2}\sum_{j\ne j'}|(j-j')\delta|^{-s}\le C_s.
\]
任意实截距和横向位移之差都只改变 (3) 的 (A\)。固定 (J,h\) 只进入常数。全部对象是有限和/非负 Borel 积分，可测性无新增缺口。

## 7. 直接物理密度界：原平均 shading 的体积 lower

对 (13) 的密度 \(g(x)\)，所有包含 (x\) 的长度 (2h\delta\) 小区间都落在 \([x-2h\delta,x+2h\delta]\)。故
\[
 U_s\mu(x)\ge (2h\delta)^{-s}
 \mu([x-2h\delta,x+2h\delta])
 \ge (2h\delta)^{1-s}g(x). \tag{14}
\]
边界 density 的选择无碍 a.e. 结论。于是 good 条件 (U_s\mu\le T\) 强迫
\[
 g(x)1_{\mathrm{good}}\le C_{s,h}T\delta^{s-1}. \tag{15}
\]

仍取 (T=C_{m,s,J,h}/\lambda\)，原平均坏路径总量至多 \(\lambda/2\)，实际 marks 上保质量至少 \(\lambda/2\)。把保留原先验推到物理，固定 (x,t\) 写其 Lebesgue density：对所有 (k\) 求和，乘各坐标小区间 density、good indicator 及原 (1_{Y_k}\)。只为 upper 丢 (1_{Y_k}\)，然后按 (k_m,\ldots,k_1\) 逆序求和；每一步恰是 (15)，不要求各输出或 good 事件独立。得到
\[
 \rho_*(x,t)\le C T^m\delta^{-m(1-s)}. \tag{16}
\]
这一个测度支持在真实 \(E\)，而非其邻域。因此
\[
 \boxed{\ |E|\ge c_{m,s,J,h}\lambda^{m+1}
                    \delta^{m(1-s)}\ }. \tag{17}
\]
量词统一于全部有限前缀表、全部原 marks、全部 (K\)。没有由某个实际集合体积 lower 倒置一份 upper certificate，也没有以大 collision 推小体积。

圆管应用需显式保几何：在 bounded slope chart 中，原单位轴的圆 \(\delta\)-管及端帽包含于固定倍宽的 (11)，取共同固定 (J=[-1,2]\) 即可；其体积与 (11) 均为固定常数乘 \(\delta^m\)。把原 (Y_k\) 原样放进外包圆柱，用 (12) 重算 \(\lambda\)，只改固定常数，(17) 仍直接约束原 \(|\bigcup Y_k|\)。此转移要求这些原轴的截距表确为前缀形式，不能给任意原管族免费添加该结构。

## 8. restriction、原分母和有限到连续边界

整个原 cube 参考有 (N=K^m\)，方向帽计数为固定 grid 上界，marks 平均密度是 (12)。保留 (qN\) 个 labels、(pI\) 个 incidence 后，按保留族重算的平均密度是 \(\lambda'=(p/q)\lambda\)；归一帽常数须除 (q\)。将删掉的 labels 在原 cube 内继续设零 marks，(17) 收费的是原 prior 的 \(q\lambda'\)，因而费用为 \((q\lambda')^{m+1}\)，没有免费变成仅 \((\lambda')^{m+1}\)。逐管 lower 可推出平均 lower；仅平均 lower 不授每管 density，更不授每前缀条件 lower。势能删选只用原平均质量。

连续 (9) 对任意原 Borel (Z\) 都成立，包括任意 whole-label restriction 或任意正总量、逐管不一致的 clock marks；这些删选不必保持全方向，故不声称删完仍为 Kakeya。有限版同样允许任意原横截 marks，不免费补满 pencil、CW 下界、filled (X\)、selected \(\xi\) 或完整 sticky source。

若取 (s=1-\varepsilon/m\)，则 (17) 给 \(|E|\gtrsim_{m,\varepsilon}\lambda^{m+1}\delta^\varepsilon\)。这确实排除完整前缀方向表的任意固定幂小 union（在近满 \(\lambda\) 的正确指数范围内），但不是普通全方向管族的无条件估计。不能把任意有限方向族填入 cube 时产生的 (q\) 损失，或非前缀截距冲突，藏进 normalization。

连续定理的证明直接由原 (dv\,dt\) 完成，并非用有限表的样本外推。反过来，有限 (17) 也没有依赖任意 Borel (f_i\) 的 step 近似与原 (E\) 邻域可比；其真实横截先验单独支付了该边界。

## 9. 反攻结果、独审边界与停止

本轮原候选允许真实非 Cartesian、任意不连续 Borel 前缀耦合；(9)/(10) 严格证明其同一集合满维，(17) 对完整 finite 方向网及任意原 shading 给统一物理体积 lower。因此“仅通过这类 rough 前缀依赖把维数压低”的尝试已被实质反攻，不是泛称尚缺 joint law。

这与 R41 逐坐标 Cartesian、R47 cycle、R112 LW、R83 acyclic 等旧对象的量词不同；但一般截距中存在双向/全向依赖，本稿没有消除它们。本轮不续 cycle、一般 graph 的 Jacobian、更多 anchors 或列一串成功公设。不以本类定理宣 ordinary (n\ge5\) 改善、Kakeya 反例、major 或 Goal 完成。

root 实际全文核验和另一代理的独立逐步审查仍须另行记录；本人核 root 的势能思路不冒为其自审以外的新 formal review。此稿仅作分配证明/反攻材料，不预认证后续公共状态、源比较、Git 或同步。
