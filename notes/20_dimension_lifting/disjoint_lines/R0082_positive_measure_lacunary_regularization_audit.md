# R0082：同一 lacunary 函数的正测度 Hölder 限制反攻

2026-10-18，A，已先实际全文读更新后的 R0082 working_spec 五节与 macro 六节，再施工唯一 phase II。本稿恰十二节；只证明明确锁定的局部度量反攻，不反完整 compact 全 RP 方向对象，不声称新维数界、major、priority 或新 ID。

## 1. 同一函数、完整量词与独立证明范围

固定

    a_k=2^(−k²)， b_k=2^(k³)，
    h(x)=Σ_(k≥1) a_k sin(2π b_k x)， x∈R。

要证明：对每个 Lebesgue measurable F⊂[−1,1]、|F|>0，每个 α>0 及有限 L≥0，存在不同 x,y∈F，使

    |h(x)−h(y)|>L |x−y|^α。                       (1)

h 在 F、α、L 选取前已经完全固定；不依 F 选新频率序列，不只证明 nowhere differentiable 或某点振荡。后半将 (1) 接回真实 R5 整线族，反驳其 canonical offset 在任意正四维角度测度子族上可作正 Hölder 限制。

标量分析 §§2–7 为本人独立正证，须由 root/B 实际独核；本人的自算不记自身独立审查。§§8–11 独立检查几何接口与反攻边界，B 的最终稿落盘后再实际全文交叉核并在 §12 记录。所有旧高级输入的 wholeproof 均不由本稿重新认证。

## 2. 一致收敛、连续性和同一全局相位

因 a_k≤2^(−k)，Σa_k≤1，级数在整个 R 上绝对一致收敛。每项连续，故 h 连续且 |h|≤1。b_k 为整数，h 还是 1-periodic；后续只用固定区间 [−1,1] 内的实际值，不按小窗另调相位。

对任一 k 分解 h=H_<k+a_k sin(2π b_k x)+H_>k。H_<k 是有限光滑和，故其全局 Lipschitz 常数至多 2πΣ_(j<k)a_jb_j；高频尾 H_>k 的 sup norm 至多 Σ_(j>k)a_j。此处分解没有对无限级数求导。虽然振幅很小，各频率的导数因 b_k 巨大，不能用逐项导数级数收敛或 Rademacher 定理代替本证明。

## 3. 正测度 F 的密度点与两个必被命中的窗口

给固定 |F|>0，取 Lebesgue density point x0∈F∩(−1,1)。当 k 足够大，

    I_k=[x0−1/b_k,x0+1/b_k]⊂(−1,1)，
    |I_k\F|=o(1/b_k)。

该区间长度恰为两个完整周期，无论 x0 的相位是什么。定义

    P_k={x∈I_k:sin(2πb_kx)≥1/2}，
    N_k={x∈I_k:sin(2πb_kx)≤−1/2}。

在任一周期内，这两个集合各占长度的 1/3，故 |P_k|=|N_k|=2/(3b_k)。密度结论使 |I_k\F|<1/(3b_k) 对所有充分大 k 成立。因此 F∩P_k、F∩N_k 各有正测度，特别各非空。可任选

    x_k∈F∩P_k， y_k∈F∩N_k。

它们不同，且 |x_k−y_k|≤2/b_k，第 k 项的差至少 a_k。这里必须使用 density point 而非只说 F 与一个小窗相交；正测度全局信息本身不保证每个位置的振荡窗都命中 F。结论只要求存在充分大的 k，不声称 k 的起点可对所有 F 一致。

## 4. 低频误差的逐项严格估计

对上述点对，均值定理只作用于有限和，给

    |H_<k(x_k)−H_<k(y_k)|
        ≤(4π/b_k) Σ_(j<k) a_jb_j。

j³−j² 对 j≥1 单调递增，所以 k≥2 时

    Σ_(j<k)a_jb_j≤(k−1)2^((k−1)³−(k−1)²)，
    [Σ_(j<k)a_jb_j]/(a_kb_k)
        ≤(k−1)2^(−3k²+5k−2)→0。                 (2)

因此低频差/a_k 至多 4π(k−1)2^(−3k²+5k−2)，趋于 0。没有把 b_(k−1)/b_k 的巨大分离与 a_(k−1)/a_k 的反向比率混淆；两个比率已在 (2) 同时支付。对某个固定 k_abs 后，此误差≤a_k/4。

## 5. 高频尾的全相位估计与主振幅存活

不同点的高频尾差至多 2Σ_(j>k)a_j。令 j=k+m，则

    2Σ_(j>k)a_j/a_k
      =2Σ_(m≥1)2^(−2km−m²)
      ≤2Σ_(m≥1)2^(−(2k+1)m)
      =2·2^(−2k−1)/(1−2^(−2k−1))→0。            (3)

不假更高频率在所选点同相、消失或可对 F 单独选择；(3) 对全部点成立。增大固定 k_abs，可使 (3)≤1/4。故 k≥k_abs 且满足 §3 密度条件时，

    |h(x_k)−h(y_k)|≥a_k−a_k/4−a_k/4=a_k/2。     (4)

低频与尾误差均在挑选 F 中点之前有 uniform 上界，因而没有点依赖或条件独立的遗漏。主振荡窗本身的正测度还保证可以避开任何预先给定的 null subset of F；本文不需要把这一观察升级成另一个定理。

## 6. 任意 α/L 的矛盾和量词顺序

固定任意 α>0 与 L<∞。由

    a_k b_k^α=2^(αk³−k²)→∞，

可取 k 同时超过 density 起点和固定 k_abs，并使

    a_k/2>L (2/b_k)^α。

结合 (4) 与 |x_k−y_k|≤2/b_k 即得 (1)。L=0 亦成立。α 可任意小，也可大于 1；标量分析无需先假 α≤1。不同 α、F 所需 k 可以不同，这与“同一个 h 对所有 F/α/L”完全相容，没有通过 uncountable union 删除一批集合。

因 F∩P_k、F∩N_k 均为正测度，若某限制仅在删去 null set 后才声称 Hölder，也可对剩余正测度集合重用同一论证。特别不能由 Lusin 的连续限制推出 Lipschitz 或正 Hölder 限制；本例已连续，但没有任一正测度 Hölder restriction。

## 7. 标量反攻检查：为什么更弱说法不够

以下替代均不能证明目标：只找一条趋 x0 的坏点列而未保点列在 F；只证每点 full-domain 振荡而允许 F 避开高低窗；只证 h 非 Lipschitz 而留 α<1；或只给一族随 α/F 改变的函数。本稿用 density、两个固定比例窗、(2)(3) 和 αk³−k²，分别付清这些责任。

I_k 的两周期长度是为避免 density point 相位落在极大值附近而只见单侧窗；任意相位的整两周期皆有同样高低集合长度。无需把 x0 或点对选成 rational，也不使用 F 的开性、闭性、AD、区间或正 lower density 常数。正 Lebesgue 测度正是唯一测度输入。

该标量证书与 R82 phase I 的 countable-height non-Hölder endpoint inverse 作用不同：后者只是部分方向上的逆模量反攻；这里对同一连续函数上的每个正测度子集均有效，后面将通过一个真实四维角度 chart 和 Fubini 保住正 angular mass。

## 8. 独立核五维整线与显式全空间逆

令 J(x1,x2)=(−x2,x1)，v=(u,w)∈R2×R2，

    c(v)=(Ju,Jw+h(u1)e1)，
    ℓ_v={(c(v)+tv,t):t∈R}。

任意实 t 都有 det(J+tI)=1+t²>0，且

    (J+tI)^−1=(tI−J)/(1+t²)。

给任意 physical point (z1,z2,t)∈R2×R2×R，可唯一恢复

    u=(J+tI)^−1z1，
    w=(J+tI)^−1[z2−h(u1)e1]。                    (5)

(5) 连续，故 Ψ(v,t)=(c(v)+tv,t) 是整个 R5 到自身的 homeomorphism。若不同 lines 相交，height 首先迫同一 t，再由第一块 (J+tI) 迫 u 相同，第二块迫 w 相同，矛盾。不同 v 的 slopes 本来不同，所以不存在 parallel 重复码。这一证明使用实际相交点的同一 height，不允许两条线各取不同 t/s 来误证。

以上独立核算与 B 的几何责任分开；最终需实际全文读其稿，不能仅凭此自算记作 B 已获独审。h 不可导不妨碍 (5) 的连续逆，故无需 inverse function theorem、光滑 fibration 输入或对 h 加正则性。

## 9. Compact chart、canonical 恢复与角度测度

固定 slope box B=[−1,1]^4；|v|≤2、|c(v)|≤|v|+1≤3。取

    d_v=(v,1)/√(1+|v|²)， P_v=d_vd_vᵀ，
    a(v)=(c(v),0)−[(c(v),0)·d_v]d_v。

这是确切 canonical offset，P_va(v)=0，|a(v)|≤3。v↦(a(v),P_v) 连续，B 上的像 C_B compact；P_v 决定 v，所以此参数 map 单射。它的方向像是 RP4 中一个 closed chart box，并含非空 open subset，绝不是低维方向集。

写 a=(a_sp,a5)，从任一 canonical code 与其 v 可精确恢复 height-zero 截距

    c(v)=a_sp(v)−a5(v)v。                       (6)

本式只用 d_v 第五坐标非零；在 B 上该坐标≥1/√5。方向参数也稳定：P55=1/(1+|v|²)≥1/5，v_i=Pi5/P55，所以 v↔P_v 在这个 chart 上双 Lipschitz。取正第五坐标的 sphere lift，其四维 surface Jacobian 为

    J_ang(v)=(1+|v|²)^(−5/2)∈[5^(−5/2),1]。     (7)

因此四维 Lebesgue 正测度与 chart 上标准 angular 正测度等价，RP 归一化只改固定常数。这里不是给未授的 arbitrary C 选择；C_B 自己就是显式 slope 图，方向 inverse 已由 Pi5/P55 实际恢复。

## 10. 任意正角度子集上的 canonical Hölder 反证

设可测 E⊂B 且 |E|>0，反设存在 α>0、L<∞，对全部 v,v′∈E 有

    |a(v)−a(v′)|≤L |v−v′|^α。                  (8)

若 α>1，用 diam B≤4 将 (8) 先降为 exponent 1 的估计（常数至多 L4^(α−1)）。记 α0=min(α,1)。由 (6)、|a5|≤3、|v|≤2，

    |c(v)−c(v′)|
       ≤3|a(v)−a(v′)|+3|v−v′|
       ≤L′ |v−v′|^α0，                         (9)

其中 L′ 有限，只依 L、α 和 B；低于 1 的指数用 |v−v′|≤4 吸收线性项。不能声称 smooth correction 自动保 α>1，故先降阶不可漏。

由 Fubini，存在固定 (u2,w1,w2) 使

    F={x∈[−1,1]:(x,u2,w1,w2)∈E}

可测且 |F|>0。在该 fibre 上，c 的第三坐标恰为 −w2+h(x)，其它固定项不会改变它；|v−v′|=|x−y|。于是 (9) 给 h|F 是 α0-Hölder，与 §§3–6 矛盾。故 (8) 在任何正 Lebesgue4 集 E 上都不可能。

结合 (7)，结论涵盖每个可测正 angular-measure 子族。若用方向球面/无向 P 的自然 metric 作 Hölder domain，chart 双 Lipschitz 仍给同一矛盾。并且 canonical joint-code metric 至少包含 offset 差，所以把 offset 换成整个 code map 也不能免费得到正测度 Hölder restriction。这一步没有把 arbitrary correlated E 当 product；只用一次真实 positive-fibre Fubini。

## 11. 完整模型边界和反例可用于何处

此例全空间族 v∈R4 是 genuine skew whole-line fibration，wholeunion=R5。但它不是 compact full-RP4 family：方向漏 horizontal hyperplane，且 v→∞ 时 canonical offset 亦无界。具体 c·v=h(u1)w1、|c|≥|v|−1；在 |v|≥1 时，故

    |a(v)|²=|c|²−(c·v)²/(1+|v|²)
            ≥(|v|−1)²−1→∞。

限制到 B 才有 compact C_B，其 direction box 有内点但不是全部 RP4。S(C_B) 包含 Ψ(int B×(−1,1)) 这个非空 open 集，故其 Hausdorff 维数是 5；不符合 R81 假低维 dim<n−1 输入，也不制造 Kakeya 低维反例。B 的边界使全 RP 连续 selector 的 proper-bundle contradiction 不适用，不能偷把本 chart 改成 closed 无边界 RP base。

真正被反驳的是：单靠局部 compact、整线不交、full-dimensional angular chart，甚至有全空间连续 fibration，就可抽一个正 angular mass 且具任意正 Hölder 模量的 canonical direction图。若另授 global full-RP compact、Hausdorff 低维、代数/光滑或多尺度质量假设，是否可正则化仍未由本例回答。不把此 proper-class 反攻称 no-family、ordinary gain、重大结果或新 source theorem。

## 12. 实际独审状态、依赖和停止

已实际全文读更新 spec 五节及 macro 六节；标量 proof 直接依统一收敛、Lebesgue density theorem、有限和均值定理与 Fubini，几何直接依 J+tI 的显式逆、canonical projection 和 slope-chart Jacobian。没有调用 Harrison/KM 的 wholeproof 来填分析或几何步骤，亦未进行新的官方 bytes/版本核。标准高级输入的文献陈述和本项目实际核算分层，未经外部同行评审。

当前已实际全文逐式独读 B 十二节 notes/20_dimension_lifting/disjoint_lines/R0082_triangular_skew_fibration_and_angular_mass_audit.md 及 root 十二节 notes/20_dimension_lifting/disjoint_lines/R0082_open_angular_chart_no_holder_regularization.md，无必须修正项。B 的四周期 sin±3/4 版本与本人两周期 sin±1/2 版本均独立支付 density、低频和尾界；几何 A_t 逆、真实同 height、canonical 截距恢复、Jacobian、α>1 降阶、Fubini 的全部正 measure 量词和 global/compact-chart 范围亦逐项核过。root 整合 §§3–5 与 §§6–11 在该限定范围完整。A 自己的分析正证由 B/root 另行实际独核，不计自审为独立审查。root §12 新下载 Harrison/Murphy 的读域只记为 root 的一手对照，本人没有伪记该 PDF 全文新阅读或高级 wholeproof 重证。没有做有限样本计算来替连续证明，也没有获授权 formal/元数据/Git 操作。

停止范围是固定 h 的全部 F/α/L 与 compact full-dimensional chart 反攻全部付清或报告精确 gap；不继续频率、球半径或 skew-block 常数变体，不以正确反攻冲淡完整 ordinary/general Goal。当前未发现本稿内部未付的数学项，仍待实际双独审；不提前认重大性、新颖性或未来同步。
