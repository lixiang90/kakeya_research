# R0086：原 clock、全参数 lift 与实际方向的正式审查

2026-10-18，A。下列明确条件和证书全文通过，无未解决强制项；未经外部同行评审。此审查不证明或反证完整欧氏 Kakeya，不新增 ID、重大性或优先权声明。

## 1. 实际全文范围、独立性与来源等级

已 fresh 实际全文读当前 root《R0086_full_clock_resolvent_and_actual_direction_certificate》8节、A《R0086_actual_Du_lift_qualification》12节、B《R0086_Du_construction_and_direction_completion》12节、working_spec5及末尾资格补锁、终 macro6、next6。工具合并输出有截断时又单独读回 B §§10–12 和 A §§1–5；最后读回 root §4 的 displayed-only 澄清、macro §§3–4 和 next §2 的同一范围收紧，未把旧稿或未读范围冒当前终稿。

本轮还实际全文读 Du2610.05404v1 的 HTML §§1–3及参考文献、当前归档 text physical1–5；读 Nadjimzadah2609.06299v1 的 Def2.1、Prop2.2及其完整 §3 proof、相关 Prop2.5(ii)，并对照 R50 全时变分范围。R81 已有完整 Du HTML 阅读，此轮不称首次发现或新版本。HTML 日期 October4、served PDF 正文 October6 的区别已保留；本代理未视觉检查 PDF 或新算官方 bytes，不能预认证 root 未来的文献计数／字节。

A 参与了变分必要条件和显式有损 lift，不能将自己的 A12 当独立审查；这些已由 root/B 实际全文独核。本文重点独立核 root 的整合及原矩形／正体积、B 的显式构造／completion。B 对2503.15760v3的 basic/coney 陈述有其实际读域；本人未冒全文读或新独证该高级 projection proof。matching Hausdorff lower 与 Prop2.2 的一般理论依赖仍明列具名层次；本证书的否定结论不使用 matching lower。

## 2. 原构造、全 clock 和 direction-family 的准确范围

独立核了二进制 Q 的 compactness、满平方投影及 prefix/tail 恒等式：跨 prefix/tail 项确为 r x0 y′，双 tail 项为 r²z′。4^n 个直径 O(r) pieces 给所有 dyadic scales 的 upper-box≤2，投影给 Hausdorff≥2，因此 Q、固定仿射 Q_s 和有 Lipschitz 逆的 E 三种相关维数均为2。对原 (p,q) 小球，a=q+p²/2 在 Q_s 的满 (p,a) 矩形范围中，所取 b 和 w 有固定界，真实曲线参数覆盖没有被预先删掉。

Ψ 与其所写逆在有关 bounded 区域固定 bi-Lipschitz；代入原 E，整个 |t|≤ε 的曲线精确变成 (a+tp,b+t p²/2,t)。prefix 误差给 |U|≤CR、|V−p0U|≤CR²，因此固定条件数的 1×R×R² 盒及 O(R^-5) 个 R² 球给真正全 upper-box≤5/2，不是只一列稀疏尺度。B 的 phase/Hörmander 矩阵、det=1+2tp−t²、worst-compression 的 coefficient/mixed-partial 矛盾也逐式通过。matching lower 仍调用具名 coney projection 与 slicing，而非本文新重证。

关键已修范围正确：一维 parabola 是原 displayed labels 所供应的直线方向 [(p,p²/2,1)]，q 只改 intercept，不能把该方向 Jacobian 当 K′ 内所有偶然线段的分类。原矩形事实上另含斜线。δ-net 的两个相位方向参数可压进仅 O(δ^-1) 个 displayed 方向帽，故原方向分离或 cap upper 不免费继承。当前主稿、A/B、macro 和 next 均保持这一限定，不靠一个 rank 计算宣称集合没有其它线段。

## 3. 任意有限 s 的全时变分与严格 proper 矛盾

零损失方向 rank 在 m=2+s 维中使 J=D_(p,q,ρ)Θ 是 m×m 可逆矩阵；s=0 同样成立。固定同一个参数内点 P，T(t)=D_zπ_t(a(P)+tΘ(P))，W=a_w(P)。因原 X_w=I2 且 Θ_w=0，链式法则对每个原 t 精确给 TW=I2。另设 C=a_(p,q,ρ)J^-1、B=[I2 0]J^-1，有

    T(t)(C+tI_m)=F(t)B， F(t)=−t[[1+p0t+t²,t],[t,1]]。

矩阵尺寸分别是 T:2×m、W:m×2、C:m×m、B:2×m，均匹配。未要求原 π affine 或解析，未把跨参数点的 Jacobian 当同一常矩阵；所有常矩阵只在同一个 P 取值。

det(C+tI) 是首一非零多项式，detF=t²(1+p0t)。在任何非退化原时间区间内删掉有限个零点，仍有非空开子区间，故可推出 F^-1=B(C+tI)^-1W。两边作为有理函数在一个开区间相等，清分母后是多项式恒等；右边 strictly proper，形式无穷远为 O(1/t)。左边 entry22 为 −(1+p0t+t²)/[t(1+p0t)]，p0≠0 时有非零极限 −1/p0，p0=0 时为 −t−1/t。两种情况完整覆盖，均矛盾。

这个步骤不在几何上把 clock、π 或 lines 延到无穷远，也不靠有限 t-jets 配对。因此全部有限 codimension、原 clock、全开 w/p/q/ρ、Θ 独立 w 的 smooth (s,0)-lift 确被排除。R50 对 parameter-linear 目标的双向分类不能原样套 p² 目标；本轮只正确使用其同点变分的必要方向，属于旧方法的实际应用。

## 4. 显式有损 lift、原矩形与实际 t³ 体积

独立代入核 A/root/B 的 (3,1)-lift：π_t(z)=(z1+t z3+t²z5,z2+t z4)，a=(w1,w2,−p−r1,−q−r2,−q−p²/2−r3)，Θ=(r1,r2,r3,−p,−p)。前两列保证空间 submersion，沿 a+tΘ 的所有 t 精确得原 X。Θ 的 r1/r2/r3 三列独立，p 列再贡献1维，q 列为0，故 rank4=N−1−ν、s3、ν1；不是“无任何 lift”。compact-buffer 与原 whole clock 可以共同选择。

丢 z5 后的真实 R5 slopes=(r1,r2,r3,−p,1) 含 open patch；不能只因一般 fiber upper 2.5+3=5.5 超过5就宣布实际失败。更强的原实体反攻成立：取二进制 e1=1、以后 e=0，f1=0，则 x=1/2、z=y/2、p=b=0、a=q∈[−s0/2,0]。这是真实 Q_s 子集，没有添加自由位置。

在这片上，投影点为 (−a+t r1,t r2,−r1+t r3,−a−r2,t)。固定 t 的前四坐标关于 (a,r1,r2,r3) 的 determinant 恰 t³；也能由第2、4、1、3坐标依次恢复 r2、a、r1、r3。取原 a 内区间、原 ρ-ball 内 box 和 t∈[ε/4,ε/2]，实际 image 的5体积至少 |I_a||R0|∫t³dt>0。只反这个 specific full-E/full-ρ 的投影构造，不泛推所有有损 lifts、只挑某个更小 selector 或更小 fiber 子集皆满维。

一般 Prop2.2 的有效 ambient 是 M=3+s−ν，而现有 guaranteed upper=s+2.5=M+ν−0.5。前节只迫 ν≥1，所以该通用预算不能给 strict upper<M；它不证明所有实际 inverse subsets 达到 upper。缺少更小 fiber 的新原质量机制仍必须诚实保留。

## 5. 补齐、restriction 与两种 density 的反攻

root/B 的实际矩形还严格排独立旋转并：在负 a 内区间、一个小 open φ 区间、原 t 内区间上，(a,φ,t)↦(a cosφ,a sinφ,t) 的绝对 Jacobian 为 |a|>0。因此同一 K′ 的这些旋转并有正3体积，乘有内点的自由盒则正 ambient 体积。B 的自由 missing-slope q completion 也确含 (a,qt,t)，在非零 t 子区间的 Jacobian 非零，是真正 open wedge。均不是从一个不够强的 upper bound 推出满维，且只排所列独立 completion，不排依赖原 labels 的其它方案。

产品上界 2.5+k 及其明显继承方向的 k+1 维预算核过；不把它当所有额外线段已分类。finite/countable rotations 对 displayed 方向像的低维结论也只用于这些 labels。若取 dense rotations 的 closure，原矩形产生的柱体仍进入 closure，不能免费以闭包修紧性而保低维。

whole-label restriction 只可能缩小已验证的方向覆盖。保原 entire clock 的包含关系与任意 shading 是不同输入：Ψ 的 fixed bi-Lipschitz/Jacobian 使同一 measurable marks 的逐管或平均 density 比较合法，但不保原 direction separation。仅平均 λ 时，heavy 到逐管 λ/2 只能保证至少 λW/2 原权；未归一 cap upper 可继承，原所有方向和原 W 不免费保。任意正 density 或 near-full marks 均不能凭本 source 自动恢复完整 unit segment，也不构成一个 uniform all-λ/weighted finite 定理。原 2ε clock 固定，若真有满方向直段可统一 dilation 成单位长，但 dilation 不创造方向。

## 6. 最终全文通过、修正记录与停止边界

最终 root8、A12、B12、working_spec5及补锁、macro6、next6在上述明确范围全文通过，无未解决强制项。重要范围修正已 actual 读回：root §4、A §§3/10/12、B §7，以及 macro §§3–4、next §2 均只指 displayed 方向，不将其升级为全部 incidental segments 的分类。matching 2.5 lower 的高级依赖未冒新独证；原 PDF 页数/版本日期不冒首次阅读全文或新版本。

Nadjimzadah Prop2.2 的蕴含方向保持正确：合格 lift 加高维 classical lower 推 curved lower；先真有零损失 lift 才可用 curved strict upper 构造 classical counter。本例在完整原定义内没有这种 lift，而已明确给出的有损构造实际正5体积。否定不覆盖换 clock、Θ 依 w、粗糙 w-selector、仅 E 上非全平移的另一构造、非 smooth 方法、所有有损 lifts 或所有更小 inverse subsets，不能将未覆盖自由度换名续同门。

macro/next完整四路径与冻结范围已核：当前无 qualified 新 gain，主 ordinary/full-branch-saving streak9 不清零；本 source 的原 clock/lift、rotation/product/ambient 模板停止，Goal 仍是完整高维／一般 Kakeya 或真实满方向反例，不以负面资格门完成。没有新 ID、ordinary 界、重大性或 priority 声明；具名 wholeproof 的使用与本项目自包含计算、内部独审与外部同行评审分开，未经外部同行评审。本文不预认证后续 metadata、Git、同步或 future receipt。
