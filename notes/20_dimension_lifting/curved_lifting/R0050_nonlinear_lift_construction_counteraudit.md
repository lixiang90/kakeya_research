# R0050：全时第一变分、一般非线性lift障碍与真实非线性校准

2026-10-17，`lifting_obstructions`。目标为固定B=diag(1,2)的整个smooth空间非线性、原clock、full-parameter (1,0)-lift。结论：该类不可能；原因是完整参数第一变分产生一个真正的空间仿射lift，而不是原π本身必须仿射。此为旧LIFT005必要条件的正确scope扩展，不预称新颖/重大，不产生R5 Kakeya结论；需独立逐步审查，未经外部同行评审。

## 1. 原量词与一手输入

已运行context.py并读固定入口/registry78/latestR49、R50 working spec及next。实际读Nadjimzadah2609.06299v1 Def2.1、Prop2.2/2.5(i)及R12仿射分类三稿；2511.10918/GAFA00750-4是另一篇文章，不作为本定义的修订本。

设m=2、F(t)=tI₂+t²B。全部参数(y,w,ρ)在有内点的共同域，时间t在同一非退化含0区间I。假定smooth

\[
 \pi_t:\mathbb R^3\supset\Omega_t\to\mathbb R^2,
 \quad a=a(y,w,\rho),\quad \Theta=\Theta(y,\rho),
\]
\[
 \pi_t\big(a(y,w,\rho)+t\Theta(y,\rho)\big)=w+F(t)y.
 \tag{1}
\]

域须包含整段原lift直线；D_zπ_t rank2，D_(y,ρ)Θ rank3。Θ独立w，整个ρ域投回同一曲线；不是仅对一个selector w(y)或ρ(y)成立。下面不对π预加affine、polynomial或analytic假设。

## 2. 第一变分给另一个真实affine lift，而不拉直原坐标

更一般地令空间维数为m+s，目标仍为参数仿射族w+F(t)y。在一个固定原参数内点P取

\[
 z_P(t)=a(P)+t\Theta(P),\qquad
 T_P(t)=D_z\pi_t(z_P(t)).
\]

P不随t变化，所有a、Θ的参数导数均在这个同一P取值。对(1)在**固定t**关于参数微分，链式法则精确给

\[
 T_P(t)a_w=I_m,\quad
 T_P(t)(a_y+t\Theta_y)=F(t),\quad
 T_P(t)(a_\rho+t\Theta_\rho)=0.
 \tag{2}
\]

没有遗漏π_t的空间Hessian：参数的一阶导数只出现D_zπ_t；没有对t求导，所以也没有漏π_t的显式t项。T_P(t)沿同一条原线取值，可以是任意smooth时间矩阵。

引入新的自由增量参数u=(u_y,u_w,u_ρ)，定义

\[
 a^{\rm var}(u)=a_yu_y+a_wu_w+a_\rho u_\rho,
 \quad \Theta^{\rm var}(u_y,u_\rho)
       =\Theta_yu_y+\Theta_\rho u_\rho,
 \quad \pi_t^{\rm var}(z)=T_P(t)z.
 \tag{3}
\]

由(2)，对于全部新参数及**全部原t∈I**，

\[
 \pi_t^{\rm var}(a^{\rm var}+t\Theta^{\rm var})
       =u_w+F(t)u_y.
 \tag{4}
\]

这不是有限阶t-jet一致，而是(2)逐t给出的精确恒等式。(3)的轨迹本身是真直线；没有用非线性坐标变换把原线弯曲，也没有在每条线另选一个π。Ta_w=I保证T_P(t)对所有t均rank m。新Θ独立u_w，方向Jacobian正是原D_(y,ρ)Θ(P)，故方向rank/损失不变。可取小compact参数box和共同时间子区间，使新线段位于一个固定有界open域；投影在其邻域始终submersion。

因此，对这种**目标本来对w,y仿射**的族，一般smooth lift存在就推出同codimension、同方向rank的空间仿射/参数线性lift存在。反向显然，因为affine类是smooth类子类。此论证不对任意非线性X(w,t;y)声称同一等价，也不声称原π必须affine。

## 3. codimension-one的完整必要分类与固定B反证

为独立检查不只引用旧scope，在m=2,s=1直接消元。由Ta_w=I，a_w为固定rank2矩阵，延长为一个常数GL₃基变换，令

\[
 T(t)=[I_2,h(t)],\quad
 a_y=\binom C r,\quad\Theta_y=\binom D s,
 \quad a_\rho=\binom p u,\quad\Theta_\rho=\binom q v.
\]

其中C,D为2×2，r,s为行，p,q为列，u,v为标量，全部是同一P的常数。原全时(2)变为

\[
 F(t)=C+tD+h(t)(r+ts),\quad
 0=p+tq+h(t)(u+tv).
 \tag{5}
\]

u=v=0不可能，否则第二式给p=q=0，从而Θ_ρ=0，违反方向rank3。乘第一式以u+tv并消h，得

\[
 (u+tv)(tI_2+t^2B)
 =(u+tv)(C+tD)-(p+tq)(r+ts).
 \tag{6}
\]

全区间成立的矩阵多项式右端次数≤2，t³项给vB=0。B≠0时v=0，继而u≠0，t²项给

\[
 uB=-qs,\qquad\operatorname{rank}B\le1.
 \tag{7}
\]

diag(1,2)秩2，故一般smooth类的主候选不可能。不需除t、u+tv或假定某段h已解析。

若继续核方向rank，t项给D=I+(p/u)s+(q/u)r。对方向Jacobian作行列初等变换，

\[
 \det\begin{pmatrix}D&q\\s&0\end{pmatrix}
 =\det\begin{pmatrix}I&q\\s&0\end{pmatrix}
 =-sq=u\operatorname{tr}B.
 \tag{8}
\]

满秩迫trB≠0。非零rank1矩阵满足B²=(trB)B，故完整必要条件是rankB=rankB²=1。B=0以及这个rank1情形的旧affine充分构造仍是本一般smooth类的真构造。因此旧分类实际适用于整个此smooth类：B=0或rankB=rankB²=1。这个scope纠正不需要再开启Hessian/ansatz参数轮。

## 4. 两条真正非线性合法构造校准

以下都让D_zπ_t rank2、Θ独立w、D_(y,ρ)Θ rank3，并在全开参数及整个共同时间区间精确成立。它们严格否定“上述证明迫使原π空间affine”的过强说法。

**B=0。** 取I避开−1，

\[
 \pi_t(z)=\left(z_1+\frac{z_3^2}{1+t},z_2\right),
 \quad a=(w_1-\rho^2,w_2,\rho),
 \quad\Theta=(y_1-\rho^2,y_2,\rho).
 \tag{9}
\]

原线上z₃=(1+t)ρ，代入即w+ty；方向Jacobian行列式1。π的z₃ Hessian为2/(1+t)，并非affine。

**B=diag(1,0)。** 在y₁=0附近令k+k²=y₁，取k=(-1+√(1+4y₁))/2，故k′=1/(1+2k)。定义

\[
 \pi_t(z)=(z_1+t z_3+z_3^2,z_2),
 \quad a=(w_1-\rho^2,w_2,\rho),
 \quad\Theta=(y_1-\rho(1+2k(y_1)),y_2,k(y_1)).
 \tag{10}
\]

展开常数项为w₁、t项为y₁、t²项为k+k²=y₁，第二坐标为w₂+ty₂。

\[
 \det D_{(y_1,y_2,\rho)}\Theta
       =(1+2k)k'=1.
\]

π的空间Hessian非零，但完全合法。这也检查(8)不能误排traceB非零的rank1。

非零rank1 nilpotent的方向loss不能丢：若在(10)改k=k(y₂)，并把Θ第一项改成y₁−ρ(1+2k(y₂))，输出曲率为B y=(y₂,0)，但方向Jacobian只有rank2。它是允许方向损失的(1,1)校准，不是本(1,0)任务的反例。标量B=bI₂可换clock τ=t+bt²变成线族，也不在本原clock类中。

## 5. 同一variation的自然codimension下界

按主代理提出的同轮推论独立核：对m维F(t)=tI_m+t²B及任意codimension s，(2)只需Θ独立w，不需full方向rank。常GL将T写成[I_m,H(t)]，参数y导数写成(C;R)、(D;L)，得到

\[
 P(t):=t^2B+t(I-D)-C=H(t)(R+tL),
 \quad\operatorname{rank}P(t)\le s.
 \tag{11}
\]

若s<m，每个(s+1)minor是全区间为零的多项式；其最高次t^(2(s+1))系数为相应B-minor，故rankB≤s。s≥m时结论平凡。没有将H(t)假成多项式：多项式的是左端P(t)。因此任何这种一般smooth、保clock、Θ独立w的lift都须s≥rankB。

源Prop2.5(i)的rank factorization在s=rankB给真实lift，方向损失ν=s−rankB²。因此该codimension lower在允许源方向损失时可达。对本diag(1,2)，所有该类smooth lift均需s≥2，标准(2,0)构造达到；这只是本曲线族的lift复杂度，不是五维Kakeya维数界。不另开一般s研究轮或登记新ID。

## 6. 结论和停止边界

主任务已由全时第一变分回答：一般空间非线性π不能绕过diag(1,2)的codimension-one障碍。正确结论是“存在性可第一变分化为另一个affine lift”，并非“原π必affine”；(9)/(10)提供真非线性反校准。旧LIFT005应更正scope，由主代理统一registry/banner，不以本稿自审当独审。

这条必要机制用到了全部原coherence和Θ独立w。若只对selector、单个ρ、或换clock，(2)不再是本系统；不能反向用本no-go否定那些不同问题。Prop2.2的方向始终是高维linear输入到曲线结论；本例不能用这个class将R5输入降至R4，不逆向解决R5/general Kakeya。

不再继续quadraticπ/Hessian或有限jet阶数尝试；全class已经被精确variation覆盖。具体classification的已有性和意义仍需一手比对，不预宣新颖、重大或Goal完成。后续由macro选择不同真实缺口，Goal active。
