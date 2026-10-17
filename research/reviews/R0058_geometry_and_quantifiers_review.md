# R0058：原割线门槛、严格反攻与后继范围独审

2026-10-17，B。已实际全文读取修后root主稿10节、A主稿11节、B主稿8节、macro6节、next6节及working_spec7节；另实际读取已存Wang–Zakharov原PDF3–4对应文本。以下是对root/A的独立逐步审查；B自身反攻的自审不替代另一代理独审。未经外部同行评审，不预认证尚未写入的metadata、registry或Git同步。

## 1. 实际源接口、排重与量词

通过当前有限门槛的scope。common-kernel形式F=F0+u eᵀ、二维非共线u确不由R16的PENCIL/IMAGE直接覆盖；固定角差后平移为二维曲线，标量投影Y不继承二维亏损。root/A保留原reference ν²×原used-angle-pair及任意相关0≤g≤1，没有把g的条件边缘改为独立。A§3仍把R16提取、重数、粗化和SM回传作为既有已审工具，不冒本轮重新证明完整Def17配置。

本轮实际选择在spec§7锁定，是slab非集中与standalone二维预处理反攻；不是完整common-kernel排除，不是CP/PM改名。完整普通五维及general-to-sticky缺口均保留。

## 2. 非零offset：双anchor及floor独核

通过root§§2–3及A§7。对称事件的CS确给p²≤共同neighbor平均。删近anchor费用是CK max(ξ,r)，保留原标签重数。两个方程消去v(z)的精确符号为

    A(t1−z)(t2−z)−c(t2−t1)
      =ε1(t2−z)−ε2(t1−z)。

在|t1−t2|≥ξ且|c|ξ≫ε时，共同neighbor强迫|A|≥c|c|ξ；随后monic二次sublevel总长度≤C√(ε/(|c|ξ))。至多两个interval的r-floor费用已计入。取ξ=max(r,C(ε/|c|)^(1/3))，两种分支均得到p²≤CK[(ε/|c|)^(1/3)+r]，开平方是所写1/6指数；大ratio由trivial1处理。不需要u可微、单射或曲率，不对无限slabs作union。

对D=θQ固定原θ后，ε与c同比缩放，比值不变；θ=0在|c|>ε时不贡献，其余为trivial范围。原θ须在reference中独立于原times，g无须独立。root/A没有在按g删选后再次假独立。

## 3. 近零offset：同原g、两端同片及真实分母

通过root§4与A§§8–9。小θ和小时差的查询都在原floor以上，其删除费用分别由原slab cap及interval cap付清。余边使两个v值接近；固定邻格clusters覆盖边、每个label有固定重数。由ΣP≤C、ΣH≥cσ、H≤P²选出H≥cσP，确有P≥cσ、H≥cσ²、H/P²≥cσ。保留的是原绝对质量，若σ=mp，不能改写成cp²或免费保m。auxiliary原权、输出事件和两端同一时间片均保留。

条件time cap及SM命中分母需付P⁻¹；本结论只有平均incidence闭包，未提供逐管密度。所选u像宽Cε^(a/2)远可大于r，不能直接套R16的O(r)linewise稳定版本。B§7独立简式也已明确D0≥CKt r，保证其g0查询合法；较小质量不声称该floor以下的删除式。

## 4. Plateau/Cantor真实分解反攻与任意删选上限

通过root§§5–9与B对应有限证明的数学链。原B保全部左半cell细δ网，是真1AD；hδ连续uniform-Lip且距t²为O(ρ)。d>a及d>e使全实矩阵affine-fit和任意空间coarse-line条件分别归为统一二次sublevel，常数不依所拟合系数。单个平台的固定正幂质量不成为subpower片。

固定平台对严格给Q=(z²,c_jk z)，故全pairs的cover≤Cδ⁻¹ρ⁻²。原Cantor product H为fixed κ-AD、γ-slab，ordered差保原重数；θ支持≤3^L只用signed-digit表示数量上界，不需要唯一表示或省略进位。D=θQ仍是真矩阵乘法，cover exponent β=1+2d+log_M3<2。root选值给β<1.225，小于2−κ。

任意positive normalized measure只要支撑未离开该全support，就需K′≥cδ^{−(2−ζ−β)+o(1)}；未归一化版本质量≤CK′δ^{2−ζ−β+o(1)}。此结论强于dominated restriction，相关删选不能增加support。反攻没有构造A_±、tube-KT输入或dense输出g，也没有实际整管AD/CW与ξ相容；明确不反完整source或Kakeya。

## 5. 容量与四维quotient的必要范围

通过A§10的有限条件计算及root§10边界。二维Frostman并非双椭圆capacity必要条件；A所列独立Y/Q all-scale假设下的W比值代数正确，但本轮粗精度slab alternative不自动供给它。A已区分conditional time profile s_θ和global support exponent t_θ，未把二者相等，也未把source保证的q当最优q上限。仅用所写θ-clock及已知保证指数作矛盾，κ<1/3的乐观预算仍不足；这不排其他变量或更强joint机制。

实际重读WZ PDF4确认：文献明确陈述一般R4 CWalone管族可有quadric浓集、union≲δ^(1/2)。因此quotient只付凸棱柱CW不能调用任意R4全union定理；OAI4 Hausdorff也不补joint3-AD或方向prior。此处只认证所读文献陈述及应用范围，没有重新独立构造该quadric族。

## 6. 结论、宏观停止与后继

修后root/A的上述证明及macro/next范围通过本次独立审查。已得的是非零slab upper、近零同原g片，以及保matrix–time–angle分解的严格standalone二维预处理反攻。无完整common-kernel排除、无普通高维维数界，不新增数学ID或重大／新颖认证。

next未把R59预定理列为已证；若续common-kernel，必须真正使用原A-D输出关联、wholeline/ξ或另一个已付metric，而非续调plateau/Cantor/offset、增添2Fst公设或重开旧Y-only。nearline粗化仍是待付接口。Goal active；本轮独审完成后停止编辑与检索，由root统一归档验证和同步。
