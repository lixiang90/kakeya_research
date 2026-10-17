# R0044：实际端点palette、整管分配及polynomial-envelope停止

2026-10-17，root。目标是检验R43下一任务，而非给旧CW换名称。完整d=5,k=ell=3 source及有界uniform whole-T PW下，下面确实构造了来自原grain的共同测试，保原管质量；natural e≈ρ²和更细e的最便宜可验证施工均只回原CW。因而本轮停止polynomial-envelope参数迭代，没有证明κ≤ζ、五维Kakeya或重大中间结果。两全文独审和root集成另存research/reviews；未经外部同行评审。

## 1. 量词、源输入和排重

固定ζ,γ>0，随后η足够小、δ足够小；κ≥ζ的实际Def17.2–17.4配置如存在，取source允许ρ∈[δ^(1/4),δ^µ]。记b=2−κ∈[0,2]，K=δ^(−Cη)，固定次幂损失写K^C。原tube法则ν是有界joint chart内uniform counting，总N≈_Kδ^(−4)，wholeclock固定[−1,1]；PW为对每个共同semialgebraic S及λ>0，

    ν{T:q_T(S)≥λ}≤C0 P(E)|S| λ^(−5),
    P(E)≤C(1+E)^A，C0≤δ^(−Cη)。                 (1)

q_T按原whole tube体积归一。R43已付coarse/wholeparent的实际费用，但(1)不为任意原Def17.1无界类免费补公设。原CW仍可用。所有新事件均为原indices子集，不把tuple/point prior改成ν，不重归一，不要求restriction后重新全AD。

本轮独立反攻包括：dyadic边界不准当EuclidLip；原跨time Y-union只在baseρ正则不准当e≪ρ公共palette；one-index assignment会丢时间密度；shortclock、degree和whole-J range费用；per-index h不准当同一测试。R43/本spec要求一轮无新saving即停。源Lemma20.2本已适用一般matrix affine拟合；R40 fine-flatflake及旧CP⇔PM/W/BSG/action/carry均不解冻。

## 2. 实际good-q及原管质量：不假任意q dense

用R16_original_tuple_audit §§1–3（各p/Φδ-bin只留原见证，固定T,z最多O(1)点）。先按实际times选admissible时间interval J，|J|=ρ，使n=#(Z∩J)≥K^(−C)ρ/δ；以J内部的原关联按空间ρ-cubes平均选q。J与q的time-projection用同一dyadicρ-parent。记d_T为q内所选原关联数，I=Σ_T d_T，T_q={d_T>0}。已证：

    I≥K^(−C)ρ^(5−κ)δ^(−5),
    #T_q≤K^Cρ^(4−κ)δ^(−4),
    d_T≤Cρ/δ.                                     (2)

后式是δ-separated times及sameT,z的O(1)重数；不需要逐管dense假设。I/max d_T又给#T_q的匹配lower。若J与q边界采用固定邻接/更大dyadic ancestor，固定损失吸入K；不能跨无共同admissible parent的f跳跃。

取阈值d0=I/(2#T_q)，heavy族H={d_T≥d0}保至少I/2。由(2)，

    d_T≥K^(−C)ρ/δ (T∈H),
    #H≥K^(−C)ρ^(4−κ)δ^(−4).                       (3)

在J至多Cρ/δ个实际δ-time上平均H的原关联；每time、每T重数O(1)，故存在一个实际z*∈Z∩J及事件

    H*={T∈H:T在q∩E_(z*)有一个原使用的见证},
    p*=ν(H*)≥K^(−C)ρ^(4−κ).                        (4)

同时p*≤K^Cρ^(4−κ)。每T保留旧d_T，筛z*只是whole-index选择而非把原markedtime改成δ^-1copies。以后甚至只用其实际endpoint和整条直线，不需要再宣H*新AD或原shading逐管dense。

## 3. 共同affine gauge及单个真实Y_(z*)

对每T∈H*选q内原endpoint p_T=(x_T^p,y_T+f(z*)x_T^p,z*)，y_T∈Y_(z*)；axis在该p的Oδ内。选一个T0∈H*为共同reference，令u_T(t)=x_T^axis(t)−x_0^axis(t)，v_T(t)=y_T^axis(t)−y_0^axis(t)，F=f(z*)。u,v都是affine，whole slopes bounded，故在J上|u|≤Cρ。

源Def17.2(4)在同q给|ξ_(p_T)−ξ_(p_0)|≤Cρ。写actual axis slopes为θ_T=(θ_T^x,θ_T^y)，由原见证关系，

    η_T=(θ_T^y−θ_0^y)−F(θ_T^x−θ_0^x)
        =ξ_(p_T)−ξ_(p_0)+Oδ， |η_T|≤Cρ。
    h_T*=v_T(z*)−F u_T(z*),
    v_T(t)−F u_T(t)=h_T*+(t−z*)η_T。             (5)

(5)是原直线上的精确恒等式（h*与η取actual axis值）；ξ关系只用于界，误差不在每time累加。h_T*=y_T−c_ref+Oδ，c_ref=y_0^axis(z*)−F x_0^axis(z*)。这些y_T都在同一个Y_(z*)的Oρ ball内。其原(δ,b,K)-AD upper及lower packing在δ≤e≤ρ给

    N_e({h_T*})≤K^C(ρ/e)^b。                       (6)

可以用原Y的maximal e-separated centers及每点e-ball的lower，所有balls放入enlarged Oρ window再用upper；window边缘不用截断lower。实际labels近δ重数可吸K，constant-neighbor扩张只多固定因子。这里完全没有使用所有z的Y_z在fine e尺度共同cover。

## 4. natural scale：degree0的整短clock包络

若Cρ²≤e≤cρ，按(6)把每T的h_T*指派一个固定e-bin中心c_j。设

    S_j={t∈J, |u|_∞≤Cρ,
               |v−F u−c_j|_∞≤Ce},                 (7)

再按共同reference affine map回原physical coordinates。由(5)，每个T∈H_j在整个原J的δ-thick段都包含于S_j，只要e≥Cδ（已由ρ≥δ^(1/4)保证）。故q_T(S_j)≥cρ，是明确的整管几何，强于单靠旧marks的lower；J仍是原clock子interval，没有重归一。

这些共同tests均由O(1)个linear inequalities给出，E=O(1)，|S_j|≤Cρ³e²；H_j是原H*的partition，Σν(H_j)=p*。PW restricted mean或直接q≥cρ给

    p*ρ^5≤C C0 Σ_j|S_j|
           ≤K^C C0 ρ^(5−κ)e^κ,
    ρ^4≤K^C C0 e^κ。                              (8)

在e≈ρ²，(8)只限制κ≤2加O(η/µ)损失；b=2−κ≥0早已给κ≤2。对于固定0<ζ≤κ<2没有新矛盾。更大的e更弱。实际能施工，但它是常矩阵、短clock的旧flat测试；Bernstein、多项式degree或C²在这里根本不需要。

## 5. fine scale：真实affine h标签及恰好支付的normal slope

对Cδ≤e≤Cρ²，仍用F常矩阵。把h_T*以e分桶，并把η_T∈B_Cρ⊂R²以e/ρ分桶，后者最多

    L_v≤C(1+ρ²/e)^2。                              (9)

每T只指派一个joint bin j=(c_j,β_j)，共同h_j(t)=c_j+(t−z*)β_j。以v−F u−h_j(t)替换(7)残差，整J的δ-tube仍覆盖、q≥cρ、体积仍Cρ³e²、presentation仍常复杂度；没有per-tube测试。label数

    N≤K^C(ρ/e)^(2−κ)(1+ρ²/e)^2。

于是实际PW预算统一为

    ρ^4≤K^C C0 e^κ(1+ρ²/e)^2。                    (10)

e≤ρ²时(10)简化为1≤K^C C0 e^(κ−2)，对0≤κ≤2恒无新限制。这是joint palette的合法上界；不声称所有实际配置都达到product上界。要得到strictgain，需要额外source估计严格减少这个joint endpoint/normal-slope palette并保(4)，本轮没有该估计，不能先假设它再宣证明。

**双向/旧输入排重：**这些S_j皆固定affine3-plane短planks。若T∈H_j，在whole原clock上|(v−F u)−h_j(t)|≤C e/ρ且|u|≤C（(5)的slope近似延长，δ≤e/ρ）。故整T在凸box U_j内，三条长轴O1，两条短轴Ce/ρ，|U_j|≤C(e/ρ)²。原CW直接给p_j≤K^C(e/ρ)²，与PW对(7)的λ≈ρ及|S_j|≈ρ³e²所得上界相同。两者对这一族tests只有常数/既有K损失差。自然及fine affine施工没有添加新的正幂约束，不登记新ID。

## 6. 真正非affine P：合法近似不等于共同包络

A稿给可验证工具：全局按dyadic边界删小time-mass，先于重选goodq；保原ν×time markedmass后，在留times上EuclidLip常数δ^(−Cη)，可bounded延拓并用Bernstein近似，D≥C(K_Lip|J|/ε_f)^2，导数和sup均有真实界。本稿不需要为(7)调用它。仅在留times近似P≈f、乘|u|≤Cρ，把误差控制在e，**不推出**同tube offsets在一个公共e-bin内。

若仍用constant-offset pieces，B稿证明沿实际axis y−P(t)x的degree≤D+1，在whole-J每坐标range R及offset-thickness≤Ce时，每tube访问至多C min((D+2)(1+R/e),(1+R/e)^2)个格。按访问全用会把A_tot=Σν(H_j)变为原tube-piece重数；强制每index只分总权1又可能损失真实visit mass。不同moving h_j还要另外计其自由参数/degree。把clock切短需付q^(−4)原incidence费用或q^(−5)未乘time的tail费用；不能删。

完整的一般有限预算为

    M=Σ∫θ_j(T)q_T(S_j)dν,
    a_j=∫θ_jdν, A_tot=Σa_j,
    M^5≤(5/4)^5 C0 [ΣP(E_j)|S_j|] A_tot^4。        (11)

只要θ_jν≤ν，相关events及fractional权均可；但A_tot≤1和M lower须各自实证。B的真实parallel jointAD4/CW/PW例中，Σθ_j≤1强制保留访问≤3e，严格否定免费one-piece质量；它κ0且不保全positiveγ source，只是接口反例。

还能完整施工一个真正nonaffine证书：每entry延拓进一步clamp到J∩Z_good的原f最小/最大值，不改变留times值、不增加K_Lip；Bernstein是这些值的凸平均，所以whole-J有|P−F|≤Cρ。精确公式

    H_T^P(t)=h_T*+(t−z*)η_T+(F−P(t))u_T(t)

给全部原J的offset在h_T*的Cρ²-neighborhood内，不只在稀疏marks近似。先给每T唯一coarseρ² anchor bin，再在其扩大ρ²窗口取e-grid constant-offset pieces（Cδ≤e≤ρ²），只对实际访问的piece计H_(c,j)。保持真实overlap≤C，M≥cp*ρ；B访问上界给A_tot≤p*L，其中

    L≤C min((D+2)(1+ρ²/e),(1+ρ²/e)^2)。
    N≤K^C(ρ/ρ²)^b(ρ²/e)^2=K^Cρ^(2+κ)e^(−2),
    Σ|S_j|≤K^Cρ^(5+κ)，E_j≤C(D+1)。

每tube截面在固定time的offset厚度≤(1+||P||)δ≤Ce，足够使用访问bound；这里从整轴段构造覆盖，不用漏掉δ|h_j′|的接点ball论证。将这些真实数代入(11)得到

    ρ^(4−2κ)≤K^C C0(D+1)^A L^4。                   (12)

κ≤2时仍平凡，degree/重数只增右边。该actual nonaffine证书同样失败；它使用的N,L是所选施工的upper，绝不是所有共同包络必须有这么多pieces的lower。本轮未施工出比(10)/(12)更优的degree/label/mass组合，也不以该校准证明所有非affine策略不可能。

## 7. 本轮结论及停止

真正得到的是：原goodq→heavy→共同实际endpoint的质量选择；单个原Y的fine palette；所有e≥Cδ的真实常matrix/affine-offset共同包络；完整whole-clock质量及PW/CW预算。natural eρ²及fine slope-grid两种均精确回CW，没有新κ约束。源dyadicLip的合法延拓和访问重数是工具，不能升格为高维进展。

按R43/R44一主轮gate，冻结本次polynomial-envelope尝试；不继续D/e/ρ/clock阈值轮，不把减少joint palette换名称当新命题。重开须独立的新source几何估计或已证明的真实palette/mass压缩（不能仅由旧全称shading结论再调用推出）。一般到sticky、其余mixed、Hausdorff及极大函数路线仍open；来源高级定理仍按既有具名层级引用。

## 8. 核验边界

本轮只做符号指数/源计数和独立全文审查，不重跑旧有限样本，不声称有限计算替连续证明。原WZ来源是literature/primary/wang_zakharov_2026_sticky.pdf，Def17.2–17.4及R16实际tuple proof；BS/PW版本沿R42，R43实际closure沿原文件。没有新增PDF或在线前沿认证；31PDF/34来源不变。仅本轮明确的预算与失败获内部审查，外部同行评审false、novelty/major false、Goal active。
