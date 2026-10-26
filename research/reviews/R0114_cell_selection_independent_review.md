# R0114：整格筛选与原实体载体门的独立逐步审查

2026-10-26，constructive_gate。结论：**通过所锁有限范围审查，无未解决的必修数学问题**。这是原平均 shading 的 closure 压力，不是新普通维数下界、HRZ 反例或实际 small-footprint Kakeya 构造；未经外部同行评审。

## 1. 独立性、实际读域和锁定版本

本人未参与 cell-discrepancy 机制的提出、主证明施工或 algebraic 资格稿施工；本轮此前只处理真实构造/source 公式分工。收到审查任务后，实际全文读 working 和主稿八节，包括第4节正概率版本与第7节可选逐管事件，再独立重算各步。没有把自己先前构造稿当本机制的独审。

实际审查文件：

- research/rounds/R0114_cell_selection_working_spec.md，SHA256 9a6cbf2449a9d5dbaf5f8d66b8e6fc22782065bb34f802d645c465d00f1148b0；
- notes/40_multiscale/R0114_whole_cell_discrepancy_and_original_carrier_gate.md，SHA256 3dfc6ffee0965aab1b31a66d7719baf8100809881f635effc804489f51d1fd18。

另全文读 algebraic 资格稿用于定位原对象；排重核实际读 R101 主证书 §§1–8 及 native-witness 资格稿后部，不冒这两份历史的本轮全文重审。只编辑本 review，不操作 metadata/Git。

## 2. 符号 pattern、零多项式及每格 Jensen

固定 degree \(D\)，系数维数 \(b=\binom{n+D}{n}\)。对任意固定点云 \(u_1,\ldots,u_K\)，每个取值 \(P(u_j)\) 是系数的线性函数。计数必须包括 hyperplane arrangement 的所有维 faces：三值符号 \(<0,=0,>0\) 的 pattern 数由
\[
 F(K,b)\le F(K-1,b)+2F(K-1,b-1)
\]
控制，给 \(\sum_{j\le b}2^j\binom Kj=O_b((2K)^b)\)。低秩/重复 hyperplanes 可降到实际 span，退化不增加该 upper。常数项坐标已包含；全零系数向量在全零 sign face 中，故 identically zero polynomial 与等号查询都未被丢掉。对至多 \(s\) 个 polynomials，相乘 pattern 数，再乘有限个 truth tables \(2^{3^s}\)，仍是 \(C_s(2K)^{sb}\)。任意长 Boolean 写法只是同一有限 truth table，不会增加一个随 \(K\) 爆炸的未计数项。

固定一个 membership pattern 后，\((\xi_j-p)w_j1_A(j)\) 独立、中心化、取值区间长至多 \(w_j\)。Hoeffding mgf 的 \(\sum w_j^2/8\) 参数正确；计正负后 log-sum-exp 给主稿 (2)。该证明没有暗用 \(p\) 的方差改善，故对本轮先固定的任意 \(p>0\) 合法。

每格按 \(g/w_j\) 抽一个 \(U_j\) 时，对每个固定 \(H,\xi\)，期望准确还原 \(\int_{Q_j}g1_H\)。然后
\[
 \sup_H|\mathbb E_U Z_H|\le\mathbb E_U\sup_H|Z_H|
\]
方向正确；不是把真实积分替成一个未经控制的抽样等式。固定 \(U\) 后才用有限 pattern upper，且该 upper 对所有点云统一，所以可以交换有限 \(\xi\) 求和与 \(U\) 积分。跨格边界的 \(H\cap Q_j\) 已在积分中处理，不缺 boundary-cell \(O(\delta)\) 费用。

可测性也已支付：固定格式可由有限维实系数和有限 Boolean 选择参数化，测试函数 jointly Borel。其 supremum 的 strict upper level 是 analytic 投影，故 universally measurable；有限 Radon 产品概率的 completion 足够，且 supremum 被 \(\sum w_j\) 控制。外层 \(\xi\) 只有有限个值。原 \(g\) 仅 Lebesgue 可测时取同一个 Borel a.e. 代表，不改变任何 \(H\) 的积分；主稿没有把这个 sup 错称普通 Borel。

## 3. 同一 mask 的原体积/质量及正概率

在 \(a\le f<2a\) 的层 \(A\) 上，\(J_A\in[aV,2aV]\)，故
\[
 \sum w_j(1_A)^2\le\delta^nV,\qquad
 \sum w_j(f1_A)^2\le2a\delta^nJ_A\le4a^2\delta^nV.
\]
两个归一 sup 的期望相加，因此选出的是**同一份** whole-cell mask，同时控制全部 \(H\)、总体积和 incidence。\(H=\mathbb R^n\) 可用常数 polynomial/恒真 Boolean 加入原格式类；不需要给 \(B\) 边界额外格式。

主稿第4节的正概率加强正确：把误差常数放大4倍，对两个归一 sup 之和用 Markov，控制事件概率至少 \(3/4\)。这与仅用“某份 mask 存在”不同，足以供第7节联合其它高概率事件；\(\delta\) 小度随后按放大后的常数选择即可。

若 \(r\le p/4\)，则
\[
 V'\le5pV/4,\qquad I'\ge3pJ_A/4.
\]
再用 \(f<2a\)、\(|H|\le CV'\)，独立重算得
\[
 \frac{I'(H)}{I'}\le\frac{10}{3}Cp+\frac43\,r/p
 \le4Cp+2r/p.
\]
取 \(p\le\theta/(16C)\)、\(r\le\theta p/8\)，右边至多 \(\theta/2<\theta\)。分母始终是同一次保留后的真实 \(I'\)，没有把期望 \(pI\) 当实际保留量，也没有按查询 \(H\) 重抽 mask。

## 4. 返回原管、dyadic 层与平均/逐管区别

原 \(f=\sum1_{Y_i}\) 是整数、\(0\le f\le N\)，非空 dyadic 层至多 \(L_0=1+\lceil\log_2N\rceil\)。因此可取 \(J_A\ge I/L_0\)。主稿使用的 \(V\ge J_A/(2N)\) 是安全的保守 bound（实际 \(f\le N\) 还给更强者）。代入 \(I=\lambda N\delta^{n-1}\) 得
\[
 r^2\le C\,\delta L_0\log(2K)/\lambda.
\]
由 \(N\le C\delta^{-(n-1)}\)、\(\lambda\ge\delta^\eta\)、固定 \(\eta<1\)，该量趋零。所需 \(\delta_0\) 可以依赖固定格式、\(C,\theta,p,\eta,B\)，没有把这些常数误装成绝对统一量。

原 indexed tubes/axes/directions/clock 和 \(N\) 全保留，只把原 \(Y_i\) 交层和 mask；允许零 shading。因此
\[
 I'\ge c p I/L_0,\qquad
 \lambda_{\rm new}\ge cp\lambda/L_0.
\]
对任意 \(\eta'>\eta\)，固定常数与 log 能在足够小 \(\delta\) 吸收；主稿正确地没有声称原同一个 \(\eta\) 字面门槛不变。若另删空管/作 heavy，须重算 \(q\) 和 \(p_I\)，\(\lambda'=(p_I/q)\lambda\)、归一帽除 \(q\)，不能重设原 \(N\)。

第7节 mask-only 的逐管论断也正确：\(w_{i,j}\le\delta^n\) 给 \(\sum_jw_{i,j}^2\le\delta^n|Y_i|\)，于是 Hoeffding upper 为
\[
 2\exp[-c p^2|Y_i|/\delta^n].
\]
若每管 \(|Y_i|\ge\delta^{n-1+\eta}\)、\(\eta<1\)，多项式 \(N\) 的 union bound 仍趋零。与上一节概率至少 \(3/4\) 的事件相交，确有同一份 mask。原 multiplicity layer 可能先删光一根管，故这**没有**把 layer+mask 主命题升级成逐管 lower；原稿已明确区分。

原 marks 若本来为同格完整 cell 并，则其 multiplicity 层及 mask 仍是同格并；一般 marks 上只保真实交集，没有虚构填格。物理 \(|E'|\) 是原 Lebesgue 量，证明未用 \(|N_\delta E|\) lower 倒推 \(|E|\)。

## 5. 常数依赖、假想 small footprint 与 HRZ 的边界

本命题直接拒的是固定 \(C,\theta,s,D\) 的 uniform literal carrier 捷径。若载体常数按**新**密度恶化，不能用固定 \(C\) 证明偷换。例如若 \(C(\lambda_{\rm new})=(\lambda_{\rm new})^{-B}\)、\(B\ge1\)，同一总量误差还给 \(I'\le(p+r)J_A\le5pI/4\)，故 \(\lambda_{\rm new}\le5p\lambda/4\)，从而
\[
 C(\lambda_{\rm new})p\ge
 (4/5)^B p^{1-B}\lambda^{-B}.
\]
不会因 \(p\to0\) 自动变小。固定原输入密度上的常数与允许对新数据重调用的常数不是同一量词。主稿 §7 已写出相应边界，本审查不扩展它。

同样，若 degree/格式随 \(\delta\) 增长，应把 \(s\binom{n+D}{n}\) 等实际增长带回 pattern 及误差预算；本稿没有全排这些情形。系数高度可任意随 \(\delta\) 变化则已由固定 coefficient dimension 统一处理，这两种复杂度不能混淆。

若假想原 small-footprint 配置存在，其真实删选仍 small footprint，同时满足新的平均密度门槛。因此一个对**所有这种合法平均限制**都免费给固定格式 carrier 的声明，将在该族中遭遇 (5)。但没有实际构造开放范围的 small-footprint 原族，不能由条件压力声称“含 small-footprint 前提的数学蕴含已被实际反例否定”；前提可能本身待排。主稿首部、§6–7 和 working 均保留这个解释。

随后实际读回主稿 §7 从“尤其要区分无条件carrier规则”起新增的两段及 §8 对应收紧，独立核其双向量词。固定 \(\beta>0\)，令 \(C_\beta(\eta)\) 表示存在固定格式、\(C,\theta,\delta_0\)，对所有原饱和方向平均配置，只要 \(\lambda\ge\delta^\eta\)、\(|E|\le\delta^\beta\) 就有该 carrier；令 \(S_\beta(\eta)\) 表示足够小 \(\delta\) 根本不存在这些配置。则
\[
 C_\beta(\eta)\ \Longrightarrow\ S_\beta(\eta/2),
 \qquad S_\beta(\eta)\ \Longrightarrow\ C_\beta(\eta)
 \quad\text{（后者为空前提）}.
\]
第一箭头确实使用同一个原 \(N\)、原方向族及原 marks 的合法 layer/mask：若在任意小尺度有 \(\lambda\ge\delta^{\eta/2}\) 的实例，则 \(\lambda_{\rm new}\ge cp\delta^{\eta/2}/L_0\ge\delta^\eta\)，且 \(E'\subset E\)；新数据仍满足 carrier 前提，却与主稿 (5) 冲突。取更小共同 \(\delta_0\) 后即得最终不存在性，不只是沿某串好尺度。反向不需构造任何 carrier。故对每个固定 \(\beta\)，\(\exists\eta\,C_\beta(\eta)\) 与 \(\exists\eta\,S_\beta(\eta)\) 在此饱和、任意平均 shading 类中同强度。没有把一个固定 \(\eta\) 的两个声明偷说成逐字等价，也没有覆盖 \(C(\lambda_{\rm new})\) 或不闭包的逐管/完整 source 类。

因此无条件的 fixed-\(C\) carrier 规则有实际筛后配置反攻；假想 small-footprint 内的条件规则则承担 finite 正幂排除本身的责任，尚未被证明真或假。它不再是可登记的新正面初始化机制。本次读回后再次读取的主稿 SHA256 仍为 §1 所列 3dfc6ffee0965aab1b31a66d7719baf8100809881f635effc804489f51d1fd18，working 哈希亦同；本 review 对该现存完整版本认证。

PW/CW upper、whole-axis containment、HRZ 的付费 nested partition/variety 信息不是这种存在性声明。多个载体、远大于 \(|E'|\) 的载体、复杂度增长或更强 source 下界没有被此 mask 否定。本审查不支持 HRZ/多项式方法失效的泛论。

## 6. 审定范围与收尾

固定符号格式的原整格 absolute discrepancy、同一次 mask、原 \(N/I\) 账本、平均密度返回和 narrow carrier 压力均通过。root 已将我在正式 proof 出现前提醒的 \(C(\lambda_{\rm new})\) 与正概率联合事件边界写入正文；本次实际全文读回后未发现剩余必修项。

R101 处理 native 几何 supergraph、见证编码及完整 witness boxes 的原质量；本次处理原物理 Lebesgue shading 的全部固定格式实体查询，不是其全称重调用。当前结论仍是经典有限复杂度随机筛选的应用，不据此认证文献新颖性、重大性或新 ID。没有新的 ordinary/完整 source gain，长期 Goal 未完成。

此 review 包括上述新增双向量词的实际读回；后续若改主量词或证明，应再读回相应变化后认证。没有执行数值试验来替代证明，也未操作其他文件、Git 或同步。
