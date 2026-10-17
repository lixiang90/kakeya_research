# R0058：原割线门槛、二维上限与 source 范围正式独审

2026-10-17，A。已实际完整读取最终 root《R0058_secant_slab_dichotomy_and_dimension_ceiling》10节、B《R0058_joint_geometry_and_counteraudit》8节、A主稿11节、macro6、next6、working_spec新增§7及原6节。本人撰写的A稿不计为独立复核；以下逐步独审 root/B。结论：所列有限 slab 门槛与 standalone 二维预处理反攻在明确范围内通过，无待修数学项。没有证明 common-kernel、完整 Mat2 或 H5，未经外部同行评审，不预认证后续metadata/Git。

## 1. primary、旧闭包与实际对象

本轮实际重读 WZ2609.22035v1 PDF88–89、抽取 `split('\n')` 4603–4695行的 (163)–(166)，并对照已审R16 linewise/source/coarsening稿。原20.3输出标量A；R16通过每个固定ψ的像落线来在同一fiber里调用13.5。common-kernel F=F0+u(t)eᵀ、非共线二维u不在该已付PENCIL/IMAGE类内。固定e·ψ非零没有把二维u曲线变直；标量Y投影可满1维而Y仍为2−κ维，不可据13.5自动加回二维。

root保原finite quotient图：同一两个time priors、原used-angle差重数、二维输入输出及0≤g≤1。standalone门槛舍去了一部分actualsource假设，所以只给该较弱环节的严格结论，不冒Def17全部证明。新 Th2.2仍须条件time双profile、真实jointellipseK、finiteD及X_v左端，不能因形式为θQ就把θ重置uniform；A对θ-clock的核对已区分整体support exponent tθ与conditional sθ，未将两者免费相等。

CP/PM与旧Y-only/BSG、R57 scalarK/fullslab等停止记录仍保。working_spec§7先选实际secant任务，再做下述证明；不是为H5另立一个等价gain名称，没有新ID或重大性认证。

## 2. 非零 offset：完整双 anchor 证明

逐式独核root§§2–3。时间概率ν只需长度q≥r的interval cap Kq，允许原atom重数或同一time不同辅助值；u仅bounded。关系E(t,s)对称，CS使p²不超过两个独立anchors的共同neighbor平均。近anchors |t1−t2|<ξ质量≤CK max(ξ,r)。far anchors的两个误差方程无分母消元，确得

    A(t1−z)(t2−z)−c(t2−t1)=O(ε)，
    A=ℓu(t1)−ℓu(t2)。

time有界，若|c|ξ≥Cε且共同neighbor存在，则|A|≥c0|c|ξ；否则二次项不可能抵消常数项。除A后monic quadratic sublevel至多两个interval，总长≤C√(ε/(|c|ξ))，有限floor给共同neighbor质量≤CK[该长度+r]。取ξ=max(r,C1(ε/|c|)^(1/3))；ξ=r时sqrt项≤Cr。非小ratio或过大ξ用p≤1，故

    p≤min{1,C√K[(ε/|c|)^(1/6)+√r]}。

常数对全部ℓ,c统一；没有用不可控derivative、Jacobian rank或slab的概率union。允许same-time多label时，该二次式仍限制time投影，原interval cap照样控制其全部标签质量。

θQ版本先在原reference下固定θ；θ≠0的epsilon/offset比值不变，θ=0且|c|>ε时无贡献。按原独立角prior积分后任意相关g≤1的原质量仍受同界。这里独立性只在原reference，未误用保留g后的独立性。

## 3. nearzero、原g质量与合法限制

root§4的近零结论确实保双方time同片。令λ=ε^(a/2)≥r，offset≤ε^a；删|t−s|<λ付≤CKλ，若σ足够大可保σ/2。余|ℓu(t)−ℓu(s)|≤2λ。用fixed邻格覆盖得到原逆像B_j，令P_j=ν(B_j)、H_j为同一个删后g在B_j²上的绝对质量，则

    ΣP_j≤C，ΣH_j≥σ/2，H_j≤P_j²。

选择H_j≥cσP_j，推P_j≥cσ、H_j≥cσ²。normalized restriction后的图密度≥cσ，time cap多付1/P_j，原SM命中比例亦多付1/P_j。不能把原总mass m下的概率p事件误当绝对mass p；此处σ始终为原质量。

对D先删小θ付Kθ ε^(aγ/4)，再删小时差付Kt ε^(a/4)，余同宽Cε^(a/2) strip，时间和角标签原重数均保。source下先定粗精度/γ再取h小才能吞费用，未把subpower当O(1)。整time片限制只是平均incidence闭包，不能赋给每管新的逐管marks。

root显式保留一个关键未付接口：strip宽λ≫r时，投影u到线会增加O(λ)输出误差；不能直接调用原r的R16。要coarsen须重新付原Y input/output、tubeKT、g quotient和all-real SM。故本轮没有通过近线片就完成common-kernel的逻辑跳跃，也没有把g未使用的时间段从rawQ law里无费删掉。

## 4. plateau反攻的全部原参数

独立核root§§5–8/B§§2–5。ρ=2^−floor(dN)、δ=2^−N，B保每ρ-cell左半的全部δ-grid，#B=1/(2δ)。在任何中心属于B、半径δ≤q≤1的ball中，一侧平台或相邻周期占比给c q/δ至C q/δ个点，故是真1AD，不只upper。端点/半开约定只改常数。

hδ左半恒j²ρ²、右半连接，斜率≤4且连续，||hδ−t²||∞≤Cρ。d>a使任何全实matrix affine fit的第二row/第一col迫monic quadratic sublevel≤Cδ^a，B的原cap给质量≤Cδ^(a/2)≤δ^b0，所有实系数统一。coarse spatial line的unit normal：|n2|≥1/4用二次sublevel，否则一阶导数有固定lower；d>e使所有Cδ^e strips均只含≤Cδ^(e/2)原time质量。平台质量ρ=δ^d本身并非subpower，不能免费限制到它。

每个平台对j,k严格有Q=(z²,c_jk z)，弧Lipschitz常数固定。ρ^−2个平台对给全support cover≤Cδ^−1ρ^−2；这覆盖全部原pairs，不是采样或单点rank。Cantor H=C_L²的κ=2/m、slabγ=1/m固定，常数只依固定M；θ差保原ordered-pair权，distinct support≤3^L不需要signed表示唯一。乘θ≤1不扩大cover，因此

    N_(Cδ)D≤δ^(−β+o(1))，β=1+2d+log_M3<2。

root数值m16,d1/16给β<1.225与κ1/8正确；可先固定这些再L→∞，无需有限数值实验。该反攻确多保matrix-time-angle分解，不能以R27 generic digitalD已否定为由跳过本轮核验。

## 5. 任意sublaw、ellipse及四维quotient范围

全support cover是任意后续submeasure的共同upper。若normalized law在每Cδ-ball质量≤K′δ^(2−ζ)，求和给K′≥cδ^(−(2−ζ−β)+o(1))；与保留质量多小无关。若用未归一化upper，保mass δ^h与K′≤δ^−h在2h<2−ζ−β时矛盾。故任意dominated/重加权selection都不能以subpower费用在此support上取得所声称2−ζ Frostman。没有假新selection独立。

它仍不是原translation graph或source反例：未建A_±、a+D∈A_+的dense g、原tubeKT/AD输出比、全管CW或ξ/coherence。parameter g≡1只保原pair law，不能冒同一g也有输出关联。反例仅阻standalone secant的二维预处理，不排真正A-D耦合。二维Frostman也不是初始jointellipsecapacity必要条件；root§10、macro与next均保留这一点，不能由cover否掉所有Th2.2接口。

本轮另实际读WZ原PDF4/抽取160–173行：作者明确陈述一般R4 CWalone管族有quadric浓集、union≤Cδ^(1/2)障碍。这里只认证该primary**陈述及scope**，没有重构全部例子。它不反普通all-directions Kakeya；也不能把OAI4集合维数结论当任意CW-law union theorem。root/next对quotient仅继承CW而未有joint3AD/角先验的责任准确。

## 6. 最终scope、macro和停止

fresh完整读取macro6、next6/spec7：本轮通过的是非零slab统一upper、nearzero原g同片质量提取、及更强standalone二维预处理的严格有限反攻；无高维维数改善、Kakeya反例、完整common-kernel或新颖重大声明。source具名wholeproof层次不变，已付四维assembly及既有KT定位未重开。

停止单独D的rank/slab/cover升级与plateau/Cantor参数微调。下一只有真正利用原A-D输出关联/wholemetric并有原量词的新任务才可推进；nearline coarsening仅为旧结论的闭包核验，不能独立冒major。next没有把尚未选定的后继定理预称已证，也未把新增2Fst或conditionalK当公设；若旧scalarABC/全称shadinggain已直接覆盖，应记旧应用而非新方向。

**最终审查通过上述范围，无待修数学项。**长期Goal保持active，H5/general仍未完成。两指定文件由本人终检后停止编辑检索，由root统一元数据、验证和同步；本review不认证那些尚未发生的操作。
