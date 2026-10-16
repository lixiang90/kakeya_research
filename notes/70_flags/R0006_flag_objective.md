# R0006：三维flag目标、外积夹逼与实际短法向对齐

日期：2026-10-16。互补任务：N5-FLAG-01。开轮已从GOAL、STATE、R0006宏观审视恢复；本轮只读取已归档原稿，不下载文献。本笔记给出自包含的条件定理和反例，不声称新颖性或Kakeya维数改进。

接近长期目标的问题：三维可见空间中，两个法向约束通常留下一个长方向。若能把这一长两短几何转成原始观测可知、质量可付的atlas，需要一个能沿真正路径比较的flag目标；逐轴宽度不精确可加，不能照搬二维最短轴叙述。

## 1. 原稿实际保证什么

已核对原稿Definition2.8、Lemma2.13、(2.16)–(2.17)、§4.1–4.3及Proposition10.2。原稿是$j=2$；时间与空间矩阵按

$$q_{cd}=q_cq_d,\quad D_{cd}=D_cD_d,\quad J_{cd}=J_cJ_d$$

提升，因此二维$\log(q^2/J)$精确可加，与轴是否平行无关。largest-axis fullness另经角度/路径准备得到，才把该标量解释成最短轴的额外窄度。三维只直接继承$\log(q^3/J)$的精确可加性；没有从这里得到逐轴可加。

Proposition10.2的原始$p_L$列表证明还使用：若二维两法向不同，两个velocity strips交于小球，因此joint angular ball cap可排除该情况。三维交集一般仍是一条长方向；该排除步骤不能仅改$j$。下面的外积论证不补齐此处的标签/质量输入。

## 2. 可选的两个标量及基本不等式

对归一化形状矩阵$A=D/q\in GL_3(\mathbb R)$，在固定底数$N>1$中定义

$$v(A)=-\log_N|\det A|,\qquad
b(A)=-\log_N\|\wedge^2A\|.$$

一律使用欧氏operator norm。若奇异值为$\sigma_1\ge\sigma_2\ge\sigma_3>0$，则

$$\|\wedge^2A\|=\sigma_1\sigma_2,\quad
v(A)=-\log_N(\sigma_1\sigma_2\sigma_3).$$

所以

$$\boxed{v(AB)=v(A)+v(B),\qquad b(AB)\ge b(A)+b(B).}\tag{F6.1}$$

第二式由$\wedge^2(AB)=(\wedge^2A)(\wedge^2B)$与范数次乘性直接得到。它是**超可加**，不是精确可加。无需引用完整Horn理论；本文使用的全部谱乘积信息都由外积范数及行列式证明。

若最大轴full，$\sigma_1=N^{o(1)}$且$\sigma_1\ge N^{-o(1)}$，则$b(A)=-\log_N\sigma_2+o(1)$，它检测第二根轴变短；$v-b=-\log_N\sigma_3$检测第三根轴。没有最大轴fullness时，$b$是两根最大奇异值的乘积成本，不能叫作“第二轴窄度”。

对于$\|A\|\le K=N^{o(1)}$，$b(A)\ge-o(1)$。由奇异值排序总有$b(A)\le2v(A)/3$；有最大轴fullness时可加强为$b(A)\le v(A)/2+o(1)$。因此有限体积窄度能限制该flag成本，但不能决定其值。

## 3. 有限网格夹逼定理：超可加已足够

**定理FLAG-OBJ-01。** 给定固定有限网格$0=r_0<r_1<\cdots<r_m=1$。令第$i$段相对归一化形状为$A_i$，累计矩阵为$P_i=A_1\cdots A_i$。假设某个有限$\ell\ge0$满足

$$b(A_i)\ge\ell(r_i-r_{i-1})-\epsilon_i,\quad
b(P_m)\le\ell+\epsilon_0,\qquad \epsilon_i\ge0.$$

设$E=\epsilon_0+\sum_{i=1}^m\epsilon_i$。则每个累计节点满足

$$\ell r_k-\sum_{i\le k}\epsilon_i
\le b(P_k)
\le\ell r_k+\epsilon_0+\sum_{i>k}\epsilon_i.\tag{F6.2}$$

更一般地，对任意连续段$A_{a+1}\cdots A_b$，其$b$值与$\ell(r_b-r_a)$的差的绝对值至多$E$。全部非可加缺陷的总和满足

$$0\le b(P_m)-\sum_i b(A_i)\le E.\tag{F6.3}$$

因而每次累计拼接的缺陷

$$\delta_i=b(P_i)-b(P_{i-1})-b(A_i)\quad(i\ge2)$$

均在$[0,E]$内。任意相邻两个连续块的拼接缺陷也至多$E$。

**证明。** 前缀下界由(F6.1)反复应用。对后缀同样应用(F6.1)，有$b(P_m)\ge b(P_k)+\sum_{i>k}b(A_i)$，移项即得前缀上界。任意连续段可用其外侧的段下界及终端上界夹住。总缺陷非负，且由段下界求和与终端上界至多$E$。累计缺陷望远镜求和恰为总缺陷，每项非负，因此各项也至多$E$。对连续块先作一次分组即可。

此定理说明原稿finite-grid narrowness校准中“精确可加”可以放宽为这个方向的超可加。若实际slacks随$N$为subpower，应把$O(\log K/\log N)$逐项加入$\epsilon_i$；网格扩大时仍需慢对角控制总误差$E$，不能无限重复乘损失。

### 3.1 何时它才是合法的Kakeya极值目标

可把$b$作为horizon极值之后的候选宽度目标，仿照原稿定义“某maximizing sequence上可达到的terminal limsup之sup”，再对序列取inf。但(F6.2)只证明**已取得两侧输入之后**的夹逼，未证明实际$j=3$类有这些输入。必须逐项另证：

1. 空间/时间归一化仍在所需exact/cap类内，且remaining/coarsened sequences仍horizon maximizing；
2. 真child可以经真实parent或合适known atlas提升，terminal floor按同一prior与world/time权重恢复；
3. 同一有限网格可选择近最优段，记录full assignments及frozen witnesses，保留所需原始$p_L$列表与inverse-subpower覆盖；
4. 输出是终端优化真正允许的竞争者，故有terminal $b$上界；另准备最大轴fullness，才把$b$识别成第二短轴成本。

若在既有determinant极值之外再作第二次$b$优化，$\omega_2$只能在**同一批**horizon近$k$、terminal determinant近$\ell_{\det}$的systems中取可达sup，再对det-minimizing sequences取inf。每段必须同时满足$\delta_{\det}\ge\ell_{\det}\Delta r-\zeta$及$b\ge\mu\Delta r-\zeta$，不能分别用两批不相容systems实现这两个下界。

一种可能的证明顺序是先用global terminal determinant上界及逐段determinant下界，证明每个remaining/coarsened sequence仍det-minimizing，再在该受限类内作同步secondary选择。但新增受限类的闭合和同步选择尚未建立；不能只因两个矩阵标量都存在就默认lexicographic优化合法。**本文登记的是条件sandwich定理，没有推出真实$j=3$flag critical path。**

## 4. 外积近等号控制实际复合frame的短法向

**定理FLAG-ALIGN-01。** 对$A,B\in GL_3(\mathbb R)$，设$A$的谱隙比

$$r_A=\sigma_3(A)/\sigma_2(A)<1,$$

令$n_A$为其最短轴的左单位法向。若

$$\|\wedge^2(AB)\|\ge\rho\|\wedge^2A\|\|\wedge^2B\|,
\qquad0<\rho\le1,$$

则$AB$的任意top左外积奇异向量经Hodge对应的实际最短轴法向$n_{AB}$满足

$$\boxed{|\sin\angle(n_{AB},n_A)|\le\min\{1,r_A/\rho\}.}\tag{F6.4}$$

这里法向取无向角；无需$B$有谱隙。

**证明。** 写$M=\wedge^2A$、$L=\wedge^2B$。$M$的top左奇异向量$u_A$唯一，对应$n_A$；其余两个奇异值之最大为$\sigma_1(A)\sigma_3(A)$。若$\Pi_\perp$是垂直$u_A$的投影，则

$$\|\Pi_\perp M\|=r_A\|M\|.$$

取$ML$的任意top右单位奇异向量$z$，则$u=MLz/\|ML\|$是其top左奇异向量，且

$$\|\Pi_\perp u\|\le\frac{r_A\|M\|\|L\|}{\|ML\|}\le r_A/\rho.$$

Hodge星算子在$\wedge^2\mathbb R^3$与$\mathbb R^3$间为等距映射，把top左二维奇异plane转成最短左轴法向，故得(F6.4)。若复合top奇异值重根，此界仍对其每个top左向量成立；足够小的$r_A/\rho$还会排除这种重根。

应用(F6.3)，有$\rho=N^{-\delta}$。若父谱隙$r_A\le N^{-\gamma}$且拼接缺陷$\delta\le E<\gamma$，则

$$|\sin\angle(n_{AB},n_A)|\le N^{-(\gamma-E)}.\tag{F6.5}$$

这给出实际原坐标中的法向对齐，超过仅称“外积近极值”。若缺陷只为$o(1)$、谱隙为固定正幂，便得到固定幂对齐；若谱隙本身只有subpower，不能得到这个结论。

不能把$A^{-T}$作用于$B$的top二维plane法向直接称作$AB$的实际短奇异法向：它描述的是该选定plane的像，未必是复合矩阵的主plane。上面的投影证明避免了这个未经证明的识别。

### 4.1 一般外积版本

同一证明适用于$A,B\in GL_j(\mathbb R)$及$1\le k<j$。$\wedge^kA$的最大奇异值为$\sigma_1\cdots\sigma_k$，次大者与它的比为

$$r_k(A)=\sigma_{k+1}(A)/\sigma_k(A).$$

若$r_k(A)<1$且$\|\wedge^k(AB)\|\ge\rho\|\wedge^kA\|\|\wedge^kB\|$，则实际top-$k$左奇异plane的Plücker线满足

$$\sin\angle_{\mathrm{Pl}}(E_k(AB),E_k(A))\le r_k(A)/\rho.$$

并且最大principal angle也有相同上界：两个单位decomposable外积的内积绝对值为$\prod_{i=1}^k\cos\theta_i$，故

$$\sin^2\theta_{\max}\le1-\prod_i\cos^2\theta_i
=\sin^2\angle_{\mathrm{Pl}}.$$

这只使用外积的谱与正交投影；没有把多重top奇异空间中任意非decomposable向量称作一个plane。选取实际top-$k$奇异plane的外积向量即可。

### 4.2 条件性的三维flag分类

若**另外已建立**同一真实路径上$\sigma_1=N^{o(1)}$且$\sigma_1\ge N^{-o(1)}$、体积节点成本$v=\ell_{\det}r+o(1)$及外积节点成本$b=\mu r+o(1)$，那么三根轴的幂指数为

$$0,\quad \mu r,\quad(\ell_{\det}-\mu)r,$$

排序强制$0\le\mu\le\ell_{\det}/2$。再有相应拼接范数比为$N^{-o(1)}$时，前述外积lemma给出：

| 参数区间 | 有固定幂谱隙的flag | 实际可稳定的对象 |
|---|---|---|
| $\mu=0<\ell_{\det}$ | 第二轴与第三轴分离 | 两长一短的短法向；两根长轴各自可旋转 |
| $0<\mu<\ell_{\det}/2$ | 第一/第二、第二/第三均分离 | 长轴线与短法向同时稳定，形成完整flag |
| $0<\mu=\ell_{\det}/2$ | 第一轴与短二维plane分离 | 长轴线稳定；短plane内部不保证唯一或具有固定幂稳定性的短法向 |
| $\ell_{\det}=0$ | 无固定幂谱隙 | 仅幂尺度各向同性，不给稳定flag |

对$k=1$，所需near-product范数比由父、相对child及累计frame的最大轴fullness给出；对$k=2$，由同一外积objective的校准缺陷给出。仅有节点指数而没有拼接控制时不能跳过这个条件。此表是条件线性代数分类，不是已经建立的$j=3$临界路径分类。

## 5. 两个全时strip的实际几何与质量条件

**定理FLAG-INT-01（条件性全时交框）。** 设同一完整trajectory assignment在单位时间内满足

$$|n\cdot y(t)-\ell_1(t)|\le a,\quad
|m\cdot y(t)-\ell_2(t)|\le b,$$

其中$n,m$为固定单位法向，$\ell_1,\ell_2$为固定仿射函数，$a,b>0$，$|y(t)|\le R$，$\tau=|n\times m|>0$。则可取一个固定affine center及全时空间frame，最大轴为$O(R+1)$，第二轴至多$C_R\max(a,b)/\tau$，空间Jacobian至多$C_Rab/\tau$。

证明：令$e_0=(n\times m)/\tau$，并在$\operatorname{span}(n,m)$中取对偶向量$u,v$，满足$n\cdot u=1,m\cdot u=0,n\cdot v=0,m\cdot v=1$。其范数均为$1/\tau$。取center $\ell_1(t)u+\ell_2(t)v$，空间列可取$(C_Re_0,au,bv)$，其行列式绝对值为$C_Rab/\tau$。在$\max(a,b)/\tau$小的目标区间，这已给所需frame。

为使任意宽度下的**最大轴**也有统一上界，可作bounded clipping：非空assignment中固定一条eligible affine轨道$y_*(t)$为center。对其余轨道，$z=y-y_*$满足$|z|\le2R$、$|n\cdot z|\le2a$、$|m\cdot z|\le2b$。令$M$的两行为$n^T/a,m^T/b$，其在$e_0^\perp$上的奇异值为$\lambda_1\ge\lambda_2>0$，右奇异轴为$e_1,e_2$。则$|z\cdot e_i|\le2\sqrt2/\lambda_i$。取长列$2(R+1)e_0$、两短列

$$\min\{2(R+1),2\sqrt2/\lambda_i\}\,e_i\quad(i=1,2).$$

它们给出包含全assignment的正交frame，最大轴至多$2(R+1)$。由于$M^+$在normal plane上的两列为$au,bv$，

$$\lambda_2^{-1}\le\sqrt{a^2+b^2}/\tau,\qquad
\lambda_1\lambda_2=\tau/(ab),$$

第二轴至多$4\max(a,b)/\tau$，Jacobian至多$C_Rab/\tau$。代表轨道按每个非空label固定选择，不随当前point改变。

若$\max(a,b)/\tau$为固定幂小量，该框是一长两短，且

$$b(D_{\rm new})\ge\log_N\frac{\tau}{\max(a,b)}-O(\log C_R/\log N).$$

若两个输入label都由**同一个原始观测**以$L_1,L_2$项列表恢复，且输出数据是这对label的确定函数，则新框label在该观测下最多有$L_1L_2$个选项。这个同观测的pair knowledge是假设；在两个不同时刻分别知道一个label不够。

若进一步两个框是**同一world/先验、同一深度、同一时间块**的真实框，共同块长为$q$，则原始true floor应写为$m_1/q\ge nJ_1/K$。若交框分支保留$m_{\rm new}\ge f m_1$（$0<f\le1$），一般充分损失是$\max\{1,KJ_{\rm new}/(fJ_1)\}$，使$m_{\rm new}/q\ge nJ_{\rm new}/K_{\rm new}$。在**同一归一化空间坐标**中，若第一框两根长轴与1可比，因而$J_1\asymp a$，本引理给新true-floor只需支付

$$K_{\rm new}=\max\left\{1,C_RK\frac{b}{\tau f}\right\}$$

作为充分的floor损失。这里使用**同坐标**的$J_{\rm new}/J_1\le C_Rb/\tau$，并把$J_1\asymp a$的比较常数一并计入$C_R$；共同$q$精确取消。当右侧比1还小时，可取$K_{\rm new}=1$，不能写出小于1的“subpower损失上界”。未经上述空间归一化，短时间raw框一般还有两根长轴宽度因子，应保留实际$J_{\rm new}/J_1$，不能直接代入$b/\tau$。

因此$f$为inverse-subpower、$b/\tau$为固定幂小时，缩框不会造成floor亏损。覆盖、branch disjointness及共同原始列表仍必须保留。这个floor推论不能把短时间真$Q$的$n(r)$ floor直接搬给depth-zero全时框的$n(0)$；原稿§10.2恰有全时known框未立即饱和的问题，需另行平衡。

## 6. 严格反例与不得漏掉的条件

**轴向不加。** 令$\varepsilon=N^{-a}$，$A=\operatorname{diag}(1,1,\varepsilon)$。若$B=A$，复合为$(1,1,\varepsilon^2)$；若$B=\operatorname{diag}(1,\varepsilon,1)$，复合为$(1,\varepsilon,\varepsilon)$。输入体积成本都为$a+a$，输出最大轴都full；前一第二轴成本0，后一为$a$。所以总det相同不能判定flag。

**相对plane的常角不等于实际复合normal不同。** 若$B=RAR^T$，其中$R$绕长轴旋转$45^\circ$，则$\|\wedge^2(AB)\|\asymp1$，故$b$拼接缺陷只有$O(1/\log N)$，但中间坐标的两top planes可成常角。这不反驳(F6.4)：实际$AB$短法向仍在$O(\varepsilon)$内对齐$A$的短法向。不能把相对坐标法向与实际法向混用。

**线性独立没有定量增益。** 取$n=e_3$、$m=(e_3+\varepsilon e_2)/\sqrt{1+\varepsilon^2}$、$a=b=\varepsilon$。两个法向始终独立，但$\tau\asymp\varepsilon$。strip交集仍允许两个常数长方向，只在$e_3$方向为$O(\varepsilon)$；新$b$成本仍为0。必须有$\max(a,b)\ll\tau$，不能只检查秩2。

**全局列表不能由两时刻自动相乘。** 两个时刻各自有$K$项列表，只给这两个观测的联合信息$K^2$列表；当前$p_L(t)$并未包含另一时刻exact base。原稿二维先排除横向法向再从邻近normal/center恢复anchor label；三维若保留两个独立法向，须另证同观测pair恢复，或支付实际大列表及其质量成本。

## 7. 本轮验收与待审输入

本轮新增的可检查工具为：超可加外积objective的finite-grid sandwich、谱隙下实际复合短法向对齐，以及显式带角度/质量/同观测列表条件的交框引理。它们不是完整$j=3$极值归约，更不是高维Kakeya结构定理。

下一步只值得核查两类具体输入：(i)真实candidate atlas是否保留同一原始观测pair knowledge与足够质量，使其成为terminal优化的合法竞争者；(ii)合法极值路径是否提供上述terminal $b$上界、段下界和谱隙。若只是再次写出两个strip留直线，或把relative normals当actual normals，本版本应停止。

主体独立审查见research/reviews/R0006_exterior_flag_review.md；其中审查人撰写的bounded clipping补证另由root复核，见R0006_root_review.md。本文自身证明不计作独立复核。
