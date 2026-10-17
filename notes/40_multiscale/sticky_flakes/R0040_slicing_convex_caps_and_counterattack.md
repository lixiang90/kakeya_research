# R0040：真实移动grains的切片、凸聚类与反攻

2026-10-17，B。读恢复入口、R40 spec、R39完整nextspec，运行context.py；实际读LPSW2610.10603v1 §9 Steps(i)–(iii)/Props9.1–9.3及原WZ Defs17.2–17.4/19.2和R22整时间层restriction闭包。唯一主目标仍为完整actual d5/k3/ell3的κ≤ζ；下列严格接口障碍不能冒充该主命题反例。只编辑分配文件，无Git。

## 1. 问题与本轮新增信息

新输入的真正对象是flat3-flakes，不是原一维直管，也不是任意ruled3-surface。R39的局部平行片CF/volume抵消已经完成，不再计作本轮成果。

本轮严格检查三个此前未核的接口：

1. LPSW §9 slice tubes的essential distinctness需要什么原始几何和先验，能否由ambient CW直接继承；
2. 原真实line加移动horizontal2-grain后的slice是否仍为直线，任意dense marks删选或subpower line表能否修复；
3. 在完整source、κ≥ζ下，global clock-transverse flat3-plank是否可能有subpower-dense原Eδ shading。

第3项在明确具名WZ19.2下可排除；它否的是一类global flatflake桥，不证明不存在原配置。前两项有完全可审的几何/有限measure证明，范围在各处明列。

## 2. 新§9的两阶段没有免费slice CW

LPSW Props9.1–9.3先固定一个coarse flatflake方向，选其n−2个transverse slicing方向X_k；每个flatflake与thick3-slice的交是long straight tube。此处使用完整flat (n−2)-plane，不只是同点的tangent planes。

第二步先按这些tube的方向分组，再沿该方向投影到R^{n−1}，得到(n−3)-flakes。**在n=5，这些是R4中的2-plane flakes，非R4 ordinaryline tubes。** induction输入是新LPSW的低一ambient plane theorem，不可把OAI4 linear theorem当成同一个statement。

真正可继承的convex cap来自：若完整投影π(F)⊂K，则完整F⊂π^{-1}(K)∩B，且后者体积≤C|K|。仅有某一slice T_ω(F)⊂K3不推出完整F contained于相同volume的prism。原§9在投影侧uniformize fibre contribution，再用低维flake估计控制高multiplicity；只在后面按原shading挑essentially distinct的slice tubes。

因此必须保留indexed shading、原Σ|Y(F)|和投影fibre law；不能直接把ambient cap写给所有normalized slice priors。本节只是核原proof调用顺序，不自行重证整个LPSW。

## 3. All-convex ambient cap不控制每个slice：显式全片族

以下是完整flatflake族的转移反例，**不是actual WZ/Kakeya反例**。坐标写(x1,y1,x2,y2,t)。取小固定c0>0及r-grid a,b∈[−c0,c0]，#indices≈r^{-2}。令

    v_a=(1,a,0,0,0)/sqrt(1+a²)，
    w_b=(0,0,1,b,0)/sqrt(1+b²)。

F_ab是由orthonormal v_a,w_b,e_t生成的centered unit3-cube之r-neighborhood。所有F_ab在fixedball中，volume≈r²，取full shading；所有indices始终unit weights，不在切片时重设先验。

**对所有convex K有Σ_{F_ab⊂K}|F_ab|≤C|K|。** 证明：若contained参数集合为S，令A=osc_S a、B=osc_S b。任取F_a0b0，K−K含三个unit-order tangent向量v_a0,w_b0,e_t及r-ball。各F含共同x1=c、x2=0的inner-axis点(c,ca,0,0,0)，比较a两极点，K−K还含cA e_y1；同理含cB e_y2。中心对称convex K−K因而含一个volume至少c(A+r)(B+r)的5D crosspolytope，determinant中三个tangent向量的x1,x2,t minor为常数。Rogers–Shephard的|K−K|≤binom(10,5)|K|给

    |K|≥c(A+r)(B+r)。

grid packing则#S≤C(1+A/r)(1+B/r)。乘每片volume≈r²即得全convex cap。这个论证容许S任意相关，不假它是参数rectangle。

现在取central thick slice |x1|,|x2|≤c r，投影到(t,y1,y2)。所有F_ab的cut都含同一个c'r-tube并contained于同一个C r-tube，轴为t-axis。可给每cut保固定比例的共同inner tube作shading；所有indexed projected tubes便相同。故slice raw convex density≥c r^{-2}，取essentially distinct representatives会在该slice丢固定幂r²的indexed mass。

这个slice只承载总原shading的O(r²)部分：每片原volume≈r²，central cut的ambient volume≈r⁴。于是它**不反**LPSW允许global refinement后在大多数质量slice上变distinct的9.2。它严格否定的只是“ambient all-convex cap⇒每个slice同cap/可逐slice免费归一化”的更强转移。

若要包含所有这些F_ab，任何whole-convex preimage的volume都≥c，而central projectedtube volume≈r²；这个r^{-2}增大正是slice containment与whole projection containment的区别。不能把它藏到normalization。

## 4. 真原line加grain后，global flatness强制f恒定

对任意真实graph line p(t)=(p_x(t),p_y(t),t)，定义连续的ruled patch

    S_p={(p_x(t)+u,p_y(t)+f(t)u,t):t∈I,u∈U}，

其中U⊂R²有内点，I非退化。假这个整个patch contained于一个affine3-plane P。每时刻的horizontal2-plane

    H_t={(u,f(t)u,0):u∈R²}

都在dir(P)中；而不同t的p(t)差有非零time component，故dir(P)∩{time=0}恰为2维。于是所有H_t相同，投影到u坐标为identity，强迫f(t)恒定。

这个结论不需f可微，也不表示source的finite dense X有open interior。它只否定把完整移动2-grain ruled patch无条件当同一个flatflake的几何声明；若仅存original selected X，必须另作定量shading论证，不能援此精确等式跳过。

## 5. Straight slice的曲率障碍：任意dense marks与有限line表

固定smooth f(t)=diag(t,t²)、真实p(t)=(0,0,0,0,t)。slice固定horizontal x=(a,b)，得到R3中的真实曲线

    γ_ab(t)=(at,bt²,t)，|t|≤1。

f符合bounded dyadic-Lip；p确为原ruled patch内完整straightline。但本数据不满足完整source的positiveκ/slab/witness/tube-family要求，故不是主命题反例。

**Lemma。** |a|≤1、0<|b|≤1、0<e<1。对任意affine line L，

    Leb{t∈[-1,1]:dist(γ_ab(t),L)≤e}
       ≤C sqrt(e/|b|)。                              (1)

证明：投影到曲线所在2-plane，projection of L为line或point；point情形用任一过该点的line扩大事件。该平面的orthonormal坐标中曲线为(c t,b t²)，c=sqrt(1+a²)∈[1,sqrt2]。unit normal写(α,β)，near-line条件蕴含

    |α c t+β b t²−d_L|≤e。

若|β|≥1/8，leading quadratic coefficient≥|b|/8，配方后的quadratic sublevel长度≤C sqrt(e/|b|)，uniform于所有linear/constant coefficients。若|β|<1/8，则在|t|≤1的derivative绝对值≥sqrt(63/64)−1/4>1/2，长度≤Ce。两种情形的event均可由至多2个intervals覆盖，证明(1)。

若time probability ν在长度h的J上满足

    ν(I)≤K_t(|I|+d)/h                            (2)

对所有interval I成立（等价于base d以上的normalized1-Frostman cap，固定倍常数允许），则对任意N条affine lines及任意原相关selected event，union bound给

    ν{dist(γ_ab,∪_{j≤N}L_j)≤e}
      ≤C N K_t [sqrt(e/|b|)+d]/h。                (3)

特别，若该event保原time mass至少β，则

    N≥c β h/[K_t(sqrt(e/|b|)+d)]。                (4)

证明不需event独立、uniform time采样或选定长interval中的整段marks；任意measurable/dense删选都受同upper。finite Z的原uniform law只要#(Z∩J)≥h/(Kδ)，便直接由interval packing得到(2)，d=δ。不是把原time先验换成Lebesgue。

例如|b|≥b0固定、e≈ρ²、d≪ρ，h=ρ^{1-c}，若β/K_t仅subpower损失，则(4)迫N≥ρ^{-c+o(1)}。因此不能用subpower大小的straightline table覆盖该larger-time curved slice的dense marks。小于e的uniform perturbation只把e改固定倍，结论stable。

**尺度警告。** 若实际horizontal patch半径R=ρ，使|b|≈ρ，则(4)只给N≥cβ h sqrt(ρ/e)/K_t，e≈ρ²时门槛h≈ρ^{1/2}；不能据固定b例子宣称所有h≫ρ都失败。一般横向半径R、|b|≈R时，近直线尺度是sqrt(e/R)。R39的ρ-window、ρ-horizontal freeze误差Oρ²与本节unit transverse b例子是不同量词，必须分开。

## 6. 完整source下的global flatflake shading：独立核验

本节是A/root发现的来源级gate的独立推导；**条件于具名WZ2609.22035v1 Lemma19.2及原R22时间restriction闭包**。设κ≥ζ>0，γ固定，原η足小。F为a×b×1³的flatplank，δ≤a≤b≤1，long3-plane对time方向的projection长度≥固定c0>0。目标：存在ε0(ζ,γ,c0)>0，使

    |E_{Cδ}∩F|≤δ^{ε0}|F|                         (5)

对足晚δ成立（固定C只改变余量）。它限于global unit long axes和fineδ blur，不适用于任意localrescaling、clock-tangent plane或coarse E_e。

令V为long3-plane的horizontal2-plane。对exact source time z，设L_z(x,y)=y−f(z)x。clock-transversality保证F在z附近δ-time层的体积≤C(c0)abδ，并可用uniformly controlled的V-coordinates和两normal offsets积分。E_{Cδ}在该层最多涉及O_C(1)个δ-separated原times；在各exact z用L_z，不跨dyadic边界假设f的Euclidean Lip。

若||L_z|V||≥σ，取其maxsingular方向；固定另一V-coordinate和normal offsets后，image为长度≈λ1≥σ的line segment。原Y_z的Tube-Katz–Tao(1−γ)给其Cδ-neighborhood在此line上的长度≤Cδ^{-Cη}δ^γ λ1^{1−γ}，拉回parameter后长度≤Cδ^{-Cη}(δ/σ)^γ。积分其它参数得这些z的relative area同样≤Cδ^{-Cη}(δ/σ)^γ，independent于a,b。

假(5)失败且shading≥δ^ε|F|。取σ=c1δ^{1/4}；ε及η足小相对γ时，large-operator部分不足一半。每exact z的F-layer体积≤Cabδ，故有至少cδ^{ε−1}个原times满足||L_z|V||≤σ。

对这些times，projection x:V→R²有uniformly good inverse：若x(v)小，则y(v)=f(z)x(v)+O(σ|v|)也小，违反unit v。故固定V=graph G，||G||≤C，且|f(z)−G|≤Cσ。G由同一个V决定，**不随z或normal offset改变**。

取这些整时间层Z′，不删每层的Y_z/X/Φ/ξ，也不改T。#Z′≥cδ^{ε−1}而#Z≤Cδ^{-1}，所以原time loss至多δ^ε。R22闭包给同κ,γ的合法配置，新η′可取原η整数倍且η′=O(η+ε)：cross-time Y-union upper由原union继承，lower由保留的一个完整Y_z提供；不能给任意point subset重设lower。

令ρ=C0δ^{1/8}、σ_L=ρ²，C0固定足大，使任意z,z0∈Z′的|f(z)−f(z0)|≤σ_L。δ小则ρ≥δ^{1/3}且σ_L∈[ρ²,ρ]。原19.2要求对每z0及其ρ-window，有δ^{ε_L}比例times近f(z0)；这里**全部新times**都满足，取任意小ε_L即可。新allowed grid可按R22整数倍/rounding付δ^{-Cη′}，不将固定ρ幂藏进K。

具名19.2于是给

    C_CW(T)≥δ^{C(η′/γ+ε_L)}(ρ/σ_L)^κ
           ≥c δ^{C(η′/γ+ε_L)−κ/8}。

先ε≪γζ、ε_L≪ζ，后η≪ε，指数严格小于−η，反原C_CW(T)≤δ^{-η}。这证明(5)的某固定ε0可选。全过程原T未变，没有用新的slice或flake normalized先验代其CW。

该gate说明：若κ≥ζ的actualsource存在，则其原fine Eδ不能承载这类globalclock flatflake的subpower-dense shading。它严格阻断“找一族unit flatflakes且每片仍以inverse-subpower原密度落在Eδ内”的直接global桥；不排除合法coarser/adapted family、curved slices或其它机制，也不证明主branch不存在。

还不能据此排掉所有fixed-loss LPSW调用：若short axis a=δ^u而shading至多δ^c，则LPSW门槛a^{η_L}=δ^{uη_L}只有在uη_L<c时被此cap排除；uη_L≥c仍须另外核总质量/union/gain。不能因引用定理的η_L可以选得小，就断言任何较大的可用η_L均已无效。原main仍未解。

## 7. 停止结论

本轮没有证明完整κ≤ζ，也没有保全source的反例。新信息是：slice cap不能逐slice免费赋值的完整all-convex family；移动grain切片的curved/time-density障碍；以及在具名19.2下真实source的global fine flatplank shading排除。后者与R39平行片toy不同，但它是**负接口结果**，不是full sticky branch解法。

原LPSW §9的projective codim2 geometry、完整flatflakes的whole convex preimages及低维plane induction，都没有从actual moving2-grains自动得到。若其余尝试只能回到local CF/volume抵消、给curved slice换名直线或越过(5)强行保global denseflake，则按R40 spec冻结该局部连接并macro换路；不续数字carry/CP/PM同义计数。

正式review须待实际读root与A全稿后另归档。本稿证明范围如上，未经外部同行评审，不改变Goal/major/novelty状态。
