# R0079：保共同X、原clock输出与局部非拟合的联合有限反模型

2026-10-18，root阶段II整合。按working_spec §2在实际读A8/B7后先锁量词，再施工。本文只攻击列出的已提取有限接口；不构造完整Def17源或Kakeya反例。root12/A12/B12已实际全文交叉逐式核，两formal6及root整合限定通过；未经外部同行评审。

## 1. 精确命题、量词与反驳范围

固定α=3/4、β=1/4、τ=1/8、γ0=1/8，故α+β=1、α>β+τ且min(α,β)>γ0。固定ε0∈(0,1/20)、θ∈(0,ε0τ/100)，任给损失上限h>0及固定整数J。存在任意小η<h及δ→0的一列有限模型，下面全部AD/KT、clock非集中与cover常数均≤δ^-h；sourceallowed尺度为δ^(jη)。

同一个A0=B0=A、X=A−A、原time prior ν和g，满足native AD1/tubeKT、全尺度共同X cover、固定高阶small sums、全部small actions、正维实际Tu-law、精确fractional关系/cone及原allowed窗口的all-real local NF。g在bulk所有原三元组恒1，wholeclock直线亦实际实现。尽管如此，对所有u和j≤J，相关fine cover至多C_(L,J)δ^-1，且NδX≥cδ^-1；其small-action比值没有任何固定正幂增长。

这否定仅凭这些联合接口推出统一正幂增长的有限捷径。wholeT joint4-AD/CW、filled native X2、pointΦ/selectedξ及其coherence尚未构造；因此不否R78的完整源归约，也不否matrix33、ordinary或Kakeya。若需要这些缺项，必须真正使用它们。

## 2. 参数次序、实际digits与fine分离

先选择整数C*足大依ε0,θ和下文固定指数C；再选L为4C*的足大整数倍，使η=C*/L<h并预留所有δ^-h损失。L此后固定。令B=2^m，m沿8的倍数趋∞，δ=B^-L，Q=B^τ、R=B^(1−τ)，故QR=B。所有C_L、2^L及固定D、J只依先定参数，B最后足大使C_L≤B；不让L随B变化。

记D_s={Σ_(i=1)^L a_i B^-i: a_i∈{0,…,B^s−1}}。取足大固定整数D，例如D=1000；A=D(D_α×D_β)。C为相同L位数字的product carrier，第一坐标digits 0,…,3B^α，第二坐标0,…,2B^β，再乘D。B足大后各digit范围远小于B；表示唯一且所有点落Dδ网格，因此不同点距离≥Dδ。它们直径→0，最终全在所需有界box中。

## 3. 一维digit正则性与任意方向native KT

对s∈{α,β,τ,1−τ}，连续短digit或偶数短digit的均匀概率，在有限深度n≤L上满足

    μ(I)≤C_L B^C(|I|+B^-n)^s。

对其支撑点，δ_n=B^-n≤r≤1时，ball质量亦≥C_L^-1 B^-C r^s。证明直接在B^-(k+1)<r≤B^-k处固定k或k+1位prefix：prefix数/单prefix质量分别相差至多一个B的固定幂；扩大digit范围固定倍或只取偶数的费用至多C^L。区间边界至多固定个相邻prefix。此处C不依L；C_L可依L，最后才以B吸收。

故A及C的product均为(δ,1,C_LB^C)-AD，尺度D仅付固定常数，fine点数分别δ^-1与C_Lδ^-1量级。任意长ℓ、宽w的tube（δ≤w≤ℓ≤1），若其长轴较接近horizontal，投影x区间长Oℓ，固定x的y切片长Ow，概率≤C_LB^C ℓ^α w^β；另一种方向交换α/β。两者均≤C_LB^C ℓ^(1−γ0)w^γ0。用支撑点w-ball的AD1下界和w分离packing，将概率上界除以w，得

    N_w(P∩tube)≤C_LB^C(ℓ/w)^(1−γ0)，P=A或C。

tube固定倍扩张只付常数。此为任意方向估计，不仅坐标管；没有赠局部ADlower给任意small-doubling X。

## 4. 同一共同carrier与真实乘积尾项

N=E12，b∈D_τ。对a,a′∈A，a+(I+bN)a′的第二坐标digits≤2B^β。第一坐标中真实乘积b a′_2的第k位raw coefficient为DΣ_(i+j=k)q_i a′_(2,j)，k≤L时≤DL B^(τ+β)。由于α>τ+β，B足大时≤DB^α；加a_1+a′_1后仍在C的第一digit范围。

L后真实尾部绝对值≤DC_L B^(τ+β−1)δ=o(δ)，故

    A+(I+bN)A⊂N_δ C，对全部b∈D_τ同时成立。       (4)

这是真实实数乘法，不是digitwise乘法；没有删除低carry tuples，也不借R28 fulltime×angle的无进位策略。这里较小的两个digit exponents之和严格小于承载坐标的α，raw convolution的全部L项已计。

X=A−A包含A某平移，NδX≥cδ^-1；任意固定j≤J，jX及X+(I+(b−b0)N)X，乃至固定阶的这些signed和，均由digits范围固定倍扩张与同一尾项证明覆盖，Nδ≤C_(L,J)δ^-1。常数不依B；j不能随δ增长。A的AD1上界和A⊂X+const给所有w≥δ的N_wX≥C_L^-1B^-C/w。

上cover亦实际付出：N_wA≤C_LB^C/w，故一个w-ball中的F⊂A有至少C_L^-1B^-C w/δ个原标签。固定a*∈A，在X内选10w-separated最大族d_i，各簇d_i+(F−a*)均在2X且簇间相距≥c w；每簇的δ-cover至少c#F。第4节已付Nδ(2X)≤C_Lδ^-1，所以族大小≤C_LB^C/w，即N_wX≤C_LB^C/w。w靠近δ时只需调固定分离倍数/网格颜色；不是从fine card直接外推。若J=1，以上只额外用固定阶2X，允许把最初固定J替换max(J,2)。

## 5. 一个共同原time clock及真实算子law

time digits d_i=R q_i+r_i，其中q_i∈{0,…,Q−1}，r_i∈{0,2,…,R−2}。首digit额外要求Q/4≤q_1<3Q/4；其余完全乘积。令Z_b为相应L位u，位于[1/4,3/4]；Z=Z_b∪{0,1}，ν=Uniform Z。恰#Z_b=B^L/2^(L+1)，故对B足大#Z≥δ^(η−1)，而ν(Z_b)→1。定义b(u)=Σq_iB^-i。

在每个非空aligned B^-k窗口内，prefix固定，余下q/r独立且均匀；首digit限制仅改变固定倍全局常数。b_*Uniform Z_b是τ-digit概率，因此所有w≥δ满足ν{u∈Z_b:|b(u)−c|≤w}≤C_LB^C w^τ。定义Tu=I+b(u)N，选同一实际u0∈Z_b，Su=TuTu0^-1=I+(b(u)−b(u0))N。算子球与b球可比，故原time law的相同cap和全部尺度coverlower成立；没有改为Uniform distinct operators。

## 6. 实际global Lip与每窗口line非集中

两个不同bulk times的首个不同digit差e−d≥2，因为所有d_i为偶数。首差层k上，|u−v|≥(e−d−1)B^-k≥(e−d)B^-k/2。相应q差≤(e−d)/R+1≤e−d，q尾差≤(Q−1)B^-k/(B−1)≤B^-k。因此|b(u)−b(v)|≤C|u−v|，C固定；本构造确有global Lip，不仅dyadic Lip。

更强的实际局部界为：非空prefix窗口J0长ρ=B^-k，δ≤w≤ρ，对所有实a,c，

    Pr_(Z_b∩J0){|b(u)+a u−c|≤w}
        ≤C_LB^C(w/ρ)^τ。                         (6)

消去prefix，u_tail=ρ(R Q_tail+R_tail)、b_tail=ρ Q_tail。若|1+aR|≥1/2，条件全部r digits，使用Q_tail的τ-cap。否则|a|≥1/(2R)，条件全部q digits，使用R_tail的(1−τ)-cap；系数放大至多B的固定幂，且1−τ>τ。w/ρ≥B^-(L−k)支付有限深度原子floor。两种条件law都来自同一原time乘积，不给g额外独立性。

## 7. 精确fractional矩阵、实际输出与wholeclock直线

anchors t=0,s=1分别设Ft=I,Fs=0，Yt=Ys=A。bulk取Fu=uI−u(1−u)b(u)N。因A_matrix=Ft−Fs=I，M_u=Fu，λ=u；M、I−M的最小奇异值均有固定正下界。

    Ct=(1−u)M=u(1−u)[I−(1−u)bN]，
    Cs=u(I−M)，Ct^-1Cs=I+bN=Tu。              (7)

令Yu=Ct(u)C。Ct及逆均统一有界；D足大使CtC仍δ-separated，体积/cover/AD1及tubeKT在线性像下只付固定常数。由(4)，Ct y+Cs y′∈N_Cδ Yu，故g(y,y′,u)=1_(Z_b)(u)，对每一个原pair都保近满clock；总体mean亦→1。

这张图由真实直线x(u)=−(1−u)y+uy′、z(u)=uy′实现，z(u)−Fu x(u)=Ct y+Cs y′。在两anchor native值恰为y、y′。本文没有只给一个抽象mixed sum后丢掉原clock输出。bulk公式不延至anchors；Z有固定大小空隙，所以整体F仍固定Lip有界。

## 8. 整个allowed窗口的native coarse正则性

Fu、b(u)、Ct(u)在bulk固定Lip。对同一ρ窗口的任意u,v，||Ct(u)−Ct(v)||≤Cρ，且C有界，故Yu⊂N_(Cρ)Yv。于是P=(∪_(u∈Z∩J0)Yu)_ρ的upper AD由固定一个Yv的ρ-cover付；lower AD对P任一中心使用实际含该点的Yu及其AD1下界。R≈ρ仅付固定常数，R≫ρ用球扩大/缩小即可。因此P为(ρ,1,C_LB^C)-AD。

allowedρ=B^(-jC*)≤B^-C*的非空bulk窗为完整prefix窗；不与孤立anchors混合。ρ=1的全局有界cover在该尺度平凡。原sourceallowed中仅含anchor的窗fine Yu=A同样正则。保的是指定native/coarse Y接口，不因此宣filled X、pointΦ或全部Def17 coherence。

## 9. 原allowed尺度的all-real local NF

设δ^(1/4)≤ρ≤δ^η为allowed，J0任意dyadicρ窗。只含一个anchor时，命中至多1，而ρ^θρ/δ→∞；空窗平凡。bulk窗全为prefix。若某全real affine矩阵Ru+U在误差ρ^(1+ε0)内命中m>ρ^θρ/δ个原times，取首末命中点，span≥(m−1)δ≥cρ^(1+θ)。整体Fu为固定Lip，故其offdiagonal fit系数r满足|r|≤C+Cρ^(ε0−θ)≤C，截距亦有界。

写d(u)=u(1−u)。offdiagonal条件给b(u)距函数−(ru+c)/d(u)不超过Cρ^(1+ε0)。bulk d≥3/16，该有理函数C² norm固定有界；在J0作Taylor，误差Cρ²≤Cρ^(1+ε0)，所以命中点满足b(u)在某条全real affine line宽Cρ^(1+ε0)内。第(6)式给

    m≤C_LB^C ρ^(ε0τ)#(Z_b∩J0)
      ≤C_LB^C ρ^(ε0τ)ρ/δ。

先让C*满足C*(ε0τ−θ)>C+3，再使B足大吸收C_L和固定常数；ρ≤B^-C*使右端<ρ^θρ/δ，矛盾。ρ≥δ^(1/4)保证所查width≫δ，且有限depth floor合法。NF是每个实际allowed窗口和所有real affine fits的原绝对计数界；不只是global非affine，也没有无证明把dyadicLip当globalLip。

## 10. 同一cone、小作用与未支付的完整源条件

W=e1，Tu和Su均精确保W，W0=Tu0^-1W=W。ell=e2^T、v0=e1给ell v0=0及ell adj(M)v0=0，原未除fractional cone精确成立。两不同bulk u,v有det(Fu−Fv)=(u−v)²，故该模型并非全部差矩阵秩一。第4节的same X smallactions、第5–9节的原law/native输出/NF同时成立，不能再以“这些toy没有拼在一起”驳回它。

但wholeclock lines参数来自A²，fine总规模约δ^-2，不能冒原4-AD的δ^-4全管族。没有证明CW上界、每native点filled二维x-fibre、每point AD1且slabγ的Φ、selectedξ及多尺度coherence。不能以添加无关管、补padding、任意赋Φ或声闭包保留来填空。本文不提供完整source反例，不给原δ²全T块的新质量结论；它只证明已提取联合有限信息本身仍有这种阻碍。

## 11. 与旧失败、restriction及literature的边界

R28旧finite box未同时保positive original Tu law、同一X与local NF；本构造逐项补齐这些，所以是严格更强的联合反攻责任，不重报“没有common X”。R28 carry门槛针对原fulltime×slabangle乘法，其输入未由本模型支付；本模型仅利用β+τ<α的数字承载，全部真实卷积与尾项已计，不否该旧门槛。CP/PM/PW4的全称正gain闭包仍不换名。

这里mean与逐pair clock都由g=1_bulk实际核；没有构造原heavy管族，故不能把逐pair nearfull升级为完整source逐管shading闭包。高级He/HdS/Li/ABC只在phaseI作不适用条件筛查，本文有限反模型证明不调用它们的wholeproof；一手筛查范围存literature/notes并列明未采用为高级输入。

## 12. 当前审查、停止与总目标

两代理已实际全文逐式反攻并限定通过，见research/reviews/R0079_clock_NF_and_joint_source_review.md、research/reviews/R0079_geometry_action_and_native_mass_review.md与research/reviews/R0079_root_integration_review.md。任意方向KT、prefix窗、digit条件law、fit斜率/C²、真实Ct输出及fullsource缺项均独核。仅列明联合有限接口记内部reviewed，未经外部同行评审；不新ID、不作major/novelty声明。

本轮无新的branch-saving。若上述严格联合反攻成立，冻结仅靠same X+Tu-cap+cone+NF的直接增长捷径；下一研究须先按连续两轮无branch-saving作完整四路径macro reset，选择真正使用尚未提取完整源几何的不同机制。ordinary n≥5/general完整证明或真全方向compact反例、经一手比对支持的重大结果均未达到，Goal active。
