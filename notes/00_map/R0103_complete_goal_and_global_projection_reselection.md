# R0103：完整出口重选与原访问质量的全局 Schubert 集中

2026-10-19，A 分配稿。先实际读 reselection5，再按 working5 锁定的原质量 profile 施工；固定入口及 R102 已付链不重做。以下为具名投影定理的实际 source 应用及有限代数、加权剥取证明，不是完整 κ1 排除、ordinary 新界或新 ID/major。高级原定理 wholeproof 仍具名，独立全文审查另记，未经外部同行评审。

## 1. 完整目标、已付输入与本轮真正问题

实际读 GOAL、STATE、ROADMAP 相关已冻结入口、registry 状态及 R102 next6，并复核 R102 root12。四条完整出口仍是 ordinary/HRZ、具名 seed 与递推、全部 rough sticky 分支及 ordinary 入口、真实同集全方向 strict 反例。ordinary/HRZ 原 broad/narrow 全预算没有新输入；DIM001 在已经审查的有限 seed/assembly、KT 及明列具名输入下六维 17/4 推论已付，源核验层级与 2026 priority 不是一个新的内部几何缺口。不能重开 R29/38/42 数表、R80 pivot 或 R84/87 几何闭包。R81–86、R91、R94 等弱模型或函数/拓扑障碍没有给完整反例。

本轮有不同、可实际使用的一手输入：CSWZ 引用的 He **全局** Schubert 非集中投影定理。它不是 He 矩阵 sum-product。R102 已经保原全局多 code 的质量，给同一个二维 Frostman 集 P 及每个实际 rich clock 的大子集 P_u；后者投影像只有一维。当前问题不是再假设方向非集中，而是反用原定理，把全部实际坏方向转成有**原 I 分母和逐簇尺度—质量 lower** 的必要集中证书。

## 2. 一手版本、完整定理量词与实际读取范围

实际官方 [arXiv history](https://arxiv.org/abs/1710.00795) 为 Weikun He，*Orthogonal projections of discretized sets*，v1 2017-10-02、current v2 2018-05-09；[v2 HTML](https://arxiv.org/html/1710.00795v2) 与本地提取对应。实际读 §1.1 全部 Th1/定义、§1.2 Th2/Cor3/Cor5、§1.4 Th6/Prop7/Th8 的范围区别、§2.2 的 wedge/对偶恒等式，以及 §3.1 Prop25 完整段；没有全文独证 §4 的高级主证明。PDF 提取显示 33 页、正文 Date May 10, 2018；官方 history 的版本日期 May 9，HTML 再生成 Date August 24, 2026，三者不混用。本稿没有据此冒称 PDF 视觉核验或新字节检查。

Th1：给 0<m<n、0<α<n、κ>0，存在 ε_H>0。δ 足小时，A⊂B(0,1) 及 Gr(n,m) 上任意 probability μ 若满足

    Nδ A ≥ δ^(−α+ε_H),
    Nδ(A∩B(x,ρ))/Nδ A ≤ δ^(−ε_H)ρ^κ,
    μ{V:d_angle(V,W)≤ρ} ≤ δ^(−ε_H)ρ^κ

对每 x、ρ≥δ、W∈Gr(n,n−m) 成立，则除 μ 质量 ≤δ^ε_H 的方向外，**每个** Nδ A′≥δ^ε_H Nδ A 的子集都有 Nδ π_V A′≥δ^(−mα/n−ε_H)。最后指数的 ε_H 是正增益。它允许 A′ 随 V 改变，且 μ 可原子化、可有重复方向权。Prop25 解释 Th6 的 subset 版本如何升级，不能只把 Th6 的存在子集当本轮输入。

这里 d_angle(V,W)=|det(v_1,…,v_m,w_1,…,w_(n−m))|。在 Gr(4,2) 它是两个 principal sine 的乘积，**不是**到 Schubert 集的 Riemannian 距离；metric 管状宽度不能无损替换它。Cor5 另需真实 analytic 参数族及对每 W 的横截性，不能将原 rough F_u 代入。

## 3. 同一个原 P、所有 rich u 和任意剩余访问概率

沿 R102 root §§1–7 的完整 bounded Def17 matrix33 κ1 det-large 分支。原 N≈Kδ^-4、m=|Z|、原全 T 的 CW/AD 及全部 selected visits 不改变分母。固定 anchors t,s，h=s−t、A=F_t−F_s，|h|、smin A≥σ=δ^b。R102 的全局 code 权层只损 L^C，取得

    |P|=L^±C δ^-2,
    |P∩B(x,ρ)|/|P|≤L^Cρ²,
    |P_u|≥L^-C|P|,  Nδ π_(V_u⊥)P_u≤L^Cδ^-1,
    G_u=((t−u)(F_u−F_s);(s−u)(F_u−F_t)), V_u=im G_u,
    I_rich=Σ_(u∈U) I_u≥L^-C N m.                    (1)

I_u 是原 H 管在实际 heavy 第三点的访问数，不是不同参数 cell 的个数。far clock 已逐管半保，point-heavy 后只平均保量；源角 upper 支付 code-cell 碰撞，P_u 可以随 u 改变。G_u 满列秩由 far 与 A 支付。P 固定有界，做共同固定 scalar 缩放即进单位球，δ-cover 常数可由减小 ε_H 吸收，不需 Grassmann chart 或 round 方向。

固定 q∈(0,1/4)，对 Th1 取 (n,m,α,κ)=(4,2,2,q)。取 e>0 足小且 e≤min(ε_H,q/4,1/100)，再选源损失 L^C≤δ^-ℓ，ℓ≪e,ε_H。ρ≤1 时 ρ²≤ρ^q，故 P 满足所需 point upper/size；ρ≥1 平凡。|P_u|≥δ^e|P|，而其像 upper 严格小于 δ^-1-e。任意非空 R⊂U，以原 I_u 归一得到

    μ_R=(Σ_R I_u)^−1 Σ_(u∈R) I_u δ_(V_u⊥)。

若它满足全部 cap upper δ^-eρ^q，则满足 ε_H 版假设；Th1 产生正质量 good 方向，与该方向任一实际 u 的 (1) 冲突。原子重合不会破坏这个论证：每个支持方向都已有某个大 P_u 坏见证。没有把 He 的小坏方向比例回传 uniform times，也没有给原 clock law 假定 Frostman。

## 4. 全局输入、旧局部障碍及合法使用区别

He 只测全局 μ_R 对每一个 W 和每个 ρ 的 cap，不要求在每个参数球内再相对测试。因此这是不同于 CSWZ Def1.5 local SPREAD 的合法弱入口；不据名称声两种 quantitative 常数自动等价。R14/R76 的固定结构 Schubert 障碍针对另一 ambient/输出对象；R97 scalar θ=(-β,−tβ,t) 的每球切面 O(r²) 也不是本 G_u 的恒等式。R102 的开 chart 只说明系数自由时不存在 universal 零项，仍不证明实际时间方向 cap。

例如上三角 F_u、上三角 anchors 使 G_u 的第一列在 span(e_1,e_3)。令 W=span(e_2,e_4)，则 det(G_u^T B)=0，所有 V_u⊥ 与 W 相交。R79 弱联合模型可出现此情形，但它缺 full point Φ/filled X/全 T AD4-CW，不能当完整 source 反例。相反，原 SM、满秩、time nearfull 或 full span 本身均未支付每个 W 的 cap；本轮用的是 cap 必失败，未偷加 cap。

R78 已付单 δ² 原 T 块的共同 X/action 及一张 fractional cone，未付此处保 δ^o(1) 原全 T 的全局多 code I_rich，也未给每个剩余访问 law 的多簇 profile。反向从本必要集中恢复 R78 的共同 X、完整原 source 或 CP/PM 全称正幂均未证，不能以此开旧 gain 的新名称。

## 5. 逐簇异常质量与有限剥取，不只少层覆盖

由 §3 对任意 R 的 cap 失败，存在 W、ρ≥δ，使

    μ_R{u:d_angle(V_u⊥,W)≤ρ}>δ^-eρ^q.              (2)

概率≤1 迫 ρ<δ^(e/q)。开始 R_0=U；第 j 步令 U_j 为剩余时刻中满足所选 cap 的全部 clocks，再从 R_(j−1) 删掉 U_j。它们在 **clock 标签** 上互不相交，几何 cap 可以重叠。只要 μ_U(R_(j−1))≥1/2，便有

    μ_U(U_j)>(1/2)δ^-eρ_j^q≥(1/2)δ^(q−e),
    δ≤ρ_j<δ^(e/q).                                 (3)

因此至多 ceil(2δ^(−(q−e)))≤Cδ^-q 步就使累计质量≥1/2。若剩余只是一原子，同样由 (2) 删除；不依赖 uniform 不同方向、原子下界或时钟可分性。本证明无额外 log，δ 最后小保证 cap failure 和 He 的阈值统一。

式 (3) 的绝对分母始终是 I_rich。最终覆盖 ≥(1/2)I_rich≥L^-C N m，**不是**无损固定比例的原全部 I。不能只摘录“至多 δ^-q 个非零多项式薄层”而删去 (3)；普通时窗覆盖也可能给一个无意义的层数上界。

## 6. 正确 normal 对偶与实际 native 多项式

令 B 是 W 的 4×2 正交列基，定义在 formal 变量 (u,F)∈R×Mat_2 上

    G(u,F)=((t−u)(F−F_s);(s−u)(F−F_t)),
    P_B(u,F)=det(G(u,F)^T B).                       (4)

每个 G entry 的总 degree≤2，故 P_B 总 degree≤4，系数 upper C 仅依有界原 chart；不用 F 的任何连续性。取 U_G=G(G^TG)^−1/2 的正交列基，有

    |P_B(u,F_u)|=sqrt(det(G_u^TG_u))
                      ·d_angle(V_u⊥,W).           (5)

这是 Gram determinant 与 complementary orthogonal projection 的恒等式：d_angle(V_u⊥,W)=|det(U_G^TB)|。不是 d_angle(V_u,W)。G bounded 给 (2) 上 |P_B(u,F_u)|≤Cρ_j；这里不为这个 upper 除 smin G，故没有漏掉 r/σ 的 conditioning。

native 展开也可写 det[(t−u)(F−F_s)^T B_top+(s−u)(F−F_t)^T B_bottom]，与 det(B^TG) 互为转置。次数、符号及所用固定 W 均来自同一个原 G，不是另选任意低次多项式拟合原 F。

## 7. 六个 Plücker 系数给非真空的统一 lower

仅作 formal polynomial 检验，令 u_0=(t+s)/2；无需 u_0∈Z，也不将 rough F_u 延拓到中点。此时

    G(u_0,F)=(h/2)(F_s−F;F−F_t).

置 S(a,b)=(-A^−1(a+b),b)，则 S G(u_0,F)=(h/2)(I;F−F_t)。有 ||S||≤Cσ^-1，||S^-1||≤C；B′=S^−T B 的两列 wedge 范数≥cσ²。于是

    P_B(u_0,F)=(h²/4)det(B′_top+(F−F_t)^T B′_bottom). (6)

对 H=F−F_t，右边 determinant 在六维基底

    1, H11,H12,H21,H22,det H

的系数，正好是 B′ 两列的六个 2×2 Plücker minors，至多固定符号/排列；在普通 monomial coefficient norm 下也只差固定因子。故该 coefficient norm≥ch²σ²。F_t 有界，H→F 平移的系数线性变换及其逆 bounded；将 u 设为有界 u_0 的评价是 full polynomial coefficients 上的 bounded map。因此

    cσ⁴≤||coef P_B||≤C.                            (7)

这涵盖任意 W，并不因 W 逼近退化位置失去 lower。形式上的六函数独立与实际 u↦F_u 曲线可以完全包含在零集是两回事；(7) 只排除 P_B 本身恒零，不排除后一种真实集中。

## 8. 归一厚度、原管 heavy 返回与删选边界

Q_j=P_(B_j)/||coef P_(B_j)||，系数 norm1；a_j=C_0σ^-4ρ_j，取 C_0 固定足大。由 (3)、(5)–(7)，U_j 上

    |Q_j(u,F_u)|≤a_j,
    μ_U(U_j)≥cδ^-eσ^(4q)a_j^q≥δ^(−e/2)a_j^q.      (8)

最后一个 lower 要先取 4bq<e/4、δ 最后小吸收 c；不能在归一后仍保同一 δ^-e 因子。并有 a_j≤δ^(e/(2q))<1（进一步缩小 δ 吸收 C_0），每层是实际薄层，不因 σ^-4 变成全空间查询。

设 U_* 为所有 U_j 的并，J(T) 为 T 在这些 clocks 上已经计入 I_u 的原访问数。Σ_T J(T)≥L^-C N m。以阈值 (ΣJ)/(2|H|) 删去较轻原管，至多损一半总访问；每条留下 T 有 J(T)≥L^-C m，而留下管数≥(ΣJ)/(2m)≥L^-C N。原 N、m 没有改分母，CW 的 normalized 常数在子族上至多按 N/|H′| 损 L^C。

这只给 **union U_*** 的逐管 lower。单个 U_j 仅 (3) 的平均访问 lower，不赠它 many tubes 各有 many marks；更不赠 U_j 上全部 Z/X/Y/Φ 的 nearfull 或合法新 Def17 配置。whole-index 权层与原 visits restriction 的 AD upper 可继承，AD lower、clock filled/coherence 若要组成新 source 还需另外证明。

## 9. 普通 Lipschitz 分窗的实测与证书的有限强度

只用 clock 长度 a 的平凡分窗，near-uniform clock law 给质量 O(L^C a)，不推出 δ^(−e/2)a^q（q<1）这样的异常。更危险的是 product-sine：若 plane curve 在一个长 l 窗内 Lipschitz 变动 O(K_0 l)，取 W 为中心 normal plane，则全部方向有 d_angle≤C K_0²l²，质量可达 O(l)。故 q>1/2 时，在合适 l 上可平凡生成某些 profile；working 已实际收窄 q∈(0,1/4)。对这种具体构造，厚度 a≈l²、质量 O(L^C sqrt(a))，比 (8) 要求的小 q 异常弱。此比较只拒该平凡推导，不声所有 Lip 曲线都不能真实集中。

也可严格测试“任意 Lip plane curve 自动满足此 profile”为假。取 K(z)=graph T(z)，T(z)=((z,z²);(z³,z⁵))，z∈[0,1]，V(z)=K(z)⊥。其六个 Plücker functions 为 1,z,z²,z³,z⁵,z⁶−z⁵，线性独立，系数到这组六维 polynomial 的线性映射有固定 lower；任意 W 的 normalized determinant 不是零 polynomial，degree≤6。一元 Remez sublevel 加 bounded Gram 因子给 uniform law 的

    μ{z:d_angle(V(z),W)≤ρ}≤Cρ^(1/6).

均匀 δ-net 版只多 Cδ；ρ≥δ 时仍≤Cρ^(1/6)。固定 0<q<1/6、δ 小，所有这些 cap 都不可能达到 (3) 的异常 lower。因此“有界 Lip 参数”单独不强迫本证书；实际全部坏 P_u 才是 He 反用的输入。这个 plane 校准不是完整 source 反例，也没有在本轮展开新的 curve 分类或参数方向。

## 10. 结论、实际审查层级与停止

本稿付清 He all-large-subsets 的原 P 输入、任意剩余原访问 law 的 cap failure、无 log 剥取、非零 quartic lower、归一 massscale 及 union 的原管 heavy 返回。没有从 nonspread 免费推出有理 F、共同 image/kernel、R78 一张 cone、ordinary 初始化或完整 κ1 排除。若以后只优化 q/e/ρ 或把同样异常重命名为 source 正幂，不应另开结果；真实后续要消费这个 profile 并回原 native 几何，或宏观转向不同完整出口。

实际全文读 R102 root12 和 R78 root14，旧输入范围如 §§1、4；He 的实际读取范围精确列于 §2，高级 33 页全证明未重证。R103 working5 已全文读回含 q<1/4 修改。本稿是 A 自己施工，不计自身独审；root10/B 终稿的实际全文互读及最终 formal 尚待其正式分配后补真实记录，不预写通过或认证未来 metadata/Git/sync。Goal active，无新 ID/major，未经外部同行评审。
