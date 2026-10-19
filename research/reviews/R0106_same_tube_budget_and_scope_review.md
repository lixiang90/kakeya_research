# R0106 正式独审：same-T预算、native tubeKT失败与拒选范围

2026-10-19，B。仅编辑本授权formal，恰六个编号节；不改已冻结B稿或其他文件、metadata/Git，不下载、不spawn。本次独审root/A，不以本人自证代独审；未经外部同行评审。

## 1. 实际全文读域与明确判定

已fresh实际全文读root主稿`notes/40_multiscale/sticky_matrix/R0106_moving_row_gate_and_two_anchor_failure_diagnosis.md`十节、A终稿`notes/00_map/R0106_full_goal_source_and_route_reselection.md`十节、R106 working五节及reselection五节；本人B资格十节已保存并冻结。root最新§8已覆盖包含原Z的固定bounded clocks、τ≠0,1，far为同时距两锚≥r，而非只估(0,1)内部。这一修订已全文读回。

本轮实际全文读GOAL/STATE/ROADMAP、registry全部78项状态、R105 next六节与两formal各六节；原R105主十节沿刚完成的同会话fresh审查记录复用。又全文读R102 root十二节、R72 root十节、R80 B七节、R98 B十二节，回读R75原有限微分门及本地WZ Def17.1–17.4/Remark17.1、19.5相关源段。没有重新核官方byte/Git，也不声WZ高级wholeproof全部独证。

判定是：**拒选判断及下列限定计算通过；所锁two-anchor反攻构造不通过working全部假设。** 关键失败是两端parabola native Y不满足原全尺度tube Katz–Tao。当前root/A已明确撤回成功前缀反例、源gain或fullsource counter的说法，没有尚待修正的成功声明。完整moving-row时间cap仍未证未否，不能把本formal的通过解释为该cap或其反例获证。

## 2. Exact row、两项native响应与未付正面质量

核root§§2–3/A§7：在参考anchors0、1、F0=I/F1=0时，真实axis为(a+uφ,b+uψ,u)，code C=(b,b−a+ψ−φ)。U2−V2=c等价a2−ψ2+φ2=c。取F_u=diag(f(u),1−u)，便有对同一whole line的精确场

    ξ2(p_u)=x2(u)−c,
    ψ2=ξ2(p_u)+(1−u)φ2.

这是真正全局线性/coherent的第二response，不是逐point或逐访问自由Γ；对应n=(e2,−e2)作固定unit正规化即可使nᵀG_u=0。它只反“filled X和coherence本身已足排row”的免费步骤，没有构造全部原Y/Φ/ξ1/T/CW。

设h=v−u、k_uv=(f(v)−f(u))/h。由同一个selected tube的两次实际访问直接展开，确得

    Y1(v)=Y1(u)+h[ξ1(p_u)−k_uvx1(u)]−h²k_uvφ1,
    Y2(v)=Y2(u)+h[2x2(u)−c]+h²φ2.

符号及原x项均正确。要把第二输出放在h²横条需x2-width≤O(|h|)。选一条strip通常损其宽度的原质量，同strip双点CS的通用账也保留此费用；不因此断言所有更强原几何都只能如此。tubeKT给不同outputs的upper，不给响应图的lower；ξ1=k_uvx1可对单pair完全取消。共同(u,v)的总tuple不授每filled点或每角共享v，不能把rough第一row删除后套19.4的wholeF慢变。

因此root/A正确保留了正面cap的未付项：共同图/large-subset投影强度、strip求和及原I分母。没有以可微Y、共享fine angles或Rademacher替换finite源，也没有将row cap附为新成功公设。

## 3. 双锚same-T代数、Jac及wholeCW的限定成立项

核root§§4–6：U=(q,w)、V=(v,w)，v=sqrt(1/16−q²−2w²)>0；参数点(q,w,r,s)=(1/8,0,0,1/16)。V对U的Jac为−1/sqrt3，固定小patch中U↔V双Lip。令Y0=(r,r²)、Y1=(s,s²)，a=U−Y0、b=U、φ=Y0+Y1−U−V、ψ=Y1−U，则真正两端为(U−Y0,U)和(Y1−V,Y1)，intrinsic code精确为(U,V)。左ξ=V−Y0、右ξ=Y1−U给同一tube的normal slope，并非分别指定两套不相容端点。

在所选点方向graph θ=(φ1,φ2,ψ1,ψ2)的四参数Jac为−2s=−1/8。固定convex小box使导数接近同一可逆矩阵，故方向map有统一双Lip；选足够固定倍δ的product格可给δ方向分离与joint4AD。一次固定homothety把参考clock跨度放进真正unit axis内部，随后延伸同一轴为单位段；不把graph clock1冒作Euclidean弧长1。所有相关尺度只改固定常数。

wholeCW也能为这个辅助family独立支付：John ellipsoid的各轴≥cδ，若含unit tube则至少一轴≥c。按一个非短方向坐标分chart，方向δ帽数≤Cδ^-4乘其余半轴的截断乘积，≤C Vol(W)δ^-4≈C Vol(W)N。族在固定球内，任意凸query可与该球相交后作有界query，故无需免费增添bounded query假设。这里用真实全方向分离，不是仅由jointAD或phase code3plane授CW。

两端filled X分别来自U和V开patch，point Φ为另一端parabola的平移，selected ξ在physical端点数据上Lipschitz，AD1/slab1/2的角输入可以成立。这些是指定smooth family的真实限定性质；它们并不检查下一节的native Y tubeKT，也不保nearfull全Z。

## 4. Native Y的mandatory失败与不可用删网修复

这是working失败的决定性检查。原Def17.3 tubeKT要求每δ≤ρ≤τ≤1及任意宽ρ长τ的tube，有N_ρ(Y∩tube)≤δ^-η(τ/ρ)^(1−γ)，不是仅全局slab upper。

对任一固定内部parabola点r*，法向tangent误差为(r−r*)²/sqrt(1+4r*²)。取query宽Cδ、长c sqrtδ，整段|r−r*|≤c′sqrtδ在管内，uniform δ参数网给≥cδ^-1/2个不同Cδ-cells。但原upper仅为

    Cδ^-η(sqrtδ/δ)^(1−γ)
      =Cδ^(-η−(1−γ)/2).

比值≥cδ^(-γ/2+η)，η在固定γ之后足小时发散；K=δ^-Cη的有限费用同样失败。无论γ≤1/2还是更小的任意固定正值，这个检验都有效。point Φ可有全局slab1/2，不意味着native Y满足所有细长tube的Katz–Tao条件。

root/A进一步排掉同一smooth arc的近满稀疏修复也正确：O(δ^-1/2)条此类切管覆盖固定弧，任意保留≥δ^(η−1)点的子网必有一管含≥cδ^(η−1/2)点；与上式比较迫η≥γ/4。当KT常数是δ^-Cη时相应阈值为γ/[2(C+1)]量级，仍与源η可先于δ足小冲突。

所以候选确未满足锁定两端Y tubeKT。不能静默删除该hyp，不能把成功的direction Jac或point Φ slab转授给Y，也不能更换rough dust后沿用smooth Jac/有限格/CW/访问结果。当前root/A已按working停止，不以弱化反攻补成成功成果；这个拒选结论通过。

## 5. 指定family的bulk原访问诊断

独核root§8。令P_τ=(a+τφ,b+τψ)，对所有固定bounded实τ≠0,1，有

    det DP_τ=τ²(1−τ)²D(q,w,r,s),
    D=2r(v_q+2s v_w)−2s.

可由输出(x−z,z)消元直接得到；D不依τ，固定patch使|D|≥c。参数点τ=1/2时Jac=−1/128。底层continuous族的联合五维map因而局部可逆、union有open五维部分；有限δ网axes本身零体积，round δtubes的uniform体积lower则另由每τ的四维packing及积分支付，二者未混同。

为诊断任意δ-point容纳多少本族tube，引入v独立变量，四output方程加sphere方程共五个degree≤2方程。patch内v≥c、DP_τ非零使每个相关解是regular isolated complex root，经典isolated Bézout上界≤32可用；没有假全零集均为0维。area formula给output Oδ-ball的参数preimage体积≤C|τ(1−τ)|^-2δ⁴。原参数格的disjoint δ-cubes经统一Lip pointmap仍落扩大Oδ-ball，故每physical δ-point附近最多C|τ(1−τ)|^-2条本族管。

于是任意试图承载这些marks的κ1型层|E_τ|≤Kδ^-3，原访问数至多CKδ |τ(1−τ)|^-2N。far同时距两锚≥r*=δ^c可保守用CKδr*^-4N，适用于包含原Z的全部bounded clocks，不只(0,1)。near clocks每管至多C(r*/δ+1)，除以m≥δ^(η−1)后，平均density≤C[δ^(c−η)+δ^(1−4c−Cη)]。先0<c<1/4、再η足小，这是固定正幂，达不到完整源δ^Oη nearfull密度。

此处保的是指定family的原N、真实tube/time计数，甚至允许任意bulk层重新选marks；说明它不能在原质量级补成κ1证据。不是任意fullsource的上界，也不否增加不同管后的完成。该诊断不修复上一节fatal假设，不能拿来改称反例达标。

## 6. 最终审查范围、闭包与停止

root十节、A十节及working五节在本formal所列计算和失败判断上通过，无遗留的错误成功声明需要修正；本人B十节的推导不自计独审。明确判定仍是**所锁构造失败，完整moving-row cap open**，没有成功的两锚source前缀反例、源gain或新的高维界。

原平均I、逐管S_T、每point Φ/filled X及每time大子集分别核：whole-index选管可保旧S_T而不保完整point条件，normalized CW付N/N′；完整time restriction按R22计真实密度/newallowed，不能把单strip的ρ幂当小η。两端仅2N visits本来不足nearfull Nm；bulk诊断按原N进一步量化失败。没有从相关g粗拒合法闭包，也没有证明旧CP/PM双向gain的一个新等价版本。

本次只同意拒选与限定计算，不认证完整Def17/Kakeya不可能，不续更多fixedtime、parabola/dust换网或row参数。ordinary/HRZ、既有DIM具名应用、全部rough/mixed及真同集strict反例四完整路线仍按原目标保留。无newID、major或Goal完成，Goal active。

高级source wholeproof未重新认证，所引Bézout等亦按既有经典输入使用；未经外部同行评审。未预认证未来macro/next、metadata、Git或同步。只新增本六节formal，完成后停止编辑检索。
