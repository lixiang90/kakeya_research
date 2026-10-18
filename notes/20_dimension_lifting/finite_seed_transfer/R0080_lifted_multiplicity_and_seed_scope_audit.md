# R0080：KT提升重数、保留遮蔽与有限种子范围审计

2026-10-18，B阶段II，按先锁spec§2。复核经典KT §6的具体核心证书，不登记新定理ID或新六维界。本文未宣完整重证KT6.2全部critical/bilinear预处理。

## 1. 精确输入、soft费用与证书边界

固定ambient M、实n,d,d′，0<d<n；实际六维用途还取d≥3、d′=4−ζ。令N→∞、δ=N^-1，K=K_N=N^o(1)统一记录有限次常数、log、boxes、几何逆分离及允许误差；K的固定幂仍subpower。若需finiteε形式，先固定输出ε及种子误差，再令log K/log N小于相应有限阈值，不把K作任意固定幂藏入o1。

输入已critical-normalized：原δ方向分离的(n−1)-collection及原shading E满足#E≤K N^d、每ball δ≤r≤1有#(E∩B(x,r))≤K(Nr)^d；有transverse-angle集合A，#A≥K^-1N^(2n−d)。空间范围、角度逆下界、稍后的pivot几何分母均≤K^C。saturated仅为N^(1−o1) marks，不声每线cN。

A模块从原shading构造Ω′，记M0=#Ω′，保M0≥K^-C N²#A；fixed z时f=(z,i)在Ω′上injective或仅K^C重数，i∈E。每index w=(α,z)有至少N/K^C个真实good collinear pairs及相应lifted mark cells。goodpairs预先保|y1−y2|≥K^-C及需要的距离分离；retained后不再假全部old pairs可用。第3节给正确d-collection，第5节实付截断，和A的retained pullback合出指数。

## 2. 提升的真实指标：第一坐标属于第二根旧管

在一个angle的二维平面取vertex x、两条方向v1,v2。写i=x+a v1、z=x+a v1+b v2，旧pair为y1=x+c v1、y2=x+e v2。共线条件为a/c+b/e=1。提升线为

    L_(α,z)(t)=(x+t(z−i),t)，
    t=e/b， first coordinate=y2。                 (1)

因此原文first-coordinate写y1不能直接照抄；方向z−i平行T2。等价重命名两旧端点亦须全链一致。共线关系给

    y1=(tz−y2)/(t−1)。                            (2)

goodpivot/oldpair分离确保|t−1|≥K^-C、|t|≤K^C；如进一步需|t|下界亦在goodpair定义中付。finite lattice只给K^Cδ的近似式，(1)(2)各自的逆条件数显式计入K。不能把N^(1−o1)密度自动升级为使这些分母绝对有界的cN配置。

## 3. 正确方向cap是d，而非d−1

fixed z的提升方向由z−i及最后clock坐标1决定。设相关slopes范数≤K^C。unit方向角≤r时，clock chart的逆变换给i落在半径K^C r的球内；r≥δ处，原E ball upper及f-injectivity给

    # {w∈Ω′_z: direction(L_w)∈Cap(ω,r)}
                               ≤K^C(Nr)^d。      (3)

球半径大于1用#E≤K N^d付，最细有限邻格/fibre重数仍为K^C。故这是d-collection，对应K(d+1,d′)；没有依据可把右侧写成(Nr)^(d−1)。原6.6 proof的display与statement不一致，在本证书按(3)独推，不由此宣布原KT定理错误。

如原提升方向仅δ/K^C分离或一个δ-bin有K^C indices，用最细direction-cell图作有限邻格着色，可分K^C个真正分离子族；shading不合并，indexed重数未免费删除。后续unsaturated种子的K^C损失一并承担，不要求每个z的line count饱和为N^d。

## 4. 真实unsaturated输入及subpower normalization

本证书使用以下明确输入：任意fixed ambient、方向分离且满足(3)的有限J族，在各index原marks至少N/K^C时，union fine cover满足

    # union marks ≥K^-C N^(d′−d−εs)#J。          (4)

这里εs>0可任意预定，K足小依该种子input tolerance。一般d′时(4)是具名K(d+1,d′)的unsaturated版本；不只引用饱和主句。实际d′=4−ζ、d≥3时，R29 FSD001已直接给任意m族

    #E≥ c λ² m Kcap^-1
                 δ^(d−4+εD)/log(1/δ)，

平均marks可先heavy；λ、Kcap均subpower，固定ζ余量及先εD后sourceη给(4)，不需要另假临界endpoint K(d+1,4)或线性η模数。

若lifted空间/clock仅在K^C box，先分K^C个fixed unit boxes，逐line选其最富box，再按共同box与固定方向chart分组。每line保N/K^C原marks，一组原indices数只损K^C；不是因box随N长大便把种子固定R常数冒uniform。把K^Cδ近线误差改到δ_eff=K^Cδ、最细方向着色及原mark合并至多再损K^C；N_eff=N/K^C，λ_eff仍subpower。apply fixedambient seed于这些真实旧marks，换回fine格只增减K的固定幂。(4)由此在本soft normalization下仍成立。不可把N_eff改名后丢掉它相对原N的费用。这些选择只是(4)的证明，未把全局μ改成每line使用不同coordinate chart；后续每个z的energy及retained indicator始终在同一个原lift格（或共同coarse格）中计算。

## 5. 高重数截断：保原Ω′分母与真实总mass

fixed z，记m_z=#Ω′_z，原提升shading为Q_w，W_z=Σ_(w∈Ω′_z)#Q_w。由原pivot marks和有限重数

    N m_z/K^C≤W_z≤K^C N m_z。                   (5)

选固定ε>0、εs<ε/4，令T=N^(d+1−d′+ε)（实际用途d′≤d+1，故T≥1）。定义μ_z(q)=Σ_w 1_(Q_w)(q)，H_z={q:μ_z(q)>T}；保Q_w^ret=Q_w\H_z。若Σ_w#(Q_w∩H_z)≥W_z/2，则该坏shading平均≥N/K^C。先删每line坏marks少于N/K^C的小部分，并用逐line marks≤K^C N，仍有至少m_z/K^C个原indices各保N/K^C坏marks。

对它们用(4)给#H_z≥K^-C m_z N^(d′−d−εs)。于是

    W_z≥Σ_(q∈H_z)μ_z(q)>T#H_z
        ≥K^-C m_z N^(1+ε−εs)，

反(5)，因为K=N^o1。故逐z坏mass<W_z/2；所有z同时有

    W_ret=Σ_w#Q_w^ret≥N M0/K^C。                (6)

保的是same Ω′上的总markmass，不要求每个pivot仍有N/K^C保留pairs；无须删掉大批indices再偷换M0。m_z小或(4)右边<1不成漏洞：真实cover仍≥该弱实数lower，上述代数矛盾仍有效。空z忽略。

## 6. L²的upper：不是原文文字所说的lower

截断后μ_z^ret≤T，原总mass≤K^C N M0。因此

    L2:=Σ_zΣ_q (μ_z^ret(q))²
        ≤T Σ_zΣ_q μ_z^ret(q)
        ≤K^C N^(d+2−d′+ε) M0。                  (7)

这确为upper，不靠Hölder另给不存在的lower。选择slightly更大的T仅消耗预定ε，不能把其ε当sourceη而后倒选。若想先按各z截断不同阈值，也须保统一N/ε及同(6)原分母；本证书不需要该额外自由。

## 7. Retained indicator与真正可回拉的关系

只定义来自原goodpair的关系：w=(α,z)∈Ω′，y1/y2是该w的原goodpair，且其由(1)产生的共同liftcell q=(y2,[t])属于Q_w^ret。记此条件为R(w;y1,y2)，显式含1_(Q_w^ret)(q)。

每个retained lifted mark至少有一个原goodpair witness，所以由(6)

    Σ_(w,y1,y2)1_R≥N M0/K^C。                   (8)

一格可能来自K^C个oldpair，足以维持(8)；绝不能说因为每old pivot原有N pairs，截断后每pivot仍有N retained pairs。相同triple(z,y1,y2)决定共同t（允许K^C相邻格），且给定(z,y2,[t])由(2)只容K^C个原fine y1-cells。A模块必须用同一canonical rounding/有限着色付这两向恢复；不能让每α随意选一个互不相容的t然后平方。

## 8. Retained L²的lower与正确triple universe

设Σ_good为所有实际可能的(z,y1,y2)。原goodpairs先保|y1−y2|≥K^-C，旧点皆在E。给定y1,y2，z在一根K^Cδ厚、长K^C的line-neighbourhood内，fine grid数≤K^C N，所以

    #Σ_good≤K^C N (#E)²≤K^C N^(2d+1)。          (9)

若删选后才临时要求此端点分离，可能失去(8)，故它已放入原liftmark定义。仅知pivot远两旧axes本身不够排旧pair接近vertex；source saturated密度也非cN。

令r(z,y1,y2)=#{α:R((α,z);y1,y2)}。由(8)(9)及CS，Σ r²≥K^-C N^(1−2d)M0²。共同liftcell/三元组的有界K^C恢复给Σr²≤K^C L2：每共同cell只容K^C triples，而每triple所有保留α确同时计入该cell的retained μ。故

    L2≥K^-C N^(1−2d)M0²。                       (10)

這是所需lower。只取全部oldpairs的同式不合法；retained指标使(10)真正对应(7)的同一个L2。

## 9. 结合指数及实际有限参数先后

A的pivot/保f核心给M0≥K^-C N^(2n−d+2)；比较(7)(10)先得M0≤K^C N^(3d+1−d′+ε)，于是

    N^(2n+1+d′−4d)≤K^C N^ε，
    4d≥2n+1+d′−ε−C logK/logN。                 (11)

ε可任意预定，K=N^o1后极限给4d≥2n+1+d′。没有把M0替成删选前后不同集合，也没有漏掉lift time贡献的一次N。fixedambient常数可依M、n,d,d′，M不得随N增长。

有限版本取(11)目标余量ω>0：先ε<ω/4，再(4)的εs和相应inputη_s；所有预处理/几何误差的logK/logN后小，使K的实际有限次数满足种子门槛及ω剩余。N_eff=N/K^C→∞、指数替换只再付C logK/logN。只声明这个先后，不声任意固定K=N^a都可在a未计时套soft定理。

## 10. Critical/raising-d及角归一化尚属哪个层次

本文证明的是第1节明确critical core输入下的certificate。原KT从K(n,d)和失败K(n,d+ε)做raising-d/挑countersequence，去heavy balls得E ball upper，再bilinear按角θ rescale至transverse，涉及新的N、shading、point-ball常数及ambient规范。这些不能由上文3行不等式自动补全。

本轮A若逐步付pivot生成、subpower好分离及f Córdoba，则该部分可独立替代原6.4–6.5；但(41)前的critical提升和(43)(44)的所有尺度blurring、(45)的完整angular normalization仍须在root最终明确是新证还是具名输入。未实际全证时不宣本文重证完整KT6.2，更不宣原已发表定理错误。历史6.6 exponent、6.7上下界文字和末段遗漏retained indicator是具体证明书写责任，不自动是原结论反例。

对于实际六维用途，若critical d被提高而仍低于目标17/4−ζ/4，它仍≥4−ζ，故第二参数d+1≥5−ζ≥4，R29 FSD任意实参数种子仍供d′=4−ζ；不能只知道单个K(5−ζ,4−ζ)就免费外推提高后的参数。本用途因已有全体real n≥4种子而安全，不是免费方向维单调性。

## 11. DIM001既有结论与具名输入不被改写

接受R38内部OAI4 proof assembly及其G/WZ/CV/OSS高级输入后，SRC/DIR与R29FSD给严格K(n,4−ζ)；具名KT6.2应用n=6,d=d′=4−ζ，得到17/4−ζ/4。R38已付任意集合outermeasure finite→Hausdorff桥，ζ↓0得既有DIM001的任意R6 Kakeya集合17/4范围。本轮不重报compact或finite源gap，也不以核一个核心certificate删除原条件或宣布新界/priority/major。

本证明对d-collection和unsaturated/平均shading的核对是明确范围缩减：无需CW、sticky或方向ADlower；fixed arbitraryambient是第二次lift所必需。外部高级wholeproof不在本轮无限递归重审；一手出处KT math/0102135v1、已发表2002版信息按库记录，本文实际读本地§6文本，未虚报新PDF下载或视觉全文核。

## 12. 实际读域、交叉审查与停止

实际全文读锁题R80 working_spec5、KT原§6（连同5.1/5.2及soft记号入口）和R29 root7/B7、R38相关finite/任意集合出口。随后actual全文逐式读A《R0080_pivot_geometry_and_retained_pullback_audit》12节与root《R0080_retained_pivot_core_certificate》12节，不以消息摘要替代。

A第3–5节的same-annulus goodtriples保N³/K^C、原pair分离、bounded pivot/fibre及Córdoba方向能量→真正f-injective，均独核；第6–10节正确y2指标、共同triple的dot-ratio time、共同单位窗/δbar格/方向着色、retained indicator及双向有限恢复亦通过。A证书的共同单位窗有实际y2∈E marker且z−i固定有界，所以整unitportion亦固定有界，非只凭marker有界冒支持线范围。

root采用另一合法fine版本：在精确lift线上取fine mark，每retained cell预选原好pair。共同triple仅恢复至K^C相邻cells而非exact相同cell，反向固定cell亦只有K^C triples；两次有限CS确给其(P)和同一retained L² lower。root§2实际已将可能skew的原两axes分别平移Oδ到共同原x，未假高ambient精确交点。真实原N/Ω′分母、seed阈值与critical仍named的边界一致；当前未见强制修改。

上述density自证不冒本人独审，A/root已各自独立核其链；本稿交叉核范围仅所列normalized certificate，非wholeKT6.2。formal按另授权完成，未经外部同行评审。不新增ID、Goal完成、无条件DIM状态或未来Git/sync认证；只编辑本12节，停止任何未锁旁支。
