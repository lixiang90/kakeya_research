# 文献库

原文存 `primary/`，提取文本存 `extracted/`，元数据存 `metadata/`。

核心输入 OAI-4D-20260924：本地 `paper.pdf` 原样复制为 `primary/openai_2026_four_dimensional_kakeya.pdf`，175页。官方Git对象SHA-1与本地 `git hash-object` 均为 `45ec20e423db2a9c70fd6303510bac361e6e9e8a`，字节数均为1371486。SHA256为 `30d0c186aa9c697d02ab9bf736968028f1ce8a2f164f1d7291398d530035ccde`。

身份/版本匹配不等于证明正确性核验。原Theorem1.1的完整内部argument已由R30–38在明列高级输入下双审；未独证全部外部高级文献或原§11所有推论。

引用论文时使用稳定文献ID，写出定理/引理编号与页码。不同版本不得悄然替换：升级时保存新文件并记录编号变动。下载失败的条目只记元数据，不能标记为本地全文。

查找：`rg -n 'Lemma 6.6|Projection to four|weighted.*plank' literature/extracted`。

R0007新增 `guth_2025_kakeya_introduction_v1.pdf`（21页，原PDF与全文均保存）；其p.20的quadric数字与Zahl综述§4.1分开记录，见 `notes/10_source_audit/R0007_quadric_source_discrepancy.md`。可调用的全框cap与加权反例采用本轮自包含证明，不依赖未经核验的更强文献措辞。

R0011新增第8篇PDF：Nadjimzadah-curved-lifting-2026v1，`primary/nadjimzadah_2026_curved_to_linear_lifting_v1.pdf`，15页、961012字节；提取全文与版本/校验元数据分别存extracted、metadata同名前缀。读过Definition 2.1、Propositions 2.2/2.5及相关证明和§6；不是全文独立重证。其lifting由高维直线输入推出低维曲线结论，未提供逆向五维约化。具体下一项检验见 `notes/20_dimension_lifting/curved_lifting/R0011_source_and_next_test.md`。R0010的abstract-only检索记录保留为当时状态，不追溯改写。

R0012无新增PDF，仍为8篇。新增阅读包括Wang–Zakharov §2.3/§17的高维sticky配置、HRZ Theorem4.1与Proposition4.2、Zahl综述§4.3–4.4；精确阅读范围与web-only候选存 `metadata/R0012_source_check.json`。有限检索不用于认证新颖性。新主任务转向真实R5管的三平面窄端点，未将sticky配置假设免费赋给一般方向分离管。

R0013新增3篇，现共11篇PDF：Kulkarni-2024-planebrush-thesis（66页）、Katz-Zahl-2019-planebrush-v3（40页）和Fassler-Orponen-horizontal-SL2-2022v1（7页）。每篇原文、全文提取、SHA256和精确read_scope/proof_status均已存档。KZ v3修正旧Lemma7.1后maximal约3.049与Hausdorff约3.059不可混淆。Kulkarni Prop18打印证明的具体待补证位置见R0013_primary_narrow_audit.md，不标整定理verified。FO单块定理不是共享时间两块耦合或任意dense shading定理。metadata/R0013_source_check.json记录本轮范围，未作穷尽前沿或新颖性认证。

R0014新增4篇，现共15篇PDF：GGW2211.09508v2、CSWZ2610.13682v1（2026-10-09）、Du2510.16671v2、Gan2308.07675v2。前缀均以R0014_开头，原PDF/全文/metadata一一对应；SHA256、版本和精确阅读范围可查。确有finite/shading定理，但本联合family的Grassmann rank、model-hyperplane/pencil或无子空间塌缩假设不合；未凭标题当CP输入。详见metadata/R0014_source_check.json及R0014_primary_projection_audit.md，未认证穷尽前沿或新颖性。

R0015新增2篇，现共17篇PDF：He1611.09639v2（29页）与He–de Saxcé1806.06375v3（23页），均以R0015_前缀存原PDF、全文和来源/校验元数据。读Theorems2/3与表示版本Theorems2.3/2.4、Prop2.5等明确假设；未将实际L-tuples的matrix作用免费当其输入，未重证全文。Wang–Zakharov真实d5/k=ell3矩阵分支的精确source阅读范围见metadata/R0015_source_check.json。

R0016新增Shmerkin2308.09846v3（19页），现共18篇PDF。原PDF、全文、SHA256、版本及精确read_scope均已保存。仅核Theorems1.2/1.5与Section4.3的声明/接口，未重证全文；其固定porosity应用不能直接套用原delta^-eta常数，未据此闭合一般矩阵分支。实际有限图直线分支使用Wang–Zakharov Theorem13.5，仍显式依赖该既有标量输入。

R0017无新增PDF，仍18篇。补读Wang–Zakharov §19.1(148)–(152)、§21 Theorem21.2/Remark21.3及§22方法范围，精确记录metadata/R0017_source_check.json；未据ambient extension假设vector multiplier，未验证全文或声称已有新向量和积输入。

R0018新增Hochman1503.09043v2（98页，官方版本2017-06-05），现19篇PDF。已保存原PDF、全文、bytes/SHA256与metadata；选读Defs2.1-2.6、Theorem2.8/Remark2.9、Theorem2.14及§4.6最后证明步，PDF19图已核，未全文重证。Theorem2.8要求独立卷积小熵增长，不能由原受限W图小像直接调用；common V_i只在每层公共，不是全局平面。source支持R依赖有核；具体W归一frame已bounded。source§22.4读到scalar恢复/convex-Wolff终步，用于下一mixed42候选，未宣称已推广。详细范围metadata/R0018_source_check.json。

R0019无新PDF，仍19篇。补核GGW2211.09508v2 Theorem2.1（PDF3图）和GWZ2601.14411v2 Definitions3.1–3.5/Lemma3.7（PDF7图），原权全局投影实际用后者，未重跑完整证明或Lean。WZ2609.22035v1 §19/21/22的量词、三维horizontal原质量和PDF98–99逐算式审查存metadata/R0019_source_check.json；(192)后过强指数已有保守修复，不是四维定理反驳。官方版本2026-10-17复核GGW仍v2、GWZ仍v2（Oct11）、WZ仍v1，未声称穷尽前沿/认证新颖性。

R0020无新PDF，仍19篇，无新在线版本声明。补读WZ Def3.9/map(20)/Obs3.2–3.4及实际配置点AD、degree、marks尺度，直接重算五维parent抵消和投影端点，不把印刷R3声明免费当任意维定理。GWZ Lemma3.7的density门槛另有自包含bush校准。精确范围metadata/R0020_source_check.json；未重证全文，没有完整mixed分支或维数结果。

R0021无新PDF，仍19篇。重核WZ Def17.3/17.4的physical tube-KT baseδ、19.4的cluster/CW范围及22.1/22.4计数；vector polynomial机制采用自包含PCT，不声称source已有向量quadratic定理。原21.1印刷all-scale声明和fixed-scale全局准备责任分开。官方arXiv history本日仍仅v1；有限一手检索空结果不认证新颖性。精确read/search scope见metadata/R0021_source_check.json。

R0022无新PDF，仍19篇，无新在线版本声明。逐核原W/observed A/B与scalarABC，PDF78/91/92已渲染并核符号、两个η参数和同步L_f；局部可修的错配不反源主定理。实际fixedρ准备以自包含time closure/rich triples及named21.2/19.2支付，不靠allscale形式否定。22.5仅为下一vector非二次目标选读，未称已推广。read/视觉核边界见metadata/R0022_source_check.json。

R0033新增3篇2026 primary PDF，共23篇：Choudhuri2610.12480v1(19页)、Moreira2610.06181v1(25页)、Hua–Yao–Yang2608.18693v2(39页)，原PDF/全文/单篇metadata均保存，pdfinfo/bytesSHA256/首页视觉核通过。Choudhuri primary/bannerAug30与PDFtitleOct12日期异常原样记录；HYY v1/v2题名及scope不混。仅读声明/所列scope，不认证全文或把它们当新高维input。官方OAI4本日目录同PDFblob/bytes，README/history/formalization目录状态已核但不等于proof正确性。原2.7/2.13/2.15–2.16、4.1–4.3与companionweighted直接链本轮内部重证，保GWZ set namedinput，详细metadata/R0033_source_check.json。有限前沿一手复核不认证六维17/4新颖性。

R0034无新PDF，仍23篇；无新online版本/前沿声明，最后onlinecheck保R33。实读原2.11有限预算及4.4–4.12完整statement/proof（PDF50–70），52/53/68图核；guard是2^((M_path+n)^2)，extract上标丢失不可误读quadratic。AIM001完整conversion在原假设/明列inputs下双独审通过；每residual真实candidate存在/后续branches未付，详细metadata/R0034_source_check.json。

R0035新增Wang–Zahl2210.09581v2（69页）与Carbery–Valdimarsson1205.6371v1（20页），共25PDF/28sources。原PDF/全文/单篇版本、bytesSHA256、statement/read_scope均存档；WZ Def4.2 upper-only AD/Thm5.2 every-restricted-triple及§8重述，CV Thm1 weighted doubly-infinite straight tubes/determinant逐核，相关17/31/2页图核。两个外部高级定理全proof保namedinput，未独证全文。原OAI4 PDF70–108完整isotropic链实读；97页A0^{-1}u上标图核正确，txt串行不可当源笔误。完整scope见metadata/R0035_source_check.json，源全文/无条件高维/新颖性仍未认证。

R0036无新PDF，仍25PDF/28sources；补入官方07-finite-narrowness.tex与09-unbounded-narrowness.tex且Gitblob/bytesSHA256核一致，partial源码状态保持。完整原8.2及§10 ℓ∞排除通过内部双全文独审；120/121/163/166页图核。官方paper同blob/bytes仅证明身份。新增Gan旧v2的2026出版、Germain–Latocca cylinder及Tang volumeclaim仅web-primary筛查，明确未下载PDF/不作advancedinput；具体scope与直接反证见metadata/R0036_source_check.json及B宏观稿。未认证positivefinite分支、全源或17/4优先权。


R0037新增OSS2309.03068v2（26页411743bytes，SHA25652342022c2d36a84222fedff2d1f94856ab7fd1e1e58973bd03676194037cab7），原PDF/全文/metadata保存，现26PDF/29sources。single-scale smoothedenergy Th1.5及原7.4实际应用核，PDF2图核，wholeadvancedproof具名；不查证期刊状态/不称新高维input。补exact06a-retained-edge.tex与08-critical-rates.tex并核Gitblob/bytes/SHA256；原§7–9全finite branch双全文独审通过FIN001，仍非fullsource/无条件新维数。PDF140/141/148/149图核，s_b=3/2不是text提取32；精确范围metadata/R0037_source_check.json。


R0038无新PDF，仍26PDF/29sources。新增exact官方02-framework.tex（65440bytes，Gitblob2cb57ede9ff053e9b3deadab92bfa544c10beb2f，SHA25653e11aade386a455e99202bb8fad6421789ee40644b80c0971c9b4b1daf648cc）。完整2.17、全部内部argument拼接、finite初始化/平均shading/KT及任意集合Hausdorff读出在具名输入下双全文独审通过RED001。实看OAI4 PDF24/25、GWZ2、KT19。原175页包含外部高级proof与§11全部推论的广义全认证不作宣称；G/KT等wholeadvancedproof与2026新颖性仍分列责任，详见metadata/R0038_source_check.json。


R0039宏观新增4篇primary PDF/全文/逐篇metadata：LPSW2610.10603v1(156p)、FernandezDelgado–deLaSalle2607.14824v3(25p)、Pohoata–Zakharov2411.13395v1(10p)、Tao2511.15135v1(实际19p，abs comments18p照录)。现30PDF/33catalog条目。LPSW4/148、FD2、PZ2、Tao2已实看，只核所列statement/scope；未全文独证。LPSW17.3/4为新codim2plank输入，非ordinarylineK；FD只有log体积衰减，PZ disks/Minkowski及Tao privatecommunication不冒六维新界。metadata/R0039_source_check.json保存版本/范围、额外web-primary与priority限制。


R0040无新增PDF，仍30PDF/33catalog来源。局部版本化primary细读WZ17/19/20、LPSW§9与FD5.4 scope；实看WZ65/78、LPSW61/62、FD18/19。Mat entries[-1,1]为原定义而非额外假设。只具名调用19.2，不认证全advancedproof；本轮未重新做online latest-version认证。


R0041仍30PDF/33sources，无新下载。FD2607.14824v3相关construction PDF6–19及root1–19/Appendixscope细读，实看13/15/17，18/19此前已看复用。仅versioned primary scope，无新online latest认证；Fourier应用未全审。原5.4现成compact桥保power输入，不把原log输出误升power。


R0042新增BS2609.24135v1（9页），现31PDF/34来源；原PDF、全文、版本/SHA256保存同stem。root全文读并实看1/2/6/7/8，Theorem1的λ任意正，与旧Conjectureλ≥δ分开；semialgebraic固定ambient poly(E)预算明确，#o-minimal高级依赖仍具名。v1/HTML dateSep21、PDFtitle dateSep22均保真。有限primary前沿/六维对照及精确scope见metadata/R0042_source_check.json，不认证穷尽/优先权或ordinary高维新界。


R0043仍31PDF/34sources，无新PDF或在线版次认证；versioned WZ2609.22035v1整§17–18及(19)/(20)/Obs3.2–3.4实际细读，root实看PDF18/69/72/74/76、A70/72。新增PW粗化传播独立证明，原其余结构推导仍具名；PDF70/72的ΔJ/√δell记号不一致如实保存，不据此宣源主定理反例。精确scope见metadata/R0043_source_check.json，最新onlinefrontier仍R42。


R0044仍31PDF/34sources，无新PDF/渲染/online版次认证；实际读WZ Def17.2–17.4、§19.1 goodq/coherence、19.2及20.2，沿用R16独立计数与R42/43 PW输入。scope见metadata/R0044_source_check.json，最新onlinefrontier仍R42。下一Kakeya–BL调用前须先核一手精确版本，本轮未调用未经核定理。


R0045新增Zorin-Kranich1807.09604v4与Zhang2608.17952v2两PDF/text/meta，库33PDF/36sources。精确scope/hash及读页见metadata/R0045_source_check.json。仅新输入版本/适用性有限online核查，非全前沿或priority认证。ZK1.5用于selectedtuples，whole高级proof具名；新Zhang仅为下一fixed rational mixednorm输入，q趋1及Hausdorff附录完整proof未独审，不把perturbed mixednorm当定理。


R0046沿用33PDF/36sources，无新增PDF；Zhang2608.17952v2的§§2–4/旧四环及uniform tensor scope、FD2607.14824v3 Prop5.4 finite-to-compact κ/4量词与本地原finite种子重核，A有限官方HTML对照，非全局版本/前沿/优先权认证。详metadata/R0046_source_check.json。


R0047无新增PDF，仍33PDF/36sources。A有限比对FD2607.14824v3、Zhang2608.17952v2官方exact页与本地对象；未找到可直接填一般cyclic closed-loop估计的已读primary，但不认证无已有式/novelty。root仅为下一gate定位读HRZ1908.05589v1 PDF1–3/目录，未审actualterminal，不把2019历史指数表当2026前沿。R48须先周期macro/有限primaryfrontier核。详metadata/R0047_source_check.json。


R0048 boundedprimaryfrontier/version审：OAI当前official tree核paper.pdf同blob45ec20e.../1371486；HRZ2022发表/机构accepted URL及JHU官方43页文本已读，关键§4/§8对应，本地v1PDF34亦实际视觉核。v1历史4D表1.4794与JHU1.4854有别，非wholebytes同。Edinburgh/JHU下载Win10013/HTTP403，无新offlinePDFbytes/hash，仍33PDF/36sources。详metadata/R0048_source_check.json及notes/00_map/R0048_primary_frontier_and_recursive_input_audit.md；有限检索非first/best认证。


R0049新增Fu–Gan2009.09108v2，公开原PDF208052bytes/14页与提取文本、来源hash齐存，root/A读1–5、root第一页视觉核；boundaryHolder或W1p/continuous假设仅作macro候选，不供roughfinite桥。现34PDF/37sources。WZ2025v2PDF13(3.5)outer责任及localonecall修复、当前v2/AMS未读刊本边界、WZ2026真实AD极值类详metadata/R0049_source_check.json。lifting2609.06299v1与Bourgaincondition2511.10918/GAFA00750-4明确不同，不混版本或证明输入。


R0050无新PDF，仍34PDF/37sources。实际重读lifting2609.06299v1的定义/forwardproof/标准rank构造和旧三稿，完成LIFT005同P全时变分范围纠正；有界primary术语比对不认证新颖性或全局priority。源最新版本沿R49核查，不虚报本轮重新核版本；详metadata/R0050_source_check.json。


R0051新增JingWu2608.11726v1(14页)、GGNSZ2607.27629v1(90页)、官方OAI3D maximal Sept23(97页，同blob已核)、GGSWT2511.02864v3(81页)四PDF及提取文本/字节hash/firstpage视觉核，现38PDF/40sources。仅读所列接口，非全文proof认证；GGSWT报1.668的strict有限有理law尚未项目独核。来源/实际阅读/三种geometry与算术候选责任详metadata/R0051_source_check.json。


R0052保存官方alphaevolve_repository_of_problems的两原始ipynb（5656/27270bytes）、固定tree/blob/SHA256及Apache2许可/署名于source_code，未执行。两本没有原SD1.668可直接复现law；本项目另独立Q12 weighted反例只反R46，不能回填为来源强下界证书。38PDF/40sources保持，详metadata/R0052_source_check.json。


R0053 targeted复核官方3D M3当前Git tree链与库存PDFfa215607/925416一致，实读Th1.1/§10.2归一与可测/端点接口；97页全proof未独证。无新PDF/source，38/40保持。Q3transfer/equivalence与canonical near-P packet只作为具名输入应用，详metadata/R0053_source_check.json。


R0054无新增文献与高级证明输入。当前模型由自含平面weighted L2闭合；为下一G3只重读本地HRZ Def5.1/5.2/(29)、alg1和vanishing接口，非新版本或全球前沿核查。38PDF/40sources，详metadata/R0054_source_check.json。


R0055新增6个原PDF版本：KR v2/v3分存（v3为实际当前主版本）、Zahl1908.05314v4、DiPlinio–Parissis1807.08255v2、Hua–Yang2608.18870v4、Germain–Latocca2606.29993v1。44PDF/45sources，原bytes/SHA256/gitblob/页数和实际readscope分别入metadata；高级wholeproof未认证。KR source counting/choice、HY既有parent条件与GL kinetic指数的范围不能被当一般G3/n5增益，详metadata/R0055_source_check.json。


R0056新增4份primary原PDF：官方elliptic103页（onlyS2/R3，Th2.2为2D all-s conditional ellipse传播）、Dvir作者April2008版5页、DKSS作者May11,2009版26页、HR1807.10940v3 43页。48PDF/49sources，逐份原bytes/hash/gitblob/readscope在metadata；作者版不称arxiv同bytes，后两篇高级未读部分不认证。官方OAI4/M3本轮fresh树的PDF blob仍同存档。
