# R0024：原角二次标量化与conditional mixed43接入独审

2026-10-17，`audit_four_dimensional`。独立读root的 `R0024_original_angle_scalarization.md` 全文及B的 `R0024_quadratic_scalarization_counterattack.md`。A的source稿由本人编写，原L恢复与incidence-heavy角先验不在本文冒充独立自审，另由root/B核验。

**结论：有限uniform引理、coefficient-weighted扩展及root§4的条件应用通过，可按现有scope归档。** 此结论不证明ell3 whole-matrix affine准备，不处理完整large-τ/weighted projection等剩余责任，未完成mixed43或五维Kakeya。

## 1. 原四时间mass与最大归一化residual

原ν interval cap使每个exact time position的总质量≤K_td；重复标签不应分别当作小atoms。若某scalar quadratic的fit集质量β≥b，则其四次乘积质量β⁴。任一对time相同的质量≤K_td β³，六对合计≤6K_td β³；b≥12K_td时四个distinct positions仍留至少b⁴/2。这一步不需要幂级gap或新AD-lower。

对四distinct时刻，`α_j=1/∏_(k≠j)(t_j−t_k)`消灭次数≤2的polynomials。选|α_j|最大并固定tie rule，得到residual

    R=F(t_j)+Σ_(i≠j)(α_i/α_j)F(t_i),
    |α_i/α_j|≤1.

因此共同scalar w-fit强迫|ψ·R|≤4w，没有小gap的逆幂。固定其它三个times和F值，`−α_i/α_j`正是它们在t_j处的Lagrange系数，所以R是F(t_j)减去一个**固定**vector quadratic的值；其系数允许任意大。分四种j积分，`|R|≤h`的原ν⁴质量≤4a。j的选择只缩小fit事件，没有产生未付的系数union。

## 2. 原slab概率、所有adaptive fits与base

在|R|>h上，事件|ψ·R|≤4w包含于normal为R/|R|、宽4w/h的central slab。故在π×ν⁴这个dominating reference上，residual统计量期望≤4a+合法slab upper。任何bad ψ都使统计量≥b⁴/2，Markov同时控制全部adaptive scalar quadratics。

该推导不要求π是Lebesgue，不要求F bounded/Lip，也不改变原weights。ψ可带重复labels，Bad事件在有限time空间上可由有限多subset的线性可行性刻画，所以可测。

root的`max(q_base,4w/h)`明确保留below-base clipping；超过1则使用trivial1而非越界查询。B稿也只在确有合法q≥4w/h时调用原slab law。两稿没有从h的lower错误推出raw slab width的lower。K_ψ在γ幂外，常数损失没有被偷放入γ以人为减小。

## 3. coefficient-weighted扩展

设|F|≤M、|ψ|≤L，scalar target误差为σA(p)，`A(p)=1+|p₁|+|p₂|`。质量≥b的fit集中，用原interval cap可选三个两两gap≥g=b/(C K_t)的真实时刻，需b≥C K_td。Lagrange的两个系数norm受Cg⁻² max|p(t_i)|控制，因而

    A(p)≤1+Cg⁻²[ML+σA(p)].

σ≤c b²/K_t²支付自依赖项的吸收，给`A(p)≤C(1+ML)K_t²/b²`。同一fit遂成为uniform width `w_u=C(1+ML)K_t²σ/b²`的fit，再用第2节；anchors可随ψ与fit改变，因为系数upper是确定性的all-real结论，不另付选择概率。

root§2.1和B§7的边界校准正确：在长度c√σ区间上取巨大`p_R(t)=R(t−t₀)²`，任何bounded signal都可按误差σA(p_R)拟合；均匀细时间的richness约√σ。因此不能把uniform nonfit无门槛地宣称为weighted nonfit，当前σ≪b²/K_t²条件具有所述有限范围内的正确数量级。稿件没有把此校准称完整source反例或所有prior的必要充分性。

## 4. 原correlated graph的实际角retention

令G(φ₁,φ₂)为g对其余原变量的平均，0≤G≤1。bad ψ由角差pushforward π衡量；若概率≤m/4，原g丢失≤m/4，good原质量≥3m/4。再删conditional graph mean<m/4的角对至多损m/4，仍保≥m/2原质量。因此确可选一个good且conditional mean≥m/2的实际角对；B所用≥m/4是更保守结论。

这只用已经支付的共同product reference与g≤1。没有要求真实time与angles独立，也没有用g-weighted角边际重新声明Frostman law。原角对可在coarse used-cell中作proxy；actual fine角误差已在原relation的τρ误差中，不能另声称所有正code都有同一个exact fine角差。

## 5. Root实际§4的尺度和指数

已逐项核对root的条件设定：真实mixed43的u,v,a是row2，b是scalar，Y从原source就是scalar AD1−κ；未投影mixed32的二维Y。matrix AFF/whole速度lower明确列作输入，未移用ell2 AFF-001。τ由row norm先固定，row F/G也在选择ψ之前定义；后取F_ψ、G_ψ不重新最小化τ。

条件small/middle-τ下，原coefficient-weighted row nonquad缩弱为uniform精度

    h₀≥K⁻Cρ^p, p=2ε₁+ζ₁,
    a≤K^Cρ^ε₂/θ.

实际ν为原fine-index，interval base d=δ/ρ≤ρ³；finite引理本身不要求time已e-separated。M≤K、|ψ|≤C、m≥K⁻C和angle slab常数的损失在retention之后完整保留。

取σ=ρ^(2p)、b_fit=ρ^β，γ可先弱化为min(γ,1)。β<min(ε₂,γp)/100后，选择所有原K、θ、stablechain损失足够小，得到两个真实正指数

    ε₂−4β−O(ℓ),
    γ(p−2β)−4β−O_γ(ℓ).

同时b_fit≫K_td，且σK_t²/b_fit²→0，满足系数吸收。raw query只需upper `q_raw≤K^Cρ^(p−2β)`；root选择更大的合法`Q_*=Cρ^(p−2β−Cℓ)`，指数在(0,1)，故Q_*≥Cρ并覆盖raw query，且趋0。该方向正确，未虚构raw query必须大于base。

最终bad概率远小于原m后，第4节保同一g的scalar coefficient-weighted quadratic nonfit，精度ρ^(2p)、质量阈值ρ^β。另选`6ε₁+2ζ₁<ε₀`，则原graph误差`e≤Kρ^(ε₀−2ε₁)≪ρ^(2p)`。F/G与translation都在同一个角世界中，norm K与γ费用均后取小；没有用两个不同的ψ分别满足两个输入。

## 6. Source和全局scope

root明确该gate还不能调用完整scalar22.5或解决mixed43。以下限制准确：

- ell3 observed A只有N_ρ≤Kρ⁻²，scalar ABC21.2的ρ^(−1−κ)下界在κ≤1时不足；whole matrix AFF的存在仍未付。
- 某ψ下scalar近常只缩小Eψ，不自动缩预先固定的vector τ，不能沿用原stable τ矛盾。
- large-τ删除G项的误差需另付mesh；当前实际应用限定small/middle τ。
- 原fine time到working-grid F/G的representative/weighted projection接口未在有限gate中解决；本gate直接保原ν，未假装它已解决。
- 标量translation图不是一个新d4/ell2完整原Kakeya配置，后续named radial/Kaufman高级输入仍须逐hypothesis核。

认证范围为有限原slab-prior quadratic scalarization、weighted precision扩展及明确条件下的actual used-angle gate。无完整mixed43、五维维数界、真实Kakeya反例或重大/新颖性认证。
