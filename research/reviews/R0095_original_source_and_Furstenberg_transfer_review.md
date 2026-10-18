# R0095正式审查：原source、实际Furstenberg转移与直化范围

2026-10-19，A。结论为下列有限范围全文通过，无未解决强制项；完整mixed42未证未否，未经外部同行评审。

## 1. 实际全文对象、原量词与独审分工

本审实际fresh全文读取当前root主稿`R0095_planar_Furstenberg_transfer_and_straightening_boundary.md`10节（包括§4最后补入的constant-β dualRW旧出口）、A原稿`R0095_actual_Furstenberg_input_audit.md`10节、B稿`R0095_complete_route_and_Furstenberg_counteraudit.md`8节、reselection/working两spec各5节，以及终macro、next和source note各6节。没有将读过旧版替代本次最终全文。以下独审以root/B的论证及整合为对象；A本人参与原source与constant-normal证明，不能把自己的主稿再算一份独立审查。A这部分已由root/B实际全文逐式核对。

保留完整bounded WZ Def17.2–17.4 d5/k4/ell2、固定0<κ<1及γ>0、η最后小、原全T/N/joint4AD/normalized whole-CW、两grains、原Z和point-Φ/ξ/coherence。K只含有限源损失δ^-Cη。实际原读域包括Def17.2–17.4及Remark17.1、19.4声明、19.5声明及相关证明输入、§22.1同管V式(174)–(176)；不声称全文独证WZ。RW实际采用已有v3的定义及Th4.1，R77已用过该源；本轮官方history检查记录为2025-01-19 v3，不是新文献发现，也没有本轮新增官方三核心wholebytes检查。

## 2. 实际共同平面、nice配置与已饱和的RW指数

root§2/B§3从第一套ℓ2 global grain的scalar filled轴取π=(t,x₁)。每time一个实际grain已给K^-1δ^-1个横排点，合原Z得到#P≥K^-Cδ^-2；二维ambient packing除该真实card使UniformP(B_r)≤K^Cr²。这里的维2是合法Frostman upper，没有借用删选后AD lower。每个projected point只选一个实际preimage，其原scalar Φ参数就是projected slope。固定倍δ尺度、有限邻格/着色与共同M≈K^-Cδ^-κ保真实相交及κ-Frostman pencil；不合并不同preimages的条件角law。

RW Th4.1的准确lower是δ^{-min{t_P,(s+t_P)/2,1}+ε}M。代(t_P,s)=(2,κ)得到δ^-1+ε M；固定一个原time横排已有≥K^-Cδ^-1M个不同line cells，因为每条有界斜率的δ管在该横排只遇O(1)个分离点。后者已不弱于RW主幂，而bounded slope/intercept空间仍允许O(δ^-2)条，κ<1时不矛盾。原native scalar Y_t的small upper在π中未保留，不能赋给该line union。单preimage的nice见证不冒保原全部incidence权或重新构成完整Def17。root/B的正面输入与无saving判定均通过。

## 3. 原CW推前、真实bush及constant-normal旧出口

对固定bounded n=(-β,1)，同q=(n·a,n·b)半径r格的whole原管满足一个随clock倾斜的物理超平面Cr slab条件。bounded原chart、r≥δ及||n||≥1给真实凸体积≤Cr，round caps付固定倍r，故以原N为分母得μ(q∈B_r)≤CKr。两个系数约束不是两个独立物理短轴，不能直接写r²。

root§5/B§4的bush用b∈(3δZ)^4小盒、a=0及真实单位轴(tb,t)，公共clock区间[1/4,1/2]存在。该处horizontal δ/10 disks分离且在原round tubes内；积分对任意whole-contained子族给|U|≥cδ⁴#T[U]，验证joint4AD及原normalized CW。q=(0,b₄)在内部球的质量≈r，严格反免费q2-Frostman。它有固定正五维union体积且缺完整Φ/双grain小label，绝非完整source或低维Kakeya反例。

缺q2不妨碍β恒定的旧出口：heavy原管保各自nearfull原clock；按q格的原multiplicity分层，选保K^-C质量的一层并每格取一根heavy代表，使uniform q-points为1-Frostman。对偶point(n·b,−n·a)，原标签(t,η)对应line v=t u−η；逐代表原clock给M≥K^-Cδ^-1且s=1 pencil。RW(1,1)给≥K^-Cδ^-2+ε条对偶线，原native总标签upper≤Kδ^-2+κ，取ε<κ、η最后小即矛盾。权层、代表clock、邻格和原分母均有实付。root新增§4与B§7正确标为19.4/固定normal旧闭包，不是一般β的新κ<1排除。

## 4. 全ambient秩、actual子族和精确fine缺陷

V_t=(n_t,t n_t)含固定坐标1,t。至少三个不同times上rank≤2使每个β_i及tβ_i同时属span{1,t}，相应二次多项式有三个根，迫β恒定；反向成立。共同非零scale不改row rank，若对所有ambient λ的观测均为共同injective clock的affine函数，代标准基亦得rank≤2。此证明不要求times连续，却确实要求全ambient λ与共同linear observable；没有证明任意nonlinear diffeomorphism或实际子族不可直化。

β=t e₁而实际b=0、a为四维网的vertical单位管族，其F_t=a₄−ta₁全部直线。它的joint4AD/whole-CW由slice积分成立，严格校准上述ambient量词不可删，但仍缺完整source。

root§7/B§6的插值恒等式逐项重算为

    F_tλ−[(1−θ)F_t0λ+θF_t1λ]
    =−(β(t)−β_lin(t))·(a_H+t b_H)
     +θ(1−θ)(t1−t0)(β1−β0)·b_H。

交叉项正号正确。真实单位轴(t e₁,0,t)、0≤t≤1/√2给F_t=−t²、中点缺陷1/8；即使β affine仍不成为fine δ直线。一般Lip仅付第一项O(Kh)，不是免费O(h²)；单在affine例中fine误差也需h≲√δ，并损真实clock比例。例子只反自动直化步骤，不反完整source、所有curved工具或特殊actual carrier。

## 5. 原质量、native输出、旧闭包与反攻边界

A原终时公式与root/B使用的native观测一致：η_s保原baseline、(c_t−c_s)x、(d_t−d_s)·w、(s−t)(ξ_y−d_s·ξ_w)，角项为(s−t)(b_t−c_s−d_s·a_t)φ。fixed s的φ线性不授跨s同一条平面线；s必须来自该actual T的原visits，不可splice两个arms或赠独立time/角law。native(t,η)平面确存在且small，但轨迹一般非直线；物理π确straight，但small native upper丢失。不能组合两个不同输出的有利条件。

原point方向在某(φ,normal slope)平面是同一条线上κ维点，并不自动是κ维不同lines的pencil；跨time还欠affine-line parameter law及诚实global upper。label/shading restriction只保原upper。平均incidence先heavy才付逐管clock，之后再限times仍需重付；原CW重归一要乘原质量倒数，AD lower及完整Φ不能默认继承。root/B未用这些非法闭包。

R74依AD0才有有限次同label的K成本，不自动扩成positive-dimensional标签；R45真实star/good-rank/原alphabet费用、R77已付的weighted robust双fibre应用和旧CP/PM/PW正幂等价保持冻结。当前校准只证明指定弱输入不能免费升级，并非完整mixed42反例。没有把所需共同carrier、q2、smooth β或独立g补成新原假设。

## 6. 修正、宏观后继与最终结论

本次fresh补读了root§4完整constant-β dualRW段、B§7相同旧闭包，以及终macro/next/source各6节。macro明确真实π有效而饱和、q1已可走旧固定normal出口、ambient秩不排actual子族；next没有预选新gain，仅要求不同原联合约束，四完整路线仍open。保守ordinary/fullbranch-saving时钟18与实际接口审查progress分列，没有把source核验当新界。A§1读域已收紧为19.4声明及19.5相关输入，未冒未读高级proof。

无未解决强制项：对实际共同平面入口、RW饱和、原CW q1/真实bush、constant-normal旧应用、ambient-rank范围和fine defect的有限结论，全文通过。完整κ∈(0,1) mixed42未证未否，ordinary/general Hausdorff增益、严格低维full-direction反例及Goal完成均未获得；不登记新数学ID或重大/新颖声明。停止本轮直接planar接口及κ/β/window微调，不将初等有限证书替代完整source。RW/WZ高级wholeproof仍具名，本审为项目内部独立审查，未经外部同行评审；不预认证未来元数据、Git、同步或来源计数验证。
