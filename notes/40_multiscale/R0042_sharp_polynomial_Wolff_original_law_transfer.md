# R0042：锐 polynomial-Wolff 输入、原质量转移与实际来源门槛

2026-10-17，root。本轮主任务是检验新 BS 输入能否合法进入既有五维机制，而非假设它已经给出正增益。引用 Binyamini–Salant arXiv:2609.24135v1 Theorem1（下称 BS）；该具名定理的高级 #o-minimal 输入未由本项目从零独证。本文的有限加权和仿射计算供内部逐步独审，不登记新结果 ID，不宣新颖或重大；未经外部同行评审。

## 1. 原命题、量词和停止条件

固定整数 n≥2。BS 对任意 0<δ,λ≤1、方向角 δ-separated 的有限 δ-tubes 和同一个复杂度 E 的半代数 S 给出 |S|≥c_n #T λ^n δ^(n−1)/P_n(E)。E 是 presentation 中多项式次数总和，n 固定；可放大 P_n(E)≤C_n(1+E)^{A_n}。一般 o-minimal 的 C(S)不等于有效的 poly(E)，不混用。Theorem1 的 λ 没有旧 Conjecture1.1.1 的 λ≥δ 限制。

本轮检验三件事：保任意原权的平均形式；共同 clock/共同仿射变换后的准确费用；WZ Prop17.2 是否实际提供这种输入的祖先。前两件是具名定理的直接推论，第三件必须读实际量词，不能从图像推测。平均 density 与逐管 density 分别核；原删选和归一化分别核。若得到的只是旧 theorem 的等价加权形式、或实际来源/复杂度尚缺，则记录接口并停止，不为新输入发明独立结果 ID，更不宣称五维 κ≤ζ。

独立反攻：重复方向/大跨度权；短 clock；小质量 parent；不同 index 使用不同 frame；任意 joint-AD/CW 配置的祖先；所有尺度 direction Frostman 是否已包含同一仿射计算；S 的实际复杂度；用 ε 改善替代 fixed-power gain。数学总目标和完成标准不变。

## 2. 有限原权：tail、平均及双向闭包

有限原管可带重复 indices，权 w_i≥0，总 W>0；取 bounded-slope chart，方向空间分为直径 O(δ)的规则 bins，每 bin 原权至多 α。有限 coloring 后，同色不同 bins 的任意代表方向 δ-separated；常数只依 n。令 q_i=|T_i∩S|/|T_i|，M=Σw_i q_i。对每 s>0，从 q_i≥s 的每个非空 bin 取一个原管，BS 与 bin 质量上界给

    W_s=Σ_{q_i≥s}w_i ≤ min(W,B s^(−n)),
    B=C_n α P_n(E)|S|δ^(1−n).                         (1)

任意权跨度不花 dyadic log。若 0<B<W，令 a=(B/W)^{1/n}，layer cake 给

    M=∫_0^1 W_s ds ≤ Wa+B∫_a^1 s^(−n)ds
      ≤ n/(n−1) W^{1−1/n}B^{1/n}.

B≥W 时 M≤W≤W^{1−1/n}B^{1/n}；B=0 时 M=0。故

    |S|≥c_n δ^(n−1) M^n/[α W^(n−1)P_n(E)].            (2)

相反，以方向-separated 各管权1、W=#T、α=1、M≥λW，(2)即给 BS。对任意子族再调用 BS 得(1)，反向取一层又回逐管形式。因此这是 **all-subfamily BS 的等价有限加权扩展**，不是新正幂机制。简单 heavy filter 导致 M^{n+1}并非必需，但纠正它也不是新 Kakeya 定理。

未归一化 restriction 保留 bin 上界 α，总 W与M须改成实际保留值；除以 parent mass p 时 W、M、α同时除 p，(2)尺度齐次。不得将 α/W 还原为删选前的值。逐管假设给 tail，平均假设经积分得到(2)，两者不混淆。

## 3. 适合原 law 的 polynomial-Wolff 性质

为精确处理 clock，使用 graph cylinder

    T_i={ (b_i+t a_i+u,t): 0≤t≤1, u∈B^{n−1}(0,δ) }.

各斜率有界。BS §6 在 Claim6.1 后正对这种 1×δ 管证明相同估计；亦可用固定数量 chart/等长柱覆盖比较。这里直接以该 graph 形式为具名输入，不删除 δ 级端部后冒称所有微小 λ 均保留。有限管概率 ν=Σ_i w_i δ_{T_i}，Σw_i=1（此处δ_{T_i}是point mass，非管宽），称满足如下 tail 条件，常数记 C0：对所有半代数 S、所有 E≥1及所有 0<λ≤1，

    ν{i: |T_i∩S|/|T_i|≥λ}
       ≤ C0 P_n(E)|S| λ^(−n).                       (PW)

BS 与方向 bin α≤Kδ^(n−1) 给 C0≤C_n K。若只有 N 根均匀方向-separated 管，则 C0≤C_n/(Nδ^(n−1))，不能自动取 O(1)。此性质的每个 S 都必须是同一个空间中的同一个测试集合。

PW 对任意原权 restriction 的未归一化 law 保同 C0；其质量为 p 的 restriction 归一化后常数为 C0/p。PW 积分给概率平均形式 |S|≥c_n (∫q_i dν)^n/[C0P_n(E)]；对 restricted law 先用其实际总质量，不能保留旧总质量1而丢掉 p^{n−1}。

## 4. 共同 parent、短 clock 与准确仿射费用

选任意 index 子集 I，原质量 p=ν(I)>0。只取共同 clock J=[t0,t0+q]⊂[0,1]，0<q≤1，且所有所选管用同一个变换

    F(x,t)=((x−x0−a0(t−t0))/r,(t−t0)/q),  0<r≤1.

假定变换后斜率仍有界且 δ/r≤1；于是新管 T'_i=F(T_i∩{t∈J})是 width δ/r、unit-clock graph cylinders，方向变成 q(a_i−a0)/r。F 的体积 Jacobian 为 1/(r^(n−1)q)。对新半代数 S' 令 S=F^(−1)S'：仿射代入不增加多项式次数总和，系数大小不算 presentation E；|S|=r^(n−1)q|S'|。若 S' 中的新管占比≥λ，则原 whole T_i 在 S 中的占比≥qλ。因此

    (ν|I)/p {new fraction≥λ}
      ≤ (C0/p)P_n(E) r^(n−1)q |S'|(qλ)^(−n)
      = C0 r^(n−1)/(p q^(n−1)) P_n(E)|S'|λ^(−n).  (3)

新 PW 常数可取 **C'=C0 r^(n−1)/(p q^(n−1))**。n=5 即 C'=C0 r^4/(p q^4)。此为已假定 PW 的精确合法闭包；不是实际 §18 所有操作的闭包证明。

whole-clock q=1、p≈r^4 时费用抵消；短 clock 留 q^(−4)，不能通过 time normalization 抹掉。新平均 intersection≥λ 时(3)给

    |S'|≥c (p/r^4)q^4 λ^5/[C0P_5(E)].              (4)

这也由(2)在 restricted total W=p、M≥p qλ、α≈δ^4下直接得到。若错误地取 W=1会多丢 p^4。逐管 restriction 与平均 restriction 在这两个推导中均付同一费用。

测试整个有界 ambient ball（所有新管包含其中）还要求 C'P_n(O(1))≳1。若某个参数表给 C'趋0，则原 parent mass 或新 bounded geometry 前提不可能同时成立，不能宣免费体积大于常数。不同 index 的 frame F_i 产生不同 S_i，PW 不能对它们逐个测试后免去合并费用。Projective、coarsening、tube replacement 也未由(3)自动涵盖。

## 5. 与 direction Frostman 的排重校准

若原 law 在所有角尺度 h≥δ 都满足方向 ball 质量≤K h^(n−1)，上述共同 affine/crop 后方向 ball h' 的质量上界同样为

    K (r/q)^(n−1) h'^(n−1)/p.

所以 **单独(3)的费用核算也已由原方向 law 得到**；不因用 PW 名称就成为新高维机制。方向 coarsening 若只是 O(ρ)内代表替换，原权 pushforward 的 ρ-bin cap亦可直接保留；但 cardinal reweight、incidence selection、每 parent frame/改变 clock须另核。

PW 本身并不强迫这种方向 Frostman。校准例：在横截面规则 δ 网放互相有界重叠的平行 graph cylinders，均匀权约 δ^(n−1)。其平均 whole-tube visit measure 的 Lebesgue density≤C_n。于是任意可测 S 都有 ∫q_i dν≤C_n|S|，Markov 给 ν{q_i≥λ}≤C_n|S|/λ≤C_n|S|/λ^n，PW 常数 O(1)；所有方向却相同。此例没有 positive κ，小 union 反例不成立；仅证明 **PW 的 law 类可比原满维方向 Frostman 更宽**。它不能替代实际极值类的闭包或证明任意 AD/CW 自动 PW。

新 BS 相比旧输入真正值得检验的是当 E 随 δ 增长时仍有明确 polynomial cost。fixed-degree 且只需任意小 δ^ε 的旧应用，不因去掉 ε 就自动补 fixed κ gap。

## 6. 实际 WZ 来源检查：目前没有免费祖先

实际读 versioned WZ *Kakeya and Furstenberg Problems for Sticky Sets of Tubes* PDF65–69：Definition17.1 以所有 joint tube-parameter (d−1)-AD、CW family及平均 δ^η shading 定义 K_d(κ)。Prop17.2/18.1 的 κ 是这个类的极值，不是 direction-separated 初始类的 κ。Prop18.2 起点 lines3489–3495也只有同一类。

因此无法追认“任意已存 Def17.4 actual五维配置均来自一个满方向-separated祖先”。用 BS 强化起点必须明写新极值类并重新检查原 recurrence 所调用的每个 coarse/parent/shading 输出留在类中。特别 §18 Step3 用 coarsened family及均匀性，Step4 再调用 K_d(κ)；仅保一个 fine affine parent 的(3)不足以合法替换这个循环。该失败是实际量词/闭包缺口，不是 full(3,3) positive κ的反例。

反方向也不能免费：满方向网的任意anchors不自动joint4-AD。B独审给显式校准：δ=ε²，每坐标A,B各取整数0,…,ε^(−1)−1，令方向v=εA+δB、intercept b=εB。v遍历完整δ网，总数δ^(−4)，却joint(b,v)为ε-separated：B不同由b分离，B相同而A不同由v分离。r=ε/10的parameter ball只含一个index，而joint4-AD lower要求约(r/δ)^4/K，即约δ^(−2)/K，K仅subpower时不成立。角分离与斜率分离在有界chart下差固定常数，可按固定color调整尺度。此为输入校准，不是Kakeya反例；一般到sticky必须另付。

本文没有证明 §18 的 strengthened-class extraction，也没有构造实际 semialgebraic S'，使原 marks 密度、|S'| upper与复杂度费用留出 κ strict saving。一个 native polynomial 的低度，不等于整 visited union 的低复杂度；任意 δ-cells 并的 E 可能已花掉所有节省。

## 7. 真正需要的 strict saving 与本轮退出

直接方向形式中，若实际 probability law 的 α≤δ^(4−χ)、平均 M≥δ^u、P_5(E)≤Cδ^(−A_5θ)、E≤δ^(−θ)，(2)仅给 |S|≥cδ^(χ+5u+A_5θ)。要矛盾于 |S|≤δ^κ，须真实付出 χ+5u+A_5θ<κ；这只是预算，不许当新假设证明高维。继承形式则还须加入 log(C')/log(1/δ)的实际费用。

本轮已完成输入有限原权/仿射核算及实际初始量词检查，**没有证明新的五维 gain**。不新增ID，不解除旧CP⇔PM、BSG/action/carry、低S、fineflatflake或独立构造参数的冻结。唯一下一有界 main 是实际 §18 strengthened-PW 极值类闭包测试：若不能连 Step4 调用都保留，立即停止此 inheritance 路线；若闭包通过而只重述旧 direction law且无复杂度新作用，也不得宣传新机制。

## 8. 审查状态

提交两代理实际全文独审本文8节、root macro、唯一next spec及对方全文；最终状态以正式 review及root integration为准。BS 原定理是文献输入，本文(1)–(4)为可逐步检查的有限推论，不能把“文献声明、项目推导、实际未付source应用”合成一个已证普通高维Kakeya结论。
