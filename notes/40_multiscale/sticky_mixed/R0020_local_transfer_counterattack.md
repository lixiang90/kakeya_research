# R0020：满方向真实管族的局部投影凸集中反例

2026-10-17。任务 N5-MIXED42-Q01 的互补反例攻击。已读 AGENTS、GOAL、STATE、ROADMAP、registry、本轮 spec 与 R19 handoff。只检验局部 transfer；长期 Kakeya Goal 未解决。

## 1. 被否定的精确推断与适用边界

下面构造有限普通直管族，保留同一原管权重及其原 shading，并同时满足：

- 环境五维管有满量级四维分离方向、常数界四维 joint AD 和常数界 whole-tube 凸 Wolff；
- 一个真实尺度 $\rho$ 空间—时间 cube 的自然相交管族，固定比例的原子族有共同的 $\asymp\rho/\delta$ 个原时间 marks；
- isotropic cube 归一化后，工作半径 $s=\delta/\rho$，这些原 marks 的 projected shading 密度 $\lambda\asymp1$；
- 每个固定 hidden 值、固定共同时间的水平三变量填满常数密度 patch；
- 指定三维直线投影保留原像权重，合并相近 projected indices 后仍有明确的 uniform representatives。

然而该 projected family 的 normalized convex Frostman 常数

\[
                  D\asymp\rho^{-1},\qquad
                  \lambda/D\asymp\rho.                      \tag{1.1}
\]

这否定“由环境 AD/CW、局部三 grain 密度和局部长 marks 自动得到小 projected CF”的推断。它不是实际源配置的反例：局部薄集是一个短区间，不能满足所需固定正 $\kappa$ 的跨尺度 $(1-\kappa)$-AD；点方向也没有宏观的 $\kappa$-AD fibre。第8节量化这两个缺项。

与只写条件化 $p^{-1}$ 不同，本稿算出有限真管例子的实际最佳 $D$、$\lambda$、union 和原质量，并且保留环境满方向。它不重复 R19 的残余 Möbius/Cantor-transport 模型。

## 2. 有限环境管族：满方向、joint AD 与常数凸 Wolff

取固定小的二进数 $r_0=2^{-10}$。令 $\delta=2^{-n}$，参数

\[
 a,b\in[r_0,2r_0)\cap\delta\mathbb Z,\qquad
 c,d\in[0,r_0)\cap\delta\mathbb Z.
\]

定义轴线

\[
 \ell_{a,b,c,d}(t)
       =(d+ta,\ tb,\ (1+t)c,\ td,\ t)\in\mathbb R^5.          \tag{2.1}
\]

取每条轴线以 $t=0$ 点为中心的物理单位线段的 $\delta$ 邻域，记 $T_{a,b,c,d}$。斜率很小，所以所有这些线段均包含 $|t|\le1/3$ 的共同轴段。全族 $\mathcal T$ 使用均匀原权，数量

\[
                      N=(r_0/\delta)^4\asymp\delta^{-4}.       \tag{2.2}
\]

图方向为 $(a,b,c,d)$，所以方向是 $\asymp\delta$-分离且占满一个固定四维方向盒；归一为单位方向仅改变固定常数。

实际截距和斜率分别是

\[
 (d,0,c,0),\qquad(a,b,c,d).                                  \tag{2.3}
\]

从 joint 参数直接读回 $(a,b,c,d)$，正向和逆向都为常数界 Lipschitz。因此在通常管参数度量下，$\mathcal T$ 是常数界四维 AD；不是把方向计数冒充 joint AD。

**环境 whole-tube CW 的直接证明。** 固定 $t_*=1/4$。同一时刻的空间位置由线性映射

\[
 L_{t_*}(a,b,c,d)=(d+t_*a,\ t_*b,\ (1+t_*)c,\ t_*d),
 \qquad \det L_t=t^3(1+t)                                   \tag{2.4}
\]

给出。$L_{t_*}$ 为固定双 Lipschitz 映射。设凸集 $U$ 含某些完整原管。其 $t=t_*$ 截面含这些轴点周围的四维 $\delta$ 球；球的重叠有固定上界。故

\[
 \#\mathcal T[U]\,\delta^4
       \lesssim \operatorname{Vol}_4(U\cap\{t=t_*\}).         \tag{2.5}
\]

若至少含一条管，$U$ 也含该管在 $t=-t_*$ 的轴点。以它为顶点、以上述凸截面为底的五维锥包含在 $U$，所以

\[
 \operatorname{Vol}_5(U)
       \ge(2t_*/5)\operatorname{Vol}_4(U\cap\{t=t_*\}).        \tag{2.6}
\]

由 (2.2)、(2.5)、(2.6) 得

\[
              \#\mathcal T[U]/N\lesssim\operatorname{Vol}_5(U).
                                                                    \tag{2.7}
\]

这证明任意凸集上的常数界 normalized CW。没有调用方向分离的隐含外部结论，也没有只控制 marked pieces。

## 3. 真局部 cube、自然管质量和同一原 marks

取 $\rho=2^{-m}$，要求 $n>2m+20$，令

\[
 s=\delta/\rho\ll\rho,\qquad q_\rho=[0,\rho]^5.
\]

保留原族中

\[
 \mathcal S_\rho:
        c,d\in[r_0\rho,2r_0\rho)\cap\delta\mathbb Z,           \tag{3.1}
\]

而 $a,b$ 范围不变。端点均二进对齐，故原质量恰为

\[
                    \nu(\mathcal S_\rho)=\rho^2.              \tag{3.2}
\]

对所有这些管，全部共同时间

\[
 Z_\rho=[\rho/4,\rho/2]\cap\delta\mathbb Z                    \tag{3.3}
\]

的轴点都在 $q_\rho$ 内部。特别，最薄的第四坐标也距边界 $\gtrsim r_0\rho^2\gg\delta$，所以可保留半径 $c\delta$ 的真实标记球。每条保留管有 $\asymp\rho/\delta$ 个这样的原 marks。

这些不是任意稀有标签选出的“局部”子族。若一个原管在 $q_\rho$ 相交，取交点的 $0\le t\le\rho$：由 $(1+t)c\lesssim\rho$ 及 $d+ta\lesssim\rho$ 可知 $c,d\lesssim\rho$（管半径只改常数）。故整个自然相交族的质量也是 $O(\rho^2)$，而 (3.1) 已给其固定比例大小的内部 packet。

环境原 shading 可以先取每条管整管。这里的 marks 是其中合法的真实子集。相对原完整单位管，局部 shading 密度为 $\asymp\rho$；下节的常数密度来自显式缩短时钟，不能在原完整时钟上免费声称常数密度。

## 4. Isotropic q 归一化后的真实三 grain 与 projection

作单一固定 affine 缩放

\[
 (x_1,x_2,x_3,x_4,t)\longmapsto
      (X_1,X_2,X_3,W,\tau)=(x_1,x_2,x_3,x_4,t)/\rho.
\]

写 $\alpha=c/\rho,\ \beta=d/\rho$。归一化轴是

\[
 (X_1,X_2,X_3,W,\tau)
   =(\beta+\tau a,\ \tau b,\ (1+\rho\tau)\alpha,
                         \rho\tau\beta,\ \tau).             \tag{4.1}
\]

这仍然是普通直线。原管半径变为 $s=\delta/\rho$，原共同 marks 的时间间距也为 $s$，时钟区间为 $[1/4,1/2]$。

在每个 $\tau\in[1/4,1/2]$、每个固定 $\beta$ 上，变量 $(a,b,\alpha)$ 给 $(X_1,X_2,X_3)$ 一个三维矩形 patch，其三轴宽度均有与 $\rho,\delta$ 无关的正下界。细网的 $s$-cover 同样有 $\asymp s^{-3}$ 个水平 cells。所以局部三维水平 grain 并未缺失。相应 hidden 集为

\[
        Y_\tau=\rho\tau\,[r_0,2r_0],                        \tag{4.2}
\]

在 $s$ 分辨率下是长度 $\asymp\rho$ 的 interval。

取固定坐标投影

\[
                   \pi(X_1,X_2,X_3,W,\tau)=(X_3,W,\tau).
\]

得到实际投影轴

\[
           P_{\alpha,d}(\tau)=((1+\rho\tau)\alpha,\ \tau d,\ \tau),
           \qquad d=\rho\beta.                              \tag{4.3}
\]

未使用时间依赖 flattening；被删除的前两个空间坐标不进入投影轴。

## 5. 保留原权的有限 representatives：没有免费 uniformization

原 $\alpha$ 网步长已经是 $s$。将 $d\in[r_0\rho,2r_0\rho)$ 分到长度恰为 $s$ 的二进对齐半开 bins。每 bin 恰含 $s/\delta=1/\rho$ 个原 $d$ 值。取 bin 中心 $d_j$，以 (4.3) 的 $d_j$ 为代表轴，并取固定倍 $s$ 半径确保包含所有 assigned 原投影管和 marks。

原 $a,b$ 完全作为原像 multiplicity 保留，每个 $(\alpha,d_j)$ 恰有相同数量原 indices。因此从 Uniform($\mathcal S_\rho$) pushforward 后的 representative weights **恰为均匀权**，不是另取独立或均匀样本。代表数

\[
 N_P=(r_0/s)(r_0\rho/s)=r_0^2\rho s^{-2}.                    \tag{5.1}
\]

对代表轴取 $\tau\in[0,1]$ 的完整固定长度段。它们的长度均为常数可比1；一次固定常数归一化即可使用通常单位长度管定义。所有容差、体积和密度只改固定常数。

每个代表任选 $d$ 最靠近 $d_j$ 的一条 assigned 原管，保留该原管 (3.3) 的全部 marks。投影小球可放入代表管，时间步长为 $s$，故每代表有 $\asymp s^{-1}$ 个标记球，各体积 $\asymp s^3$、重叠有界。于是

\[
                     \lambda(\mathcal P,Y)\asymp1.           \tag{5.2}
\]

整个操作都是原 marks 的舍入和选择，没有创造新的参与时间。

## 6. 实际 projected CF 与 union 的双边界

用 $D$ 表示均匀 representative 原权的 normalized convex Frostman 常数；固定有界 box 的体积只影响常数。

**下界。** 所有代表完整管均位于一个 $W$ 宽度 $C\rho$、其余轴固定有界的凸 slab 内，因 $s\ll\rho$，其体积 $O(\rho)$。该 slab 质量为1，所以

\[
                           D\gtrsim\rho^{-1}.                \tag{6.1}
\]

**上界。** 在 $\tau_*=1/4$，endpoint map

\[
    (\alpha,d_j)\mapsto((1+\rho/4)\alpha,d_j/4)
\]

为固定双 Lipschitz 变换。两个参数的网步长均为 $s$，范围宽度分别为常数与 $\asymp\rho$。若凸集 $U$ 含某些完整代表管，其 $\tau_*$ 截面包含这些 endpoints 的二维 $s$ 球；球重叠有界，故

\[
  \nu_{\mathcal P}(\mathcal P[U])
       \lesssim\frac{s^2\#\mathcal P[U]}{\rho}
       \lesssim\frac{\operatorname{Area}(U\cap\{\tau=\tau_*\})}{\rho}.
\]

若至少有一条管，$U$ 还含该管在 $\tau=3/4$ 的点。凸锥体积比较给截面积 $\lesssim\operatorname{Vol}_3(U)$。所以

\[
              D\lesssim\rho^{-1},\qquad D\asymp\rho^{-1}.    \tag{6.2}
\]

这是实际最优损失，明显小于原 packet 质量的粗 $p^{-1}=\rho^{-2}$，却仍是固定幂，不能藏成任意小的正则性损失。

全部 projected shading 落在同一个宽 $C\rho$ slab，给 union upper $O(\rho)$。反向，在 $\tau\in[1/4,1/2]$ 的共同 marks 上，上述二维 parameter grid 的映射统一双 Lipschitz；时间也是 $s$ 网。因此选出的 $\asymp N_Ps^{-1}$ 个原标记球重叠有固定上界，给

\[
 |U(\mathcal P,Y)|\asymp N_Ps^{-1}s^3\asymp\rho,
 \qquad \lambda/D\asymp\rho.                                \tag{6.3}
\]

这把局部投影 GWZ budget 的最坏成本落实为真直管、原权和真实原 marks 的有限计数，而非仅写一个可能不锐的条件化公式。

## 7. Slice-cover deficit 也不足以补救这个 transfer

固定任意 $0<\kappa_*<1$，可取二进序列 $\rho\asymp s^{\kappa_*}$、$\delta=\rho s$；例如 $\kappa_*=1/2$ 时取 $\delta=\rho^3,s=\rho^2$。$\kappa_*$ 在这里是**单尺度 cover 缺口指数**，不冒充源配置的真实 $\kappa$。

由 (4.2)，每共同时间的 hidden interval 在工作尺度的 cover 满足

\[
             N_s(Y_\tau)\asymp\rho/s
                     \asymp s^{-1+\kappa_*}.                 \tag{7.1}
\]

因此即使把这个 source-like slice-count upper 也列为待证 transfer 的输入，仍只有

\[
 D\asymp s^{-\kappa_*},\quad \lambda\asymp1,\quad
 |U|\asymp s^{\kappa_*},\quad \lambda/D\asymp s^{\kappa_*}.     \tag{7.2}
\]

任何声称自动给 $\lambda/D\gtrsim s^b$、固定 $b<\kappa_*$ 的推断均被否定。特别，GWZ 的额外 $s^\epsilon$ 不能与 (7.2) 及 $s^{\kappa_*}$ upper 产生矛盾：该损失恰好耗尽单尺度缺口。

若改在原完整时钟保留这些局部 marks，其密度为 $\rho$；若把时钟缩到单位长得到常数密度，则显式出现这里的 projected $D$。本构造没有证明这两种代价是所有实际 source packets 的最佳选择，也没有排除别的投影或合法多尺度机制。

## 8. 明确缺失的 source 假设，以及本轮停止位置

1. **没有真实的 $(1-\kappa)$-AD 薄集。** 归一后的 $Y_\tau$ 是长 $\asymp\rho$ 的 interval，在 $s$ 到 $\rho$ 之间为局部一维。若坚持总 cover (7.1) 的同一正指数 $1-\kappa_*$，在半径 $\rho$ 的球中已含整个 hidden 集，normalized Frostman 常数至少为 $\rho^{-(1-\kappa_*)}$。这是固定幂而非任意小误差；不是源给出的常数损失 AD。
2. **没有宏观的正指数方向 fibre。** 对 $t\ne0$，(2.4) 可逆，故一个精确点只在一条本族轴线上。在 $t\asymp\rho$，其逆映射的范数为 $O(\rho^{-2})$；所以通过同一 $\delta$ 点球的所有原管方向都落在直径 $O(\delta/\rho^2)=O(s/\rho)$ 的盒中。若其中标量方向集仍是 $\kappa$-AD、常数 $K$，结合尺度1的 cardinal lower 和尺度 $w=C\delta/\rho^2$ 的 upper 就必须有 $K^2\gtrsim w^{-\kappa}$。当 $\rho\asymp s^{\kappa_*}$、$0<\kappa_*<1$ 时这是固定幂损失，不能对任意小源 $\eta$ 保持 $K=\delta^{-\eta}$。相应的粗 ξ coherence 也未验证为源要求的次幂损失。
3. **不构成 Kakeya 反例。** 环境确有满方向，然而全局使用整管 shading 的 union 有固定正体积；局部 union 小只发生在原质量 $\rho^2$、原时间长度 $\rho$ 的真局部 packet，不能代替全局维数上界。

因此严格排除的是一个明确输入集合上的“自动 local transfer”，不是实际 mixed42 二次分支。主证明若要绕过本例，必须使用以上缺失的真实 source 结构或另一个已支付机制；不能仅由环境满方向、joint AD/CW、同一局部时间、局部满三 grain 和工作尺度 slice-cover 推出小 projected CF。本轮到此停止，不将该边界例重新命名成下一个主命题。
