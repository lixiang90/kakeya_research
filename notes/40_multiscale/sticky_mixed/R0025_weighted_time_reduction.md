# R0025：细时间先验到同F/G代表的严格有限归约

2026-10-17，root。服务于唯一scalar curvature engine，不修改长期Goal。B的独立抽样/尾界证明见R0025_weighted_engine_counterattack.md。本稿给一个有限参数网版本，明确原prior与prepared prior的差别。

## 1. 输入与结论

0<w≪1，ν为[-1,1]内有限原标签概率，长r≥w的interval有ν(I)≤K_t r。|F|,|G|≤1；所有scalar quadratics p满足

    ν{|F(t)−p(t)|≤h(1+|p₁|+|p₂|)}≤a，
    h=w^ε₁，a=w^ε₂，0<ε₁<1/4，ε₂>0。

携带0≤g(x,t,s)≤1，reference为Uniform(A)×ν²，mean≥m；g>0时x+S(t,s)距给定A_plus≤Cw，S=(s−t)[F(t)−F(s)−G(s)(t−s)]。设K_t≤w^(-η)、m≥w^η，η足够小于固定ε₁、ε₂。A无须在本抽样引理里有AD性质。

令β=min(ε₂/4,1/10)。存在w-grid上的set B，N=#B≥c/(K_t w)，N≤C/w，以及每个b对应**同一个**原细标签i_b，置F_B(b)=F(i_b)、G_B(b)=G(i_b)，使

    Uniform(B)(I)≤C K_t |I|， |I|≥w；
    mean_(UniformA×UniformB²)g_B≥c m/K_t²；
    g_B>0 ⇒ dist(x+S_B(b,b'),A_plus)≤C'w；
    Uniform(B){|F_B−p|≤w^(2ε₁)(1+|p₁|+|p₂|)}<w^β
                                                对所有real p。 (1)

这里时间位置round到cell centre；F/G值仍是共同原标签。没有免费Lip假设。常数可以依原固定support/error norm，但不依fine原子数。

## 2. 先删轻cell并写清uniform cells的费用

把time按长度w的半开格分桶，质量p_j≤C K_t w；总格数≤C/w。删p_j<cmw的轻格，c选足够小，删去原ν质量≤m/100。因此原g在两个time均保留处的未归一质量≥.98m。

剩余格数N在[c/(K_t w),C/w]内，每格p_j≥cmw。令ν_j为原ν在第j格的条件概率，定义prepared mixture

    ν_hat=(1/N)Σ_j ν_j。

在保留的原标签上，density dν_hat/dν=1/(Np_j)处于[c/K_t,C K_t/m]。故

    mean_(A×ν_hat²)g≥c m/K_t²；
    ν_hat(E)≤C K_t ν(E)/m。                       (2)

后一式用于所有nonfit事件，不能只用timecell的upper容量。此prepared mixture仍是原细标签的law，尚未取代表。

## 3. 一个抽样同时保graph和F/G

各格独立抽X_j∼ν_j，携带其(t_j,F_j,G_j)。对j≠k令g_sample(x,j,k)=g(x,X_j,X_k)，对j=k置0。其mean Z∈[0,1]满足

    E Z≥c m/K_t²−1/N≥c' m/K_t²，                  (3)

因为被丢diagonal在uniformcells的质量≤1/N≤C K_t w，η小使它远小于m/K_t²。由Z≤1，

    Pr{Z≥c''m/K_t²}≥c''m/K_t²。                   (4)

这里只用期望即可，不需假设原g在time上独立。独立性只属于新抽样的不同cells；g内部相关性全部保留。

## 4. 全部adaptive加权quadratic fits：有限admissible参数网

设A(p)=1+|p₁|+|p₂|，归一参数

    λ=1/A(p)>0，z_i=p_i/A(p)，
    λ+|z₁|+|z₂|=1。

一个在sample中非空的coarse fit必有|z₀|≤5（|F|≤1且coarse positions在固定bounded interval）。在这个bounded admissible参数集上取半径c h的finite net，**每个net中心仍选自λ>0、λ+|z₁|+|z₂|=1的实际集合**，不是任意ambient格点或λ=0。可逐格选一个相交的实际点，所以net cardinal≤C h^-4。

任一个net参数q=(λ,z₀,z₁,z₂)，对应真正的real quadratic p_q=z/λ，且A(p_q)=1/λ。其fine事件

    E_q={|λF(t)−z₀−z₁t−z₂t²|≤h/2}

包含于原precision h的加权fit，故ν(E_q)≤a；由(2)，ν_hat(E_q)≤C K_t a/m。

对固定q，独立samples的indicators均值平均≤C K_t a/m。β=min(ε₂/4,1/10)、η小使b=w^β≥4C K_t a/m。Hoeffding给

    Pr{(1/N)Σ_j1_(E_q)(X_j)≥b}≤exp(−c N b²)。

若某coarse quadratic以precision h_B=w^(2ε₁)在sample中命中≥b，除A(p)后，clock rounding误差≤Cw(|z₁|+|z₂|)≤Cw，net residual误差≤Ch。先将net radius常数选小，再令w小，h_B+Cw≪h，所有这些命中点都落某个E_q。由finite union，

    Pr{存在这样的coarse weightedfit}
        ≤C h^-4 exp(−c N b²)。                    (5)

N≥c/(K_t w)、2β≤1/5，故N b²≥c w^(-1+η+2β)；(5)比任意固定w幂小，尤其小于(4)的goodgraph probability。因此存在同一组samples同时满足graph lower与全部weighted nonfit。无无限coefficients的未付union；admissible λ再小也对应合法原fit。

## 5. round clock，保空间误差，区别旧原子质量

把t_j移至其w-cell centre b_j，F_j/G_j不改。B={b_j}是w-separated，N的lower给其interval cap C K_t r。因|F_j|,|G_j|≤1且|t_j−b_j|≤Cw，直接展开S得

    |S(t_j,t_k;F_j,G_k)−S(b_j,b_k;F_j,G_k)|≤Cw。

于是同一个g_sample变成(1)的g_B。若原norm仅≤M，则误差是CMw，不能删掉M；实际应用应先同步空间归一A/F/G，再调用此unit-norm版本，或另写工作网格及loss。

此结论**不是**原ν的restriction。均匀N_fine点分n个格、每格一代表时，代表集旧ν质量仅n/N_fine，可任意小。我们证明的是存在prepared uniform B，使原graph数值与全部nonfit经过(2)–(5)合法保留；随后所有C4/K4,2的CS质量都必须在prepared Uniform(B)下重新生成。不能称所选旧atomic ν⁴/ν⁶质量自动是小幂。

这是finite contradiction的合法归约：若prepared set engine排除所有满足(1)的图，则原加权图不可能存在。无需把代表集宣称新完整Kakeya配置，也无需旧原子质量domination。
