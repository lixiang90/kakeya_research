# R0106：moving-row准入失败与两锚模型的原质量诊断

2026-10-19，root，working5锁后检验。完整source moving-row cap未证；已锁的two-anchor反攻亦未满足其native Y tubeKT假设，不能记成功反例。本稿保存具体失败及辅助精确几何，非fullDef17/Kakeya反例，无newID/major/ordinary增益，未经外部同行评审。

## 1. 完整目标、原假设与本轮判定

继续一般n≥5/ordinary Hausdorff、真同集全方向strict反例或重大中间结果。实际恢复R105同SHA fb96580d/tree9b171bff、1672旧clean及所有当前入口；前轮原I粗line为progress。四完整出口重新比较，DIM已付内部应用不重开assembly，旧HRZ/CP/PM等冻结保原范围。

候选来自完整WZ Def17 matrix33 d5/k=ell3/κ1、原Y AD1/tubeKT(1−γ)、filledX2、pointΦ AD1/slabγ、ξ-coherence、原jointT4AD/CW及R102 det-large anchors。真正想付的是所有unit n、δd0≤z≤1的far原time cap νZ{|nᵀGu|≤z}≤L^M z^τ。它不是R104/105 two-plane cap；本轮没有证明或反驳这个完整命题。

working5另锁一个强前缀反攻，包含两个anchors的nativeY tubeKT。下面抛物线模型不满足它，故按停止条件拒绝；不得静默删YKT后称已解已锁任务。辅助Jac、CW与bulk预算只用于解释失败发生在哪里，不替换总目标或冒新源gain。

## 2. 单row真正的physical/global场关系

固定normalized affine chart，t=0,s=1,F0=I,F1=0。原线写(x(u),v(u),u)=(a+uφ,b+uψ,u)，两端code为

    C(T)=(U,V)=(b,b−a+ψ−φ).

若U2−V2=c，则a2−ψ2+φ2=c。对所有同一条线上的u都有

    ψ2=x2(u)−c+(1−u)φ2.

取F_u=diag(f(u),1−u)，则selected第二normal场可真正全局设ξ2(p)=x2−c，而非每点自由选择Γ。它对x是线性的，dyadic-coherence成立；沿同T，ξ2(p_v)+(1−v)φ2恒定。相应n=(e2,−e2)满足nᵀGu=0。

这实际否定了“filledX与coherence单独就不容该row”的预期。它没有同时构造原bulk第一场ξ1、完整Y/Φ、全T/CW，故不反完整source。将contact或单row换名，不产生正gain。

## 3. Same-T两time公式与窄片的未付费用

记native label Y(u)=v(u)−F_u x(u)，h=v−u，k_uv=(f(v)−f(u))/h。对同一条T精确有

    Y1(v)=Y1(u)+h[ξ1(p_u)−k_uv x1(u)]−h²k_uv φ1,
    Y2(v)=Y2(u)+h[2x2(u)−c]+h²φ2.              (1)

固定x2宽w的strip只将第二输出压到O(|h|w+h²)。要得h²横条须w≲|h|；单片通常仅保w原质量，同strip双point pool的通用CS lower亦损w。原同T double counting可取共同(u,v)，不授每原filledX点或每原角都访问同一v。按片重源有ρ^C费用，不能藏原K或假ξ≪θµ。

更根本地，tubeKT只上界横条内不同outputs，不直接给x1↦ξ1−k_uvx1的lower image count；长x1可分多个近常块，甚至ξ1=k_uvx1在单pair精确取消。原19.4之所以可用，是wholeF慢变后粗ξ_q固定，varying clocks产生真实直tube；这里rough k_uv项不能删除。需要共同图/全部large subsets的projection强度和全部strip原质量容量求和，本轮均未支付。由此拒“19.4直接给row cap”。

## 4. 辅助两锚构造及精确参数

下列是失败诊断，不是满足working全部假设的反例。取R=1/4，

    U=(q,w), V=(v,w), v=sqrt(R²−q²−2w²)>0,
    Y0(r)=(r,r²), Y1(s)=(s,s²),
    a=U−Y0(r), b=U,
    φ=Y0(r)+Y1(s)−U−V, ψ=Y1(s)−U.             (2)

参数(q,w,r,s)在(q0,w0,r0,s0)=(1/8,0,0,1/16)的固定小product box。U、V投影局部双Lip，detD(V1,V2)/D(q,w)=−1/sqrt3≠0。实际C(T)恰(U,V)，因此所有code在H3={U2=V2}的spherepatch内。整体一次固定homothety将两normalized anchors放在真实Euclidean单位轴内部；这是固定常数坐标改变，不把u-span1误称Euclidean弧长1，所有δ/计数只改常数。

固定小box后取Cδ间距的四参数格。由(2)得到的是同一族真实straight单位管，非每point另造线；N≈δ^-4。下面连续Jac只认证这个smooth模型自身，不能在改换fractal nativeY后沿用。

## 5. 条件代数、joint4AD与wholeCW确能付

对方向graph θ=(φ1,φ2,ψ1,ψ2)，在参数点r=w=0处，四列按(q,w,r,s)的矩阵为

    (−1−v_q,  0, 1,  1)
    (      0, −2, 0, 2s)
    (     −1,  0, 0,  1)
    (      0, −1, 0, 2s).

det=−2s=−1/8。固定小box使方向map全局biLip（在convex box上导数与固定可逆矩阵的差取足小），故parameter格给δ-separated actual directions及joint4AD管族。方向norm归一和固定homothety均为有界chart改变。

whole convex Wolff可直接按John box计：含一根unit δ-tube的bounded convex W，其长轴≥c、各短轴≥cδ；允许方向的球面盒体积≤C|W|，δ-separated方向数≤C|W|δ^-4≈C|W|N。小于tube厚度的box不能包含该tube。原CWA只需classical方向计数，不是把phase code3plane当physical plank。

这些是辅助模型的真几何；单独成立不消除§7的fatal假设失败。尤其不能从“方向Jac可逆”声原完整Y tubeKT也成立。

## 6. 两端filledX、pointΦ及ξ能真实同时实现

u=0时physical p0=(U−Y0,U,0)，native label为Y0，固定r而U遍历patch给filledX2。对应所有s的真实同族管方向形成

    Φ_(p0)=Y0−U−V+Y1(s),  ξ_(p0)=V−Y0.

u=1时p1=(Y1−V,Y1,1)，native label为Y1；固定s而V遍历同patch给filledX2，对应所有r有

    Φ_(p1)=Y0(r)+Y1−U−V,  ξ_(p1)=Y1−U.

U↔V双Lip使两端ξ在physical数据上统一Lip，而非自由Γ。四参数product格在每端形成真实δ-separated点及≈δ^-1条point pencil，不需把方向网和独立point网免费互换。两端Φ是parabola平移，AD1且slab1/2，故满足其声明的γ≤1/2角输入。因为U2=V2，两个ξ的第二分量恰是其physical x2，同T全clock的§2关系保留。

native Y0/Y1本身AD1，却不是下一节所需tubeKT；AD/slab与tubeKT是不同量词。此处不得将pointΦ的成功转授给nativeY。

## 7. 已锁任务的fatal：parabola nativeY不满足tubeKT

取固定parabola arc内部r*，在其tangent方向放宽Cδ、长c sqrtδ的tube。Taylor二阶余项保证|r−r*|≤c′sqrtδ的curve落管内，uniform δ-net有≥cδ^-1/2个不同δ-cells。原tubeKT(1−γ,δ^-η)只允许

    Cδ^-η (sqrtδ/δ)^(1−γ)
       =Cδ^(-η−(1−γ)/2),                         (3)

与前述lower在η<γ/2、δ小冲突。按原有限Cη费用，只须源η相对γ足小。

不能只换格相位或稀疏nearfull采样修复：固定arc可用O(δ^-1/2)条上述tangent tubes覆盖。任意仍有≥δ^(η−1)个点的子网，至少一管含≥cδ^(η−1/2)点；与(3)合并迫η≥γ/4（一般Cη常数作对应调整）。因此保持原small-loss native AD1计数的稀疏删选也救不了。

换成product Cantor dust可能付YKT，但将改变smooth四参数域和方向推前；不能沿用§5的Jac/δ方向分离或§8 bulk计数而声成功。依working§5，当前countergate到此强制停止，不降低hyp保留一个新弱成果。

## 8. 模型的bulk失败可按原访问分母定量看清

这只诊断(2)这个smooth family。取包含原Z的固定有界normalized clock区间，前述homothety可使该区间位于unit轴内部。对τ≠0,1，pointmap Pτ=(a+τφ,b+τψ)。其Jac在参数点为

    detDPτ=−2s τ²(1−τ)²,
    detDP_(1/2)=−1/128.                          (4)

更一般，detDPτ=τ²(1−τ)²D(q,w,r,s)，D独立τ且在固定patch上|D|≥c：把outputs改为Yphysical/(1−τ)=U+[τ/(1−τ)]Y1及(Yphysical−Xphysical)/τ=V+[(1−τ)/τ]Y0；r列只在后一block、s列只在前一block，两个系数乘积1。

每fiber引入v变量后由sphere二次式与四个degree≤2 output方程给出。非零Jac使所有相关解为isolated nonsingular complex roots；经典Bézout（或小扰动后Bézout再用局部逆保持这些解）给统一有限fiber数≤32。area formula遂给δ-ball的parameter preimage体积≤C[τ(1−τ)]^-2δ4。parameter格周围不交δ-cubes及Pτ统一Lip使每physicalδ-point最多C[τ(1−τ)]^-2条本族管。

所以任意κ1型层|Eτ|≤Kδ^-3只能承载≤CK|τ(1−τ)|^-2δN访问。对far |τ|、|1−τ|≥r*，保守用r*^-4。任意δ-separated Z、m≥δ^(η−1)，两锚距离r*=δ^c的near时钟至多C(r*/δ+1)。故任意试图在本族上选κ1层marks的平均密度有upper

    I/(Nm)≤C[δ^(c−η)+δ^(1−4c−Cη)].              (5)

固定0<c<1/4后η足小，右边固定正幂，不能达到完整source的δ^Oη nearfull密度。此处真的使用原T/N、每T每clock至多一次及全部bulk层容量，不仅说某个slice维数大。它不是任意fullsource的上界，只说明本smooth model在删除bad bulk访问后仍不能被补成完整κ1证据。

## 9. 文献、闭包与旧指纹

fresh搜索的Choudhuri2610.12480、PZ2411.13395、horizontal/SL2输入均已库旧用途；没有采用新高级工具。A对CC-geodesic2607.26906v3只作primary声明筛查，度量、方向和曲线类型不同，不下PDF作主输入。R59、R69、R72、R76、R80及R105各自作用保持，不将source书目重复当新信息或新major。

对全部原time restriction可按R22付密度参数，但§3单strip只保ρ^C并不能授NF所需small loss；对whole-index tube删选可保旧ST，但会丢完整point Φ/filledX。two-anchor marks总访问仅2N，本来不是nearfull Nm。§8即便允许任意bulk层重新选marks也给本模型实际容量不足；不能由此反完整source或将rowcap命题声已证。未证明本候选与旧CP/PM全称gain双向等价，也不能以尚未等价为自动准入。

## 10. 终判、审查与宏观停止

当前fullsource moving-row cap仍open；19.4不能直接给，窄片求和/common-v/robust投影费用未付。已锁two-anchor/YKT反攻失败，parabola在原所有尺度tubeKT条件上严格不合法。辅助geometry只将两端/wholeT-CW与bulk失败分清，不记成功的前缀反例，不登新数学ID或reviewed源定理。

本轮按无qualified源gain、actual no-information1及legacy无完整branchsaving29归档；严格拒选证据改变下一行动，但不冒高维数学收益。两份独立正式审查只应认证以上失败判断和限定计算，非外peer/源wholeproof认证。停止更多fixedtime、parabola/Cantor换网、χ/q/ρ或micro参数；下一先完整四出口宏观重选，须真正新的bulk原质量或不同输入才可施工。Goal active。
