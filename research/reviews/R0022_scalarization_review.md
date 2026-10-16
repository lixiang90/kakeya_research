# R0022：weighted scalarization 与 LOCAL-AFF 整合独审

2026-10-17，`audit_four_dimensional`。独立审查 B 的 `R0022_scalarization_counterattack.md` 和 root 的 `R0022_fixed_scale_affine_preparation.md`，并核对后者引用的 `R0022_time_restriction_closure.md`。A 的 observed-source稿由本人编写，其原W恢复表不在本报告中冒充独立自审；该部分另由B/root审查。

**结论：** 有限bounded-range scalarization证明通过。LOCAL-AFF整合终稿也通过：原Euclidean tube cap支付coarse vector band；每个coarse cell取原fine代表；ABC的“充分小”使用named定理的真实阈值；LA反证的source损失与后续低速准备损失分开。这些必要约定均已核对root终稿明确纳入，无待修的数学问题。该结论仍条件于named WZ Theorem21.2、Lemma19.2等高级输入，不认证其完整高级证明、整个mixed32或Kakeya结果。

## 1. 原权rich triples的下界

B稿假设原时间概率ν对长至少d的interval有`ν(I)≤K_t|I|`。取`g=b/(1000K_t)`，并令`b≥C_mK_t(d+w)`，则g≥d、w≤g/16。某tube的原rich set S质量β≥b；S³中一对时间间距小于g的质量至多`2K_tgβ²`，三对合计小于固定小比例β³。剩下的六种时间顺序对称，因此ordered separated triples有质量≥cb³。

这个下界在ν³上成立，允许任意原atoms与权重；没有先把S重新归一化、赋AD，或把一条rich tube中的离散点数当作连续长度。所有gap删除费用已在b、K_t和d中。

## 2. 自适应拟合线不需无限union bound

对ordered triple t₁<t₂<t₃，B稿选中间点的凸插值残差

    V=F(t₂)−[(t₃−t₂)F(t₁)+(t₂−t₁)F(t₃)]/(t₃−t₁).

两系数非负且和为1，故三个scalar vertical errors≤W时`|λ·V|≤2W`，没有另一个1/g。固定端点后，小残差`|V|≤h`的中间点原质量≤a，正是vector affine fit假设；对端点积分不增加它。

若|V|>h，选绝对值最大的坐标，条件于其余λ坐标后允许λ_j的区间长≤C_mW/h。因λ在[1,2]^m中独立均匀，Fubini给全体ordered residual统计量期望≤a+C_mW/h。Bad_b点态蕴含该统计量≥cb³，所以Markov一次控制全部adaptive scalar lines。统计量是有限个slab指标的原加权和，可测；没有将随机选出的rich line与固定参数作不合法交换。

## 3. Euclidean tube垂直化的两种版本

Lip版中，两个gap≥g的rich点确实给单位法向的vertical分量下界`c_m/(1+L)`；于是W=C_m(1+L)w，概率upper为`Cb⁻³[a+(1+L)w/h]`。该版本自身正确，但实际source不能免费用它，因为dyadic Lip不蕴含全局Euclidean Lip。

实际所用第6节只要求diam F≤M。相同两点给

    |n₀|g≤2√m M|n₁|+2w,
    |n₁|≥c_m g/(1+M).

因此`W=C_m(1+M)w/g`，结合第2节得到

    Pr(Bad_b)≤C_m[a/b³+(1+M)K_t w/(h b⁴)].

b⁻⁴费用真实保留。ordered residual无1/g与垂直化需1/g是两个不同步骤，稿件没有混淆。原坐标的finite rounding只增加Euclidean tube宽`d_round+C_me_round`，无需控制拟合斜率。不能反过来从未付的任意coarse vertical band直接传回fine band。

## 4. 有限A反例的范围

B稿第7节取r=1/n、n³个三维r-grid ξ_j和互异`x_j=j r⁴/10`。全部x在一个O(r)区间中，但`N_r(A)≈r⁻³`；任意有界λ的image只需O(r⁻¹)个r-balls覆盖。因此“有限函数graph”一词单独不保projection cardinality。

另一方面，若每个first-coordinate r-bin最多M个A-cells，一个image r-ball只跨O(1)个该bin，确实得到`N_r(Π_λ A)≥c M⁻¹N_r(A)`及bounded preimage multiplicity。该source可用结构来自原ξ-coherence，反例不满足它；B稿没有把有限反例升级为完整source反例。

## 5. 整合稿的coarse band修复与单值代表

原fine vector band宽为`h₀≈ρ^ε₀/L_f`；coarse time rounding对斜率R产生|R|s，因此不能直接继承任意R的h₀-fit上界。root终稿改取Euclidean tube宽`h=ρ^(4ε₀)`：轴的time分量≥√h时，管内点属于误差O(√h)≪h₀的vector affine band；否则整管time跨度O(√h)，由time packing控制。这只用F有界与原fine nonfit，不用F的Euclidean Lip。

heavy cells满足`P K^(−B₀)≤n_b≤P`，故uniform coarse Euclidean tube质量可用fine tube原质量除以真实lower capacity；O(s)的Euclidean rounding远小于h。有限bounded box中的任意vertical h-band又位于一条向量直线的Ch邻域，相关线段长O_m(1)，可由O_m(1)根unit Ch-tubes覆盖。这样合法取得供scalarization使用的coarse vector band cap。

这里`δ^(a/2)≤ρ^(2a)`，因为ρ≥δ^(1/4)；所以fine tube上界中的`K[δ^(a/2)+ρ^(2ε₀)+δ/ρ]`在所有source损失后可降为`ρ^χ、χ=min(a,ε₀)`。固定倍h的tube查询仍有足够ε₀余量。

coarse B_h不必在其coarse time中心上单值。root已补：每occupied cell选一个真正原fine time与F值作代表，不同cells原indices不交，故时间distinct；uniform law对长≥Cs的interval仍有K_t cap。代表点未必s-separated，但有限scalarization不要求它，只要求上述interval cap，base d=Cs。代表离原coarse中心O(s)，原g关系只再付O(s)。最后再舍入到s-grid，以first time的K-fibre cap控制碰撞，提供ABC所需s-separated carrier。未免费丢掉原fine multiplicity。

## 6. scalarization和ABC参数

整合稿取

    h=ρ^(4ε₀), χ=min(a,ε₀), β=χ/100,
    b=ρ^β, w=ρ^(8ε₀).

于是`a₀/b³≤ρ^(χ−3β)`，另一项≤`K^Cρ^(4ε₀−4β)`，两指数均正。η在a、µ、ε₀之后取小，使`b≫K_t(s+w)`且概率<1/2。故存在同一个有界λ控制所有width-w scalar tubes；同一λ作用于A和整个g，未对每个源世界单独选λ。

投影/重分箱后的K次方费用可把tube质量保守降为`ρ^(β/2)`。取ABC`ζ₀=ζ/4、ε₁=9ε₀、ε₂=β/4`；当η足够小时，`s^(9ε₀)≤ρ^(8ε₀)=w`且`K^Cρ^(β/2)≤s^(β/4)`，因此正好提供named定理所需的宽度与质量。

参数有两项必须按真实量词理解：

1. ε₀须依ζ充分小，使9ε₀落在Theorem21.2对ζ₀的实际允许区间。只给`ε₀<ζ/10000`或`ε₁≤ζ₀/100`的数值比较，不能替代未给显式函数的“sufficiently small”。
2. §2–7 LA反证中仅删去小质量整windows，K_src=δ^(−C_aη)，所以regularity参数与graph参数均可在η后取小时成为任意小的`O_a(η/µ)`。后续low-velocity/time restriction的`K_prep=δ^(−C(η+a)/(γζ))`含实际a-loss，不可回灌scalarization/ABC前半段，否则其费用未必小于β≈a/100。

上述两项已经逐字核对整合终稿§1与§7补入；这里保留其数学原因，避免后续恢复时再次混同参数。

PDF91的η_reg与barη_graph是两个不同阈值，root分开列出；二者分别依ABC的真实输入选择，不把它们合成一个未经检查的η。named标量ABC给`#A₂≥K⁻C s^(−1−κ+ζ₀)`，与`#A₂≤K/s`冲突；κ>ζ的固定余量足以吸收可任意小的source损失。

## 7. 全局删选、低速度与认证范围

从`ΣM_J<δ^aN`删除`M_J>δ^(a/2)N_J`的windows，只损δ^(a/2)N；再删过稀windows可保≥N/2。相应good-q中的nonfit只多付K；它来自原cross-time covering/incidence，未对任意q声称local lower。fixed-ρ证明不调用另一尺度的affine nonfit，仍正常使用原多尺度regularity/coherence。

只读核对time-closure稿：删整时间层保每层Y_z；coarse子并upper来自原union，lower来自其任一所属Y_z的fine AD到coarse cover转移。η'=Mη子格及相邻尺度费用有明确记录。低whole-velocityfit若携带实际全局δ^O(a)质量，可据此合法形成原time子配置；`σ=ρδ^(b/2)`处于[ρ²,ρ]，named19.2给`δ^(C(η+a)/γ−bκ/2)`，选b充分大于损失、仍小于µε₀即排除。该步骤不是从单一慢窗口调用19.2，也不直接推出首坐标r非零。

本报告通过的是有限scalarization和这些明确source接口下的LOCAL-AFF准备。高级Theorem21.2、Lemma19.2/19.4等仍是named依赖，非本轮完整重证；与R21衔接只关闭所列二次alternative的准备责任。非二次、其他mixed、一般归约和Hausdorff未解决，不构成重大/新颖性认证。
