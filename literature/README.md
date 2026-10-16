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
