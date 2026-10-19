# R0106：锁定输入、原质量诊断与拒选边界独立审查

2026-10-19，A。以下正式判定为“拒选判断通过”，不称锁定构造通过。仅审已写出的失败及条件诊断；未经外部同行评审。

## 1. 实际全文读域、锁定输入和独立责任

实际全文读取root《R0106_moving_row_gate_and_two_anchor_failure_diagnosis》10节、B《R0106_original_point_tube_global_coupling_counteraudit》终10节、working_spec5及冻结A《R0106_full_goal_source_and_route_reselection》10节。B第一次工具输出尾部被截断，随后整篇单独重读，未以截断片段记全文。原WZ Def17.1–17.4、Remark17.1、Prop17.2 statement和19.4完整proof/19.5开头沿本轮实际回读记录；未声重证WZ、R77等高级wholeproof，亦未新核官方bytes。

working§2明确要求native Y在两个anchors均满足AD1及全尺度tubeKT(1−γ)，同时要求同一原T、joint4AD/wholeCW、filled X2、point Φ AD1/slabγ、selected ξ/coherence与same-T transport。这些输入必须同时成立。parabola native标签没有满足tubeKT，因此“有真实CW和真实端点pencils”不等于完成working。root/B均已撤回成功countergate说法，本formal核这一撤回是否必要、其余条件计算是否有越界。

本人的A稿施工不算自己的独审。本次独立逐式对象是root/B的几何、finite计数及失败结论；不把B自推或root审过本人主文当作本人完成的独立验证。未读取的未来macro/next/metadata状态不预认证。

## 2. Exact row场、same-T公式与未付正面预算

root§§2–3和B§§2–5的原坐标一致。参考anchors0/1、F0=I、F1=0时，直线参数给C(T)=(b,b−a+ψ−φ)。U2−V2=c即a2−ψ2+φ2=c；故每个该T上的真实点均满足ψ2=x2(u)−c+(1−u)φ2。令ξ2(p)=x2−c是一个真point场，coherent且与整条同T transport相容，不是每次访问另选Γ。

对F_u=diag(f(u),1−u)，h=v−u、k_uv=(f(v)−f(u))/h，原native响应恰为

    Y1(v)=Y1(u)+h[ξ1(p_u)−k_uv x1(u)]−h²k_uvφ1,
    Y2(v)=Y2(u)+h[2x2(u)−c]+h²φ2.

第二式正号和二次项均核对。固定宽w的x2片只给O(|h|w+h²)带宽；欲得h²须w≲|h|。单片及同片双点的通用保量具有w费用，不能藏进原δ^Oη；若直接重源，其固定尺度指数不满足NF所需小比率。所有strip与输出容量合计可能另有机制，但本轮未付，不能由此断言完整rowcap为假。

tubeKT只给该横带内不同输出的upper。长x1不强迫ξ1−k_uvx1有长像，单pair取ξ1=k_uvx1即可取消；这只是对错误lower推理的检测，不是完整source反例。原同T平方计数能生成共同visits平均，不能把每个filled点/完整Φ都赠给一个固定v。19.4依赖whole slope慢变、粗ξ代表及varying clocks的真实tube构造，不能删除rough Δf项后直接调用。因此完整moving-row cap在本轮仍未证未否，不能用R104/105 two-plane cap替代。

## 3. 两锚smooth模型的条件几何和真实离散pencils

root§§4–6/B§6的参数为U=(q,w)、V=(v,w)，v²+q²+2w²=1/16且取正根；y0=(r,r²)、y1=(s,s²)。真实轴参数a=U−y0、b=U、φ=y0+y1−U−V、ψ=y1−U给两端physical点(U−y0,U,0)、(y1−V,y1,1)，native标签分别y0、y1，selected ξ分别V−y0、y1−U。两端同一管、C(T)=(U,V)、第二row ξ2=x2均为精确关系。

在(q,w,r,s)=(1/8,0,0,1/16)，U↔V的Jac为−1/√3；raw方向四维Jac为−2s=−1/8。固定足小product box后方向map的导数与固定可逆矩阵接近，遂全box双Lip。真实Cδ参数格给N≈δ^-4、δ方向分离及joint4AD。wholeCW由方向计数而非jointAD单独推出：可先以共同bounded ambient截凸查询，John轴长有一项≥c，其余厚度≥cδ；允许方向的δ帽数≤Cδ^-4乘相应短轴积，≤CN|W|。小于管厚的查询不能含whole管。

真实δ-heavy端点需另付，不能仅引用连续Jac。这里product格使p0由(U,r)唯一确定、p1由(V,s)唯一确定，两映射均在固定patch双Lip；固定p0时s的整格、固定p1时r的整格分别给≈δ^-1条同族管。足够疏的固定Cδ网及有界chart/rounding只改固定重数。Φ是translated parabola，故AD1/slab1/2；ξ随physical端点统一Lip。两个anchors可经一次固定同尺度坐标调整放入真正Euclidean unit轴内部，未把clock跨度1误认弧长1。

上述核算只认证这些条件式。它没有认证native Y tubeKT，亦不在更换为fractal标签后继续有效；两个clock的访问只给O(N)，不是原nearfull Nm。它不能被单独登记为已达到working全部输入的前缀反例。

## 4. Native tubeKT的fatal及任意nearfull子网

root§7和B§7的拒选理由成立。取固定parabola arc内部点，固定c足小后，参数长c√δ的一段落在宽δ、长C c√δ的tangent tube内。真实δ网命中≥cδ^-1/2个δ-cells，而原tubeKT(1−γ,δ^-η)最多允许

    Cδ^-η(√δ/δ)^(1−γ)
       =Cδ^[-η−(1−γ)/2].

对任何固定γ>0，η在γ之后足小、δ趋0便矛盾。若用一般δ^-C0η常数，同理要求C0η不能小于γ/2。原定理允许ρ=δ、τ≈√δ这一查询；固定宽度常数也可扩大ρ而只损固定倍。这里比较的是真实finite covering数，不是只说连续光滑曲线有tangent。

改格相位或删为nearfull子集不能修复。固定arc由O(δ^-1/2)个上述tangent tubes覆盖，≥δ^(η−1)个δ-separated native点迫某一管含≥cδ^(η−1/2)点。与同一KT upper比较，C0=1时迫η≥γ/4；一般为(C0+1)η≥γ/2。故原small-loss参数顺序排除这种修复，不必额外假每一点都有ADlower。

AD1与全局slab1/2不等于tubeKT1−γ，Φ的成功不能转授给Y。换真正KT dust会改变smooth原参数域、方向推前及bulk slice计数，不能沿用旧Jac追认；这也不证明所有rough构造不可能。依working停止条款，不能删YKT、少一端或另换网救成弱toy。失败的是所锁构造，不是完整source。

## 5. Bulk coarea/Bézout及原N/I容量独核

root§8与B§8的辅助诊断可独立成立。固定bulk clockτ，Pτ=(a+τφ,b+τψ)。对τ≠0,1，把输出改为

    (Zphysical/(1−τ),(Zphysical−Xphysical)/τ)
      =(U+[τ/(1−τ)]y1,
        V+[(1−τ)/τ]y0).

r列只入后一block、s列只入前一block，两个系数乘积1；回原输出的Jac因子为τ²(1−τ)²。固定patch上的其余因子D与τ无关、在基点−2s=−1/8，故|det DPτ|≥c|τ(1−τ)|²，τ=1/2时精确−1/128。此是所有实际patch参数的统一lower，不是只在一个点非零后外推全部参数。

引入v为第五变量，sphere式及四个output方程均degree≤2。patch中v≥c，扩展Jac与v det DPτ成非零倍，故所计解均是regular isolated complex roots；经典isolated Bézout给数量≤2^5=32，即使patch外有正维分支也不增加这些regular根的数。这里使用经典定理，不声本轮重新独证其wholeproof。

area formula于是给output Oδ-ball的parameter preimage体积≤C|τ(1−τ)|^-2δ⁴。每个原格点配不交参数δ-cube；pointmap在略大固定patch的统一Lip将这些cubes送入扩大Oδ-ball。因此每physicalδ-point所遇本族管≤C|τ(1−τ)|^-2。roundtube端帽及同clock恢复只改固定倍，不把连续axes并的正体积错误转授给有限axes并。

任意试图选出的κ1层|Eτ|≤Kδ^-3只能承载≤CK|τ(1−τ)|^-2δN次访问，N≈δ^-4仍是原全族分母。far距锚≥r*给保守Kr*^-4δ；near锚clocks至多C(r*/δ+1)，原m≥δ^(η−1)。取r*=δ^c、0<c<1/4且η随后小，遂

    I/(Nm)≤C[δ^(c−η)+δ^(1−4c−Cη)].

这是固定正幂，不能支撑本模型的原δ^Oη nearfull平均，逐管版本更不可能。它只诊断这一个smooth family，即便重新任意选择bulk层也容量不足；不排增添不同管的完成，不反任意完整source，也不修复前节已经fatal的两端YKT。

## 6. 最终判定和停止边界

**拒选判断通过，无未解决强制修正项。** 审查通过的是：exact row/transport及其正面用途尚缺什么；parabola native tubeKT的严格冲突与nearfull子网反攻；作为条件诊断的两端Jac/CW/pencils及bulk原I上界。不是“locked构造通过”，不是成功的完整前缀countergate，更不是完整rowcap或fullDef17反例。

fullsource moving-row cap仍open，四个完整Goal出口仍未完成；不以源gain、ordinary下界、reviewed源定理、新ID或major归档这些失败。平均、逐管、每point/每time及条件pair量词未混用。停止本fixedtime/parabola/Cantor换网模板，不以χ/q/ρ或粗糙标签参数继续；后继须完整路线重选或真bulk原质量输入。

本formal不认证未来metadata/Git/同步，未编辑冻结A稿或其他文件。高级具名输入、本次实际逐步审查与外部同行审查分层；未经外部同行评审，Goal active。
