# R0091：全单位线段transport与微分约束资格门

2026-10-18，A。仅按reselection_spec作阶段I资格核，恰八个编号二级节。原whole-line测度可以合法构造并调用来源；当前只到标准singular-rank约束，没有qualified新gain。未经外部同行评审，不改Goal标准，不预锁阶段II。

## 1. 恢复、实际版本和源阅读范围

实际全文读GOAL、STATE、当前全部ROADMAP、R90 next六节、R91 reselection_spec五节；读取registry全部78项并逐项核ID/status。R90 root10/A8/B8、两formal及source/macro/next的上轮实际全文逐步审记录按未改交接复用，没有无故重跑计算。parent记录父c6a8c3a…/treeded12…/1387旧clean，本人未另核Git或官方远端。

实际打开[De Philippis–Rindler1601.06543官方history](https://arxiv.org/abs/1601.06543)：v1为2016-01-25，current v2为2016-04-11。实际读[v2 HTML](https://arxiv.org/html/1601.06543v2) Th1.1、Remarks1.2–1.4、§1.3 Th1.10/Cor1.12–1.13，以及§3关于normal currents定义、Th1.10与Cor1.12/1.13的全部应用证明。HTML正文Date2026不是新arXiv版本；未下载、核PDFbytes或新独证§2的全部高级PDE主证明。

另实际读root新归档Moore《Descriptive Set Theory》提取文本physical47–48的Th49及相应证明文字，其标准Jankov–von Neumann声明正给Souslin measurable选择，因而对完成σ可测；原proof有composition等typing问题，不把阅读该文字称完整外部proof认证。Radon–Nikodým／disintegration及有限Borel测度在Polish空间为Radon仍用标准具名工具；下文具体carrier、endpoint、wave cone和计数自行核。来源声明、合法使用和wholeproof新认证分别记，不以作者署名代证明。

## 2. 完整四路和本门必须交付什么

ordinary仍需同一原full方向集合的Hausdorff下界，finite小阴影／allscale联合初始化不自动给；directHRZ仍须真实parent/terminal/coarse全部费用；sticky完整临界κ1、余mixed与ordinary桥仍open；真反例须同一个集合有全部方向单位段及严格维数upper。DIM001/R38/R80已付不重排，R90 polar端点、R89 cut-degree/hops、R88 cone、旧CP/PM/PW/action和更多锚点保持冻结。

本候选确有不同的已有输入：一条整单位段上的向量／矩阵transport有有限endpoint边界，可接微分约束定理，避免先要求光滑ξ或独立卷积。但最终须从原full方向或真实source推出某个超过rank barrier、保同一测度原mass的结论，再回Hausdorff／完整branch。仅写全局矩、标准wave cone或给定local ellipticity的后果不合格。

先处理compact原K的可测整段选择，再按parent要求核任意K的同维hull扩展。下面没有把finite dense shading当整clock，也不赠同测度的五个独立Alberti／normal-current表示。

## 3. 任意原K的同维Gδ hull和真实整段选择

设原K⊂R5包含每个方向一条unit segment；若h=dim_H K=5，维数目标已满足，故资格反设h<5。取s_n↓h且s_n>h，为K选开球cover，diam≤2^-n、Σdiam^(s_n)≤2^-n，令U_n为这些开球之并、G=∩U_n。则G为Borel Gδ且含K。任意s>h，在n大时s_n<s，原cover同样给H^s_(2^-n)(G)≤2^-n，故dim_H G≤h；由单调性等于h。

令R={(v,a)∈S4×R5:a+[0,1]v⊂G}。对每开U_n，整compact段包含于U_n时到其闭补集有正距离，因此该包含条件对(v,a)开放；R是Gδ、投影满S4。Jankov–von Neumann给universally measurable selector a(v)。在完成的球面概率σ上它可测，(v,t)→a(v)+tv在该完成测度与Leb_[0,1]的product上可测；推到Polish空间得到有限Radon概率与endpoint测度。无需a有界或有有限一阶矩。

这选的是G内线段，不冒选在任意非可测原K中。μ(G)=1正确，但不能声sptμ⊂G；闭support可包含G之外点。compact原K时可直接用其compact段关系作bounded Borel选择，并确有sptμ⊂K。任意集版本只需G为同维carrier，不假compact/full-D连续selector，也不改变原单位clock或方向law。

## 4. PSD矩阵、endpoint与DPR的准确结论

记x_v(t)=a(v)+tv，定义正测度与对称矩阵Radon测度

    μ(B)=∫_(S4)∫_0^1 1_B(x_v(t))dt dσ(v)，
    S(B)=∫_(S4)∫_0^1 1_B(x_v(t)) v⊗v dt dσ(v)。       (1)

它们有限且trace S=μ、μ(R5)=1、S(R5)=I5/5。对compactly supported光滑向量test直接沿t积分，按row-wise Div约定

    Div S=∫ v(δ_(a(v))−δ_(a(v)+v))dσ(v)，
    |Div S|(R5)≤2。                                (2)

a无界不妨碍该计算：test及其导数有界，积分质量有限。(2)一般不是零，不能假A-free。

源Remark1.3明确允许有限measure RHS，用(S,DivS)和零阶项扩展。更直接的Cor1.13已覆盖Div S为有限测度的矩阵S。对Div在Sym5的主符号为M↦Mξ，故

    Λ_Div={M∈Sym5:存在ξ≠0,Mξ=0}={det M=0}。

写S=M(x)μ，M为PSD且trace M=1，1/√5≤|M|_F≤1，因此μ与|S|等价，polar缩放不改rank。接受具名主定理后合法得到

    rank M(x)≤4，μ^s-a.e. x。                     (3)

可将联合访问law按位置disintegrate，M(x)=∫v⊗v dν_x(v)。若h<5，μ(G)=1使μ完全singular；(3)仍只是ν_x-a.e.方向落某个可能随x变化的4plane，不是矛盾、local rank1或dim_H μ≥5。

## 5. Normal-current入口不赠共同局部独立

源Th1.10的多个normal currents要求同一正测度被各自mass共同支配；其singular部分在同一codimension-one平面内。Cor1.12只有在d个一维normal currents的方向于同一测度a.e.张满R^d时才给绝对连续。§3证明确用有限boundary RHS、共同支配和同一点的linear span，不能换成全局方向总数。

本构造已有真实normal1-currents：把S的每行视为向量测度T_j，其mass有限、boundary由(2)的第j分量有限。若M在某同一正测度部分满秩，则这些行在那里共同支配该测度并独立，正好回到(3)的同一rank判据，而不是额外第5个方向。

把S4分成五个独立全局cones也只给五个位置测度μ_i及各自current；μ_i总质量正，不授它们有同一正质量的共同支配子测度。原full方向、pointΦ的全law和filled X不自动修这一点。把所需局部span／独立Alberti作新输入，已经把该候选最核心的责任假设进去；不能以来源Cor1.12的名称掩盖。

## 6. 两个精确校准：全局moment不等于局部rank

先用真正full方向、同一个compact K和全unit clock，而非自由matrix law。取K=closed B(0,1/2)，选l_v={tv:|t|≤1/2}。对x=rω≠0，(1)的trace测度为

    dμ(x)=2/(|S4| r⁴)·1_(0<r<1/2) dx，
    M(x)=ω⊗ω，rank M(x)=1。                       (4)

由polar坐标积分，μ总质量1，S总矩仍I5/5。各全局direction cones对应的位置主要在各自radial cones，并未在同一点产生五个独立law。这严格反full方向边际本身迫局部满秩；但μ是ac、K有正五维体积，不反任何small-deficit Kakeya/source命题。

再只校准“PDE＋full global moment”可真支持4维。令σ4为unit S4的概率面积，定义

    S_sph=(I−ω⊗ω)/4 ·σ4。

trace S_sph=σ4、rank=4、S_sph(R5)=I5/5。球面切向散度公式给Div S_sph=−ωσ4，是有限measure RHS。它具有真四维carrier并精确饱和(3)；局部切向方向作旋转不变平均也有全局uniform方向边际。但球面不含非平凡straight segment，这不是(1)的whole-line transport，更不是fullsource或Kakeya反例。两例各自的强弱范围不互换，也不把局部rank约束当完整方法不可能定理。

## 7. 联合Frostman、finite shadings与四维source出口

联合law Λ=(v,x_v(t))_#(σ×dt)有自动5-Frostman upper：joint r-ball限制v在球面r-cap，质量≤Cr4；每条unit段在physical r-ball内长≤2r，因此Λ(B_r)≤Cr5。位置边际则只自动有μ(B_r)≤2r，球bush在原点达到此尺度。联合维数5不在投影时免费保到μ，更不付原4维source与第5局部方向。

对一般marks，若以g_v(t)dt替整段，则Div S的积分分部含D_t g_v。任意可测g不保证BV，右端甚至未必是有限measure。即使每条几乎全长，删N个总长度1/N的微小interval，余集密度1−1/N而indicator variation为2N+O1，归一后的boundary也无统一upper；平均或逐管nearfull都不控制这个费用。有限δ时各固定图可能有有限边界，但δ→0的compactness／RHS总变差还须另付。

反过来保whole段并只调每label权，endpoint仍有限，却把support扩大到未marked的clock，不能说trace仍集中原小E。完整sticky finite E的filled X与ξ coherence不授BV向量场或共同normal3-current，也未给将(3)的可变kernel积分成固定4D carrier、保原N/I/clock再调DIR4的机制。故本轮合法来源调用尚无真实finite/shading正幂或Hausdorff>4返回。

## 8. 资格判定与停止范围

原compact全unit K的transport及任意K的同维Gδ carrier扩展合法，端点有限不阻来源调用；反向不能把标准singular-rank theorem说成已排source或Kakeya。当前只得(3)，全局PSD moment与联合Frostman均没有补局部ellipticity。标准normal-current/独立Alberti结论的前提尚未从原质量得到，不能以smoothξ、BV、共同支配或局部满秩公设结案。

因此目前无qualified阶段II gain候选，不以rank barrier、两校准或来源摘要单独冒完整主数学成功。四路保持，完整ordinary／general和sticky余branch未解；仅完成一次不同输入的资格核，不续R90polar/cut/cone、旧更多锚点、阈值或同义CP/PM/PW模板。未经外部同行评审，无newID/major/ordinary增益，Goal active。

本人施工不计自独审，等待root/B实际全文核及parent另锁；formal尚未授权。只写本A8，未spawn、Git、metadata或下载，未预认证未来文献计数／档案／同步，也未将没有合格候选说成external blocker。
