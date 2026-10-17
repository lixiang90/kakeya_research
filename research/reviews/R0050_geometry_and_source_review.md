# R0050 正式独审：全时变分、完整 smooth lift 范围及旧记录纠正

2026-10-17，A。**通过 root/B 的已写全 class 结论、自然 codimension 推论、nonlinear 校准及宏观停止范围。** 此次更新既有 LIFT-005，不新增数学 ID，不是普通 R5/一般 Kakeya 界，也不认证新颖性或重大性；未经外部同行评审。

## 1. 实际全文审查范围及作者身份

已实际全文读 root 八节 `R0050_variational_equivalence_and_full_smooth_lift_classification.md`、B 六节 `R0050_nonlinear_lift_construction_counteraudit.md`、A 十节独立稿、当前结果页 `results/reviewed/LIFT-005_full_smooth_variational_classification.md`、本轮 macro 七节与 next 五节。

还实际全文重读了加更正 banner 的七份历史/开轮文件：R12 A/root/B 三稿、旧 `LIFT-005_affine_codimension_one_classification.md`、R49 next、R49 macro、R50 working_spec。旧证明正文保留为历史，显著 banner 明确其“非线性未覆盖/空间 affine 是实质限制”的判断已更正，且指向当前证明与结果页。

数学来源的实际读段包括已存 Nadjimzadah2609.06299v1 PDF4–9 的 quadratic 定义、Remark1.5、Def2.1、完整 Prop2.2 与 Prop2.5(i) 证明。2511.10918/GAFA00750-4 已正确分开。A 是沿固定基线第一变分这一观察的提出者之一；下文独审对象是 root/B 的实际模型、代数、构造及 current scope，A 自己的独稿不算第二个独立证书。

## 2. 同 P、全 t 的真正 variational lift：通过

在一个固定原参数内点 P，TP(t)=Dzπt(a(P)+tΘ(P)) 有定义且 smooth。对参数求一次导数时 t 固定，所以没有 π 的显式 t 导数或 Hessian 遗漏。三种参数导数确实共用同一个 TP(t)，而 aw、ay、aρ、Θy、Θρ 都在 P 固定，因此是与 t 无关的常矩阵。

原 coherence 对每个 t 成立，故导数恒等式

    TP aw=I，TP(ay+tΘy)=F(t)，TP(aρ+tΘρ)=0

在整段原 I 上同时成立。它们并非只在 t=0 的有限 jets。由这些式子的线性组合，新 a_lin=Da(P)u、Θ_lin=D(y,ρ)Θ(P)(uy,uρ)、πlin,t(z)=TP(t)z 对**全部新 u 和全部原 t**精确给 uw+F(t)uy。

TP aw=I 给每时刻 rank TP=m；新 Θ 的方向 rank 恰是原 P 的 rank，不发生 direction loss 变化。原 smooth π 在 compact 基线周围有开邻域，TP 可在 I 的邻域定义并保持满秩；新小 compact 参数域的所有线段可放入共同开域。因此它满足真正的 lift 定义，而不是只给必要 jet 系统或把每条线另配不同 π。

反向 affine 本就是 smooth 子类，故目标本来为 w+F(t)y 时存在性等价成立。任意 smooth F 的这条几何等价不需 Hörmander 假设；若调用 source Prop2.2 的曲线定理，还应保其原 Hörmander/compact-domain 输入。当前 quadratic 的小时间区间满足这些要求。本文没有推断原 π、a、Θ 本体必须线性。

## 3. general-s minor 下界及标准可达性：通过

aw 是固定 rank-m 右逆列组，可延长为**常数**可逆基 S。之后 TP S=[I,H(t)]，ay、Θy 的块 C,R,D,L 仍常数，于是

    P(t)=t²B+t(I−D)−C=H(t)(R+tL)，rank P(t)≤s.

s<m 时，任意(s+1)-minor 是在非退化区间恒为0的左边标量多项式，所以所有系数为0。其最高次数 2(s+1) 的系数确实为对应 B-minor：每个 determinant 项只能从每一因子的 t²B 部分取得该最高次数。故所有相应 minors 消失，rankB≤s。没有将仅 smooth 的 H 当作多项式，也没有用 t→∞ 或超出 I 的原 identity；s≥m 情形本来平凡。

source 标准 factorization B=UV（U injective、V surjective，q=rankB）给 s=q；其方向 Jacobian 的 kernel 是 {(h,k):h=Uk,Vh=0}，等同 ker(VU)，所以 rankDΘ=m+rankB²，ν=q−rankB²。因而允许 source 方向 loss 时的最小 codimension 恰为 rankB。这里比较的是 lift 复杂度，不是曲线集 Hausdorff 维数，也没有声称固定 ν 的所有一般最优问题已解。

对 B=diag(1,2) 得 s≥2；源 (2,0) 达到，整个 s=1 smooth 类已排。这个必要式甚至不需 Θρ 满秩，未把方向 rank 假设偷换成额外结构。

## 4. codimension-one full-rank 分类：通过

在同一常数基内记 ay=[C;r]、Θy=[D;ℓ]、aρ=[p;u]、Θρ=[q;v]。若 u+tv 恒0，核恒等式给 p=q=0，从而 Θρ=0，违反 rank m+1；因此不能是零多项式。

乘 u+tv 再代换 h(t)，得到 root/B 的精确矩阵多项式。B≠0 时 t³ 项为 vB，故 v=0、u≠0，t² 项给 uB=−qℓ，rankB=1。该过程尚未除以可能过零的时间分母，涵盖 ruling 锚点退化。

t 项给 D=I+(p/u)ℓ+(q/u)r。先把前 m 行减去 (p/u) 倍最后行，再将前 m 列减去最后列的 r/u 倍，得到 `[[I,q],[ℓ,0]]`，行列式为 −ℓq=u trB。这里 determinant 公式在所选常数空间基下计算；原坐标只差一个非零常因子，满秩判断不变。故 trB≠0；rank-one identity B²=(trB)B 给 rankB²=1。

B0 的 ignore-extra-coordinate 构造方向 Jacobian=I；B=kℓ、ℓk≠0 的标准 affine 构造直接展开投影，detDΘ=ℓk。这两种充分性都满足 full w/ρ、原 clock 和共同开域。因此完整条件 B=0 或 rankB=rankB²=1 既必要也充分，不只是排 rank2。

## 5. genuine nonlinear 校准与方向 loss：通过

B0 例中 z3(t)=(1+t)ρ，π 的平方项为 (1+t)ρ²，正好抵消 z1 中的 −(1+t)ρ²。π 对 z1,z2 的两列为 I；Θ 的矩阵为上三角 determinant1。限制 |t|<1/2 消除唯一分母风险，空间 Hessian 非零。

rank-one 例中 z3=ρ+tk，k+k²=y1；展开 π1 的 tρ 与 tρk 交叉项均消失，留下 w1+ty1+t²y1。方向 Jacobian 的 determinant 为 (1+2k)k′=1，平方根分支在 y1=0 的共同小开域 smooth，π 空间 rank2。所有原参数和整段时间都成立，不是只配一个 selector。

B 的 nilpotent 校准把 k 改为 k(y2)，曲率变为 (y2,0)，但 Θ 的 ρ 列与 y1 列共线，余两列独立，rank 恰为2。它是 (1,1) 而非 (1,0)，没有反驳分类。标量 B 的 τ=t+bt² 是改变时钟的源例外，也不与保原 t 的 lower 冲突。

这些校准严格排除“全 coherence 迫原 π affine”的错误概括。当前三稿和结果页说的是重新构造另一套 variational affine lift，范围准确。

## 6. source 应用和旧记录更正：通过

Def2.1 的 full ρ coherence 与 Θw=0 是实际使用的输入；只在某一 w(y)/ρ-selector 上成立不能求出同一导数系统。Prop2.2 的方向始终是高维直线输入到曲线结论。其 compact submersion charts/有 buffer 的 Ω0、fiber measure 和方向 patch 的有限覆盖可以按原 proof 实现；本次 no-go 本身不依赖任何未证 Kakeya 定理。

旧 R12 正文的代数本来只使用单个 P 的上述系统，故其 affine-only 边界判断需纠正。七个已实际读回的 banners 已清楚将历史推断覆以当前存在性等价，并保留换 clock、Θ依赖 w、单 selector 等不同定义的边界。当前 LIFT-005 结果页与 root 主稿一致，没有以新名称重复登记旧代数。

有界 primary 比对只定位源标准构造及所读段落未明写此必要性，不作无已知/priority 认证；不依赖二手或机器 review。新证明的价值上限是旧 scope 补全和既有分类正确表述，未被包装成重大曲率机制。

## 7. macro/next 和最终范围

R50 macro 明确承认本轮首先是存在性等价纠错，停止整个 parameter-linear、保 clock、full w、Θw0 的 smooth lift 分类；不立即转相邻 clock/selector/Hessian 或一般 s 的相同计算。R51 next 是按周期执行的有界一手前沿/关键路径审视，要求比较不同机制并最终选一个有完整量词、合法删选闭包和独立反攻的唯一后继；不是重证17/4或换名开启当前已覆盖问题。

因此可按当前精确范围归档。普通 R5/一般 Kakeya、重大中间结果及长期 Goal 完成均未得到；未经外部同行评审。本文没有提前核准尚未写完的 metadata/registry/最终字节验证或 Git/sync，这些仍由 root 统一完成。两份 A assigned 文件固定后停止编辑，不另开数学任务。
