# R0101：原 witness box 的真实质量与删选闭包独审

2026-10-19，B／lifting_obstructions。实际全文后作有限范围独立审查，未经外部同行评审；不把本人推导计为自身独审，不认证全部 source wholeproof 或未来归档同步。

## 1. 实际全文范围、原目标和来源层级

已实际全文读最终 root《R0101_semialgebraic_witness_boxes_and_original_mass》12节、A《R0101_semialgebraic_density_primary_gate》10节、本人 B《R0101_native_graph_witness_and_complexity_gate》10节及 reselection／working 两spec各5节。A最后§8／10补的实际单box质量链已读回；终 macro、next、source-scope、round各6节亦已实际全文读。以下主核 root／A，不以本人 B正证代替独立审查。

本轮另实际全文读 R76主12、R44主8／B8、R45主10／B9，读回 WZ Def17.1–17.4、20.3(164)–(165)、21.1(172)–(173)、21.2及相关应用。新来源实际使用库存 FPS1502.01730v3的定义／Th1.1／1.3、Rubin2407.15518v2的定义／Th1.3／1.6、完整§5.2 Th5.1及该节 proof sketch；不冒已独证两篇全部 partition／cutting高级证明。root的原图视觉核／文件哈希为root实际工作，本人仅按实际本地读域记录，不重复认领下载或视觉核。

目标仍是完整普通／HRZ、sticky全部 rough及普通桥、同集全方向严格低维四路。此次直接门是同一个实际 R76 block的 native图能否以 subpower边际／原质量费用获得完整几何 witness乘积；并非假定 selected support本身 fixed-format。

## 2. 几何关系对任意原 mask 的正面应用

Rubin Th5.1的错误项是非齐次 boxes的产品计数总和，不是这些 boxes的个数比例。设 R为固定格式、0≤h≤1支撑于R、Σh=θV，其中V为原各侧大小之积。ε=θ/2时，非齐次区至多带走εV原 h质量，齐次 nonedge区没有 h，故完整 edge boxes合计保留至少θV/2。各侧部分数≤Cε^{-(d+ζ)}，k侧共有至多C^kε^{-k(d+ζ)}个 boxes，因此某完整几何 box保至少cθ^{1+k(d+ζ)}V原质量。用h≤1又得每个边际的相对 lower，root§3／A§4逐式成立。

这个结论允许任意相关、不可定义的 h，却没有补全 h>0的 selected support。两源的 fixed-format条件不能直接赋给任意子边集；反之也不能因 h相关便拒绝上述正用途。FPS的D为每个 vertex block次数，Rubin为总次数／谓词数量，root／A对两者区分正确。A§5对有理 vertex权的 extra-coordinate cloning保精确关系，不用可能改变边界的扰动；映回原点只增加非负产品权，实权有限支撑可用有理逼近及有限输出子列，逻辑成立。额外ambient维数和h的[0,1]支配必须付，当前实际无权产品域无需该扩展。

## 3. 实际 sameT witness 与产品分母

R76在明确 bounded／det-large分支中，joint residual细分保所选每条原 T的全部 S_T，同 native端点 pair的原 T重数≤M_0=O(1)。以此归一得到g≤1及总质量M=θ|Y_t||Y_s|m。保留族相对原全N仍只有含L费用的δ²级，不能把block重归一后视为完整源或免费保原 CW常数。

逐原访问预选一个原w(T,u)∈Y_u，第三域存(u,C_t(u),C_s(u),B_u,w)，则存在真实h，Σ_wh=g、Σh=M。该几何关系用四个双线性厚度不等式表示：total degree2、每block degree1，ambient13的tag构造合法；若另加label坐标则相应改到14并重算指数。F及Y任意性放在顶点集内，不破坏关系公式格式，没有额外 smooth／goodrank公设。

第三域大小W=Σ_u|Y_u|≈_Kmδ^{-1}，所以新density是θ_w=θm/W≈_Kθδ，而非θ。原M没有因此被删除δ比例，变化的是reference产品分母。固定一对端点后，每u仅O(1)个δ-separated w可合格，所以任一非空完整 witness box的第三域大小≤Cm，相对W至多CKδ。该 prior上界本身仍不能推出原 h质量小，root／A明确没有作此偷换；后续质量限制需要额外原Tube-KT。

## 4. Far clock、条带与真实单box质量逐步核算

取r=δ^c、0<c<1。每条 T的原访问时刻属于δ-separated Z，删除距t或s小于r者至多C(r/δ+1)。原各管|S_T|≥K^{-C}m且m≥K^{-C}δ^{-1}，所以相对删除≤K^C(r+δ)；η相对c先足小、δ最后小，可逐条保一半。于是M_f≥M/2且Σ_wh_f=g_f≤1。先证明逐管，再求和得平均保量，未用平均赠逐管；没有重新宣删后全部 Def17 lower。

完整 box若有正far质量，取其中一个far(u,w)。原系数精确满足

\[
\frac{C_t}{1-\lambda}+\frac{C_s}{\lambda}=I_2,
\qquad \lambda=(u-t)/(s-t).
\]

由于|s−t|≤2，far给|λ|、|1−λ|≥r/2，故max(||C_t||,||C_s||)≥cr。固定另一端和该第三顶点，将完整性的nearoutput式相减，一侧所有端点落在宽a=Cδ/r、长O(1)条带。这只用最大奇异值或一条大row，不要求该矩阵可逆。

在δ≤a≤1，原native Y的Tube-KT(δ,1−γ,K)给条带内a-cover≤CKa^{-(1−γ)}；每a-ball按原AD1 upper含≤CKa/δ点。以原|Y|≥K^{-1}δ^{-1}为分母，得到该侧比例≤CK³a^γ。长O(1)可用固定个单位tubes，不使用sub-δ尺度或裁切后的新 ADlower。最后必须使用Σ_wh_f≤1，才能不付额外w重数，得到

\[
h_f(Q)\le CK^3(\delta/r)^\gamma |Y_t||Y_s|m,
\qquad \frac{h_f(Q)}{M_f}\le CK^3\theta_f^{-1}(\delta/r)^\gamma,
\]

其中θ_f=M_f/(|Y_t||Y_s|m)≥θ/2。保q比例原M_f的B个完整boxes因而满足B≥cqθ_fK^{-3}(r/δ)^γ，允许重叠只会放宽upper。固定正γ，先取R76有限损失β≪γ(1−c)，再取η≪c及γ(1−c)，这些是固定正幂费用；subpower数量不能保固定比例或subpower比例。此actual上界与Rubin在θ_w≈θδ下仅给polynomial δ数量／质量保证相容，不是对具名定理的反例。

## 5. 限定反攻、删选闭包及旧输入排重

root／A的dense random mask例只否免费 selected completeness：即便恒真R有任意dense mask，也未必有大完整selected乘积。它不否第2节，也未实现原full T／CW／filled X／Φ。有限交替membership的复杂度反攻亦仅否无费消去任意Y。本人B初稿把2q个sample交替所需根数写得过强；根可落在sample上而引起两次变化，安全lower为sD≥(2q−1)/2。该mandatory字面已修，并与root§9及A读回一致；仍足以证明不能有uniform固定格式。当前没有遗留该错误。

完整 witness box要求同一个第三w适用于所有端点对，原输出关系只要求w可随(a,b,u)变化，二者不同。条带／质量上界没有排后者的大box或所有半代数方法，更没有证明完整source不存在。若消去w，需要给实际Y的描述复杂度；固定QE不会免费处理δ^{-1}个任意点。

顶点restriction保几何公式；whole-index restriction保原每管全部S_T，但改为新probability要付原N与新管数之比。box只留部分visits，保总I'不等于逐管保旧λ：以I'/(2N')做heavy可保I'/2，但管数及新阈值须同时计费。原h权和average／per-T量均如此，不能赠逐pair／全clock或新ADlower。

R44共同测试的physical体积、原访问重数和PW／CW预算没有被新relation格式自动压缩；两者不是同一个命题换名。R45的selected-tuple KBL原本允许任意选中hypergraph，不需Cartesian作为准入。新几何box也不赠good-BL或rank质量，反向从抽象box／mask重建原全数据未付。因此不登记成critical κ1 gain的等价结果，也不按文献新题名解冻旧参数路线。

## 6. 最终审查结论和停止范围

实际全文及逐式核验后，root12／A10在上述有限范围内通过，无未解决mandatory。本人B的finite根计数修复已记录；本人正证不算自身独审，root／A实际独立核其链另留记录。正面几何保原mask引理、真实rough编码、witness产品分母、逐管far删选、原Tube-KT单box质量及cover数、合法闭包和反攻范围均分清。

已全文核终macro／next／source／round各6：本轮严格费用改变后继动作，可记录actual信息；无ordinary／完整rough saving时钟24另计。停止直接witness completebox及d／D／ζ／θ续轮，保留可变w和其他真正新原联合结构的未排范围；没有qualified next gain被预授。完整四路与Goal仍active。

“通过”仅为本轮应用、费用和有限反攻的内部独立审查，未经外部同行评审。两篇高级wholeproof仍具名，未宣新resultID、major／novelty、完整source或Kakeya反例、任何新维数界；不预认证文件元数据、Git／sameSHA同步或未来回执。按授权完成后停止编辑与检索。
