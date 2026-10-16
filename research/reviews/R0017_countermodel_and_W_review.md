# R0017：加法校准与原 W 数据换路的独立审查

2026-10-17，lifting_obstructions。审查 `R0017_joint_expansion_attempt.md` 当前强 Cantor版本与 `R0017_original_W_reset.md`；对照已入库 WZ原文(148)–(152)、Theorem21.2及Remark21.3。结论：两稿限定的估计、反校准与范围表述通过。没有完整 finite vector strengthening反例或一般二维扩张证明；本审查不开展下一主研究。

## 1. 原 weighted energy 与分离 C4 的质量正确

固定标签s，把原正权tuple确定性分配到一个实际 A₊输出点。相同输出的两份tuple距离≤2Cr，故 E_s≥W_s²/#A₊。再按原ν积分，并用#A₊≤r⁻ʰn与 W≥r^hnm²，得∫E_s≥r^(3h)nm⁴。没有把time-pair多重集改为distinct translation的uniform prior。

固定(a,s)的weighted bipartite C4两次CS给 u_(a,s)⁴/m⁴；对同一a与ν再Jensen，得到总质量≥r^(4h)nm⁴。任意一对时刻间距<t的全部quadruples，由原B的Frostman与g≤1至多Cr⁻ʰt nm⁴。取t=r^(6h)、h<1/6，坏质量O(r^(5h))确实比下界小，保留四时刻两两分离的(1/2)r^(4h)nm⁴原乘积权。

这些是同一个g导出的真实质量，不是假设存在很多四环；但它们还不是原linear graph质量的扩张gain。归一化C4后，标签marginal最多受r⁻⁴ʰ倍原ν支配，稿中保留了这一成本。

## 2. 矩形恒等式与 sink边界正确

对T(b,c)=(b−c)(F(b)−F(c))，直接收集四个F系数得到

    T(b,c)+T(d,e)−T(b,e)−T(d,c)
      =(e−c)(F(b)−F(d))+(d−b)(F(c)−F(e)).

除以(b−d)(e−c)后确实为两条secant slope之和；F(b)=bR+U时是2R，没有消掉affine部分。输出属于2A₊−2A₊的O(r)邻域，不能把这个sink当成原tube Katz–Tao支撑。再除时间分离因子时，误差为O(r/t²)，没有无损保留O(r)。这些限制足以阻止以C4恒等式直接结束主证明。

## 3. 强 Cantor加法校准的全部量词通过

固定M,h后先选很大dyadic L₀，N=L₀⁴、D=L₀³；再令深度n任意大、r=N⁻ⁿ。C_n的维数为log_ND=3/4，所以A_n=C_n²的AD维数固定3/2，对应κ=1/2。常数C_N可以随已固定base变大，但不依赖n；因此对任意另给η>0，充分深时可吸收为r⁻η。这不是把亏损κ随着h缩到零。

一维N-adic cylinder计数给所有r≤w≤t≤1的局部 covering≤C_N(t/w)^(3/4)；两端尺度的base常数确实只进入C_N。对任意旋转tube，取其轴向分量大的坐标：该坐标每个w-bin内，tube另一坐标只变动O(w)，故二维tube covering仍有同一个3/4指数。于是γ_T=1/8所需7/8指数上界对全部宽度成立，而非只核最细r。

H_n两坐标alphabet大小L₀，故各坐标维数1/4、总AD维数1/2，确实与Y维数3/2互补为2。H_n⊂A_n；固定另一端和slab法向较大坐标后，以该坐标概率Frostman积分，uniform H_n×H_n的实际有序差law满足γ_Φ=1/4。重复差仍带其原重数，没有改成distinct差的均匀先验。

对每个固定p+q≤M，每位digit可取至多MD种值，所以实数sum/difference输出数≤(MD)^(2n)，有无进位只可能减少distinct输出，不会使这个upper失效。2log_NM<h给所需r⁻ʰ的cardinal比。A₊=A_n+H_n−H_n使未指定time结构的平移图g≡1，全质量保留。输出tubeupper也可用更大alphabet的维数log_N(3D−2)<7/8验证；主稿没有把它错误说成恰3/2维，亦注明如要同exponent的r⁻η upper须再选base。

这严格否定的是“KT固定亏损与任意小幂加法闭包不能共存”的捷径。它没有构造满足SM的F和共同B，也没有实现规定的(b−c)(F(b)−F(c))ψ表达式；因此不是finite vector strengthening反例，更不是完整source反例。原稿对此边界清楚。

## 4. 本代理carry攻击也没有越界

`R0017_vector_counterattack.md`的formal derivation恒等式只说明一个需要留意的代数模板。基数derivative的(4.1)–(4.3)给出的实数carry误差确实远大r^a；但单个坏tuple并不控制一个仅需r^h质量的restricted g。完整grid近加法图的2θ稳定性需要全部合法加法tuples，source没有这项前提。

因此，本轮两项互补尝试均没有给完整finite countermodel。不能把理想derivation图、静态加法Cantor图或carry失败之一拼成满足全部SM、prior、joint graph与source正则性的模型。

## 5. 原 W 关系及固定grain graph cover通过

直接核WZ(149)–(152)：两个终端点保留的差是

    (Δx″,Δξ″)
      =((z′−z)I₂, f(z)−f(z′))(φ₂−φ₁)
           +O(δ⁻O(η)ρ²),

而两个终端grain y-label相距O(δ⁻O(η)ρ²)。符号与块尺寸正确；新稿使用双撇记号表示原两段路径终端，不改变源等式。它们对实际原路径成立，尚未给出一个足够dense、已知prior与最大fiber的共同graph。

对一个完整原grain，A_yz={(x,ξ_p)}的cover upper来自：每个水平σ-cell的物理grain图只遇O(1)个σ-cubes，原coherence把各cube内ξ置于一个O(σ)盒。因此在source-allowedσ上N_σ(A_yz)≤Cσ⁻²。lower来自完整#X≥δ^ηδ⁻²与任意σ-ball内x投影的至多C(σ/δ)²个原点，给N_σ≥cδ^ησ⁻²。同一原x-counting概率的Frostmanupper≤Cδ⁻ησ²也正确。

这不是任意clipped patch的ADlower：一个窗口可以几乎没有原x点，路径权还可能高度不均。主稿把“选择足够dense共同grain/邻域并支付路径质量”留作下一轮真实gate，没有通过cover事实偷补它。也未从dyadic相容声称全局光滑或全局Lipschitz extension。

## 6. scalar工具与下一轮范围

WZ Theorem21.2的C确实是R内scalar multiplier集；Remark21.3只允许A、B的输出ambient维数经投影推广，不把C改为二维向量。ℓ=3时原系数是4×2块矩阵，作用在φ₂−φ₁∈R²上。仅投影输出不把它变成保原mass的scalar cb；二维grain graph的generic R²投影本来就可能满维，不能以维数符号宣布矛盾。

原(x,ξ)、full horizontal grain与原路径是Y-only graph丢去的实际配置数据。返回它们的W关系属于更换可用几何输入，仍以同一个N5-STICKY-MATRIX-01为主目标；不把源恒等式或cover bound改名为新定理。按本轮证据冻结无新输入的Y-only BSG/cycle/sink局部迭代合理。下一轮若只重述这些关系，也应停止而非继续阈值/投影改写。

没有证明一般矩阵分支、其他sticky mixed cases、一般到sticky或Hausdorff步骤；长期Goal保持active，未取得新的Kakeya维数结果或已确认重大中间结果。
