# 文献库

原文存 `primary/`，提取文本存 `extracted/`，元数据存 `metadata/`。

核心输入 OAI-4D-20260924：本地 `paper.pdf` 原样复制为 `primary/openai_2026_four_dimensional_kakeya.pdf`，175页。官方Git对象SHA-1与本地 `git hash-object` 均为 `45ec20e423db2a9c70fd6303510bac361e6e9e8a`，字节数均为1371486。SHA256为 `30d0c186aa9c697d02ab9bf736968028f1ce8a2f164f1d7291398d530035ccde`。

身份/版本匹配不等于证明正确性核验。175页全文尚未完成独立审查。

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
