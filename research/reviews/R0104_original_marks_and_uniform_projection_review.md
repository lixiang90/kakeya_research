# R0104：原marks、affine2plane cap与统一投影终审

2026-10-19，B／lifting_obstructions。本文件独立主审root／A，不以本人B同题自证替代独审。结论限于working锁定的原global code非平坦上界与真实弱投影后果；具名源高级wholeproof仍具名，未经外部同行评审。

## 1. 实际全文对象和原假设范围

实际全文读root `notes/40_multiscale/sticky_matrix/R0104_original_code_affine_plane_nonconcentration.md` 十节、A `notes/00_map/R0104_complete_goal_and_incidence_routes_reselection.md` 最终十节、本人B十节，以及reselection／working两份各五节。本人B只是交叉对照，不自算独立审查；root／A对其实际独审另记。沿同一会话已实际全文核R102 root12、R103 root10及next；本次又全文读R22整时间层闭包，读回R77一般F统一all-real非拟合准备的实际证明和R78相应dimensionless预算，未重跑source下载／Git。

输入仍为完整bounded WZ Def17 matrix33 κ1及R102已提取det-large分支：原N／CW／joint4AD、nearfull clock、filled-X、nativeY AD1／tube-KT、原pointΦ AD1／slabγ和ξcoherence。H是全局code同权层的原管，逐T保原全部S_T；P是不同codecells中心。未向ordinary原族自动授这个分支，也未把R103 Schubert集中当P平坦的证明。

所限主结论是存在β(γ)>0、M(γ)，对每affine2plane Λ及δ≤a≤1，p=|P∩N_aΛ|/|P|≤L^M a^β。L实含原K和两锚／far／log费用，不是δ无关AD常数。先固定NF参数、d₀／B／M，再取原损失exponents小，δ最后；全文没有以若flat的proper结论替代这个全部Λ上界。

## 2. 原whole-index选择、point-heavy和p取消

root§3／A§9通过。按近Λ的codecells选择其全部原管H_p。同比权层给N_p≈p|H|，且保每T旧S_T；没有选一根code代表或只留其局部marks。far逐管至多删C(r/δ+1)，除原|S_T|≥K⁻C m后η≪far指数保证半保，所以I_f≥K⁻C N_p m。这个lower只损原K，不能无必要地塞入p或anchor费用。

随后在原全E上重做point-heavy，阈值D=I_f/(2|E|)≥pL⁻Cδ⁻¹，删light访问至多I_f/2。此后仅平均保量。每time最多N_p个管访问，取rich阈值I_f/(4m)：低times总量≤I_f/4，而余每time仍≤N_p，故rich S满足

\[
|S|\ge I_f/(4N_p)\ge K^{-C}m.
\]

分子分母的N_p及p真的相消；point degree D仍线性损p。不能把这两项改成共同p损失或赠给每管在S的lower。每u∈S至少一个实际heavy point，足供下一步原角upper；不需要所有points或每管拥有完整被选角族。

对Λ方向V的每条unit normal n，在该heavy p的保留原角满足一条宽C(a+δ)/|nᵀG_u|的slab。原Φ_p的slabγ upper及δ-anglebin bounded T重数给

\[
pL^{-C}\le K^C[C(a+\delta)/|n^TG_u|]^\gamma.
\]

小normal／宽≥1情形同样服从结果；a≥δ和G bounded支付slab的fine floor。两正交normals合并得||Π_(V⊥)G_u||≤L^(C/γ)(a+δ)p⁻¹/γ。**p仅一次进入degree，因此只有p⁻¹/γ**；root／A没有以p⁻C/γ冒用同一γ/2指数。实际degree与原upper承担此步，不授裁切Φ ADlower。

## 3. 任意V的D恢复、无pole与conditioning

root§5／A§9通过。任意正交basis B=(B₁;B₂)的两blocks都可奇异，令X=BᵀG、R=G−BX、α=t−u、β_u=s−u、D(u)=β_uB₁−αB₂。由β_uG₁−αG₂=αβ_uA得

\[
D(u)X=\alpha\beta_u A+O(\|R\|).
\]

若||R||≪r²σ，右端最小奇异值≥cr²σ。于是D、X可逆，D⁻¹=X(DX)⁻¹给||D⁻¹||≤C r⁻²σ⁻¹；不用B₁／B₂可逆，也未假M_u或I−M_u满秩。恢复的whole matrix为

\[
F_u=F_s+\beta_uB_1D(u)^{-1}A+O(L^C\|R\|).
\]

A给出的较精确误差C r⁻²σ⁻¹||R||也成立：记R上下blocks为R₁、R₂，利用I−β_uB₁D⁻¹=−αB₂D⁻¹，实际误差为−B₂D⁻¹R₁+B₁D⁻¹R₂；没有被漏的额外r⁻¹。root以L固定幂写误差同样安全。

D(v)为affine矩阵，||D′||固定。每个实际u∈S处的逆界使|v−u|≪r²σ整窗口无pole；inverse导数显式给formal模型R_V(v)的C² norm≤L^C。这只是在实际occupied窗口控制模型，不把rough F外插为有理source、不口头删极点，也没有plane-dependent不可控chart条件数。affine offset只在slab中心，不进入D或这些uniform常数。

## 4. Whole-S重源、coarse矛盾与fine全尺度

root§2／6–7及A§9的预算通过。关键重源对象是**原完整S-time层**，不是H_p或point-heavy后的删点配置。由|S|≥K⁻C m，R22给η_src=Oη并可取原η整数倍；保原全T、CW及每保留层全部Y／X／Φ／ξ。跨time Y-union upper继承旧union，lower从某个保留整层的fine AD取得，newallowed是oldallowed子格。平均shading重新计；未声每原T在S仍nearfull。

先证a≥δ^d₀的coarse cap。反设p>L^M a^(γ/2)，slab误差变为E≤L^((C−M)/γ)a^(1/2)。同时p≤1迫

\[
\log L/\log(1/a)<\gamma/(2M).
\]

先选固定B大，再一次取M大吞有限conditioning、γ、NF阈值；这使所有L费用相对工作尺度小，非仅口头a足小。取target w_*=a^(1/B)，新allowed上邻w的log指数μ_w与log(1/a)/(B log(1/δ))可比；取整费η_src包含于上式。于是η_src≪θμ_w、w≪r²σ、L^C(E+w²)≪w^(1+ε₀)，且a≥δ^d₀保证δ≤w⁴。较粗a若反设不能满足log条件，本已由p≤1平凡处理；非trivial区w趋零，亦付固定NF上端。

在完整S配置内，低于2w^θw/δ点的所有windows合计≤Cw^θ/δ，除|S|≥δ^(Oη_src−1)只占o(1)。余dense windows承载半S，每窗取实际anchor，用模型C² Taylor给同一all-real affine fit覆盖全部S-times，误差小于w^(1+ε₀)，与R77统一一般F非拟合准备矛盾。此处使用已经支付的all-real V／own-slab／native KT证明，未冒literal bounded-Mat 20.2。没有μ_w→0时重选ε₀／θ或在每个a重调源参数的循环。

故coarse p≤L^M a^(γ/2)。对δ≤a<δ^d₀仅用集合单调性：p(a)≤L^Mδ^(d₀γ/2)≤L^M a^(d₀γ/2)。取β=d₀γ/2，coarse亦服从此弱指数，完成所有δ≤a≤1、所有affine2planes的主cap；未把NF推到其fine floor之外。

## 5. 所有二维投影的真实后果与未付scope

root§8通过。任意orthogonal π_W:R4→W，二维ball B_W(z,a)的preimage就是affine2plane z+W⊥的a邻域。因此实际均匀code概率满足

\[
(\pi_W)_*\mu_P(B_W(z,a))\le L^M a^\beta
\quad(\delta\le a\le1).
\]

这是每一个二维投影的正指数**概率upper**，并非2-Frostman、ADlower、uniform distinct output点law或原incidence独立性。限制P中质量v的大子集，概率upper只可按v⁻¹收费；若合并输出cells再转uniform，要另作实际权层。A§7把它代入平面临界尺度得到形式上的正u，仍明列真实nice line／tube方向law、rank0／1与重数、原marks保量未付，本审不把那段资格变成已调用OS高级定理。A所列未采用primary的读取记录不冒本人的新wholeproof认证。

Hyperplane只给一个normal row relation和phase line-complex，不能按本D的两normal恢复whole F，也不等physical convex containment。R103的det Schubert小值仅可允许一维交线，未迫P靠Λ；本cap没有解决该簇几何。抽象flat P／rich fibres或R79弱三角模型缺full point-slab／filled-X／T4AD-CW，不是此源cap或Kakeya反例。

whole-index H_p保旧逐管ST、absolute CW upper；若归一必须付N/N_p。point-heavy后只平均，rich S的K-only比例也不赠原管在S的逐管lower。仅平均λ先heavy时I／管数／normalized CW三费要同时保；本稿不替ordinary初始化提取det-large分支。原ADlower和完整point资料之所以能进入NF，是重生原整time层，而非从裁切子族继承。

## 6. 必修项、有限范围结论与停止

当前root十节、A最终十节、两spec五节所限主cap与二维投影弱β-upper，**未见未解决强制修复项，实际全文范围通过**。本人B同题自证不计独审；root／A对其实际全文记录另存。本审没有把新cap降为仅若flat的条件命题，也没有把它升成无L费用的统一AD、超平面非集中或完整Schubert排除。

新原输入消费了此前rich fibre计数未用的完整slab条件及whole-time保持：p一次角损失与rich time中p取消、任意plane的D恢复、whole-S的Oη参数和源uniform NF缺一不可。旧R78both-fullrank算子坐标不能直接套用，但其一般NF证明与R22闭包确可重用。R44／45、R76／78–80和CP/PM的旧全称gain未被新名称解冻，反向重建完整源亦未证。

完整rough及其余mixed、Schubert簇的下一原几何、ordinary／HRZ全部预算与真同集full方向strict反例仍open。停止β／M／a／degree小改，不作newID／major／novelty、ordinary／完整branchsaving或Goal完成声明；具名高级source wholeproof仍保责任，**未经外部同行评审**。不认证未来metadata／Git／sync；完成指定formal后停止编辑与检索。
