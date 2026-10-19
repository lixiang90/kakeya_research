# R0104：原全局码的affine2plane上界与Schubert反攻

2026-10-19，B／lifting_obstructions。先实际读reselection5作原几何准入，随后实际全文读root锁定的working5才施工第3–7节主cap。本文不将P平坦当源额外假设，不预认reviewed／newID／major或完整κ1增益；独立formal另授权。Goal active，未经外部同行评审。

## 1. 恢复、原对象与实际读域

实际读GOAL、当前STATE、ROADMAP当前完整路径与历史冻结、registry全部78项ID/status、R104 reselection及working各五节、R102 root十二节和R103 root十节／next六节；上轮同会话已经全文的formal及旧源读域保留。本次又实际全文读R22 whole-time restriction五节、R77统一NF第3–4节与R78 uniform-cap第2–5节所在全文，核原参数／全时层和newallowed责任，不下载或重跑context／Git。root父快照及回执由其恢复记录负责，本稿不认证。

采用完整bounded WZ Def17 matrix33 κ1的R102 det-large分支：原N≈Kδ⁻⁴、m=|Z|≥K⁻Cδ⁻¹、|E|≤K^Cδ⁻⁴，γ>0固定；原CW／joint4AD／filled-X／nativeY AD1与tube-KT／pointΦ AD1及slabγ／ξcoherence全保。H为R102 code同权层的实际原管，|H|≥L⁻C N，每根仍保全部旧S_T且|S_T|≥K⁻C m。P为不同δ-codecells，每cell管数在[w,2w)；其2Fst已付，不重做。本轮L含有限K、anchors／far条件数和log，原K只含η，不偷混二者。

固定anchors t,s，h=s−t、A=F_t−F_s，|h|、sminA≥σ；far尺度r。沿R102第三点有C(T)=Γ_p+G_uφ+Oδ，G_u=((t−u)(F_u−F_s);(s−u)(F_u−F_t))，far上sminG_u≥rσ/2。新目标是对**每个**affine2plane Λ及δ≤a≤1证明p(a,Λ)=|P∩N_aΛ|/|P|≤L^M a^β，β>0。若该主cap失败不能退成仅“若P平坦则”的proper结论收轮。

## 2. 原code是physical phase观测，但不是免费plank

设原axis在clock v为(X(v),v)=(a₀+vφ,b₀+vψ,v)，a₀,b₀,φ,ψ∈R²。两端code恰可写为

\[
U=X_z(t)-F_sX_x(t),\qquad
V=X_z(s)-F_tX_x(s).
\tag{1}
\]

将原ξ_(p_t)=ψ−F_tφ、y_t=X_z(t)−F_tX_x(t)代回即得R102的(U,V)=(y_t+Ax_t,y_t+hξ_(p_t))，误差Oδ。故码是原8维axis参数的共同linear map，非自由赋予的ξgraph。这个事实本身也不说明它的affine超平面preimage是物理plank。

具体n=(l,m₀)为code超平面normal，n·C=d等于η₀·(a₀,b₀)+η₁·(φ,ψ)=d，其中

\[
\eta_0=(-F_s^Tl-F_t^Tm_0,l+m_0),\quad
\eta_1=(-tF_s^Tl-sF_t^Tm_0,tl+sm_0).
\]

沿点(X,u)可写1-form ω=(η₁−uη₀)·dX+(η₀·X−d)du。其dω=2η₀·dX∧du一般非零，故是line-complex条件，不能无论证当所有whole axes落同物理窄凸prism。后文真实主cap用两独立normals及完整source，未从这一个linear phase等式免费调用CW。

## 3. 近plane选原管、逐管far及p真正消去

固定Λ和a，p=0时平凡。令H_p为P∩N_aΛ对应codecells里的**全部**原H管，N_p=|H_p|。同比权层给N_p/|H|在p的固定倍内，每T仍保全部原S_T。先删每根距t,s小于r的clock，原δ-separated Z使每管损≤C(r/δ+1)，除原K⁻C m后η≪far指数时至少半保。因此

\[
I_p^{\rm far}\ge K^{-C}N_pm.
\tag{2}
\]

此处没有L或p的额外clock损失。对**原全E**重做point-heavy，阈值D_p=I_p^far/(2|E|)≥pL⁻Cδ⁻¹，light p的訪问损≤I_p^far/2。此后只保平均。令I_u^p为该重heavy后的访问数，每u最多N_p；取阈值K⁻C N_p，得到一集合S⊂Z，

\[
|S|\ge K^{-C}m,
\qquad I_u^p\ge K^{-C}N_p>0\quad(u\in S).
\tag{3}
\]

证明是Σ_u I_u^p≥K⁻C N_pm除以每time upper N_p。N_p与其p因子在这里相消，故S的原time比例只损K，不损p或anchor L。D_p仍含p，两种量词不能混。每个u∈S至少有一个原heavy p带D_p根H_p管；后面仅取这样一个点应用原Φ upper，不给被选角族ADlower。

## 4. 消费原slabγ：从大角子集到whole G-plane

写Λ=c+V，V为二维linear plane。对V⊥任一unit normal n，所有H_p实际codes都满足|n·C−n·c|≤a+Cδ。在第3节heavy原点p，恒等式给这些管的原角

\[
|n^TG_u\phi+n^T\Gamma_p-n^Tc|\le a+C\delta.
\]

每δ角bin原T重数O(1)，因此至少D_p/C个不同原Φ_p角满足此式。若b_n=|n^TG_u|>0，这是原角盒中的slab，宽C(a+δ)/b_n；用完整Φ_p的slabγ upper和|Φ_p|≤Kδ⁻¹，得

\[
D_p\le CK\delta^{-1}
 \min\{1,[C(a+\delta)/b_n]^\gamma\}.
\]

宽低于δ时固定倍扩张至δ；a≥δ且G bounded保证只改变固定常数。宽≥1则b_n≤C(a+δ)，同一结论更直接。因而对两正交normal同时有

\[
\|\Pi_{V^\perp}G_u\|
 \le L^{C/\gamma}(a+\delta)p^{-1/\gamma}.
\tag{4}
\]

far sminG_u≥rσ/2再给dist(imG_u,V)≤E，其中E=L^{C/γ}(a+δ)p⁻¹/γ，有限rσ逆幂计入L。此处是真正使用R102尚未消费的完整slab输入：code-rich AD1角落一条交线会违反其slab upper，不能只停在Schubert交线。方向subfamily的lower没有继承，实际degree与原Φ upper负责两端。

## 5. 任意plane两blocks均可奇异：D恢复whole F

取V的正交列基L_V=(L₁;L₂)∈R4×2，任一block不必可逆。令α=t−u、β_u=s−u，X=L_V^TG_u，R_u=G_u−L_VX。由(4)有||R_u||≤CE，且||X||≤C。恒等式β_uG₁−αG₂=αβ_u A给

\[
D(u)X=\alpha\beta_u A+O(E),\qquad
D(u)=\beta_uL_1-\alpha L_2.
\tag{5}
\]

只要E≪r²σ，右边最小奇异值≥r²σ/2，故D和X均可逆，并由D⁻¹=X(DX)⁻¹得||D⁻¹||≤C(r²σ)⁻¹。没有给M_u或I−M_u新的可逆假设，也不用某个Grassmann block作pivot。

又G₁=α(F_u−F_s)=L₁X+O(E)，从(5)解X并除|α|≥r，得

\[
F_u=H_V(u)+O(L^CE),\qquad
H_V(v)=F_s+(s-v)L_1D(v)^{-1}A.
\tag{6}
\]

D(v)是affine矩阵，H_V是至多二次分子／二次分母的formal模型，不把原rough F先假为有理函数。对任一实际u∈S，D(u)逆已有L^C upper；||D′||固定有界，故|v−u|≤w、w≤L⁻C时Neumann给整窗口同样逆界。显式inverse导数给||H_V||C²≤L^C，uniform于所有V。极点可能在其他地方，本文只在每个实际occupied窗口证明无pole，不以measure0口头删除。

## 6. Coarse主cap：完整原time重源及非循环NF预算

固定R77一般F的all-real非拟合准备参数ε₀、θ、c_N、w₀，只依原γ及具名source工具；它们不随后依本轮a、μ重新选。该已付输入说：完整配置参数η_src若满足η_src≤c_N log(1/w)/log(1/δ)，δ≤w⁴且w为其allowed尺度，则误差w^(1+ε₀)、命中>w^θ w/δ的all-real matrix fits所在whole windows仅能承载<w^θ比例原times。其all-real扩展用原V／own-slab／native KT已实际支付，不是把literal bounded-Mat 20.2改字。

先固定小d₀>0和固定大B>4(1+ε₀)，再取M足大依B、γ和有限condition幂。仅对a≥δ^d₀反设

\[
p>L^M a^{\gamma/2}.
\tag{7}
\]

由(4)，E≤C L^{(C-M)/γ}a^(1/2)。取M大，这小于L⁻C a^(1/2)，付第5节误差／可逆门槛。非trivial p≤1还给，记ℓ_L=logL/log(1/δ)、d_a=log(1/a)/log(1/δ)，

\[
\ell_L<\gamma d_a/(2M).
\tag{8}
\]

从第3节S只损原K密度，对**原完整S-time层**依R22重源，η_src为原η的整数倍且Oη；原全T不改，S每层全部Y/X/Φ/ξ保留。不重生H_p或point-heavy后的删点源。原跨time Y-union lower由其任一保留整层继承，upper由原union继承，coherence在newallowed子格继承；原平均shading重新由witness总数计，不声每原T在S仍nearfull。

取target w_*=a^(1/B)，在newallowed取上邻w。其μ=log(1/w)/log(1/δ)满足d_a/B−η_src≤μ≤d_a/B；(8)及M后大给μ≥d_a/(2B)、η_src≪θμ、以及所有condition幂logL≪log(1/w)。故w≤L⁻C、每occupied window pole安全，且

\[
L^C(E+w^2)\ll w^{1+\varepsilon_0}.
\tag{9}
\]

例如E项指数接近d_a/2，严格大于(1+ε₀)d_a/B；Taylor项只要求Cℓ_L<(1−ε₀)μ，均由M固定大支付。a≥δ^d₀给w≥δ^(d₀/B)，d₀/B<1/4故δ≤w⁴；非trivial(8)使w趋零并小于固定w₀。没有η依未知μ重新选或先在每个a上改NF参数。

完整S配置|S|≥δ^(η_src−1)。每w窗口若少于2w^θ w/δ点，全部light窗口合计≤Cw^θ/δ，占S比例≤Cδ⁻η_src w^θ=o(1)。余dense windows各在其中取一个实际u，(6)的模型整窗C²有界，(9)给一个all-real affine fit覆盖其全部S-times。这些windows承载至少半S却全是NF坏窗，反源准备。于是(7)不可能，得到coarse cap p≤L^M a^(γ/2)。

## 7. Fine floor、全部affine2planes与主cap完成范围

原数据参数顺序为：γ和已付NF参数固定，d₀／B／M固定，再取R102的anchor、far及η exponents足小，δ最后。若某尺度使L^M a^(γ/2)≥1，只用p≤1；不强行进入Taylor／NF。因此coarse上界的固定prefactor统一，无plane-dependent最小奇异值或blockchart constants。

对δ≤a<δ^d₀，只用p(a,Λ)≤p(δ^d₀,Λ)≤L^Mδ^(d₀γ/2)。取β=d₀γ/2，因a≥δ，δ^β≤a^β；coarse段γ/2≥β也给a^(γ/2)≤a^β。故所有δ≤a≤1、每个affine2plane均有

\[
\frac{|P\cap N_a\Lambda|}{|P|}\le L^M a^\beta.
\tag{10}
\]

这是已锁的主目标，不是仅一个flat proper subclass。a≤δ^d₀的证明未外推NF细于允许floor。affine offset只影响第4节slab中心，其位置不进入D模型或condition常数；Λ远离有界P时p=0，近P时也不需另取offset下界。

## 8. Hyperplane／Schubert仍未付及严格弱反攻

若只假P近一个affine hyperplane，其单normal slab步骤同样合法，但只迫

\[
(t-u)l^T(F_u-F_s)+(s-u)m_0^T(F_u-F_t)\approx0.
\]

这只有一row响应，不能按第5节恢复whole F。式(1)的phase hyperplane也不等wholeaxes窄prism；whole-CW只对真实containment convex查询。若要沿1-form／contact约束另做finite横向兼容，必须真正用filledX与原marks，无条件取导／Stokes或假ξ smooth不可。

R103 Schubert簇仅det(GᵀB)小，允许两个2planes沿一线相交，未迫码P靠某个affine2plane。不能由(10)说已排这些簇，更不能把Q的sublevel值换成metric-flatness。R79上三角rough弱模型仍可在单Schubert cycle内运行，缺fullpointΦ／filledX／joint4AD-CW，不是本主cap或完整source的反例。光滑coefficient模型若不保local SM，只校准代数自由度。

抽象P2Fst加rich直线fibres本可取P为一张plane；它没有原Φ slabγ／source NF，故不能反(10)，也说明本轮新增消费的原条件不可省。本文没有构造fullsource反例，不续hyperplane／contact toy或goodrank参数为下一主题。

## 9. Restriction、两密度闭包及旧等价核

H_p为whole-index选择保旧每T全部ST，原absolute CW upper继承，probability常数若重归一须付N/N_p。重point-heavy后仅总量保，rich S是原time标签集，其比例p取消不是说每管在S保持lower。source NF实际重生S上的**所有原层数据和原T**，不是把H_p的删角／删点族赋新ADlower；R22的参数只依整层time比例K⁻C，正是本proof避免p损失的地方。

若原只有平均λ先heavy，必须保I/2、N′≥λN/2并付normalized CW的λ⁻¹，再可进入R102已经准备的det-large重管分支。本稿不替ordinary初始化证明这一分支总有质量。平均、逐管、逐pair和每point的实际方向数各有不同分母，没有从一项继承全部lower。

R44测试／R45 selected KBL、R76单块、R78共同X/action不自动给(10)的原point-slab用途。R78已付一般NF／whole-time预算可真实重用，但它的T_u-ball公式仅both-fullrank，本稿用D恢复避开这项未付条件。旧CP/PM全称gain重调用及反向重建未对本family证明，故不改名登记。R96固定或uniform polynomial β是F函数的额外形式，本稿的有理H_V只在反设cap内被迫近似；两者scope不同，不续degree／谱gap。

## 10. 当前证明状态、四路范围与停止

第3–7节在实际working5锁后给主cap的独立有限证明；尚待root／A终稿实际全文交叉审查，本文自身不计独审或reviewed，formal另授权。有任何原I、p取消、slab、D条件数或NF预算错误应先报告，不以若flat后果代主目标完成。

当前新输入只是在既有matrix33 det-large全局码上排affine2plane正质量集中，未排R103一般Schubert簇、全部rough／其余mixed、ordinary初始化／HRZ全费用或真同集full方向strict反例。DIM已付推论及其认证层级沿旧范围，不重算充成果。完整Goal active，无newID／major／novelty／完整branchsaving声明，具名高级source wholeproof未从零新独证，未经外部同行评审。停止β／M／a／degree小改；仅分配文件编辑，无metadata／Git／下载／新代理。
