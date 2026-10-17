# R0050：全时第一变分与smooth coherent lift的完整范围

2026-10-17，root。Goal active。本文纠正R12/R49对空间仿射限制的判断，并将既有LIFT005更新到其证明实际支持的范围；不新立数学ID，不宣重大性或高维Kakeya新界。正式独审另存，未经外部同行评审。

## 1. 原命题与需要纠正的判断

令m=n−1≥2、F(t)=tI_m+t²B。原smooth lift要求，在有内点的y,w∈R^m、ρ∈R^s及非退化时间区间I上，存在smooth空间submersionπ_t:R^(m+s)→R^m、a(y,w,ρ)、Θ(y,ρ)，使

    π_t(a(y,w,ρ)+tΘ(y,ρ))=w+F(t)y                 (1)

对全部参数和整段t成立。Θ独立w，方向rank按原(s,ν)-lift定义。R50目标为m=2、s=1、ν=0、B=diag(1,2)。

R12完成空间仿射π_t=T(t)z+c(t)分类，并把一般非线性π列为未排除；R49据此选择更大class。实际检查发现：**虽然映射class严格更大，本parameter-linear目标的lift存在性与空间仿射class等价**。旧证明在同一固定参数点只使用一阶变分式，所以并不需要原π空间仿射。这是应更正的范围与等价性判断，不能把它包装成新的curvature机制。

## 2. 精确全时变分引理

固定一个内点P=(y₀,w₀,ρ₀)，令z_P(t)=a(P)+tΘ(P)。定义

    T_P(t)=D_zπ_t(z_P(t)).

对(1)关于原参数一次微分，所有a/Θ导数均在**同一个P**取值，得到对每个t∈I的精确等式

    T_P(t) a_w(P)=I_m,
    T_P(t)[a_y(P)+tΘ_y(P)]=F(t),
    T_P(t)[a_ρ(P)+tΘ_ρ(P)]=0.                    (2)

π的Jacobian可以沿线随t变化，但同一P的三种微分共用同一个T_P(t)。这里只对参数微分，没有对t取有限阶jet，也没有用非线性空间坐标拉直π。

令u=(u_y,u_w,u_ρ)，构造真正的新lift

    a_lin(u)=Da(P)u,
    Θ_lin(u_y,u_ρ)=D_(y,ρ)Θ(P)(u_y,u_ρ),
    π_lin,t(z)=T_P(t)z.

由(2)，`π_lin,t(a_lin+tΘ_lin)=u_w+F(t)u_y`对所有u与整段t精确成立。T_P a_w=I迫rankT_P=m；Θ_lin的方向rank与原Θ在P的rank相同。限制到小compact参数balls即可满足原定义的共同域/线段包含条件，取Ω_lin=R^(m+s)×I的适当邻域。

反向任何空间仿射lift本就是smooth lift。故对任意固定smooth F(t)，只要目标对w,y是上述线性形式，就有

    smooth coherent (s,ν)-lift存在
       ⇔ 空间仿射且参数线性的coherent (s,ν)-lift存在.       (3)

这不是说原π必须affine，也不是说原a、Θ是线性的；它重新构造一个同目标、同codimension/rank的variational lift。一般非线性依赖w,y的目标X不自动满足(3)。

## 3. 同轮自然推论：quadratic族的最小codimension

由(2)的共同常数右逆A=a_w(P)，取常数S=[A,K]∈GL_(m+s)。在这个常数空间基下

    T_P(t)S=[I_m,H(t)],
    a_y=[C;R],  Θ_y=[D;L],

其中H为m×s，C,D为m×m，R,L为s×m。因此

    tI+t²B=C+tD+H(t)(R+tL).

矩阵多项式 `P(t)=t²B+t(I−D)−C`在整个I每点rank≤s。当s<m，每个(s+1)-minor为一个标量多项式，在非退化区间恒零，其最高次t^(2(s+1))系数恰是相应B-minor。所以

    rank B≤s.                                           (4)

s≥m时(4)本已平凡。此推导不需要H解析、不延拓到大t、不取不存在的t→∞极限；也不需要Θ_ρ满秩来得到这个codimension下界。关键是全部w平移和Θ独立w。

源Proposition2.5(i)以B=UV、s=rankB构造

    π_t(x,z)=x+tUz,
    a=(w,ρ),  Θ=(y−Uρ,Vy),

方向loss为s−rankB²。因此在允许direction loss的原lift类中，quadratic族的最小codimension恰为rankB。这个初等必要性/标准充分性的组合不是新的Kakeya维数增益，也不认证源外的新颖性。对B=diag(1,2)，所有本smooth保clock lift都要s≥2，特别排除(1,0)。

## 4. codimension-one full-direction分类同旧LIFT005

对s=1并要求D_(y,ρ)Θ rankm+1，(3)已允许调用旧分类。为自包含，写出剩余方向rank的关键计算。在同一常基下T_P=[I,h(t)]，记

    a_y=[C;r], Θ_y=[D;ℓ],
    a_ρ=[p;u], Θ_ρ=[q;v].

则F=C+tD+h(r+tℓ)，0=p+tq+h(u+tv)。u+tv不为零多项式，否则p=q=0且Θ_ρ=0，违反完整方向rank。乘u+tv消去h，不先除可能为零的分母：

    (u+tv)(tI+t²B)=(u+tv)(C+tD)−(p+tq)(r+tℓ).

若B≠0，t³项给v=0、继而u≠0；t²项给uB=−qℓ，故rankB=1。t项给D=I+(p/u)ℓ+(q/u)r，方向Jacobian经行列消元后为[[I,q],[ℓ,0]]，故

    det D_(y,ρ)Θ=−ℓq=u tr B≠0.

对rank-one B，有B²=(tr B)B，于是rankB²=1。旧B0、rankB=rankB²=1的affine充分构造均仍有效。因此整个smooth保clock/fullcoherence类的精确判别为

    B=0，或 rankB=rankB²=1.                            (5)

非零nilpotent rank-one B仍只有相应方向loss的标准lift，不能误升为(1,0)。

## 5. 真正nonlinear合法校准：不应声称π本身被迫affine

以下由B独立构造，root逐项展开核过。它们在空间Hessian非零时仍满足全部rank和coherence，直接否定“全coherence迫原π affine”的错误rigidity。

B=0时，取I避开−1，

    π_t(z)=(z₁+z₃²/(1+t),z₂),
    a=(w₁−ρ²,w₂,ρ),
    Θ=(y₁−ρ²,y₂,ρ).

沿线z₃=(1+t)ρ，平方项恰抵消z₁里的−(1+t)ρ²，输出w+ty；DΘ行列式1，π空间rank2。

B=diag(1,0)时，在小域取smooth k(y₁)满足k+k²=y₁、1+2k≠0，定义

    π_t(z)=(z₁+t z₃+z₃²,z₂),
    a=(w₁−ρ²,w₂,ρ),
    Θ=(y₁−ρ(1+2k),y₂,k).

输出第一坐标为w₁+ty₁+t²(k+k²)，第二坐标为w₂+ty₂。方向det=(1+2k)k′=1，πrank2。这些不是diag(1,2)的反例；它们校准(3)/(5)的真结论是**存在性可变分线性化**，而非本体空间线性。

## 6. 真实source、方法方向和适用边界

实际source为已存Nadjimzadah2609.06299v1 Def2.1/Prop2.2/Prop2.5。Def2.1允许smooth保t submersion，方向Θ独立w、全ρ一致；Prop2.2只从高维直线输入给曲线下界。2511.10918/GAFA00750-4是另一篇Bourgain-condition文章，不能混用。

(2)–(5)为自包含微分/线性代数，不使用未证Kakeya结论。完整全时coherence、原parameter-linear目标、Θw=0和fullw是必要责任；仅一个selector w(y)、换clock、少ρ或只配有限jets不在本结论。局部开放域restriction保rank，但曲线维数应用仍需source的全局/有界参数域量词。由本no-go不能逆向得高维Kakeya。

## 7. 排重、旧记录更正和停止

R49选取的是严格更大映射class，但(3)显示此目标上的存在性完全等价。按AGENTS的等价检查，本轮更新既有LIFT005/N5-CURVE-LIFT-01与旧稿范围，不新立nonlinear方向或数学ID，不把初等变分升级为重大中间结果。

旧R12三稿中“空间affine是实质限制/一般nonlinear未排”的判断需要更正：该限制对原π形状当然有区别，但对当前coherent parameter-linear lift存在性并非实质。历史证明保留、更正banner指向本稿；不能继续以这个已经消除的gap开Taylor/Hessian/normal-form轮。

本指定class已完整解决，停止其细节迭代。其它clock、selector、更一般非参数线性目标未排，但不得因此立即换成邻近class继续局部循环。R51先按既定周期做宏观审视，重新对齐一般/高维目标与最有价值的实际缺口。

## 8. 审查与目标状态

A和root独立核沿线变分，B另给真正affine variational realization并构造nonlinear可行校准；generals leading-minor由三方独立核。正式reviews须全文读main/macro/next及更正后的结果页才写。本轮无新有限实验，无新PDF；34PDF/37sources。文献主张、内部证明及高级具名输入层次仍分开，未经外部同行评审。

未解决普通高维Kakeya，未有新高维维数界、major或priority认证，Goalactive。root统一元数据/状态/路线/registry/round/验证及safe sync沿R49父59d261395f39a5d4302c9bb243c1829c64034c22。
