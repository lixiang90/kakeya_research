# R0046 独立审查：精确算术门槛、有限搜索和后继构造范围

2026-10-17，`lifting_obstructions`。修后 root/A/macro/next 在明确范围内通过内部逐步审查；未经外部同行评审。R5/3 未证未否，本轮未产生 Kakeya 反例、新维数界或重大中间结果。

## 1. 实读范围

已实际全文阅读 root `R0046_exact_rational_candidate_and_finite_seed_boundary.md` 八节、A `R0046_primary_and_geometric_seed_audit.md` 八节、`R0046_macro.md` 八节及 `R0046_next_cyclic_selector_volume_gate.md` 五节；自己的算术稿不计独立证书。已读两实验程序及两份完整 JSON，并独立只读核程序/输入 SHA256、十个网格的 adjugate 定义、十个最优见证原计数及合计。第二算法的全部重算为 root 实际运行并保存；本 review 没有再跑第三份相同穷举。

一手接口核对沿用 Zhang2608.17952v2 §§3–4 的准确形式，并重新阅读 FD–deLaSalle2607.14824v3 Proposition5.4、Lemma5.5 及其证明所需段落（本地 text1026起）。外部深层完整证明仍具名保留，不因 statement/application 核对冒充独立重证。

## 2. 原四投影与全称常数

A 的四环计数下界 `N^4/(s_1^2 s_2 s_3)` 由两次 Cauchy–Schwarz 得到；signature `(L_2 z_2,L_3 z_3,L_4 z_4)` 给 `2x_1=-L_2z_2-2L_3z_3+L_4z_4`。乘2单射确定 `x_1`，最大纤维付 `M`，其余三个点唯一恢复，故旧式 `N^4<=M(s_1s_2s_3)^2s_4` 无遗漏。将其取五次后乘 `N`，`N<=M^2` 域确已覆盖候选，没有把该域当全称新估计。

root 的无挠有限坐标群压整数证明保全部所需有限差，因而同保 `N`、全部投影基数及每个原 `x` 纤维。与数值大小无关的整数统一估计确可推广到所有无挠群；该压缩不保证任何实欧氏角性质。

张量后最大纤维恰为 `M^n` 而非仅 upper，四像集亦恰为笛卡尔幂。因此全称统一 `C` 必须 sharp1，严格整数证书足以用 tensor 否定全称式。type-class 必要熵式的系数 `14,7,10,5` 正确；同 joint type 对每个出现的 `X` 序列有同一条件 type 的纤维数，支付的是最大纤维，不能在均匀有限集合中免费把 `log M` 改成平均条件熵。稿件没有声称该熵不等式无条件成立或已付双向等价。

## 3. 有限程序与输出的实际范围

十对形式的行列式均非零；adjugate 将两个选中形式准确变为 `det*u,det*v`，无舍入。每个16点网格的 Gray traversal 确遍历所有非空子集；单 bit 增删时 row histogram、五个投影计数及最大纤维的更新正确。所有指数比较与最优排序都用任意精度整数和交叉乘法。

第二程序使用普通 mask、投影等值类的 bit intersections 和逐 row bit counts，不复用第一程序的增量状态。输出合计655350，旧域外402457，旧域内252893；网格间可重复，不声称不同集合数。所报六点例的准确比率是 `6^21/(24^10*4^5)=177147/524288<1`。程序/输出哈希、十个所报见证和合计已独立核一致。

因此只可写上述有限范围没有反例，不能写全称不等式通过、没有更大整数反例或一般连续定理成立。非均匀概率的必要熵反攻未被该均匀子集穷举替代，root 已保留这一范围边界。

## 4. 原有限种子的真实接口

自然共同 clock 直线 `(t,F(y)+tF(x))` 在四个有理 times 才由原四集合控制；固定四个 marks 的密度 `O(delta)` 达不到原 `delta^eta_src`。加厚为时间窗后，多出的 `(t-t_j)F(x)` 不受原四基数约束。A 的 drift-box cover 是诚实 upper，不是宣称所有编码不可能的 lower。

低加法 rank 不供近满三维方向网或小常数的归一化3-Frostman law，但已经分离的稀疏 slope 集仍有绝对三维 packing upper；稿件没有把这两件事混淆。补两维自由方向网的实际构造保共同 clock，但原 marks 总量与 visited cover 同乘该网格因子，远离焦点时两边抵消。

bush 校准的 `lambda=2delta^eta_src` 支付 floor 后逐管 marks 下界；方向 bin ceiling 固定，原总 marks 为 `lambda delta^-4`，union cells 至多 `C lambda^4 delta^-4`，故有效参数必须 `3eta_src<=epsilon`。方向、时钟及固定邻格费用只改变常数。它不反驳 DIR，也不提供可选择 eta 的正向模数；确排除先免费令 `epsilon/eta_src` 任意小的做法。

root 按一轮规则停止实际尝试的 seed-to-four-times 桥，未将 R5/3 标 false，也未否定所有算术路线，符合证据。

## 5. 下一 cyclic placement 的闭包与紧致出口

新对象确为同一单位 clock 上完整四参数方向网的真实五维 segments，`B_i=b_i(a_(i+1))`，没有把四个时间截面或虚拟 filled shading 当原构造。它是严格受限的 placement 类：任意删方向不保完整 Cartesian 网，任意删时间不保 wholeclock。因此不能以未付的重生闭包反推全称 CP/PM，也没有从旧 positive-power 结论免费推出 uniform log lower。反向更不包含任意 `B(A)`。R41 在这里 `TC=0` 但 `S` 可达 `4log N`，只给弱下界，不能免费证明 CYCL。

连续填方向 cell 时复用代表 intercept，使整条真实 segment 偏移 `O(delta)`；取闭 cells 后是有限个紧集的并。相邻 dyadic 尺度和固定 `C0>=10` 可以支付填充误差及所需 `N_(2delta)`，无需在已给 upper 中无费放大厚度。方向 patch 固定，有限旋转给全方向；wholeclock 段长至少1，取单位子段不增邻域体积。

若每个足够大 dyadic `N` 真有统一 `kappa>0` 的 actual-neighborhood upper，则可补全部小尺度并扩大常数处理粗尺度，得到 FD 原 `(1)_f`，其中 `f(delta)=C delta^kappa` 非减。Prop5.4 的出口确为同一 compact Kakeya 集及 `f(C delta^(1/4))`，所以保留幂 `kappa/4`，并给上 Minkowski 及 Hausdorff 的上界；没有另缺一个被遗忘的跨尺度 coherence 假设。无穷稀疏统一幂序列也可按下节 step-f 补足输入，但仅得到对应序列的维数上界。有限样本不够；uniform CYCL lower 也仅是本受限类的邻域结论，未免费升所有集合的 Hausdorff 满维。

未发现修后四份主稿的剩余必修错误。下一轮只检验该实际新构造类；若只有旧 entropy/四维投影/单时碰撞界即停止，不以循环长度、alphabet 或新阈值续同义任务。一般高维目标保持 active。

## 6. 稀疏尺度范围修正的追加独审

已实际重读 root§8、macro§§6–7 和 next§§1/4 的最新修订，修正通过。设严格递减 `delta_j->0`，同一正 `kappa` 和常数控制每个完整方向 `G_(delta_j)`。对 `0<r<=delta_1`，集合 `{j:delta_j>=r}` 非空且有限，故 `f(r)=C min{delta_j^kappa:delta_j>=r}` 的最小值取得；较大 `r` 补足常数后，`f` 正值非减并趋零。

在每个 `r` 选择达到最小值的 `j`，由 `r<=delta_j` 得 `|N_(2r)(G_(delta_j))|<=|N_(2delta_j)(G_(delta_j))|<=f(r)`，确满足 FD 的全尺度 `(1)_f`，无需假定稀疏尺度相邻可比。有限网格至完整紧方向 patch 的填充及有限旋转费用已在前节支付，不在这里重新无费放大厚度。

FD 给同一 compact `E`；在 `r_j=(delta_j/C_d)^4` 恰有 `C_d r_j^(1/4)=delta_j` 及 `f(delta_j)=C delta_j^kappa`，所以 `|N_(r_j)(E)|<=C' r_j^(kappa/4)`。相交的 `r_j`-网格盒可用这个邻域体积界数目至多 `C r_j^(-5+kappa/4)`（采用直径至多 `r_j` 的固定更细网格也只改常数），其任意 `s>5-kappa/4` 的 cover cost 趋零。因此下 Minkowski 和 Hausdorff 上界成立；稀疏序列不自动控制上 Minkowski。最新三稿保留了此区分，没有将稀疏幂证书误写成全尺度幂上界。其余正式审查结论不变；停止编辑。
