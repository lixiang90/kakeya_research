# R0079：原数字时钟、全尺度算子law与所有实仿射非拟合

2026-10-18，B阶段II。按先锁的R79 spec§2证明有限joint接口反攻的时钟部分；不称完整Def17/Kakeya反例，不作ordinary或新major声明。

## 1. 参数、欲证范围和原分母

固定有理0<τ<1/2、α+β=1、α>β+τ及0<γ0<β；例如(α,β,τ,γ0)=(3/4,1/4,1/8,1/8)。固定0<ε0<1/20及0<θ<ε0τ/100。给定损失上限h>0与固定高阶和集阶数J，先取整数C*，后取L为4C*的足大倍数，使η=C*/L<h；L固定后令B=2^m→∞，m沿使所有幂整数的倍数，δ=B^-L。可再减小h，不能让L或J随B增长。

设Q=B^τ、R=B^(1−τ)，均为偶整数，QR=B。以下C可依固定指数和J但不依B；C_L允许依固定L，最后由B足大吸收。若证明中出现B^C C_L，先令C*大于有限个C，后令B足大，即B^C C_L≤B^C*=δ^-η；要求多个固定幂费用小于δ^-h时，再预先增大L。C*的选择也满足第8节NF不等式，不反过来依η或L。

源窗口只用ρ=δ^(jη)=B^(-jC*)，δ^(1/4)≤ρ≤δ^η；它们都是dyadic格的完整base-B prefix窗。所有平均均对同一个原time集Z归一；不先用distinct operators代time，也不把g删选授予完整源。

## 2. 精确near-full time集合及interval cap

每位独立取q_i∈{0,…,Q−1}和r_i∈{0,2,…,R−2}，令

    d_i=R q_i+r_i，u=Σ_(i=1)^L d_i B^-i，
    b(u)=Σ_(i=1)^L q_i B^-i。                       (1)

首位只取Q/4≤q_1<3Q/4，r_1不变；这恰选首digit处于[B/4,3B/4)的完整偶格。所得Z_bulk⊂[1/4,3/4]，#Z_bulk=(B/2)^L/2。设Z=Z_bulk∪{0,1}，ν=Uniform Z；两anchor给定F_0=I、F_1=0，bulk用后文式(7)。

数字表示唯一；不同u的最小距离至少2δ。因此

    2^(-L-1)δ^-1≤#Z≤δ^-1，
    ν(I)≤C_L(|I|+δ)。                              (2)

第一式在B足大后给#Z≥δ^(η−1)。bulk的ν质量1−2/#Z→1，每一native pair上的同一bulk clock都如此，不只是平均pair近满。这里不声孤立anchors的time ADlower；本接口要求的near-full总数与interval upper由(2)直接付。若I是ρ-prefix窗且有bulk点，首digit限制已完全决定，剩余L−k位独立，k=−log_Bρ；其点数正是(B/2)^(L−k)。空窗为0。半开窗约定消除边界重复，最后端点1单列。

## 3. 实际全局Lipschitz而非仅dyadic振幅

取两个bulk times，第一不同位为j，记D=|d_j−d'_j|≥2。后位u差绝对值小于B^-j，故

    |u−u′|≥(D−1)B^-j。

因q_i=floor(d_i/R)，|q_j−q'_j|≤D/R+1；b的后尾差至多Q/(B−1) B^-j。因此

    |b(u)−b(u′)|≤(D/R+1+Q/(B−1))B^-j
                    ≤4(D−1)B^-j≤4|u−u′|。          (3)

最后不等式对B足大统一成立，常数不随L。并且0≤b≤Q/(B−1)≤2B^(τ−1)。定义b(0)=b(1)=0时，anchors距bulk≥1/4，(3)仅需另增固定常数仍全Z成立。若只需连续ambient函数，可作实值Lipschitz延拓；证明从不把该延拓的非原times当原law。特别同一dyadicρ窗的b振幅Oρ，原dyadicLip直接成立。

## 4. 有限数字law的全尺度interval估计

先自证基础有限式。若D_s(n)是n位base-B、字母数A≈B^s、步长1或2的短字母集，均匀概率ω_s，则对任意interval I、0≤w=|I|≤O1，有

    ω_s(I)≤C B^C(w+B^-n)^s_s，
    s_s=log_B A。                                  (4)

证明：在B^(-j-1)<w≤B^-j处取j≤n。不同j位prefix的中心间隔≥B^-j，短digit尾部≤C B^(s_s−1)B^-j；B大时I仅交固定个prefix。每prefix概率A^-j≤B^(s_s)w^(s_s)。w<B^-n用最大atom A^-n；w≥1或n=0用平凡界。固定首位半字母只多因子2。此证明适用于q-law的s_s=τ，以及r-law的

    s_R=log_B(R/2)=1−τ−log_B2≥τ                    (B足大)。

对n位完整tail设U_n=R Q_n+R_n、B_n=Q_n，其中Q_n、R_n独立，分别使用q、r字母。任意实a,c及w≥0，

    P{|aU_n+B_n−c|≤w}
                ≤C B^C(w+B^-n)^τ。                (5)

若|aR+1|≥1/2，条件化全部r digits，直接对Q_n用(4)。否则|a|≥1/(2R)，条件化全部q digits，对R_n用宽2Rw的(4)；乘R^(s_R)≤B后，且s_R≥τ、w+B^-n≤1时，得到(5)。大宽度由平凡界付。这里a可任意大，未预设bounded slope；概率不是独立化原g所得，而是本模型time digits的实际product定义。

## 5. 同一原clock的prefix cap、算子小球与coverlower

固定非空bulk prefix窗J长度ρ=B^-k，k≤L/4。在其中u=u_J+ρU_(L−k)、b=b_J+ρB_(L−k)，其真实conditional law仍是第4节的独立tail。因此任意实a,c有

    ν_J{|b+a u−c|≤w}
           ≤C B^C((w+δ)/ρ)^τ。                    (6)

右侧≥1时取平凡界；本式没有把fine floor B^-(L−k)遗漏。k=0的bulk首位半字母只改固定因子。全局所有尺度的b球cap直接用第4节n=L、a=0，不依赖此处k≤L/4的NF窗口限制；加anchors总atom≤C_Lδ≤C_L(e+δ)^τ，所以对原ν和所有δ≤e≤O1，ν{|b−c|≤e}≤C_LB^C e^τ。

T_u=I+b(u)E12在bulk对b是等距的固定线性嵌入，故同一原time概率有T-ball cap。包括anchors时可另赋相同公式的T值用于law，真正可逆native公式只在bulk U使用。由概率1和每e-ball质量upper，N_e{T_u:u∈Z_bulk}≥C_L^-1B^-C e^-τ，所有δ≤e≤1。这给正维operator-law/coverlower，未把有许多重复的原times替换成Uniform(distinct T)。

## 6. 同一F的分式关系、满秩、boundedness与Lip

在bulk设N=E12及

    F_u=uI−u(1−u)b(u)N，M_u=F_u，
    C_t=(1−u)M_u，C_s=u(I−M_u)。                  (7)

N²=0、u∈[1/4,3/4]和(3)给F、Ct、Cs统一有界且全局Lipschitz；M及I−M的最小奇异值均≥c>0，逆也统一有界。直接相乘得

    M_u^−1=u^-1I+u^-1(1−u)bN，
    C_t^−1 C_s= u/(1−u)(M_u^−1−I)=I+bN。        (8)

anchors F0=I、F1=0距bulk有固定gap，故F在整个Z仍有统一global Lip常数；不需bulk公式在0/1连续取极限。可在两个空gap延拓，不把gap点加入ν或NF计数。任意两个不同bulk times，F_u−F_v是对角值u−v的upper triangular矩阵，det=(u−v)²；exact cone不等于全差rank1或共同image/kernel。原t/s为这两个指定anchors，A=I；不伪称本模型由完整源锚管算法自动产生。

## 7. 任意实matrix affine fit的slope必须从原times支付

固定合法ρ窗J且有bulk点。取任意实2×2矩阵P,Q0，不限制其系数，考察

    H_J={u∈Z∩J: ||F_u−(P u+Q0)||_max≤ρ^(1+ε0)}。

若#H_J>ρ^θρ/δ，由fine δ分离，其extreme points距离≥cρ^(1+θ)，因为阈值在ρ≥δ^(1/4)时→∞。取两extreme fits，用第6节真实global Lip得

    ||P||≤C+ Cρ^(ε0−θ)≤C，||Q0||≤C。             (9)

不是仅由窗内diam F=Oρ误报uniform slope；该较弱事实只给ρ^-θ，而本模型确由(3)拥有global Lip。若H_J少于阈值，欲证NF已成立，不需选anchor或证明slope。max-entry norm逐entry适用，任何固定等价矩阵范数只改常数。

## 8. 从matrix fit到line-strip及NF的非循环参数顺序

取fit的(1,2) entry。bulk的u(1−u)≥3/16，故在H_J有

    |b(u)−Rfit(u)|≤Cρ^(1+ε0)，
    Rfit(u)=−(P12 u+Q0,12)/[u(1−u)]。

(9)给Rfit在整个bulk上的C² norm≤C。J长度ρ，在其中心Taylor一次，得到一个真实affine函数a_J u+c_J，且

    |b(u)−a_Ju−c_J|≤C(ρ^(1+ε0)+ρ²)
                            ≤Cρ^(1+ε0)，u∈H_J。

(6)及δ≤ρ⁴给H_J在完整prefix clock内的比例≤C B^Cρ^(ε0τ)。乘#(Z∩J)≤ρ/δ，得到

    #H_J≤C B^Cρ^(ε0τ)ρ/δ。                        (10)

先固定C*使C* (ε0τ−θ)>C+2，且满足第1节有限费用；再L为4C*的倍数且足大令η<h；最后B足大。所有合法ρ≤B^-C*便使C B^Cρ^(ε0τ)<ρ^θ，和反设矛盾。因此对每个原allowedρ窗、每个实P,Q0，

    # {u∈Z∩J: ||F_u−Pu−Q0||≤ρ^(1+ε0)}
                                      ≤ρ^θρ/δ。 (11)

常数不由μ=logρ/logδ回选ε0或θ；η=C*/L可以任意小。NF是实际finite原clock命中数，不是global非affine、矩阵图维数或数值实验。

## 9. 任意dyadic窗、孤立anchors和有限深度测试

ρ=B^-k本身为dyadic尺度，标准dyadicρ窗正好固定前k个base-B digits；首digit bulk限制取完整格，所以窗非空则tail独立，无边缘fractional law。半开约定下没有双计，u=1单独放末窗。ρ≤B^-C*<1/8时，anchors与bulk不在同窗，每窗anchor数≤1；而ρ^θρ/δ≥δ^(-(3−θ)/4)→∞，故(11)在这些窗亦成立。空窗平凡。

若用固定倍邻窗代标准格，可覆盖固定个标准prefix窗，(10)只多常数；也可把θ先留余量再吸入。本文精确(11)按锁题的原dyadic窗给出，不把移动任意实窗的无条件independent尾声作为公设。

有限深度不隐藏：k≤L/4，tail深度L−k≥3L/4，NF宽ρ^(1+ε0)/ρ=ρ^ε0至少为B^(-Lε0/4)，远大于B^-(L−k)=δ/ρ；所以(5)的atom floor实际被吸收。τ固定、Q和R字母均有多个元素；B足大使s_R≥τ。若ρ小到δ或L随B增长，本证明的NF阈值/费用不被声称继续有效。timeδ-grid和anchors都在同一物理clock，不做重新time change。

## 10. 与同一native图、原质量和共同carrier的联合检查

几何模块取固定D倍的A=D(D_α×D_β)、X=A−A。展开bD_β的raw coefficients≤CLB^(τ+β)，β+τ<α使其落在固定倍α字母；L后乘积tail≤CLB^(β+τ−1)δ=oδ。因而可用一张与u无关的finite product-digit C包所有A+(I+bN)A，付固定D、固定高阶signed和集及δ容差。不是每u分别选small image再免费相交。

在bulk取Y_u=C_t(u)C及统一fine分离代表，anchor取Y0=Y1=A。设g(y,y′,u)=1_bulk(u)，每(y,y′)保留ν质量1−o1，rectangle平均也1−o1。对同一(y,y′)取真实直线

    x(u)=−(1−u)y+u y′，z(u)=u y′。

其native normal z−F_u x=C_t y+C_s y′，两个anchor值正是y,y′。全部clock共用这条线，不为每time另选line。bulk axis和速度有界，且因digits的直径→0最终已在固定小盒，不需要物理或time重缩；time分量在整个[0,1]精确保持原u。这是所锁wholeclock line接口，不额外宣其Euclidean弧长恰为1。

S_u=T_uT0^-1=I+(b(u)−b(u0))N保W=e1，ell=e2^T、v0=e1给ell adj(M_u)v0−ell(v0)detM_u=0，未除0。Ct在同ρ窗变化Oρ，故该窗的Y_u union落在N_Cρ(Ct(anchor)C)；这只给应核的coarse AD上/cover与support-centred lower，不给该union虚增独立time维。各Y_u的AD1、任意orientation tubeKT以及X高阶small sums由A模块独立完整核，本文不以card上界替代这些几何要求。

## 11. 反攻结果与完整source明确未保的条件

已付的时钟模块同时有：near-full原总time数与interval upper；全尺度b/T球cap和operator coverlower；真global Lip及原dyadicLip；原allowed尺度所有实affine fits的(11)；same g的逐pair bulk近满clock。它们与同一small-action X、native真实输出和exact cone兼容，不能用“光滑二次global非仿射但local Taylor可拟合”否本模型，因为数字law的(5)(10)正是原local非拟合证明。

但这只反驳“上述提取后的联合有限接口已充分授reducible增长”。真实wholeline标签(y,y′)仅二维，不是原joint AD4；每physical point可仅一条line，因此pointΦ AD1/slab及filled X2未建立；未给wholeT normalized CW、terminal selectedξ和其coherence。不能用κ=0 padding补这些输入，不能宣Kakeya或完整matrix33反例。anchors time lower未声称；literal完整Def17也不由原模型倒造。原R78δ²块质量在此没有变成全源比例：本模型是给定该block接口的合法配置，不是完整源初始化。

本轮不续R78 BSG/Ruzsa常数、R77NI更多尺度、R72basicness/多time或旧R28自由action方向。严格joint反攻若经独审通过，只说明下一完整源机制必须用尚缺的真正joint约束；高维Goal和外部同行评审状态都不由此改变。

## 12. 实际交叉读取、独立分工与停止

本稿实际全文读R79锁题spec5；沿用本轮阶段I的GOAL/STATE/ROADMAP/registry恢复和R78原式独审。第2–9节为本文完整有限推导，不调用新的高级文献定理或浮点实验；官方byte/Git/sync没有由本人新核。

随后已实际全文逐式读root整合12节。共同C的raw卷积与真实tail、固定高阶signed和集、任意orientation的product strip概率/支撑球lower→KT、X全尺度heavyball packing、Ct exact输出与fine分离、sameν逐pair平均及cone均核过，当前未见强制数学修正。root所给数字几何是独立链，不将本稿自证的clock/NF重复计作独审。

又已实际全文逐式读A阶段II12节。其(2)(3)共同carrier的raw integer convolution及末尾真实误差、(4)所有尺度support-centred AD lower、(5)(6)任意orientation rectangle概率除以disjoint support-ball质量的KT、signed X的真实product/固定阶动作、Ct有界逆与Dδ fine分离、整窗coarse AD的独立lower及原g/真实同线/cone均核过，未见强制修正。A§11只用窗振幅得到ρ^−θ的C²及ρ^(2−θ)Taylor，θ+ε0<1下同样合法；本稿用实际global Lip得到O1，两个独立链不冲突。

完整互读范围至此为root12、A12及锁题spec5，自己B12的时钟证明不计作独审。B自身clock/NF由A/root实际独立审，不以本稿自审替代。通过范围只限已列的严格joint有限接口，完整源缺项保持第11节；正式审查文件另待授权，当前不认证未来元数据/Git/sync。高级wholeproof未在本模块重新复证，未经外部同行评审。
