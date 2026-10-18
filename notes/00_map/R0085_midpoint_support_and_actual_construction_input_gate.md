# R0085：中点 packing、原 shading 与真实构造输入资格门

2026-10-18，B 阶段 I。仅作现有一手定理对完整目标的实际输入匹配；未锁 phase II，不写 formal，不构造新成功公设，不宣新维数界或重大性。

## 1. 恢复、旧记录与实际来源范围

已读 R85 working_spec5、GOAL、STATE 当前顶部、ROADMAP 当前入口/冻结表、registry 当前入口、R84 next6。实际查 R29 finite-seed frontier表、R33 primary frontier §4.1、R42 primary/frontier §6及相关元数据。Fraser–Yang 2505.05709v2 已被这些旧稿准确列为“保全方向但限制 midpoint packing”的来源，并非本轮新命中定理。

本轮实际打开 [官方版本页](https://arxiv.org/abs/2505.05709) 和 [v2 HTML](https://arxiv.org/html/2505.05709v2)：当前 arXiv history仍为2025-06-25的v2。新读/复核 Definitions1.1/2.1/2.2、Proposition A完整证明、Lemma2.3、Theorems2.4/2.6、Corollaries2.7/2.11及2.12–2.14和后者证明；为核有限常数，另实际读§3.2的cover输入及§3.3相同cover输入的使用处。不声已全文重证§3.3 bush全部高级证明，不冒下载/视觉核验该PDF或官方核心wholebytes检查。

以下独立核的是这些输入如何或不能来自原ordinary对象，不能把重读旧source标题算新机制。

## 2. 准确对象：全方向仍在，限制的是同一位置集合

原对象是一个固定有界A，以及紧K中每方向的一条单位段，midpoint属于A。packing结论先由upper-box假设的restricted maximal得到，再以countable cover升级。Proposition A的基本机制直接是
\[
 B(0,1/2)\subset K-A,\qquad
 n\le\dim_H K+\dim_P A.
\]
因此只要真正支付 \(\dim_P A\le s\)，便有 \(\dim_HK\ge n-s\)。这里是packing A，不是Hausdorff A。

Theorem2.6的低一维输入是无位置限制、全函数的强 maximal估计
\[
 \|f_\delta^*\|_{L^p(S^{n-2})}
 \lesssim_\varepsilon\delta^{-h-\varepsilon}\|f\|_{L^p(\mathbb R^{n-1})}.
\]
其restricted输出转成集合维数后，改善项中的损失为
\[
                  g_n(s)=h+s(1-1/p).                   \tag{1}
\]
这不是由 \(\dim_H\) 的低维定理替换h，也不是对任意4D权重/非分离族的声明。旧R33已经保留这层假设，不能删掉A而称普通n维新下界。

## 3. 真正可放宽成 hitting set，但免费 ordinary 输入不够小

Corollary2.13比midpoint表述更灵活：同一个 \(P\subset K\) 只需命中所用的每条单位段，可把命中点作为一条半长原子段的端点。此时仍需小 \(\dim_P P\)。这是原subset/clock内操作，不是延长线段或添新点；正角度方向版本可用，而非任意δ依赖的极小方向子族无费用。

ordinary有界K确有一个无需新猜想的hitting set。取间距 \(c<1/(2\sqrt n)\) 的各坐标格超平面，在包含K的固定球内只需有限张；每条单位段至少一个坐标变化≥\(1/\sqrt n\)，必命中其中一张。于是
\[
 P=K\cap\bigcup_{\text{有限张 }H}H,\qquad \dim_P P\le n-1.              \tag{2}
\]
这是实际保所有原段的正接口，不能假装“任选一点”完全无用。但source Cor2.11在 \(s=n-1\) 的下界仅为2。即使形式上给低一维完整maximal \(p=n-1,h=0\)，(1)仍给 \(n-g_n(n-1)=2\)。

所以允许endpoint/hitting point并没有免费给普通高维新收益。需要的是比(2)显著更小的同一P及可控量词；本轮没有从ordinary输入证明这一点。Cor2.14的任意小packing hitting set充分条件不能当已经存在这种P的定理。

## 4. 原小 Hausdorff footprint 不授所需 packing 或有限统一常数

midpoints属于K，只给 \(\dim_HA\le\dim_HK\)，不授同样packing upper。这个差别即使compact也存在：交替取极长自由二进制digit块和更长全零块的紧Cantor集C，在零块末端可用稀少小区间覆盖，故 \(\dim_H C=0\)；每个非空相对开cylinder仍在自由块末端有upper-box维1。若其packing维<1，用低upper-box集合的countable cover、相对闭包及Baire会使某个cylinder upper-box<1，矛盾。同步取 \(C^n\) 同理可有Hausdorff0而packing n。

这个标准校准仅否“紧、小Hausdorff⇒小packing”的裸推论；它不含Kakeya所需线段，不反普通source或任何真实全方向结论。原K的额外线段结构也许有未知作用，但本轮没有其估计。

有限尺度不能以维数记号绕过。§3.2及§3.3实际用的是
\[
                       N_\delta(A)\lesssim\delta^{-s-\varepsilon}.
\]
由同一固定A的upper-box维导出的常数/起始尺度须保持；每δ另选有限midpoint集 \(A_\delta\)，再以“有限集packing维0”取s=0不合法。单尺度需支付真实 \(N_\delta(A_\delta)\)，不同δ的可选集合也未自动拼成同一小packing A。仅有稀疏好尺度cover也不等于packing upper。

## 5. 低维新输入能带来什么，不能冒四维 seed

本库新的M3全函数强L3可以在FY的n4公式中取 \(p=3\)、h任意小，得到restricted改善项 \(4-2s/3\)。这是接受已知强输入后的直接proper应用，仍需同一A的packing/quantitative cover；四维ordinary Hausdorff满维本身已更强于其集合结论。它没有提供无位置限制的四维强maximal，也没有给ordinary n5小A。

对n5，Theorem2.6要求的是四维全函数强maximal输入。OAI4的Hausdorffstatement和已付FSD001/DIR003有限种子不能仅改符号就满足这个函数范数假设；near-full marking门槛、任意函数和任意λ的区别仍在。即便额外假设完整M4，(2)仍只给2，所以主初始化缺项没有被这一步消除。

不将本轮写成KT递推的新数表，也不把R29/R38已付finite-to-arbitraryambient/internalassembly复活成新gap。FY的低维maximal调用具有自己的量词，不能由已有DIM001后果倒填。

## 6. restriction 与平均／逐管 shading 的真实闭包

固定同一A，whole-label restriction保留midpoint约束，任意measurable \(Y_i\subset T_i\) 也不改变它；删label却未必保所有方向。source packing升级选择的是countable cover中的一个固定正角度mass部分，再作有限旋转；不是δ依赖loss后仍声fullD或原N不变。若担心任意选择的可测性，可先闭包bounded cover片（upper-box不增），用紧K的闭incidence投影及所有合法段定义方向集，不需免费连续selector。

若固定A的restricted weak-\(L^q\) bound为
\(\|\mathcal K_{\delta,A}1_E\|_{q,\infty}\le C_A\delta^{-\beta-\varepsilon}|E|^{1/p}\)，p≤q且q>1，真实方向δ分离族的平均density也能收费。令Q为该族所占角度尺度 \(Q\asymp N\delta^{n-1}\)；相邻小角帽内用同midpoint的固定倍宽round tube覆盖原管（保端帽）。weak-Lq的子集积分给
\[
 \lambda Q\lesssim C_A\delta^{-\beta-\varepsilon}|E|^{1/p}Q^{1-1/q},
 \qquad
 |E|\gtrsim C_A^{-p}\delta^{p\beta+O(\varepsilon)}
                        \lambda^p Q^{p/q}.             \tag{3}
\]
这不是把平均擅改逐管，也不需额外λ因子；逐管版本直接取其真实lower。FY所用p=q时Q线性进入。它只说明原shadings的合法应用闭包，不补A的cover假设；任意权跨度或无方向分离族未被免费加入。

## 7. 普通初始化、构造与旧正 gain 的资格判定

这个来源不是方向受限toy：它的原K确实保所有方向；不能以此误拒。但有用proper的s未从原ordinary小Hausdorff集合、原tube/point jointlaw或现有normalization得到。本轮也未发现一个满足完整full-direction及严格低Hausdorff upper的新构造，FY论文的lower theorem不是这种构造输入。

没有证明“ordinary gain⇒存在小packing hitting set”的逆向，故不乱称该结构假设与最终目标数学等价。反面同样没有初始化就不能由proper结论推广。旧CP/PM、PW4的全称正gain等价和restriction/shading冻结仍须遵守；不能把“求一个足够小P”当已经取得的新joint机制或另登记ID。

ordinary方向/小footprint与AD-CW、directHRZ parent/terminal/局部倍率、完整matrix/mixed各κ和真full方向反例四路均未因本source闭合。没有将R84factoring、R82selector/h或更多fixedtimes换名重开。

root随后提出的不同资格候选也在此单列，尚未锁phaseII：原R5方向δ分离管整轴近 \(Z(P)\)，P次数D固定、系数有界，先只看
\[
                  |\nabla P_D(v_i)|\ge\kappa_0>0
\]
的regular-leading分支。这里 \(P_D\) 是最高齐次部分，\(\kappa_0\) 固定，不能在证明后令它随δ任意退化。

这个分支的正几何链可核。整单位轴上 \(|P(a+tv)|\lesssim\delta\)，有限差分给 \(P_D(v)=O_D(\delta)\)。Euler恒等式使 \(\nabla P_D(v)\) 与v近正交。D≥2时，\(\nabla P(a+tv)\) 至少一个分量的最高系数≥\(c\kappa_0\)，Remez给
\[
 |\{t:|\nabla P(a+tv)|\le\tau\}|
       \lesssim_D(\tau/\kappa_0)^{1/(D-1)}.
\]
从平均先heavy到逐管近满densityλ后，取 \(\tau=c_{D,\kappa_0}\lambda^{D-1}\)，坏clock和round端帽共只损固定小比例原markedmass；端帽体积 \(O(\delta)|T|\) 可删的理由是 \(\delta\ll\lambda\)，不是端点measure0。若 \(\eta(D-1)<1\)，则 \(\delta\ll\tau\)，axis梯度转实际shading点只改 \(O(\delta)\)。D=1单列constant-gradient，不使用分母D−1。

固定有限的多数projection kernels可对direction-normal和每个good physical-normal同时横截；按原label选一个保固定比例markedmass的kernel，再保一组固定比例labels。沿其kernel的degree-D一元多项式，\(|P|\lesssim\delta\) 且 \(|\partial_wP|\gtrsim\tau\) 的真实点集在至多D个单调区间内总长度 \(O_D(\delta/\tau)\)。故实际E的fiber积分
\(f=(\tau/\delta)\int_{\ker\pi}1_E\)
有界，而每投影真管上的平均至少 \(\theta\asymp\tau\lambda\)。

方向恢复不能只说finite roots：写 \(v=(u+sw)/\sqrt{1+s^2}\)，非短投影保证s bounded。\(P_D(u+sw)=O(\delta)\)，其s导数有固定lower；将u固定为某投影δ帽中心后，simple-root稳定把s收在至多D个 \(O_{D,\kappa_0}(\delta)\) 区间。每区间只含固定个原δ分离方向，所以投影cap有真实常数upper，未假设CW/PW4定理。

可测阴影仍须付DIR4的连续桥，不能用occupied-cells体积冒 \(|E|\)。取 \(F=\{f\ge c\theta\}\)，每投影管有 \(c\theta\) 真实volume density。共同随机δ格中，所有管总mark数期望≥\(c\theta N/\delta\)，逐phase至多 \(CN/\delta\)，故good phases概率≥\(c\theta\)。在good phase用已付FSD001的稀疏s=3、平均mark版本，可保守得
\[
 |F|\gtrsim \theta^3\delta^{3+\varepsilon_0}N,\qquad
 |E|\gtrsim(\delta/\tau)\theta^4\delta^{3+\varepsilon_0}N.
\]
每time的固定重数/共同graph chart按旧有限转移收费。所有额外λ/θ小幂，在η先依D和最终ε足小时可以吸进δ^ε；因此regular-leading子分支可望以这一真实finite bridge支付近满目标。没有因此声称任意λ的full maximal，或线性的精确λ最佳幂。

已actual核R61 §6–11与R60 §1–4的旧量词：R61假设R4直线参数载体 \(\Sigma\subset\mathbb R^6\) 实维≤3，R60假设空间载体实维≤3；当前R5 hypersurface四维/其一般line参数不属于它们，不能简单套用。但投影法和normal-fiber思想与R53真实quadric转移有共同旧成分，不能凭维数和degree改变就宣新方向。关键剩余仍是leading singular、重复最高因子及δ退化的原mass；没有证明全部G4，也没有把这个proper regular分支当最终Goal或预锁成功题。

反向强度也已核：\(P=x_5\) 属于regular-leading类；将任何R4原方向δ分离、near-full shading族嵌入此H4，并把原Y乘normal δ厚度，得到实际R5管内shading、相同方向数及可比density。G4的 \(\delta^{4+\varepsilon}N\) 下界除去normalδ便返还同强度DIR4。正向上述链又只用DIR4，故在这一方向分离near-full层面是已有输入的真实几何transfer，不宜单列不同gain机制。物理regular的 \(P=x_5-x_1^2\) 仍可有near-contained轴 \(v_1\asymp\sqrt\delta\)，其leading-gradient仅 \(O(\sqrt\delta)\)，不能由物理regular偷授当前fixed lower。

## 8. 阶段 I 结论与停止条件

本轮新核范围是旧v2的实际输入、hitting-set放宽的真实ordinary弱出口(2)、finitecover/packing差别，以及原average shadings的合法应用(3)。这些是输入资格证据，不是新维数下界、branchsaving、major或Goal完成；官方当前版本身份也不认证论文全部proof。

结论：Fraser–Yang作为来源合法，但本项目当前没有支付有用s所需的同一midpoint/hitting-set packing输入。该source不推荐锁phaseII；不继续proper低s、有限集packing0、把4D集合seed改成maximal或把小P作为成功公设。另提regular-leading hypersurface候选的资格检查如§7，数学链仅在所列固定lower分支；是否有实际完整source用途及剩余原mass出口尚待root锁题，不能本稿预定。若没有这种不同实输入，本轮应诚实noqualified，而非以proper分支制造完成。

本稿恰8节，尚非formal，未预认证未来元数据/Git/sync；高级wholeproof仍具名，未经外部同行评审。

实际交叉记录：已全文读A8原DIM/KT审计及其§8 regular-leading追加，逐式核实angular参数 \(s=n-1\)、unsaturated预算、M3饱和入口不改维数幂、随机格可测桥及flat反向；暂无强制修正。A/root侧不以本稿自证充独审，最终是否锁新phaseII仍由root先给完整量词决定。
