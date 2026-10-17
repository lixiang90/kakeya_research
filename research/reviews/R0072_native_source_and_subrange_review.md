# R0072：原同管双时响应、参数子范围与局部校准独立审查

2026-10-18，A。仅新增获授权的正式 review；不改 root／B、metadata 或 Git。审查结论限以下实际全文对象和原假设，未经外部同行评审。

## 1. 实际全文对象与审查分工

本次 fresh 实际全文读取 root《R0072_kernel_velocity_two_time_budget_and_stop》10节、B《R0072_kernel_response_counteraudit》9节、A《R0072_native_two_time_response_source_audit》8节、两个阶段I文件（A8节、B7节）、working_spec5节、macro6节以及 next《R0072_next_full_goal_reset_after_two_stops》6节。root 读到含独立 γ>1/2 正证、fine δ=h/B^4 buffer 的终版；B末节已读回精确“仅排 gamma>1/2”的修订。另实际重读本地 WZ 原 Lemma19.4 的完整 statement、原分母和其 native 表示开头；没有宣称本轮重新独证 WZ 全篇。

A参与同管公式、core、19.4筛选及子范围正证施工，不能把自己的重复阅读算独审。B已实际全文独核 A8 并另写正式 review；本文件负责逐步独核 root 集成与 B9 的反攻，尤其 B 的有限数字模型和 terminal selected-incidence 失败。阶段I官方身份取证由 A完成，root另行交核；这里不以自己读取自己 hash 表当另一份独立身份认证，更不预认证未来 metadata／同步。

## 2. 原 source、native 标签和 core 的原分母

matrix d5、k=ell3 的正确范围是固定 0<ζ<κ≤2、0<γ≤1，η最后小；原 Y 为二维 AD(2−κ)及 tube-KT(1−γ)。A初稿曾把 R70 mixed43 的 κ≤1／γ≤1−κ移来，经 root 指出已修；fresh A§1／7、root§6及 B§9均保当前正确范围。γ≤κ+O(η)可由 point Φ 的细尺度原 cap 得到，但 γ>1/2与 κ+γ>1不能当两个等价条件。

共同 bounded shear／rotation 后 f=u(t)e1ᵀ。沿同一原 selected T 的真实关系为 y_s=y+hξ_p+[u(t)−u(s)](x1+hφ1)+O(δ)。原 x1项保留；只有固定 root 才可中心化，不能跨 roots 隐去。φ2和原管重数也保留。global 空间 time-window core 的三类容量依次为 P≤K mδ^(−4+κ)、#used T≤Kδ^−4、F≤K mδ^(−3+κ)，原 I≥K^−1mδ^−4。按 I/(6P)、I/(6#T)、I/(6F)删点、管、厚 fibre，每个顶点只计一次，三项总删除≤I/2；其后确有 active point 角度数、active tube 至少 K^−Cm visits及厚 fibre 至少 K^−Cδ^−1个真实 x2 cells。

fibre 指固定原(y,t)和 x1 的 δ-bin，不是 exact 实数 x1等值集。原 X 允许微扰后 exact fibres 全单点，因此这个区别必需。core只授所写 degree lower和继承 upper，不产生新 AD lower／完整配置；原 unused T及 CW分母未被重新归一。整 label、shading删选、平均密度和逐 active tube lower的闭包在三稿中均分别说明，未发现此处漏费。

## 3. 同一管两终时、恢复精度和 γ>1/2 正证

原 Lemma19.4 是局部原配置输入：ρ≥δ^(1/3)、ρ²≤σ≤ρ，以及某实际 anchor 所在原 ρ窗内近常部分的原分母比例。取 σ=ρ^(1+β)，ρ∈[δ^(1/4),δ^µ]，若 u-ball有≥δ^vρ/δ个原 times，则以该球内实际 time为 anchor、用原 #Z_J≤Cρ/δ，给相对质量 cδ^v；CW lower 为 δ^[C(η+v)/γ]ρ^−βκ。先 v≪µβκγ再 η小，可得所需 absolute time cap。Cσ 的固定倍靠参数后 δ小吸收。所用 time窗 m≥K^−Cρ/δ由原全局轻窗删除支付，不把稀薄单窗的相对比例当 absolute lower。

在每条 core T 的真实访问集上选 root和两个终时，删短 clock 的比例≤K^C(q+δ/ρ)，删小 Δu 的比例≤K^Cδ^v，源损失最后小后保 #C_good≥K^−CI m²。固定 root-incidence upper≤K m²；固定 terminal pair的 root-incidence upper≤K I。因此两个真实 marginal domination成立，但不能无损传给进一步固定的 fibre／time图。恢复式仅除非零向量 u(s2)−u(s1)：若其长 d、两 clock≥qρ，terminal labels误差 ε给 errφ1≤CKε/(qρd)、errξ≤CKε/(qd)。root 用 C 的版本依原窗振幅≤Cρ；若统一记为 Kρ，A／B保 K即可。没有 smooth／goodrank 假设，亦不恢复 x2或φ2。

子范围证明另逐式核过：固定(p,t,s)，φ1输出在线段长 ℓ=|s−t||u(t)−u(s)|上；原 tube-KT给至多 K(ℓ/δ)^(1−γ)个 Y细 cells，每 cell原 Φ slab给至多 KD(δ/ℓ)^γ条 selected tubes，D=δ^−κ。O(δ)误差用固定倍细管和邻接 cells吸收；point附近一个细 φ-cell的管数仅固定倍，未漏 φ2重数。于是 upper为 K^CD(δ/ℓ)^(2γ−1)。good pair至少一支 ℓ≥cqρσ，另一终时只付 Km，故总 upper为 K^CPDm²[δ/(qρσ)]^(2γ−1)。ρ≥δ^(1/4)、q=δ^b给 δ/(qρσ)≤Cδ^[(2−β)/4−b]；固定 γ>1/2及小 b后，η最后小，与 tuple lower矛盾。该完整 common-kernel 参数子范围确被排除，细 KT／slab查询的 δ floor和 clock floor均合法。γ≤1/2时指数没有 saving，不能从同一 φ1再乘一个独立 law而制造第二份增益。

## 4. B9数字模型的实际核算与严格失败边界

独立核 B 的20倍整数 b、B=2^b、N为5倍、h=B^−N及实际 δ=h/B^4。Q=2^(b−8)、K1=2^(b−10)、V=2^(13b/20+3)，首个不同数字与尾部的固定间隔保证实数表示单射；四位 buffer使固定线性映射后的 Φ／terminal Y字面 δ分离，不把 digit resolution h误作 source δ。X基数指数为2−16/b，η后选 b大、N最后大可满足原近满 horizontal cardinal。floor(q/R)推前等重，ξ=(0,ζ)的像指数 β=13/20+3/b；其首位差估计给真 Lipschitz和原 coarse coherence，不是 full grid上的不连续 mask。

周期5中 A／B各两位、O一位的逐位恒等式已逐项核：x1、codedφ1、a1=x1+φ1、a2=x1+2φ1的表正确，O位 a2在合法 M字母范围；实际φ=8 codedφ、s1=1/8／s2=1/4使同一真实直线精确给这两个 a_i。初点 Φ维数 β1+β2=3/4，slab指数至少 min(β1,β2)>1/10，平移随 x1 Lipschitz。terminal A_i维数3/5−3/b，加 β恰为5/4=2−κ；固定可逆线性像保持 AD。任意细管逐 dominant-coordinate计数给指数 max(3/5−3/b,13/20+3/b)<9/10，故两个 terminal Y的原 tube-KT确合法。actual输出 pair维数37/20−7/b由可逆恢复(a1,a2,ζ)及真实字母数得到，不是 Jacobian rank冒 Frostman。

这不是 fullsourcecounter。原线全在 physical y1=0，CW至少 cδ^−1；真实初管参数维数11/4−16/b而非4；近满全 clock、初 Y AD及全 terminal Φ／ξ并未构造。更强的是显式冲突：固定 a1、x2、φ2而变 B-only q，s1物理终点和 y斜率相同，φ1却多值；终点同一 ξ_terminal的 selected关系只容 O(δ)宽 φ1，不能保全部原字母。它严格否少用条件的“filled X+Lip ξ+初 Φ+两个正确 terminal carriers ⇒basicness”，不否完整联合约束，更不否普通 Kakeya。

## 5. 一手范围、命名依赖和宏观／next

阶段I两稿及 macro／next已实际全文读。fresh三核心 PDF／README身份与本地 bytes不变，实际 statement重读仍分别为 OAI4的四维 Hausdorff、M3的三维 full-density maximal、elliptic的三维 sphere／有条件几何输入；有限 primary筛查没有找到直接补 ordinary5／剩余 matrix-mixed的工具，不能据此认证 absence／best／first。身份和无更新不证明 wholeproof正确。本次未重新独证这些高级证明，亦未下载新 bytes或增加 source。

本轮正证以 WZ Def17.2–17.4、原 joint4-AD／CW、Y AD及 tube-KT、filled X、Φ AD／slab和 ξ／Φ coherence为完整输入；近常 time排除调用 named Lemma19.4，其 wholeproof沿已存源责任列出。旧 R16 linewise／common-image、R58–59商 upper、R70 mixed43及 R71packet各有自己的作用域，未用名称转移新的 lower或参数限制。A8的源应用已有 B独核，本 review不把它算自审完成。

macro与 next如实保“γ>1/2子范围成立，basicness／典型 fibre lower和其余 common-kernel未付”；按先写停止标准，主要所选机制仍 no-information，冻结双 marginal恢复⇒basicness、数字参数／更多 fixed times／Markov-BSG等续题。R73须先 full-goal宏观比较 ordinary初始化、直接ordinary、完整matrix／mixed和构造，再先锁不同原估计并同轮实际数学。next没有预选或预证一个新定理，也没有以高维旧 KT数值闭包替代任务。

## 6. 必修记录及最终结论

必修范围错误是 A初稿错借 mixed43的 κ／γ范围，现已修并 fresh读回；root的同源子范围正证与 B末段精确 γ>1/2措辞亦已全文／尾段读回。native公式 x1项、δ-thick fibres、相邻 cells、δ=h/B^4、terminal selectedξ冲突均在当前终版明确。未发现剩余阻断性数学修改。

在上述原输入、参数先后和命名高级定理范围内，通过本次内部逐步审查：真实 core／同管双时原质量、恢复误差、完整 common-kernel的 γ>1/2排除，以及 B的局部反攻和失败边界。没有证明 ξ basicness、R59商 joint3-AD lower、完整 common-kernel／matrix／mixed或 ordinary n≥5/general，也没有 fullsource／Kakeya反例。无新数学ID、major、优先权或Goal完成声明；未经外部同行评审。不预认证后续 metadata、验证或Git同步。到此停止新增检索与改稿。
