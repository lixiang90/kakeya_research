# R0010：随机层标签对全部二次chart的统一质量界

2026-10-17，root。任务N5-HOR-ZERO-01。本文给出level-coloring模型的统一随机标签步骤；模型、profile/angular及单层cap见同轮R0010_zero_depth_counterexample_attack.md。已由audit_four_dimensional逐步独审（research/reviews/R0010_random_label_review.md），RL4/RL5另经lifting_obstructions在模型稿§9独审；不声称Kakeya反例、新维数界或重大结果。

## 1. 固定模型与要证的统一界

固定L>0、M>6L、δ=N0^-M（dyadic取整），λ为[1,2]上的δ格，共n≈δ^-1层，各层概率πλ=1/n。每层可见prior νλ为Q(t,Y)=tY2+Y1Y3=λ的三参数δ-grid加六系数独立δ盒噪声。混合νvis=Σπλνλ在t∈I0=[1/2,3/4]有g_t≤C；每层对任意正宽度空间全块fit统一满足

πλ νλ(G) ≤ C K^C δ^(1/2)q^-3 J。

这里G是长度q的时间块上、空间矩阵D（J=|det D|）和affine center的完整trace fit，fit slack为K。隐藏初值w0=cλ+e、W取独立极小均匀盒，e,W尺度η=N0^-U，U>M+L+10；cλ∈[0,1]稍后一次性选择。native P*=w、B=1，原incidence为1_I0 νdt，未归一化。

取终端a=N0^-L。要选出同一个有限tag向量(cλ)，使**所有**长度q、矩阵D、center、二次P及K≥1的chart current-test事件均满足

Sθ ≤ C K² a νvis(Gθ) + C (log N0)² maxλ{πλνλ(Gθ)} + r_N， (RL1)

其中r_N比N0的任意固定负幂更小。θ只含一个chart的固定维参数；任何复杂assignment与selection先扩大到该事件，不进入θ。标签不是world或观察feature。

## 2. 固定维测试的初等pattern界与quadrature

唯一计数工具如下：固定数目、固定次数的实多项式不等式，参数为固定维实向量θ，在m个输入点上的Boolean取值模式数≤(C m)^V，C,V固定。证明可把θ的全部有界次数单项式提升为一个固定维向量；每次求值的每个条件成为该向量上的affine linear form。m个超平面的全部faces（包含零号）数为O(m^V)，由逐个加超平面的归纳得到。实际单项式像只是该空间的子集，模式不会更多。任意实常数高度与大小不影响此界。

因此对任何概率测度Π，这类set family有有限ε-quadrature：存在mε≤C_V ε^-2 log(2/ε)个等权点，对所有tests的Π概率误差≤ε。简证：取mε个iid点及ghost sample；单个ghost均值集中把偏离Π的坏事件转成两样本偏离（付固定因子）；条件于成对样本后随机交换，Hoeffding加≤(C mε)^V个模式的union bound给C(Cmε)^V exp(−c mε ε²)。选大常数使其<1，故存在该quadrature。增加一个有限实参数c仍为固定维；同样可同时逼近所有(θ,c)。此处只是存在性积分工具，不是输出数据或chart labels。

在每层λ，把z记为该层原visible trajectory、hidden e,W与归一化block time τ∈[0,1]，其概率Πλ固定且与cλ无关。原时刻t=t0+qτ。令

Gθ(z) = {整条visible trace在[t0,t0+q]满足空间fit}；

Hθ(c,z) = Gθ(z) ∩ {t∈I0, |P(t,Y(t),c+e+tW)|≤Ka, |Pw(t,Y(t),c+e+tW)|≥1/K}。

Gθ不依赖c；Hθ⊂Gθ。Gθ由两个endpoint上的norm平方不等式表达，因为visible motion及center仿射、norm凸。使用D^-1的九个entries作为参数，不需要对inverse取网格。small-value/derivative条件平方后也是固定次数；P有总次数≤2。全部条件都是上一段的固定维、固定数量、固定次数多项式tests，q、t0、K、center及P系数都允许任意实值。

令ε_N=exp[−(log N0)²]。**先于随机tags**，每层选同样数量m_N≤C ε_N^-2 log(2/ε_N)的quadrature点zλ,j，同时逼近所有Hθ(c,·)及Gθ，误差≤ε_N。m_N虽可为quasipolynomial，只用于分析证明；它不进入prior、worlds、labels或tempered输出。

## 3. 一个完整的ghost／swap一致偏差引理

独立随机取cλ∼U[0,1]。设

Fλ,θ(c)=πλ E_z 1_Hθ(c,z)， bλ,θ=πλ E_z 1_Gθ(z)。

用上述等权quadrature定义F~λ,θ(c)、b~λ,θ，b~*=maxλ b~λ,θ。它们有

0≤F~λ,θ(c)≤b~λ,θ≤b~*，

Σλ|Fλ,θ(cλ)−F~λ,θ(cλ)|≤ε_N，

|Σb~λ,θ−Σbλ,θ|≤ε_N， |b~*−b*|≤πmax ε_N。

若b~*=0，所有F~均为0且ΣF≤ε_N。否则定义gλ,θ(c)=F~λ,θ(c)/b~*∈[0,1]。在任意2n个tags(cλ,c′λ)上，**一并**计算Hθ(cλ,zλ,j)、Hθ(c′λ,zλ,j)和Gθ(zλ,j)的sign patterns，数≤R=(C n m_N)^V。每个pattern决定所有quadrature计数及b~*，所以也决定整个g的2n个数值向量；除法不会产生新的连续自由数值。

记Sθ=Σgλ,θ(cλ)、µθ=ΣE_c gλ,θ(c)。以下uniform tail不要求同分布的gλ：

Pr{存在θ: Sθ>2µθ+t} ≤ 3 R exp(−t/98)。 (RL2)

证明：对坏的c样本及其某个θ，独立ghost的S′θ均值为µθ<Sθ/2，Markov给Pr{S′θ≤3Sθ/4}≥1/3。故坏事件概率至多三倍于存在θ使D=S−S′≥T/7且T=S+S′≥t的两样本事件。条件于每对未排序tags，再独立交换每对的顺序。固定θ数值向量后，D=Σελ(gλ(cλ)−gλ(c′λ))、T固定；因0≤g≤1，Σ(g−g′)²≤T。Rademacher指数矩给Pr{D≥T/7}≤exp(−T/98)。对≤R个向量union bound即(RL2)。参数取值与坏事件可用有限semialgebraic编码或outer-probability版本处理；正概率的好tag向量存在即可，不要求选择算法。

取t_N=C_V log(C n m_N)+C log N0，常数大到使(RL2)<1/2。因为n≈N0^M且log m_N=O((log N0)²)，有t_N≤C_M(log N0)²。于是存在同一组tags，对所有θ：

ΣF~λ,θ(cλ)≤2ΣE_cF~λ,θ(c)+t_N b~*。 (RL3)

## 4. 期望small-value界与回到原积分

固定任一quadrature点z，P(t,Y,c+e+tW)是c的一元次数≤2多项式，导数就是Pw。原Lemma2.9的初等单调分支论证给可用c总长≤4K²a。因此

E_c 1_Hθ(c,z) ≤ p_K 1_Gθ(z)， p_K=min(1,4K²a)。

逐quadrature点相加得ΣE F~≤p_KΣb~。由(RL3)及uniform quadrature误差，

ΣFλ,θ(cλ) ≤ 2p_K Σbλ,θ + t_N b* + (3+t_N)ε_N。 (RL4)

这就是(RL1)，r_N=(3+t_N)ε_N为superpolynomial小量。全部tags在此固定，此后prior不再随机。估计同时适用于所有chart参数，包括事后从这些tags选择的P、D、center及time block。

## 5. 任意真实chart的horizon下界

任意chart assignment/selection先扩大为Hθ；归一化block time给其m/q≤ΣFλ,θ(cλ)。如果该块与I0不相交，m=0不能参与真实覆盖；否则取任意t*∈I∩I0，visible whole-fit蕴含Y(t*)落空间椭球，g_t*≤C给νvis(Gθ)≤C K³J。单层cap给b*≤CK^C δ^(1/2)q^-3J。故

m/q ≤ CK^C [a+(log N0)²δ^(1/2)q^-3]J+r_N。 (RL5)

本模型所有深度n(r)~log1，特别n(L)=1。真实floor是m/q≥K^-1J。任何允许的tempered chart sequence有J≥N0^-B（固定有限B），K=N0^o(1)，故r_N/J比任意固定负幂更小、K^C a→0。于是(RL5)迫

q³≤N0^o(1) δ^(1/2)，即 h≥M/6。 (RL6)

进一步incidence selection仍被原νdt支配，典型密度指数由原选择lemma保留；已固定的uniform参数界照样适用。任意subsequence也不改变该固定幂。不存在通过任意二次test、复杂assignment或极薄但tempered空间框逃过(RL6)的系统。

因此对独立稿已核的完整exact/profile/angular模型，H≥M/6>L。本uniform lemma已独审通过；模型稿§8另给q=δ的真实终端atlas，root独核其原floor、常量覆盖及own-list，得H≤M。整体内部审定入口为results/reviewed/HOR-002_zero_depth_one_high_horizon.md，未经外部同行评审。
