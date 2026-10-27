# 可精确移植的一层：p-adic cap、单位管与条件极大估计

2026-10-27，root。固定奇素数p，O=Z_p，K=Q_p，Haar(O)=1，ψ标准conductor O。以下是自含的Fourier/概率计算，展示新欧氏证明的下游一层在p-adic里可工作，不是新的restriction定理，不认证尚未得到的核心输入。独立审查另存，未外部同行评审。

## 1. 选对曲率相位

取d≥1、n=d+1、Q(ξ)=Σ_(i=1)^d ξ_i²，定义复值extension

    Eg(x,t)=∫_(O^d) g(ξ) ψ(x·ξ+tQ(ξ))dξ， (x,t)∈K^d×K。

t在此是p-adic，不是径向半波测试的实时间；Q是K值多项式，不是实值||ξ||_p²。以q=n/(n−1)、s=2q=2n/d记分析指数，不与素数p混淆。

固定k≥1，δ=p^(−k)。符号δ只表实尺度；代数缩放始终明确用p^k或p^(−2k)，不把δ作为任意实数塞进K的加性character。

## 2. 精确cap积分，无渐近stationary phase

先取ξ0∈O^d、cap C=ξ0+p^kO^d。在|t|_p≤p^(2k)时，令ξ=ξ0+p^kz展开，相位为

    x·ξ0+tQ(ξ0)+p^k(x+2tξ0)·z+t p^(2k)Q(z)。

最后一项在O，ψ恒为1。Haar正交性直接给

    E1_C(x,t)=δ^d ψ(x·ξ0+tQ(ξ0))
      ·1_{x+2tξ0∈p^(−k)O^d}。                         (2.1)

所以它在时间长度尺度p^(2k)、横宽p^k的长管上常模。这里没有虚平移、高斯或椭圆方程，packet是character积分的精确结果。

取不同的ξ_j∈O^d/p^kO^d、任意中心b_j=(b_x,j,b_t,j)∈O^n，并定义单位管

    T_j={Y=(y,τ)∈O^n:
          y−b_x,j+2(τ−b_t,j)ξ_j∈p^kO^d}。

等价地T_j=b_j+O(−2ξ_j,1)+p^kO^n，体积恰δ^d，物理方向是实际primitive向量(−2ξ_j,1)。奇p保证2是unit，故不同ξ_j mod p^k给该方向chart中的δ分离。所有管和所有原权重保留，无删管损失。

对C_j=ξ_j+p^kO^d取模调

    g_j(ξ)=1_Cj(ξ)ψ(−p^(−2k)[b_x,j·ξ+b_t,j Q(ξ)])。

在Y∈O^n中，按(2.1)或直接展开可得

    |E g_j(p^(−2k)Y)|=δ^d 1_Tj(Y)。                    (2.2)

Haar缩放为d(p^(−2k)Y)=δ^(−2n)dY，后文不能漏去这个Jacobian。对p=2可另作常数尺度调整，但本稿不预认证该补充。

## 3. 明确假设尚未得到的restriction输入

假设对所有g∈L^s(O^d)有同一个常数A_k：

    ||Eg||_{L^s(p^(−2k)O^n)} ≤ A_k ||g||_{L^s(O^d)}。  (3.1)

这是本桥的输入，不是从原欧氏结果自动推出的结论。给出A_k的平凡大幂上界不解决关键问题；有用的目标是subpower或poly(k)增长。已有Kakeya估计也不能把(3.1)反向推出。

## 4. 同一随机符号论证确可使用

给任意a_j≥0，独立Rademacher符号ε_j，令g_ε=Σ ε_j a_j^(1/2)g_j。cap不交，故

    ||g_ε||_s^s=δ^d Σ a_j^q。

由s≥2及Jensen/二阶正交性，逐Y有

    E_ε |Eg_ε(p^(−2k)Y)|^s
      ≥(Σ a_j|Eg_j(p^(−2k)Y)|²)^q
      =δ^(ds)(Σ a_j1_Tj(Y))^q。

积分、支付Haar缩放后用(3.1)：

    δ^(ds)∫_(O^n)(Σ a_j1_Tj)^q
      ≤δ^(2n) A_k^s δ^d Σ a_j^q。

临界关系ds=2n恰好消去缩放费用，所以

    ||Σ a_j1_Tj||_{L^q(O^n)}
      ≤A_k² (δ^d Σ a_j^q)^(1/q)。                     (4.1)

这一步保每一原tube/中心和任意权重；没有把相关几何替换成iid方向。随机独立的只是人工符号，作用是恒等恢复平方和。

## 5. 对偶得到单chart极大估计

对f∈L^n(O^n)，定义

    M_k f(ξ)=sup_(b∈O^n) δ^(−d)∫_(T_{ξ,b})|f|。

管仅依b和ξ的mod p^k数据，故sup在有限族上取到；M_k在方向cap上常值。方向chart的Haar测度是O^d的概率测度，离散权为δ^d。

取δ^dΣ a_j^q=1，对每个ξ_j选达到sup的原中心。因为|T|=δ^d，

    δ^d Σ a_j M_k f(ξ_j)
      =∫_(O^n)|f| Σ a_j1_Tj
      ≤||f||_n ||Σ a_j1_Tj||_q ≤A_k²||f||_n。

有限维L^n–L^q对偶给

    ||M_k f||_{L^n(O^d)}≤A_k²||f||_{L^n(O^n)}。         (5.1)

若对每个ε>0先有A_k≤C_ε δ^(−ε)，取输入ε/2即可给通常每ε损失的chart maximal。若A_k≤C(1+k)^β，则输出≤C²(1+k)^(2β)。全projective方向可按某坐标unit分有限chart，另付固定chart/Haar比较；本稿的严格公式是已定义的单chart版本，不免费改计方向measure或声最优常数。

## 6. 对‘能否同样方法’的真实回答范围

Fourier caps→原生p-adic tubes→随机符号→Hölder/对偶的下游结构确实能移植，且比欧氏近似更精确。这与Hickman–Wright对rings/local fields中restriction和Kakeya联系的框架一致；不以此声新的结构定理或重大成果。

尚未移植的是产生临界(3.1)的核心正能量/PDE。本文没有把未知A_k埋成成功假设，也没有由已知maximal推出restriction。实时间径向模型的单壳反攻亦不反本多项式相位模型。两者合起来说明：应当保留可用的傅里叶和管层，重新设计与曲率character相容的能量，而不是将欧氏符号逐字换域。
