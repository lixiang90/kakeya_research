# R0073：mixed32原零球质量及fine单管计数的独立审计

2026-10-18，B。数学前已实际全文读R73 spec5的锁题段及阶段I审计，重读原Def17.2–17.4、19.2/19.4 statement、R66/70原质量接口。只编辑本文件，不Git、spawn、metadata。下述是已有具名工具在另一完整source中的用途补全；不立新ID、不认证新颖/major，不将有限代数或参数子范围称为ordinary高维新界。未经外部同行评审。

## 1. 完整source、参数及两套Y不能混淆

保全部WZ d5、k3、ell2配置：原T joint4-AD及CW≤delta^−eta；原nearfull fine time Z、两套filled grains、point xi/Phi与跨尺度coherence；f=(a;b)、tildef=(c,d)，a scalar、b/c/d为vector2，原兼容式 b=c+da。所有 entries bounded M，以下可取max-entry或固定等价Euclidean norm。

ell横向Y_z⊂R3是AD(3−kappa)、水平X维1充分填充；native横向tildeY_z⊂R2是AD(2−kappa)、水平tildeX维2充分填充且tube-KT指数1−gamma。Phi_p⊂R为kappa-AD，故0<kappa≤1。固定gamma∈(0,1]及Delta=kappa+gamma−1>0，不假AFF/quadratic/NQ、smooth/rational、a/d非集中或goodrank。各固定参数后eta最后小、delta最后。

指定原allowed rho∈[delta^(1/4),delta^mu]，0<mu<1/4。取0<beta<B<1、0<b_*<B−beta，例如 B=3beta、b_*=beta、beta足小。定义

    E(t,s)=b_t−c_s−d_s a_t， D(t,s)=(s−t)E(t,s)，
    r0=rho^(3+B)， h=rho^(1+beta)， sigma_f=rho^(1+b_*)。

本轮使用原fine单管：其误差O(delta)，不先取coarse native L图，不需要R68的large-tau结论。natural rho³代理误差不能在r0下免费工作，故这一选择是实际用途所必需。

## 2. local19.4只给whole tildef cap，不先假d spread

设u>0固定足小依mu,beta,kappa,gamma。若某原rho窗J的时刻在任一宽C_M h的(c,d)球内有≥delta^u rho/delta个，则取其中实际s0为anchor，扩大固定倍后全部tildef靠tildef(s0)。原#(Z∩J)≤C rho/delta给原relative比例≥c delta^u。取sigma=C'_M h∈[rho²,rho]（delta小后成立），具名19.4给

    CW(T)≥c delta^[C(eta+u)/gamma] rho^(−beta kappa)。        (1)

先取u使C u/gamma<mu beta kappa/4，再取eta小，(1)违原CW。因此所有这些球都有absolute time upper C delta^u rho/delta。任意球中心可用实际落点加倍半径替换；不用一个不存在的anchor。

这是whole(c,d) cap，并不授任意d-ball cap。后面只在真正共有一个left邻点的两条有向边上，才能由d近推whole tildef近；正是本轮必须补的条件。

## 3. 原heavy窗、删近对角与四边reference

取a1=C0 eta，C0固定足大。删m_J=#(Z∩J)<delta^a1 rho/delta的整窗；至多C/rho窗，所删time数≤C delta^a1/delta≤C delta^(a1−eta)|Z|。delta小后保原Z固定比例。若需保原incidence固定比例，C0还可大于原每层upper/lower的有限eta系数；不把witness参数v加入a1。

对余heavy J，nu=Uniform(Z∩J)满足

    nu(I)≤C delta^−a1 (|I|/rho+delta/rho)，
    nu{||(c,d)−H||≤C_M h}≤C delta^(u−a1)。                  (2)

称J为bad，若 nu²{|D|≤r0}≥p=delta^v。v先取足小于u，后取eta小使a1≪v。令q=delta^(4v)，删|t−s|<q rho；其raw质量≤C delta^−a1(q+delta/rho)=o(p)，因为delta/rho≤rho³≤delta^(3mu)，并取v≪mu。余有向edge indicator g0质量≥p/2，且其每条边满足

    |t−s|≥q rho， |E(t,s)|≤epsilon0:=r0/(q rho)。           (3)

对原nu两边各作一次CS，完整有向K2,2质量

    int g0(t0,s1)g0(t0,s2)g0(t,s1)g0(t,s2) dnu^4 ≥c p⁴。 (4)

四变量均保原times，不使用反向edge，不先独立化任何actual g。raw图不含输入normal labels，所以(3)没有随t变化的四输出主项。

## 4. 共同left使近d对真正落whole tildef近对

在(4)的支持上，同一left t0的两式给

    c_s1−c_s2=−(d_s1−d_s2)a_t0+O(epsilon0)。

若|d_s1−d_s2|≤h，则whole tildef=(c,d)两点距≤C_M(h+epsilon0)≤C'_M h；最后用epsilon0/h=delta^−4v rho^(1+B−beta)=o(1)。因此bad d-pairs的**四边质量**可由(2) upper为C delta^(u−a1)。取u−a1>5v，即o(p⁴)，仍有≥c p⁴的四边质量且|d_s1−d_s2|>h。

这不声raw全部d-pairs非集中，也不对g0(t0,·)归一后免费给cap。对fixed right pair写共同left集合T(s1,s2)及其质量z，四边贡献正是z²。Fubini给实际s1,s2，|d_s1−d_s2|>h、共同left T_J质量≥c p²。对每t∈T_J，均有(3)两式。

相减恢复scalar a_t：

    (d_s2−d_s1)a_t=c_s1−c_s2+O(epsilon0)。

沿这个非零vector取内积，a_t落O(epsilon0/h)的一个常数中心；代入任一边恢复b_t。所以**整个**原f=(a;b)在T_J上diam≤C_M epsilon0/h，而非仅投影或a小簇。选

    4v<mu(B−beta−b_*)/2

后，可使diam f(T_J)≤sigma_f/10；保#T_J≥c delta^(2v)m_J。这一步没有要求d为scalar，也没有goodrank公设。

## 5. global坏窗见证并、每anchor与newallowed格

反设bad窗总质量sum_bad m_J≥delta^v |Z|。并实际见证W=union T_J，则#W≥c delta^(3v)|Z|。只删整time层，T及CW分母不动，所有保留层的两grain、Y、xi/Phi不动；R22 whole-time closure给新参数eta_W=C(eta+v)，取原eta的足大整数倍使newallowed嵌入原格。这里允许eta_W含v，因为只用于反设矛盾，不是最后实际图常数。

rho未必newallowed，取dyadic newallowed上邻R∈[rho,C delta^−eta_W rho]。对每z0∈T_J，只用同一个旧J中的T_J；其f值距f(z0)≤sigma_f，且J含于该R-parent。原δ时间packing给#(W∩R)≤C R/delta，而

    #T_J≥c delta^(2v+a1) rho/delta。

所以new configuration的每个anchor均有relative cluster≥c delta^(a1+2v+eta_W)。不同旧窗的中心可以不同，没有将它们合并。取eta_W≪mu(1−b_*)，则R²≤sigma_f≤R、R≥rho≥delta^(1/3)，eta_W<gamma；具名19.2真实every-anchor量词成立，推出

    CW(T)≥c delta^[C(eta+a1+v)/gamma] rho^(−b_* kappa)。    (5)

先令v足小依mu b_* kappa gamma，最后eta小使(5)违原CW。故bad总time质量<delta^v |Z|。再删bad整窗得到Z'≥|Z|/2；每余heavy J保持原nu和raw零球cap≤delta^v。final source与每层计数常数只需delta^−C eta（含a1=C0eta），**不含v**。未保原Z的每管原平均density时，也可直接以原完整层/point供应重计下一节；不免费沿用旧图。

## 6. 原same-T平方lower与fixedpair upper

选择一个余heavy原J，m=m_J。保该窗内全部空间，原point数量每层≈_K delta^(−4+kappa)，两套表示给相同指数，point witness数量≈_K D0=delta^−kappa。每fine Phi-cell选一个Def17供应的实际tube witness，单管/角碰撞固定倍；不授新tube子族AD lower。于是

    I=sum_T n_T≈_K m delta^−4， #used T≤K delta^−4。

后式仅用原T在固定bounded joint chart中的AD upper；unused T及CW原分母不变。对同一个T的原selected visits取ordered pairs，或先tube低度剪裁再计，得到

    C_pair=sum_T n_T²≥I²/#used T≥K^−C delta^−4 m²。          (6)

fixed(t,s)，初点p及其selected tube数至多#E_t·K D0≤K delta^−4；每一T,s最多O(1)个原δ-separated终点，故真实root-incidence pair upper≤K delta^−4。raw tiny pair cap≤delta^v因而删掉的**实际**pair tuples≤K delta^v delta^−4m²，先eta小使它比(6)小。这里没有按output cover放大bad成本，也没有声每个p条件time cap。余good pair仍保(6)的固定比例。

scalar Phi的原AD interval upper始终保留；所选管/marks被限制后不另授κ-AD lower。core或整label限制的逐管访问lower与全平均I各自计算，绝对clock不变。

## 7. native fine响应的baseline及实际KT计数

fixed初点p@t写native horizontal坐标(x1,x2)，normal为tildey+c_t x1+d_t x2；原ell方向为

    theta(T)=(phi, xi1+a_t phi, xi2+b_t phi)+O(delta)。

同一T到原selected终点@s的native normal标签满足

    tildey_s = C(p,t,s)+D(t,s)phi+O(delta)，
    C=tildey+(c_t−c_s)x1+(d_t−d_s)x2+(s−t)(xi2−d_s xi1)。  (7)

不能把最后一项换成xi2−d_t xi1，也不能当C对p或s相同。fixed(p,t,s)时它才是固定baseline，所以不需要先冻结任何normal labels。式(7)是原fine数据，误差O(delta)，没有rho³ coarse代理误差。

在good pair |D|≥r0，输出随scalar phi沿长O(|D|)线段；原tildeY_s tube-KT给≤K(|D|/delta)^(1−gamma)个细output cells。每cell反推phi落长O(delta/|D|)区间，scalar Phi_p的κ-AD upper给≤K D0(delta/|D|)^kappa个角/实际管。保相邻格和fixed fine碰撞，得

    #actual T visits at fixed(p,t,s)
       ≤K^C D0 (delta/|D|)^(kappa+gamma−1)。                (8)

|D|≤C rho²<1，r0≫delta，故KT管宽度、长度、角interval的查询均在fine base以上。O(delta)方向/点误差用固定Cdelta管和相邻δ-cells支付，δ-separated normal labels只给固定细格重数。point Phi本身一维，使用的指数是κ而不是另加的gamma；不要求coarse unused角law或time-angle独立。

## 8. 完成指定参数子范围及原scale用途

记Delta=kappa+gamma−1>0。对good(t,s)求和(8)，用每层#E_t≤K delta^(−4+kappa)，给

    C_good≤K^C delta^−4 m²(delta/r0)^Delta。

原rho≥delta^(1/4)使delta≤rho⁴，故

    delta/r0≤rho^(1−B)≤delta^[mu(1−B)]。

与(6)保留后的lower相比，只要eta最后小依固定Delta、v等参数，矛盾。没有从δ到coarse重新reset，也不用tau归一化/同time sampler/13.5、AFF/quadratic/nonquad或R68。指定哪个原allowed rho均可按上述预算重新选择保留time子集；不要求不同rho的Z'求交。

因此在全部原source及具名19.2/19.4、whole-time closure下，完整mixed32在kappa+gamma>1子范围不存在；特别κ=1时任意固定gamma>0适用。这个critical κ=1用途是该source中的限定应用，不是ordinary Kakeya的critical endpoint，也不代表完整mixed32或其它分支已解。

## 9. 独立反攻、旧工具重用及尚余边界

已逐项攻击以下潜在假步：free d-spread被共同left四边和whole tildef cap替代；whole f的local簇不能直接用19.2，而用global见证并及每anchor旧窗；newallowed parent中心不合并；v只在反设eta_W出现，final K不含v；rawtime cap经fixedpair root upper才转实际图；原sameT平方计数不拼独立arms；baseline保xi2−d_sxi1；fineδ测试不挪coarse rho³误差；Y的ell/native维数及Phi的κ/gamma角色分清。

有限恢复与R70左右交换转置同型，是可重用代数工具，不另立新结构ID。新付的是不同source的完整global/local分母和fine单管最终用途。若κ+gamma≤1，(8)不给positive saving；这只是当前证书不足，不是actual图lower或完整source反例。不能继续调r0、beta、gamma或换更多固定times冒全分支进展。

本稿没有构造toy来反fullsource，也没有wholeAFF、一般κ排除或ordinary n5界。19.2/19.4等高级wholeproof继续具名；独审须由root/A实际逐式进行，B自证不算独立审查。平均/逐管删选及未来归档/Git按真实执行另记，未经外部同行评审。
