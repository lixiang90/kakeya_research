# R0097：全局cap、原质量与局部small-loss范围独立审查

2026-10-19，B。仅针对实际读取的版本作内部逐式审查，**未经外部同行评审**；不认证后续元数据、Git或同步。

## 1. 实际全文对象及审查分工

实际全文读root主文 `R0097_scalar_Segre_local_spreadout_gate.md` 12节、A稿 `R0097_adapted_projection_primary_and_mass_gate.md` 10节、本B稿8节、reselection/working两spec各5节，以及终macro、next、source scope、round各6节。root/A落盘后逐步读其完整正文，不以readiness消息代读；B已补真实cross记录。

本formal独立主核root/A，B自己的Segre/插值与unitbush推导不计本人的独审。root已实际全文核B8，A也按分工独核本轮几何；各自认证以其实际记录为准。本轮必要primary为库存CSWZ v1引言§1.1–1.3、big-cell/model-H、Def1.4–1.5、Th1.2/1.6/1.7；R14和R76旧Schubert适用边界已实际对照。未新下载、未认证其45页高级wholeproof，fresh版本/原PDF图核不冒本人的新字节检查。

## 2. Scalar finite theorem强度与真实原source质量

root§§2/6–8、A§§1–4核通过。Th1.7当前ambient8、kernel7、output1，参数下标(8,1)；Th1.6的实际kernel7 affine-plane族则经负号/transpose写在R^(7×1)。两者m1或codimension1的model-H均是全部普通affine hyperplanes，不能误用一般矩阵rank-one限制。有限结论确是nearfull的标量t_point输出，而非仅half-plus或定性a.e.结论。

A§2独立原质量链成立：每层global Y维3−κ与filled scalar X使#E_t≥K^-Cδ^(−4+κ)；每p原Φκ给≥K^-1δ^-κ个实际角。给定固定t/原T，其截面只遇O(1)原δ分离points，且第一graph slope只遇O(1)个原角，故(p,φ)到witness T有固定碰撞，#T_t≥K^-Cδ^-4≥K^-C N。最后用了原bounded全T的N upper，没有把used族重置为原分母。

point参数格化的K重数、归一4-Frostman upper和选t_point=1−κ/4均合法；每个原visited P_t仍占≥K^-C原point比例。θ最后坐标t使一个parameter δ-cell至多接O(1)原times；point与parameter独立round只损Oδ原相位。若额外spreadout真满足，robust结论可用于实际P_t，ζ<κ/4与η后小给标签upper K^Cδ^(−1+κ)的严格矛盾。Th1.6另需point-heavy/共同M及(θ,offset)总cover，A已明列，不把平均、逐管及逐pair的clock下界混用。条件正链不算获得原spreadout。

## 3. Segre局部证书与全部删选的δ尺度

root§§3–5/A§§5–7逐式通过。原θ=(-β,−tβ,t)全部位于Σ={(u,v,w):v=wu}，不需β连续或dyadic Lip。Q_i=v_i−wu_i在Σ上为零，切H法向的v_i系数恒1；对z,z0∈Σ，切方程残差严格等于(w−w0)(u_i−u0_i)。所以该H是真实model hyperplane，局部距离≤Cr²，不涉及timegap或导数条件数。

实际输入是δ-cubes的union。中心和被测点各择本cube内Σ点，误差Cδ，故整个局部子族到同一H距离≤C(r²+δ)。固定b、选择C0大与c0小，使C0δ/b≤r≤c0b时严格小于br；每个非空子族、每个中心都成立。固定b且δ足小，dyadic奇异尺度数至少log₂δ^-1−2log₂b^-1−C。取Def1.5的全子族J′=J，正确推出C_spread≥c_bδ^-b。

准确停止范围是fixedb、C_spread=δ^-ε且ε<b。ε=b与ε>b不由该下界排除；不能用“存在的theorem ε可取小”替代对所有较大数值输入的反证。任何普通parameter/每point shading删选都仍在Σ，故同样不能得到任意small-loss输入；此几何结论没有假删后ADlower或保质量。

## 4. 全局hyperplane power cap、fulljet与有限grid

root§10及A§8的全局校准核通过。β=(t²,t⁴,t⁶)使θ为t,…,t⁷的signed permutation。任意unit-normal affineH对应一个degree≤7多项式，其非constant系数norm为1，与截距无关。若sublevel长度m>0，按长度分位或greedy选八点、间距≥cm，Lagrange插值给各系数≤Crm^-7；非constant系数lower迫m≤Cr^(1/7)。这已是自含证明，不需未声明uniform Remez常数。

P²−r²非零且degree≤14，所以sublevel至多固定数interval/point组件；uniform δ-grid质量≤C(m+δ)，r≥δ时≤Cr^(1/7)。θ最后t使time到parameter cells碰撞有界；本moment例另有固定Lip upper，uniform无权cell law与time pushforward权重可比，δ厚化/舍入只改r固定倍。故对所有global affineH的同一个power cap确成立。

观测V再含常数1，fullspan8和fullmoment jet非零也成立，但仍与第3节局部奇异性并存。这个严格分离并未给模型完整small native labels/Φ/两grain；R96已在完整source下排除该poly类，不能称它是当前完整source反例。全局cap的证明与局部失败各自量词完整，未相互替代。

## 5. 可逆chart、原商、弱校准及旧等价边界

root§9的有界可逆范围正确：ambient可逆线性变换诱导的projective chart须限制分母远离0、正逆前两阶导数有固定界；像Σ仍是codimension-positive smooth子流形，其切H误差为Cr²，真实δ厚化另添Cδ。只在该明确有界chart下保常数，不外推到δ病态变换。非可逆有效商可能改变维数/模型族，尚未被证书排除；任意非线性重编码也不能免费保持原πθ的线性作用。

R96精确span上的point-law 1-Frostman upper仍有效；它并不是当前parameter-ball的local spreadout或approxspan/conditional lower。R14/R76是fixed global Schubert/model-H退化，本轮在没有任何global H包含、甚至有globalcap时仍局部失败，未抄旧rank2为m1反证。正转移只作适用性证书，不另登记全称gain，旧restriction/shading正幂等价冻结不撤。

原unitbush沿R95已付范围复用：真实unitclock、方向δ分离、joint4AD和whole-containment CW可同时存在，John ellipsoid给凸查询计数并保原N；并集正5体积。它的native normal需满interval标签，缺完整smalllabel/Φ等，不是Kakeya或fullsource反例，也未授partial/fullPW。

## 6. 必修项、最终判定与宏观读域

当前实际全文审查没有未解决的强制数学或文档修订项。在明确的finite theorem和原bounded source量词下，原质量条件正链、所有rough参数的局部Segre证书，以及global-cap/fulljet分离校准通过限定范围独审。高级CSWZ/原WZ wholeproof仍具名；本人没有重审其完整高级证明，不认证新颖、重大性或无遗漏文献优先权。

终macro6/next6/source6/round6已实际全文读，均保留ε<b、非可逆商及全部原质量边界；保守ordinary/fullrough-saving时钟20与实际信息增益分开。完整ordinary、HRZ全部费用、sticky余分支及ordinary桥、同集全方向严格低维四路仍未解决。停止本直接small-loss桥的b/ε/局部曲率/chart常数续轮，不把新“adaptive”欲证公设当next成果，也不宣布所有受限投影策略失败。无新ID、ordinary新界、major或Goal完成；**未经外部同行评审**。formal完成后停止编辑检索，不预认证未来验证或Git同步。
