# R0051：普通高维前沿、条件17/4的价值与新输入边界

2026-10-17，A。已读固定入口、本轮 spec、R42/R48 有界前沿记录、当前 DIM001/FSD001/RED001/SRC001/DIR003 的实际状态。本轮只核一手版本、结论强度和关键路径价值；没有重做 R38 组装，没有把旧 compact 范围或 `full_source_verified=false` 当作新的数学缺口。以下分开记作者声明、项目逐步核验和未验证应用；未认证优先权、最新最优或重大性。

## 1. 检索范围与原问题

普通问题为任意集合 K⊂R^n 含每个方向的单位线段，目标 dim_H K=n；不先加可测、紧、光滑 selector、sticky 或 polynomial-complexity 假设。本轮有限查询 n5/n6/higher dimensions/17/4/2025–26，随后实际打开以下 primary statements/history。restricted/curved、Nikodym、Minkowski、maximal、finite shaded-tube 和普通 Hausdorff 不互换。搜索未命中既不认证不存在，也不排除未显式列数字的标准推论。

本轮优先对照本库已有结果，未重新下载全部旧论文。root 统一保存新 PDF/metadata；web 可读不等于本地已有字节或 hash。除了明确的读取范围，不声称完整重证所列外部论文。

## 2. 可正面对照的 ordinary 基线与正式版本

| 一手资料及实际读取 | 已声明的对象/数值 | 与本项目的关系 |
| --- | --- | --- |
| [Katz–Tao, *New bounds on Kakeya problems*, math/0102135](https://arxiv.org/pdf/math/0102135)，本轮重读 Thm1.1、6.2 | 普通 Hausdorff ≥(2−√2)(n−4)+3；n6为7−2√2≈4.171572875 | 是明确的正面数值基线及具名递推输入，不是新的项目 recurrence |
| [Hickman–Rogers–Zhang1908.05589](https://arxiv.org/abs/1908.05589)，当前 history 仍只有2019-08-14 v1；另实际读 [AJM 官方43页稿](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-hickman-rogers-zhang.pdf) Thm1.2/§9.2/Fig5 | n5 maximal p>18/13，对应普通 Hausdorff ≥18/5；其方法 n6参数4，Fig5列更好的KT值 | 已发表 *AJM*144(6)(2022)1511–1560。不能把 v1 和正式稿全 bytes 视为相同；R48已核过细节差异 |
| [Zahl, *New Kakeya estimates using Gromov's algebraic lemma*,1908.05314v4](https://arxiv.org/html/1908.05314v4)，当前v4=2021-01-12，本轮重读 Thm1.5 | maximal/dimension 参数 d(n)=max_k min{n−k+2,(n²+k²+n−k)/(2n)}；n5为18/5 | 本方法不供应严格>4的R5 finite input |
| [Chuanwei Gao–Diankun Liu–Yakun Xi2503.11574v1](https://arxiv.org/html/2503.11574v1)，history仍2025-03-14 v1；实际重读 Table1/Thm1.5 | Table1 ordinary n5=18/5、n6=7−2√2；新定理向 constant-curvature Nikodym 转移 | 2025表是交叉核对，不是2026完整最优表；作者是 Chuanwei Gao，不能误写成其他 Gao |
| OpenAI 4D原稿及项目已付 finite/KT 链，见§3–4 | 接受明列输入时 ordinary n5≥4；n6≥17/4=4.25 | 仍不是 n5>4 或一般满维，不能由 n6反推 n5的严格增益 |

HRZ §9.2明确记录其 maximal Kp 到 Hausdorff p′ 的真实传递；本稿的18/5不是只靠“maximal通常更强”一句推断。其 Thm1.2 的范围为 p>1+min_(2≤k≤n)max{2n/[(n−1)n+(k−1)k],1/(n−k+1)}。R13/R48早已核其 unchanged broad/narrow 和 tiny terminal；本轮不再次把同一数值障碍登记成新信息。

## 3. 当前官方4D字节与内部责任

本轮实际打开 [官方4D README](https://raw.githubusercontent.com/openai/math/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/README.md)，仍标作者OpenAI、2026-09-24、原题名。A 的 web contents/PDF 入口失败不当成功核验；随后 root **本轮**通过官方 Git API逐级核到：root tree `1581d4cbdd69a0faf34b2089614fe2a814316a6a` → preprints `df0564b2deaab87e07854b6344d8c2f037682e77` → manuscript `807c97661f95850b7c324356febc3774e7c51c86` → PDF blob `45ec20e423db2a9c70fd6303510bac361e6e9e8a`，1371486字节，与库内相同。这里明确来源于 root 的 authoritative JSON，而非A自己读到API bytes，也不是仅凭README沿用旧hash。

当前 RED001 已在明列 G/WZ/CV/OSS 等具名输入下支付原四维内部全组装、SRC/DIR有限读出以及任意集合 outermeasure 同尺度/finite witness/Hausdorff 桥。FSD001已付 arbitrary fixed ambient 和 real direction exponent≥3 的 Gaussian 投影/unsaturated two-λ应用；KT6.2应用也已独审。故不能把 R29 历史“仅compact”“assembly待审”重复当现行未付项。

仍须忠实保留具名高级定理和新2026预印本的层次：项目没有从零重证每个高级参考文献，也没有因OpenAI署名就当整篇得到外部认证。该边界本身不要求永远递归审旧引理。已付的 source argument 与未证的 n5新几何增益是两件不同的事。

## 4. DIM001 的准确价值与有限损失量词

当前 [DIM001](../../results/reviewed/DIM-001_conditional_six_dimensional_17_over_4.md) 是既有 KT递推的条件推论。FSD001对每个严格0<ζ<1供应 K(6,4−ζ) 与 K(5−ζ,4−ζ)；KT Thm6.2 为 K(n,d)及K(d+1,d′)⇒K(n,(2n+1+d′)/4)，故得到 K(6,17/4−ζ/4)。取极限并用已审任意集合桥，给每个 ordinary R6 Kakeya集合 dim_H≥17/4。

它相对明确KT基线的数值差为17/4−(7−2√2)=2√2−11/4≈0.078427125。该差值是有意义的正面比较，不能据此认证 first/best/major。输入一旦接受，这可能是已有递推与四维 finite input 的直接后果；本轮有限检索无法判定是否早为专家注意或在别处隐含写出。

FSD的实际原计数/密度式为 #E≥c λ²m/K·δ^(s−4+ε_D)/(1+log(1/δ))，s≥3，来源是原方向角cap加投影、heavy和DIR；两个λ各有实际来源。它只在 λ≥δ^η、K≤δ^(−η)时给 ∀target ε∃source η 的近满密度种子。不能宣其等于 n4完整 maximal、任意λ的尖锐 λ^4、或 η(ε)具有线性模数。严格次临界的K(n,4−ζ)已经足够实际KT调用，不需要虚加 endpoint N^(Cε)强度。

DIM当前数学内部application已付；剩余保守flag是具名输入/外部审查与新颖性，不是本轮发现了新的DIM接口漏洞。项目一般高维目标仍active。

## 5. 2025–26一手新输入的对象筛选

以下 history 本轮已实际打开：GWZ2601.14411最新v2=2026-10-11；BS2609.24135仅v1=2026-09-21；LPSW2610.10603仅v1=2026-10-07；Moreira2610.06181仅v1=2026-10-05。对已库版本不假有后续修订，也不凭当前history没有新版本认证旧proof正确。

- [Guth–Wang–Zahl2601.14411v2](https://arxiv.org/abs/2601.14411)：本项目现有具名使用是 Theorem1.1 的 R3 convex-clustering **set** 输入。该输入和 companion完整3D maximal必须分开。
- [Binyamini–Salant2609.24135v1](https://arxiv.org/html/2609.24135v1)：角δ分离真管对同一复杂度E的semialgebraic S，逐管fraction λ给 |S|≥#T λ^nδ^(n−1)/poly_n(E)，没有旧δ^ε。它是精确复杂度输入，并不是 ordinary n5新维数界；R43–44真实PW传递/envelope账本早已支付或冻结，不能因再看到“exact”就绕回旧度数参数。
- [Lai–Pang–Sethi–Wang2610.10603v1](https://arxiv.org/abs/2610.10603)：对象为codimension-two flat flakes及convex Wolff。R40只排/付了fine wholeclock flat提取的具体范围，不能免费作用于R5任意弯曲ruled slice或所有fixed-loss方案。
- [Moreira2610.06181v1](https://arxiv.org/abs/2610.06181)：R4 restriction/maximal的约3.06737参数，不是full4D Lp，更不是R5严格>4。Choudhuri2610.12480及日期异常已在R33存档，不重复据标题扩scope。
- [Di Plinio–Parissis, *Maximal Directional Singular Integrals*,2610.02483v1](https://arxiv.org/html/2610.02483v1)：本轮实际读§1/5.2/6。其TheoremC对有限V⊂Z∩S^(n−1)、dimZ=m、#V≤N^m给 ||M_(V,1)||_(2→2)≤C N^((m−1)/2+ε)。取R5满方向m=4仍是N^(3/2+ε)级，不能误写成 L5 Kakeya maximal或新的ordinary>4。algebraic almost orthogonality是不同机制索引，但本轮没有找到它给所需严格增益的现成应用；未请求root下载、未加入证明依赖。

曲线、p-adic/finite-field、Heisenberg和复杂度受限模型均不因题名包含Kakeya就给本轮普通结论。FD–deLaSalle log-neighborhood上界不是维数反例，Zhang有理mixed-norm不是低rank方向免费满网，R50 forward lift也没有逆向普通高维维数提升。

## 6. 三维完整maximal：实际statement、任意λ与局部曲线范围

本轮已实际读 [OpenAI companion](https://github.com/openai/math/blob/main/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/paper.pdf) 的PDF2–5（Thm1.1、§1.1–1.3）、PDF90–94的§10.2全段和PDF94–96的§11全段；本地 extracted 按 `split('\n')` 为lines79–243、4705–4993。未读/认证整个97页证明。root本轮保存 `literature/primary/openai_2026_three_dimensional_kakeya_maximal.pdf` 及同stem提取，925416字节、97页、SHA256 `49cc52aa3de89f0e91d181b00ee8050fb29635ee0da9f29145d52318e7168204`，官方Git blob `fa215607c58ade54fc6d60dec81530b33f15ab0c`；该bytes核来自root，A的先前web失败不是下载成功。官方README日期2026-09-23。

Thm1.1的实际全量词是∀ε>0∃Cε<∞，∀0<δ<1，∀复值f∈L3(R3)，||Kδf||L3(S2)≤Cε δ^(−ε)||f||L3(R3)，管长1、半径δ、普通sphere surface measure、中心任意。§1.1式(1.1)明确为任意0<λ≤1的真实shading立方代价：角δ分离单位管、|Y(T)|≥λ|T|时，|∪Y(T)|≳ε δ^ε λ³∑|T|。不是把集合维数statement当定量输入。

**此处可自含核其应用强度。** 固定δ-separated方向的管T_i，令E=∪Y_i。各方向周围取不交的cδ角帽；对应T_i可由该帽方向的固定数单位Cδ圆柱覆盖，sup至少捕获固定比例的原Y_i，故K_(Cδ)1_E≥c |Y_i|/|T_i|。这里不删端帽，因λ可任意小。将Thm1.1立方积分到这些帽，得

    δ² Σ_i (|Y_i|/|T_i|)³ ≤ Cε δ^(−3ε)|E|.

Jensen给任意平均λ=(Σ|Y_i|)/(Σ|T_i|)的 |E|≥cε δ^(3ε)λ³δ²#T；最后重命名ε得到(1.1)。没有near-full门槛，也不用删一半标签再丢第二个λ。若原权在每δ-direction bin总量≤α，同一角帽的重叠总权≤Cα，原加权版同理为 |E|≥cε δ^ε λ³δ²W/α，W=Σω_i，λ为原加权平均密度。该推导仍须保真实单位管、角bin cap与统一长度，不能把α或short-clock缩放漏掉。

§10.2实际不是在中间临界式直接令p=2。Prop10.2先对p>2、h(p,0)=0得离散式(10.19)：#A≥c_p,ξ N^(−ξ)nN·max{N^(−1),λ}^(p+1)，每条线只需c max{1,λN} marks。式(10.20)用真角分离控制**整clock** plank；(10.21)给direction distribution，λ≥N^(−1)时多余λ^(2−p)被N^(p−2)吸收。小λ单独积分，cell averages/有限dyadic levels才得到(10.18)的loss(p−2)/3+κ。最后先按ε选p接近2，再固定κ；所有常数独立δ/f/λ。这是全密度改善相较现有DIR/FSD近满种子的实际不同处。

§11并没有普通n5新定理。Cor11.1由具名GLX Proposition2.3给**三维**Euclidean/constant-curvature local Nikodym，1≤p≤3、q=2p′、loss δ^(1−3/p−ε)。Cor11.2只给固定translation-invariant phase φ(x,t;y)=x·y+ψ(t;y)，需Hörmander及Bourgain条件，具体为 det(∇²_y∂tψ)≠0 且 ∇²_y∂t²ψ=c(t;y)∇²_y∂tψ；phase/chart和比较常数先固定。不能把任意WZ的f(t)或8参数ruled slices改称该类。例如(tI+t²diag(1,2))的自然二次phase其两Hessian一般不成标量比例，不受这项曲线转移免费覆盖。

本库旧 `openai_3d_maximal_source/05-inputs.tex` 只是一节set/plank输入，R38使用它的相关接口不等于已经用过整个full maximal。新的Thm1.1若接受，确实比near-full set estimate多任意λ的均匀量化；但本轮未找到已读取primary中的现成 theorem 将它自动变成 ordinary R5>4 或4D完整maximal。R48真实HRZ终点仍是原R5 variety邻域管族，维数3并不自动成为R3 straightline模型。新fullLp消除了“只有近满λ”的一个强度差，却不支付原clock、曲面straightening和角重数；不重算R13数值，也不预认证整97页。

## 7. 本轮候选排重与待合并事项

root/B正比较三个不同机制：真实curved spray模型、3D full maximal输入、有限有理投影旧状态纠正。前者须analytic/semialgebraic、4参数unique-path，R40 source slice γ=p+tq+f(t)(a−u−tv)一般8参数，即便f=tI也出现6参数且可任意加速度；不得把它免费塞进新spray定理。第三者若出现真实既有SD反例，应先纠正R46“未证未否”，不能改q/权重后继续同路线；A在此不提前认证尚未审出的反例。

R50已经证明一般smooth保原clock lift存在性等价于同codimension的affine变分lift，不再用Hessian/selector/换clock改名重开。R49一般→sticky、R48HRZ终点、R47cyclic、R43–45PW/四臂等按各原scope冻结。新输入可产生真实不同问题，但须保原质量、逐管/平均密度各自闭包与一轮可证伪目标，不能只把已付4D有限种子重新命名。

## 8. 本phase停止与审查边界

有限primary phase已完成当前基线/版本/价值核对。没有在实际读取的ordinary primary找到明确覆盖n5严格>4或另列n6≥17/4的statement；这不认证无此结果。3D companion实际PDF的局部statement/应用范围已补；最终唯一后继由root决定，并在实际全文读root/B/macro/next后写正式独审。尚未认证root未写的metadata/registry或Git，也不把宏观审查当新数学成果。Goal保持active，未经外部同行评审。
