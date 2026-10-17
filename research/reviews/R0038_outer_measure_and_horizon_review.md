# R0038：任意集合、正 horizon 与有限出口的全文独审

2026-10-17，A。**结论：root整合稿 §§1–21、B独立稿 §§1–11在所列具名输入下通过本次逐步审查。** 未经外部同行评审；这是来源已有归约、证书及已存有限工具的拼接，不声明新颖性、重大结果或一般Kakeya解决。

实际全文读取 `notes/10_source_audit/source_assembly/R0038_reduction_source_assembly_and_finite_readout_full_proof.md` 与 `R0038_certificate_finite_readout_and_named_inputs_audit.md`；核原PDF20–25/text1066–1332、官方 `02-framework.tex` 的Theorem2.17（约1161–1646行），并重读原2.1–2.16模型接口、SRC001/DIR003、R29整合稿及KT原Def5.1/5.2/6.1、(39)/(40)、Theorem6.2。本人2.17独稿不是另一份独立review；下文是对root和B全部稿件的实际交审。

## 1. 外测度、同一scale与finite choice

root §§3–4/B §6对任意非可测或非紧K的处理合法。countably many rational time intervals/integer intercept boxes覆盖固定方向chart，由outer subadditivity取得positive outer measure的S₀；没有积分K，也没有预选方向到witness的函数。

第二次dyadic pigeonhole确在**同一k**保每方向存在的mark duration与方向outer measure。先有每witness至少一个scale的duration≥ck^{-2}，再定义存在性集合S_k并对其外测度用可数次可加性；不得先选一套可测witness family。maximal δ-separated有限点集覆盖bounded S_k，外测度给M≥c_ak^{-2}δ^{-3}，普通packing给M≤Cδ^{-3}。最后只选M条见证，finite choice足够。

每scale球数有限，open ball union使各已选line的time集合可测。只留与fixed bounded trajectory region相交的球不会丢这些traces，故K本身无需bounded。cover最大半径趋零迫选出的k趋∞。

## 2. smoothing与三个profile界

六coefficient box noises给piecewise constant indexed prior；内部index不是world或observable。directions的δ-separation使full three-slope cubes仅bounded overlap，故实际Lebesgue density≤C/(Mδ³)≤K₀。给定full slope后，component weights仍和为1，各二维y₀ smoothing density≤Cδ^{-2}，所以conditional intercept ceiling成立；没有将全局mixture错误写成slope/intercept独立。

扩大原coverballs后，成功time在所有允许noise下仍成功，raw mass≥ck^{-2}。tempered的world/index/predicate数、height、degree都有统一polynomial exponent，K非可测集合不作为输出predicate。

joint homogenization在compact(r,u)范围可用原2.3–2.5。hidden δ-observation support measure≤Cδ^{σ−1}使g(1,0)≥σ；V-bin的mass与conditionaly density相乘给g(r,u)≤r+2−2u。root没有把hidden单独cap与angular单独cap任意相乘，而是条件full slope后直接积分。

g(0,0)≤0明确依原2.15。full-time plank containment在t=0,1限制V到面积Cabρ² rectangle，故2.15的A是K₀ρ²。若n00有固定幂增长，先以joint flattening冻结visitedwholecells的lower，再删short marked durations，visitedcells≤K₀N₀^{-α}ρ^{-3}；current删后不声称仍有旧cell floor。

continuous prior按far-finer coefficient rounding和finite mark sets分组，只为调用2.15作有限近似；该估计的常数不依indices数，故无需这些分析性groups也具有统一polynomial数量。bin-center移动只固定扩大E_vis。分子≥m_ret/ρ，raw multiplicity lower为K₀^{-1}N₀^αρ²；先固定mesh exponentD，再选Dε<α/2，和plank upper冲突。这里没有循环使用四维Kakeya结果，也没有调用已否定的WP4。

## 3. Joint endpoint、crop与tiny world

root §§7–8的maximizer比较逐式正确。r=0边界值≤4S，u=4边界值<0，而(1,0)≥σ−R；故r₀>0、u₀<4且g(r₀,u₀)>σ/2。该endpoint不需unique、differentiable或interior。沿hidden和angular两个方向的一侧不等式分别产生d=1−R与正S，不能由一个profile条件替代另一个。

full-time crop在(y₀,V)四坐标，给exact(t,y)和old V-bin时只有bounded crop-label ambiguity。new y=(y−y_B(t))/a_{u₀}，within-world density精确乘a_{u₀}²/ν(B)；world-weight normalizer只作用总mixture，不进入这个因子。极小prior boxes按polynomial数量删，再homogenizeν(B)指数，仍保inverse-subpower selected mass和tempered prior。

oldangulardepth u₀+u对应newdepthu，同一within-world因子同时乘pure/joint density，因此terminal cap比值和relative profile取消。L=r₀、η=(4−u₀)/(2r₀)固定正，所有Def2.6输入齐全；未偷加n_new(0)∼1。

## 4. Original true floor与uniform geometric slope volume

root §§9–12的individual chart floor恢复原prior时，m_old=ν(B)m_new、J_phys=a_{u₀}²J_new，故ν(B)严格抵消；没有将tinyworld success posterior当trajectory prior。每条贡献positive selected duration的line，其prior质量下界由m_old/q获得；不必用unused assignment lines补下界。

Σ只用固定数量的whole-block spatial/value/derivative几何tests，不夹原K membership、finite witness identity、crop/event/density tables。因此fixed-format QE/semialgebraic choice/C¹ decomposition真能给uniform complexity，尽管chart数值系数、q^{-1}或frame逆可很大。这些标准实代数基础保持具名，不将任意measurable intercept函数擅自当uniform complexity。

det(Db(s)+tI₃)的leading coefficient恒1。删三个complex roots实部周围cq intervals后Jacobian≥c³q³；P_w沿line是real affine且sup≥1/K₀，所以其小值bad time≤4εq。两个bad sets各≤q/4即得共同good time≥q/2，不需independence，也无需这些good times仍是原marked times。

regularpreimages的uniform bound来自fixed-format fibers的connected-component数量，不是全局injectivity；各openC¹piece上的nonzeroJacobianpreimage为isolated。面积公式用locallyLipschitz compact exhaustion即可，不需Db有全局bound。其lower为q³×q|Σ|；allowed image volume在fixed(t,y)由二次sublevel给w-lengthK₀a_r、y-areaK₀J_phys，积分time再给q，所以最后正确为|Σ|≤K₀a_rJ_phys/q³。

原full-slope density再给eligibleprior≤K₀|Σ|。与原truefloor比较，a_rJ_phys取消，m(r₀,u₀)≤K₀q^{-3}；g≥σ/2遂迫h≥σ/6。该论证对每truechart、每合法selection和子列有效，故horizon infimum也满足该lower；不需要inf被达到。known atlas没有truefloor不能在此代用，root没有混用。

## 5. 全证书拼接与不循环范围

已实际核root §§13–15与B §§2–4。先TEX/CRP给positive k，不留一个未处理的bad k=0分支；d*=0按relativeprofile单调性处理，k=1仍在对应模型范围。relativeprofile只比较密度差，normalization的J/ν是within-world因子，不能额外乘世界ω或总Z。

顺序为：version1的ISO propercandidate→AIM→Cor6.9 scalarH0，然后才8.2 scalar projection；再排version2 ℓ=0/正有限/∞。没有用v2全source预先证明v1。正有限的critical 2k=1、subcritical 2k<1、supercritical 2k>1齐全；∞分支用UNB直接knownatlas/terminalcompletion，不套finiteℓ AIM前提。

每geometric branch输出every-subsequence/every-substantial-residual propercandidate和原qν质量，AIM再负责originalobservations、whole priority assignment、late derivative deletion、preparedprobability p_prep、selected failure map以及预声明actualguard。root/B明确没有把analytic K自动当(K_path logN₀)^r，也没有对∞父atlas额外假truefloor。终端child lifting只需terminal-known parent，中间层floor责任没有被免费继承。

## 6. G直接依赖cut与高级输入边界

B §5/root §2的G→weightedconvex→linechart→2.15链与CRP证书一致：由任意正权/重复indices的convex cap，Bernoulli抽样和finite John网给O(log) simultaneous clustering，再去重复但保真实代表shading。必须用G的**distinct tube、平均shading density、convex-clustering set estimate**，而非高维无方向结论。

whole trace在convexbody中的John envelope给固定空间轴、affine center的full-time plank；long marks转disjoint smallball shading后约去δ³，恰给2.15。代表不需保留重复indices全部shading，原weighted numerator另有AS|T|控制。这个dependency cut无需companion整个新maximal theorem。

GWZ2601.14411v2 Theorem1.1的确切statement/application保持具名；本次没有重证或重跑其whole高级/形式化proof。已发表WZ/CV、OSS及固定次组合论、标准实代数基础同样按明列范围使用。KT6.2只出现在高维出口，不回流为四维源的前提。

## 7. SRC、稀疏/权重与arbitraryambient出口

root §§16–18/B §§6–8给SRC的实际finite反证。若所有η均失败，取η_j→0的countersequence；孤立marks先扩成长cδ的time intervals，保每line正Lebesgue时长≥cδ^{η_j}。六noise smoothing在fixed enlargement中保这些times，slopedensityδ^{-η_j}=N₀^{o(1)}、predicate和index复杂度仍有一个固定polynomial exponent。原2.17 finite初始化之后的证明不再使用同一个跨尺度K，故确能产生bad exactproblem再反证；不是从dim_H statement直接推finite定理。

稀疏shear保持原clock及各copy的原marks，#copies≤C/(Mδ³)，方向覆盖常数体积后选near-full separated真实copy-lines；finite SRC允许这些copies不属于同一K。任意权重与repeatedindices按方向bin coloring选自己的原代表，只用逐line长mark条件及每bin总权α，未拼接同bin不同line的marks。

R29投影部分在这里作接口复核，不把本人旧proof再计独立审查。boundedGaussian/nonshort/independent-set输出数与all-angle cap相符；projected separation后cap3来自packing，不是免费Frostman投影。平均λ先heavy使数量损λ，再每输出line marks损λ，故下界确为cλ²mK^{-1}δ^{s−4+ε_D}/log。unsaturated m因子、任意fixedambient和real s≥3都保留，符合KT实际第二输入。

## 8. KT small-loss与任意集合的额外Hausdorff桥

重读KT原Def5.1/5.2/6.1：points为N^{-1}Z^M∩B(0,C)，lines为固定大球内CN^{-1}邻域的supporting lines；saturated shading要求总mass≈N#T，并非逐line全长。n−1 collection的(39)是所有center/all-angle upper，saturation另是#T≈N^{n−1}。root/B没有把maximal或Minkowski statement冒作这些定义。

本种子准确量词为∀output ε∃input η。固定ζ后付K(n,4−ζ)有正余量，不能额外声称literal endpointK(n,4)具有η(ε)线性模数。具名KT6.2用于n=6,d=d'=4−ζ时，其两项分别K(6,4−ζ)、K(5−ζ,4−ζ)，后者realangular s=4−ζ≥3，正落种子范围；没有免费direction-dimension monotonicity。

root §20/B §10的**任意集合**桥可独立成立。对dim_H K<t<d的cover，重复外测度同scale选择得M≥cδ^{-(n−1)}/k²、每line marks≥cδ^{-1}/k²、union≤Cδ^{-t}。取maximal C₀δ-separated slopes以匹配固定KT线宽/方向误差；其angularupper由packing自动给，M仅损固定常数。n−1参数在这个应用是整数ambient的实际方向维。

KT narrow-vertical chart可先选固定窄方向patch，再作固定affine clock归一；所有变换常数独立δ。取KT ambient ball含原bounded graph traces并留固定margin，supporting lines有∼N latticepoints；nearest-lattice marked points离原line O(δ)，落在KT的固定厚度内，每timebin仅O(1)合并。原short interval可延长supporting line或按固定数arclength windows选最富段，**只保原marks**而不添加延长部分shading。故unitline、boundedball、格点和narrowgraph要求均可付。

polylog亏损小于任何固定δ^η；先固定d−t余量和finite输出loss，再取对应input门槛、最后k足大，有限K lower δ^{-d+ε}与δ^{-t}冲突。无需可测direction选择、K可测性或compactness。于是该额外显式桥允许将本条件链的六维17/4 scope扩到任意Euclidean Kakeya集合；不是由“standard compact transfer”一句话扩大。

## 9. 最终意见

未发现必须新增的几何估计或原量词缺口。完整2.17、各证书的模型/质量/guard接口、finite反证、平均与逐管shading的不同闭包、KT strictsubcritical和额外outermeasure读出，均在当前稿中明付。标准固定格式基础、G新高级完整proof、KT完整递推及所列具名高级输入的核验层次必须继续披露；本review不把应用核对说成它们的全proof独证。

本轮可归档为来源完整assembly及条件finite/Hausdorff出口审查。未认证2026全前沿/优先权，未独立得到一般维度Kakeya满维数，也不因内部assembly通过就将Goal或major/new-high-dimensional flags置真。完成本授权审查后停止编辑，不继续调旧projection、ε或小lemma。
