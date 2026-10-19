# R0101：半代数一手接口与原加权质量独立审查

2026-10-19，A／audit_four_dimensional。本稿审查 root 与 B 的独立推导，A 自己的有限推导不算自身独审。结论是下述有限范围全文通过、无未解决强制项；不是完整 κ1／ordinary 结论，未经外部同行评审。

## 1. 实际全文对象与审查层级

本次实际全文读 root `notes/40_multiscale/R0101_semialgebraic_witness_boxes_and_original_mass.md` 十二节、B `notes/00_map/R0101_native_graph_witness_and_complexity_gate.md` 十节及本人 A 稿十节；两份 reselection／working spec 各五节；最终 macro、next、source scope、round 各六节。B§5 sampled-root 的修订另实际读回。R76 原主稿十二节本轮全文读回，原 WZ Def17.2–17.4 的 native AD、tube-KT、Z 与逐管访问来源也实际核对；没有从抽象超图反向假造这些源输入。

一手实际读域为 FPS1502.01730v3 的 §§1–2、4相关完整段及 Rubin2407.15518v2 的相关定义、Th1.3／1.6、完整 §5.2 Th5.1／density proof；本轮实际打开官方 history 和对应 HTML。FPS current v3 为2016-10-14，Rubin current v2为2024-08-14。没有把两篇全部高级 polynomial-partition／cutting proof、算法实现或档案字节核算充作本人独立认证。R44、R45 的实际所读原预算／selected-KBL接口用于排重；不凭旧轮题名推新适用性。

## 2. 精确源量词、权重和 unequal parts

FPS 的 fixed-format 输入是精确 k-partite 关系，而非任意 selected mask；D 是逐 vertex block 次数，故原本例 D=1 与 total degree2不矛盾。其 density theorem允许各部有限不等大，constant／exponent仍依固定 ambient、谓词和次数。Rubin Th5.1直接给不等大各部 partitions，非齐次 boxes 的总 **product cardinal volume** 至多 ε∏N_i；不能换成未经加权的 bad-box 个数比例。其正文 Th1.6／§5.2 为正幂 ε^(d+1+ζ)，abstract 倒数幂不采用；更尖 d+1版本的 sharpness 另有输入，本文未免费调用。

root§3／B§3的正面引理核算正确：若 0≤h≤1、supp h⊂R、Σh=θV，取 ε=θ/2，则 bad boxes 去掉至多 θV/2的原 h，齐次 nonedge boxes 的 h为0。至多 C^k(2/θ)^(k(d+ζ))个剩余 boxes中，某个完整几何 box保至少 cθ^(1+k(d+ζ))V，原质量比例至少 cθ^(k(d+ζ))；每侧 cardinal比例也至少前一幂。h可任意相关、无需可定义。该证明只补全几何 R，不补全 selected h，也不自动保每根管全部时钟。

root未把任意 vertex概率权重当源字面结论。其注明的 extra-label rational cloning 延伸可用：精确谓词忽略新坐标，必须支付 ambient d→d+1；映回全原标签权后，非负 h质量不减，有限支持的实权可有理逼近并取固定输出子列。当前实际 g／h由原管重数 M0归一到[0,1]，无需此扩展。若仅 h≤M，必须先以 θ/M计 density。此层权重与任意 edge mask分开，root／B未混同。

## 3. 原 sameT、十三维编码与真实 witness 分母

root§1、4–5／B§2、4保 R76 bounded matrix33 κ1 det-large的实际 H*、原 N、两个 native端点和每根管完整原 S_T；H*/N的 δ²费用保留。每个 T,u事先确定实际原 w(T,u)∈Y_u，令 h为其 M0归一计数，严格有 Σ_w h=g≤1、Σh=Σg。不能把几何 supgraph 的新边当原管 lower，也没有在不同用途换不兼容 witnesses。

第三顶点 (u,C_t,C_s,B,w)有1+4+4+2+2=13坐标。root用不进入谓词的闲置坐标区分前两部，并将第三部 u平移作 tag，三部仍可放 R13且精确关系不变；B用 R14 的安全加tag版本也合法，只是指数更保守。四个 L∞ inequalities 各 total degree2、FPS每个 block degree1。rough F、δ依赖 coefficient和离散 Y只作为顶点，并不增加公式格式；反之消去任意 Y成员关系不免费维持固定复杂度。

原 native Y_u 的 AD1给 W=Σ_u|Y_u|≈_K mδ^−1，故 θ_w=θm/W≈_K θδ，原质量本身未减少。对非空完整 box，固定一对端点后每个 u只有 O(1)个允许的 δ-separated w，第三 prior比例至多 CKδ。root／B均明确这不是质量损失证明，也不迫 clock投影小。将 θ_w代正引理的保证只是固定幂δ，不能误读成原near-full θ下的 subpower提取。

## 4. 逐管 farclock、native strip 与 actual 单 box 质量

root§6–8／B§6–7的额外原质量证明独核通过。取 r=δ^c，先用原 Z的δ分离以及每根 H*管 |S_T|≥K^−C m、m≥K^−Cδ^−1：删锚点附近两个 r窗至多 C(r/δ+1) visits，比例≤K^C(r+δ)。η相对c足小、δ最后小，即每根管保一半，继而总 M_f≥M/2；不是由平均密度赠逐管 lower，也未把删后配置重新赋全部 Def17 lower。

完整 witness box交 far clocks后固定一个 u，λ=(u−t)/(s−t)满足 |λ|,|1−λ|≥r/2，实际系数满足 C_t/(1−λ)+C_s/λ=I。由三角不等式 max(||C_t||,||C_s||)≥cr；无需满秩或最小奇异值。固定另一端与同一个第三 w，至少一端落在宽 a=Cδ/r、长 O(1)的 strip。δ≤a≤1时，原 Def17.3／17.4 tube-KT(δ,1−γ,K) 给 a-cover≤CKa^−(1−γ)，原 native AD1 upper 给每 a-ball≤CKa/δ点，除原 |Y|≥K^−1δ^−1得到相对 CK³a^γ。长 O(1)以固定数量 unit tubes处理，未调用 sub-δ或新裁切集 ADlower。

最后必须使用比 h≤1更强的 Σ_w h_f≤1，才能得到 h_f(Q)≤|Q_A||Q_B|m，以及 h_f(Q)/M_f≤CK³θ^−1(δ/r)^γ。θ≥L^−1、L≤δ^−β的原 R76小损失范围中，先选β<γ(1−c)/4，再取η小，指数严格为正。任意 B个 boxes 的 retained质量至多 B倍此量，重叠不妨碍 upper。因此 δ^−o(1)个本编码的完整见证 boxes不能保固定比例原质量。该结论使用原源额外条件，不能仅由第三 prior稀释推出；本人A旧“尚未有此结论”已相应更新。

## 5. 反攻修正、合法闭包与旧机制边界

root§9的二维随机 selected 图反攻自含：q=ceil(4log₂n)，完整 q×q概率上界 n^(2q)2^−q²趋0，边数低于 n²/4 的 Chebyshev upper为4/n²；故确定性正密度 mask存在。B同类反攻与本人三部版本均只反 selected免费补全，完全不反第2节的几何完整／原质量正用途。它们未实现全 T AD4／CW／filled X／Φ，不能冒 fullsource反例。

本次唯一强制修正已解：B§5最初从2q个 sampled points 交替真假写 sD≥2q−1，忽略根可恰落样本、一个根触发两次变化；已改为 sD≥(2q−1)/2并实际读回。root§9原已采用正确1/2。复杂度随样本数增长的结论不变，无其余未解决强制项。

顶点 restriction保持固定几何公式；任意 tube／mark restriction仅能继续当 bounded mask，并按新真实 density调用。保总访问后重取 heavy可付平均→逐管，却不能保旧全部 S_T／原 N比例／normalized CW。R45 selected-tuple KBL本已容许任意选中超图，Cartesian不是其先决；R44共同测试／whole-index/CW费用也没有被新box定理消除。actual mass upper只限“同一第三 w对全部端点适用”的完整 box，不排允许 w随端点变化的原关系或所有半代数方法；未产生旧全称gain的双向等价新命名。

## 6. 最终判定、宏观范围和停止

限定范围全文通过：具名 regularity到任意 bounded原权的真实几何保量；实际 fixed-format十三维编码及全部产品分母；逐管 farclock；原 native AD1／tube-KT给完整 witness box的严格固定幂质量费用；有限反攻及合法restriction范围。本人A证书已由root／B实际独核，本formal的独立审查对象是root／B链，不以本人自证代审。

macro6／next6／source6／round6已实际全文核，保持普通／HRZ、sticky全rough及ordinary桥、真实同集full方向strict低维反例的完整目标；当前没有 qualified next gain。冻结直接 witness completebox与 d／D／ζ／θ参数续轮，未否可变见证或全部几何方法。legacy ordinary／完整branchsaving时钟24与本轮actual信息分列，Goal active；full κ1、ordinary或Hausdorff新界均未证，newID／major／novelty声明均无。

“全文通过”仅指上述本文实际读取对象的有限推导、调用资格及停止结论；FPS／Rubin和原WZ高级 wholeproof仍为具名输入，未经外部同行评审。本稿不认证元数据、档案计数、未来 Git／同步成功或未亲读的官方字节复核。
