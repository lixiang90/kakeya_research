# R0035：完整 isotropic 引擎的几何与原 prior 独立审查

2026-10-17，B。实际通读 root `notes/10_source_audit/isotropic/R0035_isotropic_candidate_full_proof.md` §§1–18及 A `R0035_scalar_jets_and_qualification_audit.md` 全稿，对照原4.13、§5及§6到Cor6.9。B后半audit不计自审通过；本 review覆盖 root全部前后半，包含A负责的 scalar/qualification接口。

**结论：修后完整稿在原假设及文中具名高级输入下通过本次逐步独审，未发现 pending数学缺口。** 范围为原j1/v1与j2/v2、ℓ=0的Theorem6.1及其Cor6.9。不是完整四维源认证，不是五维/一般Kakeya结果，未经外部同行评审。

## 1. 实际高级输入和量词

已独立读取入库 Carbery–Valdimarsson arXiv1205.6371v1 Theorem1：d=n时为任意正权 full-line tubes、determinant/wedge因子置于1/(n−1)次方内，半径r的缩放为r^n。有限measure families在bounded区域内fine rounding、固定倍radius enlargement和加强det阈值可应用；不要求方向分离。曲线先局部线性化，不把它们直接当直线输入。未重证该深层定理。

已独立读取入库 Wang–Zahl 2210.09581v2 Definition4.2与Theorem5.2：ADset只要求所有中间尺度cover upper，subset仍有该性质，没有遗漏AD lower；alternative(B)适用于任意达到指定triple-cover门槛的restricted H。其(A)要求两条正交线，root仅需第一集合的线集中，合法使用较弱后果。root/A对点积反射、两集合正比例缩放及仅平移第二集合的说明保a·(b−b')结构。未重证其全文§8。

GWZ集合输入经已核2.15用于5.1，仍保named状态。TCM/ASM/TEX/CRP/AIM的既有证明范围不追改。主命题要对**每subsequence的每substantial residual**重新给candidate；root未从AIM倒推存在性。

## 2. 一项已修补的 weighted-label责任

若λ=Gνdt且仅0≤G≤K，λ upper不自动给ν对support event的upper。root §2最新版本已明确：实际原路径restriction若在support有G≥1可直接传；一般weighted情况先在同parent mixture删G<σ_N。其损失≤σ_NΣp_γν_γ(all)≤σ_N，σ_N低于当前inverse-subpower质量且σ_N⁻¹subpower。留下event上

\[
 \sigma_N\nu^\circ1_Edt\le\lambda_E\le K\nu^\circ1_Edt.
\]

ν°是删whole lines的未归一旧prior，不改保留线的密度；以后boolean restriction保下比较。若真作新的fractional restriction则另trim并计入有限预算。于是λ caps传成product-prior caps要除σ_N，dense labelmass lower用另一方向。修后§9也在scalar-normal应用处明确此费用。

参数world q=(γ,Bρ)的a_q=pγν°_γ(Bρ)满足Σa_q≤1，因为pγ固定、Bρ disjoint、ν°≤原概率prior。故总dense质量确给某q的mass/a_q dense；除该固定分母后G的上述比较保持，不偷用current success作prior。这一补充不增新统计假设，不以min world mass收费。

## 3. Breadth、物理梯度与同一ν°

root §3先unit-normalize strip法向；有eligible |V|≤K时其offset亦≤K，故参数有tangent-subpower范围。r1-separated重条带交集才被N^{-u/3}角球控制。仅“原N0固定幂幅度”不够，此措辞已修正。state实际list/深history ambiguity满足4.13；thin-strip输出whole assignments后通过AIM/4.12回收，非analytic预测表直接冒输出。

root §§8–9以long witness/actualbasecap将packet graph physical gradient过大转为thin velocity strip，随后才获得#W_p及hereditary local support。没有从scaled derivative K免费推出physical gradient K。

coefficient-box upper与lower均针对一次冻结ν°。lower通过全bad-block residual、按affine α的原palette预算选组、再用5.1矛盾取得，不能由upper或旧floor直接推出。参与bins之外未宣称all occupied bins都有同下界。细格之间的兼容采用palette child-light删除及邻尺度K-subdivision，未重设ν°。X'列表由同cell×velocity upper和entry mass floor给出。

## 4. Scalar saturation与dense-tested-event entropy

root §4的independent D lift满足(1,t)·z=x，full-time plank得到uv mass lower。固定scalar coefficients的D接受比例≤Cu由t=0/1两法向投影保证；scalar coefficient-ball cap遂给upper Kuv^d，比较得v≤Kp，再恢复p^d/K重bin。权重和marks为同一原prior，未免费均匀化。

root §5/A §4对每个新dense tested event重新计算s(T)、s(T,B)。预采整个tuple在world内独立trajectory；event可任意相关。E_Q(1/s)≤1/P(A)、期望log损失≤log1/P(A)=o(logN)支付conditioning，π/within-bin priors未改成后验prior。联合sheared cap、局部support、薄片cover给scalar entropy指数d和切向投影指数1；若event fixed-power稀疏则这项o(logN)不成立，原文没有作此扩展。

所用H(Z|T,C)≤H(Z|T,B)+H(Z|T,A)+I(A;B|T,C)确由chain rule得，不要求变量独立，也不是“条件化不增加mutual information”。

## 5. First/higher jets与真实见证回收

root §§6–7/A §§5–6的fixed-time m(t)、H-block mass、scalar-bin与j−1 tangential slices均先按原预算作light删除；恢复fit时间上的**全部prepared labels**后才从active-time长度及m(t)floor得到global dense质量。临时pair collision成功本身未被当作全局dense。

点积输入的restricted triples数由逐(u,v,v')cell上界推出；先存pre-quadrant活动时间，再保实际活动集，避免把整个bin当有标记时间。expansion alternative与d<1局部scalar cover矛盾，取fixed ε<1−d后再慢减，合法保H/K长度。相邻scale fits比较用之前真实common witnesses，不追认当前稀疏时间仍满。

higher-jet树在trajectory之前预采，root/leaf/t'的相关性保留；Jensen用于原product experiment，不在已成功条件下再假child独立。时间尺度schedule及ζ先定，有严格余量支付所有差商/nuisance。对bad jet-discrepancy/tail另作tested-event entropy，relative o(1)再慢选K。最终t'独立于树条件block，冻结(world,line,tree)后按真实fiber success删轻项，得到包含counted incidence的同h-block ordinary long witness；不凭投影增加原mass。

## 6. Physical graph、scalar-normal zoom与qualification

root §9 的n'=m+1 lifted velocity不近m-plane会给det≥b^θ；w0=b^{2/3}内曲线线性化误差Kw0²≪b，direction误差Kw0≪b^θ。最近long block witness控制prior≤KM/w0，CV filling下界与hereditary physical support冲突，指数θ−(1−d)/3<0。捕获base basis使plane是bounded graph，得到G；coarse row-list upper用共同product palette和X'列表计数，后续删选可保其support upper。

Lemma6.4按world/scale选color、按cell选value bin，损失只乘各scale常数，不按cell/world数乘。慢增grids令累计log损失o(logN)，comparison带floor，不声称G或R全球Euclidean Lipschitz。

在qualification失败residual中保持原G和先声明meshes，重新renew breadth。normal-strip filling是最后一次使用该breadth；后面parameter/entry逐边删除只用upper lists。world是完整Bρ，不是当前physical cube的成功条件law；subtract central curves后只缩位置，时间不缩放。

Def5.2 conditional cap分子用sameν° fixed-time active bound，分母用参与subbin的sameν° lower，palette因子相消。zoomed cell的time宽s'与moving spatial宽β=ρs'分别保留，upper及entry floor均含s'，没有漏β/s'因子。

去velocity条件必须用先前m0(W)及π(I)作entry floor；代价K_pre³/K_cut、conditional palette≤Kπ(J)/π(I)。R在entry几乎常值，所以一个occurring residual bin可用有界邻bins的palette见证；即使bin边界有tiny positive fraction，也不假该单bin有mass下界。每细velocity最多支付K个扩张邻bins，双计数给K个residual bins。这里E只作分析，未变成下一world或观察feature。

每固定ε的failure若relative质量不趋0，L_ref≥c使它仍substantial；重新准备后发现任何positive qualifying mass即与“全是失败”定义矛盾。原6.11还以 G0=X'−G_yV+O(b^κ)恢复完整row：沿一线X'为affine、V固定、M≥2，所以同degree-M多项式及同一long witness拟合G0，coefficients仍K。最后ε=1/r慢对角给frozen Λ_ref下relative o(1)，不把一次dense good subset直接升级为任意后稀疏law的全覆盖。

## 7. Cartesian准备与signed conservativity

root §10修后同时声明Kξ≪ε_T、Khξ≪a1以及hξ≪h_i（i=1,2）；第一项不由第二项推出，均在G发现前可按fixed powers选择。第三项保证descendant计数中的h_i/(hξ)不小于常数。M只需h^M≪a2，已与后面a2 fixed exponent安排一致。PDF97确写A0^{-1}u，bbox上标−1与下标0分行；root/A/B均已记为提取校正，**源无该坐标笔误**。

qualification之后先删bad proportion大的states，conditional tuple再作spanning/qualified union bound；未先选少量qualified velocities后追认breadth。field近T是state属性，插值完恢复全部prepared edges才保刷新时的conditional law。fiber-polynomial数及Cartesian所有中间vertices由随机times/conditional Jensen控制，cell floor将count转回mass。support I2用full assigned descendant priors与disjointness，不借current path的旧floor。

root §11两种heat-bath各保同P；longness/pruning后使用未归一kernel，不声称成功条件law仍独立。backward product domination及signed-increment triangular Jacobian1合法。fixed start的X_start/h只平移height support；regular fibers只需Jac≠0的isolated preimages，固定次数给统一multiplicity。full(m+1)-dimensional cell volume与实际endpoint support I2相乘得K h^{c0}→0，contradiction使用真实path endpoint，不是任意模拟endpoint都落支持。

## 8. Potential、heavy intercepts和degree恢复

root §12的radial potential直接求导，error仅skewDT项；X−P全h-block variation≪a2。截距每line只一项。state里只保fixed-fraction C、重删short lines及损失过多state/group，明确用最近前置long witness及可比current mass得到prior≤KM/h；未从任意稀疏group继承breadth或旧floor。CV给每groupξ⁻m/K cells，I2给总groups≤K(a/a2)^d，heavy threshold保所需mass。

root §§13–16的原R3核逐式正确：singular conic至多覆盖四点，七点binary sextic论证给cubic qLin；quartic/q²和quintic零核用Euler与gcd。cubic two-copy injectivity不同于three-copy核，实际用于∇³f。rank4 quantitative inversion只在修复后的exact conic family。real restoration用det+evaluations的正semialgebraic下界，Euler迫spatial gradient非小再IVT得real zeros，没有以complex零代real零。

native branch先给R=P_s(z,f)/a的独立K norm/derivatives，再移方向。f的higher derivatives只按distance-to-affine S0控制，预选mesh≤h²/K支付S0相对误差，不需S0绝对上界。小S0给quadraticTaylor；大S0给nonsingular real q及R2+qL1+λq²，用H'=(w−L')/S0编码为proper total-degree2。value、first derivative perturbationKa/S0和curvatureKa/S0²均有实际幂余量，e2保持不缩水。

最终测试是time degree≤2、hidden derivative degree≤1，所以只从同h-block内h/K ordinary witness作Remez到整块，绝不外推unit parent time。每份candidate仍有hν_Q(a2/a)^d/K质量；gain趋e2ks>0 finite。AIM提供original尺度实现，未将analytic K直接冒实际K_path幂。

## 9. 修后验收与剩余条件

核的是修后root §§2/3/9/10：weighted-label双比较及budget、unit-normal strip offset bound、h^M≪a2、Kξ≪ε_T均已明确。A的坐标陈述已纠正为PDF提取问题。没有pending数学修正；上述补充不新增统计假设或改变原j1/j2目标。

通过得到的是原Theorem6.1及Cor6.9在列明高级输入下的内部重证。正有限/无限窄度分支、retained-edge工具、scalar projection实际输出、完整2.17/finite readout及KT责任仍在；无新颖性/重大性认证，Goal active。按已声明协议R36先macro，不因本节结束自动沿源继续。
