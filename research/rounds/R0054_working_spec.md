# R0054 working specification：先核五维共同因子模型的低维闭包

2026-10-17，Goal active。上一turn progress：R53真实几何应用、等价纠偏与完整同步。已context.py→tmp/R0054_context.txt，GOAL/STATE/ROADMAP/AGENTS/registry78全部状态/最近R53round/next/receipt实际恢复；HEAD=origin=remote4f9dee742e86c2110dd85ce18c30b55960cf22a6/tree0bc3b7c4acbee0bf020e9e46435a4a577e5d0c45/800files/clean。本spec先于正式研究稿/独审登记；宏观完成后不再续共同因子维数模板。

## 1. 长期目标和唯一当前问题

一般n≥5欧氏Kakeya未解。只完成一次上一spec指定的真实R5模型检查，先检验是否已被更低维旧工具闭合，避免将toy序列当独立方向。Z={x4=x1x2,x5=x1x3}，原unit axes a+tv（|v|=1、|t|≤1/2）在B10、逐点距Z≤Cδ；半径δ的T5、原非负权W、physical S4的C0δ帽权≤α，可测Y_i⊂T_i，E=∪Y_i，原avg λ=Σw|Y|/Σw|T|。

原目标∀ε>0有|E|≥cε,C δε λ³δ⁴W/α。优先反攻更强且可能为已知平面闭包的λ²/log：|E|≥cC λ²δ⁴W/[α log(2/δ)]。常数不依δ/λ/族数/权跨度，不预认证。

## 2. 闭包、拟证几何和全部预算

whole-axis近图先给两二次poly coefficients：|v1v2|,|v1v3|≤Kδ，v4−a1v2−a2v1、v5−a1v3−a3v1≤Kδ。先核|π123v|有固定正下界。若此与unitnorm迫(v1=Oδ)或(v2,v3=Oδ)两支，则不必用全dyadic h。

第一支midpoint a1分δ格，原轴近2D平面{x1=b,x4=b x2,x5=b x3}；第二支midpoint(a2,a3)分δ格，原轴近1D直线{x2=b2,x3=b3,x4=b2 x1,x5=b3 x1}。必须实际证Oδ距、原方向cap、端帽/actual E的有界空间overlap；逐管Oδ snapping若成立要完整，不类比R53抛物柱面√δ例。

第一支拟用自含平面两管intersection面积≤Cδ²/(δ+angle)的dyadic帽求和→weighted L2 overlap，再用3维normal-fiber f=δ^-3∫1_E≤C和原incidence CS；第二支同packet方向近单一轴则W_j≤Cα，|E_j|≥I_j/W_j。两支/所有包须保原W/I，平均/逐管闭包分别核，不以heavy多损密度。

## 3. 反例、独立审查及数学结果层次

反攻中间|v1|尺度、sign/极小v1/不等v2v3、原非均匀权、重合管、λ≪δ、帽角antipodal、单位clock和端帽、两方程仅nearzero与near图的区别。完整proof或合法反例才登记内部reviewed。有限计算不得替连续估计。

root主证明/整合/meta/Git。A仅notes/40_multiscale/R0054_planar_overlap_and_original_density_audit.md与research/reviews/R0054_planar_and_density_review.md：独立planar overlap/原f/平均密度及宏观来源scope。B仅notes/40_multiscale/R0054_common_factor_ruling_and_counteraudit.md与research/reviews/R0054_geometry_and_closure_review.md：独立两支/近叶片/snapping/真实方向/物理overlap和反例。至多两代理，不spawn/Git/改他人文件。formal6节须root/A/B/macro/next齐后actual全文审。

## 4. 一轮停止及宏观纠偏

若模型已为平面/直线闭包，不新增数学ID、不称M3新应用方向/高维增益；完整归档已付原几何后立即冻结整个共同因子模板，不续更多输出/ambient/rank/系数小改。比较至少三条实际高维机制，下一只选真实一般n5缺口或有新输入的实质关键路径；不能紧接再选另一个容易的quadric toy。

普通高维Hausdorff/full maximal/finite single-scale区别保持，DIM001条件17/4不升级priority/major。R46反例及R50/R49/R48等冻结保scope。下一常规macro不迟于R55，当前低维闭包成立则本轮提前macro。未经外部同行评审，长期Goal不降低。

## 5. 持久化和安全同步

保存主稿/独审/失败、source说明与macro/下一唯一spec，更新STATE/路线/registry78现有audit，不为闭包新立ID。必要验证后沿R53父按PROTOCOL精确blob/tree/commit/leasedref forcefalse同步；canonical同commit/fulltree/每blobSHA256/clean回执核才闭轮。同步失败保本地并记录原因，继续可做数学，Goal active。
