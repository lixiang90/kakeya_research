# R0073：mixed32原零球、整time回传与细尺度native单管用途

2026-10-18，A。已实际全文读先锁的R73 spec5及阶段II完整量词。仅编辑本assigned文件；不Git／spawn／metadata。以下为既有工具在完整mixed32的source应用，不另立独立方向／ID，不宣ordinary新界或重大性。高级19.2／19.4 wholeproof仍具名；独立终审另行进行。

## 1. 完整输入、符号和参数顺序

保WZ2609.22035v1 Def17.2–17.4全部原假设，d5、k3、ell2：T的joint4-AD／whole-tube CW，原Z和两套完整grains，filled水平集，原selected incidences及ξ／Φ coherence均不改。固定0<κ≤1、0<γ≤1、κ+γ>1及µ∈(0,1/4)，η最后小、δ最后小。scalar Φ_p为κ-AD；native tildeY_z⊂R²为AD(2−κ)，另有physical tube-KT(1−γ)。二者指数不能互换。

写a=f1∈R，b=f2∈R²，c=tildef1∈R²，d=tildef2∈R²，原一致性为b_t=c_t+d_ta_t。a、b、c、d均在固定有界盒，记其固定界M。只有原f的dyadic Lip与原source条件，不加AFF／NQ／rational／smooth／goodrank或a、d spread。定义

    E(t,s)=b_t−c_s−d_s a_t，D(t,s)=(s−t)E(t,s)。       (1)

任取指定原allowed ρ∈[δ^(1/4),δ^µ]。先固定0<β<B<1及0<b*<B−β，例如B=3β、b*=β、β<1/6；置r0=ρ^(3+B)。再选v>0足小于µ、β、b*、κ、γ及上述正gap，最后取η≪v和δ小。下面所有C只依固定source维数／M和所列固定参数；final K=δ^−Cη不包含v。反设坏窗证明中的K_bad可含v，但最终不保留那一反设配置。

## 2. 原heavy窗和时间分母

原#Z≥δ^(η−1)，每个ρ窗J中m_J≤Cρ/δ。取a0=C0η、C0固定足大，先删除m_J<cδ^a0ρ/δ的整light窗。因窗数≤C/ρ，总删除≤Cδ^(a0−η)|Z|，δ小后小于|Z|/10。其余heavy窗满足

    cδ^a0ρ/δ≤m_J≤Cρ/δ，ν_J=Uniform(Z∩J)，
    ν_J(I)≤Cδ^−a0(|I|/ρ+δ/ρ)。                    (2)

所有量均对原未删shading／原points计。此阶段不把相对某q的time密度冒原whole-window密度。后文whole-time restriction只删完整层，依R22已付闭包：T不改，每层X／Y／tildeY／Φ与witness不改；跨time Y-union lower由一整层AD供给，upper由原union继承。新参数可取η_S=M0η≥Cη+a_S的整数倍，η_S≤C′(η+a_S)，新allowed格是旧格子格。

## 3. 原19.4排近d的共同left fan

先记一个原局部结论。若某heavy J中A⊂Z∩J、|A|≥δ^(4v)m_J，且whole tildef=(c,d)在A上diam≤ρ^(1+β/2)，以任意实际s0∈A作anchor，原ρ窗即J。原Lemma19.4适用：ρ≥δ^(1/3)、ρ²≤ρ^(1+β/2)≤ρ，分母是原m_J，得到

    C_CW(T)≥δ^[C(η+4v)/γ]ρ^(−βκ/2)。             (3)

选v≪µβκγ/C、η后小，(3)与原CW≤δ^−η矛盾。因此这样的A不存在。这里只对原配置调用local19.4；无需把A重命名为一个global配置，也没有先假d非集中。

现在反设某heavy J有p=ν_J²{|D|≤r0}≥δ^v。取q=δ^(4v)，先删|t−s|<qρ。由(2)，其原ν_J²质量≤Cδ^−a0(q+δ/ρ)=o(δ^v)；这里η最后小且v固定小。剩有向H⊂Z_J²质量≥p/2，每条边满足

    |E(t,s)|≤ε:=r0/(qρ)=δ^(−4v)ρ^(2+B)。           (4)

固定H(t,s1)=1，令A(t,s1)为同一left t的H-neighbors中|d_s−d_s1|≤ρ^(1+β)者。由原(1)，

    c_s−c_s1=−(d_s−d_s1)a_t+E(t,s1)−E(t,s)。

故whole(c_s,d_s)距实际anchor(c_s1,d_s1)至多C_M[ρ^(1+β)+ε]。v先足小使ε≪ρ^(1+β)，δ后小再将固定C_M吸收到ρ^(1+β/2)。第3节的local结论给

    ν_J(A(t,s1))<δ^(4v)。                          (5)

这付的是同一H、同一left t上的条件集合，不是对d的独立边际另加Frostman假设。

## 4. 两个分离anchors恢复whole f

same-left fan的原质量为∫(∫1_H(t,s)dν_J(s))²dν_J(t)≥p²/4。近d部分由(5)至多δ^(4v)，故分离fan仍有≥cp²质量。Fubini可固定一对实际s1,s2，|d_s1−d_s2|>ρ^(1+β)，使共同left集合

    S_J={t:H(t,s1)=H(t,s2)=1}

满足|S_J|≥c p²m_J≥cδ^(2v)m_J。它保持原t，不重设time reference。两个向量方程相减给

    (d_s2−d_s1)a_t=c_s1−c_s2+O(ε)。

scalar未知量a_t只需除非零向量d_s2−d_s1的长度，不要求二维determinant。因此任意t,t′∈S_J有

    |a_t−a_t′|≤Cε/ρ^(1+β)，
    |b_t−b_t′|≤C_Mε/ρ^(1+β)。

选4v/µ<B−β−b*且预留固定margin后，

    diam f(S_J)≤C_Mδ^(−4v)ρ^(1+B−β)
                 ≤(1/10)ρ^(1+b*)。                  (6)

恢复的是全部(a,b)，不是单一a投影；近d支恢复的也是全部(c,d)。这正是一般vector×matrix版本不能自动使用、而当前scalar a结构可付的地方。

## 5. 坏窗并、原质量与newallowed父格

称满足p≥δ^v的原heavy J为bad。若这些bad窗在原Z的总质量≥δ^v|Z|，按第4节对每个bad J选一个S_J，令S=∪S_J。则

    |S|≥cδ^(2v)∑bad m_J≥cδ^(3v)|Z|≥δ^(4v)|Z|。    (7)

S只删整time层。R22闭包给同T、同κ／γ的合法配置，η_S可取整数倍η且η_S≤C(η+v)。各J的f中心可以不同；以下不声整个S或合并父窗diam小。

取新allowed上邻R≥ρ，ρ≤R≤δ^−η_Sρ。用原共同nested dyadic time-grid，原ρ窗J是该R窗的子窗；本选择只在新格调用19.2，不把旧ρ误称新格。对每z0∈S_J，其新R父窗包含同一整个S_J。heavy lower与(7)的逐窗版本给

    |S_J|≥cδ^(2v+a0)ρ/δ，
    |S∩parent_R(z0)|≤CR/δ。

因而对**每个**保留anchor z0，(6)供给nearconstant fraction至少cδ^(2v+a0+η_S)。不同R窗可以有不同常值，也不需同R内其它old子窗共享它。原源采用dyadic rounding的约定下，在共同nested格选择此父窗；allowed取整的比值已完整付δ^−η_S，不能跨不同fit常数免费合并。

令σ_f=ρ^(1+b*)。参数最后小满足2η_S<µ(1−b*)，则

    R²≤δ^(−2η_S)ρ²≤σ_f≤ρ≤R，R≥δ^(1/3)。          (8)

因此new配置满足19.2的每anchor、同一R／σ_f及原新分母条件，ε_den≤C(η+v)。不是一个好窗代替global19.2。

## 6. global19.2矛盾与原raw零球结论

对S配置应用named19.2，原T没有更换，仍可用原CW upperδ^−η，而lower为

    C_CW(T)≥δ^[C(η+v)/γ](R/σ_f)^κ
             ≥δ^[C(η+v)/γ]ρ^(−b*κ)。             (9)

ρ≤δ^µ、v≪µb*κγ/C后η再小，使(9)大于δ^−η，矛盾。由此bad heavy窗的原总time量<δ^v|Z|。删去这些整窗与第2节light窗后，保留至少原Z一半；每个余heavy J保持原Z_J及全部原points／marks，且

    ν_J²{|(s−t)E(t,s)|≤ρ^(3+B)}<δ^v。             (10)

这不是conditional q-law、angle law或归一化Y-law上的结论，正是后文所用原uniform time-pair upper。反设S含δ^(4v)损失只存在于证明(9)时；(10)的最终配置仅删总time小量与原source-light窗，计数仍用原J内数据，故final K只含固定倍原η，不含v。source损失依赖v选小不等于把v放入final K。

## 7. 真same-tube平方质量及原pair上界

固定任一余heavy J，m=m_J，保其全空间E_J。由原grains、scalar point Φ供应及joint4-AD，记D0=δ^−κ，可用原source K=δ^−Cη写

    P=#E_J≤K mδ^(−4+κ)，I≥K^−1mδ^−4，
    #used T≤Kδ^−4，deg(p)≤KD0。

需要时以I/(4P)、I/(4#used T)作point／tube peeling，只损≤I/2。每active tube有≥K^−Cm个实际selected visits；没有对每原tube先假独立nearfull。令n_T为这些访问的计数，保原label及固定time有限交点重数，则

    #C_same=∑T n_T²≥I_core²/#used T≥K^−Cδ^−4m²。   (11)

每项真正是同一原T的有序两个访问，不是独立arms拼接。固定(t,s)时，root points至多Kδ^(−4+κ)，每点最多KD0管；固定T在s层只有固定／K个δ-separated原points，故该pair fibre≤Kδ^−4。用(10)先删raw small-D tuples，损失≤Kδ^−4m²δ^v，η≪v后小于(11)一半。这一步在任何Y-cover或φ分桶之前完成，不乘输出桶数，也不假time与angle独立。

point删后Φ lower不免费保留；最终只使用原Φ upper与(11)。原T的AD／CW分母不变，core不被宣成新完整配置。

## 8. 原native基线与没有coarse L误差的响应

写物理root p=(x,w,tilde y+c_t x+d_t w,t)。同一原selected T在p的斜率为

    θ(T)=(φ,ξ1,p+a_tφ,ξ2,p+b_tφ)+O(δ)。

沿同一T到原selected endpoint p_s，h=s−t，完整native标签恒等式是

    tilde y_s=tilde y+(c_t−c_s)x+(d_t−d_s)w
                  +h(ξ2,p−d_sξ1,p)+D(t,s)φ+O(δ)。     (12)

全部baseline均保原p、s及ξ，既不删初始水平项，也不让不同roots共享一个假坐标系。给定(p,t,s)后它才是固定向量。原c_s、d_s及ξ有固定界，物理endpoint与方向O(δ)误差仍只放大固定倍δ。

此处没有构造coarse native L图，没有把fine φ换ρproxy，因此没有Kρ³或Kτρ误差。终点确是原访问点而非只轴线穿过某个拟造carrier；其native标签真在原tildeY_s。φ2在此不存在，scalarφ的原label重数仍须按point方向碰撞控制，而不是一角假定一管。

## 9. fineδ tube-KT乘scalar Φ cap的真实幂

固定(p,t,s)，置ℓ=|D(t,s)|。在删选后ℓ≥r0≫δ；另一方面原f在J的Lip及b=c+da给E=Δb−d_sΔa，故ℓ≤Kρ²<1，η后小。φ有界，(12)的可变输出在长Cℓ、宽Cδ的真实line tube中。

原physical tildeY tube-KT给至多K(ℓ/δ)^(1−γ)个细Y-cells。每个cell反推φ区间长≤Cδ/ℓ，位于原Φ的δ-base之上；scalar κ-AD upper给每个此区间的原角数≤K D0(δ/ℓ)^κ。一个细φ-cell在固定p附近只对应固定数原δ-tubes：其normal斜率由原ξ+fφ确定到O(δ)，joint δ-separated tube参数在相应小盒中只有限packing。所有O(δ)误差用固定倍细管及相邻cells吸收。故可能的原selected incidences满足

    N(p,t,s)≤K D0(δ/ℓ)^(κ+γ−1)
                 ≤K D0(δ/r0)^(κ+γ−1)。           (13)

这不是将二维tildeY投影成scalar；只查询它在一条实际细管内的absolute cover。也未以原slab γ代替scalar Φ的κ cap。若原tube-KT约定只写某固定宽度，固定着色／邻接扩张给同幂Cδ查询，不需要授加粗管新的PW。

## 10. 完整source子范围矛盾及κ=1

对所有root p及s求和，P≤K mδ^(−4+κ)、D0=δ^−κ，(13)给

    #C_large≤Kδ^−4m²(δ/r0)^(κ+γ−1)。              (14)

而第7节保#C_large≥K^−Cδ^−4m²。原ρ≥δ^(1/4)、B<1给

    δ/r0=δρ^(−3−B)≤δ^[(1−B)/4]。

固定κ+γ−1>0，先选β／B／b*和v，再η足小，(14)的固定δ正幂与lower矛盾。于是具名19.2／19.4及全部原输入下，完整mixed32 source的κ+γ>1子范围不存在。特别κ=1、任意固定γ>0包含在内。没有AFF／quadratic／NQ／rational／smooth／goodrank假设，没有用coarse Lworking宽度替换fineδ。

当κ+γ≤1时，(13)没有正saving；本稿不声排掉该范围、完整mixed32、其它matrix／mixed、ordinary初始化或一般Kakeya。原µ／κ／γ先固定，η可依它们及正gap；不声uniform到κ+γ=1端点。

## 11. 合法闭包、独立反攻与没有证明的加强

近d支必须在同H的共同left t上利用E方程控制c；只给d边际非集中并不足。远d支给共同t集合上的whole(a,b)，不是不同子集上的两个坐标。19.4直接用原local分母；19.2只在S全局并和newallowed父格准备后调用。各old窗中心可变，父窗合并不授whole diam小。

平均／逐管分开：整time限制保每个保留层原points、grains和selected witnesses，重计总incidence；它一般不保每一原T先前的逐管原time密度。第7节通过原平方CS或明确core支付active tubes的访问数。原逐管shading若另缩必须重算，本稿不将(10)自动赠给任意angle条件law。raw小D删选靠原fixedpair fibre支配，后续只用原Φ upper，因此未发生独立化。

本证明不排任意vector×matrix raw kernel；scalar a及vector d的形状关键。没有从单个孤立窗口取得global configuration，也没有把finite law反例升级fullsource反例。raw零球结论不等于整Dlaw二维Frostman、球以外offset cap、κ维global末角carrier或商AD lower。

## 12. 旧机制范围、依赖与审查状态

阶段I已核：R21–23没有记录此无AFF／NQ完整source子范围结论；但其有限代数为R70转置应用，若先调用R22 AFF及旧quadratic／NQ准备，也可能得到类似零球后果。因此这是旧工具的source用途补全，不另立新数学ID、普遍新gain、优先权或major。原19.2、19.4的高级wholeproof及Def17模型作为具名输入，R22整层闭包按其已独审范围调用；本稿没有重证全部文献。

当前完整链已给出rawzero→全局删窗→同管平方质量→fineδ KT实际用途，等待root／B逐步独审。局部数字／scalar临界例不能反(14)在κ+γ>1的正gap；反过来本子范围也不处理κ+γ≤1。未经外部同行评审，长期Goal保持active。没有预认证后续metadata、registry或Git同步。
