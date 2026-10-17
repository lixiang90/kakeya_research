# R0043正式独审：共同核、原计数与§18条件性PW递归

2026-10-17，A（audit_four_dimensional）。已实际全文读取root《R0043_actual_PW_coarsening_and_extremal_class_closure》10节、macro8节、next《R0043_next_actual_polynomial_grain_test》4节及B《R0043_fine_to_coarse_PW_counterattack》7节；读回root最终修补的bounded-chart/activecount、lowercorner、Step4原T/Y、邻接marked-cube和相对尺度段落。对照versioned WZ Def17.1–17.4、原(19)/(20)/Obs3.2–3.4及§18全部到(145)后consistency完成，实图核PDF70/72。本人另写source操作稿，不把自稿视为独立认证；此处逐步审的是root/B推导和最终范围。若干责任由我/B提出后root补写，现明确复核，不假称未参与讨论的外部盲审。

**结论：修后有限fine→coarse PW、无权化、共同whole-clock parent及有界规范下新增PW条件的原操作预算通过。对原§18的适用仍以其余几何结构推导、具名输入和文中明确的bounded/uniform规范为条件。没有完整认证原§18所有几何细节，没有证明五维κ≤ζ、一般到sticky或高维Hausdorff增益。** 不增新颖/重大认证，未经外部同行评审。

## 1. 原law与加强极值类必须一致

root§1现已实修：有限kernel允许任意有限非负权及subprobability，但actual K_d用无权tube counts。须用同一T的uniform counting probability，或先付counting law对ν的domination G，才可转实际无权递归。仅存在一个任意ν可令大部分实际管权极小，不给该结论。B§5也作了同样限定，正确。

PW对所有半代数S、所有presentation复杂度E和所有λ>0统一，复杂度指数A固定，系数高度不计入E。这是BS具名输入的真实有效半代数范围；并非一般o-minimal未定C(S)自动有效。测试的共同平移/仿射pullback仍在同一全称类中。

## 2. 任意相关事件的受限平均式

独立重算root(1)、B(2)。原事件H质量a，B=C0P(E)|S|。tail≤min(a,Bs^(−n))，在(B/a)^(1/n)处分积分即得

    ∫_H q_i(S)dν≤[n/(n−1)] B^(1/n)a^(1−1/n)。

B≥a时以q≤1补足，B=0或a=0平凡。H不需与位置、方向或测试独立。保留a^(1−1/n)是必要的；仅整族mean后Markov不能推出所需λ^(−n)。反以H={q_i≥λ}可恢复原tail到维数常数，所以有限mean整理本身不被登记为新增长。

## 3. fine到coarse的正向证明通过

B§3的kernel等式可直接核：若|y|≤R且δ≤R，则B(y,δ)⊂B(0,R+δ)，所以

    k_R≤2^(n−1)(k_{R+δ}*k_δ)。

对相同graph axis、相同clock积分，得到q_i^R(S)≤2^(n−1)E_u q_i^δ(S−(u,0))。u的分布对所有indices相同；不是每管独选新的测试。Tonelli可用，所有平移S保持体积及presentation，连续平均也没有被当成一个无限集合并。

固定粗管高visit事件的原preimage H，再对每u用§2并平均：λa≤C[C0P(E)|S|]^(1/n)a^(1−1/n)，消a得coarse tail≤CC0P(E)|S|λ^(−n)。因此确实没有ρ/δ、weight-span或额外λ损失；不必也没有免费比较|N_ρS|与|S|。R42的直接加厚缺口不是coarsening不可能性的证据，本轮已严格补齐。

真实coarse axis偏离fine axis O(ρ)时，先以同一fine轴的固定倍ρ cylinder包住，normalized fractions只差固定体积比，再用上述共同kernel。所有fine ancestors共用同一u law。dyadic截面在|t|≤1内含cδ球、外含Cδ球，fine inner与coarse outer的两次占比比较方向正确；half-open边界零测。微小λ与clock端段均未删除。B§§2–4完整证明通过。

## 4. 无权重计数和bounded parent费用

原AD给每个occupied parent的finecount n_j∈[K^(−1)L,KL]。uniform coarse对weighted pushforward的密度比是(N/J)/n_j≤K²，因为N/J为这些n_j的平均值。这个推导不依赖全局N的绝对量级；若原T已删成T′，必须使用T′自己的AD常数。root(5)及B§5没有漏掉这个lower责任。

parent取消则还需要全局信息。root现明确固定有界joint chart，或N≤C_nKδ^(−m)。由occupied-parent AD lower得p_τ≥cK^(−2)τ^m。原lowercorner map ψ_τ(x,t)=((x−b−at)/τ,t)保持clock，pullback体积τ^m，故C_parent≤CC0τ^m/p_τ≤CC0K²；再粗化/无权化得到CC0K⁴。ψ必须用原parameter lowercorner以保dyadic image tree；kernel中心只是形状比较，不能混同成新平移网格的AD lower。

该全局限制不是Def17.1字面自动给出的。无界许多远隔parallel满网保持local AD，却把global最优PW常数降为1/L，单parent常数仍为常数，否掉无界泛化的精确取消。root已明列为有界规范，未认证无界类免费局部化。

修后的bounded-marks替代也通过：平均density≥δ^η使active数≥cδ^ηN；active intercepts有界，局部AD上界给#active≤CKδ^(−m)。于是N≤CKδ^(−m−η)，parent额外付δ^(−η)即可，仍为明确subpower。它要求marks本来处于同一固定box，不证明任意全局marks可以免费移入一box。

## 5. whole clock、原shading与真实递归输入

原(19)共同clock[-1,1]以及Obs3.2的ψ完全匹配kernel。source“rotation使parent竖直”可按文中的clock-preserving shear实现；transverse描述basis可以调整，但计数沿原树或共同image树。没有延长旋转后投影段，也未将短marks当成短管再免费补成unit interval。若另截clock q，R42的q^(−m)费用照付。

root§5现明确(107)/(109)调用的是原T_ρ,Y与原T[T_ρ],Y，费用δ^(−Oη)。不能拿后来T′的δ_ell^(−Oη_ell)硬塞进更小ε1，因为原顺序ε1≪η_d≤η_ell。Y′通过(110)单调及uniformity回传。原平均dense只给选一个dense代表parent，Step1的incident fiber uniformity再传播其multiplicity；没有给每parent或每管免费逐管dense。

shading/point/slab删除不改变whole ν；只在真正删整管时付p^(−1)。平均densityλ0、保留incidence比例f，确有active管比例至少cfλ0。原Step2–3用MX′同时控制单tube shading量与parent incidence，另证T′的AD下界；不是任意dense subset继承AD。内部point refinement有约1/η层，不等于whole prior被归一化约1/η次，这一点对loss至关重要。

## 6. 相对新mesh及κ端点

root的换尺度方向正确：δ_new≤δ^χ给δ^(−Bη)≤δ_new^(−Bη/χ)，须先有真实χ>0再选η。18.1 Lemma5.3给τ/ρ≥δ^(−χ(ζ))，因此该处不是假定尺度比。18.2最终τ=√δ_ell、ρ=δ_ell；预先取阈值δ^{a_j}且a_jη_j/η_{j−1}≫a_{j−1}，再取η足够小，可将原δ损失吸到δ_ell中。所有a_j在δ前固定，未依赖未知countersequence事后选η。

新mesh接近1时不能照搬subpower声称。root§6的screen在极值定理不可用区，用AD平凡管数把loss估为δ^(−O(Bη/η_*))，再以η充分小吸到已预留的δ^(−ε1)。对(113)最终须有ε1≪χ_ellη_ell；原(107)仅ρ误差不能机械外推到这一区间。此为新增PW的预算验证，不是重证原几何全部最优模数。

κ_PW用**这个有界uniform加强类**的infimum，未偷用旧κ。任意最终ε先取有效κ′<κ_PW+ε/2，再用其ε/2形式，确得κ_PW的ε形式。每次调用还保原AD/CW/平均density；新增PW由前述操作支付。固定维数的grain升级和ℓ下降次数有限，translation/affine不增长A，只乘计数常数固定幂。source的point层数不会造成A或PW指数无界迭代。

## 7. 尚未认证的source几何与本轮条件范围

实际全文读原18.1三步与(145)后最后厚化：whole tube操作只有已审restriction、D_ρ与共同ψ；φ_{y,τ}用于描述point结构，不是每tube物理frame。最后厚到δ′^{1−O(η′/ε_j)}可用kernel+无权比较，η′≪ε_j时相对mesh损失可吸收。调整E不能理解成随point任意新造whole tubes；其容许的低量级误差由同一coarse tube保留。

原PDF70实图写Δ_J≈δ_ell，PDF72同j=J叙述却写Δ_j=√δ_ell。root没有假称文本提取错误或已经完整修复density。新PW操作只用明确D_{δ_ell}[T_{√δ_ell}]，不依赖把两者等同；完整grain重证仍须修索引/中间层并付density。**所以本轮通过的是新增PW条件的有限闭包及条件性source回放，不是原Prop18.1全部几何的独立完整证书。** macro与next均保留这个范围。

## 8. 实际测试、macro及唯一下一任务

root§8的Sδ取visited cells固定邻接并，体积与presentation仍O(#E)量级。原marked cube只intersects T，确不能直接计整块交量；修后选接点并纳入B(p,cδ)，graph cylinder在该球内（含clock/截面边界）体积至少cδ^n。有限colors互距10δ，对每T取最多的一色，或保固定重叠常数，得到真实|T∩Sδ|≥cδ^n#Y(T)。同一个Sδ没有随每tube改变；保的是平均M，不是偷加逐管dense。

已知cell presentation Eδ≤C#E太大，PW给的lower不足以认证strictκ margin；nativegrain pieces上界也没有自动解决它。一个粗复杂度上界不证明所有更好presentation或包络不可能，root没有作这种反向断言。实际S/M/E尝试失败被记录，闭包不被升级成高维gain。

已实读macro8节及next4节。停止继续调kernel/relative mesh/先验名合理；下一只是一次actual growing-degree ruled-grain测试，不是已实现的低复杂度包络。它要求实际f的合法延拓/近似、真实h_j offsets、原tube mass和clock、piece数与presentation的完整预算；dyadicLip没有被说成C²，Y_z也未被说成同一集合。各piece分别测试或作并须各付质量与复杂度，shortclock q^(−4)仍在。先核旧Lemma20.2 affine/Taylor和R40 flatgate是否已覆盖该特殊分支，避免等价换名；若只获四维基准或degree费用吃尽saving，一轮即停。相较继续冻结路线调参，这一有明确不同测试类的有界尝试可作为未证下一任务，但本review不预认证其可行或新颖。

最终通过范围如开头所列。无新普通高维维数界、真反例、完整κ≤ζ或major认证；一般K到有界jointAD/CW/PW加强类仍另欠。Goal保持原标准active。本人只交授权source稿和本review，UTF8/control核验后停止编辑，不操作Git。
