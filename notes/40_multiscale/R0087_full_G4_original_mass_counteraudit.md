# R0087：全 G4 的原质量、退化几何与具体桥反攻

2026-10-18，B。仅编辑本分配稿，无 Git、metadata、下载或新代理操作。本文不声 G4 已证或已否；具体桥的失败与全类反例严格区分，未经外部同行评审。

## 1. 完整原命题与实际恢复范围

实际读 R87 working_spec5、当前 STATE、R86 next6、R85 root10，以及 R60 fullG3 的完整输入和相应原质量接口；此前已读的 GOAL、ROADMAP 和78状态按同会话恢复。原全 G4 固定 D,R,C,C₀，允许 degree≤D 的非零实 P=Pδ 任意依赖δ，系数ℓ¹归一为1。原 unit round δ-tubes 的整个轴均在 B_R∩N_(Cδ)Z(P)，权和W、每个 physical C₀δ方向帽权≤α。逐管 marks |Y_i|≥δ^η Vδ，目标

\[
|E|=|\bigcup_iY_i|\ge c\delta^{4+\varepsilon}W/\alpha.
\tag{1}
\]

η必须由ε及固定格式选择，uniform于P的系数条件数和所有原权。不能把 |P| 小、远离 singular locus、physical regularity、固定 leading gradient 或 exact-line 选择加成免费假设。R53/R54/R85既有具体模型不作新的主成果；R61/R62 PW4等价也不以新名重开。本轮主目标仍完整 (1)，以下是完整量词的缩减和实际桥反攻，未将一个校准冒目标完成。

## 2. restriction、平均密度与 flat 反向闭包

删整 labels 保 P、whole-axis containment和未归一α；W/I须按实际剩余值重计。删 marks 不保原逐管 density。假逐管 (1) 在ε/2下成立，平均 λ=Σw_i|Y_i|/(VδW)≥δ^η_av 时，取 density≥λ/2的 labels，保权 W′≥λW/2；每条保 λ/2下界。选 η_av≤η_per/2并吸收固定常数后可调用逐管结论，再以 η_av<ε/2吸 λ权损，得到平均版 (1)。这不给所有λ同常数的 critical maximal，也未保原W不变。

反向取 P=x₅，将原4D round δ-tubes及实际 marks乘法向短区间、以固定倍 round tube 包络放入R5，体积增一因子δ，方向帽权固定比较。全G4 nearfull版本于是返回原DIR4 nearfull正幂输入。即使完整转移成立，也应登记为既有输入应用/闭包，不新立ID或称普通高维维数增益；正向完整几何仍须独立支付。

## 3. 重因子与不可约因子的时间分配

实因式分解写 \(P=c\prod_{j=1}^JQ_j^{m_j}\)，J≤D，忽略实零集为空的因子；重复次数不改零集。不能因轴近零集之并，便直接指定一个因子含整个轴。可合法使用下列带原marks的分段。

对每原轴 \(a_i+tv_i\)、t∈[−1/2,1/2]，令

\[
B_{ij}=\{t:\exists z, Q_j(z)=0,\ |z-a_i-tv_i|\le C\delta\}.
\]

这些集合由固定变量数/degree的实闭域公式定义，标准QE及一维半代数分量界给统一 O_(D,C,R)(1) 个区间/点；常数不依系数大小。它们覆盖全 clock。按全部边界细分，再给每开分量选一个包含它的j，得到不交区间分配；端点集合有限。

先从原 round tube 去两个球端帽，损体积 O(δVδ)；η<1且δ足小时每label仍有≥λVδ/2 marks，λ=δ^η。内部使用唯一正交clock t=v_i·(x−a_i)，横截面体积≤Cδ⁴。有限时间端点没有5D质量。故每个label能选一个assigned interval，保实际marks≥c_D λδ⁴；其长度≥c_Dλ。令r为区间长度之下邻dyadic数，用两个完整长度r子区间覆盖，选保较多marks的一段。此时

\[
r\ge c_D\lambda,\quad |Y_i'|\ge c_D\lambda\delta^4,
\quad\ell_i'\subset N_{C\delta}Z(Q_{j(i)}),\quad |\ell_i'|=r.
\tag{2}
\]

Y_i′是真实原marks，未填满片、未移动点，位于相应 r长 round δ-tube。这个方案也涵盖某label需要沿clock换因子的情况，未假无缝 whole-label factor assignment。所有有限格式定理仍具名，不冒QE全算法新独证。

## 4. 分段后的空间包、原角权与尺度回传

(2) 的r只在[cλ,1]，有O(log(2/λ))层。选一层保原权至少W/O(log(2/λ))。每个选中label取其片轴中点所在r格，按空间格和因子分组；每组的全部片和marks在共同 B_(C′r)，而这些格的 C′r球重叠有固定上界。故各组实体E_g⊂E满足 Σ_g|E_g|≤C_D|E|，不付格数r⁻⁵。

对一个组在中点格中心作 isotropic r缩放，得到 unit h-tubes，h=δ/r。多项式 \(Q_j(c+rx)\) 仍非零且同degree、归一后仍在所允许全类；邻近常数C不变，位置范围变成固定R′。原方向没有改变，但新 h帽须以原δ帽覆盖，因此

\[
\alpha_h\le C\alpha(h/\delta)^4=C\alpha r^{-4}.
\tag{3}
\]

每个缩放后轴长度恰为1、round半径恰为h=δ/r，不把subpower长轴或anisotropictube当标准管。其实际体积是共同 \(V_h\asymp h^4\)，含原δ端帽缩放后成为的h端帽；选择的marks均保留于此roundtube。新逐管 density≥cλ/r≥cλ。对其 nearfull门槛，选原η足小于被调用不可约结论的η′，使 \(c\delta^\eta\ge h^{\eta'}\)，用h≤Cδ^(1−η)及固定常数margin可付。若该不可约全类输入在ε′成立，回原尺度给

\[
|E_g|\ge c r^5 h^{4+\varepsilon'}W_g/\alpha_h
\ge c\delta^{4+\varepsilon'}r^{5-\varepsilon'}W_g/\alpha.
\tag{4}
\]

r≥cλ及polylog层只损δ^(Oη)。例如先ε′=ε/3，再η≪ε及η′，总和得到 (1)。这里不是把coarse cap当原α，也未把近factor的短段免费当原单位轴。由此可严格缩减：若 uniform fullG4 对所有实不可约degree≤D成立，则对任意P成立；反向显然。它不自行证明剩余不可约case。

## 5. 低实维因子与已知G3的真实适用范围

若不可约因子的实零集维数≤3，截到固定略大球后是uniform fixed-format semialgebraic集合。其 δ依赖系数及奇点均在R60已审输入内，whole-axis版本可直接给

\[
|E|\ge c\delta^{4+\varepsilon'}\lambda^3W/\alpha.
\tag{5}
\]

逐管λ=δ^η蕴含原加权平均≥λ，取η≪ε后可付 (1)。在 (2) 的短片上调用同理，但必须保 (3)–(4) 的尺度/角权费用。不能把任意 hypersurface 的薄邻域因有小体积就当dim≤3；需要的是实际零集实维≤3。

degree1是flat DIR4应用：非空metricnear输入迫归一线性P的法向大小有依R下界，原法向速度Oδ，正交投影非短且每 projected δ帽只对固定数原帽。实际normalfiber长Oδ；真实marks与shared-grid nearfull DIR4接口沿R85已付，不新重算为结果。因此真正余下仍是 δ依赖、实不可约、real-dim4 的 hypersurface近轴类，包含近退化却无singular点的情形。

## 6. 绝对梯度不能由远离 singular locus 免费得到

取A>2任意大，e=δ^A，

\[
P_\delta(x)=\frac{x_5^2-e x_1}{1+e}.
\tag{6}
\]

degree2、系数ℓ¹=1、在实多项式环中不可约（视为关于x₁的primitive线性式），且 ∂₁P=−e/(1+e)从不为0，故实singular locus为空。取原unit轴x₁∈[1,2]，其余坐标为0；在同x₁处的零点x₅=√(ex₁)距轴≤√(2e)≪δ。全轴满足metricnear，原tube可取fullmarks、W/α=1。

轴上的梯度为O(e)，距轴的任一最近零点x₅=O(√e)，其梯度亦O(√e)。给任何预设的δ^c梯度下界，令A>2c就能违反；系数条件数没有从norm1获得控制。此例只否‘远离Sing⇒physicalgradient≥δ^c’的uniform桥，不反G4，也不否以normalized tangent方向而非绝对梯度组织的正确方法。

类似地，P=x₅^D的零集就是超平面；由 |P|≤δ只得 |x₅|≤δ^(1/D)，不能把 polynomial sublevel换成 metric δ邻域。原metricnear假设强于该粗代数不等式。重复因子应按§3去掉，而不能以小导数认定原几何异常。

## 7. 严格凸近平面：不存在任何exactline但有合法满族近轴

取e=δ^A、A>1，

\[
P_\delta(x)=\frac{x_5-e(x_1^2+x_2^2+x_3^2+x_4^2)}{1+4e}.
\tag{7}
\]

它实不可约且physical ∂₅P≥1/2，却没有任何非恒定affine line：将a+tv代入，t²系数迫eΣ_(j≤4)v_j²=0，再t系数迫v₅=0。另一方面，取S³中一个δ分离、δ稠密的无向网，N≈δ⁻³；对应原R5方向(v_h,0)、unit axes t(v_h,0)、|t|≤1/2。对每轴点取曲面点(t v_h,e t²)，距离≤e/4≪δ。原 C₀δ帽权至多固定α，权全1，fullmarks合所有假设。

这些实际tube union有体积≈δ：上界在B⁴_(1)×[−δ,δ]；下界用方向网覆盖B⁴_(c)，与法向[−cδ,cδ]相乘进入固定较小tube半径的并。故Nδ⁴≈δ、(1)有δ^ε余量，不是反例。

但原曲面根本没有非平凡exactline，因此任何‘δ近轴都可换成同一原P内的exact Fano lines’在任意δ^c精度都失败。其真实最高次项为 \(-e|x'|^2/(1+4e)\)，在S⁴的零方向只有±e₅；上述horizontal原方向距它为固定常数。因此也不能声这些近轴方向在原leadingzero的任意δ^θ邻域，或凭R61参数Σ套到nearcontained输入。允许改为近似低degree超平面可修本例；付这一变化的真实coefficient/scale/质量正是全类机制另须证明的责任，不被此例排除。此处也不将旧regular-leading之外另一个二次校准叫新主成果。

## 8. marks集中、近多平面与indefinite分支的收费

在 (7) 的同一实际族，把每条mark限在中心clock |t|≤λ/2，其中δ≪λ≤c。每条density≈λ，真实union≈δλ⁴；可以用方向网的稠密性在该半径上证明上下界，不用occupiedcell数代体积。因此nearfull λ=δ^η的结论必须先选η相对ε小；若η>ε/4，该特定全量词便会失效，而G4的存在性量词允许取η更小，故不是G4反例。

近union的metric containment不等于任一因子whole containment。例如 (x₅²−e²x₁)(x₅²+e²x₁) 的轴x₁=t,x₅=0由两侧不同因子覆盖，单因子在另一半轴没有近零点；§3的真实时间分配是必要的。标量小P或每点有一factor不能跳过这一账。

indefinite quadratic的 nearaxis t²系数只给近isotropy，如v₁v₂=Oδ，而不自动使一个固定坐标Oδ；当其它分量承载unit速度，可能有中间dyadic slopes。R54双输出共同因子中的unit强制不能搬到单方程。也不能把marks排除badclock当常数费用：任意可测marks可集中在那些clock，必须以其原density来挑阈值/短片并重付源门槛。以上均为specific免费步骤的反攻，未给全indefinite类估计或反例。

## 9. projected方向重数与真实normalfiber须联动

任何投影transfer都须同时支付：同一个kernel的实际E纤维长度、原单位轴投影长度、projected δ帽的原总权以及新marks的真实density。仅whole-line时段上的polynomial Jacobian、exact cone有限根数或source在一处regular，均不足自动补这四项。

例如投影长度仍固定非短、mesh仍δ，若只得纤维长≤L=δ^a≥δ、projected帽权≤αδ^(−b)，则归一fiber函数f=L⁻¹∫1_E的逐管平均只能保证θ≈λδ/L。这个θ未必达到DIR4 nearfull门槛。即使额外支付该门槛，沿R85真实θ²格桥回传也只给

\[
|E|\ge c\delta^{4+\varepsilon'}\lambda^3
(\delta/L)^2\delta^b W/\alpha
=c\delta^{4+\varepsilon'+2(1-a)+b}\lambda^3 W/\alpha.
\tag{8}
\]

所以不能把fiber/cap两项各自称δ^o(1)而不选参数。δ依赖系数可使这些损失是固定幂甚至无统一先验。反过来，不同空间packet内投影可恢复角帽并以bounded spatial overlap求和；本稿不以一个global投影失败否这种方法。R53已付局部packet和R55仅globalcap障碍的范围保持。

特别是从全部近轴挑‘原P中的exactline parameters’已被 (7) 严格否；从远离Sing挑绝对grad lower已被 (6)严格否。若A的完整尝试使用其它实际joint几何，应逐式审其原W/I/α和全clock，不以这两例预先否定。真正未付不能只命名 resolution/Whitney 或加 desired cap 公设替代。

## 10. 当前全类结论与待实际交叉审查

目前未构造满足全部G4假设却违反 (1) 的族；也未证明实不可约4维全类transfer。已付的是平均/逐管restriction、重因子→不可约的真实短片尺度/原角权闭包、低实维由既有G3处理的范围，以及两个明确免费桥的严格反攻。不可约化只是等价缩小剩余scope，不开新方向/ID或续一轮该scope；exact arbitrarydegree的旧输入应用也不能冒完整nearcontained门已付。它们不等于全G4已解，flat反向仍表明成功transfer也不是新ordinary增益。

A被分配完整机制稿 `R0087_full_G4_singular_transfer_attempt.md` 尚未实际落盘供全文互审；本文不预填其通过或失败。root的HRZ downstream量词亦待其实际稿后独核，不能把G4本身或fixed parent上的结论当globalgain。待root/A落盘后仅按授权补真实cross记录；若仍只旧regular/proper子类或无uniform原质量/角度桥，应依spec停止该机制并macro，明确G4未证未否，不能续新toy、D/λ阈值或把缺input冒external blocked。
