# R0008：任意二次chart的真实floor审计与有限horizon构造

日期：2026-10-17。任务：N5-HOR-01。已读working spec、STATE、原Definition2.8、Lemmas2.3、2.9–2.11及Definition2.14。核查目标是generic $j=3$ horizon上界本身，不重做R0007 WP4反例，不声称Kakeya反例或重大中间结果。

本文固定**同一概率prior、同一原始坐标、同一$B=1$**。模型的完整系数、profile与angular输入见并行稿 `R0008_smoothed_quadric_prior.md`；全部宽度的平滑/短块cap由本轮cap稿另证。下面说明这些输入如何接入原chart定义，及为何后期选择不能躲过估计。

## 1. 同一模型与本文使用的两个输入

可见先验$\nu_{\rm vis}$是R0007 quadric参数$\delta$-grid的均匀混合，完整六个affine coefficients $(b,u)$分别独立加$U[-\delta,\delta]$噪声。取

$$\delta=N_0^{-M},\quad 0<L<M/6,$$

隐藏变量为独立的$c=w_0$及极小$W$，$w(t)=c+tW$，native $P_*=w$、$B=1$。$c$为full-density有限Cantor近似，指数$0<d<1$；在所有准备尺度$a\ge a_L=N_0^{-L}$上，每个参与dyadic $c$-bin有质量$\asymp a^d$。选中事件仅为固定时间段

$$I_0=[1/2,3/4],\qquad d\mu=1_{I_0}(t)\,d\nu\,dt,$$

不把质量$1/4$重新归一化。隐藏变量与完整visible coefficients及内部grid-index均独立。

可取定量实例$L=1,M=12,d=1/2$、Cantor末层$\ell=N_0^{-40}$、$W\sim U[N_0^{-80},2N_0^{-80}]$，并沿dyadic尺度取整。

本文调用：

1. 固定$t\in I_0$，visible density $g_t(Y)\le C\delta^{-1}$，hidden $w(t)$的每个$a$-interval概率至多$Ca^d$；原始homogeneous characteristic density为

$$n(r)=\delta^{-1}a_r^d=N_0^{M-dr},\qquad f(r)=dr-M.\tag{HF1}$$

典型lower由observational support与积分质量证明，不能只从一个空洞的support维数命名；见profile稿。

2. 对任意时间块$I$、长度$q$，任意固定affine center及可逆空间矩阵$D$，若

$$\mathcal P_I=\{\text{visible affine traces}:\sup_{t\in I}|D^{-1}(Y(t)-y_c(t))|\le K\},$$

且$\|D\|\le qK$、$J=|\det D|$，则完整原始visible prior满足

$$\nu_{\rm vis}(\mathcal P_I)\le C K^C\delta^{-1/2}q^{-3}J.\tag{HF2}$$

这里不限制轴宽相对于$\delta$的大小，矩阵和center只固定于当前chart；不得把右侧的$\nu_{\rm vis}$替换成免费条件化的$\nu_{\rm vis}(\cdot\mid A)$。

## 2. 原chart定义的精确对接

Definition2.8要求每个完整assignment $A$上的**整段**可见空间拟合与小值成立；其当前selected incidence可再是其中一个小子集。其测试是total degree不超过2的$P(t,Y,w)$，并在选中点有

$$|P|\le Ka,\qquad |P_w|\ge1/K,$$

同时原定义还有whole-block $|P_w|\le K$、曲率界$|P_{ww}|\le K/a$。下节上界甚至不需要后两个额外条件。原模型$B=1$已固定；不能在某个竞争chart中另选极小$B$而仍宣称是同一exact problem。

时间partition共同长度$q=N_0^{-h+o(1)}$；每块assignments互不相交且总selected mass为inverse-subpower。这些条件在原系统定义中必须保留，但我们的**逐chart上界**不依赖全层label数或覆盖率，因此会适用于任意满足定义的竞争系统。

## 3. 任意二次测试的质量上界

固定一个chart，记其完整assignment为$A$、selected mass为$m_A$。对每个$t\in I\cap I_0$、完整visible trace $l_{\rm vis}$，把$Y(t)$固定，视$P(t,Y(t),w)$为一元二次多项式。源Lemma2.9给

$$\{w:|P(t,Y(t),w)|\le Ka,\ |P_w|\ge1/K\}$$

至多有固定个区间，总长度不超过$4K^2a$；等价地至多遇到$CK^2$个宽$a$的bins。因此原hidden law的概率至多

$$CK^2a^d.\tag{HF3}$$

若直接使用全尺度Frostman upper可把这个$K$依赖改善为固定幂$K^{2d}$，本文不需要该改善。系数多大、是否含$w^2$、根分支如何改变均不影响此估计。

所有assigned visible traces都在$\mathcal P_I$。即使assignment或selected event把hidden变量与visible变量作任意复杂耦合，仍可把事件扩大到$\mathcal P_I$乘以上述一元可用集合，并在**原独立product prior**上积分。因而

$$\boxed{\frac{m_A}{q}\le CK^C a^d\nu_{\rm vis}(\mathcal P_I).}\tag{HF4}$$

这里用$|I\cap I_0|\le q$，没有将selection后的hidden conditional law误认为原Cantor律，也没有给每个label重新归一化。

## 4. 真实floor迫使正的绝对horizon成本

若该chart真实，原floor是

$$m_A/q\ge K^{-1}n(r)J
=K^{-1}\delta^{-1}a^dJ.$$

由(HF2)、(HF4)，同时有

$$m_A/q\le CK^C a^d\delta^{-1/2}q^{-3}J.$$

约去严格正的$a^dJ$，即得

$$\boxed{q^3\le CK^C\delta^{1/2}.}\tag{HF5}$$

所以任何非空真实chart均满足$h\ge M/6$；任何有足够覆盖的真实终端系统当然也满足。由原Definition2.14的infimum量词，

$$\boxed{H(E)\ge M/6>L.}\tag{HF6}$$

**进一步选择。** 若$\mu'$是原incidence law的inverse-subpower restriction，始终有$\mu'\le\nu dt$，所以(HF4)逐点不变。原Lemma2.3说明typical logarithmic density在这种选择下保留，故(HF1)至多改subpower因素；这些因素进入$K$，不能改变(HF5)的固定幂。若分析性prepared law仅受$G\nu dt$控制，$G$为subpower，同样把$G$乘入损失即可。任意exact subsequence也保留该固定幂估计。

在新坐标/new prior中构造的候选若要成为$H(E)$的竞争者，必须把时间、空间、test derivative unit和mass floor返回本原problem。仅在新problem中改$B$、除以小assignment质量或换用新density，并不提供原$H(E)$的反例。

此推导以(HF1)–(HF2)为输入；它没有调用被质疑的generic Proposition2.16，也没有先假定原始source full-slope density。完整model是否另满足某个$\mathcal C(d)$ angular条件由profile稿单独核验，不能由本floor计算命名。

## 5. $q=\delta$的直接终端真实atlas

以下不借用generic completion。用$\delta$长的全局dyadic time partition，只在完全位于$I_0$的blocks上使用charts，令$t_I$为midpoint。

### 5.1 有限good cells保留常量原始质量

六系数$\delta$平滑后的$Y(t_I)$支撑位于$ty+xz=1$的$C\delta$邻域。因$t_I\in[1/2,3/4]$，可写$y=(1-xz)/t_I$，固定有界图每个$(x,z)$的$\delta$-square只遇到$O(1)$个$y$-cells。因此占据的三维$\delta$-cubes数至多$C\delta^{-2}$。这里使用具体Lipschitz图，不能只从support体积$O(\delta)$推出cell数。

由$g_{t_I}\le C\delta^{-1}$，每个这样的cube概率至多$C\delta^2$。删除概率低于$\tau\delta^2$的cubes，损失至多$C\tau$。取小固定$\tau>0$，保留visible prior质量至少$3/4$，且每个good cube $Q$满足

$$\tau\delta^2\le\nu_{\rm vis}\{Y(t_I)\in Q\}\le C\delta^2.\tag{HF7}$$

不对good cells重新归一化；每块都使用同一原prior。

### 5.2 完整assignments、test与真实floor

对每个good $Q$和每个参与的hidden $c$-bin $C_a$，取完整assignment

$$A_{I,Q,C_a}=\{Y(t_I)\in Q,\ c\in C_a\},$$

不切割$W$或内部index。该块内这些assignments互不相交。独立性及Cantor aligned-bin lower给

$$\nu(A_{I,Q,C_a})\asymp_{\tau}\delta^2a^d.$$

取固定center为$Q$中心，空间矩阵$D=C_R\delta I_3$，故$J\asymp\delta^3$且$\|D\|\le qK$。有界速度保证整个$I$上的空间拟合；hidden test为

$$P_{I,Q,C_a}=w-c_{C_a}.$$

因$|c-c_{C_a}|\le a/2$、$\sup|tW|\ll a_L\le a$，whole-block $|P|\le Ca$，$P_w=1$、$P_{ww}=0$。选中assignment在完整$I$的全部incidences，则

$$m_A/q=\nu(A)\gtrsim_{\tau}\delta^2a^d
\asymp n(r)J.$$

所以这些是原定义下的真实charts。总selected mass至少固定倍$|I_0|$，不是以small-cell质量归一化产生的覆盖。

### 5.3 原始own-depth/terminal列表及有限性

当前exact $t,Y(t)$确定block，且$|Y(t_I)-Y(t)|\le C_R\delta$，所以midpoint cube $Q$最多有$O_R(1)$个候选。当前hidden $a$-bin给$c=w(t)-tW$到$O(a)$精度，所以$C_a$也只有$O(1)$选项；finer terminal bin同样足够。输出label不包含不可观察的内部grid index。

blocks有$O(\delta^{-1})$个，每块good cells $O(\delta^{-2})$，$c$-bins为多项式多个。Assignment谓词在完整系数空间中是线性bin测试，tests总次数1，矩阵倒尺度$\delta^{-1}$是固定原始幂。Good cells的测度筛选只是定位一个有限box family，最终用这些box常数编码，符合Definition2.2的有限性约定。

因此在原终端$a_L$直接有$q=\delta=N_0^{-M}$的真实系统，

$$\boxed{M/6\le H(E)\le M.}\tag{HF8}$$

若以后只保留inverse-subpower质量$\alpha$的incidence，可先令$\tau$为远小于$\alpha$的subpower，再按$\theta q\nu(A)$删掉当前轻entries，$\theta\ll\alpha$亦为subpower；原assignment预算使损失至多$\theta$。剩余完整assignments不变，floor只付$(\tau\theta)^{-1}$，不需要换prior。这给同类型prepared restrictions的有限horizon构造，但原模型(HF8)本身已由常量覆盖建立。

## 6. 已攻击的量词与结论范围

- **不是指定test反例：** (HF3)对所有二次$P$统一成立，包括$w^2$、mixed terms及大系数；原上导数与曲率条件只进一步缩小可用族。
- **不是只看选中空间点：** (HF2)施于原Definition2.8要求的完整assigned trace whole-block空间测试，然后外推；若只给某时刻空间条件，不能使用它。
- **不是后验乘积假设：** 独立性仅在原prior使用，任何当前assignment/selection都先扩大事件后积分；没有声明条件于chart后仍独立。
- **没有以$d<1$推horizon：** lower由任意test质量上界和真实floor相除得到，upper由显式$q=\delta$系统得到。
- **不具原始Kakeya来源：** 模型并不保留初始全部方向的subpower full-slope density；此项资格与generic exact问题是不同命题。

当本轮并行输入(HF1)–(HF2)完成核验时，(HF6)严格否定的是原$j=2$ universal $H\le L$结论在这种无额外来源的$j=3$类中的直接移植；不反驳原四维论文，也不否定五维Kakeya。完成此主轮后应宏观转向能排除该明确模型的新来源条件，而非无限细化其真实horizon值。
