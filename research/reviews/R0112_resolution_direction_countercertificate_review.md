# R0112：resolution方向帽反攻的独立逐步审查

2026-10-26（Asia/Shanghai）。reviewer：new_projection_gate，独立于原algebraic稿的作者。本次只新增本审查文件，不改被审稿、不改metadata或Git。结论：在下述精确范围内**通过**；没有发现须推翻具体拒桥的数学错误。特别澄清clock计数incidence与实体体积incidence的不同数量级。本审查不是外部同行评审，也不认证任何未来整合或同步。

## 1. 审查对象、实读与范围

实际全文读research/rounds/R0112_resolution_transfer_working_spec.md和notes/30_algebraic_geometry/R0112_singular_carrier_new_input_gate.md当前八节。重点重新独算§4单位轴、方向双Lip、lift aliases、round marks、实体体积、q分包修复，§5各向异性density，§6exact analytic四参数product下界。又实际读已存Binyamini–Novikov2009.02082v1 extracted的Th1/2、Def2/3和§2.1–2.2全部hyperbolic论证，以及DIR003、FSD001的精确现有有限statement；高级四维proof按仓库已有具名输入继承，本次不冒重新全证。

被否桥的量词是：仅凭固定uniform双Lip的resolution chart、strict transform光滑、所有原轴lift仍直且nonshort、round marks保量，是否足以使**同一indexed family**的原方向cap按只依chart的常数继承？一个这样的固定chart失败就反此桥。它不反“存在另一chart或额外packet机制”的命题，不反完整G4，不涉及ordinary五维全方向低维集合。

## 2. 固定chart、载体和真正单位原轴

取P=(x1x3−x2²)/2。系数l1范数确为1；不可约二次因子不依δ。β(u,v,w,z)=(u,uv,uw,z)满足

\[
P\circ\beta=\tfrac12u^2(w-v^2),\qquad \det D\beta=u^2.
\]

在所用固定紧域u∈[1,3]，β^{-1}(x)=(x1,x2/x1,x3/x1,x4,x5)各固定阶导数统一有界。strict transform w−v²梯度的w分量为1，故处处regular。这里没有small Jacobian、exceptional-divisor近零或δ依赖的条件数。

记L(q,b)=sqrt(1+q²+q⁴+|b|²)，V=(1,q,q²,b)/L，A_q=(2,2q,2q²,0,0)。参数|q|,|b_j|≤1/20给L固定接近1。ℓ=A_q+tV、|t|≤1/2的Euclidean长度精确为1；且x2=qx1、x3=q²x1，所以每根whole轴exact-contained于Z(P)。x1∈[1.5,2.5]，其δ-round tube在δ小后留于chart好域固定内部，端帽同样留有margin。

对normalized V，v1≥c>0，反解q=v2/v1、b_j=v_{j+3}/v1给固定Lip inverse；正向亦固定Lip。因此参数Mδ-grid给δ-separated无向方向：全部v1>c，可用该chart固定处理无向正负同一问题。任一θ帽的参数逆像包含于半径Cθ球，格计数≤C(1+θ/(Mδ))³≤C'(θ/δ)³，δ≤θ≤1。选M大后每C0δ帽仅O(1)权，N≈δ^{-3}。这是所需s=3 allscale输入，单位长度归一化未破坏它。

## 3. Lift仍直，却有真实δ^{-1}方向bin权

逐点代入inverse，

\[
\widetilde\ell(t)=(2+t/L,q,q^2,b_1t/L,b_2t/L).
\]

其方向向量是(1,0,0,b1,b2)/L，单位方向为(1,0,0,b1,b2)/sqrt(1+|b|²)，完全不含q。其线段长度sqrt(1+|b|²)/L在固定上下界间。于是对每固定b，约δ^{-1}个不同q原labels exact共享一条lifted方向；任何包含此方向的固定倍δ帽权至少cδ^{-1}。没有靠“角度接近”或端点误差才能得到的伪重合。

β双Lip给

\[
N_{c\delta}(\widetilde\ell)\subset
\beta^{-1}(N_\delta(\ell))\subset
N_{C\delta}(\widetilde\ell),
\]

包含端帽；Jacobian在固定上下界间。因此原full round-tube marks可真搬到lifted round包中，density只损常数。同一physical t参数的全部marks保持，换为lifted自身arclength只乘常数1/L。不需要将一根弯线当直线，也没有补满原来没有的marks。

固定shear w'=w−v²将strict transform变为平面；它沿上述轴恒等给w'=0，所以轴仍直、b方向仍相同。carrier变平不能恢复丢失的q方向：q被搬到位置v=q。故原α=O(1)直接继承为liftedα'=O(1)确被否，而失败者有α'≈δ^{-1}。

## 4. Round-tube实体并非小密度伪例：|E|≈δ

上界独核：全部轴在x1≥1的光滑图x3=x2²/x1上，坐标有界、图导数固定有界。其固定倍δ-neighborhood在有界盒中体积≤Cδ，包含全部原round tubes，故|E|≤Cδ。

下界：固定s=x1−2∈[1/5,3/10]，在每根轴上取t=sL，确有|t|<1/2且距端点固定正距离。x1切片内的轴心为

\[
((2+s)q,(2+s)q^2,sb_1,sb_2)\in\mathbb R^4.
\]

其中q由第一坐标、b由末两坐标双Lip恢复，常数对s统一。Mδ-grid上的N≈δ^{-3}点以cMδ分离；M大使其c'δ四维球两两不交，每球属于原round tube的相同x1切片。因此切片4体积≥cNδ⁴≈cδ。对固定正长度s区间积分得|E|≥cδ。由此|E|≈δ，是完整真实Euclidean实体计算。

当前G4要求δ^{4+ε}W/α≈δ^{1+ε}；实际δ更大，所以本例**与G4一致**。它的方向仅3参数，不含ordinary R5全部4参数方向，且无任何严格低Hausdorff维数Kakeya集合，不能称ordinary反例。

## 5. 两种I、删选的一幂和q包修复

working spec使用δ-clock格数；原algebraic稿§4末明确写I=Σ|Y_i|，使用5D Lebesgue体积。二者应在root整合中分别命名：

\[
m\asymp\delta^{-1},\quad
I_{\rm cnt}=Nm\asymp\delta^{-4},\quad
I_{\rm vol}=\sum_i|Y_i|\asymp N\delta^4\asymp\delta,
\quad I_{\rm vol}\asymp\delta^5I_{\rm cnt}.
\]

这里没有互相冲突的数值，但任何跨句“保I”均须指定同一种量。λ_cnt=I_cnt/(Nm)=1，λ_vol=I_vol/(N|T|)=1，可固定倍比较。

若每个b仅留一个q以恢复δ-separated lifted directions，则

\[
N'\asymp\delta^{-2},\quad I'_{\rm cnt}\asymp\delta^{-3},
\quad I'_{\rm vol}\asymp\delta^2,
\quad p=q=N'/N\asymp\delta,\quad\lambda'=(p/q)\lambda=1.
\]

这是whole-label选择，保每根完整marks，却丢一幂原总权和两种原I。若全部labels保留，则DIR003必须付α'≈δ^{-1}，所得lower同样损一幂：其#E4≥cδ^εI_cnt/α'只给δ^{-3+ε}；返回graph δ-thickness的5D体积只给δ^{2+ε}，而G4原预算是δ^{1+ε}。不是把平均λ改成逐管λ就能修复。

本例确有修复，故拒桥范围不能扩大。按q分packet：各包W_q≈δ^{-2}，b方向δ-separated、每bin权O(1)，逐包DIR003给4D footprint至少δ^{-3+ε}格，即4D体积δ^{1+ε}；增回实际w-direction δ-thickness得5D体积δ^{2+ε}。inverse tubes在v∈q+[-Cδ,Cδ]，M固定大使所有q包有固定overlap；约δ^{-1}包求和给δ^{1+ε}，恢复本例G4预算。

若要严格匹配DIR003的共同[0,1] graph-clock，可在全部lifted轴中取共同u∈[1.6,2.4]：对应t=L(u−2)始终离原端点固定距离，故每根full marks仅损固定比例。将该u区间作固定affine rescale，四维坐标(u,v,z1,z2)中的斜率为固定常数倍(0,b1,b2)，方向bin与mark费用仍只损固定常数；不需依q或δ重选clock。

原marks几何与q位置真实支持该求和，并非换分母。此修复依赖本例显式q-offset分离，不是任意resolution chart自动赠送的packet定理。原FSD001的s=3统一调用也已能直接处理全族，不因本轮坐标展示再记新成果。

## 6. 靠近exceptional divisor：形状和density账通过

在u≈r、δ≪r、v,w固定有界小盒，Dβ的singular scales确可比1,r,r,1,1，det≈r²。取沿自由z1的物理单位轴并在annulus内部，inverse round-tube实体的四个横截面尺度可比δ,δ/r,δ/r,δ，所以体积≈δ⁴/r²。此比较允许固定shear／tilt，不要求坐标截面逐点完全正交。

若放进round h=δ/r单位长包，其体积≈h⁴=δ⁴/r⁴，原full marks在新包的真实density≈r²。取r=δ^a，0<a<1，才同时满足δ≪r，density为δ^{2a}固定幂；不能对任意小ε算作subpower。返回原空间还要乘可比r²的Jacobian，而非在所有u上同一个精确恒等量。

这只是准确的单管接口压力例，不证明完整source必含这种annulus，也不排除付费分层或适当各向异性定理。§4在固定r时独立失败，故仅消除这里的condition-number损失仍不足以使原cap免费继承。

## 7. Exact analytic chart下界的product推广通过，但不反metric近似

原文Binyamini–Novikov §2.2明示：holomorphic map从N1(0,1)到xy=e、两坐标模≤2，其x-image在A(e/2,2)的hyperbolic diameter固定有界；覆盖x∈(e,1)需Ω(log|log e|)张。

被审稿要求的四参数版本可以独立逐步推出。设φ在N1((0,1)^4) holomorphic且实cube image exact满足x1x2=e、各坐标模≤2。恒等式先由实open cube逐变量identity theorem延拓到连通复域，故x1不为0，并满足e/2≤|x1|≤2；将annulus端点固定扩大一点可避免边界记号，不改常数。

任意两实参数点，用四条坐标段连接。每次冻结其它三个实坐标，剩余复坐标的N1(0,1)整条域仍包含于给定复邻域；Schwarz–Pick把每段的annulus hyperbolic距离界为同一固定常数。因此一张图的全部x1实image的hyperbolic diameter≤4C。若该图命中positive branch，实image连续且x1不为0，故positive x1-image为区间。annulus中正径向线的hyperbolic长度就是相应端点距离，区间长度≤4C。

要覆盖positive branch×(0,1)^3，x1投影必须覆盖(e,1)，其annulus hyperbolic长度≈log|log e|。区间覆盖长度次可加，遂图数≥c log|log e|。取e=exp(−exp(δ^{-a}))给≥cδ^{-a}。Q=(x1x2−e)/(1+e)仍degree2、l1范数1且irreducible；任何real singular点需x1=x2=0，与e>0矛盾。

这个结论严格针对固定复半径、固定解析范数、exact image的指定upgrade。finite-r Yomdin–Gromov定理、允许退化复半径或δ-metric近似carrier并不在被否范围内。特别e极小时坐标平面可以在相当区域作δ近似，不能将exact analytic图数下界升级为所有近似resolution的不可能性。

## 8. 最终结论与必须保留的边界

独核通过：固定uniform双Lip、strict transform光滑、lifted axes直且nonshort、全部原round marks保量，仍不能无损送原方向帽；真实失量为δ^{-1}的bin alias，或whole-label删选p=q≈δ。|E|≈δ及显式qpacket修复同时成立。shape/density例和exact analytic图数例各自有清楚范围，未混成完整source反例。

root整合须显式区分I_cnt与I_vol；这是一项记号／单位澄清，不是原稿既有明确定义的错误。另在引用§5的r=δ^a且δ≪r时使用0<a<1，不能无条件让任意a>0同时满足此前annulus假设。上述两点已在本审查中给出可直接采用的准确式子。

没有新的n≥5 Hausdorff界、newID、major或全方向反例。全文G4未证未否，regular-leading／exact旧闭包不重开。本审查只认证当前被读八节和working的具体拒桥，不预认证root未来修改、元数据、Git提交或远端同步。

## 9. Root整合与两项澄清的实际读回

按root后续授权，已实际读回algebraic稿§5当前r=δ^a句及其前后shape/density预算：现明确写**0<a<1**且说明这是为了同时满足δ≪r，原domain澄清已落实，不再有该处必修项。

又实际全文读notes/00_map/R0112_macro_and_charged_geometric_return.md当前六节，重点复核其§1–2和§5。root §2现分别给出I_cnt≈δ^{-4}、I_vol≈δ和I_vol≈δ^5I_cnt，并给删重复后的N'≈δ^{-2}、I_cnt'≈δ^{-3}、I_vol'≈δ²、p=q≈δ、λ'=1；这些均与本审查§5独算相同。weighted-bin的α'≈δ^{-1}与whole-label删选丢一幂明确分开，未把两种I混为同量。

root同时保留q空间packet的bounded-overlap修复和FSD旧闭包，因此没有把具体chart的失败升级为完整G4反例。§1限定本轮唯一主测试，§2明确不是高维正界，§5把无新ordinary/source正gain与限定拒桥证据分列，并保留同集全方向及严格Hausdorff上界的真反例要求。其停止项针对本次直接chart／exact analytic升级，不是所有resolution或δ近似carrier的不可能性宣告。

对本次实际读回的数学及声明范围，最终意见为**通过，无未解决必须修正项**。本意见仍不认证本稿未独核的其它新源wholeproof、priority、档案数目、元数据或未来Git／远端同步，也不授新的数学ID或Goal完成。
