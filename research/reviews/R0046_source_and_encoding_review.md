# R0046 独立审查：固定算术候选、精确搜索与真实几何入口

2026-10-17，audit_four_dimensional。独立于 root 主稿、B 算术稿和实验代码作者。本人 primary/encoding 稿不在此被作为自己的独立审查。已实际全文读 root8节、B6节、macro8节、next5节，两份实验程序及两份完整 JSON。**通过修后所述范围，可归档；R5/3 仍未证未否，没有新的 Kakeya 界或反例。** 以下审查未经外部同行评审。

## 1. 一手输入及原量词

直接读 Zhang2608.17952v2 本地精确 PDF/text 的 §2、Definition3.1、Lemma3.2、Theorem3.3、§4 Lemma4.2/Remark4.3，并对照官方 primary；未用普通 Hausdorff 维数4代替 finite 输入。旧式 `N^4<=M(S1S2S3)^2 S4` 的四环 lower/恢复 signature upper 已逐步核查；乘2单射在无挠群中合法，最大纤维 M 没换成平均纤维。

q5/3、r5/2、p=(2/7,2/7,2/7,1/7) 的基本缩放正确；这些必要条件不证明候选。q7/4 的 restricted 弱型经张量去 log 仍是原 q，不能改变为5/3。§3 真要求 all-G、rank/tensor 上统一常数；主稿/spec 没省略它。

旧式取五次方再乘 N，在 `N<=M^2` 区域准确得到新候选整数式。因此这一域是旧结果，不是新不等式。restriction 的投影/M upper 与原质量 lower分开；equal-cardinality 弱版未被免费升成 asymmetric 全式或 strong mixed norm。

## 2. B 的任意群/整数压缩和 sharp-C1

有限坐标生成 H≅Z^d；对所需坐标及四像集的有限并 U，整数线性映射 `ell_T(v)=sum T^i v_i` 可避开有限个非零多项式的整数根，使其在 U 上单射。四个 integer forms 与此 homomorphism 精确交换，故 N、每个 x-fibre 和全部像集基数均保持。这个证明只给算术保真，不给 angular/尺度条件数，B/root 的范围正确。

`Z^n subset(G^n)^2` 的最大 x-fibre 确为 `M^n`，并非只有 upper；每坐标可选到一个最大 fibre。所有像集取 n次幂，统一 C 强制原比率至多1。张量后再压整数也合法，所以即便只说整数群，仍不能用有限 C 隐藏一个严格坏比率。整数证书 `N^21>M^7P^10S4^5` 的有限计算与由 tensor 得到全称否定是不同步骤，本轮没有找到该证书。

## 3. 必要熵式和符号模式

B §4 的联合 type class 证明通过：固定有理 joint law，每个已出现 X-word 的 conditional Y-type 数完全相同，指数为 H(Y|X)；投影序列落在其固定 marginal type 中，故可用其熵作 upper。代候选并除长度后得到 `14HXY+7HX<=10(H1+H2+H3)+5H4`，再以有限支撑熵连续性扩到实概率。没有在任意一个均匀 Z 中直接用 H(Y|X) 替换 log M，也未声称反向熵等价。

B §5 的变元 a=x+y、b=−x+y 给 `(a,b,(a+b)/2,2a+b)` 正确；“除2”只用于乘2单射的唯一性，未假定一般群可任意除2。单投影为 singleton 的情形，其余 projections 和 x 的单射由非零整数倍在无挠群中单射给出，确不能反候选。

完整图族 `Z_m={(2k−1,1),(2k,0):0<=k<m}` 的四基数是 `(m,m+1,2,m+1)`、M=1；整数比率 `2^11 m^11/(m+1)^15` 正确。对正实 m 的最大点11/4、最大比率 `2^19 11^11/15^15<1`，及 m=3 得 `177147/524288` 均独核。其 tensor 只把小于1的比率取幂，不会生成反例。这只排该模式，不排全体 graphs。

## 4. 两份代码与完整有限输出

实际读取 `experiments/arithmetic/R0046_rational_projection_search.py`（129行）、`R0046_verify_search.py`（71行），以及真实路径 `experiments/arithmetic/outputs/R0046_search.json`、同目录 verification JSON。root 已修主稿漏目录的 literal path；没有数学影响。

搜索以五 forms 的十对 adjugate 作用于4×4整数网格，det全非零，选中两 forms 的值精确为det乘原网格坐标。Gray code穷尽每个16点网格全部65535非空子集；incremental projection counters、row histogram及最大 fibre 的升降更新正确，所有不等式/排序使用 Python integers。不会因 negative determinant 或值重复误数。

独立程序使用普通 mask、等值类 bitsets、每 row bit_count，未复用 Gray 更新。它重核全部655350个带 grid-label样本、旧域/域外计数及各 grid 最优比率，已存输出全部通过。本人没有无必要重跑这第三遍穷举；另以 read-only 独立短核重建十个 grids、直接重算十个输出最优点集的 N/M/四投影/整数证书，并核 source/input SHA256 一致。

实际总数655350，旧域252893、域外402457；域外最大比率准确为 `177147/524288`。JSON 的 false flags 与主稿结论一致。grids之间可能重复点集，作者没有声称计数是不同 Z 数量；未命中只证明所列有限范围，不证明全称候选或没有更大的整数/非均匀反例。

## 5. 四个 marks、真实 cover 和 sparse angular 范围

root §5 自然 exact homomorphic line在 t=1,−1,0,1/3 读四个像集，第四处值是 F(S4)/3。一次共同 affine clock变换仍只给四个 times，而 DIR/FSD 对小 eta要求每line至少 `delta^{-1+eta}` 个 bins。重复 weights/indices 或重参数不能把四点自动变长 duration。

把time片加厚到 w，会出现原四像集之外的 `F(y)+t_jF(x)+(t-t_j)F(x)`；原基数没有给新增 cover upper。主稿对此保留缺口，没有把朴素 cover upper 说成实际 lower或所有 encoding不可能。

低rank的措辞已正确收紧：rank1 hom slopes不能提供近满三维方向网/归一化3-Frostman小常数，但任何 separated sparse family仍满足绝对3-packing cap，所以它不是禁止调用 unsaturated DIR 的绝对理由。alpha/M和 min-separation/delta 的真实费用仍需保留。

自由补两个 direction coordinates 的直接产品，远离辅助焦点时每个原 time/spatial cell都有 Theta(|W|) 个辅助 cells；管数、marks sum与cover均乘同一个 |W|。这一 factor在 DIR两边精确抵消，不供算术 saving。该有限校准不排所有耦合 auxiliary constructions。

## 6. Bush 量词校准修后完全合法

root 已按建议取 `lambda=2delta^{eta_src}`，而非缺一格的 literal floor值。delta小且0<eta_src<1时，`floor(lambda/delta)>=delta^{-1+eta_src}`、lambda<1，所有line满足 DIR的原门槛。

full bounded delta-grid slopes共有 Theta(delta^{-3})条真实 lines `(t,tv)`，每 direction bin仅固定权重；第k time层在边长Ckdelta的三维 spatial box，故 union cell数至多 `C sum_{k<=lambda/delta}(k+1)^3<=C lambda^4delta^{-4}`。marks sum至少 `c lambda delta^{-4}`。假设选中的 eta_src 真是有效 DIR参数，便只能有 `1<=C_epsilon delta^{3eta_src-epsilon}`，因而必要 `eta_src<=epsilon/3`。

该必要性对已有 DIR合法（其可选更小eta）；不是 source反例、不是 eta正向可选下界，也不认证线性 loss模数。它准确阻止先令 epsilon远小于source事后给出的eta再消损失；没有越过 all-G/tensor 的实际scale费用。

## 7. Macro停止和新 cyclic gate 的范围

实际全文读 macro8节及 `notes/50_counterexamples/constructive/R0046_next_cyclic_selector_volume_gate.md`5节。R5/3明确仍未证未否，停止的是本轮尝试的自然 finite4D→fixed-four-times桥。没有把有限搜索通过登记 theorem，也没有调 q/weights续轮。HRZ仅作未核后备，不偷已有原 packet极限当已解决。

新对象是真实 R5全4-grid slopes、wholeclock线段，`B_i(A)=b_i(a_{i+1})`，不是四个时间像集。其 directions独立，TC=0，但 injective-bin b_i使 `H(B_i|A_i)=logN`，总S=4logN；所以原R41 separable/small-S lower不能免费给CYCL。这是改变已付假设的受限 test，不能反推任意placement。

任意 direction restriction破坏full Cartesian product，任意time shading restriction破坏wholeclock。因此没有凭未知全称positive-gain调用形成免费再生/双向CP等价；下一轮仍须按spec先检查，不因本review预先认证所有可能 equivalence。uniform log lower与allscale power family都未证明，affine/单singular time和finitevoxel观察不会自动给全clock上界。停止规则不追加循环长度/entropy阈值调参，范围通过。

## 8. Full directions、固定厚度和 FD compact桥

已重新实际读 FD–deLaSalle2607.14824v3 Proposition5.4/Lemma5.5全文（PDF18–19，text1009–1136）。该桥确由每个delta的fullKakeya `G_delta` 和 `|N_{2delta}G_delta|<=f(delta)`，产生同一compact E及 `C_d f(C_d r^{1/4})`；不是逐层体积相乘。next 没把这项已付桥重新列为未知coherence。

对有限4-grid slopes，任意同cell a'与代表a距至多2delta；整个0≤t≤1 segment偏移至多2delta。用有限个闭cells复用原intercept，可得compact的连续 direction-patch family；有限rotations覆盖sphere。每wholeclock段长度至少1，含unit segment。`N_{2r}`的额外thickness须和fill的2delta同时计，不能只审N_delta。

next 的固定 C0≥10足够：给任意 r，选dyadic delta_N在[r,2r)，则fill加2r后的半径至多 `2delta_N+2r<=4delta_N<C0delta_N`，固定rotations只付固定倍体积。因此若每个足够大dyadicN都有同κ/C的真实upper，原 `(1)_f` 对 `f(r)=C'r^kappa` 的所有小 r成立；较大r补固定常数即可使f正且非降。输出确是同compact E的 `|N_rE|<=C''r^{kappa/4}`，所以upperMinkowski/Hausdorff至多5−kappa/4，不能误写原kappa。

rounding intercept只允许双向付固定neighborhood半径费用；对固定C0的upper无费再扩大不合法，next已要求常数预算/必要时更细网。一次或有限多尺度的数值压缩不能当上述全称输入。root 后续按本次接口建议实修三文件的最终段落，已再次全文读取 root §8、macro §6–7、next §1/4 并核下述无限稀疏尺度处理；此处没有新增另一主任务。

若 `delta_j` 严格趋零、所有尺度同一 kappa/C，定义 `f(r)=C min{delta_j^kappa:delta_j>=r}`，较大 r 补常数。每个固定小 r的候选下标集有限且非空，故 minimum达到；r增大时候选集只缩，f非减。在 r<=delta_j 使用同一个真实fullKakeya `G_(delta_j)`，`N_{2r}G` 包含于 `N_{2delta_j}G`，即可供应每个 r 的原(1)_f；不要求新selectors嵌套。

Prop5.4 输出在 `r_j=(delta_j/C_d)^4` 上有 `|N_(r_j)E|<=C'r_j^{kappa/4}`。compact E的 separated-point packing/细grid cover 给 `O(r_j^{-5+kappa/4})` 个 O(r_j)-balls；任意 `s>5-kappa/4` 的 s-cost趋零，故下Minkowski和Hausdorff至多5−kappa/4。只有全scale power才另控制上Minkowski。修后 next明确区分这些结论和有限N不足，范围正确。以上为已知Prop5.4的直接应用审查，不把它作为新的Kakeya结果登记。

最终通过范围：本轮 primary/有限算术/实验及几何接口审计和停止决定，下一受限真实体积test的量词与已知compact桥。没有证明CYCL、power construction、R5/3或高维新界，没有优先权/重大性认证。两assigned文件完成；停止编辑，不操作Git。
