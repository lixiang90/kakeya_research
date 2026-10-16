# R0023：原 weighted cycle 与 common-line 接口独审

2026-10-17，`audit_four_dimensional`。独立审查root的 `R0023_weighted_cycle_concentration.md` 及B的 `R0023_rank_and_prior_counterattack.md` 全文。本文作者另写本轮source audit；其source发现不在此冒充独立自审，root/B另行核验。

**结论：两份有限稿通过，可以按所列范围归档。** actual small/middle-τ的应用保留原fine-index prior、直接从bounded L-graph提取H，不需要未付的vector BSG或coarse B。证明得到cycle点球cap及有质量的conditional common-line还原，未得到二维增长，也未把dense-cycle Q沿线当作S沿线/MNL001。N5-MIXED32-NQ01仍open；没有完整source/Kakeya反例或重大性声明。

## 1. 向量恒等式和点球cap

直接展开两稿的S，均得

    Q=Δs[F(t₁)−F(t₂)]
      +Δt[F(s₁)−F(s₂)−2s₁G(s₁)+2s₂G(s₂)]
      +(t₁²−t₂²)[G(s₁)−G(s₂)].

与2×4矩阵U作用于V差的写法一致，符号无误。固定s₁,s₂,t₂且|Δs|>u，Q命中半径e的任意球，等价于F(t₁)命中某个vector quadratic的e/|Δs|邻域。系数可能很大，但uniform NQ_h的all-real量词覆盖它们；不需要F/G Lipschitz或rank假设。

|Δs|≤u的原ν²质量≤2K_tu（u≥d_t）；余下每个原fibre由NQ_h控制≤a。因此

    ν⁴{|Q−q|≤e}≤a+2K_tu,  e≤uh.

对任意0≤c≤1，归一cycle law的cap必须再除D=∫c，两稿都保留了D⁻¹。cover lower `N_e≥D/(a+2K_tu)`也只针对同一个c的实际image。重复标签、相同time位置及原atoms都已经包含在interval cap和积分中，没有改为uniform Q-image law。

## 2. 原g直接给有质量的H-cycles

B稿令d=∫g，H由`E_Ag≥d/2`取得。由于0≤g≤1，edge mass≥d/2，weighted Cauchy–Schwarz给完整H四环质量≥d⁴/16。root实际应用采用相同阈值机制。相关性留在H/c中；ν⁴只是dominating product reference，不是声称原cycle独立。

因此本轮的点球估计确可作用于直接原L图，不先要求Lemma13.7的vector版、平衡S-image层或w-separated B。若以后另用BSG或删选cycle weights，仍需重新支付其质量D，不能继承当前完整H-cycles的lower。

## 3. Root对任意dense cycle子集的common-line还原

设0≤c≤1支撑在H四环，原质量D，且其Q支撑距q₀+L至多e。root取row threshold r=√D/4：低row的四环质量至多r²，两个左row合计≤D/8；删|Δs|≤u再损≤D/8。故剩余c_*质量≥3D/4。

先对s₁,s₂、再对t₂作原Fubini，确可固定分离s₁,s₂及t₀，使正支集T有ν(T)≥3D/4。T中每个row的原H degree≥r。投影到L的normal n并除Δs，便得n·F在同一T上的scalar quadratic fit，误差≤e/u；affine line offset n·q₀合法进入常数项，不需要先说该线经过0。

若e/u≤h/4，则沿线分量的h/4-quadratic fit与normal fit合成同一vector polynomial，误差< h，因此其conditional质量≤a/ν(T)。所得ν_T的interval cap为K_t/ν(T)，没有赋新的AD-lower。

原g的质量预算也正确：若H由threshold λ取得，conditional graph mass≥λr，原left-restricted mass≥λrν(T)≥3λD^(3/2)/16。重新生成H|T×B的完整cycles有conditional质量≥r⁴=D²/256，换原ν⁴至少9D⁴/4096。root明确这些新cycles未必继续满足原c的line假设；没有把Fubini选出的切片错误地闭包成同line的全部rectangle。

## 4. B对supportwise全部H-cycles的较强版本

B稿命题2用更强假设：**所有H-cycles**均距同一affine line至多e。其row filtering先保edge mass≥d/4；common-neighbour积分≥d²/16。删除|Δs|<u₀，u₀=d²/(1024K_t)，只损d²/512，故存在分离s₁,s₂，common left set T质量≥d²/32。

全部H-cycles在交换t₁,t₂后仍在其中而Q反号，故线的normal offset绝对值≤e，所有normal Q≤2e。固定任意t₀∈T得到normal quadratic误差2e/u₀。e≤u₀h/1000时，和沿线h/100-fit组合仍在NQ_h允许精度内，给conditional cap≤32a/d²。

T中各row原degree≥d/4，原g的conditional密度≥d²/8；新cycles的conditional质量≥d⁴/256、原ν⁴质量≥d⁸/2¹⁸。它们是原H-cycles，所以在**此更强supportwise假设**下仍继承共同线。两稿的常数与假设层级一致，未将这一版本套到任意dense cycle子集上。

## 5. Actual small/middle-τ的精度和mass

root§5已明确实际uniform精度为

    h≈K⁻Cρ^(2ε₁+ζ₁),
    a≤K^Cρ^ε₂/θ,

θ是已经实际支付的retained mass。它从coefficient-weighted vector nonfit缩弱而来，不是将原physical Δ直接叫h。原角差的逆及K费用有ρ^ε₁余量，并须将AFF/stability损失在ε₂之后取小。

原w=K[ρ+ρ^(3+ε₀)/τ]、`ρ^(3+2ε₁)<τ≤ρ^(3−ζ₁)`给

    w/h≤K^C[ρ^(1−2ε₁−ζ₁)+ρ^(ε₀−4ε₁−ζ₁)].

先选ζ₁+4ε₁<ε₀且2ε₁+ζ₁<1，两幂正；原d_t=δ/ρ≤ρ³。再将全部K/θ损失取小，便有`a+2K_t max(d_t,w/h)<D`，其中D≥K⁻C来自直接H。点球分支因此实质排除“这些全部原cycles的Q像在一个w-ball”这一强退化，而不只在抽象独立prior上成立。

对common-line conditional应用还必须用e/u≤h/4的更强常数，例如取u≥4e/h，并重查2K_tu≪D；这只多固定倍，当前正幂余量可以支付，但不是任意未知line subset都自动有足够D。两稿保留了这个责任。

这段实际应用未使用coarse B sampling，也未将fine |B|当作w-separated cardinal，避开source audit指出的F/G在单个w-timecell可能大幅振荡的问题。r的source下界与large-τ mesh由原source另稿明确记录；有限点球/common-line定理本身不需要r≠0。

## 6. Scope核查

两稿都保留以下关键缺口，未作越界推论：

- Q的四差沿线不推出原S translations沿线；normal component中的left/right coboundary不能从原g关系无费用删除。
- F的一个normal component近quadratic只给付费left carrier T上的沿线scalar quadratic nonfit；原图仍在A×T×B，两端载体不同。
- 当前固定角差是标量，不满足MNL001矩阵分支的二维difference-law slab输入；把它嵌成(ψ,0)会使全部质量共线。
- 点球cap给有限正cover增益，远未达到二维满cover或击败A的2−κ预算。A的scalar投影也可满一维，不能套原scalar基数矛盾。
- large-τ删除G需要另付误差/mesh，当前actual应用没有声称覆盖它；高维radial/矩阵projection新输入仍open。

因此可归档的成果是原weighted cycle的点球退化排除与conditional common-line mass reduction；非二次alternative的排除尚未完成。这不是完整source反例或Kakeya维数结论，也未认证重大性/新颖性。
