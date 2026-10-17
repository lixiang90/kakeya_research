# R0038：完整拼接、有限种子与具名输入的正式独审

2026-10-17，审查者B。已实际通读 root `notes/10_source_audit/source_assembly/R0038_reduction_source_assembly_and_finite_readout_full_proof.md` **§§1–21全部**及 A `R0038_arbitrary_set_reduction_and_positive_horizon_audit.md` **§§1–14全部**，并复读原PDF20–25/168、KT Definitions5.1/5.2/6.1及6.2、SRC/DIR/FSD的实际证明与独审、companion `05-inputs.tex` 前两小节和GWZ v2原Theorem1.1。B自己的assembly稿不作为本次独立审查对象。

**结论：修后root整合全稿及A完整2.17归约通过本次内部逐式审查。** 通过范围含任意集合归约、全部原模型分支拼接、有限direction-rich读出、稀疏/weighted与任意ambient接口，以及§20直接outermeasure finite→Hausdorff桥。尚存高级输入均明确具名，未经外部同行评审；不由此宣布无条件新高维界、新颖性、重大性或长期Goal完成。

## 1. 原2.17的任意集合与同尺度双质量

root §§3–4/A §§2–4 没有对非可测方向集合积分。rational clock/interceptbox的countable cover先给一个positive outermeasure S0；每line可测的是其进入有限open ballunion的time集合。两次k^{-2}预算分别付逐line时长与direction outermeasure，成功的是同一个k；max cover radius趋0使该k趋∞。

maximal separated finite slopes的balls覆盖S_k，普通packing给M上界、outermeasure给M下界。只在这一步后选有限条实际witness，无需可测选线；K的非紧性由固定轨迹区域处理。六个coefficient独立box noise的indexed-mixture prior是合法tempered full-dimensional law，原successful times在固定扩大U_k内对全部noise保留。

完整slope density≤C/(Mδ³)与给定full slope后的y-intercept density≤Cδ^{-2}是不同输入。后者用conditional mixture weights求和1，不错误假设整个mixture的slope/intercept独立。之后任意incidence restriction仍受固定原νdt支配，不改trajectory prior。

## 2. g00与joint endpoint没有漏调用

root §§5–8/A §§5–8 的support-count单位正确：δ-ball只给O(1)hiddenbins，continuousbase体积δ³，故observation support≤Cδ^{σ−1}，g10≥σ。joint angular upper另用V-bin质量及conditional y-density，给g(r,u)≤r+2−2u。

g00不是由这两个界免费推出。原fulltime containment由端点控制V rectangle，原prior cap为K0abρ²，调用2.15应代入A=K0ρ²。固定足细ρ=N0^{-D}后，typical whole-cell witnesses先冻结，再删current短duration；current residual不被赋同一cell floor。rawmark数≥mret/ρ、visitedcount≤K0N0^{-α}ρ^{-3}，与plank upper比较的次数ρ²相符。D先选，后取Dε<α/2，非循环定参。

同一joint profile上max g−Rr+Su给r0>0、u0<4、g(r0,u0)>σ/2。两条一侧比较分别付hidden terminal cap与positive angular exponent。crop-label只在exactbase/旧Vbin下有bounded ambiguity，不将内部witness index暴露给observation。

新within-world density精确乘a_{u0}²/ν(B)，world-weight normalizer不混入该式。tiny prior crops先按polynomial计数删极轻，再homogenize；它们的ν(B)虽可为固定幂，后面的原prior floor仍精确消去，不能称其一律subpower。

## 3. 所有terminal true charts与q³下界

root §§9–12/A §§9–13 对任意后续合法incidence selection及subsequence都使用同一原完整prior。true floor返回原单位为

    m_old/q ≥ n(r0,u0)J_phys/K0。

这里m_old=ν(B)m_new、J_phys=a_{u0}²J_new；若只有known atlas则没有此lower，现稿没有以known代true。贡献positive selected time的轨迹原prior至少m_old/q，即使whole assignment还包含unused trajectories也不影响。

Σ只保fixed-format whole-block几何/value/upperderivative及某处lowerderivative，主动丢弃原crop、finite index、selection与density predicates。这一步既包含所有贡献slopes，又使QE/choice/C1pieces的复杂度uniform于所有数值参数。所选b(s)无须服从原prior，它只用于几何volume估计。

det(Db+tI3)是moniccubic。删三个complex roots实部附近的cq区间后det≥c³q³；P_w沿所选line是affine，另一bad-time集长度≤4εq。各损≤q/4给joint good length≥q/2，没有两事件独立性假设。regular preimage在open C1piece内孤立，uniform semialgebraic component bound给constant multiplicity。compact/local-Lipschitz exhaustion足以用area formula，不要求Db全局有界。

因此q⁴|Σ|≤C∫|F_tΣ_t|dt，而允许image每时刻体积≤K0 a_{r0}J_phys，积分再给一个q，最终|Σ|≤K0 a_{r0}J_phys/q³。原fullslope density把volume转成eligibleprior upper；相除得m(r0,u0)≤K0q^{-3}及h≥σ/6。因为每个competitor都满足，infimum和进一步合法selection仍受此lower；不只核某个chosen system，也不需inf attained。

## 4. 全证书的模型、端点和actual law

root §§13–15 的顺序无环：CRP/TEX/AIM先配ISO的v1部分排scalar，Cor6.9随后才供8.2。v1本来允许hidden轨迹为quadratic，未误替为R4的affine w。v2的ℓ0、正finite、∞三类穷尽，∞通过原10.1直接actual atlas及terminal completion，不偷用4.11的finiteℓ前提。

d*=0的relative-profile证明另用单调性；0<k≤1由已付2.16及uniform TEX/positive remainder给出，故没有漏k0 bad case。k=1/2有critical分支，k=1属于above-critical范围。sup/inf的narrowness不要求attained，所有fixed i先inner exact limits再outer i；原finite grids上的whole assignments及各自frozen witnesses始终保留。

AIM输入确为every subsequence/every substantial原residual上的proper候选。countable scenarios经有限菜单覆盖才固定scenario，whole pieces先赋值，之后小derivative时段才收费。prepared probability要乘回pprep；μprep不免费视作原μ的submeasure。最终selected tests失效先赋failure且failure不入posterior最大列表，unknown labels也不暴露给selector。

实际list/geometry是(Kpath logN0)^rS，complexity是固定P_S(Mpath)，进入预声明指数guard；普通analytic K只有靠positive fitting buffers才消失。终端known-parent lift只需terminal equality；中间true lift需known-pr equality，∞分支完整ν_c与ν_A不能混用。root正确重用R33–37已审接口，没有把所有later current measures当旧true floors。

## 5. newGWZ的最小输入责任

root §2所用GWZ v2 PDF2 Theorem1.1确为distinct tubes、convex clustering和平均dense shading的集合估计。companion前两小节及CRP001给一条独立有限转换，不需要companion整个maximal theorem。

Bernoulli(ω/A)抽样在polynomial John-box网同时保logarithmic clustering；expected total S大时保S/2，小S用pointwise总权。去同tube重复只损log，每distinct tube保一个真实index的原long shading；原weighted numerator另以AS|T|控制，所以没要求代表保全部重复indices的marks。任意小权、跨度、repeats和index数量均无额外费用。

whole-time linechart到convex cap使用John ellipsoid的time diameter≥1及最大水平slice；common tube length/endcap余量保证spatial widths≥cδ。mark balls在同index内disjoint，δ³消去得到原2.15。只有per-index long marks才能直接走该链，平均marks需另heavy；现稿没有混用。

所以可将剩余新三维高级责任准确缩为**具名G集合估计的完整proof**，不是额外整个companion maximal。G作者报告的Lean formalization没有在本项目本地重跑，不能记作本项目独立验证。

## 6. SRC finite读出有完整初始化

root §16重新给η_j→0、δ_j→0 countersequence，而非引用Hausdorff statement。单条mark扩为cδ_j时间段，bounded velocity/noise与固定cell enlargement使selected duration≥cδ_j^{η_j}；fullslope ceiling≤Cδ_j^{-η_j}=N0^{o(1)}。indices≤Cδ_j^{-3}、cells≤Cδ_j^{-4}、六coefficient density≤Cδ_j^{-6}，复杂度统一固定多项式，不因η_j→0增长。

同observation support给g10≥σ，其后§§5–12只用这些有限data/ceilings，不再用固定跨尺度K。因此归约后由已拼接bad-problem排除矛盾。每σ>0的量词可先对0<σ'<min(σ,1)证明再加强，larger deficits不需要新分支。不能从一个fixed大的η估计推出这条任意小损命题。

## 7. DIR/FSD与strict-KT的真实预算

root §§17–19的bounded shear保clock，复制数O((Mδ³)^{-1})，正方向体积足取near-full separated真实copies；没有要求覆盖每方向，也没有额外按line数再乘footprint。任意方向格权重版本只用fixed-color代表与原marks上界；不同index的marks未拼接。

平均shading λ先heavy给cλm条；Gaussian collision/independent-set再损Kδ^{3−s}log，输出每line自己的cλδ^{-1}marks。两个λ都在，故

    #E ≥ cλ²m K^{-1}δ^{s−4+εD}/(1+logδ^{-1})。

K≤δ^{-η}、λ≥δ^η的费用是+3η，不是负号。arbitrary m、fixed arbitraryambient和real s≥3均保留，θ>1的collision余项由R29全sphere固定cover支付。unsaturated m-factor对准KT(40)，非只核饱和主statement。

修后§19明确0<ζ<1，使第二seed K(5−ζ,4−ζ)的角指数4−ζ≥3。∀output loss∃input tolerance的顺序允许固定ζ后有限次选择门槛，不承诺线性modulus或literal endpoint K(n,4)。具名KT6.2给K(6,17/4−ζ/4)的算术和实际第二ambient输入正确；其完整高级proof及旧6.6排印疑点未被本轮冒签为已重证。

## 8. §20任意集合scope扩展通过

已特别独核该新增桥，不只沿用R29的compact convention。对任意K、dimH K<t<d，outermeasure同尺度选择给≥cδ^{-(n−1)}/k²个真实slopes，每line在U_k的time≥c/k²。修后root取maximal **Cδ**-separated slopes，C是固定chart逆Lipschitz常数，因此KT实际unit directions δ-separated；所有angular caps由packing给出。

固定窄directionpatch与affine clock/spatial归一化满足KT near-vertical chart。KT discretized line本身就是固定ambientball里supportingline的Cδ邻域；共同graphinterval给length≈1，原marks换lattice仅固定合并，全部仍在U_k固定扩大，#E≤Cδ^{-t}。若改用unitsegment约定，可固定有限分窗保各自最富窗，不会增加marks。

direction count及mean shading只损polylog，满足KT soft saturated输入。固定ε<(d−t)/3后再取其input门槛，polylog最终皆为inverse-subpower，finite lower δ^{-d+ε}与δ^{-t}矛盾。K及跨尺度选线不需可测或紧，只有每条有限已选line的open-ball time可测；没有使用非可测K的Fubini。

所以由真正有限K(n,d)可以扩到任意K的Hausdorff lower。接六维各ζ后取极限的条件17/4 scope可以据此扩展；这只是显式付清outermeasure桥，不认证任何新的优先权或一般猜想。

## 9. 修订验收与停止

已实读root修后§19的0<ζ<1、§20的固定near-vertical归一化/Cδ separation/supporting-line convention；这些精确clarifications通过。A全稿与root2.17主链一致，未发现pending数学补丁或需要新增几何估计。

结论仍条件于各明确具名高级输入，特别newGWZ完整集合估计和KT完整递推；本次内部全文审查不等于外部同行评审、Lean重跑、2026全部前沿比对、新颖性/重大性认证或无条件高维定理。本代理完成授权文件后停止编辑，无Git操作，root统一归档同步。
