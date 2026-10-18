# R0084：真实凸分解的多项式计数闭包与五维遮罩输入门

2026-10-18，root。Phase I应用稿已由root/A/B与两formal实际全文cross，限定通过；不新增ID、普通高维界、major或新颖性声明，未经外部同行评审。

## 1. 对象与先锁

固定n≥5，优先n5，0<δ<1/100，原单位δ管T⊂B_R（R固定），N=#T，等体积u≈δ^(n−1)。可测Y(T)⊂T，I=Σ|Y(T)|，λ=I/(Nu)>0，E=∪Y(T)。原方向δ分离，或显式给每个固定复杂度D半代数W的完整包含计数 #T[W]≤A_D δ^(1−n)|W|；normalized常数K_D=A_D δ^(1−n)/N不得省略。ordinary满方向网N≈δ^(1−n)时K_D才可常数。若改为无N上界的任意indexed输入，L必须保留logN，不能免费称polylog(1/δ)；普通方向分离族有N≲δ^(1−n)。保原N、I、E，目标先核真实factoring closure；没有预设成功gain的phaseII。

## 2. 来源与partition的准确范围

新实读Hong Wang ICM2026 §6 Lem6.10只作检索入口；实际数学采用已存GWZ2601.14411v2 §4 Lem4.1完整greedy proof。它在Rn选近等尺寸parents P，并给真正assigned partition T′=⊔_P T_P，T⊂P；每T_P relative convexFW≤L，parent absolute convexKT≤L。再分层令#m_P≈m、parent体积≈v，N′≈mM，M=#P。L包括所有明确的polylog费用。assigned partition不声称每根几何上只含于O1 parents，亦不把T_P当全部T′[P]。GWZ source高级全部proof/Lean未在本轮重证。

## 3. 平均密度先转逐管，保原质量

删密度<λ/2的管至多损I/2，剩余分O(log(2/λ))个dyadic密度层。选层逐管密度θ至2θ、I0≥I/(2Lλ)，并有N0≥λN/(2Lλ)。先对该层真factoring及uniformm分层，只损polylog数量L0；由于逐管密度同层，保留I′≥I0/(2L0)，故I′≥I/polylog，N′≥λN/polylog。E′⊂E且原shadings未填充。若λ≥δ^η，费用才为δ^−O(η)polylog；平均与逐管闭包分开，绝不把incidence保留当parent逐管密度。

## 4. 父体积和bounded ambient的独立账本

采用GWZ greedy时可把maximizer取为其assigned children凸包，所以parents可在原B_R。若只用relativeFW黑箱，不预设这项：query P∩B_R包含全部T_P，故|P∩B_R|≥v/L。沿diameter方向的截面A(t)，Brunn–Minkowski凹性/两端cone给v≥diam(P) supA/n；交B_R长度≤2R给|P∩B_R|≤2R supA，合得diamP≤2nRL。P含至少一个原T，故P⊂B_(R+2nRL)。query该球的parent absolute convexKT，Mv≤L^O_n(1)。这只用convex计数，未假parents是圆管。

## 5. 完整包含PW上下两个方向的实际证明

对任意复杂度D半代数W，m #P[W]≲Σ_(P⊂W)#T_P≤#T′[W]≤A_D δ^(1−n)|W|。由mM≈N′得到parent normalized系数≲K_D N/N′；再乘Mv≤L^O_n，得到parent absolute系数≲K_D(N/N′)L^O_n乘|W|/v。对每P取任意可逆仿射F_P使|F_P(P)|=1。若A是同复杂度测试集，则|F_P^-1 A|=v|A|且child fullcontainment数≤A_D δ^(1−n)v|A|；除m并用v/m≈Mv/N′，normalized系数同样≤K_D(N/N′)L^O_n。这是实测同一原PW输入的ratio应用，仿射保复杂度，不声称images是各向同性δ管。

## 6. partial PW与旧R43不能混同

上述证明只用全包含。若不同parents的John shape/orientation不同，不能将q_P(W)=|P∩W|/|P|大于τ换成P⊂W，亦不能免费给partial-shading PW。若全parents共用同一对称盒E的平移，则T⊂P给μ_P≤C μ_T*k_(CE)，平均assigned children、用R43 restricted-mean/common translation核已经支付完整PW；这只是旧机制。variable kernels的统一sharp上界本轮既未证也未否，不能新命名成PW4增益。任意再次restriction须按新N重算normalized常数；shadow restriction另算λ，原绝对计数则继承。

## 7. 真正Rn−1责任及四维输入不匹配

Root实际读GWZ §5 Prop5.1完整proof、Rem5.2/5.10、Lem5.8/5.9：R3 parent shading Y_P=P∩N_(w1)(∪Y(T_P))的λ_parent≳C^-1 λ_child²来自平面Córdoba估计；Rem5.2明说高维需Rn−1适当Kakeya输入。它没有给一般Rn凸parent同结论。另一方面GWZ Lem5.11同轴round coarse-tube用直接体积比较即保parent density≳λ，不需新增FW；这一正面特殊形状与R43已付coarsening一致，不能推广为任意各向异性parent。n5初始圆管增厚w1后投影可成R4的w1管，但原δ方向分离一般只给projected w1帽≤C(w1/δ)^4原labels；除m和归一各向异性parent仍有必须付的v/scale/cap。一般递归convex children更有不同短轴。relativeCW或本节containmentPW不等于DIR003的实际4D slope-bin cap/round model；OAI4 Th1.1为Hausdorff结论，不能换成任意PW4全λ maximal。特殊slab可较好不证明一般parent。

## 8. 独立反攻、排重与停止

R43已保共同核coarsening，R53–55已算projection cap/原mass费用，R62任意PW4转DIR被冻结；本轮真实max-density factoring没有付这些缺口，所以不以不同名字重开。来源R4 CWalone的quadric obstruction只反过强CW替换，不反普通δ-dirsep或完整Kakeya；单quadricKT与many-quadrics normalizedCW的分母不混。未构造变量核closure的严格反例，也未证明该closure。拒phaseII；保守no-newdim/branchsaving streak7，不以该初等应用降Goal。

## 9. 实际读取与后继

Root本轮实际完整GWZ Lem4.1/Remark4.2–4.3与§5完整proof；R43完整10节、R55原projection ledger实际读，R40只相关摘读不称全文。OAI4 introTh1.1/§1.1与既有DIR003范围核，不重新认证175页高级proof。HongWang官方HTML和web PDF parsed页12–13核文本；本机PDF下载403/截图cache miss，无原PDF/visual本地验证。全文cross与macro已完成，只保输入门事实；下轮须完整四路径重新选实机制，不续genericfactoring/desiredparentdensity/PW4换名。
