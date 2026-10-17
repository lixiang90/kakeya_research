# R0038：任意集合归约与原2.17正 horizon 的完整审计

2026-10-17，A独立稿。范围：原PDF20–25、提取1066–1332，连同原2.1–2.16的模型、density/refinement/normalization与具名 weighted plank 接口。下文逐步重证原Theorem2.17；未找到保全部原条件的反例。正 horizon 这一归约仍用原2.15，即既有CRP证书所列的**新GWZ set estimate具名输入**，不在此解除其高级责任，也不声称完整四维或新高维定理。

## 1. 命题、量词、排重与停止条件

设任意集合 K⊂R⁴ 含每方向单位线段，dim_H K<4−σ，固定0<σ<1。不假K可测、闭、紧、bounded，也不假可测选线。目标产生原version2 tempered homogeneous exact problem E，某固定0<d<1、S,η>0，且**每子列、每进一步合法inverse-subpower incidence selection**中的每个true terminal system若q=N₀^{-h+o(1)}，则h≥σ/6。因此原Def2.14的infimum H(E)≥σ/6>0。

这个命题不是已有finite shading estimate换名：本轮须付任意集合的外测度选择、同尺度两种质量、full-slope smoothing、joint endpoint/crop与所有true terminal charts的几何上界。反攻测试为：不均匀覆盖、不可测方向集、稀疏marks、tiny crop prior、巨大test系数、near-singular/rapidly oscillating intercept choice，以及Jacobian-good与derivative-good times相关。若任一接口需新估计，则停在该准确缺口；不能只证明cubic行列式便宣称完整归约。

只重用原2.3–2.5、2.9和2.15的准确结论；下面说明各自实际输入。原3–10节的排除分支不是2.17的输入。进一步selection只缩incidence event，完整trajectory prior不改；typical density指数按2.3保留，绝不能换成successful-line后验。

## 2. 任意非紧集合：外测度选统一time/intercept范围

在方向空间固定一个bounded open graph chart，用s∈R³代表空间graph lines (t,b+ts)。chart方向有正Lebesgue measure。每个对应单位段的t投影有正长度，故其中有某个非退化rational-endpoint interval；该段的graph intercept b又落在某个integer-endpoint bounded box。所有(interval,box)选择可数。

令S_{I,B}为“存在一条K内见证并覆盖I、intercept在B内”的slopes集合；它未必可测，但这些集合覆盖整个方向chart。若它们全外测度0，可数外次可加性会使chart外测度0。故选一个S₀，a=|S₀|*>0。固定 affine change把该I化为[0,1]；slopes/intercepts及其graph traces都在固定bounded boxes中，Hausdorff dimension不变。这个阶段没有选方向到轨迹的函数。

K本身无需bounded：只取Hausdorff小球cover中与上述固定轨迹区域相交的球。球半径≤1时其中心亦bounded。这些球仍覆盖所有候选graph traces，且原cover成本不会增大。

## 3. 同一 dyadic scale 同时保方向外质量与逐线时长

取任意细的open ball cover，Σr_i^{4−σ}≤1。用U_k表示半径δ/2<r_i≤δ、δ=2^{-k}的球并；这一尺度球数≤Cδ^{-4+σ}，因此U_k实际是有限并，t→1_{U_k}(t,b+ts)可测。

选c>0使Σ_{k≥1}ck^{-2}<1。任一eligible witness的整[0,1]被各U_k覆盖，故Σ_k|{t:graph(t)∈U_k}|≥1；于是至少一个k的时长≥ck^{-2}。令S_k是有这种成功见证的s∈S₀；即使S_k非可测，S₀⊂∪S_k仍成立。

再取c′>0使c′Σk^{-2}<1。若所有k都满足|S_k|*<c′ak^{-2}，外次可加性给a≤Σ|S_k|*<a，矛盾。故有一个k满足|S_k|*≥c′ak^{-2}，并且这个**同一个k**的所有S_k方向都存在上述mark duration见证。cover最大半径趋零时任何可选k都趋∞。

在bounded S_k中作maximal δ-separated finite subset。有限性来自普通packing；greedy过程有限步结束，其δ-balls覆盖S_k，故

\[
c_ak^{-2}\delta^{-3}\le M\le C\delta^{-3}.
\]

这里只对M个方向分别选一条成功见证，有限选择不要求任何measurable selection。非可测S_k没有被积分；用到的只有它的outer measure与有限δ-ball覆盖。

## 4. 平滑后完整trajectory law、原marks及三斜率密度

置N₀=δ^{-1}、L=1、P*=w、B=1。先均匀选M个indexed lines之一，再独立平滑三个intercept坐标和三个slope坐标，各在半径c₀δ的uniform cube内。原有marked times在固定倍扩大U_k中对每个允许perturbation仍成立，所以μ(all)≥ck^{-2}=N₀^{-o(1)}；active selection就是有限并球的原几何predicate。

每个内部index的full six-coefficient prior是piecewise constant box density，高度≤Cδ^{-6}；index数M≤Cδ^{-3}，balls数≤Cδ^{-4+σ}，所有测试degree≤2、变量数固定、系数bounded（可任意实常数）。故满足Def2.2。内部index不是额外world或观察点特征；不把它加入原observation。

δ-separated slope centers的平滑slope cubes有O(1)重叠。完整s=(V,W)∈R³边缘密度

\[
\frac{d\nu_s}{ds}\le \frac C{M\delta^3}\le C_ak^2\le K₀.
\]

这不是仅δ-bin cap。对于固定完整slope，conditional mixture仍是各component的intercept smoothing convex combination；其二维y₀ density各≤Cδ^{-2}，所以ν(y₀|s)有相同ceiling。平移到y(t)=y₀+tV不改变这个conditional bound。当前incidence selection无论多相关，作为product-prior×dt的submeasure只会缩这些upper。

这些是完整斜率law、conditional y-intercept density和product-time domination三项不同事实，后面不能相互替代。

## 5. Joint homogenization与两个容易算的端点

原2.5对compact(r,u)∈[0,1]×[0,4]联合homogenize (p_r,[V]_{N₀^{-u}})。compact范围使所有bins由最细共同mesh决定，table总量polynomial；2.4给固定 polynomial base mesh的joint TV误差，density types数缓慢增加。typical profile f(r,u)连续，r方向1-Lipschitz、u方向2-Lipschitz且各自nondecreasing。进一步inverse-subpower restrictions用2.3保同指数。写n=N₀^{-f}、m=N₀^r n=N₀^{g}、g=r−f。

在r=1,u=0，cover每个δ-ball只占O(δ³)的(t,y) base volume、O(1)个hidden w_δ bins。因此全部possible observation states的dt dy×counting measure≤Cδ^{-4+σ}δ³=Cδ^{σ−1}。typical exceptional mass删掉后仍有inverse-subpower active mass，故n(1,0)≥K₀^{-1}δ^{1−σ}，即g(1,0)≥σ。没有把非可测K本身当可积集。

固定u的V-bin prior≤K₀N₀^{-2u}：完整slope density上界积分bounded W得到二维V density上界。给定full slope，y(t) density≤Cδ^{-2}。忽略w-bin即可得任意r的joint density≤K₀N₀^{2−2u}，即

\[
g(r,u)\le r+2-2u.
\]

## 6. g(0,0)≤0：原weighted plank的准确调用

原二维y-trace M_l(t)=b_l+tu_l在bounded affine chart。若整条trace contained in任意rotated full-time plank，空间radii为aρ,bρ，1≤a≤b≤ρ^{-1}，其u_l被端点差限制到radii2aρ,2bρ的rectangle。二维V density≤K₀，故原prior的full-time containment mass≤K₀abρ²。允许固定plank dilations只改常数。这一cap是完整原prior的，不是只在marked portions成立。

假n(0,0)以某固定正幂增长；取α>0小于该幂并留固定余量。按2.4在ρ∼N₀^{-D}固定够细mesh共同flatten，保typical high-density states。hidden unit bins数为O(1)，保留下来的base cells各承载至少N₀^αρ³的原selected mass（必要时减小α），所以visited base cells数≤K₀N₀^{-α}ρ^{-3}。共同flattening的TV error先选power-small，cell-table selection回原law；其support是这些实际good cells，不是把jitter后的点当原轨迹。

删total labeled duration<K₀^{-1}的轨迹，费用由product prior×time控制，可保m_ret≥K₀^{-1}，并使每used trace至少K₀^{-1} marked duration。每time bin lengthρ，令J_l为有正retained duration的bins；#J_l≥duration/ρ。原trace在bin center的位置与某原good incidence相差O(ρ)，故E_vis只需good cells的固定倍enlargement，cardinality仍≤CK₀N₀^{-α}ρ^{-3}。

将coefficient law在远细于ρ的格round，连同有限mark set J_l分组，权重为该indexed-trace group的原prior mass。组数虽可很大但有限，2.15没有其polynomial数量限制；这只是调用估计的有限近似，不作模型输出。rounding仅扩大full-plank测试固定常数并扩大E_vis固定邻域。故2.15可用A=K₀ρ²，而且#J_l≥ρ^{-1}/K₀≥ρ^{-1+η_ε}晚N成立。它给

\[
\frac{\sum_l\omega_l\#J_l}{\#E_{\rm vis}}
\le C_\epsilon K₀\rho^{2-\epsilon}.
\]

另一方面分子≥m_ret/ρ，故该ratio≥K₀^{-1}N₀^αρ²。**先固定flattening exponent D，再选Dε<α/2**，两者矛盾。因此g(0,0)≤0。这个结论明确依赖原2.15；其直接来源为具名GWZ set→weighted convex clustering→plank链，不能由斜率密度一句话替代。

## 7. Joint endpoint及完整cap-class参数

选固定R,S>0，R+4S<σ/2且R,S<1/10。连续g在[0,1]×[0,4]上使g(r,u)−Rr+Su达到maximum (r₀,u₀)。在(1,0)值≥σ−R；r=0边界因f随u不减及g(0,0)≤0而值≤4S；u=4边界因g(r,4)≤r−6而值<0。故r₀>0、u₀<4，且g(r₀,u₀)≥σ−R−4S>σ/2。

固定u₀向前hidden depths比较maximum，得

\[
f(r₀,u₀)-f(s,u₀)\le(1-R)(r₀-s),\quad0\le s\le r₀.
\]

固定r₀向右angular depths比较，得f(r₀,u₀+u)−f(r₀,u₀)≥Su，0≤u≤4−u₀。这些是需要的一侧endpoint不等式；不要求maximum是内点，不假g可微或unique maximizer。

## 8. Crop worlds、typical密度及tiny ν(B)精确抵消

以side a_{u₀}的dyadic boxes对(y₀,V)四坐标作full-time crop B，world prior为ν(.|B)，world weight proportional于原ν(B)。剔除极小ν(B)者：worlds数polynomial，选足小reciprocal polynomial阈值，总prior及selected loss negligible。按ν(B)的log-type再选inverse-subpower质量，可使各保留world的ν(B)有共同指数；其normalizing world-weight factor只为subpower，不进入within-world density。

y=y_B(t)+a_{u₀}y_new，w和time不变。coeff transform constant Jacobian且条件prior density仍piecewise constant/poly height；native P*=w、B=1保持。y_new及V_new有uniform bounded range。给定exact(t,y)和oldV_{a_{u₀}}，y₀=y−tV只允许O(1)个intercept bins，故B只是bounded-list refinement，内部finite witness index没有被观察。

记ρ_B(s)为原未归一law加B后的observation density。transported hidden bins不变，base Jacobian a_{u₀}²，conditional prior divideν(B)，故逐world精确

\[
\rho_{\rm new,B}(s)=\frac{a_{u₀}^2}{\nu(B)}\rho_B(s).
\]

bounded crop ambiguity、rounded grids的bounded overlap及2.3给n_new(s)∼_log n(s,u₀)a_{u₀}²/ν(B)。newangular depth u对应old u₀+u；同因子也乘joint density，故端点差和angular ratio都抵消。取L=r₀、d=1−R∈(0,1)、η=(4−u₀)/(2r₀)>0，恰满足原Def2.6，S,η固定正。没有要求绝对n_new(0)有界。

## 9. 所有true terminal charts的original-prior lower

任取新E的true terminal chart c，包括之后任意合法selection、任意子列中所得者。其q、D_new、J_new与degree≤2 test P满足原Def2.8：whole assigned line在全I空间约束和|P|≤K₀a_{r₀}，whole-block |P_w|≤K₀，selected incidences |P_w|≥K₀^{-1}。crop没有改变w derivative尺度。

J_phys=a_{u₀}²J_new。chart在原未条件prior的selected mass m_old,c=ν(B)m_new,c；由true floor和上一式

\[
\frac{m_{\rm old,c}}q
\ge K₀^{-1}\nu(B)n_{\rm new}(r₀)J_{\rm new}
\ge K₀^{-1}n(r₀,u₀)J_{\rm phys}
=K₀^{-1}m(r₀,u₀)a_{r₀}J_{\rm phys}.
\]

这是individual within-world公式；额外world权重及其总normalizer不混入分母。即使ν(B)是tiny polynomial也精确取消。之后incidence restriction不改fullprior及typical exponents，true floor仍必须相对于同n_new满足。任何对该chart贡献正selected duration的trajectory都在几何eligible集合，其原prior质量至少m_old,c/q；没有用unused assigned trajectories补这个lower。

## 10. 只对几何放大集合作uniform-format choice

固定chart。定义Σ为所有bounded原full slopes s∈R³，存在bounded原intercept b，使整I上空间box条件、|P(t,b+ts)|≤K₀a_{r₀}、|P_w|≤K₀、sup_I|P_w|≥K₀^{-1}成立。**不加**crop membership、原finite witness identity、density table、selection event或mark predicate。这保证包含全部contributing trajectories的slopes，又使格式与N₀无关。

这个公式的变量数、polynomial数量和degree固定，chart系数、D_phys^{-1}、q、test阈值都是实参数，大小不影响公式format。具名使用parameter-uniform real quantifier elimination、semialgebraic choice及C¹ cell decomposition：可选eligible b=b(s)，其graph complexity只依固定格式；有限个full-dimensional open C¹ pieces覆盖Σ除一个null set。较低维cells无需提供slope-volume lower。

这里是标准实代数基础输入的确切应用，不自行假设一个任意measurable intercept函数有有界fiber数，也不以source复杂assignment格式作为uniform-format前提。选出的b(s)与原prior无须相关，它只用来验证扩大的几何slope集合体积。

## 11. Monic cubic good times与regular multiplicity

在每open C¹ piece，F_t(s)=b(s)+ts，det DF_t(s)=det(Db(s)+tI₃)为leading coefficient1的cubic。每个s删三个complex roots实部附近radius cq的intervals，损≤6cq；其外每factor modulus≥cq，所以|det|≥c³q³。此论不需Db bounded、roots bounded或coef height lower。

P_w(t,b(s)+ts)是real affine function g_s(t)，其sup M≥K₀^{-1}。若variation<M/2则全程|g_s|≥M/2；否则slope≥M/(2q)，故|{t:|g_s|<ε/K₀}|≤4εq。固定c、ε使两个bad-time sets各长≤q/4，则每s的同时good times长≥q/2。根与导数bad sets可完全相关；只用长度并集界，不假独立，也不要求good times仍为原marked times。

定义Σ_t为在open pieces且通过两good tests的slopes，Fubini给∫_I|Σ_t|dt≥q|Σ|/2。它们的images是measurable semialgebraic sets。对任何fixedt和targetx，fiber{s:F_t(s)=x}有uniform bounded semialgebraic connected components；nonzero Jacobian处local inversion使该preimage在open piece内孤立，故是isolated component。所有regular preimages≤C_format；边界cells是null，不额外贡献。无全局injectivity或|Db|上界。

在各C¹ piece以countable compact/exhaustion应用area formula，monotone convergence允许unbounded derivatives。uniform regular multiplicity给

\[
q^4|\Sigma|\lesssim q^3\int_I|\Sigma_t|dt
\lesssim\int_I |F_t(\Sigma_t)|dt.
\]

## 12. 可用spatial volume与q³界

在fixed(t,y)，eligible image points满足|P(t,y,w)|≤K₀a_{r₀}、|P_w|≥ε/K₀。原2.9的一维二次sublevel lemma给w总长度≤K₀a_{r₀}，不需P系数的uniform size或全w单调。y区域面积≤K₀J_phys；故每时刻image volume≤K₀a_{r₀}J_phys。积分time再除q⁴得到

\[
|\Sigma|\le K₀\frac{a_{r₀}J_{\rm phys}}{q^3}.
\]

q⁴来自cubic det的q³和每s good-time length q；最终上界只含q^{-3}，因为allowed spatial volume再积分time给q。这个维数/时间次数没有混淆成q^{-4}。

## 13. 原斜率law与每selection的horizon下界

原完整slope density≤K₀，因此**所有**geometrically eligible trajectories的prior≤K₀|Σ|；只需对slope积分，给定slope的conditional intercept概率≤1，完全不要求semialgebraic选择b(s)服从原law。与§9的original-prior floor比较并取消a_{r₀}J_phys>0，得

\[
m(r₀,u₀)\le K₀q^{-3}.
\]

而m=N₀^{g(r₀,u₀)}、g≥σ/2，故若q=N₀^{-h+o(1)}，则h≥g/3≥σ/6。这个argument对每单独true terminal chart成立、uniform于其数值系数和tiny crop mass，也对每子列/合法进一步selection成立：原fullslope ceiling与完整prior不改，terminal density指数由2.3不改。

任何true terminal system的common horizon exponent都≥σ/6，故其任意infimum仍≥σ/6；不假H被某system达到。原2.16保证这一infimum有有限上界L，但正lower本身不需一个minimizer。未找到原不可测集合、稀疏选时、巨大test系数或tiny world能逃过该比较。

## 14. 审计结论、实际依赖与停止范围

在原2.3–2.5的tempered density selection、2.9及具名2.15输入和上述parameter-uniform semialgebraic基础定理下，原2.17全部归约与每selection正horizon结论闭合。本稿没有把整套原3–10节排除当成2.17前提；也不以2.17反过来证明2.15，故依赖无环。

其中2.15的高级来源责任仍是新GWZ set estimate及已审weighted conversion；本轮应用核不自动认证其whole proof。finite/Hausdorff读出、arbitraryambient projection与KT链由root/B另审；本稿不自行清其scope flags。来源已有归约重证不作新颖/重大成果，Goal仍active。正式whole-stage review须等root与B全文后另行实读；不提前由本稿认证完整assembly。
